**Bridge audit, phys-2: Díaz et al. Maximum Hypothesis → χ(G_{n,5}) = 3**

## Summary

- **Verdict:** the bridge is correct and there is no hidden extra hypothesis. The lane's candidate claim (README.md:82, 84–90) is "F(n) < F(n\*) = 5^{5/2}·25/24 for every n ∈ Δ∖{n\*}, with the closed domain". That is exactly Hypothesis 1.1 (L:159–160). F is the paper's own first definition (L:1313–1316, L:1745–1747), not a modified function.
- **What it settles:** if computer lemmas D (outer cells) and E (central box) are correct, the scheme settles the original H1.1, not a restriction. Together with the paper's conditional proof, that gives χ(G_{n,5}) = 3 a.a.s. for uniform simple 5-regular graphs, for all even n.
  - n ≡ 0 mod 6 is §2 of the paper.
  - n ≡ 2 and 4 mod 6 go through Theorem 6.1, which uses the same H1.1. No new hypothesis enters there.
- **Scheme check:** at the level of inequalities and coverage I found no real defect in duality, interval direction, boundary handling, domain cover or the local-to-global step. The real items are minor: a README hash typo, gate/claim wording that no longer matches what was built, and sketched or loosely worded steps inside the paper itself.
- **Checker status (read from the JSON outputs, not rechecked by me):**
  - Checker A passed all 9 cones.
  - Checker B's batch 1 and batch 2 together cover all 9 facets, with `ALL_PASS` true in both.
  - Checker B's central-box check passed.

## Files

**Paper and sources** (`L` = `sources/diaz2009-3col-preprint.layout.txt`, the 2009-10-20 preprint)
- `L:159-165`: H1.1 and Theorem 1.1. `L:152-154`: intro claim about the boundary.
- `L:191-289`: small-subgraph-conditioning (SSC) theorem and the proof for 6 | n.
- `L:300-611`: §3 (EY and joint moments with cycles). `L:614-733`: §4, the exact second moment (4.1)–(4.7).
- `L:740-1355`: §5 up to Lemma 5.6. `L:1356-1519`: Lemmas 5.7–5.10 and Theorem 5.1. `L:1525-1667`: §6. `L:1670-1895`: §7.
- `sources/acg-1812.09691v4.txt:68-70`: status attestation. `:1544-1545`: [18] is J. Graph Theory 61 (2009) 157–191.

**Lane README** (`README.md`)
- `:11` sources; `:15-25` exact objects and target; `:31` gate.
- `:53-66` frozen outer scheme; `:68-74` central scheme; `:76-79` slice-concavity domain conditions; `:81-93` candidate certificate and proof map.

**Checkers and evidence**
- `institute/runs/six-lane-2026-10-16/review/slice-concavity-parent-verification.md`: parent review of the slice-concavity lemma.
- `code/cert_cells.py:74-170`: checker A's mathematics.
- `outer/code/cert_cells.py:196-216`: the `--require-r0` guard (a FAIL verdict whenever a reason is set).
- `outer/README.md`, `outer/evidence/summary.json`: 9/9 PASS.
- `checkerB/code/cells_iv.py:8-24, 248-273`: root checks and the pinned trusted r1.
- `checkerB/evidence/cells_iv_batch{1,2}.json`, `central_iv_r0_1e-4_eps3_20_NC8.json`: checker B results.
- `evidence/anchors_lemma58.json`: summary keys plus `:416`; `code/anchors_lemma58.py:8-19, 62-76, 901-1064`.

## Architecture (dependency map)

```
Lemma A  slice concavity of ψ (exact polynomial positivity; parent-verified)
   ├─(+ concavity of H on the closed slice)→ Lemma C: a_u ≥ Ψ*(z)  (supergradient at interior m0, max over conv S)
Lemma B  weak pairing duality (Σ_u⟨z^u,m^u⟩=0 on feasible d) + per-class scaling (3/2)n ln n
   ├→ Lemma D outer: ln F ≤ U_y < L* on 'D' cells; 9 cones = Δ; 'C' cells ⊂ B0
   └→ Lemma E centre: ln F ≤ Ubar(η) < L* on B0∖{n*}   [(W) duality, (Q) Krawczyk/Loewner/Gershgorin, (C) strict concavity]
Lemma F  F(n*) = e^{L*} (b feasible; f(b)=L*; Lemma B with y=0)
   ⇒ H1.1 (closed Δ, strict)
H1.1 + L5.5 ⇒ L5.6 ⇒ L5.8 bullets 1–2 ;  [L5.7 lattice, L5.8 bullets 3–4: anchors, exact]
   ⇒ L5.9 (Euler–Maclaurin [1], Laplace via Wong IX.5.3) + L5.10 (compactness, q = O(n^162)) ⇒ Thm 5.1 = (2.5)
(2.4) Lemma 3.1 ; (2.2)/(3.2) §3 ; (2.3)  ⇒ SSC Thm 2.1 [17, Cor 4.2] (i)–(iv) ⇒ P(Y>0 | X1=0) → 1, 6 | n
   ⇒ condition on X1 = X2 = 0 ⇒ simple G_{n,5}; non-bipartite a.a.s. (L:50) ⇒ χ = 3
§6: Thm 6.1 on Ω_n (6.1), (3.2) for Ŷ, (6.2) via (6.3) [Lemmas 5.1/5.6/5.9 ⇒ H1.1 only]
   ⇒ n ≡ 2 (j* = 4), n ≡ 4 (j* = 8): delete/reinsert adjacent pairs (L:1646-1667)
```

## Report

### 1. Hypothesis 1.1 and its definitions, mapped to the lane

Exact text:
- **H1.1 (L:159–160):** "The four-variable function F (n) has a unique global maximum over its domain at the point (1/9, 1/9, 1/9, 1/9)."
- **Domain (L:1313–1314, (5.23) at L:1307–1311; (7.1) at L:1678–1681):** "the set of all nonnegative real vectors n … satisfying (5.23)". All inequalities are non-strict, so the domain is closed. It equals {all nine n^{ij} ≥ 0}, i.e. Δ = (1/3)·(Birkhoff polytope).
- **F (L:1315–1316):** "define F (n) to be the maximum of F̂ (d) over D subject to the constraints in (4.5)".
- **Boundary convention:** 0^0 = 1 and 0 ln 0 = 0 (L:765, L:1745). The max exists because the domain is compact (L:1746–1747).

| Paper object (location) | Lane object | My check |
|---|---|---|
| Spectra: row and column sums ≥ 1, entry sum 5, \|S\| = 36 (L:653–658, 1693–1703) | README:16 | ✓ recounted: 56 − 20 = 36 |
| w_s (L:710); Φ (5.7)/(7.7) (L:993–1001, 1750–1753) | w_s, Φ | ✓ inclusion–exclusion matches |
| Pairing (4.3)/(7.5) (L:649, 1725) | 18 edges of K3×K3; C_u = +1 / −1 at the two ends (README:54) | ✓ each (u,k) is an end of exactly one edge, so Σ_u⟨z^u,m^u⟩ = 0 on feasible d |
| F̂ (L:745–757, 1728–1741) | ln F̂ = Σ d ln(w/d) + ½ Σ_{36 entries} m ln m | ✓ the ½ accounts for each edge appearing twice |
| G̃ (L:1181–1191); F̃ (7.11) | ψ(m) = Σ m(½ ln m − ln μ(m)); L(m) = Σ_u ψ(m^u) | ✓ ψ(c m̂) = c ψ(m̂) + (3/2) c ln c, since (3/2) = −1 + 5/2 |
| Lemma 5.5 centre (L:1169–1170, 1293–1294) | m\* = 5/36, μ\* = 8100^{−1/5}, b_s = w_s/8100 | ✓ F̂(b) = 8100·(5/36)^{5/2} = 5^{5/2}·25/24 |
| M = 25/24 (L:1325–1327) | L\* = (5/2) ln 5 + ln(25/24) (README:63) | ✓ |

Scalar and sign checks I re-derived by hand:
- μ(m0) = μ0·Φ(μ0)^{−1/5}. So the slice gradient of ψ at m0 is ½ ln m0 − ln μ0 modulo span(1), and ψ(m0) = ½ Σ m0 ln m0 + ln Φ(μ0) − ⟨ln μ0, m0⟩. Both match README:58–60.
- Ψ\*(0) = ψ((5/4)·1) = (5/2) ln(5/4) + ln 900. Hence U_0(n\*) = Ubar(0) = Ψ\*(0) − 3 ln 3 = L\*: the bound is exactly tight at the centre.
- Ψ\*(z + t·1) = Ψ\*(z) + 5t, which is consistent with the Taylor form at README:71.

**Sufficiency.** H1.1 is used only through Lemma 5.6 (L:1329–1355). Lemma 5.6 needs exactly "F(n) < F(n\*) for all n ≠ n\*" plus per-class uniqueness at n\* (Lemma 5.5). Lemma A gives that uniqueness independently.

The two other computational facts the proof needs are not consequences of H1.1, but the anchors prove them exactly:
- nondegeneracy of the Hessian at b (Lemma 5.8, bullet 3);
- the lattice structure of Lemma 5.7.

### 2. Conditional implication, H1.1 ⇒ χ = 3 for all even n

| Step | Location | In the paper | Uses H1.1? | Lane coverage |
|---|---|---|---|---|
| χ ≥ 3 a.a.s. (not bipartite) | L:50–51 | imported, "widely known" | no | not covered (standard) |
| SSC Theorem 2.1 | L:191–217 | imported, [17, Cor 4.2] | no | not covered |
| (i) λ_k = 4^k/(2k) | L:224 | imported | no | anchors take λ_k from the paper (anchors_lemma58.py:939) |
| (ii) δ_k, (3.1)/(3.2) | L:436–611 | proved; higher moments sketched at L:597–611 | no | partly: transition-matrix and trace identities exact (`5_delta_k_(2.2)` MATCH); saddle-point and cycle-overlap argument not redone |
| (iii) (2.3) | L:229–254 | computation | no | `5_sum_lambda_delta^2_(2.3)` MATCH |
| (2.4) via Lemma 3.1 | L:300–435 (Stirling step omitted, L:433–435) | proved | no | `5_EY_(2.4)` MATCH |
| Lemma 5.1, q = O(n^162) | L:782–895 | proved | no | `5_h(n)_(5.1)` and `4_g_b` MATCH |
| Lemma 5.3 boundary "by continuity" | L:1027–1028 | asserted only | no | bypassed: Lemma B works in d-space (README:85) |
| Lemmas 5.4, 5.5 | L:1134–1299 | proved (P, Q, R positive) | no | Lemma A plus `4_e^f(b)` MATCH give an independent route |
| Lemma 5.6 | L:1325–1355 | from H1.1 + Lemma 5.5 | **yes** | this is exactly the certified target |
| Lemma 5.7: rank 23, integer coefficients, constants in (1/6)Z, 6 \| n | L:1360–1377, 1414–1415 | "proof we omit" | no | rank, parametrisation, lattice-basis checks all MATCH/PASS; lcm of constants = 6 |
| Lemma 5.8 bullets 3–4: det H̃, negative definite, g̃(b̃) | L:1422–1437 | "straightforward computations" | no | `3_detH`, `3_negative_definite`, `4_g_b` MATCH |
| Lemma 5.9: Euler–Maclaurin and Laplace | L:1441–1483 | imported analysis; Euler–Maclaurin step loosely stated | **yes** | constants only (`5_Lemma_5.9_constant`, `5_EY2_(2.5)` MATCH) |
| Lemma 5.10 and Theorem 5.1 | L:1486–1519 | proved | **yes** | logic checked by me |
| Condition (iv) | L:263–278 | combination of the above | **yes** | ratio MATCH; ratio equals exp(Σλ_kδ_k²) MATCH |
| Transfer to simple graphs | L:279–286 | standard | no | — |
| Theorem 6.1, (6.1)–(6.4) | L:1533–1645 | sketched | **yes**, through (6.3) | not covered |
| n ≡ 2 and n ≡ 4 mod 6 | L:1646–1667 | trick from [13] §3, sketched | no new hypothesis | not covered |

### 3. Scheme audit (inequalities and coverage only)

**Outer chain** (README:55–62; code/cert_cells.py:74–121)
- Pure weak duality: it holds for every n, every fibre point d and every y, with no constraint qualification needed. Empty classes are handled exactly: n^u = 0 is skipped (code/cert_cells.py:112), and the true contribution of such a class is also 0.
- The proof that a_u ≥ Ψ\*(z) is valid. It can be simplified: ψ is concave on the half-open segment [m0, m̂) by Lemma A, H is concave on the closed slice by its definition as a value function, and Σ m ln m is continuous. Together these give ψ(m̂) ≤ ψ(m0) + ⟨g, m̂ − m0⟩ at boundary points m̂. This removes the Berge and Gale–Klee–Rockafellar steps from the trusted base (README:78).
- Taking the max over S is the same as the max over the 8 vertices of Lemma 5.2 (L:979–989). I re-enumerated those vertices myself. Checker B's 8-candidate reduction is therefore exact.
- U_y is convex in n, so checking the 5 vertices suffices. A single y and μ0 are used for the whole cell.
- Interval direction: the acceptance test is the ball `LSTAR − U > 0` (code/cert_cells.py:116–118), and a_u is computed as an enclosure, not an estimate. Direction is correct.

**Cover**
- Δ = Birkhoff/3, whose 9 facets are tetrahedra. Cones from the interior point n\* over those facets cover Δ.
- The two children of an edge bisection cover the parent (code/cert_cells.py:139–145).
- 'C' cells lie inside B0 by convexity. r1 is pinned to the frozen 1/10000 in both trusted checkers (outer/code/cert_cells.py:206–213; cells_iv.py:271–273). The older code/cert_cells.py reads r0 from the certificate; only the `--require-r0` invocation counts.

**Central** (README:69–72)
- **(W):** weak duality, valid.
- **(Q):** Loewner directions are correct.
  - X ⪰ Xmin implies R ⪯ R(0) + ε(I − J/4). This needs col(B3) = 1⊥.
  - S2 ⪯ (1 + ε_L)·S2c implies S2⁻¹ ⪰ S2c⁻¹/(1 + ε_L), which is the side needed for a lower bound on X.
  - A Krawczyk interior root is the global maximiser over the closed slice, because ψ is concave there. Then ∇Ψ\* = m̂(z) and Hess Ψ\* = B3 X⁻¹ B3ᵀ.
  - The Taylor step stays inside the convex, symmetric c-box, and the γ bound covers every z^u(η).
- **(C):** n^u > 0 on B0, Ubar(0) = L\*, ∇Ubar(0) = 0, and Hess Ubar ≺ 0 on B0, so Ubar < L\* away from 0. Checker B's vertex-based (C) step is valid: λ_max(Hess Ubar(η)) is convex in η, because the matrix is an affine part plus Σ(3/2)A_uA_uᵀ/n^u(η) with 1/n^u convex.

**Local-to-global:** there is no gap. The cover is global and B0 is an explicit box matched to r1.

### 4. Defects and blockers

1. **Provenance (minor).** README:11 gives the layout-file sha256 prefix as `da12c0eb…`. Two machine receipts give `da12c0eecb77…39ea` (evidence/anchors_lemma58.json:416, evidence/indep_slice_check.json:21). [INFERENCE] The README entry is a typo. Recompute `shasum -a 256 sources/diaz2009-3col-preprint.layout.txt` to close it.
2. **Wording (minor).** Three phrases no longer match what was built:
   - README:24 states the target as "L(m) < L(m\*) on M∖{m\*}".
   - Gate (a) at README:31 asks for a "strict-concavity neighbourhood of m\*".
   - Gate (c) asks for "primal d-space and dual μ/Φ" evaluators.

   What was actually built is an n-space dual majorant, checked by two independent replays of the same dual certificate. H1.1 needs only the n-form; the m-form follows from it plus Lemma 5.5 or Lemma A. A primal evaluator can only give lower bounds, so it could not be the second upper-bound checker anyway. Fix the wording; no new work is needed.
3. **Notation (cosmetic).** README:72 uses a_u for the gradient vector A_u of n^u, which clashes with the outer constant a_u (README:58).
4. **Ledger out of date (procedural).** README:91 still says checker B is pending. The checker B JSON shows batch 1 ∪ batch 2 = all 9 facets with `ALL_PASS`, and the central check passing. `cells_iv_all9_final` has only a `.time` file so far.
5. **Paper-level issues** (trust inherited from the paper, not lane defects):
   - (a) L:152–154: "we show that the boundary of its domain contains no local maximizer". The body never proves this; Lemma 5.4 is per class, on D0(1/9). The proof doesn't use it, and the lane doesn't cite it.
   - (b) L:284–285: "Because P (X2 = 0) is bounded away from 0". This should be conditional on X1 = 0; it follows from condition (i).
   - (c) L:1307 typo: "n0,0 , n0,1 , n1,0 and n1,0".
   - (d) Lemma 5.7's displayed equation (L:1364–1367) uses ambiguous notation. The anchors read it as (4.3) with r = 1 and confirm the 18 rows are exactly the distinct (4.3) constraints.
   - (e) Steps the lane did not verify:
     - L:1621–1625 (6.3): "from Lemmata 5.1 and 5.6". It also needs the Lemma 5.9 lower bound, which still depends only on H1.1.
     - Higher joint moments (L:597–611).
     - The Euler–Maclaurin uniformity wording (L:1464–1466).
     - In §6: condition (i) on Ω_n, the "without loss of generality, u and v adjacent" step, and uniformity of G0 (L:1646–1662).

There is no mathematical blocker in the scheme.

### 5. Theorem hypotheses the final claim rests on

- **SSC:** λ_k > 0 and δ_k ≥ −1; δ_1 = −1 and |δ_k| < 1 for k ≥ 2, so the conditioning event E is {X_1 = 0}; conditions (i)–(iv).
- **Laplace (Wong IX.5.3):** unique interior maximiser b̃ of f̃ on the compact cube Q̃, negative-definite Hessian, f̃ and g̃ smooth, g̃(b̃) ≠ 0.
- **Lattice sum:** J̃ = (1/n)Z^301 ∩ Q̃, which needs the integer parametrisation of Lemma 5.7 and 6 | n.
- **Lemma 5.10:** f continuous on the compact set D; at most (n+1)^324 terms; q = O(n^162) uniformly.
- **Lane-side theorems:** Krawczyk existence and uniqueness; Danskin plus the implicit function theorem for Ψ\*; Loewner order inversion; Gershgorin for symmetric interval matrices; convexity of U_y; edge-bisection cover; the facet structure of the Birkhoff polytope (Birkhoff–von Neumann).

### 6. Original target or a restriction?

It is the original target. The scheme bounds the paper's own F everywhere on the closed Δ, all 9 cones are certified directly with no symmetry argument, and F(n\*) is attained. So, if Lemmas D and E are correct, H1.1 holds exactly as stated, and with it the paper's Theorem 1.1, for every even n.

The remaining trust lies in three places:
- the two checker implementations (results observed, not rechecked by me);
- the written Lemmas A–C, which I find correct;
- the paper's imported and sketched steps listed above. The paper was published as JGT 61 (2009) 157–191 (acg-1812.09691v4.txt:1544–1545). [INFERENCE] The published text is assumed to match this preprint; I did not compare them.

Priority and significance are not assessed here.

**Primary source:** https://web.archive.org/web/20210315161735/users.monash.edu.au/~nwormald/papers/3col.pdf (as recorded at README:11; not re-fetched) · https://arxiv.org/abs/1812.09691v4

### 7. Read scope

- **Read in full:** layout.txt lines 1–1967; README.md (re-read after it grew to include the 01:14:51 entry); outer/README.md; the parent slice-concavity review.
- **Read in part:**
  - raw.txt lines 929–1123;
  - acg text lines 39–113 and 1544–1545;
  - code/cert_cells.py lines 74–170;
  - outer/code/cert_cells.py lines 196–226, plus a grep;
  - checkerB/code/cells_iv.py by grep only;
  - anchors_lemma58.py by grep only.
- **Evidence (top-level summary fields only):** anchors_lemma58.json, outer/evidence/summary.json lines 1–300, checker B batch 1, batch 2 and central JSONs.
- **Not done:** I opened no PDF, ran no code and recomputed no hashes. Every pass/fail status above comes from recorded JSON fields.
