from datetime import datetime
import sys
import os


from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QMessageBox, QProgressBar, QDialog, QLabel, QVBoxLayout
)
from PyQt5.QtCore import QTimer

# internal
from src.interface import Ui_MainWindow
from src import settings
from src import tools


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.numberSpinBox.setMaximum(1000000000)

        # btn connection
        self.ui.numberConfirmButton.clicked.connect(lambda: self.patcher('number'))
        self.ui.phonenumberConfirmButton.clicked.connect(lambda: self.patcher('star'))

        # comboBox data
        prefix_data = tools.read_prefix_from_csv(settings.CSV_FILE)
        self.ui.prefixComboBox.addItems(prefix_data)

        # configs
        self.configs = settings.JsonConfigHandler(settings.PREFIXES_FILE)
        self.configs.load_config()

    def patcher(self, which_func):
        if which_func == 'number':
            diff_time = self.loop_adjuster()
        else:
            diff_time = self.process_from_star()
        self.success_message('Successfully phone number created at {}'.format(diff_time))

    @tools.func_runtime
    def loop_adjuster(self):
        # Get data from app
        number = self.ui.numberSpinBox.value()
        prefix = self.ui.prefixComboBox.currentText()

        range_val = 100000
        divide_num = tools.divide_number(number, range_val)

        # set progress bar
        progress_bar = ProgressBarDialog('processing...', divide_num[0] + 1)
        progress_bar.start_progress()
        # progress_bar.exec_()

        for index in range(divide_num[0]):
            addition_name = f'Item {index}'
            self._process_from_number(range_val, prefix, addition_name)
            progress_bar.update_progress()

        # remaining numbers
        if divide_num[1]:
            addition_name = f'last item'
            self._process_from_number(divide_num[1], prefix, addition_name)

    @tools.clear_ram
    def _process_from_number(self, number, prefix, addition_name):

        excel_filename = self.filename_by_time(addition_name, prefix)
        excel = self.excel_initialize(excel_filename)

        raw_phonenumber = self.configs.get_config(prefix)

        if not int(raw_phonenumber):
            raw_phonenumber = '0000000'
            excel.write_data(prefix + raw_phonenumber)

        for i in range(number):
            if raw_phonenumber.startswith('0'):
                raw_phonenumber = tools.under_one_generator(raw_phonenumber)
                main_phonenumber = prefix + raw_phonenumber
                excel.write_data(main_phonenumber)
            else:
                raw_phonenumber = tools.general_generator(raw_phonenumber)
                main_phonenumber = prefix + raw_phonenumber
                if len(main_phonenumber) > 11:
                    return self.success_message('All phonenumber of this prefix created!')

                excel.write_data(main_phonenumber)

        excel.save_workbook()
        excel.close_workbook()
        self.configs.set_config(prefix, raw_phonenumber)
        self.configs.save_config()

    @tools.func_runtime
    @tools.clear_ram
    def process_from_star(self):
        phonenumber = self.ui.phonenumberLineEdit.text()
        if not tools.check_format(phonenumber):
            self.error_message('Phone Number Format Invalid!')
            self.ui.phonenumberLineEdit.clear()
            return

        excel_filename = self.filename_by_time(phonenumber)
        excel = self.excel_initialize(excel_filename)

        counter = 0
        list_of_stars_index = []
        for index, i in enumerate(phonenumber):
            if i == '*':
                list_of_stars_index.append(index)
                counter += 1

        nums = '0' * counter
        correct_phonenumber = tools.replace_nums(phonenumber, nums, list_of_stars_index)
        excel.write_data(correct_phonenumber)

        while True:
            if nums.startswith('0'):
                nums = tools.under_one_generator(nums)
            else:
                nums = tools.general_generator(nums)
            if len(nums) != counter:
                break

            correct_phonenumber = tools.replace_nums(phonenumber, nums, list_of_stars_index)
            excel.write_data(correct_phonenumber)

        excel.save_workbook()
        excel.close_workbook()

    @staticmethod
    def excel_initialize(filename):
        excel = settings.ExcelHandler(filename)
        excel.create_workbook()
        excel.set_column_title(settings.COLUMN_TITLE)
        excel.save_workbook()
        return excel

    @staticmethod
    def filename_by_time(addition_name, prefix: str = None):
        # time
        current_datetime = datetime.now()

        # Excel configuration
        if not prefix:
            excel_filename = os.path.join(
                settings.BASE_DIR,
                settings.docs_folder,
                settings.star_folder,
                f'{current_datetime.strftime("%Y-%m-%d %H-%M-%S")} {addition_name.replace("*", "X")}.{settings.EXCEL_SUFFIX}'
            )
        else:
            excel_filename = os.path.join(
                settings.BASE_DIR,
                settings.docs_folder,
                settings.number_folder,
                prefix,
                f'{current_datetime.strftime("%Y-%m-%d %H-%M-%S")} {addition_name}.{settings.EXCEL_SUFFIX}'
            )

        return excel_filename

    def error_message(self, msg):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle('Error')
        error_box.setText(msg)
        error_box.setStandardButtons(QMessageBox.Ok)
        error_box.setGeometry(self.x() + 50, self.y() + 50, 300, 150)
        error_box.exec_()

    def success_message(self, msg):
        # Create a success message box
        success_box = QMessageBox()
        success_box.setIcon(QMessageBox.Information)
        success_box.setWindowTitle('Success')
        success_box.setText(msg)
        success_box.setStandardButtons(QMessageBox.Ok)

        # Set the position of the success box relative to the main window
        success_box.setGeometry(self.x() + 50, self.y() + 50, 300, 150)

        # Show the success message box
        success_box.exec_()


class ProgressBarDialog(QDialog):
    def __init__(self, message, stop: int):
        super(ProgressBarDialog, self).__init__()

        self.init_ui(message, stop)

    def init_ui(self, message, stop: int):
        self.setWindowTitle('Progress Bar')
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, stop)

        self.label = QLabel(message, self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.progress_bar)

    def set_progress(self, value):
        self.progress_bar.setValue(value)

    def start_progress(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)

    def update_progress(self):
        current_value = self.progress_bar.value()
        new_value = current_value + 1
        if new_value <= self.progress_bar.maximum():
            self.set_progress(new_value)
        else:
            self.timer.stop()
            self.accept()

    def close_progress(self):
        self.reject()


if __name__ == '__main__':
    configs = settings.JsonConfigHandler()
    if not os.path.exists(settings.CONFIG_FILE):
        from src import setup

    configs.load_config()

    if not configs.get_config('setup-run'):
        from src import setup

    configs.save_config()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
