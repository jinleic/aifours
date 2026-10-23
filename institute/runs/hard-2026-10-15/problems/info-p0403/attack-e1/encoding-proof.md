# Exact local-neighborhood statement and certificate correspondence

For each staged seed g (whose exact hex and bit convention are in
results/radius2.json), the claim is restricted to Hamming distance at
most six, followed by any linear output shift. No global exclusion or
novelty is asserted.

## Reduction to exactly six flips

The seed has even weight and no Walsh zero. An odd number of flips gives
odd weight; every linear output shift preserves weight parity in nine
variables, so no odd-distance modification can be balanced. Distances
two and four were exhaustively excluded independently, as recorded in
results/radius2.json and results/radius4.json. It remains to exclude
exactly six distinct flip points.

An arbitrary linear output shift can balance h precisely when W_h(a)=0
for some a. This shift only permutes the Walsh coefficients and preserves
nonlinearity. Thus it suffices to impose all 512 bounds and at least one
Walsh zero on h=g+1_S, without choosing a shift in advance.

## Binary-point encoding

The CNF selects r distinct integers x_1<...<x_r in [0,511], with nine
Boolean input bits per point. Lookup clauses exhaust all 512 values of
g(x_i). Shared XOR gates compute

    c_i(a) = g(x_i) + a dot x_i  (mod 2).

Let b_i(a)=c_i(a) if W_g(a)>0, and b_i(a)=1-c_i(a) if W_g(a)<0. These
are the indicators that the flipped sign opposes the old Walsh sign.
Write k_a=sum_i b_i(a), and M_a=|W_g(a)|. Then exactly

    sign(W_g(a))*W_h(a) = M_a - 2r + 4k_a.

For r=6, M_a is one of 4,12,20,28. The lower bound -28 is automatic
since M_a-12>=-8. The upper bound 28 is equivalent to

    k_a <= floor((28-M_a+12)/4).

Thus magnitude-28 seed coefficients impose k_a<=3; magnitude-20
coefficients impose k_a<=5; the others impose no upper restriction.
Each at-most constraint on the six literals is encoded by every
(k+1)-subset clause. This is an elementary exact encoding: it fails if
and only if at least k+1 literals are true.

A zero is possible only when M_a<=2r and 2r-M_a is divisible by four.
For r=6 these are exactly the 30 magnitude-four and 46 magnitude-twelve
positions. A selector for each possible position conditionally imposes

    k_a = (2r-M_a)/4.

One clause requires at least one selector. Equality is the conjunction
of an at-most constraint on b_i and one on its negations. No other
restriction (including algebraic degree) is included in the production
radius-six CNFs. The semantic auditor requires `forced_points=null`
and `degree_eight_necessary_constraint=false` for this claim.

Every distinct r-subset has one increasing-index assignment, every
character and lookup gate has its uniquely prescribed value, and any
actual zero can be selected. Conversely, every satisfying assignment
selects a genuine set and a true zero, with all 512 bounds. This proves
the exact correspondence of the restricted question and the CNF.

## Independent checks and controls

`code/audit_local_sat.py` imports no producing code. It reconstructs the
tables from staged literature and their spectra by direct character
matrix sums. It verifies every gate on its full truth table, each
lookup on all 512 rows, all cardinality subset clauses, all character
parities symbolically, and every strict-order circuit on all 262144
pairs of nine-bit integers. It rejects extra or missing constraints.
Its 65 sampled full flip-set checks are supplemental controls only;
they are not represented as independent exhaustion of the search range.

`code/check_lrat.py` imports no solver or producer. For each learned
clause, it assumes the negation and checks every listed unit-propagation
hint against earlier clauses until contradiction. It requires a checked
empty clause. Only positive RUP hints are accepted. Deletions are checked
as deletions; backward-trimmed proofs omit deletions and retain all
needed ancestors of the empty clause. Those trimmed proofs are checked
again from the original CNF before being used.

The full proof additions checked before trimming are:

| Seed | Variables | Input clauses | Checked additions |
|---|---:|---:|---:|
| dsbf40 | 6424 | 32497 | 1008178 |
| dsbf32 | 6424 | 32497 | 839741 |
| rsbf56 | 6424 | 32497 | 989282 |

The planted satisfiable control relaxes the Walsh bound to 32 and fixes
the six flip indices 16,50,88,96,131,153 for dsbf40. Its full SAT model
passes every CNF clause and independent direct-Walsh calculation. After
the independently determined linear shift it is balanced with
nonlinearity 240. This is a control, not a target witness.

A deliberately flipped lookup literal, with its file checksum updated,
is rejected by the semantic auditor. A deliberately invalid LRAT hint
is rejected by the proof checker. Corrupted tables are also rejected.

Consequently the neighborhood exclusions rest on both a checked
question-to-encoding correspondence and checked unsatisfiability
certificates, rather than multiple solvers sharing unchecked input.

## Affine scope

The same exclusion transports to any invertible affine change of input
variables and any affine output addition to a seed. Input permutations
preserve Hamming distance, weight, and nonlinearity. Output linear
addition permutes Walsh positions, and output complementation negates
the spectrum. Applying the inverse transformation would otherwise give
a flip set and Walsh zero already excluded above. This is an invariance
consequence of the stated local result; it does not expand the radius
or cover arbitrary Boolean functions.
