# Parent disposition: actual core-mixing PPT outputs with exact Schmidt number two

Status: ADOPTED at the proper-family scope below. Complete written reconstruction by two same-harness reviewers plus an independently authored exact finite source run once by the parent. Not independent-model-family, human, formal/kernel, novelty or unrestricted original-target acceptance.

## Actual source, physical filter and theorem

Use the displayed published 4×5 parent Q(s,r)=[A]+[B]+[D]+s([02+34]+[32]+[04])+r([20+33]+[23]+[30]), A=00+11+22, B=01+12, D=10−21. Here [v]=vv†. Throughout the adopted PPT statement, s>1, r>1 and (s−1)(r−1)>=4. The parent is PPT with exact Schmidt number3 at the corrected range-minor proof and original-source boundary already recorded in the [prior disposition](physics-3-coherent-grid-merger-entire-ppt-family-exact-sn2-parent-v1.md).

Let K_w=[I4 | w], w=(alpha,beta,gamma,0)^T with arbitrary finite complex coordinates, and n=norm(w)^2. The ACTUAL output is R_w=(I tensor K_w)Q(I tensor K_w)†=[A]+[B]+[D]+s[02+3w]+r[20+33]+s[32]+s[0w]+r[23]+r[30]. Its trace is Z_w=7+2s(1+n)+4r. The normalized physical contraction K_w/sqrt(1+n), acting on Q/T with T=7+4(s+r), succeeds with probability Z_w/((1+n)T). Both output local supports have rank4 for every w, including zero.

All such outputs are PPT in the inherited source region. The complex consuming identity uses conjugate(K_w) after Bob partial transpose, not K_w. The source region is SUFFICIENT for this filtered family; no filtered-output PPT iff claim outside that region is made.

Every such output is entangled for arbitrary w. It has EXACT Schmidt number2 on the union of:

1. the complete ellipsoid abs(beta)^2/s+abs(gamma)^2/(s−1)<=1, with alpha arbitrary complex;
2. the entire complex beta coordinate line alpha=gamma=0;
3. the entire complex gamma coordinate line alpha=beta=0.

Equality boundaries and zero coordinates are included. No infinite/projective endpoint, arbitrary fourth component of w, arbitrary filter, or uncovered parameter region is asserted.

## Complete upper and lower mechanisms

Writing U=02+alpha30+beta31, the actual fifth-root vectors V_z=zA+B−z²D+z^−1 U+beta z^−2 32 have coefficient columns C2=z^−1 C1 and C3=0, so all have complex Schmidt rank at most2. The five distinct characters give G=mean[V_z]=[A]+[B]+[D]+[U]+abs(beta)^2[32]. Then R_w=G+(s−1)[U+s gamma32/(s−1)]+delta[32]+r[20+33]+s[0w]+r[23]+r[30], delta=s−abs(beta)^2−s abs(gamma)^2/(s−1). Every residual vector has Schmidt rank at most2 and every weight is nonnegative on the ellipsoid; no division by alpha/beta/gamma occurs.

The beta line additionally has a third-root identity for T_z=A+zD+z^−1 01, with C1=z^−1 C0−z C2 and mean[T_z]=[A]+[D]+[01]. Its positive residual condition is s abs(beta)^2>=1; together with abs(beta)^2<=s it covers the entire line because s>1. The gamma line uses x=abs(gamma)^2 and the actual product-vector square s(1+x)[32+conjugate(gamma)02/(1+x)], with residual coefficient s−1+s x²/(1+x)>0. Complex conjugates are essential.

The actual filtered range matrix has rows (a+alpha h,b+beta h,c+gamma h,0), (d,a,b,0), (e,−d,a,k), (f+alpha c,beta c,g+gamma c,e). Its indexed 2×2 minors m1=a²+bd, m2=ad−be, m3=ae obey a²m1−abm2−b²m3=a^4. Thus every PRODUCT range vector has a=0 and zero physical11 entry. A positive separable decomposition must use vectors in this range, but R_(11,11)=1, contradiction. This proves SN>=2, NOT SN3. Combining with each positive upper decomposition gives exact SN2.

For nonzero w the new filter differs from the earlier extension merger under the DECLARED core/extension-preserving input gauge and invertible output changes, by the image/intersection dimensions2/1 versus1/0. This is not inequivalence under every source automorphism. Every rank4 filter with the same covered kernel span(−alpha,−beta,−gamma,0,1) equals L K_w for invertible L; invertible local filtering preserves Schmidt number in BOTH directions and preserves PPT. Physical rescaling remains necessary before interpreting probabilities.

For the literal simultaneous core-mixing member s=r=3, alpha=beta=gamma=1, Z=43, T=31, delta=1/2, and K_w/2 succeeds with43/124. The exact unnormalized marginals are [[14,0,0,3],[0,3,0,0],[0,0,8,0],[3,0,0,18]] and [[14,6,6,0],[6,9,6,0],[6,6,14,0],[0,0,0,6]], each divided by43 in the normalized output.

## Written gates, observed exact verification and corrections

- Complete [f605 author](../review-waves/f605-actual-ppt44-core-mixing-filter-and-complex-rank3-frontier/review-v1.md): SHA256 `ae433b0a756112de057db00113a3a6f1378b3c4602ef7853532078f1bf91e5a0`, 736 logical lines, full parent read.
- Complete [f625 upper/rank review](../review-waves/f625-ppt-core-mixing-ellipsoid-and-complex-rank2-decomposition-review/review-v1.md): SHA256 `ea956c6b29fd0e40c1ea1d0b84f76e90303ea9a0b1a56759f00a5470776240b4`, 393 logical lines, full parent read, 0 FATAL / 0 MAJOR / 0 MINOR.
- Complete [f626 range/physical review](../review-waves/f626-ppt-core-mixing-range-entanglement-kernel-equivalence-and-physical-member-review/review-v1.md): SHA256 `172ea6c9cf3405b173639cedcf764b66cac0475e561c213779699912364366c5`, 440 logical lines, full parent read, 0 FATAL / 0 MAJOR / 0 MINOR. Its unsupported metadata terminal-line count was withdrawn before mathematical packet access; no backdated count claim.
- Complete [f627 finite-source narrative](../review-waves/f627-ppt-core-mixing-independent-exact-physical-finite-author/author-candidate-v1.md), 126LF, and [all764 source lines](../review-waves/f627-ppt-core-mixing-independent-exact-physical-finite-author/independent-ppt-coremixing-physical-exact-v1.py), SHA256 `361760d030fff86c55e1c4642628dbee915fce91cd7c24866427a9c85f608ddd`, were parent-read before GO. The child did NOT execute scientific code.
- [Observed parent one-shot receipt](../review-waves/f627-ppt-core-mixing-independent-exact-physical-finite-author/parent-independent-finite-run-v1-receipt.json): SHA256 `10be03921c7641fdcf9b90b3d8f0547ea021b865c38fda51643fe9d0ce8f78c5`, exactly one isolated Python run, exit0, terminal success marker, empty stderr,0.810715s,55-second external deadline. No network, child launch, file mutation or deletion in the scientific source.

Exact Gaussian-rational physical calculations checked nine actual20×20-to16×16 cases, all output/partial-transpose entries, traces/probabilities, full marginals by exact LDL, complex conjugated filtering, positive sums, and one actual invertible complex output-filter congruence. Eight cases lie in the adopted PPT source region; the ninth actual s=r=2,w=0 output is NPT with a negative pivot, not an iff classification. Full matrices are retained in stdout. Exact cyclic-character-ring averages and all3×3 minors check the selected rank2 certificates without floating roots. Sparse FORMAL polynomial checks verify all three output2×2 minors, all five parent3×3 minors and both corrected a^4 identities; these are polynomial checks, not sampled identities or a proof-kernel certificate.

Nine intended-label controls rejected: wrong filter conjugation, four-root surviving cross term, wrong delta denominator, wrong ellipsoid gamma conjugation, reversed beta-coverage intervals, wrong gamma-line conjugation, wrong00-versus11 product-range obstruction, and two overclaim scope guards. The beta-coverage and two scope guards are NOT physical counterexamples. The actual nonzero product range vector0w has nonzero00 but zero11, distinguishing the valid lower-bound coordinate.

F627 made one in-place pre-return edit of its own report line11 to clarify that the native clock observation followed hashing. This violates the assigned no-overwrite instruction and is retained as a documentary/process deviation, not silently called compliant. It changed no frozen input or source science and caused no automatic full-episode mathematical hold. The [first additive disclosure](../review-waves/f627-ppt-core-mixing-independent-exact-physical-finite-author/author-report-documentary-edit-disclosure-v1.md) incorrectly ordered Main's decision versus report hashing; the [separate sequence correction](../review-waves/f627-ppt-core-mixing-independent-exact-physical-finite-author/author-disclosure-sequence-correction-v1.md) is operative. Both were fully parent-read and remain unchanged; no initial report hash or exact event time is invented.

## Original frontier and assurance limits

The actual physical transition is the specified PPT/SN3 parent to these proper-family PPT/SN2 outputs. Any Hermitian detector nonnegative on ALL complex Schmidt-rank-at-most2 vectors has nonnegative expectation on covered outputs, including invertibly filtered ones; finite detector sampling is not substituted for that premise. Negative delta outside the certificate region proves neither SN3 nor impossibility of another positive decomposition. Arbitrary fourth-component kernels, uncovered mixed beta/gamma regions, all-filter classification and unrestricted4×4 PPT/SN3 existence or impossibility remain OPEN. The prior published multiplier error/corrected-identity distinction remains; no fresh source-wide or novelty audit was performed. All held episodes and consumers remain NONINPUT.
