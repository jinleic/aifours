# sun-coset6 acceptance amendment v1 (append-only record; no new science)

**What this file is.** An append-only record of the parent's acceptance decision, together with the status overlay that the decision makes mandatory.
- Every earlier lane file stays frozen and unchanged: the proofs, rules, errata, certificate formats, code, certificates and controls.
- No computation was run for this file. The only commands were `shasum` and `date`.
- It was written on 2026-10-18 after the host clock read 12:57:21 PDT. The freeze time is in `evidence/acceptance-amendment-v1.sha256`.

## 1. Decision

The parent gate verdict `R/sun-coset6-parent-gate-verdict-v1.md` was recorded at 2026-10-18T12:55:36-07:00, with SHA256 `efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29`. Its decision reads:

> GATE MET for math-1 transition 43. CORRECTNESS-ACCEPTED, computer-assisted proof of the k=6 case for every group.

**Accepted statement**, quoting the verdict:

> Let G be any group and U_1,…,U_6 subgroups of finite index, possibly equal. If the left cosets g_1U_1,…,g_6U_6 are pairwise disjoint, then some 1≤i<j≤6 satisfies gcd([G:U_i],[G:U_j])≥6.

The original group carries no restriction: there is no cover, finiteness, abelian, solvability, normality or prime-power hypothesis. The bound is sharp, as six cosets of one subgroup of index 6 show.

**What is not claimed:**
- the conjecture for all k, or any statement for k ≥ 7;
- Lean or any other formal verification;
- human peer review, journal acceptance or publication;
- novelty, "first", or priority beyond the bounded screens.

No commit, push, deletion, publication or external contact took place.

## 2. Bound records

The lane worker re-hashed every file below at 12:57 PDT on 2026-10-18. Each hash equals the value recorded in the verdict.

| record | SHA256 |
|---|---|
| parent gate verdict `R/sun-coset6-parent-gate-verdict-v1.md` | `efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29` |
| proof composition (text of record) `proof-k6-v3.md` | `2aa4fa430dfb414dc5c726064f43e4cd1c023a58862fd8bd7b805e46c6880324` |
| cumulative erratum `rules-k6-erratum-v3.md` (read together with rules-k6-v1/v2/v3, proof-k6-lemmas-v1 and README §2) | `71cfeccbfb708c11bbdcc6f0a36f060395752a3ebfbb7c097edde270d967cc77` |
| certificate format `CERT-FORMAT-k6-v3.md` (with the overlay in §4 below) | `fd3223168a32887100f1b17198bc2dc94d3cc9b28df306871f1c254b6c7fd62f` |
| parent every-rule derivation `R/sun-coset6-parent-derivation-v1.md` | `1a5d6d9c56feb593f0edbbf36a778dae182eea46d0529d6d898c19738da28fe9` |
| primary finite verifier `R/sun-coset6-independent-checker-v1/checker_v2.py` (standard library, separate author) | `a158c45f61d561c28f250296c26b35ce9e6fceff4dc3dd4ccba7bec6f200b75c` |
| verifier diff v1 → v2 `R/sun-coset6-independent-checker-v1/checker_v1-to-v2.diff` | `467e902d0264e05fb18d29f134546fd5c6174e30b29372b6af5d8d7ece36328c` |
| parent full replay report `R/sun-coset6-independent-parent-replay-v2/REPORT.json` | `f25bab1af07bef240097ea85fd2353b7501960495e1d4ecf96e964e3653fc9fc` |
| binding replay receipt `R/sun-coset6-v2-parent-replay-receipt-v1.json` | `1a81fbf0cd8b32b4191e6145221c2efebca63c7095912a754dcaf348bfabea0b` |
| Codex final composition review | `f841d6a95a3c0fab1df01cda3e10dfa32ad958cc63e3a83d24d1bbb5ee9d6e32` |
| Claude final composition review | `424da7eac56ab2d6407aa0275f7fba1d077b148063bb6065e68126aaf454d9cd` |
| Codex reporting-fix delta review | `a170ea0d6449fc1f7b7d4090e8ab3f615ec8f8512071954b15ead2a37ee45acc` |
| accepted Core(5) input `R/sun-coset5-parent-verdict-v1.md` | `2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301` |
| post-candidate priority screen `S/math-1-sun-coset6-post-candidate-priority-v1.md` | `8311b4aea19c23f5858bfdb15d1babab8c28c9dd098b6622d000a18b3d6fd596` |
| certificate input `evidence/engine-v3-core56/run.json` | `6d8dc91dc6160a9a141da7e9bd0edba1b446aa2aaf9959e92fd05ac14babe754` |
| certificate input `evidence/engine-v3-core56/orbits.jsonl.gz` | `a580c5801b03ed84edcdf9f58618b4fb0c0d390549dab31527d8a9da20f4dc49` |
| certificate input `evidence/engine-v3-core56/rlp_duals.json` | `bbf91e057072d2840ee478a813dbebdc2266e6587e20e1c876b8da16177895ef` |
| certificate input `evidence/engine-v3-core56/survivors.json` (bytes `[]`) | `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` |

Here `R/` is `institute/runs/six-lane-2026-10-16/review/` and `S/` is `…/screening/`.

## 3. Evidence that carries the acceptance (summarised from the verdict; the parent holds the record)

**Finite part.** The separate-author standard-library verifier checker_v2 is the primary evidence. The engine is treated only as an untrusted producer of certificates. The parent's full replay found:
- 1,575,031 T-consistent labelled patterns, generated independently, across all 8 types;
- exact equality between the union of the orbits and the full leaf set;
- 61,124 of 61,124 witnesses verified, with 0 failed, 0 incomplete and 0 SURVIVE;
- every RLP q-entry and every RPLP q-entry checked with exact rational inequalities;
- every FH5 assignment domain checked for all 7 E5 placements;
- every one of the 91 marker placements reduced to the 8 types.

**Verifier bug.** In checker v1, a late deadline could produce a false PASS with witnesses skipped. The completed v1 run itself had 0 incomplete witnesses, so it was not affected. The bug was reproduced by clock injection. It is fixed in v2, which adds a PASS gate requiring verified = total, failed = 0 and incomplete = 0. A Codex reporting-fix review returned GO. No predicate and no certificate changed.

**Mathematics.**
- Both whole-composition reviews (Codex and Claude) returned ACCEPT-WITH-FIXES and accept every mathematical implication.
- The parent's derivation independently re-derives every rule that is used, not only the reduction.
- The contract's dependence on k5 proof-v3 is discharged through the accepted Sun(5) verdict, which binds k5 proof-v4. The frozen contract itself is not amended.

## 4. Mandatory status overlay, carried into the lane

These points apply to every frozen file in the lane.

1. **The engine `code` field is opaque.** In `orbits.jsonl.gz` (and in the engine-v1/v2 `orbits.tsv.gz` files) it is an informational label only. It MUST NOT be used for proof decisions. All coverage and all witnesses use `(type, rep)`.
   - *Structural reason, from the frozen engine source* (`core56_engine_v2.py`, function `canon`; added by the worker): vertex statuses enter only the initial colours of a colour refinement. Vertices are then ordered by sorted colour class, and the key records α-values only.
   - Consequently `code` is not a labelling of the stated type: special vertices are generally not at their typed positions. The key alone is also not guaranteed to separate typed orbits.
   - Coverage rests on the parent's exact orbit-union check instead.
2. **Provenance of the verifier.** checker_v2 was built from CERT-FORMAT v1/v2 plus the review requirements. Its conformance to v3 was established by the line-by-line final audits, not claimed as construction provenance.
3. **Superseded status labels, and only at the accepted scope.** The frozen lane texts contain labels such as "[NEW] … unreviewed" (README, rules-k6-v1/v2/v3, proof-k6-lemmas-v1), "CONDITIONAL", "candidate" and "pending" (proof-k6-v1/v2/v3, README-addendum-v1). These are superseded only within the scope of the verdict.
   - The conditions (i)–(iii) of proof-k6-v1/v3 are met per the verdict: the separate-author replay, the lemma reviews, and the accepted Core(5).
   - "[NEW]" still means "written in this lane" and is not a novelty claim.
   - The primary evidence is the standard-library v2 report, not the parent's NumPy auxiliary route.
4. **Editorial defects in CERT-FORMAT-k6-v2/v3 add no mathematical assumption.**
   - **The malformed N26 table sentence** (CERT-FORMAT-k6-v3, N26 section, the sentence quoting "At most one 4-edge", with the row "2,2,4 | 2 or 4 | {2, 4} or {4}") is read through erratum-v3 C14's operative rows: (2,2,2) → {2,4}; (2,2,4) → {2,4} if E2 is opposite the 4-edge, else {4}; (2,4,4) → {4,8}; (4,4,4) → {4,8,12,16}.
   - **The missing §5 heading** (the sections run §0–§4, then §6) is editorial.
   - **The conservative SAT thresholds** are editorial.
5. **Input digests.** Use the four certificate-input digests in §2. The pinned-copy replay does not need the engine manifest beside its inputs.

## 5. Priority and significance (from the verdict and the screen)

**Priority screen: PARTIAL_OVERLAP_FOUND.**
- Margolis–Schnabel Cor 3.9 already excludes some patterns that have a star of α = 1. The delta of this lane is the complete k = 6 case, not that known lemma.
- No prior claim of k ≥ 6 for general groups was located in the bounded scope. Gong's reported, unpublished k = 5 claim is not a k = 6 claim.
- The holes that were not read are listed in the screen. A search miss establishes neither novelty nor priority. A final same-day announcement refresh is still scheduled.
- If a prior k = 6 claim for general groups is found later, the correctness evidence is preserved and the new-open-target gate claim stops.

**Significance.** This is a fixed-case result for the group version of Sun 2006, Conjecture 1.2. For G = Z, k ≤ 20 was already known. The general case for k ≥ 7 remains open.

**What the result relies on:**
- CPython and exact arithmetic, the operating system and the hardware;
- the accepted k = 5 computation;
- Zhu Theorem 1.1.

## 6. Process defects, preserved and not relabelled

- **Same-author self-check.** `core56_checkB_v1` was stopped cooperatively at 12:02:48 PDT on parent instruction. Its outcome is UNKNOWN. The receipt is `evidence/checkB-v1-run1-STOP-RECEIPT.json` (`162bb488…3424`); its first draft gave a wrong start time, corrected before freezing.
- **Retired code.** The never-run same-author verifier `core56_checkB_v2` and an unused engine copy were retired to `archive/retired-v1/`. Its `MANIFEST.md` keeps a correction line for a guessed time.
- **Placeholder hash.** A placeholder hash for `rules-k6-erratum-v2.md` was sent in one IRC message and corrected in the next. No file carried it.
- **Mutation controls.** `controls_k6_v1` required T-consistent mutants, and so found no breaking mutation for K and FH5. `controls_k6_v2` relaxed that requirement and records T-consistency. Controls never gated anything.
- **Exploratory cells.** These are labelled EXPLORATORY and never counted (README §4; README-addendum-v1). One calibration cell hit its 1800 s timeout.
- **Parent-side defects.** These are recorded in the verdict: the NumPy auxiliary deviation, and the verifier deadline false PASS that was reproduced and fixed.

## 7. Lane status

- The lane is closed for new science. The lane worker runs no processes.
- Any next target will be frozen separately by the parent before any substantial work.
- Nothing for k ≥ 7 has been started.
