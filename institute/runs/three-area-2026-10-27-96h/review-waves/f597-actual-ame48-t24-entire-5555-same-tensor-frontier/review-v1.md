# author-candidate-v1.md

## Entire actual \(5555\) residual profile: a direct common-\(P\) contradiction

**Status:** GENERALAUTHOR candidate; complete written proof supplied below, **not independently reviewed or parent-adopted**. No scientific execution was performed. This body is returned for Main materialization; no repository file was written.

### Claimed theorem

There is no complex tensor \(U=6\psi\) satisfying all of the following:

1. Its three balanced \(36\times36\) flattenings are unitary.
2. Its support has exactly \(48\) entries.
3. Exactly \(24\) entries have modulus \(1\).
4. The remaining \(24\) entries use exactly five symbols at each physical party.

The contradiction uses the **same actual residual support \(E\)**, the **same actual maximal support \(P\)**, all six physical pair projections, and orthogonality of the original nonzero complex amplitudes. It uses no no-OLS(6) import, no assumed absence of distance-one pairs, no equal-modulus hypothesis, and no real-sign restriction.

The principal new reduction is:

> The \(5555\) hypotheses force exactly two disjoint, saturated degree-three twin components. Their remaining-party alphabets together exhaust the five residual symbols. Consequently all four maximal pairs between the two twin coordinates would have to use the same complementary outside pair, contradicting pair injectivity of \(P\).

---

## 1. Inputs, chronology, and execution boundary

The scientific inputs were exactly the three complete sources in the frozen f597 packet:

- **S1:** `physics-6-ame48-t24-alphabet-shadow-and-complex-external-partner-parent-v1.md`, LF1–28; SHA256 `1e93cfc6ff428aefbf4eb301eba7cfd6fd9b14c62a0dca254b231e41ccadc055`.
- **S2:** `physics-6-ame48-t24-composed-no-distance-one-and-six-symbol-parent-v1.md`, LF1–18; SHA256 `3c37fb8e669de19d50317b08d363ca40165fd1817174acf1ed6e799d4558c99c`.
- **S3:** `physics-6-actual-ame48-t24-entire-4455-profile-exclusion-parent-v1.md`, LF1–49; SHA256 `faadf4777ac1b3f0e57d484624080a08835c9d71de980b87ad823866531f3bb4`.

The manifest, all thirteen listed controls, freeze receipt, dispatch receipt, and parent-supplied metadata were read through their endings before the direct pre-body ACK to `agent://Main`. The literal packet was then read in ordered raw ranges LF1–20, 21–40, 41–60, 61–80, and 81–97, through its ending, before mathematical derivation.

The manifest and receipt pins are the supplied parent observations, not independently recomputed child hashes:

- Manifest: `0e9e16ae2ebd6bf6a08c6b44f3cc032c6cde87f4982fba17a96c033b12884cb6`.
- Receipt: `e459b1575ddbfa466a817bfedbb0448bc9d420545c4e98f563063d70d4397a91`.

No linked scientific source, f596 sibling, held scientific episode, or held consumer was opened or used. In particular, no f586 scientific content was imported. No code, enumeration, solver, numerical probe, new selected example, external-model call, or public-source follow was used. The binary labels below are a universal normal form for the actual extensions of an arbitrary hypothesized low-low pair, not a separately chosen example.

S3 supplies the relevant twin/low-low proof architecture, but its \(4455\)-specific degree arguments are **not** transferred. The \(5555\) bounds and every step used here are derived below. S2’s conditional no-distance-one conclusion is not invoked.

These statements describe the observed read/tool record and the derivation presented here, not a clean-cognition certificate.

---

## 2. The same actual \(P/E\) interface

Write the four physical coordinates as \(1,2,3,4\). Let

\[
P=\{w:|U_w|=1\},\qquad
E=\{w:0<|U_w|<1\}.
\]

Both sets have size \(24\).

A modulus-one entry exhausts the norm of its row and column in every balanced flattening. Therefore:

- Every physical pair projection of \(P\) is injective.
- No entry of \(E\) uses a physical pair value appearing in \(P\).
- At each physical pair \(ij\), the remaining \(12\) pair values are exactly
  \[
  R_{ij}=\pi_{ij}(E).
  \]

In a balanced flattening, the \(12\) remaining rows each require at least two residual entries: a singleton would have modulus one. There are exactly \(24\) residual entries, so every residual row has exactly two entries. The same argument applies to columns.

Thus every value in every \(R_{ij}\) has **exactly two extensions in \(E\)**.

Moreover, two residual rows sharing a column must share their other column. Otherwise their inner product has exactly one nonzero term. Hence every residual flattening is six full nonzero \(2\times2\) blocks. This is a statement about the actual support and actual unitary flattenings, not independent cut graphs.

For each party \(i\), let \(A_i\) be its residual alphabet. Here

\[
|A_i|=5,\qquad [6]\setminus A_i=\{o_i\}.
\]

For \(a\in A_i\), let \(r_i(a)\) be its number of neighbors in \(R_{ij}\). Its residual occurrence count is \(2r_i(a)\), so \(r_i(a)\) is independent of \(j\). Also

\[
\sum_{a\in A_i}r_i(a)=12.
\]

We have \(r_i(a)\ge2\). Indeed, if \(r_i(a)=1\), there is only one possible residual neighbor at each of the other three coordinates. The supposed two occurrences of \(a\) would therefore be the same word.

Since five integers at least two sum to twelve, the only degree profiles are

\[
\boxed{(3,3,2,2,2)}
\quad\text{or}\quad
\boxed{(4,2,2,2,2)}.
\]

Call these **ordinary** and **exceptional**, respectively. A degree-two symbol is **low**; a degree-three or degree-four symbol is **high**.

Finally, pair complementarity gives the maximal occurrence count

\[
p_i(a)=6-r_i(a).
\]

For the outside symbol, \(p_i(o_i)=6\).

---

## 3. Exact \(5555\) maximal-word moments and outside footprints

For \(w\in P\), let

\[
k(w)=|\{i:w_i\in A_i\}|,\qquad
n_k=|\{w\in P:k(w)=k\}|.
\]

At party \(i\),

\[
\sum_{a\in A_i}p_i(a)=5\cdot6-12=18.
\]

Consequently

\[
C=\sum_{w\in P}k(w)=4\cdot18=\boxed{72}.
\]

At each physical pair \(ij\), precisely \(25-12=13\) maximal pair values are internal to \(A_i\times A_j\). Therefore

\[
M=\sum_{w\in P}\binom{k(w)}2
=6\cdot13=\boxed{78}.
\]

Together with \(\sum n_k=24\), these yield

\[
3n_0+n_1+n_4=6,
\qquad
n_4=3n_0+2n_1+n_2.
\]

There is exactly one maximal word using each outside pair \((o_i,o_j)\). A word with \(k\) internal coordinates covers \(\binom{4-k}{2}\) outside pairs, so

\[
6n_0+3n_1+n_2=6.
\]

Two words with \(k=1\) would each have three outside coordinates. Their outside-coordinate sets intersect in at least two coordinates, duplicating an outside pair. Thus

\[
\boxed{n_1\le1}.
\]

If the all-outside word is present, it exhausts all six outside pairs, so \(n_0=1\) forces \(n_1=n_2=0\). The complete list of moment/outside-footprint possibilities is consequently

\[
\begin{array}{c|rrrrr}
&n_0&n_1&n_2&n_3&n_4\\ \hline
\mathrm{A}&1&0&0&20&3\\
\mathrm{B}&0&0&6&12&6\\
\mathrm{C}&0&1&3&15&5
\end{array}
\]

These are necessary histograms, not realizability claims.

### Exact local outside occupancy

Fix \(a\in A_i\), and let \(m_h(a)\) count maximal words containing \(a\) with exactly \(h\) outside coordinates among the other three parties. The three pairs \((a,o_j)\), \(j\ne i\), each occur once in \(P\). Hence

\[
\sum_{h=0}^3m_h(a)=6-r_i(a),\qquad
\sum_{h=0}^3h\,m_h(a)=3.
\]

Equivalently,

\[
r_i(a)=3-m_0(a)+m_2(a)+2m_3(a).
\]

In particular, an exceptional degree-four symbol has exactly two maximal occurrences. Their outside occupancies must be

\[
\boxed{\{0,3\}\ \text{or}\ \{1,2\}}.
\]

Thus every exceptional party requires an actual maximal word with at least two outside coordinates. Regime A has no such word containing an internal symbol, so all parties are ordinary there.

No \(4455\)-specific “at most one exceptional party” assertion is used. The contradiction below covers every histogram and every allowable placement of exceptional parties.

---

## 4. Saturated-twin lemma, derived for \(5555\)

### Lemma 1

If two words of \(E\) differ only at coordinate \(i\), their two symbols at \(i\) are the degree-three high pair of an ordinary party. Their complete three-coordinate slices coincide and contain six triples.

Thus every distance-one pair belongs to a saturated twelve-word component

\[
C_i=\{a_i,a_i'\}\times T_i,
\qquad |T_i|=6.
\]

### Proof

Suppose \((a,t),(a',t)\in E\), where \(t\) is a triple on the other three coordinates.

For each \(j\ne i\), the residual rows \((a,t_j)\) and \((a',t_j)\) share a column in the \(ij\mid\{1,2,3,4\}\setminus\{i,j\}\) flattening. Actual \(2\times2\) closure forces the same second column. Hence the common slice

\[
T=S_a\cap S_{a'}
\]

is closed under three fixed-point-free matchings, one for equality at each of the three remaining coordinates.

These matchings have distinct edges. If two different-coordinate matchings paired the same triples, those triples would agree at two coordinates. Their two copies at \(a,a'\) would give four extensions of one physical pair, contrary to multiplicity two.

The resulting graph on \(T\) is therefore simple and cubic. Define the actual nonzero complex quantity

\[
z_t=U_{a,t}\,\overline{U_{a',t}}.
\]

Orthogonality of the two actual rows along every matching edge \(tt'\) gives

\[
z_t+z_{t'}=0.
\]

An odd cycle would force \(z_t=-z_t\), impossible. Thus the graph is bipartite. Every nonempty simple cubic bipartite graph has at least six vertices.

Every symbol slice has at most eight words, because \(r_i\le4\). Consequently \(|T|=6\) or \(8\).

If \(|T|=6\), it uses exactly three values at each remaining coordinate, each twice. A degree-four slice containing it would have two additional triples. At each coordinate, the three already used values are saturated; both additional triples must use the same fourth value. They would coincide, impossible. Thus both complete slices have size six.

If \(|T|=8\), both symbols would have degree four. That is incompatible with the \(5555\) degree profiles.

Therefore both symbols have degree three and their full slices equal \(T\), proving the lemma. ∎

In particular:

\[
\boxed{\text{No distance-one pair can vary through a low symbol.}}
\]

### Lemma 2

Twin components at different coordinates are word-disjoint. There are at most two twin coordinates.

### Proof

If a word belonged to twin components at coordinates \(i,j\), full saturation would allow both twin replacements independently. The resulting four words would have identical values at the complementary two coordinates, contradicting pair multiplicity two.

Each component has twelve words, whereas \(E\) has twenty-four. At a given party, the degree profiles allow at most one twin pair. Hence there are at most two twin coordinates. ∎

---

## 5. The low-low routing lemma, with an actual complex obstruction

### Lemma 3

For every residual low-low pair at coordinates \(i,j\), its two extensions differ at exactly one complementary coordinate. That coordinate is a twin coordinate.

### Proof

If the extensions differ at one coordinate, Lemma 1 gives the asserted twin.

Suppose instead they differ at both complementary coordinates. Relabel the four coordinates as \(i,j,k,\ell\), and write the two actual extensions as

\[
(a,b,c,d),\qquad(a,b,c',d'),
\]

where \(a,b\) are low, \(c\ne c'\), and \(d\ne d'\).

The four-word slice of \(a\) has two values, each occurring twice, at every other coordinate. Its equality partitions are perfect matchings on four words. The \(j\)-matching differs from the \(k\)- and \(\ell\)-matchings because the displayed extensions differ at both \(k,\ell\).

The \(k\)- and \(\ell\)-matchings cannot coincide: their common edge through a word with \(j=b\) would produce a distance-one pair varying through the low symbol \(b\), forbidden by Lemma 1. Thus all three matchings are distinct. The slice is forced to be

\[
(a,b,c,d),\quad(a,b,c',d'),\quad
(a,b',c,d'),\quad(a,b',c',d).
\]

The identical argument for the low \(b\)-slice forces

\[
(a',b,c,d'),\qquad(a',b,c',d)
\]

as well.

Actual block closure now forces

\[
(a',b',c,d),\qquad(a',b',c',d').
\]

For example, in the \(ik\mid j\ell\) cut, the row containing \((a,b,c,d)\) shares its \((b,d)\) column with the row containing \((a',b,c',d)\). Their other columns must coincide, forcing \((a',b',c',d')\); the other missing word follows symmetrically.

Under binary labels for these actual symbols, the eight words are exactly

\[
0000,\ 0011,\ 0101,\ 0110,\ 1001,\ 1010,\ 1100,\ 1111.
\]

Every pair value used by these words already has its two extensions within them. Thus their blocks are closed in all three actual flattenings.

Let \(u_\beta\ne0\) be their actual amplitudes and

\[
\epsilon_\beta=\frac{u_\beta}{|u_\beta|}.
\]

Define the nonzero unit complex products

\[
X=\epsilon_{0000}\epsilon_{1111},\quad
Y=\epsilon_{0011}\epsilon_{1100},\quad
Z=\epsilon_{0101}\epsilon_{1010}.
\]

Three actual row-orthogonality equations are

\[
u_{0000}\overline{u_{1100}}
+u_{0011}\overline{u_{1111}}=0
\qquad(ij\mid k\ell),
\]

\[
u_{0000}\overline{u_{1010}}
+u_{0101}\overline{u_{1111}}=0
\qquad(ik\mid j\ell),
\]

\[
u_{0011}\overline{u_{1010}}
+u_{0101}\overline{u_{1100}}=0
\qquad(i\ell\mid jk).
\]

Because both summands in each equation are nonzero, their normalized phases are negatives. These equations therefore imply

\[
X=-Y,\qquad X=-Z,\qquad Y=-Z.
\]

The last two give \(X=Y\), contradicting the first.

This uses actual complex orthogonality, without imposing equal residual moduli or real phases. The assumed two-coordinate difference is impossible. ∎

**Consumer consequence:** every low-low edge must route to a twin at one of its two complementary coordinates. In particular, if neither complementary coordinate is a twin coordinate, that low-low edge cannot exist.

---

## 6. The tensor must have exactly two twin coordinates

### Lemma 4: Zero twin coordinates are impossible

If there were no twins, Lemma 3 would forbid low-low edges in every \(R_{ij}\).

Every party has low symbols. A low symbol has two distinct neighbors at every other party, and both neighbors would have to be high. Hence every party must have at least two high symbols: every party is ordinary.

Between two ordinary parties, each of the three lows must meet both highs. These six edges exhaust the opposite highs’ total degree \(3+3=6\). Consequently

\[
R_{ij}=(L_i\times H_j)\ \dot\cup\ (H_i\times L_j),
\]

with no high-high or low-low edge.

But any residual word has four low/high statuses. At least two statuses agree, producing either a prohibited low-low or a prohibited high-high pair. Contradiction. ∎

### Lemma 5: Exactly one twin coordinate is impossible

Suppose \(i\) were the only twin coordinate. It is ordinary, with high pair \(H_i\) and three lows \(L_i\).

For every \(j\ne i\), a low-low edge in \(R_{ij}\) would require a twin at one of the other two coordinates. Hence \(R_{ij}\) has no low-low edge.

Each low at \(i\) therefore needs two highs at \(j\), forcing every other party to be ordinary. Degree saturation again gives

\[
R_{ij}=(L_i\times H_j)\ \dot\cup\ (H_i\times L_j).
\]

There are

\[
3\cdot(2\cdot2)=12
\]

residual words with their \(i\)-coordinate low. Every other coordinate of each such word is high.

Choose any two coordinates \(j,k\ne i\). These twelve words project into \(H_j\times H_k\), which has only four pair values. Multiplicity two permits at most eight such words, contradiction. ∎

Combining Lemmas 2, 4, and 5:

\[
\boxed{\text{There are exactly two twin coordinates.}}
\]

---

## 7. Two twins force the common-\(P\) collision

Let the twin coordinates be \(i,j\), and let \(k,\ell\) be the other two.

Their twelve-word components \(C_i,C_j\) are disjoint and exhaust \(E\):

\[
E=C_i\ \dot\cup\ C_j.
\]

The twin symbols are the high pairs \(H_i,H_j\). No residual word can contain both an \(H_i\)-symbol and an \(H_j\)-symbol, since it would belong to both components. Thus

\[
H_i\times H_j\ \cap\ R_{ij}=\varnothing.
\]

At coordinate \(k\), let \(B_k^i\) and \(B_k^j\) be the alphabets used by \(C_i\) and \(C_j\), respectively.

The six-triple common slice of a twin uses exactly three values at every other coordinate, each twice. Including both twin copies gives

\[
|B_k^i|=|B_k^j|=3,
\]

and each value occurs four times in its component.

Because the two components exhaust \(E\),

\[
B_k^i\cup B_k^j=A_k.
\]

Since \(|A_k|=5\),

\[
|B_k^i\cap B_k^j|=1.
\]

The shared symbol has eight residual occurrences and degree four; the other four symbols have four occurrences and degree two. Thus \(k\) is exceptional. The identical conclusion holds at \(\ell\). The forced residual degree-pattern arrangement is therefore

\[
\boxed{\text{ordinary, ordinary, exceptional, exceptional}}
\]

at \(i,j,k,\ell\), respectively.

Now take any \(a\in H_i\) and \(b\in H_j\). Since \((a,b)\notin R_{ij}\), actual maximal complementarity supplies a unique word

\[
w(a,b)\in P,\qquad w_i=a,\quad w_j=b.
\]

Its \(k\)-coordinate cannot belong to \(B_k^i\): every pair \((a,c)\) with \(c\in B_k^i\) is residual. Likewise, its \(k\)-coordinate cannot belong to \(B_k^j\), because every \((b,c)\) with \(c\in B_k^j\) is residual.

But

\[
B_k^i\cup B_k^j=A_k.
\]

Thus the only possible value is the unique outside symbol:

\[
w_k=o_k.
\]

The same argument gives \(w_\ell=o_\ell\). Therefore all four pairs in \(H_i\times H_j\) require the four distinct maximal words

\[
w(a,b)=(a,b,o_k,o_\ell).
\]

They all project to the same physical pair

\[
(o_k,o_\ell)
\]

at \(k\ell\), contradicting injectivity of \(\pi_{k\ell}(P)\).

This is a contradiction in the **same maximal support \(P\)**, using residual neighborhoods from the **same \(E\)**. No independently chosen complement or pair graph is substituted.

The theorem follows. ∎

---

## 8. Scope and verification disposition

### Supplied result

The complete written argument excludes the **entire fixed residual-alphabet profile \(5555\)** for an actual complex support-\(48\), \(t=24\) AME tensor. It covers:

- All three maximal-word histograms derived above.
- Every ordinary/exceptional degree placement.
- Arbitrary nonzero complex residual amplitudes.
- Actual distance-one configurations, rather than assuming them absent.
- The common-\(P\) completion constraint at all physical pairs.

The proof uses no classical no-OLS theorem. It does not construct a physical tensor or rely on rounding to one.

### Not claimed

This candidate does **not** establish:

- Exclusion of \(4555\).
- An unconditional complete list of residual profiles.
- Impossibility of every \(t=24\) tensor.
- Impossibility of all support-\(48\) tensors.
- A bound \(N\ge49\), the global AME support minimum, or anything about other maximal-entry counts.
- Novelty, worldwide priority, printed-source equivalence, independent-family, human, or formal/kernel verification.

### Execution and remaining acceptance work

**Scientific execution: NOT RUN.** No code or experiment was authored or executed; there are no numerical results or executable claims to replay.

There is no omitted mathematical lemma within the claimed fixed-profile proof. The remaining acceptance work is a disjoint written reconstruction, particularly of:

1. Saturation of every distance-one pair into a six-triple twin slice.
2. The low-low pair’s actual eight-word closure and its three complex orthogonality equations.
3. The zero-/one-twin exclusions and the two-component alphabet union.
4. The final dispatch from each \(H_i\times H_j\) maximal pair to the same complementary outside pair.

Until that reconstruction and parent disposition occur, this remains an **unadopted GENERALAUTHOR proof candidate**, not an accepted exclusion.