# The four-zero branch is empty: an odd mod-8 law plus weighted block energies (v1)

**Status: UNREVIEWED AUTHOR CANDIDATE.** This is a conditional written argument with a small exact computer certificate. It is not a witness, not a global NL242 theorem, not a formal proof and not a novelty claim. Native clock before composing: 2026-10-29T08:16:13-0700.

## Statement

**Theorem.** Let `f:F₂⁹→{0,1}` be balanced with `max_a |W_f(a)| ≤ 28`. Put `k=W_f/4` and `Z={a: k(a)=0}`. Then `|Z|≠4`. With the adopted f152 scope (`|Z|` even, `4≤|Z|≤148`), every target function has `|Z|≥6`.

**Imported inputs.** These are the adopted same-harness dispositions f131/f152 (`info-6-four-zero-rank6-radical-parent-v1.md`, `info-6-four-zero-unequal-radical-phases-parent-v1.md`):
- `T≠0`. If `|Z|=4`, then `K=T^⊥` has `rank B=6` and `Z=R=rad B` is a 2-plane with `q|R=0`.
- (E8) `k(a⊕r) ≡ k(a)+4λ(r)q(a) (mod 8)` for `a∈K`, `r∈R`, with λ linear.
- `λ≠ρ`, and some input translate has `ρ=0` and `λ≠0`. Translation preserves every hypothesis, so assume this translate.

One standard fact is also used: on `H=F₂⁹∖K`, `k ≡ g:=(−1)^Q (mod 4)`. With `ρ=0`, g is constant on every R-coset.

## 1. Notation

- Let M be the 256-point support of f and `N(x)=#{y∈M: x·y=1}`. Then `k(x)=N(x)−128` for `x≠0`, `k(0)=0`, so `k≡N−128 (mod 8)` everywhere.
- For `r∈F₂⁹` put `M^r={y∈M: r·y=1}`, `τ^r=⊕M^r` and `N^r(x)=#{y∈M^r: x·y=1}`.
- Choose a basis `ρ₁,ρ₂` of R and a complement `M₆` of R in K, so that `a=(r,s)`. Then `q(r,s)=Q₆(s)` is nondegenerate on `F₂⁶`: elliptic (28 zeros) if `z=112`, hyperbolic (36 zeros) if `z=144`. Take Q₆ in normal form.
- Identify `R*` with `F₂²` through the dual basis. Fix `λ̂=(1,0)` by GL(R).
- Fix `a₁∈H`. The 64 odd fibres are `b_s⊕R`, with `b_s=a₁⊕(0,s)`; the 64 even fibres are `(0,s)⊕R`.

## 2. Lemma 1 (derivative identity)

For all x (mod 8 at `x∈{0,r}`):

`k(x⊕r)−k(x) = |M^r|−2N^r(x)`, and mod 8 `k(x⊕r)−k(x) ≡ |M^r|−2(x·τ^r)−4Q^r(x)`,

where `Q^r(x)=⌊N^r(x)/2⌋ mod 2 = Σ_{{y,y'}⊆M^r}(x·y)(x·y') mod 2` has degree at most 2.

*Proof.* Passing from x to `x⊕r` flips `[x·y]` exactly for `y∈M^r`. Moreover `N^r ≡ x·τ^r (mod 2)`, and the second binary digit of N^r is `C(N^r,2) mod 2`. ∎

## 3. Lemma 2 (one quadratic for each radical direction, on both halves)

For `r∈R`: `τ^r=0`, `|M^r|≡0 (mod 4)`, and `k(x⊕r)−k(x) ≡ 4φ_r(x) (mod 8)` for **all** `x∈F₂⁹`. Here `φ_r=|M^r|/4+Q^r mod 2` is quadratic and `φ_r|_K=λ(r)q`.

*Proof.*
- On K, q is R-invariant, so `k(a⊕r)≡k(a) (mod 4)`. By Lemma 1, `|M^r|≡0 (mod 4)` (take `a=0`) and `a·τ^r=0` on K. Hence `τ^r∈{0,T}`.
- On H, `ρ=0` gives `k(b⊕r)≡k(b) (mod 4)`, so `b·τ^r=0` for odd b. This excludes `τ^r=T`.
- Lemma 1 then gives the displayed form, and (E8) identifies `φ_r` on K. ∎

## 4. Lemma 3 (odd mod-8 law and split geometry)

For odd b put `ω(b)=((k(b)−g(b))/4) mod 2`; equivalently `ω=1` iff `|k|∈{3,5}`. Then:

- **Fibre law.** `ω(b⊕r)=ω(b)+φ_r(b)` for all odd b and all `r∈R`.
- **Shape of φ_r.** For fixed odd b, `r↦φ_r(b)=ℓ_b(r)+ν(r)`. Here `ℓ_b∈R*` and ν is one quadratic form on R, independent of b, whose polar β is alternating.
- **Linear parts.** For `b_s` as in §1, `ℓ_{b_s}=Q₆(s)λ̂+T(s)+ν̂` with T linear and ν̂ constant.

*Proof.*
1. **Fibre law.** With g fixed on the fibre, `k=g(1+4j)` and `k(b⊕r)−k(b)=4g(j(b⊕r)−j(b)) ≡ 4(ω(b⊕r)−ω(b)) (mod 8)`. Lemma 2 gives the same difference as `4φ_r(b)`.
2. **Cocycle.** Applying Lemma 2 three times gives `φ_{r+r'}(x)=φ_{r'}(x⊕r)+φ_r(x)` for every x.
3. **Constant derivative on H.** `x↦φ_{r'}(x⊕r)−φ_{r'}(x)` is affine, being the derivative of a quadratic. It vanishes on K, because `φ_{r'}|_K=λ(r')q` and q is R-invariant. An affine function vanishing on the hyperplane K is constant on H; call that constant `β(r,r')`.
4. **Form of r↦φ_r(x).** On H this map is a quadratic function of r with x-independent polar β. Differences for two odd points are additive in r. Setting `r'=r` gives `β(r,r)=0`.
5. **Linear parts.** `φ_r(a₁⊕a)−φ_r(a)` is affine in a and `φ_r|_K=λ(r)q`, so `φ_r(b_s)=λ(r)Q₆(s)+L_r(s)+c_r` with `L_r` linear in s. At `s=0`, `ν̂:=c−ν` must be linear in r. Hence `T(s):=ℓ_{b_s}−Q₆(s)λ̂−ν̂` lies in R* for each s and is linear in s. ∎

**The two cases for ν.** On the plane R, β is either 0 or nondegenerate:
- **h=0.** ν is linear and is absorbed into ν̂. Each odd fibre's ω-pattern is `const+x·r` with `x=ℓ_{b_s}`.
- **h=1.** `ν=r₁r₂` after absorption. Each pattern is `const+x·r+r₁r₂`.

**Split distribution.** Let `N_x=#{s: ℓ_{b_s}=x}`. The first coordinate of `ℓ_{b_s}` is `Q₆+affine`, a nondegenerate quadratic of weight 28 or 36; the second coordinate is affine. Enumerating all `2¹²` maps T and all four values of ν̂ gives exactly eight vectors `(N₀,N₁,N₂,N₃)` for each form: `(0,0,28,36)`, `(0,0,36,28)`, `(12,20,16,16)`, `(16,16,12,20)`, `(16,16,20,12)`, `(20,12,16,16)`, `(28,36,0,0)`, `(36,28,0,0)`.

## 5. Lemma 4 (block energy)

For `c∈F₂²` let `A_c={x: x·ρ_i=c_i}`, a 7-flat. Restricting f to `A_c` gives `W_{f|A_c}(a)=Σ_{r∈R}χ_r(c)k(a⊕r)`, and Parseval on 128 points gives:

`Σ_{fibres F=a⊕R} (½Σ_rχ_r(c)k(a⊕r))² = 4096` for each of the four c.

These four equations are equivalent to Parseval plus the three radical correlations. The new information enters through the admissible fibre vectors.

## 6. Admissible fibre vectors

The checker enumerates these from the definitions above. Each fibre contributes `u(c)=(½Σ_rχ_r(c)k)²` to block c.

**Even fibres.**
- `s=0`: `k≡0`.
- `Q₆(s)=0`, `s≠0` (27 or 35 fibres): `k∈{±4}⁴`. Contribution 64 at one block, or 16 at all four.
- `Q₆(s)=1` (36 or 28 fibres): `k∈{±2,±6}⁴` with `(k/2)(−1)^{λ(r)}` constant mod 4, by (E8). The contribution vectors are, with e the number of `|k|=2` entries:

| e | λ̂ block | other blocks |
|---|---|---|
| 0 | 144 | 0 |
| 1 | 64 | 16 each |
| 2 | 16 | 64 at one, 0 at two |
| 3 | 0 | 16 each |
| 4 | 16 | 0 |

**Odd fibres.** `k∈{±1,±3,±5,±7}⁴` with one common residue mod 4, and ω-pattern in the class prescribed by Lemma 3.

## 7. Capacity certificates

For any weights w, Lemma 4 gives `4096·Σ_c w_c ≤ Σ_F max_{admissible}Σ_c w_c u_F(c)`. Three weight vectors certify violation in all 32 cases (2 forms × `h∈{0,1}` × 8 vectors N).

**(i) `w=(2,3,6,6)`, `h=1`.**
- Capacity per even fibre: at most 384 for `Q₆=0` and 432 for `Q₆=1`.
- Capacity per odd fibre: 668 in every class. The maximum is attained, for example, at `(1,−7,−7,5)`.
- Total capacity: `384·27+432·36+668·64=68672` (elliptic) and `384·35+432·28+668·64=68288` (hyperbolic), both below `4096·17=69632`.

**(ii) `w=(2,3,6,6)`, `h=0`, `N₂+N₃∈{0,32}`.**
- Odd capacity is 456 in classes 0 and λ̂, and 872 in the classes with second coordinate 1 (e.g. `(5,5,−7,−7)`).
- Total capacity: `55104+416(N₂+N₃)` (elliptic) or `54720+416(N₂+N₃)` (hyperbolic). At `N₂+N₃=32` this is 68416 or 68032, both below 69632.

**(iii) `w=(12,5,12,9)`, `h=0`, `N=(0,0,N₂,N₃)`.**
- Even capacities are 768 and 848. Odd capacities in classes 2 and 3 are 1776 and 1344.
- Total capacity: at most `768·27+848·36+1776·36+1344·28=152832` (elliptic) and 152192 (hyperbolic), both below `4096·38=155648`.

Every case is contradictory, so `|Z|=4` is impossible. ∎

## 8. Exact receipts and controls

- Checker: `frontier-20261029-fourzero-block-energy-check.py`, SHA-256 `25cc156ae5b4dddb872ed10d0ca32a1a222256cc20c5d3495ed26db41547bd4c`, 177 LF.
- Result: `frontier-20261029-fourzero-block-energy-check-result.json`, SHA-256 `52d0ba2accae27e15d71d06daaa33406d93a0064b9a1460eb7c2cdd090e6fe61`, 1103 LF.

The checker also runs four controls:
- **Identity control.** On seeded random balanced Boolean functions it checks Lemma 1 and `deg Q^r≤2`: 24576 checks, 0 failures.
- **Odd-law necessity.** With the odd mod-8 law removed, none of the candidate weights certifies.
- **Geometry necessity.** An explicit elliptic type-count assignment satisfies all four block equations. It uses only affine odd patterns, but its class distribution `(16,0,16,32)` is not one of the eight realizable vectors.
- **Exact arithmetic.** All checker arithmetic is exact integer arithmetic.

The first certificates came from Z3 LP-infeasibility runs. These are not inputs to the proof: the final check is the brute-force capacity inequality above.

## 9. Scope

The exclusion is conditional on f131/f152 (same-harness support), Lemma 1–4 as written, and the exact finite certificate. It uses the common frequency geometry (one φ_r per radical direction on both halves, and the class map `s↦ℓ_{b_s}`) together with support-moment Booleanity. Beyond the three radical equations, these are the only inputs.

Still open: the ≥6-zero cases, the remaining ranks/profiles, and any global NL242 statement. Not performed: an independent review, a human check, or a formal proof.
