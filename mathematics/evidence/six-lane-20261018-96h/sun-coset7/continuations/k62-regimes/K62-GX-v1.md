# K62-GX-v1: the generic sub-case G of the K6.2* residue is empty (e_d = 4 without HD; e_d >= 5 conditional on HD) [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:45:17-0700.
- **Author:** SunK62Regimes; single author; written mathematics only. No computation of any kind was run for this file
  (global runtime HOLD respected). **Label of every new claim: CANDIDATE_UNVERIFIED.**
- **Frozen scope (written before the derivation):** `K62-GX-SCOPE-v1.md` in this directory, sha256
  56103d95a26e3ace6caed1a9abdf0092c1dcf6b62f2afd2343eba2719f9c16b5. Theorem GX below is its Goal A (parts A4, A5) and
  Corollary OM is the corollary stated there.
- **Conditional premise, used only in part (b) (e_d >= 5):** the statement of Theorem HD of `K62-HD-v2.md` (this
  directory, sha256 6c1858c04d7da52bde8533ba71d4dcea814fb69b30a357462e36024226b9f476), read with the parent erratum
  `RUN/review/sun7-K62-HD-parent-erratum-v1.md` (sha256 3c670e5ff49edfcfd10d4d4ab867f9a7587bd381f5105721d6565cb30d60a2e8).
  HD is a CANDIDATE, not parent-accepted; every use is labelled **CONDITIONAL ON HD**. Nothing else from K62-HD-v2 is
  imported: its Lemma EQ, budget and degree facts are re-proved below (2.3-2.5).
- RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`;
  K62 := `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon`.

## 0. Setting and notation
**Class (CAP section 0, setting of the accepted verdict `RUN/review/sun7-K62-CAP-DT-parent-verdict-v1.md`, sha256
84061c6fbdbd9fa834810efa43843024e04c2abce794df28446865ef635234a0).** V = {d, i*} disjoint-union O, |O| = 5;
n_d = 2^(e_d) 5^(h_d) w_d with e_d >= 4 (hence e* = 2); n_(i*) = 4 * 3^(f*) 5^(h*) w_*; n_c = 2 * 3^(f_c) 5^(h_c) w_c (c in O);
the w's are pairwise coprime and coprime to 30; at most one vertex has f >= 2 and at most one has h >= 1.
**G (that verdict, item 6):** no vertex of O carries a marker, i.e. n_c = 6 w_c for every c in O; the 3-marker is on i*
(any f* >= 2) or absent (f* = 1); the 5-marker is on d (any h_d >= 1), on i* (any h* >= 1), or absent. Since no
3-marked vertex lies in O, K62-E3 Lemma 1 gives **(alpha_(d i*), alpha*_(d i*)) = (1, 1)**.

**Families.** For x in {alpha, alpha*} let x' be the other one. The *x-configuration* is (g_jU_j) for x = alpha and the
inverted configuration (g_j^-1 U*_j), U*_j := g_jU_jg_j^-1, for x = alpha*; its alpha-matrix is x and its alpha*-matrix is
x' (INV (a)-(b) with E6). Phi_j denotes the subgroup of vertex j in the x-configuration (U_j, resp. U*_j). For S contained in
O: W_S := intersection of the Phi_j (j in S), T_x(S) := [G : W_S], **raw depth** delta_x(S) := v2 T_x(S), capped depth
min(e_d, delta_x(S)). For an O-triple R = {a, b, c}: tau_x(R) := T_x(R) / lcm(n_a, n_b, n_c); its **type** is its sorted
x-values. X^v_j := Phi_vPhi_j. mu(Y) := |Y| / |G| in a finite group G; L0.1 (old README section 0) is
|XY| = |X||Y| / |X cap Y| for subgroups, used with Lagrange.

**O-pairs.** x_uv lies in {1, 2, 4} for every O-pair uv and both families (K62-E3 C2 sub-claim (a)), and
x_uv + x'_uv <= 6 (INV (b), g_uv = 6). H_x is the graph on O of the pairs with x = 4 (*x-4-edges*); n_k(x) is the number of
O-pairs with x = k; an x-4-edge uv is **tight** if x'_uv = 2 and **non-tight** if x'_uv = 1 (these are the only options);
u(x) is the number of non-tight x-4-edges. **H_alpha and H_alpha* are edge-disjoint** (4 + 4 > 6). A *triangle of H_x* is
an O-triple of type (4,4,4); t(H_x) is their number. A *diamond* is K4 minus one edge (two triangles sharing an edge).

## 1. Imports (parent-accepted; cited only at their accepted scopes)
| tag | source (verdict path, sha256, item) | used for |
|---|---|---|
| E3-L1 | RUN/review/sun7-K62E3-parent-verdict-v1.md `576969dd…bb0f`; K62-E3 Lemma 1 | both distinguished entries are 1 in G |
| E3-a | same verdict; K62-E3 C2 sub-claim (a) (erratum v2 Z11) | O-O values in {1, 2, 4}, both families |
| E3-C2 | same verdict; Corollary C2 (Z11): for alpha* when alpha_(d i*) = 1, for alpha when alpha*_(d i*) = 1 | n_4(y) >= 2 n_1(y) + 2 for both families y in G |
| INV | RUN/review/sun7-lfc-inv-parent-verdict-v1.md `8621e744…cca18`, item 2; K7-LFC-INV-v1 §2, erratum E1, E6, E7 | x + x' <= g; the inverted configuration; q = alpha* |
| L1 | rules-k7-v1.md L1 (T3), verdict RUN-2026-10-16 `73a25ba6…9f35` line 23; for x = alpha* applied to the inverted configuration (CAP-DT erratum-v2 V11) | apex measures (2.1) |
| VFC | rules-k7-v1.md §2 (V1)-(V4), same verdict | Lemma EQ (2.3) |
| APEX | CAP-DT verdict `84061c6f…34a0` item 5: DT-A §1 table (both families; admissible only), with DG-3 (SH-DG verdict `cae455c3…ddda` item 3; SH-DG erratum G3) | admissible tau, deep types (2.2), apex equalities (2.1) |
| CI | CAP-DT verdict item 5 (DT-A §2): v in O unmarked, the family's own distinguished entry x_(d i*) = 1 | both-tight case of Lemma EQ |
| R4, B1, B3, B5 | CAP-DT verdict item 6 (DT-B (R4) in its CD13 positive-support form; B1; B3; B5's edge-disjointness computation), G only | degrees, no K4/bowtie, the final step |
| C2deg | CAP-DT verdict item 6 (DT-C C2: minimum degree; 3 <= |H_x| <= 7) | minimum degree |
| DG | SH-DG verdict item 4 (Theorem DG (a)/(b), its orientation and its four-subset hypothesis, automatic at e_d = 4) | Lemma DEEP (2.9) |
| HD (premise, not accepted) | `K62-HD-v2.md` 6c1858c0…, statement of Theorem HD; parent erratum 3c670e5f… | only in Lemma DEEP for e_d >= 5 |

No M13, K7 or O-marked material is used.

## 2. Lemmas
**2.1 Apex equality (APEX, L1).** Let {v, a, b} be an O-triple with x_va = x_vb = 4 and tau_x({v, a, b}) = 4 x_ab. Then
X^v_a = X^v_b.
*Proof.* L1 (T3) in the x-configuration at apex v (gamma_v = lcm(g_va, g_vb) = 6) gives
mu(Phi_v(Phi_a cap Phi_b)) = tau / (6 x_ab) = 4/6. By L0.1, mu(X^v_a) = x_va / 6 = 4/6 = mu(X^v_b). Phi_v(Phi_a cap Phi_b) lies in
X^v_a and in X^v_b; finite sets with an inclusion and equal measures are equal, so X^v_a = Phi_v(Phi_a cap Phi_b) = X^v_b. QED
*Instances* (the DT-A §1 table): type (2,4,4) with tau = 8, at the apex opposite the 2-edge (8 = 4 * 2); type (4,4,4) with
tau = 16, at each of its three apexes (16 = 4 * 4).

**2.2 Deep types (APEX, DG-3).** For an O-triple R, delta_x(R) = 1 + v2 tau_x(R), and tau_x(R) is a multiple of the lcm
of its x-values with tau_x(R) <= x1 x2 (sorted values x1 <= x2 <= x3). Hence **delta_x(R) >= 4 iff R has type (2,4,4) with
tau = 8, or type (4,4,4) with tau = 8 or tau = 16**; delta_x(R) = 5 only for (4,4,4) with tau = 16; always delta_x(R) <= 5.
*Proof.* A type other than (2,4,4), (4,4,4) has x1 x2 <= 4, so tau <= 4 and delta <= 3. Type (2,4,4): tau in {4, 8};
type (4,4,4): tau in {4, 8, 12, 16}; v2 tau >= 3 exactly for tau in {8, 16} (v2 12 = 2). QED

**2.3 Lemma EQ (re-proved here; same statement as in K62-HD-v2).** Let v, a, b be distinct vertices of O and x a family
with x_va = x_vb = 4 and X^v_a = X^v_b. Then **x'_va = x'_vb = 1** (both edges are non-tight).
*Proof.* Work in the x-configuration and left-translate all its cosets by the inverse of v's representative; this changes
no subgroup, no index and no set Phi_vPhi_j. VFC at v: for j != v the set D_j := Phi_v h_j Phi_j (h_j the translated
representative of j) satisfies (V1) D_j cap X^v_j = empty and mu(D_j) = q_j / g_vj with q_j = x'_vj (INV (b) for the
x-configuration, whose alpha*-matrix is x'); (V4) D_j is left Phi_v-invariant, hence a union of right cosets Phi_v y;
(V2) its local index is d_j = q_j n_j / g_vj; (V3) a right coset contained in D_j and in D_k (j != k) forces
gcd(d_j, d_k) >= 2 (|T| = 2, Sun(2)). As x_va = 4 and x' lies in {1, 2, 4} with x + x' <= 6, x'_va and x'_vb lie in {1, 2}.
Put Y := G minus X^v_a = G minus X^v_b; mu(Y) = 2/6.
- Both tight (x'_va = x'_vb = 2): every hypothesis of CI holds (v in O unmarked; x_(d i*) = 1 in G; x_va = x_vb = 4;
  X^v_a = X^v_b; both edges tight), and CI gives a contradiction.
- Exactly one tight, say x'_vb = 2 and x'_va = 1 (a and b play symmetric roles): D_b lies in G minus X^v_b = Y and has
  measure 2/6 = mu(Y), so D_b = Y. D_a lies in G minus X^v_a = Y = D_b and has measure 1/6 > 0, so it contains a right coset
  R of Phi_v, and R lies in D_a and in D_b. The local indices are d_a = 1 * 6 w_a / 6 = w_a and d_b = 2 * 6 w_b / 6 = 2 w_b,
  which are coprime (the w's are odd and pairwise coprime). This contradicts (V3).
So both edges are non-tight. QED

**2.4 Lemma BUD (budget; re-proved).** For each family x: **n_4(x) <= 8 - 2 u(x).**
*Proof.* E3-C2 for x' (it needs x_(d i*) = 1, true in G): n_4(x') >= 2 n_1(x') + 2. Every non-tight x-4-edge has x' = 1,
so n_1(x') >= u(x). Edge-disjointness gives n_4(x) + n_4(x') <= 10. Hence n_4(x) <= 10 - 2 n_1(x') - 2 <= 8 - 2 u(x). QED

**2.5 Lemma DEG (re-proved from accepted rules).** For each family x, every vertex of O has H_x-degree at least 1 and at
most 3, and H_x contains no K4 and no two triangles sharing exactly one vertex.
*Proof.* Degree >= 1 is DT-C C2 (accepted); directly: if v had H_x-degree 0, the four O-entries of the x-row at v would lie
in {1, 2} (E3-a), which DT-B (R4) forbids in G (its 5/6 bound is RC-O, which needs v unmarked and x'_(d i*) = 1; CD13
gives the positive-support certificate, valid also when h_d >= 1). Degree <= 3 is B1; the rest is B3. QED

**2.6 Lemma T16 [NEW].** In G, for both families, **no O-triple has type (4,4,4) with tau = 16.** Consequently every
O-triple has raw depth <= 4 (2.2), and an O-triple has raw depth >= 4 iff it has type (2,4,4) or (4,4,4) with tau = 8.
*Proof.* Let R = {a, b, c} have type (4,4,4) with tau_x(R) = 16. By 2.1 at each of the three apexes, X^a_b = X^a_c,
X^b_a = X^b_c and X^c_a = X^c_b. Lemma EQ at each apex makes all three pairs ab, ac, bc non-tight x-4-edges, so u(x) >= 3, and
BUD gives n_4(x) <= 2. But ab, ac, bc are three x-4-edges. Contradiction. QED

**2.7 Lemma ONE [NEW].** For each family x, **at most one O-triple has type (2,4,4) with tau_x = 8; if one exists,
u(x) >= 2 and n_4(x) <= 4.**
*Proof.* Let R = {v, a, b} have x_ab = 2, x_va = x_vb = 4 and tau_x(R) = 8. By 2.1 at v, X^v_a = X^v_b; by EQ, va and vb are
non-tight, so u(x) >= 2 and n_4(x) <= 4 (BUD). If R_1 != R_2 are two such triples, let E_i be the set of the two x-4-edges of
R_i (both non-tight). E_i determines R_i (R_i is the set of endpoints of E_i), so E_1 != E_2, hence |E_1 cup E_2| >= 3, so
u(x) >= 3 and n_4(x) <= 2 < 3 <= |E_1 cup E_2| <= n_4(x). Contradiction. QED

**2.8 Lemma TRI (graphs).** Let H be a graph on a 5-set with maximum degree <= 3, no K4, and no two triangles sharing
exactly one vertex. Then H has at most two triangles, and if it has two, they share an edge, so H contains a diamond.
*Proof.* Two distinct triangles on 5 vertices share at least one vertex (3 + 3 > 5), hence (hypothesis) exactly two, i.e. an
edge. Suppose T_1 = {p, q, r}, T_2 = {p, q, s} and a third triangle T_3, which shares an edge with each of them.
(i) If T_3 contains p and q, then T_3 = {p, q, y} with y not in {r, s}, and p is adjacent to q, r, s, y: degree 4.
(ii) Otherwise T_3 contains exactly one of the edges qr, pr of T_1, say qr (the case pr is symmetric under p <-> q), and
T_3 = {q, r, y} with y != p. T_3 must share an edge with T_2 = {p, q, s}; its edges are qr, qy, ry, and qr is not in T_2,
ry is in T_2 only if {r, y} is contained in {p, q, s}, impossible as r is not; so qy is in T_2, i.e. y in {p, s}, so y = s and
T_3 = {q, r, s}. Then {p, q, r, s} spans pq, pr, qr, ps, qs, rs: a K4.
Both cases contradict the hypotheses. QED

**2.9 Lemma DEEP.** Let x be a family. If e_d = 4, or if e_d >= 5 and **(CONDITIONAL ON HD)** Theorem HD holds, then
**at least two O-triples have type (2,4,4) or (4,4,4) with tau_x = 8.**
*Proof.* Theorem DG applies to x in G: to alpha* because alpha_(d i*) = 1, and to alpha because alpha*_(d i*) = 1 (DG's
orientation, both available in G). Its four-subset hypothesis (every 4-subset Q of O has capped depth
min(e_d, delta_x(Q)) <= 4) is automatic when e_d = 4 (accepted verdict cae455c3… item 4), and when e_d >= 5 it is exactly the
statement of Theorem HD (raw depth <= 4 for every 4-subset, both families). DG (b) then gives an O-triple of capped depth
>= 4, and if only one O-triple has capped depth >= 4, it has capped depth 5, type (4,4,4) and tau = 16, which T16 excludes.
So at least two O-triples have capped depth >= 4, hence raw depth >= 4, and by T16 each has type (2,4,4) or (4,4,4) with
tau_x = 8. QED

## 3. Theorem GX [NEW; CANDIDATE_UNVERIFIED]
**Statement.** Let a K6.2* configuration lie in G (section 0), in a finite group.
- **(a)** It does not have e_d = 4.
- **(b) (CONDITIONAL ON HD)** It does not have e_d >= 5.
Hence, conditional on HD for (b), **G is empty**, for every admissible f*, h_d, h* and w-parts (all exponents unbounded);
by R0 (finite-core quotient, accepted LFC/INV verdict item 6) the same holds for arbitrary groups with finite-index
subgroups.

*Proof.* Assume e_d = 4, or e_d >= 5 and HD.
**Step 1: for each family x, H_x contains a diamond.** By DEEP, at least two O-triples have type (2,4,4) or (4,4,4) with
tau_x = 8. Those of type (4,4,4) are triangles of H_x, so there are at most t(H_x) of them; those of type (2,4,4) are at most
one (ONE). By DEG, H_x satisfies the hypotheses of TRI, so t(H_x) <= 2. Suppose t(H_x) <= 1. Then 2 <= t(H_x) + 1 forces
t(H_x) = 1 and the existence of a (2,4,4) triple with tau_x = 8, so n_4(x) <= 4 (ONE). Let {p, q, r} be the triangle and
{s, f} := O minus {p, q, r}. By DEG, s and f have H_x-degree >= 1, while at most one x-4-edge lies outside the triangle; so
that edge is sf and H_x = {pq, qr, rp, sf}. In this graph any two x-4-edges with a common vertex lie in the triangle, so the
only O-triple containing two x-4-edges is {p, q, r}, of type (4,4,4): no O-triple has type (2,4,4). Contradiction. Hence
t(H_x) = 2, and by TRI the two triangles share an edge: H_x contains a diamond.
**Step 2: contradiction (B5).** By Step 1 for x = alpha, H_alpha contains the five edges ac, aq, bc, bq, cq of a diamond on
{a, b, c, q} (missing ab). H_alpha* is edge-disjoint from H_alpha, so it lies in {ab, ae, be, ce, qe}, e the fifth vertex of O.
The only triangle of this edge set is {a, b, e} (ce and qe are the only edges at c and at q), so t(H_alpha*) <= 1, contradicting
Step 1 for x = alpha*. QED

## 4. Corollary OM [CANDIDATE_UNVERIFIED; for e_d >= 5 CONDITIONAL ON HD]
**Every K6.2* configuration (any group, finite-index subgroups) has a marker on a vertex of O**: some c in O has f_c >= 2 or
h_c >= 1.
*Proof.* By accepted K62-E3, e_d >= 4 and e* = 2. If no vertex of O is marked, the 3-marker is not on d (f_d = 0), hence on
i* or absent, and the 5-marker is on d, on i* or absent: the configuration lies in G, and Theorem GX applies. QED
*Navigation only (no claim):* the K6.2* cases left open are those with the 3-marker t in O (orientations (1,1), (1,3), (3,1);
the last two are M13, owned elsewhere) or the 5-marker p in O. K7 and Sun(7) are untouched.

## 5. Scope, provenance and checks
- **Claims:** Lemmas T16, ONE, TRI, DEEP (2.6-2.9) and Theorem GX (a) rest only on the parent-accepted imports of section 1
  and on the re-proved Lemmas 2.1-2.5; Theorem GX (b) and the e_d >= 5 part of Corollary OM are **CONDITIONAL ON HD**, used
  only for the four-subset hypothesis of Theorem DG in Lemma DEEP. T16 shows, without HD, that no O-triple in G has raw
  depth 5.
- **Not claimed:** any O-marked case; M13; K7; Sun(7); realisability of any pattern; acceptance of HD.
- **Unused:** f* = 1, (RC-i*), C2 at i*, any i*-row or d-row count beyond those inside the cited imports; so the 3-marker on
  i* (any f*) and the 5-marker on d or i* (any exponent) are covered by the same text.
- **Sun provenance.** Direct new Sun instance: Sun(2) (Lemma EQ). Through imports: Sun(2), Sun(3) (CI, (R4)), Sun(4)
  (K62-E3). The accepted LFC/VFC package cites Sun(t), t <= 6, and the K6.2* class reduction uses the computer-assisted Sun(5)
  (verdict 2cf02436…5301) and Sun(6) (verdict efe1d849…1e29); both remain in the transitive import closure.
- **Mutation checks for reviewers (thought experiments; nothing run):**
  (1) Replace EQ by CI' alone (one non-tight edge per forced apex): ONE fails, and a triangle with tau 8 plus a pendant
  (2,4,4) tau-8 cherry is no longer excluded by the counts. (2) Drop DEG's minimum degree: H_x = triangle {p, q, r} with
  tau 8 plus the edge rs, with x_sp = 2 and tau_x({r, s, p}) = 8, passes DEEP, ONE and BUD (u = 2, n_4 = 4); only the isolated
  fifth vertex excludes it. (3) Drop the edge-disjointness of H_alpha and H_alpha*: both families could carry diamonds.
  (4) Drop T16: at e_d >= 5 the DG (b) alternative "exactly one triple, of capped depth 5" is no longer excluded.
- No computation, enumeration, novelty, priority, Lean or human-review claim.
