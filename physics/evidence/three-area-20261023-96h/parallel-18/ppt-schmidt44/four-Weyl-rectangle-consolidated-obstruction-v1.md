# Four irreducible Weyl rays: a rank-three-minimum range, exact PPT spectrum, rational target and scalar-completion obstruction

Actual `/bin/date` before writing: **Sun Oct 25 08:01:26 PDT 2026**. Owner PhysicsPPT44-2. **AUTHOR-WRITTEN CANDIDATE; independent cross-domain reconstruction and parent disposition absent.** No scientific interpreter/eval/arithmetic program, enumeration, solver or certificate replay. Source reading and metadata hashes/clocks only. HOLD v2 and parent errata remain binding.

## 1. Exact freeze and why the supported old bounds are not decisive

The prior interface freeze is `four-Weyl-rectangle-interface-freeze-v1.json`, SHA-256 `be3aab35754cba725801dc15dea2267baaafb3497b0c7ebc711d43d3d1a0903c`. It records the literal rays, full-complex rank-two interface and actual rational PPT target before this consolidated manuscript, and discloses informal written leads considered while scoping.

The mechanism uses FOUR mutually orthogonal ME4 rays. Their positive projector sum Q has rank4, so it cannot admit ANY conic representation by at most three rank-one terms, even nonorthogonal/dependent ones. It therefore genuinely escapes the supported at-most-three-ME-conic-term theorem.

The older generic bounds leave a real gap here: the swap sum gives only `Q^Gamma<=I`, while a two-ray Gram test forces `lambda>=(2+sqrt2)/4<1`. They do not exclude `W_lambda=lambda I-Q` in the interval below1. This packet derives genuinely additional structure: the EXACT partial-transpose spectrum from eight2 by2 blocks. It does not relabel the old term-count/swap argument as a new obstruction.

The negative subspace also has a substantive property: every nonzero vector in Ran(Q) has Schmidt rank at least3. This proves that non-PSD, two-block-positive scalar completions exist in an existential compactness sense. Nevertheless, their exact PPT overlap bound is smaller than the necessary rank-two threshold, so NONE detects a PPT state. This is a uniform structural obstruction for all lambda, not a list of isolated controls.

No claim is made about arbitrary four-ME subspaces, anisotropic completions, SOTA or unrestricted P44.

## 2. Literal rays, irreducibility and source-valid framework

All indices are modulo4. Let zeta=i and

```
Z|j>=zeta^j|j>, X|j>=|j+1>,
U_pq=Z^p X^q, p,q in{0,1},
Phi_pq=vec(U_pq)/2,
Q=sum_(p,q in{0,1}) P(Phi_pq),
W_lambda=lambda I16-Q, lambda>=0.                       (1)
```

The four U are I,Z,X,ZX. They are unitary, have Hilbert–Schmidt norm2 and are mutually Hilbert–Schmidt orthogonal: a nonzero shift has zero trace, while Tr(Z)=0. The one remaining cross trace is a unit scalar times Tr(Z), also zero. Hence the four Phi are unit orthonormal rays, Q is a rank4orthogonal projection and Tr(Q)=4. For0<=lambda<1, W has FOUR negative eigenvalues. This is not a literal member of either retired one/two-negative family.

The general source framework is Hou–Li–Poon–Qi–Sze, [primary2015 PDF](https://faculty.sites.iastate.edu/ytpoon/files/inline-files/pmaps_LAA_2015.pdf), Propositions2.2–2.3: full complex Choi/Schmidt-rank k-positivity and multiple negative elementary terms. It does not promise indecomposable two-positive headroom. The Chruściński–Kossakowski–Sarbicki [0908.1846v2](https://arxiv.org/html/0908.1846v2) strict spectral sufficient criterion is inapplicable: the four negative ME rays at k=2 contribute squared-Schmidt-norm sum2, not<1. No positivity certificate is borrowed from it.

## 3. Full-complex universal rank-two criterion, derived first

For EVERY complex4 by2isometry S, let P=S S* and form the4 by4Hermitian Gram matrix, with a,b indexing the four U rays,

```
H_ab(P)=(1/4)Tr(U_a* P U_b).                             (2)
```

The exact criterion is

```
W_lambda is two-block-positive
 iff H(P)<=lambda I4 for EVERY complexrank2projector P.   (3)
```

Proof. For every rank-at-most-two coefficient matrix C, write C=SZ, with columns z_j. Let V_j have columns `(1/2)S*U_a e_j`. The four negative overlaps are

```
h_a=(1/2)Tr(U_a* C), h=sum_j V_j* z_j,
||C||_F^2=||Z||_F^2, sum_j V_j*V_j=H(P).
```

The exact squared norm of the linear map Z->h is lambda_max(H), giving sufficiency. If Hv=gv for a unit v and g>lambda, choose z_j=V_jv. This gives `||Z||_F^2=g`, h=gv and witness expectation `g(lambda-g)<0` on a genuine rank-at-most-two C. Thus necessity is exact. The proof includes all complex planes and lower-rank C; no chosen real plane or finite sample is a substitute.

For the concrete plane span{e0,e1}, its principal I,Z block is

```
[1/2,(1+i)/4;(1-i)/4,1/2].
```

Therefore every universally rank-two-nonnegative W_lambda must satisfy

```
lambda>=lambda0=(2+sqrt2)/4.                             (4)
```

The fourth ray does not invalidate the principal-block lower bound. But the old swap bound for FOUR rays only gives the upper PPT overlap1, so(4) alone is not a PPT no-go.

## 4. Every nonzero range matrix has rank at least three

A vector in Ran(Q) has coefficient matrix

```
C=alpha I+beta Z+gamma X+delta ZX.
```

Define `A_r=alpha+beta zeta^r`, `B_r=gamma+delta zeta^r`. A kernel vector v satisfies the cyclic-bidiagonal recurrence

```
A_r v_r+B_r v_(r-1)=0, r=0,1,2,3.                       (5)
```

We prove dim ker(C)<=1 for every nonzero C, covering all coefficient endpoints.

- If A is identically zero, C=diag(B_r)X. The nonzero affine polynomial gamma+delta z has at most one zero among the four distinct fourth roots, so C has rank at least3. The case B identically zero is the same diagonal argument. Both identically zero would give C=0, which is excluded.
- Otherwise each list A,B has at most one zero. If either list has no zero, (5) determines every component from one chosen component by cyclic forward or backward recurrence. The closing equation may remove that freedom but cannot add one, so nullity is at most1.
- It remains that A has its unique zero at r and B its unique zero at s. If r=s, that row is zero and the other three nonzero links form one path through all four unknowns, leaving exactly one free value.
- If r differs from s, row r forces v_(r-1)=0 and row s forces v_s=0. Remove the two missing links from the four-cycle. The path from s through r-1 is anchored at both ends and is identically zero by the remaining nonzero links. The other path from r through s-1 has one free value. This includes adjacent r,s, where a path may be a single vertex. Thus again the nullity is at most1.

Consequently every nonzero C in this four-dimensional range has rank at least3, over the FULL complex field.

Let K be the compact set of unit Schmidt-rank-at-most-two vectors, and put `eta=max_(psi in K)<psi,Qpsi>`. It is compact because the rank minors and unit norm define a closed bounded finite-dimensional set. Since Q is an orthogonal projection, eta=1 would give a unit vector of K in Ran(Q), contradicting the rank argument. Hence

```
eta<1.                                                  (6)
```

By definition every lambda>=eta gives a two-block-positive W_lambda. Therefore rational choices with eta<lambda<1 exist, giving non-PSD two-block-positive scalar completions. This is **existence-only headroom**, not a displayed certified rational lambda or an indecomposable witness. An explicit value of eta is not claimed or needed for the uniform obstruction below.

## 5. Exact partial transpose: a new structural calculation beyond the swap bound

Write T=Q^Gamma. With F the swap, each normalized ME projector has partial transpose `(U tensor I)F(U* tensor I)/4`. Direct application of U_pq=Z^pX^q gives

```
T|r,s>=(1/4)[(1+zeta^(s-r))|s,r>
                    +(1+zeta^(s-r+1))|s+1,r-1>].       (7)
```

Thus the total index tau=r+s modulo4 is invariant. In its four-dimensional sector use `v_r^(tau)=|r,tau-r>`. Then

```
T v_r=(1/4)[(1+zeta^(tau-2r))v_(tau-r)
                  +(1+zeta^(tau-2r+1))v_(tau-r+1)].      (8)
```

This formula produces the following exhaustive EIGHT2 by2blocks. Each listed diagonal pair and upper off-diagonal coefficient is divided by4; the lower coefficient is its conjugate. Pair labels refer to the r indices within the indicated sector.

| tau | ordered pair | unscaled diagonal pair | unscaled upper off-diagonal |
|---:|---|---|---|
|0|(0,1)|(2,0)|1-i|
|0|(2,3)|(2,0)|1-i|
|1|(0,1)|(0,2)|1-i|
|1|(2,3)|(0,2)|1-i|
|2|(0,3)|(0,2)|1+i|
|2|(1,2)|(2,0)|1-i|
|3|(0,3)|(2,0)|1+i|
|3|(1,2)|(0,2)|1-i|

Every basis ket appears in one block. Formula(8) has no matrix entries outside these blocks. For instance at tau=0, even r has first coefficient2, odd r has first coefficient0, and the second coefficients1+i,1-i pair(0,1) and(2,3); the other sectors are obtained by substituting zeta^tau=i,-1,-i, respectively. This explains the entire table symbolically, not by an arithmetic interpreter.

Every unscaled block has trace2 and determinant-2. Its two eigenvalues are1+sqrt3 and1-sqrt3. Therefore T has EXACT spectrum

```
alphaP=(1+sqrt3)/4, multiplicity8,
betaP=(1-sqrt3)/4, multiplicity8.                         (9)
```

In particular `T<=alphaP I16`, which is strictly stronger than the old generic sum bound T<=I16. This is the genuinely new obstruction ingredient.

## 6. An actual different rational PPT-negative candidate, and its exact rank-two rejection

Define

```
rho4=(I16+4Q)/32,
W_trial=(3/5)I16-Q.                                     (10)
```

Q has Gaussian-rational entries with denominator4. Thus rho4 has Gaussian-rational entries with denominator dividing32. It is positive definite, has trace `(16+4*4)/32=1`, and has full local supports4. Its eigenvalues are5/32 on Ran(Q) and1/32 on its orthogonal complement. This is a different full-rank density matrix, not x1111 or the prior rank10 cyclic target.

There is a direct Gaussian-rational PPT Gram certificate. Each block of `I+4T` from the table is either

```
[3,u;conj(u),1] = P((u,1))+P((1,0)),
```

or

```
[1,u;conj(u),3] = P((1,conj(u)))+P((0,1)),
```

where u=1+i or1-i and |u|^2=2. This certifies all eight blocks positively with exact integer-Gaussian kets; it does not need an approximate eigenvalue. Hence rho4 is PPT, indeed its partial transpose is positive definite.

Using Q^2=Q and Tr(Q)=4,

```
Tr(Qrho4)=(4+4*4)/32=5/8,
Tr(W_trial rho4)=3/5-5/8=-1/40.                          (11)
```

This is an actual rational PPT-negative pair. But the universal rank-two certificate fails: use `C0=diag(1,1+i,0,0)/sqrt3`. The I,Z overlaps have squared moduli5/12 each. The X and ZX overlaps vanish because both are shifted with zero diagonal. Thus

```
<vec(C0),Qvec(C0)>=5/6,
<vec(C0),W_trial vec(C0)>=3/5-5/6=-7/30.                  (12)
```

C0 has rank two and unit Frobenius norm. Therefore W_trial is NOT two-block-positive; no SN3 inference is made. Ordinary block-positivity of W_trial is also not asserted. The candidate is included to make the exact state/PPT/negative-expectation interface real rather than hypothetical; the following result settles the whole lambda family, not just this failed value.

## 7. Exact all-PPT overlap boundary and uniform scalar-completion no-go

For any PPT density matrix rho,

```
Tr(Qrho)=Tr(T rho^Gamma)<=alphaP.                        (13)
```

This upper bound is attained. Let

```
t0=-1/betaP=2(1+sqrt3),
rho_t=(I+tQ)/(16+4t), 0<=t<=t0.                         (14)
```

Positivity is immediate. From(9), `I+tT>=0` precisely throughout the stated nonnegative interval, so rho_t is PPT. Its overlap is `(1+t)/(4+t)`. At t=t0,

```
(1+t0)/(4+t0)=(3+2sqrt3)/(6+2sqrt3)=alphaP.               (15)
```

The last equality follows by multiplying alphaP by its denominator: `(1+sqrt3)(6+2sqrt3)/4=3+2sqrt3`. Thus

```
max_(rho PPT,Tr rho=1) Tr(Qrho)=alphaP.                   (16)
```

It follows that W_lambda has nonnegative expectation on EVERY PPT state iff lambda>=alphaP; for lambda<alphaP the literal rho_t0 is a negative PPT direction. For rational lambda<alphaP, continuity of(14) and density of rationals give a rational t<t0 with negative expectation, hence a Gaussian-rational PPT target. Formula(10) is one explicit such target, not an uncomputed existence claim.

On the other hand, every two-block-positive W_lambda satisfies(4). Therefore

```
W_lambda^Gamma=lambda I-T
 >=[lambda0-alphaP]I
 =[(1+sqrt2-sqrt3)/4]I>0.                               (17)
```

The strict sign follows from `(1+sqrt2)^2=3+2sqrt2>3`. This proves the ENTIRE fixed four-Weyl-ray scalar-completion family is completely copositive whenever universally rank-two nonnegative. It detects no PPT state, even though its non-PSD two-positive region is nonempty by(6).

The obstruction did NOT follow immediately from the accepted at-most-three-term theorem or generic swap bound. It required the rank4irreducibility and new exact partial-transpose block structure. No isolated lambda controls are used as a substitute for(17).

## 8. Exact remaining science and assurance

This packet supplies one consolidated mechanism: four irreducible ME rays, the complete universal complex Gram interface, a four-dimensional rank>=3range, an actual rational PPT-negative trial, and an exact all-lambda structural obstruction with the complete PPT boundary.

It does NOT close arbitrary four-ME subspaces, four nonorthogonal ME terms, non-ME rays, anisotropic positive completions of this range, or arbitrary two-positive M4 maps. The compactness result does not provide a numerical positivity threshold eta or a displayed rational two-positive non-PSD witness; neither is required for the proved uniform no-detection theorem.

Any next positive use of this negative subspace must change its scalar positive completion; any next scalar completion must change the negative geometry beyond this Weyl rectangle and provide a full-complex criterion plus a genuine PPT-negative target. No such new route is declared viable here. Unrestricted P44 remains unanswered.

The old accepted families and x1111 retain their exact v8/v9-qualified dispositions. Their historical21table and native N4 faults are not repaired or rerun. No SOTA/novelty, formal/kernel, human/cross-vendor, scientific-execution or publication acceptance is claimed. This manuscript is author-WRITTEN only, pending genuine cross-domain reconstruction and parent disposition; no GO is requested.
