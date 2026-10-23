# Theorem SH3+-: one heavy rotation of value 3c or -3c cannot occur in an RGR-shape avoider of length 4p-2 (H >= 1)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T05:40:13-07:00.  Status [W], UNREVIEWED.
Supersedes proof-SH3-v2.md (b81fe382...a2031, kept) and v1 (kept).  Change from v2: the exceptional shape (E*) is
REMOVED: in the only case of Lemma FLEX that could fail, the count m° = R + 1 must be even, which (E*) (R = 2p-2)
violates; the zero-pattern subcase (Phi = 0) is treated separately.  Remaining hypotheses: RGR shape, H >= 1.
Imports: as proof-SH3-v2.md (GRX, PM*, K1; Corollary B'(b); the C1 composition; Theorems KB and KBH at their cited
scopes - parent confirmation pending for KB/KBH; Davenport-alpha (V); trivial cut).

## 1. Statement

**Theorem SH3+-.**  Let p >= 5 and let w be a word of length 4p-2 over D_(2p) with F, R >= 1 and constant maximal
cyclic reflection runs.  Suppose that for some c != 0 all rotations of w are rho_c or rho_-c except exactly one
rotation h in {rho_(3c), rho_(-3c)}, and that after Lemma PM* (all k blocks odd, runs nonempty) H >= 1.  Then w has an
identity 2p-subword.
(If k = 1, Proposition K1 (accepted) already forces all rotations equal; so assume k >= 2.)

## 2. Lemma U

Exactly as proof-SH3-v2.md Sec. 2: with s the sign of h, u° := w with h replaced by rho_(sc)^3 and two letters deleted
from a block of length >= 3 has an identity 2p-subword (trivial cut; zero pattern if minority > kappa(u°);
Corollary B'(b) / C1 if minority < kappa(u°); KBH or KB if minority = kappa(u°), the capped case of KB being impossible
by counting, (V) for u°, and the zero pattern of w).

## 3. Lemma FLEX (no exceptions)

Suppose w avoids; fix a solution of u°: pattern z (plus-set P), C° reflections, m° = 2p - C° rotations, EVEN, with
s0 + 2 <= m° <= s1 where s0 = 2kappa + 2 - Phi, s1 = 2p - Phi are w's count bounds (C_max(w) = 2H + Phi).  By z -> -z
assume the three copies of h are effective-positive.  X := effective-positive rotations of w (h and n weight-1
rotations), M := number of effective-negative rotations of w (all of weight 1).  The solution uses q+ effective-positive
copies and q- effective-negative ones (q+ + q- = m°), with signed sum (q+ - q-) c = T(z).  We give a w-selection with the
same signed sum and an even count in [s0, s1] (then GRX contradicts avoidance).
* q+ <= n: q+ weight-1 elements of X, q- negatives; count m°.
* q+ >= 3: h, q+ - 3 weight-1 elements of X, q- negatives; count m° - 2.
* (n, q+) = (0, 1): q- is odd, so >= 1; drop one negative (and the copy): count m° - 2.
* (n, q+) = (1, 2): if q- >= 1, the weight-1 element of X and q- - 1 negatives: count m° - 2; if q- = 0, h and one
  negative (M >= 1 since R >= p > 2): count m°.
* (n, q+) = (0, 2): (A) h and q- + 1 negatives, count m°, possible iff q- <= M - 1; (B) q- - 2 negatives only,
  count m° - 4, possible iff q- >= 2 and m° - 4 >= s0.  Suppose both fail: q- = M = R - 1, so m° = R + 1 and, m° being
  even, R is ODD; and R + 1 - 4 < s0 (M = R - 1 >= p - 1 >= 2 holds since R >= p).
  - Phi >= 2: R <= 2kappa + 2, so with R = 2p + 2kappa - k we get k >= 2p - 2; R >= k (runs nonempty) gives
    kappa >= p - 2, so H = 1, kappa = p-2, R = 4p - 4 - k >= k, k = 2p-2 and R = 2p-2: even, a contradiction.
  - Phi = 0: P is all runs, so w has no rotation rho_(sc) and its M rotations rho_(-sc) are all negative; T(z) = 0 gives
    2 - M = 0 mod p; m° >= s0(u°) = 2kappa + 4 gives M >= 2kappa + 2, and the failure gives M <= 2kappa + 3; M = R - 1 is
    even, so M = 2kappa + 2 and 2kappa = 0 mod p, kappa = 0, M = 2, R = 3 < p: a contradiction.
In all cases the count is m°, m° - 2 or m° - 4 >= s0, never above m° <= s1, and even.  []

## 4. Proof of the theorem

If w avoided, Lemma U would give a solution of u° and Lemma FLEX a solution of w.  []

## 5. Scope

Covered: every RGR-shape word of length 4p-2 whose rotations are rho_c, rho_-c except a single rho_(+-3c), with H >= 1
(any kappa >= 0, any number of odd blocks, the heavy alone in its run or not).
Not covered: H = 0 (all reflection blocks of length 1); two or more heavy rotations; heavy values other than +-3c;
non-constant reflection runs (u° keeps the empty runs: a solution would follow from REFL(p) of the reflection slice
applied to u°, not claimed here).
