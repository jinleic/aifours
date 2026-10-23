**ACCEPT on all ten claims**, relative to the accepted dependencies and their mandatory overlays. All 12 supplied SHA256 hashes match. Findings: **0 FATAL, 0 MAJOR, 0 MINOR requiring correction. Required fixes: none.** Only snapshot reads and hash checks were used; no mathematical computation was run or accepted.

References below use the supplied SOURCE identifiers and snapshot line numbers.

1. **ARC — ACCEPT.** SOURCE00:34–38 correctly specializes GRX. The nonempty proper interval of run labels has exactly two sign changes, including when \(j'=j+1\). With \(\theta_i=y_{i-1}-y_i\),
   \[
   T(z_A)=-\sum_{i\in A}\theta_i=y_{j'}-y_j,
   \]
   so the target sign is correct. All blocks are odd by the admissible normal form, SOURCE03:37–43; therefore \(C_{\max}=F-(k-\Phi)=2H+\Phi\). For \(\Phi=2\), \(2\le C\le2H+2\) is equivalent to \(2\widehat\kappa\le m\le2p-2\), supplemented by \(0\le m\le R\). GRX itself permits arbitrary block parities; oddness is needed for this simplified upper endpoint. Empty runs and nonmaximal representations are explicitly covered by SOURCE02:7 and do not change this argument.

2. **DIST0 — ACCEPT.** SOURCE00:44–47 legitimately uses \(m=0\). SOURCE01:18 explicitly permits \(2p-C=0\); its proof chooses rotations independently of reflection counts. The empty submultiset has sum zero. More concretely, when \(y_j=y_{j'}\), select odd counts from those two blocks and even counts from all others, at their pattern-specific maxima. Their total is \(2H+2=2p\), and the selected reflection product is the product of two equal reflections. Thus no nonempty rotation selection is required. Distinctness of all \(p\) block values makes \(y\) bijective. Translation by nonzero \(t\) has order \(p\), so its conjugate \(\pi_t\) is one \(p\)-cycle.

3. **WIND — ACCEPT.** SOURCE00:49–53 correctly counts coverage of **labelled runs**, including empty ones. Following the single cycle of \(\pi_t\) concatenates all \(p\) forward arcs into one closed directed walk around the cyclic run labels. Such a walk traverses every directed edge equally often, giving an integer \(w_t\). Each arc has length between \(1\) and \(p-1\), since its endpoints differ. Consequently
   \[
   p\le pw_t\le p(p-1).
   \]
   Hence \(1\le w_t\le p-1\). No distribution or nonemptiness assumption about rotation letters enters.

4. **ONE0 — ACCEPT.** SOURCE00:55–67 handles both cases correctly. In one run, two distinct occurrences have \(t=x+x'\ne0\) by (ZP). Whenever that run is outside an arc, both signs are positive and ARC applies with \(m=2\). Avoidance would force the run into every arc, contradicting WIND. This actually proves that no run contains two rotation occurrences.

   For different runs with unequal values, take \(t=x-x'\ne0\). Avoidance gives the stated inclusion of membership sets; WIND gives equal cardinalities and hence equality. Every proper forward arc crosses each specified run at most once. Crossing exactly one of \(\alpha,\beta\) therefore means precisely that its endpoints lie in opposite parts of \(P/Q\). Equal membership forces \(\pi_t(P)\subseteq P\), impossible for a single cycle. Finally, \(R=p\ge2\) and (ZP) exclude the common value zero.

5. **ZP-D — ACCEPT.** SOURCE00:73–79 is a valid elementary proof. The four initial sums are distinct because \(a,b\) are nonzero, unequal and not inverses. If adding a later nonzero term failed to enlarge the subset-sum set, that set would be invariant under a nonzero translation. Primality forces it to equal \(\mathbb Z_p\). It would then contain \(-s_i\), represented by a nonempty earlier selection, contradicting zero-sum-freeness after adjoining \(s_i\). Thus every subsequent step grows, giving the impossible bound \(p+1\). The conclusion \(c\ne0\) follows immediately.

6. **PAIR1-P — ACCEPT.** SOURCE00:71 validly obtains (S1): \(\widehat\kappa=1\) is integral and lies inside SOURCE04:19’s accepted S1+ scope. Also \(R=p+2\) and \(H=p-2\) follow from the normal-form identities.

   All three branches at SOURCE00:86–101 work. SC0 applies at lengths \(p+2\) and \(p+1\), without extending its accepted threshold. In the deletion branch, \(W-L\) is even, so \(W-L\le p-2\) sharpens to \(p-3\). An involution partner would force \(W\ge2p\).

   In the \(a\ge3\) contradiction, \(h\) includes the occurrence \(v\). The estimate \(m_1-a\ge h+1\ge2\) supplies enough **distinct occurrences** of \(g\) inside \(Y_0\). They exclude \(u\), which was deleted, and exclude \(v\), whose coefficient is at least three. Thus \(g^a u\) is a genuine prohibited zero-sum. Consequently \(v=g,\ u=-g\); all remaining coefficients are positive and at most \(p-2\). There is exactly one negative coefficient in this branch, and no \(Y(0)\).

   In the remaining branch, pair intersection forces three occurrences of the unique odd involution. Four would create disjoint pairs. After deleting two, \(Y''\) is zero-sum-free. An even projected zero-sum contradicts this directly; an odd one does so after adjoining the remaining involution occurrence. ZP-D therefore gives exactly the stated exceptional family.

7. **TRIPLE-ARC — ACCEPT.** SOURCE00:103–109 correctly uses the \(p\) consecutive integers in \([-U_-,U_+]\) to represent every residue after multiplication by \(c\ne0\). The selected sign determines an available supply: \(D\le U_+\) or \(-D\le U_-\). Padding uses at most two of the three distinct zero-rotation occurrences and cannot overlap the selected \(c\)-letters. If \(|D|\) is odd, it is at most \(p-2\); otherwise no padding is needed, except two zeros when \(D=0\). Hence \(m\) is even and \(2\le m\le p-1\). Zero’s sign is irrelevant.

8. **Theorem ROT-KP — ACCEPT.** SOURCE00:118–125 correctly identifies the coefficients with SHgen weights: they are odd, canonical, bounded by \(p-2\), and exclude zero rotations. For \(E>0\),
   \[
   2H=2p-4\ge p-3\ge E,\qquad
   \eta+a_{\max}\le E+2\le p-1.
   \]
   The latter gives SHgen(K) exactly at \(k=p\). It uses KETA’s unrestricted weight inequality, accepted at SOURCE08:16, rather than its separate \(k\le p-1\) consequence.

   SHgen’s displayed setting has no hidden \(k\le p-1\) restriction. For empty runs, SOURCE03:47–70 and SOURCE10:26 permit SHgen-E at its own hypotheses. Expansions preserve \(k=p\), odd nonempty blocks, block values and genuine empty gaps. Thus each base word has length \(4p-2\), rotations in one nonzero pair, and \(o_F=p\). Its surviving empty gap joins different reflection values, contradicting restricted REFL if it avoided. SOURCE11:6 includes equality \(o_F=p\). Expanded \(\kappa\) need not remain one.

9. **INV*-KP — ACCEPT.** SOURCE00:131–133 correctly uses \(k\le o_F\), parity and
   \[
   \widehat\kappa=\kappa(w)-(o_F-k)/2\le1.
   \]
   For \(k\ge2\), integrality and GRX nonnegativity give \(\widehat\kappa\in\{0,1\}\). The one-even-block terminal case is already excluded by the accepted normal form. Proposition K1 covers \(k=1\), ROT-K01 covers \(2\le k\le p-1\), and ROT-KP covers \(k=p\). Restricted REFL then applies to the **original** word because \(o_F(w)\le p\).

10. **OLSON-KP — ACCEPT.** SOURCE00:134–135 preserves the accepted deletion conditions. Case 1 has \(o_F\le p\le2p-3\), supplying the framed-pair argument. Case 2 gives \((o-1,F-1)\), preserving \(F-o\). Each separate Case 3 deletion gives \((o,F)\) or \((o-2,F)\), so neither inequality deteriorates. Every shorter avoider therefore satisfies INV*-KP. The accepted case argument reconstructs the longer word’s required rotation and reflection-run structure before applying RGR-LONG; it does not apply that theorem to an arbitrary word.

Unverified here: proofs behind accepted import interfaces, including the classical index-one import, restricted REFL and RGR-LONG. They remain trusted at their recorded scopes. No finite output supports these verdicts, and no extension to \(\widehat\kappa\ge2\) at \(k=p\) or \(o_F>p\) is established.