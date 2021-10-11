"""
Name: Luke Wood

greeting.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
import time

from graphics import GraphWin, Circle, Polygon, Text, Image, Point
from time import sleep


def main():
    width = 800
    height = 800
    win = GraphWin("ch5", width, height)
    triangle = Polygon(Point(400, 650), Point(300, 450), Point(500, 450))
    triangle.setFill("red")
    triangle.setOutline("red")
    triangle.draw(win)
    circle1 = Circle(Point(175 * 2, 440), 25 * 2)
    circle2 = Circle(Point(225 * 2, 440), 25 * 2)
    circle1.setFill("red")
    circle1.setOutline("red")
    circle2.setFill("red")
    circle2.setOutline("red")
    circle1.draw(win)
    circle2.draw(win)
    message = Text(Point(200 * 2, 350 * 2), "Happy Valentine's Day!")
    message.draw(win)
    arrow = Image(Point(150, 550), "arrow.gif")
    arrow.draw(win)
    for i in range(50):
        arrow.move(5, 1)
        time.sleep(0.1)
    message2 = Text(Point(400, 200), "Click anywhere to close")
    message2.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
