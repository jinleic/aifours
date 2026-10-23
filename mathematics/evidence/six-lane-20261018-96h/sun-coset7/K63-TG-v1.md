# K63-TG-v1: triple granularity, and no K6.3 configuration with an all-3 odd C-vertex [CANDIDATE]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T01:56:16-0700.
- **Status:** candidate for parent review; not accepted. Exploratory support (not a premise):
  `evidence/probe-v16-tg-K63-r1/postrun-v1.json` sha256 1f63a67ce5d9296c117e810508ca1192abf57d4ce57159616f1d5a127b9f2484 (exact LP: with TG the v14 survivors die at every
  odd C-vertex).
- **Premises:** accepted rules-k7-v1 items L1 (T rule with tau_min, tau_max), VFC (V1), (V3), (V4) as used in the
  accepted `K7-Z2-v1.md` section 5 (normalise g_v = 1; X_j = U_v U_j, Y_j = G \ X_j, D_j = U_v g_j U_j;
  D_j subset Y_j; mu(X_j) = alpha_vj / g_vj; mu(D_j) = alpha*_vj / g_vj by INV; tight edge => D_j = Y_j; every right
  coset R of U_v has an allowed index set S_R = {j : R subset D_j} for the labels lambda*_j = n_j alpha*_vj / g_vj;
  the union of the D_j avoids U_v); accepted Lemma INV (`K7-LFC-INV-v1.md`). G may be taken finite.

## 1. Lemma TG (triple granularity) [NEW]
For a vertex v and three other vertices a, b, c, put W = U_a cap U_b cap U_c and T = [G : W]. Then
**mu(X_a cap X_b cap X_c) >= 1 / gcd(n_v, T).**

*Proof.* U_v W is contained in U_v U_a, U_v U_b and U_v U_c. Its measure is |U_v| |W| / (|U_v cap W| |G|) =
Q / (n_v T) with Q = [G : U_v cap W]. Q is a multiple of n_v and of T, hence of lcm(n_v, T), so
mu(U_v W) >= lcm(n_v, T) / (n_v T) = 1 / gcd(n_v, T). QED

In complements: mu(Y_a cup Y_b cup Y_c) <= 1 - 1 / gcd(n_v, T). (The pair version, with I_ab in place of T, is the
granularity already used by Ppair.)

## 2. Theorem K63-CLIQUE [NEW]
In class K6.3 (C = {i*, c1, ..., c5} or any C with at most one even cofactor, d with n_d = 3 r_d odd, g = 6 in C,
g_cd = 3), there is no configuration with a C-vertex v such that r_v is odd and **alpha_vc = alpha*_vc = 3 for every
c in C \ {v}**. In particular the three canonical patterns of `evidence/probe-v14-exact-K63-r1` are impossible.

*Proof.* Fix such a v and normalise g_v = 1.

(i) *Granularity.* For a triple {a, b, c} in C \ {v}, L = lcm(n_a, n_b, n_c) = 6 r_a r_b r_c and T = L tau. By L1,
tau <= gamma_y alpha_xz min(alpha_xy / g_xy, alpha_yz / g_yz) = 6 * 3 * (1/2) = 9. T is a multiple of every pair index
I_xy = lcm(n_x, n_y) * 3 = 18 r_x r_y, hence of 18 r_a r_b r_c = 3 L, so 3 | tau and tau in {3, 6, 9}. Therefore
gcd(n_v, T) = gcd(6 r_v, 6 r_a r_b r_c tau) = 6 gcd(r_v, tau r_a r_b r_c) = 6, because r_v is odd, prime to 3 (the
3-marker, if any, is on d or on another vertex... more precisely 3 does not divide r_v unless v carries the 3-marker;
see the remark below) and prime to the other cofactors. By Lemma TG: **mu(Y_a cup Y_b cup Y_c) <= 5/6.**

(ii) *Tight C-edges.* alpha_vc + alpha*_vc = 6 = g_vc, so D_c = Y_c and mu(D_c) = 1/2 for the five c in C \ {v}.

(iii) *Allowed sets.* lambda*_c = n_c * 3 / 6 = 3 r_c for c in C \ {v}, and lambda*_d = n_d alpha*_vd / 3 with
alpha*_vd in {1, 2} (INV (b): alpha_vd + alpha*_vd <= 3). All pairwise gcds among these labels equal 3, except
gcd(lambda*_d, lambda*_(i*)) = 6 when alpha*_vd = 2 (the only even cofactor is r_(i*); the 5-marker lies on at most one
vertex). Hence by Sun(t) for local indices: an allowed S_R contains at most three elements of C, and if it contains
three elements of C and also d, then S_R = {d, i*, x, y} with alpha*_vd = 2.

(iv) *Counting.* Let m_k be the measure of the union of the right cosets R with |S_R cap C| = k (k = 1, 2, 3; k <= 3 by
(iii)). Then m_1 + 2 m_2 + 3 m_3 = sum_c mu(D_c) = 5/2. Summing (i) over the 10 triples of C \ {v}, a coset with
|S_R cap C| = k is counted 10 - C(5 - k, 3) times, i.e. 6, 9, 10 times for k = 1, 2, 3:
6 m_1 + 9 m_2 + 10 m_3 <= 10 * 5/6 = 25/3. Substituting 10 m_3 = (10/3)(5/2 - m_1 - 2 m_2) gives
25/3 + (8/3) m_1 + (7/3) m_2 <= 25/3, so m_1 = m_2 = 0 and the union of the D_c (c in C \ {v}) has measure m_3 = 5/6,
every coset in it lying in exactly three D_c.

(v) *The vertex d.* mu(D_d) = alpha*_vd / 3. A coset R in D_d and in the union of the D_c has |S_R cap C| = 3 and
d in S_R, so by (iii) S_R = {d, i*, x, y}, alpha*_vd = 2 and R is in D_(i*). If alpha*_vd = 1, D_d is disjoint from
that union and the union of all D_j has measure >= 5/6 + 1/3 > 1. If alpha*_vd = 2, D_d minus the union has measure
>= 2/3 - mu(D_(i*)) = 2/3 - 1/2 = 1/6, and the union of all D_j has measure >= 5/6 + 1/6 = 1. Both contradict (V4):
the union avoids U_v and has measure <= 1 - 1/n_v. QED

*Remark on the 3-marker.* If v itself carried the 3-marker then n_d would not be 3 r_d with the stated g's (K6.3 has
g_cd = 3 and the 3-marker on at most one vertex); in the K6.3 residue the 3-marker is on d, so 3 does not divide r_v.
If the 5-marker is on v, r_v = 5^h w_v and gcd(r_v, tau r_a r_b r_c) = 1 still holds (tau in {3, 6, 9}).

## 3. Scope
- Excludes exactly the configurations described in Theorem K63-CLIQUE (any i*, any d-row, any marker placement
  allowed in K6.3 subject to v being a non-i* C-vertex). It does **not** by itself close the K6.3 residue (i* with
  e* = 2 and d with f_d >= 2): other joint patterns may exist; the previous exploratory search (v6b r3) evaluated only
  3 of 27 residue tuples. A follow-up exploratory search with RPLP + TG over all residue tuples is planned.
- Lemma TG is general (any class); it is a candidate premise for the other residues.
