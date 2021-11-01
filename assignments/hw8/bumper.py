"""
Name: Luke Wood

bumper.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

import time

from random import randint

from graphics import Circle, color_rgb, GraphWin, Point


def main():
    width = 400
    height = 400
    win = GraphWin("bumper", width, height)
    circle_1 = Circle(Point(randint(25, 375), randint(25, 375)), 25)
    circle_2 = Circle(Point(randint(25, 375), randint(25, 375)), 25)
    circle_1.draw(win)
    circle_2.draw(win)
    circle_1.setFill(get_random_color())
    circle_2.setFill(get_random_color())
    win.setBackground(get_random_color())
    c1x = get_random(20)
    c1y = get_random(20)
    c2x = get_random(20)
    c2y = get_random(20)

    while not win.checkMouse():
        circle_1.move(c1x, c1y)
        circle_2.move(c2x, c2y)
        if hit_vertical(circle_1, win):
            c1x = -c1x
        if hit_vertical(circle_2, win):
            c2x = -c2x
        if hit_horizontal(circle_1, win):
            c1y = -c1y
        if hit_horizontal(circle_2, win):
            c2y = -c2y
        if did_collide(circle_1, circle_2):
            c1x = -c1x
            c2x = -c2x
            c1y = -c1y
            c2y = -c2y
        time.sleep(.1)

    win.getMouse()
    win.close()


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(circle, circle2):
    distance = math.sqrt((circle.getCenter().getX() - circle2.getCenter().getX()) ** 2 + (
                circle.getCenter().getY() - circle2.getCenter().getY()) ** 2)

    return distance <= circle.getRadius() + circle2.getRadius()


def hit_vertical(circle, win):
    if circle.getCenter().getX() + circle.getRadius() >= win.getWidth() \
            or circle.getCenter().getX() - circle.getRadius() <= 0:
        return True
    return False


def hit_horizontal(circle, win):
    if circle.getCenter().getY() + circle.getRadius() >= win.getHeight() \
            or circle.getCenter().getY() - circle.getRadius() <= 0:
        return True
    return False


def get_random_color():
    return color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))


if __name__ == "__main__":
    main()
