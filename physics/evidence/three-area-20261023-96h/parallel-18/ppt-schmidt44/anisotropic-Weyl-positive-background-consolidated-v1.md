# Genuine anisotropic completion of the four-Weyl range: full complex interface, exact PPT boundary, target decomposition and the entire asymmetric residual

Actual `/bin/date` before writing: **Sun Oct 25 10:26:53 PDT 2026**. PhysicsPPT44-2. **AUTHOR-WRITTEN CANDIDATE; genuine cross-domain reconstruction and parent disposition pending.** No scientific interpreter/eval/arithmetic program, enumeration, solver, replay or compile. Source/metadata/clock/hash operations only. HOLD and v9/v10/v11 remain binding.

## 1. Continuation, later overlays and inherited exact data

This is the CURRENT0853 primary push, continued under `primary-continuation-20261025-102319-v1.json`, not a new slot or a reset. The separate exposure ACKs precede this new manuscript. V10/V11 arrived later than the original0853scope; they were read before subsequent claims/checkpoints, recorded as LATER overlays, and are not retroactively declared original packet contents. `checkpoint-013-later-overlays-and-anisotropic-push-v1.json` permanently discloses the missed active checkpoint between08:57:57 and the actual10:14:24 clock. This proof does not cure that process deviation.

The new interface freeze is `anisotropic-Weyl-primary-interface-freeze-v1.json`, SHA-256 `2841e59c70f228900927cb1f99def4d277ced577502f4d45eab43b4c66bdddad`. Informal written leads after the original primaryACK are disclosed; no preregistration before all reasoning is asserted.

Use the accepted fixed four-Weyl data from the COMPLETE232LF `four-Weyl-rectangle-consolidated-obstruction-v1.md`, SHA-256 `eb1ed1c5aba2bb444a817b48a39ff3d7206c1aacc65421cca7073cffe64a5e02`, at the COMPLETE24LF parent boundary `ppt-four-Weyl-semigroup-two-choice-parent-v1.md`, SHA-256 `562ec6fde1da880b73a5f67e490b9e3d05c66e122795a740cca1e916f1a40c34`:

```
Z|j>=i^j|j>, X|j>=|j+1>, indices modulo4,
U in{I,Z,X,ZX}, Phi_U=vec(U)/2,
Q=sum_U P(Phi_U), Q^2=Q, rankQ=TrQ=4.
```

Every nonzero range matrix alpha I+beta Z+gamma X+delta ZX has complex rank>=3. Let

```
H=sum_(i-j=0or1)P(ij), L=I16-H.
```

H,L have rank8 and Q<=H; hence H-Q is a rank4projection. The inherited partial transpose T=Q^Gamma has eight2 by2blocks. Reordering each block so its H position is first, its exact form is

```
T_block=(1/4)[2,u;conj(u),0], u in{1+i,1-i}.              (1)
```

The L position is second, and every H/L basis position occurs once. This follows from the accepted sector table: a nonzero coherent diagonal of T occurs exactly at a basis difference0or1; every off-diagonal block pairs one such position with a difference2or3. No historical scientific arithmetic or old21-pair table is imported.

## 2. A genuinely new positive geometry, not another scalar control

Define

```
D(a,b)=aH+bL,
W(a,b)=aH+bL-Q, a,b>=0.                                 (2)
```

The actual new class has a!=b. Its full arbitrary-coordinate continuation is

```
W(D)=sum_ij d_ijP(ij)-Q, all16d_ij independent.           (3)
```

The two-level results below do NOT silently settle(3), much less P44.

The escape from the literal closed classes is exact:

- Qrank4 cannot be a conic sum of<=3rank-one terms, even nonorthogonal/dependent ones.
- For0<a<1 and b>0, W(a,b) has FOUR negative eigenvalues a-1 on RanQ, with positive eigenvalues a on Ran(H-Q) and b on RanL. Thus it is not the old one/two-negative literal class.
- The accepted fixedQscalar completion would have the same positive coefficient on Ran(H-Q) and L, so it equals(2) only when a=b.
- There are actual two-block-positive but NON-completely-copositive members of(2), proved in Section5. Thus the older scalar conclusion W^Gamma>=0 is not applicable merely by renaming its parameter.

This is not a claim of escaping the universal decomposable cone: the new uniform proof below will place every two-positive member of(2) in that cone. The point is that this does not follow from either old literal family or the old scalar swap bound.

## 3. Exact full-complex inverse-Gram criterion for arbitrary anisotropy

Assume d_ij>0 for this criterion. For EVERY complex4 by2isometry S and j=0,...,3 put

```
A_j(S)=S*diag(d_0j,d_1j,d_2j,d_3j)S,
V_j=[(1/2)S*U_1e_j,...,(1/2)S*U_4e_j],
G_D(S)=sum_j V_j* A_j(S)^(-1)V_j.                        (4)
```

Then

```
W(D) is two-block-positive
 iff G_D(S)<=I4 for EVERY complex4 by2isometry S.         (5)
```

Proof. Write every rank-at-most-two coefficient matrix C=SZ with columns z_j. Its positive energy is `E=sum_j z_j*A_j z_j`, and its four negative overlaps form `h=sum_j V_j*z_j`. Whitening by A_j^(1/2) makes the exact squared norm of the overlap map lambda_max(G_D). This proves sufficiency. If G_Dv=gv for unit v and g>1, choose `z_j=A_j^(-1)V_jv`. Then E=g,h=gv, and witness expectation is `g-g^2<0` on an actual rank-at-most-two C. This proves necessity and keeps ALL complex planes. No scalar Gram, real-only test or finite product-vector sample substitutes for(5).

For two levels, d_ij=a on H and b on L. The positive matrices A_j are not scalar unless a=b, so the old flat formula is not being reused. All a,b zero boundaries in the obstruction below are handled by direct vector/block arguments, not by inserting an undefined inverse.

Strict positive d loses no strict detection opportunity within route(3): if a zero-boundary W(D) is two-block-positive and has Tr(Wrho)=-delta<0 for a trace-one PPT rho, then W+epsilon I is still two-block-positive and still negative for0<epsilon<delta, with every product-diagonal coefficient positive. Rational epsilon may be chosen when rational data are wanted. This is an existence reduction for this route only, not for arbitrary witness forms.

## 4. A new rank-two completion and the actual rational target

Use matrix units E_rs. The complex matrix

```
C=(I+Z)+sqrt2(E13+E31)                                  (6)
```

has diagonal(2,1+i,0,1-i). Its{1,3}block has determinant `(1+i)(1-i)-2=0` and rank1; the isolated00entry has rank1 and row/column2 is zero. Thus C has rank exactly2. Its H part lies in RanQ and has squared norm8; its L part has squared norm4. Therefore

```
<C,W(a,b)C>=8a+4b-8=4(2a+b-2).                         (7)
```

Consequently universal two-positivity requires

```
2a+b>=2.                                                (8)
```

A separate principal I,Z Gram test, restricted to the diagonal two-coordinate matrices, requires

```
a>=a0=(2+sqrt2)/4>3/4.                                 (9)
```

Indeed its2 by2negative-overlap Gram has diagonals1/2 and off-diagonal(1+i)/4. These are necessary tests, NOT asserted sufficient for two-positivity.

The actual new rational PPT density matrix is

```
rho6=(4Q+L)/24.                                         (10)
```

It is positive, trace one and rank12 because Q and L are orthogonal projections of ranks4,8. It is not the old full-rankrho4. By(1), every partial-transpose block of4Q+L is `[2,u;conj(u),1]` in H/L order, exactly `P((u,1))` since |u|^2=2. Thus the eight literal integer-Gaussian rank1blocks give an exact PPT Gram certificate, of total rank8.

The trial W(7/8,1/8) has

```
Tr(Wrho6)=(2a+b-2)/3=-1/24.
```

But (6), after normalization by sqrt12, has the SAME negative expectation-1/24. Hence the trial fails the required universal rank-two condition. It is not an SN3 witness and is not offered as one. The following statements settle much more than this isolated failure.

## 5. Non-PSD, two-block-positive and NON-CCP headroom is real

The anisotropic mechanism is not merely PSD-only. Consider

```
W0=(H-Q)+(1/4)L>=0.
```

Its kernel is exactly RanQ, which contains no nonzero SR<=2vector by the named baseline. The continuous W0expectation on the compact set of unit SR<=2vectors therefore has a strictly positive minimum mu0. For

```
0<epsilon<min(mu0,1/8),
W_epsilon=W0-epsilon H
          =(1-epsilon)H+(1/4)L-Q,                       (11)
```

all such expectations are at least mu0-epsilon>0. Thus W_epsilon is genuinely two-block-positive and has four negative eigenvalues-epsilon on Q.

Yet its partial-transpose2 by2blocks have diagonal entries1/2-epsilon and1/4, and off-diagonal modulus sqrt2/4. Their determinant is

```
(1/2-epsilon)/4-1/8=-epsilon/4<0.
```

So W_epsilon is NOT completely copositive. Rational epsilon exists in that open interval; this is existence-only headroom, not an evaluated mu0 or a displayed certified epsilon. It proves why the accepted scalarCCPresult cannot immediately dispose of the new geometry. The new decomposability theorem, not the old CCP bound, is needed.

## 6. Uniform decomposability of the entire two-level two-positive class

For a>=1, `W=(a-1)H+(H-Q)+bL>=0` directly. Otherwise two-positivity implies(8)–(9), so3/4<a<1 and b>=2(1-a). Put s=1-a and t=4a-3=1-4s, both with s>0,t>=0. Then

```
W=t(H-Q)+R,
R=3s H+bL-4s Q.                                        (12)
```

The first summand is PSD. Using(1), every block of R^Gamma in H/L order is

```
[s,-s u;-s conj(u),b].
```

Its determinant is s b-2s^2>=0 because b>=2s; its diagonals are nonnegative. Therefore R^Gamma>=0. This is an explicit complete physical identity, with no unknown finite matrix sum:

```
W=t(H-Q)+(R^Gamma)^Gamma.                              (13)
```

The a=1 and b=0 endpoints are included in the direct PSDcase or(12)with zero coefficients. Thus EVERY two-block-positive member of the entire genuinely anisotropic two-level class is decomposable and detects NO PPT state. The conclusion is NOT completely copositive in general, as(11)proves.

## 7. Exact all-PPT boundary, including explicit rational targets

For all a,b>=0, W(a,b) is nonnegative on EVERY PPT state iff

```
a>=f(b),
f(b)=1-b/2,              0<=b<=1/2,
f(b)=1/2+1/(8b),         b>=1/2.                         (14)
```

Sufficiency on0<=b<=1/2: set a*=1-b/2 and t=1-2b>=0. Formula(12)at a* gives a PSD t(H-Q)plus a partial-transpose-positive remainder, whose blocks have H diagonal b/2,L diagonal b and off-diagonal-(b/2)u, determinant0. For a>=a*, add(a-a*)H>=0. This includes b=0.

Sufficiency on b>=1/2: W^Gamma has blocks `[a-1/2,-u/4;-conj(u)/4,b]`. At a*=1/2+1/(8b), they have determinant0 and positive diagonals; hence W is already completely copositive. Increasing a adds a positive diagonal.

Necessity in the first branch is supplied by rho6, whose expectation is `(2a+b-2)/3`.

For the second branch define

```
y=(2b-1)/(2b+1), z=1/[4b(2b+1)],
Sigma_b=Q+y(H-Q)+z L.                                  (15)
```

These coefficients are nonnegative. Generally `Sigma=xQ+y(H-Q)+zL` is PSD for x,y,z>=0, and(1)gives its partial-transpose blocks

```
[(x+y)/2,(x-y)u/4;(x-y)conj(u)/4,z].
```

They are PSD iff `4z(x+y)>=(x-y)^2`. For(15), x=1 and equality holds exactly: `1+y=4b/(2b+1)`, `1-y=2/(2b+1)`. Thus Sigma_bis a literal nonzero PPToperator, rational whenever b is rational. With a*=1/2+1/(8b),

```
Tr(W Sigma_b)=4(1+y)(a-a*).                             (16)
```

This is negative for a<a*. Normalize by the positive trace to obtain a PPTdensitymatrix. No optimizer status or approximate boundary is used. At b=1/2 this reproduces Q+L/4 and rho6. Equations(14)–(16)therefore classify the ALL-PPTside exactly, without claiming every PPTstate has the special form Sigma.

## 8. A finite32-term rank-two decomposition closes the whole low-noise extension target class

The new rho6is not just undetected by(2): it actually has Schmidt number at most2. This uses a small symbolic phase identity, not an unadmitted weighted table.

Let k=0,1,2,3 and w in{1,i,-1,-i}. Put r=k-1,s=k+1 and

```
A_k=I-i^(-k)Z,
C_(k,w)=A_k+sqrt2[w E_rs+w^(-1)E_sr].                    (17)
```

A_khas zero diagonal entry at k, entry2at k+2, and entries1+i,1-i at r,s. The{r,s}block has determinant2-2=0 and rank1, while the isolated k+2diagonal gives another rank1. Thus every C_(k,w)has rank exactly2 and squared Frobenius norm8+4=12.

Averaging w kills all cross terms between the constant A_k and the characters w,w^-1, and between those two distinct fourth-root characters. Averaging k then kills the I/Zcross term. Each opposite-position matrix unit appears for exactly two of the four k values, with squared coefficient2, so its final coefficient is1. Consequently

```
(1/16)sum_(k,w)P(vec C_(k,w))
 =P(vec I)+P(vec Z)+sum_(i-j=2)P(ij).                    (18)
```

Left multiplication by X preserves rank/norm, sends I,Z to X,XZ (the latter a unit phase times ZX), and sends the difference2positions to difference3. Therefore

```
(1/16)sum_(k,w)P(vec X C_(k,w))
 =P(vec X)+P(vec ZX)+sum_(i-j=3)P(ij).                   (19)
```

Adding(18)and(19)gives4Q+L. Thus the complete convex decomposition is

```
rho6=(1/32)sum_(epsilon=0,1;k;w)
       P(vec(X^epsilon C_(k,w))/sqrt12).                 (20)
```

All32vectors have unit norm and rank2; all32weights are1/32. Every finite character and coefficient group in the operator identity was accounted for symbolically.

This yields a WHOLE8-parameter state-family obstruction. Let

```
R=Q+sum_(ell in L)y_ell P(ell), y_ell>=0,
```

with no added H noise. Its partial-transpose blocks have H diagonal1/2,L diagonal y_ell and squared off-diagonal modulus1/8. Thus it is PPT iff EVERY y_ell>=1/4. Under those exact conditions,

```
R=(Q+L/4)+sum_(ell in L)(y_ell-1/4)P(ell)
```

is Schmidt-number-at-most-two by(20)and product noise. No witness of ANYform can make those particular states an SN3construction. This is not a claim about high-noise additions with compensating reduced L weights or arbitrary PPT states.

## 9. A necessary actual-state symmetry break for arbitrary diagonal backgrounds

The full route(3)still has16independent d_ij. Let

```
J=(X tensor I)SWAP.
```

On product kets J maps(i,j)to(j+1,i), and J^2=X tensor X. Its eight powers have exactly two product-basis orbits: the8Hpositions and the8Lpositions. On coefficient matrices J acts as C->X C^T. It sends U_pq to a unit phase times U_(p,1-q), so JQJ*=Q. It also fixes H,L. SWAP and local X preserve Schmidt rank.

If W(D)is universally rank-two nonnegative, its conjugate average over these eight powers is also rank-two nonnegative and is exactly W(a,b), where a and b are the averages of D's entries over H and L. If the ACTUAL tested PPTstate rho satisfies JrhoJ*=rho, then

```
Tr(W(D)rho)=Tr(W(a,b)rho)>=0                             (21)
```

by the newly proved decomposability of the two-level class. Thus NO arbitrary product-diagonal completion can separate ANY J-invariant PPTtarget. This includes all Sigma_band rho6, but is broader than those explicit families.

The reduction is lossless ONLY under that actual-state invariance. Averaging a general state over J would change the objective of a nonsymmetric D and is NOT licensed. No claim that all PPTstates or all potential SN3witnesses can be averaged into this closed subclass is made.

## 10. ENTIRE arbitrary-D residual, with every complex/PPT constraint retained

The strict d_ij>0 case suffices for strict detection by the regularization argument in Section3. The only state twirl imposed here is the LOSSLESS four-element group generated by Z tensor conjugate(Z). It preserves every product-diagonal D and each Qray projector, so preserves W(D)'s expectation and PPT. The resulting general state has four Hermitian4 by4difference blocks

```
R=sum_(q=0)^3 sum_(r,s) R^(q)_rs |r,r-q><s,s-q|.
```

Positivity is exactly `R^(q)>=0` for ALLq. Bob transpose has four total-index blocks

```
S^(tau)_rs=R^(r+s-tau)_rs, tau=0,1,2,3,                 (22)
```

because the original entry becomes `|r,s-q><s,r-q|` with total index tau=r+s-q. Therefore the COMPLETE PPTcondition is

```
ALL R^(q)>=0, ALL S^(tau)>=0,
sum_q Tr R^(q)=1.                                      (23)
```

No entry of these four complex Hermitian blocks is discarded. Put `B_rs=(1+i^(r-s))/4`; the restriction of Qto each difference0and1block is B. The exact objective is

```
F_D(R)=sum_(q,r)d_(r,r-q)R^(q)_rr
       -sum_(q=0,1)Tr(B R^(q)).                         (24)
```

### Eight coupled, source-valid rank-two completion inequalities

The arbitrary-D residual has additional explicit necessary constraints beyond a formal inverse-Gram restatement. For q=0,1 and k=0,1,2,3 put ell=k+2,r=k-1,s=k+1 modulo4 and consider the ENTIRE complex family

```
C_(q,k)(t,w)
 =X^q[A_k+(t-2)E_(ell,ell)
          +sqrt2(wE_rs+w^(-1)E_sr)],
t in C, w in C excluding0.                             (25a)
```

The isolated diagonal t contributes rank at most1; the opposite2 by2block has determinant2-2=0 and rank1. Hence every such C has rank at most2. Its two relevant Qoverlaps have moduli |t+2|/2; the other two vanish. For q=1 only harmless unit phases change. The low entries have difference2+q, so no discarded Qoverlap is hidden.

Define from the SAME actual coefficient array D

```
A=d_(ell+q,ell), B=d_(r+q,r), C=d_(s+q,s),
f=d_(r+q,s), g=d_(s+q,r).
```

The positive energy is `A|t|^2+2(B+C)+2f|w|^2+2g|w|^(-2)`. Since f,g>0, its w-dependent infimum is4sqrt(fg), attained by |w|^4=g/f. After subtracting the Qexpectation |t+2|^2/2, the exact infimum over w is

```
(A-1/2)|t|^2-2Re(t)+2(B+C)+4sqrt(fg)-2.
```

Nonnegativity for ALL complex t is therefore equivalent, on this literal rank-two family, to

```
A>1/2,
(A-1/2)[2(B+C)+4sqrt(fg)-2]>=1.                          (25)
```

If A<=1/2 the nonzero linear term or negative quadratic coefficient gives an immediate negative t direction, so there is no missed equality branch. Thus every universally two-block-positive W(D) satisfies ALL EIGHT coupled inequalities(25), with their shared d_ij retained. These are exact infinite-family tests, not finite sampled vectors, and they are NOT asserted sufficient for the full condition(5).

For the two-level subclass, they reduce to

```
(a-1/2)(a+b-1/2)>=1/4,
b>=2(1-a)+(1-a)^2/(a-1/2), a>1/2.                       (26)
```

In particular, for1/2<a<1 the necessary b is STRICTLY above the linear PPT boundary2(1-a). A supporting two-level PPT-boundary witness cannot be promoted to two-positive merely from its zero expectation on rho6. The original isolated-rank-one entry can vary while preserving rank two, and that variation is essential.

**First unproved step:** find actual positive d_ij and actual blocks R^(q) satisfying the FULL universal criterion(5), ALLPPTconstraints(22)–(23), the eight actual coupled necessary tests(25), and F_D(R)<0, or prove impossibility uniformly for this entire residual. Any successful target must break the Jsymmetry by Section9and lie outside the low-only diagonal extension family of Section8. The eight tests remain tied to the SAME D; they are not permission to choose independent relaxed data, omit asymmetric blocks or replace(5)by selected planes.

This is an exact unrestricted-tested-state residual for the PRODUCT-DIAGONAL completion route, not a finite solver relaxation. Even a uniform no-go for it would not classify arbitrary non-diagonal positive completions or all two-positive M4maps. No feasible pair is claimed here. The original P44target remains fully registered and unsolved; it is not replaced by the two-level problem.

## 11. Current evidence and continuation boundary

New results in this ONE manuscript are the genuinely anisotropic inverse-Gram interface, non-CCPtwo-positive headroom, the whole two-level decomposable class and exact all-PPTboundary, the complete32-term state decomposition and8-parameter extension obstruction, and the actual-target symmetry obstruction for every diagonal background. They are author-WRITTEN only until a genuine cross-domain reconstruction and parent pass. No SOTA, novelty, formal/kernel, human/cross-vendor or executable-certificate acceptance is claimed.

The exact asymmetric arbitrary-Dstep above is still actionable primary research, not an accepted theorem or a gate whose completion would finish the96-hour request. This manuscript reports that residual rather than a fake positive witness. The original cutoff/deadline, N4UNKNOWN/incomplete/exit-unestablished status and all frozen stronger gates stay unchanged. No scalarcontrol sweep, x1111rerun, scientific program or newGO occurred.
