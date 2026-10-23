# PLAN-v1: finite control for Lemma ZS (aid only, not a proof), frozen before any run

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T11:06:17-07:00.  This plan tests the written Lemma ZS
of proof-ROT-half-v1.md (3b8fa50e...c738, under parent review) and its v2 hypothesis (G) of proof-ROT-half-v2.md
(7403098f...48eb).  The lemma's proof is the written one.  This run is an aid only and is never a premise.
Code: zs-check-v1/code/zs_check_v1.py (hash sent with this plan).  It is a statement about sequences in Z_(2p); no
words over D_(2p) are enumerated.

## 1. Sub-obligations tested

For a multiset Y of R = 2p + 2kappa - k odd residues mod 2p with
  (ZP) no zero-sum sub-multiset of size in [2kappa + 2, 2p],
the run checks:
- ZP2 (every item): (ZP) re-checked by a second implementation, the set of (size, sum) pairs of all sub-multisets.  It is
  independent of the enumerator's bitmask pruning.
- CONC (every item): the conclusion of Lemma ZS, i.e. min over odd generators h of cost_h(Y) <= k - 1.
- S1-S9 (items in (G): 3k <= 2p + 1 and 0 <= kappa <= min(k - 1, p - k)): every claim of the written proof.  It uses the
  generator g of Step 3 (most frequent value of Y - Z) and Z = one maximum-size zero-sum sub-multiset.
  - S1: every zero-sum has size <= 2kappa.
  - S2: Y - Z is zero-sum-free and 0 <= e = k - 1 - 2kappa + |Z| <= k - 1.
  - S3: MULT form; weights 1 or odd in [3, m]; e' <= e; W' <= 2p - 1; completeness; m >= k - 1.
  - S5: every tau(U), U <= Z, lies in {0} u [1, k-1] u [2p-k+1, 2p-1].
  - S6: |b| <= k - 1 on Z, and sigma+ = sigma- <= k - 1.
  - S7: W' <= 2p - 1 - sigma.
  - S8: |Z-| + sigma <= 2kappa.
  - S9: cost_g(Y) <= k - 1.

## 2. Scope (66 items, in this order)

- (G) items:
  - p = 5: (5,1,0), (5,2,0..1) and the half boundary (5,3,0..2).
  - p = 7: (7,2,0..1), (7,3,0..2), the half boundary (7,4,0..3), and v2's (7,5,0..2).
  - Half boundaries (11,6,0..5) and (13,7,0..6).
  - v2 range above the half: (11,7,0..4), (13,8,0..5), (13,9,0..4).
  - Half boundary (17,9,0..8).
- Informative items outside (G), with 3k <= 2p + 1 and p - k < kappa <= k - 1: (7,5,3..4), (11,7,5..6), (13,8,6..7),
  (13,9,5..8).  These are not lemma claims.
- The k = p obstruction of Remark (3), Y = g^(2p-1) (3g)^(p-1) with kappa = p - 1, is evaluated directly for
  p = 5, 7, 11, 13.  This is not an enumeration.

## 3. Enumeration and coverage

The method is that of code/check_rotfew_v2.py part_b2 (f87831ff...c32f): depth-first choice of multiplicities over the p
odd residues, pruned by bitmask (size, sum) reachability up to size 2p.  Every multiset is covered up to multiplication
by a unit of Z_(2p), which preserves (ZP), the cost function's minimum over generators, and the proof.
- Pass "1-max": residue 1 has a largest multiplicity; ties are allowed.
- Pass "(1,0)-max": residue p, i.e. (1,0), has the strictly largest multiplicity.
The enumerator's completeness is not proved again here.  Consistency check: at (11,6) and (13,7) the "1-max" found
counts must equal those in out/check_rotfew_v3.jsonl (0e870300...48c4): 4, 6, 7, 7, 3, 1 and 7, 8, 10, 10, 8, 3, 1.  That
is the same method, so this is not independent.

## 4. Controls (expected outcome in brackets)

- Positive [found]:
  - type I, Y = 1^(2p-k), in every item with kappa = 0;
  - type II, Y = 1^(2p-1) (2p-1)^(k-1), in every item with kappa = k - 1.  It satisfies (ZP) for every kappa = k - 1.
- Tightness: in (G) items with kappa = k - 1 and k >= 2, both mutations must fire somewhere [m1_fired >= 1 and
  m2_fired >= 1]:
  - M1: cost_g <= k - 2;
  - M2: S5 with k - 1 in place of k.
- Obstruction [(ZP) holds, and the minimum cost over generators is 2p - 2 > p - 1].

## 5. Acceptance of the aid, and interpretation

- PASS:
  - zp2_fail = 0 in every completed item;
  - conc_fail = 0 and proof_fail = {} in every completed (G) item;
  - all controls as in Sec. 4;
  - found counts consistent as in Sec. 3.
- Informative items: conc_fail and the examples are reported as found.  A nonzero conc_fail there is an explicit (ZP)
  sequence on which the conclusion of Lemma ZS fails above (G).  It is not a contradiction of the lemma, and it is not a
  counterexample to ROT.
- An item not printed before the CPU limit is UNKNOWN.  The final line DONE marks completion.

## 6. Run protocol

- One process, launched via ../code/gate_v1.sh 100000000, with ulimit -t 3000.
- TMPDIR = zs-check-v1/tmp and PYTHONDONTWRITEBYTECODE=1.
- Output: zs-check-v1/out/run1.jsonl, opened exclusively, one JSON line per item, flushed.
- No retries in place.  A rerun uses a new output name and is logged.

## 7. Disclosure

- The code was drafted, then edited in place before this freeze: item order, the type II expectation, and repair of one
  broken edit to the docstring and item list.
- Before the freeze, only a Python parse check and a printout of the item list against (G) ran.  No enumeration ran.
