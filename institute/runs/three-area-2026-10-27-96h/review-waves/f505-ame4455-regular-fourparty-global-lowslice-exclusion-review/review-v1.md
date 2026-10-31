# F505 WRITTEN review: actual \(4455\) regular-four-party exclusion

**Overall correctness:** correct at the stated scope.  
**Disposition:** SUPPORTED by same-harness written reconstruction; no automatic adoption.  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Confidence:** 0.97.

The supplied proof excludes an actual complex support-\(48\), \(t=24\), \(q=(4,4,5,5)\) tensor when **both four-symbol parties are degree-three regular**. I reconstructed the common-tensor interface, twin-overlap argument, arbitrary-complex phase obstruction, and final synthesis of all low slices without finding a gap. This does **not** exclude the remaining nonregular \(4455\) profiles or establish a global support-minimum result.

## 1. Frozen bindings, access sequence and method boundary

The following measurements are **parent-attributed**, from the supplied live-metadata record, not independently executed child measurements:

| Record | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| Manifest | `115afd7f7b9bdcba73c5bf5b1ab5d74ecdfe59c8e28e9c95e9fab924774485dd` | 7,235 | 120 |
| Freeze receipt | `18fd8a29506984fdde8454c10d042039554274c721d382be3dd4508ab0668ea1` | 2,313 | 60 |
| Literal packet | `752cb126aab9bff1f68698826647f523e4940042c369e08c74a902b6443de9c2` | 34,770 | 589 |

The parent’s supplied clock observation is **2026-10-30T12:27:52-0700 PDT**. It is not my native start, checkpoint, completion time or measured runtime.

Before opening the mathematical packet, I completely read:

1. The required memory summary and applicable written-review instructions.
2. The frozen manifest and freeze receipt.
3. All ten listed status-only controls, including their endings.
4. The supplied parent live-metadata record.

I then sent Main a **direct administrative pre-body ACK**, which the communication tool reported delivered. No packet-body reading or mathematical derivation preceded that ACK.

After the ACK, I read the complete literal packet sequentially, raw, in windows of at most twenty physical lines, covering **packet lines 1–589**, including all source endings:

- **S1:** logical lines **1–540**; parent-reported source LF count 539.
- **S2:** logical lines **1–38**.
- **S3:** logical lines **1–9**.

No returned packet window contained an unresolved elision.

This was a **WRITTEN-only** review using formal parameters and the author-explicit configurations. I did not create a new selected mathematical instance or private probe, prepare or execute scientific code, run a CAS/solver/enumeration, follow packet links, open sibling reviews or author programs, or consult a new external source. Held episodes and their consumers—including the AME compression/t28 episodes and f439/f444/f448—were **NONINPUT**. This records actual access and use, not a certificate of cognitive isolation.

## 2. Exact imports and claim dispositions

| Claim | Source | Disposition |
|---|---|---|
| Actual same-\(P,E\) pair multiplicities and residual block closure | S1 LF31–77; S2 LF7–9 | **SUPPORTED** |
| Ordinary/exceptional five-party degree profiles | S1 LF81–127; S2 LF13–18 | **SUPPORTED** |
| Twin-overlap bipartiteness and both corollaries | S1 LF131–193 | **SUPPORTED** |
| Derived prohibition on distance-one pairs varying at party 1 or 2 | S1 LF199–215 | **SUPPORTED** |
| No low-to-low edge in actual \(R_{34}\), including complex phases | S1 LF219–300 | **SUPPORTED** |
| Both five-parties ordinary and \(R_{34}=K_{3,2}\sqcup K_{2,3}\) | S1 LF304–326 | **SUPPORTED** |
| Same-\(E\) incidence identity and contradiction from all low slices | S1 LF330–407 | **SUPPORTED** |
| Exclusion limited to the pair of regular four-party profiles | S1 LF411–472 | **SUPPORTED** |

S2 supplies the adopted actual common-tensor interface and degree restrictions. I also reconstruct below the portions needed by this proof; I do not import the linked finite checker or previous reviewers’ conclusions as a substitute.

S3 is the separately adopted refinement restricted to **S with singleton internal at a five-party**. It is **not needed** for the regular-subregime exclusion. Its exact restriction can qualify the residual profile ledger; it does not turn this proof into a whole-\(4455\) exclusion.

The full nonregular \(4455\) compatibility problem remains **INCONCLUSIVE / NOT PROVED by this candidate**. No claim is refuted in this review.

## 3. Actual common-tensor interface

**SUPPORTED — S1 LF31–77.**

Every balanced flattening is a \(36\times36\) unitary. A modulus-one entry exhausts its row and column, so the 24 entries of \(P\) occupy 24 distinct rows and columns in each cut and exclude residual entries there. Deleting them leaves a \(12\times12\) unitary containing exactly the 24 entries of the same residual set \(E\).

Every remaining row and column has at least two nonzeros: a row or column with exactly one would make that entry modulus one, contrary to its membership in \(E\). With 24 entries in 12 rows and 12 columns, every residual row and column therefore has exactly two.

Every physical pair appears as a row or column label in one balanced cut. Consequently, for each \(ij\),

\[
|R_{ij}|=12,
\]

every pair of \(R_{ij}\) has exactly two \(E\)-extensions, and the injective maximal-pair projection is its complement in \([6]^2\). These statements concern projections of **one actual \(P,E\)**, not independently constructed pair graphs.

For an internal symbol \(a\), the maximal words containing \(a\) use distinct partner symbols at every other coordinate. Thus

\[
r_i(a)=6-p_i(a)
\]

is partner-independent. Its residual-word multiplicity is \(2r_i(a)\), and the degrees sum to 12 at each party. If \(r_i(a)=1\), the two residual words through \(a\) would have the same unique neighbor at each other party and hence would be the same tensor word. Thus \(r_i(a)\ge2\).

Finally, if two residual rows share a column, orthogonality prevents that from being their sole common nonzero column. Their second columns must agree. With column degree two, this closes a full \(2\times2\) component. The residual flattening is therefore a disjoint union of six full nonzero unitary blocks.

## 4. Five-party degree profiles and coverage of F/S

**SUPPORTED — S1 LF81–127.**

The internal-coordinate moments follow from the common maximal set:

\[
\sum_{w\in P}k(w)=\sum_i(6q_i-12)=60,
\]

and

\[
\sum_{w\in P}\binom{k(w)}2
=\sum_{i<j}(q_iq_j-12)=49.
\]

The displayed coefficient identity gives

\[
3n_0+n_1+n_4=1.
\]

Hence \(n_0=0\), and precisely one of \(n_1,n_4\) equals one. Together with the two moments, these are exactly the supplied F and S histograms. In particular, there is at most one one-internal maximal word.

For an internal symbol \(a\) at a five-symbol party, the number of other-internal-coordinate incidences among maximal words through it is

\[
(4-r(a))+(4-r(a))+(5-r(a))=13-3r(a).
\]

Starting with one such incidence for each of its \(6-r(a)\) maximal words, a singleton subtracts one, a triple adds one, and a four-internal word adds two. Therefore

\[
\tau(a)+2f(a)-\sigma(a)=7-2r(a).
\]

Since \(\tau,f\ge0\), a symbol with \(\sigma=0\) has \(r\le3\), and a symbol with \(\sigma=1\) has \(r\le4\). Only one symbol at one party can receive the latter exception.

Five degrees at least two summing to twelve consequently give precisely

\[
(3,3,2,2,2)
\]

or, at at most one five-party,

\[
(4,2,2,2,2).
\]

Nothing here assumes no-OLS or no-distance-one. The subsequent proof covers both F and S.

## 5. Twin-overlap graph and derived distance-one restrictions

### 5.1 Twin-overlap bipartiteness

**SUPPORTED — S1 LF133–175.**

Suppose two residual words differ only at coordinate \(i\), with symbols \(a\ne a'\). Their common triple set

\[
T=V_a\cap V_{a'}
\]

is nonempty.

For each other coordinate \(j\), exact multiplicity two pairs the elements of \(V_a\) having the same \(j\)-coordinate. If \(v\in T\), the rows \((a,v_j)\) and \((a',v_j)\) share the column determined by the remaining two coordinates. Actual block closure forces their second columns to coincide. Therefore the \(j\)-partner of \(v\) also belongs to \(T\). Each of the three coordinates induces a perfect matching on \(T\).

Two distinct triples in \(T\) cannot share two coordinates: their copies with \(a\) and \(a'\) would give four distinct residual extensions of that physical pair. Thus the three matching partners at each vertex are distinct, and the resulting graph is simple and cubic.

For

\[
z_v=U_{a,v}\overline{U_{a',v}}\ne0,
\]

row orthogonality along a matching edge gives exactly

\[
z_v+z_{v'}=0.
\]

Following an odd cycle would yield \(z_v=-z_v\), impossible for a nonzero complex number. Hence the graph is bipartite. This argument does not restrict phases to real signs.

### 5.2 Low symbols and degree-three twins

**SUPPORTED — S1 LF177–193.**

A nonempty simple cubic bipartite graph has at least three vertices in each part.

If one varying symbol has degree two, its entire triple slice has four elements, too few to contain \(T\). Thus a distance-one pair cannot vary through a degree-two symbol, regardless of the degree of its other varying symbol.

If both varying symbols have degree three, both slices have six elements. The graph requires at least six common triples, so the two slices coincide completely. Their neighbor sets at every other party are therefore identical; the six-vertex graph is necessarily \(K_{3,3}\).

### 5.3 No variation at party 1 or 2 under regularity

**SUPPORTED — S1 LF199–215.**

With both four-parties degree-three regular, \(M_{12}\) has degree one at every vertex and is a perfect matching.

A distance-one pair varying at party 1 would use two degree-three symbols with identical party-2 residual neighbor sets. Their unique missing party-2 neighbor would coincide, giving that missing-graph vertex degree at least two. This contradicts the perfect matching. The party-2 argument is symmetric.

This is a **derived** restriction. It does not prohibit every distance-one pair at parties 3 or 4.

## 6. Low-to-low edge and the complex phase interface

**SUPPORTED — S1 LF219–300.**

Suppose \((\ell,m)\in R_{34}\) with both symbols low. Its two extensions cannot differ at only party 1 or only party 2, by the preceding result, so they differ at both.

The four words through \(\ell\) induce three balanced \(2+2\) partitions at parties 1, 2 and 4. The party-4 partition differs from each of the party-1 and party-2 partitions because the two words through \((\ell,m)\) have different values at both those parties.

If the party-1 and party-2 partitions coincided, their common block would give words differing only at party 4, one using the low symbol \(m\). The low-symbol corollary excludes that. All three partitions in the \(\ell\)-slice therefore differ. The symmetric argument applies to the \(m\)-slice.

Using the author’s explicit relabeling, these slices force

\[
0000,\ 1100,\ 0101,\ 1001,\ 0110,\ 1010.
\]

In the cut \(13\mid24\), block closure forces both missing even-parity words:

- The row containing \(0000,0101\) and the column containing \(0000,1010\) force \(1111\).
- The row containing \(1100,1001\) and the column containing \(1100,0110\) force \(0011\).

Thus all eight author-listed even-parity words belong to the same actual \(E\). They already supply two extensions of every physical pair they use. The following are therefore actual closed residual blocks, not independently chosen matrices:

\[
12\mid34:\quad
\begin{pmatrix}
U_{0000}&U_{0011}\\
U_{1100}&U_{1111}
\end{pmatrix},
\]

\[
13\mid24:\quad
\begin{pmatrix}
U_{0000}&U_{0101}\\
U_{1010}&U_{1111}
\end{pmatrix},
\]

\[
14\mid23:\quad
\begin{pmatrix}
U_{0011}&U_{0101}\\
U_{1010}&U_{1100}
\end{pmatrix}.
\]

For a full nonzero block \(\begin{pmatrix}u&v\\w&x\end{pmatrix}\), orthogonality implies

\[
u\overline w=-v\overline x,
\]

and hence

\[
\arg u-\arg v-\arg w+\arg x\equiv\pi\pmod{2\pi}.
\]

With the author’s definitions of \(X,Y,Z\), the three displayed blocks give

\[
X-Y\equiv\pi,\qquad
X-Z\equiv\pi,\qquad
Y-Z\equiv\pi
\pmod{2\pi}.
\]

Subtracting the first two requires \(Y-Z\equiv0\), contradicting the third.

This is a necessary-phase contradiction for **arbitrary nonzero complex entries**. It does not assume equal moduli, nor infer complex impossibility from a real-sign failure. Thus no low-to-low edge exists in \(R_{34}\).

## 7. Forced global \(R_{34}\)

**SUPPORTED — S1 LF304–326.**

If one five-party were exceptional, it would have only one high symbol. A low symbol at the opposite party has two **distinct** residual neighbors, and neither may be low. Two distinct neighbors cannot be supplied by one high symbol. The symmetric exceptional orientation is equally impossible.

Both five-parties must therefore be ordinary, each with three lows of degree two and two highs of degree three.

Every low symbol must use both highs on the opposite side. Hence

\[
(L_3\times H_4)\sqcup(H_3\times L_4)\subseteq R_{34}.
\]

These sectors contain twelve edges and already saturate every high degree. There is no room for a high-to-high edge, and low-to-low edges have been excluded. Consequently,

\[
R_{34}=(L_3\times H_4)\sqcup(H_3\times L_4)
      =K_{3,2}\sqcup K_{2,3}.
\]

The sector totals are exactly \((0,6,6,0)\). This is forced for the hypothetical actual tensor, not asserted to be realizable.

## 8. Same-\(E\) incidence and all-low-slice contradiction

### 8.1 The incidence identity

**SUPPORTED — S1 LF332–362.**

For \(a\in A_1\), retain the author’s definitions of \(x(a)\) and \(u(a)\). Under the forced \(R_{34}\),

\[
w_3\in L_3\quad\Longleftrightarrow\quad w_4\in H_4
\qquad(w\in E).
\]

Count the same residual words containing \(a\). Each used \(13\)-pair contributes exactly two words, as does each used \(14\)-pair. Thus

\[
2x(a)=2u(a).
\]

This equality uses the same \(E\); equality of unrelated graph degrees would not suffice.

Since \(a\) has three party-3 neighbors and only two high party-3 symbols are available,

\[
x(a)\ge1.
\]

Since \(H_4\) has two symbols,

\[
u(a)\le2.
\]

Therefore

\[
1\le x(a)=u(a)\le2.
\]

Counting \(R_{13}\)-edges incident to the three low party-3 symbols gives

\[
\sum_{a\in A_1}x(a)=3\cdot2=6.
\]

### 8.2 Exhaustion of low-slice types

**SUPPORTED — S1 LF364–371.**

A low party-3 slice has four distinct words and three balanced partitions at parties 1, 2 and 4. All three partitions cannot coincide, since that would duplicate tensor words.

If \(1=4\), a common partition block gives a distance-one pair varying at party 2. If \(2=4\), it gives one varying at party 1. Both are excluded.

Exactly the author’s two possibilities remain:

- **A:** all three partitions differ.
- **D:** the party-1 and party-2 partitions coincide.

No partition case is omitted.

### 8.3 Type D is impossible

**SUPPORTED — S1 LF373–390.**

The two party-4 neighbors of any low \(\ell\) are exactly the two high symbols \(h,h'\). A type-D slice contains a distance-one pair varying between them.

Both high symbols have degree three. The twin corollary makes their party-1 neighbor sets identical, each of size three. Since \(|A_1|=4\), the author’s existentially defined symbol \(a_0\) lies outside both neighbor sets. Hence

\[
u(a_0)=0,
\]

contradicting the established lower bound.

This applies the degree-three corollary only after ordinary profiles have been established.

### 8.4 All type-A slices are impossible

**SUPPORTED — S1 LF392–407.**

Two different balanced partitions of a four-element set cross with intersection size one. Thus, in a type-A slice, each party-1 neighbor occurs once with each party-4 neighbor.

Every \(a\in A_1\) has a low party-3 neighbor because \(x(a)\ge1\). Since every low slice is now type A, every such \(a\) is adjacent to both high party-4 symbols:

\[
u(a)=2.
\]

The same-\(E\) identity gives \(x(a)=2\) for all four symbols, and therefore

\[
\sum_{a\in A_1}x(a)=8,
\]

contrary to the independently established total six. This completes the regular-subregime contradiction.

## 9. Acceptance boundary and residual problem

The supported conclusion is exactly

\[
\begin{gathered}
\text{one actual complex }U,\quad
U^{12\mid34},U^{13\mid24},U^{14\mid23}\text{ unitary},\\
|\operatorname{supp}U|=48,\quad |P|=24,\quad q=(4,4,5,5)
\end{gathered}
\]

implies that **at least one four-symbol party is not degree-three regular**.

Within the supplied four-party profile list, the proof eliminates only \((D_0,D_0)\). The other listed pairs remain subject to their prior exact F/S and marked-graph restrictions, including S3 where applicable; they are not asserted feasible.

The author correctly identifies the first missing bridge outside this scope. Without both four-parties regular, \(M_{12}\) need not be a perfect matching, so identical twin neighborhoods need not yield Lemma 2’s contradiction. Degree-four symbols also fall outside the two-degree-three twin corollary. The present argument does not close those cases.

Accordingly, this review does not establish:

- A whole-\(4455\) exclusion.
- A universal \(t=24\) or support-\(48\) exclusion.
- Exclusions for \(3555,4555,5555\).
- A physical tensor or complete realizable \(P,E\).
- \(N\ge49\), an exact support minimum, worldwide novelty, independent-family/human review or kernel verification.

## 10. Execution and delivery status

- **Scientific code prepared:** none.
- **Scientific execution:** **NOT RUN**; outside this WRITTEN assignment.
- **New selected instances/private probes:** none.
- **Builds/tests/lint/formatters:** not run.
- **Child-native clock/hash commands:** not executed.
- **Runtime, memory, exit status or scientific stdout:** none claimed.
- **Working-tree changes:** none; this complete body is returned for Main materialization.
- **External-model CLI, paid run, installation, deletion, credentials or Git mutation:** none.
- **Independent-family, human, formal-kernel or novelty clearance:** not performed.

**Final disposition: SUPPORTED, with 0 FATAL / 0 MAJOR / 0 MINOR, for the entire actual complex \(4455\) subregime with both four-symbol parties degree-three regular. Parent adoption remains a separate decision; full \(4455\) and global support-minimum questions remain open.**