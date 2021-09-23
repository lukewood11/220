"""
Name: <Luke Wood>
<Lab3>.py
"""


def average():
    total = eval(input("enter number of grades"))
    acc = 0
    for i in range(1, total +1):
        grade = eval(input("Enter you grade on HW" + str(i)))
        acc = acc + grade
    average = acc/total
    print("Average grade =", average)

#def tip_jar():
    acc = 0
    for i in range(5):
        tip = eval(input("enter tip amount"))
        acc = acc + tip
    total = acc
    print("total tip amount =", total)

#def newton():
    number = eval(input("enter a number"))
    refines = eval(input("enter number of runs"))
    acc = 0
    approx = number/2
    for i in range(refines):
        approx = (approx + number/ approx)/2
    print(approx)


#def sequence():
    num = eval(input("enter the number of terms"))
    for i in range(1, num + 1):
        sq = 1 + (i//2 *2)
        print(sq)

#def pi():
    term = eval(input("enter the number of terms"))
    acc = 1
    for i in range(term):
        nu = 2 + (i//2 * 2)
        dem = 1 + ((i + 1)//2 * 2)
        frac = nu/dem
        acc = acc * frac
    print(acc)

