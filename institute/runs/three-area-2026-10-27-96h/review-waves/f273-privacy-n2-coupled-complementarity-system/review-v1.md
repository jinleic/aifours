# f273 written review: N=2 coupled complementarity

## Verdict and scope

**RETURN FOR ADDITIVE CORRECTION: 0 FATAL / 1 MAJOR / 4 MINOR mathematical findings.** The functional, independent-root obstruction and active pooled identity are supported. The late erratum supplies the correct fixed-height minimization rule. An implicit, attained two-scalar *variational* reduction can be reconstructed from that rule and f261, as below. The asserted complete characterization by the two zero-derivative equations (P3) is not supported: the feasible scalar boundary requires normal-cone conditions, not two unrestricted stationarity equations. Neither version solves those scalar equations or the original small-epsilon problem.

Native clocks actually observed: **2026-10-29T19:56:56-0700 PDT** before initial review composition; **2026-10-29T19:58:01-0700 PDT** before binding the late input; **2026-10-29T20:01:20-0700 PDT** before composing this revised review. These are observations, not inferred creation/read-completion times.

This review distinguishes the original frozen target, the subsequently authorized slack erratum, and reviewer-owned written reconstruction. No favorable author diagnostic is used as mathematical evidence.

## Input and exposure chronology

1. The manifest was opened first (LF 1–15), its SHA-256/6037-byte/79-LF binding checked, and its remaining LF displayed completely. All **nine original input** hashes, bytes and LF counts were then checked together and matched before opening input S1. Every original input was displayed completely in manifest order using raw windows of at most 15 lines, including its ending. Mathematical consideration began only after S9 LF 105.
2. When Main's additive-input notice arrived, all original inputs had been read and written mathematical reasoning had begun, including the fixed-box and scalar-boundary analysis; no review file or verdict had been issued. The notice therefore did **not** precede the original target exposure.
3. The late slack erratum S10 was hash-checked before opening it. Its SHA matches the notice, but its measured size is **3471 bytes / 29 LF**, not the notice's 33 LF. It was read completely in raw windows 1–15 and 16–30 (actual ending at LF 29), then 16–29 was displayed again. The target S9 was subsequently reread completely in seven 15-line raw windows, *after* S10. This is an authorized additive composite read, not a claim that S10 belonged to the initial freeze or was seen before the first target read.
4. The author's second new manuscript was not opened. No linked mathematical body, held/withdrawn/ZERO/protected body, sibling review, author program, external source or external model was opened/executed. No reviewer computational control was run; consequently there is no control script or control receipt.
5. Administrative scope disclosure: mandatory higher-level guidance was also read at `memory://root/memory_summary.md`, `skill://aifours-written-math-acceptance-protocol`, and `skill://independent-snapshot-review`. These were not scientific inputs or premises. Thus I do not claim literal compliance with a reading restriction interpreted to forbid even mandatory non-packet administrative guidance. This disclosure is made now, not backdated to before those reads.

## LF-located findings

### M1 — Replace unrestricted (P3) stationarity by boundary-aware conditions

**MAJOR.** S9 LF **82–88**, carried forward by S10 LF **27**. At the admitted corner `t1=t0+1/2`, the two scalar parameters cannot vary independently in both directions. Even for a differentiable reduced signed functional h(a,c;V), with a=t0>0 and c=t1, the correct first-order condition there is `(h_a,h_c)=(-kappa,kappa)` for some kappa>=0; equivalently `h_a+h_c=0` and `h_c>=0`. Both partials need not vanish. At regime kinks directional/normal-cone conditions are needed as well. S9 LF 95 expressly leaves this boundary untreated, and S10 merely says the envelope equations must be rederived. Thus selecting solutions only by the two displayed equalities is not an established necessary-and-complete optimizer system. Supply the boundary/directional envelope analysis, or state only the implicit variational reduction proved below; do not call the existing P3 equations an exact complete characterization.

### m1 — Identify what the slack example actually contradicts

**MINOR.** S10 LF **14**, compared with S9 LF **71–73**. The literal displayed P2 uses `R1`, not `R1+1`. On the erratum's stated boxes and roots it already returns `min(7/5,max(7/10,6/5,13/10))=13/10`; the erratum instead substitutes 23/10 and attributes that different expression to P2. The example contradicts the original *prose/summary* describing a universally shifted root, not that displayed P2 formula. Moreover R0=2 at y=0 fixes lambda=4, outside the actual-cutoff-two standing range lambda=V<=2. It is a legitimate synthetic fixed-box example, not an actual N=2 optimizer counterexample. Correct the attribution and retain the separately justified general correction of P1.

### m2 — Make active-interval nonemptiness a one-way implication

**MINOR.** S10 LF **23**. The active interval is nonempty whenever the independent-projection feasibility test fails, but not *exactly when* it fails. For any a>0, a+1/2<c<a+1 and 0<=y<a, its endpoints reduce to `[a,2a-y]`, a nonempty interval independently of lambda. For sufficiently large lambda both independent projections are at their upper endpoints, whose difference is `2(c-a)>1`, so the test passes strictly. The two-line algorithm remains correct because it tests the projections first; replace the erroneous biconditional by the needed implication.

### m3 — Preserve strict uniqueness in the fixed-box minimization

**MINOR.** S10 LF **23**. The statement allowing failure of profile uniqueness at isolated pooled-stationarity coincidences is false for fixed `(a,c,lambda)`. The C0 integrand is strictly convex in x>=0 (its derivative is proportional to x squared), and the C1 integrand has positive second derivative proportional to z+m>0. Their positively weighted sum is strictly convex on the convex feasible polygon. The minimizing pair is unique, including branch transitions. Integration gives uniqueness a.e. of the fixed-parameter profiles, and continuity removes version ambiguity. Possible multiplicity across *different scalar parameter pairs* is a separate question. Delete the claimed fixed-profile nonuniqueness exception.

### m4 — Avoid double-counting the initial diamond core in the f238 substitution

**MINOR.** S8 LF **25**. Substituting both `C=g0 D` and `R0=g0` into levels `C+Ri D` makes the first level `2g0 D`, not the specified `g0 D` when g0>0. Use `C={0}, R0=g0, R1=g1, Ri=g1+i-1` for i>=2, or use `C=g0 D, R0=0, R1=g1-g0` with the correspondingly shifted later radii. This is a repairable theorem-instantiation error; it does not invalidate the corrected subclass conclusion.

## Per-obligation dispositions and written reconstruction

### 1. N=2 functional and actual coupling — SUPPORTED, conditional on f261

S9 LF 15–28 is exactly the N=2 specialization of S4 LF 174–204, with the representative conventions of S1–S3 and adoption boundary of S5. The two inequalities and diagonal bound in CPL are precisely B1, not independent choices of cores. The phase levels are C0, then C1+jD for j>=0. Reindexing `(1-b) sum_i b^i` gives `(1-b)A0+b E|C1+GD|`, and the same expression for the moment. There is no additional `(1-b)` on this tail.

Write A=A1, Q=Q1, B=B1, t=t1. The adopted tail is

`Ztail=A+8tm+2T2`,

`Ntail=Q+mB+(A+8t^2)T2+(16/3)tT3+(2/3)T4`.

Substituting the profile integrals gives S9 LF 28: the term `A T2=8 T2 integral(F1-y)` contributes `-4t^2 T2`, leaving the displayed `+4t^2 T2` after adding `8t^2 T2`. The Q integrand is `F1^3/3+y^2 F1-4y^3/3`. Hence the apparent coefficient change is correct. The explicit formula after “precisely” in LF 26 is the Q0 definition used here. Positivity follows already from `Z>=2bT2>0`.

### 2. Independent roots — SUPPORTED at the stated free-free scope

S9 LF 32–42: after removing positive weights 8(1-b), 8b, the derivatives are

`d0=x^2+y^2-lambda`,

`d1=(z+m)^2+v+y^2-lambda`.

Because m,v>0, wherever the real unconstrained roots are relevant, R1<R0. Thus `(R0,R1)` cannot satisfy `z>=x+1`. This excludes a slack optimum with both coordinates interior to their boxes; it does not exclude slack optima on box faces. The corrected erratum properly introduces those faces.

### 3. Pooled identity and one-sided conditions — SUPPORTED on the active feasible branch

S9 LF 46–58. For z=S+1, the weighted derivative divided by 8 simplifies identically to

`(1-b)d0(S)+b d1(S+1)=(S+m)^2+v+y^2-lambda`.

Here `b(1+m)=m` and `m^2+v=T2`. Therefore its feasible interior zero is `S=-m+sqrt(lambda-v-y^2)`. With w the square root, the two block derivatives become `-m(1+2w)` and `1+2w`. Their weighted sum is exactly `(1+2w)(b-(1-b)m)=0`.

Raising z alone has nonnegative directional cost. Lowering x alone also has nonnegative directional cost, since the negative x derivative is multiplied by a negative displacement. The active-line objective has second derivative `16(S+m)>0` on the nonnegative feasible interval. A real root outside that interval must be projected to its endpoints; a nonexistent nonnegative root does not supply a free stationary point. The written identity needs no spot-check evidence.

### 4. Original and corrected clips, regularity, floors and corners — MIXED; corrected rule SUPPORTED

The original derivation does not justify its uniform projection argument over all scalar parameter pairs. In particular, if c>=2a+1, CPL is redundant for the entire C0 box. Its optimum is the projection of its *own* root R0, which can differ from the R1 projection. Original displayed P2 is nevertheless the correct conditional minimization of the C1 block **given F0**: its unshifted root is R1; a shift of one is produced only by an active floor. S10's rule is the correct uniform replacement.

For a fixed shared height put A=2a-y, B=2c-y, p=proj(R0,[a,A]), q=proj(R1,[c,B]). If q>=p+1, the unique product-box minimizer is feasible and is the joint minimizer; equality here is binding, not strictly slack. Otherwise any joint minimizer must bind z=x+1: a slack minimizer would separately minimize both box objectives and reproduce the infeasible pair (p,q). The active interval is

`I=[max(a,c-1),min(A,B-1)]=[max(a,c-1),A]`,

since `B-1>=A`. Failure of the feasibility test implies `c-1<p<=A`, so I is nonempty. The pooled derivative above gives exactly the projection of R1 onto I. This proves S10 LF 18–21, with m2's one-way correction.

For regularity, the same minimizer has the useful equivalent expression

`x(y)=proj_[a,2a-y]( max(R1(y), min(R0(y),c-1)) )`,

`z(y)=proj_[max(c,x(y)+1),2c-y](R1(y))`.

The expressions are continuous and piecewise smooth. Wherever an unsaturated R0 branch is selected, x=R0>=a>=y, so its slope is `-y/R0` in [-1,0]. For an R1 branch, `R1+m>=a+m>=y`, giving the same slope bound. Constant and upper-box branches have slopes 0 and -1. Thus x is nonincreasing and 1-Lipschitz, with x(a)=a.

Extend the C1 floor by `x+1` through y=a, then `2a+1-y` through y=a+1/2, then no extra floor. The first junction agrees at a+1; at the second junction that floor is a+1/2<=c, so the effective floor after taking max with c has no jump. Both pieces lie below `2c-y` because c>=a+1/2. Clipping R1 above this effective floor is again continuous, nonincreasing and 1-Lipschitz: on a free root branch z>=c>=y bounds its slope by one. At y=c both box endpoints equal c. Consequently the resulting profiles are canonical and satisfy every part of CPL, including c=a+1/2, a=0, branch coincidences, and c>=a+1. This is a reviewer reconstruction, not a proof already written in S9/S10.

There is also an important distinction for **actual** optimizers in this packet's standing range. f261 gives a>0 and the pruning inclusion `C1 subset (C0+D) union Bbar(sqrt(V))`. If c>a+1/2, its diagonal endpoint is outside C0+D, so `2c^2<=V<=2`, whence c<=1<a+1. If c=a+1/2, c<a+1 directly. Thus actual N=2 optimizers satisfy c<a+1; the large-c lower-box-slack branches belong to the unrestricted fixed-parameter minimization, not automatically to actual optimizers. In this restricted actual domain the original P1 can be recovered from the corrected rule. This does not repair the universally shifted-root prose or P3.

### 5. Exact reduction, attainment and envelope equations — distinguish three claims

**Source proof status: SKETCHED, not a complete P3 theorem.** S9 LF 92–95 expressly leaves consistency, attainment and boundary treatment open; S10 LF 27 does not prove those matters merely by noting explicit dependence on `(a,c,lambda,y)`.

**Corrected implicit variational reduction: SUPPORTED by the following reconstruction.** Fix a>=0, c>=a+1/2 and b in (0,1). Let h(a,c;lambda) be H_lambda evaluated on the corrected profiles. The preceding pointwise optimality and canonical-feasibility proof show that this is the minimum of H_lambda over all admissible profiles at those fixed scalar parameters. It is continuous in lambda by the explicit continuous clipping formulas and bounded-domain integration. Moreover, for lambda2>lambda1,

`h(lambda2)<=h(lambda1)-(lambda2-lambda1) 2bT2`.

This follows by inserting the lambda1 minimizer into H_lambda2 and using the uniform positive lower bound for Z. Also h(0)>0, while h(lambda) tends to minus infinity: compare against any fixed feasible profile pair of finite N and positive Z. Hence there is a unique zero rho(a,c). At that zero every profile has `N-rho Z>=0`, and the corrected profiles attain equality. Thus rho is the attained minimum ratio at fixed (a,c); lambda is eliminated by a unique scalar value equation, not treated as an arbitrary third free parameter.

Under the **actual-cutoff-two hypothesis**, f261 supplies an optimal phase with exactly two prefix profiles and a tail from C1. At its scalar pair, rho<=V, whereas every such feasible phase has cost>=V. Therefore

`V=min_{a>=0, c>=a+1/2} rho(a,c)`,

and the minimum is attained by that f261 pair. This argument does not assume compactness of the unbounded scalar search domain and does not claim uniqueness of the scalar pair. It supplies the missing attainment argument at the implicit variational level.

**Explicit envelope characterization: INCONCLUSIVE / NOT ACCEPTED as written.** Neither source derives all parameter derivatives, their changing floor/box regimes, or the corner normal cone. The constrained minimum above must not be replaced by the unqualified two equalities in P3. M1 remains even after the variational reconstruction.

### 6. Diamond–diamond note and corrected equality — SUPPORTED as a corollary, with m4 repaired

S7 was read completely before S8. S9 LF 7 correctly labels the note a corollary of the adopted f238 gap-removal result, not a new frontier theorem. The primary f238 body is not a declared input and was not opened; its adoption is not independently re-audited here. Its stated application requires m4's corrected core/radius substitution.

The corrected equality and subclass value can also be checked directly from the declared formulas. Let `j(g)=M4(g)/(3M2(g))`. Its derivative has the sign of

`P_m(g)=g^5+5mg^4+2m(1+6m)g^3+2m(6m^2-1)g^2-m(1+2m)(1+6m)g+m^2(1+2m)`.

In fact `j'=2P_m/(3M2^2)`. The nonzero coefficient signs have two changes, regardless of the sign of the quadratic coefficient. Descartes therefore allows at most two positive roots, counting multiplicity. Also `P_m(0)>0`, `P_m(1)=(1+m)^2(1+2m)>0`, and `M_k(1)=M_k(0)/b` for k=2,4, so j(0)=j(1). The derivative must be negative somewhere between its positive endpoint neighborhoods. Hence there are exactly two simple roots in (0,1), with signs +,-,+ and no further positive roots. The larger root g* is the unique global minimizer on g>=0; j is strictly increasing for g>=1. Endpoint law-identification is not periodicity.

For fixed g0, write the diamond-pair value as the weighted average of `j0=g0^2/3` and `j(g1)` with weights `W0=(1-b)g0^2`, `W1=bM2(g1)`. For g1>=g0+1>=1, `j(g1)>j0`, W1'>0 and j'(g1)>0. Differentiating this average gives

`J'=W1/(W0+W1) j'(g1) + W0 W1'/(W0+W1)^2 (j(g1)-j0)>0`.

This remains strict when g0=0, since its first term remains positive. Thus the minimum at fixed g0 occurs exactly at g1=g0+1, where the level sequences agree with the one-core law. The unique subclass-minimizing pair is **(g*,g*+1)**, with no “mod 1” qualification. No author grid or selected numerical instance is needed.

### 7. Standing and exclusion of the small-epsilon problem — SUPPORTED with the full condition retained

S9 LF 9–11 and 92–105 leave the actual-cutoff-two hypothesis open and claim no value for 0<epsilon<epsilon0. S6 LF 17 and 38–44 support the stated conditional N1 boundary for epsilon>=epsilon0: V<=1/2, so a genuine actual-cutoff-two optimizer is absent there. The N=2 *competitor class* still exists; “vacuous” is read as referring to that standing optimizer hypothesis, not infeasibility of two-core competitors.

Throughout this review the standing condition is the full **1/2<V<=2**. The parenthetical shorthand “equivalently V>1/2” does not remove its upper bound. No existence of that regime, maximality of epsilon0, one-core failure below epsilon0, uniqueness of the scalar pair, source/book equivalence or novelty follows. Original author spot-checks, failed scripts and grids remain disclosed non-evidence.

## Coverage receipt

Path abbreviations below are exact concatenations relative to `/Users/jinleic/repos/aifours/`:

- E = `information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/`
- D = `institute/runs/three-area-2026-10-27-96h/dispositions/`
- W = `institute/runs/three-area-2026-10-27-96h/review-waves/`

Manifest: `W/f273-privacy-n2-coupled-complementarity-system/manifest-v1.json`; SHA-256 **05caa74d3bc05659ff5a0643cd3457cf45b696ffe96a92d4334d5cf42cf83164**; **6037 bytes / 79 LF**. Raw displays: **1–15, 16–30, 31–45, 46–60, 61–75, 76–79**.

| Input, in original manifest order | Full observed SHA-256 | Bytes / LF | Complete raw display windows |
|---|---|---:|---|
| S1 E/frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1-addendum-1-f250-steiner-fibers.md | 6b8af7b2d672b470290f3673b5f799ac4ca8b5e015276f287bcdbe1a23a52e27 | 4541 / 48 | 1–15, 16–30, 31–45, 46–48 |
| S2 E/frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1-addendum-2-f256-geometry-and-cap-scope.md | 89f91e9004c9563caf3d4cc831b1101c4e4ade8a138b006b5af7f00c1fddbb14 | 8688 / 77 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–77 |
| S3 W/f250-privacy-optimizer-complementarity-and-finite-tail-reduction/parent-steiner-zero-fiber-clarification-v1.json | 3abe7a865335863704f5720f70af3abba39d8ad2d74c41db8df9791020986d6b | 1522 / 17 | 1–15, 16–17 |
| S4 E/frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1.md | 4263cf17acd50a6e1167d7c8b62560cd7c634c2d8711a808de70733cac659b43 | 22545 / 274 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, 181–195, 196–210, 211–225, 226–240, 241–255, 256–270, 271–274 |
| S5 D/info-1-privacy-all-epsilon-optimizer-complementarity-finite-tail-parent-v1.md | 28335b2def1139d4141a3f62a74ef0f0063f57f2f7500d41d065466267381c97 | 8487 / 44 | 1–15, 16–30, 31–44 |
| S6 D/info-1-privacy-n1-completed-parent-read-prospective-acceptance-v1.json | 9065e9cdbaaac3925ace542b0e35a3b2ff5afb0ff11bfb9c8291d98cc90d4a3f | 7698 / 111 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–111 |
| S7 E/frontier-20261029-n2-diamond-diamond-subclass-closed-v1-addendum-1-equality-case-v1.md | a4b0938488b38010394c7479b578f497c72af9af4cefd7f098814175340f1be1 | 4203 / 44 | 1–15, 16–30, 31–44 |
| S8 E/frontier-20261029-n2-diamond-diamond-subclass-closed-v1.md | cb46deb61119e6218f1d881d4055a438f74d91d3a00a94797de6690f0ef99814 | 5606 / 51 | 1–15, 16–30, 31–45, 46–51; focused reread 23–27 |
| S9 E/frontier-20261029-n2-coupled-complementarity-system-v1.md | d099eb4c4f0d69828e47c75ad9694b112e02ad843b13b30fd79d564ea79a50a2 | 8285 / 105 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105; focused reread 82–95; all seven complete windows repeated after S10 |
| S10 ADDITIVE: E/frontier-20261029-n2-coupled-complementarity-system-v1-addendum-1-slack-case-v1.md | 0b6e1c166f7b83479d50e8d4ad49b929af0536f6c0f2dd4933498357984f9f5d | 3471 / 29 | 1–15, 16–30 through actual LF 29; reread 16–29 |

Original nine-input aggregate observed by wc: **71575 bytes / 771 LF**, all original bindings matched. The late notice's **33-LF** description does **not** match S10's observed **29 LF**; its SHA matches exactly, and the actual ending was displayed. No frozen manifest or source was edited to hide this discrepancy.

## Open items and acceptance boundary

- Correct P3 to cover scalar feasible-boundary normals and any nondifferentiable envelope regimes; derive the actual formulas before presenting them as explicit exhaustive equations.
- Resolve M1 and m1–m4 additively, preserving frozen sources and the late-arrival/read chronology.
- The corrected profile-elimination and implicit attained variational minimum reconstructed here do not solve the scalar optimization, prove scalar-pair uniqueness, or establish that 1/2<V<=2 occurs.
- Nothing here decides 0<epsilon<epsilon0, epsilon0 maximality, full all-epsilon optimizer/value formulas, novelty or source equivalence.
- Assurance is a written in-harness review with disclosed late input and administrative-read exception, not formal/kernel, human or independent-model-family certification. No external-model acceptance is claimed.
