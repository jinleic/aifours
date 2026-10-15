# Optimization of visual cryptography schemes

**Status: PARTIALLY-SOLVED — the original general problem remains OPEN in this investigation.** This is an evidence-limited assessment, not a proof that no later solution exists. No full solution, new theorem priority, or AI advantage is claimed.

**Book:** 视觉密码方案的最优化问题 / *On the Optimization of Visual Cryptography Schemes*, Liu Feng, in *10000 Selected Problems in Sciences: Information Science* (Science Press,2011), printed pp.409–410 / PDF pp.430–431. Both [original page images](sources/book/) were read visually. Research date: **2026-10-14 (PT)**.

## Original question and what would count as a full solution

For general access structures, determine (1) minimum pixel expansion, (2) maximum contrast, (3) maximum contrast at minimum expansion, and (4) minimum expansion at maximum contrast; construct attaining schemes and clarify the expansion–contrast trade-off.

A full solution must resolve these quantitative/extremal and construction questions over the original general class, with a complete independently checked argument and reproduction evidence. **An LP/ILP restatement, an exact per-instance search procedure, a finite table, or a complexity reduction is only partial progress**, not a redefinition of that goal. The book does not demand polynomial time, and none is imposed here. The 1996 reference distinguishes arbitrary finite matrix collections from basis matrices, and strong from weak structures; our restrictions below are explicit rather than silently replacing the original question.

A concrete existing obstruction is already present in the threshold subfamily: [Blundo–De Santis–Stinson1999, Theorem4.7](sources/blundo-1999.pdf) proves that for n=3 mod4, optimum-contrast (2,n) schemes have expansion at least n, with equality **iff a real Hadamard matrix of order n+1 exists**. The [Cati–Pasechnik construction database](https://arxiv.org/abs/2411.18897) still presents the real all-orders existence statement as a conjecture. This is a substantive design-existence barrier, not merely a missing solver or an inference from unsuccessful searches.

## Fixed model

- Black-white shares; a black subpixel is1; reconstruction is Boolean **OR** (physical stacking).
- A **strong** access structure is specified by a nonempty antichain A of nonempty minimal qualified sets. Every superset of a member of A is qualified; every other subset is forbidden. The sweep includes dummy participants and singleton-qualified sets; it excludes the two constant Boolean functions.
- **Every qualified set**, not only a minimal one, must reconstruct by stacking all of its shares. Weak structures with unclassified sets are not enumerated.
- A deterministic collection VCS consists of nonempty finite multisets C0,C1 of n-by-m binary matrices with a common expansion m, sampled uniformly. Security requires identical distributions of the **entire row restriction** for each forbidden set. Deterministic means guaranteed reconstruction separation; the encoding still uses randomness.
- Its guaranteed integer gap is `g = min_Q (min_C1 W_Q - max_C0 W_Q) >= 1`, and the optimized contrast is **alpha=g/m**. Ateniese1996 calls alpha “relative difference” and g “contrast”; later terminology often calls alpha contrast. Maximizing the unnormalized g with no expansion bound is unbounded by repetition, so that cannot be the book's intended finite maximum. No alternate background normalization is substituted.
- A **basis scheme** is the subclass formed by all column permutations of two fixed matrices. General collections may mix different column multisets. We do **not** assume that this restriction preserves finite-expansion optima.
- XOR, reversing, random grids/expected-only contrast, colors, evolving participants, and meaningful cover images are different models, not improvements that settle this question.

The full definitions, LP/ILPs, inverse transform, proofs, and model-transfer limitations are in [work/model.md](work/model.md).

## Completed scope: independently certified finite tables

**Certification:** all four objectives and attaining basis matrices for **every non-isomorphic nonconstant strong access structure on n<=5**, now also certified for arbitrary deterministic finite collections. The first pass covered all n<=4 and203/208 n5 collection rows; the separate [full-distribution continuation](work/collection-continuation.md) closes the remaining five. This finite equality is not an all-n basis/collection equivalence theorem.

**Independent re-derivation (parent-commissioned, 2026-10-14):** a separate agent, given only the access structures and the full-distribution model and barred from this directory's code, proofs and certificates, re-enumerated all orbits, proved its own filters and reached the same six NO verdicts. Its certificate-only checker validates 611 nonzero integer separator terms without an LP solver; the parent replayed that checker on a hash-pinned snapshot. Its negative control shows why the full model matters: requiring only equal expected projected column counts makes the last structure feasible at m=7, while an observer of participant 1 alone sees an all-white row with probability 3/10 under white versus 0 under black. Evidence: [`../evidence/information-science-push-20261014/visual-independent/`](../evidence/information-science-push-20261014/visual-independent/), replay [`visual-independent-parent-replay.json`](../evidence/information-science-push-20261014/visual-independent-parent-replay.json), leak check [`visual-expected-count-leak-parent-check.json`](../evidence/information-science-push-20261014/visual-expected-count-leak-parent-check.json).

| n | Isomorphism classes | Labelled structures covered | All four basis objectives | All four collection objectives | Classes with a strict expansion/contrast trade-off |
|---:|---:|---:|---:|---:|---:|
|1|1|1|1|1|0|
|2|3|4|3|3|0|
|3|8|18|8|8|0|
|4|28|166|28|28|1|
|5|208|7579|208|208|23|

The totals are248 classes and7768 labelled structures across n=1..5 (dummy extensions at different n remain separate). The “trade-off” column means that the best contrast at minimum expansion is strictly smaller than global maximum contrast. It is not a novelty claim.

### Representative exact rows

Here `123` denotes participant set {1,2,3}. All numbers in this table hold for both basis and collection models.

| Minimal qualified sets / family | Minimum m | Maximum alpha | Maximum alpha at minimum m | Minimum m at maximum alpha |
|---|---:|---:|---:|---:|
|2-out-of-3|3|1/3|1/3|3|
|2-out-of-4|4|1/3|1/4|6|
|123;124;134 on four participants|6|1/6|1/6|6|
|3-out-of-4|6|1/6|1/6|6|
|4-out-of-4|8|1/8|1/8|8|
|2-out-of-5|4|3/10|1/4|10|
|3-out-of-5|8|1/8|1/8|8|
|4-out-of-5|15|1/15|1/15|15|
|5-out-of-5|16|1/16|1/16|16|

The smallest strict trade-off in the sweep is the **classical 2-out-of-4 example**, not a new counterexample to a published conjecture. At m=4, choose B0 with every row1100 and B1 with four distinct weight-two rows, e.g.1100,1010,1001,0110; the minimum gap is1. At m=6, choose B1 with the six weight-two columns and B0 with every row111000; the minimum gap is2, giving alpha1/3. The certificates prove the respective bounds and minimum lengths.

### Five collection gaps closed by full-distribution obstructions

The five rows previously reported as intervals now have the following exact collection optima. Existing basis witnesses attain every upper bound; the continuation excludes the missing shorter lengths without assuming collections are basis schemes.

| Minimal qualified sets on five participants | Minimum m | Exact alpha_max | Maximum alpha at minimum m | Minimum m at alpha_max |
|---|---:|---:|---:|---:|
|12;13;23;14;24;345|6|1/5|1/6|10|
|12;13;14;235;245;345|7|1/6|1/7|12|
|12;13;24;34;235;145|6|1/5|1/6|10|
|12;13;24;235;145;345|7|1/6|1/7|12|
|123;124;134;125;135;145|8|1/6|1/8|12|

**What changed:** uniform column permutation reduces each complete forbidden projected-matrix distribution to a distribution over whole projected-column multisets. At lengths5,6,5,6,6, exact optimal-LP-face restrictions plus complete support matching eliminate both colors in one round. The final length7 is **not** restricted to an optimum face: all32 column types are enumerated, every qualified superset is enforced, and all integer reconstruction thresholds are covered. Its sole nonempty terminal support has17 white and13 black orbits. An explicit15-term integer function of full forbidden projections is at least1 on every white orbit and at most0 on every black orbit, contradicting security for arbitrary probabilities. Necessary black-matrix SAT assignments are never used as VCS witnesses.

The [complete proof](work/collection-continuation.md), [integer certificate](evidence/continuation-20261014/certificate.json), [exact replay with complete threshold tree](evidence/continuation-20261014/verification.json), and [prior-art comparison](evidence/continuation-20261014/prior-art.json) are separate from the frozen first-pass package. The decisive verifier uses only integer/Fraction arithmetic and no optimization solver; this is not Lean/kernel certification.

**General structural consequence, not a full solution:** if Gamma+ adds one indispensable participant to a nonconstant strong access structure Gamma, then `G_basis,Gamma+(m)=G_basis,Gamma(floor(m/2))`, and the global maximum relative contrast is halved in **both** the basis and collection models. The proof does not extend the fixed-length identity to collections. The last row is the cone of2-out-of4; the full-distribution length7 obstruction is the extra collection obligation. Neither this lemma nor the five local closures has been novelty-cleared.

The fifth row is also the established **(3,5)* access family** in [Arumugam–Lakshmanan–Nagar2014](https://doi.org/10.1007/s10623-012-9722-2). Its primary abstract was checked; subscription-only detailed bounds still require comparison. “Closed” here means closed in this investigation, not a claim that the literature left these cases open.

## How the certificates work

1. A column type T is the subset of black rows. Two basis matrices are specified by nonnegative integer counts x_T,y_T, each summing to m.
2. Define `f(S)=sum_{T disjoint S}(x_T-y_T)`. Equality `f(F)=0` for every forbidden F is equivalent to equality of every forbidden projected-column histogram by inclusion–exclusion. Qualified gaps are f(Q).
3. Integer programs generate the three finite-expansion witnesses; a normalized rational LP gives maximum alpha. Clearing denominators attains that LP value with a finite basis pair.
4. The independent verifier directly checks **all forbidden projected patterns**, every qualified gap, and all rational LP primal/dual inequalities using exact fractions. It does not trust floating-point solver objectives.
5. Integer lower bounds use either exact LP/integrality/divisibility bounds or a separately derived Mobius-coordinate model: integer qualified f-values, forbidden f=0, inverse transform d, length `sum max(d_T,0)`. Z3 checks the18 remaining objective obstructions. Queries and results are retained.
6. Coverage is independently checked by antichain backtracking and complete permutation orbits, rather than the candidate generator's truth-table recursion. Four tamper controls are rejected.
7. Concatenating equal-sized encoding collections gives a basis pair with at least the same normalized gap, so maximum alpha transfers; this argument is already classical for thresholds and does **not** preserve m. A further necessary condition on every black encoding, `W_Q-W_F>=1` for forbidden F subset qualified Q, certifies four additional collection lower bounds. Rational divisibility then certifies their optimum-contrast lengths.

**First-pass observed:**248 rational primal/dual certificates,744 direct integer witnesses,726 elementary objective bounds,18 independent Mobius UNSAT checks, and four additional universal-collection UNSAT checks. Generation took22.75s and verification2.01s; no timeout or omitted row. That integer infeasibility component trusts Z3; these are not Lean/kernel-checked proofs. [Run provenance](evidence/run-notes.md) records commands, versions, the one corrected API error, and the first-pass collection extension.

**Continuation observed:** the standalone exact verifier certified all six missing-length obligations in20.86s, using no optimization solver. It checked the stored rational LP faces, the attaining basis witnesses, every complete forbidden projected-matrix signature, every qualified superset, all49 viable threshold-search nodes, the17/13 terminal support separator, and two negative controls. [Verification receipt](evidence/continuation-20261014/verification.json) binds the exact input/certificate/verifier hashes; [conclusions](evidence/continuation-20261014/conclusions.json) states the resulting four objectives and the remaining general blocker.

## State of the art and literature-status limits

| Result | Hypotheses / relevance | Primary source | Verification extent |
|---|---|---|---|
|General-access existence constructions; small-n bounds; exact 2-out-of-n minimum expansion via Sperner families|Original OR collections/basis distinctions|[Ateniese et al.1996](https://doi.org/10.1006/inco.1996.0076)|Author full text, definitions and relevant theorems read|
|Exact 2-out-of-n alpha; optimum-contrast expansion characterized by designs; two n4 gaps closed|Threshold, with collection bounds|[Blundo et al.1999](https://doi.org/10.1007/s001459900057)|Author full text and relevant proofs read; numeric anchors reproduced|
|Symmetry-reduced contrast LP and optimal families|Threshold, not all arbitrary-access trade-offs|[Blundo et al.2003](https://doi.org/10.1137/S0895480198336683)|Author full text; LP scope checked|
|Threshold contrast asymptotics and approximation-theory connection|Fixed-k threshold family|[Krause–Simon2003 / ECCC](https://eccc.weizmann.ac.il/report/2000/003/)|Primary abstract; saved PDF text garbled, not proof-audited|
|Threshold / general-access pixel-expansion optimization papers|Classical ILP baseline candidates,2011/2015|[Shyu–Chen2011](https://doi.org/10.1109/TIFS.2011.2158096), [2015](https://doi.org/10.1109/TCSVT.2015.2389372)|Publisher-deposited metadata verified; detailed formulations/numerical claims **[UNVERIFIED]**, full text inaccessible here|
|Strong general-access linear-algebra construction; (n,n) optimality|No universal general-access optimum claimed in abstract|[Adhikari2014](https://link.springer.com/article/10.1007/s10623-013-9832-5)|Publisher abstract verified|
|Integer-programming computations for <=5 participants|**Extended meaningful-share** VCS, different model|[Sekine–Koga2021](https://doi.org/10.1587/transfun.2020DMP0010)|Publisher abstract verified; not misreported as the present n5 table|
|Evolving random-grid / color monoid developments|Different models, not solutions of deterministic black-white OR optimization|[Zhuo et al.2025](https://arxiv.org/abs/2508.15917), [Reif–Zumbrägel2025](https://arxiv.org/abs/2510.00763)|Primary abstracts verified|

Full citations, fetched locations, caveats and excluded misleading matches are in [sources/references.md](sources/references.md). **No exact-model NP-hardness claim was verified or made.** An ILP formulation is not a hardness proof. No retrieved source establishes a complete arbitrary-access resolution of the book question; absence of such a retrieved source is not proof of absence.

## Outcome labels and attack log

- **Certification:** complete n<=5 basis and collection tables for all four objectives. The original203/208 transfer and its frozen evidence remain intact; the new full-distribution continuation supplies exactly the five missing collection rows.
- **Reproduction:**23 primary-source numerical comparisons match; the 2-out-of-4 trade-off, threshold formulas, n4 m=6 resolutions, and the Hadamard/design barrier are prior results.
- **Discovery:** no independently novelty-cleared mathematical discovery or published-conjecture counterexample is claimed.
- **Empirical evidence:** runtime/resource measurements only. The finite optima are exact-certification claims, not estimates extrapolated to arbitrary n.
- **Novelty status:** unclear for the complete n5 package or cone identity. Lawful full-text comparisons to Shyu–Chen2015 and Arumugam–Lakshmanan–Nagar2014 are needed before priority claims; the latter's primary abstract already matches the fifth access family.

First-pass attack: confirm book images and model distinctions -> derive count LP/ILPs and independent moment inversion -> exercise n<=3 controls -> freeze and complete n<=5 -> certify rational/independent integer bounds -> test the broader collection relaxation -> compare23 primary-source anchors -> hostile-referee review. Continuation: exact optimum-face orbit support matching -> unrestricted length7 full-projection support pruning -> complete integer-threshold branching -> explicit integer separating functional -> independent review and direct replay. No n>=6 sweep, no random-grid/XOR substitution, and no resealing of the old acceptance package.

Two independent Codex sessions completed: the main referee returned **correct-with-fixes**, and the collection-lemma referee accepted the argument with an explicit matching-witness-size condition. All objections were resolved; four proposed model counterexamples were independently exercised. Fixes clarified basis versus collection scope, separate trade-off functions, Cartesian-product collection concatenation, actual expansion in contrast constraints, and a>=0 in the written LP (already enforced in code). The prompts, unchanged replies and complete resolutions are under [evidence/](evidence/), with the disposition in [referee-resolution.md](evidence/referee-resolution.md). Neither advice nor exact finite certification is treated as full original-problem resolution or novelty clearance.

For the continuation, a separate **Claude Opus5.5/max** no-tools review completed and found no fatal mathematical defect, conditional on the exact implementation coverage. Rational-probability transfer, padding and the five-case/six-length map were made explicit; existing full-dual and every-terminal-leaf checks meet its conditional requirements. The broad first attempt timed out and is not counted as a completed review. [Raw focused result](evidence/continuation-20261014/focused-review-stdout.json), [command and input hash](evidence/continuation-20261014/focused-review-command.json), and [all dispositions](evidence/continuation-20261014/review-resolution.json) retain the review scope and limitations. The successful reviewer did not execute the enumeration or audit the full implementation.

## Exact blocker and ranked next actions

1. **Original scientific blocker:** no all-access-structures quantitative/construction characterization of the four extrema and trade-off has been proved here. Even the optimum-contrast expansion in a threshold subfamily is tied to unresolved general design-existence mathematics. A larger finite sweep or another ILP formulation does not remove this obstruction.
2. **Finite collection blocker removed:** all five n5 gaps above are closed. The remaining substantive structural question is whether basis and collection finite-expansion trade-offs agree for arbitrary strong access structures, or whether a genuine full-distribution separation exists. A relaxation SAT assignment cannot answer it.
3. **Prior-art blocker:** obtain Shyu–Chen2015 and Arumugam–Lakshmanan–Nagar2014 lawfully and compare their detailed model and bounds. The former's primary retrieval returned a WAF challenge/HTTP418; the latter's PDF redirected to subscription preview. The [dated comparison](evidence/continuation-20261014/prior-art.json) makes no priority claim.
4. **Structural route:** the proved cone identity gives an exact all-m basis transformation and an all-model global-contrast law, but leaves the cone's fixed-m collection problem open in general. Seek an extraction theorem or a certified full-distribution separation rather than enlarge the already-complete n5 table.

## Files and reproduction

- [Complete n<=5 table](evidence/table-n5.csv); [n<=4 table](evidence/table-n4.csv).
- [All rational certificates and integer matrices](evidence/certificates-n5.json).
- [Independent verification results](evidence/verification-n5.json), [Mobius SMT queries](evidence/smt/).
- [Frozen first-pass collection bounds](evidence/collection-bounds.json), [universal collection SMT queries](evidence/collection-smt/): their five SAT relaxation rows are superseded only by the separate continuation, not edited into witnesses.
- [First-pass summary and published comparisons](evidence/summary.json); [continuation conclusions](evidence/continuation-20261014/conclusions.json).
- [Frozen first-pass derivations](work/model.md), [frozen protocol](pre_statement.md), [versions](work/requirements.txt), [first-pass run log](evidence/run-notes.md); the continuation proof is separate below.
- [Frozen first-pass acceptance receipt](evidence/acceptance.json): it binds the original package only, not this continuation or the updated README. It has deliberately **not** been resealed.
- [Full-distribution continuation inputs/results](evidence/continuation-20261014/), [proof and cone theorem](work/collection-continuation.md), [standalone exact verifier](work/verify_collection_continuation.py).

Each binary column mask T in a witness is repeated the stored number of times; bit i-1 is participant i's row. Uniformly permute the resulting columns when encoding. Thus the JSON contains concrete schemes, not just objective values.

```sh
# From this target directory. The heavy environment stays outside the synced tree.
uv venv --python 3.12.12 /Users/jinleic/jinleic-workspace/scratch/ai4s-visual-cryptography-optimality/venv-reproduction
uv pip install --python /Users/jinleic/jinleic-workspace/scratch/ai4s-visual-cryptography-optimality/venv-reproduction/bin/python -r work/requirements.txt
PY=/Users/jinleic/jinleic-workspace/scratch/ai4s-visual-cryptography-optimality/venv-reproduction/bin/python
# Replay existing certificates without depending on an LP/MILP solver's answers.
$PY work/verify.py evidence/certificates-n5.json --output evidence/replay-verification.json --queries evidence/replay-smt
# Independently rerun candidate discovery, if desired.
$PY work/solve.py --max-n 5 --output evidence/reproduced-certificates.json
$PY work/verify.py evidence/reproduced-certificates.json --output evidence/reproduced-verification.json --queries evidence/reproduced-smt
# Collection bounds can be replayed separately.
$PY work/collection_bounds.py evidence/certificates-n5.json --output evidence/replay-collection-bounds.json --queries evidence/replay-collection-smt
# Replay the NEW full-distribution collection exclusions separately (standard library only).
$PY work/verify_collection_continuation.py --output evidence/continuation-20261014/replay-verification.json
```

Do not run Python with `-O`. The scripts produce exact-verification assertions and recorded solver responses; all stated verification above was actually exercised with CPython3.12.12, not assumed from another interpreter's availability. The original experiment is tracked by campaign `20261014T084950Z_c585326d_3cdc4c499527`.
