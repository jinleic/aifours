# Actual asymmetric PPT-face obstruction for the Weyl background route

Actual `/bin/date` before writing: **Sun Oct 25 10:45:35 PDT 2026**. Owner PhysicsPPT44-2. **AUTHOR-WRITTEN CANDIDATE; independent reconstruction absent.** This is additive continued PRIMARY research after the anisotropic manuscript was sent for review, not a gate return or another scalar control. No scientific eval/interpreter/arithmetic program, enumeration, solver or replay. V9/v10/v11 and HOLD remain binding; checkpoint013's cadence deviation remains disclosed.

## 1. Goal and exact statement

The live arbitrary-D route is `W(D)=sum d_ijP(ij)-Q` with16independent coefficients and the full complex rank-two inverse-Gram condition. Its tested states may be twirled losslessly by Z tensor conjugate(Z), but NOT by the extra eight-swap symmetry unless the actual target is invariant.

This note proves that trying to break that target symmetry INSIDE the particular natural PPTface is impossible. It does not assume J-invariance of the target.

Use the accepted Q onto normalized I,Z,X,ZX rays, H the difference0/1positions and L its complement. Define the unnormalized PPToperator

```
R*=Q+L/4, Tr(R*)=6.                                    (1)
```

Its rank is12; its Bob partial transpose has eight rank1blocks. These facts follow directly from the accepted T=Q^Gamma table: in each H/Lordered block,

```
(R*)^Gamma=(1/4)[2,u;conj(u),1]
            =(1/4)P((u,1)), u=1+i or1-i.                (2)
```

**Theorem.** Let R be Hermitian and invariant under Z tensor conjugate(Z). Suppose

```
Ran(R) subset Ran(R*),
Ran(R^Gamma) subset Ran((R*)^Gamma).                     (3)
```

Then R=tR* for a real scalar t. If R>=0, t>=0. In particular the normalized circulant PPTface specified by these two ACTUAL support inclusions contains only R*/6. No nontrivial J-asymmetric PPTtarget exists in that face.

The proof does not import the unreviewed32-term Schmidt-two decomposition from the previous manuscript. It uses only the literal projection range and rank1partial-transpose support data, and rederives every block relation below. It is not a claim that the full untwirled PPTface is one-dimensional.

## 2. All complex block variables are retained

Write indices modulo4, zeta=i. By the actual Zsymmetry,

```
R=sum_(q=0)^3 sum_(r,s) R^(q)_rs |r,r-q><s,s-q|.          (4)
```

The four R^(q)are arbitrary Hermitian4 by4matrices before imposing(3). Partial transpose has total-index sectors tau, with exact entries

```
S^(tau)_rs=R^(r+s-tau)_rs.                              (5)
```

Indeed the original entry becomes `|r,s-q><s,r-q|`, whose total index is tau=r+s-q. This is an entrywise identity, not a count or numerical elimination.

Let F be the4 by2isometry with row r equal to `(1,zeta^r)/2`, and put B=FF*, so `B_rs=(1+zeta^(r-s))/4`. The first support inclusion says

```
R^(0)=F A F*, R^(1)=F C F*,
A=[a,z;conj(z),b], C=[c,w;conj(w),d],                   (6)
```

with a,b,c,d real and z,w complex. The low blocks R^(2),R^(3)remain unrestricted Hermitian at this point. No diagonal/equal-weight assumption about A,C has been inserted.

## 3. Eight actual within-pair relations force the high blocks to be scalar

For a rank1partial-transpose block(2), the range is spanned by `(u,1)`. Any Hermitian matrix satisfying the second inclusion(3) obeys the corresponding column/row proportionalities, including cross-block entries. In particular its within-pair high/low relations are

```
S_hl=u S_ll, S_hh=2S_ll,
hence S_hl=(u/2)S_hh.                                 (7)
```

Using the actual eight block pairs from the accepted total-index table, (5) and(7) give, for EVERY r=0,1,2,3,

```
R^(1)_(r,r+1)=(1-i)R^(0)_(r,r)/2,
R^(0)_(r,r-1)=(1+i)R^(1)_(r,r)/2.                       (8)
```

For example the tau0pair00/13 gives the first relation at r0; the tau2pair11/20 gives it at r1; the other two come from22/31 and33/02. The second row of(8)comes from the high difference1positions03,10,21,32 paired with30,01,12,23. These are physical high/low positions, not an arbitrary orientation convention.

Now substitute(6). Multiplying by4,

```
4R^(1)_(r,r+1)=c-id-iw zeta^(-r)+conj(w)zeta^r,
4R^(0)_(r,r)=a+b+z zeta^(-r)+conj(z)zeta^r.
```

The three characters1,zeta^r,zeta^(-r)are distinct on C4. Equality in the first row of(8)therefore gives

```
c=d=(a+b)/2,
w=(1+i)z/2.                                            (9)
```

Likewise

```
4R^(0)_(r,r-1)=a+ib+iz zeta^(-r)+conj(z)zeta^r,
4R^(1)_(r,r)=c+d+w zeta^(-r)+conj(w)zeta^r.
```

The second row of(8)gives

```
a=b=(c+d)/2,
z=(1-i)w/2.                                            (10)
```

Combining the two off-diagonal equations yields `z=((1-i)(1+i)/4)z=z/2`, hence z=w=0. The real diagonal equations then give a=b=c=d=t. Thus

```
R^(0)=R^(1)=tB.                                        (11)
```

All phases and the factor1/2are essential here. No trace-zero, diagonal-A assumption, positive-weight census or interpreter was used.

## 4. The remaining low blocks are forced, not left as a hidden residual

Every total-index sector contains two high/low rank1pairs. The two LOW indices in that sector differ by2. Their off-diagonal Sentry, by(5), comes from the OPPOSITE entry of one of the high blocks R^(0)orR^(1): when tau is even it is q0, and when tau is odd it is q1. Equation(11)and `B_(r,r+2)=0` show that this low/low cross-pair entry vanishes.

On the two-dimensional range of the sector's two rank1pair vectors, the low/low2 by2submatrix determines the entire Ssector: each high row/column is the fixed u multiple of its low partner. A zero low/low cross entry therefore makes ALLcross-pair entries zero, including high/high and high/low cross entries.

The diagonal relation in(7)then makes every low diagonal t/4, because every corresponding high diagonal is t/2. Finally, EVERY off-diagonal entry of R^(2)orR^(3)is one of those zero cross-pair Sentries: if its two rindices differ by1or3, it is a cross-pair high/low entry; if they differ by2, it is a cross-pair high/high entry. A within-pair off-diagonal is always one of the HIGHq0/q1entries in(8), never a lowq2/q3entry.

Consequently

```
R^(2)=R^(3)=(t/4)I4.                                  (12)
```

Equations(11)and(12)reconstruct the entire16 by16operator as t(Q+L/4)=tR*. Hermiticity made t real; if R>=0 its nonzero diagonal entries force t>=0. This proves the theorem, including t0and trace normalization.

## 5. Consequence for the FULL arbitrary-D route, not a new symmetry assumption

If an untwirled PPTtarget R satisfies the same two support inclusions(3), its Ztwirl still does: R*is invariant under Z tensor conjugate(Z), and (R*)^Gamma under Z tensor Z. The twirl preserves positivity/PPT and all W(D)expectations because every diagonal D and Qare Z-invariant. The twirled target is therefore tR*by the theorem.

Thus a potential arbitrary-D negative target cannot be obtained merely by adding J-asymmetry while retaining BOTHof these exact support faces. It must leave at least one support inclusion in(3). This is a genuine actual-state restriction derived without assuming Jsymmetry in advance. It does not say every PPTtarget has those supports or permit discarding targets that leave them.

This note alone does not re-prove a Schmidt-number upper bound for the entire untwirled face. The previous manuscript's32-term R*/6decomposition is a separate unreviewed candidate at its own pin. The new rigidity conclusion and its support constraints are valid written linear algebra independently of that acceptance gate.

## 6. Current eligible asymmetric target interface and first unproved step

The full arbitrary-D/PPTblock/all-complex-Gram problem remains open. A concrete next interface that genuinely LEAVESthe rigid face is

```
R_x=Q+xP(00)+sum_(ell in L,ell!=13)(1/4)P(ell)
                       +[1/(4+8x)]P(13), x>0.          (13)
```

It is PSD by its Gram sum. Its altered partial-transpose block on00/13 has diagonal1/2+x and1/(4+8x), with squared off-diagonal modulus1/8; the determinant is exactly0. All other rank1blocks remain unchanged. Its trace is `tau_x=23/4+x+1/(4+8x)>0`, so `rho_x=R_x/tau_x` is an explicit Gaussian-rational PPTdensity matrix for rational x.

It is not J-invariant, and it leaves BOTHspecific support conditions in(3): P(00)adds a direction outside the old high Qrange, and the changed high/low ratio changes that partial-transpose block's range. It is not low-only diagonal noise above R*. Therefore neither the old symmetry reduction nor this new face theorem excludes it. It is only an eligible PPTcandidate interface, NOTan SN3state or an accepted separator.

**First unproved step:** produce actual16-entry positive D satisfying the full universal complex inverse-Gram criterion and all coupled source-valid rank-two completion inequalities with Tr((D-Q)R_x)<0 for some actual x, or prove a uniform obstruction for that genuine asymmetric trade while retaining the ENTIRE general block residual. No such D or universal-positivity proof is supplied here. A relaxed coefficient choice or an attractive PPTstate is not a separator.

The state-block construction and partial-transpose shuffle are part of the established circulant-state framework; a new read of Chruściński–Kossakowski [0705.3534v3](https://arxiv.org/html/0705.3534), SectionIV/Theorems2–3, confirms this ancestry, not a new general PPT criterion. Its particular Ha example is explicitly stated to have Schmidt number2and is not proposed as our SN3target. No full-paper/SOTA/novelty audit is claimed.

## 7. Evidence ceiling and continuation

This is continued original-primary research, not another scalar-lambda control or an acceptance announcement. The new theorem covers the whole actual support face, with every complex high/low block resolved; the next target deliberately escapes it. All statements are author-WRITTEN candidates, independent review/parent pass absent. No scientific execution, formal/kernel, human/cross-vendor, novelty or fullP44acceptance follows. Original deadline/cutoff and N4/old21tablehistory remain unchanged; no newGO is requested.
