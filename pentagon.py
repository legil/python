#Leslie Gil
#February 10, 2014
#Draw a 6-sided figure or hexagon

import turtle

def main():
    leslie = turtle.Turtle()    #Set up a turtle named "leslie"
    myWin = turtle.Screen()     #The graphics window

    #Draw a square
    for i in range(6):
        leslie.forward(50)     #Move forward 50 steps
        leslie.right(60)       #Turn 60 degrees to the right
        leslie.forward(50)     #Move forward 50 steps

    myWin.exitonclick()         #Close the window when clicked
    
main()		
		
