# ROT-o4 at p = 5: finite exact verification (result note), v2

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T08:29:40-07:00.  v2 written after host clock
2026-10-18T09:36:55-07:00: ERRATA of v1 (sha256 7c8a5051e40f28b5641a69cd6809aaa5b93f086d6d6eebe9f0dffeea1e93404c) after the Codex source/result
review R/olson-p5o4-code-result-codex-v1.note.md (e0504765...6468: ACCEPT-WITH-FIXES, 0 FATAL, 1 MAJOR M1 and 1 MINOR m1,
both on the comparator; no reduction, enumeration, GRX or ordered-DP defect): the counts are relabelled as labelled
block-length representations and acceptance is now by the fail-closed comparator v2 (fix map at the end).  Status [F]
finite exact result of a frozen, parent-scoped computation (GO at 08:23-08:24); independent parent replay pending; not
parent-accepted.
Packet: p5o4-v1/PLAN-v1.md 7d7793cbf137f2ddf01d7cc64872657ba26d15fbac0276101894972038e50588; code/grx_p5o4_v1.py
669dbf8b...beed; code/dp_p5o4_v1.cpp 8b748f64...581f (binary af7a3284...db76); code/compare_p5o4_v1.py ce143d6e...582e,
superseded for acceptance by code/compare_p5o4_v2.py 9d0198a69ef66d433c62284477b834436628b2ac3d0075ff5bc3246e7229a255.
Run: p5o4-v1/out/run1, verdict.json ca156d58a1cbe6aa64418e732a205b499190ab290b1cafd0ee8a0c42266ddf0f (PASS, 18/18 checks);
verdict-v2.json 780f0b6f7c8c0693888c48f23b2f8ba59514be8dd016f899664e6630624b5e30 (compare_p5o4_v2.py on the same retained
outputs, Stages G and D not rerun: PASS, 69/69 required checks, exit status 0).

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
* Stage D (direct ordered 10-subsequence DP over D_10, every block-length tuple, 255,650,000 labelled block-length
  representations (H, block-length tuple, run multisets, y-tuple), each built and decided as one word; GRX not used) and
* Stage G (accepted GRX, 25,267,500 classes),
with byte-identical survivor, avoider and mutation lists and full per-H coverage (GRX classes 613,973,068,750; labelled block-length
representations 1,021,369,625,000, which can repeat literal words and are not counts of distinct raw words).  D contains exactly 640 avoider classes, all rigid (by rotation multiset: c^9 (-c)^3 at H = 1, 80
classes; c^9 (-c) at H = 2, 160; c^8 at H = 3, 320; c^6 at H = 4, 80), no non-rigid one, and no class whose verdict
depends on the block lengths.  Hence C5', and C5.  []

Controls (all fired as specified in PLAN-v1 Sec. 7): positive PC-k2 (accepted example rho_1^9 sigma_0^7 rho_-1 sigma_0)
avoider in both stages, type I and type II classes present; TC1 6,120,000 spurious non-rigid classes; TC2 640 flips;
TC3 80 verdict differences; TC4 640 avoider words solvable at target 8; TC5 16,640 mutation lines identical in both
stages (all solvable); P1' sample 20,000 words, 0 failures; 640 avoider classes x (18 shifts + reversal), 0 failures.

Acceptance check (code/compare_p5o4_v2.py, fixing Codex M1 and m1): it requires exactly the strata H = 0..4,
p = 5, k = 4, N = 18 and exact key sets; recomputes M_H = 625 C(R+19,19), L_H M_H, the set of P1'-survivors (a
third, brute-force implementation) and the examined counts; reconciles every list (G/D byte-identical, well-formed,
sorted, unique) with every summary count and with G's file manifest; recomputes the rigidity of every avoider
multiset, the TC5 mutation structure and all controls; gives PASS only if all 69 required checks ran and hold, and
exits nonzero on FAIL.  Rejection fixtures (p5o4-v1/out/fixtures-v2, manifest
f297cf0bd966324d689564fb218ccc5a01df239c936d8ae80d81864441e09adc; separate-process results
out/fixture-results-v2/fixture-results.json 0951e5a902c6a6eecca9aac0f11a8085fdbd2597d0b4fc2c1a3033155b1e8cfc): 36/36
behave as specified (the byte-exact copy PASSes; 35 single-defect copies FAIL with exit status 1, among them a missing
G or D stratum, empty strata, altered p, k and N, self-consistently altered formula counts, dropped list lines and a
self-consistently injected non-rigid avoider class).  Single-protection mutation check
(out/mutcheck-v2/mutcheck-summary.json fbbc9b7b21e34ca1a7c89a97487cf3569d43a06a9a4f3f076f92dc11ee71e6a6): removing any
one of the 23 protections lets at least one fixture through (23/23 mutants killed).

## Scope and consequences (to be read with the parent replay and verdict)

* Finite exact, conditional on the accepted PM* and on the frozen code; not a written proof.  The historical D10 census
  and all earlier lane code and outputs were not used.
* With the accepted ROT-o2/o3 and Corollary REFL-few-odd (o_F <= 4 <= p): INV*(5) for avoiders with o_F <= 4, i.e.
  INV*-FEW (a) extends to p = 5, o_F = 4; and OLSON-FEW (a) (proof-OLSON-few-v3.md) extends to p = 5 with o_F(w) <= 4
  (its Cases 2-3 need INV* only up to o_F(w)).
* Not INV*(5) for o_F >= 5, not ordered Olson for D_10 in general; no novelty claim.

## Errata diff and fix map (proof-ROT-o4-p5-finite-v1.md -> proof-ROT-o4-p5-finite-v2.md)

Fix map (Codex source/result review R/olson-p5o4-code-result-codex-v1.note.md):
M1 (comparator accepted missing or empty strata, never validated p, k, N, trusted the formula fields) and m1 (FAIL exited
0) -> acceptance by code/compare_p5o4_v2.py: header status and packet/run lines, and the new 'Acceptance check'
paragraph (verdict-v2.json, rejection fixtures, mutation check).
Accounting wording (the review counts D's 1,021,369,625,000 and 255,650,000 as labelled block-length representations,
which can repeat literal words) -> the Stage D bullet and the coverage sentence.
No statement, reduction, decision or count value changed.
Generated by unique string replacement from proof-ROT-o4-p5-finite-v1.md (sha256 7c8a5051e40f28b5641a69cd6809aaa5b93f086d6d6eebe9f0dffeea1e93404c); body diff:

```diff
--- proof-ROT-o4-p5-finite-v1.md
+++ proof-ROT-o4-p5-finite-v2.md (body)
@@ -1,10 +1,18 @@
-# ROT-o4 at p = 5: finite exact verification (result note), v1
+# ROT-o4 at p = 5: finite exact verification (result note), v2
 
-Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T08:29:40-07:00.  Status [F] finite exact result of a
-frozen, parent-scoped computation (GO at 08:23-08:24); Codex audit of sources and outputs pending; not parent-accepted.
+Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T08:29:40-07:00.  v2 written after host clock
+2026-10-18T09:36:55-07:00: ERRATA of v1 (sha256 7c8a5051e40f28b5641a69cd6809aaa5b93f086d6d6eebe9f0dffeea1e93404c) after the Codex source/result
+review R/olson-p5o4-code-result-codex-v1.note.md (e0504765...6468: ACCEPT-WITH-FIXES, 0 FATAL, 1 MAJOR M1 and 1 MINOR m1,
+both on the comparator; no reduction, enumeration, GRX or ordered-DP defect): the counts are relabelled as labelled
+block-length representations and acceptance is now by the fail-closed comparator v2 (fix map at the end).  Status [F]
+finite exact result of a frozen, parent-scoped computation (GO at 08:23-08:24); independent parent replay pending; not
+parent-accepted.
 Packet: p5o4-v1/PLAN-v1.md 7d7793cbf137f2ddf01d7cc64872657ba26d15fbac0276101894972038e50588; code/grx_p5o4_v1.py
-669dbf8b...beed; code/dp_p5o4_v1.cpp 8b748f64...581f (binary af7a3284...db76); code/compare_p5o4_v1.py ce143d6e...582e.
-Run: p5o4-v1/out/run1, verdict.json ca156d58a1cbe6aa64418e732a205b499190ab290b1cafd0ee8a0c42266ddf0f (PASS, 18/18 checks).
+669dbf8b...beed; code/dp_p5o4_v1.cpp 8b748f64...581f (binary af7a3284...db76); code/compare_p5o4_v1.py ce143d6e...582e,
+superseded for acceptance by code/compare_p5o4_v2.py 9d0198a69ef66d433c62284477b834436628b2ac3d0075ff5bc3246e7229a255.
+Run: p5o4-v1/out/run1, verdict.json ca156d58a1cbe6aa64418e732a205b499190ab290b1cafd0ee8a0c42266ddf0f (PASS, 18/18 checks);
+verdict-v2.json 780f0b6f7c8c0693888c48f23b2f8ba59514be8dd016f899664e6630624b5e30 (compare_p5o4_v2.py on the same retained
+outputs, Stages G and D not rerun: PASS, 69/69 required checks, exit status 0).
 
 ## Statement
 
@@ -19,10 +27,11 @@
 the domain D of 4-block all-odd cyclic representations of length 18 with arbitrary runs (C5 follows from C5').  By the
 elementary facts (R3), (R4) of PLAN-v1 (cyclic shifts, runs as multisets, block selections by count; five equal pairs;
 the pairs filter P1'), only the classes listed in PLAN-v1 Sec. 3 need a decision.  Run1 decided them twice:
-* Stage D (direct ordered 10-subsequence DP over D_10, every block-length tuple, 255,650,000 words; GRX not used) and
+* Stage D (direct ordered 10-subsequence DP over D_10, every block-length tuple, 255,650,000 labelled block-length
+  representations (H, block-length tuple, run multisets, y-tuple), each built and decided as one word; GRX not used) and
 * Stage G (accepted GRX, 25,267,500 classes),
-with byte-identical survivor, avoider and mutation lists and full per-H coverage (GRX classes 613,973,068,750; words
-1,021,369,625,000).  D contains exactly 640 avoider classes, all rigid (by rotation multiset: c^9 (-c)^3 at H = 1, 80
+with byte-identical survivor, avoider and mutation lists and full per-H coverage (GRX classes 613,973,068,750; labelled block-length
+representations 1,021,369,625,000, which can repeat literal words and are not counts of distinct raw words).  D contains exactly 640 avoider classes, all rigid (by rotation multiset: c^9 (-c)^3 at H = 1, 80
 classes; c^9 (-c) at H = 2, 160; c^8 at H = 3, 320; c^6 at H = 4, 80), no non-rigid one, and no class whose verdict
 depends on the block lengths.  Hence C5', and C5.  []
 
@@ -31,7 +40,21 @@
 TC3 80 verdict differences; TC4 640 avoider words solvable at target 8; TC5 16,640 mutation lines identical in both
 stages (all solvable); P1' sample 20,000 words, 0 failures; 640 avoider classes x (18 shifts + reversal), 0 failures.
 
-## Scope and consequences (to be read with the audit outcome)
+Acceptance check (code/compare_p5o4_v2.py, fixing Codex M1 and m1): it requires exactly the strata H = 0..4,
+p = 5, k = 4, N = 18 and exact key sets; recomputes M_H = 625 C(R+19,19), L_H M_H, the set of P1'-survivors (a
+third, brute-force implementation) and the examined counts; reconciles every list (G/D byte-identical, well-formed,
+sorted, unique) with every summary count and with G's file manifest; recomputes the rigidity of every avoider
+multiset, the TC5 mutation structure and all controls; gives PASS only if all 69 required checks ran and hold, and
+exits nonzero on FAIL.  Rejection fixtures (p5o4-v1/out/fixtures-v2, manifest
+f297cf0bd966324d689564fb218ccc5a01df239c936d8ae80d81864441e09adc; separate-process results
+out/fixture-results-v2/fixture-results.json 0951e5a902c6a6eecca9aac0f11a8085fdbd2597d0b4fc2c1a3033155b1e8cfc): 36/36
+behave as specified (the byte-exact copy PASSes; 35 single-defect copies FAIL with exit status 1, among them a missing
+G or D stratum, empty strata, altered p, k and N, self-consistently altered formula counts, dropped list lines and a
+self-consistently injected non-rigid avoider class).  Single-protection mutation check
+(out/mutcheck-v2/mutcheck-summary.json fbbc9b7b21e34ca1a7c89a97487cf3569d43a06a9a4f3f076f92dc11ee71e6a6): removing any
+one of the 23 protections lets at least one fixture through (23/23 mutants killed).
+
+## Scope and consequences (to be read with the parent replay and verdict)
 
 * Finite exact, conditional on the accepted PM* and on the frozen code; not a written proof.  The historical D10 census
   and all earlier lane code and outputs were not used.
```
