# checker_b: route B (explicit MOLS) for raw (Z_n,k;1) difference matrices

## Provenance and independence

- Written 2026-10-19 by `ContinueCFR21.CheckerRouteB`, using only the contract definitions in the task.
  I read no other checker, encoder or search code: nothing under `cfr21/code` or `mols39/code`, and nothing outside this directory.
- Python 3 standard library only, no network.
- Every file here is new. Authored files were created fresh. Generated files were opened with mode `'x'`/`'xb'`.
  Nothing was modified or deleted.
- Runs used `python3 -I -B` (Python 3.14.3, `/opt/homebrew/opt/python@3.14/bin/python3.14`).

## Frozen checker

`checker_b.py`, version 1.
SHA-256 `a9b839e93ada46fc237305dc0d81e146c1b1ae053cdf413b4f68e82bf55670d7`.
The checker prints its own hash in every output line (`checker_sha256`).

```
python3 -I -B checker_b.py CANDIDATE --n 39 --k 7 [--emit NEW_DIR/squares.txt]
```

**Output.** Exactly one JSON line. It contains:

- `verdict`: PASS, FAIL, MALFORMED or ERROR;
- `verdicts`: the per-property verdicts for `dm`, `latin` and `orthogonal`;
- `properties`: failing sets, plus at most 8 witnesses per property;
- `diagnostics.bridge_agreement`;
- `input_sha256`.

**Exit status.**

| Exit | Verdict | When |
|---|---|---|
| 0 | PASS | All three properties pass. |
| 1 | FAIL | At least one property fails. |
| 2 | MALFORMED | Unreadable input, input outside the grammar, an `--n`/`--k` mismatch, or a bad command line. |
| 3 | ERROR | The `--emit` file cannot be created or written, or an internal exception occurred. |

Exit 3 was added so that a crash can never look like PASS or FAIL. With exit 2 or 3, no property verdict is reported.

**`--emit PATH`.** Requires a new file and opens it with mode `'xb'`, so an existing file is refused and left untouched.

- **Layout:** L_1 … L_{k-1} in order. Each square is n lines of n space-separated integers. One blank line separates consecutive squares, and the file ends with a final LF.
- **Source:** the file is written from the same in-memory arrays that are then checked.
- **Read-back:** after writing, it is read back and must be byte-identical; the JSON records its SHA-256.

## What each check proves

Throughout, τ_t = D_t − D_0, and the squares are L_t[c][g] = (τ_t(c) + g) mod n for t = 1..k−1.

1. **Well-formedness (otherwise exit 2).** The grammar is strict:
   - only the bytes `0-9`, space, TAB, LF, and CR directly before LF are allowed;
   - lines with no tokens are ignored;
   - n is the token count of the first non-empty line, and every row has exactly n tokens;
   - k ≥ 2;
   - tokens must be canonical decimals (no leading zero) with value < n.

   This proves the file defines one unambiguous k×n matrix D over Z_n. With `--n 39 --k 7` the matrix is exactly 7×39.

   The grammar is stricter than the contract in two ways: it rejects leading zeros, and it rejects any other whitespace or byte (VT, FF, a lone CR, a BOM, signs). Such files get MALFORMED; they never get a silent PASS.

2. **`dm` (sorting, not set sizes).** For each of the k(k−1)/2 row pairs i<j, the checker sorts the list of (D_i(c) − D_j(c)) mod n and compares it with `list(range(n))`. Equality holds exactly when the n differences are a permutation of Z_n, i.e. pairwise distinct. All pairs passing proves D is a (Z_n,k;1) difference matrix.

3. **`latin` (Counter).** Each L_t is built as an explicit n×n list of ints. For every row and column, `Counter(line) == Counter(range(n))` holds exactly when that line is a permutation of 0..n−1. A pass proves every array is a Latin square.
   - Rows are cyclic shifts (g ↦ τ_t(c)+g), so they pass for any well-formed D. The row check only guards the construction code.
   - The columns of L_t are Latin exactly when τ_t is a bijection, i.e. exactly when the DM condition holds for row pair (0,t).

4. **`orthogonal` (boolean incidence table).** For each of the (k−1)(k−2)/2 square pairs s<t, the checker fills an n×n boolean table cell by cell. The pair passes only if no ordered pair (L_s[c][g], L_t[c][g]) is met twice and all n² entries end up set. This is exactly the contract's condition that the n² superimposed pairs are all distinct, and it implies each ordered pair occurs exactly once.

   It is equivalent to the DM condition for row pair (s,t). Cells (c,g) and (c′,g′) give the same pair iff τ_s(c)+g = τ_s(c′)+g′ and τ_t(c)+g = τ_t(c′)+g′. That forces D_t(c)−D_s(c) = D_t(c′)−D_s(c′). If c = c′, then g = g′. Conversely, a collision c≠c′ yields a repeat with g = 0 and g′ = τ_s(c) − τ_s(c′).

5. **Overall PASS ⇔ dm ∧ latin ∧ orthogonal.**
   - By the contract's definition, latin ∧ orthogonal says L_1..L_{k−1} are k−1 MOLS of order n. For a 7×39 input that means six MOLS of order 39.
   - dm independently certifies the difference matrix itself.
   - Items 3 and 4 show dm ⇔ latin ∧ orthogonal, so the verdict is computed twice by different methods.
   - `bridge_agreement` compares the two computations pair by pair: (0,t) with the columns of L_t, (s,t) with L_s⊥L_t, and all rows must be Latin. It cannot change the verdict, because any mismatch implies some property already FAILs. A mismatch would indicate a checker bug. It was PASS in every well-formed control.

**Not proven:** anything about the CFR route; the correctness of the interpreter or hardware (one platform, one run); novelty or literature status. `squares.txt` is exactly the arrays verified, but no second tool has re-checked it.

## Controls

**Construction.**

- `make_controls.py` generates `controls/` from closed formulas.
- Every expectation was derived by hand: the exact exit status, verdict, failing row pairs, failing squares with bad-row and bad-column counts, and failing square pairs. These are written verbatim to `controls/expected.json` (SHA-256 `a4063e30f898dde21cf1a897ddb5cef0787a00fd64fc62e09356e0951cf06d42`), together with the intended-reason text.
- `run_controls.py` runs each case as `python3 -I -B checker_b.py …` (no timeout) and compares the results. It also re-validates every reported witness directly from the control matrix, using its own restatement of the bridge formula.

**Run.** `python3 -I -B run_controls.py runs/r1` gave harness exit 0 and the line "19/19 cases as expected".

- **Record:** `runs/r1/control_results.json`, SHA-256 `605279ca1f7d64d36993a139c2cb3565e7fef75b75bb326721f4e90ac2adb0fb`. Each case's verbatim stdout JSON line and stderr is under `cases[i].stdout` and `cases[i].stderr`.
- **Integrity:**
  - `controls/` was unchanged, by name and SHA-256 snapshots taken before and after;
  - `runs/r1` held only `squares.txt` before the record was written;
  - the checker's hash did not change during the run.

### Required controls (observed)

| Case | Input (k×n) | Intended reason (hand-derived) | Exit | Observed verdict line (key fields) |
|---|---|---|---|---|
| P1 | `pos_z7_linear.txt` (7×7) | Rows a·x mod 7, a = 0..6. Every multiplier difference is a non-zero element of the field Z_7. | 0 | PASS; dm/latin/orthogonal PASS (21/6/15 checked); "6 mutually orthogonal Latin squares of order 7" |
| P2 | `pos_z13_linear.txt` (7×13) | a = (5,0,12,1,7,3,10), distinct mod 13. D_0 = 5x ≠ 0, which exercises the D_0 subtraction. | 0 | PASS; dm/latin/orthogonal PASS; "6 mutually orthogonal Latin squares of order 13" |
| N1 (i) | `neg_i_z13_transposition.txt` | P2 with row 4 (a=7) columns 2↔9 swapped. Row pair (4,j) stays valid iff a_4=0 or a_j=0, so it fails exactly for a_j≠0. Expected: dm fails (0,4),(2,4),(3,4),(4,5),(4,6); (1,4) survives because row 1 is the zero row. Bridge: L_4 columns are non-Latin, and L_4 is not orthogonal to L_2, L_3, L_5, L_6. | 1 | FAIL; dm failing [[0,4],[2,4],[3,4],[4,5],[4,6]]; latin failing L_4 (0 bad rows, 13 bad columns); orthogonal failing [[2,4],[3,4],[4,5],[4,6]]; bridge PASS |
| N2a (ii) | `neg_ii_a_z13_dup_row0.txt` | P2 with row 6 := row 0. Pair (0,6) has all 13 differences equal to 0. Bridge: L_6[c][g] = g, so every column is constant. There is no orthogonality failure. | 1 | FAIL; dm failing [[0,6]]; latin failing L_6 (0 rows, 13 columns); orthogonal PASS; bridge PASS |
| N2b (ii) | `neg_ii_b_z7_dup_rows_2_5.txt` | P1 with row 5 := row 2. Pair (2,5) has all differences equal to 0. Bridge: L_2 = L_5 are identical Latin squares, so they are not orthogonal. | 1 | FAIL; dm failing [[2,5]]; latin PASS; orthogonal failing [[2,5]]; bridge PASS |
| N3 (iii) | `neg_iii_z9_k4.txt` (4×9) | Rows 0, x, 2x, 4x. See the note below this table. | 1 | FAIL; dm failing [[1,3]] (witness: columns 0 and 3 both give difference 0); latin PASS; orthogonal failing [[1,3]]; bridge PASS |
| N4 (iv) | `neg_iv_malformed_length.txt` | P1 whose line 7 has 6 integers instead of 7. | 2 | MALFORMED; reason "line 7: expected 7 integers (n is set by the first non-empty line), found 6" |

**N3 note.** The rows are 0, x, 2x, 4x mod 9, so the multiplier differences are 1, 2, 4 (against row 0), 1 for (1,2), 3 for (1,3) and 2 for (2,3). The only non-unit difference is 3, so the failing pair is (1,3). Difference 2 is a unit mod 9 (2·5 ≡ 1), so pairs (0,2) and (2,3) pass. All squares are Latin because their column multipliers 1, 2, 4 are units. L_1 and L_3 are not orthogonal.

Each negative failed for exactly its stated reason, and nothing more. The checker reported exactly the predicted failing pair, square and square-pair sets, and the harness confirmed every witness from the raw matrix. The required controls also cover each failure shape:

- N2a is a latin-only failure;
- N2b and N3 are orthogonality-only failures;
- N1 fails both ways;
- N4 is rejected before any property is evaluated.

### Extra controls (observed)

| Case | Invocation | Intended reason | Exit | Observed |
|---|---|---|---|---|
| X1 | `pos_z39_k3_linear.txt --n 39 --k 3` | Rows 0, x, 2x mod 39. The differences 1, 2, 1 are prime to 39. | 0 | PASS (2 MOLS of order 39) |
| X2 | `neg_z39_k7_linear.txt --n 39 --k 7` | a = 0..6 mod 39 at the target shape. The pairs with 3 dividing j−i fail. | 1 | FAIL; dm [[0,3],[0,6],[1,4],[2,5],[3,6]]; latin L_3 and L_6 (0 bad rows, 39 bad columns each); orthogonal [[1,4],[2,5],[3,6]]; bridge PASS |
| X3 | `pos_z7_crlf_blank.txt` | The P1 matrix with CRLF, space/TAB runs and blank lines. | 0 | PASS |
| X4 | `pos_z7_linear.txt --n 39 --k 7` | A valid Z_7 DM must not pass as order 39. | 2 | MALFORMED "dimension mismatch: input has n=7 but --n 39 was required" |
| X5 | `mf_out_of_range.txt` | Contains the value n. | 2 | MALFORMED "line 4, column 4 (0-based): integer 7 not in [0, 7)" |
| X6 | `mf_bad_byte.txt` | Contains the token `-1`. | 2 | MALFORMED "disallowed byte 0x2d at byte offset 34 (line 3)" |
| X7 | `mf_leading_zero.txt` | Contains the token `01`. | 2 | MALFORMED "line 2, column 1 (0-based): non-canonical integer token '01' (leading zero)" |
| X8 | `mf_single_row.txt` | k = 1. | 2 | MALFORMED "need at least 2 non-empty lines (rows), found 1" |
| X9 | `controls/no_such_file.txt` | The input path does not exist. | 2 | MALFORMED "cannot read input: FileNotFoundError: …" |
| X10 | no arguments | An argparse error must still produce one JSON line. | 2 | MALFORMED "command line: the following arguments are required: dm" |
| X11 | `pos_z13_linear.txt --emit runs/r1/squares.txt` | Exercises `--emit`. | 0 | PASS. `squares.txt` (83 lines, SHA-256 `539b36453676bdc8472476483bb66c6b70718a3238c1c6aadc0b681719e80515`) equals the closed form ((a_t−a_0)c+g) mod 13 byte for byte, and matches the JSON `emit` record. |
| X12 | `pos_z7_linear.txt --emit runs/r1/squares.txt` | The target already exists. | 3 | ERROR "cannot create --emit file: FileExistsError: …". `squares.txt` is unchanged (same SHA-256). |

I also ran two direct command-line spot checks outside the harness: N3 gave exit 1 and FAIL, matching the record, and P2 with `--n 13 --k 7` gave exit 0 and PASS.

## Files

`checker_b.py` (frozen checker), `make_controls.py`, `run_controls.py`, `controls/*.txt` and `controls/expected.json`, `runs/r1/control_results.json`, `runs/r1/squares.txt`, `report.md`, `make_manifest.py`. `manifest.json` lists every file with its SHA-256 and size; it does not list itself.
