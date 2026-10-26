# PH7: a nonuniform shared-block construction through an exact cubic endpoint

Actual returned `/bin/date` before this freeze: **Sun Oct 25 04:02:06 PDT 2026**. MathResearch96h, math-1. New successor, no edits to pinned sources. Review v28-B was completed FIRST in `peer-review-moqls-joint-residual-v1.md`.

**WRITTEN-checked-in-kernel candidate:** the full two-variable characteristic identities and all interval sign certificates below were checked with integers and `fractions.Fraction` in the persistent owner eval kernel. “Kernel” is an arithmetic session, NOT a proof-assistant kernel. No native scientific process, solver launch, model CLI, network publication or nested agent. No independent review or novelty clearance is claimed.

## 1. Full target, new theorem and named imports

For c,d>0, a=c+d, z=b²/d², retain

`H(s)=K/[(s+c)((s+a)²+b²)²]`,  `K=c(a²+b²)²`.

Let ζ be the UNIQUE root in `(77/100,31/40)` of

`384 ζ³ + 144 ζ² - 376 ζ + 27 = 0`.                         (E)

**New construction theorem.** There is a literal seven-state PH realization for EVERY c,d>0 and EVERY `13/20≤z≤ζ`. Both charts and the endpoint are actual matrices, not limiting spectral lists. The interval passes z=3/4 and strictly exceeds 77/100, whereas the previous endpoint was 5935/9126.

**Exact-order composition, at named written imports:** combining the new construction with the retained old upper-seven band and topology-unrestricted B6 yields minimum exactly7 on

`1/2 < z ≤ ζ`.

At z=1/2 minimum remains6. The composition imports:

- **B6:** `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`; prior parent written support excludes ALL PH orders≤6 for z>1/2, not only a companion ansatz.
- **Retained upper7 band:** `proof-seven-state-complex-hidden-extension-v1.md`, SHA256 `023ac8611a66263233288838eaf3dcd3ac0013111a5be93fb5974e7f47e39667`, together with its named earlier G7 import, as composed in `priority-written-dispositions-v1.md` §2. It supplies upper7 on `[1/2,5935/9126]`.

Their acceptance levels are inherited, not upgraded. The exact overlap is `5935/9126 - 13/20 = 31/91260 >0`. New work needs its own independent written reconstruction before parent acceptance. Novelty remains UNCLEAR.

**Point z=8/9 is NOT decided by this theorem.** Since `ζ<31/40<8/9`, the PH7/PH8 minimum gap there remains `{7,8}`. Nothing below is an empty-intersection certificate for the unrestricted system.

## 2. One actual common-matrix template

First set d=1; arbitrary d is recovered by literal time scaling in §7. Use y=s+c and define

`D_z(y)=y[(y+1)²+z]²`,  `K=D_z(c)>0`.

Let `J_u=[-u,1,0;0,-u,1;0,0,-u]`, and similarly J_v. In the fixed R3,o,S3 ordering define the REAL seven-by-seven raw matrix

```
G = [ J_u    e3      0
      0      -w      e1^T
      D      f       J_v ].                                  (1)
```

All entries of D,f will be nonnegative. The blocks are shared ACTUAL entries, including backward D and central returns f; no independently chosen path weights. Let

`Q(y)=y²+p y+q=(y+u)²+B(y+u)+C`,

so `B=p-2u`, `C=q-up+u²`. Put

`beta=(C,B,1,0,0,0,0)`,  `gamma=K e7`.                        (2)

For both charts B,C>0 and p,q>0. The target matrix identity is

`det(yI-G)=D_z(y)Q(y)`.                                      (3)

Because `adj(yI-J_u)e3=(1,y+u,(y+u)²)^T` and

`e1^T adj(yI-J_v)=((y+v)²,y+v,1)`,

the common-block determinant/transfer calculation gives

```
det(yI-G) = (y+w)(y+u)^3(y+v)^3
            -(y+u)^3[((y+v)^2,y+v,1) f]
            -((y+v)^2,y+v,1) D (1,y+u,(y+u)^2)^T,
beta adj(yI-G) gamma = K Q(y).                            (4)
```

Here r=0 is a CHOSEN construction, not an alleged normal form for every PH7. Formula(4) can be derived directly by eliminating the two triangular principal blocks; it does not require assuming the old normal-form theorem. Thus (3) gives the exact raw transfer `K/D_z(y)`. Positive normalization is separately proved in §7.

## 3. Chart I connects the old band to 7/10

Take `13/20≤z≤7/10`, `u=1`, `v=5/4`, and `L=31-32z>0`. Define

```
p=(85-64z)/L,
q=(475/8-58z+64z²)/L,
w=(-1/4+24z)/L,
B=23/L,
C=(43/8-26z+64z²)/L.                                      (5)
```

The equalities `w=p-11/4`, `B=p-2`, `C=q-p+1` are exact. Set f=0 and

```
D = (1/L) [ 0       A(z)    0
            0       B2(z)   0
            C2(z)   0       E2(z) ],                        (6)

A(z)  = -125/256 +(289/8)z +21z² -96z³,
B2(z) =  125/1024 -(289/32)z +(261/4)z² +128z³ -256z⁴,
C2(z) =  (43/8)z² -26z³ +64z⁴,
E2(z) =  125/1024 +(55/32)z -(479/4)z² +16z³ +256z⁴.
```

To make (3) completely inspectable, the full cleared-denominator identity is

```
L (y+w)(y+1)^3(y+5/4)^3
 -D_z(y)[L y²+(85-64z)y+475/8-58z+64z²]
 = A(z)(y+5/4)²(y+1) + B2(z)(y+5/4)(y+1)
   + C2(z) + E2(z)(y+1)².                                (7)
```

No matrix factor is chosen separately from (1),(5),(6). In particular the degree3 feedback comes from actual D12, not a freely assigned numerator term.

p,w,B are strictly positive on this interval. For q its numerator has discriminant `58²-4*64*(475/8)<0` and positive leading coefficient. C has discriminant `26²-4*64*(43/8)<0` and positive leading coefficient. Thus q,C>0 for all real z whenever L>0.

For the four feedback numerators, the following are their COMPLETE Bernstein coefficient lists on `[13/20,7/10]`, in increasing index order. All are positive, proving the signs uniformly, not only at selected z:

- A: `176047/32000, 434933/96000, 328429/96000, 69159/32000`.
- B2: `7215541/640000, 6870083/640000, 6435529/640000, 5901127/640000, 5255101/640000`.
- C2: `524407/80000, 1137487/160000, 3701863/480000, 669459/80000, 181643/20000`.
- E2: `471349/640000, 1651667/640000, 8944283/1920000, 4474263/640000, 6144829/640000`.

Precisely, if t=(z-a)/(b-a), the represented polynomial is `sum_i b_i binomial(n,i)t^i(1-t)^(n-i)`. All basis functions are nonnegative and sum to1. A displayed positive coefficient list is therefore an exact closed-interval sign certificate.

## 4. Chart II extends through the cubic endpoint

For `7/10≤z≤ζ`, take `u=3/2`, `v=1`, `L=13-8z>0`, and

```
p=(45-16z)/L,
q=(81/2-10z+16z²)/L,
w=(-1/2+12z)/L,
B=(6+8z)/L,
C=(9/4-4z+16z²)/L.                                       (8)
```

Here `w=p-7/2`, `B=p-3`, `C=q-(3/2)p+9/4`. Set

```
f=(0,0,F3(z)/L)^T,
D=(1/L) [ D1(z)  0  0
           D2(z)  0  0
           D3(z)  0  0 ],                                (9)

F3(z) = -27/16 +(47/2)z -9z² -24z³,
D1(z) =  81/32 -(73/4)z +(7/2)z² +60z³,
D2(z) =  81/64 -(141/8)z +(69/4)z² +20z³ -16z⁴,
D3(z) =  27/128 -(47/16)z +(77/8)z² +z³ +16z⁴.
```

The complete cleared-denominator identity is

```
L (y+w)(y+3/2)^3(y+1)^3
 -D_z(y)[L y²+(45-16z)y+81/2-10z+16z²]
 = F3(z)(y+3/2)^3 + D1(z)(y+1)² + D2(z)(y+1)+D3(z).       (10)
```

Thus every feedback in (10) is a literal entry of the SAME matrix (1),(8),(9). There is no assumed scalar factor feasibility.

p,w,B>0 for z in the stated range. The q numerator has negative discriminant `100-4*16*(81/2)<0`; C has negative discriminant `16-4*16*(9/4)<0`. Hence q,C>0 when L>0.

For D1,D2,D3 the COMPLETE positive Bernstein lists on the LARGER interval `[7/10,31/40]` are:

- D1: `9641/800, 5569/400, 51317/3200, 2947/160`.
- D2: `15961/40000, 105763/160000, 299027/320000, 194677/160000, 120377/80000`.
- D3: `564443/80000, 2461529/320000, 5365831/640000, 11693909/1280000, 1592461/160000`.

For the remaining entry,

`F3'(z)=47/2-18z-72z² <0` for EVERY `z≥7/10`.

Its exact values are `F3(77/100)=7163/62500>0` and `F3(31/40)=-209/4000<0`. Continuity and strict monotonicity prove the existence and uniqueness of ζ in the declared rational interval. Since `-16F3(z)=384z³+144z²-376z+27`, this is exactly (E). Consequently F3≥0 throughout `[7/10,ζ]`, including F3=0 at the upper endpoint. All other feedback entries remain strictly positive. The zero f3 endpoint is permitted by the actual matrix equations; it is not a limiting PH argument.

## 5. An uncomplicated rational anchor beyond the old band

At z=3/4, Chart II gives

```
p=33/7, q=6, w=17/14, B=12/7, C=33/28,
f=(0,0,3/28)^T,
D=[129/56,0,0;9/56,0,0;285/224,0,0],
Q(y)=y²+(33/7)y+6.
```

The hidden discriminant is `-87/49<0`. This is a genuine complex-hidden cancellation, not two independently selected real phases. Every coefficient and raw boundary is rational.

At c=d=1 the normalized positive vector, computed exactly, is

`h=(7/82,35/164,175/328,875/656,3875/1312,1873/328,7483/656)^T`.

The initial PH row is

`alpha=(33/328,15/41,175/328,0,0,0,0)`,

and the sole exit rate is `omega7=14801/7483`. The literal generator is `T=diag(h)^(-1)(G-I)diag(h)`, with G specified by (1) and this anchor. Its first six row sums are exactly0, last row sum is exactly `-14801/7483`, and all off-diagonals are nonnegative. This is an explicit exact coefficient witness at z=3/4, NOT at z=8/9.

## 6. Hurwitz stability and cancellation

p,q>0 imply that BOTH roots of Q have negative real parts, whether real or conjugate. By (3), eigenvalues of `G-cI` are:

- `-c` once;
- `-(c+1)±i sqrt(z)` each twice;
- the roots of Q shifted by -c.

Every eigenvalue is strictly stable for c>0. The repeated visible poles do not require diagonalizability. Since D_z and Q need not be coprime, the proof is the literal rational identity `KQ/(D_z Q)=K/D_z`; accidental further spectral coincidence would not invalidate it. The reduced target still has its declared double complex poles.

No characteristic factor by itself supplies a PH pair. Here G is Metzler by the actual sign proofs, and the explicit beta and gamma are nonnegative. Equations(3),(4) give the complete raw transfer for generic y, hence as a rational identity.

## 7. Positive normalization and arbitrary c,d

Set `M=G-cI`. It is Hurwitz Metzler, so `(-M)^(-1)=integral_0^infinity exp(Mt)dt` is nonnegative. Every state reaches state7 via the positive forward chain; therefore

`h=(-M)^(-1) gamma >0`.

This is an actual shared-matrix definition, not a missing positive-scaling feasibility assumption. It is also explicit rational data. With `Q_c=Q(c)`, its first four coordinates are

`h_R=(1,c+u,(c+u)²)^T/Q_c`,  `h_o=(c+u)³/Q_c`.

The last three are obtained WITHOUT any unproved sign subtraction by

```
h7 = [K + D_(3,:) h_R + f3 h_o]/(c+v),
h6 = [h7 + D_(2,:) h_R + f2 h_o]/(c+v),
h5 = [h6 + D_(1,:) h_R + f1 h_o]/(c+v).
```

Every quantity is strictly positive. Identity(3) ensures the middle equation `(c+w)h_o=h5`; alternatively these formulas follow by the same scalar block elimination giving (4). Thus they equal the stated inverse vector.

Let Δ=diag(h), `T=Δ^(-1)MΔ`, `alpha=beta Δ`, `omega=Δ^(-1)gamma`. Then T is Hurwitz Metzler and

`T1=-omega≤0`,

`alpha1=beta h=K/D_z(c)=1`,

`alpha(sI-T)^(-1)omega=K/D_z(s+c)=H(s)`.

The initial row has the particularly explicit form

`alpha=(C,B(c+u),(c+u)²,0,0,0,0)/Q(c)`.

It is nonnegative and its sum is1 by Q's actual Newton expansion. No exit-vector independence is assumed: the sole PH exit is exactly `K/h7` at state7.

For arbitrary d>0, perform this dimensionless construction with `c'=c/d` and the same z, then set `T_actual=d T_dimensionless` and leave alpha unchanged. The exit scales by d and the transform is `H_dimensionless(s/d)`, whose numerator and denominator are exactly the required dimensional K and D5. This proves the theorem for every c,d>0, not just one anchor.

## 8. Exact checks, exploration disclosure and open point

The owner's Fraction implementation checked (7) and (10) coefficient-by-coefficient as bivariate polynomials in y,z; both residual dictionaries were identically empty. It independently recombined all actual feedback polynomials. It computed every displayed Bernstein coefficient by the exact power-to-Bernstein formula, checked positivity, checked the rational ζ bracket, and checked the old/new interval overlap. At the c=d=1,z=3/4 anchor, rational Gaussian elimination verified h, alpha, all actual row ties/nonnegative off-diagonals, and the transfer at s=0,1,2,7/3. These four samples are NOT the proof of the full transfer; the full polynomial identities and normalization argument are.

The derivation used exact phase-I linear feasibility inside eval to explore fixed-block coefficient systems before selecting these charts. It also investigated several unequal-rate Newton, cyclic/Hessenberg principal-block, split-real-hidden and other chain allocations. No topology-unrestricted conclusion is inferred from any empty sampled slice. A SymPy import was attempted and unavailable; nothing was installed, and all delivered checks use Fraction/integer code only. No external arithmetic interpreter, scientific program or native solver was launched.

At z=8/9, Chart II would require `f3=-18529/22896<0`, so THAT chart is invalid there. That is not an exclusion of other coefficients or of other actual blocks. The full dominator/shared-system equivalence from `PH7-dominator-normal-form-v1.md` and `PH7-dominator-shared-block-identities-v1.md` remains the unrestricted point obligation, including ALL degree allocations, arbitrary principal blocks, r,D,f, and both real/nonreal hidden roots. No witness or universal empty-intersection certificate at8/9 is supplied by this packet.
