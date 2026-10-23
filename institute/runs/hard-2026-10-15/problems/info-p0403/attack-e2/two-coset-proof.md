# Exact maximum for specified 32-free-point families

This is a restricted result. It does not answer whether an arbitrary
balanced nine-variable function with nonlinearity 242 exists. No novelty
is asserted.

For each of the three staged seeds g, define the four-dimensional linear
space V by the following basis, with integer labels denoting nine-bit
vectors and addition denoting bitwise XOR:

| Seed | Basis of V | Distinguished core coset |
|---|---|---|
| dsbf40 | 27,45,195,325 | 5+V |
| dsbf32 | 63,90,139,278 | 30+V |
| rsbf56 | 27,45,195,325 | 5+V |

The result files give the explicit ordered basis, all 16 members of V,
all 32 canonical coset representatives, and all 496 unordered pairs of
distinct cosets. The class consists of every function obtained by
changing arbitrary truth-table values on either coset in one such pair,
leaving all other inputs equal to g, and then adding any linear output
function. The exact maximum balanced nonlinearity in this union is 240.

## Why this is not a reused rotation-symmetric exclusion

This coordinate subcube is not an invariant symmetry class: every free
point can be varied independently. A common input permutation fixing
every function in the class would have to fix all free points pointwise.
An affine conjugate of the nine-cycle coordinate shift has exactly two
fixed inputs, whereas even one 16-point subcube has sixteen independent
free inputs. Thus these whole classes cannot be subsets of one common
affine-conjugate rotation-symmetric class. This is the relevant screening
argument, not a novelty claim.

## Complete enumeration by two half catalogues

Let V(t), t in F_2^4, be the ordered linear parameterization. The selected
cosets are p+V and q+V. Assign arbitrary new sign vectors A(t),B(t) in
{+1,-1}^16, and let their 16-point Walsh spectra be alpha_h,beta_h.
There are exactly 65536 choices for each half.

For each original Walsh index a, let h be the four parities a dot v_i,
d=a dot(p+q), and epsilon=(-1)^(a dot p). Remove the fixed outside
contribution and multiply by epsilon. The full new Walsh coefficient is
exactly

    epsilon W_new(a) = C_a + alpha_h + (-1)^d beta_h.

Here C_a is calculated entirely from the fixed values outside the two
cosets. For every h there are sixteen original indices with d=0 and
sixteen with d=1. Every one of the 512 character rows on the 32 free
points is checked against this identity by the independent auditor.
Consequently this factorization holds for all 2^32 assignments, without
sampling them.

For each of the 65536 first-half assignments, all original inequalities
`-28 <= W_new(a) <= 28` give an interval for each beta_h. From the complete
second-half catalogue, a 65536-bit set contains exactly the assignments
whose h-th coefficient lies in that interval. Intersecting the sixteen
sets retains exactly the second-half assignments satisfying all 512
bounds. A second union of exact-value sets identifies whether any
coefficient is zero. This is exhaustive finite-set coverage of all
65536*65536 assignments in each case, not random validation.

The producer uses 16-point FWHTs, extrema of offset groups, and equality
bitsets. The independent checker reconstructs every half spectrum by
sixteen-term direct sums; reconstructs the fixed outside contribution
from the full 512-point character matrix; derives every interval from
the individual original inequalities; uses cumulative range bitsets;
and intersects them in reverse order. It compares the exact counts and
SHA-256 digest of every nonempty legal second-half set.

The 496 cases per seed overlap. Counts with pair multiplicity must not
be interpreted as distinct-function counts for their union.

## Results and attainment

For each seed, the 31 coset pairs containing the core each have exactly
448 assignments preserving max|W|<=28. The other 465 pairs each have
exactly one, the original seed. The independent audit additionally
checks that no bound-preserving assignment changes any input outside
the core coset. The total count with pair multiplicity is therefore
31*448+465=14353, for each seed.

None of these surviving assignments has a zero Walsh coefficient, so
none can be balanced by adding a linear output function. This excludes
nonlinearity >=242 throughout the restricted class. A balanced function
has nonlinearity even, since all its Walsh coefficients are multiples
of four. Its nonlinearity here is therefore at most 240.

An attaining balanced table for each seed is explicitly stored in
`results/<seed>-flat-attainer.json`; each changes values only on the core
coset before its stated linear output shift. It is therefore included
in the larger class. Its weight 256 and all 512 coefficients are checked
by independent direct character sums. This proves the restricted exact
maximum 240, with an attainer.

`python3 code/replay_two_coset.py --independent` replays the entire audit.
It imports no producing code. The negative control
`python3 code/check_two_coset.py results/dsbf40-two-cosets.json --broken`
changes a claimed case count and must exit nonzero.
