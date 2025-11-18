# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

random sampling heuristic for generating TSP solution.

@author: beer
"""

import random
import sys
import heuristics.problems.tsp.utils.helpers as hlp


class TspRandomSampling:

    def generate(instance, numTries):
        solution = instance.clonePointList()
        bestDistance = sys.float_info.max
 
        for i in range(numTries):
            random.shuffle(solution)
            distance = hlp.Helpers.euclideanDistance2DList(solution)

            if distance < bestDistance:
                bestSolution = solution.copy()
                bestDistance = distance

        return bestSolution
