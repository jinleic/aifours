# Unequal actual Weyl coherences with arbitrary low-only PPT completion: an exact sixteen-term Schmidt-two theorem

Actual `/bin/date` before writing: **Sun Oct 25 11:47:44 PDT 2026**. PhysicsPPT44-2. **AUTHOR-WRITTEN CANDIDATE; cross-domain reconstruction and parent disposition pending.** Continued original P44primary at genuinely changed coherent blocks. No scientific interpreter/eval/arithmetic program, enumeration, solver, replay or compile; source/clock/hashmetadataonly. V9/v10/v11and HOLD remain binding; the older cadence miss remains recorded in checkpoint013.

## 1. New target geometry and why the last constructor obstruction does not apply

Use normalized Phi_U=vec(U)/2 for U=I,Z,X,ZX, with Z|j>=i^j|j>,X|j>=|j+1>, modulo4. Set

```
Q0=P(Phi_I)+P(Phi_Z),
Q1=P(Phi_X)+P(Phi_ZX), Q=Q0+Q1,
L0=sum_(i-j=2)P(ij), L1=sum_(i-j=3)P(ij).
```

Q0andQ1are orthogonal rank2projections; L0,L1are orthogonal rank4product-basis projections. The genuinely new coherent family is

```
R_t=Q0+tQ1+(t^2/4)L0+(1/(4t))L1, t>0.                  (1)
```

For t!=1, no common kappaQplus product-diagonal noise can equal R_t: its nonzero off-diagonal entries in the difference0and1blocks have different coefficients1and t, and diagonal noise cannot alter either. It is therefore outside the exact hypothesis of the previous global diagonal-noise theorem. Also J=(X tensorI)SWAP sends R_tto tR_(1/t), so its normalized state is genuinely J-asymmetric unless t=1. No illicit Javerage is used.

The outcome is nevertheless a WHOLE-family obstruction, stronger than witness-specific non-detection: every normalized R_thas Schmidt number at most2by an explicit sixteen-term convex decomposition. It also proves the entire unequal-coherent, eight-independent-low-noise PPTcompletion class is Schmidt-two. This is not an attractive PPTcontrol presented without a separator; the exact rank-two decomposition rules out every universally rank-two-nonnegative separator for this class.

The proof does not use the previous single-trade packing or global resource no-go as an import, and does not retroactively broaden their scopes. No SOTAor novelty claim is made.

## 2. Exact PPT interface and normalization first

The coherent matrix entries of Q_qforq=0,1are

```
(Q_q)_(r,r-q;s,s-q)=(1+i^(r-s))/4.                       (2)
```

Diagonal entries are1/2, opposite coherent entries vanish, and adjacent coherent entries have modulus sqrt2/4. Partial transpose of an adjacent Q0coherence pairs a high difference1position with a low difference3position; an adjacent Q1coherence pairs a high difference0position with a low difference2position. Thus for general coefficients c0,c1and low diagonals y,zthe actual PTblocks, high first, are

```
[c0/2,c1 u/4;c1 conj(u)/4,y] on difference0/2pairs,
[c1/2,c0 u/4;c0 conj(u)/4,z] on difference1/3pairs,
|u|^2=2.                                               (3)
```

These are eight disjoint2 by2blocks, with every physical basis position accounted for. No matrix entries outside those blocks occur.

For(1), c0=1,c1=t,y=t^2/4,z=1/(4t). Both determinants in(3)are exactly0with positive diagonals. R_tis also PSD by its literal sum, hence is PPT. Its trace is

```
N_t=2+2t+t^2+1/t>0,
rho_t=R_t/N_t.                                         (4)
```

All entries of rho_tare Gaussian rational for rational t. Its rank is12and its PT rank8for every t>0. No numerical calculation is needed for those ranks: four positive coherent ray directions and eight positive product positions are orthogonal; each of the eight PTblocks has rank1.

## 3. A single actual rank-two matrix for EVERY positive t

Define positive real numbers

```
a=1/sqrt2,
g=sqrt(t/2),
s=1/sqrt(2t),
r=t/sqrt2,
```

and the literal coefficient matrix

```
C_t=[a s 0 g]
    [g a 0 r]
    [0 g a s]
    [0 r g a].                                        (5)
```

Its second row is sqrt(t)times its first; its fourth row is sqrt(t)times its third. The first and third rows are independent (their00and22coordinates witness this). Hence rank(C_t)=2over the full complex field. Its squared Frobenius norm is exactly

```
4a^2+4g^2+2r^2+2s^2=2+2t+t^2+1/t=N_t.                 (6)
```

Its four difference components are

```
q0: aI,
q1: gX,
q2: r(E13+E31),
q3: s(E01+E23).                                        (7)
```

In particular the high part is a genuine combination of the IandXrays; the two-sector coherence is retained rather than eliminated by an imposed single-ray support ansatz.

## 4. Three exact finite LOCAL operations give the whole operator identity

For n=0,1,2,3, e=0,1and k=0,1define

```
C_(n,e,k)=X^k Z^e (Z^n C_t Z^(-n)) X^(-k).             (8)
```

Each operation is an actual local unitary on vectorized coefficient matrices:

- C->Z^n C Z^(-n) is Z^n tensor conjugate(Z^n);
- C->Z^e C is Z^e tensorI;
- C->X^k C X^(-k) is X^k tensorX^k.

Thus every one of the sixteen matrices in(8)has rank2and squared norm N_t. No sampled-vector argument is used; the following finite averages DEFINE the exact decomposition.

First average over n. A coefficient matrix entry of difference qacquires character i^(nq). The four differences in(7)are distinct modulo4, so ALLcross groups cancel, leaving

```
a^2 P(vecI)+g^2 P(vecX)
 +r^2 P(vec(E13+E31))+s^2 P(vec(E01+E23)).               (9)
```

Next average the left multiplication by Z^eover e0,1. The two high terms become

```
(a^2/2)[P(vecI)+P(vecZ)]=Q0,
(g^2/2)[P(vecX)+P(vecZX)]=tQ1.                          (10)
```

The low opposite-position cross terms cancel as well: on E13,E31leftZmultipliers are i,-i, and on E01,E23they are1,-1. The result after these first eight transformations is exactly

```
Q0+tQ1+r^2[P13+P31]+s^2[P01+P23].                       (11)
```

Finally average joint Xconjugation for k0,1. Both Q0andQ1are invariant: I,Xstay fixed, while ZandZXonly acquire a unit phase. The two low positions13,31move to20,02, and01,23move to12,30. Hence (11)becomes

```
Q0+tQ1+(r^2/2)L0+(s^2/2)L1=R_t.                        (12)
```

Equations(9)–(12)account for every coefficient group of the FULLoperator sum. Therefore

```
R_t=(1/16)sum_(n,e,k)P(vec C_(n,e,k)),
rho_t=(1/16)sum_(n,e,k)P(vec C_(n,e,k)/sqrt(N_t)).       (13)
```

All sixteen vectors in the second identity have unit norm and complex Schmidt rank2. All sixteen convex weights are exactly1/16. There is no hidden finite coefficient table, optimizer output, approximate entropy or unadmitted arithmetic premise.

This proves SN(rho_t)<=2for the ENTIREunbounded range t>0. It does not assert separability or a matching entanglement lower bound. At t1the operator agrees with the older rho6source, but this proof's goal is the whole unequal-coherence family, not recertifying that old input.

## 5. Full unequal-coherent low-only completion theorem

Let c0,c1>=0and consider

```
R=c0Q0+c1Q1+sum_(ell inL0)y_ell P(ell)
                         +sum_(ell inL1)z_ell P(ell),
y_ell,z_ell>=0, no additional Hnoise.                   (14)
```

For c0,c1>0, the complete PPTcriterion from(3)is

```
y_ell>=c1^2/(4c0) for EACHof the four L0positions,
z_ell>=c0^2/(4c1) for EACHof the four L1positions.        (15)
```

The minimal operator is exactly c0R_(c1/c0), with the rank-two decomposition(13). Subtracting it from(14)leaves only nonnegative product-projector noise. Thus every PPToperator in(14), after positive-trace normalization, has Schmidt number at most2for ALLtwo coherent coefficients and ALLeight independent low noises.

If c0=0andc1>0, a difference0/2PTblock has zero high diagonal and a nonzero off-diagonal, so no finite ycan make it PSD. The c1=0,c0>0case is symmetric. If both vanish, the operator is product-diagonal and separable; the zero operator is simply omitted when discussing density normalization. These cases avoid all division-by-zero and limiting ambiguity.

## 6. Universal separator consequence and exact next primary gap

For ANY Hermitian Wnonnegative on EVERYcomplex SR<=2vector, every term of(13)is nonnegative. Equations(13)–(15)therefore forbid Tr(WR)<0for this whole state constructor, regardless of whether W's positive background is diagonal, anisotropic, or unrelated to Q. This is not finite testing promoted into positivity: the explicit STATEdecomposition discharges the universal witness implication by linearity.

The newly live mixed case is

```
R=c0Q0+c1Q1+sum_H x_hP(h)+sum_L y_ellP(ell),
c0!=c1, x_h>=0,
```

with lowered low compensators allowed by the actual PPTconditions

```
(c0/2+x_h)y_ell>=c1^2/8 on type0/2pairs,
(c1/2+x_h)y_ell>=c0^2/8 on type1/3pairs.                 (16)
```

This is NOTcovered by the previous common-scaled-Qglobal moment obstruction when c0!=c1, and it is NOTcovered by(14)because some low diagonals can be below(15). The two prior closures cannot simply be composed: their coherent amplitudes and nonlinear PTcompensators are shared physical data. No arbitrary mixture is silently treated as realizing the exact minimal noises.

**First unproved step:** actual positive16-entry D(or a genuinely different non-diagonal background)with the FULLall-complex SR2criterion and negative expectation on an ACTUALPPTmixed-case target, or a uniform obstruction retaining all coupled coefficients and all eight PTblocks. General four-complex-block PPTstates remain still further outside this constructor. No such positive separator, SN3state or all-state no-go is claimed.

The owner continues original primary research at that mixed coherence/noise interface. No more low-only target controls are warranted if the theorem is independently reconstructed. Existing accepted sources retain exact scope; parent-supplied leads and the earlier cadence deviation remain disclosed. No formal/kernel, executable-certificate, human/cross-vendor, novelty/SOTAorpublication acceptance follows. No new scientific GOis requested.
