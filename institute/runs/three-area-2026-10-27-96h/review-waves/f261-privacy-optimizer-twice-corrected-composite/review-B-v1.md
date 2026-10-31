# f261 slice B: twice-corrected optimizer, perturbations and finite tails

## Disposition and assurance boundary

**Scoped written review:** 0 FATAL / 0 MAJOR / 0 MINOR in the slice-B claims, **conditional on the exact imports below**. No unconditional disposition on the slice-A geometric/existence premises follows. The manuscript's finite-profile identity is an attained variational reduction, not a closed-form value, a global uniqueness statement, or a proof that its local conditions are sufficient. The correction's distinction between B6 alone and B6 plus the U-cap is valid. **Cap status remains UNKNOWN pending separate review**, as required by the frozen contract. A distinct exact candidate in §7 below challenges combined sufficiency; it is recorded for independent disposition, not adopted here.

Same-harness mathematical review and reviewer-written finite arithmetic controls only: **not human, independent-model-family, formal/kernel, novelty, source-equivalence or parent acceptance**. No sibling result, author control/PASS, former review body, held source, f161/f162, linked source, external model/API, Git, deletion or publication was used as a premise. The f245 disposition is used only for the optional example in §6. Its linked sources were not opened.

### Claim-by-claim severity and incompleteness

All counts refer to problems found in the stated claim, not to acceptance of imported premises. `I=no` means no unresolved point in that **conditional** claim; `I=yes` means INCONCLUSIVE at this wave's acceptance boundary.

| Claim / precise scope | F | M | m | I | Result |
|---|---:|---:|---:|:---:|---|
| Closed-D one-level deletion/addition, including positive phase mass, signed variations and zero-area circle | 0 | 0 | 0 | no | Supported subject to optimal compact-phase imports. |
| Cost-ball A1/A2 and essential-support recurrences (8) | 0 | 0 | 0 | no | Supported; raw erosion inclusion need not be literal. |
| Exact cutoff i>=ceil(sqrt(2V)) and universal N | 0 | 0 | 0 | no | Supported including the equality/boundary case. |
| Profile distance, iff inclusion B1, arbitrary-core parallel moments | 0 | 0 | 0 | no | Supported including nonconvex profiles and t=0. |
| Geometric normalization B2–B4, positivity, N=1 | 0 | 0 | 0 | no | Supported for every b in (0,1). |
| Attained B5 and restricted B5 | 0 | 0 | 0 | no | The implications follow from an imported optimizer and canonical optimal phase; those existence/geometry premises are not independently disposed here. |
| B6 and U cap as separate optimizer-necessary restrictions | 0 | 0 | 0 | no | Neither is asserted sufficient; imposing both preserves the attained minimum if the imports hold. |
| Optional f245 square demonstrates B6/local insufficiency | 0 | 0 | 0 | no | Supported using the pinned f245 premise only; the square is outside the U cap throughout its stated b-range. |
| Sufficiency/insufficiency of the **combined** B6 and U-cap restriction | 0 | 0 | 0 | yes | UNKNOWN at this review gate; §7 is a distinct candidate needing separate review, not an accepted result. No defect is assigned to the author for leaving it open. |
| All-law attainment, phase mixture, and canonical Steiner/support geometry | 0 | 0 | 0 | yes | Outside slice B; exact imports listed next. No verdict on their truth is supplied here. |

### Exact imports, not silently verified here

For the conditional deductions, import from the corrected candidate §§1–3 only: b=e^(-epsilon) in (0,1), V in (0,infinity), an attained all-law optimizer with an optimal geometric phase; that phase's positive finite mass/moment, J=V and its layer-cake identity (5); compact K_i=supp_ess(K_i), 0 in int K_0, exact K_i+D subset K_(i+1), D4 symmetry and centered axis/diagonal sections; and their representation by finite t_i and profiles (10). Product Laplace is imported as a feasible U=4/epsilon^2 upper bound. For the restricted minimization, import the existence of one such optimal phase, not compactness of the function-space search domain. The proof of all these imports is outside this slice and no A-review result is used. The finite-profile feasibility, formulas and perturbation implications are reconstructed below.

## Input integrity and actual ordered exposure

Before displaying any input body, the manifest SHA and **every** input's SHA-256, byte count, LF count, UTF-8 decoding, final LF and absence of CR were checked. All five complete bodies, including endings, were subsequently displayed in manifest order in raw consecutive windows of at most 15 lines. Both author errata preceded the unchanged candidate; no mathematics was performed before all five bodies were displayed. Paths below are relative to `/Users/jinleic/repos/aifours/`.

- Manifest `institute/runs/three-area-2026-10-27-96h/review-waves/f261-privacy-optimizer-twice-corrected-composite/manifest-v1.json`: SHA-256 `66b77dd60b4a5ca5e69004806b1bcda5731f62f26a53a79bdd23271c49f6ce5d`.
- First author erratum `information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1-addendum-1-f250-steiner-fibers.md`: `6b8af7b2d672b470290f3673b5f799ac4ca8b5e015276f287bcdbe1a23a52e27`, 4541 bytes, 48 LF.
- Second author correction `information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1-addendum-2-f256-geometry-and-cap-scope.md`: `89f91e9004c9563caf3d4cc831b1101c4e4ade8a138b006b5af7f00c1fddbb14`, 8688 bytes, 77 LF.
- Prospective parent clarification `institute/runs/three-area-2026-10-27-96h/review-waves/f250-privacy-optimizer-complementarity-and-finite-tail-reduction/parent-steiner-zero-fiber-clarification-v1.json`: `3abe7a865335863704f5720f70af3abba39d8ad2d74c41db8df9791020986d6b`, 1522 bytes, 17 LF.
- f245 scoped optional premise `institute/runs/three-area-2026-10-27-96h/dispositions/info-1-privacy-nonparallel-same-core-comparison-counterexample-parent-v1.md`: `a5005ac8173be0b0c05bb5eb3cb82678ac22b1ae90de2c4d4a418f301d98a711`, 3662 bytes, 24 LF.
- Unchanged candidate `information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1.md`: `4263cf17acd50a6e1167d7c8b62560cd7c634c2d8711a808de70733cac659b43`, 22545 bytes, 274 LF. Its owner-run code and PASS text were necessarily displayed as part of the complete body but were not used as evidence.

## 1. One-level perturbations and the exact recurrences

Put R=sqrt(V)>0 and let H_i be a replacement only for K_i. For any such full-D-feasible replacement with positive normalizer Z', layer cake gives

    Z' (J'-V) = (1-b)b^i integral (1_H_i-1_K_i)(|x|^2-V) dx.

This is an exact signed identity because the original phase has J=V. The changed compact sets are Borel, the other levels and the common tail remain unchanged, and mass/moment stay finite. The level inclusions imply the phase-index shift inequality for every h in the **closed** D. For i>=1 the deletion keeps K_(i-1)+D, so K_0 retains positive area; for i=0, K_0 intersect closed B_R contains a positive-area neighborhood of 0 because R>0. Thus the competitors are genuine probability laws after normalization; no canonical symmetry is needed of the competitors.

- Delete to H_i=(K_(i-1)+D) union (K_i intersect closed B_R), or H_0=K_0 intersect closed B_R. Both predecessor and successor inclusions are preserved. Every removed point has |x|^2>V, so positive removed area would give J'<V. The removed part is null. Since the retained bracket is closed and K_i is its own essential support, its complement cannot meet K_i: a nonempty meeting has an open ball with positive K_i-area disjoint from the bracket. Hence A1 and K_0 subset closed B_R hold **literally for these representatives**, not merely a.e.
- Add H_i=K_i union ((K_(i+1) eroded by D) intersect closed B_r), 0<r<R. The added set plus D lies in K_(i+1), and predecessor inclusion persists. Positive added area would make the integral strictly negative, since |x|^2-V<=r^2-V<0. A countable sequence r up to R proves A2. Erosion is compact, since it is the intersection of the closed translates K_(i+1)-h, h in D.
- The predecessor inclusion gives K_i subset K_(i+1) eroded by D exactly. Combining this with A1 and A2, and using that the circle |x|=R has planar area zero, gives equality a.e. between K_i and the appropriate right side of (8). Applying essential support proves the stated literal recurrences. It does **not** imply raw erosion containment at isolated or other zero-area points.

Concrete boundary cautions, not counterexamples involving an actual optimum: (a) closed B_R is the essential support of open B_R, so an a.e. open-ball statement does not by itself yield an open-ball containment for the canonical support. (b) Let E_0 be the closed Euclidean disk of radius 1/4 about 0, p=(4,0), and E_1=(E_0+D) union (p+D). The two compact components are separated. Connectedness of D and convex cancellation give E_1 eroded by D = E_0 union {p}; p lies in B_5 but not E_0. Thus the extra eroded set has zero area while raw containment fails. These sets are only a geometric demonstration, not claimed canonical optimal levels.

## 2. Closed-D cutoff

Induction gives K_(i-1)+D superset K_0+iD superset iD. The closed l1 diamond iD contains the closed Euclidean ball of radius i/sqrt(2): ||x||_1<=sqrt(2)||x||_2. Therefore if i>=ceil(sqrt(2V)), A1 sandwiches K_i exactly between K_(i-1)+D and itself. Equality at the threshold is included: e.g. (i/2,i/2) lies on the boundary of both the Euclidean ball of radius i/sqrt(2) and iD. Replacing the diamond by its open interior would lose that particular boundary inclusion. Since V<=U, N(U)=max(1,ceil(sqrt(2U))) is valid, and U=4/epsilon^2 gives N=ceil(2sqrt(2)/epsilon)>=1. No conclusion about earlier nonparallel transitions is inferred.

## 3. Profile feasibility, distance and moments

For a finite profile (10), the D4-extension C is compact and coordinatewise downward closed. In the octant x>=y>=0, closest points may be clamped coordinatewise and sorted. For y<=t, maximizing k_1+k_2 uses the monotonicity of F(y)+y, giving d_1((x,y),C)=(x-F(y))_+. For y>t the diagonal (t,t) maximizes k_1+k_2=2t, giving d_1=x+y-2t. The singleton t=0 is included. Hence the boundary of C+D in the octant is F(y)+1 for 0<=y<=t and 2t+1-y for t<=y<=t+1/2; it has no points beyond t+1/2. This proves all three B1 inequalities are jointly **necessary and sufficient**, including their shared endpoint and t=0. No convexity of the core is needed.

Independently, for every C of form (10), not just convex C,

    (C+D) eroded by D = C.                                                   (*)

One inclusion is automatic. For a point outside C, sort its absolute coordinates x>=y>=0 and shift by the signed axis unit vector in the larger coordinate. If y<=t, the shifted point has d_1=x+1-F(y)>1; if y>t, its distance is x+y+1-2t>1. Hence it is outside C+D. In particular the final i=N-1 erosion part of B6 is automatically an equality for any admissible last profile. This observation does not imply that other B6 conditions or global optimality hold.

For r>=0 the strip 0<=y<=t has boundary F(y)+r. Its octant moment increment is

    integral_0^t [r(F^2+y^2)+r^2 F+r^3/3] dy.

The extra triangle t<y<=t+r/2 contributes octant area r^2/4 and moment t^2 r^2/2+t r^3/3+r^4/12. Multiplying by 8 and using (12) yields precisely

    |C+rD|=A+8tr+2r^2,
    Q(C+rD)=Q+Br+(A+8t^2)r^2+(16/3)tr^3+(2/3)r^4.

At t=0, A=Q=B=0 and these become 2r^2 and (2/3)r^4. The independent exact polygon control also uses the genuinely nonconvex profile F(y)=3/2-y on [0,1/2], F(y)=1 on [1/2,1]; the segment joining boundary points (3/2,0) and (1,1) leaves that core.

## 4. Tail normalization, positivity and attainment

Let G have P(G=j)=(1-b)b^j and m=b/(1-b)>0. Direct shifting of the index gives E G=m, E G^2=m+2m^2, E G^3=m+6m^2+6m^3 and E G^4=m+14m^2+36m^3+24m^4. Inserting the parallel polynomials proves B2. The tail starts at level N-1, hence its correct prefactor in B3 is b^(N-1), not (1-b)b^(N-1) and not b^(N-2). The earlier N-1 levels retain the factor (1-b)b^i. All sums and moments converge by geometric decay against a fourth-degree polynomial.

Every tuple in P_N produces full-D-feasible levels; their expanding final tail covers the plane. Its normalizer is strictly positive even if the final core is {0}: Z_tail=2 E G^2>0. For N=1, singleton core explicitly gives

    Z_1=2(m+2m^2),  N_1=(2/3)(m+14m^2+36m^3+24m^4),
    R_1=(m+14m^2+36m^3+24m^4)/(3(m+2m^2)).

Thus every R_N>=V. Conversely the imported optimal phase has a prefix in P_N, and the exact cutoff makes its entire remaining tail the displayed parallel tail, so its R_N is V. This proves an **attained** min without claiming compactness of P_N. Each P_N element remains a feasible law after imposing restrictions, while this optimizer's prefix satisfies B6 with lambda=V=R_N and V<=U; hence the restricted min is also V and attained. B6 and the U cap are each necessary for this actual optimizer, not independently or jointly declared sufficient by that argument.

## 5. Explicit equality and inequality boundaries

The strict deletion argument cannot decide the sign at |x|^2=V; the circle is instead discarded by its zero area. B1 is an iff for actual inclusion, but A2 is only a zero-area exclusion. The threshold i=ceil(sqrt(2V)) is sufficient even when the Euclidean and diamond boundaries touch; no strict threshold is needed. Formula (*) is a special geometric equality for profiles, not a claim that an arbitrary raw erosion in A2 has no isolated extra points. The prefix has a finite number of functions, not a finite-dimensional scalar parametrization; no value formula or global uniqueness is inferred.

## 6. The f245 square proves B6/local insufficiency, not capped insufficiency

Here alone import the f245 disposition: for 2/3<=b<1 its nonparallel K phase is feasible and strictly cheaper than S_i=C+iD for C=[-1/2,1/2]^2, and V>1/2. The latter places C strictly inside the true V-cost ball. Every S transition is forced, and convex cancellation gives (S_(i+1) eroded by D)=S_i, so the true-V A1/A2 and the candidate-lambda B6 hold. Nevertheless S is not optimal. This shows the local conditions (even with an immediate parallel tail) and B6 **alone** are not sufficient.

The second correction's cap warning can be sharpened for this specific f245 square without importing any new source. Set m=b/(1-b)>=2 and z=2m+1>=5. Using A=1, Q=1/6, B=4/3 and the geometric moments gives

    Z_S=1+6m+4m^2=z^2+z-1,
    N_S=1/6+(23/3)m+(94/3)m^2+40m^3+16m^4,
    R_S=z^2-(z^2+5z-1)/(6(z^2+z-1)).

Since 2z^2-2z-2>0, R_S>z^2-1/2. Also epsilon=2 atanh(1/z)>(2/z)(1+1/(3z^2)); for z>=5,

    U < z^2/(1+1/(3z^2))^2 < z^2-1/2,

where the last inequality is exactly 3z^4-4z^2-1>0. Therefore **this square is outside the U-cap for the entire f245 range**, not just at b=2/3. At b=2/3, Z_S=29, N_S=4301/6, R_S=4301/174; 2 atanh(1/5)>152/375 implies U<562500/23104<R_S. This does not decide whether some different capped phase could satisfy B6 and still be suboptimal.

## 7. Distinct capped counterexample candidate: pending separate disposition

This reviewer-derived **single instance** is distinct from the f245 square. Its geometry and exact arithmetic give a counterexample to sufficiency of B6 together with the U cap, not a general result about all parameters or an additional premise of Theorems A/B. The research-gate status remains UNKNOWN pending the parent's independent disposition; this note does not adopt the result.

Take b=2/3, epsilon=ln(3/2), G geometric with m=2 and moments (1,2,10,74,730). For alpha in {1/2,3/4} use C_i=(i+alpha)D for every i. These are profiles t_i=(i+alpha)/2, F_i(y)=i+alpha-y, satisfy B1 with equality and have an exact parallel tail from the start. In particular C_i+D=C_(i+1) for the full closed D, all levels cover the plane, and the phase index n(x+h)<=n(x)+1 for each h in D. Thus the normalized phase law is feasible. For every r>=0, |rD|=2r^2 and integral_(rD)|x|^2 dx=(2/3)r^4, so the exact layer-cake normalization is

    Z(alpha)=(1-b) sum_(i>=0) b^i 2(i+alpha)^2 = 2 E(G+alpha)^2,
    N(alpha)=(1-b) sum_(i>=0) b^i (2/3)(i+alpha)^4 = (2/3) E(G+alpha)^4,
    R(alpha)=N(alpha)/Z(alpha) = E(G+alpha)^4 / [3 E(G+alpha)^2].

At alpha=1/2 these give Z=49/2, N=14305/24 and lambda=R=14305/588; K_0 has maximal squared Euclidean radius 1/4<lambda. All transitions are forced, and (*) makes every erosion B6 inclusion exact. At alpha=3/4 they give Z=217/8, N=253297/384 and the feasible competitor ratio 253297/10416. Their exact difference is 247/24304>0.

For the cap, the positive atanh series and its tail bound give

    ln(3/2) < L = 2(1/5+1/(3*5^3)+1/(5*5^5)+1/(7*5^7*(1-1/25)))
                 = 177391/437500,
    4*588*437500^2 - 14305*177391^2 = 43955767295 > 0.

Therefore the displayed arithmetic would give lambda < 4/L^2 < U. The corresponding universal cutoff is N=7: 152/375<epsilon<L, (152/375)^2>8/49, and L<5/12<sqrt(2)/3 imply 6<2sqrt(2)/epsilon<7. Thus this is a literal finite P_7 candidate, not a statement about a limit. The inequalities and fractions passed the reviewer-written exact control, but the geometric implication and research-gate status still need separate review; **no combined-cap theorem or acceptance is claimed here**.

## 8. Reviewer-written finite controls and actual execution

- `reviewer-B-exact-control-v1.py`, SHA-256 `491a9de10ba62f7f8aaf67a3c345c6e2201addf6960171c55ef46fb15ce9876b`: native clocks 2026-10-29 15:41:11 PDT before/after, monotonic 0.023656832985579967 s, actual exit 0; subprocess timeout 110 s, in-process alarm 100 s. Independent shoelace checks of a nonconvex profile, geometric moments, singleton/N=1 and N=3 normalization, square-polynomial identities and boundary checks. Intended-reason negatives rejected wrong r^4 coefficient, one missing tail b factor, zero singleton tail mass, alleged square cap membership, and an open-diamond diagonal boundary point.
- `reviewer-B-cap-example-control-v1.py`, SHA-256 `bb91a47bd0e852b1d0fe655eaebecf4962b9f711ef3251fae5b2e1357024455e`: native clocks 2026-10-29 15:43:13 PDT before/after, monotonic 0.02145291678607464 s, actual exit 0; same timeout/alarm. Exact fractions, upper log-series bound and N=7 rational comparisons; intended-reason negatives rejected reversed cost, cap and core-radius inequalities.
- `reviewer-B-control-receipts-v1.json` records actual interpreter, complete control stdout/stderr, clocks, durations, limits and exit codes. Both controls are finite arithmetic evidence, not exhaustive geometric proofs. Neither invokes author code/PASS or a model/API.
