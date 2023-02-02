from connect4helpers import *
from minimax import *
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
if __name__ == '__main__':
    print("main")
    #Gboard = GameBoard('100000 0 000000 0 000000 0 000000 0 000000 0 000000  0 011111 0000000000000000','100000 0 000000 0 000000 0 000000 0 000000 0 000000 0 111111 0000000000000000', 0, 0, 0, 0, 0, 4, -1)
    Gboard = GameBoard('000000 0 000000 0 000000 0 000000 0 000000 0 000000 0  000000 0000000000000000','000000 0 000000 0 000000 0 000000 0 000000 0 000000 0  000000 0000000000000000', 0, 0, 0, 0, 1, 5, -1)

    print(Gboard)

    Gboard.make_move(0)
    print(Gboard)
    Gboard.make_move(3)
    print(Gboard)
    Gboard.make_move(3)
    print(Gboard)
    Gboard.make_move(5)
    Gboard.make_move(4)
    Gboard.make_move(3)
    Gboard.make_move(2)
    Gboard.make_move(2)
    Gboard.make_move(7)
    Gboard.make_move(6)
    Gboard.make_move(2)
    Gboard.make_move(2)
    Gboard.make_move(4)
    Gboard.make_move(3)
    Gboard.make_move(3)
    Gboard.make_move(3)
    Gboard.make_move(5)
    Gboard.make_move(4)
    Gboard.make_move(3)
    Gboard.make_move(2)
    Gboard.make_move(2)
    Gboard.make_move(7)
    Gboard.make_move(6)
    Gboard.make_move(2)
    Gboard.make_move(1)
    Gboard.make_move(1)
    Gboard.make_move(1)
    Gboard.make_move(1)
    Gboard.make_move(1)
    # Gboard.make_move(1)
    # Gboard.make_move(0)
    # Gboard.make_move(0)
    # Gboard.make_move(0)
    # Gboard.make_move(0)
    # Gboard.make_move(0)
    # Gboard.make_move(5)
    # Gboard.make_move(5)
    # Gboard.make_move(5)
    # Gboard.make_move(5)
    # Gboard.make_move(5)
    # Gboard.make_move(5)
    # Gboard.make_move(6)
    # Gboard.make_move(6)
    # Gboard.make_move(4)


    print(Gboard)

    # Gboard.win_detect()
    # Gboard.connected_threes()
    # print(Gboard.score_r)

    # print('Children')
    # Gboard.child()
    # for i in Gboard.children:
    #     print(i)

    #call minimax
    #loop over minimax 7 times and show the result
    minimax_node=minimax()
    print(minimax.minimax_decision_pruning(Gboard,True))
    #print tree
    
    