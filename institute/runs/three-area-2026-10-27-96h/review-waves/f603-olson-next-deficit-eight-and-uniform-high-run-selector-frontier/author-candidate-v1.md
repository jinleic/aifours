# F603 author-candidate-v1 — Uniform high-run selectors and partial deficit-eight closure

**Status: AUTHOR / WRITTEN PROOF CANDIDATE.**

**Whole deficit-eight band: NOT PROVED.** This body proves:

1. A uniform rich-versus-constant-window selector covering multiple projection deficits.
2. Three unconditional structural families throughout the named high-run domain.
3. Eight complete deficit-eight run types, together with explicit rich-window regions in the other twelve types.

Every constructed identity uses exactly **two actual rotations and \(2p-2\) actual reflections**, in original occurrence order. No avoiding word, executable result, or whole-band acceptance is claimed.

## 1. Read chronology, source status, and execution boundary

Before reading any mathematical packet body, I read:

- `manifest-v1.json`, through logical line 141;
- `freeze-receipt-v1.json`, through line 60;
- the complete dispatch receipt;
- the complete parent live metadata supply;
- all fourteen named `controls_before_body`, through their declared endings.

I then delivered a **direct PREBODY ACK to Main before opening the literal packet**.

After that ACK, I read `literal-packet-v1.md` consecutively in exact raw windows of at most twenty lines, from packet line 1 through packet line 713. The observed source endings were `S1|631`, `S2|47`, and `S3|33`. One mistyped-path lookup after packet line 560 returned “not found”; it exposed no source body. I corrected the path and resumed with lines 561–580. Mathematical derivation began only after the complete packet ending.

Assigned pins:

- Manifest: `d779ae01a479f1a9c239e8102cafff6cd5f777ebc532ee02c01a2d9169df9850`.
- Freeze receipt: `21bcc6643165b1bb00462dbed89458a9c34b5c9a913167c8aa0b1562b4c1ffff`.
- Packet, according to the supplied receipt: `1a3ae97242773a5e41c1800ef2d8329266d300152dc0a873cc68357dc38c403b`.

These hashes, byte/LF matches, and the supplied clock are **parent observations**, not child-executed checks or a child-native start timestamp.

S1, the F582 deficit-six author body, remains **UNADOPTED**. Its historical ACK-after-packet sequence is disclosed by the supplied control, not backdated. I do not use its whole deficit-six assertion, long-run tables, or exceptional branch as an accepted premise. The common local mechanism needed here is reconstructed below.

S2 and S3 retain their stated adopted deficit-four and top-two-band scopes. Those adoptions do not adopt this candidate.

All genuinely held episodes and their proof, method, selection, planning, reporting, and confidence consumers—including f586—remain **NONINPUT**. No held scientific payload, sibling return, linked scientific source, or author executable was opened.

**Scientific execution: NOTRUN.** No interpreter, solver, CAS, finite scan, scientific executable, or delegated calculation was used. No executable code was authored. The calculations below are written symbolic arguments; the tables are symbolic classifications, not machine output. No new concrete field instance or word was instantiated. No external source was used.

No repository mutation or write bypass was attempted. This is the complete body for Main materialization as `author-candidate-v1.md`.

## 2. Actual target and notation

Let \(p\ge5\) be an odd prime. Let \(W\) be an actual linear word in \(D_{2p}\) having:

- exactly \(F=3p-2\) reflection occurrences;
- \(R\ge p+1\) rotation occurrences;
- at most one rotation occurrence in each **original cyclic gap** between consecutive reflection occurrences.

Delete rotations while retaining cyclic reflection occurrence order. Write the maximal constant-run lengths of this projection as \(\ell_1,\ldots,\ell_m\). Let \(o_\pi\) count its odd-length runs.

The named high-run domain is
\[
o_\pi\ge p+4.
\]

Define:

\[
D=F-o_\pi,
\qquad
E=\sum_j(\ell_j-1)=F-m,
\]
\[
C=\sum_j\max(\ell_j-2,0).
\]

Thus \(E\) counts equal adjacent reflection pairs in the cyclic projection, and \(C\) counts constant cyclic windows of three consecutive reflection occurrences.

For a chronological triple of reflection labels \((a,b,c)\), put
\[
A_0(a,b,c)=\{a-b,\ a-c,\ b-c\}.
\]
Call the triple **rich** when \(|A_0|=3\). Let \(H\) count rich cyclic windows of three consecutive projection occurrences.

All counts refer to occurrences and their actual cyclic positions, not distinct group elements.

The requested deficit-eight band is
\[
D=8,\qquad o_\pi=3p-10.
\]
It lies in the named high-run domain exactly when \(p\ge7\).

## 3. Actual ordered-product selector

Use
\[
\rho_u=(u,0),\qquad \sigma_a=(a,1),
\]
with
\[
(x,e)(y,b)=\bigl(x+(-1)^e y,\ e+b\bigr)
\]
in \(\mathbb F_p\times\mathbb Z/2\mathbb Z\).

Consequently,
\[
\sigma_a\sigma_b=\rho_{a-b}.
\]

### 3.1 Local reflection and rotation choices

Without a selected interior rotation, choosing two occurrences from a chronological reflection triple gives exactly
\[
A_0(a,b,c)=\{a-b,a-c,b-c\}.
\]

A nonconstant triple has at least two exponents.

With one selected \(\rho_u\) in its first interior gap, the three actual pair choices give
\[
A_u^{(1)}(a,b,c)
=
\{a-u-b,\ a-u-c,\ u+b-c\}.
\]
This gap is safe whenever \(b\ne c\), because the first two entries then differ.

With one selected \(\rho_u\) in its second interior gap, they give
\[
A_u^{(2)}(a,b,c)
=
\{a-b+u,\ a-u-c,\ b-u-c\}.
\]
This gap is safe whenever \(a\ne b\), because the last two entries then differ.

These formulas include cases where omission makes the selected rotation a prefix or suffix of the chosen reflection pair. No uniform-sign substitution is made.

A nonconstant triple therefore has:

- no potentially unsafe interior gap if both adjacent labels differ;
- exactly one potentially unsafe gap if one adjacent pair is equal.

A constant triple always retains a nonempty exponent set.

### 3.2 Partition and protection

Omit one reflection occurrence \(z\), cut immediately after it, and partition the remaining
\[
3p-3=3(p-1)
\]
reflection occurrences into \(p-1\) consecutive triples.

Let:

- \(c\) be the number of constant blocks;
- \(r\) be the number of rich blocks;
- \(B\) count potentially unsafe gaps of nonconstant blocks.

Protecting a block means selecting no rotation in either of its interior gaps.

If \(r\ge c\), protect any \(c\) rich blocks. Forbid rotations in their interiors and in every potentially unsafe gap of the other nonconstant blocks. Since rich blocks have unequal adjacent labels, the number of forbidden original rotation gaps is at most
\[
B+2c.
\]

Moreover,
\[
B+2c
\]
is exactly the number of equal projection adjacencies internal to the triple blocks: a constant block contributes two, a nonconstant block with a repeated adjacent pair contributes one, and every other block contributes zero.

If
\[
B+2c\le p-2,
\]
at least
\[
R-(B+2c)\ge3
\]
rotation occurrences remain eligible.

Two eligible occurrences can be chosen with at most one interior to each triple:

- an eligible boundary rotation can be paired with any other eligible occurrence;
- otherwise three eligible interior occurrences cannot all occupy one triple, which has only two original interior gaps.

The two original gaps adjacent to \(z\) remain distinct boundary locations at the two ends of the cut word. They are neither discarded nor merged.

### 3.3 Independent block choices and original-order identity

Each block selects two reflections and at most one interior rotation, so every selected block product has even reflection parity and is a rotation.

After choosing the two rotations, let \(A_i\) be block \(i\)'s actual exponent set. Then:

- a constant block has \(|A_i|\ge1\);
- every nonconstant block has \(|A_i|\ge2\);
- every protected rich block has \(|A_i|=3\).

Thus, when \(c\) rich blocks compensate \(c\) constant blocks,
\[
\sum_{i=1}^{p-1}(|A_i|-1)\ge p-1.
\]

The finite-field sumset bound proved in Section 4 gives
\[
A_1+\cdots+A_{p-1}=\mathbb F_p.
\]

Selected boundary rotations contribute a fixed offset \(q\). Choose the independent block exponents to sum to \(-q\). The resulting product is identity and selects exactly
\[
2(p-1)+2=2p
\]
distinct actual occurrences.

Returning from the cut to the original linear word cyclically rotates the selected groupword. If its cut product is \(UV=1\), then
\[
VU=U^{-1}(UV)U=1.
\]
Therefore the same occurrences give identity in original linear order.

This proves the following usable lemma.

### Actual selector lemma

A one-omission triple partition with
\[
r\ge c,\qquad B+2c\le p-2
\]
produces an original-order identity subsequence of exactly two rotations and \(2p-2\) reflections.

## 4. Self-contained sumset bound

For nonempty \(A,B\subseteq\mathbb F_p\),
\[
|A+B|\ge\min(p,|A|+|B|-1).
\]

Put \(a=|A|\), \(b=|B|\). Suppose first that \(a+b-1\le p\) and the bound fails. Enlarge \(A+B\) to a set \(Q\) of size
\[
n=a+b-2<p.
\]
The polynomial
\[
P(X,Y)=\prod_{q\in Q}(X+Y-q)
\]
vanishes on \(A\times B\), but its \(X^{a-1}Y^{b-1}\) coefficient is
\[
\binom{n}{a-1}\ne0
\]
in \(\mathbb F_p\).

Successive one-variable Lagrange coefficient extraction expresses that coefficient as
\[
\sum_{x\in A,\ y\in B}
\frac{P(x,y)}
{\displaystyle
\prod_{x'\in A\setminus\{x\}}(x-x')
\prod_{y'\in B\setminus\{y\}}(y-y')}.
\]
Every numerator is zero, a contradiction. The trivial singleton boundary case is immediate.

If \(a+b-1>p\), choose nonempty subsets whose cardinalities sum to \(p+1\), and apply the proved case.

Iteration yields
\[
|A_1+\cdots+A_t|
\ge
\min\!\left(p,\ 1+\sum_i(|A_i|-1)\right).
\]

This applies only after chronological block products have been calculated. It does not permit reordering actual reflections or combining incompatible overlapping selections.

## 5. A uniform rich-window theorem

### Theorem A: all-cut window dominance

Under the actual-word hypotheses of Section 2, suppose
\[
C-H\le3,\qquad E\le p-2.
\]
Then \(W\) has an original-order identity subsequence comprising exactly two rotations and \(2p-2\) reflections.

#### Proof

For every omitted reflection occurrence \(z\), form its one-omission triple partition. Write its rich and constant block counts as \(r_z,c_z\).

Every fixed cyclic triple window occurs as a block in exactly \(p-1\) of these \(F\) partitions: its possible preceding omitted positions are obtained by stepping backward by multiples of three, for the \(p-1\) block positions.

Hence
\[
\sum_z(r_z-c_z)=(p-1)(H-C).
\]

If every partition had \(r_z<c_z\), integrality would give
\[
\sum_z(r_z-c_z)\le-F=-(3p-2).
\]

But \(H-C\ge-3\) gives
\[
\sum_z(r_z-c_z)
\ge-3(p-1)=-(3p-3)>-(3p-2),
\]
a contradiction.

Thus some partition has \(r_z\ge c_z\). Its internal equal-adjacency count is at most \(E\le p-2\). Apply the actual selector lemma. ∎

The allowance of three more constant windows than rich windows is an integer-counting consequence of the exact length \(3p-2\); it is not an assumption that constant blocks disappear.

## 6. A long-run refinement of the rotation budget

### Theorem B: three omissions inside a long run

Suppose the word lies in the named high-run domain. Let \(L\ge3\) be the length of any chosen maximal constant run. If
\[
C-H\le3,
\qquad
E-\left\lfloor\frac{L+1}{3}\right\rfloor\le p-2,
\]
then the same exact two-rotation identity conclusion holds.

In particular, one may use the longest run.

#### Proof

Write the chosen run as \(a_1,\ldots,a_L\), all with label \(a\). For \(k=1,2,3\), let \(P_k\) omit \(a_k\), cut after it, and partition into triples. Write their rich and constant block counts as \(r_k,c_k\).

The high-run hypothesis ensures that the outside interval contains more than two reflection occurrences, so the two boundary triple windows used below are distinct.

Across these three phases:

1. Every rich cyclic triple appears exactly once. A rich window cannot contain an equal adjacent pair, so it is wholly outside the chosen run or is one of its two unequal-adjacency boundary windows.
2. Every constant window in another run appears exactly once.
3. The chosen run contributes
   \[
   \sum_{k=1}^3
   \left\lfloor\frac{L-k}{3}\right\rfloor
   =L-3
   \]
   constant blocks, whereas its contribution to \(C\) is \(L-2\).

Consequently,
\[
\sum_{k=1}^3r_k=H,\qquad
\sum_{k=1}^3c_k=C-1.
\]
Therefore
\[
\sum_{k=1}^3(r_k-c_k)=H-C+1\ge-2.
\]
All three differences cannot be negative integers, whose sum would be at most \(-3\). Thus one partition has \(r_k\ge c_k\).

It remains to bound its rotation exclusions. Put \(t=L-k\). The number of chosen-run equal adjacencies internal to \(P_k\)'s blocks is
\[
t-\left\lceil\frac t3\right\rceil+\max(k-2,0).
\]
Relative to the original \(L-1\) equal adjacencies, the losses for \(k=1,2,3\) are respectively
\[
\left\lceil\frac{L-1}{3}\right\rceil,\qquad
1+\left\lceil\frac{L-2}{3}\right\rceil,\qquad
1+\left\lceil\frac{L-3}{3}\right\rceil.
\]
Their minimum is
\[
\left\lfloor\frac{L+1}{3}\right\rfloor,
\]
as follows directly from the three residue classes of \(L\) modulo three.

Other block boundaries can only remove additional equal adjacencies. Hence every \(P_k\) satisfies
\[
B_k+2c_k
\le
E-\left\lfloor\frac{L+1}{3}\right\rfloor
\le p-2.
\]
Apply the actual selector lemma to the partition with \(r_k\ge c_k\). ∎

Theorems A and B are uniform structural results across multiple deficits, not a finite-prime scan or a restatement of an unproved long-run table.

## 7. Three unconditional families throughout the high-run domain

The following families need no rich-window hypothesis. Unlisted runs are singleton or double as specified.

### Theorem C

Every word in the named high-run domain has the exact two-rotation identity selector if its projection has any of these structures:

1. All runs have length at most three, with at most three length-three runs.
2. Exactly one length-four run, at most one length-three run, and no other run longer than two.
3. Exactly one length-five run and no other run longer than two.

#### Proof

Let \(q\) count double runs and \(t\) count triple runs.

**Family 1.** Here
\[
D=2(q+t).
\]
The high-run inequality implies
\[
q+t\le p-3.
\]

If \(t>0\), omit one of the three occurrences of a triple run. These choices give three phases for every other intact triple run. Each other triple run forbids at most one phase by becoming a constant block. Since \(t-1\le2\), some phase avoids all constant blocks.

Every double run contributes at most one unsafe gap; every surviving or interrupted triple run contributes at most one. Thus
\[
B\le q+t\le p-3.
\]

If \(t=0\), any omission leaves no constant triple, and \(B\le q\le p-3\).

**Family 2.** Omit the second or third occurrence of the four-run. Its surviving end fragments have lengths \(2,1\) or \(1,2\), so it creates no constant block and contributes at most one unsafe gap.

The possible other triple run changes phase between these two choices and can be a constant block in at most one. Choose the other phase.

Here
\[
D=2q+4+2t,\qquad q+2+t\le p-3,
\]
and
\[
B\le q+1+t\le p-4.
\]

**Family 3.** Omit the middle occurrence of the five-run, leaving two length-two end fragments. Every block is nonconstant, and
\[
B\le q+2.
\]
Since
\[
D=2q+4,\qquad q+2\le p-3,
\]
the required budget holds.

In all three families, \(c=0\), all \(p-1\) block sets have at least two elements, and at least four eligible rotations remain. Section 3 supplies the exact actual selector. ∎

These families include deficits extending to \(D=2p-6\), subject to their stated run restrictions. They are not limited to deficit eight.

## 8. Complete classification of deficit-eight run types

For each maximal run,
\[
D=
\sum_{\ell_j\ \mathrm{odd}}(\ell_j-1)
+
\sum_{\ell_j\ \mathrm{even}}\ell_j.
\]

Every positive contribution is even. Partitioning \(D/2=4\) gives exactly twenty non-singleton run types.

The following table records their symbolic quantities. Here
\[
K=E-\left\lfloor\frac{L+1}{3}\right\rfloor
\]
for longest run \(L\ge3\). “All” denotes complete uniform coverage proved in this body.

| Non-singleton run type | \(C\) | \(E\) | \(K\) | Uniform conclusion |
|---|---:|---:|---:|---|
| \(9\) | 7 | 8 | 5 | \(H\ge4\), all \(p\ge7\) |
| \(8\) | 6 | 7 | 4 | \(H\ge3\), all \(p\ge7\) |
| \(7+3\) | 6 | 8 | 6 | \(H\ge3\), \(p\ge11\) |
| \(7+2\) | 5 | 7 | 5 | \(H\ge2\), all \(p\ge7\) |
| \(6+3\) | 5 | 7 | 5 | \(H\ge2\), all \(p\ge7\) |
| \(6+2\) | 4 | 6 | 4 | \(H\ge1\), all \(p\ge7\) |
| \(5+5\) | 6 | 8 | 6 | \(H\ge3\), \(p\ge11\) |
| \(5+4\) | 5 | 7 | 5 | \(H\ge2\), all \(p\ge7\) |
| \(4+4\) | 4 | 6 | 5 | **All**, Section 9 |
| \(5+3+3\) | 5 | 8 | 6 | \(H\ge2\), \(p\ge11\) |
| \(5+3+2\) | 4 | 7 | 5 | \(H\ge1\), all \(p\ge7\) |
| \(5+2+2\) | 3 | 6 | 4 | **All**, Theorem C |
| \(4+3+3\) | 4 | 7 | 6 | \(H\ge1\), \(p\ge11\) |
| \(4+3+2\) | 3 | 6 | 5 | **All**, Theorem C |
| \(4+2+2\) | 2 | 5 | 4 | **All**, Theorem C |
| \(3+3+3+3\) | 4 | 8 | 7 | \(H\ge1\), \(p\ge11\) |
| \(3+3+3+2\) | 3 | 7 | 6 | **All**, Theorem C |
| \(3+3+2+2\) | 2 | 6 | 5 | **All**, Theorem C |
| \(3+2+2+2\) | 1 | 5 | 4 | **All**, Theorem C |
| \(2+2+2+2\) | 0 | 4 | — | **All**, Theorem C |

For \(p\ge11\), \(E\le8\le p-2\), so Theorem A alone gives every displayed rich-window region. Theorem B additionally supplies the displayed conditional regions at \(p=7\).

## 9. Complete \(4+4\) deficit-eight type

### Theorem D

The entire deficit-eight type consisting of two length-four runs and otherwise singleton runs has the exact two-rotation selector for every \(p\ge7\).

#### Proof

Here \(C=4\), \(E=6\), and \(K=5\). If \(H\ge1\), Theorem B applies.

It remains to handle \(H=0\).

Write the cyclic projection as
\[
a_1,a_2,a_3,a_4,\quad X,\quad
b_1,b_2,b_3,b_4,\quad Y,
\]
where all \(a_i\) have label \(a\), all \(b_i\) have label \(b\), and \(X,Y\) contain \(u,v\) singleton occurrences. Thus
\[
u+v=3p-10.
\]

### 9.1 Nonexceptional phases

Omitting \(a_2\) leaves the first two remaining \(a\)'s before \(X\); the \(b\)-run begins at cut position \(u+3\). A length-four run avoids a constant triple exactly when its first position is \(2\bmod3\). Hence this omission works if \(u\equiv2\pmod3\).

Omitting \(a_3\) makes that first position \(u+2\), and works if \(u\equiv0\pmod3\).

In either case the interrupted four-run contributes at most one unsafe gap, and the other four-run, split \(2+2\), contributes at most two. Thus \(c=0\), \(B\le3\), and Section 3 applies.

### 9.2 Exceptional phase and unequal AP directions

Suppose instead
\[
u\equiv1\pmod3.
\]
The length equation also gives \(v\equiv1\pmod3\). Write
\[
u=3r+1,\qquad v=3s+1,\qquad r+s=p-4.
\]

Since \(H=0\), every consecutive triple on an unequal-adjacency chain is a nonrich triple. If its consecutive increments are \(d,e\ne0\), its exponent set is
\[
\{-d,-e,-d-e\},
\]
which has two elements precisely when \(d=e\). Therefore the chains

- from \(a_4\), through \(X\), to \(b_1\);
- from \(b_4\), through \(Y\), to \(a_1\)

are arithmetic progressions with nonzero increments \(d,e\), respectively.

Their endpoint equations give
\[
(3r+2)d+(3s+2)e=0. \tag{1}
\]

The directions are not equal: \(d=e\) would give
\[
(3p-8)d=-8d=0,
\]
impossible for \(p\ge7\).

They are not opposite: \(e=-d\) would give
\[
3(r-s)d=0.
\]
Since \(|r-s|\le p-4<p\), this implies \(r=s\), contradicting the odd number \(r+s=p-4\).

Thus
\[
d\ne e,\qquad d\ne-e. \tag{2}
\]

### 9.3 Literal disjoint block partition

Omit \(a_1\) and cut after it. The remaining reflections partition as:

1. the constant triple \((a_2,a_3,a_4)\);
2. \(r\) AP triples from the first \(3r\) occurrences of \(X\);
3. \((x_u,b_1,b_2)\);
4. \((b_3,b_4,y_1)\);
5. \(s\) AP triples from the remaining \(3s\) occurrences of \(Y\).

The two displayed boundary blocks have exact exponent sets
\[
\{0,-d\},\qquad \{0,-e\}.
\]

Protect both. By (2), their combined sumset has four distinct elements:
\[
\{0,-d\}+\{0,-e\}
=
\{0,-d,-e,-d-e\}.
\]

Their four interior gaps include every potentially unsafe gap of the nonconstant blocks. Therefore only four original rotation gaps need be forbidden—not six. At least
\[
R-4\ge p-3\ge4
\]
rotation occurrences remain eligible, permitting two with at most one interior to each other block.

The protected combined set has size four; the other \(r+s=p-4\) nonconstant blocks have sets of size at least two; the constant block has a nonempty set. Consequently,
\[
|A_1+\cdots+A_{p-1}|
\ge
\min\bigl(p,\ 1+3+(p-4)\bigr)
=p.
\]

Section 3 now gives the original-order identity with exactly \(2p\) actual occurrences. This proves the whole \(4+4\) type. ∎

## 10. Exact unpaid deficit-eight region

The eight whole types proved here are
\[
\boxed{
4+4,\quad
5+2+2,\quad
4+3+2,\quad
4+2+2,\quad
3+3+3+2,\quad
3+3+2+2,\quad
3+2+2+2,\quad
2+2+2+2.
}
\]

For the other twelve types, the literal residual of the **uniform run/count conclusions proved above** is:

| Type | Unpaid at \(p=7\) | Unpaid at \(p\ge11\) |
|---|---|---|
| \(9\) | \(H\le3\) | \(H\le3\) |
| \(8\) | \(H\le2\) | \(H\le2\) |
| \(7+3\) | All \(H\) | \(H\le2\) |
| \(7+2\) | \(H\le1\) | \(H\le1\) |
| \(6+3\) | \(H\le1\) | \(H\le1\) |
| \(6+2\) | \(H=0\) | \(H=0\) |
| \(5+5\) | All \(H\) | \(H\le2\) |
| \(5+4\) | \(H\le1\) | \(H\le1\) |
| \(5+3+3\) | All \(H\) | \(H\le1\) |
| \(5+3+2\) | \(H=0\) | \(H=0\) |
| \(4+3+3\) | All \(H\) | \(H=0\) |
| \(3+3+3+3\) | All \(H\) | \(H=0\) |

“All \(H\)” means these uniform propositions supply no whole-type or rich-count guarantee there. It does **not** assert that no individual partition can satisfy the actual selector lemma. Likewise, no row asserts that every listed parameter condition is realized, or that an input in that row avoids identity.

### First precise unpaid obligation

A concrete first remaining proof obligation is:

> A single length-nine run, all other runs singleton, \(p\ge7\), and \(H\le3\).

For the three omissions used in Theorem B, each partition has exactly two constant blocks, and their rich-block counts sum to \(H\). When \(H\le3\), these identities do not force a partition with two rich blocks.

The missing step is therefore a selector for this low-richness class—through additional additive growth, different block sizes, or a different number of rotations—not a claim that the existing sumset already covers \(\mathbb F_p\).

No such step is paid in this body.

## 11. Target relation and disposition ceiling

The new uniform results concern the **actual** ordered dihedral word:

- interior rotations are consumed with their correct signs;
- selected boundary rotations contribute an explicit fixed offset;
- all block choices are disjoint;
- rotation availability uses original singleton cyclic gaps;
- selected length is exactly \(2p\);
- return to original linear order uses identity-preserving cyclic conjugation.

Theorems A–C cover structural regions across multiple deficits. Theorem D adds a complete deficit-eight type not supplied by those count bounds in its zero-rich branch.

Nevertheless:

- **The entire deficit-eight band is NOT PROVED.**
- At \(p=7\), the full named final high band \(o_\pi=11\) is **not** closed.
- F582's whole deficit-six candidate is not adopted or required as a premise.
- Existing adopted top-two and deficit-four statements retain their own scopes; this return changes no accepted frontier by itself.
- Lower projection bands, unrestricted ordered-Olson closure, all-group closure, avoiding words, original-source equivalence, novelty, and worldwide priority are not established.
- Scientific execution and finite replay are **NOTRUN**.
- No independent review, family check, human check, kernel check, or parent acceptance is asserted.

The principal new load-bearing obligations for fresh checking are the all-cut incidence count, the three-omission constant-window identity and rotation-budget loss, and the exceptional \(4+4\) protected-boundary-block construction.