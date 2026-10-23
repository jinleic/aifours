# info-1 / balanced242 — six-lane run 2026-10-16

Lane owner: worker `InfoBalanced`. Contract: `institute/runs/six-lane-2026-10-16/contract.json` (lane `info-1`).
Prior dossiers were treated as read-only inputs, and every new file is in this directory.
**Final lane status (2026-10-16 19:32 PDT = 2026-10-17 02:32 UTC, per result.json): PROOF-OBLIGATION / NEEDS-NEW-REPRESENTATION. The book question remains open.**
No residue type is excluded and no witness was found. On the parent's decision, the slot is preserved and
released.

## Frozen target (2026-10-16 18:40 PDT, before any new computation)

The claim to settle: either exhibit `f: F_2^9 -> F_2` with `wt(f)=256` and `max_a |W_f(a)| <= 28`, verified
by FWHT and by direct character sums, or prove that no such `f` exists. The proof must cover all original
quantifiers: no restricted corpus and no symmetry-class assumption.

**Primary status.** I rechecked on 2026-10-17 at 01:35 UTC; files are in `sources/`.
- Wang–Lou–Wang, arXiv:2610.17871 (v1 only) proves that the covering radius of RM(1,9) is 242 and lists
  the balanced case as open.
- Lou–Xu–Wang, arXiv:2610.17897 (v1 only) proves that the balanced 8-variable maximum is 116. Its Open
  problem 1 is balanced 9-variable NL242.
- Neither preprint is peer reviewed. WLW Theorem 3 is used below only as an imported premise.

**Prior-art screen.** `sources/prior-art-screen-20261017.json` covers the EulerSolve index, Zenodo
full-text API and the openai/math tree (truncated). No claim on this target was found. A search miss is not
novelty.

**Baseline.** These are the earlier read-only lanes:
- residue distance at least 112 (model-reviewed);
- type `(4,128)` excluded (model-reviewed);
- seven types remain;
- rounds 1/2 and the Codex attempt are unreviewed.

## What this lane did

New representation: a 9-variable *sign-digit duality*. It adapts the WLW residue involution to the balanced
setting, using Lucas digits `d_k = sigma_{2^k}(a.x : x in supp f)` of `T = W/4 mod 16`. Statements and
proofs are in [`PROOF.md`](PROOF.md). They are **model-written and UNREVIEWED**:

1. `deg d_k <= 2^k`, and the top part of `d_k` is the set of principal minors of the support-moment form
   (Cauchy–Binet). The quartic part of `d2` is `Pf4(polar d1)`.
2. Translation normalization brings the 9x9 polar rank down to `rank D`.
3. For a target, `W/4 = d0 + 2d1 + 4d2 - 8d3`, with `d3` the sign indicator, and
   `W_{d3} = 32F + 64(delta_0 + delta_s) + W_{d1}/4 + W_{d2}/2`.
4. **Sign-parity theorem:** for every `h != 0` and `c`, `#{a.h = c : W(a) < 0} = det(beta|_{h^perp})`
   (mod 2). In particular, the number of negative Walsh values on either coset of `s^perp` has the parity of
   `[rank D = 8]`. It follows that `W_{Jq} = 4[rank 8]` (mod 8).
5. An odd-coset duality bound, using the 2-adic lattice of `W_{Jq}`, forces at least about 5–10
   odd-coset values with `|W| in {4,12}` for every remaining type (`evidence/oside-bounds.json`).
6. For type `(2,192)`, `d2` is cubic, and WLW Theorem 3 gives `4c + 5n12 + 3n4 >= 32 + z + 3|Delta|`.
7. For rank-8 types, `f` lies at distance `48 + 1.25d - 2(a+c) - z` from an explicit semi-bent quadratic.

**Decisive obstruction.** Aggregate per-point integer models were solved with CP-SAT, as exploratory
relaxations only. They contain all of the above and are feasible for all seven types. Nothing proved caps
the forced small odd-coset values. A Gaussian-sphere heuristic gives about `2^-63` expected `s != 0`, cap-28
functions; calibrated the same way, the `s = 0` class gives about `2^96`. This suggests, but does not prove,
nonexistence. No construction search was run.

## Evidence and replay

| File | Content |
|---|---|
| `code/bf.py` | exact FWHT, ANF, rank and Pfaffian utilities |
| `code/digit_lemmas_check.py` -> `evidence/digit-lemmas-check.json` | Lemmas 1–5 (including all-hyperplane parity) on 40 genuine balanced controls (ranks 8/6/4: 16/23/1); two mutation controls must fail and do |
| `code/oside_bounds.py` -> `evidence/oside-bounds.json` | Proposition 6 minimal-`a` tables (single implementation) |
| `code/oside_ilp.py`, `code/oside_ilp_rank8.py` -> `evidence/oside-ilp-*.jsonl` | exploratory CP-SAT relaxations (all feasible; not Boolean functions) |
| `evidence/code-sha256.txt` | code hashes at run time |

Replay requires Python 3 with numpy. The ILP files need `.venv` (ortools 9.15.6755). The verifier takes
about 4 s and 35 MB RSS:

```sh
python3 code/digit_lemmas_check.py 40 20261016
python3 code/oside_bounds.py
```

## Frontier

These are bounded, specialist-partial routes, ranked:
- (a) The near-rigid part of `(2,192)`: when `L > 10048`, the WLW proof forces `16 | W_{d2}` and
  `F = -sgn W_{d2}` except at about 10 points. That leaves a finite residue-involution check over the
  Brier–Langevin cubic classes.
- (b) Rank 8 via `f = Phi + 1_M`.
- An independent proof review of `PROOF.md` Sections 1–4.

Section 4 is the most reusable result. None of these resolves the book problem, and further aggregate
relaxations are not justified.
