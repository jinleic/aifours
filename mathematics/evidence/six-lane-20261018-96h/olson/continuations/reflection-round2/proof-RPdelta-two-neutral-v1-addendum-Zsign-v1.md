# RP-2NE addendum: a zero increment can force a sign change at zero cost

OlsonReflectionSuccessor.  Frozen after /bin/date observation 2026-10-19T08:40:18-0700.  CANDIDATE_UNVERIFIED, written only;
no computation or model call.  Base proof-RPdelta-two-neutral-v1.md
(e6471758f0e5aaba016286ccfb0e901ecb5fc670b980728407c9bbd468c8fa20) is unchanged.  This is a separate strengthening, not a
silent change of its theorem.  Same accepted imports and verdict bindings; no unreviewed RPdelta-package premise.

## 1. Strengthened SIGN-2Z statement

In SIGN-2Z (base Sec. 4), replace the hypothesis e>z by e>=1, keeping z<=2 and every other hypothesis.  The conclusion
is unchanged.  This is stronger: it no longer forces sum abs(h_i)>k when zeros exist.
Proof.  Start as before on all nonzero h_i.  If z>=1, assign the zero signs so that at least one sign change occurs:
- if the nonzero h_i already include both signs, any filling of zeros still leaves at least two cyclic sign changes;
- if all nonzero h_i have the same sign, assign the opposite sign to ONE zero index and the common sign to all other
  zeros.  That zero index is a singleton stretch, so m0>=1, while the signed sum remains S.
There is a nonzero index (e>=1), so these cases are exhaustive.  For z=0 keep the original signs.
Case A of the base proof needs only S>=k+e-z>=M+2kappa+1-2=M+2kappa-1>M-2 (kappa>=1), not S>k.
Cases B and C are unchanged: Case B uses S>=2m0-z and z<=2; Case C uses e>=1, z<=2, n-2f>=1, and
   M-2+2m0-z+(1-2f/n)e>M-2.
Case D (m0=0) can now occur only when z=0, and then S>=k+e>k, so its LIGHT estimate still gives a strict contradiction.
This proves strengthened SIGN-2Z.  []

## 2. Full two-offset residual exclusion (still a candidate)

**Theorem RP-2NE-E.**  Let p>=5 be prime, delta in {1,2}, and w have length4p-2 over D_(2p), with exactly R=p+delta rotations
in one nonzero pair.  All maximal cyclic CONSTANT reflection blocks are odd.  Suppose at least one maximal cyclic reflection
run is nonconstant (equivalently there is a genuine empty rotation run in the maximal block decomposition), and
   1<=kappa<=floor((p-delta-3)/2).
Then w has an identity2p-subword in increasing original index order.  Any B, no run purity or inherited condition.
Proof.  Repeat base Sec.2: M=p-delta, k=M+2kappa, L=kappa+1, U=ceil(M/2), fixed C_(2p) window, and integer increments h_i
obeying the signed bound M-2 for every L<=m<=U.  Base Sec.3's zero criterion and count z<=v<=delta<=2 still hold and do not
use kappa>=delta+1.  The genuine empty-run indices form a nonempty marked set Z, disjoint from zeros, with abs(h_i)>=2;
all other nonzero h_i have abs(h_i)>=1.  Apply strengthened SIGN-2Z (e=|Z|>=1, not e>z) to contradict that signed bound.  []
The base theorem RP-2NE remains true: its kappa>=delta+1 forces g_E-z>=2, so a genuine empty run exists under its avoider
assumption even without a nonconstant-run hypothesis.  RP-2NE-E is the version needed for RES_<, which already has one.

**Corollary RES-DELTA12.**  No word of RES_<(p) with delta in {1,2}, R=p+delta and
   2<=kappa<=floor((p-delta-3)/2)
avoids.  Thus for BOTH offsets the residual band is 2<=kappa<=(p-5)/2 (p odd, nonempty first at p=11).
This now includes delta2,kappa2, which was expressly not claimed by the base sign estimate with e>z.  It is NOT evidence of
an error in the base sufficient theorem; it uses the NEW zero-sign choice to remove that obstruction.

Exact numerical delta against accepted V5 I.14: for delta1 use the base proof's Sec.5 set difference; for delta2 replace its
lower endpoint3 by2.  In particular p=11,delta2,kappa2 and p=11,delta2,kappa3 are both new to I.14.  More generally the new
candidate RES band is [2,(p-5)/2]_Z minus the accepted SEG-num band and K2P+ band.  The full theorem here concerns all-odd
words WITH a genuine empty run; no exclusion of a no-empty-run word is inferred without its separate RGR hypotheses.

## 3. Remaining obstruction

For delta>=3, the present Case C bound allows 2m0-z<0 and the Case B bound can lose >=3 units; this addendum does not
remove that gap.  A local neutral-even run still supplies only a short identity selection, not the required length2p.
No unrestricted REFL, new move, novelty or Lean claim.  Parent owns all reviews and verdicts.
