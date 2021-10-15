# stopwatch.py

'''

    (-.-) This code needs to be improved because (-.-)
                 there's lot of bugs                    

'''

# u_u
class Stopwatch:
    def __init__(self):
        self.startTime = 0

    def start(self):
        self.startTime = time.monotonic()

    def reset(self):
        self.startTime = 0

    def time(self):
        return (time.time() - self.startTime)
