# K7-D23 obstruction: an explicit joint double-3 pattern passes all LFC, INV and T tests (no coset construction)

- **Written:** 2026-10-19T03:16:02-0700 (`/bin/date`, immediately before exclusive creation).
- **Status:** precise obstruction note, written derivations only, no computation. This is an abstract necessary-rule
  pattern, NOT seven actual disjoint cosets, NOT a counterexample, NOT a Sun(7) exclusion. Full target OPEN.
- **Scope frozen here:** distinct 2-marker z and 3-marker t, 5-marker absent. All E,A >= 1 below are actual unbounded
  exponents; all w_i are pairwise coprime positive integers, each coprime to 30.
- **Imports:** the accepted K7 definition, LFC, INV, triangle T and criterion F7 pinned in `K7-D23-NO4-v1.md` SHA
  a3b47626687141dac49daf30aab302c1ea66f15a74f28ee638b2212258de189d (its new claims are NOT premises of this note).
  Explicit proofs below show which inequalities the pattern satisfies. No computation or exploratory miss is used.

## 1. Exact pattern P(E,A,w)

Let W={u1,u2,u3,u4,u5}, with

  n_z=6*2^E*w_z,  n_t=6*3^A*w_t,  n_u=6*w_u (u in W),   E,A>=1.

All pairwise index gcds are 6 (K7). Put the two symmetric abstract matrices equal, alpha*=alpha, with

  alpha_zz, alpha_tt, alpha_uu undefined (diagonal unused);
  alpha_zu=3 (u in W),   alpha_uv=3 (distinct u,v in W),
  alpha_tu=2 (u in W),   alpha_zt=1.

Thus {z} union W is a full 6-vertex clique of 3s in both matrices; t has five 2s and one 1. The two z-rows are both
3-type (five W-threes, t-entry 1), so this pattern lies in the double-3 residue of `K7-D23-NO4-v1.md`.
INV's bounds hold entrywise: (3,3) sums to 6, (2,2) to 4, (1,1) to 2, each positive. Equality of the two abstract
matrices is not a claim that conjugated subgroups realizing them exist.

## 2. Every LFC inequality holds in both orientations, with the actual strict finite bound

Allowed sets depend only on pairwise local-label gcds. We compute the maximum of sum y_j alpha_vj over all
nonnegative feasible weights, NOT by enumeration. Multiplication by 1/6 gives the LFC objective. For a row of a
hypothetical configuration the necessary upper bound is 6*(1-1/n_v), strictly less than 6.

### 2.1 Apex z

Neighbour labels: lambda_u=3w_u for the five u in W, lambda_t=3^A w_t. All pairwise gcds equal 3. Hence allowed sets
are exactly sets of size at most 3. By averaging any feasible weight vector over permutations of W (the allowed
system and objective are invariant), write weight p on W and q on t. Constraints include 3p<=1 and 2p+q<=1.
Therefore

  sum y alpha = 15p+q <= 1+13p <= 16/3,

with equality p=q=1/3 (all allowed triples sum to 1). Since n_z>=12,

  16/3 < 11/2 <= 6*(1-1/n_z).

So every z-row LFC inequality is satisfied, including its actual finite slack.

### 2.2 Apex t

Neighbour labels: lambda_u=2w_u (u in W), lambda_z=2^E w_z. All pairwise gcds equal 2; allowed sets are exactly sets
of size at most 2. Averaging over W gives weights p on W and q on z; 2p<=1 and p+q<=1. Then

  sum y alpha = 10p+q <= 1+9p <= 11/2,

with equality p=q=1/2. Since n_t>=18,

  11/2 < 17/3 <= 6*(1-1/n_t).

### 2.3 Apex u in W

The four other W labels are 3w_v, the z-label is 3*2^E*w_z, and the t-label is 2*3^A*w_t. All pairwise gcds are 3
EXCEPT the z,t pair, whose gcd is exactly 6 (E,A>=1). Allowed sets are exactly all sets of size at most 3 and the
4-sets containing both z and t. No 5-set is allowed: any such set contains a 4-subset omitting z or t, with every
pairwise gcd equal 3. Averaging over the four other W vertices gives weights p there, q on z and r on t. Constraints
include 3p<=1 and 2p+q+r<=1 (an allowed 4-set). Thus

  sum y alpha = 12p+3q+2r <= 12p+3(q+r) <= 3+6p <= 5.

Equality is attained by p=q=1/3, r=0. Since n_u=6w_u>=6,

  5 <= 6*(1-1/n_u).

At w_u=1 equality is compatible with LFC's non-strict finite inequality (the strict statement is <6, not <5).
All other feasible y satisfy the bound too, by the displayed maximum. Because alpha*=alpha, all inverse rows obey
exactly the same calculations. This proves the claimed full LFC/INV feasibility for arbitrary E,A,w.

## 3. Every triangle T passes, in both orientations; F7 has no forced pair

Here ell_i=r_i, all g_ij=gamma_i=6. The four possible types of triangle are below; these are symbolic types, not a
computed finite census.

| triangle | three alpha-values | tau_min | tau_max |
|---|---|---|---|
| three vertices of W | (3,3,3) | 3 | 9 |
| z and two W vertices | (3,3,3) | 3 | 9 |
| t and two W vertices | (2,2,3) | 2 | 4 |
| z,t,u with u in W | (1,3,2) | 1 | 2 |

Derivation: in the first two types, every compulsory 3 survives division by the opposite ell (ell_z has only an
extra 2-power), and every apex upper bound is 3*3=9. In t+W+W, the opposite ell_t contains 3 and removes the 3 from
the W-W edge; each remaining edge requires 2, so tau_min=2; the minimum apex product is 2*2=4. In z,t,u, ell_t
removes the 3 on z-u, ell_z removes the 2 on t-u, and the z-t edge is 1, so tau_min=1; the minimum product of the
other two edge values is 1*2=2. Thus each triangle admits at least tau=tau_min, which is positive, meets every
T1 divisibility and T2/T3 bound. These computations use only E,A>=1 and coprimality of the w's; they hold for all
unbounded exponents. The inverse table is identical.

F7 at any apex reduces (g=gamma=6) to tau_min >= (opposite alpha)*(one adjacent alpha). For a (3,3,3) triangle the
smallest such product is 9>3; for (2,2,3) it is 4>2; for (1,3,2) it is 2>1. Hence **the sufficient F7 criterion
forces no containment anywhere** in either matrix. This does not assert that hypothetical actual sets could not
have additional containments established by other arguments.

## 4. Local integer LFC incidence exists in the smallest profile (illustration, not global realizability)

Take E=A=1 and all w_i=1, so indices are n_z=12, n_t=18, n_u=6. The following written constructions show that the
row-feasibility above is not hiding a simple fibre-count integrality obstruction. Each construction is LOCAL to
its apex; the constructions are not coupled and are not group actions/cosets.

- **At u in W:** let B consist of z and the four other W vertices, cyclically labelled 0=z,1,2,3,4. The five fibres
  take the triples complementary to the five edges of the cycle 0-1-2-3-4-0; each B-vertex occurs three times.
  Add t to any two of the three triples containing z. Those 4-sets are allowed. Counts are 3 for each B-vertex,
  2 for t, exactly n_u*alpha_uj/6, in the n_u-1=5 available fibres.
- **At z:** start with all ten triples of W (each W-vertex occurs six times). Replace {u1,u2,u3} by {t,u2,u3} and
  {u1,u4,u5} by {t,u1,u5}, then add {u1,u4}. There are 11 fibres, all of size <=3; counts are six for each W-vertex
  and two for t, exactly n_z*alpha_zj/6.
- **At t:** start with three copies of the five edges of a cycle on W (15 fibres, degree six at each W-vertex).
  Replace one edge {u1,u2} by {u1,z} and {u2,z}, then add singleton {z}. There are 17 fibres, all of size <=2;
  counts are six for each W-vertex and three for z, exactly n_t*alpha_tj/6.

No search, program, numerical LP or solver produced these lists.

## 5. Exact missing lemma / limits of the obstruction

**Missing lemma:** show that no actual finite group with seven pairwise disjoint left cosets can realize the joint
pattern P(E,A,w) of section 1, uniformly for E,A>=1 and all pairwise-coprime prime-to-30 w_i. Any full closure of the
different-vertex family must in particular exclude this precise subfamily. Merely reapplying LFC, INV, T or the
F7 sufficient criterion at the same level cannot do so: all their stated necessary numerical conditions pass by
sections 2-3, and even the primitive local fibre counts pass by section 4.

This note does NOT claim P passes Ppair, the full RPLP constraints, TG, higher-intersection or nonlocal group
constraints. Those were not checked here. It is NOT asserted realizable by subgroups. It is a precise obstruction
to the named written rules alone, not to a stronger proof.

The accepted K63-CLIQUE theorem does not exclude P: although {z} union W is an all-3 six-clique, its remaining
vertex t has gcd 6 with that clique (K7), not gcd 3 (K6.3). In the analogous VFC step at an unmarked apex,
mu(D_t)=alpha*_ut/6=1/3, not the K6.3 value 2/3. Importing the K6.3 conclusion without these hypotheses would be
invalid. TG itself remains a permitted general lemma, but no TG exclusion of P is claimed in this note.

Also still open and NOT covered by this note: a 5-marker in any position, particularly shared2/3 on z plus a
separate 5-marker y; the third-vertex-5 mixed rows; and other double-3 z-row patterns. No broad residual closure is
inferred from this one explicit family.
