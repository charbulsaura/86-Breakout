from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        # INTRODUCE DIRECTION VARIABLE TO CONTROL DIRECTION OF BALL UNDER ball_move()
        self.direction_x = 1
        self.direction_y = 1
        # INCREASED DIFFICULTY- super high y speed
        self.BALL_SPEED_X = 5 #if x speed too high will keep bouncing horizontally (easy row clear with 1 paddle hit)
        self.BALL_SPEED_Y = 12
        self.goto(0,-(950/2-40))

    def ball_reset(self, x, y):
        # self.direction_x = 1
        self.direction_y = 1
        self.goto(x, y)

    def ball_move(self):
        new_x = self.xcor() + self.BALL_SPEED_X * self.direction_x
        new_y = self.ycor() + self.BALL_SPEED_Y * self.direction_y
        self.goto(new_x, new_y)

    def ball_bounce_brick(self):
        self.direction_y= -self.direction_y
        self.direction_x= -self.direction_x

    def ball_bounce_y(self):
        # HOW TO MAKE IT CONTINUE UNTIL IT TRIGGERS NEXT CHECKPOINT?
        # CHANGE DIRECTION --- DONT USE SET COORDINATE? (OR IT WILL JUST SET COORDINATE AND KEEP MOVING AT INITIAL DIRECTION)
        if self.ycor() > 950 / 2:
            # hitupperwall #movedown # change direction and move until hit lower wall
            self.direction_y = -1
        if self.ycor() < -(950/ 2-40): #account for collision hitbox so paddle doesn't appear to be passing through ball
            # hitlowerwall #moveup # change direction and move until hit upper wall
            self.direction_y = 1

    def ball_bounce_x(self):
        #Reduced bounce limits to prevent ball from bouncing from sides
        if self.xcor() > 340-30:
            self.direction_x = -1
        if self.xcor() < -(340-30):
            self.direction_x = 1

    def increase_speed(self):
        self.BALL_SPEED_X += 1
        self.BALL_SPEED_Y += 1
        print(f"{self.BALL_SPEED_X, self.BALL_SPEED_Y}")
