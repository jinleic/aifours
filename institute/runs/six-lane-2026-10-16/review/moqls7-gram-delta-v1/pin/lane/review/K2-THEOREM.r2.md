# Candidate K2 exclusion: no 3-MOQLS(7) set has exactly two non-classical squares

Status: producer proof package complete; both static Gram reviews found no fatal mathematical error and the
independent parent LS147 technical checks PASS. Final parent bridge/proof-replay/integration verdict remains
separate. This is a partial result: K3 is unresolved and no exact M(7), novelty or priority claim is made.

## 1. Exact case and reduction
K2 means a mutually orthogonal triple {Psi1, Psi2, L} of QLS(7), with Psi1 and Psi2 non-classical and L classical.
It does **not** mean a pair of non-classical MOQLS(7); published non-classical pairs are genuine controls here.

Choose the classical basis of L. Its symbol labels define a Latin square, and (C1) says that orthogonality to L is
exactly the ONB condition on its symbol lines. Thus each Psi_a is an ONB-assignment on the 3-net of rows, columns
and L symbol lines. The mutual tensor-ONB condition for Psi1 and Psi2 is unchanged under any permutation of the 49
points. Consequently paratopy of the 3-net preserves the entire case; a main-class representative of L suffices.

**Heavy in every basis.** Assume Theorem K1 from `K1-THEOREM.r3.md`. If either non-classical square Psi is light in
any ONB B (all its entries have weight at most two in B), rotate Psi alone to express B as the standard basis.
Global unitaries preserve all of its inner products, and hence every orthogonality to the other squares. The
printed proof of Ball–Simoens Lemma 10 (source LF178–192) replaces this light square by a classical one while
preserving **all** zero inner products. Undo the basis rotation. The other non-classical square is untouched, so
this yields a K1 triple, a contradiction. Therefore both Psi1 and Psi2 are heavy in every ONB, including each of
their 21 own line bases. This is derived for the present three-square problem; no four-square forced-weight claim
is imported.

## 2. Finite necessary representation
For every pair of distinct cells p,q, let g_a(p,q) be true exactly when <psi_a,p, psi_a,q> is nonzero. These are
symmetric predicates. The five conditions and corrected proofs are frozen in `GRAM-ENCODING.r2.md`; diagonal
Gram entries are one, the inner product is conjugate-linear in its first argument, and off-diagonal support is
symmetric. G4 here is the independent minimality argument, not the standard-frame reduction of K1 section 8.

- G1: cells on a common ONB line are orthogonal (their predicates are false).
- G2: expand both vectors in any ONB line. Zero common support coordinates force g(p,q)=0; exactly one forces
  g(p,q)=1. This condition is imposed in every line frame, not just row 0.
- G3: transition matrices between ONB lines are unitary; each point off the other line has a neighbour there, and
  a unique neighbour forces the reverse transition to be unique as well.
- G4: on every own ONB line, some off-line point has at least three neighbours (the preceding heavy lemma).
- G5: tensor orthogonality is exactly edge-disjointness: for p != q the product of the two Gram entries vanishes,
  so g_1(p,q) and g_2(p,q) cannot both be true.

Any K2 configuration induces a Boolean model of these conditions for its 3-net. Therefore a certified UNSAT of the
necessary conditions excludes that net, with no real/complex-field restriction or numerical tolerance.

## 3. Classification input and its trust boundary
`evidence/ls7_main_classes.txt` SHA-256
`898065c8a592a5a3ed1103a2657e3cff25f9588514ad3d286d441dedc95a8158`
contains 147 explicit reduced Latin squares, encoded by the 36 off-first-row/off-first-column entries. Their first
row and column are 0,...,6. The class-generation source is `code/ls_classes.c` SHA-256
`968ad4e574ed02800ac9f391aeb67e7709d328563112c0fe4febe30596058794`.

For each candidate square its canonical key is the minimum over 6*49*720 = 211680 normalisations. The multiplicity
of that minimum is |Par(L)|. The keys are distinct, and the class-size sum is

    sum_L 211680/|Par(L)| = 16942080.

This equals Egan–Wanless Table 6, pinned layout LF754; Theorem 3.2 LF382–397 supplies the factor at n=7,k=1.
`K2-CLASSIFICATION-SOURCE.r1.json` binds the pinned text and formulas. The producer's argument used this count and
its canonicalisation/stabilizer calculation, not a fresh full enumeration.

Independent parent evidence now supplements that trust base:
`institute/runs/six-lane-2026-10-16/review/moqls7-ls147-parent-v1/REPORT.md` records technical PASS for every
representative, canonical key, multiplicity and explicit autoparatopy group. Its independent union has exactly
16942080 reduced keys and zero cross-class duplicates; the separately completed parent full Latin count is
reused, not rerun. This closes the producer computation/provenance gap without claiming a parent theorem verdict.

## 4. Two encodings and 294 checked proofs
The base encoders are unchanged from their frozen review snapshot:

- A: `code/gram_enc.py`, SHA-256
  `b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833`.
  Direct AND auxiliaries and 0/1-common-support clauses, direct transition-pattern clauses, guarded cardinality
  clauses. The producer invokes `cadical` to supply binary DRAT proofs.
- B: `code/gram_encB.py`, SHA-256
  `c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45`.
  Separately written stdlib implementation with sequential >=1/>=2 counters and a one-directional >=3 counter.
  The producer invokes `kissat` to supply binary DRAT proofs. The original r4 receipts name these commands but do
  not bind run-time solver versions/binaries; no particular solver version is a soundness premise once the
  intended CNF's proof is checked. New prospective transport records also bind the executable at spawn time.

For each of the 147 representatives the producer regenerated the two-square, fixed-L, heavy CNF and streamed its
proof to the lane drat-trim. Every instance returned solver rc 20, checker rc 0 and exact `s VERIFIED`, with no
safety stop. The inventories cover indices 0 through 146 without omission:

| route | verified instances | native pipeline time, excluding CNF generation | maximum sampled aggregate RSS |
|---|---:|---:|---:|
| A / CaDiCaL / drat-trim | 147 | 316.508 s | 496599040 bytes |
| B / kissat / drat-trim | 147 | 1863.771 s | 562118656 bytes |

- A inventory: `evidence/gram/k2A_cert_summary_r4.json`, SHA-256
  `31aa7eb25bfb760c3b71af21698612ffc6ee8c877f0507d2dd7d3cfa462ddc29`.
- B inventory: `evidence/gram/k2B_cert_summary_r4.json`, SHA-256
  `ed29e3a199a650f11a10f98d0c262c5ebe4c905e68ce6de18adeee030fa20f4b`.
- Per-instance exclusive receipts and full solver/checker logs: `evidence/gram/cert_r4/`.
- Inventory reader: `code/gram_cert_summary.py`. It checks all expected indices, exact result fields, common frozen
  code pins, and both log SHA bindings. This is an evidence inventory, not an independent proof implementation.

Proof bytes were consumed through a FIFO rather than retained. Each receipt binds the regenerated CNF SHA, both
encoders, classfile, driver and checker/source SHA, solver command, full log SHA values, clock interval and sampled
RSS. Replaying the pinned generator and solver/checker pipeline is required for an independent check.

## 5. Driver, controls and rejected runs
Production driver: `code/gram_certify_r4.py` SHA-256
`ec540a8700b7933b71605e7b03f86d5ef52ad258a5895d0b558db9819f0fa18a`.
It uses native solver/checker limits, direct libproc aggregate-RSS sampling (0.25-second period), cooperative
SIGTERM safety stops, and a 12e9-byte free-space floor. The two busy native processes are the solver and checker;
there was no overlapping exploratory solver. drat-trim reads binary stdin using `-i`, not named-proof detection.

The original checker source is unchanged: SHA-256
`d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee`.
Original producer checker-control stdout was not retained, so this note no longer treats those reported outcomes
as pinned receipts. The parent's separate K1 route-2 receipt
`506b466d0fef11578a06370dd7f94190fe72357fd81e1ad6425c2588b1189701` retains its own six controls with a
freshly built same-source checker. New producer binary-stream transport controls are retained under
`evidence/gram/transport_controls_r2/summary.json`
(`34a69ae60c1f09bc4029ae9bb589b581d45204e68146af6dc4f5d54be6fd95e6`): both native UNSAT streams verify; both
SAT models are retained/directly validated and not accepted as UNSAT; invalid binary empty-clause proof on SAT
is rejected; a premature writer exits safely. These are separate checker/transport controls, not encoder
mutation counts or retrospective preregistration.

Frozen-code encoder controls (exact Gram supports, not numerical inner products):
- A: `evidence/gram/gram_controlsA_frozen.json`, SHA-256
  `a876bea8928d2ea6c62cd61b94d51dbd4c67670f8b779a17c49bb825c0049173`.
  Classical triple SAT; genuine non-classical pair (Psi(f),Phi(m)) SAT; Psi(f) on its 3-net heavy SAT and no-heavy
  SAT. Of 40 tested single-predicate mutations, the six rejected additions exercise G5; all 34 deletions passed.
  This original suite is not evidence of G2–G4 non-vacuity.
- B: `evidence/gram/gram_controlsB_frozen.json`, SHA-256
  `6c15ef284c96e2a3b1cb880d1fa4b9ca2aae7d4e76999784616641eb1531a669`.
  Classical triple SAT; genuine pair SAT; Psi(f) on its 3-net heavy SAT; classical K2-shaped data without heavy SAT.
  No mutation-count claim is made for B.

After K2 production, the static reviews requested additional matched controls. They were run on the unchanged
encoder bytes and are explicitly chronological, not asserted to have preceded the K2 certificates:
`evidence/gram/review_controls_r1/summary.json`
(`6ce1ddc241a88da9f0d2fdc0be3551b8a73f5659a979c5034ebcee5caaecd685`) retains 26/26 expected outcomes,
13 per encoder. They cover heavy+sym positive, a missing-edge sym negative distinguished by sym-off SAT,
classical-light positives/heavy negatives, A's missing classical K2-shaped positive, production-shape negatives,
exact decoder transport and conjugation, and designed G2-one/G3-singleton, G3-empty and G5-conflict failures with
independent intended-family evaluations. Complete CNFs, fixed inputs and solver logs are retained and hashed.
All valid-domain CNFs in that suite have neither `None` literals nor empty clauses. The old frozen encoders'
malformed-call branches remain outside the validated closed production domain; see GRAM r2 section 6.

Two pre-production driver revisions failed and were not accepted: r2's Darwin preexec resource-limit call failed
before native startup; r3's named-proof FIFO auto-detection consumed prefix bytes and returned `s NOT VERIFIED`.
The failed outputs remain untouched in `evidence/gram/cert_r2/` and `cert_r3/`. Explicit driver-only deltas r2/r3/r4
record the transport fixes without changing either mathematical encoding.

## 6. Candidate conclusion and what remains
Under Theorem K1, the reviewed G1-G5 bridge and complete main-class coverage, the 294 verified UNSAT instances prove:

**No mutually orthogonal triple of QLS(7) has exactly two non-classical squares.**

This excludes K2 only. K3 remains a separate case. Any surviving K3 counterexample can be chosen heavy in every ONB
by the same minimal-counterexample argument after K1 and K2 are excluded. The original K3 Gram chunk returned
UNKNOWN, not UNSAT. Its next frozen representation is `AMENDMENT-2.r1.md` (three covering cubes and singleton
same-ray identities); its searches and certificates are not part of the present K2 proof.
