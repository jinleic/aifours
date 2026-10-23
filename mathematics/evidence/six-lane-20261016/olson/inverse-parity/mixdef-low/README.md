# mixdef-low: MIX_DEF on o_F <= p (the last open piece of PAR)

Owner OlsonParity (split agreed with OlsonRunCount 2026-10-17 ~06:20 PDT: OlsonRunCount takes
kappa = B with o_F >= p+1; OlsonParity takes kappa > B >= 1, starting with o_F <= p).
Host clock read just before freezing: 2026-10-17T06:27:02-07:00.

## 1. Frozen target

MIX_low(p), p prime >= 5: every RGR word v of length 4p-2 with all k reflection runs odd,
k <= p, A >= B >= 1, kappa := p - 1 - H with B < kappa <= k - 1, has an identity
2p-subword.  (By Lemma OR, ../proof-PAR-Kplus-partial.md Sec. 1, this gives K+_viol and hence
PAR(p) in the remaining range 1 <= B < kappa.)  g := kappa - B >= 1.

## 2. Frozen representation

Lemma H (../proof-PAR-K0.md Sec. 1) with beta = 0: for a pattern Q with m blocks,
D_Q := sum_{t in Q} d_t (d_t = a_t - b_t),
  U_Q = lambda(Q) - 1 = G_m(D_Q),  L_Q = G_m(D - D_Q),
  G_m(E) := min(p - m, E - g + m - 1, floor((E + B)/2)),
  window I(Q) = [-L_Q, U_Q];  D := A - B = 2p - k + 2g.
Normalisation allowed (rechecked in ../proof-PAR-Kplus-partial.md Sec. 4): Lemma M0 of
../inverse-run-count/proof-RUNS.md Sec. 12 (remove rho_1 rho_{-1} from a run with r >= 3, add
sigma sigma to a reflection run; all half windows shrink; kappa, B drop by 1, g, k, d_t, theta
fixed); if B reaches 0, Proposition S1' / Lemma A1' (../proof-PAR-Kplus-partial.md Sec. 3')
finish.  So every run may be assumed pure aligned (d >= 1), pure anti (d = -c <= -1) or a
(1,1)-pair (d = 0).
Lifts: interval-chain lifts x_t (prefix gap representatives, Lemma TL of proof-RUNS.md Sec. 4),
bh_t = 2x_t - d_t (= d_t mod 2), sum bh_t = 2p - D = k - 2g.

## 3. Protocol (frozen)

A. Study interval-feasible theta of MIX words (p = 11..23 families from the PAR hunt, random
   o_F <= p data) to find a defect rule that kills directly (x(P) in I(P) as integers).
B. Prove it in the S1' template (Steps 0-4) with the mixed window G_m; record exactly which
   steps fail for anti runs/pairs and replace them.
C. Controls: replay every inequality on data; exact interval-DFS + all-pattern checks; any
   avoider found must be re-verified by the raw DP (../../code/was_verify.py dp_has) before
   any report.  Caps: 1 CPU, <= 4 GiB, chunks <= 30 min, host-clock labels.
