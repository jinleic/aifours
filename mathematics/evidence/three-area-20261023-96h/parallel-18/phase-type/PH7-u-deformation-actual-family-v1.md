# One actual PH7 family: the old cubic endpoint is not a feasibility boundary

Actual returned `/bin/date` before this freeze: **Sun Oct 25 04:47:36 PDT 2026**. MathResearch96h, math-1. WRITTEN ONLY after the parent's correction request. No scientific eval/interpreter, arithmetic program, enumeration, symbolic program, replay or solver. All derivatives and identities below are written algebra, not claimed machine checks. This is a new actual common-matrix constructive branch, not another necessary-only reformulation.

## 1. Claim, imports and honest point status

Let zeta be the previously isolated root

`384 zeta^3+144 zeta^2-376 zeta+27=0`,

`77/100<zeta<31/40`.

**New candidate theorem:** a fully specified algebraic seven-state common-matrix family below works on a closed interval `[zeta,z_new]` with **z_new>zeta**. Therefore the old cubic endpoint is NOT a boundary of PH7 feasibility even within the3+3 chain-principal-block orbit: it was a boundary of the fixed u=3/2 chart. At the retained B6/old-band imports, this extends candidate exact minimum7 to `1/2<z<=z_new`.

The new z_new is defined exactly by ordered roots of explicitly specified polynomials, not numerically evaluated. No rational lower increment beyond zeta is asserted. In particular the definition makes `z_new<8/9`; **the requested unrestricted8/9 decision remains NOT_PROVED**, minimum{7,8}. This is a strict local constructive extension, not a claim of a large advance to the full existence region.

Imports:

- `proof-seven-state-nonuniform-dominator-band-v1.md`, SHA256 `4e490052336693f7f65b1978820aafa600636c421f91a217015d05aeb4928a05`, for the old band and literal Chart II boundary values.
- Its actual written review `physics/evidence/three-area-20261023-96h/parallel-18/werner3-ququart/peer-review-ph7-nonuniform-band-conic-v1.md`, complete335 LF read, for independently written strict positivity of p,q,w,B,C,D1,D2,D3 at zeta and the old whole-band construction. No unadmitted arithmetic observation is a premise. The review's sole rationality qualification is repaired by `PH7-positive-normalization-conic-fibers-author-correction-1.md`; that qualification is not used in this construction.
- B6, `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, only for exact-order composition above1/2.

No dependence on the unreviewed time-reversal reduction is needed. The selected orbit is m=n=3, numerator degrees2+0, with literal actual principal matrices throughout.

## 2. Explicit two-parameter rational coefficients

Work first with d=1, y=s+c, and

`D_z(y)=y[(y+1)^2+z]^2`,  `K=D_z(c)>0`.

Use upstream rate u as a NEW free parameter and fix downstream rate1. Put

```
a=3u+3,
b=3u^2+9u+3,
c3=u^3+9u^2+9u+1,
e4=3u^3+9u^2+3u,
e5=3u^3+3u^2,
e6=u^3,
h0=b+4a-a^2-6,
L=b-4a+10-2z,
N=4h0+4-c3-b(4-a)-4z.
```

Here a,b,c3,e4,e5,e6 are the elementary symmetric coefficients of the SIX literal rates(u,u,u,1,1,1); the symbols a,b in this displayed block are local coefficient names, not the original dimensional pole parameters. Assume L≠0 and define

```
p=N/L,
q=(a-4)p+h0-2z,
w=p+4-a,
B=p-2u,
C=q-up+u^2,
Q(y)=y^2+p y+q=(y+u)^2+B(y+u)+C.
```

Define the following actual feedback entries, all rational functions of u,z:

```
phi=e4+c3*w-[(6+2z)q+(4+4z)p+(1+z)^2],
R2=e5+e4*w-(4+4z)q-(1+z)^2*p,
R1=e6+e5*w-(1+z)^2*q,
R0=e6*w,
D1=R2-3u*phi,
D2=R1-3u^2*phi-2D1,
D3=R0-u^3*phi-D1-D2.
```

Every one of p,q,w,B,C,phi,D1,D2,D3 has denominator L with a polynomial numerator in Q[u,z]. This follows directly from the displayed formulas: all appearances of p,q,w are linear, so there are no unmentioned higher denominator powers.

## 3. The literal common matrix and entire coefficient identity

Let `J_u=[-u,1,0;0,-u,1;0,0,-u]`. Define

```
G(u,z) = [ J_u    e3       0
           0      -w       e1^T
           D       f       J_1 ],

D=[D1,0,0;D2,0,0;D3,0,0],    f=(0,0,phi)^T,
beta=(C,B,1,0,0,0,0),        gamma=K e7.
```

These are ACTUAL entries and boundaries, not independent scalar polynomial factors. The construction sets r=0 by choice and keeps nonzero backwards D and the last-to-center feedback phi.

The full characteristic identity is

```
(y+w)(y+u)^3(y+1)^3-D_z(y)Q(y)
 =phi(y+u)^3+D1(y+1)^2+D2(y+1)+D3.                       (A)
```

Here is a complete coefficient derivation. The degree7 terms cancel by monicity. Degree6 cancels by w=p+4-a. Degree5 gives

`q=(a-4)p+b+4a-a^2-6-2z`,

which is the chosen q. Degree4 then becomes `L p=N`, exactly the chosen p. The residual degree3 coefficient is the displayed phi; the degree2,1,0 residuals are R2,R1,R0. Subtracting phi(y+u)^3 and D1(y+1)^2, then D2(y+1), leaves exactly the displayed D3. Thus all remaining coefficients match. This proves(A) for every u,z where L≠0, not by finitely many samples.

Triangular-block elimination on this SAME G yields

`det(yI-G)=D_z(y)Q(y)`,

`beta adj(yI-G) gamma=K Q(y)`.

The numerator follows from `adj(yI-J_u)e3=(1,y+u,(y+u)^2)^T` and `e1^T adj(yI-J_1)e3=1`. Thus the full raw transfer is K/D_z(y), independently of the feedback coefficient signs. The next sections establish actual simultaneous positivity, rather than assuming it.

## 4. A strict feasible direction at the old endpoint

At u=3/2 the formulas specialize to the old Chart II:

```
p=(45-16z)/(13-8z),
q=(81/2-10z+16z^2)/(13-8z),
w=(-1/2+12z)/(13-8z),
phi=[-27/16+(47/2)z-9z^2-24z^3]/(13-8z).
```

The imported written proof gives strict positivity of L,p,q,w,B,C,D1,D2,D3 at (3/2,zeta), with phi=0 there. It remains to show a concrete direction making phi positive.

Differentiate the actual coefficient definitions at u=3/2 with z fixed. The degree5/4 equations give

```
p_u=96(5-6z)/(13-8z)^2,
q_u=3p+(7/2)p_u-15.
```

Using `a_u=3`, `b_u=18`, `(c3)_u=171/4` and `(e4)_u=201/4`, differentiation of phi gives

```
phi_u=(99/4-6z)p+(105/8-11z)p_u-495/4+30z
      =[1152z^3-1248z^2+402z-135]/(13-8z)^2.             (B)
```

At zeta, its defining cubic reduces the numerator in(B) to

`-6(280 zeta^2-255 zeta+36)`.

The bracket is strictly positive. Indeed it is increasing for z≥77/100 since its derivative is560z-255>0 there, and its left-end value is2831/500>0. Consequently

`phi_u(3/2,zeta)<0`.                                    (C)

Therefore decreasing the actual upstream rate u slightly from3/2 makes phi STRICTLY positive, while all nine other required positivity quantities remain positive by continuity. This is a feasible-direction proof in the actual matrix entries, not a tangent necessary inequality.

## 5. Fully specified algebraic parameters, not an unspecified small epsilon

For an exact literal member and a CLOSED uniform extension, define the polynomial

```
H(u,z)=L*(Lp)*(Lq)*(Lw)*(LB)*(LC)*(Lphi)*(LD1)*(LD2)*(LD3).
```

Each factor is the polynomial obtained by the formulas in §2; this expression specifies H completely without a symbolic-arithmetic program. Its coefficients are rational.

First fix z=zeta. None of its ten factors is identically zero as a polynomial in u: nine are positive at3/2, and Lphi has a nonzero u derivative there by(C). Hence H(u,zeta) is a NONZERO polynomial with finitely many real roots. Define

```
u_left=max({1} union {r in [1,3/2): H(r,zeta)=0}),
u0=(u_left+3/2)/2.
```

The maximum is over a nonempty finite set because1 is included, so this specifies a real algebraic number u0 EXACTLY and gives `1<u0<3/2`. There are no roots on(u_left,3/2). The nine initially strict quantities stay positive throughout this interval, since none can change sign without a zero; phi is positive immediately to the left by(C), and similarly has no zero before u_left. Therefore ALL ten factors have their required positive signs at(u0,zeta). In particular u0 is not defined by assuming feasibility of an unevaluated inequality.

Now H(u0,zeta)>0, so H(u0,z) is not the zero polynomial. Define

```
z_right=min({8/9} union {r in (zeta,8/9]: H(u0,r)=0}),
z_new=(zeta+z_right)/2.
```

This again is a minimum over a nonempty finite set and gives the EXACT algebraic inequalities

`zeta<z_new<z_right<=8/9`.

There is no zero of any factor on[zeta,z_new]. Each factor had the required positive sign at zeta. Thus for EVERY z in that CLOSED interval,

`L,p,q,w,B,C,phi,D1,D2,D3>0`.

The algebraic root-order specification is not a numerical root computation or an interpreter-enumerated certificate. It gives definite algebraic parameters using the same standard finite-root/order operations as an exact isolated-root construction. No numerical location of u_left or z_right is asserted, and no inference is made about whether a boundary root occurs before8/9. In all cases the chosen z_new is strictly below8/9.

## 6. Actual PH pair for every c,d and the strict new band

For u=u0 and each z∈[zeta,z_new], the displayed G is Metzler and beta,gamma are nonnegative. Identity(A) gives all eigenvalues of G-cI: the visible roots -c and -(c+1)±i sqrt(z), the latter twice, together with the roots of Q shifted by-c. Since p,q>0, all roots are strictly stable for c>0.

The positive forward chain reaches state7 from every phase. Hence

`h=(-(G-cI))^(-1)gamma>0`,

`T=diag(h)^(-1)(G-cI)diag(h)`,

`alpha=beta diag(h)`, `omega=diag(h)^(-1)gamma`

form an ACTUAL PH pair: T1=-omega, alpha1=K/D_z(c)=1, and the full transfer is K/D_z(s+c). The entries are explicit algebraic/rational functions of u0,z,c; a positive-scaling feasibility claim is not being left unproved. Equivalently the first four h coordinates and last-three positive backward recurrences are the same formulas from the old common-matrix proof with u now replaced by u0.

For general d>0, construct at c/d and then multiply T by d, leaving alpha unchanged. This is the literal time scaling of the required dimensional target.

The prior upper7 band through zeta and this new closed interval overlap at their ACTUAL zeta point. Therefore upper7 holds through z_new; B6 supplies the lower7 for z>1/2. The old fixed-u cubic endpoint is thereby rigorously crossed by one actual constructive family. No claim is made that z_new is maximal or close to8/9.

## 7. Scope, evidence and unresolved point

This packet performs no finite interpreter check and imports no historical unadmitted arithmetic. Its load-bearing new obligations are the general coefficient identity(A), derivative identity(B), strict feasible direction(C), and the finite-root sign-interval construction. They are all presented as written proofs and need independent written reconstruction before acceptance. The earlier time-reversal5orbits packet remains unreviewed and is not a proof premise.

The unrestricted8/9 target remains open at this owner handoff. A witness there would still require literal actual common-matrix coefficients; an exclusion must cover the whole admissible orbit system. The present family is a successful STRICT LOCAL EXTENSION, not a disguised necessary-only reformulation, a universal orbit exclusion, or an evaluated8/9 witness. No formal/kernel/human/cross-vendor/novelty acceptance, finite-replay credit or new GO is asserted.
