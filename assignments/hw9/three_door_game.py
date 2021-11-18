from button import Button
from graphics import GraphWin, Rectangle, Point, Text
from random import randint


def main():
    width = 800
    height = 800
    win = GraphWin("Three Button Game", width, height)

    button1 = Button(Rectangle(Point(475, 450), Point(325, 350)), "Door2")
    button1.draw(win)

    button2 = Button(Rectangle(Point(275, 450), Point(125, 350)), "Door1")
    button2.draw(win)

    button3 = Button(Rectangle(Point(675, 450), Point(525, 350)), "Door3")
    button3.draw(win)

    top_text = Text(Point(400, 100), "I have a secret door")
    top_text.draw(win)
    bottom_text = Text(Point(400, 700), "Click to choose my door")
    bottom_text.draw(win)

    button_list = [button1, button2, button3]
    random_button = randint(0, 3)

    click = win.getMouse()

    for i in range(3):
        if button_list[i].is_clicked(click):
            if i == random_button:
                button_list[i].color_button("green")
                top_text.setText("You Win!")
                bottom_text.setText("Click to close")
            else:
                button_list[i].color_button("red")
                top_text.setText("you lost!")
                bottom_text.setText("Door" + button_list[i].get_label() + "is my secret door")
            win.getMouse()
            win.close()