##1.  Set up a turtle, and use it to draw circle boundaries to measure 
##    distance from start.
##2.  For 500 turns,
##3.    Choose a random direction:  north, west, south, or east
##         and walk 10 steps in that direction

import turtle
import random




##Note that the only way to reach the first elif is if direction was already bigger than 1/4, so, there is no need to include it in our test statement on the elif.
##
##We hid all the set up in the function, setUpTurtle(), to make the main() function easier to read.
##In turn, to make setUpTurtle() easier to read, we placed on the repeated statements for creating
##rings in a function drawRings().

def drawRing(t,radius,color):
    t.up()
    t.goto(0,-radius)
    t.color(color)
    t.down()
    t.circle(radius)

def setUpTurtle():
    #Create turtle
    t = turtle.Turtle()

    #Use the turtle to draw the rings:
    drawRing(t,100,"green")
    drawRing(t,200,"yellow")
    drawRing(t,300,"red")

    #Return turtle to starting position and set shape, speed, and color:
    t.up()
    t.home()
    t.down()
    t.color("purple")
    t.shape("turtle")
    t.speed(10)

    #Return turtle to used elsewhere in the program:
    return t



##The function random.random() returns a number between 0 and 1. Since we have four different directions, we will divide the possible range into 4 (equal) regions:
##
##    numbers between 0 and 1/4,
##    numbers between 1/4 and 1/2,
##    numbers between 1/2 and 3/4, and
##    numbers between 3/4 and 1. 
##
##When our random number is in the first region (between 0 and 1/4), we will turn right 90 degrees. For the next region (between 1/4 and 1/2) we will turn right 180 degrees. For the third region (between (1/2 and 3/4), we will turn left 90 degrees (equivalent to turning right 270 degrees but with a little less whiplash for the poor turtle). Finally, if the random number is in the last region (between 3/4 and 1), we will go straight (i.e. not turn at all).
##
##We can translate all these decisions into python using if and elif constructs:

def main():
    tess = setUpTurtle()
    
    for steps in range(500):
        direction = random.random()
        if direction < 1/4:
            tess.right(90)
        elif direction < 1/2:
            tess.right(180)
        elif direction < 3/4:
            tess.left(90)
        tess.forward(10)

    turtle.Screen().exitonclick()
main()
