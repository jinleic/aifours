# v82-A — actual two-support face rigidity and its noncircular detection corollary

MathSemigroup-2, serial cross-domain written reviewer. Actual clock observed BEFORE this write: **Sun Oct 25 11:14:36 PDT 2026** (`/bin/date`), an observation bound, not an invented completion timestamp. **WRITTEN mathematical verdict: 0 FATAL / 0 MAJOR / 0 MINOR defects found at the complete157LF main theorem plus31LF mandatory addendum scope.** No scientific interpreter/program/eval, symbolic or numerical computation, solver, enumeration, certificate replay, finite-witness admission or evaluated threshold was used. Inherited process findings remain permanent.

## 1. Actual exposure, checkpoint and complete source coverage

Fresh exposure ACK `peer-review-ppt-actual-face-rigidity-ack-v1.json` was written at actual **Sun Oct 25 11:10:00 PDT 2026**, BEFORE opening either new proof body. This is SERIAL after my actually returned v78-A review, `peer-review-ppt-anisotropic-background-v1.md`, SHA256 `42d010c964af3d8b8f53120f56d8f8963150b3fa74f81c411dd47feca64de7c1`,219LF. Prior v43/v48/v52/v55 PPT exposure and v75 TC-zero exposure remain disclosed. It is not blind or different-model-family review. The v75 correction remains that the older v67-B reviewer was MathOlson-2-2, not me.

The actual own-primary checkpoint preceded this temporary review: `primary-102319-typed-local-law-checkpoint-v1.json`, SHA256 `60f86e113433657fff5816609b9bf7d9ac18c2d3f743fe91ac0d3d8c1acc464a`, observed **Sun Oct 25 11:08:56 PDT 2026**. It records the new ALL-(M) plus local-corner-law conservativity theorem and the still-unproved off-path square-excursion/SEP gap. This review does not substitute for that original embedding task.

I read EVERY physical LF1–590 of the sole literal packet, in complete coverage1–173,174–368,369–590, INCLUDING all endings. S1/v9 was read FIRST, S2/v10 SECOND, S3/v11 THIRD before the new main body. Complete supplied bodies are main157LF, addendum31LF, baseline232LF and parent26LF. No source-body coverage is inferred from matching hashes.

Observed live metadata bindings:

- Manifest `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v82.json`: `0220a82ba517441657f12a69a2dad561df4cab88a42e08619c252dda852f8ad8`.
- Receipt `peer-review-wave-eighteen-v82-packet-receipt-v1.json`: `bc732f8961480452a61822dde3785bd49173054a225849680d23fdbe784ecd00`.
- Part `peer-review-wave-v82-v82-A-part1-v1.md`: `28e0f216f92e457e574fb78cfb57a7ef7a5ba54ce80889353183e920823ed893`.
- NEW main `physics/evidence/three-area-20261023-96h/parallel-18/ppt-schmidt44/anisotropic-Weyl-actual-PPT-face-rigidity-v1.md`: `63b7afafa63e5d8aca4652b25cb493770e7165adb6031a4af24bbcbeef2ec8c7`.
- Mandatory additive `anisotropic-Weyl-actual-PPT-face-rigidity-ADDENDUM-1-corollary-v1.md` in the same author root: `f926c30e4bef2eebf2b3e1db262a94d2bca41679265694f1283b0a24d8029f72`.
- Complete baseline `four-Weyl-rectangle-consolidated-obstruction-v1.md` there: `eb1ed1c5aba2bb444a817b48a39ff3d7206c1aacc65421cca7073cffe64a5e02`.
- Parent `institute/runs/three-area-2026-10-23-96h/ppt-anisotropic-background-parent-v1.md`: `d5b19a88b067277bfc6c9f6275e68b21a942eb5bbe4dd21f7117be52ed136119`.

Mandatory full corrections retained: v9 `b7c92143cda18c88c7c56017859ab3c7f08fa92ef3d00fd85ba29f41ac258034`; v10 `d61acbf77fefa3a8d55d0cf74e9ebe0b680edb28d273f5b22255d09cbd66aa62`; v11 `3ce29e3c49d4789106431978152ffab28a3d14402a748ec3828c825f31c4d9e7`. No clock/coverage/freeze correction is erased or backdated. The frozen author's word “pending” for the older anisotropic gate is historical at its own writing; that gate has now actually returned and the supplied parent records it. The NEW proof chain below does not depend on that older32-term or two-level theorem anyway.

## 2. Exact geometry and all eight physical phase orientations

Use `vec C=sum C_ij|i,j>`, Bob transpose Gamma, `P(v)=|v><v|`, indices modulo4, `Z e_j=i^j e_j`, `X e_j=e_(j+1)`. Q is the rank4 orthogonal projector onto the normalized I,Z,X,ZX rays. H projects onto product differences0,1; L=I-H projects onto differences2,3. Q<=H. Put

`R*=Q+L/4`, `Tr R*=4+8/4=6`.

Its range is Ran Q direct-sum Ran L, of dimension12. This actual range is not all of H+L.

The needed PT table is recovered from the basis action, not a rounded spectrum:

`4Q^Gamma|r,s>=(1+i^(s-r))|s,r>+(1+i^(s-r+1))|s+1,r-1>`.

Both destinations retain total index tau=r+s. For high difference0, h=(r,r), this gives diagonal2 and coefficient1+i from h to its low partner (r+1,r-1), so the H-FIRST UPPER coefficient is u=1-i. For high difference1, h=(r,r-1), the diagonal is2 and the coefficient to low partner (r-1,r) is1-i, so the H-first upper coefficient is u=1+i. These yield all eight physical pairs:

|tau|high h|low l|upper u in H/L order|
|---:|---|---|---|
|0|00|13|1-i|
|2|11|20|1-i|
|0|22|31|1-i|
|2|33|02|1-i|
|3|03|30|1+i|
|1|10|01|1+i|
|3|21|12|1+i|
|1|32|23|1+i|

Every product basis ket appears exactly once. Substituting in the displayed action shows no destination outside a listed pair; the unused coefficient is zero. Thus all eight H/L blocks of Q^Gamma are `(1/4)[2,u;bar(u),0]`, |u|^2=2. Adding L/4 gives

`(R*)^Gamma_block=(1/4)[2,u;bar(u),1]=(1/4)P((u,1))`.

All eight blocks are PSD rank1, on disjoint pairs. In particular R* is PPT, and its PT rank is8. The physical orientation u versus bar(u) is essential below.

## 3. All complex Z-twirled blocks and the FIRST actual support inclusion

Let V=Z tensor bar(Z). Its eigenvalue on |r,r-q> is i^q. A Hermitian V-invariant R therefore has exactly four arbitrary COMPLEX Hermitian4-by4 difference blocks:

`R=sum_(q,r,s) R^(q)_rs |r,r-q><s,s-q|`.

There are no cross-q entries, but no entry inside a block has been discarded. Bob transpose sends an entry to `|r,s-q><s,r-q|`, so in total-index sector tau its exact entry is

`S^(tau)_rs=R^(r+s-tau)_rs`.

This includes every PT matrix element; r+s-tau is symmetric in r,s, preserving Hermiticity.

Let F have row r `(1,i^r)/2`. Its two columns are orthonormal since sum i^r=0 and each column has squared norm1. The restriction of Q on BOTH high difference blocks q0,q1 is B=FF*, with `B_rs=(1+i^(r-s))/4`; Q has no low block. If Ran R subset Ran R*, Hermiticity gives two-sided support by the orthogonal range projection. Hence exactly

`R^(0)=F A F*`, `R^(1)=F C F*`,

where `A=[a,z;bar(z),b]`, `C=[c,w;bar(w),d]`, a,b,c,d real, z,w arbitrary complex. The two low blocks remain arbitrary Hermitian at this stage. This step assumes neither positivity, diagonal A/C nor J invariance.

## 4. The SECOND actual support inclusion and all eight within-pair equations

Since Ran R^Gamma is included in the direct sum of the eight lines span(u,1), Hermiticity gives support on BOTH sides. Within a total-index sector with two physical pairs one can write S=U K U*, where the two columns of U are the disjointly supported pair vectors (u,1), and K is an arbitrary Hermitian2-by2 coefficient matrix. Thus, for each pair, not merely for a PSD matrix,

`S_hl=u S_ll`, `S_hh=2S_ll`, `S_hl=(u/2)S_hh`.

Also every high row is u times its low-partner row and every high column bar(u) times its partner column, INCLUDING cross-pair entries. The K off-diagonal is not set to zero prematurely.

For the first four physical pairs in the preceding table, h=(r,r),l=(r+1,r-1), tau=2r. The shuffle makes S_hl=R^(1)_(r,r+1) and S_hh=R^(0)_rr. For the last four, h=(r,r-1),l=(r-1,r), tau=2r-1; it makes S_hl=R^(0)_(r,r-1), S_hh=R^(1)_rr. Therefore ALL eight relations are exactly

`R^(1)_(r,r+1)=(1-i)R^(0)_rr/2`,

`R^(0)_(r,r-1)=(1+i)R^(1)_rr/2`, r=0,1,2,3.

These equations use the actual00/13,11/20,22/31,33/02 and03/30,10/01,21/12,32/23 pairings, not an arbitrarily chosen phase convention.

## 5. Complex high coefficients force z=w=0 and A=C=tI

Direct expansion of F A F* gives

`4R^(0)_rr=a+b+z i^(-r)+bar(z)i^r`,

`4R^(0)_(r,r-1)=a+i b+i z i^(-r)+bar(z)i^r`.

Similarly

`4R^(1)_(r,r+1)=c-i d-i w i^(-r)+bar(w)i^r`,

`4R^(1)_rr=c+d+w i^(-r)+bar(w)i^r`.

The characters1,i^r,i^(-r) are linearly independent on C4 (their pairwise character sums vanish). Comparing ALL coefficients in the first four within-pair equations yields

`c=d=(a+b)/2`, `-i w=(1-i)z/2`, hence `w=(1+i)z/2`,

with the conjugate coefficient giving the same relation. Comparing the other four gives

`a=b=(c+d)/2`, `i z=(1+i)w/2`, hence `z=(1-i)w/2`.

Combining gives z=((1-i)(1+i)/4)z=z/2, so z=w=0. The real constant equations then force a=b=c=d=t. Therefore R^(0)=R^(1)=tB with real t. There is no hidden i^(2r) coefficient: the displayed expansions list all products of the two F characters. Neither trace constraints nor prior symmetry nor positive weights entered this conclusion.

## 6. EVERY low-block and cross-pair entry, including the zero boundary

In a total-index sector the two low row indices differ by2. For even tau their cross low/low entry, through the shuffle, belongs to R^(0); for odd tau it belongs to R^(1). One can see this directly: a low index satisfies 2r-tau=2 if tau is even and =3 if tau is odd, so at s=r+2 the block index r+s-tau is0 or1 respectively. In either case the entry is t B_(r,r+2)=0.

But in the U K U* description, each low coordinate of its pair vector is1. Hence that low/low cross entry IS K_12. Its vanishing makes every cross-pair matrix element vanish, including high/high and the two cross high/low orientations. Hermiticity gives the reverse entries as well. No unexplained low-block residual survives.

Every high diagonal is t/2; the within-pair relation S_hh=2S_ll therefore sets every low diagonal to t/4. For completeness, take ANY off-diagonal entry R^(q)_rs with q=2 or3. Put Delta=r-s and tau=r+s-q. The corresponding two S basis differences are q+Delta and q-Delta. If Delta=1 or3, one is H and the other L; it is a CROSS-pair entry, since every WITHIN-pair off-diagonal was already identified as q0 orq1. If Delta=2, both differences are high (0 for q2,1 for q3), so this is a cross-pair high/high entry. All of them vanish. Thus exactly

`R^(2)=R^(3)=(t/4)I4`.

The complete operator is R=t(Q+L/4)=tR*. This proves the claimed LINEAR Hermitian rigidity, not just a PSD subcase. If R>=0 then t>=0 from any diagonal. If t=0, ALL four blocks are zero. If R has trace1, then6t=1 and t=1/6. Hence the normalized V-invariant PPT face is the single state R*/6. Nothing here classifies the full untwirled face as one-dimensional.

## 7. Lossless twirling of an UNT WIRLED state preserves BOTH actual support faces

Suppose an actual untwirled PPT R satisfies both range inclusions. R* is V-invariant: Q's four ray projectors have definite differences and L is diagonal. Therefore Ran R* is stable under V. Also

`(V R V*)^Gamma=(Z tensor Z)R^Gamma(Z* tensor Z*)`.

The same covariance applied to R* shows (R*)^Gamma and its range invariant under Z tensor Z. Conjugating the first support inclusion by V and the second by this PT unitary preserves them; averaging their four conjugates preserves both subspace inclusions. It also preserves positivity, PPT and trace. The twirled state is consequently tR*, t>=0 (t=1/6 for trace1).

Every product-diagonal D commutes with V, and Q is fixed by V, so Tr((D-Q)R) is EXACTLY unchanged by this four-twirl. This is valid even when the ORIGINAL target is not J-invariant. It is not a license to J-twirl a general target. Strict detection therefore cannot occur while BOTH actual support inclusions hold, by the direct next argument; leaving at least ONE is necessary. It is not asserted that every possible detector must leave both.

## 8. Mandatory addendum: the no-negative corollary is independent of the old32-term/two-level gate

J=(X tensor I)SWAP sends a coefficient matrix C to X C^T, preserving Schmidt rank, and sends I,Z,X,ZX to X,XZ=-iZX,I,Z. Thus Q and R* are fixed. Its product-basis action (i,j)->(j+1,i) has J^2 shifting both indices by1; it interchanges differences0/1 and2/3. Its two length8 orbits are exactly H,L.

For a universally complex rank-two-nonnegative W(D)=D-Q, every J-conjugate is likewise rank-two nonnegative. Averaging gives `Wbar=aH+bL-Q`, with the actual orbit averages of the SAME D. As R* is actually J-invariant, Tr(W(D)R*)=Tr(WbarR*).

Now use ONLY the actual matrix `C=(I+Z)+sqrt2(E13+E31)`. The isolated00entry2 gives rank1, the opposite block has determinant(1+i)(1-i)-2=0 and rank1, and the2row/column vanishes. Hence rank C=2. Its H norm squared is8, L norm squared4; the H part is in Ran Q and L orthogonal to Q, so its Q expectation is8. The assumed universal rank-two nonnegativity of Wbar implies

`8a+4b-8>=0`.

On the other hand direct tracing, using QL=0 and Tr Q=4,Tr L=8, gives

`Tr(WbarR*)=4a+2b-4=(8a+4b-8)/2>=0`.

Consequently the lossless V-twirl tR* of any actual PPT target with BOTH support inclusions has nonnegative expectation. This assumes universal positivity and uses one necessary test to bound the objective; it does NOT use that test to certify universal positivity of a candidate. The proof uses neither the32-term Schmidt-two decomposition, nor the uniform two-level decomposability theorem, nor a Schmidt-number bound on untwirled face points. The supplied v78 parent explicitly has its own earlier proof chain and does not import this pending actual-face theorem; there is no circular dependency.

## 9. The eligible R_x is an ACTUAL PPT state and escapes BOTH faces and J

For x>0 let eta_x=1/(4+8x)>0 and

`R_x=Q+xP(00)+(1/4)sum_(ell in L,ell!=13)P(ell)+eta_x P(13)`.

It is PSD as an explicitly nonnegative sum. Only the00/13 PT block changes, becoming

`[1/2+x,(1-i)/4;(1+i)/4,eta_x]`.

Its diagonals are positive and its determinant is `(1/2+x)/(4+8x)-2/16=1/8-1/8=0`. All other seven physical rank1 PT blocks remain unchanged, with no added off-block entry. Hence R_x is PPT. Its trace is

`tau_x=4+x+7/4+eta_x=23/4+x+1/(4+8x)>0`.

Therefore rho_x=R_x/tau_x is a genuine PPT density matrix, Gaussian-rational for every rational x>0. At x=0 it reduces to R*; strict x>0 matters for the following escapes.

First support: |00> is outside Ran R*. It is high, and its squared Q projection is Q_(00,00)=1/2<1. More explicitly v=(I-Q)|00> is a nonzero vector in ker R* and `<v,R_x v>=x|<00,v>|^2=x/4>0`. Thus Ran R_x cannot be a subspace of Ran R*. Equivalently, the positive xP(00) summand adds a new high direction.

Second support: the old00/13 range line was span(1-i,1). In the changed block the ratio high/low is `(1-i)/(4eta_x)=(1-i)(1+2x)`, unequal to1-i for x>0. The fixed nonzero off-diagonal cannot obey the old row proportionality S_hl=(1-i)S_ll when eta_x!=1/4. Thus Ran R_x^Gamma is not contained in Ran(R*)^Gamma. This is an actual changed line, not merely a statement that the determinant stayed zero.

Actual J asymmetry follows already from the diagonals: the00 high diagonal is1/2+x while the10 high diagonal, in its J orbit, is1/2. Normalization cannot restore invariance. The new state also lies outside the old no-H-noise family: it adds high noise and decreases the13 low coefficient below1/4. Those two changes compensate in the actual PT determinant, explaining why the old low-only PPT criterion does not apply.

These facts establish ELIGIBILITY of a genuine asymmetric PPT target interface, not SN>=3, not feasibility of any D, and not a separator. Absence of exclusion is not positivity evidence. No evaluated parameter or finite numerical certificate is being accepted here.

## 10. Unchanged full residual, named imports and assurance ceiling

Still unproved: actual positive sixteen-entry D satisfying the FULL universal complex inverse-Gram condition for EVERY complex rank2 plane, all eight coupled source-valid infinite-family inequalities using the SAME D, and a negative objective on an actual PPT target such as rho_x, or a uniform obstruction for the genuine asymmetric trade, while retaining the ENTIRE four-complex-block PPT residual. The new face theorem does not replace that residual by a symmetric or diagonal ansatz. General non-diagonal positive completions and unrestricted P44 remain outside this route as before.

Correctness inputs reconstructed here are the literal fixed-Q range/physical PT table, complex support linear algebra, the complete face equations, the explicit rank2 test and J geometry, and the full positivity/PPT/support calculations for R_x. Elementary Hermitian spectral/range facts and the coefficient-matrix interpretation of Schmidt rank are ordinary named finite-dimensional linear-algebra imports. The circulant-state ancestry cited by the author at Chruściński–Kossakowski0705.3534v3 SectionIV/Theorems2–3 is NAMED ANCESTRY, not an unread correctness premise: the complete PT shuffle is derived above. That paper's Ha example is not imported as an SN3 target. If translated to positive-map terminology, the classical Choi/Schmidt-rank correspondence retains the already named Hou–Li–Poon–Qi–Sze2015 Propositions2.2–2.3 boundary; this review is not a new full-paper or SOTA audit.

**Decision:** scoped no mathematical defect found in the full main theorem plus mandatory addendum and eligible-interface claims. The within-V face is one-dimensional; the whole untwirled face is NOT claimed one-dimensional or SN<=2. The direct no-negative corollary has an independent proof chain. No arbitrary-D no-go outside these supports, feasible D/SN3 target, whole P44, finite-certificate/triple replay, formal/kernel, human/configured-family/cross-vendor, novelty/SOTA or publication acceptance is conferred. N4 UNKNOWN/incomplete/exit-unestablished and old21-table/process histories are not repaired. Original October27 cutoff/deadline and written-only HOLD are unchanged. This serial review is not roundcompletion; I return to the actual102319 full-SEP primary checkpoint.
