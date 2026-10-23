# Theorem B0S: the family B = 0, k <= p of the residual class (all primes p >= 5)

Owner OlsonReflectionRigidity.  r1 written after host clock 2026-10-18T04:02:00-0700; r2 after 04:07 PDT (fix map Sec. 7);
r3 after 2026-10-18T04:37:09-0700 (fix map Sec. 8); r4 (this file) after 2026-10-18T05:24:31-0700 (fix map Sec. 9).  Status: written
proof [W].  r2 was hostile-reviewed by Codex (R/olson-b0s-r2-codex-v1.note.md, sha256
de3b1fa17bf30755dc8864ecbdfdb9b1ef16ad548b93d9a8a405182226490030: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 1 MINOR, applied in r3) and by
Claude (R/olson-b0s-r2-claude-v1.note.md: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 9 MINOR, applied here); r4 is not re-reviewed.
Notation: proof-K0star-r2.md (6681676e...96e1) Sec. 0-1 (G-words, Lemma H0) and proof-RED-r2.md (c4e7697f...d3d7) Sec. 5
(RES_<(p)).  Theorem scope: B = 0 only, i.e. all rotation letters equal to one rho_x, x != 0 [r4, Claude MINOR-7]; no statement
about rotation values, INV*(p) or ordered Olson.

## 0. Statement and imports

**Theorem B0S.**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) all of whose rotation letters are EQUAL to one
rho_x with x != 0 (after normalisation rho_1, i.e. B = 0) [r4, Claude MINOR-1], with F, R >= 1, whose maximal constant reflection blocks all have ODD length, whose number k of
blocks satisfies k <= p, and with kappa = p - 1 - H >= 1.  Empty rotation runs (necessarily genuine) are allowed in any number.
Then w has an identity 2p-subword.
(The excluded case x = 0 is trivial and not needed: the H in-block pairs sigma_y sigma_y and 2p - 2H = 2 kappa + 2 <= R letters
rho_0 = 1 form an identity 2p-subword, R >= p + 2 kappa by Sec. 1.  kappa = 0 lies outside B0S; it is Theorem K0*.)
**Corollary.**  RES_<(p) contains no avoider with B = 0 and k <= p.  It bears on REFL(p) only through Theorem RED
(proof-RED-r2.md Sec. 5), which assumes (I1)-(I4).  [r4, Claude MINOR-6] Unaudited remark (not used): for g = 0 the argument
also covers the RGR words of Proposition S1' and Lemma A1' (inverse-parity/proof-PAR-Kplus-partial-r2.md L164-230); the
hypotheses of those statements were not compared line by line.
Imports [r4, Claude MINOR-4, MINOR-5]: the one instance of Lemma H0 used here (B = 0, beta = 0, every m >= 1, solvable direction).
Lemma H0 (proof-K0star-r2.md L55-58) is now parent-accepted at exact scope (R/olson-reflection-K0star-RED-parent-verdict-v1.md,
879aeee7...c02a); it is an algebraic consequence of GR0, the {+1, -1} specialisation of the parent-accepted GRX
(rotation/notes-GRX-v1.md, afc6c31a...620b1a30; specialisation at its L44-45).  Direct derivation of the instance from GRX
(GRX L18; the reviewer's check): put z = +1 exactly on P (m intervals, R_P = E, all blocks odd); then Phi_z = 2m and
C_max = 2H + 2m, so the number n = 2p - C of rotations to choose is even and lies in [2 kappa + 2 - 2m, 2p - 2m]; choosing a
rotations in P and b in P^c gives sigma = a - b and T(z) = sum_P theta = 2 u_P, so the condition is x := (a - b)/2 = u_P; for an
integer x a valid integer b exists iff max(0, -2x, kappa + 1 - m - x) <= min(R - E, E - 2x, p - m - x), whose nine pairwise
inequalities are x <= floor(E/2), x <= p - m, x <= E + m - kappa - 1, their three mirror images, and three tautologies.  Hence
every integer of [-g_m(R - E), g_m(E)] is realised, for every m >= 1.  Nothing else: no RGR theorem, no inherited hypothesis,
no finite computation.

## 1. Set-up

All blocks odd, so o_F = k, beta(P) = 0 for every pattern, and R = 2p - k + 2 kappa by (0.1) of proof-K0star-r2.md.  If R >= 2p the
subword rho_1^(2p) is an identity, so assume R <= 2p - 1; hence k >= 2 kappa + 1 and, with k <= p, p >= 2 kappa + 1,
R - kappa >= p + kappa and R - 2 kappa = 2p - k >= p (so R >= p + 2 kappa).  For a pattern P with m intervals and R_P = E,
Lemma H0 (B = 0, beta = 0) gives I(P) = [-g_m(R - E), g_m(E)] with g_m(E) := min(p - m, E + m - kappa - 1, floor(E/2)); for a
proper interval (m = 1, E <= R <= 2p - 1), g_1(E) = min(E - kappa, floor(E/2)).  Kill test: if some integer congruent to u_P lies
in I(P), w is solvable.  Suppose w avoids; then no window is full.  Empty runs are runs with r_t = 0 and u_t != 0.

## 2. Lifts (Step 0) and the defect bound (Step 1)

Step 0.  Every proper interval window is nonempty.  The sum g_1(E) + g_1(R - E) is symmetric under E <-> R - E.  [r3 fix]
If either term uses the truncation branch, interchange E and R - E if necessary so that g_1(E) = E - kappa; then
g_1(E) + g_1(R - E) >= min(R - 2 kappa, (E + R - 1)/2 - kappa) >= min(2p - k, (2p - k - 1)/2) > 0.  Otherwise both terms are
floors and the sum is >= R/2 - 1 > 0.  (E = 0 and E = R are included: an interval may consist of empty runs only, or contain
all rotations; e.g. at E = R, g_1(R) = floor(R/2) while g_1(0) = -kappa uses the truncation branch, so the interchanged form
of the first case applies.)  Index the runs 1..k cyclically and let
V_j (1 <= j <= k - 1) be the unique integer congruent to u_((0, j]) in the gap [g_1(rho_j) + 1, p - g_1(R - rho_j) - 1]
(rho_j := r_1 + ... + r_j); V_0 := 0, V_k := p; x_t := V_t - V_(t-1), so x_t = u_t (mod p), sum_t x_t = p, and for every pattern P,
x(P) := sum_(t in P) x_t = u_P (mod p).  bh_t := 2 x_t - r_t = r_t (mod 2); sum_t bh_t = 2p - R = k - 2 kappa.  An empty run has
bh_t = 2 x_t and x_t != 0.
Step 1.  For every run t, x_t >= -L^t, where U^t := g_1(r_t), L^t := g_1(R - r_t).  For t = 1 and t = k this is the nonemptiness of
the window of {t} (x_1 >= U^1 + 1, x_k = p - V_(k-1) >= U^k + 1).  For 2 <= t <= k - 1, x_t >= g_1(rho_t) + g_1(R - rho_(t-1)) + 2 - p,
so it suffices that S := g_1(rho_t) + g_1(R - rho_(t-1)) + L^t >= p - 2.  With alpha := rho_(t-1), rho_t = alpha + r_t and
g_1(E) >= min(E - kappa, (E - 1)/2), the eight choices T (truncation term) / F (floor term) give
 FFF: S >= R - 3/2;  TFF: S >= R - kappa - 1;  FTF: S >= R - kappa - 1;  TTF: S >= 2p - k + (R + r_t - 1)/2;
 FFT: S >= R - kappa - 1;  TFT, FTT: S >= 3R/2 - 2 kappa - 1/2 = (2p - k) + R/2 - 1/2;  TTT: S = 2R - 3 kappa,
each >= p - 2 by Sec. 1 (this replaces the RGR assumption R - r_t >= k - 1, false for G-words with large runs).  A defect is a
run with bh_t <= 0, i.e. x_t <= r_t/2 < p - L^t (as L^t <= (R - r_t)/2 and R < 2p); avoidance of {t} then excludes
[-L^t, U^t] and forces x_t >= U^t + 1; as x_t <= floor(r_t/2), U^t = r_t - kappa and
    delta_t := -bh_t = r_t - 2 x_t <= 2 kappa - 2 - r_t.                                                        (2.1)
An empty defect has x_t in [1 - kappa, -1].  Every defect has r_t + delta_t >= 2 and r_t + delta_t even (delta_t = r_t mod 2; an odd
run has delta_t >= 1; an empty defect has delta_t >= 2).

## 3. Kill conditions

For a proper pattern P with m intervals put rho_P = R_P, delta_P := -sum_(t in P) bh_t = rho_P - 2 x(P) (any sign; delta_P = rho_P
mod 2) and Phi(P) := rho_P + 2m + delta_P.  x(P) lies in I(P) -- so P kills -- iff
 (U1) rho_P + 2m - delta_P <= 2p;  (U2) Phi(P) >= 2 kappa + 2;  (U3) delta_P >= 0;
 (L1) delta_P + 2m - rho_P <= 2p;  (L2) delta_P + rho_P - 2m <= 2R - 2 kappa - 2;  (L3) delta_P <= R - [R - rho_P odd],
(the six inequalities x(P) <= p - m, x(P) <= rho_P + m - kappa - 1, x(P) <= floor(rho_P/2) and their three lower analogues;
(U3) is exact from the integrality of x(P); the parity delta_P = rho_P mod 2 only reconciles the two forms of (L3), which is
equivalent to delta_P <= R [r4, Claude MINOR-9]).  Z := set of defects.  Z != empty: otherwise every bh_t >= 1, empty runs have
bh_t >= 2, and sum bh_t >= k > k - 2 kappa.  Z is proper: sum bh_t = k - 2 kappa >= 1.  Phi(P) = 2(rho_P - x(P)) + 2m is even for every P [r4, Claude MINOR-9].
If kappa = 1, (2.1) and r_t + delta_t >= 2 give 2 <= 0 for every defect, so no defect exists and Z != empty is already a
contradiction [r4, Claude note].

## 4. Case I: Phi(Z) >= 2 kappa + 2

Add the defects to P one at a time (any order).  Phi of one defect is r_t + delta_t + 2 <= 2 kappa by (2.1), and each addition
raises Phi by at most r_t + delta_t + 2 <= 2 kappa; let P be the first set with Phi(P) >= 2 kappa + 2.  The previous set had
Phi <= 2 kappa (even), so Phi(P) <= 4 kappa.  Then (U2), (U3) hold; (U1), (L1) follow from Phi(P) <= 4 kappa <= 2p (p >= 2 kappa + 1);
(L2) from Phi(P) <= 4 kappa <= 2R - 2 kappa - 2 (R >= p + 2 kappa >= 4 kappa + 1); (L3) from
delta_P <= Phi(P) - 2 <= 4 kappa - 2 <= R - 1.  So P kills: contradiction.

## 5. Case II: Phi(Z) <= 2 kappa (the case created by empty runs)

Write Y := [k] \ Z, s := sum_(t in Y) (bh_t - 1) >= 0 (each non-defect has bh_t >= 1; empty or even non-defects have bh_t >= 2),
g_Z := number of empty defects, m_Z := m(Z).  From sum bh_t = k - 2 kappa: delta_Z = 2 kappa - |Z| + s.  From Phi(Z) >= 2|Z| + 2 m_Z:
|Z| <= kappa - m_Z.  From Phi(Z) <= 2 kappa: rho_Z <= |Z| - 2 m_Z - s; with rho_Z >= |Z| - g_Z this gives s <= g_Z - 2 m_Z, so
g_Z >= 2 m_Z >= 2 (Case II needs at least two empty defects), and delta_Z - rho_Z >= 2 kappa - 2|Z| + 2 m_Z + 2s >= 4 m_Z.
Deficit: d := 2 kappa + 2 - Phi(Z) = 2 + |Z| - rho_Z - 2 m_Z - s, even, 2 <= d <= g_Z <= kappa - 1.
Items.  Let U be the set of non-defects with bh_t = 1 that are not adjacent (in the cyclic run order) to a run of Z.  At most
2 m_Z runs are adjacent to Z and at most s non-defects have bh_t >= 2, so |U| >= |Y| - 2 m_Z - s.  In every maximal cyclic interval
of U-runs take every second run, starting with its first; the resulting family F has |F| >= |U|/2, its runs are pairwise
non-adjacent and non-adjacent to Z.  |F| >= d/2: this is k - |Z| - 2 m_Z - s >= 2 + |Z| - rho_Z - 2 m_Z - s, i.e.
k >= 2 + 2|Z| - rho_Z, true as k >= 2 kappa + 1 and |Z| <= kappa - 1.
Choice of W subset of F: if some y in F has r_y + 1 >= d, W := {y}; otherwise add runs of F one at a time until
sum_W (r_y + 1) >= d (possible since each gives >= 2 and |F| >= d/2), so |W| <= d/2 and sum_W (r_y + 1) <= 2d - 2 (by parity
even <= 2d - 4; not needed).
P := Z u W.  P is proper [r4, Claude MINOR-3]: Z is nonempty and proper, so some run outside Z is adjacent to Z; that run lies
in Y \ U, hence not in W, hence not in P.  Each y in W is its own interval, so m(P) = m_Z + |W|, rho_P = rho_Z + sum_W r_y, delta_P = delta_Z - |W|, and
Phi(P) = Phi(Z) + sum_W (r_y + 1) >= 2 kappa + 2: (U2).  (U3): delta_P >= delta_Z - d/2 >= (kappa + 1) - (kappa - 1)/2 > 0
(delta_Z = 2 kappa - |Z| + s >= kappa + 1).  (L3): delta_P <= delta_Z <= 2 kappa - 2 <= R - 1 (s <= g_Z - 2 m_Z <= |Z| - 2).
(U1): rho_P - delta_P + 2m(P) = (rho_Z - delta_Z) + 2 m_Z + sum_W (r_y + 1) + 2|W| <= -2 m_Z + sum_W (r_y + 1) + 2|W|, which is
<= r_y + 1 <= 2p for W = {y} (m_Z >= 1) and <= 3d - 2 - 2 m_Z <= 3 kappa - 7 < 2p otherwise.  (L1): delta_P - rho_P + 2m(P) <= delta_Z - rho_Z
+ 2 m_Z <= 2 kappa - 2 + 2(kappa - 1) < 2p.  (L2): delta_P + rho_P - 2m(P) <= Phi(P) - 4m(P), which is <= 2 kappa + r_y + 1 - 8 <= 2p + 2 kappa - 8
for W = {y} (m(P) = m_Z + 1 >= 2) and <= 2 kappa + 2d - 2 <= 4 kappa - 4 otherwise; both are <= 2R - 2 kappa - 2 (>= 2p + 2 kappa - 2).  So P kills: contradiction.  []

## 6. Remarks

(1) Where empty runs enter: Step 1 (runs with R - r_t <= 2 kappa - 2 exist only because other runs may be empty; handled by the
eight-case bound), the empty-defect range x_t in [1 - kappa, -1] (genuineness), and Case II, which cannot occur for RGR words
(it needs g_Z >= 2) and is closed by adding isolated runs with bh = 1.  The parity facts "Phi even on Z" and "r_t + delta_t even"
are what make Case II need two empty defects and make the bounds hold for p >= 2 kappa + 1, so R = 2p - 1 (k = 2 kappa + 1) needs
no separate full-window lemma.
(2) Not covered: B = 0 with k >= p + 1 (the RGR analogue is C0-B' with the Depth Lemma, proof-RUNS.md Secs. 9-11, whose Step 1
uses k + r_t <= R + 1, false here), kappa = 0 (Theorem K0*), and the classes with B >= 1 (k <= p: Theorem MXG,
proof-MXG-r3.md; k >= p + 1: open).
(3) Finite aids (not premises).  E8 (plan-E8.md 37773b44...ebe0, code/e8_b0s_replay.py 1c4c5033...3743,
out/e8_b0s_replay.json): random words were all killed by a prefix interval (931) or a full prefix window (104); the extreme
Case II family of plan-E7 reached the proof pattern 130 times (Case I 87, Case II 43), 0 failures of (U1)-(L3) or of the
actual hit; mutation control (one W item replaced by a bh = 1 run adjacent to Z): the kill survived in only 15 of 43, so the
non-adjacency is used.  E8b (plan-E8b.md ba3668b3...91ab1f, code/e8b_lift_sampled.py 20546ba7...7e15,
out/e8b_lift_sampled.json): 4000 words with values sampled through the Step 0 gaps, p = 5..29: 2006 singleton kills, 1994
Case I proof-pattern kills, 0 failures (Case II never arose under uniform lift sampling).  Raw DP (dp1 = dp2): 657/657 (E8)
and 1500/1500 (E8b) words with p <= 11 solvable.

## 7. Fix map r1 -> r2

Only arithmetic in two displayed bounds changed; no step or case changed.  Step 0: the second term of the minimum is
(2p - k - 1)/2 (r1 wrote p - 1 - kappa, not what the displayed inequality gives; both are positive).  Case II (U1),
W = {y}: the bound is r_y + 1 <= 2p (r1 wrote 2p - 1, false when r_y = 2p - 1; the condition needed is <= 2p).  Case II
(L2), W = {y}: m(P) >= 2 gives the sharper 2 kappa + r_y - 7 (r1's weaker bound also sufficed).

## 8. Fix map r2 -> r3

Codex MINOR (r2 L30-32): "otherwise both terms are floors" was false as written, because at E = R one has g_1(E) = floor(R/2)
while g_1(R - E) = g_1(0) = -kappa uses the truncation branch.  Repaired as the reviewer proposed: if either term uses the
truncation branch, interchange E and R - E (the bounded sum is symmetric) and apply the displayed bound; otherwise both
terms are floors.  No other statement or step changed.  The reviewer also confirmed that the Corollary does not use
Theorem RED or its imports (it is a direct consequence of the Theorem, as RES_< words with B = 0 and k <= p satisfy the
hypotheses).


## 9. Fix map r3 -> r4 (Claude review of r2, R/olson-b0s-r2-claude-v1.note.md; no step, case or formula changed)

1. MINOR-1: the statement now says rho_x with x != 0; the trivial x = 0 case is recorded (not needed).
2. MINOR-2: Step 0 symmetry, already applied in r3 (Codex MINOR).
3. MINOR-3: properness of P = Z u W in Case II is proved (an outside neighbour of Z lies in Y \ U, so not in W).
4. MINOR-4: imports distinguish GRX from its GR0 specialisation; H0's parent acceptance is cited; the direct derivation of
   the H0 instance used (B = 0, beta = 0, every m) from GRX is included.
5. MINOR-5: the GRX hash pin is corrected to afc6c31a...620b1a30 (r1-r3 printed the suffix ...0a30).
6. MINOR-6: the S1'/A1' cross-claim is labelled an unaudited remark, not used.
7. MINOR-7: the scope line says B = 0 only.
8. MINOR-8: the r1 -> r2 fix map (Sec. 7) said "two displayed bounds"; three displayed corrections were listed (Step 0,
   Case II (U1) W = {y}, Case II (L2) W = {y}).  Sec. 7 is kept verbatim as history; this item corrects its count.
9. MINOR-9 (cosmetic): (U3) exact from integrality; Phi(P) even for every P; the parity sharpening 2d - 4 noted; the
   kappa = 1 case made explicit; kappa = 0 and the B >= 1 classes placed in Remark (2); the Corollary's relation to REFL via
   RED's (I1)-(I4) stated.
