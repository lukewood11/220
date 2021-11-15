"""
Name: <Luke Wood >
<lab11>.py
"""
from random import randint


def words(infile):
    infile = open(infile, "r")
    contents = infile.read()
    return contents.split("\n")


def random_words(list):
    return list[(randint(0, len(list) - 1))]


def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)


def won(word, letters):
    x = fill(word, letters)
    if word == x:
        return True
    else:
        return False


def play():
    w = words("word_list.txt")
    secret = random_words(w)
    incorrect = 0
    guesses = []
    current = "_" * len(secret)
    while incorrect <= 7 and not won(secret, guesses):
        display = fill(secret, guesses)
        print(display)
        print(guesses)
        letter = input("enter a letter")
        while letter in guesses:
            letter = input("enter a different letter")
        guesses.append(letter)
        display = fill(secret, guesses)
        if current != display:
            current = display
        else:
            incorrect += 1


def main():
    play()
    # add other function calls here
    pass


main()
