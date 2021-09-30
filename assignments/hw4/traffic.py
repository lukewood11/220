"""
Name: Luke Wood
traffic.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    roads = eval(input("How many roads were surveyed? "))
    acc = 0
    for i in range(1, roads + 1):
        surveyed = eval(input("How many days was road " + str(i) + " surveyed"))
        acc2 = 0
        for n in range(1, surveyed + 1):
            traveled = eval(input("How many cars traveled on day " + str(n)))
            acc = acc + traveled
            acc2 = acc2 + traveled
            avg = acc2 / n
        print("Road " + str(i) + " average vehicles per day:", avg)
    print("Total number of vehicles traveled on all roads:", acc)
    avg2 = acc / i
    print("Average number of vehicles per road:", round(avg2, 2))


if __name__ == '__main__':
    main()
