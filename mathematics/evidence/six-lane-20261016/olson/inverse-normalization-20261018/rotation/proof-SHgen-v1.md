# Theorem SHgen: heavy rotations of arbitrary odd weights (RGR shape, length 4p-2), under explicit bounds

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T05:49:34-07:00.  Status [W], UNREVIEWED.
Generalises Theorems SH3+- (proof-SH3-v4.md) and SHm (proof-SHm-v1.md) from heavies +-3c to heavies of any odd weight
3 <= |b| <= p-2, with cruder side conditions.  Not ROT(p).
Imports: GRX (any representation), PM*, K1 (accepted lowodd verdict 0853f4ac); Corollary B'(b), the C1 composition,
Theorem KBH, the uncapped implication of Theorem KB (accepted RUNS assembly v4, verdict 82adbddd; KB/KBH scopes
confirmed by the parent; KB's capped case is shown impossible in Lemma Ua below); Davenport-alpha (V); trivial cut.

## 1. Setting and statement

p >= 5; w a word of length 4p-2 over D_(2p), F, R >= 1, constant maximal cyclic reflection runs, brought to all-odd
form by PM* (k >= 2 blocks; k = 1 is Proposition K1), runs nonempty, H = sum (l_i - 1)/2, kappa = p-1-H.  For c != 0
call rho_c, rho_-c LIGHT and every other rotation x HEAVY, with signed weight b_x: the odd integer with x = b_x c (mod p)
and |b_x| <= p-2 (every x not in {0, c, -c} has exactly one such b_x; x = 0 is excluded by the hypotheses).
eta := number of heavies >= 1, a_max := max |b_x|, E := sum (|b_x| - 1), L1 := R - eta (number of lights).

**Theorem SHgen.**  If no rotation equals rho_0, and
  (H)  H >= E/2,      (L)  L1 >= a_max,      (K)  k <= 2p - eta - (5 a_max + 5)/2,
then w has an identity 2p-subword.

## 2. Lemma Ua (single heavy: the expanded word is solvable)

Let eta = 1, h the heavy, b = b_h, a = |b|, s = sign(b), and H >= (a-1)/2.  Let u° be w with h replaced in place by
a copies of rho_(sc) and (a-1)/2 equal pairs deleted from blocks (never emptying a block; parities kept).  Then u° (an
RGR word of length 4p-2, F, R >= 1, runs nonempty, all blocks odd, kappa(u°) = kappa + (a-1)/2 >= 1) is solvable.
Proof.  Suppose u° avoids.  Normalise u° by v -> -v so that A° >= B° (majority / minority counts).  A° >= 2p: trivial
cut.  B° > kappa(u°): (rho_c rho_-c)^(kappa(u°)+1) is a zero-sum of length 2kappa(u°)+2 <= 2p.  B° < kappa(u°):
Corollary B'(b) (B° >= 1) or C1 (B° = 0).  B° = kappa(u°) >= 1: (V) gives kappa(u°) <= k-1; KBH if k >= p+1; if
k <= p, KB's uncapped implication applies unless some run G has A°_G - B°_G >= 2p-1, i.e. G holds all A° = 2p-1
majority copies and no minority copy, all other runs holding only minority copies, B° = kappa(u°) in total.
 - The a copies have the minority sign: they lie outside G, so the k-1 nonempty runs other than G contain
   kappa(u°) - a + 1 rotations of w; then k - 1 <= kappa(u°) - a + 1 < kappa(u°) <= k - 1: impossible.
 - The a copies have the majority sign: w has 2p-1-a majority lights and kappa(u°) = kappa + (a-1)/2 >= kappa + 1
   minority lights; as H >= (a-1)/2, kappa <= p-1-(a-1)/2 < 2p-1-a (a <= 2p-3), so both light counts exceed kappa and
   (rho_c rho_-c)^(kappa+1) is a zero-sum of w of length 2kappa+2 <= 2p, forbidden by the GRX zero pattern of w; so
   w does not avoid, which is the claim of the theorem anyway.
So u° is solvable (or w is not an avoider).  []

## 3. Lemma FLEXa (one expansion; other heavies may be present)

Let w avoid (eta >= 1), h a heavy with a = |b_h| <= p-2, H >= (a-1)/2, and u° as in Lemma Ua (only h expanded).
Assume (F1) L1 >= a and (F2) k <= 2p - eta - (5a+5)/2.  Then u° has no identity 2p-subword.
Proof.  Suppose u° has one: pattern z (plus-set P), C° reflections, a multiset Q of m° = 2p - C° rotations (EVEN);
with s0 = 2kappa + 2 - Phi, s1 = 2p - Phi (w's count bounds) we have d := m° - s0 >= a - 1 (C_max(u°) = C_max(w) - (a-1))
and e := s1 - m° >= 0.  By z -> -z the copies are effective-positive.  n, M: numbers of effective-positive /
effective-negative lights of w (n + M = L1); u_X, v_X: unused / used (by Q) positive lights; u_Y, v_Y likewise for
negative lights; i: copies used by Q; S: other heavies used by Q (kept as they are; |S| <= eta - 1).
If i = 0, Q is a selection of w; if i = a, replacing the copies by h gives count m° - (a-1) >= s0.  Let 1 <= i <= a-1.
 (down) drop the i copies, add r3 unused positive lights and drop r4 used negative lights, r3 + r4 = i: signed sum
   unchanged, count change -2 r4.  Possible iff some r4 in [max(0, i - u_X), min(i, v_Y)] has 2 r4 <= d.
 (up) replace the i copies by h, drop r1 used positive lights and add r2 unused negative lights, r1 + r2 = a - i:
   signed sum unchanged, count change 1 - a + 2 r2 (>= -d automatically).  Possible iff some r2 in
   [max(0, a - i - v_X), min(a - i, u_Y)] has 1 - a + 2 r2 <= e.
All counts produced are even (all absolute weights odd) and lie in [s0, s1]; by GRX w would then have a solution,
contradicting avoidance.  It remains to see that one of (down), (up) is possible.
(down) is impossible iff [u_X + v_Y < i] or [2(i - u_X) > d with i > u_X];  (up) is impossible iff
[v_X + u_Y < a - i] or [a + 1 - 2i - 2v_X > e with a - i > v_X].
 (i)  u_X + v_Y < i and v_X + u_Y < a - i: adding, L1 = n + M < a, contrary to (F1).
 (ii) u_X + v_Y < i and a + 1 - 2i - 2v_X > e = s1 - m° = s1 - (i + v_X + v_Y + |S|): then
      s1 < a + 1 - i - v_X + v_Y + |S| < a + 1 + |S| <= a + eta (using v_Y < i), so Phi > 2p - a - eta and
      k >= Phi > 2p - a - eta, contrary to (F2) since (5a+5)/2 >= a.
 (iii) 2(i - u_X) > d and v_X + u_Y < a - i: then m° < s0 + 2i <= s0 + 2a; u_X < i - (a-1)/2, v_X < a - i, so
      n < (a+1)/2; u_Y < a - i, so m° >= v_Y = M - u_Y > M - a; hence M < s0 + 3a and
      L1 = n + M < s0 + (7a+1)/2 = 2kappa + 2 - Phi + (7a+1)/2.  With L1 = R - eta = 2p + 2kappa - k - eta this gives
      k > 2p - eta - (7a+5)/2 + Phi.  [Sharper: m° >= i + v_Y and m° < s0 + 2i give v_Y < s0 + i, M < s0 + a,
      L1 < s0 + (3a+1)/2, k > 2p - eta - (3a+5)/2 + Phi.]  Either form contradicts (F2), whose bound (5a+5)/2 exceeds
      (3a+5)/2.
 (iv) 2(i - u_X) > d >= a - 1 and a + 1 - 2i - 2v_X > e >= 0: then i > (a-1)/2 and i < (a+1)/2, impossible for odd a.
So (down) or (up) is possible.  []
[Note on (iii): the sharper chain is the one used for (F2); the cruder one is recorded for checking.]

## 4. Proof of Theorem SHgen

Induction on eta.  eta = 1: Lemma Ua gives a solution of u°, and Lemma FLEXa (with eta = 1; (F1), (F2) are (L), (K))
says that this is impossible for an avoider w.  eta >= 2: suppose w avoids; expand one heavy h_j (weight a_j) as in
Lemma Ua.  u° is RGR of length 4p-2, with eta - 1 heavies, H(u°) = H - (a_j - 1)/2 >= (E - (a_j - 1))/2,
L1(u°) = L1 + a_j >= a_max(u°), the same k <= 2p - (eta - 1) - (5 a_max(u°) + 5)/2; by induction u° is solvable,
and Lemma FLEXa (whose (F1), (F2) follow from (L), (K)) contradicts avoidance of w.  []

## 5. Scope

Covered: RGR shape, length 4p-2, any kappa, heavies of any odd weights 3..p-2 (any number), provided enough spare
reflection pairs (H >= E/2), enough lights (L1 >= a_max) and k <= 2p - eta - (5a_max+5)/2.  For heavies +-3c the
sharper Theorems SH3+- (no k condition, eta = 1) and SHm (k <= 2p-4-eta) apply.
Not covered: rho_0; H < E/2; very short light supply; near-alternating words (k above the bound); non-constant
reflection runs.
