from turtle import Turtle


# 14 bricks in every row; width = 600; width (1 brick) = 600/14 =42.85...
# stretch_wid= 42.85/20=2.14
class Bricks(Turtle):
    def __init__(self, **kwargs):
        super().__init__()
        # IMPORTANT: SET COLOR FIRST BEFORE CALCULATING SCORE VALUE!!!
        self.color(kwargs["color"])
        # Add score value to specific color - automatic init when brick created
        self.score = self.calc_score()
        self.speed("fastest")
        self.penup()
        self.goto(kwargs["xy"])
        self.shape("square")
        self.shapesize(stretch_wid=600 / 14 / 20, stretch_len=1)  # width 20, height 100, default is 20/20
        self.setheading(90)

    def calc_score(self):
        #Get turtle color to determine score
        print(f"calc_score: {self.color()}")
        if self.color() == ('yellow', 'yellow'):
            print("yellow")
            return 1
        elif self.color() == ('green', 'green'):
            print("green")
            return 3
        elif self.color() == ('orange', 'orange'):
            print("orange")
            return 5
        elif self.color() == ('red', 'red'):
            print("red")
            return 7
        # print(f"calc_score: {self.score}")

    def create_bricks(self,BRICK_X_COR,BRICK_Y_COR,BRICK_Y_COR_LIST,BRICK_COLOR_LIST,BRICK_ID_LIST,colors):
        # global BRICK_X_COR, BRICK_Y_COR, BRICK_Y_COR_LIST, BRICK_COLOR_LIST, BRICK_ID_LIST, colors
        # --------------CREATING BRICKS--------------------------------#
        # Populate 8 x heights & whole width with bricks (1 SCREEN)
        for y in range(0, 8):
            print(y)
            BRICK_Y_COR_LIST.append(BRICK_Y_COR)
            BRICK_Y_COR = BRICK_Y_COR + 20 + 2  # to show brick lines
        print(BRICK_Y_COR_LIST)
        # Can simplify loop further... but for convenience sake just use this
        for row_number in range(0, 8):
            if row_number <= 1:
                BRICK_COLOR_LIST.append(colors[0])
            elif row_number <= 3:
                BRICK_COLOR_LIST.append(colors[1])
            elif row_number <= 5:
                BRICK_COLOR_LIST.append(colors[2])
            elif row_number <= 7:
                BRICK_COLOR_LIST.append(colors[3])
        print(BRICK_COLOR_LIST)

        # for j in range(0,8,2):
        # print(j)
        # print(colors[int(j / 2)])

        # Assign colors & y coord values to each row object
        for row in range(0, 8):
            BRICK_X_COR = -300 - 600 / 14
            BRICK_Y_COR = BRICK_Y_COR_LIST[row]
            BRICK_COLOR = BRICK_COLOR_LIST[row]
            for i in range(14):
                print(i)
                BRICK_X_COR = BRICK_X_COR + 600 / 14 + 2  # to show brick lines
                # How to assign object/variable to fstring identifier? (brick{i})
                # How to assign only same color rows of bricks to one list?
                brick_ID = Bricks(xy=(BRICK_X_COR, BRICK_Y_COR), color=BRICK_COLOR)

                print(f"brick_ID.color(): {brick_ID.color()}")
                print(f"brick_ID.score: {brick_ID.score}")
                BRICK_ID_LIST.append(brick_ID)
            print(BRICK_ID_LIST)
            print(int(len(BRICK_ID_LIST) / 8))

# BRICK_X_COR = -300 - 600 / 14
# BRICK_Y_COR = 235
# BRICK_Y_COR_LIST = []
# BRICK_COLOR_LIST = []
# BRICK_ID_LIST = []
# colors = ["yellow", "green", "orange", "red"]
#
#
# brick = Bricks(xy=(BRICK_X_COR, BRICK_Y_COR),color="")
# # brick = Bricks(xy=(0,0),color="red")
# print(brick.color())
# print(brick.xcor(), brick.ycor())
# brick.create_bricks()