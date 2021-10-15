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