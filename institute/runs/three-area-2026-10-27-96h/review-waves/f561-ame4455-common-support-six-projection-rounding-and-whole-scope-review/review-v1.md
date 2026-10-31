# F561 — Complete WRITTEN review of the actual AME4455 candidate

**Role:** WRITTEN  
**Overall correctness:** correct at the exact mathematical scope stated below.  
**Mathematical findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Disposition:** **SUPPORTED by this same-harness written reconstruction; UNADOPTED pending parent disposition and the other required gates.**  
**Confidence:** 0.97.

The primary whole-\(4455\) exclusion is supported by a self-contained argument using the same actual tensor and the same maximal and residual supports throughout. The six-projection rounding is also supported, but is not needed by the final direct common-\(P\) contradiction. This review supplies no global support-\(48\) exclusion, support-minimum result, external-source verification, novelty assessment, independent-family verification, human verification, or kernel certification.

## 1. Frozen bindings, coverage, and process

Wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f561-ame4455-common-support-six-projection-rounding-and-whole-scope-review/`

The following metadata is **parent-attributed**, not measured by child execution:

| Artifact | SHA-256 | Parent-reported extent |
|---|---|---|
| Manifest | `28b63f8ffc2039011ee401b7906798702ec569c7fac76cec5bb26155ce90cec3` | 7421 bytes; 119 LF |
| Freeze receipt | `ac6a515306980d279955d368310a621f15d4c70b2a1becd892dd67100cb38f47` | 1852 bytes; 47 LF |
| Literal packet | `ca604c97df433a59c5ba026236ea7a6f3681e13ed39c24b30860b6543e4ff010` | 43496 bytes; 892 LF |
| S1 — complete fresh author candidate | `454a52525b65308d262a181673cb4d43c546347bda338ff47393c89140a62c2e` | 30738 bytes; 858 LF; 859 logical lines |
| S2 — prior regular-four-party disposition | `562a98778d37a4cea3a9bdead0eaad467ee02323932a9b000f21b5a50baf2160` | 6643 bytes; 31 logical lines |

I read the complete manifest, freeze receipt, dispatch receipt, parent-live metadata supply, and all twelve listed status-only controls, including their endings. I then sent a **direct pre-body ACK to Main before opening the mathematical packet**.

After that ACK, I read the complete literal packet in consecutive raw windows of at most twenty lines:

\[
1\!-\!20,\ 21\!-\!40,\ldots,\ 861\!-\!880,\ 881\!-\!892.
\]

This included **every logical line of S1, including line 859**, and **every line of S2, including line 31**. Mathematical reconstruction began only after the complete packet read.

The parent’s live clock observation, **2026-10-30T13:16:27-0700 PDT**, is attributed to the parent. It is not my native start, completion clock, or a measurement of my derivation duration.

The quarantine controls were used only for permissions and exclusions. I did not follow embedded source links, open a sibling review or checker, read held mathematical payloads, or use held episodes or their consumers as mathematical input.

## 2. Exact reviewed theorem and claim dispositions

The reviewed theorem concerns one complex tensor

\[
U=6\psi\in(\mathbb C^6)^{\otimes4}
\]

whose three balanced flattenings are unitary, with exactly \(48\) nonzero entries, exactly \(24\) modulus-one entries, and residual coordinate-alphabet sizes

\[
(q_1,q_2,q_3,q_4)=(4,4,5,5).
\]

No no-distance-one condition, no-OLS condition, real-amplitude restriction, equal-residual-modulus condition, independently chosen pair graphs, or independently chosen maximal supports is assumed.

| Claim | Author logical lines | Review disposition |
|---|---:|---|
| Actual common-\(P,E\) interface and full \(2\times2\) residual blocks | S1:43–109 | **SUPPORTED** |
| Degree classification and unique exceptional-five-party restriction | S1:113–184 | **SUPPORTED** |
| Full-slice twin saturation and disjointness | S1:190–259 | **SUPPORTED** |
| Arbitrary-complex low-to-low obstruction | S1:263–349 | **SUPPORTED** |
| Exclusion of twins at either four-symbol party | S1:353–412 | **SUPPORTED** |
| Forced \(R_{34}\), ordinary five-party profiles, and \(D_2,D_2\) four-party profiles | S1:416–513 | **SUPPORTED** |
| Forced high-symbol twins and actual \(C_3,C_4,T_3,T_4\) structure | S1:517–556 | **SUPPORTED** |
| Same-\(P,E\) rounding at all six physical pair projections | S1:560–631 | **SUPPORTED** |
| Direct common-\(P\) contradiction | S1:635–704 | **SUPPORTED** |
| Whole actual \(4455\) exclusion under the stated hypotheses | S1:12–39, 694, 734–748 | **SUPPORTED** |
| Optional external Euler–Tarry/Betten import and its precise bibliographic/proof claims | S1:708–726 | **INCONCLUSIVE as an independently checked source claim; unnecessary for the primary proof** |
| Worldwide novelty, independent-family/human/kernel certification, global support-\(48\) exclusion or global minimum | S1:750–760 | **Not established or claimed by this review** |

There is no REFUTED mathematical claim in the assigned primary proof. The optional external-source claim is not silently accepted as verified.

## 3. Reconstruction of the actual common-support interface

Define, from the same tensor,

\[
P=\{w:|U_w|=1\},\qquad
E=\{w:0<|U_w|<1\}.
\]

Every entry has modulus at most one because it belongs to a unit-norm row of a unitary flattening. Thus the support assumptions give

\[
|P|=|E|=24.
\]

For any physical pair \(ij\), each modulus-one entry exhausts its row or column in the corresponding balanced flattening. Distinct entries of \(P\) consequently have distinct \(ij\)-projections. Removing their \(24\) exhausted rows and columns leaves a \(12\times12\) unitary matrix with \(24\) nonzero entries.

A remaining row or column cannot have only one nonzero: that entry would have modulus one and belong to \(P\). Every remaining row and column therefore has exactly two nonzeros. Hence, for every physical pair,

\[
|R_{ij}|=12,\qquad
R_{ij}=\pi_{ij}(E),
\]

and each pair in \(R_{ij}\) has exactly two \(E\)-extensions. Moreover,

\[
\pi_{ij}(P)=[6]^2\setminus R_{ij}
\]

injectively.

These are six simultaneous statements about the same \(P,E\), not six separately feasible graph conditions.

For \(a\in A_i\), pair injectivity of \(P\) gives exactly \(p_i(a)\) distinct maximal partners at every other coordinate. Therefore

\[
r_i(a)=6-p_i(a)
\]

is independent of the partner coordinate, the slice through \(a\) contains \(2r_i(a)\) residual words, and

\[
\sum_{a\in A_i}r_i(a)=12.
\]

If \(r_i(a)=1\), all residual words through \(a\) have the same unique value at every other coordinate. The two required extensions would coincide. Thus \(r_i(a)\ge2\).

Finally, two residual rows sharing a column cannot have precisely one common nonzero column, since their inner product would then be a single nonzero term. Their two-column supports coincide. Column degree two then makes this a closed full \(2\times2\) block. Repeating this argument decomposes each residual flattening into six actual nonzero \(2\times2\) unitary blocks.

## 4. Degree classification and coverage of both maximal-word regimes

For a maximal word \(w\), let \(k(w)\) count its internal coordinates. The common-\(P\) complement identities give

\[
\sum_{w\in P}k(w)
=\sum_i(6q_i-12)=60
\]

and

\[
\sum_{w\in P}\binom{k(w)}2
=\sum_{i<j}(q_iq_j-12)=49.
\]

Since

\[
\binom{s}{2}-2s+3
\]

takes the values \(3,1,0,0,1\) for \(s=0,1,2,3,4\), respectively,

\[
3n_0+n_1+n_4=49-2(60)+3(24)=1.
\]

In particular, \(n_0=0\) and \(n_1+n_4=1\). The subsequent argument does not choose between those two regimes.

For an internal symbol \(a\), counting other internal coordinates among its maximal words gives the author’s identities

\[
\tau(a)+2f(a)-\sigma(a)=8-2r_i(a)
\]

at a four-symbol party and

\[
\tau(a)+2f(a)-\sigma(a)=7-2r_i(a)
\]

at a five-symbol party.

Because \(\sigma(a)\le1\), nonnegativity of \(\tau,f\) forces \(r_i(a)\le4\). Combined with the degree sum and lower bound, this gives exactly the listed possible profiles:

\[
D_0=(3,3,3,3),\quad
D_1=(4,3,3,2),\quad
D_2=(4,4,2,2)
\]

for a four-symbol party, and

\[
(3,3,2,2,2)\quad\text{or}\quad(4,2,2,2,2)
\]

for a five-symbol party.

A degree-four five-party symbol requires \(\sigma(a)=1\). Two exceptional five-party profiles would require two different maximal words with exactly one internal coordinate, contrary to \(n_1\le1\). Thus at most one five-party profile can be exceptional.

No maximal-word regime or nonregular four-party profile has been discarded without proof.

## 5. Full-slice twin saturation

Suppose two residual words differ only at coordinate \(i\), through symbols \(a,a'\). Let

\[
T=V_a\cap V_{a'}\ne\varnothing.
\]

For each other coordinate \(j\), the two extensions of a used pair \((a,x_j)\) determine a matching partner in \(V_a\). The rows indexed by \((a,x_j)\) and \((a',x_j)\) share a column in the corresponding actual residual flattening. Block closure forces their other columns to coincide. Thus the matching partner also belongs to \(T\).

There are three perfect matchings on \(T\). They have no loops, and no two can share an edge: two different triples agreeing at two coordinates would, after taking both \(a,a'\) copies, give four extensions of a physical pair. Their union is therefore a simple cubic graph.

For

\[
z_v=U_{a,v}\overline{U_{a',v}}\ne0,
\]

actual row orthogonality gives

\[
z_v+z_{v'}=0
\]

on every matching edge. An odd cycle would imply \(z_v=-z_v\), impossible for a nonzero complex number. The graph is bipartite.

A nonempty simple cubic bipartite component has at least three vertices on each side. Since each slice has at most eight words, \(|T|\) is six or eight.

The possible incomplete saturation must also be ruled out. If an eight-word slice had a six-word overlap, then at every other coordinate the overlap already uses three values twice. The two remaining triples must both use the sole remaining coordinate value, at each of their three coordinates. They would be identical. Hence this incomplete-overlap case is impossible.

Consequently,

\[
V_a=V_{a'},\qquad
|V_a|=|V_{a'}|\in\{6,8\},
\]

and the twin symbols have equal degree three or four.

Three symbols cannot share a nonempty slice, because three copies of any triple would already violate physical-pair multiplicity two. Twin pairs are therefore disjoint symbol pairs. A word cannot belong to twins at two coordinates either: that word and its two separate coordinate flips would give three extensions of the complementary physical pair.

These arguments include the degree-two exclusion and the degree-four partial-overlap case.

## 6. The low-to-low obstruction is genuinely complex

For the author’s explicit normalized low-to-low case, the two extensions are

\[
0000,\qquad1100.
\]

A low slice has four words, with a balanced two-by-two partition at each other coordinate. The fixed low party-\(4\) pair already differs at both parties \(1,2\), so neither of those partitions equals the party-\(4\) partition.

If the party-\(1,2\) partitions were equal to one another, the slice would contain a distance-one pair varying through the low party-\(4\) symbol, which twin saturation forbids. Thus the three partitions are distinct. This forces the two low slices to contain

\[
0000,\ 1100,\ 0101,\ 1001,\ 0110,\ 1010.
\]

In the actual \(13\mid24\) flattening, shared-column block closure then forces \(1111\) and \(0011\). These are exactly the eight even-parity binary words.

Each physical pair used by these eight words has two extensions within this subsystem: fixing two binary coordinates leaves precisely two complementary assignments satisfying the parity condition. Thus the displayed blocks really are closed blocks of the actual residual flattenings.

The phase combinations

\[
X=\theta_{0000}+\theta_{1111},\quad
Y=\theta_{0011}+\theta_{1100},\quad
Z=\theta_{0101}+\theta_{1010}
\]

satisfy the necessary conditions

\[
X-Y\equiv\pi,\qquad
X-Z\equiv\pi,\qquad
Y-Z\equiv\pi
\pmod{2\pi}
\]

from the three author-displayed blocks in cuts \(12\mid34\), \(13\mid24\), and \(14\mid23\), respectively.

For any full nonzero complex unitary block, the phase relation used here follows directly from cancellation of the two nonzero terms in a row inner product. It does not assume real signs or equal entry moduli.

Taking the first congruence minus the second plus the third gives \(0\equiv\pi\pmod{2\pi}\), a contradiction. Therefore a low-to-low pair’s two extensions differ at exactly one complementary coordinate, where full-slice twin saturation applies.

## 7. Exclusion of all four-party twins

If twins occur at a four-symbol party \(i\), an other-coordinate twin component must avoid both of their symbols by component disjointness. But its degree is at least three, so it needs at least three distinct neighbors at party \(i\), where only two symbols remain. Thus no other-coordinate twin can coexist.

Two twin pairs at party \(i\) would both have degree three: their four symbol degrees sum to twelve. Every residual neighbor set at either five-symbol party would then be a union of the two twin pairs. Its degrees would all be two or four, forcing the exceptional profile \((4,2,2,2,2)\) at both five-symbol parties. That contradicts the preceding unique-exception restriction. Hence a four-party twin, if present, is the only twin pair anywhere.

For degree-four twins, the remaining two party-\(i\) symbols are low. At either five-symbol party, the residual symbol omitted by the twins can neighbor only those two remaining symbols and therefore is low and adjacent to both. This produces a low-to-low pair whose required complementary twin is prohibited by isolation.

For degree-three twins, let \(u,v\) be the remaining party-\(i\) symbols. The omitted symbol \(b\) at the other four-symbol party is low and neighbors both \(u,v\). The two omitted symbols at each five-symbol party are also low and neighbor both \(u,v\).

The low symbol \(b\) cannot neighbor a low symbol at a five-symbol party. The required complementary twin would either be at another coordinate, prohibited by isolation, or be the unique original twin pair, whose symbols do not neighbor \(b\).

Thus \(b\) has two high neighbors at each five-symbol party, forcing both five-party profiles to be ordinary. Each of \(u,v\) already has two low neighbors there and must also have a high neighbor to extend its residual pair with \(b\). Hence both have degree at least three. Their degree sum is six, so both have degree exactly three and only one high neighbor at each five-symbol party.

The two required extensions of \((u,b)\) would therefore have identical remaining coordinates. This is impossible.

Accordingly, no distance-one residual pair varies at either four-symbol party, for any of \(D_0,D_1,D_2\). This restriction is derived, not assumed.

## 8. Forced ordinary profiles and the remaining \(D_2,D_2\) case

A low-to-low pair in \(R_{34}\) would require four-party twins. Therefore no such pair exists.

An exceptional five-symbol party has only one high symbol, whereas each opposite low symbol needs two distinct neighbors. Hence both five-party profiles are ordinary, and degree exhaustion gives

\[
R_{34}=(L_3\times H_4)\sqcup(H_3\times L_4).
\]

For \(i=1,2\), define the author’s counts \(x_i(a),y_i(a)\). Counting the same residual words through the two sectors gives

\[
x_i(a)=|N_{i4}(a)\cap H_4|,\qquad
y_i(a)=|N_{i4}(a)\cap L_4|,
\]

and

\[
r_i(a)=x_i(a)+y_i(a).
\]

In a low party-\(3\) slice, the remaining three balanced partitions are either all distinct or have the party-\(1,2\) partitions equal. Equality involving the party-\(4\) partition would create a prohibited four-party distance-one pair. In both allowed cases, every four-party neighbor occurs with both high party-\(4\) symbols. Thus \(x_i(a)>0\) implies \(x_i(a)=2\). The symmetric low party-\(4\) argument gives \(y_i(a)>0\Rightarrow y_i(a)=2\).

Since both sums are six, each function equals two on three symbols and zero on one. Their zero symbols differ, because a common zero would have residual degree zero. Therefore each four-symbol party has:

- one \(a_i^X\) with \((x_i,y_i)=(2,0)\);
- one distinct \(a_i^Y\) with \((x_i,y_i)=(0,2)\);
- two symbols with \((x_i,y_i)=(2,2)\).

This forces \(D_2=(4,4,2,2)\) at both four-symbol parties and gives the actual neighborhoods

\[
N_{i3}(h)=A_i\setminus\{a_i^X\},\qquad
N_{i4}(k)=A_i\setminus\{a_i^Y\}.
\]

All profile pairs containing \(D_0\) or \(D_1\) have thus been excluded without an external no-OLS premise.

## 9. Both high pairs are forced twins in the actual support

The symbol \(a_1^Y\) is low and has two low party-\(4\) neighbors. For either corresponding low-to-low residual pair, the extensions must differ at party \(2\) or party \(3\). The first possibility is prohibited by the derived four-party restriction. They therefore differ between the two high party-\(3\) symbols, and twin saturation makes those symbols full degree-three twins.

The symmetric argument using \(a_1^X\) and a low party-\(3\) neighbor forces the two high party-\(4\) symbols to be full twins.

Consequently,

\[
E=C_3\sqcup C_4,
\]

where \(C_3\) consists of the high party-\(3\) sector and \(C_4\) of the high party-\(4\) sector. The forced \(R_{34}\) makes them disjoint and exhaustive. Each has twelve words.

Their common slices are actual six-element sets

\[
T_3\subseteq A_1\times A_2\times L_4,\qquad
T_4\subseteq A_1\times A_2\times L_3.
\]

The twin matching argument gives a simple cubic bipartite graph on each six-element set. Its two sides have three vertices each, and degree three forces the graph to be \(K_{3,3}\).

Every used coordinate value occurs twice. Projection onto any two non-twin coordinates is injective: otherwise the two triples, each with both twin copies, would supply four extensions of that physical pair.

This establishes the specific actual interfaces needed by rounding; it does not assume that a free-standing \(K_{3,3}\) has been realized by the tensor.

## 10. Explicit audit of all six rounding consumers

For either actual component, choose a bipartition of its actual matching graph and retain the twin symbol indexed by the color of each triple, exactly as in S1:562–580.

Two rules cover all consumers:

1. **Pair not containing the twin coordinate:** the corresponding two-coordinate projection of \(T_i\) is injective. A used pair has one triple and two original twin copies; retaining one copy leaves exactly one extension.
2. **Pair containing the twin coordinate:** the two triples with the specified other-coordinate value form a matching edge. Their colors are opposite, so the retained words use each twin symbol exactly once.

The complete dispatch is:

| Physical pair | \(C_3\to F_3\) | \(C_4\to F_4\) |
|---|---|---|
| \(12\) | Injective \(T_3\) projection onto \(12\) | Injective \(T_4\) projection onto \(12\) |
| \(13\) | Party-\(1\) matching; each party-\(3\) twin once | Injective \(T_4\) projection onto \(13\) |
| \(14\) | Injective \(T_3\) projection onto \(14\) | Party-\(1\) matching; each party-\(4\) twin once |
| \(23\) | Party-\(2\) matching; each party-\(3\) twin once | Injective \(T_4\) projection onto \(23\) |
| \(24\) | Injective \(T_3\) projection onto \(24\) | Party-\(2\) matching; each party-\(4\) twin once |
| \(34\) | Party-\(4\) matching; each party-\(3\) twin once | Party-\(3\) matching; each party-\(4\) twin once |

Before rounding, each used physical pair already has two extensions inside its component. Thus the components cannot share any projected physical pair: sharing would produce four extensions in \(E\). This checks cross-component compatibility rather than assuming it.

It follows that \(F=F_3\sqcup F_4\) contains twelve words and projects bijectively onto every \(R_{ij}\). Since the same \(P\) projects injectively onto its complement,

\[
Q=P\sqcup F
\]

has \(36\) words and projects bijectively onto \([6]^2\) for all six physical pairs.

Hence \(Q\) is an \(\operatorname{OA}(36,4,6,2)\). Taking the actual \(12\)-projection as row and column coordinates, the third coordinate is Latin by \(13,23\), the fourth is Latin by \(14,24\), and their orthogonality follows from \(34\). These are two coordinates of the same \(Q\), not independently gauged Latin squares.

The rounding is a combinatorial selection from the actual support. No amplitude or phase modification, and no new unitary tensor obtained by that selection, is asserted.

## 11. Independent reconstruction of the direct common-\(P\) contradiction

This is the primary endpoint. It needs the conclusions of Section 7 and the common-\(P\) complement identities, but **does not need the rounding or any external no-OLS theorem**.

At party \(1\), write

\[
a_X=a_1^X,\qquad a_Y=a_1^Y,\qquad a_X\ne a_Y.
\]

The outside set \(O_1\) has two symbols, and \(O_4=\{o_4\}\).

For each \(h\in H_3\), the actual residual neighborhood at party \(1\) is \(A_1\setminus\{a_X\}\). Its maximal partners are therefore exactly

\[
O_1\cup\{a_X\}.
\]

For each \(k\in H_4\), its maximal party-\(1\) partners are exactly

\[
O_1\cup\{a_Y\}.
\]

A maximal word with its \(34\)-pair in \(H_3\times H_4\) must consequently have its party-\(1\) symbol in the intersection

\[
\bigl(O_1\cup\{a_X\}\bigr)
\cap
\bigl(O_1\cup\{a_Y\}\bigr)
=O_1.
\]

Now fix \(h\in H_3\). Its residual degree is three, so it occurs in exactly three maximal words. Their party-\(1\) symbols cover \(O_1\cup\{a_X\}\) once each, by actual \(13\)-pair complementarity and injectivity.

Its residual party-\(4\) neighbors are exactly \(L_4\). Hence its three maximal party-\(4\) partners are exactly

\[
H_4\cup\{o_4\},
\]

again once each.

The two maximal words using the two \(H_4\) symbols must have their party-\(1\) symbols in \(O_1\). Injectivity at \(13\) makes those symbols distinct, so these words exhaust the two elements of \(O_1\). The remaining maximal word therefore has

\[
w_1=a_X,\qquad w_4=o_4.
\]

This conclusion applies to both distinct \(h\in H_3\). It produces two distinct maximal words with the same physical \(14\)-pair \((a_X,o_4)\), contradicting injectivity of \(\pi_{14}(P)\).

Every set, neighborhood, complement, and injectivity assertion in this contradiction belongs to the same actual \(P,E\). No separate graph realization or gauge compatibility is left unpaid at this endpoint.

## 12. Imports, findings, and remaining limits

### Load-bearing imports

The primary exclusion uses only:

- the stated three unitary flattenings and exact support/modulus-one counts;
- elementary row/column norm and orthogonality consequences;
- counting on the actual common supports;
- the explicitly reconstructed finite graph facts;
- necessary complex phase congruences.

The prior S2 disposition was read completely at its frozen partial scope. Its linked reviews, executable source, and historical run receipt were not opened or replayed. The present primary reconstruction does not rely on that historical finite run or on S2 as a substitute for reconstructing S1.

The Euler–Tarry/Betten discussion remains an optional external route. I did not follow its URL, verify its bibliographic details, read its figures or proof, or certify its cited classifications. None of that is load-bearing in the direct exclusion above.

### Findings

- **FATAL:** 0.
- **MAJOR:** 0.
- **MINOR:** 0.
- **Unresolved load-bearing mathematical imports in the primary direct proof:** none identified.
- **Optional external theorem/source independently verified here:** no.

### Scientific and operational limits

- Scientific code prepared: **none**.
- Scientific execution, enumeration, solver, CAS, or interpreter checking: **NOT RUN**.
- New selected private graph, parameter, gauge, tensor, state, or diagnostic instance: **not used**.
- New external-source following: **not performed**.
- Builds, tests, lint, or formatters: **not run**.
- External-model CLI or paid/heavy computation: **not used**.
- Git operations, installation, deletion, credentials, or live-infrastructure changes: **not performed**.
- Working-tree changes: **none**; this complete body is returned for parent materialization.
- Child-native clock/hash/runtime/memory/exit measurements: **none claimed**.
- Blindness or cognitive-isolation certification: **not claimed**.
- Parent adoption or completion of other review gates: **not claimed**.

## Final verdict

**SUPPORTED:** the complete fresh author candidate excludes the entire stated actual \(4455\) stratum, including nonregular four-party profiles and both maximal-word regimes, for arbitrary nonzero complex residual amplitudes. Its same-\(P,E\) six-projection rounding is supported, and its primary direct common-\(P\) contradiction closes without an external Euler–Tarry import.

**This is a completed same-harness WRITTEN review, not parent adoption.** Other residual-alphabet strata, other maximal-entry counts, the full support-\(48\) problem, the global AME support minimum, novelty, and independent-family/human/kernel acceptance remain outside this result.