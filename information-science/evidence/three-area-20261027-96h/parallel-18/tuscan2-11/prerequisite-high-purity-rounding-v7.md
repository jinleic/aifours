# Definition-first all-row bridge VII: a high-purity fractional whole-row solution rounds to the original array, including the equality boundary

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 15:11:38 PDT 2026**.

**NEW author-WRITTEN, unreviewed conditional realization theorem.** No maximal-overlap or chosen-support premise is used. At order11, a feasible whole-row mixture with squared-weight sum at least21/2 guarantees an actual original Tuscan-2 array: its rows of weight greater than1/2 are the required eleven rows. No such mixture is produced here, and no original existence/nonexistence or novelty claim follows merely from the conditional theorem.

## 0. Scope and named inputs

Only the current S1/S2 literal packet SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c` (complete LF1-37), the definition-first controls/pre-body exposure ACK and elementary finite counts/inequalities are inputs. The whole-row model is from the same admitted `prerequisite-whole-row-convex-obstruction-v6.md`, SHA256 `91167935f66f07302d365fb8b3b971e2a1b1637f4c3abb957228b5b319ccf7f3`; its needed definitions and proofs are reproduced below.

No old stopped proof, source, completed-turn theorem, author/reviewer guide or held/ZERO body is an input. The w10 Olson material remains solely review input, not a Tuscan theorem/method premise. Prior exposure survives without a clean-cognition claim.

Written proof only: no interpreter/calculator/Eval arithmetic/CAS, generation/enumeration of row permutations, selected numerical/control/boundary probe, program, solver, replay, modelCLI or new GO. The exact threshold and equality analysis are symbolic for all n, not a tested boundary instance.

## 1. Fully original row domain and relaxed hypotheses

Let n≥3 and Ω contain EVERY actual linear permutation row π of an n-symbol set X. For each x≠y, A_d(π;x,y) is the indicator that y is d positions after x in that row, d=1,2. No wraparound, column-Latin property, symmetry or support assumption is used.

Let real weights z_π satisfy:
- `z_π≥0`;
- `Σ_π z_π=n`;
- `Σ_π z_π A_1(π;x,y)=1` for every directed pair x≠y;
- `Σ_π z_π A_2(π;x,y)≤1` for every directed pair x≠y.           (F)

Every individual atom is a full actual row, with its endpoints and both event layers already coupled. The remaining issue is selecting n such atoms as mutually compatible original rows, not realizing a single atom from margins.

Define purity `P(z)=Σ_π z_π²` and the heavy support `H={π:z_π>1/2}`.

### Lemma 1 — caps and heavy-row compatibility

Every z_π≤1. Distinct heavy rows have no shared directed event at the SAME distance1 or2. Hence |H|≤n.

**Proof.** Each actual row contains an adjacent event, and its corresponding equation in (F) has nonnegative terms summing to1, so z_π≤1. If two heavy rows shared an event at distance1 or2, their two weights alone would sum to more than1, violating that event's cap. Thus their adjacency sets are disjoint; each has n−1 distinct directed events among the n(n−1) possible ones, so |H|≤n. ∎

This uses actual directed event incidence, not an assumption that all positive-weight atoms are already compatible.

## 2. Strict-threshold rounding

### Lemma 2

If `P(z)>n−1/2`, then |H|=n and H is an original Tuscan-2 array.

**Proof.** Put h=|H|. On H, `z²≤z` since z≤1. On its complement, `z²≤z/2` since z≤1/2. Hence

`P(z)≤Σ_H z+(1/2)Σ_(Ω\H) z = n/2+(1/2)Σ_H z ≤ (n+h)/2`.

If h≤n−1, this would give P≤n−1/2. Thus h≥n, and Lemma1 gives h=n.

Select these n heavy rows as actual rows. They are permutations with pairwise disjoint distance1 and distance2 event sets at the respective distances. Their n(n−1) adjacency events exhaust all directed pairs, while their distance2 events are noncolliding. This is precisely the original definition, with actual linear rows and no reordering of symbols within a row. ∎

No assertion that the original fractional weights themselves become integers is made; the output is the actual heavy-row subset.

## 3. Equality boundary: whole-row identity removes the possible scalar exception

We now prove the same conclusion when `P(z)=n−1/2`. This requires the actual whole-row domain; a generic vector-of-weights bound alone does not suffice.

### Lemma 3 — unit-row completion

If a feasible z in (F) has n−1 rows of weight1, then it is the indicator of an original n-row array.

**Proof.** Those n−1 rows are pairwise compatible by the event caps. Their directed adjacency sets are disjoint and contain `(n−1)²` events. Let U be the complement in all n(n−1) directed pairs, so |U|=n−1.

Any other positive-weight row must avoid every adjacency already covered by a unit row, hence its n−1 adjacency events are exactly U. A directed Hamilton row is uniquely determined by its directed adjacency set: its first symbol is the unique vertex with no incoming edge, and following its unique successors recovers the whole actual linear path. Thus all remaining positive row atoms must be the SAME row type τ. Ω has one atom per actual row type, so there is at most one such atom. Its weight must be1 because the remaining total row mass is1.

The distance2 caps ensure τ also shares no distance2 event with any unit row. Therefore the n unit rows form the original array. This proves the claimed full original-object caller, not just an adjacency completion. ∎

### Theorem 4 — closed-threshold rounding

For EVERY n≥3 and every feasible z in (F),

`P(z)≥n−1/2` implies that the n heavy rows exist and form an original Tuscan-2 array.

**Proof.** The strict case is Lemma2. Suppose P=n−1/2. If h≤n−1, the inequality chain in Lemma2 must be equality throughout. Therefore h=n−1 and `Σ_H z=h`, so every heavy row has weight1. Lemma3 then makes z an indicator of n rows, giving P=n, contrary to P=n−1/2. Thus h=n, and the actual-row conclusion follows exactly as in Lemma2. ∎

All boundary cases in this proof are original-variable cases, not a selected numerical probe. A threshold of1/2 is used strictly for H: a row of weight exactly1/2 is not silently treated as compatible with another half-weight row.

## 4. Exact forward/converse original caller and what remains open

**Forward:** an original array gives indicator weights for its n actual rows, satisfying (F) and P=n≥n−1/2.

**Converse:** Theorem4 extracts the n heavy actual rows from any feasible z above the closed threshold, and the proof verifies EVERY original distance1/distance2 event condition on those very rows.

Consequently the following are equivalent at the original n=11:
1. an unrestricted original Tuscan-2(11) array exists;
2. a feasible whole-row mixture (F) exists with `P(z)≥21/2`;
3. a feasible whole-row mixture exists with purity11 (an integer indicator solution).

The realization direction2→1 is the substantive new bridge: integrality of z is not assumed, and the actual object is explicitly selected. Merely introducing (F) or restating1↔3 would be an encoding, not the result.

The uniform barycentre of v6 shows that (F) is feasible but does NOT establish the purity premise. No high-purity feasible point is produced, no maximization is run or proposed, and no upper bound excluding that premise is proved. This threshold is sufficient, not claimed best possible for the original constrained polytope.

**Exact remaining mathematical obligation:** prove existence of a feasible mixture reaching the threshold, or show all feasible mixtures lie below it, using a genuinely admissible common-selection argument. The present proof does not claim either conclusion, and the original problem remains OPEN.

This applies to arbitrary coherent systems at all original support values; it does not assume every array has a concentrated cross-layer transport edge or triangle. No new source, old method release or scientific execution follows by implication.

All prior exposure, STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist. Same-harness author-written, unreviewed; no parent adoption, formal/kernel, executable, human, configured-family, source-openness, priority or novelty acceptance. New research deadline unchanged.
