# F579 — Written review of the actual ordered deficit-four certificate

**Role:** WRITTEN  
**Verdict:** SUPPORTED at the exact stated scope.  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Scientific execution and finite replay:** **NOTRUN.**

This is the complete review body for parent materialization. No repository write was attempted.

## 1. Inputs, chronology, and review boundary

Before reading the mathematical packet, I read:

- `manifest-v1.json`, LF 1–119.
- `freeze-receipt-v1.json`, LF 1–47.
- All twelve listed permission/status controls through their endings, using ordered raw windows of at most twenty LF.
- The complete parent metadata supply and dispatch receipt.

I then delivered a direct administrative pre-body ACK to `agent://Main`. Only afterward did I read `literal-packet-v1.md` consecutively in raw windows 1–20, 21–40, continuing through 461–480 and 481–491. There was no elided window. Mathematical reconstruction began after the final packet line.

Complete mathematical coverage was:

| Input | Coverage |
|---|---|
| S1: F568 fresh author candidate | All 456 numbered logical lines, including the final paragraph |
| S2: adopted top-two-band disposition | All 33 numbered lines, including its final exclusion and assurance statement |

The supplied pins are:

| Item | SHA256 |
|---|---|
| Manifest | `d37921b8473195a1ff575473bfdaa8aadef38e8ea92c638b917c3b98082cb0d0` |
| Freeze receipt | `2650ced28295db28e453b3949be37f9aafe22e46347142d034cbe54abd4552ad` |
| Literal packet | `975aef054e74d53cff63869318f2abe16cd768e02e92a2ed16bac9367cd2e9a3` |
| S1 author candidate | `abec1a3d3fb205bb0c7cc5926b18e8b0772dbbdf69c0ba509746124786e8f9bc` |
| S2 adopted disposition | `bb7186723a631295f1008f9bea3fc069bcbd89a58ad818f07112f5dd345fe992` |

These hashes, byte/LF counts, and the clock `2026-10-30T13:47:51-0700 PDT` are **parent-supplied metadata**, not independently executed child checks or a child-native review timestamp.

No author code, sibling review, cited-but-unpasted scientific source, or held scientific payload was opened. The links in S2 LF27 were not followed. All quarantined episodes and their proof, method, selection, confidence, planning, and reporting consumers remained NONINPUT.

This review used formal reconstruction and the example explicitly supplied in S1. No additional concrete word, field instance, rotation assignment, or selected parameter probe was introduced. No interpreter, CAS, solver, enumeration, scientific executable, external-model CLI, or scientific subagent calculation was used. This states the observable work boundary, not a cognitive-isolation certificate.

## 2. Exact theorem reviewed

**SUPPORTED — S1 LF34–58 and LF319–334.**

For every odd prime \(p\ge5\), let an actual linear word in \(D_{2p}\) have:

- \(F=3p-2\) reflection occurrences;
- \(R\ge p+1\) rotation occurrences;
- at most one rotation occurrence in each gap between cyclically consecutive reflection occurrences.

If the rotation-deleted cyclic reflection projection has exactly

\[
o_\pi=3p-6
\]

odd-length maximal constant-label runs, then the original linear word has an identity subsequence of exactly \(2p\) actual occurrences. The construction selects exactly two rotations and \(2p-2\) reflections.

The proof supports the whole stated band, not merely instances with a rich triple or a special placement of the rotations.

## 3. Interior-rotation formulas and their consumers

**SUPPORTED — S1 LF60–123.**

Under the stated multiplication law,

\[
(x,e)(y,b)=(x+(-1)^e y,e+b),
\]

the no-interior-rotation choices from a chronological reflection triple give

\[
A_0(a,b,c)=\{a-b,\ a-c,\ b-c\}.
\]

If all three displayed exponents coincide, comparison forces \(b=c\) and then \(a=b\). Thus a nonconstant triple supplies at least two exponents.

For a selected rotation in the first interior gap, the actual subwords are

\[
\sigma_a\rho_u\sigma_b,\qquad
\sigma_a\rho_u\sigma_c,\qquad
\rho_u\sigma_b\sigma_c.
\]

Their exponents are exactly

\[
A^{(1)}_u(a,b,c)
=
\{a-u-b,\ a-u-c,\ u+b-c\}.
\]

The third choice correctly retains the selected rotation as a **prefix** when the first reflection is omitted. If \(b\ne c\), the first two exponents differ independently of \(u\).

For a selected rotation in the second interior gap, the actual subwords are

\[
\sigma_a\sigma_b\rho_u,\qquad
\sigma_a\rho_u\sigma_c,\qquad
\sigma_b\rho_u\sigma_c.
\]

Their exponents are exactly

\[
A^{(2)}_u(a,b,c)
=
\{a-b+u,\ a-u-c,\ b-u-c\}.
\]

The first choice correctly retains the rotation as a **suffix** when the third reflection is omitted. If \(a\ne b\), the last two exponents differ independently of \(u\).

These are actual ordered products, not a uniform-sign treatment of rotations.

The safe-gap accounting also follows:

- A nonconstant triple with both adjacent pairs unequal has two safe interior gaps.
- A nonconstant triple with one equal adjacent pair has one safe gap and one potentially unsafe gap.
- Two equal adjacent pairs would make the triple constant and are excluded.

Consequently, the number \(B\) of potentially unsafe interior gaps equals the number of equal adjacent pairs lying **within** the triples. The author correctly warns that the potentially unsafe gap need not be the physical gap between the equal labels.

“Potentially unsafe” is sufficient for the argument: such a gap is discarded from the guaranteed budget without claiming that every rotation value placed there actually collapses its exponent set.

## 4. Self-contained finite-field sumset argument

**SUPPORTED — S1 LF125–170.**

When \(a+b-1\le p\), the contradiction polynomial has total degree

\[
n=a+b-2<p.
\]

Its coefficient of \(X^{a-1}Y^{b-1}\) is

\[
\binom{n}{a-1},
\]

which is nonzero in \(\mathbb F_p\), since the relevant factorials have arguments below \(p\).

The displayed coefficient-extraction formula is valid under the total-degree bound. For any monomial other than \(X^{a-1}Y^{b-1}\), at least one variable has degree below its extraction degree; its weighted one-variable evaluation sum therefore vanishes. The indicated monomial contributes one. The grid denominators are nonzero because the elements in each set are distinct.

Thus vanishing on \(A\times B\) contradicts the nonzero coefficient. The singleton boundary is harmless and is explicitly covered.

When \(a+b-1>p\), nonempty subsets with sizes summing to \(p+1\) exist within \(A\) and \(B\). Applying the established case to those subsets gives the full field.

The iterated bound therefore applies to independent choices from the disjoint chronological blocks. For \(p-1\) sets, each of size at least two,

\[
1+\sum_{i=1}^{p-1}(|A_i|-1)\ge p,
\]

so their sumset is all of \(\mathbb F_p\). No rich-triple assumption is needed.

## 5. Two-rotation certificate, including omitted-occurrence boundaries

**SUPPORTED — S1 LF172–228.**

The certificate fixes one omitted reflection occurrence \(z\), cuts immediately after it, and partitions the remaining \(3p-3\) reflection occurrences into \(p-1\) consecutive nonconstant triples.

### Rotation availability

There are at most \(B\) actual rotation occurrences in the potentially unsafe interior gaps, because the original physical gaps are singleton gaps. Hence \(R\ge B+3\) leaves at least three actual rotation occurrences in safe interior or boundary positions.

Two suitable occurrences can be fixed before any within-triple pair is chosen:

- If a boundary occurrence is available, it can be selected together with another available occurrence.
- Otherwise all available occurrences are safe interior occurrences. A triple has only two physical interior gaps, each containing at most one rotation. Three available occurrences therefore cannot all lie inside one triple; two can be selected from different triples.

This guarantees at most one selected interior rotation per triple, exactly as required by the exponent formulas.

### The two gaps incident to \(z\)

Both physical gaps incident to the omitted reflection remain boundary positions. In a cut immediately after \(z\), a selected rotation in the following gap lies before the first triple, while one in the preceding gap lies after the last triple.

These are distinct original physical gaps and may contribute two distinct rotation occurrences. The proof does not incorrectly impose a new singleton condition on a merged gap after deleting \(z\).

### Fixed boundary offset and block independence

Once the two rotations are selected, each triple receives precisely its applicable exponent set: \(A_0\), \(A^{(1)}_u\), or \(A^{(2)}_u\). Each set has at least two elements.

Every selected block subword contains exactly two reflections and hence has even reflection parity. Its product is therefore a rotation, including when its assigned selected interior rotation becomes a prefix or suffix after omitting a reflection.

The selected boundary rotations are fixed actual occurrences. Their sum \(c\) is independent of the choices of reflection pairs. Because the completed block products all have even reflection parity, the full cut-order product is indeed

\[
\rho_{\,c+\sum_i d_i},
\qquad d_i\in A_i.
\]

The proof commutes only rotation-valued factors after forming the chronological block products. It does not freely permute reflections.

The full-field sumset supplies choices with \(\sum_i d_i=-c\), proving identity in cut order.

## 6. Completeness of the five deficit-four partition types

**SUPPORTED — S1 LF230–317.**

The deficit identity assigns to each odd run the contribution \(\ell-1\), and to each even run the contribution \(\ell\). Every positive contribution is even.

Total contribution four therefore gives exactly:

1. One length-five run.
2. One length-four run.
3. Two length-three runs.
4. One length-three run and one length-two run.
5. Two length-two runs.

All other runs are singletons.

The proposed partitions cover all five types.

### One length-five run

Omitting its middle occurrence leaves length-two fragments at the two ends of the cut interval. Neither can contain a full triple. All other runs are singletons, so every block is nonconstant. Only the two surviving equal adjacencies can contribute to \(B\), giving \(B\le2\).

### One length-four run

Omitting the second occurrence leaves a length-two fragment at the beginning and one occurrence at the end. No constant triple remains, and \(B\le1\).

### Two length-three runs

Omitting an occurrence of the first run interrupts that run. The only possible constant triple block is the intact second run.

As the omitted occurrence advances through the three positions of the first run, the starting position of the second run relative to the cut changes through three consecutive integers. There is no intervening wrap because that second run is outside the first run. Exactly one residue class can align its start with a triple-block start. Thus at most one omission is bad, leaving a good omission.

For a good omission:

- The interrupted first run contributes at most one internal equal adjacency.
- The intact second run straddles a block boundary rather than forming a block, so it also contributes at most one internal equal adjacency.

Hence \(B\le2\).

### One length-three run and one length-two run

Omitting the middle of the length-three run leaves one occurrence at each end of the interval. They cannot form an internal equal adjacency across the cut. Only the length-two run can contribute, giving \(B\le1\).

### Two length-two runs

There is no constant triple window. Cutting at the omitted occurrence does not create a new adjacency inside the remaining interval: the two sides of the omission become the interval’s ends. Every block is nonconstant, and the two length-two runs contribute at most two internal equal adjacencies.

Thus \(B\le2\) uniformly over all five types.

## 7. Actual rotation budget, distinctness, and original cut

**SUPPORTED — S1 LF216–226 and LF319–334.**

The actual hypotheses give

\[
R-B\ge p+1-2=p-1\ge4.
\]

This is stronger than the three available safe/boundary occurrences required by the certificate.

The selected reflections are distinct because two are chosen from each of \(p-1\) disjoint triples. The omitted occurrence \(z\) is never selected. The two selected rotation occurrences are distinct and are different physical occurrences from all reflections. The selected length is therefore exactly

\[
2(p-1)+2=2p.
\]

Returning from the cut to the original linear word cyclically rotates the selected groupword. The stated identity

\[
VU=U^{-1}(UV)U
\]

shows that \(UV=1\) implies \(VU=1\). This restores the original occurrence order by conjugation, not by asserting invariance of an arbitrary nonidentity product or commutativity of reflections.

Together, these steps prove the full deficit-four theorem under its stated assumptions.

## 8. Supplied actual-word example

**SUPPORTED as a written witness — S1 LF336–395.**

Only the author’s supplied example was checked.

Its projection has the stated length-five zero run and eight singleton runs, so \(o_\pi=9=3p-6\) at the supplied \(p=5\). The actual word contains thirteen reflections and six singleton-gap rotations.

The listed selected positions retain exactly the displayed original-order letters:

\[
\sigma_0,\ \sigma_0,\ \rho_1,\ \rho_1,\
\sigma_0,\ \sigma_0,\ \sigma_2,\ \sigma_3,\
\sigma_1,\ \sigma_2.
\]

The two chosen rotations are the physical occurrences immediately after reflection occurrences \(2\) and \(3\). With reflection occurrence \(3\) omitted, they are the boundary rotations on the two sides of that omission.

The displayed pairing gives exponent

\[
0+1+1+0-1-1=0,
\]

so this is an identity subsequence of exactly ten actual letters with exactly two rotations.

This is written verification of the supplied witness, not an executed finite check, an avoiding-word claim, or evidence replacing the universal proof.

## 9. Imported top-two bands and exact residual

**SUPPORTED at the stated import scope — S1 LF52–58 and LF397–418; S2 LF3–17.**

The only prior mathematical result imported for the union statement is the supplied adopted disposition S2: under the same actual-word assumptions, the bands

\[
o_\pi=3p-4,\qquad o_\pi=3p-2
\]

have original-order identity subsequences of exactly \(2p\) reflections.

Combining that exact import with the newly supported deficit-four theorem covers the three top odd-projection bands for \(p\ge5\). It leaves precisely

\[
p+4\le o_\pi\le3p-8,
\qquad o_\pi\ \text{odd},
\]

inside the named high-run domain.

The source’s stated consequences at \(p=3,5,7\) agree with this scope. This review does not independently rerun or recertify the historical finite evidence summarized in S2 LF25–31.

## 10. Next-deficit discussion and nonclaims

**SUPPORTED as residual bookkeeping and a limitation of this certificate — S1 LF420–443.**

For deficit six, the positive run contributions can be six, four plus two, or two plus two plus two. Choosing the corresponding odd/even run lengths gives exactly the ten listed types.

The present nonconstant-triple geometry cannot uniformly handle a length-six or length-seven constant run:

- An omission inside the run leaves two end fragments with total length at least five, so one end fragment has length at least three and forces a constant first or last triple.
- An omission outside the run leaves an intact consecutive constant segment long enough to contain a full block of any consecutive triple partition.

This validates the stated obstruction to repeating this certificate unchanged. It does **not** prove failure of the theorem at deficit six, settle the other deficit-six types, or supply a new selection geometry.

## 11. Findings and disposition ceiling

**Candidate findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

No unsupported step was found in the chain from:

1. The five exhaustive deficit-four run types;
2. The nonconstant chronological triple partition with \(B\le2\);
3. Selection of two distinct actual rotations in safe/boundary positions;
4. Correct interior-prefix/suffix sign consumers;
5. The \(p-1\)-set full-field sumset;
6. Exact occurrence count and cyclic-to-original conjugation transfer.

**Recommended disposition:** accept this written gate as supporting the complete stated actual ordered deficit-four theorem and the exact conditional union with S2.

This review does not itself confer parent adoption or satisfy a separate finite gate. It supplies no unrestricted ordered-Olson theorem, lower-band closure, all-group result, independent-family verification, human verification, kernel verification, novelty, worldwide priority, or original-source authentication.

**Overall correctness:** correct.

**Explanation:** The candidate’s full stated deficit-four theorem follows from its self-contained sumset proof, exhaustive partition argument, and correctly routed actual-order rotation products. The remaining high-run interval and the limitation of the present certificate at the next deficit are accurately stated.

**Confidence:** 0.97.