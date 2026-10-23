# Cycle 2: full windows for every NMH word with R >= 2p-2 (items (i), (ii) of ../proof-MH.md Sec. 6)

Status: [W] = written proof, NOT yet independently reviewed; [F] = exact finite check (aid only).  Statements
and proofs below were written into c2/README.md (Secs. 2, 5, 7) before the exhaustive checks; times and hashes
are in c2/out/freeze.txt.  Representation: c2/README.md Sec. 1 (= ../proof-MH.md (1.1)), Lemma HW.

Notation.  All-odd RGR word of length 4p-2 (p >= 5 prime), k runs, R = A + B = 2p - k + 2kappa,
kappa = p - 1 - H; for a pattern P with m blocks, x := E+(P) = D_P + B, E-(P) = R - x, and
I(P) = [-g_m(R - x), g_m(x)], g_m(E) = min(p - m, E + m - 1 - kappa, floor(E/2)).  "Full window":
g_m(x) + g_m(R - x) >= p - 1; it gives an identity 2p-subword.  A move shifts one cut to an adjacent free
reflection run; it toggles one rotation run u and changes x by +-d_u with |d_u| <= r_u.  ex(t) := r_t - 1.
The rotation of Theorem ALT (../../proof-RUNS.md Sec. 2) is a path P_0 -> P_0^c of m-block patterns when
k >= 2m + 1; it toggles every run exactly once.  x(P^c) = R - x(P).

## 1. Lemma R2 (R = 2p - 2) [W]

**Lemma R2.**  Every all-odd RGR word of length 4p-2 with k >= p+1 runs and R = 2p-2 (any letters, any B)
has a full window.

Proof.  k = 2kappa + 2, kappa >= 2; W := R - 2kappa + 1 = 2p - k + 1 = |Z|, Z := [kappa, R - kappa];
E := sum ex(t) = R - k = W - 3, so r_t <= W - 2 for all t and there are >= k - E = 2k - 2p + 2 >= 4 singleton
runs.  W = 1 (mod 4) if kappa is even and W = 3 (mod 4) if kappa is odd.  m0 := floor(kappa/2) + 1,
M := kappa (kappa even) or kappa + 1 (kappa odd).
Claim 1''.  An m0-block pattern with EVEN x in [M, R - M] has a full window: for E in {x, R - x} (even),
E/2 >= kappa + 1 - m0 makes the middle term of g_{m0}(E) at least E/2, and E/2 <= (R - M)/2 <= p - m0; so
g(x) + g(R - x) = R/2 = p - 1.
Claim 2.  Let s be a singleton run, s- and s+ its neighbouring runs, and let P_0 be any m0-block pattern with
cuts at the reflection runs S_{s-1} (before s) and S_{s+1} (after s+), none at S_{s-2} and none at S_s
(possible: k - 2m0 = kappa or kappa + 1 >= 2).  Let c be the cut at S_{s-1} and i* the cut before c; run the
rotation with this i* (i* first moves to S_{s-2}, then the cuts i*-1, ..., c+ each to the original position of
their successor, then c to S_{s+1}, then i* to S_{s-1}).  Up to the index tau before c moves, c sits at
S_{s-1} and S_s is free, so from every P_j (j <= tau) the move c -> S_s is legal: it toggles s, keeps m0
blocks and changes x by +-1.  After tau exactly s, s+ and rho := s- are toggled, so
|x(P_N) - x(P_tau)| <= 1 + r_{s+} + r_rho = 3 + ex(s+) + ex(rho) <= 3 + E = W.
kappa even.  Take any singleton s.  If x(P_0) < kappa then x(P_tau) >= R - x(P_0) - W >= kappa, so there is a
first j <= tau with x(P_j) >= kappa, and x(P_j) <= kappa - 1 + (W - 2) = R - kappa - 2.  Symmetrically if
x(P_0) > R - kappa; j = 0 if x(P_0) is in Z.  Even x(P_j): Claim 1'' (M = kappa).  Odd: x(P_j) is in
[kappa + 1, R - kappa - 1], and toggling s gives an even value in Z with m0 blocks: Claim 1''.
kappa odd, W = 3.  E = 0, all steps are +-1, the target is the single even value kappa + 1, and the path from
x(P_0) to R - x(P_0) meets it.
kappa odd, W >= 7.  Claim 3 below gives a singleton s with ex(s-) + ex(s+) <= E - 2, hence
|x(P_N) - x(P_tau)| <= W - 2.  Work with Z' := [kappa + 1, R - kappa - 1] (W - 2 integers, even ends; a step
<= W - 2 cannot jump over it).  If x(P_0) <= kappa then x(P_tau) >= R - kappa - (W - 2) = kappa + 1, and the
first j with x(P_j) >= kappa + 1 has j <= tau and x(P_j) <= R - kappa - 1; symmetrically above; j = 0 if
x(P_0) is in Z'.  Even: Claim 1'' (M = kappa + 1).  Odd: x(P_j) is in [kappa + 2, R - kappa - 2] and toggling
s lands on an even value of Z'.
Claim 3.  (kappa odd, W >= 7, >= 4 singletons.)  If every singleton had neighbours carrying >= E - 1 excess:
a singleton with a singleton neighbour forces its other neighbour u to have ex(u) >= E - 1, and a singleton
not adjacent to u (>= 4 singletons) has neighbours carrying <= 1 <= E - 2; otherwise all singletons sit alone
in the q slots between consecutive non-singleton runs, and for any singleton the other q - 2 non-singletons
carry <= 1, so q <= 3 and there are <= 3 singletons.  Both are contradictions.  []

[F] r2_check.cpp, out/r2_check_p5_p7.txt: ALL all-odd pure/(1,1) words with R = 2p-2, k >= p+1, any B:
p = 5: 9,376 words, Claim 1'' on 142,100 patterns, 151,296 executions of the construction (every admissible s,
4 random completions each), W = 3 case 256 words; p = 7: 3,909,536 words, 317,156,952 patterns, 57,824,640
constructions, W = 3 case 4,096 words; 0 failures of any checked step (legality, bound on the last three
steps, entry index j <= tau, legality of the s-toggle, full window at the end, Claim 3).

## 2. Lemma BR (R >= 2p + 1 with an oversized run) [W]

**Lemma BR.**  Let w be an all-odd RGR word of length 4p-2 with k >= p+1 runs, every run pure or a
(1,1)-pair, R >= 2p+1, A, B <= 2p-1 and min(A, B) <= kappa, having a run u with |d_u| >= W + 1, W := 2p-k+1.
Then w has a full window.

Proof.  Step 0.  The flip rho_1 <-> rho_{-1} sends x to R - x for every pattern and preserves R, kappa, k,
the blocks, the hypotheses and full windows; so assume d_u >= W + 1 (u is pure aligned).  j := R - 2p >= 1.
The total excess is R - k = W + j - 1 and ex(u) >= W, so every other run has r_v <= j, and j <= W - 3 as
kappa = (k + j)/2 <= p - 1; hence also j <= k - 4.  A <= 2p - 1 gives B >= j + 1.  Let Omega be the path of
the other k - 1 runs; eps := excess of its aligned and anti runs; N_alpha := aligned letters in Omega.  For
Q subset Omega: x(Q) = sum_{aligned in Q} a + sum_{anti not in Q} b + n_pi (pairs count 1 either way, b_u = 0),
so a set Q containing all aligned runs of Omega and no anti run has x(Q) = R - a_u - n_pi = k - 1 + eps.
Step 1 (windows).  For R >= 2p and k - p + 1 <= 2m <= p + 1 let M_m := max(kappa, 2m - 2, k + 1 - 2m).  Every
m-block pattern with x in T_m := [M_m, R - M_m] has a full window (the nine sums of one term of g_m(x) and one
of g_m(R - x) are >= p - 1: (p-m)+(p-m) by 2m <= p + 1; (p-m)+(y+m-1-kappa) by y >= kappa;
(p-m)+floor(y/2) by y >= 2m - 2; (x+m-1-kappa)+(y+m-1-kappa) = 2p - k + 2m - 2 by 2m >= k - p + 1;
(x+m-1-kappa)+floor(y/2) >= (x + 2m - 3 - 2kappa + R)/2 by x >= k + 1 - 2m; floor(x/2)+floor(y/2) >= (R-2)/2;
symmetric ones likewise).  |T_m| >= j + 1 (M_m = kappa: W >= j + 3; M_m = 2m - 2: R - 4m + 5 >= j + 3;
M_m = k + 1 - 2m: >= 2p + j - 2k - 1 + 2(k - p + 1) = j + 1), so a step <= j never jumps over T_m.
Step 2 (jump lemma).  If k >= 2m + 1 and some m-block P_0 with u in P_0 has x(P_0) <= R - M_m, some pattern is
full.  If x(P_0) >= M_m, P_0.  Otherwise follow the rotation P_0 -> P_0^c: before u is toggled all steps are
<= j, so T_m is met or the value stays < M_m; the u-step removes u and lowers x by d_u; afterwards the steps
are <= j again and the path ends at R - x(P_0) > R - M_m, so it meets T_m.
Step 3 (P_0 := Q^c for Q subset Omega with m blocks and x(Q) >= M_m).  Q0 := for each maximal anti-free interval
of Omega containing an aligned run, the sub-interval from its first to its last aligned run; c := their number
(c >= 0).  Q0 contains all aligned and no anti runs, so x(Q0) = k - 1 + eps, and for c >= 1 it has c blocks on
the cycle (u separates the end stretches).  c_lo := ceil((k - p + 1)/2) >= 1.
 (2) c_lo <= c <= (p+1)/2, k >= 2c + 1: m := c, Q := Q0; x(Q0) >= k - 1 >= M_c (kappa <= k - 2,
     2c - 2 <= p - 1, k + 1 - 2c <= k - 1).
 (2') c_lo <= c <= (p+1)/2, k = 2c: then k = p + 1 and all blocks and gaps of Q0 are single runs; m := c - 1,
     Q := Q0 minus one stretch {v}: x(Q) >= k - 1 + eps - a_v >= k - 2 = p - 1 >= M_{c-1} = max(kappa, p-3, 3);
     2m = p - 1 >= k - p + 1, k >= 2m + 1.
 (3) c > (p+1)/2: m := m_max := min(floor(kappa/2) + 1, floor((k-1)/2)) (then m_lo <= m_max and M_m = kappa,
     ../proof-MH.md Theorem FWH Claim 1); Q := the m_max stretches of largest aligned mass; x(Q) = B + (their
     mass).  With tau := kappa - B <= (k - j)/2 - 1 (B >= j + 1) we have N_alpha - tau = k - 1 + eps - kappa
     >= tau, so N_alpha >= 2 tau; the c stretches are separated by >= c - 1 anti runs, so B >= c - 1.  If
     c <= 2 m_max the chosen mass is >= N_alpha/2 >= tau; if c > 2 m_max then m_max = floor(kappa/2) + 1
     (c <= k/2 <= 2 floor((k-1)/2)) and B >= 2 m_max > kappa, so tau < 0.  Either way x(Q) >= kappa.
 (1) c < c_lo: m := c_lo; starting from Q0 (empty if c = 0), flip one at a time a run v != u whose two
     neighbours share its status (u counts as outside).  Each flip adds one block; such v exists while there
     are b < c_lo blocks (otherwise all blocks and the gaps without u have <= 2 runs and the gap with u has
     <= 3, so k <= 4b + 1 <= 4c_lo - 3 <= 2k - 2p + 1 < k); a flipped run and its neighbours never qualify
     again, so no run is flipped twice and each flip lowers x by a_v, b_v (<= 1 + ex(v)) or 0.  Hence
     x(Q) >= k - 1 - c_lo + c, which is >= k + 1 - 2c_lo (as c + c_lo >= 2: if c = 0, Omega has no aligned run,
     B = k - 1 + eps > kappa, so min(A,B) <= kappa forces A = a_u + n_pi <= kappa, whence 3k + j >= 4p + 4,
     k >= p + 3 and c_lo >= 2), >= kappa (c_lo <= (k - p + 2)/2 <= k - p + c <= k - 1 - kappa + c), and
     >= 2c_lo - 2 (3(k - p + 2)/2 <= k + 1).  Also 2c_lo >= k - p + 1, c_lo <= (p+1)/2, k >= 2c_lo + 1.
In every case Step 2 applies.  []

[F] bigrun_construct2.cpp, out/bigrun_construct2.txt: the construction executed literally (random choice of
the flipped runs in case (1), random dropped stretch in (2')), followed by the rotation and an exact
full-window test: ALL big-run words in the lemma's range at p = 5 (380) and p = 7 (83,828; all four cases
occur, incl. 208 of case (2')), and 20,000 random ones at each of p = 11, 13, 17, 19, 23: 0 failures.  Also
checked: at most one oversized run, other runs <= j, N_alpha >= 2 tau.  The earlier single-flip rule
(bigrun_construct.cpp) failed 18 times at p = 7 (no single flip available with m = m_lo); m_lo itself is
not always enough (c2/README.md Sec. 6: p = 13 example), which is why m varies above.

## 3. Consequence

**Theorem FW+.**  Every all-odd RGR word of length 4p-2 with k >= p+1 runs, every run pure or a (1,1)-pair,
R >= 2p-2, A, B <= 2p-1 and min(A, B) <= kappa has a full window.  In particular every NMH word
(../README.md Sec. 1) with R >= 2p-2 has an identity 2p-subword.
Proof.  R = 2p-2: Lemma R2.  R in {2p-1, 2p}: ../proof-MH.md Theorem FWH (a), (b) (k >= p+1 >= 6).
R >= 2p+1: Theorem FWH (c) if no run has |d_u| >= 2p - k + 2, Lemma BR otherwise.  []
So NMH(p), hence MIX_DEF_HIGH(p), is reduced to the words with R <= 2p-3 (item (iii)); the ZSI-B part of
../proof-MH.md Sec. 4 covers k = p+1, kappa - B = 1 under (4.1).  RUNS(p) is not claimed.
