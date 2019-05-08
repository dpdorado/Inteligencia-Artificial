"""
@author: DD
"""
import math
from Node import Node
from problems.Problem  import Problem

class Puzzle(Problem):
    def __init__(self,initial_state=(0,1,2,3,4,5,6,7,8),final_state=(1,0,2,3,4,5,6,7,8)):
        super().__init__(initial_state,final_state)

    def child_node(self,node):
        child=[]

        son=self.move_up(node)
        if(son!=None):
            child.append(son)

        son=self.move_down(node)
        if(son!=None):
            child.append(son)

        son=self.move_right(node)
        if(son!=None):
            child.append(son)
            
        son=self.move_left(node)
        if(son!=None):
            child.append(son)

        return child

    def move_up(self,node):
        state=node.State
        pos_0=self.find_pos_O(state)
        lon_m=self.lon_matriz(state)
        if pos_0<len(state)-lon_m :
            new_state=self.to_exchange(state,pos_0,pos_0+lon_m)
            new_node=Node(new_state,parent=node,action='move_up')
            return new_node
        else:
            return None

    def move_down(self,node):
        state=node.State
        pos_0=self.find_pos_O(state)
        lon_m=self.lon_matriz(state)
        if pos_0>lon_m:
            new_state=self.to_exchange(state,pos_0,pos_0-lon_m)
            new_node=Node(new_state,parent=node,action='move_down')
            return new_node
        else:
            return None

    def move_right(self,node):
        state=node.State
        pos_0=self.find_pos_O(state)
        lon_m=self.lon_matriz(state)
        if not (pos_0 in self.getpos_numbers_left(lon_m)):
            new_state=self.to_exchange(state,pos_0,pos_0-1)
            new_node=Node(new_state,parent=node,action='move_right')
            return new_node
        else:
            return None

    def move_left(self,node):
        state=node.State
        pos_0=self.find_pos_O(state)
        lon_m=self.lon_matriz(state)
        if not (pos_0 in self.getpos_numbers_right(lon_m)):
            new_state=self.to_exchange(state,pos_0,pos_0+1)
            new_node=Node(new_state,parent=node,action='move_left')
            return new_node
        else:
            return None

    #Métodos auxiliares
    def find_pos_O(self,state):
        pos_0=0
        for pos in range(0,len(state)):
            if state[pos] == 0:
                pos_0=pos
                break
        return pos_0

    def lon_matriz(self,state):
        return math.sqrt(len(state))

    def getpos_numbers_left(self,len_m):
        pos_numbers=[]
        pos=0
        dimension_m=len_m*len_m
        while pos<dimension_m:
            pos_numbers.append(pos)
            pos+=len_m
        return pos_numbers

    def getpos_numbers_right(self,len_m):
        pos_numbers=[]
        pos_i=len_m-1
        pos=pos_i
        dimension_m=len_m*len_m
        while pos<dimension_m:
            pos_numbers.append(pos)
            pos+=pos_i+1
        return pos_numbers

    def to_exchange(self,state,pos_10,pos_1n):
        pos_0=math.floor(pos_10)
        pos_n=math.floor(pos_1n)
        new_estate=list(state)
        aux=new_estate[pos_0]
        new_estate[pos_0]=new_estate[pos_n]
        new_estate[pos_n]=aux
        return tuple(new_estate)

    #-------------------------------------------		          