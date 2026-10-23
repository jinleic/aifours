# Plan E15c: the remaining p = 7, B = 0 IIIb cells with 3-pattern pruning (pre-registered before running; file mtime authoritative)

Owner OlsonReflectionRigidity.  Follows plan-E15b.md.  It is a finite aid and not a premise.

## Status of E15b (code/e15b_census_v2.py 5c9b9b57...0a7e)

Completed with 0 full avoiders: cells (kappa, k) = (4,9), (4,10), (4,11), (4,12), (4,13), (4,14), (4,15), (5,11), (5,12),
(5,13), (6,13), together with (3,13) from E15.
- (4,13) had 2 2-avoiders, (4,14) had 380 and (4,15) had 54,927.  Every one of them was killed by a 3-interval pattern.
- (6,13) had 2 2-avoiders, both killed at m = 3.
Interrupted, UNKNOWN: (5,17).  It was the first run (exit 152, CPU limit) and the second run (exit 143, SIGTERM at 09:25, cause
not identified).  No output file exists for it.
Not started: (5,14), (5,15), (5,16), (6,14), (6,15), (6,16), (6,17), (6,18), (6,19).  All are IIIb (R <= 2 kappa).

## Change (new code version code/e15c_census.py)

The DFS of e15_two_avoiders.search is extended with 3-interval pruning.
- At step j < k - 1, every 3-pattern whose last interval ends at j is tested.  This uses the cumulative set of
  (mass, residue) pairs of 2-patterns that end at least two runs earlier.
- At the leaf, 3-patterns are not pruned.  Instead every surviving leaf goes through e14e_kills.killed_by(m = 2 and m = 3) and
  then the full 2^k check, so cyclic correctness is preserved.
- A leaf that survives the pruning and is killed only at m >= 4 is recorded with its minimal m.

## Cross-check

E15c must reproduce cell (4,15) as "0 leaves survive m <= 3; 0 full avoiders", consistent with E15b, which found all 54,927
2-avoiders killed at m = 3.

## Execution and decision use

- Cells run in increasing order of data count, one process, under ulimit -t.  Each cell writes out/e15c_<kappa>_<k>.json.
- A full avoider is reported to Main at once.
