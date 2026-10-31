# Review v1: full critical moment region

Native clock observed immediately before writing: `2026-10-28T19:35:25-0700 PDT`.

## Verdict and scope

**0 FATAL / 0 MAJOR / 0 MINOR** at the mathematical scope reconstructed below. This is a same-harness written review, not a parent adoption, independent-model-family or human review, formal/kernel proof, novelty assessment, or finite-ε region theorem. All asymptotics below fix each real θ before taking ε→∞. The full-event privacy requirement is for every Borel event and every displacement in the closed ℓ1 unit diamond D.

| Main step, candidate LF | F/M/m | Review disposition |
|---|---:|---|
| Density, peak, and translated floor, 41–56 | 0/0/0 | Reconstructed for negative θ, including a uniform-in-center quadratic bound. |
| Capped dual and all-law scalar value, 58–67 | 0/0/0 | Exact signed-cost identity and coercivity justify the bound and near-optimal deficit. |
| Actual shells for arbitrary K, 69–78 | 0/0/0 | Full closed-D/all-event privacy and the upper expansion do not require convexity, connectedness, or 0∈K. |
| Universal TV and both moments, 80–86 | 0/0/0 | Reconstructed; TV does not itself control second moments, and the macroscopic floor contributes a positive limiting term. |
| Differentiability, strict concavity, range of T′, 88–101 | 0/0/0 | Reconstructed via endpoint near-optimizers and a separate positive-θ scaling. |
| Separated disks and critical formula, 92–101 | 0/0/0 | Exact disk integrals, including tangency at the endpoint, give the stated branch. |
| Region necessity and exclusion of v=0, 103–105 | 0/0/0 | Scalarization and an independent capped ℓ1 bathtub give the claimed necessary conditions. |
| Boundary and every finite vertical ray, 107–112 | 0/0/0 | Actual private shell/translate mixtures attain the claimed coordinates. |

## Frozen input and imports

Read the manifest first, then the **entire** sole mathematical source in manifest order. Live checks:

- `manifest-v1.json`: SHA-256 `3167fca37019d0e1f9a15846584cebe3b7dd3ea520b3ca1efb15da6bb8869cba`; 1,735 bytes; 20 LF.
- `frontier-20261028-full-critical-moment-region-v1.md`: SHA-256 `c8ce61fb2d40463f5fdf488cb2ed5aebe40bf59c8bd97dc18b7674caf94bf463`; 10,008 bytes; 116 LF.

The candidate is the newly reviewed self-contained proof. Its LF 20 mentions a prior positive-θ candidate; that prior candidate was **not opened, reviewed, assumed, or imported**. The reconstruction uses standard Lebesgue differentiation/Fubini, elementary convexity and calculus, and the explicitly derived bathtub identity; it imports no prior scientific result from the research corpus. No author checker, held payload, public fetch, search, external model, or paid API was used.

## Reconstruction

Write `b=s⁴`, `cθ(z)=|z|²+θ‖z‖₁`, `G(T,θ)=∫(T−cθ)+`, and let `T=Tθ`, `K={cθ≤T}`, `A=|K|`, so `TA−∫K cθ=2/3`. Every step below is for a fixed θ.

### Density and the negative-θ translated floor

The privacy inequalities imply absolute continuity: for a Lebesgue-null event E, Fubini gives `μ(E+h)=0` for almost every h∈D, and privacy gives `μ(E)=0`. For a.e. x, integration of the density ratio over x+D bounds `2b p(x)≤1`; thus its essential supremum M is finite. Ball-average limsups give an a.e.-equal bounded representative satisfying the privacy density ratio at every point and every h∈D. Therefore a near-maximum x₀ yields the actual nonnegative floor `ℓ 1_(x₀+D)`, `ℓ=b(1−s)M`.

The exact unnormalized diamond integrals are `∫D|u|²=2/3` and `∫D‖u‖₁=4/3`. With `r=|t|`, direct integration of the marginal `2(1−|t|)+` gives

```
q(r) = ∫D |u₁+t| du − ∫D |u₁| du
     = 2r² − (2/3)r³,      0≤r≤1,
       2r − 2/3,            r≥1.
Q(x) = q(|x₁|)+q(|x₂|),    0≤Q(x)≤2|x|².
```

Consequently the translated floor has the exact form

`F_s(x)=2/3+2|x|²+θs(4/3+Q(x))`.

For θ<0 and `|θ|s≤1/2`, this is at least `2/3−(4/3)|θ|s+|x|²`; θ≥0 is easier. In particular the negative norm term is **not** discarded as nonnegative.

### Signed dual, coercivity, and the universal limit

Put `y=s²M`, `g=p−ℓ1_(x₀+D)`, `g#(z)=s²g(sz)`, and `h=∫g#=1−2(1−s)s²y`. Then `0≤g#≤y` and the exact signed-cost bathtub deficit is

```
∫cθ g# = T h − y∫(T−cθ)+ + Δ,
Δ = ∫_{cθ<T}(T−cθ)(y−g#) + ∫_{cθ>T}(cθ−T)g# ≥ 0.
```

This identity needs no sign assumption on θ or cθ. For any competitor whose scaled scalar cost is bounded above, `J/s²−|θ|√(2J/s²)` is bounded above, hence `J/s²` is bounded. The squared-cost floor gives `y≤3(J/s²)/[2(1−s)]`; hence `h→1`. Filling a centered disk under the cap gives `∫|z|²g#≥h²/(2πy)`, so y is also bounded away from zero. These bounds apply to optimizing and first-order-near-optimizing sequences.

Inserting the floor and dual gives

`(J+θsL)/s² ≥ T+(1−s)y|x₀|²−Oθ(s)y+Δ`.

The shell upper law below therefore proves `inf(J+θsL)=T s²+Oθ(s³)`. For every first-order-near-optimizer the nonnegative terms force `x₀→0` and `Δ→0`. Outside a thickness-η threshold band, the deficit bounds `‖g#−y1_K‖₁` by `Δ/η`; the level set is null and the bounded band area vanishes with η. Thus `y→1/A`, and the **whole** law of X/s converges in total variation to Uniform(K), despite the vanishing-mass macroscopic floor.

A bounded scaled second moment gives uniform integrability of the first norm, so `L/s→V=(1/A)∫K‖z‖₁`. The scaled second moment cannot be inferred from TV alone. Instead scalarized optimality and `TA−∫Kcθ=2/3` yield the exact universal limit

`J/s² → T−θV = (1/A)∫K|z|² + 2/(3A)`.

The second term is the macroscopic privacy-floor contribution; omitting it would give an incorrect moment limit.

### Actual shell and full-event privacy

For `S=sK`, let `n(x)=min{k≥0:x∈S+kD}` and `p_s(x)=b^{n(x)}/Z_s`. For every h∈D, `x∈S+kD` implies `x+h∈S+(k+1)D`; symmetry of D gives the reverse inequality. Hence `|n(x+h)−n(x)|≤1` everywhere, including diamond boundaries. Therefore `b p_s(x)≤p_s(x+h)≤b⁻¹p_s(x)` pointwise, and integration proves privacy for every Borel event. This argument never takes convex hulls of S and never assumes S is connected or contains the origin. Exponential shell decay makes Z_s and all required moments finite.

For fixed θ, K is bounded and nonempty. `D+sK` lies between a translate of D and an Oθ(s)-dilation of D, giving area and weighted symmetric-difference errors Oθ(s). Thus

```
Z_s = s²A + 2b + Oθ(bs) + Oθ(b²),
∫(|x|²+θs‖x‖₁)b^{n(x)}dx
    = s⁴∫K cθ + b(2/3+Oθ(s)) + Oθ(b²).
```

For the tail, `S+kD⊂(k+Cθs)D`, and the resulting fourth/third polynomial bounds summed against `b^k` are Oθ(b²). Since b=s⁴, the normalized scalar cost is `s²(∫Kcθ+2/3)/A+Oθ(s³)=T s²+Oθ(s³)`.

### T′, strict concavity, and its entire range

The level set of cθ has zero area, and neighboring sublevels are uniformly bounded. Differentiating G under the integral gives `G_T=A>0` and `G_θ=−∫K‖z‖₁`, so T is C¹ and

`T′(θ)=Vθ=(1/Aθ)∫Kθ‖z‖₁`.

For each s the scalarized infimum is concave in θ, and its pointwise limit T is concave. If concavity were not strict between two distinct endpoints, a middle-θ shell would have endpoint optimality gaps tending to zero as well. The universal TV result would force both endpoint uniform laws to coincide. Each K is regular closed: for θ≥0 move boundary points toward 0, and for θ<0 move them within their closed quadrant toward its minimizing center. Thus equality a.e. implies equality of the closed sets and their boundaries. Subtracting their boundary equations would force ‖z‖₁ constant on a nontrivial circular arc lying in an open quadrant, which is impossible. Therefore T is strictly concave and its continuous derivative is strictly decreasing.

For θ→+∞, set `z=θ^(-1/3)w`, `T=θ^(2/3)t`. The rescaled integrand tends to `(t−‖w‖₁)+`, whose integral is `(2/3)t³`; hence `T∼θ^(2/3)`. Concavity bounds T′ by forward/backward secants, giving `T′∼(2/3)θ^(-1/3)→0`. The explicit negative branch below gives `T′→∞` as θ→−∞. Thus T′ is a continuous strictly decreasing bijection ℝ→(0,∞).

### Exact separated-disk and intermediate-geometry checks

Let `τ=1/√(3π)`. For θ=−a and `a≥2√τ`, completing the square gives four quadrant disks of radius √τ around `(±a/2,±a/2)`. At equality neighboring disks touch at axis points; their interiors are disjoint. Exact radial integration gives

```
A = 4πτ = 4/(3τ),
G = 4·(π/2)τ² = 2/3,
T = −a²/2+τ,       V=a,
core E|Z|² = a²/2+τ/2,      floor = 2/(3A)=τ/2.
```

Consequently `U(v)=v²/2+τ` for every `v=a≥2√τ`. At θ=0, independently, the core is a disk with radius² `2τ`, `T=2τ`, `A=2/(3τ)`, `V=8√(2τ)/(3π)`, and both the core squared moment and the floor contribution equal τ.

A separate exact check exercises the connected, non-origin-centered regime. At θ=−a, T=0, polar integration in each quadrant gives

```
G(0,−a) = a⁴(π/4+2/3),
A(0,−a) = a²(π+2),
∫K‖z‖₁ = a³(π+8/3).
```

The origin lies on the threshold exactly when `a⁴=8/(3π+8)`, and there `V=a(π+8/3)/(π+2)`. In particular `G(−1/4,−1)=π/8<2/3<G(0,−1)`, so `−1/4<T_{−1}<0`. Its quadrant disks cross the axes but exclude the origin, yielding a connected non-origin core. For a>2√τ the four core disks are genuinely disconnected. The shell argument covers both, rather than borrowing a convex-core claim.

### Full region and mixing

For every finite-coordinate sequence, scalarization yields `u+θv≥Tθ` for every real θ. The peak floor gives the exact `s²M≤(3/2)J/s²`. A capped ℓ1 bathtub, filling a diamond of radius `(2y)^(-1/2)`, gives `L/s≥2/[3√(2y)]`; hence if `J/s²≤B<∞`, `L/s≥2/[3√(3B)]`. Thus v cannot be zero.

For v>0 use the unique θ with T′(θ)=v to obtain `u≥Tθ−θv`. The shell attains equality and is invariant under coordinate sign changes, so `EX₁=0`. For any finite t≥0, mix the shell with its e₁-translate at weight `δ=t s²`. Privacy is preserved under translation and mixtures, while exactly `J_mix=J_shell+δ` and `|L_mix−L_shell|≤δ`. The limiting point is `(U(v)+t,v)`. Therefore all, and not merely exposed, finite points of the claimed vertical-ray region are realized.

## Independent controls and limitations

`reviewer-independent-controls.py`, SHA-256 `87a9ee48eb7d498ad97c61bae389a50fdc66c00b460fadcd9a896d0a1e586189`, 6,238 bytes, 154 LF, was run with `python3 -B`. It imports Python `fractions` and `mpmath`, not author code. Exact rational checks cover the diamond marginal/floor formulas and sample negative-floor inequalities; coefficient checks cover both disk branches and the T=0 polar formulas. A disconnected pair of non-origin closed diamond cores passed **44,649** ordered rational-grid shift pairs; that finite test is only a diagnostic, while the all-real/all-event privacy argument is above.

Independent polar quadrature (not interval-certified) found `(θ,T,V)` approximately `(-2,-1.6742649921,2)`, `(-1,-0.1726019383,1.0294678746)`, `(0,0.65147001587,0.68511910071)`, `(1,1.2610480427,0.55077197898)`, and `(5,3.0332520162,0.37644526879)`. Central differences at θ=−1 and 1 agreed with the computed V to the displayed precision. The first version of the reviewer control failed an assertion because an integer division in the control introduced a float; the control was corrected to coerce all integration coefficients and endpoints to exact fractions, then the final pinned control completed successfully. This was a reviewer-control error, not a candidate finding.

No fixed-ε exact optimum, uniform-in-θ error bound, formal proof, external independent-family/human verification, or priority/novelty claim is established by this review. The independent finite checks do not replace the written all-law proof.
