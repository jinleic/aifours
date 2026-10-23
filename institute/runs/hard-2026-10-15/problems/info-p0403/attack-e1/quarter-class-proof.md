# Exact balanced maximum for twelve specified quarter-table classes

This is a restricted result, not a resolution of the headline question.
All vectors below are integer labels of nine-bit vectors; sums are XOR.
No novelty is asserted.

For each seed g, start with its basis V in `two-coset-proof.md` and append
standard unit vectors in increasing order whenever they increase rank,
until the basis has seven members. Call the resulting 128-element
linear space U. The precise bases, all four canonical coset origins,
production CNFs, semantic audits, checked LRAT certificates, planted
controls, and explicit balanced attainers are listed in
`results/free128-batch.json`.

There are four classes per seed: arbitrary truth-table changes on one
coset p+U, all other values fixed to g, followed by any linear output
addition. Each class has exact maximum balanced nonlinearity 240. Each
has 128 independently free bits, so the upper-bound certificates cover
all 2^128 assignments. Their four domains are checked to partition all
512 inputs, but changing more than one domain is not covered.

## Encoding the complete class

Every Boolean assignment on the free coset is represented by 128 sign
words, each either +1 or -1. A nine-bit two's-complement FWHT circuit
computes their 128 Walsh coefficients. At each stage, the values lie in
[-128,128], strictly inside the signed range [-256,255]. Thus modular
word addition/subtraction equals integer addition/subtraction, without
overflow. The circuit records every ripple-adder bit step.

For each original index a, let h be the seven parities against the basis
of U, and epsilon=(-1)^(a dot p). The full coefficient satisfies

    epsilon W_new(a) = C_a + W_free(h),

where C_a is the normalized contribution of the fixed outside values.
The independent auditor reconstructs C_a by direct character sums and
checks this character identity on every one of the 512 original rows
and all 128 free points.

Each group h has four original coefficients. Their full bounds -28,28
give one exact interval for W_free(h). Signed interval comparisons are
implemented by complementing the sign bit and comparing the resulting
unsigned word. The auditor checks both comparison outputs on every
consistent nine-bit word value, not sampled values.

Selectors require some original coefficient to be zero; every possible
zero value in every group is included, and one must be selected.
Consequently all linear output shifts are covered.

The encoding also requires nonzero support XOR. This is justified by
`degree-bound-proof.md`: any balanced target with nonlinearity >=242
must have degree eight. Adding a linear output term leaves degree eight
unchanged. Such an even-weight function has nonzero support XOR, and
the seed's support XOR is zero. Thus this condition discards no possible
target. No unrestricted 2026 covering-radius theorem is used.

## Independent universal audit and certificate replay

`code/audit_free_flat.py` imports no producer. It checks every gate's
complete truth table, all ripple-adder bit identities, the entire FWHT
wiring, the exact initial +/-1 words, all original character rows and
outside sums, every interval comparator value, all zero selectors, and
the support-XOR identity symbolically. It rejects omitted or extra
constraints. These are universal local-composition checks: no sample of
the 2^128 truth assignments is used to assert completeness.

`code/check_lrat.py` then checks the complete empty-clause derivation.
This combines an audited mathematical encoding with an independent
unsatisfiability certificate, rather than merely two solver verdicts.

For every case, the bound-32 control fixes two explicitly chosen changed
points that create a Walsh zero. Its SAT model is checked clause by
clause and by direct full Walsh sums. After the stated linear output
shift it is an explicit balanced table with nonlinearity 240. All twelve
attainers are stored with indexed bit order, SHA-256 and every Walsh
coefficient in `*-balanced-attainer.json`, and are independently checked.

Since balanced nonlinearity is even, absence of balanced nonlinearity
>=242 gives the class upper bound 240. The explicit attaining tables
give equality for each of the twelve classes.

`python3 code/replay_free128.py --independent` checks all twelve
certificates, models, domains and direct-sum attainers. The intentional
broken-gate control
`python3 code/audit_free_flat.py results/dsbf40-free128 --broken`
must fail.
