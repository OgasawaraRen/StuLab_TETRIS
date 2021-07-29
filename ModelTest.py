import unittest
class Model:
    def __init__(self) -> None:
        self.board = np.zeros([20,10])
        self.TRAP = 10
        self.BOARD_W = 10

    def checkGameOver(self)->bool:#3 ゲームオーバーだったらfalse,#ゲームオーバーか？
        self.board = np.zeros([20,10])
        def checkGameOver(self)->bool:#3 ゲームオーバーだったらfalse,#ゲームオーバーか？
        check = np.count_nonzero(self.board != -1) #-1の数を数える
        if check != self.TRAP:   
            return False

        for row in self.board:
            if np.sum(row) == self.BOARD_W:
                return False

        return True


class ModelTest(unittest.TestCase):
    def test_Model(self):
        a = np.arange(200).reshape((20,10))
        clear_board = a[0:,0:1] = 1
        expected = "True"
        actual = Model.checkGameOver(clear_board)
        self.assertEqual(expected,actual)
class ModelTest2(unittest.TestCase):
    def test_Model(self):
        miss_board = np.zeros((20,10))
        expected = "False"
        actual = Model.checkGameOver(miss_board)
        self.assertEqual(expected,actual)

class ModelTest3(unittest.TestCase):
    def test_Model(self):
        
        self.assertEqual(expected,actual)

if __name__ == "__main__":
    unittest.main()