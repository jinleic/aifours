# author-candidate-v1.md — Actual AME(4,6), support 48, exactly 24 maximal entries: exclusion of the entire \(3555\) residual-alphabet branch

**Status: AUTHOR PROPOSAL — complete written proof candidate; not independently reviewed or adopted.**

This body is returned inline for parent materialization. No scientific executable, numerical experiment, file mutation, or external-source search was performed. Scientific execution: **NOTRUN**. All calculations below are explicit finite counting and written algebra.

## 1. Scope, inputs, and chronology

The proposed theorem concerns one actual complex tensor, with the same maximal support, residual support, amplitudes, and physical coordinates in all three balanced flattenings. It does not substitute unrelated pair graphs or independently gauged block supports.

Before opening the scientific packet, I read:

- The complete manifest, LF 1–117.
- The complete freeze receipt, LF 1–60.
- All ten declared permission/status controls through their endings.
- The complete parent metadata supply.

A direct pre-body ACK was successfully delivered to Main. I then read the complete literal packet, LF 1–98, in ordered raw windows of at most 20 LF, including all endings:

- S1: the \(4445\) disposition, LF 1–27.
- S2: the \(4455\) necessary-condition disposition, LF 1–38.
- S3: the separate exact-\(t=27\) exclusion, LF 1–31.

The manifest pin is `9f11c0092743d017dd9db0a7281777a080b056e079656f3f6d1b94e6e5726c6b`; the receipt pin is `89581ccc4b4ce8429909d56aed0f3fda56d1793f8949526c7fd7480e67c3a068`. Their live matches, byte/LF observations, and the clock `2026-10-30T12:17:35-0700 PDT` are **parent-attributed metadata**, not child-native execution. Main subsequently supplied the parent observation `2026-10-30T12:30:31-0700 PDT`; it is not my start or completion timestamp.

Held scientific payloads and consumers were not opened. Linked author, checker, and review files outside the assigned packet were not opened. No \(4455\) numerical formula, no-OLS premise, no-distance-one assumption, or \(t=27\) exclusion is imported into this proof.

## 2. Proposed theorem

Let \(\psi\in(\mathbb C^6)^{\otimes4}\) be normalized, and put \(U=6\psi\). Suppose:

1. All three balanced flattenings of this same \(U\) are unitary.
2. \(U\) has exactly 48 nonzero entries.
3. Exactly 24 entries have modulus one.
4. The coordinate alphabets occurring in the other 24 entries have sizes \(3,5,5,5\), up to a physical party permutation.

**Then these hypotheses are contradictory.**

The statement allows arbitrary complex phases, arbitrary nonzero residual moduli, and distance-one pairs. It is conditional only on the displayed actual-tensor hypotheses.

For notation, rename the physical parties \(0,1,2,3\), with residual alphabet size three at party \(0\). Write \(I=\{1,2,3\}\).

---

## 3. Actual common-support interface and block closure

Let \(P\) be the 24 modulus-one tensor words, and let \(E\) be the other 24 support words.

In any unitary flattening, a modulus-one entry exhausts its row and column. Thus:

- \(P\) projects injectively onto every physical pair system.
- No pair value used by \(P\) can be used by \(E\).
- Removing the 24 singleton rows and columns leaves a \(12\times12\) unitary supported exactly on \(E\).

A residual row or column cannot have one nonzero: that entry would have modulus one and would belong to \(P\). Since the residual matrix has 24 nonzeros, every residual row and column has exactly two.

Consequently, for every pair of distinct parties \(i,j\),

\[
R_{ij}:=\pi_{ij}(E)
\]

has 12 values, every value has exactly two \(E\)-extensions, and

\[
\pi_{ij}(P)=[6]^2\setminus R_{ij}.
\tag{3.1}
\]

These are projections of the **same** \(P,E\).

### 3.1 Every residual component is a full \(2\times2\) block

A bipartite support graph with all row and column degrees two is a union of even cycles. A cycle longer than four gives two rows sharing exactly one nonzero column. Their inner product is then one nonzero complex product, contrary to unitarity.

Therefore every residual flattening is a disjoint union of six full \(2\times2\) blocks.

In particular:

> If two residual rows share a column, they share both columns. The analogous statement holds for columns.

This actual-unitarity closure is essential below.

### 3.2 Marginals

Let \(A_i\) be the residual alphabet at party \(i\), and let \(B_i=[6]\setminus A_i\). Thus

\[
q=(3,5,5,5),\qquad b=(3,1,1,1).
\]

For \(a\in A_i\), let \(r_i(a)\) be its degree in \(R_{ij}\). This is independent of \(j\), because

\[
|\{e\in E:e_i=a\}|=2r_i(a).
\tag{3.2}
\]

If \(p_i(a)\) is its number of \(P\)-occurrences, (3.1) gives

\[
p_i(a)=6-r_i(a),\qquad \sum_{a\in A_i}r_i(a)=12.
\tag{3.3}
\]

Also \(r_i(a)\ge2\). Otherwise \(r_i(a)=1\) would give two residual words using \(a\), but only one possible symbol at each other coordinate, making those words identical.

Every outside symbol in \(B_i\) occurs in exactly six \(P\)-words and no \(E\)-word.

---

## 4. Fresh \(3555\) moments, word profiles, and outside counts

Call a coordinate internal when its value lies in \(A_i\). Let \(n_s\) count \(P\)-words with exactly \(s\) internal coordinates.

The total number of internal coordinate incidences is

\[
\sum_s s n_s
=\sum_i(24-6b_i)
=96-36
=60.
\]

The total number of internal pair incidences is

\[
\sum_s \binom{s}{2}n_s
=\sum_{i<j}(q_iq_j-12)
=3\cdot15+3\cdot25-72
=48.
\]

Together with \(\sum_s n_s=24\), these imply

\[
3n_0+n_1+n_4
=48-2\cdot60+3\cdot24
=0.
\]

Hence

\[
(n_0,n_1,n_2,n_3,n_4)=(0,0,12,12,0).
\tag{4.1}
\]

Every maximal word has exactly two or three internal coordinates.

Let \(d_{ij}\) count maximal words internal exactly at \(i,j\). Their other two coordinates are outside, so injective and exhaustive outside-pair coverage gives

\[
d_{ij}=b_kb_l
\quad\text{for }\{i,j,k,l\}=\{0,1,2,3\}.
\]

Thus

\[
d_{0i}=1,\qquad d_{ij}=3\quad(i,j\in I,\ i\ne j).
\tag{4.2}
\]

Let \(\tau_i\) count triples missing party \(i\). Counting outside occurrences at party \(i\),

\[
\tau_i
=6b_i-b_i\sum_{j\ne i}b_j
=b_i^2,
\]

and therefore

\[
(\tau_0,\tau_1,\tau_2,\tau_3)=(9,1,1,1).
\tag{4.3}
\]

### 4.1 Symbol profiles

For an internal symbol \(a\) at party \(i\), let \(d(a)\) and \(t(a)\) count its maximal double and triple occurrences. Every outside pair involving \(a\) is covered once, giving

\[
2d(a)+t(a)=\sum_{j\ne i}b_j=6-b_i,
\qquad
d(a)+t(a)=6-r_i(a).
\tag{4.4}
\]

At party \(0\), this yields

\[
d(a)=r_0(a)-3,\qquad t(a)=9-2r_0(a).
\]

Nonnegativity forces \(r_0(a)\in\{3,4\}\). Since three such degrees sum to 12,

\[
r_0=(4,4,4),\qquad p_0=(2,2,2),
\tag{4.5}
\]

and each internal party-0 symbol occurs in exactly one maximal double and one maximal triple.

For \(j\in I\), every residual neighbor at party \(0\) lies in its three-symbol alphabet. Thus \(2\le r_j(a)\le3\), and five degrees sum to 12. Therefore each five-symbol party has

\[
r_j=(3,3,2,2,2),\qquad p_j=(3,3,4,4,4).
\tag{4.6}
\]

Write \(H_j\) for its two degree-three symbols and \(L_j\) for its three degree-two symbols. Formula (4.4) gives:

- Each high symbol: two maximal doubles and one maximal triple.
- Each low symbol: one maximal double and three maximal triples.

### 4.2 Outside-pair counts

All outside-containing pair values are maximal, once each:

- \(B_0\times B_j\): three values, for each \(j\in I\).
- \(B_j\times B_k\): one value, for distinct \(j,k\in I\).
- \(A_0\times B_j\): three values.
- \(A_j\times B_0\): fifteen values.
- \(A_j\times B_k\): five values, for distinct \(j,k\in I\).

For each fixed outside party-0 symbol, its six maximal words consist of three doubles—one with the outside symbol at each party in \(I\)—and three triples internal at all three parties in \(I\).

These counts were derived for \(3555\), not transferred from \(4455\).

---

## 5. Canonical low labels from the same maximal support

For each \(i\in I\), let \(D_i\) be the unique maximal double internal at \(0,i\).

By (4.5), the party-0 symbols of the three \(D_i\) are distinct. Label them \(a_1,a_2,a_3\), with \(D_i\) using \(a_i\).

The other maximal occurrence of \(a_i\) is a triple. The double \(D_i\) already uses the outside symbols at the other two parties. Pair injectivity therefore forces that triple to have its outside coordinate at party \(i\). Denote it by \(T_i\).

The missing internal graph

\[
M_{0j}:=(A_0\times A_j)\setminus R_{0j}
\]

has one edge at each \(a_i\), one at each low symbol, and none at a high symbol. Label the lows so that

\[
M_{0j}=\{(a_i,\ell_j^i):i\in I\}.
\tag{5.1}
\]

Thus

\[
R_{0j}
=(A_0\times H_j)
\;\cup\;
\{(a_s,\ell_j^i):s\ne i\}.
\tag{5.2}
\]

The actual maximal words are now constrained as follows:

- \(D_i\) uses \(a_i,\ell_i^i\), and the outside symbols at the other two five-symbol parties.
- \(T_i\) uses \(a_i\), the outside symbol at party \(i\), and \(\ell_j^i,\ell_k^i\) at the other parties.

In particular,

\[
(\ell_j^i,\ell_k^i)\notin R_{jk}
\qquad\text{when }\{i,j,k\}=I.
\tag{5.3}
\]

This is a common-\(P\) obstruction, not a choice of independent pair gauges.

For completeness, every \(M_{jk}\), \(j,k\in I\), has 13 edges, with degree three at low symbols and degree two at high symbols. Its 13 maximal pair incidences come from the one word \(T_i\), three doubles internal at \(j,k\), and nine triples internal at all three five-symbol parties.

---

## 6. Off-label low–low edges force actual twelve-word prisms

Call a residual pair

\[
(\ell_j^s,\ell_k^t)\in R_{jk}
\]

**off-label** when \(s\ne t\).

### Prism lemma

If such an off-label pair exists, and \(l\) is the remaining member of \(I\), then

\[
E\cap\{e_l\in H_l\}=W_l\times H_l,
\tag{6.1}
\]

where \(W_l\) consists of six triples on parties \(0,j,k\), with:

1. Six distinct \(j,k\) pair values.
2. Three \(j\)-symbols and three \(k\)-symbols, each of degree two.
3. A six-cycle as its \(j,k\) bipartite graph.
4. The three party-0 symbols as proper edge colors, each used twice.

In particular, both high symbols at party \(l\) have the **same** three-symbol residual neighborhood at either other five-symbol party.

### Proof

Let \(\{s,t,u\}=I\). An extension of the off-label pair cannot use \(a_s\), by its low symbol at party \(j\), and cannot use \(a_t\), by its low symbol at party \(k\). Its two extensions therefore have the form

\[
(a_u,\ell_j^s,\ell_k^t,x),
\qquad
(a_u,\ell_j^s,\ell_k^t,y),
\quad x\ne y,
\]

with the last displayed coordinate at party \(l\).

In cut \(0j\mid kl\), the row \((a_u,\ell_j^s)\) has columns \((\ell_k^t,x)\) and \((\ell_k^t,y)\). Full \(2\times2\) closure gives a second row sharing both columns.

That row cannot have first coordinate \(a_u\), because the pair \((a_u,\ell_k^t)\) already has both its extensions. It cannot have first coordinate \(a_t\), by (5.1). Hence its first coordinate is \(a_s\).

The analogous argument in cut \(0k\mid jl\) supplies words with first coordinate \(a_t\), at both \(x,y\).

Thus each of \(x,y\) has all three \(a\)-symbols as residual neighbors. They are precisely the two high symbols \(H_l\).

For each \(a_i\), the two rows \((a_i,x),(a_i,y)\) in cut \(0l\mid jk\) share a column. They therefore share both columns. This gives two \(j,k\) values for each \(a_i\), duplicated at \(x,y\): twelve words.

Those six \(j,k\) values are distinct; otherwise one \(j,k\) pair would have at least four extensions. Similarly, two edges of the same first-coordinate color cannot meet at a \(j\)- or \(k\)-symbol, because that would give four extensions of a \(0j\) or \(0k\) pair.

Each high symbol at party \(l\) has six residual words, so the twelve displayed words exhaust all words using \(H_l\). Every \(j\)-symbol appearing among them therefore has degree two in \(W_l\), because its pair with \(x\) has exactly two extensions. The same holds at party \(k\).

Thus \(W_l\) has three vertices on each side and is a simple two-regular bipartite graph: necessarily a six-cycle. This proves the lemma.

Any prisms derived from different off-label edges in the same pair system coincide: each equals the same set \(E\cap\{e_l\in H_l\}\).

---

## 7. Consequences of a prism

Fix a prism \(W_l\times H_l\), and let \(V_j,V_k\) be its three-symbol vertex sets at parties \(j,k\).

Each symbol in \(V_j\) occurs in four prism words; symbols outside \(V_j\) occur in none. Consequently:

- A low symbol in \(V_j\) has no residual occurrences outside the prism.
- A high symbol in \(V_j\) has two occurrences outside it.
- A low outside \(V_j\) has four occurrences outside it.
- A high outside \(V_j\) has six occurrences outside it.

Also

\[
R_{jl}\cap(A_j\times H_l)=V_j\times H_l.
\tag{7.1}
\]

Since \(|V_j|=|L_j|=3\),

\[
|L_j\setminus V_j|=|H_j\cap V_j|.
\tag{7.2}
\]

If \(V_j\) contains a high symbol, some low symbol lies outside \(V_j\). That low has no neighbor in \(H_l\), and hence has two distinct low neighbors at party \(l\). At least one has a different label.

Therefore:

> If a prism at \(H_l\) contains a high symbol at party \(j\), an off-label edge exists between parties \(j,l\).
> \(\tag{7.3}\)

A second useful capacity fact is:

> If \(V_j=L_j\), then \(V_k\) contains both high symbols.

Indeed, the twelve words outside the prism use only \(H_j\) at party \(j\). A high symbol at party \(k\) outside \(V_k\) would have six words there and would require three distinct residual \(j\)-neighbors, impossible among only two symbols.

---

## 8. Nonempty off-label interaction graphs are impossible

Let \(G\) be the graph on \(I\), with edge \(jk\) exactly when an off-label residual low–low pair exists between those physical parties.

### 8.1 Exactly one edge is impossible

Suppose \(jk\) is its only edge. It produces a prism at \(H_l\).

By (7.3), neither \(V_j\) nor \(V_k\) can contain a high symbol. Thus \(V_j=L_j\) and \(V_k=L_k\).

The twelve words outside the prism use only \(H_j\times H_k\) in that pair system. None of those pairs occurs inside the prism, and every residual pair has exactly two extensions. Those twelve words therefore require six distinct \(j,k\) pair values, but

\[
|H_j\times H_k|=4.
\]

Contradiction.

### 8.2 Exactly two edges are impossible

Suppose the edges are \(jk,jl\), but not \(kl\). There are prisms at \(H_l\) and \(H_k\).

In the prism at \(H_l\), (7.3) and the absence of edge \(kl\) force \(V_k=L_k\). The capacity fact then forces

\[
V_j=H_j\cup\{\text{one low symbol}\}.
\]

Consider the twelve words outside this prism. Their \(j,k\) incidence degrees are:

- Each of the two outside low symbols at \(j\): degree two into \(H_k\).
- Each high symbol at \(j\): degree one into \(H_k\).
- Each high symbol at \(k\): degree three at party \(j\).

Thus each high symbol at \(k\) sees both outside low symbols at \(j\), and one high symbol at \(j\). The two high symbols at \(k\) see different high symbols at \(j\): the high–high subgraph is a two-edge perfect matching.

But the prism at \(H_k\) requires both high symbols at \(k\) to have identical full \(j\)-neighborhoods, by (7.1). Contradiction.

### 8.3 Three edges are impossible

Now suppose \(G\) is complete, so prisms exist at all three high alphabets.

For every pair \(j,k\), the prism at \(H_j\) gives identical neighborhoods for the two high \(j\)-symbols, while the prism at \(H_k\) gives identical neighborhoods for the two high \(k\)-symbols. Therefore the \(2\times2\) high–high incidence matrix has identical rows and identical columns. It is either empty or complete.

#### No high–high block can be empty

Suppose the block between \(H_j,H_l\) is empty.

In the prism at \(H_l\), this means \(V_j=L_j\). The capacity fact gives \(V_k=H_k\cup\{\text{one low}\}\).

Outside the prism:

- Each high \(j\)-symbol has six words.
- Each high \(k\)-symbol has two words.
- Each of the two outside low \(k\)-symbols has four words.

The outside low \(k\)-symbols each meet both high \(j\)-symbols. Each high \(k\)-symbol meets one high \(j\)-symbol, and the two choices must differ. Thus the high–high graph between \(j,k\) is exactly a two-edge matching.

That contradicts its being empty or complete.

Hence every high–high block is complete.

#### Complete high–high blocks give an impossible binary support

In the prism at \(H_l\), both vertex sets consequently consist of two highs and one low:

\[
V_j=H_j\cup\{x_j\},\qquad V_k=H_k\cup\{x_k\}.
\]

The off-label edge generating this prism joins its unique low vertices \(x_j,x_k\). In its six-cycle, each low vertex has degree two and their common edge is counted twice when subtracting their incidences. Thus the number of high–high edges in \(W_l\) is

\[
6-2-2+1=3.
\]

The residual words high at all three five-symbol parties therefore give a set

\[
T\subset H_1\times H_2\times H_3
\]

of exactly six distinct triples. Distinctness follows from the injective \(j,k\) projection of \(W_l\).

Each prism shows that the corresponding pair projection of \(T\) has exactly three values. Thus all three pair projections of \(T\) have size three.

But a six-element subset of a \(2\times2\times2\) box cannot have two, let alone three, nonfull pair projections. If its \(j,k\) projection omits a pair, the two omitted triples are exactly that pair times both \(l\)-values. The other two pair projections are then full.

Contradiction.

This exhausts every nonempty graph \(G\).

---

## 9. The zero-off-label case is also impossible

It remains to exclude \(G=\varnothing\).

Every residual word containing multiple low symbols must then use the same low label at those coordinates. A word with three lows would have a common label \(i\), but its pair at the other two parties is forbidden by \(T_i\), equation (5.3). Thus every residual word has at most two lows.

Let \(N_t\) count residual words with exactly \(t\) low coordinates among the three five-symbol parties.

There are 36 low-coordinate incidences: three parties, three low symbols each, four words per low. Hence

\[
N_1+2N_2=36,\qquad N_0+N_1+N_2=24,
\]

and therefore

\[
N_2=12+N_0.
\tag{9.1}
\]

Let \(m\) be the total number of residual low–low pair values over the three pair systems. Every two-low word contributes exactly one such pair, and every such pair has two extensions, so

\[
N_2=2m.
\]

For each pair of five-symbol parties, only equal-label low pairs are possible, and (5.3) forbids one of those three. Therefore \(m\le6\). Equation (9.1) now forces

\[
N_0=0,\quad N_1=N_2=12,\quad m=6.
\tag{9.2}
\]

Every allowable equal-label low–low pair is present. For each label \(i\), they form the two-edge star centered at \(\ell_i^i\).

### 9.1 All residual words pair in the party-0 coordinate

Fix \(i\), with \(\{i,j,k\}=I\).

The four residual words using the center low \(\ell_i^i\) have neighbor sets

\[
\{\ell_j^i,h_j\},\qquad \{\ell_k^i,h_k\},
\]

for some highs \(h_j\in H_j,h_k\in H_k\).

The pair \((\ell_j^i,\ell_k^i)\) is forbidden by (5.3). Each of the two symbols in either neighbor set must occur twice. Therefore the four words use exactly the two cross pairs

\[
(\ell_j^i,h_k),\qquad(h_j,\ell_k^i),
\]

twice each.

Their first coordinate can only be \(A_0\setminus\{a_i\}\). Since the four tensor words are distinct, each cross pair occurs once at each of those two first-coordinate values.

Now consider the peripheral low \(\ell_j^i\). Its two words with the center low have already exhausted the residual pair \((\ell_j^i,h_k)\). Its other two words must use the other high symbol \(\bar h_k\) at party \(k\), and its unique high neighbor at party \(i\). The pair counts with party \(0\) force one such word at each value in \(A_0\setminus\{a_i\}\).

The same argument applies to \(\ell_k^i\).

Thus all words of low label \(i\) factor as

\[
(A_0\setminus\{a_i\})\times F_i,
\]

where \(F_i\) contains four distinct triples on the five-symbol parties. Each has at least one low, all of label \(i\). Consequently

\[
E=\bigsqcup_{i\in I}
(A_0\setminus\{a_i\})\times F_i.
\tag{9.3}
\]

This pairing is derived, not assumed. In particular, distance-one pairs are allowed and explicitly occur in this hypothetical support.

### 9.2 A forbidden three-row six-cycle

Fix any party \(j\in I\) and any high symbol \(h\in H_j\).

Let \(f_i\) be the number of triples in \(F_i\) having value \(h\) at party \(j\). Each pair \((a_s,h)\) has exactly two extensions. Equation (9.3) gives

\[
\sum_{i\ne s}f_i=2
\qquad(s\in I).
\]

Subtracting these equations shows that all \(f_i\) are equal, and hence

\[
f_1=f_2=f_3=1.
\]

Let \(c_i\) be the other-party pair in the unique such triple of \(F_i\). The three \(c_i\) are distinct: each contains a low symbol of label \(i\), and no triple here contains mixed low labels.

In flattening \(0j\mid kl\), the three rows \((a_s,h)\) and the three columns \(c_i\) therefore have nonzero pattern

\[
(a_s,h)\text{ meets }c_i
\quad\Longleftrightarrow\quad s\ne i.
\]

Each row has exactly these two nonzeros. Two distinct rows share exactly one column, so their inner product is one nonzero complex product. It cannot vanish.

This contradicts unitarity and excludes \(G=\varnothing\).

Together with Section 8, all possibilities are exhausted. The proposed theorem follows.

---

## 10. Complex phases and exact admissibility boundary

The argument does not assume equal residual moduli, real entries, or independently selectable phases in different cuts.

For any surviving support, each full residual block would have to satisfy, for the same tensor amplitudes,

\[
B=\begin{pmatrix}x&y\\z&w\end{pmatrix},\qquad
|x|^2=|w|^2=s,\quad
|y|^2=|z|^2=1-s,\quad 0<s<1,
\]

and

\[
x\overline z+y\overline w=0.
\]

Equivalently, its phase relation is

\[
\arg x+\arg w-\arg y-\arg z\equiv\pi\pmod{2\pi}.
\]

There are six blocks in each of three cuts, but they share the same 24 residual complex variables. They are not three independently phase-gauged constructions.

The proof excludes the support before a simultaneous phase assignment can succeed:

- The zero-off-label branch forces a single-overlap row inner product.
- Nonzero off-label branches force incompatible actual common-support prisms.

Arbitrary complex phases cannot repair either obstruction.

A potentially misleading shortcut is specifically avoided: unused pairs in a local four-word projection need not all be globally missing pairs. No step above identifies those two notions.

## 11. Remaining obligations and original-target ceiling

**Proposed mathematical scope:** the whole actual support-48, exact-\(t=24\), residual-\(3555\) branch. No additional no-OLS, no-distance-one, equal-modulus, or selected graph-shape assumption is used.

**Acceptance still unpaid:** independent written reconstruction of every lemma and case, followed by parent disposition. This is an unreviewed author candidate, not an accepted theorem. No finite-run corroboration, human review, independent-family review, formal/kernel certification, novelty, or worldwide-priority claim is made.

**Not established here:**

- Exclusion or feasibility of other residual-alphabet branches.
- Exclusion of the exact-\(t=28\) branch.
- A full support-48 no-go.
- A product-basis lower bound of 49.
- An exact AME(4,6) support minimum or a physical witness.
- Any exhaustive statement that a previously listed set of alphabet profiles covers all remaining possibilities.

No mathematical step is intentionally deferred inside the stated \(3555\) proof candidate. Its correctness remains subject to disjoint review; the broader original AME minimum problem remains unresolved by this return.