# f280 written-mathematics review v1

## Verdict and scope

**Mathematical findings: 0 FATAL / 2 MAJOR / 1 MINOR. Correction required.** This is a reviewer finding count, not a parent adoption decision. The vertex normal cone and its stated sign reversal are wrong. The claimed exact nonsmooth equivalences also need an argument stronger than the cited generic Clarke rule; the necessary inclusion itself has a direct proof that does not require that equality. The displayed master formula has an incorrect universal integration range.

Scope: the complete 59-LF manuscript, followed by the two named adopted dispositions, in the manifest order. The f273 corrected fixed-box rule and attained variational reduction are conditional imports, not reopened criticisms of the old f273 P3. No assertion about the actual nonemptiness certified by the unlisted f278 packet is verified here. All statements about the privacy optimum retain the actual-cutoff-two hypothesis, including both inequalities 1/2<V<=2.

## Findings

### M1 — Use the correct vertex normal cone and nonnegative h_c

**MAJOR; manuscript LF 39–43; confidence 1.00.** LF 39 states `N_K={ (−x−z, x): x,z>=0 }`, LF 41 states `h_c <= 0   and   h_a + h_c >= 0.`, and LF 43 calls this a `SIGN REVERSAL relative to (G2)`. For K={a>=0,c>=a+1/2}, the active outward normals at (0,1/2) are (-1,0) and (1,-1), not (-1,0) and (-1,1). Thus N_K={(x-z,-x):x,z>=0}, and 0 in grad h+N_K gives **h_c>=0 and h_a+h_c>=0**. The feasible ray (0,1) alone already forces h_c>=0 at a smooth minimum. The stated inequality can reject a genuine boundary minimum and permit a negative feasible vertical derivative. Correct the vertex formula, delete the sign-reversal claim, and correct the mixed vertex-kink version in LF 51 using the same selected subgradient for both inequalities.

### M2 — Justify the exact nonsmooth equivalences, not merely an inclusion

**MAJOR; primary manuscript LF 25; related LF 21 and 49; confidence 0.97 in the proof defect, not a claimed counterexample to the particular privacy value.** LF 25 says, `Because ∂_λ h<0 is continuous and single-valued, Clarke's implicit-function chain rule gives` the exact identity `∂_C rho(a*,c*) = −∂_C h_{(a,c)}(a*,c*;λ*)/(∂_λ h)`, and then asserts equivalence of the two stationarity systems. A continuous, single-valued, nonzero lambda partial plus local Lipschitzness and finite C1 stratification does not by itself give that equality; the usual generalized chain/implicit calculus gives inclusions without further regularity. LF 21 likewise asserts an exact integral-subdifferential interchange without establishing the required regularity and compatibility for these moving, feasibility-restricted branches, and LF 49 identifies Clarke stationarity with nonnegative ordinary one-sided directional derivatives. The written negative controls below distinguish these claims. Prove an appropriate stronger regularity/envelope theorem for this actual value function, including the moving-limit and deterministic terms, or restrict the claim to the necessary inclusion (F), which follows directly by the order argument below. Calling the derivatives in LF 49 *Clarke generalized directional derivatives* repairs that particular equivalence; ordinary directional derivatives require an additional regularity proof.

### m1 — Integrate the master formula over the actual block interval

**MINOR; manuscript LF 15–19, specifically LF 17; confidence 1.00.** The displayed formula uses `8∫_0^{c}` while claiming to apply to a generic block and specifically to Phi_0 with box [a,2a-y]. That box is empty for y>a, whereas c>=a+1/2, so the core specialization as written integrates an undefined minimizer over a positive-length interval. Use the same moving limits as the block value: [0,a] for the core, and the appropriate overlap/corner/free-tail intervals for the tail. This is a formula repair, not a criticism of the imported fixed-box minimization rule.

## Independent reconstruction

### 1. Feasible geometry and all five cases

Write d=(u,w). At the vertex,

T_K(0,1/2)={u>=0,w>=u}=cone{(0,1),(1,1)}.

Consequently its polar, with the standard outward-normal convention already used correctly in G2 and G4, is

N_K={n:n_c<=0,n_a+n_c<=0}=cone{(-1,0),(1,-1)}.

Putting -g in this cone gives g_c>=0 and g_a+g_c>=0. There is no reversal of the sign of g_c between G2 and G3. What changes at the vertex is that the edge's tangential equality becomes an inequality because motion in the negative (1,1) direction is no longer feasible.

A written intended-reason negative is f(a,c)=c-1/2. It has a constrained global minimum at the vertex and gradient (0,1), contradicting the proposed h_c<=0 test. Conversely, the permitted gradient (1,-1) satisfies the manuscript's two inequalities but decreases along (0,1). These are geometry controls, not claimed privacy instances or choices of epsilon.

The complete smooth conditions are:

| Geometry | Correct normal cone | Necessary gradient conditions |
|---|---|---|
| G1: a>0,c>a+1/2 | {0} | h_a=h_c=0 |
| G2: a>0,c=a+1/2 | {t(1,-1):t>=0} | h_a+h_c=0, h_c>=0 |
| G3: a=0,c=1/2 | {(x-z,-x):x,z>=0} | h_a+h_c>=0, h_c>=0 |
| G4: a=0,c>1/2 | {t(-1,0):t>=0} | h_c=0, h_a>=0 |

At a kink, the valid necessary Clarke formulation is that **one** g in the correctly defined partial Clarke subdifferential satisfies the corresponding row. For G3 both inequalities must hold for the same g. Selecting different subgradients to satisfy separate inequalities would not imply -g in N_K.

### 2. Fixed-profile uniqueness, lambda derivative and local structure

The f273 disposition imports strict fixed-parameter profile uniqueness on the convex feasible polygon, the corrected slack/active rule, its one-way active-interval implication, and the attained reduction rho. I use those statements conditionally and do not rerun the earlier uniformly-shifted-root criticism.

At fixed (a,c), h minimizes N-lambda Z over the corrected profiles. Since the minimizing profile is unique, its denominator is single-valued. Danskin in the lambda variable gives h_lambda=-Z evaluated at that minimizing profile; this is not a separate minimization of Z. The geometric-tail area identity is

A(C_1+GD)=A(C_1)+8cG+2G^2.

With the adopted N=2 weights, Z=(1-b)A(C_0)+b E[A(C_1+GD)]>=2bT2>0. Thus the claimed negative partial and its lower bound are supported conditionally on the imported finite-tail notation and fixed-profile rule. Continuity follows from the continuous feasible polygons/clips and unique optimizer, followed by dominated convergence on bounded parameter sets. Collapsed endpoint boxes occur on zero-height-measure boundaries and do not create denominator nonuniqueness.

Bounded branch slopes and matching values at moving height joins support local Lipschitzness on K. The usual smooth-cell differentiation is valid on open cells with fixed clipping/activity pattern and regular moving height boundaries. These observations are not a proof of Clarke regularity at every degenerate or positive-measure coincidence locus. In particular, C1 *on strata* is weaker than a single C1 extension through all their frontiers. A boundary use of an ambient Clarke subdifferential also needs a specified compatible local extension or a precise relative convention; K alone is not an open domain.

### 3. The required necessary inclusion does not need an exact chain rule

Fix lambda*=rho(x*) and x=(a,c). Strict decrease in lambda and the unique zero imply

rho(x)>=lambda* if and only if h(x;lambda*)>=0.

Hence a local constrained minimum of rho at x* is also a local constrained minimum of h(.;lambda*), with value zero. The Lipschitz constrained Fermat rule directly gives

0 in partial_C h(.;lambda*)+N_K.

This proves the necessary inclusion, with the correct normal cones, without asserting equality of the two generalized gradients. If an exact identity partial_C rho=kappa partial_C h with kappa=-1/h_lambda>0 is independently established, equivalence of the stationarity systems then follows algebraically because N_K is a cone. The positive-scaling algebra is sound; the unproved step is the exact generalized-gradient identity, not its sign.

### 4. Written negative controls for the nonsmooth claims

**Implicit-equality control.** Let chi be a smooth compactly supported function in (-1/2,1/2) with chi(0)=1. In local coordinates s and t=lambda-lambda_0, put

H(s,t)=s-t+s^2 chi(t/s) sin(1/s) for s!=0, and H(0,t)=-t.

This is a reviewer-constructed generic calculus control, not the privacy functional. It is locally Lipschitz with bounded first derivatives off its exceptional point and has a finite smooth stratification. Its t partial is

H_t=-1+s chi'(t/s) sin(1/s),

which is continuous at the origin with value -1 and is strictly negative on a sufficiently small neighborhood. The unique implicit zero is t=s, since chi(1)=0. Its root function therefore has Clarke derivative {1}. But H(s,0)=s+s^2 sin(1/s), whose Clarke derivative at zero is [0,2]. Thus the asserted exact fixed-slice identity would identify {1} with [0,2], and even the two interior stationarity tests differ. This disproves the stated generic inference from local Lipschitzness, finite smooth stratification and a continuous single-valued negative partial. It does **not** refute an identity proved with stronger structure for the actual privacy functional.

**Ordinary-directional control.** H(s,t)=-t-|s| is the minimum of two smooth candidates and has H_t=-1. At the origin its s-subdifferential contains zero, whereas its ordinary directional derivative in every nonzero s direction is negative. Thus the word “equivalently” in LF 49 is not justified by being a finite minimum of smooth candidates. Clarke generalized directional derivatives are different: their support-function definition gives the usual stationarity/separation equivalence. Ordinary directional equivalence can be recovered with a proof of the relevant Clarke regularity, not from local Lipschitzness alone.

**Interchange boundary.** The exact Aumann-integral formula needs verification for the actual feasible branches, rather than a generic assertion about Lipschitz integrands. A slack branch can cease to be feasible when the independent projections violate the coupling; an active interval can be empty on its nominal formula domain. Such candidates are smooth on their valid strata, not automatically a finite family of globally C1 functions with a common domain. The f273 one-way feasibility repair must be retained here. I have not claimed an actual counterexample to the manuscript's particular interchange; its equality is INCONCLUSIVE from this packet's given argument. The deterministic c polynomial and all Leibniz terms must be included in whichever exact representation is proved.

### 5. Danskin–Leibniz reconstruction and coefficients

For an actual block interval [L(x),U(x)] and direction v, the smooth-stratum formula is

D_v J=8 psi(z*(U),U) D_v U - 8 psi(z*(L),L) D_v L + 8 integral_L^U psi_z(z*,y) D_v z* dy,

with any explicit parameter derivative of psi added if present. For an interior unconstrained root the last contribution vanishes by psi_z=0. At a lower or upper clip it uses the corresponding endpoint speed. The core endpoints a and 2a-y therefore have speeds 1 and 2 under partial_a, and the tail endpoints c and 2c-y have speeds 1 and 2 under partial_c. These are speeds one and two, not one-half.

On the active diagonal S, the interval is

ell=max(a,c-1), u=min(2a-y,2c-y-1).

Away from endpoint ties the displayed partial_a speeds 1_{a>c-1} and 2 times 1_{2a-y<2c-y-1} are correct. At a tie one must use the appropriate branch gradients/hull or the actual directional formulas D_v ell=max(v_a,v_c) and D_v u=min(2v_a,2v_c). For example, on c=a+1/2, feasible directions have v_c>=v_a and D_v u=2v_a; a strict indicator evaluated as zero at equality is not a boundary directional derivative. Applying Danskin to an active block uses the pooled weighted objective. Differentiating an individual summand instead uses the dependence of the shared optimizer, including cross-dependence on the other scalar.

The integration limits are [0,a] for the core, with its endpoint integrand zero at y=a; tail overlap, corner and free pieces have joins y=a, a+1/2 and c. Their directional speeds are respectively v_a,v_a,v_c. Matching internal endpoint values can cancel Leibniz terms only after the adjacent terms are actually combined. This verifies the stated endpoint/corner mechanism while identifying the incorrect universal 0-to-c range in (M).

Using the adopted tail moments m=E[G] and T_j=E[G^j], the separate tail polynomial is

C(c;lambda)=4c^2 T2+(16/3)c T3+(2/3)T4-lambda(8cm+2T2).

Its c derivative is exactly 8cT2+(16/3)T3-lambda 8m, as in LF 19. It is separate from the profile integral and must not be lost in a subdifferential selection formula.

Finally, partial_a Tail_min=0 is supported on a genuinely fully slack regime: the entire minimizing tail profile is then determined by c and lambda, and no overlap or corner forcing depends actively on a. Slackness at only some heights is not enough to discard the remaining active/corner contributions. On active regimes the shared diagonal endpoint speeds, moving corner joins and floor derivative 2 on {2a+1-y>c} are the correct mechanisms. This is a structural verification, not certification of the unresolved exact nonsmooth interchange.

## Per-claim disposition

| Claim | Disposition and boundary |
|---|---|
| Actual-cutoff-two reduction and attainment | SUPPORTED conditionally on named f273 and f261 dispositions; no new proof of nonemptiness. |
| Corrected fixed-box rule, uniqueness, one-way active implication | SUPPORTED as named f273 imports; no reopening of its old M1. |
| Local Lipschitzness on K | SUPPORTED conditionally on the imported profiles, bounded slopes and matching joins. |
| C1 differentiation on regular open strata | SUPPORTED; not a proof of Clarke regularity through every stratum frontier. |
| Single-valued continuous h_lambda=-Z<0 and lower bound | SUPPORTED under the imported unique fixed-profile/tail formulation. |
| Box speeds 1 and 2; diagonal speeds away from ties | SUPPORTED. |
| Literal universal master formula (M) | REFUTED as written: wrong interval for the core; m1. |
| Tail constant derivative, corner floor and moving-limit mechanisms | SUPPORTED at smooth-stratum scope, with all summands/cross-dependencies retained. |
| Zero a-dependence of tail | SUPPORTED only on a fully slack tail regime. |
| Exact integral formula for partial_C h | INCONCLUSIVE: actual regularity/interchange and full deterministic/Leibniz accounting not established; M2. |
| Exact implicit Clarke identity and stationarity equivalence | INCONCLUSIVE for this h; the claimed generic justification is REFUTED by the written control; M2. |
| Necessary inclusion (F) | SUPPORTED directly by monotonicity/order and constrained Fermat, with a correctly defined subdifferential. |
| G1 | SUPPORTED. |
| G2 | SUPPORTED. |
| G3 and its claimed sign reversal | REFUTED; M1. |
| G4 | SUPPORTED. |
| G5: existence of one Clarke subgradient with -g in N_K | SUPPORTED as a necessary condition, with correct normal cone. |
| G5: exact measurable-selection representation and ordinary-directional equivalence | INCONCLUSIVE for the particular h; generic equivalence is false without extra regularity; M2. |
| Necessity only; no scalar-pair sufficiency or uniqueness | SUPPORTED as the manuscript's stated limitation. No new optimizer sufficiency/uniqueness was established or imported. |
| f278 nonemptiness certification mentioned in LF 5 | NOT CHECKED / NONINPUT; its body was neither listed nor opened. |

## Integrity and complete coverage receipt

All three scientific inputs were hashed and counted before any of their bodies were opened. Their metadata matched every declared value. Complete raw display of all three, in the following order and windows, finished before mathematical consideration or mathematical note-taking began. Every scientific window has at most 15 LF and includes the actual final line of its file.

| Input | Observed SHA-256 | Bytes | LF | Every raw display window, in order |
|---|---|---:|---:|---|
| Manifest: manifest-v1.json | eb7df92a957235f122a16c4f828134dc2c6c78d65d3958c3729f4a3e72a3727d | 4254 | 43 | Initial full raw display 1–43; after verification, repeated 1–15, 16–30, 31–43. See process disclosure. |
| Manuscript: frontier-20261029-n2-normal-cone-envelope-conditions-v1.md | df1224e15ac5723d2841f99c5c2d93626bad8d543b499bebfafe8f6886afe742 | 6990 | 59 | 1–15, 16–30, 31–45, 46–59 |
| Named f273 disposition: info-1-privacy-n2-coupled-complementarity-variational-reduction-parent-v1.md | 51502ed65a16c5fe43da2416ee7e2365dbc1df306d388c9b01dec966012d067c | 4394 | 16 | 1–15, 16–16 |
| Named f261 disposition: info-1-privacy-all-epsilon-optimizer-complementarity-finite-tail-parent-v1.md | 28335b2def1139d4141a3f62a74ef0f0063f57f2f7500d41d065466267381c97 | 8487 | 44 | 1–15, 16–30, 31–44 |

The absolute input paths are exactly those in the verified manifest. Scientific inputs total 19871 bytes / 119 LF. No further scientific displays, unlisted manuscript bodies, sibling reviews, earlier wave outputs, author scripts, network resources or external models were used. References appearing inside the adopted dispositions were not followed.

Metadata controls used shasum -a 256 and wc -c -l, with /bin/date before/after and a 120-second tool timeout. Both calls returned successfully with matching outputs; the rendered tool results did not print a numeric exit-status field. No control timed out. No mathematical script/subprocess was run; the negative controls above are written mathematics, not executed experiments. Consequently there are no executable reviewer-control artifacts or claimed executable PASS receipts.

## Native clock observations and additive process disclosure

The following are native /bin/date observations, not inferred creation times or backdated timestamps:

- 2026-10-29T20:24:30-0700 PDT, before and after manifest metadata verification.
- 2026-10-29T20:24:51-0700 PDT, before and after all scientific-input metadata verification; the subsequent small-window manifest repeat and scientific displays followed this observation.
- 2026-10-29T20:25:51-0700 PDT, after all scientific displays and before mathematical reconstruction.
- 2026-10-29T20:35:46-0700 PDT, reconstruction checkpoint.
- 2026-10-29T20:42:56-0700 PDT, before drafting/output phase.

Disclosures, not retroactive cures:

1. The initial manifest read preceded the first native clock observation and displayed all 43 LF in one raw call. The scientific-input display policy was obeyed in full, but if its <=15-LF restriction also applies to the manifest, that initial manifest display exceeded it. After verifying the manifest I displayed it again as 1–15, 16–30, 31–43; the first display is not erased by the repeat. No scientific input had been opened and no mathematics had begun at that point.
2. Mandatory administrative guidance outside the manifest was read: memory://root/memory_summary.md, skill://aifours-written-math-acceptance-protocol, and skill://independent-snapshot-review. These were process guidance, not mathematical evidence or additional scientific imports. No external-model review procedure was launched. This access is disclosed rather than represented as manifest-only file access.
3. No mathematical consideration or notes preceded completion of all scientific displays. No frozen input, manifest, disposition, ledger or README was modified. No parent adoption decision is made by this review. The mathematical finding count above does not purport to adjudicate these reviewer-process deviations.

## Assurance boundary

This is a **same-harness written mathematical review** using the two explicitly named dispositions as conditional imports and reviewer-owned hand derivations/negative controls. It is not human review, independent-model-family review, formal or kernel verification, author-code execution, a replay of prior parent executable controls, source/book equivalence, novelty verification, or confirmation of f278. The remaining task is additive mathematical correction and justification at the stated scope, not a sufficiency or uniqueness claim.
