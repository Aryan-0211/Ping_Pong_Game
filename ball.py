from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 4  # Reduced from 10 to 4 for slower movement
        self.y_move = 4  # Reduced from 10 to 4 for slower movement
        self.move_speed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1  # After hitting the wall, reverse the y direction

        
    def bounce_x(self):
        self.x_move *= -1  # After hitting the paddle, reverse the x direction
        self.move_speed *= 0.9
                
    def reset_position(self):
        self.goto(0, 0)  # Reset ball to the center
        self.move_speed = 0.1
        self.bounce_x()  # Reverse the x direction after reset
