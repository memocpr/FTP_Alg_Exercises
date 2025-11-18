# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

Demo for KNAPSACK solutions generated with simulated annealing metaheuristic.

@author: beer
"""

import random

import heuristics.metaheuristics.simulated_annealing.anneal as sa


class KnapsackSimulatedAnnealing(sa.Annealer):

    # pass extra data (if any) into the constructor
    def __init__(self, state):
        super(KnapsackSimulatedAnnealing, self).__init__(state)  # important!


    def move(self):
        while True:
            # flip a single bit randomly selected
            a = random.randint(0, self.state.getNumItems()-1)
    
            if not self.state.getItemFlag(a):   # item is not in knapsack
                new_weight = self.state.getWeight() + self.state.getItemWeight(a) 

                if new_weight <= self.state.getCapacity():
                    self.state.setWeight(new_weight)    # add item to knapsack
                    dE = -self.state.getItemValue(a)
                    self.state.addToValue(-dE)
                    self.state.setItemFlag(a)
                    break
                else:
                    continue                            # flipping bit is not feasible --> try next one

            else:                               # item is in knapsack --> remove it
                self.state.addToWeight(-self.state.getItemWeight(a))
                dE = self.state.getItemValue(a)
                self.state.addToValue(-dE)
                self.state.clearItemFlag(a)
                break

        # return delta energy
        return dE
    

    def energy(self):
        # Compute negative value and weight of knapsack instance.
        w = 0.
        e = 0.
        for i in range(self.state.getNumItems()):
            if self.state.getItemFlag(i):
                w += self.state.getItemWeight(i)
                e -= self.state.getItemValue(i)
                
        self.state.setWeight(w)
        self.state.setValue(-e)
        return e


    def special_action(self, step, T):
        # Nothing has to be done here.
        return 0
 
    
    def findSolution(self):
        solution, neg_val = self.anneal()
        return solution, -neg_val
    
