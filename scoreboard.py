from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.turns = 3
        self.score = 0
        self.scoreboard_update()

    def scoreboard_update_end(self,result):
        self.clear()
        self.goto(0, 0)
        if result == "win":
            self.write(f"BREAKOUT MISSION ACCOMPLISHED! HIGH SCORE: {self.score}", align="center", font=("Consolas", 15 , "normal"))
        if result == "lose":
            self.write(f"BREAKOUT FAILED! SCORE: {self.score}", align="center", font=("Consolas", 30 , "normal"))

    def scoreboard_update(self):
        self.clear()
        self.goto(0, 950/2-30)
        self.write("CAN YOU BREAKOUT???", align="center", font=("Consolas", 20 , "normal"))
        self.goto(680/2-100, 950/2-30)
        self.write(f"TURNS REMAINING: {self.turns}", align="center", font=("Consolas", 10 , "normal"))
        self.goto(0, 950/2-80)
        self.write(self.score, align="center", font=("Consolas", 40 , "normal"))

    def score_point(self,score_value):
        self.score += score_value
        self.scoreboard_update()

    def lose_turn(self):
        self.turns-=1
        self.scoreboard_update()