"""
Name: <Luke Wood>
<lab9>.py
"""
import math

from graphics import *


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def toNumbers(strlist):
    for i in range(len(strlist)):
        strlist[i] = float(strlist[i])


def writeSumofSqaures():
    infile = input("enter an input file name: ")
    outfile = input("enter an outfile name: ")
    readfile = open(infile, "r")
    writefile = open(outfile, "w")
    for line in infile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
        writefile.write("Sum of squares= ", +str(summation) + "\n")


def starter():
    weight = eval(input("enter the weight"))
    wins = eval(input("enter the number of wins the player has had"))
    if 150 <= weight < 160 and wins >= 5:
        print("starter")
    elif weight > 199 or wins > 20:
        print("starter")
    else:
        print("not a starter")


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("it is a leap year")
    else:
        print("it is not a leap year")


def circleOverlap():
    win = GraphWin("Circle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)
    r3 = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if r3 <= r + r2:
        x = Text(Point(100, 200), "the circles overlap")
        x.draw(win)
    else:
        x = Text(Point(100, 200), "the circles do not overlap")
        x.draw(win)

    win.getMouse()
    win.close()


def main():
    #addTen()
    #squareEach()
    #sumList()
    #toNumbers()
    #writeSumofSqaures()
    #starter()
    #leapYear()
    circleOverlap()
    # add other function calls here
    pass


main()
