# f282 written-mathematics review v1

## Verdict and scope

**0 FATAL / 1 MAJOR / 2 MINOR. Overall: incorrect as written. Confidence: 0.99.**

The mutuality identities, their parity consequences, and the five-row profile table are supported in writing, but the table requires that **M actually be a permutation digraph**, equivalently that **both** the second and penultimate columns be permutations. The manuscript repeats the explicitly non-adopted one-column implication from f279, so its proposed exhaustive search interface is not justified as stated. The two MINOR findings are arithmetic errors in the diagnostic discussion. Parent disposition is reserved; this review makes no adoption decision.

Reviewed candidate: `frontier-20261029-distance-incidence-interface-14-types-v1.md`, 63 LF, SHA-256 `27931aa7829076d1af94e8d7765b81be73685429a42dc6ace30d87a48b3797fa`.

All mathematical consideration began only after the complete raw display of all five listed input/import bodies. The park handoff was read as routing/status metadata only; its assertions are not corroborating evidence.

## Findings

### MAJOR 1 — Require both boundary columns before using the permutation branch

**Location: manuscript LF26; consequences at LF28–40, LF46 and LF63.** Exact quote at LF26:

> Suppose case (A) of the dichotomy: the penultimate column is a permutation, so M is a fixed-point-free permutation of the n symbols. Then the mutual pairs of M are exactly its 2-cycles. Writing t = number of 2-cycles in the cycle decomposition of M:

A permutation penultimate column gives only out-degree one in M; the in-degrees are the second-column multiplicities and need not follow from this hypothesis. The permitted f279 disposition, LF15, expressly does not adopt this implication. Consequently, an array with permutation penultimate column but non-permutation second column has not been placed in a justified branch: LF26 assigns it to the permutation analysis, while LF46 restricts case (B) to a non-permutation penultimate column. There is no supplied T2-specific theorem ruling out that boundary configuration. The discrete repair is to define case (A) by **both boundary columns being permutations**, and case (B) by **at least one not being a permutation**; in the latter branch conclude a full source **or** full target, as appropriate, not necessarily both. Keep every profile-by-cycle-type conclusion explicitly conditional on case (A) so that LF63 cannot authorize pruning the unproved boundary case.

A written countermodel to the degree inference is the loopless digraph consisting of the five reciprocal pairs 0↔1, 2↔3, 4↔5, 6↔7, 8↔9 and the additional arc 10→0. It has eleven arcs and out-degree one everywhere, but in-degree two at 0 and zero at 10. It has five mutual missing pairs, so its associated count vector is (5,1,49), satisfying both global identities but absent from the five-row permutation table. This is a countermodel to the claimed inference and to deriving the five-profile restriction from those identities; it is **not** asserted to arise from a T2(11) array, and does not establish realizability of the omitted configuration.

### MINOR 1 — Correct the order-six diagnostic checksum to 24

**Location: manuscript LF55.** Exact quote:

> | T2(6) | A (M = three 2-cycles, t=3) | 3 | 0 | 12 | 6 ✓; 30 ✓ |

For the displayed vector, k1 + 2k2 = 0 + 2·12 = 24 = 6(6−2), not 30. The first check, 2k0+k1=6, is correct. Replace the second checked total by 24; this is a transcription/arithmetic defect in a labelled diagnostic, not a refutation of Theorem 2 or of the displayed vector.

### MINOR 2 — Use n/2 for the all-two-cycle extremum

**Location: manuscript LF59.** Exact quote:

> The n=4, n=6 rows realize the t = C(n,2) extreme (M all 2-cycles).

Here t is the number of two-cycles of a permutation, so an all-two-cycle permutation at even order has t=n/2, not C(n,2). In the two displayed rows the values are respectively 2 and 3, whereas C(4,2)=6 and C(6,2)=15. Replace the quoted extremum by t=n/2. The five-profile table itself does not contain this error.

## Independent written reconstruction

### 1. Framework and boundary identities

Use the supplied definition of a linear T2(n): n permutation rows on n symbols; all directed distance-one events are distinct and all directed distance-two events are distinct. Positions are 0 through n−1, with no wrapping. The following counts concern n≥2. Write α_j(x) for the number of occurrences of x in column j; the manuscript’s α9 is the penultimate multiplicity at n=11, and becomes α_(n−2) at general n.

There are n(n−1) distance-one events and exactly that many ordered pairs of distinct symbols. Injectivity therefore makes distance one complete. For a fixed x, its outgoing distance-one count is n−α_(n−1)(x), and its incoming count is n−α_0(x). Both equal n−1. Hence the first and last columns are permutations.

Let M contain an arc x→y precisely when the ordered distance-two event (x,y) is absent. It is a simple loopless digraph. A fixed x produces an outgoing distance-two event in every row except those placing it in the last two columns. Thus its outgoing event count is n−1−α_(n−2)(x), and

\[
\operatorname{outdeg}_M(x)=\alpha_{n-2}(x).
\]

Similarly its incoming event count is n−1−α_1(x), giving

\[
\operatorname{indeg}_M(x)=\alpha_1(x).
\]

There are n(n−2) distinct distance-two events among n(n−1) possible ordered pairs, so |M|=n. This reconstructs the boundary law imported from I279 without the invalid extra inference about in-degrees.

For an unordered pair {x,y}, at most one event in each orientation can occur, by distance-two injectivity. The two opposite orientations cannot both occur within a single permutation row. Hence its number of distance-two row occurrences is 0, 1 or 2, with the last case using the two different orientations in different rows. In M these three cases correspond respectively to two reciprocal arcs, one arc, or no arcs. Therefore

\[
k_0+k_1+k_2=\binom n2,
\]

\[
k_1+2k_2=n(n-2),
\]

by counting distance-two events, and

\[
2k_0+k_1=n,
\]

by counting missing ordered pairs.

Solving gives k1=n−2k0 and k2=C(n,2)−n+k0. In particular k1≡n mod 2. This proves odd k1 at every odd n, including 11, and even k1 at n=8. These conclusions do not use a permutation hypothesis on either boundary column.

### 2. What the identities alone do and do not force

Non-negativity gives 0≤k0≤floor(n/2), in addition to k2≥0. At n=11 the identities alone leave the six numerical possibilities

\[
(0,11,44),\ (1,9,45),\ (2,7,46),\ (3,5,47),\ (4,3,48),\ (5,1,49).
\]

This is a list of nonnegative integer solutions to the count equations, **not** a realizability theorem. In particular the identities alone do not remove the last vector. The graph in MAJOR 1 shows that even adding out-degree one everywhere does not remove it at the degree-theory level.

At n=8 the identities leave

\[
(k_0,k_1,k_2)=(s,8-2s,20+s),\qquad s=0,1,2,3,4.
\]

Thus they force even k1, but do not force k0=0 or k1=8. For example, a loopless permutation digraph made of four two-cycles has the abstract vector (4,0,24), which obeys the same equations. This is again a graph/count countermodel, not a claimed order-eight T2 square.

At n=21 the equations are k1=21−2k0 and k2=189+k0; the displayed (0,21,189) needs additional information setting k0=0. Oddness alone does not do so.

### 3. Correct exhaustive boundary split

The degree formulas prove the exact equivalence

\[
M\text{ is a fixed-point-free permutation digraph}
\iff
\alpha_{n-2}\equiv1\ \text{and}\ \alpha_1\equiv1.
\]

The absence of fixed points follows from the absence of loops. If α_(n−2) is not identically one, its n nonnegative integer entries sum to n, so some entry is zero and some is at least two. A zero gives a full source. The same argument for α_1 gives a full target when the second column is not a permutation. Thus the exhaustive complementary branch is **full source or full target, possibly both**. A non-permutation in one boundary column alone does not prove non-permutation in the other.

This is precisely the repaired scope of I279 LF15. The bare penultimate-column dichotomy is valid, but its permutation side cannot be promoted to the permutation-M analysis without the second-column condition.

### 4. The conditional permutation table

Assume M is a permutation digraph. Its reciprocal unordered pairs are exactly its two-cycles. If their number is t, then

\[
(k_0,k_1,k_2)=\left(t,n-2t,\binom n2-n+t\right).
\]

At n=11 every cycle has length at least two. Grouping all partitions of eleven by their number t of parts equal to two gives:

| t | Complete cycle-type list | (k0,k1,k2) |
|---|---|---|
| 0 | 11; 8+3; 7+4; 6+5; 5+3+3; 4+4+3 | (0,11,44) |
| 1 | 9+2; 6+3+2; 5+4+2; 3+3+3+2 | (1,9,45) |
| 2 | 7+2+2; 4+3+2+2 | (2,7,46) |
| 3 | 5+2+2+2 | (3,5,47) |
| 4 | 3+2+2+2+2 | (4,3,48) |

For completeness, after removing all t two-cycles, the residual parts have size at least three. Their totals are 11,9,7,5,3 for t=0,1,2,3,4; their partitions are exactly the lists displayed. t=5 would leave a forbidden part of size one. The row counts 6+4+2+1+1=14 account for every fixed-point-free cycle type. Therefore the manuscript’s table and its collapse to five profiles are correct under the stated conditional hypothesis.

An 11-cycle has t=0, hence no never-occurring pair, eleven asymmetric pairs and forty-four pairs occurring in both directions. Type 3+2+2+2+2 has t=4, hence four never-occurring pairs, three asymmetric pairs and forty-eight pairs occurring in both directions. These are necessary count consequences if an array of the specified type exists. No type is proved realizable or excluded.

### 5. Sub-branch A1 and the precise import boundary

The endpoint map E takes the first symbol of each row to its last symbol. Since both endpoint columns are permutations, E is a fixed-point-free permutation. If M=E⁻¹ as directed permutation graphs, then M and E have exactly the same two-cycles: inversion reverses a cycle, and a two-cycle is its own inverse. Consequently k0 equals the number of two-cycles of E. This conclusion is supported directly and does not require the f204 symmetry theorem.

There is also a direct interpretation of the circular-completion condition under the usual operation of adjoining one common new symbol ∞ to every row and regarding the extended row as a directed circle. The new distance-one events are last→∞ and ∞→first; these are complete because the endpoint columns are permutations. The additional distance-two events are penultimate→∞, last→first and ∞→second. The middle family is exactly E⁻¹, and the other two families are complete precisely when the two boundary columns are permutations. Hence M=E⁻¹ makes those added events fill exactly the missing events and implies the necessary boundary permutations by the degree laws. Conversely, such a perfect directed circular completion must fill M by those last→first events. This explains the structural identification, with the completion operation made explicit.

The further symmetry-class assertion “Aut ∈ {1,2,3,6} for such extensions” at manuscript LF42 is retained **only conditionally on the named adopted f204 scope**. No f204 body or full statement is among the manifest-permitted imports, and none was opened. This review does not independently reconstruct its hypotheses, its definition of Aut, or that classification. The count identities do not imply the classification.

The actually permitted I175 Theorem A concerns symbol automorphisms of the **linear** row set. Its proof reconstructs as follows. Such a group acts freely on the p distinct permutation rows, since fixing an ordered row fixes every symbol. Its order divides p; if nontrivial, it has order p and, after relabelling, acts by translations of Z_p. All rows are translates of one base row. Repeated consecutive differences in that row would give repeated distance-one events among its translates. Thus the differences exhaust the nonzero residues, whose sum is zero at odd p. Telescoping then equates the two endpoints of the base row, a contradiction. Hence the linear symbol group at p=11 is trivial. This neither supplies the missing boundary implication nor identifies the automorphism group of an unrooted circular extension.

### 6. Diagnostics and the odd-order import

The four displayed vectors have the following purely arithmetic status:

| Diagnostic label | Vector | 2k0+k1 | k1+2k2 | Status in this review |
|---|---|---|---|---|
| T2(4) | (2,0,4) | 4 | 8 | Numerically consistent; pinned-row attribution not replayed |
| T2(6) | (3,0,12) | 6 | 24 | Numerically consistent; manuscript checksum 30 is wrong |
| six T2(8) | (0,8,20) | 8 | 48 | Numerically consistent; common profile not proved by identities |
| T2(21) | (0,21,189) | 21 | 399 | Numerically consistent; identities alone do not set k0=0 |

No pinned array file was permitted or opened, and the author’s claim to have recomputed these profiles is not reviewer evidence. I187 separately supplies the conditional adopted construction and the conditional order-eight census. Its statement that all six normalized order-eight squares have non-permutation second/penultimate columns supports their repaired case-(B) label under that import; it does not supply their k0 values here.

One can distinguish an additional abstract consequence of the permitted order-21 construction from its unverified diagnostic cycle label. In an imported group-table T2 of odd order 21, the rows are all left translates of a base permutation. Its nineteen distance-two quotients are distinct and nonidentity, so exactly one nonidentity quotient q is missing. Left translation makes M exactly x→xq. Because a group of odd order has no element of order two, this M has no two-cycles. Thus the profile (0,21,189) follows **conditionally on I187’s group-table T2 construction**, without using the author’s pinned-row computation. Determining that M has specifically three seven-cycles would require determining q’s order; the imported endpoint cycle type 7³ is a statement about E, not by itself about M. That finer M diagnostic is not established here.

The imported existence of a linear odd-order T2(21) is not re-proved from raw rows or terrace words in this wave. It is not a witness at order 11, does not prove a general endpoint-involution law, and does not alter the unresolved order-eleven existence question.

## Per-claim disposition table

Here “SUPPORTED” means written support at the hypotheses explicitly listed, not a parent adoption decision. Named imports remain conditional at their frozen scope.

| Claim and manuscript location | Disposition | Exact supported scope / limitation |
|---|---|---|
| Lemma 1, LF9–16 | SUPPORTED | Linear permutation rows and distance-two injectivity give n2∈{0,1,2}, with opposite orientations in the last case |
| Theorem 2 and parity, LF18–20 | SUPPORTED | Every linear T2(n), n≥2; no boundary-permutation assumption |
| Boundary law, LF22 | SUPPORTED; conditional import I279 also named | Out-degree is penultimate multiplicity, in-degree is second-column multiplicity; \|M\|=n; general-n index is n−2 |
| “penultimate ... so M ... permutation”, LF26 | REFUTED as a degree-theory inference; T2-specific strengthening UNPROVED | Both boundary columns are required under the supplied results; no actual T2 counterexample is claimed |
| Theorem 3, LF28 | SUPPORTED CONDITIONALLY | M must actually be a fixed-point-free permutation digraph |
| Fourteen types / five profiles, LF30–38 | SUPPORTED CONDITIONALLY | Exactly the permutation-M branch at n=11; not an exhaustive list from the identities alone |
| Two example readings, LF40 | SUPPORTED CONDITIONALLY | If the specified M cycle type occurs |
| A1 equality k0=#two-cycles(E), LF42 | SUPPORTED CONDITIONALLY | M=E⁻¹; circular identification uses the explicit adjoining-∞ operation described above |
| A1 automorphism classification, LF42 | CONDITIONAL IMPORT: f204; not independently adjudicated | f204 body is not permitted in this wave; its precise adopted symmetry scope must remain attached |
| Case (B) degree/parity conclusions, LF46 | SUPPORTED after the MAJOR 1 boundary repair | Complement of both-boundary-permutation case; full source or full target, not necessarily both |
| T2(4) and T2(6) diagnostics, LF54–55, LF59 | INCONCLUSIVE as pinned-row computations; arithmetic checked | Correct vector arithmetic apart from checksum 30 and stated extremum C(n,2); no census proof from identities |
| Six T2(8) common profile, LF56 and LF59 | INCONCLUSIVE as a profile census; case label conditional on I187 | k1 is provably even; k0=0 is not forced by these identities |
| T2(21) vector and three-seven-cycle M label, LF57 and LF59 | Vector SUPPORTED conditionally on I187 group construction; finer M cycle label INCONCLUSIVE | Identities alone do not force the vector; E’s cycle type cannot substitute for M’s |
| I175 Theorem A relevant to n=11 | SUPPORTED in writing at the imported linear-symbol-action scope | Trivial linear symbol group does not identify circular-extension Aut or boundary multiplicities |
| Proposed exhaustive search interface, LF63 | NOT JUSTIFIED as written; supported only after MAJOR 1 repair | Preserve the full-source/full-target complement and all conditional hypotheses; no new obstruction or witness |
| T2(11) remains open, LF63 | SUPPORTED as the limitation of these results | No existence, nonexistence, realizability or exclusion conclusion has been obtained |
| Park handoff, all 22 LF | STATUS-ONLY / NON-EVIDENCE | Read for routing; its “proved” list and diagnostics were not treated as independent mathematical support |

## Coverage and integrity receipt

### Manifest

Path: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f282-tuscan-distance-incidence-interface/manifest-v1.json`.

Observed SHA-256: `79e724529956c3795e940cf342f66278c9899d24f5dfcfe0c63526067b2b4519`; observed bytes: **5135**; observed LF: **58**. All match the assignment. Metadata was verified before opening the manifest body.

Complete exact raw display windows, in order: **1–15; 16–30; 31–45; 46–58**. The last window includes the actual closing brace and ending. Every window was at most 15 LF.

### Input identifiers and verified metadata

**C — manuscript**

Path: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/frontier-20261029-distance-incidence-interface-14-types-v1.md`.

SHA-256: `27931aa7829076d1af94e8d7765b81be73685429a42dc6ace30d87a48b3797fa`; **6186 bytes / 63 LF**.

**H — status-only park handoff**

Path: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/park-v3-addendum-6.json`.

SHA-256: `aa0055b2b4b70e64c94d55b095c6a5bd890d1975f97afe3d877642135d2ec074`; **2004 bytes / 22 LF**.

**I279 — adopted boundary disposition, with non-adopted Theorem 4(A) boundary**

Path: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-4-tuscan-sign-coset-theorem-and-repaired-boundary-dichotomy-parent-v1.md`.

SHA-256: `f8926010da34cb4460fd4b172e74a310b1629311499c7a3ceccb7c08c5464f82`; **3853 bytes / 17 LF**.

**I175 — adopted odd-prime symbol-asymmetry disposition**

Path: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-4-tuscan-odd-prime-symbol-asymmetry-and-orbit-counts-parent-v1.md`.

SHA-256: `20b187f303624afe0423fb4042b34a028f4cbdd3cc5577759bb709765e42d5eb`; **5995 bytes / 22 LF**.

**I187 — adopted odd-order-21 construction disposition**

Path: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-4-tuscan-odd-order-21-exists-and-refuted-boundary-shortcuts-parent-v1.md`.

SHA-256: `a1955a3953295908c556ad44b6bd6240c4dad3dff6cbfd916f63a0ea8d4a032d`; **4900 bytes / 22 LF**.

All five SHA-256, byte and LF values were observed to match the manifest **before any of their bodies was opened**. The combined input/import totals were **22938 bytes / 146 LF**. Only the manifest’s five listed bodies were opened as review evidence; links and filenames inside them were not followed.

### Every input display window, in actual display order

| Sequence | Body | Exact raw LF window |
|---|---|---|
| 1 | C | 1–15 |
| 2 | C | 16–30 |
| 3 | C | 31–45 |
| 4 | C | 46–60 |
| 5 | C | 61–63, actual ending included |
| 6 | H | 1–15 |
| 7 | H | 16–22, actual ending included |
| 8 | I279 | 1–15 |
| 9 | I279 | 16–17, actual ending included |
| 10 | I175 | 1–15 |
| 11 | I175 | 16–22, actual ending included |
| 12 | I187 | 1–15 |
| 13 | I187 | 16–22, actual ending included |

There were no other body-display windows or rereads. Every listed window used the exact `:raw` selector, so no automatic surrounding context was added. All 146 declared input/import LF were displayed, including every actual ending, before any mathematical consideration, mathematical note-taking or comparison between the inputs.

## Native-clock observations, controls and process disclosures

These are observations of `/bin/date -u`, not inferred creation times or backdated events:

| Observation | Phase |
|---|---|
| 2026-10-30T03:34:26Z | Before manifest metadata verification |
| 2026-10-30T03:34:26Z | After manifest metadata verification; before manifest display |
| 2026-10-30T03:35:17Z | Before verifying all five input/import metadata records |
| 2026-10-30T03:35:17Z | After those verifications; before input-body displays |
| 2026-10-30T03:36:09Z | After the final I187 ending was displayed; before mathematical reconstruction |
| 2026-10-30T03:41:41Z | Before review drafting/output phase |

The two metadata shell calls used `shasum -a 256` and `wc -c -l`, with `/bin/date` before and after and a 120-second tool timeout. Both returned normally with matching values and no timeout or command error. They performed no mathematical computation. The later shell calls only observed the native clock. No author script, mathematical program, build, test suite, SAT solver, DRAT checker, network request or external model was run. There are no reviewer-owned executable controls or control artifacts to claim as additional evidence; the countermodels and arithmetic above are written reconstructions, not machine checks.

**Additive startup-order disclosure:** mandatory harness preflight reads of `memory://root/memory_summary.md` and `skill://aifours-written-math-acceptance-protocol` preceded manifest verification. No native clock was observed before those two preflight reads; the first observed clock is recorded above. They were not used as mathematical evidence. Accordingly this review does not claim literal session-wide manifest-first or manifest-only access. After that preflight, manifest verification preceded its display, all five evidence bodies followed the manifest order, and the absolute all-displays-before-mathematics boundary was observed. This disclosure is not a claim that a sequencing exception has been waived; process disposition remains the parent’s responsibility.

No sibling review, prior wave output, held/withdrawn/ZERO/quarantined body, author script, raw pinned array, f204 source or linked external resource was opened. No frozen input, manifest, disposition, ledger or README was modified. The review preserves the unsupported cases rather than silently deciding them.

## Assurance boundary

This is a **same-harness written-mathematics review**, with metadata integrity checks and explicit conditional imports. It is not human review, independent-model-family review, formal/kernel verification, an executable replay of the pinned arrays, a novelty audit or a parent adoption. The identified gap is a missing implication in the exhaustive boundary reduction, not an asserted T2(11) counterexample. Nothing in this review establishes a witness, a no-go theorem, or exclusion of any actual order-eleven profile or boundary case.

## Additive output receipt

The attempted write to the assigned wave’s `review-v1.md` was refused because the available write tool permits only `xd://` device transport and `local://` session scratch, not repository paths. No alternative filesystem write was attempted. The native clock observed after the refusal was **2026-10-30T03:45:39Z**. This complete in-channel review is supplied under the manifest’s explicit fallback provision for parent materialization.
