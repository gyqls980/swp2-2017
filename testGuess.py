 import unittest

from guess import *
from hangman import *


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('twosomeplace')
        self.h1 = Hangman()

    def tearDown(self):
        pass


    def testDisplayCurrent(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ _ _ _ e _ _ _ _ e ')
        self.g1.guess('c')
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ _ _ _ e _ _ _ c e ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), 't _ _ _ _ _ e _ _ _ c e ')
        self.g1.guess('o')
        self.assertEqual(self.g1.displayCurrent(), 't _ o _ o _ e _ _ _ c e ')

    def testDisplayGuessed1(self):
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

    def testFinish(self):
        self.g1.secretWord = 'twosomeplace'
        self.g1.currentStatus = 'twosomeplace'
        self.assertTrue(self.g1.finished())

    def testShapeOfHangman(self):
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(), self.h1.text[5])
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(), self.h1.text[4])
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(), self.h1.text[3])

if __name__ == '__main__':
    unittest.main()
