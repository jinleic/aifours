# Notes on gap (a): SIGMA beyond (2HA) in the regime R >= 4 kappa - 4 (B = 0)

Owner OlsonReflectionRigidity.  r2 written after host clock 2026-10-18T12:27:08-0700: Lemma HOT (i) now states its split hypothesis
(r1, 20daf0db...eb0f, asserted the split without proof).  r1 was written after host clock 2026-10-18T12:26:21-0700.  Status: working notes [W].  Sec. 1 is a finite aid
(not a premise).  Sec. 2 holds short exact consequences of Lemmas C1/C2, proved here.

## 1. E17 (plan-E17.md 5ecd3f20..., code/e17_gap_a_probe_v2.py b53299fd..., out/e17_gap_a_probe.json 14dcab39...)

All-ones random arrangements.  Interval-feasible DFS leaves, at most 200 per datum, with a node cap of 2e6 per datum.
- (13, 4, 13), k = 21, Delta = 3: all 20 arrangements satisfy (2HA), so B0S-CJ''' covers them word by word.  4000 leaves, all
  with J = 0 and c = 0.
- (29, 7, 29), k = 43, Delta = 6: none of the 10 arrangements satisfies (2HA), as predicted since R < 6 Delta - 5.  Still,
  all 1400 leaves have J = 0 and c = 0 on every proper interval.
So interval-level SIGMA appears to hold in a gap-(a) cell where (2HA) is impossible.  A proof needs a mechanism other than two
disjoint heavy admissible intervals.

## 2. Lemma HOT (exact; setting of Lemmas C1, C2, i.e. B = 0, R >= 4 kappa - 4, avoider)

Call an interval light if its mass is <= 2 Delta - 2.
(i) Suppose J >= 1 and the cycle splits into two complementary arcs Q, Q^c of mass >= 2 Delta - 1 each.  Then some light
interval L has c(L) >= 1.
[r2: r1 claimed that such a split always exists because R >= 4 Delta - 2.  That needs granularity.  It does exist when some run
has mass >= 2 Delta - 1 (take Q = that run and use (F2)).  It also exists when every run has mass <= R - 4 Delta + 4, because a
prefix sweep then lands in [2 Delta - 1, R - 2 Delta + 1].  This covers all-ones words, as R >= 4 kappa - 4 >= 4 Delta.]
Proof.
- c(Q) + c(Q^c) = J >= 1, so one of them, say Q, has c(Q) >= 1.  Let L be an inclusion-minimal sub-interval of Q with c(L) >= 1.
- Then |L| >= 2, and L = L' u {t} with c(L') = 0 and c(L) > c(L') + c({t}), so (B') fails for the split (L', {t}, L^c).
- By Lemma C2(b) one of the three pair sums is < 2 Delta - 1.  m(L^c u {t}) >= m(Q^c) >= 2 Delta - 1, and R - r_t >= 2 Delta - 1
  by (F2) of proof-B0SCJ-r2.md.  So m(L) <= 2 Delta - 2.  []
(ii) Pairwise disjoint intervals I_1, ..., I_n, each with c >= 1, have n <= J.  By superadditivity (Lemma C2(a)) applied as in the
proof of Theorem B0S-CJ, J >= sum c(I_j) >= n.  []
(iii) If J = 1 and L is a light interval with c(L) >= 1, then:
- every interval containing L has c = 1 (superadditivity and c <= J);
- every interval disjoint from L has c = 0 (its complement contains L, and C1(b));
- in particular, all light intervals with c >= 1 pairwise intersect.  []
So J = 1 forces a single "hot spot".  Every interval avoiding it is exactly additive, and every interval containing it carries
the whole defect.  Excluding a hot spot from the windows near L would give SIGMA in the gap-(a) cells.  Not done.
