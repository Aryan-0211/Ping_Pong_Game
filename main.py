from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create paddles and ball
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Paddle controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Function to check for a winner
def check_winner():
    if scoreboard.l_score == 5:
        scoreboard.game_over("Left Player Wins!")
        return True
    elif scoreboard.r_score == 5:
        scoreboard.game_over("Right Player Wins!")
        return True
    return False

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Continuously update the screen
    time.sleep(0.02)  # Keep a very short delay for ball smoothness
    ball.move()

    # Check for winner and stop the game if a player wins
    if check_winner():
        game_is_on = False  # This will stop the game loop
        break  # Explicitly exit the game loop

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect R Paddle Misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L Paddle Misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
