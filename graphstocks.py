from graphics import *
fileName = "appleHistoricalData.csv"
infile = open(fileName, "r")

x = 260
win = GraphWin(fileName, 500, 500)
win.setCoords(-10, 325, 270, 750)

infile.readline()

for line in infile:
    line = line.split('","')
    Point(x,float(line[1])).draw(win)#close
    #low is 5--red
    low = Point(x,float(line[5][:-2]))
    low.setFill('red')
    low.draw(win)
    #high is 4--green
    high = Point(x,float(line[4]))
    high.setFill('green')
    high.draw(win)
    print(x, float(line[1]))
    x -= 1
    
win.getMouse()
infile.close()
