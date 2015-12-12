#Leslie Gil
#February 24, 2014
#Using Zelle's graphics module, draw your initials-- the first letters of your names.

from graphics import *
def initialsdraw():
    win = GraphWin("My Initials", 200, 200)
    L1 = Line(Point(30,30), Point(30, 100))
    L1.draw(win)

    L2 = Line(Point(30,100), Point(65, 100))
    L2.draw(win)

    G1 = Line(Point(90,30), Point(120, 30))
    G1.draw(win)

    G2 = Line(Point(90,30), Point(90, 100))
    G2.draw(win)

    G3 = Line(Point(90,100), Point(120, 100))
    G3.draw(win)

    G4 = Line(Point(120,100), Point(120, 80))
    G4.draw(win)

    G5 = Line(Point(120,80), Point(110, 80))
    G5.draw(win)
    
    win.getMouse()
    win.close()
initialsdraw()
