from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from math import pi, cos, sin

class myApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.setupUi(self)
        
        self.point = False
        self.x = -1
        self.y = -1
        self.r = 0
        self.parts_x = []
        self.parts_y = []
        self.start()
        self.sceneCreate()
        self.prevKey = 0

        self.functions()

    def start(self):
        self.parts_x.clear()
        self.parts_y.clear()

        self.parts_x.append([435, 476, 422, 478, 458, 428, 422])
        self.parts_y.append([155, 85, 145, 190, 210, 197, 145])

        self.parts_x.append([422, 360, 403, 428, 478])
        self.parts_y.append([145, 172, 201, 197, 190])

        self.parts_x.append([360, 336, 430, 425, 403, 358, 334, 385, 303, 336])
        self.parts_y.append([172, 254, 281, 256, 201, 366, 316, 268, 297, 254])

        self.parts_x.append([334, 303, 240, 320, 334, 270, 280, 346, 324, 317])
        self.parts_y.append([316, 297, 310, 374, 316, 336, 452, 510, 512, 485])

        self.parts_x.append([240, 221, 182, 215, 198, 170, 182, 189, 235])
        self.parts_y.append([310, 351, 436, 411, 442, 451, 436, 342, 321])

        self.parts_x.append([189, 221, 272, 233, 273, 281, 258, 259, 247, 273])
        self.parts_y.append([342, 351, 359, 444, 493, 516, 516, 496, 487, 493])

        self.parts_x.append([187, 221, 220, 198])
        self.parts_y.append([369, 351, 388, 402])

        self.parts_x.append([272, 220, 215])
        self.parts_y.append([359, 388, 411])
        
        self.parts_x.append([247, 233])
        self.parts_y.append([487, 444])

        self.parts_x.append([220, 257, 257])
        self.parts_y.append([388, 440, 473])

        self.parts_x.append([257, 320, 319, 295])
        self.parts_y.append([440, 374, 406, 400])

        self.parts_x.append([346, 326, 280, 300, 326])
        self.parts_y.append([510, 479, 452, 446, 479])

        self.parts_x.append([300, 319])
        self.parts_y.append([446, 406])

        self.parts_x.append([320, 358, 416, 461, 454, 437, 437, 449, 437])
        self.parts_y.append([374, 366, 328, 342, 376, 384, 397, 391, 384])

        self.parts_x.append([449, 462, 454])
        self.parts_y.append([391, 385, 376])

        self.parts_x.append([462, 485, 467, 430, 485, 461, 460, 467])
        self.parts_y.append([385, 345, 288, 281, 345, 342, 301, 288])

        self.parts_x.append([460, 447, 416, 385])
        self.parts_y.append([301, 300, 328, 268])

        self.parts_x.append([422, 368, 388, 351, 360, 324, 351])
        self.parts_y.append([145, 128, 160, 146, 172, 149, 146])

        self.parts_x.append([350, 318, 355, 309, 348, 306, 340, 297, 336, 292, 315])
        self.parts_y.append([165, 174, 191, 201, 216, 222, 242, 244, 254, 278, 282])

        self.point = False
        self.x = -1
        self.y = -1
        self.r = 3
        self.sceneScale = 1
        self.sceneShiftX = 0
        self.sceneShiftY = 0

        self.lastAction = "start"
        self.sceneCreate()

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()

        self.graphicsView.setGeometry(QtCore.QRect(10, 0, width - 226, height - 28))
        self.label.setGeometry(QtCore.QRect(width - 207, 10, 201, 31))
        self.label_2.setGeometry(QtCore.QRect(width - 207, 40, 31, 21))
        self.label_3.setGeometry(QtCore.QRect(width - 107, 40, 31, 21))
        self.lineEdit.setGeometry(QtCore.QRect(width - 177, 40, 71, 22))
        self.lineEdit_2.setGeometry(QtCore.QRect(width - 77, 40, 71, 22))
        self.pushButton.setGeometry(QtCore.QRect(width - 157, 70, 93, 28))
        self.label_4.setGeometry(QtCore.QRect(width - 207, 110, 201, 41))
        self.label_5.setGeometry(QtCore.QRect(width - 207, 150, 61, 21))
        self.lineEdit_3.setGeometry(QtCore.QRect(width - 147, 150, 61, 22))
        self.lineEdit_4.setGeometry(QtCore.QRect(width - 67, 150, 61, 22))
        self.label_6.setGeometry(QtCore.QRect(width - 87, 150, 21, 21))
        self.label_7.setGeometry(QtCore.QRect(width - 207, 170, 201, 20))
        self.label_8.setGeometry(QtCore.QRect(width - 207, 190, 41, 21))
        self.label_9.setGeometry(QtCore.QRect(width - 107, 190, 41, 21))
        self.lineEdit_5.setGeometry(QtCore.QRect(width - 167, 190, 61, 22))
        self.lineEdit_6.setGeometry(QtCore.QRect(width - 67, 190, 61, 22))
        self.pushButton_2.setGeometry(QtCore.QRect(width - 167, 220, 111, 28))
        self.label_10.setGeometry(QtCore.QRect(width - 207, 270, 201, 31))
        self.label_11.setGeometry(QtCore.QRect(width - 207, 300, 201, 20))
        self.label_12.setGeometry(QtCore.QRect(width - 207, 320, 31, 21))
        self.label_13.setGeometry(QtCore.QRect(width - 107, 320, 31, 21))
        self.lineEdit_7.setGeometry(QtCore.QRect(width - 177, 320, 71, 22))
        self.lineEdit_8.setGeometry(QtCore.QRect(width - 77, 320, 71, 22))
        self.label_14.setGeometry(QtCore.QRect(width - 207, 340, 101, 21))
        self.lineEdit_9.setGeometry(QtCore.QRect(width - 105, 340, 101, 22))
        self.pushButton_3.setGeometry(QtCore.QRect(width - 157, 370, 93, 28))
        self.pushButton_4.setGeometry(QtCore.QRect(width - 205, 410, 201, 41))
        self.menubar.setGeometry(QtCore.QRect(0, 0, width, 26))
        self.sceneCreate()

    def keyPressEvent(self, event):
        if event.key() == 90 and self.prevKey == 16777249:
            if self.lastAction == "shift":
                self.shift(-1)
            elif self.lastAction == "zoom":
                self.zoom(-1)
            elif self.lastAction == "rotate":
                self.rotate(-1)
        elif event.key() == 87:
            self.sceneShiftY += 10
            self.sceneDraw()
        elif event.key() == 65:
            self.sceneShiftX += 10
            self.sceneDraw()
        elif event.key() == 83:
            self.sceneShiftY -= 10
            self.sceneDraw()
        elif event.key() == 68:
            self.sceneShiftX -= 10
            self.sceneDraw()
        elif event.key() == 73:
            self.sceneScale *= 1.1
            self.sceneDraw()
        elif event.key() == 79:
            self.sceneScale *= 0.9
            self.sceneDraw()
        # print(event.key())
        self.prevKey = event.key()

    def mousePressEvent(self, event):
        x = event.x() - 10
        y = event.y() - 26
        xm = int(self.sceneWidth / 2)
        ym = int(self.sceneHeight / 2)
        if x >= 0 and x <= self.sceneWidth and y >= 0 and y <= self.sceneHeight:
            #self.x = round(self.sceneScale * (x + self.sceneShiftX) + xm * (1 - self.sceneScale))
            #self.y = round(self.sceneScale * (y + self.sceneShiftY) + ym * (1 - self.sceneScale))
            self.point = True
            self.x = round((x - xm * (1 - self.sceneScale)) / self.sceneScale - self.sceneShiftX)
            self.y = round((y - ym * (1 - self.sceneScale)) / self.sceneScale - self.sceneShiftY)
            #print(x, y, "|", self.x, self.y, "|", self.sceneScale * (self.x - self.r / 2 + self.sceneShiftX) + xm * (1 - self.sceneScale), self.sceneScale * (self.y  - self.r / 2 + self.sceneShiftY) + ym * (1 - self.sceneScale))
            self.r = 3
            self.lineEdit_3.setText(str(self.x))
            self.lineEdit_4.setText(str(self.y))
            self.lineEdit_7.setText(str(self.x))
            self.lineEdit_8.setText(str(self.y))
            self.sceneCreate()

    def functions(self):
        self.pushButton.clicked.connect(lambda: self.shift(0))
        self.pushButton_2.clicked.connect(lambda: self.zoom(0))
        self.pushButton_3.clicked.connect(lambda: self.rotate(0))
        self.pushButton_4.clicked.connect(lambda: self.start())

    def sceneCreate(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.sceneWidth = self.graphicsView.width()
        self.sceneHeight = self.graphicsView.height()
        self.graphicsView.setSceneRect(0, 0, 1, 1)
        self.graphicsView.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.blackBrush = QtGui.QBrush(QtCore.Qt.black)
        self.greenBrush =  QtGui.QBrush(QtCore.Qt.green)
        self.redBrush =  QtGui.QBrush(QtCore.Qt.red)
        self.blueBrush =  QtGui.QBrush(QtCore.Qt.blue)

        self.blackPen =  QtGui.QPen(QtCore.Qt.black, 3)
        self.blackPenLittle =  QtGui.QPen(QtCore.Qt.black, 1)
        self.greenPen =  QtGui.QPen(QtCore.Qt.green, 3)
        self.redPen =  QtGui.QPen(QtCore.Qt.red, 3)
        self.bluePen =  QtGui.QPen(QtCore.Qt.blue, 3)

        self.sceneDraw()

    def sceneDraw(self):
        self.scene.clear()

        self.scene.addLine(0, (1 - self.sceneScale) * (self.sceneHeight / 2), self.sceneWidth, (1 - self.sceneScale) * (self.sceneHeight / 2), self.blackPenLittle)
        self.scene.addLine((1 - self.sceneScale) * (self.sceneWidth / 2), 0, (1 - self.sceneScale) * (self.sceneWidth / 2), self.sceneHeight, self.blackPenLittle)

        #print("x: ", self.parts_x[0][1], " y: ", self.parts_y[0][1])
        xm = int(self.sceneWidth / 2)
        ym = int(self.sceneHeight / 2)
        for i in range(len(self.parts_x)):
            for j in range(len(self.parts_x[i]) - 1):
                self.scene.addLine(self.sceneScale * (self.parts_x[i][j] + self.sceneShiftX) + xm * (1 - self.sceneScale), self.sceneScale * (self.parts_y[i][j] + self.sceneShiftY) + ym * (1 - self.sceneScale), self.sceneScale * (self.parts_x[i][j + 1] + self.sceneShiftX) + xm * (1 - self.sceneScale), self.sceneScale * (self.parts_y[i][j + 1] + self.sceneShiftY) + ym * (1 - self.sceneScale), self.blackPen)

        if self.point:
            #print("RX ", self.sceneScale * (self.x - self.r / 2 + self.sceneShiftX) + xm * (1 - self.sceneScale), " RY ", self.sceneScale * (self.y  - self.r / 2 + self.sceneShiftY) + ym * (1 - self.sceneScale), " RR ", self.r * self.sceneScale)
            self.scene.addEllipse(self.sceneScale * (self.x - self.r / 2 + self.sceneShiftX) + xm * (1 - self.sceneScale), self.sceneScale * (self.y  - self.r / 2 + self.sceneShiftY) + ym * (1 - self.sceneScale), self.r * self.sceneScale, self.r * self.sceneScale, self.greenPen, self.greenBrush)

    def shift(self, mode):
        try:
            if mode == 0:
                self.dx = float(self.lineEdit.text())
                self.dy = float(self.lineEdit_2.text())
            else:
                self.dx *= -1
                self.dy *= -1
            self.point = True
            for i in range(len(self.parts_x)):
                for j in range(len(self.parts_x[i])):
                    self.parts_x[i][j] += self.dx
                    self.parts_y[i][j] += self.dy
            self.sceneDraw()
            self.lastAction = "shift"
        except ValueError:
            self.showError()

    def zoom(self, mode):
        try:
            print("zoom")
            if mode == 0:
                self.xm = float(self.lineEdit_3.text())
                self.ym = float(self.lineEdit_4.text())
                self.kx = float(self.lineEdit_5.text())
                self.ky = float(self.lineEdit_6.text())
            else:
                self.kx = 1 / self.kx
                self.ky = 1 / self.ky
            self.point = True
            for i in range(len(self.parts_x)):
                for j in range(len(self.parts_x[i])):
                    self.parts_x[i][j] = self.kx * self.parts_x[i][j] + self.xm * (1 - self.kx)
                    self.parts_y[i][j] = self.ky * self.parts_y[i][j] + self.ym * (1 - self.ky)
            self.x = self.xm
            self.y = self.ym
            self.sceneDraw()
            self.lastAction = "zoom"
        except ValueError:
            self.showError()

    def rotate(self, mode):
        try:
            if mode == 0:
                self.xc = float(self.lineEdit_7.text())
                self.yc = float(self.lineEdit_8.text())
                self.teta = float(self.lineEdit_9.text()) * pi / 180
            else:
                self.teta *= -1 
            for i in range(len(self.parts_x)):
                for j in range(len(self.parts_x[i])):
                    x = self.parts_x[i][j]
                    y = self.parts_y[i][j]
                    self.parts_x[i][j] = self.xc + (x - self.xc) * cos(self.teta) + (y - self.yc) * sin(self.teta)
                    self.parts_y[i][j] = self.yc - (x - self.xc) * sin(self.teta) + (y - self.yc) * cos(self.teta)
            self.x = self.xc
            self.y = self.yc
            self.sceneDraw()
            self.lastAction = "rotate"
        except ValueError:
            self.showError()

    def showError(self):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText("Введенные параметры не являются вещественным числом.")
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myApp()
    MainWindow.show()
    sys.exit(app.exec_())