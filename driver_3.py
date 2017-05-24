
#"""
#Created on Mon May 15 12:46:56 2017
#
#@author: FraDepa
#"""


from sys import argv
import time
import collections
from heapq import heappush, heappop

print("START")
#get start time
start_time = time.clock()

ACTION = []

#dictionary with index element of goal node

dictGN = {}
dictGN.update({0:[0,0]})
dictGN.update({1:[0,1]})
dictGN.update({2:[0,2]})
dictGN.update({3:[1,0]})
dictGN.update({4:[1,1]})
dictGN.update({5:[1,2]})
dictGN.update({6:[2,0]})
dictGN.update({7:[2,1]})
dictGN.update({8:[2,2]})


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

#Open output.txt file
f = open('output.txt', 'a')

#BFS
LIFO = False
if algorithm == "dfs":
    LIFO = True


#get array of elements
puzzleList =  [int(x) for x in puzzleString.split(',')]


def memory():

   import sys
   if sys.platform == "win32":
       import psutil
#       ps = format(psutil.Process().memory_info().rss, '.8f')
       return str(psutil.Process().memory_info().rss)
   else:
       # Note: if you execute Python from cygwin,
       # the sys.platform is "cygwin"
       # the grading system's sys.platform is "linux2"
       import resource
       print("resource", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
       
       return str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)



class Node(object):

    parentNode = None
    childs = ()
    f = 0

    def __init__(self, parentNode, board, action, depth):
        self.parentNode = parentNode
        self.board = board
        self.action = action
        self.depth = depth
        
        if algorithm == "ast":
            man = self.getHn(self.board)
            self.f = depth + man
    
    def __eq__(self, othr):
        return self.board == othr.board

    def __hash__(self):
        return hash((self.board))
    
    def __lt__(self, other):
        
        if self.f < other.f:
            return self.f < other.f
        else:
            if self.action == "Up":  #Io sono UP  ---> return Io(UP)
                return self
            elif other.action == "Up":
                return other
            elif self.action == "Down" and (other.action == "Left" or other.action == "Right"):
                return self
            elif self.action == "Left" and other.action == "Right":
                return self
   
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
            

            n = Node(self, upBoard, "Up", self.depth + 1)
            listNode.append(n)

        if indexEmptySpace + 3 <= 8: #can moveDown

            downBoard = list(self.board)
            value = downBoard[indexEmptySpace + 3]
            downBoard[indexEmptySpace] = value
            downBoard[indexEmptySpace + 3] = 0



            n = Node(self, downBoard, "Down", self.depth + 1)
                
            listNode.append(n)


        if indexEmptySpace != 0 and indexEmptySpace != 3 and indexEmptySpace != 6: #cam moveLeft

            leftBoard = list(self.board)
            value = leftBoard[indexEmptySpace - 1]
            leftBoard[indexEmptySpace] = value
            leftBoard[indexEmptySpace - 1] = 0


            n = Node(self, leftBoard, "Left", self.depth + 1)
                
            listNode.append(n)

        if indexEmptySpace != 2 and indexEmptySpace != 5 and indexEmptySpace != 8: #can moveRight

            rightBoard = self.board
            value = rightBoard[indexEmptySpace + 1]
            rightBoard[indexEmptySpace] = value
            rightBoard[indexEmptySpace + 1] = 0


            n = Node(self, rightBoard, "Right", self.depth + 1)
                
            listNode.append(n)

        t = tuple(listNode)
        self.childs = self.childs + t

    def getParentStory(self,search_depth):
        
        ACTION.append(self.action)
        for i in range(search_depth-1):
            
            ACTION.append(self.parentNode.action)
            self = self.parentNode
        
#        if self.parentNode is None:
#            return -2
#        elif self.parentNode.action == "":
#            ACTION.append(self.action)
#            return -1
#        else:
#            ACTION.append(self.action)
#            return self.parentNode.getParentStory()
        

    def getHn(self, elements):
        
#        print()
#        print("MANHATTAN")
        manhattanDist = 0
        
        r = 0
        c = 0
        for i,n in enumerate(elements):
            
            if i == 3 or i == 6:
                c = 0
            elif i > 2:
                r = 1
            elif i > 5:
                r = 2
               
            if n != 0:
                
                if n != i:
#                    print()
#                    print("n: " + str(n))
                    
                    
                    coord = dictGN.get(n)
                   
#                    print("coord: " + str(coord[0]) + str(coord[1]))
#                    print("r: " + str(r) + " c: " + str(c))
                    
                    #calculate distance
                    dist = abs(coord[0] - r) + abs(coord[1] - c)
#                    print("dist: " + str(dist))
                    
                    manhattanDist += dist
                    
            c += 1
            
#        print("manhattan")
#        print(manhattanDist)
#        print()
        return manhattanDist


#create initial Node
initialNode = Node(None, puzzleList, "", 0)

print(algorithm)

if algorithm == "ast":
    frontier = []
    heappush(frontier, (initialNode.f, initialNode))

    it = 0
    explored = set()
    maxF = 0
    while len(frontier) > 0:

        print("------------------")
        print(it)

        t = heappop(frontier)
        currentNode = t[1]   
#    print("currentNode")
#    print(currentNode.board)
#    print("f: " + str(currentNode.f))
#    print()

        explored.add(str(currentNode.board))

        if str(currentNode.board) == str(goalList):
            print("Goal State Found!")

            currentNode.getParentStory(currentNode.depth)

            print("path_to_goal")
            ACTION.reverse()
            print(ACTION)
            f.write("path_to_goal: " + str(ACTION) + "\n")

            print("cost_of_path")
            print(len(ACTION))
            f.write("cost_of_path: " + str(len(ACTION)) + "\n")

            print("nodes_expanded")
            print(it)
            f.write("nodes_expanded: " + str(it) + "\n")

            print("search_depth")
            print(currentNode.depth)
            f.write("search_depth: " + str(currentNode.depth) + "\n")

            print("max_search_depth")
            print(maxF)
            f.write("max_search_depth: " + str(maxF) + "\n")

            print("running_time")
            t = time.clock() - start_time
            tFormat = format(t, '.8f')
            print(tFormat)
            f.write("running_time: " + str(tFormat) + "\n")

            print("max_ram_usage")
            f.write("max_ram_usage: " + memory())
            
            f.close()
        
            break

        currentNode.calculateChilds()
        
        if len(currentNode.childs) > 0:  
            for c in currentNode.childs:

                #check if the child State is not in the explored
                present = str(c.board) in explored
                if present == False:  #has not been explored
                
                
                    index = 0
                    present = False
                    print("frontier size: " + str(len(frontier)))
                    for ff in frontier:
                        if ff[1].board == c.board:
                            present = True
                            print(present)
                            if c.f < ff[1].f:
                                ff[1].f = c.f
                                frontier[index] = (ff[1].f, ff[1])
                            break
                        index += 1
                    if present == False:
                        if c.depth > maxF:
                            maxF = c.depth
                        heappush(frontier,(c.f, c))
               
#                    present = c.board in [x[1].board for x in frontier]
#                    if present == False:
#                        if c.depth > maxF:
#                            maxF = c.depth
#                        heappush(frontier,(c.f, c))
                        
        it += 1

else:
    

    print("ALGHORITM BFS/DFS: "  + str(algorithm))
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
            
            currentNode[1].getParentStory(currentNode[1].depth)

            print("path_to_goal")
            ACTION.reverse()
            print(ACTION)
            f.write("path_to_goal: " + str(ACTION) + "\n")

            print("cost_of_path")
            print(len(ACTION))
            f.write("cost_of_path: " + str(len(ACTION)) + "\n")

            print("nodes_expanded")
            print(it)
            f.write("nodes_expanded: " + str(it) + "\n")

            print("search_depth")
            print(currentNode[1].depth)
            f.write("search_depth: " + str(currentNode[1].depth) + "\n")

            print("max_search_depth")
            print(maxF)
            f.write("max_search_depth: " + str(maxF) + "\n")

            print("running_time")
            t = time.clock() - start_time
            tFormat = format(t, '.8f')
            print(tFormat)
            f.write("running_time: " + str(tFormat) + "\n")

            print("max_ram_usage")
            f.write("max_ram_usage: " + memory())
            
            f.close()
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
#                            frontier.append(c)
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


















