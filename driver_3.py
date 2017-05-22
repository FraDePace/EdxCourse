## -*- coding: utf-8 -*-
#"""
#Created on Mon May 15 12:46:56 2017
#
#@author: FraDepa
#"""
#

from sys import argv
from collections import deque
import time
import collections



#get start time
start_time = time.time()

ACTION = []

def memory():

   import sys
   if sys.platform == "win32":
       import psutil
       print("psutil", psutil.Process().memory_info().rss)
   else:
       # Note: if you execute Python from cygwin,
       # the sys.platform is "cygwin"
       # the grading system's sys.platform is "linux2"
       import resource
       print("resource", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
       



class Node(object):

    parentNode = None
    childs = ()

    def __init__(self, parentNode, board, action, depth):
        self.parentNode = parentNode
        self.board = board
        self.action = action
        self.depth = depth
    
    def __eq__(self, othr):
        return self.board == othr.board

    def __hash__(self):
        return hash((self.board))
   
    def calculateChilds(self):

        for i,b in enumerate(self.board):
            if b == 0:
                indexEmptySpace = i
                break

        listNode = []

        if indexEmptySpace - 3 >= 0:  #can moveUp

            upBoard = list(self.board)
            value = upBoard[indexEmptySpace - 3]
            upBoard[indexEmptySpace] = value
            upBoard[indexEmptySpace - 3] = 0

            n = Node(self, upBoard, "UP", self.depth + 1)
            listNode.append(n)

        if indexEmptySpace + 3 <= 8: #can moveDown

            downBoard = list(self.board)
            value = downBoard[indexEmptySpace + 3]
            downBoard[indexEmptySpace] = value
            downBoard[indexEmptySpace + 3] = 0


            n = Node(self, downBoard, "DOWN", self.depth + 1)
            listNode.append(n)


        if indexEmptySpace != 0 and indexEmptySpace != 3 and indexEmptySpace != 6: #cam moveLeft

            leftBoard = list(self.board)
            value = leftBoard[indexEmptySpace - 1]
            leftBoard[indexEmptySpace] = value
            leftBoard[indexEmptySpace - 1] = 0


            n = Node(self, leftBoard, "LEFT", self.depth + 1)
            listNode.append(n)

        if indexEmptySpace != 2 and indexEmptySpace != 5 and indexEmptySpace != 8: #can moveRight

            rightBoard = self.board
            value = rightBoard[indexEmptySpace + 1]
            rightBoard[indexEmptySpace] = value
            rightBoard[indexEmptySpace + 1] = 0


            n = Node(self, rightBoard, "RIGHT", self.depth + 1)
            listNode.append(n)

        t = tuple(listNode)
        self.childs = self.childs + t

    def getParentStory(self):
        if self.parentNode is None:
            return -2
        if self.parentNode.action == "":
            ACTION.append(self.action)
            return -1
        else:
            ACTION.append(self.action)
            return self.parentNode.getParentStory()




if len(argv) != 3:
    print("Error number of elements in the command line!")


print("Program Name: " + argv[0])

algorithm = argv[1]
print("algorithm: "  + algorithm)

puzzleString = argv[2]
print("puzzleString: " + puzzleString)
print()

goalList = []
for i in range(9):
    goalList.append(i)

print("goalList")
print(goalList)
print()


#print("Prova OrderedDict")
#
#a = []
#for i in range(3):
#    a.append(i)  
#n1 = Node(None, a, "", 0)
#
#
#b = []
#b.append(3)
#b.append(4)
#b.append(5)
#n2 = Node(n1, b, "UP", 1)
#
#
#d = collections.OrderedDict()
#
#d.update({str(n1.board): n1})
#d.update({str(n2.board): n2})
#
#for k,v in d.items():
#    print(k)
#    print(v)
#    
#print()
#present = str(n2.board) in d
#print(present)
#
#print("popitem")
##nItem = d.popitem(False)  #get a tuple with FIFO
#nItem = d.popitem(True)  #LIFO
#print(nItem[0])
#print()
#for k,v in d.items():
#    print(k)
#    print(v)

#while len(d) > 0:
#   nItem = d.popitem(False)
#
#print("len dict")
#print(len(d))
#Open output.txt file
f = open('output.txt', 'a')

#BFS
LIFO = False
if algorithm == "dfs":
    LIFO = True


#get array of elements
puzzleList =  [int(x) for x in puzzleString.split(',')]

#create initial Node
initialNode = Node(None, puzzleList, "", 0)

print(algorithm)

#    #create frontier ----> double-ended queue
#    frontier = deque()
frontier = collections.OrderedDict()

    #create explored Set
explored = set()
print()
print("create explored set: " + str(explored))

#    #add initial state to the frontier
#    frontier.append(initialNode)
frontier.update({str(initialNode.board):initialNode})
maxF = 0

it = 0
#    while len(frontier) > 0:
while len(frontier) > 0:

    print("------------------")
    print(it)
#        currentNode = frontier.popleft()
    currentNode = frontier.popitem(LIFO)   #tuple
#        explored.add(str(currentNode.board))
    explored.add(currentNode[0])


        #check if it is the Goal State
#        if currentNode.board == goalList:
    if currentNode[0] == str(goalList):
        print("Goal State Found!")

#            currentNode.getParentStory()
        if LIFO == False:
            currentNode[1].getParentStory()

            print("ACTION")
            ACTION.reverse()
            print(ACTION)

        print("cost_of_path")
        print(len(ACTION))

        print("nodes_expanded")
        print(it)

        print("search_depth")
#            print(currentNode.depth)
        print(currentNode[1].depth)

        print("max_search_depth")
        print(maxF)

        print("runnin_time")
        print(time.time() - start_time)

        print("max_ram_usage")
        memory()
        break

    currentNode[1].calculateChilds()
        
    if len(currentNode[1].childs) > 0:  #bfs
#            for c in currentNode.childs:
        if LIFO == False:
            for c in currentNode[1].childs:

                #check if the child State is not in the explored
                present = str(c.board) in explored
                if present == False:  #has not been explored
                    present = str(c.board) in frontier.keys()
                    if present == False:
                        if c.depth > maxF:
                            maxF = c.depth
#                        frontier.append(c)
                    frontier.update({str(c.board):c})
        else:                                                 #dfs
            for c in currentNode[1].childs[::-1]:
                
                present = str(c.board) in explored
                if present == False:  #has not been explored
                    present = str(c.board) in frontier.keys()
                    if present == False:
                        if c.depth > maxF:
                            maxF = c.depth
#                        frontier.append(c)
                    frontier.update({str(c.board):c})
    it += 1


##DFS
#
#elif algorithm == "dfs":
#    #get array of elements
#    puzzleList =  [int(x) for x in puzzleString.split(',')]
#
#    #create initial Board
##    initialBoard = Board(puzzleList);
#
#    initialNode = Node(None, puzzleList, "", 0)
#
#    print(algorithm)
#
#    #create initial State
##    print("Initial State")
#
##    initialState = State(None, initialBoard, "", 0)
##
##    #create frontier ----> queue FIFO
##    #frontier = queue.Queue()
##
##    #create frontier ----> double-ended queue
#    frontier = deque()
##
#    #create explored Set
#    explored = set()
#    print()
#    print("create explored set: " + str(explored))
##
##
##    #add initial state to the frontier
#    frontier.append(initialNode)
#
#    maxF = 0
#
#    it = 0
#   
#    while len(frontier) > 0:
##    for i in range(1):
#        print("------------------")
#        currentNode = frontier.pop()
#
#        explored.add(str(currentNode.board))
#
#
#
#       # check if it is the Goal State
#        if currentNode.board == goalList:
#            print("Goal State Found!")
#            print(currentNode.board)
#            print("it")
#            print(it)
#            print()
##            print("frontier")
##            for f in frontier:
##                print(f.board)
##            print()
##            currentNode.getParentStory()
##
##            print("ACTION")
##            ACTION.reverse()
##            print(ACTION)
#
#            print("cost_of_path")
#            print(len(ACTION))
#
#            print("nodes_expanded")
#            print(it)
#
#            print("search_depth")
#            print(currentNode.depth)
#
#            print("max_search_depth")
#            print(maxF)
#
#            print("running_time")
#            print(time.time() - start_time)
#
#            print("max_ram_usage")
#            memory()
#            break
#
#        currentNode.calculateChilds()
#
#        
#        if len(currentNode.childs) > 0:
#            for c in currentNode.childs[::-1]:
#                
#                if c.board == goalList:
#                    print("Goal state found at it: " + str(it))
#                    presentE = str(c.board) in explored
#                    presentF = c in frontier
#                    print(str(presentE) + " " + str(presentF))
#
#                presentE = str(c.board) in explored
#                presentF = c in frontier
#                
#                if presentE == False and presentF == False: 
#                    
##                    if c.board == goalList:
##                        print("Goal state added")
##                        print("it goal state: " + str(it))
#                    if c.depth > maxF:
#                        maxF = c.depth
#                    frontier.append(c)
#                    print(len(frontier))
#                    
#        
#      
#                
#        it += 1

















