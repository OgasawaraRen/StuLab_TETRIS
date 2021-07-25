import pygame
from pygame.locals import *
from View import View
from Model import Model
from Controller import Controller
import Const
import sys
import time
blockSize = Const.BLOCK_SIZE
WIN_SIZE = (blockSize*10+240,blockSize*20+12)
WIN_TITLE=""

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WIN_SIZE)
        pygame.display.set_caption(WIN_TITLE)
        self.view = View(self.screen)
        self.model = Model(self.view)
        #self.sound = Sound()
        self.controller = Controller(self.model)
    
    def startGame(self):
        #while True:
            #Title
            #self.playGame()
            #Resurt

        self.playGame()

    def playGame(self):
        dropFrame = 60#60f毎に落下
        dropFrame = 6
        frameCount = 0
        while not (self.isGameOver() or self.isClear()):
            self.drawBoard()
            time.sleep(0.01)
            frameCount += 1
            if frameCount >= dropFrame:
                frameCount = 0
                if not self.tryDrop(): #落下可能なら落下
                    #落下不可能な場合
                    self.putMino() #ミノ設置
                    if self.isClear():
                        break
                    self.loadMino()#落下ミノ更新
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.controller.keyDown(event.key)
        
        if self.isGameOver():
            print("GAME OVER")
        else:
            print("CLERA")


    def isGameOver(self):
        return self.model.checkGameOver()

    def isClear(self):
        return self.model.checkGameOver()

    def canDrop(self):
        return self.model.canDrop()
    
    def tryDrop(self):
        canDrop = self.model.tryDrop()
        self.drawBoard()
        return canDrop

    def putMino(self):
        self.model.putMino()
        self.drawBoard()

    def loadMino(self):
        self.model.loadMino()
    
    def drawBoard(self):
        self.view.drawBoard(self.model.board,self.model.mino)
    
    def drawHold(self):
        pass

    def drawNext(self):
        pass




if __name__ == "__main__":
    app = App()
    app.startGame()