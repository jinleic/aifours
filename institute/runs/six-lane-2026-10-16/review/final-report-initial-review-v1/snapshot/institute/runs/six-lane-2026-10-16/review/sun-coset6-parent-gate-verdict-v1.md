# Sun's disjoint-coset conjecture at k=6: parent gate verdict v1

Recorded at 2026-10-18T12:55:36-07:00.

## Decision

**GATE MET for math-1 transition43. CORRECTNESS-ACCEPTED, computer-assisted proof of the k=6 case for every group.** This is not the conjecture for allk, not a k≥7 theorem, not Lean-verified and not human-peer-reviewed. Priority remains bounded/NOVELTY-UNCLEAR; no publication or external contact occurred.

**Exact theorem.** Let G be any group and U_1,…,U_6 subgroups of finite index, possibly equal. If the left cosets g_1U_1,…,g_6U_6 are pairwise disjoint, then some1≤i<j≤6 satisfies gcd([G:U_i],[G:U_j])≥6. There is no cover, finiteness, abelian, solvability, normality or prime-power restriction on the original group. The bound is sharp: six distinct cosets of one index6 subgroup have every pairwise gcd6.

## Text of record and dependency

- [Proof compositionv3](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/proof-k6-v3.md), SHA256 `2aa4fa430dfb414dc5c726064f43e4cd1c023a58862fd8bd7b805e46c6880324`.
- [Cumulative erratumv3](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/rules-k6-erratum-v3.md), SHA256 `71cfeccbfb708c11bbdcc6f0a36f060395752a3ebfbb7c097edde270d967cc77`, read with rules-k6-v1/v2/v3, proof-k6-lemmas-v1 and the reduction README.
- [Corrected certificate formatv3](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/CERT-FORMAT-k6-v3.md), SHA256 `fd3223168a32887100f1b17198bc2dc94d3cc9b28df306871f1c254b6c7fd62f`, with the documentation overlay below.
- [Independent parent every-rule derivation](sun-coset6-parent-derivation-v1.md), SHA256 `1a5d6d9c56feb593f0edbbf36a778dae182eea46d0529d6d898c19738da28fe9`.
- **Primary finite verifier:** [checker_v2.py](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset6-independent-checker-v1/checker_v2.py), SHA256 `a158c45f61d561c28f250296c26b35ce9e6fceff4dc3dd4ccba7bec6f200b75c`; standard library, one process, exact integer/Fraction decisions. The engine is an untrusted certificate producer.

The frozencontract names the k5 proof-v3 dependency. That obligation is discharged through the accepted [Sun(5) correctness verdict](sun-coset5-parent-verdict-v1.md), SHA256 `2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301`, binding k5 proof-v4 and its cumulative erratumv3. The frozencontract is not amended. The proof uses that locally verified theorem, not Gong's unread thesis. k5 has a prior reported unpublished confirmation; it is not counted as a new-open-target gate.

## Bound certificate inputs

These are the exact bytes read from the [parent input pins](sun-coset6-parent-inputs-v1/MANIFEST-v1.json), independently matched to the lane's frozen outputs:

| File | Bytes | SHA256 |
|---|---:|---|
| run.json | 2,853 | `6d8dc91dc6160a9a141da7e9bd0edba1b446aa2aaf9959e92fd05ac14babe754` |
| orbits.jsonl.gz | 407,387 | `a580c5801b03ed84edcdf9f58618b4fb0c0d390549dab31527d8a9da20f4dc49` |
| rlp_duals.json | 106,879 | `bbf91e057072d2840ee478a813dbebdc2266e6587e20e1c876b8da16177895ef` |
| survivors.json | 2 | `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` |

The decompressed orbit-content SHA256 is `f4f69363a1a602ec56f3a957566e566d2f03f988792a8d04565d2cce31976579`. The survivor bytes are exactly`[]`. Hashes identify data; they do not replace the mathematical and coverage checks below.

## Actual parent verification

[Parent v2 full report](sun-coset6-independent-parent-replay-v2/REPORT.json), SHA256 `f25bab1af07bef240097ea85fd2353b7501960495e1d4ecf96e964e3653fc9fc`, records:

- **1,575,031** independently generated T-consistent labelled patterns across all8types.
- Two differently structured enumerations agree exactly; every typed stabilizer orbit is re-expanded from its representative. The orbit sets are disjoint and their union equals the full independent leaf set, not just its size or hash.
- **61,124 of61,124 witnesses verified**, zero failed, zero incomplete, zero SURVIVE.

| Rule | Verified orbits |
|---|---:|
| K | 55,159 |
| RLP | 5,513 |
| FH5 | 134 |
| N26 | 108 |
| PB | 55 |
| RPLP | 155 |

Every RLPq and every RPLPq entry is checked, with exact rational dual inequalities. RLP makes324,428q checks; RPLP has9,371RLP references and385P vectors. All1,275used dual keys pass;71unused duals carry no proof weight. FH5 checks the complete assignment domain with safe monotone pruning for all7E5placements, including every non-a vertex's full trace choices. All91marker placements reduce to the8types.

Parent execution took **56.9seconds**, with all three independent completion gates true. [Parent mutation controls](sun-coset6-independent-parent-controls-v1.json):68/68expected outcomes, including43/43intended mutation rejections. The separate author reran those same controls onv2 with the same outcomes. The parent also wrote ancillary independent universe/witness and FH5 implementations; their results support cross-checking, but **are not needed as primary evidence** and their NumPy deviation is disclosed.

## Whole-composition reviews and repaired reporting bug

| Review | Disposition |
|---|---|
| [Codex final composition](sun-coset6-composition-final-v1-codex-v1.note.md), `f841d6a95a3c0fab1df01cda3e10dfa32ad958cc63e3a83d24d1bbb5ee9d6e32` | ACCEPT-WITH-FIXES; exact all-group theorem established from the accepted imports and completed finite replay. One MAJOR latent verifier reporting bug, not reached by that run. |
| [Claude final composition](sun-coset6-composition-final-v1-claude-v1.note.md), `424da7eac56ab2d6407aa0275f7fba1d077b148063bb6065e68126aaf454d9cd` | ACCEPT-WITH-FIXES; no FATAL/MAJOR,6MINOR including the same latent timeout bug. All mathematical implications accepted. |
| [Codex reporting-fix delta](sun-coset6-checker-v2-reporting-fix-codex-v1.note.md), `a170ea0d6449fc1f7b7d4090e8ab3f615ec8f8512071954b15ead2a37ee45acc` | REPORTINGFIXGO, no remaining load-bearing blocker; exact predicates unchanged; every-rule parent derivation accepted. |

**Bug and regression:** v1 could label a run PASS after skipping witnesses on a late deadline. Its actual completed run had61,124verified and0incomplete, so that path did not affect it. The frozen v1 remains preserved. v2 adds global skip recording and an independent PASSgate requiring verified==total_lines, failed0, incomplete0. [Exact diff](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset6-independent-checker-v1/checker_v1-to-v2.diff), SHA256 `467e902d0264e05fb18d29f134546fd5c6174e30b29372b6af5d8d7ece36328c`.

The targeted full-input clock injection reproduced v1's falsePASS with zero witnesses checked. Parent execution of the same injection onv2 [returned INCOMPLETE,exit1](sun-coset6-independent-parent-deadline-v2/INJECTION-RESULT.json), recording all61,124skipped witnesses globally. The injected falsePASS report is bug evidence, never theorem evidence. [Binding receipt](sun-coset6-v2-parent-replay-receipt-v1.json), SHA256 `1a81fbf0cd8b32b4191e6145221c2efebca63c7095912a754dcaf348bfabea0b`. No mathematical predicate or certificate changed.

## Parent mathematical bridge

The [parent derivation](sun-coset6-parent-derivation-v1.md) independently checks each used rule, not only the reduction:

1. Finite-index cores reduce arbitrary groups to finite groups preserving indices and disjointness. The prime-clique cover on6vertices forces a common prime if every gcd≤5. Common2/3 contradict acceptedSun(5); common5 gives indices5r_i with pairwise coprimer_i.
2. In a least-order fullSun(6)counterexample, every proper subgroup satisfiesSun(6). H5 constructs a proper index5subgroup. Only that subgroup's six-piece fibre invokesSun(6); RLP/RPLP use atmost5pieces.
3. T,K,K2,Ppair/PB,F,H5,hereditaryL9,RLP,XE,N26 andRPLP follow from product/intersection cardinalities, disjoint cosets and the stated lower-orderSun cases. The parent re-derived product-inclusion orientations, grid rounding, trace enumeration, all-q duality, ordered containments and empty-S columns.
4. The N26 missing prime-support justification is supplied in cumulativeC14 and independently re-derived: neighbour triangles have admissibleτ among{2,4},{4},{4,8},{4,8,12,16}. The E3test excludes12where necessary. Every cofactor—including1, arbitrary prime powers and primes≥7—is covered by the marker/saturation argument. E5irrelevance is justified for every non-FH5rule; FH5 coversall7placements.
5. Exact orbit-union equality transfers every checked certificate across its typed orbit. Thus no least-order counterexample carriesCore5(6), contradicting the reduction. This closes all finite groups and hence all groups.

The strict mass bound is1−1/(5r_v)<1 for eachfinite r_v; no uniform positive gap over unboundedr is assumed. No numerical LPsolver or realizability of arbitraryadmissibleτ is trusted.

## Mandatory documentation/status overlay

- The engine `code` field is an **opaque informational label**, with no typed-stabilizer-orbit guarantee; it MUST NOT be used for proof decisions. All witnesses and coverage use`(type,rep)`. The observed mismatch is harmless under this verified boundary.
- The checker was constructed fromformatv1/v2 plus review requirements; conformance tov3was established by the line-by-line final audits, not retroactively claimed as construction provenance.
- Frozen “pending/unreviewed” labels inproofv3/README are superseded only at the accepted scopes inthisverdict. The primary evidence is the standard-library v2report, not the NumPy auxiliary route.
- The malformed N26 table sentence is read through cumulativeC14's operative rows; the skipped§5heading and conservative SATthresholds are editorial, not extra mathematical assumptions.
- Use the four checked input digests above; the primary pinned-copy replay does not need the engine manifest besideitsinputdirectory.

## Priority, significance and residual risks

[Post-candidate primary comparison](../screening/math-1-sun-coset6-post-candidate-priority-v1.md), SHA256 `8311b4aea19c23f5858bfdb15d1babab8c28c9dd098b6622d000a18b3d6fd596`: PARTIAL_OVERLAP_FOUND, no prior k≥6general-group claim located in the bounded scope. The parent re-read Sun's MathOverflow statement and Menon's currentabstract; the scout checked currentarXiv/citers/authorpages/depositcatalogs with explicit unreadholes. M–SCor3.9 already covers someα1star patterns; the delta is the completek6case, not that knownlemma. Gong's k5claim is not a k6claim. A search miss establishes no novelty or priority. A final same-day announcement refresh is still scheduled.

This is a substantive specialist fixed-case result for the group version ofSun2006Conjecture1.2. ForG=Z,k≤20wasalreadyknown. GeneralSunfork≥7remainsopen. No humanreferee, journalacceptance orpublication; trustedCPython/exactarithmetic, OS andhardware, plus the acceptedk5computation. NoLean, Comparator orindependentformal kernel.

Preserved process defects: stopped same-author selfcheckUNKNOWN; never-run same-authorverifierarchived; placeholderhashcorrected; originalmetadata/timephrases corrected; NumPyauxiliarydeviation; verifierdeadlinefalsePASS reproducedandfixed. None is silently relabelled. Sourceandinputbytes remain immutable. All new evidence staysinsideaifours; no commit,push,deletionorcontact.
