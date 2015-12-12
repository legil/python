#Leslie Gil
#February 25th, 2014
#Using Zelle's graphics module, draw a snow-person.
#Your display should contain 3 or more circles forming the body, as well as shapes for the mouth and eyes.
#Use the Text object to include your name in the picture

from graphics import*
def main():
    win = GraphWin("Snow Man", 300,300)
    
    bottomcircle = Circle(Point(150,230), 60)
    bottomcircle.draw(win)

    middlecircle = Circle(Point(150,124), 45)
    middlecircle.draw(win)

    topcircle = Circle(Point(150, 49), 30)
    topcircle.draw(win)

    lefteye = Circle(Point(134, 43), 5)
    lefteye.draw(win)
    lefteye.setFill('black')

    righteye = lefteye.clone()
    righteye.move(30,0)
    righteye.draw(win)
    

    mouth = Line(Point(132, 65), Point(166, 65))
    mouth.draw(win)

    rightsmile = Line(Point(132,65), Point(132, 60))
    rightsmile.draw(win)

    leftsmile = Line(Point(166,65), Point(166, 60))
    leftsmile.draw(win)

    leftarm = Line(Point(103,124), Point(85, 144))
    leftarm.draw(win)

    rightarm = Line(Point(194, 124), Point(208, 147))
    rightarm.draw(win)

    name = Text(Point(150, 260),"Leslie Gil")
    name.draw(win)
    
    win.getMouse()
main()
                        
