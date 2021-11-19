from random import randint
from graphics import GraphWin, Rectangle, Point, Text
from button import Button




def main():
    width = 400
    height = 400
    win = GraphWin("Three Button Game", width, height)

    button1 = Button(Rectangle(Point(60, 210), Point(140, 250)), "Door1")
    button1.draw(win)

    button2 = Button(Rectangle(Point(160, 210), Point(240, 250)), "Door2")
    button2.draw(win)

    button3 = Button(Rectangle(Point(260, 210), Point(340, 250)), "Door3")
    button3.draw(win)

    top_text = Text(Point(200, 100), "I have a secret door")
    top_text.draw(win)
    bottom_text = Text(Point(200, 350), "Click to choose my door")
    bottom_text.draw(win)

    button_list = [button1, button2, button3]
    random_button = button_list[randint(0, 2)]

    click = win.getMouse()

    if random_button.is_clicked(click):
        random_button.color_button("green")
        u_win = Text(Point(200, 100), "you win")
        top_text.undraw()
        bottom_text.undraw()
        u_win.draw(win)
        close = Text(Point(200, 350), "click to close")
        close.draw(win)
    else:
        if button1.is_clicked(click):
            button1.color_button("red")
            u_lose = Text(Point(200,100), "you lose!")
            top_text.undraw()
            bottom_text.undraw()
            close = Text(Point(200, 350), "Door" + random_button + "is my secret door")
            close.draw(win)
            u_lose.draw(win)

        elif button2.is_clicked(click):
            button2.color_button("red")
            u_lose = Text(Point(200, 100), "you lose!")
            top_text.undraw()
            bottom_text.undraw()
            close = Text(Point(200, 350), "Door" + random_button + "is my secret door")
            u_lose.draw(win)

        elif button3.is_clicked(click):
            button3.color_button("red")
            u_lose = Text(Point(200, 100), "you lose!")
            top_text.undraw()
            bottom_text.undraw()
            close = Text(Point(200, 350), "Door" + random_button + "is my secret door")
            close.draw(win)
            u_lose.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()