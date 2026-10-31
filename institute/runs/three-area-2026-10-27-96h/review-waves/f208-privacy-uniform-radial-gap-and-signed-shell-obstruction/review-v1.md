# f208 independent same-harness scientific review

**Disposition: 0 FATAL / 0 MAJOR / 1 MINOR; INCONCLUSIVE items within the stated claims: none.** The one minor is the missing explicit restriction `t >= 0` in the square-core specialization. With that restriction, the fixed-core radial gap theorem, the signed-shell obstruction, the conditional minimal-shell criterion, and the ln15 trial are supported by the independent written reconstructions below. The unrestricted nonradial general-epsilon minimal-shell problem remains open; this is a scope limitation, not a proof of that problem or a finding against the conditional statement.

Native `/bin/date` observation before writing this review: **2026-10-29T13:17:39-0700 PDT**. This is an observation before writing, not an asserted creation time.

## Frozen inputs and actual sequence

First scientific artifact opened was the assigned `manifest-v1.json`. Its observed SHA-256 was `a0083fd6d865f0b155ddc137f28f2bb394d9a327347f030486441ce02d677eef`, matching the assigned prefix `a0083fd6d865`. The initial manifest display truncated its long requirements line; that line was subsequently displayed in full raw form before any input body. The SHA-256, byte count, and LF count of **every** declared input were measured and compared with the manifest before any of the four input bodies was read. All matched:

| Order | Frozen input | Observed SHA-256 | Bytes | LF | Actual complete raw windows |
|---|---|---|---:|---:|---|
| 1 | `institute/runs/three-area-2026-10-27-96h/dispositions/info-1-matching-norm-unique-optima-and-unconditional-LJ-gap-parent-v1.md` | `ce7bc24bf3af76df7cd7e32a7e4591ba9a383ff49e4705996dce3790959ce33d` | 5426 | 39 | 1–15, 16–30, 31–39 |
| 2 | `institute/runs/three-area-2026-10-27-96h/dispositions/info-1-matching-norm-parent-read-coverage-addendum-v1.json` | `e4cd453b45703ae49a2bf73de162fbb83a6d3057b0535fd5a4ee74632eebc9c6` | 1204 | 14 | 1–14 |
| 3 | `institute/runs/three-area-2026-10-27-96h/dispositions/info-1-ln64-all-law-unique-rounded-shell-optimum-parent-v1.md` | `4a7fd302c57df60e6df3221a1326452dd425d78a3a012916625399b15c1b629a` | 8786 | 54 | 1–15, 16–30, 31–45, 46–54 |
| 4 | `information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-uniform-radial-gap-and-signed-shell-obstruction-v1.md` | `52acfa0b5d9a0b883d0ca13b3fb6f77c6633f2c5440476f495c725ee35e9299f` | 19082 | 258 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, 181–195, 196–210, 211–225, 226–240, 241–255, 256–258 |

Paths above are relative to `/Users/jinleic/repos/aifours`. The four bodies were displayed in that order, including their final lines, before mathematical reconstruction or the reviewer control. The target's embedded author code was read as text only: it was not run, imported, or compiled. Neither an author-reported PASS nor a linked body is used as evidence. There was one attempted read of a mistyped, nonexistent path for target lines 121–135; it returned not found and was immediately retried with the correct path. It exposed no additional body and did not change the successful read order. General memory/skill guidance was consulted between integrity measurement and the input-body reads; it is not scientific evidence.

## Claim-by-claim verdicts

| Claim | Verdict | Scope and reason |
|---|---|---|
| Full-D privacy of diamond phases, moments, and monotonicity of the unit-spaced tail for radius at least 1 | **0F/0M/0m** | The pointwise level inclusion, diamond integrals, and independently expanded positive derivative polynomial establish the assertions. |
| Strict fixed-initial-core improvement for any nonempty finite or infinite collection of radial gaps | **0F/0M/0m** | Last-gap removal is strictly improving, including a zero-mass prefix; a fixed first-gap comparison survives dominated-convergence truncation. |
| Strict aggregate signed inequality at the true all-law value `V_b` | **0F/0M/0m** | The already-proved strict cost comparison, mass ordering, and feasibility of the comparator give the sign, without requiring each summand to be positive. |
| All-law marginal lower bound and negative first excess for every `1/2 <= b < 1` | **0F/0M/0m** | The two-sided tail argument yields `V_b >= 17/4`, and the explicit annulus then has the stated negative bound. The phase is feasible but is not claimed optimal. |
| At `b=1/2`, positive complete weighted excess and tail compensation | **0F/0M/0m** | Exact geometric sums and the feasible unit-spaced upper law yield the stated fractions and opposite signs. |
| General core criterion `V_b <= rho(C)^2` | **0F/0M/0m** | Conditional on an actual finite-moment optimal phase with the stated exact inclusions; it is not an existence or all-core theorem. |
| Square-core specialization | **0F/0M/1m** | The formula and sufficient condition are correct for `t >= 0`, which should be stated explicitly. |
| Trial at and above `epsilon=ln 15`, its unique-root threshold, and comparison with the product-Laplace cutoff | **0F/0M/0m** | Exact polynomial signs and a rational exponential-series bound establish the claimed sufficient interval, not the true threshold. |
| Claimed remaining nonradial gap | **0F/0M/0m** | Correctly kept open; neither the counterexample nor the radial comparison settles it. |

### Minor m1 — square parameter domain

The target's square condition and the displayed inradius formula do not explicitly quantify `t >= 0`. This is a natural implicit convention for `[-t,t]^2`, but it matters literally. With standard interval-set notation, `t=-2` makes that square empty, so it gives no positive inradius information: for example `C={0}` has `rho(C)^2=1/2`, while the displayed minimum of squared expressions is 1. State `t >= 0` at the first introduction of the square and throughout the geometric formula. This is a domain/wording repair; it does not affect the intended nonnegative-square results.

## Independent written reconstructions

### 1. Feasible phases, geometric moments, and tail monotonicity

Put `D={|x_1|+|x_2|<=1}` and `b=exp(-epsilon)`, and set

`u_R(x)=(1-b) sum_{i>=0} b^i 1_{R_i D}(x)`.

The level inclusions `R_i D + D subset R_{i+1} D` hold because `R_{i+1}>=R_i+1`. Every point eventually belongs to a level. If its least level is `n`, then `u_R(x)=b^n` and its least level after any shift in `D` is at most `n+1`. Thus `u_R(x+h)>=b u_R(x)` pointwise using the closed-level representative; normalization gives privacy for every Borel set and every full-closed-D shift. This also covers the singleton first level when `R_0=0`.

Direct integration over quadrants gives `|rD|=2r^2` and `int_{rD}|x|^2 dx=2r^4/3`. The fourth-moment hypothesis also gives the needed second-moment summability, since `r^2<=1+r^4`. Therefore

`Z_R=2(1-b) sum b^i R_i^2`,  `J(R)=(sum b^i R_i^4)/(3 sum b^i R_i^2)`.

The denominator is positive because `R_1>=1`. For unit spacing, let `G` be geometric on nonnegative integers with `P(G=i)=(1-b)b^i`, set `m=b/(1-b)`, and write `M_j(r)=E(r+G)^j`. Its factorial moments give

`E G=m`, `E G^2=m+2m^2`, `E G^3=m+6m^2+6m^3`, and `E G^4=m+14m^2+36m^3+24m^4`.

Consequently `Z_r=2M_2(r)` and `J_r=M_4(r)/(3M_2(r))`. The mass derivative is `Z'_r=4(r+m)>0`. Independently expanding the quotient numerator at `r=1+s` gives

`(M'_4 M_2-M_4 M'_2)/2 = (1+s)^5 + m(4+21s+34s^2+22s^3+5s^4) + m^2(5+28s+36s^2+12s^3) + m^3(2+12s+12s^2)`.

All coefficients are positive, so `J'_r>0` for all `r>=1`. Also, `M_4(r)>=r^2 M_2(r)`, hence `J_r>=r^2/3`.

### 2. Last gap, arbitrary finite gaps, and infinitely many gaps

Suppose the last gap is after index `k`, with size `delta>0`, let `a=R_k`, and let `r=a+1`. For any tail-start `z>=r`, the density is the common prefix `(1-b) sum_{j=0}^k b^j 1_{R_jD}` plus `b^(k+1) u_z`, where `u_z` is the complete unit-spaced phase beginning at `z`. The prefix mass `alpha` is nonnegative; when positive its cost `c` is at most `a^2/3`, since it is a positive mixture of uniform diamonds of radius at most `a`. Its tail mass `beta(z)` and tail cost `J_z` both strictly increase with `z`, and `J_z>=z^2/3>=r^2/3>a^2/3>=c`.

For `alpha>0`, the full cost `(alpha*c+beta*J_z)/(alpha+beta)` increases strictly with both `beta` and `J_z` in this regime. If `alpha=0`, the cost is simply `J_z`, still strictly increasing; in particular the `k=0, R_0=0` case is not lost. Replacing `z=r+delta` by `r` removes the last gap, preserves feasibility and the initial core, and strictly reduces cost. Repetition handles every finite number of gaps.

For an infinite gap set, fix the first gap after `k`. For each `n>=k+1`, retain the original levels through `n` and continue with unit spacing. The truncated radii are bounded above by the originals and converge pointwise to them. Dominated convergence of both weighted second and fourth powers yields convergence of the normalized costs, with positive limiting denominator. Removing all later gaps from a truncation gives the **same** one-gap phase determined by the first positive gap. Its cost is strictly above the no-gap cost by the previous paragraph, so every truncation is at least this fixed larger value; the limit is strictly larger too. If no gap exists, the two sequences coincide. This proves the claimed fixed-core comparison for all `b in (0,1)` and every summable sequence, not just finite examples.

For `Phi_lambda(A)=int_A(|x|^2-lambda)dx`, the phase identity is

`(1-b) sum b^i Phi_lambda(R_iD) = Z_R (J(R)-lambda)`.

Writing `g=R_0`, the radius ordering gives `Z_R>=Z_g`; the no-gap phase is feasible, so `J_g>=V_b`. Thus the difference at `lambda=V_b` is

`Z_R (J(R)-J_g) + (Z_R-Z_g)(J_g-V_b)`,

which is strictly positive when a gap exists. This proves the aggregate inequality without asserting termwise signs. All the signed series are absolutely convergent under the stated fourth-moment hypothesis.

### 3. All-law lower bound and the signed obstruction

For any feasible planar law, projection to either coordinate preserves the one-dimensional privacy inequality for all shifts of magnitude at most 1. For `p(r)=P(|X|>=r)`, the open interval `(-1/2,1/2)` has two disjoint unit translates in its complement. The privacy inequality gives

`p(1/2)>=2b(1-p(1/2))`, hence `p(1/2)>=2b/(1+2b)`.

Applying privacy separately to the positive and negative half-lines gives `p(r+1)>=b p(r)` for `r>0`. Layer cake and the lower values on `[0,1/2]` and `[k-1/2,k+1/2]` yield

`E X^2 >= p(1/2)[1/4+2 sum_{k>=1} k b^k] >= (2b/(1+2b))[1/4+2b/(1-b)^2]`.

Sum the two coordinate inequalities; no coordinate independence is used. Therefore

`V_b >= (4b/(1+2b))[1/4+2b/(1-b)^2]`.

Both positive factors are increasing on `(0,1)`, so this is at least `17/4` on `[1/2,1)`. `V_b` is finite: the normalized density proportional to `exp(-epsilon ||x||_1)` is full-D private and has finite second moment.

Now let `K_0=(1/2)D`, `K_i=(i+3/5)D` for `i>=1`, and `C_i=(i+1/2)D`. These compact diamonds are D4-symmetric and have interval sections in every direction. They satisfy the required exact level inclusions, and the corresponding phase is full-D private. For the first excess shell,

`Phi_lambda(K_1)-Phi_lambda(C_1) = 14911/15000-(31/50)lambda`.

At the actual all-law `lambda=V_b`, the lower bound gives at most `-12307/7500` for every `b>=1/2`. This is a counterexample to a termwise nonnegative assertion, not to optimal minimal shells: the exhibited gapped phase is not asserted to be optimal.

At `b=1/2`, the exact geometric sums give

`Delta H_lambda = sum_{i>=1} 2^(-i)[Phi_lambda(K_i)-Phi_lambda(C_i)] = 50517/5000-(51/50)lambda`.

The full-D-private minimal-shell law with `g=1/2` has `J=1697/204`, so `V_(1/2)<=1697/204`. Hence `Delta H_(V_(1/2))>=2023/1250>0`. The first **weighted** term is at most `-12307/15000`, forcing the subsequent weighted tail to contribute at least `36583/15000`. The negative local term and positive total are therefore mutually consistent.

### 4. Conditional nonradial sufficiency and square geometry

Let an actual optimal phase have compact initial `C` containing 0, measurable finite-moment levels `K_i`, and exact inclusions `K_i superset C+iD`. Define `rho(C)=inf{|x|:x not in C+D}`. The comparator with levels `C+iD` is feasible: the levels are closed, cover the plane, are nested, and `(C+iD)+D=C+(i+1)D`. Its mass is positive and its second moment is finite, because `C` is compact and `0 in C`.

For `i>=1`, `C+iD` contains `C+D`, so every excess point is outside `C+D` and has squared distance at least `rho(C)^2`. If `V_b<=rho(C)^2`, every excess contribution to the signed functional is nonnegative. The equality case can only occur on the circle `|x|^2=V_b`, which has planar Lebesgue measure zero. Optimality makes the original signed phase functional zero, while feasibility of the comparator makes its signed functional nonnegative. Thus their nonnegative difference is zero and each countably many excess sets has zero area: `K_i=C+iD` a.e. This conclusion is conditional on an actual optimal phase and on the inradius bound; it does not show either for arbitrary cores at general epsilon.

For `t>=0` and `C superset [-t,t]^2`, the square-plus-diamond set is the octagon

`|x_1|<=1+t`, `|x_2|<=1+t`, `|x_1|+|x_2|<=1+2t`.

Its closest axial and diagonal boundary distances are respectively `1+t` and `(1+2t)/sqrt(2)`, and both closest points occur on the corresponding boundary. Hence

`rho(C)^2 >= min{(1+t)^2,(1+2t)^2/2}`.

This proves the stated sufficient condition with the `t>=0` clarification in m1. For `t>0` the right-hand side is strictly larger than `1/2`, but the packet does not establish that an actual optimal core/value pair realizes that extra range.

### 5. The explicit ln15 extension

For the feasible unit-spaced phase with `g=1/2`, substitution into its exact moments gives

`M_4(g)-(3/2)M_2(g) = 24m^4+48m^3+26m^2+2m-5/16 = Delta(m)`.

Since `M_2(g)>0`, its cost is below `1/2` exactly when `Delta(m)<0`. The polynomial is strictly increasing for `m>=0`, starts negative, and tends to positive infinity; its unique positive root `m_0` satisfies

`Delta(1/14)=-725/38416<0`, `Delta(1/13)=8171/456976>0`.

Because `m=1/(exp(epsilon)-1)`, the trial is below `1/2` for `epsilon>log((1+m_0)/m_0)`, whose threshold lies strictly between `ln 14` and `ln 15`. In particular, at `epsilon=ln 15` the feasible cost is `22501/46452 = 1/2-725/46452`; all larger epsilon are also covered. This is a sufficient trial threshold only.

For comparison, the product-Laplace law proportional to `exp(-epsilon ||x||_1)` has cost `4/epsilon^2`, hence gives `V_b<1/2` only under the elementary sufficient condition `epsilon>2sqrt(2)`. The rational partial exponential series through degree five at `14/5` is `720653/46875>15`, and `(14/5)^2<8`; therefore `ln 15<14/5<2sqrt(2)`. The new trial indeed supplies a nonempty extension of that elementary regime, without asserting the true boundary of `V_b<1/2`.

## Independent exact control and receipts

The reviewer wrote and ran only `reviewer-exact-control-v1.py` inside this wave directory. It constructs geometric moments independently from the Stirling-number recurrence and factorial moments, uses rational arithmetic throughout, and does not import the author cell. Script SHA-256: **`0b966d0975adf3f445d4e29c340ef5ad5edda34a874999f182136cf3f6ba7211`**. Native `/bin/date` observation before writing the control: `2026-10-29T13:15:39-0700 PDT`. Execution: `/usr/bin/python3` on that file, with a 120-second subprocess cap; start `2026-10-29T13:16:37-0700 PDT`, end `2026-10-29T13:16:37-0700 PDT`, **exit 0**, empty stderr. No timeout occurred.

Observed checks: the complete derivative polynomial identity and its positive coefficients; `L=17/4`, `U=1697/204`, first signed excess at `L` equal to `-12307/7500`, total at `U` equal to `2023/1250`, and tail lower bound `36583/15000`; strict finite two-gap ordering; and an exact infinite-gap example with `R_i=i+(1/5)(1-2^(-i))`, whose costs are `38278720909/4468708125 > 1607681/192300 > 25/3` for infinite gaps, its fixed first gap, and no gap. The trial and exponential fractions in §5 were also reproduced; at `t=1/2` the square support endpoint squares were `9/4` and `2`.

Eight intended-reason negatives were rejected: a perturbed derivative coefficient; a nonnegative assertion for the negative first annulus; a nonpositive assertion for the positive full excess; omission of the diamond-area factor 2; reversed last-gap ordering; failure of strict improvement with a zero-area prefix; incorrectly including `m=1/13` in the trial's negative region; and taking the larger rather than smaller square-support endpoint. The finite examples and rational controls are checks, not substitutes for the universal written arguments above.

## Imports, remaining gap, and deviations

Explicit classical imports: elementary Lebesgue integration and null circles; Tonelli/layer cake and dominated convergence for the nonnegative/summable series; basic geometric-series and factorial-moment identities; elementary calculus, Euclidean/convex polygon geometry, and the positive exponential series. The general `V_b` is defined over the original all-Borel/full-D class; no LAW642, f161/f162, held body, linked source body, author code execution, solver status, web result, sibling review, or author consultation is a premise. The two adopted dispositions and coverage addendum were read at their stated scope; no general-epsilon all-law optimizer, radial-to-nonradial lift, or optimizer phase decomposition was imported from them.

**Remaining mathematical gap:** no proof here that every unrestricted nonradial optimizer has a core satisfying the inradius criterion, or that signed excess shells are globally controlled without it. There is no novelty or source-equivalence conclusion.

**Contract deviations:** none substantive. The failed nonexistent-path read and the non-scientific guidance reads are disclosed in the sequence above; all declared inputs were successfully displayed in manifest order before reconstruction. No input was modified. The control is bounded and its negative checks are identified by intended reason.

This same-harness review is **not** human review, independent-model-family review, formal/kernel verification, or novelty verification.
