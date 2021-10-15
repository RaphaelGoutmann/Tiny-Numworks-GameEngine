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