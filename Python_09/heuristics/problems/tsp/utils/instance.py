# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

Use this class to represent instances of TSP.

@author: beer
"""

import heuristics.problems.tsp.utils.point as pnt


class Instance:
    NAME_INDEX = 0
    COMMENT_INDEX = 1

    name = ''
    comment = ''

    points = []

    def __init__(self, *args):
  
        # if there are 3 args: create instance from data in args
        if len(args) == 3:
            if isinstance(args[0], str) and isinstance(args[1], str) and isinstance(args[2], list):
                self.name = args[0]
                self.comment = args[1]
                self.points = args[2]
            else:
                raise ValueError

        # if there is 1 arg: create instance from given file
        elif isinstance(args[0], str):
            try:
                with open(args[0]) as f:
                    lines = f.readlines()
            except OSError as err:
                print('OS error: {0}'.format(err))

            header = lines[0:2]
            self.name = header[self.NAME_INDEX].split()[1]
            self.comment = header[self.COMMENT_INDEX].split()[1]
                    
            self.points = []
            for line in lines[2:]:
                splits = line.split()
                point = pnt.Point(int(splits[0]), float(splits[1]), float(splits[2]))
                self.points.append(point)
        else:
            raise ValueError


    def getName(self):
        return self.name


    def getComment(self):
        return self.comment


    def getPoints(self):
        return self.points


    def clonePointList(self):
        clonedPoints = self.points.copy()
        return clonedPoints
