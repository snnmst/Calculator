import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.Nums = []
        self.ops = []
        self.pow = 1
        self.flagDat = False
        self.flagPow = False
        self.flagSign = False
        self.setWindowTitle("Generic Window")
        self.setFixedSize(330,360)

        self.txt_screen = QLineEdit(self)
        self.txt_screen.move(10,24)
        self.txt_screen.resize(305,25)
        self.txt_screen.setReadOnly(True)

        self.btnBackSpace = QPushButton("Back Space", self)
        self.btnBackSpace.move(10, 74)
        self.btnBackSpace.clicked.connect(self.btnBackSpaceClickedHandler)

        self.btnClearAll = QPushButton("Clear All", self)
        self.btnClearAll.move(100, 74)
        self.btnClearAll.clicked.connect(self.btnClearAllClickedHandler)

        self.btnNum7 = QPushButton("7", self)
        self.btnNum7.move(10, 104)
        self.btnNum7.resize(48, 48)
        self.btnNum7.clicked.connect(self.btnNumClickedHandler)

        self.btnNum8 = QPushButton("8", self)
        self.btnNum8.move(70, 104)
        self.btnNum8.resize(48, 48)
        self.btnNum8.clicked.connect(self.btnNumClickedHandler)

        self.btnNum9 = QPushButton("9", self)
        self.btnNum9.move(130, 104)
        self.btnNum9.resize(48, 48)
        self.btnNum9.clicked.connect(self.btnNumClickedHandler)

        self.btnDiv = QPushButton("/", self)
        self.btnDiv.move(210, 104)
        self.btnDiv.resize(48, 48)
        self.btnDiv.clicked.connect(self.process)

        self.btnSqrt = QPushButton("Sqrt", self)
        self.btnSqrt.move(270, 104)
        self.btnSqrt.resize(48, 48)
        self.btnSqrt.clicked.connect(self.btnSqrtClickedHandler)

        self.btnNum4 = QPushButton("4", self)
        self.btnNum4.move(10, 164)
        self.btnNum4.resize(48, 48)
        self.btnNum4.clicked.connect(self.btnNumClickedHandler)

        self.btnNum5 = QPushButton("5", self)
        self.btnNum5.move(70, 164)
        self.btnNum5.resize(48, 48)
        self.btnNum5.clicked.connect(self.btnNumClickedHandler)

        self.btnNum6 = QPushButton("6", self)
        self.btnNum6.move(130, 164)
        self.btnNum6.resize(48, 48)
        self.btnNum6.clicked.connect(self.btnNumClickedHandler)

        self.btnMul = QPushButton("*", self)
        self.btnMul.move(210, 164)
        self.btnMul.resize(48, 48)
        self.btnMul.clicked.connect(self.process)

        self.btnOneOverX = QPushButton("1/x", self)
        self.btnOneOverX.move(270, 164)
        self.btnOneOverX.resize(48, 48)
        self.btnOneOverX.clicked.connect(self.btnOneOverClickedHandler)

        self.btnNum1 = QPushButton("1", self)
        self.btnNum1.move(10, 224)
        self.btnNum1.resize(48, 48)
        self.btnNum1.clicked.connect(self.btnNumClickedHandler)

        self.btnNum2 = QPushButton("2", self)
        self.btnNum2.move(70, 224)
        self.btnNum2.resize(48, 48)
        self.btnNum2.clicked.connect(self.btnNumClickedHandler)

        self.btnNum3 = QPushButton("3", self)
        self.btnNum3.move(130, 224)
        self.btnNum3.resize(48, 48)
        self.btnNum3.clicked.connect(self.btnNumClickedHandler)

        self.btnSub = QPushButton("-", self)
        self.btnSub.move(210, 224)
        self.btnSub.resize(48, 48)
        self.btnSub.clicked.connect(self.process)

        self.btnPow = QPushButton("pow", self)
        self.btnPow.move(270, 224)
        self.btnPow.resize(48, 48)
        self.btnPow.clicked.connect(self.process)

        self.btnNum0 = QPushButton("0", self)
        self.btnNum0.move(10, 284)
        self.btnNum0.resize(48, 48)
        self.btnNum0.clicked.connect(self.btnNumClickedHandler)

        self.btnSign = QPushButton("+/-", self)
        self.btnSign.move(70, 284)
        self.btnSign.resize(48, 48)
        self.btnSign.clicked.connect(self.btnSignClickHandler)

        self.btnDat = QPushButton(".", self)
        self.btnDat.move(130, 284)
        self.btnDat.resize(48, 48)
        self.btnDat.clicked.connect(self.btnDatClickHandler)

        self.btnAdd = QPushButton("+", self)
        self.btnAdd.move(210, 284)
        self.btnAdd.resize(48, 48)
        self.btnAdd.clicked.connect(self.process)

        self.btnEq = QPushButton("=", self)
        self.btnEq.move(270, 284)
        self.btnEq.resize(48, 48)
        self.btnEq.clicked.connect(self.btnEqClickedHandler)

    def btnNumClickedHandler(self):
        if self.flagDat is True:
            self.evalDatNums()
        elif self.flagSign is True:
            self.num = self.num * 10 - int(self.sender().text())
        else:
            self.num = self.num * 10 + int(self.sender().text())
            # self.Nums.append(int(self.num))
        self.txt_screen.setText(str(self.num))


    def btnClearAllClickedHandler(self):
        self.flagDat = False
        self.flagSign = False
        self.pow = 1
        self.txt_screen.clear()
        self.num = 0
        self.Nums.clear()
        self.ops.clear()

    def btnBackSpaceClickedHandler(self):
        if self.num < 0:
            self.num = self.num * -1
            self.num = self.num // 10
            self.num = self.num * -1
            if self.num == 0:
                self.flagSign = False
        else:
            self.num = self.num // 10
        self.txt_screen.setText(str(self.num))

    def btnDatClickHandler(self):
        self.num = float(self.num)
        self.txt_screen.setText(str(self.num))
        self.flagDat = True

    def btnSignClickHandler(self):
        self.num = self.num * -1
        self.txt_screen.setText(str(self.num))
        self.flagSign = True

    def btnOneOverClickedHandler(self):
        self.num = 1.0 / self.num
        self.txt_screen.setText(str(self.num))

    def btnSqrtClickedHandler(self):
        self.num = math.sqrt(self.num)
        self.txt_screen.setText(str(self.num))

    def process(self):
        self.txt_screen.clear()
        self.ops.append(self.sender().text())
        self.Nums.append(self.num)
        self.num = 0
        if len(self.Nums) == 2 and len(self.ops) == 2:
            self.eval()
        self.txt_screen.setText(str(self.Nums[0]))
        self.flagDat = False
        self.flagSign = False
        self.pow = 1

    def btnEqClickedHandler(self):
        self.txt_screen.clear()
        self.Nums.append(self.num)
        if len(self.Nums) == 2 and len(self.ops) == 1:
            a = float(self.Nums.pop())
            b = float(self.Nums.pop())
            op = self.ops.pop()

            if op == '+':
                self.num = b + a
            elif op == '-':
                self.num = b - a
            elif op == '*':
                self.num = b * a
            elif op == '/':
                self.num = b / a
            elif op == 'pow':
                self.num = math.pow(b,a)

        elif len(self.Nums) == 1 and len(self.ops) == 0:
            pass
        self.txt_screen.setText(str(self.num))

    def evalDatNums(self):
        if self.flagSign is True:
            self.num = float(self.num) - int(self.sender().text()) * float(math.pow(10, self.pow * -1))
        else:
            self.num = float(self.num) + int(self.sender().text()) * float(math.pow(10, self.pow * -1))
        self.pow = self.pow + 1

    def eval(self):
        #if len(self.Nums) == 2 and len(self.ops) == 2:
            a = float(self.Nums.pop())
            b = float(self.Nums.pop())
            self.ops.reverse()
            op = self.ops.pop()

            self.cal(a,b,op)
    def cal(self, a,b, op):
        if op == '+':
            self.Nums.append(b + a)
        elif op == '-':
            self.Nums.append(b - a)
        elif op == '*':
            self.Nums.append(b * a)
        elif op == '/':
            self.Nums.append(b / a)
        elif op == 'pow':
            self.Nums.append(math.pow(b, a))

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()


main()
