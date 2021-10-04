"""
Name: <Luke Wood>
<ProgramName>.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    first_last = input("Enter first and last name")
    fl_list = first_last.split(" ")
    print(fl_list[1] + ", " + fl_list[0])


def company_name():
    website = input("Enter a three-part internet domain")
    web_ab = website.split(".")
    print(web_ab[1])


def initials():
    names = input("Enter the number of students: ")
    for i in range(int(names)):
        student = input("Enter the name of student: " + str(i + 1))
        last = input("Enter " + student + "'s last name: ")
        print(student + "'s " + "initials are " + student[0].upper() + last[0].upper())


def names():
    name = input("Enter a list of names, first and last separated by commas: ")
    name_split = name.split(", ")
    for i in name_split:
        n = i.split(" ")
        print("The initials are " + n[0][0] + n[1][0])


def thirds():
    number = input("enter the number of sentences: ")
    for i in range(int(number)):
        sent = input("enter sentence " + str(i + 1))
        print(sent[2:-1:3])


def word_average():
    sentence = input("enter a sentence")
    acc = 0
    sentence = sentence.split(" ")
    for i in sentence:
        acc = acc + len(i)
    print(acc/len(sentence))


def pig_latin():
    lat = input("Enter a sentence")
    lat = lat.split(" ")
    for i in lat:
        print(i[1:] + i[0] + "ay", end=" ")

    # def main():
    # name_reverse()
    # add other function calls here
    # initials()

# main()
