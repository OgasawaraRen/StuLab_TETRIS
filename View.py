import pygame
from pygame.locals import *
import Const
import numpy as np
class Font:
    def __init__(self):
        self.impact = {
                30:pygame.font.SysFont("impact", 30),
                35:pygame.font.SysFont("impact", 35),
                38:pygame.font.SysFont("impact", 38),
                50:pygame.font.SysFont("impact", 50),
                60:pygame.font.SysFont("impact", 60)}

class View:
    
    def __init__(self,screen,font):
        self.colors = Const.BOARD_COLORS
        self.frameColors = Const.FRAME_COLORS
        self.backgroundColor = Const.BACKGROUND_COLOR
        self.screen = screen
        self.screen.fill(self.backgroundColor)
        self.titleImage = pygame.image.load(Const.TITLE_BACK_IMAGE)
        self.font = font

    def drawBoard(self,board,mino=None):
        blockSize = Const.BLOCK_SIZE
        #落下中のミノ以外の盤面を描画
        for y,row in enumerate(board):
            for x,block in enumerate(row):
                pygame.draw.rect(self.screen, self.colors[board[y,x]], Rect(x*blockSize+5,y*blockSize+5,blockSize,blockSize))
                pygame.draw.rect(self.screen, (160,160,160), Rect(x*blockSize+5,y*blockSize+5,blockSize,blockSize), 1)
        if mino != None:
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
        #文字を描画
        font = self.font.impact[30]
        text = font.render("HOLD", True, self.frameColors["green"])
        self.screen.blit(text, [380, 25])

        blockSize = Const.HOLD_BLOCK_SIZE
        frame_x = 380
        frame_y = 70

        #枠を描画
        pygame.draw.rect(self.screen, self.backgroundColor,Rect(frame_x,frame_y,blockSize*5,blockSize*5))
        pygame.draw.rect(self.screen, self.frameColors["green"],Rect(frame_x,frame_y,blockSize*5,blockSize*5),3)

        #ミノを描画
        if holdMino != None:
            frameMid_x = frame_x+((blockSize*5)/2)
            frameMid_y = frame_y+((blockSize*5)/2)
            #pygame.draw.rect(self.screen, self.backgroundColor,Rect(frameMid_x,frameMid_y,blockSize*5,blockSize*5))
            minoWidth = holdMino.width*blockSize
            minoHeight = holdMino.height*blockSize
            for i,minoRow in enumerate(holdMino.shapes[0]):
                for j,block in enumerate(minoRow):
                    if block == 0:
                        continue
                    pygame.draw.rect(self.screen, self.colors[1], Rect((j)*blockSize+(frameMid_x-(minoWidth/2)),(i)*blockSize+frameMid_y-minoHeight/2,blockSize,blockSize))
                    pygame.draw.rect(self.screen, (160,160,160),  Rect((j)*blockSize+(frameMid_x-(minoWidth/2)),(i)*blockSize+frameMid_y-minoHeight/2,blockSize,blockSize), 1)


    def drawNexts(self,nexts):

        #文字を描画
        font = self.font.impact[30]
        text = font.render("NEXT", True, self.frameColors["white"])
        self.screen.blit(text, (390, 230))

        #最上段のNEXT描画
        topBlockSize = Const.TOP_NEXT_BLOCK_SIZE
        blockSize = NEXT_BLOCK_SIZE = 15
        frame_x = 390
        topFrame_y = 265
        #枠を描画
        pygame.draw.rect(self.screen, self.backgroundColor,Rect(frame_x,topFrame_y,topBlockSize*5,topBlockSize*5))
        pygame.draw.rect(self.screen, self.frameColors["white"],Rect(frame_x,topFrame_y,topBlockSize*5,topBlockSize*5),3)
        #ミノを描画
        frameMid_x = frame_x+((topBlockSize*5)/2)
        frameMid_y = topFrame_y+((topBlockSize*5)/2)
        minoWidth = nexts[0].width*topBlockSize
        minoHeight = nexts[0].height*topBlockSize
        for i,minoRow in enumerate(nexts[0].shapes[0]):
            for j,block in enumerate(minoRow):
                if block == 0:
                    continue
                pygame.draw.rect(self.screen, self.colors[1], Rect((j)*topBlockSize+(frameMid_x-(minoWidth/2)),(i)*topBlockSize+frameMid_y-minoHeight/2,topBlockSize,topBlockSize))
                pygame.draw.rect(self.screen, (160,160,160),  Rect((j)*topBlockSize+(frameMid_x-(minoWidth/2)),(i)*topBlockSize+frameMid_y-minoHeight/2,topBlockSize,topBlockSize), 1)

        gap = 10
        frame_y = topFrame_y+topBlockSize*5+gap
        frameMid_x = frame_x+((blockSize*5)/2)
        for i in range(4):
            #枠を描画
            pygame.draw.rect(self.screen, self.backgroundColor,Rect(frame_x,frame_y,blockSize*5,blockSize*5))
            pygame.draw.rect(self.screen, self.frameColors["white"],Rect(frame_x,frame_y,blockSize*5,blockSize*5),3)

            #ミノを描画
            frameMid_y = frame_y+((blockSize*5)/2)
            minoWidth = nexts[i+1].width*blockSize
            minoHeight = nexts[i+1].height*blockSize
            for j,minoRow in enumerate(nexts[i+1].shapes[0]):
                for k,block in enumerate(minoRow):
                    if block == 0:
                        continue
                    pygame.draw.rect(self.screen, self.colors[1], Rect((k)*blockSize+(frameMid_x-(minoWidth/2)),(j)*blockSize+frameMid_y-minoHeight/2,blockSize,blockSize))
                    pygame.draw.rect(self.screen, (160,160,160),  Rect((k)*blockSize+(frameMid_x-(minoWidth/2)),(j)*blockSize+frameMid_y-minoHeight/2,blockSize,blockSize),1)
            frame_y += blockSize*5+gap

    def drawTitle(self):
        self.screen.blit(self.titleImage,(0,0))
        pygame.display.update()


    def drawResult(self,resultData):
        s = pygame.Surface((Const.WIN_SIZE),pygame.SRCALPHA)
        s.fill((0,0,0,100))
        win_w = Const.WIN_SIZE[0]
        win_h = Const.WIN_SIZE[1]
        frame_w = win_w*0.8
        frame_h = win_h*0.5
        frame_x = win_w/2-frame_w/2
        frame_y = win_h*0.25
        #背景描画
        pygame.draw.rect(s, Const.BACKGROUND_ALPHA_COLOR, Rect(frame_x,frame_y,frame_w,frame_h))
        pygame.draw.rect(s, self.frameColors["white"], Rect(frame_x,frame_y,frame_w,frame_h),5)

        #文字描画
        resultText = ""
        if resultData[0] == "game over":
            resultText = self.font.impact[50].render("GAME OVER", True, self.frameColors["white"])
        elif resultData[0] == "clear":
            resultText = self.font.impact[50].render("CLEAR", True, self.frameColors["white"])
            #スコア描画
            scoreText = self.font.impact[60].render("SCOER:"+str(resultData[1])+"%", True, self.frameColors["white"])
            score_rect = scoreText.get_rect(center = (Const.WIN_SIZE[0] // 2, frame_y+150))
            s.blit(scoreText ,score_rect)
        
        text_rect = resultText.get_rect(center = (Const.WIN_SIZE[0] // 2, frame_y+50))
        s.blit(resultText, text_rect)
        
        #区切り線を描画
        pygame.draw.line(s,self.frameColors["white"],(frame_x+30,frame_y+90),(frame_x+frame_w-30,frame_y+90),2)


        #画面遷移キー説明を描画
        text_x = frame_x+50
        retryText = self.font.impact[35].render("RETRY:R", True, self.frameColors["white"])
        s.blit(retryText, (text_x,frame_y+200))
        titleText = self.font.impact[35].render("TITLE:T", True, self.frameColors["white"])
        s.blit(titleText, (text_x,frame_y+250))
        quitText = self.font.impact[35].render("QUIT:ESC", True, self.frameColors["white"])
        s.blit(quitText,  (text_x,frame_y+300))


        self.screen.blit(s,(0,0))
        pygame.display.update()


