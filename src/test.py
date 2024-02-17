import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QFrame


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create two vertical layouts
        top_layout = QVBoxLayout()
        bottom_layout = QVBoxLayout()

        # Create a checkbox
        checkbox = QCheckBox("My Checkbox")

        # Add the checkbox to the top layout
        top_layout.addWidget(checkbox)

        # Add widgets to the top layout (You can add more widgets here)
        # top_layout.addWidget(another_widget)

        # Add widgets to the bottom layout (You can add more widgets here)
        # bottom_layout.addWidget(another_widget)

        # Set main layout as a vertical layout
        main_layout = QVBoxLayout()

        # Add the top layout to the main layout
        main_layout.addLayout(top_layout)

        # Add a separator (QFrame) between the two layouts
        separator_line = self.create_separator_line()
        main_layout.addWidget(separator_line)

        # Add the bottom layout to the main layout
        main_layout.addLayout(bottom_layout)

        # Set the main layout for the main window
        self.setLayout(main_layout)

        self.setWindowTitle("PyQt Checkbox Between Two Layouts")
        self.setGeometry(100, 100, 400, 300)

    def create_separator_line(self):
        # Create a horizontal line (QFrame) to act as a separator between layouts
        line = self.line = self.create_line()
        return line

    def create_line(self):
        # Create a horizontal line (QFrame)
        line = self.line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        return line

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
