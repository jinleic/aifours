# Beyond the V<1/2 shell argument: all-epsilon radial gap removal and an exact signed-shell obstruction

Owner: InfoResearch96h-2 / info-1. Actual native clock observed before writing: `Thu Oct 29 10:09:59 PDT 2026`.

**AUTHOR-WRITTEN / UNREVIEWED candidate.** The mathematical proofs are written below; an owner-run exact Fraction polynomial/identity check is supplied in §9. No parent adoption, formal/kernel proof, independent-model or human review, source-priority/novelty claim, or general nonradial solution is asserted.

## 0. Results and exact scope

Let F_b be the original all-Borel, every-full-closed-D-shift class, b=e^(-ε)∈(0,1), with D={||h||_1<=1}, J(μ)=E|X|_2^2, and V_b=inf_(μ∈F_b)J(μ). Three separate results are proved:

**A. Uniform fixed-core gap removal, EVERY ε>0.** Let 0<=R_0=g, R_(i+1)>=R_i+1 for every i, with `Σ_i b^i R_i^4<∞`. The full-D-private phase built from centered diamond levels K_i=R_iD is strictly worse in J than the MINIMAL-shell law with the SAME initial core gD unless R_i=g+i for every i. Equivalently, for every sequence with a gap,

    Σ_i b^i[Φ_(V_b)(R_iD)-Φ_(V_b)((g+i)D)]>0,                           (A)

although individual summands may be negative. If all gaps vanish the sum is zero. This is a genuine all-epsilon extension of the minimal-shell COMPARISON for the stated radial phase subclass, not a theorem for arbitrary nonradial cores/levels or arbitrary radial laws without an accompanying phase decomposition.

**B. Exact failure of the old term-by-term argument at the true V_b.** For EVERY b∈[1/2,1), a valid centered-diamond phase with K_0=(1/2)D and K_1=(8/5)D has

    Φ_(V_b)(K_1)-Φ_(V_b)(K_0+D)<=-12307/7500<0.                         (B)

It also satisfies K_(i+1)=K_i+D for all i>=1. Thus the old assertion that every excess-shell term is nonnegative is false on actual feasible D4-symmetric, four-direction-convex phases when V_b>1/2. At b=1/2, the COMPLETE weighted difference for this same sequence is nevertheless at least 2023/1250>0. This is an exact example of negative local contribution plus mandatory positive tail compensation. It does NOT refute minimal-shell structure of an actual optimizer; the displayed phase is in fact strictly improved by its minimal-shell comparator.

**C. A core-sensitive nonradial sufficient condition, and an explicit parameter extension.** If an optimal phase has compact initial core C containing 0 and exact levels K_i⊇C+iD, define `ρ(C)=inf{|x|_2:x∉C+D}`. Whenever `V_b<=ρ(C)^2`, its levels are necessarily C+iD a.e. In particular, if C contains the centered square [-t,t]^2, it suffices that

    V_b <= min{(1+t)^2,(1+2t)^2/2}.                                      (C)

This is a valid condition even for V_b>1/2, but this packet DOES NOT establish it for all optimal cores or any unconditional interval with V_b>1/2. Separately, an explicit feasible trial proves V_b<1/2 for every ε>=ln 15; the exact root criterion in §8 gives a slightly larger interval. This strengthens the elementary product-Laplace sufficient cutoff ε>2sqrt(2), but stays inside V_b<1/2.

**Remaining original-target gap.** Prove a weighted analogue of (A) for arbitrary D4/four-direction-convex NONRADIAL optimal phases, or otherwise control their signed excess shells when (C) is not known. No inference from the radial subcase, local negative term, or parameter bound settles this gap.

### Ancestry and noninputs

The immediately preceding self-contained ln64 geometry/scalar packet is `frontier-20261029-lawfree-lower-half-v1.md`, SHA-256 `ddd3fc87bd38475500589957e030119de451c6fa5f0b27ea54fb8e0856ea62ea`; its parent disposition `dispositions/info-1-ln64-all-law-unique-rounded-shell-optimum-parent-v1.md` supports the single instance only. Its §4.4 is the V<1/2 argument whose failure mode is investigated here. The f181 matching-norm disposition `dispositions/info-1-matching-norm-unique-optima-and-unconditional-LJ-gap-parent-v1.md` already supports the unique GLOBAL l1-radial J optimum and unit spacing for optimal radial phases; result A here is the different, fixed-initial-core comparison for EVERY finite-moment radial diamond phase, not a new global optimum or a claim that W=J in general. Neither disposition is used as a theorem premise below: all needed deductions are rederived.

Same continuing author and prior LAW642/bridge exposure are explicitly disclosed; no independent-authorship or clean-cognition claim is made. Historical held/withdrawn/ZERO bodies, their consumers/guides, MDA26 source text, and f161/f162/protected v214 bodies are NONINPUT and were not opened for this work. The earlier process findings and exclusions are not cured or retrospectively reclassified.

## 1. Phase laws, moments, and privacy

Let `R_i>=0` increase with R_(i+1)>=R_i+1. Put

    u_R(x)=(1-b) Σ_(i>=0)b^i 1_{R_iD}(x),   Z_R=∫u_R,   N_R=∫|x|^2u_R.

Up to null boundaries u_R=b^n, where n is the least index with x∈R_nD. Because R_iD+D⊆R_(i+1)D, `u_R(x+h)>=b u_R(x)` for every closed-D shift h, up to the null boundary convention; taking a Borel representative with the least-index definition gives this pointwise. The normalized law is in the FULL original F_b. Finiteness of `Σ b^iR_i^4` gives finite N_R and Z_R>0: R_1>=1 even if R_0=0.

Area and Euclidean moment of a radius-r diamond are

    |rD|=2r^2,       ∫_(rD)|x|_2^2 dx=(2/3)r^4,       J(Unif(rD))=r^2/3.    (1)

The last identity applies when r>0. Thus

    Z_R=2(1-b)Σ_i b^iR_i^2,
    N_R=(2/3)(1-b)Σ_i b^iR_i^4,
    J(R)=[Σ_i b^iR_i^4]/[3Σ_i b^iR_i^2].                                 (2)

Let G have `P(G=i)=(1-b)b^i`, m=b/(1-b), and M_j(r)=E(r+G)^j. The minimal-shell density u_r corresponds to R_i=r+i, with

    Z_r=2M2(r),    J_r=M4(r)/(3M2(r)),                                     (3)
    M2=r^2+2mr+m+2m^2,
    M4=r^4+4mr^3+6(m+2m^2)r^2
       +4(m+6m^2+6m^3)r+(m+14m^2+36m^3+24m^4).

The geometric moments follow by differentiating `(1-b)/(1-bs)` at s=1 and expanding powers into falling factorials. All expressions are finite.

## 2. A scalar fact on the whole range r>=1

For any fixed m>0 and r>=1, J_r is strictly increasing and Z_r is strictly increasing. Indeed Z_r'=4(r+m)>0. Write r=1+s, s>=0. Expansion of (3) gives

    M4'(r)M2(r)-M4(r)M2'(r)=2P(1+s,m),
    P(1+s,m)=(1+s)^5
      +m(4+21s+34s^2+22s^3+5s^4)
      +m^2(5+28s+36s^2+12s^3)
      +m^3(2+12s+12s^2).                                             (4)

Every coefficient on the right is nonnegative and the first term is strictly positive. Hence J_r'>0 for every r>=1. This uses no optimum or source theorem. The exact bivariate coefficient identity and positivity are additionally checked by the self-contained cell in §9.

For r>=1 and any a<r, `(r+G)^4>=r^2(r+G)^2` gives

    J_r>=r^2/3>a^2/3.                                                      (5)

## 3. Removing the last gap strictly improves J

Suppose the last positive gap is between levels k and k+1, of size δ>0: R_(k+1)=R_k+1+δ and R_(j+1)=R_j+1 for every j>=k+1. Let a=R_k and r=a+1>=1. Keep levels 0,...,k and lower every later radius by δ; the new sequence remains admissible.

For z>=r, the unnormalized density decomposes EXACTLY as

    u(z)=(1-b)Σ_(j=0)^k b^j1_{R_jD}+b^(k+1)u_z,                          (6)

where z=r+δ is the original tail and z=r is the gap-removed tail. The first term is the SAME prefix in both laws. Its mass α is nonnegative; if α>0 its normalized squared cost c satisfies c<=a^2/3 by (1), since all prefix radii are <=a. The tail mass β(z)=b^(k+1)Z_z and tail cost J_z both increase strictly with z>=r by §2; J_z>a^2/3>=c by (5).

If α>0, the full cost is

    (α c+β(z)J_z)/(α+β(z)).

It strictly increases both when J_z increases and when β increases, because J_z>c. If α=0 it is just J_z, also strictly increasing. Therefore removing the last gap strictly reduces J, without evaluating V_b and without assuming any sign on an individual shell. This remains true for k=0,g=0, where the prefix has zero area.

## 4. Any finite or infinite collection of radial gaps

For finitely many positive gaps, remove the last one, then the last remaining one, and so on. Each operation preserves all earlier levels and all shift constraints, and strictly reduces J by §3. The endpoint is the minimal-shell sequence g+i.

For infinitely many positive gaps, define the n-truncation by retaining R_i for i<=n and setting `R_i^(n)=R_n+i-n` for i>n. It has only finitely many gaps and `R_i^(n)<=R_i`. By (2) and dominated convergence for the summable series `Σ b^iR_i^2` and `Σ b^iR_i^4`, both Z and N of the truncation converge to those of R.

Let k be the first positive gap. For every n>=k+1, remove all later gaps in the n-truncation. The remaining fixed one-gap phase has initial g, its first gap δ_k>0 at k, and unit gaps elsewhere. Section 3 removes that gap and gives a fixed positive difference in J from the all-unit phase. Thus every truncation is at least that fixed one-gap cost; passing to the limit preserves a STRICT gap above J_g. This proves the first assertion of Theorem A for every b∈(0,1), g>=0, and finite-moment sequence.

For (A), write (PHASE) in the notation of §1:

    (1-b)Σ_i b^iΦ_λ(R_iD)=Z_R(J(R)-λ).

The original phase contains every minimal shell, so Z_R>=Z_g. If any gap exists, the comparison above gives J(R)>J_g, and the minimal shell is full-D private, so `J_g>=V_b`. Hence

    Z_R[J(R)-V_b] > Z_g[J_g-V_b]>=0.

Dividing by 1-b gives the strict AGGREGATE inequality (A). It is exactly this weighted whole-tail statement—not positivity level by level—that survives beyond the earlier cost-ball condition.

## 5. A self-contained all-law lower bound, used only for the obstruction

Fix any μ∈F_b and project onto either coordinate X. The marginal satisfies the same ε-DP inequality for every shift of magnitude <=1, by applying the planar inequality to inverse-image Borel sets. Integer shifts follow by iteration.

Set p(r)=P(|X|>=r). The interval A=(-1/2,1/2) and A±1 are pairwise disjoint, and the two shifted copies are outside A. Privacy implies

    p(1/2)>=2b[1-p(1/2)],  so p(1/2)>=2b/(1+2b).                     (7)

For every r>0, the two disjoint half-line inequalities give `p(r+1)>=b p(r)`. The layer-cake identity `E X^2=∫_0^∞2r p(r)dr`, bounded below on [0,1/2] and on [k-1/2,k+1/2], k>=1, yields

    E X^2 >= p(1/2)[1/4+2Σ_(k>=1)k b^k]
            >= [2b/(1+2b)] [1/4+2b/(1-b)^2].                             (8)

Sum this for both coordinates, with no independence assumption:

    V_b >= [4b/(1+2b)] [1/4+2b/(1-b)^2].                                 (9)

The right side is increasing on (0,1), so for every b>=1/2 it is at least 17/4. This bound is not claimed sharp.

## 6. Explicit negative first term, positive forced tail

Take `g=1/2`, `δ=1/10`, and define

    K_0=(1/2)D,     K_i=(i+3/5)D for i>=1,
    C_i=(i+1/2)D for i>=0.                                                (10)

All sets are compact, centered D4-symmetric diamonds with centered sections in all four directions. They obey K_0+D⊂K_1 and K_i+D=K_(i+1) for i>=1. Thus they are actual valid full-D phase levels, not a lattice relaxation.

By (1), the first level's excess signed integral is EXACTLY

    Φ_λ(K_1)-Φ_λ(C_1)
      =(2/3)[(8/5)^4-(3/2)^4]-2λ[(8/5)^2-(3/2)^2]
      =(31/50)(481/300-λ).                                                (11)

For b>=1/2, insert the actual all-law λ=V_b and (9), obtaining (B). In particular the extra annulus has negative aggregate signed contribution at the true infimum; the earlier per-level nonnegative comparison cannot be extended to this parameter region from its former hypotheses. The example does not assert that these K_i occur at the optimum.

At b=1/2 the full weighted excess is also EXACTLY

    ΔH_λ=Σ_(i>=1)2^(-i)[Φ_λ(K_i)-Φ_λ(C_i)]
         =50517/5000-(51/50)λ.                                            (12)

The actual minimal-shell law P_(1/2) is feasible, and (3) gives `V_(1/2)<=J_(1/2)=1697/204`. Therefore

    ΔH_(V_(1/2))>=2023/1250>0.                                            (13)

The first WEIGHTED summand is at most -12307/15000, so all subsequent weighted summands together contribute at least 36583/15000. These two signs are compatible: future forced dilations compensate more than the negative first shell. Formula (12) is obtained by subtracting the geometric sums of powers at g+δ and g, and subtracting the missing i=0 term; the exact rational check is in §9.

## 7. A conditional extension of the nonradial minimal-shell step

Consider an ACTUAL optimal phase with compact C=K_0, 0∈C, exact K_i⊇C+iD, and the finite-moment property. These hypotheses arise from the original all-shift phase/Steiner analysis, but no such earlier analysis is imported as a premise for the following conditional statement.

Let `ρ(C)=inf{|x|:x∉C+D}`. Since C+iD contains C+D for i>=1, whenever V_b<=ρ(C)^2, every excess point in K_i\(C+iD) has |x|^2>=V_b. Its equality subset is contained in a circle and hence is null. Comparing the signed sum with the feasible minimal-shell sequence gives

    0<=H_(V_b)((C+iD))<=H_(V_b)((K_i))=0,

so each excess set is null. Thus K_i=C+iD a.e. for all i, even if V_b>1/2. This is CONDITIONAL on the actual core's inradius; it does not establish that condition.

If C contains [-t,t]^2, the centered square plus D is contained in C+D. Its Euclidean inradius is

    r(t)=min{1+t,(1+2t)/sqrt(2)}.                                         (14)

To see this without assuming C convex, compute the support function of the convex square+D in a unit direction `(cos θ,sin θ)`, 0<=θ<=π/4: `(1+t)cos θ+t sin θ`. It is concave on that interval, so its minimum is at an endpoint, giving the two displayed values; D4 symmetry covers all directions. Hence ρ(C)>=r(t), giving condition (C). For t>0, r(t)^2>1/2, so there is a genuine geometric range above 1/2 in which this implication applies. The packet does not prove an actual optimal t/value pair lands in that range.

## 8. A nonvacuous explicit all-epsilon cutoff within V<1/2

For the actual feasible centered staircase P_(1/2), put m=b/(1-b). By (3), J_(1/2)<1/2 iff

    Δ(m)=24m^4+48m^3+26m^2+2m-5/16<0.                                   (15)

Δ is strictly increasing on m>=0, negative at m=0 and positive for large m. It has one positive root m_0. Exact substitution gives

    Δ(1/14)=-725/38416<0,    Δ(1/13)=8171/456976>0.

Hence for `ε>log((1+m_0)/m_0)` the original all-law V_b<=J_(1/2)<1/2; the threshold lies strictly between ln14 and ln15, so every ε>=ln15 is covered. At b=1/15 specifically, J_(1/2)=22501/46452=1/2-725/46452.

This extends the simple product-Laplace sufficient regime ε>2sqrt(2). The interval [ln15,2sqrt(2)] is nonempty: 14/5<2sqrt(2), and the positive exponential series through degree five gives `exp(14/5)>720653/46875>15`. The root in (15) is only a threshold for THIS trial, not the true boundary of V_b<1/2; failure of (15) makes no claim about the original optimum.

## 9. Exact finite control, with limits

The following complete cell was run in the owner's fresh Python eval kernel; it printed PASS A, PASS B and PASS C. It checks the ENTIRE bivariate coefficient identity (4), exact selected-instance values in (11)–(13), and the rational cutoff/certificates in §8. It does not verify the universal measure, optimization or infinite-gap proof; those are written arguments in §§1–8. Two earlier interactive attempts failed due to shadowed Python names and were retried after restoring the affected polynomial variables and functions; the final cell below is standalone and avoids those collisions.

```python
from fractions import Fraction as F

def add(*terms):
 out={}
 for p in terms:
  for k,v in p.items():out[k]=out.get(k,F(0))+v
 return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*F(c) for k,v in p.items() if v*c}
def mul(*factors):
 out={(0,0):F(1)}
 for p in factors:
  temp={}
  for (a,b),v in out.items():
   for (c,d),w in p.items():temp[(a+c,b+d)]=temp.get((a+c,b+d),F(0))+v*w
  out={k:v for k,v in temp.items() if v}
 return out
def power(p,n):return mul(*([p]*n)) if n else {(0,0):F(1)}
def derivative(p,axis):
 out={}
 for k,v in p.items():
  if k[axis]:
   t=list(k);t[axis]-=1;out[tuple(t)]=v*k[axis]
 return out
one={(0,0):F(1)};s={(1,0):F(1)};m={(0,1):F(1)};r=add(one,s)
T2=add(m,scale(power(m,2),2));T3=add(m,scale(power(m,2),6),scale(power(m,3),6));T4=add(m,scale(power(m,2),14),scale(power(m,3),36),scale(power(m,4),24))
M2=add(power(r,2),scale(mul(m,r),2),T2)
M4=add(power(r,4),scale(mul(m,power(r,3)),4),scale(mul(T2,power(r,2)),6),scale(mul(T3,r),4),T4)
Pshift=add(power(r,5),mul(m,add(scale(one,4),scale(s,21),scale(power(s,2),34),scale(power(s,3),22),scale(power(s,4),5))),mul(power(m,2),add(scale(one,5),scale(s,28),scale(power(s,2),36),scale(power(s,3),12))),mul(power(m,3),add(scale(one,2),scale(s,12),scale(power(s,2),12))))
assert add(mul(derivative(M4,0),M2),scale(mul(M4,derivative(M2,0)),-1))==scale(Pshift,2)
assert all(v>0 for v in Pshift.values())
print('PASS A: complete bivariate derivative identity and nonnegative-variable coefficients')

def M2q(x,mm):return x*x+2*mm*x+mm+2*mm*mm
def M4q(x,mm):
 t2=mm+2*mm*mm;t3=mm+6*mm*mm+6*mm**3;t4=mm+14*mm*mm+36*mm**3+24*mm**4
 return x**4+4*mm*x**3+6*t2*x*x+4*t3*x+t4
b=F(1,2);mm=b/(1-b);g=F(1,2);delta=F(1,10)
U=M4q(g,mm)/(3*M2q(g,mm)); assert U==F(1697,204)
L=F(2)*((2*b)/(1+2*b))*(F(1,4)+2*b/(1-b)**2);assert L==F(17,4)
old=g+1;new=old+delta
A1=F(2,3)*(new**4-old**4);B1=2*(new*new-old*old)
assert A1==F(14911,15000) and B1==F(31,50)
assert A1-B1*L==-F(12307,7500)
D2=(M2q(g+delta,mm)-M2q(g,mm))/(1-b)-((g+delta)**2-g*g)
D4=(M4q(g+delta,mm)-M4q(g,mm))/(1-b)-((g+delta)**4-g**4)
A=F(2,3)*D4;B=2*D2
assert A==F(50517,5000) and B==F(51,50)
assert A-B*U==F(2023,1250)
print('PASS B: U, lower bound, negative first excess and positive total compensation')

m15=F(1,14);trial=M4q(g,m15)/(3*M2q(g,m15))
assert trial==F(22501,46452) and F(1,2)-trial==F(725,46452)
from math import factorial
s5=sum(F(14,5)**k/factorial(k) for k in range(6))
assert s5==F(720653,46875) and s5>15 and F(14,5)**2<8
print('PASS C: ln(15) is below 2 sqrt(2), with exact V<1/2 trial')
```

## 10. Review priorities and boundaries

Request one full-scope disjoint review of: the monotonic scalar polynomial (4); the increasing-prefix/tail-mixture proof including zero-area prefix; truncation and the fixed-positive-gap limit for infinitely many gaps; conversion from strict J ordering plus Z ordering to (A); the one-dimensional two-sided tail bound; the signs and units in (11)–(13); and the conditional/nonconditional distinction in (C) and §8.

The signed first-shell counterexample is to the OLD PROOF STEP, not to an all-law optimizer, not a demonstration that every optimum contains a gap, and not a failure of theorem A. The nonradial general-epsilon gap remains OPEN at the exact residual in §0. Matching-norm prior ancestry, actual named checks, all historical findings and the unchanged deadline remain as stated.
