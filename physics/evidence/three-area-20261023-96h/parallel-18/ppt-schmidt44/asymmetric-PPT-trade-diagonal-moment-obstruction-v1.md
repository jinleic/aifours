# Uniform obstruction for actual J-asymmetric PPT trades against ALL sixteen diagonal-background coefficients

Actual `/bin/date` before writing: **Sun Oct 25 11:08:29 PDT 2026**. PhysicsPPT44-2. **AUTHOR-WRITTEN CANDIDATE; independent cross-domain reconstruction and parent disposition pending.** Continued original P44primary, not a gate return or a scalar-control sweep. No scientific interpreter/eval/arithmetic program, enumeration, solver, replay or compile. Metadata/source/clock/hashonly; HOLD and v9/v10/v11remainbinding. Earlier cadence deviation remains recorded in checkpoint013.

## 1. What is new and what remains unresolved

The live route has arbitrary product-diagonal D with ALL16coefficients and W_D=D-Q, not the already closed two-level/scalar restriction. The actual J-asymmetric family R_x below escapes the previous low-only-noise and two-support-face interfaces. This manuscript proves a uniform obstruction for EVERYx>=0 and EVERY such universally complex-rank-two-nonnegative W_D.

The new proof does not average D or R_xover J. It constructs, for every actual x, a positive conic sum Tof actual rank-two vectors whose PRODUCT-BASIS DIAGONALS fit inside4R_xwhile its Q-overlap is at least that of4R_x. This diagonal-moment comparison is sufficient for the entire D-Qwitness class, but is NOT an operator decomposition of R_xand does NOT prove SN(R_x)<=2. Its exact Schmidt number remains unresolved here; a different witness geometry might still be relevant.

This is not implied by the old scalar swap bound, at-most-three-MEterm theorem, J-invariant-target theorem or the pending face-rigidity lemma. Both x and the sixteen Dentries retain their full ranges; no individual parameter point is substituted for the family.

## 2. Literal data and actual eligible PPT family

Use the accepted four-Weyl Q=sum P(vec(U)/2), U in{I,Z,X,ZX}, with Z|j>=i^j|j>,X|j>=|j+1>, modulo4. H consists of the8product positions of difference0or1; L is the8positions of difference2or3. Q is a rank4projection supported in H. Its partial-transpose blocks, Hposition first, are

```
Q^Gamma_block=(1/4)[2,u;conj(u),0], u=1+i or1-i.
```

The 00/13pair is one such actual block. Set

```
R_x=Q+xP(00)+(1/4)sum_(ell inL,ell!=13)P(ell)
                         +[1/(4+8x)]P(13), x>=0,
tau_x=23/4+x+1/(4+8x), rho_x=R_x/tau_x.                 (1)
```

It is PSD by its literal sum. Its altered PTblock has diagonals1/2+x and1/(4+8x), product1/8 equal to the squared off-diagonal modulus. All other rank1PTblocks remain PSD. Thus rho_xis an exact Gaussian-rational PPTdensity matrix for rational x. For x>0 it is NOT J-invariant and leaves the old support faces. No SN3claim is made merely from those facts.

Work with M_x=4R_xand write

```
y=sqrt(1+2x)>=1, kappa=1/y^2.
```

Its sixteen product-basis diagonals are exactly:

- difference1:2at each of four positions;
- difference0:2at11,22,33and2+4xat00;
- difference3:1at each of four positions;
- difference2:1at02,20,31andkappaat13.

Since Q^2=Q, TrQ=4, Q_(00,00)=1/2and Qhas zero Ldiagonals,

```
Tr(Q M_x)=16+2x.                                      (2)
```

## 3. The diagonal-moment domination lemma

For a coefficient matrix C, let P(C)=P(vec(C)); its vector need not be normalized. Suppose a positive conic sum T=sum_alpha w_alpha P(C_alpha), with w_alpha>=0and each complex C_alphaof rank<=2, satisfies

```
T_(ij,ij)<=M_(ij,ij) for every product positionij,
Tr(QT)>=Tr(QM).                                       (3)
```

Then Tr((D-Q)M)>=0for EVERY nonnegative diagonal Dfor which D-Qis two-block-positive. Indeed

```
Tr((D-Q)M)
 >=Tr(DT)-Tr(QM)
 >=Tr(DT)-Tr(QT)=sum_alpha w_alpha <C_alpha,(D-Q)C_alpha>
 >=0.                                                 (4)
```

Nonnegativity of D is automatic for any two-block-positive D-Q: testing each product basis ket gives d_ij>=Q_(ij,ij)>=0. Thus no candidate diagonal boundary is excluded. This is a universal obstruction deduced from actual rank-two tests, NOT a claim that selected tests suffice to certify an arbitrary W.

Crucial distinction: (3)is a comparison of diagonals and ONEQ-moment. It does NOT assert T=M, T<=M, matching all coherences, PPT of T, or a Schmidt-two decomposition of M. Those stronger conclusions are not used or claimed.

## 4. Actual rank-two atoms and their exact Q-score

For q=0,1and k=0,1,2,3 put ell=k+2,r=k-1,s=k+1and

```
A_k=I-i^(-k)Z,
C_(q,k)(t,z)=X^q[A_k+(t-2)E_(ell,ell)
                   +sqrt2(z E_rs+z^(-1)E_sr)],
t in C, z!=0.                                        (5)
```

The diagonal entries before left multiplication are0at k, t at ell, and1+i,1-iat r,s. The opposite2 by2block has determinant2-2=0and rank1; the isolated tentry has rank<=1. Hence each C has rank<=2 for all indicated complex parameters. Left Xpreserves that rank.

The high part has difference q; its two relevant Q-overlaps have moduli |t+2|/2, and the other two vanish. For q0the traces are t+2and-i^(-k)(t+2), before dividing by2; q1only adds unit phases. The low part has difference2+q and is orthogonal to Q. Therefore the exact score is

```
Tr(Q P(C_(q,k)(t,z)))=|t+2|^2/2.                       (6)
```

Its low squared entries are2|z|^2and2|z|^(-2). The construction uses full complex rank-two matrices; no real-vector sufficiency assertion is present.

Define the fixed four-atom operator

```
T1=(1/4)sum_(k=0)^3 P(C_(1,k)(2,1)).                    (7)
```

Its diagonals are2on all difference1positions and1on all difference3positions, zero elsewhere. Its Q-score is8. These are exactly those eight diagonal resources of M_x, for EVERYx. No phase average or operator-identity claim is needed for this moment statement.

## 5. One exact packing for the ENTIRE smaller-y range

Suppose1<=y<=Y=15/8. Put

```
sigma=1/(2y), e=sigma-1/4=(2-y)/(4y)>0,
B=1+4x=2y^2-1,
v=2sqrt(2-1/y), t=sqrt(B/e).
```

Define a FOUR-atom operator T0 with the following positive weights and literal atom parameters:

| k | weight | t_k | z_k |
|---:|---:|---:|---:|
|0|1/4|2|sqrt(y)|
|1|1/4|v|1|
|2|e|t|1/sqrt(y)|
|3|1/4|v|1|

Here the atom in each row is C_(0,k)(t_k,z_k). Let T=T0+T1. All roots are positive and finite on this closed range; in particular Y<2keeps e>0.

Every product diagonal of Tmatches M_xEXACTLY. The full accounting is:

- 00:the k1,k3nonisolated entries give1, and the k2isolated entry gives e t^2=B, totaling2+4x.
- 22:the k0isolated entry gives1and k1,k3give1, totaling2.
- 11and33:the two k0,k2nonisolated contributions total `1/2+2e=1/y`; the corresponding isolated k1or k3contributes `v^2/4=2-1/y`, totaling2.
- 13:the k0,k2contributions total `(1/2+2e)/y=1/y^2=kappa`.
- 31:they total `(1/2+2e)y=1`.
- 02and20:the k1,k3contributions total1each.
- The remaining eight resources are exactly those of T1in(7).

Using(6), the score is

```
Tr(QT)=13+2x+v+2sqrt(eB).                               (8)
```

For example k0contributes2, k2contributes B/2+2e+2sqrt(eB), and k1,k3together contribute(v+2)^2/4. These plus T1score8reduce exactly to(8).

It remains to prove a UNIVERSAL inequality on the entire interval, not check selected values. Define

```
F(y)=2sqrt(2-1/y)
      +sqrt[(2y^2-1)(2-y)/y]
    =v+2sqrt(eB).                                     (9)
```

Both square-root arguments are positive on[1,Y]. The first inner function has second derivative-2/y^3<0. The second equals `-2y^2+4y+1-2/y`, with second derivative-4-4/y^3<0. Since square root is concave and increasing, both summands and F are concave on this interval.

Now F(1)=3. At Y=15/8,

```
F(Y)=2sqrt(22/15)+sqrt(193/480)>12/5+3/5=3,
```

because22/15>36/25and193/480>9/25. A concave function lies above the chord joining its endpoints, so F(y)>=3for EVERY1<=y<=Y. Consequently(8)gives `Tr(QT)>=16+2x`, proving both requirements of(3)on the whole smaller-y regime.

No approximate logs, derivatives in an interpreter, parameter grid or sampled-positivity inference is used; the two displayed second derivatives and endpoint comparisons are written identities.

## 6. A different exact packing for ALL larger y

For y>=2sqrt2-1define the two diagonal rank-two matrices

```
D01=diag(sqrt(2+4x),1+i,0,0),
D23=diag(0,0,sqrt2,1+i),
T=T1+P(D01)+P(D23).                                    (10)
```

Their diagonals fill exactly the four difference0resources of M_x; T1fills the difference1and3resources. No difference2resource is consumed, so all sixteen inequalities of(3)hold. In this regime they are inequalities, not a hidden full operator equality.

The complex phases1+ialign the adjacent Qcoherences. Direct overlap calculation gives

```
Tr(QP(D01))=2+2x+sqrt2 y,
Tr(QP(D23))=2+sqrt2,
Tr(QT)=12+2x+sqrt2(y+1).                                (11)
```

For instance the I,Ztrace moduli of D01are equal to the modulus of sqrt(2+4x)+1+i; the shifted-ray traces vanish. Equation(11)is at least16+2xexactly when y>=2sqrt2-1. Thus(3)holds for this ENTIREunbounded regime.

The two constructions cover ALLy>=1. Indeed

```
2sqrt2-1<15/8,
```

because `(23/8)^2=529/64>8`. Use Section5for y<=15/8and Section6for y>15/8. There is no uncovered intermediate range and no finite cutoff.

## 7. Whole-family theorem for all sixteen diagonal coefficients

For every x>=0, Sections5–6construct a finite positive conic sum of actual complex rank-two projectors obeying(3)for M_x. The domination lemma therefore proves

```
Tr((D-Q)R_x)>=0
```

for EVERY product-diagonal Dsuch that D-Qis universally complex-rank-two nonnegative. This includes all sixteen independent nonnegative coefficients and zero boundaries. Normalizing R_xby tau_xdoes not change the sign.

The same theorem covers every one of the EIGHTactual single-pair PPTtrades obtained by conjugating with powers of J=(X tensorI)SWAP. Jfixes Q, preserves Schmidt rank/PPTand permutes product positions; conjugating a diagonal Dproduces another diagonal D. Thus a hypothetical negative pair on any translated trade would produce a forbidden negative pair on the base R_x. No J-invariance of the target is assumed or imposed.

This is not a new characterization of all two-positive D. It is a uniform no-separation theorem for the specified genuinely asymmetric PPTtarget family, proved by necessary rank-two expectations. It does NOT prove those states have Schmidt number<=2against arbitrary witness geometry.

## 8. Genuine remaining primary residual, not a round finish

The actual single-pair trade is now excluded within the FULLdiagonal-background route if this proof is reconstructed. It cannot be promoted as an SN3candidate on the strength of its PPTproperty and symmetry escape alone. The eight-term constructions are certificates of diagonal/Qmoment domination, not Schmidt decompositions of rho_x.

The first unproved diagonal-background step is now SIMULTANEOUS genuinely asymmetric changes across multiple PTpairs and/or general nontrivial high/low coherences in the four complex PPTblocks. The entire system remains:

- actual16-entry Dand all-plane inverse-Gram positivity;
- all four R^(q)>=0and all four partial-transpose blocks `S^(tau)_rs=R^(r+s-tau)_rs>=0` with trace1;
- the same eight coupled rank-two completion inequalities;
- negative exact original expectation and a target outside the already closed symmetry/face/single-trade families.

No pairwise packing may be summed as though the same diagonal resources were available independently for each trade. For minimal simultaneous trades the low-noise coefficients are nonlinear functions of their OWN high noises; convex mixtures of one-trade states do not automatically reproduce them. This is an exact new compatibility gap, not permission to discard the multi-pair residual or claim the full diagonal-background class closed.

Other negative geometries and non-diagonal positive completions remain outside even that route. Unrestricted P44is unsolved here. The owner continues primary research rather than treating this theorem or its review as completion of the96-hour request.

All mathematical statements are author-WRITTEN candidates pending genuine cross-domain reconstruction and parent pass. No SOTA/novelty, formal/kernel, human/cross-vendor, executable-certificate or GOclaim. Old accepted sources, old21tableunreconstructed status and N4historicalUNKNOWN/exit-unestablished record are unchanged; no rerun occurred.
