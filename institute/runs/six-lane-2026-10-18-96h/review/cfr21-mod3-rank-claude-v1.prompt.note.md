**VERDICT: ACCEPT-WITH-FIXES**

I re-derived Theorem A, Corollaries A1 and A2, the rank definitions and the invariance claims by hand, and they are correct under 3 | n, 9 ∤ n. I found no counterexample to any core implication. The defects are one false identity in the point form and three loose or false scope sentences. Line numbers refer to the embedded text as displayed, with L1 as the title.

### FATAL
None.

### MAJOR
None.

### MINOR

**m1 — L25–26, point form (false as written; must fix).** The identity `a_i(c) = ⟨λ_i,y_c⟩ + s_i` with y_c ∈ F_3^r forces every a_i into span{coordinate functions of y, 1}. That space has dimension at most r+1.
- A column offset leaves r unchanged but can raise dim(span{a_i}+⟨1⟩) to r+2. So the identity conflicts with L9's "no normalisation".
- **Counterexample:** over Z_3, take rows (c², c²+c, c²+2c) = (0,1,1), (0,2,0), (0,0,2).
  - This is a DM, with K = ⟨(1,1,1)⟩ and r = 1.
  - The rows together with 1 span all of F_3^3.
- **In-scope version:** apply a generic column offset to any of the pinned (Z_21,6;1)-DMs.
- **Fix:** write `a_i(c) = ⟨λ_i,y_c⟩ + s_i + h(c)`, for example with h = a_{i_0}, or say "after subtracting row i_0 from all rows".
  - Then χ(c) = ⟨Σχ_iλ_i, y_c⟩ + const. Since the y_c affinely span F_3^r, **K = {χ : Σχ_i=0, Σχ_iλ_i=0}**, with equality rather than ≅.
  - Add "the λ_i are distinct", which follows from the support-2 exclusion and which "cap" presupposes.
- The cap, parallelogram and 4+1 consequences are unaffected.

**m2 — L76 (false as written; must fix).** "Generic stratum r = 6 (where all 96 known Z_21 DM6 live)" cannot hold.
- A 6-row DM has r ≤ k−1 = 5, and L67 itself reports r = 5 for these 96.
- **Fix:** "The 96 known DM6 are full rank (r = 5). Any 7-row extension of one has K ∩ {χ_new = 0} = 0, so every nonzero χ ∈ K involves the new row. Both r = 5 and r = 6 remain open for such extensions."

**m3 — L74–75, "mod-3 affine relation".** The sentence is true only for relations with coefficient sum 0 and constant value.
- Read loosely, it is false and would "prove" nonexistence.
- **Counterexample to the loose reading:** for any DM and rows a ≠ b, apply the column offset g := lift(a_a+a_b). The new rows satisfy a′_a+a′_b ≡ 0, a support-2 relation with coefficient sum 2.
- **Fix:** write "Σχ_i a_i ≡ const with Σχ_i = 0 and |supp χ| ≤ 5".

**m4 — L22 and L73, CFR ⇔ DM (an auxiliary normalisation, not part of the core).** The equivalence holds, but only for the right matrix.
- **CFR → DM:** take the rows {0, τ_1,…,τ_6}, where τ_r = σ_r⁻¹

(symbol → position, i.e. the inverse of the positional row σ_r). Columns are indexed by symbols.
- **DM → CFR:** subtract one row from every row. This is a column-offset equivalence. The result has a zero row, and the other six rows are bijections forming a CFR.
- "Affine rank 5 or 6" refers only to this 7-row matrix. It does not apply to:
  - the six τ-rows alone, which have r ≤ 5 (and r ≥ 4 by A2);
  - the positional array σ, which need not be a DM, because the Florentine condition constrains τ_r − τ_s, not σ_r − σ_s.
- Theorem A and A1 need no normalisation, because K and r are offset-invariant.
- **Suggested CFR-coordinate restatement:** there is no relation Σβ_rτ_r ≡ const (mod 3) with |supp β| ≤ 5 when Σβ_r = 0. There is also none with |supp β| ≤ 4 when Σβ_r ≠ 0, because the zero row absorbs −Σβ_r. For example, τ_a+τ_b ≡ const is excluded.

**m5 — L78–79, priority wording.** I cannot verify the Evans citation without tools.
- As paraphrased, it concerns the literal rows (0, x, 2x). For Z_n the Sylow-3 subgroup is always cyclic, so the paraphrase also covers 9 | n, where L3 is not proved.
- Maximality of {0, x, 2x} does hold for every odd n with 3 | n, by second moments. Let S = Σx² and T = Σx·d(x) over a hypothetical fourth row d.
  - Σ(d−x)² = S gives S = 2T.
  - Σ(d−2x)² = S gives S = T.
  - Hence S ≡ 0. But S ≡ 2n/3 (mod n); for n = 21, S = 2870 ≡ 14.
- L3 instead covers arbitrary rows whose mod-3 images sum to a constant, but needs 9 ∤ n.
- **Fix:** state that the two results overlap and neither contains the other.

**m6 — nits.**
- L23: write e_a+…+e_f rather than e_1+…+e_6.
- L21: restate the hypotheses 3 | n and 9 ∤ n.
- L52–56: state explicitly that A2 for k = 4, 5 follows because support ≥ 6 > k forces K = 0.
- A2 can be sharpened: for k = 6, r = 4 iff K = ⟨χ⟩ with χ of full support and μ ∈ {0,3,6}.
- The Step-3 count actually gives dim K ≤ 1 for every 4 ≤ k ≤ 7.
- L62–64: the 3-dimensional check is implied by the 2-dimensional one. Any 2-dimensional subspace of such a W would already be a 2-dimensional witness.

### Independent rederivation (all pass)

- **Rank, L13–15.**
  - The left kernel of the matrix [a_i − a_{i_0} (i ≠ i_0); 1] maps bijectively onto K, via (β, γ) ↦ χ with χ_i = β_i, χ_{i_0} = −Σβ and constant value −γ. Hence the rank is k − dim K = r+1, for every choice of i_0.
  - The dual of F_3^R/⟨1⟩ is the sum-zero space. The annihilator of the differences P_c − P_{c′} is exactly K, so the affine span has dimension r.
- **Invariance, L16–18.**
  - A row offset adds Σχ_i t̄_i to χ(c).
  - A column offset adds ḡ_c·Σχ_i = 0.
  - A unit u acts as ū = ±1, because 3 | n.
  - Permutations only relabel.
  - So K (up to coordinate permutation) and r are invariant, with no normalisation needed.
- **Step 0.** Reduction Z_n → F_3 is a homomorphism because 3 | n, and each residue class has n/3 elements.
- **Step 1.** The 8 nonzero pairs (x, y) give exactly ±f, ±g, ±(f+g), ±(f−g).
  - Character-free cross-check: N has sum n/3 on all 12 lines of AG(2,3).
  - The 4 lines through a point p cover p four times and every other point once.
  - So 4n/3 = 3N(p) + n, giving N(p) = n/9.
- **Step 2, shape list.** A support-m vector with μ entries equal to 2 has coordinate sum m + μ, so μ ≡ −m (mod 3). The list is complete:
  - m=1: no shape.
  - m=2: e_a−e_b.
  - m=3: μ ∈ {0,3}.
  - m=4: μ = 2 only.
  - m=5: μ ∈ {1,4}.
- **Step 2, identities.** Each re-expands correctly. The sign case is redundant because K is a subspace.

  | shape | f | g | f−g | f+g |
  |---|---|---|---|---|
  | e_a+e_b+e_c | a_b−a_a | a_d−a_a | a_b−a_d | a_a+a_b+a_d = s+(a_d−a_c) |
  | e_a+e_b−e_c−e_d | a_a−a_c | a_b−a_c | a_a−a_b | a_a+a_b+a_c = s+(a_d−a_c) |
  | e_a+e_b+e_c+e_d−e_e | a_a−a_c | a_b−a_c | a_a−a_b | a_a+a_b+a_c = s+(a_e−a_d) |

  Each entry is a difference of two distinct rows, plus a constant in the f+g column. k ≥ 4 is used only to choose d; 9 ∤ n is used only in Step 1.
- **Counts in F_3^7.** By support 2 through 7: 42, 70, 210, 210, 154, 42. The total is 728 = 3⁶−1.
- **Step 3.** On U, each coordinate functional is 0 or onto. When onto, 6 of the 9 elements are nonzero there. So Σwt ≤ 6k < 48 for k ≤ 7.
- **Support-6/7 shapes.**
  - m=6: μ ∈ {0,3,6}, giving 7+140+7 = 154 vectors.
  - m=7: μ ∈ {2,5}, giving 21+21 = 42 vectors.
  - That is five S₇-orbits, or three up to sign, exactly as listed in L23. The "iff" in A1 holds in both directions.
- **Point form, after the m1 fix.** Affine dependencies of support 2, 3, 4 and 5 correspond to coincident points, a collinear triple (λ_a+λ_b+λ_c = 0), a parallelogram, and λ_a+λ_b+λ_c+λ_d = λ_e.

### Machine-check claims

These are non-premises. I checked them by hand, not by trusting the reported counts.

**p4 "support 6/7: none" is true.**
- Suppose r1+r2 = ε₃r3+αχ and r1−r2 = ε₄r4+βχ, with r1, r2 independent modulo χ.
- Then (α+β)χ = −(r1+ε₃r3+ε₄r4) and (α−β)χ = −(r2+ε₃r3−ε₄r4).
- The case α = β = 0 is impossible:
  - if two roots share one index, exactly one of r1 ± r2 is a root and the other is ±(e_i+e_j+e_l);
  - disjoint roots give support 4.
- Otherwise a nonzero multiple of χ, which has support ≥ 6, equals a signed sum of three roots. That forces pairwise-disjoint supports and the (+++−−−) shape. The remaining subcases give r2 = ±r1, or a root of support 4.
- So root-line Fourier cannot exclude any support-6/7 χ, in dimension 2 or 3.

**Cap census: true, and 32,760 is exact.**
- For a 7-cap, let A, B, C, D count the parallel classes of plane types (4,3,0), (4,2,1), (3,3,1) and (3,2,2).
- The identities ΣC(s_P,2) = 84 and ΣC(s_P,3) = 35 give B = 3, C = 13−4A and D = 3A−3. Hence A ≥ 1, so some plane misses the cap.
- In that class the cap splits 4+3, and the 4-set is a parallelogram Π.
  - The non-parallel directions it determines are S̄₃−Π̄.
  - S̄₃−Π̄ never covers F_3²: every non-collinear triple lies in a complement of a translate of Π, i.e. a union of two lines.
  - So at least one direction is missed.
- At most one direction is missed: missing both d1 and d2 allows at most 2 points per plane of class ⟨d1,d2⟩, hence at most 6 points.
- Counting (cap, missed direction) pairs gives 13·36·270 = 126,360. Here 270 is the number of valid lifts over F_3² minus two points. Through a fixed point this is 126,360·7/27 = 32,760.
- The r ≤ 3 route therefore works for 9 ∤ n, and Corollary A1 subsumes it.

**p5.** The 96 Z_21 DMs and the two Z_27 witnesses depend on data I cannot check without tools. The Fourier control for n = 3 and n = 6 is exactly Step 1.

### Scope
- L4, L76 and L80 correctly disclaim nonexistence and novelty.
- L77 is accurate; Step 0 also uses 3 | n.
- The stated scope is narrower than what is proved: A1 holds for every (Z_n,7;1)-DM with 3 | n and 9 ∤ n, not just n = 21.
