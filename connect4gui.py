import connect4helpers
from gui import *
from PyQt5.Qt import *
from minimax import *
import time
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from gui import Ui_MainWindow
from main import *
from connect4helpers import *


class connect4(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.Gboard = GameBoard('000000 0 000000 0 000000 0 000000 0 000000 0 000000 0  000000 0000000000000000',
                                '000000 0 000000 0 000000 0 000000 0 000000 0 000000 0  000000 0000000000000000', 0, 0,
                                0, 0, 1, 4, -1)
        self.graph=False
        self.maxDepth = self.Gboard.depth
        self.minimax_or_pruning = False
        # self.gui.pushButton_4.clicked.connect(self.connect4_board)
        # self.gui.start.clicked.connect(lambda: self.opponent_turn(self.Gboard))
        self.gui.minimax.clicked.connect(lambda: self.minimax())
        self.gui.pruning.clicked.connect(lambda: self.pruning())
        QtWidgets.QApplication.processEvents()
        #self.comp_turn(self.Gboard)
    def minimax(self):
        self.minimax_or_pruning = True
        self.gui.pB0.clicked.connect(lambda: self.change_col0())
        self.gui.pB1.clicked.connect(lambda: self.change_col0())
        self.gui.pB2.clicked.connect(lambda: self.change_col0())
        self.gui.pB3.clicked.connect(lambda: self.change_col0())
        self.gui.pB4.clicked.connect(lambda: self.change_col0())
        self.gui.pB5.clicked.connect(lambda: self.change_col0())
        self.gui.pB7.clicked.connect(lambda: self.change_col1())
        self.gui.pB8.clicked.connect(lambda: self.change_col1())
        self.gui.pB9.clicked.connect(lambda: self.change_col1())
        self.gui.pB10.clicked.connect(lambda: self.change_col1())
        self.gui.pB11.clicked.connect(lambda: self.change_col1())
        self.gui.pB12.clicked.connect(lambda: self.change_col1())
        self.gui.pB14.clicked.connect(lambda: self.change_col2())
        self.gui.pB15.clicked.connect(lambda: self.change_col2())
        self.gui.pB16.clicked.connect(lambda: self.change_col2())
        self.gui.pB17.clicked.connect(lambda: self.change_col2())
        self.gui.pB18.clicked.connect(lambda: self.change_col2())
        self.gui.pB19.clicked.connect(lambda: self.change_col2())
        self.gui.pB21.clicked.connect(lambda: self.change_col3())
        self.gui.pB22.clicked.connect(lambda: self.change_col3())
        self.gui.pB23.clicked.connect(lambda: self.change_col3())
        self.gui.pB24.clicked.connect(lambda: self.change_col3())
        self.gui.pB25.clicked.connect(lambda: self.change_col3())
        self.gui.pB26.clicked.connect(lambda: self.change_col3())
        self.gui.pB28.clicked.connect(lambda: self.change_col4())
        self.gui.pB29.clicked.connect(lambda: self.change_col4())
        self.gui.pB30.clicked.connect(lambda: self.change_col4())
        self.gui.pB31.clicked.connect(lambda: self.change_col4())
        self.gui.pB32.clicked.connect(lambda: self.change_col4())
        self.gui.pB33.clicked.connect(lambda: self.change_col4())
        self.gui.pB35.clicked.connect(lambda: self.change_col5())
        self.gui.pB36.clicked.connect(lambda: self.change_col5())
        self.gui.pB37.clicked.connect(lambda: self.change_col5())
        self.gui.pB38.clicked.connect(lambda: self.change_col5())
        self.gui.pB39.clicked.connect(lambda: self.change_col5())
        self.gui.pB40.clicked.connect(lambda: self.change_col5())
        self.gui.pB42.clicked.connect(lambda: self.change_col6())
        self.gui.pB43.clicked.connect(lambda: self.change_col6())
        self.gui.pB44.clicked.connect(lambda: self.change_col6())
        self.gui.pB45.clicked.connect(lambda: self.change_col6())
        self.gui.pB46.clicked.connect(lambda: self.change_col6())
        self.gui.pB47.clicked.connect(lambda: self.change_col6())
        self.gui.minimax.disconnect()
        self.gui.pruning.disconnect()
        if(self.Gboard.turn == 1):
            self.comp_turn(self.Gboard)

    def pruning(self):
        self.minimax_or_pruning = False
        self.gui.pB0.clicked.connect(lambda: self.change_col0())
        self.gui.pB1.clicked.connect(lambda: self.change_col0())
        self.gui.pB2.clicked.connect(lambda: self.change_col0())
        self.gui.pB3.clicked.connect(lambda: self.change_col0())
        self.gui.pB4.clicked.connect(lambda: self.change_col0())
        self.gui.pB5.clicked.connect(lambda: self.change_col0())
        self.gui.pB7.clicked.connect(lambda: self.change_col1())
        self.gui.pB8.clicked.connect(lambda: self.change_col1())
        self.gui.pB9.clicked.connect(lambda: self.change_col1())
        self.gui.pB10.clicked.connect(lambda: self.change_col1())
        self.gui.pB11.clicked.connect(lambda: self.change_col1())
        self.gui.pB12.clicked.connect(lambda: self.change_col1())
        self.gui.pB14.clicked.connect(lambda: self.change_col2())
        self.gui.pB15.clicked.connect(lambda: self.change_col2())
        self.gui.pB16.clicked.connect(lambda: self.change_col2())
        self.gui.pB17.clicked.connect(lambda: self.change_col2())
        self.gui.pB18.clicked.connect(lambda: self.change_col2())
        self.gui.pB19.clicked.connect(lambda: self.change_col2())
        self.gui.pB21.clicked.connect(lambda: self.change_col3())
        self.gui.pB22.clicked.connect(lambda: self.change_col3())
        self.gui.pB23.clicked.connect(lambda: self.change_col3())
        self.gui.pB24.clicked.connect(lambda: self.change_col3())
        self.gui.pB25.clicked.connect(lambda: self.change_col3())
        self.gui.pB26.clicked.connect(lambda: self.change_col3())
        self.gui.pB28.clicked.connect(lambda: self.change_col4())
        self.gui.pB29.clicked.connect(lambda: self.change_col4())
        self.gui.pB30.clicked.connect(lambda: self.change_col4())
        self.gui.pB31.clicked.connect(lambda: self.change_col4())
        self.gui.pB32.clicked.connect(lambda: self.change_col4())
        self.gui.pB33.clicked.connect(lambda: self.change_col4())
        self.gui.pB35.clicked.connect(lambda: self.change_col5())
        self.gui.pB36.clicked.connect(lambda: self.change_col5())
        self.gui.pB37.clicked.connect(lambda: self.change_col5())
        self.gui.pB38.clicked.connect(lambda: self.change_col5())
        self.gui.pB39.clicked.connect(lambda: self.change_col5())
        self.gui.pB40.clicked.connect(lambda: self.change_col5())
        self.gui.pB42.clicked.connect(lambda: self.change_col6())
        self.gui.pB43.clicked.connect(lambda: self.change_col6())
        self.gui.pB44.clicked.connect(lambda: self.change_col6())
        self.gui.pB45.clicked.connect(lambda: self.change_col6())
        self.gui.pB46.clicked.connect(lambda: self.change_col6())
        self.gui.pB47.clicked.connect(lambda: self.change_col6())
        self.gui.minimax.disconnect()
        self.gui.pruning.disconnect()
        if(self.Gboard.turn == 1):
            begin = time.time()
            self.comp_turn(self.Gboard)
            end = time.time()


        
    def change_col0(self):
        self.Gboard.make_move(0)
        pos = self.Gboard.pos
        # switch case for all 6 positions
        if pos == 0:
            self.gui.pB0.setStyleSheet("border-radius : 25; \n"
                                       "border : 2px solid black;\n"
                                       "border-color: rgb(108, 108, 108);\n"
                                       "background-color: yellow;\n"
                                       "")
            self.gui.pB0.setText(" ")
        elif pos == 1:
            self.gui.pB1.setStyleSheet("border-radius : 25; \n"
                                       "border : 2px solid black;\n"
                                       "border-color: rgb(108, 108, 108);\n"
                                       "background-color: yellow;\n"
                                       "")
            self.gui.pB1.setText(" ")

        elif pos == 2:
            self.gui.pB2.setStyleSheet("border-radius : 25; \n"
                                       "border : 2px solid black;\n"
                                       "border-color: rgb(108, 108, 108);\n"
                                       "background-color: yellow;\n"
                                       "")
            self.gui.pB2.setText(" ")

        elif pos == 3:
            self.gui.pB3.setStyleSheet("border-radius : 25; \n"
                                       "border : 2px solid black;\n"
                                       "border-color: rgb(108, 108, 108);\n"
                                       "background-color: yellow;\n"
                                       "")
            self.gui.pB3.setText(" ")
        elif pos == 4:
            self.gui.pB4.setStyleSheet("border-radius : 25; \n"
                                       "border : 2px solid black;\n"
                                       "border-color: rgb(108, 108, 108);\n"
                                       "background-color: yellow;\n"
                                       "")
            self.gui.pB4.setText(" ")
        elif pos == 5:
            self.gui.pB5.setStyleSheet("border-radius : 25; \n"
                                       "border : 2px solid black;\n"
                                       "border-color: rgb(108, 108, 108);\n"
                                       "background-color: yellow;\n"
                                       "")
            self.gui.pB5.setText(" ")
        print(self.Gboard)
        QtWidgets.QApplication.processEvents()
        if self.Gboard.pos!= -1:
            self.comp_turn(self.Gboard)

    def change_col1(self):
        self.Gboard.make_move(1)
        pos = self.Gboard.pos
        # switch case for all 6 positions
        if pos == 7:
            self.gui.pB7.setStyleSheet("border-radius : 25; \n"
                                       "border : 2px solid black;\n"
                                       "border-color: rgb(108, 108, 108);\n"
                                       "background-color: yellow;\n"
                                       "")
            self.gui.pB7.setText(" ")
        elif pos == 8:
            self.gui.pB8.setStyleSheet("border-radius : 25; \n"
                                       "border : 2px solid black;\n"
                                       "border-color: rgb(108, 108, 108);\n"
                                       "background-color: yellow;\n"
                                       "")
            self.gui.pB8.setText(" ")
        elif pos == 9:
            self.gui.pB9.setStyleSheet("border-radius : 25; \n"
                                       "border : 2px solid black;\n"
                                       "border-color: rgb(108, 108, 108);\n"
                                       "background-color: yellow;\n"
                                       "")
            self.gui.pB9.setText(" ")
        elif pos == 10:
            self.gui.pB10.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB10.setText(" ")
        elif pos == 11:
            self.gui.pB11.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB11.setText(" ")
        elif pos == 12:
            self.gui.pB12.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB12.setText(" ")
        print(self.Gboard)
        QtWidgets.QApplication.processEvents()
        if self.Gboard.pos!= -1:
            self.comp_turn(self.Gboard)

    def change_col2(self):
        self.Gboard.make_move(2)
        pos = self.Gboard.pos
        # switch case for all 6 positions
        if pos == 14:
            self.gui.pB14.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB14.setText(" ")
        elif pos == 15:
            self.gui.pB15.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB15.setText(" ")
        elif pos == 16:
            self.gui.pB16.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB16.setText(" ")
        elif pos == 17:
            self.gui.pB17.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB17.setText(" ")
        elif pos == 18:
            self.gui.pB18.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB18.setText(" ")
        elif pos == 19:
            self.gui.pB19.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB19.setText(" ")
        print(self.Gboard)
        QtWidgets.QApplication.processEvents()
        if self.Gboard.pos!= -1:
            self.comp_turn(self.Gboard)

    def change_col3(self):
        self.Gboard.make_move(3)
        pos = self.Gboard.pos
        # switch case for all 6 positions
        if pos == 21:
            self.gui.pB21.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB21.setText(" ")
        elif pos == 22:
            self.gui.pB22.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB22.setText(" ")
        elif pos == 23:
            self.gui.pB23.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB23.setText(" ")
        elif pos == 24:
            self.gui.pB24.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB24.setText(" ")
        elif pos == 25:
            self.gui.pB25.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB25.setText(" ")
        elif pos == 26:
            self.gui.pB26.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB26.setText(" ")

        print(self.Gboard)
        QtWidgets.QApplication.processEvents()
        if self.Gboard.pos!= -1:
            self.comp_turn(self.Gboard)

    def change_col4(self):
        self.Gboard.make_move(4)
        pos = self.Gboard.pos
        # switch case for all 6 positions
        if pos == 28:
            self.gui.pB28.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB28.setText(" ")
        elif pos == 29:
            self.gui.pB29.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB29.setText(" ")
        elif pos == 30:
            self.gui.pB30.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB30.setText(" ")
        elif pos == 31:
            self.gui.pB31.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB31.setText(" ")
        elif pos == 32:
            self.gui.pB32.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB32.setText(" ")
        elif pos == 33:
            self.gui.pB33.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB33.setText(" ")
        print(self.Gboard)
        QtWidgets.QApplication.processEvents()
        if self.Gboard.pos!= -1:
            self.comp_turn(self.Gboard)

    def change_col5(self):
        self.Gboard.make_move(5)
        pos = self.Gboard.pos
        # switch case for all 6 positions
        if pos == 35:
            self.gui.pB35.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB35.setText(" ")
        elif pos == 36:
            self.gui.pB36.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB36.setText(" ")
        elif pos == 37:
            self.gui.pB37.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB37.setText(" ")
        elif pos == 38:
            self.gui.pB38.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB38.setText(" ")
        elif pos == 39:
            self.gui.pB39.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB39.setText(" ")
        elif pos == 40:
            self.gui.pB40.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB40.setText(" ")
        print(self.Gboard)
        QtWidgets.QApplication.processEvents()
        if self.Gboard.pos!= -1:
            self.comp_turn(self.Gboard)

    def change_col6(self):
        self.Gboard.make_move(6)
        pos = self.Gboard.pos
        # switch case for all 6 positions
        if pos == 42:
            self.gui.pB42.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB42.setText(" ")
        elif pos == 43:
            self.gui.pB43.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB43.setText(" ")
        elif pos == 44:
            self.gui.pB44.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB44.setText(" ")
        elif pos == 45:
            self.gui.pB45.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB45.setText(" ")
        elif pos == 46:
            self.gui.pB46.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB46.setText(" ")
        elif pos == 47:
            self.gui.pB47.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: yellow;\n"
                                        "")
            self.gui.pB47.setText(" ")
        print(self.Gboard)
        QtWidgets.QApplication.processEvents()
        if self.Gboard.pos!=-1:
            self.comp_turn(self.Gboard)

    def comp_turn(self, Gboard):
        if self.gui.graphcheck.isChecked():
            self.graph=True
        else:
            self.graph=False
        if self.Gboard.mask.count(1)==42:
            self.Gboard.win_detect()
            # create a qt widget to display the winner
            self.gui.msgBox = qtw.QMessageBox()
            self.gui.msgBox.setIcon(qtw.QMessageBox.Information)
            if self.Gboard.score_r>self.Gboard.score_y:
                self.gui.msgBox.setText("AI wins")
            else:
                self.gui.msgBox.setText("Human wins")
            scorestr ="AI: "+str(self.Gboard.score_r)+"  Human: "+str(self.Gboard.score_y)
            self.gui.msgBox.setText("Game Over")
            self.gui.msgBox.setInformativeText(scorestr)
            self.gui.msgBox.setWindowTitle("Game Over")
            self.gui.msgBox.setStandardButtons(qtw.QMessageBox.Ok)
            self.gui.msgBox.show()
        else:
            if(self.minimax_or_pruning == 1):
                begin = time.time()
                self.Gboard = minimax.minimax_decision(self.Gboard, self.graph)
                end = time.time()
                print("Time taken by minimax: ", end-begin)
            else:
                begin = time.time()
                self.Gboard = minimax.minimax_decision_pruning(self.Gboard, self.graph)
                end = time.time()
                print("Time taken by minimax with pruning: ", end-begin)
            self.Gboard.depth = self.maxDepth
            print(self.Gboard)
            pos = self.Gboard.pos
            if pos == 0:
                self.gui.pB0.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: red;\n"
                                        "")
                self.gui.pB0.setText(" ")
            elif pos == 1:
                self.gui.pB1.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: red;\n"
                                        "")
                self.gui.pB1.setText(" ")

            elif pos == 2:
                self.gui.pB2.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: red;\n"
                                        "")
                self.gui.pB2.setText(" ")

            elif pos == 3:
                self.gui.pB3.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: red;\n"
                                        "")
                self.gui.pB3.setText(" ")
            elif pos == 4:
                self.gui.pB4.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: red;\n"
                                        "")
                self.gui.pB4.setText(" ")
            elif pos == 5:
                self.gui.pB5.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: red;\n"
                                        "")
                self.gui.pB5.setText(" ")
            elif pos == 7:
                self.gui.pB7.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: red;\n"
                                        "")
                self.gui.pB7.setText(" ")
            elif pos == 8:
                self.gui.pB8.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: red;\n"
                                        "")
                self.gui.pB8.setText(" ")
            elif pos == 9:
                self.gui.pB9.setStyleSheet("border-radius : 25; \n"
                                        "border : 2px solid black;\n"
                                        "border-color: rgb(108, 108, 108);\n"
                                        "background-color: red;\n"
                                        "")
                self.gui.pB9.setText(" ")
            elif pos == 10:
                self.gui.pB10.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB10.setText(" ")
            elif pos == 11:
                self.gui.pB11.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB11.setText(" ")
            elif pos == 12:
                self.gui.pB12.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")

                self.gui.pB12.setText(" ")
            elif pos == 14:
                self.gui.pB14.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB14.setText(" ")
            elif pos == 15:
                self.gui.pB15.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB15.setText(" ")
            elif pos == 16:
                self.gui.pB16.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB16.setText(" ")
            elif pos == 17:
                self.gui.pB17.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB17.setText(" ")
            elif pos == 18:
                self.gui.pB18.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB18.setText(" ")
            elif pos == 19:
                self.gui.pB19.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB19.setText(" ")
            elif pos == 21:
                self.gui.pB21.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB21.setText(" ")
            elif pos == 22:
                self.gui.pB22.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB22.setText(" ")
            elif pos == 23:
                self.gui.pB23.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB23.setText(" ")
            elif pos == 24:
                self.gui.pB24.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB24.setText(" ")
            elif pos == 25:
                self.gui.pB25.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB25.setText(" ")
            elif pos == 26:
                self.gui.pB26.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB26.setText(" ")
            elif pos == 28:
                self.gui.pB28.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB28.setText(" ")
            elif pos == 29:
                self.gui.pB29.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB29.setText(" ")
            elif pos == 30:
                self.gui.pB30.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB30.setText(" ")
            elif pos == 31:
                self.gui.pB31.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB31.setText(" ")
            elif pos == 32:
                self.gui.pB32.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")

                self.gui.pB32.setText(" ")
            elif pos == 33:
                self.gui.pB33.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB33.setText(" ")

            elif pos == 35:
                self.gui.pB35.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB35.setText(" ")
            elif pos == 36:
                self.gui.pB36.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB36.setText(" ")
            elif pos == 37:
                self.gui.pB37.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")

                self.gui.pB37.setText(" ")
            elif pos == 38:
                self.gui.pB38.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB38.setText(" ")
            elif pos == 39:
                self.gui.pB39.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB39.setText(" ")
            elif pos == 40:
                self.gui.pB40.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB40.setText(" ")
            elif pos == 42:
                self.gui.pB42.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB42.setText(" ")
            elif pos == 43:
                self.gui.pB43.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB43.setText(" ")
            elif pos == 44:
                self.gui.pB44.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB44.setText(" ")
            elif pos == 45:
                self.gui.pB45.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB45.setText(" ")
            elif pos == 46:
                self.gui.pB46.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB46.setText(" ")
            elif pos == 47:
                self.gui.pB47.setStyleSheet("border-radius : 25; \n"
                                            "border : 2px solid black;\n"
                                            "border-color: rgb(108, 108, 108);\n"
                                            "background-color: red;\n"
                                            "")
                self.gui.pB47.setText(" ")
        self.Gboard.win_detect()
        QtWidgets.QApplication.processEvents()
        # change text color
        self.gui.Score.setStyleSheet("color: rgb(255, 255, 255);\n")
        self.gui.Score.setText("Human: "+str(self.Gboard.score_y)+" : "+"AI: "+str(self.Gboard.score_r))
        QtWidgets.QApplication.processEvents()


if __name__ == "__main__":
    import sys

    board_gui = qtw.QApplication(sys.argv)
    gui = connect4()
    gui.show()
    sys.exit(board_gui.exec())
