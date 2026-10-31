# Actual ordered dihedral words: whole projection-deficit-four band

**Disposition: scoped same-harness written support with independently authored actual-groupword finite verification run once by parent.** Let p≥5 be an odd prime, and let an actual linear word in \(D_{2p}\) have exactly \(3p-2\) reflection occurrences, at least \(p+1\) rotation occurrences, and at most one rotation in every CYCLIC gap between consecutive reflections. If its cyclic rotation-deleted projection has exactly \(o_\pi=3p-6\) odd-length maximal constant-label runs, then the ORIGINAL-ORDER word has an identity subsequence of exactly \(2p\) actual occurrences, comprising precisely **two rotations and \(2p-2\) reflections**. This is the entire deficit-four band under those actual-word hypotheses, not an unrestricted dihedral or all-group theorem.

With the [previously adopted top-two bands](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/math-2-actual-dihedral-top-two-odd-projection-bands-parent-v1.md), the named actual-word setting is covered at \(o_\pi\in\{3p-6,3p-4,3p-2\}\). The remaining named high-run interval is \(p+4\le o_\pi\le3p-8\), odd. In particular the named high branch closes for p=5, not the unrestricted ordered-Olson problem. The earlier top-two theorem holds for every odd p; this new deficit-four theorem is explicitly p≥5.

## Actual chronological selector and safe interior rotations

Use \(\rho_u=(u,0)\), \(\sigma_a=(a,1)\), with \((x,e)(y,b)=(x+(-1)^ey,e+b)\). For one chronological reflection triple (a,b,c), selecting two reflections without an interior rotation yields

\[A_0=\{a-b,a-c,b-c\}.\]

For a selected rotation \(\rho_u\) in the first or second interior gap, the actual ordered products give

\[A_u^{(1)}=\{a-u-b,a-u-c,u+b-c\},\qquad A_u^{(2)}=\{a-b+u,a-u-c,b-u-c\}.\]

The first gap is safe whenever \(b\ne c\); the second is safe whenever \(a\ne b\). Crucially, the rotation may become a PREFIX or SUFFIX after a reflection is omitted; it is not assigned one uniform sign. Every nonconstant triple has at most one potentially unsafe interior gap, and the total number B of such gaps equals the number of equal adjacent reflection pairs INSIDE the triples. The proof excludes the potentially unsafe gaps without claiming they necessarily collapse for every rotation label.

Omit one reflection occurrence z, cut immediately after it, and split the other \(3p-3\) reflections into \(p-1\) consecutive nonconstant triples with \(B\le2\). The two original cyclic gaps adjacent to z remain distinct boundary positions—one before the first triple, one after the last—so rotations there are not dropped or merged into a fictitious singleton gap. From \(R\ge p+1\) and \(B\le2\) there are at least \(p-1\ge4\) safe/boundary rotations. Choose two distinct occurrences, with at most one interior to each triple. Singleton actual gaps ensure that three safe interior occurrences cannot all occupy one triple.

Every chosen triple subword contains exactly two reflections and is itself a rotation. Each resulting exponent set has size≥2; the p−1 disjoint sets cover \(\mathbb F_p\) by the supplied Cauchy–Davenport proof. A fixed boundary-rotation offset is therefore canceled by an actual selection of two reflections from each chronological triple. Disjoint blocks and distinct chosen rotation occurrences give exactly \(2p\) physical letters. Returning from the chosen cut to the original word cyclically conjugates the selected group product, preserving identity; no arbitrary permutation or reflection commutativity is used.

## All five deficit-four run types

For a run of length \(\ell\), its contribution to \(F-o_\pi\) is \(\ell-1\) if odd and \(\ell\) if even. Deficit four therefore has exactly these non-singleton run types:

| Type | Omitted occurrence | Bound B |
|---|---|---:|
| One run of length5 | Middle | 2 |
| One run of length4 | Second | 1 |
| Two runs of length3 | One of three positions in one run, chosen to avoid alignment of the other with a triple | 2 |
| Length3 plus length2 | Middle of length3 | 1 |
| Two runs of length2 | Any occurrence | 2 |

In the two-length3 case the three omissions produce three consecutive partition phases for the other run; at most one aligns it as an entire constant triple. In every case, the omission cut does not create a new internal adjacency between its two sides. Thus all triples are nonconstant and the safe-gap selector applies uniformly.

The assigned p=5 actual word and actual original positions 1,3,4,6,7,9,13,14,16,17 give an identity with two rotations and eight reflections; that is one witness, not a substitute for the all-prime written proof. Deficit six has ten run types and length6/7 runs obstruct this PARTICULAR one-omission nonconstant-triple partition; this says nothing about other possible selectors.

## Review and observed finite evidence

[Complete f568 author body](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f568-actual-ordered-olson-deficit-four-and-residual-high-band-frontier/review-v1.md) · [f579 interior-rotation and sumset written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f579-olson-deficit-four-interior-rotation-sumset-certificate-written-review/review-v1.md) · [f580 all-five-run and original-order written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f580-olson-deficit-four-five-run-types-and-actual-order-written-review/review-v1.md) · [f581 independently authored report/source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f581-olson-actual-deficit-four-two-rotation-selector-independent-finite-check/review-v1.md) · [materialized actual-word checker](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f581-olson-actual-deficit-four-two-rotation-selector-independent-finite-check/independent-actual-deficit-four-checker-v1.py) · [parent one-shot receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f581-olson-actual-deficit-four-two-rotation-selector-independent-finite-check/parent-independent-finite-run-v1-receipt.json) · [earlier top-two-band disposition](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/math-2-actual-dihedral-top-two-odd-projection-bands-parent-v1.md). Parent displayed456/364/284/825 author/review/source logical lines. Both written reviews report0F/0M/0m. F580’s initial administrative terminal-range description was over-wide by one line; the complete metadata ending had actually been read before its direct ACK, and the additive correction is not a missing-read event.

After full static read and GO, the independent standard-library actual-word checker ran ONCE: exit0, empty stderr,0.652s. It scanned all8192 binary reflection lists at p=5, of which260 have the specified deficit, then tested FOUR stated actual gap/rotation placement controls per admitted list. These binary lists cover only run types (3,2) and (4); two deterministic actual words for each of all five types at each p=5,7,11 supply the remaining type coverage. In total1071 actual-word cases were compared to an independent original-order group-subsequence DP, with10,890 identity cyclic-cut checks,74,266 local interior-slot interfaces and222,798 actual pair products. Rotation labels are physical occurrences; raw labels may coincide modulo p, and no impossible p+1 distinct rotation group elements are claimed.

Ten named controls reject wrong prefix/suffix signs, both reversed safe-gap tests, two interior rotations in one block, dropping rotations adjacent to z, unrequested p=3 scope, interleaved incompatible pair choices, incomplete run-type reporting and false equality of nonidentity cyclic products. **Merely omitting the written conjugation explanation is NOTTESTED**; identity products stay identity at all cuts. The p=5 binary scan is not an exhaustion of all p-ary reflection labels or all rotation placements, and bounded higher-prime cases are not an all-prime proof. The universal result rests on the written argument above.

All held episodes and their proof/method/selection/planning/confidence/report consumers remain NONINPUT. Deficit six, lower high-run bands, unrestricted ordered-Olson, all finite groups, original-source correspondence, novelty, independent-family/human review and kernel acceptance remain open.
