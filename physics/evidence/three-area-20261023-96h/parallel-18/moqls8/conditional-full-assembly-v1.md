# Problem16 n8 — full conditional rank-composition candidate v1

Actual clock observed immediately before this freeze: **2026-10-23T14:37:06-0700**. Author PhysicsMOQLS8, physics-4. Deadline remains the original October27 deadline.

**STATUS: CONDITIONAL FULL-TARGET CANDIDATE, NOT CLOSURE.** The purpose is to expose a complete implication chain for triage and actual reconstruction. New low-span/sector arguments are not yet independently or parent-accepted. Old exact-input/classification imports retain every stated limitation. Original A10 remains **UNSATISFIED** and A11 **UNSATISFIED/OPEN**. No GB UNKNOWN is converted to UNSAT, and no runtime HOLD is cleared.

## 1. Literal theorem under consideration

For EVERY five arrays Q_s:{0,...,7}^2->C^8 whose rows and columns are ONBs and whose pairwise product-cell arrays are ONBs of C^8 tensor C^8, all five squares are classical up to entry phases, common row/column permutations and a separate output unitary for each square.

This is exactly Ball–Simoens arXiv:2607.12933v2 Problem16 at n8. No real-only, support, finite-field, phase-alphabet, low-rank, preselected classical square, B2/B3 or fixed-nonclassical-count assumption is added to the primary theorem. The argument BELOW is conditional on the precise new/old statement imports in §2. It is not a claim that their acceptance gates are already discharged.

For each square let

    a_s=dim_R span{Q_s(x)Q_s(x)^*: all64cells x}.

This dimension is invariant under its output unitary, entry phases and cell permutations, and hence under every common row/column move and square relabelling used below. A square is classical iff a_s=8; every square has a_s>=8.

## 2. Exact statement dependencies and current gates

### New mathematical dependencies

- **RANK:** `proof-global-gram-defect-v1.md`, SHA256 `3b54a3e46ceb9ffa9edccab28664e13e322f5b47707fdffb77a51beba9a608d8`, with `proof-global-gram-defect-v1-erratum-1.md`, SHA256 `ef32720fe1b7c64a8539d6ae8cf5d94a0605e10a002aeb8483a5a2ac8eeb5d59`. Its TheoremT/corollary gives

      sum_s(a_s-8)<=14.                                   (R)

  Actual PhysicsRQLS10 reconstruction:0F/0M/1wordingMINOR, repaired by the numbered erratum. The full parent mathematical check remains separate; no formal/novelty acceptance.
- **LS:** `proof-low-span-rigidity-v1.md`, SHA256 `d64f57609450e2c6afbff5ddf3a6d768b1bb9c23d3159a8bf7a19604475380a6`. Its TheoremLS says that n<2(t+1) makes any nonclassical member of t MOQLS(n) have projector-span at least n+3. At n8,t5:

      Q_s nonclassical => a_s>=11.                        (L)

  Status AUTHOR CANDIDATE, actual separate/parent reconstruction outstanding. Both the overlapping-edge one-channel case and the no-weight2-in-ANY-line-frame case are load-bearing; do not silently assume disjoint two-block structure.
- **ISOLATE:** ONLY §§2–3 of `proof-isolated-sector-exclusion-v1.md`, SHA256 `34e5eca0a0d7ebac81b67c39cde758591513c79bf848d3bf9263c27126d1855d`. A globally isolated two-space using two distinct orthonormal ray-pairs in a t-MOQLS(n) family requires n>=2(t+1). At n8,t5 this is impossible.

  Status AUTHOR CANDIDATE, reconstruction outstanding. The harder later B3 span>=14 proof in that manuscript is **NOT needed in this assembly**. In particular a defect there would not automatically invalidate the simpler ISOLATE argument; the actual review must localize any finding.

### Old mathematical imports

Paths below are repository-root-relative. Full actual source bodies and current qualifications are routed by `assembly-imports-v1.json`.

- **K12:** `institute/runs/six-lane-2026-10-16/review/moqls8-k1k2-parent-verdict.md`, SHA256 `919daeac811bd551c4165ba415f9c6835b564adcb9bb6fcde1969307f2caa8f9`: no physical five-MOQLS8 family has exactly one or exactly two nonclassical members. It imports the stated classical MOLS classifications and recorded sound encodings/parent checks. This is old internally accepted computer-assisted/written evidence, not new credit, formal proof or fresh replay.
- **K3:** `institute/runs/six-lane-2026-10-16/review/moqls8-k3-parent-verdict.md`, SHA256 `6aff343d6182ec8936df73235efba6afea3dce1b7391efa3967eaf2e38b0217f`: no such family has exactly three nonclassical members. It imports the stated2165classical2-MOLS8net count, exact coverage/encoding bindings and recorded parent DRAT checks, with their compiler/checker/provenance boundary. Its literal consequence says that in every row/column standard form of a nonclassical five-set at least four squares have a weight3 entry. No fresh catalogue or certificate replay is supplied here.
- **LIGHT:** Ball–Simoens v2 Lemma10: a square with no entries of weight>=3 in a fixed ONB frame can be replaced by a classical square preserving orthogonality with EVERY other square. The operation shrinks supports and preserves all old zero inner products; it does not assert that the original square was classical. This is a printed theorem with proof, not a new method.
- **T16:** property-form normalization/cover accepted in `institute/runs/six-lane-2026-10-16/review/moqls8-unified-parent-disposition-v1.md`, SHA256 `29d17f380416045f73cd4e4b6923e55316bed8a62a45dd6310235cb239f8eaeb`, read with `N8_UNIFIED_ONE_P4_BRIDGE.r2.md` and `N8_UNIFIED_REVIEW_REPAIRS.r1.md`. It covers a physical five-set with the explicit standard row0 and SB2 witness hypotheses by ALL SIXTEEN templates, without requiring the other squares nonclassical or P4 on squares2–5. Only its admitted property-form scope is used. Old13case/c112/strong-F conclusions are NOT imported.
- **G:** GB canonical necessity/genuine representative implication, `institute/runs/six-lane-2026-10-16/review/moqls8-gb-necessity-genuine-nf-parent-verdict-v1.md`, SHA256 `f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c`, read with its actual GB necessity/NF/erratum sources. It applies to physical normalized configurations regardless of which other squares are classical. It does NOT transform arbitrary Boolean GB models and does not use GA proof bytes as GB evidence.
- **F14:** the exact fifteen qualified GB inputs listed in §3, coupled to G, exclude fourteen physical template classes. This import is conditional on their recorded soundness and exact qualification, NOT on an unqualified solver status or release label alone. Digested-but-unretained proof streams remain unretained; no certificate was replayed in this assignment.

### Gate state remains explicit

- Original **A10 ALL18 GB exact inputs: UNSATISFIED**, fifteen qualified and three UNKNOWN.
- Original **A11 final composition acceptance: UNSATISFIED/OPEN**. This new proposed mathematical route requires its own complete acceptance decision; it does not retroactively satisfy the old route.
- Shared T16/WMAN/NF/source-necessity imports are accepted only at their recorded conditional interfaces, not independently replaced by the new rank argument.
- All twelve historical runtime repair/qualification obligations remain incomplete/HOLD. No startup, solver, checker, replay or control authorization follows from this assembly.

## 3. Every one of the fourteen imported template exclusions

Use P=`institute/runs/six-lane-2026-10-18-96h/review/` and O=`institute/runs/six-lane-2026-10-16/review/`. The companion `assembly-imports-v1.json` contains each FULL formula SHA/byte identity, release SHA, audit SHA and raw-receipt SHA. All fifteen science-release bodies were actually read; their current file hashes were observed as metadata. Controls are not counted as exclusions. These are statement-level historical imports, not fresh proof replays.

| Physical template | Exact GB input(s) required and imported | Actual parent science release(s) |
|---|---|---|
|P0-B1|P0-B1 direct|P/moqls8-gb-staged-release-gbs6e-run-20261019T045025.json|
|P0-B2|P0-B2 direct|P/moqls8-gb-staged-release-gbs6e-run-20261019T050319.json|
|P0-B3|P0-B3 direct|P/moqls8-gb-staged-release-gbs6e-run-20261019T043836.json|
|P0-B4|P0-B4 direct|P/moqls8-gb-staged-release-gbs6e-run-20261019T032419.json|
|P0-B5|P0-B5 direct|P/moqls8-gb-staged-release-gbs6e-run-20261019T033511.json|
|P0-B6|P0-B6 direct|P/moqls8-gb-staged-release-gbs6e-run-20261019T042212.json|
|P1-B4|P1-B4 direct|O/moqls8-gb-staged-release-gbs5-run-20261018T134548.json|
|P1-B6|P1-B6 direct|P/moqls8-gb-staged-release-gbs6e-run-20261019T041303.json|
|P2-C1|P2-C1 direct|P/moqls8-gb-staged-release-gbs6e-run-20261019T053203.json|
|P2-C2|P2-C2 direct|P/moqls8-gb-staged-release-gbs6e-run-20261019T051909.json|
|P2-C3|P2-C3 direct|P/moqls8-gb-staged-release-gbs6e-run-20261019T034934.json|
|P2-C4|P2-C4 direct|P/moqls8-gb-staged-release-gbs6e-run-20261019T040528.json|
|P1-B1|P1-B1.M2 AND genuine representative implication G|P/moqls8-gb-staged-release-gbs7-run-20261019T061802.json|
|P1-B5|BOTH P1-B5.M2 and P1-B5.M3 AND G|P/moqls8-gb-staged-release-gbs7-run-20261019T100423.json AND ...T071308.json|

For B1 the representative set is{2}; for B5 it is{2,3}. A B5.M3 refutation alone did NOT exclude B5; the later M2 qualification is also required. B1/B5 are genuine-image exclusions, not direct Boolean-base GB refutations.

The fifteen exact inputs correspond to fourteen templates because B5 consumes two inputs. This leaves ONLY P1-B2 and P1-B3 in the genuine T16 cover. It does not mean their exact GB inputs have been refuted. In particular:

- B2.M2: UNKNOWN, solver budget, no checker.
- B2.M4: UNKNOWN, solver UNSAT but checker RSS-cap stop; no qualified refutation.
- B3.M2: UNKNOWN, solver budget, no checker.

No F14 result is inferred from old worker-only PASS observations, the two control releases, proof-feed equality alone, a stopped checker or GA/GB ID transfer.

## 4. First full-target reduction: a counterexample would have exactly four nonclassical squares

Assume for contradiction that a physical five-set is not classical. Let k be its number of nonclassical members, so1<=k<=5.

By L, k=5 would give

    sum_s(a_s-8)>=5*(11-8)=15,

contradicting R. Thus k<=4. The OLD K12/K3 imports exclude k=1,2,3, so

    k=4.                                                  (10)

This step consumes the complete LS theorem, not the earlier encoding or a restricted-real claim. If LS fails, K5 is not closed by this argument.

In any chosen row/column standard frame, EACH of the four nonclassical squares must have a weight3 entry. The elementary support budget gives weight<=3 for every square: at an off-reference-line cell, the five nonempty supports are pairwise disjoint and avoid the collinear reference cell, leaving seven coordinates. If one of the four nonclassical squares had no weight3 entry, LIGHT would replace just it by a classical square, preserving the other four squares unchanged. Exactly three nonclassical squares would remain, contradicting OLD K3. This also reconstructs the required part of K3's literal all-frame consequence without silently importing a stronger normalization theorem.

## 5. Normalize EACH chosen quantum square separately — not one joint template assertion

Fix ANY of the four nonclassical squares, call it Q_*. Choose an actual reference row and use a separate unitary on EACH square to align that row with the computational basis in common column order. The dimension a_* and the four/nonclassical count do not change. By §4, Q_* has some weight3 cell outside that row.

The following operations can start from THAT chosen witness, not merely a witness in some unspecified member:

1. Relabel Q_* as square1. Put the reference row at row0 by a common row permutation.
2. If its weight3 cell is(i,j), use a common row permutation fixing row0 to send i to1; use a common column permutation sigma sending j to0 and apply the coordinate-permutation unitary P_sigma to every square. Row0 stays computational in its final column order.
3. At(1,0), square1's three-coordinate support avoids0. The other four supports are nonempty, pairwise disjoint, avoid0 and avoid those three coordinates. They must therefore be the FOUR DISTINCT singleton supports in the remaining four coordinates.
4. A common coordinate/column permutation fixing0 sends the chosen support to{1,2,3}. Relabel the other four squares to give singleton supports{4},{5},{6},{7}. This never changes whether any square is classical, and keeps Q_* as square1.
5. Apply the exact property-form T16 residual moves and common non-strict row sorting. The new physical configuration has square1 column0 equal to one of ALL SIXTEEN tables, with a_1=a_*.

The other four members may be classical or nonclassical throughout. G has no fixed classical data and only square1's P4 witness; the fact its syntax calls all five “quantum” does not impose nonclassicality on them. Thus the fourteen F14 genuine exclusions apply to this normalized copy with this independently chosen Q_*.

Consequently THIS Q_* can only have P1-B2 or P1-B3 as its normalized column0 table. Repeat the argument starting afresh with each of the other three nonclassical squares. This gives four separate invariant lower bounds; it does NOT assert that one common normalization simultaneously gives all four the same table.

If the accepted cover/import were only an existence assertion for one unspecified chosen square, that would NOT suffice for this step. The explicit witness-preserving operations above and T16's literal SB2 antecedent are what license the per-square application.

## 6. The two load-bearing a>=12 arguments

### 6.1 P1-B2: dimension11 forces whole-vector sector isolation

For a chosen Q_* normalized to P1-B2, its column0 supports in rows0,...,7 are

    {0}, {1,2,3}, {7}, {6}, {4,5}, {4,5}, {2,3}, {1,2,3}.

The row0/column0 support graph has five components: coordinate blocks

    {0},   {1,2,3},   {4,5},   {6},   {7}.

Both axes are ONBs. The intersection-of-diagonal-algebras argument used in RANK LemmaB gives their projector span dimension16-5=11. Denote this axis span S_axis. Every projector in it is block diagonal across these five blocks.

The full projector span S contains S_axis, so a_*=dim S>=11. Suppose a_*=11. Then S=S_axis. Hence EVERY cell rank-one projector vv* is block diagonal across the five blocks, not merely a linear combination with unspecified outside components.

Let B=span(e4,e5). If v had both nonzero v_B and nonzero v_{B-perp}, the B/B-perp block of vv* would be the nonzero outer product v_B v_{B-perp}*. It cannot vanish. Therefore every full-cell vector is either WHOLLY in B or WHOLLY perpendicular to B. This is exactly ISOLATE's global isolation predicate; it is stronger than mere containment in a sum of block spans.

Row0 supplies the ray-pair{e4,e5}. Column0 supplies q^4,q^5, both with exact support{4,5}; they form an ONB of B and are a DIFFERENT orthonormal ray-pair. ISOLATE would require8>=2*(5+1)=12, contradiction. Thus a_*>11, and its integer dimension gives

    a_*>=12 in B2.                                        (11)

No whole-square classicality, prescribed interior support, phase choice or rank-one sufficiency from a Boolean model is used.

### 6.2 P1-B3: the axes already have dimension12

For P1-B3, the exact column0 support list is

    {0}, {1,2,3}, {6,7}, {6,7}, {4,5}, {4,5}, {2,3}, {1,2,3}.

The graph components have coordinate sizes1,3,2,2, so the two-axis projector span dimension is16-4=12, retaining every allowed amplitude/phase. As a subspace of the full projector span, it yields directly

    a_*>=12 in B3.                                        (12)

This assembly does NOT need the stronger B3>=13 or B3>=14 conclusions in the later sector manuscript. A reviewer finding a problem in those stronger arguments must not silently transfer it to this elementary axis lower bound unless the finding actually affects its stated proof.

## 7. Final conditional contradiction

Sections5–6 give a_s>=12 for EACH of the four nonclassical members. The fifth square has a_s>=8, so

    sum_s(a_s-8)>=4*(12-8)=16>14,

contradicting R. Therefore IF all precise new/old statement dependencies hold at their declared interfaces, no nonclassical five-set exists. This is the entire n8 target implication, with every quantum member and arbitrary phases/supports included.

It is not an exact GB_B2/GB_B3 Boolean refutation, not a witness, not a newly checked native computation, and not an accepted unconditional theorem in this run.

## 8. Explicit degraded cases — no hidden narrowing on partial failure

The full contradiction needs enough separate lower bounds; the following failures are not cosmetic.

- **B2 isolation step fails:** its axes alone still give a>=11, not12. All four quantum members might normalize to B2 in their separate normalizations. Then the only uniform lower bound is11, giving4*(11-8)=12<=14. K4 remains OPEN; no full closure follows from B3 alone.
- **B3 axis dimension step fails:** the conservative validated bound would be LS's a>=11 for a quantum square. If all four independently reach the weakened type, the same surplus12<=14 leaves K4 OPEN. Valid B2 bounds alone do not establish how many members reach B2.
- **Only k of the four quantum members have a verified a>=12 bound:** the other4-k have only a>=11 by LS, so the total lower bound is12+k. A contradiction requires k>=3. There is NO proof here that k>=3 if either template-wide bound is unavailable; in particular k<=2 leaves the bound<=14.
- **Per-square normalization or fourteen-template coverage fails:** normalization of one unspecified square could at best give one a>=12 bound and three a>=11 bounds, totaling13<=14. That is NOT sufficient. A missed physical template may likewise escape both §6 bounds.
- **LS fails or its all-complex/all-line-frame scope is narrower than stated:** K5 remains open under this new argument. Old K12/K3 do not settle it. No all-family conclusion survives by counting only K4.
- **Any old classification/necessity/representative/exact-input import is unavailable:** this remains a CONDITIONAL implication with that exact missing premise, not a new qualification or solved-book claim.

## 9. Verification and status preservation

Parent triage must read the COMPLETE new LS proof, the simple isolated-sector proof, RANK plus its operative erratum, the chosen-square normalization and both §6 bounds. Separate reconstruction must attack precisely these boundaries rather than treating an encoding as scientific progress. The current artifact and import ledger are frozen before any new review; no later review is presumed.

Historical final-v17 plus its operative delivery erratum remain the governing old status. GA18/18 and GB15/18 stay as recorded; B2.M2/B2.M4/B3.M2 remain UNKNOWN; original A10/A11 remain UNSATISFIED. The proposed mixed written/computer-assisted route could only replace the original all-input route through an explicit parent acceptance decision, with genuine-image mathematics and legacy trust limitations intact.

All computation in the old evidence is imported at statement level; no raw stream, control matrix, old held supervisor or historical process deviation was revalidated here. All twelve runtime obligations and HOLD remain. No independent-model CLI, new agent, program, solver, numerical assay, compilation, paid fallback, account change, Git mutation, deletion, publication or external contact occurred.

Priority/novelty/significance are unresolved. Even if the mathematics is accepted, this would be a composite result importing substantial old classifications and exact-input computations, not a pure new written proof, formal theorem, human review or automatically priority-certified discovery. The source is a modern Problem16, not a verbatim2009book conjecture or whole quantum-code chapter solution.
