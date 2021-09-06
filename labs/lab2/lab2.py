"""
Name: <Luke Wood >
<lab2>.py
"""
import math


def sum_of_threes():
    upper_bound= eval(input("enter upper bound"))
    total = 0
    for x in range(0, upper_bound + 1, 3):
        total+=x
    print(total)

def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h*l, end=" ")
        print()

def triangle_area():
    a = eval(input("enter length 1"))
    b = eval(input("enter length 2"))
    c = eval(input("enter length 3"))
    s = ((a + b + c)/2)
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(A)

def sumSquares():
    lower_range = eval(input("enter lower range"))
    upper_range = eval(input("enter upper range"))
    total = 0
    for x in range(lower_range, upper_range+1):
        total+= (x*x)
    print(total)

def power():
    base = eval(input("enter base"))
    exponent = eval(input("enter exponent"))
    total = 1
    for x in range(exponent):
        total*= base
    print(base,"^", exponent,"=",total)
