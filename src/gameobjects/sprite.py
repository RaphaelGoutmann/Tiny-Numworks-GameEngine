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