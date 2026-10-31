# F896 author candidate: exact forced-selector and weighted-incidence engine for composite original gcd 18..30

**Status.** Prospective GENERAL AUTHOR candidate under owner addendum 2. It consists of this narrative and ONE new, complete, **UNRUN** standard-library source, `exact-composite-selector-incidence-v1.py`, in this wave directory. I did not run, compile, test, import or hash it. Consequently this document reports **no** per-g outcome, count, timing, passing control or certificate for any target gcd: every statement about what the program "reports" is a specification. The written reduction and closure rules below are author mathematics awaiting a disjoint check. A parent full source read and a **separate** one-shot GO (outer wall limit ≤55 s; internal cooperative limit 38 s ≤ 40 s) are required. `INCOMPLETE` is never `PASS`. No family/human/formal acceptance, priority, novelty or global theorem is claimed.

## 1. Quantifiers and the actual objects

Let `n>14` and let actual sets `P,Q ⊆ Z_n` satisfy `P⊕Q=Z_n` (every residue has exactly one ordered representation), with the literal anchors

`A={0,3,8,11} ⊆ P`, `S={0,1,7,13,14} ⊆ Q`.

Assume **additionally** (it is not implied by the anchors) an actual direct factorization of the ORIGINAL head `P={u,u+d}⊕C_0`, `d≢0 (mod n)`, and put `g=gcd(d,n)` in the original cyclic group. The target values are exactly

`g ∈ G_T = {18,20,21,22,24,25,26,27,28,30}`

(the composite values in `18..30`; this candidate makes no statement about `19,23,29`, which are prime and covered by the separately written S1/S5/S6 Theorem A as a conditional import, nor about any `g>30`).

**Reduction (reconstructed from the actual objects, following S5 §1, S6 §1, S7 §1, S8 §1).** Absorb `u`; since `0∈P`, if the representation of `0` uses the element `d` of the two-point factor, replace `(d,C)` by `(−d,C+d)`. This preserves `P`, `Q` and `g` and gives `P={0,d}⊕C` with `0∈C`. Then `T=C⊕Q` is an actual direct sum and `{0,d}⊕T=Z_n`, so `1_T(x)+1_T(x−d)=1` for all `x`. Each `d`-cycle has length `n/g`; alternation forces `n/g` even, so `2g|n`, `d/g` is odd, `gcd(2d,n)=2g`, `d≡g (mod 2g)`, and `T` is a union of complete fibres modulo `m=2g`. Its image `V⊂Z_m` contains exactly one element of every antipodal pair `{r,r+g}`. With `L=n/m>0` and ORIGINAL-element counts `c_i=#{c∈C: c≡i (mod m)}`, `q_j=#{q∈Q: q≡j (mod m)}`, directness of `C⊕Q` and completeness of the fibres give, for every `s∈Z_m`,

`(W)   Σ_{i∈Z_m} c_i q_{s−i} = L·1_V(s).`

All `c_i,q_j` are nonnegative integers. Necessary positivity: `c_0>0`; `q_s>0` for `s∈S mod m`; each anchor `a∈{3,8,11}` has its actual `C` representative `c_a` with `a=c_a+e_a d`, so `c_a ≡ a` or `a+g (mod m)` carries a positive count. No unweighted quotient tiling, unit multiplicity or independent CRT sign is assumed; (W) is the only coefficient identity used.

## 2. Exact closure rules (decisive written identities)

Throughout, `C_f ⊆ supp(c)` and `Q_f ⊆ supp(q)` denote residue sets already proved positive, initially `C_f=I={0,p_3,p_8,p_11}` (one chosen residue `p_a∈{a,a+g} mod m` per anchor) and `Q_f=S mod m`.

**(R1) Selector.** `V` is an antipodal selector with `S⊆V` and, for each `i∈C_f`, `i+S⊆V` (positive `c_i q_s` lands in row `i+s`, whose right side must be `L≠0`). Hence `F=⋃_{i∈I}(i+S) ⊆ V`. If `F` contains an antipodal pair, the anchor choice `I` is impossible.

**(R2) Necessary supersets.** `supp(c) ⊆ C*(V,Q_f)=⋂_{j∈Q_f}(V−j)` and `supp(q) ⊆ Q*(V,C_f)=⋂_{i∈C_f}(V−i)`, since `c_i q_j>0` forces `i+j∈V`. These are coordinatewise supersets; optional residues in them may be zero.

**(R3) Row support.** For every `s`, the set `E_s={(i,j): i∈C*, j∈Q*, i+j≡s}` contains every pair that can contribute to row `s` of (W); all omitted pairs have zero product.

**(R4) Singleton propagation.** If `s∈V` and `E_s={(i,j)}`, then (W) reads exactly `c_i q_j=L>0`; so `i∈C_f`, `j∈Q_f` may be added. Supersets are recomputed (they only shrink), and this repeats to a fixpoint (monotone on finite sets).

**(R5) Forced outside superset.** If some `i∈C_f` is not in `C*(V,Q_f)`, then for some `j∈Q_f`, `c_i q_j>0` lies in a row outside `V`, whose right side is `0` — contradiction. Symmetrically for `Q_f`.

**(R6) Empty occupied row.** If `s∈V` and `E_s=∅`, row `s` of (W) reads `0=L>0` — contradiction.

**(R7) Strict positive cycle.** For a pair `(i,j)` with `i∈C_f, j∈Q_f` in an occupied row `s`, nonnegativity of the other terms gives `c_i q_j ≤ L`; if row `s` contains a *second* pair `(i',j')≠(i,j)` with `i'∈C_f, j'∈Q_f`, then `c_i q_j ≤ L − c_{i'}q_{j'} < L`. A singleton occupied row gives `c_i q_j = L`. Put `x_i=c_i` and `z_j=L/q_j` (positive rationals for forced residues). Then the three row facts read `x_i ≤ z_j`, `x_i < z_j`, `x_i = z_j`. Encode `v ≤ u` as a directed edge `u→v` (an equality contributes both directions). A directed cycle through at least one strict edge yields `w < w` for its start `w` — a contradiction using only (W), positivity and nonnegativity. This is precisely the f870/F869 two-cycle when the cycle has four edges, e.g. S8 `g=15,h=5`:

`z_0 > x_0` (row 0: `c_0q_0 + c_23q_7 ≤ L`), `x_0 = z_14` (row 14: `L=c_0q_14`), `z_14 > x_11` (row 25: `c_11q_14 + c_18q_7 ≤ L`), `x_11 = z_0` (row 11: `L=c_11q_0`).

**Completeness of the case split.** For an actual configuration, let `p_a` be the residue of the actual representative of anchor `a`. Then `I={0,p_3,p_8,p_11} ⊆ supp(c)` and `V ⊇ F(I)`. So every actual configuration lies in at least one enumerated case `(I,V)`: `I` ranges over the `2^3` choice products and `V` over all selectors containing `F(I)`, i.e. `F` plus one element of each pair untouched by `F`. A case closed by (R1), (R5), (R6) or (R7) has no actual configuration; hence if every case closes, the factor with that original `g` is impossible. A case that does not close is reported with its complete residual system (§3), which is necessary only, not a construction.

## 3. What the prepared source does (specification; unrun)

1. **Literal F870 regression** (`literal_f870_s8_cases`): enumerates `g=15,16` and requires exactly the four S8/S9 cases (selector, forced `C` residues), checks the four S8 supersets `C*(V,S)`, `Q*(V,I)` literally, requires the engine to find a strict cycle on `g=15,h=5`, independently validates the literal S8 four-edge cycle above, and runs the intended-reason mutants on that literal certificate.
2. **Regression `g=1..16`** with the full engine. Expectations taken from packet statements (S2 table, S6 §§2–3, S7, S8): `g∈{1,2,3,4,5,6,7,9,12,13,14}` must yield `NO_SELECTOR_SURVIVES` (tail antipodes or forced-translate antipodes), and `g∈{8,10,11,15,16}` must yield every case closed. A mismatch is `FAIL` with the offending g; it would be a discrepancy to investigate, not a refutation of a packet statement or of the target.
3. **Brute-force enumeration cross-check** for `g∈{15,16,18,20}`: an independent scan of all `2^g` antipodal selectors, collecting all `(I,V)` with `S⊆V` and `p_a+S⊆V`, must equal the forced-first enumeration as a set.
4. **Actual non-target fixtures** (`ACTUAL_DIRECT_TILING_NON_TARGET`): for every `g∈{15,16}∪G_T`, `n=4g`, `d=g`, `C={0,2g}`, `Q={0,…,g−1}`, `P={0,g,2g,3g}`; and `n=32,d=3,C={0,8},Q={0,2,4,6,16,18,20,22}`, `P={0,3,8,11}` (S8 §4). Each checks actual ordered directness of `P⊕Q`, directness of the factor and of `C+Q`, alternation, full fibres, the selector property and every weighted coefficient of (W); it requires at least one anchor family to be missing (never a target). It then runs the engine on the fixture's own actual supports as `C_f,Q_f` and **requires no closure** (`SOUNDNESS`): an actual solution of (W) must survive (R4)–(R7).
5. **Targets** `g∈G_T`, in increasing order. For each `(I,V)` case: (R1) validation; the f870-style cycle search with only `C_f=I`, `Q_f=S` (reason `STRICT_POSITIVE_CYCLE_INITIAL_FORCED`); otherwise the propagation engine (R4)–(R7) (reasons `FORCED_C_OUTSIDE_SUPERSET`, `FORCED_Q_OUTSIDE_SUPERSET`, `EMPTY_OCCUPIED_ROW`, `STRICT_POSITIVE_CYCLE_AFTER_PROPAGATION`) or `RESIDUAL`. Every cycle is re-validated edge by edge from an independent `O(m²)` per-row filter with recomputed supersets; every propagation step is replayed (each new forced residue must come from an independently recomputed singleton row); every residual row system is compared with the independent filter.
6. **Per-g report**: `NO_SELECTOR_SURVIVES`, `ALL_CASES_STRICT_POSITIVE_CYCLE`, `ALL_CASES_CLOSED_MIXED_EXACT_REASONS` (with counts per reason), or `RESIDUAL_EQUATIONS_REMAIN`, plus enumeration statistics (anchor picks, picks with forced antipodes, free pairs, selectors, duplicates), up to 64 listed closed cases (the first 8 with complete row equations) and up to 64 residual cases with **every** row equation `Σ_{(i,j)∈E_s} c_i q_j = L` or `= 0`, each term flagged `F` (both factors forced positive) or `O` (optional, nonnegative). `listing_truncated` marks a cap on listing only; every case is still analysed and validated.
7. **Intended-reason mutants** (on the literal S8 certificate and on the first cycle-closed case of every g that has one): `add_antipode_of_zero→SELECTOR_ANTIPODAL`, `swap_away_tail_zero→TAIL_ANCHOR_MISSING`, `remove_anchor_three_residues→HEAD_ANCHOR_3_MISSING` (both choices removed, never residue 0), `drop_closing_edge→CYCLE_NOT_CLOSED`, `mark_every_edge_nonstrict→NO_STRICT_EDGE`, `unforce_strict_remainder→STRICT_REMAINDER_NOT_FORCED`, `extra_singleton_incident_pair→SINGLETON_INCIDENCE` (recorded `NOT_APPLICABLE_NO_FREE_RESIDUE` if no admissible extra pair exists), `drop_optional_or_forced_term→ROW_TERMS_INCOMPLETE`. Any wrong reason or accepted mutant is `FAIL`.
8. **Status semantics**: overall `COMPLETE` (exit 0) only if every section completes without violation; deadline, signal or the per-g enumeration cap `2^16` gives `INCOMPLETE` (exit 2, never PASS); any failed check or mutant gives `FAIL` (exit 1); unexpected exceptions `ERROR`. One JSON object on stdout; no files, subprocesses, network, randomness or floating point.

**Author expectations, not results.** By hand I counted, for `g∈{26,27,28,30}`, that the translates `S, 3+S, 8+S, 11+S` occupy 20 distinct antipodal pairs, so no anchor choice conflicts and the forced-first enumeration should visit `8·2^{g−20}` selectors (512, 1024, 2048, 8192); for `g=24,25` the lower choice for anchor 11 meets the antipode of `0` (`11+13=24`, resp. `11+14=25`), leaving 4 picks. These are unreviewed mental counts used only for a time estimate (well inside 38 s by my estimate); the program asserts none of them.

## 4. Boundary cases and conditional imports

* Coincidences modulo `m`: residues of anchors and tail are reduced mod `m`; for target `g≥18`, `m≥36` and the five tail residues are distinct. The two choices for one anchor are distinct residues; different anchors may share residues (e.g. at `g=8`, anchors 3 and 11 have the same choice set) and duplicate `(I,V)` keys are merged.
* Rows outside `V` may contain optional pairs; (W) forces their products to be zero, recorded as residual `= 0` equations, never as positive information.
* The strict rule uses only forced positive pairs; positivity obtained from a singleton row is used for strictness only after propagation.
* Imports: prime `g` (S1/S5/S6 Theorem A) and `g≤14` (S2) are not needed for any target and are not used; regression expectations quote S2/S6/S7/S8 statements only as finite comparators. The coprime-cardinality graph route, the RSS/pure-letter bridge, printed-problem correspondence and all linked-but-unlisted bodies are not used. No missing load-bearing body is imported.

## 5. Result limits

Even after a separately authorized complete run, a target `g` reported as fully closed would be an exact finite case exhaustion **under the assumed actual two-point original head factor**, resting on the written reduction (W), rules (R1)–(R7) and the audited program; it would not show that anchored tilings exist or do not exist, that heads have such a factor, or anything for `g>30`, other spectra or unclosed allocations. A residual report gives necessary equations only. Fixtures and `n`-free projections are not anchored witnesses. Nothing here is a global theorem.

## 6. Read, process and execution declarations

* Before any mathematical body, I read completely the f896 manifest, freeze receipt, final pre-dispatch binding, parent-live metadata supply and actual dispatch receipt (including the full dispatch line), and all 22 manifest-listed status-only controls. Initial formatted displays elided entries/one long line; complete raw rereads recovered them before acknowledgement. I wrote `prebody-ack-v1.md` exclusively and delivered a direct PREBODY ACK to Main, both before opening either packet part. Controls were used for status/permissions only.
* Part 01 (supplied 87,886 bytes, 882 LF) was read serially in raw windows `1–20, 21–40, …, 841–860`, then **`861–882` (22 LF)**: this final window exceeded the 20-LF window rule by two lines. **Process deviation (administrative), disclosed here, not backdated**; the display was far below 30,000 bytes and complete. Part 02 (41,299 bytes, 633 LF) was read in raw windows `1–20, …, 601–620, 621–633`, all ≤20 LF. No display showed clipping; no recovery was needed. Together these cover S1 1–20, S2 1–51, S3 1–31, S4 1–20, S5 1–278, S6 1–280, S7 1–172, S8 1–129, S9 1–494, each through its ending. No link was followed; no unlisted or held source was opened. Hashes are parent-supplied, not recomputed.
* Mental calculations on concrete cases (disclosed; my runtime role has no narrower no-new-instance restriction): selector/antipode checks at packet regression values `g=1..9,10,12,13,14,15,16` while writing expectations, and the pair counts for `g=24..30` in §3. No result from them is asserted beyond §3's labelled expectations.
* No network, external model, code execution, compilation, test, scientific eval, child subprocess, shell command, Git, delete or cleanup. The write tool reported that it set the executable bit on the new source; nothing was executed. The source was edited in place several times while drafting, before this delivery and before any audit or GO; the parent should hash the final bytes. One earlier drafting response was discarded by the harness output limit before any of its tool calls ran; it had no file effect.
* All genuinely held episodes and all proof/method/planning/selection/verification/reporting/confidence/downstream consumers remained NONINPUT. No clean-cognition certificate is claimed. Prepared-code hash: **not computed by the author** (no execution); parent-supplied hash required.
