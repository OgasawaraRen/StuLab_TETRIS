class Mino():
    def __init__(self):
        self.shapes = [] #ミノの形
        self.x = 0 #x座標
        self.y = 0 #y座標
        self.rotateNum = 0 # 値×90度 時計回りに回転
    
    def rotateRight(self):
        self.rotateNum = (self.rotateNum+1)%4

    def rotateLeft(self):
        self.rotateNum = (self.rotateNum-1)%4