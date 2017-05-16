# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:25:44 2017

@author: csto935
"""
#Example Class to understand Priority Queue


class State(object):
    
    def __init__(self, nodes):
        self.nodes = nodes
        return
    def __eq__(self, other):
        return self.nodes == other.nodes
    def __lt__(self, other):
        return self.nodes < other.nodes
    def __gt__(self,other):
        return self.nodes > other.nodes
    
    

