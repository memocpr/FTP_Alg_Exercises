# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

greedy random insertion heuristic for generating TSP solution.

@author: beer
"""

import random
import sys

import heuristics.problems.tsp.utils.helpers as hlp


class TspGreedyInsertionRandom:

    def generate(instance):
        points = instance.getPoints()
        #points.sort(key=lambda x: x.getId())
        random.shuffle(points)

		
        nextIndices = [int(0)]*len(points)  # array with the indices of the next nodes
        nextIndices[0] = 1                  # initial partial tour is 0 -> 1 -> 0
		
        TspGreedyInsertionRandom.findBestInsertPosition(points, nextIndices)
        solution = TspGreedyInsertionRandom.buildTourFromIndices(points, nextIndices)

        return solution


    def	findBestInsertPosition(points, nextIndices):
        # find the best position to insert for each remaining point
        for i in range(2, len(points)):
            lowestDistanceIncrease = sys.float_info.max
            lowestDistanceIncreaseIdx = int(-1)
			
            for j in range(i):
                # compute increase of cost of tour if point i is inserted in place j
                distanceIncrease = hlp.Helpers.euclideanDistance2DPoints(points[j], points[i]) + hlp.Helpers.euclideanDistance2DPoints(points[i], points[nextIndices[j]]) - hlp.Helpers.euclideanDistance2DPoints(points[j], points[nextIndices[j]])
                if distanceIncrease < lowestDistanceIncrease:
                    lowestDistanceIncrease = distanceIncrease
                    lowestDistanceIncreaseIdx = j
			
            nextIndices[i] = nextIndices[lowestDistanceIncreaseIdx]
            nextIndices[lowestDistanceIncreaseIdx] = i

	
    def buildTourFromIndices(points, nextIndices):
        # walk along next indices to build solution
        solution = []
        j = int(0)
        for i in range(len(points)):
            solution.append(points[j])
            j = nextIndices[j]
            
        return solution
