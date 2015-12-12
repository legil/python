# click.py
from graphics import *

def main():
    win = GraphWin("Click Me!")
    oldPoint = win.getMouse()
    for i in range(20):
        p = win.getMouse()
        print("You clicked at:", p.getX(), p.getY())
        Line(oldPoint,p).draw(win)
        oldPoint = p
        p.draw(win)
        
    
main()
