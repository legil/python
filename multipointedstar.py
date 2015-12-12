#Leslie Gil
#February 13, 2014
#Use turtle graphics to draw a multi-pointed star. Your star must have at least 10 points (or outer corners)

import turtle
def main():
    pen =  turtle.Turtle()
    sides = 12
    turn = 150
    
    for x in range(sides):
        pen.forward(200)
        pen.left(turn)

    turtle.exitonclick()
main()

