from graphics import *

def main():
    win = GraphWin()
    message = Text(Point(100,190), "Plese click four points")
    message.draw(win)

    p1 = win.getMouse()
    Circle(p1,5).draw(win)
    
    p2 = win.getMouse()
    Circle(p2,5).draw(win)
    
    p3 = win.getMouse()
    Circle(p3,5).draw(win)
    
    p4 = win.getMouse()
    Circle(p4,5).draw(win)

    Line(p1,p2).draw(win)
    Line(p2,p3).draw(win)
    Line(p3,p4).draw(win)
    Line(p4,p1).draw(win)

    Circle(p1,5).draw(win)

    message.setText("Click To Close")
    win.getMouse()
    win.close()
    
main()
