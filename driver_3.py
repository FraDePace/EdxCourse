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

#
#def hello():
#    print("Hello World")
#
#hello()
#print()
#
##FIFO queue 
#q = queue.Queue()
#
#for i in range(7):
#    q.put(i)
#    
#print("Queue FIFO:")
#
#while not q.empty():
#    print(q.get())
#
#print()
#    
##LIFO queue 
#q = queue.LifoQueue()
#
#for i in range(7):
#    q.put(i)
#    
#print("Queue LIFO:")
#
#while not q.empty():
#    print(q.get())
#    
#print()
#    
##Priority queue
#q = queue.PriorityQueue()
#
#q.put(State(4))
#q.put(State(7))
#q.put(State(2))
#q.put(State(7))
#q.put(State(19))
#
#print("Queue Priority:")
#
#
#while not q.empty():
#    next_state = q.get()
#    print(next_state.nodes)
#
#print()
#
##Heap
#

#
#for i in range(len(data)):
#    smallest = heapq.heappop(heap)
#    print('pop    {:>3}:'.format(smallest))
#    
#script, first, second, third = sys.argv
#print("The script is called:", script)
#print("Your first variable is:", first)
#print("Your second variable is:", second)
#print("Your third variable is:", third)

#q = deque(range(5))
#print(q)
#print()
#
#q.append(5)
#print(q)
#print()
#
#q.appendleft(-1)
#print(q)
#print()
#
#a = q.pop()
#print("pop: " + str(a))
#print(q)
#print()
#
#c = q.popleft()
#print("pop left: " + str(c))
#print(q)
#print()
#
#b = 1
#present = b in q
#print(present)
#
#b = -1
#present = b in q
#print(present)

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
        
        if self.parentNode.action == "":
            ACTION.append(self.action)
            return -1
        else:
            ACTION.append(self.action)
            return self.parentNode.getParentStory()
        
#       print(self.action) 
#        
#       parent = self.parentNode
#       print(parent.action)
#       
#       pparent = parent.parentNode
#       print(pparent.action)
#       
#       if pparent.parentNode.action == "":
#           print(-1)
        
        
        
        




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
    
#goalBoard = Board(goalList)
#goalState = State(None, goalBoard, "", 0)   #State(parent, board, action, depth)


#Open output.txt file
f = open('output.txt', 'a')



#BFS

if algorithm == "bfs":
    #get array of elements
    puzzleList =  [int(x) for x in puzzleString.split(',')]
    
    #create initial Board
#    initialBoard = Board(puzzleList);

    initialNode = Node(None, puzzleList, "", 0)
    
    print(algorithm)
    
    #create initial State
#    print("Initial State")

#    initialState = State(None, initialBoard, "", 0)
#
#    #create frontier ----> queue FIFO
#    #frontier = queue.Queue()
#    
#    #create frontier ----> double-ended queue
    frontier = deque()
#    
    #create explored Set
    explored = set()
    print()
    print("create explored set: " + str(explored))
#    
#    
#    #add initial state to the frontier
    frontier.append(initialNode)
    
    maxF = 0
    
#    
    while len(frontier) > 0:
#    for i in range(1):
        print("------------------")
        currentNode = frontier.popleft()
        
        explored.add(str(currentNode.board))
        
        
        
        #check if it is the Goal State
        if currentNode.board == goalList:
            print("Goal State Found!")
            
            currentNode.getParentStory()
            
            print("ACTION")
            ACTION.reverse()
            print(ACTION)
            
            print("cost_of_path")
            print(len(ACTION))
            
            print("nodes_expanded")
            print(len(frontier) -1)
            
            print("search_depth")
            print(currentNode.depth)
            
            print("max_search_depth")
            print(maxF)
            
            print("runnin_time")
            print(time.time() - start_time)
            
            print("max_ram_usage")
            memory()
            break

        currentNode.calculateChilds()
#
        if len(currentNode.childs) > 0:
            for c in currentNode.childs:

                #check if the child State is not in the explored
                present = str(c.board) in explored
                if present == False:  #has not been explored
                    present = c in frontier
                    if present == False:
                        if c.depth > maxF:
                            maxF = c.depth
                        frontier.append(c)
                    
                
                        
                

                        
                    
                    
    
    
    
    
    
    
    
    
    
    

