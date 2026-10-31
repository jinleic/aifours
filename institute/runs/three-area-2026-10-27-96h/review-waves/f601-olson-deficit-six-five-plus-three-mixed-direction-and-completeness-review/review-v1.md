# F601 — Complete written review: deficit-six completeness and the \(5+3\) mixed-direction selector

**Role:** WRITTEN  
**Verdict:** **SUPPORTED at the exact stated actual-word scope.**  
**Mathematical findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Scientific execution:** **NOTRUN.**  
**Disposition ceiling:** Same-harness written review only; this review does not itself adopt the candidate.

This is the complete review body for parent materialization as `review-v1.md`. No repository file was written and no write bypass was attempted.

## 1. Frozen inputs, read chronology, and methodological boundary

The assigned wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f601-olson-deficit-six-five-plus-three-mixed-direction-and-completeness-review/`

The frozen metadata supplied by the parent identifies:

- **Manifest:** `c30deb3ed6cdb7f4d08b91b9b87acb5ca1f5bf294bc92488c4805cce65622a2d`
- **Freeze receipt:** `6f46622a28d1977d96b4b0e09cda1da75e9a7d2d0e9a6f17c73dcd3bccb0b308`
- **Literal packet:** `49299417a83b063d336a05ec5053b20899a541ad7956c4863d7e5d1d6682878d`

I read the complete manifest, freeze receipt, dispatch receipt, parent live-metadata supply, and all fourteen listed status-only controls before accessing the mathematical packet. I then sent a **direct PREBODY ACK to `agent://Main`**, before the first mathematical packet read.

After that ACK, I read the literal packet consecutively, in exact raw windows of at most twenty lines, from packet LF1 through LF713. The observed source endings were:

- **S1:** `S1|631`, the complete F582 candidate;
- **S2:** `S2|47`, the adopted deficit-four disposition;
- **S3:** `S3|33`, the adopted top-two-band disposition.

The receipt’s S1 count of 630 LF characters and the packet’s final logical source label `S1|631` are recorded as supplied; I do not silently replace one with the other.

All mathematical reconstruction below began after the entire packet had been read. It uses general variables and the objects explicitly supplied in the frozen packet. I did not select an additional concrete field instance, word, label assignment, diagnostic, or probe, privately or publicly. No interpreter, CAS, solver, enumeration, replay, scientific executable, author code, external model, linked scientific source, or sibling review was used.

The supplied clock **2026-10-30T14:07:19-0700 PDT**, and the supplied hash/byte/LF checks, are **parent observations**, not my native execution observations. No independent child hash execution or native start-time claim is made.

All held episodes and all their consumers, including f586, remain **HELD/ZERO/NONINPUT**. The controls were read as status and exclusion instructions only. No excluded links were followed.

The f582 ACK-after-packet sequence fault is preserved exactly as disclosed in its status control: the author reported an ACK before derivation but after packet access. That is not retroactively a successful pre-body ACK. It is also not, by itself, a mathematical refutation or quarantine of the frozen candidate. No new finding below depends on that episode.

## 2. Exact statement reviewed and permitted imports

### New statement under review

For an odd prime \(p\ge7\), let an actual linear word \(W\) in \(D_{2p}\) have:

1. exactly \(F=3p-2\) reflection occurrences;
2. at least \(R=p+1\) rotation occurrences;
3. at most one rotation occurrence in each **original cyclic gap** between consecutive reflection occurrences.

Let \(o_\pi\) count odd-length maximal constant-label runs in the cyclic, rotation-deleted reflection projection. The candidate asserts:

\[
o_\pi=3p-8
\quad\Longrightarrow\quad
W\text{ has an original-order identity subsequence of exactly }2p
\text{ actual occurrences.}
\]

This is S1 LF39–55.

The construction uses exactly two rotations and \(2p-2\) reflections in the two-rotation branches. The single-six-run AP branch instead uses \(2p\) reflections and no rotations; its occurrence is restricted to \(p=7\). The candidate does **not** assert that every input has an exactly-two-rotation selector.

### Imports

- **S2 LF3–5:** the adopted actual deficit-four result, for odd primes \(p\ge5\), under the same actual-word and cyclic-gap hypotheses.
- **S3 LF3–5:** the adopted actual top-two bands, for every odd prime, under their stated named hypotheses.

I use those dispositions only at their exact stated scopes. Their linked review bodies, code, and finite receipts were not opened. Their reported historical finite evidence is not represented as execution performed in this review.

S1’s statement that the deficit-four candidate was then unadopted is a historical qualification of the author return. In this frozen wave, S2 supplies the subsequently adopted deficit-four statement. The new deficit-six candidate remains unadopted pending parent disposition and the other required gates.

## 3. Per-claim results

| Claim | Result | Principal source |
|---|---|---|
| Actual local products and safe-gap routing | **SUPPORTED** | S1 LF59–119 |
| Protected-block rotation availability | **SUPPORTED** | S1 LF121–149 |
| Independent block choices, exact \(2p\) length, and original-cut transfer | **SUPPORTED** | S1 LF151–175 |
| Finite-field sumset bound and both extra-growth lemmas | **SUPPORTED** | S1 LF179–259 |
| Exhaustiveness of the ten deficit-six run types | **SUPPORTED** | S1 LF263–275 |
| All seven nonconstant-partition types | **SUPPORTED** | S1 LF277–307 |
| Complete single-six-run type, including the zero-rotation qualification | **SUPPORTED** | S1 LF309–358 |
| Complete single-seven-run type, including the one-rich-block case | **SUPPORTED** | S1 LF360–458 |
| \(5+3\) direct phase and exceptional-phase identification | **SUPPORTED** | S1 LF460–503 |
| Exceptional-phase AP reconstruction, direction separation, and literal \(b_2\)-omission selector | **SUPPORTED** | S1 LF505–573 |
| Whole deficit-six conclusion | **SUPPORTED** | S1 LF575–603 |
| Conditional union and remaining high-run interval | **SUPPORTED, conditional on adoption of the new band** | S1 LF605–618; S2 LF3–5; S3 LF3–5 |

The reconstructions supporting these results follow.

## 4. Actual selector: signs, routing, availability, and occurrence order

### 4.1 Local products

Using the packet’s coordinates,

\[
\rho_u=(u,0),\qquad \sigma_a=(a,1),\qquad
(x,e)(y,b)=\bigl(x+(-1)^e y,e+b\bigr),
\]

a chronological reflection pair has exponent \(a-b\). Thus a triple \((a,b,c)\), with no selected interior rotation, gives exactly

\[
A_0(a,b,c)=\{a-b,a-c,b-c\}.
\]

If \(d=b-a\) and \(e=c-b\) are nonzero, then

\[
A_0=\{-d,-e,-d-e\}.
\]

Its only possible equality is between \(-d\) and \(-e\): the other two possible equalities would force \(d=0\) or \(e=0\). Therefore an unequal-adjacency triple is non-rich exactly when \(d=e\). This justifies the later AP propagation without an additional structural theorem.

For a selected rotation in the first interior gap, the three actual pair selections give

\[
A_u^{(1)}
=\{a-u-b,\ a-u-c,\ u+b-c\}.
\]

For the second interior gap, they give

\[
A_u^{(2)}
=\{a-b+u,\ a-u-c,\ b-u-c\}.
\]

These include the cases in which omission of one reflection makes the selected rotation a prefix or suffix of its selected block subword. In particular, no uniform sign is incorrectly assigned to an interior rotation.

The first gap is safe when \(b\ne c\), because its first two displayed exponents differ. The second is safe when \(a\ne b\), because its last two displayed exponents differ. Consequently:

- an unequal-adjacency triple has two safe gaps;
- a nonconstant triple with one equal adjacent pair has only one potentially unsafe gap;
- a constant triple still has a nonempty achievable exponent set.

This verifies the consuming-side sign routing in S1 LF95–119.

### 4.2 Availability of two rotations

After omitting one reflection occurrence and cutting immediately after it, the other \(3p-3\) reflections form \(p-1\) disjoint chronological triples.

Let \(B\) count potentially unsafe interior gaps of nonconstant triples, and protect \(h\) triples by forbidding selected rotations in both of their interior gaps. The number of excluded actual rotation occurrences is at most

\[
B+2h.
\]

This is an upper bound even if some exclusions overlap or a gap contains no rotation.

If at least three rotations remain eligible, two can be chosen with at most one interior to each triple:

- an eligible boundary rotation can be paired with any other eligible rotation;
- if none is a boundary rotation, three eligible interior occurrences cannot all belong to one triple, since its two original interior gaps contain at most two rotations.

The two original gaps adjacent to the omitted reflection must remain distinct boundary positions. The proof does retain them: one is before the first block and the other after the last. It neither drops their rotations nor treats their combined boundary region as one fictitious original singleton gap.

The smallest availability bounds actually needed are:

| Branch | \(B\) | Protected triples \(h\) | Guaranteed eligible rotations |
|---|---:|---:|---:|
| Seven direct types | \(\le3\) | 0 | \(\ge5\) |
| Six-run rich compensation | \(\le1\) | 1 | \(\ge5\) |
| Seven-run one-constant compensation | \(\le1\) | 1 | \(\ge5\) |
| Seven-run two protected blocks | 0 | 2 | \(\ge4\) |
| \(5+3\) rich compensation | \(\le2\) | 1 | \(\ge4\) |
| \(5+3\) two-direction selector | 0 | 2 | \(\ge4\) |

Here \(R\ge p+1\ge8\). Each bound exceeds the required threshold of three.

### 4.3 Global product and exact length

Every selected triple subword contains exactly two reflections and at most one selected interior rotation. It therefore has even reflection parity and is a rotation. If \(c\) is the sum of labels of selected boundary rotations, the full cut-order product is

\[
\rho_{\,c+\sum_i d_i},\qquad d_i\in A_i.
\]

Boundary rotations contribute with positive sign between the rotation-valued blocks. Interior prefix/suffix cases have already been consumed in their respective \(A_i\); they are not counted again in \(c\).

The blocks use disjoint reflection occurrences. The two selected rotation occurrences are fixed and distinct before the exponent choices are made. Consequently, independent choices from the \(A_i\) really are simultaneously realizable chronological choices, not incompatible choices from overlapping triples.

If the sumset is \(\mathbb F_p\), choose \(\sum_i d_i=-c\). The selection then has exactly

\[
2(p-1)+2=2p
\]

actual occurrences.

Finally, restoring the original linear cut cyclically rotates the selected groupword. If the cut product is \(UV=1\), the restored product is

\[
VU=U^{-1}(UV)U=1.
\]

This is a valid identity-preserving conjugation argument, not an assertion that arbitrary nonidentity cyclic products are equal.

## 5. Sumset bounds and protected extra growth

### 5.1 Iterated sumset bound

The supplied polynomial argument proves

\[
|A+B|\ge\min(p,|A|+|B|-1)
\]

for nonempty subsets of \(\mathbb F_p\). In the non-saturated case, the degree is \(a+b-2<p\), the relevant binomial coefficient is nonzero, and the displayed coefficient-extraction identity contradicts vanishing on \(A\times B\). The singleton boundary case is immediate. Subsets of cardinalities summing to \(p+1\) give the saturated case.

Iteration therefore yields

\[
|A_1+\cdots+A_t|
\ge
\min\!\left(p,1+\sum_i(|A_i|-1)\right).
\]

For \(p-1\) blocks, the bookkeeping is correct:

- all nonconstant blocks of size at least two already give \(p\);
- one protected rich block compensates one constant block;
- two protected rich blocks compensate two constant blocks.

### 5.2 Two AP directions

For \(D_d=\{-d,-2d\}\), the four sums in \(D_d+D_e\) are distinct when \(d,e\ne0\) and \(d\ne\pm e\). Every possible collision would force one of those excluded equalities. Hence

\[
|D_d+D_e|=4.
\]

This is exactly one extra unit over the ordinary two-plus-two growth bound.

### 5.3 Rich-plus-AP growth

For

\[
T_{d,e}=\{-d,-e,-d-e\},
\qquad d,e\ne0,\quad d\ne e,
\]

the candidate reduces the cardinality question to

\[
\left|\{d,e,d+e\}+\{0,d\}\right|.
\]

A proper three-element subset of the cyclic order generated by \(d\) gains exactly one element under translation by \(d\) precisely when it forms one three-element interval. Since \(e,e+d\) are already consecutive, its third element \(d\) must extend that pair at one end. Thus

\[
|T_{d,e}+D_d|<5
\quad\Longleftrightarrow\quad
e\in\{2d,-d\}.
\]

The symmetric criterion follows by exchanging \(d,e\). The stated \(p\ge7\) domain excludes the small-cycle identifications relevant to the later simultaneous-failure argument.

These are written cardinality arguments; no finite test was used.

## 6. Exhaustive deficit-six classification and the seven direct types

For every maximal cyclic constant run of length \(\ell\),

\[
\ell-\mathbf 1_{\ell\text{ odd}}
=
\begin{cases}
\ell-1,&\ell\text{ odd},\\
\ell,&\ell\text{ even}.
\end{cases}
\]

Thus every positive run contribution to \(F-o_\pi\) is even. A total of six has only contribution partitions \(6\), \(4+2\), or \(2+2+2\). A contribution of six corresponds to length six or seven; four to length four or five; two to length two or three. This gives exactly

\[
7;\ 6;\ 5+3;\ 5+2;\ 4+3;\ 4+2;\
3+3+3;\ 3+3+2;\ 3+2+2;\ 2+2+2.
\]

There is no omitted deficit-six type.

For the seven direct types:

| Type | Reconstruction | Bound |
|---|---|---:|
| \(5+2\) | Omit the middle of the five-run. Its surviving end fragments have length two; the other long run also has length two. No constant triple can occur. | \(B\le3\) |
| \(4+3\) | The second and third omissions in the four-run shift the intact three-run’s block phase by one. It cannot be an entire triple in both phases. Choose a nonaligned phase. | \(B\le2\) |
| \(4+2\) | Omit the second occurrence of the four-run. There is one possible internal equal adjacency from its length-two fragment and one from the intact two-run. | \(B\le2\) |
| \(3+3+3\) | The three omissions in one three-run give all three phases for each intact three-run. Each intact run forbids at most one phase, leaving at least one choice avoiding both constant blocks. | \(B\le3\) |
| \(3+3+2\) | The intact three-run forbids only one of the three phases. The interrupted run, straddling three-run, and two-run contribute at most one internal equality each. | \(B\le3\) |
| \(3+2+2\) | Omit the middle of the three-run. Its fragments are singletons, leaving only the two possible internal equalities in the double runs. | \(B\le2\) |
| \(2+2+2\) | Every surviving run or end fragment has length at most two, regardless of the omitted occurrence. | \(B\le3\) |

The omission cut does not create a new internal adjacency between its two ends. All triples are nonconstant, all remaining local sets have size at least two after the permitted rotation selection, and the iterated sumset bound covers \(\mathbb F_p\). Thus these seven types are uniformly closed.

## 7. Single-six-run type and its zero-rotation exception

Write the supplied generic reflection pattern as

\[
a_1,\ldots,a_6,x_1,\ldots,x_N,
\qquad N=3p-8,
\]

where the \(x_i\) are singleton runs. Adjacent \(x_i\) differ, and the two outer singleton labels differ from \(a\).

For omission partitions \(P_1,P_2,P_3\), the reconstruction agrees with S1 LF320–328:

- each has exactly one constant triple;
- \(B\le1\);
- wholly-\(X\) triple starts cover residues \(2,0,1\), respectively;
- \(P_2\) supplies both unequal-adjacency boundary triples of
  \[
  Y=(a,x_1,\ldots,x_N,a).
  \]

If any partition has a rich block, protecting it compensates the one constant block and gives the two-rotation selector.

If none has a rich block, every consecutive triple of \(Y\) is non-rich and has unequal adjacent labels. Hence all successive increments of \(Y\) equal one nonzero \(d\).

The chain contains

\[
N+2=3p-6\ge2p
\]

distinct actual reflection occurrences. Its first \(2p\) reflections have alternating sum \(-pd=0\). This gives a chronological identity selection of exactly \(2p\) reflections and zero rotations.

The chain’s equal endpoint labels imply

\[
(N+1)d=(3p-7)d=-7d=0.
\]

Since \(d\ne0\), the prime must be \(p=7\).

**Conclusion:** The complete six-run type is supported. The zero-rotation branch is correctly confined to \(p=7\); the proof does not improperly upgrade that branch to an exactly-two-rotation conclusion.

## 8. Single-seven-run type, including exactly one rich \(P_4\) block

Here

\[
a_1,\ldots,a_7,x_1,\ldots,x_N,
\qquad N=3p-9.
\]

The three supplied partitions have the stated properties:

| Partition | Constant triples | Unsafe-gap bound | Wholly-\(X\) starts |
|---|---:|---:|---:|
| \(P_2\) | 1 | \(B\le1\) | \(2\bmod3\) |
| \(P_3\) | 1 | \(B\le1\) | \(0\bmod3\) |
| \(P_4\) | 2 | \(B=0\) | \(1\bmod3\) |

Together with the boundary triples supplied by \(P_2\) and \(P_3\), these cover every consecutive triple of

\[
Y=(a,x_1,\ldots,x_N,a).
\]

A rich block in \(P_2\) or \(P_3\) compensates its one constant block. Two rich blocks in \(P_4\) compensate its two constant blocks. These cases satisfy the rotation-availability bound.

If all three partitions had no rich block, \(Y\) would be an AP with nonzero increment \(d\), and equal endpoints would give

\[
(3p-8)d=-8d=0,
\]

which is impossible in the stated prime domain.

Therefore the remaining case has exactly one rich block in \(P_4\). If \(r\) and \(s\) count its preceding and following \(X\)-blocks, then

\[
r+s=p-4.
\]

All consecutive triples other than that rich block impose equality of successive increments. Thus the increments before its middle vertex are a fixed nonzero \(d\), and those afterward are a fixed nonzero \(e\), with \(d\ne e\). Their respective counts are

\[
L=3r+2,\qquad M=3s+2,
\]

so the equal endpoint labels give

\[
Ld+Me=0.
\]

If \(e=-d\), then \(3(r-s)d=0\). Because \(p\ge7\), \(|r-s|<p\), and \(d\ne0\), this forces \(r=s\). That contradicts the oddness of \(r+s=p-4\).

When both \(r,s>0\), failure of both available rich-plus-AP combinations would require

\[
e/d\in\{2,-1\},
\qquad d/e\in\{2,-1\}.
\]

For \(p\ge7\), simultaneous failure leaves only \(e=-d\), already excluded. Thus one available AP direction combines with the rich block to give at least five exponents.

When \(r=0\), the endpoint equation gives \(d=5e\). The available AP direction is \(e\), and its failure condition would require \(d/e\in\{2,-1\}\). Neither equality holds for any prime \(p\ge7\). The \(s=0\) argument is symmetric.

Protect that rich block and one suitable AP block. There are two constant blocks, a protected combined set of size at least five, and \(p-5\) other nonconstant blocks. Hence

\[
|A_1+\cdots+A_{p-1}|
\ge
\min\bigl(p,1+4+(p-5)\bigr)=p.
\]

**Conclusion:** The entire seven-run type is supported, including the endpoint cases \(r=0\) and \(s=0\). No availability or block-count gap remains.

## 9. The \(5+3\) type: direct phases, complete AP coverage, and the literal mixed selector

This is the principal assigned focus.

### 9.1 Direct phase and exceptional congruence

The supplied run pattern is

\[
a_1,\ldots,a_5,\quad
u\text{ singleton occurrences},\quad
b_1,b_2,b_3,\quad
v\text{ singleton occurrences},
\]

with

\[
u+v=3p-10.
\]

The long-run labels \(a,b\) are not assumed distinct.

Omitting \(a_3\) leaves a length-two head fragment and a length-two tail fragment. In this partition, the first \(b\)-occurrence is at reflection position \(u+3\). The \(b\)-run is an entire triple exactly when this start is \(1\bmod3\), namely exactly when

\[
u\equiv1\pmod3.
\]

If that congruence fails, all blocks are nonconstant and \(B\le3\), so the direct selector applies.

In the exceptional phase, \(u\equiv1\pmod3\), the total-length equation gives \(v\equiv1\pmod3\) as well. Consequently,

\[
u=3r+1,\qquad v=3s+1,\qquad r,s\ge0,\qquad r+s=p-4.
\]

In particular, both singleton intervals have at least one occurrence. No hidden assumption that either interval is longer is required.

### 9.2 Exactly one constant block in each of \(P_1,P_2,P_3\)

Let \(P_k\) omit \(a_k\) and cut immediately afterward.

- **\(P_1\):** \((a_2,a_3,a_4)\) is the constant block. The surviving \(b\)-run straddles blocks.
- **\(P_2\):** \((a_3,a_4,a_5)\) is the constant block. Again the \(b\)-run straddles blocks.
- **\(P_3\):** \((b_1,b_2,b_3)\) is the constant block. The two surviving \(a\)-fragments each have length two.

Thus every partition has exactly one constant block. Their nonconstant unsafe-gap counts are bounded by two; \(P_1\) and \(P_2\) in fact need at most one.

If any contains a rich block, protect it. The single rich block compensates the single constant block, and at least four rotations remain eligible. This branch is supported.

### 9.3 Why absence of rich blocks forces both entire outside chains to be APs

For clarity, denote the two already-supplied singleton intervals generically by \(X\) and \(Z\); this is notation for the arbitrary input occurrences, not an additional selected instance.

Consider the chronological unequal-adjacency chains

\[
C_d=(a_5,X,b_1),
\qquad
C_e=(b_3,Z,a_1).
\]

Their lengths are

\[
u+2=3(r+1),\qquad v+2=3(s+1).
\]

The three partitions provide the following coverage:

| Partition | Coverage in \(C_d\) | Coverage in \(C_e\) |
|---|---|---|
| \(P_1\) | The complete disjoint triple partition of \(C_d\), including its end windows | Wholly-\(Z\) starts \(2\bmod3\) |
| \(P_2\) | Wholly-\(X\) starts \(1\bmod3\) | The complete disjoint triple partition of \(C_e\), including its end windows |
| \(P_3\) | Wholly-\(X\) starts \(2\bmod3\) | Wholly-\(Z\) starts \(1\bmod3\) |

In the full-chain triple partitions, wholly-singleton starts have residue \(0\bmod3\). Thus the three partitions jointly cover every wholly-singleton triple start in each chain, and the complete-chain partitions supply the boundary windows.

This reasoning also covers \(r=0\) or \(s=0\): the corresponding full chain is simply one triple. Statements about internal starts are needed only when those starts exist. No nonexistent second singleton is assumed.

Every adjacent pair in either chain has unequal labels, by maximality of the original runs and the singleton-run condition. If none of \(P_1,P_2,P_3\) has a rich block, every consecutive triple of both chains is therefore non-rich with unequal adjacent labels. Successive increments consequently agree throughout each chain.

This proves that the **entire** two chains, not merely separate disjoint blocks, are APs with nonzero increments \(d\) and \(e\).

### 9.4 Endpoint equations separate the two directions

The first chain goes from label \(a\) to label \(b\), and the second from \(b\) back to \(a\). Therefore

\[
b-a=(3r+2)d,\qquad
a-b=(3s+2)e,
\]

and hence

\[
(3r+2)d+(3s+2)e=0.
\]

This equation is valid even when the original long-run labels coincide; no division by \(b-a\) is used.

If \(d=e\), it gives

\[
(3p-8)d=-8d=0,
\]

impossible for the stated primes and nonzero \(d\).

If \(e=-d\), it gives \(3(r-s)d=0\). Since \(p\ge7\) and \(|r-s|\le p-4<p\), this implies \(r=s\), contrary to \(r+s=p-4\) being odd.

Thus

\[
d\ne e,\qquad d\ne-e.
\]

The required extra-growth condition is proved uniformly, rather than inferred from different endpoint labels or from a selected example.

### 9.5 Omitting \(b_2\) gives an actual disjoint partition

Now omit the middle occurrence \(b_2\), and cut immediately after it. The remaining chronological reflection list is exactly

\[
(b_3,Z,a_1),\qquad
(a_2,a_3,a_4),\qquad
(a_5,X,b_1).
\]

The first and last displayed chains have lengths \(3(s+1)\) and \(3(r+1)\). They therefore partition into:

- \(s+1\) AP triples of direction \(e\);
- one constant triple \((a_2,a_3,a_4)\);
- \(r+1\) AP triples of direction \(d\).

The total number of blocks is

\[
(s+1)+1+(r+1)=r+s+3=p-1.
\]

They are literal disjoint blocks of actual occurrences. In particular, \(a_1\) and \(a_5\), and \(b_1\) and \(b_3\), are different occurrences even when labels coincide. No overlapping choices or freely reordered projection labels are introduced.

Each AP triple has unequal adjacent labels, so the nonconstant unsafe-gap count is \(B=0\). At least one AP triple exists in each direction, including the cases \(r=0\) or \(s=0\).

Protect one triple from each direction. Their exact sets are \(D_d,D_e\), and direction separation gives

\[
|D_d+D_e|=4.
\]

With \(h=2\), at least four actual rotations remain eligible. After choosing the two permitted rotation occurrences, the combined protected set still has size four. There are \(p-4\) other nonconstant blocks and one constant block. Therefore

\[
|A_1+\cdots+A_{p-1}|
\ge
\min\bigl(p,1+3+(p-4)\bigr)=p.
\]

The chronological selector from Section 4 then yields exactly \(2p-2\) reflections and two rotations, with identity product in the original linear word.

**Conclusion:** The complete exceptional-phase \(5+3\) argument is supported. The AP reconstruction, nonzero directions, exclusion of equal and opposite directions, literal repartition, rotation availability, sumset growth, and exact occurrence count all close.

## 10. Whole-band conclusion and exact residual

The exhaustive classification has ten types. Section 6 closes seven of them; Sections 7–9 close \(6\), \(7\), and \(5+3\). Thus the candidate proves its stated whole actual deficit-six band for every odd prime \(p\ge7\).

The proof supports exactly the following selector qualification:

- the two-rotation branches select \(2p-2\) reflections and two rotations;
- the single-six-run AP branch selects \(2p\) reflections and zero rotations and can occur only at \(p=7\);
- no universal exactly-two-rotation claim is established or needed.

The currently imported adopted coverage remains:

\[
o_\pi\in\{3p-6,3p-4,3p-2\}
\]

at the respective prime domains of S2 and S3. This review does not itself add the new band to the adopted frontier.

**If the new deficit-six candidate receives the required gates and parent adoption**, then for \(p\ge7\) the named actual-word setting would have coverage

\[
o_\pi\in\{3p-8,3p-6,3p-4,3p-2\}.
\]

Since the deficit identity forces \(o_\pi\) to be odd, the resulting literal residual inside the named high-run domain would be exactly

\[
\boxed{p+4\le o_\pi\le3p-10,\qquad o_\pi\text{ odd}.}
\]

The packet’s stated \(p=7\) residual \(o_\pi=11\) is not closed by this candidate or this review. No claim is made for the next deficit-eight band, lower bands, unrestricted ordered-Olson closure, or all finite groups.

Until new parent adoption, the new deficit-six band remains an author candidate with written support, and the adopted residual is not silently reduced.

## 11. Findings and acceptance limits

**No mathematical defect was found in the frozen candidate at its stated scope: 0 FATAL / 0 MAJOR / 0 MINOR.**

The already-disclosed author ACK-after-packet fault remains a separate historical process qualification. It has not been backdated, excused, or converted into mathematical evidence. This review’s own direct pre-body ACK preceded all packet access.

This review provides:

- a complete written reconstruction of all ten run types;
- detailed verification of the exceptional \(5+3\) phase and mixed-direction selector;
- verification of the seven-run one-rich-block argument;
- explicit accounting for actual rotation gaps, interior signs, disjoint occurrences, selected length, and original-order identity transfer;
- the exact conditional union and residual.

It does **not** provide:

- scientific execution, a finite replay, or an independently executed metadata check;
- an independently audited account of the author’s private work history;
- parent adoption or completion of the other fresh gates;
- independent-family, external-model, human, or kernel verification;
- original-source correspondence, source authentication, novelty, worldwide priority, or global problem closure;
- a cognitive-isolation certificate.

**overall_correctness:** correct

**explanation:** The complete written argument establishes the stated actual deficit-six identity-subsequence theorem, including all ten run types and the qualified zero-rotation AP branch. The exceptional \(5+3\) case has complete phase coverage and a disjoint mixed-direction construction with sufficient actual rotation availability. Adoption and the corresponding frontier reduction remain conditional on the parent’s required remaining gates and disposition.

**confidence:** 0.97