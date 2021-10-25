# stopwatch.py

# u_u
class Stopwatch:
    def __init__(self):
        self.startTime = inf

    def start(self):
        self.startTime = time.monotonic()

    def reset(self):
        self.startTime = inf

    def time(self):
        difference = time.monotonic() - self.startTime

        if difference < 0 :
            return 0

        return difference