from PyQt5.QtWidgets import QMessageBox, QDialog


class Alerts(QDialog):
    def __init__(self):
        super().__init__()
        self.message_box = QMessageBox()

    def info(self, title, msg):
        # Create a success message box
        self.message_box.setIcon(QMessageBox.Information)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(msg)
        self.message_box.setStandardButtons(QMessageBox.Ok)

        # show window
        self.message_box.exec_()

    def error_message(self, msg):
        self.message_box.setIcon(QMessageBox.Critical)
        self.message_box.setWindowTitle('Error')
        self.message_box.setText(msg)
        self.message_box.setStandardButtons(QMessageBox.Ok)

        # show window
        self.message_box.exec_()
