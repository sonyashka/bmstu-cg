from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(787, 549))
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 0, 561, 521))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 10, 201, 31))
        self.label.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 40, 31, 21))
        self.label_2.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 40, 31, 21))
        self.label_3.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(610, 40, 71, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(230, 255, 255);")
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(710, 40, 71, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(230, 255, 255);\n")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 70, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(255, 168, 152);")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, 110, 201, 41))
        self.label_4.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(580, 150, 61, 21))
        self.label_5.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(640, 150, 61, 22))
        self.lineEdit_3.setStyleSheet("background-color: rgb(230, 255, 255);\n")
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(720, 150, 61, 22))
        self.lineEdit_4.setStyleSheet("background-color: rgb(230, 255, 255);")
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(700, 150, 21, 21))
        self.label_6.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 170, 201, 20))
        self.label_7.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(580, 190, 41, 21))
        self.label_8.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(680, 190, 41, 21))
        self.label_9.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(620, 190, 61, 22))
        self.lineEdit_5.setStyleSheet("background-color: rgb(230, 255, 255);")
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(720, 190, 61, 22))
        self.lineEdit_6.setStyleSheet("background-color: rgb(230, 255, 255);")
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 220, 111, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 168, 152);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(580, 270, 201, 31))
        self.label_10.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(580, 300, 201, 20))
        self.label_11.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(580, 320, 31, 21))
        self.label_12.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(680, 320, 31, 21))
        self.label_13.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(610, 320, 71, 22))
        self.lineEdit_7.setStyleSheet("background-color: rgb(230, 255, 255);")
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(710, 320, 71, 22))
        self.lineEdit_8.setStyleSheet("background-color: rgb(230, 255, 255);")
        self.lineEdit_8.setFrame(False)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(580, 340, 101, 21))
        self.label_14.setStyleSheet("background-color: rgb(135, 207, 255);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(682, 340, 101, 22))
        self.lineEdit_9.setStyleSheet("background-color: rgb(230, 255, 255);")
        self.lineEdit_9.setFrame(False)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 370, 93, 28))
        self.pushButton_3.setStyleSheet("background-color: rgb(248, 164, 148);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(582, 410, 201, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(242, 160, 145);")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 26))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Геометрические преобразования"))
        self.label.setText(_translate("MainWindow", "Введите смещение объекта:"))
        self.label_2.setText(_translate("MainWindow", "dx:"))
        self.label_3.setText(_translate("MainWindow", "dy:"))
        self.pushButton.setText(_translate("MainWindow", "Перенести"))
        self.label_4.setText(_translate("MainWindow", "Введите параметры масштабирования:"))
        self.label_5.setText(_translate("MainWindow", "Центр X:"))
        self.label_6.setText(_translate("MainWindow", "Y:"))
        self.label_7.setText(_translate("MainWindow", "Коэффициенты"))
        self.label_8.setText(_translate("MainWindow", "По X:"))
        self.label_9.setText(_translate("MainWindow", "По Y:"))
        self.pushButton_2.setText(_translate("MainWindow", "Масштабировать"))
        self.label_10.setText(_translate("MainWindow", "Введите параметры переноса:"))
        self.label_11.setText(_translate("MainWindow", "Центр поворота:"))
        self.label_12.setText(_translate("MainWindow", "X:"))
        self.label_13.setText(_translate("MainWindow", "Y:"))
        self.label_14.setText(_translate("MainWindow", "Угол поворота:"))
        self.pushButton_3.setText(_translate("MainWindow", "Повернуть"))
        self.pushButton_4.setText(_translate("MainWindow", "Вернуть исходник"))

    def task(self):
        taskMes = QtWidgets.QMessageBox()
        taskMes.setWindowTitle("Условие задачи")
        taskMes.setText("Нарисовать исходный рисунок, затем его переместить, промасштабировать, повернуть.")
        taskMes.setIcon(QtWidgets.QMessageBox.Information)
        taskMes.exec_()

    def info(self):
        infoMes = QtWidgets.QMessageBox()
        infoMes.setWindowTitle("Об авторе")
        infoMes.setText("Лабораторная работа №2 'Геометрические преобразования' была написана Параскун Софией, ИУ7-44Б")
        infoMes.setIcon(QtWidgets.QMessageBox.Information)
        infoMes.exec_()
