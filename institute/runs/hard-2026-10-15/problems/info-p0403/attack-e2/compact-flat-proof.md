# Two certificate-supported free-flat maxima

This is a restricted result. The former assertion for twelve quarter-
table classes is withdrawn: eleven corresponding certificates are
unavailable. Only the following two classes are claimed. No novelty is
asserted.

| Seed | Basis of U | Free domain | Free bits | Preserved LRAT proof |
|---|---|---|---:|---|
| dsbf40 | 27,45,195,325,1,2 | 5+U | 64 | results/dsbf40-free64.lrat.gz |
| dsbf32 | 63,90,139,278,1,2,4 | U | 128 | results/dsbf32-free128-origin0.lrat.gz |

Integer vectors are nine-bit input labels and addition is XOR. All
values on the free domain may change independently, all outside values
remain equal to the explicit seed, and any linear output function may
then be added. Each class has exact balanced maximum nonlinearity 240.
Changes on larger domains are not covered.

## Complete encoding

A sign word for each free input is either +1 or -1. A signed FWHT
circuit computes the n free-domain coefficients, with word width
log2(n)+2: widths 8 and 9 for n=64 and n=128. True intermediate values
lie in [-n,n], strictly inside the signed range; modular arithmetic
therefore equals integer arithmetic without overflow.

For each original Walsh index a, let h be its parities against the basis
and epsilon=(-1)^(a.origin). Exactly

    epsilon W_new(a) = C_a + W_free(h),

where C_a is the normalized outside contribution. Every original
character row and every free point in that row is independently checked
against this identity. Direct outside sums give the exact interval for
each free-domain coefficient imposed by all original bounds -28,28.

The 64-point circuit forbids all disallowed word values. The 128-point
circuit uses signed interval comparators, audited at every consistent
nine-bit word. Zero selectors include every possible value creating a
zero in every Walsh group. Requiring one covers all balancing shifts.

The encoding requires nonzero support XOR. By `degree-bound-proof.md`,
every balanced target has degree eight. A linear addition preserves its
degree-eight coefficients, which are exactly the support-XOR bits for
an even-weight function. The seed has support XOR zero, independently
checked. Thus this requirement discards no target. The unrestricted
covering-radius preprint is not assumed.

## Audit, proof, and attainment

The auditor imports no producer. It exhausts every gate truth table and
full-adder bit identity, checks all FWHT wiring and initial sign words,
all original character rows and outside sums, every comparator value,
all zero selectors, and the support-XOR identity symbolically. It
rejects omitted or extra constraints. These are universal composition
checks, not samples of 2^64 or 2^128 assignments.

The separate Python LRAT/RUP checker verifies every learned clause from
its listed unit-propagation hints and requires an empty-clause
derivation. Compressed CNFs and metadata preserve their uncompressed
SHA-256 hashes. The 64-point CNF was deterministically regenerated and
matched the original CNF hash of its preserved proof before replay.

Both bound-32 planted controls have complete SAT models checked clause
by clause and by direct full Walsh sums. The balanced NL240 attainers
are `results/dsbf40-flat-attainer.json` and
`results/dsbf32-free128-origin0-control-balanced-attainer.json`. Direct
sums check their weight and nonlinearity; removing their stated linear
output shifts verifies that changes lie wholly in the free domain.

Balanced nonlinearity is even, so excluding >=242 gives an upper bound
240; the attainers prove equality. The independent path of
`python3 code/replay_compact_flats.py --independent` never imports
producing code and checks exactly these two classes.

These are free coordinate domains, not invariant symmetry classes. A
common input permutation fixing every table must fix all free points
pointwise. A conjugate of the nine-cycle shift has only two fixed inputs
and cannot fix these 64 or 128 independent free points. This screen is
not a novelty claim.
