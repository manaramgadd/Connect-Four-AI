from connect4helpers import *
import graphviz  # doctest: +NO_EXE
#import doctest
#import unittest.mock
#import pylab
# import PySide6.QtSvg
#import PySide6.QtCore
from PyQt6 import QtGui, QtSvg, QtCore,QtWebEngineWidgets,QtWidgets
import os
import sys
from PyQt5.QtWidgets import QApplication
import QtDesigner
import pydot

import random
import string



class minimax:
    #create a transposition table
    # transposition_table = {}
    #minimax algorithm with decision returned
    # max value 
    app = QtWidgets.QApplication(sys.argv)
    def max_value(board, depth):
        if depth == 0 or board.mask.count(1) > 41:
            board.heuristic()
            return (board, board.utility)
        max_child=None
        max_utility = float('-inf')
        board.child()
        for child in board.children:
            child_utility = minimax.min_value(child, depth-1)[1]
            child.utility = child_utility
            if child_utility > max_utility:
                max_child = child
                max_utility = child_utility
        max_child.utility=max_utility
        
        return (max_child, max_child.utility)
    
    def min_value(board, depth):
        if depth == 0 or board.mask.count(1) > 41:
            board.heuristic()
            return (board, board.utility)
        min_child=None
        min_utility = float('inf')
        board.child()
        for child in board.children:
            child_utility = minimax.max_value(child, depth-1)[1]
            child.utility = child_utility
            if child_utility < min_utility:
                min_child = child
                min_utility = child_utility
        min_child.utility=min_utility
        return (min_child, min_child.utility)

    # minimax with pruning
    def max_value_pruning(board, depth, alpha, beta):
        if depth == 0 or board.mask.count(1) > 41:
            board.heuristic()
            return (board, board.utility)
        max_child=None
        max_utility = float('-inf')
        board.child()
        board.alpha=alpha
        board.beta=beta
        i=0
        for child in board.children:
            if(child.depth!=0):
                child.alpha=board.alpha
                child.beta=board.beta
            child_utility = minimax.min_value_pruning(child, depth-1, alpha, beta)[1]
            child.utility = child_utility
            if child_utility > max_utility:
                max_child = child
                max_utility = child_utility
                alpha=max(alpha,max_utility)
            board.alpha = max(alpha, max_utility)
            if max_utility >= beta:
                for i in range(i+1,len(board.children)):
                    board.children[i].pruned=True
                #print("PRUNED IN MAX!!!!!!!!")
                break
            i+=1
        return (max_child, max_child.utility)
    
    def min_value_pruning(board, depth, alpha, beta):
        if depth == 0 or board.mask.count(1) >41:
            board.heuristic()
            return (board, board.utility)
        min_child=None
        min_utility = float('inf')
        board.child()
        i=0
        board.alpha=alpha
        board.beta=beta
        for child in board.children:
            child.alpha=board.alpha
            child.beta=board.beta
            child_utility = minimax.max_value_pruning(child, depth-1, alpha, beta)[1]
            child.utility = child_utility
            if child_utility < min_utility:
                min_child = child
                min_utility = child_utility
                beta = min(beta, min_utility)
            board.beta = min(beta, min_utility)
            if min_utility <= alpha:
                #print("PRUNED IN MIN!!!!!!!!")
                #print(board)
                for i in range(i+1,len(board.children)):
                    board.children[i].pruned=True
                break  
            i+=1          
        return (min_child, min_child.utility)
    
    def minimax_decision(board,print):
        (child, utility) = minimax.max_value(board, board.depth)
        board.utility = utility
        if print:
            dot = graphviz.Digraph(comment='MINMAX TREE')
            #make dot shape a square and prevent all edges from overlapping
            dot.attr('node', shape='square')
            #make dot size a 10
            dot.attr(size='500')
            #overlapping = False
            dot.overlap = 'false'
            boardstr=''.join(random.choices(string.ascii_lowercase, k=12))
            print_max = minimax.print_minmax(board,boardstr,dot)
            (graph,) = pydot.graph_from_dot_data(print_max.source)
            graph.write_pdf('minimax.pdf')
            # print_max.save('minmax_tree.gv')
            #display pdf in qt and allow zooming
            view=QtWebEngineWidgets.QWebEngineView()
            settings = view.settings()
            settings.setAttribute(view.settings().WebAttribute.PluginsEnabled, True)
            view.load(QtCore.QUrl.fromLocalFile(os.path.abspath('minimax.pdf')))
            #view.load(QtCore.QUrl.fromLocalFile("F:\College\Term7\Artificial Intelligence\mariem ai\minimax.pdf"))
            #resize the window to full screen
            view.setZoomFactor(500)
            view.resize(800,600)
            view.show()
            minimax.app.exec()
        return child
        #print_max.render('minmax_tree.gv')
        #print_max.view()
        # (graph,) = pydot.graph_from_dot_data(print_max.source)
        # # use graphviz.unflatten to make the graph more readable
        # graph = graphviz.unflatten(print_max.source)        
        # #construct a QApplication
        



        return child
        
    def minimax_decision_pruning(board,print):
        (child, utility) = minimax.max_value_pruning(board, board.depth, float('-inf'), float('inf'))
        board.utility = utility
        if print:
            dot = graphviz.Digraph(comment='MINIMAX TREE WITH PRUNING')
            #make dot shape a square and prevent all edges from overlapping
            dot.attr('node', shape='square')
            #make dot size a 10
            dot.attr(size='500')
            #overlapping = False
            dot.overlap = 'false'
            boardstr=''.join(random.choices(string.ascii_lowercase, k=12))
            print_max = minimax.print_minmax_pruning(board,boardstr,dot)
            #print_max.save('minmax_tree_pruning.gv')
            #print_max.render('minmax_tree.gv')
            (graph,) = pydot.graph_from_dot_data(print_max.source)
            graph.write_pdf('minimax_pruning.pdf')
            
            #display pdf in qt and allow zooming
            view=QtWebEngineWidgets.QWebEngineView()
            settings = view.settings()
            settings.setAttribute(view.settings().WebAttribute.PluginsEnabled, True)
            view.load(QtCore.QUrl.fromLocalFile(os.path.abspath('minimax_pruning.pdf')))
            # view.load(QtCore.QUrl.fromLocalFile("F:\College\Term7\Artificial Intelligence\mariem ai\minimax_pruning.pdf"))
            #resize the window to full screen
            view.setZoomFactor(500)
            view.resize(800,600)
            view.show()
            minimax.app.exec()
            #print_max.view()
        # # (graph,) = pydot.graph_from_dot_data(print_max.source)
        # # # use graphviz.unflatten to make the graph more readable
        # # graph = graphviz.unflatten(print_max.source)        
        # # #construct a QApplication
        # # app = QtWidgets.QApplication(sys.argv)
        # # #display pdf in qt and allow zooming
        # # view=QtWebEngineWidgets.QWebEngineView()
        # # settings = view.settings()
        # # settings.setAttribute(view.settings().WebAttribute.PluginsEnabled, True)
        # # view.load(QtCore.QUrl.fromLocalFile("F:\College\Term7\Artificial Intelligence\Lab2-int\minmax_tree.gv.pdf"))
        # # #resize the window to full screen
        # # view.setZoomFactor(500)
        # # view.resize(800,600)
        # # view.show()


        # # sys.exit(app.exec())

        return child

    def print_minmax(board,parentstr,dot):
        # generate unique string for each node
        #dot.node(parentstr, str(board.utility)+"\n"+board.tostring())
        dot.node(parentstr, str(board.utility))
        for child in board.children:
            childstr=''.join(random.choices(string.ascii_lowercase, k=12))
            dot.edge(parentstr, childstr)
            minimax.print_minmax(child,childstr,dot)
        return dot
    
    def print_minmax_pruning(board,parentstr,dot):        
        # generate unique string for each node
        # if(board.pruned==True):
        #     dot.node(parentstr, str(board.utility)+"\\n"+board.tostring() +"\\n"+"PRUNED")
        # elif(board.depth!=0):
        #     dot.node(parentstr, str(board.utility)+"\\n"+board.tostring() +"\\n"+"alpha: "+str(board.alpha)+"\\n"+"beta: "+str(board.beta))
        # elif(board.depth==0):
        #     dot.node(parentstr, str(board.utility)+"\\n"+board.tostring())

        if(board.pruned==True):
            dot.node(parentstr,"PRUNED")
        elif(board.depth!=0):
            dot.node(parentstr, str(board.utility)+"\\n" +"alpha: "+str(board.alpha)+"\\n"+"beta: "+str(board.beta))
        elif(board.depth==0):
            dot.node(parentstr, str(board.utility)+"\\n")
       
        for child in board.children:
            childstr=''.join(random.choices(string.ascii_lowercase, k=12))
            dot.edge(parentstr, childstr)
            minimax.print_minmax_pruning(child,childstr,dot)
        return dot