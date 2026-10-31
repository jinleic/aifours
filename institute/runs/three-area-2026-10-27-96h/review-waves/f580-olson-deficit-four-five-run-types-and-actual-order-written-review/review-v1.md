# F580 WRITTEN review — Deficit-four run types and actual occurrence order

**Overall correctness: correct within the frozen scope.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**  
**Confidence: 0.98.**

The complete deficit-four theorem is **SUPPORTED** by the written argument. Its five run-type partitions, safe-gap rotation selection, actual group-product consumers, finite-field coverage, and transfer back to the original linear order all reconstruct without an additional hypothesis. This is a same-harness written review, not parent adoption, finite execution, independent-family review, human review, kernel verification, or a novelty determination.

This is the full review body for parent materialization as this wave’s `review-v1.md`. No repository write or write bypass was attempted.

## 1. Binding, read chronology, and boundaries

The reviewed wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f580-olson-deficit-four-five-run-types-and-actual-order-written-review/`

Frozen bindings:

- Manifest SHA256: `7f3362eefc4b6e6be17b16041a33a2d02be41927695ed2c036d2df98accc9684`
- Freeze-receipt SHA256: `03bef5580adc2e3f8b937871ec70c1d3f93e6bafd74249854abdba2db5f4ed7c`
- Literal-packet SHA256: `975aef054e74d53cff63869318f2abe16cd768e02e92a2ed16bac9367cd2e9a3`
- S1, complete author candidate: `abec1a3d3fb205bb0c7cc5926b18e8b0772dbbdf69c0ba509746124786e8f9bc`
- S2, previously adopted top-two-band disposition: `bb7186723a631295f1008f9bea3fc069bcbd89a58ad818f07112f5dd345fe992`

These hash and clock observations are **parent-supplied metadata**, not independently executed reviewer hashing or a reviewer-native clock observation.

Before reading mathematical packet content, I read the complete manifest and freeze receipt, all twelve listed status-only controls through their endings, the complete parent metadata supply, and the dispatch receipt. I then sent a direct administrative pre-body ACK to Main.

After ACK, I read the literal packet consecutively in raw windows of at most twenty lines: 1–20, 21–40, and so on through 461–480, followed by the complete ending at 481–491. This covered all 456 numbered logical lines of S1 and all 33 lines of S2. Both the S1 ending at `S1|456` and the packet ending at `S2|33` were read before derivation. No packet elision remained.

One administrative correction was sent separately: the metadata supply closes at LF111, whereas the ACK had described its terminal range as 1–112. The initial reads already included its complete ending before ACK; this was an over-wide range description, not incomplete coverage.

**Scientific execution: NOTRUN.** No scientific executable, interpreter, CAS, solver, enumeration, replay, or scientific code was used or authored. No new selected field instance, word, group rotation, parameter, or probe was introduced. The only concrete witness reconstructed below is S1’s explicitly supplied \(p=5\) word and its explicitly supplied ten selected positions.

No cited-but-unpasted scientific source, author code, sibling return, prior review body, or held scientific payload was opened. All held episodes and their proof, method, selection, planning, verification, confidence, and reporting consumers remain NONINPUT. This states the observable access boundary, not a cognitive-isolation certificate.

## 2. Exact theorem and imports

**Claim: SUPPORTED.** S1 LF38–58 and LF319–334.

For every odd prime \(p\ge5\), consider an actual linear word in \(D_{2p}\) with:

- exactly \(F=3p-2\) reflection occurrences;
- \(R\ge p+1\) rotation occurrences;
- at most one rotation occurrence in each cyclic gap between consecutive reflection occurrences.

If its rotation-deleted cyclic reflection projection has \(o_\pi=3p-6\) odd-length maximal constant-label runs, then it contains an identity subsequence of exactly \(2p\) actual occurrences, in original linear order, comprising exactly two rotations and \(2p-2\) reflections.

The new theorem is reconstructed from S1 itself. Its sumset argument is supplied and checked rather than imported from an unprovided source. The only earlier mathematical result used in the **frontier union** is the exact previously adopted statement at S2 LF3: the same named actual-word setting is already covered when \(o_\pi\in\{3p-4,3p-2\}\), using zero rotations.

S2’s linked author, review, code, and execution artifacts were not followed. Its historical execution claims are not independently reverified here.

## 3. Actual interior-rotation products

**Claim: SUPPORTED.** S1 LF60–123.

With
\[
(x,e)(y,b)=\bigl(x+(-1)^e y,e+b\bigr),
\qquad
\rho_u=(u,0),\quad \sigma_a=(a,1),
\]
two selected chronological reflections multiply to \(\rho_{a-b}\).

For a projection triple \((a,b,c)\), selecting two reflections and no interior rotation gives
\[
A_0=\{a-b,\ a-c,\ b-c\}.
\]
If all three values coincide, equality of the first two forces \(b=c\), and equality with the third then forces \(a=b\). Thus a nonconstant triple gives \(|A_0|\ge2\).

For a selected rotation in the first interior gap, the actual pair choices give
\[
A^{(1)}_u=\{a-u-b,\ a-u-c,\ u+b-c\}.
\]
The third value correctly retains the rotation as a prefix when the first reflection is omitted:
\[
\rho_u\sigma_b\sigma_c=\rho_{u+b-c}.
\]
There is no erroneous retained minus sign from an unselected reflection. If \(b\ne c\), the first two values are distinct for every \(u\).

For a selected rotation in the second interior gap, the actual values are
\[
A^{(2)}_u=\{a-b+u,\ a-u-c,\ b-u-c\}.
\]
If \(a\ne b\), the last two values are distinct for every \(u\).

Consequently:

- the **first** interior gap is safe when \(b\ne c\);
- the **second** interior gap is safe when \(a\ne b\).

The safety condition concerns the opposite adjacent pair, not necessarily the pair bordering the rotation itself. S1 correctly preserves this routing.

A nonconstant triple cannot have both adjacent pairs equal. Its number of potentially unsafe gaps therefore equals its number of internal equal adjacencies and is at most one.

## 4. Finite-field coverage

**Claim: SUPPORTED.** S1 LF125–170.

The supplied proof establishes
\[
|A+B|\ge\min(p,|A|+|B|-1)
\]
for nonempty subsets of \(\mathbb F_p\).

In the unsaturated case, writing \(a=|A|\), \(b=|B|\), and \(n=a+b-2<p\), a failure permits an \(n\)-element set \(C\) containing \(A+B\). Then
\[
P(X,Y)=\prod_{c\in C}(X+Y-c)
\]
vanishes on \(A\times B\), while its \(X^{a-1}Y^{b-1}\) coefficient is
\[
\binom n{a-1}\ne0\quad\text{in }\mathbb F_p.
\]

The displayed Lagrange coefficient formula applies under the stated total-degree bound. A monomial below either extraction degree contributes zero; a monomial at least as large in both degrees can satisfy that bound only at the target bidegree. The denominators are nonzero because the field elements within each set are distinct. Grid vanishing therefore contradicts the nonzero coefficient. The singleton boundary presents no gap.

When \(a+b-1>p\), nonempty subsets with cardinality sum \(p+1\) reduce the argument to the established boundary case.

Iteration gives
\[
|A_1+\cdots+A_t|
\ge
\min\!\left(p,1+\sum_i(|A_i|-1)\right).
\]
Thus \(p-1\) sets of size at least two cover all of \(\mathbb F_p\). No rich-triple or arithmetic-progression premise is needed for the new construction.

## 5. Two-rotation chronological certificate

**Claim: SUPPORTED, including the consuming side.** S1 LF172–228.

Omit one reflection occurrence \(z\), cut immediately after it, and partition the remaining \(3p-3\) reflection occurrences into \(p-1\) consecutive nonconstant triples.

Let \(B\) count their potentially unsafe interior gaps. Each such gap is an original cyclic reflection gap: no interior triple gap crosses the omitted occurrence. The singleton assumption therefore bounds the number of rotation occurrences in unsafe gaps by \(B\).

The two original gaps incident to \(z\) require explicit treatment. After omission, they lie at the trailing and leading ends of the cut interval, respectively. Their rotations are **boundary rotations**, not unsafe interior rotations. Both may be occupied; the proof does not incorrectly apply a one-rotation bound to their merged boundary.

If \(R\ge B+3\), at least three rotation occurrences are safe-interior or boundary occurrences.

- If a boundary occurrence is available, select it and any other good occurrence.
- Otherwise all good occurrences are interior. Singleton gaps give at most two such occurrences in one triple, so three available occurrences guarantee a choice from two different triples.

Hence no triple receives two selected interior rotations.

For each triple, its actual exponent set is now exactly one of \(A_0,A^{(1)}_u,A^{(2)}_u\), and has at least two values. Each selected block subword has exactly two reflections and therefore even reflection parity, including when its selected rotation becomes a prefix or suffix of that subword.

Every block product is consequently a rotation. Boundary rotations contribute ordinary \(+u\) exponents between these rotation-valued blocks. If their total is \(c\), the actual cut-order product is
\[
\rho_{c+d_1+\cdots+d_{p-1}},
\qquad d_i\in A_i.
\]
The sumset result permits \(d_1+\cdots+d_{p-1}=-c\).

The construction selects exactly
\[
2(p-1)+2=2p
\]
distinct actual occurrences. Disjoint chronological blocks make the reflection choices compatible; the two fixed rotation occurrences are also distinct. No quotient-only selector or incompatible overlapping choice is being substituted for an actual subsequence.

## 6. Complete deficit-four classification and partitions

**Claim: SUPPORTED for all five types.** S1 LF230–317.

For maximal cyclic constant-run lengths \(\ell_j\),
\[
F-o_\pi
=
\sum_{\ell_j\text{ odd}}(\ell_j-1)
+
\sum_{\ell_j\text{ even}}\ell_j.
\]
Every nonsingleton run contributes a positive even integer. Deficit four therefore consists of either one contribution four or two contributions two. This gives exactly the five listed types.

### One length-five run

Omitting its middle occurrence leaves two equal-label occurrences at the beginning and two at the end of the cut interval. No length-three constant fragment remains. All other runs are singleton runs, so every block is nonconstant. Only the two surviving equal-adjacency edges can contribute, giving \(B\le2\).

### One length-four run

Omitting its second occurrence leaves a length-two fragment at the beginning and a singleton at the end. Every triple is nonconstant, and only the length-two fragment can contribute an internal equal adjacency. Thus \(B\le1\).

### Two length-three runs

The three proposed omissions in one run genuinely provide the needed three partition phases.

Represent that run consecutively as \(a_1,a_2,a_3\), and let \(J\) be the index of the first occurrence of the other run in the cyclic representative beginning at \(a_1\). After omission of \(a_i\) and cutting immediately afterward, the other run starts at position
\[
J-i.
\]
These are three consecutive positions as \(i\) ranges over the three proposed omissions. There is no wrap between them: the other run lies outside the first run and remains wholly within the cut interval.

Exactly one residue class starts a block, namely position \(1\bmod3\). At most one omission therefore makes the intact second run a constant triple block. Either of the other two choices avoids that block.

The interrupted first run contributes at most one internal equal adjacency. The intact second run, when not aligned as a block, straddles a block boundary; one of its two equal-adjacency edges crosses that boundary, leaving at most one internal edge. Thus every block is nonconstant and \(B\le2\).

This covers the actual cyclic placement, including runs adjacent across the originally chosen linear cut; it is not an at-most-one-window argument incorrectly reused for two windows.

### One length-three run and one length-two run

Omitting the middle of the length-three run leaves one occurrence at each end. It supplies no internal equal adjacency. The intact length-two run contributes at most one. All blocks are nonconstant and \(B\le1\).

### Two length-two runs

An arbitrary omission cannot create an interior adjacency between its two neighbors: the cut is placed at the omission, so any new cyclic joining is at the boundary, not within a triple. Every triple remains nonconstant. The two original equal-adjacency edges contribute at most two internal edges, giving \(B\le2\).

The stated summary bounds \(2,1,2,1,2\) are therefore justified uniformly in occurrence positions and labels.

## 7. Completion and original linear order

**Claim: SUPPORTED.** S1 LF222–226 and LF319–334.

All five types give \(B\le2\). Since \(p\ge5\) and \(R\ge p+1\),
\[
R-B\ge p-1\ge4,
\]
which is stronger than the certificate’s requirement of three good rotation occurrences.

Returning from the chosen cyclic cut to the original linear word cyclically rotates the selected groupword. This remains true if the original cut falls inside a triple, between selected letters, or inside a rotation gap: selected occurrences retain their circular order.

If the cut product is \(UV=1\), the original-cut product is
\[
VU=U^{-1}(UV)U=1.
\]
The argument uses conjugation of the full selected groupword, not commutation of individual reflections or cut-invariance of a nonidentity exponent. It therefore preserves the actual original-order identity conclusion.

## 8. Supplied concrete witness

**Claim: SUPPORTED by written reconstruction only.** S1 LF336–395.

For the supplied \(p=5\) word, the reflection projection has one length-five zero run and eight singleton runs. Thus \(F=13\), \(R=6\), and \(o_\pi=9\), with singleton cyclic rotation gaps.

The supplied partition after omitting reflection occurrence 3 is
\[
(4,5,6),\ (7,8,9),\ (10,11,12),\ (13,1,2).
\]
The rotations after reflection occurrences 2 and 3 lie on the two sides of the omitted occurrence and are boundary rotations, as required.

The supplied actual positions
\[
1,3,4,6,7,9,13,14,16,17
\]
indeed contain, in original order,
\[
\sigma_0,\sigma_0,\rho_1,\rho_1,
\sigma_0,\sigma_0,\sigma_2,\sigma_3,\sigma_1,\sigma_2.
\]
Their product is
\[
\rho_{0+1+1+0-1-1}=1.
\]
There are exactly ten selected actual occurrences, including exactly two rotations.

This checks the supplied witness and occurrence mapping. It is not machine replay, exhaustive evidence, or an avoiding-word construction.

## 9. Frontier union and unpaid scope

**Conditional frontier union: SUPPORTED.** S1 LF397–418, using only S2 LF3 for the previously adopted bands.

After adoption of the new theorem, the three covered bands would be
\[
o_\pi\in\{3p-6,3p-4,3p-2\}
\]
under the named actual-word assumptions.

The literal remaining high-run interval would be
\[
p+4\le o_\pi\le3p-8,\qquad o_\pi\text{ odd}.
\]
S1’s stated consequences for \(p=3,5,7\) follow at their stated scopes. In particular, the \(p=5\) conclusion closes only this named high-run branch, not unrestricted ordered-Olson.

**Deficit-six bookkeeping and limitation: SUPPORTED.** S1 LF420–443.

The ten displayed run-type patterns exhaust the partitions of deficit six into the allowed positive even run contributions. No deficit-six theorem is established.

The stated limitation of this particular certificate is valid: omission inside a length-six or length-seven run leaves endpoint fragments with total length at least five, so one forces a constant first or last triple. Omission outside leaves an intact long constant interval containing a full triple block. This establishes a limitation of the present partition geometry, not impossibility of another construction.

Lower bands, the displayed residual interval, unrestricted ordered-Olson, all-group closure, original-source equivalence, novelty, and worldwide priority remain unproved here.

## 10. Final disposition

There are **no actionable mathematical findings** against the frozen candidate: **0 FATAL / 0 MAJOR / 0 MINOR**. Historical author-process assertions and prior execution receipts are not independently certified by this review; that limitation is not a defect in the reconstructed theorem.

**Overall correctness: correct.** The frozen argument supports the complete actual ordered deficit-four theorem, including all five run types and every selected-rotation consumer. Parent adoption remains separate, and this return supplies no finite-execution, independent-family, human, kernel, or novelty credit.

**Confidence: 0.98.**