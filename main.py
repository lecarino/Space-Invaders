from turtle import Screen, Turtle
from ship import Ship
from ball import Ball
import time
from blocks import Blocks
from scoreboard import Scoreboard
from laser import Laser
import random
from lives import Lives

SHIP_STARTING_COORDINATES = (0,-250)

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Space Invaders")
screen.tracer(0)
vertex = ((0,15),(-15,0),(-18,5),(-18,-5), (0,0), (18,-5), (18,5), (15,0))
screen.register_shape('ship', vertex)

#SpaceShip
ship = Ship(SHIP_STARTING_COORDINATES)
screen.listen()
screen.onkey(fun= ship.left, key= "Left")
screen.onkey(fun= ship.right, key= "Right")


#Alines
blocks = Blocks()
blocks.create_blocks()

#Scoreboard 
scoreboard = Scoreboard()

#Lives
lives = Lives()

# Lasers
laser = Laser()
screen.onkey(lambda: laser.fire_laser((ship.xcor(), ship.ycor())), key="space")

block_laser = Laser()

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    blocks.move_blocks()
    screen.update()  

    #BLOCKS' LASERS 
    random_block = random.choice(blocks.blocks)
    random_number = random.randint(1,10)
    if random_number == 10:
        block_laser.fire_laser((random_block.xcor(),random_block.ycor()))
    for laser_obj in block_laser.all_lasers:
        if laser_obj.state == 'fire':
            laser_obj.backward(10)

        if laser_obj.ycor() < -300:
            laser_obj.hideturtle()

        if laser_obj.distance(ship) < 20:
            if lives.lives > 1:
                ship.destroy_ship()
                block_laser.remove_laser(laser_obj)
                lives.remove_life()
            else:
                game_is_on = False
                lives.clear()
                scoreboard.game_over()
            
    #SHIP'S LASERS
    for laser_obj in laser.all_lasers:
        if laser_obj.state == 'fire':
            laser_obj.fd(20)
        if laser_obj.ycor() > 300:
            laser_obj.hideturtle()

        # COLLISION WITH BLOCKS:
        for block in blocks.blocks:
            if laser_obj.distance(block) < 20:  # Adjust the distance as needed
                blocks.remove_block(block)
                laser.remove_laser(laser_obj)
                scoreboard.point()

    #CHECK IF ALIENS REACH SHIP'S LEVEL:
    lowest_block = min(block.ycor() for block in blocks.blocks)
    if lowest_block == ship.ycor() + 20:
        #Game over:
        game_is_on = False
        scoreboard.game_over()

# Main game loop
screen.mainloop()