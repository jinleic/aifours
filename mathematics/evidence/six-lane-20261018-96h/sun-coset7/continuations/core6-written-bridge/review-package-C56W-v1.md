# C56W written review package v1 — a direct written proof of Core5(6) [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T17:49:12-0700, immediately before this exclusive create. Owner SunM13MixedFibres. Packaging used
  only sha256, byte counts and raw line ranges; no scientific computation. The parent owns reviews and verdicts.
- **Candidate:** K/C56W-v1.md, sha256 63cbcdb1cc3b8620a9f16207a1a6a7ed99b898568c59af549c6a73592263f8b1 (141 lines, 13,255 B). **Scope:** K/C56W-SCOPE-v1.md, sha256 86badde3477ce7e824314388bc0fe5aaa2fbd2087191b783dc7ff1362da22b0e,
  frozen before the k6 definition was read; post-freeze reading is disclosed in the candidate header.
- K = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/core6-written-bridge; ROOT = /Users/jinleic/repos/aifours. Exact absolute paths and whole-file hashes are in the JSON manifest.

## 1. Claim and boundary
Theorem C56W proves Core5(6) (k6 README line 27) for every finite group: six disjoint cosets with indices 5 r_i, r_i pairwise
coprime, do not exist; every E2 (any 2-power), E3, E5 placement, r_i = 1 and all cofactors. Imports: Sun(2) (proved) and
Zhu's Sun(3), Sun(4) only — no Sun(5), no C5W, no Core(5), no k6 rule/certificate/count, no minimal frame. Verification
replacement, no novelty. CANDIDATE_UNVERIFIED; the Remarks' conditional Sun(6) route is explicitly NOT claimed.

## 2. Verbatim theorem and proof (candidate lines 109-122)
```text
**Theorem C56W [CANDIDATE_UNVERIFIED].** Core5(6) holds: no finite group has six pairwise disjoint left cosets with indices
5 r_i and r_i pairwise coprime; every placement of E2 (any 2-power), E3 and E5, r_i = 1 and all cofactors are included.
*Proof.* Let Gamma be such a configuration and Gamma* its inverse (Lemma INV).
- **Case 1: E2 and E3 are not two distinct vertices.** Let v = E2 if it exists, else v = E3 if it exists, else any vertex;
  every neighbour of v is plain. By Lemma P6 for Gamma, at least three alpha_vj equal 4; then those alpha*_vj equal 1, so the
  row of v in Gamma* has at least three multipliers 1, which none of the multisets of Lemma P6 has. Lemma P6 for Gamma*
  gives a contradiction.
- **Case 2: E2 = a and E3 = b with a != b.** By Lemma A6, Gamma is in (S-i), (S-ii) or (S-iii) at a, and so is Gamma*.
  If Gamma is in (S-i), at least three alpha_ap equal 3, so at least three alpha*_ap are <= 2; then M* has at most one entry
  >= 3, whereas (S-i) needs three 3s and (S-ii), (S-iii) need at least two 4s. If Gamma is in (S-ii) or (S-iii), at least two
  alpha_ap equal 4, so M* has at least two 1s, whereas every allowed multiset has at most one 1. Contradiction. QED

**Remarks.** (1) E5 and the 2-power class of E2 never enter: E2 is always the apex when it exists. (2) Conditional
observation, NOT claimed: the k6 README's R1(6) (lines 31-43) reduces Sun(6) to Core5(6) plus Core(5), Prop 4.5 and Zhu;
```

## 3. Proof map (candidate line numbers)
Target and imports 17-32; setting and MU 33-41; INV and FC 42-59; local groups G1/G3/GE and weights E(a)-E(d)
60-74; Lemma P6 75-85; Lemma A6 86-107; theorem 108-120; remarks 121-125; DAG and checks 126-141.
Mechanism: at an apex the neighbours carry labels r_j alpha and masses alpha/5; plain neighbours split into isolated 1s,
pairwise-gcd-3 threes (at most three per fibre by Sun(4)) and evens (2s and 4s). Five plain neighbours fail the count unless
at least three multipliers are 4; at E2 (when E2 != E3) only the multisets (S-i)-(S-iii) survive. Inversion maps 4 -> 1 and
3 -> <= 2, and no surviving multiset is closed under that map.

## 4. Review questions
1. Exact quotation of Core5(6) and the markers; nothing dropped or added.
2. FC: only 2-, 3-, 4-subsets of actual fibre sets are constrained (five-element fibres allowed); Sun(2) proof.
3. INV: same markers; alpha + alpha* <= 5.
4. Feasibility of the standard weights E(a)-E(d) and the G3 weights on ALL admissible sets, including five-element ones.
5. Lemma P6's case split; Lemma A6's compatibilities of b for beta = 1, 2, 3, 4, the 1/3 weights, and the two reductions
   to Lemma P6 (b acting as a plain 2 or 4).
6. The theorem's case split and the multiset comparisons under INV.
Return FATAL/MAJOR/MINOR per group with exact file:line and the smallest repair; an empty list is valid.

## 5. Excerpt sources (inclusive raw physical lines; whole-file sha256)
| source | sha256 | lines | role |
|---|---|---|---|
| K/C56W-v1.md | 63cbcdb1cc3b8620a9f16207a1a6a7ed99b898568c59af549c6a73592263f8b1 | 1-141 | NEW whole proof: MU, INV, FC (Sun2 proved; Zhu Sun3, Sun4), local groups and weights, Lemmas P6 and A6, Theorem C56W |
| K/C56W-SCOPE-v1.md | 86badde3477ce7e824314388bc0fe5aaa2fbd2087191b783dc7ff1362da22b0e | 1-47 | frozen scope (before the definition was read); exposure; no sketch |
| ROOT/institute/runs/six-lane-2026-10-18-96h/control/written-slot-transitions-core6-corner-sigma-v1.json | 7ff16d5b5b312bb3ca65206cb84f73331ccf3cd7b71cc7f0753687f1e2da26ec | 1-29 | parent authority (key math1) |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset6/README.md | 10fc493e5bf79f98fb805dc9e4b48becbf51fc7d7648848fa8874542dda5e2bf | 20-60 | Core5(6) statement (line 27), R1(6) context, marker definitions (54-57); everything read post-freeze |
| ROOT/institute/runs/six-lane-2026-10-16/review/sun-coset6-parent-gate-verdict-v1.md | efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29 | 1-19 | accepted computer-assisted Sun(6) scope (context only; nothing imported) |
| ROOT/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-v1.md | 45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c | 18-71 | origin of the fibre count and inversion; re-proved in the new file with Sun2-Sun4 only |
| ROOT/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-erratum-v1.md | 7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5 | 10-32, 47-63 | mandatory elementary overlays E1-E3, E6-E7 |
| ROOT/institute/runs/six-lane-2026-10-18-96h/review/sun7-lfc-inv-parent-verdict-v1.md | 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18 | 16-19 | accepted LFC/INV statements; its Sun(5)/Sun(6) provenance is NOT imported |

## 6. Packaging metadata
Manifest K/review-excerpts-C56W-v1.json, sha256 c6a130b6888cc3b242417f6d4b948926516afcafd8e4ac72eeaa6b8b5939ee45 (2,157 B): 9 ranges from 8 sources as
{path, sha256, start, end}. Selected raw bytes 34,693; package plus selected source 41,293 B (<= 100,000). The full new
proof is included; no new node is replaced by a context-only declaration.
