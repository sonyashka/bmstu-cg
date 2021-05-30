from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QColor, QPixmap, QPainter
from ui import Ui_MainWindow
import time
import threading
from math import ceil, floor

class myApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.setupUi(self)
        self.sceneCreate()
        self.process = False
        self.lastKeys = [0, 0]
        self.mode = 'null'
        self.line = 'ordinary'
        self.figure = []
        self.barier = []
        self.xPrev = -1
        self.yPrev = -1
        self.xCur = -1
        self.yCur = -1

        self.functions()

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()
        #800x555
        self.graphicsView.setGeometry(QtCore.QRect(10, 0, width - 220, height - 41))
        self.colorBox.setGeometry(QtCore.QRect(width - 190, 190, 171, 22))
        self.labelColor.setGeometry(QtCore.QRect(width - 190, 160, 171, 31))
        self.labelMethod.setGeometry(QtCore.QRect(width - 190, 230, 171, 31))
        self.paintBox.setGeometry(QtCore.QRect(width - 190, 260, 171, 22))
        self.paintBut.setGeometry(QtCore.QRect(width - 150, 300, 93, 28))
        self.labelTitle.setGeometry(QtCore.QRect(width - 190, 80, 171, 51))
        self.menubar.setGeometry(QtCore.QRect(0, 0, width, 26))

    def sceneCreate(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.sceneWidth = self.graphicsView.width()
        self.sceneHeight = self.graphicsView.height()
        self.graphicsView.setSceneRect(0, 0, self.sceneWidth - 10, self.sceneHeight - 10)
        self.graphicsView.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.image= QImage(self.sceneWidth, self.sceneHeight, QImage.Format_RGB32)
        self.image.fill(QtCore.Qt.white)
       
        self.painter = QPainter()
        self.painter.begin(self.image)
        self.painter.setPen(QtCore.Qt.black)
        self.painter.drawImage(0, 0, self.image)

    def reDraw(self):
         self.pixmap = QPixmap.fromImage(self.image)
         self.scene.clear()
         self.scene.addPixmap(self.pixmap)

    def reDrawFig(self, mode):
        if mode == "clear":
            self.image.fill(QtCore.Qt.white)
        self.setColor()
        for i in range(len(self.figure)):
            for j in range(len(self.figure[i]) - 1):
                self.xCur, self.xNext = self.figure[i][j][0], self.figure[i][j + 1][0]
                self.yCur, self.yNext = self.figure[i][j][1], self.figure[i][j + 1][1]
                self.painter.drawLine(self.xCur, self.yCur, self.xNext, self.yNext)
        if mode != "no_redraw":
            self.reDraw()

    def mousePressEvent(self, event):
        x = event.x() - 10
        y = event.y() - 26
        if x >= 0 and x <= self.sceneWidth - 10 and y >= 0 and y <= self.sceneHeight - 10 and self.mode == 'start':
            self.xPrev, self.yPrev = self.xCur, self.yCur
            if self.line == 'horizontal': #q - горизонт линия
                self.xCur, self.yCur = x, self.yPrev
            elif self.line == 'vertical': #w - верт линия
                self.xCur, self.yCur = self.xPrev, y
            else:
                self.xCur, self.yCur = x, y
            if self.mode == 'start':
                print("Current point [{0}, {1}]".format(self.xCur, self.yCur))
                self.figure[len(self.figure) - 1].append([self.xCur, self.yCur])
                self.painter.drawPoint(self.xCur, self.yCur)
                if self.xPrev != -1 and self.yPrev != -1:
                    self.painter.drawLine(self.xCur, self.yCur, self.xPrev, self.yPrev)
        elif x >= 0 and x <= self.sceneWidth - 10 and y >= 0 and y <= self.sceneHeight - 10 and self.mode != 'start':
                self.showError(1)
            
        self.reDraw()

    def keyPressEvent(self, event):
        if not self.process:
            self.lastKeys[0], self.lastKeys[1] = self.lastKeys[1], event.key()
            if self.lastKeys[0] == 16777249 and self.lastKeys[1] == 83:
                self.mode = 'start'
                self.xCur, self.yCur, self.xPrev, self.yPrev = -1, -1, -1, -1
                self.figure.append([])
                print('Start drawing')
            elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 69:
                if len(self.figure[len(self.figure) - 1]) < 3:
                    self.showError(2)
                else:
                    self.mode = 'end'
                    self.figure[len(self.figure) - 1].append([self.figure[len(self.figure) - 1][0][0], self.figure[len(self.figure) - 1][0][1]])
                    self.painter.drawLine(self.xCur, self.yCur, self.figure[len(self.figure) - 1][0][0], self.figure[len(self.figure) - 1][0][1])
                    self.xCur, self.yCur, self.xPrev, self.yPrev = -1, -1, -1, -1
                    self.setColor()
                    self.reDrawFig("clear")
                    self.reDraw()
                    print('End drawing')
            elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 81: #q - горизонт
                if self.line != 'horizontal':
                    self.line = 'horizontal'
                    print("Horizontal-line mode: ON")
                else:
                    self.line = 'ordinary'
                    print("Horizontal-line mode: ON")
            elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 87: #w - вертикаль
                if self.line != 'vertical':
                    self.line = 'vertical'
                    print("Vertical-line mode: ON")
                else:
                    self.line = 'ordinary'
                    print("Vertical-line mode: ON")
            elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 67:
                self.mode = 'null'
                self.figure = []
                self.barier = []
                self.xCur, self.yCur, self.xPrev, self.yPrev = -1, -1, -1, -1
                self.image.fill(QtCore.Qt.white)
                self.reDraw()
                print('Clear all')
            elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 90:
                self.image.fill(QtCore.Qt.white)
                self.reDrawFig("clear")
                self.reDraw()
            elif self.lastKeys[1] == 16777220:
                if self.mode == 'end':
                    self.paint()
                else:
                    self.showError(2)
            # else:
            #     print(event.key())

    def functions(self):
        self.paintBut.clicked.connect(lambda: self.paint())

    def paint(self):
        if not self.process and self.mode == 'end':
            self.process = True
            print("Numb of figure: {0}".format(len(self.figure)))
            self.setColor()
            self.setMode()
            self.reDrawFig("clear")

            start = time.time()
            self.findBariers()
            print("Barier list: {0}".format(self.barier))
            for i in range(len(self.figure)):
                self.paintOneFig(i)
            self.reDrawFig("not")
            end = time.time()

            print("{0:.3f} s".format(end - start))
            self.setColor()
            self.process = False
        elif self.mode != 'end':
            self.showError(2)

    def paintOneFig(self, ind):
        curBar = self.barier[ind]
        prevDy, firstDy = 0, 0
        for i in range(len(self.figure[ind]) - 1):
            xCur, xNext = self.figure[ind][i][0], self.figure[ind][i + 1][0]
            yCur, yNext = self.figure[ind][i][1], self.figure[ind][i + 1][1]
            if yCur != yNext:
                dy = self.sign(yCur, yNext)
                if i == 0:
                    firstDy = dy
                dx = (xNext - xCur) / abs(yNext - yCur)
                x = xCur
                if yNext > yCur:
                    yNext += 1
                    if dy == prevDy:
                        yCur += 1
                    if i == len(self.figure[ind]) - 2 and dy == firstDy:
                        yNext -= 1
                if yNext < yCur:
                    yNext -= 1
                    if dy == prevDy:
                        yCur -= 1
                    if i == len(self.figure[ind]) - 2 and dy == firstDy:
                        yNext += 1
                prevDy = dy
                for j in range(yCur, yNext, dy):
                    if x < curBar:
                        for k in range(floor(x), curBar):
                            self.checkPixel(k, j)
                        # self.checkPixel(ceil(x) - 1, j)
                    else:
                        for k in range(curBar, ceil(x)):
                            self.checkPixel(k, j)
                        # self.checkPixel(floor(x), j)
                    if self.method == "delay":
                        self.reDrawFig("no_redraw")
                        self.reDraw()
                        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents, 0) # замедляет выполнение всех процессов, найти сброс!
                    x += dx
    
    def sign(self, x1, x2):
        if x1 > x2:
            return -1
        else:
            return 1

    def mathRound(self, x):
        if x >= 0:
            return int(x + 0.5)
        else:
            return int(x - 0.5)

    def setColor(self):
        color = self.colorBox.currentIndex()
        if color == 0:
            self.painter.setPen(QtCore.Qt.black)
        elif color == 1:
            self.painter.setPen(QtCore.Qt.red)
        elif color == 2:
            self.painter.setPen(QtCore.Qt.green)
        else:
            self.painter.setPen(QtCore.Qt.blue)

    def setMode(self):
        method = self.paintBox.currentIndex()
        if method == 1:
            self.method = "no delay"
        else:
            self.method = "delay"

    def checkPixel(self, x, y):
        if self.image.pixelColor(x, y).name() == "#ffffff":
            self.setColor()
        else:
            self.painter.setPen(QtCore.Qt.white)
        self.painter.drawPoint(x, y)

    def findBariers(self):
        self.barier.clear()
        for i in range(len(self.figure)):
            curMax, curMin = self.figure[i][0][0], self.figure[i][0][0]
            for j in range(1, len(self.figure[i]) - 1):
                if self.figure[i][j][0] > curMax:
                    curMax = self.figure[i][j][0]
                if self.figure[i][j][0] < curMin:
                    curMin = self.figure[i][j][0]
            curBar = (curMax + curMin) / 2
            self.barier.append(int(curBar))

    def showError(self, mode):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Ошибка")
        if mode == 1:
            error.setText("Вы находитесь вне режима внесения точек фигуры.")
        elif mode == 2:
            error.setText("Фигура вырождена в прямую/точку или не дорисована. Добавьте вершин.")
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myApp()
    MainWindow.show()
    sys.exit(app.exec_())