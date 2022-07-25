# Assignment: Breakout Game
"""
Using Python Turtle, build a clone of the 80s hit game Breakout.

Breakout was a hit game originally coded up by Steve Wozniak before he and Jobs started Apple.
It's a simple game that is similar to Pong where you use a ball and paddle to break down a wall.
Breakout Wikipedia Page
https://en.wikipedia.org/wiki/Breakout_(video_game)

You can try out the gameplay here:
https://elgoog.im/breakout/


A good starting point is to review the lessons on Day 22 when we built the Pong game.
But you will have plenty of things to Google, figure out and struggle through to complete this project.
Try to avoid going to a tutorial on how to build breakout, instead spec out the project, figure out how it's going to work.
Write down a checklist of todos and draw out a flow chart (if it helps).
"""
"""
Breakout Wikipedia Page
Breakout begins with eight rows of bricks, with each two rows a different kinds of color. 
The color order from the bottom up is yellow, green, orange and red. 
Using a single ball, the player must knock down as many bricks as possible by using the walls and/or the paddle below to hit the ball against the bricks and eliminate them. 
If the player's paddle misses the ball's rebound, they will lose a turn. 
The player has three turns to try to clear two screens of bricks. 

Yellow bricks earn one point each, green bricks earn three points, 
orange bricks earn five points and the 
top-level red bricks score seven points each. 

The paddle shrinks to one-half its size after the ball has broken through the red row and hit the upper wall. 
Ball speed increases at specific intervals: after four hits, after twelve hits, and after making contact with the orange and red rows.
"""

# APPROACH: Step by step
"""
!1. Create the basic layout first--- 8 rows of bricks. 2x yellow,green,orange,red (using square turtle objects) + paddle + ball
!2. Allocate movement of objects (ball). Account for rebound & speed-- increases aft 4/12/orange/red --- ball_speed=xyz, 
   Ball speed increases aft # of hits (hit_counter=0, +1 speed/hit_counter aft # of collisions)
   (collision check for ball)
!3. Make brick disappear aft ball collision (remove from BRICK_ID_LIST + hide turtle)
!4. Shrink paddle aft breaking red & hit upper wall --- paddle_size = 1/2 paddle_size

Accounting for game state
!5. If 3 turns used, game over --- turns=3, turns-=1 if ball y position <... 
!6. Add score: yellow = 1, green = 3, orange = 5, red = 7. 
Add score variable to BRICK_ID_LIST and access after collision to add to global player score
Add score variable to brick class instead and access score tabulation from there
!7. 2 screens of bricks--- screen_counter to take note/keep track of # of screens cleared
                      --- if screen_counter = 2; stop game loop & display score/ win condition
>>ISSUES:
>>(FIXED: ADD BRICK ID?) How to account for collision with multiple created brick objects? No unique identifier provided...
>>(FIXED: Implemented ball_bounce_brick for specific ball & brick behaviour- also reduced collision hitbox)
    -Weird bounce of ball on paddle/to every single brick aft collision (direction problem?)
    -Ball will bounce upwards and through every single brick
"""
"""
>>IMPROVEMENTS:
--- Allow player to choose difficulty level (easy/medium/hard)
--- Paddle physics; if hit left/right/centre- different effects on ball direction (complicated to implement)
--- Turtle: How to allow for repeat on keypress/move on keyhold?
    repeat command on keypress
"""

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=680 - 40, height=950)
screen.title("Breakout")
screen.tracer(0)

BRICK_X_COR = -300 - 600 / 14
BRICK_Y_COR = 235
BRICK_Y_COR_LIST = []
BRICK_COLOR_LIST = []
BRICK_ID_LIST = []
colors = ["yellow", "green", "orange", "red"]

# --------------CREATING PADDLE--------------------------------#
paddler = Paddle((0, -380 - 150 / 2))

# --------------CREATING BALL----------------------------------#
ball = Ball()
brick_cr= Bricks(xy=(BRICK_X_COR, BRICK_Y_COR),color="")
# --------------CREATING BRICKS--------------------------------#
brick_cr.create_bricks(BRICK_X_COR,BRICK_Y_COR,BRICK_Y_COR_LIST,BRICK_COLOR_LIST,BRICK_ID_LIST,colors)
# -------------KEEPING TRACK OF GAME STATE----------------#
# Deduct turns based on # of missed balls
hit_counter = 0
screen_counter = 0
# turns = 3
# score = 0

# CREATING SCOREBOARD
scoreboard = Scoreboard()
# MAX HIGHSCORE
max_high_score = 0
for brick in BRICK_ID_LIST:
    max_high_score+=brick.score
print(f"MAXIMUM SCORE (1 SCREEN): {max_high_score} ")
print(f"MAXIMUM SCORE (2 SCREEN): {2*max_high_score} ")

# ALLOW PADDLE MOVEMENT
screen.listen()
screen.onkey(paddler.left, "Left")
screen.onkey(paddler.right, "Right")

running = True
while running:
    # Loop checks for event every 0.001 secs
    time.sleep(0.001)
    screen.update()
    # print(ball.xcor(), ball.ycor())
    ball.ball_move()
    ball.ball_bounce_x()
    # Ball only bounce when hitting upper wall/bricks but not lower wall (only bounces upon paddle contact)
    if ball.ycor() > 950 / 2:
        ball.ball_bounce_y()
    # Prevent paddle from exiting window dimension (x)
    if paddler.xcor() > (680 / 2 - 65):
        paddler.goto(680 / 2 - 65, -950/2+20)
    if paddler.xcor() < -(680 / 2 - 45):
        paddler.goto(-(680 / 2 - 45), -(950/2-20))
    # If paddle break red & hit upper wall, reduce paddle size
    if ball.ycor() > 950/2:
        paddler.shapesize(stretch_wid=1, stretch_len=2.5)

    # Account for collision bet ball & paddle
    if ball.distance(
            paddler) < 55:  # tweaked value (increased) bcos it keeps missing collision even when on edge of paddle
        print("PADDLE vs BALL")
        ball.ball_bounce_y()
        # Increase BALL_SPEED_Y from impact -- force
        ball.BALL_SPEED_Y = 12
    # Account for collision bet ball & bricks (individual)
    for brick in BRICK_ID_LIST:
        # if ball.distance(brick) < 5: #TESTING MODE
        if ball.distance(brick) < 25:  # if hitbox too little it will pass through some bricks and not register as collided
            print(len(BRICK_ID_LIST))
            print("BRICK vs BALL")
            # Remove brick from collection & hide display
            # Update hit_counter & score (BASED ON COLOR)
            hit_counter+=1
            print(brick.score)
            scoreboard.score_point(brick.score)

            print(f"hit_counter: {hit_counter}")
            BRICK_ID_LIST.remove(brick)
            brick.hideturtle()
            print(len(BRICK_ID_LIST))
            print(f"BALL SPEED BEF COLLISION: {ball.BALL_SPEED_Y}")

            # TESTING MODE (remove collision) & set super low x speed
            # ball.BALL_SPEED_X = 0.5
            # ball.BALL_SPEED_Y = 9
            ball.ball_bounce_brick()

            # Reduce ball speed to 0 to prevent additional collisions
            # Increase ball speed aft 4/12/orange/red
            ball.BALL_SPEED_Y = 0
            time.sleep(0.001)
            if hit_counter <=3:
                ball.BALL_SPEED_Y = 8
            elif 3<hit_counter<12:
                ball.BALL_SPEED_Y = 10
            elif hit_counter >= 12:
                ball.BALL_SPEED_Y = 18

            print(f"BALL SPEED AFT COLLISION: {ball.BALL_SPEED_Y}")

    # BRICK_ID_LIST=[]
    if len(BRICK_ID_LIST) == 0 and screen_counter==1:
        print("WIN!")
        print(f"screen_counter: {screen_counter}")
        scoreboard.scoreboard_update_end("win")
        running = False
    # If screen cleared but screen_counter!=2, reset ball position & replenish screen
    elif len(BRICK_ID_LIST) == 0:
        ball.ball_reset(paddler.xcor(), -(950/2-40) - 150 / 2)
        screen_counter+=1
        brick_cr.create_bricks(BRICK_X_COR, BRICK_Y_COR, BRICK_Y_COR_LIST, BRICK_COLOR_LIST, BRICK_ID_LIST, colors)

    # Check for lose condition if ball goes out of window
    if ball.ycor() < -1200 / 2:
        print("LOSE 1 TURN!")
        scoreboard.lose_turn()
        print(f"turns: {scoreboard.turns}")
        time.sleep(1)
        ball.ball_reset(paddler.xcor(), -(950/2-40) - 150 / 2)
        print("BALL RESET")
    if scoreboard.turns <= 0:
        scoreboard.scoreboard_update_end("lose")
        running = False

screen.exitonclick()
