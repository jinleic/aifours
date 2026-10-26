# Upper zero-six: complete written 1+3 Schmidt-family closure

Actual before-writing clock: **2026-10-24T04:22:38-07:00**, `/bin/date -Iseconds`. Author PhysicsResearch96h.

**CANDIDATE / UNREVIEWED.** This is a new analytic family calculation within the same single upper-zero residual attack. It is not the requested unrestricted-spectrum sign, the other three residual signs, the all-reference co-Choi theorem, W4, or a novelty/formal-verification verdict. No scientific program, arithmetic interpreter, numerical experiment, import, compile/test, model CLI or nested agent was used.

## 1. Exact claim, dependencies and non-substitution boundary

Use the same literal Z_up as `all-reference-four-residuals-v1.md`, SHA256 `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277`. Consume the actual p principal components017–019 and their parent/component disposition, not the corrected charge branch as a mathematical premise.

New edge checkpoint001, SHA256 `70bdec0140a9cbaf788cee074bd09dc43a467fe488fb8200b30ca7930a053372`, supplies H and the six-variable incidence chart. Checkpoint002, SHA256 `1bc5491c3ab60be713cf47193c7a75a8da0f90db405308dbe879058db5d7c2c6`, supplies the **exact** nonnegative raw remainder `Qraw-R0`; its stronger p comparison was explicitly unproved there.

The candidate proved HERE is that stronger comparison, and hence the entire six-dimensional Z_up sign, for

```
c=(a,b,b,b), a,b>=0, a^2+3b^2=1,
```

and permutations of this family. All complex q-plus directions are included. This is not the old two-pair `(1,1,t,t)` family. It includes but is not a new proof claim about the already-covered uniform and equal-rank-three points.

**The primary target remains Z_up>=0 for ALL Schmidt spectra.** This continuum is an analytic probe/new scoped closure, not a silent replacement of that target. The unrestricted stronger comparison and unrestricted Z_up sign both remain open after this file.

## 2. Two useful identities without an inverse

Put `V=UQ`, where U is complex symmetric with zero diagonal. The comparison energy of002 has the exact norm representation

```
R0(U)=(1/4)|| (DU+UD)/2 ||_HS^2
      +(1/4)||D^(1/2)UQ||_HS^2.               (S1)
```

Indeed the first norm is `2 sum d_ij^2|U_ij|^2` and the second is `2 sum d_ij|U_ij|^2-b^dagger D b`, with b=Uc. This is an immediate independent derivation of positivity of R0, not the missing inverse bound.

Also, `diag(V)=-diag(c_i b_i)`. With the actual supported p operator `B'=D^2 P_B` acting rowwise on the input-Q space, checkpoint001's filtered coupling is exactly

```
h=vec(D H(q))=-(D_out+B')vec(V)/(2sqrt(2)).     (S2)
```

Here D_out is left matrix multiplication by D; it is not an input filter. These identities alone do not establish `Cost_p<=R0`.

## 3. Family parameters and full q representation

For the interior let

```
t=b^2, p=a^2=1-3t, 0<t<1/3,
A=3t, B=1-t, h=1+8t,
s=(A+B)/2=(1+2t)/2,
r=A B/h,
D=diag(A,B,B,B).
```

Here h is a scalar parameter, distinct from the vector h in (S2); below h_i denote vector coordinates only where explicitly indicated. The source inverse normalizer is `W=B^2 h`, and the supported p filter parameter is indeed `r=1/sum_i1/d_i=A B/h`.

Index the three active/inactive edges `(1,i)` by i=2,3,4 and the three inactive edges by their opposite inactive vertex i. Write their U amplitudes u_i and v_i. Under permutations of the three inactive labels, each edge triple is `trivial1 plus standard2`. Thus q6 consists of two trivial coordinates and two copies of the same standard two-coordinate calculation.

For completeness, the full source Tq has

```
E=s/(B h)-1/4,
k=a b/(4s), l=t/(4B),
Tq=[[ (E-l)I3+l J3, k(J3-I3) ],
    [ k(J3-I3), (E-l)I3+l J3 ]].              (S3)
```

Both diagonal pair types have the same E because complementary pair products are sB. No adjacency or complex direction is omitted.

## 4. Trivial q2: exact p3 elimination and positive remainder

Take u_i=u, v_i=v. Let e0 be the normalized inactive all-ones vector and

```
v0=(sqrt(3)b,-a/sqrt(3),-a/sqrt(3),-a/sqrt(3)),
P_E=I_inactive-|e0><e0|.
```

An orthonormal p-trivial basis (output row/input column matrices) is

```
T1=|1><v0|, T2=|e0><v0|, T3=P_E/sqrt(2).
```

The actual filtered p3 matrix is

```
R_T=[[r A, -r sqrt(3)a b, 0],
     [-r sqrt(3)a b, 2B/3+r p, B a sqrt(2)/3],
     [0, B a sqrt(2)/3, B p/3+r]].             (S4)
```

This follows by restricting `B'+r F_Q`. For B', the first basis vector is in its kernel and the lower two-by-two block is `(B/3)[[2,a sqrt(2)],[a sqrt(2),p]]`; the r term gives the remaining displayed entries.

The coupling coordinates are

```
h1=A sqrt(3)a u/(2sqrt(2)),
h2=B[-(5/2)b u+2a v]/sqrt(2),
h3=B[(1-(3/2)t)v-(a b/2)u].                  (S5)
```

These result from the full H(q), not an assumed reference-orthogonality of an unrelated lower column. Eliminate T1. The corrected h2 becomes

```
h2tilde=[-b(1+2t)u+2B a v]/sqrt(2),
```

the remaining p2 matrix is `[[2B/3,B a sqrt(2)/3],[B a sqrt(2)/3,Bp/3+r]]`, and its final pivot is r. Consequently

```
Cost_T=3/(4B){(p h/2)|u|^2
             +|-b(1+2t)u+2B a v|^2
             +t h|B v+a b u|^2}.             (S6)
```

The direct R0 formula on these same unnormalized edge amplitudes is

```
R0_T/3=[1+16t-20t^2]|u|^2/8
        +B(1-(3/2)t)|v|^2-B a b Re(conj(u)v).
```

Subtract (S6). The complete difference is

```
(R0_T-Cost_T)/3
 =[u,v]^dagger Delta_T [u,v],

Delta_T,11=t[4-11t+t^2+24t^3]/(4B),
Delta_T,22=B t(5-8t)/4,
Delta_T,12=Delta_T,21=a b t(5-8t)/4.           (S7)
```

Its second diagonal is positive and its exact determinant is

```
det Delta_T=t^2(5-8t)(1-4t+6t^2)/4>0.         (S8)
```

For the expansion in (S8), subtracting the off-diagonal square reduces the bracket to

```
[4-11t+t^2+24t^3]-p t(5-8t)=4-16t+24t^2.
```

Also `1-4t+6t^2=6(t-1/3)^2+1/3`. This proves the full complex trivial-q2 stronger comparison, strictly on the declared interior.

## 5. Standard q2: exact p4 and all four cross columns

Let e be any normalized real inactive standard vector, `sum e_i=0`. Set u_i=u e_i and v_i=v e_i. Choosing two orthonormal such e's gives two identical blocks; all displayed entries are the bilinear intertwiner coefficients, so complex linear combinations are included.

An orthonormal p-standard basis is

```
A1=|1><e|,
B1=|e><v0|,
C1=|e0><e|,
D1=sqrt(3)P_E diag(e)P_E.
```

The last norm is one since `||P_E diag(e)P_E||^2=1/3`; its diagonal is e/sqrt(3). All other basis inner products vanish. This accounts for four copies of the inactive standard representation. Together with p-trivial3 and p-sign1 these exhaust the twelve-dimensional quotient. The sign representation has no q coupling and retains the supported positive p pivot.

The actual filtered p4 matrix, in this order, is

```
R_S=[[A^2, r sqrt(3)b, 0, 0],
     [r sqrt(3)b, 2B/3, a(B/3-r), aB/3],
     [0, a(B/3-r), B^2-B/3, -B/3],
     [0, aB/3, -B/3, B^2-B/3+r]].             (S9)
```

One derivation is that B' is `A^2` on A1 and `B^2 I3-(B/3)ww^T` on the other three, with `w=(-a,1,1)`. The only rF entries are A1/B1=`sqrt(3)b`, B1/C1=`-a`, and D1/D1=1.

The full standard coupling is `-(1/sqrt(6))` times

```
[A sqrt(3)(1+A)u/2,
 B((5/2)b u+a v),
 B((a b/2)u-v),
 B((a b/2)u+(2-(3/2)t)v)]^T.                 (S10)
```

The standard R0 two-matrix has diagonal

```
R0_S,uu=(1+16t-2t^2)/8,
R0_S,vv=B(1-(3/4)t),
```

and off-diagonal `B a b/4`. Prove the stronger comparison by proving positivity of the joint matrix with p block R_S, cross (S10), and q block R0_S. This is an ordinary positive-pivot Schur assertion; no inverse is guessed.

### 5.1 First positive pivot and a five-dimensional real matrix

Eliminate A1, whose pivot is A^2. The corrected p B1 diagonal is `2B/3-r^2/A`; its u cross coefficient inside the common `-B/sqrt(6)` factor becomes `b j`, where

```
j=(2+31t)/(2h).
```

The q uu coefficient becomes `t(10-11t)/8`. Replace u by `w/b`, rescale the remaining three p test variables by sqrt(6), and divide the entire form by positive B. Define

```
n=2-(3/2)t, m=2-3t.
```

The resulting EXACT five-matrix in coordinates `(B1,C1,D1,w,v)` is

```
K5=[[4-6AB/h^2, 2aB/h, 2a, -j, -a],
    [2aB/h, 2m, -2, -a/2, 1],
    [2a, -2, 2m+6A/h, -a/2, -n],
    [-j, -a/2, -a/2, (10-11t)/(8B), a/4],
    [-a, 1, -n, a/4, n/2]].                 (S11)
```

Every rescaling is invertible on `0<t<1/3`. Thus this matrix includes the true incidence/image cross terms, not a subspace test.

### 5.2 Two exact decouplings

Eliminate v, pivot n/2>0. The D1 diagonal becomes

```
A(5-8t)/h>0,
```

and **all** its remaining couplings vanish: B1/D1, C1/D1 and w/D1 cancel exactly. For example the B1/D1 correction is `(-a)(-n)/(n/2)=2a`, and the w/D1 correction is `(a/4)(-n)/(n/2)=-a/2`.

The remaining three-matrix on `(B1,C1,w)` has entries

```
BB=4-6AB/h^2-2p/n,
CC=2m-2/n,
BC=2a(B/h+1/n),
Bw=-j+p/(2n),
Cw=-(a/2)(1+1/n),
ww=(10-11t)/(8B)-p/(8n).                     (S12)
```

Let

```
k0=2-6t+3t^2>=1/3,
P4=28+207t-819t^2+518t^3-24t^4,
P3=68-227t+196t^2-48t^3,
H4=64-300t+477t^2-312t^3+72t^4.
```

The C1 pivot is `3k0/n>0`. Eliminating it leaves the actual two-matrix

```
Y11=3t P4/(h^2 n k0),
Y12=-3t P3/(4h n k0),
Y22=H4/(16B n k0).                           (S13)
```

For explicit cross-checking of (S13), the intermediate numerators reduce to

```
(2h^2-6tBn)k0-p(t+1)^2(t+2)^2=t P4,
(2+36t-15t^2)k0-p(t+1)(t+2)(2-t)=t P3,
(38-66t+27t^2)k0-3Bp(2-t)^2=H4.
```

These are full polynomial identities; the proof uses their written expansion, not finite point substitution.

### 5.3 Hand coefficient certificate for the last sign

Set x=3t in [0,1]. The displayed P4 is

```
P4=28+69x-91x^2+(518/27)x^3-(8/27)x^4
   >=28-22-8/27=154/27>0,
```

using x^2<=x, x^4<=1 and the nonnegative cubic. Hence Y11>0 on the interior.

The exact determinant is

```
det Y=3t D8/(16B h^2 n^2 k0^2),
D8=P4 H4-3Bt P3^2
 =1792-9024t+5328t^2+41684t^3-89076t^4
   +57558t^5+5040t^6-18576t^7+5184t^8.       (S14)
```

Here is a complete positive-coefficient certificate for this polynomial on the whole interval, not evaluations at selected parameters. First

```
81 D8(x/3)=145152-243648x+47952x^2+125052x^3
          -89076x^4+19186x^5+560x^6-688x^7+64x^8.
```

Write this power-coefficient list as f_j. With x=y/(1+y), y>=0, multiplication by `(1+y)^8` yields the coefficient list

```
C_k=sum_(j<=k) f_j binom(8-j,k-j),

(C0,...,C8)=
(145152, 917568, 2406672, 3424668, 2888424,
 1473274, 441110, 70338, 4554).               (S15)
```

Every coefficient is a positive integer. Therefore D8(t)>0 for `0<=t<1/3`; at `t=1/3` the endpoint value is `4554/81>0`. The printed convolution formula and both full coefficient lists allow exact independent reconstruction; no interpreter or kernel replay produced them.

Thus Y11>0 and detY>0, so Y is positive. All earlier pivots were positive. Therefore K5, the joint standard p4/q2 matrix, and `R0_S-Cost_S` are positive on the whole interior. This proves the stronger comparison for BOTH standard copies, not merely a single real e direction.

## 6. Candidate conclusion and remaining unrestricted obligation

Sections4–5 prove `Cost_p(U)<R0(U)` for every nonzero complex U on the entire positive 1+3 family. Together with002's exact `Qraw>=R0`, this proves **all six directions of Z_up** on that family, with no discarded mixed terms. Adding the supported p/reference/q-minus components would give the corresponding upper zero-sector block only; it supplies none of the other three generic final signs.

Sparse endpoints are included by continuity of the original physical joint matrix `(rho,Hq,R0)` with `q_ij=d_ij U_ij`. Prove it for positive t,p by invertible filters first, then take the physical matrix limit. In particular no D inverse, frame inverse or boundary-singular p pivot is evaluated at t=0. The separately supported range/Moore-Penrose interface then gives the stated boundary residual meaning. At p=0 this is the already-covered equal-rank-three endpoint, not a newly independent discovery.

The desired **unrestricted** `Cost_p<=Qraw` and the proposed unrestricted stronger `Cost_p<=R0` remain unproved. Their next input is a genuinely coupled four-spectrum estimate, not an inference from S3 symmetry, an equal-rank endpoint, or a finite reference list. A counterexample to the stronger comparison alone would not refute Z_up; a negative Z_up would refute only the sufficient route, not automatically W4.

No independent review, parent acceptance, proof assistant, priority clearance or execution authorization for this NEW packet has been claimed. Historical producer receipts and all operative timestamp/evidence errata keep their separate status. Both held polynomial requests remain unused and unrun.
