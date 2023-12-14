from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-330,270)
        self.write(f'Score {self.score}', align='center', font=(("SPACE RACER", 20, "normal")))
        
    def update_score(self):
        self.goto(-330, 270)
        self.write(f'Score {self.score}', align='center', font=(("SPACE RACER", 20, "normal")))
    
    def point(self):
        self.score +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f'GAME OVER\n Score: {self.score}', align= 'center', font=(("SPACE RACER", 55, "normal")))
