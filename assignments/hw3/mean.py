"""
Name: Luke Wood
mean.py

Problem: this program calculates RMS, Harmonica Mean, and Geometric Mean

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def main():
    total_values = eval(input("enter the values to be entered:"))
    acc = 0
    acc2 = 0
    acc3 = 1
    for i in range(1, total_values + 1):
        value = eval(input("enter value " + str(i)))
        acc = acc + value ** 2
        acc2 = acc2 + (1 / value)
        acc3 = acc3 * value
    rms_average = math.sqrt((acc / total_values))
    harmonic_mean = total_values / acc2
    geometric_mean = acc3 ** (1 / total_values)
    print(round(rms_average, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))


if __name__ == '__main__':
    main()
