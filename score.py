from ctypes import alignment
from turtle import Turtle, update
ALIGNMENT = "center"
FONT = ("Courier", 12 , "normal")
FONT2 = ("Courier", 20 , "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.setposition(0, 280)
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}: High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
            


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


  
    



    
        