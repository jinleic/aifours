# author-candidate-v1.md

## F482: exclusion of the entire regular-four-party \(4455\) subregime

**Role:** GENERAL AUTHOR  
**Status:** **COMPLETE WRITTEN AUTHOR CANDIDATE — UNREVIEWED, NOT ADOPTED.**  
**Scientific execution:** **NOT RUN.** No program was prepared or executed.

### Main result

Let \(U=6\psi\in(\mathbb C^6)^{\otimes4}\) have three unitary balanced flattenings, exactly \(48\) nonzero entries, and exactly \(24\) entries of modulus one. Suppose its residual coordinate-alphabet sizes are
\[
(q_1,q_2,q_3,q_4)=(4,4,5,5).
\]

Then the following additional hypothesis is impossible:
\[
r_1(a)=r_2(b)=3
\qquad
(a\in A_1,\ b\in A_2).
\]

Thus **the whole \(4455\) subregime in which both four-symbol parties are degree-three regular is excluded**, for arbitrary nonzero complex phases and residual moduli. This includes both maximal-word regimes F and S, and does not assume no-OLS or no-distance-one.

The proof uses the same \(P,E\), exact two-extension multiplicities, and actual unitary block closure in all three cuts. It does not promote a missing graph or a slice shadow to a physical support.

The full \(4455\) class, all support \(48\), and the original support-minimum problem remain unresolved.

---

## 1. Actual common-tensor interface

Write
\[
P=\{w:|U_w|=1\},\qquad
E=\{w:0<|U_w|<1\},
\]
so that
\[
|P|=|E|=24.
\]
Let
\[
A_i=\pi_i(E),\qquad |A_i|=q_i.
\]

A modulus-one entry exhausts its row and column in every balanced flattening. Removing the \(24\) maximal rows and columns therefore leaves a \(12\times12\) unitary with \(24\) residual nonzeros. No residual row or column can have only one nonzero: that entry would itself have modulus one. Consequently every residual row and column has exactly two nonzeros.

For every physical pair \(ij\), therefore,
\[
R_{ij}:=\pi_{ij}(E)
\]
has \(12\) elements, every element has exactly two \(E\)-extensions, and
\[
\pi_{ij}(P)=[6]^2\setminus R_{ij}
\]
injectively.

For \(a\in A_i\), put
\[
p_i(a)=|\{w\in P:w_i=a\}|.
\]
Counting maximal pairs containing \(a\) gives the partner-independent degree
\[
r_i(a)=6-p_i(a).
\]
Its residual-word multiplicity is \(2r_i(a)\), and
\[
\sum_{a\in A_i}r_i(a)=12.
\]
Also \(r_i(a)\ge2\): if it were one, the two residual words containing \(a\) would have the same unique neighbor at every other coordinate and would coincide.

### Actual block closure

In a residual flattening, two rows sharing one column cannot have only that overlap, since their inner product would be nonzero. They must share their other column as well. Thus every residual flattening is a disjoint union of six full nonzero \(2\times2\) unitary blocks.

This condition is used below, rather than merely the degrees of the support graph.

---

## 2. The five-symbol degree profiles needed in the proof

For completeness, the relevant profile classification follows directly from the common maximal set.

For \(w\in P\), let \(k(w)\) be its number of internal coordinates and \(n_s\) the number with \(k(w)=s\). The first two internal-coordinate moments are
\[
\sum_{w\in P}k(w)=6(4+4+5+5)-48=60
\]
and
\[
\sum_{w\in P}\binom{k(w)}2
=\sum_{i<j}q_iq_j-72=49.
\]
Since
\[
\binom{s}{2}-2s+3=(3,1,0,0,1)
\quad(s=0,1,2,3,4),
\]
we obtain
\[
3n_0+n_1+n_4=49-2(60)+3(24)=1.
\]
In particular, there is at most one one-internal maximal word.

Fix a symbol \(a\) at a five-symbol party. Let \(\sigma(a)\) indicate that it is the internal symbol of that one-internal word, let \(\tau(a)\) count maximal triples containing it, and let \(f(a)\) indicate membership in the four-internal word. Counting other internal coordinates among its maximal words gives
\[
13-3r(a)
=
(6-r(a))-\sigma(a)+\tau(a)+2f(a),
\]
or
\[
\tau(a)+2f(a)-\sigma(a)=7-2r(a). \tag{2.1}
\]

If \(\sigma(a)=0\), nonnegativity implies \(r(a)\le3\). If \(\sigma(a)=1\), it implies \(r(a)\le4\). At most one symbol, at at most one party, can receive this exception.

Since five degrees at least two sum to twelve, each five-symbol party consequently has profile
\[
(3,3,2,2,2),
\]
except that at most one may have
\[
(4,2,2,2,2).
\]

Call degree-two symbols **low** and the other residual symbols **high**. An ordinary five-symbol party has three low and two high symbols; an exceptional one has four low and one high.

---

## 3. A new cross-slice invariant: the twin-overlap graph

### Lemma 1 — Twin-overlap bipartiteness

Suppose two residual words differ at exactly one coordinate \(i\), using distinct symbols \(a,a'\) there.

Let
\[
V_a=\{v:(a,v)\in E\},\qquad
V_{a'}=\{v:(a',v)\in E\},
\]
where \(v\) denotes the other three coordinates, and set
\[
T=V_a\cap V_{a'}.
\]

Then \(T\) carries a nonempty simple cubic bipartite graph. Its three edge colors correspond to equality at each of the other three coordinates.

#### Proof

For another coordinate \(j\), every used pair \((a,x_j)\) has exactly two residual extensions. Thus the elements of \(V_a\) with a fixed \(j\)-coordinate form a pair.

Take \(v\in T\). In the flattening
\[
ij\mid kl,
\]
the rows \((a,v_j)\) and \((a',v_j)\) share the column \((v_k,v_l)\). Actual \(2\times2\) block closure forces their other nonzero columns to agree. Hence the other element of the \(j\)-coordinate pair through \(v\) also belongs to \(T\).

Doing this for all three coordinates defines three perfect matchings on \(T\).

Two distinct elements of \(T\) cannot share two of their three coordinates: otherwise the corresponding physical pair would have the four distinct residual extensions
\[
(a,v),\ (a',v),\ (a,v'),\ (a',v'),
\]
contrary to exact multiplicity two. Therefore the three matching edges at each vertex are distinct, and their union is a simple cubic graph.

Now define the nonzero complex number
\[
z_v=U_{a,v}\,\overline{U_{a',v}}.
\]
If \(v,v'\) are joined by a matching edge, the corresponding two rows form a full unitary \(2\times2\) block. Their orthogonality says exactly
\[
z_v+z_{v'}=0.
\]
Thus \(z\) changes sign on every edge. An odd cycle would force a nonzero \(z_v\) to equal its negative. No odd cycle exists, so the graph is bipartite. ∎

### Corollary 1 — A varying low symbol cannot occur in a distance-one pair

If \(r_i(a)=2\), no residual word containing \(a\) can have a residual distance-one partner differing only at coordinate \(i\).

Indeed, \(T\subseteq V_a\) would have at most four vertices, whereas a simple cubic bipartite graph has at least three vertices in each part.

This is a consequence of actual complex orthogonality, not an imposed no-distance-one assumption.

### Corollary 2 — Degree-three twins have identical residual neighborhoods

If the two varying symbols both have residual degree three, then
\[
V_a=V_{a'}=T,
\]
and their residual neighbor sets agree at every other coordinate.

Indeed, both slices have six words. Lemma 1 requires at least six common words, so all six coincide. The twin-overlap graph is necessarily \(K_{3,3}\).

---

## 4. Consequence of regularity at the two four-symbol parties

Assume henceforth that both four-symbol parties are degree-three regular.

Then
\[
M_{12}:=(A_1\times A_2)\setminus R_{12}
\]
is a perfect matching: every vertex has missing degree \(4-3=1\).

### Lemma 2 — No residual distance-one pair varies at party 1 or 2

Suppose two residual words differed only at party \(1\), using \(a,a'\). Both symbols have degree three. Corollary 2 would give identical \(R_{12}\)-neighbor sets for \(a,a'\).

Their unique missing party-\(2\) neighbor would then be the same symbol, giving that vertex missing degree at least two in \(M_{12}\). This contradicts the perfect-matching property.

The argument for party \(2\) is identical. ∎

Distance-one pairs at parties \(3\) or \(4\) have not been globally prohibited.

---

## 5. A low-to-low edge would force an impossible binary phase subsystem

### Lemma 3 — No low-to-low edge in \(R_{34}\)

Under the regular-four-party hypothesis,
\[
R_{34}\cap(L_3\times L_4)=\varnothing.
\]

#### Proof

Suppose \((\ell,m)\in R_{34}\), where both symbols have degree two. Its two residual extensions agree at parties \(3,4\). By Lemma 2, they cannot differ only at party \(1\) or only at party \(2\). Therefore they differ at both:
\[
(a,b,\ell,m),\qquad(a',b',\ell,m),
\]
with \(a\ne a'\), \(b\ne b'\).

The four words through \(\ell\) use two symbols twice at each of parties \(1,2,4\), giving three balanced \(2+2\) partitions of a four-element word set. They cannot all coincide, since that would duplicate tensor words.

Because the two words through \((\ell,m)\) differ at both \(1,2\), this slice has either:

1. three different partitions; or
2. equal party-\(1\) and party-\(2\) partitions, different from the party-\(4\) partition.

The second alternative would include
\[
(a,b,\ell,m),\qquad(a,b,\ell,n)
\]
for another \(n\), a distance-one pair varying at party \(4\) and involving the low symbol \(m\). Corollary 1 excludes it. Thus the three partitions in the \(\ell\)-slice are all different.

The same argument shows that the three partitions in the \(m\)-slice are all different.

Relabel the two values at each coordinate by \(0,1\), with \(\ell=m=0\). These two slices then contain
\[
0000,\quad1100,\quad0101,\quad1001,
\]
and
\[
0000,\quad1100,\quad0110,\quad1010.
\]

Block closure in the cut \(13\mid24\) forces the remaining words
\[
1111,\qquad0011.
\]
For example, the row through \(0000,0101\) and the column through \(0000,1010\) force \(1111\).

Thus all eight even-parity binary words occur:
\[
0000,\ 0011,\ 0101,\ 0110,\
1001,\ 1010,\ 1100,\ 1111. \tag{5.1}
\]

These eight words already provide exactly two extensions for each of their physical pairs, so the blocks used next are genuine closed residual blocks.

Write their entry phases as \(\theta_w\), and put
\[
X=\theta_{0000}+\theta_{1111},\quad
Y=\theta_{0011}+\theta_{1100},\quad
Z=\theta_{0101}+\theta_{1010}.
\]

For a nonzero unitary block with entries arranged as
\[
\begin{pmatrix}u&v\\w&x\end{pmatrix},
\]
orthogonality requires
\[
\arg u-\arg v-\arg w+\arg x\equiv\pi\pmod{2\pi}.
\]

Three actual blocks of (5.1), one in each cut, therefore give
\[
\begin{aligned}
X-Y&\equiv\pi &&\pmod{2\pi},\\
X-Z&\equiv\pi &&\pmod{2\pi},\\
Y-Z&\equiv\pi &&\pmod{2\pi}.
\end{aligned} \tag{5.2}
\]
The first two imply \(Y-Z\equiv0\), contradicting the third.

Equivalently, the first equation minus the second plus the third has identically zero left side and right side \(\pi\) modulo \(2\pi\). This contradiction allows arbitrary complex phases and does not depend on equal residual moduli. ∎

---

## 6. Forced common \(R_{34}\) structure

If one five-symbol party had the exceptional profile, say party \(3\), it would have only one high symbol. Every low party-\(4\) symbol has two distinct residual neighbors. Lemma 3 would require both to lie among that single high symbol, which is impossible.

Thus both five-symbol parties are ordinary:
\[
(3,3,2,2,2).
\]

Every low symbol must use both high symbols at the other party. Consequently
\[
R_{34}
=
(L_3\times H_4)\ \sqcup\ (H_3\times L_4). \tag{6.1}
\]
Indeed, these two complete bipartite sectors already give every high symbol its full degree three. There are no high-to-high edges.

So the earlier matching parameter is not merely bounded in this actual regular subregime: actual block closure and phases would force
\[
m=0,\qquad
(LL,LH,HL,HH)=(0,6,6,0).
\]
The following argument shows that even this forced common graph cannot extend to the required tensor.

---

## 7. Synthesis of all low slices: final contradiction

Fix \(a\in A_1\), and define
\[
x(a)=|\{\,\ell\in L_3:(a,\ell)\in R_{13}\,\}|,
\]
\[
u(a)=|\{\,h\in H_4:(a,h)\in R_{14}\,\}|.
\]

By (6.1), an \(E\)-word has party \(3\) low if and only if its party \(4\) is high. Counting those residual words containing \(a\), first through their \(13\)-pair and then through their \(14\)-pair, gives
\[
2x(a)=2u(a),
\qquad\text{hence}\qquad x(a)=u(a). \tag{7.1}
\]

The total \(R_{13}\)-degree of \(a\) is three, but \(H_3\) has only two symbols, so
\[
x(a)\ge1.
\]
Also \(H_4\) has only two symbols, so
\[
u(a)\le2.
\]
Therefore
\[
1\le x(a)=u(a)\le2. \tag{7.2}
\]

Summing the low-side degrees gives
\[
\sum_{a\in A_1}x(a)=3\cdot2=6. \tag{7.3}
\]

Now consider an arbitrary low symbol \(\ell\in L_3\). Its four-word slice again induces three balanced partitions at parties \(1,2,4\).

If the equal partitions were \(1=4\), the slice would contain a distance-one pair varying at party \(2\). If they were \(2=4\), it would contain one varying at party \(1\). Lemma 2 excludes both alternatives.

Hence only two slice types remain:

- **A:** all three partitions differ;
- **D:** the party-\(1\) and party-\(2\) partitions agree.

### Type D is impossible

By (6.1), the two party-\(4\) neighbors of \(\ell\) are exactly the two high symbols \(h,h'\). A type-D slice has the form
\[
(a,b,\ell,h),\quad(a,b,\ell,h'),\quad
(a',b',\ell,h),\quad(a',b',\ell,h').
\]
It contains a distance-one pair varying between \(h,h'\).

Both high symbols have degree three. Corollary 2 therefore says their party-\(1\) residual neighbor sets are identical, each of size three.

Since \(|A_1|=4\), there is a symbol \(a_0\in A_1\) adjacent to neither \(h\) nor \(h'\). Thus
\[
u(a_0)=0,
\]
contradicting (7.2).

So **every low party-\(3\) slice is type A**.

### All type-A slices are also impossible

In a type-A slice, every party-\(1\) neighbor occurs once with each of the two party-\(4\) neighbors. Thus whenever \(a\) is adjacent to a low \(\ell\), it is adjacent to both high party-\(4\) symbols.

Every \(a\) has at least one such low neighbor by (7.2). Consequently
\[
u(a)=2
\qquad(a\in A_1).
\]
Equation (7.1) gives \(x(a)=2\) for all four symbols. Hence
\[
\sum_{a\in A_1}x(a)=8,
\]
contradicting (7.3).

This completes the proof. ∎

---

## 8. Exact scope of the advance

The proved author implication is
\[
\begin{gathered}
\text{one actual complex }U,\quad
U^{12\mid34},U^{13\mid24},U^{14\mid23}\text{ unitary},\\
|\operatorname{supp}U|=48,\quad |P|=24,\quad(q_i)=4455
\\[2mm]
\Longrightarrow
\text{at least one four-symbol party is not degree-three regular}.
\end{gathered}
\]

Within the adopted four-party degree list
\[
D_0=(3,3,3,3),\qquad
D_1=(4,3,3,2),\qquad
D_2=(4,4,2,2),
\]
the pair \((D_0,D_0)\) is excluded. Up to exchanging the two four-symbol parties, the remaining profile pairs are
\[
(D_0,D_1),\quad(D_0,D_2),\quad
(D_1,D_1),\quad(D_1,D_2),\quad(D_2,D_2),
\]
subject to the previously adopted F/S and marked-graph restrictions.

No claim is made that these remaining profiles are realizable.

### First unproved step outside the excluded subregime

The regular proof rejects residual distance-one pairs at parties \(1,2\) by combining the twin-overlap invariant with the perfect-matching property of \(M_{12}\).

For the nonregular profiles, \(M_{12}\) need not be a perfect matching. Identical residual neighbor sets need not produce the contradiction used in Lemma 2; degree-four symbols also permit larger twin-overlap components. The present proof does not eliminate those cases.

Thus the remaining task is actual common-\(P,E\) compatibility, three-cut block closure and complex phase consistency in the nonregular profiles—not completion of an independently chosen low-slice shadow.

---

## 9. What is new here, and what is not claimed

The additional written results beyond the frozen necessary-condition ledger are:

1. **Twin-overlap invariant:** a distance-one residual pair generates a simple cubic bipartite graph on its common three-coordinate slice.
2. **Low-symbol prohibition:** a distance-one pair cannot vary through a degree-two symbol.
3. **Derived regular-party prohibition:** distance-one residual pairs cannot vary at either four-symbol party when both are degree-three regular.
4. **Three-cut phase obstruction:** a low-to-low \(R_{34}\) edge in that regular stratum forces an inconsistent eight-word binary phase subsystem.
5. **Whole-subregime exclusion:** the remaining forced \(R_{34}=K_{3,2}\sqcup K_{2,3}\) cannot satisfy all low slices of the same tensor.

“Additional” refers to this frozen assignment, not worldwide novelty. No literature-priority claim is made.

In particular, this return does **not**:

- exclude the entire \(4455\) class;
- construct a physical tensor or complete candidate \(P,E\);
- exclude \(3555,4555,5555\);
- prove a universal \(t=24\) exclusion;
- exclude every support-\(48\) tensor;
- prove \(N\ge49\) or an exact product-basis support minimum;
- treat a failure of real signs as a failure of arbitrary complex phases.

The phase contradictions above are explicit congruence contradictions over arbitrary complex phases.

---

## 10. Frozen inputs, access chronology and attribution

### Assigned bindings

All following hash, byte-count and clock observations are **parent-attributed**, not child-executed measurements.

- Manifest SHA-256:  
  `ce83a237d3942e68db9f5fdcb05516bf72bb13ffb1288929f01018c5bb74a386`
- Freeze-receipt SHA-256:  
  `9789e0d147c50f3dede9481ebdfbc3f479cbde1269f52cc2c80aa9af310fcdec`
- Literal-packet SHA-256:  
  `18d39676590f166eb61f456ea4a79aac01c06e683ecf5288d672d9178b2cecda`

The parent supply reports manifest \(7168\) bytes/\(117\) LF, receipt \(2369\) bytes/\(60\) LF, and packet \(48396\) bytes/\(802\) LF. Its clock observation is **2026-10-30T12:13:16-0700 PDT**. This is not asserted to be my native start, checkpoint or completion time.

### Actual sequence

Before mathematical work, I read:

1. the mandatory memory summary and written-math acceptance skill;
2. the complete manifest, including the initially truncated research-task line through a separate raw read;
3. the complete freeze receipt;
4. all ten permission/status controls;
5. the parent live metadata supply and dispatch receipt.

I then delivered the **pre-body ACK to Main**, before opening the mathematical packet or doing new mathematics.

After that ACK, I read the literal packet sequentially in raw windows of at most twenty LF, covering its complete \(1\)–\(802\) lines and its ending:

- S1: logical lines \(1\)–\(38\);
- S2: logical lines \(1\)–\(735\);
- S3: logical lines \(1\)–\(27\).

Only after that complete packet reading did I develop the twin-overlap and regular-subregime proof above.

### Source boundaries

The scientific inputs were the frozen actual-\(4455\) disposition and full f433 author body. The \(4445\) disposition was read as the assigned nontransferable analogy, not used as a theorem about \(4455\).

The f460 refinement mentioned in S1 remains **unadopted** and was not used. Its report, program and linked reviews were not followed.

No local source links inside the packet were followed. No new public source was opened; the proof invokes no external no-AME theorem.

All quarantine controls were used only for permissions and status. No held mathematical payload, held consumer, sibling result or unassigned code was opened or used. This records actual access and use, not a certificate of cognitive isolation.

---

## 11. Proof, experiment and acceptance status

- **Scientific work:** written combinatorics, actual block-closure arguments and exact complex orthogonality.
- **Scientific code prepared:** none.
- **Scientific execution:** **NOT RUN**.
- **Enumeration, solver or CAS:** not used.
- **Builds/tests/lint/formatters:** not run.
- **Working-tree writes:** not attempted under the read-only runtime; this complete body is returned for Main materialization.
- **Child-native clock/hash commands:** not executed.
- **Measured runtime, memory, exit status or stdout:** none claimed.
- **Independent reconstruction:** not performed in this child.
- **Parent disposition:** not yet obtained.
- **Independent-family, human or kernel verification:** not performed.
- **Novelty/priority clearance:** not performed.

There is no omitted executable source or experimental output. The proof body above contains the complete load-bearing argument, including the explicit phase inconsistency.

**Final status: COMPLETE GENERAL-AUTHOR PROOF CANDIDATE EXCLUDING THE ENTIRE REGULAR-FOUR-PARTY \(4455\) SUBREGIME; UNREVIEWED, NOT ADOPTED; FULL \(4455\) AND GLOBAL SUPPORT-MINIMUM QUESTIONS REMAIN OPEN.**