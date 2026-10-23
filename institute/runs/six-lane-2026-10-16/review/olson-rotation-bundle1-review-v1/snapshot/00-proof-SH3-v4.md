# Theorem SH3+-: one heavy rotation of value 3c or -3c cannot occur in an RGR-shape avoider of length 4p-2 (H >= 1), v4

Owner OlsonRotationRigidity.  v4 assembled after host clock 2026-10-18T05:4x (label not a clock read; bounded by the
README entry that records its sha256).  Status [W], UNREVIEWED.  v4 = v3 (proof-ROT... proof-SH3-v3.md, kept) made
SELF-CONTAINED at the parent's request: Sec. 2 (Lemma U, including the impossibility of KB's capped case) is copied
verbatim from proof-SH3-v2.md Sec. 2 instead of being cited.  No mathematical change from v3.  v1, v2, v3 kept.
Imports (parent-confirmed scopes, IRC between 05:40:13 and this assembly): GRX (any representation), PM*, K1
[R/olson-rotation-lowodd-parent-verdict-v2.md]; from the RUNS assembly v4 [verdict R/olson-runs-parent-verdict-v1.md,
82adbddd...9237]: Corollary B'(b); the C1 lemma composition (OR, then S1'/A1'/trivial cut if o_F <= p, C0-B'/A1/trivial
cut otherwise); Theorem KBH (kappaB-high/proof-KBH.md L10-14: RGR, F, R >= 1, A >= B, B = kappa >= 1, o_F >= p+1 =>
solvable, no inherited hypothesis); Theorem KB (inverse-parity/proof-PAR-Kplus-partial-r2.md L238-273, UNCAPPED
implication only: no (D0) is used; the capped case is shown impossible below, inside this file); Davenport-alpha (V)
(an avoider has kappa <= o_F - 1); the trivial cut.  KB and KBH are applied only to the genuine RGR word u° of length
4p-2.

## 1. Statement

**Theorem SH3+-.**  Let p >= 5 and let w be a word of length 4p-2 over D_(2p) with F, R >= 1 and constant maximal
cyclic reflection runs.  Suppose that for some c != 0 all rotations of w are rho_c or rho_-c except exactly one
rotation h in {rho_(3c), rho_(-3c)}, and that after Lemma PM* (all k blocks odd, runs nonempty) H >= 1.  Then w has an
identity 2p-subword.
(If k = 1, Proposition K1 (accepted) already forces all rotations equal; so assume k >= 2.)

## 2. Lemma U (the expanded word is solvable)

Let s = +1 if h = rho_(3c), s = -1 if h = rho_(-3c).  Let u° be w with h replaced in place by rho_(sc) rho_(sc) rho_(sc)
and two letters deleted from one block of length >= 3.  Then u° (an RGR word of length 4p-2, F, R >= 1, runs nonempty,
all blocks odd, k blocks, kappa(u°) = kappa + 1 >= 1) has an identity 2p-subword.
Proof.  Suppose u° avoids.  Write a = #rho_c(w), b = #rho_-c(w); the counts of u° are a + 3, b (s = +1) or a, b + 3
(s = -1).  Normalise u° by v -> -v so that its majority count A° >= its minority count B°; let sigma be the sign (in
u°'s normalisation) of the three expansion copies.  If A° >= 2p the trivial cut solves u°; so A° <= 2p-1.
If B° > kappa(u°): (rho rho^-1)^(kappa(u°)+1) is a zero-sum of length 2kappa(u°)+2 <= 2p (all-plus pattern) - solved.
If B° < kappa(u°): (B') (B° >= 1) or (C1) (B° = 0) - solved.
If B° = kappa(u°) (>= 1): u° avoids, so (V) gives kappa(u°) <= k - 1.  If k >= p+1, KBH solves u°.  If k <= p, KB solves
u° provided its capped case does not arise.  All blocks are odd, so the OR-segments are the single runs; a capped
segment G has A°_G - B°_G >= 2p-1, hence A°_G = A° = 2p-1 and B°_G = 0: G holds every majority copy and every other
run holds only minority copies, B° = kappa(u°) of them.
 - If sigma is the minority sign, the three expansion copies lie in a run other than G, and the k-1 nonempty runs
   other than G contain only kappa(u°) - 3 + 1 = kappa(u°) - 2 rotations of w: k - 1 <= kappa(u°) - 2, contradicting
   kappa(u°) <= k - 1.
 - If sigma is the majority sign, then A° = (majority count of w) + 3 = 2p-1, so w has 2p-4 rotations of the majority
   value, while its minority value occurs B° = kappa(u°) = kappa + 1 > kappa times; then
   (rho_c rho_-c)^(kappa+1) is a zero-sum of w of length 2kappa + 2 <= 2p (kappa + 1 <= 2p-4), contradicting the GRX zero
   pattern of the avoider w (forbidden lengths [2kappa+2, 2p]).  [If w does not avoid, the theorem holds anyway.]
So the capped case does not arise, KB applies, and u° is solved.  []

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
