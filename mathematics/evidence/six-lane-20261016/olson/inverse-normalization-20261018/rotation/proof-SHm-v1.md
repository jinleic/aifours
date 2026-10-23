# Theorem SHm: several heavy rotations of values +-3c (RGR shape, length 4p-2)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T05:46:12-07:00.  Status [W], UNREVIEWED.
Extends Theorem SH3+- (proof-SH3-v4.md, sha256 321978ff...b06c, unreviewed) from one heavy rotation to eta heavy
rotations by induction, under explicit bounds.  Not ROT(p).
Imports: GRX (any representation), PM* (accepted); Theorem SH3+- (base case, with its own imports listed there).

## 1. Statement

**Theorem SHm.**  Let p >= 5 and let w be a word of length 4p-2 over D_(2p) with F, R >= 1 and constant maximal
cyclic reflection runs; bring it to all-odd form by PM* (k blocks, runs nonempty, H = sum (l_i - 1)/2,
kappa = p-1-H).  Suppose that for some c != 0 all rotations are rho_c or rho_-c except eta >= 1 rotations ("heavies"),
each equal to rho_(3c) or rho_(-3c), and that
    H >= eta,    eta <= p - 3,    k <= 2p - 4 - eta.
Then w has an identity 2p-subword.

## 2. Lemma STEP (one expansion, other heavies present)

Let w be as in Sec. 1 (any eta >= 1, H >= 1), suppose w avoids, let h be a heavy of sign s, and let u° be w with h
replaced in place by rho_(sc)^3 and two letters deleted from one block of length >= 3.  If u° has an identity
2p-subword and eta <= p-3 and k <= 2p - 4 - eta, then so does w (a contradiction).
Proof.  R >= k (runs nonempty) and R = 2p + 2kappa - k give R >= p, so the number of light rotations (rho_c, rho_-c)
is L1 = R - eta >= 3.  Fix a solution of u°: pattern z (plus-set P), C° reflections, a multiset Q of m° = 2p - C°
rotations, m° EVEN, s0 + 2 <= m° <= s1 with s0 = 2kappa + 2 - Phi, s1 = 2p - Phi (w's bounds; C_max(u°) =
C_max(w) - 2).  By z -> -z assume the three copies are effective-positive.  Let n, M be the numbers of effective-
positive and effective-negative LIGHT rotations of w (n + M = L1), l+ <= n and l- <= M the numbers Q uses, and i the
number of copies Q uses; the other heavies used by Q are kept unchanged.  Replacing (part of) Q as below keeps the
signed sum (copies and lights have absolute weight 1, h has 3) and gives an even count in [s0, s1]:
 i = 0: Q itself (count m°).   i = 3: the copies -> h (count m° - 2).
 i = 1 (O1) copy -> an unused X-light (0); (O2) drop the copy and a used Y'-light (-2); (O3) copy and two used X-lights
   -> h (-2); (O4) copy and one used X-light -> h and one unused Y'-light (0); (O5) copy -> h and two unused Y'-lights
   (+2, needs m° + 2 <= s1).  [X-light = effective-positive light, Y'-light = effective-negative light.]
   If all fail: l+ = n, l- = 0, n <= 1, so M >= 2 (L1 >= 3); then (O4) failing forces n = 0 and (O5) failing forces
   m° = s1.  Q then consists of the copy and of other heavies only, so 2p - Phi = m° <= 1 + (eta - 1) and
   k >= Phi >= 2p - eta, contrary to k <= 2p - 4 - eta.  (Phi = 0 would need m° = 2p <= eta.)
 i = 2 (P1) two copies -> two unused X-lights (0); (P2) two copies and a used Y'-light -> one unused X-light (-2);
   (P3) drop two copies and two used Y'-lights (-4, needs m° - 4 >= s0); (P4) two copies and a used X-light -> h (-2);
   (P5) two copies -> h and one unused Y'-light (0).
   If all fail: l+ = 0, l- = M, n <= 1, and since M = L1 - n >= 2, (P2) failing forces n = 0 and (P3) failing forces
   m° < s0 + 4.  But m° >= 2 + M = 2 + L1, so R - eta = L1 < 2kappa + 4 - Phi, i.e. k > 2p - 4 - eta + Phi
   >= 2p - 4 - eta, contrary to the hypothesis.
In every case w has a solution (GRX).  []

## 3. Proof of Theorem SHm

Induction on eta.  eta = 1 is Theorem SH3+- (which needs only H >= 1).  For eta >= 2 suppose w avoids; pick a heavy h
and form u° as in Lemma STEP.  u° is an RGR-shape word of length 4p-2 with F, R >= 1, eta - 1 heavies of values +-3c,
H(u°) = H - 1 >= eta - 1, eta - 1 <= p-3 and the same k <= 2p - 4 - (eta - 1); by induction u° has an identity
2p-subword, and Lemma STEP gives one of w.  []

## 4. Scope

Covered: RGR shape, length 4p-2, any kappa, every heavy equal to +-3c, with H >= eta, eta <= p-3 and
k <= 2p - 4 - eta.  Not covered: too few spare reflection pairs (H < eta), near-alternating words
(k >= 2p - 3 - eta), very many heavies, heavy values other than +-3c, non-constant reflection runs.
