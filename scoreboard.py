from  turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def show_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.left_score}", align="center", font = ("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(f"{self.right_score}", align="center", font=("Courier", 80, "normal"))