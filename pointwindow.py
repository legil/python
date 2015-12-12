#Simple graphics program
from graphics import *
def main():
    win = win.GraphWin()
    rect = Rectangle(Point(100, 100), Point(100, 100))
    rect.draw(win)
    win.getMouse()
    win.close()
main()
    
