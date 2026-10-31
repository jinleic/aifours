# Root-of-unity relative ratios are impossible at every invertible Weyl slope

**WRITTEN + EXACT ALGEBRA/INTERVAL-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at the new exact algebra check: **Wed Oct 28 19:17:15 PDT 2026**. This closes the pair-plus-triangle gap for k=3,7 left open in `frontier-20261028-mub-unit-slopes-primepower-v1.md` SHA **76bb1c6173030280cd4ce9b28bb3b375ad8380bbfa5b4bab5110386b6a96430a**. The root-of-unity conclusion explicitly imports the Lam–Leung small-weight theorem named in the earlier all-root packet; NO unrestricted QLS10 no-go is claimed.

## 1. Statement

For ANY unit `k in {1,3,7,9}` and `D_k=diag(exp(pi*i*k*t²/10))`, no unit vector phi unbiased to the fixed MUB triple `I10,F10,D_k F10` can have its five CRT Schmidt ratios `z_t=b_t/a_t` in a single arbitrary-phase coset of ANY finite group of roots of unity. Thus at least one relative ratio z_t/z_s has an irrational phase modulo2pi. A common phi would, via the earlier Weyl caller, yield a 100-ray 1-RQLS10 with transversal `r=k c` and its shifts; no such phi is found here.

The proof independently excludes (i) a rotated regular fifth-root pentagon and (ii) an antipodal pair plus equilateral triple with arbitrary independent continuous rotations. The root conclusion uses the named Lam–Leung theorem exactly as in `frontier-20261028-mub-all-root-ratio-obstruction-v1.md` SHA **3fac11c5e6f334f543de33bf934b89292df03aba18643efd63659e96fbcd8419**: every minimal vanishing sum of roots of weight<=5 is a regular prime-gon, so any vanishing five-term sum is either a pentagon or a 2-gon plus a 3-gon. Source: https://arxiv.org/pdf/math/9511209v1, Cor.3.4 and Thm.4.8. This named import is not independently reproved.

## 2. Reduction to the new 5D case

CRT gives the 5D bases I,U,B_q, with `U_(t,j)=omega^(3tj)/sqrt(5)`, `B_q=diag(omega^(q t²))U`, `q=4k mod5`, and omega primitive fifth root. The rank-two P=aa†+bb† must have flat diagonal2/5 in all three bases. All non-affine regular-pentagon ratios are excluded for every q by the h=1/h=2 spectral arguments in the prime-power packet; affine pentagons are excluded by the odd-cycle cross-phase lemma. Hence only pair-plus-triangle remains.

A common monomial unitary `T v_t=omega^(eta t²) v_(c t+d)` preserves I and permutes B0,Bq, choosing eta=0 for c²=1 and eta=q for c²=4. Thus pair positions may be sent to0,1; phase and a/b swap normalize any pair-plus-triangle multiset to

`z=(1,-1,lambda,lambda*tau,lambda*tau²)`, |lambda|=1, `tau=exp(2*pi*i/3)`.

These operations preserve the NECESSARY flat-P condition, not necessarily the X/Y cross gates. Exact 4000 basis-exponent identities for every q are in `frontier-20261028-mub-slope2-fifthroot-check-v1.py` SHA **b494559d50e6127106c245b13f76c07fc1e7448ff6bcd5205bd614eeff0356f7**. Coordinate scaling t->2t maps q to -q, so only q=4 and q=3 need checking. q=4 was fully excluded in §§3–4 of the cited all-root packet. Below is q=3.

## 3. Gap one: two forced lambda values

Put `p_t=sqrt(5)*a_t` and `y_t^(h)=5P_(t+h,t)`. Flat B0 and B3 diagonals imply `sum_t y_t^(h)=0` and `sum_t y_t^(h) omega^(-6h t)=0`. For h=1 the Fourier support is `{2,3,4}`. Since z1=-z0, `y0=0`; write

`y_t=c2 omega^(2t)+c3 omega^(3t)+c4 omega^(4t)`, `c2+c3+c4=0`.

For `d_j=(1/5)sum_t |y_t|² omega^(-jt)`,

`d1=c3 conjugate(c2)+c4 conjugate(c3)`, `d2=c4 conjugate(c2)`,
`d1+2d2=-(|c2|²+|c4|²)`.                                 (1)

With lambda=exp(i theta), define `A=2-2cos(theta)`, `B=2+2cos(theta-2pi/3)`. The squared-modulus pattern is `(0,A,1,1,B)`. Taking imaginary parts of (1) gives `(sin(2pi/5)+2sin(pi/5))*(B-A)/5=0`. Therefore A=B, forcing theta=5pi/6 or11pi/6.

Let `g=(1+sqrt5)/2`, `h=(sqrt5-1)/2`. For either branch d1,d2 are real with `d1=(A h-g)/5`, `d2=(-A g+h)/5`.

For theta=5pi/6, A=2+sqrt3, so d1>0 and d2<0. Equation (1) and AM–GM give `d1+2d2<=-2|d2|=2d2`, implying d1<=0: contradiction.

## 4. Small-phase branch: coupled gaps contradict each other

For theta=11pi/6 write `a=2-sqrt3`; then d1<0<d2. From `d2=c4 conjugate(c2)>0` choose a common phase gamma and positive u,v with

`c2=e^(i gamma)u`, `c4=e^(i gamma)v`, `c3=-e^(i gamma)(u+v)`,
`(u+v)²=-d1=(g-a h)/5`, `u v=d2=(h-a g)/5`.             (2)

There are exactly two coefficient branches, related by swapping u,v. Let

`Y_t=u omega^(2t)-(u+v)omega^(3t)+v omega^(4t)`.

Then `y_t^(1)=e^(i gamma)Y_t`, `Y4=conjugate(Y1)`, `Y3=conjugate(Y2)`, `|Y1|²=a`, `|Y2|²=1`.

Define `q_t=p_(t+1)/p_t`. Gap-one weights `w_t=1+z_(t+1)conjugate(z_t)` are

`w=(0,1-lambda,exp(i*pi/3),exp(i*pi/3),1-lambda)`.

For t=1,2,3,4, `q_t=e^(i gamma)Y_t/w_t`. Since `product_t q_t=1`, the missing edge is

`q0=-i exp(-4 i gamma)`.

For gap two, the weights are

`w^(2)=(1+lambda,1-i,exp(-i*pi/3),1-i,1+lambda)`.

Use the exact identities

`(1+lambda)/(1-lambda)=-i(2+sqrt3)`,
`(1-i)/[(1-lambda)exp(i*pi/3)]=-(1+sqrt3)`.

The NECESSARY flat-U gap-two equation `sum_t y_t^(2)=0` reduces, after pairing conjugate terms, to

`0=exp(-3 i gamma)*A0 + exp(2 i gamma)*B0`,                 (3)

where A0,B0 are REAL:

`A0=-(2+sqrt3)*sqrt5*v`,
`B0=-2(1+sqrt3)*R-1`,
`R=Re(Y1 Y2)=sqrt5*u²+(sqrt5/2)u v-(5+sqrt5)v²/4`.       (4)

Therefore (3) requires `|A0|=|B0|`.

The two solutions of (2) have u,v equal to `(S±T)/2,(S∓T)/2`, where `S=sqrt(-d1)` and `T=sqrt(-d1-4d2)`. Rigorous Fraction intervals in `frontier-20261028-slope2-pairtriangle-interval-v1.py`, SHA **55939ecf777e971aa5859d9768887dcbbc5c40363338747b69f286467ffc3474**, use `1.732<sqrt3<1.733` and `2.236<sqrt5<2.237`, with square-root brackets certified by integer squares. They prove:

```text
u>v branch:  0.669 < |A0| < 0.682,   3.714 < |B0| < 3.741
u<v branch:  3.816 < |A0| < 3.832,   0.757 < |B0| < 0.780
```

The intervals are disjoint in BOTH cases, so (3) is impossible for ANY gamma. `frontier-20261028-slope2-coupled-gap-algebra-v1.py`, SHA **c6aa6c2ba2f1af4811030da600db2d137cdbe423281d42f1caa815934662c9e3**, verifies the lambda identities and the coefficients in (4) exactly in Q(zeta60); the cited q=4 packet's checker also independently verifies the h=1 small-branch d1,d2 formulas. This excludes q=3 and, by q->-q, q=2. With the earlier q=4/q=1 proof, the geometric pair-plus-triangle obstruction holds for ALL unit k.

## 5. Limits

The analytic/computer-assisted arguments are unreviewed, and the root-sum classification is an explicit published import. They exclude only root-of-unity cosets of the CRT relative phases in this fixed Weyl/MUB construction, plus the broader pair-plus-triangle geometry. They do not exclude all irrational ratios, other Weyl transversals, noncirculant/nonproduct arrays, or the original unrestricted 1-RQLS10 target. No numerical-search failure is used as a theorem.
