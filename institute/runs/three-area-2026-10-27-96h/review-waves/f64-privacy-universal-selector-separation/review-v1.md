# Independent same-harness review: universal first/squared selector separation

Observed clock immediately before writing: **2026-10-28T18:01:10-0700 PDT**.

## Verdict and scope

**FATAL 0 / MAJOR 0 / MINOR 0 at the stated imported per-cost theorem.** The candidate's all-finite-ε selector separation, strict comparison, full-closed-ball/all-Borel feasibility, and parameter-specific positive gap are supported by the reconstruction below. This is a same-harness mathematical review conditional on §I of the named MDA26 alternative per-cost import. I read that complete parent input but did not independently reopen or re-review its underlying 237-line proof. Nothing here certifies that imported proof, an as-printed source proof, or any broader theorem by implication.

I actually read the frozen manifest first and then, in the prescribed order, **all 74 LF** of `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md` (SHA-256 `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`) and **all 148 LF** of `frontier-20261028-universal-pmlr-selector-separation-v1.md` (SHA-256 `4c92d56867a959298836063d0045634cd61a0efb8f3175fcb701c4ac4a722fc6`). Both sizes and hashes matched the manifest; the checker also rehashed them. The manifest SHA-256 is `1ae4161cc11acb940391a58b5b5f1c4798e3ca53b3eabb24ddaeba17b19acae5`. No held payload was used as a premise.

## Actual source objective and import

I inspected the cited local publisher PDF, SHA-256 `4e67a46d80e705df6b23a92e8fb88599a8b14c874af3f7b434a0ed217ca71df3`, particularly printed pp. 2–3: Definition 3 imposes the additive privacy inequality for events and shifts in the sensitivity set; §2.1 defines loss by the **first power** of the matching norm, so its expected objective is `E[||Z||_K]`; Definition 5 defines optimality for that objective; Definition 6 and Theorem 2 assert existence of an optimal generalized staircase. The source also discusses empirical performance under other metrics, so the qualification is specifically about its theoretical optimality objective, not a claim that it never mentions other metrics. Publisher identification: https://proceedings.mlr.press/v258/kulesza25a.html . The candidate does not refute that first-norm theorem. Its right-closed threshold convention and the source's displayed half-open intervals differ at most on countably many diamond boundaries, hence define the same absolutely continuous laws; the γ=0 law agrees with γ=1 almost everywhere after normalization.

The actual import's common model requires a compact, convex, centrally symmetric norm ball with interior and **every** Borel event and **every** shift in the **closed** ball. Its §I gives, separately for each nonnegative nondecreasing matching-norm cost, equality of the all-law infimum and the attained minimum over the centered staircase family. `K=D={||h||_1≤1}⊂R²`, `φ(r)=r` and `φ(r)=r²` each meet those hypotheses. Their finite staircase costs are established below. Thus finding each scalar minimum identifies an all-law minimizer for that cost; it does not identify all minimizers, provide a shared minimizer, or make squared Euclidean loss a matching-norm cost. §II's universal dominator and all-law uniqueness are not used.

## 1. Full privacy and exact layer normalization

For `b=e^(−ε)∈(0,1)`, `m=b/(1−b)>0`, `r(x)=||x||_1`, and `0≤g≤1`, put `n_g(x)=min{k≥0:r(x)≤g+k}` and `f_g(x)=b^n_g(x)`. If `||h||_1≤1`, the triangle inequality gives `r(x+h)≤r(x)+1`. If `n_g(x)=k`, then `r(x+h)≤g+k+1`, so `n_g(x+h)≤k+1`; reversing the roles of `x` and `x+h` gives the other inequality. This is pointwise for **every** `x` and every closed-ball `h`, including all threshold boundaries. Consequently `f_g(x+h)≥b f_g(x)`, and for any Borel `A`, translation of Lebesgue measure gives

`Q_g(A+h)=Z_g^(−1)∫_A f_g(x+h)dx ≥ b Q_g(A)`.

This pays the event and shift quantifiers without interchanging uncountably many exceptional null sets.

Pointwise, including `g=r=0`,

`f_g(x)=(1−b) Σ_{k≥0} b^k 1_{r(x)≤g+k}`.

A diamond of radius `R` has area `2R²`, and for `p≥0` its `r^p` integral is `4R^(p+2)/(p+2)`. Tonelli and `K∼Geom(1−b)` on nonnegative integers therefore give

`Z_g=2 E[(g+K)²]=2D(g)`,

`∫f_g r^p dx=4 E[(g+K)^(p+2)]/(p+2)`.

The geometric factorial moments `E[(K)_j]=j!m^j` give

```
D  = g²+2mg+m+2m²,
M3 = g³+3mg²+3(m+2m²)g+m+6m²+6m³,
M4 = g⁴+4mg³+6(m+2m²)g²
     +4(m+6m²+6m³)g+m+14m²+36m³+24m⁴.
L = (2/3)M3/D,        W = M4/(2D).
```

`D>0` on `[0,1]`; all these sums converge. In each quadrant, write `(x₁,x₂)=(ru,r(1−u))` with `0≤u≤1` and Jacobian `r`. The angular integral of `u²+(1−u)²` is `2/3`, so **for these diamond-radial laws only**, `J=(2/3)W`.

At `r>0`, `n_0(r)=n_1(r)+1` and `Z_0=bZ_1`, so `Q_0=Q_1` as probability measures. At `r=0` the unnormalized indices coincide rather than differ by one; this single point is null. This distinction does not weaken the pointwise privacy proof above.

## 2. Derivatives and all-m root order

The quotient rule and the displayed moments give, identically for `m>0`,

```
L' = (2/3) Q/D²,
Q = g⁴+4mg³+6m²g²−2m(1+3m)g+m²,
W' = P/D²,
P = g⁵+5mg⁴+(2m+12m²)g³+(12m³−2m)g²
    −m(1+2m)(1+6m)g+m²(1+2m).
```

Let `v=m(1+m)`, `t=1+2m`, `x=g+m`. Then `t²=4v+1` and

`Q=x⁴−2vtx+3v²`.

Set `g₀=√v−m`. Since `m<√v<m+1`, `g₀∈(0,1)`, and

`Q(g₀)=2v^(3/2)(2√v−t)<0`, because `t²=4v+1`.

Moreover `Q(0)=m²>0`, `Q(1)=(1+m)²>0`. Its descending nonzero coefficient signs are `+,+,+,−,+`, with exactly two changes. IVT gives one root on each side of `g₀`, and Descartes, counting multiplicity, makes these the only two positive roots and makes both simple. The second root `γ₁∈(g₀,1)` is the unique scalar global minimum of L: L increases, then decreases, then increases; also `L(0)=L(1)`. Thus `x₁=γ₁+m>√v` and `z=x₁²/v>1`.

Independently, the checker verifies the useful all-m rational negative witness

`(1+2m)^4 Q(m/(1+2m)) = −v²(8v+1)<0`.

This is a separate exact control, not a replacement for the `x₁>√v` argument.

With `R=2g³+6mg²−(1+6m)g+m`, the exact identities are

`P=(g+m)Q+vR`,  `R=2x³−(1+6v)x+2vt`.

At `Q(γ₁)=0`, eliminate `2vt` to obtain

`R(γ₁)=[3(x₁²−v)²−x₁²]/x₁`.

Squaring the positive equality `2vt=(x₁⁴+3v²)/x₁` and using `t²=4v+1` yields

```
1/v = ((z²+3)²−16z)/(4z),
1/v − 3(z−1)²/z = (z−1)³(z+3)/(4z),
P(γ₁) = −v³(z−1)³(z+3)/(4x₁) < 0.
```

The denominator-cleared factor identity was also checked as a polynomial identity; strictness follows from `z>1`, not from sample root comparisons.

`P(0)=m²(1+2m)>0` and `P(1)=(1+m)²(1+2m)>0`. Its descending nonzero coefficients have exactly two sign changes for every `m>0`, including when the `g²` coefficient vanishes. IVT now gives one positive root before γ₁ and one after, while Descartes counts exactly these two and their multiplicities. The second root `γ₂∈(γ₁,1)` is simple and is the unique scalar global W-minimum, using `W(0)=W(1)`. Hence `W'<0` and `L'>0` on `(γ₁,γ₂)`, giving strict opposite-cost inequalities. `J=(2/3)W` supplies the strict Euclidean comparison between these two actual feasible laws.

## 3. Fixed-ε explicit bounds and all-law caller

On `[0,1]`, termwise bounding the explicit derivative of P gives

`|P'|≤B=5+31m+44m²+36m³`.

Let `p₀=−P(γ₁)>0`, `h=min{(1−γ₁)/2,p₀/(2B)}>0`, and `Dmax=D(1)=(1+m)(1+2m)`. The derivative bound gives `P(g)≤−p₀/2` for `g∈[γ₁,γ₁+h]`, while `D(g)≤Dmax`; hence

```
W(Q_γ₁)−W(Q_(γ₁+h)) ≥ p₀h/(2 Dmax²),
J(Q_γ₁)−J(Q_(γ₁+h)) ≥ p₀h/(3 Dmax²).
```

If `V=inf_{μ feasible} J(μ)`, the competitor is feasible, so the same last lower bound holds for `J(Q_γ₁)−V`; no existence or radiality of a Euclidean optimizer is assumed. Likewise `Wmin=W(Q_γ₂)` at the per-cost import and has at least the W bound above. Since `P(γ₂)=0`, the mean-value theorem gives `γ₂−γ₁≥p₀/B`. These are explicit for each fixed ε via its uniquely characterized quartic root; no ε-uniform lower bound is asserted.

Applying the import separately makes `Q_γ₁` an all-Borel global L-minimizer and `Q_γ₂` an all-Borel global W-minimizer. The feasible competitor `Q_γ₂` proves that this **particular** global L-minimizer is not a global J-minimizer. This is not a statement about all L-minimizers, nor a solution or uniqueness theorem for the original mixed-norm Euclidean problem.

## 4. Executed exact checks and controls

A newly authored standard-library sparse-polynomial/Fraction checker was run: [checker-v1.py](checker-v1.py), SHA-256 `9ad78623ce9d0b01e516b9a79c4f466700eae1a76ebba30d300032f9c7ae41c9`; [checker-receipt-v1.json](checker-receipt-v1.json), SHA-256 `fe837e04b152cdfeb2e3665b50e98a51a2f023edb8646bbbed0d9f362e1f86b1`, records observed pre-creation clock `2026-10-28T18:00:01-0700 PDT`. The completed run reported **46 exact checks, six intended-reason controls, and five exact rational parameter certificates** (`m=1/10000,1/10,1,10,1000`). It independently generated moments from geometric factorial moments, checked both quotient-rule numerators, shifts/factor identities, endpoints, the derivative bound, exact isolating intervals and positive rational gap lower bounds. Controls reject omitted normalizer/fourth-moment terms, a perturbed derivative, an incorrect strict factor, an incorrect angular factor, and an unwarranted shift outside the unit diamond. Boundary samples cover `g=0,1/4,1/2,1`; these finite checks do not prove all real shifts or all m.

A useful exact event control takes `b=1/2`, `g=1/2`, and `A={||x||_1≤1/8}`. `A` is entirely layer 0; for `h=(1,0)` the translated event is entirely layer 1, saturating the required inequality. For the **outside-domain** shift `h=(7/4,0)`, it is entirely layer 2 and the same one-step bound fails, as intended. This control does not assert privacy for shifts outside the closed unit diamond.

A separate exact Fraction calculation at `m=1` gave `Q(7/10)=−479/10000`, `Q(71/100)=3036081/100000000`, `P(71/100)=−4072390149/10000000000`, and `P(73/100)=724572093/10000000000`. Thus the second Q-root lies in `(7/10,71/100)` and the second P-root in `(71/100,73/100)`. Direct evaluation also gave `W(71/100)−W(18/25)=2962881/24812660000>0`. This is a bounded reason-sensitive control, not the all-m proof.

Execution history: the first checker run stopped at its first rational comparator with `TypeError` because the independent checker omitted the `m` argument in two calls to `W`; it created no receipt. Both calls were corrected, and the complete checker was then rerun successfully. This failure and correction are also recorded in the receipt; it is not a finding against the candidate.

## Limits

No independent-family or external-model review, human review, formal/kernel proof, worldwide literature/priority verification, or complete original squared-Euclidean solution is claimed. The numerical certificates are bounded diagnostics; the all-variable conclusion rests on the written argument and the explicitly named per-cost theorem as an import. Existing source-proof, process, and publication qualifications are not modified.
