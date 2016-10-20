class X:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.lock = threading.RLock()

    def changeA(self):
        with self.lock:
            self.a = self.a + 1

    def changeB(self):
        with self.lock:
            self.b = self.b + self.a

    def changeAandB(self):
        # you can use chanceA and changeB threadsave!
        with self.lock:
            self.changeA() # a usual lock would block in here
            self.changeB()
