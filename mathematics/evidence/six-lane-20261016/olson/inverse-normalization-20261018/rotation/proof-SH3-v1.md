# Theorem SH3: one heavy rotation of weight 3 cannot occur in an RGR-shape avoider of length 4p-2 (any kappa, any o)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T05:32:55-07:00.  Status [W], UNREVIEWED.
Partial result toward ROT(p): it covers the configuration that every non-rigid avoider found at lengths 4p-4, 4p-5
has (exactly one heavy, value +-3c), when that heavy is POSITIVE relative to the majority sign, with one explicit
exceptional shape (E*).  Not ROT(p).
Imports: GRX (accepted, any representation); accepted Corollary B'(b) and the accepted lemma composition C1 (RGR words
of length 4p-2 with F, R >= 1, A >= B and B < kappa are solvable); Lemma PM* (accepted).

## 1. Statement

**Theorem SH3.**  Let p >= 5 and let w be a word of length 4p-2 over D_(2p) with F, R >= 1, of RGR shape (every maximal
cyclic reflection run constant).  Suppose that for some c != 0 every rotation of w is rho_c or rho_-c except exactly one
rotation h = rho_(3c), that #rho_-c <= #rho_c, and that w has a reflection run of length at least 3 after Lemma PM*
(i.e. H >= 1 in the all-odd form).  If w is not of the exceptional shape
  (E*) all runs (of the all-odd form) are single rotations, k = 2p-2, and H = 1,
then w has an identity 2p-subword.

## 2. Proof

By Lemma PM* we may assume all blocks odd (k blocks, k = o), all runs nonempty, maximal blocks; PM* keeps avoidance,
the rotation multiset, the length and H, so H >= 1 means some block has length >= 3.  kappa := p-1-H; F = 2H + k;
R = 2p + 2kappa - k.  Suppose w avoids.
Let w° be w with h replaced in place by rho_c rho_c rho_c and with two letters deleted from one block of length >= 3.
w° is an RGR word of length 4p-2 (blocks nonempty with their parities, runs nonempty), A(w°) = #rho_c + 3,
B(w°) = #rho_-c, kappa(w°) = kappa + 1.  The GRX zero pattern of w forbids zero-sums of even length in [2kappa+2, 2p];
(rho_c)^j (rho_-c)^j shows min(#rho_c, #rho_-c) = #rho_-c <= kappa.  Hence B(w°) < kappa(w°) <= ... and A(w°) >= B(w°).
If w° avoids, (B') (B(w°) >= 1) or (C1) (B(w°) = 0) is contradicted.  It remains to show that w° avoids.

Fix a pattern z with plus-set P; s0 := 2kappa + 2 - Phi and s1 := 2p - Phi are the admissible rotation-count bounds of w
(C_max(w) = 2H + Phi), while for w° (C_max(w°) = C_max(w) - 2) the counts must lie in [s0 + 2, s1].  The three copies of
rho_c that replace h lie on one side of the pattern: by the global sign change z -> -z (which swaps the two sides and
negates T(z) and all signed sums) assume they are effective-positive (h lies in a run of P).  Let X be the multiset of
effective-positive rotations of w (h, the rho_c of runs in P, the rho_-c of runs not in P) and n := |X| - 1 (the
weight-1 elements of X); the effective-negative rotations of w all have weight 1, there are M of them.  Then the
effective-positive weights realisable in w form [0, n] u [3, 3+n] (h used or not), with count equal to the weight
without h and weight - 2 with h; negative weights 0..M with count equal to the weight.
A solution of w° uses q+ effective-positive copies (0 <= q+ <= n+3) and q- effective-negative ones (0 <= q- <= M),
m° = q+ + q- in [s0+2, s1], even, with (q+ - q-) c = T(z).  We produce a w-selection with the same signed sum
(q+ - q-) c and an even count m in [s0, s1]; by GRX that is a solution of w, a contradiction.
* q+ <= n: take q+ weight-1 elements of X and q- negatives: m = m°.
* q+ >= 3: take h, q+ - 3 weight-1 elements of X (q+ - 3 <= n) and q- negatives: m = m° - 2 >= s0.
* n < q+ < 3, so (n, q+) in {(0,1), (0,2), (1,2)}:
  (A) h and q- + 3 - q+ negatives (needs q- + 3 - q+ <= M): signed sum 3 - (q- + 3 - q+) = q+ - q-,
      m = 1 + q- + 3 - q+ = m° + 4 - 2q+;
  (B) all n weight-1 elements of X and q- - (q+ - n) negatives (needs q- >= q+ - n): signed sum q+ - q-,
      m = m° - 2(q+ - n).
  (0,1): q- is odd (m° even), so q- >= 1 and (B) gives m = m° - 2 in [s0, s1].
  (1,2): (B) needs q- >= 1 and gives m = m° - 2; if q- = 0, (A) needs M >= 1 and gives m = m°.  M = 0 would mean that
         every rotation is effective-positive, i.e. R = |X| = 2; but R >= k and R = 2p + 2kappa - k give R >= p > 2.
  (0,2): (A) needs q- <= M - 1 and gives m = m°.  If q- = M, (B) gives m = m° - 4 and needs m° - 4 >= s0.  Here X = {h},
         so M = R + 2 - 3 = R - 1 and m° = R + 1; the remaining failure is R + 1 < s0 + 4 = 2kappa + 6 - Phi, i.e.
         2p - k < 5 - Phi.  As Phi >= 2 (a pattern isolating h has a sign change), k >= 2p - 2; with R >= k and
         R = 2p + 2kappa - k this forces kappa >= p - 2, i.e. H <= 1, so H = 1, kappa = p-2, k = 2p-2, R = 2p-2 = k:
         every run is a single rotation.  This is exactly the excluded shape (E*).
In every non-(E*) case the w-selection has an even count in [s0, s1] (all counts above are m°, m° - 2 or m° - 4 >= s0,
and none exceeds m° <= s1), so w has a solution.  Hence w° avoids, and the contradiction above proves the theorem.  []

## 3. Remarks

* kappa = 0 is also covered by Theorem ELT0 (proof-ELT0-v2.md); SH3 needs no fullness hypothesis at all: the single
  weight-3 heavy may sit alone in its run ("thin"), which defeated the per-run fullness of Theorem EXP.
* Negative orientation: if instead h = rho_(-3c) with #rho_-c <= #rho_c, apply SH3 with c' := -c only when
  #rho_c' = #rho_-c ... (orientation condition fails); the zero pattern then gives #rho_-c <= kappa - 2 and the same
  expansion (into rho_-c copies) yields B(w°) = #rho_-c + 3 <= kappa + 1 = kappa(w°): the argument closes unless
  #rho_-c = kappa - 2 (the boundary case found in all negative-heavy avoiders at lengths 4p-4..4p-6).  Written as
  part of the next version, not claimed here.
* Exceptional shape (E*): k = 2p-2 single-rotation runs, one block of length 3 and 2p-3 blocks of length 1.  Not
  treated here.
