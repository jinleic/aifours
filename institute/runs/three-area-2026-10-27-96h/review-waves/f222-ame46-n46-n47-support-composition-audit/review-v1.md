# f222 — AME(4,6) support composition audit

Reviewer: `ReviewF222AmeUnion`, same-harness. Native `/bin/date` observed **2026-10-29T13:49:39-0700 PDT** before this write; it is not a file-creation timestamp.

## Verdict and scope

**At the expressly adopted scopes of the seven pinned parent dispositions, with the stated classical and computational trust boundaries, the composition excludes support 46 and support 47. The recorded lower bound 45 and an actual 60-term witness then imply that the integer minimum support satisfies**

\[
 m\in\{45\}\cup\{48,49,\ldots,60\}.
\]

This is a set of **not-yet-excluded values of the minimum**, not a claim that each value is attained. In particular no 45-term state has been supplied or excluded by these inputs, and no global lower bound of 48 follows. A 60-term state is an adopted actual upper witness, not a claim that the minimum itself is 60.

The result is a **conditional union audit**, not a fresh proof/re-execution of the underlying dispositions. It inherits the classical no-OLS(6) theorem and the prior `t≤30` boundary, the f127 computer-enumerator reduction and coverage, and the remaining review-specific boundaries described below. No unlisted linked source, receipt, author PASS, held result, SAT/solver outcome, external source, or author communication was used as an additional premise. Same-harness support is not human, independent-model-family, formal/kernel, or novelty verification.

### Quantified findings, by claim

Columns give the number of FATAL / MAJOR / MINOR / INCONCLUSIVE findings for **that row**. A zero-finding in-scope row means that its composition is valid at the named imported scopes; it does not upgrade an import to an independently proved theorem.

| Claim audited | F / M / m / I | Result and exact limitation |
|---|---:|---|
| Common normalized state, one product basis, `P,E,N,t` and all six projections | 0 / 0 / 0 / 0 | Hypotheses match; all six projections refer to the same tensor and basis. |
| `N=46` forces `t=26` | 0 / 0 / 0 / 0 | `N≥72−t`, f113 `t≤29`, and f141's **N=46** exclusions; inherits f113's no-OLS and `t≤30` provenance. |
| f127 no-Hamming-one at `N=46,t=26` | 0 / 0 / 0 / 0 | Adopted lemma matches the forced case; conditional on no-OLS(6), not on alphabet 4444. |
| Ten-profile coverage and the nine f182 exclusions | 0 / 0 / 0 / 0 | Nine are accounted for exactly: 3444 by the recorded unitary argument, the eight with a 5 by f127 no-H1 plus f182; f182's non-clean-room control boundary remains. |
| Remaining 4444 exclusion | 0 / 0 / 0 / 0 | f127 applies at the same `N,t` and fixed tensor; depends on the reviewer-written finite enumerator and its reduction/coverage, not a formal certificate. |
| No support-46 state | 0 / 0 / 0 / 0 | Conditional composition of the preceding rows; not an independently replayed underlying exclusion. |
| No support-47 state | 0 / 0 / 0 / 0 | Directly adopted f214 composition: `N=47 ⇒ t=27`, and the separately adopted `N=47,t=27` exclusion stated there; inherits f113. |
| Optional consistency: `t≤28` | 0 / 0 / 0 / 0 | Explicit f214 parent composition; not needed to force `t=26` and inherits f113. |
| Global lower bound 45 | 0 / 0 / 0 / 0 | Adopted f107 statement at no-OLS(6) and its stated dependencies; its finite-only review did not itself establish the universal theorem. |
| Actual support-60 upper bound | 0 / 0 / 0 / 0 | Adopted f89 witness assertion and exact Gram-check statement imply a normalized 60-term state; literal coefficients/checker are not in these seven inputs and were not independently checked here. |
| Resulting possible-minimum set | 0 / 0 / 0 / 0 | Uses existence from the 60-term witness, lower45, and exactly the two exclusions 46 and 47. |
| Independent proof of classical no-OLS(6) | 0 / 0 / 0 / 1 | Imported, not reconstructed in the frozen dispositions or this audit. |
| Independent reproof of the prior `t≤30` and f113 chain | 0 / 0 / 0 / 1 | Adopted statements and their express provenance are used; their full linked bodies were not reviewed. |
| Independent verification of f127 enumerator coverage/correctness | 0 / 0 / 0 / 1 | No enumerator was opened or rerun; no independently checked formal certificate is supplied by the pinned disposition. |
| Independent reproof/clean-room verification of f182's eight detailed cases | 0 / 0 / 0 / 1 | Composition only; its original control was independently implemented but was not clean-room. |
| Independent literal reconstruction/check of all 60 witness coefficients | 0 / 0 / 0 / 1 | The parent states the 60-term and Gram results, but the literal coefficient table is not a declared input. |
| Existence at 45 or the exact minimum, including whether any particular 48–59 is attainable | 0 / 0 / 0 / 1 | Not decided by these inputs; the displayed set is an outer bound only. |
| Any family/general-`q` endpoint claim | 0 / 0 / 0 / 1 | All seven adopted inputs fix local dimension 6; no variable-`q` construction or theorem is supplied. |

**Totals:** 0 FATAL, 0 MAJOR, 0 MINOR, and 7 explicitly scoped INCONCLUSIVE stronger or independently unreplayed claims. These seven are not hidden premises and do not invalidate the stated conditional composition. The unsuccessful path lookup documented under reading coverage is an operational deviation without a scientific finding.

## Written reconstruction of the composition

### 1. Common objects and the `N=46` forcing

Fix **one** normalized complex AME(4,6) state and **one** local orthonormal product basis. For each of its three 2|2 flattenings the matrix `U=6ψ` is a 36×36 unitary; its row and column Gram identities together give the six pair marginals. These are three reshapes of the **same** tensor. Let `N` be its number of nonzero coefficients, `P` the set of coefficients of modulus exactly `1/6`, `t=|P|`, and `E` the remaining nonzero support. Thus `N=t+|E|` in this same basis.

In every cut a `P` entry has modulus one in `U` and is the only nonzero in its row and column. The `t` singleton rows and columns can be removed, leaving an `n×n` unitary, `n=36−t`, without singleton rows or columns: a residual singleton of modulus one would itself have belonged to `P`. Counting its nonzeros gives

\[
 |E|\ge 2n=2(36-t),\qquad N\ge 72-t.
\]

For `N=46` this gives integer `t≥26`. The f113 disposition expressly adopts `t≤29` for every normalized complex AME(4,6) state in every product basis. Its exclusion of `t=30` requires the separately supported `t≤30` result to give `t≤29`; the latter carries the unreplayed classical no-OLS(6) provenance. Hence `t∈{26,27,28,29}`. The f141 disposition excludes **exactly at N=46** the last three values by its stated unitary argument. Therefore any putative 46-term state must have `t=26`. This is a consequence of the two records together, not a premise of f127, and f141 alone still permits the larger counts recorded there.

At this forced point `n=10`, `|E|=20=2n`. Every residual row and column in each cut has degree exactly two. Equivalently, for each of the six coordinate pairs, `E` projects to 10 cells, and each such cell has exactly two extensions in the same `E`; each `P` word occupies its own distinct singleton pair cell. The normalization, support, `t`, coefficient threshold, and basis are identical to the hypotheses of f127 and f182.

### 2. No-Hamming-one premise and explicit ten-profile union

The f127 disposition asserts that for this very `N=46,t=26` tensor no two `E` words differ in exactly one coordinate. It imports no-OLS(6); the four-symbol alphabet hypothesis is **not** needed for this lemma. The recorded written route uses the three-cut two-regular residual, the isolated cubic block, and the `m=10,8,6` alternatives, with no-OLS used in the OA(36,4,6,2) completion case. We import the lemma at its adopted scope, not as a fresh proof of that classical theorem.

Let `r_i` be the number of symbols in coordinate `i` used by `E`, and sort the four `r_i`. f182 states that the local partner degree `d(a)=|E_a|/2` is independent of the chosen other party, is at least 2, and sums to 10 over symbols at each party. Thus `r_i≤5`; also every party uses at least two symbols. Since every pair projection has 10 cells, `r_i r_j≥10` for every pair. For sorted `r_1≤r_2≤r_3≤r_4`, the smallest product is `r_1r_2`; the integer possibilities are precisely:

| Sorted residual profile | Disposition eliminating it |
|---|---|
| `(2,5,5,5)` | f182, using f127 no-H1 |
| `(3,4,4,4)` | f182, actual unitaries; no no-H1 import for this case |
| `(3,4,4,5)` | f182, using f127 no-H1 |
| `(3,4,5,5)` | f182, using f127 no-H1 |
| `(3,5,5,5)` | f182, using f127 no-H1 |
| `(4,4,4,4)` | f127's separate finite branch exclusion |
| `(4,4,4,5)` | f182, using f127 no-H1 |
| `(4,4,5,5)` | f182, using f127 no-H1 |
| `(4,5,5,5)` | f182, using f127 no-H1 |
| `(5,5,5,5)` | f182, using f127 no-H1 |

To see completeness without a new enumerator: if the first size is 2, the second and hence all others must be 5; if it is 3, each other size is 4 or 5; if it is 4, each other size is 4 or 5; and if it is 5, all are 5. This yields `1+4+4+1=10` sorted profiles, including exactly one 4444 row and the nine other rows. Sorting only permutes party labels; it does not replace the actual joint support by independently chosen marginal realizations.

For 3444, f182 records activity sums 50 and 24, so `Σ(k−binom(k,2))=26`; the per-word upper bound 1 forces equality for all 26 `P` words, and the integer local-degree condition gives the recorded contradiction. For each of the other eight non-4444 profiles, at least one party has five size-two fibers. f182's adopted proof uses the **same-tensor** no-H1 condition to reduce their balanced binary-cube fibers to parity classes, then the recorded incidence/rank and degree-cap obstructions. Its parent expressly carries two corrections: degree lists need the degree cap in addition to the sum, and *all*, not merely some, of the relevant 3,600 checker pairs have the stated size-three type. These details are part of the imported scope; the unlisted underlying proof and checker have not been independently reconstructed here.

For the sole surviving 4444 row, f127 applies to the same normalized state, basis, `N=46`, `t=26`, and `E`. Its adopted branch conclusion combines no-H1 with the degree normal form and a finite unitary row-overlap check. In the parent's description, the reviewer enumerated 2,975 normalized all-Y patterns yielding 40 candidates, all failing the stated overlap necessity in all three cuts, and 240 one-X patterns with no compatible high fiber; the separately reported labeled counts are 39,304 patterns/512 failing candidates and 3,375 one-X patterns/no matches. Thirty of the 40 normalized candidates have cross-fiber distance one but were deliberately retained as a conservative superset. These are **reported inherited results**, not new observations of a run here. The conclusion requires the normal-form reduction and the enumerator to cover the asserted branch correctly. It is computer-assisted, not a formal certificate.

The f182 nine and f127 4444 statements exhaust the ten possibilities. Thus a putative support-46 state gives a contradiction, conditional on the accepted statements and trust boundaries. The f182 disposition did not itself adopt this last union; performing exactly this separately frozen audit supplies the logical composition, not a new replay of f127 or f182.

### 3. Independent `N=47` branch

For `N=47`, the same support count gives `t≥25` and residual excess

\[
 e=|E|-2n=(47-t)-2(36-t)=t-25.
\]

The pinned f214 parent disposition expressly adopts the reduction to `t=27`: `t=25` has odd `n` with zero excess, `t=26` has forbidden excess one, `t=28` conflicts with the recorded excess-three parity structure, `t=29` would give an excluded seven-dimensional residual with 18 entries, and `t≥30` is ruled out **only** via f113's `t≤29`. At `t=27` f214 separately states and adopts the `N=47,t=27` exclusion. Therefore its explicit parent composition excludes `N=47` at f113's no-OLS(6) and prior-`t≤30` boundaries. The f141 `t=27` exclusion cannot by itself be applied here: it assumes `N=46`, not 47. The f214 parent reports having read its reduction source's first 12 lines and the review completely, relying on that review for the source remainder; this audit has read only the f214 disposition and does not improve that provenance.

The same f214 disposition also explicitly composes f113 `t≤29` with an adopted all-support `t=29` exclusion to give `t≤28`. This is compatible with the `N=46` proof above, but is unnecessary for it. Linked underlying bodies are not additional premises in this audit.

### 4. Lower bound, actual upper witness, and minimum

The f107 lower45 disposition directly adopts, for every normalized complex AME(4,6) state and every local product basis, `N≥45` at the unreplayed no-OLS(6) import. It records use of the earlier lower44/`t≤30` chain and unitary-support, parity, shadow and actual-orthogonality arguments for `N=44`. Its two stated qualifications are that R34 requires its `(2,3,3)` degree hypothesis and that the two-ternary case needs the relevant actual row-overlap form. The finite review reported its **global theorem INCONCLUSIVE within the finite slice**; its finite checks do not replace the adopted universal written argument.

The f89 lower44 disposition expressly records a checked **actual** 60-distinct-nonzero tensor, not merely a bound conjecture. Its statement says that the unnormalized tensor `A` has row and column Gram `2I_36` over `Z[√2]` in all three 36×36 cuts, and that normalization is division by `√72`. If that adopted statement is accepted, then in every cut

\[
 (A/\sqrt{72})(A/\sqrt{72})^\dagger=I_{36}/36,
\]

and the corresponding column Gram is also `I_36/36`; the six two-party marginals are maximally mixed, and the squared norm is `36/36=1`. Nonzero scaling preserves the 60 distinct nonzero positions. Thus the stated tensor is a normalized AME(4,6) state with support exactly 60, so the set of such states and product bases is nonempty and its integer minimum exists with `m≤60`. This paragraph reconstructs the **consequence of the parent-stated Gram data**, not the literal coefficient table or the checker run: neither body is a declared input here. The parent also distinguishes its table-transcription check from a separate reported match to the public HTML; no external source was inspected for this audit.

Combining `m≥45`, `m≤60`, and the absence of any support-46 or support-47 state gives exactly the stated outer set `{45}∪[48,60]∩Z`. A support-45 state remains an open possibility on these inputs; consequently excluding 46 and 47 does **not** establish that every state has support at least 48. No value from 48 through 59 is asserted attainable, and no exact minimum is determined. The local dimension is fixed at 6 throughout; there is no variable-`q` endpoint premise in the seven records, and no extrapolation to other dimensions is justified.

## Inherited trust and documentary boundaries

1. **No-OLS and prior bound.** The classical nonexistence of two orthogonal Latin squares of order 6 is an unreplayed mathematical import. f89 derives the earlier `t≤30` and lower44 at this boundary; f113 combines that earlier bound with exclusion of 30 to obtain `t≤29`. f141's three exclusions at `N=46` are recorded as unitarity-only, but the forcing to `t=26` inherits f113. f127's no-H1 and 4444 conclusions are conditional on no-OLS; f182's 3444 case is stated unitarity-only, while its other eight use f127 no-H1. f214's 47 exclusion and `t≤28` inherit f113. f107 lower45 independently names the same classical import. The in-harness OLS search mentioned by f107 is supplementary, not a replacement classical proof.
2. **f127 computational and historical provenance.** The 4444 exclusion is computer-assisted and depends on the coverage/correctness of the reviewer-written enumerator and the mathematical reduction. The disposition reports that the historical reviewer did not read or run author programs, but that is a reported fact, not an observation by this reviewer and not independent-model-family or formal verification. The f127 disposition expressly says its receipt reported a match to the assigned candidate pin, but **no separate f127 manifest file was present in that review directory**. This f222 manifest pins the later parent disposition; it does not retroactively supply or prove the contents, freeze ordering, or existence of the missing historical f127 manifest. No receipt was opened as evidence here.
3. **f182 non-clean-room control.** The disposition says the reviewer independently implemented its controls after reading author checkers. Thus the control is not clean-room; its numerical outcomes support, but do not replace, the written cases or become a formal certificate. Its retained same-tensor and all-six-projection hypotheses are essential for this union.
4. **Earlier review qualifications.** f113's finite controls and the f141 finite checks are reported same-harness support rather than externally checked solver certificates. f107 explicitly marks its finite-only global theorem inconclusive, notwithstanding the parent's separate adoption of the written global lower45 result. f89's manifest-v3 qualification says lower44 uses `2n` and `2n+1`, not a separate `2n+2` classification; the latter was described there as an unreviewed lower45 dependency at that earlier time, while f107 later separately adopts lower45 with its own review and stated trust boundaries. No chronology is upgraded into a stronger prior review.
5. **Historical nonclaims are not contradictions.** f127/f141/f89/f107 and f182 state that later branches or compositions were not adopted at their respective times; f214's earlier possible-minimum set includes 46. Those are historical scoped dispositions, not assertions that 46 must remain possible after this separately frozen composition. The present audit does not alter those records or adopt unrelated successors, f161/f162 payloads, or a global `≥48` claim.
6. **Witness and scope limits.** The f89 parent assertion is the only imported actual-60 witness fact here. Its literal table, checker and receipt are outside the seven declared inputs, so their bytes, program, and calculation were not checked by this reviewer. Similarly, this audit neither reads the linked `N=47,t=27` body nor treats a bare author PASS as a premise: the proposition and its composition are expressly stated in the pinned f214 parent disposition.

## Actual input and execution record

The assigned manifest `review-waves/f222-ame46-n46-n47-support-composition-audit/manifest-v1.json` had measured SHA-256 `d3413126ea184e26df025b414da35fd7c3003297963b5e41c39eae4f0737ba94`, matching the assignment before its body was displayed. It was displayed in raw windows 1–15, 16–30, 31–45, 46–60, and 61–65. **Before any declared input body was displayed**, every input's complete bytes were measured against all three manifest pins; all SHA-256, byte and LF counts matched, and all seven files ended in LF. Each was then displayed in the following manifest order in the indicated raw windows, including its actual final line. All windows have at most 15 lines. `D/` abbreviates `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`.

| Order and source | Measured SHA-256 | Bytes / LF | Actually displayed raw line windows |
|---|---|---:|---|
| 1. `D/physics-6-maximal-coefficients29-parent-v1.md` | `86968ac972bf26f1f6cac6936bbccd23b27696487c96a9779be5ef0553723d9b` | 5473 / 28 | 1–15, 16–28 |
| 2. `D/physics-6-n46-unitary-bridge-t27-t29-parent-v1.md` | `b1d3face7eb8a06faec59031e62971c3054dbd99b9426087d73d882af3f30e40` | 4648 / 24 | 1–15, 16–24 |
| 3. `D/physics-6-n46-no-hamming-one-parent-v1.md` | `262a5a09276a2d7ef3ce350425236b29af327c99f8ea3ba03cf50878978baac0` | 5552 / 25 | 1–15, 16–25 |
| 4. `D/physics-6-ame46-n46-t26-nine-profile-exclusions-parent-v1.md` | `f9760843a45e8792aa98de0811d2b80c2dae8f4ae7e6f40ef1314c062fc952f4` | 4637 / 22 | 1–15, 16–22 |
| 5. `D/physics-6-ame46-support-47-excluded-and-at-most-28-maximal-coefficients-composition-parent-v1.md` | `4101ae2cdb08aa2c9238b680359dc2793bcccfc3af672fbb92be9dd460a41003` | 4423 / 17 | 1–15, 16–17 |
| 6. `D/physics-6-ame46-global-support-lower45-parent-v1.md` | `28ffc96f2b7295dd62c7efcfe39d066ac1a77449fbf0804a67c86cbce8c8a8cc` | 8441 / 34 | 1–15, 16–30, 31–34 |
| 7. `D/physics-6-ame46-global-support-lower44-parent-v1.md` | `c6e578a2555f476c45ac5e3e31753fceda1e855c1d5a3adf90847f477444d90a` | 8288 / 36 | 1–15, 16–30, 31–36 |

There was one failed lookup while requesting source 1's last window: the run directory year was mistyped as `20210`, the tool returned path-not-found and displayed no body, and the correctly spelled 16–28 window was immediately displayed before source 2. This did not omit or reorder any displayed input; it is disclosed rather than represented as a successful read. Mandatory workflow memory/skill material was read as process guidance, not as scientific evidence.

No mathematical reasoning or control preceded completion of the seven displays. **No scientific control was executed**: in particular no inherited enumerator was rerun and no author program was opened, imported, compiled, or executed. The manifest/input hashing and byte/LF measurements were metadata operations, not computational verification of the mathematical claims. There are consequently no scientific-control start/end clocks, source hashes, exit codes, or negative-control results to report. No Git, deletion, publication, external model/API, web search, solver, global execution, build, lint, test suite, or formatter was used. The full SHA-256 of this review is reported separately after its bytes are written.
