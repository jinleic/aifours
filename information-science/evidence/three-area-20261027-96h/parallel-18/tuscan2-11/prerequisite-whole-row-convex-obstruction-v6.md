# Definition-first all-row bridge VI: even exact Hamilton-row columns have an always-feasible convex relaxation; the missing coupling is integral common selection

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 15:07:51 PDT 2026**. This resumes the admitted S1 line after the w10 review was returned at actual15:04:46. The Olson review packet is REVIEW-ONLY and is not a proof/method input here.

**NEW author-WRITTEN, unreviewed global prerequisite obstruction.** It applies without a maximal-overlap, support, Latin-column, symmetry or chosen-instance hypothesis. The exact whole-row integer model below is equivalent to the original problem. Its plain convex relaxation is explicitly feasible at EVERY n≥3, including the original n=11, even with the common-middle Laplacian from v2. Thus infeasibility of that relaxation cannot supply an original universal no-go. The proof identifies the exact missing integral common-row-selection premise rather than silently concluding that a fractional solution realizes some eleven rows.

## 0. Scope and permitted inputs

Only current S1/S2 literal packet SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c` (complete LF1-37), the definition-first release and pre-body exposure ACK, and named elementary finite counting/linearity are problem inputs. The identity of `prerequisite-common-middle-laplacian-v2.md` (SHA256 `8dec8f35e53114009c9e2f10f2e37f54ec078af002133e6779d324fa3f2c1b97`) is proved again where needed below, with its exact boundary terms.

No old stopped theorem, completed-turn, source, candidate, reviewer guide, private type8 setup or held/ZERO material is imported. Prior authorship/review exposure is not cleansed or claimed independent. The just-completed Olson duty supplies no premise or selection guidance for this Tuscan proof.

**Method:** a closed-form count over the mathematically defined set of ALL row permutations. No permutation list was generated, enumerated, sampled or proposed for scientific execution. No interpreter/calculator/Eval/CAS/program/solver/modelCLI, selected numeric/control/boundary probe or new GO.

## 1. Exact original-object model with whole actual rows

Let X be an arbitrary set of n≥3 symbols and let Ω be the set of all bijective linear rows π:[n]→X. This is the complete original row domain, not a restricted source family.

For x≠y and d∈{1,2}, put `A_d(π;x,y)=1` exactly when y occurs d LINEAR positions after x in π, and0 otherwise. There is no wraparound. An event at a fixed distance cannot repeat inside one row, because x has one position.

Associate a NONNEGATIVE INTEGER multiplicity z_π to each whole row. Consider:

1. `Σ_{π∈Ω} z_π = n`;
2. `Σ_π z_π A_1(π;x,y) = 1` for EVERY x≠y;
3. `Σ_π z_π A_2(π;x,y) ≤ 1` for EVERY x≠y.                 (IP)

### Lemma 1 — full forward/converse caller

Integer solutions of (IP) are exactly original Tuscan-2 arrays, up to permutation of their n row identities.

**Proof.** An original array gives its multiplicity for each actual row and satisfies all three constraints by the literal definition. Conversely, an integer solution specifies n whole actual permutation rows with multiplicities; reading those rows in any order gives the original array, exact distance1 coverage and distance2 noncollision. No pair/triple margins, independent endpoints or hidden Hamilton realization theorem is being substituted: each column π already IS a whole actual Hamilton row.

In fact z_π≤1 is automatic. If a row had multiplicity at least2, any one of its adjacent events would make the corresponding distance1 sum at least2. Thus repeated rows cannot enter unnoticed. No Latin-column property or support bound is imposed. ∎

This equivalence alone is an encoding, not the substantive result. The next lemma gives a uniform analytic feasible point of the relaxation and thereby identifies a real obstruction to using convex feasibility as original realization.

## 2. The plain convex relaxation is always feasible

Replace INTEGER in (IP) by REAL, preserving nonnegativity, every exact adjacency equation and every distance2 inequality. Call this relaxation (LP). Define, for EVERY π∈Ω,

`z*_π := n/n! = 1/(n−1)!`.

These are exact rational expressions, not floating estimates or computed factorials.

### Theorem 2 — all-variable barycentre

For EVERY n≥3 and EVERY symbol set X, z* satisfies (LP). More precisely, for each directed pair x≠y,

- its distance1 sum is exactly1;
- its distance2 sum is `(n−2)/(n−1)`;
- its missing-distance2 deficit is `1/(n−1)`.

**Proof.** There are n! mathematical row permutations, so their common weight n/n! has total n.

For a fixed ordered pair x,y:
- Exactly `(n−1)!` rows have y immediately after x: treat the consecutive ordered block xy as one item together with the other n−2 symbols. Hence the weighted adjacency sum is1.
- For distance2, choose its legal starting position in n−2 ways, then fill the other n−2 positions with the remaining symbols in `(n−2)!` ways. Equivalently choose its middle symbol and treat that ordered triple as one block. Thus exactly `(n−2)(n−2)!` rows have that event. Multiplying by `1/(n−1)!` gives `(n−2)/(n−1)<1`.

This count covers every ordered pair simultaneously by the same uniform weights. No particular permutation, parameter value, selected state or boundary case is tested. ∎

**Original-size consequence.** At n=11, every directed adjacent pair has total1, every directed distance2 pair has total9/10, and its deficit is1/10. This is a feasible fractional whole-row multiset, NOT a table of eleven actual rows and not an original T2(11) witness.

For n≥3 every z*_π is nonintegral, so THIS fractional vector cannot itself be the occurrence-multiplicity vector of n rows. Whether a DIFFERENT integral feasible vector exists at n=11 is exactly the original question and is not decided here.

## 3. Whole-row coherence and the common-middle PSD condition do not remove this point

The barycentre is stronger than separately picked pair/triple margins: each positive-weight object π is already a genuine complete permutation row, with all its endpoints, adjacencies and consecutive triples coupled correctly. What is relaxed is the requirement that the n units of row mass be n actual integral row occurrences.

For each ordered pair x≠y, the weighted boundary-adjacency usage (first edge plus last edge) is

`B*(x,y)=2/(n−1)`.

Indeed the first-edge occurrence count is `(n−2)!`, as is the last-edge count. They are distinct positions for n≥3; one directed pair cannot occupy both in one permutation row.

Consequently the weighted interior adjacency usage is

`I*(x,y)=1−2/(n−1)=(n−3)/(n−1)`.

The deficit is `M*(x,y)=1/(n−1)`. Unlike an original array these deficits are fractional; no missing-graph simplicity/integrality is silently assigned to them.

For ANY real function f:X→R define the whole-row-averaged common-middle sum

`Q*(f)=Σ_π z*_π Σ_{i=1}^{n−2}(f(π(i))−f(π(i+1)))(f(π(i+2))−f(π(i+1)))`.

The elementary per-row identity and exact overlap multiplicities from v2 apply by linearity: every interior edge belongs to two triples, each first/last edge to one, with the same actual middle in each product. Thus

`2Q*(f)=Σ_{x≠y}(I*(x,y)+M*(x,y))(f(x)−f(y))²`

`         = ((n−2)/(n−1)) Σ_{x≠y}(f(x)−f(y))²`.

Writing f-bar for the arithmetic mean of all symbol weights, elementary expansion gives

`Q*(f)= n(n−2)/(n−1) · Σ_x (f(x)−f-bar)²`.

So the common-middle matrix is

`((n−2)/(n−1))(nI−J)`.

It has the same constant diagonal n−2, zero row sums, nonpositive off-diagonal entries and strict positivity off constants as required by v2. It also satisfies the v2 cut identities for EVERY subset simultaneously, now with the fractional B*,M* values. No particular test vector, subset or numerical matrix was evaluated.

At n=11 this is the exact matrix `(9/10)(11I−J)`, with diagonal9 and rank10. It is not the integer-multiplicity combined graph of an original array. That distinction is precisely why satisfying the PSD/cut condition does not complete the gluing step.

## 4. What this falsifies — and what it does not

**The failed pointwise implication is exact:**

> A nonnegative real solution with total row mass n, built entirely from actual Hamilton rows, exact distance1 event totals and noncolliding-in-expectation distance2 totals, automatically realizes that SAME data as n actual rows.

It fails for z* at every n≥3: its occurrence weights are not integers. Adding whole-row consistency and the displayed common-middle PSD/cut constraints does not fix the point.

**The precise proof-method obstruction:** (LP), even with those extra PSD/cut constraints, cannot prove original nonexistence by infeasibility at any n≥3: Theorem2 and §3 exhibit an analytic feasible point for every n, including11. A proposed contradiction obtained solely from valid consequences of THESE relaxed constraints must be incorrect; evaluating it at z* would satisfy all the premises.

**Not asserted:**
- Feasibility of (LP) implies existence of SOME integral solution. That existential implication is not paid, and its truth at n=11 is not refuted here either; doing so would decide the original question.
- Every possible convex or semidefinite approach fails. Integer-valid cuts, genuinely joint multirow moments, or additional conditions NOT satisfied by z* could change the relaxation. They are not covered by this obstruction.
- The common-middle condition is useless. It remains a valid necessary coupling; it simply is not sufficient to enforce integral common selection.
- The fractional M* proves or prescribes regularity of an original missing graph. It does not.

## 5. Exact all-variable next gap

The remaining implication is now explicit without any maximal-overlap or chosen-support premise:

> Transport from the full actual-row convex mixture to an integral set of eleven mutually compatible rows, or derive an obstruction that genuinely uses that integral/joint-selection requirement.

No proof of that transport or contradiction is supplied. Single-row consistency, linear event margins, the common-middle Laplacian and its cut identities all survive the barycentre. Reasserting those conditions or selecting a numerical instance would not repair the gap.

The old original target stays OPEN, and every original support value remains in the scope of this definition-first result. No computational search or relaxation solver is proposed or admitted. A further written step must retain actual cross-row integrality/coherence, not treat an expected event count as occurrence-level noncollision.

Author-WRITTEN, unreviewed, same harness; no Main adoption, formal/kernel, executable, human, configured-family, source-openness, priority or novelty claim. All prior exposure, STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist; the science deadline remains2026-10-31T21:23:27.000Z.
