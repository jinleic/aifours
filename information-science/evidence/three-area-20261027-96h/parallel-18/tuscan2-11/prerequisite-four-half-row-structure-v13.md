# Definition-first common selection XIII: the forced four-half-row boundary has three matching signatures, genuine cut capacity and exact within-support rounding obstructions

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 15:46:46 PDT 2026**.

**NEW author-WRITTEN, unreviewed boundary theorem, universally quantified.** The four rows here are NOT a hand-picked small input or a numerical sanity probe. They are the analytically forced equality structure from v12, for arbitrary n and arbitrary feasible original-row mixtures. No such boundary point is constructed or asserted at n=11. This identifies real actual-row provenance missing from abstract residual data and gives exact positive/negative statements about rounding WITHIN the four-row support. No unrestricted original existence/nonexistence follows.

## 0. Inputs, setting and separation

Only admitted Tuscan S1/S2 literal definitions, elementary real linear equations, finite counts and matching-cycle signs are mathematical inputs, using the complete own proof `prerequisite-purity-gap-and-half-boundary-v12.md`, SHA256 `34f89d821b9afad25409b52581a22e112925d986dc55309b508e76aa0063b2a6`. The sentinel/component facts are re-established where needed below.

No old source/turn/support/Latin theorem, held/ZERO guide or Olson review is an input. The w38 selected-control PROCESS MAJOR and ENTIRE w38 episode/partial-assessment/consumer ZERO persist; Main permitted only genuinely disjoint already admitted Tuscan work. These are the pre-existing whole-row/graph inputs, not group/field/polynomial/carry material, with no clean-cognition claim.

No program, row/graph enumeration, scientific interpreter/calculator/Eval/CAS, solver, chosen numerical/control/boundary probe, modelCLI or new GO. All support patterns below are a complete symbolic classification of the forced equality case, not sampled candidate row sets.

Assume a feasible whole-row mixture has purity n−1 and the v12 rounding callers have not supplied an original array. Then it has n−2 UNIT rows and FOUR DISTINCT HALF rows P1,…,P4. Augment by ∞ and delete the unit-row cycles from the complete directed graph. The residual D on N=n+1 vertices is2-in/2-out; each Pi is an ACTUAL Hamilton cycle in D, and every residual arc belongs to EXACTLY TWO Pi. Every original D2 outer pair unused by the unit rows occurs in at most two Pi; a used pair occurs in none. These are all proved in v12, not merely formal pair margins.

## 1. Actual mixture provenance forces every residual cut to have capacity at least two

### Lemma 1

For EVERY nonempty proper A⊂V(D), `|δ⁺(A)|≥2`. If the outgoing cut has exactly two arcs e,f, each Pi contains exactly one of them.

**Proof.** Each actual Hamilton Pi leaves A at least once. Across all four Pi there are therefore at least4 outgoing-arc occurrences. Each residual arc is counted twice, so the total is `2|δ⁺(A)|`, proving the capacity bound. At cut size2 the total is exactly4; all four positive Hamilton cycles must therefore leave exactly once. ∎

More generally the same proof holds for ANY feasible residual mixture of total mass2 on actual Hamilton cycles, with every residual arc usage1; half weights are not needed for that assertion.

This is precisely an actual-row antecedent absent from the abstract counterfamily in v11, whose one-arc cuts cannot arise from such a feasible residual mixture. That counterfamily was not asserted to have this provenance; no abstract obstruction is retroactively promoted to an original-row one.

## 2. Three signatures exhaust the common matching data

Make the bipartite representation of D, with left tails and right heads. Every component is an even cycle, and any perfect matching chooses one of its two alternating orientations. Choose Pi=P1 as the reference orientation0 on every component.

Because each residual arc is present in exactly two of P1,…,P4, on each component exactly ONE of P2,P3,P4 agrees with P1; the other two take the opposite orientation. Thus every component has exactly one of the following signature columns:

| signature | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| A | 0 | 0 | 1 | 1 |
| B | 0 | 1 | 0 | 1 |
| C | 0 | 1 | 1 | 0 |

Complementing the original reference on a component does not change its signature partition. At least TWO signature types occur: otherwise one of P2,P3,P4 would equal P1 on every matching component and be the same actual row, contrary to distinctness.

A pair of Pi is adjacency-disjoint exactly when its two bits differ on EVERY occurring signature. If all three types occur, every pair agrees somewhere, so none of the six pairs is an adjacency completion. If exactly two types occur, exactly TWO pairs (a pairing of all four indices) are adjacency-disjoint and hence complementary cycle covers. Since each Pi is already Hamilton, either such pair passes the adjacency/row-realization requirement without a new Hamilton assumption.

This is an exact within-support conclusion. It does NOT say that a completion outside the four rows is impossible when no pair within them works.

## 3. Distance-two compatibility and exact pair-rounding criterion

Each unused original outer pair occurs in at most two Pi. It forbids selecting Pi,Pj together exactly when it occurs in BOTH (an occurrence set of size2). Used outer pairs occur in no Pi and cause no new pairwise exception.

Consequently, when exactly two signature types occur, the following are equivalent:
- some two Pi complete the original array together with the n−2 unit rows;
- at least one of the two adjacency-complementary pairs has no common original distance2 outer pair.

Both directions concern these SAME actual rows: no independent per-event or per-cut choices are glued. A blocked pair is rejected by its actual shared outer pair; this does not reject the other complementary pair unless it has its own obstruction.

## 4. Exact real perturbation structure within the four-row support

Keep the unit rows fixed and change the four half weights by real increments d1,…,d4. An adjacency arc appearing in a pair {i,j} keeps usage1 exactly when `di+dj=0`. For each occurring signature, BOTH such pair equations are required.

### Lemma 2

- If all three signatures occur, the only adjacency-preserving perturbation is d=0.
- If exactly two signatures occur, after relabelling the Pi the perturbations are exactly

`d=(t,−t,−t,t)`.

The positive pair and negative pair are precisely the two adjacency-complementary pairs.

**Proof.** For signatures A and B, the equations are `d1+d2=d3+d4=0` and `d1+d3=d2+d4=0`, giving the displayed one-parameter vector. Adding signature C requires `d1+d4=0`, hence 2t=0 over the REAL numbers and t=0. Any other pair of signatures is obtained by permuting P2,P3,P4. ∎

The distinction between real weight perturbation and binary component orientation is explicit; no characteristic-two cancellation is used to remove the factor2.

For exactly two signatures, a D2 pair occurring in a non-complementary pair of rows has derivative0 under this perturbation. A D2 pair common to the positive complementary pair has derivative2t, so its tight cap requires t≤0. A D2 pair common to the negative pair requires t≥0. Pairs occurring in only one row have slack at least1/2 at the half point and stay feasible for sufficiently small |t|.

Therefore:
- if at least one complementary pair has no common D2 pair, a nonzero feasible perturbation toward that pair exists (or select that pair directly), and the original array is obtained;
- if BOTH complementary pairs have D2 blockers, the only feasible within-support perturbation is t=0;
- with all three signatures, even adjacency constraints alone isolate the four-support point.

Purity along a feasible nonzero line is `n−1+4t²>n−1`, so the first conclusion also matches v12's all-variable rounding theorem. No perturbation or numerical value is actually chosen or evaluated.

These are exact support-face obstructions, not proof that no point on a larger support, or no original array, exists.

## 5. A further global sign constraint, with its exact limitation

Let the bipartite matching components have half-lengths l_j. Let w_A,w_B,w_C be, modulo2, the sums of l_j−1 over the components of each signature type (zero if the type is absent).

All four Pi are Hamilton cycles of length N, hence have the same sign. Comparing to P1:
- P2 flips the B and C components, so `w_B+w_C=0`;
- P3 flips A and C, so `w_A+w_C=0`;
- P4 flips A and B, so `w_A+w_B=0`.

Thus `w_A=w_B=w_C=w`. The parity obstruction for TWO complementary Hamilton cycles is

`Σ_j(l_j−1)=w_A+w_B+w_C=w=0`.

If w=1, NO two-Hamilton-cycle decomposition of this residual is possible, even though it has four actual Hamilton cycles as a two-cover. This is a conditional certificate; existence of such a critical boundary point is not asserted. If exactly two signature types occur, the absent type has w=0, so the common w is automatically0, consistently with its two known Hamilton complementary pairs. Their D2 compatibility still must be checked.

With three types, the sign argument does NOT force w=0 merely because four individual Hamilton cycles exist. It also does not assert that w=1 actually occurs for a partial original system. No parity gap is hidden or a symbolic possibility promoted to an example.

## 6. Original boundary after this step

We have used actual residual-mixture provenance, not just formal degrees, to prove cut capacity; completely classified the forced matching signatures; and identified exactly when a complementary pair or a feasible within-support purity improvement exists.

**Still unresolved:**
- a two-signature boundary with both candidate pairs D2-blocked may require new rows or a genuinely larger-support change;
- a three-signature boundary has no adjacency-preserving direction on those four atoms, and cannot be rounded by selecting two of them;
- no proof excludes such boundary patterns for actual original partial systems, nor produces a high-purity feasible mixture at n=11.

The next common-selection step must confront those exact simultaneous constraints, not claim that a fractional two-cover is already a Hamilton pair or that one positive choice works for every D2 pair. Original Tuscan-2(11) remains OPEN. All original support values remain in scope; no selected-state experiment or stronger verification occurs.

The w38 PROCESS MAJOR/complete ZERO consumer boundary and all earlier exposure/STOP/HOLD/ZERO/N4UNKNOWN/historical-exit-UNESTABLISHED/aux214STOP limits persist. Same-harness author-written, unreviewed; no Main adoption, formal/kernel, executable, human, configured-family, source-openness, priority or novelty claim. Full-window standing direction and deadline unchanged.
