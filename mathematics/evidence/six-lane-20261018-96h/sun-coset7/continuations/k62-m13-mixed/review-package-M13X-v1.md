# M13X written review package v1: full exclusion of the M13 orientations (1,3)/(3,1) of K6.2* [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T13:07:43-0700, immediately before this exclusive write.
- **Owner:** SunM13MixedFibres. Written mathematics only; no computation, model call or nested agent. Packaging used only
  sha256, byte counts and line-range extraction. The parent owns model reviews and verdicts.
- **Candidate:** `K/K62-M13X-v1.md`, sha256 `b86bb186e425ea5ac69a51d85ad5f56cfc1abd2a08c66c169fd54de074262db9` (332 lines, 34,995 B). **Frozen scope:** `K/K62-M13X-SCOPE-v1.md`, sha256
  `072c509805f89b8cfff7f57c97ff4508f1a7aca6925977fb341198881497bf01` (written before derivation). **Input-change record:** `K/checkpoint-001-v1.md`, sha256 `46f168fe88b0d642cf7e043e3f7c536fb0a6053202287663f0da4fbef8a5ed98`.
- Root aliases (exact absolute prefixes): K = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-m13-mixed`;
  F = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon`;
  S = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7`;
  O16 = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7`;
  R = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review`;
  R16 = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`.

## 1. Claim and exact status
**Theorem M13X / Corollary M13X' (CANDIDATE_UNVERIFIED):** no K6.2* configuration, in any group with finite-index
subgroups, has (alpha_(d i*), alpha*_(d i*)) in {(1,3), (3,1)}; every admissible 5-marker placement (d, i*, t, some p in
O minus {t}, or none); all exponents and w-parts unbounded. (3,1) is handled by applying (1,3) to the ACTUAL inverted
configuration (INV (a)-(b) with E6), not by a symmetry assertion. Not claimed: the orientation (1,1), the rest of K6.2*, K7,
Sun(7); novelty, priority, significance, Lean or human review. Sun(5)/Sun(6) remain computer-assisted transitive imports.

## 2. Reading order
1. Scope (whole) and checkpoint-001 lines 8-16 (input change: M13 A-D accepted at scope 2fac7a30…).
2. Candidate, whole: section 0 setting/notation; section 1 interface table; sections 2-9 proofs; section 10 boundaries.
3. Accepted imports at the literal ranges listed in section 4 (statement text, not headings).
4. Pending texts (R2MIX Lemmas 1-2; MK-v2 3.3-3.7, 5-6; M3R-v2 section 7) are included ONLY for attribution and comparison;
   they are not premises. The candidate re-proves every step it borrows from them.

## 3. Verbatim key statements (raw candidate lines)
K62-M13X-v1.md:101-104
```text
## 3. Proposition SG (i*-free subset granularity at every O-vertex) [NEW; CANDIDATE_UNVERIFIED]
**Statement.** In M13, let z be either family and R a non-empty subset of O. Then
  T_z({d} cup R) = lcm(n_d, n_j : j in R) * 2^s  for some integer s >= 0.
Consequently, **for every v in O (t and p included) and both families z: gcd(n_v, T_z(V minus {v, i*})) = 6.**
```
K62-M13X-v1.md:132-133
```text
**Lemma R4S.** In M13, for every family x and every v in O (t and p included), the four O-entries x_vu (u in O minus {v}) do
not all lie in {1, 2}.
```
K62-M13X-v1.md:157-158
```text
**Lemma CIS (no tight equal-X cherry).** In M13, let x be a family, v in O (t and p included) and a != b in O minus {v} with
x_va = x_vb = 4, X^v_a = X^v_b and x'_va = x'_vb = 2. Contradiction.
```
K62-M13X-v1.md:177-178
```text
**Lemma EQS [MK-v2 Lemma 3.4, re-proved at every apex].** In M13, let x be a family, v in O and a != b in O minus {v} with
x_va = x_vb = 4 and X^v_a = X^v_b. Then **x'_va = x'_vb = 1** (both pairs non-tight).
```
K62-M13X-v1.md:234-234
```text
**Lemma FB.** For each family x and every 4-subset Q of O: delta_x(Q) <= 4.
```
K62-M13X-v1.md:266-267
```text
**Lemma DEEP.** For each family x, at least two O-triples R have delta_x(R) = 4; each has type (2,4,4) or (4,4,4) with
tau_x(R) = 8.
```
K62-M13X-v1.md:273-274
```text
**Theorem M13X.** In any finite group there is no configuration of class K6.2* with (alpha_(d i*), alpha*_(d i*)) = (1, 3), for every
admissible 5-marker placement (d, i*, t, some p in O', or none) and all exponents and w-parts.
```
K62-M13X-v1.md:287-288
```text
**Corollary M13X'.** No K6.2* configuration, in any group with finite-index subgroups, has (alpha_(d i*), alpha*_(d i*)) in
{(1, 3), (3, 1)}.
```

## 4. Source/authority table (each row = manifest entries; whole-file sha256; inclusive one-based ranges)
| ID | Path | SHA256 | Lines | Scope / authority |
|---|---|---|---|---|
| X | K/K62-M13X-v1.md | b86bb186e425ea5ac69a51d85ad5f56cfc1abd2a08c66c169fd54de074262db9 | 1-332 | NEW candidate, whole: re-derive every claim |
| SC | K/K62-M13X-SCOPE-v1.md | 072c509805f89b8cfff7f57c97ff4508f1a7aca6925977fb341198881497bf01 | 1-66 | frozen target/premise discipline (navigation) |
| CP1 | K/checkpoint-001-v1.md | 46f168fe88b0d642cf7e043e3f7c536fb0a6053202287663f0da4fbef8a5ed98 | 8-16 | input-change record (navigation) |
| README | O16/README.md | 2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1 | 9-29, 85-97 | accepted (R16 written verdict): L0.1, L0.2, Sun(2), R0; class K6.2* |
| RULES | O16/rules-k7-v1.md | 77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee | 7-24, 38-46 | accepted: L0.3, L1 (T1)-(T3); VFC (V1)-(V4) |
| WV | R16/sun-coset7-written-parent-verdict-v1.md | 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35 | 16-23, 34, 58-60 | verdict for README/rules: VFC and T sound necessary conditions; imports incl. Sun(5)/(6) |
| LFC | S/K7-LFC-INV-v1.md | 45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c | 18-45, 52-71 | accepted: LFC (a)-(d), INV (a)-(b) |
| LFCE | S/K7-LFC-INV-erratum-v1.md | 7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5 | 12-32, 47-63 | mandatory overlay: E1, E2, E3, E6, E7 |
| LFCV | R/sun7-lfc-inv-parent-verdict-v1.md | 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18 | 5, 16-23 | verdict: LFC, INV, R0 lift (item 6) |
| E3 | F/K62-E3-v1.md | 70a60d551583e8d6ad920acadb829d3ddf0d9c5c46ac988f8677645ee5457372 | 22-34, 36-55, 91-105 | accepted: theorem e_d >= 4, Lemma 1, Lemma 2, C2 (alpha*, alpha_(d i*) = 1) |
| E3E2 | F/K62-E3-erratum-v2.md | f9f52e1bc4896d94cd014ed3f8915af0318ddcd06d1efc1ad7f14478685add4c | 80-89, 276-297 | mandatory overlay: Z2 (Lemma 1 proof), Z11 (C2 proof incl. sub-claim (a)) |
| E3V | R/sun7-K62E3-parent-verdict-v1.md | 576969ddb99fc2d0f5c6382f66428a7f4d7d3a1b59f681fc4d9d0f458fecbb0f | 5, 14-25 | verdict for E3 |
| DG | F/K62-DG-v1.md | a4bfc41e832ebc4e77770cab7a8092a3341827cec93a01bfb437c978c1e84f52 | 20-36, 50-61 | accepted: DG-1, DG-2, Theorem DG (alpha*, alpha_(d i*) = 1) |
| SHDGE | F/K62-SH-DG-erratum-v1.md | 755edc21abdf7484f9187078d7e8cb6b4111f076906e7880085428d54f1b9d75 | 240-268, 323-327 | mandatory overlay: G5, G6; DG (b) conditionality and orientation |
| SHDGV | R/sun7-K62-SH-DG-parent-verdict-v1.md | cae455c3252b9066c261bcebb05ee4917b838bb5e2370101689c8297a017ddda | 14-24 | verdict: DG-1..4, Theorem DG item 4 |
| M13A | F/K62-M13-A-v1.md | 77ce4077584582c699ce1bec870f2b19c55242bfc05aac99febcfbd69c466a8d | 18-31, 69-107 | accepted (M13 verdict items 1-2): DG*, C2* for alpha in (1,3) |
| M13V | R/sun7-K62-M13-parent-verdict-v1.md | 2fac7a30ab4b832166c770492fdd6d0f555660e5c3eabcb95d514797a39c4e34 | 5-20 | verdict: exact accepted M13 scope |
| R2MIX | S/continuations/k62-r2-mixed/K62-R2MIX-v2.md | b75e6dc7e72b8c0b1cd5388e8845a3bcd23854b0fbd83292fa6ff7c22ade0806 | 77-95 | PENDING: Lemmas 1-2, re-proved in X (attribution only) |
| MK | S/continuations/k62-regimes/K62-MK-v2.md | ab7cfcb6ccebb19465eb6dfc3f96580d58c599a2507aee697604f691ad5abee9 | 115-136, 141-166, 185-225 | PENDING, (1,1): CI*/EQ*, R4*/DEG, FB-M/DEEP/MK arguments re-proved in X without NR (attribution only) |
| M3R | S/continuations/k62-regimes/K62-M3R-v2.md | af2b965bf69b252e266064aff5b201b16757bcb76af152d7eee8c89ee77888b3 | 161-177 | PENDING: obstruction note that SG bypasses (comparison only) |
The JSON manifest `K/review-excerpts-M13X-v1.json` lists these 36 ranges as {path, sha256, start, end} in this order.

## 5. Dependency and scope checks
| New claim (X lines) | Required interface / status |
|---|---|
| Lemma 1 (74-86), 1' (88-94), 2 (96-99) | Re-proved from L0.1, L0.2, Lagrange, LFC (a)-(c), VFC (V1); no normalisation needed in Lemma 1; Lemma 1' uses the own family's intersection T_x(Q). |
| Prop. SG (101-129) | E1 pair index (x_dc = 1); LFC (a)-(b) in the z-configuration at d (degrees n_d/2, own fibre empty); Lemma 2; arithmetic of the class (one 3-marker t in O, one 5-marker, coprime w's). Product separation needed only at v = t. |
| R4S (132-142) | Lemma 1 (b)-(c) with SG for z = x'; feasibility by Sun(2)/Sun(3) through LFC (c) on the positive support; y_(i*) = 0. |
| P1, DEG (144-154) | E3-a (Z11 (a)) both families; INV (b); R4S at every O-vertex. |
| CIS (157-175), EQS (177-181) | VFC (V1)-(V3) applied to the x-configuration (q = x', INV (b)); Lemma 1' with SG for z = x; Sun(2), Sun(3). No i*-piece, no full granularity, no marker restriction. |
| P2-P4 (185-209) | L0.1, Lagrange, E1, P1; P3 needs e != t only. |
| BUD (211-213) | Accepted E3-C2 for alpha* (alpha_(d i*) = 1) and accepted M13-A C2* for alpha. |
| T16, ONE (215-224) | P4, EQS at every apex (t included), BUD. |
| TRI (226-231) | Elementary graph theory. |
| FB (234-263) | P2-P4, T16, ONE, DEG; uses chain steps only at e != t. |
| DEEP (266-271) | Accepted Theorem DG (alpha*) and DG* (alpha) under r_Q <= 4 (supplied by FB); T16 removes the r_R = 5 alternative. |
| M13X (273-284) | DEEP, ONE, DEG, TRI, P1 (edge-disjointness of H_alpha, H_alpha*). |
| M13X' (287-294) | R0 lift (LFCV item 6); INV (a)-(b) with E6 for (3,1). |

## 6. Exhaustive location map of Sun instances and index/count steps
| X lines | Step / literal hypotheses to verify |
|---|---|
| 79-83 | W_Qh_vPhi_v consists of [W_Q : W_Q cap Psi] fibres, Psi of index n_v; lcm divisibility; no fibre meets h_jPhi_j (j in Q). |
| 84-86 | Incidence identity sum_j y_j deg_v(j) = sum_F sum_(S_F) y; zero on light fibres since y vanishes off Q. |
| 93-94 | Phi_vW inside X_j, disjoint from D_j by (V1); mu(Phi_vW) >= 1/gcd. |
| 98-99 | p^-1q = ab; pa = qb^-1 in both pieces. |
| 107-121 | Chain: T_1 = lcm(n_d, n_c1) (z_dc = 1); gcd(n_e, T_(r-1)) = 6 (2-, 3-, 5-, w-parts; e = t added after O' vertices); k <= 3; k = 3 => Pi_eW = Pi_ePi_d => Pi_d = (Pi_d cap Pi_e)(Pi_d cap Pi_c1) => Lemma 2 at d; #both = #neither >= 1 (degrees n_d/2, own fibre); lcm with 2^s. |
| 122-124 | gcd(n_v, T_z(V minus {v, i*})) = 6 for v = t (R = O', f = 1) and v != t (f_v = 1). |
| 134-142 | Labels ell_u x_vu and 2^(e_d - 1)5^(h_d)w_d; odd parts coprime; 1-labels isolated (Sun(2)); 2-labels and d pairwise gcd 2 (Sun(3)); value 11/12 > 5/6. |
| 151-154 | Degree 0/4 and degree-3 fourth pair via R4S in x and x'; K4 and bowtie. |
| 160-175 | (V3) labels d_u = ell_u x'_vu, d_d = n_d/2; steps 1-5 (Sun(3), measure 5/6 saturation, Sun(2) parity, Sun(3) disjointness, 2/6 + 2/6 > 1/2). |
| 179-181 | One-tight case: labels ell_a and 2 ell_b coprime (Sun(2)). |
| 187-209 | Apex identity; triangle divisibility and tau <= x1 x2; prime-to-6 part of T_x(S); k <= x_ej with equality criterion. |
| 212-213 | n_4(x) + n_4(x') <= 10; u(x) <= n_1(x'). |
| 217-224 | All three apex pairs non-tight; two (2,4,4) tau-8 triples give three non-tight pairs. |
| 235-263 | FB cases (N), (i)-(vii) with the four N-shapes in case (c). |
| 268-284 | DG (b)/DG* (b) alternatives; triangle counting; diamond; complement of a diamond on five vertices has one triangle. |

## 7. Review contract
Independently re-derive every claim of X. In particular check: (a) SG at v = t in BOTH families, including that the
product equality forbids the e/c_1 fibre sharing in the SAME z-configuration whose d-degrees are n_d/2, and that the own
fibre makes #both >= 1; (b) that R4S and CIS really use no i*-piece and that Lemma 1 (b) / Lemma 1' need only Q = V minus
{v, i*}; (c) label coprimality at t and at p, every marker placement (d, i*, t, p in O', none), including p = t; (d) the use of
accepted DG/DG* exactly at their four-subset hypothesis and orientation; (e) BUD's use of C2 in BOTH families (E3-C2 for alpha*,
M13-A C2* for alpha); (f) every case of FB; (g) the (3,1) transfer through the actual inversion. Return FATAL/MAJOR/MINOR counts per
claim group (Lemmas 1/1'/2; SG; R4S/DEG; CIS/EQS; P2-P4/BUD/T16/ONE/TRI; FB; DEEP/M13X/M13X'), with exact file:line and minimal
repair. An empty findings list is valid. Accept imports only at the table's literal scopes; pending texts are not premises.
Mutation controls to try: X:311-317 (seven thought experiments).

## 8. Packaging metadata
36 inclusive-range excerpts from 20 sources; selected raw UTF-8 bytes 95,752 (<= 100,000). Every whole-file sha256 and
every range in the JSON manifest was re-checked against the files immediately before this write. Byte/hash operations are
packaging, not science runs.
Manifest: `K/review-excerpts-M13X-v1.json`, sha256 `c3e0851d1e801fc69c99271a69247cc03b2f8522c7c1c38308cea6d364b6b056` (8,883 B).
