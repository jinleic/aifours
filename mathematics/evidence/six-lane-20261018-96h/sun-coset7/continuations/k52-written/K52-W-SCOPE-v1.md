# K52-W-SCOPE-v1 — full K5.2* written exclusion (verification replacement) [target, no claim]

- Written: `/bin/date` read at 2026-10-19T16:47:53-0700, immediately before this exclusive create. Owner SunM13MixedFibres.
- Authority: RUN/control/mathematics-slot-transition-sun-stageB-written-20261019-1639-v1.json,
  sha256 f189835cfd4e5e20cd4494e73b27851a07ba0576efc01551260ef5e38ad379cd; first slice clock 2026-10-19T16:43:21-0700.
  RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h.

## 1. Frozen target and quantifiers
No group with finite-index subgroups has seven pairwise disjoint left cosets in the full README class K5.2*:
V = {d_1,d_2,s} disjoint-union O, |O| = 4, C = {s} cup O, a <= 1, D = {d_1,d_2} subset (A_2 minus A_3) cap E,
C cap E = {s}. Pairwise gcds are 6 inside C, 4 for d_1-d_2 and d_j-s, and 2 for d_j-o, o in O. Thus
n_dj = 2^(e_j)5^(h_j)w_j (e_j >= 2), n_s = 2^(e_s)3^(f_s)5^(h_s)w_s (e_s >= 2,f_s >= 1),
n_o = 2*3^(f_o)5^(h_o)w_o (f_o >= 1). All exponents and prime-to-30 w factors are unbounded, all admissible 2/3/5 marker
placements included, arbitrary groups via R0. The class is exactly README line 94, not KII, the D2' case or a larger class.

## 2. Allowed premises and success/fallback
Use only elementary subgroup product/index/coset facts, the accepted written class/P0/P1 statements as exact hypotheses,
R0, literal LFC/INV/VFC statements, and Sun(2), Sun(3), Sun(4). Any restriction of the general fibre construction to
Sun(t) with t <= 4 must be proved here, with no Sun(5)/Sun(6) premise. Do not use the accepted K52 exclusion, StageB
certificate/output/checker/engine, a numerical LP answer, M-S Lemma 4.6, Menon, Sun(7) or a pending result as premise.
Success: complete written proof and exact import DAG with <=100 KB package and excerpt manifest, every new claim
CANDIDATE_UNVERIFIED until both model families and parent. Fallback: exact failing gcd/allowed-set obstruction with the
failed route, never fake closure. KII requires a separate scope and is not part of this task.

## 3. Parent sketch and pre-freeze exposure (not a premise)
The transition supplies an UNVERIFIED parent sketch: at apex d_1 put b=alpha_(d1 d2), a=alpha_(d1 s), O-labels 3r_o.
Try y_o=y_s=1/3, y_d2=2/3 for b=1,2, value 2/3+a/12+b/6. If b=1,a>=2, contradiction; if b=a=1, perhaps use y_d2=1,
value 1. Forbid b=1 in both families, then INV forces b=b*=2 and the first vector would contradict. This is NOT a lemma.
The preceding model's unwritten pre-freeze analysis additionally noticed the potential exceptional allowed 4-set when
a=3 and the unique higher-3 vertex lies in O (the s--that-vertex local gcd can be 9), and proposed checking an altered
weight there. It also inspected the d_2/s 2-parts for b=1,2, including the unique higher-2 vertex. These are unfinished
mental sketches, not proved claims, and will be re-derived after this freeze. No calculation/enumeration was run.
Read before freeze: transition; README P0/P1 and class table; LFC/INV statements (base lines 8-75) with E1-E3/E6-E7;
rules-k7-v1 lines 9-44; the LFC/INV verdict lines 18-23 and 33. No old checker or producer implementation/output read.
The accepted general LFC package has Sun(5)/Sun(6) provenance; the present restricted counting proof will not assume it.

## 4. Deliverables and governance
K52-W-v1.md (proof or exact obstruction, scope/import table, marker cases, provenance), review-package-K52W-v1.md,
review-excerpts-K52W-v1.json (path,sha256,start,end; raw ranges inclusive), checkpoints <=1800 s apart (target 1200 s),
and final paths/hashes to Main, then park. Every file new/exclusive-create here; old files immutable. No scientific
scripts/assertions/enumeration, solver, model CLI, nested agent, tests or source import. Only text authoring and
hash/byte/range metadata operations. No new class closure credit, full Sun(7), acceptance, novelty, Lean or human-review claim.
