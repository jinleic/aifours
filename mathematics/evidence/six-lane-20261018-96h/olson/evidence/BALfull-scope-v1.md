# BAL-full: frozen scope (before proof text or probe)

Owner ContinueOlson.  Written after /bin/date 2026-10-19T00:56:33-0700, on parent instruction (IRC: 'prove/refute that some LONGEST
zero-sum Z is balanced (or stronger every Z if justified) WITHOUT the (B)/Lambda alternatives; freeze scope; distinguish
existential generator/Z choices').  k = p / S(p) stays a separate parked boundary.

## Setting (S') (ROT-ZR Setting (S) with the kappa-range replaced)
p >= 5 prime; 2 <= k <= p - 1; kappa integer, 1 <= kappa < p; Y a sequence of R = 2p + 2kappa - k odd elements of
C_(2p) with (S1) at kappa (every zero-sum subsequence has length <= 2kappa).  Additional hypothesis under test:
  (H*) 2kappa + k <= 2p - 1.
Z: a LONGEST zero-sum subsequence of Y (|Z| = 2t, so t <= kappa); Y' := Y - Z (zero-sum-free); L := |Y'| = R - 2t >= p + 1.
g: an INDEX-<1 GENERATOR of Y' (an odd generator with sum of least positive coefficients W <= 2p - 1; at least one exists by
SC0); m, slack, e' := W - L as in ROT-ZR REALIZE.  By ROT-ZR ZSTRUCT (valid for every such Z and g):
Z = g^(n+) (-s_1 g)...(-s_(n-) g), s_i odd, 1 <= s_i <= min(2t - 1, slack).  BALANCED: sum s_i = n+.

## Claims distinguished
- BAL-exists: for some longest Z and some index-<1 generator g of Y - Z, Z is balanced.
- BAL-forall: for every longest Z and every index-<1 generator g of Y - Z, Z is balanced.
- Only BAL-exists is needed by the SHgen route (the word step uses one Z and one g).  A proof of BAL-forall implies
  BAL-exists.  A refutation must exhibit Y (exact) with (S1), (H*), and every (Z, g) unbalanced (for BAL-exists), or one
  unbalanced (Z, g) (for BAL-forall).

## Consequence to be checked if BAL-forall/exists holds under (H*)
ROT-ZB's alternative (B)/(Lambda) becomes unnecessary: terminal 2 <= k <= p-1, kappa^ >= 1, 2kappa^ + k <= 2p - 1
(with (S1) from S1-sharp since kappa^ <= min(k-1, (2p-1-k)/2) <= (2p-2)/3) would give rotations in one nonzero pair, and
uniformly o_F <= p - 1 with F >= 2o_F - 1 would give INV* / ordered Olson.  This consequence will be stated only after
the proof text is frozen.

## Controls
Existing aid: probe v5 (support <= 3, p = 13, 17, 19 partly: no unbalanced (Z, g) beyond LAMBDA's range).  No new probe
is planned before the written proof; any later probe will get a gated-launcher PID record first and will not be offered
as a larger finite range.
