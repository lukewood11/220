"""
Name: <Luke Wood>
<lab12>.py
"""

from random import randint


def find_and_remove(list, value):
    try:
        i = list.index(value)
        list[i] = "Luke"
    except:
        pass


def read_data(filename):
    f = open("filename", "r")
    data = f.read()
    data = data.split()
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if i == search_val:
            return True
        i += 1
    return False


def good_input():
    x = eval(input("enter a number"))
    while x <= 1 or x > 10:
        x = eval(input("enter a number"))
    return x


def num_digits():
    num = eval(input("enter a number"))
    while num >= 1:
        digits = 0
        while num != 0:
            num //= 10
            digits += 1
        print("total digits:", digits)
        num = eval(input("enter a number"))


def hi_lo_game():
    secret = randint(1, 100)
    guess = 0
    num = eval(input("guess a number 1-100"))
    while num != secret and guess < 7:
        guess+=1
        if num > secret:
            print("your number was too high")
        else:
            print("your number was too low")
        num = eval(input("guess a number 1- 100"))
    if num == secret and guess < 7:
        print("you win")
    else:
        print("you lose, the number was" + str(secret))


def main():
    # add other function calls here
    #good_input()
    #num_digits()
    hi_lo_game()
    pass


main()
