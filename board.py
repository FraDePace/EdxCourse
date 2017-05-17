# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:25:24 2017

@author: csto935
"""
from state import State

class Board(object):
    
    def __init__(self, board):
        self.board = board
#        for i,b in enumerate(self.board):
#             print("i: " + str(i) + " b: " + str(b) + "\n")           
        return
    
    def moveEmptyTile(self, st): #move empty tile
        indexEmptySpace = 0
        
        upBoard = []
        downBoard = []
        leftBoard = []
        rightBoard = []

        for i,b in enumerate(self.board):
            if b == 0:
                indexEmptySpace = i
                break
        
        print("index empty space: " + str(indexEmptySpace))
        print()
            
        if indexEmptySpace - 3 >= 0:  #can moveUp
            print("UP")
            print()
            upBoard = list(self.board)
            value = upBoard[indexEmptySpace - 3]
            upBoard[indexEmptySpace] = value
            upBoard[indexEmptySpace - 3] = 0
            
            b = Board(upBoard)
            s = State(b)
            st.childs.append(s)
         
        if indexEmptySpace + 3 <= 8: #can moveDown
            print("DOWN")
            print()
            downBoard = list(self.board)
            value = downBoard[indexEmptySpace + 3]
            downBoard[indexEmptySpace] = value
            downBoard[indexEmptySpace + 3] = 0
                
            b = Board(downBoard)
            
            st.childs.append(State(b))
       
        
        if indexEmptySpace != 0 and indexEmptySpace != 3 and indexEmptySpace != 6: #cam moveLeft
            print("LEFT")
            print()
            leftBoard = list(self.board)
            value = leftBoard[indexEmptySpace - 1]
            leftBoard[indexEmptySpace] = value
            leftBoard[indexEmptySpace - 1] = 0
                 
            b = Board(leftBoard)
            
            st.childs.append(State(b))
                 
            
        
            
        if indexEmptySpace != 2 and indexEmptySpace != 5 and indexEmptySpace != 8: #can moveRight
            print("RIGHT")
            print()
            rightBoard = self.board
            value = rightBoard[indexEmptySpace + 1]
            rightBoard[indexEmptySpace] = value
            rightBoard[indexEmptySpace + 1] = 0
                 
            b = Board(rightBoard)
            
            st.childs.append(State(b))
            
          