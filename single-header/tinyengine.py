import math 
import time
from kandinsky import *

# vector.py

class Vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # equal

    def __eq__(self, other):

        if not isinstance(other, Vector2):
            return False

        return ((self.x == other.x) and (self.y == other.y))

    # addition

    def __add__(self, other):

        if isinstance(other, Vector2):
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other

        return Vector2(x, y)

    __radd__ = __add__

    # substraction 

    def __sub__(self, other):

        if isinstance(other, Vector2):
            x = self.x - other.x
            y = self.y - other.y
        else:
            x = self.x - other
            y = self.y - other

        return Vector2(x, y)

    def __rsub__(self, other):

        if isinstance(other, Vector2):
            x = other.x - self.x
            y = other.y - self.y
        else:
            x = other - self.x
            y = other - self.y

        return Vector2(x, y)

    # multiplication

    def __mul__(self, other):

        if isinstance(other, Vector2):
            x = self.x * other.x
            y = self.y * other.y
        else:
            x = self.x * other
            y = self.y * other

        return Vector2(x, y)

    __rmul__ = __mul__

    # division

    def __truediv__(self, other):

        if isinstance(other, Vector2):
            x = self.x / other.x
            y = self.y / other.y
        else:
            x = self.x / other
            y = self.y / other

        return Vector2(x, y)

    def __rtruediv__(self, other):

        if isinstance(other, Vector2):
            x = other.x / self.x
            y = other.y / self.y
        else:
            x = other / self.x
            y = other / self.y

        return Vector2(x, y)

    # utility

    def mean(self) -> float:
        return ( (self.x + self.y) / 2.0 )

    def isnull(self) -> bool():
        return ((self.x == 0) and (self.y == 0))

    # up, down, right, left

    def up(self):
        return Vector2(0, -1)

    def down(self):
        return Vector2(0, 1)

    def right(self):
        return Vector2(1, 0)
    
    def left(self):
        return Vector2(-1, 0)

# stopwatch.py

'''

    (-.-) This code needs to be improved because (-.-)
                 there's lot of bugs                    

'''

# u_u
class Stopwatch:
    def __init__(self):
        self.startTime = 0

    def start(self):
        self.startTime = time.monotonic()

    def reset(self):
        self.startTime = 0

    def time(self):
        return (time.time() - self.startTime)


# error.py

def error(error) -> None:
    print("error: " + str(error) ) # there's no way to quit graphics mode on numworks calculator for the moment

# graphics.py

# Merci kandinsky pour la diversité de fonctions offertes par ton API <3

def circle(point, radius, borderColor, borderSize):

    x0, y0 = point
    for i in range(borderSize):
        xd = x0 - int((radius-i) / math.sqrt(2))
        xf = x0 + int((radius-i) / math.sqrt(2))
        
        for x in range(xd, xf + 1):
            x1 = x
            y1 = y0 + int(math.sqrt((radius-i) ** 2 - (x - x0) ** 2))
            set_pixel(x, y1, borderColor)

            for j in range(3):
                x2 = x0 + y1 - y0
                y2 = y0 + x0 - x1
                set_pixel(x2, y2, borderColor)
                x1, y1= x2, y2

def fillCircle(point, radius, borderColor, borderSize, backgroundColor):
    circle(point, radius, borderColor, borderSize)
    circle(point, (radius - borderSize), backgroundColor, (radius - borderSize))

def line(p0, p1, color):
    x1, y1 = p0
    x2, y2 = p1
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    
    for x, y in points:
        set_pixel(x, y, color)


def horizontalLine(point, length, color):
    (x, y) = point
    for count in range(length):
        set_pixel(x, y, color)
        x += 1
        
def verticalLine(point, length, color):
    (x, y) = point
    for count in range(length):
        set_pixel(x, y, color)
        y += 1

# color.py

BLACK    = color(0, 0, 0)
WHITE    = color(255, 255, 255)

BLUE     = color(0, 0, 255)
RED      = color(255, 0, 0)
GREEN    = color(0, 255, 0)

CYAN     = color(0, 255, 255)
MAGENTA  = color(255, 0, 255)
YELLOW   = color(255, 255, 0)

# color treatment

def grayscale(color):
    lightness = (0.21 * color[0]) + (0.72 * color[1]) + (0.07 * color[2])
    return color(lightness, lightness, lightness)       # ...

def invert(color):
    return color(255 - color[0], 255 - color[1], 255 - color[2])

# screen.py

screenWidth, screenHeight = 320, 240

def fillScreen(color):
    fill_rect(0, 0, screenWidth, screenHeight, color)

def clearScreen():
    fillScreen(WHITE)

# events.py

# nothing for the moment

# game.py

class Game:
    def __init__(self):
        self.currentScene = None

    def start(self):
        pass

    def update(self):
        self.draw()

    def draw(self):

        if self.currentScene == None:
            return

        self.currentScene.draw()

    # scene management

    def setCurrentScene(self, scene):
        self.currentScene = scene

    def getCurrentScene(self):
        return self.currentScene

# scene.py

class Scene:
    def __init__(self, backgroundColor = WHITE):
        self.gameobjects = []
        self.backgroundColor = backgroundColor

    # gameobjects list

    def addGameObject(self, obj):
        self.gameobjects.append(obj)

    def removeGameObject(self, obj):
        self.gameobjects.remove(obj)

    def countGameObjects(self):
        return len(self.gameobjects)

    def clear(self):
        self.gameobjects.clear()

    def getGameObjectsByName(self, name):

        o = []
        for gameobject in self.gameobjects:
            if name == gameobject.name:
                o.append(gameobject)

        return o


    def getGameObjectsByType(self, t):

        o = []
        for gameobject in self.gameobjects:
            if type(gameobject) == t:
                o.append(gameobject)
                
        return o

    # backgroundColor

    def setBackgroundColor(self, backgroundColor):
        self.backgroundColor = backgroundColor

    def getBackgroundColor(self):
        return self.backgroundColor

    # draw

    def draw(self):
        fillScreen(self.backgroundColor)

        for gameobject in self.gameobjects:
            if gameobject.isActive():
                gameobject.draw()            # draws the object if it's visible

# sprite.py

class GameObject:
    def __init__(self, name: str, x: int, y: int):
        
        self.name = name

        self.x, self.y = x, y
        self.enabled = True

    # name

    def getName(self) -> str:
        return self.name

    def setName(self, name: str):
        self.name = name

    # position

    def setPosition(self, x, y):
        self.x, self.y = x, y

    def getPosition(self):
        return (self.x, self.y)

    def setX(self, x: int):
        self.x = x
    
    def setY(self, y: int):
        self.y = y

    def getX(self) -> int:
        return self.x
    
    def getY(self) -> int:
        return self.y

    # visibility 

    def setActive(self, x: bool):
        self.enabled = x

    def isActive(self) -> bool:
        return self.enabled

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

# circle.py

class Circle(GameObject):
    def __init__(self, name, x, y, radius, borderSize, borderColor = BLACK, backgroundColor = WHITE):
        GameObject.__init__(self, name, x, y)
        self.radius = radius
        self.backgroundColor = backgroundColor

        self.borderSize = borderSize
        self.borderColor = borderColor
        self.backgroundColor = backgroundColor

    # background color

    def setBackgroundColor(self, backgroundColor):
        self.backgroundColor = backgroundColor

    def getBackgroundColor(self):
        return self.backgroundColor

    # border color

    def setBorderColor(self, borderColor):
        self.borderColor = borderColor

    def getBorderColor(self):
        return self.borderColor

    # border size

    def setBorderSize(self, borderSize):
        self.borderSize = borderSize

    def getBorderSize(self):
        return self.borderSize

    # radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    # draw ^-^

    def draw(self):
        fillCircle((self.x, self.y), self.radius, self.borderColor, self.borderSize, self.backgroundColor)

# rectangle.py

class Rectangle(GameObject):

    def __init__(self, name: str, x: int, y: int, width: int, height: int, backgroundColor = WHITE):
        GameObject.__init__(self, name, x, y)
        self.width, self.height = width, height
        self.backgroundColor = backgroundColor

    # dimensions 

    def getDimensions(self):
        return (self.width, self.height)

    def setDimensions(self, width, height):
        self.width, self.height = width, height

    def setWidth(self, width: int):
        self.width = width

    def getWidth(self) -> int:
        return self.width

    def setHeight(self, height: int):
        self.height = height

    def getHeight(self) -> int:
        return self.height

    # backgroundColor

    def getBackgroundColor(self):
        return self.backgroundColor

    def setBackgroundColor(self, backgroundColor):
        self.backgroundColor = backgroundColor

    # draw

    def draw(self):
        fill_rect(self.x, self.y, self.width, self.height, self.backgroundColor)

# sprite.py

class Sprite(GameObject):

    def __init__(self, name: str, x: int, y: int, data):
        GameObject.__init__(self, name, x, y)
        self.data = data
        self.scaleX, self.scaleY = 1, 1 

    # scale

    def getScale(self):
        return (self.scaleX, self.scaleY) 

    def setScale(self, scaleX, scaleY):
        self.scaleX, self.scaleY = scaleX, scaleY

    def getScaleX(self) -> int:
        return self.scaleX

    def setScaleX(self, scaleX: int):
        self.scaleX = scaleX

    def getScaleY(self) -> int:
        return self.scaleY

    def setScaleY(self, scaleY: int):
        self.scaleY = scaleY

    # data

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    # operations

    def revertX(self):
        for line in self.data:
            line.reverse()

    def revertY(self):
        self.data.reverse()

    # draw ^_^

    def draw(self):
        
        for y in range( len(self.data) ):
            for x in range( len(self.data[y]) ):
                fill_rect(x * self.scaleX + self.x, y * self.scaleY + self.y, self.scaleX, self.scaleY, self.data[y][x])

# text.py

'''

    (-.-) for the moment kandinsky.draw_string (-.-)
             can't manage the font size

'''


class Text(GameObject):
    def __init__(self, name, x, y, text, textColor = BLACK, backgroundColor = WHITE):
        GameObject.__init__(self, name, x, y)
        self.text = text
        self.textColor = textColor
        self.backgroundColor = backgroundColor

    # text 

    def setText(self, text: str):
        self.text = text

    def getText(self) -> str:
        return self.text

    # backgroundColor

    def setBackgroundColor(self, backgroundColor):
        self.backgroundColor = backgroundColor

    def getBackgroundColor(self):
        return self.backgroundColor

    # textColor 

    def setTextColor(self, textColor):
        self.textColor = textColor
    
    def getTextColor(self):
        return self.textColor

    # draw

    def draw(self):
        draw_string(self.text, self.x, self.y, self.textColor, self.backgroundColor)

