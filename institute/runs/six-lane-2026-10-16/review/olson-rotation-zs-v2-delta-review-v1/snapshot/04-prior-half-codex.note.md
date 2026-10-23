All twelve SHA-256 hashes match. The audit used only static reads and hashes inside the snapshot.

| Claim | Disposition |
|---|---|
| Lemma ZS | **ACCEPT** |
| ROT-HALF | **ACCEPT** |
| INV*-HALF | **ACCEPT** |
| OLSON-HALF | **ACCEPT** |
| Method obstruction | **ACCEPT-WITH-FIXES** |

**Findings: 0 FATAL, 0 MAJOR, 1 MINOR**, concerning the obstruction’s wording only.

The nine steps of ZS are valid independently of the old \(5k\le2p+4\) hypothesis:

1. **Every zero-sum is short — SOURCE00:39–44.** A minimal zero-sum has even length at most \(2p\), hence at most \(2\kappa\) by ZP. Factor any nonempty zero-sum into disjoint minimal zero-sums. At the first cumulative length reaching \(2\kappa+2\), the preceding even length is at most \(2\kappa\); the crossing length is therefore at most \(4\kappa\le2p-2\). This contradicts ZP. When \(\kappa=0\), the initial minimal-zero-sum argument already excludes every nonempty zero-sum.

2. **Maximal-length splitting — SOURCE00:46–49.** A longest zero-sum \(Z\) exists, allowing the empty sequence. Any nonempty zero-sum in its complement would extend it to a longer zero-sum. Thus \(Y'\) is zero-sum-free. The exact identities
   \[
   L=2p+2\kappa-k-|Z|,\qquad
   e=k-1-2\kappa+|Z|
   \]
   give \(0\le e\le k-1\), using Davenport for the lower bound and Step 1 for the upper bound.

3. **MULT and integer completeness — SOURCE00:51–62; SOURCE01:63–81.** The accepted MULT lemma has no inherited \(5k\) restriction: its relevant hypothesis is \(3e+2\le2p\). Here
   \(3e+2\le3k-1\le2p\). Consequently \(m\ge\max(2,e+1)\), \(g\) is a generator, and the positive integer weights satisfy \(e'=\sum(d_j-1)\le e\).

   COMP is an integer subset-weight argument: \(m\) unit weights supply \([0,m]\), and each next weight is at most \(e'+1\le m\), so adding it leaves no integer gap. A weight-\(2p\) subsequence would contradict zero-sum-freeness, proving \(W'\le2p-1\). Also \(d_j\le k\le p-2\), so these integer weights equal the prescribed signed representatives.

4. **Completions through \(Z\) — SOURCE00:64–68.** For positive \(\tau(U)\le W'\), COMP provides a nonempty completion \(Q\) wholly inside \(Y'\), disjoint from \(U\). The resulting zero-sum is short by Step 1, regardless of its initially possible length. Both length bounds follow:
   \[
   |U|+\tau(U)-e'\le2\kappa,
   \]
   and, when \(\tau(U)\le m\), the stronger bound obtained from \(g^{\tau(U)}\).

5. **Complementary completions — SOURCE00:70–76.** If \(k\le\tau(U)\le2p-k\), both \(\tau(U)\) and \(\tau(U^c)=2p-\tau(U)\) lie in COMP’s available interval. Each completion separately yields a valid inequality. The two completions may overlap in \(Y'\): the proof adds numerical inequalities and never asserts that their union is a subsequence.

   Adding gives
   \[
   |Z|+2p-2e'\le4\kappa.
   \]
   Substituting \(e'\le k-1-2\kappa+|Z|\) forces
   \(2p-2k+2\le|Z|\le2k-2\), hence \(4k\ge2p+4\). But the stated range gives \(4k\le2p+2\). Both interval endpoints are therefore excluded as required.

6. **Balance of \(Z\) — SOURCE00:78–84.** Singleton applications of Step 5 first bound every coefficient in \(Z\). If the positive integer sum first crosses \(k\), it lands in \([k,2k-2]\subseteq[k,p-1]\); its signed representative cannot wrap and violates Step 5. The negative magnitudes have the same argument. Thus \(\sigma_+,\sigma_-\le k-1\), and their difference, being zero modulo \(2p\), must be zero as an integer.

7. **Room in \(Y'\) — SOURCE00:86–90.** Assuming \(W'\ge2p-\sigma\) permits completion of \(Z_+\). Substitution of the exact expression for \(e\) yields
   \[
   2p+1\le\sigma+k+|Z_-|
          \le2\sigma+k\le3k-2,
   \]
   impossible in the stated range. Hence \(W'\le2p-1-\sigma\), equivalently \(e'\le e-\sigma\). The strict inequality and its integer decrement are correct.

8. **Negative count — SOURCE00:92–94.** Since \(\sigma\le k-1\le m\), the completion of \(Z_-\) can use exactly \(\sigma\) copies of \(g\). Therefore \(|Z_-|+\sigma\le2\kappa\). If \(\sigma=0\), both signed parts are empty.

9. **Sign-sensitive cost — SOURCE00:96–102.** Every coefficient in \(Y'\) is positive, so its cost is exactly \(e'\). Consequently
   \[
   \begin{aligned}
   \operatorname{cost}(Y)
   &=e'+2\sigma-|Z_+|\\
   &\le e+\sigma-|Z_+|\\
   &=k-1-2\kappa+|Z_-|+\sigma\\
   &\le k-1.
   \end{aligned}
   \]
   This retains the full cost \(|b|\) of each negative term. Since \(N=|Z_-|\), the identity \(\operatorname{cost}=E+N\) proves \(E\le k-1-N\).

The requested endpoints are covered. For \(k=1\), necessarily \(\kappa=0\), \(Z=\varnothing\), \(e=0\), and MULT forces \(Y=g^{2p-1}\). For general \(\kappa=0\), \(Z=\varnothing\) and the conclusion follows directly from MULT. At \(k=(p+1)/2\), the crucial bounds remain \(4\kappa\le2p-2\), \(4k\le2p+2\), and \(2k-2\le p-1\). At \(p=5\), \(k\le3\), \(e\le2\), and all these inequalities remain valid.

A **single order-two term is not silently excluded**. Multiplicity \(m\ge2\) excludes it as the selected generator. C1 subsequently excludes it from \(Y'\); Step 5 applied to a singleton excludes it from \(Z\), because its signed coefficient would be \(p>k-1\).

For ROT-HALF, the composition is valid:

- **Normal form — SOURCE03:30–43; SOURCE00:121–125.** PM* is used only in its accepted original-to-reduced avoidance direction. Length, \(F\), and the rotation multiset are preserved. Equal-valued fusions lower the odd-block count by zero or two. \(H\) is recomputed from the terminal \(F,k\); it need not remain unchanged through an odd-plus-odd fusion. The one-even-block terminal case is excluded by accepted K1, or by the displayed Davenport argument followed by \(2p\) identical reflections. The \(k=1\) nonzero rotation case is supplied by accepted K1/lowodd, SOURCE09:9.
- **V and ZP.** For \(k\ge2\), \(F\ge2\). DAV permits the boundary frame outside the marked interior gaps even with empty rotation runs. It gives \(\kappa\le k-1\). If \(H\ge p\), the all-plus pattern with no rotations already gives an identity selection; thus \(\kappa\ge0\). GRX’s all-plus pattern gives precisely the sequence ZP required by ZS.
- **Weights — SOURCE00:126–132.** An odd generator has form \(Y(c)\) with \(c\ne0\). Since \(|b|\le k\le p-2\), these coefficients coincide with SHgen’s weights and exclude \(\rho_0\). Lights are exactly \(b=\pm1\). If \(E>0\), then \(\eta\ge1\), \(\eta\le E/2\), and \(a_{\max}\le E+1\le k\).
- **SHgen hypotheses.** The displayed estimates establish H from \(3k\le2p+1\), and K from \(5k\le4p-1\). Both follow from the new half-range; neither invokes the old \(5k\le2p+4\).
- **Genuine empty runs — SOURCE03:47–70; SOURCE02:51–55,115–121.** Each expansion stays inside its existing rotation run, removes reflection pairs while retaining every odd block, and preserves block values and empty runs. Therefore every descendant retains a nonconstant reflection run wherever an original empty run separated different values. At the base expansion its rotations are algebraically in \(\{\rho_c,\rho_{-c}\}\), and \(o_F\le k\le p\). Restricted REFL supplies the contradiction at every induction level. H and K persist under the expansion. Full ROT, full INV*, and unrestricted REFL are unnecessary.

For **INV*-HALF**, restricted REFL is applied anew to the original word, after ROT-HALF establishes its rotation pair. Its original \(o_F\le(p+1)/2\le p\) supplies the required scope; reflection constancy is not lifted backwards through PM* (SOURCE00:140–144; SOURCE08:6).

For **OLSON-HALF**, every deletion in SOURCE05:28–47 remains valid with \(B=(p+1)/2\):

- If \(R\le2\), \(F\ge4p-3\) and \(B\le2p-3\) provide at least \(p\) disjoint equal-reflection pairs. The specified cyclic frame prevents a wrapping block from invalidating adjacency. Their ordered product is identity; returning to original index order cyclically shifts the selected product and preserves identity by conjugation.
- Deleting one letter from an odd block of length at least three leaves the block present and lowers \(o_F\) by exactly one. Restoring that same letter preserves the RGR conclusion.
- For \(R\ge3\), the two words each delete **one** distinct rotation occurrence. A deletion leaves \(o_F\) unchanged or lowers it by two. A third rotation survives in both words and is nonzero, identifying their two \(\pm\)-pairs. Every original rotation occurs in at least one deletion word. Any adjacent unequal reflections in the original cyclic word persist after rotation deletion, contradicting the deletion word’s reflection rigidity.

Thus the reconstructed length-\((4p-1)\) word satisfies the exact accepted RGR-LONG hypotheses, including cyclic reflection-run constancy. No deletion from an even reflection block is needed.

**MINOR — SOURCE00:114.** Replace “for \(k\) near \(p\) a proof must use GRX patterns with sign changes” with:

> At \(k=p\), the cost conclusion cannot follow from ZP alone. Extending this approach requires additional avoidance information, for example nonconstant-sign GRX patterns.

The counterexample itself is correct. With \(k=p,\kappa=p-1\), the ZP window contains only length \(2p\). Such a selection has sum \(2bg\), where \(1\le b\le p-1\), so it cannot vanish. For any generator other than \(g\), the \(2p-1\) copies of \(g\) already exceed cost \(p-1\); relative to \(g\), the \(3g\) copies cost \(2(p-1)\). This refutes the proposed ZP-only extension at \(k=p\). It supplies no ordered-Olson counterexample and establishes no obstruction interval below \(p\).

**Audited/imported boundary:** Audited here are ZS’s nine steps and the HALF theorem composition, including all ordered deletion arguments. Imported at their accepted scopes are Davenport/EGZ, MULT, GRX, PM*, K1, DAV, SHgen/SHgen-E, restricted REFL, and RGR-LONG. The existing \(o_F\le4\) result combines only by union, yielding \(o_F\le\max(4,(p+1)/2)\). Its separate \(p=5,o_F=4\) finite foundation remains imported through SOURCE11. No finite check supports the new ZS/HALF proof, and no conclusion outside that union is audited.