# unify.py

import sys  # argv

paths =     ["src/header.py",

             "src/math/vector.py",

             "src/utils/stopwatch.py",
             "src/utils/error.py",
             
             "src/graphics/graphics.py",
             "src/graphics/color.py",
             "src/graphics/screen.py", 

             "src/events.py", 
             "src/game.py", 
             "src/scene.py", 
             "src/gameobject.py", 

             "src/gameobjects/circle.py", 
             "src/gameobjects/rectangle.py", 
             "src/gameobjects/sprite.py",
             "src/gameobjects/text.py"]


def usage():
    print("usage: python3 unify [output]")

def main():
    
    if len(sys.argv) != 2:
        usage()
        exit()

    # output = open("output/tinyengine.py", "w")
    output = open(sys.argv[1], 'w')

    for path in paths:
        file = open(path, "r")
        output.write(file.read() + '\n\n')

main()