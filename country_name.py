from turtle import Turtle

class Country:

    def __init__(self, name, posx, posy):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.create(self.name, self.posx, self.posy)

    def create(self, name, posx, posy):
        self.text = Turtle()
        self.text.hideturtle()
        self.text.penup()
        self.text.goto(posx, posy)
        self.text.write(name)
