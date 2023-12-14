from turtle import Turtle
from itertools import cycle
import random
from laser import Laser

class Blocks():
    def __init__(self):
        super().__init__()
        self.blocks= []
        self.direction = 1
        
    def create_blocks(self): #THIS WAS ALL TRIAL AND ERROR
        colors = ['blue', 'green', 'yellow', 'orange', 'red']
        color_iterator = cycle(colors) #Need this to not mess with the double for loop

        for y in range(250, 100, -30):
            color = next(color_iterator)
            for x in range(-300, 300, 60):
                block = Turtle(shape='square')
                block.penup()
                block.shapesize(stretch_wid= 1, stretch_len= 1)
                block.color(color)
                block.goto(x,y)
                self.blocks.append(block)
    
    def remove_block(self, block):
        block.hideturtle()
        self.blocks.remove(block)
        
    def move_blocks(self):
        for block in self.blocks:
            x, y = block.position()
            block.setx(x + self.direction * 1)
            
        self.check_boundary()

    def check_boundary(self):
        rightmost_block_x = max(block.xcor() for block in self.blocks)
        leftmost_block_x = min(block.xcor() for block in self.blocks)

        if rightmost_block_x > 320 or leftmost_block_x < -320:
            self.direction *= -1  # Change direction

            # Move the blocks down
            for block in self.blocks:
                block.sety(block.ycor() - 10)

        
    