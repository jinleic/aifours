DISPOSITION: ACCEPT-WITH-FIXES

This is advice on the inactive draft package, not an activation or a parent acceptance. All copied-file SHA-256 values match `manifest.json`, including all eight required pins. References below are snapshot-relative, with one-based LF line numbers.

**FATAL**

None found in the conditional mathematical construction.

**MAJOR**

**M1. The receipt does not bind a selected source input as the draft promises.**  
`lane/review/drafts/AMENDMENT-4.r1.md:69` says the generator binds the source cube CNF SHA. The record constructed at `lane/code/k3_cuts_r1.py:292–319` binds the draft, code, wrappers, oracle receipt and cut-block digest, but consumes no source CNF or metadata and selects neither original nor lex C311. Binding the draft transitively binds its two named alternatives; it does not identify an actual input receiving the cuts.

**Correction:** before use, add a versioned composition record selecting the encoder and source variant, validating its CNF/metadata hashes, and binding the complete strengthened DIMACS header and SHA. Preserve this receipt as evidence of block generation only.

**M2. No supplied driver constructs or certifies the strengthened input.**  
The “append rule” at `lane/code/k3_cuts_r1.py:319` is descriptive text. `lane/code/k3_cube_certify_r3.py:27–73` regenerates original cube inputs only; its certification path additionally requires an UNSAT screen of that same original input at lines 95–97. It cannot certify either strengthened C311 variant unchanged.

**Correction:** supply and review an appender/regenerator and certification path for the selected strengthened input, including lex regeneration when selected, exact header/hash checks, resource accounting, and the cut prerequisites. The present 1 MiB retained-growth allowance covers the small receipt, not future retained CNF materialisation.

**MINOR**

**m1. Binding 3 incorrectly describes AMENDMENT-2’s existing prerequisite.**  
`lane/review/K3-Q4-SIDECAR.r1.json:40` says AMENDMENT-2 did not explicitly state the K2 half. However, `lane/review/AMENDMENT-2.r1.md:5–6` already says “hence on the K1/K2 exclusions before any unrestricted claim.”

**Correction:** distinguish AMENDMENT-2’s existing statement from the omissions in AMENDMENT-3, receipt scope fields, and the old AMENDMENT-4 draft.

**m2. The Gram citation repair has an inaccurate historical explanation and a mistyped digest abbreviation.**  
`lane/review/K3-Q4-SIDECAR.r1.json:47` and `lane/review/K3-ERRATA.r1.md:60` attribute the K1 §8 pointer to Gram r1. The copied `lane/review/GRAM-ENCODING.r1.md:45–55` already contains the minimality argument. The bad §8 pointer is in `lane/code/gram_enc.py:15`, identified as a code-comment error by Gram r2:26–27. Also, ERRATA:59 abbreviates the r2 digest as ending `d7c6`; it ends `d6c7`.

**Correction:** retain the correct r2/LEMMAS destination and line numbers, correct the explanation, and use the full digest already present in SIDECAR:48.

**m3. The historical generation/freeze-order exception remains unrecorded in the repair sidecar.**  
AMENDMENT-3’s lex metadata mtime is 21:20:58 (`manifest.json:376`), before its binding’s `frozen_at` 21:21:39 (`lane/review/AMENDMENT-3.bindings.r1.json:2`). AMENDMENT-2 likewise generated inputs before its binding record; G6 controls at 20:15:24 postdate the first screen start at 20:13:35.

**Correction:** explicitly record “bindings after input generation, before search; G6 controls after screen start.” This is a provenance exception, not a mathematical defect. Neither the new sidecar nor later controls can establish retrospective preregistration.

The substantive static checks supporting this disposition follow.

**Q1 — provenance and oracle.** Binding 1’s available-target hashes and values agree: source cube metadata, lex metadata, source/lex CNF digest fields, control receipt, wrappers, amendment/bindings, and all three screen receipts. The original screen is UNKNOWN after 1800.145 s; the lex screens are UNKNOWN safety stops after 769.881 and 1229.385 s. The sidecar meets AMENDMENT-3:46’s binding requirement in substance as supplementary, post-hoc provenance. The absent CNFs themselves cannot be hashed here.

Binding 2 agrees with the copied delta, driver and both receipts: r2 uses 3600/3600 caps, and both receipts pin `49677766…8211`. The recorded chronology is consistent: driver mtime 21:38:35; delta frozen 21:39:20 and mtime 21:39:40; A/C321 starts 21:39:49 and finishes 22:11:36; A/C411 runs 22:12:04–23:04:28. The stale 1800/3600 binding is superseded, not rewritten.

The K2 prerequisite is met by the copied parent verdict: `parent/moqls7-k2-parent-verdict.md:5–7,15–21,64` accepts the exactly-two-non-classical **triple** exclusion, with r2 accepted text and parent corrections. Its trust/provenance caveats, including the 35-class caveat at lines 54–56, remain attached. It does not exclude genuine non-classical pairs.

E2–E5 correctly repair the cited invariance, permutation, zero-coefficient and collinear-G6 wording. E7 correctly separates producer certificates from parent acceptance. E8 correctly states the dependency, subject to m1’s historical correction.

The B oracle observes B’s actual dictionary:

- `gram_encB.py:113–123` allocates `gv` and defines `g()` through it.
- G2/G3/G4 builders use `g()`; G5 uses `gv` directly.
- The fix branch at lines 203–215 iterates that same dictionary and appends signed units after all base clauses.
- `dump()` writes the header and clause lines; the trailing `vars` line is separate.
- `bmap_oracle_r1.py:125–176` reads those units and decodes each **B variable’s** pair label using A-index bits. It does not substitute A’s indices for observed B indices.

Twelve bits distinguish all 2646 labels. Under the inspected source, identity decoding establishes the stated pair identity for every variable. The necessary assumptions are: unchanged production arguments with no net; stable pinned code and ordinary local import resolution; A’s complete, correctly parsed map; the fix branch using the same unmodified `gv`; no pre-unit change caused by `--fix-json`; the inspected stdout layout; faithful execution records; and SHA-256 binding assumptions. Header checks enforce unchanged `nv`, `nc+2646`, declared line count and complete distinct unit coverage; prefix checks compare base-body digests. The trailing statistics line is recognised by prefix, not numerically cross-validated.

The runtime base hash matches B/C321 and B/C411 metadata. The oracle does **not** check B/C311 metadata. Independently reading `lane/explore/k3cubes/B_C311.meta.json:4–7` finds the same base hash and encoder/wrapper pins; production use still needs that instance explicitly bound. Comparator self-tests are correctly labelled comparison-only tests, not encoder mutations.

The new pre-execution pin chronology is supported by the records:

- Oracle: code mtime 00:48:11; frozen 00:48:54; pin-file mtime 00:49:12; run 00:49:18–00:49:40.
- Generator: code mtime 01:00:20; pinned 01:00:31; pin-file mtime 01:00:53; run 01:00:59–01:02:16.
- Sidecar, errata, draft and later README/LOG entries follow the relevant earlier work. They do not turn the old bindings into preregistration.
- GENERATOR:3’s “01:12” is explicitly a message label, not a host timestamp; LOG:167 records the discrepancy. It cannot establish wall-clock ordering.
- `cert_B_r4/B_C321.json:2–3,20–25,39` predates the oracle and records UNKNOWN, not a usable exclusion.

Filesystem mtimes are observations, not attestations. Omitted helpers, binaries and full original review documents cannot be independently hashed from their cited digest strings.

**Q2 and Q5 — transport and composition.** H1–H2 make every surviving K3 configuration minimal among non-classical triples. The replacement argument in Gram r2:52–65 and LEMMAS:54–78 then supplies all-line G4. H3–H5 correctly restrict application to accepted encoder bridges, K3 with no classical symbol lines, and the accepted cover/normalisation. All-ONB heaviness is stronger than the cuts require; own-row/column heaviness suffices.

For any selected frame and off-line point, unit norm gives nonempty support; G1 removes the unique cell sharing the other line. G5 is precisely the correct disjointness rule: it applies across different squares to the **same distinct cell pair** `(p,r)`, including all six available positions. Therefore the three weights sum to at most six. The asserted thresholds force exactly `(4,1,1)` or `(3,2,1)`.

After transposition when necessary, the stated row/column maps send the excluded frame cell to `(0,0)`. All six available positions are occupied in either forbidden case, so the maps fix every positive **and negative** cube literal. Every assignment of roles `a,b,c` is covered by square relabelling. Transposition exchanges row and column ONBs, reindexes every tensor ONB, and preserves rays/non-classicality. All-line heaviness transports too. The image satisfies the three symmetry units and the heavy condition whose guard encoding those units replace. Singleton G6 follows from G1/G2 and the signed cube.

Thus the cuts have the claimed conditional scope. “Heavy local type” consistently means a local occurrence with some weight at least three; it does not say every off-line point is heavy. Other local types, such as `(2,2,2)`, remain possible. Nothing here licenses arbitrary ONBs, classical symbol lines, or K1/K2/non-minimal applications.

The full cut family is invariant under arbitrary row, column and square permutations and transpose, hence under all three listed H groups. C411’s `(3,4)` swap need not preserve bare symmetry units: its cube supplies the fourth positive unit. E2 correctly uses the g-projection of **base ∧ cube**.

A common lex-minimal orbit member therefore satisfies cube, base and cuts. Reconstruct A’s AND auxiliaries and select true heavy-witness guards; reconstruct B’s products, threshold summaries and heavy counters; set lex-prefix auxiliaries according to prefix equality. No vector reconstruction from a Boolean model is required for this direction. Universal validity of each cut on actual K3 configurations would already preserve actual-configuration coverage; family invariance additionally establishes the Boolean orbit argument.

No mathematical composition step is missing under the stated hypotheses. The remaining gaps are the concrete input/driver bindings in M1–M2 and the unmet external exclusion gates.

**Q3–Q4 — generator and controls.** `positions()` and `off_points()` implement both frame orientations correctly. Pair normalisation preserves the unordered non-collinear pair. Each group contains
`3·C(6,4)=45` at-most-three clauses and `6·C(6,3)·C(3,2)=360` mixed clauses. Four/five distinct star edges uniquely determine their common point and frame; within a mixed clause, multiplicities identify the two square roles. This proves distinctness across the 588 groups.

A’s map comes from `gram_enc.build` and is compared with the wrapper map. B’s decoder obtains the A-labelled pair carried by each observed B variable, then correctly inverts it as `pair → B variable` (`k3_cuts_r1.py:259–274`). It is independent of A’s numerical ordering in the relevant sense. Its parser is weaker than the oracle: it lacks base-prefix, complete header and sign-control checks. The separately pinned oracle supplies those checks for the unchanged code.

Byte order is deterministic: rows then columns; off-points in row-major order; at-most-three templates before mixed templates; combinations in iterator order; three-position literals before two-position literals. Each clause is ASCII integers separated by spaces, followed by `" 0\n"`. Every g variable occurs 440 times. The digit sum for indices 1–2646 is 9477, so the block length is
`440·9477 + 2·1164240 + 2·238140 = 6974640` bytes.

The receipt reports A/B block SHA `05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd`. Its computation is specified by the source; the absent block’s digest was not independently recomputed. All generator/import/draft/oracle pins in the pin record and receipt match the copied files. `/usr/bin/python3 -B` is declared, and LOG:164 records that interpreter; the receipt lacks its own observed interpreter identity.

`shape_report()` is a complete characterisation given the trusted A inverse map: valid unique shapes have at most 45+360 possibilities per group, so exact group sizes establish completeness. Missing, extra, duplicated, mis-framed or incorrectly distributed-square clauses cannot pass unless the resulting family is still exactly the intended family.

For C1, inclusion–exclusion gives `4⁶−3·3⁶+3·2⁶−1=2100`. Forbidden counts are `3·30=90` assignments of type `(4,1,1)` and `6·60=360` of type `(3,2,1)`, totalling 450. The code checks specification/template equality; `emit()` applies that template to each group, while shape checking independently characterises the result.

The classical slope triples are valid weight-one positives. For `psi_gram`, the first shift is `m0=2`, giving `f=[0,6,5,1,3,4,2]`. At prime seven, the roots-of-unity zero criterion used is exact. The predicate has five neighbours at every own frame/off-point, yielding `588·C(5,4)=2940` at-most-three violations. Mixed violations are zero because the other squares have weight one.

There is no genuine K3 positive. Indeed, the Psi fixture with slopes 4 and 2 is not even a mutually orthogonal triple: at displacement `(1,5)`, Psi and slope 2 both have nonzero Gram support. Its NON-VACUITY label is correct. README:91 requires admitting **matched** genuine controls; it does not make this outside-domain fixture a K3 positive.

The six mutations have meaningful failure mechanisms: broken common-frame geometry; five literals merged into one square; duplicated row groups with column groups absent; forbidden one-square five-literal shapes; an incomplete group after deletion; and a collinear lookup from the wrong column exclusion. Note that `distinct_ok()` also demands the expected total, so its false result alone does not establish duplication.

The 22 generator equalities plus transpose check implementation transport; equality on generators implies equality on H. Removing one clause breaks some generator equality. Once decoded B equals A, equal blocks/sets are consequences of using the same `emit()`; control e supplies map/serialization consistency, not an independent cut implementation. Its text does not claim otherwise.

**Q6 — required before freeze/use and acceptance.**

1. Obtain parent verdicts accepting the exact A/C321 `d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388` and A/C411 `2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2` exclusions, with their explicit A-only or A+B standard. Neither exists here.
2. Resolve the protocol standard explicitly. README:80–81 calls for two encodings. The cover-parent disposition:18 offers an A-replay acceptance alternative, but an A-only production package should explicitly identify the parent-authorised exception rather than silently treat it as compliance with Phase C.
3. Select original A/C311 `7fca33f1…c2001` or lex A/C311 `059be616…a8c4f`. For B, bind original B/C311 `b3ec010855ad4abd75ffd6eb57aaa3ff158bc8447625ee2097f5a6057594c077`, or generate and bind a reviewed B-lex counterpart. No B-lex C311 artifact exists in this snapshot.
4. Freeze a new reviewed amendment and bindings after correcting these findings. Bind upstream verdicts, source metadata/CNF, generator/imports, oracle, controls and any lex composition.
5. Implement M1–M2. Expected strengthened headers are A-original `(96978,865696)`, A-lex `(107513,897308)`, and B-original `(461370,1867942)`. Regenerate/hash in memory under r3’s storage policy; bind the complete input SHA and validate the actual supplied bytes. Apply fresh growth-qualified launch gates and continuous native-stage floors.
6. Obtain newly DRAT-checked UNSAT on the protocol’s required independent routes, with exact input and tool/log bindings, then parent replay and parent review of the full composition. Old proofs transfer no certification to strengthened C311. UNKNOWN remains UNKNOWN.

| Q1..Q6 | Status | One-line reason |
|---|---|---|
| Q1 | FIX-REQUIRED | Main links/oracle hold; prerequisite-history, citation and chronology text need correction. |
| Q2 | CONDITIONAL | Transport is sound under H1–H5 and parent-accepted exact upstream exclusions. |
| Q3 | FIX-REQUIRED | Correct block family; selected-source binding and strengthened-input implementation are missing. |
| Q4 | ACCEPT | Controls establish their stated finite checks within the limits described. |
| Q5 | CONDITIONAL | Lex/composition coverage holds under the mathematical prerequisites. |
| Q6 | FIX-REQUIRED | New bindings/driver and an explicit production standard are required before use. |

| Prior id | Disposition | Evidence file:LF |
|---|---|---|
| Desk MAJOR 1 | CLOSED | `lane/review/K3-Q4-SIDECAR.r1.json:8–19` |
| Desk MAJOR 2 | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:12–21` |
| Desk MAJOR 3 | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:24–28` |
| Desk MINOR B map | CLOSED | `lane/review/K3-ERRATA.r1.md:8–24` |
| Desk MINOR lex invariance | CLOSED | `lane/review/K3-ERRATA.r1.md:30–36` |
| Desk MINOR T(X) | CLOSED | `lane/review/K3-ERRATA.r1.md:39–44` |
| Desk MINOR wording: AM2 zero | CLOSED | `lane/review/K3-ERRATA.r1.md:47–49` |
| Desk MINOR wording: G6 zero | CLOSED | `lane/review/K3-ERRATA.r1.md:53–54` |
| Desk MINOR wording: collinear G6 | CLOSED | `lane/review/K3-ERRATA.r1.md:55–56` |
| Desk MINOR stale driver | CLOSED | `lane/review/K3-Q4-SIDECAR.r1.json:26–31` |
| Desk MINOR chronology | OPEN | `manifest.json:376`; `lane/review/AMENDMENT-3.bindings.r1.json:2`; m3 above |
| Desk MINOR dependency text | PARTIALLY-CLOSED | `lane/review/K3-Q4-SIDECAR.r1.json:40,48`; m1–m2 above |
| Desk MINOR exclusion status | CLOSED | `lane/review/K3-ERRATA.r1.md:66–74` |
| Desk MINOR polish: frame scope | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:30–55` |
| Desk MINOR polish: full maps | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:39–50` |
| Desk MINOR polish: nonemptiness | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:34–37` |
| Desk MINOR polish: instance/H | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:79–85` |
| Desk MINOR polish: distinctness/maps | CLOSED | `lane/code/k3_cuts_r1.py:308,324,443` |
| Desk MINOR polish: spaces | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:61–67` |
| Desk MINOR identical logs | CLOSED | `lane/explore/k3cubes/screenA_r1/A_C311.solver.log:1`; `lane/explore/k3lex/screenA_r1/A_C311.solver.log:1` |
| Codex M1 | CLOSED | `lane/review/K3-Q4-SIDECAR.r1.json:8–15` |
| Codex M2 | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:11–28` |
| Codex m1 | CLOSED | `lane/review/K3-ERRATA.r1.md:30–36` |
| Codex m2 | CLOSED | `lane/review/K3-ERRATA.r1.md:8–24` |
| Claude D1 | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:12–21` |
| Claude D2 | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:24–28` |
| Claude m1 | CLOSED | `lane/review/K3-ERRATA.r1.md:47–49` |
| Claude m2 | CLOSED | `lane/review/K3-ERRATA.r1.md:8–24` |
| Claude m3 | CLOSED | `lane/review/K3-ERRATA.r1.md:53–56` |
| Claude m4 | CLOSED | `lane/review/K3-ERRATA.r1.md:30–36`; `lane/code/gram_enc.py:123–126` |
| Claude m5 | CLOSED | `lane/review/K3-ERRATA.r1.md:39–44` |
| Claude m6 | CLOSED | `lane/review/K3-Q4-SIDECAR.r1.json:8–15` |
| Claude m7 | CLOSED | `lane/review/K3-Q4-SIDECAR.r1.json:26–31` |
| Claude m8 | OPEN | `manifest.json:376`; `lane/review/AMENDMENT-3.bindings.r1.json:2`; m3 above |
| Claude m9 | PARTIALLY-CLOSED | `lane/review/K3-Q4-SIDECAR.r1.json:40,48`; m1–m2 above |
| Claude m10 | CLOSED | `lane/review/K3-ERRATA.r1.md:66–74` |
| Claude m11 | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:30–58` |
| Claude m12 | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:39–50` |
| Claude m13 | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:34–37` |
| Claude m14 | CLOSED | `lane/review/drafts/AMENDMENT-4.r1.md:60–85`; `lane/code/k3_cuts_r1.py:324,443` |
| Claude m15 | CLOSED | `lane/explore/k3lex/screenA_r1/A_C311.solver.log:1`; all three copied logs are exactly 10-byte `c UNKNOWN\n` files |

**Control limits**

- **a:** Establishes exact structural family/completeness given A’s inverse map; does not independently establish that map’s semantics.
- **b:** Establishes finite local coverage and specified support evaluations; supplies no genuine K3 positive or proof of cut validity.
- **c:** Detects six concrete mutation classes; does not establish detection of arbitrary defects, and some indicators include count checks.
- **d:** Establishes reported implementation invariance and a sensitivity check; does not replace the mathematical symmetry argument.
- **e:** Establishes decoded-map/emission consistency; equal emissions are not independent cut implementations.
- **Oracle:** Observes B’s actual map under pinned production code and arguments; does not certify cube satisfiability, proofs, or the unbound B/C311 instance.

Scope: read only the snapshot’s primary code, documents, metadata, receipts and relevant logs; used `prior/` only for the delta audit. No execution, simulation, solver/proof replay, network, delegation or writes occurred. CNF/proof bytes, omitted runtime helpers/binaries and source publications were unavailable for direct verification.