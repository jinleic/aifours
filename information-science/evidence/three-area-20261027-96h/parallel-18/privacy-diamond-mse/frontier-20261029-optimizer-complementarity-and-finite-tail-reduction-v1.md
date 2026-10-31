# All-epsilon optimal-phase complementarity and an exact finite-profile reduction

Owner: InfoResearch96h-2 / info-1. Native clock observed before drafting: `Thu Oct 29 15:00:52 PDT 2026`.

**AUTHOR-WRITTEN candidate; NOT independently reviewed or parent-adopted.** The exact owner-run arithmetic controls in §9 check only the named finite polynomial identities. They do not verify the infinite-dimensional optimization, measure theory, Steiner arguments or theorems below.

## 0. Main results and exact scientific boundary

For ε>0 write b=e^(-ε), D={h∈R²:||h||_1<=1} with its FULL CLOSED boundary, and F_b for all Borel probability laws satisfying `μ(A)<=b^(-1)μ(A+h)` for EVERY Borel A and EVERY h∈D. Put `J(μ)=E|X|_2^2` and `V=inf_(μ∈F_b)J(μ)`.

**Theorem A — optimizer-level complementarity and eventual shape coherence, every ε>0.** V is attained and finite. Every optimal law admits an exact mixture of optimal geometric phases. For almost every phase, there are compact canonical essential-support levels K_i with exact `K_i+D⊆K_(i+1)`, and the following NECESSARY conditions hold for the ACTUAL V:

1. `K_0⊆B̄(0,sqrt(V))`.
2. For every i>=1,

       K_(i-1)+D ⊆ K_i ⊆ (K_(i-1)+D) ∪ B̄(0,sqrt(V)).                 (A1)

3. For every i>=0, with `E⊖D={x:x+D⊆E}`,

       |[(K_(i+1)⊖D)∩B(0,sqrt(V))] \ K_i|=0.                            (A2)

   Equivalently the exact essential-support recurrences in §4 hold. Thus unforced material is confined to the cost ball, and within that ball every positive-area point whose whole D-shift is allowed by the next level is already included.
4. For every integer `i>=ceil(sqrt(2V))`,

       K_i=K_(i-1)+D EXACTLY.                                            (A3)

   In particular all sufficiently far levels are parallel dilations of ONE tail core, without assuming initial-core parallelism or V<1/2. Since the feasible product-Laplace law has cost 4/ε², the explicit universal cutoff

       N=ceil(2sqrt(2)/ε)                                                 (A4)

   always works: the only possibly nonminimal transitions are i=1,...,N-1.

The exactness in (A1),(A3) is for the constructed essential-support representatives, not an assertion that arbitrary Borel versions are literally equal.

**Theorem B — attained finite-profile reformulation, every ε>0.** With N from (A4), the original ALL-law V equals the attained minimum of the explicit ratio (B1)–(B4) in §7 over N nested canonical Lipschitz profiles. The infinite geometric tail is eliminated exactly; each of the first N profiles remains an unknown function, so this is still a finite-*number*-of-functions variational problem, not an elementary scalar solution. The same minimum holds after imposing the finite optimizer-level self-consistency constraints in §7.4.

**Remaining gap:** decide that finite nonparallel prefix variational problem, or prove stronger optimizer-level coherence. Local complementarity and eventual minimal tails are NECESSARY, not sufficient for optimality; §8 recalls the separately parent-supported f245 counterexample to their sufficiency. No general-ε uniqueness, value formula, source/book equivalence, novelty, or formal proof is claimed.

### Ancestry and inputs

The earlier `frontier-20261029-lawfree-lower-half-v1.md`, SHA `ddd3fc87bd38475500589957e030119de451c6fa5f0b27ea54fb8e0856ea62ea`, reconstructed the phase/Steiner/essential-support machinery for the ln64 result. Its parent disposition supports ln64 only. The f238 parent disposition `a0d8d728e66fc256495cd08b5644f2688051fe7fe2edf8b6aa4da4d76529e9ba` expressly did NOT adopt an optimizer-structure aside. This packet rederives the required all-ε preliminaries and makes neither disposition a theorem premise.

The separately adopted f245 disposition `a5005ac8173be0b0c05bb5eb3cb82678ac22b1ae90de2c4d4a418f301d98a711` is used ONLY for the optional insufficiency corollary in §8, not for Theorems A–B. No f238 fixed-core comparison, f245 counterexample, LAW642 theorem or external matching-norm result is a premise of the main proof. Same continuing author and prior LAW642/bridge exposure are disclosed; no clean-cognition or independent-authorship claim follows. Historical held/withdrawn/ZERO bodies, consumers/guides, MDA26 source text, f161/f162 and protected v214 bodies are NONINPUT and were not opened for this packet. Earlier findings are not rehabilitated.

## 1. Attainment and an everywhere-private density

The product-Laplace density `(ε²/4)e^(-ε||x||_1)` satisfies the full shift condition and has J=4/ε². A minimizing sequence has uniformly bounded second moment, so Markov tightness and Prokhorov give a weak probability limit. For fixed h∈D, the measure inequality passes to nonnegative bounded continuous test functions and then, by closed-set approximation and Borel regularity, to every Borel event. The squared cost is weakly lower semicontinuous as the supremum of integrals of min(|x|²,R). Therefore V is finite and attained. V>0: an attained probability with zero squared cost would be δ_0, which fails privacy for the event {0} and any nonzero h∈D.

Integrate the original privacy inequality over the area-two diamond. Tonelli gives, for every Borel A,

    2b μ(A)<=∫_D μ(A+h)dh=∫|D∩(x-A)|dμ(x)<=|A|.                        (1)

Thus μ has a density bounded by 1/(2b). Set `f(x)=limsup_(r↓0, r rational) μ(B_r(x))/|B_r|` using Euclidean balls. It is Borel, bounded everywhere by 1/(2b), and is the density a.e. by differentiation. Comparing each pair of shifted balls gives

    f(x+h)>=b f(x) for EVERY x∈R² and EVERY h∈D.                         (2)

It is positive at some point and therefore everywhere by a finite chain of D-shifts. Let M=sup f∈(0,1/(2b)].

## 2. Every optimum is a mixture of optimal geometric phases

For a∈(bM,M), let `E_i(a)={f>ab^i}`, `n_a(x)=min{i>=0:x∈E_i(a)}`, and `u_a=b^n_a`. By (2), `E_i+D⊆E_(i+1)` exactly, n_a is finite, and u_a itself satisfies the every-point version of (2). E_0 has positive area: if f(x)>a, some sufficiently small ball has μ-average greater than a, so the density exceeds a on a positive-area subset of that ball.

For every x the phase identity is

    ∫_(bM)^M u_a(x)da=(1-b)f(x).                                         (3)

Indeed put f(x)=Mb^κ with κ>=0, a=Mb^σ, σ∈(0,1). Then n_a is the least n>=0 with σ+n>κ. The quantity σ+n runs once, piecewise with unit slope, through (κ,κ+1], so the integral is `∫_κ^(κ+1)Mb^w|log b|dw=(1-b)f(x)`.

Tonelli applied to (3) gives `∫Z_a da=1-b` and `∫N_a da=(1-b)J(μ)`, where Z_a,N_a are the mass and squared moment of u_a. For a.e. a they are finite, Z_a>0, and P_a=u_a/Z_a is originally feasible. With `w(a)=Z_a/(1-b)`,

    μ=∫w(a)P_a da,   ∫w=1,   J(μ)=∫w(a)J(P_a)da.                        (4)

If μ is optimal, J(P_a)=V for a.e. a, because all P_a are feasible. Fix any such optimal phase and suppress a. Its Borel sets E_i have positive E_0 area, finite individual area/moment, and

    E_i+D⊆E_(i+1),
    Z=(1-b)Σ_i b^i|E_i|,   N=(1-b)Σ_i b^i∫_(E_i)|x|²dx,
    N-VZ=(1-b)Σ_i b^iΦ_V(E_i)=0.                                        (5)

Both positive series converge, so the signed series is absolutely convergent.

## 3. Four strict Steiner equalities and exact compact levels

For a unit direction e, let S_e center each measurable section of a set on the line e^perp, preserving that section's length. Use the two axes and the two diagonal directions. The centered interval uniquely minimizes ∫w² over a line section of a fixed length, up to null sets; hence S_e preserves area, does not increase ∫|x|², and equality at finite moment implies the original set equals S_e of it a.e.

For each of these four directions D has centered interval sections. If A+D⊆B exactly, then `S_e A+D⊆S_e B` exactly: a section of B contains a section of A plus the appropriate centered interval of D, whose one-dimensional length is at least the section length of A plus the interval length. This follows for compact subsets by adding two endpoint intervals and then for Borel sections by inner regularity. Infinite-length sections use arbitrarily large compact subsets. Axis fibers have half-length 1-|q|; in orthonormal diagonal coordinates D is a square of half-side 1/sqrt(2).

Apply EACH S_e separately to all levels of the fixed optimal phase. The new phase remains feasible, has the same Z and no greater N, so optimality forces equality in the summed nonnegative moment reductions. By (5), every level has equality for every direction. Thus

    E_i=S_e E_i a.e. for EACH i and EACH of the four directions.           (6)

This is not an assertion that four successive operations automatically preserve earlier symmetries.

Let `K_i=supp_ess(E_i)={x:|E_i∩B_r(x)|>0 for every r>0}`. The double axis symmetrization of E_i agrees with E_i a.e. and is a coordinate down-set: after horizontal symmetrization, vertical symmetrization has a section-length function even and nonincreasing in |x|. Such a set has null boundary, since away from countably many jumps its boundary has at most one point per vertical fiber. Hence it agrees a.e. with its essential support. Consequently K_i=E_i a.e., so the phase law is unchanged.

For a set with centered interval e-sections, its essential support has closed centered interval e-sections on EVERY line: the contraction `(p,w)↦(p,αw)`, 0<α<=1, sends the set into itself, maps a ball into a ball and scales positive area by α; reflection and α→0 finish the claim. Applying this to each of (6), K_i has centered sections in all four directions and D4 symmetry. Positive area and the axis sections give a neighborhood of 0 in K_i. If x∈K_i, put s=||x||_1. The anti-diagonal segment to its swap contains (s/2,s/2), and the centered axis sections contain the square [-s/2,s/2]^2; hence `s²<=|K_i|<∞`. Thus every K_i is compact.

Finally the original set inclusion gives an EXACT closed-D inclusion of supports. For x∈K_i and h∈D, `(E_i∩B_r(x))+h` has positive area inside `E_(i+1)∩B_r(x+h)` for every r>0. Therefore

    K_i+D⊆K_(i+1) EXACTLY,   0∈int K_0,   K_i=supp_ess(K_i).             (7)

No unjustified a.e.-replacement inside a Minkowski sum is made.

## 4. One-level variations give optimizer complementarity

Write B°=B(0,sqrt(V)), B̄=closure(B°), and `E⊖D={x:x+D⊆E}`. For compact E, E⊖D is compact: it is the intersection of closed translates E-h and is a subset of E since 0∈D.

### 4.1 Remove unforced high-cost material

For i>=1 replace ONLY K_i by

    K_i'=(K_(i-1)+D) ∪ (K_i∩B̄).

It is compact, is contained in K_i, contains K_(i-1)+D, and satisfies K_i'+D⊆K_(i+1). All other levels stay unchanged. Thus the modified phase is a full-D feasible law with finite mass and moment; it need not retain canonical symmetry. If the removed set had positive area, its integral of |x|²-V would be strictly positive and (5) would become strictly negative, contradicting optimality. Therefore `K_i\[(K_(i-1)+D)∪B̄]` is null. The bracketed set is closed, and K_i is its own essential support, so this inclusion is in fact EXACT. This proves (A1).

For i=0, the same argument with `K_0'=K_0∩B̄` proves K_0⊆B̄ exactly. It is nonempty and has positive area because V>0 and 0∈int K_0.

### 4.2 Add available low-cost material

For any i>=0 and r<sqrt(V), replace ONLY K_i by

    K_i'=K_i ∪ [(K_(i+1)⊖D)∩B̄(0,r)].

The added compact set plus D lies inside K_(i+1); previous inclusion is preserved because K_i only grows. If it added positive area, its integral of |x|²-V would be strictly negative and the modified feasible phase would beat V. Letting r↑sqrt(V) over a countable sequence proves (A2). The original inclusion already gives `K_i⊆K_(i+1)⊖D` exactly.

Combining (A1),(A2), and the fact that the circle |x|²=V has zero area gives the following exact essential-support equations:

    K_0=supp_ess[(K_1⊖D)∩B°],
    K_i=supp_ess[(K_(i-1)+D) ∪ ((K_(i+1)⊖D)∩B°)]  for i>=1.          (8)

The sets on the right equal K_i a.e.: outside B̄ only the forced previous dilation remains; inside B° K_i lies in the next erosion and every extra erosion point is null; the boundary circle is null. Taking essential supports is therefore legitimate. No claim is made that the raw erosion inclusion itself is literal on zero-area components.

## 5. Exact common tail and a uniform finite cutoff

By (7), inductively K_(i-1)+D contains K_0+iD and hence iD. The l1 diamond iD contains the Euclidean ball of radius i/sqrt(2). If i>=ceil(sqrt(2V)), it contains B̄. The exact sandwich (A1) therefore reduces to

    K_i=K_(i-1)+D EXACTLY.                                                (9)

Even using only the a.e. version of the pruning argument, this equality is literal for the chosen representatives: a compact A+D is its own essential support. Indeed every point a+d can be approximated by a+d' with d'∈int D, and every neighborhood of a+d meets a positive-area ball inside a+D. Since K_i is also its own essential support, its a.e. equality with K_(i-1)+D implies set equality.

For any explicitly known bound U>=V put `N(U)=max(1,ceil(sqrt(2U)))`. Equation (9) holds for all i>=N(U). Choosing U=4/ε² yields (A4). All optimal phases of every optimal law therefore have one common-core tail beginning at K_(N-1), although different phases may initially have different cores. No conclusion that K_i=K_0+iD for the finite early levels is made.

## 6. Canonical profiles and their exact parallel moments

For each compact K_i from §3 set `t_i=max{s>=0:(s,s)∈K_i}` and let F_i(y) be the maximum horizontal coordinate of K_i at height y, 0<=y<=t_i. Its first-octant part is `0<=y<=t_i, y<=x<=F_i(y)`. Axis sections make F_i nonincreasing. F_i(t_i)=t_i; otherwise the anti-diagonal segment to the swap would contain a larger diagonal point. For y<=y'<=t_i, this same segment from (F_i(y),y) to its swap contains `(F_i(y)+y-y',y')`, giving F_i(y)+y<=F_i(y')+y'. Thus

    t_i>=0,  F_i(t_i)=t_i,  t_i<=F_i(y)<=2t_i-y,
    F_i nonincreasing,  F_i(y)+y nondecreasing.                           (10)

In particular F_i is 1-Lipschitz and continuous. For t=0 use C={0}. Conversely, D4-extending any profile (10) gives a compact coordinate down-set C; every candidate in §7 built from such cores remains feasible, even if extra symmetry beyond (10) is not separately asserted.

For a canonical C=C(t,F), reflection and coordinatewise contraction of a closest point give, in x1>=x2>=0,

    d_1(x,C)=(x1-F(x2))_+  if x2<=t,
    d_1(x,C)=x1+x2-2t      if x2>t.                                    (11)

Indeed d_1=x1+x2-max{k1+k2:k∈C∩Q1,k<=x}; sorting k remains dominated by sorted x, F(y)+y is nondecreasing, and the diagonal point (t,t) attains the outer maximum.

Define

    A=8∫_0^t(F-y)dy,
    Q=8∫_0^t[(F³-y³)/3+y²(F-y)]dy,
    B=8∫_0^t(F²+y²)dy.                                                   (12)

These are respectively |C|, ∫_C|x|², and the first parallel moment coefficient. For r>=0, (11) and one-octant integration give

    |C+rD|=A+8tr+2r²,
    ∫_(C+rD)|x|²dx=Q+Br+(A+8t²)r²+(16/3)tr³+(2/3)r⁴.                  (13)

The strip y<=t contributes moment increment `r(F²+y²)+r²F+r³/3`. The remaining triangle t<y<=t+r/2 has octant area r²/4 and moment `t²r²/2+tr³/3+r⁴/12`. Multiply by eight and combine. No convexity of C beyond (10) is used.

## 7. Explicit finite-profile variational problem

Fix N=N(U), with any known U>=V; (A4) supplies one for every ε. Let P_N be all N-tuples `(t_i,F_i)`, i=0,...,N-1, satisfying (10), with their corresponding compact C_i satisfying C_i+D⊆C_(i+1). The exact profile form of this inclusion is

    t_(i+1)>=t_i+1/2,
    F_(i+1)(y)>=F_i(y)+1                    for 0<=y<=t_i,
    F_(i+1)(y)>=2t_i+1-y                   for t_i<=y<=t_i+1/2.          (B1)

This follows from (11), whose `d_1<=1` sublevel has precisely that two-piece octant boundary. For t_i=0 the first interval is a singleton and the second describes D. These conditions are both necessary and sufficient for the actual set inclusion by D4 symmetry.

For each tuple define levels C_0,...,C_(N-1), then C_(N-1)+jD for j>=1. They satisfy every closed-D inclusion, so the resulting phase is originally feasible. Let A_i,Q_i,B_i be (12), let G be geometric with P(G=j)=(1-b)b^j, and put

    m=EG=b/(1-b),  T2=m+2m²,
    T3=m+6m²+6m³,  T4=m+14m²+36m³+24m⁴.

Writing t=t_(N-1), A=A_(N-1), Q=Q_(N-1), B=B_(N-1), the last core's unnormalized shell mass and moment are

    Z_tail=A+8tm+2T2,
    N_tail=Q+Bm+(A+8t²)T2+(16/3)tT3+(2/3)T4.                           (B2)

These are E|C+GD| and E∫_(C+GD)|x|² from (13). The complete finite phase has

    Z_N=(1-b)Σ_(i=0)^(N-2)b^i A_i + b^(N-1) Z_tail,
    N_N=(1-b)Σ_(i=0)^(N-2)b^i Q_i + b^(N-1) N_tail,                   (B3)
    R_N=N_N/Z_N.                                                          (B4)

Empty sums are zero for N=1. Z_N>0 even for a singleton last core, since b>0 and a positive-area later shell occurs.

Every tuple is originally feasible, so R_N>=V. Conversely, by §§1–5, an optimal law has an optimal phase whose essential-support levels are canonical, satisfy (B1), and are exactly the displayed last-core tail from index N onward. Its first N profiles lie in P_N and its R_N equals V. Consequently

    V = min_(P_N) R_N.                                                    (B5)

This is an ATTAINED equality, not an assertion that P_N is compact or that any minimizer is unique. N is finite for every ε, but the remaining profiles are functions and may be nonparallel. Thus (B5) is not a scalar closed-form solution to the original problem.

### 7.4 Optional exact necessary self-consistency restrictions

Let λ=R_N for a candidate tuple and define C_N=C_(N-1)+D. By §4 the actual optimal tuple also obeys

    C_0⊆B̄(0,sqrt(λ)),
    C_i⊆(C_(i-1)+D)∪B̄(0,sqrt(λ))                    (1<=i<N),
    |[(C_(i+1)⊖D)∩B(0,sqrt(λ))]\C_i|=0              (0<=i<N).             (B6)

Therefore the same attained minimum (B5) holds if P_N is restricted by (B6) and R_N<=U: the true optimum remains in that subclass, and every candidate remains originally feasible. These are necessary conditions, not an assertion that solving them alone decides global optimality. They do not impose a common initial core on the prefix.

## 8. Why the local conditions do not finish the problem

This paragraph ALONE uses the separately parent-dispositioned f245 result named in §0. For b>=2/3, f245 gives V_b>1/2 and two full-D phases with initial C=[-1/2,1/2]^2: S_i=C+iD and a nonparallel K phase with J(P_K)<J(P_S). The S phase obeys all the local necessary conditions above, though it is not globally optimal: C lies inside B°; every later level is exactly forced; and `(S_(i+1)⊖D)=S_i` because S_i is closed convex. The latter follows from support functions: `x+D⊆S_i+D` implies `x·n<=h_(S_i)(n)` for every n, hence x∈S_i.

Thus even exact one-level complementarity plus an immediate common tail does not suffice for optimality. Theorems A–B do not import f245; this optional corollary only prevents reading (8) or (B6) as a sufficient optimizer test. The remaining finite global prefix/profile optimization is real.

## 9. Owner-run exact controls

The following single standalone Python eval cell was run in a fresh owner kernel and printed PASS A/B/C. It checks the symbolic geometric moments, the arbitrary-profile strip increment and the triangle moment used in (13). These finite identities are auxiliary arithmetic checks only; the all-law and optimizer arguments above remain WRITTEN and require disjoint review.

```python
from fractions import Fraction as F
from math import factorial

# Geometric factorial-moment identity E[(G)_k]=k! m^k and Stirling conversion.
S=[[0]*5 for _ in range(5)];S[0][0]=1
for n in range(1,5):
 for k in range(1,n+1):S[n][k]=S[n-1][k-1]+k*S[n-1][k]
Tk=[[F(S[n][k]*factorial(k)) for k in range(n+1)] for n in range(5)]
expected=[[1],[0,1],[0,1,2],[0,1,6,6],[0,1,14,36,24]]
assert Tk==[[F(c) for c in row] for row in expected]
print('PASS A: all geometric moments T0..T4 as exact polynomials in m')

# Exact polynomial identity for the old octant strip moment increment.
# Indeterminates (f,r,y); use sparse coefficient dictionaries.
def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,F(0))+v
 return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*F(c) for k,v in p.items() if v*c}
def mul(p,q):
 out={}
 for k,v in p.items():
  for j,w in q.items():
   a=tuple(k[i]+j[i] for i in range(3));out[a]=out.get(a,F(0))+v*w
 return {k:v for k,v in out.items() if v}
def pw(p,n):
 o={(0,0,0):F(1)}
 for _ in range(n):o=mul(o,p)
 return o
f={(1,0,0):F(1)};r={(0,1,0):F(1)};y={(0,0,1):F(1)}
lhs=add(scale(add(pw(add(f,r),3),scale(pw(f,3),-1)),F(1,3)),mul(pw(y,2),r))
rhs=add(mul(r,add(pw(f,2),pw(y,2))),mul(pw(r,2),f),scale(pw(r,3),F(1,3)))
assert lhs==rhs
print('PASS B: arbitrary-profile strip increment identity')

# Triangle moment int_0^r (t^2*s+t*s^2+s^3/3) ds.
# A monomial (t exponent, s exponent) integrates to (t exponent,r exponent).
integrand={(2,1):F(1),(1,2):F(1),(0,3):F(1,3)}
result={(a,k+1):c/F(k+1) for (a,k),c in integrand.items()}
assert result=={(2,2):F(1,2),(1,3):F(1,3),(0,4):F(1,12)}
print('PASS C: exact triangle contribution to parallel moments')
```

## 10. Review targets and assurance ceiling

Request complete disjoint review of: (i) every-shift weak closure, positive density representative and nonradial phase mixture; (ii) four separate Steiner equality cases and exact essential-support inclusions; (iii) one-level deletion/addition feasibility and the signed optimality contradiction, including Borel and zero-area boundary cases; (iv) the exact essential-support recurrences (8) and upgrade from a.e. to set equality; (v) the cost-ball/diamond cutoff and its equality case; (vi) (B1)–(B5), including N=1, t=0 and the normalization of the geometric tail; (vii) the self-consistent restriction (B6); and (viii) the exact boundary of the optional f245-dependent insufficiency paragraph.

This is WRITTEN same-harness author work, with separate finite exact arithmetic, not human/independent-model-family review, formal/kernel verification, novelty or parent adoption. It narrows the all-epsilon problem to a bounded number of nonparallel profile functions; it does not claim the unresolved prefix is solved or unique.
