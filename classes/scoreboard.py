from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
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
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.home()
        self.write("Game over!", False, align=ALIGNMENT, font=FONT)

