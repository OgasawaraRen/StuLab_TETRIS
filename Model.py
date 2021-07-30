import numpy as np
import random
import copy
import Const
from Mino import Mino

class CheckPut():
    #ミノが設置可能かを判断するクラス
    @classmethod
    def canSet(cls,board,mino,x,y,rotate)->bool:
        #設置可能か？(盤外に出ない、既にあるブロックと重ならない)
        for i,minoRow in enumerate(mino.shapes[rotate]):
            blockY = y+i
            for j,block in enumerate(minoRow):
                if block == 0:#ブロックが空白の時は無視
                    continue
                blockX = x+j

                if (blockX >= Const.BOARD_W or blockX < 0 or blockY >= Const.BOARD_H):# ボード外に出ていないか
                    return False
                if blockY < 0:
                    continue
                if board[blockY][blockX] == 1:#盤面に既にブロックがあるか
                    return False
        return True

    @classmethod
    def canDrop(cls,board,mino):
        #1マスしたに移動可能か？
        return cls.canSet(board,mino,mino.x,mino.y+1,mino.rotateNum)

    @classmethod
    def canRotate(cls,board,mino,rotateNum):
        #回転可能か？
        return cls.canSet(board,mino,mino.x,mino.y,rotateNum)

    @classmethod
    def canRotateRight(cls,board,mino):
        #右回転可能か？
        return cls.canRotate(board,mino,(mino.rotateNum+1)%4)

    @classmethod
    def canRotateLeft(cls,board,mino):
        #左回転可能か？
        return cls.canRotate(board,mino,(mino.rotateNum-1)%4)
    
    @classmethod
    def canMoveRight(cls,board,mino):
        #1マス右に移動可能か？
        return cls.canSet(board,mino,mino.x+1,mino.y,mino.rotateNum)

    @classmethod
    def canMoveLeft(cls,board,mino):
        #1マス左に移動可能か？
        return cls.canSet(board,mino,mino.x-1,mino.y,mino.rotateNum)

class Model:
    #ミノ、盤面は左上が(0,0)
    def __init__(self,view):
        self.NUM_MINO = 7 #ミノの数
        self.TRAP = 10 #トラップマスの数
        self.baseShape = [] #７種類のミノ（0°）
        self.allMinos = self.setAllMinos() #7種類のミノ(Mino型)
        self.board = np.zeros([Const.BOARD_H,Const.BOARD_W],dtype=int) #現在の盤面 状態:0=空白 1=ブロックが存在 -1=トラップマス
        self.nexts = self.initNexts(copy.deepcopy(self.allMinos)) #落下するミノ
        self.dropMinoNum = 0 #落下中のミノのインデックス
        self.mino = self.nexts[self.dropMinoNum] #落下中のミノ
        self.holdMino = None #ホールド中のミノ(存在しなければNone)
        self.minoIsOutside = False #ミノが枠外に出ているか？
        self.canHold = True #ホールドが可能か？(ホールドはターンごとに一回のみ可能)
        self.initTraps() #トラップマスを設置
        self.view = view

    def setAllMinos(self)->[Mino]:#1
        #7種類*4のミノを返す
        i_mino = np.array([[ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ]])
        o_mino = np.array([[ 1, 1 ], [ 1, 1 ]])
        t_mino = np.array([[ 0, 1, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ]])
        z_mino = np.array([[ 1, 1, 0 ], [ 0, 1, 1 ], [ 0, 0, 0 ]])
        s_mino = np.array([[ 0, 1, 1 ], [ 1, 1, 0 ], [ 0, 0, 0 ]])
        j_mino = np.array([[ 1, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ]])
        l_mino = np.array([[ 0, 0, 1 ], [ 1, 1, 1 ], [ 0, 0, 0 ]])
        baseShape = [i_mino,o_mino,t_mino,z_mino,s_mino,j_mino,l_mino]
        minoSizes = [(4,3),(2,2),(3,2),(3,2),(3,2),(3,2),(3,2)]
        allminos = [] 
        for i in range(self.NUM_MINO):
            shapes = self.getShapes(baseShape[i])
            mino = Mino(shapes,minoSizes[i])#ミノを生成、４パターンの回転形を設定
            allminos.append(mino)
        return allminos

    def getShapes(self,baseShape)->[np.ndarray]:
        #引数で受け取った形を4パターン(90度回転*4)にして返す
        return [np.rot90(baseShape,i) for i in range(0,-4,-1)]

    def initNexts(self,minos)->[np.ndarray]:
        #14個のミノを返す
        sample1 = random.sample(copy.deepcopy(minos),self.NUM_MINO)
        sample2 = random.sample(copy.deepcopy(minos),self.NUM_MINO)
        nextMinos = sample1 + sample2
        return nextMinos

    def initTraps(self):
        traps = []
        for i in range(Const.BOARD_W): #全ての列にトラップマスを用意する
            traps.append(i)
            random.shuffle(traps)
        for i in range(int(Const.BOARD_H/2)): #二行ごとに一つのトラップマスを用意する
            self.board[i*2,traps[i]] = -1
            

    def checkGameOver(self)->bool:#3 ゲームオーバーだったらTrue,#ゲームオーバーか？
        check = np.count_nonzero(self.board == -1) #-1の数を数える
        if check != self.TRAP:   
            return True
        for row in self.board:
            if np.sum(row) == Const.BOARD_W:
                return True
        return False
    
    def getAlignedLines(self):
        #揃っている行番号のリストを返す
        alignedLines = []
        for i,row in enumerate(self.board):
            if np.sum(row) == Const.BOARD_W:
                alignedLines.append(i)
        return alignedLines

    def setBoardRow(self,rowNum,val):
        #rowNum番目の行全てにvalをセットする
        for i in range(Const.BOARD_W):
            self.board[rowNum][i] = val

    def checkClear(self)->bool:#ミノの１マスごとの値がボードからはみだしていたら
        #クリアしたか？
        return self.minoIsOutside

    def drop(self):
        self.mino.drop()

    def tryDrop(self):
        if CheckPut.canDrop(self.board,self.mino):
            self.drop()
            return True
        else:
            return False

    def tryMoveRight(self):
        if CheckPut.canMoveRight(self.board,self.mino):
            self.mino.moveRight()
            return True
        return False

    def tryRotateRight(self):
        if CheckPut.canRotateRight(self.board,self.mino):
            self.mino.rotateRight()
            return True
        return False
    def tryRotateLeft(self):
        if CheckPut.canRotateLeft(self.board,self.mino):
            self.mino.rotateLeft()
            return True
        return False
    def tryMoveLeft(self):
        if CheckPut.canMoveLeft(self.board,self.mino):
            self.mino.moveLeft()
            return True
        return False

    def putMino(self):
        #盤面にミノを設置(canSetは通過している前提)、ホールドを許可
        self.canHold = True
        self.minoIsOutside = False
        rotateNum = self.mino.rotateNum
        for i,minoRow in enumerate(self.mino.shapes[rotateNum]):
            blockY = i+self.mino.y
            if blockY < 0:#ブロックが上外にある場合無視
                self.minoIsOutside = True
                continue
            for j,block in enumerate(minoRow):
                if block != 0:#ブロックが空白の時は無視
                    blockX = j+self.mino.x
                    if self.board[blockY][blockX] == -1:#トラップマス上に配置する場合
                        self.board[blockY][blockX] = 2
                    else:
                        self.board[blockY][blockX] = block

    def loadMino(self):
        #dropMinoNumをインクリメント,落下ミノを更新(必要があればreloadNext)
        self.dropMinoNum += 1
        if self.dropMinoNum >= 7:
            self.reloadNext()
        self.mino = self.nexts[self.dropMinoNum]
        self.view.drawNexts(self.nexts[self.dropMinoNum+1:self.dropMinoNum+6])

    def reloadNext(self):
        #前半7つを削除、新しく7つを付け足す、dropMinoNumを0に(リセット)
        del self.nexts[:7]
        newNext = random.sample(copy.deepcopy(self.allMinos),self.NUM_MINO)
        self.nexts = self.nexts + newNext
        self.dropMinoNum = 0

    def hold(self):
        #ホールドする
        if self.canHold == True:
            if self.holdMino == None:
                self.holdMino = self.mino
                self.loadMino()
            else:
                changeMino = self.holdMino
                self.holdMino = self.mino
                self.mino = changeMino
            self.canHold = False

            #ホールドミノを初期状態にする
            self.holdMino.x = int(Const.BOARD_W/2) - len(self.holdMino.shapes[0][0])
            self.holdMino.y = -2
            self.holdMino.rotateNum = 0
            return True
        else:
            return False

    def hardDrop(self):
        #ミノを一気に下に落下させる
        y = self.mino.y
        while CheckPut.canSet(self.board,self.mino,self.mino.x,y+1,self.mino.rotateNum):
            y += 1
        self.mino.moveDown(y)
        self.putMino()

    def calcScore(self) -> int:
        check = np.count_nonzero(self.board != 0) #０以外の要素を数える
        result = check / 2
        #スコアを計算する
        return result