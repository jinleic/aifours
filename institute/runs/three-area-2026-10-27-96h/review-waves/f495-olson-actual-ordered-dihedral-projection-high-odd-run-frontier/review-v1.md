# F495 author-candidate-v1 — Top two actual cyclic-projection bands

## Status and exact result

**AUTHOR / WRITTEN PROOF CANDIDATE — disjoint mathematical check and parent disposition required.**

For every odd prime \(p\), the assigned actual dihedral word has an original-order identity subsequence of exactly \(2p\) reflection occurrences whenever
\[
o_\pi\ge 3p-4.
\]
This proves the two top possible odd-projection-run bands
\[
o_\pi=3p-4\quad\text{and}\quad o_\pi=3p-2.
\]

The result concerns actual groupword subsequences, not diagnostic label lists. It uses **zero selected rotations**, so it does not rely on an unproved extension of the two-rotation selector or its sign equations.

Complete body also retained at [local://f495-author-candidate-v1.md](local://f495-author-candidate-v1.md).

## Chronology, sources, and runtime boundary

Before opening the scientific packet, I completely read the frozen manifest, freeze receipt, parent metadata, and every listed status/permissions control through its ending, using raw windows of at most 20 LF. I then sent Main a direct pre-body ACK. After that ACK, I read the complete literal packet in order: raw LF 1–20, 21–40, and 41–55, through the final `S2|30` line. Scientific derivation and the written example below began afterward.

The supplied pins are:

- Manifest: `96186744d7f4827f87673829c5a76df66cb72f649dad83bcfc85db2148410a08`.
- Freeze receipt: `9b2dd844dd120923e8b36e14f58b27d53d1a51448e23fd2b63ded4373186b8c2`.
- Literal packet: `c5a9fe3965c8e07de4e5038ede6a2c02b3ff9a8154bf794a7db143ea5555f9fb`.

These are **parent-supplied metadata**, not hashes executed by me. Parent supplies the observation `2026-10-30T12:22:49-0700 PDT` and matching pins/bytes/LF. This is not my native clock, start time, or execution receipt.

The scientific inputs completely read were:

- **S1:** the 23-LF adopted \(p+2\) projection-selector disposition, hash `13dba63b3a47a25746fe2e36a0943801cec87fa78229af204d991c44044ec940`.
- **S2:** the 30-LF normal-defect disposition, hash `258e0b5f031064aeb10cad9ae38e075a58aac9a417a130127a37ee210ac3c767`.

Cited-but-unpasted sources were not opened. The proof below directly establishes its group multiplication, sumset, and cyclic-cut steps. It does not assume the omitted P2 case argument or turn S2’s normal-closure statement into a selection theorem.

All listed quarantines were read as status/permission controls only. No held f111/f320, F439/F444/F448, PH, AME, or other held scientific payload or consumer was opened or used. This is an access/use chronology, not a cognition or provenance certificate.

**Scientific computation: NOTRUN.** The active runtime restrictions preclude scientific executable commands here. No interpreter, shell, device, or subagent bypass was attempted. No executable code was used or authored; there is no omitted computational source, machine output, or finite-enumeration claim. Section 7 is written algebra, not execution.

No repository file was created or edited. This complete body is returned for Main materialization.

## 1. Original target and notation

Work in \(D_{2p}\), with
\[
\rho_u=(u,0),\qquad \sigma_a=(a,1),
\]
and multiplication
\[
(x,e)(y,b)=\bigl(x+(-1)^e y,\ e+b\bigr),
\]
where field coordinates are modulo \(p\) and parity coordinates modulo \(2\).

The input is an actual linear group word with:

- exactly \(F=3p-2\) reflection occurrences;
- \(R\ge p+1\) rotation occurrences;
- singleton cyclic rotation gaps.

Delete all rotations, retaining reflection occurrence order, and form maximal constant-label **cyclic projection runs**. Let \(o_\pi\) be the number of those runs having odd length.

The theorem preserves these input assumptions. Its proof selects only reflections, so it does not need the restrictions on the rotations. It does not replace the input by a quotient or a relaxed diagnostic target.

For two ordered reflection occurrences,
\[
\sigma_a\sigma_b=\rho_{a-b}.
\]
Thus, if \(p\) chronologically separated blocks each supply two reflection occurrences with ordered-pair exponents \(d_i\), their selected product is
\[
\rho_{\sum_i d_i}.
\]

All selections below concern **occurrences**, not merely distinct label values.

## 2. Finite-field sumset fact, with proof

For nonempty \(A,B\subseteq\mathbb F_p\),
\[
|A+B|\ge \min\bigl(p,\ |A|+|B|-1\bigr).
\]

Write \(a=|A|\) and \(b=|B|\). First suppose \(a+b-1\le p\). If
\[
|A+B|\le a+b-2,
\]
enlarge \(A+B\) to a set \(C\) of exactly \(n=a+b-2\) elements and consider
\[
P(X,Y)=\prod_{c\in C}(X+Y-c).
\]
It vanishes on \(A\times B\). Its coefficient of \(X^{a-1}Y^{b-1}\) is
\[
\binom{n}{a-1},
\]
which is nonzero in \(\mathbb F_p\), because \(n<p\).

For a polynomial of total degree at most \(a+b-2\), however, that coefficient equals
\[
\sum_{\substack{x\in A\\y\in B}}
\frac{P(x,y)}
{\displaystyle
 \prod_{x'\in A\setminus\{x\}}(x-x')
 \prod_{y'\in B\setminus\{y\}}(y-y')}.
\]
This identity follows from one-variable Lagrange coefficient extraction. A monomial with \(X\)-degree below \(a-1\) or \(Y\)-degree below \(b-1\) contributes zero; the total-degree bound leaves only the indicated monomial. Every denominator is nonzero.

Since \(P\) vanishes on the grid, the coefficient must be zero, a contradiction.

If \(a+b-1>p\), take nonempty subsets \(A',B'\) with
\[
|A'|+|B'|=p+1
\]
and apply the proved case. It gives \(|A'+B'|=p\), hence \(A+B=\mathbb F_p\).

Iterating yields, for nonempty \(A_1,\ldots,A_t\),
\[
|A_1+\cdots+A_t|
\ge
\min\left(p,\ 1+\sum_i(|A_i|-1)\right).
\]

No external theorem or numerical computation is needed for this use of the sumset bound.

## 3. A chronological block certificate

For a consecutive projection triple with labels \((a,b,c)\), define
\[
\Delta(a,b,c)=\{a-b,\ a-c,\ b-c\}.
\]
These are precisely the exponents obtainable by choosing two of its three ordered reflection occurrences.

A nonconstant triple has at least two distinct such exponents. Call it **rich** if it has three distinct exponents.

### Certificate

Suppose a cyclic reflection list of length \(3p-2\) has:

1. a rich consecutive triple; and
2. at most one constant consecutive triple, counted as an occurrence window.

Then it has an original-order \(2p\)-reflection identity subsequence.

### Proof

Cut immediately before a rich triple and keep that triple as the first block. The remaining linear interval has length
\[
3p-5=3(p-3)+4.
\]
Put \(q=p-3\ge0\). Partition this interval by either of the two length patterns:

- \(2,2\), followed by \(q\) blocks of length \(3\); or
- \(q\) blocks of length \(3\), followed by \(2,2\).

If no constant triple remains, either works.

If a unique constant triple remains and starts at relative position \(j\), a length-three block of the first partition starts at
\[
5+3k\equiv2\pmod3,
\]
whereas one of the second partition starts at
\[
1+3k\equiv1\pmod3.
\]
The same \(j\) cannot be a length-three block start in both partitions. Therefore at least one partition contains no constant length-three block.

For \(q=0\), there are no remaining length-three blocks, so the conclusion is immediate. If the rich block intersected the unique constant triple, no intact constant triple remains.

There are now exactly \(p\) disjoint chronological blocks:

- one rich triple;
- \(p-3\) other nonconstant triples;
- two pairs.

For a pair block, use its single ordered-pair exponent. For a triple block, use its \(\Delta\) set. These exponent-set sizes are respectively
\[
3,\quad \underbrace{\ge2,\ldots,\ge2}_{p-3\text{ sets}},\quad1,\quad1.
\]
Consequently,
\[
1+\sum_i(|A_i|-1)\ge1+2+(p-3)=p.
\]
Section 2 gives
\[
A_1+\cdots+A_p=\mathbb F_p.
\]

Choose exponents summing to zero, and choose the corresponding two actual reflection occurrences in every block. This selects exactly \(2p\) distinct occurrences in cut order, with product \(1\). There are no incompatible simultaneous choices or identifications of equal-valued occurrences.

Finally, rotating the cut of a fixed selected cyclic list changes its product by conjugation. If the cut-order product is \(UV=1\), another cut has
\[
VU=U^{-1}(UV)U=1.
\]
Thus the same selected occurrences, read in the original linear word order, also multiply to \(1\). Unselected rotations have no effect. ∎

## 4. Classification of the top two projection bands

For cyclic projection-run lengths \(\ell_j\),
\[
F-o_\pi
=
\sum_{\ell_j\text{ odd}}(\ell_j-1)
+
\sum_{\ell_j\text{ even}}\ell_j.
\]

Every summand is an even nonnegative integer. Any even-length run contributes at least two.

Thus \(o_\pi\ge F-2\) leaves exactly these possibilities:

**A.** Every projection run has length \(1\).

**B.** Exactly one run has length \(2\); all others have length \(1\).

**C.** Exactly one run has length \(3\); all others have length \(1\).

Cases A and B have no constant consecutive triple. Case C has exactly one constant consecutive triple as a cyclic occurrence window.

This classification concerns the **rotation-deleted cyclic projection**, not actual blocks separated by rotation occurrences.

## 5. Proof of the whole-parameter theorem

Take any word in cases A–C.

If it has a rich consecutive projection triple, section 3 applies.

Otherwise, every consecutive triple \((a,b,c)\) with
\[
a\ne b,\qquad b\ne c
\]
must satisfy
\[
a-b=b-c.
\]

Indeed, put \(x=a-b\) and \(y=b-c\). Both are nonzero, and
\[
\Delta=\{x,x+y,y\}.
\]
The element \(x+y\) is distinct from both \(x\) and \(y\). If \(x\ne y\), all three are distinct, contrary to the absence of a rich triple. Hence \(x=y\).

Therefore, along any projection chain having unequal adjacent labels, every successive difference is the same nonzero field element: the labels form an arithmetic progression.

A sufficiently long such chain exists in every case:

- **A:** Take a linear cut of the complete reflection list. It has \(F=3p-2\) terms and unequal adjacent labels.
- **B:** Write the unique double run as \(a_1,a_2\), both labelled \(a\). Start the cyclic cut at \(a_2\) and end at \(a_1\). This uses all \(F\) terms and breaks the only equal adjacent pair at the cut.
- **C:** Write the unique triple run as \(a_1,a_2,a_3\). Take the cyclic interval beginning at \(a_3\), continuing through every outside reflection, and ending at \(a_1\), omitting \(a_2\). Its length is
  \[
  F-1=3p-3,
  \]
  and all adjacent labels are unequal.

Every triple inside the chosen chain is a consecutive cyclic projection triple. Hence the arithmetic-progression conclusion applies throughout.

All these chains have length at least \(2p\), since \(p\ge3\) and
\[
3p-3\ge2p.
\]

Take their first \(2p\) reflection occurrences, labelled
\[
\alpha,\ \alpha+d,\ \ldots,\ \alpha+(2p-1)d.
\]
Their alternating exponent is
\[
\sum_{k=0}^{p-1}
\left[(\alpha+2kd)-(\alpha+(2k+1)d)\right]
=-pd=0
\quad\text{in }\mathbb F_p.
\]
They therefore have product \(1\).

The cyclic-cut argument in section 3 transfers this identity to the original linear occurrence order.

This completes the proof for **every odd prime \(p\)**, including \(p=3\), without an exceptional computational check. ∎

## 6. Exact target relation and remaining obligation

The supported **AUTHOR candidate statement** is:

> For every odd prime \(p\) and every assigned actual word, if \(o_\pi\) is either \(3p-4\) or \(3p-2\), there exists an identity subsequence of exactly \(2p\) letters in original order, all of them reflections.

This does not change the prior adoption status of S1 or S2.

Within the assigned high-run domain \(o_\pi\ge p+4\), the remaining **uniform full-band obligation** is
\[
p+4\le o_\pi\le3p-6,
\qquad o_\pi\text{ odd}.
\]

- For \(p=3\), that residual is empty: the assigned high-run branch at that prime is completely handled.
- For \(p=5\), the residual is \(o_\pi=9\).
- For larger primes, the displayed residual remains an actual open obligation, not a diagnosis of impossibility.

Lower projection bands, unrestricted ordered-Olson closure, and all-group closure are not claimed.

### First unpaid structural bridge

The first remaining deficit is
\[
F-o_\pi=4.
\]
Its complete run-length types are:

1. one length-five odd run;
2. one length-four even run;
3. two length-three odd runs;
4. one length-three odd run and one length-two even run;
5. two length-two even runs;

with every other run having length one.

Section 3 resolves those individual instances that meet its rich-triple and at-most-one-constant-triple hypotheses. The proof above does **not** supply a uniform rich-triple partition or a sufficiently long arithmetic chain for all deficit-four words.

That is the first missing step. No two-rotation selector or sign equation for that step is asserted.

## 7. Actual-word witness illustrating the projection distinction

This is a **written instance**, not executed code and not a counterexample.

Take \(p=5\). In original reflection occurrence order, let
\[
(a_1,\ldots,a_{13})
=
(0,0,0,1,0,1,2,3,4,0,1,2,3).
\]

Let the actual word be
\[
W=
\left(\prod_{i=1}^{6}\sigma_{a_i}\rho_1\right)
\sigma_{a_7}\sigma_{a_8}\sigma_{a_9}
\sigma_{a_{10}}\sigma_{a_{11}}\sigma_{a_{12}}\sigma_{a_{13}},
\]
where the displayed product is in increasing index order.

It has:

- \(F=13=3p-2\) reflection occurrences;
- \(R=6=p+1\) rotation occurrences;
- no cyclically adjacent rotations.

Deleting the rotations merges the first three zero-labelled reflection occurrences into **one projection run of length three**, even though rotations separate them in the actual word. All ten remaining projection runs have length one; the final label \(3\) differs from the initial label \(0\). Thus
\[
o_\pi=11=3p-4.
\]

Select reflection occurrence indices
\[
1,2,3,4,6,7,8,10,12,13.
\]
These are exactly ten original-order occurrences and no rotations. Their labels are
\[
0,0,0,1,1,2,3,0,2,3.
\]
Their alternating exponent is
\[
0-0+0-1+1-2+3-0+2-3=0.
\]
Their product is therefore \(1\) in the actual group.

This witness retains original occurrence order and explicitly distinguishes occupied-gap actual blocks from projection runs.

## Final assurance ceiling

The deliverable is a complete written author candidate for the stated top-two-band branch, **not an accepted theorem receipt**.

No actual-word avoiding example, general high-run closure, novelty, independent-family, human, kernel, or machine-verification credit is claimed.

Before adoption, the disjoint check should reconstruct:

1. the sumset coefficient argument;
2. the two partition phases;
3. the exact \(F,F,F-1\) chain lengths;
4. the cyclic-to-linear identity transfer.