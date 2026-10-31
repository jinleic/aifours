# RQLS10: other sixty-ray complement and all 100 specified cyclic/circulant four-sector completions

**Disposition: same-harness written adoption, plus independently authored exact physical-incidence and local-operator checks run once.** For the actual 60-cell complement of the cyclic difference support \(S=\{0,1,3,4\}\), there do not exist sixty pairwise nonparallel rays in \(\mathbb C^6\) making each actual restricted row, column, and additive-symbol \(r+c\) class an orthonormal basis. This excludes an actual full orthogonal \(4+6\) completion on this support and its ten-mask affine orbit. In union with the precisely identified prior 60+20+10 exclusions, **all 100 balanced cyclic/circulant four-sector supports are excluded as full 4+6 completions**. This is NOT an unrestricted hundred-ray, noncirculant, other-resolution, rank-28 \(5+5\), or irreducible no-go.

The positive previously adopted 40-ray \(\mathbb C^4\) subsystem for the DIFFERENT support \(\{0,1,5,6\}\) is not contradicted: its separate complement no-go excludes only its full \(4+6\) completion.

## Actual cells and operator balance

The original complement is \(T=\{2,5,6,7,8,9\}\), with actual cells \(H_T=\{(r,c):c-r\in T\pmod{10}\}\). Set \(c'=c-2\) and CRT-label \(r=(a,u),c'=(b,v)\) in \(\mathbb Z_5\times\mathbb Z_2\). Equal a,b give all four bit pairs; difference ±1 gives v=u; difference ±2 gives v=u+1. These are the actual20 diagonal and40 off-diagonal cells. Their thirty contexts are the original ten rows, ten columns, and ten cyclic \(r+c\) symbols—not arbitrary context occurrences.

The four actual diagonal rays at each a are mutually orthogonal. Their two diagonal-pair projections \(U_a,V_a\) and the missing projection \(E_a\) form an orthogonal rank-two partition of \(I_6\). Each ordered off-diagonal block projection \(P_{ab}\) is rank2 because its two rays share an actual symbol ONB. Actual row/column/symbol equations imply

\[U_{a-2}+U_{a+2}+V_{a-1}+V_{a+1}=2(U_a+V_a).\]

Positivity on \(\operatorname{ran}E_a\) gives \(E_aU_{a\pm2}=E_aV_{a\pm1}=0\) and the corresponding range containments. A projection contraction argument applied to the adjacent and distance-two ODD five-cycles shows, without assuming commutation,

\[E_aE_b=G\quad(a\ne b)\]

for one common orthogonal intersection projection. The five residuals \(E_a-G\) are mutually orthogonal, and \(g+5(2-g)\le6\) leaves exactly \(g=\operatorname{rank}G\in\{1,2\}\).

## Both physical-ray consumers

**Rank one.** The five residual lines \(L_a\), together with G, exhaust \(\mathbb C^6\), and the actual diagonal planes become \(U_a=L_{a-1}\oplus L_{a+1}\), \(V_a=L_{a-2}\oplus L_{a+2}\). A coordinate ONB consumes two of the five line rays; global nonparallelness allows at most two such bases among ten. At least three indices have both diagonal bases noncoordinate. For any two good indices a,b, their ACTUAL symbol plane and the actual row and column diagonal-ray orthogonalities force each of the two off-diagonal rays into both \(E_a\) and \(E_b\), hence the one-dimensional G. They are orthogonal members of one actual symbol ONB, contradiction. The coefficient argument uses both complex nonzero diagonal components and correct original column-bit routing; it is not a block-span-only inference.

**Rank two.** All \(E_a=G\). Operator balance forces \(U_a=U,V_a=V\) by the five-cycle linear recurrence. Equivalently, its rational coefficient matrix L satisfies \(L^2=5I-J\), so its kernel is exactly the constant line. The fixed \(G,U,V\) partition gives three two-sectors. A three-partition lemma makes the actual row and column group planes each reduce those sectors. For one off-diagonal ray, its row and column group planes cannot be equal: their OTHER rays would be parallel in distinct physical cells, violating global nonparallelness. Their intersection is therefore precisely the ray, which the sector projections preserve; the individual ray lies in one sector. Every row and column ONB has two rays per sector, making a given ray’s same-sector row and column partners parallel at distinct cells: contradiction. No unproved commutation between row and column group planes or vector covariance is assumed.

## Exact orbit and limited union

For every unit \(h\pmod{10}\) and translation t, the actual-cell relabeling \((r,c)\mapsto(hr,hc+t)\) permutes rows, columns and cyclic symbols, and sends differences to \(h(c-r)+t\). It transports the physical no-go without any unitary representation assumption. For S, \(3S=S+9,7S=S+7,9S=S+6\), and its ten translations are distinct; this excludes its entire ten-mask orbit at the full-completion scope.

There are exactly \(\binom52^2=100\) balanced four-element masks (two even, two odd). The union is:

| Disjoint mask family | Number | Exclusion scope |
|---|---:|---|
| Contains a nondegenerate three-term AP | 60 | Prior actual four-sector \(\mathbb C^4\) obstruction |
| Affine orbit of \(\{0,1,3,8\}\) | 20 | Prior actual four-sector \(\mathbb C^4\) obstruction |
| Orbit of \(\{0,1,5,6\}\), two antipodal pairs | 10 | Prior actual 60-cell \(\mathbb C^6\) complement obstruction; full completion only |
| Orbit of \(\{0,1,3,4\}\) | 10 | New actual 60-cell \(\mathbb C^6\) complement obstruction; full completion only |

The prior 80/100 four-sector obstructions are imported from the [binary-sector/cyclic-support disposition](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-5-rqls10-binary-sector-and-cyclic-rank4-family-exclusions-parent-v1.md), and the prior 10 full-completion obstruction from the [other complement disposition](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-5-rqls10-sixty-ray-complement-and-ten-four-sector-orbit-exclusion-parent-v1.md). The ten new masks are not asserted to be standalone four-sector no-gos. A full original array would have four sector rays spanning the common 4-plane in each physical context, forcing the other six into its common orthogonal 6-plane; this actual consumer supplies the necessary complement ONBs and global nonparallelness.

## Evidence and process qualifications

[Complete f557 author body](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f557-rqls10-other-cyclic-four-sector-orbit-actual-complex-closure-frontier/review-v1.md) · [f570 complete five-cycle/whole proof written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f570-rqls10-other-orbit-five-cycle-missing-projection-rigidity-review/review-v1.md) · [f571 rank-one/good-index and complete proof review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f571-rqls10-other-orbit-rank-one-sector-and-good-block-consumer-review/review-v1.md) · [f572 rank-two/individual-ray and union review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f572-rqls10-other-orbit-rank-two-individual-ray-and-orbit-exclusion-review/review-v1.md) · [f573 independent finite report/source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f573-rqls10-other-orbit-sixty-cell-projection-and-rank-regime-exact-check/review-v1.md) · [materialized verifier](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f573-rqls10-other-orbit-sixty-cell-projection-and-rank-regime-exact-check/f573-finite-verifier-v1.py) · [parent one-shot receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f573-rqls10-other-orbit-sixty-cell-projection-and-rank-regime-exact-check/parent-independent-finite-run-v1-receipt.json). Parent displayed747/398/231/400/1141 logical author/review/source lines. F570/f571/f572 each report0F/0M/0m at their stated mathematical scopes; all are same-harness, not independent-family/human/kernel reviews.

After full static parent source read and GO, the independent exact stdlib checker ran ONCE, exit0, empty stderr,0.0483s. It checks all60 actual physical cells,30 contexts, five balance rows, both odd-cycle index dispatches, \(L^2=5I-J\),18 formal three-partition sandwiches, all26 necessary coordinate-line choice patterns and520 good-endpoint/bit routes, all100 mask memberships and40 physical affine maps, and10 named controls. Its exact even-cycle and equal-group-plane examples are LOCAL countermodels to weakened hypotheses, not actual 60-ray configurations or witnesses; the formal operator words and finite controls do NOT automate the general complex Hilbert-space contraction proof.

**F573 documentary MINOR retained:** its initial direct pre-body ACK said eleven controls and gave unsupported exact LF totals for two administrative files; all TWELVE were in fact read before the ACK. Its additive correction had a transport-request range typo, immediately corrected to the actual request. This is one documentary finding, not a missing-control read or mathematical refutation. The prior complement’s f540 ACK transport fault remains disclosed in its disposition; it is not erased by this new union. All held episodes and their proof/method/selection/planning/confidence/report consumers remain NONINPUT.

The unrestricted original100-ray question, noncirculant supports, noncyclic resolutions, other orthogonal dimensions including rank28 \(5+5\), irreducible arrays, original-source equivalence, novelty, independent-family/human review and kernel acceptance remain OPEN.
