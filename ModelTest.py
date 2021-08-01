import unittest
import numpy as np
from Model import Score
import random
import Const
class ModelDriver:
    def __init__(self) -> None:
        self.TRAP = 10
        self.BOARD_H = 20
        self.BOARD_W = 10
        self.board = np.zeros([self.BOARD_H,self.BOARD_W],dtype=int)
        self.initTraps()

    def initTraps(self):
        #全ての列にトラップマスを用意する
        traps = list(range(10))
        random.shuffle(traps)
        for i in range(int(Const.BOARD_H/2)): #二行ごとに一つのトラップマスを用意する
            self.board[i*2,traps[i]] = -1

class PerfectScoreTest(unittest.TestCase):
    def test_Model(self):
        md = ModelDriver()
        self.board = md.board
        for i in range(Const.BOARD_H):
            if i%2 != 0:
                for j in range(Const.BOARD_W-1):
                    self.board[i,j] = 1
            else:
                for j in range(Const.BOARD_W):
                    if self.board[i,j] != -1:
                        self.board[i,j] = 1
        print(self.board)
        expected = 100.0
        actual = Score.calcScore(self.board)
        self.assertEqual(expected,actual)

if __name__ == "__main__":
    unittest.main()