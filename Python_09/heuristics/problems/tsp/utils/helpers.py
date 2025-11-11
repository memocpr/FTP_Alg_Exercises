# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:24:10 2021

Collection of Helper functions implemented as static methods

@author: beer
"""

import random
import math

import heuristics.problems.tsp.utils as utl


class Helpers:
        
    """
    Get the Euclidean distance between two points in 2D.
    @param a: Point
    @param b: Point
    @return: float
    """

    def euclideanDistance2DPoints(a, b):
        return math.sqrt((a.getX() - b.getX())**2 + (a.getY() - b.getY())**2)


    """
    Get the cost for a whole trip using the Euclidean distance. The way from
    the last point in the list to the start is included.
    
    @param points: list of Points
    @return: float
    """
    def euclideanDistance2DList(points):
        totalDistance = 0.

        currentPoint = points[0]
        for i in range(1, len(points)):
            nextPoint = points[i]
            totalDistance += Helpers.euclideanDistance2DPoints(currentPoint, nextPoint)
            currentPoint = nextPoint

        totalDistance += Helpers.euclideanDistance2DPoints(currentPoint, points[0])
        return totalDistance


    """
    Get the point with the lowest id.
    @param points: List of Points
    @return: Point
    """
    def getLowestIdPoint(points):
        lowestPoint = points[0]
        for point in points:
            if point.getId() < lowestPoint.getId():
                lowestPoint = point
        return lowestPoint


    """
    Generate a random instance.
    
    @param name:        The name of the generated instance (string).
    @param comment:     The comment for the generated instance (string).
    @param numPoints:   The number of points to generate randomly.
    @return An Instance with given name and comment and randomly distributed points.
    """
    def getRandomTspInstance(name, comment, numPoints):
        maxX = 2000
        maxY = 2000

        points = []
        id = 0

        for i in range(numPoints):
            x = random.randint(0, maxX)
            y = random.randint(0, maxY)

            points.add(utl.point.Point(id, x, y))
            id += 1

        return utl.instance.Instance(name, comment, points)
