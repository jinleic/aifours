# f256 hostile review: optimizer complementarity and finite-profile reduction

**Disposition:** 0 FATAL, 0 MAJOR, **2 MINOR**, 0 INCONCLUSIVE for the scoped written claims, after the binding owner erratum and parent convention. The two minor findings are literal inaccuracies in intermediate geometric wording; neither invalidates the reconstructed theorems. This is same-harness written mathematical review, **not** human, independent-model-family, formal/kernel, novelty, publication, or source-equivalence verification. The finite-profile minimum is not a general-ε value formula. The optional f245 use has exactly the limited scope described below.

Native clock observed before composing: `2026-10-29T15:24:22-0700 PDT`; this is not a file-creation time.

## Frozen inputs and actual coverage

Manifest `manifest-v1.json`: SHA-256 `0562588cc99dac936ba4aca6eaaa7844cbcd5a8eaba8ac7212b68c408967a638`, checked against the supplied full hash before opening it. All four declared input hashes, byte counts and LF counts were checked **before** any declared source body was displayed. The first combined metadata command also passed an accidental nonexistent fifth pathname to `wc` and exited 1; a corrected four-input `wc` command exited 0 and confirmed all four counts. The four hash outputs in the initial command all matched their manifest values.

The complete source bodies were displayed in this exact order, in raw windows of at most 15 lines, including their endings:

1. Owner Steiner erratum: SHA-256 `6b8af7b2d672b470290f3673b5f799ac4ca8b5e015276f287bcdbe1a23a52e27`, 4,541 bytes, 48 LF; lines 1–48.
2. Parent prospective clarification: SHA-256 `3abe7a865335863704f5720f70af3abba39d8ad2d74c41db8df9791020986d6b`, 1,522 bytes, 17 LF; lines 1–17.
3. Adopted f245 disposition: SHA-256 `a5005ac8173be0b0c05bb5eb3cb82678ac22b1ae90de2c4d4a418f301d98a711`, 3,662 bytes, 24 LF; lines 1–24; used only for the optional comparison example.
4. Candidate: SHA-256 `4263cf17acd50a6e1167d7c8b62560cd7c634c2d8711a808de70733cac659b43`, 22,545 bytes, 274 LF; lines 1–274.

No mathematics was done before the full ordered read. The earlier f250 review, author control outputs/code as evidence, linked source bodies, f161/f162, held or withdrawn bodies, and the unadopted f238 aside were not used. No computational control, solver, external model/API, Git operation, or deletion was run. In particular the appendix was included in the required complete display, but its claimed PASS results and author code were neither executed nor relied upon.

## Findings with counterexamples

### m1 — two-sided boundary fibers, candidate LF 92

The literal assertion that away from countably many jumps the boundary of the double-axis down-set has **at most one** point per vertical fiber is false on the full plane. Take the centered square `[-1,1]^2`: at every `x∈(-1,1)`, including `x=1/2` where the section-height function is continuous, the vertical boundary fiber contains both `(x,1)` and `(x,-1)`.

The intended null-boundary conclusion is nevertheless valid: there is at most one such boundary point in each open upper/lower half-plane, hence at most two on the full vertical line, away from the countable jumps, with the axes handled separately. Fubini then gives two-dimensional boundary measure zero. The essential-support step can use this corrected statement without changing the theorem.

### m2 — uniqueness of a Steiner section with infinite length, candidate LF 81

The unqualified statement that the centered interval **uniquely** minimizes the `w²` integral among sections of a fixed length is false when that length is infinite. The sections `[0,∞)` and `R` both have infinite one-dimensional length and integral `+∞`, but differ by the positive-infinite-measure set `(-∞,0)`. The unique-up-to-null-sets statement needs finite section length (and the finite-moment equality argument uses almost-everywhere finite sections).

This does not invalidate the optimizer argument. Each phase level `E_i` is in fact bounded: `E_i+D⊆E_(i+1)` and `|E_(i+1)|<∞`; otherwise one could choose infinitely many widely separated points of `E_i`, whose disjoint positive-area translates of a small ball inside `D` give infinite area in `E_(i+1)`. More generally Fubini is enough to restrict the planar equality argument to finite-length fibers almost everywhere. The erratum's whole-line convention remains correct for the **literal inclusion** with an infinite section; it does not supply an infinite-length uniqueness claim.

## Per-claim reconstruction and theorem dependencies

Each row below is **0 F / 0 M / 0 m and not INCONCLUSIVE** except where explicitly linked to m1 or m2. Standard real-analysis theorems used are named rather than treated as self-contained source proofs. None is the f238 optimizer aside or a circular optimizer premise.

### 1. Attainment, full closed-D privacy, and representative — clear

The product density `(ε²/4) exp(-ε||x||_1)` has cost `4/ε²`; the triangle inequality gives the full closed-diamond shift inequality, including `||h||_1=1`. A minimizing sequence with uniformly bounded second moment is tight. **External standard theorem used:** Prokhorov's theorem supplies a weakly convergent probability subsequence. For an arbitrary fixed `h∈D`, translation is weakly continuous, and integrating against every nonnegative bounded continuous test function passes the measure domination to the limit. Borel regularity/closed-set approximation then extends it to every Borel set. Since `h` was arbitrary and the same subsequence is used, there is no exceptional set of shifts. The cost is lower semicontinuous by bounded continuous truncations and monotone convergence. The attained value is positive because only `δ_0` has zero cost and `δ_0` violates a nonzero permitted shift.

Integrating privacy over the area-two diamond and applying Tonelli yields `2b μ(A)≤∫_D μ(A+h)dh≤|A|`. Thus `μ` has a density bounded almost everywhere by `1/(2b)`. **External standard theorem used:** Lebesgue differentiation for Euclidean balls makes the rational-radius limsup `f` a Borel version of this density, bounded everywhere. Comparing each pair of shifted balls before taking limsup gives `f(x+h)≥b f(x)` simultaneously for every `x` and every `h∈D`. Positivity at one point follows from total mass one; finitely many diamond steps then make it positive everywhere. No unadopted optimizer reduction is used.

### 2. Geometric phase identity, normalization, and optimality — clear

For `a∈(bM,M)`, the strict superlevel sets obey `E_i+D⊆E_(i+1)` even at boundary shifts. Their union is all of `R²` because `f>0`, and `n_a` is finite. An `f(x)>a` point has a small ball with average `>a`, so `E_0` has positive area; this does not assume the point itself is a Lebesgue point.

For an independent phase calculation, write `f(x)=M b^(k+θ)` with integer `k≥0` and `0≤θ<1`, and write `a=M b^σ`, `0<σ<1`. Up to the single irrelevant endpoint `σ=θ`, `n_a=k+1` for `σ<θ` and `n_a=k` for `σ>θ`. Changing variables in the two integrals gives

`M b^k [b(1-b^θ)+(b^θ-b)] = (1-b) f(x)`.

Consequently `∫u_a da=(1-b)f` pointwise. Tonelli gives `∫Z_a da=1-b` and the analogous moment identity. The phase density `u_a/Z_a` is full-D private wherever `Z_a` is finite; it has positive mass and, for almost every phase, finite mass and moment. The measure-valued mixture weights `Z_a/(1-b)` integrate to one. Every phase cost is at least `V`; hence the average equals `V` only if almost every positively weighted phase has cost exactly `V`. Absolute convergence of the signed level sum follows from the separate finite positive mass and moment sums. This proves per-phase optimality rather than assuming it.

### 3. Literal Steiner inclusion and individual equality cases — m2 only

For a fixed direction, let the `D` section at transverse coordinate `q` be `[-δ(q),δ(q)]`. With the binding convention: zero-length `A` sections become empty, positive finite sections become closed centered intervals, and infinite sections become the entire line. If `A+D⊆B`, inner compact approximation in one dimension gives `ℓ_B(p+q)≥ℓ_A(p)+2δ(q)` for positive finite `ℓ_A(p)`; the `δ(q)=0` case is ordinary containment, with no false positive growth. Thus the sum of the two **closed** centered intervals lies in the centered `B` section, including endpoints. Infinite `A` length forces infinite `B` length; zero `A` length creates no source point. This works for every transverse coordinate, not merely almost every coordinate. The axis half-widths are `1-|q|`; in orthonormal diagonal coordinates the diamond is a square with half-side `1/√2`.

As a boundary check, a positive vertical section of `A` at `p=1/2` can be shifted by the diamond boundary point `(1,0)`: the target section need only have at least the same length, and closed symmetrized endpoints are still included. Conversely, the discarded zero-section-to-singleton convention fails already for `A=B=∅`: it manufactures a full transverse axis and its sum with `D` is not contained in that axis.

For a finite-length section, put `I=[-c,c]` with the same length as `A_p`. Direct subtraction of `c²` on `A_p\I` and `I\A_p` shows the `w²` moment cannot decrease below that of `I`, with equality only up to a null set. Fubini supplies the planar assertion. Each of the four symmetrizations is applied **separately** to every level; all weighted reductions are nonnegative and preserve mass, so optimality forces equality at every level in each direction. No claim is needed that a sequence of four symmetrizations preserves earlier symmetries. The general infinite-length wording has the m2 qualification above. Standard dependencies are one-dimensional Lebesgue inner regularity and Fubini/Tonelli; the inclusion and finite-fiber strictness are otherwise reconstructed here.

### 4. Essential support, symmetry, compactness, and exact inclusion — m1 only

Equality for each separate axis implies `S_y S_x E_i=E_i` almost everywhere: equal sets almost everywhere have equal section lengths almost everywhere. Horizontal centering followed by vertical centering gives a coordinate down-set; its section height is even and nonincreasing in the absolute transverse coordinate. Using the **corrected** two-sided boundary count in m1 and the standard fact that a monotone real function has at most countably many jumps, its boundary has planar measure zero. Thus this down-set and its essential support agree almost everywhere, and `K_i=supp_ess(E_i)=E_i` almost everywhere.

If a set has centered interval sections in direction `e`, contraction `(p,w)→(p,αw)` for `0<α≤1` sends it into itself. It sends a positive-measure subset of a small ball into a positive-measure subset of a ball around the contracted point (the image is an ellipse, contained in such a ball); reflection and closure handle the remaining endpoints and `α=0`. Therefore the support has each section either empty, a closed centered interval, or the whole line. Applying this independently to all four almost-everywhere equal symmetrizations gives exact axis/diagonal reflection symmetries and centered sections. Positive area and axis contractions give a neighborhood of zero.

For any point of `K_i`, first use axis reflection to put it in the first quadrant. Its anti-diagonal centered section contains the swapped point and midpoint `(s/2,s/2)`, where `s=||x||_1`; the axis sections contain the square of side `s`. Thus `s²≤|K_i|<∞`. The support is closed, hence compact. Finally, for `x∈K_i`, `h∈D`, every positive-area piece of `E_i` in a small ball around `x` shifts into `E_(i+1)` in the corresponding ball around `x+h`; consequently `K_i+D⊆K_(i+1)` **literally**, including closed-D boundary shifts. The proof does not take a Minkowski sum of arbitrary almost-everywhere representatives.

### 5. One-level deletion/addition and essential-support recurrences — clear

For deletion at `i≥1`, replace only `K_i` by `(K_(i-1)+D)∪(K_i∩B̄(0,√V))`; for `i=0` use `K_0∩B̄(0,√V)`. Previous and next inclusions remain literal, the altered chain still covers the plane, and the `i=0` level retains positive area because `0∈int K_0` and `V>0`. The modified phase need not be symmetric. If the deleted part had positive area, its integral of `|x|²−V` would be strictly positive, so the modified signed numerator `N'−VZ'` would be strictly negative. Because `Z'>0`, this contradicts global optimality even though normalization changed. Zero-area changes and the equality circle do not produce a strict contradiction. Since the candidate forced union is closed and `K_i` is its own essential support, the a.e. pruning conclusion upgrades to exact (A1); similarly `K_0⊆B̄(0,√V)`.

For addition at `i≥0`, adjoin `(K_(i+1)⊖D)∩B̄(0,r)`, with `0≤r<√V`. The erosion is compact, and each added point plus every `h∈D` is already in the next level. The preceding inclusion is preserved by enlarging the current level. A positive-area addition would make `N'−VZ'<0`; an increasing countable sequence `r↑√V` gives the a.e. low-cost erosion inclusion (A2). The boundary circle has zero area. The two perturbations therefore imply the displayed essential-support equations (8); conversely those equations recover the literal forced inclusion and a.e. erosion condition, since a measurable set differs from its support outside the support only on a null set and `K_(i-1)+D` is self-supporting. No literal claim is made for zero-area erosion components.

### 6. Finite cutoff and equality case — clear

The exact chain gives `K_(i-1)+D⊇K_0+iD⊇iD`. By `||x||_1≤√2||x||_2`, `iD` contains the **closed** Euclidean ball of radius `i/√2`. Therefore the whole cost ball is already forced for every integer `i≥ceil(√(2V))`, including equality, and (A1) gives `K_i=K_(i-1)+D` as sets. Also, a nonempty compact set plus `D` equals its own essential support: approximate any boundary translate by translates using interior points of `D`. For any finite real upper bound `U≥V`, `max(1,ceil(√(2U)))` works; the feasible product-Laplace bound gives `N=ceil(2√2/ε)`. The core can vary with phase; no same-initial-core prefix is inferred.

### 7. Profile geometry, nonconvexity, and exact B1 inclusion — clear

The axis and anti-diagonal section properties of an optimal compact `K` give (10): `F(t)=t`, `F` is nonincreasing, and `F(y)+y` is nondecreasing. Consequently `t≤F(y)≤2t−y`, and `F` is 1-Lipschitz. Conversely the defined D4 extension is a compact coordinate down-set for every finite `t≥0`; for `t=0` it is the singleton `{0}`. The admitted singleton is a feasible profile core but is **not** its own planar essential support, so it should not be confused with an optimizer's positive-area essential-support core. No optimizer-existence argument relies on the singleton being an optimizer.

For sorted nonnegative `x`, a closest point can be reflected, coordinatewise clipped, and sorted without leaving the down-set. Maximizing its coordinate sum gives `d_1(x,C)=(x_1−F(x_2))_+` for `x_2≤t`, and `x_1+x_2−2t` for `x_2>t`. Thus the radius-one sublevel has exactly the two octant boundaries in (B1), and the three inequalities in (B1) are necessary and sufficient for the literal set inclusion. For `t=0`, the first inequality concerns the singleton height `y=0` and the second traces the boundary of `D`; no open-boundary substitution is made.

The argument does not require convexity. For an explicit admissible nonconvex profile take `t=1` and

`F(y)=3/2−y` on `[0,1/4]`, `F(y)=5/4` on `[1/4,3/4]`, and `F(y)=2−y` on `[3/4,1]`.

It obeys all of (10), but `(3/2,0)` and `(5/4,1/2)` lie in the core while their midpoint `(11/8,1/4)` does not. The distance formula still gives `d_1((3/2,1/2),C)=1/4`. The arbitrary-profile strip and triangle calculation, not a convex parallel-body formula, is what establishes (13).

### 8. Moment coefficients, tail normalizer, and N=1 — clear

The original octant has area `∫(F−y)` and squared moment `∫[(F³−y³)/3+y²(F−y)]`; multiplying by eight gives `A,Q`. The parallel strip has moment increment `r(F²+y²)+r²F+r³/3`. The octant triangle above height `t` has area `r²/4` and moment `t²r²/2+tr³/3+r⁴/12`. Combining these directly yields all coefficients in (13), including `A+8t²` and `16t/3`.

For `P(G=j)=(1-b)b^j`, differentiating the geometric series gives factorial moments `E[(G)_k]=k!m^k`, where `m=b/(1-b)`; conversion to ordinary powers gives the listed `T2,T3,T4`. Thus (B2) is an **expectation** over the entire last-core tail, and the factor `b^(N−1)` in (B3), rather than `(1-b)b^(N−1)`, is correct. Prefix levels carry `(1-b)b^i`; no shell is double-counted.

At `N=1`, the prefix sums are empty. For the singleton core `t=0`, `A=Q=B=0`; the full phase has `Z=2T2>0`, moment `(2/3)T4`, and ratio `T4/(3T2)`. Here the singleton contributes no area but the subsequent closed-diamond shells do. All finite profile tuples have finite mass and moment: a finite compact last core has only polynomial parallel-volume and moment growth, while the weights are geometric. These are direct integrations/series identities; no author-run control is used.

### 9. Attained minimum and optional constraints — clear

Every tuple satisfying (10) and (B1) defines a literal full-D feasible phase; therefore `R_N≥V`. Conversely, attainment and the independently reconstructed optimal-phase/compact-level/tail arguments produce at least one tuple in this domain with ratio `V`. Hence `V=min R_N`, with attainment proved by the exhibited optimizer-derived tuple, not by an unjustified compactness claim for the profile space. All profiles remain unknown functions; this is not an elementary value formula.

For `λ=R_N`, the true optimizer-derived tuple obeys (B6), and its ratio is at most any chosen finite bound `U≥V`. Restricting to these conditions therefore preserves the attained minimum, while every remaining candidate stays feasible. The restrictions are necessary, not a sufficient global optimality certificate. No profile convexity or uniform a priori bound on the whole parameter space is assumed; finite real `t_i`, the Lipschitz bounds, and the geometric tail supply the per-tuple boundedness actually needed.

### 10. Optional f245 insufficiency example — clear at adopted scope only

The f245 disposition, and only that input, supplies two full-D phases with common square core `C=[-1/2,1/2]^2` and `J(P_K)<J(P_S)` for `b≥2/3`, plus `V>1/2`. Thus the square lies strictly inside the true cost ball, all `S_i=C+iD` transitions are forced, and `S_(i+1)⊖D=S_i`. For the latter, support functions add under Minkowski addition and a closed convex set is the intersection of its support half-spaces; this uses the standard convex separation theorem. Hence the actual-V one-level conditions and the immediate tail, and (B6) with `λ=J(P_S)>V`, do not by themselves certify global optimality. This does not refute an optimizer's eventual-tail theorem or assert an optimizer shape.

A useful boundary on that example: it does **not** automatically demonstrate insufficiency after additionally imposing the scalar `R_N≤U` with the product-Laplace `U`. At `b=2/3`, `m=2`, the square-core direct formulas give `Z=29`, moment `4301/6`, and `J(P_S)=4301/174`. Since `ln(3/2)=2 atanh(1/5)>152/375`,

`U=4/ln(3/2)^2 < 562500/23104 < 4301/174 = J(P_S)`.

Thus this particular `S` is outside that further scalar restriction. The candidate's stated insufficiency of one-level conditions/(B6) alone remains supported; the stronger restricted-domain insufficiency is neither proved nor claimed here.

## Assurance boundary

The reconstruction uses standard Prokhorov, Borel regularity/measure domination, Lebesgue differentiation, Fubini/Tonelli, one-dimensional inner regularity, countable discontinuities of monotone functions, geometric-series differentiation, and (only for the optional convex example) separation/support-function facts. These are external standard mathematical results, not independently formalized in this review. All optimizer-specific implications, finite-tail cutoff, phase weighting, and profile arguments above were reconstructed from the declared inputs rather than imported from an unadopted optimizer theorem. No general-ε optimizer value, uniqueness, novelty, human review, independent model family, or formal certification follows.
