# Nonparallel phases can beat the same-core minimal shells at the true all-law value

Owner: InfoResearch96h-2 / info-1. Native clock observed before drafting: `Thu Oct 29 14:25:40 PDT 2026`.

**AUTHOR-WRITTEN theorem/obstruction candidate with owner-run exact Fraction checks; NOT independently reviewed or parent-adopted.** This packet is self-contained and makes no LAW642, f208 or f238 theorem a premise. It does not edit the frozen parallel-core packet or assert its review outcome.

## 0. Main result and what it does NOT show

For any `0<b<1` let D={h∈R²:||h||_1<=1}, including its FULL CLOSED boundary, let F_b be all Borel probability laws satisfying `μ(A)<=b^(-1)μ(A+h)` for every Borel set A and every h∈D, and put

    J(μ)=E_μ|X|_2^2,   V_b=inf_(μ∈F_b)J(μ),
    Φ_λ(E)=∫_E(|x|_2^2-λ)dx.

Let C=[-1/2,1/2]^2. Compare these two geometric-phase level sequences:

    S_i=C+iD                         for every i>=0;
    K_0=C,   K_i=(i+1)D              for every i>=1.                     (1)

Both sequences have exact closed-D inclusions; all their sets are compact, convex, D4-symmetric and have centered sections in the axis and diagonal directions. They induce actual feasible laws P_S and P_K in the FULL original class F_b.

**Theorem — uniform nonparallel obstruction.** For EVERY `2/3<=b<1`, equivalently `0<ε<=ln(3/2)`,

    J(P_K)<J(P_S),                                                        (2)
    Σ_(i>=0)b^i[Φ_(V_b)(K_i)-Φ_(V_b)(S_i)]<0.                            (3)

Thus the following plausible bridge is FALSE: “for every feasible geometric phase with canonical levels and a given initial core, replacing all later levels by the initial core's minimal shells cannot increase cost, or cannot increase the signed functional at the true V_b.” It fails even though K_i+D=K_(i+1) for every i>=1, the two phases have exactly the same K_0, and all levels satisfy the usual symmetries.

At b=3/4, the ACTUAL costs are exactly

    J(P_S)=16087/330,   J(P_K)=64957/1338,
    J(P_S)-J(P_K)=2461/12265>0,                                          (4)

and the aggregate signed excess at the true all-law value satisfies

    Σ_i(3/4)^i[Φ_(V_(3/4))(K_i)-Φ_(V_(3/4))(S_i)]<=-325/14<0.            (5)

**Critical limitation.** Neither displayed phase is asserted to be globally optimal. In particular this is NOT a counterexample to minimal-shell structure of an actual all-law optimizer, and it does not prove that any optimizer has nonparallel levels. It is a counterexample to the unrestricted fixed-core comparison/weighted-sign route, so any successful optimizer-level bridge must use additional optimality or shape hypotheses not present in that route.

### Ancestry, control status, and noninputs

Main froze `frontier-20261029-nonradial-parallel-core-gap-removal-v1.md`, SHA `91478ea61fed8a9a5e0f6551d11ced9f3ee890d9e1314c3a387c81a701b52286`, for f238. Its claimed comparison concerns levels that are parallel dilations of one fixed C. The present K sequence is genuinely NONPARALLEL to its first core, as shown in §1; this packet neither relies on nor contradicts f238. No f238 verdict or parent adoption is claimed here.

The f208 review of the older radial packet was returned with 0F/0M/1m but parent disposition was pending at Main's assignment; this packet does not treat it as accepted. Same-author LAW642/bridge exposure is disclosed, not a theorem premise or independent-cognition claim. Historical held/withdrawn/ZERO bodies and consumers/guides, MDA26 source text, f161/f162 and protected v214 bodies remain NONINPUT and were not opened for this work. No prior finding is cured or reclassified.

## 1. Exact full-D feasible phase laws

For S_i in (1), S_i+D=S_(i+1). For K_0=C, `C+D⊆2D=K_1`, since ||c||_1<=1 for c∈C and ||h||_1<=1 for h∈D. For every i>=1, K_i+D=K_(i+1). Both sequences are nested, cover the plane, and consist of compact Borel sets.

For either E=S or E=K, define

    n_E(x)=min{i>=0:x∈E_i},
    u_E(x)=b^n_E(x)=(1-b)Σ_(i>=0)b^i1_(E_i)(x).                         (6)

If h∈D, n_E(x+h)<=n_E(x)+1, including shifts on the boundary, so `u_E(x+h)>=b u_E(x)` pointwise. Their normalizers are finite and positive because the level areas and second moments grow polynomially and b<1. Integrating this pointwise inequality over any Borel A proves the normalized laws P_S,P_K satisfy the ORIGINAL privacy condition for every h∈D. There is no lattice discretization, axis-only substitution or unspecified tail cutoff.

The nonparallel nature is exact. C+rD has maximal axis coordinate 1/2+r and maximal diagonal coordinate 1/2+r/2. K_1=2D has maximal axis coordinate 2 and maximal diagonal coordinate 1. Matching the axis would require r=3/2, which gives diagonal extent 5/4, not 1. Thus no r makes K_1=C+rD.

## 2. Complete shell area and moment difference

For i>=1, K_i=(i+1)D and S_i=C+iD. Direct quadrant integration gives

    |S_i|=1+4i+2i^2,
    M(S_i):=∫_(S_i)|x|_2^2dx
      =1/6+(4/3)i+3i^2+(8/3)i^3+(2/3)i^4.                            (7)

For completeness, in one quadrant the distance to C is `(x-1/2)_++(y-1/2)_+`. The set S_i consists of the base quarter-square, two rectangular strips, and the triangle of shifted coordinates u,v>=0,u+v<=i. Their areas are respectively 1/4, i in total, and i^2/2; their moments after multiplication by four are respectively

    1/6,  (4/3)i+2i^2+(4/3)i^3,  i^2+(4/3)i^3+(2/3)i^4,

which proves (7).

For a radius-r diamond, direct integration gives `|rD|=2r^2` and `M(rD)=(2/3)r^4`. Thus

    |K_i|-|S_i|=1,
    M(K_i)-M(S_i)=i^2+(4/3)i+1/2.                                       (8)

K_i contains S_i by the same triangle inequality as §1. Therefore the difference in (8) is literally the area and moment of the nonnegative added set `K_i\S_i`, not cancellation between unrelated regions. At i=0 the sets coincide.

## 3. Exact added-mass law and aggregate signed difference

Write `m=b/(1-b)`, the normalizers `Z_S=∫u_S`, `Z_K=∫u_K`, and unnormalized moments `N_S,N_K`. Let

    T(m)=17/6+(13/3)m+2m^2.                                              (9)

Because `Σ_(i>=1)b^i=m`, `Σ i b^i=m(1+m)` and `Σ i^2b^i=m(1+m)(1+2m)`, (6) and (8) give

    Z_K-Z_S=b,
    N_K-N_S=b T(m),
    Σ_(i>=0)b^i[Φ_λ(K_i)-Φ_λ(S_i)]=m[T(m)-λ]                            (10)

for EVERY real λ. All signed series converge absolutely.

More structurally, `u_K>=u_S`. The nonnegative added density `u_K-u_S` has mass b and normalized squared cost exactly T(m). Therefore

    P_K=[Z_S/(Z_S+b)]P_S+[b/(Z_S+b)]P_add,                               (11)
    J(P_K)-J(P_S)=[b/(Z_S+b)][T(m)-J(P_S)].

P_add is a probability law, but it is NOT a full-D-private law. For a concrete violation take the positive-area rectangle `A=(7/4,9/5)×(0,1/20)`. It lies in K_1\S_1, so P_add(A)>0. Its unit-left translate is contained in S_1 and hence in every S_i for i>=1, so P_add(A-(1,0))=0. Therefore applying the all-law lower bound V_b to P_add would be invalid. Equations (10)–(11) also explain why optimality of V_b alone cannot justify positivity of an arbitrary excess measure.

## 4. Independent lower bound on the TRUE all-law V_b

For any μ∈F_b, either coordinate X inherits ε-privacy for every one-dimensional shift of magnitude <=1, by pulling back Borel events to the plane. Integer shifts follow by iteration.

Let A=(-1/2,1/2) and p(r)=P(|X|>=r). The translates A+k, k∈Z, are disjoint. Privacy gives `P(X∈A+k)>=b^|k|P(X∈A)`. Summing the disjoint probabilities yields

    P(X∈A)<= (1-b)/(1+b),   p(1/2)>=2b/(1+b).                           (12)

Unlike the weaker two-translate bound, (12) uses ALL integer translates; their union need not contain any boundary atoms for the inequality to hold. For r>0 the two disjoint half-line inequalities give `p(r+1)>=b p(r)`. By layer cake, integrate `2r p(r)` on [0,1/2] and on [k-1/2,k+1/2], k>=1:

    E X^2 >= [2b/(1+b)] [1/4+2Σ_(k>=1)k b^k]
            = [2b/(1+b)] [1/4+2b/(1-b)^2].                              (13)

Sum the coordinate bounds, without independence, and express them in m=b/(1-b):

    V_b>=L(m):=(m+8m^2+8m^3)/(1+2m).                                     (14)

The full class is nonempty (product Laplace is feasible), so V_b is finite. No optimal-law existence is needed for this lower bound.

## 5. Uniform strict negativity for b>=2/3

A direct expansion of (9) and (14) gives

    6(1+2m)[L(m)-T(m)]
       =24m^3-16m^2-54m-17.

When m=2+x with x>=0, the right side is

    24x^3+128x^2+170x+3>0.                                               (15)

Thus for m>=2, equivalently b>=2/3,

    T(m)<L(m)<=V_b.

Using (10) at the ACTUAL global infimum,

    ΔH_(V_b):=Σ_i b^i[Φ_(V_b)(K_i)-Φ_(V_b)(S_i)]
      <=-m[24(m-2)^3+128(m-2)^2+170(m-2)+3]/[6(1+2m)]<0.               (16)

This proves (3) for the whole stated ε interval, including the boundary b=2/3.

Because P_S is feasible, `J(P_S)>=V_b>T(m)`. The added density in (11) has positive mass, so (11) strictly lowers J and proves (2). Equivalently, `Z_K>Z_S` and (16) already force `J(P_K)<J(P_S)`. The same-core constrained infimum is at most J(P_K), which is strictly less than the unique minimal-shell law P_S's cost. This statement does not assert the constrained infimum is attained.

## 6. Explicit rational instance b=3/4

For m=3, the baseline S has exactly

    Z_S=55,   N_S=16087/6,   J(P_S)=16087/330.

Equation (10) gives `Z_K=223/4`, `N_K=64957/24` and `J(P_K)=64957/1338`. Their exact difference is 2461/12265. Also (14) gives `V_(3/4)>=291/7`, while T(3)=203/6. Hence

    ΔH_(V_(3/4))=3[203/6-V_(3/4)]<=-325/14.

These are actual full-shift privacy laws and exact rational inequalities, not floating optimizer results. The only use of the unspecified true V is via the proved all-law lower bound.

## 7. Exact arithmetic certificate

The following standalone Python cell was executed in a fresh owner eval kernel and printed PASS A/B/C. It checks both complete polynomial identities in (8) and (15), and the exact normalizers, costs and signed margin in §6. It does NOT execute or formally verify the written measure, privacy or geometric arguments.

```python
from fractions import Fraction as F
from math import comb

def add(*polys):
 out=[F(0)]*max(len(p) for p in polys)
 for p in polys:
  for i,c in enumerate(p):out[i]+=c
 while len(out)>1 and out[-1]==0:out.pop()
 return out
def scale(p,c):return [F(c)*x for x in p]
def mul(p,q):
 out=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):out[i+j]+=a*b
 while len(out)>1 and out[-1]==0:out.pop()
 return out
def power(p,n):
 out=[F(1)]
 for _ in range(n):out=mul(out,p)
 return out

# Exact area and Euclidean-moment differences, polynomials in shell index i.
i=[F(0),F(1)]
one=[F(1)]
Ad=scale(power(add(one,i),2),2)
As=[F(1),F(4),F(2)]
Md=scale(power(add(one,i),4),F(2,3))
Ms=[F(1,6),F(4,3),F(3),F(8,3),F(2,3)]
assert add(Ad,scale(As,-1))==[F(1)]
assert add(Md,scale(Ms,-1))==[F(1,2),F(4,3),F(1)]
print('PASS A: exact shell excess area 1 and moment i^2+4i/3+1/2')

# L(m)-T(m) identity after clearing 6(1+2m).
Lnum=[F(0),F(1),F(8),F(8)]
T=[F(17,6),F(13,3),F(2)]
poly=scale(add(Lnum,scale(mul([F(1),F(2)],T),-1)),6)
assert poly==[F(-17),F(-54),F(-16),F(24)]
shift=[F(0)]*len(poly)
for k,c in enumerate(poly):
 for j in range(k+1):shift[j]+=c*comb(k,j)*2**(k-j)
assert shift==[F(3),F(170),F(128),F(24)] and all(x>0 for x in shift)
print('PASS B: V_b lower exceeds added-mass cost for every m>=2')

# b=3/4, m=3: exact phase normalizers, costs and true-V signed margin.
b=F(3,4);m=b/(1-b)
Z0=1+6*m+4*m*m
N0=F(1,6)+F(23,3)*m+F(94,3)*m*m+40*m**3+16*m**4
T0=F(17,6)+F(13,3)*m+2*m*m
Zc=Z0+b;Nc=N0+b*T0
assert (Z0,N0,Zc,Nc)==(F(55),F(16087,6),F(223,4),F(64957,24))
J0=N0/Z0;Jc=Nc/Zc;assert (J0,Jc,J0-Jc)==(F(16087,330),F(64957,1338),F(2461,12265))
L=(m+8*m*m+8*m**3)/(1+2*m);assert L==F(291,7)
assert m*(T0-L)==-F(325,14)
print('PASS C: exact full-law comparison and signed upper bound at b=3/4')
```

Earlier in this work, exact rational explorations of several square-to-octagon facet and axial bulges guided the choice of (1); some comparisons had the opposite sign. Float renderings were diagnostics only. The universal interval and the written theorem rely on (8), (14) and (15), not on a finite grid or decimal calculation.

## 8. Review priorities and scientific boundary

Request a complete disjoint review of the every-closed-D privacy construction, exact Minkowski geometry and added sets, absolute convergence of (10), the all-integer marginal event bound (12), the layer-cake interval endpoints, the polynomial sign (15), and the normalization/cost distinction in (11). In particular verify that P_add is not treated as private and that no optimizer claim is inferred from this nonoptimal phase.

This is written/same-harness author work with exact finite arithmetic; it is not human/independent-model-family review, formal/kernel verification, source-equivalence, novelty or parent acceptance. The original general-ε optimizer/coherence problem remains open. A prospective successful bridge would have to exploit genuine OPTIMAL-phase restrictions or a different invariant; (1) rules out the unconditional same-core aggregate comparison as a valid route.
