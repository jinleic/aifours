# Generic upper-zero operator mechanism: observable graph norm and a weighted Korn comparison

Actual clock observed before writing: **2026-10-24T05:53:55-07:00**, `/bin/date -Iseconds`. Owner PhysicsResearch96h. This is not an uninterrupted-activity attestation.

**NEW CANDIDATE written operator identities and one invalid-certificate obstruction.** No scientific program, arithmetic interpreter, CAS, import, compile/test, enumeration, solver, model CLI or nested agent was used. No GO exists.

## 1. Same unrestricted target; parent scope consumed

The active problem is still ONLY generic `Z_up(c)>=0` for every normalized four-component Schmidt vector and every complex q-plus six-vector. No selected reference family is introduced as its replacement.

The complete actual parent disposition, including untruncated lines9/17, and its complete59-line binding receipt were read:

- RUN/wave-v17-werner-parent-disposition-v1.md, observed SHA256 **`1b85107d54127373d0a05c0d73dff0e71a741ee83fd5151e52d1e291692c0184`**;
- RUN/peer-review-wave-eighteen-v17-werner-receipt-v1.json, observed SHA256 **`38128308a4a478b9abeebbee4322693a0522867809183a122df9befedce215b0`**.

RUN is `institute/runs/three-area-2026-10-23-96h/`. These support the old generic incidence001/002 identities and the complete complex1+3 comparison at their stated written level. They do not prove any unrestricted final sign. The correct endpoint label is NON-STRICT physical extension, not strictness through a singular inverse. All evidence-v4 and earlier overlays remain operative.

Before this new attack, Main was ACKed with the first operator input: the exact graph norm from supported(S1) and coupling from supported(S2), with the dual lift tested only on its OBSERVABLE feature range. The purpose below is a genuine arbitrary-spectrum operator mechanism, not another symmetric-family calculation.

## 2. Spaces and supported identities

For now take all c_i>0, real, `sum c_i^2=1`. Set

```
x_i=c_i^2, d_i=1-x_i, D=diag(d_i),
d_ij=(d_i+d_j)/2>=1/2,
P=cc^T, Q=I-P,
r=1/sum_i1/d_i.
```

Let E be the COMPLEX transpose-symmetric zero-diagonal four-matrices, dimension6. Let H be the p quotient matrices Z with `Zc=0`, dimension12. All inner products are Hermitian Hilbert–Schmidt products; transpose-symmetric does not mean Hermitian or real.

On H the supported actual row operator is

```
B'Z=D^2 Z-D diag(Z_ii)Q,
rho'Z=B'Z+r Q Z^T Q.
```

B' equals `D_out^2 P_B`; D_out commutes with the row-space projectors P_B and P_T. T is the four-dimensional kernel frame from incidence001. This commutation follows row by row and is not an assumed simultaneous diagonalization of rho'.

For U in E, put `V=UQ`, `F=L_D U=(DU+UD)/2`. The actual filtered p/q coupling and comparison energy are

```
h_c(U)=-(D_out+B')V/(2sqrt(2)),
R0(U)=(||F||_HS^2+||D^(1/2)V||_HS^2)/4.       (G1)
```

The exact physical target is `Cost_p(U)<=Qraw(U)`. The stronger `Cost_p(U)<=R0(U)` is still only a sufficient conjectured comparison. The entire positive remainder of incidence002 remains available if that stronger bound fails.

## 3. The exact six-edge observable graph kernel

L_D is invertible on E: it multiplies edge i,j by d_ij. Define

```
A_c F=D^(1/2)(L_D^(-1)F)Q,
K_c=I_E+A_c^dagger A_c.
```

Then

```
R0(U)=<F,K_c F>_HS/4.                         (G2)
```

In the six edge coordinates (matrix entries F_ij, i<j), the actual kernel has the remarkably simple entries

```
(K_c)_(ij,ij)=1+d_i d_j/d_ij^2,
(K_c)_(ij,it)=-d_i c_j c_t/(2d_ij d_it),
(K_c)_(ij,kt)=0 for disjoint edges.            (G3)
```

Every shared-edge entry is present. To derive them, with U=L_D^(-1)F and b=Uc, the adjoint gives

```
A_c^dagger A_c F
 =L_D^(-1) SymOff(D UQ),
(SymOff(D UQ))_ij=d_ij U_ij-(d_i b_i c_j+d_j b_j c_i)/2.
```

The diagonal subtraction simplifies through

```
d_i x_j+d_j x_i=2d_ij-2d_i d_j,
```

giving the first line of(G3). The adjacency term gives the second. SymOff is the orthogonal projection onto complex transpose-symmetric zero-diagonal matrices.

K_c is positive with

```
I<=K_c<=3I.                                  (G4)
```

Indeed Q is an orthoprojection and

```
||A_cF||^2<=||D^(1/2)U||^2
 =2sum_edges d_ij|U_ij|^2
 <=2||F||^2,
```

since d_ij>=1/2. Thus this kernel has NO small-pivot or rank-boundary inversion difficulty. Its off-diagonal entries are nonpositive. It is therefore a symmetric positive Stieltjes matrix, with entrywise nonnegative inverse. One direct justification: write K=Delta-N, Delta positive diagonal and N entrywise nonnegative. Positivity of K implies the Perron eigenvalue of Delta^(-1/2)NDelta^(-1/2) is less than1; its convergent Neumann series gives the nonnegative inverse. This is an exact operator statement, not a sampled inverse-sign observation.

## 4. Reverse Schur form with an explicit generic forcing

For ANY complex p test Z in H define the symmetric zero-diagonal matrix

```
J_c(Z)=L_D^(-1) SymOff[(D_out+B')Z].
```

Its edge entries are explicitly

```
j_ij=[d_i(1+d_i)Z_ij+d_j(1+d_j)Z_ji
       +c_i c_j(d_i Z_ii+d_j Z_jj)]/(d_i+d_j). (G5)
```

No p test has been assumed symmetric, normal or real. Pairing with the full coupling gives

```
<Z,h_c(U)>=-sum_edges conj(j_ij)F_ij/sqrt(2).
```

Here the factor is important: HS products count an unordered symmetric edge twice, whereas F_ij are unnormalized entries. Thus minimization of the full joint quadratic over all six F entries is exactly

```
min_F { <Z,rho'Z> -sqrt(2)Re(j^dagger F)
                     +(1/2)F^dagger K_c F }
 =<Z,rho'Z>-j^dagger K_c^(-1)j.               (G6)
```

Consequently the GENERIC stronger comparison is equivalent to the arbitrary-spectrum operator inequality

```
j_c(Z)^dagger K_c^(-1)j_c(Z)<=<Z,rho'Z>
for every Zc=0.                              (G7)
```

G7 is **UNPROVED**. Equivalence is not a certificate for its sign. Its advantages are a uniformly regular six-edge kernel, a genuine graph Green operator, and completely explicit forcing, rather than twelve-dimensional inverse entries. For the exact Qraw target one adds its full positive remainder to the q kernel before taking the inverse; a failed G7 alone cannot be a negative Z_up or W4 witness.

## 5. Polynomial ground-state transform and the exact directed-row energy

On the positive interior choose positive edge weights

```
w_ij=c_i c_j d_ij,
g_ij=d_ij-(d_i-d_j)^2/4
    =d_ij(1-d_ij)+d_i d_j,
m_ij=x_i x_j g_ij,
gamma_(i;jt)=d_i x_i x_j x_t/2, j<t, j,t!=i.
```

The off-diagonal weight of -K between edges ij and it, multiplied by w_ij w_it, is EXACTLY gamma_(i;jt). Also

```
(Kw)_ij/w_ij=(1-d_ij)/d_ij+d_i d_j/d_ij^2,
((Kw)_ij/w_ij) w_ij^2=m_ij.
```

Therefore, for arbitrary complex edge potentials z,

```
(wz)^dagger K_c(wz)
 =sum_edges m_ij|z_ij|^2
  +sum_i sum_(j<t; j,t!=i) gamma_(i;jt)|z_ij-z_it|^2.   (G8)
```

These are POLYNOMIAL physical weights in x. In particular no hidden inverse of c appears in them. The change of coordinates using w is only asserted on the positive interior. Positivity of g is also regular: with u=d_ij in[1/2,1] and |d_i-d_j|<=2(1-u),

```
g_ij>=u-(1-u)^2>=1/4.
```

For a p test Z introduce directed variables

```
T_ij=Z_ij/(c_i c_j), including the diagonal.
```

Then Zc=0 is precisely `sum_j x_j T_ij=0` for every row. The whole B' energy has the exact weighted-variance formula

```
<Z,B'Z>
 =sum_i sum_(j<t; j,t!=i)d_i x_i x_j x_t|T_ij-T_it|^2
 =2 Gamma(T),                                 (G9)
```

where Gamma denotes the gamma-weighted central-row difference form in(G8), extended to directed arrays. Derivation: rowwise elimination of T_ii gives

```
x_i d_i[d_i sum_(j!=i)x_j|T_ij|^2
             -|sum_(j!=i)x_j T_ij|^2],
```

and weighted Lagrange/variance expands this into(G9). All complex cross terms are retained. Also

```
<Z,Q Z^T Q>=sum_(i,j)conj(Z_ij)Z_ji,           (G10)
```

because Zc=0. This last real quadratic is not incorrectly assumed nonnegative; its skew part is exactly the known Hodge difficulty.

## 6. Exact completion of squares and ONE new full-spectrum sufficient operator inequality

Write U_ij=c_i c_j z_ij, z_ij=z_ji, z_ii=0, and define

```
e_ij(Z)=x_i x_j[d_i T_ij+d_j T_ji]
       =c_i c_j[d_i Z_ij+d_j Z_ji].
```

The row centering in UQ cancels in its B' differences and in its pairing with Z. Consequently the full p/q cross has the exact expression

```
2Re<Z,h_c(U)>
 =-sqrt(2)Re Gamma(T,z)
  -(1/sqrt(2))Re sum_edges conj(e_ij(Z))z_ij.   (G11)
```

For clarity, the B' bilinear pairing is `2Gamma(T,z)` and the D_out pairing is `sum conj(e_ij)z_ij`; their common coefficient is -1/sqrt(2), as follows directly from(G1).

Combining(G8)-(G11), the ENTIRE stronger joint quadratic has the exact identity

```
<Z,rho'Z>+2Re<Z,h_c(U)>+R0(U)
 =P_c(Z)
  +(1/2)Gamma(z-sqrt(2)T)
  +(1/2)sum_edges m_ij
         |z_ij-e_ij(Z)/(sqrt(2)m_ij)|^2,       (G12)

P_c(Z)=<Z,(B'/2+r F_Q)Z>
       -sum_edges |d_i Z_ij+d_j Z_ji|^2/(4g_ij),
F_Q Z=Q Z^T Q.
```

This is a generic operator completion of squares, not a reference-family representation. The two squares have DIFFERENT centers and neither may be silently set to zero together with the other. For example the Gamma completion is

```
2Gamma(T)-sqrt(2)ReGamma(T,z)+(1/2)Gamma(z)
 =Gamma(T)+(1/2)Gamma(z-sqrt(2)T),
```

and the edge-mass completion subtracts `|e_ij|^2/(4m_ij)`, which is exactly the term in P_c after canceling x_i x_j.

Thus a concrete **genuinely full-spectrum** sufficient inequality is

```
P_c(Z)>=0 for every complex Zc=0.             (G13)
```

G13 is **UNPROVED**, and is stronger than what G12 requires. Its left first operator is already positive from the supported Hodge estimate:

```
B'/2+rF_Q=(B'/2-rP_a)+rP_s>=0.
```

The new challenge is its domination of the explicit weighted symmetric off-diagonal row form, not an unjustified positivity of F_Q. Proving G13 would prove the unrestricted stronger R0 comparison and hence generic upper Z_up. A negative P_c would only refute THIS sufficient Korn-type estimate; it would not refute G7, the R0 comparison, Z_up or W4, because BOTH nonnegative squares in G12 still remain. The exact Qraw remainder is retained beyond that.

## 7. A valid but overstrong bare dual lift actually fails at generic spectra

This obstruction explains why the observable range in the initial ACK is essential. Let the feature map be

```
G U=(L_D U,D^(1/2)UQ)/2.
```

A simple exact dual lift of h is

```
W_bare Z=-(1/sqrt(2))(
 L_D^(-1)SymOff[(B'+D_out P_T)Z],
 D^(1/2)P_B Z).
```

It really satisfies `<W_bare Z,GU>=<Z,h_c(U)>` by D_out commuting with the row projectors and by Zc=0. However the sufficient assertion

```
||W_bare Z||^2<=<Z,rho'Z>
```

is FALSE. This is not a negative R0 or Z_up direction.

For a written generic perturbation let

```
x_i(epsilon)=1/4+epsilon delta_i,
delta=(3,1,-1,-3),
c_i(epsilon)=sqrt(x_i(epsilon)),
v0=(0,0,1,-1)/sqrt(2),
v(epsilon)=Q(epsilon)v0,
K(epsilon)=star(c(epsilon) wedge v(epsilon)).
```

For every sufficiently small epsilon>0, all FOUR Schmidt squares are positive and DISTINCT; K is a skew-transpose p vector with Kc=0. No selected positive reference-family theorem is inferred from this perturbation. Its Hodge row norms are `d_i||v||^2-|v_i|^2`, with `||K||^2=2||v||^2`.

Since P_B K=K, P_T K=0 and B'K=D^2K,

```
< K,rho'K >-||W_bare K||^2
 =<K,(D_out^2-D_out/2)K>-r||K||^2
  -(1/2)||L_D^(-1)SymOff(D^2K)||^2.            (G14)
```

At epsilon=0, d_i=3/4 and r=3/16, so the first operator difference vanishes. Also SymOff(D^2K)=0 there. The derivative r'(0)=0 since sum delta_i=0, and the norm-square term is O(epsilon^2). The exact first derivative is

```
-sum_i delta_i[(3/4)||v0||^2-|v0_i|^2]
 =sum_i delta_i|v0_i|^2=-2.
```

Therefore the contractivity defect in(G14) is `-2epsilon+O(epsilon^2)<0` for every sufficiently small positive epsilon. This rigorously excludes the bare lift as a universal certificate, even arbitrarily close to the uniform point. It does not produce any admissible negative Werner coefficient operator.

The minimum-norm observable lift is instead the projection of W_bare onto ran G. Its exact squared norm is `j^dagger K_c^(-1)j`, so it returns to(G7), not to the false bare assertion. At uniform the bare skew second feature is orthogonal to the observable graph range; projecting it out removes this spurious obstruction. No claim that the resulting observable lift is globally contractive has been made.

## 8. Actual new frontier

The new attack is now a fully explicit weighted line-graph / directed-row operator mechanism valid for ARBITRARY positive four-spectra and ALL complex p/q tests. Its useful quantities are the regular Stieltjes kernel K_c, polynomial masses/conductances, exact p row variance, and the full completion(G12). No selected-family sampling, local-equality theorem or unproved symmetry reduction was used.

The exact target remains `Cost_p<=Qraw`, with its FULL positive remainder retained. G7 is equivalent only to the stronger R0 comparison. The still stronger G13 offers ONE concrete general operator estimate to attack; neither it, G7, nor generic Z_up is proved here. The three other final residual signs and W4 remain open. The new identities and bare-lift obstruction require actual independent reconstruction before promotion. There was no scientific execution, CLI/model fallback, nested delegation, shared-index edit or alteration of any frozen earlier evidence.
