# Three noncommuting maximally entangled rays: full complex Gram criterion and a scalar-completion obstruction

Actual `/bin/date` before writing: **Sun Oct 25 06:56:37 PDT 2026**. Owner PhysicsPPT44-2. **AUTHOR-WRITTEN CANDIDATE; independent reconstruction and parent disposition absent.** No scientific eval, interpreter, arithmetic program, enumeration, solver or certificate replay was run. Metadata clocks/hashes and source reads only. HOLD v2 and parent errata remain binding.

## 1. Source/criterion freeze, genuinely new subspace and outcome

The prior source/Gram freeze is `three-ME-scalar-source-gram-freeze-v1.json`, SHA-256 `cbad607a9649989e1372f211c452906153b4fffa8f121e7d78b1ecaca2b57bdb`. It records the full-complex simultaneous Gram derivation before this consolidated PPT screen. Informal written leads during scoping are disclosed; it is not represented as preregistration before all reasoning.

The literal new rays are normalized

```
Phi0=vec(I4)/2,
Phi1=vec(Z)/2, Z=diag(1,i,-1,-i),
Phi2=vec(X)/2, X|j>=|j+1 mod4>.
```

The three unitaries are Hilbert–Schmidt orthogonal, and ZX=iXZ. Consequently these rays are orthonormal and their span is a genuine **three-dimensional noncommuting unitary subspace**, not the old two-Bell cyclic plane. With Q=sum_(r=0)^2 P(Phi_r), the family

```
W_lambda=lambda I16-Q, lambda>=0                         (1)
```

has three negative eigenvalues for0<=lambda<1. Inertia therefore distinguishes it from both literal retired one-negative and two-negative classes.

We first derive the exact full-complex rank-two condition. We then analytically screen **all PPT targets**, rather than select one and assume it negative. This yields an exact first obstruction: every two-block-positive member of(1) is completely copositive, so a PPT-negative target cannot exist. The same proof mechanism closes the broader common scalar-completion family with **at most three orthogonal maximally entangled ququart rays and arbitrary nonnegative weights**, as specified below. This is not a theorem about arbitrary rank-three negative parts, arbitrary positive completions, or unrestricted P44.

The first obstruction occurs BEFORE a valid negative PPT target can be chosen; no separable control or unproved state is substituted for the requested SN3 construction.

## 2. Source validity and the inapplicable shortcut

Hou–Li–Poon–Qi–Sze, [primary2015 PDF](https://faculty.sites.iastate.edu/ytpoon/files/inline-files/pmaps_LAA_2015.pdf), Propositions2.2–2.3, gives the Choi/Schmidt-rank characterization and elementary operators with arbitrary positive/negative term counts. That is the source-valid multiple-ray framework, not a published claim that a specific three-ray ququart witness is two-positive or indecomposable. The Gram criterion below is derived directly.

Chruściński–Kossakowski–Sarbicki, [arXiv:0908.1846v2](https://arxiv.org/html/0908.1846v2), SectionII/Theorem1, gives a sufficient spectral condition requiring a STRICT sum of squared k-Schmidt norms below1. In the literal unweighted0<=lambda<1 trial, all three negative eigenrays are ME4, each has squared2-Schmidt norm1/2, and their sum is3/2. The condition is inapplicable, not a positivity certificate. Weighted trials require their actual spectrum to be considered; no borrowed spectral sufficient condition is used anywhere here. SectionIV's rank-one partial-transpose spectrum supports the standard ME bound, which is independently rederived using the swap operator in Section4.

No source theorem is promoted to an unrestricted M4 classification or a promise that the mechanism has positive P44 headroom.

## 3. Full-complex simultaneous Gram condition, derived before PPT testing

Consider the common family

```
Q_p=sum_(r=1)^m p_r P(Phi_r),
Phi_r=vec(U_r)/2,
Tr(U_r*U_s)=4 delta_rs,
0<=m<=3, p_r>=0,
W=lambda I16-Q_p, lambda>=0.                            (2)
```

Let S be ANY complex4 by2 isometry, P=S S*, and define the m bym matrix

```
H_rs(S)=sqrt(p_r p_s)/4 Tr(U_r* P U_s).                  (3)
```

Then the **exact** universal criterion is

```
W is two-block-positive
 iff H(S)<=lambda I_m for EVERY complex4 by2isometry S.   (4)
```

There is no real-plane, finite-grid, chosen-Schmidt-basis or sampled-parameter replacement for this quantifier.

Proof. Every rank-at-most-two coefficient matrix C can be written C=SZ, extending its column space when necessary. Let z_j be the columns of Z. The weighted negative overlaps are

```
h_r=sqrt(p_r)/2 Tr(U_r* C).
```

Put `v_jr=sqrt(p_r)/2 S* U_r e_j` and let V_j have these columns. Then

```
h=sum_j V_j* z_j,
||C||_F^2=||Z||_F^2,
sum_j V_j*V_j=H(S).
```

The exact squared norm of the linear map Z->h is lambda_max(H), as follows either by its Gram matrix or weighted Cauchy–Schwarz. This proves sufficiency in(4). If H has a unit eigenvector v with g>lambda, take `z_j=V_j v`. Then `||Z||_F^2=g`, h=gv, and

```
<vec(C),W vec(C)>=lambda g-g^2=g(lambda-g)<0.
```

Such a C has rank at most two and is nonzero. This proves necessity. The trace form in(3) follows by summing over j, and shows that only the complex plane P matters, not its chosen orthonormal basis. All zero weights cause no difficulty.

## 4. The all-PPT target bound

Let F be the swap operator on C4 tensor C4. Since

```
Phi_U=(U tensor I)(00+11+22+33)/2,
P(Phi_U)^Gamma=(U tensor I) F (U* tensor I)/4,
```

and F<=I, every normalized maximally entangled ray satisfies

```
P(Phi_U)^Gamma<=I16/4.                                 (5)
```

Therefore

```
Q_p^Gamma<=(sum_r p_r) I16/4.                            (6)
```

For any PPT density matrix rho,

```
Tr(Q_p rho)=Tr(Q_p^Gamma rho^Gamma)<=sum_r p_r/4.         (7)
```

This is a uniform screen of the entire PPT cone, not an eigenvalue computation or an untested candidate state. A negative PPT expectation would require

```
lambda<sum_r p_r/4.                                    (8)
```

We now show that the universal rank-two condition forces the OPPOSITE strict inequality, with an explicit gap. No search for a PPT target is justified once that incompatibility is proved.

## 5. Literal three-ray example: an explicit complex rank-two control

For the literal I,Z,X rays, take the plane spanned by e0,e1. Formula(3), with unit weights, gives exactly

```
H=[ 1/2      (1+i)/4   0   ]
  [ (1-i)/4  1/2       0   ]
  [ 0        0         1/2 ].                            (9)
```

The off-diagonal entries involving X vanish because X has zero diagonal, even after multiplication by the diagonal P or Z*P. The other off-diagonal trace is Tr(PZ)=1+i. Hence

```
lambda>=1/2+sqrt2/4=(2+sqrt2)/4                          (10)
```

is necessary for two-block-positivity. This is an exact evaluation of the newly derived universal condition, with the correct complex conjugations.

A Gaussian-rational unnormalized control is also available:

```
C0=diag(1,1+i,0,0), ||C0||_F^2=3.
```

It has rank two. Its normalized overlaps with Phi0 and Phi1 have squared moduli5/12 each; the Phi2 overlap is zero. Thus the normalized vector vec(C0)/sqrt3 has Q-expectation5/6 and W-expectation lambda-5/6. This weaker rational control already forces lambda>=5/6>3/4; it is not a substitute for the full criterion(4), but a valid necessary consequence of it.

For all PPT rho, (7) gives Tr(Qrho)<=3/4. Combining with(10),

```
W^Gamma >= [lambda-3/4] I16
         >= [(sqrt2-1)/4] I16 >0.                       (11)
```

So the literal three-negative mechanism has no PPT-negative target for ANY sound lambda. This first obstruction is exact and predates any need for a solver, enumeration or approximate Schmidt calculation.

## 6. Uniform weighted obstruction for any three orthogonal ME4 rays

The literal example is not the final cutoff. The same scalar-completion mechanism fails for ANY at-most-three orthogonal maximally entangled ququart rays with arbitrary nonnegative weights.

Order the nonzero weights `p1>=p2>=p3>=0`, appending a zero third weight if there are only two rays. If only p1 is nonzero, truncate the first ray's Schmidt decomposition to any two terms and normalize. Its squared overlap with that ME4 ray is1/2, so two-block-positivity gives `lambda>=p1/2`. Equation(6) then yields `W^Gamma>=p1 I16/4>0`. The all-zero case is trivial.

Suppose p2>0. Use local unitaries to put the first ray at vec(I)/2 and diagonalize the relative unitary between the first two rays. Write its eigenvalues eta1,...,eta4. Their moduli are1 and their sum is0 by Hilbert–Schmidt orthogonality. Therefore

```
sum_(i<j) Re(eta_i conj(eta_j))
 = (|sum_i eta_i|^2-4)/2=-2.
```

Among the six unordered pairs there is consequently a pair with

```
Re(eta_i conj(eta_j))>=-1/3.                             (12)
```

This is a written sum/average identity, not a computational census.

Restrict C to the corresponding two diagonal entries in this eigenbasis, with unit Frobenius norm. Such C always has rank at most two. The weighted expectation of the FIRST TWO negative projectors is the Rayleigh quotient of the2 by2 matrix with diagonal entries `(p1+p2)/4` and off-diagonal modulus `|p1+p2 eta_i conj(eta_j)|/4`. Its largest eigenvalue is

```
[p1+p2+|p1+p2 eta_i conj(eta_j)|]/4.
```

The third negative term is nonnegative and can only increase Q_p's expectation. Using(12), universal rank-two positivity thus requires

```
lambda >= [p1+p2+R]/4,
R=sqrt(p1^2+p2^2-(2/3)p1 p2).                            (13)
```

This lower bound is derived from actual rank-at-most-two matrices, not from a spectral sufficient condition for witnesses.

Now

```
R^2-p2^2=p1[p1-(2/3)p2]>0
```

because p1>=p2>0. Hence `R>p2>=p3`. Combining(6) and(13),

```
W^Gamma >= delta I16,
delta=(R-p3)/4>0.                                      (14)
```

This proves the promised whole-mechanism theorem:

> Every two-block-positive scalar completion of a nonzero positive combination of at most THREE mutually orthogonal ME4 projectors is COMPLETELY COPOSITIVE, with the explicit positive margin above. It therefore detects NO4-by4PPT state.

For three unit weights the uniform bound is `lambda>=1/2+1/(2sqrt3)>3/4`; the literal I,Z,X control(10) is stronger for that chosen subspace. The distinction between these two bounds is explicit; no stronger literal constant is claimed uniformly for arbitrary rays.

## 7. Exact remaining gap and what this does NOT retire

This packet settles the first obstruction for a genuinely three-negative-ray noncommuting mechanism. It is a uniform result for the entire stated scalar-completion/at-most-three-ME-ray class, not an inconsequential lambda increment. No PPT-negative state is fabricated after the all-PPT bound rules one out.

The rank count alone is not the theorem: MAXIMAL ENTANGLEMENT, ORTHOGONALITY of the chosen rays, and the SCALAR positive completion are essential hypotheses. This does not close:

- nonmaximally entangled negative rays;
- negative spaces not admitting the required orthogonal ME decomposition;
- four or more subtracted ME rays;
- anisotropic/non-scalar positive completions of these same rays;
- arbitrary two-positive M4 maps or unrestricted P44.

Operationally, any next positive attack using a scalar positive completion and an orthogonal ME negative basis must have at least FOUR relevant rays, or abandon one of these hypotheses. Merely changing the three unitary rays or their weights cannot help if this written theorem is independently reconstructed.

The previously accepted single-Bell D-type and two-Bell cyclic families retain their own v8-qualified histories. x1111 remains retired only by its accepted37-term proof; old21table remains unreconstructed; N4 remains historical UNKNOWN/incomplete, exit unestablished, no retry. None of those artifacts is a proof premise here.

Full P44 acceptance is still UNMET: no different exact rational PPT/SN3 state, arbitrary-positive-completion theorem, or all-state no-go is supplied. Correctness is author-WRITTEN candidate pending genuine cross-domain reconstruction and parent disposition. Formal/kernel, scientific execution/replay, cross-vendor/human and novelty acceptance are not claimed. No GO is requested.
