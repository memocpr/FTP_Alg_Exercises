# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

Demo for TSP solutions generated with simulated annealing metaheuristic.

@author: beer
"""

import os
import time
from types import MethodType

import heuristics.problems.knapsack.utils.instance as inst
import heuristics.knapsack_simulated_annealing as sa


def live_update(self, step, T, E, acceptance, improvement):
    """Stream condensed progress information for the active run."""
    label = getattr(self, 'run_label', 'run')
    if acceptance is None:
        print(f"\n[{label}] warmup  step={step:6d}  temp={T:10.2f}  energy={E:10.2f}")
        return
    print(
        f"[{label}] update  step={step:6d}  temp={T:10.2f}  energy={E:10.2f}  "
        f"accept={acceptance:6.2%}  improve={improvement:6.2%}",
        flush=True,
    )


if __name__ == '__main__':
    
    instanceName = 'KS_P08'
    
    instanceExtension = '.txt'

    script_dir = os.path.dirname(os.path.abspath(__file__))
    pathToInstance = os.path.join(
        script_dir,
        'heuristics', 'problems', 'knapsack', 'instances', instanceName + instanceExtension,
    )

    print('Loading instance ' + instanceName + ' ...')
    instance = inst.Instance(pathToInstance)

    print('Instance has ' + str(instance.getNumItems()) + ' items.')

    schedules = [
        {
            'label': 'baseline',
            'params': {'tmax': 1.0e7, 'tmin': 7.0e3, 'steps': 100000, 'updates': 200},
        },
        {
            'label': 'fast_cool',
            'params': {'tmax': 5.0e6, 'tmin': 5.0e3, 'steps': 60000, 'updates': 150},
        },
        {
            'label': 'slow_precise',
            'params': {'tmax': 2.0e7, 'tmin': 1.0e3, 'steps': 150000, 'updates': 300},
        },
    ]

    for schedule in schedules:
        label = schedule['label']
        print('\n' + '=' * 80)
        print(f"Running schedule '{label}' with {schedule['params']}")
        print('=' * 80)

        ks = sa.KnapsackSimulatedAnnealing(instance)
        ks.copy_strategy = 'method'
        ks.set_schedule(schedule['params'])
        ks.updates = schedule['params']['updates']
        ks.run_label = label
        ks.update = MethodType(live_update, ks)

        start = time.perf_counter()
        solution, bestNegVal = ks.findSolution()
        elapsed = time.perf_counter() - start

        print('\n[Result]', flush=True)
        print('Knapsack has capacity: ' + str(solution.getCapacity()))
        print('Solution has weight: ' + str(solution.getWeight()))
        print('Solution has value: ' + str(solution.getValue()))
        print(f"Elapsed time: {elapsed:.2f}s")
        flags = []
        for k in range(solution.getNumItems()):
            if solution.getItemFlag(k):
                flags.append(1)
            else:
                flags.append(0)
        print('Item flags: ' + str(flags))
        print('')
