# Olson repair delta check v2 (delegated parent delta check) — `olson-repair-delta-v1` — AUTHORITATIVE

v2 written 2026-10-17T23:14:06.257168-07:00; it supersedes `delta-check.md` (sha256 `88133a19fead27b157d6eac39a527538b25ff77dcc0992bf9e7ec1aef82156b1`, retained unchanged under the no-edit rule). Differences: R5's last sentence (an unverifiable 'first check' claim) is replaced by the search result; D4's last sentence is reworded; D7 records this. All outcomes, findings, numbers and hashes are otherwise identical.

Delegated parent delta check by subagent OlsonRepairDeltaDesk, written 2026-10-17T23:11:35.149116-07:00. Advisory only: the parent decides. Lane files were read only (no lane edits, commits, pushes, publication, contact or paid APIs). Correctness, novelty and significance are kept separate (Sec. 9). No full NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered-Olson result is claimed or implied.

Lane L = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-run-count/mixdef-high/c6`. Line numbers below are LF lines of the pinned bytes (`str.split('\n')`, 1-based). `star` = proof-SEEDGstar(.md|-r1.md), `cls` = proof-SEEDG-cls(.md|-r1.md), `C0WB` = proof-C0WB(.md|-r1.md).

## Outcome (delegated parent delta check)

| repaired file (sha256) | delegated parent delta outcome | Codex delta verdict |
|---|---|---|
| `proof-SEEDGstar-r1.md` (`8d4c844979d435b4a22815de39e113604aed5c0cb8973537521f7b0613250806`) | **DELTA-ACCEPT-WITH-NOTES** | DELTA-ACCEPT-WITH-NOTES |
| `proof-SEEDG-cls-r1.md` (`30c442668d5154c0188f64976d948e201920fe73d00ce77f4c5c30797d8eff61`) | **DELTA-ACCEPT-WITH-NOTES** | DELTA-ACCEPT-WITH-NOTES |
| `proof-C0WB-r1.md` (`7a38730089b8b97328b158a8accfefa606e2d8393869ad67c7d53e8eba464084`) | **DELTA-ACCEPT-WITH-NOTES** | DELTA-ACCEPT |

- Every FATAL/MAJOR/MINOR item of the four notes maps to r1 text that addresses it (Sec. 3). The single MAJOR in the four notes (Codex star note M1: COUNT-only scope overclaim at star:82–83) is replaced at star-r1:116–118 by the reviewer's own corrected sentence plus a per-word caveat; the old sentence is deleted.
- No repair introduces a mathematical error. The compact LF forms, the doubled-difference vectors, the integer relaxation J(u), automatic PIN, the extended QQ pair domain, the allowed-profile filter and the C0WB quantifier/bracket repairs all check (Sec. 4, own arithmetic; Sec. 6, Codex by hand).
- Residual notes are wording/provenance only (Sec. 7, R1–R8). Codex reports exactly three residual MINORs (R1–R3), FATAL 0, MAJOR 0. My T3 outcome is one step more conservative than Codex's DELTA-ACCEPT because of R4/R5 (evidence pointer and import-status wording); neither blocks the written mathematics.

## 1. Pinned pairs (hashes verified against the assignment before any reading)

| file | sha256 | LF-split lines | bytes |
|---|---|---|---|
| `c6/proof-SEEDGstar.md` | `476e9a2871cc81352b7bcbb84c31f9c29606f76cb330d18556330578385f5b22` | 88 | 8545 |
| `c6/proof-SEEDGstar-r1.md` | `8d4c844979d435b4a22815de39e113604aed5c0cb8973537521f7b0613250806` | 167 | 16061 |
| `c6/proof-SEEDG-cls.md` | `5a5038e4b22c9a00e95c11f5157357b65ab2cbb3311d241b5478dbcb4e8602ba` | 82 | 7478 |
| `c6/proof-SEEDG-cls-r1.md` | `30c442668d5154c0188f64976d948e201920fe73d00ce77f4c5c30797d8eff61` | 110 | 9952 |
| `c6/proof-C0WB.md` | `ac52d85fc04ebc29aacd5bffbe923355234af752c5b5e2a52efe8b9a9935de77` | 125 | 11927 |
| `c6/proof-C0WB-r1.md` | `7a38730089b8b97328b158a8accfefa606e2d8393869ad67c7d53e8eba464084` | 158 | 15716 |

Copies of all six are in `inputs/inverse-run-count/mixdef-high/c6/` (byte-identical; see `inputs/manifest.json`). The worker's `out/freeze.txt` LF 274–304 lists the same r1, code and receipt hashes as my snapshot copies (checked entry by entry).

## 2. Exact diffs (difflib.unified_diff, n = 3, of LF-split lines)

| diff file (this dir) | sha256 | hunks | r0 lines unchanged / removed | r1 lines added |
|---|---|---|---|---|
| `diff-SEEDGstar-r0-r1.txt` | `8963161d6f4591b7f448b2c18fd9b895fb80be76d81aa12be97b78158325ef3b` | 4 | 45 / 43 | 122 |
| `diff-SEEDG-cls-r0-r1.txt` | `22108e95ddf87c6af2ff56dcee83904d6417befc79057fd90a53555d2d08dc28` | 5 | 66 / 16 | 44 |
| `diff-C0WB-r0-r1.txt` | `69c94a704b208abf17e35d867d13d40a196962708054cfa44c3e8d33c33f2e8a` | 4 | 92 / 33 | 66 |

The C0WB diff confirms that DF/C0W/C0B (C0WB:27–69) are byte-unchanged: they reappear as C0WB-r1:39–81 (block sha256 with trailing LF `7e673e8b3282a9db6e6361e77f3d269b8f34ed59a90bfb277a658ec226f7e995`, matching Codex). The r0 Case-B Remark (C0WB:70–71) is the first changed line of that region.

## 3. Finding map: every item of the four notes → r1 text

### A. Codex star/cls note (`olson-c6g-r2-star-codex-review-v1.note.md`, sha256 ae6d6682…71d3; ACCEPT-WITH-FIXES, FATAL 0 / MAJOR 1 / MINOR 4)

| ID (note LF) | r0 location | finding | r1 text addressing it (pinned LF) | status |
|---|---|---|---|---|
| **M1 (MAJOR)** (LF 7) | star:82–83 | "obstacle left … is the COUNT condition" exceeds receipt: one OPENE class fails the seed test | star-r1:116–118 (Codex's replacement sentence nearly verbatim + "not a proof that C+'s per-word (i)/(ii+) fail … nor that counting is the only general obstacle"); r0:82–83 sentence deleted (diff hunk 4) | ADDRESSED |
| m1 (LF 11) | star:42 | "≥ each of the nine bounds" false | star-r1:62–66 (sum = min_i U_i + min_j T_j = min_(i,j)(U_i+T_j) ≥ min B_ij = L_A; integrality; explicit disclaimer) | ADDRESSED |
| m2 (LF 23) | cls:35 | "(k ≥ 12)" wrong | cls-r1:40 (ends t+2, t−2, cyclic distance min(4,k−4) ≥ 2, k ≥ 2κ+3 ≥ 7) | ADDRESSED |
| m3 (LF 25) | seedXstar2.py:23 | float bounds() not exact for unrestricted p | star-r1:50–51, 126–128, 160–162; seedXstar3.py `bounds` uses eight doubled integer expressions and (n+1)//2 (read statically; matches 2× the eight L_A/L_B expressions); frozen seedXstar2.py and its receipts unchanged | ADDRESSED (new code); residual wording at star-r1:13 (see R2) |
| m4 (LF 34) | desk prompt | prompt hash suffix typo | not a lane defect; star-r1:5 quotes …f5b22 correctly | NOT-A-LANE-ITEM |
| remark (LF 129) | cls:6 | cite r2 instead of r1 | cls-r1:10, 29, 65, 73 | ADDRESSED |
| remark (LF 145) | map6.py | unpinned c4 label dependencies | star-r1:131–133; seedX3.py `source_manifest()` hashes seedX3/map6/both c4 files; new receipt headers carry them; old receipts not retro-hashed (stated) | ADDRESSED going forward |

### B. Claude star/cls note (`olson-c6g-r2-star-claude-review-v1.note.md`, sha256 4e55c8cc…3f41; ACCEPT-WITH-FIXES, FATAL 0 / MAJOR 0 / MINOR 15)

| ID (note LF) | r0 location | finding | r1 text (pinned LF) | status |
|---|---|---|---|---|
| m1 (19) | star:50–52 | per-run either/or ill-formed | star-r1:81–86 (global EITHER actual-empty OR every run has nonempty QS* seed and P2; empty case discharged first) | ADDRESSED |
| m2 (26) | star:42–43 | = Codex m1 | star-r1:62–66 | ADDRESSED |
| m3 (31) | star:20 | facts-used list | star-r1:28–29 ((2.1), (F1) [which encodes 2m ≤ k], (0.1'), m−1 ≤ m' ≤ m, m' ≥ 1, floor inequality; (0.2') only in comparison/simplification) | ADDRESSED |
| m4 (36) | star:22–29 | LF proof incomplete; compact form | star-r1:30–42 (compact forms, both doubled-difference vectors, d = 0 vector, 2↔4 reflection, discarded linear term) | ADDRESSED (verified, §4) |
| m5 (45) | star:40, 46, 63 | PIN superfluous | star-r1:60–61, 67–69, 95–96; seedXstar3 real modes 0/1/3 omit PIN, MODE2 keeps a mutation-only pin diagnostic | ADDRESSED |
| m6 (53) | cls:35 | wrap reason | cls-r1:40 | ADDRESSED |
| m7 (57) | cls:6, 25, 54, 58 | stale r1 citations | cls-r1:10, 29, 65, 73 | ADDRESSED (nit R6: "sha256353b0e95" missing space) |
| m8 (65) | cls:39–42 | 'allowed' definition ≠ profiles() | cls-r1:44–52; matches seedX3.py:33–53 clause by clause (read statically) | ADDRESSED |
| m9 (78) | star:84 | "class for class" | star-r1:119–120 (PER-LABEL COUNTS; QQ supplies nesting) + new per-class evidence star-r1:142–144 | ADDRESSED |
| m10 (82) | star:47–49, 70–80 | QQ must cover non-co-occurring/equal formal pairs | star-r1:71–79 (formal domain, four weakened lower bounds, m = 1, 2, canonical containment) | ADDRESSED (verified, §4) |
| m11 (96) | star:81; cls:73–74 | "RA2" not identifiable from aggregate receipt | star-r1:114–115; cls-r1:84–85 ("RA class of base r2 Sec. 6 … subtype not identified") | ADDRESSED; see R4 (new per-class receipt does identify RA2; C0WB-r1:132 still says RA2) |
| m12 (101) | star:84–86 | no OPENE-sensitive X* control; per-class failure report | star-r1:129–131, 145–159 (MODE3 = ±1, tight2, 4-unit ablation, P2 negative fixture, per-class first-failure records) | ADDRESSED (MODE3/tight2 openly declared OPENE-insensitive; the 4-unit ablation and P2 fixture are the sensitive controls) |
| m13 (109) | seedXstar2.py:13, 64; seedX2.py:111 | no exec-source hashes | star-r1:131–133, 137–140; cls-r1:97–99, 104–107 | ADDRESSED going forward (old receipts explicitly not retro-hashed) |
| m14 (115) | star:82–83 | interpretive overreach (= Codex M1) | star-r1:116–118 | ADDRESSED |
| m15a (122) | star:78–80 | label X/X* totals [W+F] | star-r1:112–113 | ADDRESSED |
| m15b (123) | star:71–77 | OPEN0 X* column = all passing | star-r1:111–112 | ADDRESSED |
| m15c (124) | seedXstar2.py:2 | wrong filename | seedXstar3.py docstring cites proof-SEEDGstar-r1.md (frozen seedXstar2.py unchanged) | ADDRESSED in new code |
| m15d (125) | seedX2.py:16; seedXstar2.py:6 | cite r2 | seedX3.py:17 (r2); seedXstar3 docstring | ADDRESSED in new code |
| m15e (126) | seedX2.py:6 | docstring E ≥ 2 vs E = 0 processing | seedX3.py docstring; cls-r1:97 | ADDRESSED |
| m15f (127) | cls:30 | state properness and S1 total | cls-r1:34–35, 38 | ADDRESSED |
| m15g (128) | cls:78 | unproved "generic seeds attain (QS) bounds" gloss | cls-r1:88–90 | ADDRESSED |

### C. Codex C0WB note (`olson-c0wb-codex-review-v1.note.md`, sha256 dbb85529…bd5e; ACCEPT-WITH-FIXES, FATAL 0 / MAJOR 0 / MINOR 5)

| ID (note LF) | r0 location | finding | r1 text (pinned LF) | status |
|---|---|---|---|---|
| MINOR-1 (17) | C0WB:121 | "exactly those" converse false | C0WB-r1:141–147 ("SUFFICIENT family … no converse is proved"); C0WB-r1:83–84 | ADDRESSED |
| MINOR-2 (41) | C0WB:71 | "n_ev,al = E cannot occur there" too strong | C0WB-r1:82–84 (Codex's corrected statement) | ADDRESSED |
| MINOR-3 (64) | C0WB:87 | X** quantifier vs seedXX.py | C0WB-r1:104–112 (profiles not already excluded by a configuration-derived empty σ_π at a guaranteed weight; σ_π(d) = [a_π(d), b_π(d)]; vacuous case) | ADDRESSED |
| MINOR-4 (76) | C0WB:92, 96, 110, 106–109 | census lower prime bound | C0WB-r1:116, 119, 120, 130, 134; p = 5, 7 remark C0WB-r1:153–154 | ADDRESSED |
| MINOR-5 (89) | C0WB:10, 12 | path convention; review qualifier | C0WB-r1:20 (../../inverse-parity/…, resolves from mixdef-high/; file exists), 21–23 | ADDRESSED |
| required (161–170, 215) | C0WB:75–80 | explicit F3 brackets; actual-empty before endpoints | C0WB-r1:93 (k ≥ kB+3B AND [2kB ≤ p OR ∀t …]); 88–89, 95, 102, 110 | ADDRESSED |
| imported (186–192) | star:42–43, cls:35, star:82, floats | conditions of acceptance | repaired in star-r1/cls-r1; C0WB-r1:17–19 imports the r1 texts; floats C0WB-r1:155–157 | ADDRESSED (R5: C0WB-r1 does not itself say the r1 imports are unreviewed) |

### D. Claude C0WB note (`olson-c0wb-claude-review-v1.note.md`, sha256 76b4c909…bd512b; ACCEPT-WITH-FIXES, FATAL 0 / MAJOR 0 / MINOR 6 + imported i1–i4)

| ID (note LF) | r0 location | finding | r1 text (pinned LF) | status |
|---|---|---|---|---|
| m1 (15) | C0WB:82–84 | SA**/PA** misquotes base; per-word; actual-empty alternative | C0WB-r1:97–103 (per-word restatement; regions, b*, m unchanged; quality seeds or actual-empty; class conditions as sufficient) | ADDRESSED |
| m2a (29) | C0WB:78 | F3 unbracketed | C0WB-r1:93 | ADDRESSED |
| m2b (30) | C0WB:75–78 | a_t quantified before actual-empty discharge; name (QS*)/(P2)/(PIN) | C0WB-r1:88–90, 94 (PIN stated automatic) | ADDRESSED |
| m2c (31) | C0WB:80 | cite PROOF of SEED-G*/SEED-G stopped before C0+ | C0WB-r1:33–35, 95–96 | ADDRESSED |
| m3 (38) | C0WB:86–88 | X** quantifier; σ_π notation | C0WB-r1:104–112 | ADDRESSED |
| m4a (49) | C0WB:120–121 | "exactly" false | C0WB-r1:84, 146–147 | ADDRESSED |
| m4b (56) | C0WB:120 | premise holds only for count-clause violators | C0WB-r1:83, 145–146 | ADDRESSED |
| m4c (59) | C0WB:70–71 | n_ev,al = E remark | C0WB-r1:82–83 | ADDRESSED |
| m5 (63) | C0WB:92–96, 106, 110, 112–121 | [W+F] label; ranges; p = 5, 7; replay bookkeeping; zero Case-B | C0WB-r1:116–119, 120, 130, 134, 141–148, 153 | ADDRESSED — r1 also CORRECTS the note's bookkeeping: replayW_mut1.txt has 1,440 C0W outcomes and no C0B outcome (the note said 420 C0B for MUT1); MUT3 has 401 + 19 = 420 C0B |
| m6a (71) | C0WB:11 | "wording fixes only in Sec. 2" | C0WB-r1:21–23 | ADDRESSED |
| m6b (72) | C0WB:10 | path | C0WB-r1:20 | ADDRESSED |
| m6c (73) | C0WB:7–9 | imports omit cls; star/cls review status | C0WB-r1:17–19 | ADDRESSED (R5 residual) |
| i1–i3 (77–79) | star:42–43; cls:35; seedXstar2 floats | imported repair conditions | star-r1:62–66; cls-r1:40; C0WB-r1:155–157 | ADDRESSED |
| i4 (80) | star:82 | not inherited | C0WB-r1:130–131 keeps the seed-failing class | consistent |

## 4. Own in-memory arithmetic (aids, not premises)

Own code only (`delta_arith_check.py`, sha256 `96a716d692254b69a3aabeaa73b3298e76f13c9794af5a9f08fc212bbb0ed02a`; output `arith-check.json`, sha256 `212ff00f46b41e4282f269fa8229b8ade63ce35193c1ec1a98b0e0c4257dd258`), run once with `/usr/bin/python3 -B` (Python 3.9.6, 188.1 s, one process). No lane module was imported or executed; lane receipts were only parsed as text/JSON. The JSON uses `collections.Counter`, so **a failure key that is absent means zero** (checked keys: `closed_form_mismatch`, `vector_mismatch`, `reflection_mismatch`, `r0_extra_term_attains`, `real_gap_below_3_2`, `integer_relaxation_formula_mismatch`, `integer_gain_below_2`, `term_bound_fail_in/out`, `min_sum_identity_fail`, `sum_below_L`, `P2_fail`, `fail`, `violations`). Class enumeration is my own from the written setting (proof-SEEDG-r2.md:41–46); at 11 ≤ p ≤ 31 it reproduces exactly the class-ID sets of the new receipts (2,154 at p ≤ 23; 7,264 at p ≤ 31).

1. **LF closed forms (star-r1:30–42)** — abstract domain Δ0 ∈ [3,40], E even ∈ [0,40], κ ∈ [2,15], 1 ≤ B ≤ κ−1, −min(B,E+1) ≤ d ≤ E+1: 2,250,892 tuples; class domain (all 101,472 classes at primes 5–61): 2,683,817 (class, weight) tuples. Zero mismatches for: the compact forms L_A=(Δ0+E+3−max(d,−1))/2, L_B=(Δ0+E+3+min(d,1))/2=L_A(−d); every entry of both displayed doubled-difference vectors for d=u≥1 (all ≥ 0); the d=0 vector and its 2↔4 exchange; the negative-d reflection (A/B collections exchanged with entries 2↔4); r0's discarded linear term never attains.
2. **Relaxation (star-r1:44–51)** — minimum continuous gap exactly 3/2 (never below; attained), exact integer formula (h+2, J(d)) / (h+2, h+2) / (J(−d), h+2) with J(u)=h+2−⌊(u−ε)/2⌋: zero mismatches; minimum integer gain exactly 2 (never below). **So QS* relaxes QS by ≥ 3/2 real units and ≥ 2 integer endpoint units on each side, before canonical clipping and P2.** The literal sentence at star-r1:44 ("(E−|d|+4)/2 on the far side") fails only at d = 0 (all 83,790 abstract / 101,472 class mismatches have d = 0, where both gaps are (E+3)/2) → R1.
3. **Codex's legal large case** p=2^61−1, Δ0=2^60+200, κ=p−Δ0, k=p+κ, B=d=1, E=0: exact ⌈L_A⌉ = 576460752303423589 = 2^59+101, ⌈L_B⌉ = 576460752303423590 = 2^59+102 (matches the worker's `out/star3_exact_controls.txt`); an in-kernel float transcription of the r0 formula reproduced the +27/+26 overshoot (exploratory, not in the JSON).
4. **Minimum-over-term-sums (star-r1:62–66)** and the facts-used list (star-r1:28–29) — primes 5–23, every (class, d, y', m, m') with (2.1), 2m ≤ k [(F1)], m−1 ≤ m' ≤ m, m' ≥ 1: 19,091,434 domain tuples, all 18 displayed term bounds hold, lam(y',m')+lamc(y,m) = min U + min T exactly, sums ≥ L_A / L_B; the r0 wording "≥ each of the nine bounds" is false in 17,374,592 of them (so the repair was needed). The same 18 bounds also hold on 9,940,572 tuples with d up to 3 beyond (0.2') on each side, supporting "(0.2') enters only the later comparison".
5. **Extended QQ (star-r1:71–79)** — primes 5–61, all formal weight pairs d1 ≤ d2 in [−min(B,E+1), E+1] with e(d1)+e(d2) ≤ E, both m ∈ {1,2}, extreme seeds of the QS ∩ canonical windows: 57,173,708 cases, zero P2 failures, including 3,209,034 equal-weight and 3,350,586 y < −B (non-co-occurring anti) cases. Codex's hand example (11;13,2,1), d1=d2=1, intervals [−3,−3] (QS but below λ(1,1)=1) violates P2 at m=1,2 (sum −6 < −5) — re-checked in-kernel — so the canonical lower endpoint really is needed, as star-r1:79 says.
6. **Automatic PIN (star-r1:60–61, 67–69, 95–96)** — Lemma P0 λ({t})+λ({t}^c) ≥ 1 on all 2,683,817 (class, weight) cases at primes 5–61: zero failures.
7. **C0WB repairs** — p = 5, 7: max E = 0, 2 (C0WB-r1:153 "E ≤ 2, so (i)"); sufficient-family algebra (k ≥ kB+3B, n_ev,al ≥ 2(k−kB−2B)+n_pr, n_an ≤ B−n_pr ⇒ n_ev,al > B+n_an−2): 862,866 cases, zero violations; Codex's relaxed Case-B example (17;21,7,4) with n_ev,al = E = 6, Σx = 17, singleton bounds met, Z = anti block, Φ(Z) = 3 = kB: reproduced (relaxed singleton+sum data only, not a (0.2) solution or group counterexample), consistent with C0WB-r1:82–83 "not ruled out in general".
8. Own count of small-domain weights at primes 11–43 = 528,214 (= the worker's 528,214).

## 5. Receipt / provenance reconciliation (own parsing; text only)

- New receipts' per-label counts equal the historical ones: star3 MODE0 = seedXstar2 MODE0 (11 ≤ p ≤ 31), X3 MODE0 = seedX2 MODE0 (11 ≤ p ≤ 23), star3 MODE1 = seedXstar2 MODE1 — all true.
- star3 MODE1 vs X3 MODE0: 2,154 class IDs, 0 verdict/label mismatches (star-r1:142–144, cls-r1:104–106).
- MODE0: 70 failures, all first stage QS* (IE 38, IS 21, OPEN0 10, OPENE 1); the OPENE failure is (31;51,24,23), profile (26,28,8,1,false), weight 8, seed [8,8], required [−2,7] — exactly star-r1:145–148 (and README Sec. 34). My closed form gives the same required range (Δ0 = 3, E = 8).
- MODE3: 151 failures (all QS*); changes vs MODE0: IS 46, IE 34 pass→fail, OPENE 1 pass-noC+→fail; tight2 (p ≤ 23): IE 16, IS 34; tight4 (p ≤ 23): OPENE 630 pass→fail, plus W 63, IE 769 (+48 noC+), SB 185, IS 201, OPENE 6 noC+ — all as stated at star-r1:149–154 and in `out/review_repair_summary.json`.
- Replays (C0WB-r1:136–148): MUT0 1,320 C0W + 360 C0B (all Case-A kills); MUT1 1,151 broken-M + 289 kills = 1,440 C0W and **no C0B outcome** (r1 is right; the Claude C0WB note's "MUT1 … 420 C0B" was wrong); MUT3 1,440 C0W (622 lost) + 420 C0B (19 lost); replayW2 27/29 words, 1,080/1,160 Case-A kills, zero Case-B. `replayW2.py:41–48` (read only) selects k ≥ kB+3B, 2kB ≤ p and words with n_ev,al > 4 and n_ev,al > 2(k−kB−2B)+n_pr−1, as C0WB-r1:145–146 states.
- The two passing OPEN0 classes in the new per-class receipt are (29;55,26,2) and (31;59,28,2): B = 2, kB = p−5, i.e. RA2 (proof-SEEDG-r2.md:244) → R4.
- New receipt headers record map6.py `a76f8fac…`, ../c4/ind_star3.py `ef0db857…`, ../c4/ind_star_ex.py `8685d3fc…`; these equal the current lane bytes and the copies pinned at 19:14 in `REVIEW/olson-c0wb-inputs-v1/`. This closes Codex's "PARTIAL" on the SC LF-145 remark for the NEW receipts (bytes are available in REVIEW, though not in my snapshot); execution-time bytes of the OLD receipts remain unknown, as the r1 files disclose.
- Static code reading (not executed): seedX3.py differs from seedX2.py only in docstring, imports, `source_manifest()` and detail printing (profile/seed/class_pass arithmetic unchanged, cls-r1:97, 107); seedXstar3.py `bounds()` is exactly twice the eight L_A/L_B expressions with ⌈n/2⌉ = (n+1)//2, MODE3 = (lo+1, hi−1), PIN only in MODE2; `review_revision_runs.py:9–11` sets RLIMIT_CPU (1800, 1860) and RLIMIT_FSIZE 128 MiB, but `out/review_revision_runs.json` contains no limit fields → R3.

## 6. Codex delta review `olson-repair-delta-codex-v1` (static)

- Prompt `REVIEW/olson-repair-delta-codex-v1.prompt.txt` sha256 `99357e7af6c4a8cc831bd05fd62c0fed0aa9e43197347f6f42f7343a62ecb08d`; note `REVIEW/olson-repair-delta-codex-v1.note.md` sha256 `a2abb2023677a5eadbc2f9d88acc3029304690f4710c2a6ffc46e9a5de31d3c3`; receipt sha256 `78a807dd5f1ff1510bd28aa6524bf8af4273b1b8c049be8c21134f561c572cf8`; status NOTE_RETURNED_UNVERIFIED, exit 0, reported identity gpt-6.1-sol / openai / read-only / max, 625 s. Snapshot `inputs/` (manifest sha256 `dd35998fe40b20917f36e54cf6414147777828d0bae9396cd515c135e9b402e1`, 59 files, 3,265,591 bytes). Codex verified all six target hashes, ran no Python/claimant code/solver, and used only read-only commands.
- **DISPOSITION: ACCEPT-WITH-FIXES. FATAL 0, MAJOR 0, MINOR 3** (all three also found independently in my pre-check; see deviation D4 on independence):
  - MINOR-1 `proof-SEEDGstar-r1.md:44` — the far-side gap (E−|d|+4)/2 is stated without excluding d = 0; at d = 0 both gaps are (E+3)/2 (hand example (11;14,4,1), E=2, Δ0=6, d=0: gaps 5/2 vs printed 3). The 3/2 bound, integer relaxation and proof survive.
  - MINOR-2 `proof-SEEDGstar-r1.md:137–138` — attributes CPU/file-size limits to `out/review_revision_runs.json`, which has no limit fields; the hashed driver `review_revision_runs.py:9–11` configures them. `proof-SEEDG-cls-r1.md:107–108` should make the same distinction.
  - MINOR-3 `proof-SEEDGstar-r1.md:12–13` — retained status line calls `seedXstar2.py` "exact integer arithmetic"; its `bounds()` uses float division + `math.ceil` (`seedXstar2.py:23–27`), exact only on the historical range, as star-r1:126–128 itself says.
- Delta verdicts: T1 DELTA-ACCEPT-WITH-NOTES; T2 DELTA-ACCEPT-WITH-NOTES; T3 DELTA-ACCEPT. Finding map: every item ADDRESSED (or NOT-A-LANE-ITEM for the desk's own prompt-hash typo), except SC LF-145 (c4 label dependencies) marked PARTIAL for want of c4 bytes in the snapshot — see Sec. 5 for the hash match closing it for new receipts.
- Codex independently confirmed: the min-over-sums repair; every LF vector entry; J(u) for both parities; automatic PIN; each of the four weakened QQ branch bounds against r2:139–151 (and that the canonical lower endpoint is needed); seedX2→seedX3 arithmetic unchanged; the cls-r1 filter clause-by-clause against seedX3.py:33–53; C0WB F3 bracket/actual-empty order/X** quantifier and vacuous case; the Case-B one-way remark; MUT1 has no C0B replay; RA2 identity of the two OPEN0 passes; DF/C0W/C0B byte-unchanged. "No substantive theorem change in the three supplied diffs falls outside the review findings or the r1 headers' repair lists."
- My spot-checks of Codex's own claims: DF/C0W/C0B block hash (match), its QQ lower-endpoint example (match), its receipt counts (match Sec. 5).

## 7. Residual notes (non-blocking; suggested corrections for the owner)

- **R1** `proof-SEEDGstar-r1.md:44` (Codex MINOR-1; new prose regression): replace by the three-case table — d>0: (E+3)/2 (A side), (E−d+4)/2 (B side); d=0: (E+3)/2 both; d<0: mirror. Own check: mismatch occurs only at d = 0.
- **R2** `proof-SEEDGstar-r1.md:12–13` (Codex MINOR-3; inherited wording): "exact integer arithmetic (c6/seedXstar2.py)" → historical checker exact on 11 ≤ p ≤ 31 via exactly represented half-integers; doubled integers in seedXstar3.py.
- **R3** `proof-SEEDGstar-r1.md:137–138`, `proof-SEEDG-cls-r1.md:107–108` (Codex MINOR-2): limits are set by the hashed driver (`review_revision_runs.py:9–11`), not recorded in the JSON.
- **R4** `proof-C0WB-r1.md:132–133` vs `proof-SEEDGstar-r1.md:114–115`, `proof-SEEDG-cls-r1.md:84–85`: C0WB-r1 says "RA2" while citing the aggregated `out/seedXX_X.txt`; star/cls-r1 say the aggregated receipt does not identify the subtype. Both are true; the new per-class receipt `out/revision_star3mode0.txt` (LF 4413, 7247; re-checked) identifies (29;55,26,2), (31;59,28,2) as RA2. Suggest citing it in all three files.
- **R5** `proof-C0WB-r1.md:17–19`: imports star-r1/cls-r1, whose repairs were "not yet independently re-reviewed" at freeze (their own headers); C0WB-r1 records only the originals' review status. At 23:15 PDT a search of REVIEW for the three r1 hashes/filenames found no other review of these bytes (only this desk's files, and `olson-uniform-claude-review-v1.prompt.txt`, which uses C0WB-r1/star-r1 as imports explicitly labelled 'NOT independently reviewed'/'repairs not re-reviewed'); concurrent desks may exist, so no priority of this check is claimed.
- **R6** `proof-SEEDG-cls-r1.md:10`: "sha256353b0e95…" (missing space); "review fixes submitted" — the r1→r2 delta was DELTA-ACCEPT-WITH-NOTES by SeedGReviewDesk.
- **R7** `proof-SEEDGstar-r1.md:59`: the (P2) item ends with ";" left over from the deleted (PIN) item (cosmetic).
- **R8** `proof-SEEDG-cls-r1.md:83, 87` and `proof-SEEDGstar-r1.md:120`: "Totals p <= 31", "p <= 23" retained beside "primes 11..31"/"11<=p" wording elsewhere (cosmetic; the receipts start at 11).

None of R1–R8 changes a hypothesis, a conclusion or a finite count.

## 8. Scope after the repairs (subject to R1–R8)

- **[W] written:** Lemma LF (compact forms), SCW-G* without a PIN premise, extended QQ, Theorem SEED-G* (well-formed actual-empty alternative), Lemma PR, Lemma CF', the written implications behind Corollaries X, X*, X**; Lemmas DF, C0W, C0B (unchanged), Theorem SEED-G** (F3 bracketed), per-word Corollary SA**/PA** with unchanged regions.
- **[W+F] computer-assisted:** the X/X*/X** class instantiations at primes 11–31 (3,113 of 3,114 OPENE classes excluded under X**: 1,793 by the written SA/PA regions and 756 X + 187 X* [W+F], all with C+'s class condition, plus 377 by the count-free finishers F2/F3/F3* (343 + 19 + 15)), and the SA**/PA** region-class instantiation at primes 11–61. Receipts reconciled statically/by parsing; the class enumerations were not replayed by this desk.
- **[F] aids:** label partitions (map6.py + c4 code), counts, controls, mutations, replays (Case B has zero empirical instances).
- **Open:** (31;51,24,23) (seed test fails, QS* at weight 8); ten OPEN0 seed-failing classes at p ≤ 31; p = 7 classes (kB,B) = (2,2), (1,3) and (11;5,3) outside SA/PA; everything beyond the census ranges; NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV*, ordered Olson.

## 9. Correctness / novelty / significance (separate)

- **Correctness:** all reviewed repairs are mathematically adequate; no new mathematical error found by my arithmetic or by Codex; residual items are wording/provenance (R1–R8).
- **Novelty:** none assessed beyond this ledger; the r1 texts complete and clarify existing conditional arguments and their evidence attribution. No external novelty or priority check was performed; no firstness claim.
- **Significance:** unchanged from the reviewed originals: finite and modest (the repairs neither add a uniform seed-existence theorem nor change any finite count).

## 10. Deviations (reported, not hidden)

- D1. Read-only inspection used shell `ls`, `grep -E`, `awk`, `cut`, `cat`, `wc` and `cd … &&` in bash for listings/hashes instead of specialized tools. No file was modified by those commands.
- D2. A first in-kernel LF check with `fractions.Fraction` hit the 30 s cell limit and was interrupted (no file written); the checks were redone with doubled integers, first in the eval kernel (Python 3.14.3, used for my analysis) and then as the saved script (Python 3.9.6) whose JSON is authoritative. Results agree.
- D3. The snapshot includes ≈2.8 MB of per-class receipt text so Codex could check Sec. 5 claims by grep; free disk at creation was ≈13.8 GB (> 12e9 floor). No CNF or binary copied. The C0WB desk artifact list was copied from `agent://OlsonC0WBReviewDesk` (no file existed) into `inputs/desk/olson-c0wb-desk-final-output.md` with a provenance header.
- D4. The Codex prompt explicitly asked it to check several items my pre-check had already flagged (d = 0 gap sentence, JSON limits, RA2 per-class identification, MUT1 count, "exact integer arithmetic", unreviewed imports). Codex's agreement on those items is therefore not fully independent. For the other items the prompt asked for verification without stating an expected outcome.
- D5. Only the requested Codex review was run (no Claude delta review). No lane code was executed; the old floating implementation was not run (only my own float transcription of the r0 formula, in-kernel, for one large input).
- D6. `arith-check.json` omits zero-valued counters (Counter semantics); Sec. 4 lists the failure keys whose absence means zero.
- D7. `delta-check.md` (v1) contained the two wording errors corrected here (R5 'first check' claim; D4 'unprompted in content'). v1 is kept byte-unchanged; this v2 is authoritative.

## 11. Artifacts (all created exclusively by this desk under REVIEW; sha256)

| path (relative to REVIEW) | sha256 |
|---|---|
| `olson-repair-delta-v1/diff-SEEDGstar-r0-r1.txt` | `8963161d6f4591b7f448b2c18fd9b895fb80be76d81aa12be97b78158325ef3b` |
| `olson-repair-delta-v1/diff-SEEDG-cls-r0-r1.txt` | `22108e95ddf87c6af2ff56dcee83904d6417befc79057fd90a53555d2d08dc28` |
| `olson-repair-delta-v1/diff-C0WB-r0-r1.txt` | `69c94a704b208abf17e35d867d13d40a196962708054cfa44c3e8d33c33f2e8a` |
| `olson-repair-delta-v1/delta_arith_check.py` | `96a716d692254b69a3aabeaa73b3298e76f13c9794af5a9f08fc212bbb0ed02a` |
| `olson-repair-delta-v1/arith-check.json` | `212ff00f46b41e4282f269fa8229b8ade63ce35193c1ec1a98b0e0c4257dd258` |
| `olson-repair-delta-v1/inputs/manifest.json` (pinned Codex snapshot, 59 files) | `dd35998fe40b20917f36e54cf6414147777828d0bae9396cd515c135e9b402e1` |
| `olson-repair-delta-codex-v1.prompt.txt` | `99357e7af6c4a8cc831bd05fd62c0fed0aa9e43197347f6f42f7343a62ecb08d` |
| `olson-repair-delta-codex-v1.note.md` | `a2abb2023677a5eadbc2f9d88acc3029304690f4710c2a6ffc46e9a5de31d3c3` |
| `olson-repair-delta-codex-v1.receipt.json` | `78a807dd5f1ff1510bd28aa6524bf8af4273b1b8c049be8c21134f561c572cf8` |
| `olson-repair-delta-codex-v1.stdout.txt` / `.stderr.txt` | runner logs (unchanged) |

Superseded v1: `olson-repair-delta-v1/delta-check.md` (`88133a19fead27b157d6eac39a527538b25ff77dcc0992bf9e7ec1aef82156b1`). This file's own hash and a full created-file inventory are in `olson-repair-delta-v1/created-files.json` (created after this file).
Inputs consulted (not created here): the four notes (hashes in Sec. 3 headers; they equal the worker's `review_repair_summary.json` entries), `olson-c6g-r2-review-summary-v1.md` (`5ad5049e3717ee148e16fa7ba783e76ae893219e0aeaa0cc73946d80b97541f8`), the C0WB desk output (`agent://OlsonC0WBReviewDesk`), worker `out/review_repair_summary.json` (`1c4656b4938ab8d0526ab85366b60b700db8ae687fc1abedf8c88552bb89f11e`) and README (`50751f259afeb5b259fc8d0914a4bc937341e8a3a4a3968161c47c90163cec75`, Sec. 35 at LF 538–550).
