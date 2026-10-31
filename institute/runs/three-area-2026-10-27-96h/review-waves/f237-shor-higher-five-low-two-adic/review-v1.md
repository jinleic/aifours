# f237 independent same-harness review: higher-five / low-two-adic slice

## Disposition and assurance

**Conditional written support**, with **0 fatal, 0 major and 2 minor scope/wording findings** below. Subject to the expressly unverified LL/T2 and ordinary-cyclotomic imports, the all-\(n\) exclusions and the stated necessary low-2-adic allocation follow by the reconstruction below. The \(|P|=4\cdot5^e\) branch is **not excluded** and **no anchored tiling or original-code witness is inferred**. The border caller is a separate conditional import. This is same-harness review, not a human, independent-model-family, formal/kernel, external-source, or novelty verification. The e=2, head100, f220 and later high-bit claims are not premises or conclusions.

Severity labels: F = fatal, M = major, m = minor. “0F/0M/0m” in a branch row means the stated branch deduction has no finding; it is conditional where its proof uses T2. INCONCLUSIVE is used for an unverified import, provenance, or unresolved existence/exclusion, not a pass.

### Per-branch verdicts

All rows assume \(e\ge3\), an anchored tiling, and \(|P|=2^a5^e\) with the indicated \(a\); \(K=v_2(n)\).

| Branch | Exact verdict | Reason / remaining scope |
|---|---|---|
| \(K=1\), \(a=0,1\) | **0F/0M/0m: impossible** | Equal-gcd collision between the 3-dilate of head difference 8 and tail difference 13−1. This step does not use T2. |
| \(K=1\), \(a=2\) | **0F/0M/0m: impossible** | Already \(4\nmid n\) contradicts \(|P|\mid n\); the same collision also applies to any hypothetical tiling. |
| \(K=2\), \(a=0,1,2\) | **0F/0M/0m: impossible** | Same equal-gcd collision, without T2. |
| \(K=3\), \(a=0\) | **0F/0M/0m: impossible** | Independently \(\Phi_2\mid P\), contrary to odd \(|P|\). |
| \(K=3\), \(a=1\) | **0F/0M/0m: impossible, conditional** | \(Q\) owns \(\Phi_8\); transport in the 13-fibre produces a mod-8 collision against 1. |
| \(K=3\), \(a=2\), second \(P\)-owned factor \(\Phi_4\) | **0F/0M/0m: impossible, conditional** | Then \(Q\) owns \(\Phi_8\), giving the same 13-versus-1 collision. |
| \(K=3\), \(a=2\), second factor \(\Phi_8\) | **0F/0M/0m: impossible, conditional** | Then \(Q\) owns \(\Phi_4\); the 7-fibre gives a mod-8 collision against 1 or 13. |
| \(K\ge4\), \(a=0\) | **0F/0M/0m: impossible** | \(\Phi_2\mid P\), independently of T2. |
| \(K\ge4\), \(a=1\) | **0F/0M/0m: impossible, conditional** | \(Q\) owns both \(\Phi_8\) and \(\Phi_{16}\); the 13-fibre gives the required mod-16 collision with 1. |
| \(K\ge4\), \(a=2\), second \(P\)-factor \(\Phi_4\) or \(\Phi_{2^s}\), \(5\le s\le K\) | **0F/0M/0m: impossible, conditional** | In each such case \(Q\) owns both \(\Phi_8,\Phi_{16}\). The \(s\ge5\) part is empty when \(K=4\). |
| \(K\ge4\), \(a=2\), second \(P\)-factor \(\Phi_8\) | **0F/0M/0m: impossible, conditional** | \(Q\) owns \(\Phi_4,\Phi_{16}\); the 7-fibre gives a mod-16 collision against 1 or 13. |
| \(K\ge4\), \(a=2\), second \(P\)-factor \(\Phi_{16}\) | **0F/0M/0m for necessity; INCONCLUSIVE for existence or exclusion** | This is the literal surviving allocation, not a construction or a sufficiency theorem. |

### Findings and unverified categories

- **m1 — diagnostic cardinality.** The source's context-only \((e,K)=(3,4)\), \((|P|,|Q|)=(2000,165)\) examples have \(|P|=16\cdot5^3\), not \(4\cdot5^3=500\). Their stated cardinality is explicit, and they are not used in the proof; nevertheless they should not be presented as examples in the fixed \(a=2\) branch. Independent controls below construct examples of both cardinalities, but **all** miss the head anchors and the \(a=2\) examples also fail the anchored parity/odd-difference conditions. Neither supplies an anchored witness.
- **m2 — graph-level “arbitrary.”** The six unpinned \(f\)-values may be chosen independently from \(Y\) at the level of the displayed parity/mod-25 pairwise graph. This does **not** establish that every such choice is realized by a full cyclic tiling. Read “arbitrary” only in the former sense; the residual retains all tiling constraints.
- **INCONCLUSIVE — LL/T2.** The exact external Łaba–Londner Corollary 6.2 and its applicability are not source-verified here. They are assumed only in the named form: if at most two primes divide both factor cardinalities, each factor satisfies T2, including arbitrary odd cofactor \(R\). Ordinary cyclotomic irreducibility and the prime-power evaluation are also retained as named conditional algebraic imports.
- **INCONCLUSIVE — original-code border.** The cited Restivo–Salemi–Sportelli/Cordero actual-word caller and its hypotheses were not externally checked. The conditional implication is explained below; no converse, actual extension, or global completion follows.
- **INCONCLUSIVE — author provenance and broader status.** The author's checker, exact constructed objects and computational/provenance statements were not imported or inspected; independent constructions below verify existence of differently specified relaxations, not their identity. Unrestricted Shor completion, novelty, and external literature status are not decided.

## Mandatory snapshot and read sequence

The first research artifact was the supplied manifest, whose full SHA-256 was checked **before its body was read**:

`manifest-v1.json`: `1faa323b1e5314521c057185f99bb04181a77a8bb182dc851b436ea52b04a175` (match).

Next, before reading either declared source body, whole-file measurements were obtained for **both** inputs, in manifest order. Both matched every declared SHA, byte count and LF count, and both end in LF:

1. `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/math-5-shor-single-small-shared-prime-head-exclusion-conditional-parent-v1.md` — `c1c4c95dc4f399fbcb9cc3356b0d415778f8a496e9417c9e8828c3ecf27ea8aa`, **3637 bytes, 13 LF**, ending LF present. This was read only for the named import/context; its prior theorem or review receipt was not adopted.
2. `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-higher-five-power-low-two-adic-obstruction-v1.md` — `3446342ed71f10372e2229034588b3ad9908965937ec91e5a405e97b527f7026`, **12608 bytes, 117 LF**, ending LF present.

Actual raw displayed body windows, in order, with no window over 15 lines: contextual input **1–13**; target **1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–117**. Both endings, including the target's END line, were displayed. There was no declared erratum in this manifest. Complete source reading preceded every mathematical reconstruction and scientific control. No source body linked from either input, author code, held material, other review, search, web page or external model was used. No process deviation identified.

## Independent reconstruction

### 1. Dilation, gcd exclusion, actual anchors, and parameters

A direct tiling of \(\mathbb Z_n\) gives \(|P||Q|=n\). More generally let \(X\oplus Z=\mathbb Z_n\). For prime \(\ell\nmid|X|\), in \(\mathbb F_\ell[\mathbb Z_n]\), writing \(x,z\) for the characteristic sums and \(G\) for the group sum, \(xz=G\) and \(xG=|X|G\). Thus
\[
 x^\ell z=x^{\ell-1}G=|X|^{\ell-1}G=G.
\]
The corresponding integer coefficients are nonnegative, congruent to 1 modulo \(\ell\), and sum to \(n\); each is therefore exactly 1. This proves both injectivity of \(x\mapsto\ell x\) on \(X\) and \(\ell X\oplus Z=\mathbb Z_n\). Iterating prime factors gives \(tX\oplus Z\) whenever \(\gcd(t,|X|)=1\).

If nonzero differences \(d_X,d_Z\) have the same gcd \(g\) with \(n\), their quotients by \(g\) differ by a unit modulo \(n/g\). A CRT lift is a unit \(u\) modulo \(n\); since \(|X|\mid n\), \(u\) is coprime to \(|X|\), so the dilated tiling has the colliding differences \(ud_X=d_Z\). This proves equal-gcd exclusion. The CRT lift can be chosen nonzero modulo every prime dividing \(n\): where the prime already divides \(n/g\) the prescribed residue is a unit, and otherwise set it to 1.

The actual head differences include \(3,5=8-3,8,11\), and the actual tail difference 1 is present. Missing any of \(2,3,5,11\) from \(n\) makes one of those head differences have the same gcd 1 with \(n\) as the tail difference. Thus \(330\mid n\). If one of \(3,5,11\) did not divide \(|Q|\), dilation of \(Q\) by that prime would turn the actual tail difference 1 into the corresponding actual head difference, contradicting directness. In particular \(5\mid|Q|\).

Write
\[
 n=2^K5^vR,\qquad |Q|=2^{K-a}5^{v-e}R,
 \quad K\ge1,\quad v\ge e+1,\quad 33\mid R,\quad R\text{ odd},\ (R,5)=1.
\]
As \(\gcd(R,|P|)=1\), the tiling \(RP\oplus Q\) shows that each actual fibre \(Q_r=\{q\in Q:q\equiv r\pmod R\}\) has exactly \(2^{K-a}5^{v-e}>0\) elements. Each class modulo 33 has \(w=|Q|/33>0\) elements.

For the **odd tail rule**, take an odd \(d=q-q'\) divisible by 3, 5 or 11 but not by 25, and put \(g=\gcd(d,n)\). If \(5\mid d\), then \(v_5(g)=1\) and choose head difference 5 and multiplier \(t=g/5\). Otherwise choose a head difference \(p\in\{3,11\}\) dividing \(d\), and \(t=g/p\). In both cases \(t\) is odd and 5-free, hence coprime to \(|P|\); its dilated head difference has gcd \(g\), as does \(d\), a contradiction. Therefore every such odd difference is divisible by 25. The residue and parity statements here are well-defined modulo \(n\), since \(2\cdot25\cdot33\mid n\).

### 2. All-\(Q\) parity and \(f\)-graph

An even \(q\equiv1\pmod3\) would, by comparison with odd anchors 1 and 7, have to equal both 1 and 7 modulo 25. Hence no such element exists.

All classes below are nonempty. A class-3 element is even: an odd one compares with even 0 modulo 3 and even 14 modulo 11, forcing 0 and 14 modulo 25. Class 25 is odd by the previous paragraph, and comparison with 14 modulo 11 gives residue 14 modulo 25. Comparing classes 3 and 25 modulo 11 makes every class-3 element 14 modulo 25. Similarly class 11 is even, since an odd element would compare with 14 modulo 3 and 0 modulo 11; class 22 is odd and is 0 modulo 25 by comparison with 0 modulo 11. The class-22/class-11 comparison makes every class-11 element 0 modulo 25.

An odd element in a class 0 modulo 3 would compare with 0 and a class-3 element, forcing both 0 and 14 modulo 25. An odd element in a class 2 modulo 3 would compare with 14 and a class-11 element, forcing 14 and 0. Therefore, for **every** \(q\in Q\),
\[
 q\text{ is odd}\quad\Longleftrightarrow\quad q\equiv1\pmod3. \tag{G1}
\]
For any \(j\pmod{11}\), the three nonempty classes modulo 33 include an odd class and two even classes. The odd rule applied along common mod-11 edges shows that **all** elements in those three classes have one common mod-25 value \(f(j)\). The five actual anchors give
\[
 f(0)=0,\quad f(1)=1,\quad f(2)=13,\quad f(3)=14,\quad f(7)=7. \tag{G2}
\]
If \(f(j)\equiv f(k)\pmod5\), compare an odd element over \(j\) with an even element over \(k\): they are congruent modulo 25. The anchor values occupy all five mod-5 classes, so every \(f(j)\) lies in \(Y\). At the graph level the other six values can be chosen independently from \(Y\): the only odd/even equal-mod-3 edges have disappeared, equal-mod-11 edges have common \(f\), and equal-mod-5 values in \(Y\) are identical. This does not assert an actual tiling for any assignment.

There are \(11w\) odd and \(22w\) even \(Q\)-elements. Therefore \(Q(-1)=11w\ne0\), while the tiling mask equation evaluated at \(-1\) has right-hand side 0. Hence \(P(-1)=0\), so \(\Phi_2\mid P\) and \(a=0\) is impossible. No T2 was used in this paragraph.

### 3. Exact cyclotomic ownership and every actual fibre

Only 2 and 5 can be shared primes, so **assuming the named LL/T2 import**, both masks satisfy T2. For each \(1\le i\le K\), evaluation of the tiling mask equation at a primitive \(2^i\)-th root, plus the named cyclotomic irreducibility import, puts \(\Phi_{2^i}\) in at least one factor. Distinct such polynomials have value 2 at 1. Their product in \(P\) can have at most \(a\) factors, and their product in \(Q\) at most \(K-a\). There are \(K\) factors to cover, hence each is owned exactly once; \(P\) owns exactly \(a\) and \(Q\) exactly \(K-a\). The same evaluation-at-1 budget also rules out **additional** \(\Phi_{2^i}\) with \(i>K\); thus the theorem's “only” is not merely restricted to orders dividing \(n\).

For every prime-power \(\ell^j\mid R\), \(P(1)\) is not divisible by \(\ell\), so \(Q\) owns \(\Phi_{\ell^j}\). If \(Q\) owns \(\Phi_{2^i}\), T2 gives \(\Phi_{2^i d}\mid Q\) for each \(d\mid R\): choose at most one prime power for each distinct prime in \(d\). Since \(R\) is odd,
\[
 \Phi_{2^i}(X^R)=\prod_{d\mid R}\Phi_{2^i d}(X). \tag{C1}
\]
Indeed a root whose \(R\)-th power has exact order \(2^i\) has exact order \(2^id\) for a unique \(d\mid R\), and all roots are simple. The factors are pairwise distinct and, conditionally on irreducibility, their product divides \(Q(X)\).

Use representatives \(0\le r<R\) and write uniquely
\[
 Q(X)=\sum_{r=0}^{R-1}X^rF_r(X^R).
\]
Division by the monic \(\Phi_{2^i}(X^R)\) and uniqueness of the residue basis over \(\mathbb Z[X^R]\) imply \(\Phi_{2^i}\mid F_r\) for **each** \(r\). The actual-fibre mask is \(X^rF_r(X^R)\), which also vanishes at primitive \(2^i\)-th roots because \(R\) is odd. Equivalently, after folding actual fibre counts modulo \(2^i\), the counts at \(j\) and \(j+2^{i-1}\) agree for every \(j<2^{i-1}\). To see this without an omitted coefficient step, reduce the folded polynomial modulo \(1+X^{2^{i-1}}\); the remaining coefficients are exactly those differences, in degree less than the monic divisor's degree.

Every actual \(Q_r\) has fixed parity by (G1), since \(3\mid R\). The 13-fibre has mod-25 value 13, and the 7-fibre value 7, because \(11\mid R\) and (G2) holds for all tails. These are the particular fibres used next, not averages over fibres.

### 4. High-bit collision and each allocation

If \(5\nmid(q-q')\) and the 2-part of \(g=\gcd(q-q',n)\) is exactly 8, then \(t=g/8\) is odd and 5-free. In the tiling \(tP\oplus Q\), the actual head difference \(t\cdot8=g\) has the same gcd with \(n\) as \(q-q'\), impossible. For \(K=3\) this applies when \(q-q'\equiv0\pmod8\); for \(K\ge4\), when \(q-q'\equiv8\pmod{16}\), in each case requiring the difference to be 5-free.

For \(K\le2\), independently of ownership,
\[
 \gcd(3\cdot8,n)=\gcd(13-1,n)=3\cdot2^K.
\]
The multiplier 3 is coprime to \(2^a5^e\), so gcd exclusion in \(3P\oplus Q\) proves those cases impossible. The equality uses \(3\mid n\), exactly one 3 in each of 24 and 12, and no other odd prime in either.

For \(K=3\), if \(Q\) owns \(\Phi_8\), the 13-fibre has an element 5 modulo 8 and therefore, by the equal halves property, an element 1 modulo 8. It is 13 modulo 25, so comparison with anchor 1 is 5-free and divisible by 8. Thus \(Q\) cannot own \(\Phi_8\). If \(a=1\) it must own it. If \(a=2\), \(P\) must own \(\Phi_2,\Phi_8\), leaving \(\Phi_4\) for \(Q\). In the 7-fibre, \(7\equiv3\pmod4\) forces an element 1 modulo 4, hence 1 or 5 modulo 8. Compare it with anchor 1 in the first case or 13 in the second; 7−1 and 7−13 are both nonzero modulo 5. Both \(a=1,2\) are excluded.

For \(K\ge4\), \(Q\) cannot own both \(\Phi_8,\Phi_{16}\): the 13-fibre has 13 modulo 16, \(\Phi_8\) supplies a point 1 modulo 8, and \(\Phi_{16}\) ensures a point 9 modulo 16. Compare it with anchor 1: the difference is 8 modulo 16 and 13−1 is 5-free. Thus \(a=1\) is excluded. For \(a=2\), the second \(P\)-factor is \(\Phi_{2^s}\) with \(2\le s\le K\), and the preceding contradiction leaves \(s=3\) or 4. If \(s=3\), \(Q\) owns \(\Phi_4,\Phi_{16}\). In the 7-fibre, \(\Phi_4\) gives a point 1 modulo 4. If it is 1 modulo 8, \(\Phi_{16}\) supplies 9 modulo 16, colliding with anchor 1; if it is 5 modulo 8, \(\Phi_{16}\) supplies 5 modulo 16, colliding with anchor 13. The fibre's mod-25 value 7 differs modulo 5 from both anchors. Hence \(s=3\) is excluded and \(s=4\) is necessary. This exhausts the stated branches, including every \(s\ge5\).

### 5. Literal residual and conditional caller

For the claimed \(|P|=4\cdot5^e\) residual, the unknowns remain **the original anchored direct tilings** \(P\oplus Q=\mathbb Z_n\), not arbitrary solutions of the following necessary conditions. In any such tiling, conditionally:

- \(K\ge4\), \(n=2^K5^vR\), \(v\ge e+1\), \(R\) odd, \((R,5)=1\), and \(33\mid R\); \(|Q|=2^{K-2}5^{v-e}R\).
- The only 2-power cyclotomic factors of \(P\) are exactly \(\Phi_2,\Phi_{16}\); \(Q\) owns exactly those with \(2\le i\le K\), \(i\ne4\), and no additional 2-power factors. Every \(Q_r\) has \(2^{K-2}5^{v-e}\) elements and obeys every resulting half-count equality.
- The all-\(Q\) graph (G1)–(G2), \(f(j)\in Y\), the odd-difference rule, and the 5-free mod-16 high-bit collision rule all remain necessary. Actual head and tail anchors and **every** original tiling equation remain in force.
- The same valuation argument also gives exactly \(e\) owned 5-power factors for \(P\) and \(v-e\) for \(Q\), chosen among the first \(v\), with the attendant T2 mixed-prime factors. It does not determine which 5-power levels are owned or prove that these necessary conditions are jointly sufficient. A genuine further high-modulus/head-anchor argument is missing.

The literal displayed code contains words with head exponents \(0,3,8,11\) and the five actual tail exponents \(0,1,7,13,14\). **Assuming** the named actual-word border theorem really supplies the asserted same-code anchored factors for any finite UD factor-complete extension with pure-a atom \(a^n\), the above excludes its anchored factor \(P\) having either of the two claimed cardinalities. The boundary \(n>14\) is harmless for this conditional caller: if \(n=1\), the extension contains \(a,b,ba\) and is not UD; if \(n>1\), the anchored gcd argument already forces \(330\mid n\). The caller's truth, the existence of an extension, the remaining head cardinalities, and any converse are not established.

## Reviewer-owned bounded exact controls

Only `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f237-shor-higher-five-low-two-adic/reviewer-f237-controls.py` was executed; it is independently written, imports no author code, and is not an author test suite. Its whole SHA-256 at execution was `21025de35f239be6da863a0efca54f9b054b3cc826e6ac8bda36a2d4901edaf0`. A subprocess timeout of 120 seconds was imposed. Actual `/bin/date` observations: start **2026-10-29T14:13:42-0700 PDT**, end **2026-10-29T14:13:43-0700 PDT**. Actual exit **0**; stderr empty; no cap was hit. These are finite controls, not proofs of the quantified theorem.

1. **Graph:** initial parity/mod-25 domains from the five actual anchors were reduced by exact pairwise arc consistency over all 33 nonempty mod-33 classes. All 33 final domains matched (G1)–(G2), including the five pinned and six graph-level free values, after three passes. Intended-reason negatives: even class 3 with value 0 survives the anchor-only filter but conflicts with forced odd class 25/value 14; removing all anchor constraints admits a forbidden parity in class 1 and a forbidden parity in class 0.
2. **Dilation/gcd:** for anchored-at-zero finite direct tilings with \(2\le n\le11\), 126 tilings gave 1,304 admissible dilation checks and 732 gcd-difference comparisons. Negative: for \(n=4\), \(X=\{0,1\},Z=\{0,2\}\), the non-coprime multiplier \(t=2\) creates collisions.
3. **Low gcd/high-bit arithmetic:** 42 choices of \(K\in[1,7]\), \(v\in\{4,6\}\), and three odd cofactors; 6,180 5-free signed differences checked the stated \(K=3\) and \(K\ge4\) high-bit equivalences. Negative: at \(K=3\), the low-\(K\) equal gcds are 24 and 12, not equal.
4. **Folded-count branch logic:** all \(3^8=6561\) vectors of odd-residue counts in \(\{0,1,2\}\) modulo 16; respectively 342 and 1,017 qualifying \(K=3\) \(\Phi_8/\Phi_4\) cases, and 6 and 13 qualifying \(K\ge4\) \(\Phi_8+\Phi_{16}/\Phi_4+\Phi_{16}\) cases. Deleting the \(\Phi_{16}\) premise gives explicit count vectors for which each high-bit conclusion fails. The anchor differences were separately checked nonzero modulo 5.
5. **Transport:** 24 exact integer polynomial identities (C1) for four exponents and six odd \(R\), plus three binary actual-fibre fold examples. Negatives: even \(R=6\) breaks the displayed odd-\(R\) factor identity; deleting one required partner breaks a fibre half-count.
6. **Independent relaxations, not witnesses:** for each \(j=3,4\), exact 330,000-residue coverage and unique representations were checked for one \((2000,165)\) and one \((500,660)\) pair. Each has \(Y\subseteq Q\), \(P\subseteq33\mathbb Z_n\), and \(Q\) owns \(\Phi_{5^j}\) but not the other of \(\Phi_{125},\Phi_{625}\). The \((500,660)\) pairs also have exactly \(\Phi_2,\Phi_{16}\) in \(P\) and \(\Phi_4,\Phi_8\) in \(Q\) at the four relevant 2-powers. Their intended-reason negative is decisive: \(3,8,11\notin P\); moreover \(0,3\in Q\) violate the anchored odd-tail rule. Thus they cannot be substituted for a full residual solution.

For reproducibility of the latter stronger-cardinality examples: put \(d=5^{j-1}\), \(A_5=\{0\le x<625:\lfloor x/d\rfloor\equiv0\pmod5\}\), \(B_5=\{0,d,2d,3d,4d\}\), \(A_{16}=\{0,1,8,9\}\), \(B_{16}=\{0,2,4,6\}\), and \(c(u,v)=v+625((u-v)\bmod16)\). Take \(P=\{33c(u,v):u\in A_{16},v\in A_5\}\) and \(Q=\{r+33c(u,v):0\le r<33,u\in B_{16},v\in B_5\}\). Binary digits show \(A_{16}\oplus B_{16}=\mathbb Z_{16}\), the indicated base-5 digit shows \(A_5\oplus B_5=\mathbb Z_{625}\), and CRT plus the 33 residue classes gives the exact cover. This construction deliberately omits the head anchors and does not satisfy the full anchored residual.

The full SHA-256 of this finalized review is measured after writing and supplied in the reviewer handoff; it is not self-embedded in the bytes being hashed.
