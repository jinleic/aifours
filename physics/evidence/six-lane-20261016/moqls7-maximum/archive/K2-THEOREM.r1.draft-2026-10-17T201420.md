# Candidate K2 exclusion: no 3-MOQLS(7) set has exactly two non-classical squares

Status: producer proof package complete; awaiting parent mathematical review, independent classification/proof
replay, and hostile CLI reviews. This is a partial result for determining M(7). K3 remains unresolved, and nothing
in this note claims M(7) = 2 or 3. No novelty or priority claim is made.

## 1. Exact case and reduction
K2 means a mutually orthogonal triple {Psi1, Psi2, L} of QLS(7), with Psi1 and Psi2 non-classical and L classical.
It does **not** mean a pair of non-classical MOQLS(7); published non-classical pairs are genuine controls here.

Choose the classical basis of L. Its symbol labels define a Latin square, and (C1) says that orthogonality to L is
exactly the ONB condition on its symbol lines. Thus each Psi_a is an ONB-assignment on the 3-net of rows, columns
and L symbol lines. The mutual tensor-ONB condition for Psi1 and Psi2 is unchanged under any permutation of the 49
points. Consequently paratopy of the 3-net preserves the entire case; a main-class representative of L suffices.

**Heavy in every basis.** Assume Theorem K1 from `K1-THEOREM.r2.md`. If either non-classical square Psi is light in
any ONB B (all its entries have weight at most two in B), rotate Psi alone to express B as the standard basis.
Global unitaries preserve all of its inner products, and hence every orthogonality to the other squares. The
printed proof of Ball–Simoens Lemma 10 (source LF178–192) replaces this light square by a classical one while
preserving **all** zero inner products. Undo the basis rotation. The other non-classical square is untouched, so
this yields a K1 triple, a contradiction. Therefore both Psi1 and Psi2 are heavy in every ONB, including each of
their 21 own line bases. This is derived for the present three-square problem; no four-square forced-weight claim
is imported.

## 2. Finite necessary representation
For every pair of distinct cells p,q, let g_a(p,q) be true exactly when <psi_a,p, psi_a,q> is nonzero. These are
symmetric predicates. The five conditions and proofs are frozen in `GRAM-ENCODING.r1.md`:

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

This equals the published total of reduced Latin squares of order seven. The producer completeness argument uses
that count and the exact canonicalisation/stabilizer calculation; it is not itself a fresh full enumeration of all
16942080 reduced squares. Independent parent coverage is a separate acceptance requirement.

## 4. Two encodings and 294 checked proofs
The base encoders are unchanged from their frozen review snapshot:

- A: `code/gram_enc.py`, SHA-256
  `b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833`.
  Direct AND auxiliaries and 0/1-common-support clauses, direct transition-pattern clauses, guarded cardinality
  clauses. CaDiCaL 3.0.1 supplies binary DRAT proofs.
- B: `code/gram_encB.py`, SHA-256
  `c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45`.
  Separately written stdlib implementation with sequential >=1/>=2 counters and a one-directional >=3 counter.
  kissat 4.0.4 supplies binary DRAT proofs.

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
Its local controls accepted a contradictory unit CNF with an empty-clause proof and rejected a satisfiable unit CNF
with an empty-clause proof. These are checker controls, not mutation tests of both encoders.

Frozen-code encoder controls (exact Gram supports, not numerical inner products):
- A: `evidence/gram/gram_controlsA_frozen.json`, SHA-256
  `a876bea8928d2ea6c62cd61b94d51dbd4c67670f8b779a17c49bb825c0049173`.
  Classical triple SAT; genuine non-classical pair (Psi(f),Phi(m)) SAT; Psi(f) on its 3-net heavy SAT and no-heavy
  SAT. Of 40 tested single-predicate mutations, 6 were rejected; these are only necessary conditions.
- B: `evidence/gram/gram_controlsB_frozen.json`, SHA-256
  `6c15ef284c96e2a3b1cb880d1fa4b9ca2aae7d4e76999784616641eb1531a669`.
  Classical triple SAT; genuine pair SAT; Psi(f) on its 3-net heavy SAT; classical K2-shaped data without heavy SAT.
  No mutation-count claim is made for B.

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
