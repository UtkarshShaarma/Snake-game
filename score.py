from turtle import Turtle

Align="center"
Font=("Arial",24,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}",align=Align, font=Font)




    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def Game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="Center", font=Font)