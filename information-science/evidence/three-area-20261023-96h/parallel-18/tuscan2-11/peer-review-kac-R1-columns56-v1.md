# v35-C — product-trace columns S5/S6: exact central coefficients, remaining a/b gate

Observed `/bin/date` before creation: **Sun Oct 25 05:14:17 PDT 2026**. Reviewer `InfoRecursiveMDS18-2`, author `MathKacMoody`. This assignment began only after the complete v33-B return was written, pinned and delivered.

## Verdict first

**NOT_RECONSTRUCTED for the complete requested36-scalar column slice.** I derive all **twelve central-parameter coefficients**, together with complete grouped associative coefficient formulas for BOTH product-trace sources. The remaining **twenty-four a/b coefficients** have not been derived and are explicitly not accepted below.

Established mathematical defects in the reconstructed portion: **0 FATAL / 0 MAJOR / 0 MINOR**. There is one blocking **MAJOR reconstruction obligation R1-C**, not a finding that the advertised a/b entries are false. Neither a copied matrix nor the known central results is a proof of that remaining obligation.

No full matrix, determinant, invariant injectivity or actual3-to5 quotient verdict is given. The prior written R2 resolution is unchanged but does not transfer a verdict to these columns. No scientific eval/interpreter/arithmetic program, enumeration program, symbolic program, certificate replay, solver, CLI delegate or nested agent was used. All finite sums displayed here are written algebra. Only metadata hashes/clocks and source reading were performed. Parent erratumv7 is binding.

## 1. Exact pins and complete reading

Manifest v35 SHA-256 observed: `8bdc46291eb47f18245077588ad3811e2f5fad420e485f0710e7530cc5971b7a`.

The complete mandatory literal packet LF1–464 was read raw in ranges1–165,166–320,321–464. All source lines were exposed, none truncated:

|Label|Source|Read source LF|Observed SHA-256|
|---|---|---|---|
|N|`level5-written-R1-R2-reconstruction-v1.md`|1–306|`ef814cb9d86583ed4d81811cc47ac83bbc054c642778447602a6288509c8b91d`|
|Q|`level5-full-invariant-quotient-v1.md`|1–144|`a539f8b96afa6314367db190ae38bbd9c2f33afc517c2e96f5eb7a7d731129aa`|

Packet SHA-256 independently observed: `19a5f2bb04f7dbdbe2e20766813d8be5c1dda265bcf22128b1282e85694829f3`, matching its metadata receipt. The exact assignment, receipt and binding v7 qualifications were read before the proof pass.

Exposure is serial and supplied-proof: I authored v29-C and v33-B. I have already seen the advertised matrix and historical arithmetic statements, but use neither as a derivation. No other detector-slice or determinant-review verdict is inherited. This is cross-domain same-harness written reconstruction, not blind/cross-vendor/human/formal/novelty acceptance.

## 2. Literal normalizations and the exact contraction rules

Write d^i for the unscaled trace-dual of b_i. The off-diagonal dual is the reversed matrix unit; the Cartan duals are `(2H1+H2)/3` and `(H1+2H2)/3`. Thus c_i=3d^i and every five-slot source has common factor243. Q56–57 define

`F5=-81 S5`, `F6=-27 S6`.

The normalization factors after contracting all source indices are therefore **-3** and **-9**, respectively. They are different and must not be exchanged.

I recheck the contraction mechanism rather than assuming that a prior cut/join verdict evaluates these columns. For traceless x=E13 and output trace-dual Z,

`sum_i d^i M b_i=Tr(M)I-M/3`,
`sum_i d^i Tr(M b_i)=M-Tr(M)I/3`.

On a same-cycle source Tr(d^p A d^q B), summing q then p in the a term expands `[Z,[x,b_p]]` into four products. Their trace products are

`Tr(AZx)TrB-Tr(AZ)Tr(xB)-Tr(Ax)Tr(ZB)+TrA Tr(xZB)`.

The one-third corrections cancel. In the b term the second/fourth signs change, leaving the ADDITIONAL correction `(2/3)Tr(A[x,Z]B)`. The central contraction is `-Tr(xAZB)`. These are exactly N251–260.

For distinct cycles, duality replaces A by `A_0=A-Tr(A)I/3`, not automatically by A. Hence

`J_a=Tr(B[Z,[x,A]])`,
`J_b=Tr(B[Z,xA+Ax])-(2/3)TrA Tr(B[Z,x])`,
`J_c=-Tr(xA)Tr(ZB)`.

This proves the N268–270 branch. Its scalar correction can be nonzero for product-trace sources when A is a product of two fixed duals. It cannot be omitted globally. This derivation checks the FORMULA; it does not evaluate the twenty-four remaining a/b sums.

The right-normed associative permutations and ordered lowering positions are exactly N276–288. The tensor coefficient definitions below explicitly sum all sixteen permutations first, avoiding any unstated basis search.

## 3. Collapse of all sixteen tensor permutations for BOTH sources

For five traceless matrices A_0,...,A_4 and p<q, let r<s<t be the three remaining positions. Define

`T_pq=Tr(A_p A_q)Tr(A_r A_s A_t)`,
`U_pq=Tr(A_p A_q)Tr(A_r A_t A_s)`.

Pair symmetry and triple cyclicity are included in these definitions. For each subset R of{0,1,2,3}, the right-normed permutation is the complement increasingly, then4, then R decreasingly, with sign(-1)^|R|. Relabeling the original trace cycles by its inverse gives this COMPLETE grouping table:

|R|F5/243 signed tensor term|F6/243 signed tensor term|
|---|---|---|
|empty|T02|T03|
|0|-T14|-T24|
|1|-T01|-T02|
|2|-T04|-U02|
|3|-U02|-T04|
|01|T04|T14|
|02|T34|U14|
|03|U14|T34|
|12|T03|U01|
|13|U01|T03|
|23|U04|U03|
|012|-T24|-U04|
|013|-U04|-T24|
|023|-U34|-U24|
|123|-U03|-U02|
|0123|U24|U14|

For example R=0 gives tensor order(1,2,3,4,0). In F5, the original paired slots0,2 occur at positions4,1, and the triple1,3,4 retains its cyclic order: this is -T14. In F6, the original paired slots0,3 occur at4,2, again with forward triple orientation: -T24. The other rows follow from the same literal inverse-permutation rule; both trace cycles, not just one, have been moved.

Thus put

`Q5=(T02-U02)-(T14-U14)-(T01-U01)`
`       +(T34-U34)+(T03-U03)-(T24-U24)`,

`Q6=2T03+U03-2T24-U24-T02-2U02-T04-U04`
`       +T14+2U14+T34+U01`.

The associative tensor coefficients of the normalized sources are exactly

`[word]S5=-3 Q5`, `[word]S6=-9 Q6`,

where A_j is the trace-dual of that word's j-th generator. This is a new explicit grouped source derivation from the sixteen signed right-normed permutations. It is not the lowering matrix, and it does not independently supply its a/b coefficients.

## 4. Central lowering reduces to five insertions

To avoid confusing the parameter with matrix letters, write kappa for Q's scalar c=2-r-s in this section only.

The pure central local term is `-kappa Tr(x b_p)b_q`. After deleting tensor slot i, every later j contributes the SAME surviving four-letter word: no other generator label changes. There are4-i such positions. Trace duality inserts x at the deleted slot. Therefore, for any target word w with duals A_0,...,A_3,

`[w]D_c(S)=-kappa sum_(i=0)^3(4-i) Phi_S(A_0,...,A_(i-1),x,A_i,...,A_3)`.

Here Phi_S is the normalized associative source coefficient just derived. Slot4 has weight zero and may be included for a useful complete insertion table. Consequently the scalar coefficients to be derived are

`[kappa]M_i5=3 sum_(j=0)^4(4-j)Q5_j`,
`[kappa]M_i6=9 sum_(j=0)^4(4-j)Q6_j`.

There is no extra factor3 at this step: `sum_p d^p Tr(x b_p)=x`, since x is traceless. This also shows why the pure central computation does not require an a/b commutator contraction.

## 5. All insertion traces, with matrix-unit/Cartan reductions

Use the following matrix letters, all UNscaled duals:

`A=E21`, `B=E12`, `C=E32`, `D=E23`, `Y=E31`, `x=E13`,

`H=diag(2/3,-1/3,-1/3)`.

The six target dual words are

`A A B C`, `A A C B`, `A B A C`,
`A B Y H`, `A B H Y`, `A C C D`.

### Root-only rows

For the first three rows, the only nonzero paired trace is AB, with value1. For the last row it is CD, again value1. In either case the unpaired triple contains A,C,x, with

`Tr(A x C)=1`, `Tr(A C x)=0`,

and cyclic rotations preserving those values. Thus every surviving T/U pair is exactly(1,0) or(0,1). This collapses all unused trace paths to zero.

### Cartan rows

The only nonzero paired traces are AB and xY, both1. If the pair is AB, the remaining triple is x,Y,H:

`Tr(xYH)=2/3`, `Tr(xHY)=-1/3`.

If the pair is xY, the remaining triple is A,B,H:

`Tr(ABH)=-1/3`, `Tr(AHB)=2/3`.

Their cyclic rotations are the only further values needed. H paired with any available root has trace zero. These statements follow directly from multiplying the displayed matrix units and the three diagonal entries of H.

Using these rules in the sixteen-permutation source grouping yields the following COMPLETE five-insertion tables. Column j means x is inserted at position j of the four-letter target dual word:

|target|Q5_0|Q5_1|Q5_2|Q5_3|Q5_4|
|---|---:|---:|---:|---:|---:|
|A A B C|0|-1|1|1|-1|
|A A C B|2|-1|-1|1|-1|
|A B A C|0|-1|1|-1|1|
|A B Y H|-1|1|-1|1|0|
|A B H Y|0|0|2|-2|0|
|A C C D|0|0|-2|2|0|

|target|Q6_0|Q6_1|Q6_2|Q6_3|Q6_4|
|---|---:|---:|---:|---:|---:|
|A A B C|0|1|2|-1|-2|
|A A C B|1|-3|0|1|1|
|A B A C|0|-2|1|0|1|
|A B Y H|0|0|-1/3|2/3|-1/3|
|A B H Y|-1/3|0|2/3|-2/3|1/3|
|A C C D|-1|-1|1|1|0|

Two representative grouped reductions make the arithmetic reproducible rather than a copied final coefficient table:

1. For target A A C B, insertion0 is(x,A,A,C,B). Only pairs14 and24 survive. In each, T=0,U=1. Their Q5 contributions are+1,+1, while their Q6 contributions are+2,-1. Hence the table entries are2 and1.
2. For target A B H Y, insertion0 is(x,A,B,H,Y). PairAB occupies12 and contributes no term to either Q. PairxY occupies04; Q5 has no04 term, while Q6 contains-(T04+U04). The remaining tripleABH has total forward-plus-reverse trace1/3, yielding Q5=0,Q6=-1/3.

All other cells use the same explicit pair lists and cyclic orientations above. Each row's five entries sums to zero, as also follows from scalar derivations annihilating a positive-degree Lie bracket; this is an internal written consistency relation, not an executable check.

## 6. Twelve central coefficients actually derived

Multiplying the tables by weights(4,3,2,1,0) gives the Q5 weighted sums

`0,4,-2,-2,2,-2`,

and the Q6 weighted sums

`6,-4,-4,0,-2/3,-4`.

The normalization factors3 and9 from section4 therefore give

|detector row|central coefficient of S5 image|central coefficient of S6 image|
|---|---:|---:|
|1|0|54|
|2|12|-36|
|3|-6|-36|
|4|-6|0|
|5|6|-6|
|6|-6|-36|

These match the c coefficients advertised in Q102–107. Unlike copying that matrix, sections3–5 give the independent complete trace-permutation and insertion derivation for these twelve scalar values.

## 7. Precise unresolved R1-C obligation

The following identities remain **NOT_RECONSTRUCTED**, rather than false:

`[a]M_i5`, `[b]M_i5`, `[a]M_i6`, `[b]M_i6` for EVERY i=1,...,6.

This is24 scalars: both noncentral coefficients in both product-trace columns at all six detectors. I have not supplied a complete grouped evaluation of their same-cycle and different-cycle cut/join sums. The proof of K/J, the collapsed Q5/Q6 source formulas, and the twelve central coefficients do not logically establish those missing commutator/Jordan contractions.

In particular the essential scalar-trace subtraction in J_b has been derived, not silently discarded; but that derivation is not a numerical evaluation of every affected b coefficient. An acceptance verdict for columns5/6 must await those24 calculations. The exact remaining task can start from the compact Q5/Q6 formulas rather than the original8^5 source sums, applying the fully signed ordered lowering and both K/J branches.

No verdict is given on columns1–4, the determinant, full matrix equality with original D3, source-basis independence, invariant injectivity or actual3-to5 quotient. GeneralF5, the seven original nontrivial maps and H13 remain outside this slice. Historical kernel booleans and arithmetic outputs remain unadmitted and provide no credit.

**Final disposition:**12/36 requested scalar coefficients reconstructed in writing;24/36 explicitly NOT_RECONSTRUCTED. The column-slice gate remains OPEN, with no mathematical defect established in the supplied advertised values. This is an honest partial reconstruction return, not PASS and not a counterexample.
