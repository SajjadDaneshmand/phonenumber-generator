# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 257)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.numberTab = QtWidgets.QWidget()
        self.numberTab.setObjectName("numberTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.numberTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.numberTab)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.numberLabel = QtWidgets.QLabel(self.widget)
        self.numberLabel.setObjectName("numberLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.numberLabel)
        self.numberSpinBox = QtWidgets.QSpinBox(self.widget)
        self.numberSpinBox.setObjectName("numberSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numberSpinBox)
        self.prefixComboBox = QtWidgets.QComboBox(self.widget)
        self.prefixComboBox.setObjectName("prefixComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.prefixComboBox)
        self.prefixLabel = QtWidgets.QLabel(self.widget)
        self.prefixLabel.setObjectName("prefixLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.prefixLabel)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.numberTab)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.numberConfirmButton = QtWidgets.QPushButton(self.widget_2)
        self.numberConfirmButton.setObjectName("numberConfirmButton")
        self.horizontalLayout_3.addWidget(self.numberConfirmButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.widget_2)
        self.tabWidget.addTab(self.numberTab, "")
        self.autoCompeleteTab = QtWidgets.QWidget()
        self.autoCompeleteTab.setObjectName("autoCompeleteTab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.autoCompeleteTab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_5 = QtWidgets.QWidget(self.autoCompeleteTab)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.formLayout_3 = QtWidgets.QFormLayout(self.widget_6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.phonenumberLabel = QtWidgets.QLabel(self.widget_6)
        self.phonenumberLabel.setObjectName("phonenumberLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.phonenumberLabel)
        self.phonenumberLineEdit = QtWidgets.QLineEdit(self.widget_6)
        self.phonenumberLineEdit.setObjectName("phonenumberLineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.phonenumberLineEdit)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.phonenumberConfirmButton = QtWidgets.QPushButton(self.widget_7)
        self.phonenumberConfirmButton.setObjectName("phonenumberConfirmButton")
        self.horizontalLayout_6.addWidget(self.phonenumberConfirmButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.horizontalLayout_5.addWidget(self.widget_5)
        self.tabWidget.addTab(self.autoCompeleteTab, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 22))
        self.menubar.setObjectName("menubar")
        self.menusettings = QtWidgets.QMenu(self.menubar)
        self.menusettings.setObjectName("menusettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.addPrefixMenubar = QtWidgets.QAction(MainWindow)
        self.addPrefixMenubar.setObjectName("addPrefixMenubar")
        self.deletePrefixMenubar = QtWidgets.QAction(MainWindow)
        self.deletePrefixMenubar.setObjectName("deletePrefixMenubar")
        self.menusettings.addAction(self.addPrefixMenubar)
        self.menusettings.addAction(self.deletePrefixMenubar)
        self.menubar.addAction(self.menusettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.numberLabel.setText(_translate("MainWindow", "Number:"))
        self.prefixLabel.setText(_translate("MainWindow", "Prefix:"))
        self.numberConfirmButton.setText(_translate("MainWindow", "Confirm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.numberTab), _translate("MainWindow", "Tab 1"))
        self.phonenumberLabel.setText(_translate("MainWindow", "Phone Number:"))
        self.phonenumberConfirmButton.setText(_translate("MainWindow", "Confirm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.autoCompeleteTab), _translate("MainWindow", "Page"))
        self.menusettings.setTitle(_translate("MainWindow", "settings"))
        self.addPrefixMenubar.setText(_translate("MainWindow", "add prefix"))
        self.deletePrefixMenubar.setText(_translate("MainWindow", "delete prefix"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
