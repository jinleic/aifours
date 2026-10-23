# review-package-COMP-v1 — unit U0: Sun(7) proof-level composition (CONDITIONAL) [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T16:36:37-0700, immediately before this exclusive write. Owner SunM13MixedFibres. Written
  mathematics only; packaging used sha256, byte counts and raw line-range extraction. Parent owns reviews and verdicts.
- **Unit under review:** `C/SUN7-COMP-v1.md`, sha256 98796f95bf2faa7f0530ad9d4d999817fb5234d89ea09ea35eb232f2954913d7 (166 lines, 24,490 B), scope
  `C/SUN7-COMP-SCOPE-v1.md` a7f304f0456e9ff5011b300ce8d1e06d3ecd6e1dd398353e1a59162fa6ae0c38.
- Root aliases (exact absolute prefixes): C = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/sun7-composition`; K = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-complement-f`; A = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-a2-closure`; S = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7`; O16 = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016`; RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`; R16 = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`.

## 1. What is claimed
Theorem SUN7-COMP is CONDITIONAL: (H-NF) Theorem K7-NF and (H-A2X) Theorem A2X, together with accepted nodes at their
literal scopes (including computer-assisted Sun(5), Sun(6) and StageB), imply Sun(7) for every group. New in this unit:
Lemma CE-LIFT (restated R0), the exhaustiveness re-check of the accepted six-class reduction, Lemma K7-SPLIT, the
conditional theorem, the DAG, computation boundary and gate tables. (H-NF) and (H-A2X) are UNTRUSTED hypotheses here;
their complete proofs are reviewed in units U1 (K7-NF) and U2-U4 (A2 units 1-3), listed in `C/review-index-COMP-v1.json`.
No acceptance, Sun(7), novelty, Lean or human-review claim.

## 2. Verbatim theorem (raw lines SUN7-COMP-v1.md:87-89)
```text
**Theorem SUN7-COMP [CANDIDATE_UNVERIFIED; CONDITIONAL].** Assume (H-NF) and (H-A2X). Then, relative to the accepted nodes
of section 5 at their literal scopes (including the computer-assisted Sun(5), Sun(6) and StageB nodes), Sun(7) holds for
every group.
```

## 3. Reading order
1. Scope, transition, correction. 2. SUN7-COMP-v1.md sections 0-4. 3. For each class row of section 2, the literal
statement and verdict lines listed below. 4. Sections 5-8 (DAG, computation boundary, gates, obligations) against the
verdict lines. The NF/A2 lines here are statements only (hypotheses), never proofs.

## 4. Source table (manifest order; whole-file sha256; inclusive one-based raw line ranges)
| path | sha256 | lines | role |
|---|---|---|---|
| C/SUN7-COMP-v1.md | 98796f95bf2faa7f0530ad9d4d999817fb5234d89ea09ea35eb232f2954913d7 | 1-166 | NEW (whole): composition, Lemma K7-SPLIT, Theorem SUN7-COMP (conditional), DAG, boundary, gates |
| C/SUN7-COMP-SCOPE-v1.md | a7f304f0456e9ff5011b300ce8d1e06d3ecd6e1dd398353e1a59162fa6ae0c38 | 1-53 | frozen scope with pre-freeze disclosure |
| RUN/control/mathematics-slot-transition-sun-composition-20261019-1623-v1.json | 769525e0091bb9d864cd08e9acad1f7ac5f58a163801a3461ca43bb4eee3c3b5 | 1-18 | parent authority (composition target) |
| RUN/review/sun7-X1-stale-route-correction-v1.json | d272679d2e9e68e002fe409ee1c11cc0b3948a0a81918a3a53f744a4adf95ff0 | 1-20 | parent route correction (X1 duplicate withdrawn; StageA not load-bearing for K5.3) |
| RUN/control/six-slot-written-resumption-20261019-1603-v1.json | ac09b46532a233c6d9ce1b227c3dffecee9655bd83413d96d3a403065a0ef0f8 | 9-13 | definition of F (K7-NF target) |
| O16/sun-coset7/README.md | 2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1 | 9-29, 31-107 | ACC: Sun(7) text, imports, L0, R0, CE, P0, P1, R1(7), R1a-c, D2/D2', six-class table |
| R16/sun-coset7-written-parent-verdict-v1.md | 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35 | 5, 16-24, 44-47, 52-56, 58-60 | accepting verdict of the reduction/rules; overlay items; imports |
| O16/sun-coset7/rules-k7-addendum-v1.md | fb2c306b17a258181bb770c7c6c38585da77c0e312c68463cee7dc0f15fd1066 | 150-159 | ACC: X1 universe hypotheses and bridge X1 => K5.3 (line 159) |
| R16/sun-coset7-stageB-classes-parent-verdict-v1.md | fd14952c31852fe6c9b291114f99809f090a5f3bbb0caf07065ba50fffd3c13f | 1-16, 19-28, 40-48 | ACC: K5.2* (incl. D2') and KII excluded; computer-assisted, one checker; F-1 |
| RUN/review/x1-written-parent-verdict-v1.md | 84d7d8abef60fad092713fbf9530abba03ce0d269eb24a0494ac8d2729d40c4c | 1-14, 17-20, 26-29 | ACC: X1 written exclusion (K5.3), computation-free |
| RUN/review/sun7-K62-FULL-parent-verdict-v1.md | f3b22e536ea6f0e93647cde167a50101735baf4bf4d13ee71c4e704e3da21f0c | 1-11, 19-23, 41-43 | ACC: full K6.2* (K62X) with errata; imports |
| S/continuations/k62-full-closure/K62-FULL-v1.md | fabf04dd6abb1d3ec7e71b1cc3d459e008e9a96b5186b5a1f571fedac1312e5b | 16-26, 241-243 | K62X class definition and statement (literal) |
| RUN/review/sun7-K63DE-K735-parent-verdict-v1.md | 1a1c639093dd334cb404a8216ca70a839ea85454978c9fdf354cc5bc577a3919 | 5-13, 17-19 | ACC: K63-D, K63-E (and K7-35) with errata |
| S/K63-D-v1.md | f4027779f19a4733614f543d56a4cf596af9383f04510fbc725a5a7a3ebed255 | 13-24 | K63-D setting and statement |
| S/K63-E-v1.md | 73bcde10f4197ffc06c65107b5786ec9a03426c8ba86b7308343bfddac2d4de8 | 10-19 | K63-E setting and statement |
| S/continuations/k63-residue/K63-RES-v1.md | 1542a551f6d9787784a2434d18a5aa7275f673b23aab4901a384518206f67515 | 21-43 | K63-RES setting and statement |
| RUN/review/sun7-K63RES-parent-verdict-v1.md | 5ac595295727218cd86d0888720213972fe0520f64cea8d93a5c50ef18ed7bac | 1-10, 17-18 | ACC: K63-RES; all of K6.3 exhausted; Sun(6) load-bearing |
| RUN/review/sun7-K63-frontier-status-correction-v1.json | b41e47fc15cb903013cfb71e4340943d2a38939355d139170652423b676b5887 | 1-12 | parent correction: full K6.3 accepted |
| RUN/review/sun7-K7-R2-parent-verdict-v1.md | 9b0f7df54165575c2cee4818896738e886ae77ff2fcd6c1a328d5946cd1b926d | 1-17, 19-31, 46-50 | ACC: (a1) closure; reading order; prerequisites |
| K/K7-NF-v1.md | 734613fd21d9ea21aa940293c489f40549b74a3ac13d1ce3720db6bc98f73e97 | 84-86, 120-133 | UNTRUSTED hypothesis (H-NF): statement and K7-REM only; full proof in unit U1 |
| RUN/review/sun7-K7-NF-parent-erratum-v1.md | 21f31a50ae7a1fcb1746a7f9108892a108e6cdab9c381b880857561293d623f2 | 1-5 | parent wording erratum to K7-NF (line 143) |
| A/K7-A2-SCOPE-v1.md | 4a9502ac1116a4a0f06a92ffa8fc95e00a60595fe051085ffb5fa17f0a2ee320 | 13-23 | (a2) definition (A2 scope) |
| A/K7-A2-UNIT-3-v1.md | a2b40a9eecc1f8373cca60355217f9a5ac449105fc77886616f6cdad387d59be | 142-148 | UNTRUSTED hypothesis (H-A2X): Theorem A2X statement; full proofs in U2-U4 |
| R16/sun-coset5-parent-verdict-v1.md | 2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301 | 1-18 | ACC: Sun(5), computer-assisted |
| R16/sun-coset6-parent-gate-verdict-v1.md | efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29 | 1-19 | ACC: Sun(6), computer-assisted |
| RUN/review/sun7-stageA-K53-parent-verdict-v1.md | 0927a0d445b52f166e7cacdb2ddeb1eb57674b712227dcd0ba76537bf10c822b | 20-24 | two-checker full-result gate statement (line 24) |

## 5. Review contract
Independently check: (1) Lemma CE-LIFT against R0/CE; (2) the coverage table of section 1 against README P1, R1(7),
R1a-c, D2, D2' and the class table (exhaustiveness; every leaf a class or an accepted removal); (3) each row of section 2:
does the literal accepted statement cover the README class exactly, including every marker/exponent placement; (4) Lemma
K7-SPLIT against F (transition line 12), (a1) (R2 verdict line 9) and (a2) (A2 scope lines 14-17); (5) the proof of the
conditional theorem; (6) DAG accuracy (paths, hashes, overlays, acyclicity) and that no pending candidate other than
(H-NF), (H-A2X) is used; (7) the computation boundary and gate table (no promotion). Return FATAL/MAJOR/MINOR counts with
exact file:line and minimal repair; an empty findings list is valid. Do not treat (H-NF)/(H-A2X) as proved here.

## 6. Packaging metadata
43 inclusive ranges from 26 sources; selected raw UTF-8 bytes 85,249. Manifest
`C/review-excerpts-COMP-v1.json`, sha256 100611f66577bbec23daed4bbe1a96d85428cdea1f95da063eb16cee458f8010 (10,334 B). Every whole-file sha256 and range was re-checked
against the files immediately before this write. Package plus selected source: 93,836 B (<= 100,000).
