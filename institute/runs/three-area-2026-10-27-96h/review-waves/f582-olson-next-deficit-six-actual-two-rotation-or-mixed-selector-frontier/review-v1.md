# F582 author-candidate-v1 — Whole actual deficit-six band by protected triples and mixed selectors

**Status: AUTHOR / WRITTEN PROOF CANDIDATE.** The argument below closes the complete actual deficit-six band for \(p\ge7\). It requires independent checking and parent disposition before adoption.

The construction uses exactly two rotations and \(2p-2\) reflections except in one arithmetic-progression branch, where it selects \(2p\) reflections and no rotations. Consequently, the result is a whole-band theorem for the requested actual identity subsequence, **not** a claim that every input admits a selector using exactly two rotations.

## 1. Read chronology, pins, and execution boundary

Before beginning the derivation, I completely read:

- The frozen manifest, logical lines 1–116.
- The freeze receipt, lines 1–47.
- All twelve named permission/status controls through their endings.
- The dispatch receipt and complete parent metadata supply.
- The literal packet consecutively in raw windows of at most twenty lines, through packet line 491.

The source endings observed were `S1|456` and `S2|33`. I then sent Main a direct pre-derivation ACK. Derivation began afterward.

The assigned manifest and receipt pins are:

- Manifest: `199badc850bf1113f5ba9d37692d29afb217a3e1211bf74df71a6aa3d5155c60`.
- Receipt: `7009f53c53bdb839b238cdac814505c72552d5de418cba208aa7c43cfbfd6c08`.
- Literal packet, according to the supplied receipt: `f8a73c493f8e9c498db4f9fccdaf770041f1c72423da68a177a0d0836b42351e`.

These hashes, byte counts, and the recorded clock are **parent-supplied observations**, not child-executed hash checks or a child-native execution receipt.

S1, the F568 deficit-four author candidate, remains **UNADOPTED**. Its shared local mechanism is reconstructed below rather than assumed as an accepted theorem. S2 retains only its stated adopted top-two-band scope.

No cited-but-unpasted scientific source, author executable, sibling return, or held scientific payload was opened. All held episodes **and their consumers** remain NONINPUT. This describes observable access and work chronology, not a cognitive-isolation certificate.

**Scientific execution: NOTRUN.** No interpreter, CAS, solver, scientific executable, or delegated calculation was used. No executable code was authored. All calculations below are written algebra. No external source was used, so there are no new public-source citations.

No repository file was written or write bypass attempted. This is the complete body for Main materialization as `author-candidate-v1.md`.

## 2. Exact theorem

### Actual deficit-six theorem

Let \(p\ge7\) be an odd prime. Let \(W\) be an actual linear word in \(D_{2p}\) with:

1. \(F=3p-2\) reflection occurrences;
2. \(R\ge p+1\) rotation occurrences;
3. at most one rotation occurrence in each gap between cyclically consecutive reflection occurrences.

Delete rotations while retaining reflection occurrence order. Let \(o_\pi\) be the number of odd-length maximal constant-label runs in the resulting cyclic reflection projection.

If
\[
o_\pi=3p-8,
\]
then \(W\) has an identity subsequence of exactly \(2p\) actual letters in its **original linear order**.

The proof is uniform in all reflection labels, rotation labels, run positions, and permitted rotation placements.

The relation \(3p-8\ge p+4\) holds for every prime in this theorem. Thus this is the complete next deficit-six band inside the assigned high-run domain.

## 3. Actual group products and the protected-triple selector

Write
\[
\rho_u=(u,0),\qquad \sigma_a=(a,1),
\]
with coordinates in \(\mathbb F_p\times\mathbb Z/2\mathbb Z\) and multiplication
\[
(x,e)(y,b)=\bigl(x+(-1)^e y,\ e+b\bigr).
\]
In particular,
\[
\sigma_a\sigma_b=\rho_{a-b}.
\]

Consider three chronological reflection occurrences with labels \(a,b,c\).

### 3.1 No selected interior rotation

Selecting two of these reflections gives the exponent set
\[
A_0(a,b,c)=\{a-b,\ a-c,\ b-c\}.
\]

A nonconstant triple has at least two exponents. A triple is called **rich** when this set has three exponents.

If both adjacent labels differ, put
\[
d=b-a,\qquad e=c-b.
\]
Then \(d,e\ne0\), and
\[
A_0(a,b,c)=\{-d,-e,-d-e\}.
\]
It has two elements exactly when \(d=e\). Thus, on an unequal-adjacency chain, absence of rich triples is exactly the arithmetic-progression condition.

### 3.2 One selected interior rotation

A selected \(\rho_u\) between the first and second reflections gives
\[
A^{(1)}_u(a,b,c)
=
\{a-u-b,\ a-u-c,\ u+b-c\}.
\]
The three entries correspond to selecting reflection pairs \((a,b)\), \((a,c)\), and \((b,c)\), respectively.

If \(b\ne c\), the first two entries differ for every \(u\). Call this first interior gap **safe** in that situation.

A selected \(\rho_u\) between the second and third reflections gives
\[
A^{(2)}_u(a,b,c)
=
\{a-b+u,\ a-u-c,\ b-u-c\}.
\]
If \(a\ne b\), the last two entries differ for every \(u\). Call this second interior gap **safe** in that situation.

Therefore:

- A nonconstant triple with unequal adjacent labels has two safe interior gaps.
- A nonconstant triple with an equal adjacent pair has one safe gap and one potentially unsafe gap.
- A constant triple always has a nonempty exponent set, whether or not it contains a selected rotation.

The potentially unsafe gap need not be the equal-label gap itself. The displayed formulas determine the actual sign routing.

### 3.3 Partition and rotation availability

Omit one reflection occurrence \(z\), cut immediately after it, and partition the remaining \(3p-3\) reflection occurrences into \(p-1\) consecutive triples.

A **protected** triple is one in whose interior no rotation will be selected. Its exponent set consequently remains exactly \(A_0\).

Let:

- \(B\) count potentially unsafe interior gaps of the **nonconstant** triples;
- \(h\) be the number of protected triples.

Exclude rotations in those \(B\) unsafe gaps and in the two interior gaps of every protected triple. At most
\[
B+2h
\]
rotation occurrences are excluded, because all these interior gaps are original singleton rotation gaps.

If
\[
R-(B+2h)\ge3,
\]
two remaining rotation occurrences can be selected without putting both inside the same triple:

- If a boundary rotation is available, choose it and any other remaining rotation.
- Otherwise three remaining interior occurrences cannot all lie in one triple, since a triple has only two interior gaps.

Fix such two rotations. Every triple now contains at most one selected interior rotation.

For each nonprotected nonconstant triple, its actual exponent set has at least two elements by safety. A constant triple retains at least one. Protected triples retain their original exact sets.

Let \(c\) be the sum of the selected boundary-rotation labels. Every selected block subword has two reflections and hence even reflection parity. The product in cut order is therefore
\[
\rho_{\,c+\sum_{i=1}^{p-1}d_i},
\qquad d_i\in A_i.
\]

This is the consuming-side calculation: interior rotations use the signed formulas above, while boundary rotations contribute \(+u\) between rotation-valued blocks.

If
\[
A_1+\cdots+A_{p-1}=\mathbb F_p,
\]
choose the block exponents to sum to \(-c\). The resulting subsequence has
\[
2(p-1)+2=2p
\]
distinct actual occurrences and identity product.

Any grouping of exponent sets below is grouping in the abelian rotation subgroup **after** these chronological block products have been computed. It does not reorder actual reflections.

Finally, returning to the original linear word merely cyclically rotates the selected groupword. If its cut product is \(UV=1\), then
\[
VU=U^{-1}(UV)U=1.
\]
Thus the same occurrences give identity in original linear order.

## 4. Finite-field sumsets and two additional growth lemmas

### 4.1 Sumset bound

For nonempty \(A,B\subseteq\mathbb F_p\),
\[
|A+B|\ge\min(p,|A|+|B|-1).
\]

For completeness, let \(a=|A|\), \(b=|B|\), and first suppose \(a+b-1\le p\). If the claim failed, enlarge \(A+B\) to a set \(C\) of size \(n=a+b-2<p\). The polynomial
\[
P(X,Y)=\prod_{c\in C}(X+Y-c)
\]
vanishes on \(A\times B\), but its \(X^{a-1}Y^{b-1}\) coefficient is
\[
\binom{n}{a-1}\ne0\quad\text{in }\mathbb F_p.
\]

For total degree at most \(a+b-2\), that coefficient equals
\[
\sum_{x\in A,\ y\in B}
\frac{P(x,y)}
{\displaystyle
 \prod_{x'\in A\setminus\{x\}}(x-x')
 \prod_{y'\in B\setminus\{y\}}(y-y')}.
\]
This is successive one-variable Lagrange coefficient extraction. The displayed sum is zero, a contradiction. The singleton boundary case is immediate.

If \(a+b-1>p\), choose nonempty subsets with cardinalities summing to \(p+1\), apply the proved case, and obtain the whole field.

Iteration gives
\[
|A_1+\cdots+A_t|
\ge
\min\left(p,1+\sum_i(|A_i|-1)\right).
\]

Consequences for \(p-1\) triple blocks include:

- No constant blocks: sets of size at least two suffice.
- One constant block and one protected rich block: all other sets of size at least two suffice.
- Two constant blocks and two protected rich blocks: all other sets of size at least two suffice.

### 4.2 Two different two-point directions

Put
\[
D_d=\{-d,-2d\}\qquad(d\ne0).
\]
If \(d\ne e\) and \(d\ne-e\), then
\[
|D_d+D_e|=4.
\]

Indeed, the four displayed sums are distinct: the only possible nontrivial collisions would force \(d=e\) or \(d=-e\).

This supplies one extra unit of growth beyond the ordinary \(2+2-1=3\) bound.

### 4.3 A rich triple and a two-point direction

Let
\[
T_{d,e}=\{-d,-e,-d-e\},
\qquad d,e\ne0,\ d\ne e.
\]
Then
\[
|T_{d,e}+D_d|<5
\quad\Longleftrightarrow\quad
e\in\{2d,-d\}.
\]

To prove this, remove the harmless common sign and translate the two-point set. The question becomes whether
\[
\{d,e,d+e\}+\{0,d\}
\]
has four rather than at least five elements.

A three-element set \(A\) satisfies \(|A\cup(A+d)|=4\) exactly when it consists of three consecutive elements in the cyclic order generated by \(d\). Each component of \(A\) in that cyclic order contributes one new element after translation.

The elements \(e,e+d\) are consecutive. For \(\{d,e,e+d\}\) to be a three-element interval, its remaining element \(d\) must equal either \(e-d\) or \(e+2d\). These give \(e=2d\) or \(e=-d\). Here \(p\ge7\) excludes the small-cycle identifications.

Interchanging \(d,e\) gives the corresponding criterion for \(T_{d,e}+D_e\).

## 5. Run classification and seven direct types

For maximal cyclic constant-run lengths \(\ell_j\),
\[
F-o_\pi
=
\sum_{\ell_j\ \mathrm{odd}}(\ell_j-1)
+
\sum_{\ell_j\ \mathrm{even}}\ell_j.
\]
Every positive contribution is even. Deficit six therefore gives exactly the following ten types, with all unlisted runs singleton:
\[
7;\quad6;\quad5+3;\quad5+2;\quad4+3;\quad4+2;
\quad3+3+3;\quad3+3+2;\quad3+2+2;\quad2+2+2.
\]

Seven types admit a partition with no constant triple:

| Run type | Omission and partition choice | Bound on \(B\) |
|---|---|---:|
| \(5+2\) | Omit the middle of the five-run | \(3\) |
| \(4+3\) | Omit the second or third occurrence of the four-run, choosing the phase avoiding the other constant triple | \(2\) |
| \(4+2\) | Omit the second occurrence of the four-run | \(2\) |
| \(3+3+3\) | Omit a suitable occurrence of one three-run | \(3\) |
| \(3+3+2\) | Omit a suitable occurrence of one three-run | \(3\) |
| \(3+2+2\) | Omit the middle of the three-run | \(2\) |
| \(2+2+2\) | Omit any occurrence | \(3\) |

Here are the phase and adjacency details.

For \(5+2\), omission leaves two length-two end fragments and the intact two-run. These contribute at most three internal equal adjacencies, and no constant triple.

For \(4+3\), omitting the second or third occurrence leaves end fragments of lengths \(2,1\) or \(1,2\). The intact three-run changes position by one between these choices, so it cannot be a triple block in both. In the good choice it contributes at most one internal equal adjacency; the four-run fragments contribute at most one.

For \(4+2\), the fragments and intact two-run each contribute at most one.

For \(3+3+3\), omit separately each of the three occurrences of one three-run. Each other three-run forbids at most one of these three phases. Thus one phase avoids both. The interrupted run contributes at most one internal equal adjacency, as does each straddling intact three-run.

For \(3+3+2\), the other three-run forbids only one phase. The interrupted run, straddling three-run, and two-run contribute at most one each.

The last two rows follow directly from the surviving length-two fragments or runs.

In every row, \(B\le3\), no protection is needed, and
\[
R-B\ge8-3=5.
\]
The selector in Section 3 applies, and \(p-1\) nonconstant triple sets cover the field. This proves all seven types.

## 6. One length-six run

Write the cyclic reflection projection as
\[
a_1,\ldots,a_6,\ x_1,\ldots,x_N,
\qquad N=3p-8,
\]
where every \(a_i\) has label \(a\), and all \(x_i\) are singleton runs.

For \(k=1,2,3\), let \(P_k\) omit \(a_k\), cut immediately afterward, and partition into triples.

Each \(P_k\) has exactly one constant triple and \(B\le1\). The relevant coverage is:

| Partition | Starts of triples wholly inside \(X\), modulo \(3\) | Additional unequal-adjacency boundary triples |
|---|---:|---|
| \(P_1\) | \(2\) | None needed |
| \(P_2\) | \(0\) | \((a,x_1,x_2)\), \((x_{N-1},x_N,a)\) |
| \(P_3\) | \(1\) | None needed |

For example, \(P_1\) begins with a constant triple followed by \((a,a,x_1)\); \(P_2\) begins with a constant triple followed by \((a,x_1,x_2)\); and \(P_3\) ends with \((x_N,a,a)\).

If any partition contains a rich triple, protect it. Then \(h=1\), \(B\le1\), and at least
\[
8-(1+2)=5
\]
rotation occurrences remain eligible. One rich block compensates the one constant block, giving the whole field and an actual two-rotation identity.

Suppose none contains a rich triple. The coverage above includes every consecutive triple of the unequal-adjacency chain
\[
Y=(a,x_1,\ldots,x_N,a).
\]
Thus \(Y\) is an arithmetic progression with nonzero increment \(d\).

Its length is
\[
N+2=3p-6\ge2p.
\]
The first \(2p\) reflections of this chronological chain have alternating sum
\[
-pd=0.
\]
They give an original-order identity subsequence of exactly \(2p\) reflections.

This zero-rotation branch can occur only at \(p=7\): the equal endpoints of \(Y\) imply
\[
(N+1)d=(3p-7)d=-7d=0.
\]
No exact-two-rotation conclusion is asserted for this exceptional branch.

This closes the entire six-run type.

## 7. One length-seven run

Write
\[
a_1,\ldots,a_7,\ x_1,\ldots,x_N,
\qquad N=3p-9.
\]

Consider \(P_2,P_3,P_4\), defined by omission and cut after \(a_2,a_3,a_4\), respectively.

| Partition | Constant blocks | \(B\) | Triple starts wholly inside \(X\) |
|---|---:|---:|---:|
| \(P_2\) | \(1\) | \(\le1\) | \(2\bmod3\) |
| \(P_3\) | \(1\) | \(\le1\) | \(0\bmod3\) |
| \(P_4\) | \(2\) | \(0\) | \(1\bmod3\) |

In addition, \(P_2\) contains the boundary triple \((x_{N-1},x_N,a)\), and \(P_3\) contains \((a,x_1,x_2)\).

If \(P_2\) or \(P_3\) has a rich triple, protect it. As in Section 6, it compensates the one constant block and gives a two-rotation identity.

If \(P_4\) has at least two rich triples, protect two. Here \(h=2\), \(B=0\), and at least four rotation occurrences remain eligible. The two rich blocks compensate its two constant blocks.

Assume neither of these situations holds.

### 7.1 Zero rich blocks in \(P_4\) is impossible

Together, the three partitions cover every consecutive triple of
\[
Y=(a,x_1,\ldots,x_N,a).
\]
If \(P_4\) also had no rich block, \(Y\) would be an arithmetic progression with nonzero increment \(d\). Its equal endpoints would force
\[
(N+1)d=(3p-8)d=-8d=0,
\]
impossible for \(p\ge7\).

### 7.2 The remaining one-rich-block case

There is therefore exactly one rich block in \(P_4\). Let \(r\) be the number of its preceding \(X\)-blocks and \(s\) the number of its following \(X\)-blocks. Then
\[
r+s=p-4.
\]

Every increment along \(Y\) is a fixed nonzero \(d\) before the rich block’s middle vertex and a fixed nonzero \(e\) afterward. The rich block has exponent set
\[
T_{d,e}=\{-d,-e,-d-e\},
\qquad d\ne e.
\]

The lengths of the two increment segments are
\[
L=3r+2,\qquad M=3s+2.
\]
Since \(Y\) begins and ends at \(a\),
\[
Ld+Me=0. \tag{1}
\]

Also \(e\ne-d\). Otherwise (1) gives
\[
3(r-s)d=0.
\]
Because \(|r-s|\le p-4<p\), this implies \(r=s\), contradicting that \(r+s=p-4\) is odd.

The preceding AP blocks have set \(D_d\), and the following AP blocks have set \(D_e\).

If \(r,s>0\), at least one of
\[
|T_{d,e}+D_d|,\qquad |T_{d,e}+D_e|
\]
is at least five. Otherwise Section 4.3 would give simultaneously
\[
e/d\in\{2,-1\},
\qquad
d/e\in\{2,-1\}.
\]
For \(p\ge7\), their only common possibility is \(e=-d\), already excluded.

If \(r=0\), equation (1) becomes
\[
2d+(3p-10)e=0,
\]
so \(d=5e\). The available AP direction is \(e\). The failure condition would require \(d/e\in\{2,-1\}\), whereas \(5\) equals neither modulo any prime \(p\ge7\). Hence
\[
|T_{d,e}+D_e|\ge5.
\]
The case \(s=0\) is symmetric.

Thus in every remaining case there is a rich block and an AP block whose combined exponent set has at least five elements.

Protect those two blocks. Since \(B=0\), at least four rotations remain eligible. After selecting the two rotations, the combined protected set still has size at least five, the other \(p-5\) nonconstant blocks have sets of size at least two, and the two constant blocks have nonempty sets. Consequently,
\[
|A_1+\cdots+A_{p-1}|
\ge
\min\bigl(p,\ 1+4+(p-5)\bigr)
=p.
\]

This supplies the required two-rotation identity and closes the entire seven-run type.

## 8. One length-five run and one length-three run

Write the cyclic run pattern as:

- five occurrences of label \(a\);
- \(u\) singleton occurrences;
- three occurrences of label \(b\);
- \(v\) singleton occurrences.

Here
\[
u+v=3p-10.
\]
The two long-run labels \(a,b\) need not be different.

### 8.1 The direct phases

Omit the middle \(a_3\) of the five-run. Its two remaining end fragments have length two.

The \(b\)-run becomes a constant triple block exactly when
\[
u\equiv1\pmod3.
\]

If \(u\not\equiv1\pmod3\), all blocks are nonconstant and \(B\le3\): the two \(a\)-fragments contribute at most two, and the straddling \(b\)-run contributes at most one. Section 3 closes this case.

Hence suppose
\[
u\equiv1\pmod3.
\]
Then also \(v\equiv1\pmod3\).

Let \(P_1,P_2,P_3\) omit \(a_1,a_2,a_3\), respectively. All three partitions have exactly one constant block:

- In \(P_1,P_2\), it comes from the five-run.
- In \(P_3\), it is the three-run.

Their nonconstant unsafe-gap counts satisfy \(B\le2\).

If any of the three partitions has a rich block, protect one. At least
\[
8-(2+2)=4
\]
rotations remain eligible, and the rich block compensates the constant block.

### 8.2 No rich block in these phases

Suppose none has a rich block.

The three phases cover all consecutive triples outside the five-run. They also cover the unequal-adjacency boundary triples at both ends of that outside interval. It follows that each of the following two chronological chains is an arithmetic progression:

1. from the final \(a\)-occurrence, through the \(u\) singleton occurrences, to the first \(b\)-occurrence;
2. from the final \(b\)-occurrence, through the \(v\) singleton occurrences, to the first \(a\)-occurrence.

Write
\[
u=3r+1,\qquad v=3s+1,
\qquad r+s=p-4.
\]
Let their nonzero increments be \(d,e\), respectively. Their endpoint equations give
\[
(3r+2)d+(3s+2)e=0. \tag{2}
\]

The directions cannot agree: \(d=e\) would turn (2) into
\[
(3p-8)d=-8d=0,
\]
impossible for \(p\ge7\).

They also cannot be opposite. If \(e=-d\), equation (2) implies \(r=s\), contradicting that \(r+s=p-4\) is odd.

Therefore
\[
d\ne e,\qquad d\ne-e. \tag{3}
\]

Now omit the middle occurrence \(b_2\) of the three-run and cut immediately afterward. The remaining sequence partitions exactly as follows:

1. \(s+1\) AP triples from
   \[
   b_3,\ \text{the \(v\) singleton occurrences},\ a_1;
   \]
2. the constant triple
   \[
   (a_2,a_3,a_4);
   \]
3. \(r+1\) AP triples from
   \[
   a_5,\ \text{the \(u\) singleton occurrences},\ b_1.
   \]

The first and third displayed chains have lengths
\[
v+2=3(s+1),\qquad u+2=3(r+1),
\]
so these are literal disjoint chronological triple partitions, not overlapping choices.

Protect one AP triple in each direction. Their exponent sets are \(D_d,D_e\), and by (3),
\[
|D_d+D_e|=4.
\]

All nonconstant triples have unequal adjacent labels, so \(B=0\). With \(h=2\), at least four rotations remain eligible. After selecting two, the protected combined set has size four, the remaining \(p-4\) nonconstant blocks have sets of size at least two, and the constant block has a nonempty set. Thus
\[
|A_1+\cdots+A_{p-1}|
\ge
\min\bigl(p,\ 1+3+(p-4)\bigr)
=p.
\]

The actual selector gives a two-rotation identity subsequence of exactly \(2p\) letters.

This closes the entire \(5+3\) type.

## 9. Whole-band conclusion and exact frontier relation

Sections 5–8 cover all ten deficit-six run types:

| Type | Complete uniform mechanism |
|---|---|
| \(7\) | Rich-block compensation or rich-plus-AP extra growth |
| \(6\) | Rich-block compensation or a \(2p\)-reflection AP selector |
| \(5+3\) | Nonconstant phase, rich compensation, or two-direction AP extra growth |
| \(5+2\) | Nonconstant partition |
| \(4+3\) | Nonconstant partition |
| \(4+2\) | Nonconstant partition |
| \(3+3+3\) | Nonconstant partition |
| \(3+3+2\) | Nonconstant partition |
| \(3+2+2\) | Nonconstant partition |
| \(2+2+2\) | Nonconstant partition |

Every two-rotation branch explicitly accounts for:

- original reflection occurrence order;
- selected interior-rotation signs;
- selected boundary rotations;
- availability under singleton actual rotation gaps;
- independent choices from disjoint blocks;
- distinct actual occurrences;
- selected length exactly \(2p\);
- cyclic-to-original identity transfer by conjugation.

This proves the stated complete actual deficit-six theorem. ∎

The existing accepted frontier is not changed merely by this AUTHOR return. If both the separately unadopted deficit-four candidate and this deficit-six candidate receive the required independent checking and parent adoption, the combined top-band coverage would be
\[
o_\pi\in
\{3p-8,\ 3p-6,\ 3p-4,\ 3p-2\}
\]
where each band lies in its stated prime domain.

Inside the named high-run domain, the resulting literal residual for \(p\ge7\) would be
\[
\boxed{
p+4\le o_\pi\le3p-10,\qquad o_\pi\ \text{odd}.
}
\]
At \(p=7\), that residual consists of \(o_\pi=11\). This body does not close it.

## 10. Proof, unpaid scope, and disposition ceiling

- **New author claim:** the complete actual deficit-six identity-subsequence theorem for every odd prime \(p\ge7\).
- **Mixed-selector qualification:** the AP branch for a single six-run selects zero rotations. It can occur only at \(p=7\). A universal exactly-two-rotation theorem is not claimed.
- **Scientific execution:** NOTRUN. There are no machine results, executable inputs, or finite-replay claims.
- **Avoiding words:** none claimed; no incomplete avoidance certificate is offered.
- **Unpaid original scope:** lower odd-projection bands, the displayed remaining high-run interval, unrestricted ordered-Olson closure, and all-group closure.
- **Review status:** AUTHOR, not a disjoint review. Independent F/M/m counts and an acceptance verdict are not asserted.
- **Acceptance ceiling:** not parent-adopted, independently reviewed, independent-family checked, human-checked, kernel-checked, or machine-verified.
- **Source and novelty ceiling:** no original-source equivalence, source authentication, novelty, or worldwide-priority claim.

The new load-bearing steps are the protected-block availability argument, the rich-plus-AP growth criterion, and the exceptional-phase \(5+3\) decomposition. They are explicit written proof obligations for the independent gates, not conclusions credited merely from author confidence.