# F568 author-candidate-v1 — Actual ordered deficit-four closure using two rotations

**Status: AUTHOR / WRITTEN PROOF CANDIDATE.** This body proves the complete deficit-four branch in the assigned high-run domain. It requires disjoint checking and parent disposition before adoption.

The new construction selects **exactly two rotations and \(2p-2\) reflections**, in their actual occurrence order. It explicitly handles rotations lying inside reflection triples; it does not assume that two suitable rotations occur at triple boundaries.

## 1. Read chronology, input pins, and execution boundary

Before scientific derivation, I completely read:

- The frozen manifest, LF 1–116.
- The freeze receipt, LF 1–47.
- All twelve listed permissions/status controls through their endings.
- The dispatch receipt and complete parent metadata supply.

I then sent Main a direct pre-body ACK. After that ACK, I read the literal packet in order, using raw windows of at most twenty LF: 1–20, 21–40, continuing consecutively through 381–400 and 401–412. The final packet line was `S2|377|4. the cyclic-to-linear identity transfer.` Derivation began only afterward.

The assigned pins are:

| Item | SHA256 |
|---|---|
| Manifest | `fabdff525c3fea3a3195eb8f3b72ecbbd9529afd506352c35d3c8c9d1f2b01a9` |
| Freeze receipt | `9d7fc825272e5a9320f3a72d86b134b904ffd0a80c73f461a866b30c871de61a` |
| Literal packet | `155cdac512bade6a497087b66cce1e622a0e75ef45918d9e5957853a314ae521` |
| S1, adopted top-two-band disposition | `bb7186723a631295f1008f9bea3fc069bcbd89a58ad818f07112f5dd345fe992` |
| S2, complete F495 author argument | `f02e2f8def6d00b078be42a7072c9458ea89d23b921e4b5407bed57671ea6ca4` |

The live hash/byte/LF observations and clock `2026-10-30T13:31:55-0700 PDT` are **parent-supplied observations**, not my executed checks, native start time, or execution receipt. S2 has 377 numbered logical source lines in the packet; the supplied metadata reports 376 LF characters.

No cited-but-unpasted scientific source, author code, sibling return, or held scientific payload was opened. All held episodes and their consumers remain NONINPUT. This records observable access and work chronology, not a cognitive-isolation certificate.

**Scientific execution: NOTRUN.** No interpreter, CAS, solver, scientific executable, or subagent calculation was used. No executable code was authored. The example below is written group algebra, not a machine result. Runtime constraints prohibit repository writes here; no file-write bypass was attempted. This is the complete body for Main materialization.

## 2. Exact new theorem

### Deficit-four theorem

Let \(p\ge5\) be an odd prime. Let \(W\) be an actual linear word in \(D_{2p}\) having:

1. \(F=3p-2\) reflection occurrences;
2. \(R\ge p+1\) rotation occurrences;
3. singleton cyclic rotation gaps: each gap between cyclically consecutive reflection occurrences contains at most one rotation occurrence.

Delete rotations while retaining reflection occurrence order. Let \(o_\pi\) count the odd-length maximal constant-label runs in the resulting cyclic reflection projection.

If
\[
o_\pi=3p-6,
\]
then \(W\) has an identity subsequence of exactly \(2p\) letters in its **original linear order**. The construction uses exactly two rotations and \(2p-2\) reflections.

Together with the separately adopted S1 result, this closes the three top odd-projection bands
\[
o_\pi\in\{3p-6,\;3p-4,\;3p-2\}
\qquad(p\ge5).
\]

The restriction \(p\ge5\) is intentional. At \(p=3\), deficit four lies outside the assigned high-run domain \(o_\pi\ge p+4\). No new deficit-four assertion at that prime is made.

## 3. Actual group multiplication and interior-rotation consumers

Use
\[
\rho_u=(u,0),\qquad \sigma_a=(a,1),
\]
with
\[
(x,e)(y,b)=\bigl(x+(-1)^e y,\ e+b\bigr).
\]
Field coordinates are modulo \(p\), and parity coordinates modulo \(2\). In particular,
\[
\sigma_a\sigma_b=\rho_{a-b}.
\]

Consider three consecutive reflection occurrences in projection order, labelled \(a,b,c\). Unselected rotations are omitted from the subsequence.

### No selected interior rotation

Choosing two reflections gives precisely the exponent set
\[
A_0(a,b,c)=\{a-b,\ a-c,\ b-c\}.
\]
If the triple is nonconstant, this set has at least two elements. Indeed, equality of all three displayed values would first force \(b=c\), then \(a=b\).

### One selected rotation in the first interior gap

If \(\rho_u\) lies between the first and second reflection occurrences, the three possible selected subwords have exponents
\[
A^{(1)}_u(a,b,c)
=
\{a-u-b,\ a-u-c,\ u+b-c\}.
\]

These correspond respectively to choosing reflections \(a,b\), \(a,c\), and \(b,c\). The last choice retains the rotation as a prefix:
\[
\rho_u\sigma_b\sigma_c=\rho_{u+b-c}.
\]

If \(b\ne c\), the first two exponents are distinct for **every** \(u\). Call this first interior gap **safe** when \(b\ne c\).

### One selected rotation in the second interior gap

If \(\rho_u\) lies between the second and third reflection occurrences, the exponent set is
\[
A^{(2)}_u(a,b,c)
=
\{a-b+u,\ a-u-c,\ b-u-c\}.
\]

If \(a\ne b\), the last two exponents are distinct for every \(u\). Call this second interior gap **safe** when \(a\ne b\).

Thus a nonconstant triple has:

- two safe interior gaps when both adjacent label pairs are unequal;
- one safe and one potentially unsafe interior gap when it has an equal adjacent pair.

It cannot have two equal adjacent pairs, because that would make it constant.

Consequently, the number of potentially unsafe interior gaps in a partition into nonconstant triples equals the number of equal adjacent pairs lying inside its triples. The unsafe gap need not itself be the equal-label gap; the formulas above specify the actual routing.

A rotation in a gap **between** triple blocks is a boundary rotation. After replacing each selected triple subword by its product, every block has even reflection parity and is a rotation. Boundary rotations therefore contribute their ordinary \(+u\) exponents between those rotation-valued blocks.

These formulas are the consuming-side sign calculation needed by the construction.

## 4. Finite-field sumset lemma

For nonempty \(A,B\subseteq\mathbb F_p\),
\[
|A+B|\ge \min(p,\ |A|+|B|-1).
\]

Here is a self-contained proof. Put \(a=|A|\), \(b=|B|\), and first assume \(a+b-1\le p\). If the inequality failed, enlarge \(A+B\) to a set \(C\) of size
\[
n=a+b-2<p.
\]
The polynomial
\[
P(X,Y)=\prod_{c\in C}(X+Y-c)
\]
vanishes on \(A\times B\), but its coefficient of \(X^{a-1}Y^{b-1}\) is
\[
\binom{n}{a-1}\ne0
\quad\text{in }\mathbb F_p.
\]

For any polynomial of total degree at most \(a+b-2\), that coefficient equals
\[
\sum_{\substack{x\in A\\y\in B}}
\frac{P(x,y)}
{\displaystyle
 \prod_{x'\in A\setminus\{x\}}(x-x')
 \prod_{y'\in B\setminus\{y\}}(y-y')}.
\]
This follows from one-variable Lagrange coefficient extraction in each variable. A monomial with either degree below the corresponding extraction degree contributes zero; the total-degree bound leaves only the indicated monomial. All denominators are nonzero.

Since \(P\) vanishes on the grid, the displayed coefficient must be zero, a contradiction. The singleton boundary case is immediate as well.

If \(a+b-1>p\), choose nonempty subsets \(A'\subseteq A\), \(B'\subseteq B\) with
\[
|A'|+|B'|=p+1.
\]
The established case gives \(A'+B'=\mathbb F_p\), hence \(A+B=\mathbb F_p\).

Iteration yields
\[
|A_1+\cdots+A_t|
\ge
\min\left(p,\ 1+\sum_{i=1}^{t}(|A_i|-1)\right).
\]
In particular, the sum of \(p-1\) sets, each of size at least two, is all of \(\mathbb F_p\).

## 5. A new two-rotation chronological certificate

Suppose the cyclic reflection projection of length \(3p-2\) admits the following arrangement:

- omit one reflection occurrence \(z\);
- cut immediately after \(z\);
- partition the remaining \(3p-3\) reflection occurrences, in that cyclic order, into \(p-1\) consecutive **nonconstant triples**.

Let \(B\) be the number of potentially unsafe interior gaps of these triples. If the actual word has singleton cyclic rotation gaps and
\[
R\ge B+3,
\]
then it has an original-order identity subsequence of exactly \(2p\) letters, using two rotations.

### Proof

There are at most \(B\) rotation occurrences in unsafe gaps: each such gap contains at most one rotation. Hence at least three rotation occurrences are in safe interior gaps or boundary gaps.

Choose two of these occurrences so that they are not both interior to the same triple:

- If a boundary rotation is available, choose it and any other safe/boundary rotation.
- Otherwise all available occurrences are in safe interior gaps. A triple has only two interior gaps, so three such occurrences cannot all belong to one triple. Choose occurrences from two different triples.

The selected rotations are now fixed. Each triple contains at most one selected interior rotation.

For triple \(i\), form its actual exponent set \(A_i\):

- use \(A_0\) if it contains no selected interior rotation;
- use \(A^{(1)}_u\) or \(A^{(2)}_u\) if it contains the corresponding selected rotation.

Every \(A_i\) has at least two elements by Section 3. Let \(c\) be the sum of the labels of the selected boundary rotations; take \(c=0\) if neither selected rotation is a boundary rotation.

Because the blocks are disjoint chronological blocks and each chosen block subword has even reflection parity, the selected cyclic-order product is
\[
\rho_{\,c+\sum_{i=1}^{p-1}d_i},
\qquad d_i\in A_i.
\]

Section 4 gives
\[
A_1+\cdots+A_{p-1}=\mathbb F_p.
\]
Choose the \(d_i\) to sum to \(-c\), and choose the corresponding two actual reflection occurrences in each triple.

This selects exactly
\[
2(p-1)+2=2p
\]
distinct actual occurrences. Their product in cut order is \(1\).

Finally, restoring their original linear order cyclically rotates the selected groupword. If one cut gives \(UV=1\), another cut gives
\[
VU=U^{-1}(UV)U=1.
\]
Therefore the same selected occurrences have identity product in the original linear word order. This uses conjugation, not commutation of reflections. ∎

The certificate neither assumes boundary placement of the two rotations nor imports an unproved two-rotation selector.

## 6. Every deficit-four type admits the required partition

For cyclic constant-run lengths \(\ell_j\),
\[
F-o_\pi
=
\sum_{\ell_j\text{ odd}}(\ell_j-1)
+
\sum_{\ell_j\text{ even}}\ell_j.
\]
Each positive contribution is an even integer. Therefore deficit four has exactly five run-length types, with all unlisted runs of length one:

1. one length-five run;
2. one length-four run;
3. two length-three runs;
4. one length-three run and one length-two run;
5. two length-two runs.

For each type, a suitable omitted occurrence gives \(p-1\) nonconstant triples and \(B\le2\).

### Type 1: one length-five run

Write the run as \(a_1,a_2,a_3,a_4,a_5\), all with the same label. Omit \(a_3\) and cut immediately afterward.

The remaining run fragments are \(a_4,a_5\) at the beginning and \(a_1,a_2\) at the end of the linear interval. Neither has length three. Every other run is a singleton, so every triple block is nonconstant.

Only those two length-two fragments can contribute equal adjacent pairs inside triples. Thus
\[
B\le2.
\]

### Type 2: one length-four run

Write it as \(a_1,a_2,a_3,a_4\). Omit \(a_2\) and cut immediately afterward.

The beginning has the length-two fragment \(a_3,a_4\), and the end has the singleton \(a_1\). No constant triple remains, and only the length-two fragment can contribute an internal equal adjacency. Hence
\[
B\le1.
\]

### Type 3: two length-three runs

Write one run as \(a_1,a_2,a_3\), and let \(j\) denote the first occurrence of the other length-three run.

Consider omitting \(a_i\), separately for \(i=1,2,3\), cutting immediately afterward, and partitioning into triples.

The first constant triple has been interrupted by the omission. The only possible constant triple block is therefore the other length-three run.

Measured from the beginning of the cut interval, the position of \(j\) changes by one as the omitted occurrence advances from \(a_1\) to \(a_2\) to \(a_3\). These three positions are consecutive integers: no wrap occurs between these choices because the other run lies outside the first run.

Triple blocks start at positions congruent to \(1\pmod3\). At most one of the three choices therefore makes the other constant triple a block. Choose either of the remaining choices.

All blocks are then nonconstant. The interrupted first run contributes at most one internal equal adjacency. The intact second length-three run, not being a block, straddles a block boundary and also contributes at most one internal equal adjacency. Thus
\[
B\le2.
\]

This argument handles both constant triple windows; it does not reuse the earlier at-most-one-window certificate.

### Type 4: one length-three run and one length-two run

Omit the middle occurrence of the length-three run and cut immediately afterward.

The length-three run leaves one occurrence at each end, so it contributes no internal equal adjacency. The length-two run may contribute one. No constant triple block remains, and
\[
B\le1.
\]

### Type 5: two length-two runs

There are no constant triple windows. Omit any reflection occurrence and partition the remaining interval into triples.

Every block is nonconstant. Each length-two run contributes at most one internal equal adjacency, so
\[
B\le2.
\]

### Complete partition summary

| Deficit-four run type | Omission | Bound on \(B\) |
|---|---|---:|
| One \(5\)-run | Middle occurrence | \(2\) |
| One \(4\)-run | Second occurrence | \(1\) |
| Two \(3\)-runs | A good choice among the three occurrences of one run | \(2\) |
| One \(3\)-run and one \(2\)-run | Middle of the \(3\)-run | \(1\) |
| Two \(2\)-runs | Any occurrence | \(2\) |

These are occurrence partitions in the rotation-deleted projection. They do not identify projection runs with actual blocks separated by rotations.

## 7. Proof of the deficit-four theorem

Apply Section 6 to obtain \(p-1\) nonconstant triples with \(B\le2\).

Since \(p\ge5\) and \(R\ge p+1\),
\[
R-B\ge p-1\ge4.
\]
In particular,
\[
R\ge B+3.
\]

The chronological certificate in Section 5 therefore supplies two actual rotation occurrences and \(2p-2\) actual reflection occurrences whose original-order product is \(1\).

This proves all five deficit-four types, uniformly in their run positions, reflection labels, and rotation labels. No rich-triple hypothesis, arithmetic-progression classification, selected numerical parameter, or restriction on the rotation values is needed. ∎

## 8. Written actual-word example in the newly closed band

This is a written illustration, not executed finite evidence and not an avoiding-word claim.

Take \(p=5\), with reflection labels
\[
(a_1,\ldots,a_{13})
=
(0,0,0,0,0,1,2,3,4,1,2,3,4).
\]
Define the actual word
\[
W=
\left(\prod_{i=1}^{6}\sigma_{a_i}\rho_1\right)
\sigma_{a_7}\sigma_{a_8}\sigma_{a_9}
\sigma_{a_{10}}\sigma_{a_{11}}\sigma_{a_{12}}\sigma_{a_{13}},
\]
where the product is in increasing index order.

It has thirteen reflections and six rotations, with at most one rotation in each cyclic reflection gap. Its reflection projection has one length-five zero run and eight singleton runs. Therefore
\[
o_\pi=9=3p-6.
\]

Omit reflection occurrence \(3\). In cyclic order after that omission, the four triple blocks are
\[
(4,5,6),\quad(7,8,9),\quad(10,11,12),\quad(13,1,2),
\]
with label triples
\[
(0,0,1),\quad(2,3,4),\quad(1,2,3),\quad(4,0,0).
\]

Choose the two rotation occurrences immediately after reflection occurrences \(2\) and \(3\). Both are boundary rotations for this partition.

Select reflection occurrences
\[
1,2,4,5,7,8,10,11.
\]
In the original actual word, the complete selected positions are
\[
1,3,4,6,7,9,13,14,16,17.
\]
Their letters, in that original order, are
\[
\sigma_0,\ \sigma_0,\ \rho_1,\ \rho_1,\
\sigma_0,\ \sigma_0,\ \sigma_2,\ \sigma_3,\
\sigma_1,\ \sigma_2.
\]

Their product is
\[
(\sigma_0\sigma_0)\rho_1\rho_1
(\sigma_0\sigma_0)(\sigma_2\sigma_3)(\sigma_1\sigma_2)
=
\rho_{\,0+1+1+0-1-1}
=
1.
\]
There are exactly ten selected actual letters, including exactly two rotations.

## 9. Exact frontier change and unpaid residual

The new author theorem closes the complete band
\[
o_\pi=3p-6
\]
for every odd prime \(p\ge5\), not merely its rich-triple instances.

Combining this candidate with the separately adopted top-two-band theorem would leave the following literal residual inside the named high-run domain:
\[
\boxed{
p+4\le o_\pi\le3p-8,
\qquad o_\pi\text{ odd}.
}
\]

Thus:

- At \(p=3\), the named high-run branch was already covered by the prior result.
- At \(p=5\), adopting this candidate would close the entire named high-run branch.
- At \(p=7\), the remaining named values would be \(o_\pi=11,13\).
- Higher-prime residuals remain exactly as displayed.

### First unpaid structural bridge

The next deficit is
\[
F-o_\pi=6.
\]
Its complete run-length types, with all other runs singleton, are:

1. one \(7\)-run;
2. one \(6\)-run;
3. one \(5\)-run and one \(3\)-run;
4. one \(5\)-run and one \(2\)-run;
5. one \(4\)-run and one \(3\)-run;
6. one \(4\)-run and one \(2\)-run;
7. three \(3\)-runs;
8. two \(3\)-runs and one \(2\)-run;
9. one \(3\)-run and two \(2\)-runs;
10. three \(2\)-runs.

This body does not close that band.

In particular, the present partition certificate cannot uniformly handle a length-six or length-seven constant run. If the omitted occurrence lies inside such a run, the two fragments at the ends of the cut interval have total length at least five, so one has length at least three and forces a constant first or last triple. If the omitted occurrence lies outside it, a consecutive constant run of length at least six necessarily contains a full block of any consecutive length-three partition.

A further argument must therefore handle constant triple blocks or use a different selection geometry; merely repeating this nonconstant-triple partition is insufficient. No claim is made that solving those two run types alone would settle all deficit-six types.

## 10. Assurance and disposition ceiling

- **New mathematical scope:** complete actual ordered deficit-four branch for \(p\ge5\), using two rotations.
- **Proof versus experiment:** written proof only; scientific execution and finite replay **NOTRUN**.
- **Original interfaces:** reflection occurrence order, interior-rotation signs, boundary rotations, distinct occurrence selection, exact selected length, and cyclic-to-original transfer are all explicit.
- **Unproved scope:** the displayed remaining high-run interval, lower bands, unrestricted ordered-Olson closure, and all-group closure.
- **No avoiding-word claim:** the example is an explicit identity witness.
- **F/M/m:** this is an AUTHOR return, not a disjoint review; no independent finding count or acceptance verdict is asserted.
- **Acceptance ceiling:** not independently reviewed, parent-adopted, independent-family, human-checked, kernel-checked, or machine-verified.
- **Source/priority ceiling:** no original-source equivalence, source authentication, novelty, or worldwide-priority claim.

The central new step is the proved two-rotation consumer: \(p-1\) nonconstant chronological triples already supply the necessary full-field sumset, provided two rotations are chosen in safe locations. Deficit four always admits such a partition with at most two unsafe gaps, and the actual rotation count guarantees the required choices.