#!/usr/bin/python

import matplotlib.pylab as plt
import math
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


def draw_bike(chainstay_len, seat_tube_len, seat_tube_angle, reach, stack, wheelbase, y_rh=70, color='g', name='new bike'):
    #head_tube_angle = math.radians(head_tube_angle)
    seat_tube_angle = math.radians(seat_tube_angle)

    plt.plot([0, chainstay_len], [y_rh, 0], color=color)
    #plt.plot([chainstay_len, chainstay_len-1.2*seat_tube_len*math.cos(seat_tube_angle)],
    #         [0, 1.2*seat_tube_len*math.sin(seat_tube_angle)], 'k--', alpha=0.5)
    plt.plot([0, chainstay_len-seat_tube_len*math.cos(seat_tube_angle)],
             [y_rh, seat_tube_len*math.sin(seat_tube_angle)], color=color)
    plt.plot([chainstay_len-seat_tube_len*math.cos(seat_tube_angle), chainstay_len+reach],
             [seat_tube_len*math.sin(seat_tube_angle), stack], color=color)
    plt.plot([chainstay_len, chainstay_len-seat_tube_len*math.cos(seat_tube_angle)],
             [0, seat_tube_len*math.sin(seat_tube_angle)], color=color)
    plt.plot([chainstay_len, chainstay_len+reach],
             [0, stack], color=color)
    plt.plot([chainstay_len+reach, wheelbase],
             [stack, y_rh], color=color, label=name)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 500))
        self.setWindowTitle("Bike Drawer v0.1 - A stupid program by Teobaldobau")

        self.seat_tube_len = 520
        self.top_tube_len = 556
        self.head_tube_len = 155
        self.head_tube_angle = 73.25
        self.seat_tube_angle = 73.5
        self.chainstay_len = 410
        self.wheelbase = 988
        self.stack = 567
        self.reach = 391
        self.saddle_height = 800
        self.y_rh = 70
        self.color = 'r'
        self.name = 'Canyon ULTIMATE (default)'

        pybutton2 = QPushButton('Ultimate', self)
        pybutton2.clicked.connect(self.UltimateGeo)
        pybutton2.resize(100,32)
        pybutton2.move(50, 150)

        pybutton = QPushButton('Draw bike', self)
        pybutton.clicked.connect(self.draw)
        pybutton.resize(100,32)
        pybutton.move(50, 50)



        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Reach:')
        self.reach_new = QLineEdit(self)
        self.reach_new.setPlaceholderText(str(self.reach))
        self.reach_new.move(280, 20)
        self.reach_new.resize(200, 32)
        self.nameLabel.move(220, 20)

        self.stackLabel = QLabel(self)
        self.stackLabel.setText('Stack:')
        self.stack_new = QLineEdit(self)
        self.stack_new.setPlaceholderText(str(self.stack))
        self.stack_new.move(280, 60)
        self.stack_new.resize(200, 32)
        self.stackLabel.move(220, 60)


        pybutton3 = QPushButton('Update GEO', self)
        pybutton3.clicked.connect(self.Update)
        pybutton3.resize(200,32)
        pybutton3.move(280, 460)

    def Update(self):
        if self.reach_new.isModified()==False:
            reach_n = self.reach
        else:
            reach_n = float(self.reach_new.text())
        if self.stack_new.isModified()==False:
            stack_n = self.stack
        else:
            stack_n = float(self.stack_new.text())

        print('====> NEW GEO:' \
        + '\n reach = ' + str(reach_n) \
        + '\n stack = ' + str(stack_n))
        self.reach = reach_n
        self.stack = stack_n


    def UltimateGeo(self):
        self.seat_tube_len = 520
        self.top_tube_len = 556
        self.head_tube_len = 155
        self.head_tube_angle = 73.25
        self.seat_tube_angle = 73.5
        self.chainstay_len = 410
        self.wheelbase = 988
        self.stack = 567
        self.reach = 391
        self.saddle_height = 800
        self.y_rh = 70
        self.color = 'g'
        self.name = 'Canyon ULTIMATE'


    def draw(self):
        print('Clicked Pyqt button.')
        plt.draw()
        plt.show()
        plt.subplot(111, aspect=True)

        draw_bike(self.chainstay_len, self.seat_tube_len, self.seat_tube_angle, self.reach,\
                                 self.stack, self.wheelbase, self.y_rh, self.color, self.name)
        plt.legend(loc='best')


'''
plt.subplot(111, aspect=True)

seat_tube_len = 520
top_tube_len = 556
head_tube_len = 155
head_tube_angle = 73.25
seat_tube_angle = 73.5
chainstay_len = 410
wheelbase = 988
stack = 567
reach = 391
saddle_height = 800
y_rh = 70

def draw_bike(chainstay_len, seat_tube_len, seat_tube_angle, reach, stack, wheelbase, y_rh=70, color='g', name='new bike'):
    #head_tube_angle = math.radians(head_tube_angle)
    seat_tube_angle = math.radians(seat_tube_angle)

    plt.plot([0, chainstay_len], [y_rh, 0], color=color)
    #plt.plot([chainstay_len, chainstay_len-1.2*seat_tube_len*math.cos(seat_tube_angle)],
    #         [0, 1.2*seat_tube_len*math.sin(seat_tube_angle)], 'k--', alpha=0.5)
    plt.plot([0, chainstay_len-seat_tube_len*math.cos(seat_tube_angle)],
             [y_rh, seat_tube_len*math.sin(seat_tube_angle)], color=color)
    plt.plot([chainstay_len-seat_tube_len*math.cos(seat_tube_angle), chainstay_len+reach],
             [seat_tube_len*math.sin(seat_tube_angle), stack], color=color)
    plt.plot([chainstay_len, chainstay_len-seat_tube_len*math.cos(seat_tube_angle)],
             [0, seat_tube_len*math.sin(seat_tube_angle)], color=color)
    plt.plot([chainstay_len, chainstay_len+reach],
             [0, stack], color=color)
    plt.plot([chainstay_len+reach, wheelbase],
             [stack, y_rh], color=color, label=name)

draw_bike(chainstay_len, seat_tube_len, seat_tube_angle, reach, stack, wheelbase, y_rh=y_rh, color='g', name='Canyon ULTIMATE')

seat_tube_len = 545
top_tube_len = 547
head_tube_len = 159
head_tube_angle = 73.3
seat_tube_angle = 73.5
chainstay_len = 415
wheelbase = 989
stack = 590
reach = 380
saddle_height = 800
y_rh = 70

draw_bike(chainstay_len, seat_tube_len, seat_tube_angle, reach, stack, wheelbase, y_rh=y_rh, color='b', name='Canyon ENDURACE')

plt.legend(loc='best')
plt.show()

'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
