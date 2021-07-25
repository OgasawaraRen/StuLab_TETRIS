from pygame.locals import *
class Controller:
    def __init__(self,Model):
        self.model = Model
        self.mino = Model.mino
        self.key_down_bind = {}
        self.key_down_bind[K_j] = lambda:self.model.tryRotateLeft() #= self.Mino.rotateLeft()
        self.key_down_bind[K_l] = lambda:self.model.tryRotateRight()
        self.key_down_bind[K_w] = lambda:self.model.hardDrop()
        self.key_down_bind[K_d] = lambda:self.model.tryMoveRight()
        self.key_down_bind[K_a] = lambda:self.model.tryMoveLeft()
        self.key_down_bind[K_s] = lambda:self.model.tryDrop()
        self.key_down_bind[K_k] = lambda:self.model.hold()

    def keyDown(self, key):
        if key in self.key_down_bind:
            self.key_down_bind[key]()