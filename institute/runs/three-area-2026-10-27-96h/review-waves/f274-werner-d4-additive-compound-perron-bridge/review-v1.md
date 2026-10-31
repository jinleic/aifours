The write tool refused the repository path, so `review-v1.md` was not created. Under the manifest’s fallback rule, the complete review follows.

# f274 written-math review v1

## Verdict

**SUPPORTED at the frozen written-math scope. 0 FATAL / 0 MAJOR / 0 MINOR.** All seven mathematical obligations are supported by the reconstructions below. In particular, the compression argument in (7) is valid because the compressed operator is real symmetric and J₊ is an isometry; bare entrywise nonnegativity is not the justification. No correction to the target is required by this review.

Overall correctness: **correct**, restricted to the statements actually asserted, not a global T2/T3/Z2 result. Confidence: **0.98**. This is an independent same-harness written reconstruction, not independent-model-family, human, formal/kernel, novelty, or physical-operational acceptance.

Native `/bin/date` observed before composing: **2026-10-29T19:55:17-0700 PDT**. This records an observation, not a file-creation time.

## Frozen scope and complete-read receipt

Manifest: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f274-werner-d4-additive-compound-perron-bridge/manifest-v1.json`.

The manifest’s SHA-256, bytes and LF count matched the assignment before its body was displayed. All seven declared inputs then had SHA-256, bytes and LF checked successfully in one metadata-only operation **before any input body was opened**. Every body was subsequently displayed completely, in manifest order, using exact `:N-M:raw` windows of at most 15 lines. Every file has a terminal LF. Mathematical review began only after S7 LF 91–94, including its actual ending, was displayed.

Identifiers below denote these exact paths:

- **S1:** `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261029-f198-block-bound-trace-erratum-v1.json`
- **S2:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-1-werner-stratified-duals-and-support-ladder-parent-v1.md`
- **S3:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-1-werner-d4-t2-rank-one-reduction-and-safe-classes-parent-v1.md`
- **S4:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-1-werner-d4-t2-rank-one-B-closed-square-normal-and-weighted-shift-classes-parent-v1.md`
- **S5:** `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261029-d4-t2-entrywise-perron-open-complement-bridge-v1.md`
- **S6:** `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261029-d4-perron-bridge-nonnecessity-addendum-v1.json`
- **S7 (target):** `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261029-d4-t2-additive-compound-perron-bridge-v2.md`

| Input | Verified full SHA-256 | Bytes | LF | Raw windows actually displayed |
|---|---|---:|---:|---|
| Manifest | c91a9d40228843370c016e076823d918a6800d172b96f67b33252ce87edd97f5 | 5363 | 65 | 1–15; 16–30; 31–45; 46–60; 61–65 |
| S1 | c00425bb6e64b322a251d07f03aa277dc8591c87d68c0e94ab7eacb54a544205 | 4521 | 14 | 1–14 |
| S2 | adbc15fdcccb66519353a8288993f571d9e94931ffae23c77f7a01da3d8579bf | 7488 | 41 | 1–15; 16–30; 31–41 |
| S3 | 1eebc50e0ec0a17e92294b548344edf271c1c1516e57956fdb2cf6cece2c8049 | 5100 | 22 | 1–15; 16–22 |
| S4 | 2d479e9f48f707eba0ae98fe0689976fc32e6b1b04075176c261be35c819db30 | 5286 | 22 | 1–15; 16–22 |
| S5 | ee03876158c521fc74d365ec31b4cdd95237cbac6c5e59beb5cbfa4efac27728 | 8474 | 80 | 1–15; 16–30; 31–45; 46–60; 61–75; 76–80 |
| S6 | 548dcdd440f430b5548bcd6c746d5e1a6bcea62b6ec79694c5a2dac35dede509 | 1762 | 10 | 1–10 |
| S7 | 037649140175113fbfb955bf3c25f74affc057e2ab5edc83f759634a96012d1f | 9195 | 94 | 1–15; 16–30; 31–45; 46–60; 61–75; 76–90; 91–94 |

S1–S4 are the declared erratum/adopted-scope boundaries, S5 is the declared superseded predecessor, S6 its limitation, and S7 the sole target. No links in them were followed; no held, withdrawn, protected, ZERO, sibling-review, or other undeclared research body was opened. Mandatory assistant memory/protocol guidance was read before packet intake, but supplies no mathematical premise here. No external source, model, or additional reviewer was consulted.

## Per-claim dispositions and written reconstruction

### 1. SUPPORTED — original scaling and second additive compound

**Locations:** S2 LF 5–9; S3 LF 3; S7 LF 9–21, especially equations (1)–(2) at LF 15 and 19.

For traceless A,B, the cross term in the squared Frobenius norm of X vanishes:

`||X||F² = 4||A||F² + 4||B||F² + 2 Re(conj(Tr A) Tr B) = 4L`.

Thus the adopted half-Frobenius Ky-Fan obligation is precisely `σ₁²+σ₂² ≤ 2L`.

Let J₋ map the pair coordinate (i,j), i<j, to `(e_i⊗e_j−e_j⊗e_i)/√2`. Directly expanding `J₋†(H⊗I+I⊗H)J₋` gives

`h_ik δ_jl + h_jl δ_ik − h_il δ_jk − h_jk δ_il`,

with the signs in (1). The antisymmetric space is invariant under the tensor sum, so this compression is its restriction. If `H u_i = h_i u_i`, then `u_i∧u_j` is an eigenvector with eigenvalue `h_i+h_j`. These vectors give all 120 dimensions, including multiplicities. With `H=X†X`, all h_i are nonnegative, K is PSD, and its largest eigenvalue is exactly `h₁+h₂ = σ₁(X)²+σ₂(X)²`. No multiplicative-compound identity is being substituted.

### 2. SUPPORTED — Theorem 2.1 and minimization over local bases

**Locations:** S7 LF 25–42, equations (3)–(4).

For any unit complex z and Hermitian K, triangle inequality gives

`|z†Kz| ≤ Σ_ab |z_a||K_ab||z_b| = |z|ᵀ|K||z|`.

Since |K| is real symmetric, its Rayleigh quotient is at most `λ_max(|K|)`, which equals `ρ(|K|)` because it is entrywise nonnegative. Also `|||z|||₂=1`. Taking a top eigenvector of the PSD K gives `σ₁²+σ₂² ≤ ρ(R_UV)` for every U,V.

Writing `W=U⊗V` shows `X_UV=W X W†`, so the singular values and L do not change. Matrix products, entrywise modulus, and the largest eigenvalue of a real symmetric matrix are continuous. Therefore `ρ(R_UV)` is continuous on compact `U(4)×U(4)` and attains its minimum. Taking that minimum gives `σ₁²+σ₂² ≤ η`, which is exactly the stated gap bound after subtracting from 2L. A negative lower bound is allowed and supplies no counterexample or automatic certificate.

### 3. SUPPORTED — positive-vector certificate and reducible case

**Locations:** S7 LF 44–48; predecessor S5 LF 42–52.

For w>0, set D=diag(w). The nonnegative matrix `D⁻¹ R D` has row sums `(Rw)_i/w_i`. Hence (5) implies `ρ(R) ≤ max_i (Rw)_i/w_i ≤ 2L`. If every component is strict, the finite maximum is strictly below 2L and the Ky-Fan gap is strictly positive.

Conversely, suppose `ρ(R)<s`, where `s=2L`. This premise itself forces s>0. The convergent finite-dimensional Neumann series

`w=Σ_{k≥0} R^k 1/s^{k+1}`

has every entry positive because its k=0 term is positive. Multiplying the series gives `Rw=sw−1<sw`. Nothing requires an irreducible matrix or a strictly positive Perron eigenvector. At L=0, A=B=0 and R=0; the non-strict certificate remains true for any w>0, whereas the strict premise cannot occur.

A certified nonnegative upper matrix bounds R by the same positive-vector argument. Under strict slack, both the upper matrix and w can be chosen rational sufficiently close to their real values; this is a possible certificate representation, not an executed exact checker for arbitrary input data. The packet appropriately makes no execution claim.

### 4. SUPPORTED — identity (7), compression, and comparison with γ

**Locations:** S7 LF 52–70, especially LF 60–68 and equation (7) at LF 62.

For equal pair indices (i,j), the diagonal entry of K is `h_ii+h_jj`; it is nonnegative because H is PSD. For distinct pair indices, disjoint pairs give zero and pairs sharing exactly one index give a single term `±h_ab`. There are no sums of competing off-diagonal terms whose absolute value could spoil (7). Thus replacing the antisymmetric pair vectors with the symmetric hard-core vectors changes precisely those single-term signs, while replacing H by |H| takes their moduli. The resulting compression has diagonal `h_ii+h_jj` and off-diagonal entries exactly |K_ab|, proving (7).

For the spectral step, write `C=|H|` and `N=C⊗I+I⊗C`. Here C and N are **real symmetric**, not merely nonnegative, and `J₊†J₊=I`. Consequently, for every unit v,

`(J₊v)ᵀN(J₊v) ≤ λ_max(N)`.

Since R is also real symmetric nonnegative, this yields

`ρ(R)=λ_max(R) ≤ λ_max(N)=2λ_max(C)=2ρ(C)`.

The hard-core space need not be invariant under N; the isometric Rayleigh argument is sufficient. There is no appeal to an invalid general spectral-radius theorem for compressions of arbitrary nonnegative matrices.

Entrywise,

`C_ij = |Σ_k conj(X_ki)X_kj| ≤ Σ_k |X_ki||X_kj| = G_ij`.

For any unit real v,

`vᵀCv ≤ |v|ᵀC|v| ≤ |v|ᵀG|v| ≤ λ_max(G)`.

Taking the maximum proves `ρ(C)≤ρ(G)`. This explicitly uses symmetry/nonnegativity, and does not require C to be PSD.

Thus `ρ(R_UV)≤2ρ(G_UV)` for every common basis choice. Evaluating this inequality at a minimizer of G gives `η≤2γ`; together with claim 2, `σ₁²+σ₂²≤η≤2γ`. This minimization step does not interchange incompatible extrema.

### 5. SUPPORTED — normal exactness and the nonnecessity family

**Locations:** S7 LF 74–78, equation (8); S6 LF 6–8.

When A and B are normal, independent local diagonalizations make X diagonal, H diagonal nonnegative, and K diagonal with entries `h_i+h_j≥0`. Therefore the majorant has spectral radius exactly `σ₁²+σ₂²` in that basis. Claim 2 supplies the reverse inequality for every basis, proving (8).

For completeness, normal-pair T2 itself follows directly from traceless diagonal eigenvalue lists a,b. For any two distinct product indices, the two functionals `(a,b)↦a_i+b_j` have Gram diagonal 3/2 on the traceless lists. Their mutual Gram entry is +1/2 if one index is shared and −1/2 if neither is shared. The largest Gram eigenvalue is 2 in either case. Hence the sum of any two selected squared diagonal entries is at most `2(||a||²+||b||²)=2L`. This is consistent with, and does not expand, the adopted normal class.

For arbitrary rank-one orthogonal P, `4P−I` has eigenvalues 3 once and −1 three times. On `P⊗P`, the two mixed projection sectors, and `(I−P)⊗(I−P)`, respectively, X has eigenvalues **6t once, +2t six times, and −2t nine times**. Thus the stated fifteen small singular values have the correct multiplicity. Each factor has Frobenius square `12|t|²`, so

- `L=24|t|²`,
- `σ₁²=36|t|²`,
- `σ₁²+σ₂²=η=40|t|²<48|t|²=2L` for t≠0.

For every basis, `||X||op ≤ || |X| ||op`, with the inner absolute bars denoting entrywise modulus; equivalently `ρ(G_UV)≥36|t|²`. Therefore `γ≥36|t|²>L`. In fact a diagonalizing basis attains 36|t|², though only the lower bound is needed. S6’s old-certificate nonnecessity claim and S7’s strict improvement are both supported without any selected physical q-value.

### 6. SUPPORTED — strict open region outside the named f215 pair classes

**Locations:** S4 LF 11–16; S5 LF 56–74; S7 LF 82–88.

**Symbolic base family.** Here `S=|3><0|+ε|0><1|`, so `S²=ε|3><1|` for every ε>0. This square is nonzero nilpotent and nonnormal, and S has rank two. For 0<ε<1 its squared singular values are `1,ε²,0,0`; hence `||S||F²=1+ε²` and `L_ε=2(1+ε²)`.

**Grade blocks and strict Perron slack.** Let E_k be spanned by `|i,k−i>` with indices modulo four. X maps E_k into E_{k−1}. With output row r and input column i, its block has entry

`a_i δ_{r,i−1}+a_{k−i} δ_{r,i}`.

Thus each block has the four distinct nonzero entries 1,ε,1,ε and Frobenius square L_ε. The full cyclic-bidiagonal pattern is an eight-cycle, so its subgraph has no four-cycle and all row/column degrees are at most two. Four edges with those degree bounds cannot form a single-row or single-column star; they contain two edges with distinct rows and columns. Their 2×2 minor cannot have both cross edges present, since that would create a four-cycle. The minor is nonzero, proving block rank at least two. Consequently each block’s largest squared singular value is strictly below its Frobenius square. Orthogonality of grade domains and images gives

`||X||op²=max_k ||X|E_k||op²<L_ε`.

All entries are nonnegative, so M=X and `ρ(G)=||X||op²<L_ε` in this fixed basis. It follows that `γ<L_ε` and `η≤2γ<2L_ε`. No equality classification or numerical target evaluation is needed.

**Strict failure of the old spectral tests.** Each tail is `s_A=s_B=ε²`, whereas `2||A||op||B||op=2`, so the tail sufficient inequality fails strictly for 0<ε<1. In the variance expression, let

- `a=||A||F²`, `b=||B||F²`,
- `p=Tr[(A†A)²]`, `q=Tr[(B†B)²]`,
- `z=Re(conj(Tr A²) Tr B²)`.

Expanding H² using the trace-zero hypotheses gives `Tr H²=4(p+q)+4ab+2z`. The 16-eigenvalue variance bound is

`σ₁²+σ₂²≤L/2+sqrt[(7/4)(Tr H²−L²)]`;

requiring its right side to be at most 2L gives exactly the sufficient test recorded in S4 LF 16:

`14(p+q)+7z≤8(a²+b²)+2ab`.

At this family, `a=b=1+ε²`, `p=q=1+ε⁴`, and `Tr A²=Tr B²=0`, so z=0. The test’s left side minus right side is

`28(1+ε⁴)−18(1+ε²)²=10−36ε²+10ε⁴`,

strictly positive for all sufficiently small positive ε by continuity at zero. These failures are failures of sufficient tests, not failures of T2.

**Full-dimensional complement.** In the fixed identity basis just used, `ρ(R)<2L` is an open condition because R and its largest eigenvalue are continuous. The nonzero commutators of the squares, a nonzero rank-two minor, and both strict test failures also persist in a sufficiently small open neighborhood in `sl₄(C)×sl₄(C)`.

For each permutation σ, the zero-diagonal weighted-partial-permutation matrices can be parameterized smoothly by U∈U(4) and up to four complex weights, setting weights at fixed points to zero. Partial injections extend to permutations with zero added weights, so these finitely many parameterizations cover P. Their domain dimension is at most `16+8=24<30=dim_R sl₄(C)`. Every image point is a critical value; applying Sard in countably many manifold charts shows that each image, and hence their finite union P, has measure zero and empty interior. Compactness of the weights’ parameter space is not assumed in this step.

P is nevertheless closed: in a convergent sequence, choose a subsequence with a single permutation, extract a convergent unitary subsequence, and use `Σ|a_i|²=||A||F²` to bound and extract the weights. The limiting representation remains zero-diagonal of the same permitted pattern. Thus P is closed nowhere dense. The rank≤1 locus is also proper closed algebraic; square-normality is a proper closed real-algebraic condition, witnessed to be proper by the displayed S².

Removing P in each factor, together with the rank≤1 loci, from the nonempty strict neighborhood leaves a nonempty **open** subset: the excluded sets are closed nowhere dense, including after lifting to either factor of the product. Both square conditions and both spectral-test failures were already strict throughout the neighborhood. Cyclic shifts are contained in P, normal factors are square-normal, and the rank-one pair classes are avoided by requiring rank>1 for both factors. This proves precisely the claimed full-dimensional open portion outside the listed f215 pair classes/tests, not coverage of their entire complement. The restricted 4×2 lemma is not an additional 4×4 pair class to subtract.

### 7. SUPPORTED for dependency/scope; INCONCLUSIVE for historical provenance

**Locations:** S1 LF 7–11; S4 LF 3–7 and 18; S5 LF 78–80; S6 LF 8–9; S7 LF 3–5 and 90–94.

The reconstructed proofs use trace-zero scaling, exterior powers, elementary absolute-value and spectral inequalities, the symbolic cyclic grading, continuity, and the explicitly named smooth-image/Sard fact. None uses the arbitrary-T 4×2 lemma or trace removal involving such a T. The correction in S1 is respected; neither the withdrawn arbitrary-T version nor a linked withdrawn body was used as evidence.

S7 explicitly withholds global `η≤2L`, necessity of the certificate, T2/T3/Z2 closure, global equality classification, novelty, formal verification, and operational acceptance. Its statement that certificate failure is not a T2 counterexample is correct for a one-sided majorant. The new results do not modify the declared parent dispositions.

Author statements about past exposure, who read which earlier review, the absence of other historical reasoning, and the stale-checkpoint correction are **INCONCLUSIVE provenance** under this closed packet. No external record was opened to corroborate them, and none is needed as a mathematical premise. This is an assurance boundary, not an identified mathematical defect.

## Findings and open items

- **Findings:** none; **0 FATAL / 0 MAJOR / 0 MINOR**. No LF-located correction is requested. The potentially delicate locations S7 LF 60–68 and LF 84–88 are supported for the explicit reasons above.
- **Intentional mathematical residual:** the universal claim `η(A,B)≤2L` is unproved here. Pairs outside the certified region, certificate necessity, the full both-squares-nonnormal complement, T3/Z2, and global equality remain outside this review’s supported conclusions. They are not missing steps in the scoped sufficient-certificate proof.
- **Provenance/open acceptance:** historical exposure assertions remain inconclusive; novelty, independent-family, human, formal/kernel, and physical-operational acceptance were not performed or inferred.
- **Verification actually exercised:** manifest/input SHA-256, byte and LF checks; complete raw packet display; and the written all-variable reconstructions above. No executable mathematical control, author code, target-instance evaluation, selected q-value, network access, build, or test was run. Therefore no optional control script or receipt is claimed or required.
- **Protocol:** no mathematical consideration preceded the completed packet read, and no timestamp was backdated. No input, source, disposition, ledger, or README was modified. This review is the only requested output; the repository-write refusal is reported above, with the complete review returned under the manifest’s fallback rule.
