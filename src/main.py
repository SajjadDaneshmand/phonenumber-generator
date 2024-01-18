from datetime import datetime
import sys
import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

# internal
from interface import Ui_MainWindow
import settings
import tools


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.numberSpinBox.setMaximum(1000000000)

        # btn connection
        self.ui.numberConfirmButton.clicked.connect(self.process_from_number)
        self.ui.phonenumberConfirmButton.clicked.connect(self.process_from_star)

        # comboBox data
        prefix_data = tools.read_prefix_from_csv(settings.CSV_FILE)
        self.ui.prefixComboBox.addItems(prefix_data)

        # configs
        self.configs = settings.JsonConfigHandler(settings.PREFIXES_FILE)
        self.configs.load_config()

    def process_from_number(self):
        # Get data from app
        number = self.ui.numberSpinBox.value()
        prefix = self.ui.prefixComboBox.currentText()

        # time
        current_datetime = datetime.now()

        # Excel configuration
        excel_filename = os.path.join(
            settings.BASE_DIR,
            settings.docs_folder,
            settings.number_folder,
            prefix,
            f'{current_datetime.strftime("%Y-%m-%d %H-%M-%S")}.{settings.EXCEL_SUFFIX}'
        )

        excel = settings.ExcelHandler(excel_filename)
        excel.create_workbook()
        excel.set_column_title(settings.COLUMN_TITLE)

        raw_phonenumber = self.configs.get_config(prefix)

        if not int(raw_phonenumber):
            raw_phonenumber = '0000000'
            excel.write_data(prefix + raw_phonenumber)

        for i in range(number):
            if raw_phonenumber.startswith('0'):
                raw_phonenumber = tools.under_one_generator(raw_phonenumber)
                excel.write_data(prefix + raw_phonenumber)
            else:
                raw_phonenumber = tools.general_generator(raw_phonenumber)
                excel.write_data(prefix + raw_phonenumber)
        excel.save_workbook()
        excel.close_workbook()
        self.configs.set_config(prefix, raw_phonenumber)
        self.configs.save_config()
        self.success_message('Successfully phone number created!')

    def process_from_star(self):
        phonenumber = self.ui.phonenumberLineEdit.text()
        if not tools.check_format(phonenumber):
            self.error_message('Phone Number Format Invalid!')
            self.ui.phonenumberLineEdit.clear()
            return

        # time
        current_datetime = datetime.now()

        # Excel configuration
        excel_filename = os.path.join(
            settings.BASE_DIR,
            settings.docs_folder,
            settings.star_folder,
            f'{current_datetime.strftime("%Y-%m-%d %H-%M-%S")} {phonenumber}.{settings.EXCEL_SUFFIX}'
        )
        excel = settings.ExcelHandler(excel_filename)
        excel.create_workbook()
        excel.set_column_title(settings.COLUMN_TITLE)

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
        self.success_message('Successfully phone number created!')

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


if __name__ == '__main__':
    configs = settings.JsonConfigHandler()
    if not os.path.exists(settings.CONFIG_FILE):
        import setup

    configs.load_config()

    if not configs.get_config('setup-run') == 'true':
        import setup

    configs.load_config()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
