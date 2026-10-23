# Exploratory pilot: the d = 8 second moment via the x^{7/8} dual (no frozen target, no claim)

**Status.** EXPLORATORY PILOT. No target is frozen and nothing is claimed. Time box: ≤ 2 h from the parent IRC
(≈ 06:50–06:55 PDT, 2026-10-17). The note's first version has mtime 07:21:28 PDT. The route (weak duality with
λ_v = α + (7/8) ln m_v, then complete-graph hypercontractivity) is the parent's. This note checks it, fills in
the constants, and maps it onto KPW.

Lane-local check: `code/verify_d8_pilot.py` → `evidence/verify_d8_pilot.json` (+ `.stdout.txt`). The run of
07:18:26–07:18:56 PDT returned all_ok = true. Section 6 lists every item.

**Go / no-go: GO** for freezing the target "χ(G_{n,8}) = 4 a.a.s.".
- Beyond the structure of χ7 r2, the only new ingredient is a global quadratic decay of the exact second-moment
  exponent at (k, d) = (4, 8). It has a short analytic proof (§§2–4), with every constant checked exactly or in arb.
- The per-row inequality now has two independent proofs: hypercontractivity, and an elementary two-value
  reduction plus arb.
- Every other input is the same as in r2: KPW §§2–4 at general d, W99 small subgraph conditioning, KPW Theorem 10
  (a sketch in KPW), and Molloy–Reed. §5 maps the parameters.

## 1. Setting: the exact count

- k = 4. Cells u = (p, q) carry entries m_u of a doubly stochastic M (Σ_u m_u = 4); J = (1/4)J_4.
- Allowed pairs: u ~ v iff p ≠ r and q ≠ s. This is the graph K_4 × K_4, with 72 unordered pairs and adjacency A.
- B(M, n) is the set of symmetric non-negative integer arrays b on allowed pairs with
  Σ_{v ~ u} b_uv = d m_u n/4 (KPW (3.2)–(3.3), l.620–624).
- KPW (3.4) (l.630–645): |T(M)| = n!·Π_u (d m_u n/4)!/(m_u n/4)! · Σ_{b ∈ B(M,n)} Π_{unordered e} 1/b_e!.
- |P_{n,d}| = (dn)!/((dn/2)! 2^{dn/2}).
- For the S_2 estimate KPW bound the inner sum through Lemma 5 (l.713–723). That relaxation fails at d = 8: at
  (J + I)/2, φ_8 exceeds φ_8(J) (r2 control C2).

## 2. Lemma A (finite-n weak-duality bound; replaces Lemma 5, (3.7) and (3.9) in the S_2 estimate)

For every n with 4 | n and dn even, every M ∈ M ∩ (4/n)Z^{4×4} with support S = {u : m_u > 0}, and every λ ∈ R^S:

  |T(M)|/|P_{n,d}| ≤ P_d(n)·exp(n·U_λ(M)),
  U_λ(M) := C_d + ((d−1)/4) Σ_u m_u ln m_u − (d/4) Σ_{u∈S} m_u λ_u + (1/4) Σ_{e = uv ⊆ S} e^{λ_u + λ_v},
  C_d := (1 − d/2) ln 4 + (d/2) ln d − d/2.

Here P_d(n) is a polynomial that depends on neither M nor λ. This is D8_SCREEN's U_λ.

*Proof.*
- Apply (m/e)^m ≤ m! ≤ e√(m+1)(m/e)^m to every factorial, and n!/Π n_u! ≤ Π (n/n_u)^{n_u} to the colouring
  multinomial. The n ln n terms and the linear terms cancel exactly, as in D8_SCREEN §1.1, because
  Σ_u m_u n/4 = n, Σ_u d m_u n/4 = dn and Σ_e b_e = dn/2.
- There are at most (dn + 1)^{72} arrays b.
- Edges touching an empty cell carry b_e = 0 by (3.3).
- For each b ∈ B(M, n), write b_e = nβ_e. Pointwise weak duality with the constraints Σ_{v ~ u} β_uv = d m_u/4
  gives −Σ_e β_e ln β_e ≤ Σ_{e ⊆ S} e^{μ_u + μ_v − 1} − (d/4) Σ_{u∈S} μ_u m_u for every μ. The kernel is
  max_{β ≥ 0}(−β ln β + βθ) = e^{θ−1} (item S6).
- The substitution μ = λ + (1 − ln 4)/2 turns the result into the displayed form. ∎

No strong duality and no exact inner optimum is needed. Weak duality holds for every λ, as the parent noted.

## 3. Proposition B (closed form at d = 8)

Take λ_u = ln C + (7/8) ln m_u for u ∈ S.
- At d = 8 the entropy terms cancel, since (d − 1)/4 = (d/4)(7/8) (item S1).
- Optimising C gives C² = 16/E(M) (item S2), and then
  U(M) := −10 ln 2 + 4 ln E(M),   E(M) := Σ_{unordered allowed {u,v}} (m_u m_v)^{7/8}.
- U(J) = 8 ln 3 − 12 ln 2 = 2 ln 4 + 8 ln(3/4) = Ψ_8(J), the exponent of (EY)² (item S2). Also E(J) = 9/√2.
- On M, E(M) ≥ Σ_{allowed} m_u m_v = (8 + ‖M‖²)/2 ≥ 9/2 > 0, since t^{7/8} ≥ t on [0, 1].

## 4. Theorem C (global decay)

For every 4×4 row-stochastic M, and in particular every M ∈ M:
  E(M) ≤ E(J) − κ‖M − J‖²,   κ := (441/128)(a² − 1/9),   a := 7^{−(ln 3)/2}.
Hence
  U(M) ≤ U(J) − C_8‖M − J‖²,   C_8 := 4κ/E(J) = (49√2/32)(a² − 1/9).
The arb enclosures (item R2) are:
- a = 0.343385896618341840676…;
- a² − 1/9 = 0.006802762885271439260… > 0;
- κ = 0.023437644003161755578…;
- C_8 = 0.014731481786375019801… (radius ≤ 4·10⁻⁶⁰).

*Proof.*
1. *Inclusion–exclusion* (item S3). Put f = m^{7/8}, with row sums R_p and column sums C_q. Then
   2E = (Σf)² − Σ_p R_p² − Σ_q C_q² + Σ f².
2. *Column Cauchy–Schwarz, then AM–QM over rows.* Σ_q C_q² ≥ (Σf)²/4 gives 2E ≤ (3/4)(Σf)² − ΣR_p² + Σf². Then
   (Σf)² = (ΣR_p)² ≤ 4ΣR_p², and the coefficient 3/4 is positive, so 2E ≤ 2ΣR_p² + Σf². Thus
   E ≤ Σ_p F(r_p), where F(r) := S(r)² + Q(r)/2, S := Σ_j r_j^{7/8}, Q := Σ_j r_j^{7/4} and r_p is row p.
3. *Row inequality:* F(r) ≤ F(U) − κ|r − U|² for every r ∈ Δ_4, where F(U) = 9/(4√2).
   - **Proof 1 (hypercontractivity).**
     - Let g := (r_j^{7/8})_j on {1,…,4} with the uniform measure π, and T_ρ g := Eg + ρ(g − Eg). Then
       F(r) = 18‖T_{1/3} g‖₂² (item S4).
     - T_ρ = H_t with ρ = e^{−t}, H_t = e^{−t(I−K)} and K(x, y) = π(y).
     - Diaconis–Saloff-Coste 1996 (`sources/diaconis-saloffcoste-1996-lsi.pdf`, 6a67ed86…db0c), Theorem A.1
       (layout l.2727–2739): α = (1 − 2/|X|)/log(|X| − 1) = 1/(2 ln 3).
     - Theorem 3.5(ii) (l.1370–1371): for reversible chains ‖H_t‖_{2→q} ≤ 1 whenever e^{4αt} ≥ q − 1.
     - H_t is self-adjoint on L²(π), so ‖H_t‖_{q′→2} = ‖H_t‖_{2→q} with q′ = q/(q − 1), the same duality D–SC use
       at l.2672–2676. At q = 8 this gives ‖T_ρ g‖₂ ≤ ‖g‖_{8/7} for ρ ≤ 7^{−1/(4α)} = a.
     - ρ = 1/3 ≤ a ⟺ ln 7 ≤ 2 ⟺ 7 ≤ e² (item R1; e² > Σ_{j≤4} 2^j/j! = 7, as the parent noted).
     - ‖g‖²_{8/7} = 4^{−7/4} (item S5), so 18‖g‖²_{8/7} = F(U).
     - ‖T_{1/3} g‖² = ‖T_a g‖² − (a² − 1/9) Var_π g ≤ ‖g‖²_{8/7} − (a² − 1/9) Var_π g.
     - By the mean value theorem, |s^{7/8} − t^{7/8}| ≥ (7/8)|s − t| on [0, 1], zero included. So
       Var_π g ≥ (49/64) Var_π r = (49/256)|r − U|².
     - Altogether F(r) ≤ F(U) − 18·(49/256)(a² − 1/9)|r − U|² = F(U) − κ|r − U|².
   - **Proof 2 (elementary; independent of D–SC; constant c = 1/40 > κ).** Let G(r) := F(r) + c|r − U|².
     - *Boundary.* No maximiser lies on the boundary of Δ_4. Moving ε into a zero coordinate raises S by
       ≥ ε^{7/8} − O(ε), while Q and |r − U|² change by O(ε), and S ≥ 1.
     - *Two values.* At an interior maximiser, ∂G/∂r_j = ψ(r_j) = μ, where
       ψ(t) := (7/4)S t^{−1/8} + (7/8)t^{3/4} + 2ct. Since t^{9/8}ψ′(t) = −(7/32)S + (21/32)t^{7/8} + 2c t^{9/8} is
       strictly increasing, ψ is strictly decreasing and then increasing. So the r_j take at most two values, and
       up to permutation r is (x, y, y, y) or (x, x, y, y).
     - *Away from U* (item R4). On both families, outside |x − 1/4| < 1/25, arb subdivision certifies G < F(U):
       8000 pieces each, with a monotone enclosure and a centred-form fallback on 113 pieces of family 1.
     - *Near U.* There h := G − F(U) has h(1/4) = h′(1/4) = 0 exactly. Also h″ < 0 on 400 balls covering
       |x − 1/4| ≤ 1/25, with largest upper bounds −0.2087 and −1.0331.
     - So G ≤ F(U), with equality only at U.
4. *Summing rows.* E(M) ≤ 4F(U) − κ Σ_p |r_p − U|² = E(J) − κ‖M − J‖², since 4F(U) = 9/√2 = E(J).
5. *Logarithm.* U(M) − U(J) = 4 ln(E(M)/E(J)) ≤ 4 ln(1 − κ‖M − J‖²/E(J)) ≤ −C_8‖M − J‖². This uses E(M) > 0,
   which keeps the argument of ln positive, and ln(1 − x) ≤ −x. ∎

Consistency checks (floats):
- min (U − Ψ_8) over 300 random doubly stochastic M is +1.7·10⁻⁵ ≥ 0, and U − Ψ_8 = −8.9·10⁻¹⁶ at J. This is weak
  duality.
- At M_{2/3}, the bound gives U − Ψ_8(J) = −0.046221, against the exact −0.046677.
- The bound is consistent with D8_SCREEN's global margin 0.035008, since C_8 = 0.0147 < 0.035.

## 5. How this slots into KPW at (k, d) = (4, 8)

- **S_2 estimate** (KPW l.997–1033). Use Lemma A plus Theorem C instead of (3.9) plus (3.15). For
  M ∈ M ∩ (4/n)Z^{4×4} ∖ B_4(δ):
  |T(M)|/|P_{n,8}| ≤ P_8(n)·4^{2n}(3/4)^{8n}·e^{−C_8 nδ²},   with nδ² = ε² log² n/81 (KPW l.926–928, with r2's
  (k−1)⁻⁴ remark).
  So S_2 = 4^{2n}(3/4)^{8n}·n^{−Θ(log n)} = o(S_1).
- **Lemma 5 is used only for S_2.** KPW l.775–779 call (3.9) "a sufficient bound … since it will allow us to show
  that the sum in (3.1) receives a negligible contribution due to terms with M away from (1/k)J_k". They then
  obtain the S_1 asymptotics "by improving our previous estimates in (3.6) and (3.7)" through Lemmas 6–9.
  Theorem 10's restriction (l.1610) reuses the S_2 conclusion. A frozen proof must state this as an explicit
  audit row; it is checked here only at l.775–779 and l.997–1033.
- **(H1).** k² − 2k − d + 2 = 2 > 0. The Gaussian coefficient is (k² − 2k − d + 2)/(2(k² − 2k + 2)) = 1/10, matching
  D8_SCREEN's numerical Hessian coefficient −0.10000.
- **(1.2)–(1.3).**
  - (d − 1)/(k − 1)² = 7/9 < 1.
  - Σ_m λ_mδ_m² = (9/2) Σ (7/9)^m/m = (9/2) ln(9/2) = 9 ln(3/√2).
  - E(Y²)/(EY)² → (3/√2)⁹.
- **SSC on P_{n,8}.**
  - λ_i = 7^i/(2i) and δ_i = (−1)^i/3^{i−1}; only δ_1 = −1, so P(Y > 0) → e^{−7/2}.
  - A loop forces Y = 0.
  - P(X_2 = 0 | X_1 = 0) → e^{−49/4} > 0, and P(Simple) → e^{−63/4}.
  - EY grows, since 4(3/4)⁴ = 81/64 > 1.
- **All n.**
  - d = 8 is even, so dn is always even, dk = 32 and k′ = 4. The residues r = 1, 2, 3 all occur. (D8_SCREEN §4
    listed only r = 2 with ℓ = 8; that list was incomplete.)
  - Delete v_1, …, v_r: pairwise at distance ≥ 4, none in a triangle. Their 8r neighbours form an independent set.
  - Add a random perfect matching on them, which gives ℓ = 4r ∈ {4, 8, 12} distinguished edges whose endpoints
    induce a perfect matching.
  - Conditional uniformity is exact: each structure has multinomial(8r; 8, …, 8) preimages (KPW l.1638–1640). The
    argument is r2 §4.3 with C(14,7) replaced by this multinomial.
  - Apply Theorem 10 at (4, 8, 4r) under (H1) plus the new S_2 estimate, then give every v_i colour 3.
- **Lower bound.**
  - Molloy–Reed at q = 3, d = 8: 3(2/3)⁴ = 16/27 < 1 (KPW l.67–68; W99 l.1107 covers every d ≥ 6).
  - Cross-check: verify_rigorous.json C."d=8".

## 6. Evidence (`evidence/verify_d8_pilot.json`; floats only in the sanity and control items)

- **S (sympy, exact).**
  - S1: entropy cancellation.
  - S2: C² = 2d/E, the closed form, E(J) = 9/√2, U(J) = Ψ_8(J).
  - S3: inclusion–exclusion on a generic 4×4 array.
  - S4: S² + Q/2 = 18‖T_{1/3} g‖² for generic g.
  - S5: the ‖·‖_{8/7} value.
  - S6: the weak-duality kernel.
- **R (arb at 200 bits / exact rationals).**
  - R1: 7 < e², also via e > 27/10.
  - R2: a, a² − 1/9 > 0, κ and C_8 (> 0.0147); ρ = 1/3 < a.
  - R3: control, ln 8 > 2, so the route's condition ln(d − 1) ≤ 2 fails at d = 9 (consistent with D8_SCREEN's
    rigorous d = 9 no-go); ln 6, ln 7 < 2.
  - R4: Proof 2 of the row inequality.
- **Sanity (floats).**
  - max (E(M) − E(J))/‖M − J‖² is −0.0641 over 2·10⁴ random doubly stochastic M and −0.1045 over 2·10⁴ random
    row-stochastic M. Both are ≤ −κ.
  - Weak duality as in §4.
- **β-window control (floats).** B_β is the D8_SCREEN §3 bound with λ_v = α + β ln m_v. Over 3300 doubly
  stochastic test matrices (random Sinkhorn, plus (1−t)J + tP for three permutations), the maximum of
  (B_β − B_β(J))/‖M − J‖² is negative for every tested β:
  - 0.80: −0.0115;
  - 0.875: −0.03466;
  - 0.885: −0.035008, which is Ψ_8's own margin;
  - 0.95: −0.0216.

## 7. Correction to D8_SCREEN §3

D8_SCREEN is unchanged (SHA d554d87c07a659fb0e581f817786070380e8f90dd2832cab90c0bd767b23043e); this section
corrects it.
- "g = β ln m, β ∈ [0, 1]: fails at d = 8 for every β" over-generalised. The evidence was a 7-point grid,
  `code/explore_d8_followup.py` F2, β ∈ {0, 0.25, 0.4, 0.5, 0.6, 0.75, 1}. Its multistart maxima of
  B_β − B_β(J) were +9.70, +3.28, +1.58, +0.87, +0.40, +0.032 and +0.0081. β = 7/8 was never tested.
  Theorem C proves B_{7/8} = U ≤ U(J) − C_8‖M − J‖², and the float control above shows a whole window
  β ∈ [0.80, 0.95] with negative margins.
- "Fully separable relaxations fail badly" referred to the tuned (β, γ) families only. With (β, γ) = (7/8, 0), the
  row-separable bound E ≤ Σ_p F(r_p) suffices.
- The routes (b1) and (b2) in §4, and their cost estimates, are superseded for d = 8.

## 8. Risks and what a frozen d = 8 proof must still do

1. The KPW reliance is identical to r2, including Theorem 10, which is a sketch in KPW.
2. An explicit audit row must establish that Lemma 5, (3.7) and (3.9) enter only through the S_2 estimate and
   Theorem 10's restriction (§5). A grep of the pinned KPW layout (before 07:24:04 PDT) found these references only:
   - Lemma 5, (3.7), (3.8) and (3.15) at l.713–779 (statement and derivation of (3.9));
   - l.912, where Lemma 8 with (3.10) gives an asymptotic "which improves the bound already stated in (3.9)" for
     M near J, so S_1 does not use (3.9);
   - l.999–1033 (S_2);
   - l.1034–1138 (proof of Lemma 5).
   §4 has none. Theorem 10's proof cites "the last lines of the proof of Proposition 2(b)" (l.1610). The textual
   check therefore supports the claim; a frozen proof should restate it as an audit row.
3. Import boundary. Proof 1 imports D–SC Theorem A.1, Theorem 3.5(ii) and L² duality (primary source read; the
   parent independently confirmed the normalisation). Proof 2 avoids D–SC, using a hand two-value lemma plus arb.
4. Priority. No d = 8 search has been run beyond the d = 7 audit. Known statuses:
   - KPW {4, 5};
   - AM04 {4, 5, 6};
   - Shi–Wormald {4, 5} (abstract, quoted in the parent audit);
   - NPG's lift result covers d < ℓ_4 = 7.4156…, so not d = 8.
   A bounded search for a uniform-model statement of χ(G_{n,8}) = 4 is needed before any report. A search miss
   would not be novelty.
5. The physics prediction (Krzakala–Pagnani–Weigt, quoted in the parent audit) has q = 4 colourable at c = 8.
   That is consistent with this result, but it is not evidence.
6. The exact-exponent second moment is a natural refinement of KPW's Lemma 5. Experts may regard the d = 8
   extension as routine once the decay inequality is known. No novelty claim.

**Proposed frozen target, if the parent agrees.** "χ(G_{n,8}) = 4 a.a.s.", as a new candidate file
`review/PROOF_CHI8.r1.md`. Its structure is r2's, plus:
- Lemma A;
- Theorem C, with both proofs;
- the audit addendum of risk 2;
- the (4, 8) SSC arithmetic;
- the r ∈ {1, 2, 3} reduction;
- the Molloy–Reed lower bound.
A small exact verifier extension would cover (H1) = 2, 7/9 < 1, 81/64 > 1, 16/27 < 1 and the SSC numbers.
Estimated effort: about 1 h of writing plus minutes of compute.
