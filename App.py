import pygame
from pygame.locals import *
from View import View
from View import Font
from Model import Model
from Sound import Sound
from Controller import Controller
import Const
import sys
import time
blockSize = Const.BLOCK_SIZE
WIN_SIZE = Const.WIN_SIZE
WIN_TITLE="REV_TETRIS"

class App:
    def __init__(self):
        pygame.init()
        self.font = Font()
        self.sound = Sound()
        self.screen = pygame.display.set_mode(WIN_SIZE)
        pygame.display.set_caption(WIN_TITLE)
        self.view = View(self.screen,self.font)
        self.model = Model(self.view,self.sound)
        self.controller = Controller(self.model,self.view)

    def startGame(self):
        while True:
            self.view.drawTitle()
            mode = self.controller.titleInput()
            while True:
                self.resetGame(mode)
                resultData = self.playGame()
                self.view.drawResult(resultData)
                key = self.controller.getKeyResultScene()
                self.sound.cancelBgm()
                if key == "retry":
                    continue
                elif key == "title":
                    break

    def resetGame(self,mode):
        self.screen = pygame.display.set_mode(WIN_SIZE)
        pygame.display.set_caption(WIN_TITLE)
        self.view = View(self.screen,self.font)
        self.sound = Sound(mode)
        self.model = Model(self.view,self.sound)
        self.controller = Controller(self.model,self.view)

    def playGame(self):
        self.initDraw() #初期状態の画面描画
        dropFrame = 30 #30f毎に落下
        frameCount = 0
        self.sound.playBgm() #BGMstart
        self.sound.SE("start") #startvoice
        while not (self.isGameOver() or self.isClear()):
            self.drawBoard()
            pygame.time.wait(10)
            frameCount += 1
            if frameCount >= dropFrame:
                frameCount = 0
                if not self.tryDrop(): #落下可能なら落下
                    #落下不可能な場合
                    self.putMino() #ミノ設置
                    self.sound.SE("Landing")#着地音
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
            self.sound.SE("gameover")
            self.sound.endBgm()
            alignedLines = self.model.getAlignedLines()
            if len(alignedLines) != 0:
                for rowNum in alignedLines:
                    self.model.setBoardRow(rowNum,3)
            self.view.drawBoard(self.model.board)
            print("GAME OVER")
            return ("game over",0)
        else:
            self.sound.SE("gameclear") #clearvoice
            self.sound.endBgm() #bgm終了
            if Score.calcScore() >= 90:  #高得点限定ボイス
                self.sound.SE("perfect")
            print("CLERA")
            return ("clear",self.getScore())


    def isGameOver(self):
        return self.model.checkGameOver()

    def isClear(self):
        return self.model.checkClear()

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

    def getScore(self):
        return Score.calcScore(self.model.board)

    def initDraw(self):
        self.view.drawBoard(self.model.board,self.model.mino)
        self.view.drawNexts(self.model.nexts[1:6])
        self.view.drawHold(self.model.holdMino)

    def drawBoard(self):
        self.view.drawBoard(self.model.board,self.model.mino)



if __name__ == "__main__":
    app = App()
    app.startGame()