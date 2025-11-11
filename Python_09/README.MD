# TSP Heuristics Demos (Task 2)

This folder contains simple Python demos and heuristic implementations for the Traveling Salesman Problem (TSP) used in Task 2 (Comparing Heuristics).

## Implemented Heuristics
- Nearest Neighbor (`heuristics/tsp_nearest_neighbor.py`)
  - Starts from a chosen start index (clamped) and repeatedly appends the nearest unvisited city.
- Random Sampling (`heuristics/tsp_random_sampling.py`)
  - Shuffles the full tour multiple times; keeps the best found.
- Greedy Random Insertion (`heuristics/tsp_greedy_insertion_random.py`)
  - Random order of points, then inserts each remaining point into the partial tour at the position causing minimal increase.

Each heuristic returns a list of `Point` objects representing the visit order (final edge back to start is implicit in distance computation & SVG output).

## Data Structures
Located under `heuristics/problems/tsp/utils/`:
- `instance.py` loads `.tsp` instance files and provides `clonePointList()`.
- `point.py` simple 2D point with id.
- `helpers.py` distance utilities (`euclideanDistance2DPoints`, `euclideanDistance2DList`).
- `printer.py` writes an HTML+SVG visualization to the `solutions` directory.

Instances: `heuristics/problems/tsp/instances/*.tsp` (e.g. `berlin52.tsp`, `bier127.tsp`).
Solutions (HTML) are written to: `heuristics/problems/tsp/solutions/`.

## Demo Scripts
- `demo_tsp_nearest_neighbor.py`
- `demo_tsp_random_sampling.py`
- `demo_tsp_greedy_insertion_random.py`
- `demo_tsp_compare.py` (added): runs all three heuristics on a chosen instance and reports distance + runtime.

## Quick Start
Requires Python 3.11+ (standard library only).
Run from the folder `Python_09` so relative paths resolve.

```bash
cd Python_09
python3 demo_tsp_nearest_neighbor.py
python3 demo_tsp_random_sampling.py
python3 demo_tsp_greedy_insertion_random.py
python3 demo_tsp_compare.py            # default: berlin52
```

### Run comparison on multiple instances (example)
```bash
python3 - <<'PY'
from demo_tsp_compare import run_compare
for inst in ['berlin52','bier127','tsp225']:
    run_compare(inst, num_tries_random_sampling=200)
PY
```

## Sample Comparison Output (your numbers may differ)
```
Results for instance berlin52:
Heuristic, Distance, Time[s]
NearestNeighbor, 10260.40, 0.001
RandomSampling, 25590.91, 0.015
GreedyInsertionRandom, 8684.97, 0.003
```
Additional runs (earlier) showed for `bier127` and `tsp225` that Greedy Random Insertion often beats Nearest Neighbor; Random Sampling is worst with modest try counts.

## Notes & Assumptions
- Random Sampling quality depends on `numTries` (increase for better tours but longer runtime).
- Nearest Neighbor start index currently fixed at `0` in demos; you can test different starts by changing the call.
- Import fallbacks allow heuristics to work whether executed as script or package.
- SVG shows total distance (rounded) and highlights start node in blue.

## Extending
- Add more heuristics (e.g., 2-opt) and register them in a similar compare script.
- Optionally export results to CSV: adapt `demo_tsp_compare.py` to write `name,distance,time` lines.

## Directory Overview (key parts)
```
heuristics/
  tsp_nearest_neighbor.py
  tsp_random_sampling.py
  tsp_greedy_insertion_random.py
  problems/tsp/
    instances/*.tsp
    utils/{instance.py,point.py,helpers.py,printer.py}
    solutions/*.html
```

## License / Attribution
Educational exercise code for heuristic comparison (Task 2). Original scaffolding authored by *beer*; Nearest Neighbor implementation & comparison script added in this iteration.

