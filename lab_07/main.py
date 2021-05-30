from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QColor, QPixmap, QPainter
from ui import Ui_MainWindow
from math import sqrt

EPS = 1e-3

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
                self.cutterMode = 'endCutter'
            elif self.cutterMode == 'endCutter':
                self.reDrawCutter(x, y)
                self.cutter.append([x, y])
                self.cutterMode = 'doneCutter'
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
        print("Start cutter-input")
        self.setColorCutter()
        if self.cutterMode == 'null':
            self.cutterMode = 'startCutter'
        self.mode = 'null'

    def lineInput(self):
        print("Start line-input")
        self.setColorLine()
        self.mode = 'startLine'

    def cut(self):
        self.swapCutterValue()
        for i in range(len(self.line)):
            p1 = [self.line[i][0][0], self.line[i][0][1]]
            p2 = [self.line[i][1][0], self.line[i][1][1]]
            t1 = self.checkPointVisibility(p1[0], p1[1])
            t2 = self.checkPointVisibility(p2[0], p2[1])
            s1 = self.codeSum(t1)
            s2 = self.codeSum(t2)
            if not(s1 or s2): # отрезок полностью видим
                pass
                # print("{0}: all-visible".format(i))
                self.res.append([p1, p2])
            else:
                p = self.codeSumLine(t1, t2)
                if p != 0: # отрезок невидим
                    pass
                    # print("{0}: all-invisible".format(i))
                else:
                    self.findIntersection(p1, p2)
        
        self.clearCache()
        self.setColorCutted()
        # print("Visible parts: {0}".format(len(self.res)))
        for i in range(len(self.res)):
            # print("Point-size: {0}".format(len(self.res[i])), end='')
            if len(self.res[i]) == 2:
                # print(" {0} {1}".format(self.res[i][0], self.res[i][1]))
                self.lineDraw(self.res[i][0][0], self.res[i][0][1], self.res[i][1][0], self.res[i][1][1])
        self.res.clear()
        self.setColorLine()

    def swapCutterValue(self):
        if self.cutter[0][0] > self.cutter[1][0]:
            self.cutter[0][0], self.cutter[1][0] = self.cutter[1][0], self.cutter[0][0]

        if self.cutter[0][1] > self.cutter[1][1]:
            self.cutter[0][1], self.cutter[1][1] = self.cutter[1][1], self.cutter[0][1]

    def checkPointVisibility(self, x, y):
        if self.mathRound(x) < self.cutter[0][0]:
            t1 = 1
        else:
            t1 = 0
        
        if self.mathRound(x) > self.cutter[1][0]:
            t2 = 1
        else:
            t2 = 0

        if self.mathRound(y) < self.cutter[0][1]:
            t3 = 1
        else:
            t3 = 0

        if self.mathRound(y) > self.cutter[1][1]:
            t4 = 1
        else:
            t4 = 0

        t = [t1, t2, t3, t4]
        return t

    def codeSum(self, t):
        s = 0
        for i in range(4):
            s+= t[i]
        return s
    
    def codeSumLine(self, t1, t2):
        p = 0
        for i in range(4):
            p += t1[i] * t2[i]
        return p

    def findIntersection(self, p1, p2):
        # cut = [[self.cutter[0][0], self.cutter[0][1]], [self.cutter[1][0], self.cutter[1][1]]]
        flag = False
        r = p1
        if self.codeSum(self.checkPointVisibility(p2[0], p2[1])):
            while (self.lineLength(p1, p2) > EPS):
                pAverage = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
                if self.codeSumLine(self.checkPointVisibility(pAverage[0], pAverage[1]), self.checkPointVisibility(p2[0], p2[1])):
                    p2 = pAverage
                else:
                    p1 = pAverage

            if not(self.codeSumLine(self.checkPointVisibility(p1[0], p1[1]), self.checkPointVisibility(p2[0], p2[1]))):
                flag = True
                self.addPoint(p1, 0)
        else:
            flag = True
            self.addPoint(p2, 0)
        
        if flag:
            p1, p2 = p2, r
            if self.codeSum(self.checkPointVisibility(p2[0], p2[1])):
                while (self.lineLength(p1, p2) > EPS):
                    pAverage = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
                    if self.codeSumLine(self.checkPointVisibility(pAverage[0], pAverage[1]), self.checkPointVisibility(p2[0], p2[1])):
                        p2 = pAverage
                    else:
                        p1 = pAverage

                if not(self.codeSumLine(self.checkPointVisibility(p1[0], p1[1]), self.checkPointVisibility(p2[0], p2[1]))):
                    self.addPoint(p1, 1)
            else:
                self.addPoint(p2, 1)

    def addPoint(self, p, mode):
        cut = [[self.cutter[0][0], self.cutter[0][1]], [self.cutter[1][0], self.cutter[1][1]]]
        if abs(p[0] - self.cutter[0][0]) < 2:
            p[0] = self.cutter[0][0]
        elif abs(p[0] -  self.cutter[1][0]) < 2:
            p[0] = self.cutter[1][0]

        if abs(p[1] - self.cutter[0][1]) < 2:
            p[1] = self.cutter[0][1]
        elif abs(p[1] - self.cutter[1][1]) < 2:
            p[1] = self.cutter[1][1]

        if mode == 0:
            self.res.append([p])
        else:
            self.res[len(self.res) - 1].append(p)

    def lineLength(self, p1, p2):
        return sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))
    
    def clearCache(self):
        self.painter.setPen(QtCore.Qt.white)
        for i in range(self.cutter[0][0], self.cutter[1][0] + 1):
            self.lineDraw(i, self.cutter[0][1], i, self.cutter[1][1])
        self.setColorCutter()
        self.reDrawCutter(self.cutter[1][0], self.cutter[1][1])

    def reDrawCutter(self, xe, ye):
        self.lineDraw(self.cutter[0][0], self.cutter[0][1], self.cutter[0][0], ye)
        self.lineDraw(self.cutter[0][0], self.cutter[0][1], xe, self.cutter[0][1])
        self.lineDraw(xe, self.cutter[0][1], xe, ye)
        self.lineDraw(self.cutter[0][0], ye, xe, ye)
    
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
        # for i in range(l + 1):
        #     self.painter.drawPoint((xs), (ys))
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
            self.image.fill(QtCore.Qt.white)
            self.reDraw()
            self.setColorLine()
            self.reDrawLines()
            self.setColorCutter()
            #redrawAll
    
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