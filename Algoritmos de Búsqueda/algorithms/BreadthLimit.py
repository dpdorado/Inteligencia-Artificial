"""
@author: DD
"""

from collections import deque


class BreadthLimit():
 
    def __init__(self,problem):
        self.problem=problem

    
    def run(self,limit=5):
        open_list=deque()
        close_list=deque()
        starting_node=self.problem.Initial_Node
        open_list.append(starting_node)
        solution=[]
        
        while len(open_list) > 0:
            current_node=open_list.popleft()
            
            print('Current_Node:'+str(current_node.State))
            
            close_list.append(current_node)
            
            if self.problem.goal_test(current_node):
                while current_node.Parent!=None:
                    solution.append(current_node.Action)
                    current_node=current_node.Parent
                solution.reverse()
                return solution 

            if current_node.Level()-1 > limit:
                break   
                   
            children= self.problem.child_node(current_node) 
    
            for child in children :
                if child not in open_list and child not in close_list:
                    print('Child:'+str(child.State))
                    open_list.append(child)
                    
        return solution
