# S56W review package v1 — written Sun(5)/Sun(6) composition, CONDITIONAL on H5/H6 [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T17:57:13-0700, immediately before this exclusive create. Owner SunM13MixedFibres. Packaging used
  only sha256, byte counts and raw line ranges; no scientific computation. The parent owns reviews and verdicts.
- **Candidate:** K/S56W-v1.md, sha256 9dfa360e6b54d6075e79f240bf2375e9049a66ae02fc14f375946e0bed61b894 (193 lines, 20,320 B). **Scope:** K/S56W-SCOPE-v1.md, sha256 50e681cf025b137c07e20f455b720f30ef275b39090fbe5f64d839b32f4ce507.
- K = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/sun56-written-composition; ROOT = /Users/jinleic/repos/aifours. Exact absolute paths and whole-file hashes are in the JSON manifest.

## 1. Claim and boundary
CONDITIONAL theorems with statements verbatim equal to the accepted ones: **S5W** (Sun(5), every group) from H5; **S6W**
(Sun(6), every group) from H5 and H6. H5 = Core(5) via the UNREVIEWED C5W; H6 = Core5(6) via the UNREVIEWED C56W. Everything
else (R0, L0.1-L0.6, L1-L3, K2, Prop 4.5, R1, R1(6)) is reproduced in full written form; Zhu k = 3, 4 is the only external
import. No accepted Sun(5)/Sun(6) theorem, engine, checker, certificate, count or minimal-order frame is a premise; no proof in
the DAG uses Sun(5) or Sun(6). Old computer-assisted records are NOT re-labelled. No acceptance, novelty, Lean or human claim.

## 2. Verbatim theorem lines (candidate lines 116-120 and 138-143)
```text
**Theorem S5W (CONDITIONAL on H5).** (Statement as in section 1.) *Proof.* Suppose five pairwise disjoint left cosets of
finite-index subgroups of a group G have all pairwise index gcds <= 4. By R0 (section 6) pass to a finite quotient with the
same indices and disjointness. Lemma R1 yields one of four configurations in that finite group: the first contradicts Zhu
Theorem 1.1 at k = 4, the second Zhu at k = 3, the third Proposition 4.5, the fourth H5. QED (Equal subgroups and every
cofactor are allowed throughout; no minimal-order frame is used.)
...
**Theorem S6W (CONDITIONAL on H5 and H6).** (Statement as in section 1.) *Proof.* Given six pairwise disjoint cosets with all
pairwise gcds <= 5, pass by R0 to a finite quotient; Lemma R1(6) gives one of five configurations there, contradicting Zhu
k = 4, Zhu k = 3, Proposition 4.5, H5 or H6 respectively. QED (Equivalent route for p = 2 and p = 3, per C1's remark: any
five of the cosets have all gcds <= 4, contradicting S5W; it uses the same inputs.) No minimal-order frame is used.

## 6. R0 (complete)
```

## 3. Proof map (candidate line numbers)
Statements and hypotheses 16-33; elementary lemmas and erratum dispositions 34-66; Prop 4.5 67-104;
R1 and S5W 105-121; R1(6) and S6W 122-142; R0 143-148; DAG and audit 149-168; substitution protocol 169-187;
non-claims and checks 188-193.

## 4. Review questions
1. Verbatim equality of S5W/S6W with the accepted statements, and of H5/H6 with proof-v4 line 49 / k6 README line 27 and the
   C5W/C56W theorems; equal-subgroup and all-group scope preserved.
2. L0.1-L0.6, L1, L2, L3, K2 proofs; every L3 application's pair condition and inversion in Prop 4.5 (erratum E9).
3. Prop 4.5 steps (a)-(g): divisibilities, (T2)/(T3) sizes (including the apex-2 bound in (d), (e)), double-coset granularity.
4. R1 and R1(6) exhaustiveness (odd/even split; e = 1 counting; binomial argument; C1).
5. DAG/audit: no old computational theorem, no minimal frame, no circularity (H5, H6 use only Sun(2)-Sun(4)).
6. Substitution protocol: correct, not overstated, history unchanged.
Return FATAL/MAJOR/MINOR per group with exact file:line and the smallest repair; an empty list is valid.

## 5. Excerpt sources (inclusive raw physical lines; whole-file sha256)
| source | sha256 | lines | role |
|---|---|---|---|
| K/S56W-v1.md | 9dfa360e6b54d6075e79f240bf2375e9049a66ae02fc14f375946e0bed61b894 | 1-193 | NEW whole composition (statements, L0-L3/K2/R0, Prop 4.5, R1+S5W, R1(6)+S6W, audit/DAG, substitution protocol) |
| K/S56W-SCOPE-v1.md | 50e681cf025b137c07e20f455b720f30ef275b39090fbe5f64d839b32f4ce507 | 1-43 | frozen scope and exposure |
| ROOT/institute/runs/six-lane-2026-10-18-96h/control/written-sun56-import-cutover-and-E2-closure-v1.json | e1317e565a1c6218dbd594ec6530f76080a41d9fefab559e8639b60578990193 | 1-29 | parent authority (key math1) with H5/H6 pins |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset5/proof-v4.md | 3d17efcc034cca643515e581fa4667515086d0844a58b951e2641080d6c94516 | 37-103 | Sun(5) theorem, R0, R1, Prop 4.5 (text of record), F-3 |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset5/rules-v1.md | cb86c16836d929a21256c34f0a87a5fc71788b970a6e1052751a69d637d1390f | 16-141 | rules-v1 setting, L0.1-L0.8, L1 (T), L2, L3 (K), K2 |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset5/rules-v1-erratum-v3.md | 1b3e126e1c398a71401b4c7e13cbc19c276befe095bb1c0043450c3cd425e8ed | 1-18 | cumulative rules erratum v3 (E6, E9 applied; others dispositioned) |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset6/README.md | 10fc493e5bf79f98fb805dc9e4b48becbf51fc7d7648848fa8874542dda5e2bf | 21-50 | k6 R0, R1(6), minimal frame (not used) |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset6/rules-k6-erratum-v3.md | 71cfeccbfb708c11bbdcc6f0a36f060395752a3ebfbb7c097edde270d967cc77 | 20-36, 80-82 | k6 erratum C1-C13 (C1 mandatory for R1(6); C12 citation) and C18 (minimal-frame closure, not used) |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset6/proof-k6-v3.md | 2aa4fa430dfb414dc5c726064f43e4cd1c023a58862fd8bd7b805e46c6880324 | 7-14, 29-34 | proof-k6-v3 component status and composition (minimal frame; not used) |
| ROOT/institute/runs/six-lane-2026-10-16/review/sun-coset5-parent-verdict-v1.md | 2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301 | 5-8 | accepted Sun(5) statement (verbatim for S5W) |
| ROOT/institute/runs/six-lane-2026-10-16/review/sun-coset6-parent-gate-verdict-v1.md | efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29 | 5-9 | accepted Sun(6) statement (verbatim for S6W) |
| ROOT/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/core5-written-bridge/C5W-v1.md | 2e4b42b2ce88cad9f13b56b027fb10ea1082fb3d20df8acbbdff5667d4db5c69 | 110-120 | H5 = Theorem C5W statement and proof (UNREVIEWED) |
| ROOT/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/core6-written-bridge/C56W-v1.md | 63cbcdb1cc3b8620a9f16207a1a6a7ed99b898568c59af549c6a73592263f8b1 | 109-119 | H6 = Theorem C56W statement and proof (UNREVIEWED) |
| ROOT/institute/runs/six-lane-2026-10-18-96h/control/sun7-full-result-computation-gate-ruling-v1.json | 4818f1ca96c99e012d758e165982ec0844228eae07ff3f38b95dc2b7a3a5eada | 1-20 | full-result computation gate ruling (substitution protocol item 2) |

## 6. Packaging metadata
Manifest K/review-excerpts-S56W-v1.json, sha256 f8a4e939db54055832816ca44c1c540adedc4d1820d97b9321026d5673521316 (3,792 B): 16 ranges from 14 sources as
{path, sha256, start, end}. Selected raw bytes 57,676; package plus selected source 64,971 B (<= 100,000). The full new
composition is included; H5/H6 are included as statements with their proof blocks (their full files are separate review units).
