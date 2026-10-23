DISPOSITION: ACCEPT

The stated partial result is sound for every prime \(p\ge5\). I found no FATAL, MAJOR, or required MINOR correction. Classical EGZ for \(C_p\) is the only substantive imported theorem. Neither the reported computations nor any parent review is needed.

Here “subword” means an ordered subsequence of occurrences. This audit concerns the supplied inlined texts.

**Q1 — GRX: both directions and all degeneracies**

Use the group law encoded in `notes-GRX-v1.md:LF30–32`:
\[
(a,\epsilon)(b,\eta)=(a+(-1)^\epsilon b,\epsilon+\eta),
\qquad
\rho_x=(x,0),\quad \sigma_y=(y,1).
\]
An identity selection necessarily contains an even number of reflections, by projection to \(C_2\).

Fix the indicated cut and initially normalize \(z_1=+1\). If \(c_i\) reflections are selected from \(S_i\), the signs before successive rotation runs satisfy
\[
z_{i+1}=z_i(-1)^{c_i}.
\]
Thus \(c_i\equiv f_i\pmod2\). Conversely, counts satisfying these congruences realize the prescribed signs: select any \(c_i\) occurrences in each constant block and the desired rotation occurrences. Empty rotation runs impose no additional restriction. Constancy gives \(\sigma_{y_i}^{c_i}=1\) or \(\sigma_{y_i}\) according to parity. This proves the selection correspondence in `notes-GRX-v1.md:LF24–29`.

The ordered product has rotation coordinate
\[
V=\sigma+\sum_{f_i=1}z_i y_i,
\]
where \(\sigma\) is the sum of the selected signed rotation values. Since \(p\) is odd, division by \(2\) is legitimate, and
\[
\sum_{f_i=1}z_i y_i
=\frac12\sum_i y_i(z_i-z_{i+1})
=-\frac12\sum_i z_i\theta_i
=-T(z).
\]
The last equality uses \(\sum_i\theta_i=0\). Therefore the product is the identity exactly when \(\sigma=T(z)\). The calculation in `notes-GRX-v1.md:LF30–35` is correct.

The entire claimed interval of reflection counts is realizable. Put
\[
M_i=\ell_i-[\ell_i\not\equiv f_i\pmod2].
\]
Because \(\ell_i\ge1\), \(M_i\ge f_i\), and the choices are exactly
\[
c_i=f_i+2q_i,\qquad 0\le q_i\le (M_i-f_i)/2.
\]
Sums of these integer intervals contain every integer between their endpoints. Consequently \(C\) takes every value in
\[
\Phi,\ \Phi+2,\ldots,\sum_iM_i=C_{\max}.
\]
The cyclic number of sign changes \(\Phi\) is even. Hence these are precisely **all even integers** in the stated interval, with no missing values. Rotation selections are independent of these counts. A submultiset of \(X^z\) can always be realized by choosing corresponding occurrences in their original runs, preserving their order. This verifies `notes-GRX-v1.md:LF35–40`, including arbitrary rotation values and multiplicities.

Both directions now follow:

- An identity \(2p\)-selection yields its normalized signs, feasible \(C\), and signed rotation sum \(T(z)\).
- A condition in GRX supplies realizable reflection counts and rotation occurrences whose ordered product is the identity and whose total size is \(2p\).

Global normalization is valid: replacing \(z\) by \(-z\) preserves \(f_i,\Phi,\delta,C_{\max}\), while negating both \(X^z\) and \(T(z)\). Strictly, the displayed product formula uses the normalized pattern. For an unnormalized pattern the actual coordinate is \(z_1(\sigma-T(z))\), which has the same zero condition. The text’s normalization at `notes-GRX-v1.md:LF40–41` therefore closes this point.

Cyclic cutting preserves identity selections: if the selected products on the two sides of a cut are \(U,V\), then \(UV=1\) iff \(VU=1\). This cyclically rotates the selected order; it does not permit arbitrary rearrangement. The argument at `notes-GRX-v1.md:LF41–42` is exact.

The degeneracies also work:

- **\(F=0\):** all selected letters commute, so the criterion is exactly \(0\in\Sigma_{2p}(X)\), as stated at `notes-GRX-v1.md:LF20`.
- **\(R=0\):** necessarily \(m=0,C=2p\); with \(\Sigma_0(\varnothing)=\{0\}\), GRX requires precisely a feasible reflection selection with \(T(z)=0\).
- **Nonmaximal representations:** the proof uses only positive constant block lengths and intervening rotation runs. Adjacent equal constant pieces separated by an empty run are allowed.

**Q2 — PM*: preservation direction and nonmaximal blocks**

The preservation direction is correct:
\[
w\text{ avoids}\quad\Longrightarrow\quad \widetilde w\text{ avoids}.
\]

Lift a reduced pattern by assigning the merged run’s sign to both original runs. Then \(z_j=z_{j+1}\), so \(f_j=0\). Since \(\ell_j\) is even, its original contribution to \(\delta\) is zero. Adding \(\ell_j\) to the following block changes neither that block’s parity nor its corresponding \(f\)-value. Thus \(F,\Phi,\delta,C_{\max}\) all agree, and the signed rotation multisets agree. These assertions in `proof-ROT-lowodd-v1.md:LF31–37` are correct.

For the merged run,
\[
\widetilde\theta
=y_{j-1}-y_{j+1}
=(y_{j-1}-y_j)+(y_j-y_{j+1})
=\theta_j+\theta_{j+1}.
\]
The two original terms are either both included in \(T\), or both excluded, because their signs agree. All other terms are unchanged. Therefore \(\widetilde T=T\), as claimed at `proof-ROT-lowodd-v1.md:LF37–39`.

In particular, **\(k=2\to1\)** causes no indexing exception: \(y_{j-1}=y_{j+1}\), so the new \(\theta\) is zero, equal to the sum of the two original \(\theta\)'s.

Every reduced GRX witness therefore gives an original witness. Taking the contrapositive proves avoidance preservation. No converse is claimed or needed.

Empty runs do not affect this mapping. Newly adjacent equal pieces need not be recombined into maximal blocks: retain the displayed representation, to which GRX applies. Iteration removes one even block each time, preserves all remaining block parities, and ends with either \(o\) odd blocks or one even block when \(o=0\). This validates `proof-ROT-lowodd-v1.md:LF40–41`.

K1 and K2’s arguments require only the corresponding constant-block representation, not maximality. Moreover, if the final two odd pieces are adjacent equal pieces across an empty run, they physically form one even constant block; K1 rules that case out anyway. Thus the change of maximality creates no gap in the final application.

**Q3 — Z1/Z2: elementary inverse proofs**

The proofs at `proof-ROT-lowodd-v1.md:LF15–27` are valid.

For **D**, take the \(n+1\) prefix sums including zero of any \(n\) terms in \(C_n\). Two coincide, giving a nonempty zero-sum subsequence of length at most \(n\).

For **Z1**, write the terms as \(a_1,\ldots,a_{n-1}\). In **every ordering**, their prefix sums are distinct and nonzero: a zero prefix or equal prefixes would exhibit a nonempty zero-sum subsequence. They therefore exhaust \(C_n\setminus\{0\}\).

Swapping \(a_1,a_2\) changes only the first prefix sum. The unchanged prefixes already occupy every nonzero element except the old first prefix, so the replacement first prefix must equal it. Hence \(a_1=a_2\). Any two occurrences can be placed first, forcing all terms equal to \(g\). Zero-sum-freeness excludes \(jg=0\) for \(1\le j<n\), so \(g\) has order \(n\). The actual applications have \(n=2p\ge10\); the trivial smaller cases present no issue.

For **Z2**, in every ordering the even-indexed prefixes
\[
P_2,P_4,\ldots,P_{2p-2}
\]
are \(p-1\) distinct, nonzero elements of \(\{0\}\times C_p\). They therefore exhaust its \(p-1\) nonzero elements.

Swap positions \(2,3\). Only \(P_2\) changes; all other even prefixes remain fixed. Exhaustion forces \(P_2\) to remain unchanged, giving
\[
a_1+a_2=a_1+a_3,\qquad a_2=a_3.
\]
Any two occurrences can occupy positions \(2,3\), so all terms equal \(g=(1,c)\). These positions exist throughout the stated range. If \(c=0\), two copies already sum to zero. Thus \(c\ne0\); because \(p\) is prime and odd, \(g\) has order \(2p\).

There is no unrestricted inverse theorem for length \(2p-2\) hidden here: the first-coordinate hypothesis is essential to the even-prefix exhaustion and remains true in every application of Z2.

**Q4 — K1/K2: packing, CRT, availability and endpoints**

First, the shared EGZ application is correct. If \(R\ge3p-1\), apply classical EGZ to \(2p-1\) rotation occurrences and remove the resulting \(p\)-term zero-sum. At least \(2p-1\) rotations remain, so apply EGZ again. The two selections are disjoint, and their union is an identity \(2p\)-subword because rotations commute. Hence
\[
R\le3p-2.
\]
This also excludes \(F=0\) at length \(4p-2\). The bounds used at `proof-ROT-lowodd-v1.md:LF46–47, LF67–68` are justified without importing EGZ at \(2p\).

The pairs bound is elementary: choose \(p\) disjoint adjacent equal reflection pairs inside constant blocks; their selected product is a product of \(p\) identities.

For **K1**, these bounds give
\[
F\le2p-1,\quad 2p-1\le R\le3p-2,\quad
s=R-(2p-1)\in[0,p-1].
\]
The normalized one-block pattern is uniquely \(+\). Its feasible reflection counts give minimum rotation count \(s+1\) when \(s\) is odd, and \(s+2\) when \(s\) is even. Since every zero-sum in \(Y\) has even length, the single interval \([s+1,2p]\) in (*) is exactly equivalent. There is no parity or range enlargement error in `proof-ROT-lowodd-v1.md:LF47–50`.

When \(s=0\), every possible nonempty zero-sum in \(Y\), whose length is \(2p-1\), is forbidden. Z1 gives \(Y=g^{2p-1}\), with \(g=(1,c)\) a generator and \(c\ne0\).

For \(s\ge1\), at each packing step with \(|Z|\le s-1\), the remainder has at least \(2p\) terms. D supplies a nonempty zero-sum \(U\) of length at most \(2p\), and (*) forces \(|U|\le s\). The disjoint union satisfies
\[
|Z\sqcup U|\le2s-1\le2p-3,
\]
so (*) forces its length back to at most \(s\). Its length strictly increases. Consequently the loop must reach exactly \(s\); an odd \(s\) is impossible because all these lengths are even. This verifies termination and exact size at `proof-ROT-lowodd-v1.md:LF53–56`.

For even \(s\ge2\), the remainder has length \(2p-1\). Any nonempty zero-sum \(U'\) there would have even length between \(2\) and \(s\). Then \(Z\sqcup U'\) would have forbidden length between \(s+2\) and \(2s\le2p-2\). Thus the remainder is zero-sum-free and equals \(g^{2p-1}\) by Z1.

The CRT coefficient step is sound. Since \(g=(1,c)\) has order \(2p\), every \(h\) has a unique coefficient modulo \(2p\). Its first coordinate \(1\) forces that coefficient to be odd, represented by
\[
a_h\in\{1,3,\ldots,2p-1\}.
\]
Set \(e_h=2p-a_h\). There are enough remainder copies of \(g\) to form \(h+e_hg=0\), whose even length \(b_h=1+e_h\) lies in \([2,2p]\). Hence (*) forces \(b_h\le s\).

The \(s\) terms of \(Z\) give total \(\sum b_h\ge2s\). At the first cumulative sum \(\lambda_i\ge s+1\),
\[
i\ge2,\qquad
s+1\le\lambda_i\le2s\le2p-2.
\]
The construction uses \(\lambda_i-i\le2s-2\le2p-4\) copies of \(g\), fewer than the available \(2p-1\). It is therefore a genuine forbidden subsequence. All positive \(s\) are excluded. This checks `proof-ROT-lowodd-v1.md:LF57–61`.

The examples at line 62 also check: an identity would require an even rotation count \(m\in[2,2p-2]\) with \(mc=0\). No such even \(m\) is divisible by odd \(p\).

For **K2**, the number of available equal reflection pairs is
\[
H=\frac{\ell_1-1}{2}+\frac{\ell_2-1}{2}=\frac{F-2}{2}.
\]
Avoidance gives \(H\le p-1\), hence \(F\le2p\). The EGZ bound gives \(F\ge p\), and evenness strengthens this to \(F\ge p+1\). Therefore
\[
0\le t=\frac{2p-F}{2}\le\frac{p-1}{2},
\qquad R=2p-2+2t.
\]
The all-plus pattern has \(C_{\max}=F-2\), so (**) is exactly the asserted necessary condition. No sufficiency of this single pattern is assumed. See `proof-ROT-lowodd-v1.md:LF66–70`.

For **\(t=0\)**, \(Y\) has length \(2p-2\), and every possible nonempty zero-sum is directly forbidden. Take \(Z=\varnothing\); Z2 applies immediately. The packing loop is skipped.

For **\(t\ge1\)**, while \(|Z|\le2t-2\), the remainder has at least \(2p\) terms. D and (**) supply a nonempty even zero-sum \(U\) of length at most \(2t\). Then
\[
|Z\sqcup U|\le4t-2\le2p-4,
\]
and (**) forces the new length to be at most \(2t\). Strict growth through even lengths forces termination at exactly \(2t\).

The remainder has length \(2p-2\). A nonempty zero-sum there would have even length between \(2\) and \(2t\); adjoining \(Z\) produces forbidden length in
\[
[2t+2,4t],\qquad 4t\le2p-2.
\]
Thus Z2 gives the remainder \(g^{2p-2}\). This verifies `proof-ROT-lowodd-v1.md:LF71–74`, including the separate \(t=0\) endpoint.

If \(Z\) contained two copies of \(g\), together with the remainder they would give the forbidden \(g^{2p}\). Hence at least \(2t-1\) terms of \(Z\) differ from \(g\).

For each such \(h\), the odd CRT coefficient excludes \(1\):
\[
3\le a_h\le2p-1,\qquad
1\le e_h=2p-a_h\le2p-3.
\]
Thus the required \(e_h\) copies are available among the \(2p-2\) remainder copies. The zero-sum \(h+e_hg\) has even length at most \(2p-2\), so (**) gives \(e_h\le2t-1\). The exclusion \(h\ne g\) is precisely what makes this availability argument valid. See `proof-ROT-lowodd-v1.md:LF74–76`.

For **\(t=1\)**, this forces \(e_h=1\), hence \(h=-g\). Every term is therefore \(g\) or \(-g\).

For **\(t\ge2\)**, there are at least \(2t-1\) non-\(g\) terms. Their increments \(b_h=1+e_h\) are even, lie in \([2,2t]\), and have total at least
\[
2(2t-1)=4t-2\ge2t+2.
\]
At the first cumulative sum \(\lambda_i\ge2t+2\), the preceding sum is even and at most \(2t\). Hence
\[
i\ge2,\qquad
2t+2\le\lambda_i\le4t\le2p-2,
\]
and the required copies satisfy
\[
\lambda_i-i\le4t-2\le2p-4<2p-2.
\]
The resulting subsequence exists and contradicts (**). This verifies `proof-ROT-lowodd-v1.md:LF77–79`.

At the extreme \(t=(p-1)/2\), the bounds are exactly \(4t=2p-2\) and \(4t-2=2p-4\). For \(p=5\), the first \(t\ge2\) case is \(t=2\), and both bounds remain valid. Thus all requested endpoints are covered.

**Q5 — ROT-o2: exact universal scope**

The conclusion at `proof-ROT-lowodd-v1.md:LF84–89` follows for the stated number of **odd maximal constant reflection blocks**.

First exclude \(F=0\) by the two-selection EGZ argument. Start with the maximal constant pieces, including pieces created by changes of reflection value within a reflection run. PM* then preserves the rotation multiset and avoidance while eliminating even pieces.

- **\(o=0\):** the final representation has one even block. K1 requires its reflection count to be \(2p-1\), a contradiction.
- **\(o=1\):** K1 gives \(F=R=2p-1\) and all rotation values equal to one nonzero \(c\). These counts and the rotation multiset are preserved.
- **\(o=2\):** K2 gives all rotation values in \(\{c,-c\}\), with \(c\ne0\).

This covers arbitrarily many reflection runs and constant pieces, provided at most two constant pieces have odd length. It requires no original reflection constancy.

Nothing establishes the conclusion for \(o\ge3\), reflection constancy, or full ordered Olson. The parity remark is correct:
\[
o\equiv F\equiv R\pmod2,
\]
because \(F+R=4p-2\) is even.

**Q6 — hypotheses, circularity and corrections**

No counterexample or mathematical gap was found under the stated hypotheses. There is no circularity: GRX is proved directly; PM* uses that criterion; K1/K2 use necessary GRX conditions and independently proved zero-sum lemmas; the corollary applies these results in that order.

The relevant assumptions are explicit or definitional: \(p\ge5\) prime, word length \(4p-2\) for ROT, positive constant-block lengths, ordered subsequence selection, and \(\Sigma_0=\{0\}\). Primality is used when nonzero \(c\) makes \((1,c)\) a generator. Maximality is needed to identify the original scope, not to validate GRX or the merging construction.

**Severity:** FATAL — none; MAJOR — none; MINOR — no required correction. The normalized interpretation of the GRX product formula is already justified by its global-sign argument.

- **Fully checked:** GRX in both directions; all count intervals, signs, cyclic-order issues and degeneracies; PM* including empty runs and \(2\to1\); D, Z1 and Z2; the pairs bound; CRT coefficients and generation; both packing arguments, copy availability and endpoint arithmetic; and the exact ROT-o2 scope.
- **Imported:** classical EGZ for \(C_p\): every sequence of \(2p-1\) elements contains a \(p\)-term zero-sum. Its two disjoint applications were checked above. No parent proof, inverse theorem, finite computation, or control in `notes-GRX-v1.md:LF47–54` is imported.