# F543 — WRITTEN review of F495

**Disposition: SUPPORTED at the stated top-two-projection-band scope.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

This is the complete returned review body for parent materialization. No repository file was created or edited.

## 1. Inputs, chronology, and coverage

Before opening the mathematical packet, I completely read the manifest, freeze receipt, parent dispatch receipt, parent live-metadata supply, and all twelve listed status-only controls, including their endings. I then sent a direct administrative pre-body ACK.

After that ACK, I read the literal packet completely and in order, using exact raw windows of at most 20 lines: packet lines 1–20 through 341–360, followed by 361–379. The final line was `S1|377|4. the cyclic-to-linear identity transfer.` Mathematical reconstruction began only after that complete read.

The supplied bindings are:

- Manifest SHA256: `a707b086df53e941db6a9a20947bab6964627af2fe771ee6aea201afc3d900fd`.
- Freeze-receipt SHA256: `ee9ec233d3d7ba1a0191d84e0f5c02016f1eb2b89f672c53736fe245a603ba91`.
- Literal-packet SHA256: `b4d588fd8a00d4fb06f7f30965d4d50fd02fd86a67df880c226a1cb220263eeb`.
- Sole mathematical source: the F495 `review-v1.md`, SHA256 `f02e2f8def6d00b078be42a7072c9458ea89d23b921e4b5407bed57671ea6ca4`, completely represented by `S1|1` through `S1|377`.

The supplied source metadata records 376 LF delimiters and 377 logical lines; the packet contains all 377 labelled source lines. These are supplied metadata bindings, not independently recomputed reviewer hashes. The parent’s recorded clock is not represented as my native clock or execution receipt.

Quarantine records were used only as status/exclusion controls. I did not follow their links, the candidate’s local-body link, the earlier selector or normal-defect sources, author code, sibling reviews, or held scientific payloads.

## 2. Exact supported statement

For every odd prime \(p\), consider an assigned actual linear word in \(D_{2p}\) with exactly \(3p-2\) reflection occurrences, at least \(p+1\) rotation occurrences, and the stipulated singleton cyclic rotation gaps. Delete rotations and count the odd-length maximal constant-label cyclic projection runs, obtaining \(o_\pi\).

The candidate establishes:

\[
o_\pi\ge 3p-4
\quad\Longrightarrow\quad
\text{an original-order identity subsequence of exactly \(2p\) reflections exists.}
\]

Since \(3p-2-o_\pi\) is even and nonnegative, this is precisely the two bands

\[
o_\pi=3p-4,\qquad o_\pi=3p-2.
\]

The selections use zero rotations. The proof retains the assigned actual-word hypotheses but does not need the restrictions on the rotations.

## 3. Per-claim reconstruction

### A. Finite-field sumset lemma — SUPPORTED

**Anchors: S1 lines 80–124.**

Let \(a=|A|\), \(b=|B|\). In the case \(a+b-1\le p\), a hypothetical bound \(|A+B|\le a+b-2\) permits the displayed polynomial of degree \(n=a+b-2<p\), vanishing on \(A\times B\). Its coefficient of \(X^{a-1}Y^{b-1}\) is

\[
\binom{n}{a-1}\ne0\quad\text{in }\mathbb F_p,
\]

because all factorial arguments are below \(p\).

The displayed coefficient-extraction identity is valid under the stated total-degree bound. Applied to a monomial \(X^rY^s\), its right-hand side factors into the two one-variable Lagrange coefficient sums. If \(r<a-1\) or \(s<b-1\), one factor vanishes. Otherwise, the total-degree bound forces \(r=a-1\) and \(s=b-1\), for which both factors equal one. Thus the right-hand side extracts exactly the claimed coefficient. All denominators are products of differences of distinct field elements and are nonzero.

Vanishing on the grid therefore contradicts the nonzero coefficient. The boundary \(a+b-1=p\) is included: the polynomial degree is \(p-1\), not \(p\).

When \(a+b-1>p\), the required nonempty subsets with total cardinality \(p+1\) exist. Applying the already proved boundary case gives their full-field sumset, and hence \(A+B=\mathbb F_p\). Iteration yields the stated bound for any finite collection of nonempty sets.

No omitted P2 argument or external sumset theorem is needed.

### B. Ordered-pair exponent sets and chronological certificate — SUPPORTED

**Anchors: S1 lines 67–76 and 128–195.**

For a triple of actual reflection occurrences with ordered labels \((a,b,c)\), its three possible two-occurrence selections have exponents

\[
a-b,\qquad a-c,\qquad b-c.
\]

These are exactly the elements of \(\Delta(a,b,c)\). A singleton \(\Delta\) would force \(b=c\) from \(a-b=a-c\), and then \(a=b\) by comparison with \(b-c=0\). Consequently, every nonconstant triple has at least two exponents, as required.

After cutting immediately before a rich triple, the remaining interval has length

\[
3p-5=3(p-3)+4.
\]

Writing \(q=p-3\), both displayed partitions cover this interval exactly: two pairs followed by \(q\) triples, or \(q\) triples followed by two pairs.

Their triple starts lie respectively in residue classes \(2\) and \(1\) modulo \(3\). If the unique constant triple remains intact in the interval, its start cannot coincide with a triple-block start in both partitions. At least one partition therefore avoids a constant triple block. If the rich block or cut intersects that window, no intact constant triple remains to obstruct the partition.

This gives exactly \(p\) disjoint blocks: one rich triple, \(p-3\) nonconstant triples, and two pairs. Their exponent sets satisfy

\[
1+\sum_i(|A_i|-1)\ge1+2+(p-3)=p.
\]

The reconstructed sumset lemma therefore guarantees a choice of exponents summing to zero.

The transition from exponent choices to the actual word is sound. Each exponent is realized by two occurrences in its own block; the blocks are disjoint and chronologically ordered. Choosing one realization per block selects exactly \(2p\) distinct occurrences, with no compatibility constraint between blocks. Each pair multiplies to a rotation, so their total product is the rotation whose exponent is the selected sum, namely zero.

For the author-specified boundary \(p=3\), \(q=0\). The rich triple and two pairs still form exactly three blocks; there is no remaining triple block to avoid. No exceptional computation is required.

### C. Classification of the top two bands — SUPPORTED

**Anchors: S1 lines 199–220.**

The identity

\[
F-o_\pi
=
\sum_{\ell_j\text{ odd}}(\ell_j-1)
+
\sum_{\ell_j\text{ even}}\ell_j
\]

correctly counts the defect contributed by each cyclic projection run. Every contribution is nonnegative and even.

A defect of at most two therefore permits exactly:

1. all runs of length one;
2. one run of length two and all other runs of length one;
3. one run of length three and all other runs of length one.

The first two cases contain no constant consecutive triple. The third contains exactly one such occurrence window. This is a classification of the rotation-deleted cyclic projection, not a claim about contiguous constant blocks in the undeleted word.

### D. No-rich-triple alternative and chain lengths — SUPPORTED

**Anchors: S1 lines 224–277.**

For a consecutive triple with both adjacent labels unequal, put \(x=a-b\) and \(y=b-c\). Both are nonzero, so \(x+y\) differs from both \(x\) and \(y\). Absence of a rich triple therefore forces \(x=y\). Successive differences are consequently constant along every chain with unequal adjacent labels.

The three proposed chains have the claimed lengths and preserve original cyclic adjacency:

- In case A, a linear cut uses all \(F\) occurrences.
- In case B, cutting between the two occurrences of the double run removes the sole equal adjacency from the chain interior, again using all \(F\) occurrences.
- In case C, the interval from the final occurrence of the triple run, around the outside reflections, to its first occurrence uses \(F-1\) occurrences. The omitted middle occurrence lies outside that interval; its omission does not create an artificial interior adjacency or triple.

Every interior triple of each chain is thus an original consecutive projection triple. The arithmetic-progression conclusion applies throughout.

All chain lengths are at least \(2p\), including the boundary \(3p-3=2p\) at the author-specified \(p=3\). The first \(2p\) labels have the displayed progression form, and their alternating exponent is

\[
\sum_{k=0}^{p-1}
\bigl[(\alpha+2kd)-(\alpha+(2k+1)d)\bigr]
=-pd=0.
\]

This proves the identity subsequence in the no-rich alternative.

### E. Transfer to original linear occurrence order — SUPPORTED

**Anchors: S1 lines 189–195 and 275.**

Changing from the chosen cyclic cut to the original linear order cyclically permutes the fixed selected list. If its cut-order product is \(UV=1\), the corresponding cyclically shifted product is

\[
VU=U^{-1}(UV)U=1.
\]

Thus the same selected occurrences multiply to the identity in original linear order. Deleting unselected rotations is legitimate for a subsequence and does not alter this selected product. The proof therefore reaches the actual groupword conclusion, rather than stopping at a label-list or sumset surrogate.

### F. Author’s explicit actual-word witness — SUPPORTED

**Anchors: S1 lines 323–364.**

I checked only the author-specified \(p=5\) word and selection, without introducing another instance.

The displayed word has thirteen reflection occurrences and six rotations, with no cyclically adjacent rotations. Its projection has one initial run of three zero labels and ten singleton runs; the final label differs from the initial label. Hence \(o_\pi=11=3p-4\).

The listed occurrence indices are ten distinct indices in original order. Reading them from the displayed word gives exactly the author’s selected labels, whose alternating exponent is

\[
0-0+0-1+1-2+3-0+2-3=0.
\]

This is an actual original-order reflection subsequence, not a synthetic replacement witness.

### G. Residual obligation and deficit-four classification — SUPPORTED as scope bookkeeping

**Anchors: S1 lines 283–317.**

Within the stated high-run domain, removing the two established top bands leaves

\[
p+4\le o_\pi\le3p-6,\qquad o_\pi\text{ odd}.
\]

The author’s stated residuals for \(p=3\) and \(p=5\) follow from these endpoints.

For defect four, the listed run types are complete: one contribution of four comes from a length-five odd run or length-four even run; two contributions of two give the three listed combinations of length-three odd and length-two even runs.

The candidate correctly does **not** claim that its partition or arithmetic-chain argument uniformly handles those remaining words.

## 4. Imports, execution, and assurance ceiling

The reconstructed proof is self-contained at the stated scope. It does not require adoption of the earlier \(p+2\) selector, normal-closure disposition, omitted P2 case argument, or a two-rotation sign equation.

Scientific execution was **NOTRUN**. I used no interpreter, CAS, solver, enumeration, executable checker, new selected field/word/operator/parameter diagnostic, or subagent bypass. The only concrete instance checked was the one explicitly supplied by the author.

This return supplies a written reconstruction within the same harness. It supplies no independent-family, external-model, human, kernel, machine-verification, novelty, original-source-authentication, or unrestricted original-target-closure credit. The separate FINITE gate is not discharged by this return.

## 5. Verdict fields

**Overall correctness:** correct.

**Explanation:** The complete frozen candidate supports the asserted \(o_\pi\in\{3p-4,3p-2\}\) theorem for the assigned actual dihedral words. The sumset argument, chronological partition, no-rich alternative, and transfer to original occurrence order all reconstruct without an identified defect; the lower residual bands and unrestricted ordered-Olson target remain unproved by this candidate.

**Confidence:** 0.98.