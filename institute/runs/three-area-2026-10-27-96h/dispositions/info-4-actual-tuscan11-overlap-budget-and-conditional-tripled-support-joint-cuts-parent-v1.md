# Actual T2(11): unconditional overlap budget and conditional joint-cut frontier

**Disposition: same-harness written support with independent finite-lemma corroboration.** No actual eleven-row witness, unrestricted T2(11) no-go, universal \(M=C\), novelty, independent-family/human review or kernel proof is claimed. The finite constraints below apply to the **same actual eleven permutation rows**, not unrelated row/cycle shadows.

## Universal overlap budget

For every actual T2(11), the 110 original directed adjacency events and 99 original linear directed distance-two events are all distinct. Fix any six-symbol set \(B\). Let \(N_t(B)\) count rows whose six-symbol odd-position support intersects \(B\) in \(t\) symbols, and let \(\mu_B\) count missing original distance-two ordered pairs internal to \(B\). Then
\[
\boxed{11N_6(B)+5N_5(B)+6N_1(B)\le36-\mu_B.}
\]
For one actual permutation row with odd support \(D\), the respective minimum numbers of finite singleton vertices of its augmented cycle, indexed by \(|B\cap D|=1,\ldots,6\), are exactly \((6,0,0,0,5,11)\); each is attainable on an individual row. Summing the bounds over the same actual array uses the previously adopted finite-singleton identity \(W_B=36-\mu_B\).

Consequences needing **no \(M=C\)**: if three rows share support \(B\), every other row's support meets \(B\) in two, three or four symbols; if exactly two rows share \(B\), at most two rows total meet it in one or five symbols. Individual-row sharpness does not imply global budget equality or a valid eleven-row array.

## Additional joint restrictions only under \(M=C\)

Let \(M\) be the missing original distance-two ordered pairs and \(C\) the actual last-to-first closing pairs. Assume explicitly \(M=C\) and suppose distinct supports \(B,D\) each occur in three rows. Then \(|B\cap D|=3\). Adjoining one common infinity gives eleven actual directed Hamilton cycles on twelve vertices. The assumption makes their singleton sum for each six-cut exactly 36, including infinity; three alternating cycles saturate it. Under those actual constraints the overlap-four case would require all eight directed arcs between two size-two cells in the remaining five Hamilton cycles, but the no-singleton and directed-arc conditions allow at most two. Overlap two is excluded by complementing the **cut** on the augmented set; that complement is not asserted to be an original odd-position support.

Now write the four three-element cells \(I=B\cap D\), \(J=B\setminus D\), \(K=D\setminus B\), \(L=X\setminus(B\cup D)\). Among the six cycles alternating across \(B\) or \(D\), put
\[
T=\sum_{h\text{ alternating across }B}r_D(h)+\sum_{h\text{ alternating across }D}r_B(h),
\]
where \(r_A(h)\) counts monochromatic \(A\)-runs. On the **five remaining actual Hamilton cycles**, each of the four cells has the same exact layout counts:

| \(T\) | One length-3 run | A length-2 and length-1 run | Three singleton runs |
|---|---:|---:|---:|
| 13 | 1 | 4 | 0 |
| 14 | 2 | 2 | 1 |

The proof uses the third cut \(E=B\triangle D\), its complete singleton budget and all 24 directed internal-cell arcs on the SAME cycles. If \(G\) counts full length-three cell runs, \(G=4T-48\). Three length-three runs cannot partition all six ordered arcs on three vertices, so each cell has one or two; \(G\) is necessarily 4 or 8. Consequently \(T\in\{13,14\}\), with the uniform table above. The remaining five cycles have 16 or 20 \(E\)-singletons, so \(B\triangle D\) can be an odd support in **at most one** row. If three distinct supports each occur three times, their pairwise intersections are three and their triple intersection is one or two. These are conditional necessities, not existence of any surviving arrangement.

## Verification and remaining work

[Complete author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f461-tuscan11-joint-actual-row-budget-and-residual-branch-frontier/review-v1.md) · [f474 unconditional written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f474-tuscan11-unconditional-overlap-budget-written-review/review-v1.md) · [f475 conditional joint-cut written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f475-tuscan11-conditional-tripled-support-four-cell-ledger-review/review-v1.md) · [f476 independent finite report](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f476-tuscan11-overlap-and-three-cell-independent-finite-check/review-v1.md) · [independent source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f476-tuscan11-overlap-and-three-cell-independent-finite-check/independent-finite-v1.py) · [parent one-shot run](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f476-tuscan11-overlap-and-three-cell-independent-finite-check/parent-independent-finite-run-v1-receipt.json). Parent displayed the entire 670-line author, 285/316-line written returns and 910-line finite report/source, reconstructed both the finite/infinity accounting and the conditional three-cut proof. Both written reviewers report 0F/0M/0m. Child-authored independent code was NOTRUN by the child; parent displayed it fully, froze GO and executed once: exit0, empty stderr, 0.025s. It checked all 462 six-subsets of one actual row, all64 neighbor triples, all216 ordered three-path tuples, all243 five-slot cell-layout words, the actual T2(4) positive control and six intended-reason mutations. The five-cycle cell ledgers are weak local fixtures, not an actual compatible T2(11).

A single tripled support, multiplicity-at-most-two branches, surviving joint \(T=13,14\) cases and all relevant \(M\ne C\) branches remain. A full no-go must exclude every actual Hamilton-row collection with the original linear conditions; alternatively a complete eleven-row array must be directly verified. Public source comparison remains bounded and no claim of priority follows.
