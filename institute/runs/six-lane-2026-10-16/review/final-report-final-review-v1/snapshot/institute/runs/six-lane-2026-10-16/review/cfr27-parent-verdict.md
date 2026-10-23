# CFR(5,27) parent verdict — info-2 — 2026-10-17 18:24:55 PDT (host clock)

**Disposition: GATE MET (info-2).** Two explicit 5 × 27 circular Florentine rectangles exist, so CPro1's listed open instance [5,27] is resolved and F_c(27) ≥ 5. Correctness: **VERIFIED** for the finite witnesses, by six independent routes listed below. Priority: **NONE-FOUND-IN-SCOPE** (bounded; important primary texts unread). Novelty: **UNCLEAR**. Significance: **modest, specialist**. Not Lean-checked. No human peer review.

Frozen target contract: [`screening/info-2-cfr27-contract.json`](../screening/info-2-cfr27-contract.json) (sha256 `027f36d7ffe68e7765ab990b5ee7ee4ce3af092c3123a2adedea200686e277b0`). Its success gate is: a raw witness passing the parent definition-first event checker, an independent Codex CLI verifier, a Claude CLI prompt-only checker, intended-reason controls and producer replay, plus a post-result priority screen against primary sources. Every element is met below.

## Object

- **Definition (CPro1 `problem_def.py`, read by the parent at commit `827f02b4048fc96a6b79f0970c87ca5a54f31f40`):** "A \"Circular Florentine Rectangle\" CFR(r,n) is an r x n array … with each row having a permutation of the set of symbols S={0,1,2,...,n-1}, such that for any two distinct symbols a and b in S and each m in {1,2,3,...,n-1} there is at most one row in which b appears in the position which is m steps to the right of a. \"Steps to the right\" is taken circularly". The same file lists `OPEN_INSTANCES = [[6,21],[5,25],[5,27],[4,33]]`.
- **Equivalent object:** a (Z_27, 6; 1) difference matrix over the **cyclic** group Z_27 (6 rows; each ordered row pair's column differences cover Z_27 exactly once). Equivalently, 4 mutually orthogonal normalized orthomorphisms of Z_27. These are cyclic Z_27 objects. They are not GF(27) = (Z_3)^3 objects; that distinction is exercised by a reproduction control below.
- **Producer:** InfoCFR27Lift's deterministic symmetric orbit models, exact-cover search, information-science lane `cfr33/cfr27/dmorbit-v1/`. Model T10 (cyclic group of order 6) gave witness A; model S3a (S_3) gave witness B.

## Parent pins ([manifest](cfr27-parent-inputs-v1/manifest.json))

| File | sha256 | Lane source |
|---|---|---|
| A-CFR.raw | `6ceed793b3cd733461b8bec06091c282e300b1f1feeef9c95cf6d1c679588c7a` | `cfr27/candidates-v2/cfr-5-27-T10-zero-first.raw` |
| A-DM.raw | `b8eec25f6d575aecfce12933a067b582774dd1be8738604797d5c76169c6c65c` | `cfr27/dmorbit-v1/runs-xc/T10-zero-first.dmraw` |
| B-CFR.raw | `a9faf3dd0d2c2bbff53499d869ed00eeeb7b876abbb75c294680b10969b35f0a` | `cfr27/candidates-v2/cfr-5-27-S3a-nozero-first.raw` |
| B-DM.raw | `3f45f8c33d4f2379a154dd4d6bb21da6ef40beb50b7548d56ee3bf799357b664` | `cfr27/dmorbit-v1/runs-xc/S3a-nozero-first.dmraw` |

## Verification routes (all passed)

1. **Parent definition-first checker** `check_cfr_dm_parent.py` (sha256 `aa977011d074291d95ede4f1070ef83aec7c17e286b8c986f4cf23062e761f45`): PASS on all four files ([receipts](cfr27-parent-check-v1/)). For each CFR, all 3,510 circular events are distinct, with 135 per nonzero displacement. For each DM, all 15 row pairs cover Z_27 exactly once.
2. **Parent intended-reason controls:** 43/43 matched the intended category ([result](cfr27-parent-controls-v1/parent-result.json), controls sha256 `2a7c7f142f2c21d358002520ea96108b8c682c46f3e720f309ddeff013b75df5`). They comprise 12 equivalence-preserving positives (unit multiplier, rotation, symbol swap, DM column transforms, a CFR(2,3)) and 31 negatives: format, digest, row count, width, range, permutation, event collision, and a circular-wrap-only collision at n = 4.
3. **Codex CLI `gpt-6.1-sol`, own in-memory verifier:** `RESULT: VALID` ([note](cfr27-codex-verify-v1.note.md), sha256 `0f0477425ff288f115ba89bad29ca6360206f017bd1b56d639c66860dbc72d07`). It re-did the strict parse of all 4 files, counted 702/702 ordered symbol pairs and 3,510/3,510 distinct events for each CFR and 15/15 row pairs for each DM, and rejected 14 targeted mutations by their intended invariants. It also derived DM↔CFR in both directions.
4. **Claude CLI `claude-opus-5-5` prompt-only checker**, executed by the parent ([extracted checker](cfr27-claude-verifier-v1/checker.py) sha256 `49628fd83e9af84516e18f4ac89c5fc5410e5ecb31e07687a64f695920d5901e`; [runner](cfr27-claude-verifier-v1/run_checker_parent.py) `3e4705cf3d4683c6fea02c56eaddbe68c9912889dc785c69381ec80e201f48d7`): 58/58 expected outcomes ([result](cfr27-claude-verifier-v1/result.json), sha256 `fbd3041a7a5a0de9a46369befc3a8ae37d875dd53f1b150eb1e80230ccc10f28`).
   - 20 accepts: the 4 pins under both `python3 -B` and `python3 -O -B`, plus the 12 positive fixtures.
   - 38 rejects: the 31 negative fixtures plus 7 argument controls (wrong digest, wrong row count, wrong n, DM/CFR kind swaps, uppercase digest, missing file).
   - Its DM mode decides DM validity from the definition alone, then re-verifies the derived CFR.
5. **Producer rebuild and replay** (subagent Cfr27ParentReproduce; [receipt](cfr27-parent-reproduce-v1/receipt-v1.json) sha256 `e8b1f77c8eb38ee993e37d6c36dad7dcac4878b35dca5efc726edd92085feb72`; [report transcription](cfr27-parent-reproduce-v1-report.md)):
   - The frozen C source rebuilt to a byte-identical binary `b9ab6856…a572158`. Both DM raws were regenerated byte-for-byte, with matching search-node counts (3,296,253 and 6,082,255).
   - The lane model compiler reproduced the pinned model files.
   - An independent stdlib audit of the group actions found T10 = C6 with orbit sizes [1,2,6,6,6,6] and S3a = S3 with orbit sizes [3,6,6,6,6]. Both DMs are invariant under every group element.
   - Independent DM→CFR regeneration is byte-identical to both CFR pins.
   - 13/13 controls behaved as intended. These include a wrong generator, wrong multipliers, the opposite action convention, a perturbed base column, and GF(27) digit arithmetic, which fails.
6. **Problem-poser predicate:** CPro1's own `problem_def.v` with `utils.parsesoltext`, AST-extracted from the commit-pinned Apache-2.0 sources ([dir](cfr27-cpro1-predicate-v1/); upstream sha256 `44f4d4ff…70aa` and `b4f7c66d…9c26`; only those three functions were executed). It accepts both CFR pins ([v2 result](cfr27-cpro1-predicate-v1/result-v2.json), sha256 `f90814e8d73e20638c75d8c23153cf325dde4a37582d2cfc868819bf59054d7c`).
   - 20/20 scored controls agree with the intended verdict. The other 14 are strict-format or binding-only controls (CRLF, leading zero, digest, row count, declared width) that CPro1's lenient parser is not designed to reject, so they are not applicable.
   - The v1 runner ([result](cfr27-cpro1-predicate-v1/result.json), retained) forced parameters [5,27] and treated those controls as semantic rejects. It is superseded by v2, and its accept verdicts on the two pins are unchanged.

## Priority and derivability (bounded)

- **Scout** Cfr27Priority: NONE-FOUND-IN-SCOPE ([transcription](cfr27-priority-scout-v1.md), sha256 `77d8309814ac191619e02264f26958f111ebc2a146ccfcfae142f756890ee176`).
  - Coverage: DataCite, OpenAlex full text, arXiv, zbMATH, CPro1, Sage `database.py` (no 27 entry among the DMs), GitHub, OEIS, the Handbook "new results" pages, and works citing Pan et al. 2022, Ge 2005 and Abel–Ge 2005.
  - It records the equivalent objects it searched for: the cyclic (6,27)-CDM, 4 MOO(Z_27), 5 MOLS(27) of the form f_i(x)+y, mutually orthogonal diagonally cyclic Latin squares, and (27,27,5) one-coincidence FHS sets.
- **Parent DataCite spot check** ([summary](cfr27-priority-parent-spot-v1/summary.json), sha256 `81a8128530f9a1a15166fda29365263478b8f9ef0f8e0aa0bfe35eaecf30978f`; raw responses gzipped and hashed): 12 queries, covering "circular florentine", florentine, orthomorphism(s), difference matrix/matrices, frequency hopping with 27, and the creator families Kirtchakov, Long, Vos, Raval, Ferudun, Gippini and Sadhu. No CFR(5,27), 6-row cyclic Z_27 DM or 4-MOO(Z_27) claim was found. The only on-topic CFR record is Kirtchakov's CFR(5,25) (zenodo.21831896, 2026-08-07).
- **Baseline correction:** the 5-row cyclic DM over Z_27, equivalently CFR(4,27), dates to Abel–Ge 2005, Theorem 4.2. This rests on the secondary citation in arXiv:2006.06921, Lemma 4.11; the 2005 bodies were not read. The witnesses add one row to that baseline.
- **Derivability** (scout analysis, unreviewed): none of the located constructions yields it.
  - CRT products do not apply to a prime power.
  - Field constructions give (Z_3)^3, not Z_27.
  - Multiplier rows give only 3 rows.
  - Holey recursion would need a 6-row DM over Z_3 or Z_9, which cannot exist.
  - Derivability from the unread bodies is unresolved.
- **Access holes:** Handbook VI.62 Table 62.27 (the n = 27 entry), VI.17 and III.3; Song 2000 body; Song 1991 thesis; Abel–Ge 2005 and Ge 2005 bodies; Abel–Finizio–Ge–Greig 2006 Table 1; Evans 2018 Ch. 8/13 and Evans 2007; Wanless 2004; IEEE papers by Zhang–Helleseth and Song–Song; Zenodo API (403; DataCite metadata used instead). The recorded Handbook value F_c(27) = 4 is itself an inference from CPro1's dev/open lists.

## Significance

This is a modest extension of a specialist table. It resolves one CPro1 open instance, comparable to Kirtchakov's CFR(5,25), and adds one row beyond the 2005 cyclic Z_27 baseline.
- It does not determine F_c(27); the trivial upper bound is 26.
- It does not answer van Greevenbroek–Jedwab Question 7.2.
- It has no MOLS-table consequence, because N(27) = 26 from GF(27).

Suggested external wording: "We exhibit explicit 5×27 circular Florentine rectangles, equivalently 6-row difference matrices over cyclic Z_27, so F_c(27) ≥ 5. A bounded screen on 2026-10-17 PDT found no earlier construction; the Handbook VI.62/VI.17 bodies, Song (2000), Evans (2018) and Wanless (2004) were not readable, and no priority over them is claimed." Never "first". Before any deposit, re-run the same-day DataCite "circular florentine" and florentine queries.

## Deviations and caveats

- The CPro1-predicate v1 runner had the design error described above. It is retained, and v2 supersedes it.
- The priority scout had no host clock. Its time base is the server stamps it quotes, about 17:40–18:10 PDT.
- Lane deviations recorded earlier still apply: eval-timeout SIGKILLs in InfoCFR33 and InfoCFR27Lift (one killed a control-run wrapper whose solver finished SAT without a record), a `mv -n` rename, and a guessed heading. None touches the pinned witnesses, which were re-derived from the frozen source by the parent replay.
- The checker toolchains are trusted: Python 3.9.6 and Apple clang 17.0.0 for the producer rebuild. No formal proof.

## Verification-count clarification — 2026-10-17 18:32:45 PDT

The six numbered rows above are evidence categories, **not six independently authored checker implementations**. Row 2 exercises the same parent checker as row 1. The three separately authored definition-level implementations are the parent checker, Codex's own verifier, and the Claude-authored checker. CPro1's upstream predicate is an additional implementation; the independently rebuilt producer and group-action/conversion audit add reproduction and construction evidence. The opening phrase “six independent routes” must be read with this correction. No witness, check outcome, priority limit or gate decision changes.

