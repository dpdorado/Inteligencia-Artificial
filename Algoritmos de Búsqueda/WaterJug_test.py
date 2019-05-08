# -*- coding: utf-8 -*-
"""
@author: DD
"""

from algorithms.DepthFirst import DepthFirst
from algorithms.DepthLimit import DepthLimit
from algorithms.BreadthFirst import BreadthFirst
from problems.WaterJug import WaterJug
from problems.SumProblem import SumProblem


#wj=WaterJug(4,3,(4,3),(2,0))
wj=WaterJug()


#DepthFirst
#bf=DepthFirst(wj)

#DepthLimit
bf=DepthLimit(wj)

#BreadthFirst
#bf=BreadthFirst(wj)



#sol=bf.run(5)
sol=bf.run()
print('Solution: '+str(sol))
