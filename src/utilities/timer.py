import time

class Timer:
    def __init__(self, delay):
        self.current_time = time.time()
        self.delay = delay

    def elapsed(self):
        if time.time() - self.current_time > self.delay :
            self.current_time = time.time()
            return True
        return False