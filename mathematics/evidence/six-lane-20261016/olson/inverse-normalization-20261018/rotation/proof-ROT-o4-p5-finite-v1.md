# ROT-o4 at p = 5: finite exact verification (result note), v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T08:29:40-07:00.  Status [F] finite exact result of a
frozen, parent-scoped computation (GO at 08:23-08:24); Codex audit of sources and outputs pending; not parent-accepted.
Packet: p5o4-v1/PLAN-v1.md 7d7793cbf137f2ddf01d7cc64872657ba26d15fbac0276101894972038e50588; code/grx_p5o4_v1.py
669dbf8b...beed; code/dp_p5o4_v1.cpp 8b748f64...581f (binary af7a3284...db76); code/compare_p5o4_v1.py ce143d6e...582e.
Run: p5o4-v1/out/run1, verdict.json ca156d58a1cbe6aa64418e732a205b499190ab290b1cafd0ee8a0c42266ddf0f (PASS, 18/18 checks).

## Statement

**C5 (ROT-o4 at p = 5).**  Every word of length 18 over D_10 with no identity 10-subword (in increasing index order)
and exactly four odd blocks in its maximal cyclic constant-block decomposition has all rotation letters in one set
{rho_c, rho_-c}, c != 0.

## Proof

PLAN-v1 Sec. 2: the accepted Lemma PM* (any cyclic constant-block representation, original-to-reduced) applied to every
even block leaves exactly four odd blocks, so every such avoider yields an avoider with the same rotation multiset in
the domain D of 4-block all-odd cyclic representations of length 18 with arbitrary runs (C5 follows from C5').  By the
elementary facts (R3), (R4) of PLAN-v1 (cyclic shifts, runs as multisets, block selections by count; five equal pairs;
the pairs filter P1'), only the classes listed in PLAN-v1 Sec. 3 need a decision.  Run1 decided them twice:
* Stage D (direct ordered 10-subsequence DP over D_10, every block-length tuple, 255,650,000 words; GRX not used) and
* Stage G (accepted GRX, 25,267,500 classes),
with byte-identical survivor, avoider and mutation lists and full per-H coverage (GRX classes 613,973,068,750; words
1,021,369,625,000).  D contains exactly 640 avoider classes, all rigid (by rotation multiset: c^9 (-c)^3 at H = 1, 80
classes; c^9 (-c) at H = 2, 160; c^8 at H = 3, 320; c^6 at H = 4, 80), no non-rigid one, and no class whose verdict
depends on the block lengths.  Hence C5', and C5.  []

Controls (all fired as specified in PLAN-v1 Sec. 7): positive PC-k2 (accepted example rho_1^9 sigma_0^7 rho_-1 sigma_0)
avoider in both stages, type I and type II classes present; TC1 6,120,000 spurious non-rigid classes; TC2 640 flips;
TC3 80 verdict differences; TC4 640 avoider words solvable at target 8; TC5 16,640 mutation lines identical in both
stages (all solvable); P1' sample 20,000 words, 0 failures; 640 avoider classes x (18 shifts + reversal), 0 failures.

## Scope and consequences (to be read with the audit outcome)

* Finite exact, conditional on the accepted PM* and on the frozen code; not a written proof.  The historical D10 census
  and all earlier lane code and outputs were not used.
* With the accepted ROT-o2/o3 and Corollary REFL-few-odd (o_F <= 4 <= p): INV*(5) for avoiders with o_F <= 4, i.e.
  INV*-FEW (a) extends to p = 5, o_F = 4; and OLSON-FEW (a) (proof-OLSON-few-v3.md) extends to p = 5 with o_F(w) <= 4
  (its Cases 2-3 need INV* only up to o_F(w)).
* Not INV*(5) for o_F >= 5, not ordered Olson for D_10 in general; no novelty claim.
