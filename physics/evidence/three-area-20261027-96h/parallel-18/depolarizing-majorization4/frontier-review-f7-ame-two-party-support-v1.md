# f7 — scientific review of the 60-term AME two-party obstruction

**Verdict: NO_SUBSTANTIVE_DEFECT at the specified scope** for the universal no-Hamming-one/two-invertible-party lemma, its application to the specifically transcribed 60-term tensor, and the one-party unitary 60/78 classification. This is a same-harness written review plus one independently written exact implementation, **not** a formal proof, independent-model/human review, novelty clearance, or finding about the unrestricted AME minimum. The candidate's depth-2/depth-3 search claims and prior checker implementations were not independently replayed or audited.

Native prewrite observation: **Wed Oct 28 17:19:56 PDT 2026**; not an inferred completion or delivery clock.

## Scope, inputs, source and exposure

- Assignment `institute/runs/three-area-2026-10-27-96h/review-waves/f7-ame-two-party-support/assignment-v1.json`, SHA256 `232a9ce41e57d4c69130ae130238b72d847d1a6f743b5bc5bdd32bb0fab8be86`.
- Candidate `physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-two-party-orbit-obstruction-v1.md`, SHA256 `94f85389567b2a3ea8e8f1a418af58977f4fdc3670f4a696fa6512703b7a9f75`, all 54 LF read, including ending.
- Author's 36-cell data and the review-owned byte-identical snapshot `frontier-review-f7-ame-two-party-support-input-v1.txt` both SHA256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`. The reviewer checker read its snapshot once and enforced that hash.
- The registered target was read from the author slot's `intake-v1.md`: minimize support across **all** normalized complex AME(4,6) states and **all** physical product orthonormal bases; all six two-party marginals must be \(I_{36}/36\) for one tensor. An exact minimum requires a general lower bound and an attaining tensor. Nothing here proves that global minimum.
- [P. Pandya, arXiv:2610.16673v1, Section II and Table 1](https://arxiv.org/html/2610.16673v1) gives the 36 source cells with global normalization \(1/\sqrt{72}\); its Proposition 1 asserts the AME property. The 36 literal cells in the separate review script were checked against that displayed primary table and against the pinned input. I read the author's transcription before the public table: this is not a blind or independent-source-transcription claim. The manuscript's Section VI reports a 38–60 gap; I did **not** reconstruct its imported classical code bound, audit all literature or establish a current global priority claim.
- I have prior general AME/cross-domain project context and make no clean-cognition, first-exposure or full lifetime-contact-census claim. No historical quarantined result is treated as a premise here; those records are not retrospectively validated. No author or comparer was contacted for this review.

## Independent finite witness checks

Independently written `frontier-review-f7-ame-two-party-support-check-v1.py` SHA256 `0b13a9814461d4c8427ccf130c4fa5edc2df429c989c1c43ef8b0389312994ae`, 252 LF/10517 bytes, imports no author code. Ran from the repository root:

```
python3 -B physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-review-f7-ame-two-party-support-check-v1.py
```

The command exited 0. The checker uses exact integer/rational pairs \(a+b\sqrt2\), not floating thresholds. Its own separately written parser enforces the pinned byte hash, both headers, the exact 36 indexed cells, token grammar and the source-table cell comparison. Results:

- 60 distinct nonzero 4-tuples: 48 coefficients \(\pm1\), 12 coefficients \(\sqrt2\), all divided by \(\sqrt{72}\). The exact numerator of the squared norm is 72.
- For **each of the six** choices of actual two-party marginal, a direct partial trace produces all 36 diagonal numerators 2 and all 1260 off-diagonal numerators 0. Dividing by 72 gives \(I_{36}/36\). This checks all 7776 matrix entries of the six reductions, including the actual signs, on the **same** normalized tensor.
- The support has zero Hamming-distance-one pairs. For each party there are exactly 60 distinct spectator triples and level counts `(9,12,12,9,9,9)` in printed local-level order.
- For each of the six active-party pairs, all 36 spectator-pair slices were enumerated, directly tested for distinct occupied rows and columns, and their ranks computed by exact elimination in \(\mathbb Q(\sqrt2)\). The actual histogram was 12 rank-one slices and 24 rank-two slices; sum of ranks 60. The general proof below is not limited to rank at most two or to this field.
- Four **separate** one-party 0/3 Hadamards gave support exactly 78 and preserved each of the six exact marginals. Each rotated tensor has 22 Hamming-one support pairs. Six selected two-party 0/3 Hadamard products gave supports `(101,101,90,102,101,101)` in lexicographic active-party order `(01,02,03,12,13,23)` and retained all six exact marginals. These are sanity instances, not enumeration of arbitrary local matrices.
- In-memory controls rejected the changed-amplitude fixture as `NORM`, the sign-only fixture as `MARGINAL_ENTRY`, and a malformed cell as `FORMAT_TOKEN`; a same-size altered support with a manufactured one-coordinate neighbor was detected as `HAMMING_ONE`. These controls test the named failure modes only, not full checker completeness. The existing author-reported checkers share the same primary table and were not taken as reviewer observations.

The original and rotated states are numerical inputs with exact arithmetic; the observed rotated support/AME property also demonstrates why “no Hamming-one pair” must **not** be silently generalized to every AME state or every product basis.

## Complete reconstruction: arbitrary two local invertibles

Let \(T\) be an arbitrary finite four-index complex tensor with support \(\mathcal S\) such that distinct support tuples never differ in exactly one coordinate. Choose any two active parties \(i,j\). Fix a spectator pair \((u,v)\), and form the matrix \(M_{uv}\) in the active indices. If two occupied entries shared a row but differed in their column, their four-tuples would agree in all but party \(j\); if they shared a column, they would agree in all but party \(i\). Both are prohibited. Thus \(M_{uv}\) is a weighted partial permutation. After row/column permutations, its nonzero part is diagonal with nonzero diagonal entries, so
\[
 \operatorname{rank} M_{uv}=\operatorname{nnz}(M_{uv}).
\]
This includes the empty slice, for which both sides are zero. It does not use AME, equal dimensions, realness, normalized coefficients or a chosen amplitude field.

For arbitrary invertible complex local maps \(A\) and \(B\) on those two parties, the fixed-spectator slice becomes \(A M_{uv} B^T\), preserving its rank. Every finite matrix \(N\) satisfies \(\operatorname{rank}N\le\operatorname{nnz}N\), e.g. rank is at most the number of nonzero rows, which is at most the number of nonzero entries. Therefore
\[
 \operatorname{nnz}(A M_{uv}B^T)\ge\operatorname{rank}M_{uv}
 =\operatorname{nnz}(M_{uv}).
\]
The spectator labels partition all coefficients into disjoint slices, so summing over **all** \((u,v)\) proves no total support decrease. Monomial maps on the two spectator parties can be commuted through the active maps and only reindex/rephase or nonzero-rescale slices, hence do not affect support. In particular, for the checked source tensor all products of local unitaries with at most two nonmonomial factors have support at least 60. If a product unitary lowers this particular tensor below 60, at least three factors must be nonmonomial. Neither direction asserts that any three- or four-party lowering exists.

## Complete reconstruction: one changing unitary

For a fixed site, each original spectator triple contains at most one source coefficient. If its original local level is \(j\), after \(U\in U(6)\) the number of nonzero output coefficients in that fibre is exactly \(\operatorname{nnz}(U_{:,j})\): no contributions from two original local levels share the fibre, so cancellation between source levels is impossible. Therefore the total is precisely
\[
 \sum_{j=0}^{5}m_j\operatorname{nnz}(U_{:,j}),\quad
 (m_0,\ldots,m_5)=(9,12,12,9,9,9).
\]
Every column of a unitary has at least one nonzero. If exactly one column had more than one nonzero, the other five singleton columns, being orthogonal, would occupy five distinct rows and force the remaining column onto the sixth row, contradiction. Hence every nonmonomial unitary has at least two columns with at least one **additional** nonzero each, costing at least \(2\min m_j=18\). Its support is at least 78. A 2×2 Hadamard on levels 0 and 3, both of count 9, has exactly two double-nonzero columns and attains 78; the exact checker independently observed this at each party. Conversely, a monomial unitary has exactly one nonzero per column and gives 60. Thus the stated 60-iff-monomial and least nonmonomial value 78 are correct for this tensor and basis.

The 78 classification relies on unitarity. An invertible nonunitary shear \(I+|0\rangle\langle3|\) has just one double-nonzero column and, by the same fibre formula, gives support \(60+9=69\). It does not contradict the two-invertible-party lower bound 60 or assert preservation of AME. This distinction is not a defect in the candidate, which states the 78 result for \(U(6)\).

## Findings and limits

- Candidate LF13–19: **NO_SUBSTANTIVE_DEFECT** for the stated arbitrary-complex finite-tensor lemma and monomial-spectator corollary.
- LF23–33: **NO_SUBSTANTIVE_DEFECT** for the checked tensor's exact support/histograms and the quantified 60/78 one-party claims.
- LF35–44: the witness's actual normalization and all six marginal equalities were independently checked as above. The author's named code/receipts, mutations and claim of two implementations were not inspected or adopted by title/hash.
- LF46–52: the reported finite 216000-sequence search was not independently replayed and is not used in the reviewed proof. Neither its result nor this review implies no three-/four-party improvement or any all-orbit/global lower bound.

The no-Hamming hypothesis is a basis-specific condition, not a consequence of AME; the exact rotated 78-support AME tensor above is a concrete counterexample to such a generalization. The primary-source 60-term table is a known published witness, not a new upper-bound improvement. The separate 38 lower-bound import, unrestricted minimum, full literature/priority, cross-family verification, formal/kernel checking, independently audited three-checker witness certification and human review remain outside this review. The 3+/4-party original support question remains open here.
