# Recursion audit and fixed-hole obstructions for LKTS(57), LKTS(87)

Research date: 2026-10-14. No design search, code verification, or computation was run. The new counting arguments below are supplied with proofs, not claimed as published results. No LKTS(57) or LKTS(87) is constructed here.

## 1. Source access and epistemic boundary

Primary mathematical text actually opened:

- **Wang 2026**, [arXiv:2607.21521](https://arxiv.org/abs/2607.21521), local `wang-2607.21521.txt`, especially Section 4, lines 486–506. This explicitly reports 57 and 87 as the two possible exceptions below 200 and proposes the forms 4v−3 and 4v+3. That is a dated author's status statement, not a proof of nonexistence and not an independently reproduced classification here.
- **Wang–Shi**, [arXiv:1307.3019, Theorem 2.1](https://arxiv.org/html/1307.3019#S2.Thmtheorem1), published in Discrete Mathematics 340 (2017), 1042–1045. Full theorem and construction opened.
- **Liu–Lei**, [2023 publisher page](https://link.springer.com/article/10.1007/s10623-023-01221-9), and [author preprint 2210.06214v2](https://arxiv.org/pdf/2210.06214), Theorem 1.1, Section 3, and Theorem 4.4. The preprint is dated 12 February 2023; journal pages 2677–2686.
- **Tan–Zhou**, [2503.11934v1](https://arxiv.org/pdf/2503.11934), especially Section 2, Theorems 1.1 and 3.2, Corollary 3.3. The preprint is dated 15 March 2025; Wang cites its 2025 journal publication.
- **Ge**, [More large sets of KTS(v), JCMCC 49 (2004), 211–214](https://combinatorialpress.com/article/jcmcc/Volume%20049/vol-049-paper%2015.pdf). Scanned PDF visually opened; page 212, Lemma 2.2, explicitly restates Denniston's TKTS(v)+LKTS(v) ⇒ LKTS(3v).
- **Zhao**, [EJC 16 (2009), R114](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i1r114/pdf/), Section 2: precise definitions of TRISQ and LR(u). This paper concerns directed systems; its directed product theorems must NOT be silently used as LKTS theorems.
- **Zhou–Chang**, [Australasian J. Combin. 33 (2005), 47–56](https://ajc.maths.uq.edu.au/pdf/33/ajc_v33_p047.pdf), scanned page 49: LR definition visually opened.
- **Xu–Ji 2024**, [Special overlarge sets of Kirkman triple systems](https://link.springer.com/article/10.1007/s10623-024-01386-x), publisher abstract opened. Its OLKTS⁺(v) replaces RDSQS(v+1) in the implication to LKTS(3v), not to LKTS(v).

Original records opened, but original mathematical body unavailable in this run:

- Lei 2002, [DOI 10.1016/S0012-365X(01)00470-8](https://doi.org/10.1016/S0012-365X(01)00470-8).
- Zhang–Zhu 2002, [DOI 10.1016/S0012-365X(01)00178-9](https://doi.org/10.1016/S0012-365X(01)00178-9).
- Zhang–Zhu 2003, [DOI 10.1016/S0012-365X(02)00766-5](https://doi.org/10.1016/S0012-365X(02)00766-5).
- Xu–Ji 2021, [DOI 10.1016/j.disc.2021.112373](https://doi.org/10.1016/j.disc.2021.112373), [publisher article](https://www.sciencedirect.com/science/article/pii/S0012365X21000868).

For these four, DOI/Elsevier metadata were readable, ScienceDirect article/PDF requests returned 403, and the browser exposed a CAPTCHA rather than article text. API full/abstract views required authorization. CiteSeer manuscript links returned unavailable archive pages; OpenAlex exposed metadata/content locations but its content endpoint required authorization. No credentials, paywall circumvention, or paid access were used. Thus the exact indexed-abstract transcriptions below are explicitly weaker evidence than the opened full-text theorems.

## 2. Known recursions: hypotheses and exact failure at 57/87

### 2.1 Tripling and product

**Denniston, as explicitly restated by Ge, Lemma 2.2:** if there exist a TKTS(v) and an LKTS(v), there exists an LKTS(3v). Ge defines TKTS(v) using a transitive automorphism group of order v. This is a regular action, not merely an arbitrary transitive group.

Wang–Shi Section 1 and Liu–Lei Section 1 both explicitly say Zhang–Zhu removed the transitive-KTS restriction. The resulting tripling implication is LKTS(v) ⇒ LKTS(3v), with v an admissible KTS order. The replacement object is a transitive resolvable idempotent symmetric quasigroup, TRISQ(v).

**Product statement, indexed original abstract; body not independently opened:** Lei's hypothesis is LKTS(v), TKTS(v), and LR(u), with conclusion LKTS(uv). Zhang–Zhu's 2003 abstract says it removes TKTS(v), using TRISQs instead. Thus the improved implication is LKTS(v)+LR(u) ⇒ LKTS(uv), not an unrestricted product of arbitrary positive integers. The historical removal is independently corroborated by the opened Wang–Shi and Liu–Lei introductions; original theorem numbering and proof were not recovered.

The crucial LR condition is visible in the opened Zhao Section 2 / Zhou–Chang page 49. An LR(u) consists of u−1 KTS(u)s indexed by (k,j), 1≤k≤(u−1)/2, j∈{0,1}, with specified resolutions. One selected parallel class from each system in either row has the same union A, which is itself a KTS(u); the union of all component systems covers every triple. These are not u−1 disjoint KTSs. In particular, LR(u) necessarily has u≡3 (mod 6). The quasigroup definition also requires partitions of the point set into triples; it cannot supply a resolvable object on 19 or 29 points.

**Arithmetic obstruction:** tripling 57 and 87 would require LKTS(19) and LKTS(29), respectively, neither even admissible as a KTS. In the stated product theorem both u and v are divisible by 3, hence 9 divides uv. Neither 57 nor 87 is divisible by 9. Equivalently their only nontrivial factorizations are 3·19 and 3·29, and the 19/29 factor cannot be an LR or an LKTS ingredient. This excludes the stated product mechanism, not other product-like constructions using weaker ingredients.

### 2.2 The q^n+2 recursion

**Wang–Shi Theorem 2.1:** q is a prime power, q≡1 (mod 6), an LKTS(q+2) is given, and n≥2 is an integer. The output is LKTS(q^n+2).

For the targets q^n would be 55=5·11 or 85=5·17. Each is squarefree and has two distinct prime divisors. Consequently neither is a prime power, nor even an integer n-th power for n≥2. Setting n=1 would only assume the target itself and is not a recursion step.

Wang 2026's 7q+2 output also cannot equal 57 or 87: neither 55 nor 85 is divisible by 7. Its discussion of CO(55)/CO(85) concerns the targets viewed as q+2 inputs, not a way to invert the output formula.

### 2.3 Xu–Ji 2021: two distinct families; the order-147 issue

The family LKTS(2^(2n+1)+1) is explicitly attributed to Xu–Ji in the opened Liu–Lei introduction, using a special (2,1)-RSQS*(4^n). For n≥1 its first orders are 9,33,129; n=0 gives the trivial order 3. The targets require 56 or 86 to equal a power of 2, which is impossible.

**Important source-limited additional result:** the search-indexed publisher abstract for Xu–Ji 2021 states that the construction is also used with 3-wise balanced designs to obtain

    LKTS(6·5^m(4·5^n+1) ± 3),    m,n ≥ 0.

This explains **147 = 6·5·(4·1+1)−3**, with m=1,n=0. It also gives 27,33 at m=n=0 and 123,129 at m=0,n=1. It is not a consequence of tripling a KTS(49), because such a KTS cannot be resolvable. Do not substitute a guessed family 3·7^s.

This additional family still misses 57/87: solving for 5^m(4·5^n+1) gives 9 or 10 for 57, and 14 or 15 for 87. If n=0 the expression is 5^(m+1), hence neither pair; if n≥1 it is at least 21. The arithmetic is proved here, but the additional-family theorem is currently supported by an indexed publisher abstract, not an opened publisher body. An independently verified “all admissible orders below 200” table should retain this access caveat for its 147 entry unless another primary copy is obtained.

### 2.4 Liu–Lei 2023: RDSQS* is not merely an SQS

An RDSQS(t) is an SQS(t) whose derived STS(t−1) at every point is resolvable. Thus t≡4 (mod 6) is necessary.

**Theorem 1.1:** RDSQS(u+1) ⇒ LKTS(3u).

**Construction 3.2:** RDSQS*(t) ⇒ RDSQS(4t). In Section 3 the special RDSQS* hypothesis is the following, for every point x. Let B_x be the derived STS(t−1):

1. Choose a parallel class P'_x={B_(x,k):1≤k≤(t−1)/3} in B_x.
2. The multiset containing each triple of P'_x three times and every other derived triple twice has a resolution into t−1 parallel classes P_(x,k)^l, with 1≤k≤(t−1)/3 and 1≤l≤3.
3. For each k the three classes P_(x,k)^1,P_(x,k)^2,P_(x,k)^3 all contain the designated B_(x,k).

An arbitrary SQS, or an arbitrary resolution of each derived design, does not by definition provide these coupled multiplicity conditions.

Theorem 4.4 obtains RDSQS(u+1) and LKTS(3u) when u is a product of elements of

- {7·4^n−1:n≥1};
- {3·7^n:n≥0};
- {3·13^n:n≥0};
- {4^m25^n−1:m≥1,n≥0};
- {4·7^n−1:n≥0};
- {2q^n+1:n≥0, q a prime power with q≡7 (mod 12)};
- {45,57,81,93,105,117,141,165}.

Every displayed element is divisible by 3. In particular **57 in this list means LKTS(171), not LKTS(57)**.

There is a stronger, family-independent obstruction: the conversion RDSQS(u+1) ⇒ LKTS(3u) always has 3|u and hence 9|3u. To output 57 would require RDSQS(20), whose derived design would be a resolvable STS(19), impossible since 3∤19. To output 87 would require RDSQS(30); even SQS(30) is inadmissible, and the proposed derived order 29 is not an STS order. A known mcDSQS(20) is not a substitute for RDSQS(20).

### 2.5 Tan–Zhou 2025: exact small ingredient and outcome

Theorem 3.2 constructs RDSQS(2^(2n+1)+2) for every n≥0; Corollary 3.3 obtains LKTS(3·2^(2n+1)+3). This is again divisible by 9 and cannot produce either target.

The construction is genuinely auxiliary-design based:

- Lemma 3.1 explicitly constructs an RDCQS(8^4:2).
- For n≥3, Construction 2.4 uses a 2-RSQS*(4^(n−1)), an RDCQS(8^4:2), and an RDTD(3,4,8) to form an RDCQS(8^(4^(n−1)):2).
- Construction 2.1 fills the groups plus stem. Its general hypotheses are a gcDCQS(g^r:s), an mcDSQS(g+s), and a gcDSQS(g+s,s), yielding mcDSQS(gr+s). For the stated RDSQS family the local order is 8+2=10.

Construction 2.4 requires a 2-RSQS*(v), a gcDCQS(m^4:s), an RDTD(3,4,m), and 4m+s≡2 or4 (mod6); it yields gcDCQS(m^v:s). The special 2-RSQS* is a coupled family of v−1 S(2,4,v)s whose triple bundles share prescribed parallel classes, with ordinary blocks occurring twice and special blocks three times. It is not implied by having LKTS(15) or LKTS(21).

Finally, deriving KTS(87) from a hypothetical suitable SQS(88) would only produce individual KTSs on different 87-subsets. It does not partition the triples of one fixed 87-set. The RDSQS/OLKTS⁺ conversion in the opened papers retains the factor 3.

## 3. General block-type equations for four groups and a stem

Let X be the disjoint union of four groups G_0,...,G_3 of size g and a stem H of size h, so N=4g+h. In one STS(N), write the counts of block types as

- a: HHH;
- b: HHA (two stem points, one group point);
- c: HAA (one stem point, two points in one group);
- d: HAB (one stem point, points in two different groups);
- e: AAA (three points of one group);
- f: AAB (two points of one group, one of another);
- k: ABC (three different groups).

Counting respectively stem pairs, stem–group pairs, within-group pairs, and cross-group pairs gives

    3a+b = C(h,2),
    b+c+d = 2gh,
    c+3e+f = 4 C(g,2),
    d+2f+3k = 6g^2.                       (1)

For example an HHA block contributes two stem–group pairs, an AAB block one within-group and two cross-group pairs, and an ABC block three cross-group pairs. This proves (1).

Across a complete large set the type totals, in the same order, must be

    C(h,3), 4g C(h,2), 4h C(g,2), 6hg^2,
    4 C(g,3), 12g C(g,2), 4g^3.           (2)

These simply count every possible triple of each type once. Equations (1)–(2) are necessary but do not ensure resolvability or construct an LKTS.

**Fixed-subsystem bound (w≥3).** In a family of pairwise block-disjoint STS(N)s, at most w−2 members can contain an STS(w) on the same fixed w-set W. Indeed a fixed pair in W must get a third point in W in every such member; only w−2 choices exist and repeated choices repeat a block. This bound applies even without resolvability.

## 4. The 4v−3 route: a valid single-system construction, an invalid large-set construction

Take g=v−1, h=1. For v≡3 (mod6), g is even and 3g is divisible by3. A Kirkman frame KF(g^4) exists by the standard spectrum quoted in Tan–Zhou Section 2: m even, number of groups at least4, and m(r−1) divisible by3.

A frame KF(g^4) is a triple decomposition of the complete four-partite graph, resolved into classes each omitting one group. It has g/2 classes omitting each group: if C is the total number of classes, then a point of G_i lies in C−c_i=3g/2 classes; the c_i are therefore equal, and 3c_i=3g/2. Thus c_i=g/2 and C=2g.

Fill each of the g/2 classes missing G_i with one parallel class of a KTS(g+1) on G_i∪{∞}. Every resulting class partitions X; all pairs are covered once. This constructs a KTS(4g+1)=KTS(4v−3).

**At v=15:** g=14, N=57. Each frame has 392 ABC blocks and 28 holey classes; each of the four KTS(15)s has 35 blocks and 7 parallel classes. The result has 532 blocks, 28 classes, and 19 triples per class, as required.

**Rigorous obstruction to repeating this for a large set:** every constructed system contains an STS(15) on each fixed G_i∪{∞}. The fixed-subsystem bound allows at most13 disjoint systems, whereas LKTS(57) requires55. Moreover all ∞AB and AAB triples are absent from this entire fixed-hole scheme. This is not just a divisibility defect; it omits entire triple types.

For g=14,h=1, one such system has

    (c,d,e,f,k) = (28,0,112,0,392).

The full large-set totals would be

    (c,d,e,f,k) = (364,1176,1456,15288,10976).

### A precise replacement object for 57: a mixed frame package

Here is a proved sufficient condition which retains all four input LKTS(15)s but explicitly supplies the missing triple types.

Let Y be the union of four 14-sets. Supply:

1. Thirteen pairwise block-disjoint frames F_i of type 14^4 on Y.
2. A 1-factorization {M_t:1≤t≤42} of the cross-group graph K_(14,14,14,14).
3. For each t, a Kirkman frame Q_t of type 2^28, whose 28 groups are the edges of M_t. Require Q_t to contain no AAA triple relative to the four original 14-groups.
4. Every AAB triple occurs in exactly one Q_t; every ABC triple occurs exactly once among all F_i and Q_t.

The matching ingredient in item 2 is elementary: use the three pairings of four group labels. For each pairing {(i,j),(k,l)} and each t in Z_14, take the edges (i,x)(j,x+t) and (k,x)(l,x+t), x in Z_14. These 42 perfect matchings partition all cross-group edges.

**Proof of sufficiency.** Fill F_i using the i-th KTS(15) on each G_j∪{∞}, choosing the four input large sets independently. This gives thirteen KTS(57)s and uses exactly all AAA and ∞AA triples. A frame Q_t has one holey class for each 2-point group; append the triple consisting of that pair and ∞ to its class. This gives another KTS(57). Across the 42 such systems all ∞AB triples occur exactly once by the factorization. Conditions 3–4 partition the remaining AAB/ABC triples. Therefore these 13+42=55 systems form LKTS(57).

The counts force each Q_t to have 364 AAB and 140 ABC blocks: every original within-group pair must be covered in an AAB block, so there are 4C(14,2)=364; the remaining 1176−28−2·364=420 cross-group pairs require140 ABC blocks. Its 504 triples are resolved into28 classes of18 triples; adjoining the ∞-triple makes19. The totals check symbolically as

    42·364 = 15288,
    13·392 + 42·140 = 10976.

**Unproved ingredient:** the mutually compatible frame package in items1,3,4. Existence of one KF(14^4), or separate existence of KF(2^28)s, does not provide this triple-disjoint packing. This is the exact next design object for this 4v−3 approach, not a claimed new recursion theorem.

## 5. The 4v+3 route: why direct stem inflation fails

The most literal representation of 87 is four groups of21 plus a common 3-point stem.

### 5.1 Three distinct obstructions to naive constructions

1. **KF(21^4) is impossible.** In the frame count above, each group would have to be omitted in g/2=21/2 classes. This proves the parity obstruction directly.
2. **Filling a 21-group plus a 3-hole is impossible even at pair level.** An STS(24,3) would have, for an outside point x, 23 pairs involving x, all of which must be covered by triples contributing two such pairs each. Its replication would be23/2. Thus the proposed KTS(24,3) ingredient does not exist.
3. **Synchronizing four full KTS(21) parallel classes fails.** Their union covers84 points and leaves precisely H; each resulting global parallel class would have to include H itself as a triple. Four KTS(21)s have10 parallel classes each. Synchronizing all ten would repeat H ten times in one STS. Only one global class may be assembled this way.

Also, retaining a subsystem on each fixed21-group in every output system permits at most19 disjoint systems, not the85 required by LKTS(87). None of these statements excludes a construction that breaks the local resolutions, changes holes between colors, or adds mixed block types.

### 5.2 A smaller first auxiliary object that repairs the resolution count

A possible restricted seed-stage object is a GDD(2,3,87) of type 21^4 1^3, with the three singleton groups forming H, equipped with:

- ten classes partitioning X\G_i for each i=0,1,2,3;
- three full classes partitioning X.

There are40 holey and3 full classes. For a point in G_i the replication is43−10=33=(87−21)/2, while a stem point occurs43 times. The total block count is40·22+3·29=967.

Fill its ten G_i-holes with the ten parallel classes of a KTS(21) on G_i. This proves that such an object, together with four KTS(21)s, yields a KTS(87) without the odd-group frame obstruction. It is a mixed-resolution GDD, not an ordinary Kirkman frame and not asserted to exist here.

For nineteen pairwise disjoint such objects, fill with the nineteen systems from each of four LKTS(21)s. To complete a large set one must still construct66 further systems with no AAA blocks. It would be incorrect to call nineteen seed systems a solution of the recursion.

### 5.3 Exact block counts after the nineteen-seed split

For g=21,h=3 equations (1) are

    3a+b=3,
    b+c+d=126,
    c+3e+f=840,
    d+2f+3k=2646.

A seed retaining four KTS(21)s has e=280 and hence c=f=0. It has either

    (a,b,c,d,e,f,k)=(1,0,0,126,280,0,840),

or

    (a,b,c,d,e,f,k)=(0,3,0,123,280,0,841).

At most one seed may have the first type, since H is a single triple. If exactly one of the19 seeds has it, they exhaust every AAA triple and H itself. The remaining66 systems must each satisfy

    a=e=0, b=3, d=123−c, f=840−c, k=281+c,
    0≤c≤123.

Across those66 systems the required totals are

    sum(b,c,d,f,k)=(198,2520,5598,52920,21066).

These follow by subtracting the19 seed contributions from the exact large-set inventory

    (a,b,c,d,e,f,k)=(1,252,2520,7938,5320,52920,37044).

### 5.4 A complete stem-deletion formulation of the unresolved object

There is a more intrinsic way to state what must replace the impossible KF(21^4). It applies to any putative LKTS(87), not only the seed ansatz.

Fix H={s0,s1,s2}, Y=X\H, |Y|=84. There is exactly one color/system containing H; call it *. In each of the other84 colors t, the three stem pairs force blocks

    {s0,s1,a_t}, {s0,s2,b_t}, {s1,s2,c_t}.

The points a_t,b_t,c_t are distinct in each color: equality would repeat a stem–outside pair. Across84 colors, each of the three lists a,b,c is a permutation of Y, because each HHA triple occurs once.

The blocks containing exactly one stem point define matching arrays M_(s,t) on Y:

- In color *, each M_(s,*) is a perfect matching of Y with42 edges.
- In an ordinary color t, M_(s0,t) misses {a_t,b_t}, M_(s1,t) misses {a_t,c_t}, and M_(s2,t) misses {b_t,c_t}; each has41 edges.
- The three matchings in a fixed color are edge-disjoint, since an outside pair cannot occur twice in its STS.
- For each fixed s, the matchings over all85 colors partition E(K_84): 42+84·41=C(84,2).

For one stem alone, this matching-count pattern is realized by taking a 1-factorization of K_86 and deleting two distinguished vertices: the factor pairing those two vertices restricts to a perfect matching on84 points, and every other factor misses two points. **What is not supplied by this observation is three jointly compatible factorizations with the stated shared a,b,c holes, nor the triangle completion.**

For each color t put L_t=K_84 minus the union of its three stem matchings. The pure-Y blocks must triangle-decompose L_t, and the triangle sets across all85 colors must partition all triples of Y. They must also have the following prescribed resolutions:

- Color *: one class with28 pure-Y triples accompanies H; the other42 classes each contain three disjoint stem-matching edges and26 pure-Y triples covering their complement.
- Each ordinary color: the three HHA blocks occupy three distinct classes (any two share a stem point). Each such class also contains one edge from the remaining stem's matching and27 pure-Y triples. The other40 classes contain one edge from each stem matching, pairwise vertex-disjoint, and26 pure-Y triples.

Here a prescribed resolution is an actual partition of the complete per-color block inventory, not merely the displayed class sizes: every matching edge and every pure-Y triangle is assigned exactly once. In an ordinary HHA class the remaining-stem matching edge avoids the HHA block's outside point; the 27 pure-Y triples partition the other 81 points. In every other class the displayed blocks are pairwise disjoint and cover precisely their stated complement.

Thus a normal color needs1121 pure-Y triangles and color * needs1120. The pure triple total is84·1121+1120=C(84,3). The outside graph has degree80 everywhere in color *, and in a normal color degree82 at a_t,b_t,c_t and degree80 elsewhere, so its triangle replication constraints are integral.

**Sufficiency is exact:** append the prescribed stem triples to the triangle classes. Every class partitions87 points; every pair is covered once within its color; the permutation and matching-partition conditions cover all triples meeting H once; the global triangle partition covers the remaining triples once. This yields an LKTS(87).

This coupled matching/triangle-resolution object is the precise unresolved replacement for naive hole inflation. The nineteen-seed route additionally fixes its AAA triangles to the four known LKTS(21)s in nineteen colors. The counts leave it arithmetically viable, but no existence proof or certificate is supplied.

## 6. What was actually established

- The stated tripling, LR-product, q^n+2, and RDSQS conversions have concrete parameter obstructions at57/87; the binary family has an elementary numerical obstruction.
- The Xu–Ji additional-family explanation of147 was identified, with its original-body access limitation retained. A guessed 3·7^s theorem is unnecessary and should not be asserted.
- A fixed four-hole filling construction cannot make either large set: at57 it is capped at13 systems and omits two whole triple types; at87 its ordinary frame and local24-point ingredients are impossible.
- A fully proved sufficient frame package for57 and an exact coupled matching/triangle-resolution formulation for87 were derived, including all class counts and global block-type inventories.
- The missing compatible auxiliary objects remain missing. These restricted obstructions are not nonexistence theorems for LKTS(57), LKTS(87), or all possible 4v±3 recursions.
