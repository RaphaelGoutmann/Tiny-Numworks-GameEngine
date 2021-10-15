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