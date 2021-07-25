import numpy as np
import random
from Mino import Mino

class Model:
    #ミノ、盤面は左上が(0,0)

    def __init__(self,view):
        self.BOARD_W = 10 #盤面の幅
        self.BOARD_H = 20 #盤面の高さ
        self.NUM_MINO = 7 #ミノの数
        self.TRAP = 10
        self.baseShape = [] #７種類のミノ（０度）
        self.allMinos = self.setAllMinos() #7種類のミノ(Mino型)
        self.board = np.zeros([self.BOARD_H,self.BOARD_W]) #現在の盤面 状態:0=空白 1=ブロックが存在 -1=トラップマス
        self.nexts = self.initNexts(self.allMinos) #落下するミノ
        self.dropMinoNum = 0 #落下中のミノのインデックス
        self.mino = self.nexts[self.dropMinoNum] #落下中のミノ
        self.holdMino = None #ホールド中のミノ(存在しなければNone)
        #self.hold = Hold()
        self.minoIsOutside = False #ミノが枠外に出ているか？
        self.canHold = False #ホールドが可能か？(ホールドはターンごとに一回のみ可能)
        self.initTraps() #トラップマスを設置
        self.view = view
        self.view.drawBoard(self.board,self.mino)

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
        allminos = [] 
        for i in range(self.NUM_MINO):
            shapes = self.getShapes(baseShape[i])
            mino = Mino(shapes)#ミノを生成、４パターンの回転形を設定
            allminos.append(mino)
        return allminos.copy()

    def getShapes(self,baseShape)->[np.ndarray]:
        #引数で受け取った形を4パターン(90度回転*4)にして返す
        return [np.rot90(baseShape,i).copy() for i in range(0,-4,-1)]

    def initNexts(self,minos)->[np.ndarray]:
        #14個のミノを返す
        sample1 = random.sample(minos,self.NUM_MINO)
        sample2 = random.sample(minos,self.NUM_MINO)
        nextMinos = sample1 + sample2
        return nextMinos

    def initTraps(self):
        traps = []
        for i in range(self.BOARD_W): #全ての列にトラップマスを用意する
            traps.append(i)
            random.shuffle(traps)
        for i in range(int(self.BOARD_H/2)): #二行ごとに一つのトラップマスを用意する
            self.board[i*2,traps[i]] = -1
            


    def checkGameOver(self)->bool:#3 ゲームオーバーだったらTrue,#ゲームオーバーか？
        check = np.count_nonzero(self.board == -1) #-1の数を数える
        if check != self.TRAP:   
            return True
        for row in self.board:
            if np.sum(row) == self.BOARD_W:
                return True
        return False

    def checkClear(self)->bool:#ミノの１マスごとの値がボードからはみだしていたら
        #クリアしたか？
        return self.minoIsOutside

    def canSet(self,x,y,rotate)->bool:
        #設置可能か？(盤外に出ない、既にあるブロックと重ならない)
        for i,minoRow in enumerate(self.mino.shapes[rotate]):
            blockY = y+i
            for j,block in enumerate(minoRow):
                if block == 0:#ブロックが空白の時は無視
                    continue
                blockX = x+j
                if blockY < 0:
                    continue

                if (blockX >= self.BOARD_W or blockX < 0 or blockY >= self.BOARD_H):# ボード外に出ていないか
                    return False
                if self.board[blockY][blockX] == 1:#盤面に既にブロックがあるか
                    return False
        return True
    
    def canDrop(self)->bool:
        #1マスしたに移動可能か？
        return self.canSet(self.mino.x,self.mino.y+1,self.mino.rotateNum)

    def drop(self):
        self.mino.drop()

    def tryDrop(self):
        if self.canDrop():
            self.drop()
            return True
        else:
            return False

    def canRotate(self,rotateNum)->bool:
        #回転可能か？ canSet利用
        return self.canSet(self.mino.x,self.mino.y,self.mino.rotateNum)
        
    def canMoveRight(self)->bool:
        #1マス右に移動可能か？
        return self.canSet(self.mino.x+1,self.mino.y,self.mino.rotateNum)
    
    def tryMoveRight(self):
        if self.canMoveRight():
            self.mino.moveRight()
            return True
        return False

    def tryRotateRight(self):
        if self.canMoveRight():
            self.mino.rotateRight()
            return True
        return False
    def tryRotateLeft(self):
        if self.canMoveLeft():
            self.mino.rotateLeft()
            return True
        return False
    
    def canMoveLeft(self)->bool:
        #1マス左に移動可能か？
        return self.canSet(self.mino.x-1,self.mino.y,self.mino.rotateNum)

    def tryMoveLeft(self):
        if self.canMoveLeft():
            self.mino.moveLeft()
            return True
        return False

    def putMino(self):
        #盤面にミノを設置(canSetは通過している前提)
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
                    self.board[blockY][blockX] = block

    def loadMino(self):
        #dropMinoNumをインクリメント,落下ミノを更新(必要があればreloadNext)
        self.dropMinoNum += 1
        if self.dropMinoNum >= 7:
            print("call reload")
            self.reloadNext()
        self.mino = self.nexts[self.dropMinoNum]

    def reloadNext(self):
        #前半7つを削除、新しく7つを付け足す、dropMinoNumを0に(リセット)
        del self.nexts[:7]
        self.nexts.extend(random.sample(self.allMinos,self.NUM_MINO))
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
        else:
            pass
            #警告文「ホールドできません」を表示

    def hardDrop(self):
        #ミノを一気に下に落下させる
        y = self.mino.y
        while self.canSet(self.mino.x,y+1,self.mino.rotateNum):
            y += 1
        self.mino.moveDown(y)
        self.putMino()

    def calcScore(self) -> int:
        check = np.count_nonzero(self.board != 0) #０以外の要素を数える
        result = check / 2 
        #スコアを計算する
        return result
"""
class MoveMino():
    def __init__(self,model):
        self.board = model.board
        self.mino = model.mino
        self.model = model
    
    def canSet(self,mino,x,y,rotate)->bool:
        #設置可能か？(盤外に出ない、既にあるブロックと重ならない)
        for i,minoRow in enumerate(self.mino.shapes[rotate]):
            blockY = y+i
            for j,block in enumerate(minoRow):
                if block == 0:#ブロックが空白の時は無視
                    continue
                blockX = x+j
                if blockY < 0:
                    continue

                if (blockX >= self.model.BOARD_W or blockX < 0 or blockY >= self.model.BOARD_H):# ボード外に出ていないか
                    return False
                if self.board[blockY][blockX] == 1:#盤面に既にブロックがあるか
                    return False
        return True
    
    def canDrop(self,mino)->bool:
        #1マスしたに移動可能か？
        #mino = self.model.mino
        return self.canSet(mino,self.mino.x,self.mino.y+1,self.mino.rotateNum)

    def drop(self):
        self.mino.drop()

    def tryDrop(self,mino):
        #ドロップ可能ならドロップ、Trueを返す
        if self.canDrop(mino):
            self.mino.drop()
            return True
        return False

    def hardDrop(self):
        #ミノを一気に下に落下させる
        #mino = self.model.mino
        y = self.mino.y
        while self.canSet(self.mino.x,y-1,self.mino.rotate):
            y -= 1
        self.mino.moveDown(y)
        self.model.putMino()


    def canRotate(self,rotateNum)->bool:
        #回転可能か？ canSet利用
        #mino = self.model.mino
        return self.canSet(self.mino.x,self.mino.y,self.mino.rotateNum)
    
    def tryRotateRight(self):
        #可能なら右回転
        rotateNum = (self.mino.rotateNum+1)%4
        if canRotate(self.mino,rotateNum):
            self.mino.rotateRight()
            return True
        return False
    
    def tryRotateLeft(self):
        #可能なら左回転
        rotateNum = (self.mino.rotateNum-1)%4
        if canRotate(self.mino,rotateNum):
            self.mino.rotateLeft()
            return True
        return False

    def canMoveRight(self)->bool:
        #1マス右に移動可能か？
        return self.canSet(mino.x+1,mino.y,mino.rotateNum)
    
    def tryMoveRight(self):
        #可能なら右に移動
        if canMoveRight():
            mino.moveRight()
            return True
        return False
    
    def canMoveLeft(self)->bool:
        #1マス左に移動可能か？
        return self.canSet(mino.x-1,mino.y,mino.rotateNum)

    def tryMoveLeft(self):
        #可能なら左に移動
        if canMoveLeft():
            mino.moveLeft()
            return True
        return False
"""