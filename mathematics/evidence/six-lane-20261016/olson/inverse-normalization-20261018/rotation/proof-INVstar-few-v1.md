# Corollary INV*-FEW: INV*(p) for avoiders with few odd maximal constant reflection blocks (combination), v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T06:59:38-07:00.  Status [W], UNREVIEWED combination
note; no new lemma.  It records how the rotation results meet the reflection slice's
reflection/proof-REFL-fewodd-r1.md (OlsonReflectionRigidity, sha256 6058831acc970e86a33f007bf900de397eaba5ccac7318bd3ba93a0bd61d7dd7,
[W] unreviewed; its inputs are parent-accepted: Theorem RED and the small-k verdict).  Interface confirmed with its
author by IRC (06:59).  Not ordered Olson (length 4p-1); not INV*(p) for all avoiders.
Notation: o_F(w) := number of maximal constant reflection blocks of odd length in the maximal cyclic decomposition of
w (each maximal cyclic reflection run split into its maximal constant blocks).  This is the parameter o of ROT-o2,
ROT-o3, ROT-o4 and of proof-ROT-few-E-v1.md, and the o_F of REFL-few-odd.  INV*(p) for w: rotations in one
{rho_c, rho_-c}, c != 0, and every maximal cyclic reflection run constant.

## Statement

**Corollary INV*-FEW.**  Let p >= 5 be prime and w an avoider of length 4p-2 over D_(2p).
 (a) If o_F(w) <= 3, or p >= 7 and o_F(w) = 4, then w satisfies INV*: conditional ONLY on Corollary REFL-few-odd.
 (b) If 5 o_F(w) <= 2p + 4, then w satisfies INV*: conditional on Theorem SHgen (proof-SHgen-v2.md 8fde88c0...d239)
     and Corollary REFL-few-odd.

## Proof

(a) Rotations: ROT-o2 (accepted, lowodd verdict v2: "maximal cyclic constant reflection blocks include at most two
odd-length blocks"; o_F = 0 impossible, o_F = 1 gives equal rotations), ROT-o3 (accepted for primes p >= 5) and ROT-o4
(accepted for primes p >= 7) are stated for avoiders with exactly o odd maximal constant reflection blocks and assume
nothing about run constancy; their proofs use GRX, PM*, DEL and Davenport-alpha on arbitrary cyclic constant-block
representations (o3o4 verdict: "GRX, PM*, the pairs bound and Davenport-alpha do not use maximality, and o is read on
the original maximal blocks").  So w's rotations lie in one {rho_c, rho_-c}, c != 0.  Reflections: o_F(w) <= 4 <= p,
so REFL-few-odd applies to w and every maximal cyclic reflection run of w is constant.
(b) Rotations: proof-ROT-few-E-v1.md Theorem ROT-FEW-E, whose only use of REFL(p) is in Lemma SHgen-E on the expanded
word u°(h) and in its final sentence on w.  (i) u°(h) has length 4p-2 and rotations in {rho_c, rho_-c}; its blocks are
the k blocks of the normal form w^ (all odd and nonempty, every empty run between DIFFERENT values), so they are its
maximal constant blocks and o_F(u°(h)) = k <= o_F(w) <= (2p+4)/5 <= p.  If u°(h) avoided, REFL-few-odd would make
its maximal cyclic reflection runs constant, but the empty run between two different values lies inside one maximal
run: so u°(h) does not avoid, which is exactly what Lemma SHgen-E needs.  (ii) Once the rotations of w lie in one
{rho_c, rho_-c}, REFL-few-odd applies to w (o_F(w) <= p).  []

## Scope

* (a) depends only on accepted rotation results and the unreviewed REFL-few-odd; (b) additionally on SHgen-v2 [W].
* Range of (b): o_F <= 5 for p = 11; 6 for p = 13; 7 for p = 17; 8 for p = 19; 10 for p = 23; about 2p/5 in general.
* Avoiders with o_F > (2p+4)/5 (and o_F > 4 when SHgen is not assumed) are not covered; p = 5 with o_F = 4 is not
  covered by (a) (ROT-o4 is accepted only for p >= 7).
* Observation [O] (not a premise): the listed normalised avoiders at p = 5, 7 have o_F up to p, so the uncovered range
  contains avoiders.
* No novelty claim; not ordered Olson.
