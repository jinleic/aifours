# Definition-first common selection XI: strong connectivity, exact D2 compatibility and Hamilton signs still do not imply a Hamilton pair

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 15:32:18 PDT 2026**.

**NEW author-WRITTEN, unreviewed exact failure theorem for the ABSTRACT residual relaxation.** A uniform symbolic family has all degree, strong-connectivity, local D2 and cycle-sign conditions used in v8-v10, yet has NO decomposition into two Hamilton cycles. This validates why the cut/common-Hamilton conditions cannot be dropped using only those premises. The family is NOT asserted to arise from n−2 actual admissible original rows, and it is NOT an original Tuscan counterexample.

## 0. Scope, inputs and the essential domain boundary

Current S1/S2 literal packet only: SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c`, complete LF1-37. Own new v8/v9/v10 supply the exact residual/cut caller, but the construction and all claims below are proved directly with elementary directed graphs/permutation signs/counts. No old proof/turn/Latin/support method, held/ZERO body, old source or Olson-review premise is used. Prior exposure is not declared clean.

No scientific interpreter/calculator/Eval/CAS, program/enumeration, solver, selected numeric/control/boundary probe, replay, modelCLI or new GO. Every block size, symbol order and permitted used-pair set below stays arbitrary. There is no finite group/table/row instance test or original-row ansatz asserted WLOG.

**Domain:** an augmented degree-two residual graph with formal already-used D2 pair data. Such abstract data are necessary consequences of a genuine n−2-row subsystem but are not by themselves a proof of that provenance. This missing partial-row realization is not filled by the counterfamily.

## 1. Full symbolic construction

Partition an arbitrary augmented vertex set V into THREE ordered nonempty blocks

`V_0=(v_(0,1),…,v_(0,l0)), V_1=(v_(1,1),…,v_(1,l1)), V_2=(v_(2,1),…,v_(2,l2))`,

where every l_j≥3 and l_j≠4. All labels are distinct. Let N=l0+l1+l2, choose ANY vertex of V_0 as the sentinel ∞, and let X=V\{∞}, n=N−1.

Define:
- P to be the ONE directed Hamilton cycle obtained by reading V_0,V_1,V_2 in their displayed forward order and returning to the first vertex;
- Q to be the cycle cover consisting of the THREE separate BACKWARD cycles on V_0,V_1,V_2;
- D=P∪Q, retaining the actual arc orientations.

This is an all-variable construction at every size given by the displayed hypotheses, not a choice of a numerical instance.

## 2. The structural and affine premises really hold

**Degree and simplicity.** P's within-block arcs are forward and Q's are backward; at l_j≥3 they are distinct. P's three splice arcs go between different blocks, whereas every Q-arc remains inside one block. Thus P,Q are disjoint, D is loopless/simple and every indegree/outdegree is2. P itself spans V, so D is strongly connected.

**Actual D2 compatibility of the two cycle covers.** On the whole augmented vertex set, the ordered two-step outer pairs of P and Q are disjoint:
- A P two-step path lying within one block increases its block index by2. A Q two-step path decreases it by2 modulo l_j. Equality would require l_j to divide4, impossible under l_j≥3,l_j≠4.
- A P two-step path crossing a splice has outer vertices in different blocks, since each block has at least3 vertices and a two-step path cannot cross two splices. Q two-step paths always stay in one block.

Within each cover, a two-step outer pair cannot repeat because its first vertex determines one image under the square of that cover permutation. No such outer pair is diagonal: all P/Q cycles have length at least3. Hence restricting to triples wholly in X also gives disjoint, distinct directed D2 events.

Each cover has N augmented two-step events. Exactly3 involve ∞ as first/middle/last vertex, distinct since its cycle has length at least3. Thus each has exactly `N−3=n−2` internal-original-symbol two-step events. Each also has N−2=n−1 original-symbol adjacency arcs after removing the two sentinel-incident arcs. These counts match the original row counts, but Q minus ∞ still has additional directed cycles and is NOT a row.

**Formal already-used pairs can have the required count.** Let E be the union of these2(n−2) disjoint internal D2 outer-pair sets. Its complement among X's directed distinct pairs has size

`n(n−1)−2(n−2)=n²−3n+4`.

For EVERY subset U of that complement with size `(n−2)^2`, the construction avoids all already-used pairs U. Such subsets exist because the complement size exceeds `(n−2)^2` by n. Thus the proper P/Q arc colouring satisfies all of v8's exact D2-XOR requirements relative to ANY such U. This is a formal U of correct size, not an invented claim that U came from n−2 actual rows.

**Hamilton parity.** P has sign `(-1)^(N−1)`. Q's three cycles have sign `(-1)^((l0−1)+(l1−1)+(l2−1))=(-1)^(N−3)`, the SAME sign. Thus both covers meet the individual Hamilton-sign requirement even though Q is not Hamilton. In particular the necessary product-sign condition `N−c` even in v8 holds for D's actual bipartite component count c, by the proved matching-sign identity. No component count is guessed or numerically computed.

## 3. Nevertheless NO Hamilton pair exists

For ANY one of the three blocks V_j, D has exactly ONE arc leaving it:
- P contributes its final forward block-splice arc;
- Q contributes none.

In a Hamilton cycle on all N vertices, a proper nonempty block must have at least one outgoing arc. Two edge-disjoint Hamilton cycles would need at least two DIFFERENT outgoing arcs across that block cut. Only one exists. **Therefore D has no two-Hamilton-cycle decomposition under ANY proper colouring**, not merely that the displayed Q happens to fail.

This is an exact HCUT obstruction. Strong connectivity, proper cycle covers, correct original adjacency/D2 event counts, local affine D2 compatibility and even both individual Hamilton signs do not imply a Hamilton pair on the abstract residual domain.

## 4. What has and has not been falsified

**Falsified:**

> An arbitrary augmented2-in/2-out residual with strong connectivity, correct event counts, an affine D2 solution and both Hamilton signs necessarily has some two-Hamilton decomposition.

Every hypothesis has been proved for the entire symbolic family; its conclusion is ruled out by the one-arc cuts.

**NOT falsified or established:**
- That those premises PLUS provenance as the complement of n−2 genuine partial original rows might imply more. No such partial rows are supplied for this family.
- Existence/nonexistence of the original T2(11), or of any original nine-row partial system with this residual.
- A particular fixed-size state/control. The construction is not a selected probe and is not promoted to a witness or counterexample at original order.
- The exact completion theorem of v8-v10, which retains HCUT/Hamiltonicity. The counterfamily explains precisely why those conditions remain load-bearing.

The boundary matters: abstract residual feasibility does not authenticate its actual-row antecedent, and an abstract residual obstruction is not a universal original obstruction.

## 5. Next original common-selection obligation

To turn residual reasoning into an original result, one must either construct an actual n−2-row system meeting the robust positive caller, or prove an unavoidable negative cut/parity/capacity condition for EVERY such actual subsystem, or use a different all-array route. The present counterfamily does none of these and does not pretend its formal U carries the missing occurrence-level provenance.

A next genuinely useful step must use actual partial-row provenance or integral all-row selection, not silently relax them again. No external source, old stopped method, solver or finite probe is authorized by this observation.

All prior exposure/STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP remain. Same-harness author-written, unreviewed; no Main adoption, formal/kernel, executable, human, configured-family, source-openness, priority or novelty claim. Original target OPEN; full-window standing direction and deadline unchanged.
