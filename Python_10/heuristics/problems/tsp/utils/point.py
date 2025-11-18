# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

Use this class to represent points in 2D Space.

@author: beer
"""

class Point:
    id = 0
    x = 0.
    y = 0.;
	
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def getId(self):
        return self.id

    def getX(self):
        return self.x

    def	getY(self):
        return self.y
