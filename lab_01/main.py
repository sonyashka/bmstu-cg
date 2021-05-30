from PyQt5 import QtCore, QtGui, QtWidgets
from math import pow, sqrt
from ui import Ui_MainWindow

class myApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.x = []
        self.y = []
        self.r = []
        self.lastAction = ""
        self.lastx = []
        self.lasty = []
        self.lastr = []
        self.count = 0
        self.setupUi(self)
        self.functions()

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()

        self.label.setGeometry(QtCore.QRect(width - 185, 0, 171, 41))
        self.pushButton.setGeometry(QtCore.QRect(width - 175, 140, 151, 28))
        self.label_5.setGeometry(QtCore.QRect(width - 185, 180, 181, 16))
        self.lineEdit.setGeometry(QtCore.QRect(width - 155, 40, 141, 22))
        self.lineEdit_2.setGeometry(QtCore.QRect(width - 155, 60, 141, 22))
        self.label_2.setGeometry(QtCore.QRect(width - 185, 40, 31, 21))
        self.label_3.setGeometry(QtCore.QRect(width - 185, 60, 31, 21))
        self.lineEdit_3.setGeometry(QtCore.QRect(width - 185, 110, 171, 22))
        self.label_6.setGeometry(QtCore.QRect(width - 185, 90, 171, 21))
        self.pushButton_2.setGeometry(QtCore.QRect(width - 175, height - 146, 71, 31))
        self.pushButton_3.setGeometry(QtCore.QRect(width - 175, height - 66, 161, 28))
        self.pushButton_4.setGeometry(QtCore.QRect(width - 85, height - 146, 71, 31))
        self.listWidget_2.setGeometry(QtCore.QRect(width - 185, 200, 181, height - 350))
        self.graphicsView.setGeometry(QtCore.QRect(10, 0, width - 204, height - 30))
        self.pushButton_5.setGeometry(QtCore.QRect(width - 135, height - 106, 101, 31))
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 725, 26))
        self.sceneCreate()

    def functions(self):
        self.sceneCreate()
        self.pushButton.clicked.connect(lambda: self.addCircle())
        self.pushButton_2.clicked.connect(lambda: self.deleteCircle(-1))
        self.pushButton_3.clicked.connect(lambda: self.showDecision())
        self.pushButton_4.clicked.connect(lambda: self.changeCircle())
        self.pushButton_5.clicked.connect(lambda: self.deleteAll())

    def keyPressEvent(self, event):
        if event.key() == 90:
            if self.lastAction == "add":
                self.deleteCircle(self.count - 1)
            elif self.lastAction == "delete all":
                for i in range(len(self.lastx)):
                    self.lineEdit.setText(str(self.lastx[i]))
                    self.lineEdit_2.setText(str(self.lasty[i]))
                    self.lineEdit_3.setText(str(self.lastr[i]))
                    self.addCircle()
                self.lastx.clear()
                self.lasty.clear()
                self.lastr.clear()
            elif self.lastAction == "delete":
                self.lineEdit.setText(str(self.lastx[0]))
                self.lineEdit_2.setText(str(self.lasty[0]))
                self.lineEdit_3.setText(str(self.lastr[0]))
                self.addCircle()
                self.lastx.clear()
                self.lasty.clear()
                self.lastr.clear()
            elif self.lastAction == "change":
                self.lineEdit.setText(str(self.lastx[0]))
                self.lineEdit_2.setText(str(self.lasty[0]))
                self.lineEdit_3.setText(str(self.lastr[0]))
                self.saveChanges(self.lastInd)
                self.lastx.clear()
                self.lasty.clear()
                self.lastr.clear()
            elif self.lastAction == "show":
                self.sceneDraw()
                for i in range(self.count):
                    item = self.listWidget_2.item(i)
                    item.setForeground(self.blackBrush)
                    #self.drawCircle(self.x[i], self.y[i], self.r[i], self.greenPen)
    
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

        self.sceneCoef = 1
        self.scene.addLine(0, self.sceneHeight / 2, self.sceneWidth, self.sceneHeight / 2, self.blackPen)
        self.scene.addLine(self.sceneWidth / 2, 0, self.sceneWidth / 2, self.sceneHeight, self.blackPen)

        for i in range(self.count):
            if self.x[i] + self.r[i] > self.sceneWidth / 2 * self.sceneCoef or self.x[i] - self.r[i] < self.sceneWidth / 2 * -self.sceneCoef or self.y[i] + self.r[i] > self.sceneHeight / 2 * self.sceneCoef or self.y[i] - self.r[i] < self.sceneHeight / 2 * -self.sceneCoef:
                ind1 = (self.x[i] + self.r[i]) / (self.sceneWidth / 2 * self.sceneCoef)
                ind2 = (self.x[i] - self.r[i]) / (self.sceneWidth / 2 * -self.sceneCoef)
                ind3 = (self.y[i] + self.r[i]) / (self.sceneHeight / 2 * self.sceneCoef)
                ind4 = (self.y[i] - self.r[i]) / (self.sceneHeight / 2 * -self.sceneCoef)
                if max(ind1, ind2, ind3, ind4) == ind1:
                    self.sceneCoef *= ind1
                elif max(ind1, ind2, ind3, ind4) == ind2:
                    self.sceneCoef *= ind2
                elif max(ind1, ind2, ind3, ind4) == ind3:
                    self.sceneCoef *= ind3
                elif max(ind1, ind2, ind3, ind4) == ind4:
                    self.sceneCoef *= ind4

        serif = 10
        widthStep = self.sceneWidth / 2 / 6
        heightStep = self.sceneHeight / 2 / 6
        for i in range(1, 6):
            self.scene.addLine(0, self.sceneHeight / 2 + i * heightStep, self.sceneWidth, self.sceneHeight / 2 + i * heightStep, self.blackPenLittle)
            self.scene.addLine(0, self.sceneHeight / 2 - i * heightStep, self.sceneWidth, self.sceneHeight / 2 - i * heightStep, self.blackPenLittle)
            self.scene.addLine(self.sceneWidth / 2 + i * widthStep, 0, self.sceneWidth / 2 + i * widthStep, self.sceneHeight, self.blackPenLittle)
            self.scene.addLine(self.sceneWidth / 2 - i * widthStep, 0, self.sceneWidth / 2 - i * widthStep, self.sceneHeight, self.blackPenLittle)

            self.scene.addLine(self.sceneWidth / 2 - serif, self.sceneHeight / 2 + i * heightStep, self.sceneWidth / 2 + serif, self.sceneHeight / 2 + i * heightStep, self.blackPen)
            serifLabel = self.scene.addText("{0:.1f}".format(-i * heightStep * self.sceneCoef))
            serifLabel.setPos(self.sceneWidth / 2 - serif * 5, self.sceneHeight / 2 + i * heightStep - serif)
            self.scene.addLine(self.sceneWidth / 2 - serif, self.sceneHeight / 2 - i * heightStep, self.sceneWidth / 2 + serif, self.sceneHeight / 2 - i * heightStep, self.blackPen)
            serifLabel = self.scene.addText("{0:.1f}".format(i * heightStep * self.sceneCoef))
            serifLabel.setPos(self.sceneWidth / 2 - serif * 5, self.sceneHeight / 2 - i * heightStep - serif)
            self.scene.addLine(self.sceneWidth / 2 + i * widthStep, self.sceneHeight / 2 + serif, self.sceneWidth / 2 + i * widthStep, self.sceneHeight / 2 - serif, self.blackPen)
            serifLabel = self.scene.addText("{0:.1f}".format(i * widthStep * self.sceneCoef))
            serifLabel.setPos(self.sceneWidth / 2 + i * widthStep - serif * 2, self.sceneHeight / 2 + serif * 0.5)
            self.scene.addLine(self.sceneWidth / 2 - i * widthStep, self.sceneHeight / 2 + serif, self.sceneWidth / 2 - i * widthStep, self.sceneHeight / 2 - serif, self.blackPen)
            serifLabel = self.scene.addText("{0:.1f}".format(-i * widthStep * self.sceneCoef))
            serifLabel.setPos(self.sceneWidth / 2 - i * widthStep - serif * 2, self.sceneHeight / 2 + serif * 0.5)

        zeroLable = self.scene.addText("0")
        zeroLable.setPos(self.sceneWidth / 2 - serif * 1.5, self.sceneHeight / 2 + serif * 0.5)
        self.scene.addLine(self.sceneWidth / 2 - serif, serif, self.sceneWidth / 2, 0, self.blackPen)
        self.scene.addLine(self.sceneWidth / 2 + serif, serif, self.sceneWidth / 2, 0, self.blackPen)
        axesLable = self.scene.addText("Y")
        axesLable.setPos(self.sceneWidth / 2 - serif * 3, 0)
        self.scene.addLine(self.sceneWidth - serif, self.sceneHeight / 2 - serif, self.sceneWidth, self.sceneHeight / 2, self.blackPen)
        self.scene.addLine(self.sceneWidth - serif, self.sceneHeight / 2 + serif, self.sceneWidth, self.sceneHeight / 2, self.blackPen)
        axesLable = self.scene.addText("X")
        axesLable.setPos(self.sceneWidth - serif * 1.5, self.sceneHeight / 2 + serif * 0.5)

        for i in range(self.count):
            self.drawCircle(self.x[i] / self.sceneCoef, self.y[i] / self.sceneCoef, self.r[i] / self.sceneCoef, self.greenPen)
    
    def task(self):
        taskMes = QtWidgets.QMessageBox()
        taskMes.setWindowTitle("Условие задачи")
        taskMes.setText("На плоскости задано множество окружностей. Две окружности A и B назовем связанными, если они пересекаются либо существует третья окружность C заданного множества, свяазанная с A и B.\nВыбрать максимальное подмножество попарно не связанных друг с другом окруженостей.")
        taskMes.setIcon(QtWidgets.QMessageBox.Information)
        taskMes.exec_()

    def info(self):
        infoMes = QtWidgets.QMessageBox()
        infoMes.setWindowTitle("Об авторе")
        infoMes.setText("Лабораторная работа №1 'Геометрические преобразования' была написана Параскун Софией, ИУ7-44Б")
        infoMes.setIcon(QtWidgets.QMessageBox.Information)
        infoMes.exec_()

    def addCircle(self):
        try:
            self.x.append(float(self.lineEdit.text()))
            self.y.append(float(self.lineEdit_2.text()))
            self.r.append(float(self.lineEdit_3.text()))
            self.count += 1
            if self.r[self.count - 1] > 0:
                if self.x[self.count - 1] + self.r[self.count - 1] > self.sceneWidth / 2 * self.sceneCoef or self.x[self.count - 1] - self.r[self.count - 1] < self.sceneWidth / 2 * -self.sceneCoef or self.y[self.count - 1] + self.r[self.count - 1] > self.sceneHeight / 2 * self.sceneCoef or self.y[self.count - 1] - self.r[self.count - 1] < self.sceneHeight / 2 * -self.sceneCoef:
                    ind1 = (self.x[self.count - 1] + self.r[self.count - 1]) / (self.sceneWidth / 2 * self.sceneCoef)
                    ind2 = (self.x[self.count - 1] - self.r[self.count - 1]) / (self.sceneWidth / 2 * -self.sceneCoef)
                    ind3 = (self.y[self.count - 1] + self.r[self.count - 1]) / (self.sceneHeight / 2 * self.sceneCoef)
                    ind4 = (self.y[self.count - 1] - self.r[self.count - 1]) / (self.sceneHeight / 2 * -self.sceneCoef)
                    if max(ind1, ind2, ind3, ind4) == ind1:
                        self.sceneCoef *= ind1
                    elif max(ind1, ind2, ind3, ind4) == ind2:
                        self.sceneCoef *= ind2
                    elif max(ind1, ind2, ind3, ind4) == ind3:
                        self.sceneCoef *= ind3
                    elif max(ind1, ind2, ind3, ind4) == ind4:
                        self.sceneCoef *= ind4
                    self.sceneDraw()
                else:
                    self.drawCircle(self.x[self.count - 1] / self.sceneCoef, self.y[self.count - 1] / self.sceneCoef, self.r[self.count - 1] / self.sceneCoef, self.greenPen)
                self.listWidget_2.addItem(str(self.count) + ". (" + str(self.x[self.count - 1]) + "; " + str(self.y[self.count - 1]) + "), R = " + str(self.r[self.count - 1]) + "\n")
                self.lastAction = "add"
            else:
                self.showError()
                self.x.pop(i)
                self.y.pop(i)
                self.r.pop(i)
                self.count -= 1
        except ValueError:
            self.showError()
        
    def draw(self, event):
        self.lineEdit.setText(str(event.x))
        self.lineEdit_2.setText(str(event.y))
        self.scene.addEllipse(event.x - 2, event.y - 2, 5, 5, self.greenPen, self.greenBrush)
    
    def drawCircle(self, x, y, r, color):
        self.scene.addEllipse(self.sceneWidth / 2 + x - 1, self.sceneHeight / 2 - y - 1, 3, 3, color)
        self.scene.addEllipse(self.sceneWidth / 2 + x - r, self.sceneHeight / 2 - y - r, r * 2, r * 2, color)

    def deleteCircle(self, ind):
        if ind < 0:
            i = self.listWidget_2.currentRow()
            self.listWidget_2.takeItem(self.listWidget_2.currentRow())
        else:
            i = ind
            self.listWidget_2.takeItem(i)
        self.lastAction = "delete"
        self.lastx.append(self.x.pop(i))
        self.lasty.append(self.y.pop(i))
        self.lastr.append(self.r.pop(i))
        for j in range (i, self.count - 1):
            curItem = self.listWidget_2.item(j)
            curItem.setText(str(j + 1) + ". (" + str(self.x[j]) + "; " + str(self.y[j]) + "), R = " + str(self.r[j]) + "\n")
        self.count -= 1
        self.sceneDraw()

    def showDecision(self):
        self.matrixConnections = [[0 for x in range(self.count)] for y in range(self.count)]
        print("start")
        for i in range(0, self.count):
            for j in range(0, self.count):
                print(self.matrixConnections[i][j], end = ' ')
            print("")

        for i in range(0, self.count):
            for j in range(i + 1, self.count):
                if i == j or self.distance(i, j) <= self.r[i] + self.r[j] and self.distance(i, j) > abs(self.r[i] - self.r[j]): #and self.distance(i, j) > self.r[i] and self.distance(i, j) > self.r[j]:
                    self.matrixConnections[i][j] = 1
                    self.matrixConnections[j][i] = 1

        print("before checking")
        for i in range(0, self.count):
            for j in range(0, self.count):
                print(self.matrixConnections[i][j], end = ' ')
            print("")
        
        for i in range(0, self.count):
            for j in range(i, self.count):
                if i != j and self.matrixConnections[i][j] == 0:
                    self.checkConnect(i, j)
                elif i == j:
                    self.matrixConnections[i][j] = 1
        for i in range(0, self.count):
            for j in range(i, self.count):
                if i != j and self.matrixConnections[i][j] == 0:
                    self.checkConnect(i, j)
                elif i == j:
                    self.matrixConnections[i][j] = 1

        print("after checking")
        for i in range(0, self.count):
            for j in range(0, self.count):
                print(self.matrixConnections[i][j], end = ' ')
            print("")

        maxCircles = 0
        indMax = 0
        for i in range(0, self.count):
            stringCount = 0
            for j in range(i, self.count):
                if self.matrixConnections[i][j] == 0:
                    stringCount += 1
            if stringCount > maxCircles:
                maxCircles = stringCount
                indMax = i
        
        if maxCircles == 0 and self.count > 0:
            maxCircles = 1
            indMax = 0
            self.drawRes(indMax)
        elif maxCircles > 0:
            self.drawRes(indMax)
        else:
            self.showBadResult()
        self.lastAction = "show"
        print(maxCircles, indMax)

    def checkConnect(self, i, j):
        for k in range(0, self.count):
            if i != k and j != k and (self.matrixConnections[i][k] != 0 or self.matrixConnections[j][k] != 0):
                self.matrixConnections[i][k] = 1
                self.matrixConnections[k][i] = 1
                self.matrixConnections[j][k] = 1
                self.matrixConnections[k][j] = 1
            #if self.matrixConnections[i][k] != 0 or self.matrixConnections[j][k] != 0:
             #   self.matrixConnections[i][j] = 1

    def drawRes(self, ind):
        for i in range(self.count):
            if self.matrixConnections[ind][i] == 0 or i == ind:
                self.drawCircle(self.x[i] / self.sceneCoef, self.y[i] / self.sceneCoef, self.r[i] / self.sceneCoef, self.redPen)
                item = self.listWidget_2.item(i)
                item.setForeground(self.redBrush)

    def showBadResult(self):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Результат")
        error.setText("Недостаточно элементов. Добавьте окружность и повторите снова.")
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.exec_()
    
    def distance(self, i, j):
        return sqrt(pow((self.x[i] - self.x[j]), 2) + pow((self.y[i] - self.y[j]), 2)) 

    def changeCircle(self):
        i = self.listWidget_2.currentRow()
        if i >= 0:
            self.lastAction = "change"
            self.lastx.append(self.x[i])
            self.lasty.append(self.y[i])
            self.lastr.append(self.r[i])
            self.lastInd = i
            self.lineEdit.setText(str(self.x[i]))
            self.lineEdit_2.setText(str(self.y[i]))
            self.lineEdit_3.setText(str(self.r[i]))
            self.pushButton_4.pressed.connect(lambda: self.saveChanges(i))
    
    def saveChanges(self, ind):
        try:
            self.x[ind] = float(self.lineEdit.text())
            self.y[ind] = float(self.lineEdit_2.text())
            self.r[ind] = float(self.lineEdit_3.text())

            if self.r[ind] > 0:
                if self.x[ind] + self.r[ind] > self.sceneWidth / 2 * self.sceneCoef or self.x[ind] - self.r[ind] < self.sceneWidth / 2 * -self.sceneCoef or self.y[ind] + self.r[ind] > self.sceneHeight / 2 * self.sceneCoef or self.y[ind] - self.r[ind] < self.sceneHeight / 2 * -self.sceneCoef:
                    ind1 = (self.x[ind] + self.r[ind]) / (self.sceneWidth / 2 * self.sceneCoef)
                    ind2 = (self.x[ind] - self.r[ind]) / (self.sceneWidth / 2 * -self.sceneCoef)
                    ind3 = (self.y[ind] + self.r[ind]) / (self.sceneHeight / 2 * self.sceneCoef)
                    ind4 = (self.y[ind] - self.r[ind]) / (self.sceneHeight / 2 * -self.sceneCoef)
                    if max(ind1, ind2, ind3, ind4) == ind1:
                        self.sceneCoef *= ind1
                    elif max(ind1, ind2, ind3, ind4) == ind2:
                        self.sceneCoef *= ind2
                    elif max(ind1, indк2, ind3, ind4) == ind3:
                        self.sceneCoef *= ind3
                    elif max(ind1, ind2, ind3, ind4) == ind4:
                        self.sceneCoef *= ind4
                curItem = self.listWidget_2.currentItem()
                curItem.setText(str(ind + 1) + ". (" + self.lineEdit.text() + "; " + self.lineEdit_2.text() + "), R = " + self.lineEdit_3.text() + "\n")
                self.sceneDraw()
                self.lastAction = ""
            else:
                self.showError()
        except ValueError:
            self.showError()

    def deleteAll(self):
        self.listWidget_2.clear()
        for i in range(self.count):
            self.lastx.append(self.x[i])
            self.lasty.append(self.y[i])
            self.lastr.append(self.r[i])
        self.lastAction = "delete all"
        self.x.clear()
        self.y.clear()
        self.r.clear()
        self.count = 0
        self.sceneDraw()

    def showError(self):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText("Введенные параметры не являются вещественным числом или радиус не положительный.")
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myApp()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
