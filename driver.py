# -*- coding: utf-8 -*-
"""
Created on Mon May 15 12:46:56 2017

@author: FraDepa
"""

import Queue

def hello():
    print("Hello World")

hello()

q = Queue.Queue()

for i in range(7):
    q.put(i)
    
while not q.empty():
    print(q.get())
    
    
