# author-candidate-v1.md

**Wave:** f433-ame48-t24-4455-common-maximal-word-frontier  
**Role:** GENERAL AUTHOR  
**Status:** **COMPLETE WRITTEN AUTHOR CANDIDATE — UNREVIEWED; NOT ADOPTED.**  
**Result:** A whole-\(4455\) necessary-class theorem: exact maximal-word stratification, a four-edge missing-graph classification, and simultaneous low-symbol slice constraints. In the regular-four-party stratum, these imply that the low-to-low residual graph between the two five-symbol parties is a matching.

**Original-target boundary:** The entire \(4455\) class is **not excluded** here. No physical tensor is constructed. The theorem below concerns every actual tensor in the stated class, not a selected support or a real-phase restriction.

**Execution/materialization:** No scientific program was prepared or executed. No working-tree file was written; this is the complete body for parent materialization.

## 1. Exact actual-tensor hypotheses

Work in a fixed product basis. Let
\[
\psi\in(\mathbb C^6)^{\otimes4},\qquad U=6\psi,
\]
and suppose the three balanced flattenings
\[
U^{12\mid34},\qquad U^{13\mid24},\qquad U^{14\mid23}
\]
are unitary.

Suppose \(U\) has exactly \(48\) nonzero entries, exactly \(24\) of modulus one. Define the same tensor-word sets throughout:
\[
P=\{w:|U_w|=1\},\qquad
E=\{w:0<|U_w|<1\}.
\]
Thus \(|P|=|E|=24\).

Permute the physical parties so that the residual alphabets
\[
A_i=\pi_i(E)
\]
satisfy
\[
(q_1,q_2,q_3,q_4):=(|A_1|,|A_2|,|A_3|,|A_4|)
=(4,4,5,5).
\]
Let
\[
B_i=[6]\setminus A_i,\qquad
(b_1,b_2,b_3,b_4):=(|B_1|,\ldots,|B_4|)
=(2,2,1,1).
\]

A coordinate of a maximal word \(w\in P\) is **internal** if \(w_i\in A_i\). Write
\[
k(w)=|\{i:w_i\in A_i\}|,\qquad
n_s=|\{w\in P:k(w)=s\}|.
\]

All statements below allow arbitrary nonzero complex amplitudes and phases. Neither no-distance-one nor no-OLS(6) is assumed.

## 2. Main necessary-class theorem

Under the hypotheses of §1, all the following conclusions hold.

### A. Exactly two global maximal-word regimes

Exactly one of these alternatives occurs:

- **F regime:** There is one four-internal maximal word, no one-internal maximal word, and
  \[
  (n_0,n_1,n_2,n_3,n_4)=(0,0,13,10,1).
  \]
- **S regime:** There is one one-internal maximal word, no four-internal maximal word, and
  \[
  (n_0,n_1,n_2,n_3,n_4)=(0,1,10,13,0).
  \]

Let \(t_i\) count maximal words whose internal positions are exactly the three parties other than \(i\). In the F regime,
\[
(t_1,t_2,t_3,t_4)=(4,4,1,1).
\]
In the S regime, if \(h\) is the internal party of the unique one-internal word, then
\[
t_i=b_i^2+\mathbf1_{\{i\ne h\}}. \tag{2.1}
\]

Let \(d_{ij}\) count maximal words whose internal positions are exactly \(i,j\), and let \(\{k,l\}\) be the complementary party pair. Then
\[
d_{ij}=
\begin{cases}
b_kb_l,&\text{F regime},\\
b_kb_l-\mathbf1_{\{h\in\{i,j\}\}},&\text{S regime}.
\end{cases} \tag{2.2}
\]

These formulas account for all \(24\) words of the same \(P\).

### B. Symbol degrees and the exceptional singleton

For each residual symbol, the partner-independent residual pair-degree \(r_i(a)\) exists.

At each four-symbol party its degree multiset is one of
\[
(3,3,3,3),\qquad (4,3,3,2),\qquad (4,4,2,2). \tag{2.3}
\]

At each five-symbol party the multiset is
\[
(3,3,2,2,2), \tag{2.4}
\]
except possibly at the internal party of the unique one-internal word. That party, if it is a five-symbol party, may instead have
\[
(4,2,2,2,2). \tag{2.5}
\]

More precisely:

- A one-internal word internal at a four-symbol party uses a degree-four symbol. That symbol occurs in precisely one other maximal word, whose internal positions are that party and the two five-symbol parties.
- A one-internal word internal at a five-symbol party uses a degree-three or degree-four symbol, never a degree-two symbol.
- The four-internal word, when present, uses degree-two symbols at both five-symbol parties.

### C. A four-edge graph, with sharply restricted cycles

Define the internal missing graph
\[
M_{12}=(A_1\times A_2)\setminus\pi_{12}(E).
\]
It has exactly four edges and maximum degree two.

In the F regime, \(M_{12}\) is a linear forest. Up to graph isomorphism, after omitting isolated vertices, its only possible types are
\[
4P_2,\quad P_3\sqcup2P_2,\quad
2P_3,\quad P_4\sqcup P_2,\quad P_5, \tag{2.6}
\]
where \(P_m\) denotes a path on \(m\) vertices.

In the S regime with the unique one-internal word internal at a five-symbol party, \(M_{12}\) contains an isolated edge. Its only possible types are
\[
4P_2,\qquad P_3\sqcup2P_2,\qquad P_4\sqcup P_2. \tag{2.7}
\]

A cycle in \(M_{12}\) therefore forces:

1. the S regime;
2. the unique one-internal word to be internal at a four-symbol party;
3. \(M_{12}=C_4\), apart from isolated vertices;
4. both four-symbol parties to have degree multiset \((4,4,2,2)\).

Conversely, the last pair of degree multisets forces \(M_{12}=C_4\), so it cannot occur in either of the first two regimes just described.

These are necessary graph types, not assertions that any type extends to a common packing or tensor.

### D. Simultaneous low-symbol defect constraints

Fix a degree-two symbol \(\ell\) at one five-symbol party, say party \(3\). For \(i\in\{1,2,4\}\), define
\[
N_i=\{a\in A_i:(a,\ell)\in\pi_{i3}(E)\},\qquad
S_i=A_i\setminus N_i.
\]
Then
\[
|N_1|=|N_2|=|N_4|=2,\qquad
|S_1|=|S_2|=2,\quad |S_4|=3.
\]

Set
\[
D_i=\sum_{a\in N_i}r_i(a)-6\quad(i=1,2),\qquad
H=\sum_{a\in N_4}r_4(a)-4. \tag{2.8}
\]
Here
\[
-2\le D_i\le2,\qquad H\in\{0,1,2\}.
\]

For \(ij\in\{12,14,24\}\), write
\[
s_{ij}=|M_{ij}\cap(S_i\times S_j)|,\qquad
z_{ij}=|M_{ij}\cap(N_i\times N_j)|.
\]
The exact identities are
\[
\begin{aligned}
z_{12}&=s_{12}-D_1-D_2,\\
z_{14}&=s_{14}-D_1-H,\\
z_{24}&=s_{24}-D_2-H.
\end{aligned} \tag{2.9}
\]

Moreover,
\[
z_{ij}\in\{0,1,2\},\qquad
\text{at most one of }z_{12},z_{14},z_{24}\text{ is positive}. \tag{2.10}
\]

Let \(u_{12},u_{14},u_{24}\) count maximal triples containing \(\ell\) and the indicated two other internal parties. Let \(f\) indicate whether the four-internal maximal word contains \(\ell\). Then
\[
u_{12}+u_{14}+u_{24}=3-2f,\qquad
u_{ij}\le2, \tag{2.11}
\]
and at least two of the following three inequalities hold:
\[
\begin{aligned}
u_{12}+f&\le D_1+D_2,\\
u_{14}+f&\le D_1+H,\\
u_{24}+f&\le D_2+H.
\end{aligned} \tag{2.12}
\]

The corresponding constraints hold for every degree-two symbol at party \(4\), with parties \(3,4\) exchanged. They concern the same six pair complements and the same maximal set—not separately adjustable local interfaces.

### E. Matching theorem in the regular-four-party stratum

Suppose additionally that every residual symbol at parties \(1,2\) has degree three.

At a five-symbol party, call its degree-two symbols **low** and its other residual symbols **high**. Then every low symbol at either five-symbol party has at least one high residual neighbor at the other.

Consequently, the residual graph between the low sets at parties \(3,4\) is a matching.

If both five-symbol degree multisets are \((3,3,2,2,2)\), let \(m\) be its number of low-to-low edges. Then \(0\le m\le3\), and the four sector edge counts of \(R_{34}=\pi_{34}(E)\) are exactly
\[
\begin{array}{c|cc}
 &L_4&H_4\\ \hline
L_3&m&6-m\\
H_3&6-m&m
\end{array}. \tag{2.13}
\]

If one five-symbol party has degree multiset \((4,2,2,2,2)\), the low-to-low matching has exactly three edges. With that exceptional party taken to be party \(3\), the sector counts are
\[
\begin{array}{c|cc}
 &L_4&H_4\\ \hline
L_3&3&5\\
H_3&3&1
\end{array}. \tag{2.14}
\]

The proofs follow.

## 3. Derivation of the actual shared support interface

A modulus-one entry of a unitary matrix exhausts its row and column. Thus in each balanced flattening the \(24\) entries of \(P\) occupy distinct rows and columns, containing no other support entries.

Deleting those rows and columns leaves a \(12\times12\) unitary with exactly \(24\) nonzeros. No remaining row or column can be a singleton: its entry would then have modulus one and belong to \(P\). Every remaining row and column therefore has exactly two nonzeros.

The three cuts cover all six physical pair projections. For every \(ij\), putting
\[
R_{ij}=\pi_{ij}(E),
\]
we obtain
\[
|R_{ij}|=12,\qquad
|\pi_{ij}^{-1}(x)\cap E|=2\quad(x\in R_{ij}), \tag{3.1}
\]
and
\[
\pi_{ij}\text{ is injective on }P,\qquad
\pi_{ij}(P)=[6]^2\setminus R_{ij}. \tag{3.2}
\]

For \(a\in A_i\), define
\[
p_i(a)=|\{w\in P:w_i=a\}|.
\]
Equation (3.2) gives, for every partner \(j\),
\[
r_i(a):=|\{b:(a,b)\in R_{ij}\}|=6-p_i(a). \tag{3.3}
\]
Hence the residual degree is partner-independent, and
\[
|\{w\in E:w_i=a\}|=2r_i(a),\qquad
\sum_{a\in A_i}r_i(a)=12. \tag{3.4}
\]

A used symbol cannot have residual degree one. Its two residual words would then have the same unique neighbor at each other party and would coincide. Therefore
\[
r_i(a)\ge2. \tag{3.5}
\]

Nothing here uses no-distance-one.

For completeness, actual orthogonality also makes each residual flattening a union of six full \(2\times2\) blocks. If two degree-two rows share one column, a lone overlap would give a nonzero inner product, so they must share both columns. The new necessary-class theorem does not need that additional block condition.

## 4. Global moments and all maximal-word types

The first internal-coordinate moment is
\[
\sum_{w\in P}k(w)
=6\sum_iq_i-48
=60. \tag{4.1}
\]
The second is
\[
\sum_{w\in P}\binom{k(w)}2
=\sum_{i<j}q_iq_j-72
=49. \tag{4.2}
\]

For \(s=0,1,2,3,4\), the values of
\[
\binom{s}{2}-2s+3
\]
are \(3,1,0,0,1\). Summation therefore gives
\[
3n_0+n_1+n_4
=49-2\cdot60+3\cdot24
=1. \tag{4.3}
\]
Thus \(n_0=0\) and exactly one of \(n_1,n_4\) equals one. Using \(\sum n_s=24\) and (4.1) gives the two histograms in §2A.

To refine the histogram to actual internal-position types, fix a party \(i\). Exactly \(6b_i\) maximal words are outside at that party. By (3.2), their total number of internal coordinates elsewhere is
\[
b_i\sum_{j\ne i}q_j.
\]
Let \(\sigma_i\) indicate whether the unique one-internal word exists and is outside at party \(i\). Among these \(6b_i\) words, all have two or three internal coordinates except that possible single word. Consequently,
\[
b_i\sum_{j\ne i}q_j
=12b_i-\sigma_i+t_i.
\]
Since \(\sum_jq_j=18\) and \(b_i=6-q_i\),
\[
t_i=b_i(6-q_i)+\sigma_i=b_i^2+\sigma_i. \tag{4.4}
\]
This proves (2.1).

For the double-internal types, fix complementary pairs \(ij\) and \(kl\). Every outside pair in \(B_k\times B_l\) is used by exactly one maximal word. Such a word is either:

- internal exactly at \(i,j\); or
- the unique one-internal word, with internal party in \(\{i,j\}\).

There are no zero-internal words, and a triple has only one outside coordinate. This proves (2.2).

In particular, the complete F-regime double counts are
\[
(d_{12},d_{13},d_{14},d_{23},d_{24},d_{34})
=(1,2,2,2,2,4).
\]

Up to exchanges \(1\leftrightarrow2\) and \(3\leftrightarrow4\), the S-regime triple counts are
\[
\begin{array}{c|rrrr}
\text{internal party }h&t_1&t_2&t_3&t_4\\ \hline
1&4&5&2&2\\
3&5&5&1&2
\end{array}.
\]
These are exact counts of words of one common \(P\), not separately chosen pair counts.

## 5. Symbol-degree classification

For \(a\in A_i\), let:

- \(\tau_i(a)\) count maximal triples containing \(a\);
- \(f_i(a)\) indicate whether the four-internal word contains \(a\);
- \(\sigma_i(a)\) indicate whether the one-internal word is internal at \(i\) with symbol \(a\).

Counting other internal coordinates among the maximal words containing \(a\) gives
\[
18-q_i-3r_i(a)
=p_i(a)-\sigma_i(a)+\tau_i(a)+2f_i(a).
\]
Using \(p_i(a)=6-r_i(a)\),
\[
\tau_i(a)+2f_i(a)-\sigma_i(a)
=12-q_i-2r_i(a). \tag{5.1}
\]

### Four-symbol parties

Here the right side is \(8-2r_i(a)\). Since \(\sigma_i(a)\le1\) and the other counts are nonnegative, \(r_i(a)\le4\). Together with \(r_i(a)\ge2\) and the degree sum twelve, this gives exactly the three multisets (2.3).

If the unique one-internal word is internal at party \(1\), using \(a\), every other maximal word containing \(a\) must be internal at parties \(3,4\): each of those parties has only one outside symbol, already paired with \(a\) in the one-internal word.

There is no four-internal word in this regime. Hence every other such word is outside at party \(2\). Thus no internal party-\(2\) symbol is paired with \(a\) in \(P\), so
\[
4-r_1(a)=0.
\]
Therefore \(r_1(a)=4\), \(p_1(a)=2\), and its other maximal word has internal positions \(134\). The party-\(2\) version is identical.

### Five-symbol parties

Away from the internal symbol of the one-internal word, (5.1) gives \(r_i(a)\le3\). Five degrees at least two summing to twelve must then be \((3,3,2,2,2)\).

If the four-internal word contains \(a\), (5.1) gives
\[
\tau_i(a)+2=7-2r_i(a).
\]
Thus \(r_i(a)=2\) and \(\tau_i(a)=1\).

Suppose instead that \(a\) is the internal symbol of the one-internal word at a five-symbol party. Then
\[
\tau_i(a)=8-2r_i(a).
\]
The one-internal word is not a triple, so
\[
\tau_i(a)\le p_i(a)-1=5-r_i(a).
\]
It follows that \(r_i(a)\ge3\), while (5.1) gives \(r_i(a)\le4\).

Degree three leaves the ordinary degree multiset. Degree four forces all four other degrees to equal two. At most one five-symbol party can have this exception, since there is only one one-internal word and only one internal coordinate in it.

This proves §2B. In particular, **every degree-two symbol at a five-symbol party has**
\[
\sigma_i(a)=0,\qquad
\tau_i(a)+2f_i(a)=3. \tag{5.2}
\]

## 6. The four-edge missing-graph classification

By (3.2),
\[
|M_{12}|=q_1q_2-12=4.
\]
At a vertex \(a\in A_1\), its degree in \(M_{12}\) is
\[
4-r_1(a),
\]
and similarly on the other side. Thus the maximum degree is two.

Let \(o_3,o_4\) be the unique outside symbols of the two five-symbol parties. Exactly one maximal word \(v\) uses \((o_3,o_4)\).

### F regime

There are no one-internal or zero-internal words, so \(v\) has internal positions \(12\). The four edges of \(M_{12}\) are exactly the pair projections of:

1. \(v\), with parties \(3,4\) outside;
2. the unique triple with party \(3\) outside;
3. the unique triple with party \(4\) outside;
4. the four-internal word.

The edge from \(v\) cannot share an endpoint with either triple edge. Sharing an endpoint with the party-\(3\)-outside triple would repeat the corresponding pair with \(o_3\); sharing with the party-\(4\)-outside triple would repeat a pair with \(o_4\).

Its only possible adjacent edge is therefore the four-internal edge. It cannot meet that same edge at both endpoints, since the \(12\)-projection on \(P\) is injective.

Thus \(v\)'s edge cannot lie in a cycle. A cycle not using it would have at most three edges, impossible in a simple bipartite graph. Hence \(M_{12}\) is a forest of maximum degree two. Its four-edge component partitions give exactly (2.6).

This argument does **not** prohibit the four-internal edge from meeting a triple edge; no such stronger restriction is needed or claimed.

### S regime, internal party five-symbol

Take the internal party to be party \(3\). Then \(v\) cannot be the one-internal word, since \(v_3=o_3\). Consequently \(v\) again has internal positions \(12\).

The remaining three internal-\(12\) maximal words are triples: one outside at party \(3\), two outside at party \(4\). Each shares an outside coordinate with \(v\), so none of their edges can meet \(v\)'s edge. It is an isolated component.

The other three edges have maximum degree two and cannot contain a bipartite cycle. Their possibilities are a three-edge path, a two-edge path plus an edge, or three disjoint edges. This gives (2.7).

### S regime, internal party four-symbol

Take the internal party to be party \(1\). The one-internal word is now \(v\) itself, so its projection is not an internal-\(12\) edge.

All four edges of \(M_{12}\) come from triples: two outside at party \(3\), two outside at party \(4\). Each of these two edge classes is a matching, by pair injectivity with the corresponding unique outside symbol.

Their union is a graph of maximum degree two. With four edges, its only possible cycle is \(C_4\).

Finally, both four-symbol degree multisets are \((4,4,2,2)\) exactly when \(M_{12}\) has two degree-two and two isolated vertices on each side. Its four edges must then be all edges of a \(K_{2,2}=C_4\). This proves all claims in §2C.

## 7. Four-word slices, including the distance-one alternative

Fix a degree-two symbol \(\ell\in A_3\). By (3.4), its residual slice
\[
E_\ell=\{w\in E:w_3=\ell\}
\]
has four distinct words. At each other party, exactly two symbols occur, each twice.

Index these words by a four-element set \(V\). Each other coordinate induces an unordered \(2+2\) partition of \(V\).

There are exactly three such partitions. Two different partitions intersect in four singleton cells, so the corresponding pair projection contains the full product of its two neighbor sets.

All three coordinate partitions cannot coincide: that would give only two distinct coordinate triples, each repeated, contradicting distinct tensor support words.

Therefore either:

- the three partitions are all different, and all three pair projections are full; or
- exactly two partitions coincide, and only that coordinate-pair projection is nonfull.

In the latter case the nonfull projection consists of two pairs forming a bijection between its two-symbol alphabets. Its omitted pairs form the other bijection.

Thus missing global pairs can occur inside \(N_i\times N_j\) for at most one of the three pairs \(12,14,24\). For that pair there are at most two, and they form a submatching.

This proves (2.10). It explicitly retains the exactly-two-equal-partitions alternative; no no-distance-one assumption removes it.

## 8. Exact defect identities and common-\(P\) inequalities

For any bipartite missing graph \(M_{ij}\), splitting each side into \(N\) and \(S\) gives
\[
|M_{ij}\cap(N_i\times N_j)|
-
|M_{ij}\cap(S_i\times S_j)|
=
\deg_{M_{ij}}(N_i)-\deg_{M_{ij}}(S_j). \tag{8.1}
\]

For \(M_{12}\), its degree at a party-\(1\) vertex is \(4-r_1(a)\). Hence
\[
\deg_{M_{12}}(N_1)=8-\sum_{N_1}r_1.
\]
The total degree sum on party \(2\) is four, while
\[
\deg_{M_{12}}(N_2)=8-\sum_{N_2}r_2.
\]
Therefore
\[
\deg_{M_{12}}(S_2)=\sum_{N_2}r_2-4.
\]
Equation (8.1) yields
\[
z_{12}-s_{12}
=12-\sum_{N_1}r_1-\sum_{N_2}r_2
=-D_1-D_2. \tag{8.2}
\]

For \(M_{14}\), the degree at a party-\(1\) vertex is \(5-r_1(a)\), and at a party-\(4\) vertex it is \(4-r_4(a)\). Since this graph has eight edges,
\[
\deg_{M_{14}}(N_1)=10-\sum_{N_1}r_1,\qquad
\deg_{M_{14}}(S_4)=\sum_{N_4}r_4.
\]
Consequently,
\[
z_{14}-s_{14}
=10-\sum_{N_1}r_1-\sum_{N_4}r_4
=-D_1-H. \tag{8.3}
\]
The \(24\) identity is identical. This proves (2.9).

The bounds on \(D_i\) follow from the four-party degrees lying between two and four. At a five-symbol party, either the degrees are \(3,3,2,2,2\), or they are \(4,2,2,2,2\). Any two degrees therefore sum to four, five, or six, proving \(H\in\{0,1,2\}\).

Every maximal triple containing \(\ell\) supplies an edge between the corresponding \(S\)-sets: a maximal pair with \(\ell\) cannot be a residual pair. The four-internal word containing \(\ell\), if present, supplies an edge for each of the three pairs. Pair injectivity on the same \(P\) makes these edges distinct. Thus
\[
s_{ij}\ge u_{ij}+f. \tag{8.4}
\]

Equation (5.2) gives
\[
u_{12}+u_{14}+u_{24}=3-2f.
\]
Each \(u_{ij}\le2\), since such triples use distinct maximal pairs consisting of \(\ell\) and a symbol from one of the two-element \(S_1,S_2\).

By §7 at least two \(z_{ij}\) vanish. Substitution into (2.9), followed by (8.4), proves the three-way requirement (2.12).

A zero defect is not asserted to imply a full slice projection. The argument only uses the valid implication from slice fullness to zero defect, and the fact that at most one defect can be positive.

## 9. Proof of the low-to-low matching theorem

Assume now that the four-symbol parties are regular of degree three. Then, for every low-symbol slice,
\[
D_1=D_2=0.
\]

Suppose a low symbol \(\ell\in A_3\) had no high residual neighbor at party \(4\). Both of its neighbors there would have degree two, so \(H=0\). Equations (2.9) would then give
\[
z_{12}=s_{12},\qquad
z_{14}=s_{14},\qquad
z_{24}=s_{24}. \tag{9.1}
\]
At most one of these three \(s\)-counts could be positive.

There are two possibilities.

- If \(f=1\), the four-internal word containing \(\ell\) gives
  \[
  s_{12},s_{14},s_{24}\ge1,
  \]
  an immediate contradiction.
- If \(f=0\), equation (2.11) gives
  \[
  u_{12}+u_{14}+u_{24}=3.
  \]
  Each \(u_{ij}\le2\), so at least two are positive. By (8.4), at least two \(s_{ij}\) are positive, again a contradiction.

Thus every low party-\(3\) symbol has a high party-\(4\) neighbor. The symmetric argument applies to low party-\(4\) symbols.

Each low symbol has total residual degree two, so it can have at most one low neighbor. The low-to-low graph is therefore a matching.

### Ordinary degree multisets

There are three low and two high symbols on each side. If the low-to-low matching has \(m\) edges, the low-side degree sums give
\[
|R_{34}\cap(L_3\times H_4)|
=
|R_{34}\cap(H_3\times L_4)|
=6-m.
\]
The high degree sum is six, leaving \(m\) high-to-high edges. This proves (2.13).

### One exceptional degree multiset

Suppose party \(3\) has one degree-four high symbol and four low symbols. Party \(4\) has two high symbols and three low symbols.

Each low party-\(4\) symbol must use the unique high party-\(3\) symbol, and its other neighbor must be low: the graph is simple, so it cannot use that same high symbol twice. Thus the low-to-low matching has exactly three edges.

The remaining sector counts follow from the low and high degree sums, giving (2.14).

### Additional F-regime consequence

In the regular-four-party F regime, let \(\ell\) be the party-\(3\) symbol of the four-internal word. It has exactly one maximal triple.

Since \(s_{12}\ge1\) and \(D_1=D_2=0\), the \(12\) defect is positive. The other two defects therefore vanish, and
\[
H\ge u_{14}+1,\qquad H\ge u_{24}+1. \tag{9.2}
\]

Consequently:

- \(\ell\) has at least one high neighbor at party \(4\);
- if its unique maximal triple has internal positions \(134\) or \(234\), then \(H=2\), so both residual neighbors are high;
- if it has only one high neighbor, its unique maximal triple must have internal positions \(123\), with party \(4\) outside.

The same statement holds with the two five-symbol parties exchanged.

This is a restriction, not a contradiction closing the F regime.

## 10. Relation to the original target and exact unpaid step

The result is the implication
\[
\begin{split}
&\text{one actual complex }U,\ \text{three unitary balanced flattenings},\\
&|\operatorname{supp}U|=48,\quad |P|=24,\quad(q_i)=4455\\
&\hspace{1cm}\Longrightarrow
\text{the classifications and simultaneous constraints of §§2–9}.
\end{split}
\]

The proof preserves:

- the same \(24\)-word maximal set \(P\);
- all six maximal/residual pair complements;
- exactly two residual extensions per residual pair;
- distinct residual words;
- the distance-one-allowed slice alternative;
- arbitrary nonzero complex phases and residual moduli.

It does not establish a physical tensor from a graph or moment shadow.

**The first unpaid scientific implication is global incompatibility:** no contradiction has been proved between all surviving maximal-word regimes, the six shared pair complements, the low-slice constraints, and simultaneous \(2\times2\) block closure of an actual \(24\)-word residual set.

In particular, this manuscript has not established either existence or nonexistence of complete \(P,E\) sets satisfying that entire support interface.

If such a support is found, complex phase consistency remains essential. For a full \(2\times2\) block with entries \(a,b,c,d\), actual unitarity requires
\[
|a|^2=|d|^2,\qquad |b|^2=|c|^2,\qquad
|a|^2+|b|^2=1
\]
and
\[
\arg a-\arg b-\arg c+\arg d\equiv\pi\pmod{2\pi}. \tag{10.1}
\]

On a support that genuinely decomposes into full \(2\times2\) residual blocks in all three cuts, assigning all residual squared moduli \(1/2\) satisfies the modulus equations simultaneously. Finding compatible phases is still necessary; failure of real signs alone would not exclude arbitrary complex phases.

No conclusion here excludes \(3555\), \(4555\), or \(5555\), proves a universal \(t=24\) exclusion, excludes all support \(48\), proves \(N\ge49\), or determines a product-basis support minimum.

## 11. Public-source comparison and novelty boundary

After developing the packet-based counting, graph, and slice route, I opened the public primary source:

Palash Pandya, *Euler’s thirty-six officers need not all be entangled: real AME(4,6), families and classification*, [arXiv:2610.16673v1](https://arxiv.org/html/2610.16673v1).

The relevant inspected material was:

- [§III, Lemma 1](https://arxiv.org/html/2610.16673v1#Thmlemma1), including its complete displayed proof, which gives the modulus equations and complex phase congruence for supports composed of \(1\times1\) and \(2\times2\) blocks;
- [§VI](https://arxiv.org/html/2610.16673v1#S6), specifically its support-bound discussion, which states the \(38\)–\(60\) gap as open at that version.

The block equations in §10 are consistent with that lemma. The new graph and low-slice necessity claims above are proved directly here and do not import an external no-OLS or no-distance-one premise.

This was **not** an exhaustive literature search, a complete-paper verification, or a priority audit. “New” in this return means an additional theorem developed for this frozen assignment beyond the supplied \(4444/4445\) exclusions and general moment interface—not a worldwide novelty claim.

## 12. Access, bindings, chronology, and execution limits

### Frozen bindings

The assigned bindings are:

| Artifact | SHA-256 |
|---|---|
| Manifest | `70e21aa06c7f7ab6a075e05395ec1c236e0e414e26b43d251eedbf6e2305fe6b` |
| Freeze receipt | `869e72e6bb2c2a8cadd6fb149468f441671a0ccf1fccfbb4944050cbad929f28` |
| Literal packet | `e413c6c70a75b820365be1467423baa0188a7167e0c4798dc83feb90317f5def` |

The parent metadata reports respectively:

- manifest: \(7085\) bytes, \(131\) LF;
- receipt: \(3152\) bytes, \(86\) LF;
- packet: \(44450\) bytes, \(604\) LF.

Matching pins, byte counts, and LF counts are **parent-attributed observations**, not child-executed hash checks. The supplied observation **2026-10-30T11:10:50-0700 PDT** is likewise parent metadata, not my native start or completion time.

### Actual read sequence

I read:

1. the required memory summary and relevant research/acceptance skills;
2. the manifest, freeze receipt, and parent live metadata;
3. all eight named permission/status controls, before reading the mathematical packet;
4. an initial packet window, followed by complete raw windows covering packet lines \(1\)–\(604\);
5. the dispatch receipt in the complete-packet read batch;
6. the public primary-source material described in §11, followed by further written refinement.

The complete frozen packet coverage was:

- S1: logical lines \(1\)–\(23\);
- S2: logical lines \(1\)–\(27\);
- S3: logical lines \(1\)–\(481\);
- S4: logical lines \(1\)–\(28\);
- S5: logical lines \(1\)–\(43\).

The source links appearing inside the packet were not followed into additional local research records.

### Exclusions

The quarantine controls were used for permissions and status only. No held \(t=28\) phase/compression payload, held PH registration/report consumer, CORE/privacy diagnostic payload, or unassigned sibling result/program was opened or used.

This is an actual access chronology, not a claim of certified cognitive isolation.

### Execution and files

All scientific calculations in this return are written counting and algebra.

- Scientific code: **none prepared**.
- Scientific execution: **NOT RUN**.
- Interpreter, solver, CAS, enumeration: **not used**.
- Builds, tests, lint, formatters: **not run**.
- Working-tree writes: **not attempted under the current read-only runtime restriction**.
- Child-native clock/hash commands: **not executed**.
- No argv, stdout, exit status, measured runtime, or measured memory is claimed.

There is consequently no executable source or output omitted from this return. The complete mathematical body is supplied above rather than referred to through an earlier message.

## 13. Acceptance status

The delivered scientific progress is:

1. an exact two-regime classification of all \(24\) maximal words by internal-position type;
2. a missing-graph forest/cycle theorem that restricts the simultaneous four-party degree patterns;
3. exact shared-\(P\) low-slice defect identities and inequalities;
4. a low-to-low matching theorem, with exact sector counts, whenever the two four-symbol parties are degree-three regular;
5. a further restriction on the four-internal word in that regular stratum.

These are complete written proofs at their stated **necessary-condition scope**. They have not received a disjoint reconstruction, parent disposition, independent-family review, human review, formal/kernel verification, or novelty clearance.

**Final status: COMPLETE WHOLE-\(4455\) NECESSARY-CLASS AUTHOR CANDIDATE; FULL \(4455\) EXCLUSION NOT PROVED; NO PHYSICAL WITNESS; NO AUTOMATIC PARENT ADOPTION.**