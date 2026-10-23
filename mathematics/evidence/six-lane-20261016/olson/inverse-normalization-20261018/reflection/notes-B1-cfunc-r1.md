# Notes: the c-function for B >= 1 (pure runs, all blocks odd), toward k >= p + 1

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T12:22:50-0700.  Status: route notes [W].  Secs. 1-2 are exact
computations; Sec. 3 gives obstructions; nothing here is a theorem about avoiders.

## 1. Windows

Setting of MXG / RES_<(p): all blocks odd (beta = 0), every run pure (all rho_1, all rho_-1, or empty), A >= B >= 1, B < kappa.
Put d_t = a_t - b_t and D_Q = sum_(t in Q) d_t.
- By H0 (K0star-r2 L55-58) with m = 1, a proper interval Q has window I(Q) = [-g(R - E_Q), g(E_Q)], where
  E_Q := D_Q + B lies in [0, R] and g(E) = min(p - 1, E - kappa, floor(E/2)).  The complement's index is
  E_(Q^c) = D - D_Q + B = R - E_Q.
- So the windows are those of the B = 0 theory, with the mass m_Q replaced by the index E_Q.  But E is NOT additive:
  E_(Q1 u Q2) = E_(Q1) + E_(Q2) - B.

## 2. The split conditions

Singleton representatives, the c-function, J, and C1(a), C1(b) are exactly as in proof-B0SPP-r5.md Sec. 2; they use only the
window shape.  For a split Q = Q1 u Q2, Q3 = Q^c, write E_i := E_(Q_i).  Then E_1 + E_2 + E_3 = R + B, and the proof of C1(c) gives:
   (A_B) g(E_1) + g(E_2) + g(E_3) >= -2   implies  c(Q) >= c(Q1) + c(Q2);
   (B_B) g(E_2 + E_3 - B) + g(E_1 + E_3 - B) + g(E_1 + E_2 - B) >= p - 2   implies  c(Q) <= c(Q1) + c(Q2).
The three "pair indices" E_i + E_j - B add up to 2R - B.  Any two of them add up to R - B + E_shared >= R - B.
- (A_B) holds for every split if R + B >= 4 kappa - 3 (same computation as C2(a), with the sum R + B).
- (B_B), exactly one small pair index s (<= 2 kappa), the other two floor terms: (B_B) >= R - kappa - 1 + (s - B)/2 roughly.  So
  it holds if s >= 2 Delta + B - 1 (up to parity), where Delta := p + kappa - 1 - R = k - p - kappa - 1 as before.
- (B_B), no small pair index: (B_B) >= (2R - B - 3)/2.  This needs 2R >= 2p + B - 1.  [Unlike B = 0, this is NOT automatic:
  R >= p (from P0: n_E <= 2 kappa and R >= N_+ >= k - 2 kappa) does not give it when B >= 2 and R is close to p.]
- At most one pair index is small iff R - B >= 4 kappa + 1 (the analogue of (H)).

## 3. Consequences and obstructions

- Under (H_B): R - B >= 4 kappa + 1 and 2R >= 2p + B - 1.  Then (A_B) always holds, and (B_B) holds whenever all three pair
  indices are >= 2 Delta + B - 1 (to be re-derived exactly, with parity).  So Lemma CJ should carry over with "heavy" read on the
  index E, giving SIGMA (sum w_t = p) from two disjoint heavy admissible intervals.  NOT written as a lemma: the admissibility
  bookkeeping (non-additive E) has not been checked.
- SIGMA is not the bottleneck for B >= 1.  MXG's kill (Lemmas K, KL, GIANT, MIX-R', W, B1, A', KS', AC', ZP, C, R4') uses k <= p
  repeatedly, e.g. 2g + B <= k - 1 <= p - 1 with g := kappa - B (MXG L68), and phi_t <= g - 1 <= p - k + g (MXG L239).  Each
  use would need a replacement for k >= p + 1.
- RED's process, started from a mixed-rotation avoider, can end with B_T >= 1, so REFL-B0's composition does not extend to
  mixed rotations without a B >= 1 theorem for k >= p + 1.
