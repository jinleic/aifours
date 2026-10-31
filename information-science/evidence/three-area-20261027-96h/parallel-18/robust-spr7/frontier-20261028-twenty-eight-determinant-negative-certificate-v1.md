# A negative septic witness has a fixed-size all-integer certificate: 28 Hurwitz determinants and 8 pairing sums

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 18:16:44 PDT 2026**. **WRITTEN author-unreviewed candidate.** This supplies an explicit finite exact eligibility check for the hypothetical all-integer obstruction normal form. No determinant search or negative witness was run or found.

## 1. The exact finite criterion

Import the COMPLETE `frontier-20261028-all-integer-eight-frequency-certificate-v1.md`, SHA256 `ac57739a9e005bde9ea97deb566a093ee69645d6cd0ed0a334033f331f2690e3`, and its full cited original-box, positive-numerator, support-8 and strict-rational completeness chain. They remain author-unreviewed candidates. The actual registered target is every monic degree-seven independent closed interval box with every member strictly Hurwitz and one unrestricted exact-degree-seven numerator.

**Theorem.** A counterexample to this original septic target exists IFF a finite tuple of POSITIVE INTEGERS satisfies ALL of the following:

1. Fourteen integers `l_j<u_j`, j=0,...,6, define one monic independent coefficient box. The four actual parity corners are the `E_-/E_+` and `O_-/O_+` combinations displayed below.
2. For each of those four corners, every one of its **seven leading Hurwitz determinants is >0**: 28 explicit integer determinant inequalities in total.
3. Eight pairwise distinct positive integer frequencies `w_l`, eight positive integer weights `N_l`, and eight corner indices i_l in `{1,2,3,4}` satisfy the eight strict INTEGER coefficient-sum inequalities `C_k<0`, k=0,...,7, printed in §4.

No predicate quantifies over continuum many denominators or frequencies once this tuple is supplied. The nontrivial assertion that the 28 determinants prove stability of EVERY box member is proved for this exact monic box in §§2–3. Its classical general analogue is Kharitonov's theorem; no novelty or independent discovery is claimed.

## 2. Four corner polynomials and the edge lemma

For t>=0 write `a(i sqrt(t))=E_a(t)+i sqrt(t) O_a(t)`. Independent coefficient intervals give

`E_-=l_0-u_2 t+l_4 t^2-u_6 t^3`,
`E_+=u_0-l_2 t+u_4 t^2-l_6 t^3`,
`O_-=l_1-u_3 t+l_5 t^2-t^3`,
`O_+=u_1-l_3 t+u_5 t^2-t^3`.

The four displayed combinations `(E_-,O_-)`, `(E_-,O_+)`, `(E_+,O_-)`, `(E_+,O_+)` are polynomials belonging to K; signs in this definition are evaluation extrema, not coefficientwise extrema. At t=0 E ranges over `[l_0,u_0]` and the odd term vanishes.

**Edge lemma.** Let two real monic Hurwitz septics share their entire E part, or share their entire O part. Then their entire coefficient segment is Hurwitz.

For any actual monic Hurwitz septic, factor its roots as `-alpha+i beta` with alpha>0. The continuous phase of a(iw) starts at0, has strictly positive derivative `sum alpha/[alpha^2+(w-beta)^2]`, and tends to `7pi/2`. Thus its E roots and O roots are simple positive cubics, strictly interlaced `e1<o1<e2<o2<e3<o3`. At E roots the O signs are `(+,-,+)`; at O roots the E signs are `(-,+,-)`. Its constant coefficient is positive.

If two endpoints share E, any imaginary-axis zero of their convex segment at t>0 would require this fixed E to vanish and the interpolated O to vanish. At each E root the two endpoint O values have the SAME listed nonzero sign, so their convex combination cannot vanish. At t=0 the shared constant is positive. With shared O, the analogous assertion holds at each O root, and at t=0 the interpolated constants are positive. The segment remains monic degree seven, so root continuity carries the initial Hurwitz root count along it without an imaginary-axis crossing. This proves the edge lemma, including repeated coefficients and degenerate endpoint segments.

## 3. Four corners are necessary and sufficient for the entire box

Necessity is immediate since each corner is an actual member. For sufficiency suppose all four corners are Hurwitz. The two edges with E fixed and the two with O fixed are Hurwitz by §2. In particular their constants give `l_0>0`.

Assume for contradiction that some actual box member has an imaginary-axis zero at positive t0. Then the value rectangle contains the origin:

`E_-(t0)<=0<=E_+(t0)` and `O_-(t0)<=0<=O_+(t0)`.

The set of t in `[0,t0]` satisfying both closed interval conditions is nonempty and closed. Let t* be its least member. Since `E_-(0)=l_0>0`, continuity makes t*>0. If zero lay strictly inside BOTH value intervals at t*, it would also do so at a slightly smaller positive t, contradicting minimality. Thus one of `E_-(t*),E_+(t*),O_-(t*),O_+(t*)` is zero.

If, say, E_-(t*)=0, then `O_-(t*)<=0<=O_+(t*)`; some convex interpolation of the two fixed-E_- corner odd parts has O(t*)=0. This is an actual polynomial on an E-fixed edge, which §2 says is Hurwitz — a contradiction. The other three endpoint equalities are identical. Hence no K member has a positive-frequency imaginary root; at zero every member has a_0>=l_0>0.

Finally K is convex and monic fixed degree. A straight segment from a Hurwitz actual corner to any actual member stays in K. Its root count cannot change without an imaginary-axis crossing, which was just excluded. Thus every actual member is Hurwitz. This proves the four-corner stability statement in the exact original model, including zero widths and repeated corners.

## 4. The actual 28 determinants and 8 integer sums

For a corner `a=s^7+sum_(j=0..6)a_j s^j`, write `c_0=1`, `c_i=a_(7-i)` for i=1,...,7, and c_i=0 outside 0,...,7. Form the integer Hurwitz matrix `H_(p,q)=c_(2q-p)` for p,q=1,...,7. Let D_k be its leading kxk determinant. The ordinary strict Routh–Hurwitz criterion says this corner is strictly Hurwitz IFF **all D_k>0**, k=1,...,7. By §3, all 28 tests across the four corners are equivalent to the actual full-box Hurwitz hypothesis. Repeated determinants in a degenerate case may be checked repeatedly; the integer normal form requires positive widths but can have coincident numeric determinant values.

For the chosen eight actual corners, w_l and N_l, calculate for each k=0,...,7

`C_k = sum_(l=1..8) N_l sum_(0<=j<=7; j+k even)`
`       [(-1)^((k-j)/2) a_(i_l,j) w_l^(j+k)]`.

These eight expressions are integers. If they are strictly negative, then any common exact-degree numerator b, normalized to positive leading coefficient, has b_k>0 by the predecessor's direct Hurwitz homotopy; the weighted sum of its eight actual pairings is `sum C_k b_k<0`. Yet every pairing is strictly positive under the original SPR condition, contradiction. Thus any tuple passing 1–3 of §1 is a genuine original negative witness.

For the converse, the full imported all-integer normal form constructs such a tuple from ANY original counterexample; §3 ensures its eligibility is exactly detected by the 28 determinants. Therefore the finite criterion has no false positive and no false negative **conditional on the complete cited chain**.

## 5. Verification boundary and original residual

The fixed-size checker is specified as exact integer determinant and sign arithmetic; no code, determinant replay, finite search, LP, solver or numeric instance was run. The argument needs independent review of every imported source and of the edge lemma, first-contact construction, root-count continuity and determinant conventions. It gives a complete ONE-SIDED certificate family, not a bound on witness integer sizes, an executable result, or a guarantee of terminating when no counterexample exists.

No actual negative box, universal positive theorem, numerical optimum, novelty, formal/kernel/human/configured-family verification or changed historical process status is claimed. The original shared-numerator sign remains OPEN.

**END.**
