from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QColor, QPixmap, QPainter
from ui import Ui_MainWindow
from math import sqrt

EPS = sqrt(2)

class myApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.setupUi(self)
        self.sceneCreate()
        self.lastKeys = [0, 0]
        self.lineMode = 'ordinary'
        self.line = []
        self.cutter = []
        self.res = []
        self.mode = 'null'
        self.cutterMode = 'null'

        self.functions()

    def mousePressEvent(self, event):
        x = event.x() - 11
        y = event.y() - 37
        if x >= 0 and y >= 0 and x <= self.sceneWidth and y <= self.sceneHeight:
            if self.mode == 'startLine':
                self.painter.drawPoint(x, y)
                self.reDraw()
                self.line.append([[x, y]])
                self.mode = 'endLine'
            elif self.mode == 'endLine':
                if self.lineMode == 'horizontal':
                    y = self.line[len(self.line) - 1][0][1]
                elif self.lineMode == 'vertical':
                    x = self.line[len(self.line) - 1][0][0]
                self.line[len(self.line) - 1].append([x, y])
                self.lineDraw(self.line[len(self.line) - 1][0][0], self.line[len(self.line) - 1][0][1], self.line[len(self.line) - 1][1][0], self.line[len(self.line) - 1][1][1])
                # self.line[len(self.line) - 1].append([x, y])
                self.mode = 'startLine'
            elif self.cutterMode == 'startCutter':
                self.cutter.append([x, y])
                self.cutterMode = 'inputCutter'
            elif self.cutterMode == 'inputCutter':
                # self.reDrawCutter(x, y)
                if self.lineMode == 'horizontal':
                    y = self.cutter[len(self.cutter) - 1][1]
                elif self.lineMode == 'vertical':
                    x = self.cutter[len(self.cutter) - 1][0]
                # print(self.cutter[len(self.cutter) - 1][0], self.cutter[len(self.cutter) - 1][1], x, y)
                self.lineDraw(self.cutter[len(self.cutter) - 1][0], self.cutter[len(self.cutter) - 1][1], x, y)
                self.cutter.append([x, y])
                # self.cutterMode = 'doneCutter'
            elif self.cutterMode == 'doneCutter' or len(self.cutter) != 0:
                self.newCutterQ()

    def keyPressEvent(self, event):
        self.lastKeys[0], self.lastKeys[1] = self.lastKeys[1], event.key()
        if self.lastKeys[0] == 16777249 and self.lastKeys[1] == 81: #q - горизонт
            if self.lineMode != 'horizontal':
                self.lineMode = 'horizontal'
                print("Horizontal-line mode: ON")
            else:
                self.lineMode = 'ordinary'
                print("Horizontal-line mode: OFF")
        elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 87: #w - вертикаль
            if self.lineMode != 'vertical':
                self.lineMode = 'vertical'
                print("Vertical-line mode: ON")
            else:
                self.lineMode = 'ordinary'
                print("Vertical-line mode: OFF")
        elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 67: # clear
            self.mode = 'null'
            self.cutterMode = 'null'
            self.cutter.clear()
            self.line.clear()
            self.image.fill(QtCore.Qt.white)
            self.reDraw()
            print('Clear all')
        elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 90: # отмена отсечения
            self.image.fill(QtCore.Qt.white)
            self.setColorCutter()
            self.reDrawCutter()
            self.setColorLine()
            self.reDrawLines()
            self.reDraw()
        # else:
        #     print(event.key())

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()
        #800x600
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, width - 220, height - 50))
        self.actionLabel.setGeometry(QtCore.QRect(width - 190, 190, 171, 41))
        self.cutterInputBut.setGeometry(QtCore.QRect(width - 190, 240, 171, 41))
        self.lineInputBut.setGeometry(QtCore.QRect(width - 190, 300, 171, 41))
        self.cutBut.setGeometry(QtCore.QRect(width - 190, 360, 171, 41))
        self.colorCutterBox.setGeometry(QtCore.QRect(width - 190, 40, 171, 22))
        self.butLabel.setGeometry(QtCore.QRect(width - 190, 400, 171, 151))
        self.colorCutterLabel.setGeometry(QtCore.QRect(width - 190, 10, 171, 31))
        self.colorCuttedBox.setGeometry(QtCore.QRect(width - 190, 160, 171, 22))
        self.colorCuttedLabel.setGeometry(QtCore.QRect(width - 190, 130, 171, 31))
        self.colorLineBox.setGeometry(QtCore.QRect(width - 190, 100, 171, 22))
        self.colorLineLabel.setGeometry(QtCore.QRect(width - 190, 70, 171, 31))
        self.menubar.setGeometry(QtCore.QRect(0, 0, width, 26))
        self.sceneResize()

    def sceneCreate(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.sceneResize()
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

    def reDraw(self):
         self.pixmap = QPixmap.fromImage(self.image)
         self.scene.clear()
         self.scene.addPixmap(self.pixmap)

    def setColor(self):
        self.setColorCutter()
        self.setColorLine()
        self.setColorCutted()

    def setColorCutter(self):
        color = self.colorCutterBox.currentIndex()
        if color == 0:
            self.painter.setPen(QtCore.Qt.red)
        elif color == 1:
            self.painter.setPen(QtCore.Qt.green)
        else:
            self.painter.setPen(QtCore.Qt.blue)

    def setColorLine(self):
        color = self.colorLineBox.currentIndex()
        if color == 0:
            self.painter.setPen(QtCore.Qt.black)
        elif color == 1:
            self.painter.setPen(QtCore.Qt.gray)
        else:
            self.painter.setPen(QtCore.Qt.magenta)

    def setColorCutted(self):
        color = self.colorCuttedBox.currentIndex()
        if color == 0:
            self.painter.setPen(QColor(255, 128, 0))
        elif color == 1:
            self.painter.setPen(QtCore.Qt.yellow)
        else:
            self.painter.setPen(QtCore.Qt.cyan)

    def functions(self):
        self.cutterInputBut.clicked.connect(lambda: self.cutterInput())
        self.lineInputBut.clicked.connect(lambda: self.lineInput())
        self.cutBut.clicked.connect(lambda: self.cut())

    def cutterInput(self):
        self.setColorCutter()
        if self.cutterMode == 'null':
            self.cutterMode = 'startCutter'
        elif self.cutterMode == 'inputCutter':
            self.cutterMode = 'doneCutter'
            self.lineDraw(self.cutter[0][0], self.cutter[0][1], self.cutter[len(self.cutter) - 1][0], self.cutter[len(self.cutter) - 1][1])
            self.cutter.append([self.cutter[0][0], self.cutter[0][1]])
            self.cutter.append([self.cutter[1][0], self.cutter[1][1]])
        self.mode = 'null'

    def lineInput(self):
        self.setColorLine()
        self.mode = 'startLine'

    def cut(self):
        self.setColorCutted()
        if self.checkConvexity() and self.checkIntersection(self.cutter):
        # if self.checkIntersection():
            for i in range(len(self.line)):
                self.findIntersection(i)
            
            # self.clearCache()
            self.setColorCutted()
            # print("Visible parts: {0}".format(len(self.res)))
            for i in range(len(self.res)):
                # print("Point-size: {0}".format(len(self.res[i])), end='')
                if len(self.res[i]) == 2:
                    # print(" {0} {1}".format(self.res[i][0], self.res[i][1]))
                    self.lineDraw(self.res[i][0][0], self.res[i][0][1], self.res[i][1][0], self.res[i][1][1])
            self.res.clear()
            self.setColorLine()
        else:
            self.showErrorNotConvexity()

    def checkConvexity(self):
        res = True
        resSign = 0
        i = 0
        while res and i < len(self.cutter) - 2:
            c11 = [self.cutter[i][0], self.cutter[i][1]]
            c12 = [self.cutter[i + 1][0], self.cutter[i + 1][1]]
            c1 = [c12[0] - c11[0], c12[1] - c11[1]]

            c21 = c12
            c22 = [self.cutter[i + 2][0], self.cutter[i + 2][1]]
            c2 = [c22[0] - c21[0], c22[1] - c21[1]]

            determinator = c1[0] * c2[1] - c1[1] * c2[0]
            if resSign == -1 and determinator <=0:
                # res = True
                pass
            elif resSign == 0:
                if determinator > 0:
                    resSign = 1
                elif determinator < 0:
                    resSign = -1
            elif resSign == 1 and determinator >= 0:
                # res = True
                pass
            else:
                res = False
            i += 1
        return res

    def checkIntersection(self, fig):
        res = True
        for i in range(len(fig) - 3):
            for j in range(i + 2, len(fig) - 2):
                # print(i,s j)
                c11 = [fig[i][0], fig[i][1]]
                c12 = [fig[i + 1][0], fig[i + 1][1]]
                
                c21 = [fig[j][0], fig[j][1]]
                c22 = [fig[j + 1][0], fig[j + 1][1]]
                    
                c1 = [c11, c12]
                c2 = [c21, c22]
                    
                if i == 0 and j == len(fig) - 3:
                    pass
                elif self.isIntersec(c1, c2)[0] != -1:
                    res = False # стороны пересекаются
                # print(f"intersec {intersection}")
        return res

    def isIntersec(self, c1, c2):
        resPoint = [-1, -1]
        if c1[0][0] >= c1[1][0]:
            c1[0], c1[1] = c1[1], c1[0]
        if c2[0][0] >= c2[1][0]:
            c2[0], c2[1] = c2[1], c2[0]

        if c1[1][0] == c1[0][0]:
            k1 = 0
        else:
            k1 = (c1[1][1] - c1[0][1]) / (c1[1][0] - c1[0][0])

        if c2[1][0] == c2[0][0]:
            k2 = 0
        else:
            k2 = (c2[1][1] - c2[0][1]) / (c2[1][0] - c2[0][0])
        
        if k1 != k2:
            b1 = c1[0][1] - k1 * c1[0][0]
            b2 = c2[0][1] - k2 * c1[0][0]

            x = (b2 - b1) / (k1 - k2)
            y = k1 * x + b1

            layOnFirst = False
            layOnSecond = False
            if x >= c1[0][0] and x <= c1[1][0] and y >= min(c1[0][1], c1[1][1]) and y <= max(c1[0][1], c1[1][1]):
                layOnFirst = True
            if x >= c2[0][0] and x <= c2[1][0] and y >= min(c2[0][1], c2[1][1]) and y <= max(c2[0][1], c2[1][1]):
                layOnSecond = True
            if layOnFirst and layOnSecond:
                resPoint = [x, y]
        return resPoint
           
    def findIntersection(self, i):
        tLow, tHigh = 0, 1
        p1 = [self.line[i][0][0], self.line[i][0][1]]
        p2 = [self.line[i][1][0], self.line[i][1][1]]
        D = [self.line[i][1][0] - self.line[i][0][0], self.line[i][1][1] - self.line[i][0][1]]
        for j in range(len(self.cutter) - 2):# помни что в массиве вершин отсекателя лежат еще нулевая вершина и первая для удобства обращения
            # вычисление параметров вектора внутренней нормали nвн
            tmp0 = [self.cutter[j][0], self.cutter[j][1]]
            tmp1 = [self.cutter[j + 1][0], self.cutter[j + 1][1]]
            tmp2 = [self.cutter[j + 2][0], self.cutter[j + 2][1]]
            n = self.normal([tmp1[0] - tmp0[0], tmp1[1] - tmp0[1]], [tmp2[0] - tmp1[0], tmp2[1] - tmp1[0]])
            # n = [self.cutter[j][0] - self.cutter[j + 1][0], self.cutter[j + 1][1] - self.cutter[j][1]]
            # self.lineDraw(tmp0[0], tmp0[1], tmp0[0] + n[0] * 10, tmp0[1] + n[1] * 10)
            # if (n[0] * (tmp2[0] - tmp1[0]) + n[1] * (tmp2[1] - tmp1[1]) < 0):
            #     n[0], n[1] = n[0] * (-1), n[1] * (-1)
            w = [self.line[i][0][0] - tmp0[0], self.line[i][0][1] - tmp0[1]]
            wScalar = w[0] * n[0] + w[1] * n[1]
            DScalar = D[0] * n[0] + D[1] * n[1]
            if DScalar == 0:
                if wScalar > 0:
                    pass # переход к следующему шагу цикла
                else:
                    return # отрезок невиден
            else:
                t = -wScalar / DScalar
            
            if DScalar > 0:
                if t > 1:
                    return # отрезок невиден
                else:
                    tLow = max(tLow, t)
            elif t < 0:
                return # отрезок невиден
            else:
                tHigh = min(tHigh, t)

        if tLow <= tHigh:
            pLow = self.paramPoint(self.line[i][0], self.line[i][1], tLow)
            pHigh = self.paramPoint(self.line[i][0], self.line[i][1], tHigh)
            self.res.append([pLow, pHigh])

    def normal(self, c1, c2):
        if c1[0] == 0:
            n = [1, 0]
        else:
            n = [-c1[1] / c1[0], 1]

        if (n[0] * c2[0] + n[1] * c2[1]) < 0:
            n[0], n[1] = n[0] * (-1), n[1] * (-1)
        return n
        
    def paramPoint(self, p1, p2, t):
        x = p1[0] + (p2[0] - p1[0]) * t
        y = p1[1] + (p2[1] - p1[1]) * t
        return [x, y]

    def lineLength(self, p1, p2):
        return sqrt(pow(p1[0] - p2[0], 2) * pow(p1[1] - p2[1], 2))

    def clearCache(self):
        self.painter.setPen(QtCore.Qt.white)
        self.setColorCutter()
        self.reDrawCutter()

    def reDrawCutter(self):
        for i in range(len(self.cutter) - 2):# помни что в массиве вершин отсекателя лежат еще нулевая вершина и первая для удобства обращения
            self.lineDraw(self.cutter[i][0], self.cutter[i][1], self.cutter[i + 1][0], self.cutter[i + 1][1])
    
    def reDrawLines(self):
        for i in range(len(self.line)):
            self.lineDraw(self.line[i][0][0], self.line[i][0][1], self.line[i][1][0], self.line[i][1][1])

    def lineDraw(self, xs, ys, xe, ye): #цда
        self.painter.drawLine(xs, ys, xe, ye)
        # if (abs(xe - xs) >= abs(ye - ys)):
        #     l = abs(int(xe - xs))
        # else:
        #     l = abs(int(ye - ys))
        # if l == 0:
        #     l = 1
        # dx = (xe - xs) / l
        # dy = (ye - ys) / l
        # for i in range(l):
        #     self.painter.drawPoint(self.mathRound(xs), self.mathRound(ys))
        #     xs += dx
        #     ys += dy
        self.reDraw()

    def newCutterQ(self):
        newCutter = QtWidgets.QMessageBox()
        newCutter.setWindowTitle("Переопределение")
        newCutter.setText("Вы уже ввели отсекатель. Хотите задать новый?")
        newCutter.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        newCutter.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        newCutter.setIcon(QtWidgets.QMessageBox.Question)
        ret = newCutter.exec()
        if ret == QtWidgets.QMessageBox.Yes:
            self.cutterMode = 'startCutter'
            self.cutter.clear()
            self.setColorLine()
            self.image.fill(QtCore.Qt.white)
            self.reDrawLines()
            self.setColorCutter()
            #redrawAll

    def showErrorNotConvexity(self):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText("Отсекатель не является выпуклым. Введите новый")
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.exec()
    
    def mathRound(self, x):
        if x >= 0:
            return int(x + 0.5)
        else:
            return int(x - 0.5)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myApp()
    MainWindow.show()
    sys.exit(app.exec_())