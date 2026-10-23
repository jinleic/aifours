# MIX_low after MIX-R: Lemma W (B >= g+1), Lemma B1, Theorem A, Lemma G1, KS, AC, ZP, C and the residual

Owner OlsonParity2 (task from Main, slot math-2).  Version r3, written after host clock
2026-10-17T17:46 PDT.  r3 answers the reviews of v2 (sha256 0df17ff8...4a40, kept unchanged):
Codex ACCEPT, no findings (review/olson-rstar-codex-review-v1.note.md, sha 41fa3541...); Claude
ACCEPT-WITH-FIXES, six MINOR findings (review/olson-rstar-claude-review-v1.note.md, sha 8e1034fe...6b),
all applied and marked [r3 fix N]; r3 also ADDS Lemma ZP and Lemma C (Sec. 6, new, unreviewed [W]) and the
smaller residual R4.  Change log at the end.
Status: Sec. 1-6 written proofs [W]; v2 parts reviewed (Codex ACCEPT; Claude ACCEPT-WITH-FIXES), r3
additions unreviewed.  Sec. 7: the residual of these arguments, with finite evidence [F].  This file claims
MIX_low(5) (Remark in Sec. 6) and nothing else of that kind: no MIX_low(p) for p >= 7, no PAR(p), RUNS(p),
INV, INV* or ordered Olson.

Imports (exact):
* proof-MIX-low-partial-r2.md (this directory; r1 reviewed ACCEPT-WITH-FIXES, r2 = fixes applied,
  sha256 adf8cb70...6a22): setting, Lemma S (Sec. 1), Lemma K and its Corollary (Sec. 2), the review
  fixes 2 and 3 (Sec. 3, 6), Theorem MIX-R (Sec. 5) and the definition of R* (Sec. 6).
* Through r2: Lemma H (../../proof-PAR-K0.md Sec. 1; [r3 fix 5] reviewed in review/olson-parity-k0-kplus-codex-review-v1
  (ACCEPT on proof-PAR-K0.md: "the corrected empty/full residue condition and every proper-pattern half-window
  formula are correct"); the status line at proof-PAR-K0.md:4 predates that review), Lemma M0 (normalisation,
  ../../../inverse-run-count/proof-RUNS.md Sec. 12, [W], not independently reviewed).
No use of RUNS(p), PAR(p) or MIX_low(p).

## 0. Setting and notation

v: an RGR word of length 4p-2 (p >= 5 prime), all k reflection runs odd, k <= p, A >= B >= 1,
B < kappa <= k-1, g := kappa - B >= 1, every rotation run pure aligned (d >= 1), pure anti (d = -c <= -1)
or a (1,1)-pair (d = 0); A <= 2p-1, hence 2g + B <= k-1 <= p-1; D := A - B = 2p - k + 2g.
s := k - 1 - 2g - B >= 0.  Suppose v avoids.  x: the interval-chain lifts of Lemma S (x_t = u_t mod p,
sum x_t = p); phi_t := d_t - x_t, bh_t := 2x_t - d_t = d_t - 2 phi_t (so bh_t = d_t mod 2),
sum_t bh_t = k - 2g, sum_t phi_t = p - k + 2g.  For a set P of runs: phi(P), BH(P), D_P are sums, m(P)
the number of maximal cyclic blocks, c(P) := phi(P) + m(P) (so Phi(P) = 2 c(P) in r2's notation).
Lemma S (r2 Sec. 1) in phi-form: for every proper cyclic interval Q,
  phi(Q) <= gam(D_Q),   gam(E) := max(E - p, g - 1, floor((E - B - 1)/2))
(x(Q) >= U_Q + 1 with U_Q = min(p-1, D_Q - g, floor((D_Q+B)/2)); D - 1 - floor((D+B)/2) = floor((D-B-1)/2)).

**Fact F.**  (a) Every run has d_t <= 2p - 2 (r2 Sec. 3, review fix 2).  (b) If d_t >= 2g + B + 1 then
bh_t >= 2.  (c) If d_t <= 2g + B then phi_t <= g - 1.  (d) If 2g + B - 1 <= d_t <= 2p - B - 1 then
bh_t >= B + 1.
Proof.  Singleton intervals {t} are proper (k >= 2), so phi_t <= gam(d_t) and bh_t >= d_t - 2 gam(d_t)
= min(2p - d_t, d_t - 2g + 2, d_t - 2 floor((d_t - B - 1)/2)), and the last term is >= B + 1.  (b): the
three terms are >= 2 by (a), >= B + 3, >= B + 1.  (c): d_t - p <= 2g + B - p < 0 <= g - 1 and
floor((d_t - B - 1)/2) <= floor((2g - 1)/2) = g - 1.  (d): 2p - d_t >= B + 1, d_t - 2g + 2 >= B + 1.  []

Run classes.  cheap: phi_t >= 0 and bh_t <= 1.  free: phi_t >= 0 and bh_t <= 0.  filler: cheap with
bh_t = 1.  A filler is aligned (a pair has bh even; an anti with bh >= 1 has phi = (-c - bh)/2 < 0).
Every cheap run has d_t <= 2g + B (Fact F(b)), hence phi_t <= g - 1 (Fact F(c)).
Weight w_t := phi_t + 1; W(P) := sum_P w_t.  For an independent set P (no two runs of P cyclically
adjacent, P != [k]) one has m(P) = |P| and c(P) = W(P).

## 1. Lemma KL (kill lemma)

**Lemma KL.**  Let S be a proper nonempty set of runs with phi_t <= g - 1 for all t in S,
c(S) >= g + 1 and BH(S) <= B.  Then v has an identity 2p-subword.
Proof.  List S as: all t in S with bh_t <= 0 (any order), then the others (any order); P_i := first i
elements.  Adding one run t to a set changes m by -1, 0 or +1, so c changes by at most phi_t + 1 <= g;
c(P_0) = 0 and c(S) >= g + 1, so the shortest prefix P with c(P) >= g + 1 has g + 1 <= c(P) <= 2g.
BH(P) <= B: if P contains only runs with bh <= 0 then BH(P) <= 0; otherwise P contains all runs of S with
bh <= 0, and BH(P) = BH(S) - (sum of bh over S \ P) <= BH(S) <= B since every omitted run has bh >= 1.
D_P >= -B (only anti runs have negative d; [r3 fix 3] their total mass is B - n_P <= B).  P is proper and nonempty.  In r2's notation
Phi(P) = 2 c(P) lies in [2g + 2, 4g], so Lemma K (ii), (iii) hold and its Corollary gives (i), (iv), (v),
(vi): P kills (u_P in I(P)).  []

## 2. Lemma W (the case B >= g + 1)

**Lemma W.**  If B >= g + 1, v has an identity 2p-subword.  (No hypothesis R*.)
Proof.  Step 1: W(cheap) >= 2g + 1.  sum_t w_t = (p - k + 2g) + k = p + 2g.  A run that is not cheap
and has phi_t >= 0 has bh_t >= 2 and is aligned (pairs with bh >= 2 and antis with bh >= 1 have phi <= -1);
for such a run w_t = (d_t - bh_t)/2 + 1 <= d_t/2.  Runs with phi_t <= -1 have w_t <= 0.  Hence
W(cheap) >= p + 2g - (sum of d_t over aligned runs)/2 >= p + 2g - A/2 >= p + 2g - (2p - 1)/2 = 2g + 1/2,
and W(cheap) >= 2g + 1 as it is an integer.
Step 2: an independent set U of cheap runs with W(U) >= g + 1.  If not every run is cheap, the cheap
runs form paths separated by non-cheap runs; in each path take the positions of one parity, the one of
larger weight; the union U is independent and W(U) >= W(cheap)/2 > g, so W(U) >= g + 1.  If every run is
cheap, W(cheap) = p + 2g; delete one run t0, take the heavier parity class of the path [k] \ {t0}
(independent in the cycle since k >= 2g + B + 1 >= 4): its weight is >= (p + 2g - w_t0)/2 >= (p + g)/2
>= g + 1 (w_t0 <= g, p >= k >= g + 2).
Step 3: order U by decreasing weight and let S be the shortest prefix with W(S) >= g + 1; every weight is
>= 1, so |S| <= g + 1.  S is independent, proper and nonempty; c(S) = W(S) >= g + 1; phi <= g - 1 on S
(cheap); BH(S) <= #{fillers in S} <= |S| <= g + 1 <= B.  Lemma KL.  []

## 3. Lemma B1 (a run of mass d_T >= 2p - B)

**Lemma B1.**  If some run T has d_T >= 2p - B, v has an identity 2p-subword.  (No hypothesis R*.)
Proof.  T is aligned.  a' := A - d_T (the A-mass outside T) <= 2p - 1 - d_T <= B - 1, and a' >= 1 (else
the other k - 1 runs are antis, B >= k - 1 >= 2g + B).  For t != T: d_t <= a' <= B - 1, so phi_t <= g - 1
(Fact F(c)).  gam(d_T) = d_T - p (d_T - p >= p - B >= 2g + 1 > g - 1 and d_T >= 2p - B - 1 gives
d_T - p >= (d_T - B - 1)/2), so phi_T <= d_T - p and, with R' := [k] \ {T},
  phi(R') = (p - k + 2g) - phi_T >= D - d_T = D_{R'} = a' - B.
Hence W(R') = phi(R') + (k - 1) >= a' - B + 2g + B = 2g + a' >= 2g + 1.  Number R' as the path
t_1, ..., t_{k-1} (t_1 after T); each parity class of the path is independent in the cycle (t_1 and
t_{k-1} are not adjacent as k >= 2g + B + 1 >= 4); the two classes have total weight >= 2g + 1, so one
of them, X, has W(X) >= g + 1.  S := {t in X : phi_t >= 0} is independent, proper, nonempty and
c(S) = W(S) >= W(X) >= g + 1 (only weights <= 0 were dropped).  BH(S) = sum_S (d_t - 2 phi_t) <= sum_S d_t
<= (mass of the aligned runs other than T) <= a' <= B - 1.  Lemma KL.  []

## 4. Theorem A (R* with a run of bh_T >= B + 1)

Notation of r2 Sec. 3: Z0 = {bh <= 0}, Y = complement, m = m(Z0), exc = sum_Y (bh - 1),
a_Z = sum_{Z0} (d - 1), S_Z = sum over aligned t in Z0 of (d_t - 1) >= 0,
L_Z = sum over anti t in Z0 of (1 + c_t) + #pairs in Z0, so a_Z = S_Z - L_Z.  R* (r2 Sec. 6):
  (R1) a_Z + exc + 2m <= 0   (Phi(Z0) <= 2g + 1, and Phi is even),   (R2) |Y_al| + a_Z <= 2.
B_Z := (anti mass in Z0) + #pairs in Z0, B_Y := B - B_Z; L_Z = #anti_{Z0} + B_Z.

**Theorem A.**  In R*, if some run T has bh_T >= B + 1, v has an identity 2p-subword.
Proof.  T is not cheap.  Classify the runs t != T that are not cheap: (i) aligned, bh >= 2; (ii) pair,
bh >= 1 (then bh >= 2); (iii) anti in Y; (iv) anti in Z0 with phi <= -1 (then bh >= 2 - c, so c >= 2).
exc >= (bh_T - 1) + #(i) + #(ii), and (R1) gives exc <= L_Z - S_Z - 2m = #anti_{Z0} + B_Z - S_Z - 2m, so
  #(i) + #(ii) <= #anti_{Z0} + B_Z - S_Z - 2m - bh_T + 1.
#(iii) <= B_Y (each anti of Y has c >= 1) and #anti_{Z0} + #(iv) <= (anti mass in Z0) <= B_Z ((iv) has
c >= 2).  With k - 1 = 2g + B + s:
  #cheap = (k - 1) - [#(i) + #(ii) + #(iii) + #(iv)] >= (2g + B + s) - (2 B_Z + B_Y) + S_Z + 2m + bh_T - 1
         = 2g + s + 2m + S_Z + bh_T - 1 - B_Z >= 2g + s + 2m + S_Z + (bh_T - 1 - B) >= 2g + 2.
(The classes (i)-(iv) are all non-cheap runs other than T: an aligned run or a pair with bh <= 1 has
phi >= 0, and an anti run is cheap iff phi >= 0.)
BH(cheap) <= #fillers <= |Y_al \ {T}|, and (R2) gives |Y_al| <= 2 - a_Z = 2 - S_Z + L_Z <= 2 + 2 B_Z
= 2 + 2B - 2B_Y; if T is aligned this gives BH(cheap) <= 2B + 1, otherwise B_Y >= 1 and |Y_al| <= 2B
([r3 fix 4] T is then a pair or an anti run; bh_T >= 2 puts it in Y, where it contributes >= 1 to B_Y).
The cheap runs lie on the path [k] \ {T}; in each maximal block of consecutive cheap runs put alternate
runs into U and V, choosing the start so that ||U| - |V|| <= 1 overall.  U, V are independent (blocks are
separated by non-cheap runs, the path ends are adjacent only to T, k >= 4), |U|, |V| >= g + 1, so
c(U) = W(U) >= g + 1, c(V) >= g + 1, and BH(U) + BH(V) = BH(cheap) <= 2B + 1 gives min <= B.  Cheap runs
have phi <= g - 1.  Lemma KL for the one with BH <= B.  []

## 5. Lemma G1 (g = 1 without large runs)

**Lemma G1.**  (R1) fails when g = 1 and every aligned run has d_t <= B + 2.  So no configuration of R*
has g = 1 and all d_t <= 2g + B - 2.
Proof.  By Fact F(c) every aligned run has phi <= g - 1 = 0, so no aligned run is a defect (bh <= 0 would
give phi >= d/2 > 0): S_Z = 0, every aligned run is in Y, and d_t = bh_t + 2 phi_t <= bh_t.  Hence
A = (aligned mass) + n_P <= sum_{Y_al} bh + n_P = |Y_al| + exc_al + n_P <= (k - n_A - n_P) + exc + n_P.
(R1) gives exc <= L_Z - 2m, so A <= k - n_A + L_Z - 2m.  But A = 2p - k + 2 + B >= k + 2 + B, so
L_Z >= B + 2 + n_A + 2m, while L_Z <= n_A + B (each anti in Z0 gives 1 + c, each pair 1).  []

## 6. Assembly of what is proved (and of what remains)

By Theorem MIX-R (r2 Sec. 5), Lemma W, Lemma B1 and Theorem A, [r3 fix 2] no normalized MIX_low avoider has
lift data outside
  R** := R* intersect {B <= g} intersect {no run with bh_t >= B + 1} intersect {no run with d_t >= 2p - B}.
By Fact F(d), in R** every run has d_t <= 2g + B - 2 (so phi_t <= g - 1 for all t), and by Lemma G1, g >= 2.
**Lemma KS (count form of the split; inside R*).**  Let alpha be the number of free anti runs (anti,
bh <= 0, phi >= 0), Z0+ the set of free runs, and suppose not every run is cheap.  If
  2 phi(Z0+) + alpha <= 2g + s - 1 + S_Z,
then v has an identity 2p-subword.
Proof.  Runs of Z0 that are not free are antis with phi <= -1 (beta of them; aligned defects have
phi >= d/2 > 0 and pairs in Z0 have phi = -bh/2 >= 0).  Let N be the runs of Y that are not fillers
(nu := |N|; N = aligned runs with bh >= 2, of number nu_al, plus anti/pair runs of Y, n_apY of them).  Then
#cheap = k - beta - nu.  Each run counted in nu_al contributes >= 1 to exc_al := sum over aligned runs of
Y of (bh - 1) = exc - exc_ap, so nu <= exc - exc_ap + n_apY.  Identities (r2 Lemma Phi): 2 phi(Z0) =
Phi(Z0) - 2m = 2g + a_Z + exc, a_Z = S_Z - L_Z, L_Z = alpha + beta + B_Z, k = 2g + B_Z + B_Y + s + 1.  So
#cheap >= k - beta - (2 phi(Z0) - 2g - a_Z - exc_ap) - n_apY
       = 4g + s + 1 + S_Z - alpha - 2 beta - 2 phi(Z0) + (B_Y - n_apY) + exc_ap,
and phi(Z0) <= phi(Z0+) - beta, B_Y >= n_apY, exc_ap >= 0 give
  #cheap >= 4g + s + 1 + S_Z - alpha - 2 phi(Z0+) >= 2g + 2   (by the hypothesis).
BH(cheap) <= 2B + 1: BH(cheap) <= #fillers <= |Y_al| <= 2 - a_Z = 2 - S_Z + L_Z (R2) and L_Z <= 2 B_Z;
if B_Y >= 1 or S_Z >= 1 or L_Z <= 2B_Z - 1 this is <= 2B + 1; otherwise every unit of B sits in an anti
run of Z0 with c = 1, such a run has odd bh <= 0, hence bh <= -1, it is cheap, there is at least one
(B >= 1), and BH(cheap) <= #fillers - 1 <= 2B + 1.  The cheap runs lie on paths (not every run is cheap);
the balanced alternating split of Theorem A gives independent U, V with |U|, |V| >= g + 1 and
BH(U) + BH(V) <= 2B + 1; Lemma KL for the one with BH <= B.  []

**Lemma AC (every run cheap; inside R*).**  If every run is cheap, v has an identity 2p-subword.
Proof.  Then Y consists of fillers, so h := |Y| satisfies h - delta = sum bh = k - 2g with
delta = -BH(Z0) >= 0, i.e. h >= k - 2g = s + 1 + B, and (R2) gives h <= |Y_al| <= 2 - S_Z + L_Z <= 2 + 2B;
hence s <= B + 1.  All weights are >= 1 and all phi <= g - 1 (cheap).  If B + s >= 2: delete one filler
t0 (there are h >= 2) and split the path [k] \ {t0} into its two parity classes U, V (independent in the
cycle, k >= 4); |U|, |V| >= floor((k-1)/2) = floor((2g + B + s)/2) >= g + 1, so c(U), c(V) >= g + 1, and
BH(U) + BH(V) = (k - 2g) - 1 = s + B <= 2B + 1.  If B + s <= 1, then B = 1, s = 0 and k = 2g + 2 is even;
the two parity classes O, E of the cycle are independent, |O| = |E| = g + 1, BH(O) + BH(E) = k - 2g = 2.
In both cases one class has BH <= B; Lemma KL.  []

[r3 fix 1] The normalized interval-feasible data not handled by Theorem MIX-R and Lemmas W, B1, A, KS, AC are
exactly those in
  R*** := R** intersect {not every run is cheap} intersect {2 phi(Z0+) + alpha >= 2g + s + S_Z};
hence every MIX_low avoider, if one exists, has lift data in R***.  R*** is cut out by necessary conditions
only (interval windows, (R1), (R2), the inequalities above); membership in R*** implies neither
realisability by an RGR word, nor survival of the non-interval windows u_P notin I(P), nor an
ordered-product counterexample.
**Corollary.**  If no interval-feasible normalized MIX_low data at p lie in R***, then MIX_low(p).

**Lemma ZP (new in r3).**  If c(Z0+) >= g + 1 (Z0+ = the free runs), v has an identity 2p-subword.
Proof.  Z0+ is nonempty (c > 0) and proper (Y is nonempty, as sum bh = k - 2g > 0); free runs are cheap, so
phi <= g - 1 on Z0+; BH(Z0+) <= 0 <= B.  Lemma KL with S = Z0+.  []

**Lemma C (new in r3).**  Suppose every run has phi_t <= g - 1 except possibly t0 (e.g. in R**, where all
d_t <= 2g + B - 2), phi_{t0} <= p - k + g, and bh_{t0} >= s + 1 = k - 2g - B.  Then v has an identity
2p-subword.
Proof.  S := [k] \ {t0} is a proper cyclic interval, m(S) = 1, c(S) = (p - k + 2g) - phi_{t0} + 1 >= g + 1,
BH(S) = (k - 2g) - bh_{t0} <= B, phi <= g - 1 on S.  Lemma KL.  []

Consequently (all r3, [W]) every MIX_low avoider has lift data in
  R4 := R*** intersect {c(Z0+) <= g} intersect {every bh_t <= s},
and in R4: s >= 1 (some bh_t >= 1), alpha >= 2 m(Z0+) + s + S_Z (from c(Z0+) <= g and the R*** inequality),
so s <= alpha - 2 <= B - 2 <= g - 2, and exc >= alpha + beta + pi_0 + s, (anti mass in Z0) >= s + S_Z + 2m
(exc = |Z0| + delta - 2g and delta >= 2 phi(Z0+) + (anti mass of free antis) - S_Z - n_d >= 2g + s - n_d;
then (R1)), where beta = #(iv)-antis, pi_0 = #pairs in Z0, n_d = #aligned runs in Z0.
**Corollary'.**  If no interval-feasible normalized MIX_low data at p lie in R4, then MIX_low(p).

**Remark (MIX_low(5), from the written proofs alone; observed by the Claude review).**  At p = 5,
2g + B <= k - 1 <= 4 forces g = 1 and B <= 2.  B = 2 = g + 1: Lemma W.  B = 1: outside R*, MIX-R; in R* with some
bh_t >= 2 = B + 1, Theorem A; with some d_t >= 2p - B = 9, Lemma B1 (impossible anyway); otherwise, by Fact F(d),
every d_t <= 2g + B - 2 = 1 and Lemma G1 contradicts (R1).  So MIX_low(5) holds [W].

## 7. The residual (open) and evidence [F]

[r3 fix 6a] No computer-assisted MIX_low(p) is claimed in this file; the census below is evidence only.  (A
separate assembly, proof-PAR-assembly-r1.md, records the consequence of the census as a [W+F] statement that
is explicitly conditional on the unreviewed census programs.)

R**: normalized MIX_low data with interval-feasible lifts, (R1), (R2), B <= g, g >= 2, all
d_t <= 2g + B - 2, all bh_t <= B; R*** as in Sec. 6 (adds: some run not cheap, and
2 phi(Z0+) + alpha >= 2g + s + S_Z; by (R1) this forces alpha + sum over (iv)-antis of 2|phi| >= 2m + s + S_Z).
Finite-exact (c2/README.md; code rstar_census*.cpp, lemma_replay*.cpp; all interval-feasible (d, phi),
rotation-canonical; aids only, never hypotheses):
* p = 5: no interval-feasible configuration at all; p = 7: 15; p = 11: 211,911; p = 13: 48,094,987.
  R* sizes 0 / 1 / 847 / 29,577; R* intersect {B <= g} is EMPTY at p = 7, 11, 13.
* p = 17, complete for B <= g (rstar_census21, DFS pruned only by necessary conditions of R*; [r3 fix 6b]
  rstar_census21.cpp lines 200-208: after placing runs 0..t, with zphi = phi of the prefix runs in Z0, zbl =
  the number of LINEAR blocks of Z0 in the prefix, nfirst = [run 0 in Z0], nB = the unused B budget, the branch
  is cut iff zphi + zbl - nfirst - floor(nB/2) > g; this is sound for the CYCLIC count m because the final
  cyclic m is >= zbl - nfirst (only the first and the last linear blocks can merge, and only if run 0 is in Z0;
  later runs never merge earlier prefix blocks), and future Z0 runs add phi >= -c/2 per anti (bh <= 0),
  >= 0 per pair, >= 1 per aligned run, so the final phi(Z0) >= zphi - floor(nB/2) (an integer); a cut branch has
  phi(Z0) + m >= g + 1, i.e. Phi(Z0) >= 2g + 2, so (R1) fails.  The second cut, yal_az - 2 nB > 2, is sound
  because each future unit of B lowers |Y_al| + a_Z by at most 2 (anti: -(c + 1) >= -2c; pair: -1) and future
  aligned runs do not lower it; all k <= 17, all (g, B) with B <= g):
  R* intersect {B <= g} has exactly 150 configurations, all at (k, g, B) = (16, 4, 4), all with a run of
  bh >= B + 1 (Theorem A), and the Theorem A construction kills all 150 (exact window test).  So R** is
  empty at p = 7, 11, 13, 17.
* Exact replay (lemma_replay.cpp, lemma_replay2.cpp; each construction of Sec. 1-6 is executed and its
  KL prefix is checked with the exact mod-p window test of Lemma H):
  p = 11: W 207,206 / B1 8,875 / A 847 / KS 752 / AC 0; p = 13: W 47,256,945 / B1 715,752 / A 29,577 /
  KS 22,984 / AC 0; 0 failures, KL hypotheses never violated, W(cheap) >= 2g + 1 on every configuration,
  Lemma G1 never violated.  Mutation (windows shrunk by one): p = 11 116,744 / 7,426 / 845 / 750 and
  p = 13 12,392,540 / 543,659 / 28,740 / 22,245 replays rejected.
* Singleton-only relaxation (only |Q| = 1 interval bounds; research aid): R* intersect {B <= g} is not empty
  at p = 11 (13,535 relaxed configurations; 12 with intervals of length <= 2 or >= k-2; 0 with length <= 3
  or >= k-3), but its intersection with R*** is empty at p = 11 (also with [r3 fix 6c] the restriction
  'every d_t <= 2g + B - 2', which holds throughout R** by Fact F(d): 12,030 relaxed R* configurations,
  R*** = 0).  At p = 13 the relaxed searches stopped at their CPU limits (UNKNOWN).
* Independent cross-check of the census DFS (xcheck_run.py, xcheck_pos.py: theta-domain enumeration with
  Lemma GR's Ach from ../../../code/gr_window.py, unchanged, on an explicit realisation of each d-vector,
  versus the phi-domain Lemma S system): p = 7 all 15; p = 11 5,000 sampled d-vectors with lifts (18,987
  solutions) and 20,000 random d-vectors; p = 13 2,000 sampled R* d-vectors (72,913 solutions) and 20,000
  random d-vectors: 0 mismatches.

## Change log r3 (2026-10-17T17:46 PDT; answers the Claude review v1, six MINOR findings; Codex: none)

1. (L163-165) Residual and Corollary reworded: R*** is the residual of these arguments; Corollary hypothesis is
   about interval-feasible normalized data, not avoiders.
2. (L128) 'no normalized MIX_low avoider has lift data outside R**'.
3. (L52) anti mass B - n_P <= B.
4. (L109) justification of B_Y >= 1 when T is a pair or anti run.
5. (L13) Lemma H's review cited (Codex ACCEPT on proof-PAR-K0.md); path of proof-RUNS.md given.
6. (L181-191) (a) no computer-assisted MIX_low claimed here; (b) soundness of the p = 17 pruning for the cyclic
   block count, with code lines; (c) 'B2 restriction' defined.
New in r3 (unreviewed): Lemma ZP, Lemma C, residual R4 and its consequences, Remark MIX_low(5).
