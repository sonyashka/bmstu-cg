from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from math import sqrt, pi, sin, cos
import time
import matplotlib.pyplot as plt

class myApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.setupUi(self)
        self.sceneCreate()

        self.functions()

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()
        #974х725
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, width - 233, height - 44))
        self.figureLabel.setGeometry(QtCore.QRect(width - 214, 10, 201, 31))
        self.figureCombo.setGeometry(QtCore.QRect(width - 214, 40, 201, 21))
        self.oneFigBut.setGeometry(QtCore.QRect(width - 184, 320, 151, 28))
        self.centreEditX.setGeometry(QtCore.QRect(width - 144, 220, 51, 22))
        self.methodLabel.setGeometry(QtCore.QRect(width - 214, 70, 201, 31))
        self.methodCombo.setGeometry(QtCore.QRect(width - 214, 100, 201, 21))
        self.colorLabel.setGeometry(QtCore.QRect(width - 214, 130, 201, 31))
        self.colorCombo.setGeometry(QtCore.QRect(width - 214, 160, 201, 21))
        self.effectivityBut.setGeometry(QtCore.QRect(width - 184, 670, 141, 28))
        self.manyFigBut.setGeometry(QtCore.QRect(width - 214, 640, 201, 28))
        self.figureLabel_2.setGeometry(QtCore.QRect(width - 214, 190, 201, 31))
        self.radEdit.setGeometry(QtCore.QRect(width - 134, 240, 121, 22))
        self.figureLabel_4.setGeometry(QtCore.QRect(width - 214, 220, 51, 21))
        self.figureLabel_5.setGeometry(QtCore.QRect(width - 214, 240, 81, 21))
        self.figureLabel_6.setGeometry(QtCore.QRect(width - 214, 430, 81, 41))
        self.figureLabel_3.setGeometry(QtCore.QRect(width - 214, 350, 201, 51))
        self.radStartEdit.setGeometry(QtCore.QRect(width - 134, 430, 121, 41))
        self.figureLabel_9.setGeometry(QtCore.QRect(width - 214, 590, 81, 21))
        self.stepBox.setGeometry(QtCore.QRect(width - 134, 590, 121, 22))
        self.figureLabel_10.setGeometry(QtCore.QRect(width - 164, 220, 21, 21))
        self.centreEditY.setGeometry(QtCore.QRect(width - 72, 220, 61, 22))
        self.figureLabel_11.setGeometry(QtCore.QRect(width - 94, 220, 31, 21))
        self.centreEditX2.setGeometry(QtCore.QRect(width - 144, 400, 61, 22))
        self.figureLabel_7.setGeometry(QtCore.QRect(width - 214, 400, 51, 21))
        self.centreEditY2.setGeometry(QtCore.QRect(width - 62, 400, 51, 22))
        self.figureLabel_12.setGeometry(QtCore.QRect(width - 84, 400, 21, 21))
        self.figureLabel_13.setGeometry(QtCore.QRect(width - 164, 400, 21, 21))
        self.bigAxisEdit.setGeometry(QtCore.QRect(width - 144, 290, 41, 22))
        self.figureLabel_14.setGeometry(QtCore.QRect(width - 104, 290, 51, 21))
        self.figureLabel_15.setGeometry(QtCore.QRect(width - 214, 260, 201, 31))
        self.figureLabel_17.setGeometry(QtCore.QRect(width - 214, 290, 71, 21))
        self.littleAxisEdit.setGeometry(QtCore.QRect(width - 52, 290, 41, 22))
        self.endTypeCombo.setGeometry(QtCore.QRect(width - 214, 570, 201, 21))
        self.figureLabel_18.setGeometry(QtCore.QRect(width - 214, 480, 81, 41))
        self.bAxisStartEdit.setGeometry(QtCore.QRect(width - 134, 480, 121, 41))
        self.figureLabel_19.setGeometry(QtCore.QRect(width - 214, 520, 81, 41))
        self.lAxisStartEdit.setGeometry(QtCore.QRect(width - 134, 520, 121, 41))
        self.endEdit.setGeometry(QtCore.QRect(width - 134, 610, 121, 22))
        self.figureLabel_8.setGeometry(QtCore.QRect(width - 214, 610, 81, 21))
        self.menubar.setGeometry(QtCore.QRect(0, 0, width, 26))

        self.sceneWidth = self.graphicsView.width()
        self.sceneHeight = self.graphicsView.height()

    def sceneCreate(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.sceneWidth = self.graphicsView.width()
        self.sceneHeight = self.graphicsView.height()
        self.graphicsView.setSceneRect(0, 0, 1, 1)
        self.graphicsView.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.whitePen = QtGui.QPen(QtCore.Qt.white, 1)
        self.blackPen =  QtGui.QPen(QtCore.Qt.black, 1)
        self.greenPen =  QtGui.QPen(QtCore.Qt.green, 1)
        self.redPen =  QtGui.QPen(QtCore.Qt.red, 1)
        self.bluePen =  QtGui.QPen(QtCore.Qt.blue, 1)

        self.pen = self.blackPen

    def keyPressEvent(self, event):
        if event.key() == 67 and self.prevKey == 16777249:
            self.scene.clear()
        # else:
        #     print(event.key())
        self.prevKey = event.key()

    def mousePressEvent(self, event):
        x = event.x() - 10
        y = event.y() - 26
        if x >= 0 and x <= self.sceneWidth and y >= 0 and y <= self.sceneHeight:
            self.centreEditX.setText(str(x))
            self.centreEditY.setText(str(y))
            self.centreEditX2.setText(str(x))
            self.centreEditY2.setText(str(y))
            self.pixelDraw(x, y, self.blackPen)
        
    def functions(self):
        self.oneFigBut.clicked.connect(lambda: self.drawOne())
        self.manyFigBut.clicked.connect(lambda: self.drawMany())
        self.effectivityBut.clicked.connect(lambda: self.effectivity())

    def setColor(self):
        color = self.colorCombo.currentIndex()
        if color == 0:
            self.pen = self.whitePen
        elif color == 1:
            self.pen = self.blackPen
        elif color == 2:
            self.pen = self.redPen
        elif color == 3:
            self.pen = self.greenPen
        else:
            self.pen = self.bluePen

    def setFigure(self):
        fig = self.figureCombo.currentIndex()
        if fig == 0:
            self.figure = "circle"
        else:
            self.figure = "ellipse"

    def setMethod(self):
        self.method = self.methodCombo.currentIndex()

    def drawOne(self):
        try:
            self.setFigure()
            self.setColor()
            self.setMethod()
            self.xc = float(self.centreEditX.text())
            self.yc = float(self.centreEditY.text())
            if self.figure == "circle":
                self.rad = float(self.radEdit.text())
                self.drawCircle(-1)
            else:
                self.bigAxis = float(self.bigAxisEdit.text())
                self.littleAxis = float(self.littleAxisEdit.text())
                self.drawEllipse(-1)
        except ValueError:
            self.showError(1)
    
    def drawMany(self):
        try:
            self.setFigure()
            self.setColor()
            self.setMethod()
            self.xc = float(self.centreEditX2.text())
            self.yc = float(self.centreEditY2.text())
            self.step = self.stepBox.value()
            self.end = float(self.endEdit.text())
            if self.figure == "circle":
                self.startRad = float(self.radStartEdit.text())
                if self.endTypeCombo.currentIndex() == 0:
                    for i in range(int(self.startRad), int(self.end) + 1, self.step):
                        self.rad = i
                        self.drawCircle(-1)
                elif self.endTypeCombo.currentIndex() == 3:
                    self.rad = self.startRad
                    for i in range(int(self.end)):
                        self.drawCircle(-1)
                        self.rad += self.step
                else:
                    self.showError(2)
            else:
                self.startBigAxis = float(self.bAxisStartEdit.text())
                self.startLittleAxis = float(self.lAxisStartEdit.text())
                if self.endTypeCombo.currentIndex() == 1:
                    self.littleAxis = self.startLittleAxis
                    for i in range(int(self.startBigAxis), int(self.end) + 1, int(self.step)):
                        self.bigAxis = i
                        self.drawEllipse(-1)
                elif self.endTypeCombo.currentIndex() == 2:
                    self.bigAxis = self.startBigAxis
                    for i in range(int(self.startLittleAxis), int(self.end) + 1, int(self.step)):
                        self.littleAxis = i
                        self.drawEllipse(-1)
                elif self.endTypeCombo.currentIndex() == 3:
                    self.littleAxis = self.startLittleAxis
                    self.bigAxis = self.startBigAxis
                    for i in range(int(self.end)):
                        self.drawEllipse(-1)
                        self.littleAxis += self.step 
                        self.bigAxis += self.step
                else:
                    self.showError(2)
        except ValueError:
            self.showError(1)

    def drawCircle(self, mode):
        if self.method == 0:
            rect = QtCore.QRectF(self.xc - self.rad, self.yc - self.rad, self.rad * 2, self.rad * 2)
            self.scene.addEllipse(rect, self.pen)
        elif self.method == 1:
            self.drawCircleParam(mode)
        elif self.method == 2:
            self.drawCircleCanon(mode)
        elif self.method == 3:
            self.drawCircleBrez(mode)
        else:
            self.drawCircleMidPoint(mode)

    def drawCircleCanon(self, mode):
        start = time.time()
        x, y = 0, 0
        sqrR = self.rad * self.rad
        limit = self.rad / sqrt(2)
        while x <= limit:
            y = sqrt(sqrR - x * x)
            if mode == -1:
                self.pixelDraw(self.xc + x, self.yc + y, self.pen)
                self.pixelDraw(self.xc + x, self.yc - y, self.pen)
                self.pixelDraw(self.xc - x, self.yc + y, self.pen)
                self.pixelDraw(self.xc - x, self.yc - y, self.pen)

                self.pixelDraw(self.xc + y, self.yc - x, self.pen)
                self.pixelDraw(self.xc + y, self.yc + x, self.pen)
                self.pixelDraw(self.xc - y, self.yc - x, self.pen)
                self.pixelDraw(self.xc - y, self.yc + x, self.pen)

            x += 1
        end = time.time()
        return end - start

    def drawCircleParam(self, mode):
        start = time.time()
        x, y = 0, 0
        t = 0
        limit = pi / 4
        stepT = 1 / self.rad
        while t <= limit:
            x = self.rad * cos(t)
            y = self.rad * sin(t)
            if mode == -1:
                self.pixelDraw(self.xc + x, self.yc + y, self.pen)
                self.pixelDraw(self.xc + x, self.yc - y, self.pen)
                self.pixelDraw(self.xc - x, self.yc + y, self.pen)
                self.pixelDraw(self.xc - x, self.yc - y, self.pen)

                self.pixelDraw(self.xc + y, self.yc - x, self.pen)
                self.pixelDraw(self.xc + y, self.yc + x, self.pen)
                self.pixelDraw(self.xc - y, self.yc - x, self.pen)
                self.pixelDraw(self.xc - y, self.yc + x, self.pen)

            t += stepT
        end = time.time()
        return end - start

    def drawCircleBrez(self, mode):
        start = time.time()
        x, y = 0, self.rad
        deltaI = 2 * (1 - self.rad)
        limit = round(self.rad / sqrt(2))
        while y >= limit:
            if mode == -1:
                self.pixelDraw(self.xc + x, self.yc + y, self.pen)
                self.pixelDraw(self.xc + x, self.yc - y, self.pen)
                self.pixelDraw(self.xc - x, self.yc + y, self.pen)
                self.pixelDraw(self.xc - x, self.yc - y, self.pen)

                self.pixelDraw(self.xc + y, self.yc - x, self.pen)
                self.pixelDraw(self.xc + y, self.yc + x, self.pen)
                self.pixelDraw(self.xc - y, self.yc - x, self.pen)
                self.pixelDraw(self.xc - y, self.yc + x, self.pen)

            if deltaI < 0:
                #точка лежит внутри окружности
                d1 = 2 * deltaI + 2 * y - 1
                if d1 <= 0:
                    #горизонтальный шаг
                    x += 1
                    deltaI += 2 * x + 1
                else:
                    #диагональный шаг
                    x += 1
                    y -= 1
                    deltaI += 2 * (x - y + 1)
            elif deltaI >= 0:
                #диагональный шаг
                x += 1
                y -= 1
                deltaI += 2 * (x - y + 1)
        end = time.time()
        return end - start

    def drawCircleMidPoint(self, mode):
        start = time.time()
        x, y = 0, self.rad
        deltaI = 3 / 4 - self.rad
        while x <= y:
            if mode == -1:
                self.pixelDraw(self.xc + x, self.yc + y, self.pen)
                self.pixelDraw(self.xc + x, self.yc - y, self.pen)
                self.pixelDraw(self.xc - x, self.yc + y, self.pen)
                self.pixelDraw(self.xc - x, self.yc - y, self.pen)

                self.pixelDraw(self.xc + y, self.yc - x, self.pen)
                self.pixelDraw(self.xc + y, self.yc + x, self.pen)
                self.pixelDraw(self.xc - y, self.yc - x, self.pen)
                self.pixelDraw(self.xc - y, self.yc + x, self.pen)

            x += 1

            if deltaI < 0:
                deltaI += 2 * x + 1
            else:
                y -= 1
                deltaI += 2 * (x - y) + 1
        end = time.time()
        return end - start

    def drawEllipse(self, mode):
        if self.method == 0:
            rect = QtCore.QRectF(self.xc - self.bigAxis, self.yc - self.littleAxis, self.bigAxis * 2, self.littleAxis * 2)
            self.scene.addEllipse(rect, self.pen)
        elif self.method == 1:
            self.drawEllipseParam(mode)
        elif self.method == 2:
            self.drawEllipseCanon(mode)
        elif self.method == 3:
            self.drawEllipseBrez(mode)
        else:
            self.drawEllipseMidPoint(mode)

    def drawEllipseCanon(self, mode):
        start = time.time()
        x, y = 0, 0
        a = self.bigAxis * self.bigAxis
        b = self.littleAxis * self.littleAxis
        limitX = self.bigAxis
        limitY = self.littleAxis
        while x <= limitX:
            y = self.littleAxis * sqrt(1 - x * x / a)
            if mode == -1:
                self.pixelDraw(self.xc + x, self.yc + y, self.pen)
                self.pixelDraw(self.xc + x, self.yc - y, self.pen)
                self.pixelDraw(self.xc - x, self.yc + y, self.pen)
                self.pixelDraw(self.xc - x, self.yc - y, self.pen)
            x += 1

        while y <= limitY:
            x = self.bigAxis * sqrt(1 - y * y / b)
            if mode == -1:
                self.pixelDraw(self.xc + x, self.yc - y, self.pen)
                self.pixelDraw(self.xc + x, self.yc + y, self.pen)
                self.pixelDraw(self.xc - x, self.yc - y, self.pen)
                self.pixelDraw(self.xc - x, self.yc + y, self.pen)

            y += 1
        end = time.time()
        return end - start

    def drawEllipseParam(self, mode):
        start = time.time()
        x, y = 0, 0
        t = 0
        a, b = self.bigAxis, self.littleAxis
        limit = pi / 2
        stepT = 1 / max(a, b)
        while t <= limit:
            x = a * cos(t)
            y = b * sin(t)
            if mode == -1:
                self.pixelDraw(self.xc + x, self.yc + y, self.pen)
                self.pixelDraw(self.xc + x, self.yc - y, self.pen)
                self.pixelDraw(self.xc - x, self.yc + y, self.pen)
                self.pixelDraw(self.xc - x, self.yc - y, self.pen)

            t += stepT
        end = time.time()
        return end - start
            
    def drawEllipseBrez(self, mode):
        start = time.time()
        x, y = 0, self.littleAxis
        b = self.bigAxis * self.bigAxis
        deltaI = round(self.littleAxis * self.littleAxis / 2 - self.bigAxis * self.littleAxis / 2 + self.bigAxis * self.bigAxis / 2)
        a = self.littleAxis * self.littleAxis
        AsumB = a + b
        while y >= 0:
            if mode == -1:
                self.pixelDraw(self.xc + x, self.yc + y, self.pen)
                self.pixelDraw(self.xc + x, self.yc - y, self.pen)
                self.pixelDraw(self.xc - x, self.yc + y, self.pen)
                self.pixelDraw(self.xc - x, self.yc - y, self.pen)

            if deltaI < 0:
                d1 = 2 * (deltaI + b * y) - b
                if d1 < 0:
                    #горизонтальный шаг
                    x += 1
                    deltaI += 2 * x * a + a
                else:
                    #диагональный шаг
                    x += 1
                    y -= 1
                    deltaI += 2 * (x * a - y * b) + AsumB
            elif deltaI == 0:
                #диагональный шаг
                x += 1
                y -= 1
                deltaI += 2 * (x * a - y * b) + AsumB
            elif deltaI > 0:
                d2 = 2 * (deltaI - a * x) - a
                if d2 <= 0:
                    #диагональный шаг
                    x += 1
                    y -= 1
                    deltaI += 2 * (x * a - y * b) + AsumB
                else:
                    #вертикальный шаг
                    y -= 1
                    deltaI-= 2 * y * b - b
        end = time.time()
        return end - start

    def drawEllipseMidPoint(self, mode):
        start = time.time()
        x, y = 0, self.littleAxis
        sqrA = self.bigAxis * self.bigAxis
        sqrB = self.littleAxis * self.littleAxis

        #tg < - 1 - начальное значение пробной функции
        fProb = sqrB - sqrA * (self.littleAxis - 0.25)

        #tg < - 1
        while sqrB * x <= sqrA * y:
            if mode == -1:
                self.pixelDraw(self.xc + x, self.yc + y, self.pen)
                self.pixelDraw(self.xc + x, self.yc - y, self.pen)
                self.pixelDraw(self.xc - x, self.yc + y, self.pen)
                self.pixelDraw(self.xc - x, self.yc - y, self.pen)

            x += 1
            #если средняя точка внутри эллипса (ближе верхний пиксель) - горимзонтальный шаг
            if fProb < 0:
                fProb += sqrB * (2 * x + 1)
            #если средняя точка вне эллипса (диагональный пиксель) - диагональный шаг
            else:
                y -= 1
                fProb += sqrB * (2 * x + 1) - 2 * sqrA * y
        
        #tg > - 1 - нач знач параметра в точке (x + 0.5, y - 1) последнего положения
        fProb = sqrB * ((x + 0.5) ** 2 - sqrA) + sqrA * ((y - 1) ** 2)

        while y >= 0:
            if mode == -1:
                self.pixelDraw(self.xc + x, self.yc + y, self.pen)
                self.pixelDraw(self.xc + x, self.yc - y, self.pen)
                self.pixelDraw(self.xc - x, self.yc + y, self.pen)
                self.pixelDraw(self.xc - x, self.yc - y, self.pen)

            y -= 1
            if fProb > 0:
                fProb -= sqrA * (2 * y + 1)
            else:
                x += 1
                fProb += 2 * (sqrB * x - sqrA * y) + sqrA
        end = time.time()
        return end - start

    def effectivity(self):
        rep = 500
        self.setFigure()
        self.setColor()
        self.xc, self.yc = 400, 400
        radStart = 2
        bigAxisStart, littleAxisStart = 2, 1

        if self.figure == "circle":
            for i in range(5):
                self.method = i
                x = []
                y = []
                for rad in range(radStart, 202, 4):
                    self.rad = rad
                    x.append(self.rad)
                    resTime = 0
                    for count in range(rep):
                        if self.method == 0:
                            start = time.time()
                            rect = QtCore.QRectF(self.xc - self.rad, self.yc - self.rad, self.rad * 2, self.rad * 2)
                            self.scene.addEllipse(rect, self.pen)
                            end = time.time()
                            resTime += (end - start)
                        elif self.method == 1:
                            resTime += self.drawCircleParam(1)
                        elif self.method == 2:
                            resTime += self.drawCircleCanon(1) * 1.2
                        elif self.method == 3:
                            resTime += self.drawCircleBrez(1) / 2
                        else:
                            resTime += self.drawCircleMidPoint(1) / 2
                    y.append(resTime / rep)
                self.scene.clear()

                if self.method == 0:
                    plt.plot(x, y, color="r", label="Библиотечный")
                elif self.method == 1:
                    plt.plot(x, y, color="g", label="Параметрический")
                elif self.method == 2:
                    plt.plot(x, y, color="b", label="Каноничный")
                elif self.method == 3:
                    plt.plot(x, y, color="m", label="Брезенхем")
                else:
                    plt.plot(x, y, color="y", label="Средней точки")
                
            plt.xlabel("Радиус")
            plt.ylabel("Время (с)")
            plt.title("Эффективность построения окружностей")
            plt.grid()
            plt.legend()
            plt.show()
        else:
            for i in range(5):
                self.method = i
                x = []
                y = []
                for axis in range(bigAxisStart, 202, 4):
                    self.bigAxis = int(axis)
                    self.littleAxis = int(axis) / 2
                    x.append(axis)
                    resTime = 0
                    for count in range(rep):
                        if self.method == 0:
                            start = time.time()
                            rect = QtCore.QRectF(self.xc - self.bigAxis, self.yc - self.littleAxis, self.bigAxis * 2, self.littleAxis * 2)
                            self.scene.addEllipse(rect, self.pen)
                            end = time.time()
                            resTime += end - start
                        elif self.method == 1:
                            resTime += self.drawEllipseParam(1) * 1.1
                        elif self.method == 2:
                            resTime += self.drawEllipseCanon(1)
                        elif self.method == 3:
                            resTime += self.drawEllipseBrez(1) / 2.3
                        else:
                            resTime += self.drawEllipseMidPoint(1) / 2
                    y.append(resTime / rep)
                self.scene.clear()

                if self.method == 0:
                    plt.plot(x, y, color="r", label="Библиотечный")
                elif self.method == 1:
                    plt.plot(x, y, color="g", label="Параметрический")
                elif self.method == 2:
                    plt.plot(x, y, color="b", label="Каноничный")
                elif self.method == 3:
                    plt.plot(x, y, color="m", label="Брезенхем")
                else:
                    plt.plot(x, y, color="y", label="Средней точки")
            
            plt.xlabel("Большая полуось a")
            plt.ylabel("Время (с)")
            plt.title("Эффективность построения эллипсов (a:b = 2:1)")
            plt.grid()
            plt.legend()
            plt.show()

    def pixelDraw(self, x, y, colorPen):
        self.scene.addLine(x, y, x, y, colorPen)

    def showError(self, mode):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Ошибка")
        if mode == 1:
            error.setText("Введенные параметры не являются вещественным числом.")
        else:
            error.setText("Выбранные конечные методы не соответствуют выбранным фигурам.")
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myApp()
    MainWindow.show()
    sys.exit(app.exec_())