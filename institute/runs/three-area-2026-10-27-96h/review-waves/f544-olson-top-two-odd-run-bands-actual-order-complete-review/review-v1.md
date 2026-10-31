# F544 — Complete WRITTEN review of the top-two odd-projection-run bands

**Disposition:** SUPPORTED at the stated top-two-band scope.  
**Findings:** **FATAL 0 / MAJOR 0 / MINOR 0.**  
**Delivery:** Full review returned for parent materialization; no repository file was written.

## 1. Reviewed input and process boundary

The sole mathematical input was the complete F495 author candidate reproduced as **S1** in the F544 literal packet:

- Source: `review-waves/f495-olson-actual-ordered-dihedral-projection-high-odd-run-frontier/review-v1.md`
- Supplied source SHA256: `f02e2f8def6d00b078be42a7072c9458ea89d23b921e4b5407bed57671ea6ca4`
- Source coverage: **S1 lines 1–377**, including its final cyclic-to-linear reconstruction requirement.
- F544 manifest SHA256: `ed7dca036592af5d5815223eb15b0646e51e0267facdc9c02f996b64406a3beb`
- Freeze-receipt SHA256: `a8c240c69ba6baf79ecdc929df71b20e605ae2cb35b84573a4cdc64e51f53e1c`
- Literal-packet SHA256: `b4d588fd8a00d4fb06f7f30965d4d50fd02fd86a67df880c226a1cb220263eeb`

These hashes are **parent-supplied observations**, not independently executed child hashes.

Before reading the mathematical packet, I completely read the manifest, freeze receipt, all twelve listed status-only controls through their endings, parent metadata supply, and dispatch receipt. I then sent Main a direct administrative pre-body ACK; delivery was confirmed by the messaging tool.

After that ACK, I read the literal packet in order in raw windows of at most twenty lines: 1–20, 21–40, continuing through 341–360 and the final 361–380 request. The last returned packet line was the ending `S1|377`. Mathematical reconstruction began only after that complete read. The supplied source count of 376 LF separators does not omit its 377th textual line.

All references below to **S1 lines** mean this F544 packet’s author source. The earlier dispositions called “S1” and “S2” inside the author’s chronology are **not additional mathematical inputs to this review**.

No cited-but-unpasted source, author code, sibling review, or held scientific payload was opened. Quarantine records were used only for status and exclusion boundaries. No scientific execution, CAS, interpreter, enumeration, tests, or executable checking occurred. No additional concrete field, word, operator, or parameter diagnostic was introduced. The concrete check below is exclusively the author’s explicitly supplied \(p=5\) word and selection.

## 2. Exact statement reviewed

**SUPPORTED — S1 lines 7–16, 47–76, 281–297.**

For every odd prime \(p\), consider an actual linear word in \(D_{2p}\) with \(F=3p-2\) reflection occurrences and the author’s stated rotation assumptions. Delete rotations while retaining reflection-occurrence order, and form maximal constant-label runs in the resulting **cyclic reflection projection**. Let \(o_\pi\) count its odd-length runs.

The candidate establishes:

\[
o_\pi\ge 3p-4
\quad\Longrightarrow\quad
\text{an original-order identity subsequence of exactly }2p
\text{ reflections exists.}
\]

The selected subsequence uses **zero rotations**. Consequently, the proof does not need a rotation-selector theorem or the rotation-gap restrictions. This is a proof applying to every input satisfying the stated assumptions, not a substitution of a diagnostic label problem for the actual-word problem.

I reconstructed both branches: a rich-triple block certificate, and the arithmetic-progression argument when no rich triple exists.

## 3. Finite-field sumset bound

**SUPPORTED — S1 lines 80–124.**

For nonempty \(A,B\subseteq\mathbb F_p\), write \(a=|A|\), \(b=|B|\).

When \(a+b-1\le p\), the contradiction hypothesis

\[
|A+B|\le a+b-2
\]

allows a containing set \(C\) of size \(n=a+b-2<p\). The polynomial

\[
P(X,Y)=\prod_{c\in C}(X+Y-c)
\]

vanishes on \(A\times B\). Its coefficient of \(X^{a-1}Y^{b-1}\) is

\[
\binom{n}{a-1}\ne0\quad\text{in }\mathbb F_p,
\]

because the factorials involved have arguments below \(p\).

The displayed coefficient-extraction identity is valid under the stated total-degree bound. For a monomial \(X^iY^j\), one-variable Lagrange coefficient extraction gives zero if \(i<a-1\) or \(j<b-1\). If neither inequality holds, the bound \(i+j\le a+b-2\) forces \(i=a-1\), \(j=b-1\). Thus the product of the two coefficient functionals extracts exactly the claimed coefficient. Every denominator is nonzero because the grid coordinates are distinct within each set.

Applying this identity to \(P\), whose grid values all vanish, contradicts its nonzero coefficient.

When \(a+b-1>p\), nonempty subsets with combined size \(p+1\) exist; the already proved boundary case gives their sumset size \(p\). Hence

\[
|A+B|\ge\min(p,a+b-1).
\]

Iteration yields the stated bound

\[
|A_1+\cdots+A_t|
\ge
\min\left(p,1+\sum_i(|A_i|-1)\right).
\]

This part is self-contained. No external sumset theorem is needed as an unverified import.

## 4. Rich-triple chronological certificate

**SUPPORTED — S1 lines 128–195.**

For an ordered projection triple \((a,b,c)\),

\[
\Delta(a,b,c)=\{a-b,\ a-c,\ b-c\}
\]

is exactly the set of exponents obtainable by selecting two of those three occurrences in their existing order. A nonconstant triple has at least two exponent values. Indeed, if all three displayed differences were the same value \(d\), the relation \(a-c=(a-b)+(b-c)\) would give \(d=2d\), hence all three differences would vanish.

A rich triple supplies three exponent values.

Cutting immediately before a rich triple leaves \(3p-5\) occurrences after that first block. With \(q=p-3\), both proposed partitions use the entire remaining interval:

\[
2,2,\underbrace{3,\ldots,3}_{q}
\qquad\text{or}\qquad
\underbrace{3,\ldots,3}_{q},2,2.
\]

Their length-three block starts, measured from the beginning of that remaining interval, are respectively

\[
5+3k
\quad\text{and}\quad
1+3k.
\]

These have different residues modulo \(3\). If an intact unique constant triple remains, its start cannot coincide with a length-three block start in both partitions. At least one partition therefore avoids using that constant triple as a block. If the constant triple intersects the removed rich block, there is no intact constant triple left to avoid.

The resulting blocks are:

- one rich triple;
- \(p-3\) other nonconstant triples;
- two pairs.

There are exactly \(p\) blocks. Their exponent-set sizes give

\[
1+\sum_i(|A_i|-1)
\ge 1+2+(p-3)=p.
\]

The reconstructed sumset bound therefore makes their exponent sumset all of \(\mathbb F_p\), including zero.

Choosing one exponent from each set and its corresponding ordered pair selects **two distinct actual occurrences per block**, hence exactly \(2p\) occurrences. Blocks are disjoint and chronological, so these choices do not conflict. Their group product is the rotation with exponent equal to the sum of the chosen exponents, therefore the identity.

### Endpoint \(p=3\)

Here \(q=0\). The partition consists of the rich triple and two pairs; there are no remaining triple blocks requiring avoidance. The rich triple already supplies \(p=3\) exponent values, so the same sumset argument applies. No computational endpoint exception is needed.

## 5. Run classification and the no-rich case

### 5.1 Classification of the top two bands

**SUPPORTED — S1 lines 199–220.**

For the cyclic projection-run lengths,

\[
F-o_\pi
=
\sum_{\ell_j\ \mathrm{odd}}(\ell_j-1)
+
\sum_{\ell_j\ \mathrm{even}}\ell_j.
\]

Each contribution is an even nonnegative integer. Every run other than a singleton contributes at least two. Thus \(F-o_\pi\le2\) permits exactly:

1. all singleton runs;
2. one length-two run, with all other runs singleton;
3. one length-three run, with all other runs singleton.

The first two types have no constant consecutive projection triple. The third has exactly one such cyclic occurrence window. These are properties of the **rotation-deleted cyclic projection**, not of contiguous reflection blocks in the original word.

Also, \(F-o_\pi\) is even and \(F=3p-2\) is odd. Therefore \(o_\pi\ge F-2\) comprises precisely the two possible values \(F-2\) and \(F\), as claimed.

### 5.2 Local arithmetic-progression implication

**SUPPORTED — S1 lines 228–243.**

Suppose no rich consecutive projection triple exists. For a consecutive triple with \(a\ne b\) and \(b\ne c\), put

\[
x=a-b,\qquad y=b-c.
\]

Both are nonzero, and

\[
\Delta=\{x,x+y,y\}.
\]

The value \(x+y\) differs from \(x\), because \(y\ne0\), and differs from \(y\), because \(x\ne0\). Hence \(x\ne y\) would make the triple rich. It follows that

\[
a-b=b-c.
\]

Thus every consecutive triple in a chain with unequal adjacent labels has equal successive differences. The forward increment \(d\) is nonzero, so the entire chain is an arithmetic progression.

### 5.3 The three actual chains

**SUPPORTED — S1 lines 245–260.**

The required chain lengths are correctly obtained:

- **All singleton runs:** a cut of the full cyclic list has \(F\) terms and unequal adjacent labels.
- **One double run \(a_1,a_2\):** cutting between its two occurrences gives the chain starting at \(a_2\) and ending at \(a_1\). It uses all \(F\) occurrences, and the sole equal-adjacent pair is across the omitted closing edge.
- **One triple run \(a_1,a_2,a_3\):** the interval from \(a_3\), through all outside occurrences, to \(a_1\) omits only \(a_2\). It has \(F-1\) terms with unequal adjacent labels.

Crucially, the omission in the third case is at the chain’s closing boundary, not in its interior. Every triple **inside** each linear chain remains a genuinely consecutive triple of the original cyclic projection, including triples crossing the original word’s cut. No newly spliced interior triple is used to invoke the no-rich hypothesis.

The lengths are therefore exactly \(F,F,F-1\). Their minimum is

\[
F-1=3p-3\ge2p
\]

for every odd prime \(p\), with equality when \(p=3\).

### 5.4 Identity from the first \(2p\) terms

**SUPPORTED — S1 lines 262–277.**

The first \(2p\) occurrences have labels

\[
\alpha,\alpha+d,\ldots,\alpha+(2p-1)d.
\]

Pairing them chronologically gives exponent

\[
\sum_{k=0}^{p-1}
\bigl[(\alpha+2kd)-(\alpha+(2k+1)d)\bigr]
=-pd=0
\]

in \(\mathbb F_p\). Their parity is even, so their product is the identity.

This completes the no-rich branch, including \(p=3\), without adding an unproved selector or a finite check.

## 6. Transport to original linear occurrence order

**SUPPORTED — S1 lines 189–195 and 275.**

Both constructions initially describe a selection in a cyclically cut reflection list. The selected occurrences are nevertheless distinct occurrences of the original word. Returning to the original cut cyclically rotates their selected product.

If the cut-order product is \(UV=1\), the original-order product is of the form

\[
VU=U^{-1}(UV)U=1.
\]

This is a conjugation argument in the actual group. It does **not** assume reflections commute. It remains valid when the cut splits the selected list after an odd number of reflections.

Unselected rotations are absent from the subsequence product. Consequently, the constructed identity is an identity of the actual selected letters in their original linear order, not merely of a projected label calculation.

## 7. Author’s explicit \(p=5\) actual-word instance

**SUPPORTED — S1 lines 323–364. Written check only.**

The supplied reflection labels are

\[
(a_1,\ldots,a_{13})
=(0,0,0,1,0,1,2,3,4,0,1,2,3).
\]

The original word places one \(\rho_1\) after each of the first six reflections, followed by reflections \(a_7,\ldots,a_{13}\).

It therefore contains thirteen reflection occurrences and six rotations. Every rotation is separated from the next by a reflection; the cyclic closing boundary also contains no adjacent rotations.

Deleting the rotations produces one length-three zero run, consisting of occurrences \(1,2,3\). Occurrences \(4,\ldots,13\) form ten singleton runs, including at the cyclic closing boundary since \(a_{13}=3\ne a_1=0\). Thus the eleven runs are all odd:

\[
o_\pi=11=3p-4.
\]

The exact author selection checks as follows:

| Reflection occurrence | Position in the original 19-letter word | Label |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 3 | 0 |
| 3 | 5 | 0 |
| 4 | 7 | 1 |
| 6 | 11 | 1 |
| 7 | 13 | 2 |
| 8 | 14 | 3 |
| 10 | 16 | 0 |
| 12 | 18 | 2 |
| 13 | 19 | 3 |

These are exactly ten distinct occurrences in increasing original position, with no rotations selected. Their alternating exponent is exactly the displayed expression:

\[
0-0+0-1+1-2+3-0+2-3=0.
\]

Their even parity and zero exponent give identity in \(D_{10}\).

This checks the author’s **actual original word and exact occurrence selection**. No substitute word, synthetic witness, or new selected instance was used.

## 8. Residual band and first unpaid bridge

### Residual bookkeeping

**SUPPORTED as an exact remaining obligation — S1 lines 287–297.**

Within the assigned high-run domain \(o_\pi\ge p+4\), removing the proved values \(3p-4\) and \(3p-2\) leaves

\[
p+4\le o_\pi\le3p-6,
\qquad o_\pi\ \text{odd}.
\]

The parity restriction follows from the deficit identity above.

- At \(p=3\), this residual is empty; the assigned high-run branch at that prime is covered.
- At \(p=5\), the residual is exactly \(o_\pi=9\).
- The displayed interval remains an unpaid uniform obligation for larger primes.

This is scope bookkeeping, not a claim that those residual words avoid identity subsequences or that no other literature resolves them.

### Deficit-four classification

**SUPPORTED — S1 lines 301–317.**

For \(F-o_\pi=4\), a single positive contribution of four comes from either a length-five odd run or a length-four even run. Two contributions of two come from the three unordered combinations of length-three and length-two runs. Therefore the five listed types are exhaustive:

1. one length-five run;
2. one length-four run;
3. two length-three runs;
4. one length-three run and one length-two run;
5. two length-two runs;

with every other run singleton.

The author correctly limits the existing certificate to individual instances satisfying its rich-triple and at-most-one-constant-triple hypotheses. Neither a uniform certificate nor a sufficient arithmetic chain for every deficit-four word is proved here.

**INCONCLUSIVE / NOT ESTABLISHED by this candidate:** the residual high band, a general rotation sign selector, unrestricted ordered-Olson closure, and all-group closure. Their absence is explicitly disclosed, not a defect in the stated top-two-band theorem.

## 9. Imports, findings, and assurance ceiling

### Exact import boundary

The mathematical reconstruction uses only the definitions and proof arguments in the complete frozen author body:

- the displayed \(D_{2p}\) multiplication law;
- the internally proved finite-field sumset inequality;
- actual chronological occurrence selection;
- cyclic-cut transport by conjugation.

The earlier projection-selector and normal-defect dispositions mentioned in the author’s chronology were not opened or used as theorem premises. This review does not independently authenticate their earlier adoption, the author’s historical access chronology, or an original external source. Those questions are outside this packet’s mathematical reconstruction.

### Findings

- **FATAL:** 0.
- **MAJOR:** 0.
- **MINOR:** 0.
- **REFUTED mathematical claims:** none.

The rich and no-rich branches both reconstruct completely at the stated scope. The \(p=3\) endpoints, original-order transport, and the author’s exact \(p=5\) occurrence witness all check in writing. No repair is required for that scoped theorem.

### Verdict fields

**overall_correctness:** correct

**explanation:** The complete frozen candidate supports the existence of an original-order \(2p\)-reflection identity subsequence whenever \(o_\pi\ge3p-4\), for every odd prime \(p\). It correctly leaves the residual high band unpaid and does not establish either unrestricted original target.

**confidence:** 0.98

This is a completed **WRITTEN review**, not a parent acceptance receipt, finite-execution certificate, independent-family review, human or kernel verification, novelty assessment, original-source authentication, or clean-cognition certificate.