# Critical PH7: a linear family of imbalanced triangles must contain two vertex-disjoint triples

**NEW ALL-TOPOLOGY WRITTEN CANDIDATE, conditional on the exact critical triangle-capacity theorem; independent peer review pending.** MathResearch96h-2. A triangle-triple family is called *linear* here if any two of its unordered triples share at most one vertex. This result goes beyond the previous shared-hub and exactly-two-triangle cases.

## Claim

For a critical z=8/9 PH representation using at most seven states, suppose the family of all **imbalanced** triangle vertex triples is linear. Then it contains at least two vertex-disjoint triples.

More generally, for any irreducible seven-state row generator G and any linear family F of triangle triples, let nu(F) be the maximum number of pairwise vertex-disjoint triples in F. With M=-S the geometric-mean symmetric comparison and `lambda5 lambda6 lambda7` the product of its three largest eigenvalues,

    sum_(C in F) w_C <= nu(F) lambda5 lambda6 lambda7,     (PACK)
    w_C=(sqrt(A_C)-sqrt(B_C))².

The general bound(PACK) has no z or target-spectrum hypothesis. At the critical target, the separately frozen `frontier-20261028-ph7-critical-triangle-imbalance-capacity-v1.md` SHA256 `c2c95deebfaa048072704da11126636d19b166c60a3cc7f41a266927716dc409` requires the total imbalance of ALL triples to be STRICTLY GREATER than one top-three product. If the imbalanced family is linear, (PACK) forces `nu>=2`. All balanced triples contribute0.

This is conditional on review of the exact capacity theorem. It does NOT assert every critical graph has a linear imbalanced-triangle family or decide PH7 at8/9.

## 1. A multiplicative local triangle budget

For a given triple C, after row normalization let `p_i` and `q_i` be the two row fractions from vertex i to its two C-neighbors in the forward/backward cyclic orientation. Put

    s_i=p_i+q_i<=1,    P=product_i p_i,    Q=product_i q_i,
    D=det(M_C)/product_i u_i
      =1-sum_i p_i q_(i+1)-2 sqrt(PQ),
    w_C/product_i u_i=(sqrt(P)-sqrt(Q))².

If any s_i=0, w_C=0 and the desired inequality is immediate. Otherwise write `p_i=s_i a_i`, `q_i=s_i(1-a_i)`, and `S0=s1s2s3`. Since all s_i<=1,

    D >= 1-sum_i a_i(1-a_(i+1))
           -2 sqrt[product_i a_i product_i(1-a_i)].

The exact cyclic identity

    1-sum_i a_i(1-a_(i+1))
       =product_i a_i + product_i(1-a_i)

turns the right-hand side into a square. Meanwhile

    w_C/product_i u_i
       =S0 [sqrt(product_i a_i)-sqrt(product_i(1-a_i))]².

The proper principal M_C is positive definite, so D>0. Thus the exact rate-independent local bound is

    w_C/det(M_C) <= product_(i in C) s_i.             (LOCAL-PRODUCT)

It includes either orientation missing, reversible triangles, and arbitrary other outgoing edges.

## 2. Independent triangle labels and a packing bound

For each vertex i and each triple C in F containing i, let

    s_(i,C)=sum_(j in C\{i}) G_ij/u_i.

Because F is linear, the two-neighbor sets associated with distinct triples incident to i are disjoint. Therefore `sum_(C containing i) s_(i,C)<=1`.

Independently at each vertex, randomly select an incident triangle label C with probability `s_(i,C)`, and select a null label with the remaining probability. For each C, the event that ALL THREE of its vertices selected C has probability `product_(i in C)s_(i,C)`. In any outcome, two such selected triples cannot share a vertex, because a vertex selects only one label. Hence at most nu(F) events occur at once, and taking expectations gives

    sum_(C in F) product_(i in C)s_(i,C) <= nu(F).

Cauchy interlacing bounds each proper 3-by3 principal determinant by `lambda5 lambda6 lambda7`. Combining this with(LOCAL-PRODUCT) and the expectation bound proves(PACK). □

## 3. Consequences and precise limits

If the linear family is pairwise intersecting, nu(F)=1 and(PACK) contradicts the strict critical capacity theorem. In particular this excludes any number of imbalanced triangles that form a linear intersecting family, even when they do NOT share one common hub. If the family has a disjoint pair, no contradiction follows. If two imbalanced triples share an entire edge, linearity fails and this theorem says nothing; the separate common-edge hitting-budget theorem covers only families with one common edge.

The proof uses exact row normalization, a three-term algebraic identity, independent finite label choices, principal-eigenvalue interlacing and the named Q/H capacity dependency. No numerical computation, optimizer, unsupplied positivity, new PH6 result, or proof of the capacity lemma is claimed here. Review must check the local product bound, disjoint-neighbor implication and finite expectation argument in addition to the capacity dependency. Historic process findings remain; held outputs are nonpremises.

END — under the linearity condition, a critical PH7 graph must contain two vertex-disjoint imbalanced triangles.
