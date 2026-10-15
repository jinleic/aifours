# Why the unnormalized linear relaxation cannot refute the completion

Date: 2026-10-14 PT. This is a written combinatorial observation and an exact-rational finite check, not a construction, impossibility theorem for LKTS, or new claimed literature result. It supplements the HMZ actor's genuine released-system search. It is not itself asserted to be Lean-certified.

## General lemma

Let X have odd order v and put h=(v-1)/2. Suppose k pairwise block-disjoint KTS(v)s have already been fixed. Let U be the triples not used by them. Suppose a group of order p preserves U and every triple orbit in U has size p. Let r be a positive integer such that v-2-k=rp.

For each orbit O in U, each block B in O, each free-base label a in{0,...,r-1}, and each resolution-class label c in{0,...,h-1}, use a nonnegative variable x[O,B,a,c]. The unnormalized exact-cover relaxation imposes:

1. sum x over all placements of each orbit O equals1;
2. for each free base a and each unordered pair e, sum x over B containing e and all classes c equals1;
3. for each free base a, each class c and each point y, sum x over B containing y equals1.

**Then x=1/(rph) on every permitted row is a feasible rational solution.**

**Proof.** An orbit has p blocks, r base labels and h class labels, hence rph rows. A pair belongs to v-2 triples in the complete3-uniform hypergraph and exactly one in each of the k fixed STSs. It therefore belongs to rp remaining triples, giving rph rows for a fixed free base after class labels are included. At a point y the remaining point-pair incidences number (v-1)rp; every remaining triple through y accounts for exactly two of these incidences. Thus the number of remaining triples through y is (v-1)rp/2=h rp, again exactly the denominator. All three constraints sum to1. This argument counts actual pairs/points and does not assume a future integral completion or resolution. Bounds0<=x<=1 hold because r,p,h are positive.

Deleting class labels yields the analogous pair-cover relaxation with uniform weight1/(rp). Consequently a separating linear inequality valid for precisely these linear equalities and nonnegativity cannot prove this polytope empty: it contains this explicit point. Additional integral, nonlinear, cutting-plane or symmetry-breaking restrictions can change the conclusion. In particular this observation does not predict CP-SAT runtime and does not cover the symmetry-pruned class-placement matrices of the historical implementation.

## Application to the checked57 packing and released-system16 route

For v=57,k=17,p=19,r=2,h=28:

- U has20,216 triples in1,064 full C19 orbits.
- Every pair belongs to38 triples of U; every point belongs to1,064 triples of U.
- Pair-cover placements have uniform weight1/38.
- Full unrestricted class placements have uniform weight1/1,064, with1,132,096 rows before any class symmetry restriction.

After releasing zero-based system16, the16 retained systems leave1,092 orbits. In the joint linear relaxation, select the original released system's genuine resolved rows integrally; they use28 orbits. Set all free-base variables on those28 orbits to0, and use the fractional assignment above on the other1,064 orbits. This is an explicit mixed integral/fractional feasible point for the joint relaxed problem. It does **not** freeze the replacement in the actual construction attempt, and says nothing about whether any replacement permits two integral resolved free bases.

`check_fractional.py` reuses the existing independent fixed-system verifier, checks the16/17 packing orbit sets and the exact concrete pair/point degrees, and evaluates both weights using Python `Fraction`. A wrong denominator37 is a negative control and must fail the exact-one pair/orbit conditions. The saved receipt is `fractional-receipt.json`; it must be consulted for actual execution status.

## Conditional application to87

If the27 fixed resolved C29 constituents of the surviving pattern existed, then v=87,k=27,p=29,r=2,h=43 gives the same uniform pair-cover weight1/58 and class-placement weight1/2,494 on the2,494-orbit complement. This is conditional on a suitable27-packing; none is supplied by this observation. The exact integral compatibility of fixed systems and free bases, and their genuine resolutions, remain missing.

## Status

The observation isolates integrality and simultaneous resolution/orbit compatibility as the real bottleneck; the basic incidence LP is never a nonexistence certificate in these hypotheses. The universal book question and both57/87 constructions remain unaffected. No novelty or universal impossibility claim is made.
