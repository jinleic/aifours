# Independent exact replay of the three-member physical witness

**RESULT: PASS**

Observed clock before this report: 2026-10-28T20:11:29-0700 PDT.

## Byte binding

- `manifest-v1.json`: SHA-256 `bc1753bab7dc9efa691a13ab8fa03be2b403172c00b837d503d04a745f74f9f0`, 2935 bytes, 43 LF.
- `parent-inputs-v1/physical-definition-v1.md`: SHA-256 `3df4d2bec7f566a66508110176e8217c15e38025323b6f19444e70e435c01fff`, 2115 bytes, 11 LF.
- `parent-inputs-v1/witness.json`: SHA-256 `a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413`, 8040 bytes, 891 LF.
- `replay-check-v1.py`: SHA-256 `becb47d1e37a8147152823f8e3e2bf0621c19a9c75a7162c655c2cd4b36fc6ba`, 26891 bytes, 484 LF.

The frozen manifest and its first two input pins were compared to the hard-coded full hashes, byte counts and LF counts before calculation.

## Method and finite result

A cell is an eight-integer numerator and a positive integer squared denominator. For each member and each row/column, every one of the 8×8 integer Gram entries is checked: diagonal numerator equals its denominator, and every off-diagonal numerator is zero. For each pair, this replay explicitly constructs all 64 length-64 Kronecker numerators with squared denominator equal to the product of the two cell denominators, then checks all 64×64 integer Gram entries against the corresponding diagonal denominators and off-diagonal zeros. Thus no floating point or factorized Gram shortcut is used.

| Check | Matrices | Entries | Mismatches |
|---|---:|---:|---:|
| Q row/column | 16 | 1024 | 0 |
| A row/column | 16 | 1024 | 0 |
| B row/column | 16 | 1024 | 0 |
| Q-A tensor Gram | 1 | 4096 | 0 |
| Q-B tensor Gram | 1 | 4096 | 0 |
| A-B tensor Gram | 1 | 4096 | 0 |

Quantum mixed cells relative to the supplied basis: [18, 19, 26, 27, 36, 37, 44, 45] (count 8); stated trade cells: [18, 19, 26, 27, 36, 37, 44, 45].
Q distinct-cell squared-overlap histogram: `{"0": 1760, "1": 192, "1/2": 64}` (2016 unordered pairs).
A distinct-cell squared-overlap histogram: `{"0": 1792, "1": 224}` (2016 unordered pairs).
B distinct-cell squared-overlap histogram: `{"0": 1792, "1": 224}` (2016 unordered pairs).

Nonclassicality certificate: Q cells [0, 0] and [2, 2] have exact squared overlap **1/2**, with numerator vectors `[1, 0, 0, 0, 0, 0, 0, 0]` and `[1, 1, 0, 0, 0, 0, 0, 0]` and squared denominators 1 and 2. A single global orthonormal output frame with per-cell phases permits only overlap squares 0 or 1; this strict intermediate value rules it out. The mixed count by itself is not the certificate.

## Positive classical control

Replace each (e0+e1)/sqrt(2) by e0 and each (e0-e1)/sqrt(2) by e1; leave both supplied classical members unchanged.
The transformed cells are [18, 19, 26, 27, 36, 37, 44, 45]. All three members consist of normalized standard-basis vectors; all 48 member line Grams and all three 64×64 pair Grams pass. This gives an independently checked classical three-member control from the two supplied mates and the observed exact +/- structure. The complete canonical control fixture is retained, hashed, in the receipt.

## Intended-reason negative controls

- **PASS** `row_permute_only_A` — all member bases survive, but A-B same-cell tensor orthogonality fails; observed `{"expected_integer": 0, "integer_inner_product": 1, "kind": "off_diagonal", "left_cell": 0, "left_denominator_squared": 1, "right_cell": 29, "right_denominator_squared": 1}`. Fixture SHA-256 `b19000a2afe570e3a4e90935f7c4099d22b87973548646f44ef909924af66e83`.
- **PASS** `transpose_only_Q` — all member bases survive, but Q-A same-cell tensor orthogonality fails; observed `{"expected_integer": 0, "integer_inner_product": 1, "kind": "off_diagonal", "left_cell": 4, "left_denominator_squared": 1, "right_cell": 15, "right_denominator_squared": 1}`. Fixture SHA-256 `0baef6f55f10b1847b871f715d07661a168bfea524f698bf7404782a8d1d9e48`.
- **PASS** `replace_plus_by_minus` — the two superpositions in quantum row 2 have nonzero off-diagonal overlap; observed `{"axis": "row", "expected_integer": 0, "integer_inner_product": 2, "kind": "off_diagonal", "left_cell": 18, "left_denominator_squared": 2, "right_cell": 19, "right_denominator_squared": 2, "slice": 2}`. Fixture SHA-256 `49bbe7d5b61610e4f4c6289f04ef163b11356bdfd644d4b2261f1dc60f4c5d7a`.
- **PASS** `double_without_normalizer` — the quantum row-0 Gram diagonal is 4 instead of 1; observed `{"axis": "row", "expected_integer": 1, "integer_inner_product": 4, "kind": "diagonal", "left_cell": 0, "left_denominator_squared": 1, "right_cell": 0, "right_denominator_squared": 1, "slice": 0}`. Fixture SHA-256 `96eb686a9f257f619c2976de47e4e5a83324e1d87940fe8de26c8604c14ad7ac`.
- **PASS** `column_permute_only_A` — all member bases survive, but A-B same-cell tensor orthogonality fails; observed `{"expected_integer": 0, "integer_inner_product": 1, "kind": "off_diagonal", "left_cell": 0, "left_denominator_squared": 1, "right_cell": 43, "right_denominator_squared": 1}`. Fixture SHA-256 `de098becacca72a85d2f55119b6ba252262b0df1f23fec19396197c5ed6d5f45`.
- **PASS** `swap_two_Q_cells_in_one_row` — every quantum row survives, but column 0 has a nonzero off-diagonal overlap; observed `{"axis": "column", "expected_integer": 0, "integer_inner_product": 1, "kind": "off_diagonal", "left_cell": 0, "left_denominator_squared": 1, "right_cell": 8, "right_denominator_squared": 1, "slice": 0}`. Fixture SHA-256 `f090debd5d52eadd1450876f5e34990f10e12703ffb43a8011d0200c96cf5e91`.
- **PASS** `duplicate_one_A_label` — a single relabel creates a nonzero classical row Gram off-diagonal; observed `{"axis": "row", "expected_integer": 0, "integer_inner_product": 1, "kind": "off_diagonal", "left_cell": 0, "left_denominator_squared": 1, "right_cell": 1, "right_denominator_squared": 1, "slice": 0}`. Fixture SHA-256 `216519f13f291bea5b722f9288b71279ec636b7adcbc4472cb721b8b98b5ee40`.
- **PASS** `zero_denominator` — strict input validation rejects a nonpositive squared denominator; observed `{"code": "bad_normalizer", "detail": "cell 0: denominator_squared must be a positive integer"}`. Fixture SHA-256 `34462c08c61ab4e3f334de4ff2b5539933ecf5862d3ec6479bbb531cc58451cb`.
- **PASS** `duplicate_json_key` — strict JSON parsing rejects a duplicated top-level key; observed `{"code": "duplicate_json_key", "detail": "duplicate key: kind"}`. Fixture SHA-256 `b8cd2b40e28633660a166fa3e91076232bc817b6989f022d0d5a8d08b10b3fce`.
- **PASS** `short_quantum_vector` — strict input validation rejects a seven-coordinate vector; observed `{"code": "quantum_vector_shape", "detail": "cell 0: need eight integer coordinates"}`. Fixture SHA-256 `f7b95bb5108e992fe25d630fa4960cea0811c642f4899b64778884e295353a6c`.

Each complete literal/canonical mutated fixture, its hash, every control's intended reason and the observed diagnostics are preserved in `replay-receipt-v1.json`.

## Limits

This is one same-harness independent implementation of a finite physical check, not a human, independent-family, external-vendor, formal/kernel or exhaustive review. It does not audit the external source definition, current literature or priority, and does not establish any M(8) claim. It checks only three members; the registered four-family alternative remains open from this result. No author producer/checker, solver, catalog, held mathematics, external model, or network source was used.
