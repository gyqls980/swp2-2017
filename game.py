# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from hangman import Hangman
from guess import Guess
from word import Word


class HangmanGame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


        self.word = Word('words.txt')

        #Hangman 상태 표시
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        # 왼쪽 정렬 (그래야 올바르게 보임)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        #고정 폭(fixed-with) 글꼴을 이용.
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # hangmanLayout을 만들고 그 안에 위젯을 배치.
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)
        self.showRemainingLife = QLineEdit()
        self.showRemainingLife.setReadOnly(True)
        #status Layout 만들기.
        statusLayout = QGridLayout()

        #currentWord-사용자가 입력한 단어가 맞는지 표시
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)#읽기 전용.사용자가 편집불가.
        self.currentWord.setAlignment(Qt.AlignCenter)#가운데 정렬.
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)#글꼴 크기.
        self.currentWord.setFont(font)
        # statusLayout에 위젯 배치.
        # (0,0,1,2)는 0행 0열 가로 1 세로 2
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        #guessedChars-사용자가 입력한 단어들 표시.
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        # statusLayout에 위젯 배치.
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        #message-상태를 알려주는 메세지를 보임.
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        # statusLayout에 위젯 배치.
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        #charInput-사용자가 단어를 입력할 칸.
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0) #3행 0열

        #guessButton-사용자가 단어를 입력하고 누를 버튼.
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        # statusLayout에 위젯 배치.
        statusLayout.addWidget(self.guessButton, 3, 1) #3행 1열

        # newGameButton-새로운 게임을 다시 시작하기 위해 누를 버튼.
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)
        statusLayout.addWidget(self.showRemainingLife, 4, 1)
        #mainLayout을 만들고 위에서 구성한 두 레이아웃을 가로로 배치.
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle('Hangman Game')


        self.startGame()

    def startGame(self):
        self.hangman = Hangman()
        self.guess = Guess(self.word.randFromDB(9))
        print(self.guess.secretWord)
        self.gameOver = False
        self.charInput.setReadOnly(False)
        self.hangmanWindow.setText(self.hangman.currentShape())
        #self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())
        self.message.clear()

    def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()

        if self.gameOver == True:
            self.message.setText("Game Over")

        if len(guessedChar) != 1:
            self.message.setText("Input wrong word")

        if guessedChar in self.guess.guessedChars:
            self.message.setText("Already used")


        success = self.guess.guess(guessedChar)
        if success == False:
            self.hangman.decreaseLife()
            self.hangmanWindow.setText(self.hangman.currentShape())
            self.currentWord.setText(self.guess.displayCurrent())
            self.guessedChars.setText(self.guess.displayGuessed())
            self.message.setText("No " + guessedChar + " in the word")
            self.showRemainingLife.setText("try : " + str(self.hangman.remainingLives))
        elif success == True:
            self.currentWord.setText(self.guess.displayCurrent())
            self.guessedChars.setText(self.guess.displayGuessed())
            self.message.setText(guessedChar + " is in the word!")
            self.showRemainingLife.setText("try : " + str(self.hangman.remainingLives))

        elif success == "alpha":
            self.message.setText("Input wrong value")

        if self.guess.finished():
            self.message.setText("Success!")
            self.gameOver = True
            self.charInput.setReadOnly(True)
            self.hangman.RemainingLives = 6

        if self.hangman.getRemainingLives() == 0:
            self.message.setText("Fail! " + self.guess.secretWord)
            self.gameOver = True
            self.charInput.setReadOnly(True)
            self.hangman.RemainingLives = 6



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())
