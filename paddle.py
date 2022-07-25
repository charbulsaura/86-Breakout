from turtle import Turtle

#Add hit_counter
class Paddle(Turtle):
    def __init__(self, xy):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(xy)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)  # width 20, height 100, default is 20/20
        self.setheading(0)
        self.hit_counter= 0

    def left(self):
        self.setheading(0)
        self.backward(20)

    def right(self):
        self.setheading(0)
        self.forward(20)
