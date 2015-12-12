# Leslie Gil
# March 3, 2014
# Write a program that takes twenty mouse clicks from the user and draws a polygon whose corners, or vertices, are the clicked points.

from graphics import *
def main():
    win = GraphWin("Draw a 20 sided polygon", 300, 300)
    message = Text(Point(145,260), "Click on twenty points")
    message.draw(win)

    # Get and draw vertices of polygon
    firstpoint = win.getMouse()
    firstpoint.draw(win)

    for i in range (19):
        point = win.getMouse()
        point.draw(win)
        line = Line(firstpoint, point)
        line.draw(win)
        firstpoint = point

   

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
