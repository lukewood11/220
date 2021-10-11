"""
Name: <Luke Wood >
Partner: <your partner's name goes here – first and last>
<lab7>.py
"""


def cash_conversion():
    dollar = eval(input("Enter an integer: "))
    print('${:.2f}'.format(dollar))


def encode():
    code = input("Enter a message: ")
    num_val = eval(input("Enter a number: "))
    acc = ""
    for c in code:
        i = ord(c)
        add = num_val + i
        new = chr(add)
        acc = acc + new
    print(acc)


def sphere_area(radius):
    area = 4 * 3.14159 * radius ** 2
    return area


def sphere_volume(radius):
    volume = (4 / 3) * 3.14159 * radius ** 3
    return volume


def sum_n(n):
    acc = 0
    for i in range(n + 1):
        acc = acc + i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n + 1):
        acc = acc + (i ** 3)
    return acc


def encode_better():
    s1 = input("Enter a string: ")
    s2 = input("Enter another string:")
    acc = ""
    for i in range(len(s1)):
        c = ord(s1[i])
        key = ord(s2[i])
        both = c + key - 97
        acc = acc + chr(both)
    print(acc)


def main():
    cash_conversion()
    encode()
    print(sphere_area(5))
    print(sphere_volume(5))
    print(sum_n(3))
    print(sum_n_cubes(3))
    # add function calls here
    pass


main()
