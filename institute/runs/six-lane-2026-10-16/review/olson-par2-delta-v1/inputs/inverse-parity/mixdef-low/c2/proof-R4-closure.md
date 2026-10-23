# Closure of the MIX_low residual: Lemma R4, and MIX_low(p), PAR(p) for every prime p >= 5

Owner OlsonParity2.  Written after host clock 2026-10-17T17:52:55-07:00.  Status: written proof [W],
NOT reviewed (Sec. 1 is new; it closes the residual R4 of c2/proof-Rstar-r3.md).  Finite replays [F] in Sec. 4.
Claims are exactly Theorems M and P below; nothing about RUNS(p), INV, INV* or ordered Olson for D_{2p}
(ordered Olson would additionally need RUNS(p) and INV*(p)).

Imports (exact): c2/proof-MIX-low-partial-r2.md (adf8cb70...6a22: setting, Lemma S, Lemma K + Corollary,
MIX-R, R*); c2/proof-Rstar-r3.md (acdde81f...4e2b: Fact F, Lemma KL, W, B1, A, G1, KS, AC [v2 parts reviewed:
Codex ACCEPT, Claude ACCEPT-WITH-FIXES, fixes in r3]; ZP, C, R4 [r3, unreviewed]); c2/proof-PAR-assembly-r1.md
(b1b320bf...c601: the PAR chain (a), (b)).  Notation as in proof-Rstar-r3.md Sec. 0, 4, 6 (X := phi(Z0+),
delta+ := -BH(Z0+), alpha = #free anti runs, s = k - 1 - 2g - B, TOT = p - k + 2g = sum phi).

## 1. Lemma R4

**Lemma R4.**  No lift data of a normalized MIX_low avoider lie in R4 (proof-Rstar-r3.md Sec. 6).
Proof.  Let the data lie in R4.  Facts (all from r3 Sec. 6): (i) every d_t <= 2g + B - 2, so every
phi_t <= g - 1 (Fact F(c)); (ii) every bh_t <= s; (iii) Z0+ is nonempty and X + m(Z0+) <= g, so
X <= g - 1, and with the R*** inequality 2X + alpha >= 2g + s + S_Z this gives alpha >= 2m(Z0+) + s + S_Z
>= s + 2, hence B >= alpha >= s + 2 (alpha <= anti mass <= B); (iv) delta+ = 2X - S_Z - n_d + (anti mass of
the free antis) >= 2g + s - n_d, and n_d <= X <= g - 1 (each aligned run of Z0 has phi >= 1), so
delta+ >= g + s + 1.
Step 1 (a set N of Y-runs).  Y = {bh >= 1} is not the whole cycle (Z0 is nonempty), so its maximal cyclic
intervals are paths.  BH(Y) = (k - 2g) - BH(Z0) = s + 1 + B + delta >= s + 1 + B + delta+ >= 2s + 3
(delta := -BH(Z0) >= delta+, as the other runs of Z0 have bh <= 0).  In every path take the parity class
of larger BH; the union Q is independent in the cycle and BH(Q) >= BH(Y)/2 > s + 1.  Add runs of Q to N
one at a time until BH(N) >= s + 1; as 1 <= bh <= s on Y, s + 1 <= BH(N) <= 2s, |N| >= 2, N independent.
Step 2 (dichotomy).
(a) If phi(N) <= (p - k + g - 1) + |N|: S' := [k] \ N is proper, nonempty, m(S') = |N| (N independent),
    c(S') = TOT - phi(N) + |N| >= g + 1, BH(S') = (k - 2g) - BH(N) <= (k - 2g) - (s + 1) = B, and phi <= g - 1
    on S' by (i).  Lemma KL.
(b) Otherwise phi(N) >= p - k + g + |N| >= g + 2.  S := Z0+ union N (disjoint): c(S) >= phi(S) + 1 =
    X + phi(N) + 1 >= g + 3; BH(S) = -delta+ + BH(N) <= -(g + s + 1) + 2s < 0 <= B, so S != [k]
    (BH([k]) = k - 2g > 0); phi <= g - 1 on S by (i).  Lemma KL.
In both cases v has an identity 2p-subword, contradicting avoidance.  []

## 2. Theorem M (MIX_low(p) for every prime p >= 5)

**Theorem M.**  MIX_low(p) holds for every prime p >= 5.
Proof.  By proof-PAR-assembly-r1.md Sec. 2(b)-(c) and proof-Rstar-r3.md Sec. 6 (Corollary'), every
normalized MIX_low avoider has lift data in R4 (the cases outside R4 are killed by MIX-R, W, B1, A, AC, KS,
ZP, C); Lemma R4 excludes R4.  The non-normalized words reduce to the normalized ones by Lemma M0, the case
B = 0 after M0 by Proposition S1' / Lemma A1', and A >= 2p is trivial (assembly r1 Sec. 2(b)).  []

## 3. Theorem P (PAR(p) for every prime p >= 5)

**Theorem P.**  For every prime p >= 5, every inherited avoider w' in RGR_{4p-2}(p) with k <= p has all 2k
runs odd (PAR(p), ../../../proof-INV-reduction.md Sec. 2).
Proof.  proof-PAR-assembly-r1.md Theorem PA, part (a): PAR(p) <= K0, K1, K1', S1'/A1', KB and MIX_low(p)
(via Lemma OR); MIX_low(p) is Theorem M.  []
Dependencies and their review status: proof-PAR-assembly-r1.md Sec. 4, plus this file and the r3 additions
(ZP, C, R4), which are unreviewed; Lemma M0 is [W] rechecked but not independently reviewed.
Consequence for the lane (proof-INV-reduction.md Sec. 2): INV_Res(p) = PAR(p) + RUNS(p); with Theorem P only
RUNS(p) (and INV*(p) for ordered Olson, proof-DR.md Corollary DR') remain open in the inverse reduction.

## 4. Replays [F] (research aids; never hypotheses)

c2/r4_replay.py (sha256 4e1b6d0b...6c6a), output c2/out/r4_replay_p11.json (seed 20261017, host
17:52:51-17:52:54 PDT):
* p = 11 census (all 211,911 interval-feasible configurations): Lemma ZP applicable to 211,284, every
  produced KL prefix satisfies integer window containment x(P) in [-L_P, U_P]; Lemma C never applicable.
  (R4 itself is empty in every census computed, so Lemma R4 has no census instance.)
* Synthetic integer data on normalized MIX_low run data satisfying exactly the hypotheses used (Lemma C:
  phi <= g - 1 off t0, bh_t0 >= s + 1, phi_t0 <= p - k + g; Lemma R4: all phi <= g - 1, all bh <= s,
  delta+ >= 2s - B, heavier Y-class BH >= s + 1), p = 11..37, NOT interval-feasible (the conclusions are pure
  arithmetic): C 3,200 / 3,200 and R4 2,815 / 2,815 produced prefixes inside their windows; mutation (every
  window shrunk by one at both ends) rejects 1,202 (C) and 1,046 (R4) of them.
* Earlier eval-session checks (same constructions, seeds 4242, 99, 777): 15,285 + 9,000 applicable synthetic
  cases, 0 failures; mutation rejections 4,254 and 3,535.
