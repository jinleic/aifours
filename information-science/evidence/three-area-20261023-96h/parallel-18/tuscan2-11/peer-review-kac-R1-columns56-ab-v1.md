# v39-A — written completion of the24 noncentral S5/S6 detector coefficients

Observed `/bin/date` before creation: **Sun Oct 25 05:31:52 PDT 2026**. Reviewer `InfoRecursiveMDS18-2`; author `MathKacMoody`.

## Verdict

**The24 remaining a/b scalars in my v35-C gate are RECONSTRUCTED IN WRITING.** All six detector rows of both product-trace columns agree exactly with the displayed author pencil. **0 FATAL / 0 MAJOR / 0 MINOR defects found at this column-source identity scope; no mismatches.**

The derivation below supplies compact tensor copairs, explicit matrix-unit/Cartan trace tables, all grouped intermediate contractions, and their final sums. It uses neither the advertised coefficients as premises nor old program output. Together with the twelve central coefficients derived in v35-C, this completes THIS reviewer's36-scalar column5/6 slice. No verdict on the other columns, determinant, R2, source-basis independence or full invariant/actual3-to5 theorem transfers from this slice.

**WRITTEN ONLY:** no scientific interpreter/eval/arithmetic program, symbolic program, enumeration program, certificate replay, solver, CLI delegate or nested agent. Metadata hashes/clocks and source reading only. Parent erratumv7 is binding; no unadmitted arithmetic credit is used.

## 1. Frozen sources and serial exposure

Assignment v39-A; observed manifest SHA-256 `030c81efcb0e11c658a2a49fad2940c8075ca77b4037463efd07dad168ce07fe`.

The complete literal packet LF1–464 was read raw in ranges1–165,166–320,321–464, with no truncated or skipped source line. Original bytes were independently metadata-hashed:

|Label|Source|Complete LF|Observed SHA-256|
|---|---|---|---|
|N|`level5-written-R1-R2-reconstruction-v1.md`|1–306|`ef814cb9d86583ed4d81811cc47ac83bbc054c642778447602a6288509c8b91d`|
|Q|`level5-full-invariant-quotient-v1.md`|1–144|`a539f8b96afa6314367db190ae38bbd9c2f33afc517c2e96f5eb7a7d731129aa`|

Packet SHA-256 observed: `5bc358220a806ef6011da4ce28f468e3533801a56a9cc3768fe3b059a054a047`, matching the metadata receipt. Entry/v7/receipt were read before the full body.

This is deliberately the same reviewer as v35-C. My prior compact Q5/Q6 definitions and twelve central calculations are used as explicit written source identities, not a verdict that already cleared the missing a/b terms. I have seen the advertised pencil, but each new coefficient follows from the reductions below. No peer detector/determinant verdict was read or inherited. This is same-harness supplied-proof cross-domain review, not blind/cross-vendor/human/formal/novelty acceptance.

The original local bracket is exactly Q82–93; the source definitions are Q56–57, and detectors are Q67–68. The actual-isotypic interpretation retains the named positive-elimination/no-invariantT5/no-adjointT4 imports Q25–33. This paper calculation reconstructs the literal free tensor coefficients; it does not re-prove the entire imported structural source.

## 2. Product-trace polynomials, source scales and useful Lie identities

For five traceless matrices A0,...,A4, and p<q with remaining r<s<t, put

`T_pq=Tr(Ap Aq)Tr(Ar As At)`,
`U_pq=Tr(Ap Aq)Tr(Ar At As)`.

The complete sixteen-right-normed-permutation grouping in v35-C gives

`Q5=(T02-U02)-(T14-U14)-(T01-U01)`
`       +(T34-U34)+(T03-U03)-(T24-U24)`,

`Q6=2T03+U03-2T24-U24-T02-2U02-T04-U04`
`       +T14+2U14+T34+U01`.

The unscaled dual normalization is d^i=b^i, c_i=3d^i. Thus the source coefficients are `Phi5=-3Q5`, `Phi6=-9Q6`, since243/(-81)=-3 and243/(-27)=-9. Neither factor is fitted to the target pencil.

Write

`g(A,B)=Tr(AB)`,
`f(A,B,C)=Tr(A[B,C])`,
`d(A,B,C)=Tr(A{B,C})`.

The f tensor is alternating and the d tensor is symmetric. Define the symmetric product-trace polynomial

`R=2Q6-Q5=3d03-3d24-3d02-2d04+3d14+d34+d01`,

where `d_pq=g(Ap,Aq)d(Ar,As,At)`. Consequently

`Q6=(Q5+R)/2`.                                            (1)

Every normalized source is a degree-five Lie polynomial. Two coefficient identities therefore hold for Phi, Q5 and Q6, hence also R:

- reversal preserves the coefficient: `Phi(A0,...,A4)=Phi(A4,...,A0)`;
- the sum over all five insertions of any traceless P into a fixed four-slot word is zero.

The first follows by reversing a Lie bracket of total degree five, which has reversal sign(-1)^4=+1. The second follows by applying the scalar-valued derivation `u_b -> Tr(Pb)` to a Lie bracket of degree>=2. These are algebraic identities, not new enumerations.

## 3. The original a/b lowering as a FOUR-dyad copair

Let x=E13. If the acted output detector has unscaled trace-dual Z, its contracted original inputs are represented by

`K_a(Z)=sum_p d^p tensor [Z,[x,b_p]]`,
`K_b(Z)=sum_p d^p tensor [Z,x b_p+b_p x]`.

These follow directly by first summing the acted input q with trace duality in Q87–89. They retain the ordered deleted/acted input distinction.

Use the matrix letters

`A=E21, B=E12, C=E32, D=E23, Y=E31, x=E13`,

`h1=diag(1,-1,0), h2=diag(0,1,-1)`,

`K=h1+h2=diag(1,0,-1)`,
`P=(h1-h2)/3=diag(1,-2,1)/3`,

`H=(2h1+h2)/3=diag(2,-1,-1)/3`,
`J=(h1+2h2)/3=diag(1,1,-2)/3`.

Only b1,b3,b5,b6,b7 contribute to the displayed copairs. Their original brackets with x are respectively -D,B,K,-x,-x. Their Jordan products with x are D,B,E11+E33,x,-x. Using d^1=B,d^3=D,d^5=x,d^6=H,d^7=J, and H+J=K,H-J=P, gives

`K_a(Z)=-B tensor[Z,D]+D tensor[Z,B]`
`             +x tensor[Z,K]-K tensor[Z,x]`,

`K_b(Z)= B tensor[Z,D]+D tensor[Z,B]`
`             +x tensor[Z,P]+P tensor[Z,x]`.             (2)

Replacing E11+E33 by its traceless part P INSIDE its commutator is legitimate because its scalar part commutes. This does not discard the scalar input projection in the separate-cycle formula.

For a pair of test matrices define the ordered pair of scalar contractions

`k_Z(M,N)=(sum_(U tensor V in K_a)Tr(UM)Tr(VN),`
`             sum_(U tensor V in K_b)Tr(UM)Tr(VN))`.

Equivalently, writing M0=M-Tr(M)I/3,

`k_Z(M,N)=(Tr(N[Z,[x,M]]),`
`  Tr(N[Z,xM+Mx])-(2/3)Tr(M)Tr(N[Z,x]))`.                (3)

The second component is EXACTLY the essential J_b scalar-trace correction. No unprojected anticommutator may be substituted as its first input. All numerical work below uses (3), or equivalently the explicit traceless copair(2).

Define, for traceless T,

`tau_Z=(6Tr(xZ),0)`,
`f_Z(T)=(3Tr(x[Z,T]), -3Tr(x{Z,T}))`,
`d_Z(T)=(3Tr(x{Z,T}), -(5/3)Tr(x[Z,T]))`.               (4)

These are respectively contractions of g(U,V), f(U,V,T), d(U,V,T) with the two copairs. They follow by the same-cycle completeness identities N251–260. For instance the two cyclic triple contractions have a parts3Tr(xZT),3Tr(xTZ); their b parts combine to -3 times the anticommutator for f, and -5/3 times the commutator for d. They also follow by direct substitution in the four dyads(2).

## 4. Reduction of all TEN ordered positions to two kernels

For an ordered triple(R,S,T), let U5_Z be Q5 with the copair in its first two slots. Let V5_Z be the copair contraction of

`Q5(U,R,V,S,T)+Q5(R,U,V,S,T)`.

The corresponding kernels for R are UR_Z and VR_Z. Using g/f/d and (3)–(4), direct collection of the six Q5 terms gives

`U5_Z(R,S,T)= k_Z(R,[S,T])-k_Z([R,S],T)-tau_Z f(R,S,T)`
` +g(S,T)f_Z(R)+k_Z(S,[R,T])-g(R,T)f_Z(S)`,

`V5_Z(R,S,T)= tau_Z f(R,S,T)+k_Z([S,T],R)+k_Z(T,[R,S])`
` -2k_Z(R,[S,T])-k_Z(S,[R,T])`
` -g(R,T)f_Z(S)+g(R,S)f_Z(T)`.                           (5)

Collecting the seven symmetric product-trace terms in R similarly gives

`UR_Z(R,S,T)=3k_Z(S,{R,T})-3g(R,T)d_Z(S)`
` -3k_Z(R,{S,T})-2k_Z(T,{R,S})+3k_Z({R,S},T)`
` +g(S,T)d_Z(R)+tau_Z d(R,S,T)`,

`VR_Z(R,S,T)=3k_Z(S,{R,T})+3g(R,S)d_Z(T)`
` -6k_Z({R,S},T)-3tau_Z d(R,S,T)-3k_Z({S,T},R)`
` +k_Z(T,{R,S})+g(R,T)d_Z(S)`
` +2g(S,T)d_Z(R)+2k_Z(R,{S,T})`.                        (6)

Here every quantity is an ordered pair(a coefficient,b coefficient). Equations(5) and(6) are a displayed grouping, not a hidden sum over unspecified permutations.

For a target dual word(Z0,Z1,Z2,Z3), summing the original lowering positions gives

`U_Z0(Z1,Z2,Z3)+V_Z1(Z0,Z2,Z3)`
` -V_Z2(Z3,Z1,Z0)-U_Z3(Z2,Z1,Z0)`.                     (7)

To justify the two minus signs: for acted position2, the three deleted-position insertions before it equal minus the two insertions after it; reverse those two words to obtain V with the listed reversed remaining slots. For acted position3, the four insertions before it equal minus its single last insertion, whose reversal is U. Thus (7) covers all ten i<j terms, not a subset. For acted positions0/1 the one/two original insertions are precisely U/V.

The same derivation applies to Q5 and R. Finally use (1) for Q6 and the -3/-9 source normalizations.

## 5. Explicit matrix-unit and Cartan trace-path tables

The six target dual words are

`A A B C`, `A A C B`, `A B A C`,
`A B Y H`, `A B H Y`, `A C C D`.

All scalar evaluations in(5)–(6) reduce to the following short tables. B and D as INPUTS have both [x,M] and {x,M} zero. For other needed inputs:

|M|[x,M]|traceless part of{x,M}|
|---|---|---|
|A|-D|D|
|C|B|B|
|Y|K|P|
|H|-x|x/3|
|J|-x|-x/3|
|h1|-x|x|
|h2|-x|-x|

The required outer commutators are:

|Z|[Z,B]|[Z,D]|[Z,x]|[Z,K]|[Z,P]|
|---|---|---|---|---|---|
|A|-h1|0|D|A|A|
|B|0|x|0|-B|-B|
|C|0|-h2|-B|C|-C|
|D|-x|0|0|-D|D|
|Y|C|-A|-K|2Y|0|
|H|B|0|x|0|0|

For scalar pairing, `g(A,B)=g(C,D)=g(x,Y)=1`; all other unequal root pairings needed here vanish. On the diagonal matrices,

`g(h1,h1)=g(h2,h2)=2, g(h1,h2)=-1`,
`g(H,h1)=1, g(H,h2)=0, g(J,h1)=0, g(J,h2)=1`.

All further diagonal pairings follow by linearity from the displayed K,P,H,J definitions. Root/diagonal pairings vanish.

The needed commutator paths, besides antisymmetry, are

`[A,B]=-h1, [A,C]=-Y, [C,D]=-h2, [B,Y]=-C, [D,Y]=A`,

`[A,D]=[A,Y]=[B,C]=[C,Y]=0`,

`[H,A]=-A, [H,B]=B, [H,C]=[H,D]=0, [H,Y]=-Y`.

For anticommutators, only their traceless parts matter when used as inputs of k:

`{A,B}_0=J`, `{C,D}_0=-H`, `{A,C}=Y`, `{B,Y}=C`,

`{A,D}={A,Y}={B,C}=0`,

`{H,A}=A/3`, `{H,B}=B/3`, `{H,C}=-2C/3`,
`{H,D}=-2D/3`, `{H,Y}=Y/3`.

Squares of the root units occurring twice vanish. These entries follow from `Eij Ekl=delta_jk Eil` and diagonal multiplication, and are enough for EVERY kernel value below.

A concrete check of the scalar correction: for Z=A, M={A,B}=E11+E22, N=C, the uncorrected b contraction is1. But Tr(M)=2 and Tr(C[A,x])=1. Equation(3) subtracts4/3, giving **-1/3**, equal to k_A(J,C)'s b component. Omitting this correction would corrupt the symmetric-R calculations. It is not zero merely because all individual basis generators are traceless.

For reference the only nonzero f_Z/d_Z values used below are

|Z,T|f_Z(T)|d_Z(T)|
|---|---|---|
|A,C|(-3,-3)|(3,5/3)|
|C,A|(3,-3)|(3,-5/3)|
|Y,H|(3,-1)|(1,-5/3)|
|H,Y|(-3,-1)|(1,5/3)|

Also tau_Y=(6,0); the other used tau values vanish. Whenever Z=Y and(R,S,T)=(H,B,A), `f(R,S,T)=1` and `d(R,S,T)=1/3`. The other nonzero pieces in the tables follow directly from the commutator/anticommutator and pairing lists above.

## 6. COMPLETE grouped Q5 kernel evaluation

For each target row, the four contexts in(7) are as follows. Columns2 and3 below are SUBTRACTED in the final sum.

|row|context0: U|context1: V|context2: V|context3: U|
|---|---|---|---|---|
|1|A;(A,B,C)|A;(A,B,C)|B;(C,A,A)|C;(B,A,A)|
|2|A;(A,C,B)|A;(A,C,B)|C;(B,A,A)|B;(C,A,A)|
|3|A;(B,A,C)|B;(A,A,C)|A;(C,B,A)|C;(A,B,A)|
|4|A;(B,Y,H)|B;(A,Y,H)|Y;(H,B,A)|H;(Y,B,A)|
|5|A;(B,H,Y)|B;(A,H,Y)|H;(Y,B,A)|Y;(H,B,A)|
|6|A;(C,C,D)|C;(A,C,D)|C;(D,C,A)|D;(C,C,A)|

The first entry in a context is Z. Substituting the trace tables into(5) gives these ordered pairs:

|row|U5 context0|V5 context1|V5 context2|U5 context3|
|---|---|---|---|---|
|1|(-1,1)|(-1,-1)|(0,0)|(-5,5)|
|2|(6,6)|(1,1)|(0,0)|(0,2)|
|3|(1,-1)|(-2,4)|(3,5)|(3,-3)|
|4|(-2,-2)|(2,-2)|(6,-4/3)|(-4,-2)|
|5|(1,-1/3)|(-2,2)|(-1,1)|(-2,-4/3)|
|6|(-2,-2)|(3,-5)|(6,-6)|(-2,-2)|

For full traceability, the nonzero grouped additions in these cells are listed below; the zero factors are eliminated by the explicit matrix-unit paths of section5:

- Row1: `(-1,1)`; `(2,2)+(-3,-3)`; `(-1,1)+(1,-1)`; `(-1,1)+(-1,1)+(-3,3)`.
- Row2: `(1,1)+(2,2)+(3,3)`; `(-2,-2)+(3,3)`; `(-1,1)+(1,-1)+(-3,3)+(3,-3)`; `(1,1)+(-1,1)`.
- Row3: `(1,-1)`; `(1,1)+(-2,2)+(-1,1)`; `(-1,1)+(4,4)`; `(-1,1)+(1,-1)+(3,-3)`.
- Row4: `(-1,-1)+(-1,-1)`; `(-1,-1)+(2,-2)+(1,1)`; `(6,0)+(1,-1)+(1,-1)+(-2,2/3)`; `(-1,-1)+(-3,-1)`.
- Row5: `(1,-1/3)`; `(1,1)+(-1,-1)+(-2,2)`; `(-1,1)`; `(1,-1/3)+(-6,0)+(3,-1)`.
- Row6: `(-1,-1)+(-3,-3)+(-1,-1)+(3,3)`; `(-1,-1)+(4,-4)`; `(1,-1)+(2,-2)+(3,-3)`; `(-1,-1)+(-1,-1)`.

For example row1 context3 uses `-k_C(h1,A)`, `k_C(A,h1)`, and `-f_C(A)`. Their values are(-1,1),(-1,1),(-3,3), giving(-5,5). This exhibits both the ordered argument positions and the final subtraction in(7).

Adding context0+context1-context2-context3 gives the unnormalized Q5 a/b totals

`(3,-5), (7,5), (-7,1), (-2,-2/3), (2,2), (-3,1)`.       (8)

Multiplication by -3 is postponed to the final source table.

## 7. COMPLETE grouped symmetric-R kernel evaluation

Use the SAME contexts, now substituting the anticommutator trace paths into(6):

|row|UR context0|VR context1|VR context2|UR context3|
|---|---|---|---|---|
|1|(-3,-1)|(15,7)|(2,10)|(-5,5)|
|2|(-6,-2)|(-3,-13/3)|(10,-38/3)|(-4,-2)|
|3|(-3,-1)|(-2,8)|(9,13/3)|(1,13/3)|
|4|(0,-8/3)|(-2/3,2/3)|(-14/3,-16/3)|(4,14/3)|
|5|(-11/3,1/3)|(2,-2/3)|(-1,-5/3)|(-2/3,0)|
|6|(-6,-10/3)|(3,5/3)|(12,-4)|(0,0)|

The complete nonzero grouped additions, in the context order, are:

- Row1: `(-3,-1)`; `(9,5)+(6,2)`; `(-3,3)+(6,6)+(-1,1)`; `(3,-3)+(-9,5)+(-2,2)+(3,1)`.
- Row2: `(-9,-5)+(3,3)`; `(-6,-6)+(3,5/3)`; `(3,-3)+(9,-5)+(-6,-2)+(1,-1)+(3,-5/3)`; `(-3,3)+(2,-2)+(-3,-3)`.
- Row3: `(-3,-1)`; `(-3,3)+(3,3)+(-2,2)`; `(3,1)+(6,10/3)`; `(-3,3)+(-2,2)+(3,1)+(3,-5/3)`.
- Row4: `(1,1)+(2,-2/3)+(-3,-3)`; `(-1,-1)+(1,1)+(-2/3,2/3)`; `(-6,0)+(-3,-1)+(1/3,-1/3)+(2,-10/3)+(2,-2/3)`; `(3,3)+(1,5/3)`.
- Row5: `(-3,1)+(-2/3,-2/3)`; `(2,-2)+(1,1)+(-1/3,-1/3)+(-2/3,2/3)`; `(-6,-6)+(3,1)+(2,10/3)`; `(-3,1)+(-2/3,2/3)+(1,-5/3)+(2,0)`.
- Row6: `(3,3)+(-9,-5)+(-3,-3)+(3,5/3)`; `(-6,6)+(3,-1)+(6,-10/3)`; `(9,-5)+(6,-2)+(-3,3)`; `(-3,-3)+(3,3)`.

This is a direct evaluation of the missing Jordan/commutator part, not an assumption that the symmetric sector vanishes. In particular the thirds in rows4–5 come from the literal trace-dual Cartan H/J/P and the essential first-input scalar projection.

Again summing context0+context1-context2-context3 gives

`(15,-9), (-15,25/3), (-15,-5/3),`
`(0,-4/3), (0,4/3), (-15,7/3)`.                         (9)

For a useful explicit scale check, row1 has `(Q5+R)/2=((3,-5)+(15,-9))/2=(9,-7)`. Its sourceS6 factor is -9, not -3.

## 8. Final24 scalars and literal comparison

From(8), multiply by -3 for S5. From(8)–(9), average first and multiply by -9 for S6, using(1). The resulting a/b pairs are:

|detector|S5:(a,b)|S6:(a,b)|
|---|---|---|
|w1|(-9,15)|(-81,63)|
|w2|(-21,-15)|(36,-60)|
|w3|(21,-3)|(99,3)|
|w4|(6,2)|(9,9)|
|w5|(-6,-6)|(-9,-15)|
|w6|(9,-3)|(81,-15)|

These are the24 scalars that remained unproved in my v35-C. Their derivation is the trace reductions and grouped sums above. Direct comparison with Q102–107 finds **no mismatch**.

For clarity, adjoining ONLY the previously written-derived central coefficients from v35-C gives these complete affine columns:

|row|M_i5|M_i6|
|---|---|---|
|1|-9a+15b|-81a+63b+54c|
|2|-21a-15b+12c|36a-60b-36c|
|3|21a-3b-6c|99a+3b-36c|
|4|6a+2b-6c|9a+9b|
|5|-6a-6b+6c|-9a-15b-6c|
|6|9a-3b-6c|81a-15b-36c|

This completes the literal tensor-source identity for columns5/6, with the original central level action preserved. It does not use an actual-source dimension or a determinant as a premise for those entries.

## 9. Gate disposition

The precise own-reviewer obligation is now closed: the prior12 central scalars plus the new24 a/b scalars give all36 requested scalar coefficients for the two product-trace columns. There are **no remaining NOT_RECONSTRUCTED numerical identities inside this24-scalar slice**.

Other detector columns and the full determinant remain separate reviews; I do not infer their verdicts, their parent composition, full invariant injectivity, source-basis independence or the actual3-to5 quotient theorem. The selected R2 source-image result retains its own return and imports. The original sevenD3 ranks, generalF5, B4/H13 authentication and broad Serre problem are outside this scope.

This is a complete written column reconstruction, not executable verification, a proof-assistant check, configured dual-family/human acceptance or novelty clearance. Parent disposition remains separate. All earlier files and the historical NOT_RECONSTRUCTED return remain immutable.
