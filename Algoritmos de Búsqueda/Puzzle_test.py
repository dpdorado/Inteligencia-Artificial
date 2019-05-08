# -*- coding: utf-8 -*-
"""
@author: DD
"""
from algorithms.DepthFirst import DepthFirst
from algorithms.BreadthFirst import BreadthFirst
from problems.Puzzle import Puzzle

#pz=Puzzle((1,0,2,3),(1,3,0,2))
#pz=Puzzle((1,0,2,3,4,5,6,7,8),(1,4,2,6,3,5,7,0,8))
#pz=Puzzle((1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15),(1,5,2,3,4,6,7,11,8,9,10,15,0,12,13,14))
pz=Puzzle()

#DepthFirst
#bf=DepthFirst(pz)

#BreadthFirst
bf=BreadthFirst(pz)

sol=bf.run()
print('Solution: '+str(sol))
