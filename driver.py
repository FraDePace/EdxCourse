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

#BFS

if algorithm == "bfs":
    #get array of elements
    puzzleList =  [int(x) for x in puzzleString.split(',')]
    
    #create initial Board
    initialBoard = Board(puzzleList);
    
    #create initial State
    initialState = State(initialBoard)
    
    #create frontier ----> queue FIFO
    frontier = queue.Queue()
    
    #create explored Set
    explored = set()
    print()
    print("create explored set: " + str(explored))
    
    #add initial state to the frontier
    frontier.put(initialState)
    
    while not frontier.empty():
        currentState = frontier.get()
        explored.add(currentState)
        
        #check if it is the Goal State
        if currentState.board == goalList:
            print("Goal State Found!")
            break
        
        currentState.calculateNeighbours()
        
        if len(currentState.childs) > 0:
            for c in currentState.childs:
                print("board: " + str(c.board))
    
    
    
    
    
    
    
    
    
    

