from turtle import Turtle
class Score:

    def __init__(self, scor):
        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(-50, 250)
        self.point = scor
        self.score.write(f"Your Score is {self.point}", font=('Arial', 15, 'bold'))