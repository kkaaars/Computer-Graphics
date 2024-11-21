from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLineEdit,QLabel, QWidget, QTextEdit)
from PyQt5.QtGui import QFont
import sys
import time
import pygame as pg
import ctypes
from ctypes import wintypes

from PyQt5.uic.Compiler.qtproxies import QtCore

WEIGHT = 700
HEIGHT = 700
MID = (WEIGHT / 2, HEIGHT / 2)
DARKGREY = (150, 150, 150)
WHITE = (200, 200, 200)
GRAY = (70, 70, 70)
BLUE = (255, 0, 0)
BLACK = (0, 0, 0)
OXY = (10, 10, 10)
step = 10
x = WEIGHT / 2
y = HEIGHT / 2
s = 1


def Exit():
    sys.exit()



def init_pg():
    pg.init()
    window = pg.display.set_mode((WEIGHT, HEIGHT))
    hwnd = pg.display.get_wm_info()['window']
    ctypes.windll.user32.SetWindowPos(hwnd, 0, -9, -40, 0, 0, 0)
    pg.display.set_caption("Drawing Algorithms")
    window.fill(DARKGREY)

    draw_cords(window)
    pg.display.flip()



class TextEditLogger(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setAcceptRichText(True)

    def write(self, message):
        self.append(message)

    def flush(self):
        pass


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setWindowTitle("Menu")
        self.setFixedSize(700, 250)
        self.move(0,698)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.button_panel = QHBoxLayout()
        self.radius_panel = QHBoxLayout()

        self.pbc = QPushButton("Circle", self)
        self.pbc.clicked.connect(self.CirclePB)
        self.button_panel.addWidget(self.pbc)

        self.pbl = QPushButton("Line", self)
        self.pbl.clicked.connect(self.StepLine)
        self.button_panel.addWidget(self.pbl)

        self.pbb = QPushButton("Line BR", self)
        self.pbb.clicked.connect(self.BresenhamLine)
        self.button_panel.addWidget(self.pbb)

        self.pbc2 = QPushButton("Line СDA", self)
        self.pbc2.clicked.connect(self.CDALine)
        self.button_panel.addWidget(self.pbc2)

        self.pbs = QPushButton("Smoothing", self)
        self.pbs.clicked.connect(self.SmoothingLine)
        self.button_panel.addWidget(self.pbs)

        self.exit_button = QPushButton("=Exit=", self)
        self.exit_button.clicked.connect(Exit)

        self.layout.addLayout(self.button_panel)

        self.coord_label = QLabel("Input Coordinates (x1, y1, x2, y2):", self)
        self.layout.addWidget(self.coord_label)

        self.leX1 = QLineEdit(self)
        self.leY1 = QLineEdit(self)
        self.leX2 = QLineEdit(self)
        self.leY2 = QLineEdit(self)

        self.coord_input_layout = QHBoxLayout()
        self.coord_input_layout.addWidget(QLabel("X1:"))
        self.coord_input_layout.addWidget(self.leX1)
        self.coord_input_layout.addWidget(QLabel("Y1:"))
        self.coord_input_layout.addWidget(self.leY1)
        self.coord_input_layout.addWidget(QLabel("X2:"))
        self.coord_input_layout.addWidget(self.leX2)
        self.coord_input_layout.addWidget(QLabel("Y2:"))
        self.coord_input_layout.addWidget(self.leY2)

        self.layout.addLayout(self.coord_input_layout)

        self.radius_label = QLabel("Input Radius:", self)
        self.radius_input = QLineEdit(self)
        self.radius_panel.addWidget(self.radius_label)
        self.radius_panel.addWidget(self.radius_input)
        self.radius_panel.addWidget(self.exit_button)
        self.layout.addLayout(self.radius_panel)
        self.logger = TextEditLogger(self)
        self.logger.setStyleSheet("background-color: white;")
        self.logger.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.logger)

        self.writer()

    def writer(self):
        sys.stdout = self.logger
        self.logger.clear()

    def extremum(self, x1,y1,x2,y2):
        if x1 > 33:
            x1 = 33
            self.leX1.setText("33")
        if x1 < -33:
            x1 = -33
            self.leX1.setText("-33")
        if self.leX1.text() == '':
            x1 = 0
            self.leX1.setText("0")

        if y1 > 33:
            y1 = 33
            self.leY1.setText("33")
        if y1 < -33:
            y1 = -33
            self.leY1.setText("-33")
        if self.leY1.text() == '':
            y1 = 0
            self.leY1.setText("0")

        if x2 > 33:
            x2 = 33
            self.leX2.setText("33")
        if x2 < -33:
            x2 = -33
            self.leX2.setText("-33")
        if self.leX2.text() == '':
            x2 = 0
            self.leX2.setText("0")

        if y2 > 33:
            y2 = 33
            self.leY2.setText("33")
        if y2 < -33:
            y2 = -33
            self.leY2.setText("-33")
        if self.leY2.text() == '':
            y2 = 0
            self.leY2.setText("0")

    def CirclePB(self):
        R_text = self.radius_input.text()
        R = int(R_text) if R_text else 0

        if R > 33:
            R = 33
            self.radius_input.setText("33")
        if R < 0 or R_text == '':
            R = 0
            self.radius_input.setText("0")


        DrawCircle(R * 10)

    def StepLine(self):
        X1 = int(self.leX1.text()) if self.leX1.text() else 0
        Y1 = int(self.leY1.text()) if self.leY1.text() else 0
        X2 = int(self.leX2.text()) if self.leX2.text() else 0
        Y2 = int(self.leY2.text()) if self.leY2.text() else 0

        self.extremum(X1,Y1,X2,Y2)

        DrawLineStep(int(X1) * 10 + x, y - int(Y1) * 10, int(X2) * 10 + x, y - int(Y2) * 10)

    def BresenhamLine(self):
        X1 = int(self.leX1.text()) if self.leX1.text() else 0
        Y1 = int(self.leY1.text()) if self.leY1.text() else 0
        X2 = int(self.leX2.text()) if self.leX2.text() else 0
        Y2 = int(self.leY2.text()) if self.leY2.text() else 0
        self.extremum(X1, Y1, X2, Y2)
        DrawLineBresenham(int(X1) * 10 + x, y - int(Y1) * 10, int(X2) * 10 + x, y - int(Y2) * 10)


    def CDALine(self):
        X1 = int(self.leX1.text()) if self.leX1.text() else 0
        Y1 = int(self.leY1.text()) if self.leY1.text() else 0
        X2 = int(self.leX2.text()) if self.leX2.text() else 0
        Y2 = int(self.leY2.text()) if self.leY2.text() else 0
        self.extremum(X1, Y1, X2, Y2)
        DrawCDA(int(X1) * 10 + x, y - int(Y1) * 10, int(X2) * 10 + x, y - int(Y2) * 10)

    def SmoothingLine(self):
        X1 = int(self.leX1.text()) if self.leX1.text() else 0
        Y1 = int(self.leY1.text()) if self.leY1.text() else 0
        X2 = int(self.leX2.text()) if self.leX2.text() else 0
        Y2 = int(self.leY2.text()) if self.leY2.text() else 0
        self.extremum(X1, Y1, X2, Y2)
        smoothing(int(X1) * 10 + x, y - int(Y1) * 10, int(X2) * 10 + x, y - int(Y2) * 10)


def draw_cords(window):
    for i in range(0, WEIGHT // (10*s)):
        pg.draw.line(window, OXY, ((10*s) * i + 5, 0), ((10*s) * i + 5, HEIGHT))
    for i in range(0, HEIGHT // (10*s)):
        pg.draw.line(window, OXY, (0, (10*s) * i + 5), (WEIGHT, (10*s) * i + 5))
    pg.draw.line(window, BLACK, (0, y), (WEIGHT - 10, y), 2)
    pg.draw.line(window, BLACK, (x, 10), (x, HEIGHT), 2)
    pg.draw.polygon(window, BLACK, ((x - 7, 14), (x + 7, 14), (x, 7)))
    pg.draw.polygon(window, BLACK, ((WEIGHT - 14, y - 7), (WEIGHT - 14, y + 7), (WEIGHT - 7, y)))
    for i in range(0, WEIGHT, (10*s)):
        pg.draw.line(window, BLACK, (i, y - 3), (i, y + 3))
    for i in range(0, HEIGHT, (10*s)):
        pg.draw.line(window, BLACK, (x - 3, i), (x + 3, i))

    font = pg.font.Font('freesansbold.ttf', 13)
    Xtxt = font.render('X', True, BLACK, DARKGREY)
    Ytxt = font.render('Y', True, BLACK, DARKGREY)
    textRectX = Xtxt.get_rect()
    textRectY = Ytxt.get_rect()
    textRectX.center = (WEIGHT - 10, y - 15)
    textRectY.center = (x + 15, 15)
    window.blit(Xtxt, textRectX)
    window.blit(Ytxt, textRectY)


def mul(A, B):
    ans = [0, 0]
    for i in range(0, 2):
        for j in range(0, 2):
            ans[i] += A[i][j] * B[j]
    return ans


def draw(pos, w):
    pg.draw.rect(w, WHITE, pg.Rect(pos[0] - 5, pos[1] - 5, 10, 10))


def circle(R):
    cords = []
    xStep = 0
    yStep = R
    cords.append([xStep, -yStep])
    while abs(xStep) < abs(yStep):
        mW = abs((xStep + step) ** 2 + yStep ** 2 - R ** 2)
        mH = abs(xStep ** 2 + (yStep - step) ** 2 - R ** 2)
        mD = abs((xStep + step) ** 2 + (yStep - step) ** 2 - R ** 2)
        if min(mH, mW, mD) == mH:
            yStep -= step
        elif min(mH, mW, mD) == mW:
            xStep += step
        elif min(mH, mW, mD) == mD:
            xStep += step
            yStep -= step
        cords.append([xStep, yStep])
    matr1 = ((0, 1),
             (1, 0))
    matr2 = ((-1, 0),
             (0, 1))
    matr3 = ((1, 0),
             (0, -1))

    cords2 = []
    for i in cords:
        cords2.append(mul(matr1, i))
    for i in cords2:
        cords.append(i)
    cords2.clear()
    for i in cords:
        cords2.append(mul(matr2, i))
    for i in cords2:
        cords.append(i)
    cords2.clear()
    for i in cords:
        cords2.append(mul(matr3, i))
    for i in cords2:
        cords.append(i)
    cords2.clear()
    return cords


def StepLineGetCords(x1, y1, x2, y2):
    if x1 == x2:
        cords = [[x1, y1]]
        for i in range(min(y1, y2), max(y1, y2) + 10, 10):
            cords.append([x1, i])
        return cords
    k = (y2 - y1) / (x2 - x1)
    b = (y1 * (x2 - x1) - x1 * (y2 - y1)) / (x2 - x1)

    x1 = (x1 // 10) * 10
    x2 = (x2 // 10) * 10
    y1 = (y1 // 10) * 10
    y2 = (y2 // 10) * 10
    ans = [[x1, y1]]

    if abs(x2 - x1) > abs(y2 - y1):
        for i in range(x1, x2 + 10, 10):
            newY = i * k + b
            newY = (newY // 10) * 10
            ans.append([i, newY])
    else:
        for i in range(y2, y1 + 10, 10):
            newX = (i - b) / k
            newX = (newX // 10) * 10
            ans.append([newX, i])
    return ans


def BresenhamLineGetCords(x1, y1, x2, y2):
    if x1 != x2:
        alph = -(1 / 2)
        k = (y2 - y1) / (x2 - x1)
    else:
        cords = [[x1, y1]]
        for i in range(min(y1, y2), max(y1, y2) + 10, 10):
            cords.append([x1, i])
            return cords

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    x1 = (x1 // 10) * 10
    x2 = (x2 // 10) * 10
    y1 = (y1 // 10) * 10
    ans = [[x1, y1]]

    if abs(x2 - x1) <=\
            abs(y2 - y1):
        c = 10
    else:
        c = 0

    for i in range(x1 + 10, x2 + 10, 10):
        if alph > 0:
            y1 += 10
            alph -= 1
        if alph < -1:
            y1 -= 10
            alph += 1
        ans.append([i, y1 - c])
        alph += k
    return ans


def DrawLineBresenham(x1, y1, x2, y2):

    pg.display.set_caption("Line Bresenham")
    window = pg.display.set_mode((WEIGHT, HEIGHT))
    window.fill(DARKGREY)
    draw_cords(window)
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    start = time.perf_counter()
    if abs(x2 - x1) > abs(y2 - y1):
        cords1 = BresenhamLineGetCords(x1, y1, x2, y2)
    else:
        matr = [[0, 1],
                [1, 0]]
        cords1 = BresenhamLineGetCords(y1, x1, y2, x2)
        for i in range(0, len(cords1)):
            cords1[i] = mul(matr, cords1[i])

    for i in cords1:
        draw((i[0], i[1]), window)
    pg.draw.line(window, BLUE, (x1, y1), (x2, y2), 3)
    finish = time.perf_counter()
    print(f"LineBresenham: {finish - start:.4e}")
    pg.display.flip()


def DrawLineStep(x1, y1, x2, y2):

    pg.display.set_caption("Line Step")
    window = pg.display.set_mode((WEIGHT, HEIGHT))
    window.fill(DARKGREY)
    draw_cords(window)
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    start = time.perf_counter()
    if x2 < x1:
        x2, x1 = x1, x2
        y2, y1 = y1, y2
    cords1 = StepLineGetCords(x1, y1, x2, y2)
    for j in cords1:
        draw((j[0], j[1]), window)
    pg.draw.line(window, BLUE, (x1, y1), (x2, y2), 3)
    finish = time.perf_counter()
    print(f"Line step: {finish - start:.4e}")
    pg.display.flip()


def DrawCDA(x1, y1, x2, y2):

    pg.display.set_caption("Line CDA")
    window = pg.display.set_mode((WEIGHT, HEIGHT))
    window.fill(DARKGREY)
    draw_cords(window)
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    start = time.perf_counter()
    cords1 = CDA(x1, y1, x2, y2)
    for j in cords1:
        draw((j[0], j[1]), window)
    pg.draw.line(window, BLUE, (x1, y1), (x2, y2), 3)
    finish = time.perf_counter()
    print(f"CDA Line: {finish - start:.4e}")
    pg.display.flip()



def DrawCircle(R):

    pg.display.set_caption("Circle")
    window = pg.display.set_mode((WEIGHT, HEIGHT))
    window.fill(DARKGREY)
    draw_cords(window)
    start = time.perf_counter()
    cords1 = circle(R)
    for j in cords1:
        draw((x + j[0], y - j[1]), window)
    pg.draw.circle(window, BLUE, MID, R, 3)
    finish = time.perf_counter()
    print(f"Circle: {finish - start:.4e}")
    pg.display.flip()


def CDA(x1, y1, x2, y2):
    Dx = (x2 - x1)
    Dy = (y2 - y1)

    if abs(Dy) > abs(Dx):
        L = Dy
        step = -10 if Dy < 0 else 10

    else:
        L = Dx
        step = -10 if Dx < 0 else 10

    ans = [[x1 // 10 * 10, y1 // 10 * 10]]
    for i in range(0, abs(L), abs(step)):
        x1 += (Dx / L) * step
        y1 += (Dy / L) * step
        # Format to ensure integer coordinates
        ans.append([int(x1 // 10 * 10), int(y1 // 10 * 10)])
    return ans


def smoothing(x1, y1, x2, y2):
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if abs(x2 - x1) > abs(y2 - y1):
        cords1 = BresenhamLineGetCords(x1, y1, x2, y2)
    else:
        matr = [[0, 1],
                [1, 0]]
        cords1 = BresenhamLineGetCords(y1, x1, y2, x2)
        for i in range(0, len(cords1)):
            cords1[i] = mul(matr, cords1[i])


    pg.display.set_caption("Smoothing")
    window = pg.display.set_mode((WEIGHT, HEIGHT))
    window.fill(DARKGREY)
    draw_cords(window)

    start = time.perf_counter()


    if x1 != x2:
        k = (y2 - y1) / (x2 - x1)
        b = (y1 * (x2 - x1) - x1 * (y2 - y1)) / (x2 - x1)

    for i in range(0, len(cords1)):
        if x1 != x2:
            if abs(x2 - x1) > abs(y2 - y1):
                dif = cords1[i][1] - (cords1[i][0] * k + b)
            else:
                dif = cords1[i][0] - ((cords1[i][1] - b) / k)
        else:
            dif = 0
        if dif != 0 and x1 != x2:
            color = (
                70 + min(abs(150 * (1 / dif)), 150), 70 + min(abs(150 * (1 / dif)), 150),
                70 + min(abs(150 * (1 / dif)), 150))
        else:
            color = (220, 220, 220)
        pg.draw.rect(window, color,
                     pg.Rect(cords1[i][0] - 5, cords1[i][1] - 5, 10, 10))
    pg.draw.line(window, BLUE, (x1, y1), (x2, y2), 3)
    finish = time.perf_counter()
    print(f"Smoothing:  {finish - start:.4e}")
    pg.display.flip()

def show_app(window):
    window.show()
    init_pg()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    show_app(mw)
    sys.exit(app.exec_())