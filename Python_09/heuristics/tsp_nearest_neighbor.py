# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

nearest neighbor heuristic for generating TSP solution.

@author: beer
"""

import sys
try:
    import heuristics.problems.tsp.utils.helpers as hlp
except Exception:  # fallback for relative import when within package
    from .problems.tsp.utils import helpers as hlp


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

        # Guard: empty instance
        if not workingPoints:
            return solution

        # Clamp start index to valid range
        n = len(workingPoints)
        idx = max(0, min(startIndex, n - 1))

        # Start from the chosen point
        current = workingPoints.pop(idx)
        solution.append(current)

        # Iteratively select the nearest unvisited point
        while workingPoints:
            nearest_idx = 0
            best_dist = sys.float_info.max
            for i, p in enumerate(workingPoints):
                d = hlp.Helpers.euclideanDistance2DPoints(current, p)
                if d < best_dist:
                    best_dist = d
                    nearest_idx = i
            current = workingPoints.pop(nearest_idx)
            solution.append(current)

        return solution
