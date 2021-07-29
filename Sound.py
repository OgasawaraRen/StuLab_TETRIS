import pygame
from pygame.locals import *
import sys

class Sound:
    def __init__(self):
        pass

    def playBgm(self):
        pygame.mixer.init(frequency = 44100)
        bgm = pygame.mixer.Sound("sample.wav")     # 音楽ファイルの読み込み
        bgm.play()
    
    def endBgm(self):
        pygame.mixer.music.stop()


    def SE(self,word):

        if word == "Landing" :
            landing = pygame.mixer.Sound("Landingmino.wav") #着地
            landing.play()
        #SE("Landing")で実行

        if word == "turn" :
            turn = pygame.mixer.Sound("turn.wav")
            turn.play()
""""
        turn = pygame.mixer.Sound("ファイル名")
        Descent = pygame.mixer.Sound("ファイル名")
        gamestart = pygame.mixer.Sound("ファイル名")
        gameover = pygame.mixer.Sound("ファイル名")
        gameclear = pygame.mixer.Sound("ファイル名")

        #変数.play() #効果音の出力
"""