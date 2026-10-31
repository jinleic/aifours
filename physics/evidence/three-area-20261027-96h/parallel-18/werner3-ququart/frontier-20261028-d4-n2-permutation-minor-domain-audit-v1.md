# Exact n=2 permutation-minor domain binding

**PhysicsResearch96h-2 / physics-1.** Native clock at completed result/hash observation: Wed Oct 28 20:01:25 PDT 2026. This is a fixed-d4 **source-span witness** audit. The actual pinned n=2 witness is valid; the guard observation below is not a source falsity, mathematical counterexample, automatic withdrawal, or f62/parent/human/model-family/formal acceptance.

## 1. Why the row domain is a real premise

The source-span rank sandwich uses the 14×14 n=2 permutation minor as a lower bound on the rank of the 24 permutation columns **inside** `(C²)^tensor4`. A matrix row is therefore indexed by a pair `(x,y)` of four-symbol words whose symbols are in `{0,1}`; the permutation columns are supported only at same-weight pairs. A determinant alone, without this domain binding, would not establish a minor of the actual target matrix.

The earlier standalone checker `frontier-20261028-commutant-standalone-verifier.py` hash-pins the witness and explicitly reconstructs its 0/1 matrix and determinant, but its inner `verify_permutation_minor` did not separately check that the supplied row labels are 4-tuples over `{0,1}`. Hash-pinning prevents an *unapproved modified file* from passing that checker; it does not by itself establish that a hash-pinned witness was semantically drawn from the claimed source basis. The actual data do satisfy the missing condition, as independently checked below.

## 2. Actual complete n=2 domain/determinant check

`frontier-20261028-d4-n2-permutation-minor-domain-check.py`, SHA256 `d84f770f219cd187f36dbd2131f0de369c9d86b662ee8f6fd3ce81f7d4930535`, reads only the pinned actual permutation-minor witness `frontier-20261028-permutation-span-integer-minors-results.json`, SHA256 `b8996e8f6fb9103be8ce6daa4798b0d5440c5544483ebf30c0ed8609c486e426`. It independently verifies all14 row pairs have length4, integer entries in `{0,1}` and identical x/y weights; the14 selected columns are distinct S4 permutations. It reconstructs the entire literal 14×14 action matrix and checks it equals the pinned matrix. Standard-library integer Bareiss elimination returns **determinant −1**.

Actual result `frontier-20261028-d4-n2-permutation-minor-domain-check-results.json`, SHA256 `8963ad473f3363b9dddcda8542b6406012c5dc17e2677eb7dbd0e15750dba6f4`, is **PASS**. This explicitly pays the n=2 permutation-lower-bound row-domain premise for the actual pinned witness. The separate n=2 commutator rank56, n=4 rank2692 and permutation rank24, physical tensor-product invariant argument, full source orbit identity and multiplier PSD remain required.

## 3. Exact in-memory guard fault and its limits

An in-memory relabeling maps every 0→2 and 1→3 in the witness row labels. It preserves all coordinate equalities, so the reconstructed 0/1 minor matrix and determinant remain identical, while every label leaves the claimed C² basis. A simulation of the old **inner index/matrix/determinant guards only** therefore accepts that relabeled mathematical object, whereas the new explicit domain guard rejects it. The complete old checker would also reject an altered witness **file hash**; no claim is made that a tampered file would pass its full pipeline. Wrong-weight and duplicate-row faults were also rejected. No pinned evidence bytes were changed.

The earlier commutant result is therefore still supported for its **actual** verified rows; the additional explicit domain check strengthens the witness interface rather than changing the theorem. No source-wide all-d, q3 operational, novelty or cross-family/formal claim follows from this component alone. This work is prospective after Main's explicit resumption; the earlier 20/30-minute cadence deviations remain separately disclosed and unaltered.
