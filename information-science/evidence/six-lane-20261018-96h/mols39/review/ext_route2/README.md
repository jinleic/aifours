# ext_route2: route-2 search for one new equivariant DM row

Independent second implementation, written from the task definitions only
(route-1 code under `mols39/code/` and runs under `mols39/evidence/runs-ext1/`
were not read). Python 3.14 stdlib only; single process; no threads,
subprocesses or network. Not executed by its author; the owner runs it.

## Definition
- RAW: k lines of n integers; `D[i][c]` is read mod n; `col_c = (D[0][c], ..., D[k-1][c])`.
- D is a (Z_n,k;1)-DM iff its n columns are distinct and, for all rows i<j,
  the values `(D[i][c] - D[j][c]) mod n`, c = 0..n-1, are pairwise distinct.
- A generator `[mu, perm]` (mu a unit mod n, perm a permutation of 0..k-1) acts
  by `(g.v)[perm[x]] = mu*v[x] mod n`; G is the closure of the generators,
  identity included (`[]` gives G = {identity}). Every generator must map the
  column set onto itself.
- Wanted: every f: columns -> Z_n with (a) `f(g.v) = mu_g*f(v) mod n` for all g
  in G and all columns v, and (b) for every old row i the values
  `(D[i][c] - f(col_c)) mod n` pairwise distinct, i.e. D with f appended is a
  (Z_n,k+1;1)-DM. `--fix-zero-column` also requires f(all-zero column) = 0.

## Algorithm
1. G by BFS closure as explicit `(mu, perm)` pairs. Orbits of G on the columns;
   representative r = smallest column index of the orbit; for each member v the
   multiplier of the first g (BFS order) with g.r = v (identity for r); the
   multipliers of Stab(r).
2. Admissible w for an orbit: `(mu_h - 1)*w = 0 mod n` for every h in Stab(r)
   (only w = 0 for the zero column under `--fix-zero-column`). w defines
   `f(g.r) = mu_g*w` on the orbit; the stabiliser condition makes this well
   defined, and these are exactly the f satisfying (a) on the orbit. For each
   old row i: bitmask of `(D[i][v] - f(v)) mod n` over the orbit; (orbit, w) is
   dropped if two members collide in some row. `admissible_pairs` counts the
   surviving pairs.
3. DFS over orbits in a fixed order (larger orbits first, ties by smaller
   representative), w increasing, one used-value bitmask per old row. A pair is
   placed only if its masks are disjoint from the used masks in every row; each
   full assignment is one solution. `nodes` = partial assignments visited
   (root included). The search stops at MAX_SOLUTIONS, or when
   `time.monotonic()` passes program start + BUDGET_S (clock read every 4096
   nodes).
4. If there is at least one solution: `os.makedirs(OUT_DIR, exist_ok=False)`;
   the first <= 20 solutions in search order are exclusive-created as
   `solution_NN.raw` (old rows reduced mod n, then f), read back, re-checked as
   a (Z_n,k+1;1)-DM (`dm_ok`) and hashed (`sha256`). `constant`: f is constant.

## CLI
    python3.14 -I -B ext_route2.py RAW SHA256 N GENS_JSON BUDGET_S OUT_DIR MAX_SOLUTIONS [--fix-zero-column]

- GENS_JSON is JSON text, e.g. `'[[16,[1,2,0,4,5,3]],[38,[0,1,2,3,4,5]]]'`.
- BUDGET_S: finite number >= 0. MAX_SOLUTIONS: integer >= 1. OUT_DIR must not exist.
- Stdout: one JSON line with keys `status`, `input_sha256`, `n`, `k_old`,
  `group_order`, `orbit_sizes` (ascending), `admissible_pairs`, `solutions`,
  `nodes`, `written` (list of `{path, sha256, dm_ok, constant}`), `wall_s`, and
  `detail` (reason for error statuses, else null). Values not reached are null.

## Exit codes
| exit | status |
|---|---|
| 0 | COMPLETE (search exhausted), INCOMPLETE_BUDGET, STOPPED_AT_MAX_SOLUTIONS |
| 2 | INPUT_PIN_MISMATCH (SHA-256 of the RAW bytes differs from SHA256); BAD_INPUT (extension: malformed arguments, RAW or generators, or OUT_DIR exists) |
| 3 | OLD_NOT_DM, NOT_INVARIANT, NO_ZERO_COLUMN |
| 1 | uncaught Python exception (no JSON line) |

Checks run in this order: arguments, pin, RAW and generator parsing,
OLD_NOT_DM, NOT_INVARIANT, NO_ZERO_COLUMN.
