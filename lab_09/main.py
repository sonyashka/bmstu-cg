from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QColor, QPixmap, QPainter
from ui import Ui_MainWindow
from math import sqrt
from numpy import sign, linalg, dot
from copy import deepcopy

class myApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.setupUi(self)
        self.sceneCreate()
        self.lastKeys = [0, 0]
        self.lineMode = 'ordinary'
        self.figure = []
        self.cutter = []
        self.res = []
        self.cutterMode = 'null'
        self.figureMode = 'null'
        self.lastInput = 'null'

        self.functions()

    def mousePressEvent(self, event):
        x = event.x() - 11
        y = event.y() - 37
        if x >= 0 and y >= 0 and x <= self.sceneWidth and y <= self.sceneHeight:
            if self.figureMode == 'startFigure':
                self.figure.append([x, y])
                self.figureMode = 'inputFigure'
            elif self.figureMode == 'inputFigure':
                if self.lineMode == 'horizontal':
                    y = self.figure[len(self.figure) - 1][1]
                elif self.lineMode == 'vertical':
                    x = self.figure[len(self.figure) - 1][0]
                # print(self.figure[len(self.figure) - 1][0], self.figure[len(self.figure) - 1][1], x, y)
                self.lineDraw(self.figure[len(self.figure) - 1][0], self.figure[len(self.figure) - 1][1], x, y)
                self.figure.append([x, y])
            elif self.cutterMode == 'startCutter':
                self.cutter.append([x, y])
                self.cutterMode = 'inputCutter'
            elif self.cutterMode == 'inputCutter':
                if self.lineMode == 'horizontal':
                    y = self.cutter[len(self.cutter) - 1][1]
                elif self.lineMode == 'vertical':
                    x = self.cutetr[len(self.cutter) - 1][0]
                # print(self.cutter[len(self.cutter) - 1][0], self.cutter[len(self.cutter) - 1][1], x, y)
                self.lineDraw(self.cutter[len(self.cutter) - 1][0], self.cutter[len(self.cutter) - 1][1], x, y)
                self.cutter.append([x, y])
            elif self.lastInput == 'cutter' and (self.cutterMode == 'doneCutter' or len(self.cutter) != 0):
                self.newCutterQ()
            elif self.lastInput == 'figure' and (self.figureMode == 'doneFigure' or len(self.figure) != 0):
                self.newFigureQ()

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
            self.figureMode = 'null'
            self.cutterMode = 'null'
            self.cutter.clear()
            self.figure.clear()
            self.image.fill(QtCore.Qt.white)
            self.reDraw()
            print('Clear all')
        elif self.lastKeys[0] == 16777249 and self.lastKeys[1] == 90: # отмена отсечения
            self.image.fill(QtCore.Qt.white)
            self.setColorCutter()
            self.reDrawCutter()
            self.setColorLine()
            self.reDrawFigure()
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
        self.lineInputBut.clicked.connect(lambda: self.figInput())
        self.cutBut.clicked.connect(lambda: self.cut())

    def cutterInput(self):
        # print("Input of cutter:")
        self.lastInput = 'cutter'
        if self.figureMode == 'inputFigure':
            self.figureMode = 'doneFigure'
            self.lineDraw(self.figure[0][0], self.figure[0][1], self.figure[len(self.figure) - 1][0], self.figure[len(self.figure) - 1][1])
            self.figure.append([self.figure[0][0], self.figure[0][1]])
            self.figure.append([self.figure[1][0], self.figure[1][1]])

        self.setColorCutter()
        if self.cutterMode == 'null':
            self.cutterMode = 'startCutter'
        elif self.cutterMode == 'inputCutter':
            self.cutterMode = 'doneCutter'
            self.lineDraw(self.cutter[0][0], self.cutter[0][1], self.cutter[len(self.cutter) - 1][0], self.cutter[len(self.cutter) - 1][1])
            self.cutter.append([self.cutter[0][0], self.cutter[0][1]])
            self.cutter.append([self.cutter[1][0], self.cutter[1][1]])
        # self.figureMode = 'null'

    def figInput(self):
        # print("Input of figure:")
        self.lastInput = 'figure'
        if self.cutterMode == 'inputCutter':
            self.cutterMode = 'doneCutter'
            self.lineDraw(self.cutter[0][0], self.cutter[0][1], self.cutter[len(self.cutter) - 1][0], self.cutter[len(self.cutter) - 1][1])
            self.cutter.append([self.cutter[0][0], self.cutter[0][1]])
            self.cutter.append([self.cutter[1][0], self.cutter[1][1]])

        self.setColorLine()
        if self.figureMode == 'null':
            self.figureMode = 'startFigure'
        elif self.figureMode == 'inputFigure':
            self.figureMode = 'doneFigure'
            self.lineDraw(self.figure[0][0], self.figure[0][1], self.figure[len(self.figure) - 1][0], self.figure[len(self.figure) - 1][1])
            self.figure.append([self.figure[0][0], self.figure[0][1]])
            self.figure.append([self.figure[1][0], self.figure[1][1]])
        # self.setColorLine()
        # self.cutterMode = 'null'

    def cut(self):
        if not self.checkConvexity():
            self.showError(0)
            return

        if not self.checkIntersection(self.cutter):
            self.showError(0)
            return

        # if not self.checkIntersection(self.figure):
        #     self.showError(1)
        #     return

        self.res = self.figure
        self.res = self.res[:-1]
        for i in range(len(self.cutter) - 2):
            # print(i, i+1)
            Res = []
            F = self.res[0]
            pointSign = self.checkPointVisibility(F, [self.cutter[i], self.cutter[i + 1]])
            if pointSign >= 0:
                Res.append(F)
            S = F
            for j in range(1, len(self.res)):
                # print(j)
                buf = self.isIntersec([S, self.res[j]], [self.cutter[i], self.cutter[i + 1]])
                if buf[0] != -1:
                    Res.append(buf)

                S = self.res[j]
                pointSign = self.checkPointVisibility(S, [self.cutter[i], self.cutter[i + 1]])
                if pointSign >= 0:
                    Res.append(S)

            if len(Res) == 0:
                self.res.clear()
                self.showError(2)
                return

            buf = self.isIntersec([S, F], [self.cutter[i], self.cutter[i + 1]])
            if buf[0] != -1:
                Res.append(buf)

            self.res = deepcopy(Res)

            # self.clearCache()
        self.res.append(self.res[0])
        self.resDraw()

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
            c11 = [fig[i][0], fig[i][1]]
            c12 = [fig[i + 1][0], fig[i + 1][1]]
            c1 = [c11, c12]
            for j in range(i + 2, len(fig) - 2):
                print(i, j)
                c21 = [fig[j][0], fig[j][1]]
                c22 = [fig[j + 1][0], fig[j + 1][1]]
                c2 = [c21, c22]
                    
                if i == 0 and j == len(fig) - 3:
                    pass
                elif self.isIntersec(c1, c2)[0] != -1:
                    res = False # стороны пересекаются
                    print(f"I J {i, j}")
        return res

    def isIntersec(self, c1, c2):
        t1 = self.checkPointVisibility(c1[0], c2)
        t2 = self.checkPointVisibility(c1[1], c2)
        #считается что ребро многоугольника, которое начинается
        #или заканчивается на стороне отсекателя, не пересек с ней
        #эта точка должна быть занесена в резльтат ранее
        if t1 == 0:
            resPoint = c1[0]
        elif t2 == 0:
            resPoint = c1[1]
        elif t1 < 0 and t2 > 0 or t1 > 0 and t2 < 0:
            coef = [[0, 0], [0, 0]]
            coef[0][0] = c1[1][0] - c1[0][0]
            coef[0][1] = c2[0][0] - c2[1][0]
            coef[1][0] = c1[1][1] - c1[0][1]
            coef[1][1] = c2[0][1] - c2[1][1]

            right = [0, 0]
            right[0] = c2[0][0] - c1[0][0]
            right[1] = c2[0][1] - c1[0][1]
            
            coef = linalg.inv(coef)
            param = dot(coef, right)
            resPoint = [c1[0][0] + (c1[1][0] - c1[0][0]) * param[0], c1[0][1] + (c1[1][1] - c1[0][1]) * param[0]]
        else:
            resPoint = [-1, -1]
        # print(resPoint)
        return resPoint

    def checkPointVisibility(self, point, edge):
        p1 = (point[0] - edge[0][0]) * (edge[1][1] - edge[0][1])
        p2 = (point[1] - edge[0][1]) * (edge[1][0] - edge[0][0])
        p3 = p2 - p1
        return sign(p3)

    def clearCache(self):
        self.image.fill(QtCore.Qt.white)
        self.setColorCutter()
        self.reDrawCutter()
        self.setColorLine()
        self.reDrawFigure()

    def reDrawCutter(self):
        for i in range(len(self.cutter) - 2):# помни что в массиве вершин отсекателя лежат еще нулевая вершина и первая для удобства обращения
            self.lineDraw(self.cutter[i][0], self.cutter[i][1], self.cutter[i + 1][0], self.cutter[i + 1][1])
    
    def reDrawFigure(self):
        for i in range(len(self.figure) - 2):
            self.lineDraw(self.figure[i][0], self.figure[i][1], self.figure[i + 1][0], self.figure[i + 1][1])
    
    def resDraw(self):
        self.setColorCutted()
        for i in range(len(self.res) - 1):
            if len(self.res[i]) == 2:
                self.lineDraw(self.res[i][0], self.res[i][1], self.res[i + 1][0], self.res[i + 1][1])
        self.res.clear()

    def lineDraw(self, xs, ys, xe, ye):
        self.painter.drawLine(xs, ys, xe, ye)
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
            self.reDrawFigure()
            self.setColorCutter()
            #redrawAll
    
    def newFigureQ(self):
        newCutter = QtWidgets.QMessageBox()
        newCutter.setWindowTitle("Переопределение")
        newCutter.setText("Вы уже ввели фигуру. Хотите задать новую?")
        newCutter.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        newCutter.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        newCutter.setIcon(QtWidgets.QMessageBox.Question)
        ret = newCutter.exec()
        if ret == QtWidgets.QMessageBox.Yes:
            self.figureMode = 'startFigure'
            self.figure.clear()
            self.setColorCutter()
            self.image.fill(QtCore.Qt.white)
            self.reDrawCutter()
            self.setColorLine()
            #redrawAll

    def showError(self, mode):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Ошибка")
        if mode == 0:
            error.setText("Отсекатель не является выпуклым. Введите новый")
        elif mode == 1:
            error.setText("Отсекаемый многоуголник имеет пересечения. Введите новый")
        elif mode == 2:
            error.setText("Весь отсекаемый многоугольник находится вне отсекателя")
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myApp()
    MainWindow.show()
    sys.exit(app.exec_())