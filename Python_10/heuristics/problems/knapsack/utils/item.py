# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

Use this class to represent items to put in knapsack.

@author: beer
"""

class Item:
    value = 0.
    weight = 0.
	
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def	getWeight(self):
        return self.weight

    def getValue(self):
        return self.value
