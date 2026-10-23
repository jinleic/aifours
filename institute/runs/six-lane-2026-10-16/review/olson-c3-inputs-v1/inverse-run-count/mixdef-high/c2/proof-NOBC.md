# Lemma NOBC: inherited NMH words with no Lemma BC certificate (p >= 11), and Lemma AV

Status: [W] = written proof, NOT yet independently reviewed; [F] = exact finite computation (aid only).
Written 2026-10-17 after host clock 10:04 PDT (times and hashes: c2/out/freeze.txt).  Scope: this file
shows that Lemma BC certificates (every ordered partition, every s >= 2, hence also full windows and the
flat 3-partition certificate) cannot settle item (iii) of ../proof-MH.md Sec. 6.  It does NOT bear on
the truth of RUNS(p) or NMH(p): the words below are NOT avoiders at p = 11, 13 by exact search (Sec. 3).

Notation (../../../inverse-parity/proof-PAR-K0.md Sec. 1, Lemma H; Sec. 2, Lemma BC).  For an all-odd RGR
word (every reflection run odd, so beta(Q) = 0 for every pattern) and a proper pattern Q with m(Q) blocks,
   lambda(Q) = min(p - m(Q) + 1,  D_Q + B - kappa + m(Q),  floor((D_Q + B)/2) + 1).
Lemma BC: an ordered partition (P_1, ..., P_s), s >= 2, of the rotation runs into nonempty proper patterns
satisfying (a) sum_t lambda(P_t) >= p + 1, (b) the step conditions, (c) lambda(P_s) + lambda(P_s^c) >= 1,
excludes avoidance.

## 1. The family

For a prime p >= 11 and an integer kB with 4 <= kB < (p + 6)/4 let W(p, kB) be the set of RGR words of
length 4p - 2 with k = p + 1 + kB rotation runs, each consisting of ONE letter, exactly one of them
rho_{-1} and the others rho_1, and odd reflection runs l_1, ..., l_k with sum_j floor(l_j/2) = p - 2 - kB.
(Example kB = 4: k = p + 5; the smallest case is p = 11, k = 16.)  Parameters: R = k, A = k - 1 = p + kB,
B = 1, D = A - B = p + kB - 1, F = 4p - 2 - k = 3p - 3 - kB, H = p - 2 - kB, kappa = p - 1 - H = kB + 1,
kappa - B = kB.  Nonempty: H >= 0 as kB <= p - 2; k <= 2p - 2.
Inherited conditions: (E) R = p + 1 + kB <= 3p - 2; (P) F + sum floor(r_t/2) = 3p - 3 - kB <= 3p - 2;
(V) R + H = 2p - 1 <= 3p - 2; (Pairs) H <= p - 1; (D0) a_t, b_t <= 1 <= p - 1.  All hold.
NMH (../README.md Sec. 1): all reflection runs odd; p + 1 <= k <= 2p - 2; every run pure; 1 <= B = 1 <=
kappa - 1 = kB; B <= A = p + kB <= 2p - 1 (kB <= p - 1).  Also R = p + 1 + kB <= 2p - 3 (kB <= p - 4,
implied by kB < (p + 6)/4 and p >= 11), so these words lie in item (iii) and are not in the ZSI-B case
(k >= p + 5).

## 2. Lemma NOBC [W]

**Lemma NOBC.**  No word of W(p, kB) admits a Lemma BC certificate: for every ordered partition
(P_1, ..., P_s), s >= 2, of its rotation runs into nonempty proper patterns, sum_t lambda(P_t) <= p.

Proof.  Here B - kappa = -kB.  Let P be a proper pattern with j aligned runs and e in {0, 1} anti runs; then
D_P = j - e and 1 <= m(P) <= |P| = j + e, so
   lambda(P) <= min(D_P + m(P) - kB, floor((D_P + 1)/2) + 1) <= min(2j - kB, floor((j - e + 1)/2) + 1)
             <= min(2j - 4, floor((j - e + 1)/2) + 1)                                            (2.1)
(kB >= 4).  Part without the anti run (e = 0): lambda(P) <= 4j/5.  Indeed for j <= 3,
2j - 4 <= 4j/5 (6j <= 20); for j = 4, floor(5/2) + 1 = 3 <= 16/5; for j >= 5,
floor((j+1)/2) + 1 <= (j + 3)/2 <= 4j/5 (j >= 5).
Part with the anti run (e = 1): lambda(P) <= (4j - 1)/5.  Indeed for 0 <= j <= 3, 2j - 4 <= (4j - 1)/5
(6j <= 19); for j >= 4, floor(j/2) + 1 <= j/2 + 1 <= (4j - 1)/5 (3j >= 12).
Exactly one part contains the anti run and sum_t j_t = k - 1 = p + kB, so
   sum_t lambda(P_t) <= (4/5)(p + kB) - 1/5 = (4p + 4kB - 1)/5 < p + 1,
the last inequality being 4kB - 6 < p.  As the left side is an integer, it is <= p, so condition (a) of
Lemma BC fails for every ordered partition.  []

Remarks.  (1) The bound uses only (a); in particular full windows (s = 2), the flat 3-partition (s = 3)
and every longer chain are excluded, whatever the order.  (2) Lemma OBS (../proof-MH.md Sec. 2) already
excludes fixed-target pigeonhole certificates (ZS, Davenport) when kappa - B >= 2, and R <= 2p - 3 excludes
full windows; so for W(p, kB) none of the certificate types used so far in this route applies.
(3) Item (iii) therefore needs a certificate outside Lemma BC (Sec. 4 gives one for p = 11).

## 3. Exact computations [F] (aids; never used as hypotheses)

* General Lemma BC DP over all ordered partitions (bcgbig.cpp, from ../bcgcheck.cpp; out/big_p11.txt,
  out/big_p13.txt): random NMH words with R <= 2p - 3, p = 11 (k = 16..19, 57 words) and p = 13 (k = 17..19,
  166 words); after the RR rule, NO certificate exactly for the members of W(11, 4) (1 word) and W(13, 4)
  (3 words) that occurred; all other sampled words have a certificate.
* nobc_bound.py (out/nobc_bound.txt): the type-count maximum of sum_t UB(P_t) over partitions (UB as in
  (2.1) but with the exact maximum over 1 <= m <= |P| and the cap) for all-singleton words (R = k) with B
  anti runs, p = 5, ..., 31: it is <= p (so no Lemma BC certificate) for B = 1, kB = 4 at every
  p in {11, 13, 17, 19, 23, 29, 31}, and for further classes marked * there (e.g. B = 1, 4 <= kB <= 10 at
  p = 17; B = 2, kB = 5 at p = 19, 23, 29, 31); at p = 11, 13 only kB = 4 is marked (B = 1, kB = 5 gives
  the bound p + 1, which does not exclude Lemma BC).
* Exact avoider search over all patterns, two independent implementations:
  the C++ DFS of ../mhc.cpp (inside bcgbig.cpp) on the four words above: no avoider; famdfs.py (Python,
  written from Lemma H; anti run at position 0; the window system does not depend on the l_j or on the
  position of the anti run) (out/famdfs.txt): p = 11, k = 16: no avoider (37,639 checks); p = 13, k = 18:
  no avoider (157,720 checks); control p = 7, k = 11 (kB = 3, a BC3 word): no avoider.
* Mutation controls of famdfs.py (out/famdfs_controls.txt): with every lambda lowered by 1 (both window
  ends pulled in) still no avoider at p = 11 and p = 13; lowered by 2, an "avoider" of the weakened system
  is found at p = 11 (u = (0,0,0,0,0,1,...,1)), so the search does return solutions when they exist.

## 4. Lemma AV (symmetric averaging) [W], and its use at p = 11

**Lemma AV.**  Let w be an avoider (all-odd RGR word, so the representation of Lemma H applies with
beta = 0), and O a set of n >= 2 rotation runs, O != [k], pairwise non-adjacent (cyclically), all with
the same d_t = delta.  For a j-subset Q of O, m(Q) = m(Q^c) = j and D_Q = j delta, so Lam_j := lambda(Q) and
Lam'_j := lambda(Q^c) depend only on j; put alpha_j := Lam_j, beta_j := p - Lam'_j.  Suppose that for
2 <= j <= J (some J <= n)
   [alpha_{j-1} + alpha_1, beta_{j-1} + beta_1]  is contained in  [1 - Lam'_j, p + Lam_j - 1].     (L_j)
Then n alpha_a / a <= S <= n beta_b / b for all a, b <= J, for one integer S.  Consequently, if
ceil(n alpha_a / a) > floor(n beta_b / b) for some a, b <= J, w is not an avoider.
Proof.  Claim (from the proof of Lemma BC): if y = u_Q (mod p) is an integer with
1 - lambda(Q^c) <= y <= p + lambda(Q) - 1, then lambda(Q) <= y <= p - lambda(Q^c).  For i in O choose an
integer x_i = u_{{i}} (mod p) in [alpha_1, beta_1] (it exists, as in the proof of Lemma BC).  By induction on
j <= J, every j-subset Q of O has sum_{i in Q} x_i in [alpha_j, beta_j]: for Q = Q' u {i} the sum lies in
[alpha_{j-1} + alpha_1, beta_{j-1} + beta_1], hence by (L_j) in the Claim's range, and it is = u_Q (mod p)
(u is additive), so the Claim applies.  Summing over the C(n, j) subsets of size j, each x_i is counted
C(n-1, j-1) times: C(n, j) alpha_j <= C(n-1, j-1) S <= C(n, j) beta_j with S := sum_{i in O} x_i.  []
Application, W(11, 4) (k = 16, D = 14, kB = 4, B = 1).  O := the 8 aligned runs at odd distance from the
anti run (pairwise non-adjacent).  Lam_j = min(12 - j, 2j - 4, floor((j+1)/2) + 1),
Lam'_j = min(12 - j, 10, floor((15 - j)/2) + 1), so for j = 1..8
   alpha = (-2, 0, 2, 3, 4, 4, 5, 4),   beta = (3, 4, 4, 5, 5, 6, 6, 7).
(L_j) for j = 2..7: [-4,6] in [-6,10]; [-2,7] in [-6,12]; [0,7] in [-5,13]; [1,8] in [-5,14]; [2,8] in
[-4,14]; [2,9] in [-4,15].  a = 5: S >= 8*4/5 = 6.4, so S >= 7; b = 7: S <= 8*6/7 < 7, so S <= 6.
Contradiction: no word of W(11, 4) is an avoider, by a phi-independent certificate that is not of Lemma BC
type.  At p = 13 (W(13, 4), n = 9) the same averaging only gives S in [7.2, 8] (S = 8 is not excluded), so
Lemma AV in this simple form does not cover the family; see c2/README.md for the bounded LP exploration.
