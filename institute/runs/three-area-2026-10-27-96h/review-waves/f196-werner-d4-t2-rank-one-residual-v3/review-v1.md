# f196 independent same-harness review: Werner d=4 two-copy packet v3

**Disposition:** 0 FATAL / 0 MAJOR / **3 MINOR** in the reconstructed written scope; the numerical/descent and Hessian reports are **INCONCLUSIVE / not independently checked**. The Böttcher–Wenzel case is reconstructed only **conditional on that explicitly stated inequality**. The complete rank-one-B claim and the general nonnormal case remain open. This review does **not** establish T2, T3, Z2, the original target, a counterexample, novelty, or independent-family, human, formal/kernel verification.

Native clock observed before writing: `2026-10-29T10:02:57-0700 PDT`; this is not asserted to be the creation time. The source labels below are pinned whole files, not permission to expand the linked source chain.

## 1. Frozen inputs, sequence, and scope

The first research artifact read was `manifest-v1.json`, SHA-256 `330fb254ad304456daec491c3b32161e89397d6674f715eea59469ef905722c7` (3,315 bytes, 30 LF), equal to the assigned hash. Environment/skill guidance and directory/name metadata were inspected before that manifest; they contained no mathematical payload from this review. After the manifest, the complete whole-file SHA-256, bytes, and LF of **both** declared inputs were measured and matched **before** either body was read. Then the bodies were read completely, in manifest order and in short raw windows, including their final lines, **before mathematical reconstruction or control construction**:

1. **F168:** `dispositions/physics-1-werner-stratified-duals-and-support-ladder-parent-v1.md`, `adbc15fdcccb66519353a8288993f571d9e94931ffae23c77f7a01da3d8579bf`, 7,488 bytes, 41 LF; windows 1–10, 11–20, 21–30, 31–41.
2. **V3:** `physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261029-d4-t2-two-copy-obligation-packet-v3.md`, `7c0df3e55f53eae89710381a8c1cbf3c5a58418e192d74997dd94181fec7acaf`, 9,076 bytes, 117 LF; windows 1–12, 13–24, 25–36, 37–48, 49–60, 61–72, 73–84, 85–96, 97–108, 109–117.

Only F168's expressly adopted odd-sector/dual equivalence, rank-one positivity, two-plane spread bound, and one-site support ladder, with its five stated qualifications, are imported; in particular, **input and output legs at one site do not count as two sites**. T1 for rank at most two is also shown directly below. No linked source/certificate body, f161/f162/held material, sibling review, author script/result, literature recollection, web/model/API, or author contact was used. The first reviewer-control run failed because of a reviewer fixture arithmetic error; that retained deviation and corrected bounded run are reported in §7. No claimed complete reading preceded the actual complete reads.

## 2. Individual claim dispositions

`0F/0M/0m` means no finding at the specifically reconstructed scope, not a claim of global target acceptance. `m` means a MINOR correction is required; `INCONCLUSIVE` means the claimed numerical or external premise is not established by this review.

| V3 claim | Verdict and precise scope |
|---|---|
| §1 primal/dual equivalence, traceless parametrization, and original target implies T2 | **0F/0M/0m**, importing only the corresponding qualified F168 statements; explicit reconstruction below. Removing tracelessness from the displayed `2(‖A‖²+‖B‖²)` formula is invalid. |
| §2 Lemma 2.1: a two-plane supported on a ≤2-dimensional leg at **one** site | **0F/0M/0m**, including input and adjoint/left orientations. Uses F168's one-site ladder and T1; no two-distinct-sites inference. |
| §2 Theorem 2.2: A or B normal | **0F/0M/0m** for the displayed **dual inequality on that pair**. It is not a proof of the universally quantified T2 assertion. Degenerate top singular values permit a suitable block-supported choice. |
| §2 `B=−Aᵀ` | **0F/0M/0m conditional** on `‖[A,Ψ]‖²≤2‖A‖²‖Ψ‖²` for all complex Ψ. The imported Böttcher–Wenzel inequality itself is **INCONCLUSIVE** here; an exact finite instance is not its proof. |
| §3 block identity, each site; Lemma 3.2 trace-sign class | **0F/0M/0m** for all C in the identity and rank ≤2 in the sufficient sign lemma. |
| §3 projection split and existence-of-J sufficient condition | **0F/0M/0m**, with rank-2 P and the rank-≤2 hypothesis for the sign of the two projected terms. Existence of such J is not established. |
| §3 Haar second moment and averaged split | **0F/0M/0m** as identities; the average yields no universal positivity not already present in the block formula. |
| §4 traceless rank-one B normalization; direct sum and both-same-block/cross cases | **0F/0M/0m**, including arbitrary complex phases, repeated singular values, and the B=0 limit. |
| §4 Proposition 4.1, including both directions of (†) | **0F/0M/0m**: equivalence is for each **fixed traceless A** and **all** traceless rank-one B, not a proof that (†) holds universally. |
| §4(a) Frobenius/top-singular sufficient threshold | **0F/0M/0m** with exact threshold `(5−2√2)/2`; sufficiency is reconstructed, not its optimality for traceless A. |
| §4(b) fixed-b second-singular-value bound and orthogonal top pair | **0F/0M/0m**, including `|⟨u,φ⟩|=1` and b=0 degeneracies. |
| §4 rank-one traceless A and equality in (†) | **0F/0M/0m**. The equality test includes all normalized choices with ψ0 and ψ1 parallel to the top right vector. |
| §4 near-rank-one/overlap bounds | **m, MINOR 2:** the analytic bound is valid, but the printed `1.0858` is a rounded conservative envelope, not an exact residual cutoff. The exact and quantified residual is §5 below. |
| §4 statement that *any proof* must be sharp to second order | **m, MINOR 3:** equality at a rank-one point alone does not establish that methodological necessity. A concrete quadratic-gap family exists (§5), but it does not prove a theorem about every possible proof. |
| §5 primal rank-one, supported-leg and spread classes; T2/Z2 relations | **0F/0M/0m** under F168's qualified imports. The trace-sign class is covered independently by §3. Neither T2 nor Z2 is closed. |
| §5 general nonnormal residual | **0F/0M/0m** as a necessary uncovered region, read with explicit quantifiers in §5; it is not a characterization of counterexamples. Calling its isolated rank-one slice the “sharpest” is not a quantified comparison theorem. |
| §6 descent/search counts, limiting-point observations and both Hessian inertias | **INCONCLUSIVE / NOT REPLAYED:** author code and result bodies were not read or executed; these are reported observations only. Even if correct they are finite/local diagnostics, not universal positivity or a global counterexample. |
| §6 equality family | **m, MINOR 1:** the equality is valid for complex coefficients after replacing `a²,b²` in the squared-singular-value list by `|a|²,|b|²`, or explicitly restricting a,b to real values. |

The three MINORs do not supply the missing universal inequality and are not silently promoted to source corrections.

## 3. Dual, support, normal and block reconstructions

All norms below are Hilbert–Schmidt unless a singular value or operator norm is specified. F168 gives `q2(C)=‖C‖²−2‖Podd C‖²` and the rank-two/Ky-Fan dual. At d=4 its odd sector is exactly `X=A⊗I+I⊗B` with `Tr A=Tr B=0`. Its two summands are Hilbert–Schmidt orthogonal and `‖X‖²=4(‖A‖²+‖B‖²)`, giving the displayed dual bound. F168 gives T3⇒T2 and, with its qualifications, the support ladder. For rank-≤2 Y, `|Tr Y|²≤rank(Y)‖Y‖²≤2‖Y‖²`, hence `q1(Y)≥0` (T1).

For Lemma 2.1, suppose a two-plane F has a ≤2-dimensional leg at one site and `‖XP_F‖²>‖X‖²/2`. Set `C=XP_F`. Then `rank C≤2`, `ran C†⊂F`, and `⟨X,C⟩=‖C‖²`; since X is in the odd sector, Cauchy–Schwarz gives `‖Podd C‖²≥‖C‖⁴/‖X‖²>‖C‖²/2`. Thus `q2(C)<0`, contradicting the **one-site** support ladder and T1. Passing to X† gives the left-plane statement. Nothing here counts both orientations at the same site as separate supported sites.

If B is normal, diagonalize it by a local unitary. X is the orthogonal direct sum of `A+b_j I` over site-2 basis vectors. Even when singular values tie, select two maximizing right singular vectors within individual blocks. Their span has site-2 support in at most two basis vectors, so the lemma supplies the desired sum-of-top-two bound; interchange sites when A is normal.

With row vectorization, `B=−Aᵀ` gives `X vec Ψ=vec[A,Ψ]`. The stated commutator premise bounds the largest squared singular value of X by `2‖A‖²`; the second is no larger. Therefore their sum is at most `4‖A‖²=2(‖A‖²+‖B‖²)`. This is only the conditional implication: neither the premise nor its literature provenance is adopted as established here.

For site-2 blocks `C^{kl}` and `S=Tr₂C`, direct expansion yields

`Σ_{kl} q1(C^{kl}) = ‖C‖²−(1/2)‖Tr₁C‖²`,

and consequently `q2(C)=Σ_{kl}q1(C^{kl})−(1/2)q1(S)`; exchange sites for the mirror identity. Each block is a left/right contraction of C and has rank at most rank C. Hence, for rank C≤2, all block q1 terms are nonnegative, proving the trace-sign class. The rank hypothesis cannot be removed: `C=I₄⊗|0⟩⟨0|` has rank 4, `q1(Tr₂ C)=−4`, but `q2(C)=−2`.

Let `P+Q=I`, `rank P=rank Q=2`, `J=P−Q`, `C_P=(I⊗P)C`, `C_Q=(I⊗Q)C`, and `D=Tr₂[C(I⊗J)]`. Orthogonality of the two output blocks, cyclicity of the partial trace on site 2, and polarization of q1 give

`q2(C)=q2(C_P)+q2(C_Q)−q1(S)/4+q1(D)/4`.

Both projected rank-≤2 operators have a supported output leg at site 2, so their q2 terms are nonnegative by the one-site ladder and T1. Thus `q1(D)≥q1(S)` for even one P is a sufficient condition; the identity gives no general existence of P.

For Haar-random rank-2 P, `E[J⊗J]=aI+bF`. Unitary invariance gives this two-term form; `Tr J=0` and `Tr J²=4` give `16a+4b=0`, `4a+16b=4`, hence `a=−1/15,b=4/15`. Let `T=Σ q1(C^{kl})`, `S₁=q1(Tr₂C)`. Contracting the covariance gives `E q1(D)=(4T−S₁)/15`. Also `E[q2(C_P)+q2(C_Q)]=(14/15)T−(7/30)S₁`. Substitution reduces the averaged split to `q2(C)=T−S₁/2`; it is not an independent proof of T2.

## 4. Complete rank-one-B reduction and proved subcases

For nonzero rank-one traceless B, write `B=|x⟩⟨y|` with `⟨y,x⟩=0`. A site-2 unitary and phases put it in the form `bE01`, with b≥0; allowing complex b instead simply retains the phase and is convenient for optimization. Then

`X = M_b ⊕ A ⊕ A`,  `M_b = [[A,bI],[0,A]]`.

Its singular-value multiset is the union of the three blocks. If two selected top vectors come from `M_b`, their span has a supported site-2 leg; the same is true if both come from the two A blocks. Thus Lemma 2.1 settles those cases. In a cross selection one uses a top right vector of `M_b` and one top right vector φ of A from either A copy. The cross-pair sum is `σ₁(M_b)²+σ₁(A)²`; it is a legitimate two-vector Ky-Fan test even when ties allow other choices.

Fix traceless A. Put `σ=σ₁(A)`, `p²=‖ψ0‖²`, `q²=‖ψ1‖²`, `p²+q²=1`, and `z=⟨Aψ0,ψ1⟩`, with the inner product conjugate-linear in its first argument. For any complex b,

`‖M_b(ψ0,ψ1)‖²−2|b|² = ‖Aψ0‖²+‖Aψ1‖²+2 Re(bz)−(1+p²)|b|²`.

Its maximum over b is `‖Aψ0‖²+‖Aψ1‖²+|z|²/(1+p²)`, attained at `b*=conj(z)/(1+p²)`. Therefore the cross-pair inequalities for **all** b and all normalized `(ψ0,ψ1)` are equivalent to

`‖Aψ0‖²+‖Aψ1‖²+|⟨Aψ0,ψ1⟩|²/(1+p²)+σ² ≤ 2‖A‖²`.  (†)

Combining with the two safe same-block cases proves both directions of Proposition 4.1. If (†) fails, `z≠0`: otherwise its left side is at most `2σ²≤2‖A‖²`. Thus the optimizing b is nonzero and supplies a genuine rank-one B; alternatively, B=0 is included by continuity and is already normal. Arbitrary b phases do not change the reduction or its local-unitary normalization.

For (a), `‖Aψ0‖²+‖Aψ1‖²≤σ²` and `|z|²≤σ²p²q²`. With `t=p²∈[0,1]`, the derivative of `t(1−t)/(1+t)` has numerator `1−2t−t²`; its maximum is `3−2√2`, at `t=√2−1`. Thus the left side of (†) is at most `(5−2√2)σ²`, proving the condition `‖A‖²≥[(5−2√2)/2]σ²`. No optimality of this coarse sufficient threshold is asserted.

For (b), choose a top singular pair `Aφ=σu`, `A†u=σφ`. If `|⟨u,φ⟩|<1`, let χ be the normalized component of φ perpendicular to u; otherwise take any unit χ perpendicular to u. The domain vectors `(φ,0)` and `(0,χ)` are orthonormal and their M_b images are orthogonal. Their squared norms are `σ²` and `|b|²+‖Aχ‖²`, with `‖Aχ‖²≥σ²(1−|⟨u,φ⟩|²)`. The min–max principle gives

`σ₂(M_b)² ≥ min{σ², |b|²+σ²(1−|⟨u,φ⟩|²)}`.

If `|b|≥σ|⟨u,φ⟩|`, two top vectors may be chosen in the safe M_b block, including equality/tie cases. If one top pair has `⟨u,φ⟩=0`, this works for every b; hence (†) holds for that A. A nonzero rank-one traceless A has this orthogonality and `‖A‖²=σ²`. For normalized ψ0,ψ1 parallel to φ, z=0 and the left side of (†) equals `2σ²`, so equality is attained. A=0 is trivial; a rank-zero B is normal.

## 5. Literal residuals and the three minor corrections

**Rank-one B.** Set `c₀=(5−2√2)/2≈1.0857864376`. Once all the proved classes are removed, a possible failure of (†), if one exists, must have a traceless, nonnormal A of rank at least two, `σ=σ₁(A)>0`,

`‖A‖² < c₀ σ²`,

and a normalized test pair `(ψ0,ψ1)` with `z=⟨Aψ0,ψ1⟩≠0` and

`0 < |b*| = |z|/(1+‖ψ0‖²) < σ|⟨u,φ⟩|`,

where `Aφ=σu`, `A†u=σφ`. Here the top singular value is simple: `σ₂²≤‖A‖²−σ²<(c₀−1)σ²<σ²`. In particular the top pair is unique up to phase and its overlap is nonzero. The proposition reduces this remaining proof obligation literally to (†) for **every** such A and every such normalized test pair. These conditions are necessary for an uncovered failure, not a guarantee that one exists. The source's rounded `1.0858` is a larger, safe-to-state but inexact envelope: values between the exact cutoff and 1.0858 are already covered by (a).

Writing `R=A−σuφ†`, a singular-value decomposition gives `rank R≤3`, `‖R‖²=‖A‖²−σ²`, and tracelessness gives

`σ|⟨u,φ⟩|=|Tr R|≤√3‖R‖ < √[3(3−2√2)/2] σ < 0.51σ`.

This establishes the stated small-overlap conclusion. It does not prove the remaining inequality.

Equality at rank-one A precludes a uniform strictly positive margin, but does not logically imply that **every** possible proof must be “sharp to second order.” To make the diagnostic precise, for `0<c<1` set `s=√(1−c²)`, `ε=c/(2+c)`, `u=c e0+i s e1`, `u₂=i s e0+c e1`, and

`A_c=u e0†−ε(u₂ e1†+e2e2†+e3e3†)`.

This A is traceless and nonnormal, with singular values `1,ε,ε,ε`, top pair `(u,e0)` and overlap c. For `ψ0=(3/5)e0`, `ψ1=(4/5)e0`, the optimal `b*=6c/17<c`, and the (†) right-minus-left gap is exactly

`c² [ 6/(2+c)² − 72/425 ]`.

It is positive and quadratic as c→0; for small c it lies in the literal near-rank-one regime. This illustrates a delicate boundary and gives a checkable family, not a necessity theorem for proof methods. The exact control at `c=7/25` is recorded below.

**General nonnormal residual.** A still-unsettled dual pair has traceless A and B, both nonnormal. For every choice of a maximizing top-two **right** singular two-plane F, neither a ≤2-dimensional leg at either site nor the spread test `μ₁(F)+μ₂(F)≤2` can be available, where `μ_i(F)=‖Tr_i P_F‖∞`. The same is necessary for every maximizing **left** singular two-plane, by the adjoint argument. Choices in singular-value degeneracies are included: one favorable maximizing plane suffices to prove that pair safe. If one matrix is traceless rank one, its remaining slice is the fully quantified (†) regime just stated (or the site-swapped version); pairs with both matrices of rank at least two are not resolved by that reduction. The `B=−Aᵀ` family cannot be removed unconditionally on the strength of the unverified commutator premise. These are necessary conditions for a failure of the displayed dual inequality, not a claim that any such failure occurs.

On the primal side, after the established classes, a possible counterexample must have rank exactly two; all input and output legs at both sites have dimension at least three; neither its input nor its output two-plane can obey the corresponding `μ₁+μ₂≤2` test; and `q1(Tr₁C)>0`, `q1(Tr₂C)>0`. Moreover, for every rank-2 local projection P at each site, the corresponding split witness must fail: `q1(Tr_i[C J_i])<q1(Tr_i C)` with `J_i=2P−I`, in the appropriate local tensor placement. These necessary exclusions do not prove positivity in their complement. F168's one-site ladder plus T1 covers every rank-≤2 C outside the full-leg stratum, so T2⇔Z2, while F168 states T3⇔Z2∧Z3. Neither equivalence closes T2, Z2, T3, Z3, or the original problem.

**Complex equality-family correction.** For `X=aE01⊗I+bI⊗E01` with arbitrary complex a,b, its squared singular values are `|a|²+|b|²` twice, `|a|²` twice, `|b|²` twice, and zero ten times. Hence the top-two sum is `2(|a|²+|b|²)=‖X‖²/2`. The printed a²/b² list is correct if a,b are explicitly real, but not as a literal list for general complex scalars; for example `a=1+i,b=2−i` gives squared values 7,2,5,0 with the stated multiplicities, not complex values `a²,b²`.

## 6. Independent exact finite controls, with boundaries

The reviewer-authored controller/worker uses only standard-library `Fraction` arithmetic over exact Gaussian rationals, not author code. The corrected run produced **45 positive controls and 16 intended-reason negative controls**. Among them:

- A complex rank-two C has `q1(Tr₂ C)=−209/50` and `q2(C)=1809/100`; both block orientations, the odd-sector formula, a complex rank-two projector split and exact Haar-covariance contractions agree. Changing the odd-sector overlap coefficient, block coefficient, Haar coefficient, or split sign is detected. Dropping the rank restriction is detected by the rank-four counterfixture above.
- A complex nonnormal A and diagonal normal traceless B give top sum `6+4√2≤16`; replacing traceless A,B by `(1+i)E00` makes the displayed dual bound fail as `10>8`. This mutation only shows the traceless **formula** cannot be extended verbatim; it is not a counterexample to T2. A complex commutator instance gives `48≤96`; replacing transpose by adjoint breaks the vectorization identity.
- Complex-b square completion and direct-sum cross pairing agree exactly. Replacing `1+p²` by `1+q²` or omitting `2|b|²` is detected. Dropping traceless A gives a genuine dagger-mutation failure `1844/425>4`. The false extremal constant `1/8` is detected by `72/425>1/8`. Exact orthogonal-top-pair and rank-one-traceless-A controls include equality.
- In the near-rank-one family above, c=`7/25`, `ε=7/57`, `σ²=1`, `‖A‖²=1132/1083`, `b*=42/425<7/25`; the tested (†) instance has left `534778/265625` and right `2264/1083`. This is one **positive finite point inside the residual**, not a proof of that residual.
- For complex `a=1+i,b=2−i`, the equality-family Gram matrix satisfies its exact spectral polynomial and power sums for squared eigenvalues `0,2,5,7` with multiplicities `10,2,2,2`; the non-modulus-square mutation produces a nonreal wrong trace.

A control checks its stated instance or mutation only. Exact finite arithmetic, finite descent, and local second-order behavior do not establish any universal sign or counterexample exclusion.

## 7. Control receipts, actual failure, and file fingerprints

Each run had its own controller-enforced 110-second child cap and an outer 120-second tool deadline. A cap would be `UNKNOWN`, not PASS.

| Run | Native start → end; monotonic duration | Worker exit / result | Evidence |
|---|---|---|---|
| v1 | `2026-10-29T09:57:50-0700 PDT` → `2026-10-29T09:57:51-0700 PDT`; 0.144893 s | exit 1, **FAILED**, not counted | The reviewer's near-rank-one fixture mistakenly used `(3,24,25)` as a Pythagorean triple. The traceless/singular-Gram positive assertion failed; this was a fixture error, not a V3 counterexample. Artifacts retained unchanged. |
| v2 | `2026-10-29T10:00:40-0700 PDT` → `2026-10-29T10:00:40-0700 PDT`; 0.137255 s | exit 0, **COMPLETED**, 45 positive and 16 intended-reason negatives | Corrected to the exact `(7,24,25)` triple, with `ε=7/57`; worker stderr empty. No v1 partial assertions are counted. |

All paths below are in this review-wave directory; SHA-256 values are whole-file fingerprints, with bytes and LF in parentheses:

- `reviewer-controls-v1.py`: `9395198feca6a5baf1630a90b7e7bb6ebda88b1db7a4f88a9baa442e0f05e169` (18,153 B, 300 LF).
- `reviewer-controls-v1-results.json`: `d4a97251817ceb4f3ef9814e37022155ea74204fd0bd96fe57a2f01798c4d96c` (1,452 B, 5 LF).
- `reviewer-controls-v1-receipt.json`: `881875fae4c5990f5edff3f1aff47afbbb9565cc909477399aee3006172ae2b8` (752 B, 18 LF).
- `reviewer-controls-v2.py`: `eeb0718f861d4b139ce39b7cae7861d23ce1828bb0751dc97ce7d25da9cd9856` (18,153 B, 300 LF).
- `reviewer-controls-v2-results.json`: `8b83f162fb3f27b6e658f19ce85e8ba972b97b2b87d292e6e846d929e0e351cf` (7,290 B, 257 LF).
- `reviewer-controls-v2-receipt.json`: `984e15eb2eb974bb9e944fae6a583a6050a33201ffb2f355c522c54c8f343a1f` (753 B, 18 LF).

The SHA-256 of this review is supplied externally in the reviewer-prefixed SHA receipt, avoiding a self-referential hash claim. Same-harness review and exact checks are not independent-family, human, formal/kernel, novelty, T2, T3, Z2, or original-target acceptance.
