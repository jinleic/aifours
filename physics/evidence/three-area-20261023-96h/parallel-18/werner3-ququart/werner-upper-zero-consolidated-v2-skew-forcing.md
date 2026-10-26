# Werner upper zero-six — a new all-spectrum complex-skew forcing certificate

Observed `/bin/date` before this manuscript: **Sun Oct 25 09:27:47 PDT 2026**. Owner PhysicsResearch96h-2, physics-1. Immutable successor under `primary-continuation-20261025-0853-v1.json`; the separate primary exposure ACK preceded this proof work. No previously pinned source is changed.

**NEW WRITTEN CANDIDATE: actual forcing domination on the ENTIRE three-dimensional complex antisymmetric p subspace, uniformly over ALL positive four-Schmidt spectra and with ALL six complex q directions.** This is not another equivalent representation, p-only positivity, a selected-spectrum theorem, or a sampled coefficient observation. The requested full p12/q6 sign is STILL NOT_PROVED; its exact nine-dimensional mixed-complement residual is specified in Section8.

All reasoning below is WRITTEN algebra/inequalities. No scientific eval/interpreter/arithmetic or symbolic program, enumeration, replay, solver, compilation, new GO, extra agent or model CLI was used. Parent errata v1-v9 remain binding. Additive **v10** was read completely, LF1-31, before the first new checkpoint and this manuscript; its fresh metadata hash is `d61acbf77fefa3a8d55d0cf74e9ebe0b680edb28d273f5b22255d09cbd66aa62`. It changes evidence chronology/rendering qualifications, not the frozen mathematical scope. No Olson input or historical unadmitted output is a premise.

## 1. Full primary, new partial theorem and accepted input boundary

The original primary remains unrestricted complex rank<=2 three-copy ququart Werner nonnegativity. The active upper-zero E_full leaf is only one sufficient co-Choi-route subgoal; F_up,F_low,Z_low and the full W4 bridge remain separate.

Use the exact positive-interior data

```
c_i>0, sum_i c_i^2=1,
x_i=c_i^2, d_i=1-x_i, D=diag(d_i),
d_ij=(d_i+d_j)/2, Q=I-cc^T,
r=1/(sum_i 1/d_i), W=e3(d).
```

On the complex twelve-dimensional space H={Z:Zc=0}, the ACTUAL filtered p quadratic is

```
rho'Z=D^2Z-D diag(Z_ii)Q+rQZ^TQ.
```

Let F be the six unnormalized edge entries `F_ij=d_ij U_ij`, where U is any COMPLEX transpose-symmetric zero-diagonal matrix. The exact forcing is

```
j_ij(Z)=[d_i(1+d_i)Z_ij+d_j(1+d_j)Z_ji
             +c_i c_j(d_i Z_ii+d_j Z_jj)]/(d_i+d_j).
```

The ENTIRE actual raw q kernel, with {k,l} complementary to {i,j}, is

```
(K_full)_(ij,ij)=3-2d_ij d_kl/W,
(K_full)_(ij,it)=-c_j c_t/(2d_jt),
(K_full)_(e,f)=0 for disjoint edges.
```

All shared-edge terms are retained. The exact joint form and its q minimum are

```
J_c(Z,F)=<Z,rho'Z>-sqrt(2)Re(j(Z)^dagger F)
                         +(1/2)F^dagger K_full F,
E_full,c(Z)=<Z,rho'Z>-j(Z)^dagger K_full^(-1)j(Z).          (1)
```

Named inputs, at their existing written assurance only:

- Generic G1-G12/forcing source, SHA256 `249c1becd5e89ff08a3badebaab8234f3e89d7cb7879430e8e9152eabff18a7e`.
- COMPLETE raw remainder/full pivot addendum2, SHA256 `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64`.
- Literal raw physical source, SHA256 `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277`.
- Parent v24, SHA256 `55d24c07c592c8e2e3d5bdd06aa0ca2c6c1ce9d9d2a3a527398251c5b8d29248`; parent v30/v31, SHA256 `73c736679bcdcc3e9f3e84a6840d0c66e48222cd62e6c0616e217584724dd476`, exact Werner section8. These support identities/pair condensation, not the full sign.
- Fully read current baseline `werner-upper-zero-consolidated-v1.md`, SHA256 `b006646d85afb5b6f4428880d733a413f22f6a92c4320654e4d8dabbcafd553b`. Its inverse-free/polynomial successor boundary is NOT promoted or used in this proof.

The complete raw-remainder import gives `K_full>=I`. No upper bound K_full<=3I is used. No false G13, bare dual lift, p-only H>0 inference or unreviewed polynomial coefficient is used.

### The new theorem — precise uniform scope

Let

```
A_c={Z: Z^T=-Z, Zc=0}.
```

Transpose-skew here is COMPLEX LINEAR and does not mean skew-Hermitian or real. Its complex dimension is3. For EVERY positive normalized c and EVERY Z in A_c,

```
<Z,rho'Z>-||j(Z)||_edge^2 >= ||Z||_HS^2/40.               (2)
```

Consequently, for EVERY complex edge vector F,

```
J_c(Z,F) >= ||Z||_HS^2/40
          +(1/2)||F-sqrt(2)j(Z)||_edge^2
          +(1/2)F^dagger(K_full-I)F >=0.                 (3)
```

In particular `E_full,c(Z)>=||Z||_HS^2/40` on A_c. Formula(3) is a certificate for an ACTUAL joint p3/q6 compression, not merely p3 principal positivity: the forcing is present and ALL q6 directions vary freely. The full raw correction remains in the displayed K_full-I term.

## 2. Exact skew forcing and one scalar edge function

For Z in A_c, its diagonal is zero. Also Zc=0 and Z^T=-Z imply c^TZ=0, so QZ=ZQ=Z. Therefore

```
<Z,rho'Z>=sum_(i<j)(d_i^2+d_j^2-2r)|Z_ij|^2,
j_ij(Z)=(d_i-d_j)(1+d_i+d_j)Z_ij/(d_i+d_j).
```

Define for a,b>0

```
g(a,b)=a^2+b^2-[(a-b)(1+a+b)/(a+b)]^2
      =2ab-(a-b)^2[2/(a+b)+1/(a+b)^2].                   (4)
```

Then the LEFT side of(2), before any bound, is EXACTLY

```
sum_(i<j)[g(d_i,d_j)-2r]|Z_ij|^2.                       (5)
```

The following argument bounds this FORCING DIFFERENCE, not rho' alone. Some coefficients in(5) can be negative; they are not thrown away or incorrectly declared individually positive. The actual Zc=0 relations control them.

We will repeatedly use the elementary harmonic bound

```
r<=3/16,                                                (6)
```

because sum_i d_i=3 and Cauchy gives `(sum d_i)(sum 1/d_i)>=16`.

## 3. A scalar estimate for two non-small d entries

**Lemma1.** If A>=1/2 and a,b in[A,1], then `g(a,b)>=2A^2`.

Proof: order a<=b and write delta=b-a, T=a+b=2a+delta. Then `0<=delta<=1-a<=a`, T>=1 and delta/T<=1/3. Hence

```
delta[2/T+1/T^2]<=2/3+1/3=1<=2a.
```

Using(4),

```
g(a,b)=2a^2+delta{2a-delta[2/T+1/T^2]}>=2a^2>=2A^2.
```

This is an entire two-variable interval inequality, not endpoint sampling.

If all x_i<=1/2, all d_i>=1/2. Lemma1 and(6) give `g(d_i,d_j)-2r>=1/8` on every edge. Equation(5) then proves

```
<Z,rho'Z>-||j||^2 >= (1/8)sum_(i<j)|Z_ij|^2
                         =||Z||_HS^2/16.                (7)
```

The remaining case is a unique dominant Schmidt square, and must not be discarded as a boundary or special spectrum.

## 4. Dominant Schmidt square: use the ACTUAL complex-skew constraint

Suppose, after a label permutation, `x1=1-s>1/2`. Put A=1-s, so0<s<1/2. The other x_j sum to s, and all d_j>=A for j>1. Define

```
T0=sum_(2<=j<k<=4)|Z_jk|^2,
Tstar=sum_(j=2)^4|Z_1j|^2.
```

The weak3x3 block M=(Z_jk)_(j,k>1) is COMPLEX transpose-skew. With w=(c2,c3,c4)^T real, the row constraints give

```
(Z_12,Z_13,Z_14)^T=Mw/c1.
```

Represent M as the cross-product matrix of a complex3-vector a; then `||a||^2=T0`. The complex Lagrange identity with REAL w gives

```
||Mw||^2=||w||^2||a||^2-|w^T a|^2<=s T0.
```

Consequently

```
Tstar<=s T0/A,
||Z||_HS^2=2(T0+Tstar)<=2T0/A.                            (8)
```

This retains arbitrary complex phases. It is precisely the constraint that prevents the potentially negative dominant-star coefficients of(5) from becoming independent tests.

A sharper harmonic bound in this case is

```
r<=rmax(s):=s(3-s)/(3+8s),                               (9)
```

since the three weak d_j sum to3-s and `sum_(j>1)1/d_j>=9/(3-s)`.

Lemma1 gives `g(d_j,d_k)>=2A^2` on weak edges. For a dominant edge, `d1=s` and `d_j` lies in[A,1]. The next lemma gives a complete lower bound over that interval.

## 5. Exact two-endpoint bound for the dominant edges

**Lemma2.** For0<s<=1/2 and b in[1-s,1],

```
g(s,b)>=min{g0(s),g1(s)},
g0(s)=-3+14s-14s^2,
g1(s)=2s-(1-s)^2(3+2s)/(1+s)^2.                          (10)
```

Proof: write T=s+b in[1,1+s]. Direct algebra in(4) gives

```
G_s(T)=g(s,T-s)
 =-2(1-s)T+8s-2s^2-1
       +4s(1-2s)/T-4s^2/T^2,
G_s'(T)=-2(1-s)-4s(1-2s)/T^2+8s^2/T^3,
G_s''(T)=8s[(1-2s)T-3s]/T^4.
```

For0<s<=1/4, `G_s'<=-2(1-s)+8s^2<=-1<0`, so the minimum is at T=1+s. For1/4<=s<=1/2,

```
(1-2s)T-3s<=(1-2s)(1+s)-3s=1-4s-2s^2<0.
```

Thus G_s is concave and its minimum is at one of the two interval endpoints. Substitution at T=1 and1+s gives exactly g0,g1. This proves the full interval statement, including both endpoint possibilities.

## 6. Two complete positive interval identities

Define

```
N0(s)=2(1-s)^3+s g0(s)-2rmax(s),
N1(s)=2(1-s)^3+s g1(s)-2rmax(s).
```

We now prove, on the ENTIRE interval0<=s<=1/2,

```
N0>=1/7,
N1>=83/1512.                                            (11)
```

### 6.1 N0

Clearing the positive denominator3+8s gives

```
(3+8s)N0=6-17s-10s^2+112s^3-128s^4=:P0(s).
```

With t=1-2s in[0,1], the exact decomposition is

```
P0=1+t[10t^2-(17/2)t+7/2]+8t^3(1-t).
```

The quadratic has positive leading coefficient and discriminant `-271/4<0`, so it is strictly positive for all real t. The last term is nonnegative on[0,1]. Hence P0>=1 and `N0>=1/(3+8s)>=1/7`.

### 6.2 N1

Clearing its positive denominator gives the COMPLETE polynomial identity

```
(1+s)^2(3+8s)N1
 =6-5s-44s^2+41s^3+80s^4+10s^5-16s^6=:P1(s).             (12)
```

For t=2s, P1(t/2) has power coefficients

```
a=(6,-5/2,-11,41/8,5,5/16,-1/4).
```

Its degree6 Bernstein coefficients in increasing index are

```
b=(6,67/12,133/30,449/160,31/24,83/96,43/16).             (13)
```

This is a written polynomial identity, not a computer-generated or sampled positivity claim. To make every conversion inspectable, the exact conversion is

```
b_k=sum_(j=0)^k a_j*binom(k,j)/binom(6,j).
```

It gives respectively

```
b0=6,
b1=6-5/12=67/12,
b2=6-5/6-11/15=133/30,
b3=6-5/4-11/5+41/160=449/160,
b4=6-5/3-22/5+41/40+1/3=31/24,
b5=6-25/12-22/3+41/16+5/3+5/96=83/96,
b6=6-5/2-11+41/8+5+5/16-1/4=43/16.
```

All seven coefficients are at least83/96. The Bernstein basis `binom(6,k)t^k(1-t)^(6-k)` is nonnegative and sums to1 on[0,1]. Thus P1>=83/96 on the WHOLE interval. Since `(1+s)^2(3+8s)<=63/4`, identity(12) gives `N1>=83/1512`. No finite parameter grid or unreviewed multivariate characteristic coefficient is involved.

## 7. Finish the uniform actual forcing estimate and joint certificate

Set

```
mu=min(g0,g1)-2r,
Wweak=2A^2-2r.
```

Equations(5), Lemmas1/2 give

```
<Z,rho'Z>-||j||^2 >=Wweak*T0+mu*Tstar.                   (14)
```

Wweak>=1/8 by A>=1/2 and(6). If mu>=0, equation(8) yields

```
(14)>=T0/8>=A||Z||_HS^2/16>=||Z||_HS^2/32.
```

If mu<0, use(8) in the CORRECT direction for its negative coefficient:

```
(14)>=[Wweak+mu*s/A]T0
     =[2A^3+s min(g0,g1)-2r]T0/A
     >=min(N0,N1)T0/A
     >=83 T0/(1512 A)
     >=83||Z||_HS^2/3024.
```

Here(9) and the full interval proofs(11) justify the third/fourth lines; `1/7>83/1512`. Since `83*40>3024`, this is stronger than `||Z||_HS^2/40`. Together with(7) and the mu>=0 case, it proves(2) for ALL positive spectra. No symmetric-spectrum assumption is used: the central/dominant split exhausts the entire simplex, and the dominant index may be any label.

Finally there is the exact full-raw identity

```
J_c(Z,F)
 =(<Z,rho'Z>-||j||^2)
   +(1/2)||F-sqrt(2)j||^2
   +(1/2)F^dagger(K_full-I)F.
```

The imported ACTUAL full K_full-I is positive, and(2) bounds the first term. This proves certificate(3) with every original coefficient and raw correction intact, for arbitrary complex F. Minimizing that actual joint form gives the stated E_full bound. The new work is the forcing domination(2), not the already-known fact that the q pivot or p principal block is positive.

## 8. ENTIRE remaining unrestricted p residual — no full-sign inference

The theorem closes only the antisymmetric p3 compression, with all q6 still present. It does not permit deleting or assuming positivity on the other p9 directions or their mixed terms.

Let the Hermitian operator on H be

```
E_c=rho'-J_c^dagger K_full^(-1)J_c,
```

where the linear map J_c sends Z to its six forcing entries j(Z); the use of J_c for this map here is distinct from the joint scalar J_c(Z,F). Let

```
P_a Z=(1/2)Q(Z-Z^T)Q,
A=range(P_a),
S=H intersect ker(P_a), dim_complex(S)=9.
```

These are orthogonal complex subspaces; neither S nor a general Z in H is assumed transpose-symmetric. Denote the actual blocks by E_AA,E_AS,E_SA,E_SS. The new theorem gives

```
E_AA >= I_A/40.
```

Therefore the FULL original upper-zero sign is now equivalent to the still-unproved NINE-dimensional mixed-complement inequality

```
E_SS-E_SA E_AA^(-1)E_AS >=0 on ALL of S.                  (15)
```

Every E block in(15) contains the full actual K_full inverse and its six-edge forcing. No cross block is assumed zero, no p-only Hodge positivity is substituted, and no new boundary inverse is claimed. A genuine negative direction cannot have its p component wholly in A; it could still use S or mixing, precisely as(15) records. This is the exact first unproved input after the new partial forcing certificate, not a proof of it by a positive pivot.

The previous P11/full18 sign remains NOT_PROVED. The unreviewed inverse-free polynomial presentation and original coefficients remain unchanged; this theorem does not upgrade that gate or rely on sampled coefficient signs. F_up,F_low,Z_low, the asymmetric-route composition and unrestricted rank<=2 W4 all remain separate and NOT_PROVED. A negative route direction would still require a distinct W4 eligibility bridge.

## 9. Evidence, scope and next mathematical task

**Delivered:** one new uniform WRITTEN actual p3/q6 forcing certificate, all positive normalized c, all COMPLEX transpose-skew Zc=0 and all complex q6, with an explicit non-sharp1/40 p margin. No selected reference family, false G13/bare lift, zeroed undo/correction analogue, sampled spectrum or equivalent-representation-only claim is counted as this theorem.

**Not delivered:** the full joint18 positive certificate, a negative actual full-target spectrum, closure of the remaining mixed p9 Schur form(15), any other final sign, W4, novelty clearance, formal/kernel/human/cross-vendor/executable-certificate acceptance, or mathematical exhaustion. The original target has not been reduced: this is an explicitly partial uniform advance with its ENTIRE exact residual.

**Single next task:** prove(15) for all positive c with its genuine mixed forcing, or produce an exact negative value of that actual residual and reconstruct the corresponding full route direction. Do not infer it from the new skew pivot, and do not return to equivalent polynomial repackaging or isolated symmetric spectra. Any scientific interpreter/checker/replay remains unadmitted without a separate exact named GO. All arithmetic identities in this successor were derived in WRITING; no machine-check or historical computation is used or retrospectively authorized.
