# MIX_low: reduction to one residual case (partial proof)

Owner OlsonParity.  Written after host clock 2026-10-17T12:40 PDT.  Status: Sec. 1-5
written proofs [W], not yet reviewed.  Sec. 6 is the precise open case, with evidence [F].
Setting and notation: README.md here (frozen).  MIX_low(p): an RGR word of length 4p-2,
all k reflection runs odd, k <= p, A >= B >= 1, B < kappa <= k-1, g := kappa - B >= 1.
Runs are pure aligned (d >= 1), pure anti (d = -c <= -1) or (1,1)-pairs (d = 0), by Lemma M0.
D := A - B = 2p - k + 2g >= p + 2g.  If A >= 2p, rho_1^{2p} is an identity 2p-subword, so
assume A = D + B <= 2p - 1, i.e. 2g + B <= k - 1 <= p - 1.
Windows (Lemma H, beta = 0): U_P = G_m(D_P), L_P = G_m(D - D_P),
G_m(E) = min(p - m, E - g + m - 1, floor((E + B)/2)).
Assume v avoids, with theta and u_P = 2^{-1} sum_P theta.

## 1. Lemma S (interval lower bounds; Step 1)

Fix a run boundary as the chain start.  Let P_j be the first j runs, and let V_j be the
representative of u_{P_j} in [U_{P_j} + 1, p - L_{P_j} - 1].  Then V_0 = 0 and V_k = p
(as in proof-PAR-Kplus-partial-r2.md Sec. 3' Step 0; here use B - kappa - 1 < 0 and
floor(A/2) <= p - 1).  Put x_t := V_t - V_{t-1}.
**Claim.**  Every proper cyclic interval Q satisfies U_Q + 1 <= x(Q) <= p - L_Q - 1.
In particular x_t is the representative of u_t in [U_t + 1, p - L_t - 1], so x does not
depend on the start, and sum_t x_t = p.
Proof.  Take Q = (a, b] with 0 < a < b < k; the cases a = 0 and b = k are immediate from
the ranges of V_b and V_a.  The three parts P_a, Q and P_b^c are nonempty intervals with
masses alpha, q, beta, where alpha + q + beta = D.  Every nonempty proper interval has mass
in [-B, D + B].  Put G~(E) := min(p - 1, E - g, (E + B - 1)/2).  It is concave and
G~ <= G_1.
(lower) x(Q) = V_b - V_a >= G_1(alpha+q) + 1 - (p - G_1(q+beta) - 1); this is >= -L_Q =
-G_1(alpha+beta) once the three values G_1 of the pair sums add up to >= p - 2.  The
triple of pair sums lies in {y in [-B, D+B]^3 : sum y = 2D}, whose vertices are the
permutations of (-B, D, D + B).  There
  G~(-B) + G~(D) + G~(D+B) = -B - g + (D + B - 1)/2 + min(p - 1, (D + 2B - 1)/2),
which is >= min(D + B/2 - g - 1, p - 1 + (p - B - 1)/2) >= p - 2.
Hence x(Q) >= -L_Q.  Since u_Q is not in [-L_Q, U_Q] mod p, it follows that x(Q) >= U_Q + 1.
(upper) x(Q) <= p - G_1(alpha) - G_1(beta) - 2.  The masses alpha, q, beta lie in
{y in [-B, D+B]^3 : sum y = D}, whose vertices are the permutations of (-B, 0, D + B).  There
  sum G~ = -B - 2g + min(p - 1, (D + 2B - 1)/2) >= -2
(use 2g + B <= p - 1 and D >= p + 2g).  So x(Q) <= p + U_Q, and therefore
x(Q) <= p - L_Q - 1.
Wrapping intervals are complements of non-wrapping ones, and x(Q^c) = p - x(Q).  []
Conversely, an integer x with x_t = u_t mod p, sum x_t = p and x(Q) >= U_Q + 1 for all
proper intervals makes theta interval-feasible.  So "interval-feasible theta" means the
same as "integer bh_t := 2x_t - d_t (= d_t mod 2) with BH(Q) >= 2G_1(D_Q) + 2 - D_Q for
every proper interval and sum bh = k - 2g".

## 2. Lemma K (direct kill)

For a proper pattern P with m blocks, put x(P) = (D_P + BH(P))/2 and
Phi(P) := D_P - BH(P) + 2m.  P has u_P in I(P), and so v has an identity 2p-subword, if
 (i) x(P) + m <= p, (ii) Phi(P) >= 2g + 2, (iii) BH(P) <= B, (iv) x(P) >= m - p,
 (v) x(P) >= D_P - D + g - m + 1, (vi) BH(P) >= -A.
These are the six terms of -L_P <= x(P) <= U_P; (iii) is x(P) <= floor((D_P+B)/2).
**Corollary.**  If Phi(P) <= 4g + 1, BH(P) <= B and D_P >= -B, then (i), (iv), (v) and (vi)
hold, because 2g + B <= p - 1 and D >= p + 2g:
(i) D_P + BH + 2m = Phi + 2BH <= 4g + 1 + 2B <= 2p;
(iv) 2x = 2D_P + 2m - Phi >= -2B + 2m - 4g - 1 >= 2m - 2p;
(v) Phi <= 4g + 1 <= 2D - 2g - 2 + 4m;
(vi) BH = D_P + 2m - Phi >= -B + 1 - 4g >= -A.

## 3. Lemma Phi (accounting)

Put f_t := d_t - bh_t, Z0 := {bh_t <= 0} (nonempty and proper, since sum bh = k - 2g lies
in [B + 1, k - 1]), Y := the complement of Z0, m := m(Z0), delta := -BH(Z0) >= 0,
exc := sum_Y (bh_t - 1) >= 0, a_Z := sum_{Z0} (d_t - 1).  Then delta = 2g + exc - |Z0| and
  Phi(Z0) = 2g + a_Z + exc + 2m.
Every proper-interval bound from Sec. 1 applied to a single run gives f_t <= 2g - 2 unless
d_t >= 2g + B.  The latter runs have bh_t >= 2 and are not defects.  An aligned run with
bh_t = 1 has d_t <= 2g - 1 or d_t >= 2p - 1.
A filler is an aligned run with bh_t = 1 and d_t <= 2g - 1.  If F is a set of fillers that
are pairwise non-adjacent and not adjacent to Z0, then
Phi(Z0 u F) = Phi(Z0) + sum_F (d_t + 1) and BH(Z0 u F) = -delta + |F|.

## 4. Lemma G (budget and greedy)

Suppose Delta := 2g + 2 - Phi(Z0) >= 1.  Then Delta <= 2 - 2m + L_Z <= L_Z, where
L_Z := sum_{anti in Z0} (1 + c_t) + #pairs in Z0 <= 2B, so j := ceil(Delta/2) <= B.  If such
an F exists with |F| = j, then P* := Z0 u F has Phi(P*) >= 2g + 2 and BH(P*) <= -delta + B <= B.
Order the elements of P*: first Z0 (any order), then F.  Adding one element changes Phi by
at most f_t + 2 <= 2g (defects) or d_t + 1 <= 2g (fillers).  So the shortest prefix P with
Phi(P) >= 2g + 2 has Phi(P) <= 4g + 1, BH(P) <= B and D_P >= -B.  It is proper, because the
end runs of every gap are not in P*.  By Lemma K and its Corollary, v has an identity
2p-subword.  If Delta <= 0, take P* = Z0.

## 5. Lemma AV (enough fillers outside the residual case)

Write the cycle as Z_1 G_1 ... Z_m G_m, with defect blocks Z_i and gaps G_i of lengths
l_i >= 1.  The interior of G_i consists of its runs other than the two end runs.  A
blocker is an interior run that is anti, a pair, or has bh >= 2; there are at most
exc + #AP_Y blockers.  On a path, any set S of vertices contains a pairwise non-adjacent
subset of size ceil(|S|/2): take every other element of S.  The interior fillers of
different gaps are never adjacent.  Hence the number of available fillers is
  phi >= sum_i (l_i - 2 - b_i)/2 >= (|Y| - 2m - exc - #AP_Y)/2.
phi >= ceil(Delta/2) follows from |Y| - 2m - exc - #AP_Y >= 3 - a_Z - exc - 2m, that is,
from
  |Y_al| + a_Z >= 3   (Y_al := aligned runs in Y).
Under this condition no aligned bh = 1 run has d_t >= 2p - 1: such a run would carry all of
A, all other runs would be anti, Y_al would be that run alone, and a_Z = -L_Z <= -2.
**Theorem MIX-R.**  MIX_low(p) holds for every avoider configuration with
Phi(Z0) >= 2g + 2 or |Y_al| + a_Z >= 3 (proof: Sec. 1-5).

## 6. Open: the residual case R*

R*: Phi(Z0) <= 2g + 1 and |Y_al| + sum_{Z0} (d_t - 1) <= 2.  Then there are at most
2 + L_Z <= 2 + 2B aligned non-defects.  Since exc <= 1 - a_Z - 2m <= 2B - 1, at most one of
them has d >= 2g + B - 1.  Almost all aligned runs are d = 1 or d = 2 defects.
Evidence [F], an aid only:
* An ILP (scipy milp, single process) over 1,482,446 random residual structures (d, Z)
  with p <= 31, 1 <= g <= 4, 1 <= B <= 4 and k in [2g+2B+2, 2g+3B+4] found no integer bh
  satisfying all interval bounds, sum bh = k - 2g and Phi(Z) <= 2g + 1.  So the bh
  constraints of R* were infeasible in every sampled structure.
* Every interval-feasible solution with Phi(Z0) < 2g + 2 found so far (record-Z0-rule-
  counterexample.md and the structured searches) has many fillers and |Y_al| + a_Z >= 3.
Failed approaches: defect-only Z0 (false: the [F] record); crude counting without the
exact identity delta = 2g + exc - |Z0| (needed k >= 2g + 3B + 2).
