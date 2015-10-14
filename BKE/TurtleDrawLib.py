import turtle

__author__ = 'terence'

### Graphics alias for drawing
global g
g = turtle.Turtle()
global width
global height

'''
### Example colors
###             {"1": "#FF3385", "2": "blue", "3": "yellow", "4": "purple",
###                "5": "green", "6": "orange", "7": "olive", "8": "aqua",
###                "9": "navy", "10": "Beige", "11": "Aquamarine", "12": "Chartreuse",
###                "13": "Mauve", "14": "Crimson", "15": "Lavender"}
'''

def graphicsInit(title,bgcolor,s_width,s_height):
    global width
    width = s_width
    global height
    height = s_height
    # hideturtle() same as ht()
    g.hideturtle()
    # SetWindowResolution
    #turtle.setup (width=200, height=200, startx=0, starty=0)
    turtle.setup(width, height, 0, 0)
    g.speed(0)
    g.tracer(1,0)
    #g.goto(0,0);
    turtle.title(title)
    turtle.bgcolor(bgcolor)
    # screen = g._Screen
    # showturtle() same as st()
    #g.showturtle()

def drawRectangle(x, y, width,height, drawColor, fillColor):
    g.begin_fill()
    g.color(drawColor,fillColor)
    movePen(x, y)
    g.setheading(0)
    g.forward(width)
    g.right(90)
    g.forward(height)
    g.right(90)
    g.forward(width)
    g.right(90)
    g.forward(height)
    g.end_fill()
    g.penup()

#Needs improvement!
def drawCircle(x,y,width,height,drawColor,fillColor,bgcolor):
    g.begin_fill()
    g.color(drawColor,fillColor)
    movePen(x+(width/2), y+(height*0.1))
    g.setheading(0)
    i = 0
    while i < 360:
        g.forward(3.5)
        g.right(3)
        i+=3
    g.end_fill()
    g.begin_fill()
    g.color(drawColor,bgcolor)
    movePen(x+(width/2), y+(height*0.27))
    i = 0
    while i < 360:
        g.forward(2)
        g.right(3)
        i+=3
    #g.circle((height/3))
    #drawC(g,(height/4))
    g.end_fill()

'''
def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawC(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)
'''

def drawCross(x,y,width,height,drawColor,fillColor):

    g.color(drawColor,fillColor)
    moveDrawedPen(x+(width*0.1), y+(height*0.2))
    g.pendown()
    g.begin_fill()
    moveDrawedPen(x+(width*0.1), y+(height*0.2))
    moveDrawedPen(x+(width*0.2), y+(height*0.1))

    moveDrawedPen(x+(width*0.5), y+(height*0.4))

    moveDrawedPen(x+(width*0.8), y+(height*0.1))
    moveDrawedPen(x+(width*0.9), y+(height*0.2))

    moveDrawedPen(x+(width*0.6), y+(height*0.5))

    moveDrawedPen(x+(width*0.9), y+(height*0.8))
    moveDrawedPen(x+(width*0.8), y+(height*0.9))

    moveDrawedPen(x+(width*0.5), y+(height*0.6))

    moveDrawedPen(x+(width*0.2), y+(height*0.9))
    moveDrawedPen(x+(width*0.1), y+(height*0.8))

    moveDrawedPen(x+(width*0.4), y+(height*0.5))

    moveDrawedPen(x+(width*0.1), y+(height*0.2))

    g.end_fill()
    g.penup()

def moveDrawedPen(x, y):
    #Converting to x & y coordinate from topleft position of window, removing negative values, conform standard C# windows forms.
    xx = -(width/2)+x
    yy = (height/2)-y
    g.goto(xx,yy)

def movePen(x, y):
    g.penup()
    #Converting to x & y coordinate from topleft position of window, removing negative values, conform standard C# windows forms.
    xx = -(width/2)+x
    yy = (height/2)-y
    g.goto(xx,yy )
    g.pendown()

def draw_button(x,y,text,fillcolor,drawcolor):
    drawRectangle(x, y, len(text)+4,4, fillcolor, drawcolor)
    g.write("  %s  " % text)

def done():
    turtle.done()

def writeText(text,x,y):
    movePen(x,y)
    #g.speed(3)
    g.color("yellow")
    g.write(text, move=True, align="left", font=("Arial", 10, "normal"))
    #g.speed(3)