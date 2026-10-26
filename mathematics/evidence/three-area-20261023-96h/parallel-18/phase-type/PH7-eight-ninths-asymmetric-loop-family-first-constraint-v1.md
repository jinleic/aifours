#8/9 witness direction: a different hidden quadratic and the first unavoidable common-matrix constraint

Actual returned `/bin/date` before this freeze: **Sun Oct 25 06:23:32 PDT 2026**. MathResearch96h, math-1. WRITTEN ONLY; no scientific interpreter/eval/program/enumeration/symbolic program/replay/solver, no nested agent or model CLI. Metadata clocks and actual source reading only.

## 1. Direction, new mechanism and exact outcome

The parent now supports the earlier exact PH8 quotient obstruction, but that result excludes only its fixed hidden pair. This packet does NOT revisit that pair, rebase/shear its quotient, stretch an interval endpoint, or assume principal blocks are WLOG Erlang.

The direction remains an ACTUAL PH7 WITNESS at8/9. The new chosen mechanism is a3+3 common matrix with an ASYMMETRIC INTERNAL TWO-CYCLE in its upstream principal block, all backwards cross-feedback retained, and a genuinely different one-parameter family of real hidden quadratics. The internal cycle changes both the actual adjugate numerator and the available constant/leading feedback budget; it is not another holding-rate perturbation of the prior chain family.

**Outcome:** a complete first-unavoidable-constraint proof shows that this entire literal construction family cannot realize the point. At the representative p=10 candidate the target passes the trace/trace-square screen and all three displayed coefficient signs, yet the required leading-degree feedback already exceeds the available constant budget. Allowing the OTHER nonnegative actual feedback entries cannot repair that coupled contradiction. This closes one concrete witness mechanism, not the unrestricted five-orbit union. No PH7 witness is claimed; minimum remains{7,8} and unrestricted8/9 is NOT_PROVED.

Current authority read: `institute/runs/three-area-2026-10-23-96h/ppt-Dtype-ph8-compression-parent-v1.md`, complete48 LF. Its new support is not backdated before erratum v8. The present calculations do not import the old forbidden quotient spectrum as a candidate or use unadmitted arithmetic.

## 2. A literal common seven-state matrix, not independent polynomial weights

Set d=1,z=8/9 and y=s+c, c>0. Let

`D(y)=y[(y+1)²+8/9]²`

`=y^5+4y^4+(70/9)y³+(68/9)y²+(289/81)y`,

`K=D(c)>0`.

Use the actual principal matrices and forward boundaries

```
A=[-3/2, 1,  0
      2,-3/2,1
      0, 0,-3/2],

F=[-1,1,0;0,-1,1;0,0,-1],
b=(0,0,1)^T,    t=(1,0,0)^T.
```

A is NOT an Erlang block: its1↔2 cycle has nonzero product2. Its roots are -3/2 and -3/2±sqrt(2), all negative since2<9/4; F is also Hurwitz Metzler. These are CHOSEN actual matrices, never asserted to be a normal form for the full orbit.

For p>7/2 put

`w=p-7/2>0`,

`beta_R=(1/20,p-3,1)`,

`Q_p(y)=y²+p y+(3/2)p-21/5`.

The whole raw7-state family is

```
G=[ A     b       0
    r^T  -w       t^T
    Dback f       F ],

beta=(beta_R,0,0),       gamma=K e7,
```

where ALL entries of the ACTUAL r,f,Dback are free nonnegative matrix entries. In particular no Dback or f term is dropped. The corresponding stable raw candidate would be M=G-cI if its target characteristic can be achieved.

The hidden quadratic is Hurwitz throughout p>7/2: its linear coefficient is positive and its constant term is greater than21/20>0. Its discriminant is

`p²-6p+84/5=(p-3)²+39/5>0`,

so it has two negative real roots. This is an allowed2+0 numerator allocation and is not restricted by the three nonreal-pair representatives. The old compression pair `y²+(14/3)y+6` is NOT any member: at p=14/3 this family has constant14/5, not6.

## 3. The actual numerator fixes the hidden family

Write x=y+3/2. Direct triangular/two-cycle elimination gives

```
a_R(y)=det(yI-A)=x(x²-2)
       =y³+(9/2)y²+(19/4)y+3/8,

v(y)=adj(yI-A)b
    =(1,x,x²-2)^T
    =(1,y+3/2,y²+3y+1/4)^T,

a_S(y)=(y+1)³,
w_S(y)=t^T adj(yI-F)=((y+1)²,y+1,1).
```

Indeed x v1-v2=0, -2v1+xv2-v3=0, and x v3=a_R, so(yI-A)v=a_R b. This proves the adjugate column without treating it as free data.

The ACTUAL initial polynomial is

`beta_R v=1/20+(p-3)(y+3/2)+(y²+3y+1/4)`

`=y²+p y+(3/2)p-21/5=Q_p(y)`.

The actual downstream polynomial is w_S(K e3)=K. Hence the literal full adjugate numerator is KQ_p, independently of the feedback choices, by the common-block elimination identity. The hidden polynomial was derived from the same matrix and beta, not independently selected to satisfy trace conditions.

Consequently an admissible witness in this family requires the characteristic identity

`det(yI-G)=D(y)Q_p(y)`.                                  (C)

If(C) held, it would supply all transfer and PH ties; the first unavoidable failure below is therefore not a normalization oversight.

## 4. All PH initial/exit ties would be retained

For clarity, no probability row or exit is being falsely assigned to raw beta,gamma. If(C) held, the spectrum of M=G-cI would be the stable visible target spectrum and the strictly negative roots of Q_p shifted by-c. G is Metzler by its actual nonnegative entries. Every phase reaches state7 through the fixed positive forward chain. Thus

`h=(-M)^(-1)gamma>0`,

`T=diag(h)^(-1)M diag(h)`,

`alpha=beta diag(h)`, `omega=diag(h)^(-1)gamma`

would give ACTUAL PH row/exit ties:

`T1=-omega≤0`, `alpha1=beta h=K/D(c)=1`.

The sole normalized exit would be K/h7 at state7, and the three initial probabilities would be(1/20)h1,(p-3)h2,h3. Similarity would preserve the full target transfer K/D(s+c). This is a proved normalization of the common matrix, not an assumption that beta or gamma is an independently free PH boundary. The subsequent contradiction prevents(C), so no such PH pair is supplied.

## 5. The exact common feedback polynomial

Define E=a_R a_S. Multiplying the two displayed actual principal polynomials gives

```
E(y)=y^6+(15/2)y^5+(85/4)y^4+(233/8)y³
          +(159/8)y²+(47/8)y+3/8.
```

The determinant identity for the SAME G is

```
R_p(y):=(y+w)E(y)-D(y)Q_p(y)
       =a_S(y) r^T v(y)+a_R(y) w_S(y) f
          +w_S(y) Dback v(y).                           (F)
```

Trace chooses exactly w=p-7/2: degree6 of the target is p+4 and the six fixed diagonal holding rates sum to15/2. Thus R_p has degree at most5. Every generator on the right of(F) has NONNEGATIVE coefficients in y, because a_R,a_S,v,w_S all do so as literally printed. This positivity is derived for the chosen matrices, not asserted for an arbitrary shifted basis or every principal block.

Only TWO actual feedback entries have degree5 generators:

- r3 multiplies a_S v3, leading coefficient1 and constant1/4;
- f1 multiplies a_R(w_S)_1, leading coefficient1 and constant3/8.

All other r,f,Dback generators have degree≤4 and nonnegative constants. Therefore(F) forces the COUPLED inequality

`[y^0]R_p >= (1/4) r3+(3/8) f1`

`             >=(1/4)(r3+f1)=(1/4)[y^5]R_p`.             (B)

It also forces `[y^1]R_p>=0`. These are linked actual-entry constraints; allowing independent nonnegative coefficient signs would miss(B).

## 6. Entire p-family contradiction — the first unavoidable constraint

The relevant three coefficients are obtained directly from the displayed E,D,Q_p:

```
[y^5]R_p=(85/4)+(15/2)(p-7/2)
           -[(3/2)p-21/5+4p+70/9]
         =2p-386/45,

[y^0]R_p=(3/8)(p-7/2),

[y^1]R_p=3/8+(47/8)(p-7/2)
           -(289/81)[(3/2)p-21/5]
         =(1130p-11237)/2160.
```

Thus the coefficient[y] nonnegativity already forces

`p>=11237/1130>9`.

But the actual leading/constant feedback budget(B) is

```
[y^0]R_p-(1/4)[y^5]R_p
 = (599-90p)/720 >=0,
```

which forces

`p<=599/90<7`.

These inequalities are incompatible. This is a complete exact infeasibility proof for the WHOLE chosen p>7/2 family, with arbitrary nonnegative r,f,Dback and the actual initial/output numerator. There is no solver, sampled p set, free path-weight substitution, or assertion about all five orbit representatives.

## 7. The representative p=10 passes the requested spectral screen but fails the coupling

This provides a simple literal point candidate with a genuinely different canceled quadratic:

`p=10`, `Q(y)=y²+10y+54/5`,

`w=13/2`, `beta_R=(1/20,7,1)`.

The trace matches exactly: six fixed diagonal holding rates sum to15/2, so the total is14=p+4. The target shifted trace-square is

`4(1-8/9)+(p²-2q)=4/9+100-108/5=3548/45>0`.

The fixed diagonal-square sum is52 and the actual internal two-cycle contributes4. The required remaining two-cycle total is compatible with the leading coefficient equation:

`r3+f1=[y^5]R=514/45`,

`56+2(r3+f1)=3548/45`.

Thus trace/trace-square do NOT themselves reject the candidate and are used only as a screen, as instructed. The actual low coefficient is also positive:

`[y]R=7/240>0`.

The unavoidable failure is instead

`[y^0]R=39/16`,

`(1/4)[y^5]R=257/90`,

`39/16-257/90=-301/720<0`.

The leading-degree entries have already spent more constant determinant budget than exists, even before adding any other nonnegative feedback. Moving weight from r3 to f1 only INCREASES the constant contribution. Adding Dback or other r/f entries cannot repair this. This is the first decisive coupling for the actual family, not a negative trace or a repeated forbidden quadratic.

## 8. Scope and exact remaining gap

This packet consolidates ONE new witness branch and its first unavoidable common-matrix constraint. It closes that asymmetric-internal-loop mechanism for all its hidden parameters; it does not promote the chosen principal matrices to WLOG data, exclude a whole time-reversal orbit, or supply a uniform five-orbit separator. General principal blocks, other diagonal rates, other numerator coefficients and different hidden quadratics remain free in the unrestricted problem.

No actual PH7 witness at8/9 has been found. A replacement witness must change this actual principal/input coupling, not merely redistribute its r,f,Dback feedback, because that full cone is already inconsistent. The initial/exit normalization was proved conditional on the target identity and is not an unresolved implementation prerequisite. Unrestricted8/9 remains NOT_PROVED, minimum{7,8}, at the retained B6/upper8 boundaries. No endpoint extension, same-pair quotient repair, scientific execution, formal/kernel/cross-vendor/human/novelty acceptance or new GO follows.
