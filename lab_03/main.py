from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from math import radians, sin, cos, pi, floor, fabs
import time
import matplotlib.pyplot as plt

eps = 1e-5

class myApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.setupUi(self)
        self.sceneCreate()
        self.point = False
        self.prevKey = 0

        self.functions()

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()

        self.graphicsView.setGeometry(QtCore.QRect(10, 0, width - 309, height - 29))
        self.label1.setGeometry(QtCore.QRect(width - 290, 0, 281, 31))
        self.label1_2.setGeometry(QtCore.QRect(width - 290, 30, 281, 21))
        self.label1_3.setGeometry(QtCore.QRect(width - 290, 50, 31, 21))
        self.label1_4.setGeometry(QtCore.QRect(width - 150, 50, 31, 21))
        self.label1_5.setGeometry(QtCore.QRect(width - 290, 70, 281, 21))
        self.label1_6.setGeometry(QtCore.QRect(width - 290, 90, 31, 21))
        self.label1_7.setGeometry(QtCore.QRect(width - 150, 90, 31, 21))
        self.label1_8.setGeometry(QtCore.QRect(width - 290, 110, 55, 21))
        self.label1_9.setGeometry(QtCore.QRect(width - 290, 130, 111, 21))
        self.label2.setGeometry(QtCore.QRect(width - 290, 200, 281, 31))
        self.label2_1.setGeometry(QtCore.QRect(width - 290, 270, 111, 21))
        self.label2_2.setGeometry(QtCore.QRect(width - 290, 290, 111, 21))
        self.label2_4.setGeometry(QtCore.QRect(width - 290, 330, 111, 21))
        self.label2_3.setGeometry(QtCore.QRect(width - 290, 310, 55, 21))
        self.push1.setGeometry(QtCore.QRect(width - 220, 160, 131, 28))
        self.push2.setGeometry(QtCore.QRect(width - 220, 360, 131, 28))
        self.push3.setGeometry(QtCore.QRect(width - 220, 450, 131, 31))
        self.label3.setGeometry(QtCore.QRect(width - 290, 400, 281, 41))
        self.label4.setGeometry(QtCore.QRect(width - 290, 490, 281, 41))
        self.label4_1.setGeometry(QtCore.QRect(width - 290, 530, 111, 21))
        self.push4.setGeometry(QtCore.QRect(width - 220, 560, 131, 31))
        self.label1_10.setGeometry(QtCore.QRect(width - 150, 250, 31, 21))
        self.label1_11.setGeometry(QtCore.QRect(width - 290, 250, 31, 21))
        self.label1_12.setGeometry(QtCore.QRect(width - 290, 230, 281, 21))

        self.lineEditX1.setGeometry(QtCore.QRect(width - 260, 50, 111, 22))
        self.lineEditY1.setGeometry(QtCore.QRect(width - 120, 50, 111, 22))
        self.lineEditX2.setGeometry(QtCore.QRect(width - 260, 90, 111, 22))
        self.lineEditY2.setGeometry(QtCore.QRect(width - 120, 90, 111, 22))
        self.lineEditX1_2.setGeometry(QtCore.QRect(width - 260, 250, 111, 22))
        self.lineEditY1_2.setGeometry(QtCore.QRect(width - 120, 250, 111, 22))

        self.lineEditL1.setGeometry(QtCore.QRect(width - 180, 270, 171, 22))
        self.lineEditA.setGeometry(QtCore.QRect(width - 180, 290, 171, 22))
        self.lineEditL2.setGeometry(QtCore.QRect(width - 180, 530, 171, 22))
        self.comboBoxM1.setGeometry(QtCore.QRect(width - 240, 110, 231, 22))
        self.comboBoxC1.setGeometry(QtCore.QRect(width - 180, 130, 171, 22))
        self.comboBoxC2.setGeometry(QtCore.QRect(width - 180, 330, 171, 22))
        self.comboBoxM2.setGeometry(QtCore.QRect(width - 240, 310, 231, 22))
        self.menubar.setGeometry(QtCore.QRect(0, 0, width, 26))
        #self.sceneCreate()

    def sceneCreate(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.sceneWidth = self.graphicsView.width()
        self.sceneHeight = self.graphicsView.height()
        self.graphicsView.setSceneRect(0, 0, 1, 1)
        self.graphicsView.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.whitePen = QtGui.QPen(QtCore.Qt.white, 1)
        self.blackPen =  QtGui.QPen(QtCore.Qt.black, 1)
        self.grayPen = QtGui.QPen(QtCore.Qt.darkGray, 1)
        self.darkGreenPen = QtGui.QPen(QtCore.Qt.darkGreen, 1)
        self.greenPen =  QtGui.QPen(QtCore.Qt.green, 1)
        self.darkRedPen = QtGui.QPen(QtCore.Qt.darkRed, 1)
        self.redPen =  QtGui.QPen(QtCore.Qt.red, 1)
        self.darkBluePen = QtGui.QPen(QtCore.Qt.darkBlue, 1)
        self.bluePen =  QtGui.QPen(QtCore.Qt.blue, 1)

    def keyPressEvent(self, event):
        if event.key() == 67 and self.prevKey == 16777249:
            self.scene.clear()
        else:
            print(event.key())
        self.prevKey = event.key()

    def mousePressEvent(self, event):
        x = event.x() - 10
        y = event.y() - 26
        if x >= 0 and x <= self.sceneWidth and y >= 0 and y <= self.sceneHeight:
            if not self.point:
                self.point = True
                self.lineEditX1.setText(str(x))
                self.lineEditY1.setText(str(y))
            else:
                self.point = False
                self.lineEditX2.setText(str(x))
                self.lineEditY2.setText(str(y))
            self.lineEditX1_2.setText(str(x))
            self.lineEditY1_2.setText(str(y))
            self.pixelDraw(x, y, self.blackPen)

    def functions(self):
        self.push1.clicked.connect(lambda: self.lineDraw())
        self.push2.clicked.connect(lambda: self.spectrumDraw(-1))
        self.push3.clicked.connect(lambda: self.resEffectivity())
        self.push4.clicked.connect(lambda: self.checkStadging())

    def setColor(self, ind):
        if ind == 0:
            color = self.comboBoxC1.currentIndex()
        else:
            color = self.comboBoxC2.currentIndex()

        if color == 0:
            self.curColor = [255, 255, 255, 1]
            self.pen = self.whitePen
        elif color == 1:
            self.curColor = [0, 0, 0, 1]
            self.pen = self.blackPen
        elif color == 2:
            self.curColor = [255, 0, 0, 1]
            self.pen = self.redPen
        elif color == 3:
            self.curColor = [0, 255, 0, 1]
            self.pen = self.greenPen
        else:
            self.curColor = [0, 0, 255, 1]
            self.pen = self.bluePen

    def lineDraw(self):
        try:
            self.xs = float(self.lineEditX1.text())
            self.ys = float(self.lineEditY1.text())
            self.xe = float(self.lineEditX2.text())
            self.ye = float(self.lineEditY2.text())

            self.pixelDraw(self.xs, self.ys, self.whitePen)
            self.pixelDraw(self.xe, self.ye, self.whitePen)
            self.setColor(0)

            ind = self.comboBoxM1.currentIndex()
            if ind == 0:
                self.scene.addLine(self.xs, self.ys, self.xe, self.ye, self.pen)
            elif ind == 1:
                self.cdaDraw(self.xs, self.ys, self.xe, self.ye, self.pen)
            elif ind == 2:
                self.brezFloatDraw(self.xs, self.ys, self.xe, self.ye, self.pen)
            elif ind == 3:
                self.brezIntDraw(self.xs, self.ys, self.xe, self.ye, self.pen)
            elif ind == 4:
                self.brezStageEliminateDraw(self.xs, self.ys, self.xe, self.ye, self.curColor, self.pen)
            else:
                self.vuDraw(self.xs, self.ys, self.xe, self.ye, self.curColor, self.pen)
        except ValueError:
            self.showError()

    def spectrumDraw(self, method):
        try:
            self.xs = float(self.lineEditX1_2.text())
            self.ys = float(self.lineEditY1_2.text())
            self.l = float(self.lineEditL1.text())
            self.angle = radians(float(self.lineEditA.text()))

            self.xe = self.xs + self.l
            self.ye = self.ys

            self.pixelDraw(self.xs, self.ys, self.whitePen)
            self.setColor(1)

            for i in range(0, int(2 * pi / self.angle)):
                if method != -1:
                    ind = method
                else:
                    ind = self.comboBoxM2.currentIndex()
                if ind == 0:
                    self.scene.addLine(self.xs, self.ys, self.xe, self.ye, self.pen)
                elif ind == 1:
                    self.cdaDraw(self.xs, self.ys, self.xe, self.ye, self.pen)
                elif ind == 2:
                    self.brezFloatDraw(self.xs, self.ys, self.xe, self.ye, self.pen)
                elif ind == 3:
                    self.brezIntDraw(self.xs, self.ys, self.xe, self.ye, self.pen)
                elif ind == 4:
                    self.brezStageEliminateDraw(self.xs, self.ys, self.xe, self.ye, self.curColor, self.pen)
                else:
                    self.vuDraw(self.xs, self.ys, self.xe, self.ye, self.curColor, self.pen)
                xe = self.xe
                ye = self.ye
                self.xe = self.xs + (xe - self.xs) * cos(self.angle) + (ye - self.ys) * sin(self.angle)
                self.ye = self.ys - (xe - self.xs) * sin(self.angle) + (ye - self.ys) * cos(self.angle)
        except ValueError:
            self.showError()

    def resEffectivity(self):
        pen = QtGui.QPen(QtCore.Qt.black, 1)
        times = [0] * 6

        reps = 20
        xs = 400
        ys = 400
        l = 300
        angle = 15

        self.lineEditX1_2.setText(str(xs))
        self.lineEditY1_2.setText(str(ys))
        self.lineEditL1.setText(str(l))
        self.lineEditA.setText(str(angle))

        start = time.time()
        self.spectrumDraw(0)
        end = time.time()
        times[0] = (end - start) / reps

        start = time.time()
        self.spectrumDraw(1)
        end = time.time()
        times[1] = (end - start) / reps
        
        start = time.time()
        self.spectrumDraw(2)
        end = time.time()
        times[2] = (end - start) / reps
        
        start = time.time()
        self.spectrumDraw(3)
        end = time.time()
        times[3] = (end - start) / reps

        start = time.time()
        self.spectrumDraw(4)
        end = time.time()
        times[4] = (end - start) / reps

        start = time.time()
        self.spectrumDraw(5)
        end = time.time()
        times[5] = (end - start) / reps

        fig, ax = plt.subplots()
        plt.title("Результаты эффективности")
        ax.bar(["Библиотечный", "ЦДА", "Брезенхем\n(int)", "Брезенхем\n(float)", "Брезенхем\n(сглаживание)", "Ву"], times)
        ax.set_facecolor('white')
        ax.set_xlabel('Алгоритм')
        ax.set_ylabel('Время')
        fig.set_facecolor('white')
        fig.set_figwidth(8)
        fig.set_figheight(4)
        self.scene.clear()
        plt.show()

    def checkStadging(self):
        try:
            l = float(self.lineEditL2.text())
            angle = 5
            pen = QtGui.QPen(QtCore.Qt.black, 1)

            reps = 20
            xs = 400
            ys = 400
            angle = 5
            angleRad = radians(angle)

            stadging = []
            xe = xs
            ye = ys + l
            for i in range(angle, 90, angle):
                tmpXe = xe
                xe = xs + (xe - xs) * cos(angleRad) + (ye - ys) * sin(angleRad)
                ye = ys - (tmpXe - xs) * sin(angleRad) + (ye - ys) * cos(angleRad)
                
                dx = abs(xe - xs)
                dy = abs(ye - ys)
                stadging.append([i, min(dx, dy)])

            x = []
            y = []
            for i in range(len(stadging)):
                x.append(stadging[i][0])
                y.append(stadging[i][1])
            plt.plot(x, y, color="r", label="Библиотечный")
            plt.xlabel("Угол в градусах")
            plt.ylabel("Количество ступенек")
            plt.legend()

            stadging = []
            xe = xs
            ye = ys + l
            for i in range(angle, 90, angle):
                tmpXe = xe
                xe = xs + (xe - xs) * cos(angleRad) + (ye - ys) * sin(angleRad)
                ye = ys - (tmpXe - xs) * sin(angleRad) + (ye - ys) * cos(angleRad)
                
                dx = abs(xe - xs)
                dy = abs(ye - ys)
                stadging.append([i, min(dx, dy)])

            x = []
            y = []
            for i in range(len(stadging)):
                x.append(stadging[i][0])
                y.append(stadging[i][1])
            plt.plot(x, y, color="r", label="ЦДА")
            plt.xlabel("Угол в градусах")
            plt.ylabel("Количество ступенек")
            plt.legend()

            stadging = []
            xe = xs
            ye = ys + l
            for i in range(angle, 90, angle):
                tmpXe = xe
                xe = xs + (xe - xs) * cos(angleRad) + (ye - ys) * sin(angleRad)
                ye = ys - (tmpXe - xs) * sin(angleRad) + (ye - ys) * cos(angleRad)
                
                dx = abs(xe - xs)
                dy = abs(ye - ys)
                stadging.append([i, min(dx, dy)])

            x = []
            y = []
            for i in range(len(stadging)):
                x.append(stadging[i][0])
                y.append(stadging[i][1])
            plt.plot(x, y, color="g", label="Брезенхема(int)")
            plt.xlabel("Угол в градусах")
            plt.ylabel("Количество ступенек")
            plt.legend()

            stadging = []
            xe = xs
            ye = ys + l
            for i in range(angle, 90, angle):
                tmpXe = xe
                xe = xs + (xe - xs) * cos(angleRad) + (ye - ys) * sin(angleRad)
                ye = ys - (tmpXe - xs) * sin(angleRad) + (ye - ys) * cos(angleRad)
                
                dx = abs(xe - xs)
                dy = abs(ye - ys)
                stadging.append([i, min(dx, dy)])

            x = []
            y = []
            for i in range(len(stadging)):
                x.append(stadging[i][0])
                y.append(stadging[i][1])
            plt.plot(x, y, color="b", label="Брезенхема(float)")
            plt.xlabel("Угол в градусах")
            plt.ylabel("Количество ступенек")
            plt.legend()

            stadging = []
            xe = xs
            ye = ys + l
            for i in range(angle, 90, angle):
                tmpXe = xe
                xe = xs + (xe - xs) * cos(angleRad) + (ye - ys) * sin(angleRad)
                ye = ys - (tmpXe - xs) * sin(angleRad) + (ye - ys) * cos(angleRad)
                
                dx = abs(xe - xs)
                dy = abs(ye - ys)
                stadging.append([i, min(dx, dy)])

            x = []
            y = []
            for i in range(len(stadging)):
                x.append(stadging[i][0])
                y.append(stadging[i][1])
            plt.plot(x, y, color="y", label="Брезенхема(сглаживание)")
            plt.xlabel("Угол в градусах")
            plt.ylabel("Количество ступенек")
            plt.legend()

            stadging = []
            xe = xs
            ye = ys + l
            for i in range(angle, 90, angle):
                tmpXe = xe
                xe = xs + (xe - xs) * cos(angleRad) + (ye - ys) * sin(angleRad)
                ye = ys - (tmpXe - xs) * sin(angleRad) + (ye - ys) * cos(angleRad)
                
                dx = abs(xe - xs)
                dy = abs(ye - ys)
                stadging.append([i, min(dx, dy)])

            x = []
            y = []
            for i in range(len(stadging)):
                x.append(stadging[i][0])
                y.append(stadging[i][1])
            plt.plot(x, y, color="c", label="Ву")
            plt.xlabel("Угол в градусах")
            plt.ylabel("Количество ступенек")
            plt.legend()

            plt.title("Длина отрезка " + str(int(l)))
            plt.legend()
            plt.show()
        except ValueError:
            self.showError()

    def cdaDraw(self, xs, ys, xe, ye, pen):
        if (abs(xe - xs) >= abs(ye - ys)):
            l = abs(int(xe - xs))
        else:
            l = abs(int(ye - ys))
        dx = (xe - xs) / l
        dy = (ye - ys) / l
        for i in range(l):
            self.pixelDraw(mathRound(xs), mathRound(ys), pen)
            xs += dx
            ys += dy

    def brezFloatDraw(self, xs, ys, xe, ye, pen):
        try:
            swap = False
            dx = int(xe - xs)
            dy = int(ye - ys)
            xSign = sign(dx)
            ySign = sign(dy)
            dx = abs(dx)
            dy = abs(dy)
            if dy > dx:
                dx, dy = dy, dx
                swap = True
            if dx != 0:
                d = dy / dx
            else:
                d = 0
            e = d - 0.5

            for i in range(dx):
                self.pixelDraw(xs, ys, pen)
                if not swap:
                    if e >= 0:
                        ys += ySign
                        e -= 1
                    xs += xSign
                else:
                    if e >= 0:
                        xs += xSign
                        e -= 1
                    ys += ySign
                e += d
        except ZeroDivisionError:
            print(xs, xe, dx)

    def brezIntDraw(self, xs, ys, xe, ye, pen):
        swap = False
        dx = int(xe - xs)
        dy = int(ye - ys)
        xSign = sign(dx)
        ySign = sign(dy)
        dx = abs(dx)
        dy = abs(dy)
        if dy > dx:
            dx, dy = dy, dx
            swap = True
        e = 2 * dy - dx
        for i in range(dx):
            self.pixelDraw(xs, ys, pen)
            if swap:
                if e >= 0:
                    xs += xSign
                    e -= 2 * dx
                ys += ySign
            else:
                if e >= 0:
                    ys += ySign
                    e -= 2 * dx
                xs += xSign
            e += 2 * dy

    def brezStageEliminateDraw(self, xs, ys, xe, ye, color, pen):
        dx = int(xe - xs)
        dy = int(ye - ys)
        xSign = sign(dx)
        ySign = sign(dy)
        dx = abs(dx)
        dy = abs(dy)
        swap = False

        if dy > dx:
            swap = True
            dx, dy = dy, dx

        m = dy / dx
        e = 0.5
        w = 1 - m

        for i in range(dx):
            curColor = color[:]
            curColor[3] *= e

            curColor[0] /= 255
            curColor[1] /= 255
            curColor[2] /= 255

            curColor[0] = ((1 - curColor[3]) + curColor[3] * curColor[0]) * 255
            curColor[1] = ((1 - curColor[3]) + curColor[3] * curColor[1]) * 255
            curColor[2] = ((1 - curColor[3]) + curColor[3] * curColor[2]) * 255

            pen.setColor(QtGui.QColor(int(curColor[0]), int(curColor[1]), int(curColor[2])))

            if not swap:
                self.pixelDraw(xs, ys + ySign, pen)
                if e >= w:
                    ys += ySign
                    e -= w + m
                xs += xSign
            else:
                self.pixelDraw(xs + xSign, ys, pen)
                if e >= w:
                    xs += xSign
                    e -= w + m
                ys += ySign
            e += m            

    def vuDraw(self, xs, ys, xe, ye, color, pen):
        #беды со спектром, левая половина улетает
        dx = float(xe - xs)
        dy = float(ye - ys)
        xSign = sign(dx)
        ySign = sign(dy)
        dx = fabs(dx)
        dy = fabs(dy)
        swap = False
        m = 1

        if dy > dx:
            if ys > ye:
                xs, xe = xe, xs
                ys, ye = ye, ys
                swap = True
            if dy != 0:
                m = float(dx / dy) * xSign * ySign

            xs -= 0.5
            for y in range(int(mathRound(ys)), int(mathRound(ye) + 1)):
                d1 = xs - floor(xs)
                d2 = 1 - d1
                colord2 = color[:]
                colord2[3] *= fabs(d2)

                colord2[0] /= 255
                colord2[1] /= 255
                colord2[2] /= 255

                colord2[0] = ((1 - colord2[3]) + colord2[3] * colord2[0]) * 255
                colord2[1] = ((1 - colord2[3]) + colord2[3] * colord2[1]) * 255
                colord2[2] = ((1 - colord2[3]) + colord2[3] * colord2[2]) * 255

                pen.setColor(QtGui.QColor(int(colord2[0]), int(colord2[1]), int(colord2[2])))
                self.pixelDraw(int(xs), y, pen)

                colord1 = color[:]
                colord1[3] *= fabs(d1)

                colord1[0] /= 255
                colord1[1] /= 255
                colord1[2] /= 255

                colord1[0] = ((1 - colord1[3]) + colord1[3] * colord1[0]) * 255
                colord1[1] = ((1 - colord1[3]) + colord1[3] * colord1[1]) * 255
                colord1[2] = ((1 - colord1[3]) + colord1[3] * colord1[2]) * 255

                pen.setColor(QtGui.QColor(int(colord1[0]), int(colord1[1]), int(colord1[2])))
                self.pixelDraw(int(xs) + 1, y, pen)

                xs += m
        else:
            if xs > xe:
                xs, xe = xe, xs
                ys, ye = ye, ys
                swap = True
            if dx != 0:
                m = float(dy / dx) * xSign * ySign

            # ys -= 0.5
            for x in range(int(mathRound(xs)), int(mathRound(xe) + 1)):
                d1 = ys - floor(ys)
                d2 = 1 - d1
                colord2 = color[:]
                colord2[3] *= fabs(d2)

                colord2[0] /= 255
                colord2[1] /= 255
                colord2[2] /= 255

                colord2[0] = ((1 - colord2[3]) + colord2[3] * colord2[0]) * 255
                colord2[1] = ((1 - colord2[3]) + colord2[3] * colord2[1]) * 255
                colord2[2] = ((1 - colord2[3]) + colord2[3] * colord2[2]) * 255

                pen.setColor(QtGui.QColor(int(colord2[0]), int(colord2[1]), int(colord2[2])))
                self.pixelDraw(x, int(ys), pen)

                colord1 = color[:]
                colord1[3] *= fabs(d1)

                colord1[0] /= 255
                colord1[1] /= 255
                colord1[2] /= 255

                colord1[0] = ((1 - colord1[3]) + colord1[3] * colord1[0]) * 255
                colord1[1] = ((1 - colord1[3]) + colord1[3] * colord1[1]) * 255
                colord1[2] = ((1 - colord1[3]) + colord1[3] * colord1[2]) * 255

                pen.setColor(QtGui.QColor(int(colord1[0]), int(colord1[1]), int(colord1[2])))
                self.pixelDraw(x, int(ys) + 1, pen)

                ys += m

    def pixelDraw(self, x, y, colorPen):
        self.scene.addLine(x, y, x, y, colorPen)

    def showError(self):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText("Введенные параметры не являются вещественным числом.")
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.exec_()

def mathRound(x):
        if (x >= 0):
            return x + 0.5
        else:
            return x - 0.5

def sign(x):
    if x > 0:
        return 1
    else:
        return -1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myApp()
    MainWindow.show()
    sys.exit(app.exec_())