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