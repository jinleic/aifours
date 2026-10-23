# Addendum 2 to proof-LSplus-red-v1.md: case (alpha) with a = -1/2 is impossible for e >= 3 and prime p >= 10e - 13

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T06:44:37-0700.  Status: CANDIDATE [W], UNREVIEWED.  Applies to proof-LSplus-red-v1.md
(166fbac828e7e55a8f2139648930c82c5df1e8823bf9d8c4f84daf36086b4c27), Theorem LS+-RED (A), (B).  Same dependencies as that file: Lemma CF (proof-CF-XT-v1.md with the
accepted errata, parent verdict run review/olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0); Lemma CT
(proof-LSplus-e2-v1.md 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1) and Lemma CTgen (lemma-CTgen-v1.md 462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad), both CONDITIONAL until
their parent verdict; parent-accepted SLZ3 (2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24); the index-one record (e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6) with n = p.
No new import.  Addendum 1 is not used.  LS+ and STAB are not assumed.  No computation.

## 0. Setting and notation
p prime, kappa0 + 1 <= kappa <= p - 2, e := p - kappa >= 3, p >= 10e - 13.  For prime p and e >= 3 this is equivalent to p >= 10e - 16
(10e - 16 and 10e - 14 are even, 10e - 15 = 5(2e - 3) with 2e - 3 >= 3), and it implies p >= 9e - 13, so LS+-RED applies.
From LS+-RED (A), (B) in the case a = -1/2: Y odd, |Y| = 3kappa + 2, (ZP_kappa), a zero-sum of length >= 2p + 2; g a generator,
M = v_g(Y) = 2p - delta0, 1 <= delta0 <= 3e - 4; U the CF mu-multiset of the other terms, r = |U| = p - 3e + 2 + delta0 <= p - 2;
Z0 <= U an inclusion-maximal mod-p zero-sum, |Z0| <= delta0 - 1, delta' := delta0 - |Z0| >= 1; U' := U - Z0 with mu_u = -x_u/2 (mod p),
integers x_u >= 1, S' := sum x_u <= p - 1, |U'| = p - 3e + 2 + delta', E' := S' - |U'|, delta' + E' <= e - 1.
- For every term w of U put xi_w := -2mu_w (mod p), and for W <= U let t(W) in [0, p - 1] be the least residue of sum_W xi.
  Then sigma(W) = -t(W)/2 (mod p).  For u in U', xi_u = x_u (mod p).  A term w has xi_w = 1 iff mu_w = (p - 1)/2 iff w = p.g = p, the
  involution (c = 2mu + 1 = p); so the u in U' with x_u = 1 are copies of the involution.
- n_P := #{u in U' : x_u = 1}.  As #{u in U' : x_u >= 2} <= E' <= e - 1 - delta', n_P >= |U'| - E' >= p - 4e + 3 + 2delta' >= p - 4e + 5.
- A := p - 2e + 1 - n_P (so A <= e - 1 - delta' + E' <= 2e - 2 - 2delta').  Theta := {p - 2e + 2, p - 2e + 4, ..., p}: the e odd integers
  theta with (p - theta)/2 in [0, e - 1].

## 1. (F*) and (L) in t-form
(F*) (LS+-RED Sec. 3, as r <= p - 2): every W <= U with rho(W) <= e - 1 has |W| + 2rho(W) <= delta0 - 1.  Now rho(W) = 0 if t(W) = 0,
(p - t)/2 if t is odd, and p - t/2 >= (p + 1)/2 > e - 1 if t >= 2 is even.  So (F*) says exactly:
  (F0) t(W) = 0  implies  |W| <= delta0 - 1;
  (Fo) t(W) odd and t(W) >= p - 2e + 2  implies  |W| + p - t(W) <= delta0 - 1.
(L*) Y has a zero-sum of length >= 2p + 2 iff some W <= U has t(W) even and 2 <= t(W) <= |W| - delta0 (it then has length 2p + t(W)).
Proof.  CF (b) (M <= 2p - 1): such a zero-sum exists iff some W <= U and integer j >= 1 have p | sigma(W) + j and
delta0 + 2j <= |W| <= 2p + 2j; its length is 2p + 2j.  As |W| <= r < p, rho(W) = 0 is impossible (it forces j >= p), and otherwise
the least admissible j is p - rho(W), so the condition is |W| + 2rho(W) >= 2p + delta0.  For t(W) odd this reads
|W| >= p + t(W) + delta0 > r: impossible.  For t(W) even >= 2 it reads t(W) <= |W| - delta0, with j = t(W)/2.  []

## 2. Lemma 0 (involutions as units)
Let V <= Z0 and tau0 an integer with tau0 = sum_V xi (mod p) and A + 1 <= tau0 <= p.  Then |V| + p - tau0 <= delta0 - 1.
Proof.  [tau0, tau0 + n_P] contains some theta in Theta: if tau0 <= p - 2e + 2 take theta := p - 2e + 2 (odd, and <= tau0 + n_P as
tau0 >= A + 1); otherwise one of tau0, tau0 + 1 is odd and lies in [p - 2e + 3, p] (n_P >= 1).  Put s := theta - tau0 in [0, n_P] and
W := V u P^s, P^s being s copies of the involution taken from U'.  Then sum_W xi = tau0 + s = theta (mod p).  If theta = p: t(W) = 0
and (F0) gives |W| = |V| + p - tau0 <= delta0 - 1.  If theta <= p - 2: t(W) = theta is odd and >= p - 2e + 2, and (Fo) gives
|W| + p - theta = |V| + p - tau0 <= delta0 - 1.  []

## 3. Theorem LS+-RED-c
In the setting of Sec. 0 (e >= 3, prime p >= 10e - 13), case (B) with a = -1/2 does not occur.
Proof.
Step 1 (Z0 splits).  For z in Z0 let zeta_z in [1, p - 1] be the least residue of xi_z (xi_z != 0, as mu_z != 0).  If zeta_z >= A + 1,
Lemma 0 (V = {z}, tau0 = zeta_z) gives zeta_z >= p + 2 - delta0.  So z is POSITIVE (zeta_z <= A) or NEGATIVE
(nu_z := p - zeta_z in [1, delta0 - 2]).  Write Z0+, Z0-; for V <= Z0+ put P_V := sum_V zeta; for V <= Z0- put N_V := sum_V nu and
Omega_V := |V| + N_V.
Step 2 (P_(Z0+) <= max(A, 0)).  If A <= 0, Z0+ is empty.  Let A >= 1 and suppose P_(Z0+) >= A + 1; add the terms of Z0+ one at a time;
the first partial set V with P_V >= A + 1 has P_V <= 2A <= 4e - 4 - 4delta' <= 4e - 8 < p.  Lemma 0 (tau0 = P_V) gives
P_V >= p + 1 + |V| - delta0 >= p + 2 - delta0 >= p - 3e + 6 > 4e - 8 (p >= 7e - 13): contradiction.
Step 3 (Omega_(Z0-) <= delta0 - 1).  For V <= Z0- with N_V <= n_P, W := V u P^(N_V) has sum_W xi = sum_V (p - nu) + N_V = 0 (mod p), so
(F0) gives Omega_V = |W| <= delta0 - 1.  Suppose Omega_(Z0-) >= delta0; add the terms of Z0- one at a time; the first partial set V
with Omega_V >= delta0 has Omega_V <= (delta0 - 1) + (delta0 - 1) (each 1 + nu_z <= delta0 - 1), so
N_V = Omega_V - |V| <= 2delta0 - 3 <= 6e - 11 <= p - 4e + 5 <= n_P (p >= 10e - 16): contradiction.
Step 4 (no long zero-sum).  Let W <= U, W = W' u V+ u V- with W' <= U', V+ <= Z0+, V- <= Z0-, and put tau := X(W') + P_(V+) - N_(V-),
X(W') := sum_(W') x_u; tau is an integer and tau = sum_W xi (mod p).
- tau <= p - 3: if A <= 0, tau <= S' = |U'| + E' <= p - 2e + 1; if A >= 1, tau <= S' + A = p - 2e + 1 + sum over u with x_u >= 2 of x_u
  <= p - 2e + 1 + 2E' <= p - 3 (x <= 2(x - 1) for x >= 2; E' <= e - 1 - delta' <= e - 2).
- tau >= -N_(V-) >= -(delta0 - 2) (Step 3: N_(V-) <= Omega_(V-) - |V-|; if V- is empty, tau >= 0).
- If tau >= 0: t(W) = tau >= |W'| + |V+| - N_(V-) = |W| - Omega_(V-) >= |W| - delta0 + 1 (x_u >= 1, zeta >= 1, Step 3).
- If tau < 0: t(W) = p + tau >= p - delta0 + 2 >= p - 3e + 6 > p - 3e + 2 = r - delta0 >= |W| - delta0.
In both cases t(W) > |W| - delta0, so (L*) fails for every W <= U: Y has no zero-sum of length >= 2p + 2, a contradiction.  []

## 4. Remark (even involution deletion; an independent partial criterion, not used in Sec. 3)
In the setting of LS+-RED (B) with a = -1/2 (any p >= 9e - 13): if W <= U satisfies (L*) with t := t(W), then W contains at most t - 1
involutions (removing t of them gives t = 0 and size |W| - t >= delta0, against (F0); in zero-sum terms, a zero-sum of length 2p + t
minus t involutions, t even, is a zero-sum of length 2p).  Hence W has at least |W| - (t - 1) >= delta0 + 1 terms other than the
involution.  U has at most |Z0| + E'' such terms, E'' := #{u in U' : x_u >= 2} <= E'.  So a long zero-sum forces E'' >= delta' + 1, and
the case a = -1/2 with E'' <= delta' is excluded for every p >= 9e - 13 by this criterion alone.

## 5. Exact scope; retained cells
- Theorem LS+-RED-c: e >= 3 and prime p >= 10e - 13 (equivalently p >= 10e - 16), sequence level, relative to the dependencies above.
- RETAINED (not decided) inside LS+-RED's own range p >= 9e - 13: the case a = -1/2 with E'' >= delta' + 1 for primes
  9e - 13 <= p <= 10e - 17; the first instances are (p, e) = (23, 4), (41, 6), (43, 6), (53, 7), (59, 8), (61, 8).  Only Step 3 uses
  p >= 10e - 16 (to have n_P >= 2delta0 - 3); Step 2 needs p >= 7e - 13 and Steps 1, 4 nothing beyond Sec. 0.
- The assembly with LS+2, LS+-RED and addendum 1 is a separate file (proof-LSplus-lin-v1.md).
Credit context [INFERENCE, run review/olson-new-cells-priority-scout-v3.json]: the index-one/greedy inputs of LS+-RED (B) are
Savchev-Chen 2007 Thm 8 / Prop 5; no priority or novelty claim.
