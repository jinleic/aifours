# RUNS(p): written lemmas, reduction, and status (task OlsonRunCount)

Written after host clock 2026-10-17T03:42:56-07:00.  Representation frozen in
README.md Sec. 2 (Lemma HW).  Evidence labels: [W] written proof here (not yet
independently reviewed); [F] finite-exact computation (aid only, never a hypothesis).
Nothing below assumes PAR(p) (parity of runs); even runs are allowed throughout
(they enter only through h(P) / beta(P)).

## 0. Setting

p prime >= 5.  RGR word of length N, F, R >= 1, x normalised to 1, cyclic runs
R_1 S_1 ... R_k S_k; a_t, b_t = numbers of rho_1, rho_{-1} in R_t, r_t = a_t + b_t,
d_t = a_t - b_t; S_j = sigma_{y_j}^{l_j}; A = sum a_t, B = sum b_t, R = A + B, D = A - B,
F = sum l_j, H = sum floor(l_j/2), o = #{j : l_j odd}, kappa := p - 1 - H.
phi_t = (y_{t-1} - y_t)/2 in Z_p.  For P subset [k]: m = m(P) (number of maximal
cyclic intervals; P proper nonempty => m >= 1), beta(P) = number of EVEN reflection
runs among the 2m boundary runs of P, h(P) = H - beta(P), E+(P) = sum_P a + sum_{P^c} b,
E- = R - E+, g_P(E) = min(p - m, E + m + h(P) - p, floor(E/2)),
I(P) = [-g_P(E-), g_P(E+)], W(P) = I(P) mod p.
Lemma HW (README Sec. 2): the word avoids (no identity 2p-subword) iff
phi(P) := sum_{t in P} phi_t notin W(P) for every P.  "Full window": |I(P)| >= p.

## 1. Lemma FW (full window from p+1 boundaries) [W]

If some P has m(P) = (p+1)/2 and E+(P), E-(P) >= p-1, the word (any length) has an
identity 2p-subword.
Proof.  p - m = (p-1)/2; for E >= p-1: floor(E/2) >= (p-1)/2 and
E + m + h - p >= (p-1)/2 + h >= (p-1)/2; so g_P(E+-) = (p-1)/2 and I(P) =
[-(p-1)/2, (p-1)/2] has p elements, hence W(P) = Z_p contains phi(P).  (Explicit
selection: one reflection from each of the p+1 boundary runs and p-1 rotations, A+ of
them effectively positive, A+ = 0..p-1; t = 2A+ - (p-1) runs through p consecutive even
integers, so one is = tau(z_P) mod p; Lemma GR.)  []

## 2. Theorem ALT (fully alternating words) [W]

Every RGR word of length 4p-2 with k = 2p-1 (all 2k runs single letters) has an
identity 2p-subword.  (No inherited hypothesis needed.)
Proof.  All runs are single letters, d_t = +-1, R = 2p-1.  A pattern with m = (p+1)/2
is a choice of p+1 "particles" (boundary reflection runs) among the 2p-1 reflection
runs, the 2m arcs between consecutive particles being alternately in P and in P^c.
Put Dl(P) = E+(P) - E-(P) = sum_t z_t d_t (z_t = +1 on P, -1 on P^c); it is odd.
Moving one particle by one position (onto a free neighbouring reflection run) moves
one run t between P and P^c and changes Dl by -2 z_t d_t = +-2.
Path from P_0 to P_0^c: lift positions x_1 < ... < x_{p+1} < x_1 + k.  There are
k - (p+1) = p-2 >= 3 free runs, so some gap x_{i*+1} - x_{i*} >= 2.  Move particle i*
forward to x_{i*+1} - 1; then particles i*-1, i*-2, ..., i*+1 (cyclically backwards)
each forward to the original position of the next particle (always vacated already);
finally particle i* one more step to x_{i*+1}.  Particles never collide, so every
intermediate pattern has exactly p+1 boundaries; at the end particle i sits at x_{i+1},
and since the arc labels travel with the particles, the final pattern is P_0^c.
Dl(P_0^c) = -Dl(P_0) and Dl moves in steps +-2 through odd values, so some pattern on the
path has Dl = +-1, i.e. {E+, E-} = {p-1, p}.  Lemma FW applies.  []
[F] consistent: inherited k = 2p-1 data at p = 5 (256 split classes) and p = 7 all have
a full window (out/ logs of hwsearch).

## 3. Normalisation and the zero certificate [W]

The automorphism rho_v -> rho_{-v}, sigma_v -> sigma_{-v} maps (a, b, phi) to (b, a, -phi)
and preserves avoidance, so WLOG A >= B.  For P = empty (m = 0, h = H, E+ = B, E- = A):
g_0(E) = min(p, E - kappa - 1, floor(E/2)); 0 in I(empty) iff A, B >= kappa + 1.  Hence an
avoider has B <= kappa, so g_0(B) = B - kappa - 1 <= -1.  Consequently
   D = R - 2B >= R - 2 kappa = 2p - o >= 2p - k.                         (3.1)
(Also an avoider has g_0(A) <= p-1: otherwise -p in I(empty).)

## 4. Lemma TL (telescoping lifts) [W]

Assume the word avoids, A >= B, no window is full, and o <= 2p-2 (if o >= 2p-1 then
k = 2p-1 and Theorem ALT applies).  For a pattern Q with nonempty I(Q) = [lo, hi] put
lift(Q) := the unique integer in (hi, lo + p) congruent to phi(Q) (exists by avoidance,
unique as the window is nonempty and not full); for Q with empty window choose any
integer congruent to phi(Q).
(a) lift(empty) = 0 and lift([k]) = p.
(b) For any chain empty = P_0 < P_1 < ... < P_k = [k] (P_j = P_{j-1} + {t_j}) put
x_{t_j} := lift(P_j) - lift(P_{j-1}).  Then x_t = phi_t (mod p), sum_t x_t = p, and the
lifted brackets bh_t := 2x_t - d_t satisfy bh_t = d_t (mod 2), bh_t = beta_t (mod p)
(beta_t = 2 phi_t - d_t the bracket), and
   sum_t bh_t = 2p - D <= k        (by (3.1)).                            (4.1)
Proof of (a).  I(empty) = [-g_0(A), B - kappa - 1].  It is nonempty: g_0(A) >= kappa + 1 - B
because A - kappa - 1 - (kappa + 1 - B) = R - 2kappa - 2 = 2p - 2 - o >= 0 and
A - (2kappa + 2 - 2B) = B + 2p - 2 - o >= 0 (so floor(A/2) >= kappa + 1 - B), and p >= kappa + 1 - B.
The gap (B - kappa - 1, p - g_0(A)) contains 0.  I([k]) (m = 0, E+ = A, E- = B) is
[kappa + 1 - B, g_0(A)], nonempty by the same computation; its gap (g_0(A), p + kappa + 1 - B)
contains p, and phi([k]) = 0 = p (mod p).  (b) telescopes.  []
Remark.  No "no-jump" hypothesis is used; the lifts x_t depend on the chain.  Every
kill test below is a congruence test (Lemma KW), valid for any integer lifts.

## 5. Lemma KW (kill test in deficiency coordinates) [W]

Let x_t be any integers with x_t = phi_t (mod p), bh_t = 2x_t - d_t, e_t := 1 - bh_t,
and for P proper nonempty: e(P) = sum_P e_t, D_P = sum_P d_t, tau(P) = |P| - D_P,
epsP = [E+(P) odd], epsM = [E-(P) odd].  If
   max( tau(P) + 2(kappa - B) + 2 + 2beta - 2m,  |P| - B + epsP,  |P| + D_P - 2p + 2m )
      <=  e(P)  <=
   min( |P| + A - epsM,  |P| + 2A - D_P - 2kappa - 2 + 2m - 2beta,  |P| + 2p - 2m + D_P ),
then X_P := sum_P x_t lies in I(P), so phi(P) in W(P) and the word does NOT avoid.
Proof.  X_P = (D_P + sum_P bh_t)/2 = (D_P + |P| - e(P))/2.  The three upper bounds
X_P <= p - m, X_P <= E+ + m + h - p, X_P <= floor(E+/2) are, after substituting
E+ = A_P + B - B_P, h = p - 1 - kappa - beta, 2 floor(E+/2) = E+ - epsP, exactly the
three left inequalities; the three lower bounds -X_P <= g_P(E-) give the three right
ones.  []  ([F] check_killform.py: 120000 random (data, lifts, P), 0 mismatches.)

## 6. Theorem ND (the no-defect case) [W]

Assume the hypotheses of Lemma TL (inherited word) and fix a chain.  If bh_t >= 1 for
every t, then by (4.1) bh_t = 1 for all t, k = 2p - D, and equality holds in (3.1):
B = kappa and o = k (all reflection runs odd, so beta(P) = 0 for every P); also
d_t = bh_t = 1 (mod 2), so every r_t is odd.  If moreover k >= p+1, the word does not avoid.
Consequence (reduction):
   RUNS(p)  <=  DEF_RUNS(p): for an inherited avoider with k >= p+1 (hypotheses of TL),
                some chain has all bh_t >= 1,
and (shared with PAR) DEF for all k would give k = 2p - D, all runs odd and all lifted
brackets 1 (the conjectured INV+ shape).

### 6.1 Proof of the kill in Theorem ND

Here e_t = 0 for all t, kappa = B, beta = 0, A - kappa = A - B = D = 2p - k, and
kappa = (R + o - 2p)/2 = (R + k - 2p)/2 >= 1 because R >= k >= p+1.
(i) Some run t has 1 <= d_t <= 2D + 1.  D >= 1 (k <= 2p-1), so some d_t >= 1.  If every
positive d_t were >= 2D + 3, then R >= r_t + (k - 1) >= 2D + 2 + k = 4p - k + 2, so
F = 4p - 2 - R <= k - 4 < k, impossible (every reflection run is nonempty).
(ii) P = {t} is killed (Lemma KW with e(P) = 0, |P| = m = 1, tau = 1 - d_t, D_P = d_t):
  left 1: 1 - d_t + 0 + 2 + 0 - 2 = 1 - d_t <= 0;
  left 2: 1 - kappa + epsP <= 0, where E+({t}) = a_t + B - b_t = d_t + kappa has the parity
          of 1 + kappa, so epsP = [kappa even] and kappa >= 1 + [kappa even] holds;
  left 3: 1 + d_t - 2p + 2 <= 0 since d_t <= a_t <= p-1 (D0);
  right 1: 0 <= 1 + A - epsM;   right 3: 0 <= 1 + 2p - 2 + d_t;
  right 2: 0 <= 1 + 2A - d_t - 2kappa - 2 + 2 = 1 + 2D - d_t by (i).  []

## 7. Status (precise)

Proved here ([W], unreviewed): Lemmas FW, TL, KW, Theorems ALT, ND, the reduction of
Sec. 6, Theorem S1 (Sec. 9), the Depth Lemma and Theorem C0-B (Sec. 10), and in Sec. 11-12:
Theorem C0-B' (no inherited hypotheses, any k, R <= 2p-2), Lemma A1 (R = 2p-1), the trivial
cut A >= 2p, Corollary B0, kappa = 0 via OlsonParity's Theorem K0, pair removal (M0) and
Corollary MNA.  Hence RUNS(p) holds for every inherited word with B = 0 (all k, all
reflection parities) and for every inherited word with kappa = 0.
Open: B >= 1 (Sec. 13 states the exact remaining lemma MIX_RUNS).  Evidence: Sec. 8.

## 8. Finite-exact evidence (aids only) [F]

Code (this directory): hw.py (HW decision + fresh raw DP), hwsearch.cpp (HW search over
run data), hwsingle.cpp, check_killform.py; outputs in out/.
* HW form vs fresh raw ordered-product DP: 1760 random RGR words (p = 5, 7, 11;
  lengths 4p-3..4p-1): 0 disagreements, 8 NO instances among them.
* RUNS at N = 4p-2, inherited, all a/b splits: p = 5 (k = 6..9) and p = 7 (k = 8..13,
  561,309,562 split classes): 0 avoiders (independent of ../code/).
* Every such datum with R >= 2p-2 has a full window; the no-full-window data are
  exactly R <= 2p-3 (p = 5, 7).
* Inherited avoiders at N = 4p-3 already have k <= p (p = 5 all splits; p = 7 constant
  runs); at N = 4p-4, k = p+1 occurs (p = 5: also p+2), e.g. p = 7: a = (1^8),
  l = (1^6, 2, 8), phi = (1^7, 0).
* Patterns with m <= 2 certify all k >= p+1 data at p = 7 (constant runs) and the sampled
  p = 11 data; single intervals do not.
* Chain lifts along intervals: in all sampled regime-R<=2p-3 data (p = 7 constant runs
  complete; p = 11, 13 samples, constant and mixed) the interval-feasible phi have
  sum x_t = p and the defect set Z = {bh_t <= 0} is killed by Lemma KW for constant runs;
  for mixed runs at p = 5 one aligned singleton must be added to Z.
* Theorem S1 replay (check_S1.py: follows the proof of Sec. 9 on every interval-feasible
  phi plus random phi, and checks every claimed kill with the window test): p = 7, 11, 13
  S1 data: 0 failures (greedy kills 14,789 + 10,313 phi); outside S1 (high kappa,
  constant runs, all l odd) the same greedy also killed all 29,327 + 14,982 sampled phi
  (observation only: the proof below needs R + 2k <= 4p - 3).
* B = 0 parts (Sec. 11): hwsearch_c0b.cpp, check_C0B_ineq.py, check_A1.py, hwsearch_c0a.cpp
  and fwminm.cpp (rho_1-only all-odd data with R in [2p-2, 3p-2]: every datum with k~ >= 3
  has a full window, p = 5, 7; the minimal m of a full window grows like (k - p + 1)/2).
  Non-inherited check of the B = 0 statement: hwsearch p = 7, b = 0, any reflection
  parities, no inherited filter, k = 8..13 (547,778 run data): 0 avoiders.
* B >= 1 (Sec. 13): inherited, all splits, p = 5: no avoider with B >= 1 and A <= 2p-2 for
  any k (hwsearch_mixa); inherited with A = 2p-1, B >= 1: every datum has a full window
  (p = 5 k = 3..8, 25,406 data; p = 7 k = 6..12, 20,666,249 data; hwsearch_mixa1); FW
  patterns alone fail at k = p+1, p+2 (fa_minm.cpp).

## 9. Theorem S1 [W]

**Theorem S1.**  Let p >= 5 and let w' be an inherited RGR word of length 4p-2 with
k >= p+1, all rotation letters equal (after normalisation all are rho_1, i.e. b_t = 0),
all reflection runs of odd length, and R + 2k <= 4p - 3.  Then w' has an identity
2p-subword.

Notation.  Here d_t = r_t, A = R, B = 0, o = k, beta(P) = 0 and h(P) = H for all P,
kappa = p - 1 - H = (R + k - 2p)/2, so R + k >= 2p + 2 gives kappa >= 1, and the hypothesis
reads 4kappa + 3 <= R.  Also R <= 4p - 3 - 2k <= 2p - 5, so floor(E/2) <= p - 3 for every
E <= R and, for m = 1 (resp. m = 0),
   g_1(E) = min(E - kappa, floor(E/2)),   g_0(E) = min(E - kappa - 1, floor(E/2)).
Full windows: |I(P)| <= floor(E+/2) + floor(E-/2) + 1 <= R/2 + 1 < p, so none.  o = k <=
2p - 2.  Suppose w' avoids; we derive a contradiction.

Step 0 (chain).  Index runs 1..k cyclically and use the interval chain P_j = {1..j}.
For 1 <= j <= k-1 write rho_j = R_{P_j}, U_j = g_1(rho_j), L_j = g_1(R - rho_j).  Every
I(P_j) is nonempty: if both minima are attained by floor terms, U_j + L_j >= 0; if
U_j = rho_j - kappa, then U_j + L_j >= rho_j - kappa + (R - rho_j - 1)/2 =
(rho_j + 2p - k - 1)/2 > 0; symmetrically; if both are reflection terms, U_j + L_j =
R - 2kappa = 2p - k > 0.  Lemma TL gives lifts x_t with sum p, lifted brackets bh_t =
2x_t - r_t (bh_t = r_t mod 2), sum_t bh_t = 2p - R < k.

Step 1 (every defect is shallow).  For a single run t: U^t := g_1(r_t),
L^t := g_1(R - r_t) = floor((R - r_t)/2) (since R - r_t - kappa - floor((R - r_t)/2) >=
(2p - k - r_t)/2 > 0, as k + r_t <= R + 1 <= 2p - 4).  Claim: x_t >= -L^t for every t.
If t is added at step j = 1 or j = k this is immediate: x_t = lift({t}) lies in the gap
(U^t, p - L^t), resp. x_t = p - lift([k] - t) lies in (U^t, p - L^t) because
I([k] - t) = -I({t}).  For 2 <= j <= k-1, lift(P_j) >= U_j + 1 and lift(P_{j-1}) <=
p - L_{j-1} - 1, so x_t >= U_j + L_{j-1} - p + 2, and it suffices that
   S := U_j + L_{j-1} + L^t >= p - 1.                                          (9.1)
With rho_j = rho_{j-1} + r_t and R - kappa = (R - k + 2p)/2 >= p:
 (a) U_j, L_{j-1} floor terms: S >= (rho_j - 1 + R - rho_{j-1} - 1 + R - r_t - 1)/2 = R - 3/2,
     so S >= R - 1 >= p - 1;
 (b) U_j = rho_j - kappa, L_{j-1} floor: S >= rho_j - kappa + (2R - rho_{j-1} - r_t - 2)/2 =
     rho_j/2 + R - kappa - 1 >= p - 1/2;
 (c) U_j floor, L_{j-1} = R - rho_{j-1} - kappa: S >= (R - rho_{j-1})/2 + R - kappa - 1 >= p - 1;
 (d) both reflection terms: S >= R + r_t - 2kappa + (R - r_t - 1)/2 =
     2p - k + (R + r_t - 1)/2 >= p - 1  (as R + r_t + 1 >= k + 2 >= 2k - 2p + 2).
So x_t >= -L^t; avoidance of {t} (x_t = phi_t mod p) forbids x_t in [-L^t, U^t], hence
x_t >= U^t + 1.  If bh_t <= 0 then x_t <= r_t/2 < p - L^t, so x_t is in the base gap; and
U^t = floor(r_t/2) would give bh_t >= 1, so for a DEFECT U^t = r_t - kappa and
   delta_t := -bh_t <= 2kappa - 2 - r_t.                                       (9.2)

Step 2 (defects exist; the defect set has enough "capacity").  Z := {t : bh_t <= 0}.  If
Z is empty, Theorem ND gives a contradiction (k >= p+1).  Z is a proper subset (sum bh > 0).
For P subset of Z with m = m(P) components put rho_P, delta_P = -sum_P bh_t >= 0 and
Phi(P) := rho_P + 2m + delta_P.  With Y = [k] - Z (bh >= 1 there):
delta_Z = sum_Y bh - (2p - R) >= |Y| - (2p - R) = 2kappa - |Z|, so Phi(Z) >= |Z| + 2 + 2kappa
- |Z| = 2kappa + 2.

Step 3 (kill conditions for P subset of Z).  Lemma KW with B = 0, beta = 0, tau = |P| - rho_P,
e(P) = |P| + delta_P: P is killed if
 (K1) Phi(P) >= 2kappa + 2;                (K2) sum_P bh <= -[rho_P odd];
 (K3) rho_P + 2m <= 2p + delta_P (in particular if rho_P + 2m <= 2p);
 (K4) delta_P <= R - 1 (gives the right inequality 1 up to the parity term epsM);
 (K5) delta_P + rho_P - 2m <= 2R - 2kappa - 2;   (K6) delta_P + 2m - rho_P <= 2p.
(K2) always holds for P subset of Z: all terms are <= 0, and if rho_P is odd some r_t, hence
bh_t, is odd and <= -1.  (Right inequality 1 is e(P) <= |P| + R - epsM, i.e.
delta_P <= R - epsM; (K4) suffices.)

Step 4 (greedy).  Order Z by increasing depth delta_t and let P_i be the first i defects.
Adding one defect t changes Phi by r_t + delta_t + 2(change of m) <= r_t + delta_t + 2 <=
2kappa by (9.2).  Let i* be the least i with Phi(P_i) >= 2kappa + 2 (exists by Step 2).
i* >= 2, since Phi({t}) = r_t + 2 + delta_t <= 2kappa.  P := P_{i*}.  Then (K1) holds and
Phi(P) <= 2kappa + 1 + 2kappa = 4kappa + 1.  Moreover delta_{P_{i*-1}} = Phi(P_{i*-1}) -
rho - 2m <= 2kappa + 1 - (i* - 1) - 2 and delta_t <= 2kappa - 3, so
delta_P <= 4kappa - 3 - i* <= 4kappa - 5.
(K4): 4kappa - 5 <= R - 1 by 4kappa + 3 <= R.  (K3), (K5), (K6): each left side is at most
Phi(P) <= 4kappa + 1 <= R - 2 <= min(2p, 2R - 2kappa - 2).  So P is killed: phi(P) is in
W(P), contradicting avoidance.  []

Remarks.  (1) Only the hypothesis 4kappa + 3 <= R is used beyond inherited + constant
alphabet + odd reflection runs, and only in (K4).  (2) PAR is not used; even rotation runs
are allowed (they produce defects with even bh).  (3) Step 1 shows the chain lifts of
defects coincide with the singleton-gap lifts, independently of the chain start.

## 10. Depth Lemma and Theorem C0-B (constant alphabet, odd reflection runs, R <= 2p-3) [W]

Setting C0-B: inherited RGR word of length 4p-2, k >= p+1, all rotations rho_1 (b = 0),
all reflection runs odd, R <= 2p-3 (no hypothesis on kappa).  Notation of Sec. 9; for a
pattern Q with m intervals g_Q(E) = min(p - m, E + m - kappa - 1, floor(E/2)), and
   g_Q(E) = floor(E/2)  iff  floor(E/2) + m <= p  and  ceil(E/2) + m >= kappa + 1.    (10.1)
Steps 0-2 of Sec. 9 never used 4kappa + 3 <= R, so they hold here: chain lifts with
sum p, every defect is canonical (its lift is the representative x_t of phi_t in the gap
(U^t, p - L^t) of I({t})), U^t = r_t - kappa for defects, (9.2), L^t = floor((R - r_t)/2),
and Phi(Z) >= 2kappa + 2.  For any pattern Q with nonempty non-full window write
lift(Q) for the representative of phi(Q) in its gap (U_Q, p - L_Q), U_Q = g_Q(E+), L_Q = g_Q(E-).

**Split lemma.**  If Q1, Q2 are disjoint, Q = Q1 u Q2 is a proper pattern, all three windows
are nonempty and not full, and
   (A') U_{Q1} + U_{Q2} + L_Q >= -2,     (B') L_{Q1} + L_{Q2} + U_Q >= p - 2,
then (for an avoider) lift(Q) = lift(Q1) + lift(Q2).
Proof.  X := lift(Q1) + lift(Q2) = phi(Q) (mod p) lies in [U_{Q1} + U_{Q2} + 2,
2p - L_{Q1} - L_{Q2} - 2], so -L_Q <= X <= p + U_Q by (A'), (B').  Avoidance puts X outside
[-L_Q, U_Q] + pZ; the only integers of [-L_Q, p + U_Q] outside it are those of the gap
(U_Q, p - L_Q).  []

**Depth Lemma.**  In setting C0-B, if the word avoids, every defect t has
delta_t = -bh_t <= 2p - R - 2.
Proof.  Let m = max(1, m1, m2), m1 = ceil((2kappa - 1 - r_t)/4), m2 = ceil((R + 2k - 4p - 1 + r_t)/4),
and P = union over i = 1..m of the pairs {t + 3i - 1, t + 3i} (indices mod k).
Room: 3m <= k - 2 (3 m1 <= 3(2kappa + 1)/4 <= 3(k - 2)/4 as 2kappa + 1 = R + k - 2p + 1 <= k - 2;
3 m2 <= 3(2R + k - 4p + 3)/4 <= 3(k - 3)/4 using r_t <= R - k + 1; 3 <= k - 2).  So P has
exactly m intervals (the pairs), is disjoint from {t-1, t, t+1}, and P u {t} has m+1 intervals.
Let rho = R_P = 2m + exc with 0 <= exc and exc + (r_t - 1) <= R - k.
(F1) rho + r_t + 2m <= 2p - 1: if m = m1, 4m + exc + r_t <= 2kappa + 2 + exc <= 2R - 2p + 3 - r_t
     <= 2p - 4; if m = m2, <= R + 2k - 4p + 2 + 2r_t + exc <= 3R - 4p + 4 <= 2p - 5; if m = 1,
     4 + exc + r_t <= 5 + R - k <= 2p - 1 (as R - k <= p - 4).
(F2) rho + r_t + 2m >= 4m + r_t >= 4 m1 + r_t >= 2kappa - 1.
(F3) rho >= 2m >= R - 2p + 2m - 1.      (F4) exc <= R - k <= 2p - k - 1, i.e. rho <= 2p - k - 1 + 2m.
By (10.1): (F1),(F2) give U_{P+t} = floor((rho + r_t)/2), and (F3),(F4) give
L_P = floor((R - rho)/2).  Also floor(rho/2) <= p - m and floor((R - rho - r_t)/2) <= p - m - 1, so
U_P = min(rho + m - kappa - 1, floor(rho/2)) and L_{P+t} = min(R - rho - r_t + m - kappa,
floor((R - rho - r_t)/2)).
(A') with U^t = r_t - kappa.  Both minima attained by the reflection terms would need
ceil(rho/2) + m <= kappa and ceil((R - rho - r_t)/2) + m <= kappa - 1, whose sum gives
4m <= R + 2k - 4p - 2 + r_t < 4 m2; impossible.  If both floor terms:
U_P + U^t + L_{P+t} >= (R - r_t)/2 - 1 + r_t - kappa = (2p - k + r_t)/2 - 1 >= 1.  If only U_P is
the reflection term: >= (rho + r_t)/2 + m + R/2 - 2kappa - 3/2 >= (by F2) R/2 - kappa - 2
= (2p - k)/2 - 2 > -2.  If only L_{P+t} is: >= R - rho/2 + m - 2kappa - 1/2 >= (by F4) p - k/2 > 0.
(B') L_P + L^t + U_{P+t} >= (R - rho - 1 + R - r_t - 1 + rho + r_t - 1)/2 = R - 3/2, so >= R - 1
>= p - 2.
Windows: I({t}) nonempty (Step 1); U_P + L_P > 0 (if U_P is the reflection term,
U_P + L_P >= rho/2 + m + (2p - k)/2 - 3/2 > 0); U_{P+t} + L_{P+t} >= 0 (if L_{P+t} is the
reflection term, the sum is >= R - p + 2m - kappa = (R - k)/2 + 2m > 0); none is full (R <= 2p-3).
By the split lemma, lift(P + t) = lift(P) + x_t, hence
x_t >= (U_{P+t} + 1) - (p - L_P - 1) >= (R + r_t)/2 - 1 + 2 - p, i.e. bh_t >= R + 2 - 2p.  []

**Theorem C0-B.**  In setting C0-B the word has an identity 2p-subword.
Proof.  Suppose it avoids.  If Z is empty, Theorem ND.  Otherwise run Step 4 of Sec. 9 with
the Depth Lemma in place of (9.2) for the depth of the added defect (i* >= 2 still by (9.2)):
delta_P <= (2kappa - i*) + (2p - R - 2) = k - i* - 2 <= R - 1  (K4);
Phi(P) <= 2kappa + 1 + (r_t + 2 + delta_t) <= 2kappa + 3 + r_t + 2p - R - 2 = k + r_t + 1 <= R + 2;
(K3): rho_P + 2m <= Phi(P) <= R + 2 <= 2p;  (K6): delta_P + 2m - rho_P <= Phi(P) <= 2p;
(K5): delta_P + rho_P - 2m = Phi(P) - 4m <= k + r_t - 3 <= R - 2 <= R - k + 2p - 2.
(K1), (K2) as before.  So P_{i*} is killed, a contradiction.  []
Theorem S1 is the special case 4kappa + 3 <= R.
[F] check_C0B.py replays this proof (chain lifts, Step 1, the pairs pattern with every
inequality (F1)-(F4), (A'), (B'), the derived depth bound, the greedy and the final window
test) on all interval-feasible phi plus random phi: p = 7 (80 data), 11 (40), 13 (20),
k up to 15: 0 failures (kills found at: prefixes, the pairs pattern P or P + t, or the greedy).

## 11. Removing k >= p+1 and the parity restriction when B = 0; kappa = 0 [W]

**Theorem C0-B'.**  Let p >= 5 and let w be ANY RGR word of length 4p-2 (no inherited
hypothesis) with all rotation letters rho_1, all reflection runs odd, R <= 2p-2 and
kappa = p - 1 - H >= 1.  Then w has an identity 2p-subword.
Proof.  If some window is full we are done; assume none is (for R <= 2p-3 this is
automatic).  Secs. 9-10 use k >= p+1 only (i) to get kappa >= 1 (now a hypothesis), (ii) in
"Z empty => Theorem ND": with kappa >= 1, Z is never empty, since all bh_t >= 1 would give
2p - R = sum bh_t >= k, i.e. kappa = (R + k - 2p)/2 <= 0, and (iii) in the bound R - k <= p - 4
of (F1) (case m = 1), where R - k <= 2p - 6 (k >= 4) suffices.  If kappa = 1, (9.2) reads
delta_t <= -r_t < 0, so no run is a defect, contradicting Z nonempty; so kappa >= 2 when the
Depth Lemma is used, and then k >= 2kappa + 2 >= 6 (R <= 2p - 2).  All other steps use only
R <= 2p - 2, k <= R, R >= p (R = 2p - k + 2kappa is >= k if k >= p and > p if k < p), k <= 2p
and k >= 5 (room).  Re-check of the places where R <= 2p - 3 was written:
 Step 1: L^t = floor((R - r_t)/2) needs ceil((R - r_t)/2) > kappa, and
   ceil((R - r_t)/2) - kappa >= (2p - k - r_t)/2 >= 1/2 as k + r_t <= R + 1 <= 2p - 1;
   x_t <= r_t/2 < p - L^t as r_t/2 + L^t <= R/2 < p.
 Room: 2kappa + 1 = R + k - 2p + 1 <= k - 1, so 3 m1 <= 3(k - 1)/4 <= k - 2 (k >= 5);
   3 m2 <= 3(2R + k - 4p + 3)/4 <= 3(k - 1)/4.
 (F1): case m1: <= 2R - 2p + 3 - r_t <= 2p - 2; case m2: <= 3R - 4p + 4 <= 2p - 2.
 (F4): exc <= R - k <= 2p - k - 2.  (A'): the three case bounds stay >= 1/2, -1, 1.
 Greedy: Phi(P) <= k + r_t + 1 <= R + 2 <= 2p, so (K3), (K6) hold; (K4), (K5) as before.
 Lemma TL needs o = k <= 2p - 2.
No inherited inequality ((E), (P), (V), (D0)) is used in Secs. 9-10.  []
[F] hwsearch_c0b.cpp (hwsearch.cpp plus the filter: b = 0, all l odd, R <= 2p-3,
H <= p-2; no inherited filter; all phi): p = 5, k = 5..7, 119 data; p = 7, k = 5..11,
21,229 data; 0 avoiders.  check_C0B_ineq.py (every phi-independent inequality of the proof:
Step 0, L^t, (9.1), room, (F1)-(F4) as window identities, (A'), (B'), the K3 bound) on random
b = 0, all-odd, kappa >= 1 data: p = 7 and p = 11 with R <= 2p-3 (300 data each), R = 2p-2
(300 each) and R = 2p-1 (200 each); p = 13 with R <= 2p-3 (300 data); 0 failures (the
p = 13 runs with R >= 2p-2 hit the 30-minute cap and are not claimed).

**Lemma A1 (B = 0, R = 2p - 1).**  Let w be an RGR word of length 4p-2 with all rotation
letters rho_1, all reflection runs odd, R = 2p - 1 and kappa >= 1.  Then some window is
full.
Proof.  Here k = 2kappa + 1 and every run has r_t <= R - (k - 1) = 2p - k.  Put
m* = floor(kappa/2) + 1 and let P have m* intervals, x = R_P, with kappa <= x <= R - kappa.
For E in {x, R - x}: ceil(E/2) >= ceil(kappa/2) = kappa + 1 - m*, so floor(E/2) <=
E + m* - kappa - 1; and floor(E/2) <= floor((2p - 1 - kappa)/2) = p - 1 - floor(kappa/2) = p - m*.
So g(E) = floor(E/2) on both sides and g(x) + g(R - x) = p - 1 (R odd): I(P) is full.
Existence of P: k = 2kappa + 1 >= 2m* + 1.  The m*-interval patterns, encoded by their
2m* boundary cuts on the k-cycle, form a connected graph under "move one cut to an adjacent
free position" (an exclusion process on a cycle with a free site; cyclic order and hence
the in/out labelling is preserved), and rotating every cut to the next cut's position turns
P into P^c.  A move changes x by r_u for one run u, so |step| <= 2p - k, while
x(P^c) = R - x(P) and the target [kappa, R - kappa] contains R - 2kappa + 1 = 2p - k + 1
integers.  A path from P to P^c with x(P) < kappa cannot jump over the target.  []

**Trivial cut.**  If A >= 2p the subword rho_1^{2p} is an identity 2p-subword.

**Lemma OR (odd-segment reduction; OlsonParity, ../inverse-parity/proof-PAR-Kplus-partial.md
Sec. 1; rechecked here in the HW form).**  Merge every segment of consecutive rotation runs
between cyclically consecutive odd reflection runs into one rotation run (a~ = sum a,
b~ = sum b) and every even reflection run into the odd reflection run ending its segment.
The resulting RGR word w~ of length 4p-2 has the same R, F, A, B, H, kappa, k~ = o, all
reflection runs odd, and if w avoids then w~ avoids.  Check: a pattern of w~ is a pattern of
w that is a union of segments; its boundary runs are odd in both words, so beta = 0, m, E+-
and h = H agree, hence I(P) agrees (README Sec. 2); phi of a cyclic interval telescopes to
(y_{i-1} - y_j)/2 at its two boundary runs, whose values y are kept; so phi(P) agrees.  The
P = empty condition (min(A,B) <= kappa) is the same.  (o >= 1 by (V).)

**Corollary B0.**  An inherited RGR word of length 4p-2 with B = 0 (all rotations equal
after normalisation) and kappa >= 1 has an identity 2p-subword, whatever k, R and the
reflection-run parities.  Proof: w~ (Lemma OR) has B = 0, all reflection runs odd and the
same R and kappa >= 1: R <= 2p-2 Theorem C0-B', R = 2p-1 Lemma A1, R >= 2p the trivial cut
(A = R).  If w~ has an identity 2p-subword, w~ does not avoid, hence neither does w.  []

**kappa = 0 (any alphabet, any k).**  OlsonParity's Theorem K0
(../inverse-parity/proof-PAR-K0.md Sec. 3, [W]) is stated for k <= p, but its proof uses
k <= p only as R >= p (Step 1) and o_F <= p (Step 4).  For kappa = 0 both hold for every k:
o_F <= k <= R = 2p - o_F.  An inherited avoider with kappa = 0 and k >= p+1 would have
o_F = 2p - R <= 2p - k <= p - 1 < k, hence an even reflection run, and K0 (which uses only
(V), the zero condition B <= kappa = 0, kappa = 0 and R >= 5; I rechecked Steps 1-4 and
Lemma BC line by line) gives an identity 2p-subword.  So RUNS holds when kappa = 0.

**Status after Sec. 11.**  RUNS(p) holds for every inherited avoider candidate with B = 0
(Corollary B0 for kappa >= 1, K0 for kappa = 0).  In fact no inherited hypothesis is
needed: an avoider has kappa >= min(A, B) >= 0 (zero condition); if o = 0 then
R = 2p + 2kappa >= 2p and the trivial cut applies (B = 0); if o >= 2p - 1 the word is fully
alternating (Theorem ALT); otherwise Lemma OR, C0-B', A1 and the trivial cut use nothing
inherited, and K0 uses only o >= 1 and R >= 5 (R >= k >= p+1).  So every RGR word of length
4p-2 with B = 0 and k >= p+1 has an identity 2p-subword.  Remaining: B >= 1 (so
kappa >= B >= 1), where moreover A <= 2p - 1 (trivial cut) and B <= kappa <= p - 1.

## 12. Mixed alphabets (B >= 1): pair removal and net-aligned segments [W]

**Lemma M0 (pair removal).**  Let w be an RGR word of length 4p-2 and R_t a rotation run with
a_t, b_t >= 1 and r_t >= 3.  Delete one rho_1 and one rho_{-1} from R_t and insert
sigma_y sigma_y into any reflection run S_j = sigma_y^{l_j}.  The new RGR word w' (length 4p-2)
has the same k, the same d_t, the same reflection-run parities and the same phi (the values
y are unchanged), A' = A - 1, B' = B - 1, R' = R - 2, H' = H + 1, kappa' = kappa - 1, and every
half window shrinks, so if w avoids then w' avoids.
Proof.  For every pattern P (including P = empty, m = 0) E+-' = E+- - 1 and h' = h + 1
(l_j + 2 has the parity of l_j, so beta(P) is unchanged), hence
g'(E - 1) = min(p - m, E + m + h - p, floor((E - 1)/2)) <= g(E).  []
Iterating, every run with a_t != b_t becomes pure (a_t b_t = 0) and every run with
a_t = b_t becomes a (1,1)-pair; the zero condition B <= kappa is preserved (both drop by 1).
No inherited inequality is claimed for w' ((P) can fail by 1 per step); the theorems of
Sec. 11 that are applied to w' do not use them.

**Corollary MNA (net-aligned segments).**  Let w avoid, A >= B >= 1 (so B <= kappa), o >= 1,
and suppose every segment G_j of Lemma OR has D_{G_j} >= 1.  Then kappa = B and o <= p.
In particular an inherited word with k >= p+1, B >= 1, o >= p+1 and all D_{G_j} >= 1 does not
avoid.
Proof.  In w~ (Lemma OR) the merged runs are (A_{G_j}, B_{G_j}) with A_{G_j} > B_{G_j}; Lemma M0
(a run with a > b >= 1 has r >= 3) turns each into (D_{G_j}, 0).  The result w^ avoids, has
B = 0, all reflection runs odd, k^ = o, R^ = R - 2B and kappa^ = kappa - B >= 0.  If kappa^ >= 1,
the argument of Corollary B0 (C0-B' / A1 / trivial cut, none of which uses inherited
hypotheses) shows that w^ does not avoid; so kappa^ = 0, i.e. R^ = 2p - o, and R^ >= k^ = o
gives o <= p.  []

Remaining for RUNS (B >= 1): words in which some segment has D_{G_j} <= 0, and words with
o <= p (then w^ may be one of the extremal shapes with k^ = o <= p, and the even reflection
runs of w must be used).

**Lemma PM (merging across one even reflection run).**  Let S_j be an even reflection run
between R_j and R_{j+1}.  Merge R_j, R_{j+1} into one rotation run (a_j + a_{j+1}, b_j + b_{j+1})
and add the l_j letters of S_j to S_{j+1} (constant y_{j+1}).  The new RGR word has length 4p-2,
k - 1 runs, the same R, F, A, B, H, kappa, o and reflection parities, and its avoidance
conditions are those of w for the patterns not separating R_j, R_{j+1} (S_j is then not a
boundary and contributed l_j/2 to h, which S_{j+1} now carries: floor((l_{j+1} + l_j - f)/2) =
floor((l_{j+1} - f)/2) + l_j/2; phi telescopes over S_j).  So if w avoids, so does the merge.
(Lemma OR is the iteration of Lemma PM over all even runs.)  Consequently, for the
non-inherited form of RUNS (Sec. 11 status), it suffices to treat words that have all
reflection runs odd, or have k = p+1 exactly.

## 13. The open part: exact statement, evidence, failed approaches

**MIX_RUNS(p) (open).**  Every RGR word of length 4p-2 with k >= p+1 and 1 <= B <= min(A, kappa)
has an identity 2p-subword.
By Secs. 11-12 it suffices to take A <= 2p-1 (trivial cut), every rotation run pure or a
(1,1)-pair (Lemma M0), and either all reflection runs odd or k = p+1 (Lemma PM); if all
reflection runs are odd and every run has d_t >= 1, Corollary MNA already applies (so some
run is anti-aligned or a (1,1)-pair).  RUNS(p) for inherited avoiders follows from
Sec. 11 and MIX_RUNS(p).  By Theorem ND (whose kill needs only one run with
1 <= d_t <= min(2D + 1, 2p - 3)), MIX_RUNS(p) for all-odd words reduces to DEF for them:
some chain has all bh_t >= 1.
kappa = 1 is already closed: then B = 1 and OlsonParity's Theorem K1'
(../inverse-parity/proof-PAR-Kplus-partial.md Sec. 2, [W]) applies for every k.  Rechecked:
its Lemma BC certificate uses k <= p only through D + 3 >= p + 1 in (b), where D = 2p - o and
o <= p + 1 is automatic for kappa = 1 (R = 2p + 2 - o >= k >= o); its case E (o = 2, the
rho_{-1} alone, 2p - 1 letters rho_1 in the other segment) needs only c >= 3 runs in that
segment, which k >= p+1 gives without (D0) (and then R' = 2p - 1 - r_1 >= c - 1 >= 2, so
lambda({t_1}) + lambda(T) = ceil(r_1/2) + ceil(R'/2) + 2 = p + 2 or p + 1 as stated).
So MIX_RUNS(p) is open exactly for kappa >= 2 (with 1 <= B <= kappa).
Evidence [F]: p = 5, all a/b splits, NO inherited filter: no RGR word of length 18 with
k >= 6 avoids (hwsearch, k = 6..9, 220,019 + 50,684 + 3,584 + 256 data); p = 7 inherited,
all splits, k >= 8: no avoider (Sec. 8).  For mixed all-odd data with pure/(1,1) runs
(interval-feasible plus random phi surviving all prefix windows): check_M2_canon.py found
the interval-chain lifts canonical at every run in all 7,469 (p = 7) + 10,588 (p = 11)
cases in which no singleton window was hit (2 further p = 7 cases were singleton kills);
check_M2_var.py: the rule "all defects in depth order until
Phi_D := D_P + 2m + delta_P >= 2(kappa - B) + 2, then isolated aligned runs with bh = 1"
(variant V3; also V4 = anti/balanced defects first) killed all 7,704 (p = 7) + 9,364
(p = 11) cases; adding all anti/balanced runs (V1) or all of Z (V2) does not always work.
Failed approaches for B >= 1 (each checked, not just tried):
 * Transporting the C0 proof via the "padded shadow" (masses d_t, kappa -> kappa - B, R -> D;
   all mixed windows contain the shadow windows) fails exactly at runs with d_t <= 0: the
   C0 depth bound fails for anti-aligned defects (they reach the singleton bound
   2(kappa - B) - 2 - d_t; the D-based bound 2p - D - 2 held for every aligned defect but
   failed for 12 + 0 anti-aligned ones), and the chain-step inequality (9.1) has z3
   counterexamples (z3_step1*.py) for anti-aligned and also aligned t when the suffix
   D-sum is negative, even with a cycle-lemma chain start; so the C0 Step 1 argument does
   not transfer, although canonicity held in every sampled case.
 * Local moves that would lower B (deleting one rho_{-1} with one rho_1 from different runs,
   or one rho_{-1} with an inserted sigma) enlarge one side of some half window by 1, so
   they do not preserve avoidance; only the within-run move M0 does.
 * Lemma OR loses the information for o <= p: w~ can then be a genuine avoider with
   k~ <= p (cf. ../repr-WAS.md 4.3 type (II) shapes, non-inherited), so the even
   reflection runs of w must enter the argument.
 * Full windows alone: for inherited data with A = 2p-1, B >= 1 a full window always existed
   (p = 5, 7, Sec. 8) but no proof was found (the target range of D_P can be short while
   single runs carry up to p - 1); for A <= 2p-2 phi-dependent certificates are needed.

### 13.1 Division of the open part and further checks (host clock 2026-10-17 ~05:50 PDT)

Agreed with OlsonParity: kappa = B >= 1 (all k) is theirs (single-run Lemma BC chain of w~ plus
the capped case inside w; their notes, not yet a proof here).  The remaining part of RUNS on
this side is kappa > B >= 1, which would follow from
  MIX_DEF(p): every RGR word of length 4p-2 with ALL reflection runs odd and 1 <= B < kappa,
  B <= A, has an identity 2p-subword (any k; no inherited hypothesis).
Indeed Lemma OR keeps kappa and B, and Lemma M0 keeps kappa - B (so WLOG pure/(1,1) runs; if B
drops to 0, Corollary B0 applies since kappa - B >= 1).  Here sum bh_t = k - 2(kappa - B) < k,
so the defect set is never empty.  MIX_DEF is open.
Further failed approaches (z3, symbolic p): at block level (each anti/balanced run grouped
with aligned neighbours so blocks have net mass >= 1, j merges), the Step-1 inequality is
z3-PROVED when j <= B (z3_block.py) but has counterexamples for the bound j <= 2B that a
general block construction gives (z3_block2.py, also with kappa <= p-2 and kappa > B);
the split conditions (A'),(B') with non-fullness of the three windows still have
counterexamples (z3_split_nf.py), and on real data without full windows the split fails at
674 of ~9,100 interval-chain steps at p = 11 (split_cert.py) although sampled lifts stayed
canonical.  For B = 1 with the special run last in the chain, Step 1 is z3-PROVED (z3_B1.py).
Pipeline control for the B = 0 route: check_B0_pipeline.py (rho_1-only, any parities, OR to
w~, C0-B' replay on w~, kill pattern mapped back to w): p = 7, 150 data x 60 phi: every kill
transferred with identical windows (8,995 prefix + 5 singleton kills, 0 failures).
Addendum (2026-10-17 ~05:45 PDT): check_B0_pipeline.py at p = 11 (60 data x 60 phi) also finished:
3,600 kills (all at prefixes of w~) transferred to w with identical windows, 0 failures.
Addendum: split_cert_kb1.py (same test restricted to kappa > B, no full window, all chain starts):
p = 7, 150 data: all 11,612 interval-chain steps certified directly by the split lemma;
p = 11, 40 data: 8,358 direct + 2 via the cocycle decomposition, 1,294 uncertified.  So for
kappa > B the split lemma alone cannot give canonicity at p = 11 either.
