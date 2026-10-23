# CLAIM: the Maximum Hypothesis of Díaz–Kaporis–Kemkes–Kirousis–Pérez–Wormald holds; hence χ(G_{n,5}) = 3 a.a.s.

Status: computer-assisted candidate. Checker A is complete for every computer lemma. Independent checker B (mpmath.iv) results are recorded in §6. The claim is not yet hostile-reviewed. Every file named here is pinned in `MANIFEST.sha256`. Revisions get new file names; pinned files are never edited.
Lane: `physics/evidence/six-lane-20261016/random5reg-colour/` (run six-lane-2026-10-16, slot phys-2). Host-clock times are PDT.

## 1. Exact statement

**Objects** (primary preprint, §§4, 5.1, 7).
- **Spectra S.** All 2×2 nonnegative integer matrices s = (s_{−1,−1}, s_{−1,1}; s_{1,−1}, s_{1,1}) with entry sum 5, both row sums ≥ 1 and both column sums ≥ 1. |S| = 36, and w_s = 5!/∏ s_{r,t}!.
- **Domain Δ (7.1).** The set of n = (n1, n2, n3, n4) ≥ 0 with n1+n2 ≤ 1/3, n3+n4 ≤ 1/3, n1+n3 ≤ 1/3, n2+n4 ≤ 1/3 and n1+n2+n3+n4 ≥ 1/3.
- **Overlap values (7.2).** n^{00} = n1, n^{01} = n2, n^{02} = 1/3 − n1 − n2, n^{10} = n3, n^{11} = n4, n^{12} = 1/3 − n3 − n4, n^{20} = 1/3 − n1 − n3, n^{21} = 1/3 − n2 − n4, n^{22} = n1+n2+n3+n4 − 1/3. So Δ = {n : all nine n^{ij} ≥ 0}, i.e. 1/3 times the Birkhoff polytope B_3.
- **Fibre of n.** Arrays d = (d^{ij}_s) ≥ 0 with Σ_s d^{ij}_s = n^{ij} (7.4) and m^{ij}_{r,t} = m^{i+r,j+t}_{−r,−t} (7.5), where m^{ij} = Σ_s d^{ij}_s s (7.3) and indices are taken mod 3.
- **Objective (7.6).** F̂(d) = ∏_{i,j,s} (w_s/d^{ij}_s)^{d^{ij}_s} · ∏_{i,j,r,t} (m^{ij}_{r,t})^{m^{ij}_{r,t}/2}, with 0^0 = 1. F(n) := max of F̂ over the fibre of n. Write f = ln F̂, L* := (5/2) ln 5 + ln(25/24), and n* = (1/9, 1/9, 1/9, 1/9).

**Theorem (certified, computer-assisted).** For every n ∈ Δ with n ≠ n*, F(n) < F(n*) = 5^{5/2}·25/24 = e^{L*}.

The domain is closed: boundary points with some n^{ij} = 0 are included. This is Hypothesis 1.1 of the primary preprint exactly as stated there. Combined with that paper's Theorem 1.1, it gives χ(G_{n,5}) = 3 asymptotically almost surely (§2 lists every place the hypothesis is used).

## 2. Primary source

Source: `sources/diaz2009-3col-preprint.pdf`, the Wayback snapshot of 2021-03-15 of users.monash.edu.au/~nwormald/papers/3col.pdf (33 pages; sha256 5e317a44…28b1). This is the author preprint of J. Graph Theory 61 (2009) 157–191.

PDF page numbers equal the printed page numbers. Prose below is quoted verbatim. Formulas are transcribed from the PDF, because text extraction garbles their layout.

**Statements quoted in §1**
- **p. 4, Hypothesis 1.1.** "Hypothesis 1.1 (Maximum Hypothesis) The four-variable function F (n) has a unique global maximum over its domain at the point (1/9, 1/9, 1/9, 1/9)."
- **p. 4, Theorem 1.1.** "Theorem 1.1 Under the Maximum Hypothesis, the chromatic number of Gn,5 is a.a.s. 3."
- **p. 4, the ordinary-colouring remark** (used as our positive control). "for the case of the ordinary (not balanced locally rainbow) colourings there exists an analogue to function F which also has a local maximum at the point (1/9, 1/9, 1/9, 1/9) but unfortunately this is not the global maximum."
- **pp. 28–29, definitions (7.1)–(7.6).** These are transcribed in §1. The prose reads: "We first define the domain of F . This is the set of all nonnegative real vectors n = (n1 , . . . , n4 ) satisfying" (7.1); "A spectrum s is a 2 × 2 nonnegative integer matrix such that each row and column sum is at least 1, and the sum of all four entries is 5"; "(We follow the convention that 0^0 equals 1.) … Then, we set F (n) to be the value of this maximum."
- **p. 17, Lemma 5.3.** "Lemma 5.3 For any m in the interior of M, each of the nine systems in (5.8) has a unique positive solution. Moreover, in terms of the solutions of these systems, F̃(m) = ∏ ((m^{ij}_{r,t})^{1/2}/µ^{ij}_{r,t})^{m^{ij}_{r,t}}, and the equation remains valid for m on the boundary of M if the expression on the right is extended by continuity." Our certificate does not depend on this lemma (Lemma B below bounds F̂ directly).

**Every use of Hypothesis 1.1 in the conditional proof.** None of these uses anything stronger than the statement certified here.
- **p. 4, overview.** "determine its asymptotic value, under the Maximum Hypothesis, in Section 5."
- **p. 6, (2.5).** "and, under the Maximum Hypothesis," E(Y²) ∼ … (25/24)^n; this establishes condition (iv) and proves Theorem 1.1 for 6 | n.
- **p. 14.** "In this section, we complete the proof of the main theorem given in Section 2 by showing that equation (2.5) holds, assuming the Maximum Hypothesis."
- **p. 15.** "In the next subsection we determine the value of M under the Maximum Hypothesis."
- **p. 22, Lemma 5.6.** "Under the Maximum Hypothesis, the function f has a unique maximizer in D at b. Moreover, M := max_{d∈D} 5^{−5/2} e^{f(d)} = 25/24." Its proof says "The Maximum Hypothesis implies that any maximizer of F̂ on D must satisfy Σ_{s∈S} d^{i,j}_s = 1/9, for all i, j ∈ Z3."
- **p. 24, Lemma 5.8.** First two bullets: "Under the Maximum Hypothesis, f has a unique maximum in D at b" and the analogue for f̃ on Q̃. Also on p. 24, Lemma 5.9: "Under the Maximum Hypothesis".
- **p. 25.** Lemma 5.10: "Under the Maximum Hypothesis, there exists some positive real α < e^{f(b)} …". Theorem 5.1: "Under the maximum hypothesis".
- **p. 26, Theorem 6.1** (the n ≢ 0 mod 6 reduction): "Under the Maximum Hypothesis, G a.a.s. has a 3-colouring in which …".
- **p. 27, proof of (6.3).** "It is easy to see, from Lemmata 5.1 and 5.6, that under the maximum hypothesis, the contribution to E(Y²) from d where d^{i,j}_s ∼ b^{i,j}_s is E(Y²)(1 + o(1))."
- **p. 28, Theorem 1.1 for n ≡ 2, 4 (mod 6).** "Therefore G0 is distributed as the random structures in Theorem 6.1 with j* = 4. Thus, by Theorem 6.1, …". The case n ≢ 0 mod 6 therefore uses the same F and the same hypothesis. There is no separate hypothesis.

**Other numerical or omitted steps in the paper, and how they are covered**
- **p. 9.** "We omit the calculations." This is a Stirling step for EY. Reproduced exactly as (2.4)/(2.5) constants in `evidence/anchors_lemma58.json`.
- **p. 21, Lemma 5.5.** "which is strictly positive, so µ1 = µ4" (and likewise for Q and R). These polynomials have only positive coefficients as printed. Lemma 5.5 is used only at n* (Lemma F below gives F(n*) independently).
- **p. 23, Lemma 5.7.** "First we need the following result, whose proof we omit". Rank 23 and an integer parametrisation are reproduced exactly (`evidence/anchors_lemma58.json`).
- **p. 24, Lemma 5.8.** "From Lemma 5.6 and by straightforward computations …". The determinant det H̃ = −2^175 3^1078 5^310 7^12 11^14 13·17·79^4, the negative definiteness of H̃ and g̃(b̃) = 2^90 3^558 5^171 are reproduced exactly (same file).
- **p. 30, Theorem 7.1.** "The Hessian, computed using Maple, shows that F̂ has a local maximum here". This is superseded by the theorem above.
- **p. 31.** "This was numerically confirmed with the help of a computer." This refers to the concavity of ln G̃ on M0(n^{ij}), and is replaced by Lemma A. The grid search, which "avoids a fine layer of width 1/1000 around the boundary", is replaced by Lemmas D and E.

## 3. Written lemmas

Notation:
- Classes u = (i, j) ↔ 3i + j. A 2×2 matrix is a 4-vector in the order (−1,−1), (−1,1), (1,−1), (1,1).
- K3×K3 has 18 edges e = (u, k, v, k′). For y ∈ R^18, z^u = C_u y, where C_u[k, e] = +1 if (u, k) is the first end of e and −1 if it is the second.
- conv(S) = M0(1) is the set {m̂ : Σ m̂ = 5} reachable by probability vectors on S.
- For m in the cone K = cone(S): H(m) := max{Σ_s d_s ln(w_s/d_s) : d ≥ 0, Σ_s d_s s = m}, and ψ(m) := H(m) + ½ Σ_k m_k ln m_k, with 0 ln 0 = 0.
- Ψ*(z) := max_{m̂ ∈ conv(S)} [ψ(m̂) + ⟨z, m̂⟩].

### Lemma A (slice concavity)
Statement:
- (A1) ψ is strictly concave on each open slice {Σm = c} ∩ int K.
- (A2) Tangent bound up to the boundary: for every m0 in the relative interior of the slice conv(S) (Σ = 5) and every m̂ ∈ conv(S), ψ(m̂) ≤ ψ(m0) + ⟨∇ψ(m0), m̂ − m0⟩.

*Proof.*
- **Parametrisation.** For μ ∈ (0,∞)^4 put d_s = w_s μ^s, Φ = Σ_s d_s, m(μ) = Σ_s d_s s and S2(μ) = Σ_s d_s s s^T.
- **Bijection.** θ = ln μ ↦ m is a bijection of R^4 onto int K, with Jacobian ∂m/∂θ = S2 ≻ 0. The normalised family p ∝ w e^{⟨θ,s⟩} is a full exponential family on 36 points, whose mean map is a diffeomorphism onto the relative interior of the slice. Homogeneity gives m(cμ) = c^5 m(μ).
- **Max-entropy duality.** For m = m(μ), Gibbs' inequality gives H(m) = Σ_s d_s ln(w_s/d_s) = −⟨ln μ, m⟩. Indeed, any feasible d′ gives Σ d′ ln(w/d′) = −⟨ln μ, m⟩ − KL(d′‖d) − (Σd′ − Σd), where KL(d′‖d) = Σ d′ ln(d′/d) − Σd′ + Σd ≥ 0, and Σd′ = Σm/5 = Σd.
- **Hessian.** It follows that H is C^∞ on int K, with ∇H = −ln μ − (1/5)1 and ∇²H = −S2^{-1}. Hence Hess ψ = ½ D^{-1} − S2^{-1} with D = diag(m).
- **Reformulation on m⊥.** S2·1 = 5m, because every spectrum sums to 5. Set X = D^{1/2} S2^{-1} D^{1/2} and q = D^{1/2}1. Then Xq = q/5, so q⊥ is X-invariant. Negative definiteness of Hess ψ on 1⊥ is therefore equivalent to u^T S2 u < 2 u^T D u for every nonzero u ⊥ m.
- **Polynomial form.** Write u = u′ + c1 with u′ ⊥ m. For Mpoly := 5Φ(2D − S2) + 3mm^T one gets Mpoly·1 = 0 and u^T Mpoly u = 5Φ(2u′^T D u′ − u′^T S2 u′). So the condition holds iff Mpoly ⪰ 0 with kernel exactly span(1), iff the leading 3×3 block of Mpoly is positive definite.
- **Positivity.** That block's three leading principal minors are integer polynomials in μ of degrees 10, 20 and 30, with 154, 949 and 2766 terms. Every coefficient is strictly positive, and this holds for each of the four choices of dropped index (`evidence/slice_minors_rainbow.json`). Hence the minors are positive on (0,∞)^4, which gives strict concavity on every open slice.
- **Boundary: proof of (A2)** (segment argument, which needs no global continuity theorem).
  - H is concave on the closed polytope conv(S) directly from its definition as a value function: if d′ attains H(m′) and d″ attains H(m″), then td′ + (1−t)d″ is feasible for tm′ + (1−t)m″, and Σ d ln(w/d) is concave.
  - Put m_t = m0 + t(m̂ − m0). For 0 ≤ t < 1, m_t is in the relative interior, so (A1) gives ψ(m_t) ≤ ψ(m0) + t⟨∇ψ(m0), m̂ − m0⟩.
  - Concavity of H on the closed segment gives H(m_t) ≥ (1−t)H(m0) + tH(m̂), so liminf_{t→1} H(m_t) ≥ H(m̂).
  - ½Σ m ln m is continuous on the closed slice (0 ln 0 = 0).
  - Hence ψ(m̂) ≤ liminf_{t→1} ψ(m_t) ≤ ψ(m0) + ⟨∇ψ(m0), m̂ − m0⟩. (Berge / Gale–Klee–Rockafellar, cited in an earlier README entry, are no longer needed.)
- **No uniform margin.** The minors are not claimed positive on the boundary of the orthant. The supremum of the ratio u^T S2 u / u^T D u is exactly 2, approached only in limits (independent finding of checker SliceConcavityIndep). Only (A2) is used at boundary points. ∎

### Lemma B (weak pairing duality)
For every n ∈ Δ, every d in the fibre of n and every y ∈ R^18:

f(d) ≤ Σ_u [ n^u Ψ*(z^u) + (3/2) n^u ln n^u ], with z^u = C_u y.

Classes with n^u = 0 contribute 0.

*Proof.*
- **Pairing.** Σ_u ⟨z^u, m^u⟩ = Σ_e y_e (m^{u_e}_{k_e} − m^{v_e}_{k′_e}) = 0 by (7.5). So f(d) = Σ_u T_u with T_u = Σ_s d^u_s ln(w_s/d^u_s) + ½ Σ_k m^u_k ln m^u_k + ⟨z^u, m^u⟩.
- **Empty classes.** If n^u = 0, then d^u = 0, m^u = 0 and T_u = 0.
- **Non-empty classes.** Otherwise write d^u = n^u p with Σp = 1 and m̂ = Σ_s p_s s ∈ conv(S), so that Σ m̂ = 5. Then:
  - Σ_s d ln(w/d) = n^u Σ_s p ln(w/p) − n^u ln n^u ≤ n^u H(m̂) − n^u ln n^u;
  - ½ Σ m ln m = n^u · ½ Σ m̂ ln m̂ + (5/2) n^u ln n^u.
- **Conclusion.** Therefore T_u ≤ n^u [ψ(m̂) + ⟨z^u, m̂⟩] + (3/2) n^u ln n^u ≤ n^u Ψ*(z^u) + (3/2) n^u ln n^u. Taking the maximum over the fibre gives the same bound for ln F(n).

The paper's Lemma 5.3 is not used. ∎

### Lemma C (inner bound)
For every z ∈ R^4 and every μ0 ∈ (0,∞)^4, let Φ0 = Φ(μ0), m0 = m(μ0)/Φ0 (so Σ m0 = 5), ψ0 = ½ Σ m0 ln m0 + ln Φ0 − ⟨ln μ0, m0⟩, and g = ½ ln m0 − ln μ0 + z. Then

Ψ*(z) ≤ a(z; μ0) := ψ0 + ⟨z, m0⟩ + max_{s∈S} ⟨g, s − m0⟩.

*Proof.*
- **m0 is interior.** m0 is the mean of the strictly positive probability vector p_s = w_s μ0^s/Φ0 on S. It is therefore in the relative interior of conv(S), since every spectrum has positive weight.
- **Value at m0.** The Gibbs step in Lemma A, applied on the slice, gives H(m0) = ln Φ0 − ⟨ln μ0, m0⟩, hence ψ(m0) = ψ0.
- **Gradient at m0.** ψ is differentiable at m0 (H is C^∞ in the interior; ½Σ m ln m is smooth for m > 0). Its gradient along the slice is ½ ln m0 + ½·1 − ln μ0 − c·1, and multiples of 1 are irrelevant on the slice.
- **Supergradient bound.** By Lemma A (A2), for every m̂ ∈ conv(S), boundary points included: ψ(m̂) + ⟨z, m̂⟩ ≤ ψ0 + ⟨z, m0⟩ + ⟨g, m̂ − m0⟩, since the slice gradient of ψ at m0 is g − z modulo span(1) and Σ(m̂ − m0) = 0.
- **Maximum over conv(S).** The last term is linear in m̂, so its maximum over conv(S) is attained at one of the 36 spectra. ∎

### Lemma F (value at n*)
F(n*) = e^{L*}.

*Proof.*
- **Lower bound.** b^{ij}_s = w_s/8100 is in the fibre of n*: Σ_s w_s = 900 and all m^{ij}_{r,t} = 5/36. Then f(b) = 9·(1/9) ln 8100 + ½·36·(5/36) ln(5/36) = ln 8100 + (5/2) ln(5/36) = ln(5^{5/2}·8100/7776) = L*.
- **Upper bound.** Lemma B with y = 0 gives ln F(n*) ≤ Ψ*(0) − 3 ln 3. At z = 0, the stationarity condition holds at m̂* = (5/4)1 with μ0 = 1, and the maximiser is unique by strict concavity. So Ψ*(0) = ψ(m̂*) = (5/2) ln(5/4) + ln 900, and Ψ*(0) − 3 ln 3 = ln(900·5^{5/2}/(32·27)) = L*. ∎

### Lemma G (cover)
Δ = ⋃_{u} Σ_u over the 9 classes u = (i, j), where Σ_u = conv(n*, P_σ/3 : σ ∈ S_3, σ(i) ≠ j) is a 4-simplex.

*Proof.*
- **Shape of Δ.** Δ = (1/3)B_3 is a 4-dimensional polytope. Its six vertices are the matrices P_σ/3, and its inequalities are the nine n^u ≥ 0.
- **Facets.** For each u, exactly 4 permutations avoid the cell u. They are affinely independent: their images span the 3-dimensional face {n^u = 0}. So each of the 9 inequalities defines a facet that is a tetrahedron.
- **The centre.** n* has every n^u = 1/9 > 0. So it is interior and lies outside every facet's affine hull, which makes each Σ_u a nondegenerate 4-simplex.
- **Cone decomposition.** For a polytope with an interior point c, the cones conv(c ∪ F) over its facets F cover it. (Radial projection: the ray from c through any point x exits through some facet.) ∎

### Lemma D (outer cells; computer)
Each cone Σ_u is partitioned by an edge-bisection tree replayed in exact rational arithmetic. Bisecting a simplex at an edge midpoint yields two simplices whose union is the parent.

Leaves are of two kinds:
- **'C' leaves** have all 5 vertices in B0 := {|n_k − 1/9| ≤ 1/10000, k = 1..4}. B0 is convex, so the whole cell lies in B0.
- **'D' leaves** carry y ∈ Q^18 and μ0^u ∈ Q_{>0}^4. For them U(n) := Σ_u [n^u a(z^u; μ0^u) + (3/2) n^u ln n^u] is shown to be < L* at all 5 vertices, in outward-rounded ball arithmetic.

U is convex in n, since t ↦ t·a + (3/2) t ln t is convex for t ≥ 0 and each n^u is affine. Hence U < L* on the whole cell. Lemmas B and C then give ln F < L* on every 'D' cell.

Data (checker A, `outer/code/cert_cells.py --require-r0 1/10000`, arb at 200 bits):
- all 9 cones PASS;
- 291,552 'D' leaves and 4,616 'C' leaves;
- minimum margin ≥ 1.7271e-11 (`outer/evidence/cone*.check.json`, `outer/README.md`).

### Lemma E (central box; computer)
ln F(n) < L* for every n with 0 < max_k |n_k − 1/9| ≤ r0 = 1/10000.

*Setup* (all exact rationals; `code/cert_ldc3.py 1/10000 3/20 12 4`):
- **Coordinates.** η = n − n* ∈ B0 = [−r0, r0]^4 and n^u = 1/9 + A_u·η, where A has rows (1,0,0,0), (0,1,0,0), (−1,−1,0,0), (0,0,1,0), (0,0,0,1), (0,0,−1,−1), (−1,0,−1,0), (0,−1,0,−1), (1,1,1,1). So n^u ≥ 1/9 − 4r0 > 0 on B0, and no class is empty.
- **Basis.** B3 = [[1,0,0], [−1,1,0], [0,−1,1], [0,0,−1]] is a basis of 1⊥.
- **Inner Hessian at 0.** p_s = w_s/900 has mean (5/4)1 and covariance V0, so R(0) = −V0 B3 [B3^T((2/5)V0 − I)B3]^{-1} B3^T. Its first row is (46065/33592, −1145/1768, −1145/1768, −2555/33592).
- **Response matrix.** G = Σ_u C_u^T R(0) C_u and Y = −(45/4) G^{-1} Σ_u C_u^T 1 A_u. Every entry of Y lies in {0, ±75582/17915}. Put K_u = C_u Y, ℓ_u = (5/4) K_u^T 1 and P = I − J/4.
- **Majorant data.** With ε = 3/20: R̄ = R(0) + εP and Q_u = K_u^T R̄ K_u. X0 = −(1/9) B3^T Hess ψ(5/36·1) B3 and Xmin = (X0^{-1} + ε(B3^TB3)^{-1})^{-1}.
- **Asserted identities.** The script asserts exactly that B3 X0^{-1} B3^T = R(0) and B3 (B3^TB3)^{-1} B3^T = P. Hence B3 Xmin^{-1} B3^T = R̄.

*Steps.*
1. **(W) weak duality.** Lemma B with y = Yη gives ln F(n) ≤ U(η) := Σ_u [n^u Ψ*(K_u η) + (3/2) n^u ln n^u]. Any Y is allowed.
2. **(Q) regularity and the Hessian bound.**
   - **Dependence on c.** Ψ* and its maximiser depend on z only through c = B3^T z. Indeed Ψ*(z + t1) = Ψ*(z) + 5t, and the maximiser is unchanged.
   - **The c-box.** γ_c := max_u Σ_k |(B3^T K_u)_{c,k}| r0 (here γ = (113373/44787500, 113373/89575000, 113373/44787500)). The box C_box = ∏[−γ_c, γ_c] contains c(K_u η) for every u and every η ∈ B0. It is convex and symmetric.
   - **Krawczyk enclosure.** C_box is split into 12^3 sub-boxes. On each sub-box Z the script certifies, by the parametric Krawczyk test, that for every c ∈ Z the stationarity system G(μ; c) := B3^T(½ ln m(μ) − ln μ) + c = 0 (μ4 := 1) has a unique solution μ(c) in an explicit box of positive μ.
     - Test: K(X) = μ̃ − Ỹ G(μ̃; Z) + (I − Ỹ G′(X))(X − μ̃) ⊂ int X.
     - The Jacobian enclosure G′(X) is built from corner evaluations of the nonnegative-coefficient polynomials m(μ) and ∂m/∂μ, which are monotone on positive boxes, together with 1/μ.
   - **Interior maximiser, global and unique.** μ(c) gives the interior point m0 = 5m(μ)/Σm(μ), where the slice gradient of f := ψ + ⟨z,·⟩ vanishes. By (A2), f(m̂) ≤ f(m0) for every m̂ ∈ conv(S), so m0 is a global maximiser.
     - Suppose some m̂ ≠ m0 also attained the maximum, and put φ(t) = f(m0 + t(m̂ − m0)).
     - φ is concave on [0,1) by (A1), and liminf_{t→1} φ(t) ≥ φ(1) (as in the proof of (A2)).
     - So for 0 < t < 1, φ(t) ≥ (1−t)φ(0) + t·liminf_{s→1} φ(s) ≥ max, i.e. φ is constant on (0,1). This contradicts strict concavity on the open slice. Hence the maximiser is unique.
   - **Smoothness.** At every such z the unique maximiser is the interior nondegenerate stationary point (Hess ψ ≺ 0 on 1⊥ by (A1)). The implicit function theorem makes the stationary-point map m̂(·) C^∞ on the region certified by Krawczyk, and Ψ*(z) = f_z(m̂(z)) there. So Ψ* is C^∞ there with ∇Ψ*(z) = m̂(z) (envelope) and ∇²Ψ*(z) = R(z) = B3 X(z)^{-1} B3^T, where X = −B3^T Hess ψ(m̂) B3 ≻ 0.
   - **Bound on X.** Each sub-box then certifies X(μ) − Xmin ≻ 0 for every μ in the Krawczyk box. The steps are:
     - **Mean-value form.** X(μ) − X(μ_c) ∈ Σ_{j≤3} [∂_jX(box)]·[μ_j − μ_{c,j}] for a rational centre μ_c. The derivative is ∂_jX = −(∂_jΣm/5) B3^T H B3 − (Σm/5) B3^T ∂_jH B3, with ∂_jH = −½ diag(∂_j m_k/m_k²) + S2^{-1}(∂_j S2)S2^{-1}. Here H(m̂) = H(m)·Σm/5 by homogeneity.
     - **Loewner bound.** Every ratio d_s(μ)/d_s(μ_c) lies in [1−ε_L, 1+ε_L]. Hence (1−ε_L)S2(μ_c) ⪯ S2(μ) ⪯ (1+ε_L)S2(μ_c), and every entry satisfies |S2^{-1}(μ) − S2^{-1}(μ_c)| ≤ ε_L/(1−ε_L)·‖S2(μ_c)^{-1}‖_F.
     - **Positivity test.** A congruence by a rational nonsingular P is applied before the interval terms. Gershgorin lower bounds are then shown to be positive. The minimum over the 1728 sub-boxes is ≥ 0.02922.
   - **Conclusion of (Q).** X ⪰ Xmin, so R(z) ⪯ R̄ for every z with c(z) ∈ C_box.
3. **(T) Taylor step.** For each u and η ∈ B0, the segment {t·K_uη : t ∈ [0,1]} has c ∈ C_box. So Ψ*(K_uη) = Ψ*(0) + (5/4)1·K_uη + ∫_0^1 (1−t) η^T K_u^T R(tK_uη) K_u η dt ≤ Ψ*(0) + ℓ_u·η + ½ η^T Q_u η. Multiplying by n^u > 0 gives U(η) ≤ Ū(η) := Σ_u [n^u(Ψ*(0) + ℓ_u·η + ½η^TQ_uη) + (3/2) n^u ln n^u].
4. **(C) concavity of Ū.**
   - **Value at 0.** Ū(0) = Ψ*(0) − 3 ln 3 = L* (Lemma F).
   - **Gradient at 0.** ∇Ū(0) = (Σ_u A_u)(Ψ*(0) + (3/2)(ln(1/9) + 1)) + (1/9)Σ_u ℓ_u = 0. This holds exactly: Σ_u A_u = 0 and Σ_u ℓ_u = 0 are asserted.
   - **Hessian.** Hess Ū(η) = Haff(0) + Σ_c η_c D_c + Σ_u (3/2) A_u A_u^T / n^u(η). Here Haff(0) = Σ_u [A_u ℓ_u^T + ℓ_u A_u^T + Q_u/9] and D_c = Σ_u [A_u (Q_u e_c)^T + (Q_u e_c) A_u^T + A_{u,c} Q_u] are exact rationals.
   - **Negative definiteness.** The Hessian is negative definite on each of the 4^4 = 256 sub-boxes of B0 (congruence + Gershgorin; minimum margin ≥ 1.1651).
   - **Conclusion.** Ū is strictly concave on B0 with a critical point at 0. So Ū(η) < L* for η ≠ 0, and ln F(n) ≤ U(η) ≤ Ū(η) < L*. ∎

Result: PASS in 9.4 s (`evidence/cert_ldc3_r0_1e-4_eps0.15_NC12_M4.json`).

**Float sanity check (not part of the proof).** On 12 random η: ln F ≤ U ≤ Ū < L* (`code/sanity_ldc_chain.py`).

## 4. Conclusion
Take any n ∈ Δ \ {n*}.
- By Lemma G, n lies in some cone Σ_u.
- By Lemma D, n lies in a 'D' cell, where ln F(n) < L*, or in B0 \ {n*}, where Lemma E gives ln F(n) < L*.
- By Lemma F, L* = ln F(n*).

Hence Hypothesis 1.1 holds. Uniqueness and boundary points are included.

**n-form and m-form.** What is certified is the paper's n-form. The m-form, "L(m) < L(m*) on M∖{m*}", used as a working form in the frozen README §1.3, follows from it together with per-class uniqueness at n* (Lemma A (A1) or the paper's Lemma 5.5). The certificate does not need the m-form.

## 5. Trusted base and controls
- **Trusted.**
  - The written proofs of Lemmas A ((A1) polynomial chain, (A2) segment argument), B, C, F, G and of the analytic steps of E.
  - Two independent implementations per computer lemma:
    - Lemma A polynomials: python-flint, sympy (separate author), and the parent's plain-integer recomputation.
    - Lemma D: checker A (python-flint arb) and checker B (mpmath.iv, separate author with no access to `code/`).
    - Lemma E: checker A and checker B.
  - The interval semantics of python-flint 0.9.0 and mpmath 1.3.0.
- **Not trusted.**
  - The producers (`outer/code/bnb_produce.py`, `outer/code/fastdual.py`, `code/dual.py`).
  - All floating-point search and the multistart runs.
- **Controls.**
  - **Ordinary-colouring analogue.** All 30 multistarts reach a non-central global maximum with L − L* = +0.01374, reproducing the p. 4 remark.
  - **Checker-A mutations.** Every mutation was rejected: y×1.1, a far μ0, L* − 0.02 (which rejects 32,888 of 33,032 cone-(0,0) leaves, including those near the six secondary maxima of margin 0.0106), a dropped subtree, a relabelled leaf, and a changed r0 (caught by `--require-r0`).
  - **Checker B.** The ε = 0 negative control for the central box, plus its own mutations (see §6).
  - **Anchors.** All anchors match the paper exactly (`evidence/anchors_lemma58.json`).
- **Claim discipline.**
  - Correctness is pending hostile review.
  - Novelty is not established: the screen and parent searches found no 2009–2026 resolution, but a search miss is not novelty.
  - The reduction and the conditional theorem are due to Díaz et al. EulerSolve OPG-37656 (a different model) was read; nothing from it is used.

## 5a. Trust inherited from the paper (imported, NOT checked here)
The implication "H1.1 ⇒ χ(G_{n,5}) = 3 a.a.s." is the paper's. This lane checks only H1.1 itself, plus exact reproductions of the constants listed in §2. The following paper-level steps are imported as published (refereed, J. Graph Theory 61 (2009)); an independent bridge audit (parent's ColourBridgeAudit) found no gap but did not re-prove them:
- **Small subgraph conditioning.** Theorem 2.1, imported from [17, Cor. 4.2], with conditions (i)–(iv). For (ii), the joint moments (3.2) are computed for single cycles and sketched for overlapping cycles (pp. 11–12; L:588–611).
- **Asymptotics of E(Y²).** Lemma 5.1 (Stirling uniformity, q = O(n^162)), Lemma 5.9 (Euler–Maclaurin summation over the lattice J̃ and Laplace's method via Wong, Thm IX.5.3), Lemma 5.10, Theorem 5.1. The exact constants were reproduced here, not the analysis.
- **Section 6 (n ≡ 2, 4 mod 6).** Theorem 6.1, (6.1)–(6.4) and the vertex-deletion argument are sketched in the paper (pp. 26–28). The bridge audit notes that (6.3) also uses the Lemma 5.9 lower bound, which again depends only on H1.1.
- **Standard facts.** G_{n,5} is a.a.s. not bipartite (p. 2). Transfer from pairings to simple graphs. Minor wording issues noted by the audit: p. 6 "P(X2 = 0) bounded away from 0" should be read conditionally on X1 = 0; p. 4's claim that the boundary contains no local maximiser is not proved in the body and is not used; typos on p. 22 (L:1307).
- **Version.** The published JGT text is assumed to match this 2009-10-20 preprint; this was not compared.

## 6. Checker B results (independent author, mpmath.iv + fractions, 128 bits; no access to `code/` or `outer/code/`)
- Outer: `checkerB/evidence/cells_iv_all9_final.json`: 9/9 PASS, ALL_PASS true; identical D/C counts to checker A; min margin 1.72707e-11 (cone10); trusted r1 = 1/10000 pinned; max over S reduced to the 8 vertices of conv(S) (Lemma 5.2 vertex list, re-enumerated).
- Central: `checkerB/evidence/central_iv_r0_1e-4_eps3_20_NC8.json`: PASS ((Q) 512/512 c-boxes; (C) by vertex argument, lambda_max(Hess Ubar) <= -1.1762 exactly at all 16 vertices, valid because lambda_max is convex in eta). Negative control eps = 0: (Q) fails 64/64, FAIL as required (`central_iv_negctl_eps0_NC4.json`).
- Mutations (`checkerB/evidence/mutants_cone00.json`, `mutants_cone22.json`): see `checkerB/README.md`.
- Parent re-ran checker A on all 9 cones + central from hash-verified inputs: identical results (run dir `review/colour-parent-replay-v1/`). A third, Codex-authored checker C is being run by the parent.
