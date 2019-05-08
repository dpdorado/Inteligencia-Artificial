"""
@author: DD
"""

from Node import Node
from problems.Problem  import Problem

class SumProblem(Problem):

    def __init__(self, elements_list, number, initial_state=()):
        self.elements_list=elements_list
        self.number=number
        super().__init__(initial_state,None)

    def child_node(self,node):
        child=[]
        for num in self.elements_list:
            son= self.add_num(num,node)
            if son != None :
                child.append(son)
        return child

    def add_num(self,num,node):
        state=node.State
        if num in state and state.index(num) == self.elements_list.index(num):
            return None
        new_state=list(state)
        new_state.append(num)
        if self.sum_num(new_state)<=self.number:
            return Node(tuple(new_state),parent=node,action='add_num')
        return None  

    def sum_num(self,state):
        sum_state=0
        for num in state:
            sum_state=sum_state+num
        return sum_state

    def goal_test(self,node):
        result=False
        if self.sum_num(node.state)==self.number:
            result=True
        return result