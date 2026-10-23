**DISPOSITION: ACCEPT-WITH-FIXES for the written mathematics**, conditional on the separately stipulated exact verification of the finite certificates. I found no FATAL or MAJOR defect in the essential mathematical path. The fixes below are local; they do not require a new elimination rule.

All eight SHA-256 hashes match. References below use physical snapshot-file line numbers. The summary JSON establishes neither enumeration completeness nor certificate validity by itself.

Three MINOR findings:

- **MINOR, essential justification — [SOURCE00:53](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset5-written-proof-review-v1/snapshot/00-proof-v1.md:53).** R5 is true, but applying R4 to the full \(S_C\) only produces *some* pair with sufficiently large gcd. It does not necessarily select the specified \(j,k\). **Repair:** restrict to the configuration consisting of \(v,j,k\), or apply Sun’s \(k=2\) result directly to the two disjoint fibre pieces inside \(U_v\). This proves precisely \(\gcd(d_j,d_k)\ge2\).

- **MINOR, unused commentary — [SOURCE01:139](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset5-written-proof-review-v1/snapshot/01-rules-v1.md:139).** The claimed linking vertex for the Corollary 3.11 discussion is wrong. For triangle labels \(\alpha_{UV}=1,\alpha_{UW}=\alpha_{VW}=p\), the forced value is \(\tau=p\); K1 links occur at \(U,V\), not at the shared vertex \(W\), whose product is \(p^2\).

  An explicit counterexample to that local inference is \(G=\mathbf F_2^3\), \(U=V=\langle e_1\rangle\), \(W=\langle e_2\rangle\), with disjoint cosets
  \[
  U,\qquad e_2+V,\qquad e_3+W.
  \]
  Their labels are \(1,2,2\), and \(\tau=2\). At \(W\), neither K1 containment holds: \(W+U\) has four elements whereas \(V+U=U\) has two. **Repair:** name \(U\) or \(V\). The formal L2/K1 rules are correct, and the engine path does not need this erroneous explanatory sentence.

- **MINOR, unused control — [SOURCE01:266](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset5-written-proof-review-v1/snapshot/01-rules-v1.md:266).** Arbitrary one-label mutation need not invalidate a certificate. For example, the T witness \(\alpha_{01}=\alpha_{02}=1,\alpha_{12}=3\), with no E3 vertex, has \(\tau_{\min}=3>\tau_{\max}=1\). Changing the unrelated edge \(\alpha_{34}\) leaves that witness valid. **Repair:** require selected mutations that actually invalidate the stated witness, or describe C4 simply as certificate rechecking. Neither version substitutes for exhaustive exact verification.

I audited the essential path as follows.

1. **Finite quotient and full-target minimality are sound.**

   SOURCE02:28 uses the intersection of the five normal cores. Each core has finite index through the action on the finite coset space, so their intersection \(N\) is normal of finite index. Because \(N\subseteq G_i\), each original coset is a full inverse image from \(G/N\). Disjointness, subgroup indices, and intersection indices are preserved.

   SOURCE00:18 and SOURCE01:30 correctly minimize over **all finite counterexamples to the full five-coset target**. Therefore every proper subgroup satisfies the five-coset theorem, including configurations whose indices do not initially have Core(5) form. This is exactly the minimality needed later in F2. It introduces no solvability or bounded-order hypothesis.

2. **R1 reaches Core(5) without losing cases.**

   By the two-coset theorem, every pairwise gcd is \(2,3,\) or \(4\). If one index is odd, its gcd with every other index must be \(3\), so all five indices are divisible by \(3\). Every pairwise gcd is then exactly \(3\); division by \(3\) gives pairwise coprime cofactors, contradicting the imported four-coset result.

   Otherwise all indices are even. Writing \(n_i=2^{e_i}m_i\), the odd parts are pairwise coprime, and at most one \(e_i\) exceeds \(2\). Two indices with \(e_i=1\), together with any third, give the prohibited \((2r,2r',2r'')\) shape: only the third cofactor can be even. Exactly one such index gives the prohibited \((2r_1,4r_2,4r_3,4r_4)\) shape with \(r_1\) odd. Otherwise division by \(4\) gives pairwise coprime \(r_i\).

   The stronger M–S Proposition 4.5 is genuinely needed here; Sun’s four-coset theorem alone does not prohibit its shape. Its precise hypotheses match [SOURCE03:249](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset5-written-proof-review-v1/snapshot/03-M-S-primary-imports.md:249).

   The implication-arrow labels in SOURCE02:38–39 are reversed; swap them. Both mathematical implications are nevertheless established.

3. **The product, intersection and triangle calculus is valid.**

   L0.1–L0.5 use cardinalities and invariance of product **sets**, without assuming those products are subgroups. In particular,
   \[
   |U_iU_j|=\frac{\alpha_{ij}}{\gcd(n_i,n_j)}|G|
   \]
   follows directly from the subgroup product formula. Disjointness makes this product proper, giving \(\alpha_{ij}\in\{1,2,3\}\) in Core(5).

   The double-coset divisibility proof correctly uses \(A\cap xBx^{-1}\). The intersection \(AB\cap AC\) is invariant under left \(A\) and right \(B\cap C\), so its decomposition into the relevant double cosets is valid.

   For triples, subgroup containment gives divisibility of the triple-intersection index by all pair-intersection indices. Thus
   \[
   \tau_{\min}
   =\operatorname{lcm}_{xy}
     \frac{\alpha_{xy}}{\gcd(\alpha_{xy},r_z)}
   \]
   is correct. The product formula gives
   \[
   |U_y(U_x\cap U_z)|=\frac{\tau|G|}{4\alpha_{xz}},
   \]
   and containment in both adjacent products gives exactly the stated bounds on \(\tau\). No assumption about products being subgroups enters T.

4. **Linking and K have the correct orientations.**

   L2’s equal-cardinality containment is valid. Taking inverses correctly changes
   \(U_yU_x\subseteq U_yU_z\) into \(U_xU_y\subseteq U_zU_y\).

   For K, an overlap of \(g_iU_iU_v\) and \(g_jU_jU_v\) gives
   \[
   g_j^{-1}g_i\in U_jU_vU_i.
   \]
   Either specified containment reduces this to the forbidden subgroup product, in the appropriate orientation. The enlarged sets also avoid the entire nonempty coset \(g_vU_v\). Consequently their total size is strictly below \(|G|\), yielding the Core(5) bound \(\sum\alpha_{iv}\le3\).

   K2 correctly applies this result after inverting its hypothesis. The formal K rules do not inherit the erroneous explanatory linking-vertex sentence identified above.

5. **P’s quantization, bounds, and Bonferroni direction are correct.**

   The double-coset decomposition gives the intersection quantum
   \[
   u_{vjk}
   =\frac{|G|}{\gcd(n_v,I_{jk})}
   =\frac{|G|}{4\gcd(r_v,\alpha_{jk})}.
   \]
   Both lower bounds in P3 are necessary. Equality with the smaller set forces the stated containment, so lowering the upper bound by one quantum when K2 prohibits that equality is sound. Equal-sized sets require checking both containment directions.

   Bonferroni gives
   \[
   \sum |Y_j|-\sum |Y_j\cap Y_k|
   \le \left|\bigcup Y_j\right|
   \le |G|-|U_v|<|G|.
   \]
   Substitution makes its left side **decrease** with each \(|X_j\cap X_k|\). Hence testing all intersections at their upper bounds is conservative: failure even there excludes their true values. The strict inequality is justified by the common nonempty subset \(U_v\) of all \(X_j\).

6. **N2’s quadruple-index argument works.**

   With all labels \(2\), each triangle has even \(\tau\le4\). The value \(4\) supplies K1 links and contradicts K, leaving \(\tau=2\).

   At an odd-\(r_v\) vertex, quantization and K2 force
   \[
   X_j\cap X_k=U_v(U_j\cap U_k),
   \qquad |X_j\cap X_k|=|G|/4.
   \]

   For three other vertices \(j,k,l\), the fourfold-intersection index \(Q\) is divisible by
   \[
   \operatorname{lcm}
   (8r_vr_jr_k,\;8r_vr_jr_l,\;8r_vr_kr_l)
   =8r_vr_jr_kr_l.
   \]
   This equality follows from pairwise coprimality, including when some cofactors equal \(1\). Therefore
   \[
   |U_v(U_j\cap U_k\cap U_l)|\ge |G|/4.
   \]
   Its containment in three quarter-sized sets forces their equality. Applying this across the four other vertices identifies all six pairwise intersections. Four disjoint quarter-sized remainders plus their common quarter-sized intersection then require \(5|G|/4\) elements. No index exponent was bounded.

7. **H2 and the fibres in H are valid.**

   The \((1,2,2)\) triangle forces \(\tau=2\), giving
   \[
   U_vU_a=U_vU_b=X,\qquad |X|=|G|/2.
   \]
   Right invariance under both generating subgroups implies right invariance under \(W=\langle U_a,U_b\rangle\). Thus \(X=U_vW\), and \(W\ne G\).

   Since \(W\) contains \(U_a,U_b\), its index divides \(\gcd(4r_a,4r_b)=4\). Its properness leaves index \(2\) or \(4\). Cardinalities give exactly the two stated alternatives. The same \(W\) works for every relevant \(v\).

   For F, \(g_lU_l\) meets exactly
   \(t_l=[U_l:U_l\cap H]\) left \(H\)-cosets, even when \(H\) is not normal. A nonempty intersection in one such coset is \(y(U_l\cap H)\); translating into \(H\) preserves disjointness and gives index \(\lambda_l\).

   Sun’s results handle two through four pieces. Five pieces invoke minimality in the **proper** subgroup \(H\), supplied by H2. This is not circular application of the theorem in \(G\). Also, \(t_l=1\) really does imply \(U_l\subseteq H\), so the enumeration’s F3 constraints are sound.

8. **Both evaluation-point reductions are sound.**

   For M1, a link detected at \(\tau_{\min}\) realizes one of T2’s upper bounds. Any larger \(\tau\) would violate that bound. Such a link is therefore forced for every genuine configuration. P’s lower bounds only increase with \(\tau\), while its upper bounds are independent of it.

   For M2, the important formula is
   \[
   \lambda_l=(4/m)r_lt_l,\qquad m\in\{2,4\},\quad1\le t_l\le m.
   \]
   No prime at least \(5\) can enter a pairwise gcd: the \(r_l\) are pairwise coprime and the remaining multipliers have only primes \(2,3\).

   At each prime, at most one cofactor has a variable positive valuation. The other endpoint’s bounded multiplier caps the minimum valuation. Representative valuations \(v_2=4,v_3=4\) exceed every such cap, simultaneously for all pairs. Consequently every actual pairwise gcd divides its representative counterpart. Killing an assignment because all representative gcds are too small is valid for every actual assignment.

   These representatives impose no restriction on actual powers of \(2,3\), other prime factors, or cofactors equal to \(1\).

9. **Lemma R is sound after the specified pairwise clarification.**

   Distinct \((U_v,U_j)\)-double cosets justify R1. Double-coset divisibility justifies R2. Every right coset \(U_vy\subseteq D_j\) meets \(g_jU_j\), and a meeting point \(w\) gives
   \[
   g_jU_j\cap U_vy=(U_v\cap wU_jw^{-1})w.
   \]
   The subgroup has index
   \[
   [U_v:U_v\cap wU_jw^{-1}]
   =|D_j|/|U_j|=d_j.
   \]
   This index orientation is correct.

   Right translation identifies each fibre with a right coset inside \(U_v\); inversion gives disjoint left cosets there. Sun’s \(k\le4\) results therefore apply **inside \(U_v\)**. Neither conjugation nor inversion changes the relevant index.

10. **The S-D contradiction is exact.**

    At \(v=2\), \(X_0\) has size \(|G|/4\), and the other three products have size \(3|G|/4\). R1/R2 force their complements to equal \(D_1,D_3,D_4\), with indices \(d_j=r_j\). Pairwise coprimality and repaired R5 make those complements disjoint.

    The triangle values are indeed
    \(\tau_{012}=1,\tau_{023}=\tau_{024}=2\). Their product-set cardinalities imply \(X_0\subseteq X_1\cap X_3\cap X_4\). Thus the three complements partition \(G\setminus X_0\).

    Write \(d_0=s_0r_0\), where \(s_0\in\{1,2,3\}\). R5 excludes intersection with \(D_3,D_4\), since their cofactors are coprime to \(6\). Hence \(D_0\subseteq D_1\). Meeting \(D_1\) requires \(\gcd(s_0,r_1)>1\); evenness and \(3\nmid r_1\) force \(s_0=2\). This gives \(|D_0|=|G|/2>|D_1|=|G|/4\), the contradiction.

The finite bridge remains a separate obligation. Each genuine configuration determines an allowed \((\alpha,E2,E3)\) pattern, and all rules respect relabelling. Therefore an exhaustive exact replay of the stated witnesses—including every fibre assignment in **both** H2 alternatives—plus identification of the sole survivor as the exact S-D pattern suffices. Counts and sanity examples do not suffice.

**Audited versus imported:** I independently checked R0/R1’s reduction logic, the elementary L0 facts, T/L/K/P, N2, F/H2, M1/M2, R and S-D. The published theorem imports are Zhu’s all-groups \(k=3,4\) theorem and M–S Proposition 4.5; their supplied statements match the uses. Propositions 4.2/4.3 also match and follow from the imported Zhu theorem. Zhu’s full proof is absent, so it remains an import.

The supplied extraction already states the exclusion of \(\alpha=2\) in Lemma 4.4 and explicitly derives it; no unseen textual correction is needed. R2/R3, H1, the Corollary 3.11 commentary, and controls C1–C4 are outside the essential certificate path. No novelty or priority conclusion is made.