# Frozen scope: KP4 residual at p=7 (terminal k=8, kappa^=3, H^=3, length 26), all non-constant rotation multisets, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T16:40:24-0700, BEFORE any derivation or case checking for this target.
Authority: Main's IRC and RUN/control/written-slot-transitions-olson-moqls8-20261019-1634-v1.json, whole-file SHA256
0c852bf12ebc5daa6e176ae465a038cb5e82f5f24d8355e925b09ada6276b0de (recorded 2026-10-19T16:37:41-0700), slot math2,
RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h. Existing ordered-Olson problem; not an extra target,
not runtime authority (global HOLD unchanged). Writes ONLY this new directory, exclusive create x, then chmod a-w;
corrections are new numbered versions or errata. Every older packet (KP4, KP3, UH, PP1, KP2, ...) stays untouched.
Governance: written mathematics only; hash/byte/line-range metadata only. NO in-memory assertions, scripts, enumeration,
probes, CLI, nested agents, tests, native or scientific computation, not even short bookkeeping over scientific data. All
case work is by hand in the written files, with every branch closed explicitly.

## Exact target
R7: let p=7. There is no avoider w of length 26 over D_14 (no 14 letters in increasing original index order with identity
product) having SOME admissible normal form u (accepted PM*/fusion process, existential reading of ZX overlay 2) with
terminal k=8 and kappa^=3 (so H^=3 distributed ARBITRARILY among the 8 odd blocks, F=14, R=12; every empty NF run separates
blocks of different values) whose twelve rotation letters are NOT all equal. No hypothesis on o_F, reflection runs, nonempty
runs or rotation pairs. Together with the pure case this would give the whole p=7 cell; the pure case itself (Proposition
KP4-7P of the pending KP4 packet) is NOT a premise and is re-proved here if used.

## Inputs (accepted scopes only)
NF (proof-ROT-few-E-v4.md 28-43; empty-run rule at 38; fewodd addendum 1 line 12, ZX overlays 1-3, lowodd item 2, M1, M4);
GRX if direction (notes-GRX-v1.md 7-20; lowodd item 1, M2; every cyclic constant-block representation and pattern, empty runs
allowed); RS(b) (proof-ROW-v1.md 16-27 with erratum-2 R5; CFXT item 4) with classical Cauchy-Davenport; CT (STAB-delta item 6)
if needed. Accepted UH-A (RUN/review/olson-UH-CONSTRAINTS-parent-verdict-v1.md, SHA256
7c7b90f2745ba0cb7a8300c3f914a72c4b457259e4fcd45385266db15e4a71e3, mandatory errata v1 8f1ea491..., v2 ac2a7f26..., v3
0dc67886...) MAY be used at its literal scope (prime p>=7, (p-1)/2<=kappa<=p-3, some admissible NF with terminal k=p+1, any
H-distribution, empty-run rule; conclusion 2kappa+3<=A<=2p-1, A'<=kappa, b<=p-4, oriented A>=A' in the common nonzero class);
any use is recorded as an input change. NOT premises: the pending KP4 packet (proof-KP4-v1.md a6308ea8..., erratum
cb2802c6..., obstruction cdac29f4...), KP3-EXCL, UH-MW/SH/L/PH/E beyond literal accepted scopes, PP1/KP2 endpoints,
ASSEMBLY-P, RPdelta, REFL, RUNS/RGR-LONG, S(p), Lev, (S1), LS-family. Every reused KP4/KP3 step is re-proved here.

## Pre-freeze disclosure (prior knowledge and sketches; NONE is a premise or verified for this target)
From my own pending KP4 work (written there, not reviewed): the p=7 selection lists (m=0: n in {8,10,12}; m=1: {6,..,12};
m=2: {4,..,10}; m=3: {2,..,8}; m=4: {0,..,6}); pairing gives a dominant class {a,-a} with multiplicity >=7; the exact
attained interval [max(-nu,nu-alpha), min(nu,12-alpha-nu)] for all-equal letters; its pair-case analogue with
epsilon=A'+d(P); forbidden values (arcs epsilon!=6; m=2,3 sets epsilon not in {4,6,8}); empty-run bounds E<=2 (A'=1,3),
E<=1 (A'=2), E<=2 in the pure case; the pure-case profile enumeration; Lemma B1 (all-plus: 3 in M, 2 not a sum over >=b-2
weights, total weight !=1; b=1 forces the special letter to be -a, 2a or 4a).
Unwritten mental sketches during the KP4 slot (disclosed now): (i) for the pair case with A'=1 the forbidden weight sums
become arcs w!=5 and m=2,3 sets w not in {3,5,7} with total weight 10 and one weight possibly -1; (ii) a selection that uses
a subset J of the non-a letters gives normalized sums omega_J+[max(|J|-nu,nu-alpha), min(nu,A-alpha+|J|-nu)].
Planned route (unverified): re-derive the general p=7 tools; use accepted UH-A to reduce to A in {9,10,11} (b in {1,2,3});
handle b=1, 2, 3 by explicit attained-set calculations for every sign/side configuration of the non-a letters, plus run
profile enumerations; or stop with an exact residual.

## Allowed outcomes
(O1) a complete written exclusion of every non-pure case; (O2) a genuine written avoider word at p=7 with written GRX avoidance
verification (all patterns), never a count model; (O3) proved exclusion of explicitly named sub-cases plus the exact
remaining cases, the failing step and the smallest missing claim, with every failed branch and its arithmetic retained.

## Not claimed
Anything outside this exact p=7 cell; reflection rigidity, INV*, REFL, o_F assembly, ordered Olson for D_14 or other groups,
multiset-only non-existence outside the full NF antecedent, novelty, priority, "first", Lean or human review. Every new
claim is CANDIDATE_UNVERIFIED; the parent owns both-family reviews and verdicts.

## Deliverables
Proof and/or obstruction file with interface/import table, review package and {path,sha256,start,end} manifest (<=100 KB
embedded), checkpoints at most 1800 s apart (target 1200 s) including waits, IRC to Main with full paths/SHAs; then park.
