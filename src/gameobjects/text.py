# text.py

'''

    (-.-) for the moment kandinsky.draw_string (-.-)
             can't manage the font size

'''


class Text(GameObject):
    def __init__(self, name, x, y, text, textColor = BLACK, backgroundColor = WHITE):
        GameObject.__init__(self, name, x, y)
        self.text = text
        self.textColor = textColor
        self.backgroundColor = backgroundColor

    # text 

    def setText(self, text: str):
        self.text = text

    def getText(self) -> str:
        return self.text

    # backgroundColor

    def setBackgroundColor(self, backgroundColor):
        self.backgroundColor = backgroundColor

    def getBackgroundColor(self):
        return self.backgroundColor

    # textColor 

    def setTextColor(self, textColor):
        self.textColor = textColor
    
    def getTextColor(self):
        return self.textColor

    # draw

    def draw(self):
        draw_string(self.text, self.x, self.y, self.textColor, self.backgroundColor)