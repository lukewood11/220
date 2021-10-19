"""
Name: Luke Wood

vigenere.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def code(code_text, keyword_text):
    acc = ""
    code_text = code_text.upper()
    keyword_text = keyword_text.upper()
    code_text = code_text.replace(" ", "")
    keyword_text = keyword_text.replace(" ", "")
    for i in range(len(code_text)):
        l = ord(code_text[i]) - 65
        u = ord(keyword_text[i % len(keyword_text)]) - 65
        k = l + u
        k = k % 26
        k = chr(65 + k)
        acc = acc + k
    return acc


def main():
    win = GraphWin("Vigenere", 500, 500)
    win.setCoords(0, 0, 10, 10)
    message = Text(Point(2, 9), "Message to Code")
    message.draw(win)
    code_input = Entry(Point(5, 9), 25)
    code_input.draw(win)

    keyword = Text(Point(2, 8), "Enter keyword")
    keyword.draw(win)
    keyword_input = Entry(Point(4, 8), 15)
    keyword_input.draw(win)

    entry = Rectangle(Point(4, 7), Point(6, 6))
    entry.draw(win)
    entry_text = Text(Point(5, 6.5), "Encode")
    entry_text.draw(win)

    win.getMouse()

    code_text = code_input.getText()
    keyword_text = keyword_input.getText()

    encrypted = code(code_text, keyword_text)
    entry.undraw()
    entry_text.undraw()

    result = Text(Point(5, 5), "Resulting Message\n" + encrypted)
    result.draw(win)

    click_quit = Text(Point(5, 2), "Click anywhere to close")
    click_quit.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    code
