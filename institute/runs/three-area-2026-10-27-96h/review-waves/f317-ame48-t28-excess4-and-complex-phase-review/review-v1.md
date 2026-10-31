# f317 review-v1 — excess-four components and simultaneous complex phases

**Delivery note:** The attempt to write this wave’s `review-v1.md` was refused by the write tool’s filesystem restriction. No bypass was attempted and no reviewer file was created. This is the complete review text for parent materialization. Final native-clock checkpoint: **2026-10-30T07:45:55-0700**.

## Disposition

**SUPPORTED at the stated necessary/conditional scopes. Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

I find no mathematical defect in the assigned claims of f311 §§4–6. The excess-four classification, the \(t=28\) cut/multiplicity restrictions, and the exact two-term complex-phase criterion admit the universal proofs below. The overlap-two-only residual-unitarity conclusion is correct with common positive moduli and all line norms explicitly retained.

This is a same-harness written audit, not human, independent-family, formal/kernel, or novelty assurance. The entire manuscript was read; the disjoint §3 \(t=27\) exclusion is not independently disposed of by this review. No \(t=28\) exclusion, witness, support-48 exclusion, or \(N\ge49\) conclusion is made.

## 1. Administrative record and exact inputs

Before mathematical packet access, I read the f317 manifest, freeze receipt, and all six status-only controls in the manifest. The administrative PRE-BODY ACK was delivered to Main before the first packet read. The fresh initial native clock was **2026-10-30T07:37:39-0700**.

Live metadata hashes matched:

- Manifest: `687568f2b44217d539a82bad5d6ba3c31997018c419c55cfd92162f0d7296f0a`.
- Freeze receipt: `49ac8f8aff17c2c080e31d9c9a309d09ec4614b59b35cd9b159d0587c0bfac6a`.
- Literal packet: `dbebf4e5a94206e7423b64ba02b3fa0d00823d3d7f4e82962ca7c2a52e967c6b`.
- S1, f311 author manuscript: `13ecb3fd9fd4605bb8dfe22bd839983a5c560dba1bbccd2993dee8c0921a9ef1`.
- S2, selected unitary-support facts: `906975c6c9b1ff03d3553e72263ad7f1a448ea44f15b66673a6ffedbceac1ea6`.
- S3, adopted branch/interface disposition: `2af4fde719fbee23fa740160792e152945bd6e352e9006a77f7817c1949fe9aa`.

I read the complete literal packet raw, in source order, in successive windows 1–20, 21–40, continuing through 581–600, followed by 601–608. No elision was displayed. Coverage includes:

- S1 logical lines 1–542, including its non-LF-terminated ending;
- the selected S2 LF19–46 only;
- S3 LF1–36 through its ending.

The complete-read/binding checkpoint was **2026-10-30T07:40:02-0700**; a subsequent substantive audit checkpoint was **2026-10-30T07:41:57-0700**.

No sibling review, excluded linked body, held payload, or author code was accessed. No scientific code, CAS, solver, numerical enumeration, replay, selected tensor, support graph, amplitude, phase assignment, or parameter example was used. Machine activity was limited to permitted reading, delivery, and metadata/hash/date operations; no build, lint, test, or formatter was run. Status controls supplied no mathematical premises.

### Exact mathematical imports

- **S3 LF11–18; S2 LF23–38:** residual-unitary setup, square components, minimum line degree two, nonnegative additive excess, full \(2\times2\) excess-zero components, absence of excess one, and \(3\times3\) eight-entry excess-two components. The elementary unitary arguments used below are also reconstructed explicitly.
- **S1 LF52–68:** notation for the common residual word set and maximal words. In each pair system, maximal pair values and residual pair values partition the 36 possibilities.
- **Classical facts used explicitly:** finite-dimensional row/column orthonormality and square-isometry unitarity; subgroups of the additive integers are either zero or \(m\mathbb Z\); and every unit-circle number has an \(m\)-th unit-circle root for every positive integer \(m\). No unquoted scientific theorem is needed for §§4–6.

The conditional \(t=28\) analysis does not use the no-OLS(6) theorem. That named classical provenance remains attached to the imported global branch frontier in S3 LF7–9; it is not silently removed or enlarged. Neither the excess-three theorem nor the \(t=27\) argument is needed for the present conclusions.

All row/column, party, symbol, and subgroup choices below are arbitrary universally quantified variables, not selected examples.

## 2. Low-row structure and the complete excess-four classification

**Claim: SUPPORTED. Source: S1 LF264–346; relevant imported facts: S2 LF23–32.**

Let \(V\) be any connected square unitary component of order \(m\), with every line degree at least two, and with exactly \(2m+4\) supported entries. Write \(a\) for its number of degree-two rows and \(b=m-a\) for its higher-degree rows.

### 2.1. The low-row pair lemma

Two degree-two rows cannot share exactly one column, because their inner product would be one nonzero complex product. If they shared both columns, their restrictions would be two orthonormal vectors spanning that two-coordinate space. Every other row would vanish on those columns, isolating a full \(2\times2\) component. Connectedness and positive excess exclude this. Therefore all \(a\) low-row column pairs are disjoint.

Every other row meets a low-row pair in either zero or two columns, again by the prohibition on one-term inner products.

Each pair has at least two higher-row neighbours. Indeed, minimum column degree supplies another row on the pair. If there were only one such row, the two columns would be supported on that row and the original low row. Their \(2\times2\) restriction would have orthonormal columns and hence orthonormal rows. The neighbour’s entire unit row norm would already be exhausted on the pair, making it another degree-two row and isolating the forbidden \(2\times2\) component.

Consequently the higher rows have at least four entries on each of the \(a\) pairs and at least two entries on every one of the \(m-2a\) other columns. Their supported-entry count is therefore at least
\[
4a+2(m-2a)=2m.
\]
Their actual entry count is \(2m+4-2a\). Hence \(a\le2\).

Also, each higher row contributes at least one unit of row excess, so \(b\le4\). Thus
\[
m=a+b\le6.
\]
For \(m\le3\), the required count \(2m+4\) exceeds \(m^2\). Only \(m=4,5,6\) remain.

These estimates use the full complex unitary hypotheses, not signs or equal moduli.

### 2.2. The \(m=6\) case

The bounds force \(a=2\), \(b=4\), and all four higher rows have degree three. The two disjoint low-row pairs occupy four columns, leaving two outside columns.

A higher row cannot avoid both pairs: it would then have only two available columns. It cannot meet both pairs: that would require at least four entries. Thus every higher row uses exactly one pair and exactly one outside column.

Each pair needs at least two higher neighbours; with four higher rows, precisely two attach to each pair.

Higher rows attached to different pairs cannot use the same outside column, since their overlap would then consist only of that column. Thus the nonempty sets of outside columns used by the two groups are disjoint. There are only two outside columns, so each group uses exactly one.

Each pair, its low row, its two higher neighbours, and its group’s outside column is consequently disconnected from the other group. This contradicts connectedness. Therefore \(m=6\) is impossible.

### 2.3. The \(m=5\) cases

The bounds leave exactly \(a=1\) or \(a=2\).

**If \(a=1\):** all four higher rows have degree three. Let \(C\) be the arbitrary low-row pair.

A higher row meeting \(C\) uses both its columns and one outside column. A higher row avoiding \(C\) would have to use all three outside columns. Such an avoiding row would overlap every meeting row exactly once. Meeting rows exist by the pair lemma, so no avoiding row can exist.

All four higher rows therefore contribute only four outside incidences in total, whereas the three outside columns require at least six. This is impossible.

**If \(a=2\):** the three higher-row degrees are \(3,3,4\). The pairs leave one outside column.

The degree-four row must use both pairs: meeting only one pair would allow at most three entries. Each degree-three row must use one entire pair and the outside column.

The pair lemma requires a second higher neighbour for each pair besides the degree-four row, so the degree-three rows attach to different pairs. They then overlap only at the outside column, again impossible.

This exhausts \(m=5\) without checking any concrete support.

### 2.4. Every \(m=4\) profile, including transpose

Here the total degree is 12.

- **If \(a=0\):** all four row degrees are three.
- **If \(a=1\):** the row degrees are \(2,3,3,4\). Each degree-three row must use the low pair, since only two columns lie outside it. Each then uses exactly one outside column; the degree-four row uses both. Minimum outside-column degree forces the degree-three rows to use different outside columns. Those outside columns consequently overlap only at the degree-four row, contrary to column orthogonality. Thus \(a=1\) is impossible.
- **If \(a=2\):** both higher rows have degree four. The two low pairs are disjoint and cover the four columns, so each column meets its unique low row and both higher rows. Every column has degree three.

Apply these same proved arguments to \(V^{\mathsf T}\). When all row degrees are three, the column side cannot have exactly one degree-two column; it either has all degrees three or has degrees \(2,2,4,4\). No additional transpose profile is omitted.

Thus the only necessary paired degree profiles are
\[
\begin{aligned}
&(3,3,3,3)/(3,3,3,3),\\
&(2,2,4,4)/(3,3,3,3),\\
&(3,3,3,3)/(2,2,4,4).
\end{aligned}
\]

In the first profile every row and column misses exactly one position, so the missing positions form a perfect matching. In the second, the low rows occupy disjoint column pairs and the high rows are full; the third is precisely its transpose.

This proves the source’s necessary classification. It does not claim realization of these descriptions.

## 3. All \(t=28\) cut decompositions and pair-system restrictions

### 3.1. Complete component decompositions

**Claim: SUPPORTED. Source: S1 LF350–365; imports: S2 LF24–38 and S3 LF11–18.**

Fix any normalized complex AME\((4,6)\) state having \(N=48\) and \(t=28\), conditionally on its existence. Every residual cut has
\[
n=8,\qquad |E|=20,\qquad e=4.
\]

Component excesses are nonnegative integers. Excess one is impossible, excess-zero components have order two, and excess-two components have order three and eight entries.

The only partitions of positive component excess are therefore four, or two plus two. An excess-three component would leave excess one, which cannot be supplied by any collection of components. The excess-four classification just proved gives order four. Hence the dimensions must be exactly:

- **\(4+2+2\):** one excess-four component and two full \(2\times2\) components;
- **\(3+3+2\):** two excess-two components and one full \(2\times2\) component.

There is no omitted size or component-excess partition. This is a necessary statement for each cut of a common tensor, not a construction of three independently compatible cuts.

### 3.2. D/Q profiles and complementary pairs

**Claim: SUPPORTED. Source: S1 LF367–381.**

On either side of a \(3+3+2\) cut, each eight-entry \(3\times3\) component contributes degrees \(2,3,3\). Together with the \(2\times2\) component, this gives four degree-three and four degree-two pair values: type D.

For a \(4+2+2\) cut, the all-degree-three side of the four-row component similarly gives four degree-three and four degree-two values: D. Its possible \(2,2,4,4\) side instead gives two degree-four and six degree-two values: Q. The classification ensures that the complementary side of a Q side is always D.

Thus no complementary pair systems can both be Q. On four parties, two disjoint two-party subsets are complementary, so the Q pair systems necessarily form an intersecting family. This restriction does not assert that every such choice is realizable.

Importantly, a D marginal profile alone does not identify the \(4+2+2\) decomposition: it can also come from \(3+3+2\). The source’s later overlap-two-only conclusion uses the stronger stated component hypothesis, not merely D labels.

### 3.3. Shared weighted party marginals and parity

**Claim: SUPPORTED. Source: S1 LF383–416; definitions: S1 LF119–125 and LF385–398.**

For any party \(i\) and symbol \(a\), let \(p_i(a)\) count maximal words with that coordinate, let
\[
d_i(a)=6-p_i(a),
\]
and let \(s_i(a)\) count residual words with that coordinate.

In every pair system \(ij\), the maximal words occupy \(p_i(a)\) distinct partner values and exclude residual words from those values. All remaining partner values are residual. Their number is therefore \(d_i(a)\), independently of \(j\).

Write \(\mu_{ij}(a,b)\) for residual multiplicity. Counting residual words first by their \(ij\) pair gives
\[
s_i(a)=\sum_{b:\,(a,b)\in\pi_{ij}(E)}\mu_{ij}(a,b).
\]
Subtracting twice the number of residual \(b\) values yields, for every \(j\ne i\),
\[
h_i(a):=s_i(a)-2d_i(a)
=\sum_{b:\,(a,b)\in\pi_{ij}(E)}
\bigl(\mu_{ij}(a,b)-2\bigr).
\]

This is the same \(h_i(a)\) for all three choices of partner \(j\), because its left side depends only on the common word set and maximal-word counts.

Multiplicities are at least two, so \(h_i(a)\ge0\). Also,
\[
\sum_a s_i(a)=20,\qquad \sum_a d_i(a)=8,
\]
giving
\[
\sum_a h_i(a)=4
\]
for every party.

For D, the summands are one on the degree-three pair values and zero otherwise. For Q, they are two on the degree-four values and zero otherwise. Consequently an endpoint party of any Q system has every \(h_i(a)\) even, and the identical \(h_i\) values remain even in all its other pair systems.

In particular, its positive \(h_i\) values have the necessary partition form \(4\), or \(2+2\). This is only a consequence of evenness and their total four, not an existence assertion.

No independent assignment of the six marginals is allowed by this argument: the counts must come from the same \(E\) and \(P\).

## 4. Exact simultaneous two-term complex-phase criterion

**Claim: SUPPORTED. Source: S1 LF426–510, with simultaneous-cut and complex-root scope at LF514–516.**

Let \(E\) be any of the common finite residual supports under consideration. For every row or column overlap of size exactly two in any of the three cuts, collect the equation
\[
z_{\alpha(q)}\overline{z_{\beta(q)}}
+
z_{\gamma(q)}\overline{z_{\delta(q)}}=0.
\]

Every index denotes its actual support word, so phase variables are shared across cuts. Let \(\mathcal Q\) index the entire collected family, including any repetitions, and define
\[
\lambda_q
=e_{\alpha(q)}-e_{\beta(q)}
-e_{\gamma(q)}+e_{\delta(q)}
\in\mathbb Z^E.
\]

For arbitrary prescribed positive moduli \(r_w\), the following are necessary and sufficient for simultaneous solution of all collected equations by complex amplitudes of those moduli:

1. For every \(q\),
   \[
   r_{\alpha(q)}r_{\beta(q)}
   =r_{\gamma(q)}r_{\delta(q)}.
   \]
2. Every integer relation
   \[
   \sum_q k_q\lambda_q=0
   \]
   has even coefficient sum \(\sum_q k_q\).

### 4.1. Necessity and modulus separation

Write \(z_w=r_wu_w\) with \(u_w\in U(1)\). Two nonzero complex numbers sum to zero exactly when they have equal absolute values and opposite phases. Thus each collected equation is equivalent to its stated modulus equality together with
\[
u^{\lambda_q}=-1.
\]

Multiplying these identities with arbitrary integer exponents \(k_q\) is legitimate because every phase is nonzero. An integer relation among the \(\lambda_q\) then gives
\[
1=(-1)^{\sum_q k_q}.
\]
This proves the parity necessity. No line norm or equality between unrelated moduli was used or inferred.

### 4.2. The character on the generated subgroup

Let \(L\) be the subgroup of \(\mathbb Z^E\) generated by all \(\lambda_q\). Define the proposed value on a represented element by
\[
\chi\!\left(\sum_q k_q\lambda_q\right)
=(-1)^{\sum_q k_q}.
\]

If two representations give the same element of \(L\), their difference is an integer relation. Condition 2 makes the two proposed values equal. Thus \(\chi\) is well defined; adding representations shows it is a homomorphism
\[
\chi:L\longrightarrow U(1),
\]
and it sends every \(\lambda_q\) to \(-1\).

This proof includes dependent or redundant equations without an independence assumption.

### 4.3. Full extension, including nonprimitive and torsion cases

Suppose a character is already defined on an arbitrary subgroup \(H\subseteq\mathbb Z^E\), and let \(v\) be an arbitrary coordinate generator to be adjoined. Set
\[
I=\{n\in\mathbb Z:nv\in H\}.
\]
This is a subgroup of \(\mathbb Z\).

**If \(I=\{0\}\):** choose any \(\xi\in U(1)\) as the value for \(v\), and set
\[
\chi'(h+nv)=\chi(h)\xi^n.
\]
Representations in \(H+\mathbb Zv\) are unique in their \(v\) coefficient, so this is a well-defined extension.

**If \(I\ne\{0\}\):** then \(I=m\mathbb Z\) for its least positive element \(m\). Choose any \(m\)-th unit-circle root \(\xi\) of \(\chi(mv)\), which exists for every positive integer \(m\). Use the same definition.

To check it, if \(h+nv=h'+n'v\), then \(n'-n=tm\) for an integer \(t\), and
\[
\chi(h-h')
=\chi(mv)^t
=\xi^{n'-n}.
\]
The factors therefore cancel in the ratio of the two proposed character values, proving well-definedness. Multiplicativity follows directly. The case \(m=1\) simply preserves the already prescribed value when \(v\in H\).

Beginning with \(H=L\) and adjoining the finitely many coordinate generators yields a character on all of \(\mathbb Z^E\).

This argument neither assumes \(L\) is primitive/saturated nor assumes \(\mathbb Z^E/L\) is torsion free. The \(m\)-th-root step is exactly what handles finite order in the successive quotients; free directions are the \(I=\{0\}\) case. Roots remain in \(U(1)\), and no real-sign restriction is imposed. Thus nonprimitive lattices, torsion, and arbitrary root orders create no missing obstruction.

Taking \(u_w\) equal to the extended character’s value at \(e_w\) gives
\[
u^{\lambda_q}=-1
\]
for every \(q\) simultaneously. With condition 1, each pair of summands has equal modulus and opposite phase, so every collected equation vanishes. This proves sufficiency for every positive modulus family satisfying the stated equalities.

The actual criterion concerns integral zero relations, not merely relations after reduction modulo two. Replacing it by a real-sign linear system would discard the unit-circle root extension argument and would not establish this theorem. No such replacement occurs in the source.

## 5. Exact overlap-two-only residual unitarity, and longer-overlap boundary

### 5.1. The claimed special subcase has no hidden longer equations

**Claim: SUPPORTED. Source: S1 LF518.**

Assume every cut has an excess-four component whose rows and columns all have degree three. By the proved classification, that component is \(4\times4\) with a missing perfect matching; the rest of that cut consists of two full \(2\times2\) components.

In the \(4\times4\) component, two distinct rows omit different columns and hence share exactly two columns. The identical statement holds for columns. In a full \(2\times2\) component, distinct rows share exactly two columns, and distinct columns share exactly two rows. Lines from different components have disjoint supports.

Consequently every off-diagonal row or column inner product in every cut is either identically zero by disjointness or is one of the collected two-term equations. **There are no three- or four-term inner products hidden in this subcase.**

The diagonal conditions are the common line norms: for every residual pair value \(p\) in each of the six pair systems,
\[
\sum_{w:\,\pi_{ij}(w)=p}r_w^2=1.
\]
These norms are a separate condition and are not consequences asserted by the phase theorem.

Necessity follows from unitarity. Conversely, fix common positive moduli satisfying all those norms, all modulus-product equalities, and the integral-relation parity criterion. The character theorem supplies one common phase per word for all three cuts. All diagonal Gram entries are then one; all off-diagonal entries vanish by the preceding overlap classification and two-term cancellations. Each square residual flattening is unitary.

Thus the source’s exact simultaneous residual-unitarity test is correct under its stated special-subcase hypothesis. This is not a theorem that type D labels alone suffice, nor a construction of a compatible support or maximal-word complement.

### 5.2. Other profiles retain longer equations

**Claim: SUPPORTED as an explicitly unresolved boundary. Source: S1 LF520 and LF540.**

In an excess-four component with row degrees \(2,2,4,4\), its two full rows overlap in four columns. Its columns have degree three:

- columns in the same low-row pair overlap in the two full rows and their shared low row, hence in three rows;
- columns from different low-row pairs overlap in the two full rows.

Transposition interchanges these row/column statements.

In an eight-entry \(3\times3\) component, the missing position is unique. The two full rows overlap in three columns, and the two full columns overlap in three rows. Pairs involving the shorter row or column have overlap two. Hence \(3+3+2\) cuts also have longer overlaps.

The two-term theorem solves precisely the collected two-term subsystem for a common choice of amplitudes. In the other profiles, the line norms and all remaining longer inner products must still be imposed, or separately proved consequences.

This review does not assert those longer equations are independent, inconsistent, or satisfiable; no redundancy or completion argument is imported. The source correctly leaves that question open.

## 6. Claim-by-claim disposition

| Source claim | Status | Exact reviewed scope |
|---|---|---|
| S1 LF282–310: disjoint low pairs, at least two higher neighbours, \(a\le2\), and \(m\le6\) | **SUPPORTED** | Every connected positive-excess-four complex unitary component |
| S1 LF314–336: all \(m=6\) and \(m=5\) cases excluded | **SUPPORTED** | Exhaustive degree cases established symbolically above |
| S1 LF264–278, LF338–346: three \(m=4\) profiles | **SUPPORTED** | Necessary descriptions, including every transpose case; no realization claim |
| S1 LF350–365: \(4+2+2\) or \(3+3+2\) | **SUPPORTED** | Every cut of a conditional \(N=48,t=28\) state, at the explicit excess-zero/one/two import boundary |
| S1 LF367–381: D/Q types and no complementary Q/Q | **SUPPORTED** | Necessary same-tensor restrictions, not independent cut choices |
| S1 LF383–416: weighted shared \(h_i\) and Q parity | **SUPPORTED** | Same residual/maximal word sets in all six pair systems |
| S1 LF426–510, LF514–516: exact complex two-term criterion | **SUPPORTED** | All prescribed positive moduli; all integer relations; nonprimitive/torsion/root cases included |
| S1 LF518: exact overlap-two-only residual-unitarity criterion | **SUPPORTED** | All three cuts have the degree-three excess-four shape; all common line norms retained |
| S1 LF520, LF540: other profiles’ longer equations | **INCONCLUSIVE for their completion** | Correctly left open; not a flaw or nonexistence result |
| \(t=28\) exclusion or witness; support-48 exclusion; \(N\ge49\); novelty | **NOT ESTABLISHED / NOT CLAIMED** | No such conclusion follows here |

No source correction is proposed. The explicit universal derivations above support the frozen claims rather than silently rewriting a faulty proof.

The open simultaneous-tensor problem remains a common \(E\), compatible \(P\), positive moduli, and phases satisfying all three cuts; in the longer-overlap shapes, this includes the remaining longer equations.

**Overall correctness:** correct for the assigned §§4–6 necessary/conditional mathematical claims.

**Explanation:** The low-row counting exhausts the possible component sizes and profiles, and the character-extension proof gives precisely the claimed complex two-term criterion without a primitivity or real-sign assumption. The residual-unitarity sufficiency is correctly confined to the overlap-two-only component subcase with explicit line norms; the other shapes and the full \(t=28\) branch remain open.

**Confidence:** 0.96.