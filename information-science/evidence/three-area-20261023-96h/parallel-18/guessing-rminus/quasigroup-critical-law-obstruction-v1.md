# R-minus: a nonassociative all-law obstruction and an unrestricted critical-law criterion

Owner: `InfoGuessingRminus`, slot info-5. Last actual source/derivation clock before this freeze: `2026-10-24T05:55:23-0700` (`/bin/date`). This is a complete **written CANDIDATE**, not an accepted theorem, an executed certificate, a new guessing-number bound, or a novelty verdict. Scientific HOLD and the original October27 deadline are unchanged.

## 1. Literal target, dependency pins, and delta from the actual baseline

The target remains the exact ten-vertex BCDRV R-minus, obtained by deleting only edge9–10 from R. Its edges are

`12 13 14 15 16 17 23 27 29 2-10 34 38 39 45 48 4-10 56 59 5-10 67 68 69 78 7-10 89 8-10`.

A finite support `C` satisfies the graph functional dependencies, abbreviated FD, when, for every vertex v and x,y in C, equality on N(v) forces x_v=y_v. A finite law is FD-consistent when its positive-probability support is such a C. Alphabets are arbitrary finite nonempty sets; the full guessing-number target uses every common integer alphabet s>=2, arbitrary deterministic local functions and the asymptotic supremum. No linear, group, prime-power or quasiuniform assumption is imposed on that target.

Write, with logarithms in base2,

`Phi(X) = 2 sum_(v=1)^10 H(X_v) - 3 H(X_1,...,X_10)`.

The old triangle-padding/types equivalence between universal Phi>=0 and gn(R-minus)=20/3 remains an **existing baseline**, not a result of this packet. The unrestricted matched interval remains

`20/3 <= gn(R-minus) <= 1847/276`.

Load-bearing local pins:

- `inputs-v1.json`, SHA256 `bdc4cd14d20e2401971a7354c2a6239106fbe2be158b50921d5c486c6a086be6`: literal graph and source identification.
- `I2-complete-written-verification-v1.md`, SHA256 `152f6fed3f7654c9207383892effdd8abe1cc796bca5544cfc7c2271cc077585`,1402 LF: the eight exact identities Phi=J_D+3S_D on the graph FDs, where each S_D is a nonnegative Shannon combination. Only D1 is needed below.
- Actual I2 peer return in the ordered-olson root, `peer-review-I2-complete-written-verification-v1.md`, SHA256 `9697e619e7c6129c47da178c3b9ce608fe2b43358a0cc6862d71e267a961a412`,233 LF; actual parent `wave-v16-written-frontiers-parent-v1.md`, SHA256 `0189f2186aa54e486736db167235eb78ca3ee184e6d1628f8ecb25a0ce57aa8c`: ordinary WRITTEN scope only. The parent expressly did not recompute all1005 raw Shannon rows. Executable/triple finite-certificate certification remains UNMET.
- Prior six-lane `review/codex-phi-out.md`, SHA256 `c31396a955d48e29a637c10ab09aab4cfe6293a0b60f748d18ba1b2ddd691560`, read in full: old C1 already treats subgroups of products of **arbitrary finite groups**, their cosets, and every reweighting. It is NOT merely an abelian baseline. Its doubling identity and max-entropy-minimizer idea are credited below, not rediscovered.

The proposed delta is an associativity-free extension to supports closed under coordinatewise **Latin multiplication**, together with an unrestricted, fixed-alphabet **one-product obstruction at an actual variational minimizer**. It is not another support threshold or group-order count. No claim is made that its entropy-vector class is strictly separated from every possible group representation; public novelty and significance require a separate audit.

For D1 put `(U,V;P,Q)=(X_2,X_4;X_1,X_3)` and `Z=(X_5,...,X_10)`. The already reconstructed I2 identity is

`Phi = J_D1 + 3 S_D1`,

where

`J_D1 = I(U;V|PZ)+I(U;V|QZ)+I(P;Q|Z)-I(U;V|Z)`

and S_D1>=0 on every finite law. The displayed identity uses the exact graph FDs. The packet uses no I1 deletion certificate, no order120 classification, no support300 theorem and no assumption that an arbitrary input law is quasiuniform.

## 2. Precise algebraic definitions

A **finite quasigroup** `(A,*)` is a finite nonempty set with a binary operation for which every left translation `y -> a*y` and every right translation `x -> x*b` is a bijection. No associativity, identity, commutativity or medial law is assumed. Let `a\b` be the unique y with a*y=b, and `b/a` the unique x with x*a=b.

Choose an independently specified quasigroup `*_v` on each alphabet A_v. Product, left division and right division of ten-tuples are coordinatewise. A nonempty support J is **closed** if x*y belongs to J for all x,y in J.

A finite nonempty closed J is itself a quasigroup under the inherited multiplication: each fixed-word translation is injective on J, maps J into J, and hence is onto J. Its division operations are consequently the ambient coordinatewise divisions. This elementary finite-set argument is the only closure fact being used.

A **loop** is a quasigroup with a two-sided identity. A subset L of a product of loops is a subloop here when it contains the identity word and is closed under multiplication and both divisions. Finite multiplication closure plus the identity already implies division closure by the preceding translation argument.

## 3. Uniform subloop laws have every conditional Ingleton

### Lemma3.1: every projection of a uniform finite subloop is uniform

Let L be a finite subloop of a product of finite loops, and h_A its projection onto any coordinate set A. The image h_A(L) is a finite loop. For any a,b in that image, choose c=a\b and a word z in L with h_A(z)=c. Right translation `x -> x o z` is a bijection of L and carries the h_A-fiber over a bijectively onto the fiber over b. Its inverse is right division by z, also in L. Thus all nonempty fibers have equal cardinality.

Consequently, if X is uniform on L, X_A is uniform on its support for every A. In particular the law of `(X_U,X_V,X_Z)` is uniform on its joint support, and for every supported value z the conditional pair `(X_U,X_V)|X_Z=z` is uniform on its joint support. This conclusion is derived, not assumed of the original arbitrary input law later in the packet.

### Lemma3.2: the conditional pair support is a union of complete bipartite components

For a loop operation o with right division /, the ternary term

`p(x,y,z) = (x/y) o z`

satisfies `p(x,y,y)=x` and `p(y,y,z)=z`. Indeed `(x/y)o y=x`, while y/y is the identity. These are the Mal'tsev identities; they require no associativity.

Fix a supported value z of an arbitrary conditioning coordinate tuple Z. The fiber L_z need NOT be closed under the binary loop product. The proof does NOT assert that it is. It is closed under the coordinatewise ternary term p, since three equal Z-coordinates z give p(z,z,z)=z, and L is closed under the term's multiplication and division.

Suppose the conditional support of `(X_U,X_V)` contains the three pairs `(a,b),(a',b),(a',b')`. Lift them to words r,s,t in L_z. The word p(r,s,t) remains in L_z. Its U-coordinate is p(a,a',a')=a; its V-coordinate is p(b,b,b')=b'. Therefore `(a,b')` is also in the support.

This three-corner completion implies that each connected component of the bipartite support graph is complete bipartite: any odd path between a left and a right vertex can be shortened by two edges using three-corner completion until it becomes a single edge.

By Lemma3.1 the conditional pair is uniform on all its supported edges. Conditioned on the component label W_z, its support is a complete Cartesian product and its law is uniform on that product. Therefore the two endpoints are conditionally independent given W_z. The label W_z is a function of either endpoint. Hence, in the fixed z-law,

`H(W_z|U)=H(W_z|V)=0` and `I(U;V)=H(W_z)`.

Different components need not be assigned any arbitrary equal-weight convention; the conclusion follows from the actual uniform-edge law. No classification of small supports is used.

### Lemma3.3: extractable mutual information gives Ingleton in every slice

For any joint extension `(U,V,P,Q)` in a fixed z-law, if W is determined by both U and V and I(U;V)=H(W), then

`I(U;V|P) >= H(W|P)` and `I(U;V|Q) >= H(W|Q)`.

Also, by direct entropy expansion,

`H(W|P)+H(W|Q)+I(P;Q)-H(W)`

`= I(P;Q|W)+H(W|P,Q) >= 0`.

These identities prove J>=0 for the fixed z-law. Average over the actual conditional probabilities of z. Lemmas3.1–3.2 give the required W_z separately in every fiber, so

`J_D(X) >= 0`

for every pair of coordinate variables, every choice of two further coordinate variables, and every conditioning coordinate tuple for a uniform finite subloop law.

In particular, if L satisfies the exact R-minus FDs, the pinned D1 identity yields

`Phi(uniform L) = J_D1 + 3 S_D1 >= 0`.                         (L)

Only the ordinary-written I2 dependency is imported. No FD is inferred for a projection after discarding needed conditioning coordinates.

## 4. Associativity-free doubling and the unrestricted critical-law theorem

### Lemma4.1: the exact old doubling identity needs only Latin translations

Let Y,Y' be iid with an arbitrary law p on the fixed product of alphabets, and put T=Y*Y'. Conditional entropy functionals below mean the average of Phi in the fully conditioned ten-variable laws. Coordinatewise bijectivity gives

`H(T,Y')=H(Y,Y')=2H(Y)`

and, for each vertex v,

`H(T_v,Y'_v)=H(Y_v,Y'_v)=2H(Y_v)`.

Use

`H(Y'_v|T)=H(Y'_v|T_v)-I(Y'_v;T_(-v)|T_v)`

and the chain rule for the full tuple. Multiplying the singleton equations by2 and the full-tuple equation by-3 gives exactly

`2 Phi(Y) = Phi(T) + E_t Phi(Y'|T=t)`

`             + 2 sum_v I(Y'_v;T_(-v)|T_v)`.                   (D)

This is the prior C1 identity, now with its actual needed hypothesis identified as coordinatewise Latin bijectivity. It is not advertised as a new entropy identity. Also,

`H(T|Y')=H(Y)` and `H(T|Y)=H(Y')=H(Y)`.                        (E)

These facts hold whether or not T satisfies any graph FD.

### Theorem4.2: negative critical laws lose an FD after every Latin self-product

Fix finite nonempty alphabets A_1,...,A_10. Let F be the set of ALL FD-consistent laws on their fixed product, with arbitrary local functions allowed. It is compact: it is a closed subset of a finite probability simplex, equivalently a finite union of the simplex faces associated with FD-consistent supports. The entropy convention 0log0=0 makes Phi and joint entropy continuous.

Let m=min_F Phi. Among all laws attaining m choose p with maximum joint entropy. Suppose m<0. Then for EVERY choice of quasigroup operations on these SAME alphabets,

`law(Y*Y') is NOT FD-consistent`, for Y,Y' iid with law p.       (C)

In particular at least one vertex v has `H(T_v|T_N(v))>0`. This is a conclusion about an actual fixed-alphabet variational extremizer, not every law with negative Phi and not a claim that a particular minimizer has been found.

**Proof.** Suppose, to the contrary, that T is FD-consistent for one such choice of operations. Its law lies in F. For each supported t, the conditional law of Y'|T=t is supported on a subset of supp(p). Every such subset still satisfies the graph FDs, so this conditional law also belongs to F. Thus both Phi(T) and every conditional Phi on the right of (D) are at least m. The mutual-information correction is nonnegative. Since the left side is2m, equality forces Phi(T)=m, E Phi(Y'|T)=m and all the correction terms to be zero.

Maximum joint entropy among the Phi-minimizers now gives H(T)<=H(Y), while (E) gives the reverse inequality. Hence H(T)=H(Y), and (E) implies BOTH

`T independent of Y` and `T independent of Y'`.                (I)

The second independence alone was enough in the old group proof after a group translation. Here both are used to avoid any hidden group assumption.

Put C=supp(p), K=supp(T). For x,y in C set t=x*y. By coordinatewise Latin uniqueness,

`P(T=t|Y'=y)=p(x)` and `P(T=t|Y=x)=p(y)`.

Independence (I) therefore gives q(t)=p(x)=p(y), where q is the law of T. Since x,y were arbitrary, p is uniform on C. Fix r,s in C. Independence further gives

`K=C*C=C*s=r*C`,

and q is uniform on K, with |K|=|C|. This does NOT assert C*C=C or that either C or K is a subgroup.

Use the original left/right divisions to define the coordinatewise principal isotope

`z o w = (z/s) * (r\w)`, with identity word `e=r*s`.            (P)

This is a loop on the ambient product: `e o w = r*(r\w)=w`, and `z o e=(z/s)*s=z`. For z,w in K, the equalities K=C*s=r*C imply z/s belongs to C and r\w belongs to C. Thus z o w belongs to C*C=K. The word e is in K, and finite Latin translations then give division closure. Consequently K is a finite subloop under (P).

By the contradiction assumption, K is an FD-consistent support. The uniform-subloop result (L) gives Phi(T)>=0. But Phi(T)=m<0. This contradiction proves (C).

All alphabets were held fixed during the minimizing argument. Replacing each alphabet by an alphabet of pairs, using concatenation of independent codes, or an infinite limiting construction is NOT a witness for the preservation premise of this theorem.

## 5. Complete all-law inequality on Latin-closed FD supports

### Theorem5.1

Let A_v be arbitrary finite quasigroups, and let nonempty J be closed under their coordinatewise multiplication. Suppose the exact R-minus FDs hold on J. Then for EVERY probability distribution p supported on J, including arbitrary nonuniform reweightings and arbitrary restrictions of support,

`2 sum_v H_p(X_v) >= 3 H_p(X_1,...,X_10)`.                    (Q)

**Proof.** Minimize Phi over the compact simplex of all laws supported on J, and choose a maximum-joint-entropy minimizer p. The law of T=Y*Y' is supported on J by closure. Every conditional Y'|T=t is also supported on J. Thus every comparison with m in the proof of Theorem4.2 remains valid when minimization is restricted to this simplex; no minimizer over all FD codes is needed.

Equations (D)–(I) and the principal-isotope construction give a uniform minimizing law q on a finite subloop K contained in J. It inherits the graph FDs. Therefore (L) gives m=Phi(q)>=0, and all laws on J have Phi>=0. Point masses give0, so the minimum is exactly0. This proves (Q).

This is an all-law inequality with an explicit algebraic-support hypothesis, not a quasiuniform-input theorem and not a universal inequality on every FD law. Associativity, a group identity on the original alphabets, and normal coordinate subgroups are absent from its hypotheses.

### Corollary5.2: unrestricted algebraic-span obstruction

Let p be ANY finite FD-consistent law with Phi(p)<0. Choose ANY injective coordinate embedding into finite quasigroup alphabets and let J be the smallest set containing the embedded positive-probability support and closed under coordinatewise multiplication. Such J exists in the finite ambient product; it is a finite subquasigroup by the translation argument of Section2.

Then J MUST violate at least one R-minus FD. Otherwise Theorem5.1 would apply to the embedded law, whose entropies and Phi are unchanged. Equivalently there are a vertex v and two actual words x,y in J agreeing on N(v) but differing at v.

This quantifies over arbitrary input weights and arbitrary finite coordinate quasigroup structures, not only group structures or quasiuniform laws. It does not claim to supply or enumerate the conflicting words for an unknown input.

For a uniform winning code C contained in an FD-consistent closed J, (Q) also gives

`3 log|C| <= 2 sum_v H(X_v) <= 2 sum_v log|pi_v C|`.

Thus `|C|^3 <= product_v |pi_v C|^2`; for a common alphabet s this implies `|C|<=s^(20/3)`. These are exclusions of the specified algebraic-container family, NOT a new unrestricted upper bound.

## 6. Exact failure of the tempting unrestricted preservation lemma

The statement “every FD-consistent law, even with every coordinate nonconstant, has an FD-preserving coordinatewise Latin self-product” is FALSE already on binary R-minus alphabets. This prevents dropping the genuine extremizer hypothesis from the next open obligation.

Let A,B be independent uniform bits, and define

`X_1=A, X_2=A OR B, X_3=B, X_4=A AND B`,

`X_5=X_6=X_7=X_8=X_9=X_10=A`.

The four codewords, in the literal vertex order1,...,10, are

| A B | word |
| --- | --- |
| 0 0 | `0000000000` |
| 0 1 | `0110000000` |
| 1 0 | `1100111111` |
| 1 1 | `1111111111` |

All coordinates are nonconstant. Here are complete local decoders, each using actual neighbors only:

- f1=x5;
- f2=x1 OR x3;
- f3=x2 when x1=0, and x4 when x1=1;
- f4=x1 AND x3;
- f5=f6=f7=x1;
- f8=x6;
- f9=f10=x5.

The ten local equations have exactly the four displayed simultaneous solutions: A and B are free, OR/AND determine2,4, and the remaining coordinates copy A. Thus this is a literal winning code, not an invented graph or a marginal FD surrogate.

For XOR self-product, two supported output words are

`0110000000 XOR 1100111111 = 1010111111`,

`1111111111 XOR 0000000000 = 1111111111`.

They agree on `N(2)={1,3,7,9,10}` (all those coordinates equal1), but their coordinate2 values differ. They also agree on N(4)={1,3,5,8,10} while differing at4. Both output events have positive probability for the iid input, so the self-product violates an actual graph FD.

Every binary quasigroup has the form `a*b=a XOR b XOR c`: choosing the table entry at(0,0) forces the other three entries by the two Latin conditions. Therefore ten independently chosen binary quasigroups only add a fixed coordinate word c to the XOR output. Such coordinatewise bijective relabeling preserves the exhibited FD conflict. The same four-word law therefore loses an FD under **EVERY** coordinatewise binary quasigroup self-product, without running an enumeration.

This is a control against an overbroad lemma, not a lower-bound improvement. With h2(1/4)=2-(3/4)log2(3),

`H(X_V)=2`,

`sum_v H(X_v)=8+2 h2(1/4)=12-(3/2)log2(3)`,

`Phi=18-3 log2(3)=3 log2(64/3)>0`.

Hence it is NOT a negative critical law and does not refute Theorem4.2. Universal one-product failure alone is not sufficient for negative Phi. Nonconstant coordinates alone are not sufficient for the missing preservation step either.

The AND/OR mechanism is an existing prior-dossier baseline, not a newly discovered Ingleton violation. Its explicit full-graph copying and the symbolic all-binary-Latin FD conflict are used only as the exact control stated here. The four-row reconstruction and entropy calculation are written, not independently executed or formally certified.

## 7. Current-source and corpus gate, with actual limitations

The strongest matched general source remains Gürpınar, [Kybernetika60(5),553–575(2024), Theorem5.2](https://www.kybernetika.cz/content/2024/5/553/paper.pdf), DOI10.14736/kyb-2024-5-0553; [arXiv:2310.09232v2](https://arxiv.org/html/2310.09232v2). The initial selection freeze actually read its definitions and graph section and recorded its explicit unknown-value statement. The current abstract/author-matched search was refreshed, with no later matched resolution found. Search misses are NOT a freshness or openness theorem; the earlier `selection-v1.md` source-status limitations remain.

Directly relevant antecedents actually read:

1. The old local C1 proof, full83LF, pinned above. It already covers arbitrary finite groups and all subgroup/coset reweightings. Its entropy identity and extremizer selection are expressly credited. This packet adds neither a nonabelian-group claim nor a group-order improvement.
2. Fong–Shadbakht–Hassibi, [On the Entropy Region and the Ingleton Inequality, MTNS2008](https://scholar.lib.vt.edu/MTNS/Papers/164.pdf), complete reader body including bibliography: quasiuniform conventions and the classical normal-subgroup Ingleton baseline. These are prior results.
3. Matveev–Romashchenko, [Spectral Conditions for the Ingleton Inequality, arXiv:2602.16536v2](https://arxiv.org/html/2602.16536v2), explicitly v2 dated18May2026, sections1.1–1.3 including TheoremA read. Extractable common information implying Ingleton is explicitly classical there. Its new spectral theorem assumes a uniform-edge biregular support graph and contains a parameter-dependent O(log H) term. Nothing in the R-minus FDs automatically supplies its hypotheses or an explicit new numeric graph bound; this packet imports no such spectral claim.
4. J.D.H. Smith, [Loops and quasigroups: Aspects of current work and prospects for the future,2000](https://dml.cz/dmlcz/119175), survey body and references read: isotopies, loops and quasigroup coding are old. Its algebraic use of the word “entropic” is not automatically Shannon entropy. The named1990 paper [Entropy, character theory and centrality of finite quasigroups](https://doi.org/10.1017/s0305004100069334) was identified via the primary bibliographic reference and publisher-deposited Crossref title/abstract. That abstract concerns entropy/asymptotic entropy of a quasigroup and maximality criteria. Its full text has not been used as a proof import or excluded as a novelty antecedent by an abstract-only inspection.

Targeted public searches for quasigroup/loop/Mal'tsev plus Ingleton or entropy/convolution/minimization found no matched published version of the complete R-minus statements above in the read scope. That is **UNCERTIFIED NOVELTY**, not a discovery certificate. No claim that the elementary loop/Mal'tsev/common-information lemmas themselves are new is intended.

Local `/Users/jinleic/jinleic-workspace/math` was refreshed with exact word-bounded Ingleton/quasigroup/Mal'tsev/R-minus/guessing-number terms: no matches. The initial unbounded substring query falsely matched “singleton” and “remainder-minus” and was discarded, not counted as relevant evidence.

Public `openai/math` was refreshed at actual tree `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. The complete nonrecursive root metadata has truncated=false, identifies `CONTENTS.md` blob `2c68c086fff36a5806c936ad1659cf1a8d0b6dd9` (638727 bytes) and README blob `50feb63d396138f30dc1ff1e0af121d0263bf5a3`. Its pinned README was read; the pinned CONTENTS was searched with the same bounded terms, with no matches. The recursive-tree response was visibly cut mid-object in this interface, so no completeness claim is made for that attempted path scan. This is a current catalogue/topic screen, not a read of every remote proof or an acceptance of all model claims.

## 8. Exact outcome, missing ingredient, and reconstruction scope

Complete written outcomes at the candidate level are:

- the all-law inequality (Q) on Latin-closed FD supports;
- the arbitrary-weight, arbitrary-finite-quasigroup closure-defect consequence;
- the unrestricted fixed-alphabet negative-critical-law one-product obstruction (C);
- the full-graph all-nonconstant binary control showing that a generic FD-preservation theorem is false.

The original unrestricted gap is NOT closed. No new numeric upper/lower bound is claimed. To turn the critical-law route into a proof of Phi>=0 on every finite FD law, one would have to derive a same-alphabet FD-preserving Latin product from the **actual Phi-minimal/max-entropy structure**, or supply another quantitative argument that excludes the universally defective critical laws. Neither assertion is proved here. The control shows why the bare FDs and nonconstant marginals are insufficient substitutes. Tensoring or enlarging alphabets does not repair the fixed-alphabet variational premise.

A bounded peer reconstruction should attack: (a) every sign and conditioning convention in(D); (b) compactness and the use of the actual global fixed-alphabet minimum in Theorem4.2; (c) why conditional Y'|T laws retain the original FDs even if an arbitrary T does not; (d) why entropy maximality forces BOTH independences; (e) the uniformity and K=C*s=r*C conclusions without a group identity; (f) the principal loop isotope and its closure; (g) equal-size projection fibers, and especially the distinction between binary closure and ternary closure of a Z-fiber; (h) slice-wise extractable common information and exact D1-I2 composition; (i) the separate restricted-simplex argument of Theorem5.1; and (j) every literal decoder/output word in the binary control.

No LP, code search, group enumeration, scientific arithmetic interpreter, native solver, compilation, test, independent-model CLI or old held runtime was executed for this packet. Its sources and proof are frozen for a new exact-scope reconstruction; existing I2/T300 review does not transfer automatically to it. Correctness, import trust, unrestricted scope, novelty and significance remain separate gates.
