from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.game_over_flag = False  # Flag to check if the game is over
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    
    def l_point(self):
        if not self.game_over_flag:  # Prevent incrementing score after game is over
            self.l_score += 1
            self.update_scoreboard()
            if self.l_score == 5:  # Change 5 to any winning score
                self.game_over("Left Player Wins!")

    def r_point(self):
        if not self.game_over_flag:  # Prevent incrementing score after game is over
            self.r_score += 1
            self.update_scoreboard()
            if self.r_score == 5:  # Change 5 to any winning score
                self.game_over("Right Player Wins!")

    def game_over(self, winner):
        self.game_over_flag = True  # Set the flag to True to stop the game loop
        self.clear()
        self.goto(0, 50)
        self.write(f"Game Over!", align="center", font=("Courier", 36, "normal"))
        self.goto(0, -50)
        self.write(f"{winner}!", align="center", font=("Courier", 48, "bold", "italic"))
        
        # Optionally, add a pause effect before closing or restart prompt
        self.goto(0, -100)
        self.write("Click to Exit", align="center", font=("Courier", 24, "normal"))
