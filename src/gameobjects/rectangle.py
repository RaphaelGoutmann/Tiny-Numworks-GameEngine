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