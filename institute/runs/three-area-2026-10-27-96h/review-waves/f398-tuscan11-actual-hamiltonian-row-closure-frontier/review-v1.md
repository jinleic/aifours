# Author candidate v1: a Hamiltonian parity-support obstruction for actual T2(11)

**Intended file:** `review-waves/f398-tuscan11-actual-hamiltonian-row-closure-frontier/author-candidate-v1.md`

**Status:** AUTHOR CANDIDATE — UNREVIEWED. Complete written proof of a quantified actual-row branch exclusion; **not** an existence or nonexistence proof for unrestricted T2(11). Separate written review and parent disposition remain required.

**Materialization:** This response supplies the complete manuscript. I have not written a repository file or executed scientific code under the active read-only tool-role restriction.

## 1. Result and exact relation to the assigned target

An actual T2(11) consists of eleven rows, each a permutation of the same eleven symbols, such that:

1. every ordered pair of distinct symbols occurs exactly once as a directed distance-one event;
2. every ordered pair of distinct symbols occurs at most once as a directed distance-two event.

For a row \(r=(r_1,\ldots,r_{11})\), define its **odd-position support**

\[
O(r)=\{r_1,r_3,r_5,r_7,r_9,r_{11}\}.
\]

The main result is:

> **Actual-branch exclusion.** For every actual T2(11) and every six-element symbol set \(B\), at most three rows have odd-position support \(B\).
>
> Equivalently, after adjoining the same vertex \(\infty\) to all eleven actual rows, at most three of the resulting Hamilton cycles can alternate across any one common \(6+6\) vertex partition.

Consequently, the following entire actual branches are excluded:

- four or more rows have the same odd-position support;
- the eleven rows collectively use at most three distinct odd-position supports;
- four or more symbol-class Hamilton cycles in the augmented incidence square alternate across a common equipartition.

These conclusions impose **no** hypothesis on the cycle type of the endpoint permutation \(E\), no equality \(M=C\), and no second-column or penultimate-column permutation assumption.

The obstruction is not a selected abstract permutation, a sign calculation, or merely a Latin-degree condition. It uses all eleven actual rows, their exhausted distance-one edge set, the distance-two packing condition, and the fact that each augmented row is one Hamilton cycle.

A uniform version is also proved:

> **Uniform odd-order theorem.** In any actual T2\((2m-1)\), \(m\ge2\), every fixed odd-position support occurs in at most \(\lfloor m/2\rfloor\) rows.

No unrestricted T2(11) witness or no-go is obtained here.

## 2. Inputs, permissions, and chronology

### 2.1 Frozen inputs read

I read the complete manifest, freeze receipt, parent live-metadata supply, and dispatch receipt for this wave. I then read all seven listed controls in full before reading the complete ordered literal packet.

The scientific inputs were exactly the two complete packet sources:

- **S1:** `info-4-tuscan-adjacency-row-closing-derangements-parent-v1.md`, LF 1–22, declared SHA256 `72d608050ac1f115057fc89e2135ce700db38681636081f3f9b6ab7d90b935c5`.
- **S2:** `info-4-t1-cross-row-closing-parity-compatibility-parent-v1.md`, LF 1–25, declared SHA256 `1cfc3b41f42ba9fa118ae1f12790f350f8399876b460c0454db5e04618fe5368`.

The parent-supplied live metadata reports the assigned manifest, receipt, packet, control, and input pins/bytes/LF as matching. I did **not** independently execute a hashing command.

The recorded clock `2026-10-30T10:37:10-0700 PDT` is a **parent observation**, not my native start time or a timestamp of this proof.

### 2.2 Research chronology

The order of work was:

1. read the scope and status controls;
2. read the complete ordered scientific packet;
3. inspect public primary-source material concerning Tuscan squares;
4. develop the written run-count argument below, with further public-source searches interleaved;
5. assemble this complete manuscript.

No separately instrumented arithmetic timestamps were collected.

No held scientific payload, linked held proof, or sibling current outcome was opened as an input. This is a statement of the tool-read frontier, not a cognitive-isolation certificate.

### 2.3 Execution boundary

No scientific executable, solver, CAS, search campaign, test, build, formatter, installation, remote computation, or external-model CLI was run.

The calculations below are displayed written identities and finite integer arithmetic. They are not represented as machine output.

## 3. Actual-row and Hamiltonian incidence interface

Let \(S\) have \(n\ge3\) elements. Let \(R\) be \(n\) permutation rows on \(S\), with all directed distance-one events distinct.

There are \(n(n-1)\) distance-one slots and exactly \(n(n-1)\) ordered pairs of distinct symbols. Therefore every such pair occurs exactly once.

For each symbol \(x\), the outgoing events \(x\to y\), \(y\ne x\), occupy \(n-1\) rows. Since \(x\) occurs once in every row, it is last in exactly one row. The dual argument shows that \(x\) is first in exactly one row.

Thus rows can be indexed by their first symbols \(c\). Write \(E(c)\) for the last symbol. Then \(E\) is a permutation and \(E(c)\ne c\).

Adjoin the same vertex \(\infty\) to every row:

\[
(\infty,r_{c,1},r_{c,2},\ldots,r_{c,n}),
\qquad r_{c,1}=c.
\]

Its successor permutation \(h_c\) is one \((n+1)\)-cycle. The augmented cycles partition all directed edges between distinct vertices of

\[
X=S\cup\{\infty\}.
\]

Indeed:

- finite-to-finite edges are the original exhausted adjacency events;
- \(\infty\to c\) occurs once for each first symbol;
- \(E(c)\to\infty\) occurs once for each last symbol.

Consequently, defining \(H(x,x)=\infty\) and labeling each off-diagonal edge \(x\to y\) by its unique row \(c\) gives the Latin incidence square described in S2. Its non-diagonal symbol classes are the **actual single Hamilton cycles** \(h_c\), not arbitrary cycle covers.

The original distance-two events are only

\[
r_{c,i}\longrightarrow r_{c,i+2},
\qquad 1\le i\le n-2.
\]

They do not include the three augmented square edges

\[
\infty\to r_{c,2},\qquad
r_{c,n-1}\to\infty,\qquad
E(c)\to c.
\]

In particular, uniqueness of all augmented distance-two edges is **not** assumed.

## 4. An exact subset run identity

The following identity is the load-bearing statement.

### Definitions

Fix any \(B\subseteq S\), with \(|B|=b\). In a row, color symbols in \(B\) black and symbols in \(S\setminus B\) white.

For a row \(r\), let:

- \(q_B(r)\): number of maximal black runs in the linear row;
- \(s_B(r)\): number of black runs of length one, including boundary runs;
- \(t_B(r)\): number of white runs of length one that are strictly between two black runs;
- \(d_B(r)\): number of original directed distance-two events whose two endpoints lie in \(B\).

Define

\[
W_B=\sum_{r\in R}\bigl(s_B(r)+t_B(r)\bigr).
\]

If the rows form T2\((n)\), let \(M\) be their missing directed distance-two pairs, and put

\[
\mu_B=|M\cap(B\times B)|.
\]

All these are counts in the same actual rows.

### Lemma 1: per-row identity

For every permutation row,

\[
d_B(r)=b-2q_B(r)+s_B(r)+t_B(r).
\tag{1}
\]

**Proof.** Distance-two events with both endpoints black have exactly two forms:

1. **BBB:** three consecutive black entries within a black run;
2. **BWB:** a white singleton strictly between black runs.

A black run of length \(\ell\) contributes

\[
\max(\ell-2,0)
=\ell-2+\mathbf 1_{\ell=1}
\]

events of the first form. Summing over black runs gives \(b-2q_B(r)+s_B(r)\).

Every internal white singleton contributes exactly one event of the second form. There are \(t_B(r)\) of them. The two forms are disjoint and exhaustive. ∎

### Lemma 2: adjacency determines the total number of black runs

For actual T1\((n)\),

\[
\sum_{r\in R}q_B(r)=b(n-b+1).
\tag{2}
\]

**Proof.** A row has \(b-q_B(r)\) adjacent black-to-black events. Across all rows, the exhausted adjacency condition gives exactly \(b(b-1)\) such events. Therefore

\[
nb-\sum_rq_B(r)=b(b-1),
\]

which is (2). ∎

### Theorem 1: exact singleton-run budget

For every actual T2\((n)\) and every \(B\subseteq S\),

\[
\boxed{W_B=b(n+1-b)-\mu_B.}
\tag{3}
\]

In particular,

\[
\boxed{W_B\le b(n+1-b).}
\tag{4}
\]

**Proof.** Summing (1) and using (2),

\[
\begin{aligned}
\sum_r d_B(r)
&=nb-2b(n-b+1)+W_B\\
&=b(2b-n-2)+W_B.
\end{aligned}
\]

Distance-two injectivity gives

\[
\sum_r d_B(r)=b(b-1)-\mu_B.
\]

Equating these expressions yields

\[
W_B=b(b-1)-\mu_B-b(2b-n-2)
=b(n+1-b)-\mu_B.
\]

Since \(\mu_B\ge0\), (4) follows. ∎

The equality, not just the upper bound, will identify the unexcluded tight boundary later.

## 5. Hamiltonian interpretation of the budget

Color \(\infty\) white. For an augmented Hamilton cycle \(h_c\), call a vertex a **singleton vertex** if both of its cycle neighbors have the opposite color.

Then

\[
s_B(r_c)+t_B(r_c)
\]

is exactly the number of singleton vertices in \(S\) on that augmented cycle.

To check the boundary carefully:

- a black singleton at either end of the linear row remains a singleton on the cycle because its new neighbor \(\infty\) is white;
- a finite white singleton is counted precisely when it lies internally between black entries;
- a white boundary run joins the white vertex \(\infty\), so its finite boundary entry is not a singleton;
- \(\infty\) itself is deliberately not counted.

Thus Theorem 1 can equivalently be written

\[
\sum_{c\in S}
\#\left\{
x\in S:
h_c^{-1}(x),h_c(x)
\text{ both have color opposite to }x
\right\}
=b(n+1-b)-\mu_B.
\tag{5}
\]

This is where the actual Hamiltonian-row interpretation enters explicitly. A general Latin incidence square whose symbol classes are disconnected cycle covers does not automatically supply the linear permutation rows or their run counts used in the proof.

## 6. Complete exclusion of the common parity-support branch

### Theorem 2: uniform odd-order multiplicity bound

Let \(m\ge2\), \(n=2m-1\), and let \(R\) be an actual T2\((n)\). For any \(m\)-element subset \(B\subseteq S\), define

\[
k_B=
\#\left\{
r\in R:
\{r_1,r_3,\ldots,r_{2m-1}\}=B
\right\}.
\]

Then

\[
\boxed{(2m-1)k_B\le m^2-\mu_B}
\tag{6}
\]

and hence

\[
\boxed{k_B\le\left\lfloor\frac m2\right\rfloor.}
\tag{7}
\]

**Proof.** Every row counted by \(k_B\) has the alternating color word

\[
B,\bar B,B,\bar B,\ldots,\bar B,B.
\]

It has \(m\) singleton black runs and \(m-1\) internal singleton white runs. Its contribution to \(W_B\) is therefore \(2m-1\).

All other rows contribute a nonnegative number. Applying (3) with \(b=m\) gives

\[
(2m-1)k_B\le W_B
=m((2m-1)+1-m)-\mu_B
=m^2-\mu_B.
\]

Thus

\[
k_B\le\left\lfloor\frac{m^2}{2m-1}\right\rfloor.
\]

For \(m\ge2\),

\[
\frac m2
\le
\frac{m^2}{2m-1}
<
\frac{m+1}{2}.
\]

Taking floors, separately for even and odd \(m\), gives

\[
\left\lfloor\frac{m^2}{2m-1}\right\rfloor
=\left\lfloor\frac m2\right\rfloor.
\]

This proves (7). ∎

### Corollary 2.1: the actual T2(11) branch is impossible

For \(n=11\), \(m=6\),

\[
11k_B\le36-\mu_B\le36,
\]

so \(k_B\le3\).

Four rows with a common odd-position support would contribute at least

\[
4\cdot11=44
\]

to a budget of at most

\[
6\cdot6=36.
\]

This is a contradiction.

The displayed integers are written arithmetic, not observed program output.

### Corollary 2.2: at least four distinct supports are required

Every row has exactly one odd-position support. If eleven rows used at most three different supports, one support would occur at least four times. Corollary 2.1 excludes this.

Therefore every actual T2(11) has at least four distinct odd-position supports.

### Corollary 2.3: augmented incidence formulation

Fix any partition

\[
X=A\sqcup B,\qquad
|A|=|B|=6,\qquad
\infty\in A.
\]

At most three actual symbol-class Hamilton cycles can alternate between \(A\) and \(B\).

Indeed, cutting any such cycle at \(\infty\) produces an original row whose odd-position support is exactly \(B\).

This quantifies over every such partition and every collection of actual rows. It is not an assertion about one chosen labeled configuration.

## 7. Connection to \(E\), closing pairs, and the still-live tight boundary

Let

\[
C=\{(E(c),c):c\in S\}.
\]

The proof above never assumes \(M=C\). In the additional branch \(M=C\), however, its equality case has a useful exact form.

### Proposition 3: three common supports in the \(M=C\) branch

Suppose an actual T2(11) satisfies \(M=C\), and exactly three rows have the same odd-position support \(B\), \(|B|=6\). Then:

1. exactly three closing pairs lie in \(B\times B\);
2. the remaining eight rows contribute zero to \(W_B\);
3. in each of those eight augmented Hamilton cycles, every monochromatic run has length at least two.

**Proof.**

Each of the three alternating rows starts and ends in \(B\), so its closing pair lies in \(B\times B\). The pairs are distinct. As \(M=C\), this gives

\[
\mu_B\ge3.
\]

Their contribution to \(W_B\) is \(33\), while Theorem 1 gives

\[
W_B=36-\mu_B.
\]

Hence

\[
33\le36-\mu_B\le33.
\]

Therefore \(\mu_B=3\), \(W_B=33\), and all other rows contribute zero.

By the Hamiltonian interpretation, no finite vertex is a singleton in any remaining cycle. Also, \(\infty\) cannot be a singleton in a remaining cycle: that would mean the row starts and ends in \(B\), creating a fourth closing pair in \(B\times B\). Thus those cycles have no singleton monochromatic run at all. ∎

This is a necessary structural conclusion, **not an exclusion** of the three-row branch.

For completeness, its remaining run counts can also be stated exactly. Let \(r_i\) be the number of black runs in each of the eight remaining augmented cycles. Since each black run has length at least two and \(B\) has six vertices,

\[
1\le r_i\le3.
\]

The augmented adjacency decomposition has \(2\cdot6\cdot6=72\) directed cross-partition edges. The three alternating cycles consume \(36\), leaving \(36\) for the other eight. A cycle with \(r_i\) black runs has \(2r_i\) cross-partition edges, so

\[
\sum_{i=1}^{8}r_i=18.
\]

Writing \(u_j=\#\{i:r_i=j\}\), the remaining possibilities satisfy exactly

\[
u_1+u_2+u_3=8,\qquad
u_1+2u_2+3u_3=18,
\]

or

\[
u_3=u_1+2,\qquad
u_2=6-2u_1,\qquad
0\le u_1\le3.
\]

These integer conditions have not been shown realizable or contradictory.

Without \(M=C\), three common supports give only

\[
0\le\mu_B\le3,\qquad
\sum_{\text{other eight rows}}
(s_B+t_B)=3-\mu_B.
\]

The stronger zero-singleton conclusion must not be exported to that broader branch.

## 8. What has and has not been proved

### Proved in this author manuscript

Subject to separate review of the written argument:

- the exact subset identity (3) for every actual T2\((n)\), every \(n\ge3\), and every symbol subset;
- the uniform odd-order support-multiplicity bound (7);
- exclusion of every actual T2(11) branch with four rows sharing an odd-position support;
- exclusion of every actual T2(11) branch using at most three such supports;
- the precise conditional structure in Proposition 3.

### Not proved

- existence of any actual T2(11);
- nonexistence of unrestricted T2(11);
- impossibility of three rows sharing an odd-position support;
- sufficiency of the singleton budgets;
- realization or exclusion of an endpoint-permutation cycle type merely from its cycle type;
- realization or exclusion of an arbitrary collection of local closing derangements;
- any additional consequence of the joint sign identity in S2;
- independence of this inequality from every previously known Tuscan invariant;
- novelty, priority, human acceptance, independent-family verification, or kernel verification.

All configurations with at least four distinct odd-position supports, each occurring at most three times, remain unpaid **unless independently excluded by other valid work**. This manuscript supplies no claim about which of those configurations actually exist.

## 9. Why the result is an actual branch proof

The contradiction does not begin with freely chosen local permutations and then infer that they describe rows.

Its premises are the original eleven actual permutation rows. From those rows:

1. their adjacency events exhaust the same directed graph;
2. their black-run totals are fixed by that exhausted graph;
3. their distance-two slots are counted in those same rows;
4. distance-two injectivity bounds the total internal-\(B\) events;
5. four alternating Hamilton rows force a singleton count exceeding the resulting exact budget.

In particular, there is no separate choice of an \(E\), incidence square, row cycle, or closing permutation at different stages. The endpoint map and augmented Hamilton cycles are all induced by the same actual rows.

The proof is insensitive to whether the local closing permutations happen to be derangements and whether their product sign agrees with \(\operatorname{sign}(E)\). Satisfying those conditions cannot repair the contradiction \(44>36\).

Conversely, satisfying this new necessary bound does not certify that an abstract incidence object is Hamiltonian or that it realizes T2(11).

## 10. Public attribution and status limitations

Two public primary-source records were inspected.

1. **Tuvi Etzion, Solomon W. Golomb, Herbert Taylor, “Tuscan-K squares,” _Advances in Applied Mathematics_ 10(2), 164–174 (1989).**  
   DOI: [10.1016/0196-8858(89)90009-2](https://doi.org/10.1016/0196-8858(89)90009-2).  
   The [Technion publication record and abstract](https://cris.technion.ac.il/en/publications/tuscan-k-squares/) explicitly describe reviewing computer-found Tuscan-2 squares and discussing nine questions. They also state results about polygonal-path circular Tuscan arrays. Those results concern specified stronger structures and are not used to assert a no-go for the present unrestricted target. The publisher full-text request returned HTTP 403; I did not read the full 1989 paper.

2. **Christopher D. Rosin, “Using Reasoning Models to Generate Search Heuristics that Solve Open Instances of Combinatorial Design Problems,” arXiv:2505.23881v1 (2025).**  
   [Primary text](https://arxiv.org/html/2505.23881v1).  
   Table 2 includes Tuscan-2 squares among the studied Handbook problems, and the supplied definition in Table 6 matches the actual-row target used here: all adjacency pairs exactly once and distance-two pairs at most once. The reported successful open-instance types do not include Tuscan-2. This establishes what that study reports, not the complete current existence status of T2(11).

The run-count theorem above was derived here from the actual-row definition. Neither the searches nor the inspected passages establish that it is new. A novelty comparison against the full Tuscan-square literature remains unperformed.

Search summaries were not used as mathematical evidence.

## 11. Evidence and remaining original-target obligations

**Evidence supplied:** complete definitions, universally quantified identities, proof of the actual excluded branch, precise boundary deductions, and public-source access limitations.

**Scientific code/inputs/output:** none executed; no machine transcript exists. The proof’s specialization uses \(n=11\), \(b=6\), and the contradictory assumption \(k_B\ge4\).

**Verification status:** author-written only. No independent written review, parent mathematical acceptance, finite replay, or formal proof is claimed.

To close the original target, one still needs either:

- an explicit eleven-row permutation array with independently checked uniqueness of all 110 adjacency events and all 99 distance-two events; or
- a proof excluding every remaining actual-row configuration, including those with four or more different odd-position supports and with the full endpoint/incidence/Hamiltonian consistency retained.

The present contribution closes the common-support family completely, but leaves those other branches open.