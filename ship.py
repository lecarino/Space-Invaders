from turtle import Turtle

class Ship(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("ship")
        self.color("white")
        self.penup()
        self.setposition(coordinates)
        self.setheading(90)

    def left(self):
        new_x = self.xcor()-20
        self.goto((new_x,self.ycor()))
    
    def right(self):
        new_x = self.xcor()+20
        self.goto((new_x,self.ycor()))

    def destroy_ship(self):
        for _ in range(3):  # Blink three times
            self.hideturtle()
            self.getscreen().update()
            self.getscreen().ontimer(self.show_after_delay, 200)  # 200 milliseconds delay
            self.getscreen().update()
            self.getscreen().ontimer(self.hide_after_delay, 200)  # 200 milliseconds delay
            self.getscreen().update()
            self.getscreen().ontimer(self.show_after_delay, 200)  # 200 milliseconds delay

    def show_after_delay(self):
        self.showturtle()
        self.getscreen().update()

    def hide_after_delay(self):
        self.hideturtle()
        self.getscreen().update()


