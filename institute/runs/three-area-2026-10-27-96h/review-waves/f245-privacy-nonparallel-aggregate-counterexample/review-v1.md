# f245: independent same-harness review of the nonparallel aggregate obstruction

## Verdict and scope

**Supported as written:** for every `2/3 <= b < 1`, both constructed phase laws belong to the original full closed-diamond privacy class; the nonparallel phase has strictly smaller squared-Euclidean cost than the minimal-shell phase with the same initial square; and its signed aggregate excess at the actual all-law infimum is strictly negative. At `b=3/4` the two costs, their difference `2461/12265`, and the true-infimum aggregate upper bound `-325/14` are exact. No mathematical fatal, major or minor defect was found in the scoped claims; none of those claims is inconclusive under the elementary imports stated below.

**Precisely refuted:** an unconditional comparison asserting that, for *every* feasible canonical geometric phase with a specified initial core, replacing all subsequent levels by that core's minimal shells cannot increase cost, or cannot increase the signed aggregate evaluated at the true all-law infimum. For the exhibited same-core pair, replacement by minimal shells increases both quantities in the asserted comparison direction.

**Not refuted:** minimal-shell structure of an actual optimizer, nor any assertion that an optimizer is nonparallel. Neither constructed law is established to be optimal. This counterexample does not rule out an optimizer-level argument using additional optimality or shape hypotheses. `f238`, LAW642 and `f208` are not premises, and no finding about them is made. The adopted `ln64` disposition is background/scope only, not used to infer any bound, formula, or optimizer structure here.

This is a **same-harness written review**, not a human review, independent-model-family review, formal/kernel verification, source-equivalence check, novelty verification, or parent adoption. Same-harness independence is not an independent-authorship or model-family claim.

## Frozen input verification, actual reading order, and deviations

1. Opened the manifest first, in raw windows `1-15`, `16-40`. Full measured SHA-256 of `manifest-v1.json`: `816befa77cc28a6dbd8601d0af2a6d4b907f0dd53c7186a0b17ce1db4c677c32`; this matches assigned prefix `816befa77cc2`.
2. Before opening either declared input body, measured both using `shasum -a 256` and `wc -lc`. First input, the adopted ln64 disposition: SHA-256 `4a7fd302c57df60e6df3221a1326452dd425d78a3a012916625399b15c1b629a`, 8,786 bytes, 54 LF. Second input, the target: SHA-256 `db29a99331592a5a8c87b51d45020338a81b5680716b00fc5f5ac77c48e4b1ce`, 13,240 bytes, 222 LF. All match the manifest.
3. Read the entire first input in manifest order, raw windows `1-15`, `16-30`, `31-45`, `46-54`; then read the entire target in raw windows `1-15`, `16-30`, `31-45`, `46-60`, `61-75`, `76-90`, `91-105`, `106-120`, `121-135`, `136-150`, `151-165`, `166-180`, `181-195`, `196-210`, `211-225`. The latter displays through the actual final line 222. No mathematical reasoning preceded completion of both inputs. The target's author certificate was read as required but was not run, imported, or used as evidence.
4. After the two frozen bodies, read process memory and the written-math acceptance protocol skill, before mathematical reconstruction. **Process-order deviation:** the global memory-summary-first and skill-first reads were deferred to give this assignment's explicit manifest-first and frozen-input sequence priority. They supplied process context only, not mathematical premises. No source-chain body, held/f161/f162 material, sibling review, external source or author contact was used.
5. Native `/bin/date` returned `2026-10-29T14:43:29-0700 PDT` before writing the reviewer-owned exact-control script. The bounded control run and its own receipt are below. Native `/bin/date` returned `2026-10-29T14:44:42-0700 PDT` before this report was written. These are observations before writes, not asserted file creation times. No other deviation is known.

## Per-claim dispositions

In the table, `0F/0M/0m; not INCONCLUSIVE` means that this reviewer found no fatal, major or minor defect in the stated claim, with the mathematical imports and review limitations below. It is not a formal proof or a broader acceptance verdict.

| Claim | Verdict and reason |
|---|---|
| Closed-D inclusions, nesting, exhaustion, compactness, convexity, D4 symmetry and centered sections for both sequences | `0F/0M/0m; not INCONCLUSIVE`: explicit Minkowski and reflection arguments in §1. |
| Both normalized phase laws satisfy every Borel-event inequality for **every** shift in the full closed diamond, including boundary shifts | `0F/0M/0m; not INCONCLUSIVE`: exact pointwise level-index inequality and translation in §1; no axis-only or lattice restriction. |
| Same initial core and genuinely nonparallel second sequence | `0F/0M/0m; not INCONCLUSIVE`: exact axis and diagonal extents in §1. |
| Complete areas, moments and nested-set excess (target (7)–(8)) | `0F/0M/0m; not INCONCLUSIVE`: direct square/strip/simplex integration in §2 and independent rational control. |
| Added-mass mixture, signed series and all real `lambda` identity (target (9)–(11)) | `0F/0M/0m; not INCONCLUSIVE`: exact weighted geometric sums and absolute convergence in §3. |
| Added component need not be private | `0F/0M/0m; not INCONCLUSIVE`: explicit positive rectangle and boundary-shift witness in §3. |
| All-law marginal and layer-cake lower bound (target (12)–(14)) | `0F/0M/0m; not INCONCLUSIVE`: all integer translates, two disjoint tails, and all intervals are accounted for in §4; no optimizer existence required. |
| Uniform inequality and sign at the true infimum, including `b=2/3` | `0F/0M/0m; not INCONCLUSIVE`: positive-coefficient expansion and finite infimum in §5. |
| Strict cost improvement for all `2/3 <= b < 1` | `0F/0M/0m; not INCONCLUSIVE`: mixture plus `T < V <= J(P_S)`; independently, direct gap polynomial has positive shifted coefficients. |
| Exact `b=3/4` values and signed bound | `0F/0M/0m; not INCONCLUSIVE`: fully rational computations in §6 and reviewer control. The bound is an upper bound, not a claimed exact value of the aggregate. |
| Scope and limitation of the obstruction | `0F/0M/0m; not INCONCLUSIVE`: counterexample concerns the unrestricted comparison, not the shape of an actual optimizer. |

## 1. Reconstruction of both full-class phase laws and geometry

Let `D={(x,y): |x|+|y|<=1}`, `C=[-1/2,1/2]^2`, `S_i=C+iD`, and `K_0=C`, `K_i=(i+1)D` for `i>=1`. For all `c in C`, `||c||_1<=1`, so `C subset D` and

```
S_i + D = S_(i+1),
K_0 + D = C + D subset 2D = K_1,
K_i + D = K_(i+1)  (i>=1).
```

All these are exact set statements for the **closed** D; positive dilates of D add exactly because D is convex. Each sequence is nested, consists of compact Borel sets, and covers the plane. Sums and positive dilates of compact convex sets are compact and convex. C and D are invariant under sign changes and interchange of coordinates, so all the stated sets have D4 symmetry.

The section assertion follows for every line, not just almost every line. A horizontal section is a closed interval centered on the y-axis by the reflection `(x,y)->(-x,y)`; a vertical section is centered on the x-axis. On `x+y=s`, the coordinate-swap reflection preserves the line and fixes `(s/2,s/2)`; on `x-y=s`, reflection `(x,y)->(-y,-x)` preserves the line and fixes `(s/2,-s/2)`. Convexity makes each nonempty intersection an interval, and the appropriate reflection makes it centered. Empty and singleton sections are allowed.

For either sequence E, define `n_E(x)=min{i>=0:x in E_i}`. The preceding exact inclusion yields `n_E(x+h)<=n_E(x)+1` for **each** `x` and **each** `h in D`, including `||h||_1=1`. Thus, for `0<b<1`,

```
u_E(x) = b^n_E(x) = (1-b) sum_(i>=0) b^i 1_(E_i)(x),
u_E(x) <= b^(-1) u_E(x+h).
```

The index and density are Borel. The level areas and second moments grow at most as constants times `(i+1)^2` and `(i+1)^4`, respectively; the geometric factor makes both the normalizer `Z_E=integral u_E` and moment `N_E=integral |x|^2 u_E` finite, and `Z_E>0`. Integrate the displayed pointwise inequality over arbitrary Borel `A` and translate Lebesgue measure to obtain `P_E(A)<=b^(-1)P_E(A+h)`. Therefore `P_S` and `P_K` are actual full-closed-D-private probability laws with finite cost.

The common initial level is exactly C. The maximum first-axis coordinate of `C+rD` is `1/2+r`; its maximum `t` on the diagonal point `(t,t)` is `1/2+r/2`. The corresponding maxima for `K_1=2D` are 2 and 1. Axis matching forces `r=3/2`, giving diagonal maximum `5/4`, not 1. Thus K is genuinely nonparallel to its initial square.

## 2. Reconstruction of the areas and moments

In one quadrant, `S_i` is given by `(x-1/2)_+ + (y-1/2)_+ <= i`. It decomposes into a quarter-square, two rectangles, and the triangle `u,v>=0`, `u+v<=i`, translated by `(1/2,1/2)`. Their respective total areas after multiplying by four are `1`, `4i`, `2i^2`. The corresponding moments are

```
1/6,
(4/3)i + 2i^2 + (4/3)i^3,
i^2 + (4/3)i^3 + (2/3)i^4.
```

For the triangle, use `integral 1=i^2/2`, `integral (u+v)=i^3/3`, and `integral (u^2+v^2)=i^4/6`, before multiplying by four. Consequently

```
|S_i| = 1 + 4i + 2i^2,
M(S_i) = 1/6 + (4/3)i + 3i^2 + (8/3)i^3 + (2/3)i^4.
```

The quadrant simplex of `rD` gives `|rD|=2r^2` and `M(rD)=(2/3)r^4`. For each `i>=1`, `S_i subset (i+1)D=K_i` by `C subset D`, hence subtraction is the area/moment of an actual nonnegative added set. Expanding gives

```
|K_i|-|S_i| = 1,
M(K_i)-M(S_i) = i^2 + (4/3)i + 1/2.
```

The difference is zero at `i=0`, because **both** initial levels are C. This distinction matters in the weighted sums.

## 3. Added-mass mixture and nonprivacy of the component

Put `m=b/(1-b)` and `T=17/6+(13/3)m+2m^2`. Since `sum_(i>=1)b^i=m`, `sum i b^i=m(1+m)`, and `sum i^2 b^i=m(1+m)(1+2m)`, the preceding level differences imply

```
Z_K-Z_S = (1-b)m = b,
N_K-N_S = b T,
H_K(lambda)-H_S(lambda)
  := sum_(i>=0) b^i [Phi_lambda(K_i)-Phi_lambda(S_i)] = m(T-lambda).
```

The last identity holds for every real lambda; absolute convergence follows from the polynomial bounds on moments and areas. By nesting, `u_K>=u_S`. The nonnegative added density has total mass b and moment bT, so normalizing it gives a probability law `P_add` of cost T and

```
P_K = [Z_S/(Z_S+b)] P_S + [b/(Z_S+b)] P_add,
J(P_K)-J(P_S) = [b/(Z_S+b)] [T-J(P_S)].
```

`P_add` is not entitled to the all-law lower bound: it is not private. For `A=(7/4,9/5) x (0,1/20)`, every point has l1 norm less than `37/20<2`, but l1 distance to C greater than `5/4>1`; hence `A subset K_1\S_1` and `u_K-u_S>=b-b^2>0` there. After the closed-boundary shift `h=(-1,0)`, the rectangle lies in `S_1` because its x-coordinate is between `3/4` and `4/5` and its y-coordinate is below `1/20`. All later S and K levels then contain it and the zeroth levels coincide, so `u_K-u_S=0` throughout `A+h`. Thus `P_add(A)>0=P_add(A+h)`, a direct violation of full-D privacy.

## 4. Independent lower bound on the true all-law infimum

Let a coordinate marginal be X. Pulling back each Borel set under that coordinate shows the one-dimensional privacy inequality for every shift `|h|<=1`; iterating gives, for `A=(-1/2,1/2)` and each integer k,

```
P(X in A+k) >= b^|k| P(X in A).
```

These open translates are pairwise disjoint even though their union can omit boundary points. Thus `P(X in A)<=1/(sum_Z b^|k|)=(1-b)/(1+b)` and, for `p(r)=P(|X|>=r)`,

```
p(1/2) >= c_b := 2b/(1+b).
```

For `r>0`, apply privacy separately to `[r,infinity)` shifted by +1 and `(-infinity,-r]` shifted by -1; they are disjoint, giving `p(r+1)>=b p(r)`. Hence `p(r)>=c_b` on `[0,1/2]`, and `p(r)>=c_b b^k` on `[k-1/2,k+1/2]` for every integer `k>=1`. Layer cake/Tonelli gives `E X^2=integral_0^infinity 2r p(r) dr`, with boundary atoms harmless in this integral. The first interval contributes `1/4`, and each subsequent interval contributes `2k`, so

```
E X^2 >= c_b [1/4 + 2 sum_(k>=1) k b^k]
       = c_b [1/4 + 2b/(1-b)^2].
```

Summing the two coordinate bounds does not assume independence. In terms of `m`, every feasible law, including those with infinite second moment, satisfies

```
J(mu) >= L(m) := (m+8m^2+8m^3)/(1+2m).
```

Therefore `V_b>=L(m)`. The class is nonempty and V is finite by the explicitly constructed finite-cost `P_S`; also the product density proportional to `exp[-ln(1/b)(|x|+|y|)]` is feasible by the triangle inequality. No existence or uniqueness of an optimizer is used.

## 5. Strict uniform conclusions at the actual infimum

Exact expansion, also checked by the reviewer control, gives for `x=m-2`

```
6(1+2m)[L(m)-T(m)]
 = 24m^3-16m^2-54m-17
 = 24x^3+128x^2+170x+3.
```

For `m>=2` all four terms are nonnegative and the constant is strictly positive; this includes the endpoint `m=2`, i.e. `b=2/3`. Thus `T<L<=V_b`. The signed series at the **actual** global infimum is consequently

```
H_K(V_b)-H_S(V_b) = m(T-V_b)
 <= -m [24(m-2)^3+128(m-2)^2+170(m-2)+3]/[6(1+2m)] < 0.
```

Also `J(P_S)>=V_b>T`, so the positive added-mass mixture coefficient proves `J(P_K)<J(P_S)`. This is an unconditional same-core phase comparison failure, not an inference about an optimizer. As an additional independent algebra check, the control derives `N_S-Z_S*T`; after substituting `m=2+x` its coefficients are `454/3, 1015/3, 248, 224/3, 8`, all strictly positive. This directly corroborates the phase-cost comparison without using the all-law lower bound.

## 6. Exact rational instance

With `m=3`, weighted geometric moments yield

```
Z_S = 1+6m+4m^2 = 55,
N_S = 1/6 + (23/3)m + (94/3)m^2 + 40m^3 + 16m^4 = 16087/6,
Z_K = Z_S+b = 223/4,
N_K = N_S+b T(3) = 64957/24,
J(P_S) = 16087/330,  J(P_K) = 64957/1338,
J(P_S)-J(P_K) = 2461/12265 > 0.
```

Here `T(3)=203/6` and `V_(3/4)>=L(3)=291/7`; hence

```
H_K(V_(3/4))-H_S(V_(3/4))
 = 3[203/6 - V_(3/4)] <= 3[203/6-291/7] = -325/14 < 0.
```

The actual aggregate can be more negative; the calculation does not identify V or assert equality in this bound.

## 7. Reviewer-owned exact-control receipt and negative controls

The independent script `reviewer-exact-controls-v1.py` uses only standard-library integers, `Fraction`, elementary polynomial operations and `signal`. It independently integrates rectangle/simplex monomials, obtains the level polynomials by exact interpolation of bounded-degree expressions, derives geometric moments via the Stirling recurrence and falling factorial moments, and then checks the symbolic uniform gap and exact rational instance. It does not run or import the author certificate. Its 120-second wall-clock alarm reports `UNKNOWN` and exits 124 on a cap; no cap was hit.

- Script SHA-256 measured before the run: `f008e01ddfdfc0597d059e92a984da51e3994571cdf498b7f6b3fd88164c3cfa`.
- Native start: `2026-10-29T14:44:11-0700 PDT`; native end: `2026-10-29T14:44:11-0700 PDT`; process exit `0`. These clocks have one-second displayed resolution.
- Seven deliberate mutations were rejected for their intended reasons: open instead of closed `K_1` fails the **pointwise boundary-inclusion** witness; replacing `K_0=C` by D changes the initial core; omitting the shifted triangle changes the area excess; moving the rectangle into S1 destroys the nonprivacy witness; using `k` instead of `2k` gives the wrong layer-cake weight; lowering the cubic coefficient of L from 8 to 7 destroys the claimed gap at `m=2`; reversing the lambda sign makes the signed aggregate nonnegative. The open-level mutation is only a negative control for exact pointwise inclusion, not a claim that a null-boundary modification necessarily changes privacy of a density.

## Imports and remaining gap

The reconstruction imports standard finite-dimensional facts about convex Minkowski sums, Borel sets, translation-invariance of Lebesgue measure, Tonelli/layer-cake, elementary polynomial/geometric sums and integration on intervals/simplexes. It does **not** import an optimizer theorem, attainment, the adopted ln64 bounds or shape theorem, any linked document, any author execution output, an external computation, or f238/LAW642/f208.

Remaining gap: this review does not determine `V_b` exactly, prove the existence or shape of a general-epsilon optimizer, validate an optimizer-specific bridge, establish novelty/source equivalence, or supply human, independent-family, formal or kernel verification. Nothing in the calculation justifies calling `P_add` private or treating its cost as an all-law upper/lower bound.
