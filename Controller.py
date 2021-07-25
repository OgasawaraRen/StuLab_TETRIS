from pygame.locals import *
class Controller:
    def __init__(self,model):
        self.model = model
        #self.sound = model.sound
        self.mino = model.mino
        self.key_down_bind = {}
        self.key_down_bind[K_j] = lambda:self.keyDown(self.model.tryRotateLeft())
        self.key_down_bind[K_l] = lambda:self.model.tryRotateRight()
        self.key_down_bind[K_w] = lambda:self.model.hardDrop()
        self.key_down_bind[K_d] = lambda:self.model.tryMoveRight()
        self.key_down_bind[K_a] = lambda:self.model.tryMoveLeft()
        self.key_down_bind[K_s] = lambda:self.model.tryDrop()
        self.key_down_bind[K_k] = lambda:self.model.hold()

        self.key_up_bind = {}

    def keyDown_Rotate(self,func):
        if func():#回転可能ならSE
            #効果音
            pass



    def keyDown(self, key):
        if key in self.key_down_bind:
            self.key_down_bind[key]()
    
    def keyUp(self, key):
        if key in self.key_up_bind:
            self.key_up_bind[key]()