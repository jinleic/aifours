# PAR for kappa >= 1: odd-segment reduction, Theorem K1, the integer lemma, and the open part

Lane `olson`, owner OlsonParity.  Written after host clock 2026-10-17T04:20:38-07:00.
Revision r2 (host clock 2026-10-17T11:43:46-07:00): answers the three MINOR findings of
institute/runs/six-lane-2026-10-16/review/olson-parity-k0-kplus-codex-review-v1.note.md
(review input: proof-PAR-Kplus-partial.md, sha cc289e5d...a7e5, kept unchanged).  Changes
only: Sec. 1 Remark (conditional preservation), Lemma A1' (coloured-pattern connectivity,
vacancy construction), Theorem KB uncapped (b) upper inequality (second capped term); see
the change log at the end.  Status: Sec. 1-3, 3', 6 written proofs [W], reviewed once
(ACCEPT-WITH-FIXES, fixes applied here); Sec. 4-5 precise open statements with evidence.
Notation as in proof-PAR-K0.md Sec. 1 (Lemma H, Lemma BC).

Throughout: w in RGR_{4p-2}(p), F, R >= 1, normalised B <= A, an avoider, so B <= kappa
(zero condition) and every window |I(Q)| <= p - 1.  Recall (V) <=> kappa <= o_F - 1, so
kappa >= 1 forces o_F >= 2.

## 1. Odd-segment reduction (Lemma OR)

Let O be the set of odd reflection runs (o_F >= 1).  The o_F segments G_1, ..., G_{o_F}
are the maximal sets of rotation runs strictly between cyclically consecutive odd
reflection runs.  A pattern whose boundary runs all lie in O is exactly a union of
segments; for it beta = 0 and m is its number of blocks counted in segments.

**Lemma OR.**  Let w~ be the RGR word of length 4p-2 obtained from w by merging every
segment into one rotation run (a~_j = A_{G_j}, b~_j = B_{G_j}) and every even reflection
run into the odd reflection run that ends its segment (so all o_F reflection runs of w~
are odd, with the values y of the odd runs of w).  Then R, F, A, B, H, kappa of w~ equal
those of w, k(w~) = o_F, and if w avoids then w~ avoids.
Proof.  R, F, A, B are unchanged and H = (F - o_F)/2 is unchanged (o_F(w~) = o_F(w)), so
kappa is unchanged.  A proper pattern Q~ of w~ is a union of segments of w, i.e. a pattern Q
of w with all boundary runs odd; Q~ and Q have the same m, beta = 0, D_Q + B, hence by
Lemma H the same lambda and the same window; and u_{Q~} = u_Q because both are the sum of
y-differences at the same odd reflection runs (theta telescopes over the merged runs).  The
P = empty condition (0 notin I(empty) mod p, which depends only on A, B, kappa) is the same.
By Lemma H applied to w~, its avoidance conditions are a subset of those of w.  []

Remark (conditional preservation).  w~ may violate (P) and (D0) (a segment can contain
>= p equal rotations).  Since R, F, A, B, H, kappa and o_F are unchanged, each of (E), (V),
(Pairs) (conditions on R and H only) holds for w~ whenever it is assumed for w;
k(w~) = o_F(w) <= k(w), so k(w~) <= p holds whenever k(w) <= p (or just o_F(w) <= p) is
assumed; and if w~ avoids, it satisfies the zero condition B <= kappa (Lemma H; A, B <= 2p - 1
are unchanged).  Each later use of Lemma OR states the input bounds it needs.

## 2. Theorem K1 (kappa = 1, B = 0)

**Theorem K1.**  Let p >= 5 be prime and w in RGR_{4p-2}(p) with F, R >= 1, k <= p,
(V), kappa = 1 and B = 0 after normalisation.  Then w has an identity 2p-subword.
(Hence PAR holds for inherited avoiders with kappa = 1, B = 0.)
Proof.  Suppose w avoids; by Lemma OR so does w~, with k~ = o_F >= 2 runs (kappa <= o_F - 1),
all reflection runs odd, all rotation letters rho_1, r~_j >= 1, R = 2p - o_F + 2.
For a cyclic interval Q of w~ (m = 1, beta = 0) Lemma H gives
lambda(Q) = min(p, R_Q, floor(R_Q/2) + 1) = min(p, floor(R_Q/2) + 1) (as R_Q >= 1).
Partition: the o_F single runs of w~ in cyclic order.  Each r~_j <= R - 1 <= 2p - 1, so
lambda({j}) = floor(r~_j/2) + 1 >= (r~_j + 1)/2 and the sum is >= (R + o_F)/2 = p + 1:
condition (a) of Lemma BC.  For (b): every lambda of an interval is >= 1, so the lower
inequality holds (sum >= 3).  For the upper one, X u Y, Y u Z, Z u X are proper intervals
with R-values summing to 2R; if none is capped at p their lambdas sum to
>= (2R - 2)/2 + 3 = R + 2 >= p + 4 (R >= p + 2 since o_F <= p); if one is capped, the sum
is >= p + 1 + 1.  (c): both lambdas >= 1.  Lemma BC applied to the avoider w~ gives the
contradiction.  []
Control: all inherited kappa = 1, B = 0 run data with k <= p at p = 5 (2,366) and
p = 7 (426,275) pass this certificate (session check `seg_chain_check`, recorded in
notes-checkpoint.md).

**Theorem K1' (kappa = 1, B = 1).**  Same hypotheses with kappa = 1, B = 1, and w
satisfying (D0).  Then w has an identity 2p-subword.  (So PAR holds for every inherited
avoider with kappa = 1.)
Proof.  Suppose w avoids.  In w~ (Lemma OR) let G* be the segment containing the unique
rho_{-1}; o_F >= 2, R = 2p - o_F + 2, D = 2p - o_F.  For a cyclic interval Q of w~,
lambda(Q) = min(p, D_Q + 1, floor((D_Q + 1)/2) + 1): it is >= 1 unless Q is the single run
{rho_{-1}} (D_Q = -1, lambda = 0).  Single-run partition of w~:
lambda(G_j) = min(p, ceil(r~_j/2) + 1) for j != *, and lambda(G*) = min(p,
floor((r~* - 1)/2) + 1) if r~* >= 2, lambda(G*) = 0 if r~* = 1.  Without caps the sum is
>= R/2 + o_F - 1 = p + o_F/2 if r~* >= 2, and >= (R - 1)/2 + o_F - 1 = p + (o_F - 1)/2 if
r~* = 1; a cap (ceil(r~_j/2) + 1 > p, i.e. r~_j >= 2p - 1) needs a segment with >= 2p - 1
of the R = 2p - o_F + 2 rotations, so o_F = 2 and the other segment is a single letter.
Hence the sum is >= p + 1 except in the case E: o_F = 2, G* = {rho_{-1}}, G_1 = 2p - 1
letters rho_1.  Outside E, (b) and (c) of Lemma BC hold for the cyclic order: at most one of
three intervals partitioning the cycle has lambda = 0, the others have lambda >= 1; each of
the three unions has lambda >= 1, and either one is capped (sum >= p + 2) or the sum is
>= (2D + 3 - 3)/2 + 3 = D + 3 >= p + 3.  So Lemma BC kills w~.
Case E in w itself: by (D0) the 2p - 1 letters rho_1 of G_1 form c >= 3 rotation runs
t_1, ..., t_c (in cyclic order after the odd run O_2 that follows G*), separated by c - 1
even reflection runs E_1, ..., E_{c-1}.  Take the parts G*, {t_1}, T := {t_2, ..., t_c} of w
(cyclic intervals; boundaries (O_1, O_2), (O_2, E_1), (E_1, O_1)).  With B = kappa = 1:
lambda(G*) = 0; lambda({t_1}) = min(p, r_1, ceil(r_1/2) + 1) (= ceil(r_1/2) + 1 if r_1 >= 2,
= 1 if r_1 = 1); lambda(T) = min(p, R', ceil(R'/2) + 1) = ceil(R'/2) + 1 with
R' = 2p - 1 - r_1 in [p, 2p - 2].  As r_1 + R' is odd, ceil(r_1/2) + ceil(R'/2) = p, so
the sum is p + 2 (r_1 >= 2) or p + 1 (r_1 = 1).  Lower inequality of (b): 0 + 1 + 1 >= 1.
Upper inequality: lambda(G_1) = min(p, 2p, p + 1) = p and lambda(T u G*) =
floor(R'/2) + 1 >= 1, so the three unions give >= p + 1.  (c) holds.  Lemma BC.  []
Control: all inherited kappa = 1, B = 1 run data with k <= p at p = 5 (10,512: 10,446 by
the w~ single-run chain, 66 by case E) and p = 7 (2,411,817: 2,407,001 + 4,816) pass
(session check `check_k1p`).

## 3. The integer lemma (combinatorial core for kappa >= 1, B = 0)

**Lemma IP.**  Let v be an RGR word of length 4p-2 with all k reflection runs odd, B = 0,
1 <= kappa <= k - 1 (so R = 2p - k + 2kappa).  Let x in Z^k with sum_t x_t = p, put
bh_t := 2x_t - r_t, Z := {t : bh_t <= 0}, N := [k] \ Z.  Then Z is nonempty, and if N is
nonempty then x(Z) := sum_{t in Z} x_t < lambda(Z).

Proof.  sum_t bh_t = 2p - R = k - 2kappa < k, so not all bh_t >= 1.  Suppose N != empty
and x(Z) >= lambda(Z), i.e. (Lemma H with beta = 0, B = 0)
BH(Z) := sum_{Z} bh_t = 2x(Z) - R_Z >= min(C, T, 2 - [R_Z odd]),
C := 2p + 2 - 2m - R_Z, T := R_Z + 2m - 2kappa, m = m(Z) >= 1.  As BH(Z) <= 0 the floor
term is not the minimum, so BH(Z) >= T or BH(Z) >= C.  Since bh_t >= 1 on N,
BH(Z) <= (k - 2kappa) - |N| = |Z| - 2kappa.
If BH(Z) >= T: R_Z + 2m <= |Z|, impossible (R_Z >= |Z|, m >= 1).
If BH(Z) >= C: R_Z + |Z| + 2m >= 2p + 2 + 2kappa; with R_Z <= R - |N| =
2p - 2k + 2kappa + |Z| this gives |Z| + m >= k + 1, but the m blocks of Z are separated by
runs of N, so m <= |N| and |Z| + m <= k.  []
(Random check of the statement: 198,887 instances, p <= 23, 0 failures.)

Consequence.  If w~ (Lemma OR) is an avoider with B = 0, kappa >= 1, then for EVERY integer
vector x with x_t = u_t (mod p) and sum x_t = p, writing Z = Z(x), N = N(x):
either N = empty, or x(Z) lies outside [1 - lambda(N), p + lambda(Z) - 1].
(Indeed u_Z notin I(Z), so by the Claim in the proof of Lemma BC an x(Z) in that range would
satisfy x(Z) >= lambda(Z), contradicting Lemma IP.)  The upper end is harmless in practice
(x(Z) <= R_Z/2); the content is the lower end x(Z) >= 1 - lambda(N) ("lap for Z").

## 4. What is open (precise; updated 2026-10-17T05:50 PDT)

PAR(p) = Theorem K0 (kappa = 0) + K+_viol(p): no inherited avoider with k <= p, an even
run, kappa >= 1 and B <= min(A, kappa).  Status of K+_viol (every parity, not only
violators):
* kappa = 1: Theorems K1, K1' (this file, Sec. 2).
* B = 0, kappa >= 1: proved for k <= p in Sec. 3' (Proposition S1' for R <= 2p-2,
  Lemma A1' for R = 2p-1, rho_1^{2p} for R >= 2p, after Lemma OR); this is the k <= p part of
  OlsonRunCount's Corollary B0 (../inverse-run-count/proof-RUNS.md Sec. 11 [W]), whose
  Steps (their Sec. 9) and Lemma A1 Sec. 3' follows and rechecks.
* B = kappa >= 1: Theorem KB (Sec. 6), for every word with o_F <= p.
* 1 <= B < kappa: OPEN.  Exact remaining statement (owned by OlsonRunCount as MIX_DEF(p),
  ../inverse-run-count/mixdef/): every RGR word of length 4p-2 with all reflection runs
  odd and 1 <= B < kappa, B <= A, has an identity 2p-subword.  By Lemma OR it implies
  K+_viol in this range (and Lemma M0 of proof-RUNS.md Sec. 12 lets one assume every merged
  run pure or a (1,1)-pair).
So: PAR(p) <= MIX_DEF(p) restricted to o_F <= p (all other cases proved in this directory:
K0, K1, K1', S1' + A1' (B = 0), KB (B = kappa)).  Only Lemma M0 (pair removal, rechecked:
every E+- drops by 1 and h rises by 1, so every half window shrinks) is quoted from
proof-RUNS.md, and only as a normalisation inside MIX_DEF.
The earlier B = 0 reduction to LIFT (Sec. 3 Consequence) is superseded by Sec. 3';
Lemma IP is kept as the integrality core it shares with Proposition S1'.

## 5. Evidence and failed approaches (aids; finite)

* Interval (single-bracket) certificates do not suffice at p = 11 (notes F1).
* Lemma BC with the best set partition fails at p = 17 (notes F4(i)): any proof of
  K+_viol must use integrality, cf. the p = 19 family where the LP relaxation is feasible
  and the integer program is not (notes F4(ii)).
* Lemma IP is exactly such an integrality argument; in all sampled data (notes F5) the
  defect set Z of the interval-chain lifts kills directly and "strong lap" held for every
  interval-feasible theta tested (p = 11, 13, 17), i.e. LIFT held with x = chain lifts.
* Finite-exact status of K+_viol: p = 5 (all k <= 5) and p = 7 (k <= 5) by s <= 3 block
  chains for all inherited kappa >= 1 words (any parity); p = 7, k <= 7 for violators by the
  earlier worker's PAR(7) run (../proof-INV-reduction.md 3.1; code-fidelity unreviewed).
* The length-(4p-1) variant does not help: Lemma BC also fails there (p = 19, kappa_w = 3,
  best partition = p) although Theorem DR could be rerouted to need only K0 plus a
  length-(4p-1) statement (notes, checkpoint 3).

## 3'. Cross-check: B = 0, all reflection runs odd, k <= p (written after
## 2026-10-17T05:51:59-07:00; re-derivation of OlsonRunCount's Theorem S1 / Lemma A1)

**Proposition S1'.**  Let v be an RGR word of length 4p-2 with all k reflection runs odd,
all rotation letters rho_1, k <= p, kappa >= 1 and R = 2p - k + 2kappa <= 2p-2 (i.e.
k >= 2kappa + 2; then p >= 2kappa + 3 as p is odd).  Then v has an identity 2p-subword.
Proof (Steps of ../inverse-run-count/proof-RUNS.md Sec. 9, rechecked for k <= p).  With
g_m(E) := min(p - m, E + m - kappa - 1, floor(E/2)) the window of a pattern with m blocks and
R_Q = E is [-g_m(R - E), g_m(E)] (Lemma H, beta = 0, B = 0).  If some window is full we are
done (for R <= 2p-3 none is: |I| <= floor(E/2) + floor((R - E)/2) + 1 < p); assume none is.
For a proper interval E <= R - 1 <= 2p - 3, so floor(E/2) <= p - 2 and
g_1(E) = min(E - kappa, floor(E/2)).
Step 0.  Every interval window is nonempty (if g_1(E) = E - kappa then g_1(E) + g_1(R - E)
>= (E + 2p - k - 1)/2 > 0; if both are truncation terms the sum is 2p - k > 0).  Prefix
lifts V_j := the representative of u_{(0,j]} in [g_1(rho_j) + 1, p - g_1(R - rho_j) - 1]
(rho_j = r_1 + ... + r_j), V_0 = 0, V_k = p (for P = empty the window is
[-g_0(R), g_0(0)] with g_0(0) = -kappa - 1 < 0 <= p - g_0(R) - 1, so 0 is the lift of the
empty set, and symmetrically p is that of [k]); x_t := V_t - V_{t-1}, so sum x_t = p,
bh_t := 2x_t - r_t = r_t (mod 2), sum bh_t = 2p - R = k - 2kappa.
Step 1 (defects).  Put U^t = g_1(r_t), L^t = g_1(R - r_t) = floor((R - r_t)/2) (because
R - r_t >= k - 1 >= 2kappa + 1).  Then x_t >= -L^t: for t = 1 and t = k directly; for
2 <= t <= k-1, x_t >= g_1(rho_t) + g_1(R - rho_{t-1}) + 2 - p and
S := g_1(rho_t) + g_1(R - rho_{t-1}) + L^t >= p - 2 in the four cases (floor/floor:
S >= R - 1 >= p + 1; truncated/floor: S >= rho_t/2 + R - kappa - 1 >= p - 1/2 since
R - kappa = (R - k + 2p)/2 >= p; floor/truncated: S >= R - kappa - 1 + (R - rho_{t-1})/2 >= p - 1;
both truncated: S >= 2p - k + (R + r_t - 1)/2 >= p).  Avoidance of {t} then forces
x_t >= U^t + 1 or x_t >= p - L^t; a defect (bh_t <= 0, i.e. x_t <= r_t/2 < p - L^t as R < 2p)
therefore has U^t + 1 <= x_t <= floor(r_t/2), so U^t = r_t - kappa and
delta_t := -bh_t <= 2kappa - 2 - r_t.
Step 2.  Z := {bh_t <= 0} is nonempty (sum bh_t < k) and proper (sum bh_t = k - 2kappa >= 2).
For P subset Z with m blocks put rho_P = R_P, delta_P = -sum_P bh_t >= 0,
Phi(P) = rho_P + 2m + delta_P.  With Y = [k] \ Z: delta_Z = sum_Y bh - (k - 2kappa) >=
2kappa - |Z|, hence Phi(Z) >= 2m_Z + 2kappa >= 2kappa + 2.
Step 3 (direct kill).  x(P) = (rho_P - delta_P)/2 lies in [-g_m(R - rho_P), g_m(rho_P)] (so
P kills) as soon as (K1) Phi(P) >= 2kappa + 2, (K3) rho_P + 2m <= 2p, (K4) delta_P <= R - 1,
(K5) delta_P + rho_P - 2m <= 2R - 2kappa - 2, (K6) delta_P + 2m - rho_P <= 2p: indeed
x(P) <= floor(rho_P/2) because delta_P = rho_P (mod 2) and delta_P >= 0; (K1) is
x(P) <= rho_P + m - kappa - 1; (K3) gives x(P) <= p - m; (K6), (K5), (K4) are the three
lower bounds x(P) >= -(p - m), -(R - rho_P + m - kappa - 1), -floor((R - rho_P)/2).
Step 4 (greedy).  Order Z by increasing delta_t, P_i = first i elements.  Adding one defect
changes Phi by at most r_t + delta_t + 2 <= 2kappa; i* := least i with Phi(P_i) >= 2kappa + 2
exists (Step 2) and i* >= 2.  P := P_{i*}: Phi(P) <= 4kappa + 1 and delta_P <=
(2kappa - i*) + (2kappa - 3) <= 4kappa - 5.  Since 2kappa + 3 <= p and k <= p:
(K4) 4kappa - 5 <= p + 2kappa - 1 <= R - 1; (K3), (K6): left sides <= Phi(P) <= 4kappa + 1
<= 2p - 5; (K5): left side <= 4kappa + 1 <= 2p + 2kappa - 2 <= 4p - 2k + 2kappa - 2 = 2R - 2kappa - 2.
So P kills.  []
**Lemma A1' (B = 0, R = 2p - 1; OlsonRunCount's Lemma A1, proof rechecked).**  Same setting with
R = 2p - 1 (k = 2kappa + 1): some window is full.  With m* = floor(kappa/2) + 1, every
m*-block pattern P with kappa <= R_P <= R - kappa has, for E in {R_P, R - R_P},
ceil(E/2) >= ceil(kappa/2) = kappa + 1 - m* and floor(E/2) <= floor((2p - 1 - kappa)/2) = p - m*,
so g_{m*}(E) = floor(E/2) on both sides and |I(P)| = floor(R_P/2) + floor((R - R_P)/2) + 1 = p
(R odd).  Such P exists.  Cut positions are the k reflection runs; an m*-block pattern is a
set of 2m* distinct cut positions together with an alternating colouring (in P / not in P)
of the arcs between consecutive cuts.  Since 2m* <= kappa + 2, we have 2m* + 1 <= 2kappa + 1 = k
(also for kappa = 1), so some cut position is free.  An elementary move shifts one cut to a
free adjacent cut position, the colours of the two arcs at that cut travelling with it; it
keeps 2m* distinct cuts (m* nonempty blocks) and changes R_P by exactly one
r_u <= R - (k - 1) = 2p - k (the run passed over changes membership).  Vacancy construction:
label the cuts c_1, ..., c_{2m*} in cyclic order at positions pi_1, ..., pi_{2m*}, with a free
position strictly between pi_j and pi_{j+1} (indices mod 2m*).  Move c_j one step forward
into it (vacating pi_j); then move c_{j-1} forward to pi_j, then c_{j-2} to pi_{j-1}, ...,
then c_{j+1} to pi_{j+2} (each target has just been vacated and the positions passed over are
free); finally move c_j on to pi_{j+1}, vacated by c_{j+1}.  Now every c_i sits at pi_{i+1}:
the cut set is the original one and every arc carries the colour of the preceding arc, so the
colours are swapped and the final pattern is P^c, with R_{P^c} = R - R_P.  Take any m*-block
pattern P.  If kappa <= R_P <= R - kappa we are done.  Otherwise, replacing P by P^c if
necessary, R_P < kappa and R_{P^c} > R - kappa; along the path of elementary moves from P to
P^c the value R_P changes in steps <= 2p - k, while [kappa, R - kappa] contains
R - 2kappa + 1 = 2p - k + 1 integers, so some pattern on the path has
kappa <= R_P <= R - kappa.  []
For R >= 2p (B = 0) the subword rho_1^{2p} is an identity 2p-subword.  Hence, via Lemma OR,
every inherited word with k <= p, B = 0 and kappa >= 1 is solvable (Proposition S1' for
o_F >= 2kappa + 2, Lemma A1' for o_F = 2kappa + 1, R >= 2p for o_F <= 2kappa), independently
of the Depth Lemma; this agrees with OlsonRunCount's Corollary B0.

## 6. Theorem KB (kappa = B >= 1) (written after 2026-10-17T05:51:59-07:00)

**Theorem KB.**  Let p >= 5 be prime and w in RGR_{4p-2}(p), F, R >= 1, normalised
A >= B, with B = kappa >= 1, (V) and o_F <= p (any k, any reflection parities).  If the merged
word w~ of Lemma OR has a segment G with A_G - B_G >= 2p - 1, assume also (D0) for w.  Then w
has an identity 2p-subword.  In particular K+_viol holds when B = kappa.
Proof.  Suppose w avoids; then so does w~ (Lemma OR): k~ = o_F runs, all reflection runs
odd, kappa = B, B + 1 <= k~ <= p by (V).  Put d_j := A_{G_j} - B_{G_j} for the runs of w~,
D := A - B = R - 2B = 2p - k~ (>= p), so sum_j d_j = D.  For a cyclic interval Q of w~ with
D_Q := sum_{j in Q} d_j Lemma H gives lambda(Q) = f(D_Q), f(x) := min(p, x + 1,
floor((x + B)/2) + 1).  Facts: (i) f(x) = x + 1 for x <= 0, and D_Q >= -B_Q >= -B;
(ii) for x >= 1, f(x) >= min(p, ceil(x/2) + 1) >= 2; (iii) for all x >= -B,
f(x) >= min(p, h(x)), h(x) := min(x + 1, (x + B + 1)/2) = (x + B + 1)/2 - max(0, B - 1 - x)/2.
Uncapped case (every d_j <= 2p - 2).  Partition of w~ into its single runs, cyclic order.
(a) With N := {j : d_j <= 0} and D_N := sum_N d_j >= -B >= -(k~ - 1):
sum_j f(d_j) >= sum_{j notin N} (d_j/2 + 1) + sum_N (d_j + 1) = D/2 + D_N/2 + k~ =
p + (k~ + D_N)/2 >= p + 1/2, hence >= p + 1 (an integer).
(b) lower inequality: for three intervals X, Y, Z partitioning the cycle (D_X + D_Y + D_Z =
D >= p): if no lambda is capped, the sum is >= (D + 3B + 3)/2 - (1/2) sum max(0, B - 1 - D_Q);
with s small parts (D_Q <= B - 2) this is >= (D + 3B + 3)/2, (D + B + 4)/2, (D + 5)/2, D + 3
for s = 0, 1, 2, 3 (using D_Q >= -B for one part, D_a + D_b >= -B for two, and
D_X + D_Y + D_Z = D for three), so >= 1; if one lambda equals p the other two are >= 2 - B
together (both truncated) or >= 1 - B + B, so the sum is >= p + 2 - B >= 3 (B <= p - 1).
upper inequality: the unions X u Y, Y u Z, Z u X have D-values summing to 2D; if none is capped
the sum is >= D + (3B + 3)/2 - (1/2) sum max(0, B - 1 - D_Q) >= min(D + (3B+3)/2,
D + (B + 4)/2, (3D + 5)/2, 2D + 3) >= p + 1 (two small unions cover the cycle, so their
D-values sum to D + D_common >= D - B); if one is capped (= p), let x, y be the D-values of
the other two unions, so x + y = D + D_common >= D - B >= 1 (in particular x, y are not both
negative).  If a second union is capped as well, the third term is >= 1 - B (f(z) = z + 1
>= 1 - B for -B <= z <= 0, f(z) >= 2 for z >= 1), so the three terms sum to
>= 2p + 1 - B >= p + 2 (B <= k~ - 1 <= p - 1).  Otherwise neither of the two is capped and
they contribute >= 1: if x, y >= 0 each is >= 1 by (i), (ii); if x < 0 then y > 0,
f(x) = x + 1 and f(y) = min(y + 1, floor((y + B)/2) + 1) >= min(y + 1, (y + B + 1)/2), so
f(x) + f(y) >= min(x + y + 2, ((x + y) + (x + B) + 3)/2) >= min(D - B + 2, (D - B + 3)/2) >= 1
(x >= -B).  So the sum is >= p + 1 in every case.  (c): for a single run j, if d_j <= 0
then D - d_j >= D >= p >= B + 1 and
f(d_j) + f(D - d_j) >= (1 - B) + min(p, B + 1) >= 2; symmetrically if D - d_j <= 0; else
both >= 2.  Lemma BC kills w~.
Capped case (some d_G >= 2p - 1).  The other k~ - 1 runs have sum of d <= D - (2p - 1) =
1 - k~, while their B-total is <= B = kappa <= k~ - 1; hence they contain no rho_1, contain
all B letters rho_{-1}, one each, kappa = B = k~ - 1, A_G = 2p - 1, B_G = 0.  So w~ is the type
(II) shape: in w the segment G is a cyclic interval of c rotation runs t_1, ..., t_c (only
rho_1, a_t <= p - 1 by (D0), so c >= 3), separated by even reflection runs E_1, ..., E_{c-1},
between odd runs O_0 and O_1, followed by kappa single-letter runs a_1, ..., a_kappa (each
rho_{-1}) separated by the odd runs O_1, ..., O_kappa, O_0.  Work in w with the parts, in cyclic
order, {t_1}, T := {t_2, ..., t_c}, {a_1}, ..., {a_kappa}.  With B = kappa (Lemma H; E+ = D_Q + B):
lambda({a_i}) = 0; lambda({t_1}) = min(r_1, floor((r_1 + kappa)/2) + 1) (boundaries O_0, E_1);
lambda(T) = min(p, floor((R' + kappa)/2) + 1), R' = 2p - 1 - r_1 in [p, 2p - 2] (boundaries
E_1, O_1); if lambda(T) = p the sum is >= p + 1, otherwise lambda({t_1}) = floor((r_1+kappa)/2)+1
(r_1 <= kappa would force lambda(T) >= p) and the sum is >= p + kappa + 1/2: (a) holds.
Step t = 2 (X = {t_1}, Y = T, Z = {a_1..a_kappa}, lambda(Z) = 1 - kappa): lower sum
>= p + 2 - kappa >= 1; upper: lambda(G) = min(p, 2p, floor((2p - 1 + kappa)/2) + 1) = p,
lambda(T u Z) = min(p, R' - kappa, floor(R'/2) + 1) (boundaries E_1, O_0) and
lambda(Z u {t_1}) = min(r_1 - kappa, floor(r_1/2) + 1) (boundaries O_1, E_1); the last two
sum to >= 1 (if the last is <= 0 it equals r_1 - kappa, and R' - kappa, floor(R'/2) + 1, p are
each >= kappa + 1 - r_1 since kappa <= p - 1).  Steps with Y = {a_i}, 1 <= i <= kappa - 1
(X = G u {a_1..a_{i-1}}, Z = {a_{i+1}..a_kappa}): lambda(X) = lambda(X u Y) = lambda(Z u X) = p,
lambda(Z) = i - kappa + 1, lambda(Y u Z) = i - kappa, so the lower sum is p + i - kappa + 1 >= 1
and the upper sum 2p + i - kappa >= p + 1.  (c): lambda({a_kappa}) + lambda(co a_kappa) = 0 + p.
Lemma BC kills w.  []
Controls: all inherited kappa = B >= 2 run data with k <= p at p = 5 (27,847: 27,838 by the
single-run chain of w~, 9 capped, all 9 killed by the capped chain) and p = 7 (30,970,359:
30,968,784 + 1,575 capped, all killed); random odd-reflection kappa = B data with o_F <= p,
1,500 each at p = 11, 13, 17, 19, 23: the single-run chain works whenever uncapped (2 capped
samples at p = 11).  (Session checks `check_kappaB`, `capped_chain`.)

## Change log r2 (2026-10-17T11:43:46-07:00; answers Codex review v1, three MINOR findings)

1. (review item at input line 31) Sec. 1 Remark now states conditional preservation: (E), (V),
   (Pairs) persist when assumed; k(w~) = o_F <= p needs the input bound k <= p or o_F <= p.
   Every theorem that uses Lemma OR (K1, K1', S1'/A1' consequence, KB) assumes its bound.
2. (input line 202) Lemma A1': coloured-pattern connectivity proved by the vacancy
   construction (each labelled cut moved to the next original cut position; colours swap,
   giving P^c; each elementary move changes R_P by one r_u <= 2p - k).
3. (input line 239) Theorem KB, uncapped case, (b) upper inequality: a second capped union is
   handled explicitly (with the third term >= 1 - B the sum is >= 2p + 1 - B >= p + 2); the
   uncapped computation covers the remaining case.
No statement changed.  Sec. 4 is left as reviewed; current ownership of the open range:
MIX_low (o_F <= p) OlsonParity (mixdef-low/), MIX_high (o_F >= p+1) OlsonRunCount.
