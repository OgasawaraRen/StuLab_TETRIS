import pygame
import sys
from pygame.locals import *
from Sound import Sound
class Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view
        self.sound = model.sound
        self.key_down_bind = {}
        self.key_down_bind[K_j] = lambda:self.keyDown_Rotate(self.model.tryRotateLeft) #左回転
        self.key_down_bind[K_l] = lambda:self.keyDown_Rotate(self.model.tryRotateRight)#右回転
        self.key_down_bind[K_w] = lambda:self.keyDown_hardDrop() #急降下
        self.key_down_bind[K_d] = lambda:self.model.tryMoveRight() #右移動
        self.key_down_bind[K_a] = lambda:self.model.tryMoveLeft() #左移動
        self.key_down_bind[K_s] = lambda:self.model.tryDrop() #一マス落下
        self.key_down_bind[K_k] = lambda:self.keyDown_hold() #ホールド
        #self.key_down_bind[K_space] =

        self.key_up_bind = {}

    def keyDown_Rotate(self,func):
        if func():#回転可能ならSE
            self.sound.SE("turn")
            #効果音
            pass

    def keyDown_hold(self):
        if self.model.hold():
            self.view.drawHold(self.model.holdMino)
            self.sound.SE("hold")
            #効果音

    def keyDown_hardDrop(self):
        self.model.hardDrop()
        self.view.drawBoard(self.model.board,self.model.mino)
        self.sound.SE("harddrop")
        #効果音



    def keyDown(self, key):
        if key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if key in self.key_down_bind:
            self.key_down_bind[key]()
            self.view.drawBoard(self.model.board,self.model.mino)

    def titleInput(self):
        #何かしらのキー入力を受けるまでループ
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_q:#Qキー押した場合はボイスモード
                        return "voice"
                    return "normal"#それ以外だと通常モード

    def getKeyResultScene(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_t:
                        return "title"
                    elif event.key == K_r:
                        return "retry"
