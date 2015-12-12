#Leslie Gil
#February 27th, 2014
#Write a program that takes two mouse clicks from the user and draws rectangle whose corners include the two points clicked.

from graphics import *

def main():
    win = GraphWin("Draw a rectangle", 350, 350)
    message = Text(Point(175, 330), "Click on two points to draw a rectangle")
    message.draw(win)

    # Get and draw two corners of rectangle
    p1 = win.getMouse()
    p1.draw(win)
    
    p2 = win.getMouse()
    p2.draw(win)

    # Use Rectangle object to draw rectangle
    rectangle = Rectangle(p1,p2)
    rectangle.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
