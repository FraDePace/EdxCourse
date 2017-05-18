## -*- coding: utf-8 -*-
#"""
#Created on Mon May 15 12:46:56 2017
#
#@author: FraDepa
#"""
#
import queue
import heapq
from sys import argv
from state import State
from board import Board
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
#heap = []
#data = [2,19,45,3,89,1]
#
#print("Heap:")
#
#for d in data:
#    print("Add %d" % d)
#    heapq.heappush(heap, d)
#    
#print()
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
#
#    
#

#class Prova(object):
#    
#    def __init__(self, name):
#        self.name = name
#        return
#    def __repr__(self):
#        return "Prova(%s)" % (self.name)
#    def __eq__(self, other):
#        if isinstance(other, Prova):
#            return ((self.name == other.name))
#        else:
#            return False
#    def __hash__(self):
#        return hash(self.__repr__())
#        
#
#
#a = set()
#a.add(Prova("Marco"))
#a.add(Prova("Piero"))
#a.add(Prova("Gianna"))
#
#print(len(a))
#
#p = Prova("Piero")
#p1 = Prova("Alessandro")
#
#print(p in a)
#print(p1 in a)





#print(s2 in a)
#print(s3 in a)
#print()

#frontier = queue.Queue()
#
#l = []
#for i in range(3):  #0,1,2
#    l.append(i)
#    
#s = State(l) #State(0,1,2)
#
#r = []
#r.append(1)
#r.append(2)
#r.append(7)
#
#s1 = State(r) #State(1,2,7)
#
#
#frontier.put(s)
#frontier.put(s1)
#
##################################à
#s2 = State(r) #State(1,2,7)
#
#w = []
#w.append(4)
#w.append(9) #State(4,9)
#
#s3 = State(w)
#
#print("f")
#
#
#
#
#while not frontier.empty():
#    ff = frontier.get()
#    print("ff: " + str(ff))
#    print("s2: " + str(s2))
#    print("s3: " + str(s3))
#    if s2 == ff:
#        print("s2 == ff")
#    else:
#        print("s2 != ff")
#        
#    if s3 == ff:
#        print("s3 == ff")
#    else:
#        print("s3 != ff")
#    print()
#    
#    print(frontier.qsize())
#    
#   
#print()
#print("Array")
#array = []
#
#for i in range(7):
#    array.append(i)
#    
#for a in array:
#    print(a)
#    
#print()
#    
#
#array.reverse()
#a1 = array.pop()
#
#print("a1:" + str(a1))
#
#print()
#for a in array:
#    print(a)
#    
#
#array.append(a1)
#array.reverse()
#print()
#for a in array:
#    print(a)
#    
#print()
#
#array.append(7)
#for a in array:
#    print(a)
#
#array.reverse()
#print()
#print(array.pop())

#puzzleS = argv[2]
#puzzleL =  [int(x) for x in puzzleS.split(',')]
#
#stat1 = State(puzzleL)
#
#
#
#stat2 = State(puzzleL)
#
#if stat1 == stat2:
#    print("stat1 == stat2")
#else:
#    print("stat1 != stat2")
#
#
#for i in range(3):
#    stat1.childs.append(i)
#
#for i in range(7):
#    stat2.childs.append(i)
#
#print(stat1.childs)
#
#if stat1 == stat2:
#    print("stat1 == stat2")
#else:
#    print("stat1 != stat2")




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
    
goalBoard = Board(goalList)
goalState = State(goalBoard)

#BFS

if algorithm == "bfs":
    #get array of elements
    puzzleList =  [int(x) for x in puzzleString.split(',')]
    
    #create initial Board
    initialBoard = Board(puzzleList);
    
    #create initial State
    print("Initial State")
    
    initialState = State(initialBoard)
    initialState.depth = 0
    
  
    
    #create frontier ----> queue FIFO
    #frontier = queue.Queue()
    frontier = []
    

    #create explored Set
    explored = set()
    print()
    print("create explored set: " + str(explored))
    
    #add initial state to the frontier
    #frontier.put(initialState)
    frontier.append(initialState)
    
    while len(frontier)>0:
        frontier.reverse()
        #currentState = frontier.get()
        currentState = frontier.pop()
        explored.add(currentState)
        
        #check if it is the Goal State
        if currentState.board == goalState.board:
            print("Goal State Found!")
            print("depth: " + str(currentState.depth))
            break
        
        currentState.calculateNeighbours()
        
        frontier.reverse()
        
        if len(currentState.childs) > 0:
            for c in currentState.childs:
                
                #check if is not equal with cirrent state
                if c != currentState:
                     #check if the child State is not in the explored
                     present = c in explored
                     if present == False:  #has not been explored
                         front = list(frontier)
                         
                         if len(front) > 0:
                             found = False
                             for f in front:
                                 if f.board == c.board:
                                     found = True
                                     break
                             if found == False:
                                 frontier.append(c)
                         else:
                             frontier.append(c)
                
#for i in range(2):
#    print("-------------------------------------------")
#    frontier.reverse()
#        #currentState = frontier.get()
#    currentState = frontier.pop()
#   
#    explored.add(currentState)
#        
#        #check if it is the Goal State
#    if currentState.board == goalState.board:
#        print("Goal State Found!")
#        
#          
#    currentState.calculateNeighbours()
#    
#    
#    frontier.reverse()
#              
#    
#    
#    
#    if len(currentState.childs) > 0:
#        for c in currentState.childs:
#                
#                
#            if c != currentState:
#                
#                    
#                present = c in explored
#                
#                if present == False:  #has not been explored
#                    front = list(frontier)
#                    print(len(front))
#                    if len(front) > 0:
#                        found = False
#                        for f in front:
#                            if f.board == c.board:
#                                found = True
#                                break
#                        if found == False:
#                            
#                            frontier.append(c)
#                    else:
#                        frontier.append(c)
#                        
#                   
#    print("frontier AFTER")                
#    for f in frontier:
#        print(str(f.board))
#    print()
#    print("explored AFTER")
#    for e in explored:
#        print(str(e.board))
#    print()
    
               
                        
                    
                    
    
    
    
    
    
    
    
    
    
    

