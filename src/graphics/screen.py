# screen.py

screenWidth, screenHeight = 320, 240

def fillScreen(color):
    fill_rect(0, 0, screenWidth, screenHeight, color)

def clearScreen():
    fillScreen(WHITE)