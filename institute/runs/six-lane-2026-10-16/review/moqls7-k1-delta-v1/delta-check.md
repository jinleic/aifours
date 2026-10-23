# moqls7 K1 delta check (delegated parent delta check)

**DELTA-ACCEPT-WITH-NOTES**

This verdict is a delegated parent delta check by desk M7K1DeltaDesk, written 2026-10-17T23:09:11.149468-07:00 (host clock, PDT). It is not
the parent's theorem verdict, which remains with the parent. All line references are LF-lines: 1-based indices into
text.split('\n') of the pinned copies.

## 1. Pinned inputs
Snapshot: `review/moqls7-k1-delta-v1/snapshot/`. Its `manifest.json` (sha256
817b9fce2e8af6f2486ee466866c2b0e1997ac8eaef8ea5b436c14a6dcc1e8c4) lists 38 files. Every copy was checked as
byte-identical to its source.

Lane P = `physics/evidence/six-lane-20261016/moqls7-maximum`; REVIEW = `institute/runs/six-lane-2026-10-16/review`.

| item | sha256 | assignment value |
|---|---|---|
| P/review/K1-THEOREM.r1.md | b702b021e94aafeaace754370b79a2f11c0e8bfebcfb3a3984df720d0e728767 | matches |
| P/review/K1-THEOREM.r2.md | 98b06d226d0c53d7db53540a6760be049e6df3aaba62aefdfa69024837842f59 | matches |
| P/review/K1-THEOREM.r3.md | 2d77c63719fafd1e7f7cfe2a3161931f2e90dff0976e3ee9c5083a88d076a096 | matches |
| P/review/LEMMAS.md | 4bddc9d422cf989bb9bfdf4f09de72742ea2d423b9a082f8fd76263ba1c850c9 | matches the worker-reported 4bddc9d4…50c9 |
| P/review/REVIEW-CORRECTIONS.r2.json | 5105a6864bcc6a415df29531e87bd742931cc4e55502841f7b83fafeeb070770 | not given |
| P/review/K1-COROLLARY.r1.md | 7ded3c698163c18757a21964d3552e053f1081f9fd854895054a606e56ef6b6d | matches the parent IRC |
| REVIEW/moqls7-k1-review-codex-v1.note.md | 54a83ff321e4d068e494d4b53b6a95efaf1208306481ba73e04b1469d51fdf34 | equals its receipt |
| REVIEW/moqls7-k1-review-claude-v2.note.md | 9ed374609f6b5499e26338d4d6893346b3cea0b1699d43d07e1708dfa43efb68 | — |
| REVIEW/moqls7-k1-parent-check-v1/RESULT.json | f46a741602fcc36cda6828e282063d14cb8df4bb4f3fbc81bccbb3db74396570 | — |
| …/route2/receipt-route2.json | 506b466d0fef11578a06370dd7f94190fe72357fd81e1ad6425c2588b1189701 | equals r3:93 and RESULT.json:25 |
| P/README.md (pinned later version) | 548915aec87f… (see manifest) | — |

Arrival and change notes:
- K1-COROLLARY.r1.md was absent at 22:42 and was frozen by the lane at 22:43; the pinned copy matches.
- README.md changed during the session (7c5c5d84… at 22:42), so the later version was pinned.

## 2. Exact diffs
Files in `snapshot/diffs/` (difflib unified diff, context 3):

| diff | sha256 |
|---|---|
| K1-THEOREM.r1-to-r2.diff | 54abde67fd9bbceb3a7a073a411d2a7e0fbddcc9bbc33fe35e01576d539346d1 |
| K1-THEOREM.r2-to-r3.diff | 7075515dac3a8207c072392c10623a2928693791a17e84903321193c8b5d6632 |
| K1-THEOREM.r1-to-r3.diff | 93efea3bb7572c93a3345dc3deb77c5da928d136c889c32024cf2363314b9ccf |
| README.reviewed-to-pinned.diff | 99dc3d9d22ce9ba801c84c4a854ef13b8d38581d4af503ff272a086c126dbb26 |

The README diff runs from the review-pinned copy 6afea008… to the current pin.

**r1→r2 (2 hunks):**
- §3: sets/lists wording and trust-base sentence.
- §4: full driver SHA.
- §5: the 315/97/MILP sentences are replaced by an explicit non-claim.
- Unchanged in r2: the producer drat-trim control-outcome claim and the solver versions (r2:66–73).

**r2→r3 (6 hunks):**
- Status line.
- §1: new straightening/ray/C0 paragraph (r3:8–14).
- §3: net_canon wording, flag/free-action argument and parent RESULT citation (r3:51–53, r3:68–78).
- §4: solver-version withdrawal and route-2 control citation (r3:83–97).
- §5: row references (r3:129–131).
- §7: C1 wording, evaluator/encoder note and void-history relabel (r3:148–160).
- §8: case split (r3:172–175).

The statement of Theorem K1 (r3:139–142) is unchanged since r1.

## 3. Finding map: both K1 notes → current text
The full table is in `finding-map.md` (sha256 1f8926aa…829a). It was written at 22:58:58, before the Codex delta note
was read. The Codex delta note gives an independent map (§8).

| finding | desk status → current text | Codex delta status |
|---|---|---|
| Codex v1 MAJOR 1 (r1:70–71) | RESOLVED; residue is wording only → r3:90–97 | PARTIAL, minor residue only |
| Codex v1 MAJOR 2 (r1:110–111) | RESOLVED → r3:136–137 | RESOLVED |
| Codex v1 MINOR 1 | RESOLVED → r3:82, README:7 | RESOLVED |
| Codex v1 MINOR 2 | RESOLVED → r3:66–67 | RESOLVED |
| Codex v1 MINOR 3 | RESOLVED → r3:51–53, r3:68–71 | RESOLVED |
| Codex v1 MINOR 4 | RESOLVED → r3:83–86 | RESOLVED |
| Codex v1 MINOR 5 | RESOLVED in substance → LEMMAS:3–4 and :38–52; r3:77–78; r3:158–160 | RESOLVED |
| Claude v2 MINOR 1 | RESOLVED in substance → r3:82, r3:92–97 | RESOLVED |
| Claude v2 MINOR 2 | RESOLVED → README:7 | RESOLVED |
| Claude v2 MINOR 3–6 | RESOLVED → r3:83–86, r3:90–97, r3:136–137, LEMMAS.md | RESOLVED |
| Claude v2 MINOR 7 | RESOLVED for the text, r3:66–67 | RESOLVED |
| Claude v2 MINOR 8 | RESOLVED → r3:51–53, r3:68–71 | RESOLVED |
| Claude v2 MINOR 9 | RESOLVED in substance → r3:73–78 | RESOLVED |
| Claude v2 MINOR 10–13 | RESOLVED → r3:8–14, r3:129–131, r3:172–175, r3:148–157 | RESOLVED |

Residues behind the qualified statuses:
- Codex v1 MINOR 5: k1_sat.py:15 still cites a "K1 weight lemma" that LEMMAS.md does not name. The `--w3` option it belongs to is unused (k1_certify.py:52).
- Claude v2 MINOR 1: the binding of the driver to its outputs comes from the parent byte-exact replay, not from the lane summary.
- Claude v2 MINOR 7: the r3:55 header and the frozen comment net_canon.c:7 are numerically harmless at k = 2.
- Claude v2 MINOR 9: r3 cites RESULT.json by path only.

No finding is unaddressed.

## 4. MAJOR 1 (unreceipted drat-trim control outcomes): resolved by hash-bound parent controls
r3:90–91 withdraws the producer outcomes ("Original producer control outputs were not saved"). It also correctly
describes the lane `ctl_unsat.drat` as the two-byte step `0` plus LF (sha 9a271f2a…86aa). r3:92–97 cites the parent
route-2 receipt by full SHA-256.

The desk followed the hash chain:
- r3:93 → `receipt-route2.json` 506b466d…9701, which equals RESULT.json receipts[1].
- receipt → `outputs` → `verify/route2-verify.json` 16ff38d2ec9df076affa3d593861975fa70554f54c54355cf80c6f341a3c5378.
- That file → per-control `stdout_sha256`. All six equal the raw files:
  - `dt/ctl_sat_emptyclause.out` eb3c96af…0735
  - `ctl_unsat_empty.out` 6459c58a…9232
  - `ctl_A5_base.out` b2bd4dd0…
  - `ctl_A6_base.out` 039c52da…
  - `ctl_B6_base.out` 0bfecf18…
  - `ctl_A6_minus_w4.out` 33365830…

The six controls in `results.controls` and `drat_runs` match r3's description:

| control | CNF / proof | exit, status |
|---|---|---|
| SAT CNF + empty-clause proof | sat.cnf 6642f3ff… + emptyclause.drat 9a271f2a… | rc1, `s NOT VERIFIED` |
| contradictory-unit CNF + truly empty proof | unsat.cnf ac42a371… + empty.drat e3b0c442… (0 B) | rc0, `s VERIFIED` |
| lane A5 proof against SAT base A5 | — | rejected |
| lane A6 proof against SAT base A6 | — | rejected |
| lane B6 proof against SAT base B6 | — | rejected |
| A6 final CNF minus the weight-4 block (SAT) | — | rejected |

The 14 production proofs A0–A6 and B0–B6 are all `s VERIFIED` under the parent checker (binary a46c0c71…8e37). The
parent receipt also records the solvers it used (cadical 3.0.1, sha 601c9fa8…; kissat 4.0.4, sha 05d6f3e9…).

The lane control inputs are byte-identical to the parent's sat.cnf, unsat.cnf and emptyclause.drat
(`snapshot/controls-binding.md`). r3 asserts no producer output that was never saved. Codex agrees: "No original
producer control outcome or run-specific solver-version claim survives".

Two wording residues remain (MINOR; §8):
- r3:94 "separately built". The cited route-2 receipt shows only a different binary hash. The build record exists
  elsewhere in the parent's files: `REVIEW/moqls7-parent-proofcheck-v1/parent-result.json` (sha256
  200d307dd52ab4d6559ff89d5faa6c3859e256bbd20c6d1fb439d237b9af3bfe) records source d834b649…c2ee from upstream
  2e3b2dc0, binary a46c0c71…8e37, compiled with `cc -O2`. Cite that file, or adopt Codex's wording.
- r3:89 attributes the original `s VERIFIED` outcomes directly. They come from driver-parsed summary fields, not
  retained raw stdout. The parent replay re-ran the pinned drivers with the lane binary 111b0405… and reproduced
  those fields (replayA/B summaries; route-2 2a/2b PASS). The parent checker's raw stdout exists for all 14 proofs.

## 5. MAJOR 2 (315 / 97 / MILP / minimality): resolved
The two r1 sentences are deleted, starting in r2. r3:136–137 states: "No minimality claim, independent-count claim,
or acceptance of the exploratory elimination/MILP output is made." A grep of r3, LEMMAS.md and K1-COROLLARY.r1.md
finds no "97", "315" or minimum-size phase claim. MILP appears only inside that disclaimer. The minimum in
LEMMAS:70–75 concerns the number of non-classical squares, which is unrelated.

## 6. New content since r1
The desk re-derived each new argument, and the Codex delta note agrees on every point. No new mathematical defect
was found.
- **r3:8–14, straightening/ray criterion/C0:** sound under Ball–Simoens isotopy, since per-square unitaries act
  independently.
- **r3:68–71, flags:** there are 4!·49·6! = 846720 flags. An automorphism fixing a flag fixes every line of the other
  three classes, then every point by intersection, so the action is free. Fibres are Aut-orbits, so each reduced
  image has exactly |par| preimages. r3:51–53 matches net_canon.c:68–74.
- **r3:129–131:** rows 1+3 give Δ28(4,6) ≡ Δ34(4,5)+Δ29(5,6). Rows 6+7 give Δ26(4,6) ≡ Δ29(0,6)−Δ34(0,4). Rows 2 and
  5 equate them, so Δ34(0,5) ≡ Δ29(0,5), which contradicts row 4.
- **r3:148–150:** 294 = 42·7 = 84 additions + 210 removals.
- **r3:172–175:** the case split and sequential classicalization are correct.
- **LEMMAS.md:** C0, C1, W, frame/F1–F4, the arbitrary-basis Lemma 10 and G4 are all sound. Its late origin is
  disclosed at LEMMAS:3–4.
- **REVIEW-CORRECTIONS.r2.json:** its `new_texts` hashes match the files, and GRAM-ENCODING.md is byte-identical to
  GRAM-ENCODING.r2.md (c6c506a7…).

Desk MINOR residues (non-blocking):
- **D-m1:** r3:74–75 cites RESULT.json by path only. Add its sha256 f46a7416…6570, as r3 does for route 2.
- **D-m2:** frozen docstring k1_sat.py:15 cites a "K1 weight lemma, review/LEMMAS.md" that has no exactly named
  counterpart. The `--w3` option is disabled in production (k1_certify.py:52), so an overlay note suffices.

Optional wording: Codex suggests labelling the remaining history at r3:77–78 and r3:158–159 as "unverified history".

## 7. Corollary note K1-COROLLARY.r1.md: bridge checked by the desk
**Computation.** `bridge_check.py` (sha256 d1ddbb13…2968) is stdlib-only, ran as one process in 0.064 s wall, and
writes nothing. Its result is `bridge_check.result.json` (e7f49583…32b0) and its run record is
`bridge_check.run.json`. It read P/evidence/nets7_classes.json (78d1728f…0d67, matches) and found:
- **B1:** the pandiagonal net (x=c, y=c, y−x=b, y+x=b; point 7x+y) satisfies the 4-net axioms. Its directions are
  {∞,0,1,6=−1}, with cross-ratio set {2,4,6}, which is harmonic.
- **B2:** the shear (x,y)↦(x,y+x) is a bijection and maps all 56 lines of AG(2,7) to lines. Its image has directions
  {∞,0,1,2} and equals class 5 line-for-line and class-for-class:
  - pandiagonal x maps to class-5 coordinate 0;
  - y maps to y−x;
  - y−x maps to y−2x;
  - y+x maps to y.

  The image is not class 6, the unsheared net is not literally class 5, and the image is no maximal class.
- **B3:** at all 49 points, class-5 labels are (x,y,y−x,y−2x) (origin "desarguesian-harmonic", cross ratios
  {2,4,6}) and class-6 labels are (x,y,y−x,y−3x) (equianharmonic, cross ratios {3,5}).
- **B4:** each broken diagonal or anti-diagonal meets every row and every column once. The two diagonal resolutions
  are orthogonal (every pair of lines meets in one cell), and the main diagonal and anti-diagonal are lines of the
  respective families.

Codex independently spot-checked ten points against the JSON.

**Cardinality 7 = classical for one square.** Zhang–Cao (ZC) and Huang–Li (HL) both count vectors distinct up to a
global phase, i.e. rays. Every row is an ONB, so there are at least 7 rays. With exactly 7, every entry is parallel
to the row-0 basis, and a unitary maps that basis to the standard basis, which gives Ball–Simoens classicality. A
classical square has exactly 7 rays. ZC's own "classical" means computational-basis entries, and ZC calls c > v
"non-classical". The note uses the Ball–Simoens sense explicitly (COROLLARY:7–10), which is correct.

**Zhang–Cao Lemma 2.2** (arXiv 2608.29201v2; PDF sha256 dc525efe…ac43; ≤40-word quote): "A is a t-RQLS(v) if and
only if there exist t classical QLS(v)s, B0, …, Bt−1, such that A, B0, …, Bt−1 form a (t + 1)-MOQLS(v)."

Corollary 1 uses the forward direction. ZC's printed proof sets |b^(r)_ij> = |k> on T^(r)_k, and ZC's orthogonality
(Definition 2.1, product ONB) is the Ball–Simoens notion. So a non-classical 2-RQLS(7) would be a K1 triple, and
Corollary 1 is correct.

**Corollary 2.** HL's definition of PQLS(n) (HL v1 Introduction; PDF sha256 dc0264f5…8c63) gives two orthogonal
transversal resolutions (B4), so PQLS(7) ⇒ 2-RQLS(7). The harmonic route is equivalent (B2), so Corollary 2 is
correct.

**Dependency.** The harmonic route needs only K1's class-5 clause: frame lemma, F1–F4, the class-5 enumeration with
its DRAT-checked final UNSAT, and the all-singleton conclusion. It needs neither class completeness, the maximal
nets, the class-6 phase cycle nor §8. Corollary 1 needs all of K1. Codex reached the same split.

**Scope against sources** (desk in-memory fetch receipt `source_fetch.receipt.json`, sha256 76b2f905…c8e4; all 17
anchors found):
- HL v1 §5 "Conclusion" says MCPQLS(5) does not exist and that "the existence of MCPQLS(7), MCPQLS(11), and
  MCPQLS(n) with gcd(n, 6) ≠ 1 remains to be determined".
- ZC v2 §5 records maximal-cardinality 2-RQLS(v) only for gcd(v,6)=1 with v ∉ {5,7,11}, or v = n² with n ≥ 6. It adds:
  "It remains to determine the existence of maximal-cardinality 2-RQLS(v)s for the remaining orders".
- The note's two "addresses the order-seven case" sentences (COROLLARY:31, :49) are therefore accurate.
- Ball–Simoens 2603.02334v1 (PDF sha256 66e43b92…bcd), Lemma 21, sits in §4.2 "Checking twelve cases" and states the
  order-6 classical-companion/orthonormal-representation equivalence. The prior-art acknowledgement (COROLLARY:20–25)
  is accurate.
- There is no "first", priority, novelty, M(7) or K2/K3 claim. Both corollaries inherit K1's status (COROLLARY:3–4)
  and are scoped against classical PQLS(7) and DQLS(7) (COROLLARY:51–53).
- The HTML anchor links in the note were not opened; the PDF content was verified instead.

**Aid F1** (computed; not a premise). Z_7 has 28 strong complete mappings, and all 28 are affine. Every HL-type
Fourier PQLS(7) has exactly 7 rays, with all line ONB checks exact. This is consistent with Corollary 2 and with HL
leaving 7 open: a non-affine example would have given a 49-ray PQLS(7).

## 8. Codex delta review `moqls7-k1-delta-codex-v1` (static, gpt-6.1-sol, effort max, read-only)

| artifact | sha256 |
|---|---|
| prompt `REVIEW/moqls7-k1-delta-codex-v1.prompt.txt` | ae704795fe098cae065701a6ad24db67c632b4ccf2ce5c7b8313ef0348baefa8 |
| note `REVIEW/moqls7-k1-delta-codex-v1.note.md` | 7a768a1f5cf336d839c6e211c10006d987bb24fccb39bc15fb66912591fc365f |
| receipt | 2a145721368eb232b01a10b76f63d14ca9ef1817b1b75e26d933e11d4c6274ac |

The receipt reports NOTE_RETURNED_UNVERIFIED, rc 0, 439.9 s, identity gpt-6.1-sol/openai/read-only/max.

Compliance: the desk parsed the stderr log, which shows 47 commands: 42 nl, 3 rg, 1 cat and 1 shasum. All ran with
cwd set to the snapshot, and none used an interpreter, network, solver or an outside path.

**DISPOSITION: ACCEPT-WITH-FIXES.** There is no FATAL and no MAJOR finding: "No new mathematical defect found. The
original control discrepancy is substantially repaired; its remaining provenance wording is MINOR." It has 2 MINOR
findings:
1. r3:94 "separately built" exceeds the receipt; Codex suggests "a separate parent checker with binary SHA-256
   a46c0c71…8e37". Desk adjudication: valid as a citation gap. The build record exists in the parent's
   parent-result.json (§4), so either the citation or the rewording fixes it.
2. r3:89: attribute the original verification outcomes to the saved producer summaries, with parent route 2
   recording `s VERIFIED` for all fourteen. Desk adjudication: valid wording precision. The underlying claim is also
   reproduced by the parent replay (§4).

Codex marks every other finding RESOLVED, with Codex v1 MAJOR 1 as PARTIAL (minor residue only). It also confirms:
- the corollaries, including the forward direction of Lemma 2.2;
- the dependency split;
- the scope;
- that the corollaries exclude every non-classical 2-RQLS(7) and PQLS(7), not just cardinality 49;
- that classical PQLS(7) exist, e.g. |y−2x>.

## 9. Correctness, novelty, significance (kept separate)
- **Correctness.** The K1 delta introduces no new defect and resolves both MAJOR findings. The corollaries follow
  from K1 and are correctly stated as conditional on K1's status. Finite-enumeration and SAT results stay certificate
  evidence; the parent technical checks are cited, not re-proved.
- **Novelty.** Not assessed by this desk. The prior-art acknowledgements were verified against the sources. The
  parent's bounded screen `REVIEW/moqls7-k1-priority-scout-v1.md` (NONE-FOUND-IN-SCOPE; covers DataCite, Zenodo,
  arXiv and OpenAlex) is cited, not relied on. The parent spot note `moqls7-k1-corollary-parent-spot-v1.md`
  (d6fe7a4b…b622) agrees with §7 and was not relied on.
- **Significance.** Conditional on K1, the corollaries settle the order-7 cases left open in HL v1 §5 (MCPQLS(7)) and
  ZC v2 §5 (maximal-cardinality 2-RQLS(7)). They do not determine M(7).

## 10. Recommended non-blocking fixes for an r4 or overlay
1. r3:94: cite `moqls7-parent-proofcheck-v1/parent-result.json` (200d307d…3bfe) for the build, or reword as Codex
   suggests.
2. r3:89: attribute the original statuses to the saved summaries, and the raw `s VERIFIED` for all 14 to the parent.
3. r3:74–75: add the RESULT.json sha256.
4. Optional:
   - mark r3:77–78 and r3:158–159 as "unverified history";
   - add an overlay note for k1_sat.py:15;
   - in the corollary, state that the harmonic route needs only K1's class-5 clause.

## 11. Deviations and resource use
- **Extra GETs.** Beyond the authorized Zhang–Cao GET, the desk made read-only HTTPS GETs of HL 2606.27758v1 and
  Ball–Simoens 2603.02334v1, which the corollary cites. There were 10 GETs to arxiv.org in total:
  - reader tool: the ZC abstract page and the ZC, HL and BS PDFs;
  - an in-memory prototype: 3 PDFs;
  - frozen `source_fetch.py`: 3 PDFs.

  No PDF or text copy was written. pdftotext 26.04.0 read stdin, with TMPDIR set to `moqls7-k1-delta-v1/tmp`, which
  stayed empty.
- **Extra snapshot material.** Text-only copies were added beyond the minimal list: 5 lane code files, the two pinned
  source layouts and the route 1/3/4/5 receipts. No CNF, proof or PDF copies were made; control inputs are described
  in controls-binding.md.
- **Withheld from Codex.** The desk bridge result and the parent spot note were deliberately excluded to keep the
  reviewer independent.
- **SOURCES.md.** It calls the Lemma 2.2 quote verbatim, but its ellipses are normalised; the receipt anchor is the
  exact extraction (recorded in the manifest notes). Desk-written files are write-once, so this was not edited.
- **No Claude review.** None was run; the assignment specified one Codex review.
- **Resources.**
  - Desk computations used ≤1 CPU: the bridge check took 0.064 s wall, the fetch 0.96 s.
  - Codex took 440 s.
  - New desk data is about 0.45 MB plus about 0.45 MB of Codex logs.
  - Free space on disk was about 13 GB at the start.

## 12. Files written (all new, exclusive)
- `REVIEW/moqls7-k1-delta-v1/` contains:
  - `snapshot/` (38 files plus `manifest.json`)
  - `finding-map.md`
  - `bridge_check.py`, `bridge_check.result.json`, `bridge_check.run.json`
  - `source_fetch.py`, `source_fetch.receipt.json`
  - `tmp/` (empty)
  - `delta-check.md`
- `REVIEW/moqls7-k1-delta-codex-v1.prompt.txt`
- Written by the runner: `REVIEW/moqls7-k1-delta-codex-v1.{note.md,stdout.txt,stderr.txt,receipt.json}`
