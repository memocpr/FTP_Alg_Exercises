# -*- coding: utf-8 -*-
"""
Compare TSP heuristics: Nearest Neighbor, Random Sampling, Greedy Random Insertion.
Runs on a chosen instance and reports distance and runtime for each.
"""
import os
import time

import heuristics.problems.tsp.utils.printer as prnt
import heuristics.problems.tsp.utils.instance as inst
import heuristics.problems.tsp.utils.helpers as hlp

import heuristics.tsp_nearest_neighbor as nn
import heuristics.tsp_random_sampling as rs
import heuristics.tsp_greedy_insertion_random as gir


def run_compare(instance_name: str, num_tries_random_sampling: int = 200):
    instance_ext = '.tsp'
    solution_ext = '.html'

    path_to_instance = (
        'heuristics' + os.path.sep + 'problems' + os.path.sep + 'tsp' + os.path.sep + 'instances' + os.path.sep + instance_name + instance_ext
    )
    base_sol_path = (
        'heuristics' + os.path.sep + 'problems' + os.path.sep + 'tsp' + os.path.sep + 'solutions' + os.path.sep
    )

    results = []

    # Nearest Neighbor
    instance = inst.Instance(path_to_instance)
    t0 = time.perf_counter()
    sol_nn = nn.TspNearestNeighbor.generate(instance, 0)
    t1 = time.perf_counter()
    dist_nn = hlp.Helpers.euclideanDistance2DList(sol_nn)
    prnt.Printer.writeToSVG(instance, sol_nn, os.path.join(base_sol_path, f"{instance_name}_nearest_neighbor{solution_ext}"))
    results.append(("NearestNeighbor", dist_nn, t1 - t0))

    # Random Sampling
    instance = inst.Instance(path_to_instance)
    t0 = time.perf_counter()
    sol_rs = rs.TspRandomSampling.generate(instance, num_tries_random_sampling)
    t1 = time.perf_counter()
    dist_rs = hlp.Helpers.euclideanDistance2DList(sol_rs)
    prnt.Printer.writeToSVG(instance, sol_rs, os.path.join(base_sol_path, f"{instance_name}_random_sampling{solution_ext}"))
    results.append(("RandomSampling", dist_rs, t1 - t0))

    # Greedy Random Insertion
    instance = inst.Instance(path_to_instance)
    t0 = time.perf_counter()
    sol_gir = gir.TspGreedyInsertionRandom.generate(instance)
    t1 = time.perf_counter()
    dist_gir = hlp.Helpers.euclideanDistance2DList(sol_gir)
    prnt.Printer.writeToSVG(instance, sol_gir, os.path.join(base_sol_path, f"{instance_name}_greedy_insertion_random{solution_ext}"))
    results.append(("GreedyInsertionRandom", dist_gir, t1 - t0))

    print(f"\nResults for instance {instance_name}:")
    print("Heuristic, Distance, Time[s]")
    for name, dist, secs in results:
        print(f"{name}, {dist:.2f}, {secs:.3f}")


if __name__ == '__main__':
    # You can change the instance name here; keep small for quick runs.
    run_compare('berlin52', num_tries_random_sampling=200)

