import Const

class Mino:
    def __init__(self,shapes,size):
        self.shapes = shapes #ミノの形
        self.x = (Const.BOARD_W//2) - (len(shapes[0][0])//2)#x座標
        self.y = -2 #y座標
        self.rotateNum = 0 # 値×90度 時計回りに回転
        self.width = size[0]
        self.height = size[1]
    
    def rotateRight(self):
        self.rotateNum = (self.rotateNum+1)%4

    def rotateLeft(self):
        self.rotateNum = (self.rotateNum-1)%4

    def moveRight(self):
        self.x += 1
    
    def moveLeft(self):
        self.x -= 1

    def drop(self):
        self.y += 1
    
    def moveDown(self,moved_y):
        self.y = moved_y