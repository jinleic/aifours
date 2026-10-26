# Werner upper zero — GLOBAL maximal-coordinate edge positivity and an anchored deficit triangle

PhysicsResearch96h-2 / physics-1. **WRITTEN OWNER-CANDIDATE, not parent-read/reviewed/adopted.** Immediately preceding actual `/bin/date`: **Sun Oct 25 17:21:09 PDT 2026**, precreation observation only. Same ENTIRE all-positive-spectrum full complex p12/q6 target. No scientific interpreter/eval/calculator/program, symbolic/numerical computation, enumeration, solver/replay, test/build, scientific CLI, GO or nested agent. All algebra/calculus below is WRITTEN, NOT checked-in-kernel. HOLD and all additive process histories, original October27 cutoff/deadline, and the actual serial-review RETURN boundary remain unchanged.

## 1. Exact inputs and purpose

Use the actual full-raw mass/operator identities in v7, SHA256 `31f993aa031d4affc156f08bfe58ec289eb10d287f2351da0be4938eccb49d08`; the global signless-row budget and exact full-target identity in v9, SHA256 `1a41695f8bbde665338e4daca4fdba41713472cdb20d9490ac78add2a277b616`; and the stronger gF>dij theorem plus exact deficit Gram in v10, SHA256 `8fd87df6cd19dfc1ddd3205ee59ebc090cddb2c962ef337abcf87a2b75350938`.

Their raw import union remains unchanged: generic G1–G12 `249c1becd5e89ff08a3badebaab8234f3e89d7cb7879430e8e9152eabff18a7e`; FALSE-G13 addendum1 `1b0e9a523810b5fb29cfa3c53ad287112d19803dc8110913d1b1f975817e6eb5`; ENTIRE raw Gram addendum2 `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64`; physical K_full/Schur P4/P10 `1a814168eec30b5a8698b669fceae33145862f58c1b380d0f6b679caecf8fe98`, NOT P11; literal four residuals `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277`; original v24 limited identity support `55d24c07c592c8e2e3d5bdd06aa0ca2c6c1ce9d9d2a3a527398251c5b8d29248`. No false G13/bare dual lift, unadmitted arithmetic or external theorem is imported. Ordinary facts: exact positive-factor algebra, derivative monotonicity/log-concavity, endpoint comparisons and elementary finite graph/Gram reasoning.

This successor proves that every edge incident to a LARGEST Schmidt-square coordinate has kappa>0. Thus the v10 potential negative-star case is excluded analytically, and the original sign gate can always be anchored to the triangle on the OTHER three coordinates. This is not yet the sign of that gate.

## 2. Exact scalar quantities for one edge

As before ALL ci>0, sum ci^2=1, xi=ci^2, di=1-xi, r=(sum1/di)^(-1), W=e3(d), dij=(di+dj)/2. For edge ij with complement kl set

```
T=xi+xj, L=1-T, S=2-T,
h=xi*xj, v=xk*xl,
A=di*dj=L+h, B=dk*dl=T+v,
Delta=A(1+T)-BS
     =1-2T+(1+T)h-Sv.                                  (AT1)
```

Here the symbols A,B denote PRODUCTS, not the reciprocal sums used in v10 Section3. The identities W=A(1+T)+BS and r=AB/W give

```
A/(4r)-dij =Delta/(4B).                                 (AT2)
```

Thus `kappa_ij=r-A/(4gF_ij)>0` is equivalent to `gF_ij>A/(4r)`.

V10 gives

```
gF_ij-dij >= 3S T L^2(4-T^2)/(16W).
```

Also `W<=3/2+3TL/4<=27/16`. Consequently it suffices to use the explicit lower bound

```
gF_ij-dij >= eta(T):=S T L^2(4-T^2)/9.                  (AT3)
```

If Delta<=0, positivity follows immediately from gF>dij. If Delta>0, it suffices to prove `4B eta(T)>Delta`. The proof below does this uniformly with exact interval inequalities. No root solve, partition program or spectrum enumeration is used.

## 3. ALL edges with T>=1/2 are positive

Without any maximal-coordinate hypothesis, h<=T^2/4 and v>=0 imply

```
Delta<=f0(T):=1-2T+(1+T)T^2/4.
```

On[1/2,1], `f0'(T)=-2+T/2+3T^2/4<=-3/4`. In particular `f0(1/2)=3/32` and `f0(3/5)=-7/125`. Thus Delta<0 for T>=3/5.

For T in[1/2,3/5], the positive factors obey

```
S T>=3/4, L^2>=4/25, 4-T^2>=91/25, B=T+v>=1/2.
```

Hence

```
eta(T)>=(3/4)(4/25)(91/25)/9=273/5625,
4B eta(T)>=546/5625>3/32>=Delta.                        (AT4)
```

The strict rational comparison is `546*32-3*5625=597>0`. This proves kappa_ij>0 for EVERY positive spectrum/edge with xi+xj>=1/2.

## 4. Edges containing a maximal coordinate: the remaining interval

Now suppose xi is a largest one of the four x values. The remaining case has T<=1/2. Since xk,xl<=xi<=T and xk+xl=L,

```
L<=2T, so T>=1/3,
(T-xk)(T-xl)>=0, so v>=T(1-2T),
B=T+v>=2T L.                                           (AT5)
```

Using this v lower bound and h<=T^2/4 in(AT1) gives

```
Delta<=f(T):=(1-2T)L^2+(1+T)T^2/4
            =1-4T+(21/4)T^2-(7/4)T^3.
```

On[1/3,1/2],

```
f'(T)=-4+(21/4)T(2-T)<=-1/16<0.                        (AT6)
```

From(AT3),(AT5), define a positive exact lower bound

```
4B eta(T)>=R(T):=(8/9) S T^2 L^3(4-T^2)
                 =(8/9)(2-T)^2(2+T)T^2(1-T)^3.          (AT7)
```

The logarithm of R is strictly concave, because

```
(log R)''=-2/(2-T)^2-1/(2+T)^2-2/T^2-3/(1-T)^2<0.
```

Therefore on any subinterval its minimum is bounded below by the smaller endpoint value. Exact endpoint values are

```
R(1/3)=11200/59049,
R(3/8)=401375/2097152,
R(1/2)=5/32,
f(1/3)=5/27, f(3/8)=299/2048.
```

The comparisons needed are all rational:

```
R(3/8)>19/100>R(1/3)>5/27,
R(3/8)>19/100>5/32,
299/2048<5/32.
```

For example `R(1/3)-5/27=265/59049>0`, `R(3/8)>19/100` is `40137500>39845888`, and the last comparison is `299<320`. No decimal approximation is a premise.

On[1/3,3/8], log-concavity gives `R(T)>=R(1/3)>5/27>=f(T)`. On[3/8,1/2], it gives `R(T)>=5/32>299/2048>=f(T)`. Combining with(AT7) proves `4B eta(T)>Delta` throughout. With Section3 this establishes the GLOBAL theorem

```
xi=max_a xa ==> kappa_ij>0 for EVERY j!=i.               (AT8)
```

The largest coordinate need not be unique, and no tie is broken to discard a test. Every edge touching ANY maximal coordinate is positive by the same proof.

## 5. Consequences for the EXACT original deficit gate

Choose an index0 with x0 maximal. By(AT8), every negative-kappa edge is confined to the triangle on{1,2,3}. There is no negative edge through0. This is stronger than merely saying negative edges pairwise intersect; it excludes the unresolved star envelope of v10 as a new theorem, without changing the older source.

Let N>0 be the exact v9 direct sum, C_comp>=0 the ENTIRE actual common-q6 compatible minimum, and

```
L_+=N+C_comp+sum_(kappa_e>0)kappa_e s_e^dagger s_e>0,
s_ij=sqrt(di/dj)Zij+sqrt(dj/di)Zji.
```

For E_- contained in{12,13,23}, let S_- collect the ACTUAL negative edge forms and D_-=diag(-kappa_e). The original operator remains EXACTLY

```
E_full=L_+-S_-^dagger D_- S_-,
E_full>=0 iff I-D_-^(1/2)S_- L_+^(-1)S_-^dagger D_-^(1/2)>=0. (AT9)
```

The last matrix has size at most3 and is now always an anchored-triangle gate, not an arbitrary star/triangle choice. Every row surplus, positive edge, output-c coupling, all complex p directions and actual q6 minimum remain in L_+. The gate is still NOT_PROVED; positive pieces do not imply its sign.

If there are at least TWO tied largest coordinates, negative edges can touch neither, hence at most the SINGLE edge between the other two survives. If there are at least THREE tied largest coordinates, NO negative edge survives and v9 proves actual E_full>0 for every nonzero Zc=0. These are consequences of a global ordering theorem, not an enumeration of reference spectra. With a unique maximum, up to all three deficit edges can survive, as the exact1+3 control in v9 shows.

The already proved global inertia bound remains at most3 negative eigenvalues, with strict positivity on the complex codimension<=3 kernel of the actual negative-edge forms. No conclusion about the sign on their coupled complement is inferred.

## 6. Actual frontier and continuation

NEW GLOBAL WRITTEN progress: all edges with xi+xj>=1/2 are kappa-positive; EVERY edge touching a maximal Schmidt square is positive; and the full original deficit interface is confined to the complementary triangle. The proof uses actual full-raw mass domination, exact normalization, rational endpoint inequalities and log-concavity—not an executed assay, field search, or resurrection of a false certificate.

Still NOT_PROVED: the anchored-triangle Gram in(AT9) at EVERY positive spectrum, full generic E_full/Z_up, the other three canonical F_up/F_low/Z_low signs, whole co-Choi route and unrestricted rank<=2 W4. No exact negative full-target spectrum or physical Werner witness is delivered. Dropping C_comp would still give only a sufficient Praw question, not the original target.

Next genuine action: use the maximal anchor and the actual row-frame/q6 compatibility to bound that three-edge Gram or construct a true separator under authorized evidence rules. A complete joint-source written reconstruction and parent disposition are required for any new claim here. No formal/kernel/configured-family/human/executable/triple-witness/novelty acceptance, GO or park. Original science cutoff2026-10-27T11:05:38-07:00 and delivery deadline12:35:38-07:00 unchanged.
