# CLAIM-r2: the Maximum Hypothesis of Díaz–Kaporis–Kemkes–Kirousis–Pérez–Wormald holds; with Theorem 1.1 of the pinned preprint, χ(G_{n,5}) = 3 a.a.s.

Revision r2 of `CLAIM.md` (sha256 8c1081f8…f972, kept unchanged). It applies the fixes requested by the hostile reviews (Claude: `review/colour-complete-claim-hostile-review.note.md`; Codex: `review/colour-codex-claim-review-v1/final.md`) and by the central-checker implementation reviews. Every finding is mapped to its change in `DISPOSITIONS-r2.md`. Pinned files: `MANIFEST-r2.sha256`. Review paths are relative to the run directory `institute/runs/six-lane-2026-10-16/`. Host-clock times are PDT, 2026-10-17.

**Status.** The result is computer-assisted. The written proofs are below.
- **Outer region:** three independently written checkers pass (A python-flint arb; B mpmath.iv; C Codex-authored arb, run by the parent).
- **Central box:** two independently written checkers pass (A, B), each also in a hardened r2 form.
- **Reviews:** both hostile reviews returned ACCEPT-WITH-FIXES with no critical, major or fatal finding; their fixes are applied here.
- **Priority:** the parent's priority audit found no earlier proof. A search miss does not establish novelty.

## 1. Exact statement

**Objects** (pinned preprint, §§4, 5.1, 7)
- **Spectra.** S is the set of 2×2 nonnegative integer matrices s = (s_{−1,−1}, s_{−1,1}; s_{1,−1}, s_{1,1}) with entry sum 5 and every row and column sum ≥ 1. |S| = 36, with weights w_s = 5!/∏_k s_k!. Entries are indexed by k ∈ O := {(−1,−1), (−1,1), (1,−1), (1,1)}, in that order.
- **Domain Δ (7.1).** Δ = {n = (n1,n2,n3,n4) ≥ 0 : n1+n2 ≤ 1/3, n3+n4 ≤ 1/3, n1+n3 ≤ 1/3, n2+n4 ≤ 1/3, n1+n2+n3+n4 ≥ 1/3}.
- **Overlap values (7.2).** n^{00} = n1, n^{01} = n2, n^{02} = 1/3−n1−n2, n^{10} = n3, n^{11} = n4, n^{12} = 1/3−n3−n4, n^{20} = 1/3−n1−n3, n^{21} = 1/3−n2−n4, n^{22} = n1+n2+n3+n4−1/3. Thus Δ = {all n^u ≥ 0} = (1/3)·(Birkhoff polytope B_3), with classes u = (i,j) ∈ Z3².
- **Ports and edges (L7).** A port is a pair (u, k). The map ι(u, k) := (u + k, −k) is an involution on the 36 ports, with addition in Z3² and −k = (−r, −t). It has no fixed point, because k ≠ −k. Its 18 orbits are the edges e = {(u,k), (u+k,−k)}, and the quotient graph is K3×K3. Constraint (7.5), m^{u}_k = m^{u+k}_{−k}, says exactly that m is constant on each edge.
- **Fibre of n.** The arrays d = (d^u_s) ≥ 0 with Σ_s d^u_s = n^u (7.4), m^u := Σ_s d^u_s s (7.3), and (7.5).
- **Objective (7.6).** F̂(d) = ∏_{u,s} (w_s/d^u_s)^{d^u_s} · ∏_{u,k} (m^u_k)^{m^u_k/2}, with 0^0 = 1. Write f := ln F̂ and F(n) := max of F̂ over the fibre of n; this is well defined by Lemma 0.
- **Constants.** L* := (5/2) ln 5 + ln(25/24), and n* := (1/9, 1/9, 1/9, 1/9).
- **The paper's polytope 𝒟 (§4).** All d ≥ 0 with (7.5), Σ_{j,s} d^{ij}_s = 1/3 for every i, and Σ_{i,s} d^{ij}_s = 1/3 for every j. Put b := (b^u_s) = (w_s/8100).

**Theorem (certified, computer-assisted).** For every n ∈ Δ with n ≠ n*: F(n) < F(n*) = 5^{5/2}·25/24 = e^{L*}. The domain Δ is closed.

This is Hypothesis 1.1 of the pinned preprint exactly as stated there.

**Lemma F′.** b is the unique maximiser of f on 𝒟. This is the conclusion of the paper's Lemma 5.6.

**Corollary (scope, M2).** χ(G_{n,5}) = 3 a.a.s. for uniformly random simple 5-regular graphs (n even). It follows from three ingredients:
- Theorem 1.1 of the pinned preprint (sha256 5e317a44…28b1), whose proof uses H1.1 only as listed in §2;
- Lemma F′, which replaces the paper's appeal to Lemma 5.5 for the uniqueness of b;
- the paper-level steps imported in §6a.

The preprint was published as J. Graph Theory 61 (2009) 157–191. The published text was not compared, because the publisher returned HTTP 403 to the parent. The corollary is therefore stated relative to the pinned preprint.

## 2. Primary source

- **File.** `sources/diaz2009-3col-preprint.pdf`, the Wayback 2021-03-15 snapshot of users.monash.edu.au/~nwormald/papers/3col.pdf: 33 pages, sha256 5e317a44a75bd88fa454824ced64501b4d9eeb8c6fcd7adedeb29eb2219428b1.
- **Date provenance.** The date comes from the PDF metadata: CreationDate = ModDate = 2009-10-20 13:17:41 PDT, Creator "TeX", Producer "pdfTeX-1.40.9" (pdfinfo 26.04.0, run 2026-10-16).
- **Extracted text.** `sources/diaz2009-3col-preprint.layout.txt`, sha256 da12c0eecb7773b6b148861512e1cbb1507d72e074ca6e409d18502e0c7639ea. The prefix "da12c0eb" in README §1.1 is a typo, corrected in the README addendum of 01:36:35.

PDF page numbers equal the printed numbers. Prose is quoted verbatim; formulas are transcribed.

**Statements**
- **p. 4.** "Hypothesis 1.1 (Maximum Hypothesis) The four-variable function F (n) has a unique global maximum over its domain at the point (1/9, 1/9, 1/9, 1/9)."
- **p. 4.** "Theorem 1.1 Under the Maximum Hypothesis, the chromatic number of Gn,5 is a.a.s. 3."
- **p. 4** (positive control). "for the case of the ordinary (not balanced locally rainbow) colourings there exists an analogue to function F which also has a local maximum at the point (1/9, 1/9, 1/9, 1/9) but unfortunately this is not the global maximum."
- **pp. 28–29, definitions (7.1)–(7.6).** "We first define the domain of F . This is the set of all nonnegative real vectors n = (n1 , . . . , n4 ) satisfying" (7.1); "A spectrum s is a 2 × 2 nonnegative integer matrix such that each row and column sum is at least 1, and the sum of all four entries is 5"; "(We follow the convention that 0^0 equals 1.) … Then, we set F (n) to be the value of this maximum."
- **p. 17, Lemma 5.3.** Quoted in CLAIM.md §2. The certificate does not use Lemma 5.3, because Lemma B bounds F̂ directly.

**Every use of H1.1 in the conditional proof**
- **Overview and (2.5).** p. 4: "determine its asymptotic value, under the Maximum Hypothesis, in Section 5". p. 6, (2.5): "and, under the Maximum Hypothesis".
- **Section 5 framing.** p. 14: "showing that equation (2.5) holds, assuming the Maximum Hypothesis". p. 15: "we determine the value of M under the Maximum Hypothesis".
- **Lemma 5.6** (p. 22). "Under the Maximum Hypothesis, the function f has a unique maximizer in D at b. Moreover, M := max_{d∈D} 5^{−5/2} e^{f(d)} = 25/24."
- **Lemma 5.8, bullets 1–2, and Lemma 5.9** (p. 24). "Under the Maximum Hypothesis".
- **Lemma 5.10 and Theorem 5.1** (p. 25). "Under the Maximum Hypothesis" / "Under the maximum hypothesis".
- **Section 6.** p. 26, Theorem 6.1: "Under the Maximum Hypothesis, G a.a.s. has a 3-colouring …". p. 27, proof of (6.3): "from Lemmata 5.1 and 5.6, that under the maximum hypothesis …".
- **n ≡ 2, 4 (mod 6)** (p. 28). "by Theorem 6.1, G0 a.a.s. has a 3-colouring". There is no separate hypothesis for this case.

**Other numerical or omitted steps, and their coverage**
- **p. 9: "We omit the calculations."** The constants (2.4)/(2.5) are reproduced exactly in `evidence/anchors_lemma58.json`. The condition-(iv) identity itself is also checked there: the key "ratio_equals_exp(sum_lambda_k_delta_k^2)_(condition_(iv)_with_equality)" reads MATCH.
- **p. 21, Lemma 5.5 (corrected, M1).** The conditional proof needs more than the value F(n*). Lemma 5.6 asserts that b is the *unique* maximiser of f on 𝒟, and Lemmas 5.8–5.10 use this. The paper derives it from Lemma 5.5 together with the sentence "This solution must correspond to the unique stationary point of G̃ in the interior of M0(1/9), which must then be a maximum". That sentence does not exclude maximisers on the boundary. Lemma F′ below proves the uniqueness of b from Lemmas A and B and the Theorem, so neither Lemma 5.5 nor that sentence is used.
- **p. 23, Lemma 5.7** ("whose proof we omit"). The rank (23) and the integer parametrisation are reproduced exactly (anchors).
- **p. 24, Lemma 5.8, bullets 3–4.** Reproduced exactly (anchors): det H̃ = −2^175 3^1078 5^310 7^12 11^14·13·17·79^4; −H̃ positive definite; g̃(b̃) = 2^90 3^558 5^171.
- **p. 30, the Maple Hessian, and p. 31, numerical concavity and the grid search.** Replaced by Lemma A and Lemmas D and E.

## 3. Notation (de-collided, L2)
- **Basic objects.** Λ(m) := diag(m); 1 := (1,1,1,1); J := 11ᵀ; Π := I − J/4; B3 := [[1,0,0],[−1,1,0],[0,−1,1],[0,0,−1]], a basis of 1⊥ with B3 (B3ᵀB3)^{−1} B3ᵀ = Π.
- **Cone and slice.** Cone(S) := {Σ_s λ_s s : λ ≥ 0}, which is full-dimensional because S spans ℝ⁴. Since every spectrum has entry sum 5, conv(S) = Cone(S) ∩ {Σm = 5} (the paper's M0(1)), and relint conv(S) = int Cone(S) ∩ {Σm = 5}.
- **Entropy and ψ.** H(m) := max{Σ_s d_s ln(w_s/d_s) : d ≥ 0, Σ_s d_s s = m} for m ∈ Cone(S). This is the maximum of a continuous function over a compact polytope, so it is attained. ψ(m) := H(m) + ½Σ_k m_k ln m_k, with 0 ln 0 = 0.
- **Hessian.** 𝓗(m) := Hess ψ(m) on int Cone(S). This is a different object from the entropy H.
- **Dual function (L5).** Ψ*(z) := **sup**_{m̂∈conv(S)} [ψ(m̂) + ⟨z, m̂⟩]. This is a supremum; attainment is proved only where (A3) applies.
- **Exponential family.** For μ ∈ (0,∞)⁴ and θ = ln μ: d_s(μ) = w_s μ^s, Φ(μ) = Σ_s d_s(μ), m(μ) = Σ_s d_s s, S2(μ) = Σ_s d_s s sᵀ.
- **Multipliers.** For y ∈ ℝ^18, set z^u := C_u y, where (C_u)_{k,e} = +1 if (u,k) is the first-listed port of e and −1 if it is the second.
- **Leaves.** Leaves of the outer trees are called dual leaves or central leaves.

## 4. Written lemmas

### Lemma 0 (F is well defined; L1)
For every n ∈ Δ the fibre of n is nonempty and compact, and F̂ is continuous on it. Hence F(n) is attained.

*Proof.*
1. **Convexity.** Q := {(n, d) : d ≥ 0, Σ_s d^u_s = n^u(n), (7.5)} is a polyhedron, because each n^u(n) is affine. Its projection N := {n : the fibre of n is nonempty} is therefore convex.
2. **Vertices of Δ.** By Birkhoff–von Neumann, Δ = conv{P_σ/3}, where the P_σ are the six permutation matrices. At P_σ/3 the occupied classes are u_i = (i, σ(i)), each with n^{u_i} = 1/3.
   - A port (u_i, k) with k = (r, t) points to (i+r, σ(i)+t). That class is occupied iff σ(i+r) = σ(i) + t.
   - Every permutation of Z3 is affine, σ(i) = ±i + c. For translations the live ports are k ∈ {(−1,−1), (1,1)}; for reflections they are k ∈ {(−1,1), (1,−1)}.
   - Put d^{u_i} := (1/6)(δ_{(1,0,0,4)} + δ_{(4,0,0,1)}) in the first case and (1/6)(δ_{(0,1,4,0)} + δ_{(0,4,1,0)}) in the second, and d^v := 0 for unoccupied v. All four spectra lie in S. This gives m^{u_i} = 5/6 on the two live ports and 0 elsewhere.
   - (7.5) holds: a live port of an occupied class is paired by ι with a live port of an occupied class (both carry 5/6); a dead port of an occupied class is paired with a port of an unoccupied class (both carry 0).
   - So every vertex lies in N, and Δ ⊂ N.
3. **Compactness and continuity.** The fibre is closed, with 0 ≤ d^u_s ≤ 1/3. The map x ↦ x ln x is continuous on [0, ∞), so f is continuous on the fibre and F̂ = e^f attains its maximum. ∎

(The Codex reviewer independently constructed feasible fibres at all six vertices.)

### Lemma A (slice concavity and its boundary extensions)
- **(A1)** ψ is C^∞ on int Cone(S), with 𝓗(m) = ½Λ(m)^{−1} − S2(μ(m))^{−1}, and it is strictly concave on every open slice {Σm = c} ∩ int Cone(S). Moreover 𝓗(cm) = c^{−1}𝓗(m) for c > 0.
- **(A2)** Tangent bound: for m0 ∈ relint conv(S) and m̂ ∈ conv(S), ψ(m̂) ≤ ψ(m0) + ⟨∇ψ(m0), m̂ − m0⟩.
- **(A3)** Uniqueness: let z ∈ ℝ⁴. If m0 ∈ relint conv(S) satisfies ∇ψ(m0) + z ∈ span(1), then m0 is the unique maximiser of ψ + ⟨z,·⟩ on conv(S), and Ψ*(z) = ψ(m0) + ⟨z, m0⟩.

*Proof.*
- **Bijectivity (L6).** Let m ∈ int Cone(S). Then m − εΣ_s s ∈ Cone(S) for small ε > 0, so m = Σ_s λ_s s with all λ_s > 0.
  - Define A_m(θ) := Φ(e^θ) − ⟨m, θ⟩. Its Hessian S2(e^θ) is positive definite because S spans ℝ⁴, so A_m is strictly convex.
  - A_m tends to +∞ along every ray. Take v ≠ 0. If max_s ⟨v, s⟩ > 0, the exponential term dominates. Otherwise every ⟨v, s⟩ ≤ 0 and not all are 0, so ⟨m, v⟩ = Σ_s λ_s ⟨s, v⟩ < 0 and A_m(tv) ≥ −t⟨m, v⟩ → ∞.
  - A closed proper convex function that tends to +∞ along every ray has bounded level sets (Rockafellar, *Convex Analysis*, Thm 27.1). So A_m has a minimiser, unique by strict convexity, and at it m(e^θ) = m.
  - Conversely m(e^θ) ∈ int Cone(S) for every θ. Hence θ ↦ m(e^θ) is a bijection ℝ⁴ → int Cone(S), and a diffeomorphism because its Jacobian is S2 ≻ 0.
- **Normalised mean map (L3, Codex 1).** Every spectrum has entry sum 5, so m(e^{θ+t1}) = e^{5t} m(e^θ). The normalised mean θ ↦ m(e^θ)/Φ(e^θ) ∈ relint conv(S) is therefore invariant under θ ↦ θ + t1. It is a diffeomorphism from ℝ⁴/span(1) onto relint conv(S), not from ℝ⁴.
- **Gibbs.** Let m = m(μ) and let d′ ≥ 0 satisfy Σ d′ s = m. Then Σ d′ = Σm/5 = Σ d(μ), and Σ_s d′_s ln(w_s/d′_s) = −⟨ln μ, m⟩ − KL(d′‖d(μ)), where KL(d′‖d) = Σ d′ ln(d′/d) ≥ 0 with equality iff d′ = d(μ). Hence H(m) = −⟨ln μ(m), m⟩, with the unique maximiser d(μ).
- **Hessian.** Write θ(m) = ln μ(m). Then ∂θ/∂m = S2^{−1}. Since S2·1 = 5m, S2^{−1}m = (1/5)1. Hence ∇H = −θ − (1/5)1, ∇²H = −S2^{−1}, and 𝓗 = ½Λ^{−1} − S2^{−1}.
- **Scaling.** H(cm) = cH(m) − (Σm/5) c ln c and ½Σ cm ln(cm) = c·½Σ m ln m + ½ c ln c Σm, so ψ(cm) = cψ(m) + (3/10)(Σm) c ln c. The last term is linear in m, so 𝓗(cm) = c^{−1}𝓗(m). On the slice Σm = 5 this reads ψ(cm̂) = cψ(m̂) + (3/2) c ln c.
- **Reformulation.** Put X̃ := Λ^{1/2} S2^{−1} Λ^{1/2} and q := Λ^{1/2}1. Then X̃q = q/5, so q⊥ is X̃-invariant. Hence 𝓗 ≺ 0 on 1⊥ iff uᵀS2u < 2uᵀΛu for every nonzero u ⊥ m.
- **Polynomial form.** Mpoly := 5Φ(2Λ − S2) + 3mmᵀ is homogeneous of degree 10 in μ and satisfies Mpoly·1 = 0. Writing u = u′ + c1 with u′ ⊥ m gives uᵀMpoly u = 5Φ(2u′ᵀΛu′ − u′ᵀS2u′). So the condition above holds iff the leading 3×3 block of Mpoly is positive definite.
- **Positivity (L9a, Codex 2).** The block's leading principal minors P1, P2, P3 have the following term counts and minimum coefficients, for each dropped index:

| dropped index | P1 terms | P2 terms | P3 terms | minimum coefficients (P1, P2, P3) |
|---|---|---|---|---|
| 0 | 154 | **943** | 2766 | 200, 10^5, 5·10^7 |
| 1, 2, 3 | 154 | 949 | 2766 | 200, 10^5, 5·10^7 |

  - Every coefficient is strictly positive, so the minors are positive on (0,∞)⁴. This gives (A1).
  - The raw coefficients are in the pinned `evidence/slice_minors_rainbow.json` (sha256 775a563d…b5c3).
  - The standalone script `code/slice_poly_dump_r2.py` (no lane imports, writes no files; Codex 3) reproduces that JSON byte-for-byte.
  - The coefficients were also rebuilt independently by the sympy worker, by the parent's plain-integer recomputation, and by the Codex reviewer's sparse-integer rebuild.
- **(A2), segment argument.**
  - H is concave on the closed polytope conv(S) directly from its definition. If d′ attains H(m′) and d″ attains H(m″), then td′ + (1−t)d″ is feasible for tm′ + (1−t)m″, and Σ d ln(w/d) is concave.
  - Put m_t = m0 + t(m̂ − m0). For 0 ≤ t < 1, m_t ∈ relint conv(S), so (A1) gives ψ(m_t) ≤ ψ(m0) + t⟨∇ψ(m0), m̂ − m0⟩.
  - Concavity of H gives liminf_{t→1} H(m_t) ≥ H(m̂), and ½Σ m ln m is continuous on the closed slice.
  - Letting t → 1 yields (A2).
- **(A3).** By (A2), for every m̂ ∈ conv(S): ψ(m̂) + ⟨z, m̂⟩ ≤ ψ(m0) + ⟨z, m0⟩ + ⟨∇ψ(m0) + z, m̂ − m0⟩. The last term is 0, because ∇ψ(m0) + z ∈ span(1) and Σ(m̂ − m0) = 0. So m0 is a maximiser and the sup is attained.
  - For uniqueness, suppose m̂ ≠ m0 is also a maximiser, and let φ(t) := (ψ + ⟨z,·⟩)(m0 + t(m̂ − m0)).
  - φ is concave on [0,1), and liminf_{s→1} φ(s) ≥ φ(1) by the previous bullet. For 0 < t < s < 1, φ(t) ≥ (1 − t/s)φ(0) + (t/s)φ(s). Letting s → 1 gives φ(t) ≥ max.
  - So φ is constant on [0,1). This contradicts strict concavity on the open segment, which lies in relint conv(S). ∎
- **Observation (not used; L9b).** Numerically, sup uᵀS2u/uᵀΛu over m⊥ appears to equal 2, approached only at the boundary. SliceConcavityIndep observed this, and the Codex reviewer checked one boundary-limit example. It is not proved, and nothing depends on it.

### Lemma B (weak pairing duality)
For every n ∈ Δ, every d in the fibre of n and every y ∈ ℝ^18:

f(d) ≤ Σ_u [ n^u Ψ*(C_u y) + (3/2) n^u ln n^u ],

and classes with n^u = 0 contribute 0.

*Proof.*
- **Pairing.** Σ_u ⟨z^u, m^u⟩ = Σ_e y_e (m at the first port of e − m at the second port of e) = 0 by (7.5). So f(d) = Σ_u T_u with T_u := Σ_s d^u_s ln(w_s/d^u_s) + ½Σ_k m^u_k ln m^u_k + ⟨z^u, m^u⟩.
- **Empty classes.** If n^u = 0, then d^u = 0, m^u = 0 and T_u = 0.
- **Non-empty classes.** Otherwise write d^u = n^u p with p a probability vector on S, set m̂ := Σ p_s s ∈ conv(S), and E(p) := Σ p ln(w/p). Then T_u = n^u[E(p) + ½Σ m̂ ln m̂ + ⟨z^u, m̂⟩] + (3/2) n^u ln n^u. The coefficient is −1 + 5/2 = 3/2.
- **Bound.** Since E(p) ≤ H(m̂), T_u ≤ n^u[ψ(m̂) + ⟨z^u, m̂⟩] + (3/2) n^u ln n^u ≤ n^u Ψ*(z^u) + (3/2) n^u ln n^u. ∎

### Lemma C (inner bound)
Let z ∈ ℝ⁴ and μ0 ∈ (0,∞)⁴. Put Φ0 = Φ(μ0), m0 = m(μ0)/Φ0, ψ0 = ½Σ m0 ln m0 + ln Φ0 − ⟨ln μ0, m0⟩ and g = ½ ln m0 − ln μ0 + z. Then

Ψ*(z) ≤ a(z; μ0) := ψ0 + ⟨z, m0⟩ + max_{s∈S} ⟨g, s − m0⟩ = ln Φ0 + max_{s∈S} ⟨g, s⟩.

*Proof.*
- **m0 is interior.** m0 is the mean of the strictly positive distribution w_s μ0^s/Φ0 on S, so m0 ∈ relint conv(S).
- **Value and gradient.** By Gibbs, ψ(m0) = ψ0. By (A1), ∇ψ(m0) ≡ ½ ln m0 − ln μ0 modulo span(1).
- **Bound.** (A2) gives ψ(m̂) + ⟨z, m̂⟩ ≤ ψ0 + ⟨z, m0⟩ + ⟨g, m̂ − m0⟩ for every m̂ ∈ conv(S), boundary points included. A linear form attains its maximum over conv(S) at a spectrum. The final identity is algebra, using ⟨g, m0⟩ = ½Σ m0 ln m0 − ⟨ln μ0, m0⟩ + ⟨z, m0⟩. ∎

### Lemma F (value at n*)
F(n*) = e^{L*}.

*Proof.*
- **Lower bound.** b lies in the fibre of n*, since Σ_s w_s = 900 and every m^u_k = 5/36. Then f(b) = ln 8100 + (5/2) ln(5/36) = L*.
- **Upper bound.** Lemma B with y = 0 gives ln F(n*) ≤ Ψ*(0) − 3 ln 3.
  - The point m̂* := (5/4)1 = m(1)/Φ(1) lies in relint conv(S), because Σ_s w_s s_k = 1125 for each k and Φ(1) = 900.
  - ∇ψ(m̂*) = ½ ln m̂* − θ(m̂*) + const·1 ∈ span(1), since θ(m̂*) = −(1/5) ln 900 ·1.
  - So (A3) with z = 0 gives Ψ*(0) = ψ(m̂*) = ln 900 + (5/2) ln(5/4).
  - Hence Ψ*(0) − 3 ln 3 = (9/2) ln 5 − 3 ln 2 − ln 3 = L*. ∎

### Lemma F′ (b is the unique maximiser of f on 𝒟; M1)
For every d ∈ 𝒟, f(d) ≤ L*, with equality iff d = b. In particular max_𝒟 5^{−5/2} e^f = 25/24, which is the conclusion of the paper's Lemma 5.6.

*Proof.*
1. **Off the centre.** Every d ∈ 𝒟 lies in the fibre of n(d) := (Σ_s d^{00}_s, Σ_s d^{01}_s, Σ_s d^{10}_s, Σ_s d^{11}_s) ∈ Δ; the row and column sums 1/3 give (7.2). If n(d) ≠ n*, then f(d) ≤ ln F(n(d)) < L* by the Theorem.
2. **At the centre.** If n(d) = n*, then every n^u = 1/9. Write d^u = p^u/9 and m̂^u = Σ_s p^u_s s.
   - The identity in the proof of Lemma B (y = 0) gives f(d) = Σ_u (1/9)[E(p^u) + ½Σ m̂^u ln m̂^u] − 3 ln 3 ≤ Σ_u (1/9)ψ(m̂^u) − 3 ln 3 ≤ Ψ*(0) − 3 ln 3 = L*.
   - Equality forces ψ(m̂^u) = Ψ*(0), hence m̂^u = (5/4)1 by the uniqueness in (A3).
   - It also forces E(p^u) = H((5/4)1) = ln 900. Every probability vector p on S satisfies E(p) = ln 900 − KL(p‖w/900), so p^u = w/900, i.e. d^u = b^u.
3. **Attainment.** b ∈ 𝒟 and f(b) = L*. ∎

### Lemma G (cover)
Δ = ⋃_u Σ_u, where Σ_u = conv(n*, P_σ/3 : σ(i) ≠ j) for u = (i, j), and each Σ_u is a nondegenerate 4-simplex.

*Proof.*
- Δ is a 4-polytope with vertices P_σ/3 and facets {n^u = 0}.
- Exactly four permutations avoid the cell u, and their images span the 3-dimensional facet, so each facet is a tetrahedron.
- n* is interior, because every n^u = 1/9 > 0.
- The cones from an interior point over the facets cover the polytope (radial projection). ∎

### Lemma D (outer cells; computer)
Each Σ_u is partitioned by an edge-bisection tree with exact rational midpoints.
- **Central leaves** have all 5 vertices in B0 := {max_k |n_k − 1/9| ≤ 1/10000}. B0 is convex, so the whole cell lies in B0.
- **Dual leaves** carry y ∈ ℚ^18 and μ0^u ∈ ℚ_{>0}⁴, given as binary64 values and read exactly. For them U(n) := Σ_u [n^u a(C_u y; μ0^u) + (3/2) n^u ln n^u] is shown to be < L* at the 5 vertices. U is convex in n, because t ↦ ta + (3/2) t ln t is convex on [0,∞) and each n^u is affine. So U < L* on the whole cell, and Lemmas B and C give ln F < L* there.

**Results.**
- **Checker A** (`outer/code/cert_cells.py --require-r0 1/10000`, arb at 200 bits): 9/9 cones PASS; 291,552 dual leaves and 4,616 central leaves.
- **Minimum margin** ≥ **1.7270e−11**. This is rounded down from the arb enclosure 1.7270736843852880…e−11 at cone (1,0), preorder node 61243.
- **n^u = 0 handling, checker A.** Vertex coordinates are exact fmpq. `outer/code/cert_cells.py` lines 122–125 raise an error on n^u < 0 and skip n^u = 0 with `continue`. So 0·log 0 is never evaluated in ball arithmetic.
- **n^u = 0 handling, checker B.** `checkerB/code/cells_iv.py` uses exact Fractions. It rejects negative n^u at lines 226–227, restricts to classes with some n^u > 0 (`active`) at line 228, and adds a term only `if n > 0` at lines 240–242. `nlogn15` (lines 176–184) is called only with n > 0.

### Lemma E (central box; computer)
For every n with 0 < max_k |n_k − 1/9| ≤ r0 = 1/10000: ln F(n) < L*.

**Setup.** All quantities below are exact rationals.
- **Coordinates.** Let η := n − n* ∈ B0 = [−r0, r0]⁴. Then n^u = 1/9 + A_u·η, where A has the rows (1,0,0,0), (0,1,0,0), (−1,−1,0,0), (0,0,1,0), (0,0,0,1), (0,0,−1,−1), (−1,0,−1,0), (0,−1,0,−1), (1,1,1,1). Hence n^u ≥ 1/9 − 4r0 > 0 on B0.
- **Inner Hessian at 0.** p_s = w_s/900 has mean (5/4)1 and covariance V0. Put R(0) := −V0 B3 [B3ᵀ((2/5)V0 − I)B3]^{−1} B3ᵀ. Its first row is (46065/33592, −1145/1768, −1145/1768, −2555/33592).
- **Response.** N := Σ_u C_uᵀ R(0) C_u is nonsingular. Set Y := −(45/4) N^{−1} Σ_u C_uᵀ 1 A_u, with entries in {0, ±75582/17915}. Put K_u := C_u Y and ℓ_u := (5/4) K_uᵀ1.
- **Majorant data.** With ε := 3/20: R̄ := R(0) + εΠ and Q_u := K_uᵀ R̄ K_u. X0 := −(1/9)B3ᵀ𝓗((5/36)1)B3 (scaling law of (A1)), and Xmin := (X0^{−1} + ε(B3ᵀB3)^{−1})^{−1}.
- **Exact identities.** The code checks R(0) = B3 X0^{−1} B3ᵀ and B3(B3ᵀB3)^{−1}B3ᵀ = Π, hence R̄ = B3 Xmin^{−1} B3ᵀ. It also checks Σ_u A_u = 0 and Σ_u ℓ_u = 0.

**Steps**
1. **(W) Weak duality.** Lemma B with y = Yη gives ln F(n) ≤ U(η) := Σ_u [n^u Ψ*(K_uη) + (3/2) n^u ln n^u]. This holds for any Y.
2. **(Q) Curvature bound.**
   - **c-dependence (L3, Codex 1).** Ψ*(z + t1) = Ψ*(z) + 5t, so the value Ψ* does **not** depend on c := B3ᵀz alone. The maximiser m̂(z), the matrix X(z) and R(z) := ∇²Ψ*(z) do depend only on c, since ker B3ᵀ = span(1). The Taylor step below keeps the affine term.
   - **c-box.** Let γ_c := max_u Σ_k |(B3ᵀK_u)_{c,k}| r0, so γ = (113373/44787500, 113373/89575000, 113373/44787500). The box C_box := ∏[−γ_c, γ_c] is convex, symmetric, and contains every c(K_uη) for η ∈ B0.
   - **Krawczyk.** C_box is split into 12³ sub-boxes Z. On each, the parametric Krawczyk test Kr(B_μ) := μ̃ − Ỹ Γ(μ̃; Z) + (I − Ỹ Γ′(B_μ))(B_μ − μ̃) ⊂ int B_μ is certified. Here Γ(μ; c) := B3ᵀ(½ ln m(μ) − ln μ) + c, with μ4 := 1, and Γ′ is enclosed by corner evaluations of nonnegative-coefficient polynomials together with 1/μ. The test gives, for every c ∈ Z, a unique zero μ(c) ∈ B_μ.
   - **Identifying the maximiser.** A zero of Γ means m0 := 5m(μ)/Σm(μ) ∈ relint conv(S) satisfies ∇ψ(m0) + z ∈ span(1). By (A3), m0 is the unique maximiser and Ψ*(z) = ψ(m0) + ⟨z, m0⟩.
   - **Smoothness.** By (A1) the stationary point is nondegenerate. The implicit function theorem then gives smooth m̂(z), with ∇Ψ*(z) = m̂(z) (envelope theorem) and ∇²Ψ*(z) = R(z) = B3 X(z)^{−1} B3ᵀ, where X(z) := −B3ᵀ𝓗(m̂(z))B3 ≻ 0.
   - **X ⪰ Xmin on every B_μ.**
     - (i) Mean value. X(μ) = −(Σm(μ)/5) B3ᵀ𝓗(m(μ))B3 by scaling. Then X(μ) − X(μ_c) ∈ Σ_{j≤3} [∂_jX(B_μ)]·[μ_j − μ_{c,j}], where ∂_jX = −(∂_jΣm/5) B3ᵀ𝓗B3 − (Σm/5) B3ᵀ(∂_j𝓗)B3 and ∂_j𝓗 = −½ diag(∂_j m_k / m_k²) + S2^{−1}(∂_jS2)S2^{−1}.
     - (ii) **Side condition (L8): μ_c ∈ B_μ.** This keeps every mean-value segment inside the enclosure domain. It is enforced by `require()` at `code/cert_ldc3_r2.py` line 272; it was an `assert` at line 257 of the pinned `code/cert_ldc3.py`.
     - (iii) Loewner bound. Every ratio d_s(μ)/d_s(μ_c) lies in [1−ε_L, 1+ε_L]. Hence (1−ε_L)S2(μ_c) ⪯ S2(μ) ⪯ (1+ε_L)S2(μ_c), and |S2^{−1}(μ) − S2^{−1}(μ_c)|_entry ≤ ε_L/(1−ε_L)·‖S2(μ_c)^{−1}‖_F.
     - (iv) **Side condition (L8): ε_L < 1.** It is enforced as ε_L < 1/2 by `require()` at `code/cert_ldc3_r2.py` line 293 (formerly an `assert` at line 278).
     - (v) Positivity. A rational nonsingular congruence T is applied before the interval terms (nonsingularity enforced at lines 214, 308 and 349), followed by symmetric Gershgorin bounds. The minimum over the 1728 sub-boxes is ≥ **0.0292**.
     - Since X ⪰ Xmin ≻ 0, R(z) ⪯ R̄ whenever c(z) ∈ C_box.
3. **(T) Taylor step.** The segment {tK_uη : 0 ≤ t ≤ 1} stays in C_box. So Ψ*(K_uη) ≤ Ψ*(0) + ℓ_u·η + ½ηᵀQ_uη, where ∇Ψ*(0) = (5/4)1 supplies ℓ_u. Multiplying by n^u > 0 gives U(η) ≤ Ū(η) := Σ_u [n^u(Ψ*(0) + ℓ_u·η + ½ηᵀQ_uη) + (3/2) n^u ln n^u].
4. **(C) Concavity of Ū.**
   - Ū(0) = Ψ*(0) − 3 ln 3 = L* (Lemma F), and ∇Ū(0) = 0 exactly.
   - Hess Ū(η) = Haff_0 + Σ_c η_c Haff_c + Σ_u (3/2) A_uA_uᵀ/n^u(η), where Haff_0 := Σ_u [A_uℓ_uᵀ + ℓ_uA_uᵀ + Q_u/9] and Haff_c := Σ_u [A_u(Q_ue_c)ᵀ + (Q_ue_c)A_uᵀ + A_{u,c}Q_u] are exact rationals.
   - Hess Ū is negative definite on each of the 4⁴ = 256 sub-boxes of B0 (congruence + Gershgorin), with margin ≥ **1.1650**.
   - So Ū is strictly concave on B0 with a critical point at 0, and ln F(n) ≤ U ≤ Ū < L* for η ≠ 0. ∎

**Runs (checker A, r2).** `code/cert_ldc3_r2.py` is the parent's guarded copy (`review/colour-centralA-guarded-v2/cert_ldc3.py`, sha256 2aa71de6…0d1cd: NC, M > 0; PASS only if all NC³ + M⁴ boxes are checked; exit code). On top of that it refuses `python -O` and replaces every certificate-critical `assert` with `require()`, an explicit FAIL with exit 1. Log: `evidence/cert_ldc3_r2_runs.log`.

| invocation | result | exit code |
|---|---|---|
| `1/10000 3/20 12 4` | PASS; output byte-identical to the pinned r1 output (sha256 39349c26…c6fa) | 0 |
| `1/10000 0 4 2` (ε = 0 negative control) | FAIL; 64/64 Q boxes fail | 1 |
| `python -O` | refused | 1 |
| NC = M = 0 or −1 | rejected | 1 |

## 5. Conclusion
- Let n ∈ Δ∖{n*}. By Lemma G, n lies in some Σ_u. By Lemma D or Lemma E, ln F(n) < L* = ln F(n*) (Lemma F). Hence H1.1 holds: strictly, with a unique maximiser, on closed Δ.
- **Lemma F′** adds that b is the unique maximiser of f on 𝒟. This is what the paper's Lemmas 5.6 and 5.8–5.10 use.
- **The m-form follows.** Let m ∈ M with L(m) := Σ_u ψ(m^u) ≥ L*. The per-class maxima attaining L(m) form some d ∈ 𝒟 with f(d) = L(m) ≥ L*. By F′, d = b, so m = m* = (5/36)1.

## 6. Trusted base, checkers and controls
- **Written proofs.** Lemmas 0, A (A1–A3), B, C, F, F′, G, and the analytic steps of E. Both hostile reviews re-derived them, with no critical or major finding.
- **Lemma A positivity.** Five computations agree: flint (r1) and the standalone r2 script (byte-identical), the sympy worker, the parent's integer recomputation, and the Codex reviewer's integer rebuild.
- **Lemma D.**
  - Checker A: python-flint arb, run with `--require-r0 1/10000`.
  - Checker B: mpmath.iv, separate author, `checkerB/evidence/cells_iv_all9_final.json`. 9/9 PASS with identical leaf counts; minimum margin ≥ 1.7270e−11. It pins r1 = 1/10000, and it maximises over the 8 vertices of conv(S) (re-enumerated in code).
  - Checker C: Codex-authored arb checker, run by the parent (`review/colour-codex-checker-v1/parent-result.json`; checker sha256 e4c055da…a217; status PARENT_INDEPENDENT_CHECKER_AND_CONTROLS_PASS). Totals: 592,327 nodes, 296,159 splits, 291,552 dual and 4,616 central leaves, 0 failed. It also passed a positive smaller certificate (r1 = 1/20) and rejected 8 corruption controls for the intended reasons.
  - Codex reviewer: replayed all tree structures (the largest central-vertex radius is 7/73728 < 1/10000) and evaluated 36 dual leaves (180 vertex tests) with 80-digit Decimal intervals, including every minimum-margin leaf.
- **Lemma E.**
  - Checker A: the pinned `code/cert_ldc3.py` and the r2 `code/cert_ldc3_r2.py` (§4 table). The parent replayed the pinned run.
  - Checker B: the pinned `central_iv.py`, plus r2 `checkerB/code/central_iv_r2.py` with `cb_common_r2.py` (`checkerB/README-r2.md`).
    - Positive run: PASS, exit 0; 512/512 Q boxes with minimum Gershgorin ≥ 0.0708; 16/16 (C) vertices with δ = 1176209/10⁶; all 22 explicit checks ran.
    - ε = 0: FAIL, exit 1. `python -O`: refused, exit 3. Invalid arguments: exit 2.
    - The parent's replay of the pinned checker B (`review/colour-parent-centralB-v1/parent-result.json`) gave PASS, and ε = 0 FAIL as intended. The Codex reviewer's rerun agreed, and it checked all 16 Hessian majorants exactly.
- **Checker B's actual (C) step (L9c).**
  - Let n_lo,u be the exact minimum of n^u over B0 (≥ 2491/22500). Then Hess Ū(η) ⪯ Tm(η) := Haff_0 + Σ_c η_cHaff_c + Σ_u (3/2)A_uA_uᵀ/n_lo,u, because A_uA_uᵀ ⪰ 0 and 1/n^u(η) ≤ 1/n_lo,u.
  - Tm is affine in η. Exact rational tests show Tm(v) + δI ≺ 0 at the 16 vertices v of B0, with δ = 1176209/10⁶. So Hess Ū ⪯ −δI on B0.
- **Checker B's inputs (L9d).** Its README imports "ψ concave on conv(S)" (D4). What it actually uses is (A2) for the dual leaves, and (A2) with (A3) for the central box. Both are proved in Lemma A, so the stronger import is not needed.
- **Rigour.** The rigorous base is python-flint 0.9.0 (arb). mpmath.iv 1.3.0 is corroboration, since its elementary-function enclosures are less documented. The certified margins (≥ 1.7270e−11; ≥ 0.0292 and ≥ 1.1650; ≥ 0.0708) are far above working precision, which is at least 128 bits.
- **Common-mode risk.** Checkers A, B and C all implement one written scheme, so a scheme-level error would pass all three. The written lemmas are the safeguard; they were hostile-reviewed.
- **Not trusted.** The producers (`outer/code/bnb_produce.py`, `outer/code/fastdual.py`, `code/dual.py`), the floating-point searches and the multistarts.
- **Controls.**
  - Ordinary-colouring analogue: non-central global maximum, +0.01374 (p. 4 remark).
  - Checker-A mutations, all rejected: y × 1.1, far μ0, L* − 0.02 (rejects 32,888 of 33,032 cone-(0,0) leaves, including those near the secondary maxima of margin 0.0106), dropped subtree, relabelled leaf, changed r0.
  - Checker-B mutations, all rejected.
  - Checker-C corruption controls.
  - ε = 0 central controls in A, B and the parent replays.
  - The anchors (§2).

## 6a. Trust inherited from the paper (imported, NOT checked here)
The implication "H1.1 + Lemma F′ ⇒ χ(G_{n,5}) = 3 a.a.s." uses the following steps of the pinned preprint as published. This lane checks only the Theorem, Lemma F′ and the exact constants of §2.
- **Small subgraph conditioning.** Theorem 2.1, from [17, Cor. 4.2], with conditions (i)–(iv). The overlapping-cycle joint moments (3.2) are sketched on pp. 11–12.
- **Asymptotics.** Lemma 5.1 (Stirling uniformity), Lemma 5.9 (Euler–Maclaurin summation over J̃; Laplace's method via Wong, Thm IX.5.3), Lemma 5.10, Theorem 5.1. The constants are reproduced; the analysis is not.
- **Section 6.** Theorem 6.1, (6.1)–(6.4) and the vertex-deletion argument are sketched. (6.3) also uses the Lemma 5.9 lower bound, which depends only on H1.1 and F′.
- **Standard facts and minor paper wording.**
  - G_{n,5} is a.a.s. not bipartite, and pairings transfer to simple graphs.
  - p. 6: "P(X2 = 0) bounded away from 0" should be read conditionally on X1 = 0.
  - p. 4: the claim that there is no boundary local maximiser is not proved in the paper, and is not used here.
  - p. 22: typo.
- **Version.** The published text of JGT 61 (2009) 157–191 was not compared with the preprint.

## 7. Claim discipline
- **Correctness.** Hostile reviews: Claude ACCEPT-WITH-FIXES (2 MEDIUM, 9 LOW) and Codex ACCEPT-WITH-FIXES (4 MINOR); the fixes are applied here. Implementation reviews: central A ACCEPT-WITH-FIXES (vacuous-PASS guard, fixed in r2) and central B ACCEPT.
- **Novelty.** The parent's audit (`review/colour-priority-audit.md`) found no earlier proof. A search miss does not establish novelty.
- **Attribution.** The reduction and the conditional theorem are due to Díaz et al. EulerSolve OPG-37656 (a different model) was read, and nothing from it is used.
