# KII-W-SCOPE-v1 — full KII written exclusion (verification replacement) [target only; no claim]

- **Written:** `/bin/date` read at 2026-10-19T17:03:00-0700, immediately before this exclusive create (directory created empty just before;
  an earlier write attempt failed before creating any file because the eval kernel had lost its helpers).
  Owner SunM13MixedFibres, slot math-1. First `/bin/date` of this slice: 2026-10-19T17:02:03-0700.
- **Authority:** `RUN/control/written-slot-transitions-sun-physics-20261019-1700-v1.json`, sha256
  b29119aa12222bf31cdaf6afdb59e81bc58ad2525fa9e08c5384bf86bc7d6bf2, key "math1".
  RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h.

## 1. Frozen target (exact quantifiers)
**Theorem target KII-W.** No group G with finite-index subgroups U_1..U_7 has pairwise disjoint left cosets g_jU_j whose
labelled index tuple lies in README class KII (O16/sun-coset7/README.md line 96, with the CE definition lines 33-35,
Lemmas P0/P1 lines 37-52 and Theorem R1(7)(II) line 58): all pairwise index gcds <= 6; a = |A_5| = 2 with A_5 = {x, y},
x in A_2 \ A_3, y in A_3 \ A_2; C = A_2 cap A_3 = V \ {x, y}, |C| = 5. Displayed gcd matrix: C-C 6; x-y 5; x-c 2, or 4
when x, c in E; y-c 3. Every exponent, every prime-to-30 cofactor, every 2-/3-/5-marker placement admitted by the class,
arbitrary groups (via R0). The exact raw index normalisation must be DERIVED from the class definition, not assumed.
This is a verification replacement for the KII branch of StageB, not a new class closure; KII only (not K5.2*).

## 2. Premise discipline
- Allowed: elementary subgroup/coset/index facts (Lagrange, product formula, coset-intersection criterion, finite-index
  cores); R0; Sun(2) (re-proved); Zhu Sun(3), Sun(4) (accepted classical import); the geometric fibre construction and
  actual inversion INV, each RE-PROVED in the new file at the literal scope needed.
- Sun(5)/Sun(6): only if unavoidable, then only through their accepted exact statements (Sun(5) verdict 2cf02436…5301,
  Sun(6) verdict efe1d849…1e29), with the load-bearing boundary labelled (they are computer-assisted).
- NOT premises: StageB certificates/outputs/code/engine/checker or its accepted KII conclusion; the K52-W candidate
  (`../k52-written/K52-W-v1.md`, c9c5ecbf…8e5d) — its methods may be re-proved here with attribution, never cited as a
  premise; any parent/worker sketch; minimal-counterexample frame; Sun(7); exponent caps; M-S Lemma 4.6; Menon; any
  pending candidate (K7-NF, A2X, SUN7-COMP).

## 3. Outcomes
(A) Complete written proof with exact import DAG and Sun-boundary table; or (B) the exact failing case (index data,
alpha pattern, the allowed sets that defeat every weight) and the exact remaining statement, never a fake closure.

## 4. Exposure before this freeze (disclosed)
Read earlier in this session, not premises: README lines 1-111 (incl. R1(7) step 2 for a = 2, gcd matrices line 67,
class table line 96); written verdict (73a25ba6…9f35) incl. line 20; StageB classes verdict (fd14952c…c13f), which
reports old KII counts (924 labelled tuples / 132 orbits, 1,584 leaves / 528 orbits, 0 survivors, each matched to an RPLP
line) — exposure to OUTPUT COUNTS only, no certificate, code or leaf content read; addendum line 155 (universe table row
'K52, KII, ...'); LFC/INV base, erratum and verdict; rules-k7-v1 lines 1-47. I authored K52-W (restricted fibre count
FC24 with Sun(2)/Sun(4), local gcd tables, uniform and corrected weights, actual-inversion finish) shortly before.
**Pre-freeze sketch:** none. No KII derivation, case check or weight was attempted before this file. Planned route
(not a result): exact factor normalisation; actual fibre counts at the 5-vertices and C-vertices with Sun(2)/(3)/(4)
admissibility; actual inversion; locate any case needing Sun(5)/(6) and label it.

## 5. Deliverables and governance
`KII-W-v1.md` (proof or exact obstruction, import/DAG table), `review-package-KIIW-v1.md`, `review-excerpts-KIIW-v1.json`
({path, sha256, start, end}, inclusive raw ranges), checkpoints <= 1800 s apart (target 1200 s), IRC with paths and
SHA256s, park. All files exclusive-create here; old files immutable. Written mathematics only: no scientific scripts,
assertions, enumeration, probes, solver, model CLI, tests, nested agents or source import; hash/byte/range metadata only.
New claims CANDIDATE_UNVERIFIED; no full Sun(7), acceptance, novelty, Lean or human-review claim.
