# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

Demo for TSP solutions generated with simulated annealing metaheuristic.

@author: beer
"""

import os

import heuristics.problems.knapsack.utils.instance as inst
import heuristics.knapsack_simulated_annealing as sa


if __name__ == '__main__':
    
    instanceName = 'KS_P08'
    
    instanceExtension = '.txt'

    pathToInstance = 'heuristics' + os.path.sep + 'problems' + os.path.sep + 'knapsack' + os.path.sep + 'instances' + os.path.sep + instanceName + instanceExtension

    print('Loading instance ' + instanceName + ' ...')
    instance = inst.Instance(pathToInstance)

    print('Instance has ' + str(instance.getNumItems()) + ' items.')

    print('Computing solution with the simulated annealing metaheuristic ...')
    print('', flush=True)

    ks = sa.KnapsackSimulatedAnnealing(instance)

    ks.copy_strategy = "method"     # deepcopy is very slow!

    ks.set_schedule({'tmax': 10000000., 'tmin': 7000., 'steps': 100000, 'updates': 500})

    solution, bestNegVal = ks.findSolution()

    print('')
    print('', flush=True)
    print('Knapsack has capacity: ' + str(solution.getCapacity()))
    print('Solution has weight: ' + str(solution.getWeight()))
    print('Solution has value: ' + str(solution.getValue()))
    flags = []
    for k in range(solution.getNumItems()):
        if solution.getItemFlag(k):
            flags.append(1)
        else:
            flags.append(0)
    print('Item flags: ' + str(flags))
    print('')
