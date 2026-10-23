# Route C checker: OA strength 2 + CPro1 CFR for a raw (Z_n,k;1) difference matrix

Author: `ContinueCFR21.CheckerRouteC`, 2026-10-19 (host clock of the control run: 2026-10-19T01:37:23-0700).
Directory: `information-science/evidence/six-lane-20261018-96h/mols39/review/checker_c/`.
Frozen checker: `checker_c.py`, version 1, SHA-256 `5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7`.
Control run `control-run-1/results.json` (SHA-256 `67b412c14375a970c2d2ce464d208a2dfb044e59ce537f0f82c51fa0d30d4d77`): **22/22 cases matched their hand-derived
expectations**. All 7 positives exit 0 with PASS. All 4 well-formed negatives exit 1 with FAIL for the intended reason.
All 11 malformed or non-evaluable inputs exit 2 with the intended kind.

## 1. Independence and constraints

- I wrote this from the task-contract definitions only: the raw DM format, the DM definition, the MOLS bridge, and the
  CFR definition and bridge. The only other document I read was the managed process skill
  `finite-witness-triple-verification`, which is procedure guidance and contains no code for this problem.
- I opened no existing checker, encoder or search code. That covers everything under `.../cfr21/code` and
  `.../mols39/code`. The only probe outside `checker_c/` was a `test -d` existence test of the parent `review/`.
- Python 3 standard library only. Every file here was created with mode `x` (exclusive create) and never modified.
  No scratch files, no `/tmp`, no network, no other agents.
- Every test run was a plain `python3 -I -B ...` run under Python 3.14.3
  (`/opt/homebrew/opt/python@3.14/bin/python3.14`).

## 2. Files (SHA-256 in `manifest.json`)

| file | role |
|---|---|
| `checker_c.py` | the frozen checker |
| `make_controls.py` | builds `controls/`: 15 matrices plus `controls/expected.json`, which holds 22 cases with hand-derived expectations. It imports and runs no checker. |
| `controls/*.txt`, `controls/expected.json` | the control set (`expected.json` SHA-256 `2b8b81281917ac77d2f67640789a91b49363b08307a12dfd0c7f96266ab1cf5e`) |
| `run_controls.py` | replays every case as its own `python3 -I -B checker_c.py ...` process, with no timeout, and writes `<run>/results.json`. It compares the exit status, the single stdout JSON line, empty stderr, `file_sha256`, `checker_sha256` and the expected verdict fields. |
| `control-run-1/results.json` | the observed run: exit codes, verbatim verdict lines, and the problem list (empty for every case) |
| `control-run-1/receipt_P7.json` | the `--output` receipt written by case P7 (SHA-256 `950c22e0d49311483cb4b3e43e92e812414f741b501a4e066aab23e4537a6bfa`) |
| `make_manifest.py`, `manifest.json` | SHA-256 of every file in this directory |

## 3. Command, output and exit status

```
python3 -I -B checker_c.py --n 39 --k 7 --sha256 <pinned SHA-256> --output <new receipt path> <candidate file>
```

- **`--n` and `--k`** are mandatory integers, each at least 2. Nothing is inferred from the file, so a file of another
  shape is MALFORMED rather than evaluated at another order (control M7).
- **`--sha256 HEX`** is optional. If the file's SHA-256 differs, the verdict is `SHA256_MISMATCH` and nothing is
  evaluated (control M10).
- **`--output PATH`** is optional. The same JSON line is also written to PATH, which is created with mode `x`. If PATH
  already exists, the result is `USAGE_ERROR` (control M11).
- **stdout** is exactly one JSON line with sorted keys:
  - always: `checker`, `version`, `checker_sha256` (hash of the running checker file), `verdict`, `exit_code`;
  - after the command line parses: `file`, `n`, `k`;
  - once the file is read: `file_sha256`, `file_bytes`;
  - for well-formed input: `checks.{oa_strength2,cfr,dm_definition}`, `bridge_consistent`, `blank_lines_ignored`.
- **Exit status:**

| exit | verdict | meaning |
|---|---|---|
| `0` | `PASS` | the input is well-formed, all three checks PASS, and `bridge_consistent` is true |
| `1` | `FAIL` | the input is well-formed and at least one check fails |
| `2` | `MALFORMED`, `SHA256_MISMATCH` or `USAGE_ERROR` | the input could not be evaluated, or the `--output` file could not be created |
| `3` | `INTERNAL_ERROR` | an uncaught exception; it never yields 0 |

- **Acceptance rule for the parent:** require all of the following:
  - exit 0 and `"verdict":"PASS"`;
  - `"n":39` and `"k":7`;
  - `file_sha256` equal to the pinned hash;
  - `checker_sha256` equal to `5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7`.

## 4. Input grammar (exactly what is accepted)

1. If the file cannot be read, the verdict is `MALFORMED` with kind `UNREADABLE`. With `--sha256`, a hash mismatch is
   reported before any parsing.
2. Every byte must be below 0x80 (`NON_ASCII`). This also rejects Unicode digits such as U+FF13, which Python's
   `int()` would accept (control M6).
3. Lines are separated by LF, and a final LF ends the last line. CR, TAB, VT, FF and space are whitespace, so CRLF files
   are accepted (control P5).
4. A line holding only ASCII whitespace counts as empty. Empty lines are ignored and counted in `blank_lines_ignored`.
   This is the literal reading of "exactly k non-empty lines"; control P5 has 2 such lines.
5. There must be exactly k non-empty lines (`LINE_COUNT`). The i-th non-empty line (0-based) is row D_i, and its c-th
   token (0-based) is D_i(c).
6. The non-empty lines are checked in file order:
   - each must hold exactly n tokens (`TOKEN_COUNT`);
   - then, token by token, each token must be ASCII digits only (`NOT_INTEGER`, which covers signs, decimal points,
     letters and control bytes);
   - and each value must be below n (`OUT_OF_RANGE`).

   Leading zeros are accepted ("007" = 7). Reported line numbers are physical line numbers. The first violation in
   this order is the one reported.

## 5. Check `oa_strength2` (route C instead of building squares)

**Notation.**
- D_i(c), i = 0..k-1, c in Z_n, are the matrix entries.
- Delta_ij(c) = D_i(c) - D_j(c) mod n.
- The DM property says: for all i < j, Delta_ij is injective, which is the same as being a bijection of Z_n.

**The array.** A has one row for each (x, y) in Z_n x Z_n (n^2 rows) and **k+1 coordinates**:

    A(x, y) = ( x, D_0(x)+y, D_1(x)+y, ..., D_{k-1}(x)+y )  mod n

Coordinate 0 is x, and coordinate 1+i is D_i(x)+y for i = 0..k-1. The parameter y is **not** a coordinate.

**The test.**
- For each of the C(k+1,2) coordinate pairs (p,q) with p < q, a `bytearray(n*n)` counts the key a*n+b, where (a,b) is
  the row's value pair (A_p, A_q). Counts saturate at 2.
- The pair passes iff all n^2 counters equal 1, that is, every ordered pair of symbols occurs exactly once.
- Pairs that involve coordinate 0 hold for every D (see below). They are still checked, as a guard against
  implementation errors.
- For n = 39 and k = 7 this is 28 coordinate pairs over 1521 rows.

**Lemma 1 (pairs with coordinate 0).** For any D and any i, the rows with A_0 = a are exactly those with x = a. On
those rows A_{1+i} = D_i(a)+y takes every value of Z_n once as y does. So every (a,b) occurs exactly once.

**Lemma 2.** For i < j, (A_{1+i}, A_{1+j}) = (a,b) holds iff y = a - D_i(x) and Delta_ij(x) = a - b. So (a,b) occurs
exactly #{x : Delta_ij(x) = a-b} times. Every (a,b) occurs exactly once iff Delta_ij is a bijection. A failing pair
misses exactly n*(n - |image Delta_ij|) ordered pairs; this is the `missing_pairs` field.

**Theorem A.** A has strength 2 and index 1 iff D is a (Z_n,k;1) difference matrix. This follows from Lemmas 1 and 2.

**Theorem B (MOLS).**
- phi(x,y) = (x, D_0(x)+y) is a bijection of Z_n x Z_n, because for each fixed x the map y -> D_0(x)+y is one.
- Write (c,g) = phi(x,y). For t >= 1, D_t(x)+y = D_t(c) - D_0(c) + g = L_t[c][g], which is the contract's square.
- So the rows of A are exactly the n^2 tuples (c, g, L_1[c][g], ..., L_{k-1}[c][g]), one per cell.

The coordinate pairs then mean the following:

| coordinate pair (p,q) | (a,b) occurs ... times | "exactly once for all (a,b)" means | DM meaning |
|---|---|---|---|
| (0,1) | #{cell (c,g) = (a,b)} | always true | none |
| (0,1+t) | #{g : L_t[a][g] = b} | row a of L_t is a permutation (always true) | none |
| (1,1+t) | #{c : L_t[c][a] = b} | column a of L_t is a permutation | Delta_0t is a bijection |
| (1+t,1+u), 1 <= t < u | #{(c,g) : (L_t[c][g], L_u[c][g]) = (a,b)} | the n^2 superimposed ordered pairs are distinct (n^2 cells, n^2 pairs) | Delta_tu is a bijection |

So A has strength 2 iff L_1, ..., L_{k-1} are Latin and pairwise orthogonal. That means they are k-1 MOLS of order n in
the contract's sense, and by Theorem A this holds iff D is a DM. Each failing coordinate pair in the output states this
meaning in its `meaning` field.

**Why y is excluded.**
- If y were an extra coordinate, the pair (y, D_i(x)+y) would contain (a,b) exactly #{x : D_i(x) = b-a} times.
- Strength 2 would then also demand that every row D_i be a permutation of Z_n.
- That is not part of the DM definition. It fails for every normalised DM with D_0 = 0, as in P1, P2, P4 and N1-N4.
- It also fails for P3's D_0(c) = 6 + 3c^2 mod 13, which takes equal values at c and -c.
- This is a derivation; that variant was not run.
- With coordinate x and without y, the array has exactly k+1 coordinates, and its strength 2 is equivalent to the DM
  property.

## 6. Check `cfr` (CPro1 circular Florentine rectangle, as defined in the contract)

**Building the rows.**
- For t = 1..k-1, compute tau_t(s) = (D_t(s) - D_0(s)) mod n. Each symbol s is placed at position tau_t(s).
- Row t is a permutation iff every position receives exactly one symbol and the resulting list, sorted, equals 0..n-1.
- A row that fails is listed in `rows_not_permutation` with its numbers of empty and multiply filled positions, and
  CFR fails.

**The literal predicate.** For the rows that are permutations, the checker re-reads every symbol's position from the
row array and executes the quantifiers of the definition directly:
- for every ordered pair of distinct symbols (a,b) and every m in 1..n-1, it lists the rows with
  pos_t(b) = (pos_t(a) + m) mod n;
- two or more such rows is a conflict, recorded in `conflicting_triples`, `conflicting_row_pairs`, and up to 5
  `conflict_examples`.

PASS iff every row is a permutation and there is no conflict. For n = 39 this is 39*38*38 = 56316 triples.

**Theorem C.** The k-1 rows form a CFR(k-1, n) iff D is a DM.
- (i) Row t is a well-defined permutation iff tau_t is a bijection, iff Delta_0t is a bijection (DM pair (0,t)).
- (ii) Suppose rows t != u are permutations. Then pos_t = tau_t, and b is m steps to the right of a in row t iff
  tau_t(b) - tau_t(a) = m mod n. The following are equivalent:
  - rows t and u share a triple (a,b,m);
  - some a != b satisfy tau_t(b) - tau_t(a) = tau_u(b) - tau_u(a) (m != 0 is automatic, because tau_t is injective);
  - some a != b satisfy Delta_tu(a) = Delta_tu(b), because tau_t - tau_u = D_t - D_u;
  - DM pair (t,u) fails.
- The number of conflicting triples between rows t and u is sum_v mu_v(mu_v - 1), where mu_v = |Delta_tu^-1(v)|.
- Parts (i) and (ii) together cover every DM pair (0,t) and (t,u), which is the whole DM property.

**Orientation.** Reading "m steps to the left" instead of "to the right" replaces m by n-m. That is a bijection of
1..n-1, so the predicate does not depend on the direction convention.

## 7. Check `dm_definition` and the self-test `bridge_consistent`

**`dm_definition`.** For each i < j, the n values Delta_ij(c) must be pairwise distinct (`len(set(...)) == n`), which
is the literal definition. Failing pairs are reported with their number of distinct differences.

**`bridge_consistent`** is true iff all three of these hold:
- (a) the failing OA coordinate pairs are exactly {(1+i,1+j) : DM pair (i,j) fails}, so in particular no pair with
  coordinate 0 fails;
- (b) `rows_not_permutation` = {t : DM pair (0,t) fails};
- (c) `conflicting_row_pairs` = {(t,u) : 1 <= t < u, DM pair (t,u) fails, and rows t and u are permutations}.

Theorems A-C say it is always true, so false would expose an implementation defect. It is required for exit 0, and it
was true in every evaluated control.

## 8. What exit 0 proves, and what it does not

Exit 0 with `"verdict":"PASS"` covers the exact bytes whose SHA-256 is printed as `file_sha256`, parsed under section
4 with the declared n and k (for the target, n = 39 and k = 7). Computation plus the proofs above then establish:

1. D is a (Z_n,k;1) difference matrix. `dm_definition` checks this directly.
2. The array A has strength 2 and index 1. `oa_strength2` checks this directly.
   - By Theorem B, the arrays L_t[c][g] = (D_t(c) - D_0(c) + g) mod n, t = 1..k-1, are then k-1 mutually orthogonal
     Latin squares of order n. For the target that is **six MOLS of order 39**.
   - The only step not executed is the re-indexing bijection phi of Theorem B, which is proved above.
3. The k-1 rows of the contract's inverse-permutation bridge form a CFR(k-1, n) under the definition as worded in the
   contract (CFR(6,39) for the target). `cfr` checks this directly.

It does **not** establish:
- that the contract's wording of the CFR definition matches CPro1's own code (CPro1 was not consulted);
- independence among the three checks. They are mathematically equivalent (Theorems A-C) and share one parser and one
  author, so they diversify implementation, not mathematics. Independence holds only relative to the other route.
- anything about how the candidate was found, about other files, or about novelty or priority;
- the correctness of the Python interpreter or the hardware. Nothing here is Lean-checked.

## 9. Controls and observed outcomes (`control-run-1`)

The command `python3 -I -B run_controls.py control-run-1` ran from 2026-10-19T01:37:23-0700 to 2026-10-19T01:37:24-0700 and printed
`ALL_OK 22/22 cases match`.

| ID | task ref | arguments | exit | verdict | observed (which check fails, or why the input was refused) | matches expectation |
|---|---|---|---|---|---|---|
| P1 | positive Z_7 | `--n 7 --k 7 controls/pos1_z7_k7_linear.txt` | 0 | PASS | oa_strength2/cfr/dm_definition PASS (28 coordinate pairs, 252 CFR triples, 21 DM row pairs); blank_lines_ignored=0 | yes |
| P2 | positive Z_13 | `--n 13 --k 7 controls/pos2_z13_k7_linear.txt` | 0 | PASS | oa_strength2/cfr/dm_definition PASS (28 coordinate pairs, 1872 CFR triples, 21 DM row pairs); blank_lines_ignored=0 | yes |
| P3 | extra | `--n 13 --k 7 controls/pos3_z13_k7_shifted.txt` | 0 | PASS | oa_strength2/cfr/dm_definition PASS (28 coordinate pairs, 1872 CFR triples, 21 DM row pairs); blank_lines_ignored=0 | yes |
| P4 | extra | `--n 39 --k 3 controls/pos4_z39_k3_linear.txt` | 0 | PASS | oa_strength2/cfr/dm_definition PASS (6 coordinate pairs, 56316 CFR triples, 3 DM row pairs); blank_lines_ignored=0 | yes |
| P5 | extra | `--n 7 --k 7 controls/pos5_z7_k7_layout.txt` | 0 | PASS | oa_strength2/cfr/dm_definition PASS (28 coordinate pairs, 252 CFR triples, 21 DM row pairs); blank_lines_ignored=2 | yes |
| P6 | extra | `--n 13 --k 7 --sha256 757f100a648fd78dd59bdf27f1a51e4019979dea98f8986f18a4c601e3d07b8a controls/pos2_z13_k7_linear.txt` | 0 | PASS | oa_strength2/cfr/dm_definition PASS (28 coordinate pairs, 1872 CFR triples, 21 DM row pairs); blank_lines_ignored=0 | yes |
| P7 | extra | `--n 7 --k 7 --output control-run-1/receipt_P7.json controls/pos1_z7_k7_linear.txt` | 0 | PASS | oa_strength2/cfr/dm_definition PASS (28 coordinate pairs, 252 CFR triples, 21 DM row pairs); blank_lines_ignored=0 | yes |
| N1 | (i) | `--n 13 --k 7 controls/negi_z13_k7_swap.txt` | 1 | FAIL | all three FAIL; DM pairs (1,3),(2,3),(3,4),(3,5),(3,6) (distinct 11); OA coords (2,4),(3,4),(4,5),(4,6),(4,7) (missing 26); CFR non-permutation rows none, conflicting rows (1,3),(2,3),(3,4),(3,5),(3,6), 20 triples; bridge_consistent=true | yes |
| N2 | (ii) | `--n 13 --k 7 controls/negii_z13_k7_single_entry.txt` | 1 | FAIL | all three FAIL; DM pairs (0,5),(1,5),(2,5),(3,5),(4,5),(5,6) (distinct 12); OA coords (1,6),(2,6),(3,6),(4,6),(5,6),(6,7) (missing 13); CFR non-permutation rows 5, conflicting rows none, 0 triples; bridge_consistent=true | yes |
| N3 | (iii) | `--n 9 --k 4 controls/negiii_z9_k4_mult0124.txt` | 1 | FAIL | all three FAIL; DM pairs (1,3) (distinct 3); OA coords (2,4) (missing 54); CFR non-permutation rows none, conflicting rows (1,3), 18 triples; bridge_consistent=true | yes |
| N4 | extra | `--n 39 --k 7 controls/negx_z39_k7_linear.txt` | 1 | FAIL | all three FAIL; DM pairs (0,3),(0,6),(1,4),(2,5),(3,6) (distinct 13); OA coords (1,4),(1,7),(2,5),(3,6),(4,7) (missing 1014); CFR non-permutation rows 3,6, conflicting rows (1,4),(2,5), 156 triples; bridge_consistent=true | yes |
| M1 | (iv) | `--n 13 --k 7 controls/maliv_a_short_row.txt` | 2 | MALFORMED | TOKEN_COUNT (line 3): line 3: expected exactly 13 integers, found 12 tokens | yes |
| M2 | (iv) | `--n 13 --k 7 controls/maliv_b_out_of_range.txt` | 2 | MALFORMED | OUT_OF_RANGE (line 4): line 4 token 5 '13' is not in [0, 13) | yes |
| M3 | (iv) | `--n 13 --k 7 controls/maliv_c_negative_token.txt` | 2 | MALFORMED | NOT_INTEGER (line 2): line 2 token 2 '-1' is not an unsigned decimal integer | yes |
| M4 | (iv) | `--n 13 --k 7 controls/maliv_d_missing_line.txt` | 2 | MALFORMED | LINE_COUNT (line None): expected exactly 7 non-empty lines, found 6 | yes |
| M5 | (iv) | `--n 13 --k 7 controls/maliv_e_extra_line.txt` | 2 | MALFORMED | LINE_COUNT (line None): expected exactly 7 non-empty lines, found 8 | yes |
| M6 | (iv) | `--n 13 --k 7 controls/maliv_f_fullwidth_digit.txt` | 2 | MALFORMED | NON_ASCII (line None): byte offset 117 holds 0xef, which is not ASCII | yes |
| M7 | (iv) | `--n 13 --k 7 controls/pos1_z7_k7_linear.txt` | 2 | MALFORMED | TOKEN_COUNT (line 1): line 1: expected exactly 13 integers, found 7 tokens | yes |
| M8 | (iv) | `--n 13 --k 7 controls/absent_never_created.txt` | 2 | MALFORMED | UNREADABLE (line None): FileNotFoundError: [Errno 2] No such file or directory: 'controls/absent_never_created.txt' | yes |
| M9 | extra | `--n 13 controls/pos2_z13_k7_linear.txt` | 2 | USAGE_ERROR | usage: checker_c.py --n N --k K [--sha256 HEX] [--output NEW_PATH] FILE | yes |
| M10 | extra | `--n 13 --k 7 --sha256 0000000000000000000000000000000000000000000000000000000000000000 controls/pos2_z13_k7_linear.txt` | 2 | SHA256_MISMATCH | file_sha256 757f100a648f... != expected 000000000000... | yes |
| M11 | extra | `--n 7 --k 7 --output control-run-1/receipt_P7.json controls/pos1_z7_k7_linear.txt` | 2 | USAGE_ERROR | --output 'control-run-1/receipt_P7.json' already exists; refusing to overwrite | yes |

### Hand derivations of the intended reasons

These were derived by hand and written into `controls/expected.json` before any checker run.

- **P1, P2 (task positives):** D_a(c) = a*c mod p for a = 0..6 and p in {7, 13}. Then Delta_ab(c) = (a-b)c, and a-b is
  a unit mod p, so every Delta is a bijection.
- **Extra positives:**
  - P4 is the same construction over Z_39 with a in {0,1,2}; the differences 1 and 2 are units mod 39.
  - P3 is P2 with r_i + s_c added; this changes Delta_ij only by the constant r_i - r_j.
  - P5 is P1's matrix in another layout.
  - P6 and P7 exercise `--sha256` and `--output`.
- **N1 (i), swap D_3(1)=3 and D_3(2)=6 in P2:**
  - Delta_03 = -D_3 is still a bijection, so pair (0,3) stays intact.
  - For j in {1,2,4,5,6}, Delta_3j(c) = (3-j)c was a bijection. After the swap, its values at c = 1 and c = 2 are 6-j
    and 3-2j.
  - 6-j would need j = 0 to equal an old value at c = 1 or 2, and so would 3-2j. The two new values are equal only if
    j = 10 mod 13.
  - So each new value collides with a different untouched column. That gives 2 collisions, 11 distinct differences,
    2*13 = 26 missing OA pairs, and 2*2 = 4 CFR triples per pair, so 5*4 = 20 triples in total.
- **N2 (ii), single entry D_5(4): 7 -> 8 in P2:**
  - For every j != 5, Delta_5j changes only at c = 4, by +1. Because it was a bijection, the new value repeats exactly
    one other column's value.
  - That gives 6 failing pairs, each with 12 distinct differences and 13 missing OA pairs.
  - tau_5 = D_5 (since D_0 = 0) now misses 7 and hits 8 twice. So CFR row 5 is not a permutation: 1 empty position
    and 1 doubly filled position.
  - All pairs among rows 1, 2, 3, 4 and 6 are intact, so there are 0 conflicting triples.
- **N3 (iii), Z_9 rows 0, x, 2x, 4x with k = 4:**
  - The multiplier differences are 1, 2, 4, 1, 3, 2. Only 4-1 = 3 is a zero divisor mod 9.
  - Delta_13 = -3x takes the values 0, 3 and 6, three times each. That gives 3 distinct differences, 6*9 = 54 missing OA
    pairs, and 3*3*2 = 18 CFR triples between rows 1 and 3.
  - tau_1, tau_2 and tau_3 are permutations, so all three squares are Latin; only L_1 and L_3 are not orthogonal.
- **N4 (extra, target shape n=39, k=7), multipliers 0..6 over Z_39:**
  - Delta_ij = (i-j)x is a bijection iff gcd(i-j, 39) = 1, which for |i-j| <= 6 means 3 does not divide i-j.
  - The failing pairs are those with i-j in {3,6}: (0,3), (1,4), (2,5), (3,6) and (0,6). Each Delta has the 13
    multiples of 3 as its image, giving 13 distinct differences and 26*39 = 1014 missing OA pairs.
  - CFR rows 3 and 6 (tau = 3x and 6x) are not permutations.
  - Among rows 1, 2, 4 and 5, only (1,4) and (2,5) conflict, with 13*3*2 = 78 triples each, so 156 in total.
- **M1-M8 (iv):** each file has one grammar violation, located as shown in the table. M7 is a valid Z_7 file declared
  as n = 13. M8 is a path that was never created.
- **M9-M11 (extra, command line):**
  - M9 omits `--k`.
  - M10 passes a wrong `--sha256`.
  - M11 passes `--output` pointing at P7's existing receipt. The runner confirmed afterwards that the receipt is still
    byte-identical to P7's stdout.

There is no n=39, k=7 positive. Multiplier (linear) constructions over Z_39 give at most 3 rows, because the
multipliers must be distinct mod 3. The n=39 positive is therefore P4 with k=3, and the k=7 positives are over Z_7 and
Z_13. N4 exercises the exact target command shape on a well-formed non-DM.

## 10. Reproduce

```
cd /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/checker_c
python3 -I -B run_controls.py control-run-2     # needs a new run directory each time; expect ALL_OK 22/22
python3 -I -B checker_c.py --n 39 --k 7 --sha256 <pinned hash> --output <new receipt path> <candidate file>
```

- `make_controls.py` will not run again here, because `controls/` already exists.
- The whole 22-case replay took about 1 s.

## Appendix: verbatim verdict lines (stdout of each case in `control-run-1`)

```
# P1 exit=0
{"blank_lines_ignored":0,"bridge_consistent":true,"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","checks":{"cfr":{"bridge":"row t (t=1..6) holds at position p the symbol s with (D_t(s)-D_0(s)) mod 7 = p","conflict_examples":[],"conflicting_row_pairs":[],"conflicting_triples":0,"rows":6,"rows_not_permutation":[],"rows_tested_for_triples":[1,2,3,4,5,6],"triples_tested":252,"verdict":"PASS"},"dm_definition":{"failing_row_pairs":[],"row_pairs_checked":21,"verdict":"PASS"},"oa_strength2":{"array":"A(x,y) = (x, D_0(x)+y, ..., D_6(x)+y) mod 7, (x,y) in Z_7^2","coordinate_pairs_checked":28,"coordinates":8,"failing_coordinate_pairs":[],"rows":49,"verdict":"PASS"}},"exit_code":0,"file":"controls/pos1_z7_k7_linear.txt","file_bytes":98,"file_sha256":"47c70a5729450457e96dfa56a69fbb06aa1f4e25ea35e343067e402aaec6ddf5","k":7,"n":7,"verdict":"PASS","version":1}
# P2 exit=0
{"blank_lines_ignored":0,"bridge_consistent":true,"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","checks":{"cfr":{"bridge":"row t (t=1..6) holds at position p the symbol s with (D_t(s)-D_0(s)) mod 13 = p","conflict_examples":[],"conflicting_row_pairs":[],"conflicting_triples":0,"rows":6,"rows_not_permutation":[],"rows_tested_for_triples":[1,2,3,4,5,6],"triples_tested":1872,"verdict":"PASS"},"dm_definition":{"failing_row_pairs":[],"row_pairs_checked":21,"verdict":"PASS"},"oa_strength2":{"array":"A(x,y) = (x, D_0(x)+y, ..., D_6(x)+y) mod 13, (x,y) in Z_13^2","coordinate_pairs_checked":28,"coordinates":8,"failing_coordinate_pairs":[],"rows":169,"verdict":"PASS"}},"exit_code":0,"file":"controls/pos2_z13_k7_linear.txt","file_bytes":200,"file_sha256":"757f100a648fd78dd59bdf27f1a51e4019979dea98f8986f18a4c601e3d07b8a","k":7,"n":13,"verdict":"PASS","version":1}
# P3 exit=0
{"blank_lines_ignored":0,"bridge_consistent":true,"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","checks":{"cfr":{"bridge":"row t (t=1..6) holds at position p the symbol s with (D_t(s)-D_0(s)) mod 13 = p","conflict_examples":[],"conflicting_row_pairs":[],"conflicting_triples":0,"rows":6,"rows_not_permutation":[],"rows_tested_for_triples":[1,2,3,4,5,6],"triples_tested":1872,"verdict":"PASS"},"dm_definition":{"failing_row_pairs":[],"row_pairs_checked":21,"verdict":"PASS"},"oa_strength2":{"array":"A(x,y) = (x, D_0(x)+y, ..., D_6(x)+y) mod 13, (x,y) in Z_13^2","coordinate_pairs_checked":28,"coordinates":8,"failing_coordinate_pairs":[],"rows":169,"verdict":"PASS"}},"exit_code":0,"file":"controls/pos3_z13_k7_shifted.txt","file_bytes":204,"file_sha256":"3fe37c1f1cd7b8c34671d767b006c4a0b5b0ca9bf1281dad39839acdb68b14d9","k":7,"n":13,"verdict":"PASS","version":1}
# P4 exit=0
{"blank_lines_ignored":0,"bridge_consistent":true,"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","checks":{"cfr":{"bridge":"row t (t=1..2) holds at position p the symbol s with (D_t(s)-D_0(s)) mod 39 = p","conflict_examples":[],"conflicting_row_pairs":[],"conflicting_triples":0,"rows":2,"rows_not_permutation":[],"rows_tested_for_triples":[1,2],"triples_tested":56316,"verdict":"PASS"},"dm_definition":{"failing_row_pairs":[],"row_pairs_checked":3,"verdict":"PASS"},"oa_strength2":{"array":"A(x,y) = (x, D_0(x)+y, ..., D_2(x)+y) mod 39, (x,y) in Z_39^2","coordinate_pairs_checked":6,"coordinates":4,"failing_coordinate_pairs":[],"rows":1521,"verdict":"PASS"}},"exit_code":0,"file":"controls/pos4_z39_k3_linear.txt","file_bytes":292,"file_sha256":"82ec424c47883e7b824f234912edeca16058839391d7ed38383d7bb036572b8d","k":3,"n":39,"verdict":"PASS","version":1}
# P5 exit=0
{"blank_lines_ignored":2,"bridge_consistent":true,"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","checks":{"cfr":{"bridge":"row t (t=1..6) holds at position p the symbol s with (D_t(s)-D_0(s)) mod 7 = p","conflict_examples":[],"conflicting_row_pairs":[],"conflicting_triples":0,"rows":6,"rows_not_permutation":[],"rows_tested_for_triples":[1,2,3,4,5,6],"triples_tested":252,"verdict":"PASS"},"dm_definition":{"failing_row_pairs":[],"row_pairs_checked":21,"verdict":"PASS"},"oa_strength2":{"array":"A(x,y) = (x, D_0(x)+y, ..., D_6(x)+y) mod 7, (x,y) in Z_7^2","coordinate_pairs_checked":28,"coordinates":8,"failing_coordinate_pairs":[],"rows":49,"verdict":"PASS"}},"exit_code":0,"file":"controls/pos5_z7_k7_layout.txt","file_bytes":116,"file_sha256":"f9aa334e4c3cba659cb5ce0fa0706d7f8101622e5b06d295e9448bf16cc7dd0f","k":7,"n":7,"verdict":"PASS","version":1}
# P6 exit=0
{"blank_lines_ignored":0,"bridge_consistent":true,"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","checks":{"cfr":{"bridge":"row t (t=1..6) holds at position p the symbol s with (D_t(s)-D_0(s)) mod 13 = p","conflict_examples":[],"conflicting_row_pairs":[],"conflicting_triples":0,"rows":6,"rows_not_permutation":[],"rows_tested_for_triples":[1,2,3,4,5,6],"triples_tested":1872,"verdict":"PASS"},"dm_definition":{"failing_row_pairs":[],"row_pairs_checked":21,"verdict":"PASS"},"oa_strength2":{"array":"A(x,y) = (x, D_0(x)+y, ..., D_6(x)+y) mod 13, (x,y) in Z_13^2","coordinate_pairs_checked":28,"coordinates":8,"failing_coordinate_pairs":[],"rows":169,"verdict":"PASS"}},"exit_code":0,"expected_sha256":"757f100a648fd78dd59bdf27f1a51e4019979dea98f8986f18a4c601e3d07b8a","file":"controls/pos2_z13_k7_linear.txt","file_bytes":200,"file_sha256":"757f100a648fd78dd59bdf27f1a51e4019979dea98f8986f18a4c601e3d07b8a","k":7,"n":13,"verdict":"PASS","version":1}
# P7 exit=0
{"blank_lines_ignored":0,"bridge_consistent":true,"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","checks":{"cfr":{"bridge":"row t (t=1..6) holds at position p the symbol s with (D_t(s)-D_0(s)) mod 7 = p","conflict_examples":[],"conflicting_row_pairs":[],"conflicting_triples":0,"rows":6,"rows_not_permutation":[],"rows_tested_for_triples":[1,2,3,4,5,6],"triples_tested":252,"verdict":"PASS"},"dm_definition":{"failing_row_pairs":[],"row_pairs_checked":21,"verdict":"PASS"},"oa_strength2":{"array":"A(x,y) = (x, D_0(x)+y, ..., D_6(x)+y) mod 7, (x,y) in Z_7^2","coordinate_pairs_checked":28,"coordinates":8,"failing_coordinate_pairs":[],"rows":49,"verdict":"PASS"}},"exit_code":0,"file":"controls/pos1_z7_k7_linear.txt","file_bytes":98,"file_sha256":"47c70a5729450457e96dfa56a69fbb06aa1f4e25ea35e343067e402aaec6ddf5","k":7,"n":7,"verdict":"PASS","version":1}
# N1 exit=1
{"blank_lines_ignored":0,"bridge_consistent":true,"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","checks":{"cfr":{"bridge":"row t (t=1..6) holds at position p the symbol s with (D_t(s)-D_0(s)) mod 13 = p","conflict_examples":[{"a":0,"b":1,"m":6,"rows":[3,6]},{"a":1,"b":0,"m":7,"rows":[3,6]},{"a":1,"b":4,"m":6,"rows":[2,3]},{"a":1,"b":6,"m":12,"rows":[3,5]},{"a":1,"b":9,"m":8,"rows":[1,3]}],"conflicting_row_pairs":[[1,3],[2,3],[3,4],[3,5],[3,6]],"conflicting_triples":20,"rows":6,"rows_not_permutation":[],"rows_tested_for_triples":[1,2,3,4,5,6],"triples_tested":1872,"verdict":"FAIL"},"dm_definition":{"failing_row_pairs":[{"distinct_differences":11,"rows":[1,3]},{"distinct_differences":11,"rows":[2,3]},{"distinct_differences":11,"rows":[3,4]},{"distinct_differences":11,"rows":[3,5]},{"distinct_differences":11,"rows":[3,6]}],"row_pairs_checked":21,"verdict":"FAIL"},"oa_strength2":{"array":"A(x,y) = (x, D_0(x)+y, ..., D_6(x)+y) mod 13, (x,y) in Z_13^2","coordinate_pairs_checked":28,"coordinates":8,"failing_coordinate_pairs":[{"coordinates":[2,4],"meaning":"L_1 orthogonal to L_3 <=> DM rows (1,3)","missing_pairs":26,"pairs_exactly_once":117,"repeated_pairs":26},{"coordinates":[3,4],"meaning":"L_2 orthogonal to L_3 <=> DM rows (2,3)","missing_pairs":26,"pairs_exactly_once":117,"repeated_pairs":26},{"coordinates":[4,5],"meaning":"L_3 orthogonal to L_4 <=> DM rows (3,4)","missing_pairs":26,"pairs_exactly_once":117,"repeated_pairs":26},{"coordinates":[4,6],"meaning":"L_3 orthogonal to L_5 <=> DM rows (3,5)","missing_pairs":26,"pairs_exactly_once":117,"repeated_pairs":26},{"coordinates":[4,7],"meaning":"L_3 orthogonal to L_6 <=> DM rows (3,6)","missing_pairs":26,"pairs_exactly_once":117,"repeated_pairs":26}],"rows":169,"verdict":"FAIL"}},"exit_code":1,"file":"controls/negi_z13_k7_swap.txt","file_bytes":200,"file_sha256":"2525f79c5eff6afdb6db6a2aeb87a8ece9217d76927a503bc35d6373dd9f2c19","k":7,"n":13,"verdict":"FAIL","version":1}
# N2 exit=1
{"blank_lines_ignored":0,"bridge_consistent":true,"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","checks":{"cfr":{"bridge":"row t (t=1..6) holds at position p the symbol s with (D_t(s)-D_0(s)) mod 13 = p","conflict_examples":[],"conflicting_row_pairs":[],"conflicting_triples":0,"rows":6,"rows_not_permutation":[{"empty_positions":1,"multiply_filled_positions":1,"row":5}],"rows_tested_for_triples":[1,2,3,4,6],"triples_tested":1872,"verdict":"FAIL"},"dm_definition":{"failing_row_pairs":[{"distinct_differences":12,"rows":[0,5]},{"distinct_differences":12,"rows":[1,5]},{"distinct_differences":12,"rows":[2,5]},{"distinct_differences":12,"rows":[3,5]},{"distinct_differences":12,"rows":[4,5]},{"distinct_differences":12,"rows":[5,6]}],"row_pairs_checked":21,"verdict":"FAIL"},"oa_strength2":{"array":"A(x,y) = (x, D_0(x)+y, ..., D_6(x)+y) mod 13, (x,y) in Z_13^2","coordinate_pairs_checked":28,"coordinates":8,"failing_coordinate_pairs":[{"coordinates":[1,6],"meaning":"columns of L_5 are permutations <=> DM rows (0,5)","missing_pairs":13,"pairs_exactly_once":143,"repeated_pairs":13},{"coordinates":[2,6],"meaning":"L_1 orthogonal to L_5 <=> DM rows (1,5)","missing_pairs":13,"pairs_exactly_once":143,"repeated_pairs":13},{"coordinates":[3,6],"meaning":"L_2 orthogonal to L_5 <=> DM rows (2,5)","missing_pairs":13,"pairs_exactly_once":143,"repeated_pairs":13},{"coordinates":[4,6],"meaning":"L_3 orthogonal to L_5 <=> DM rows (3,5)","missing_pairs":13,"pairs_exactly_once":143,"repeated_pairs":13},{"coordinates":[5,6],"meaning":"L_4 orthogonal to L_5 <=> DM rows (4,5)","missing_pairs":13,"pairs_exactly_once":143,"repeated_pairs":13},{"coordinates":[6,7],"meaning":"L_5 orthogonal to L_6 <=> DM rows (5,6)","missing_pairs":13,"pairs_exactly_once":143,"repeated_pairs":13}],"rows":169,"verdict":"FAIL"}},"exit_code":1,"file":"controls/negii_z13_k7_single_entry.txt","file_bytes":200,"file_sha256":"9040dc37fc2ca54a19a978232bed302aceb6c288a223f3727f6ac70569454f28","k":7,"n":13,"verdict":"FAIL","version":1}
# N3 exit=1
{"blank_lines_ignored":0,"bridge_consistent":true,"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","checks":{"cfr":{"bridge":"row t (t=1..3) holds at position p the symbol s with (D_t(s)-D_0(s)) mod 9 = p","conflict_examples":[{"a":0,"b":3,"m":3,"rows":[1,3]},{"a":0,"b":6,"m":6,"rows":[1,3]},{"a":1,"b":4,"m":3,"rows":[1,3]},{"a":1,"b":7,"m":6,"rows":[1,3]},{"a":2,"b":5,"m":3,"rows":[1,3]}],"conflicting_row_pairs":[[1,3]],"conflicting_triples":18,"rows":3,"rows_not_permutation":[],"rows_tested_for_triples":[1,2,3],"triples_tested":576,"verdict":"FAIL"},"dm_definition":{"failing_row_pairs":[{"distinct_differences":3,"rows":[1,3]}],"row_pairs_checked":6,"verdict":"FAIL"},"oa_strength2":{"array":"A(x,y) = (x, D_0(x)+y, ..., D_3(x)+y) mod 9, (x,y) in Z_9^2","coordinate_pairs_checked":10,"coordinates":5,"failing_coordinate_pairs":[{"coordinates":[2,4],"meaning":"L_1 orthogonal to L_3 <=> DM rows (1,3)","missing_pairs":54,"pairs_exactly_once":0,"repeated_pairs":27}],"rows":81,"verdict":"FAIL"}},"exit_code":1,"file":"controls/negiii_z9_k4_mult0124.txt","file_bytes":72,"file_sha256":"4fd0ee5c716ac47c2f95f35579ef834f93b10cfaa0eb2db17e8594abb84c4b81","k":4,"n":9,"verdict":"FAIL","version":1}
# N4 exit=1
{"blank_lines_ignored":0,"bridge_consistent":true,"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","checks":{"cfr":{"bridge":"row t (t=1..6) holds at position p the symbol s with (D_t(s)-D_0(s)) mod 39 = p","conflict_examples":[{"a":0,"b":13,"m":13,"rows":[1,4]},{"a":0,"b":13,"m":26,"rows":[2,5]},{"a":0,"b":26,"m":13,"rows":[2,5]},{"a":0,"b":26,"m":26,"rows":[1,4]},{"a":1,"b":14,"m":13,"rows":[1,4]}],"conflicting_row_pairs":[[1,4],[2,5]],"conflicting_triples":156,"rows":6,"rows_not_permutation":[{"empty_positions":26,"multiply_filled_positions":13,"row":3},{"empty_positions":26,"multiply_filled_positions":13,"row":6}],"rows_tested_for_triples":[1,2,4,5],"triples_tested":56316,"verdict":"FAIL"},"dm_definition":{"failing_row_pairs":[{"distinct_differences":13,"rows":[0,3]},{"distinct_differences":13,"rows":[0,6]},{"distinct_differences":13,"rows":[1,4]},{"distinct_differences":13,"rows":[2,5]},{"distinct_differences":13,"rows":[3,6]}],"row_pairs_checked":21,"verdict":"FAIL"},"oa_strength2":{"array":"A(x,y) = (x, D_0(x)+y, ..., D_6(x)+y) mod 39, (x,y) in Z_39^2","coordinate_pairs_checked":28,"coordinates":8,"failing_coordinate_pairs":[{"coordinates":[1,4],"meaning":"columns of L_3 are permutations <=> DM rows (0,3)","missing_pairs":1014,"pairs_exactly_once":0,"repeated_pairs":507},{"coordinates":[1,7],"meaning":"columns of L_6 are permutations <=> DM rows (0,6)","missing_pairs":1014,"pairs_exactly_once":0,"repeated_pairs":507},{"coordinates":[2,5],"meaning":"L_1 orthogonal to L_4 <=> DM rows (1,4)","missing_pairs":1014,"pairs_exactly_once":0,"repeated_pairs":507},{"coordinates":[3,6],"meaning":"L_2 orthogonal to L_5 <=> DM rows (2,5)","missing_pairs":1014,"pairs_exactly_once":0,"repeated_pairs":507},{"coordinates":[4,7],"meaning":"L_3 orthogonal to L_6 <=> DM rows (3,6)","missing_pairs":1014,"pairs_exactly_once":0,"repeated_pairs":507}],"rows":1521,"verdict":"FAIL"}},"exit_code":1,"file":"controls/negx_z39_k7_linear.txt","file_bytes":716,"file_sha256":"9f7696d47d02e78dc83e30bc4472197a2f5d1f17a7f5b2e0de3711a79a2a41d4","k":7,"n":39,"verdict":"FAIL","version":1}
# M1 exit=2
{"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","exit_code":2,"file":"controls/maliv_a_short_row.txt","file_bytes":197,"file_sha256":"91bdf1c036606bf010c1fc96e292bf69c81d7c84ff73ab2d23a928f9f1520c05","k":7,"malformed":{"detail":"line 3: expected exactly 13 integers, found 12 tokens","kind":"TOKEN_COUNT","line":3},"n":13,"verdict":"MALFORMED","version":1}
# M2 exit=2
{"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","exit_code":2,"file":"controls/maliv_b_out_of_range.txt","file_bytes":200,"file_sha256":"5d5ae9e5e85d94152c0d880cdfaf456e69ce3f054d4df9ae796aec5762a091ca","k":7,"malformed":{"detail":"line 4 token 5 '13' is not in [0, 13)","kind":"OUT_OF_RANGE","line":4},"n":13,"verdict":"MALFORMED","version":1}
# M3 exit=2
{"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","exit_code":2,"file":"controls/maliv_c_negative_token.txt","file_bytes":201,"file_sha256":"9210907e0c0e71ea91cba09ec649c5ba9da2ad8ba57324f93f61688f5e0f2047","k":7,"malformed":{"detail":"line 2 token 2 '-1' is not an unsigned decimal integer","kind":"NOT_INTEGER","line":2},"n":13,"verdict":"MALFORMED","version":1}
# M4 exit=2
{"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","exit_code":2,"file":"controls/maliv_d_missing_line.txt","file_bytes":171,"file_sha256":"18181cc12abfe8612ff6eedc02d204b7624265313d72ccc60aaec568102f8450","k":7,"malformed":{"detail":"expected exactly 7 non-empty lines, found 6","kind":"LINE_COUNT","line":null},"n":13,"verdict":"MALFORMED","version":1}
# M5 exit=2
{"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","exit_code":2,"file":"controls/maliv_e_extra_line.txt","file_bytes":229,"file_sha256":"c39ed2038a87fd1400c0d9e242acf58c8d60d3aa8a620f6e482b2e1d4718d104","k":7,"malformed":{"detail":"expected exactly 7 non-empty lines, found 8","kind":"LINE_COUNT","line":null},"n":13,"verdict":"MALFORMED","version":1}
# M6 exit=2
{"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","exit_code":2,"file":"controls/maliv_f_fullwidth_digit.txt","file_bytes":202,"file_sha256":"6599e3bca82542041d28bec35d08b3eda6331bd29ca0940fb14b02d6def2765b","k":7,"malformed":{"detail":"byte offset 117 holds 0xef, which is not ASCII","kind":"NON_ASCII","line":null},"n":13,"verdict":"MALFORMED","version":1}
# M7 exit=2
{"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","exit_code":2,"file":"controls/pos1_z7_k7_linear.txt","file_bytes":98,"file_sha256":"47c70a5729450457e96dfa56a69fbb06aa1f4e25ea35e343067e402aaec6ddf5","k":7,"malformed":{"detail":"line 1: expected exactly 13 integers, found 7 tokens","kind":"TOKEN_COUNT","line":1},"n":13,"verdict":"MALFORMED","version":1}
# M8 exit=2
{"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","exit_code":2,"file":"controls/absent_never_created.txt","k":7,"malformed":{"detail":"FileNotFoundError: [Errno 2] No such file or directory: 'controls/absent_never_created.txt'","kind":"UNREADABLE","line":null},"n":13,"verdict":"MALFORMED","version":1}
# M9 exit=2
{"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","detail":"usage: checker_c.py --n N --k K [--sha256 HEX] [--output NEW_PATH] FILE","exit_code":2,"verdict":"USAGE_ERROR","version":1}
# M10 exit=2
{"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","exit_code":2,"expected_sha256":"0000000000000000000000000000000000000000000000000000000000000000","file":"controls/pos2_z13_k7_linear.txt","file_bytes":200,"file_sha256":"757f100a648fd78dd59bdf27f1a51e4019979dea98f8986f18a4c601e3d07b8a","k":7,"n":13,"verdict":"SHA256_MISMATCH","version":1}
# M11 exit=2
{"checker":"checker_c","checker_sha256":"5b88e457d9dca0531c9c6e8e40d19a29539b981f7f59c82982d6ac05a30436d7","detail":"--output 'control-run-1/receipt_P7.json' already exists; refusing to overwrite","exit_code":2,"verdict":"USAGE_ERROR","version":1}
```
