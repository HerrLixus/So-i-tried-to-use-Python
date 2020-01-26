from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_Form
app = QtWidgets.QApplication(sys.argv)

field = ['', '', '', '', '', '', '', '', '']
flag = 1

Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


def cell():
    global flag
    if flag % 2 == 1 and ui.pushButton.text() == '':
        ui.pushButton.setText("X")
        field[0] = "X"
    elif ui.pushButton.text() == '':
        ui.pushButton.setText("O")
        field[0] = "O"
    flag += 1
    wincheck()


def cell2():
    global flag
    if flag % 2 == 1 and ui.pushButton_2.text() == '':
        ui.pushButton_2.setText("X")
        field[1] = "X"
    elif ui.pushButton_2.text() == '':
        ui.pushButton_2.setText("O")
        field[1] = "O"
    flag += 1
    wincheck()


def cell3():
    global flag
    if flag % 2 == 1 and ui.pushButton_3.text() == '':
        ui.pushButton_3.setText("X")
        field[2] = "X"
    elif ui.pushButton_3.text() == '':
        ui.pushButton_3.setText("O")
        field[2] = "O"
    flag += 1
    wincheck()


def cell4():
    global flag
    if flag % 2 == 1 and ui.pushButton_4.text() == '':
        ui.pushButton_4.setText("X")
        field[3] = "X"
    elif ui.pushButton_4.text() == '':
        ui.pushButton_4.setText("O")
        field[3] = "O"
    flag += 1
    wincheck()


def cell5():
    global flag
    if flag % 2 == 1 and ui.pushButton_5.text() == '':
        ui.pushButton_5.setText("X")
        field[4] = "X"
    elif ui.pushButton_5.text() == '':
        ui.pushButton_5.setText("O")
        field[4] = "O"
    flag += 1
    wincheck()


def cell6():
    global flag
    if flag % 2 == 1 and ui.pushButton_6.text() == '':
        ui.pushButton_6.setText("X")
        field[5] = "X"
    elif ui.pushButton_6.text() == '':
        ui.pushButton_6.setText("O")
        field[5] = "O"
    flag += 1
    wincheck()


def cell7():
    global flag
    if flag % 2 == 1 and ui.pushButton_7.text() == '':
        ui.pushButton_7.setText("X")
        field[6] = "x"
    elif ui.pushButton_7.text() == '':
        ui.pushButton_7.setText("O")
        field[6] = "O"
    flag += 1
    wincheck()


def cell8():
    global flag
    if flag % 2 == 1 and ui.pushButton_8.text() == '':
        ui.pushButton_8.setText("X")
        field[7] = "X"
    elif ui.pushButton_8.text() == '':
        ui.pushButton_8.setText("O")
        field[7] = "O"
    flag += 1
    wincheck()


def cell9():
    global flag
    if flag % 2 == 1 and ui.pushButton_9.text() == '':
        ui.pushButton_9.setText("X")
        field[8] = "X"
    elif ui.pushButton_9.text() == '':
        ui.pushButton_9.setText("O")
        field[8] = "O"
    flag += 1
    wincheck()


ui.pushButton.clicked.connect(cell)
ui.pushButton_2.clicked.connect(cell2)
ui.pushButton_3.clicked.connect(cell3)
ui.pushButton_4.clicked.connect(cell4)
ui.pushButton_5.clicked.connect(cell5)
ui.pushButton_6.clicked.connect(cell6)
ui.pushButton_7.clicked.connect(cell7)
ui.pushButton_8.clicked.connect(cell8)
ui.pushButton_9.clicked.connect(cell9)
print(field)
wins = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]]
count = 0


def wincheck():
    global wins
    global field
    global count
    global flag
    for i in wins:
        if field[i[0]] == field[i[1]] == field[i[2]] != '' or flag == 10:
            sys.exit()


sys.exit(app.exec_())
