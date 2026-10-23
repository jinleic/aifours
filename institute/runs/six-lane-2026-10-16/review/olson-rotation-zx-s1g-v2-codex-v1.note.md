The mathematical argument closes. I found **no FATAL or MAJOR defect**. The corrections concern wording, domain, and citation bookkeeping.

| Audited claim | Verdict |
|---|---|
| Lemma S1(g) | **ACCEPT-WITH-FIXES** — minor wording |
| Corollary S1(g)+ | **ACCEPT-WITH-FIXES** — premise/domain clarification |
| Uniform INV* | **ACCEPT** |
| Uniform ordered Olson | **ACCEPT** |
| Tables, coverage, and residual arithmetic | **ACCEPT** |

I used only static reads and hashes inside the designated snapshot. All nine SHA256 hashes and byte counts match. I independently checked SOURCE00’s eight steps, corollary, Section 2 deductions, and arithmetic. Imports are Davenport, EGZ, the full index-one statement recorded in SOURCE03:7–17, accepted S1(d) through SOURCE02’s overlay, and the accepted ZX/S1+ framework through SOURCE04’s mandatory overlay. The latter imports normal form, GRX, PM*, K1, DAV, SHgen/SHgen-E, restricted REFL, and RGR-LONG at their accepted scopes. Their underlying proofs are not newly certified here. **S1(e), residual notes, and finite-search results are not premises.**

The proof checks follow.

1. **Lengths — SOURCE00:29–34.** Every zero-sum has even length. Thus a shortest counterexample has \(N\ge p+\delta+2\), and (ZP) forces \(N\ge2p+2\). Davenport applied after removing one occurrence supplies a nonempty proper zero-sum. For any proper nonempty zero-sum \(A\), both \(A\) and its nonempty complement are shorter zero-sums. Minimality and parity give lengths at most \(p+\delta\). Consequently
   \[
   |A|\ge l=N-p-\delta\ge p+2-\delta.
   \]
   Here \(l\) is even.

2. **Claims A and B — SOURCE00:36–41.** EGZ supplies \(p\) distinct occurrences \(T_1\) with \(x(T_1)=0\); its complement \(M\) is an odd half-sum. For every nonempty proper \(V\subset M\) with \(x(V)=0\), even \(V\) is a proper zero-sum, giving \(|V|\ge l\). Odd \(V\) makes \(T_1V\) a proper zero-sum, giving \(|V|\le\delta\). Two disjoint odd such subsets produce a proper zero-sum of length at most \(2\delta<l\). Indeed P1 gives \(l\ge2\delta+6\). These claims hold for every eligible choice of \(T_1\).

3. **Upper bound on \(N\) — SOURCE00:43–46.** If \(l>p\), Davenport on \(p\) occurrences of \(M\) gives an odd \(V_1\), since an even result would have length both at most \(p\) and at least \(l\). Removing \(V_1\) leaves at least \(\mu-\delta=l>p\) occurrences, so a second application gives a disjoint odd \(V_2\). Claim B excludes this. Hence \(l\le p\), and parity improves this to \(l\le p-1\), equivalently \(N\le2p+\delta-1\).

4. **Excluding \((1,0)\) — SOURCE00:48–53.** EGZ can avoid the specified occurrence \(u\), since \(N-1\ge2p+1\). Davenport in \(M-\{u\}\) gives \(V\) of length at most \(p\). Odd \(V\) contradicts Claim B with \(\{u\}\). If \(V\) is even, its length is at most \(p-1\), and the leftover
   \[
   W=M-\{u\}-V
   \]
   has even size satisfying
   \[
   2\le\mu-p\le |W|\le\mu-1-l=\delta-1<l.
   \]
   It has \(x\)-sum zero and therefore is a forbidden short proper zero-sum. The omitted lower-bound calculation is valid.

5. **Minimality and index one — SOURCE00:55–70.** The construction gives an odd half-sum \(C\) with \(3\le|C|\le\delta\). Its even complement \(V\) has length \(\beta\ge l\). A proper even \(x\)-zero subset would split \(V\) into two zero-sums of length at least \(l\), impossible because
   \[
   2l-\mu=\mu-2\delta\ge p+2-2\delta>0.
   \]
   A proper odd subset and its odd complement contradict Claim B. Thus \(V\) is minimal **over \(C_p\)**, and Davenport gives \(\beta\le p\).

   The imported index-one theorem applies because
   \[
   \beta\ge p+2-\delta\ge\lfloor p/2\rfloor+2.
   \]
   Its nonzero basis element \(h\) has order \(p\). Positive coefficients sum to \(p\), so their excess is \(p-\beta\le\delta-2\), and
   \[
   m_V\ge2\beta-p\ge p+4-2\delta.
   \]
   Relative to the order-\(2p\) generator \(\hat h=(1,h)\), the signed weights are \(c\) for odd \(c\), and \(c-p\) for even \(c\). Their sum is \(p(1-n_{\rm even})\); zero-sumness forces \(n_{\rm even}\) odd. Hence an occurrence \(y\) with even coefficient \(2\le e\le\delta-1\) exists, and \(t\ge m_V\).

6. **Classification and occurrence availability — SOURCE00:72–89.** In (6a), the chosen \(z\) is not an \(\hat h\) occurrence. In (6b), \(z\) has odd coefficient while \(y\) has even coefficient, so they are distinct occurrences; neither uses an \(\hat h\) copy. The assumed copy counts produce proper even zero-sums. When those counts are unavailable, the integer inequalities give precisely the alternative bounds in \(K_e,K_o\).

   For a near-\(p\) occurrence, \(s=p-c\) is even and
   \(2\le s\le e-2\le\delta-3\le m_V\). If it lies outside \(C\), the \(s\) copies taken from \(V\) are disjoint from both it and \(C\), yielding the stated contradiction. Two distinct near-\(p\) occurrences require at most
   \[
   s+s'\le2\delta-6\le p+4-2\delta\le t,
   \]
   exactly where P2 is used. Their constructed zero-sum is shorter than \(l\). Thus at most one exists. The bounds \(K\le2\delta-5\) for \(\delta\ge5\) follow. For \(\delta=3\), near-\(p\) terms are impossible, \(K_e=2\), and \(K_o\le1\); therefore \(U\) contains only coefficient 2.

7. **Congruence and mass — SOURCE00:91–99.** Substituting \(t=N-|U|-u_q\) gives
   \[
   (N-2p)+X-(s_q+1)u_q\equiv0\pmod p.
   \]
   Put \(d=N-2p\), so \(2\le d\le\delta-1<p\). Without \(q\), the least nonnegative residue gives \(X\ge p-d\ge p+1-\delta\). With \(q\), one actually has
   \[
   4-\delta\le r=s_q+1-d\le e-3;
   \]
   the printed weaker lower bound is valid. Since \(y\in U\), \(X\ge e-1>r\). Therefore the positive multiple \(X-r\) of \(p\) is at least \(p\), giving \(X\ge p+r\ge p+3-\delta\).

8. **Stopping argument — SOURCE00:101–118.** The S-condition is correct. Its parity is
   \[
   p-\sigma+|S|\equiv1+n_{\rm even}(S)\equiv0\pmod2.
   \]
   The copies exist because \(0\le p-\sigma\le t\), and are disjoint from \(S\subset U\). Properness follows explicitly from
   \[
   0<p-\sigma+|S|=p-\operatorname{mass}(S)\le p-1<N.
   \]
   This also handles \(\sigma=p\), when no \(\hat h\) copies are needed.

   Starting with \(y\), the allowed additions preserve odd even-coefficient count. At exhaustion, no odd-coefficient occurrence and at most one even-coefficient occurrence remain. Hence exhaustion reaches coefficient sum at least \(X-K\). The first crossing of \(2\delta-2\) therefore occurs: the sufficient bound is \(p\ge5\delta-8\), supplied by P1 at \(\delta=5\), P3 for odd \(\delta\ge7\), and directly by P1 at \(\delta=3\).

   Since \(e<2\delta-2\), a last addition exists, giving
   \[
   2\delta-2\le\sigma\le2\delta-3+2K\le6\delta-13\le p
   \]
   for \(\delta\ge5\); for \(\delta=3\), \(\sigma\le7\le p\). Also \(p-t\le2\delta-4<\sigma\). Finally, \(c\ge2\) implies
   \(\operatorname{mass}(S)\ge\sigma/2\ge\delta-1\), contradicting the S-condition’s upper bound \(\delta-2\).

P1 thus supplies the separation, minimality, index applicability, and copy bounds, together with the small-\(\delta\) stopping estimates. P2 supplies simultaneous copies for two near-\(p\) occurrences. P3 controls the final overshoot and large-\(\delta\) availability. P2 is redundant under P3, as the candidate states.

The requested boundaries and table entries check as follows. Bounds in the middle columns are evaluated at the displayed boundary prime.

| \(\delta\) | Boundary \(p\) | \(l_{\min}\) | \(t_{\min}\) | Final \(\sigma\) upper bound | Primes having this \(\delta^*\) |
|---:|---:|---:|---:|---:|---|
| 3 | 13 | 12 | 11 | 7 | 13, 17 |
| 5 | 19 | 16 | 13 | 17 | 19, 23 |
| 7 | 29 | 24 | 19 | 29 | 29, 31, 37 |
| 9 | 41 | 34 | 27 | 41 | 41, 43, 47 |
| 11 | 53 | 44 | 35 | 53 | 53, 59, 61 |

I tested algebraically the concentrated counterexample candidate
\(T=\hat h^{p+4}y^{p-2}\), with \(y=(1,2h)\). It is a zero-sum of length \(2p+2\), but contains the zero-sum
\(\hat h^{p-2\delta}y^\delta\) of length \(p-\delta\). Its complement has forbidden length \(p+\delta+2\). At the five boundaries these complement lengths are \(18,26,38,52,66\). This attempt fails (ZP); neither the near-\(p\) construction nor the endpoint \(\sigma=p\) exposes a missing hypothesis.

For the corollary, **S1(g) at \(\delta=5\) alone proves the entire \(p\ge19\) branch**: the three lower bounds are \(19,10,17\). S1(e) is unnecessary. Decreasing odd \(\delta\) preserves the hypotheses, and successive odd \(\delta\) correspond to successive integer \(\kappa\), so there are no holes. Complete the definition with \(\delta^*=1\) at \(p=5,7\), and \(\delta^*=3\) at \(p=11,13,17\). For \(p\ge19\), the displayed maximum is correct. The next value, \(\delta=13\), requires \(p\ge65\).

For uniform INV*, put \(B=(p+\delta^*)/2\). Handle \(k=1\) by accepted K1. Otherwise \(k\le o\), and:

- \(o\le B+1\) gives \(\widehat\kappa\le k-1\le o-1\le B\).
- \(F-o\ge p-\delta^*-2\) gives \(\widehat\kappa\le\kappa(w)\le B\).

GRX supplies (ZP), and the corollary supplies (S1). The accepted terminal criterion gives the nonzero pair. Restricted REFL applies to the original length-\(4p-2\) avoider because \(3o\le2p+1\) implies \(o\le p\).

For ordered Olson, the accepted deletion ledger preserves both branches: odd-block deletion gives \((o-1,F-1)\); separate deletions of two distinct rotation occurrences give \((o\text{ or }o-2,F)\). Thus \(o'\le o\), \(F'-o'\ge F-o\), and \(3o'\le2p+1\). Case 1 uses \(o\le2p-3\) and adjacent equal pairs. In the rotation-deletion case, a third shared rotation pins the two nonzero pairs together. RGR-LONG completes the increasing-index conclusion.

The unconditional low-\(o\) bounds equal \(\lfloor(2p+1)/3\rfloor\) at \(p=13,17,19,23,29\): respectively \(9,11,13,15,19\). At \(p=31\), \(B=19\) and \(k\le21\), leaving exactly \((k,\widehat\kappa)=(21,20)\) outside this parameter certificate. This is **sufficiency only**: actual (S1), or another admissible normal form, may still suffice.

There are three MINOR findings:

- **SOURCE00:107–108:** “any value” overstates greedy reachability. At \(\delta=3\), reachable sums satisfy \(\sigma\equiv2\pmod4\). Replace it with “continuing to exhaustion reaches a value at least \(\sum_Uc-K\).”
- **SOURCE00:124,137:** Replace the S1(e) attribution with “S1(g), \(\delta=5\)” and remove S1(e) from the table’s dependency list.
- **SOURCE00:120–127:** State the inherited domain \(\kappa\in\mathbb Z_{\ge0}\) and the complete piecewise definition of \(\delta^*\) above. If negative integers are intended, add the Davenport argument that (ZP) then forces zero-sum-freeness.