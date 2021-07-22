import pygame
from pygame.locals import *
import ViewConst
import numpy as np

class View:
    colors = {0:(58,58,58),1:(250,250,250),-1:(255,0,0)}
    def __init__(self,screen):
        self.screen = screen
        #screen.fill((89,87,87))
        self.screen.fill((0,0,0))


    def drawBoard(self,board,mino):
        blockSize = ViewConst.BLOCK_SIZE
        #落下中のミノ以外の盤面を描画
        for y,row in enumerate(board):
            for x,block in enumerate(row):
                pygame.draw.rect(self.screen, self.colors[board[y,x]], Rect(x*blockSize+5,y*blockSize+5,blockSize,blockSize))
                pygame.draw.rect(self.screen, (160,160,160), Rect(x*blockSize+5,y*blockSize+5,blockSize,blockSize), 1)
        
        #落下中のミノを描画
        for i,minoRow in enumerate(mino.shapes[mino.rotateNum]):
            for j,block in enumerate(minoRow):
                if block == 0:
                    continue
                if mino.y+i >= 0:
                    pygame.draw.rect(self.screen, self.colors[1], Rect((mino.x+j)*blockSize+5,(mino.y+i)*blockSize+5,blockSize,blockSize))
                    pygame.draw.rect(self.screen, (160,160,160), Rect((mino.x+j)*blockSize+5,(mino.y+i)*blockSize+5,blockSize,blockSize), 1)

        pygame.display.update()


    def drawHold(self,holdMino):
        pass

    def drawNexts(self,nexts):
        pass


