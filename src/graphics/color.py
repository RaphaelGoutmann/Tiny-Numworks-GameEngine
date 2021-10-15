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