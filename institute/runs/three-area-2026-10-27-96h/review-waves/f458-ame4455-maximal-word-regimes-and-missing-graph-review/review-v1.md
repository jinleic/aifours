# F458 — Written audit of the whole-\(4455\) maximal-word and missing-graph theorem

**Role:** WRITTEN  
**Disposition:** **SUPPORTED at the stated necessary-condition scope.**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR mathematical findings.**  
**Delivery:** Complete review body for parent materialization. No working-tree file was written.

This review reconstructs the actual-tensor implication, both maximal-word regimes, the symbol-degree restrictions, the four-edge missing-graph classification, the simultaneous low-symbol inequalities, and the regular-stratum matching theorem. It does **not** establish existence or nonexistence of a tensor in the entire \(4455\) class.

## 1. Bindings, access, and method

### Frozen bindings

The following are **parent-observed metadata**, not reviewer-executed hash or clock checks:

| Artifact | SHA-256 |
|---|---|
| F458 manifest | `0aa88f6e616bc8f4c62b5db9510977d3f5cf451b8d25842b8745745b24985bf8` |
| Freeze receipt | `48611af7d03ce9bdd89c02a7c9a6344560c3b789394eb637c849943b6c2d7e22` |
| Literal packet | `d1111904d1a3393456e5697dd4d70d12dbd7f0304154e21e0b24be47dfc5a86a` |
| S1: F433 author candidate | `b0f908b800c0c0db23509bdb7e6bbb9748ae513a091142969398662a1a0f08d5` |
| S2: whole-\(4445\) disposition | `4a1e3ef8241a7a6701e6b99afd25c3cd5352829dc4acdea28ecdf27b638d0ac1` |
| S3: alphabet-shadow disposition | `1e93cfc6ff428aefbf4eb301eba7cfd6fd9b14c62a0dca254b231e41ccadc055` |

The supplied observation **2026-10-30T11:43:56-0700 PDT** belongs to the parent. It is not my native start, completion time, or independently executed clock observation.

### Actual read sequence

Before opening the mathematical packet, I read:

1. The required memory summary and the relevant written-acceptance and independent-review skills.
2. The complete manifest, freeze receipt, dispatch receipt, and parent live-metadata supply.
3. All ten manifest-listed permission/status controls, including their endings.
4. I then sent a direct administrative pre-body ACK to Main; the tool reported delivery.

After that ACK, I read the literal packet sequentially in exact raw windows of at most twenty lines, covering **packet lines 1–792**, including its final line. The rendered source coverage was:

- **S1:** logical lines **1–735**, including the final acceptance-status paragraph. The parent reports 734 LF characters; this is distinct from the 735 rendered logical lines.
- **S2:** logical lines **1–27**, complete.
- **S3:** logical lines **1–28**, complete.

No packet elision appeared in these reads.

### Method and exclusions

The reconstruction below uses formal counting and algebra on the frozen hypotheses and supplied cases. I did not introduce an additional selected mathematical instance, privately or publicly.

- Scientific code prepared: **none**.
- Scientific execution, CAS, interpreter, solver, enumeration, or replay: **NOT RUN**.
- Builds, tests, lint, and formatters: **not run**.
- Author programs, sibling reviews, and additional local or public mathematical sources: **not opened**.
- The public links quoted in S1 §11 were **not followed**.
- All quarantine records were used **for status and permission only**. No held episode or consumer supplied a mathematical premise.
- No claim of certified cognitive isolation, human review, independent-family review, or kernel verification is made.

The current read-only role prevents materializing the review in the working tree. This response supplies the complete body without a write bypass.

## 2. Claim-by-claim disposition

Line references below use the packet’s **S1/S2/S3 logical source labels**.

| Claim | Disposition | Evidence and reconstruction |
|---|---|---|
| Actual same-\(U\), same-\(P\), six-pair complement and exact-two-extension interface | **SUPPORTED** | S1 234–276; reconstructed in §3 below |
| Moments \(60,49\), identity \(3n_0+n_1+n_4=1\), and both complete histograms | **SUPPORTED** | S1 280–303; §4 |
| Outside-party, triple-type, and double-type counts for the same 24 maximal words | **SUPPORTED** | S1 305–341; §4 |
| Partner-independent degrees, identity (5.1), degree multisets, and exceptional singleton restrictions | **SUPPORTED** | S1 345–399; §5 |
| Four-edge \(M_{12}\), the five F-regime forest types, the three S/five-symbol types, and the cycle equivalence | **SUPPORTED** | S1 404–449; §6 |
| Full four-word partition alternative without assuming no-distance-one | **SUPPORTED** | S1 453–474; §7 |
| All three defect identities and simultaneous common-\(P\) inequalities | **SUPPORTED** | S1 478–534; §8 |
| Low-to-low matching theorem and both sector tables in the regular-four-party stratum | **SUPPORTED** | S1 538–585; §9 |
| Additional regular F-regime restriction on the four-internal word | **SUPPORTED** | S1 589–604; §10 |
| Local complex \(2\times2\) modulus and phase equations | **SUPPORTED directly by algebra** | S1 633–643; §11 |
| S1’s descriptive public-source comparison and literature-status statements | **INCONCLUSIVE in this review** | S1 649–660; no external-source follow was permitted or performed |
| Existence or nonexistence of the entire \(4455\) class | **INCONCLUSIVE; not proved here** | The candidate expressly leaves this unpaid: S1 629–645 |

No claim was refuted.

## 3. Actual-tensor interface: all six consumers use the same support

Assume one tensor
\[
U=6\psi\in(\mathbb C^6)^{\otimes4}
\]
has three unitary balanced flattenings, exactly 48 nonzero entries, and exactly 24 modulus-one entries. Let \(P\) be those maximal entries and \(E\) the other 24 support words.

A modulus-one entry exhausts its unitary row and column. Consequently, in each cut the 24 words of \(P\) use distinct rows and columns, and no residual entry can occupy one of those rows or columns.

Deletion leaves a \(12\times12\) unitary with 24 nonzeros. Every remaining row and column has at least two nonzeros: a singleton would have modulus one and would already belong to \(P\). The count therefore forces exactly two nonzeros in every remaining row and column.

The three cuts account for **all six physical pair projections**, not just three independently adjustable row interfaces. For every pair \(ij\),
\[
R_{ij}:=\pi_{ij}(E)
\]
satisfies
\[
|R_{ij}|=12,
\qquad
|\{w\in E:\pi_{ij}(w)=x\}|=2
\quad(x\in R_{ij}),
\]
and
\[
\pi_{ij}|_P\text{ is injective},
\qquad
\pi_{ij}(P)=[6]^2\setminus R_{ij}.
\]

These complements are projections of the **same** 24-word set \(P\). The later arguments consistently consume that stronger shared incidence.

For an internal symbol \(a\in A_i=\pi_i(E)\), write \(p_i(a)\) for its multiplicity in \(P\). For any partner \(j\), the six possible pairs containing \(a\) split between \(P\) and \(R_{ij}\), giving
\[
r_i(a)=6-p_i(a).
\]
Thus \(r_i(a)\) is partner-independent. Exact two-extension counting gives
\[
|\{w\in E:w_i=a\}|=2r_i(a),
\qquad
\sum_{a\in A_i}r_i(a)=12.
\]

If \(r_i(a)=1\), the two residual words containing \(a\) would have the same unique neighbor at every other party. They would be identical support words, a contradiction. Therefore
\[
r_i(a)\ge2.
\]

No no-distance-one or no-OLS premise enters this derivation.

Actual orthogonality additionally forces the residual matrix in each cut to decompose into full \(2\times2\) blocks: two rows that share one column cannot have just that one nonzero overlap, so their two-column supports coincide. This condition is a further necessary constraint, not something the graph and moment shadows have already solved.

## 4. The two regimes and all maximal-word types

Here
\[
(q_1,q_2,q_3,q_4)=(4,4,5,5),
\qquad
(b_1,b_2,b_3,b_4)=(2,2,1,1).
\]

For \(w\in P\), let \(k(w)\) be the number of its internal coordinates.

### Moments and histograms

The first moment is
\[
\sum_{w\in P}k(w)
=\sum_i\sum_{a\in A_i}(6-r_i(a))
=6\sum_iq_i-48
=60.
\]

For a pair \(ij\), the number of maximal words internal at both parties is \(q_iq_j-12\). Pair injectivity therefore gives
\[
\sum_{w\in P}\binom{k(w)}2
=\sum_{i<j}q_iq_j-72
=49.
\]

For \(s=0,1,2,3,4\), the expression
\[
\binom{s}{2}-2s+3
\]
has values \(3,1,0,0,1\). Hence
\[
3n_0+n_1+n_4
=49-2(60)+3(24)
=1.
\]

Nonnegative integrality forces \(n_0=0\) and exactly one of \(n_1,n_4\) to equal one. Combining this with the first moment and \(\sum n_s=24\) gives precisely:

- **F regime**
  \[
  (n_0,n_1,n_2,n_3,n_4)=(0,0,13,10,1).
  \]
- **S regime**
  \[
  (n_0,n_1,n_2,n_3,n_4)=(0,1,10,13,0).
  \]

### Triple types

Fix party \(i\). Each outside symbol occurs in six maximal words, so exactly \(6b_i\) words are outside at \(i\). The total number of their internal coordinates at the other parties is
\[
b_i\sum_{j\ne i}q_j,
\]
because every pair in \(B_i\times A_j\) occurs once in \(P\).

Let \(\sigma_i\) indicate that the unique one-internal word exists and is outside at \(i\). Among the \(6b_i\) words, the default internal-coordinate contribution is two; the singleton lowers that contribution by one, and a triple outside at \(i\) raises it by one. Therefore
\[
b_i\sum_{j\ne i}q_j=12b_i-\sigma_i+t_i,
\]
so
\[
t_i=b_i^2+\sigma_i.
\]

This yields:

- F: \(t=(4,4,1,1)\).
- S, with singleton internal party \(h\):
  \[
  t_i=b_i^2+\mathbf1_{\{i\ne h\}}.
  \]

### Double types

Let \(ij\) and \(kl\) be complementary pairs. Every outside pair in \(B_k\times B_l\) occurs once in \(P\). Its word is either internal exactly at \(i,j\), or is the singleton with internal party in \(\{i,j\}\). There are no zero-internal words, and triples cannot have two outside coordinates. Thus
\[
d_{ij}=
\begin{cases}
b_kb_l,&F,\\
b_kb_l-\mathbf1_{\{h\in\{i,j\}\}},&S.
\end{cases}
\]

In F this is
\[
(d_{12},d_{13},d_{14},d_{23},d_{24},d_{34})
=(1,2,2,2,2,4).
\]

Together with the triples and the unique exceptional word, these formulas account for all 24 words in each regime. They are not independent pair-count assignments.

## 5. Symbol degrees and the exceptional word

For \(a\in A_i\), let \(\tau_i(a)\) count maximal triples containing \(a\), \(f_i(a)\) indicate membership in the four-internal word, and \(\sigma_i(a)\) indicate that \(a\) is the internal symbol of the singleton.

Counting other internal coordinates among maximal words containing \(a\) gives
\[
\sum_{j\ne i}(q_j-r_i(a))
=p_i(a)-\sigma_i(a)+\tau_i(a)+2f_i(a).
\]
Substituting \(p_i(a)=6-r_i(a)\) yields
\[
\boxed{\tau_i(a)+2f_i(a)-\sigma_i(a)
=12-q_i-2r_i(a).}
\]

### Four-symbol parties

For \(q_i=4\), the right-hand side is \(8-2r_i(a)\). Nonnegativity of the other counts and \(\sigma_i(a)\le1\) imply \(r_i(a)\le4\). Four degrees in \(\{2,3,4\}\) summing to twelve have exactly the listed possibilities:
\[
(3,3,3,3),\qquad(4,3,3,2),\qquad(4,4,2,2).
\]

If the singleton is internal at a four-symbol party, say at symbol \(a\) of party 1, it already pairs \(a\) with the unique outside symbol at each of parties 3 and 4. Every other maximal word containing \(a\) must therefore be internal at both parties 3 and 4. Since S has no four-internal word, that other word must be outside at party 2.

Thus no internal party-2 symbol is paired with \(a\) in \(P\), giving
\[
4-r_1(a)=0.
\]
Hence \(r_1(a)=4\), \(p_1(a)=2\), and its unique other maximal word has internal positions \(134\). The party-2 version follows by exchange.

### Five-symbol parties

Away from a singleton’s internal symbol, the identity gives \(r_i(a)\le3\). Five degrees at least two, summing to twelve, must then be
\[
(3,3,2,2,2).
\]

If the four-internal word contains \(a\), then
\[
\tau_i(a)+2=7-2r_i(a).
\]
The lower bound \(r_i(a)\ge2\) forces
\[
r_i(a)=2,\qquad \tau_i(a)=1.
\]

If \(a\) is the singleton’s internal symbol at a five-symbol party, then
\[
\tau_i(a)=8-2r_i(a).
\]
The singleton is not a triple, so
\[
\tau_i(a)\le p_i(a)-1=5-r_i(a).
\]
Together these give \(3\le r_i(a)\le4\).

Degree three leaves the ordinary multiset. Degree four forces
\[
(4,2,2,2,2).
\]
Only the singleton’s internal party can have that exception, so both five-symbol parties cannot be exceptional.

In particular, every degree-two symbol \(\ell\) at a five-symbol party satisfies
\[
\sigma_i(\ell)=0,
\qquad
\tau_i(\ell)+2f_i(\ell)=3.
\]

## 6. Complete verification of the asserted four-edge graph restrictions

Define
\[
M_{12}=(A_1\times A_2)\setminus R_{12}.
\]
It has
\[
|M_{12}|=4\cdot4-12=4
\]
edges, and a vertex at party \(i\in\{1,2\}\) has missing degree \(4-r_i(a)\). Thus its maximum degree is two.

Let \(o_3,o_4\) be the unique outside symbols at the five-symbol parties. There is exactly one maximal word \(v\) using \((o_3,o_4)\).

### F regime

Here \(v\) is internal exactly at parties 1 and 2. The four \(M_{12}\) edges come from:

1. \(v\);
2. the unique triple outside at party 3;
3. the unique triple outside at party 4;
4. the four-internal word.

The edge of \(v\) cannot meet either triple edge. Such an endpoint coincidence would repeat a maximal pair containing \(o_3\) or \(o_4\). Its only possible adjacent edge is the four-internal edge, and injectivity prevents coincidence at both endpoints.

Therefore \(v\)’s edge cannot lie in a cycle. A cycle excluding it would have at most three edges, impossible in a simple bipartite graph. The graph is consequently a linear forest with four edges. The five edge-length partitions give exactly
\[
4P_2,\quad
P_3\sqcup2P_2,\quad
2P_3,\quad
P_4\sqcup P_2,\quad
P_5.
\]

The proof does not impose the stronger, unjustified prohibition on adjacency between the four-internal edge and a triple edge.

### S regime, singleton internal at a five-symbol party

Take its internal party to be 3. The word \(v\), which is outside at party 3, cannot be the singleton, so it is again internal exactly at parties 1 and 2.

The other three \(M_{12}\) edges arise from one triple outside at party 3 and two outside at party 4. Each shares an outside coordinate with \(v\), so endpoint coincidence would repeat a maximal pair. The edge of \(v\) is isolated.

The remaining three edges form a linear forest. Including the isolated edge, the only types are
\[
4P_2,\qquad
P_3\sqcup2P_2,\qquad
P_4\sqcup P_2.
\]

### S regime, singleton internal at a four-symbol party

Take its internal party to be 1. The singleton itself uses \((o_3,o_4)\), so it is \(v\), and it does not produce an internal-\(12\) edge.

All four \(M_{12}\) edges come from triples: two outside at party 3 and two outside at party 4. Each of these two classes is a matching, by maximal-pair injectivity with the corresponding unique outside symbol.

With four edges, the only possible cycle is \(C_4\). Such a cycle uses all edges, giving two degree-two and two isolated vertices on each side. Translating missing degrees back to residual degrees yields
\[
(4,4,2,2)
\]
at both four-symbol parties.

Conversely, those two multisets leave exactly two active missing-graph vertices on each side, each of degree two. The simple graph is necessarily \(K_{2,2}=C_4\).

Thus a cycle forces exactly the conditions claimed in S1. None of these necessary graph types is asserted to extend to a complete common packing or an actual tensor.

## 7. Four-word slices without no-distance-one

Fix an arbitrary degree-two symbol \(\ell\in A_3\). Its residual slice has four distinct words. At each other party exactly two symbols occur, each twice.

Each other coordinate therefore gives a balanced \(2+2\) partition of the same four-word index set. There are three such unordered partitions:

- Different partitions have four singleton intersections, so their coordinate-pair projection is the full product of the two neighbor sets.
- All three partitions cannot coincide, because that would repeat complete support words.

Hence either all three partitions differ, or exactly two coincide.

In the latter case, only the coincident coordinate pair can have a nonfull slice projection. Its two omitted pairs form a matching. Global residual support may supply some of those omitted pairs elsewhere, but it cannot create additional omissions.

It follows that, for
\[
z_{ij}=|M_{ij}\cap(N_i\times N_j)|,
\qquad ij\in\{12,14,24\},
\]
each \(z_{ij}\) belongs to \(\{0,1,2\}\), and at most one is positive.

This retains the exactly-two-equal-partitions alternative. No no-distance-one assumption has been inserted.

## 8. Defect identities and simultaneous maximal-word inequalities

For the fixed low symbol \(\ell\), let \(N_i\) be its two residual neighbors and \(S_i=A_i\setminus N_i\). Then
\[
|S_1|=|S_2|=2,\qquad |S_4|=3.
\]

Set
\[
D_i=\sum_{a\in N_i}r_i(a)-6\quad(i=1,2),
\qquad
H=\sum_{a\in N_4}r_4(a)-4.
\]
The degree classifications give
\[
-2\le D_i\le2,\qquad H\in\{0,1,2\}.
\]

For any missing graph split into \(N/S\) on each side,
\[
z_{ij}-s_{ij}
=\deg_{M_{ij}}(N_i)-\deg_{M_{ij}}(S_j).
\]

In \(M_{12}\), whose total edge count is four,
\[
\deg(N_1)=8-\sum_{N_1}r_1,\qquad
\deg(S_2)=\sum_{N_2}r_2-4.
\]
Therefore
\[
z_{12}=s_{12}-D_1-D_2.
\]

In \(M_{14}\), whose total edge count is eight,
\[
\deg(N_1)=10-\sum_{N_1}r_1,\qquad
\deg(S_4)=\sum_{N_4}r_4.
\]
Hence
\[
z_{14}=s_{14}-D_1-H.
\]
The same calculation gives
\[
z_{24}=s_{24}-D_2-H.
\]

Let \(u_{ij}\) count maximal triples containing \(\ell\) and the indicated other two internal parties, and let \(f\) indicate that the four-internal word contains \(\ell\). The symbol identity gives
\[
u_{12}+u_{14}+u_{24}=3-2f.
\]

Every such maximal triple uses symbols in the corresponding \(S\)-sets: a maximal pair containing \(\ell\) cannot be residual. It contributes a missing edge between those sets. The four-internal word, when present, contributes one for each pair. Injectivity of pair projections on the same \(P\) makes those edges distinct:
\[
s_{ij}\ge u_{ij}+f.
\]

Also \(u_{ij}\le2\), using injectivity with \(\ell\) and the relevant two-element \(S_1\) or \(S_2\).

At least two defects \(z_{ij}\) vanish by §7. Substitution into the exact identities proves that at least two of
\[
u_{12}+f\le D_1+D_2,\qquad
u_{14}+f\le D_1+H,\qquad
u_{24}+f\le D_2+H
\]
hold.

This uses the valid implication from local slice fullness to zero global defect. It does not assume the converse. The argument applies to every low symbol at either five-symbol party, with the same global \(P,E\).

## 9. Regular-stratum matching theorem and sector counts

Suppose the two four-symbol parties have degree three at every residual symbol. Then \(D_1=D_2=0\) for every low-symbol slice.

Assume an arbitrary low symbol \(\ell\in A_3\) has no high neighbor at party 4. Both its neighbors there have degree two, so \(H=0\). The defect identities then give
\[
z_{12}=s_{12},\qquad z_{14}=s_{14},\qquad z_{24}=s_{24}.
\]
Thus at most one \(s_{ij}\) can be positive.

If \(f=1\), all three \(s_{ij}\ge1\), a contradiction. If \(f=0\), the \(u\)-counts sum to three and each is at most two, so at least two are positive. Since \(s_{ij}\ge u_{ij}\), this is again a contradiction.

Every low symbol therefore has a high residual neighbor. The symmetric argument applies at party 4. Because each low symbol has total residual degree two, it has at most one low neighbor. The low-to-low graph is a matching.

### Ordinary five-symbol degree multisets

There are three low and two high symbols on each side. If the low-to-low matching has \(m\) edges, then \(0\le m\le3\). The low degree sums and total high degree sums force

| \(R_{34}\) sector | \(L_4\) | \(H_4\) |
|---|---:|---:|
| \(L_3\) | \(m\) | \(6-m\) |
| \(H_3\) | \(6-m\) | \(m\) |

These are conditional edge counts, not an assertion that every indicated \(m\) extends to an actual tensor.

### One exceptional five-symbol degree multiset

If party 3 has degrees \((4,2,2,2,2)\), it has one high symbol and four low symbols. Party 4 is ordinary.

Each of party 4’s three low symbols must use the unique high symbol at party 3. Its second neighbor is distinct, so it must be low. Hence the low-to-low matching has exactly three edges. Degree sums give

| \(R_{34}\) sector | \(L_4\) | \(H_4\) |
|---|---:|---:|
| \(L_3\) | \(3\) | \(5\) |
| \(H_3\) | \(3\) | \(1\) |

This verifies both supplied tables.

## 10. Additional F-regime restriction

In the regular F regime, let \(\ell\) be the party-3 symbol of the four-internal word. It has degree two and lies in exactly one maximal triple.

Here \(s_{12}\ge1\), and regularity gives \(z_{12}=s_{12}>0\). Therefore the other two defects vanish:
\[
H=s_{14}\ge u_{14}+1,\qquad
H=s_{24}\ge u_{24}+1.
\]

Consequently:

- \(H\ge1\), so \(\ell\) has a high neighbor.
- If its unique triple has internal positions \(134\) or \(234\), then \(H=2\). In F both five-symbol parties are ordinary, so both neighbors are high.
- If it has only one high neighbor, then \(H=1\), forcing \(u_{14}=u_{24}=0\). Its unique triple has internal positions \(123\).

The party-exchanged statement follows as claimed. This restricts F; it does not close F by contradiction.

## 11. Complex phase equations and the remaining implication

For a full nonzero \(2\times2\) block
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
unitarity gives
\[
|a|^2=|d|^2,\qquad
|b|^2=|c|^2,\qquad
|a|^2+|b|^2=1.
\]
Row orthogonality gives
\[
a\overline c+b\overline d=0,
\]
hence
\[
\arg a-\arg b-\arg c+\arg d
\equiv\pi\pmod{2\pi}.
\]

Thus S1’s displayed complex block equations are correct independently of its public citation. If one support decomposes into full residual blocks in all three cuts, assigning residual squared moduli \(1/2\) satisfies all these modulus equations. It does not by itself solve the simultaneous phase equations.

The unresolved global step is exactly substantive:

1. Determine whether complete, distinct \(P,E\) sets can simultaneously satisfy all six pair complements, exact two extensions, the surviving type and graph restrictions, every applicable low-slice constraint, and all-three-cut block closure.
2. If such a support survives, determine simultaneous positive-modulus and arbitrary complex-phase feasibility.

The review supplies neither a compatible support nor a proof that all such supports are impossible. A weak moment, degree, graph, or matching shadow is not a physical witness. Failure of real signs alone would not establish failure of arbitrary complex phases.

## 12. Exact imports and nonconclusions

The proof above reconstructs the interface and moments directly from the actual tensor hypotheses. It agrees with the interface in S2 line 11 and S3 lines 7, 11–12.

It does **not** import:

- The inherited no-OLS-dependent list of all possible residual profiles.
- S3’s no-distance-one-dependent external-partner obstruction.
- The finite-program results described in S2 or S3 as a substitute for this written proof.
- Any held \(t=28\), PH/report, CORE, privacy, or quarantined reviewer episode.
- The public paper’s literature-status statements as verified premises.

The full bodies of S2 and S3 were read because they belong to the frozen packet; their unrelated claims are not thereby newly audited or adopted.

This review does not prove a universal \(t=24\) exclusion, a support-48 exclusion, \(N\ge49\), a product-basis support minimum, or exclusions of \(3555\), \(4555\), or \(5555\). It grants no worldwide novelty, priority, source-equivalence, independent-family, human, or formal/kernel acceptance.

## 13. Final verdict

**Findings:** None meeting the stated evidence-backed defect criteria.

**Overall correctness:** **correct**

**Explanation:** The whole-\(4455\) necessary-condition theorem in S1 is supported by the complete written reconstruction above, including the shared-support interface, both maximal-word regimes, all asserted missing-graph restrictions, and the regular-stratum matching consequences. This does not resolve global \(4455\) realizability, verify the external literature comparison, or authorize automatic parent adoption.

**Confidence:** **0.97**

**Final status:** **COMPLETE WRITTEN REVIEW; NECESSARY-CLASS THEOREM SUPPORTED; FULL \(4455\) EXCLUSION NOT PROVED; NO PHYSICAL WITNESS; PARENT DISPOSITION STILL REQUIRED.**