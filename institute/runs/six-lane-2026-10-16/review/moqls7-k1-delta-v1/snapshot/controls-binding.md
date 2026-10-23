# drat-trim control inputs: lane files versus parent route-2 controls (desk hash check; no CNF copies made)

The hashes below were recomputed by the delegated parent delta check on 2026-10-17 PDT. The control files are
tiny; their contents are described here instead of being copied.

| file | bytes | sha256 | content |
|---|---|---|---|
| lane `env/drat-trim/ctl_sat.cnf` | 14 | 6642f3ff4fae6f869a53f303bc768802cec0a16af731686c6bf03f342cf0489e | `p cnf 1 1` / `1 0` (satisfiable) |
| lane `env/drat-trim/ctl_unsat.cnf` | 19 | ac42a371b5a124286c410ed5dfa2e3be7ee7d5b1feac6f08e7e1715f0c3669a8 | `p cnf 1 2` / `1 0` / `-1 0` (contradictory units) |
| lane `env/drat-trim/ctl_unsat.drat` | 2 | 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa | `0` plus LF: one empty-clause step |
| parent `route2/verify/controls/sat.cnf` | 14 | 6642f3ff…0489e | byte-identical to lane ctl_sat.cnf |
| parent `route2/verify/controls/unsat.cnf` | 19 | ac42a371…69a8 | byte-identical to lane ctl_unsat.cnf |
| parent `route2/verify/controls/emptyclause.drat` | 2 | 9a271f2a…86aa | byte-identical to lane ctl_unsat.drat |
| parent `route2/verify/controls/empty.drat` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | empty file |

- Lane `env/drat-trim/drat-trim` binary: sha256 111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4.
  Lane source `drat-trim.c`: d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee.
- The parent route-2 checker recorded in `parent/route2/receipt-route2.json` has binary sha256 a46c0c71…8e37.
  `parent/RESULT.json` discrepancy X3 states that it differs from the lane binary and that the source identity
  d834b649…c2ee holds.
- Each `results.drat_runs` entry for a `ctl_*` run in the receipt records cnf_sha256, proof_sha256, the exit code and
  the parsed `s` line. The raw checker stdout of each control run is in `parent/route2/dt/ctl_*.out`.
