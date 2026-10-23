# K62-HD-v1: in the generic sub-case G every 4-subset of O has raw depth <= 4 (the higher-depth alternative of Theorem DG is empty) [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:15:54-0700.
- **Author:** SunK62Regimes; single author; written mathematics only. No computation of any kind was run for this file
  (global runtime HOLD respected). **Label of every new claim: CANDIDATE_UNVERIFIED.**
- **Frozen scope (written before any derivation):** `K62-HD-SCOPE-v1.md` in this directory, sha256
  c0cbb507adc8d23fb5894e02744d1176ba27f613b904c0ddb40739feb0702f82. The statement below is exactly its section 3.
- RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`;
  K62 := `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon`.

## 0. Setting and notation
**Class (CAP section 0, accepted setting of verdict 84061c6f…).** V = {d, i*} disjoint-union O, |O| = 5;
n_d = 2^(e_d) 5^(h_d) w_d with e_d >= 4 (so e* = 2); n_(i*) = 4 * 3^(f*) 5^(h*) w_*; n_c = 2 * 3^(f_c) 5^(h_c) w_c (c in O);
the w's are pairwise coprime and coprime to 30; at most one higher 3-marker and at most one 5-marker.
**G (verdict 84061c6f… item 6):** no vertex of O carries a marker, i.e. n_c = 6 w_c for every c in O; the 3-marker is on i*
(f* >= 2, any value) or absent; the 5-marker is on d, on i* (any exponent) or absent. In G,
(alpha_(d i*), alpha*_(d i*)) = (1, 1) (K62-E3 Lemma 1), so **both distinguished entries are 1** and every O-vertex is unmarked.

**Families.** x in {alpha, alpha*}, x' the other family. Phi^alpha_j = U_j, Phi^alpha*_j = U*_j = g_jU_jg_j^-1; we write Phi_j
for Phi^x_j when x is fixed. For S contained in O: W_S := intersection of Phi_j (j in S), T_x(S) := [G : W_S], and the
**raw depth** delta(S) := v2 T_x(S). For an O-triangle R = {a, b, c}: tau(R) := T_x(R) / lcm(n_a, n_b, n_c). X^v_j := Phi_vPhi_j.
mu(Y) := |Y| / |G| (finite G; arbitrary groups via R0, see section 5).
**Edges.** For an O-pair uv: x_uv in {1, 2, 4} (K62-E3 C2 sub-claim (a), both families). The pair is an **x-4-edge** if
x_uv = 4; H_x is the graph on O of the x-4-edges; n_k(x) := #{O-pairs with x = k}. An x-4-edge uv is **tight** if
x'_uv = 2 and **non-tight** if x'_uv = 1 (x + x' <= 6 by INV (b), so x' in {1, 2}); u(x) := number of non-tight x-4-edges.

## 1. Imports (parent-accepted; cited only at the accepted scopes)
| tag | source (verdict path, sha256, item) | used as |
|---|---|---|
| INV | RUN/review/sun7-lfc-inv-parent-verdict-v1.md `8621e744…cca18`, item 2; K7-LFC-INV-v1 §2 + erratum E1, E6 | alpha + alpha* <= g; the inverted configuration is a configuration of the same class with alpha and alpha* swapped; q = alpha* |
| L1 | rules-k7-v1.md (77b9afec…) L1 (T1)-(T3), accepted RUN-2026-10-16 verdict `73a25ba6…9f35` line 23 | apex identity (T3); for x = alpha* applied to the inverted configuration |
| VFC | rules-k7-v1.md §2 (V1)-(V4), same verdict line 23 | used only in Lemma EQ |
| APEX | RUN/review/sun7-K62-CAP-DT-parent-verdict-v1.md `84061c6f…34a0`, item 5 (DT-A §1 table, both families, admissible only) with K62-SH-DG-erratum-v1 G3 (DG-3, verdict `cae455c3…dda` item 3) | admissible tau of O-triangles |
| CI, CI' | verdict 84061c6f… item 5 (K62-DT-A §2; v in O unmarked; the family's own distinguished entry x_(d i*) = 1) | forced non-tightness |
| R4, B3 | verdict 84061c6f… item 6 (K62-DT-B (R4) positive-support form CD13; B3 no K4), in G only | min degree; no K4 in H_x |
| E3-L2 | RUN/review/sun7-K62E3-parent-verdict-v1.md `576969dd…ee0f`; K62-E3 Lemma 2 | at most two entries 1 in an O-row, both families |
| E3-C2 | same verdict; Corollary C2 with erratum v2 Z11 | n_4(x) >= 2 n_1(x) + 2 for alpha* when alpha_(d i*) = 1, for alpha when alpha*_(d i*) = 1 (both in G) |
| E3-L3 | same verdict; Lemma 3 proof form for every non-empty Q in O (erratum v2 Z6, Z10) | prime-to-30 part of T_x(S) is the product of the w_j (j in S) |
| DG-4 | verdict cae455c3… item 3 (K62-DG-v1 §3 with SH-DG erratum G4) | chain step for an unmarked added vertex, raw depths; written out with its equality case in P3 |
| DG | verdict cae455c3… item 4 | only in Corollary HD (its hypothesis is what Theorem HD supplies) |

Nothing else is imported. M13 material and K7 material are not used.

## 2. Preliminaries
**P1 (O-values).** Every O-pair has x, x' in {1, 2, 4} and x + x' <= 6 (E3 C2 sub-claim (a); INV (b), g = 6). Hence H_x and
H_x' are edge-disjoint, and a non-tight x-4-edge is an O-pair with x' = 1.

**P2 (triangle table, raw depth).** For an O-triangle R with x-values x1 <= x2 <= x3: delta(R) = 1 + v2 tau(R), and tau(R)
is a multiple of lcm(x1, x2, x3) with tau(R) <= x1 x2 (APEX: L1 for the configuration whose alpha-matrix is x, INV for
x = alpha*; v2 lcm(n_a, n_b, n_c) = 1 since every n_c = 6 w_c). The admissible values:
(1,1,1): tau 1, delta 1; (1,2,2): tau 2, delta 2; (1,4,4): tau 4, delta 3; (2,2,2): tau 2 or 4, delta 2 or 3;
(2,2,4): tau 4, delta 3; (2,4,4): tau 4 or 8, delta 3 or 4; (4,4,4): tau 4, 8, 12, 16, delta 3, 4, 3, 5;
(1,1,2), (1,1,4), (1,2,4): impossible. **Hence delta(R) <= 5; delta(R) >= 4 iff R is (2,4,4) with tau = 8 or (4,4,4) with
tau in {8, 16}; delta(R) = 5 iff R is (4,4,4) with tau = 16; a triangle with an edge of value 1 has delta <= 3.**

**P3 (chain step with equality case).** Let S be a non-empty subset of O and e in O minus S. Then
T_x(S + e) = lcm(n_e, T_x(S)) * k with k a positive integer, **k = 6 mu(Phi_e W_S)**, k <= x_ej for every j in S, with
**equality k = x_ej iff Phi_e W_S = X^e_j**; and **delta(S + e) = delta(S) + v2 k**.
*Proof.* n_e and T_x(S) divide T_x(S + e) (Lagrange), so lcm(n_e, T_x(S)) divides it; call the quotient k. By L0.1,
mu(Phi_e W_S) = T_x(S + e) / (n_e T_x(S)) = k / gcd(n_e, T_x(S)). Here n_e = 6 w_e (e unmarked in G); 6 divides T_x(S)
(it is divisible by n_j = 6 w_j, j in S); and w_e is coprime to T_x(S), whose prime-to-30 part is the product of the w_j,
j in S (E3-L3 chain for S; for x = alpha apply it to the inverted configuration, INV). So gcd(n_e, T_x(S)) = 6 and
k = 6 mu(Phi_e W_S). Since W_S is contained in Phi_j, Phi_e W_S is contained in X^e_j, of measure x_ej / 6 (L0.1), so
k <= x_ej, and equality of measures of finite nested sets is equality of sets. Finally v2 n_e = 1 <= v2 T_x(S), so
v2 lcm(n_e, T_x(S)) = v2 T_x(S). QED (This is the proof of DG-4 with the equality case recorded.)

**P4 (apex identity).** For an O-triangle {a, b, c}: mu(Phi_b(Phi_a cap Phi_c)) = tau({a, b, c}) / (6 x_ac) (L1 (T3),
gamma_b = lcm(g_ba, g_bc) = 6; for x = alpha* via the inverted configuration). Phi_b(Phi_a cap Phi_c) contains Phi_b W_S for
every S containing {a, c}.

**P5 (budget).** n_4(x) <= 8 - 2 u(x), for both families.
*Proof.* E3-C2 for x' (applicable in G): n_4(x') >= 2 n_1(x') + 2, and n_1(x') >= u(x) by P1. Edge-disjointness (P1):
n_4(x) + n_4(x') <= 10. So n_4(x) <= 10 - (2 u(x) + 2). QED

**P6 (minimum degree).** Every v in O has H_x-degree >= 1, for both families.
*Proof.* Otherwise the four O-entries of the x-row at v lie in {1, 2} (P1), which (R4) forbids (G; Lemma RC case (RC-O)
with x'_(d i*) = 1). QED (This is DT-C C2; it is re-derived here from the accepted (R4).)

**Lemma EQ [NEW].** Let v, a, b be distinct vertices of O with x_va = x_vb = 4 and X^v_a = X^v_b. Then **both va and vb
are non-tight** (x'_va = x'_vb = 1).
*Proof.* Work in the Phi^x-configuration at v after the left translation making v's representative 1 (the subgroups are
unchanged). By VFC (V1) and INV (b), for j in V minus {v} the set D'_j (a union of right cosets of Phi_v, (V4)) is
disjoint from X^v_j and has measure x'_vj / g_vj; its local index (V2) is lambda'_j = n_j x'_vj / g_vj; and a right coset
lying in D'_j and D'_k needs gcd(lambda'_j, lambda'_k) >= 2 ((V3) with |T| = 2, Sun(2)). Put Y := G minus X^v_a =
G minus X^v_b, of measure 2/6.
- If both edges are tight, Lemma CI (hypotheses: v in O unmarked, x_(d i*) = 1, x_va = x_vb = 4, X^v_a = X^v_b, both
  tight; all hold in G) gives a contradiction.
- If exactly one is tight, say vb (x'_vb = 2) and x'_va = 1: then D'_b is contained in Y and has measure 2/6 = mu(Y), so
  D'_b = Y. D'_a is contained in G minus X^v_a = Y = D'_b and has measure 1/6 > 0, so it contains a right coset R of Phi_v
  with {a, b} contained in S_R. But lambda'_a = n_a * 1/6 = w_a and lambda'_b = n_b * 2/6 = 2 w_b (a, b unmarked) are
  coprime (w's odd, pairwise coprime). Contradiction. QED
(Remark: the isolation of an entry x' = 1 used here is the same fact as "entries 1 are isolated" in DT-B section 0.)

## 3. Theorem HD [NEW; CANDIDATE_UNVERIFIED]
**Statement.** In G (any e_d >= 4 and every admissible f*, h_d, h*, w), for both families x in {alpha, alpha*} and every
4-subset Q of O: **delta(Q) = v2 T_x(Q) <= 4.**

*Proof.* Suppose delta(Q) >= 5 for some x and some 4-subset Q. For e in Q put R_e := Q minus {e} and
m_e := min over j in R_e of x_ej (a power of 2). By P3 with S = R_e and k = k_e <= m_e:
  **(N_e)** 5 <= delta(Q) = delta(R_e) + v2 k_e <= delta(R_e) + v2 m_e, for every e in Q.
By P2: (N_e) with m_e = 1 forces R_e to be (4,4,4) with tau = 16; with m_e = 2 it forces delta(R_e) >= 4, i.e. R_e is
(2,4,4) with tau = 8 or (4,4,4) with tau in {8, 16}; with m_e = 4 it forces delta(R_e) >= 3.
By B3, H_x has no K4, so **Q contains an O-pair with x != 4.**

**Case A: some pair ab in Q has x_ab = 1.** Let c, q be the other two vertices of Q. R_c and R_q contain ab, so by P2
delta(R_c), delta(R_q) <= 3; (N_c), (N_q) then force m_c = m_q = 4 and delta(R_c) = delta(R_q) = 3. So every pair at c and at q
is an x-4-edge: x_ca = x_cb = x_cq = x_qa = x_qb = 4. Now m_a = x_ab = 1, so (N_a) forces R_a = {b, c, q} to be (4,4,4) with
tau = 16; likewise (N_b) gives tau({a, c, q}) = 16. Apply CI' (v unmarked, x_(d i*) = 1):
- at c: triangle {c, a, b} has x_ca = x_cb = 4 and tau = 4 = 4 x_ab (forced for (1,4,4), P2); triangle {c, a, q} has
  tau = 16 = 4 x_aq; triangle {c, b, q} has tau = 16 = 4 x_bq. So each of the pairs {ca, cb}, {ca, cq}, {cb, cq} contains a
  non-tight edge, hence at least two of ca, cb, cq are non-tight;
- at q, in the same way (triangles {q, a, b}, {q, a, c}, {q, b, c}), at least two of qa, qb, qc are non-tight.
These are at least three distinct non-tight edges (only cq is shared), so u(x) >= 3 and P5 gives n_4(x) <= 2. But
ca, cb, cq, qa, qb are five x-4-edges. Contradiction.

**Case B: every pair of Q has x in {2, 4}.** Let N be the set of pairs of Q with x = 2; N is non-empty. A vertex v of Q
incident with an edge of N has m_v = 2, so by (N_v) R_v is (2,4,4) or (4,4,4): **R_v contains at most one edge of N**,
i.e. at most one edge of N avoids v. This leaves exactly four shapes for N:
- |N| = 3: a star (a leaf is avoided by two edges) and a path on four vertices (an end is avoided by two edges) fail;
  only the **triangle** remains.
- |N| >= 4: a vertex incident with N is avoided by at least |N| - 3 >= 1 edges of N, so every such vertex has N-degree
  |N| - 1 >= 3, i.e. N-degree 3, which forces |N| = 6 (if one vertex has degree 3, all four are incident with N); then
  every vertex is avoided by three edges. Impossible.
- |N| = 2: **two adjacent** or **two disjoint** edges; |N| = 1: **one edge**. (All pass the counting.)
Name the vertices Q = {a, b, c, q} as indicated in each sub-case; f denotes the fifth vertex of O.

**B1: N = {ab}.** The x-4-edges in Q are ac, aq, bc, bq, cq (five). m_b = 2, so tau({a, c, q}) in {8, 16} (values (4,4,4)).
- tau({a, c, q}) = 16: CI' at the three (unmarked) apexes of {a, c, q} (at each apex tau = 16 = 4 * 4) gives at least two
  non-tight edges among ac, aq, cq (if only one were non-tight, the apex opposite it would have two tight edges). So
  u(x) >= 2 and P5 gives n_4(x) <= 4 < 5. Contradiction.
- tau({a, c, q}) = 8: delta({a, c, q}) = 4, so (N_b) needs v2 k_b >= 1 with k_b <= m_b = x_ba = 2: k_b = 2 = x_ba, and by P3
  Phi_bW_{a,c,q} = X^b_a, of measure 2/6. By P4 at apex b, mu(Phi_b(Phi_a cap Phi_c)) = tau({a, b, c}) / 24 >= 2/6, so
  tau({a, b, c}) >= 8; its values are (2,4,4), so tau({a, b, c}) = 8; likewise (P4 with {a, q}) tau({a, b, q}) = 8. CI' at c
  (x_ca = x_cb = 4, tau = 8 = 4 x_ab) gives a non-tight edge among ca, cb; CI' at q gives one among qa, qb. They are
  distinct, so u(x) >= 2 and n_4(x) <= 4 < 5. Contradiction.

**B2: N = {ab, bc} (adjacent at b).** The x-4-edges in Q are ac, aq, bq, cq. m_b = 2, so tau({a, c, q}) in {8, 16}.
- tau({a, c, q}) = 8: as in B1, k_b = 2 = x_ba, and Phi_bW_{a,c,q} = X^b_a has measure 2/6. Triangle {a, b, c} has values
  (2,2,4), so tau({a, b, c}) = 4 (P2) and, by P4 at apex b, mu(Phi_b(Phi_a cap Phi_c)) = 4/24 = 1/6. But this set contains
  Phi_bW_{a,c,q}, of measure 2/6. Contradiction.
- tau({a, c, q}) = 16: as in B1, u(x) >= 2, so n_4(x) <= 4; Q already carries four x-4-edges, so H_x consists of exactly
  ac, aq, bq, cq and f has H_x-degree 0, contradicting P6.

**B3: N = {ab, cq} (disjoint).** The x-4-edges in Q form the 4-cycle a-c-b-q-a. Every vertex of Q has m = 2, and each
R_v contains exactly one edge of N, so each R_v is (2,4,4) with tau = 8: tau({b, c, q}) = tau({a, c, q}) = tau({a, b, q}) =
tau({a, b, c}) = 8. CI' at the apex opposite the 2-edge of each of these triangles (b for {b, c, q}, a for {a, c, q}, q for
{a, b, q}, c for {a, b, c}; there tau = 8 = 4 * 2) shows that **every vertex of the 4-cycle is incident with a non-tight
cycle edge**. One edge covers two vertices, so u(x) >= 2 and n_4(x) <= 4: H_x is exactly the 4-cycle and f has
H_x-degree 0, contradicting P6.

**B4: N = {ab, bc, ac} (triangle).** The x-4-edges in Q are qa, qb, qc, so m_q = 4. R_q = {a, b, c} has values (2,2,2),
so delta(R_q) in {2, 3} (P2), and (N_q) with v2 k_q <= v2 m_q = 2 forces delta(R_q) = 3 and k_q = 4 = x_qa = x_qb = x_qc.
By P3, X^q_a = X^q_b = X^q_c (= Phi_qW_{a,b,c}). Lemma EQ for the pairs (a, b) and (a, c) at v = q makes qa, qb and qc
non-tight, i.e. x'_qa = x'_qb = x'_qc = 1: three entries 1 in the x'-row at q, contradicting E3-L2.

Cases A and B1-B4 exhaust all possibilities, so delta(Q) <= 4. QED

## 4. Corollary HD [CANDIDATE_UNVERIFIED; consequence at the accepted scope of Theorem DG]
In G, for every e_d >= 4 and both families, every 4-subset Q of O has capped depth min(e_d, v2 T_x(Q)) <= 4. Hence:
- **the higher-depth alternative of Theorem DG (b) for e_d >= 5 is empty in G**;
- the four-subset hypothesis of Theorem DG (a) holds in G for alpha* (alpha_(d i*) = 1) and for alpha (alpha*_(d i*) = 1), so
  Theorem DG (a), (b) apply to both families in G with no remaining hypothesis: N(O) <= n_d / 16, the triple sum is
  <= 19/16 - 2/n_d, and each family has at least two O-triples of capped depth >= 4, or exactly one, of capped depth 5
  (values (4,4,4), tau = 16, e_d >= 5);
- the pattern-level consequence of DT-A (3c), 2 theta_4 + 3 theta_5 >= 3 + 4 theta_2 + 12 theta_1, holds in G for both
  families (a LOSSY necessary consequence in the sense of CAP (D3); not an equivalence), and the "otherwise" branch of the
  DT-B B4 proof (a 4-subset of capped depth >= 5) never occurs in G.
These are restatements of accepted conclusions with their hypothesis now supplied; no new exclusion of G or of any
pattern beyond Theorem HD itself is claimed.

## 5. Scope, provenance and limits
- **Claim:** Theorem HD and Corollary HD, exactly in G (section 0): no marker on O; the 3-marker on i* with any f* or
  absent; the 5-marker on d or i* with any exponent, or absent; every e_d >= 4; all exponents unbounded. Over arbitrary
  groups with finite-index subgroups by R0 (the common finite-core quotient preserves indices, intersection indices and
  disjointness; every imported lemma is stated for that setting).
- **Not claimed:** any O-marked case; the (1,3)/(3,1) orientations (M13, owned elsewhere); K7; any exclusion of G or of
  any G-pattern other than "a 4-subset of raw depth >= 5"; full K6.2* with e_d >= 4, e* = 2; Sun(7); realisability of any
  pattern.
- **New steps:** P3's equality case (from L0.1/Lagrange), Lemma EQ's one-tight case (VFC (V1)-(V4), INV (b), Sun(2)), the
  case analysis of section 3. Every other step is an accepted import at its stated scope.
- **Sun provenance.** Direct new Sun instance: Sun(2) (Lemma EQ). Through imports: Sun(2), Sun(3) (CI, (R4)), Sun(4)
  (K62-E3). The accepted LFC/VFC package cites Sun(t), t <= 6, and the K6.2* class reduction uses the computer-assisted
  Sun(5) (verdict 2cf02436…5301) and Sun(6) (verdict efe1d849…1e29); these remain in the transitive import closure. No
  claim is made that the closure avoids them.
- **Suggested mutation checks for reviewers (thought experiments, nothing run):** (1) drop B3: then Q could be a 4-clique
  of x-4-edges with every tau = 16, which (N_e) alone does not exclude; (2) drop the equality case of P3: B2's tau = 8
  branch and B4 lose their contradictions; (3) drop E3-C2 (P5): B1 and B3 are no longer contradictory; (4) allow a
  marked vertex in Q: P3's gcd 6 and Lemma EQ's coprimality both fail, so the proof does not extend.
- No computation, enumeration, novelty, priority, Lean or human-review claim.
