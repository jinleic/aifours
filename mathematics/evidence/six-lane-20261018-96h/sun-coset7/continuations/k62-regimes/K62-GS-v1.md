# K62-GS-v1 (standalone): in the generic sub-case G every 4-subset of O has raw depth <= 4, and G is empty for every e_d >= 4 [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:53:31-0700.
- **Author:** SunK62Regimes; single author; written mathematics only. No computation of any kind was run for this file
  (no compute GO; global runtime HOLD respected). **Label of every new claim: CANDIDATE_UNVERIFIED.**
- **Frozen scope (written before the derivation):** `K62-GS-SCOPE-v1.md` in this directory, sha256
  cdd5f84a27f22661e479c5d8fc9b8713a62273afd758b2f192530eae9a6fc0d7. Theorems FB, GE and Corollary OM below are its section 2.
- **Standalone.** Only parent-accepted results are imported (section 1), at their original scopes. This file does **not**
  import `K62-HD-v1.md`/`K62-HD-v2.md` (Theorem HD or any of its lemmas), the parent HD erratum, or `K62-GX-v1.md`; every
  fact needed from them is proved again below. Those files stay unchanged; their relation to this one is navigation only
  (section 7). The parent's IRC branch hint was treated as untrusted; every branch is derived here.
- RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`;
  K62 := `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon`.

## 0. Setting and notation
**Class** (the setting of the accepted CAP-DT verdict `RUN/review/sun7-K62-CAP-DT-parent-verdict-v1.md`, sha256
84061c6fbdbd9fa834810efa43843024e04c2abce794df28446865ef635234a0). V = {d, i*} disjoint-union O, |O| = 5;
n_d = 2^(e_d) 5^(h_d) w_d with e_d >= 4 (hence e* = 2); n_(i*) = 4 * 3^(f*) 5^(h*) w_*; n_c = 2 * 3^(f_c) 5^(h_c) w_c (c in O);
the w's are pairwise coprime and coprime to 30; at most one vertex has f >= 2 and at most one has h >= 1.
**G** (that verdict, item 6): no vertex of O carries a marker, i.e. **n_c = 6 w_c for every c in O**; the 3-marker is on i*
(any f* >= 2) or absent (f* = 1); the 5-marker is on d (any h_d >= 1), on i* (any h* >= 1), or absent. As no 3-marked vertex
lies in O, K62-E3 Lemma 1 gives **(alpha_(d i*), alpha*_(d i*)) = (1, 1)**.

**Families.** For x in {alpha, alpha*}, x' is the other one. The *x-configuration* is (g_jU_j) if x = alpha and the
inverted configuration (g_j^-1 U*_j), U*_j := g_jU_jg_j^-1, if x = alpha*: a family of pairwise disjoint left cosets with
the same indices whose alpha-matrix is x and whose alpha*-matrix is x' (INV (a)-(b) with E6; inverting twice returns the
original configuration). Phi_j is the subgroup of vertex j in the x-configuration (U_j, resp. U*_j). Thus
[G : Phi_j] = n_j and [G : Phi_i cap Phi_j] = lcm(n_i, n_j) x_ij.
For non-empty S contained in O: W_S := intersection of the Phi_j (j in S); T_x(S) := [G : W_S]; **raw depth**
delta(S) := v2 T_x(S); capped depth min(e_d, delta(S)). For an O-triple R = {a, b, c}: tau(R) := T_x(R) / lcm(n_a, n_b, n_c)
(a positive integer, Lagrange); the **type** of R is its sorted x-values; R is **deep** if delta(R) >= 4.
X^v_j := Phi_vPhi_j. mu(Y) := |Y| / |G| in a finite group G. **L0.1** (old README section 0): |XY| = |X||Y| / |X cap Y| for
subgroups X, Y; used with Lagrange. So mu(Phi_iPhi_j) = [G : Phi_i cap Phi_j] / (n_i n_j) = x_ij / g_ij (the L0.3 identity).
For a 4-subset Q of O and e in Q: R_e := Q minus {e}, m_e := min over j in R_e of x_ej, and k_e := the multiplier of P3 below
for S = R_e.

## 1. Imports (parent-accepted; original scopes)
| tag | source (verdict path, sha256, item) | used for |
|---|---|---|
| R0, L0.1 | old README (`six-lane-20261016/sun-coset7/README.md`) sections 0-1; accepted verdict 73a25ba6… | finite reduction; product formula |
| E3-L1 | RUN/review/sun7-K62E3-parent-verdict-v1.md `576969dd…bb0f`; K62-E3 Lemma 1 | both distinguished entries 1 in G |
| E3-a | same verdict; K62-E3 C2 sub-claim (a) (erratum v2 Z11) | every O-O value of alpha and alpha* lies in {1, 2, 4} |
| E3-C2 | same verdict; K62-E3 Corollary C2 (Z11): for alpha* when alpha_(d i*) = 1, for alpha when alpha*_(d i*) = 1 | n_4(y) >= 2 n_1(y) + 2, both families in G |
| INV | RUN/review/sun7-lfc-inv-parent-verdict-v1.md `8621e744…cca18`, item 2; K7-LFC-INV-v1 §2 with erratum E1, E6, E7 | alpha + alpha* <= g; inverted configuration; VFC integer q = alpha* |
| L1, VFC | rules-k7-v1.md L1 (T3) and §2 (V1)-(V4); RUN-2026-10-16 verdict `73a25ba6…9f35` line 23 | P4 (also re-derived); Lemma EQ |
| APEX, DG-3 | CAP-DT verdict `84061c6f…34a0` item 5 (DT-A §1 table, both families, admissible only); SH-DG verdict `cae455c3…ddda` item 3 (DG-3, erratum G3) | P2 (also re-derived) |
| DG-4 | SH-DG verdict item 3 (K62-DG §3, erratum G4; unmarked added vertex, raw depths) | P3 is DG-4 written out with its equality case |
| CI | CAP-DT verdict item 5 (DT-A §2; v in O unmarked; the family's own distinguished entry 1) | both-tight case of Lemma EQ |
| R4, B1, B3, B5 | CAP-DT verdict item 6 (DT-B (R4) in its CD13 positive-support form; B1; B3; B5's edge-disjointness computation), in G | Lemma DEG; Theorem GE step 2 |
| C2deg | CAP-DT verdict item 6 (DT-C C2, minimum degree) | Lemma DEG |
| DG | SH-DG verdict item 4 (Theorem DG (a)/(b), orientation, four-subset hypothesis) | Lemma DEEP |
Nothing else is imported. No M13, O-marked or K7 material is used.

## 2. Basic facts (each proved here; the accepted sources are cited for cross-checking)
**P1 (O-values).** For an O-pair uv and both families, x_uv lies in {1, 2, 4} (E3-a) and x_uv + x'_uv <= 6 (INV (b), g_uv = 6).
Hence: H_x, the graph on O of the pairs with x = 4 (*x-4-edges*), and H_x' are **edge-disjoint**; for an x-4-edge,
x' is 1 (**non-tight**) or 2 (**tight**). n_k(x) := number of O-pairs with x = k; u(x) := number of non-tight x-4-edges;
t(H_x) := number of triangles of H_x (O-triples of type (4,4,4)).

**P2 (triangles; DG-3 and the DT-A table).** For an O-triple R = {a, b, c} with sorted x-values x1 <= x2 <= x3:
T_x(R) = 6 w_a w_b w_c tau(R), so **delta(R) = 1 + v2 tau(R)**; **tau(R) is a multiple of lcm(x1, x2, x3)** and
**tau(R) <= x1 x2**. Hence the admissible values: (1,1,1): tau 1; (1,2,2): 2; (1,4,4): 4; (2,2,2): 2 or 4; (2,2,4): 4;
(2,4,4): 4 or 8; (4,4,4): 4, 8, 12 or 16; (1,1,2), (1,1,4), (1,2,4): none. **R is deep iff it has type (2,4,4) with tau 8,
or type (4,4,4) with tau 8 or 16**; delta(R) = 5 only for (4,4,4) with tau 16; always delta(R) <= 5.
*Proof.* lcm(n_a, n_b, n_c) = 6 w_a w_b w_c (pairwise coprime w's), of 2-adic valuation 1. T_x(R) is divisible by
[G : Phi_a cap Phi_b] = 6 w_a w_b x_ab (Lagrange), so x_ab divides w_c tau(R), hence tau(R) (x_ab is a power of 2, w_c is odd);
likewise for the other pairs. P4 below gives mu(Phi_c(Phi_a cap Phi_b)) = tau(R) / (6 x_ab); this set lies in X^c_a and X^c_b,
of measures x_ca / 6 and x_cb / 6, so tau(R) <= x_ab min(x_ca, x_cb); the minimum over the three apexes is x1 x2. The table
follows; v2 tau >= 3 exactly for tau in {8, 16}. QED

**P3 (chain step with equality case; DG-4 written out).** Let S be a non-empty subset of O.
(a) The prime-to-30 part of T_x(S) is the product of the w_j (j in S), and 6 divides T_x(S).
(b) For e in O minus S: T_x(S + e) = lcm(n_e, T_x(S)) * k with k a positive integer, **k = 6 mu(Phi_e W_S)**, **k <= x_ej**
for every j in S, with **k = x_ej iff Phi_e W_S = X^e_j**, and **delta(S + e) = delta(S) + v2 k**. If m is a power of 2 with
k <= m, then v2 k <= v2 m.
*Proof.* By induction on |S|. For S = {j}: T_x(S) = n_j = 6 w_j. Assume (a) for S and let e be in O minus S. n_e and T_x(S)
divide T_x(S + e) (Lagrange: W_(S+e) lies in Phi_e and in W_S), so T_x(S + e) = lcm(n_e, T_x(S)) k with k a positive
integer. By L0.1, mu(Phi_e W_S) = T_x(S + e) / (n_e T_x(S)) = k / gcd(n_e, T_x(S)). By (a), w_e (coprime to 30 and to every
w_j, j in S) is coprime to T_x(S), so gcd(n_e, T_x(S)) = gcd(6 w_e, T_x(S)) = gcd(6, T_x(S)) = 6, and k = 6 mu(Phi_e W_S).
For j in S, W_S lies in Phi_j, so Phi_e W_S lies in X^e_j, of measure x_ej / 6: k <= x_ej, with equality iff the two finite
sets are equal. As x_ej <= 4 (P1), k <= 4 has no prime factor > 3, so the prime-to-30 part of T_x(S + e) is that of
lcm(n_e, T_x(S)), namely w_e times the product over S; and 6 divides T_x(S + e). This proves (a) for S + e and (b). Since
v2 n_e = 1 <= v2 T_x(S), v2 lcm(n_e, T_x(S)) = v2 T_x(S), so delta(S + e) = delta(S) + v2 k. Finally, if v2 k > v2 m then
k >= 2^(v2 k) >= 2m > m. QED

**P4 (apex identity and apex equality; L1 (T3)).** For an O-triple {a, b, c}:
mu(Phi_b(Phi_a cap Phi_c)) = tau({a, b, c}) / (6 x_ac). Consequently, **if x_ba = x_bc = 4 and tau({a, b, c}) = 4 x_ac, then
X^b_a = X^b_c** (= Phi_b(Phi_a cap Phi_c)).
*Proof.* L0.1: mu(Phi_b(Phi_a cap Phi_c)) = T_x({a, b, c}) / (n_b [G : Phi_a cap Phi_c]) =
6 w_a w_b w_c tau / (6 w_b * 6 w_a w_c x_ac) = tau / (6 x_ac) (this is L1 (T3) with gamma_b = 6). Under the stated
hypotheses this equals 4/6 = mu(X^b_a) = mu(X^b_c); the set lies in both, and finite sets with an inclusion and equal
measures are equal. QED
*Instances (the DT-A §1 table):* type (2,4,4) with tau 8, at the apex opposite the 2-edge; type (4,4,4) with tau 16, at
each of the three apexes.

**P5 = Lemma EQ.** Let v, a, b be distinct vertices of O and x a family with x_va = x_vb = 4 and X^v_a = X^v_b. Then
**x'_va = x'_vb = 1** (both edges are non-tight).
*Proof.* Work in the x-configuration and left-translate all its cosets by the inverse of v's representative (no subgroup,
index or set Phi_vPhi_j changes). VFC at v: for j != v, D_j := Phi_v h_j Phi_j (h_j the translated representative of j)
satisfies (V1) D_j cap X^v_j = empty and mu(D_j) = q_j / g_vj with q_j = x'_vj (INV (b) for the x-configuration, whose
alpha*-matrix is x'); (V4) D_j is left Phi_v-invariant, hence a union of right cosets Phi_v y; (V2) its local index is
d_j = q_j n_j / g_vj; (V3) a right coset lying in D_j and in D_k (j != k) forces gcd(d_j, d_k) >= 2 (|T| = 2, Sun(2)).
By P1, x'_va and x'_vb lie in {1, 2}. Put Y := G minus X^v_a = G minus X^v_b, of measure 2/6.
- Both tight (x'_va = x'_vb = 2): all hypotheses of CI hold (v in O unmarked; x_(d i*) = 1 in G; x_va = x_vb = 4;
  X^v_a = X^v_b; both tight); CI gives a contradiction.
- Exactly one tight, say x'_vb = 2 and x'_va = 1 (a, b symmetric): D_b lies in Y and has measure 2/6 = mu(Y), so D_b = Y;
  D_a lies in G minus X^v_a = Y = D_b and has measure 1/6 > 0, so it contains a right coset R of Phi_v, which then lies in
  D_a and in D_b. But d_a = 1 * 6 w_a / 6 = w_a and d_b = 2 * 6 w_b / 6 = 2 w_b are coprime: contradiction with (V3).
Hence both edges are non-tight. QED

**P6 = Lemma BUD.** For each family x: **n_4(x) <= 8 - 2 u(x).**
*Proof.* E3-C2 for x' (it needs x_(d i*) = 1, true in G): n_4(x') >= 2 n_1(x') + 2. Each non-tight x-4-edge has x' = 1, so
n_1(x') >= u(x). Edge-disjointness (P1): n_4(x) + n_4(x') <= 10. So n_4(x) <= 10 - 2 n_1(x') - 2 <= 8 - 2 u(x). QED

**P7 = Lemma DEG.** For each family x: every vertex of O has H_x-degree >= 1 and <= 3; H_x contains no K4 and no two
triangles sharing exactly one vertex.
*Proof.* Degree >= 1: DT-C C2 (accepted); directly, a vertex v of H_x-degree 0 would have its four O-entries of the x-row in
{1, 2} (P1), which DT-B (R4) forbids in G (its 5/6 bound is RC-O: v unmarked, x'_(d i*) = 1; CD13 gives the positive-support
certificate, valid also for h_d >= 1). Degree <= 3 is B1; no K4 and no bowtie is B3. QED

## 3. Three lemmas on triples and graphs
**3.1 Lemma T16.** In G, for both families, **no O-triple has type (4,4,4) with tau = 16.** Hence (P2) every O-triple has
raw depth <= 4, and an O-triple is deep iff it has type (2,4,4) or (4,4,4) with tau = 8.
*Proof.* If R = {a, b, c} has type (4,4,4) and tau 16, P4 at each apex gives X^a_b = X^a_c, X^b_a = X^b_c, X^c_a = X^c_b, and
EQ at each apex makes ab, ac, bc non-tight: u(x) >= 3, so n_4(x) <= 2 (BUD), while ab, ac, bc are three x-4-edges. QED

**3.2 Lemma ONE.** For each family x, **at most one O-triple has type (2,4,4) with tau = 8**; if one exists, u(x) >= 2 and
n_4(x) <= 4.
*Proof.* For such a triple {v, a, b} (x_ab = 2, x_va = x_vb = 4, tau 8), P4 at v gives X^v_a = X^v_b and EQ makes va, vb
non-tight; so u(x) >= 2 and n_4(x) <= 4 (BUD). Two distinct such triples R_1, R_2 have edge pairs E_1, E_2 (the two
x-4-edges of R_i, both non-tight); R_i is the set of endpoints of E_i, so E_1 != E_2 and |E_1 cup E_2| >= 3. Then u(x) >= 3 and
n_4(x) <= 2 < 3 <= n_4(x). QED

**3.3 Lemma TRI.** A graph on a 5-set with maximum degree <= 3, no K4 and no two triangles sharing exactly one vertex has at
most two triangles, and two of its triangles share an edge (so it then contains a diamond, i.e. K4 minus an edge).
*Proof.* Two triangles in a 5-set share a vertex (3 + 3 > 5), hence exactly two vertices. Let T_1 = {p, q, r} and
T_2 = {p, q, s}, and suppose a third triangle T_3. If T_3 contains p and q, T_3 = {p, q, y} with y not in {r, s}, and p has
neighbours q, r, s, y: degree 4. Otherwise T_3 shares exactly one of qr, pr with T_1; by the symmetry p <-> q say qr, so
T_3 = {q, r, y}, y != p. T_3 shares an edge with T_2: not qr or ry (r is not in T_2), so qy, i.e. y = s, T_3 = {q, r, s}, and
{p, q, r, s} spans pq, pr, qr, ps, qs, rs: a K4. Both contradict the hypotheses. QED

## 4. Theorem FB (four-subset bound) [NEW; CANDIDATE_UNVERIFIED]
**Statement.** In G (any e_d >= 4 and every admissible f*, h_d, h*, w), for both families x and every 4-subset Q of O:
**delta(Q) = v2 T_x(Q) <= 4.**
*Proof.* Fix x and suppose delta(Q) >= 5. For e in Q, P3 (S = R_e) gives
  **(N_e)** delta(Q) = delta(R_e) + v2 k_e, with 1 <= k_e <= m_e and v2 k_e <= v2 m_e (m_e is a power of 2, P1).
(i) *No pair of Q has x = 1.* By T16, delta(R_e) <= 4, so (N_e) gives v2 k_e >= 1, hence m_e >= k_e >= 2, for every e in Q.
If x_ab = 1 for a, b in Q, then m_a <= 1. So the six pairs of Q have x in {2, 4}.
(ii) They are not all x-4-edges (H_x has no K4, DEG). Let N be the non-empty set of pairs of Q with x = 2 and I the set of
their endpoints (|I| >= 2).
(iii) For v in I: m_v = 2 (an N-edge at v, and (i)), so v2 k_v <= 1 and (N_v) gives delta(R_v) >= 4: R_v is deep, so by T16
it has type (2,4,4) or (4,4,4), with tau = 8. The pairs of R_v with x = 2 are the N-edges not containing v. So at most one
N-edge avoids v, and exactly one does iff R_v has type (2,4,4).
(iv) Distinct v give distinct R_v, so by ONE at most one v in I has R_v of type (2,4,4); every other v in I lies on every
N-edge. If |I| >= 3, two distinct vertices of I lie on every N-edge, so N consists of the single pair they form and |I| = 2,
a contradiction. Hence N = {ab} for one pair, and with Q = {a, b, c, q} the pairs ac, aq, bc, bq, cq are x-4-edges.
(v) R_b = {a, c, q} has type (4,4,4) and is deep by (iii), so tau(R_b) = 8 and delta(R_b) = 4. Then (N_b) gives v2 k_b >= 1,
and k_b <= m_b = min(x_ba, x_bc, x_bq) = 2, so k_b = 2 = x_ba; by the equality case of P3, Phi_b W_(R_b) = X^b_a, of measure
2/6. For j in {c, q}: W_(R_b) lies in Phi_a cap Phi_j, so Phi_b W_(R_b) lies in Phi_b(Phi_a cap Phi_j), and P4 gives
tau({a, b, j}) / (6 x_aj) = tau({a, b, j}) / 24 >= 2/6, i.e. tau({a, b, j}) >= 8. The triple {a, b, j} has type (2,4,4)
(x_ab = 2, x_aj = x_bj = 4), so tau({a, b, j}) = 8 (P2). Thus {a, b, c} and {a, b, q} are two distinct O-triples of type
(2,4,4) with tau = 8, contradicting ONE. QED

## 5. Lemma DEEP and Theorem GE [NEW; CANDIDATE_UNVERIFIED]
**Lemma DEEP.** For each family x and every e_d >= 4: **at least two O-triples have type (2,4,4) or (4,4,4) with tau = 8.**
*Proof.* Theorem DG applies to alpha* (alpha_(d i*) = 1) and to alpha (alpha*_(d i*) = 1); its four-subset hypothesis (every
4-subset Q of O has capped depth min(e_d, delta(Q)) <= 4) holds by Theorem FB. DG (b) gives an O-triple of capped depth
>= 4, and if only one O-triple has capped depth >= 4, its capped depth is 5, so its raw depth is >= 5, contradicting T16.
So at least two O-triples have capped depth >= 4, hence raw depth >= 4; by T16 they have the stated types with tau = 8. QED

**Theorem GE.** **G is empty:** no K6.2* configuration in a finite group lies in G, for any e_d >= 4 and every admissible
f*, h_d, h* and w-parts (all exponents unbounded). By R0 (the finite-core quotient preserves indices, intersection indices
and disjointness; accepted LFC/INV verdict item 6) the same holds for arbitrary groups with finite-index subgroups.
*Proof.* **Step 1: for each family x, H_x contains a diamond.** By DEEP, at least two O-triples have type (2,4,4) or (4,4,4)
with tau = 8. Those of type (4,4,4) are triangles of H_x: at most t(H_x) of them. Those of type (2,4,4): at most one (ONE).
H_x satisfies the hypotheses of TRI (DEG), so t(H_x) <= 2. If t(H_x) <= 1, then 2 <= t(H_x) + 1 forces t(H_x) = 1 and a
(2,4,4) triple with tau 8, so n_4(x) <= 4 (ONE). Let {p, q, r} be the triangle and {s, f} := O minus {p, q, r}. By DEG, s and f
have H_x-degree >= 1, and at most one x-4-edge lies outside the triangle; so H_x = {pq, qr, rp, sf}. Any two x-4-edges with a
common vertex then lie in the triangle, so the only O-triple containing two x-4-edges is {p, q, r}, of type (4,4,4): no
O-triple has type (2,4,4), a contradiction. Hence t(H_x) = 2, and by TRI H_x contains a diamond.
**Step 2 (B5).** By Step 1, H_alpha contains the five edges ac, aq, bc, bq, cq of a diamond on {a, b, c, q} (missing ab). By
edge-disjointness (P1), H_alpha* lies in {ab, ae, be, ce, qe}, e the fifth vertex of O, whose only triangle is {a, b, e} (c
and q have degree 1 there). So t(H_alpha*) <= 1, contradicting Step 1 for alpha*. QED

## 6. Corollary OM [NEW; CANDIDATE_UNVERIFIED]
**Every K6.2* configuration (any group, finite-index subgroups) has a marker on a vertex of O:** some c in O has f_c >= 2 or
h_c >= 1.
*Proof.* By accepted K62-E3, e_d >= 4 and e* = 2. If no vertex of O is marked, the 3-marker is not on d (f_d = 0), so it is
on i* or absent, and the 5-marker is on d, on i* or absent: the configuration lies in G, contradicting Theorem GE. QED
*Navigation only:* the K6.2* cases left open are those with the 3-marker t in O (orientations (1,1), (1,3), (3,1); the
last two are M13, owned elsewhere) or the 5-marker p in O. K7 and Sun(7) are untouched.

## 7. Scope, dependency order, provenance, checks
- **Dependency order (acyclic):** P1-P4 (elementary, with accepted cross-references) -> EQ (VFC, INV, CI) -> BUD (E3-C2)
  -> DEG (R4, B1, B3) -> T16, ONE, TRI -> FB (uses P3, P4, T16, ONE, DEG; not DG) -> DEEP (DG + FB + T16) -> GE (DEEP, ONE,
  TRI, DEG, P1) -> OM (E3).
- **Claims:** Theorems FB and GE and Corollary OM, exactly in the stated settings, with all exponents unbounded. Not claimed:
  any O-marked case, M13, K7, Sun(7), realisability of any pattern, and no promotion of the pending HD or GX v1 candidates.
- **Unused:** f* = 1, (RC-i*), C2 at i*, i*-row and d-row counts beyond those inside the cited imports; so the 3-marker on i*
  (any f*) and the 5-marker on d or i* (any exponent) are covered by the same text.
- **Relation to older files (navigation, not premises):** Theorem FB has the statement of Theorem HD (`K62-HD-v2.md`), with
  a different proof (T16 and ONE replace HD's Cases A, B1-B4); Theorem GE is K62-GX-v1's Theorem GX without its HD
  condition. Whether this file supersedes them is the parent's decision.
- **Sun provenance.** Direct new Sun instance: Sun(2) (EQ). Through imports: Sun(2), Sun(3) (CI, (R4)), Sun(4) (K62-E3). The
  accepted LFC/VFC package cites Sun(t), t <= 6, and the K6.2* class reduction uses the computer-assisted Sun(5) (verdict
  2cf02436…5301) and Sun(6) (verdict efe1d849…1e29); both remain in the transitive import closure.
- **Mutation checks for reviewers (thought experiments; nothing run):** (1) without T16, FB (i) fails (a tau-16 triple
  allows v2 k_e = 0) and DEEP keeps DG (b)'s single capped-depth-5 alternative; (2) without ONE, FB (iv)-(v) and GE Step 1
  lose their contradictions; (3) with CI' in place of EQ (one non-tight edge per forced apex), T16 and ONE are no longer
  proved; (4) without minimum degree, H_x = triangle {p, q, r} (tau 8) plus the edge rs, with x_sp = 2 and
  tau({r, s, p}) = 8, passes DEEP, ONE and BUD (u = 2, n_4 = 4); (5) without edge-disjointness, both families could carry
  diamonds.
- No computation, enumeration, novelty, priority, Lean or human-review claim.
