# F560 — Complete WRITTEN review

**Role:** WRITTEN  
**Candidate status:** Reviewed here at its exact stated scope; **not adopted by this return**.  
**Scientific code or execution:** **NONE / NOT RUN**.

**Overall correctness:** correct.  
**Explanation:** The complete frozen candidate supports the exclusion of the whole actual \(4455\) stratum under its stated support-\(48\), \(t=24\), common-complex-tensor hypotheses. I reconstructed the twin and phase lemmas, the forced \((4,4,2,2)\) profiles, all six rounding consumers, and the direct contradiction in the same maximal set \(P\); the primary proof requires no external no-OLS theorem.  
**Confidence:** 0.97.

**Candidate findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**

## 1. Frozen bindings, access and method

The following measurements are **parent-attributed**, not independently executed child hash/count observations:

| Artifact | Parent-supplied SHA-256 | Parent-supplied size |
|---|---|---|
| Manifest | `a2a31b17dc05425ab2956ca06b2ebc3e79d31245621b13e151078e891ec99f02` | 7,473 bytes; 119 LF |
| Freeze receipt | `4e94d46145f5089b45e52ea38ba533d47f0a3aa2a7ba49629e4cc5ddfb1ed460` | 1,933 bytes; 47 LF |
| Literal packet | `60956ee093ca047f32946a5f10de7638d1e44e558ce41ab1b0b979cc8b110890` | 44,483 bytes; 899 LF |
| S1 — complete f539 author candidate | `454a52525b65308d262a181673cb4d43c546347bda338ff47393c89140a62c2e` | 30,738 bytes; 858 LF; 859 logical lines |
| S2 — prior necessary-condition disposition | `60448959ee1043506210ebec876ede3fc2b91d233781a06d6513942129837632` | 7,588 bytes; 38 LF |

The parent supplied the native observation **2026-10-30T13:16:27-0700 PDT**. I do not claim this as my native start, completion time, or measured duration.

### Read order

Before mathematical packet reads or derivation, I read:

- the mandatory memory summary and relevant review/acceptance skills;
- the complete manifest and freeze receipt;
- the complete dispatch receipt and parent live metadata supply;
- all twelve declared permission/status controls, including their endings.

I then sent the required **direct administrative pre-body ACK to Main**.

Only afterward did I read the complete mathematical packet in consecutive raw windows of at most twenty lines:

\[
1\!-\!20,\ 21\!-\!40,\ \ldots,\ 861\!-\!880,\ 881\!-\!899.
\]

This included S1 logical line 859 and S2 line 38. Mathematical reconstruction began only after the final packet window.

**Administrative correction:** My initial ACK gave an unsupported exact line count for the parent metadata supply. I withdrew that count in a direct additive correction to Main: the actual reads were raw windows through `101–120`, including the closing brace. This is a reviewer reporting correction, not a candidate mathematical finding or an incomplete-body-read waiver.

### Method boundary

This review used written reasoning from the frozen packet, including its explicit normalized formal cases. It used:

- no additional privately selected parameter, graph, tensor, \(P,E\) fixture, matrix or numerical probe;
- no scientific code, CAS, solver, enumeration or replay;
- no linked source, sibling review, author checker or held mathematical payload;
- no held episode or its proof, selection, planning or confidence consumers.

Manifest guidance and the author argument were visible, so this is **not a blind reconstruction or cognitive-isolation claim**. It is a separate same-harness written review.

## 2. Exact theorem reviewed

The supported statement is:

> There is no \(U=6\psi\in(\mathbb C^6)^{\otimes4}\) whose three balanced flattenings \(12\mid34\), \(13\mid24\), and \(14\mid23\) are unitary, which has exactly 48 nonzero entries and exactly 24 modulus-one entries, and whose residual coordinate-alphabet sizes are \((4,4,5,5)\).

The proof permits arbitrary nonzero complex residual amplitudes. It does not assume:

- no-distance-one;
- no orthogonal Latin squares;
- equal residual moduli or real signs;
- independent realizability of separately chosen pair graphs;
- independent choices of maximal supports.

The same actual sets \(P,E\) must satisfy every projection and orthogonality condition throughout.

## 3. Common-\(P,E\) interface — SUPPORTED

**Source:** S1 lines 43–109.

Every entry of a unitary matrix has modulus at most one. Thus the 48 nonzeros split into the 24 modulus-one entries \(P\) and the other 24 nonzeros \(E\).

A modulus-one entry exhausts its row and column in each flattening. Distinct maximal entries therefore occupy distinct rows and columns, and no residual entry shares those rows or columns.

Removing the 24 maximal rows and columns leaves a \(12\times12\) unitary residual matrix with 24 nonzeros. A residual singleton row or column would contain a modulus-one entry, contrary to its definition. Every residual row and column therefore has at least two nonzeros. The total count forces exactly two in each.

Applying this to the rows and columns of all three balanced cuts proves, for every physical pair \(ij\),

\[
|R_{ij}|=12,\qquad
|\{w\in E:\pi_{ij}(w)=b\}|=2
\quad(b\in R_{ij}),
\]

and

\[
\pi_{ij}(P)=[6]^2\setminus R_{ij}
\]

injectively.

For an internal symbol \(a\in A_i\), projection injectivity makes its \(p_i(a)\) maximal partners distinct at every other party. The complementary residual neighbor count is consequently

\[
r_i(a)=6-p_i(a),
\]

independent of the partner party. Its residual slice has \(2r_i(a)\) words, and the residual graph degree sum is 12.

If \(r_i(a)=1\), both residual words in the slice would use the same unique neighbor at every other coordinate, making them identical. Hence \(r_i(a)\ge2\).

Finally, two residual rows sharing one column cannot share only that column: their inner product would be one nonzero product. Because each row has exactly two nonzeros, they must have the same two-column support. The residual support is therefore a disjoint union of full \(2\times2\) unitary blocks in each cut.

These statements concern the **same** \(P,E\), not six independent projection relaxations.

## 4. Degree bounds and both maximal-word regimes — SUPPORTED

**Source:** S1 lines 113–186.

Let \(k(w)\) be the number of internal coordinates of a maximal word. Counting internal positions and internal pairs gives

\[
\sum_{w\in P} k(w)=60,\qquad
\sum_{w\in P}\binom{k(w)}2=49.
\]

For \(k=0,1,2,3,4\), the quantity

\[
\binom{k}{2}-2k+3
\]

takes values \(3,1,0,0,1\). Consequently,

\[
3n_0+n_1+n_4=49-2\cdot60+3\cdot24=1.
\]

Thus \(n_0=0\) and \(n_1+n_4=1\). In particular, at most one maximal word has exactly one internal coordinate. No selection between the F and S regimes has been assumed.

For a fixed internal symbol \(a\), count the other internal coordinates among its \(6-r_i(a)\) maximal words. Writing \(\sigma,\tau,f\) for the one-, three-, and four-internal counts through \(a\) gives

\[
\sum_{j\ne i}q_j-3r_i(a)
=(6-r_i(a))-\sigma(a)+\tau(a)+2f(a).
\]

It follows that

\[
\tau+2f-\sigma=
\begin{cases}
8-2r,&q_i=4,\\
7-2r,&q_i=5.
\end{cases}
\]

Because \(\sigma\le1\), both equations imply the integral bound \(r\le4\).

Together with \(r\ge2\) and degree sum 12, this leaves exactly

\[
(3,3,3,3),\quad (4,3,3,2),\quad (4,4,2,2)
\]

at a four-symbol party, and

\[
(3,3,2,2,2)\quad\text{or}\quad(4,2,2,2,2)
\]

at a five-symbol party.

A five-party degree-four symbol forces \(\sigma=1\). Two different five-symbol parties cannot both require that unique one-internal maximal word, because such a word has only one internal coordinate. Thus at most one five-party profile is exceptional.

This supplies the complete degree classification used later, including the nonregular four-party cases.

## 5. Full-slice twin saturation and disjointness — SUPPORTED

**Source:** S1 lines 190–259.

Suppose residual words differing only at coordinate \(i\) use symbols \(a,a'\). Let \(V_a,V_{a'}\) be their other-coordinate slices and put

\[
T=V_a\cap V_{a'}\ne\varnothing.
\]

For each other coordinate \(j\), the two triples with a fixed used \(j\)-value form a pair in \(V_a\). If one is in \(T\), the rows indexed by \((a,j)\) and \((a',j)\) share a column in the actual cut \(ij\mid kl\). Block closure forces the second triple into \(T\) as well.

Thus each of the three other coordinates supplies a perfect matching on \(T\).

Two vertices cannot share two of those coordinates: their copies at both \(a,a'\) would yield four extensions of the shared physical pair. The three matchings therefore form a simple cubic graph.

For each vertex,

\[
z_v=U_{a,v}\overline{U_{a',v}}\ne0.
\]

Row orthogonality on each matching edge gives \(z_v=-z_{v'}\). An odd cycle would imply \(z_v=-z_v\), impossible. The graph is bipartite.

A simple cubic bipartite graph needs at least three vertices on each side. Since every slice has at most eight words,

\[
|T|\in\{6,8\}.
\]

The possible slice sizes are \(4,6,8\). An eight-word slice cannot contain a six-word overlap: each coordinate value used by \(T\) already occurs twice, so the two leftover triples must use the single remaining value at every coordinate and hence coincide. Therefore

\[
V_a=V_{a'}=T,\qquad |T|\in\{6,8\},
\]

and both symbols have the same degree, three or four.

This proves, rather than assumes, that no distance-one pair can vary through a low symbol.

Twin pairs at one coordinate cannot share a symbol: equality of slices would then give three extensions of a physical pair. Components at different coordinates cannot share a word either: that word and its two distinct single-coordinate flips would be three extensions of the complementary physical pair.

## 6. Low-to-low complex obstruction — SUPPORTED

**Source:** S1 lines 263–349.

The two extensions of a low-to-low pair are distinct. Assume, as in the author’s explicit formal case, that they differ at both complementary coordinates. Relabeling gives

\[
0000,\qquad1100
\]

with the fixed low coordinates at parties 3 and 4.

Each low slice has four words and induces three balanced two-by-two partitions at the other coordinates. In the low party-3 slice, the partitions at parties 1 and 2 are both different from the party-4 partition, because the two displayed words agree at party 4 but differ at parties 1 and 2.

If the party-1 and party-2 partitions agreed, words sharing both values would differ only at the low party-4 coordinate. Twin saturation forbids this. All three partitions must therefore differ. The same reasoning applies to the low party-4 slice.

This forces precisely the six displayed words

\[
0000,\ 1100,\ 0101,\ 1001,\ 0110,\ 1010.
\]

In \(13\mid24\), the row containing \(0000,0101\) shares a column with the row containing \(1010\), forcing \(1111\). The row containing \(1100,1001\) shares a column with the row containing \(0110\), forcing \(0011\).

All eight even-parity binary words are therefore present. Fixing any two binary coordinates leaves exactly two of these words, so every used physical pair has already exhausted its two extensions. The author’s three displayed blocks are genuine closed blocks.

For a full nonzero complex unitary block, row orthogonality implies

\[
\arg u-\arg v-\arg w+\arg x\equiv\pi\pmod{2\pi}.
\]

This does not require real entries or equal moduli.

With the author’s \(X,Y,Z\), the three cuts impose

\[
X-Y\equiv\pi,\qquad
X-Z\equiv\pi,\qquad
Y-Z\equiv\pi.
\]

Subtracting the second congruence from the first and adding the third gives \(0\equiv\pi\pmod{2\pi}\), a contradiction.

Hence the original two extensions differ at exactly one complementary coordinate, where full-slice twin saturation applies.

No extra selected example was needed: the reconstruction uses the candidate’s explicit quantified normalization case.

## 7. Excluding every four-party twin — SUPPORTED

**Source:** S1 lines 353–412.

### Isolation

A twin component at a four-symbol party exhausts the words through its two symbols. A twin component at another coordinate must avoid both symbols, by component disjointness. But its degree is at least three, while only two residual symbols remain at the four-symbol party. This is impossible.

There cannot be two twin pairs at that same four-symbol party. Their degrees would both be three. Every symbol at either five-symbol party would then have a neighborhood that is a union of whole twin pairs, so its degree would be two or four. Five positive such degrees summing to twelve force the exceptional profile \((4,2,2,2,2)\) at both five-symbol parties, contradicting the unique-exception restriction.

Therefore, if a four-party twin exists, it is the only twin pair in the tensor.

### Degree-four twins

The other two symbols at that four-symbol party must both have degree two. At a five-symbol party, the degree-four twins have four common neighbors and omit one residual symbol. That omitted symbol can neighbor only the other two four-party symbols, so it is low and adjacent to both.

There is then a low-to-low pair whose complementary twin, required by the complex obstruction, would have to occur at another coordinate. Isolation forbids it.

### Degree-three twins

Let the twins be \(a,a'\), with remaining four-party symbols \(u,v\).

At the other four-symbol party, their common three-element neighborhood omits a symbol \(b\). It has only \(u,v\) as possible neighbors, hence is low and adjacent to both. At each five-symbol party, the two omitted symbols are likewise low and adjacent to both \(u,v\).

The low symbol \(b\) cannot neighbor a low symbol at either five-symbol party. A complementary twin would either occur at another coordinate, contrary to isolation, or be \(a,a'\), which are not adjacent to \(b\).

Thus \(b\) has two distinct high neighbors at each five-symbol party, forcing both five-party profiles to be ordinary.

Each of \(u,v\) already has the two omitted low neighbors at each five-symbol party. Because \((u,b)\) and \((v,b)\) occur, each also needs a high neighbor there. Their degrees are at least three and sum to six, so both are exactly three.

For the fixed residual pair \((u,b)\), only one high value remains available at each complementary five-symbol party. Its two extensions would coincide, contradicting exact multiplicity two.

This excludes degree-three twins as well. There is consequently **no distance-one pair varying at party 1 or 2**, for any of the three allowed four-party profiles.

## 8. Forced sectors and nonregular profiles — SUPPORTED

**Source:** S1 lines 416–513.

A low-to-low pair in \(R_{34}\) would require a twin at party 1 or 2, already excluded. Hence

\[
R_{34}\cap(L_3\times L_4)=\varnothing.
\]

If a five-symbol party were exceptional, it would have only one high symbol. Any low symbol at the opposite party requires two distinct neighbors, both high by the displayed exclusion. This is impossible.

Both five-party profiles are therefore ordinary. Each low symbol uses both opposite high symbols; these edges exhaust the degree-three high symbols. Thus

\[
R_{34}=(L_3\times H_4)\sqcup(H_3\times L_4).
\]

For \(i=1,2\), define

\[
x_i(a)=|N_{i3}(a)\cap L_3|,\qquad
y_i(a)=|N_{i3}(a)\cap H_3|.
\]

Counting the **same residual words** in the two sectors gives

\[
x_i(a)=|N_{i4}(a)\cap H_4|,\qquad
y_i(a)=|N_{i4}(a)\cap L_4|,
\]

and \(r_i(a)=x_i(a)+y_i(a)\). These equalities do not substitute independent graph counts for actual support compatibility.

In a low party-3 slice, equality of the party-1 and party-4 partitions would produce a forbidden party-2 distance-one pair; equality of the party-2 and party-4 partitions would produce a forbidden party-1 distance-one pair.

The remaining partition patterns make every used party-\(i\) value occur with both party-4 neighbors. Those neighbors are exactly \(H_4\). Therefore \(x_i(a)>0\) implies \(x_i(a)=2\). The symmetric low party-4 argument proves the same assertion for \(y_i\).

Consequently,

\[
x_i(a),y_i(a)\in\{0,2\}.
\]

The sums are both six: the three low party-3 symbols contribute two edges each, and the two high party-3 symbols contribute three each. Each function is therefore two on three of the four symbols and zero on one.

Their zero symbols differ, since a common zero would give residual degree zero. With the candidate’s naming,

\[
a_i^X:(x_i,y_i)=(2,0),\qquad
a_i^Y:(x_i,y_i)=(0,2).
\]

The remaining symbols have \((2,2)\), proving the forced profile

\[
(4,4,2,2)
\]

at **both** four-symbol parties.

Since positive \(y_i\) means adjacency to both elements of \(H_3\), and positive \(x_i\) means adjacency to both elements of \(H_4\), this also proves

\[
N_{i3}(h)=A_i\setminus\{a_i^X\},\qquad
N_{i4}(k)=A_i\setminus\{a_i^Y\}.
\]

The naming is consistent: \(a_i^X\) is the zero of \(y_i\), and \(a_i^Y\) is the zero of \(x_i\).

## 9. Forced high twins and six-projection rounding — SUPPORTED

**Source:** S1 lines 517–631.

The low symbol \(a_1^Y\) has low party-4 neighbors. For one of those residual low-to-low pairs, the complementary twin cannot occur at party 2, so it occurs at party 3. The sector decomposition forces its two values to be the two elements of \(H_3\). They are full degree-three twins.

The symmetric argument using \(a_1^X\) and a low party-3 neighbor forces the two elements of \(H_4\) to be full twins.

Thus the actual residual set splits as

\[
E=C_3\sqcup C_4,
\]

where each component has twelve words. Their common slices \(T_3,T_4\) have six triples.

The matching graph on each common slice is simple, cubic and bipartite by the already reconstructed twin proof. On six vertices it is \(K_{3,3}\). Every used coordinate value occurs twice. Projection onto any two slice coordinates is injective, since otherwise the two twin copies would give four extensions of a physical pair.

### Rounding rule

Color each slice graph by its two bipartition classes and retain, for each triple, the twin copy indicated by its color.

- For a physical pair **not containing the twin coordinate**, the slice’s injective pair projection supplies one triple, and exactly one of its twin copies is retained.
- For a physical pair **containing the twin coordinate**, the two triples with the other fixed coordinate value form a matching edge. Their opposite colors retain each twin symbol exactly once.

The complete consuming-side check is:

| Pair | \(C_3\to F_3\) | \(C_4\to F_4\) |
|---|---|---|
| \(12\) | Injective slice projection \(12\) | Injective slice projection \(12\) |
| \(13\) | Party-1 matching | Injective slice projection \(13\) |
| \(14\) | Injective slice projection \(14\) | Party-1 matching |
| \(23\) | Party-2 matching | Injective slice projection \(23\) |
| \(24\) | Injective slice projection \(24\) | Party-2 matching |
| \(34\) | Party-4 matching | Party-3 matching |

Every used pair already has two extensions within its original component. Consequently the components cannot share a projected physical pair: that would give four extensions in \(E\).

It follows that \(F=F_3\sqcup F_4\) has twelve words and projects bijectively onto each \(R_{ij}\). The original \(P\) supplies exactly the complementary 24 pairs at every projection. Hence

\[
Q=P\sqcup F
\]

has 36 words and is an \(\operatorname{OA}(36,4,6,2)\).

The Latin-square interpretation follows from all six consumers: \(12\) gives the indexing grid, \(13,23\) and \(14,24\) give the two Latin properties, and \(34\) gives orthogonality.

This is a conditional construction from the hypothesized actual support, not a physical witness or a claim that the retained original amplitudes form a new unitary tensor.

## 10. Direct contradiction in the same \(P\) — SUPPORTED

**Source:** S1 lines 635–704.

This is the decisive primary endpoint. It needs Sections 2–7, **not** the rounding or an external no-OLS theorem.

Write \(a_X=a_1^X\) and \(a_Y=a_1^Y\). They are distinct. The forced neighborhoods and maximal-complement identity give:

- for every \(h\in H_3\), its maximal party-1 partners are exactly \(O_1\cup\{a_X\}\);
- for every \(k\in H_4\), its maximal party-1 partners are exactly \(O_1\cup\{a_Y\}\).

A maximal word with its \(34\)-pair in \(H_3\times H_4\) must therefore have party-1 value in

\[
(O_1\cup\{a_X\})\cap(O_1\cup\{a_Y\})=O_1.
\]

Now fix an arbitrary \(h\in H_3\). It has residual degree three and thus exactly three maximal words. Their party-1 values cover \(O_1\cup\{a_X\}\) injectively.

Its residual party-4 neighbors are \(L_4\), so its three maximal party-4 partners are the two elements of \(H_4\) and the unique outside symbol \(o_4\).

The two maximal words using \(H_4\) must have party-1 values in \(O_1\). Injectivity at \(13\) makes those values distinct, exhausting the two-element set \(O_1\).

The remaining maximal word must therefore have

\[
w_1=a_X,\qquad w_4=o_4.
\]

There are two distinct \(h\in H_3\). Repeating the universally quantified argument gives two distinct maximal words with the same actual \(14\)-pair \((a_X,o_4)\). This contradicts injectivity of \(\pi_{14}(P)\).

Every transition uses the same maximal support:

\[
\text{residual neighborhoods}
\longrightarrow
\text{maximal complements}
\longrightarrow
13\text{-injectivity}
\longrightarrow
14\text{-collision}.
\]

There is no independently chosen support, missing routing condition or unproved simultaneous-realization step at this endpoint.

## 11. Claim dispositions and remaining imports

| Claim | Disposition |
|---|---|
| Common residual multiplicity two and maximal complement at all six pairs | **SUPPORTED** |
| Full-slice twin saturation and component disjointness | **SUPPORTED** |
| Arbitrary-complex low-to-low obstruction | **SUPPORTED** |
| Exclusion of all four-party twins, including nonregular profiles | **SUPPORTED** |
| Both five-party profiles ordinary and exact \(R_{34}\) sectors | **SUPPORTED** |
| Both four-party profiles forced to \((4,4,2,2)\) | **SUPPORTED** |
| Both five-party high pairs forced twins | **SUPPORTED** |
| Same-\(P,E\) rounding at all six physical pairs | **SUPPORTED** |
| Direct common-\(P\) contradiction | **SUPPORTED** |
| Whole actual \(4455\) exclusion under the stated hypotheses | **SUPPORTED** |
| Independent validation of the cited external article’s proof | **INCONCLUSIVE / NOT PERFORMED** |
| Universal support-\(48\) exclusion or global support minimum | **NOT ESTABLISHED BY THIS CANDIDATE** |
| Worldwide novelty or priority | **NOT ASSESSED** |

### Exact import boundary

The primary proof has no remaining external no-OLS import. Its elementary unitary, counting and finite-graph steps have been reconstructed above.

S2’s common-tensor interface and degree/moment restrictions agree with the reconstruction. Its additional marked-graph classifications, defect formulas, historical finite-run results and linked reviews are **not needed for the direct proof** and are not independently re-certified by this return. No S2 link was followed.

The optional Euler–Tarry/Betten route remains separate. I did not open or validate the cited paper, and no conclusion here depends on its correctness, accessibility or detailed classification.

No mathematical compatibility step remains unpaid within the candidate’s stated direct \(4455\) exclusion. Adoption and any other frozen review gates remain separate parent decisions.

## 12. Findings and assurance ceiling

**Mathematical candidate findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The reviewer’s corrected metadata-line-count statement is an administrative reporting qualification, not evidence against the proof. No source-order breach, scientific execution or additional selected diagnostic occurred in this review.

This return supplies a complete **same-harness written reconstruction** of the frozen candidate. It does not supply:

- independent-family, human or kernel verification;
- an executed finite checker;
- a physical tensor or numerical witness;
- a novelty determination;
- parent adoption;
- a theorem about other residual-alphabet strata, other maximal-entry counts, or the global AME support minimum.

No working-tree file was edited. No scientific source was prepared or executed; no build, test, lint, formatter, external-model CLI, paid/heavy run, Git operation, installation, deletion, credential access or infrastructure change was performed.

**Final disposition: SUPPORTED at the complete stated actual-\(4455\) scope, with both the six-projection rounding and the self-contained direct common-\(P\) contradiction reconstructed. Candidate remains UNADOPTED pending the parent’s required gates.**