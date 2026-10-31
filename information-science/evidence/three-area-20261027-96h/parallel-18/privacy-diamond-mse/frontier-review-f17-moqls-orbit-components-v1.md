# f17 independent written review — classical orbit components and full-Gram residual

**VERDICT: 0 FATAL / 0 MAJOR / 0 MINOR at the exact declared scope, conditional on the named f2 neighborhood theorem.** I reconstructed that theorem in my immediately preceding complete f2 review and re-use its exact demonstrated scope; the present topology, separation and quantitative residual arguments are independently reconstructed below. This is same-harness written review plus one small exact rational diagnostic, not formal/kernel/human/configured-family review, global order-8 existence/nonexistence, or novelty clearance.

Reviewer InfoResearch96h-2. Actual native pre-write observation `Wed Oct 28 17:16:05 PDT 2026`.

## Inputs, quantifiers and dependency

I first read the complete frozen `review-waves/f17-moqls-orbit-components/assignment-v1.json`, then the entire assigned 101-LF candidate through its true ending:

`physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261028-orbit-components-and-residual-v1.md`, live SHA-256 `98d5f79b6ccd25e1442c7a1abaddd481819b88e481a4ba7600b480982e218675`, **101 LF / 9355 bytes**. Candidate source coordinates below refer to this file.

The load-bearing f2 candidate `frontier-20261028-uniform-classical-neighborhood-v1.md`, SHA-256 `12d8a6e3e3c27ff0e5c776a196578a94ed1010f907986680ef74c0e7f42eb8aa`, **141 LF / 14567 bytes**, was read completely and its live pin measured for my immediately preceding f2 review. My return `frontier-review-f2-moqls-neighborhood-v1.md`, SHA-256 `dd325e80dfaf34dcefc5e3ac58b94655f13b85b30a9edf24b5704bba2f122238`, reconstructed all graph/phase/nonlinear estimates and gave 0F/0M/0m at the stated scope. This f17 result remains explicitly conditional on that f2 proof and does not promote its review into formal or parent acceptance.

Fix integers n>=2 and m>=1 with `2(m+1)>n`. X contains ALL labelled ACTUAL complex m-MOQLS(n) families as tuples of rays, with the stated maximum projective distance. Any classical C is an actual family; its member-specific global output-unitary orbit O(C) includes per-cell phases automatically because X is projective. If no such C exists the orbit statement is vacuous; any actual classical reference necessarily has m+1<=n by the f2 simple matching graph. No common output basis or shared unitary between members is assumed.

I am the same-harness prior f2 reviewer and am not blind to this dependency or the topic. I am not the physics-4 author; earlier administrative/source contact and lifetime exposure uncertainty are not a clean-cognition or independent-vendor certificate. No held historical result is a mathematical premise. The author's diagnostic source/receipt and its output are read as claims in the candidate, not used as my independent check; no author contact occurred.

## 1. Projective topology and the classical orbit is a component

Candidate lines 5–37. For unit representatives `v,w`,

    ||vv* - ww*||_F^2 = 2 - 2|<v,w>|^2.

Therefore `sqrt(1-|<v,w>|^2)=||vv*-ww*||_F/sqrt(2)` is a metric on rays. The maximum over finitely many labelled members/cells is a metric, and X has its relative topology in the finite product of projective spaces. No manifold or local parametrization of X is needed.

**Closed:** `U(n)^m` is compact; the map sending an m-tuple of memberwise unitaries to the corresponding tuple of projective reference rays is continuous. O(C) is therefore compact, hence closed in the Hausdorff ambient product and in X.

**Open:** Take any C' in O(C). It is an ACTUAL classical family with the same labelled occurrence pattern, so the EXACT f2 theorem applies at C': every Q in X at max distance at most `eta_n=1/[8n(n+1)]` is in its orbit. Since O(C')=O(C), the relative OPEN ball of radius eta_n around C' is contained in O(C). This covers every C' and proves relative openness. The closed endpoint of f2 is stronger than needed for openness; no assertion about arbitrary non-MOQLS perturbations follows from it.

**Path connected:** for every unitary U, diagonalize `U=V diag(e^{i theta_j}) V*` and use `U(t)=V diag(e^{it theta_j}) V*`. Applying these paths independently in each member yields a path in U(n)^m from the identity to any tuple. Its continuous orbit image connects C to any point of O(C), while preserving every row/column and tensor-product ONB. So O(C) is connected.

Any connected subset of X containing C is contained in the clopen O(C), since intersection with O(C) and its complement would otherwise split it into two nonempty relatively open sets. Because O(C) itself is connected, it is exactly C's connected component. Any path from C to a nonclassical actual family would be connected and contradict this conclusion. This says nothing about whether any nonclassical component exists, whether X is connected as a whole, or how many classical patterns exist.

## 2. Distinct occurrence-pattern separation

Candidate lines 39–48. In each classical member, equal-ray occurrence classes are exactly the cells carrying the same one of n pairwise orthogonal basis rays. If two labelled classical tuples have the same occurrence equivalence relation in every member, map each member's n basis rays to the corresponding n rays of the other tuple by a member-specific unitary. Thus they are in the same output-unitary orbit; converse invariance is immediate. Per-cell phase choices do not change the partitions.

If two classical tuples have different orbits, then for at least one member their two occurrence equivalence relations differ. Consequently there are cells x,y that coincide as a ray v in one tuple while being distinct, hence orthogonal, reference rays u,w in the other; if necessary interchange the tuples. Bessel gives

    |<v,u>|^2+|<v,w>|^2 <= ||v||^2=1.

At least one squared overlap is <=1/2, so the associated cell's projective distance is >=1/sqrt(2), and so is the maximum distance between tuples. This is an all-pairs lower bound, not a claim that two available classical Latin patterns achieve equality. Independently relabeling one member's grid is not silently part of the orbit; simultaneous grid relabeling of BOTH tuples simply changes their common labels.

For comparison, a rational rank-one-projector check in §5 attains equality in the TWO-RAY Bessel inequality. It is not claimed to realize two distinct complete classical MOQLS orbits.

## 3. Actual full-Gram residual and anchored leakage

Candidate lines 50–78. The arrays in this section need only consist of unit vectors. Every first row is ASSUMED already exactly equal, after valid member-specific unitary/phase choices, to its classical reference first row. This is a genuine hypothesis: arbitrary noisy first rows need not be unitarily alignable. The remaining vectors are rephased so their reference coefficient is positive; this is possible because their maximum complementary leakage delta satisfies `delta<=1/(4n)<1`.

The residual r is the maximum absolute selected-member inner product over every distinct same-row or same-column pair; s is the maximum absolute product of same-cell cross-member overlaps for EVERY distinct cell pair and EVERY pair of distinct members, with s=0 when m=1. R=max(r,s). With unit diagonals, R=0 is equivalent to all row/column ONBs and all n^2 pair-product vectors being an ONB: finite unit orthogonal sets of full dimension are bases. No subset/sampling interpretation is substituted.

For a graph edge in the exact f2 reference incidence graph, if it is a row/column edge the selected overlap has modulus <=r. If it is an edge from equality of a companion symbol, the two companion vectors have complementary norms <=delta to the SAME reference ray. Their intended coefficients have product >=1−delta^2 and their complementary inner product has modulus <=delta^2, so that companion overlap has modulus >=`1−2delta^2>0`. Its product with the selected overlap is bounded by s; hence the selected overlap is <=`s/(1−2delta^2)`. All graph edges therefore satisfy the single error bound

    e=max(r, s/(1−2delta^2)).

Expanding the actual selected overlap exactly as in f2 gives an edge potential difference bounded by

    e + delta^2 + 2delta^3 = e + delta^2(1+2delta).

The two relevant first-row potentials are exactly zero, and each occurrence is at same-side distance at most two from its own anchor. Thus every off-reference coefficient is bounded by twice that edge error, and taking the norm of at most n−1 such coordinates yields

    delta <= 2sqrt(n−1) [ e + delta^2(1+2delta) ].                         (B)

This is a statement about the ACTUAL maximum leakage, not merely the declared admissible upper bound. It includes n=2 and the m=1 no-companion case. For delta=0 the following inequalities are trivial; no division by delta is needed.

For n>=2 and `delta<=1/(4n)`,

    e >= delta/(2sqrt(n−1)) - delta^2(1+2delta)
      >= delta/(2n) - delta/(4n)(1+1/(2n))
      = delta[1/(4n)-1/(8n^2)]
      >= 3delta/(16n).

The denominator d=`1−2delta^2` lies in [1/2,1]. Since r<=R and s<=R, `e<=R/d`; hence

    R >= d e >= 3delta/(32n).                                             (C)

For n=8 the bound is `R>=3delta/256`; at R=0 it forces delta=0 in this anchored neighborhood. A finite nonzero residual, however small, is not an exact MOQLS witness. Neither (B) nor (C) makes a claim outside the stipulated anchored delta range or certifies that a numerical solver found all components.

## 4. Source-dependent and open claims

The clopen/open argument and (B)'s graph-distance step depend on f2's `2(m+1)>n` reference graph theorem, not merely on a finite GF8 incidence or a tangent rank. The Bessel lower bound itself holds for any two different actual classical occurrence-pattern orbits, without the >n/2 condition. Candidate (C) is an inequality for arbitrary unit arrays under its exact alignment and leakage hypotheses; it does not require the array to be an actual family.

The logical order is unbroken: f2 local actual-family rigidity -> relative openness -> clopen connected orbit -> component; separately finite-Gram residual -> bounded edge potentials -> (B) -> (C). There is no inference from component isolation to absence of other components. Unrestricted 4-MOQL(8) existence/nonexistence, M(8), any QOA equivalence, priority, novelty and strong assurance remain unestablished. No historical quarantined outcome is rehabilitated.

## 5. Independent bounded exact diagnostics

I executed this independent local Eval cell in Python using integer/`fractions.Fraction` operations only. It does NOT use the author's GF8 tables, code or output. The first check is an anchored order-2, one-member unit array with a deliberately nonzero Gram residual; the second checks equality in Bessel for individual rank-one projectors, not equality of two full MOQLS orbits.

```python
from fractions import Fraction as F
# Orthogonal 2x2 classical reference; perturb exactly one non-anchor vector.
a,d=F(544,545),F(33,545)
assert a*a+d*d==1
basis=((F(1),F(0)),(F(0),F(1)))
Q=((basis[0],basis[1]),((d,a),basis[0]))
def dot(x,y): return sum((u*v for u,v in zip(x,y)),F(0))
r=max(abs(dot(Q[i][j],Q[i][1-j])) for i in range(2) for j in range(2))
r=max(r,max(abs(dot(Q[i][j],Q[1-i][j])) for i in range(2) for j in range(2)))
delta=d; n=2; s=F(0); e=r
B_rhs=2*(e+delta*delta*(1+2*delta))
C_rhs=F(3)*delta/(32*n)
print('unit_vector_norm_squared=',a*a+d*d,'anchor_first_row=',Q[0]==basis)
print('delta=',delta,'admissible_delta_le_1_over_8=',delta<=F(1,8))
print('r=',r,'s=',s,'R=',r,'bound_3delta_over_32n=',C_rhs)
print('B_inequality:',delta<=B_rhs,'C_inequality:',r>=C_rhs)
Pv=((F(1),F(0)),(F(0),F(0)))
Pu=((F(1,2),F(1,2)),(F(1,2),F(1,2)))
Pw=((F(1,2),-F(1,2)),(-F(1,2),F(1,2)))
def trace_product(A,B):
 return sum((A[i][j]*B[j][i] for i in range(2) for j in range(2)),F(0))
print('Bessel_projector_overlaps=',trace_product(Pv,Pu),trace_product(Pv,Pw),
      'sum=',trace_product(Pv,Pu)+trace_product(Pv,Pw))
```

Actual output:

```text
unit_vector_norm_squared= 1 anchor_first_row= True
delta= 33/545 admissible_delta_le_1_over_8= True
r= 33/545 s= 0 R= 33/545 bound_3delta_over_32n= 99/34880
B_inequality: True C_inequality: True
Bessel_projector_overlaps= 1/2 1/2 sum= 1
```

The unit array has NONZERO residual and is not a witness. This check exercises m=1 and the boundary Bessel arithmetic, not arbitrary n, any nonclassical component, the complete f2 theorem or the author's separate selected-input receipt.

## 6. Verdict and disclosure

No FATAL/MAJOR/MINOR at exact candidate scope after the above reconstruction. Standard imports: finite-dimensional spectral theorem, compactness of U(n)^m and projective spaces, elementary topology of connected/clopen sets, Bessel/Cauchy–Schwarz and f2's stated local graph theorem. F2 is a same-harness written dependency, not a formal proof. No external model/source, author contact, nested agent, deletion, Git or infrastructure mutation occurred. Parent must independently read the complete candidate and return before any disposition.
