# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TicTacToe.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(213, 199)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(-10, 60, 311, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(-23, 130, 341, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(60, -10, 20, 361))
        self.line_3.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(140, -10, 20, 341))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"font-size: 36px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 0, 81, 71))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"font-size: 36px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 0, 71, 71))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"font-size: 36px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 70, 71, 71))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"font-size: 36px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 70, 81, 71))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"font-size: 36px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 70, 71, 71))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"font-size: 36px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}\n"
"")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 140, 71, 71))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"font-size: 36px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}\n"
"")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 140, 81, 71))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"font-size: 36px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}\n"
"")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 140, 71, 71))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"font-size: 36px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}\n"
"")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.line_2.raise_()
        self.line.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.line_4.raise_()
        self.line_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
