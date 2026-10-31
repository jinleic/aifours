# Candidate: the four remaining N48/t24 residual profiles are impossible (six-word sweep)

Owner **PhysicsAME46-2**. Native clock observed before writing: `Thu Oct 29 12:27:55 PDT 2026` (not an exact completion time). **WRITTEN reduction plus exact-CNF certificates**, not independently reviewed, adopted, formally verified or novelty-cleared. No held material is used.

## 1. Claim and dependencies

A normalized complex AME(4,6) state with `N=48` and exactly `t=24` maximal coefficients cannot have residual alphabet profile 3555, 4455, 4555 or 5555.

Dependencies, all separately written and **unreviewed**:

- the exact-scope N48/t24 no-Hamming-one candidate `frontier-20261029-n48-t24-noh1-and-six-alphabets-v1.md`, SHA-256 `6bbe85a8b1bec38ef5984d32408c52479ec58edeb3502398d87ab1f7e04a7c96`, which carries the classical no-OLS(6) import;
- the six-word lemma `frontier-20261029-zero-excess-six-word-lemma-v1.md`, SHA-256 `3e8e5a4fc9fbc58b5b6e0a3c6a16bc246fdccd78b2bbbcf6f9e1014b26172f07` (three row-orthogonality equations, no import);
- elementary zero-excess structure (§2), reproved here.

The finite part is the certificate set in §4. Nothing here excludes the other five profiles; those are the separate written candidates listed in the N48 composition packet.

## 2. Zero-excess facts encoded

For t=24, n=12 and |E|=24=2n (zero excess). In each cut every E row and column has exactly two nonzeros, so:

- **(Z1)** every E pair value of every pair system has exactly two extensions, and no value has exactly one;
- **(Z2)** a local E symbol a at party i with partner degree d_i(a) (the number of E pair values (a,y) in any system containing i; it is j-independent because the six values (a,y) split into 6−d P-carried and d E-carried ones) has |E_a|=2d_i(a); d_i(a)>=2, Σ_a d_i(a)=12 and d_i(a)<=min_{j≠i} r_j;
- **(Z3)** every E support component of every cut is a full2x2 block: a component is a cycle in the bipartite support graph; neighbouring rows of a longer cycle share exactly one column and cannot be orthogonal. Equivalently, if (r,c),(r,d),(t,c) are in E with r≠t, c≠d, then (t,d) is in E;
- **(Z4)** conditional no-Hamming-one: no two E words differ in exactly one coordinate;
- **(Z5)** the six-word lemma: no binary sub-grid contains a parity class minus an antipodal pair inside E.

With sizes ascending (party permutation) and E symbols relabeled 0..r_i−1 in ascending degree inside each party, every case is an ordered choice of sorted degree vectors with entries in [2,min_{j≠i} r_j] summing to12. For 3555 the size-3 party has (2,5,5),(3,4,5) or (4,4,4) and every size-5 party (2,2,2,3,3); for 4455 the size-4 parties have (2,2,4,4),(2,3,3,4),(3,3,3,3) and the size-5 parties (2,2,2,2,4) or (2,2,2,3,3); for 4555 the size-4 party also allows (2,2,3,5); for 5555 each party has (2,2,2,2,4) or (2,2,2,3,3). That gives 3+36+32+16=87 cases. The manifest regenerates this list independently and checks equality.

## 3. Encoding

`frontier-20261029-n48-t24-six-word-cnf-v1.py`, SHA-256 `26805ed074a14ab011d335be65c91fe1ffbfc22c55de7eba5bacf7b78dcda2bc`, with flags `--no-H1 --six`, E variables only. Clauses: exact fiber sizes 2d (Z2); per pair value at most two and never exactly one (Z1); the closure clause of (Z3) for all ordered r≠t, c≠d in all three cuts; at-most-one per line through any three fixed coordinates (Z4); one negative six-literal clause per six-set of (Z5), namely 8·Π C(r_i,2): 24000 (3555), 28800 (4455), 48000 (4555), 80000 (5555) per formula, as recorded in each `.cnf.meta.json`. No phases, moduli or P code are encoded.

## 4. Certificates

All87 formulas are UNSAT by CaDiCaL 3.0.1 `--plain --lrat --no-binary`, and every textual LRAT proof was checked through EOF by the separate RUP checker `frontier-20261029-lrat-rup-check-v2.py` (SHA-256 `d04eb821104b12bfddfb3d6e9a6f7a03b4f97ae65247959de6eddaa39ab99366`). The full per-case list (CNF, LRAT and receipt SHA-256, all re-hashed from disk) is `frontier-20261029-n48-t24-six-word-sweep-manifest-v1.json`, SHA-256 `c3d0a0876cb8dd014d559b10489bac8fa64641543d285b5e898e129864163087`. Batch receipts: `sat-20261029/six-cert/batch-3555-v1.json` SHA-256 `35225c1a7a7bbe50d3931758d30ca3ebadb7f384c34726e81914ce655836f7f7`, `sat-20261029/six-cert/batch-4455-v1.json` SHA-256 `d3afe01d722b76c3fcdd560de44b7d4714c78d834f564c29cd315b6cddfd7f88`, `sat-20261029/six-cert/batch-4555-v1.json` SHA-256 `5a33ba605994dfb518fa92ca7fdbf550e1020900f67521fd8363981cfd7993d5`, `sat-20261029/six-cert/batch-5555-v1.json` SHA-256 `3ad6eeeb083aa02b99928efb53d3c9f1254468216205c369346efcbd57e66358`. Driver `frontier-20261029-n48-t24-six-word-batch-v1.py`, SHA-256 `9fd141aa23cc57a03d7717f26b7ee13554f026ba9848de4cffe2d939ef712c86`.

## 5. Controls and what is load-bearing

- With the same flags, the24 permutation words of {0,1,2,3} (profile4444, degrees3333) satisfy the CNF (SAT with all E units fixed). So (Z4)+(Z5) do not exclude every residual. That residual has fourth-root phases with all active residual Gram entries exact (`frontier-20261029-fourth-root-positive-control-v1.json`); the separate written 4444 packet rejects it through its no-OLS(6) step, not through phases.
- Without (Z4) the3555 (3,4,5) formula is SAT; its model fails phases through a degenerate three-block obstruction with distance-one words. So the no-Hamming-one dependency is genuinely used.
- Six-word generator equality and exact rectangle/kernel checks: `frontier-20261029-six-word-lemma-controls-v1.json`, SHA-256 `3f8e43f6f0ae7b8d14c0cc3b097a22721b2196be2f60090353399afcf0c630a3`.

## 6. Scope

UNSAT certificates prove only that the exact CNFs have no models. Independent review must re-derive (Z1)–(Z5), the case list and relabeling conventions, and audit the encoder. No witness, global bound, formal proof or novelty claim is made here.
