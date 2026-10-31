# All-epsilon weighted gap removal for nonradial parallel-core privacy phases

Owner: InfoResearch96h-2 / info-1. Native clock observed before drafting: `Thu Oct 29 13:59:52 PDT 2026`.

**AUTHOR-WRITTEN candidate with exact owner-run coefficient certificates; NOT independently reviewed or parent-adopted.** The two finite-arithmetic cells in §9 were actually executed and printed the displayed PASS lines. They do not formally verify the geometry, the infinite-gap limit, or the all-law target.

## 0. Main theorem, example, and exact residual

For ε>0 set b=e^(-ε), D={h:||h||_1<=1} with its full CLOSED boundary, and F_b the class of all Borel probability laws satisfying `μ(A)<=b^(-1)μ(A+h)` for every Borel A and every h∈D. Put `J(μ)=E|X|_2^2`, `V_b=inf_(μ∈F_b)J(μ)`, and `Φ_λ(E)=∫_E(|x|_2^2-λ)dx`.

**Theorem A — all-epsilon fixed-core, NONRADIAL parallel phases.** Let C be ANY compact canonical core of §1, with parameter t>=0, including nonconvex cores, squares, diamonds and rounded cores. Let R_0=g>=0 and R_(i+1)>=R_i+1, and set

    K_i=C+R_iD,     K_i^0=C+(g+i)D.

Assume `Σ_i b^i∫_(K_i)(1+|x|^2)dx<∞`. The normalized geometric-phase law P_K is feasible for the full original model. Its cost satisfies

    J(P_K)>=J(P_K0),
    equality iff R_i=g+i for every i.                                    (A)

If any gap exists then, at the TRUE all-law V_b,

    Σ_i b^i[Φ_(V_b)(K_i)-Φ_(V_b)(K_i^0)]>0.                             (B)

The result holds for EVERY finite ε>0, every allowed C, every initial g, and finitely or infinitely many positive gaps; there is no V_b<1/2 requirement. Individual excess terms can be negative. No original-law radiality or independence is assumed: only the PHASES to which this comparison applies are required to have this fixed-C parallel form.

**Concrete genuinely nonradial obstruction.** Take C=[-1/2,1/2]^2, R_0=0 and R_i=i+1/10 for i>=1. These are compact, centrally symmetric, nonradial square/octagonal phase levels obeying every closed-D inclusion. For EVERY b>=1/2, an independent all-law tail bound proves V_b>=17/4, and the first individual signed excess obeys

    Φ_(V_b)(C+(11/10)D)-Φ_(V_b)(C+D)<=-956/625<0.                       (C)

At b=1/2 the ENTIRE weighted excess for this same phase is at least 486731/165000>0. Thus even for a nonradial core, negative first-shell contribution is offset by later mandatory shells. It is a counterexample to the old **per-level sign argument**, not to all-law minimal-shell optimality; the displayed phase is strictly improved by its fixed-core comparator.

**Exact remaining original-target gap.** General optimal Steiner phases have D4/four-direction-convex levels, but the defining inclusions `K_i+D⊆K_(i+1)` do NOT by themselves show all K_i are parallel sets of one common C. Theorem A does not establish that missing shape coherence, nor an aggregate comparison for arbitrary nonparallel levels. Therefore the unrestricted general-ε original J optimization remains OPEN at this proof boundary. No full all-law optimum, book/source equivalence or novelty conclusion is asserted.

### Provenance and review boundary

This is one self-contained successor to `frontier-20261029-uniform-radial-gap-and-signed-shell-obstruction-v1.md`, SHA-256 `52acfa0b5d9a0b883d0ca13b3fb6f77c6633f2c5440476f495c725ee35e9299f`. Its f208 same-harness review returned 0F/0M/1m, with the square condition needing explicit `t>=0`; parent disposition was pending when Main assigned this work. This packet states t>=0 throughout and does NOT cite that review or candidate as an accepted proof premise. The previous radial theorem is recovered as C={0}; the new content is arbitrary canonical C and genuinely nonradial phases.

The same continuing owner authored/consulted earlier LAW642 material and the ln64 packet; no independent-authorship or clean-cognition claim follows. No LAW642 theorem, matching-norm theorem, f208 verdict, or other research result is used as a premise below. Held/withdrawn/ZERO bodies and consumers, MDA26 source text, f161/f162, and protected v214 bodies remain NONINPUT and were not opened for this work. Original scope, historical findings and deadline are unchanged.

## 1. Canonical cores and exact parallel geometry

For t>0 choose a continuous F:[0,t]→R with

    F(t)=t,   t<=F(y)<=2t-y,
    F nonincreasing, and F(y)+y nondecreasing.                            (1)

Let C be the D4 extension of the closed first-octant set `{0<=y<=t, y<=x<=F(y)}`. For t=0 take C={0}. These sets are coordinate down-sets in each quadrant; their boundaries are null. The four-direction-centered sections obtained from the original optimum yield (1) by the anti-diagonal segment argument, but that earlier reduction is not needed as an input for the conditional theorem here.

Examples: F=t gives the square [-t,t]^2; F=2t-y gives 2tD; an arc/facet F can be a rounded core. For t>0, `F=t+(t-y)^2/(2t)` satisfies (1) but gives a nonconvex core, so convexity is not silently assumed.

For x1>=x2>=0, reflection and coordinatewise contraction of a nearest core point give

    d_1(x,C)=(x1-F(x2))_+  when x2<=t,
    d_1(x,C)=x1+x2-2t      when x2>t.                                    (2)

Proof: for x∈Q1, `d_1=x1+x2-max{k1+k2:k∈C∩Q1,k<=x}`. Sort k's coordinates by a swap, which remains dominated by sorted x. If x2<=t and x1>F(x2), the maximum is F(x2)+x2 because F(y)+y is nondecreasing; if x is inside C the distance is zero. If x2>t, all core sums are <=2t and (t,t) attains that value.

Define for r>=0

    A(r)=|C+rD|,       M(r)=∫_(C+rD)|x|_2^2 dx,
    A0=A(0), Q0=M(0), U0=8∫_0^t(F(y)^2+y^2)dy.

Then EXACTLY

    A(r)=A0+8tr+2r^2,
    M(r)=Q0+U0 r+(A0+8t^2)r^2+(16/3)t r^3+(2/3)r^4.                    (3)

To derive (3), integrate one octant and multiply by 8. By (2), for 0<=y<=t the horizontal slice extends from y to F(y)+r. Its moment increment over C is

    r(F^2+y^2)+r^2F+r^3/3.

The added triangle t<y<=t+r/2 has area r^2/4 in one octant. Write x=t+p,y=t+q,s=p+q: its moment is

    ∫_0^r∫_0^(s/2)[(t+s-q)^2+(t+q)^2]dq ds
      =t^2r^2/2+tr^3/3+r^4/12.

Together with `A0=8∫_0^t(F-y)dy`, these expressions give every coefficient in (3). The boundary convention is immaterial to the integrals.

## 2. Three sharp-enough geometric inequalities

Write

    I=8∫_0^t(F-t)dy,
    U=8∫_0^t(F^2-t^2)dy,
    K=8∫_0^t[(F^3-t^3)/3+y^2(F-t)]dy.                                   (4)

All are nonnegative. The square-core baselines and (1) give

    A0=4t^2+I,    U0=(32/3)t^3+U,    Q0=(8/3)t^4+K,
    0<=I<=4t^2,   2tI<=U<=3tI,   0<=K<=tU.                              (5)

The first two inequalities follow from `0<=F-t<=t-y` and `2t<=F+t<=3t`. For the last, factor (F-t) and note

    3[t(F+t)-(F^2+Ft+t^2)/3-y^2]
      =-F^2+2tF+2t^2-3y^2
      >=2(t-y)(t+2y)>=0.

The displayed lower bound uses F∈[t,2t-y], on which the left side is nonincreasing in F. All assertions hold at t=0 with I=U=K=0.

## 3. Strict monotonicity of uniform parallel-core costs

For t+r>0 let `j(r)=M(r)/A(r)`, the cost of the UNIFORM probability on C+rD. It is strictly increasing for every r>=0 at which it is defined.

Indeed let `D=N'Z-NZ'` with Z=A(r), N=M(r). Using (3)–(5), D is affine in U and has coefficient `-Z'<=0` on K. Substituting the upper bound K=tU gives a lower bound affine in U; its minimum over the permitted interval `[2tI,3tI]` is at an endpoint. The two endpoint polynomials, their one explicit correction using I<=4t^2, and the exact nonnegative-coefficient certificate are given in §5. For m=0 and r=q>=0, the certificate gives each endpoint lower bound a positive t^5 coefficient and a positive q^5 coefficient. Thus D>0 whenever t+r>0, proving j'(r)>0.

This is a statement about the actual uniform dilations, not an assumed pointwise sign for every new shell.

## 4. Strict monotonicity of the geometric tail cost for r>=1

Let G be geometric with P(G=k)=(1-b)b^k, and put m=b/(1-b). Let

    Z(r)=E A(r+G),     N(r)=E M(r+G),     J_tail(r)=N(r)/Z(r).           (6)

The normalized density proportional to `b^ceil(d_1(x,C+rD))` has these mass and moment values, by its level-set decomposition. From (3), Z is strictly increasing for r>=1. The same endpoint certificate as §3, now with r=1+q, q>=0 and arbitrary m>=0, proves

    N'(r)Z(r)-N(r)Z'(r)>0,   hence J_tail'(r)>0, for EVERY r>=1.        (7)

Here are the exact formulas used in the certificate. Let H_j=E(r+G)^j. Then

    H1=r+m,
    H2=r^2+2mr+T2,
    H3=r^3+3mr^2+3T2r+T3,
    H4=r^4+4mr^3+6T2r^2+4T3r+T4,
    T2=m+2m^2, T3=m+6m^2+6m^3, T4=m+14m^2+36m^3+24m^4,
    Z=4t^2+I+8tH1+2H2,
    N=(8/3)t^4+K+[(32/3)t^3+U]H1+(12t^2+I)H2
       +(16/3)tH3+(2/3)H4.                                               (8)

The H_j are obtained by elementary geometric factorial moments. Since `(1-b)Σ b^k A(r+k)=Z` and similarly for M, the normalized tail law is a positive mixture of the uniform laws on C+(r+k)D with weights proportional to their areas. Therefore, by §3, if a<r and the uniform C+aD has positive area,

    J_tail(r)>j(a).                                                       (9)

## 5. Reproducible coefficient proof of §§3–4

Let D=N'Z-NZ', where prime means d/dr. From (8), the coefficient of K in D is `-Z'`; Z'>0 for the tail r>=1 and for every nondegenerate uniform case. Thus replacing K by its upper bound tU can only LOWER D. The resulting expression is affine in U. For each j∈{2,3}, let D_j be that expression after U=j tI and K=tU. It follows from (5) that

    D>=min(D_2,D_3).                                                       (10)

Set

    D_3^lo = D_3+(4/3)t^3 I-(16/3)t^5.                                   (11)

Since I<=4t^2, `D_3>=D_3^lo`. The complete exact expansion checked in the first cell of §9 is:

| Domain/substitution | D_2 nonzero terms | D_3^lo nonzero terms | Strictness witness |
|---|---:|---:|---|
| r=1+q, q>=0, m>=0 | 76, all positive coefficients | 75, all positive coefficients | constant 8/3 in each |
| r=q>=0, m=0 | 12, all positive coefficients | 11, all positive coefficients | positive t^5 and q^5 coefficients in each |

These are polynomials over Q in the four NONNEGATIVE variables (t,q,m,I); the uniform case has m=0. The count and coefficients are generated directly from (8), not read from a supplied table. In the second row the only point not covered by strictness is t=q=0, where A(0)=0 and a uniform probability on the singleton is undefined. This proves §§3 and 4.

A preliminary exploratory assertion that the UNshifted arbitrary-m polynomial had all positive coefficients failed: it has negative coefficients. That failure was not a counterexample to monotonicity. The certificate above uses the necessary r>=1 domain, the geometric bounds (5), and the explicit correction (11); the stronger failed coefficientwise assertion is not used.

## 6. Every finite and infinite parallel-core gap

Let a=R_k and suppose the LAST positive gap occurs after level k, of size δ>0; all later increments are one. Denote by u_z the unnormalized minimal-shell density of C+zD. For z=a+1+δ, the phase has the exact nonnegative decomposition

    u_R=(1-b)Σ_(i=0)^k b^i1_(C+R_iD)+b^(k+1)u_z.                        (12)

The gap-removed phase has the SAME prefix and z=a+1. Let the prefix mass be α. If α>0, it is a positive mixture of uniform C+R_iD laws with all R_i<=a, so its cost c<=j(a) by §3. The tail has mass `β(z)=b^(k+1)Z(z)` and cost J_tail(z). For z>=a+1>=1, both increase strictly by §4, and J_tail(z)>j(a)>=c by (9).

Consequently, when α>0 the total cost

    [αc+β(z)J_tail(z)]/[α+β(z)]

increases strictly as z increases; when α=0 it is simply the strictly increasing tail cost. Removing the last gap strictly improves J, preserves the same initial core C+gD, and retains every full-D inclusion. This also covers t=g=k=0, where the prefix is a singleton of zero area.

Remove the last gap repeatedly to handle a finite gap set. For infinitely many gaps, let n-truncation retain R_i through i=n and use unit spacing thereafter. Its radii are <=R_i and converge pointwise to R_i. The sets C+R_i^(n)D are nested inside C+R_iD, so their areas and moments are dominated termwise by the assumed finite series; both phase mass and moment converge by dominated convergence. Pick the first positive gap. Removing every later gap from any sufficiently late truncation leaves the SAME fixed one-gap phase, whose cost is strictly above the no-gap phase by the last-gap argument. This fixed positive difference survives the limit. Thus (A) holds, with equality only if there is no gap at all.

For (B), pointwise set containment gives Z_R>=Z_0. The no-gap comparator is originally feasible, so J(P_K0)>=V_b. With a gap, (A) is strict, hence

    (1-b)Σ_i b^i[Φ_(V_b)(K_i)-Φ_(V_b)(K_i^0)]
      =Z_R[J(P_K)-V_b]-Z_0[J(P_K0)-V_b]>0.

The relevant signed series are absolutely convergent by the finite mass/moment assumption. This is the complete weighted compensation for the precise fixed-C parallel subclass; it does not assume that the separate terms are positive.

## 7. Explicit nonradial negative first shell

We first derive a lower bound for the TRUE V_b without any research input. Every planar feasible law projects to a one-dimensional ε-private coordinate X. Let p(r)=P(|X|>=r). The two unit translates of (-1/2,1/2) are disjoint and lie outside that interval, so

    p(1/2)>=2b[1-p(1/2)],  i.e. p(1/2)>=2b/(1+2b).

Privacy on positive and negative half-lines gives p(r+1)>=b p(r) for r>0. Integrating `E X^2=∫_0^∞2r p(r)dr` over [0,1/2] and [k-1/2,k+1/2], k>=1, yields

    E X^2 >= [2b/(1+2b)] [1/4+2b/(1-b)^2].

Adding both coordinate bounds requires no independence. In particular

    V_b >= [4b/(1+2b)] [1/4+2b/(1-b)^2] >=17/4 for b>=1/2.           (13)

Now let t=1/2, C=[-t,t]^2, R_0=0, and R_i=i+1/10 for i>=1. For this square, (3) specializes to

    A(r)=4t^2+8tr+2r^2,
    M(r)=(8/3)t^4+(32/3)t^3r+12t^2r^2+(16/3)tr^3+(2/3)r^4.             (14)

The first comparison is between r=1 and r=11/10. Exact integration gives area increment 41/50 and moment increment 9777/5000. Combining with (13) gives (C).

For b=1/2, the actual minimal-shell P_C is feasible and (6),(14) give its cost 571/66. The COMPLETE weighted signed excess, at arbitrary λ, is

    Σ_(i>=1)2^(-i)[Φ_λ(C+(i+1/10)D)-Φ_λ(C+iD)]
      =202571/15000-(61/50)λ.                                             (15)

Since the actual V_(1/2)<=571/66, (15) is at least 486731/165000>0 at λ=V_(1/2). Both the negative first-shell inequality and positive full-tail inequality are exact; §9 supplies an independent finite-arithmetic transcription check. The displayed K is a valid example, not asserted to be an optimum.

## 8. What this does—and does not—change

The earlier radial unit-spacing comparison is the special case C={0}. This packet extends the comparison and the all-epsilon weighted signed inequality to EVERY fixed canonical core, including nonradial and nonconvex examples. It does not reduce arbitrary geometric phases to one fixed C, does not establish any nonradial optimizer's levels are parallel, and does not bypass the actual all-law infimum definition.

A sufficient criterion that a particular optimal phase has minimal shells can still be obtained if its own C+D contains the relevant cost ball; that condition is not proved automatically here. In particular, the review-reported domain correction for the older square condition is `t>=0`; no negative-t square is contemplated. No previous packet or parent disposition is modified or retroactively upgraded.

## 9. Complete owner-run exact certificates

The first standalone cell below was run in a fresh Python eval kernel. It printed:

    PASS tail endpoint 2 positive terms 76
    PASS tail endpoint 3 positive terms 75
    PASS uniform endpoint 2 positive terms 12
    PASS uniform endpoint 3 positive terms 11
    PASS nonradial octagon: integral invariants and exact parallel-core costs

It computes the COMPLETE endpoint polynomials from (8), applies exactly the correction in (11), checks each nonzero coefficient is strictly positive, and checks the strictness witnesses stated in §5. The octagon check uses t=1,F(y)=3/2-y/2 and exact rational integrals. It is a finite arithmetic/code check, not a proof assistant verification of §§1–8.

```python
from fractions import Fraction as F

# Sparse exact polynomials in the ordered variables (t,q,m,I).
names=('t','q','m','I')
def var(name):
 e=[0]*4; e[names.index(name)]=1; return {tuple(e):F(1)}
def con(c): return {(0,0,0,0):F(c)} if c else {}
def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,F(0))+v
 return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*F(c) for k,v in p.items() if v*c}
def mul(*ps):
 out=con(1)
 for p in ps:
  result={}
  for k,v in out.items():
   for j,w in p.items():
    a=tuple(k[i]+j[i] for i in range(4))
    result[a]=result.get(a,F(0))+v*w
  out={k:v for k,v in result.items() if v}
 return out
def power(p,n):return mul(*([p]*n)) if n else con(1)
def deriv(p,axis):
 out={}
 for k,v in p.items():
  if k[axis]:
   j=list(k);j[axis]-=1;out[tuple(j)]=v*k[axis]
 return out

t,q,m,I=(var(x) for x in names)
def endpoint(shifted,j):
 # For shifted=True, s=1+q and m is arbitrary. Otherwise s=q and m=0.
 s=add(q,con(1)) if shifted else q
 g=m if shifted else con(0)
 T2=add(g,scale(power(g,2),2))
 T3=add(g,scale(power(g,2),6),scale(power(g,3),6))
 T4=add(g,scale(power(g,2),14),scale(power(g,3),36),scale(power(g,4),24))
 M1=add(s,g)
 M2=add(power(s,2),scale(mul(g,s),2),T2)
 M3=add(power(s,3),scale(mul(g,power(s,2)),3),scale(mul(T2,s),3),T3)
 M4=add(power(s,4),scale(mul(g,power(s,3)),4),scale(mul(T2,power(s,2)),6),scale(mul(T3,s),4),T4)
 A0=add(scale(power(t,2),4),I)
 U=scale(mul(t,I),j);K=mul(t,U)
 Z=add(A0,scale(mul(t,M1),8),scale(M2,2))
 N=add(scale(power(t,4),F(8,3)),K,mul(add(scale(power(t,3),F(32,3)),U),M1),mul(add(A0,scale(power(t,2),8)),M2),scale(mul(t,M3),F(16,3)),scale(M4,F(2,3)))
 D=add(mul(deriv(N,1),Z),scale(mul(N,deriv(Z,1)),-1))
 if j==3:
  # D3 minus (4/3)t^3(4t^2-I), a valid lower bound when I<=4t^2.
  D=add(D,scale(mul(power(t,3),I),F(4,3)),scale(power(t,5),F(-16,3)))
 return D

for shifted,counts in ((True,(76,75)),(False,(12,11))):
 for j,want in ((2,counts[0]),(3,counts[1])):
  p=endpoint(shifted,j)
  assert len(p)==want and all(v>0 for v in p.values())
  if shifted: assert p[(0,0,0,0)]==F(8,3)
  else:
   assert p[(5,0,0,0)]>0 and p[(0,5,0,0)]==F(8,3)
  print('PASS', 'tail' if shifted else 'uniform', 'endpoint',j,'positive terms',len(p))

# Independent explicit nonradial octagonal core: t=1, F(y)=3/2-y/2.
t0=F(1); k=F(1,2)
I0=4*k*t0*t0
U0=8*t0**3*(k+k*k/3)
K0=8*t0**4*(F(7,12)*k+k*k/3+k**3/12)
assert (I0,U0,K0)==(F(2),F(14,3),F(37,12))
assert 0<=I0<=4*t0*t0 and 2*t0*I0<=U0<=3*t0*I0 and 0<=K0<=t0*U0
A=lambda r: F(6)+8*r+2*r*r
N=lambda r: F(23,4)+F(46,3)*r+14*r*r+F(16,3)*r**3+F(2,3)*r**4
assert A(F(0))==6 and N(F(0))==F(23,4)
assert N(F(1))/A(F(1))==F(493,192)
assert N(F(2))/A(F(2))==F(583,120)
print('PASS nonradial octagon: integral invariants and exact parallel-core costs')
```

The following second cell was run separately and printed `PASS square: first excess <= -956/625; all-level excess >= 486731/165000 at b=1/2`. Its exact arithmetic checks (14)–(15) for the named square example, given the written all-law bound (13).

```python
from fractions import Fraction as F
t=F(1,2);b=F(1,2);m=b/(1-b);d=F(1,10)
A=lambda r:4*t*t+8*t*r+2*r*r
M=lambda r:F(8,3)*t**4+F(32,3)*t**3*r+12*t*t*r*r+F(16,3)*t*r**3+F(2,3)*r**4
area=A(1+d)-A(F(1)); moment=M(1+d)-M(F(1))
assert area==F(41,50) and moment==F(9777,5000)
assert moment-F(17,4)*area==-F(956,625)
T2=m+2*m*m;T3=m+6*m*m+6*m**3;T4=m+14*m*m+36*m**3+24*m**4
def ms(s):return [F(1),s+m,s*s+2*m*s+T2,s**3+3*m*s*s+3*T2*s+T3,s**4+4*m*s**3+6*T2*s*s+4*T3*s+T4]
def za(s):
 H=ms(s);return 4*t*t+8*t*H[1]+2*H[2]
def na(s):
 H=ms(s);return F(8,3)*t**4+F(32,3)*t**3*H[1]+12*t*t*H[2]+F(16,3)*t*H[3]+F(2,3)*H[4]
upper=na(F(0))/za(F(0));assert upper==F(571,66)
Ad=(za(d)-za(F(0)))/(1-b)-(A(d)-A(F(0)))
Md=(na(d)-na(F(0)))/(1-b)-(M(d)-M(F(0)))
assert Ad==F(61,50) and Md==F(202571,15000)
assert Md-Ad*upper==F(486731,165000)
print('PASS square: first excess <= -956/625; all-level excess >= 486731/165000 at b=1/2')
```

A separate earlier sweep of 525 exact rational linear-profile parameter combinations found no nonpositive tail derivative. It was exploratory and does not replace the universal coefficient proof. The failed stronger unshifted-coefficient assertion is recorded in §5 and checkpoint010.

## 10. Required review and limits

Request a full disjoint scientific review of: (i) canonical-profile distance and the nonconvex parallel moment identity (3); (ii) the pointwise proof of K<=tU; (iii) every endpoint/correction direction in §5 and the standalone coefficient code; (iv) uniform-versus-tail cost ordering and the zero-area-prefix branch; (v) finite-last-gap removal and the fixed-first-gap infinite-limit margin; (vi) the all-law marginal tail and square-example calculations; and (vii) the explicit nonparallel-level residual.

This is same-harness author work, with finite exact arithmetic but no formal/kernel, human, independent-model-family, novelty, source-equivalence or parent acceptance. The original general-ε nonradial all-law problem remains unresolved beyond the exact parallel-phase subclass.
