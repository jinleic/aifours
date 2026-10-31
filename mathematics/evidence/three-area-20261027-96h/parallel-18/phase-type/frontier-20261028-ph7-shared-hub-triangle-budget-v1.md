# Critical PH7: imbalanced triangles cannot form a disjoint-petal sunflower

**NEW ALL-TOPOLOGY WRITTEN APPLICATION; conditional on the separately frozen exact triangle-capacity theorem, not yet independently reviewed.** MathResearch96h-2. It is a structural restriction, not an unrestricted PH7 exclusion.

## Claim

At z=8/9, suppose an actual PH representation using at most seven states has all its imbalanced triangle vertex triples sharing one vertex h, and outside h those triples are pairwise disjoint. This is impossible. Balanced triangle triples, 2-cycles, 4-cycles, arbitrarily many longer cycles and arbitrary edge counts may be present.

In particular, if there are exactly two imbalanced triangle triples, they cannot share exactly one vertex: they must either be vertex-disjoint or share an entire edge. An 'imbalanced' triple means the two opposite orientation products differ; balanced triangles may have both orientations or neither.

The proof uses the separate `frontier-20261028-ph7-critical-triangle-imbalance-capacity-v1.md` SHA256 `c2c95deebfaa048072704da11126636d19b166c60a3cc7f41a266927716dc409`, whose exact six-rate copositivity and spectral application are under review. That theorem forces total imbalance W strictly ABOVE the top-three symmetric eigenrate product. We show that a disjoint-petal sunflower forces W AT MOST that product.

## 1. A sharper local triangle bound

Use positive Perron similarity to make the normalized seven-state G a row generator, and let `M=-S` be the positive semidefinite geometric-mean symmetrization of its off-diagonal entries, as in the cited capacity theorem.

For one triangle C containing h, label its vertices cyclically h,1,2. Let p_i be the forward row fractions and q_i the backward row fractions, indexed cyclically, and define

    s=p_h+q_h <=1,
    P=product_i p_i, Q=product_i q_i,
    R=sqrt(PQ),
    D=det(M_C)/(u_h u_1 u_2)
      =1-(p_h q_1+p_1 q_2+p_2 q_h)-2R,
    w_C/(u_h u_1 u_2)=P+Q-2R.

Every `p_i,q_i>=0` and `p_i+q_i<=1`. Direct expansion gives

    sD - w_C/(u_h u_1 u_2)
      = p_h[(1-p_1-q_1)+p_1(1-p_2-q_2)+(1-s)q_1]
        +q_h[(1-p_2-q_2)+q_2(1-p_1-q_1)+(1-s)p_2]
        +2(1-s)R >=0.                              (HUB)

All bracketed factors are nonnegative. Therefore

    w_C <= s det(M_C),
    s=(G_(h,1)+G_(h,2))/u_h.                        (LOCAL)

This is stronger than the individually known bound `w_C<=det(M_C)` and remains valid when either triangle orientation is missing.

## 2. Sum disjoint petals at the common vertex

For distinct imbalanced triples C in the hypothesis, their two non-h vertices are disjoint. Consequently the outgoing h-row entries counted in their s_C are disjoint, so

    sum_C s_C <=1.

Cauchy interlacing gives `det(M_C)<=lambda5 lambda6 lambda7` for every C, where lambda are the seven sorted nonnegative eigenvalues of M. Balanced triangles contribute exactly0 to W. Applying(LOCAL) and summing,

    W=sum_C w_C
      <= sum_C s_C det(M_C)
      <= lambda5 lambda6 lambda7 sum_C s_C
      <= lambda5 lambda6 lambda7.

This contradicts the strict opposite inequality from the cited critical capacity theorem. Hence no such PH7 representation exists. □

The shared-hub condition is essential to this proof: two vertex-disjoint imbalanced triangles can have total normalized imbalance greater than one top-three product, and triangles sharing an edge do not have disjoint hub-neighbor sets. No assertion about either case follows.

## Review boundary

Review must verify the exact(HUB) decomposition, the disjoint outgoing-row budget, interlacing, every prerequisite of the strict capacity theorem and the PH caller. No new numerical computation, 8/9 feasibility decision, PH order8, novelty, formal/kernel or cross-vendor review is claimed. Historic process findings remain and held material is not a premise.

END — imbalanced critical triangles cannot all share one vertex with disjoint remaining petals.
