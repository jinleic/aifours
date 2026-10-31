# f238 same-harness review: fixed-core parallel gap removal

Review drafting clock observed before this write: `2026-10-29T14:26:19-0700 PDT`.

## Disposition and exact scope

**Theorem A and the stated square-core inequalities are supported on the entire manifest scope: F=0, M=0, m=1, with the one minor qualification below.** I reconstructed the geometry, full closed-D feasibility, derivative bounds, finite/infinite comparison and all-law signed excess without adopting another research result. The symbolic coefficient and example calculations were independently checked by reviewer-written, exact, bounded controls. This is not parent adoption.

**m1 — contextual cost-ball criterion needs a precise conclusion** (source 207–209). The aside about a particular optimal phase having “minimal shells” does not specify its hypotheses or whether equality is of sets or only almost everywhere. The argument I can reconstruct proves equality **up to Lebesgue-null sets** under the explicit hypotheses in the last subsection below; literal set equality requires additional regularity. This is not a defect in Theorem A, which has strict equality in its radius sequence and whose proof does not use the aside.

**INCONCLUSIVE, not a premise:** source 32 and 47 allude to a reduction of original optimal laws to D4/four-direction-convex Steiner phases and to the resulting canonical profiles. No adopted disposition is declared in this manifest and that all-law reduction is not established by this packet. I do not import it. The statement that a particular earlier review, author-run cell, prior sweep or predecessor has a particular status is also not independently established here; I do not use those statuses as evidence. The standalone fixed-core theorem does not need any of them.

**Residual:** The theorem concerns `K_i=C+R_i D` for one common canonical `C`, not arbitrary nonparallel levels or arbitrary optimal laws. The original general-epsilon nonradial all-law optimization remains **open at this proof boundary**. No claim about literature-wide status, novelty, source/book equivalence, attainment, or a global optimum follows.

## Integrity, display chronology and imports

- First research artifact was the assigned manifest. Observed SHA-256 was `7d227f70753615619cd99b1ddb5497e2f2c0a81078289c1e8bdaedee29671f13`, matching the entire assigned digest. It was displayed raw at LF 1–15 then 16–30.
- Before displaying any declared input, `shasum -a 256` and `wc -lc` gave the sole declared input, `information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-nonradial-parallel-core-gap-removal-v1.md`, SHA-256 `91478ea61fed8a9a5e0f6551d11ced9f3ee890d9e1314c3a387c81a701b52286`, 331 LF and 21,446 bytes, exactly as declared. There were no mandatory correction inputs.
- The native display-start clock observed after integrity checking was `2026-10-29T14:21:14-0700 PDT`. The one declared input was displayed in order in raw windows 1–15, 16–30, ..., 316–330, and 331–331; a further raw request for 332–345 was empty. The completion clock was `2026-10-29T14:22:26-0700 PDT`. No mathematics or scientific control preceded completion of the declared source displays. General administrative memory/skill instructions were read between manifest verification and source display and were not mathematical evidence.
- Two initial raw requests for 46–60 and 106–120 returned path-not-found, with no content displayed; each was immediately retried successfully at the correct path before continuing in order. The latter failed request misspelled `aifours` as `aours`. No other display-order deviation occurred. A non-scientific runtime probe found SymPy unavailable, so the controls use only Python standard-library rational arithmetic; nothing was installed.
- **Mathematical imports:** only the definitions and statements of this declared target as objects to be checked, plus explicitly reconstructed elementary set/measure theory, integration, algebra, and geometric factorial moments below. There are **no adopted research-premise imports**. No linked/sibling/held/f161/f162 payload, LAW642, f208 theorem or verdict, author PASS, solver status, literature, web, other model, or author contact was used. The author code was displayed as part of the input but never executed, imported or compiled. No global PH execution, bulk scientific search, scientific certificate replay, build, lint, test suite, formatter, Git, deletion or publication was performed.

## Per-claim disposition

`F0/M0/m0` means no fatal/major/minor finding for the explicitly stated claim, not a formal certification.

| Claim (source LF) | Disposition | Basis / qualification |
|---|---|---|
| Canonical compact/nonconvex geometry and parallel area and moment formulas (43–76) | F0/M0/m0 | Direct octant/distance reconstruction below; singleton and nonconvex cases included. |
| Invariant bounds, including `K<=tU` (78–98) | F0/M0/m0 | Pointwise factorization and exact bounds below. |
| Uniform cost monotonicity and tail cost monotonicity for `r>=1` (100–150) | F0/M0/m0 | Independent coefficient construction and strict witnesses below; no extrapolation to arbitrary `r` for the tail. |
| Full closed-D privacy and finite moment (9–20, 153–167) | F0/M0/m0 | Direct pointwise translated-density proof, including `||h||_1=1`; independent boundary positive and negative control. |
| Last-gap removal, finite/infinite gaps and equality iff every radius is `g+i` (153–168) | F0/M0/m0 | Strict prefix/tail comparison and fixed-first-gap margin under dominated convergence. |
| Positive aggregate signed excess at the actual all-law infimum `V_b`, without `V_b<1/2` (18–25, 169–174) | F0/M0/m0 | Comparator is feasible, masses are ordered, and the exact signed-series identity is strict. Individual summands need not be positive. |
| True all-law coordinate tail bound and square signed example (27–30, 177–204) | F0/M0/m0 | Full Borel marginal argument and independent rational arithmetic; here `1/2<=b<1` follows from `epsilon>0`. |
| Nonparallel/general all-law limitation (32–34, 205–209, 328–331) | F0/M0/m0 | Explicit nonparallel feasible phase below; it is not an optimality counterexample. The optimizer-structure aside itself is INCONCLUSIVE as described above. |
| Cost-ball sufficient-criterion aside (207–209) | m1 | A precise a.e. version is reconstructed below; literal set equality and omitted hypotheses need clarification. |
| Statements about prior review/author execution/exploratory sweep (36–38, 211–223, 301–326) | INCONCLUSIVE | Historical execution and earlier dispositions are not independent premises. The relevant arithmetic was reconstructed independently. |

## Reconstruction

### Canonical geometry, including nonconvex cores

Let `t>0` and `F` obey (1). The D4 extension is compact and coordinate-downward closed in each quadrant. For a sorted `x_1>=x_2>=0`, reflect and coordinate-contract a closest core point; sorting the core point preserves domination by `x`. Thus the distance is `x_1+x_2` minus the largest `k_1+k_2` over dominated core points. If `x_2<=t` and `x_1>F(x_2)`, monotonicity of `F(y)+y` bounds that sum by `F(x_2)+x_2`, which is attained. If `x_1<=F(x_2)` the point is in the core. If `x_2>t`, the maximum is `2t`, attained at `(t,t)`. This proves (2); `C={0}` gives the same formulas at `t=0`.

In one octant the dilation has horizontal range `y<=x<=F(y)+r` for `0<=y<=t` and, above it, the triangle `t<y<=t+r/2`, `y<=x<=2t+r-y`. Direct integration yields

`A(r)=A0+8tr+2r^2`,

`M(r)=Q0+U0 r+(A0+8t^2)r^2+(16/3)tr^3+(2/3)r^4`.

For example, the added upper triangle has octant area `r^2/4` and octant moment `t^2 r^2/2+tr^3/3+r^4/12`; the lower-strip increments supply the remaining terms. Boundaries are null for the integrals, but feasibility below is pointwise and does not discard the sensitivity boundary.

The allowed profile `F(y)=t+(t-y)^2/(2t)` is genuinely nonconvex for `t>0`: at `t=1`, `(3/2,0)` and `(1,1)` are core points, but their midpoint `(5/4,1/2)` has `5/4>F(1/2)=9/8`. No convexity argument was used. As a second exact profile check, `t=1,F(y)=3/2-y/2` gives `(I,U,K)=(2,14/3,37/12)`, `A(r)=6+8r+2r^2`, `M(r)=23/4+(46/3)r+14r^2+(16/3)r^3+(2/3)r^4`, and uniform costs `493/192` and `583/120` at radii 1 and 2 respectively.

The three deviations from the square satisfy `I,U,K>=0`, `I<=4t^2` and `2tI<=U<=3tI` directly from `0<=F-t<=t-y` and `2t<=F+t<=3t`. For `K<=tU`, after factoring `F-t`, three times the remaining difference is `-F^2+2tF+2t^2-3y^2`, which is decreasing on `F in [t,2t-y]` and at the upper endpoint equals `2(t-y)(t+2y)>=0`. The inequalities also hold at `t=0`.

### Independent derivative argument and exact coefficient controls

For geometric `G`, let `m=b/(1-b)` and `H_j=E(r+G)^j`. The factorial-moment identity `E[(G)_k]=k! m^k` gives the displayed `H_1,...,H_4` and hence the source expressions for `Z=E A(r+G)` and `N=E M(r+G)`. The reviewer control generates these raw moments from Stirling numbers, differentiates in `r` **before** shifting the radius, and expands exactly over rational coefficients.

For `D=N'Z-NZ'`, the coefficient of `K` is `-Z'`. On the relevant domains `Z'>0`, so replacing `K` by its upper bound `tU` lowers `D`. The result is affine in `U`; consequently it is bounded below by the minimum of its values at `U=2tI` and `U=3tI`. For the latter, subtracting `(4/3)t^3(4t^2-I)>=0` gives a further valid lower bound. The independent exact results are:

| Domain | Endpoint | Nonzero coefficients | Strictness witness |
|---|---:|---:|---|
| `r=1+q`, `q,m>=0` | 2 | 76, all positive | constant `8/3` |
| `r=1+q`, `q,m>=0` | 3, corrected | 75, all positive | constant `8/3` |
| `r=q>=0`, `m=0` | 2 | 12, all positive | `t^5:64/3`, `q^5:8/3` |
| `r=q>=0`, `m=0` | 3, corrected | 11, all positive | `t^5:16`, `q^5:8/3` |

Hence `j(r)=M(r)/A(r)` is strictly increasing whenever `t+r>0`, while `J_tail(r)=N(r)/Z(r)` is strictly increasing for `r>=1`. At `t=r=0`, the uniform singleton has zero area and is not a probability, so no assertion about its undefined cost is needed. The tail law is an area-weighted mixture of uniform dilations `C+(r+k)D`; therefore `J_tail(r)>j(a)` for `a<r` whenever `A(a)>0`. Also `Z'(r)=8t+4(r+m)>0` for `r>=1`.

### Full closed-D privacy and all finite/infinite gaps

For the stated radii put `u_R(x)=(1-b) sum_{i>=0} b^i 1_{K_i}(x)`. Every `K_i` is compact and `K_i+D subset K_{i+1}`. For **every** `h` with `||h||_1<=1`, including its boundary, `1_{K_i}(x)<=1_{K_{i+1}}(x+h)`; hence pointwise

`u_R(x+h) >= (1-b) sum_i b^(i+1) 1_{K_i}(x) = b u_R(x)`.

Integrating over any Borel `A` gives `mu(A)<=b^(-1)mu(A+h)`. The normalizing mass `Z_R=(1-b) sum_i b^i A(R_i)` is finite by hypothesis and strictly positive (even for `t=g=0`, level 1 has positive area); the second moment is finite by the same hypothesis. Radius growth also makes the union of levels all of the plane. The no-gap comparator is dominated termwise and is likewise feasible. This is the original closed-D privacy model, not an almost-everywhere replacement of the sensitivity set.

For a last gap after `k`, write `a=R_k`, suffix start `z=a+1+delta`, and separate the density into its common prefix and `b^(k+1)` times the minimal-shell tail based at `C+zD`. If the prefix has mass `alpha>0`, its uniform-dilation mixture has cost `c<=j(a)`. The suffix has mass `beta(z)=b^(k+1)Z(z)` and cost `J_tail(z)>j(a)>=c`. Both `beta` and `J_tail` strictly increase with `z>=a+1>=1`, so the weighted total strictly increases. If `alpha=0`, the total is just `J_tail(z)`, which is strictly increasing; this covers the zero-area singleton case. Removing the last gap strictly decreases cost and preserves all inclusions. Iteration handles finitely many gaps.

For infinitely many, let the `n`th truncation retain `R_i` through `n` and use unit spacing afterward. Its radii never exceed the original and eventually equal every fixed original radius. Area and nonnegative moment are termwise dominated by the assumed summable series, so both mass and moment converge; their limiting mass is positive. Fix the first positive gap. For every sufficiently large truncation, remove all subsequent gaps: the result is the **same** one-gap phase, strictly above the no-gap comparator. Thus the same strictly positive margin survives the limit. Equality can occur only when all gaps vanish, i.e. every `R_i=g+i`.

For `V=V_b`, feasibility gives `0<=V<=J(P_K0)<infinity`. Let `Z_0` be the no-gap mass. Since `K_i^0 subset K_i`, `Z_R>=Z_0`. With a gap,

`(1-b) sum_i b^i[Phi_V(K_i)-Phi_V(K_i^0)]`

`= (Z_R-Z_0)[J(P_K0)-V] + Z_R[J(P_K)-J(P_K0)] > 0`.

The signed series is absolutely convergent by the finite mass/moment assumption. The argument uses the actual all-law infimum and neither assumes its attainment nor places it below `1/2`.

### All-law tail and square example

A coordinate projection of any feasible planar law is one-dimensional private for shifts in `[-1,1]`. With `p(r)=P(|X|>=r)`, translating the open central interval by both boundary shifts `+1` and `-1` gives `p(1/2)>=2b[1-p(1/2)]`; half-line shifts give `p(r+1)>=b p(r)` for `r>0`. Integrating the tail on `[0,1/2]` and `[k-1/2,k+1/2]` yields

`E X^2 >= (2b/(1+2b)) [1/4+2b/(1-b)^2]`.

Adding the two coordinate inequalities requires no independence and gives source (13), including `V_b>=17/4` for `1/2<=b<1`.

For `C=[-1/2,1/2]^2`, the exact reviewer check gives first area increment `41/50`, moment increment `9777/5000`, and so the first excess at `V_b` is at most `-956/625`. For `b=1/2`, the feasible no-gap square law has cost `571/66`; the entire weighted area and moment increments are `61/50` and `202571/15000`. Thus the complete signed excess is `202571/15000-(61/50)V_(1/2) >= 486731/165000>0`. This is genuinely nonradial and invalidates a per-level sign argument, not the all-law comparator.

### Explicit nonparallel residual and qualified cost-ball aside

The phase-inclusion conditions do not force one fixed core even among compact convex D4-symmetric levels. For example, let `K_0={0}`, `K_1=D`, `K_2=[-2,2]^2`, and `K_i=K_2+(i-2)D` for `i>=2`. Every `K_i+D subset K_(i+1)`; the levels are convex, centrally symmetric, D4 symmetric, and have finite weighted mass and second moment for every `0<b<1`. The same translated-density argument makes their geometric phase feasible. If they were all `C+R_iD`, the singleton `K_0` forces `C={0}` and `R_0=0`, but the square `K_2` is not a diamond `R_2D`. This example does **not** assert that these levels are optimal. It isolates the missing shape-coherence or genuinely nonparallel aggregate-comparison step.

For m1, one valid conditional statement is: suppose a finite-moment optimal geometric phase has initial level `C`, nested levels `K_(i+1) superset K_i+D`, cost `lambda=V_b`, and `C+D` contains the closed Euclidean cost ball `{x:|x|^2<=lambda}`. Then its levels equal `C+iD` almost everywhere. Indeed `K_i superset C+iD`; for `i>=1`, every excess point lies outside `C+D` and has strictly positive `|x|^2-lambda`. If any excess has positive area, replacing the levels by `C+iD` produces a feasible phase with strictly negative unnormalized `Phi_lambda`, hence cost below `V_b`, a contradiction. No such cost-ball condition or optimal-phase reduction is established generally here, and this a.e. proof alone does not establish literal equality of arbitrary closed sets.

## Reviewer-owned bounded controls and assurance

Both controls were authored after complete source display, use no author code and no external packages, were run with a 120-second deadline, and finished with actual exit 0; no timeout was treated as a verdict.

1. `reviewer-exact-controls.py`: native clock before writing `2026-10-29T14:23:48-0700 PDT`; before running `2026-10-29T14:24:19-0700 PDT`; measured source SHA-256 `b73941811a1eca2519c031b33ac7c3af05e69d456efa259ee7238ecb78433e14`; actual exit `0`. It independently reconstructed all four endpoint polynomials using exact rationals and factorial/Stirling moments, confirmed the term counts and strictness witnesses in the table, the square rational values, and the nonconvex midpoint. **Intended-reason negatives:** deliberately corrupting the tail constant was rejected at exponent `(0,0,0,0)` with coefficient `-1`; replacing the valid lower bound `17/4` by the insufficient bound `2` was rejected because the supposed first-shell upper bound became `1577/5000>0`.
2. `reviewer-boundary-control.py`: native clock before writing `2026-10-29T14:25:08-0700 PDT`; before running `2026-10-29T14:25:15-0700 PDT`; measured source SHA-256 `417d14913328b77db6cc7851efd51cde557cfc5d0d90bd3bbb719f528e0ba1c2`; actual exit `0`. For a square and `h=(1,0)` exactly on the closed boundary, a positive-area rectangle has unnormalized masses `1/50` and `1/100`, saturating privacy at `b=1/2`. The **intended-reason negative** uses invalid spacing `R_1=1/2` and finds translated mass `1/200`, giving the strict failure `1/50 > (1/200)/(1/2)`. This negative is a positive-area privacy violation, not a pointwise-only artifact.

These bounded controls supplement the written reasoning; they are not formal/kernel verification, a human review, an independent-model-family review, a novelty check, or a scientific certificate replay. The full SHA-256 of this review is supplied externally with the delivery because embedding a file's own full hash in its bytes would be self-referential.
