All eight snapshot hashes and byte counts match the supplied manifest. I audited SOURCE00’s five new statements, the substitutions into ZX’s proof, the word-level hypotheses, deletion ledger, and scope calculations. Only static snapshot reads and hashes were used.

| Statement | Verdict |
|---|---|
| Lemma SC0 | **ACCEPT** |
| Lemma ZX-SC | **ACCEPT-WITH-FIXES** |
| Theorem ROT-ZX-SC | **ACCEPT** |
| Corollary INV*-ZX-SC | **ACCEPT** |
| Corollary OLSON-ZX-SC | **ACCEPT** |

**No FATAL or MAJOR findings. One MINOR arithmetic correction; no hypothesis needs strengthening.**

I import the classical index-one statement exactly as recorded in SOURCE03, and the accepted ZX/S1+ results through SOURCE02’s mandatory overlay. Normal form, PM*, K1, GRX, DAV, SHgen/SHgen-E, restricted REFL, RGR-LONG, and the OLSON case structure remain accepted imports. I checked their application here, rather than re-proving those results. No finite-search report or unreviewed note is a premise.

**MINOR — [SOURCE00:48](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-zxsc-v1-review-v1/snapshot/00-ZXSC-v1.md:48): the displayed real-number inequality fails at \(p=5\).**  
The claim
\[
(4p+1)/5\le p-1
\]
becomes \(21/5\le4\). Its intended integer consequence remains correct.

Concrete fix:
> Since \(k\) is integral, \(k\le\lfloor(4p+1)/5\rfloor\le p-1\) for \(p\ge5\).

Alternatively, handle \(p=5\) separately with \(k\le4\). This preserves \(L\ge p+1\), SC0’s applicability, and every subsequent conclusion.

For **SC0**, the minimality argument is sound (SOURCE00:25–30). Since \(S\) is nonempty and zero-sum-free, \(s\ne0\). A proper nonempty zero-sum in \(S^+\) cannot lie inside \(S\), so it must be \(U(-s)\). Then \(S-U\) has sum zero. Zero-sum-freeness forces that complement to be empty, making the purported subsequence all of \(S^+\), a contradiction. This works with occurrences, including when the appended value already occurs in \(S\).

The imported theorem applies over \(C_{2p}\): \(2p\ge10\), and
\[
|S^+|=t+1\ge p+2=\lfloor2p/2\rfloor+2.
\]
SOURCE03:9–11 explicitly supplies positive coefficients summing to \(\operatorname{ord}(a)\). Thus \(\operatorname{ord}(a)\ge p+2\); since it divides \(2p\), it must equal \(2p\). Removing the appended occurrence removes a positive coefficient, leaving coefficient sum at most \(2p-1\). A generator of \(C_{2p}\) is odd, and an odd term expressed as \(a_i g\) has odd \(a_i\). The general classical statement supports this application at \(p=5,7\); SOURCE04’s separate \(p\ge11\) S1(d) restriction is irrelevant to SC0.

For **Step A′**, longest-\(Z\) maximality makes \(Y'\) zero-sum-free. Together with (D) and (S1), this gives
\[
2p-k\le L\le2p-1,\qquad
e=2p-1-L=k-1-2\kappa+|Z|\in[0,k-1].
\]
After the minor integer correction, \(L\ge p+1\). SC0 therefore supplies the required positive odd coefficients and \(W'\le2p-1\).

Write \(q=L-m\). Every nonunit coefficient contributes at least two to \(e'=W'-L\), so
\[
q\le e'/2,\qquad m\ge L-e'/2.
\]
Also \(a_i-1\le e'\), hence \(a_i\le e'+1\). The critical calculation at SOURCE00:53–54 is correct:
\[
5L\ge5(2p-k)\ge6p-1
\iff 3e\le2L-2.
\]
Consequently
\[
a_i\le e'+1\le L-e'/2\le m.
\]

The asserted largest multiplicity is also valid, although it follows most directly from the counting bounds: \(e'\le e<L\), so \(q<L/2<m\). Every other value occurs at most \(q\) times. Thus \(g\) is actually the unique most frequent value in \(Y'\). Moreover \(a_i\le k\le p-1\); oddness then gives \(a_i\le p-2\), including the exceptional possibility \(k=p-1\) at \(p=5\). Hence \(b_g(a_i g)=a_i\).

COMP(a) follows by starting with the \(m\) unit weights and adding weights at most \(m\); COMP(b) is supplied directly by SC0; COMP(c) follows by subtracting the selected excesses, whose total is at most \(e'\). Every singleton has weight at most \(m\), so the full consequence of (A4)—weight greater than \(m\) requires at least two occurrences—also survives.

For **Steps B–D**, no unavailable MULT conclusion remains necessary. The exchange inequality uses only longest-\(Z\) maximality and disjointness of \(Z,Y'\). Step C uses \(b\le p<W'\), completeness, and (A4), all supplied by A′.

The two relevant occurrences of “\(p+2\)” in ZX’s sequence proof have different roles. SOURCE01:106’s lower bound \(W'\ge p+2\) can be weakened to \(W'>p\), exactly as asserted. SOURCE01:124’s inequality
\[
2p-\beta\ge p+2
\]
comes independently from the canonical negative-coefficient bound \(\beta\le p-2\). It remains valid. Step D therefore still forces
\[
\beta\le e-e'.
\]
The other “\(p+2\)” expressions elsewhere in SOURCE01 belong to the separate S1 discussion and supply no hidden hypothesis for Steps B–G.

For **Step E**, the definitions are correctly inherited: \(Z=g^rT\), \(T\) contains precisely the negative terms, \(\beta(z)=-b_g(z)>0\), and \(\sigma=\sum_T\beta(z)\). Since \(Z\) sums to zero,
\[
\sigma=r+2pt.
\]
Here \(r\le|Z|\le2\kappa<2p\), so \(\sigma\ge0\) forces the integer \(t\ge0\).

The exact window estimate in SOURCE01:134 is
\[
2m-2p+1
\ge2p-1-2e-e'
\ge e-e',
\]
whose last inequality requires precisely \(3e\le2p-1\). It does **not** require \(3e\le2p-2\). Thus (R2)’s second alternative supplies the needed condition, including equality. If \(t\ge1\), the negative-weight prefix sums hit \([2p-m,m]\); the two separate exchanges then give \(2p\le|Z|<2p\). Their replacement subsequences need not be mutually disjoint, because the exchanges are independent.

Under (R2)’s first alternative, Step D gives every \(\beta\le e-e'\le k-1\), while \(|T|\le|Z|\le2\kappa\). Therefore
\[
\sigma\le2\kappa(k-1)<2p,
\]
forcing \(t=0\). Both alternatives establish \(\sigma=r\).

For **Steps F–G**, all required bounds remain available. A completion of weight \(2p-r\) would give
\[
2p\le|Z|+e'
\le2\kappa+e
\le2\kappa+k-1
\le2p-2,
\]
contradicting (R1). Thus \(W'\le2p-1-r\), and
\[
\operatorname{cost}_g(Y)=e'+r\le e\le k-1.
\]
Coefficients on \(Y'\), positive terms of \(Z\), and negative terms are bounded respectively by \(k\), \(1\), and \(e-e'\le k-1\). The identity \(E+N=\operatorname{cost}_g(Y)\) also carries over unchanged.

For **ROT-ZX-SC**, the nontrivial theorem branch begins at \(k=2\); the corollary’s \(k=1\) branch is correctly discharged first by accepted K1, including the nonzero rotation value. For \(k\ge2\), DAV supplies \(\widehat\kappa\le k-1\). At \(\widehat\kappa\in\{0,1\}\), all remaining (R1) conditions hold, and
\[
\widehat\kappa(k-1)\le k-1<p
\]
supplies (R2). GRX supplies (ZP), and accepted integer-domain S1+ supplies (S1).

The integer upper bound gives \(k\le p-2\), with \(p=5,7\) checked separately. Thus the signed coefficients are precisely the required SHgen weights, with no \(\rho_0\). From \(E+N\le k-1\), a heavy configuration satisfies
\[
\eta\le(k-1)/2,\qquad a_{\max}\le k.
\]
The SHgen conditions follow:
\[
2H=2p-2-2\widehat\kappa\ge2p-4\ge E,
\]
and
\[
2p-\eta-a_{\max}-1
\ge(4p-3k-1)/2\ge k
\]
by \(5k\le4p-1\).

The normal form supplies the remaining representation hypotheses. For SHgen-E, expansions retain the same odd blocks and empty runs between different values (SOURCE06:52–69). Its REFL instances have \(o_F\le k\le p\). This verifies the restricted caller obligation throughout the induction.

For **INV*-ZX-SC**, the advertised equivalence is exact:
\[
\kappa(w)\le1
\iff F-o_F\ge2p-4.
\]
Normal form gives
\[
\widehat\kappa=\kappa(w)-(o_F-k)/2\le\kappa(w).
\]
Avoidance and GRX supply \(\widehat\kappa\ge0\), as in the accepted overlay; therefore the terminal value is indeed \(0\) or \(1\). After rotation rigidity, restricted REFL is applied to the **original** word, whose \(o_F\le(4p-1)/5\le p\).

For **OLSON-ZX-SC**, both inequalities survive the accepted deletions. Case 2 gives \((o',F')=(o-1,F-1)\); Case 3 gives \((o',F')=(o\text{ or }o-2,F)\). Hence \(5o'\le4p-1\) and \(F'-o'\ge2p-4\). Case 1 is valid because \((4p-1)/5\le2p-3\), giving at least \(p\) equal reflection pairs when \(R\le2\). SOURCE07’s framing/conjugation argument preserves increasing original index order. Cases 2–3 then recover RGR and invoke accepted RGR-LONG.

The **scope calculation** is correct strictly beyond \(3k\le2p+2\): the second (R2) alternative fails, and
\[
\kappa<\frac p{k-1}<\frac{3p}{2p-1}<2.
\]
At equality \(3k=2p+2\), larger \(\kappa\) remain possible. SOURCE00:114 should therefore be read as describing the stated theorem’s sufficient hypotheses, not a maximal limitation of Lemma ZX-SC. Coverage remains existential over admissible normal forms.

The examples recompute correctly: \(p=11\): \(o_F=8,F\ge26\); \(p=13\): \(o_F=10,F\ge32\); \(p=19\): \(o_F=14,15\); \(p=29\): \(o_F=20,\ldots,23\). They assert sufficiency only.

Finally, the small-prime bounds are: \(p=5\), lemma \(k\le4\), theorem \(k\le3\); \(p=7\), both \(k\le5\); \(p=11\), lemma \(k\le9\), theorem \(k\le8\). At the exact lemma boundary \(p=11,k=9\), \(Y=g^{12}(9g)\), \(\kappa=0\), is zero-sum-free and has cost \(8=k-1\). This confirms sharpness without breaking the claim.