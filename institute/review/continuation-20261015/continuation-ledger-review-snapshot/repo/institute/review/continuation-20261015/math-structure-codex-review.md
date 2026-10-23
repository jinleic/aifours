**ACCEPT-WITH-FIXES.** Lemmas 1–2 and Theorem 3 are correct, including for composite \(P\). The stated collision-search corollary is correct under its prime-modulus hypothesis. One later necessity claim overstates the conclusion.

1. **Required scope correction — [lines 137–140](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/math-structure-snapshot/proofs/FORCED-SUBGROUP.md:137).** The theorem does not establish that every resolution must exploit the *full* multiplicative closure of \(D\), or treat the cyclotomic family individually. For example, it does not rule out a uniform arithmetic obstruction to that family.

   Replace that necessity claim with: “Theorem 3 rules out exclusion certificates consisting of repeated nonzero differences inside the specified forced subgroup. Further exclusions require additional information; the theorem does not prescribe its form.”

2. **Lemmas 1–2 — [lines 23–33](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/math-structure-snapshot/proofs/FORCED-SUBGROUP.md:23): valid.** The ideal \((N-\omega)\) has index \(N^2+N+1=P\), giving the asserted kernel. Multiplicativity of the Eisenstein norm makes every nonzero kernel element have norm at least \(P\). Distinct elements of \(T_a\) have difference norm at most \(N^2<P\), proving injectivity. Together with \(2^{3a}\equiv1\), this proves exact order \(3a\). No field assumption enters.

3. **Small norms, all unit symmetries, and coordinates — [lines 40–52](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/math-structure-snapshot/proofs/FORCED-SUBGROUP.md:40): valid.** The size bound gives \(\operatorname{Nm}(E')<4\); norm \(2\) is impossible since Eisenstein norms are \(0\) or \(1\pmod3\). The six norm-one elements are precisely the units, and the six norm-three elements form one unit orbit of \(1-\omega\). Multiplication by \(\omega\) permutes \(T_a\), while negation exchanges the two positive and two negative terms, covering every unit. Thus the norm-three case really can be normalized to
   \[
   (N-\omega)\omega(1-\omega)=(N+2)+(2N+1)\omega.
   \]
   Its second coordinate violates the valid bound \(|A|,|B|\le2N\).

4. **Norm one — [lines 54–68](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/math-structure-snapshot/proofs/FORCED-SUBGROUP.md:54): all direction cases close.** The first coordinate forces both positive terms onto direction \(1\). For the negative terms:
   
   - Both along \(-1\) give second coordinate \(0\).
   - Exactly one along \(-1\) forces the other to be \(-\omega\), of magnitude \(1\), and then \(m_1+m_2=N+m'>N\).
   - Neither along \(-1\) forces magnitudes \(2,1\), respectively along \(-\omega,-\omega^2\). The resulting equation is \(m_1+m_2=2^a-1\), impossible for \(a\ge3\) by binary expansion.

5. **Norm zero — [lines 70–83](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/math-structure-snapshot/proofs/FORCED-SUBGROUP.md:70): all pair types are covered.** Parallel pairs have unique binary decompositions. An equal-magnitude nonparallel pair points along \(-\mu_3\), excluding equality with a parallel pair. For unequal magnitudes, the displayed norm comparison is correct. When \(e=1\), its right side is \(8\), forcing \(d=3\) by valuation, but the left side is then \(56\). When \(e\ge2\), valuations force \(d=e+1\), yielding the stated impossibility.

   For two nonparallel pairs, the odd factors and powers of \(4\) determine both magnitudes. Equal magnitudes determine the missing cube-root direction; unequal magnitudes force both differences in line 83 to vanish. Thus there is no omitted characteristic-zero collision.

6. **Forced-subgroup conclusion — [lines 89–93](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/math-structure-snapshot/proofs/FORCED-SUBGROUP.md:89): correct with the stated scope.** For prime \(P\), the listed generators give exactly \(K=\langle2\rangle\). A nonzero difference collision implies
   \[
   x+w=z+y,
   \]
   and Sidonicity forces the ordered difference pairs to coincide. Hence every rejection certificate of this precise form, confined to this \(K\), is blocked.

   The prime restriction matters when identifying the full cube-root subgroup. For example, with \(a=5\), \(P=1057=7\cdot151\), adjoining **all** cube roots enlarges \(\langle2\rangle\) and produces
   \[
   1-4=771-774=-3.
   \]
   Indeed \(r=722\) satisfies \(r^3\equiv1\), with \(774\equiv4r\) and \(771\equiv512r\). This does not contradict Theorem 3 or the explicitly prime-modulus corollary.

The universal theorem passes by its Eisenstein proof, independently of Singer/Cohen and the finite controls. It establishes the specified method limitation, not an exclusion of the candidate plane orders.