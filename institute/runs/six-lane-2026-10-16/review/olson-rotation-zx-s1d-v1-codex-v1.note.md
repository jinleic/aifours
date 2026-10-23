**S1(d) is mathematically sound relative to the declared classical imports.** The only required fix is Savchev’s initial. No FATAL or MAJOR finding emerged.

| Claim | Verdict |
|---|---|
| S1(d) | **AWF** — bibliographic correction only |
| S1++ | **ACCEPT** |
| Terminal ROT-ZX++ | **ACCEPT** |
| Uniform INV*-ZX++ | **ACCEPT** |
| Ordered OLSON-ZX++ | **ACCEPT** |

AWF means accept with fixes. These verdicts retain the stated hypotheses and SOURCE02’s mandatory overlay.

All seven SHA256 digests and byte counts match the supplied manifest. I used static snapshot reads and hashes only. No interpreter, execution of mathematical searches, network, writes, delegation, or outside-path reads were used.

The classical imports are \(D(C_{2p})=2p\), EGZ over \(C_p\), and the index-one theorem recorded in SOURCE01. The \(C_p\) Davenport instance also has the valid prefix-sum proof in SOURCE04:LF15–17. I audited the new argument, applicability of these imports, and the downstream parameter and deletion calculations. The accepted ZX/S1+ results and their GRX, PM*, K1, DAV, MULT, SHgen/SHgen-E, restricted REFL, and RGR-LONG dependencies remain imports at SOURCE02’s stated scopes. Their underlying external proofs were not independently re-established here. Neither unreviewed residual notes nor UNKNOWN search outcomes enter the reasoning.

1. **Shortest long zero-sum and its proper subsums — valid.**  
   At SOURCE00:LF47–55, every zero-sum has even length. Thus failure of the claimed bound supplies a shortest \(T\) with \(N\ge p+5\), and (ZP) forces \(N\ge2p+2\). Davenport applied after deleting one occurrence supplies a nonempty proper zero-sum. For every such subsequence \(U\), both \(U\) and \(T-U\) are shorter zero-sums. Minimality therefore bounds both lengths by \(p+3\), giving
   \[
   N\le2p+6,\qquad N-p-3\le |U|\le p+3.
   \]
   Hence \(N\in\{2p+2,2p+4,2p+6\}\). The lower bound applies to every nonempty proper zero-subsum.

2. **EGZ half-sum and Claims A/B — valid.**  
   SOURCE00:LF57–65 correctly applies EGZ to second coordinates of \(2p-1\) occurrences. Its \(p\)-term selection \(T_1\) has group sum \((1,0)\), since \(p\) is odd. Consequently \(M=T-T_1\) has odd length \(N-p\) and second-coordinate sum zero.

   For Claim A, an even \(x\)-zero-sum \(V\) is a proper group zero-sum. An odd such \(V\), with \(|V|\le p\), combines disjointly with \(T_1\) into a proper zero-sum of length at most \(2p<N\); therefore \(|V|\le3\). Claim B also follows: two disjoint short half-sums would give a proper zero-sum of length at most six, whereas its required minimum is
   \[
   N-p-3\ge p-1\ge10.
   \]

3. **Excluding \(N\ge2p+4\) — valid.**  
   At SOURCE00:LF67–72, Claim A would require every even \(x\)-zero-sum of length at most \(p\) to have length at least \(p+1\), which is impossible. Davenport therefore supplies an odd half-sum \(V_1\) of length at most three. Since \(|M|\ge p+4\), removing it leaves at least \(p+1\) occurrences. A second Davenport application supplies a disjoint \(V_2\), contradicting Claim B.

   Thus \(N=2p+2\), and the only possible proper zero-sum lengths are \(p-1,p+1,p+3\).

4. **Excluding \((1,0)\) — valid, including occurrence accounting.**  
   SOURCE00:LF74–79 fixes one occurrence \(u=(1,0)\), then chooses the EGZ selection among the other \(2p+1\) occurrences. Thus \(u\in M\), without any overlap ambiguity.

   Davenport on \(M-\{u\}\), whose length is \(p+1\), gives \(V\) of length at most \(p\). If odd, it contradicts Claim B together with the separate occurrence \(u\). If even, Claim A forces \(|V|=p-1\). Exactly two occurrences remain in \(M-\{u\}-V\); their second coordinates sum to zero because those of \(M,u,V\) do. They therefore form a forbidden length-two group zero-sum. No second Davenport application is needed in this latter branch.

5. **The factorization \(M=C\,V\) and minimality over \(C_p\) — valid.**  
   SOURCE00:LF81–91 obtains a three-term half-sum \(C\), either directly or as the complement of a \((p-1)\)-term even zero-sum. Its complement \(V\) has length \(p-1\) and second-coordinate sum zero.

   Crucially, the proof establishes minimality of the second-coordinate sequence over \(C_p\), not merely minimality over \(C_{2p}\). A proper even \(x\)-zero-sum would violate the minimum proper group-zero-sum length. A proper odd one has an odd \(x\)-zero-sum complement in \(V\). Claim A bounds both lengths by three, forcing \(p-1\le6\), impossible here.

6. **Classical index-one application — valid at the declared scope.**  
   SOURCE00:LF93–97 uses exactly the theorem recorded in [SOURCE01:LF7–17](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-zx-s1d-v1-review-v1/snapshot/01-classical-index-one-primary-record.md:7). Its input is now a minimal zero-sum over \(C_p\) of length \(p-1\), and
   \[
   p-1\ge\lfloor p/2\rfloor+2
   \]
   holds for primes \(p\ge5\). The basis element \(h\) cannot be zero, since \(V\) has no zero second-coordinate term; hence it has order \(p\).

   The \(p-1\) positive coefficients summing to \(p\) must be \(p-2\) ones and one two. Thus
   \[
   V=\widehat h^{\,p-2}y,\qquad
   \widehat h=(1,h),\quad y=(1,2h).
   \]
   This deduction is audited; the classical theorem itself is imported, not proved self-containedly.

7. **Classification of every other term — valid.**  
   At SOURCE00:LF99–109, write \(x(z)=ch\), excluding \(c=0,1\).

   If \(c\) is even, \(\beta=p-c\) is odd and satisfies \(1\le\beta\le p-2\). The fixed \(V\) supplies enough \(\widehat h\) occurrences, all distinct from \(z\). Hence \(\widehat h^\beta z\) is a proper even zero-sum of length at most \(p-1\). Its length must equal \(p-1\), forcing \(c=2\).

   If \(c\ge3\) is odd, then \(c\le p-2\), so \(j=p-2-c\) lies in \([0,p-5]\). Such \(z\) is outside the fixed \(V\), whose terms have coordinates \(h\) or \(2h\). Therefore its fixed \(y\) and \(j\) copies of \(\widehat h\) are available disjointly from \(z\). The resulting zero-sum has even length \(p-c\le p-3\), a contradiction. The endpoint \(j=0\) is legitimate.

8. **Multiplicity contradiction — valid.**  
   SOURCE00:LF111–116 has \(t+u=2p+2\) and \(u+2\equiv0\pmod p\). Nonnegative multiplicities therefore allow only \(u=p-2\) or \(2p-2\). The latter gives \(t=4<p-2\), contradicting the copies already present in \(V\).

   Thus \(u=p-2,\ t=p+4\). The available subsequence
   \[
   \widehat h^{\,p-6}y^3
   \]
   has second-coordinate sum \(ph=0\) and even length \(p-3<p-1\), contradicting Step 3.

At **\(p=11\)**, the candidate shortest long zero-sum has length 24, with proper zero-sum lengths restricted to \(10,12,14\). The final construction has length eight. Every strict inequality used above holds.

At **\(p=7\)**, the six-term obstruction is allowed because \(6=p-1\). For a generator \(g\in C_{14}\), the control \(g^{13}(5g)^3\) has nonempty zero-sum lengths exactly \(6,10,16\): solving \(a+5b\equiv0\pmod{14}\), with \(0\le a\le13,\ 0\le b\le3\), gives those lengths. It excludes lengths 12 and 14 but violates the bound ten. Thus the boundary failure is mathematical, not merely a missing estimate. No new claim at \(p=5\) or \(7\) follows.

**S1++ follows correctly** at SOURCE00:LF125–126: integer \(\kappa\) leaves exactly one new value beyond accepted S1+, namely \((p+3)/2\).

The **terminal corollary** at SOURCE00:LF130–136 also follows. It requires **some** admissible normal form, with no uniqueness assumption. Handle \(k=1\) first through K1, including the nonzero rotation value. For \(k\ge2\), \(F\equiv k\pmod2\) makes \(\widehat\kappa\) integral. Its nonnegativity follows independently from GRX: \(H\ge p\) would already yield an identity selection using zero rotations. DAV then gives \(\widehat\kappa\le k-1\), and GRX supplies (ZP).

The accepted SHgen-E caller conditions remain discharged: \(E\le k-1\),
\[
2H\ge2p-2k\ge k-1\ge E,
\]
and the other SHgen inequality follows from \(5k\le4p-1\). Expansion base words retain the representation and satisfy \(o_F=k\le p\). Applying restricted REFL to the **original** word still requires its separate condition \(o_F(w)\le p\), exactly as stated.

The **uniform hypothesis** is correctly grouped as
\[
3o\le2p+1
\quad\text{and}\quad
\left[o\le\frac{p+5}{2}\ \text{or}\ F\ge o+p-5\right].
\]
The low-\(o\) branch gives \(\widehat\kappa\le k-1\le o-1\). The high-\(F\) branch gives
\[
\widehat\kappa\le p-1-\frac{F-o}{2}\le\frac{p+3}{2}.
\]
Moreover \(o\le(2p+1)/3\le p\), so original-word REFL applies.

The **ordered Olson deletion argument** preserves both branches:

- Case 1: \(R\le2\) gives \(F\ge4p-3\), while \(3o\le2p+1\) implies \(o\le2p-3\). Thus \((F-o)/2\ge p\) disjoint equal pairs exist. SOURCE06’s cyclic framing and conjugation argument preserves an identity selection in increasing original order.
- Case 2: deleting one reflection from an odd block of length at least three gives \((o',F')=(o-1,F-1)\).
- Case 3: deleting two distinct rotation **occurrences separately** gives two words, each with parameters \((o,F)\) or \((o-2,F)\).

Consequently \(o'\le o\) and \(F'-o'\ge F-o\). Both uniform branches and the \(3o\) bound survive. Restoring the reflection in Case 2 preserves INV*. In Case 3, a third rotation shared by both deletions identifies their nonzero pairs, and existing reflection adjacencies persist. RGR-LONG then completes the contradiction.

The range table is correct:

| \(p\) | Coverage without extra \(F\) | Additional coverage |
|---:|---:|---|
| 11 | \(o\le7\) | — |
| 13 | \(o\le9\) | — |
| 17 | \(o\le11\) | — |
| 19 | \(o\le12\) | \(o=13,\ F\ge27\) |
| 23 | \(o\le14\) | \(o=15,\ F\ge33\) |

The numerical residual starts at \(\widehat\kappa\ge(p+5)/2\), requiring \(k\ge(p+7)/2\); feasibility first occurs at \(p=19\). All displayed residual pairs, including those for \(p=29\), are arithmetically correct. This describes limits of the numerical sufficient criterion. Actual (S1), another normal form, or another argument may still suffice. It establishes neither necessity nor nonexistence outside the ranges, and assumes no new-range avoiders exist.

**Finding: MINOR — [SOURCE00:LF23](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-zx-s1d-v1-review-v1/snapshot/00-S1d-addendum-v1.md:23).** Replace **“V. Savchev”** with **“S. Savchev”**, as explicitly documented in SOURCE01:LF7, LF14 and LF17. No mathematical statement or proof step needs alteration.