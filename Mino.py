class Mino():
    def __init__(self):
        self.shapes = []
        self.x = 0
        self.y = 0
        self.rotateNum = 0
    
    def rotateRight(self):
        self.rotateNum = (self.rotateNum+1)%4

    def rotateLeft(self):
        self.rotateNum = (self.rotateNum-1)%4