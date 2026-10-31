# Independent checks of the published three-copy d=4 certificate data

**Observed clock before writing:** Wed Oct 28 17:08:57 PDT 2026. **Author:** PhysicsResearch96h-2 / physics-1. This is an initial bounded scientific audit, not theorem acceptance. All paths below are in the exclusive owner root unless absolute.

## Result and exact scope

For the actual d=4, three-copy data in Tomar v3's public `release_ep3.tar.gz`:

1. **Every one of the 1237 stored uncorrected dyadic multiplier matrices is symmetric and positive definite**, checked exactly by two distinct algorithms. All actual row/cut/family tags, five equality-group signatures and compression matrix shapes passed independent structural checks.
2. **Every site-local map actually used by these d4 block types matched explicit basis-index contractions**: 81,552 raw diagram-pair/permutation comparisons, plus the same number for the dimension-fixed loop formula; no mismatches.
3. **Every used auxiliary Gram compression and every specified equality compression matched independent explicit basis-index contraction**: 1224 and 648 respectively; no mismatches. The objective numerator matched independently counted literal permutation traces on all 331,776 four-factor words, with exact denominator 2,147,483,648.
4. Independently rebuilt union-find orbits on all 331,776 words in each of the three letter families matched the author verifier's orbit partition up to a bijection. Counts are 1142, 2391, 1142, total **4675**; zero partition disagreements.

**Critical limitation:** these are checks on the literal source/data and **base** multipliers. The stored data are an approximate dyadic certificate requiring exact correction. The corrected multipliers and the all-orbit identity have NOT yet been independently checked by these four scripts. They do **not** establish `q3(C)>=0`, disprove it, or certify Tomar's theorem, Lean proof, historical verifier output or novelty. A bounded author-code d4 correction/verification with an independently implemented final rational PSD check is running separately; its outcome is not represented here until observed.

## Original target and source binding

Let `H=(C^4)^tensor3` and let C be ANY complex linear map H→H of actual rank at most2, including0/1, without normality, Hermiticity, positivity, realness or product-range hypotheses. The registered target is

`q3(C)=||C||HS² − (1/2)Σ_i||Tr_i C||HS²
        +(1/4)Σ_(i<j)||Tr_ij C||HS² − (1/8)|Tr C|² >=0`,

all partial traces **unnormalized** on the indicated physical factors. The source's moment model is the same actual-object problem, not an altered norm or independently selected partial-trace tuple.

Public primary registry: [Zenodo v3 record 23682914](https://zenodo.org/records/23682914), [record API](https://zenodo.org/api/records/23682914). The previously pinned locally archived paper PDF is `tomar-werner-copies-zenodo23682914-v3.pdf`, SHA256 `fe272e67d880a67c3ae2103e4e486753541accc8f64586182df06c279545a4e5`. Its Theorem1.2/§2–4/AppendixA are the stated full-rank<=2 source and finite certificate route. Its explicit claim is prior-publication evidence, not evidence of independent correctness.

The public `release_ep3.tar.gz` was downloaded from `https://zenodo.org/api/records/23682914/files/release_ep3.tar.gz/content` into `frontier-20261028-tomar-release-ep3-v3.tar.gz`, 11,746,154 bytes, SHA256 `2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3`. Its MD5 `704bae52c2083bf81b5c11332415b3d4` matches the registry entry; this confirms the published bytes, not their correctness. The actual d4 compressed data member has SHA256 `0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f`. Author core `ep3core.py` SHA256 is `0f0d84a9ce257edbf9b0b6cbbff2690041fbd6aad18d139c8845e8edf547d450`.

The scripts read the xz pickle with a restricted unpickler which rejects every global/class lookup; no package construction code or external API is run by the data-only PSD script. `python-flint==0.9.0` was installed only under `frontier-20261028-python-deps/`; the actual Python was3.14.3 and numpy2.4.3. Every check below used one process and single BLAS/OMP threads.

## What a successful full certificate would have to prove

For every actual nonzero C, scale it to ||C||HS²=1/2 and choose an isometry A:C²→H containing its range. Put B=2C†A and a=vec(A)/sqrt2, b=vec(B)/sqrt2. Then `C=AB†/2`, `||a||=||b||=1` and `Tr_H |a><a|=I₂/2`. Conversely every such physical pair produces a normalized rank<=2 C; zero C is separate. Thus this lift covers the full original complex-rank domain.

The paper's three-family moment variables are constructed from the SAME physical a,b. Its canonical block types are whole-replica partial-transpose Gram blocks and the two coupled Gram patterns; the actual d4 file uses 1126 single-row and111 coupled Gram blocks, **no gram2 block**. The canonical equalities are three Stiefel contrasts at a replicas and the two correctly reordered common marginal families. For an actual physical moment tuple the block maps are PSD and equality maps vanish.

If concrete corrected matrices `Z_t` are PSD and their exact functional identity holds on the 4675 actual word-orbit sums, this spanning identity and the original swap objective yield q3(C)>=0 for all original C. Arbitrary compressions of a PSD Gram block remain PSD; no completeness/injectivity of the chosen compression is needed. The present checks validate exact source ingredients below, but do not assume the missing corrected-identity premise.

## Check 1 — exact uncorrected multiplier positivity and structural metadata

Script `frontier-20261028-independent-d4-base-check.py`, SHA256 `bb9cf61ea6a26c0eb4570cd28abf2c26c94f64a4054640902f84ba8e4aff69ec`. Result `frontier-20261028-independent-d4-base-check-results.json`, SHA256 `07de3138cbf0f7e3ea078efd11bfa9df4eb6270e30369abc2ac3bdec940b6d0e`. Actual runtime **1.785 s**, verdict PASS.

The stored multiplier is `Z_t=2^(−e_t) A_t` with integer A_t and positive scaling. Every flattened matrix was checked for its declared shape, integer data and exact symmetry. Two independently programmed exact tests then checked every matrix:

- FLINT integer characteristic polynomial: for real symmetric A, coefficients of det(xI+A) are all nonnegative iff A is PSD. If a negative eigenvalue existed, its absolute value would be a positive root of a monic polynomial with nonnegative coefficients; PSD gives nonnegative elementary symmetric coefficients. A positive constant term then makes a PSD matrix positive definite.
- Python `fractions.Fraction` symmetric Schur elimination: any negative diagonal or zero diagonal with a nonzero row fails; each positive pivot reduces PSD exactly to its rational Schur complement. This includes singular-pivot handling.

**Observed:** 1237/1237 positive definite by both tests, zero failures/disagreements; dimensions1–40. Canonical row-pattern/cut/family checks, integer compression shapes, five literal equality-group/slot/order/sign signatures and 272 equality-multiplier count gave zero structural errors. The correction-coordinate sets each have2634 entries. The source tuple reports4675 orbit rows; its independent reconstruction is §7.

Positive definiteness here is a fact about **stored approximate base matrices**. The proof requires PSD **after** the exact equality correction; base positivity alone does not prove a correction margin or final PSD.

## Check 2 — all USED d4 site-local diagrams against literal indices

Script `frontier-20261028-independent-d4-localmaps-check.py`, SHA256 `5ca678583772e2b904ede65b365f0efee53b82323f8ea42f0c71cf7f29b7da3b`. Result `frontier-20261028-independent-d4-localmaps-check-results.json`, SHA256 `00dc31e0cb7b06b8855449a5321d3f259a1a472d68e60e0ae2f14fa506caff62`. Actual runtime **1.098 s**, PASS.

The reference constructs each actual four-slot n=4 diagram vector as an integer sparse vector by summing its permitted contraction-index assignments. It computes the local operator entry by the literal replica permutation condition after the actual row/column rearrangement. It does **not** use the loop-count formula as its reference.

Only four author pure functions (pattern parser, entry rule, matching edges and loop counter) were isolated from the pinned source by AST and executed for comparison. All17 actual row-pair/cut rules independently passed factor-multiset matching; all84 used cut/row-pair/site-label combinations and all24 permutations were covered. The 133 distinct sparse diagram keys generated **81,552** actual diagram-pair/permutation comparisons, and another81,552 comparisons using the source's explicit fixed-dimension mode. Every literal integer matched. Since actual diagram compression matrices are fixed integer linear combinations, their corresponding site map follows by bilinearity.

This checks actual used d4 local maps, not all dimensions, unused types, auxiliary maps, global summation, correction or theorem.

## Check 3 — all USED auxiliary/equality maps and all objective words

Script `frontier-20261028-independent-d4-aux-equality-objective-check.py`, SHA256 `0949e4945fa5cd20bac6a5d4e976c6756f97a16de2fb5c6b20c759f60798e99c`. Result `frontier-20261028-independent-d4-aux-equality-objective-check-results.json`, SHA256 `dc0bab7553cab5f6de615cbf22816b8083df547d5cb07858b21e9c0860e0c6e4`. Actual runtime **4.209 s**, PASS.

The independent reference directly forms finite permutation entries, actual partial traces, the auxiliary Stiefel operator `2V_p−I_slot⊗Tr_slot V_p`, and integer compression contractions; it compares them with the pinned author core. It covers all51 used auxiliary-row/module combinations ×24 permutations = **1224**, and all actual equality compression/slot/order specifications = **648** permutation comparisons. Zero mismatches.

For the objective, independently counting actual fixed basis tuples for `Tr V_p` and `Tr(F_14 V_p)` at local dimensions4 and2 yields the tensor numerator. It was compared entrywise with the author core on **all 24^4=331776 words**. The exact denominator is `2^3(2*4^3)^4=2147483648`; zero numerator/denominator mismatches. This preserves the same physical q3 normalization.

These finite checks compare actual local maps and objective values; they do not establish the all-orbit certificate identity or that unrelated maps for another dimension are correct.

## Check 4 — complete source-word orbit partition

Script `frontier-20261028-independent-d4-orbits-check.py`, SHA256 `f15090ef47437eeb850ee29614409f92830793aae3f4637e2c9229770b6ed3cc`. Result `frontier-20261028-independent-d4-orbits-check-results.json`, SHA256 `e9d6adcd09fe816ecda624b62bf8e9be265d5862917e6b38d666046043d49618`. Actual runtime **3.164 s**, PASS.

An independent union-find uses generators for both left and right stabilizer actions of the actual family letter string, adjacent permutations of the three physical sites, and simultaneous inversion. For each of the three source families it joins all generated edges over **all 331776** words. Each family used 2,322,432 edges. Components count 1142 for31,2391 for22,1142 for13. Comparing partitions in BOTH directions—not merely counts—against author labels yields zero disagreements. This is finite source-space coverage, not an independent evaluation of the certificate coefficients on those orbits.

## Source-description discrepancy, not a mathematical refutation

The actual package files contain **715,1237,1347,1347,1347,1347** multiplier types for d=3,4,5,6,7,8 respectively, determined by data-only parsing. The paper's separate Section4/V1/V2 descriptions name715 at d3 and1237 at d4, consistent with the files and the published d4 expected log. AppendixA V17's unqualified phrase that the d3…8 package certificates each have “every one of the 1347 multipliers” does not accurately describe these two smaller files. This is a factual count/documentation inconsistency, **not** by itself an incorrect inequality, PSD failure or invalid certificate. No author contact was made.

## Remaining load-bearing predicates

- **Exact correction/NR-IDENTITY:** the fixed d4 base data are not the final certificate. Reconstruct the 2634-coordinate rational correction and verify the complete 4675 orbit-sum identity. At this writing this remains unverified by the independent scripts above.
- **Corrected PSD:** every corrected rational multiplier, not just each dyadic base, must be PSD. At this writing independently unverified.
- **Full-map aggregation:** local/aux/equality/objective maps and orbit partition passed independent finite checks, but the author's global contraction/aggregation and exact residual code have not been independently rebuilt end to end.
- **Trust:** FLINT/Python/numpy are computational dependencies. No Lean kernel build, external-model/human review or original physical experiment was performed. Existing held outcomes remain historical/unvalidated, not accepted premises.

The applicable research direction is prospective under the current owner addendum; no earlier process is retroactively declared successful. No target, d=4 convention, complex rank class or q3 normalization is changed.
