# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\MainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 280, 971, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 310, 951, 341))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 110, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 190, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(160, 40, 801, 31))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 190, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label1_2.setGeometry(QtCore.QRect(20, 100, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 20, 971, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.SpinBox_X_6 = QtWidgets.QDoubleSpinBox(self.frame)
        self.SpinBox_X_6.setGeometry(QtCore.QRect(320, 90, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SpinBox_X_6.setFont(font)
        self.SpinBox_X_6.setSuffix("")
        self.SpinBox_X_6.setDecimals(0)
        self.SpinBox_X_6.setMinimum(0.0)
        self.SpinBox_X_6.setMaximum(360.0)
        self.SpinBox_X_6.setSingleStep(5.0)
        self.SpinBox_X_6.setProperty("value", 0.0)
        self.SpinBox_X_6.setObjectName("SpinBox_X_6")
        self.SpinBox_X_7 = QtWidgets.QDoubleSpinBox(self.frame)
        self.SpinBox_X_7.setGeometry(QtCore.QRect(530, 90, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SpinBox_X_7.setFont(font)
        self.SpinBox_X_7.setSuffix("")
        self.SpinBox_X_7.setDecimals(0)
        self.SpinBox_X_7.setMinimum(0.0)
        self.SpinBox_X_7.setMaximum(360.0)
        self.SpinBox_X_7.setSingleStep(5.0)
        self.SpinBox_X_7.setProperty("value", 360.0)
        self.SpinBox_X_7.setObjectName("SpinBox_X_7")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(10, 50, 951, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label1_4 = QtWidgets.QLabel(self.frame)
        self.label1_4.setGeometry(QtCore.QRect(200, 80, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label1_4.setFont(font)
        self.label1_4.setObjectName("label1_4")
        self.label1_5 = QtWidgets.QLabel(self.frame)
        self.label1_5.setGeometry(QtCore.QRect(410, 80, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label1_5.setFont(font)
        self.label1_5.setObjectName("label1_5")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(180, 70, 20, 71))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(590, 70, 20, 71))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(740, 70, 20, 71))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.SpinBox_X_8 = QtWidgets.QDoubleSpinBox(self.frame)
        self.SpinBox_X_8.setGeometry(QtCore.QRect(870, 90, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SpinBox_X_8.setFont(font)
        self.SpinBox_X_8.setSuffix("")
        self.SpinBox_X_8.setDecimals(0)
        self.SpinBox_X_8.setMinimum(1800.0)
        self.SpinBox_X_8.setMaximum(2050.0)
        self.SpinBox_X_8.setSingleStep(1.0)
        self.SpinBox_X_8.setProperty("value", 2000.0)
        self.SpinBox_X_8.setObjectName("SpinBox_X_8")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(660, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label1_3 = QtWidgets.QLabel(self.centralwidget)
        self.label1_3.setGeometry(QtCore.QRect(610, 100, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label1_3.setFont(font)
        self.label1_3.setObjectName("label1_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 160, 951, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label1_6 = QtWidgets.QLabel(self.centralwidget)
        self.label1_6.setGeometry(QtCore.QRect(760, 100, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label1_6.setFont(font)
        self.label1_6.setObjectName("label1_6")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(290, 180, 21, 101))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 200, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label1_7 = QtWidgets.QLabel(self.centralwidget)
        self.label1_7.setGeometry(QtCore.QRect(20, 200, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label1_7.setFont(font)
        self.label1_7.setObjectName("label1_7")
        self.frame.raise_()
        self.groupBox.raise_()
        self.textEdit.raise_()
        self.comboBox.raise_()
        self.pushButton_2.raise_()
        self.listWidget.raise_()
        self.label1.raise_()
        self.pushButton_3.raise_()
        self.label1_2.raise_()
        self.comboBox_3.raise_()
        self.label1_3.raise_()
        self.line_2.raise_()
        self.label1_6.raise_()
        self.line_6.raise_()
        self.comboBox_2.raise_()
        self.label1_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScrapIBANDL"))
        self.groupBox.setTitle(_translate("MainWindow", "Status"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.comboBox.setCurrentText(_translate("MainWindow", "EBS"))
        self.comboBox.setItemText(0, _translate("MainWindow", "EBS"))
        self.comboBox.setItemText(1, _translate("MainWindow", "NRA"))
        self.comboBox.setItemText(2, _translate("MainWindow", "PIGE"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ALL"))
        self.pushButton_2.setText(_translate("MainWindow", "Scrap"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label1.setText(_translate("MainWindow", "Destination"))
        self.pushButton_3.setText(_translate("MainWindow", "Update SIMNRA"))
        self.label1_2.setText(_translate("MainWindow", "Data"))
        self.label1_4.setText(_translate("MainWindow", "Theta_min"))
        self.label1_5.setText(_translate("MainWindow", "Theta_max"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "mb"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "yield"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "rr"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "tot"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "all"))
        self.label1_3.setText(_translate("MainWindow", "Unit"))
        self.label1_6.setText(_translate("MainWindow", "Year_min"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "Chrome"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Chrome"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Firefox"))
        self.label1_7.setText(_translate("MainWindow", "Browser"))

