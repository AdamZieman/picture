# picture.py
# Draws a picture of a movie theater sign promoting their new debute.
# I'm anxious to go to movies without a mask or fear of COVID, while enjoying a refreshing soda 
# and a warm, buttery popcorn

# Course: CSCI 130 (Introduction to Programming)
# Assignment: 5

# Author: Adam Zieman
# Date: March 18, 2021

from graphics import *

def main():
    # <var> = new window (title, length, height)
    win = GraphWin("Can't Wait!",700,500)

    # background color set to white
    win.setBackground("black")

    # MAIN BOAD
    mainBoard = Rectangle(Point(55,50),Point(650,445))
    mainBoard.setFill("firebrick3")
    mainBoard.draw(win)


    # LIGHT BULBS
    # top row of lights
    topCenter = 25
    topRadius = 40
    topLight = 0
    for i in range(15):
        topCenter = topCenter + 40
        topRadius = topCenter + 15
        topLight = Oval(Point(topCenter,60),Point(topRadius,75))
        topLight.setFill("yellow")
        topLight.setOutline("yellow")
        topLight.draw(win)
        
    # bottom row of lights
    bottomCenter = 25
    bottomRadius = 40
    bottomLight = 0
    for i in range(15):
        bottomCenter = bottomCenter + 40
        bottomRadius = bottomCenter + 15
        bottomLight = Oval(Point(bottomCenter,435),Point(bottomRadius,420))
        bottomLight.setFill("yellow")
        bottomLight.setOutline("yellow")
        bottomLight.draw(win)
        
    # left column of lights
    leftCenter = 60
    leftRadius = 75
    leftLight = 0
    for i in range(8):
        leftCenter = leftCenter + 40
        leftRadius = leftCenter + 15
        leftLight = Oval(Point(65,leftCenter),Point(80,leftRadius))
        leftLight.setFill("yellow")
        leftLight.setOutline("yellow")
        leftLight.draw(win)
    
    # right column of lights
    rightCenter = 60
    rightRadius = 75
    rightLight = 0
    for i in range(8):
        rightCenter = rightCenter + 40
        rightRadius = rightCenter + 15
        rightLight = Oval(Point(625,rightCenter),Point(640,rightRadius))
        rightLight.setFill("yellow")
        rightLight.setOutline("yellow")
        rightLight.draw(win)


    # TEXT AREA
    # rectangle outline of text area
    textArea = Rectangle(Point(95,85),Point(610,410))
    textArea.draw(win)
    
    # circle corners to add curve to text box outline
    topLeftCorner = Oval(Point(95,85),Point(135,125))
    topLeftCorner.draw(win)
    topRightCorner = Oval(Point(610,85),Point(570,125))
    topRightCorner.draw(win)
    bottomLeftCorner = Oval(Point(95,410),Point(135,370))
    bottomLeftCorner.draw(win)
    bottomrightCorner = Oval(Point(610,410),Point(570,370))
    bottomrightCorner.draw(win)
    
    # creates a rectangle within text box to hide circle lines
    hide2 = Rectangle(Point(96,100),Point(609,395))
    hide2.setOutline("white")
    hide2.setFill("white")
    hide2.draw(win)
    hide3 = Rectangle(Point(110,86),Point(595,409))
    hide3.setOutline("white")
    hide3.setFill("white")
    hide3.draw(win)
    
    # creates a line on text box corners to appear as a curved box
    # top left corner
    hide4 = Line(Point(95,85),Point(95,100))
    hide4.setOutline("firebrick3")
    hide4.setFill("firebrick3")
    hide4.draw(win)
    hide5 = Line(Point(95,85),Point(110,85))
    hide5.setOutline("firebrick3")
    hide5.setFill("firebrick3")
    hide5.draw(win)

    # top right corner
    hide6 = Line(Point(610,85),Point(610,100))
    hide6.setOutline("firebrick3")
    hide6.setFill("firebrick3")
    hide6.draw(win)
    hide7 = Line(Point(610,85),Point(595,85))
    hide7.setOutline("firebrick3")
    hide7.setFill("firebrick3")
    hide7.draw(win)

    # bottom left corner
    hide8 = Line(Point(95,410),Point(95,395))
    hide8.setOutline("firebrick3")
    hide8.setFill("firebrick3")
    hide8.draw(win)
    hide9 = Line(Point(95,410),Point(110,410))
    hide9.setOutline("firebrick3")
    hide9.setFill("firebrick3")
    hide9.draw(win)

    # bottom right corner
    hide10 = Line(Point(610,410),Point(610,395))
    hide10.setOutline("firebrick3")
    hide10.setFill("firebrick3")
    hide10.draw(win)
    hide11 = Line(Point(610,410),Point(595,410))
    hide11.setOutline("firebrick3")
    hide11.setFill("firebrick3")
    hide11.draw(win)
    
    # creates a circle (x (+/-) 1, y (+/-) 1) over text corner circles to hid majority of circle
    # top left
    hide1 = Oval(Point(96,86),Point(136,126))
    hide1.setOutline("white")
    hide1.setFill("white")
    hide1.draw(win)
    
    # top right
    hide12 = Oval(Point(609,86),Point(569,126))
    hide12.setOutline("white")
    hide12.setFill("white")
    hide12.draw(win)

    # bottom left
    hide13 = Oval(Point(96,369),Point(136,409))
    hide13.setOutline("white")
    hide13.setFill("white")
    hide13.draw(win)

    # bottom right
    hide14 = Oval(Point(609,369),Point(569,409))
    hide14.setOutline("white")
    hide14.setFill("white")
    hide14.draw(win)
    

    # TEXT & LINES
    # displays the text 'NOW FEATURING!'
    nowFeaturing = Text(Point(352.5,130),"NOW FEATURING!")
    nowFeaturing.setStyle("bold")
    nowFeaturing.setSize(36)
    nowFeaturing.setOutline("gold")
    nowFeaturing.draw(win)

    # creates the top line for the text
    topLine = Line(Point(115,160),Point(590,160))
    topLine.setWidth(4)
    topLine.draw(win) 

    # displays the text 'TOP GUN:'
    topGun = Text(Point(352.5,210),"TOP GUN:")
    topGun.setStyle("bold")
    topGun.setSize(36)
    topGun.setOutline("gold")
    topGun.draw(win)

    # creates the middle line for the text
    middleLine = Line(Point(115,240),Point(590,240))
    middleLine.setWidth(4)
    middleLine.draw(win)

    # displays the text 'MAVERICK'
    maverick = Text(Point(352.5,290),"MAVERICK")
    maverick.setStyle("bold")
    maverick.setSize(36)
    maverick.setOutline("gold")
    maverick.draw(win)

    # creates the bottom line for the text
    bottomLine = Line(Point(115,320),Point(590,320))
    bottomLine.setWidth(4)
    bottomLine.draw(win)


    # CONCESSION PICTURES
    # soda
    sodaCup = Polygon(Point(317,355),Point(313,395), Point(295,395),Point(291,355))
    sodaCup.setWidth(2)
    sodaCup.setFill("gray95")
    sodaCup.draw(win)
    straw1 = Line(Point(304,355),Point(304,335))
    straw1.draw(win)
    straw2 = Line(Point(304,335),Point(297,328))
    straw2.draw(win)
    lid = Oval(Point(291,356),Point(317,350))
    lid.setFill("gray39")
    lid.draw(win)
    sodaStrip1 = Line(Point(292,365),Point(317,365))
    sodaStrip1.setOutline("red")
    sodaStrip1.draw(win)
    sodaStrip2 = Line(Point(295,380),Point(314,380))
    sodaStrip2.setOutline("red")
    sodaStrip2.draw(win)
    sodaPoint = Point(304,372)
    sodaPoint.draw(win)

    # popcorn
    popcornBucket = Polygon(Point(362,350),Point(377,395),Point(419,395),Point(434,350))
    popcornBucket.setFill("LightGoldenrod1")
    popcornBucket.draw(win)
    popcornTop = Oval(Point(362,335),Point(434,360))
    popcornTop.setFill("yellow2")
    popcornTop.draw(win)
    popcornY = Text(Point(383,372),"Y")
    popcornY.setSize(14)
    popcornY.setStyle("bold")
    popcornY.setFill("red")
    popcornY.draw(win)
    popcornU = Text(Point(395,380),"U")
    popcornU.setSize(14)
    popcornU.setStyle("bold")
    popcornU.setFill("white")
    popcornU.draw(win)
    popcornM = Text(Point(411,375),"M")
    popcornM.setSize(14)
    popcornM.setStyle("bold")
    popcornM.setFill("blue")
    popcornM.draw(win)

    # while I was stationed at NAS Whidbey Island, they filmed a portion of this movie there
    
main()