# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:25:44 2017

@author: csto935
"""



class State(object):
    
    childs = []
    
    depth = -1
    
    
    def __init__(self, board):
        self.board = board
        
        return
    
    def __repr__(self):
        return "State(%s)" % (self.board)
    
    def __eq__(self, other):
        if isinstance(other, State):
            return ((self.board == other.board))
        else:
            return False
        
    def __hash__(self):
        return hash(self.__repr__())
    
    def calculateNeighbours(self):
        
        #try to move the empty tile
        self.board.moveEmptyTile(self)
        
        
        
#        if boards is not None:
#            print(boards)
#            for i,b in enumerate(boards):
#                print("i: " + str(i) + " b: " + str(b) + "\n")
#        else:
#            print("Cannot moveUp")
        
        
        
#    def __eq__(self, other):
#        return self.nodes == other.nodes
#    def __lt__(self, other):
#        return self.nodes < other.nodes
#    def __gt__(self,other):
#        return self.nodes > other.nodes
    
    

