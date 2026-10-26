# v30-B written review: literal x1111 PPT input and Schmidt-two candidate

Actual returned `/bin/date` before writing: **Sun Oct 25 04:27:14 PDT 2026**. Reviewer MathResearch96h-2. Strictly WRITTEN reconstruction; no scientific eval/interpreter/arithmetic program, enumeration, replay, solver, external model or nested agent. Metadata clocks/hashes/source reads only. Parent erratum v7 is mandatory.

## 1. Source binding, coverage and overall verdict

Read ALL343 LF of `peer-review-wave-v30-ppt-x1111-schmidt-two-sources-v1.md`, SHA256 `73551a4f49b1757443a763df1aae893e9052e816b2259d852775234b22f5b603`. Its sole truncated line, packet LF21/source markdown LF13, was explicitly reread raw. Both complete source bodies were supplied: markdown LF1–241 and JSON LF1–88. Fresh metadata hashes match manifest pins:

- Markdown: `2d38c9947d4c4ef87149f694dbc277e915eb0e706ec83656f6c626d7c6c76e56`.
- JSON: `b2d8e13a63fa4be2a2c6deead8b2b04921dd1d92f7f75e5b9d6ea50794ebe761`.

Also read the frozen N4 proposal's explicit target at LF175–181, SHA256 `de428a73ccca38fdd9066c9a64f319f8da8c2d60c238ed56df2ae5886ad15f6d`. Its target exactly matches the literal R here; no separate paper-access or whole-proposal reconstruction is claimed.

**Overall: PARTIAL WRITTEN RECONSTRUCTION; SN=2 NOT ACCEPTED.** No false equation or correctness defect is established. There is **one MAJOR, load-bearing acceptance gap: the full weighted21-pair identity is NOT_RECONSTRUCTED**. This is not a finding that the table is wrong. It is exactly the unmet gate specified by v30-B. All positive individual weights, all21 rank-two vector conditions, the analytic eight-vector assembly, literal PPT identity, entanglement lower bound and generic-x qualitative barrier reconstruct below. The historical unadmitted matrix-sum observation is NOT substituted for the missing written summation.

FATAL:0. Established author correctness MAJOR:0. MINOR:0. Unmet load-bearing reconstruction:1 MAJOR. At the accepted analytic boundaries below the verdict is0F/0M/0m. Same-harness written review only; no finite execution, formal/kernel, cross-vendor, human or novelty acceptance.

## 2. B0 — literal target, trace and PPT Gram identity:0F/0M/0m

Sources: markdown LF19–47, JSON LF8–36; frozen proposal LF175–181.

The nine literal source kets are exactly the proposal's a,b,c and its six weighted non-core kets at x1111. Their squared norms give the displayed trace49, so rho=R/49 is a density matrix. Every coefficient in the defining Gram sum is positive.

Here is a direct reconstruction of the partial-transpose identity, without a16-by16 replay. Write `S(v,w)=v w*+w v*` and l=30+31+32+33. The partial transpose of the three core projectors is

`P00+P11+P22+P01+P12+P10+P21`

`+S(01,10)+S(02,20)+S(12,21)+S(02,11)-S(11,20)`.

The first six Gram terms in markdown LF40–41 produce precisely this operator PLUS `3P02+3P20`: expand P(02+11-20) and2P(02+20); the 02/20 cross coefficient becomes -1+2=1 and the 02,20 diagonal coefficients become3 each. These extra diagonal terms are supplied by the non-core part, as follows.

Since d=02+l, its partial transpose is `P02+P(l)+S(h,32)`. Since e=20+33, its partial transpose is `P20+P33+S(23,30)`. Combining the remaining f,g,h,j projectors yields exactly

`3P02+3P20+3P(32+h)+3P(30+23)+3P(l)+3P33`.

Thus the source's full positive Gram identity for R^Gamma is correct, with no solver-status premise. The rank observations can also be recovered without elimination: the nine original Gram kets are independent by successively selecting their unique coordinates03,23,31,20,30,32,22,12,21; the ten partial-transpose Gram kets are independent by selecting31,23,03,33,00,22,11,02,10,21. Therefore the stated ranks9 and10 follow. The JSON LDL pivot LIST itself was not reconstructed and is not needed for positivity or rank.

## 3. B1 — complex eight-vector rank and averaging:0F/0M/0m

Sources: markdown LF51–99; JSON LF37–43.

For delta=2i/3, the displayed gamma has square -5i/12 and modulus squared5/12. Hence beta²+chi²=-5i/6=delta+delta^(-1), independent of the two independent signs; conjugation covers the other delta. The fourth matrix row is delta times the SECOND row (row index1), as printed. The upper3-by3 determinant is `1-delta(beta²+chi²)+delta²=0`, while the upper-left2-by2 minor is nonzero since |beta chi|=5/12<1. Every one of the eight actual complex kets therefore has rank exactly2.

The complete averaging identity becomes transparent on writing

`psi=a+beta b+chi c+delta v+delta chi f+delta beta g`,

`v=d-e-f-g`.

The independent beta/chi signs kill all cross covariances except possible b/g and c/f terms. Those two are proportional to `(5/12) E(conj(delta))`, hence vanish upon the equal delta/conjugate-delta average. The a/v covariance also vanishes because E(delta)=0. The surviving variances are1 on a,5/12 on b,c,4/9 on v, and(4/9)(5/12)=5/27 on f,g. This proves the full operator identity(2), not just selected entries. The source's alternative f/g covariance explanation is consistent with this regrouping.

## 4. B2 — exact two-product residual representation:0F/0M/0m

Sources: markdown LF103–140; JSON LF45–57 and LF62–82.

Expanding the first product in source(4) gives exactly `r|0,x>+p|0,2>+p|3,x>+u|3,2>`. Expanding the second gives `t|3,0>+q|3,3>+q|2,0>+s|2,3>`. Thus the displayed coordinate map is exact, with order(p,q,t,u,r,s) retained. A complex symmetric2-by2 matrix of rank≤1 is a scalar times v v^T, including its zero and axis cases. Hence ru=p² and ts=q² supply the written rank≤2 certificate; no real-only argument or division by a possibly zero component is required.

For completeness the following table reconstructs ALL21 literal JSON vectors. The first array is `(r,p,u)=(1,z,z²)` unless marked ZERO. The second is `(t,q,s)=epsilon(1,w,w²)` unless marked ZERO. Each row index refers to consecutive JSON LF62–82. Substitution reproduces the actual rational/imaginary entries, not a freely chosen replacement vector.

| Row | z or first array | epsilon | w or second array |
|---:|---|---|---|
|1|-3/4|—|ZERO|
|2|(3+4i)/5|1|(-3+4i)/5|
|3|ZERO|1|5/4|
|4|i|1|5/4|
|5|(3+4i)/5|—|ZERO|
|6|-2/3|—|ZERO|
|7|ZERO|1|4/3|
|8|-2/3|-1|(-3+4i)/5|
|9|(3+4i)/5|i|(-3-4i)/5|
|10|(3+4i)/5|1|(-3-4i)/5|
|11|-2/3|-1|3/2|
|12|i|-1|-i|
|13|5/4|1|5/4|
|14|-4/5|—|ZERO|
|15|(3+4i)/5|-i|i|
|16|(3+4i)/5|-i|-4/5|
|17|-4/5|-1|i|
|18|5/4|—|ZERO|
|19|-4/5|i|(-3+4i)/5|
|20|i|1|(-3+4i)/5|
|21|-4/5|-1|5/4|

For example row9 has q=(4-3i)/5 and s=(-24-7i)/25: multiplying the stated w by i and w² by i gives those exact entries. Row19 similarly gives q=(-4-3i)/5 and s=(24-7i)/25. Row16 gives q=4i/5 and s=-16i/25. These are the easy places to lose a conjugation/sign; they agree.

All21 listed coefficient_Re_yy_star numerators and denominators in JSON LF62–82 are strictly positive integers. Thus the weights themselves are individually positive. No weighted matrix-sum claim follows merely from those facts.

## 5. B3 — residual matrix and half-weight convention:0F/0M/0m

Sources: markdown LF142–166, JSON LF45–60.

Subtracting the independently reconstructed eight-vector average from R leaves exactly(7/12)[P(b)+P(c)] and

`F[3I6-(4/9)zz^T-(5/27)(E_tt+E_uu)]F*`,

where z=(1,-1,-1,-1,0,0) in the declared coefficient order. This directly reconstructs all displayed entries of M: its first two diagonal entries are23/9, its next two64/27, last two3; the ±4/9 off-diagonals have precisely the signs of -zz^T. The displayed trace428/27 agrees.

For complex y, the ENTRYWISE real part satisfies

`Re(y y*)=(P(y)+P(conj(y)))/2`.

Because F is real in this chart, conjugation commutes with F. Therefore the t field is the coefficient of Re(yy*), and the actual two pure-projector weights are t/2, including when a real y duplicates its own conjugate. The convention is correct. There is no missing factor2.

## 6. B4 — complete21-pair matrix identity:MAJOR NOT_RECONSTRUCTED gate

Load-bearing claim: markdown LF159–180, equation(6) at LF162–163; JSON LF59–60 and all actual coefficients LF62–82.

I read every coefficient/vector and reconstructed individual positivity and rank-two parametrization above. I did NOT complete the written weighted sum of all21 outer products to all entries of M. In particular I have not derived all six diagonal sums and fifteen real off-diagonal sums from those large rational coefficients. The historical conic elimination and entrywise-comparison booleans are unadmitted observations and are NOT premises for this review. No arithmetic program or replay is authorized or was launched to close the gap.

Consequently equation(6) is **NOT_RECONSTRUCTED**, not refuted. It is a MAJOR acceptance gate because the final operator decomposition(7), the normalized convex weights and the upper bound SN≤2 all require it. The absence of a new algebraic-number16-by16 replay is not itself the issue: the eight-vector operator identity has a complete written proof. The exact unresolved finite identity is the rational6-by6 residual sum, with its precise half-weight convention.

Conditional assembly is sound: IF(6) holds, every term of(7) has rank≤2, all weights are positive, there are at most52 terms before merging, and normalizing each nonzero vector after dividing by49 gives weights summing to1 by trace. This conditional conclusion must NOT be restated as accepted SN=2.

## 7. B5 — matching entanglement lower bound:0F/0M/0m

Source: markdown LF182–198.

The local Alice projection has exactly the displayed range matrices. For a rank-one matrix, a nonzero Bob3 column(H,0,J)^T forces the Alice1 component to vanish and hence the middle row and A vanish. If that column is zero, H=J=0; the two displayed minors are A²-BC and A²+BC. Their simultaneous vanishing over C forces A=0. Therefore every product vector in the projected range has11 coefficient0.

A pure summand of a positive separable operator must lie in its range: every vector in the operator's kernel has zero nonnegative expectation in each summand. Thus separability would force the projected11 diagonal entry0. The actual entry is1, supplied only by P(a). Contradiction. The projected state is entangled; local projection cannot create entanglement from a separable input. Hence **the literal PPT input has SN≥2**, independently of equation(6). The proof does not confuse the11 functional with orthogonality to a.

## 8. B6 — generic-x qualitative barrier:0F/0M/0m

Source: markdown LF200–226.

When x3≠0, choose tau²x3=-1. Expanding the stated vector gives rows(1,0,tau,0), (0,1,0,0), (-tau x3,0,1,0), and(0,tau x1,0,0). The last two are exactly -tau x3 times row0 and tau x1 times row1. When x3=0 the second proposed vector has rows(1,0,1,0), (1,1,0,0), their difference, and x1 times the second row. Both have rank≤2 and a-coordinate1 for arbitrary complex x in their respective cases.

The other eight source generators already have rank≤2. Replacing a by the displayed a-plus-others vector leaves their total span unchanged, whether or not the generators have dependencies. The a coefficient remains well defined through the unique22 coordinate. Thus every chart range is spanned by rank≤2 vectors and contains one with nonzero a coordinate. A witness equal on this range only to a negative multiple of squared a coordinate, plus a penalty vanishing on the range, fails two-block-positivity on that explicit vector. No quantitative Schmidt-two conclusion follows from this qualitative span statement, and no general witness/extension/P44 no-go is inferred.

## 9. Final disposition and exact unresolved obligations

Accepted by this WRITTEN review at the stated scope: literal target binding, positivity/trace/PPT Gram identity, analytic ranks9/10, all eight complex rank-two vectors and their full averaging identity, exact residual map and all21 individual rank-two conditions/positive weights, residual M entries and half-weight convention, entanglement lower bound, and generic-x qualitative-nullspace barrier.

**NOT accepted:** the complete21-pair operator identity, SN≤2 or SN=2 for x1111, any theorem retiring the N4 input as an SN3 candidate on the strength of this review, or P44. Equation(6) remains the explicit load-bearing finite obligation. The independently reconstructed entangled/PPT lower statement does not fill that upper-bound gap. N4 remains UNKNOWN/incomplete with historical exit unestablished; no retry, recovered run verdict, certificate replay or GO. Independent finite execution/formal/novelty gates remain unperformed.
