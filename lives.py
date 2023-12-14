from turtle import Turtle, Screen

class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.goto(330,270)
        self.write(f'Lives {self.lives}', align='center', font=(("SPACE RACER", 20, "normal")))
        
    def remove_life(self):
        self.lives -= 1
        self.clear()
        self.goto(330, 270)
        self.write(f'Lives {self.lives}', align='center', font=(("SPACE RACER", 20, "normal")))
    
    