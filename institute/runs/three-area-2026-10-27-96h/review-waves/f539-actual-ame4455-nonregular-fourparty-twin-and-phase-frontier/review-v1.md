# author-candidate-v1.md

## F539 — Actual AME4455: twin saturation, exact six-projection rounding, and a direct common-\(P\) contradiction

**Role:** GENERALAUTHOR  
**Status:** **COMPLETE WRITTEN AUTHOR CANDIDATE — UNREVIEWED, NOT ADOPTED.**  
**Scientific code prepared or executed:** **NONE / NOT RUN.**  
**Delivery:** Complete body returned for Main materialization; no working-tree write attempted.

## 1. Main result and exact scope

### Theorem — Whole actual \(4455\) exclusion

There is no tensor
\[
U=6\psi\in(\mathbb C^6)^{\otimes4}
\]
such that:

1. its three balanced flattenings
   \[
   U^{12\mid34},\qquad U^{13\mid24},\qquad U^{14\mid23}
   \]
   are unitary;
2. \(U\) has exactly \(48\) nonzero entries;
3. exactly \(24\) entries have modulus one;
4. the residual coordinate-alphabet sizes are
   \[
   (q_1,q_2,q_3,q_4)=(4,4,5,5).
   \]

The proof allows arbitrary nonzero complex residual amplitudes. It does **not** assume no-distance-one, no-OLS, equal residual moduli, real signs, separately chosen pair graphs, or separately chosen maximal supports.

The new argument has two endpoints:

- an exact, common-\(P,E\) rounding construction producing an \(\operatorname{OA}(36,4,6,2)\), with all six physical pair projections explicitly checked;
- a **direct contradiction inside the same maximal set \(P\)**, which makes an external no-OLS theorem unnecessary for the primary exclusion.

This is a candidate exclusion of the **entire actual \(4455\) stratum**, including its nonregular profiles and both maximal-word regimes. It is **not** a universal support-\(48\) exclusion, an \(N\ge49\) theorem, or an exact global AME support minimum.

---

## 2. The actual common-\(P,E\) interface

Define
\[
P=\{w:|U_w|=1\},\qquad
E=\{w:0<|U_w|<1\}.
\]
Then
\[
|P|=|E|=24.
\]

Let
\[
A_i=\pi_i(E),\qquad |A_i|=q_i,
\]
and let
\[
O_i=[6]\setminus A_i.
\]

A modulus-one entry exhausts its row and column in every unitary flattening. Removing the \(24\) maximal rows and columns therefore leaves a \(12\times12\) residual unitary with \(24\) nonzero entries.

Every residual row and column has at least two nonzeros: a singleton would itself have modulus one. Hence every residual row and column has exactly two nonzeros.

Consequently, for every physical pair \(ij\),
\[
R_{ij}:=\pi_{ij}(E)
\]
has \(12\) elements, each with exactly two \(E\)-extensions, and
\[
\pi_{ij}(P)=[6]^2\setminus R_{ij}
\tag{2.1}
\]
injectively.

These are six projections of the **same** sets \(P,E\).

For \(a\in A_i\), let
\[
p_i(a)=|\{w\in P:w_i=a\}|.
\]
The residual degree, independent of the partner party, is
\[
r_i(a)=6-p_i(a).
\tag{2.2}
\]
The slice through \(a\) contains \(2r_i(a)\) residual words, and
\[
\sum_{a\in A_i}r_i(a)=12.
\tag{2.3}
\]

Also
\[
r_i(a)\ge2.
\tag{2.4}
\]
Indeed, degree one would make the two residual words through \(a\) use the same unique neighbor at every other coordinate, so they would coincide.

### Actual block closure

Two residual rows sharing a column cannot have only that overlap, because their inner product would be nonzero. Their other nonzero columns must also agree.

Thus every residual flattening is a disjoint union of six full nonzero \(2\times2\) unitary blocks.

All block-closure arguments below refer to these actual blocks.

---

## 3. Degree bounds and the unique-exception restriction

The needed degree classification follows from the same maximal set \(P\).

For \(w\in P\), let \(k(w)\) be its number of internal coordinates, and let \(n_s\) count words with \(k(w)=s\).

Counting internal positions gives
\[
\sum_{w\in P}k(w)
=\sum_i(6q_i-12)
=60.
\]
Counting internal pairs gives
\[
\sum_{w\in P}\binom{k(w)}2
=\sum_{i<j}(q_iq_j-12)
=49.
\]
Therefore
\[
3n_0+n_1+n_4
=49-2(60)+3(24)
=1.
\tag{3.1}
\]

In particular, there is at most one maximal word with exactly one internal position.

Fix an internal symbol \(a\) at party \(i\). Let:

- \(\sigma(a)\) count its maximal one-internal words;
- \(\tau(a)\) count its maximal three-internal words;
- \(f(a)\) count its maximal four-internal words.

Counting other internal coordinates among its \(6-r_i(a)\) maximal words gives
\[
\sum_{j\ne i}q_j-3r_i(a)
=(6-r_i(a))-\sigma(a)+\tau(a)+2f(a).
\]

For a four-symbol party this becomes
\[
\tau(a)+2f(a)-\sigma(a)=8-2r_i(a),
\tag{3.2}
\]
and for a five-symbol party,
\[
\tau(a)+2f(a)-\sigma(a)=7-2r_i(a).
\tag{3.3}
\]

Since \(\sigma(a)\le1\), all residual degrees are at most four.

Together with (2.3)–(2.4), the four-symbol profiles are exactly among
\[
D_0=(3,3,3,3),\qquad
D_1=(4,3,3,2),\qquad
D_2=(4,4,2,2).
\tag{3.4}
\]

A five-symbol party has either
\[
(3,3,2,2,2)
\tag{3.5}
\]
or
\[
(4,2,2,2,2).
\tag{3.6}
\]
In the second case, its degree-four symbol requires \(\sigma(a)=1\) in (3.3). Thus **at most one five-symbol party can have profile (3.6)**.

Call degree-two symbols **low**, and the other residual symbols **high**.

---

## 4. Twin saturation: partial overlaps cannot occur

### Lemma 1 — Full-slice twin saturation

If two residual words differ only at coordinate \(i\), using distinct symbols \(a,a'\), then
\[
r_i(a)=r_i(a')\in\{3,4\},
\]
and their entire other-coordinate slices coincide:
\[
V_a=V_{a'},
\qquad
V_a:=\{v:(a,v)\in E\}.
\tag{4.1}
\]

Call such a pair a **twin pair**.

### Proof

Set
\[
T=V_a\cap V_{a'}\ne\varnothing.
\]

For each other coordinate \(j\), the two residual extensions of a used pair \((a,x_j)\) form a pair in \(V_a\). Actual block closure in the cut \(ij\mid kl\) shows that if one member belongs to \(T\), then its partner also belongs to \(T\).

Thus equality at each of the other three coordinates supplies a perfect matching on \(T\).

Two vertices of \(T\) cannot share two of those coordinates: their copies at both \(a,a'\) would give four extensions of a physical pair. Hence the three matchings form a **simple cubic graph**.

For \(v\in T\), put
\[
z_v=U_{a,v}\overline{U_{a',v}}\ne0.
\]
Across every matching edge \(vv'\), actual row orthogonality gives
\[
z_v+z_{v'}=0.
\tag{4.2}
\]
The graph has no odd cycle and is bipartite. A nonempty simple cubic bipartite graph has at least six vertices.

All slices have at most eight words. Therefore
\[
|T|\in\{6,8\}.
\]

Every coordinate value occurs in \(T\) either zero or two times, because \(T\) is closed under the corresponding matching.

If an eight-word slice had a six-word overlap \(T\), its two remaining triples would have to agree at each of their three coordinates: at every coordinate, those two remaining occurrences must form the unused pair. They would be duplicate triples, impossible.

Thus an eight-word slice cannot have a six-word overlap. A four-word slice cannot contain \(T\). The only possibilities are
\[
|V_a|=|V_{a'}|=|T|\in\{6,8\},
\]
proving the lemma. ∎

### Consequences

1. A distance-one pair cannot vary through a low symbol.
2. Twin pairs are disjoint pairs of symbols. Three symbols with the same nonempty slice would already give at least three extensions of a physical pair.
3. A twin pair of degree \(r\) occupies all \(4r\) words through its two symbols.

### Lemma 2 — Twin components at different coordinates are disjoint

A residual word cannot belong to twin pairs at two different coordinates.

Indeed, that word and its two single-coordinate flips would be three distinct extensions of the physical pair on the other two coordinates, contradicting multiplicity two.

Therefore the complete word sets occupied by twin pairs at different coordinates are disjoint. ∎

---

## 5. A uniform complex obstruction for low-to-low pairs

### Lemma 3 — A low-to-low pair must extend by a single-coordinate twin

Suppose a physical pair consists of two low symbols and lies in a residual projection. Its two residual extensions differ at **exactly one** of the two complementary coordinates.

Consequently, those extensions belong to a full twin pair at that complementary coordinate.

### Proof

The extensions cannot coincide. Suppose they differ at both complementary coordinates.

Relabel the low coordinates as parties \(3,4\), and normalize the two extensions to
\[
0000,\qquad1100.
\]

The four words through the low party-\(3\) symbol induce three balanced partitions at parties \(1,2,4\).

Because the two words through the fixed low party-\(4\) symbol differ at both parties \(1,2\), the partitions are either:

- all distinct; or
- equal at parties \(1,2\), with a different party-\(4\) partition.

The second alternative would give a distance-one pair varying through the low party-\(4\) symbol, contrary to Lemma 1. Hence all three partitions differ.

The same applies to the low party-\(4\) slice.

The two slices therefore force
\[
0000,\ 1100,\ 0101,\ 1001,\ 0110,\ 1010.
\]
Actual block closure in \(13\mid24\) forces the remaining words
\[
1111,\qquad0011.
\]
Thus all eight even-parity binary words occur.

These eight words already exhaust the two extensions of each physical pair they use, so the following are genuine closed blocks:

\[
\begin{array}{c|c}
\text{physical cut}&\text{block}\\ \hline
12\mid34&
\begin{pmatrix}
U_{0000}&U_{0011}\\
U_{1100}&U_{1111}
\end{pmatrix}\\[3mm]
13\mid24&
\begin{pmatrix}
U_{0000}&U_{0101}\\
U_{1010}&U_{1111}
\end{pmatrix}\\[3mm]
14\mid23&
\begin{pmatrix}
U_{0011}&U_{0101}\\
U_{1010}&U_{1100}
\end{pmatrix}
\end{array}
\]

Write their phases as \(\theta_w\), and define
\[
X=\theta_{0000}+\theta_{1111},\qquad
Y=\theta_{0011}+\theta_{1100},\qquad
Z=\theta_{0101}+\theta_{1010}.
\]

A full nonzero unitary block
\[
\begin{pmatrix}u&v\\w&x\end{pmatrix}
\]
requires
\[
\arg u-\arg v-\arg w+\arg x\equiv\pi\pmod{2\pi}.
\]
The three displayed blocks give
\[
X-Y\equiv\pi,\qquad
X-Z\equiv\pi,\qquad
Y-Z\equiv\pi
\pmod{2\pi}.
\tag{5.1}
\]
The first minus the second plus the third has zero left side and right side \(\pi\), a contradiction.

This is an arbitrary-complex phase contradiction, not a real-sign diagnostic. Therefore the two original extensions differ at just one complementary coordinate. Lemma 1 supplies the full twin pair there. ∎

---

## 6. No twin pair can occur at either four-symbol party

### Lemma 4 — Four-party twin isolation

If a twin pair occurs at a four-symbol party \(i\), no twin pair can occur at another coordinate.

### Proof

The twin component exhausts all words through its two symbols. By Lemma 2, any other-coordinate twin component must avoid those symbols.

But such a component has degree at least three, so it requires at least three distinct neighbors at party \(i\). Only two symbols of \(A_i\) remain. Contradiction. ∎

There also cannot be two twin pairs at that same four-symbol party. Two such pairs must both have degree three, since their degrees sum to twelve. At either five-symbol party, its neighbors at party \(i\) would then be unions of the two twin pairs, giving every residual symbol degree two or four. Five such degrees summing to twelve force
\[
(4,2,2,2,2)
\]
at **both** five-symbol parties, contrary to Section 3.

Hence, if any four-party twin exists, it is the **only twin pair in the entire tensor**.

### Lemma 5 — Degree-four four-party twins are impossible

Suppose a four-symbol party \(i\) has degree-four twins \(a,a'\).

The other two symbols of \(A_i\) both have degree two.

At either five-symbol party, the twins have a common four-element neighbor set. Its omitted residual symbol \(\ell\) can be adjacent only to the other two party-\(i\) symbols. Thus \(\ell\) has degree two and is adjacent to both.

This supplies a low-to-low edge between party \(i\) and that five-symbol party. Lemma 3 requires a twin pair at one of the complementary coordinates. Lemma 4 forbids it. ∎

### Lemma 6 — Degree-three four-party twins are impossible

Suppose a four-symbol party \(i\) has degree-three twins \(a,a'\). Write its remaining symbols as \(u,v\).

At the other four-symbol party \(j\), the twins have three common neighbors and omit a unique residual symbol \(b\). The symbol \(b\) is adjacent only to \(u,v\), hence has degree two and is adjacent to both.

At each five-symbol party, the twins omit two residual symbols. Each omitted symbol is low and is adjacent to both \(u,v\).

The low symbol \(b\) cannot be adjacent to any low symbol at either five-symbol party. Otherwise Lemma 3 would require:

- a twin at the remaining five-symbol party, forbidden by Lemma 4; or
- the unique twin pair \(a,a'\) at party \(i\), impossible because \(b\) is adjacent to neither.

Therefore \(b\) has two high neighbors at each five-symbol party. Both five-symbol parties must be ordinary, each with exactly two high symbols.

Each of \(u,v\) already has the two omitted low neighbors at each five-symbol party.

Since \((u,b)\) and \((v,b)\) are residual pairs, their extensions must use high symbols at both five-symbol parties. Thus
\[
r_i(u),r_i(v)\ge3.
\]
Their degrees sum to six, so both equal three.

Each consequently has only one possible high neighbor at each five-symbol party. For a fixed pair \((u,b)\), both residual extensions would therefore have the same two remaining coordinates. They would coincide, contradicting exact multiplicity two. ∎

### Conclusion

There is **no residual distance-one pair varying at party \(1\) or party \(2\)**, for any of the profiles \(D_0,D_1,D_2\).

This prohibition has been derived from the actual tensor. It is not an added no-distance-one premise.

---

## 7. Forced five-party graph and forced nonregular four-party profiles

A low-to-low edge in \(R_{34}\) would, by Lemma 3, require twins at party \(1\) or \(2\). Therefore
\[
R_{34}\cap(L_3\times L_4)=\varnothing.
\tag{7.1}
\]

An exceptional five-symbol party has only one high symbol. A low symbol at the opposite party needs two distinct neighbors, and (7.1) would require both to be high. This is impossible.

Thus both five-symbol parties have profile
\[
(3,3,2,2,2).
\]
Every low symbol uses both high symbols at the other party. Those edges exhaust the high degrees, giving
\[
R_{34}
=(L_3\times H_4)\ \sqcup\ (H_3\times L_4).
\tag{7.2}
\]

Fix \(i\in\{1,2\}\) and \(a\in A_i\). Define
\[
x_i(a)=|N_{i3}(a)\cap L_3|,\qquad
y_i(a)=|N_{i3}(a)\cap H_3|.
\]
Counting the same residual words through the two sectors of (7.2) gives
\[
x_i(a)=|N_{i4}(a)\cap H_4|,
\qquad
y_i(a)=|N_{i4}(a)\cap L_4|,
\tag{7.3}
\]
and
\[
r_i(a)=x_i(a)+y_i(a).
\tag{7.4}
\]

Consider a low party-\(3\) slice. Its partitions at parties \(1,2,4\) cannot have equality \(1=4\) or \(2=4\), because those alternatives give a distance-one pair varying at a four-symbol party.

The remaining possibilities are:

- all three partitions distinct;
- the party-\(1\) and party-\(2\) partitions equal, with a different party-\(4\) partition.

In either case, every party-\(i\) neighbor in that slice occurs with **both** party-\(4\) neighbors, namely both elements of \(H_4\).

Therefore
\[
x_i(a)>0\quad\Longrightarrow\quad x_i(a)=2.
\]
The symmetric low party-\(4\) argument gives
\[
y_i(a)>0\quad\Longrightarrow\quad y_i(a)=2.
\]
Hence
\[
x_i(a),y_i(a)\in\{0,2\}.
\tag{7.5}
\]

Moreover,
\[
\sum_{a\in A_i}x_i(a)=6,\qquad
\sum_{a\in A_i}y_i(a)=6.
\]
Each function is therefore two on three symbols and zero on one. Their zero symbols must differ, since otherwise (7.4) would give residual degree zero.

Write these two symbols as
\[
a_i^X:\ (x_i,y_i)=(2,0),\qquad
a_i^Y:\ (x_i,y_i)=(0,2).
\tag{7.6}
\]
The remaining two symbols have \((x_i,y_i)=(2,2)\).

Thus **both four-symbol parties are forced to have profile**
\[
(4,4,2,2).
\tag{7.7}
\]

In particular, all profile pairs containing \(D_0\) or \(D_1\) have already been excluded, without any external no-OLS theorem.

The neighborhoods of the five-party high symbols are now
\[
N_{i3}(h)=A_i\setminus\{a_i^X\}
\quad(h\in H_3),
\tag{7.8}
\]
and
\[
N_{i4}(k)=A_i\setminus\{a_i^Y\}
\quad(k\in H_4).
\tag{7.9}
\]
The omitted symbols \(a_i^X,a_i^Y\) are distinct.

---

## 8. Both five-party high pairs are forced twins

This section supplies the exact common-\(P,E\) rounding requested in the parent instruction.

The symbol \(a_1^Y\) is low and has two low party-\(4\) neighbors by (7.3), (7.6). Choose one, \(\ell_4\).

The residual pair \((a_1^Y,\ell_4)\) is low-to-low. Lemma 3 says its two extensions differ at party \(2\) or \(3\). They cannot differ at party \(2\). Thus they differ at party \(3\), between the two high symbols in \(H_3\).

Lemma 1 makes those two degree-three high symbols full twins.

Similarly, \(a_1^X\) has two low party-\(3\) neighbors. Applying Lemma 3 to one of those low-to-low pairs forces the two high symbols in \(H_4\) to be full twins.

Consequently,
\[
E=C_3\ \sqcup\ C_4,
\tag{8.1}
\]
where
\[
C_3=\{w\in E:w_3\in H_3\},
\qquad
C_4=\{w\in E:w_4\in H_4\}.
\]
Each component has twelve words. Equation (7.2) makes them disjoint and shows they cover \(E\).

For \(C_3\), the common slice of its two high symbols is a six-element set
\[
T_3\subseteq A_1\times A_2\times L_4.
\]
Its equality matchings form a simple cubic bipartite graph on six vertices, hence \(K_{3,3}\).

Similarly,
\[
T_4\subseteq A_1\times A_2\times L_3
\]
is the common six-element slice of the high party-\(4\) twins, with its own \(K_{3,3}\).

Within either \(T_i\), every coordinate value occurs twice, and projection onto any two of its three coordinates is injective. Otherwise the two twin copies of two triples would give four extensions of a physical pair.

These are slices of the actual \(E\), not independently selected fixtures.

---

## 9. Exact same-\(P,E\) rounding, including all six physical pair consumers

Label the two high symbols of party \(3\) as \(h_0,h_1\). Choose a bipartition
\[
\varepsilon_3:T_3\longrightarrow\{0,1\}
\]
of its \(K_{3,3}\), and retain the six words
\[
F_3=
\{\operatorname{ins}_3(h_{\varepsilon_3(v)},v):v\in T_3\}.
\tag{9.1}
\]

Here \(\operatorname{ins}_i\) inserts the indicated symbol at its actual coordinate \(i\).

Likewise, label \(H_4=\{k_0,k_1\}\), choose a bipartition \(\varepsilon_4\) of the graph on \(T_4\), and set
\[
F_4=
\{\operatorname{ins}_4(k_{\varepsilon_4(v)},v):v\in T_4\}.
\tag{9.2}
\]

No amplitude or phase is altered. This is a selection of words from the actual support.

### Pair-projection rule

For either component:

- **A physical pair not containing the twin coordinate:** injectivity of the corresponding two-coordinate projection of \(T_i\) gives one triple. The rounding retains exactly one of its two twin copies.
- **A physical pair containing the twin coordinate and coordinate \(j\):** the two triples with a fixed \(j\)-value form a matching edge. Its endpoints lie in opposite bipartition classes, so the rounding selects each twin symbol exactly once.

Thus every used physical pair has multiplicity one after rounding, with its projection support unchanged.

### Explicit dispatch to all six physical pairs

| Physical pair | \(C_3\to F_3\) | \(C_4\to F_4\) |
|---|---|---|
| \(12\) | Injective \(T_3\) projection onto \(12\) | Injective \(T_4\) projection onto \(12\) |
| \(13\) | Party-\(1\) matching edge selects each party-\(3\) twin once | Injective \(T_4\) projection onto \(13\) |
| \(14\) | Injective \(T_3\) projection onto \(14\) | Party-\(1\) matching edge selects each party-\(4\) twin once |
| \(23\) | Party-\(2\) matching edge selects each party-\(3\) twin once | Injective \(T_4\) projection onto \(23\) |
| \(24\) | Injective \(T_3\) projection onto \(24\) | Party-\(2\) matching edge selects each party-\(4\) twin once |
| \(34\) | Party-\(4\) matching edge selects each party-\(3\) twin once | Party-\(3\) matching edge selects each party-\(4\) twin once |

Each used pair already has multiplicity two within its original component. Therefore \(C_3,C_4\) cannot share a projected physical pair: that would give at least four extensions in \(E\).

It follows that
\[
F:=F_3\sqcup F_4
\]
has twelve words and projects bijectively onto \(R_{ij}\) for **every** physical pair \(ij\).

By (2.1),
\[
Q:=P\sqcup F
\tag{9.3}
\]
has \(36\) words and projects bijectively onto \([6]^2\) at all six physical pairs.

Thus
\[
Q\text{ is an }\operatorname{OA}(36,4,6,2).
\tag{9.4}
\]

For completeness, using the \(12\)-projection as row and column coordinates, the third and fourth coordinates define two Latin squares:

- \(13,23\) bijectivity gives the row and column Latin properties of the third coordinate;
- \(14,24\) bijectivity gives those of the fourth coordinate;
- \(34\) bijectivity gives their orthogonality.

This establishes the tensor-to-OA reduction without assuming an external no-OLS theorem.

---

## 10. Direct common-\(P\) closure: no external theorem is needed

The following contradiction closes the remaining \((D_2,D_2)\) case directly.

Fix party \(1\), and abbreviate
\[
a_X=a_1^X,\qquad a_Y=a_1^Y.
\]
They are distinct.

Because \(q_1=4\), the outside set \(O_1\) has two symbols. Because \(q_4=5\), write
\[
O_4=\{o_4\}.
\]

From (7.8), for every \(h\in H_3\), its maximal party-\(1\) partners are exactly
\[
O_1\cup\{a_X\}.
\tag{10.1}
\]
From (7.9), for every \(k\in H_4\), its maximal party-\(1\) partners are exactly
\[
O_1\cup\{a_Y\}.
\tag{10.2}
\]

Therefore every maximal word whose party-\(3,4\) symbols lie in \(H_3\times H_4\) has its party-\(1\) symbol in
\[
\bigl(O_1\cup\{a_X\}\bigr)
\cap
\bigl(O_1\cup\{a_Y\}\bigr)
=O_1.
\tag{10.3}
\]

Now fix \(h\in H_3\).

Its residual degree is three, so it belongs to exactly three maximal words. Their party-\(1\) symbols cover the three values in (10.1) injectively.

Its residual party-\(4\) neighbors are exactly \(L_4\), by (7.2). Its maximal party-\(4\) partners are consequently
\[
H_4\cup\{o_4\}.
\tag{10.4}
\]

Two of its three maximal words use the two distinct symbols of \(H_4\). By (10.3), their party-\(1\) symbols lie in \(O_1\). Pair injectivity at \(13\) makes those symbols distinct, so they exhaust \(O_1\).

Its remaining maximal word must therefore contain
\[
w_1=a_X,\qquad w_4=o_4.
\tag{10.5}
\]

There are two distinct symbols \(h\in H_3\). Applying the same argument to both gives two distinct maximal words with the **same physical \(14\)-pair**
\[
(a_X,o_4).
\]
This contradicts injectivity of \(\pi_{14}(P)\).

Hence no actual tensor satisfying the hypotheses exists. ∎

### Why this closes the actual caller

The final contradiction uses:

- neighborhoods derived from the same \(E\);
- maximal complements supplied by the same \(P\);
- injectivity of the actual maximal \(13\)- and \(14\)-projections.

It does not replace simultaneous tensor compatibility by separate graph feasibility. It does not require an independent gauge choice, a modulus assignment, an OLS assumption, or an external classification.

---

## 11. Separate external classical import: optional alternative, not a primary premise

The classical Euler–Tarry theorem states that no pair of orthogonal Latin squares of order six exists, equivalently no \(\operatorname{OA}(36,4,6,2)\) exists.

A publicly accessible primary research source proving this classical statement is:

Dieter Betten, **“A direct proof of the non-existence of a MOL(6)”**, *Journal of Geometry* **114**, article 8 (2023), particularly its case division and Theorems 4, 5, 7–8:  
https://doi.org/10.1007/s00022-023-00669-3

If explicitly imported, that theorem supplies an alternative contradiction immediately after (9.4).

However:

- the new tensor-to-OA argument in Section 9 does not assume it;
- the primary whole-\(4455\) proof closes independently in Section 10;
- I have not independently reconstructed the external article’s full illustrated proof or its cited auxiliary classifications;
- no external theorem is being silently promoted to an independently verified result of this child.

Thus the classical theorem is a **separate, cited, optional import**, not an unpaid load-bearing step in the direct common-\(P\) exclusion.

---

## 12. Achieved scope and remaining unpaid work

### Achieved in this written candidate

Under the exact original actual-\(4455\) hypotheses:

1. Any residual distance-one pair is a saturated equal-degree twin pair.
2. A low-to-low physical pair must extend through a complementary twin pair; otherwise three actual cuts force an inconsistent complex phase subsystem.
3. Twins at either four-symbol party are impossible.
4. Both five-symbol parties are ordinary and
   \[
   R_{34}=L_3\times H_4\ \sqcup\ H_3\times L_4.
   \]
5. Both four-symbol profiles are forced to \((4,4,2,2)\), excluding all profile pairs containing \(D_0\) or \(D_1\).
6. Both five-party high pairs are forced twins.
7. Their two actual components admit exact rounding at all six physical pair projections, preserving the same maximal set \(P\).
8. The remaining profile pair contradicts maximal pair injectivity directly.

Accordingly, **no mathematical compatibility step remains unpaid inside this candidate’s stated \(4455\) proof**.

### Not achieved or not performed

- Independent disjoint reconstruction of this new proof has **not** been performed.
- Parent scientific disposition has **not** been obtained.
- The candidate is **not adopted**.
- No independent-family, human or kernel verification is claimed.
- No worldwide novelty or priority claim is made.
- Other residual-alphabet strata and other maximal-entry counts are not settled here.
- The full support-\(48\) problem and global AME support minimum remain unresolved by this return alone.

The original target must not be reported complete merely because this one stratum has a complete author candidate.

---

## 13. Frozen bindings and access chronology

### Parent-attributed metadata

All hashes, byte counts, LF counts and native clock observations below are **parent-attributed**, not child-executed measurements.

Wave:
`f539-actual-ame4455-nonregular-fourparty-twin-and-phase-frontier`

| Artifact | Parent-supplied SHA-256 | Parent-supplied size |
|---|---|---|
| Manifest | `10dfe18c8e7b34eead215312510540eb5a4479a2153dec64187edf52fef4e83d` | 8339 bytes; 142 LF |
| Freeze receipt | `9e0fb3a90d16f16a208223c02b8648fbf6053c22003728609f003698766d3dca` | 2870 bytes; 73 LF |
| Literal packet | `e664740b49ffc43cf494d252d496fb22322aab65ef2c38ed6aeaf3fc28d069e0` | 41594 bytes; 620 LF |

Frozen scientific inputs:

| Input | Whole-source SHA-256 | Packet coverage |
|---|---|---|
| S1 — Both-four-parties regular exclusion | `562a98778d37a4cea3a9bdead0eaad467ee02323932a9b000f21b5a50baf2160` | Complete logical lines 1–31 |
| S2 — Maximal regimes, missing graphs and slice necessities | `60448959ee1043506210ebec876ede3fc2b91d233781a06d6513942129837632` | Complete logical lines 1–38 |
| S3 — S/five-party singleton degree refinement | `7cd5558dfb8436f37d25348f093401e477135b95e8066a9efebb3b5aba1f1854` | Complete logical lines 1–9 |
| S4 — Full f482 author body | `9ca95b79fa0a264ce3d8e04b151253b5c95c8920a71f5c6d771b5d2c9b00237d` | Complete logical lines 1–540; parent reports 539 LF |

The parent supplied native observations:

- **2026-10-30T12:50:40-0700 PDT**, in the live metadata supply;
- **2026-10-30T13:04:25-0700 PDT**, in a subsequent direct message.

Neither is asserted to be my native start, completion time, or derivation duration. Receipt of a substantive checkpoint was expressly not adoption.

### Actual sequence

Before reading the mathematical packet or doing new mathematics, I read:

1. the mandatory memory summary and written-math acceptance skill;
2. the complete manifest and freeze receipt;
3. the complete parent live metadata supply;
4. all twelve listed permission/status controls, including endings;
5. the parent dispatch receipt.

The controls were read in raw windows of at most twenty LF. I then delivered a **direct pre-body ACK to Main**.

Only afterward did I read the mathematical packet in consecutive raw windows of at most twenty LF:
\[
1\!-\!20,\ 21\!-\!40,\ \ldots,\ 601\!-\!620,
\]
including its ending and the complete S4 ending.

Only after that full packet reading did I develop the new written argument.

### Public-source exploration and dependency correction

After developing the structural and rounding route, I searched publicly for the classical order-six obstruction.

The observed access included:

- part of Betten’s 2020/2021 article, **“The problem of Euler/Tarry revisited”**, DOI  
  https://doi.org/10.1007/s13366-020-00547-y;
- a Stinson PDF route that initially returned HTTP 404;
- the full extracted HTML text of Betten’s 2023 article cited in Section 11, including its ending; its illustrated figures were not independently reconstructed;
- a subsequent Stinson PDF fetch whose text extraction was incomplete;
- CrossRef metadata for Stinson’s 1984 article, DOI  
  https://doi.org/10.1016/0097-3165(84)90044-X.

I do not claim to have read Stinson’s complete proof from those attempts.

An interim checkpoint described the rounding route with an external classical import. Subsequent written work found the direct common-\(P\) contradiction in Section 10. I sent an additive correction to Main explaining that the primary no-go no longer depends on that import.

The public-source reading is disclosed; this is not a claim of blind or cognitively isolated reconstruction.

### Excluded inputs

No local source link embedded in the frozen scientific packet was followed. No linked sibling review, checker, held mathematical payload, held consumer or excluded diagnostic record was opened.

All quarantine records were used only for permissions and status. No clean-fragment salvage or retrospective rehabilitation is asserted.

---

## 14. Proof, experiment and acceptance status

- **Scientific work:** written combinatorics, actual unitary block closure, exact complex phase congruences, common-support projection counting.
- **Scientific code prepared:** none.
- **Scientific execution:** **NOT RUN**.
- **Selected numerical probes, enumeration, solver or CAS:** not used.
- **Builds/tests/lint/formatters:** not run.
- **External-model CLI, paid/heavy/remote computation:** not used.
- **Git operations, installation, deletion, credentials or live-infrastructure changes:** not performed.
- **Working-tree writes:** not attempted; this full body is returned for Main materialization.
- **Child-native clock/hash commands:** not executed.
- **Measured runtime, memory, exit status or scientific stdout:** none claimed.
- **Independent verification and parent adoption:** not performed or obtained.

There is no omitted executable source or experimental output.

**Final status: COMPLETE GENERALAUTHOR WRITTEN CANDIDATE EXCLUDING THE ENTIRE ACTUAL AME4455 STRATUM, WITH EXPLICIT SIX-PROJECTION SAME-\(P,E\) ROUNDING AND A SELF-CONTAINED DIRECT COMMON-\(P\) CONTRADICTION; UNREVIEWED, NOT ADOPTED. GLOBAL SUPPORT-\(48\) AND SUPPORT-MINIMUM CLAIMS REMAIN OUTSIDE THIS RESULT.**