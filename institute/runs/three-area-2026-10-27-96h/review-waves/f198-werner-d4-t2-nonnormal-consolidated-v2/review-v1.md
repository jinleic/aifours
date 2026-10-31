# Independent same-harness review: f198 Werner d=4, T2 nonnormal v2

**Disposition: 1 FATAL / 0 MAJOR / 0 MINOR; 2 INCONCLUSIVE boundary items.** Lemma 4.1 is **false as stated** for arbitrary `T∈M₂(C)`, including for diagonal normal matrices. Its proof centers `N` as if `T` were traceless, and consequently also states a false identity and false inequality (4.2). A fully explicit rational counterexample is below. This single underlying defect is counted once, not separately for the identity, (4.2), and (4.1). The rank-one-B theorem is independently reconstructed. The square-normal theorem is also independently reconstructed using the **strictly narrower, true version of Lemma 4.1 with `Tr T=0`**; both blocks in its application do have trace zero. Thus the fatal finding does not by itself refute either headline T2 subclass, but the packet cannot be adopted as written without correcting the false lemma and its downstream citation.

The two inconclusive boundary items are (I1) arbitrary traceless A,B with **both squares nonnormal**, together with the still-larger T2/T3/Z2/Z3/original questions; and (I2) historical, external-source, literature, and novelty assertions. I1 is outside the proved classes, not a counterexample. I2 is not verified under this manifest's evidence restrictions. This review does not prove or disprove those statements.

## Frozen inputs, measurement, and actual sequence

1. The first research artifact opened was this wave's `manifest-v1.json`. Its measured SHA-256 was `b20567a4af1ae5222b611f8b3e7e83a5e85aaece07650f7591d2f83608601a58`, matching the assigned prefix `b20567a4af1a`. I read the manifest, including its long requirements line in full.
2. **Before reading either declared input body**, I measured SHA-256, bytes, and LF for both files. Each matched its manifest entry:
   - `dispositions/physics-1-werner-stratified-duals-and-support-ladder-parent-v1.md`: SHA-256 `adbc15fdcccb66519353a8288993f571d9e94931ffae23c77f7a01da3d8579bf`; 7,488 bytes; 41 LF.
   - `physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261029-d4-t2-nonnormal-sharp-residual-consolidated-v2.md`: SHA-256 `193bad400026692c4d806f3b4c64bd234e05b087e94d43aa32bc42346404fad8`; 12,522 bytes; 163 LF.
3. In manifest order, I displayed the disposition completely in raw windows `1–15, 16–30, 31–41`, then the candidate completely in raw windows `1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–163`. Thus both final lines were displayed, and no window exceeded 15 lines. No mathematical reconstruction or control preceded these completed displays.
4. In addition to the manifest, I consulted the mandatory workspace memory summary and the review-process skill as procedural instructions only, not as mathematical evidence. I did **not** open linked research bodies, the v1/v3 packets, f196, held material, sibling reviews, literature, web sources, or author code, or contact the author. I did not run/import/compile author code.
5. The native clock observed before writing the first control script was `/bin/date`: `2026-10-29T13:16:19-0700 PDT`; before copying and editing the second script: `2026-10-29T13:18:01-0700 PDT`; and before writing this review: `2026-10-29T13:19:27-0700 PDT`. These are observed clocks, not asserted file-creation times.

**Sequence deviation:** the first attempt to display candidate lines 151–163 accidentally used the nonexistent path `/Users/jinleic/repos/aifours/three-area-placeholder`; the read returned “Path ... not found” and displayed no body. I immediately displayed lines 151–163 from the actual pinned candidate, still before analysis or controls. This was not an additional research input. The first independent control also exited with an unexpected assertion failure, fully disclosed below; its source and receipt hash are retained. No other contract deviation is claimed.

## Per-claim verdicts

| Scoped claim | Verdict | Basis and qualification |
|---|---|---|
| `d_A≥0`; trace-zero weighted lemma (2.1), including dependent and zero vectors | **0F/0M/0m** | Weighted projection, Gram inversion, explicit rational bound and continuous limit reconstructed below. |
| Corollary (2.3), sharp (†), explicit margin and stated necessary equality conditions | **0F/0M/0m** | Algebraic decomposition and equality reconstructed; the leading constant 2 is attained. |
| Full rank-≤1 B T2 class and strict mixed-block inequality | **0F/0M/0m** | Rank-one unitary form, completion of squares, and all three singular-block cases reconstructed. |
| Lemma 4.1 for **arbitrary** `T`; displayed centered identity and (4.2) | **F — one finding** | Diagonal rational counterexample: `25/16 > 5/4`. The missing term is `c Tr(T)/2`. The correct arbitrary-T multiplicative constant is 5/4, not 1. |
| Swap identity (4.3), centered weight bound, and Lemma 4.1 **when `Tr T=0`** | **0F/0M/0m** | Independently reconstructed for the restricted hypothesis; the missing term then vanishes. This is a replacement proposition, not the arbitrary-T claim. |
| Lemma 5.1, one 2-supported **site**, including (5.2) and dual use | **0F/0M/0m** | Independent Haar decomposition and rank-≤2 `q₁` argument, with the expressly adopted f168 odd-sector identity as an admissible premise. |
| Theorem 6.1, two separately traceless reducing 2×2 blocks | **0F/0M/0m for the conclusion, after repair** | Both cross-block uses have traceless T, so the restricted inequality suffices; same-block uses Lemma 5.1. The written citation to false Lemma 4.1 must be restricted. |
| Lemma 7.1, intrinsic 4×4 square-normal classification | **0F/0M/0m** | Orthogonal spectral subspaces, nilpotent/SVD and ±μ/SVD cases, and dimension-four trace accounting reconstructed. |
| Theorem 7.2, A² normal or B² normal | **0F/0M/0m for the conclusion, after repair** | Normal case and nonnormal block case reconstructed using the repaired traceless-block bound. Includes square-zero rank ≤2 and nonnormal full-rank examples. |
| Both squares nonnormal, full T2/T3/Z2/Z3/original closure, global T2/q₂/q₃ equality or gap | **INCONCLUSIVE (I1)** | These are outside the established classes; there is no universal sign or exclusion proof here. The both-squares-nonnormal domain is nonempty. |
| External historical/provenance and literature/novelty claims | **INCONCLUSIVE (I2)** | Not investigated or adopted; linked bodies and external expansion are forbidden. Author checks and solver statuses were not used as evidence. |

## Written reconstruction

Write `F_A=||A||_F²`, `σ=||A||_op`, and use complex inner products conjugate-linear in the first argument. The definitions and equations below are reconstructed from the displayed target, not imported from the v3 packet it mentions.

### 1. Weighted trace-zero lemma and (†)

Put `t=||u||²`, `q=||v||²=1−t`, `U=[u v]`, `D=I−uu†−vv†`, and `d=Tr(A†AD)=F_A−||Au||²−||Av||²`. Since `uu†+vv†` is positive with trace 1, it is at most I, so `d≥0`. If u,v are independent then the two nonzero eigenvalues of `UU†` are both strictly between 0 and 1, hence `D>0`.

In the inner product `⟨M,N⟩_D=Tr(M†ND)`, the functional `v†Au` has representer `Z=v u†D⁻¹`, and `Tr A` has representer `H=D⁻¹`. Orthogonal projection onto `Tr A=0` and Cauchy–Schwarz give

`|v†Au|² ≤ N d`, where `N=q u†D⁻¹u−|v†D⁻¹u|²/Tr(D⁻¹)`.

Let `z=u†v`, `r=|z|²`, `Δ=tq−r>0`, and `G=U†U`. Because `Tr G=1`, `det(I−G)=Δ` and `G²=G−ΔI`. Woodbury or direct multiplication gives

`U†D⁻¹U=G(I−G)⁻¹=G²/Δ`,
`u†D⁻¹u=(t²+r)/Δ`, `|v†D⁻¹u|²=r/Δ²`, and `Tr D⁻¹=2+1/Δ`.

Consequently

`N=q(t²+r)/Δ−r/[Δ(1+2Δ)]`,
`(1+t)−N=(1+2tq−4r)/(1+2Δ)=(1−2tq+4Δ)/(1+2Δ)`.

The last quantity exceeds `1−2tq` by `(2+4tq)Δ/(1+2Δ)≥0`. Therefore `N≤t+2tq=t(1+2q)≤t+1/2`, since `tq≤1/4`. For dependent nonzero u,v, perturb v within its fixed norm to make the pair independent and pass to the continuous limit; if either vector is zero, the left side is zero. This proves (2.1) for every traceless A. For any fixed `0<t<1`, the projected representer attains N in the positive-definite case and `N→t+2tq` as `Δ→0+`; hence that t-dependent coefficient cannot be uniformly lowered there. This limiting observation does not require the singular limiting D to be inverted.

With `L=v†Au`, direct rearrangement and (2.1) give

`2F_A−[||Au||²+||Av||²+|L|²/(1+t)+σ²]`
`= (F_A−σ²)+d−|L|²/(1+t)`
`≥ (F_A−σ²)+(1−2tq)d/(1+t)`
`≥ (F_A−σ²)+d/[2(1+t)]≥0`.

For nonzero A, equality forces `F_A=σ²`, so A has rank one, and `d=0`. Since `uu†+vv†≤I` has trace 1, `d=0` forces it to have eigenvalue 1 on the top right singular vector, so u,v both lie in that vector's span (allowing a zero vector). Rank-one trace zero makes the left and right singular vectors orthogonal, and then `L=0`. Conversely those conditions do attain equality; A=0 also gives equality. In particular the coefficient 2 in (†) is genuinely sharp.

### 2. Full rank-one-B class and its mixed-block margin

A nonzero traceless rank-one B is `b|e₀⟩⟨e₁|` in a suitable local orthonormal basis, with `b>0`: its left and right singular vectors are orthogonal because `Tr B=0`. Decomposing the second site gives `X=Γ_b⊕A⊕A`, where `Γ_b=[[A,bI],[0,A]]`. For a unit `(u,v)`, using the preceding definitions,

`||Γ_b(u,v)||²=||Au||²+||Av||²+b²q+2 Re(b̄L)`.

Completing the square yields exactly

`2(F_A+b²)−[||Γ_b(u,v)||²+σ²]`
`= (F_A−σ²)+d−|L|²/(1+t)+(1+t)|b−L/(1+t)|²`
`≥ (F_A−σ²)+(1−2tq)d/(1+t)+(1+t)|b−L/(1+t)|²≥0`.

If the two largest singular values both come from Γ, their right singular plane is supported on the two-dimensional local site of Γ and the one-supported-site lemma below gives T2. If one comes from Γ and one from a complementary A block, the displayed bound applies, taking a maximizing unit Γ vector. If both come from complementary A blocks, the sum is at most `2σ²≤2F_A`. Ties may be resolved within the orthogonal block decomposition. For B=0, singular values of A occur with multiplicity four, so the same bound is immediate.

For b>0 the mixed estimate is strict: vanishing all nonnegative remainders would give `d=0`, hence `L=0` by (2.1), and the last square would then force `b=0`. Compactness of the unit sphere transfers the strict inequality to the maximal Γ singular value. This is only a mixed-block strictness result, not a global gap or global equality classification.

### 3. Fatal counterexample to the arbitrary-T swap/HS lemma

Take

`A=diag(3/4,−1/4,−1/4,−1/4)`, `T=diag(1/2,0)`.

A is traceless and both matrices are normal. The largest absolute eigenvalue of `A⊗I₂+I₄⊗T` is `5/4`, attained at `e₀⊗e₀`. Thus

`||A⊗I₂+I₄⊗T||_op²=25/16`,
`||A||_F²+2||T||_F²=3/4+2(1/4)=5/4=20/16`.

This directly contradicts (4.1). For `ψ=φ=e₀⊗e₀`, `c=1`, `M=diag(1,0,0,0)`, and `N=diag(1,0)`. Hence `M₀=A`, `N₀=diag(1/2,−1/2)`, while

`Tr(A M₀)+Tr(T N₀)=3/4+1/4=1 ≠ 5/4=⟨φ,(A⊗I+I⊗T)ψ⟩`.

The exact missing term is `c Tr(T)/2=1/4`. Also `||M₀||²+||N₀||²/2=1`, so (4.2) itself falsely asserts `25/16≤5/4` on this example. This is a mathematical counterexample, not merely a missing exposition step.

For arbitrary T, the correct weighted Cauchy–Schwarz uses N, not N₀:

`|⟨φ,Γψ⟩|² ≤ (F_A+2||T||²)(||M₀||²+||N||²/2)`
`= (F_A+2||T||²)(s₂+s₁/2−|c|²/4)`.

The swap relation and `s₂≤1`, `|c|²≤1` give

`s₂+s₁/2−|c|²/4 = s₂/2+(s₁+s₂−|c|²)/2+|c|²/4 ≤ 5/4`.

Thus a universal arbitrary-T version has multiplicative factor 5/4; the displayed counterexample attains that factor, so it cannot be decreased. This repair does **not** make the original factor-1 lemma true.

### 4. Valid traceless-T swap/HS replacement

Now impose `Tr T=0`. For unit ψ,φ, define `M=Tr₂|ψ⟩⟨φ|`, `N=Tr₁|ψ⟩⟨φ|`, `c=⟨φ,ψ⟩`, `M₀=M−cI₄/4`, `N₀=N−cI₂/2`. Both traces are c. Tracelessness of **both** A and T gives the centered identity. Weighted Hilbert–Schmidt Cauchy–Schwarz gives

`|⟨φ,Γψ⟩|²≤(F_A+2||T||²)(||M₀||²+||N₀||²/2)`.

Put `s₁=||N||²`, `s₂=||M||²`. The swap trick expresses each as the overlap of the appropriate normalized reduced density matrices of ψ and φ, so `0≤s₁,s₂≤1`. On ψ⊗φ, the positive product `(I−F₁)(I−F₂)` has expectation `1−s₁−s₂+|c|²`; hence `s₁+s₂−|c|²≤1`. Centering gives

`||M₀||²+||N₀||²/2=s₂+s₁/2−|c|²/2`
`=s₂/2+(s₁+s₂−|c|²)/2≤1`.

Taking the supremum over unit ψ,φ proves exactly the factor-1 inequality when T is traceless. It remains valid for arbitrary nonnormal A,T under these trace hypotheses.

### 5. Supported-site lemma and reduction to two 2×2 blocks

The expressly adopted f168 premises are the d=4 odd-sector identity and the one-supported-site scope, with the stated distinct-site qualification. I also reconstruct the local supported-site argument. If a rank-≤2 C has its input leg at a site in a 2-plane E, vectorizing and compressing the local reflection yields

`I⊗P̄_E−|Ω_E⟩⟨Ω_E|/2`
`=3∫|u⊥⟩⟨u⊥|⊗|ū⟩⟨ū| dμ(u)+(I−P_E)⊗P̄_E`.

Indeed the Haar second moment on E is `(I+F)/6`; after partial transpose and using `|u⊥⟩⟨u⊥|=I_E−|u⟩⟨u|`, the integral term is `P_E⊗P̄_E−|Ω_E⟩⟨Ω_E|/2`. The complement is a sum of positive rank-one product terms. Each contraction leaves a one-site matrix Y of rank at most 2, and `|Tr Y|≤√rank(Y)||Y||_F≤√2||Y||_F`, so `q₁(Y)=||Y||²−|Tr Y|²/2≥0`. Therefore `q₂(C)≥0`. Input/output orientations and site exchange are handled by adjoints and relabeling; a supported input plus output at the **same** site is not two distinct supported sites.

For `X=A⊗I₄+I₄⊗B` with traceless A,B, the d=4 trace-insertion reflection has `WX=−X`, and the adopted identity says `q₂(C)=||C||²−2||P_-C||²`. For a two-plane F in `C⁴⊗E`, set `C=XP_F`. Then `rank C≤2`, C has the required supported input site, and `⟨X,C⟩=||C||²`. If X,C are nonzero,

`||P_-C||²≥|⟨X,C⟩|²/||X||²=||C||⁴/||X||²`.

Combining with `q₂(C)≥0` gives `||XP_F||²≤||X||²/2`; the zero cases are immediate. Also `||X||²=4(F_A+F_B)`, so this gives precisely the T2 bound for a top-two right singular plane with one supported site.

If `B=B₁⊕B₂` with both 2×2 blocks traceless, write `X=Γ₁⊕Γ₂`, `Γ_j=A⊗I₂+I₄⊗B_j`. Two leading singular vectors in one block are covered by the supported-site result. If one is chosen from each, the valid traceless-T replacement gives

`σ₁(Γ₁)²+σ₁(Γ₂)²≤2F_A+2(||B₁||²+||B₂||²)=2(F_A+F_B)`.

The proof is symmetric under site exchange. This reconstructs Theorem 6.1, while explicitly repairing its dependence on the false general lemma.

### 6. Classification and the square-normal theorem

If B is normal then B² is normal. If `B=B₁⊕B₂` with each `Tr B_j=0`, Cayley–Hamilton gives `B_j²=−det(B_j)I₂`, hence B² is normal.

Conversely, let B² be normal. B commutes with B², so every eigenspace of B² is B-invariant. Their orthogonal direct sum therefore gives reducing subspaces. On the zero eigenspace, `B²=0` implies `ran B⊂ker B`; choosing orthonormal bases by an SVD of B from `(ran B)⊥` to `ran B` produces 2×2 blocks `[[0,c],[0,0]]` and zero scalar leftovers. In particular rank of a square-zero 4×4 matrix is at most two.

On the λ≠0 eigenspace choose μ²=λ. The restriction satisfies `(B−μI)(B+μI)=0` with distinct roots, so it is diagonalizable. Let `E_+=ker(B−μI)`; in the orthogonal decomposition `E_+⊕E_+⊥`, B has form `[[μI,C],[0,D]]`. The quotient has only eigenvalue −μ and satisfies `D²=λI`; the same distinct-root argument gives `D=−μI`. An SVD of C using independent unitaries within the two summands yields 2×2 blocks `[[μ,c_j],[0,−μ]]` plus scalar ±μ leftovers. Zero-coupling blocks are diagonal and may be split into scalars. Every remaining genuinely nonnormal block has dimension 2 and trace zero.

In dimension four there can be zero, one, or two such blocks. Zero gives a diagonal scalar direct sum, hence B normal. Two exhaust the space and form the required pair. One leaves exactly two scalar summands whose traces sum to zero because `Tr B=0`; together they form the other traceless 2×2 block. This proves the stated if-and-only-if classification.

For normal B, unitary diagonalization decomposes X into four invariant local-eigenvector blocks; two leading right singular vectors may be chosen from at most two of them, so the supported-site lemma proves T2. For nonnormal square-normal B, the classification yields two separately traceless blocks and the repaired Theorem 6.1 applies. Swapping A,B proves the A²-normal alternative. For a concrete full-rank nonnormal example, use the direct sum `[[1,2i],[0,−1]] ⊕ [[2,3],[0,−2]]`; its square is `diag(1,1,4,4)`. These arguments do not extend to arbitrary pairs whose squares are both nonnormal.

## Own bounded exact controls and receipts

All control arithmetic uses only this reviewer's standard-library Python code, including rational Gaussian-complex operations. The first control was not an author script, and the first failure is retained rather than hidden. Both invocations used a 115-second subprocess cap inside a 120-second tool deadline. There was no timeout; a timeout would be UNKNOWN, never an exclusion.

1. `reviewer-f198-exact-controls-v1.py`, SHA-256 `76eda2b66bce2db5570af494bd8c9a67a436cd447f7e72062713a0194241f`; interpreter `/opt/homebrew/opt/python@3.14/bin/python3.14`; native `/bin/date` start `2026-10-29T13:17:01-0700 PDT`, end `2026-10-29T13:17:01-0700 PDT`; **exit 1**. Before failure it displayed 90 rational Gram checks, exact complex Riesz saturation, 30 lemma/(†)/cross checks, and the missing-trace-zero negative. It then raised `AssertionError` at line 299 on the candidate's claimed centered amplitude identity for a nontraceless T. This was an unexpected diagnostic failure, not a passing run or a proof of a counterexample to the norm claim by itself.
2. `reviewer-f198-exact-controls-v2.py`, SHA-256 `a157ef8e671a839655dc9f732e7447ad21bd96f12f888f53f54046ecc2999848`; same interpreter; `/bin/date` start `2026-10-29T13:18:22-0700 PDT`, end `2026-10-29T13:18:23-0700 PDT`; **exit 0**, empty stderr. This preserved the first script, restricted the positive swap checks to traceless T, and added the explicit fatal arbitrary-T negative. Output: 90 rational parameter checks; one exact complex Gram/Riesz saturation; 30 exact lemma/(†)/mixed-gap cases; 25 complex swap/HS vector pairs; supported-site saturation; a nonnormal full-rank square-normal example; a rank-two square-zero example; and a both-squares-nonnormal pair. The script directly computes the fatal `25/16 > 5/4` example and the wrong centered amplitude `1 ≠ 5/4`.

Intended-reason negatives in the second script include: changing `−4r` to `−3r` in the cleared Gram identity; trying the smaller coefficient `t(1+q)` on a projected complex Riesz maximizer; dropping trace zero from Lemma 2.1, where a rank-one projection has `d=0` but `|L|²=1/4`; omitting centering in the swap factor, producing `3/2>1`; strengthening supported-site `1/2` to `1/4` at an exact saturator; and asserting square-normal implies normal, contradicted by the full-rank block example. The explicit arbitrary-T counterexample is separately checked. The nonempty both-squares-nonnormal pair is **not** represented as a violation of T2. These finite checks are controls only; the written derivations and counterexample carry the universal and falsity conclusions.

## Explicit imports, remaining gap, and assurance ceiling

The only adopted mathematical context used is the pinned f168 disposition's explicitly stated d=4 odd-sector identity and qualified one-supported-site support/dual framework, at that scope; the local calculation above also reconstructs the supported-site implication. I did not import any linked body, author PASS/receipt, solver UNKNOWN/timeout, prior packet, outside search, literature recollection, other model, sibling review, or author contact. Ordinary finite-dimensional spectral theory, SVD, Cauchy–Schwarz, the stated elementary Haar second moment, and swap positivity are used explicitly in the reconstruction.

**Remaining gap:** the pair of traceless 4×4 matrices for which both A² and B² are nonnormal is not covered by the rank-one or square-normal arguments. For example `A=2E₀₁+iE₁₂` and `B=A†` have nonnormal squares, so this domain is not empty; this example is not a T2 counterexample. Full T2, T3, Z2, Z3, the original q₃ problem, and a global equality or strict-gap statement remain unproved by this packet and this review. No solver failure or finite sampling has been used to exclude them.

This is a same-harness written review, **not** human review, independent-model-family review, formal/kernel verification, or novelty verification.
