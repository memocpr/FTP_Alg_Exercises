# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

nearest neighbor heuristic for generating TSP solution.

@author: beer
"""

import sys
import heuristics.problems.tsp.utils.helpers as hlp


class TspNearestNeighbor:

    def generate(instance, startIndex):
        workingPoints = instance.clonePointList()

        solution = []
        
        """
        Hints:
        - workingPoints is a list of the point coordinates of the cities to be visited in the given tsp instance
        - instance is a class defined in tsp->utils
        - point is class defined in tsp->utils
        - hlp.Helpers.euclideanDistance2DPoints() computes the distance between two points
        - solution must be a list of points, specifying the order, in which the cities are to be visited
        """

        solution = workingPoints    # must be replaced by the code for the nearest neighbor heuristic!

        return solution
