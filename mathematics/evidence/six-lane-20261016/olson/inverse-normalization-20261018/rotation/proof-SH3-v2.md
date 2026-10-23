# Theorem SH3+-: one heavy rotation of value 3c or -3c cannot occur in an RGR-shape avoider of length 4p-2

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T05:39:02-07:00.  Status [W], UNREVIEWED.
Supersedes proof-SH3-v1.md (02968482...278f1, kept): v2 removes the orientation hypothesis #rho_-c <= #rho_c (both
signs of the heavy are covered) by showing that the expanded word u° is ALWAYS solvable (Lemma U), using two more
accepted lemma imports (Theorems KB and KBH) whose capped/inherited side conditions are shown not to arise.
Not ROT(p): exceptions H = 0 and the shape (E*) remain, and words with more than one heavy rotation are not covered.

Imports (accepted at their exact cited scopes; the parent should confirm that KB and KBH are used within scope):
GRX (any representation) and PM* [R/olson-rotation-lowodd-parent-verdict-v2.md]; from the RUNS assembly
[R/olson-runs-assembly-proof-v4.md; verdict R/olson-runs-parent-verdict-v1.md]: Corollary B'(b) (RGR, length 4p-2,
F, R >= 1, A >= B, 1 <= B < kappa => solvable); the C1 composition (same with B = 0 < kappa); Theorem KB
(inverse-parity/proof-PAR-Kplus-partial-r2.md Sec. 6: RGR length 4p-2, F, R >= 1, A >= B, B = kappa >= 1, (V),
o_F <= p, any k; (D0) assumed only if the OR-merged word has a segment G with A_G - B_G >= 2p-1 => solvable); Theorem
KBH (inverse-run-count/kappaB-high/proof-KBH.md Sec. 1: RGR length 4p-2, F, R >= 1, A >= B, B = kappa, at least p+1
odd reflection runs => solvable, no inherited hypothesis); Davenport-alpha ((V): an avoider has kappa <= o_F - 1);
the trivial cut (2p equal rotations rho_x multiply to 1).

## 1. Statement

**Theorem SH3+-.**  Let p >= 5 and let w be a word of length 4p-2 over D_(2p) with F, R >= 1 and constant maximal
cyclic reflection runs.  Suppose that for some c != 0 every rotation of w is rho_c or rho_-c except exactly one
rotation h in {rho_(3c), rho_(-3c)}.  After Lemma PM* (all k blocks odd, runs nonempty) assume H >= 1 and that w is not
of the shape (E*): k = 2p-2, every run a single rotation, H = 1.  Then w has an identity 2p-subword.

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

## 3. Lemma FLEX (every solution of u° gives one of w, outside (E*))

This is Sec. 2 of proof-SH3-v1.md verbatim, which never used the sign of h: fix a solution of u° with pattern z
(plus-set P), C° reflections, q+ effective-positive and q- effective-negative copies (by z -> -z assume the three
expansion copies are effective-positive), m° = q+ + q- in [s0+2, s1] even, s0 = 2kappa + 2 - Phi, s1 = 2p - Phi.
With X = the effective-positive rotations of w (h and n weight-1 ones) and M = #effective-negative rotations of w, the
cases q+ <= n (count m°), q+ >= 3 (count m° - 2), (n, q+) = (0,1) (count m° - 2), (1,2) (count m° - 2 or m°), (0,2)
(count m° or m° - 4) give a w-selection with signed sum (q+ - q-) c and even count in [s0, s1], except in (0,2) when
q- = M and R + 1 < 2kappa + 6 - Phi, which forces H = 1, k = 2p-2 and R = k, i.e. (E*).  By GRX, w is solved.  []

## 4. Proof of the theorem

If w avoids, Lemma FLEX turns the solution of u° given by Lemma U into a solution of w (w is not of shape (E*)):
contradiction.  []

## 5. Scope and remaining cases (precise)

Covered: every RGR-shape word of length 4p-2 whose rotations lie in {rho_c, rho_-c} except one rho_(+-3c), with H >= 1,
not (E*), any kappa, any number of odd blocks, the heavy alone in its run or not.  This is the configuration of every
non-rigid avoider found at lengths 4p-4 and 4p-5 (README log; observation only).
Not covered: H = 0 (no spare reflection pair), the shape (E*), two or more heavy rotations, heavy values other than
+-3c, and non-constant reflection runs (u° would keep the empty runs; REFL needed).  kappa = 0 with several heavies is
covered separately by Theorem ELT0 (proof-ELT0-v2.md) under global fullness.
