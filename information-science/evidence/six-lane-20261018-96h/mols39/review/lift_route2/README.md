# lift_route2 — independent count of mod-3 rainbow lifts (route 2)

## Definitions (as specified)
- Input: D is k x n over Z_n, where n = 3q and gcd(3,q) = 1. It must be a (Z_n,k;1) DM; otherwise the status is OLD_NOT_DM.
- E[x][c] = D[x][c] - D[0][c] (mod n); B = E mod q (skeleton); T = E mod 3 (true lift).
- Fibre F(x,y,t) = {c : B[x][c]-B[y][c] = t (mod q)}, for x<y. Each fibre must have size 3; this is reported as fibres_all_size_3.
- LIFT: A in Z_3^{k x n} with A[0][*] = 0 such that, on every fibre, the values A[x][c]-A[y][c] are pairwise distinct ("rainbow").
- Classes are taken modulo row constants e (with e_0 = 0). The representative of a class is the lift with A[x][0] = 0 for every x (c_ref = 0).

## Algorithm
The search is a depth-first search over the unknown cells (x,c), x >= 1, c >= 1. Row 0 and column 0 are fixed to 0; fixing column 0 is the class normalisation. Each node does the following:
1. Rainbow filtering: a value w is removed from a cell's domain if, in some fibre through that cell whose partner cell (other row, same column) is already set, w would repeat a difference that is already set in that fibre.
2. Fibre-sum propagator (sound pruning and forcing only). A rainbow triple of Z_3 sums to 0, so every lift satisfies sum_{c in F}(A[x][c]-A[y][c]) = 0 for every fibre. The propagator keeps these equations, plus the DFS decisions as unit equations, in reduced form (pivot = const + sum of free cells). It assigns a cell as soon as it is determined, and it prunes a branch on contradiction. There is no basis enumeration and no kernel or quotient step.
3. Branching: the unassigned cell with the smallest filtered domain (first such cell in row-major order) is chosen, and each value in its domain is tried.
4. After every assignment, every fibre that touches the changed cells is re-checked: its set differences must be pairwise distinct.
5. Leaf (all cells set): the full array is re-checked against the rainbow definition (is_lift) and counted. If this check fails, the status is INTERNAL_ERROR.

Self-tests: on COMPLETE, the leaves must include the normalised T and the normalised -T. Duplicate leaves are an error. Either failure gives INTERNAL_ERROR.

N_classes is the number of leaves, and N_total = 3^(k-1) * N_classes. Adding row constants with e_0 = 0 maps lifts to lifts, and A -> (A - A[.][0], A[.][0]) is a bijection between lifts and (normalised lift, e). So divisibility by 3^(k-1) holds by construction.

The `--no-linear` flag disables step 2 (pure rainbow DFS). It is intended for cross-checking the propagator on small inputs, for example 6x21. It is exponential on 6x39 and 8x57.

## CLI
    python3.14 -I -B lift_route2.py (--raw RAW --sha256 SHA | --builtin singer57) --n N \
        [--rows 0,1,2,...] --budget-s B --out OUT_JSON [--no-linear]

- OUT_JSON is created exclusively. If it already exists, the program prints a BAD_INPUT JSON line and writes no file.
- `--rows` keeps that ordered subset of input rows. Row 0 of the kept list is the normalisation row.
- `singer57` is the 8 x 57 array described in the task: GF(8) = F_2[w]/(w^3+w+1), B57 = (1,6,7,9,19,38,42,49), columns in (u,v) row-major order, then the zero column.

The output is one JSON object, written to OUT_JSON and printed as one line. Its keys are:
- status, n, q, k, input_sha256 ("builtin" for singer57), fibres_all_size_3
- T_is_lift, minusT_is_lift, N_total, N_classes, nodes, wall_s
- classes: a list of {equals: T | -T | other, rep_sha256}
- linear_propagator, rows_kept, and message (only on error)

rep_sha256 is the SHA-256 of the k lines of the representative. Each line holds its entries 0/1/2 separated by single spaces. Lines are joined by "\n", with no trailing newline. On INCOMPLETE_BUDGET, `classes` lists the leaves found so far, and N_total and N_classes are null.

## Exit codes
| exit | status |
|---|---|
| 0 | COMPLETE or INCOMPLETE_BUDGET |
| 3 | OLD_NOT_DM |
| 2 | INPUT_PIN_MISMATCH or BAD_INPUT (bad n, rows, tokens, --rows, existing --out, fibre size != 3); argparse errors also exit 2, with no JSON |
| 4 | INTERNAL_ERROR (self-test failure) |

## Complexity
- Setup: the DM check costs O(k^2 n). The fibre-sum system has C(k,2) q equations in (k-1)(n-1) unknowns, and is reduced once at the root by sparse elimination. The deadline is checked between equations.
- Search: every branching cell is undetermined by the system, so each decision lowers the dimension d of the residual solution space by exactly 1. The search depth is therefore at most d = dim{normalised solutions of the fibre-sum system}, and the number of nodes is at most (3^(d+1)-1)/2. Rainbow filtering usually prunes far more.
- Lower bound for d: d >= (k-1)(n-1) - (C(k,2) q - C(k-1,2)), because each pair 1 <= x < y gives one dependency among the equations. For 6x21 and 6x39 this gives d >= 5; for 8x57 it gives no bound beyond d >= 1.
- Each node costs O(k n * fibres per cell) for filtering, plus copying the reduced system (O(rank * d)).
- The budget is enforced with time.monotonic(): at every node, and between root equations.
