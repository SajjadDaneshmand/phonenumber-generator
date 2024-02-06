from datetime import datetime
import subprocess
import sys
import os


from PyQt5.QtWidgets import (
    QMainWindow, QApplication
)
from PyQt5.uic import loadUi

# internal
from src.interface import Ui_MainWindow
from src.alerts import *
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
        self.ui.addPrefixMenubar.triggered.connect(lambda: self.prefix_patcher('add'))
        self.ui.deletePrefixMenubar.triggered.connect(lambda: self.prefix_patcher('delete'))

        # comboBox data
        prefix_data = tools.read_prefix_from_csv(settings.CSV_FILE)
        self.ui.prefixComboBox.addItems(prefix_data)

        # configs
        self.configs = settings.JsonConfigHandler(settings.PREFIXES_FILE)
        self.configs.load_config()

        # Alerts
        self.alerts = Alerts()

    def patcher(self, which_func):
        # set message window on a main window
        self.alerts.message_box.setGeometry(self.x() + 50, self.y() + 50, 300, 150)

        if which_func == 'number':
            diff_time = self.loop_adjuster()
        else:
            diff_time = self.process_from_star()
        return self.alerts.info('success', 'Successfully phone number created at {}'.format(diff_time))

    @tools.func_runtime
    def loop_adjuster(self):
        # set message window on a main window
        self.alerts.message_box.setGeometry(self.x() + 50, self.y() + 50, 300, 150)

        # Get data from app
        number = self.ui.numberSpinBox.value()
        prefix = self.ui.prefixComboBox.currentText()

        range_val = 100000
        divide_num = tools.divide_number(number, range_val)

        for index in range(divide_num[0]):
            addition_name = f'Item {index}'
            self._process_from_number(range_val, prefix, addition_name)

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
                    return self.alerts.info('success', 'All phonenumber of this prefix created!')

                excel.write_data(main_phonenumber)

        excel.save_workbook()
        excel.close_workbook()
        self.configs.set_config(prefix, raw_phonenumber)
        self.configs.save_config()

    @tools.func_runtime
    @tools.clear_ram
    def process_from_star(self):
        # set message window on a main window
        self.alerts.message_box.setGeometry(self.x() + 50, self.y() + 50, 300, 150)

        phonenumber = self.ui.phonenumberLineEdit.text()
        if not tools.check_format(phonenumber):
            self.alerts.error_message('Phone Number Format Invalid!')
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

    def prefix_patcher(self, ctype):
        # add prefix instance
        prefix_instance = AddPrefixWindow(ctype)

        prefix_instance.setGeometry(self.x() + 50, self.y() + 50, 300, 150)
        prefix_instance.exec_()
        self.restart_app()

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

    @staticmethod
    def restart_app():
        python = sys.executable
        subprocess.Popen([python] + sys.argv)
        sys.exit()


class AddPrefixWindow(QDialog):
    def __init__(self, ctype):
        super().__init__()
        loadUi(settings.ADD_PREFIX_UI, self)
        self.ctype = ctype

        # connect btn
        self.checkButtonBox.accepted.connect(self.patcher)
        self.checkButtonBox.rejected.connect(self._close_window)

        # list of prefix
        self.prefix_list = tools.read_prefix_from_csv(settings.CSV_FILE)

        # This variable is for get data from Line Edit
        self.line_text = None

        # Set config to json file
        self.prefix_conf = settings.JsonConfigHandler(settings.PREFIXES_FILE)
        self.prefix_conf.load_config()

        # Alerts
        self.alerts = Alerts()

    def patcher(self):
        if self.ctype == 'add':
            return self.set_prefix()
        else:
            return self.delete_config()

    def set_prefix(self):
        # Set the position of the success box relative to the main window
        self.alerts.message_box.setGeometry(self.x() + 50, self.y() + 50, 300, 150)

        # Get data from line edit
        self.line_text = self.prefixLineEdit.text()

        # Check prefix validation
        if not tools.check_prefix(self.line_text):
            return self.alerts.error_message("Your prefix is not valid!")

        # check if prefix exists, don't do anything
        if not self._prefix_exist():
            return self.prefixLineEdit.clear()

        # Set config to csv file
        tools.to_csv(settings.CSV_FILE, self.line_text)

        # add prefix to json file
        if self.line_text in self.prefix_conf.config:
            return self.prefixLineEdit.clear()

        self.prefix_conf.set_config(self.line_text, 0)
        self.prefix_conf.save_config()

        # clear line edit
        return self.prefixLineEdit.clear()

    def delete_config(self):
        # Set the position of the success box relative to the main window
        self.alerts.message_box.setGeometry(self.x() + 50, self.y() + 50, 300, 150)

        # Get data from line edit
        self.line_text = self.prefixLineEdit.text()

        # Check prefix validation
        if not tools.check_prefix(self.line_text):
            return self.alerts.error_message("Your prefix is not valid!")

        # check if prefix exists, don't do anything
        if not self._prefix_exist():
            return self.prefixLineEdit.clear()

        tools.del_from_csv(settings.CSV_FILE, self.line_text)
        return self.prefixLineEdit.clear()

    def _prefix_exist(self):
        if self.line_text in self.prefix_list:
            return True
        return False

    def _close_window(self):
        self.close()


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
