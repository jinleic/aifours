# Support48 AME(4,6): maximal-count branches and the distance-one interface

**Disposition: same-harness written adoption of the branch/interface theorems reconstructed in f307, with two source-text omissions corrected explicitly.** Native clock before composition: 2026-10-30T07:08:13-0700 PDT. Review0F/0M/2m. No support48 exclusion or N>=49 bound follows.

## Maximal-count restriction

For every normalized complex AME(4,6) state in a product basis with exactly48 nonzero coefficients, let t count coefficients of modulus1/6. At the adopted t<=28 boundary and its classical no-OLS(6) provenance,

t is one of24,27,28.

Each paired flattening6psi is unitary. Removing its t unit-modulus singleton rows/columns leaves n=36−t rows and |E|=48−t residual entries, all line degrees>=2. Thus t>=24 and total row-degree excess is t−24. Each connected support component is square by row/column orthonormality and has nonnegative excess.

- Excess0 gives complete2x2 components: a degree2 row forces every intersecting degree2 row to use the same pair, and column degree2 fixes the component size.
- Excess1 is impossible: one degree3 row has degree2 neighbors, whose two-subsets must coincide to avoid a one-column overlap, leaving its third column degree1.
- Excess2 with one degree4 row is impossible: other rows split into equal/disjoint pairs of its four columns; columns from different pairs then overlap at only that row.
- Excess2 with two degree3 rows: overlap size1 is forbidden, size2 forces a private column degree1, and DISJOINT supports cannot connect through degree2-row chains. For equal supports, all remaining pairs coincide; component squareness (not connectivity alone) gives a3x3 eight-entry block with degrees2,3,3.

Therefore t=25 would require an impossible excess1 component. At t=26, residual dimension10 would be one3-row excess2 component plus2-row components, an odd number of rows, contradiction. The source omitted the disjoint-support subcase and used connectivity alone where squareness is required; f307 supplies both, not a retrospective claim that they were written in the original.

## Unconditional distance-one interface at N48,t24

Without importing no-OLS(6), an arbitrary residual pair differing in one coordinate propagates by paired-cut orthogonality to S times{d0,d1}. Every base symbol occurs twice in S and base-pair projections are injective, giving a connected simple cubic triple graph. Nonzero complex products x_s=psi(s,d0)conjugate(psi(s,d1)) flip sign along every edge, so the graph is bipartite; each part has at least3 vertices and m=|S| is6,8,10 or12. All used pair values have both extensions within this block, making the complement isolated in every cut.

For m12 there are six symbols in each base party. For m10 the four-word complement would lie in a one-point box, impossible. For m8 the normalized eight-word complement would be AME(4,2), excluded by the universally reconstructed Pauli spin-flip argument. Thus a distance-one pair forces either a six-symbol residual party OR the isolated m6 decomposition with a twelve-word complement and at most3 complement symbols per party. The source's initial label6−d_i as residual-carried is reversed: d_i is residual-carried and6−d_i maximal-carried; the proof uses the corrected convention.

With f293 as the explicit conditional input, write H for distance-one, Z for six-symbol party and M for the exceptional m6 decomposition. The precise consequence is notM implies(H iffZ); “unlessM” neither constructsM nor asserts equivalence fails insideM.

## Later composition and unverified standalone lemma

The separately adopted [f296+f293 result](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-ame48-t24-composed-no-distance-one-and-six-symbol-parent-v1.md) already yields noH and noZ at N48,t24, conditional on no-OLS(6). It may be imported prospectively; it does not backfill the original source's proof. f307 does NOT prove the source's standalone unrestricted P2 six-word selection theorem or authenticate its exact source-identity description. The AME-scoped conclusion is sufficient here. Any separate use of P2 must retain multiplicity2, actual simultaneous unitarity, isolation and distinct support words.

## Evidence and limits

Parent displayed complete62-LF source, all three named disposition imports and complete266 logical-line review (265LF, no terminal LF); all live pins match. Parent reconstructed the degree-excess accounting, disjoint-support closure, odd residual-row contradiction and the H/Z/M logic in writing. Reviewer independently reconstructed all complex-amplitude and paired-cut cases, after full ordered114LF packet reads and verified bindings. No scientific executable or selected tensor/graph was used.

The source SHA transcription error caught before freeze is separately documented and is not source drift. No t27/t28 exclusion, surviving-profile existence, support48 exclusion, N>=49, human, independent-family, formal/kernel, priority or novelty claim. [Review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f307-ame48-maximal-count-branches-and-interface/review-v1.md) · [Manifest](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f307-ame48-maximal-count-branches-and-interface/manifest-v1.json).
