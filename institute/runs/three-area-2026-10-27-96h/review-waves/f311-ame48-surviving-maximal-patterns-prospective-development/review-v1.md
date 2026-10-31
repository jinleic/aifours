# f311 review-v1 — prospective mathematical development candidate

**UNREVIEWED AUTHOR CANDIDATE.** This is a development manuscript, not independent peer-review acceptance.

**Result:** At the adopted source boundary, the argument below excludes the entire \(N=48,t=27\) branch. It also classifies connected excess-four unitary support components and derives simultaneous-cut restrictions for \(t=28\), including an exact compatibility criterion for their two-term complex orthogonality equations.

**Remaining boundary:** \(t=24\) and \(t=28\) remain live. The adopted frontier remains unchanged until this candidate receives its required review. No support-48 exclusion, existence claim, or \(N\ge49\) conclusion is made.

**Self-findings:** 0 FATAL / 0 MAJOR / 0 MINOR detected.  
**Overall correctness:** correct at the explicitly stated candidate scope.  
**Confidence:** 0.93.

## 1. Administrative record and source dependence

The complete manifest, freeze receipt and all five status-only controls were read before mathematical packet access. The live hashes matched the assignment:

- Manifest: `cafdfff4fd8ae5a1fa52fec2ce7bfe43289ea6f0683e2e56e16ff9d5cbf60bdf`.
- Freeze receipt: `fc32b8153f136c06bcb7f1d640211b3a292e2d2a1430117e908146639ba4c6d2`.
- Literal packet: `91d55d66717730576e2af32f9327cab9f7b0145b503a5f29925e7a195cdf9c52`.

A PRE-BODY ACK was delivered to Main before mathematical packet reads, using the fresh native observation **2026-10-30T07:20:59-0700 PDT**. An initial attempt addressed to the nonexistent agent `parent` failed; the roster was used to find Main, and no failed delivery was represented as successful.

The entire ordered packet was read raw in windows of at most 20 LF: 1–20, 21–40, continuing consecutively through 381–400, then the ending at 401. Coverage was complete:

- S1: logical lines 1–36.
- S2: logical lines 1–266, with 265 LF and no terminal LF.
- S3: lines 1–62.
- S4: lines 1–18.
- S5: lines 1–17.

No displayed elision required recovery. All five source hashes matched their receipt pins at **2026-10-30T07:22:40-0700 PDT**.

Substantive checkpoint observations were **07:27:37** and **07:30:28 PDT**; the fresh observation before this return was **2026-10-30T07:31:57-0700 PDT**.

The attempt to write `reviewer-prebody-and-coverage-v1.md` in this wave was refused by the write tool’s filesystem restriction. No shell or other bypass was attempted. **No reviewer file or `review-v1.md` was created by me; this is the complete text for parent materialization.**

All new mathematics below is universally quantified. No selected tensor, support graph, parameter example, numerical probe, scientific code, CAS, solver, enumeration or replay was used. No external-model CLI was used. Quarantined payloads and their consumers were excluded.

### Exact mathematical imports

1. **S1 lines 7–18; S2 lines 65–127:** the residual unitary reduction, component squareness, minimum line degree two, the excess identity, and the adopted excess-zero/one/two results. These are imports, not new results of this duty.
2. **S5 line 5:** the quoted unitary-support Lemma D, whose connected positive-excess-three component is a full \(3\times3\) block. Its adopted provenance is retained. Its proof is not repeated here.
3. **S4 lines 7–10:** the adopted \(t=24\) no-distance-one/no-six-symbol conclusions retain their stated no-OLS(6) condition. They are not used to exclude \(t=27\) or \(t=28\).
4. **S1 lines 7–9 and S5 lines 3–9:** the existing branch boundary and its f113/classical provenance are retained.

The new \(t=27\) contradiction uses unitary-support consequences rather than a fresh classical OA contradiction. This observation does **not** remove the provenance qualifications of its adopted imports. The diagnostic descriptions in S5 line 15 are not premises or verification of this candidate.

---

## 2. Common setup

Let \(\psi\) be an arbitrary normalized complex AME\((4,6)\) state in a product basis, with exactly \(48\) nonzero coefficients. Write:

- \(P\) for the \(t\) words with coefficient modulus \(1/6\);
- \(E\) for the other support words;
- \(z_w=6\psi_w\) for every support word.

Every paired flattening of \(z\) is unitary. Every \(P\)-entry is an isolated unit-modulus entry in every paired cut. Deleting these entries and their rows and columns leaves, in each cut, a unitary support on

\[
n=36-t,\qquad |E|=48-t,\qquad e=|E|-2n=t-24.
\]

Every residual row and column has degree at least two. Distinct rows, or distinct columns, cannot overlap in exactly one nonzero position: their inner product would then contain one nonzero complex summand.

A pair value carried by \(P\) is never carried by \(E\). In every pair system, the \(t\) maximal words and the \(n\) residual pair values partition all \(36\) pair values.

No reality, equal-modulus or phase restriction is imposed.

---

## 3. Candidate theorem: the entire \(t=27\) branch is impossible

### Statement

**UNREVIEWED AUTHOR CANDIDATE.** At the adopted unitary-support import boundary, there is no normalized complex AME\((4,6)\) state with exactly \(48\) nonzero coefficients and exactly \(27\) coefficients of modulus \(1/6\).

### Proof

Assume such a state exists.

Then \(n=9\), \(|E|=21\) and \(e=3\). Since excess-one components are impossible, the adopted excess-three result implies that **each paired cut consists of one full \(3\times3\) component and three full \(2\times2\) components**.

Consequently, in each of the six pair systems:

- exactly three residual pair values have multiplicity three;
- exactly six residual pair values have multiplicity two.

For distinct parties \(i,j\), let

\[
H_{ij}
=
\{(a,b):\text{the residual pair value }(a,b)
\text{ has multiplicity }3\}.
\]

Thus \(|H_{ij}|=3\). In any paired cut \(ij\mid k\ell\), its full \(3\times3\) component is exactly

\[
H_{ij}\times H_{k\ell}.
\]

In particular, for every residual word \(w\),

\[
w_{ij}\in H_{ij}
\quad\Longleftrightarrow\quad
w_{k\ell}\in H_{k\ell}.
\tag{3.1}
\]

This is an assertion about the same support words in all three cuts.

### 3.1. High-pair incidence has partywise fixed marginals

For a symbol \(a\) at party \(i\), define

\[
p_i(a)=|\{w\in P:w_i=a\}|,\qquad
d_i(a)=6-p_i(a),\qquad
s_i(a)=|\{w\in E:w_i=a\}|.
\]

In every pair system \(ij\), the number of residual partner values at \(a\) is \(d_i(a)\): its other \(p_i(a)\) partner values are occupied exclusively by maximal words.

Counting extensions of these residual pair values gives

\[
s_i(a)
=
2d_i(a)+|\{b:(a,b)\in H_{ij}\}|.
\]

Therefore

\[
h_i(a):=s_i(a)-2d_i(a)
=
|\{b:(a,b)\in H_{ij}\}|
\tag{3.2}
\]

is independent of the other party \(j\). It is nonnegative, and

\[
\sum_a h_i(a)=3
\tag{3.3}
\]

for every party \(i\).

### 3.2. At most one party could have a high-pair incidence greater than one

Take any distinct parties \(i,j\), with remaining parties \(k,\ell\). The full core in the cut \(ik\mid j\ell\) contains every combination of a pair from \(H_{ik}\) and a pair from \(H_{j\ell}\).

For any symbols \(a,b\) at \(i,j\), it consequently contains exactly

\[
h_i(a)h_j(b)
\]

distinct words with coordinates \(a,b\) at those parties. Every residual pair value has at most three extensions, so

\[
h_i(a)h_j(b)\le3
\quad\text{for all distinct }i,j\text{ and all }a,b.
\tag{3.4}
\]

Thus two different parties cannot both have a symbol with \(h\ge2\).

### 3.3. An exceptional party is also impossible

Suppose, for contradiction, that a symbol \(a\) at party \(i\) satisfies \(h_i(a)\ge2\). By (3.4), every other party has all its positive \(h\)-values equal to one.

Let \(j,k,\ell\) be the other parties. Take an arbitrary \(c\) with \((a,c)\in H_{ik}\). Since \(h_k(c)=1\), there is a unique \(d\) with

\[
(c,d)\in H_{k\ell}.
\]

For **every** \(b\) with \((a,b)\in H_{ij}\), the Cartesian core in the cut \(ij\mid k\ell\) contains

\[
w=(a,b,c,d).
\]

Its \(ik\)-pair lies in \(H_{ik}\). Applying (3.1) in the cut \(ik\mid j\ell\) shows that \((b,d)\in H_{j\ell}\).

Hence \(d\) has at least \(h_i(a)\ge2\) high neighbours at party \(j\), contradicting \(h_\ell(d)=1\).

Therefore no exceptional party exists. For every party,

\[
h_i(a)\in\{0,1\}.
\tag{3.5}
\]

By (3.3), the set

\[
X_i=\{a:h_i(a)=1\}
\]

has exactly three symbols. Every \(H_{ij}\) is a perfect matching between \(X_i\) and \(X_j\).

### 3.4. All six residual pair projections are full three-symbol products

Fix any two parties \(i,j\), and let \(k,\ell\) be the other parties. The full core in the cut \(ik\mid j\ell\) is \(H_{ik}\times H_{j\ell}\).

Because both high-pair sets are matchings on their three-symbol alphabets, its \(ij\)-projection contains every pair in

\[
X_i\times X_j.
\]

There are nine such pair values. The entire residual \(ij\)-projection has exactly \(n=9\) values. Consequently,

\[
\pi_{ij}(E)=X_i\times X_j
\quad\text{for every pair }ij.
\tag{3.6}
\]

This conclusion requires the cores in different cuts to belong to the same tensor; it is not a single-cut feasibility assertion.

### 3.5. The maximal words cannot occupy the complementary pair values

By (3.6), no maximal word can have coordinates in \(X_i\) and \(X_j\) at two different parties: its \(ij\)-pair would already be residual.

Thus every word in \(P\) has **at most one** coordinate in its corresponding \(X_i\).

On the other hand, for every \(a\in X_i\), equation (3.6) gives \(d_i(a)=3\), and hence

\[
p_i(a)=6-d_i(a)=3.
\]

The total number of \(X_i\)-coordinate occurrences among the maximal words is therefore

\[
\sum_i\sum_{a\in X_i}p_i(a)
=
4\cdot3\cdot3
=
36.
\]

But \(P\) contains only \(27\) words, each contributing at most one such occurrence. This gives \(36\le27\), a contradiction.

The entire \(t=27\) branch is excluded at the stated candidate scope. \(\square\)

### Complex-amplitude boundary

This argument applies to arbitrary complex amplitudes. Its orthogonality inputs use the impossibility of a single nonzero complex summand and the adopted unitary component theorem. No replacement by real signs, common nonzero moduli or a selected support was made.

---

## 4. Candidate classification of connected excess-four components

### Statement

**UNREVIEWED AUTHOR CANDIDATE.** Let \(V\) be a connected square unitary support component with minimum row and column degree at least two and

\[
|{\rm supp}(V)|-2m=4,
\]

where \(m\) is its number of rows. Then \(m=4\). Its row and column degree multisets are exactly one of:

1. \((3,3,3,3)\) on both sides;
2. \((2,2,4,4)\) on the row side and \((3,3,3,3)\) on the column side;
3. the transpose of case 2.

In case 1, the missing positions form a perfect matching. In case 2, the two degree-two rows use disjoint column pairs and both degree-four rows meet every column.

These are necessary support descriptions, not assertions that every such support is realizable or that three independently chosen cut descriptions form a tensor.

### Proof

Let \(a\) be the number of degree-two rows and \(b=m-a\) the number of higher-degree rows.

Degree-two rows have equal or disjoint column pairs, by the no-single-overlap property. Two distinct degree-two rows on the same pair would be orthonormal vectors spanning that two-dimensional coordinate space. No other row could meet the pair, so they would form an isolated full \(2\times2\) component. That is incompatible with the present connected positive-excess component.

Thus its \(a\) degree-two rows use disjoint column pairs.

Every other row meeting such a pair contains both columns. Moreover, each pair has at least two higher-row neighbours. If it had only one, its two columns would be orthonormal and supported on precisely the degree-two row and that neighbour. The resulting square two-row restriction would exhaust both row norms, making the neighbour degree two and again isolating a \(2\times2\) component.

The high-row entries therefore number at least

\[
4a+2(m-2a)=2m:
\]

at least four incidences on each low-row pair, and at least two on every remaining column. Their actual number is \(2m+4-2a\), so

\[
a\le2.
\tag{4.1}
\]

Also, every higher row contributes at least one to the row excess, so

\[
b\le4.
\tag{4.2}
\]

Therefore \(m\le6\). An excess-four component cannot have \(m\le3\), because an \(m\times m\) support then has at most \(m^2\le2m+3\) entries.

It remains to exclude \(m=5,6\), then classify \(m=4\).

### 4.1. Six rows are impossible

Equations (4.1)–(4.2) force \(a=2,b=4\), with all four higher rows of degree three.

The two low-row pairs occupy four columns, leaving two other columns. Every higher row must meet exactly one low-row pair and one of the two other columns. Each pair needs at least two higher neighbours, so each has exactly two.

A higher row attached to one pair and a higher row attached to the other cannot use the same extra column: they would overlap there alone. Thus the extra columns used by the two groups are disjoint. Since there are only two extra columns, each group uses its own single extra column.

The component consequently splits into two disconnected three-row components, a contradiction.

### 4.2. Five rows are impossible

There are two possible degree counts.

**One degree-two row.** Then \(a=1,b=4\), and all higher rows have degree three. Let \(C\) be the low-row column pair.

A higher row avoiding \(C\) would use all three outside columns. Every higher row meeting \(C\) uses the pair and one outside column, and would overlap that avoiding row exactly once. As \(C\) has higher neighbours, no higher row can avoid it.

All four higher rows therefore use \(C\) and one outside column. The three outside columns need at least six incidences, but receive only four.

**Two degree-two rows.** Then the higher-row degrees are \(3,3,4\). Their disjoint low-row pairs leave one outside column. The degree-four row must meet both pairs. Each degree-three row must use one pair and the outside column.

Each pair needs a second higher neighbour, so the two degree-three rows attach to different pairs. They then overlap only at the outside column, impossible.

### 4.3. Four-row classification

If \(a=0\), all four rows have degree three.

If \(a=1\), the other row degrees are \(3,3,4\). Both degree-three rows must meet the low-row pair. Each also uses one of the two outside columns; the degree-four row uses both. Minimum column degree forces the two degree-three rows to choose different outside columns. Those outside columns then overlap only at the degree-four row, impossible.

If \(a=2\), both higher rows have degree four. The low-row pairs are disjoint and cover all four columns, so every column has degree three.

Applying the same argument to the transpose, when all rows have degree three the columns either all have degree three or have degrees \(2,2,4,4\). This gives exactly the stated alternatives. \(\square\)

---

## 5. Consequences for the entire \(t=28\) branch

At \(t=28\),

\[
n=8,\qquad |E|=20,\qquad e=4.
\]

Using the imported excess-zero/one/two results and the preceding excess-four theorem, **every paired cut** has one of the following decompositions:

| Cut decomposition | Residual dimensions |
|---|---:|
| One connected excess-four component and two full \(2\times2\) components | \(4+2+2\) |
| Two eight-entry excess-two components and one full \(2\times2\) component | \(3+3+2\) |

The excess-four component has one of the three profiles in Section 4. An excess-three component cannot occur here: the remaining excess would be one, which is impossible.

### 5.1. Only two multiplicity profiles occur in a pair system

Each of the six residual pair systems is of one of these types:

- **D:** four pair values of multiplicity three and four of multiplicity two;
- **Q:** two pair values of multiplicity four and six of multiplicity two.

A Q side occurs only on the \((2,2,4,4)\) side of an excess-four component. Its complementary pair system is D. Therefore:

\[
\boxed{\text{Two complementary pair systems cannot both be Q.}}
\tag{5.1}
\]

Equivalently, the Q pair systems form an intersecting family of pairs of parties. This is a necessary relation between the three cuts, not a license to choose their profiles independently.

### 5.2. Common party marginals constrain all six pair systems

Define \(p_i,d_i,s_i\) as in Section 3 and put

\[
h_i(a)=s_i(a)-2d_i(a).
\]

For every other party \(j\),

\[
h_i(a)
=
\sum_{b:\,(a,b)\in\pi_{ij}(E)}
\bigl(\operatorname{mult}_E(a,b)-2\bigr).
\tag{5.2}
\]

Thus the weighted high-multiplicity incidences have the **same party marginal in all three partner systems**, and

\[
h_i(a)\ge0,\qquad \sum_a h_i(a)=4.
\tag{5.3}
\]

In a D pair system, \(h_i(a)\) counts its multiplicity-three neighbours. In a Q pair system, it is twice the number of multiplicity-four neighbours. Consequently,

\[
\boxed{\text{If party }i\text{ belongs to a Q pair system, every }h_i(a)
\text{ is even in all its pair systems.}}
\tag{5.4}
\]

These constraints are imposed on the same residual word set and the same maximal-word counts. Separate single-cut support feasibility does not establish them.

---

## 6. Exact complex compatibility for all two-term equations

The following result gives an amplitude-level obstruction shared across the cuts. It neither substitutes real signs for complex phases nor claims that longer orthogonality equations disappear.

### 6.1. Universal construction of the constraints

Consider the common residual support \(E\), with positive moduli

\[
r_w=|z_w|>0.
\]

Collect **all** row and column orthogonality equations, from all three paired cuts, whose two lines overlap at exactly two positions. Write each such equation as

\[
z_{\alpha(q)}\overline{z_{\beta(q)}}
+
z_{\gamma(q)}\overline{z_{\delta(q)}}=0,
\qquad q\in\mathcal Q.
\tag{6.1}
\]

Here the indices denote actual support words; the same word has the same amplitude wherever it appears.

Let \(e_w\) be the coordinate basis of \(\mathbb Z^E\), and define

\[
\lambda_q
=
e_{\alpha(q)}-e_{\beta(q)}
-e_{\gamma(q)}+e_{\delta(q)}.
\tag{6.2}
\]

### 6.2. Candidate phase-gluing theorem

For any universally quantified positive moduli \((r_w)_{w\in E}\), there exist complex phases satisfying **all** equations (6.1) simultaneously if and only if both conditions below hold:

\[
r_{\alpha(q)}r_{\beta(q)}
=
r_{\gamma(q)}r_{\delta(q)}
\quad\text{for every }q,
\tag{6.3}
\]

and

\[
\boxed{
\sum_q k_q\lambda_q=0,\ k_q\in\mathbb Z
\quad\Longrightarrow\quad
\sum_q k_q\ \text{is even}.
}
\tag{6.4}
\]

In particular, any integral dependence with odd coefficient sum is an exact obstruction to actual complex amplitudes, regardless of the positive moduli.

### Proof

Write \(z_w=r_w u_w\), with \(u_w\) on the complex unit circle.

For (6.1) to hold, its two summands must have equal moduli, giving (6.3). Their phases must differ by a minus sign, giving

\[
u^{\lambda_q}=-1.
\tag{6.5}
\]

Multiplying these identities with arbitrary integral exponents \(k_q\), an integral relation \(\sum_q k_q\lambda_q=0\) gives

\[
1=(-1)^{\sum_q k_q}.
\]

This proves necessity of (6.4).

Conversely, let \(L\subseteq\mathbb Z^E\) be the subgroup generated by the \(\lambda_q\). Condition (6.4) makes

\[
\chi\!\left(\sum_q k_q\lambda_q\right)
=
(-1)^{\sum_q k_q}
\]

a well-defined homomorphism \(L\to U(1)\).

This homomorphism extends to \(\mathbb Z^E\). An elementary extension argument suffices: when adjoining a coordinate generator \(v\) to an existing subgroup, either no positive multiple of \(v\) lies in that subgroup, in which case its unit-circle value can be assigned freely, or there is a least positive such multiple \(mv\), in which case choose an \(m\)-th complex root of the already prescribed value of \(mv\). The resulting extension is well defined. Adjoining the finitely many coordinate generators completes the extension.

Put \(u_w=\chi(e_w)\) for the extended character. Then (6.5) holds for every \(q\); with (6.3), the two summands in every equation (6.1) have equal modulus and opposite phase. Hence they cancel. \(\square\)

### 6.3. What this does and does not settle at \(t=28\)

This theorem is a simultaneous-cut statement: \(\mathcal Q\) is the union of the equations from all three cuts, not three separately solved phase systems.

It uses **integral relations**, not merely relations modulo two. Arbitrary complex roots are allowed; no real-sign restriction is present.

For the subcase in which every cut’s excess-four component has degree three on both sides, every overlapping pair of distinct lines has exactly two common positions. The remaining components are full \(2\times2\) blocks. Therefore, once common positive moduli satisfy the line norms, (6.3) and (6.4) are an exact criterion for simultaneous residual unitarity in that subcase.

For the other \(t=28\) profiles, some line pairs have three or four common positions. The theorem settles their entire two-term subsystem, but **does not settle those longer equations**. They must hold for the same amplitudes satisfying the common line norms and the two-term subsystem. No assertion of tensor existence follows from the component classification or the parity criterion alone.

---

## 7. Per-claim status and exact residual

| Claim | Status in this return | Scope |
|---|---|---|
| Adopted \(t\in\{24,27,28\}\) frontier | IMPORTED | S1 lines 7–18; provenance retained |
| Excess-three full-core input | IMPORTED | S5 line 5; not re-proved |
| Entire \(N=48,t=27\) exclusion | **SUPPORTED — UNREVIEWED AUTHOR CANDIDATE** | Section 3; all support words and complex amplitudes |
| Connected excess-four classification | **SUPPORTED — UNREVIEWED AUTHOR CANDIDATE** | Section 4; arbitrary square unitary component |
| Two possible \(t=28\) cut decompositions | **SUPPORTED — UNREVIEWED AUTHOR CANDIDATE** | Section 5; necessary, not existence |
| Q incompatibility and common weighted marginals | **SUPPORTED — UNREVIEWED AUTHOR CANDIDATE** | Equations (5.1)–(5.4); all three cuts |
| Exact two-term complex phase criterion | **SUPPORTED — UNREVIEWED AUTHOR CANDIDATE** | Section 6; common amplitudes across cuts |
| Exclusion or realization of \(t=28\) | **INCONCLUSIVE** | No full simultaneous-tensor result |
| Exclusion of \(t=24\) | **NOT CLAIMED** | Existing adopted restrictions retained |
| Standalone unrestricted P2 | **NOT USED / NOT ESTABLISHED** | No source-scope enlargement |
| Support-48 exclusion or \(N\ge49\) | **NOT CLAIMED** | Required live branches remain |

The precise outstanding \(t=28\) problem is not single-cut component feasibility. It is existence or impossibility of a **common** residual word set, compatible maximal words, positive moduli and complex phases satisfying the three-cut conditions together. In the profiles with longer overlaps, the remaining three- and four-term orthogonality equations are not proved satisfiable or contradictory here.

The substantive completed development is the branch-wide \(t=27\) contradiction. If accepted after review, it would reduce the support-48 survivors to \(t=24\) and \(t=28\); it does not dispose of either.