# Frozen scope: R-UH round 3 -- close residual R2 (then R1), v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T17:30:02-0700, BEFORE any derivation for this target.
Authority: Main's IRC and RUN/control/written-slot-transition-olson-20261019-1730-v1.json, whole-file SHA256
b95a3c222c5d95faf838ce9db98e6e94050196bc6b6f6366339922f311755455 (recorded 2026-10-19T17:29:18-0700), key math2,
RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h. Existing ordered-Olson problem (math2 slot); not an
extra target or runtime authority (global HOLD unchanged). Writes ONLY this new directory, exclusive create x, then chmod a-w;
corrections are new versions or errata. Older packets (RUH2, KP3, KP4, R7, UH, ...) stay untouched. Written mathematics only;
hash/byte/range metadata only; NO scripts, assertions, enumeration, probes, CLI, nested agents, tests or computation over
scientific data.

## Exact target
R2 of residual-RUH2-v1.md (SHA256 267bd0354543568a1dbb7b3aa56327afedb415335b96f204c92b3aa3b435059b, with its erratum): for every
prime p>=13 and every e with 6<=e<=(p+2)/3 (kappa=p-e), under the FULL antecedent (an avoider w of length 4p-2 over D_(2p) has
SOME admissible NF with terminal k=p+1 and kappa^=kappa; H^=e-1 extra reflection pairs anywhere in the odd blocks; every empty
run separates different reflection values; no o_F, nonempty-run, reflection-rigidity or rotation-pair hypothesis), exclude every
case with A=2kappa+c, e<=c<=2e-1 (A the larger multiplicity of the common nonzero dominant class). If R2 closes, attack R1 of
the same note (prime p>=11, 3e>p+2, 5<=e<=(p+1)/2, 3<=c<=2e-1) in this slot. Deliverable: a full written proof, OR the exact
smaller residual in (p,e,c,run-profile) form with every failed branch retained. A single-cell result is reported only as a
clearly labelled partial with its exact parameter range; nothing is silently substituted.

## Inputs (accepted scopes only)
NF (proof-ROT-few-E-v4.md 28-43; empty-run rule 38; fewodd addendum 1 line 12, ZX overlays 1-3, lowodd item 2, M1, M4); GRX if
direction (notes-GRX-v1.md 7-20; lowodd item 1, M2); RS(b) (proof-ROW-v1.md 16-27 with erratum-2 R5) and classical
Cauchy-Davenport; accepted UH-A/L/E at literal scope (UH verdict 7c7b90f2745ba0cb7a8300c3f914a72c4b457259e4fcd45385266db15e4a71e3
with errata v1-v3); PP1/KP2 verdicts only at their own cells. NOT premises: RUH2 (proof f391b08f..., erratum a3c67313...,
residual 267bd035...), KP3, KP4, R7 -- CANDIDATES; every step used from them is re-proved inline [RE-DERIVED]. Not used: UH-SH,
UH-MW, UH-PH as imports (re-derived if needed), ASSEMBLY-P, RPdelta, REFL, RUNS/RGR-LONG, S(p), Lev, (S1), LS-family, CT.

## Pre-freeze exposure (prior knowledge and unwritten sketches; NONE is a premise or verified for this target)
From my candidate RUH2 packet: the SH re-derivation (m=e omission window, toggle path, super-heavy run h, light sets, counts
E+|Q|>=c+1, |Q|<=c-1, E>=2); Lemma L (sets P avoiding h, 1<=m(P)<=e: d(P)<=c-min(e,2m-1)); Theorem A (c<=e-1); the e=5 lists
for c=5..9 (missing set M, free/(N1) lengths, position endgames). Unwritten sketches formed during RUH2 (disclosed now, unverified):
(i) for c<=2e-2 every forced interval meets the all-plus block B0=[e-mu,e-1] (plus e-mu-1 for odd c<=2e-3), so the forced part
of M is one integer interval U with |U|<=c; writing U+ and U- for its excess beyond B0 on each side gives U+ + U- <= mu (as a
first estimate), the empty-run values bounded accordingly, and 0 not in M gives a further bound; (ii) for c=2e-1 a
two-piece argument excludes t>=e, then s(Y)+m(Y)<=e for every set Y of empty runs, E<=e-1, with E=e-1 forcing e-1 consecutive
empty runs of value 1; (iii) a "slack" view of the endgame: splitting a block of pure-a runs or adding an isolated empty run
raises m by one and lowers the Lemma L bound by two; (iv) Cauchy-Davenport counting on sums of at most e-mu empty-run values,
which alone gives only E<=ceil(c/2) (insufficient, route F3 of the residual note).
Planned route: re-derive the SH structure and Lemma L; derive a uniform missing-set/empty-run lemma for e<=c<=2e-1 with exact
free and (N1) lengths and the 0-exclusion; derive a uniform position lemma; then R1 if R2 closes; else record the exact smaller
residual.

## Not claimed
UH-EXCL itself, other cells, reflection rigidity, INV*, REFL, o_F assembly, ordered Olson, the lower half, multiset-only
statements outside the full NF antecedent, novelty, priority, "first", Lean or human review. Every new claim is
CANDIDATE_UNVERIFIED; the parent owns both-family reviews and verdicts.

## Deliverables
Proof or residual note with interface/import table, review package and {path,sha256,start,end} manifest (<=100 KB embedded),
checkpoints at most 1800 s apart (target 1200 s) including waits, IRC to Main with full paths/SHAs; then park.
