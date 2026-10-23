# Gram-support encoding for K2 and K3 (lane moqls7-maximum): soundness

Status: corrected proof source after both static ACCEPT-WITH-FIXES reviews; parent integration/theorem verdict is
separate. The definitions are those of Ball–Simoens arXiv:2607.12933v2 §2.2–2.4. Entries are unit vectors taken up
to phase. The corrected K1 argument is `K1-THEOREM.r3.md`; `LEMMAS.md` supplies the previously missing references.
This file did not exist in the original review snapshot. The original frozen r1 bytes remain unchanged.

**Pinned code:**
- `code/gram_enc.py` (encoder A): b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833
- `code/gram_encB.py` (encoder B): c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45
- `code/gram_certify_r4.py` (actual K2 production driver): ec540a8700b7933b71605e7b03f86d5ef52ad258a5895d0b558db9819f0fa18a
- `code/ls_classes.c`: 968ad4e574ed02800ac9f391aeb67e7709d328563112c0fe4febe30596058794
- The unbounded `gram_certify.py` in the old review snapshot was not used for production. Driver-only deltas r2,
  r3 and r4 record its replacement; every retained K2 certificate binds the actual r4 driver and frozen encoders.
- Future K3 certification uses the separately controlled `proof_stream.py` aa0d5a0b…05de and
  `k3_cube_certify_r2.py` 49677766…8211, under `K3-CERTIFICATION-DRIVER-DELTA.r2.json`.

Encoder correspondence with §2:
- Both encoders create g variables only for pairs not on a common line, so G1 holds by absence.
- G2: A uses AND-auxiliaries h = g(p,r)∧g(q,r) with direct 0/1-count clauses. B uses a sequential counter that
  gives "≥ 1" and "≥ 2".
- G3 over ordered pairs of lines: A uses direct clauses; B uses counters.
- G5 is pairwise exclusion in both.
- G4: A uses "every (n−2)-subset contains a true literal" guards; B uses a one-directional ≥ 3 counter.
- `--sym` is identical in both; scientific production uses it only for K3, with L absent. Matched one-square
  controls also exercise this branch. The frozen code comments referring to K1 section 8 are dependency-reference
  errors: G4 uses Theorem K1 plus the independent minimality argument below, not that standard-frame reduction.

## 1. Objects
Let S be a set of mutually orthogonal QLS(7). For all cells p,q define
G_a(p,q) = ⟨ψ_a,p, ψ_a,q⟩, conjugate-linear in the first argument. Unit norms give G_a(p,p)=1, and
G_a(q,p)=conj(G_a(p,q)). For distinct cells the Boolean support g_a(p,q)=[G_a(p,q) != 0] is therefore symmetric and
does not depend on phases or a global unitary. Diagonal Gram entries are one, not false Boolean predicates; the
encoders never represent them as off-diagonal variables. The ONB lines of each quantum square are:
- its 7 rows and 7 columns (QLS axioms);
- in K2, the 7 symbol lines of the classical square L. By (C1), Ψ_a ⊥ L iff Ψ_a is an ONB on each symbol line of L.

## 2. Necessary conditions (each holds for every quantum square a)
- **G1.** If p ≠ q lie on a common ONB line, then g_a(p,q) = 0.
- **G2 (frame consistency).** Let ℓ be an ONB line and p, q ∉ ℓ. Then ψ_p = Σ_{r∈ℓ} G(r,p) ψ_r, so
  G(p,q) = Σ_{r∈ℓ} conj(G(r,p)) G(r,q). Hence #{r ∈ ℓ : g(p,r) ∧ g(q,r)} = 0 forces g(p,q) = 0, and = 1 forces
  g(p,q) = 1. When p and q are collinear, G1 then forbids the count 1.
- **G3 (unitary transitions).** For ONB lines ℓ1 ≠ ℓ2, the matrix U[r,q] = G(r,q) (r ∈ ℓ1, q ∈ ℓ2) is the product
  of two unitaries. If the lines meet in s, then U[s,s] = 1 and the 6 × 6 block on (ℓ1∖s) × (ℓ2∖s) is unitary.
  Hence:
  - every r ∈ ℓ1∖ℓ2 has a neighbour on ℓ2∖ℓ1;
  - if r has exactly one neighbour q there, then |U[r,q]| = 1, so q has no other neighbour on ℓ1∖ℓ2.
- **G5 (orthogonality, exact).**
  - For quantum squares a ≠ b: ⟨ψ_a,p ⊗ ψ_b,p, ψ_a,q ⊗ ψ_b,q⟩ = G_a(p,q)·G_b(p,q). So Ψ_a ⊥ Ψ_b iff
    g_a(p,q)·g_b(p,q) = 0 for all p ≠ q.
  - Orthogonality to a classical L is exactly G1 on L's symbol lines.
- **G4 (heavy).** In a non-classical 3-set S that minimises the number m of non-classical squares, every
  non-classical square Ψ is heavy in every ONB B: some entry has ≥ 3 nonzero coefficients in B.
  - *Proof.* Theorem K1 gives m ≥ 2. Suppose Ψ is light in B, i.e. every entry has ≤ 2 nonzero coefficients.
    Apply a global unitary V with V(B) = standard basis. Lemma 10 (Ball–Simoens LF178–192) then gives a classical
    Ψ'' that is orthogonal to every square orthogonal to VΨ. Orthogonality of Ψ to the other squares is invariant
    under ψ ↦ Vψ applied to all entries of Ψ alone. So V⁻¹Ψ'' is classical and orthogonal to the other two squares.
    The resulting 3-set has m − 1 ≥ 1 non-classical squares, which contradicts minimality. ∎
  - With B the ONB of an own line ℓ: the weight of p ∉ ℓ is #{r ∈ ℓ : g(p,r)}. So *every own ONB line ℓ has a
    point p ∉ ℓ with ≥ 3 neighbours on ℓ.*
  - When K1 is impossible, any K2 set already has minimal m = 2. When K1 and K2 are both impossible, any K3 set has
    minimal m = 3. G4 therefore applies to every K2 set and to every K3 set that survives.
  - The minimisation is over all non-classical triples, not over one preselected representation. It exists
    because m belongs to {1,2,3}; no compactness argument is needed. `LEMMAS.md` gives the simultaneous-partner
    preservation proof of Lemma 10. K1 section 8 is not used in this G4 argument.

## 3. Symmetry and the case split
- **K2.** All conditions are symmetric in the three classes (rows, columns, L lines) and invariant under relabelling
  of each class. A K2 configuration on L therefore transports to every L′ paratopic to L. One representative per
  main class suffices.
  - The 147 main classes are in `evidence/ls7_main_classes.txt`
    (898065c8a592a5a3ed1103a2657e3cff25f9588514ad3d286d441dedc95a8158).
  - Normalisation flags choose one of six ordered class roles, an origin and an ordering of the other six points
    of its row: 6*49*6! = 211680 flags. The ordered row forces column/symbol labels and the first column forces
    row labels. Every paratopy to a reduced square arises this way.
  - Autoparatopies act freely on flags: fixing the ordered roles and row points fixes every column/symbol line,
    hence every point. The flags giving any reduced output form a free group orbit. Their multiplicity is |Par|,
    and each class therefore has 211680/|Par| reduced squares. The least key is a complete main-class invariant.
  - Egan–Wanless Theorem 3.2 (pinned layout LF382–397) gives this factor at n=7,k=1. Table 6 LF754 gives 16942080
    reduced squares and 147 paratopy/main classes; this is not the maximal-one-MOLS table of bachelor squares.
    Source binding: `K2-CLASSIFICATION-SOURCE.r1.json`.
  - The independent parent `institute/runs/six-lane-2026-10-16/review/moqls7-ls147-parent-v1/REPORT.md`
    records technical PASS: all representatives validated,
    147 distinct canonical keys; all multiplicities/group orders matched by two separately authored routes;
    the explicit union has 16942080 keys and zero cross-class duplicates. It reuses, rather than reruns, the
    parent's full reduced-Latin count. This supplies the source-independent computation missing from the
    producer's original BFS log; it is not itself a theorem verdict.
- **K3.** Row and column permutations, transposition and relabelling of the squares preserve every condition.
  - WLOG (`--sym`) square 1 is heavy in the frame of row 0 at point (1,0), with neighbours (0,1), (0,2), (0,3).
  - Justification: permute rows so that the frame row is 0 and the heavy point's row is 1. Permute columns so that
    the heavy point's column is 0 and three of its neighbours lie in columns 1, 2, 3. A neighbour cannot be in
    column 0, because (0,0) and (1,0) are collinear.

## 4. Controls (genuine data, exact Gram supports)
For a prime p, a sum of p p-th roots of unity vanishes iff each root occurs once. So the Ψ(f) Gram support is exact:
g(p,q) = 1 iff x ↦ (k−i)f(x) + (l−j)x is not a permutation.

| control | encoder A (`explore/gram/gram_controls_v1.json`) | encoder B (`explore/gram/gram_controlsB_v1.json`) |
|---|---|---|
| classical triple aI + J, 3 squares, no heavy | SAT | SAT |
| genuine non-classical pair (Ψ(f), Φ(m)), Ex. 15, q = 7, H = {1,2,4}, f shifted | SAT | SAT |
| Ψ(f) alone on its 3-net (net-L = Φ(m)), heavy | SAT | SAT |
| classical K2-shaped data (net-L = L1, squares L2, L3), no heavy | — | SAT |
| single-bit mutations of Ψ(f)'s support (40) | 6 rejected (the conditions are necessary only) | — |

The old 40-mutation split exercises G5 alone in its six rejected additions; the 34 deletions passed. It is not
evidence that G2–G4 are non-vacuous. The original frozen-code rerun before K2 production is retained under
`evidence/gram/gram_controls{A,B}_frozen.json`. A later, explicitly chronological review remediation added 26
matched cases on the **unchanged** encoders (13 fixtures each), with complete inputs, CNFs, solver logs and SHA
receipts in `evidence/gram/review_controls_r1/`:

- Psi(f), heavy plus sym: SAT in both. Swapping columns 1/4 removes one required edge: UNSAT with sym and SAT
  without sym, under heavy in both cases.
- Classical one-square data: SAT without heavy, UNSAT with heavy.
- Classical K2-shaped data: SAT without heavy, UNSAT with heavy; this includes encoder A's missing positive.
- Classical triple with heavy plus sym: UNSAT.
- Exact transport of Psi(f) to the decoded Z7 representative, then through a conjugate: heavy SAT in both.
- Designed G2-one/G3-singleton, G3-empty and G5-edge-conflict mutants: UNSAT in both, with an independently
  evaluated intended-family violation for each. Some mutants violate more than one family; no exclusivity is
  claimed.

All 26 expected outcomes occurred. Summary SHA-256:
6ce1ddc241a88da9f0d2fdc0be3551b8a73f5659a979c5034ebcee5caaecd685.
These controls occurred **after** the K2 producer certificates, not before them; they precede new K3 certification.
No positive K2/K3 witness is presumed. The small-order QLS4 control belongs to the separate pattern evaluator and
is not matched to these hard-coded order-seven CNF encoders.

## 5. Results and acceptance boundary
- K2 exploratory screens: both encoders returned UNSAT on all 147 two-heavy-square class instances.
- K2 production: all 147 A and all 147 B regenerated CNFs received checked binary DRAT proofs. Every receipt has
  solver rc20, checker rc0, exact `s VERIFIED` and no safety stop. Inventories:
  - `evidence/gram/k2A_cert_summary_r4.json`: 31aa7eb25bfb760c3b71af21698612ffc6ee8c877f0507d2dd7d3cfa462ddc29.
  - `evidence/gram/k2B_cert_summary_r4.json`: ed29e3a199a650f11a10f98d0c262c5ebe4c905e68ce6de18adeee030fa20f4b.
  - `K2-THEOREM.r1.md` states the candidate theorem and original evidence trust boundary; independent parent proof
    replay and final integration remain separate.
- K3 original heavy+sym chunk was UNKNOWN at 3600 seconds. Under the separately frozen three-cube representation,
  A/C311 is UNKNOWN, A/C321 and A/C411 are UNSAT exploratory. The last two are not exclusions until certified;
  no exact value of M(7) follows yet. Further cube/lex lemmas are separate reviewed deltas, not silently part of
  the original G1–G5 snapshot.

## 6. Valid production domain and frozen latent branches
Every production L is a validated Latin square of order seven; K3 has L absent, and sym is never combined with
a net. On a 3-net frame line an off-line point has five structurally possible neighbours; on a 2-net frame it
has six. Two such allowed sets intersect in at least three or five points respectively. Thus encoder B's
malformed one-item/collinear G2 branch is unreachable in these production inputs, as are zero-candidate transition
or heavy branches. All 26 new matched-control CNFs are explicitly checked to contain neither `None` nor an empty
clause, with consistent DIMACS clause counts.

The frozen B CLI's permissive malformed `fix-json` behaviour is not advertised as a general validated API; the
new control harness independently validates all fixed G1 pairs and Latin/net/sym prerequisites. These historical
encoder bytes are preserved for exact proof binding, rather than silently rewritten after certification. Their
unreachable malformed-call branches do not enter the finite instances claimed here.

## 7. Transport controls and bounded lifecycle
The actual K2 r4 pipeline had native limits, complete direct-to-file logs, code/classfile/CNF/log hashes, strict
return-code and exact-status checks, and direct libproc RSS/floor monitoring. Its remaining named-FIFO startup
failure paths are addressed prospectively, not retrospectively erased, by the new controlled transport.

`proof_stream.py` uses nonblocking parent FIFO endpoints, checker blocking stdin with explicit binary `-i`, and a
keepalive writer closed when the native solver exits. This avoids parent startup blocking and delivers EOF even
if the solver never opens its proof path. Early checker exit causes bounded cooperative shutdown of the writer.
No output pipe can backpressure; SAT models remain in full solver logs. Absolute solver path and binary hash are
bound at spawn time. Timestamped pipeline checkpoints persist every 15 minutes.

New end-to-end controls in `evidence/gram/transport_controls_r2/summary.json`
(34a69ae60c1f09bc4029ae9bb589b581d45204e68146af6dc4f5d54be6fd95e6) observed:
both real native UNSAT streams verified; both SAT models retained and directly checked while UNSAT acceptance
failed; binary empty-clause proof on SAT rejected; an intentional prematurely exiting writer rejected without a
hang. These test transport/checker behaviour, not a quantum theorem. The earlier rejected `/dev/fd` attempt and
all r2/r3 failed starts remain retained and are not accepted certificates.
