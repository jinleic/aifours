# MIX_DEF_HIGH cycle: proved pieces, exact checks, and the precise open part (task OlsonRunCount)

Status: [W] = written proof, NOT yet independently reviewed; [F] = finite exact check (aid only, never a
hypothesis).  First version written between host clock 2026-10-17T08:23 and 08:44:40 PDT (an earlier
"09:15" label here was a guess and is withdrawn); later additions are dated in place.  Representation and
target: README.md of this directory (frozen 08:20 PDT, hashes in out/freeze.txt).  Nothing outside this
directory is edited.

## 1. Setting

NMH(p) (README Sec. 1): all-odd RGR words of length 4p-2 with p+1 <= k <= 2p-2 runs, every run pure or
a (1,1)-pair, 1 <= B <= kappa - 1, B <= A <= 2p-1.  NMH(p) implies MIX_DEF_HIGH(p) by Lemma OR, Lemma M0,
the trivial cut A >= 2p, Corollary B0 and Theorem ALT (all cited, [W]).  kB := kappa - B >= 1,
D := A - B = 2p - k + 2kB, R := A + B = 2p - k + 2kappa.

For an all-odd word every proper pattern P (m = m(P) blocks) has beta = 0, h = H = p - 1 - kappa and
E+(P) = D_P + B, E-(P) = R - E+(P), so (Lemma HW, ../README.md Sec. 2)
   I(P) = [-g_m(E-), g_m(E+)],   g_m(E) := min(p - m, E + m - 1 - kappa, floor(E/2)).      (1.1)
Equivalently U_P = min(p - m, D_P + m - 1 - kB, floor((D_P + B)/2)), L_P = U(m, D - D_P).  (1.1) holds for
every all-odd word (any letters, any B), not only for NMH.  In NMH the empty and full patterns never
kill (corrected Lemma H: A, B <= 2p-1 and B < kappa + 1).

## 2. Lemma OBS: no fixed-target pigeonhole certificate when kB >= 2 [W]

**Lemma OBS.**  Let w be an all-odd RGR word of length 4p-2 with k runs and kB = kappa - B >= 1 (any B,
any k).  Let G_1, ..., G_n be pairwise disjoint nonempty sets of runs whose union V is a proper
pattern, tau_1, ..., tau_n integers, and suppose that for some partition [n] = J_1 u ... u J_r
   tau(J_j) := sum_{i in J_j} tau_i  lies in  I(G_{J_j})  (G_J := union of G_i, i in J)  for all j,
and tau([n]) lies in I(V).  Then (r - 1) kB + r + 1 <= 2p.
Proof.  By (1.1), U_Q <= D_Q + m(Q) - 1 - kB and L_Q <= D - D_Q + m(Q) - 1 - kB for every proper Q.  So
tau(J_j) <= D_{G_{J_j}} + m(G_{J_j}) - 1 - kB and tau([n]) >= -L_V >= D_V - D - m(V) + 1 + kB.  Summing
the r upper bounds, (r + 1) kB + r + 1 <= D + m(V) + sum_j m(G_{J_j}).  Now sum_j m(G_{J_j}) <= |V|
(every block contains a run) and m(V) = m(V^c) <= |V^c| = k - |V|; with D = 2p - k + 2kB this gives
(r + 1) kB + r + 1 <= 2p + 2kB.  []

**Corollary.**  A "fixed-target pigeonhole certificate" is: groups G_i and targets tau_i as above,
and a family F of nonempty subsets of [n] with the zero-sum property "for all x in Z_p^n some J in F
has sum_{J} x_i = 0 (mod p)", together with tau(J) in I(G_J) for every J in F; it kills every phi
(take x_i = phi(G_i) - tau_i).  For n = p every such F contains all singletons and [n] (test
x = (c, ..., c) and x = (0, c, ..., c), c != 0; n = p).  Hence (Lemma OBS with r = n = p):
 * for kB >= 2 NO such certificate with n = p exists; in particular neither Lemma ZS of
   ../kappaB-high/proof-KBH.md (prefix sums along any chain, F = chain intervals) nor its Davenport
   version (F = all subsets) can kill any word with kappa - B >= 2, for any window or order;
 * for kB = 1 equality must hold throughout: every G_i is a set of pairwise non-adjacent runs,
   V^c consists of k - |V| isolated runs, all reflection-term bounds are attained.
(For n > p the Lemma still applies to every F containing singletons and [n], e.g. chains and all
subsets, and then forbids n >= p+1 for kB >= 1 and n >= p for kB >= 2; families avoiding singletons
would need a partition of [n] into r parts in F, and Lemma OBS bounds r.  The Erdos-Ginzburg-Ziv family
needs n >= 2p-1 disjoint nonempty groups in a proper pattern, impossible as k <= 2p-2.)
So for kappa - B >= 2 and R <= 2p-3 (where no window is full, U + L <= R/2) a proof needs certificates
of another kind, e.g. Lemma BC lift ranges or phi-dependent arguments.  [F] consistent: the census
(Sec. 5) never finds interval ZS for kB >= 2.

## 3. Full windows for R in {2p-1, 2p} (and a conditional extension) [W]

**Theorem FWH.**  Let w be an all-odd RGR word of length 4p-2 with k runs (any rotation letters, any
B) and kappa = p - 1 - H.  Put m* := floor(kappa/2) + 1.
 (a) If R = 2p-1 and k >= 3, then k = 2kappa + 1 and some pattern has a full window.
 (b) If R = 2p and k >= 6, then k = 2kappa and some pattern has a full window.
 (c) If R >= 2p + 1, k >= 6 and every run has |d_u| <= 2p - k + 1, some pattern has a full window.
In each case w has an identity 2p-subword.
Proof.  R = 2p - k + 2kappa gives the stated k.  Write x := E+(P), so E-(P) = R - x and x(P^c) = R - x(P).
Claim 1.  If R >= 2p-1, m(P) = m with m_lo <= m <= m* where m_lo := m* if R = 2p-1 and
m_lo := max(1, ceil((k + 1 - kappa)/2)) if R >= 2p, and kappa <= x <= R - kappa, then I(P) is full.
 For R = 2p-1 and m = m*: for E in {x, R - x}, ceil(E/2) >= ceil(kappa/2) = kappa + 1 - m*, so the middle
 term of g_{m*}(E) is >= floor(E/2); and floor(E/2) <= floor((2p - 1 - kappa)/2) = p - m*.  Hence
 g(x) + g(R - x) = floor(x/2) + floor((R - x)/2) = (R - 1)/2 = p - 1 (R odd).  (This is Lemma A1 of
 ../proof-RUNS.md Sec. 11 verbatim; there B = 0, but only x = E+ enters.)
 For R >= 2p: g(x) + g(y) >= p - 1 (y = R - x) iff all nine sums of one term of g(x) and one of g(y) are
 >= p - 1.  Using kappa <= x, y: (p-m) + (p-m) >= p - 1 as m <= m* <= (p+1)/2 (kappa <= p - 1);
 (p - m) + (y + m - 1 - kappa) >= p - 1 as y >= kappa; (p - m) + floor(y/2) >= p - 1 as
 y >= kappa >= 2m* - 2 >= 2m - 2; (x + m - 1 - kappa) + (y + m - 1 - kappa) = R + 2m - 2 - 2kappa
 = 2p - k + 2m - 2 >= p - 1 as 2m >= k + 1 - kappa >= k - p + 2; (x + m - 1 - kappa) + floor(y/2)
 >= (2x + 2m - 2 - 2kappa + R - x - 1)/2 >= p - 1 iff x >= k + 1 - 2m, true as x >= kappa >= k + 1 - 2m;
 floor(x/2) + floor(y/2) >= (R - 2)/2 >= p - 1; the remaining three are symmetric.
Claim 2 (existence).  Patterns with exactly m blocks correspond to 2m cut positions among the k
reflection runs; if k >= 2m + 1 they form a connected graph under "move one cut to an adjacent free
reflection run", and a path from P_0 to P_0^c exists (rotate every cut to the next cut's position:
the explicit order of Theorem ALT, ../proof-RUNS.md Sec. 2).  One move toggles one run u, so x changes
by +-d_u, |d_u| <= r_u <= R - (k - 1).  Since x(P_0^c) = R - x(P_0), the path cannot avoid the integer
interval [kappa, R - kappa] (R - 2kappa + 1 = 2p - k + 1 integers) if every step is <= 2p - k + 1:
 (a) m = m*: k = 2kappa + 1 >= 2m* + 1 (kappa >= 1); steps <= R - k + 1 = 2p - k.
 (b) m = m*: k = 2kappa >= 2m* + 1 as kappa >= 3; steps <= R - k + 1 = 2p - k + 1.
 (c) m = m_lo: 2 m_lo <= max(2, k + 2 - kappa) <= k - 1 as kappa >= k/2 >= 3; steps by hypothesis.
Hence some P on the path has x in [kappa, R - kappa] and Claim 1 applies.  []
Corollary.  Every NMH word with R in {2p-1, 2p} has an identity 2p-subword (k >= p+1 >= 6).
[F] zsib_check.cpp (out/zsib_check_p5_p7.txt): over ALL all-odd pure/(1,1) words with k >= p+1, any
B >= 1, B <= A and R in {2p-1, 2p} (p = 5: 15,231 words; p = 7: 6,250,553 words), every pattern with
m* blocks and x in [kappa, R - kappa] has a full window (871,600,076 patterns at p = 7, 0 failures), and
the continuity hypotheses (k >= 2m*+1, max r_u <= 2p-k+1) hold in every word.
[F] fwh_c_check.cpp (out/fwh_c_check_p5_p7.txt): Claim 1 for R >= 2p with EVERY m in [m_lo, m*], over all
all-odd pure/(1,1) words with k >= p+1, B >= 1, B <= A, R >= 2p (p = 5: 22,783 words, 649,028 patterns;
p = 7: 12,525,051 words, 2,143,400,456 patterns): 0 failures; m_lo <= m* and k >= 2 m_lo + 1 in all.
Not covered by the proof: R = 2p-2 (a full window needs x = E+ EVEN, and odd steps can skip the even
values of the target) and R >= 2p+1 with a run |d_u| > 2p - k + 1.  [F] fwcheck.cpp (out/fwcheck.txt):
every NMH word with R = 2p-2 has a full window with the canonical m (p = 5, 7 all: 465 + 210,833;
p = 11: 2,180 random), and every NMH word with R >= 2p+1 has a full window (p = 5, 7 all:
2,557 + 1,909,719, including 115 + 27,601 with a big step; p = 11: 6,421 random).

## 4. The boundary case kappa - B = 1, k = o = p+1 [W]

**Lemma ZSI-B.**  Let w be an all-odd RGR word of length 4p-2 with k = p+1 runs and kB = 1 (any
letters, any B >= 0).  Then Lemma ZS of ../kappaB-high/proof-KBH.md (any window W of p consecutive runs,
any integer targets) applies if and only if every proper cyclic interval Q of runs satisfies
   D_Q <= min(2|Q| + B, |Q| + p - 1).                                                (4.1)
In particular (4.1) implies that w has an identity 2p-subword.
Proof.  Here D = 2p - k + 2 = p + 1.  For a window W = [k] - {s} and tau_i = d_i - theta_i, Lemma ZS
requires lo(Q) <= theta(Q) <= hi(Q) for every subinterval Q of W, where by (1.1) with m = 1
lo(Q) = max(D_Q - p + 1, 1, ceil((D_Q - B)/2)) and hi(Q) = min(D_Q + p - 1, p, floor((p+1+D_Q+B)/2)).
Every singleton has lo >= 1 and hi(W) <= p, so theta_t = 1 for all t in W is forced, and then the
conditions read, for c = |Q|: D_Q <= c + p - 1, D_Q <= 2c + B, D_Q >= c - p + 1, D_Q >= 2c - p - 1 - B.
With D_{Q'} = p + 1 - D_Q and |Q'| = p + 1 - c for the complementary interval Q' (which contains s), the
last two are D_{Q'} <= |Q'| + p - 1 and D_{Q'} <= 2|Q'| + B.  As Q runs over the nonempty subintervals
of W, Q and Q' together run over all proper cyclic intervals, independently of s.  []
Remarks.  (1) By the equality case of Lemma OBS, any interval-chain or Davenport certificate in this
case has the same rigid form (singleton groups, theta = 1).  (2) (4.1) is NOT implied by R <= 2p-3:
exact counterexample (zsifail.cpp, out/mhc_p11_rnd.txt): p = 11, k = 12, a = (1,0,1,1,5,1,1,1,1,1,1,0),
b = (0,1,0,...,0,1), l = (1,1,1,1,3,3,5,1,3,1,3,3), A = 14, B = 2, kappa = 3, R = 16: the run d = 5
violates D_Q <= 2|Q| + B = 4; this word is killed by a flat 3-partition Lemma BC certificate (and the
exact search finds no avoider).  So the boundary case is settled by interval ZS exactly under (4.1);
otherwise other certificates are needed.  [F] zsib_check.cpp: ZSI <=> (4.1) on ALL boundary words
(all-odd, pure/(1,1), k = p+1, kB = 1, B >= 1): p = 5: 2,984 words; p = 7: 857,281 words; 0 mismatches.

Added after host clock 2026-10-17T08:52 PDT.
**Lemma V (shape of (4.1)-violators) [W].**  In the boundary case with pure/(1,1) runs and R <= 2p-3
(so B <= (p-5)/2), (4.1) fails iff some proper interval Q has D_Q >= 2|Q| + B + 1, and then the word
has n_anti >= |Q| + 1 >= 2 anti runs (so B >= 2).
Proof.  D_Q >= |Q| + p implies D_Q >= 2|Q| + B + 1 because D_Q <= A = p + 1 + B forces |Q| <= B + 1 <=
p - B - 1.  With n_al, n_anti, n_pair the numbers of aligned, anti and (1,1) runs (sum p + 1), the
aligned excess sum_{al} (a_t - 1) = A - n_pair - n_al = B + n_anti, so D_Q <= |Q| + B + n_anti, and
D_Q >= 2|Q| + B + 1 gives n_anti >= |Q| + 1.  []
**Lemma BC3I-B (interval 3-partitions in the boundary case) [W].**  In the same setting a flat
3-partition Lemma BC certificate with three cyclic intervals X, Y, Z exists iff the cycle splits into
three consecutive arcs each with D <= B + 2.
Proof.  For an interval Q, lambda(Q) = f(D_Q), f(x) = min(p, x, floor((x + B)/2) + 1) <= x, with equality
iff x <= B + 2; as D_X + D_Y + D_Z = p + 1, condition (a) holds iff all three D <= B + 2.  The
complements have D >= p - 1 - B >= B + 4 and <= p + 1 + B <= 2p - 1 - B (B <= (p-5)/2), so
sum lambda(complements) = sum (floor((p + 1 - D_Q + B)/2) + 1) >= p + 1.5B + 2.5 >= p + 1 (the upper
inequality of (b)); the lower inequality of (b) follows from (a); (c): f(D_X) + f(p + 1 - D_X) >=
(D_X + p + B + 2)/2 >= 1 as D_X >= -B.  []
[F] boundviol.cpp (planted violators: k = p+1, kB = 1, R <= 2p-3, a heavy aligned run a_h >= B+3; output
out/boundviol_p11_p13_p17.txt, rerun 09:02-09:07 PDT): p = 11: 400 words, all violate (4.1), interval
split in 160, general flat 3-partition BC in 400; p = 13: 400 words, interval split in 118, flat
3-partition in 300, longer Lemma BC chains in the other 100; p = 17: 400 words, interval split in 120,
flat 3-partition in 299, longer chains in 101; no word without a Lemma BC certificate.  So in the
boundary case, words violating (4.1) need non-interval Lemma BC certificates; no proof of their
existence is given here.

## 5. Census of NMH (exact; aids) [F]

mhc.cpp (out/mhc_*.txt; out/mhc_aggregate.txt via agg.py; note: the label "<=-3" in mhc.cpp output
means R <= 2p-4).  Per word: FULL, ZSI, BC3 (flat 3-partition Lemma BC, k <= 13) and the exact
phi-search with pattern families m <= 1 / m <= 2 / all (DFS validated on a genuine avoider and on the
IL word, validate.py).
 * NO AVOIDER: p = 5 all (6,438 words, k = 6..8), p = 7 all (3,317,913 words, k = 8..12), p = 11
   (3,000 random, k = 12..18), p = 13 (1,500 random, k = 14..20).  No raw-DP confirmation was needed.
 * R >= 2p-2: always a full window (all p).
 * R <= 2p-3: k = p+1, kB = 1: interval ZS in 11,590/11,590 (p = 7), 101/103 (p = 11), 50/50 (p = 13);
   all other words with R <= 2p-3 at p = 5, 7 have a flat 3-partition certificate (BC3; 28 + 40,051
   words), but at p = 11, 13 BC3 is impossible for many words (e.g. sum_P lambda(P) <= (R + B)/2 + 3, so
   BC3 needs R + B >= 2p - 4) and the exact search shows that patterns with m >= 3 are needed for some
   words (p = 11: 151 of the 1,020 words with R <= 2p-3; p = 13: 96 of 621).
 * General Lemma BC (any ordered partition; bcgcheck.cpp, DP over subsets, k <= 15 resp. 16): every
   sampled word with R <= 2p-3 has a Lemma BC certificate (ZSI, BC3 or a longer chain):
   p = 11: 788 words (seed 111) + 8,945 words (seed 4242), 0 without certificate; p = 13: 340 words,
   0 without certificate (out/bcgcheck_p11.txt, out/bcgcheck_p11_b.txt, out/bcgcheck_p13.txt).
   Typical chains (bcgchain.cpp): first parts are sets of 2-3 pairwise non-adjacent runs (m = 2, 3,
   gaining m - 1 in the reflection term), the last part a long interval, e.g. p = 11, k = 13, R = 15,
   B = 1, kB = 2, d = (0,2,1^11): parts {1,3}, {2,5}, {4,6,7}, {0,8,...,12} with lambda = 3, 2, 3, 4.

## 6. What is proved and the precise open part

Proved here [W] (with the cited [W] reductions): NMH(p), hence MIX_DEF_HIGH(p), for every word whose
OR/M0-normal form has R in {2p-1, 2p}, or R >= 2p+1 with all |d_u| <= 2p - k + 1, or k = p+1, kB = 1 and
(4.1).  Proved obstruction: Lemma OBS.
Open (precise): NMH(p) for the normal forms with
 (i) R = 2p-2 (full window in all data; proof gap = the parity of E+),
 (ii) R >= 2p+1 with a run |d_u| > 2p - k + 1 (full window in all data),
 (iii) R <= 2p-3, except k = p+1, kB = 1 with (4.1) (no full window possible; Lemma OBS excludes
       pigeonhole certificates for kB >= 2; BC3 suffices at p <= 7 but not at p >= 11; general
       Lemma BC chains suffice in every sampled word at p = 11, 13).
Item (iii) is the substantive open core of MIX_DEF_HIGH(p); RUNS(p) is NOT claimed.  Recommended
route for (iii), supported by the data and forced by Lemma OBS for kB >= 2: a structured Lemma BC
chain (multi-block early parts, one long final interval), i.e. a value-independent lift-range
argument, not a pigeonhole one.
