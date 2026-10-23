All nine SHA-256 hashes match. **0 FATAL, 0 MAJOR, 0 MINOR**, under the stipulated integer-\(\kappa\) convention and the stated imports.

| Claim | Verdict |
|---|---|
| S1(c), SOURCE00:L27–48 | **ACCEPT** |
| Integer-range consequence S1+, SOURCE00:L50–51 | **ACCEPT** |
| ROT-ZX+ terminal, SOURCE00:L58–61 | **ACCEPT** |
| Uniform ROT-ZX+, SOURCE00:L63–70 | **ACCEPT** |
| Uniform INV*-ZX+, SOURCE00:L63–72 | **ACCEPT** |
| Uniform OLSON-ZX+, SOURCE00:L74–82 | **ACCEPT** |

**S1(c) is valid.** Each step survives the multiset and parity checks.

1. **Shortest long zero-sum — SOURCE00:L31–38.** Failure of (S1) supplies a zero-sum of even length at least \(p+3\). Choose one, \(T\), of minimum such length \(N\). By (ZP), \(N\ge2p+2\).

   Delete one occurrence from \(T\). The remaining sequence has at least \(2p+1\) terms, so Davenport supplies a nonempty zero-sum contained strictly in \(T\). Thus the subsequent argument about proper zero-sums is nonvacuous.

   For **any** proper nonempty zero-sum \(A\le T\), its complement \(B=T-A\) is also a nonempty zero-sum. Both are shorter than \(T\); minimality and evenness give
   \[
   |A|,|B|\le p+1.
   \]
   Therefore \(N\le2p+2\), forcing \(N=2p+2\). Since their lengths sum to \(2p+2\), both must equal \(p+1\). This proves the asserted universal restriction on proper zero-sums.

2. **EGZ selection — SOURCE00:L39–40.** Apply EGZ to the \(x\)-coordinates of any \(2p-1\) occurrences of \(T\). It supplies \(T_1\) of length \(p\) and \(x\)-sum zero. Since \(p\) is odd,
   \[
   s(T_1)=(1,0).
   \]
   Consequently \(M=T-T_1\) has length \(p+2\) and sum
   \[
   s(M)=-(1,0)=(1,0).
   \]
   Repeated coordinates and repeated group elements are permitted by EGZ.

3. **Classification of \(V\) — SOURCE00:L41–45.** Take any nonempty \(V\le M\) with \(x\)-sum zero and \(|V|\le p\).

   If \(|V|\) is even, \(V\) is a proper nonempty zero-sum of \(T\), contradicting its required length \(p+1\).

   If \(|V|\) is odd, \(s(V)=(1,0)\). Because \(V\) and \(T_1\) use disjoint occurrences, \(T_1V\le T\) is a zero-sum. Its length is at most \(2p<N\), so it is proper. The preceding restriction gives
   \[
   p+|V|=p+1.
   \]
   Hence \(V\) consists of one occurrence of \((1,0)\). This conclusion applies to every qualifying \(V\) in the original \(M\).

4. **Repeated Davenport application — SOURCE00:L46–48.** Choose any \(p\) occurrences of \(M\). Davenport in \(\mathbb Z_p\) supplies a qualifying \(V\), hence an occurrence \(u_1=(1,0)\). Delete exactly that occurrence. There remain \(p+1\) terms, so another choice of \(p\) terms supplies \(u_2=(1,0)\).

   The second selection is still a subsequence of the original \(M\), so step 3 applies unchanged. The occurrences \(u_1,u_2\) are distinct even though their values coincide. Together they form a proper zero-sum of length \(2\), contradicting the required length \(p+1\).

There is no assumption that \(T\), \(T_1\), or \(M\) initially avoids \((1,0)\). Two such occurrences in \(T\) would already contradict step 1; zero or one causes no difficulty in the argument. At \(p=5\), the hypothetical \(T\) has length \(12\), proper zero-sums length \(6\), and \(M\) length \(7\). At \(p=7\), these lengths are \(16,8,9\). Both Davenport applications remain available.

**S1+ and the terminal consequence are valid.** For integer \(0\le\kappa\le(p+1)/2\), either \(\kappa\le(p-1)/2\), covered by S1(a), or \(\kappa=(p+1)/2\), covered above. There is no intervening integer. At \(\kappa=0\), Davenport excludes any zero-sum under (ZP), so (S1) holds vacuously.

For SOURCE00:L55–61, the normal-form interface supplies integer \(\widehat\kappa\ge0\), DAV supplies \(\widehat\kappa\le k-1\), and GRX supplies (ZP). S1+ therefore supplies exactly the (S1) hypothesis required by SOURCE01:L203–234. The ZX and SHgen estimates retain their stated scope; they impose no additional \(\widehat\kappa\le(p-1)/2\) restriction. The \(k=1\) branch uses K1. The existential **“SOME normal form”** quantifier is correctly retained.

**Both uniform consequences are valid — SOURCE00:L63–72.** Since \(k\le o\), the condition \(3o\le2p+1\) supplies \(3k\le2p+1\). The two alternatives respectively give
\[
\widehat\kappa\le k-1\le o-1\le(p+1)/2
\]
or
\[
\widehat\kappa\le\kappa(w)
=p-1-\frac{F-o}{2}
\le(p+1)/2.
\]
ROT-ZX+ supplies the nonzero rotation pair. Restricted REFL then applies to the original word: its length is \(4p-2\), the pair is established, and \(o\le(2p+1)/3\le p\).

**The OLSON deletion argument is valid — SOURCE00:L77–82; SOURCE01:L256–266; SOURCE07:L28–47.**

| Deletion | Resulting \((o',F')\) | Resulting \(F'-o'\) |
|---|---|---|
| One reflection from an odd constant block of length at least three | \((o-1,F-1)\) | \(F-o\) |
| One rotation occurrence | \((o,F)\) or \((o-2,F)\) | \(F-o\) or \(F-o+2\) |

The reflection block remains nonempty, preventing additional fusion. Rotation deletion can merge neighbouring equal-valued blocks; their parity calculation lowers \(o\) by two exactly when both were odd. Thus both sufficient branches, and the \(3o\) bound, survive every required deletion.

For \(R\le2\), \(F\ge4p-3\) and \(o\le2p-3\), yielding at least \(p\) disjoint equal reflection pairs; SOURCE07’s cyclic framing and conjugation argument preserves increasing-index identity selection.

For the other cases, reinsertion into the surviving constant block preserves RGR. With rotation deletions, a third shared rotation identifies the two nonzero pairs, while existing adjacent unequal reflections survive deletion. RGR-LONG then applies.

**Coverage and residual — SOURCE00:L88–109.** The stated arithmetic is correct:

- \(p=7\): every avoider with \(o\le5\), without an additional \(F\) condition.
- \(p=11\): every avoider with \(o\le7\), likewise.
- \(p=13\): \(o\le8\), plus \(o=9,\ F\ge19\).
- \(p=17\): \(o\le10\), plus \(o=11,\ F\ge25\).

The same numerical bounds apply to the OLSON word class. Within \(3k\le2p+1\), DAV makes the numerical terminal residual empty at \(p=7,11\). The listed remaining pairs \((9,8)\) at \(p=13\) and \((11,10)\) at \(p=17\) are correct.

The residual wording is acceptable as a limitation of these numerical sufficient conditions. Higher \(\widehat\kappa\) does not establish failure: actual (S1), or another admissible normal form, may still give terminal coverage.

I audited S1(c), the displayed \(\mathbb Z_p\) Davenport prefix-sum proof, the S1+ deduction, consequence interfaces, deletion/reconstruction arguments, and coverage arithmetic. I imported EGZ, \(D(\mathbb Z_{2p})=2p\), ZX, MULT, GRX/PM*/K1, normal form/DAV, SHgen/SHgen-E, restricted REFL, and RGR-LONG at the supplied scopes. SOURCE08 was contextual evidence, not a substitute for this audit.