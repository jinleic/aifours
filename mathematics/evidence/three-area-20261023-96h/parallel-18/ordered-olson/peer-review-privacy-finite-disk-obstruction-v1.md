# Bounded reconstruction — every finite-b positive-radius disk core is improvable

Observed before exclusive creation: **2026-10-23T15:56:29-0700 PDT**. Reviewer MathOlson-2, primary math-2. Read full `peer-review-wave-eighteen-v7.json`, including the common contract and my entry. Only this named exclusive reviewer-root output is written; no author/shared mutation, scientific program, arithmetic code, CAS, solver, enumeration, compiler, test, CLI or nested agent.

## 1. Exact operative packet, exposure and verdict

Read the complete376-line source, including full raw LF208:

    information-science/evidence/three-area-20261023-96h/parallel-18/
      privacy-diamond-mse/proof-no-finite-disk-core-optimum-v1.md

**Independently observed source SHA256:**

    44b68f86550f36cc560d31683f887b188a3310c63f175ebfb0abaf7fb868c7b4

It matches the assigned pin. The actual immutable notation repair was also read completely and its hash observed:

    proof-no-finite-disk-core-optimum-ADDENDUM-1-notation.md
    e013b011ebaaaddb365e7458a019a8037423b55caa5f0fcf3739b0bb77e6a2e4

This repair is REQUIRED: the raw source defines u_1=a/4 but later writes nu_1. The operative interpretation is EVERY nu_1=u_1=a/4, with nu_2=3a/4 unchanged. The parent's reported MINOR is therefore REPAIRED for the two-file packet, not a clean pass of the literal uncorrected original.

Read the complete56-line `selection-v2-finite-epsilon.md`. Read the actual known-mechanism `source-history-ADDENDUM-1.md` completely, observed SHA `06dd8df55880b9fcef632370089dfd72428d1b45f991c3407849814248a5ae57`; the mandatory SCDF2013 containment addendum was already read completely during the preceding assigned review. The mechanism is prior, including the authenticated2011-labeled presentation history. These source qualifications supply no new mathematical verdict or priority clearance.

**Prior exposure disclosed:** I previously reviewed the octagonal comparison and the all-law leading asymptotic, and have read the actual full-diamond privacy/family definitions. NO verdict from either review is inherited here. The C2 geometry, every-k Minkowski profile and complete cost-change expansion were independently reconstructed below.

**Verdict at the operative two-file scope: 0 FATAL / 0 MAJOR / 0 unresolved MINOR. No substantive defect found.** One pre-existing literal MINOR naming defect is disposed by the observed repair. The checked theorem is for EVERY0<b<1 and EVERYr>0, not only an asymptotic regime. It excludes positive-radius disk-core laws as exact finite-b minimizers but proves neither the finite V value nor a positive gap from an unattained infimum over disk radii. Parent acceptance, novelty and human/formal verification remain separate.

## 2. Actual perturbation and the explicit bounds

Use a=r/sqrt2, w=a/16, nu_1=a/4 and nu_2=3a/4. The two bump supports are exactly[3a/16,5a/16] and[11a/16,13a/16], disjoint and strictly inside(0,a). On its support,

    phi(s)=(1-(s/w)²)³,
    phi''(s)=w^(-2)[-6+36(s/w)²-30(s/w)⁴].

Its value and first two derivatives vanish at both endpoints, so zero extension is genuinely C2. The coefficient-sum bound is |phi''|<=72/w², hence |psi''|<=144/w². Disjoint support could improve this bound, but the crude bound is valid.

The amplitude

    tau=min{r/2^18, 3mr/[128(m+r)]}, m=b/(1-b)

is explicit and strictly positive for EVERY stated b,r. No undocumented sufficiently-small choice is required. Since w²=r²/512,

    tau||psi''||<=144*512/(2^18 r)=9/(32r).

The disk boundary F(y)=sqrt(r²-y²) satisfies F''=-r²/(r²-y²)^(3/2)<=-1/r on[0,a], so F_tau''<=-23/(32r)<0 exactly as stated.

The supports stay away from both endpoints. Thus F_tau(0)=r,F_tau'(0)=0,F_tau(a)=a,F_tau'(a)=-1. Strict concavity then makes F_tau strictly decreasing with derivative between-1 and0; its endpoint tangent at a gives F_tau(y)<=2a-y, and monotonicity gives F_tau(y)>=a. These consequences establish positivity/geometric containment directly; no separate unproved perturbation-sign or slope bound is needed.

The translated bumps have equal integrals, so integral psi=0. Because their supports are disjoint and their signed magnitudes are identical translates, integral psi³ is ALSO exactly0. This is cancellation of the complete cubic term, not a small-parameter or odd-symmetry guess.

## 3. Convexity, inverse gluing and the eight-octant core

F_tau is a continuous strictly decreasing bijection[0,a]→[a,r]. Its inverse has

    (F_tau^(-1))''=-F_tau''/(F_tau')³<0

on the open inverse branch, since the numerator after the minus sign is positive and the denominator negative. This sign is correct. The inverse derivative at y=a is1/(-1)=-1, matching the direct branch's derivative. At y=r the inverse slope may be unbounded; only continuous endpoint values and concavity are needed there, not a false C2 endpoint inverse.

Therefore the piecewise q is concave and decreasing on[0,r], continuous at its endpoints and glued with matching slope at a. Its even extension q(|y|) is concave on[-r,r]: the triangle inequality and q's monotonicity give q(|theta y+(1-theta)z|)>=q(theta|y|+(1-theta)|z|), and concavity gives the remaining inequality. The matching derivative0 at the origin is also consistent.

The set |x|<=q(|y|), |y|<=r is convex as the intersection of hypographs x<=q(|y|), -x<=q(|y|) and the strip. It equals the eight-octant union: below y=a, the unswapped cap covers y<=x<=F_tau(y) while the swapped pieces fill0<=x<=y; above a only the inverse piece contributes0<=x<=F_tau^(-1)(y). Thus no signed union leaves an unfilled region or a nonconvex seam.

The inequalities a<=F_tau<=2a-y imply it contains[-a,a]², hence0 in its interior, has coordinate extrema r and l1 support exactly2a=sqrt2 r attained at(a,a). Its exact area is8 integral_0^a(F_tau-y)dy. Integral psi=0 makes this pi r², equal to the disk area for the WHOLE positive amplitude, not just to first order. This does not assume that every unrestricted optimizer is symmetric or convex; it constructs one actual competitor.

## 4. Every-k Minkowski support profile — including all possible facet regimes

On the curved first-octant boundary x=F_tau(y), the outward normal is proportional to(1,-F_tau'(y)), ranging continuously from(1,0) to(1,1). For a normal with first coordinate strictly larger than the second, the unique maximizer of the sensitivity diamond D is(1,0). Support maximizers add under Minkowski summation. Thus that entire curved arc is translated by(k,0), preserving its y parameter, giving x=k+F_tau(y) for0<=y<=a.

At the diagonal normal, the core's maximizer is the unique(a,a), while kD contributes its entire edge between(k,0) and(0,k). Their sum is the segment from(a+k,a) to(a,a+k). Its first-octant half has x+y=k+2a and a<=y<=a+k/2. Other octants follow by the actual core/diamond symmetries.

These normal ranges exhaust every first-octant supporting direction. Strict core concavity prevents an unlisted core facet, the axis direction gives the proper endpoint, and the diagonal direction gives precisely the displayed face. The resulting convex body is filled by the origin-side regions. Hence the exact source profile(16) holds for EVERY k>=0, including all integer shells, with no k-versus-r clipping transition or additional large-k facet. At k0 the diagonal piece has zero area and the first cap is exactly the core.

Integrating gives

    |A_k^tau|=8ka+|S_tau|
       +8 integral_0^(k/2)(k-2v)dv
       =pi r²+8ak+2k².

The second integral is k²/4 BEFORE multiplication by8, which checks the2k² coefficient. Since8a=4sqrt2 r, this is exactly the disk parallel-body area for every k and the entire amplitude. Equal area and diagonal support here were combined with a complete support-function proof; neither was assumed by itself sufficient for arbitrary cores.

## 5. Full continuous-shift privacy, exact equal Z and all tails

The core is compact, contains0 and has positive area. Its A_k are nested, compact and exhaustive; the closed-set integer index is finite and Borel. For EVERYh∈D and EVERYx, A_k+h⊂A_(k+1). Applying the same inclusion with-h gives |n(x+h)-n(x)|<=1 pointwise, including shell corners and closed boundaries. Thus the normalized density satisfies the required ratio bound and, by integration/translation, the measure inequality for EVERY Borel E and continuous diamond shift h.

The layer identity

    b^n=(1-b)sum_(k>=0)b^k 1_(A_k)

is exact. Tonelli on nonnegative terms and the all-k area formula give for BOTH laws the same EXACT normalizer

    Z=pi r²+8am+2T2
      =pi r²+4sqrt2 rm+2b(1+b)/(1-b)²>0.

No missing factor(1-b), sampled normalization or omitted higher shell is involved. The competitor lies in2aD, so A_k^tau⊂(k+2a)D and its moment is at most(2/3)(k+2a)⁴. Polynomial geometric moments are finite for every0<b<1. Hence both moment sums are finite. In particular later subtraction/summation of their differences is justified by ordinary integrable linearity; the argument is not applying Tonelli to an uncontrolled signed series.

For large r, the source's prior core-inside-sensitivity condition may not hold; the preceding independent privacy argument still does. The theorem does not improperly extend an old optimality statement to that regime.

## 6. FULL moment-change polynomial and exact cubic cancellation

Only the curved cap changes; its lower boundary x=y and the diagonal region are fixed. Integrating x²+y² in x first gives the EXACT difference

    DeltaM_k=8 integral_0^a[
       ((k+F+tau psi)³-(k+F)³)/3+y² tau psi]dy.

It remains valid where psi is negative because it subtracts two actual cap integrals, not a positive-density ansatz. Full expansion yields

    8tau integral[(k+F)²+y²]psi
      +8tau² integral(k+F)psi²
      +(8/3)tau³ integral psi³.

Use F²+y²=r² and integral psi=0. The k² and r² linear pieces vanish, leaving16kA tau where A=integral F psi. The cubic term vanishes EXACTLY by the disjoint equal-bump identity, not by an inequality. Thus

    DeltaM_k=16kA tau+8tau²(kP2+B0),

where P2=integral psi² and B0=integral F psi². No fourth-order term can occur because the original moving-upper-bound integral is cubic. At k0 the linear term is0 and the positive quadratic core cost is retained, agreeing with the disk's area-constrained moment minimality.

Taking the FULL geometric expectation gives

    N_tau-N_0=16mA tau+8B tau²,
    B=mP2+B0>0.

All k dependence has degree1 here, and the finite tails were already justified. The normalizer remains exactly the same Z, so this unnormalized difference has the correct sign for the normalized MSE as well.

## 7. Every numerical coefficient in the strict margin

The two centers obey nu_1+s<=5a/16 and nu_2+s>=11a/16 for-supp<=s<=supp. Since F decreases,

    F(nu_1+s)-F(nu_2+s)
      >=[(11a/16)²-(5a/16)²]/(2r)
      =3r/32.

This follows from the exact square-root difference formula; its denominator is at most2r. The bounds need not be simultaneously tight for the common s to be valid lower bounds.

The bump integral is

    integral_-w^w phi(s)ds
      =2w[1-1+3/5-1/7]=32w/35.

Thus A<0 and |A|>=3rw/35. Also0<=phi<=1, so disjoint supports give psi²<=phi_1+phi_2, hence P2<=64w/35. Since F<=r,

    B<=64(m+r)w/35.

The SECOND amplitude bound supplies

    Btau<= [64(m+r)w/35]*[3mr/(128(m+r))]
          =3mrw/70<=m|A|/2.

Therefore

    N_tau-N_0=-16m|A|tau+8Btau²
             <=-12m|A|tau
             <=-36mrw tau/35<0.

Division by the identical positive Z proves the stated quantitative decrease(4). Every factor is positive for every fixed0<b<1,r>0, and the first amplitude bound independently guarantees the geometry. The two bounds are used for distinct purposes; neither is an unspecified perturbative remainder control. No asymptotic approximation or finite sample is part of this proof.

## 8. Exact consequence and limits

For EVERY positive radius r at EVERY finite epsilon>0, the constructed law is feasible and strictly improves that disk-core law. Hence no such disk law can be a global finite-b minimizer. This is stronger than a first-variation sign: it defines an actual convex competitor with an explicit amplitude and a full finite positive cost margin.

It does NOT establish V_b, an all-law reduction to a single convex core, the optimal noncircular shape, or existence of a finite-b minimizer. Pointwise strict improvement for each r does NOT on its own establish a positive gap between V_b and inf_r J_disk(r) if that infimum is unattained. The source correctly retains that distinction and excludes r0. No assertion at b0 or b1 is licensed by this theorem; the claim is exactly0<b<1 andr>0.

For r<=1/sqrt2, the core is coordinate-downward because q is decreasing: shrinking either absolute coordinate preserves |x|<=q(|y|). Its l1 support is sqrt2 r<=1, so it lies in D and fits the prior arbitrary-core construction interface. For larger r feasibility comes from the independent level-index proof, not a new-mechanism claim. The actual prior-mechanism/source-history addenda remain operative; this review supplies no novelty clearance or proof that the deformation comparison has no prior occurrence.

## Findings/disposition

- FATAL: none at the stated operative scope.
- MAJOR: none at the stated operative scope.
- Unresolved MINOR: none after the actual e013b011 notation repair.
- Historical parent MINOR: u_1/nu_1 is genuinely undefined in the original alone; the immutable alias addendum repairs it and MUST accompany that source.
- Verification: complete supplied-proof written reconstruction only, with the explicit prior-review exposure disclosed; not an inherited octagon/all-law verdict, execution, kernel, human or publication acceptance.

The bounded assignment is complete. I return to the ONE ordered-Olson primary and its current new consolidated-caller review boundary.
