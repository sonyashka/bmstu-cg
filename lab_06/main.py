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
        self.point = False
        self.pointX = 0
        self.pointY = 0
        self.stack = []
        self.leftX = -1
        self.rightX = -1

        self.functions()

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()
        #800x555
        self.graphicsView.setGeometry(QtCore.QRect(10, 0, width - 220, height - 41))
        self.colorBox.setGeometry(QtCore.QRect(width - 190, 120, 171, 22))
        self.labelColor.setGeometry(QtCore.QRect(width - 190, 90, 171, 31))
        self.labelMethod.setGeometry(QtCore.QRect(width - 190, 160, 171, 31))
        self.paintBox.setGeometry(QtCore.QRect(width - 190, 190, 171, 22))
        self.paintBut.setGeometry(QtCore.QRect(width - 150, 230, 93, 28))
        self.labelTitle.setGeometry(QtCore.QRect(width - 190, 10, 171, 51))
        self.label.setGeometry(QtCore.QRect(width - 190, 270, 171, 251))
        self.menubar.setGeometry(QtCore.QRect(0, 0, width, 26))
        self.sceneResize()

    def sceneCreate(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.sceneWidth = self.graphicsView.width()
        self.sceneHeight = self.graphicsView.height()
        self.graphicsView.setSceneRect(0, 0, self.sceneWidth - 10, self.sceneHeight - 10)
        self.graphicsView.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.image = QImage(1800, 1000, QImage.Format_RGB32)
        self.image.fill(QtCore.Qt.white)
       
        self.painter = QPainter()
        self.painter.begin(self.image)
        self.painter.setPen(QtCore.Qt.black)
        self.painter.drawImage(0, 0, self.image)
        self.reDraw()

    def sceneResize(self):
        self.sceneWidth = self.graphicsView.width()
        self.sceneHeight = self.graphicsView.height()
        # self.image = QImage(self.sceneWidth, self.sceneHeight, QImage.Format_RGB32)
        # self.painter.begin(self.image)
        # self.painter.drawImage(0, 0, self.image)
        self.reDrawFig("clear")

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
        self.reDraw()

    def mousePressEvent(self, event):
        x = event.x() - 11
        y = event.y() - 27
        if x >= 0 and x <= self.sceneWidth and y >= 0 and y <= self.sceneHeight and self.mode == 'start':
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
        elif x >= 0 and x <= self.sceneWidth - 10 and y >= 0 and y <= self.sceneHeight - 10 and self.point:
            if self.pointX != 0 and self.pointY != 0:
                self.painter.setPen(QtCore.Qt.white)
                self.painter.drawPoint(self.pointX, self.pointY)
                self.setColor()
                self.reDrawFig("not")
            self.pointX = x
            self.pointY = y
            self.point = False
            print("Point [{0}, {1}] was choosen".format(x, y))
            self.painter.drawPoint(x, y)
        elif x >= 0 and x <= self.sceneWidth - 10 and y >= 0 and y <= self.sceneHeight - 10 and self.mode != 'start':
            self.showError(1)
            
        self.reDraw()

    def keyPressEvent(self, event):
        if not self.process:
            self.lastKeys[0], self.lastKeys[1] = self.lastKeys[1], event.key()
            if self.lastKeys[0] == 16777249 and self.lastKeys[1] == 83: # start ввода точек фигуры
                self.mode = 'start'
                self.xCur, self.yCur, self.xPrev, self.yPrev = -1, -1, -1, -1
                self.figure.append([])
                print('Start drawing')
            elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 69: # end ввода точек фигуры
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
            elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 67: # clear
                self.mode = 'null'
                self.figure = []
                self.barier = []
                self.xCur, self.yCur, self.xPrev, self.yPrev = -1, -1, -1, -1
                self.image.fill(QtCore.Qt.white)
                self.reDraw()
                print('Clear all')
            elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 81: #q - горизонт
                if self.line != 'horizontal':
                    self.line = 'horizontal'
                    print("Horizontal-line mode: ON")
                else:
                    self.line = 'ordinary'
                    print("Horizontal-line mode: OFF")
            elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 87: #w - вертикаль
                if self.line != 'vertical':
                    self.line = 'vertical'
                    print("Vertical-line mode: ON")
                else:
                    self.line = 'ordinary'
                    print("Vertical-line mode: OFF")
            elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 90: # убрать заливку
                # self.image.fill(QtCore.Qt.white)
                self.reDrawFig("clear")
                # self.reDraw()
            elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 80:
                print("Choose paint-point")
                self.point = True
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
            # print("Numb of figure: {0}".format(len(self.figure)))
            self.setColor()
            self.setMode()
            self.reDrawFig("clear")

            start = time.time()
            self.move = 'up'
            self.seedPaint(self.pointX, self.pointY)
            # self.reDrawFig("not")
            end = time.time()

            print("{0:.3f} s".format(end - start))
            self.setColor()
            self.process = False
        elif self.mode != 'end':
            self.showError(2)

    def seedPaint(self, x, y):
        curX = x
        curY = y 
        mode = "start"
        while (len(self.stack) != 0 or mode == "start"):
            self.painter.drawPoint(curX, curY)
            self.linePaint(curX, curY)
            if len(self.stack) != 0:
                cur = self.stack.pop(0)
                curX, curY = cur[0], cur[1]
            else:
                mode = "stop"

    def linePaint(self, x, y):
        curX = x

        while (self.pointValid(curX + 1, y) and self.checkPixel(curX + 1, y)):
            curX += 1
            self.painter.drawPoint(curX, y)
        self.rightX = curX

        curX = x
        while (self.pointValid(curX - 1, y) and self.checkPixel(curX - 1, y)):
            curX -= 1
            self.painter.drawPoint(curX, y)
        self.leftX = curX

        if self.method == "delay":
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents, 0)
        self.reDraw()

        mode = 0
        for i in range(self.leftX, self.rightX + 1):
            if self.pointValid(i, y + 1) and self.checkPixel(i, y + 1):
                if not mode:
                    self.stack.append([i, y + 1])
                    mode = 1
            else:
                if mode:
                    # self.stack.append(i)
                    mode = 0
        mode = 0
        for i in range(self.leftX, self.rightX + 1):
            if self.pointValid(i, y - 1) and self.checkPixel(i, y - 1):
                if not mode:
                    self.stack.append([i, y - 1])
                    mode = 1
            else:
                if mode:
                    # self.stack.append(i)
                    mode = 0

    def pointValid(self, x, y):
        if x >= 0 and x <= self.sceneWidth and y >= 0 and y <= self.sceneHeight:
            return 1
        else:
            return 0

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
            return 1
        else:
            return 0
            # self.painter.drawPoint(x, y)

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