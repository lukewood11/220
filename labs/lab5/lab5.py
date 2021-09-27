"""
Name: <Luke Wood>
<lab5>.py
"""
import math

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    s1 = Line(p1, p2)
    s2 = Line(p1, p3)
    s3 = Line(p2, p3)
    s1.draw(win)
    s2.draw(win)
    s3.draw(win)
    p1.draw(win)
    p2.draw(win)
    p3.draw(win)
    l1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    l2 = math.sqrt((p2.getX() - p3.getX()) ** 2 + (p2.getY() - p3.getY()) ** 2)
    l3 = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    s = (l1 + l2 + l3) / 2
    area = math.sqrt((s * (s - l1) * (s - l2) * (s - l3)))
    perimeter = l1 + l2 + l3

    text_p = Point(win_width / 2, win_height - 50)
    text_perimeter = Text(text_p, "The Perimeter is: " + str(perimeter))
    text_perimeter.draw(win)

    text_a = Point(win_width / 2, win_height - 30)
    text_area = Text(text_a, "The Area is: " + str(area))
    text_area.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text

    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # Wait for another click to exit
    blue_box = Entry(Point(200, 250), 3)
    blue_box.draw(win)
    red_box = Entry(Point(200, 275), 3)
    red_box.draw(win)
    green_box = Entry(Point(200, 300), 3)
    green_box.draw(win)
    win.getMouse()
    for i in range(5):
        blue = int(blue_box.getText())
        red = int(red_box.getText())
        green = int(green_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)
        win.getMouse()
    win.close()


def process_string():
    string = input("Enter a word with more than 5 letters: ")
    one = string[0]
    print(one)
    two = string[-1]
    print(two)
    three = string[1:5]
    print(three)
    four = string[0] + string[-1]
    print(four)
    five = string[0:3] * 10
    print(five)
    for c in string:
        print(c)
    seven = len(string)
    print(seven)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[2] + values[0] + float(values[5])
    print(x)
    x = len(values)
    print(x)




def another_series():
    n = eval(input("enter number of terms:"))
    acc = 0
    for i in range(n):
        y = 2 + (2 * (i % 3))
        acc = acc + y
        print(y, end=" ")
    print()
    print("Sum", acc)


def main():
    # target()
    # triangle()
    # color_shape()
    pass


main()
