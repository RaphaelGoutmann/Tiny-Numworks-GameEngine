from GameEngine import *
from ion import *

def main():
    game = Game()
    mainScene = Scene()
    game.setCurrentScene(mainScene)

    player = Rectangle("player", 0, 0, 10, 10, BLACK)
    mainScene.addGameObject(player)

    while(1):
        speed = Vector2(0, 0)

        if keydown(KEY_LEFT):
            speed = speed.left()
        elif keydown(KEY_RIGHT):
            speed = speed.right()
        elif keydown(KEY_UP):
            speed = speed.up()
        elif keydown(KEY_DOWN):
            speed = speed.down()
        
        player.setX(player.getX() + speed.x)
        player.setY(player.getY() + speed.y)

        game.update()

main()