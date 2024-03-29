import pygame
import random
from pygame.locals import *
import sys

class Sound:
    def __init__(self,mode="normal"):
        self.mode = mode

    def playBgm(self):
        pygame.mixer.init(frequency = 44100)
        def bgm0():
            pygame.mixer.music.load(f"Sound/bgm0.wav")     # 音楽ファイルの読み込み
            pygame.mixer.music.play(-1)
            
        def bgm1():
            pygame.mixer.music.load(f"Sound/bgm1.wav")     # 音楽ファイルの読み込み
            pygame.mixer.music.play(-1)
                

        def bgm2():
            pygame.mixer.music.load(f"Sound/bgm2.wav")     # 音楽ファイルの読み込み
            pygame.mixer.music.play(-1)

        random.choice([bgm0,bgm1,bgm2])()


    def endBgm(self):
        pygame.mixer.music.fadeout(5000)

    def cancelBgm(self):
        pygame.mixer.music.fadeout(0)


    def SE(self,word):

        if word == "start" :

            def start0():
                start = pygame.mixer.Sound(f"Sound/{self.mode}/start0.wav")
                start.play()
            def start1():
                start = pygame.mixer.Sound(f"Sound/{self.mode}/start1.wav")
                start.play()    
            def start2():
                start = pygame.mixer.Sound(f"Sound/{self.mode}/start2.wav")
                start.play()
               

            random.choice([start0,start1,start2])()

        if word == "Landing" :
            landing = pygame.mixer.Sound(f"Sound/{self.mode}/Landingmino.wav") #着地
            landing.play()
        #SE("Landing")で実行

        if word == "turn" :
            turn = pygame.mixer.Sound(f"Sound/{self.mode}/turn.wav")
            turn.play()
    
        if word == "gameover" :
            over = pygame.mixer.Sound(f"Sound/{self.mode}/gameover.wav") 
            over.play()
            over1 = pygame.mixer.Sound(f"Sound/{self.mode}/gameover1.wav") 
            over1.play()
            over1.set_volume(0.8)

        if word == "gameclear" :

            def clear0():
                clear = pygame.mixer.Sound(f"Sound/{self.mode}/clear0.wav")
                clear.play()
                clear.set_volume(1)
            
            def clear1():
                clear = pygame.mixer.Sound(f"Sound/{self.mode}/clear2.wav")
                clear.play()
                clear.set_volume(1)
                
            def clear2():
                clear = pygame.mixer.Sound(f"Sound/{self.mode}/clear2.wav")
                clear.play()
                clear.set_volume(1)

            random.choice([clear0,clear1,clear2])()


        if word == "harddrop" :

            drop = pygame.mixer.Sound(f"Sound/{self.mode}/drop.wav")
            drop.play()
        
        if word == "hold" :
            def hold0():
                hold_0 = pygame.mixer.Sound(f"Sound/{self.mode}/hold0.wav")
                hold_0.play()
            
            def hold1():
                hold_1 = pygame.mixer.Sound(f"Sound/{self.mode}/hold1.wav")
                hold_1.play()

            def hold2():
                hold_2 = pygame.mixer.Sound(f"Sound/{self.mode}/hold2.wav")
                hold_2.play()

            random.choice([hold0,hold1,hold2])()
        
        if word == "perfect" :
            
            perfect = pygame.mixer.Sound(f"Sound/{self.mode}/perfect.wav")
            perfect.play()


