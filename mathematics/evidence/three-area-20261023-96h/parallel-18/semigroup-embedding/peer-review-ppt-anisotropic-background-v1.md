# v78-A — independent written reconstruction of the anisotropic Weyl positive background

Reviewer MathSemigroup-2. Actual clock observed before this write: **Sun Oct 25 10:52:34 PDT 2026** (`/bin/date`); this is an observation bound, not an invented exact completion time. **WRITTEN only. Verdict: 0 FATAL / 0 MAJOR / 0 MINOR mathematical defects found at the exact scope below.** This does not erase any inherited process finding. No scientific interpreter, symbolic/numerical program, solver, enumeration, certificate replay, evaluated threshold or finite-witness acceptance occurred in this review.

## 1. Exposure, complete reading and source binding

The exposure ACK `peer-review-ppt-anisotropic-background-ack-v1.json`, SHA256 `10b55c1a17cd7b0fd2c7ddcc89f7016675c781d8d6eeb3ba8034fc24434d0ac5`, was written at the actual observed **Sun Oct 25 10:45:11 PDT 2026**, BEFORE opening the new proof body. It records prior v43/v48/v52/v55 PPT exposure and my returned v75 TC-zero review. This is not blind or cross-model review; the new 362-LF body was not inherited from the scalar verdict. The v75 attribution correction is retained: the older v67-B depolarizing reviewer was MathOlson-2-2, not me.

Before this temporary review I wrote the actual own-primary interruption checkpoint `primary-102319-M-normalform-checkpoint-v1.json`, SHA256 `cfff011575f621332da08a678b0e66eb1c3283007a53f7f76879ae52e9c95b23`, observed **Sun Oct 25 10:42:44 PDT 2026**. That records the all-(M) contraction normal form and its still-open V-reflection/SEP obligation. This review does not replace that primary task.

Complete packet coverage: physical LF1–757, including EVERY LF of S1/v9, then S2/v10, then S3/v11, followed by the COMPLETE 362-LF new source, COMPLETE 232-LF baseline and COMPLETE 24-LF parent boundary. Reads covered 1–203, 204–408, 409–623 and 624–757; the truncated physical LF751 was recovered verbatim with a raw read. No ending was inferred from a hash or headline.

Live metadata pins observed after the full read:

- Manifest `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v78.json`: `cd2dba071b382b483ce08b2692ec2fa213a92d23febc1969020cd327656bc3fd`.
- Receipt `peer-review-wave-eighteen-v78-packet-receipt-v1.json`: `1bd22b674859bd92782d4db71333fa61eb4de406c04a8fa59bda16d7208ed9b1`.
- Sole literal part `peer-review-wave-v78-v78-A-part1-v1.md`: `9f7d3886dd91d31a74cf9c89c88debcbdfb3f5305cb8e711e62428ca3585e77c`.
- NEW `physics/evidence/three-area-20261023-96h/parallel-18/ppt-schmidt44/anisotropic-Weyl-positive-background-consolidated-v1.md`: `fa39d6a671455eec40a7f05b0c48ec80cd3b63f0b395920609de8611a8d64d3c` (S4,362LF).
- Baseline `four-Weyl-rectangle-consolidated-obstruction-v1.md` in the same author root: `eb1ed1c5aba2bb444a817b48a39ff3d7206c1aacc65421cca7073cffe64a5e02` (S5,232LF).
- Parent `institute/runs/three-area-2026-10-23-96h/ppt-four-Weyl-semigroup-two-choice-parent-v1.md`: `562ec6fde1da880b73a5f67e490b9e3d05c66e122795a740cca1e916f1a40c34` (S6,24LF).

S1/v9 is `b7c92143cda18c88c7c56017859ab3c7f08fa92ef3d00fd85ba29f41ac258034`; S2/v10 is `d61acbf77fefa3a8d55d0cf74e9ebe0b680edb28d273f5b22255d09cbd66aa62`; S3/v11 is `3ce29e3c49d4789106431978152ffab28a3d14402a748ec3828c825f31c4d9e7`. Their permanent execution/coverage/freeze/clock/href corrections are retained. They are frozen inputs to this v78 review, not retroactively inserted into older waves. The author's disclosed missed earlier active checkpoint remains a separate process deviation; this mathematical reconstruction does not cure it.

## 2. Conventions and a fresh reconstruction of the needed baseline

Use `vec C=sum C_ij |i,j>`, Bob partial transpose Gamma, `P(v)=|v><v|`, indices modulo4, `Z e_j=i^j e_j`, `X e_j=e_(j+1)`. Let U run through I,Z,X,ZX and Phi_U=vec(U)/2. The four U have squared Hilbert–Schmidt norm4 and are mutually orthogonal: nontrivial shifts have zero trace, and the remaining diagonal cross traces are phases times Tr Z=0. Hence Q=sum P(Phi_U) is an orthogonal rank4 projection.

Here H denotes the PRODUCT-BASIS projector onto differences i-j=0 or1, and L=I-H. Both have rank8. The I,Z rays have difference0, X,ZX difference1, so Q<=H, and H-Q is an orthogonal rank4 projection. This H is not a one-local Hamiltonian from another review.

### 2.1 Full-complex range rank, including the degenerate endpoints

A range matrix is C=alpha I+beta Z+gamma X+delta ZX. Put A_r=alpha+beta i^r, B_r=gamma+delta i^r. The kernel equations are A_r v_r+B_r v_(r-1)=0.

If A is identically zero, C=diag(B)X; a nonzero affine polynomial gamma+delta z has at most one zero among the four distinct fourth roots, so rank C>=3. The B-identically-zero case is diagonal and identical in conclusion. Both identically zero is precisely the excluded zero matrix. Otherwise each list has at most one zero. If A has no zero, each equation determines v_r from v_(r-1); if B has no zero it determines v_(r-1) from v_r. In either case cyclic closure leaves at most one scalar free. This includes the case in which the other list has its one zero; that zero can remove freedom, never add it.

If both lists have unique zeros, say A_r=0, B_s=0, then for r=s one row vanishes and the other three nonzero links make one path through all four vertices: one free scalar. For r!=s, row r anchors v_(r-1)=0 and row s anchors v_s=0. Removing those two links splits the four-cycle into the path from s to r-1, anchored zero, and the other path from r to s-1, with at most one free scalar. When s=r-1 the anchored path is the single vertex s; when s=r+1 the other path is the single vertex r; the opposite case gives two two-vertex paths. Thus every adjacent and opposite separation is covered. Nullity<=1, over C, in ALL cases.

It follows directly that Ran Q contains no nonzero vector of Schmidt rank<=2. Compactness of the unit rank<=2 set K gives eta=max_K <Q><1: equality would place an element of K in Ran Q. This is existential, with NO evaluated eta or explicit certified rational scalar parameter.

### 2.2 Exact eight PT blocks, not a rounded spectrum

Applying `(U tensor I)F(U* tensor I)/4` to each basis ket gives

`4T|r,s>=(1+i^(s-r))|s,r>+(1+i^(s-r+1))|s+1,r-1>`, T=Q^Gamma.

Thus tau=r+s is invariant. For v_r=|r,tau-r>, the two destinations are v_(tau-r),v_(tau-r+1), with coefficients `1+i^(tau-2r)` and `1+i^(tau-2r+1)`. Substitution gives the exhaustive table below. Entries are the UNDIVIDED diagonal pair and upper off-diagonal; divide each block by4.

|tau|pair of r-indices|diagonal pair|upper|
|---:|---|---|---|
|0|(0,1)|(2,0)|1-i|
|0|(2,3)|(2,0)|1-i|
|1|(0,1)|(0,2)|1-i|
|1|(2,3)|(0,2)|1-i|
|2|(0,3)|(0,2)|1+i|
|2|(1,2)|(2,0)|1-i|
|3|(0,3)|(2,0)|1+i|
|3|(1,2)|(0,2)|1-i|

There are no omitted matrix elements: the displayed action has only the two listed destinations; coefficients that would leave a listed pair are zero. Every one of the sixteen basis vectors belongs to exactly one pair. Since the basis difference is 2r-tau, the diagonal2 position is H and the diagonal0 position L in EVERY pair. Reordering each pair H-first therefore gives exactly `(1/4)[2,u;bar(u),0]`, u=1+i or1-i. The reordering conjugates the upper coefficient when it reverses a pair, which does not change this stated set of u's.

Each unscaled block has trace2 and determinant-2, so its eigenvalues are 1±sqrt3. Therefore T has eigenvalues (1±sqrt3)/4, each eightfold. This rederives the actual H/L geometry used below; merely importing the scalar alphaP bound would not establish it.

## 3. Universal complex inverse-Gram iff and the zero-boundary reduction

Let D=sum d_ij P(ij), initially ALL d_ij>0. Every rank<=2 matrix is C=SZ for some complex 4-by-2 isometry S, including lower-rank matrices by extending their column span. Write its columns S z_j and define A_j=S*diag_i(d_ij)S, V_j with columns S*U_a e_j/2. Then

`E=sum_j z_j* A_j z_j`, `h_a=Tr(U_a* C)/2`, `h=sum_j V_j* z_j`.

All A_j are positive definite. With x_j=A_j^(1/2)z_j the overlap map is L_D(x)=sum V_j* A_j^(-1/2)x_j, so

`L_D L_D*=sum V_j* A_j^(-1)V_j=G_D(S)`.

Consequently E-||h||^2>=0 for all Z exactly when G_D(S)<=I. If G_D v=g v with ||v||=1 and g>1, take z_j=A_j^(-1)V_j v. Then E=g, h=g v and expectation g-g^2<0 on an actual rank<=2 C. This proves BOTH directions, with all complex planes retained, without inverting G_D or assuming independent negative features. Replacing S by another isometric basis of the same plane leaves G_D unchanged. No real-only or sampled-plane surrogate is present.

Zero coefficients are not put into these inverses. For a Hermitian diagonal D, the product-ket tests already force d_ij>=1/2 on H and d_ij>=0 on L whenever W(D)=D-Q is two-block-positive. Thus any eligible D is nonnegative. If a zero-boundary W has strict expectation -delta on a trace-one PPT state, W+epsilon I remains two-block-positive and still has negative expectation for 0<epsilon<delta; all its diagonal coefficients are positive. A rational epsilon exists if rational data are wanted. This is a lossless reduction for EXISTENCE OF STRICT DETECTION in this route, not an inverse formula at zero or a classification of every boundary equality. The two-level zero endpoints are treated directly below.

## 4. The rank-two controls and actual rational target

For `C=(I+Z)+sqrt2(E13+E31)`, the diagonal is (2,1+i,0,1-i). The {1,3} block has determinant `(1+i)(1-i)-2=0` and is nonzero, hence rank1; the isolated00 entry has rank1, row/column2 is zero. Therefore rank C=2. Its H part is exactly I+Z in Ran Q, of squared norm8, and its L part has squared norm4. Thus

`<C,W(a,b)C>=8a+4b-8=4(2a+b-2)`.

Universal rank-two nonnegativity requires 2a+b>=2. On the diagonal two-coordinate subspace the I,Z FEATURE Gram has diagonal1/2 and upper (1+i)/4, hence top eigenvalue a0=(2+sqrt2)/4. The coefficient-variable Gram is its conjugate-convention counterpart and has the same eigenvalues; no phase is silently discarded. The X/ZX overlaps vanish there. This gives the independent necessary condition a>=a0>3/4. Neither necessary test is asserted sufficient.

`rho6=(4Q+L)/24` is positive, trace one and rank12, since its Q and L supports are orthogonal of ranks4,8. Every PT block of 4Q+L in the H/L order is `[2,u;bar(u),1]=P((u,1))`; |u|^2=2. These eight rank1 Gaussian-integer blocks cover the whole matrix, so rho6 is PPT with PT rank8. This is an exact symbolic Gram certificate, not a numerical finite-witness admission.

Its H,L,Q expectations are 2/3,1/3,2/3, so `Tr(Wrho6)=(2a+b-2)/3`. At a=7/8,b=1/8 this is -1/24. The displayed rank2 C has squared norm12, and after normalization its witness expectation is the SAME -1/24. Therefore the trial is rejected, not an SN3 witness.

## 5. Genuine non-CCP headroom, with an unevaluated threshold

`W0=(H-Q)+(1/4)L` is PSD with kernel Ran Q. Its expectation on every unit rank<=2 vector is strictly positive by Section2.1, and compactness gives a minimum mu0>0. Equivalently W0>=(I-Q)/4 and eta<1 imply a positive lower bound, without evaluating it. For `0<epsilon<min(mu0,1/8)`,

`W_epsilon=(1-epsilon)H+(1/4)L-Q`

has every such expectation at least mu0-epsilon>0. Its eigenvalues on Q are -epsilon (fourfold), on H-Q are 1-epsilon, and on L are1/4. It is non-PSD and genuinely anisotropic. Its PT blocks have diagonal (1/2-epsilon,1/4) and off-diagonal modulus sqrt2/4, whose determinant is -epsilon/4<0. Hence it is NOT completely copositive.

This is a valid existence argument for two-block-positive, non-CCP headroom, including existence of rational epsilon in the open interval. It supplies NO evaluated mu0/eta, NO displayed certified epsilon, and NO indecomposable or SN3-positive example. In particular the old scalar CCP verdict cannot dispose of this new class just by renaming a scalar.

## 6. The whole two-level class is nevertheless decomposable

For a>=1, `W=(a-1)H+(H-Q)+bL>=0`. This includes a=1,b=0. If a<1 and W is two-block-positive, the two controls imply a>=a0>3/4 and b>=2(1-a). Set s=1-a>0, t=4a-3=1-4s>=0. Direct coefficient comparison gives

`W=t(H-Q)+R`, `R=3sH+bL-4sQ`.

Every PT block of R is `[s,-s u;-s bar(u),b]`. Both diagonals are nonnegative and its determinant is s(b-2s)>=0. Thus R^Gamma>=0, and

`W=t(H-Q)+(R^Gamma)^Gamma`

is a complete explicit decomposable identity. No unknown sum or inverse at an endpoint is used. For b=0 the control 2a+b>=2 forces a>=1, already covered directly. Values a=0 or other excluded boundary values cannot be two-block-positive by the controls. At a=1 the same identity is also consistent with s=0. This proves the full two-level no-PPT-detection statement, NOT complete copositivity; Section5 explicitly precludes that stronger conclusion.

## 7. Exact ALL-PPT boundary, all endpoints, and actual targets

For a,b>=0 the exact condition is a>=f(b), with f=1-b/2 on 0<=b<=1/2 and f=1/2+1/(8b) on b>=1/2.

For the first branch set a*=1-b/2, s=b/2,t=1-2b. The identity in Section6 applies algebraically and its R^Gamma blocks are `[b/2,-(b/2)u;-(b/2)bar(u),b]`, PSD of determinant0, with t>=0. This includes b=0 (R=0, W=H-Q). Increasing a adds (a-a*)H>=0. Necessity is rho6, with expectation (2a+b-2)/3<0 exactly below this branch.

For b>=1/2 the PT block of W is `[a-1/2,-u/4;-bar(u)/4,b]`. At a*=1/2+1/(8b) the determinant is0 and the diagonals positive, so W is CCP; increasing a preserves this. The two formulas agree at b=1/2, a*=3/4.

For necessity in this branch put y=(2b-1)/(2b+1), z=1/[4b(2b+1)] and Sigma_b=Q+y(H-Q)+zL. It is nonzero PSD. More generally xQ+y(H-Q)+zL has PT blocks `[(x+y)/2,(x-y)u/4;(x-y)bar(u)/4,z]`, PSD exactly when 4z(x+y)>=(x-y)^2, for x,y,z>=0. With x=1,

`1+y=4b/(2b+1)`, `1-y=2/(2b+1)`, `4z(1+y)=(1-y)^2`.

Therefore Sigma_b is PPT. Its trace is 4(1+y)+8z>0, and

`Tr(W Sigma_b)=4a(1+y)+8bz-4=4(1+y)(a-a*)`.

For example `8bz=2/(2b+1)` and `4(1+y)a*=4-2/(2b+1)`, verifying the cancellation exactly. Normalizing gives an actual PPT density matrix negative whenever a<a*. At b=1/2 this is Q+L/4, whose normalization is rho6. For rational b all coefficients are rational and Q is Gaussian-rational. No optimizer, rounded spectrum or claim that all PPT states have this form is used.

## 8. Complete 32-term symbolic decomposition and all eight noise parameters

For k modulo4 let r=k-1,s=k+1 and A_k=I-i^(-k)Z. Its k entry is0, k+2 entry2, r/s entries1+i,1-i. For w in {1,i,-1,-i},

`C_kw=A_k+sqrt2(w E_rs+w^(-1)E_sr)`

has the nonzero rank1 opposite block (determinant2-2=0), the isolated rank1 entry2 and the zero k row/column. Thus all sixteen C_kw have rank2 and squared norm12. Left multiplication by X preserves both properties.

The four-root sums of w and w^(-1) are zero. Their cross character is w^2, whose sum is also zero. Consequently the w-average of P(vec C_kw) is exactly `P(vec A_k)+2P(rs)+2P(sr)`; this accounts for ALL cross terms, including the two off-diagonal characters. The k-average of P(vec A_k) is P(vec I)+P(vec Z), because the I/Z cross characters i^k and i^(-k) sum to zero. Each ordered difference2 position appears for exactly two k values, each contributing2 before the factor1/4; its resulting coefficient is1. Therefore

`(1/16)sum_(k,w)P(vec C_kw)=P(vec I)+P(vec Z)+sum_(i-j=2)P(ij)`.

Multiplying on the left by X sends I,Z to X,XZ, with P(vec XZ)=P(vec ZX), and difference2 to difference3. The second sixteen-term average is thus `P(vec X)+P(vec ZX)+sum_(i-j=3)P(ij)`. Adding gives 4Q+L, because P(vec U)=4P(Phi_U). Division by24 yields precisely

`rho6=(1/32)sum_(e=0,1;k;w)P(vec(X^e C_kw)/sqrt12)`.

There are32 unit rank2 vectors, equal weights1/32 summing to1. The normalization is also checked by tracing:32*12/16=24 before division by24. This is a full symbolic phase identity, not a 32-row numerical table or a replay. It proves Schmidt number AT MOST2, not necessarily exactly2.

For `R=Q+sum_(ell in L)y_ell P(ell)`, all eight y_ell>=0 independent and no extra H noise, the eight PT blocks have diagonal (1/2,y_ell) and squared off-diagonal modulus1/8. Each L position appears once, so PPT is EXACTLY the eight inequalities y_ell>=1/4. Then

`R=(Q+L/4)+sum_(ell in L)(y_ell-1/4)P(ell)`

is a conic sum of the preceding SN<=2 operator and product projectors. Every normalized PPT member of this full eight-parameter family is therefore SN<=2 and cannot be an SN3 target for ANY witness form. This conclusion is not extended to arbitrary added H noise, compensating reduced L coefficients or arbitrary PPT states.

## 9. The actual J symmetry, and why a general state cannot be averaged by it

J=(X tensor I)SWAP sends |i,j> to |j+1,i>, has J^2=X tensor X and order8. On matrix coefficients it sends C to X C^T, preserving rank. Its ray action is I->X, Z->XZ=-iZX, X->I, ZX->Z. Thus it preserves Q,H,L. Its product-basis orbits are exactly H and L: J switches difference d to1-d, while J^2 shifts both indices through all four values. There are two length8 orbits, not a larger hidden orbit or an assumed local-unitary group.

Conjugation by J preserves rank-two nonnegativity; it also preserves PPT. For the SWAP part, Bob transpose after swapping corresponds to Alice transpose before swapping, and rho^Gamma_A=(rho^Gamma_B)^T>=0; the remaining factor is local unitary X. Averaging a two-block-positive W(D) over all8 powers therefore gives exactly W(a,b), with a,b the actual orbit averages of the SAME D.

ONLY if the ACTUAL state obeys JrhoJ*=rho does the objective remain `Tr(W(D)rho)=Tr(W(a,b)rho)`. The right side is nonnegative for PPT rho by Section6. This excludes arbitrary diagonal completions of this Q against every J-invariant PPT target, including rho6 and Sigma_b. It does NOT assert all such targets have SN<=2, and it does NOT justify J-twirling an arbitrary target against a nonsymmetric D. The eight-parameter SN<=2 result in Section8 and this witness-family symmetry obstruction have different scopes.

## 10. The lossless four-twirl and every complex PPT block/objective entry

The local unitary V=Z tensor bar(Z) has eigenvalue i^(i-j) on |i,j>. It fixes every product-diagonal D and each of the four Q ray projectors (the ray differences are0 or1). Hence the four-element V-twirl of ANY state preserves its W(D) expectation, trace, positivity and PPT. For strict detection in this route it is LOSSLESS, unlike the J-average of a general state.

The general twirled state has four COMPLEX Hermitian blocks:

`R=sum_(q,r,s) R^(q)_rs |r,r-q><s,s-q|`.

Positivity is equivalent to every R^(q)>=0. Bob transpose sends an entry to `|r,s-q><s,r-q|`. Its total index is tau=r+s-q, so in the total-index basis the exact entry is

`S^(tau)_rs=R^(r+s-tau)_rs`.

Consequently PPT is exactly all four R-blocks PSD and all four S-blocks PSD, together with sum Tr R^(q)=1. The index r+s-tau is symmetric in r,s, so Hermiticity is retained. Every matrix element is included; there is no real-entry restriction, omitted off-diagonal part or independent relaxation of coupled blocks.

On difference0 and1 the Q block is exactly `B_rs=(1+i^(r-s))/4`; on difference2 and3 it is zero. This follows directly from the two ray coefficients 1,i^r in each supported block. The full objective is therefore

`F_D(R)=sum_(q,r)d_(r,r-q)R^(q)_rr-sum_(q=0,1)Tr(B R^(q))`.

The trace contraction retains the complex conjugation convention through the Hermitian matrix product, not an entrywise real replacement.

## 11. All eight infinite rank-two tests, with the same sixteen coefficients

Fix q=0,1 and k=0,1,2,3, ell=k+2,r=k-1,s=k+1. For ALL complex t and nonzero complex w use

`C_qk(t,w)=X^q[A_k+(t-2)E_(ell,ell)+sqrt2(wE_rs+w^(-1)E_sr)]`.

The isolated entry is t; the opposite block still has determinant0 and rank1. Thus rank<=2 for the ENTIRE complex family, including t=0. Before multiplication by X,

`Tr C=t+2`, `Tr(Z* C)=-i^(-k)(t+2)`.

After multiplication by X the relevant rays are X,ZX, with only unit phases changing; the other two overlaps vanish by basis difference. Thus the total Q expectation is exactly |t+2|^2/2, with no w-dependent negative overlap hidden in L.

From the SAME D define A=d_(ell+q,ell), B=d_(r+q,r), C_d=d_(s+q,s), f=d_(r+q,s), g=d_(s+q,r). Positive energy is

`A|t|^2+2(B+C_d)+2f|w|^2+2g|w|^(-2)`.

For f,g>0, AM-GM gives infimum4sqrt(fg), attained at |w|^4=g/f; the phase is irrelevant here, not discarded from a phase-dependent expression. Subtracting the Q expectation leaves

`(A-1/2)|t|^2-2Re(t)+K`, `K=2(B+C_d)+4sqrt(fg)-2`.

If A<1/2 the quadratic is negative for large t; if A=1/2 the nonzero linear term is unbounded below. If A>1/2, completing the complex square gives

`(A-1/2)|t-1/(A-1/2)|^2+K-1/(A-1/2)`.

Hence nonnegativity on this entire family is EXACTLY A>1/2 and `(A-1/2)K>=1`. This verifies the equality boundary as well as the strict side; no A=1/2 branch is missing. The strict-D case suffices for strict detection by Section3. These are eight necessary infinite-family tests, not eight sampled vectors and not a sufficient replacement for the all-plane inverse-Gram condition.

Each A cycles through the four difference-q H entries; the accompanying B,C_d,f,g refer to the very same shared16-entry array. No family is allowed separately relaxed coefficients. For two levels A=B=C_d=a,f=g=b, the condition reduces to

`(a-1/2)(a+b-1/2)>=1/4`, `a>1/2`,

or `b>=2(1-a)+(1-a)^2/(a-1/2)`. The latter follows since the numerator over a-1/2 is a(1-a). For 1/2<a<1 the extra squared term is strictly positive. Thus a zero expectation of the supporting low-noise PPT-boundary witness cannot be promoted to universal two-positivity: the isolated rank1 entry can vary while the whole matrix remains rank<=2.

## 12. Exact residual, imports, and the disposition boundary

The original remaining step is retained in full: find actual positive d_ij and actual complex R^(q) satisfying the universal G_D(S)<=I for EVERY complex rank2 plane, all R^(q)>=0, all coupled S^(tau)>=0, trace1, the eight necessary shared-D inequalities above, and F_D(R)<0; or prove impossibility UNIFORMLY for that entire asymmetric product-diagonal route. Any detecting target must fail actual J invariance and be outside the eight-parameter no-H-noise SN<=2 class. The eight tests alone do not settle this residual. No feasible pair, arbitrary-D no-go, feasible SN3 state or P44 theorem is established.

Named imports are elementary finite-dimensional complex linear algebra (Schmidt rank equals coefficient-matrix rank, isometric column-span factorization, Hermitian spectral theorem, PSD2-by2 criterion), Heine–Borel/extreme-value compactness and density of rationals, and the definition of the SN<=2 convex cone. The needed range-rank and PT-block baseline is reconstructed above rather than imported from a rounded spectrum or a hash. If the matrix statements are translated into k-positive-map language, the classical Choi/Schmidt-rank correspondence is a NAMED import at Hou–Li–Poon–Qi–Sze2015 Propositions2.2–2.3 (the primary source was read in my earlier v43 assignment, not re-presented here as a new complete-paper read). The strict spectral sufficient criterion discussed in S5 is not used: its four-ME negative contribution is2, not<1. Older at-most-three-term or scalar swap bounds do not supply this anisotropic theorem.

**Scoped mathematical decision:** no defect found in the complete new interface, whole two-level decomposability/all-PPT boundary, symbolic32-term SN<=2 identity, independent eight-noise classification, actual-target J obstruction, lossless C4 residual, or eight coupled infinite-family controls. The non-CCP headroom is existential and is compatible with decomposability. Historical N4 UNKNOWN/incomplete/exit-unestablished findings and all parent errata remain untouched. This is one same-harness cross-domain written reconstruction with disclosed prior exposure, NOT formal/kernel, human, configured-family/cross-vendor, executable/triple-witness, novelty/SOTA or publication acceptance. Original cutoff/deadline unchanged; the review is not completion of the96-hour request. I return to the actual102319 full-SEP primary checkpoint, with its original embedding gap still open.
