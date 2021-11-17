from graphics import *


class Button:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.label = label

    def get_label(self):
        return self.get_label().getText()

    def undraw(self, label):
        self.text.undraw()
        self.shape.undraw()

    def is_clicked(self, point):
        if (self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX()) and (
                self.shape.getP1().getY() <= point.getY() <= self.shape.getP2().getX()):
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)
