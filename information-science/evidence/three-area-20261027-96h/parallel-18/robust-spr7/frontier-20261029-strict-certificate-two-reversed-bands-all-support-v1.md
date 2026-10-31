# Every strict negative certificate needs two reversed root bands

**Status: WRITTEN theorem candidate, not parent adoption.** This is a direct, universal structural obstruction to the requested strict negative-coordinate atom certificates. It applies to **any finite number of atoms**, not only five frequencies, and is not an equivalent encoding or a conjectured verdict.

Let \(K\) be a compact independent coefficient box of monic strictly Hurwitz polynomials of odd degree \(n=2m+1\ge3\). Merge any repeated positive squared frequencies in a finite positive-weight actual-denominator atom list by averaging the actual denominators in \(K\). If the resulting aggregate has a strictly negative coefficient on **every** numerator monomial, then:

* some global even-part root band contains two distinct selected positive nodes at which the even sign crosses **backwards** relative to the natural sign change through that band;
* some global odd-part root band contains two distinct selected positive nodes at which the odd sign crosses backwards;
* these two nondegenerate node intervals lie in **different, disjoint** parity-root bands.

Zero and compactified-infinity atoms may be present; they do not change the conclusion. In particular **no finite grid with at most one positive node in each even-root band can ever produce such a certificate**, regardless of how many nodes it has elsewhere; the same is true if at most one node lies in each odd-root band. The two requirements must both be met. This excludes whole classes of actual-box certificate searches, but does not exclude all certificates.

## Proof

The oriented alternating-moment lemma in `frontier-20261029-odd-degree-strict-certificate-support-obstruction-v1.md` proves that the actual averaged even values and the actual averaged odd values each contain, among their nonzero entries, an ordered alternating sign subsequence of length \(m+1\) beginning with \(-\). It allows positive zero and infinity atoms. The proof uses the strict coordinate signs and a polynomial with \(m\) positive roots; no zero-annihilator conversion is involved.

For any monic Hurwitz degree-\(2m+1\) polynomial, the even and odd parts are positive at zero and have exactly \(m\) simple positive zeros each, interlacing in the order \(E_1<O_1<\cdots<E_m<O_m\). Because the coefficient intervals for the two parities are independent, the maximum of any earlier parity root is strictly below the minimum of the next opposite-parity root: the two extrema can be combined into one actual box member. Compactness makes these extrema attainable. Thus all \(2m\) global root bands are closed, ordered and mutually disjoint.

Fix one parity, discard its zero-valued samples, and write \(k_i\in\{0,\ldots,m\}\) for the number of that actual member's positive parity roots below the \(i\)-th selected node. Its parity sign is \((-1)^{k_i}\). If the counts never decrease as frequency increases, an alternating subsequence of length \(m+1\) beginning negative is impossible: the first count is at least 1 and every sign change raises it by at least 1, forcing the last count to be at least \(m+1\). Therefore there are two increasing positive nodes \(t_i<t_j\) with \(k_i>k_j\).

The decrease is exactly one. If \(k_i\ge k_j+2\), the earlier actual \((k_j+2)\)-nd root is below \(t_i\) while the later actual \((k_j+1)\)-st root is above \(t_j\), contradicting the strict global order of their bands. Take \(q=k_i=k_j+1\). The earlier actual \(q\)-th parity root lies below \(t_i\), while the later actual \(q\)-th root lies above \(t_j\). Hence the entire nondegenerate interval \([t_i,t_j]\) lies in the global \(q\)-th root band, and the sign crosses backward. Repeating the argument independently for even and odd values gives the two claimed intervals. The global even and odd root bands are disjoint, so the intervals cannot be the same.

For septics, `frontier-20261029-strict-negative-certificate-two-band-obstruction-v1.md` (SHA-256 `33cce85c5451984a670de2ae05c921ea3a61d0c88c867c3c81a1bb94cd026783`) additionally proves at least five nodes and classifies the three possible five-node band pairs. The present result constrains **all** support sizes and extends to every odd degree. It is a written deduction from the pinned alternating-moment and phase-root arguments, not formal verification, cross-vendor review, novelty clearance, or an original negative/positive verdict.
