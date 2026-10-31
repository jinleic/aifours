# Unique all-law squared-l1 optimizer and rigidity of staircase angular preimages

**AUTHOR CANDIDATE — WRITTEN with exact integer-polynomial identity checks; NOT yet independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 17:12:19 PDT 2026`.

## 1. Scope, imports and new claims

Fix EVERY finite epsilon>0, put `b=exp(-epsilon) in (0,1)`, and `D={h: |h1|+|h2|<=1}`. Let F_epsilon be the entire class of Borel probability laws mu on R^2 with

    mu(A)<=b^(-1)mu(A+h) for EVERY Borel A and EVERY h in FULL CLOSED D.

No symmetry, density, radiality, independent coordinates, attained maximum or restricted event family is assumed of an input law. Define

    W(mu)=integral (|x1|+|x2|)^2 mu(dx),      W=inf_(mu in F_epsilon) W(mu).

This squared-l1 objective is DISTINCT from the registered squared-Euclidean objective `J(mu)=integral(x1^2+x2^2)mu(dx)` and from the first-power l1 objective printed in the Kulesza/PMLR theorem. Its finite minimizer exists by the named MDA matching-norm alternative per-cost reconstruction below; a product-Laplace law separately shows W<infinity.

**New candidate A (all-law uniqueness).** For each epsilon>0, W is attained by EXACTLY ONE Borel probability law, a centered l1-diamond staircase Q_gamma*. No nonradial, translated, discontinuous-version or other law is a second minimizer. Its unique gamma* lies in `(0,1)`, with an explicit globally selected polynomial root in §4. This pays the nonradial squared-l1 uniqueness left open by the prior v253 parent result; it is NOT an independent proof of the registered Euclidean LAW642 theorem or the Euclidean rounded selector.

**New candidate B (source-map preimage rigidity).** Let T be the actual diamond angular-average map from the already parent-supported Kulesza bridge. If ANY mu in F_epsilon has Tmu equal AS A LAW to ANY centered epsilon staircase Q_gamma with `0<gamma<=1`, then mu=Q_gamma as a law. Thus every such staircase has a singleton preimage under T within the full original feasible class. This is stronger than the optimality-only uniqueness and does not assume that the staircase is squared-l1-optimal. It does not imply T never raises squared-Euclidean cost, which is already known to be false.

### Named research inputs and verification ceiling

For A I import the separate parent-WRITTEN_SUPPORTED MDA per-cost alternative proof for the FULL closed norm ball and ANY nondecreasing radial cost, at `institute/runs/three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA-256 `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, especially lines 20–46. The operative complete alternative proof is `information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/privacy-MDA26-norm-monotone-cost-direct-reconstruction-v1.md`, SHA-256 `54cc4fd54fa74bad4c74d857ca7bca028cb0772bffe7771933857ebce52f164a`; its §§2–6 were consulted at lines 43–207. I use its actual privacy-preserving equal-volume radial rearrangement, phase mixture, exact level-growth and parallelization comparison, not its printed-primary proof NR-A/NR-D. I independently establish the STRICT equality consequences, scalar uniqueness and every-original-law conclusion below. No LAW642 or v253 result is a premise of A.

For B I reconstruct the same explicit publisher map and the density bridge in §6 directly, importing only ordinary Tonelli/Radon–Nikodym/Lebesgue differentiation and the planar change of variables. It is compatible with, but does not require, the parent-supported map disposition `dispositions/info-1-angular-cost-and-radial-infimum-parent-v1.md` SHA-256 `5e8fd8ec0cbd42af73a891acff0d8c0073d38e5e3795f558d401f6e5350374b4`.

Standard facts also used: geometric series differentiation, Descartes' rule of signs, the intermediate value theorem, and measure-theoretic layer cake. This is same-harness WRITTEN work with exact algebra checks; no independent-model, human, formal/kernel or novelty gate follows.

## 2. Strict equality in the all-law radial rearrangement

Take ANY original W-minimizer mu; existence and a feasible finite-cost competitor are covered by the named matching-norm result and product Laplace. The MDA alternative proof shows mu has a bounded Borel density p and constructs a pointwise-private nonincreasing radial rearrangement p-sharp with the SAME level-set volumes and no greater radial cost. More explicitly, for every s>0 let `A_s={p>s}`, choose R(s) so `|A_s|=|R(s)D|`, and take `{p-sharp>s}={r<R(s)}`, where `r=||x||_1` and boundary changes are null. The imported model-specific enlargement argument supplies genuine full-D privacy of p-sharp.

For the STRICT equality upgrade, set B_s=R(s)D. When both moments are finite, equal volumes give

    integral_(A_s) r^2 dx - integral_(B_s) r^2 dx
      = integral_(A_s minus B_s) (r^2-R(s)^2) dx
        + integral_(B_s minus A_s) (R(s)^2-r^2) dx.                     (1)

Both terms are nonnegative and strictly positive wherever their corresponding symmetric-difference set has positive area, because a diamond sphere has zero planar area and r^2 is strictly increasing in r. A_s has finite area for s>0. Layer cake and Tonelli show both total costs are integrals of these level costs; the original optimality of p and feasibility of p-sharp force equal finite total costs. Hence (1) is 0 for almost every s, so every such level equals its centered ball a.e. Layer cake again gives p=p-sharp a.e. Thus EVERY original W-minimizer law is radial nonincreasing. No equality claim for costs with flat pieces is being made.

This establishes radiality of the SAME original law, not merely existence of a different rearranged optimizer.

## 3. Every optimal phase has exact unit-spaced radii

Use the amplitude-phase identity of the cited complete MDA alternative proof. Let M=esssup p-sharp. For `a in [bM,M)`, set

    n_a(x)=min{i>=0: p-sharp(x)>a b^i},
    u_a=b^(n_a),   Z_a=integral u_a,   q_a=u_a/Z_a.

The proof supplies positive weights `Z_a da/(1-b)` of total 1 and the exact law/cost mixture of p-sharp by the q_a. Each phase is genuinely full-D private; its finite closed level radii R_i satisfy `R_0>0`, `R_(i+1)>=R_i+1`. Since the mixed cost is exactly W and each phase cost is >=W, almost every weighted phase is itself W-optimal.

For such a phase let its cost be v=W. In the notation of the source's parallelization proof, for radius R>=0,

    B(R)=2R^2,       A(R)=integral_(||x||_1<=R) ||x||_1^2 dx=R^4,
    H_v(R)=A(R)-v B(R)=R^4-2vR^2.

The source constructs one t>0 so every `t+i` lies between R_i and the unique cost-crossing radius `sqrt(v)`, and its signed series is absolutely convergent. Here `H_v'(R)=4R(R^2-v)`, so H_v is STRICTLY decreasing on `[0,sqrt(v)]` and STRICTLY increasing on `[sqrt(v),infinity)`. Every term of its comparison satisfies

    H_v(t+i)<=H_v(R_i),

with equality if and only if `R_i=t+i`. The resulting actual staircase Q_t has cost <=v; original optimality forces equality of costs, and therefore equality of the sums. Since all weights `(1-b)b^i` are positive and all nonnegative deficits are summable, EVERY individual deficit is zero. Thus EVERY optimal phase has `R_i=t+i` for all i and is the actual staircase Q_t.

It remains to rule out t>1. For t>1 the exact layer identity is

    u_(t-1)=b u_t+(1-b) 1_((t-1)D).

After normalization Q_(t-1) is a nontrivial mixture of Q_t and the uniform law on (t-1)D. Q_t itself is a positive volume-weighted mixture of uniform laws on `(t+i)D`, i>=0. Coupling these uniforms by scaling one uniform point of D shows the strictly increasing squared-radius expectation of every `(t+i)D` uniform is strictly larger than that of `(t-1)D`. Thus `W(Q_(t-1))<W(Q_t)=W`, impossible. Consequently `0<t<=1`. The source's `Q_0=Q_1` a.e.-law endpoint is retained; no zero-radius atom is introduced.

## 4. One explicit unique scalar minimizer for EVERY epsilon

Write `m=b/(1-b)>0` and geometric moments

    A=m+2m^2,
    B=m+6m^2+6m^3,
    C=m+14m^2+36m^3+24m^4.

For `0<=gamma<=1`, the staircase has layers `gamma+i`. Geometric-series differentiation gives

    D(gamma)=gamma^2+2m gamma+A,
    N(gamma)=gamma^4+4m gamma^3+6A gamma^2+4B gamma+C,
    W(Q_gamma)=N(gamma)/(2D(gamma)).                                    (2)

D>0. Direct differentiation gives `d W(Q_gamma)/d gamma = P_m(gamma)/D(gamma)^2`, where

    P_m(gamma) = gamma^5 + 5m gamma^4 + (2m+12m^2) gamma^3
               + (12m^3-2m) gamma^2
               - m(1+2m)(1+6m) gamma + m^2(1+2m).                     (3)

The coefficient list in descending gamma powers has signs `+,+,+, either, -, +`: after deleting any zero coefficient, it has EXACTLY TWO sign changes for every m>0. Descartes' rule therefore gives at most two positive roots counted with multiplicity.

The endpoint values are

    P_m(0)=m^2(1+2m)>0,
    P_m(1)=(1+m)^2(1+2m)>0.

Set `gamma_0=2m/(1+4m) in (0,1)`. Exact polynomial expansion gives

    (1+4m)^5 P_m(gamma_0)
       = -m^2 [1+34m+352m^2+1472m^3
                    +2944m^4+2816m^5+1024m^6] < 0.                      (4)

Thus there is a root in `(0,gamma_0)` and another in `(gamma_0,1)`; the Descartes bound makes them the ONLY positive roots and forces both simple. The first is a local maximum, the second is a strict local minimum. In addition `Q_0=Q_1` as laws, so W(Q_0)=W(Q_1). Since the scalar cost rises strictly from the second root to 1, neither endpoint is a minimum. Therefore the SECOND root is the unique global minimizer gamma* on [0,1], and it lies strictly in `(gamma_0,1)`.

Every optimal phase from §3 is Q_gamma*; the phase mixture then equals that single law. By §2 this is the SAME law as every original W-minimizer, so the full Borel law minimizer is unique. In particular this is not merely uniqueness among radial profiles or a single staircase representative.

## 5. Exact algebra checking, with actual output

A bounded local Eval cell used integer polynomial dictionaries, not floats or Sympy. An earlier optional `import sympy` in the preceding scientific work failed because Sympy is absent; no installation was attempted. The following executable Python code is the actual independent check of (3), endpoint signs and (4):

```python
from collections import defaultdict

def poly(*terms):
 d=defaultdict(int)
 for coeff,i,j in terms: d[(i,j)]+=coeff
 return {k:v for k,v in d.items() if v}
def add(A,B):
 d=defaultdict(int,A)
 for k,v in B.items(): d[k]+=v
 return {k:v for k,v in d.items() if v}
def neg(A): return {k:-v for k,v in A.items()}
def mul(A,B):
 d=defaultdict(int)
 for (i,j),a in A.items():
  for (h,k),b in B.items(): d[(i+h,j+k)]+=a*b
 return {k:v for k,v in d.items() if v}
def dg(A): return {(i,j-1):v*j for (i,j),v in A.items() if j}
A=poly((1,1,0),(2,2,0)); B=poly((1,1,0),(6,2,0),(6,3,0))
C=poly((1,1,0),(14,2,0),(36,3,0),(24,4,0))
G=poly((1,0,1)); M=poly((1,1,0)); I=poly((1,0,0))
def pw(X,n):
 out=I
 for _ in range(n): out=mul(out,X)
 return out
def scale(X,k): return {e:k*v for e,v in X.items() if k*v}
D=add(add(pw(G,2),scale(mul(M,G),2)),A)
N=add(add(add(add(pw(G,4),scale(mul(M,pw(G,3)),4)),
           scale(mul(A,pw(G,2)),6)),scale(mul(B,G),4)),C)
P=add(add(add(add(add(pw(G,5),scale(mul(M,pw(G,4)),5)),
    mul(poly((2,1,0),(12,2,0)),pw(G,3))),
    mul(poly((-2,1,0),(12,3,0)),pw(G,2))),
    mul(poly((-1,1,0),(-8,2,0),(-12,3,0)),G)),poly((1,2,0),(2,3,0)))
print('Nprime_D_minus_N_Dprime_equals_2P:',
      add(mul(dg(N),D),neg(mul(N,dg(D))))==scale(P,2))
print('P(m,0) ascending:',[P.get((i,0),0) for i in range(6)])
print('P(m,1) ascending:',[sum(v for (i,j),v in P.items() if i==k) for k in range(6)])
H=poly((1,0,0),(4,1,0)); Num=scale(M,2); sub={}
for (i,j),coef in P.items():
 sub=add(sub,scale(mul(mul(pw(M,i),pw(Num,j)),pw(H,5-j)),coef))
print('(1+4m)^5 P(m,2m/(1+4m)) ascending:',[sub.get((i,0),0) for i in range(9)])
print('all nonzero coefficients negative:',all(v<0 for v in sub.values()))
```

Actual output:

```text
Nprime_D_minus_N_Dprime_equals_2P: True
P(m,0) ascending: [0, 0, 1, 2, 0, 0]
P(m,1) ascending: [1, 4, 5, 2, 0, 0]
(1+4m)^5 P(m,2m/(1+4m)) ascending: [0, 0, -1, -34, -352, -1472, -2944, -2816, -1024]
all nonzero coefficients negative: True
```

A subsequent exact dictionary check evaluated `N(0)D(1)-N(1)D(0)` and returned `True` for equality to the zero polynomial. These checks certify only the displayed formal polynomial identities/arithmetic, not Descartes' theorem, phase equality, density privacy, the original MDA alternative proof, or source/novelty acceptance.

## 6. Stronger singleton preimage for the actual Kulesza angular map

This section uses no optimality or MDA result. Start with ANY original feasible mu. As in the admitted publisher bridge, integrating its event inequalities over D and using Tonelli gives bounded density. The ball-average limsup representative p is finite everywhere, represents the SAME law a.e., and obeys `p(y)>=b p(x)` for EVERY pair with `||x-y||_1<=1`: apply the event inequality to shrinking Euclidean balls. This avoids an uncountable union of density-version null sets.

Parametrize the diamond boundary by `theta(u)`, u in R/(4Z), at constant speed along its four unit-parameter edges. Then `||theta(u)||_1=1`,

    ||theta(u+h)-theta(u)||_1 <= 2|h|

for sufficiently small h, and normalized Lebesgue du/4 is EXACTLY the cone/angular measure. The direct quadrant Jacobian yields

    q(r)=(1/4)integral_0^4 p(r theta(u))du,
    density of Tmu at x is q(||x||_1).

Assume Tmu=Q_gamma as laws, `0<gamma<=1`. Hence for almost every r>0, q(r) equals the staircase's constant value on the shell containing r. Let G be this full-measure set of GOOD radii, excluding all shell boundaries.

Choose good radii `r<s` with `s-r<1` in consecutive shells, so `q(s)=b q(r)`. For every sufficiently small angular shift h with `s-r+2s|h|<1`, the two points `r theta(u)` and `s theta(u+h)` are within the full D. Pointwise privacy gives

    p(s theta(u+h)) >= b p(r theta(u))           for every u.

Integrating du/4 makes both sides equal because angular translation preserves measure and q(s)=bq(r). The nonnegative difference therefore vanishes for a.e. u. Taking h=0 too gives, for EACH small h,

    p(s theta(u+h))=p(s theta(u))                for a.e. u.             (5)

Invariance of an L1 circle function under all shifts in an open interval implies invariance under all circle translations (iterate shifts); Fubini then makes it a.e. constant. The h=0 equality makes the inner-radius angular function constant as well. No simultaneous uncountable exceptional-set assumption is needed: equality holds separately for each fixed h, and the standard L1 translation argument handles the group.

Every good radius is paired with another GOOD radius in the adjacent shell at separation strictly less than 1. For a radius in the top interval `(0,gamma)`, choose an outer good radius in `(gamma,min(gamma+1,r+1))`; the interval is nonempty because gamma<=1 and r>0. For a radius in any later shell, choose an inner good radius in the immediately preceding shell greater than `r-1`; that interval is also nonempty. Full measure of G ensures such a partner exists. Hence the angular function is constant for almost every radius and equals its average q(r). The polar change of variables proves p(x)=q(||x||_1) for Lebesgue-a.e. x. Thus mu=Tmu=Q_gamma AS LAWS, as claimed.

For the gamma=0 endpoint, the level formula gives Q_0=Q_1 a.e. after normalization; it is already covered by gamma=1. The rigidity statement applies to every staircase in this family, including nonoptimal ones, and does not assert that every feasible law has a staircase average.

## 7. Source distinction and exact remaining questions

- The explicit Kulesza PMLR primary's theoretical theorem is about E||X||_1; its same-norm radialization map does not itself print the full squared-l1 unique-law theorem or the registered squared-Euclidean solution. The new strict equality/scalar derivation is not attributed to that printed theorem.
- The named MDA alternative per-cost theorem establishes staircase existence; the present §§2–4 pay new strict equality and phase/scalar steps. Whether equivalent uniqueness appeared elsewhere is unresearched; no worldwide novelty or priority claim.
- Original squared-Euclidean V, Euclidean equality law and rounded transition are not reproved here; SOURCE-MATCH-U1 remains a separate literature/source question. The result does not grant the v253 comparison without its other inputs.
- No prior historical quarantine is treated as a valid premise; immutable prior findings remain historical. Request a disjoint full mathematical review including the equality-cases, all-variable polynomial, and angular-translation measure argument. No full-proof formal/kernel, human, configured-family, executable or novelty acceptance is claimed.
