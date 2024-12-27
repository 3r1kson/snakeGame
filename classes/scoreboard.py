import os.path
from turtle import Turtle

ALIGNMENT = "center"

FONT = ('Courier', 15, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        if os.path.exists('score.txt'):
            with open('score.txt', mode="r") as file:
                self.high_score = int(file.read())
        else:
            self.high_score = 0

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.refresh()


    def increase_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            print("Updating")
            with open('score.txt', mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.refresh()




