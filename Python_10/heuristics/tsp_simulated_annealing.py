# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

Demo for TSP solutions generated with simulated annealing metaheuristic.

@author: beer
"""

import random

import heuristics.problems.tsp.utils.helpers as hlp
import heuristics.metaheuristics.simulated_annealing.anneal as sa


class TspSimulatedAnnealing(sa.Annealer):

    # pass extra data (if any) into the constructor
    def __init__(self, state):
        super(TspSimulatedAnnealing, self).__init__(state)  # important!


    def move(self):
        # choose two different cities in the route
        while True:
            a = random.randint(0, len(self.state) - 1)
            b = random.randint(0, len(self.state) - 1)
            if a != b:
                break

        # enforc a < b, except for special case    
        if a>b:
            a, b = b, a
        if a==0 and b==len(self.state)-1:
            a, b = b, a

        # compute delta energy
        dE = 0.
        dE += hlp.Helpers.euclideanDistance2DPoints(self.state[a], self.state[(b+1)%len(self.state)])
        dE += hlp.Helpers.euclideanDistance2DPoints(self.state[b], self.state[a-1])
        dE -= hlp.Helpers.euclideanDistance2DPoints(self.state[a], self.state[a-1])
        dE -= hlp.Helpers.euclideanDistance2DPoints(self.state[b], self.state[(b+1)%len(self.state)])
        if (a+1)%len(self.state) != b:
            dE += hlp.Helpers.euclideanDistance2DPoints(self.state[a], self.state[b-1])
            dE += hlp.Helpers.euclideanDistance2DPoints(self.state[b], self.state[(a+1)%len(self.state)])
            dE -= hlp.Helpers.euclideanDistance2DPoints(self.state[a], self.state[(a+1)%len(self.state)])
            dE -= hlp.Helpers.euclideanDistance2DPoints(self.state[b], self.state[b-1])
            
        # swap cities
        self.state[a], self.state[b] = self.state[b], self.state[a]
        
        return dE


    def special_action(self, step, T):
        # empty stub
        return 0
 
    
    def energy(self):
        """Calculates the length of the route."""
        e = 0.
        for i in range(len(self.state)):
            e += hlp.Helpers.euclideanDistance2DPoints(self.state[i-1], self.state[i])
        return e


    def findSolution(self):
        # since our state is just a list, slice is the fastest way to copy
        self.copy_strategy = "slice"
        solution, distance = self.anneal()
        return solution, distance
    
