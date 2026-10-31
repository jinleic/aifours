# Actual anchored cyclic heads: every two-point direct factor has gcd at least fifteen

**Disposition: scoped same-harness written support plus independently authored exact finite projected-coefficient checks, parent-run once.** If actual sets satisfy \(P\oplus Q=\mathbb Z_n\), \(n>14\), with head anchors \(\{0,3,8,11\}\subseteq P\), tail anchors \(\{0,1,7,13,14\}\subseteq Q\), and the ACTUAL head admits a two-point DIRECT factor

\[P=\{u,u+d\}\oplus C,\qquad d\not\equiv0\pmod n,\]

then **\(\gcd(d,n)\ge15\)**. In particular, the actual head cannot have a two-point direct factor of difference3,5,8 or11. This is a uniform structural-subclass exclusion across cardinality allocations, NOT proof that every remaining head has such a factor, unrestricted anchored nonexistence, an anchored witness or finite-maximal-code-completion impossibility.

## Original factor, orientation and multiplicities

Absorb u into C, retaining the original head as \(P=\{0,d\}\oplus C\). The ACTUAL direct factorization gives \(\{0,d\}\oplus C\oplus Q=\mathbb Z_n\); hence \(T=C\oplus Q\) is an actual set with no representation collisions. Its indicator satisfies \(t(x)+t(x-d)=1\). If \(g=\gcd(d,n)\), alternation around the d-cycles forces \(n/g\) even, \(2g\mid n\), and \(\gcd(2d,n)=2g\). Thus T consists of COMPLETE fibers modulo2g, with occupied residues V choosing exactly one point from each antipodal pair in \(\mathbb Z_{2g}\).

Since0∈P, either0∈C or−d∈C. Reversing the factor orientation to \(\{0,-d\}\oplus(C+d)\) in the latter case preserves the original P and Q and ensures0∈C. The actual tail anchor projections \(S=\{0,1,7,13,14\}\bmod2g\) therefore lie in V. Each projected C-residue c satisfies S+c⊆V, and each original head anchor a requires c=a or a−g.

Let \(c_i,q_j\) count ORIGINAL C,Q elements in their residue classes modulo2g. Because T fills complete occupied fibers and C⊕Q is direct, the consuming equation is exactly

\[\sum_i c_iq_{s-i}=L\,1_V(s),\qquad L=\frac n{2g}>0.\]

Projection multiplicities are not discarded, and the projected head is not assumed itself to form an unweighted quotient tiling.

## Exhaustive fourteen-case obstruction

Tail-anchor antipodes directly exclude g=1,2,4,6,7,12,13,14. At g=3,5 the tail projection fills V and has trivial translation stabilizer, forcing C to project only to0; the actual head then misses anchor8 or3. At g=9 the two forced head choices generate an antipodal pair. The only remaining necessary support shadows occur at g=8,10,11. Their original positive multiplicities contradict the weighted equation:

| g | Singleton weighted rows | Other occupied rows force | Contradiction |
|---:|---|---|---|
| 8 | L=c3 q0=c0 q14 | L>c0 q0 and L>c3 q14 | c3>c0>c3 |
| 10 | L=c13 q13=c8 q1 | L>c8 q13 and L>c13 q1 | c13>c8>c13 |
| 11 | L=c14 q14=c8 q0 | L>c8 q14 and L>c14 q0 | c14>c8>c14 |

Every strict remainder uses only positive residues forced by the original head and tail anchors; optional C or Q residues are merely nonnegative. The complete support sets and all coefficient incidences are recorded in the full author/review/checker inputs below. No equal-unit-weight assumption or quotient-shadow witness is used.

## Actual CRT consumer and exact remaining step

At the separately named earlier coprime-cardinality dilation import, in the stated one-odd-prime families \(n=HR\), \(H=2^{a+b}p^{j+t}\), \(|P|=2^ap^j\), \(|Q|=2^bp^tR\), \(\gcd(R,2p)=1\), dilation shows the ORIGINAL head is a graph \(P=\{(a,f(a)):a\in A\}\) in \(\mathbb Z_H\times\mathbb Z_R\), and every actual tail fiber \(Q_r\) separately complements A. But the ORIGINAL undilated factorization still requires the coupled equations

\[\sum_{a\in A}1_{Q_{r-f(a)}}(h-a)=1\quad\text{for every }(h,r).\]

Separate complement choices do not pay these equations. A projected pairing of A lifts to one fixed original difference only if \(f(a+\delta_H)-f(a)=\delta_R\) is constant across that pairing, and its ORIGINAL cyclic gcd must then be checked. Neither the anchor rectangle nor a replacement tile implies this.

The first unpaid route is an actual qualifying two-point factor for the remaining head, or an independent contradiction for heads with no such factor or only gcd≥15 factors. All higher-two-adic p3/p5/p11 and mixed-odd numerical families retain their stated residual scope; no whole numerical allocation is closed solely by this structural theorem. The literal eight-word UD result and RSS/pure-letter completion bridge get no new unconditional upgrade.

## Evidence and observed finite limits

[Complete f569 author body](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f569-actual-anchored-tiling-higher-twoadic-and-shared-prime-frontier/review-v1.md) · [f589 periodic/orientation written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f589-anchored-two-point-factor-periodic-reduction-small-gcd-written-review/review-v1.md) · [f590 weighted coefficient/CRT consumer review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f590-anchored-small-gcd-weighted-coefficients-and-crt-boundary-written-review/review-v1.md) · [f591 independent exact report/source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f591-anchored-small-gcd-weighted-original-projection-independent-check/review-v1.md) · [materialized verifier](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f591-anchored-small-gcd-weighted-original-projection-independent-check/independent-small-gcd-anchored-projection-v1.py) · [parent one-shot receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f591-anchored-small-gcd-weighted-original-projection-independent-check/parent-independent-finite-run-v1-receipt.json) · [prior actual two-adic/word disposition](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/math-5-actual-anchored-tiling-twoadic-allocation-and-literal-eight-word-code-parent-v1.md). Parent displayed all694/413/496/785 logical author/review/source lines. Both WRITTEN gates report0F/0M/0m. F569’s earlier direct pre-body ACK counted11 instead of12 controls; that count is withdrawn, with all twelve actual pre-body read ranges supplied. The count correction is not backdated into an extra missing-read event or a mathematical finding.

After full static read and exclusive GO, the independent stdlib checker ran ONCE: exit0, empty stderr,0.0621s. It enumerates all32,766 antipodal selectors for g=1,…,14:122 satisfy tail-support constraints and only three satisfy the necessary head-support screen. For the g8/10/11 shadows it checks every residue’s coefficient incidence and exact nonnegative-remainder/positive-witness strict two-cycle certificates. Those are **support shadows plus symbolic weight contradictions**, not actual target tilings or a general tiling solver.

Fourteen separate actual non-target direct tilings check the physical periodicity/multiplicity consumer for every g. Two genuine non-target controls show that dropping head anchors or tail anchors destroys the conclusion. The dropped-weighted-equation control is PROJECTION_ONLY, NOT an actual anchored tiling. Dropping the actual original-P-factor hypothesis is **NOTTESTED** on an actual target, because no such target array was supplied; no fake shadow replaces it. The transparent output adapter loads the unchanged source once and prints its retained RESULT.

All genuinely held episodes and ALL scientific/method/selection/planning/report/confidence consumers remain NONINPUT. Original-source correspondence, unrestricted anchored nonexistence, finite-maximal-completion impossibility, current-literature novelty, independent-family/human review and formal/kernel acceptance remain unpaid.
