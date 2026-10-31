RESULT: VALID

# Exact physical review of the three-member witness

The pinned witness satisfies the pinned **physical** definition of three mutually orthogonal quantum Latin squares of order 8 in the same cell coordinates. One member is genuinely nonclassical; the other two are classical Latin squares in the supplied standard basis. This is a finite, exact-arithmetic verdict on these bytes only. Number members as quantum 0 and classical 1 and 2; all row, column and coordinate indices below are zero-based.

## Inputs, execution and binding

The manifest, definition and witness were read before the verifier was written. The single invocation `python3 -B verifier-check-v1.py` started at `2026-10-28T20:10:54.607276-07:00`; its receipt records `2026-10-28T20:10:54.647127-07:00`. It used Python 3.14.3 and completed `VALID`, with all seven retained mutation controls rejected for their intended reasons. The verifier reads no author checker/producer, solver, catalog or held mathematics. The full execution evidence, error details and fixture hashes are in [`verifier-receipt-v1.json`](verifier-receipt-v1.json).

| Input or artifact | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| [`manifest-v1.json`](manifest-v1.json) | 2,935 | 43 | `bc1753bab7dc9efa691a13ab8fa03be2b403172c00b837d503d04a745f74f9f0` |
| [`physical-definition-v1.md`](parent-inputs-v1/physical-definition-v1.md) | 2,115 | 11 | `3df4d2bec7f566a66508110176e8217c15e38025323b6f19444e70e435c01fff` |
| [`witness.json`](parent-inputs-v1/witness.json) | 8,040 | 891 | `a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413` |
| [`verifier-check-v1.py`](verifier-check-v1.py) | 20,784 | 484 | `13733053c30da47e7d074b6aee0f0eb05a53d9df0773c21c30683ead8c28c0a8` |
| [`verifier-receipt-v1.json`](verifier-receipt-v1.json) | 10,705 | 478 | `66d4f70f48720c698f082e320af80de7d7634a46d846cc61aeb59e4145367bed` |

The three pinned inputs also had zero CR bytes and ended in LF. The manifest hash agrees with the frozen manifest pin; the definition and witness SHA-256, byte and LF counts agree with their manifest entries. The checker rejects duplicate JSON keys, unrecognized or missing root fields, malformed dimensions, noninteger components or labels (including booleans), invalid or nonpositive denominators, out-of-range labels and duplicated or invalid trade-cell indices. It requires exactly 64 row-major length-8 quantum numerator vectors, 64 corresponding squared denominators, and two 8-by-8 classical label matrices.

## Exact checks

For an integer numerator vector `a` and squared denominator `d`, the represented vector is `a/sqrt(d)`. The actual witness uses only `d=1,2`, so all its coordinates lie in `Q(sqrt(2))`. The verifier constructs the standard-basis vectors for the classical labels, uses integer dot products and exact rational arithmetic, and never approximates a square root. In particular,

- `||a/sqrt(d)||² = (a·a)/d`, and the squared modulus of a single-vector inner product is `(a·b)²/(de)`;
- the squared modulus of a tensor-product inner product is the product of the two corresponding squared overlaps. Checking these exact nonnegative rationals against 0 or 1 is sufficient for the required Gram conditions.

The complete successful counts are:

| Check | Exact coverage |
|---|---|
| Classical Latin property | All 16 rows and all 16 columns of the two classical members contain the complete label set `0..7`. |
| Row/column ONBs | All 48 member-lines; 8 squared norms and all 28 unordered off-diagonal overlaps per line, totaling 384 norms and 1,344 overlaps. Every norm is 1 and every overlap is 0. |
| Pair (0,1) products | All 4,096 ordered Gram entries: 64 diagonal entries and 4,032 off-diagonal entries, corresponding to all 2,016 distinct cross pairs. |
| Pair (0,2) products | The same full 4,096-entry Gram check. |
| Pair (1,2) products | The same full 4,096-entry Gram check. |

Every product Gram diagonal is 1 and every off-diagonal entry has squared modulus 0. Thus, in each case, the 64 same-cell product vectors are an orthonormal basis of the 64-dimensional tensor-product space, not merely a set of distinct labels or a sample of constraints.

## Nonclassicality and mixed cells

Quantum cell `(0,0)` is `e0`, and cell `(2,2)` is `(e0+e1)/sqrt(2)`. Their exact squared overlap is `1/2`, strictly between 0 and 1. A member whose cells are all rays of one global orthonormal frame can have only 0 or 1 as squared overlaps; the displayed intermediate value survives per-cell phases, row/column permutations and a global unitary. It therefore certifies genuine memberwise nonclassicality, separately from the mixed-cell count.

Exactly eight cells have support on more than one supplied standard-basis vector: `(2,2)`, `(2,3)`, `(3,2)`, `(3,3)`, `(4,4)`, `(4,5)`, `(5,4)` and `(5,5)`. Each has support `{0,1}` with squared basis overlaps `1/2, 1/2`. Their row-major indices are `18, 19, 26, 27, 36, 37, 44, 45`; these match the witness's `trade_cells` exactly.

## Retained intended-reason controls

Each fixture was created from the pinned positive witness, retained under this directory, reread and hashed, and checked within the **same single invocation**. The checker matched both the indicated rejection class and the prescribed location/value, not just an arbitrary exception.

| Fixture | Observed intended rejection |
|---|---|
| [`verifier-mutation-swapped-row-labels-v1.json`](verifier-mutation-swapped-row-labels-v1.json) | `classical_latin_column`: member 1, column 0; swapping two entries leaves their row a permutation but breaks a column. |
| [`verifier-mutation-duplicate-label-v1.json`](verifier-mutation-duplicate-label-v1.json) | `classical_latin_row`: member 1, row 0. |
| [`verifier-mutation-relabeled-classical-member-v1.json`](verifier-mutation-relabeled-classical-member-v1.json) | `pair_overlap`: members 1 and 2, cells `(0,0)` and `(1,3)`, squared overlap `1`. Member 2 is replaced by a cyclic symbol relabeling of member 1; both members remain Latin. A mere global symbol relabeling of the original member 2 would preserve its product orthogonality and would not be a valid negative control. |
| [`verifier-mutation-superposition-sign-flip-v1.json`](verifier-mutation-superposition-sign-flip-v1.json) | `line_overlap`: quantum row 2, cells `(2,2)` and `(2,3)`, squared overlap `1`. |
| [`verifier-mutation-altered-denominator-v1.json`](verifier-mutation-altered-denominator-v1.json) | `line_norm`: quantum cell `(2,2)`, squared norm `2/3`. |
| [`verifier-mutation-truncated-vector-v1.json`](verifier-mutation-truncated-vector-v1.json) | `quantum_vector_length`: cell `(2,2)`, expected 8, actual 7. |
| [`verifier-mutation-mixed-cell-basis-replacement-v1.json`](verifier-mutation-mixed-cell-basis-replacement-v1.json) | `line_overlap`: replace `(2,2)` by `e0`; its squared overlap with `(2,3)` is `1/2`. |

## Limits

This is an independently written, same-harness finite verifier, not an independent-family, human, or formal/kernel review. No literature or primary-source priority audit was performed in this slice. **Nothing here establishes any claim about `M(8)`, source priority, novelty, a fourth family, or closure of the original four-family target.**
