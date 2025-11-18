# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

Demo for TSP solutions generated with simulated annealing metaheuristic.

@author: beer
"""

import random
import os

import heuristics.problems.tsp.utils.printer as prnt
import heuristics.problems.tsp.utils.instance as inst
import heuristics.problems.tsp.utils.helpers as hlp
import heuristics.tsp_simulated_annealing as sa


if __name__ == '__main__':
    
    instanceName = 'tsp225'
    solutionName = instanceName + '_simulated_annealing'

    instanceExtension = '.tsp'
    solutionExtension = '.html'

    pathToInstance = 'heuristics' + os.path.sep + 'problems' + os.path.sep + 'tsp' + os.path.sep + 'instances' + os.path.sep + instanceName + instanceExtension
    pathToSolution = 'heuristics' + os.path.sep + 'problems' + os.path.sep + 'tsp' + os.path.sep + 'solutions' + os.path.sep + solutionName + solutionExtension
    

    print('Loading instance ' + instanceName + '...')
    instance = inst.Instance(pathToInstance)

    solution = instance.getPoints()
    print('Instance has ' + str(len(solution)) + ' points.')

    print('Generating a random initial solution...')

    random.shuffle(solution)
    distance = hlp.Helpers.euclideanDistance2DList(solution)
        
    print('Initial solution for ' + instanceName + ' has length: ' + str(distance))
    print('Refining solution with the simulated annealing metaheuristic...')
    print('', flush=True)

    tsp = sa.TspSimulatedAnnealing(solution)

    tsp.copy_strategy = "slice"
    tsp.set_schedule({'tmax': 8000., 'tmin': 15., 'steps': 2000000, 'updates': 500})

    solution, distance = tsp.findSolution()

    for i in range(len(solution)):          # rotate id = 0 to beginning
        if solution[i].getId() == 0:
            break
    solution = solution[i:] + solution[:i]  

    print('')
    print('', flush=True)
    print('Solution for ' + instanceName + ' has length: ' + str(distance))
    print('')

    # generate visualization of result, will be stored in directory pathToSolutions
    prnt.Printer.writeToSVG(instance, solution, pathToSolution)
