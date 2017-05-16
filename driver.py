# -*- coding: utf-8 -*-
"""
Created on Mon May 15 12:46:56 2017

@author: FraDepa
"""

import queue
import heapq
from state import State

def hello():
    print("Hello World")

hello()
print()

#FIFO queue 
q = queue.Queue()

for i in range(7):
    q.put(i)
    
print("Queue FIFO:")

while not q.empty():
    print(q.get())

print()
    
#LIFO queue 
q = queue.LifoQueue()

for i in range(7):
    q.put(i)
    
print("Queue LIFO:")

while not q.empty():
    print(q.get())
    
print()
    
#Priority queue
q = queue.PriorityQueue()

q.put(State(4))
q.put(State(7))
q.put(State(2))
q.put(State(7))
q.put(State(19))

print("Queue Priority:")


while not q.empty():
    next_state = q.get()
    print(next_state.nodes)

print()

#Heap

heap = []
data = [2,19,45,3,89,1]

print("Heap:")

for d in data:
    print("Add %d" % d)
    heapq.heappush(heap, d)
    
print()

for i in range(len(data)):
    smallest = heapq.heappop(heap)
    print('pop    {:>3}:'.format(smallest))

    

