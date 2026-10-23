# Theorem KBH: kappa = B with at least p+1 odd reflection runs (task OlsonRunCount, option (A))

Status: written proof [W], NOT yet independently reviewed.  Written after host clock
2026-10-17T06:41 PDT.  Representation: ../README.md Sec. 2 (Lemma HW = half-window form of the
reviewed Lemma WAS), frozen for this cycle in README.md Sec. 2 of this directory.  Finite checks
(Sec. 5) are aids only and are not used in the proof.

## 1. Statement

**Theorem KBH.**  Let p >= 5 be prime and let w be an RGR word of length 4p-2 with F, R >= 1,
normalised so that A >= B (automorphism rho_v -> rho_{-v}, sigma_v -> sigma_{-v}), with
B = kappa := p - 1 - H and with at least p+1 reflection runs of odd length.  Then w has an
identity 2p-subword.  No inherited hypothesis ((E), (P), (V), (Pairs), (D0)) is used, and the
rotation runs may contain both letters.

(For B = 0 the hypotheses are contradictory: see Step 0.  kappa = B = 1 was already covered by
OlsonParity's Theorem K1'.)

**Corollary (bookkeeping for RUNS(p)).**  Let w be an inherited RGR word of length 4p-2 with
k >= p+1 rotation runs, normalised A >= B; an avoider has B <= kappa (zero condition).
* B = 0: ../proof-RUNS.md Sec. 11 (Corollary B0 for kappa >= 1; OlsonParity's K0 for kappa = 0).
* kappa = B >= 1 and o_F <= p: OlsonParity's Theorem KB
  (../../inverse-parity/proof-PAR-Kplus-partial.md Sec. 6; its capped case uses (D0)).
* kappa = B >= 1 and o_F >= p+1: Theorem KBH.
* kappa > B >= 1: MIX_DEF, open (OlsonParity's current cycle).
So RUNS(p) follows from MIX_DEF(p) together with the cited [W] results; RUNS(p) itself is NOT
claimed here.

## 2. Setting and the interval windows

Runs and notation as in ../proof-RUNS.md Sec. 0: rotation runs R_1, ..., R_k, reflection run S_j
between R_j and R_{j+1}, a_t, b_t, d_t = a_t - b_t, H = sum floor(l_j/2), o = o_F the number of odd
l_j, phi_t = (y_{t-1} - y_t)/2.  Lemma HW: w avoids iff phi(P) := sum_{t in P} phi_t is not in
I(P) = [-g_P(E-), g_P(E+)] (mod p) for every proper pattern P, where g_P(E) = min(p - m,
E + m + h(P) - p, floor(E/2)), m = m(P) the number of cyclic blocks of P, h(P) = H - beta(P),
beta(P) the number of even boundary reflection runs, E+ = sum_P a + sum_{P^c} b, E- = R - E+.
We only use: if phi(P) is in I(P) (mod p) for ONE proper P, then w has an identity 2p-subword.

**Segments.**  Let O = {j : l_j odd}, |O| = o >= p+1.  The segments G_1, ..., G_o are the maximal
sets of rotation runs strictly between cyclically consecutive odd reflection runs (each is a
nonempty cyclic interval of runs; they partition [k] in cyclic order).  For a segment G put
d_G = A_G - B_G.  A union Q of c consecutive segments, 1 <= c <= o-1, is a proper cyclic interval
of runs whose two boundary reflection runs are odd, so m(Q) = 1, beta(Q) = 0, h(Q) = H, and
E+(Q) = A_Q + B - B_Q = D_Q + B with D_Q := sum_{G in Q} d_G.  With H = p - 1 - kappa = p - 1 - B:
   U_Q := g_Q(E+) = min(p - 1, D_Q, floor((D_Q + B)/2)),
   L_Q := g_Q(E-) = min(p - 1, D - D_Q, floor((D - D_Q + B)/2)),       D := A - B,
since E+ + 1 + H - p = D_Q and E- = R - D_Q - B = (D - D_Q) + B.  (This is the observation behind
OlsonParity's Lemma OR; no merged word is needed below.)

## 3. Lemma ZS (zero-sum interval certificate)

**Lemma ZS.**  Let w be any RGR word, G_1, ..., G_o its segments with o >= p+1, and fix p
cyclically consecutive segments W = (G_{s+1}, ..., G_{s+p}).  For 0 <= i < j <= p let
Q_{ij} = G_{s+i+1} u ... u G_{s+j}.  If integers tau_1, ..., tau_p satisfy
   tau_{i+1} + ... + tau_j  in  [-L_{Q_ij}, U_{Q_ij}]      for all 0 <= i < j <= p
(with U, L the windows of Q_ij in w), then w has an identity 2p-subword.
Proof.  Put S_0 = 0 and S_j = sum_{i=1}^{j} (phi(G_{s+i}) - tau_i) mod p, j = 0..p.  These are
p+1 residues mod p, so S_i = S_j for some i < j.  Then phi(Q_ij) = tau_{i+1} + ... + tau_j
(mod p) lies in I(Q_ij), and Q_ij is a proper pattern (it misses at least o - p >= 1 segments,
hence at least one run).  Lemma HW.  []

## 4. Proof of Theorem KBH

**Step 0 (parameters).**  If A >= 2p, the subword rho_1^{2p} is an identity 2p-subword; so
assume A <= 2p - 1.  F = o + 2H and R = 4p - 2 - F = 2p - o + 2B, hence
   D = A - B = R - 2B = 2p - o,   1 <= D <= p - 1,
since p+1 <= o <= k and 2k <= R + F = 4p - 2 give o <= 2p - 1.  Also B = kappa <= p - 1 (H >= 0).
If B = 0 then R = 2p - o <= p - 1 < p + 1 <= o <= k <= R, impossible; so B >= 1.
Positive and negative parts: P_G := max(0, d_G) <= A_G and N_G := max(0, -d_G) <= B_G, so for any
set Q of segments D_Q = P_Q - N_Q, N_Q <= B, and for pairwise disjoint Q_1, ..., Q_r:
sum_r P_{Q_r} <= A <= 2p - 1.

**Step 1 (the constraints in theta-coordinates).**  Fix ANY window W (s arbitrary) and write
tau_i = d_{G_{s+i}} - theta_i, theta(Q_ij) := theta_{i+1} + ... + theta_j.  By Sec. 2,
tau(Q) in [-L_Q, U_Q] is equivalent to
   lo(Q) <= theta(Q) <= hi(Q),
   lo(Q) := D_Q - U_Q = max(0, ceil((D_Q - B)/2), D_Q - p + 1),
   hi(Q) := D_Q + L_Q = min(D, floor((D + D_Q + B)/2), D_Q + p - 1).
The function x -> lo(x) := max(0, ceil((x - B)/2), x - p + 1) is nondecreasing, satisfies
lo(x + c) - lo(x) <= c for c >= 0 (each of the three terms does), lo(x) = 0 for x <= B
(as B <= p - 1), and lo(x) <= x for x >= 0.

**Step 2 (greedy theta).**  For j = 1, ..., p define
   theta_j := max(0, max_{0 <= i < j} [ lo(Q_ij) - theta(Q_{i,j-1}) ]),   theta(Q_{j-1,j-1}) := 0.
By induction on j, theta(Q_ij) >= lo(Q_ij) for all 0 <= i < j <= p.
(2a) 0 <= theta_j <= P_{G_{s+j}}.  For i = j-1 the bracket is lo(d) with d = d_{G_{s+j}}, which is
0 if d <= 0 and <= d if d > 0.  For i < j-1, by induction theta(Q_{i,j-1}) >= lo(Q_{i,j-1}), so
the bracket is <= lo(D_{Q_{i,j-1}} + d) - lo(D_{Q_{i,j-1}}) <= max(0, d).
(2b) theta(W) := theta_1 + ... + theta_p <= D.  Let J = {j : theta_j > 0}; if J is empty we are
done.  Otherwise let j_1 = max J and i_1 a maximiser in the definition of theta_{j_1}; then
theta(Q_{i_1 j_1}) = lo(Q_{i_1 j_1}) ("tight").  Recursively let j_{r+1} = max(J n [1, i_r]) and
i_{r+1} a maximiser for it, as long as J n [1, i_r] is nonempty.  The intervals
Q_r := Q_{i_r j_r} are pairwise disjoint, every element of J lies in one of them, so
theta(W) = sum_r theta(Q_r) = sum_r lo(Q_r), and lo(Q_r) >= theta_{j_r} > 0 forces
D_{Q_r} >= B + 1 (lo(x) > 0 needs x > B or x >= p > B).
 * One interval: D_Q <= P_Q <= A = D + B, so ceil((D_Q - B)/2) <= ceil(D/2) <= D and
   D_Q - p + 1 <= D + B - p + 1 <= D; hence lo(Q_1) <= D.
 * r >= 2 intervals: sum_r D_{Q_r} <= sum_r P_{Q_r} <= A <= 2p - 1 and every D_{Q_r} >= B + 1, so
   every D_{Q_r} <= 2p - 2 - B, and then D_{Q_r} - p + 1 <= (D_{Q_r} - B)/2; thus
   lo(Q_r) = ceil((D_{Q_r} - B)/2) <= (D_{Q_r} - B + 1)/2 and
   sum_r lo(Q_r) <= (A - r(B - 1))/2 <= (A - 2(B - 1))/2 = (D - B + 2)/2 <= D
   (B >= 1 and D + B >= 2).
(2c) Upper bounds.  For every subinterval Q of W: theta(Q) <= min(D, P_Q) by (2a), (2b) and
theta >= 0.  Hence theta(Q) <= D; 2 theta(Q) <= D + P_Q <= D + P_Q + (B - N_Q) = D + D_Q + B; and
theta(Q) <= P_Q <= P_Q - N_Q + p - 1 = D_Q + p - 1 (N_Q <= B <= p - 1).  So theta(Q) <= hi(Q).

**Step 3.**  By Steps 1-2, tau_i := d_{G_{s+i}} - theta_i satisfies the hypothesis of Lemma ZS
for the window W, so w has an identity 2p-subword.  []

Remarks.  (1) Every window W works, and the certificate is value-independent.  (2) The proof uses
o >= p+1 only in Lemma ZS (p+1 prefix sums, proper Q); for o <= p the window would be the whole
cycle, and the non-inherited type (II) avoiders of ../../repr-WAS.md 4.3 show that some other
argument (OlsonParity's Theorem KB with (D0)) is needed there.  (3) kappa > B: the same interval
windows then carry the offset kappa - B: lo({G}) >= kappa - B for every segment and
hi(W) <= D - (kappa - B), so an additive tau needs p(kappa - B) <= D - (kappa - B), i.e.
(p - 1)(kappa - B) <= 2p - o; this fails for kappa - B >= 2 and for kappa - B = 1 unless
o = p+1.  So Lemma ZS with intervals does not reach MIX_DEF.

## 5. Finite checks (aids only; files in this directory, outputs in out/)

* kbh.cpp census (Lemma BC families) and zs.cpp (exact ZS feasibility by Bellman-Ford with the
  exact windows, every start): all KB_HIGH* data (all-odd, pure/(1,1) runs, B = kappa, k >= p+1)
  at p = 5 (7,923 rotation classes x splits) and p = 7 (3,097,666): ZS feasible; zs_allwin.cpp:
  feasible for EVERY window in all of them; 20,000 random p = 11 data (k = 12..20): ZS feasible
  (out/zs_p5_exh.txt, out/zs_p7_exh.txt, out/zs_allwin_p5_p7.txt, out/zs_p11_rnd.txt).
* zs_replay.py follows the proof on random words with ARBITRARY rotation runs and arbitrary
  reflection parities (A >= B = kappa, o_F >= p+1, A <= 2p-1): greedy theta for every window
  checked against the exact general half-window formula (with beta); end-to-end, random y,
  pigeonhole collision mapped back to w and the raw ordered-product DP (../hw.py dp_has) finds an
  identity 2p-subword: p = 5, 7 (300 words each), 11 (200), 13 (120), 17, 19, 23, 29 (80 each):
  all windows ok and all end-to-end checks ok.  Control: the same greedy on all-odd words with
  kappa = B + 1 fails for some window in every control sample (75, 75, 50, 30, 20 x 4), so the
  checker is not vacuous (out/zs_replay_*.txt).
* Lemma BC single-run chains (kbh.cpp) cover p = 5, 7 and the 400 random p = 11 data but provably
  not k >= (3p+5)/2 (step 2 is <= 2D + 4); the extreme family p = 11, k = 19, R = 19 has no
  single-run chain and no full window, yet is killed (out/extreme_p11_k19.txt) -- by ZS0.
