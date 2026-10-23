# Theorem MXG: the residual class with k <= p and B >= 1 (all primes p >= 5); with Theorem B0S, no avoider in RES_<(p) with k <= p

Owner OlsonReflectionRigidity.  r1 (579128c1...0c1c) written after host clock 2026-10-18T04:46:30-0700; r2 (this file) after
2026-10-18T04:48:03-0700 (author proofreading fixes before review; fix map Sec. 10).  Status: written proof [W], UNREVIEWED.
Route: notes-MXG-route-r1.md (734e7a58...7ffe).  The proof re-uses the PROOFS of the parent-accepted Theorem M chain
(MIX_low for RGR words) and re-verifies each of them for words with empty rotation runs; three pieces are new (Sec. 0.3).
Scope: words whose rotations lie in one {rho_x, rho_-x}; nothing about rotation values, INV*(p), RUNS(p) or ordered Olson.

## 0. Statement, imports, import map

### 0.1 Statement

**Theorem MXG.**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) whose rotation letters lie in {rho_1, rho_-1}
(normalised x = 1), written as a cyclic alternation R_1 S_1 ... R_k S_k of rotation runs and maximal constant reflection blocks
(a G-word, proof-K0star-r2.md Sec. 0: runs may be empty; an empty run lies between blocks of different values, i.e. u_t != 0).
Assume: every block has odd length; every run is pure aligned (a_t >= 1, b_t = 0), pure anti (a_t = 0, b_t >= 1) or empty;
A >= B >= 1; B < kappa := p - 1 - H; k <= p.  Then w has an identity 2p-subword (2p letters in increasing index order with
product 1).  The number of empty runs is arbitrary (0 allowed).
**Corollary (with Theorem B0S).**  RES_<(p) (proof-RED-r2.md Sec. 5) contains no avoider with k <= p.
Proof.  A word of RES_<(p) is a G-word with all blocks odd, every run pure or empty, A >= B and B < kappa.  If B = 0 then
kappa >= 1 and Theorem B0S (proof-B0S-r3.md, 95851b9c...e1ee; r2 bd854fe8...7170 Codex ACCEPT-WITH-FIXES) applies; if B >= 1,
Theorem MXG.  []

### 0.2 Imports

* Lemma H0 (proof-K0star-r2.md L55-58, 6681676e...96e1; algebra on the parent-accepted GRX): with all blocks odd (beta = 0),
  for a proper pattern P with m = m(P) intervals, I(P) = [-L_P, U_P], U_P = G_m(D_P), L_P = G_m(D - D_P),
      G_m(E) := min(p - m, E - g + m - 1, floor((E + B)/2)),   g := kappa - B,
  since lambda(P) - 1 = min(p - m, D_P + B - kappa + m - 1, floor((D_P + B)/2)); I(empty) excludes 0 iff min(A, B) <= kappa.
  P kills (w is solvable) if u_P lies in I(P) mod p, u_P := 2^(-1) sum_(t in P) theta_t.
* The Theorem M chain, parent-accepted (R/olson-par-mixlow-parent-verdict.md, c0ee2c46...e42a1), in
  inverse-parity/mixdef-low/c2/: [MXL] proof-MIX-low-partial-r2.md (adf8cb70...6a22), [RS4] proof-Rstar-r4.md
  (3b27db3f...3fa9), [R4C] proof-R4-closure-r1.md (4432a2d8...8837).  Their statements concern RGR words (all runs nonempty,
  runs pure or (1,1)-pairs); only their proofs are used, and each is re-checked below for G-words.
* Nothing else: no finite computation, no inherited hypothesis, no RUNS/INV result.

### 0.3 Import map (source lines; what changes for empty runs)

| piece here | source | status | what is checked or changed |
|---|---|---|---|
| Lemma S (Sec. 2) | MXL L21-68 | proof verbatim | uses only: interval masses in [-B, D + B], the window formula, 2g + B <= p - 1, D >= p + 2g, floor(A/2) <= p - 1 |
| Lemma K + Cor. (Sec. 2) | MXL L70-82 | verbatim | window algebra only |
| Lemma KL (Sec. 2) | RS4 L61-72 | verbatim | D_P >= -B: only anti runs have d < 0 |
| **Lemma GIANT (Sec. 3)** | new | NEW | replaces MXL L90-92 / RS4 Fact F(a) ("no d_t >= 2p - 1"), whose proof used nonempty runs |
| Fact F' (Sec. 3) | RS4 L47-53 | (a) by GIANT, (b)-(d) verbatim | |
| run classes (Sec. 3) | RS4 L55-59 | verbatim + empty runs classified | |
| **Lemmas Phi, G, AV, Theorem MIX-R (Sec. 4)** | MXL L84-130 | RE-DERIVED, tightened | L_Z gains n_EZ (empty defects); budget via delta >= 2 n_EZ; parity gives j = Delta/2 and residual R*_G (R2') |
| Lemma W (Sec. 5) | RS4 L74-90 | verbatim + checks | empty runs with phi >= 0 are cheap |
| Lemma B1 (Sec. 5) | RS4 L92-105 | verbatim except one sentence | "a' >= 1" (L95-96) replaced by GIANT |
| Lemmas ZP, C (Sec. 5) | RS4 L195-203 | verbatim | |
| **Lemma SPLIT (Sec. 6)** | new | NEW | replaces the cardinality-balanced split of RS4 L129-133, L168-170, L175-179 |
| Theorem A (Sec. 7) | RS4 L107-133 | RE-DERIVED with SPLIT | counts carry -n_EZ, compensated in SPLIT |
| Lemma KS (Sec. 7) | RS4 L151-170 | RE-DERIVED with SPLIT | same |
| Lemma AC (Sec. 7) | RS4 L172-180 | RE-DERIVED with SPLIT | same |
| Lemma R4 (Sec. 8) | R4C L24-57 | verbatim + checks | empty defects are free with d = 0 |
| assembly (Sec. 8) | RS4 L145-221, R4C L59-80 | re-stated | M0 and S1' steps of R4C are not needed (runs pure; B = 0 is Theorem B0S) |
| Lemma G1 | RS4 L135-143 | not used | |

## 1. Setting and notation

w as in Theorem MXG.  R = A + B = 2p - k + 2 kappa (all blocks odd: o_F = k, eq. (0.1) of proof-K0star-r2.md), so
D := A - B = 2p - k + 2g.  If A >= 2p, rho_1^(2p) is an identity 2p-subword; so A <= 2p - 1, i.e. 2g + B <= k - 1 <= p - 1, and
s := k - 1 - 2g - B >= 0, D >= p + 2g, k >= 4.  Runs: aligned (d_t = a_t >= 1), anti (d_t = -c_t, c_t = b_t >= 1), empty
(d_t = 0).  B = sum of c_t over anti runs (the anti mass; there are no pairs).  For every nonempty proper set of runs Q,
D_Q = A_Q - B_Q lies in [-B, A] = [-B, D + B].  Suppose w avoids; then no window is full, u_P is not in I(P) mod p for every
proper P, and u_t != 0 for every empty run t.  From here on w is assumed to avoid: each lemma below either states a property
of the lift data or exhibits an identity 2p-subword ("w is solvable"), i.e. a contradiction.
Lift data (Lemma S): x_t, phi_t := d_t - x_t, bh_t := 2 x_t - d_t = d_t - 2 phi_t (bh_t = d_t mod 2); sum_t bh_t = k - 2g,
sum_t phi_t = TOT := p - k + 2g.  For a set P of runs: sums phi(P), BH(P), D_P; m(P) = number of maximal cyclic blocks;
c(P) := phi(P) + m(P); Phi(P) := D_P - BH(P) + 2m(P) = 2 c(P) (so Phi(P) is EVEN); weights w_t := phi_t + 1, W(P) := sum w_t;
for an independent P (no two runs cyclically adjacent, P != [k]) m(P) = |P| and c(P) = W(P).
Classes (RS4 L55-59): cheap: phi >= 0 and bh <= 1; free: phi >= 0 and bh <= 0; filler: cheap with bh = 1.
Z0 := {bh <= 0} (the defects), Y := [k] \ Z0; Y_al, Y_anti, Y_E := aligned, anti, empty runs of Y; n_EZ := number of empty
runs in Z0; Z0+ := free runs; alpha := number of free anti runs; beta := number of anti runs of Z0 with phi <= -1;
n_d := number of aligned runs of Z0; B_Z, B_Y := anti mass in Z0, in Y (B = B_Z + B_Y).

## 2. Lemma S, Lemma K, Lemma KL (proofs verbatim)

**Lemma S (MXL L21-68).**  Fix a run boundary as chain start, P_j := the first j runs.  For 1 <= j <= k - 1 the window of P_j
is nonempty and not full, and V_j := the representative of u_(P_j) in [U_(P_j) + 1, p - L_(P_j) - 1] is unique; V_0 = 0,
V_k = p; x_t := V_t - V_(t-1).  Every proper cyclic interval Q satisfies U_Q + 1 <= x(Q) <= p - L_Q - 1; in particular x_t is
the representative of u_t in [U_t + 1, p - L_t - 1] (independent of the start) and sum_t x_t = p.  phi-form (RS4 L43-45):
phi(Q) <= gam(D_Q) := max(D_Q - p, g - 1, floor((D_Q - B - 1)/2)) for every proper cyclic interval Q.
Proof.  MXL L23-68 verbatim.  It uses about the runs only: (i) every nonempty proper interval has mass in [-B, D + B]
(MXL L28, L49-50, L54-55, L59-60); (ii) the window formula of Sec. 0.2; (iii) 2g + B <= p - 1 and D >= p + 2g (L36, L57, L62);
(iv) B - kappa - 1 < 0 and floor(A/2) <= p - 1 for the cases j = 0, k (L25-26, L39-43).  All four hold here (Sec. 1).  []
Consequences for empty runs.  For an empty run t, U_t = G_1(0) = -g, so x_t >= 1 - g; and x_t != 0 (u_t != 0 and
x_t in [1 - g, p - 1]).  Hence an empty run is either an EMPTY DEFECT (x_t <= -1: phi_t = -x_t in [1, g - 1], bh_t = 2 x_t <= -2;
free) or an empty non-defect (x_t >= 1: phi_t <= -1, bh_t >= 2; not cheap).  If g = 1 there is no empty defect.
Singleton bound (RS4 L50-51): from x_t >= U_t + 1, bh_t >= min(2p - d_t, d_t - 2g + 2, B + 1 + [d_t + B even]).
**Lemma K (MXL L70-82), verbatim.**  A proper P with m blocks kills if (i) x(P) + m <= p, (ii) Phi(P) >= 2g + 2,
(iii) BH(P) <= B, (iv) x(P) >= m - p, (v) x(P) >= D_P - D + g - m + 1, (vi) BH(P) >= -A (x(P) = (D_P + BH(P))/2).
Corollary: if Phi(P) <= 4g + 1, BH(P) <= B and D_P >= -B, then (i), (iv), (v), (vi) hold (2g + B <= p - 1, D >= p + 2g).
**Lemma KL (RS4 L61-72), verbatim.**  If S is a proper nonempty set of runs with phi_t <= g - 1 on S, c(S) >= g + 1 and
BH(S) <= B, then w is solvable.  (Its proof orders S with the runs of bh <= 0 first, takes the shortest prefix P with
c(P) >= g + 1, so c(P) <= 2g, BH(P) <= B, and D_P >= -B because only anti runs have negative d, of total mass B; then Lemma K.)
S need not be independent.

## 3. Lemma GIANT (new) and Fact F'

**Lemma GIANT.**  (w avoids.)  Every run has d_t <= 2p - 2.
Proof.  Suppose d_T >= 2p - 1.  Since d_T <= a_T <= A <= 2p - 1, T is aligned with a_T = A = 2p - 1, and every other run has
a = 0, i.e. is anti or empty.  There are at most B anti runs (each has c >= 1), so n_E >= k - 1 - B >= 2g >= 2 empty runs.  For
an empty run t: L_t = G_1(D) = min(p - 1, D - g, floor(A/2)) = p - 1, because floor(A/2) = p - 1 and D - g = 2p - 1 - B - g
>= p - 1 (B + g <= p - 1).  By Lemma S, x_t <= p - L_t - 1 = 0, and x_t != 0, so every empty run is an empty defect (if g = 1
this is already impossible): phi_t in [1, g - 1], bh_t <= -2.  Let S be the set of empty runs: nonempty, proper (T notin S),
phi <= g - 1 on S, c(S) >= phi(S) + 1 >= |S| + 1 >= 2g + 1, BH(S) <= -2|S| < B.  Lemma KL.  []
**Fact F'.**  (a') = Lemma GIANT.  (b) d_t >= 2g + B + 1 implies bh_t >= 2.  (c) d_t <= 2g + B implies phi_t <= g - 1.
(d) 2g + B - 1 <= d_t <= 2p - B - 1 implies bh_t >= B + 1.  Proof: RS4 L50-53 verbatim, with (a') in place of (a) (only
2p - d_t >= 2 is used).  Consequently (RS4 L56-57) a filler is aligned (empty runs have even bh; an anti run with bh >= 1 has
phi = (-c - bh)/2 < 0), and every cheap run has d_t <= 2g + B, hence phi_t <= g - 1.  Empty defects are free; empty
non-defects are not cheap.

## 4. Theorem MIX-R for G-words (re-derived and tightened; replaces MXL L84-130)

**Lemma Phi'.**  Z0 is nonempty and proper (sum bh = k - 2g lies in [B + 1, k - 1]).  With m := m(Z0), delta := -BH(Z0),
exc := sum_Y (bh - 1) >= 0, a_Z := sum_(Z0) (d - 1), S_Z := sum over aligned t in Z0 of (d_t - 1) >= 0 and
L_Z := sum over anti t in Z0 of (1 + c_t) + n_EZ   [n_EZ replaces "#pairs in Z0" of MXL L106],
one has a_Z = S_Z - L_Z, delta = 2g + exc - |Z0| and Phi(Z0) = 2g + a_Z + exc + 2m (MXL L88-89; pure arithmetic).  Every
defect t has f_t := d_t - bh_t <= 2g - 2, and every aligned run with bh_t = 1 has d_t <= 2g - 1: in the singleton bound the terms
2p - d_t >= 2 (GIANT) and B + 1 + [..] >= 2 exceed 1, so bh_t <= 1 forces bh_t >= d_t - 2g + 2.  So every aligned run with
bh = 1 is a filler of MXL's kind (d <= 2g - 1, Phi-increment d + 1 <= 2g).  Also L_Z <= 2 B_Z + n_EZ and delta >= 2 n_EZ (each
empty defect has -bh >= 2, every defect -bh >= 0).  If F is a set of fillers, pairwise non-adjacent and not adjacent to Z0, then
Phi(Z0 u F) = Phi(Z0) + sum_F (d_t + 1) and BH(Z0 u F) = -delta + |F|.
**Lemma G'.**  If Phi(Z0) >= 2g + 2, or Phi(Z0) <= 2g and some F as above has |F| = j := (2g + 2 - Phi(Z0))/2, then w is
solvable.  (j is an integer because Phi is even.)
Proof.  If Phi(Z0) <= 2g: j = (2 - a_Z - exc - 2m)/2 <= (2 - 2m + L_Z)/2 <= L_Z/2 <= B_Z + n_EZ/2.  Put P* := Z0 u F (P* := Z0 if
Phi(Z0) >= 2g + 2); Phi(P*) >= 2g + 2.  Order P*: Z0 first (any order), then F.  Every prefix has BH <= max(0, -delta + j)
<= max(0, B_Z + n_EZ/2 - 2 n_EZ) <= B [this replaces "j <= B" of MXL L106, which used L_Z <= 2B].  Adding one run changes Phi by
at most f_t + 2 <= 2g (defect) or d_t + 1 <= 2g (filler), so the shortest prefix P with Phi(P) >= 2g + 2 has Phi(P) <= 4g + 1,
BH(P) <= B, D_P >= -B; P is proper since the end runs of every gap of Z0 are not in P*.  Lemma K with its Corollary.  []
**Lemma AV'.**  If Phi(Z0) <= 2g and |Y_al| + |Y_E| + a_Z >= 2, the set F of Lemma G' exists.
Proof.  Write the cycle as Z_1 G_1 ... Z_m G_m (defect blocks Z_i, gaps G_i of lengths l_i >= 1, sum l_i = |Y|).  Interior
runs of G_i are those other than its two end runs; they are not adjacent to Z0, and interior runs of different gaps are not
adjacent.  A blocker is an interior run that is not a filler: an aligned run with bh >= 2 or an empty run of Y (each
contributes >= 1 to exc), or an anti run of Y (|Y_anti| of them; they contribute >= 0 to exc).  So the number b_i of blockers
in G_i satisfies sum b_i <= exc + |Y_anti|.  Taking every other filler in each maximal segment of interior fillers gives at least
sum_i (l_i - 2 - b_i)/2 >= (|Y| - 2m - exc - |Y_anti|)/2 pairwise non-adjacent fillers not adjacent to Z0.  This is >= j =
(2 - a_Z - exc - 2m)/2 iff |Y| - |Y_anti| + a_Z >= 2, i.e. |Y_al| + |Y_E| + a_Z >= 2.  []
**Theorem MIX-R'.**  If w avoids, its lift data lie in
  R*_G := {Phi(Z0) <= 2g, i.e. (R1) a_Z + exc + 2m <= 0} and {(R2') |Y_al| + |Y_E| + a_Z <= 1}.
(R*_G is contained in MXL's R*, whose (R2) reads |Y_al| + a_Z <= 2.)

## 5. Lemmas W, B1, ZP, C for G-words

**Lemma W (RS4 L74-90).**  If B >= g + 1, w is solvable.  Proof verbatim.  Checks: Step 1 needs that a run with phi >= 0
which is not cheap is aligned with bh >= 2 (an anti run with phi >= 0 has bh = -c - 2 phi < 0; an empty run with phi >= 0 has
bh = -2 phi <= 0; both are then cheap), so W(cheap) >= p + 2g - A/2 >= 2g + 1/2; Step 2 needs w_t0 <= g (cheap runs have
phi <= g - 1, Fact F'), p >= k >= g + 2 and k >= 4; Step 3 needs BH(S) <= #{t in S : bh_t = 1} <= |S| <= g + 1 <= B.  []
**Lemma B1 (RS4 L92-105).**  If some run T has d_T >= 2p - B, w is solvable.
Proof.  As in RS4 L95-105, except that the sentence "a' >= 1 (else the other k - 1 runs are antis, ...)" (L95-96), which used
that runs are nonempty, is replaced by: by GIANT, d_T <= 2p - 2; with gam(d_T) = d_T - p (L97-98), phi(R') = TOT - phi_T >=
2p - k + 2g - d_T, hence W(R') = phi(R') + k - 1 >= 2g + (2p - 1 - d_T) >= 2g + 1, which is what L100 uses.  The rest is
verbatim: for t != T, d_t <= a' := A - d_T <= B - 1, so phi_t <= g - 1 (F'(c)); a parity class X of the path R' has
W(X) >= g + 1; S := {t in X : phi_t >= 0} has c(S) >= g + 1 and BH(S) <= sum_S d_t <= a' <= B - 1 (possibly a' = 0); Lemma KL.  []
**Lemma ZP (RS4 L195-197), verbatim.**  If c(Z0+) >= g + 1, w is solvable (S = Z0+: free runs are cheap, BH <= 0).
**Lemma C (RS4 L199-203), verbatim.**  If every run has phi_t <= g - 1 except possibly t0, phi_(t0) <= p - k + g and
bh_(t0) >= s + 1, then w is solvable (S = [k] \ {t0}, an interval: c(S) = TOT - phi_(t0) + 1 >= g + 1, BH(S) <= B).

## 6. Lemma SPLIT (new)

**Lemma SPLIT.**  Let C be a nonempty set of cheap runs with C != [k], and let E be the set of empty runs in C (all of them
empty defects).  Then there are U*, V* with U* u V* = C, U* n V* = E,
   min(c(U*), c(V*)) >= floor((|C| + |E|)/2),   BH(U*) + BH(V*) = BH(C) + BH(E) <= BH(C) - 2|E|.
Proof.  C' := C \ E.  A C'-block is a maximal set of cyclically consecutive runs of C'; no C'-block is the whole cycle.  An
E-block is a maximal set of consecutive runs of E; m(E) := number of E-blocks; each E-block has at most two outer neighbours
(the runs just outside it), which are not in E.  For each C'-block beta = (t_1, ..., t_L) put its two classes
{t_1, t_3, ...} and {t_2, t_4, ...}; choosing an orientation per block sends one class to U', the other to V'.  U' and V' are
independent (runs of one class of a block are not adjacent; different C'-blocks are separated by a run outside C').  Let
a(U') := number of pairs (b, t), b an E-block, t in U' an outer neighbour of b; similarly a(V'); a(U') + a(V') <= 2 m(E).
Put U* := U' u E, V* := V' u E.  The U'-runs are pairwise non-adjacent and so are the E-blocks; the adjacency graph between
U'-runs and E-blocks is a disjoint union of paths (no cycle, as U* != [k]), so m(U*) = |U'| + m(E) - a(U') and
   c(U*) = W(U') + phi(E) + m(E) - a(U') >= (|U'| - a(U')) + |E| + m(E)
(cheap runs have w >= 1, empty defects phi >= 1); likewise for V*.  For a C'-block with L runs whose end runs t_1, t_L have
eps_1, eps_L in {0, 1} outer E-neighbours (for L = 1 the single run has eps_l + eps_r in {0, 1, 2}), the two classes contribute
to |U'| - a(U') the values (1 - eps_l - eps_r, 0) if L = 1; ((L + 1)/2 - eps_1 - eps_L, (L - 1)/2) if L >= 3 is odd; and
(L/2 - eps_1, L/2 - eps_L) if L is even: they differ by at most 1.  Choosing the orientations one block at a time so that the
running difference (|U'| - a(U')) - (|V'| - a(V')) stays in [-1, 1] gives |(|U'| - a(U')) - (|V'| - a(V'))| <= 1, while their
sum is |C'| - a(U') - a(V') >= |C'| - 2 m(E).  Hence
   min(c(U*), c(V*)) >= (|C'| - 2 m(E) - 1)/2 + |E| + m(E) = (|C| + |E| - 1)/2,
and min >= floor((|C| + |E|)/2) by integrality.  Finally BH(U*) + BH(V*) = BH(U') + BH(V') + 2 BH(E) = BH(C) + BH(E), and every
empty defect has bh <= -2.  []
(With E empty this is the cardinality-balanced alternating split of RS4 L129-133.)

## 7. Theorem A, Lemma KS, Lemma AC for G-words (re-derived with SPLIT)

**Theorem A'.**  In R*_G, if some run T has bh_T >= B + 1, w is solvable.
Proof.  T is not cheap.  The non-cheap runs t != T are: (i) aligned with bh >= 2; (ii) empty runs of Y; (iii) anti runs of Y;
(iv) anti runs of Z0 with phi <= -1 (then -c + 2 <= bh <= 0, so c >= 2).  [An aligned run with bh <= 1 has phi = (d - bh)/2 >= 0;
an empty run with phi >= 0 is an empty defect, cheap; an anti run is cheap iff phi >= 0.]  exc >= (bh_T - 1) + #(i) + #(ii)
(T is in Y), and (R1) gives exc <= -a_Z - 2m = L_Z - S_Z - 2m with L_Z = #anti(Z0) + B_Z + n_EZ.  Also #(iii) <= B_Y and
#anti(Z0) + #(iv) <= B_Z.  With k - 1 = 2g + B + s:
  #cheap >= (2g + B + s) - [#anti(Z0) + B_Z + n_EZ - S_Z - 2m - bh_T + 1] - B_Y - #(iv)
         >= 2g + s + 2m + S_Z + (bh_T - 1 - B_Z) - n_EZ >= 2g + 2 - n_EZ.
Let C := the cheap runs (T notin C) and E := its empty runs (= the n_EZ empty defects): |C| + |E| >= 2g + 2.  BH(C) <=
#fillers + BH(E) <= #fillers - 2 n_EZ, and #fillers <= |Y_al| - [T aligned] <= 1 - a_Z - |Y_E| <= 1 - S_Z + L_Z <= 1 + 2 B_Z + n_EZ
by (R2').  Lemma SPLIT gives U*, V* with c >= g + 1 and BH(U*) + BH(V*) <= BH(C) - 2 n_EZ <= 1 + 2B - 3 n_EZ <= 2B + 1, so one of
them has BH <= B; it is proper, nonempty and consists of cheap runs (phi <= g - 1).  Lemma KL.  []
**Lemma KS'.**  In R*_G, suppose not every run is cheap and 2 phi(Z0+) + alpha <= 2g + s - 1 + S_Z.  Then w is solvable.
Proof.  The runs of Z0 that are not free are the beta anti runs with phi <= -1 (aligned defects have phi >= d/2 > 0, empty
defects phi >= 1).  Let nu := number of runs of Y that are not fillers: the aligned ones with bh >= 2 (nu_al, each contributing
>= 1 to exc_al := sum over Y_al of (bh - 1)), and the runs of Y_anti and Y_E.  Then #cheap = k - beta - nu and
nu <= exc - exc_ae + |Y_anti| + |Y_E| with exc_ae := sum over Y_anti u Y_E of (bh - 1) >= |Y_E|.  From 2 phi(Z0) = Phi(Z0) - 2m
= 2g + a_Z + exc, a_Z = S_Z - L_Z, L_Z = alpha + beta + B_Z + n_EZ and k = 2g + B_Z + B_Y + s + 1:
  #cheap >= 4g + s + 1 + S_Z - alpha - 2 beta - 2 phi(Z0) - n_EZ + (B_Y - |Y_anti|) + (exc_ae - |Y_E|)
         >= 4g + s + 1 + S_Z - alpha - 2 phi(Z0+) - n_EZ       (phi(Z0) <= phi(Z0+) - beta, B_Y >= |Y_anti|),
so #cheap + n_EZ >= 2g + 2 by hypothesis.  BH(cheap) <= #fillers - 2 n_EZ <= |Y_al| - 2 n_EZ <= 1 + 2 B_Z + n_EZ - 2 n_EZ (R2').
Lemma SPLIT with C := the cheap runs (C != [k]) and E := the empty defects: c(U*), c(V*) >= g + 1 and BH(U*) + BH(V*) <=
1 + 2 B_Z - 3 n_EZ <= 2B + 1.  Lemma KL for the one with BH <= B.  []
**Lemma AC'.**  In R*_G, if every run is cheap, w is solvable.
Proof.  Then Y consists of fillers and every empty run is an empty defect (|Y_E| = 0, n_E = n_EZ).  h := |Y| satisfies
h - delta = sum bh = k - 2g, so h >= k - 2g = s + 1 + B; (R2') gives h = |Y_al| <= 1 - a_Z = 1 - S_Z + L_Z <= 1 + 2B + n_EZ;
hence s <= B + n_EZ.  All runs are cheap: weights >= 1, phi <= g - 1.
If B + s + n_EZ >= 2: pick a filler t0 and apply Lemma SPLIT to C := [k] \ {t0}, E := all empty runs: min c >= floor((k - 1 +
n_EZ)/2) = floor((2g + B + s + n_EZ)/2) >= g + 1, and BH(U*) + BH(V*) = BH(C) + BH(E) <= (k - 2g - 1) - 2 n_EZ = B + s - 2 n_EZ
<= 2B - n_EZ <= 2B + 1.  If B + s + n_EZ <= 1: B = 1, s = 0, n_EZ = 0, so there is no empty run and k = 2g + 2 is even; the two
parity classes of the cycle are independent, of size g + 1, with BH summing to k - 2g = 2: one has BH <= 1 = B (RS4 L178-179).
In both cases Lemma KL.  []

## 8. Lemma R4 for G-words, assembly, proof of Theorem MXG

Elimination order (RS4 L145-221 with the G-versions): GIANT, MIX-R', W, B1, A', AC', KS', ZP, C.  If w avoids, its lift data
therefore lie in
  R4_G := R*_G n {B <= g} n {every d_t <= 2p - B - 1} n {every bh_t <= B} n {not every run cheap}
          n {2 phi(Z0+) + alpha >= 2g + s + S_Z} n {c(Z0+) <= g} n {every bh_t <= s}.
(For Lemma C: with every bh_t <= B and every d_t <= 2p - B - 1, Fact F'(d) gives every d_t <= 2g + B - 2, so every
phi_t <= g - 1 <= p - k + g (k <= p); hence any t0 with bh_(t0) >= s + 1 is killed.)
**Lemma R4' (R4C L24-57).**  No avoider has lift data in R4_G.
Proof.  R4C L27-55 verbatim.  Checks: (i) every d_t <= 2g + B - 2 and phi_t <= g - 1 (as just said); (ii) every bh_t <= s;
(iii) Z0+ != empty, X := phi(Z0+) <= g - 1, alpha >= 2 m(Z0+) + s + S_Z >= s + 2, and B >= alpha because each free anti run carries
>= 1 unit of the anti mass B; with B <= g, s <= B - 2 <= g - 2; (iv) aligned defects are free with phi >= 1 and empty defects are
free with d = 0 [replaces "every pair of Z0 is free"], so D(Z0+) = S_Z + n_d - (anti mass of free antis) and
delta+ := -BH(Z0+) = 2X - D(Z0+) >= 2X + alpha - S_Z - n_d >= 2g + s - n_d >= g + s + 1 (n_d <= X).  Step 1: Y is nonempty
(sum bh = B + s + 1 > 0) and not the whole cycle; BH(Y) = s + 1 + B + delta >= 3s + g + 4; on Y, 1 <= bh <= s (empty runs of Y
included); a parity class Q of larger BH in each path of Y is independent (k >= 4); N, built from Q, has s + 1 <= BH(N) <= 2s,
|N| >= 2.  Step 2 (a)/(b) verbatim: (a) S' := [k] \ N, m(S') = |N|, c(S') = TOT - phi(N) + |N| >= g + 1, BH(S') <= B;
(b) S := Z0+ u N, BH(S) <= 2s - delta+ < B, S != [k], c(S) >= X + phi(N) + 1 >= g + 3.  Lemma KL in both cases.  []
**Proof of Theorem MXG.**  Suppose w avoids.  Sec. 1 (trivial cut) gives A <= 2p - 1.  Lemma S gives lift data; by GIANT,
MIX-R', W, B1, A', AC', KS', ZP and C every alternative to R4_G yields an identity 2p-subword; Lemma R4' excludes R4_G.
Contradiction.  []

## 9. Remarks

(1) Where empty runs enter.  (a) Lemma S: masses of intervals made of empty runs are 0 (inside [-B, D + B]); genuineness gives
x_t != 0, which makes every empty run either an empty defect (phi >= 1, bh <= -2) or not cheap.  (b) GIANT replaces the RGR
fact that no run carries all of A (with nonempty runs the others would all be anti).  (c) L_Z gains n_EZ (MIX-R', Theorem A',
KS'), paid for by delta >= 2 n_EZ (Lemma G') and by SPLIT, where the empty defects are put into BOTH halves (each has phi >= 1 and
bh <= -2).  (d) Empty runs of Y are blockers counted in exc (AV') and are type (ii) in Theorem A'.  (e) In R4' empty defects are
free runs of mass 0.
(2) The parity of Phi (Phi = 2c) is used for j = Delta/2 (Lemma G') and for the threshold 2 in (R2'); (R2') is what Theorem A'
and KS' need when T or the excess sits on empty runs of Y (RS4 L127-128 used that a non-aligned T contributes to B_Y, false for
an empty T).
(3) Not covered: k >= p + 1 (B = 0 and B >= 1).  No finite computation is used; a lift-sampled replay of every elimination with
raw-DP checks (plan to be frozen before running) is an aid only.

## 10. Fix map r1 -> r2 (author, before any review)

1. Sec. 0.1: the typo "(a_t >= 1 = ... b_t = 0)" now reads "(a_t >= 1, b_t = 0)".
2. Sec. 1: the standing assumption "w avoids" for Secs. 2-8 is stated explicitly; Lemma GIANT says so in its statement.
No mathematical step changed.
