# F459 WRITTEN review — low-slice defects and regular low-to-low matching

**Wave:** `f459-ame4455-low-slice-defect-and-regular-matching-review`  
**Verdict:** **SUPPORTED at the frozen necessary-condition scope.**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Adoption:** Parent disposition remains required. This review does not establish a full \(4455\) exclusion or a physical witness.

## 1. Bindings, access, and method

The assigned manifest SHA is:

`8518e4169ca87622e544bb80b55adb35cbe53f8289c97c192914165ff0090d2f`

The assigned freeze-receipt SHA is:

`af4a7a631c8d93457f3deb11c029c60abc48b0bd33c772cf227e33d093c7e79a`

The packet SHA supplied by the parent is:

`0245d8fe49f825879908441ae207a997c8f0280a512529659f4ac5765c3cb07a`

I read the complete manifest, freeze receipt, dispatch receipt, parent-live-metadata supply, and all ten status-only controls, including their endings. I then delivered a direct administrative pre-body ACK before opening the mathematical packet.

After that ACK, I read the entire literal packet in raw windows of at most 20 lines, through its ending. Coverage includes:

- **S1:** the complete author candidate, logical lines **1–735**, including its final status.
- **S2:** the complete supplied \(4445\) disposition, lines **1–27**, including its final scope restrictions.

The source’s reported 734 LF and its 735 numbered logical lines are recorded as different metadata quantities, not treated as a discrepancy.

All hash, byte-count, LF-count, and clock observations are **parent-attributed**, including the supplied observation `2026-10-30T11:43:56-0700 PDT`. They are not child-executed checks or my native start/completion times.

This review uses written derivation with the supplied formal parameters only. I did not introduce a chosen diagnostic instance, follow source links, read unassigned sibling bodies or programs, access held mathematical payloads, prepare scientific code, or execute scientific calculations. No external-model CLI, interpreter, CAS, solver, enumeration, build, test, lint, or formatter was used. No working-tree file was written or write restriction bypassed; this is the complete body for parent materialization.

## 2. Exact reviewed proposition

Assume one tensor \(U=6\psi\) has three unitary balanced flattenings, exactly 48 nonzero entries, and exactly 24 modulus-one entries. Let \(P\) be those 24 maximal words and \(E\) the remaining 24 residual words. Assume the residual alphabet sizes, after a physical party permutation, are

\[
(q_1,q_2,q_3,q_4)=(4,4,5,5).
\]

The reviewed conclusions are:

1. Every degree-two symbol at either five-symbol party has the stated four-word slice alternative, including exactly two equal coordinate partitions.
2. The three defect identities and common-\(P\) triple inequalities hold simultaneously.
3. If both four-symbol parties are degree-three regular, every low symbol has a high neighbor at the opposite five-symbol party, so the low-to-low residual graph is a matching.
4. The ordinary and exceptional sector counts follow.
5. The additional restriction on the unique four-internal word in the regular F regime follows.

All are **necessary conditions on an actual common tensor**. No sufficiency or existence assertion is reviewed into acceptance.

## 3. Prerequisites reconstructed from the actual tensor

### 3.1 The shared pair-complement interface

**Status: SUPPORTED.**  
**Source:** S1 lines 234–274.

A modulus-one entry of a unitary flattening exhausts its row and column. Thus the 24 entries of \(P\) occupy distinct rows and columns in every balanced cut.

Deleting those rows and columns leaves a \(12\times12\) unitary with 24 nonzeros. No remaining row or column can contain only one nonzero: that entry would have modulus one and would already belong to \(P\). Every remaining row and column consequently has exactly two nonzeros.

The three balanced cuts cover all six physical pair projections. Therefore, for every pair \(ij\),

\[
|R_{ij}|=12,\qquad
R_{ij}=\pi_{ij}(E),
\]

each pair in \(R_{ij}\) has exactly two extensions in \(E\), and

\[
\pi_{ij}(P)=[6]^2\setminus R_{ij},
\]

with \(\pi_{ij}\) injective on \(P\).

For a residual symbol \(a\in A_i\), put

\[
p_i(a)=|\{w\in P:w_i=a\}|.
\]

Counting the six possible partners in any other party gives

\[
r_i(a)=6-p_i(a).
\]

This is independent of the partner party. Also,

\[
|\{w\in E:w_i=a\}|=2r_i(a),
\qquad
\sum_{a\in A_i}r_i(a)=12.
\]

If \(r_i(a)=1\), the two residual words containing \(a\) would have the same unique neighbor at each other coordinate, hence would be the same tensor word. Thus

\[
r_i(a)\ge2.
\]

These statements concern one common \(P,E\), not separately chosen pair interfaces.

### 3.2 Global regimes and the symbol identity needed below

**Status: SUPPORTED.**  
**Source:** S1 lines 278–303 and 343–400.

Let \(k(w)\) count the internal coordinates of \(w\in P\). Pair complementation gives

\[
\sum_{w\in P}k(w)=6\sum_iq_i-48=60
\]

and

\[
\sum_{w\in P}\binom{k(w)}2
=\sum_{i<j}q_iq_j-72=49.
\]

Since \(\binom{s}{2}-2s+3\) takes the values \(3,1,0,0,1\) for \(s=0,1,2,3,4\),

\[
3n_0+n_1+n_4=1.
\]

Hence there are no zero-internal words, and exactly one of the following occurs:

\[
(n_0,n_1,n_2,n_3,n_4)=(0,0,13,10,1)
\]

or

\[
(n_0,n_1,n_2,n_3,n_4)=(0,1,10,13,0).
\]

In particular, the four-internal word, if present, is unique.

For a residual symbol \(a\in A_i\), let \(\tau_i(a)\) count maximal triples containing it, \(f_i(a)\) indicate membership in the four-internal word, and \(\sigma_i(a)\) indicate that it is the internal symbol of the one-internal word.

Counting the other internal coordinates among maximal words containing \(a\) gives

\[
18-q_i-3r_i(a)
=p_i(a)-\sigma_i(a)+\tau_i(a)+2f_i(a).
\]

Substituting \(p_i(a)=6-r_i(a)\) yields

\[
\tau_i(a)+2f_i(a)-\sigma_i(a)
=12-q_i-2r_i(a). \tag{R1}
\]

At a four-symbol party, this implies \(r_i(a)\le4\). Together with the lower bound two and degree sum twelve, the possible degree multisets are

\[
(3,3,3,3),\quad(4,3,3,2),\quad(4,4,2,2).
\]

At a five-symbol party, every symbol other than a possible one-internal symbol has degree at most three. If \(a\) is that one-internal symbol, then

\[
\tau_i(a)=8-2r_i(a)
\]

and

\[
\tau_i(a)\le p_i(a)-1=5-r_i(a).
\]

Thus its degree is at least three and at most four. The five-symbol degree multiset is consequently

\[
(3,3,2,2,2)
\]

or, only at the internal party of the unique one-internal word,

\[
(4,2,2,2,2).
\]

There can be at most one exceptional party.

In particular, a degree-two symbol at a five-symbol party cannot be the one-internal symbol. Equation (R1) therefore becomes

\[
\tau_i(a)+2f_i(a)=3. \tag{R2}
\]

If \(f_i(a)=1\), equation (R1) also forces \(r_i(a)=2\) and \(\tau_i(a)=1\).

These are sufficient prerequisites for the audited slice and matching arguments; no \(4445\)-specific global matching structure is transferred.

## 4. The complete four-word slice alternative

**Status: SUPPORTED.**  
**Source:** S1 lines 451–474; the same general partition observation appears in S2 line 17.

Fix an arbitrary degree-two symbol \(\ell\in A_3\). Its residual slice contains

\[
2r_3(\ell)=4
\]

distinct tensor words. At each other party, it has exactly two residual neighbors, each occurring twice.

Index the four words by a four-element set \(V\). Each of coordinates \(1,2,4\) induces an unordered \(2+2\) partition of \(V\).

There are exactly three such partitions. Two different partitions have four singleton intersections, so their coordinate-pair projection contains all four pairs of the corresponding two-symbol alphabets.

The three coordinate partitions cannot all coincide. If they did, each of the two partition blocks would give repeated identical coordinate triples; with party 3 fixed to \(\ell\), the tensor words would duplicate.

Consequently:

- If all three partitions differ, all three pair projections are full.
- If exactly two partitions coincide, only that coordinate-pair projection is nonfull. It contains a two-edge bijection, and its omitted pairs form the complementary two-edge bijection.

A pair missing globally is necessarily missing from this slice. Therefore

\[
M_{ij}\cap(N_i\times N_j)
\]

can be nonempty for at most one of \(ij=12,14,24\). For that pair it is a submatching with at most two edges. Hence

\[
z_{ij}\in\{0,1,2\},
\qquad
\text{at most one }z_{ij}>0. \tag{R3}
\]

The exactly-two-equal-partitions case is retained. No no-distance-one assumption is used.

**Zero-defect boundary:** \(z_{ij}=0\) says that no pair in the neighbor box is missing from the global residual projection. It does not certify that every such pair occurs in this particular slice. The proof needs only “full slice projection implies zero defect,” not its converse. This review does not construct an actual tensor realizing any converse failure.

## 5. Reconstruction of all three defect identities

**Status: SUPPORTED.**  
**Source:** S1 lines 149–188 and 476–519.

Write

\[
\rho_i=\sum_{a\in N_i}r_i(a).
\]

The slice has

\[
|N_1|=|N_2|=|N_4|=2,
\quad
|S_1|=|S_2|=2,
\quad
|S_4|=3.
\]

The definitions are

\[
D_1=\rho_1-6,\qquad
D_2=\rho_2-6,\qquad
H=\rho_4-4.
\]

The four-symbol degree bounds give

\[
-2\le D_i\le2.
\]

In either five-symbol degree multiset, two distinct symbols have total degree four, five, or six. Thus

\[
H\in\{0,1,2\}.
\]

For a bipartite missing graph, splitting each side into \(N\) and \(S\) gives the exact cancellation

\[
z_{ij}-s_{ij}
=\deg_{M_{ij}}(N_i)-\deg_{M_{ij}}(S_j). \tag{R4}
\]

For \(M_{12}\), there are \(4\cdot4-12=4\) edges. Therefore

\[
\deg_{M_{12}}(N_1)=8-\rho_1,
\]

\[
\deg_{M_{12}}(S_2)
=4-(8-\rho_2)=\rho_2-4.
\]

Substitution into (R4) gives

\[
z_{12}-s_{12}
=12-\rho_1-\rho_2=-D_1-D_2.
\]

For \(M_{14}\), there are \(4\cdot5-12=8\) edges. Its degrees on the two sides are \(5-r_1(a)\) and \(4-r_4(a)\), so

\[
\deg_{M_{14}}(N_1)=10-\rho_1,
\]

\[
\deg_{M_{14}}(S_4)
=8-(8-\rho_4)=\rho_4.
\]

Consequently,

\[
z_{14}-s_{14}
=10-\rho_1-\rho_4=-D_1-H.
\]

The same calculation for \(M_{24}\) gives

\[
z_{24}-s_{24}=-D_2-H.
\]

Thus all three claimed identities hold:

\[
\boxed{
\begin{aligned}
z_{12}&=s_{12}-D_1-D_2,\\
z_{14}&=s_{14}-D_1-H,\\
z_{24}&=s_{24}-D_2-H.
\end{aligned}}
\]

## 6. Common-\(P\) triple counts and simultaneous inequalities

**Status: SUPPORTED.**  
**Source:** S1 lines 190–204 and 521–534.

Let \(u_{ij}\) count maximal triples containing \(\ell\) whose other internal parties are \(i,j\). Let \(f\) indicate whether the unique four-internal word contains \(\ell\).

Equation (R2) gives

\[
u_{12}+u_{14}+u_{24}=3-2f. \tag{R5}
\]

Each indicated pair contains party 1 or party 2. In such a triple, the internal symbol at that party lies in its two-element \(S\)-set, because its pair with \(\ell\) is maximal rather than residual. Injectivity of that projection on \(P\) gives

\[
u_{ij}\le2. \tag{R6}
\]

Every such maximal triple supplies a missing pair in \(S_i\times S_j\). If the four-internal word contains \(\ell\), it supplies one such edge for every pair \(12,14,24\). Pair injectivity on the same \(P\) makes these edges distinct. Therefore

\[
s_{ij}\ge u_{ij}+f. \tag{R7}
\]

By (R3), at least two defects vanish. For each vanishing defect, its exact identity and (R7) give the corresponding inequality. Hence at least two of

\[
\boxed{
\begin{aligned}
u_{12}+f&\le D_1+D_2,\\
u_{14}+f&\le D_1+H,\\
u_{24}+f&\le D_2+H
\end{aligned}}
\]

hold.

The argument applies to every low symbol at party 3 and, after exchanging parties 3 and 4, to every low symbol there. All quantities come from the original common \(P,E\) and their six pair complements. Nothing permits independently readjusting one slice’s interface.

## 7. Regular-four-party low-to-low matching theorem

**Status: SUPPORTED.**  
**Source:** S1 lines 536–566.

Assume every residual symbol at parties 1 and 2 has degree three. Every low-symbol slice then has

\[
D_1=D_2=0.
\]

Suppose a low symbol \(\ell\in A_3\) has no high residual neighbor at party 4. Its two distinct residual neighbors both have degree two, so \(H=0\). The defect identities reduce to

\[
z_{12}=s_{12},\qquad
z_{14}=s_{14},\qquad
z_{24}=s_{24}.
\]

By (R3), at most one of these three \(s\)-counts can be positive.

There are exactly two cases:

- **\(f=1\).** By (R7), all three \(s_{ij}\ge1\), a contradiction.
- **\(f=0\).** By (R5), the three \(u_{ij}\) sum to three. Since each is at most two, at least two are positive. By (R7), at least two \(s_{ij}\) are positive, again a contradiction.

Thus every low party-3 symbol has a high party-4 neighbor. The exchanged argument proves the same assertion for every low party-4 symbol.

Each low vertex has total residual degree two and at least one high neighbor. It therefore has at most one low neighbor. This holds at both ends of the low-to-low graph, which is consequently a matching.

The proof covers both the ordinary and exceptional five-symbol degree strata.

## 8. Exact sector counts

### 8.1 Both five-symbol parties ordinary

**Status: SUPPORTED.**  
**Source:** S1 lines 568–577.

There are three degree-two low symbols and two degree-three high symbols on each side. Let \(m\) be the low-to-low edge count. The matching theorem gives

\[
0\le m\le3.
\]

Each low-side degree sum is six, so both cross-sector edge counts are \(6-m\). Each high-side degree sum is also six, leaving \(m\) high-to-high edges. Thus

\[
\boxed{
\begin{array}{c|cc}
 &L_4&H_4\\ \hline
L_3&m&6-m\\
H_3&6-m&m
\end{array}}
\]

is exact. No assertion that every allowed \(m\) is realized by an actual tensor follows.

### 8.2 One exceptional five-symbol party

**Status: SUPPORTED.**  
**Source:** S1 lines 579–585.

Take party 3 to have degree multiset \((4,2,2,2,2)\). It has four low symbols and one high symbol. Party 4 is ordinary, since there can be at most one exceptional party.

Each of the three low party-4 vertices must have a high party-3 neighbor. There is only one such high vertex. Because the residual graph is simple and the low vertex has degree two, its other neighbor must be low. Hence the low-to-low matching has exactly three edges.

The degree sums then give

\[
\boxed{
\begin{array}{c|cc}
 &L_4&H_4\\ \hline
L_3&3&5\\
H_3&3&1
\end{array}}.
\]

This is a forced sector census, not a physical construction.

## 9. Additional regular F-regime restriction

**Status: SUPPORTED.**  
**Source:** S1 lines 587–604.

Let \(\ell\) be the party-3 symbol of the unique four-internal word. The symbol calculation above gives

\[
r_3(\ell)=2,\qquad f=1,\qquad
u_{12}+u_{14}+u_{24}=1.
\]

The four-internal word gives \(s_{12}\ge1\). Since \(D_1=D_2=0\),

\[
z_{12}=s_{12}>0.
\]

The other two defects must therefore vanish. Their identities and (R7) imply

\[
H=s_{14}\ge u_{14}+1,
\qquad
H=s_{24}\ge u_{24}+1.
\]

Consequently:

- \(\ell\) has at least one high neighbor.
- If its unique maximal triple has internal positions \(134\) or \(234\), then \(H=2\).
- In the F regime there is no one-internal word, so both five-symbol degree multisets are ordinary. Therefore \(H=2\) here means that both residual neighbors are high.
- If \(\ell\) has only one high neighbor, then \(H=1\), forcing \(u_{14}=u_{24}=0\); its unique maximal triple consequently has internal positions \(123\).

The exchanged statement holds at party 4.

The qualification about the F regime matters: “\(H=2\) implies two high neighbors” is justified here by the ordinary degree multiset, not by the definition of \(H\) alone.

## 10. Claim disposition and exact exclusions

| Claim | Status |
|---|---|
| Four distinct residual words with two occurrences of each neighbor symbol | **SUPPORTED** |
| Full-projection / exactly-two-equal-partitions alternative | **SUPPORTED** |
| Missing pairs inside a neighbor box form a submatching of size at most two | **SUPPORTED** |
| At most one positive low-slice defect | **SUPPORTED** |
| Bounds on \(D_1,D_2,H\) and all three defect identities | **SUPPORTED** |
| \(u_{12}+u_{14}+u_{24}=3-2f\), \(u_{ij}\le2\), \(s_{ij}\ge u_{ij}+f\) | **SUPPORTED** |
| At least two of the three common-\(P\) inequalities | **SUPPORTED** |
| Every low vertex has a high neighbor in the regular-four-party stratum | **SUPPORTED** |
| Low-to-low graph is a matching | **SUPPORTED** |
| Ordinary and exceptional sector counts | **SUPPORTED** |
| Additional regular F-regime restriction | **SUPPORTED** |
| Entire \(4455\) exclusion | **NOT ESTABLISHED** |
| Existence of complete compatible \(P,E\), or a physical tensor | **NOT ESTABLISHED** |
| Global phase consistency or impossibility | **NOT ESTABLISHED** |
| Worldwide novelty, priority, or source equivalence | **NOT AUDITED** |

S2 contributes the permitted general four-word partition observation. Its \(4445\)-specific moments, global matchings, contradiction, finite-run claims, and linked artifacts are not used to transfer an exclusion to \(4455\). No linked source or checker was opened or run.

The author’s missing-graph classification in §6 and public-source comparison in §11 were completely read, but this disposition does not expand the frozen slice/matching gate into a separate adoption of those claims.

## 11. Final verdict

**Overall correctness: correct at the frozen review scope.**

The low-slice defect identities, simultaneous common-\(P\) inequalities, regular low-to-low matching theorem, sector counts, and stated F-regime refinement follow by complete written reconstruction from the actual-tensor hypotheses. No defect requiring correction was found; the remaining global support-compatibility and complex-phase questions are not resolved by these necessary conditions.

**Confidence:** 0.98.

**Assurance ceiling:** Same-harness WRITTEN reconstruction only; no independent-family, human, formal/kernel, executable-verification, novelty, or automatic parent-adoption credit.