from turtle import Turtle
import random

LASERS_CREATION = 2        #The speed of the creation of the Lasers. Higher = Slower, Lower = Faster

class Laser():
    def __init__(self):
        self.all_lasers = []
        self.count = 1

    def fire_laser(self, coordinates):
        self.create_lasers(coordinates=coordinates)
        for laser in self.all_lasers:
            if laser.state == "ready":
                laser.showturtle()
                laser.state = 'fire'
                break

    def create_lasers(self, coordinates):
        self.count +=1
        if self.count == LASERS_CREATION:
            new_laser = Turtle('square')
            new_laser.shapesize(stretch_wid=0.1, stretch_len=1)
            new_laser.penup()
            new_laser.color("red")
            new_laser.hideturtle()
            new_laser.goto(coordinates)
            new_laser.setheading(90)
            new_laser.state = "ready"
            self.all_lasers.append(new_laser)
            self.count = 0
    
    def remove_laser(self, laser):
        laser.hideturtle()
        self.all_lasers.remove(laser)

