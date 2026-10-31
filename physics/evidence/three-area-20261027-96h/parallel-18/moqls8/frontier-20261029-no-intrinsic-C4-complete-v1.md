# No intrinsic four-dimensional component in any ordinary four-MOQLS(8)

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE — UNREVIEWED, NOT ADOPTED.** PhysicsMOQLS8-2. Actual preceding native clock: Thu Oct 29 10:35:31 PDT 2026. This is stronger than LOCAL4>=10: it excludes the ENTIRE intrinsic C4 component stratum, with arbitrary complex rays and no projector-span assumption. It uses a new three-space capacity consequence of the two-plane mass bound. No f192 or later review is silently enlarged, and no C5 file is changed.

## 1. Actual family, component and sole adopted import

Let Q,X1,X2,X3 be ANY four ordinary MOQLS of order 8. All actual rows and columns are ONBs in C^8, and all six actual same-cell tensor-product families are ONBs in C^8 tensor C^8. For distinct cells y,z and distinct members M,N,

    <M_y,M_z><N_y,N_z>=0.

Suppose C is an intrinsic irreducible component of Q with complex span W of dimension FOUR. Different intrinsic components are orthogonal. Projecting an actual Q-row or column resolution to W shows that it meets C in exactly four cells, an ONB of W. Thus C has 32 original cells and

    sum_{z in C} P_z=8P_W,       P_z=|Q_z><Q_z|.

The ONLY adopted theorem used is **GAP3**, every ray in a nontrivial intrinsic component of every member of a four-MOQLS(8) has GLOBAL multiplicity at most three. It is Gate 1 of the prior-round parent disposition `institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md`, SHA256 `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4`. Everything else is proved below. In particular no earlier C4 theorem, reality, tensor structure, catalogue, solver outcome, numerical witness or new unreviewed packet is a premise.

## 2. The exact three-mate identity gives a five-fold orthogonal-star frame

Fix an actual component cell y with ray u, and a mate X. Evaluate the X-factor in the complete Q-X tensor-ONB resolution along X_y. After removing z=y, all nonzero terms lie outside y's row and column and have Q_z perpendicular to u:

    sum_{z off y's row/column, Q_z perpendicular to u}
          |<X_y,X_z>|^2 P_z = I_8-P_u.

At each distinct z, the weights for two different mates cannot both be nonzero, by their pair-product orthogonality. Each weight is at most one. Sum the three identities and compress to W. The off-line unweighted star sum dominates 3(P_W-P_u). Adding back y's row and column stars, two DISJOINT actual three-ONBs each resolving P_W-P_u, proves

    A_u := sum_{z in C, Q_z perpendicular to u} P_z >=5(P_W-P_u).       (STAR)

Thus every actual u has at least FIFTEEN orthogonal-star CELLS, counting original occurrences. No multiplicity ceiling or reality was used to derive STAR.

## 3. Any complex two-plane contains at most three distinct actual component rays

Let B be ANY complex two-plane of W, not necessarily an actual span of entries. Its total projection mass is

    sum_{z in C} ||P_B Q_z||^2=16.                         (MASS-2)

For each actual ray v in B let v' be its unit in-plane perpendicular ray, possibly virtual. Evaluate STAR for v along v'. If Q_z is perpendicular to v, its nonzero B-projection is parallel to v' and its v'-weight is exactly its B-projection mass. Consequently

    sum_{z in C, nonzero P_B Q_z parallel to v'} ||P_B Q_z||^2>=5.       (FIVE)

Distinct actual v in B have distinct perpendicular projective directions v'; these positive-mass cell sets are disjoint. Four actual rays would therefore require at least twenty projection-mass units, contradicting MASS-2. Hence B has at most THREE distinct actual component rays.

There is a useful sharp boundary. If three actual B-rays had no orthopair, their own cells would lie outside all three target perpendicular directions, contributing at least three additional mass units beyond the required fifteen. This would exceed sixteen. Thus three actual B-rays contain an orthopair x,x'. Their third ray v is orthogonal to neither, so its occurrence cells lie outside all three target directions. FIVE gives

    15+m(v)<=16.

Because v is actual, **m(v)=1**. In particular an actual orthopair and a third different actual ray in their two-plane force the third ray to have global multiplicity one. This statement requires no actual status for any virtual perpendicular direction used in the proof.

## 4. Every actual C4 ray must have multiplicity one

Fix an actual u with m=m(u)<=3 by GAP3. Its m actual rows each contain three star-u cells. If every row WITHOUT u contained at most one star-u cell, the total star count would be at most

    3m+(8-m)=8+2m<=14,

contradicting the fifteen-cell lower bound from STAR.

Thus an actual row WITHOUT u contains at least two star-u rays v,w. It cannot contain three, as then its fourth ray would equal u. Its other two actual rays x,x' form an ONB of the two-plane B=span(v,w)-perp within W. Since u is perpendicular to v,w, it lies in B; since the row is u-free, u is distinct from x,x'. Section 3 makes u's multiplicity ONE.

This applies to EVERY actual ray of C. Thus all component cell rays are distinct; in particular the fifteen star cells at any actual u are FIFTEEN DISTINCT actual rays.

## 5. Any complex three-space contains at most seven distinct actual component rays

Let D be ANY complex three-space in W. Let v_1,...,v_N be ALL distinct actual component rays which lie in D. For each v_i compress STAR to D and take the trace. Since v_i is in D,

    sum_{z in C, Q_z perpendicular to v_i} ||P_D Q_z||^2 >=5(3-1)=10.

Sum this inequality over i. For a fixed component cell z with nonzero projection a_z=P_D Q_z, the rays v_i perpendicular to Q_z are exactly the actual rays among {v_i} lying in the complex two-plane D intersect a_z-perp. Section 3 bounds their number by THREE. Cells with a_z=0 contribute zero mass and need no such bound. Therefore

    10N
      <= sum_{z in C} ||P_D Q_z||^2
                        * #{i: v_i perpendicular to Q_z}
      <=3 sum_{z in C} ||P_D Q_z||^2
       =3*8*3=72.

Thus **N<=7**. This is a distinct-ray capacity bound for an arbitrary actual subspace D, not an assumption that D supports its own QLS or independent tensor bases. Multiplicities on cells z are retained in the mass sum; the distinct-ray count is only over the v_i.

## 6. Contradiction and full theorem

For ANY actual u in C, Section 4 gives fifteen DISTINCT actual star rays. They all lie in the complex three-space D=W intersect u-perp. Section 5 allows at most SEVEN actual rays in that space. Contradiction.

Therefore **no member of any ordinary four-MOQLS(8) has an intrinsic irreducible component of complex dimension FOUR**. There is no projector-span hypothesis, common-real restriction, fixed-ray assumption or classical mate assumption. The 32 original component cells, all three mates and the adopted GAP3 are used exactly as stated; three-MOQLS examples are not excluded by replacing four with three.

## 7. Exact original-target boundary and review requirement

This stronger C4 exclusion removes every b9 C4 case and every higher-span C4 case. It is a NEW WRITTEN AUTHOR candidate, requiring a NEW complete review and parent disposition; the earlier longer LOCAL4 proof and f192 sources stay immutable and are not silently relabelled.

The C5>=11 union remains byte-fixed as requested. Conditional on acceptance of this theorem, that whole C5 union, and the adopted C2/C3 exclusions plus C6/C7/C8 span/budget inputs, every nonclassical four-family member has projector span at least fourteen and the all-four-nonclassical q4 stratum is excluded by 56>53. This is not automatic adoption and does not settle q1/q2/q3, unrestricted four-family existence, numerical M(8) or maximum-three. A10 stays GB15/18 with P1-B2.M2, P1-B2.M4, P1-B3.M2 UNKNOWN; A11 stays OPEN.

Only exact WRITTEN derivations and source/clock metadata were used: no scientific interpreter, selected numeric probe, solver, heavy/multi-GB run, model CLI or nested agent. Full review must independently reconstruct STAR, disjoint perpendicular projection masses, the third-ray multiplicity argument, the original-row multiplicity-one bridge and the three-space capacity double count. No formal/kernel, human, configured-family, executable, priority, novelty or parent acceptance is claimed; all prior frozen records and process/cadence findings remain preserved.
