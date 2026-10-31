# Complete finite classification of the full-state-only functional relaxation

## Required first inputs

1. Read `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` (SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`) before its source consumers: the publisher's cross-branch omission is Remark 5.4, not 3.8.
2. Read `frontier-20261029-primal-checker-subset-coverage-erratum-v1.json` before any primal-checker evidence. Two new v1 primal checkers had an incomplete subset iterator. Their claimed full coverage is withdrawn; only the corrected v2 replays below carry the primal claims. Old dual and copy-certificate checkers were unaffected.

**Status: WRITTEN with exact independently checked finite identities and profiles; mathematical review/formalization/novelty clearance unperformed.** This is a complete classification of one specified relaxation, not a solution of the R-minus guessing-number problem or a full classification of actual binary-plane laws.

**Boundary.** No f161 review/parent consumer and no paused imported-functional-gates episode is an input. The only entropy gate here is the old full-state gate. No theorem about laws with two syndrome values is imported.

## 1. The finite algebraic result

The residual binary-plane census has 515 canonical parity colorings, representing 1,905 direction planes. For the functional relaxation specified below:

| Exact disposition | Canonical classes | Direction planes |
|---|---:|---:|
| An exact conic identity proves Delta <= 0 | 495 | 1,841 |
| A positive exact rational relaxation profile exists | 20 | 64 |
| Total | 515 | 1,905 |

The two sets are disjoint and exhaustive. The four factor-preserving graph automorphisms, their closure, coloring canonicalization under their four actions times the six functional relabelings, and the plane-orbit accounting were checked exactly.

**Master receipt.** `frontier-20261029-plane-functional-v1-complete-classification-v1.json`, SHA-256 `8a66da6344c8f4f1d7bc59ba29ac1a63ba0b9caff0ad47c37dce922f4957e930`. It binds every certificate bundle and checker receipt, the residual census, and all exact positive profiles.

## 2. What is being classified

Write Delta = H(Y_V) - (2/3) sum_v H(Y_v). The coloring labels each of the ten triangle factors as fixed (`-`) or as one of A, B, A+B, where S=(A,B) is the two-bit syndrome-plane coordinate. The old relaxation has four separate eleven-variable Shannon branches:

- (Y1,...,Y10,S);
- (Y1,...,Y10,A);
- (Y1,...,Y10,B);
- (Y1,...,Y10,A+B).

They share the original Y-subset coordinates. Its additional rows are:

- each auxiliary is determined by Y_V;
- the original graph FDs;
- functional visibility at neighborhoods and selected triangles, full-state visibility where two different functionals are visible, and the actual-component local FDs given S;
- H(Y_U,l) <= H(Y_U,S);
- H(Y_U,S) <= H(Y_U,l)+H(Y_U,m)-H(Y_U) for distinct nonzero functionals l,m;
- ONLY the full-state gate

  3H(Y_V)+17H(S)-2 sum_v H(Y_v,S) <= 0.

The exact row definitions are in the independent v1 semantic checker `frontier-20261028-plane-functional-check.py`, SHA-256 `0d2f99580d9f939a6f6f4dba1e36b93ec84b9f111f92818571cdefd25ac931c3`. It deliberately rejects a gate on an individual functional. There are no inequalities using a numerical cap on H(S).

For actual selected-component laws, the fixed-state gate and the fixed-factor lifting have the written conditional tensorization proof in `frontier-20261028-triangle-code-global-obstruction-v1.md` (SHA-256 `bdf79fd631e8e58a734a4ef4c93f899e319f45712a219a876f527b52f1d61bb4`) and `frontier-20261028-syndrome-cover-entropy-gate-v1.md` (SHA-256 `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b`); the mixed-block application is stated in `frontier-20261028-mixed-visibility-theorem-v1.md`. Their scientific review boundaries remain. The finite algebraic classification itself needs only the literal row system.

## 3. The 495 exclusion identities

The disjoint certificate bundles are:

- `frontier-20261029-plane-functional-certs-part2.json`: 197 certificates;
- `frontier-20261029-plane-functional-certs-part3.json`: 295 certificates;
- `frontier-20261029-plane-functional-direct-recovered-certs-v1.json`: 3 certificates, classes 48, 366, 382.

The last three were recovered by solving the signed dual identity directly with an L1 objective (`frontier-20261029-plane-functional-direct-dual-v1.py`, SHA-256 `c556be1bf30d6b408182831d59df95bee6b800d6d12447af1c1af25e8633ac90`), rather than optimizing a degenerate homogeneous primal cone. Every proposed support was reconstructed over Q and then independently checked. The independent checker verifies row validity, action/color compatibility, coefficient signs and all raw coefficients of the identity for 3*Delta. Its changed-target negative control is rejected.

These identities remain conditional on the row premises when applied to actual laws; the algebraic identities are exact.

## 4. The other twenty classes are a real relaxation boundary, not just timeouts

The class indices are

`65,72,150,157,225,247,335,336,353,354,355,359,363,493,494,495,496,497,498,499`.

Normalize sum_v H(Y_v)=1. Exact feasible profiles have:

- Delta = 1/174 in eighteen classes;
- Delta = 1/228 in classes 493 and 494.

These are feasible witness values, not claimed exact maxima. Since every allowed row holds but Delta is positive, no conic combination of just this row family proves Delta<=0 in these classes.

**Profiles.** `frontier-20261029-plane-functional-v1-countermodels-all20.jsonl`, SHA-256 `142149de036a3adba99d9c88533ec80c8301d10074ee6b39e8421214bfb66b28`.

**Corrected independent checker.** `frontier-20261029-plane-functional-primal-check-v2.py`, SHA-256 `00092f5252bef63638c215cb596e6727a37bd31823d7759b96603739908ebd81`. It expands each profile and checks about 118,000 full rows per case, plus normalization and positive gap, with Python integers. It asserts the expected full row count. Its receipt is `frontier-20261029-plane-functional-v1-countermodels-all20-check.json`, bound in the master receipt. Changed-joint and changed-normalization controls are rejected.

Two failed numerical grid proposals were replaced by exact raw-profile transfers: 335 to 336 and 353 to 354. Every target row was checked independently; no monotonicity shortcut was assumed. Provenance is `frontier-20261029-plane-functional-v1-countermodel-transfers-v1.json`.

## 5. Even the complete joint Shannon system admits these profiles

Introduce three explicit auxiliary variables L0=A, L1=B, L2=A+B. Complete the old profile by assigning an entropy of (Y_U,T) as:

- the original branch if T is empty;
- the appropriate functional branch if T is a singleton;
- the full-state branch if T contains two or three auxiliaries.

For every one of the twenty profiles, this assignment satisfies all 159,757 elemental inequalities of a thirteen-variable Shannon polymatroid, all 3,072 pair-determination equalities over original subsets, and auxiliary determination by Y_V.

**Independent joint check.** `frontier-20261029-functional-joint-completion-check-v1.py`, SHA-256 `9b7d81b804fea77c0769723d83236ab141d225fc009e0053ca567394ac004f57`; receipt `frontier-20261029-functional-joint-completions-all20-check.json`, SHA-256 `3259785f6fa83bceb2ec322526cc3bb38caf57494cfbd82e39516a141dcdc506`. Across the twenty cases it checks 3,195,140 elemental rows and 61,440 circuit equalities. A changed joint entropy is rejected.

Thus simply adding the missing joint Shannon CMIs cannot eliminate these particular profiles. They still are NOT entropic or coding witnesses: exact conditional Zhang-Yeung/DFZ rows separate the two representative gap types, and a separate non-Shannon cutting-plane route is in progress.

## Limits

This completes the finite relaxation classification and gives an explicit stronger Shannon-method obstruction. It leaves the twenty actual entropy-law classes open. It neither improves the unrestricted lower bound nor changes the independently checked but unreviewed upper-bound candidate 2603/389. The paused source-order episode and all held reviews remain outside this result.
