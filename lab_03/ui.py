# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab03.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(QtCore.QSize(1020, 630))
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 0, 711, 601))
        self.graphicsView.setObjectName("graphicsView")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(730, 0, 281, 31))
        self.label1.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setWordWrap(False)
        self.label1.setObjectName("label1")
        self.label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label1_2.setGeometry(QtCore.QRect(730, 30, 281, 21))
        self.label1_2.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_2.setObjectName("label1_2")
        self.label1_3 = QtWidgets.QLabel(self.centralwidget)
        self.label1_3.setGeometry(QtCore.QRect(730, 50, 31, 21))
        self.label1_3.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_3.setObjectName("label1_3")
        self.label1_4 = QtWidgets.QLabel(self.centralwidget)
        self.label1_4.setGeometry(QtCore.QRect(870, 50, 31, 21))
        self.label1_4.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_4.setObjectName("label1_4")
        self.label1_5 = QtWidgets.QLabel(self.centralwidget)
        self.label1_5.setGeometry(QtCore.QRect(730, 70, 281, 21))
        self.label1_5.setStyleSheet("background-color: rgb(140, 209, 255)")
        self.label1_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_5.setObjectName("label1_5")
        self.label1_6 = QtWidgets.QLabel(self.centralwidget)
        self.label1_6.setGeometry(QtCore.QRect(730, 90, 31, 21))
        self.label1_6.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label1_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_6.setObjectName("label1_6")
        self.label1_7 = QtWidgets.QLabel(self.centralwidget)
        self.label1_7.setGeometry(QtCore.QRect(870, 90, 31, 21))
        self.label1_7.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label1_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_7.setObjectName("label1_7")
        self.label1_8 = QtWidgets.QLabel(self.centralwidget)
        self.label1_8.setGeometry(QtCore.QRect(730, 110, 55, 21))
        self.label1_8.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label1_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_8.setObjectName("label1_8")
        self.label1_9 = QtWidgets.QLabel(self.centralwidget)
        self.label1_9.setGeometry(QtCore.QRect(730, 130, 111, 21))
        self.label1_9.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label1_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_9.setObjectName("label1_9")
        self.push1 = QtWidgets.QPushButton(self.centralwidget)
        self.push1.setGeometry(QtCore.QRect(800, 160, 131, 28))
        self.push1.setStyleSheet("background-color: rgb(255, 145, 135);")
        self.push1.setObjectName("push1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(730, 200, 281, 31))
        self.label2.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.label2_1 = QtWidgets.QLabel(self.centralwidget)
        self.label2_1.setGeometry(QtCore.QRect(730, 270, 111, 21))
        self.label2_1.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label2_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_1.setObjectName("label2_1")
        self.label2_2 = QtWidgets.QLabel(self.centralwidget)
        self.label2_2.setGeometry(QtCore.QRect(730, 290, 111, 21))
        self.label2_2.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_2.setObjectName("label2_2")
        self.label2_4 = QtWidgets.QLabel(self.centralwidget)
        self.label2_4.setGeometry(QtCore.QRect(730, 330, 111, 21))
        self.label2_4.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_4.setObjectName("label2_4")
        self.push2 = QtWidgets.QPushButton(self.centralwidget)
        self.push2.setGeometry(QtCore.QRect(800, 360, 131, 28))
        self.push2.setStyleSheet("background-color: rgb(255, 145, 135);")
        self.push2.setObjectName("push2")
        self.label2_3 = QtWidgets.QLabel(self.centralwidget)
        self.label2_3.setGeometry(QtCore.QRect(730, 310, 55, 21))
        self.label2_3.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_3.setObjectName("label2_3")
        self.push3 = QtWidgets.QPushButton(self.centralwidget)
        self.push3.setGeometry(QtCore.QRect(800, 450, 131, 31))
        self.push3.setStyleSheet("background-color: rgb(255, 145, 135);")
        self.push3.setObjectName("push3")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(730, 400, 281, 41))
        self.label3.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setWordWrap(True)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(730, 490, 281, 41))
        self.label4.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setWordWrap(True)
        self.label4.setObjectName("label4")
        self.label4_1 = QtWidgets.QLabel(self.centralwidget)
        self.label4_1.setGeometry(QtCore.QRect(730, 530, 111, 21))
        self.label4_1.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label4_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_1.setObjectName("label4_1")
        self.push4 = QtWidgets.QPushButton(self.centralwidget)
        self.push4.setGeometry(QtCore.QRect(800, 560, 131, 31))
        self.push4.setStyleSheet("background-color: rgb(255, 145, 135);")
        self.push4.setObjectName("push4")
        self.lineEditX1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditX1.setGeometry(QtCore.QRect(760, 50, 111, 22))
        self.lineEditX1.setStyleSheet("background-color: rgb(198, 253, 255);")
        self.lineEditX1.setFrame(False)
        self.lineEditX1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditX1.setObjectName("lineEditX1")
        self.lineEditY1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditY1.setGeometry(QtCore.QRect(900, 50, 111, 22))
        self.lineEditY1.setStyleSheet("background-color: rgb(198, 253, 255);")
        self.lineEditY1.setFrame(False)
        self.lineEditY1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditY1.setObjectName("lineEditY1")
        self.lineEditX2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditX2.setGeometry(QtCore.QRect(760, 90, 111, 22))
        self.lineEditX2.setStyleSheet("background-color: rgb(198, 253, 255);")
        self.lineEditX2.setFrame(False)
        self.lineEditX2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditX2.setObjectName("lineEditX2")
        self.lineEditY2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditY2.setGeometry(QtCore.QRect(900, 90, 111, 22))
        self.lineEditY2.setStyleSheet("background-color: rgb(198, 253, 255);")
        self.lineEditY2.setFrame(False)
        self.lineEditY2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditY2.setObjectName("lineEditY2")
        self.lineEditL1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditL1.setGeometry(QtCore.QRect(840, 270, 171, 22))
        self.lineEditL1.setStyleSheet("background-color: rgb(198, 253, 255);")
        self.lineEditL1.setFrame(False)
        self.lineEditL1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditL1.setObjectName("lineEditL1")
        self.lineEditA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditA.setGeometry(QtCore.QRect(840, 290, 171, 22))
        self.lineEditA.setStyleSheet("background-color: rgb(198, 253, 255);")
        self.lineEditA.setFrame(False)
        self.lineEditA.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditA.setObjectName("lineEditA")
        self.lineEditL2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditL2.setGeometry(QtCore.QRect(840, 530, 171, 22))
        self.lineEditL2.setStyleSheet("background-color: rgb(194, 248, 250);")
        self.lineEditL2.setFrame(False)
        self.lineEditL2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditL2.setObjectName("lineEditL2")
        self.comboBoxM1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxM1.setGeometry(QtCore.QRect(780, 110, 231, 22))
        self.comboBoxM1.setStyleSheet("background-color: rgb(217, 255, 255);")
        self.comboBoxM1.setEditable(False)
        self.comboBoxM1.setFrame(False)
        self.comboBoxM1.setObjectName("comboBoxM1")
        self.comboBoxM1.addItem("")
        self.comboBoxM1.addItem("")
        self.comboBoxM1.addItem("")
        self.comboBoxM1.addItem("")
        self.comboBoxM1.addItem("")
        self.comboBoxM1.addItem("")
        self.comboBoxC1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxC1.setGeometry(QtCore.QRect(840, 130, 171, 22))
        self.comboBoxC1.setStyleSheet("background-color: rgb(217, 255, 255);")
        self.comboBoxC1.setEditable(False)
        self.comboBoxC1.setFrame(False)
        self.comboBoxC1.setObjectName("comboBoxC1")
        self.comboBoxC1.addItem("")
        self.comboBoxC1.addItem("")
        self.comboBoxC1.addItem("")
        self.comboBoxC1.addItem("")
        self.comboBoxC1.addItem("")
        self.comboBoxC2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxC2.setGeometry(QtCore.QRect(840, 330, 171, 22))
        self.comboBoxC2.setStyleSheet("background-color: rgb(217, 255, 255);")
        self.comboBoxC2.setEditable(False)
        self.comboBoxC2.setFrame(False)
        self.comboBoxC2.setObjectName("comboBoxC2")
        self.comboBoxC2.addItem("")
        self.comboBoxC2.addItem("")
        self.comboBoxC2.addItem("")
        self.comboBoxC2.addItem("")
        self.comboBoxC2.addItem("")
        self.comboBoxM2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxM2.setGeometry(QtCore.QRect(780, 310, 231, 22))
        self.comboBoxM2.setStyleSheet("background-color: rgb(217, 255, 255);")
        self.comboBoxM2.setEditable(False)
        self.comboBoxM2.setFrame(False)
        self.comboBoxM2.setObjectName("comboBoxM2")
        self.comboBoxM2.addItem("")
        self.comboBoxM2.addItem("")
        self.comboBoxM2.addItem("")
        self.comboBoxM2.addItem("")
        self.comboBoxM2.addItem("")
        self.comboBoxM2.addItem("")
        self.lineEditX1_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditX1_2.setGeometry(QtCore.QRect(760, 250, 111, 22))
        self.lineEditX1_2.setStyleSheet("background-color: rgb(198, 253, 255);")
        self.lineEditX1_2.setFrame(False)
        self.lineEditX1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditX1_2.setObjectName("lineEditX1_2")
        self.label1_10 = QtWidgets.QLabel(self.centralwidget)
        self.label1_10.setGeometry(QtCore.QRect(870, 250, 31, 21))
        self.label1_10.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label1_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_10.setObjectName("label1_10")
        self.label1_11 = QtWidgets.QLabel(self.centralwidget)
        self.label1_11.setGeometry(QtCore.QRect(730, 250, 31, 21))
        self.label1_11.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label1_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_11.setObjectName("label1_11")
        self.lineEditY1_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditY1_2.setGeometry(QtCore.QRect(900, 250, 111, 22))
        self.lineEditY1_2.setStyleSheet("background-color: rgb(198, 253, 255);")
        self.lineEditY1_2.setFrame(False)
        self.lineEditY1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditY1_2.setObjectName("lineEditY1_2")
        self.label1_12 = QtWidgets.QLabel(self.centralwidget)
        self.label1_12.setGeometry(QtCore.QRect(730, 230, 281, 21))
        self.label1_12.setStyleSheet("background-color: rgb(140, 209, 255);")
        self.label1_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_12.setObjectName("label1_12")
        self.graphicsView.raise_()
        self.label1_2.raise_()
        self.label1_3.raise_()
        self.label1_4.raise_()
        self.label1_5.raise_()
        self.label1_6.raise_()
        self.label1_8.raise_()
        self.label1_9.raise_()
        self.push1.raise_()
        self.label2_1.raise_()
        self.label2_2.raise_()
        self.label2_4.raise_()
        self.push2.raise_()
        self.label2_3.raise_()
        self.label1.raise_()
        self.push3.raise_()
        self.label3.raise_()
        self.label4_1.raise_()
        self.label4.raise_()
        self.push4.raise_()
        self.lineEditX1.raise_()
        self.lineEditY1.raise_()
        self.lineEditX2.raise_()
        self.lineEditY2.raise_()
        self.lineEditL1.raise_()
        self.lineEditA.raise_()
        self.lineEditL2.raise_()
        self.label2.raise_()
        self.label1_7.raise_()
        self.comboBoxM1.raise_()
        self.comboBoxC1.raise_()
        self.comboBoxM2.raise_()
        self.comboBoxC2.raise_()
        self.lineEditX1_2.raise_()
        self.label1_10.raise_()
        self.label1_11.raise_()
        self.lineEditY1_2.raise_()
        self.label1_12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 26))
        self.menubar.setObjectName("menubar")
        self.menu_1 = QtWidgets.QAction("Условие задачи")
        self.menubar.addAction(self.menu_1)
        self.menu_1.triggered.connect(self.task)
        self.menu_2 = QtWidgets.QAction("Об авторе")
        self.menubar.addAction(self.menu_2)
        self.menu_2.triggered.connect(self.info)
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Введите координаты отрезка"))
        self.label1_2.setText(_translate("MainWindow", "Начало:"))
        self.label1_3.setText(_translate("MainWindow", "X:"))
        self.label1_4.setText(_translate("MainWindow", "Y:"))
        self.label1_5.setText(_translate("MainWindow", "Конец:"))
        self.label1_6.setText(_translate("MainWindow", "X:"))
        self.label1_7.setText(_translate("MainWindow", "Y:"))
        self.label1_8.setText(_translate("MainWindow", "Метод:"))
        self.label1_9.setText(_translate("MainWindow", "Цвет:"))
        self.push1.setText(_translate("MainWindow", "Построить отрезок"))
        self.label2.setText(_translate("MainWindow", "Введите параметры спектра"))
        self.label2_1.setText(_translate("MainWindow", "Длина:"))
        self.label2_2.setText(_translate("MainWindow", "Шаг угла:"))
        self.label2_4.setText(_translate("MainWindow", "Цвет:"))
        self.push2.setText(_translate("MainWindow", "Построить спектр"))
        self.label2_3.setText(_translate("MainWindow", "Метод:"))
        self.push3.setText(_translate("MainWindow", "Вывести"))
        self.label3.setText(_translate("MainWindow", "Результаты эффективности (гистограмма)"))
        self.label4.setText(_translate("MainWindow", "Исследование ступенчатости отрезка (график)"))
        self.label4_1.setText(_translate("MainWindow", "Длина:"))
        self.push4.setText(_translate("MainWindow", "Вывести"))
        self.comboBoxM1.setItemText(0, _translate("MainWindow", "Библиотечный"))
        self.comboBoxM1.setItemText(1, _translate("MainWindow", "ЦДА"))
        self.comboBoxM1.setItemText(2, _translate("MainWindow", "Брезенхема с действ. данными"))
        self.comboBoxM1.setItemText(3, _translate("MainWindow", "Брезенхема с целочисл. данными"))
        self.comboBoxM1.setItemText(4, _translate("MainWindow", "Брезенхема с устр. ступенчатости"))
        self.comboBoxM1.setItemText(5, _translate("MainWindow", "Ву"))
        self.comboBoxC1.setItemText(0, _translate("MainWindow", "Белый (фон)"))
        self.comboBoxC1.setItemText(1, _translate("MainWindow", "Черный"))
        self.comboBoxC1.setItemText(2, _translate("MainWindow", "Красный"))
        self.comboBoxC1.setItemText(3, _translate("MainWindow", "Зеленый"))
        self.comboBoxC1.setItemText(4, _translate("MainWindow", "Синий"))
        self.comboBoxC2.setItemText(0, _translate("MainWindow", "Белый (фон)"))
        self.comboBoxC2.setItemText(1, _translate("MainWindow", "Черный"))
        self.comboBoxC2.setItemText(2, _translate("MainWindow", "Красный"))
        self.comboBoxC2.setItemText(3, _translate("MainWindow", "Зеленый"))
        self.comboBoxC2.setItemText(4, _translate("MainWindow", "Синий"))
        self.comboBoxM2.setItemText(0, _translate("MainWindow", "Библиотечный"))
        self.comboBoxM2.setItemText(1, _translate("MainWindow", "ЦДА"))
        self.comboBoxM2.setItemText(2, _translate("MainWindow", "Брезенхема с действ. данными"))
        self.comboBoxM2.setItemText(3, _translate("MainWindow", "Брезенхема с целочисл. данными"))
        self.comboBoxM2.setItemText(4, _translate("MainWindow", "Брезенхема с устр. ступенчатости"))
        self.comboBoxM2.setItemText(5, _translate("MainWindow", "Ву"))
        self.label1_10.setText(_translate("MainWindow", "Y:"))
        self.label1_11.setText(_translate("MainWindow", "X:"))
        self.label1_12.setText(_translate("MainWindow", "Центр:"))

    def task(self):
        taskMes = QtWidgets.QMessageBox()
        taskMes.setWindowTitle("Условие задачи")
        taskMes.setText("Предоставить пользователю возможность отрисовки отреза/спектра отрезков разными методами и цветами, а также просмотра результатов эффективности и диаграммы ступенчатости предложенных методов.")
        taskMes.setIcon(QtWidgets.QMessageBox.Information)
        taskMes.exec_()

    def info(self):
        infoMes = QtWidgets.QMessageBox()
        infoMes.setWindowTitle("Об авторе")
        infoMes.setText("Лабораторная работа №3 'Разложение отрезка в растр' была написана Параскун Софией, ИУ7-44Б")
        infoMes.setIcon(QtWidgets.QMessageBox.Information)
        infoMes.exec_()