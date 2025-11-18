# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

Demo for TSP solutions generated with the greedy random insertion heuristic.

@author: beer
"""

import os

import heuristics.problems.tsp.utils.printer as prnt
import heuristics.problems.tsp.utils.instance as inst
import heuristics.problems.tsp.utils.helpers as hlp
import heuristics.tsp_greedy_insertion_random as gir


if __name__ == '__main__':
    
    instanceName = 'rl5915'
    solutionName = instanceName + '_greedy_insertion_random'

    instanceExtension = '.tsp'
    solutionExtension = '.html'

    pathToInstance = 'heuristics' + os.path.sep + 'problems' + os.path.sep + 'tsp' + os.path.sep + 'instances' + os.path.sep + instanceName + instanceExtension
    pathToSolution = 'heuristics' + os.path.sep + 'problems' + os.path.sep + 'tsp' + os.path.sep + 'solutions' + os.path.sep + solutionName + solutionExtension

    print('Loading instance ' + instanceName + '...')
    instance = inst.Instance(pathToInstance)

    solution = instance.getPoints()
    print('Instance has ' + str(len(solution)) + ' points.')

    print('Generating a solution with the greedy random insertion heuristic...')

    solution = gir.TspGreedyInsertionRandom.generate(instance)
    distance = hlp.Helpers.euclideanDistance2DList(solution)
        
    print('Solution for ' + instanceName + ' has length: ' + str(distance))
    print('')

    # generate visualization of result, will be stored in directory pathToSolutions
    prnt.Printer.writeToSVG(instance, solution, pathToSolution)
