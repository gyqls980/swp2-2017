import pickle
import sys
from PyQt5.QtWidgets import (QMainWindow,QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,QGridLayout,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.sortkey = ''
        self.name = ''
        self.age = ''
        self.score = ''
        self.amount = 0
        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.ResultEdit = QTextEdit()
        self.keySet = QComboBox()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.writeScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        name = QLabel('Name:')
        age = QLabel('Age:')
        score = QLabel('Score:')
        amount = QLabel('Amount:')
        key = QLabel('Key:')
        result = QLabel('Result')
        self.ResultEdit.setReadOnly(True)
        self.keySet.addItems(['Name','Age','Score'])
        grid = QGridLayout()
        grid.setSpacing(0)
        grid.addWidget(name,1,0)
        grid.addWidget(self.nameEdit,1,1)
        grid.addWidget(age,1,2)
        grid.addWidget(self.ageEdit,1,3)
        grid.addWidget(score,1,4)
        grid.addWidget(self.scoreEdit,1,5)
        grid.addWidget(amount,2,2)
        grid.addWidget(self.amountEdit,2,3)
        grid.addWidget(key,2,4)
        grid.addWidget(self.keySet,2,5)
        btn1 = QPushButton("Add", self)
        grid.addWidget(btn1,3,0)
        btn2 = QPushButton("Del", self)
        grid.addWidget(btn2,3,1)
        btn3 = QPushButton("Find", self)
        grid.addWidget(btn3,3,2)
        btn4 = QPushButton("Inc", self)
        grid.addWidget(btn4,3,3)
        btn5 = QPushButton("Show", self)
        grid.addWidget(btn5,3,4)
        grid.addWidget(result,4,0)
        grid.addWidget(self.ResultEdit,5,0,5,5)
        btn1.clicked.connect(self.Add)
        btn2.clicked.connect(self.Del)
        btn3.clicked.connect(self.Find)
        btn4.clicked.connect(self.Inc)
        btn5.clicked.connect(self.Show)
        self.ResultEdit.toPlainText()
        self.setLayout(grid)
        self.show()
    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
            pass
        else:
            fH.close()



    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def Add(self):
        self.name = self.nameEdit.text()
        self.age = self.ageEdit.text()
        self.score = self.scoreEdit.text()
        record = {'Name':self.name, 'Age':self.age, 'Score':self.score}
        self.scoredb += [record]
        self.Show()


    def Del(self):
        k = list(range(len(self.scoredb)))
        k.sort(reverse = True)
        self.name = self.nameEdit.text()
        for i in k:
            for j in range(3):
                if self.scoredb[i]['Name']== self.name:
                    del(self.scoredb[i])
                    break
        self.Show()


    def Find(self):
        self.name = self.nameEdit.text()
        for i in range(len(self.scoredb)):
            if self.scoredb[i]['Name'] == self.name:
                self.ResultEdit.setText('Age' + ' = ' + str(self.scoredb[i]['Age']) + '    ' + 'Name' + ' = ' + self.scoredb[i]['Name'] + '    ' + 'Score' + ' = ' + str(self.scoredb[i]['Score']) + "\n")
        self.Show()


    def Inc(self):
        self.name = self.nameEdit.text()
        self.amount = int(self.amountEdit.text())
        for i in range(len(self.scoredb)):
            for j in range(3):
                if self.scoredb[i]['Name'] == self.name:
                    self.scoredb[i]['Score'] = int(self.scoredb[i]['Score']) + int(self.amount)
                    break
        self.Show()


    def Show(self):
        scdb = ''
        self.sortkey = str(self.keySet.currentText())
        for p in self.scoredb :
            for dat in p :
                p[dat] = str(p[dat])
        for p in sorted(self.scoredb, key = lambda person : person[self.sortkey]):
            for attr in sorted(p):
                scdb += str(attr) + " = " + str(p[attr]) + "    "
            scdb += '\n'
        self.ResultEdit.setText(scdb)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
