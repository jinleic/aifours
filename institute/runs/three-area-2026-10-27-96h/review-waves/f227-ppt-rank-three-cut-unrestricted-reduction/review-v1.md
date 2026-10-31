# f227 written scientific review

## Disposition and severity

The residual deductions below are mathematically supported **conditional on the named imports where stated**; this is not a verification of those external theorems. I found no FATAL, MAJOR, or MINOR defect in the reviewed deductions at their stated scope. The items marked INCONCLUSIVE are not established unconditionally from the declared mathematical inputs, or concern novelty rather than validity. “No finding” means no FATAL/MAJOR/MINOR mathematical finding and no INCONCLUSIVE finding **within the explicitly stated hypotheses**; it is not a claim of formal verification or novelty.

| Claim | Severity / disposition |
|---|---|
| General Schmidt-number projection inequality, including zero | No finding in the written argument. This is PRIOR-CLAIM, not a new discovery; the zero convention is explicit. |
| Extreme normalized PPT-state selection | No finding, for a normalized 4-by-4 PPT input of Schmidt number at least 3. |
| Possible local ranks | INCONCLUSIVE without external import I; valid conditional on I. |
| Birank lower bounds and numerical census | INCONCLUSIVE without I and II; valid conditional on I and II and extremality. The dimension inequality itself has no finding. |
| Edge/other-marginal lemma | No finding, under its extreme, entangled, PPT and full-other-marginal hypotheses. |
| Full-local codimension-one cuts are nonzero PPT entangled with full cut local ranks | No finding, conditional on the existence of the stated full-local extreme target; no external import is needed for this implication. |
| Cut ranks, fiber bounds and rank-5 CES conclusions | INCONCLUSIVE without II, and the selected-state census additionally uses I; the stated implications hold conditional on these imports. The fiber rank identity itself has no finding. |
| One separable cut prunes Schmidt number at least 3 | No finding, including the zero-cut corner; independent of PPT and I–II. |
| Novelty of the residual edge, fiber and extreme-birank deductions | INCONCLUSIVE. No comprehensive prior-art review is permitted or claimed. |

The result is a necessary-condition reduction: it neither constructs a 4-by-4 witness nor proves a global no-go. Only the deductions actually proved below are assessed; the external papers and the parent source-match record are not accepted as proofs by virtue of their citations or receipts. Same-harness review is not independent-model-family, human, formal/kernel, or novelty verification.

## Exact premises, imports, and attribution

Write `SN(0)=0`; for nonzero PSD operators Schmidt number is the least maximum Schmidt rank among finite PSD rank-one decompositions. All rank-three projections in the 4-by-4 statements are **orthogonal** local projections. Partial transpose `Gamma` is on Bob, with conjugation relative to its chosen basis.

* **Import I, conditional:** Yang–Leung–Tang, arXiv:1603.03534v1, Corollary 3.6, as stated in the target: every 3-by-3 PPT state has Schmidt number at most 2. It is used to exclude the selected state's `(3,3)` local-rank branch, not to assert anything about every 3-by-4 PPT state. Its source body was not a declared input and was not opened or proved here.
* **Import II, conditional:** Chen–Djoković, arXiv:1301.2372v1, Proposition 5(i), as stated in the target: a bipartite PPT entangled state has rank strictly greater than the larger of its two local marginal ranks. It is applied separately to the state and to its PPT-entangled partial transpose, and later to the relevant PPT-entangled cuts and their partial transposes. Its source body was not a declared input and was not opened or proved here.
* The mandatory correction and status record report that Chen–Yang–Tang, arXiv:1609.05100v1, Lemma 15(i),(ii),(v) and Lemma 33(iii), prior-claim the nonzero projection inequality/lift, the specified PPT separable-codimension-one-cut consequence, and the rank-at-least-five obstruction. The source itself was not a declared input and was not read here. These records are provenance/status only, **not imported proofs**. In particular, the target's independently reconstructed Schur proof and its `SN(0)=0` treatment do not establish novelty. The below rank bounds instead follow conditionally from I–II. The residual claims' novelty remains unestablished.

## Claim-by-claim reasoning

### 1. Projection inequality and zero corner — no finding; PRIOR-CLAIM

Let Alice's local space split as `P A` plus its `t`-dimensional orthogonal complement, and let

`rho = [[A, B], [B*, D]]`, with `A = (P tensor I) rho (P tensor I)` on its retained space.

If `A=0`, positivity forces `B=0`: each zero diagonal quadratic form has a zero row/column, or equivalently the two-by-two quadratic polynomial in a retained and a deleted vector must remain nonnegative for all scalar coefficients. Thus `rho` is supported on the deleted `t`-dimensional Alice factor, so `SN(rho) <= t = SN(0)+t`; this includes `rho=0` and `t=0`. A nonzero cut is therefore not silently assumed.

If `A != 0`, put `s=SN(A)` and choose `A=V V*`, with every column `v_i` of `V` having Schmidt rank at most `s`. PSD block-matrix positivity gives `range(B) subset range(A)` and `D-B* A^dagger B >= 0`. With `C=B* A^dagger V`, `V C*=B` and `C C*=B* A^dagger B`. Thus

`rho = sum_i [v_i direct_sum c_i] + diag(0, D-B* A^dagger B)`.

Each first term has Schmidt rank at most `s+t`; the PSD remainder decomposes into vectors supported on the `t`-dimensional deleted Alice factor, with Schmidt rank at most `t`. Hence `SN(rho) <= SN(A)+t`. Local compression of each rank-one term cannot increase its Schmidt rank, including terms that compress to zero, so `SN(A) <= SN(rho)` as well. The same proof works with the parties swapped. Normalization is unnecessary.

For a codimension-one **separable nonzero** cut, `SN(rho)<=2`; for a zero cut, the sharper `SN(rho)<=1` holds. If `rho` is additionally PPT and entangled, the cut cannot be zero, its partial transpose is separable, and the same lift applied to `rho^Gamma` and the appropriately conjugated cut yields `SN(rho)=SN(rho^Gamma)=2`. This latter PPT-entangled conclusion, like the projection inequality/lift, is recorded as PRIOR-CLAIM, not novel.

### 2. Extreme-state selection and local ranks — no finding for selection; I-dependent thereafter

The normalized Schmidt-number-at-most-2 set is the convex hull of the compact set of normalized pure vectors of Schmidt rank at most 2 and is compact in finite dimension. A normalized PPT state `rho` with `SN(rho)>=3` lies outside it. Strict finite-dimensional convex separation produces a Hermitian `W` nonnegative on that set and negative on `rho`; in particular `W` is 2-block-positive. The normalized PPT set is compact and convex. A minimizer of `Tr(W .)` lies in its nonempty minimizing face; choosing an extreme point of that face gives an extreme point `rho_*` of the entire PPT set with negative witness value, hence `SN(rho_*)>=3`.

Positivity implies the state is supported on the tensor product of the supports of its two marginals, so its Schmidt number cannot exceed either local rank. Since both local ranks are at most 4 and at least 3, their only possibilities are `(3,3)`, `(3,4)`, `(4,3)`, and `(4,4)`. Applying **I** after restricting by local isometries to the local supports excludes `(3,3)`. Therefore the advertised three branches follow only conditional on I. The existence of the extreme state alone did not use I or II.

Bob partial transposition changes the Bob marginal to its transpose and leaves Alice's marginal unchanged, so both local ranks are preserved. It maps separable PSD operators to separable PSD operators and is involutive; since `rho_*` is PPT entangled, `rho_*^Gamma` is also PPT entangled. Under **II**, both `r=rank(rho_*)` and `s=rank(rho_*^Gamma)` exceed the larger local rank 4, hence `r,s>=5`. No claim that `SN(rho_*^Gamma)>=3` is needed or established.

### 3. Extreme birank dimension and arithmetic — no finding conditionally

Work in the `m`-by-`n` local support, where `(m,n)` is one of the I-permitted branches. For non-real support subspaces one may first choose local bases making those supports coordinate subspaces, or equivalently regard Bob's transposed support as its conjugate; this does not change PPT, extremality, Schmidt number, or ranks. The restricted normalized state is extreme in the restricted PPT set, because any such decomposition would also be a decomposition in the ambient 4-by-4 PPT set.

The real Hermitian subspace supported on `range(rho_*)` has dimension `r^2`; the inverse partial-transpose image of the real Hermitian subspace supported on `range(rho_*^Gamma)` has dimension `s^2`. Both lie in real dimension `(mn)^2`, so their intersection has dimension at least `r^2+s^2-(mn)^2`. It contains `rho_*`. If the intersection had dimension at least 2, subtracting the appropriate multiple of normalized `rho_*` from an independent member would give a nonzero traceless `H` in it. For sufficiently small nonzero real `epsilon`, both `rho_* +/- epsilon H` and their partial transposes remain PSD: the perturbations act only on the respective supports, where the unperturbed operators are positive definite. These are distinct normalized PPT states averaging to `rho_*`, contradicting extremality. Thus

`r^2+s^2 <= (mn)^2+1`.

For `(m,n)=(3,4)` or `(4,3)`, this is `r^2+s^2<=145`; combining with the II-derived `r,s>=5` yields `r,s<=floor(sqrt(120))=10` and `min(r,s)<=8`. For `(4,4)` it is `r^2+s^2<=257`, yielding `r,s<=floor(sqrt(232))=15` and `min(r,s)<=11`. These are necessary numerical constraints, not a claim that any listed pair is realized. The dimension inequality itself does not need I or II; the three-branch and numerical lower-bound census does.

### 4. Extreme edge/other-marginal lemma — no finding

Let an extreme entangled PPT state have full-rank marginals on its local spaces. Take normalized `a` on Alice, `P=I-[a]`, and suppose the Bob marginal of `sigma=(P tensor I)rho(P tensor I)` has a nonzero kernel vector `b`. Normalize `b` if desired. Positivity and vanishing of its Bob-marginal quadratic form give `rho|x,b>=0` for every `x perpendicular a`: each diagonal term in the retained Alice basis is nonnegative and must vanish, and a zero quadratic form for a PSD operator implies the vector lies in its kernel. Because `sigma^Gamma=(P tensor I)rho^Gamma(P tensor I)` is PSD and its Bob marginal is the transpose of that of `sigma`, likewise `rho^Gamma|x,bar b>=0` for every such `x`.

The full Bob marginal is essential: it gives `<b|rho_B|b> > 0`. All terms from `x perpendicular a` vanish, so `<a,b|rho|a,b> > 0`. For arbitrary `c` and `x perpendicular a`, partial-transpose matrix elements give

`<x,c|rho|a,b> = <x,bar b|rho^Gamma|a,bar c> = 0`.

Thus `rho|a,b> = |a> tensor v` for a **nonzero** `v`; indeed `<b|v> > 0`. The analogous identity, using the kernel of `rho`, plus Hermiticity gives `rho^Gamma|a,bar b> = |a> tensor bar v`. Thus a nonzero product vector `p=|a,v>` lies in `range(rho)` and its Bob-conjugate `p^Gamma=|a,bar v>` lies in `range(rho^Gamma)`.

For any PSD operator, a sufficiently small positive multiple of a rank-one projector onto a vector in its range may be subtracted while preserving PSD; for instance the admissible positive coefficient is bounded by the reciprocal of the appropriate pseudoinverse quadratic form. Choose one coefficient small enough for **both** `p` and `p^Gamma`, and small enough to leave positive trace. After normalization, this writes the original state as a nontrivial convex combination of a pure product state and another PPT state. The two terms cannot coincide because the original state is entangled. This contradicts extremality. Therefore every Alice codimension-one projection has full Bob cut marginal. Swap parties for the Bob-side result, taking account of conjugation on the transposed side.

The hypotheses cannot be discarded by this proof. If the original other marginal has a kernel then `<a,b|rho|a,b>` can be zero and the constructed `v` can vanish. For a concrete illustration that PPT and full marginals alone do not suffice, `( [00] + [11] )/2` has both marginals full rank on 2-by-2 but projection onto Alice's `|0>` leaves a rank-one Bob marginal; it is separable and non-extreme, so it does not meet the lemma's hypotheses. Also, subtraction alone contradicts extremality only after showing the decomposition is nontrivial; entanglement supplies this step.

### 5. Full-local cuts and fiber implications — no finding conditional on II where used

Suppose the selected `rho_*` is in the full-local `(4,4)` branch, and let `P=I-[a]` be any Alice rank-three orthogonal projection. Its retained Alice marginal is positive definite on `P A` because `rho_{*,A}` is positive definite; the edge lemma makes the other marginal rank 4. The cut is PPT and has local ranks `(3,4)`. The projection bound gives `SN(sigma)>=SN(rho_*)-1>=2`, so it is nonzero and entangled. Its partial transpose is also PPT entangled and has the same two local ranks. **II**, applied to each, gives both cut ranks at least 5. Every Bob rank-three cut has `(4,3)` local ranks and the same conclusions. For a Bob projection `P_B`, the partial-transposed cut uses `bar P_B`, not `P_B` unless it is real.

For any orthogonal projection `T` and PSD `rho`,

`rank(T rho T) = rank(T rho^(1/2)) = dim(range(rho)) - dim(range(rho) intersect ker(T))`.

The equality follows because `range(rho^(1/2))=range(rho)`. Consequently, with `R=range(rho_*)` and `R_G=range(rho_*^Gamma)`, the II-derived lower bounds give, for each Alice line `C a`,

`dim(R intersect (C a tensor B)) <= r-5` and `dim(R_G intersect (C a tensor bar B)) <= s-5`.

For each Bob line `C b`, the corresponding inequalities use `A tensor C b` for `R` and `A tensor C bar b` for `R_G`. These are all-line statements; they are not merely generic-projection statements. If `r=5`, every such `R` fiber vanishes, so any nonzero product vector in `R` would be a contradiction. Thus `R` is completely entangled. The same argument with the conjugated fibers gives a completely entangled `R_G` when `s=5`. No conclusion about the existence of either rank-5 case is drawn.

The packet's displayed fiber proof is explicitly in the full-local branch. If its summary is read as asserting the rank-5 CES conclusion for **all three** selected branches, that conclusion also follows from the declared premises, with this additional step: in a `(3,4)` branch, regard the state on its actual 3-by-4 local support and project the 3-dimensional side onto the orthogonal complement of any line, producing a codimension-one rank-2 cut on that support. The edge lemma gives the other marginal rank 4, the retained marginal has rank 2, and the Schmidt lift makes the cut PPT entangled. II gives rank at least 5 for the cut and its partial transpose. The same fiber identity then rules out all product vectors in `R` when `r=5` and in `R_G` when `s=5`. In a `(4,3)` branch use the 3-dimensional Bob support and conjugate the Bob line for `R_G`. This is an internal-support codimension-one cut, not an assertion that the original full 4-dimensional ambient projector has rank 3. Thus the global selected-state CES reading is also conditionally justified, without implying that any branch or rank is realized.

### 6. Direct pruning — no finding, including zero

Independently of I, II, extremality, and PPT, any separable nonzero codimension-one local cut has Schmidt number 1, so the lift gives `SN(rho)<=2`. If that cut is zero, the zero case gives `SN(rho)<=1`; for example, `rho=[a] tensor tau` is killed by projection onto `a`'s orthogonal complement and is separable. Contrapositively, a 4-by-4 PSD state of Schmidt number at least 3 has every rank-three local orthogonal cut nonzero and entangled. The converse is not claimed: entanglement of all such cuts does not itself establish Schmidt number at least 3.

## Record integrity and actual read sequence

The first research artifact was the manifest. Its whole-file SHA-256 was measured as `84720f9d2ca3ac1e2b89c330d15f5e83b7755b83b2aa803fd295a8a2f2507e07` (3,583 bytes, 37 LF), matching the assignment. It was displayed in raw requested windows `1–15`, `16–30`, and `31–45` (the last actually ends at line 37). Administrative memory/skill material was read separately before research; no undeclared mathematical source body was read.

Before displaying any declared input body, all three complete inputs were measured in manifest order and matched their declared SHA-256, bytes, and LF counts; each has a terminal LF. Then every body was displayed completely, in this actual order and in raw windows of at most 15 lines, including its final line:

1. Mandatory correction: `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/frontier-20261029-rank3-cut-prior-art-correction-v1.json`; SHA-256 `12661773a946b2400a8be1f28a76a9e976f45feffdbfcc473d42d78d8d5f1ba9`; 1,955 bytes; 10 LF; window `1–10`.
2. Parent prior-status record, provenance only: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/parent-ppt-rank3-cut-public-prior-status-v1.json`; SHA-256 `4b3d7c12bbb1437b8b3f97d17830a38f4997bdd36d5ba8923ef40931eba8d45e`; 2,661 bytes; 27 LF; windows `1–15`, `16–27`.
3. Target packet: `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/frontier-20261029-unrestricted-ppt-rank3-cut-reduction-v1.json`; SHA-256 `6681aab43c26c7e6b41eb0a2fe772f97f5fa777825429e6a167017bdc5e02033`; 6,500 bytes; 14 LF; window `1–14`.

Mathematical analysis started only after the last window was displayed. No reviewer computation/control was run or created; no author code, external literature body, held material, sibling review, solver result, or author contact was used. No build, lint, test suite, or formatter was run. There was no process deviation from the declared source order, full-body coverage, or proof-evidence restriction.

## Residual gap

The imports I–II were not independently reconstructed or inspected; conditional deductions must not be promoted to unconditional verified theorems on this review alone. Even assuming both imports, these necessary conditions neither exhibit an unrestricted 4-by-4 PPT state of Schmidt number at least 3 nor rule all such states out. The correction establishes a prior-claim attribution only through declared provenance records, and neither those records nor this review settle novelty of the remaining deductions.
