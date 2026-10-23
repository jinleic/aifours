# Import note: S(p) as a classical corollary of Xia-Yuan 2010 (Thm 3.1), the index-one theorem and splitting, v1

Owner ContinueOlson (math-2 lane, 96-hour continuation).  Written after /bin/date 2026-10-19T03:15:57-0700, on parent instruction (IRC after
run review/olson-priority-parent-note-v1.md).  Status: IMPORT NOTE (a known corollary of published results, NOT a lane
result), unreviewed by the parent.  It replaces the status 'open' of S(p) (old round notes-SC-lengthp-v2.md; lane
evidence/proof-KPS-cond-v3.md) by 'classical import at the trust level of Sec. 2'.  No novelty or priority claim.

## 0. Notation and the statements concerned

n := 2p, p >= 5 prime; C_n written additively as Z_(2p).  EVEN elements: the subgroup 2C_n (order p) = the even residues;
ODD elements: the odd residues.  Every generator of C_n is odd; the only odd non-generator is the involution p.
For a generator g and x != 0: |x|_g := the least positive integer a with x = a g (so |x|_g in [1, n - 1]); for a sequence S
of nonzero terms, ||S||_g := (1/n) sum_(x in S) |x|_g, and ind(S) := min over generators g of ||S||_g.  For a zero-sum S of
nonzero terms n ||S||_g is a positive multiple of n; INDEX 1 means sum_(x in S) |x|_g = n for some generator g.
SC (lane; notes-SC-lengthp-v2.md Sec. 0): a sequence U of odd elements is SC if sum_(x in U) |x|_g <= 2p - 1 for some
generator g.
- S(p): every zero-sum-free sequence of p odd elements of C_(2p) is SC.
- IDX1-odd(p+1): every minimal zero-sum sequence of p + 1 odd elements of C_(2p) has index 1.
SPLITTABLE (the standard notion used by Xia-Yuan and Peng-Sun Sec. 1): a minimal zero-sum sequence S is splittable if there
are a term x of S and y, z in C_n - {0} with y + z = x such that S x^(-1) y z is a minimal zero-sum sequence; otherwise
UNSPLITTABLE.

## 1. Result recorded (classical import)

**Import S(p).**  For every prime p >= 5 (used in the lane only for p >= 7), every zero-sum-free sequence of p odd elements
of C_(2p) is SC; equivalently (Sec. 5) every minimal zero-sum sequence of p + 1 odd elements of C_(2p) has index 1.

## 2. Imported statements, exact citations and trust

(I1) Index-one theorem (existing lane import): every minimal zero-sum sequence over C_n, n >= 3, of length >= floor(n/2) + 2
has a 1-element basis {a} (every term is x(t) a with positive least coefficients x(t) summing to ord(a)).  S. Savchev,
F. Chen, Long zero-free sequences in finite cyclic groups, Discrete Math. 307 (2007) 2671-2679, DOI
10.1016/j.disc.2007.01.012; P. Yuan, On the index of minimal zero-sum sequences over finite cyclic groups, J. Combin.
Theory Ser. A 114 (2007) 1545-1551.  Parent import record: run of 2026-10-16, review/olson-index-one-primary-statement-parent-v1.md,
sha256 e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 (author statement read in F. Chen's CANT 2016 slides, p. 4, Thm 1; proofs not read).
(I2) Xia-Yuan 2010, Theorem 3.1: Discrete Math. 310 (2010) 1127-1133, DOI 10.1016/j.disc.2009.11.029 (zbMATH Zbl
1205.11029; title as indexed begins 'Indexes of unsplittable minimal zero-sum ...').  It classifies the unsplittable minimal
zero-sum sequences over C_n of length floor(n/2) + 1 = I(C_n) - 1.  Even-n part as restated verbatim in J. Peng, F. Sun,
'On the unsplittable minimal zero-sum sequences over finite cyclic groups of prime order', arXiv:1409.1970v1 (submitted
2014-09-06), Theorem 1.3(2), citing [26, Theorem 3.1]:
  "If n is even, then either S = (2g)^(n/2-1) (x_1 g) ((n + 2 - x_1) g), where 2 does not divide x_1, ... or
   S = g^t (n/2 g) ((1 + n/2) g)^(2l), where ... t + 2l = n/2.  Moreover ind(S) >= 2."
  (PDF extraction lost the 'not equal' in x_1 != n + 2 - x_1 and some exponent layout; the conditions elided as '...' are
  not recorded.)  Scope confirmed by P. Yuan, CANT 2016 slides 'Unsplittable minimal zero-sum subsequences over C_n',
  slide 25: 'Xia and Yuan 2010 (Discrete Math) determined all unsplittable minimal zero-sum sequence of length
  |S| = floor(n/2) + 1.'  The zbMATH review is garbled (drops 'unsplittable') and is not used.
Trust boundary.  The lane opened no source; it relies on the scout audit run screening/olson-zero-sum-priority-audit-v1.json
(sha256 28e9e5678e958d5339912b110ba2bfbe493bf7fdaaf36c0bc8d729d9cc64d93c; findings 0, 1, 3, 9 and theorem_comparison 3) and the parent's note run
review/olson-priority-parent-note-v1.md (sha256 6e62cca7d56196792d2cf704eb7b82cd7cd7f3e791e1c33f30e76f21fc0604ed; the parent independently read Peng-Sun Sec. 1, Thm 1.3 and the
Thm 1.5 proof).  Xia-Yuan's primary text was NOT read (ScienceDirect HTTP 403; nothing bypassed); its exact hypotheses on
n (the audit records an open question about an n = 9 exception) are not verified.  The use here is n = 2p, even, n >= 14 for
the lane's applications (p >= 7); p = 5 (n = 10) is covered only if Thm 3.1 includes n = 10.
The splitting monotonicity (stated in Peng-Sun Sec. 1 and the proof of their Thm 1.5, and in Gao-Li-Yuan-Zhuang, Arch.
Math. 105 (2015) 361-370, Sec. 1) is NOT imported: it is proved in Sec. 3.

## 3. Lemma SPLIT (proved here)

Let M be a minimal zero-sum sequence over C_n and M' := M x^(-1) y z with y + z = x, y, z != 0, M' a minimal zero-sum
sequence.  Then ||M||_g <= ||M'||_g for every generator g; hence ||M'||_g = 1 implies ||M||_g = 1.
Proof.  |y|_g + |z|_g is a positive integer congruent to |x|_g modulo n, and |x|_g is the least positive integer in its
class, so |x|_g <= |y|_g + |z|_g; summing, n ||M||_g <= n ||M'||_g.  If n ||M'||_g = n, then n ||M||_g is a positive multiple
of n (M is a zero-sum of nonzero terms) that is <= n, so it equals n.  []

## 4. Parity check of both Xia-Yuan families at n = 2p (the only property of (I2) used)

Claim P.  Every unsplittable minimal zero-sum sequence S of length p + 1 over C_(2p) that consists of odd elements is
g^p (pg) for a generator g, and has index 1.
Proof.  By (I2) (n = 2p even, floor(n/2) + 1 = p + 1), S belongs to one of the two families.
- Family A, (2g)^(p-1) (x_1 g) ((2p + 2 - x_1) g): the term 2g lies in 2C_(2p) for EVERY g (generator or not) and occurs
  p - 1 >= 4 times; so S contains an even element: excluded.
- Family B, g^t (pg) ((p + 1) g)^(2l) with t + 2l = p: (p + 1) g = 2 ((p + 1)/2) g lies in 2C_(2p) for every g; if l >= 1, S
  contains an even element: excluded.  If l = 0 (whether or not the elided conditions exclude it), S = g^p (pg).  All terms
  odd forces g odd; g = p would give S = p^(p+1), which contains the proper zero-sum p p: not minimal.  So g is a generator,
  and sum |.|_g = p * 1 + p = 2p: index 1.  []
(With the full statement 'ind(S) >= 2' no all-odd unsplittable S of length p + 1 exists at all; this is not needed.)

## 5. Derivation of IDX1-odd(p+1) and of S(p)

Theorem.  For every prime p >= 5 (n = 2p within the range of (I2)), every minimal zero-sum sequence M of p + 1 odd elements
of C_(2p) has index 1.
Proof.  If M is unsplittable, Claim P.  If M is splittable, M' := M x^(-1) y z is a minimal zero-sum sequence of length
p + 2 = floor(2p/2) + 2, so by (I1) it has a 1-element basis {a}.  M' contains the p >= 5 odd terms of M other than x;
an odd element is not a multiple of an even element, so a is odd; a = p would make every term of M' equal to p, and p p
would be a proper zero-sum of M' (length p + 2 > 2): impossible.  So a is a generator and ||M'||_a = 1; Lemma SPLIT gives
||M||_a = 1.  []
Equivalence (lane, evidence/notes-Sp-IDX1-v1.md, sha256 7af84f0d10670594c90274af9d9a70bc2e4a067b7b59a4e691d8a72500d31e53; repeated in full).
(IDX1-odd(p+1) => S(p)) Let U be zero-sum-free, p odd terms; x := -sigma(U) is odd (a sum of p odd elements is odd), so
x != 0.  M := U x is a zero-sum of length p + 1, minimal: a proper nonempty zero-sum avoiding x lies in U; one containing x
leaves a nonempty zero-sum M - S inside U.  Index 1 of M with generator g gives sum_U |.|_g = 2p - |x|_g <= 2p - 1: U is SC.
(S(p) => IDX1-odd(p+1)) For M all-odd minimal of length p + 1 and a term m, U := M - m is zero-sum-free of length p; SC
with g gives m = -sigma(U) = (2p - sum_U |.|_g) g, so |m|_g = 2p - sum_U |.|_g and sum_M |.|_g = 2p.  []
Hence Import S(p) holds at the trust level of Sec. 2.

## 6. Controls and cross-checks (NOT premises)

- Involution case without any import: if U contains pg, then U = g^(p-1) (pg) (parent's argument, checked in
  evidence/notes-Sp-involution-reduction-v1.md, sha256 233b1cb1a1815ba0e5793a97b322104d8299ed75f408661aca1844e31abd843f); the import is needed only for sequences of units.
- Lane probe v13 (code/sp_falsify_probe_v13.py 9b0d6a7aab239c1b4fa8cb5453afc090cdc00219b83689fb16623ff5ab1a6e88, gated launcher, pid 57453, rc 0; recorded in
  notes-Sp-IDX1-v1.md): complete canonical enumeration, every zero-sum-free odd sequence of length p is SC for
  p = 5, 7, 11, 13, 17.
- Parent finite control run review/olson-sp-import-parent-control-v1.json (sha256 133396151e311a6b51993c29f8f6bb35bfd0646387bb1516dd5cb8d84fa9860b; status
  PARENT_FINITE_CONTROL_NOT_PREMISE): exhaustive all-odd minimal zero-sums of length p + 1 over C_(2p): p = 5: 8, p = 7: 18,
  p = 11: 70, every one of index 1; the all-odd minimal sequence g^(p-4) ((p+2) g)^2 (pg) of length p - 1 has index 2 for
  p = 7, 11, 13, 17, 19 (index 1 at p = 5).  So index 1 can fail for all-odd minimal zero-sums just below length p + 1, and
  for general sequences at length p + 1 (Family B with l >= 1, e.g. the parent's 1^(p-2) p (p+1)^2): the all-odd
  restriction and the length p + 1 are both used.
- The scout's cross-check via the Savchev-Chen 2017 (J. Number Theory 177) unsplittable forms is slide-level and its own
  arithmetic; not used.

## 7. Uses in the lane

- evidence/proof-KPS-v4.md (to be frozen next): Theorem ROT-KP+ and its Corollary hold relative to this import (no longer
  conditional on an open statement).
- evidence/notes-LS-base-v1.md + erratum 1: its clauses 'under S(p)' read 'relative to Import S(p)'; not restated here.
