# -*- coding: utf-8 -*-
"""
@author: DD
"""
from algorithms.DepthFirst import DepthFirst
from algorithms.BreadthFirst import BreadthFirst
from problems.SumProblem import SumProblem


#sp=SumProblem((1,2,3,4,10,13),13)
#sp=SumProblem((1,2,3,4,10),7)
sp=SumProblem((1,2,3,4),10)

#DepthFirst
bf=DepthFirst(sp)

#BreadthFirst
#bf=BreadthFirst(sp)

sol=bf.run()
print('Solution: '+str(sol))
