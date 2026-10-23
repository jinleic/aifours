# Frozen scope: EXCLUSION of terminal k = p+1, kappa^ = p-2 (one length-3 block, p singleton blocks), v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T12:52:47-0700, BEFORE any written or worked derivation for this target.
Authority: Main's IRC of 2026-10-19 12:52:04 and the slot transition /Users/jinleic/repos/aifours/institute/runs/
six-lane-2026-10-18-96h/control/mathematics-slot-transition-olson-20261019-1252-v1.json (sha256
aee5c6147cdce23ac4f886625862122a1832e16ca05b42382b799c6c6f41933c), slot math2 (existing ordered-Olson problem; not an extra
target, not runtime authority). Status of everything below: target statement only, NOT a proof or verdict. Written mathematics
only: no computation, enumeration, script, solver, test, build, Lean or model CLI; hash/byte/line-range metadata only. Writes only
in this directory, exclusive create, versioned names. Every PP1-EXCL file (terminal-pplus1-exclusion/) and every older packet
stays untouched.

## Pre-freeze disclosure
Between Main's IRC (received after 12:49:09) and this freeze I read only the transition record and Main's message. Nothing was
written and no case was worked. The only plan formed is the generic one suggested by the previous slot: (s1) recompute the GRX
selection rule (delta, C_max and the admissible C) per pattern for one block of length 3, which can contribute 1 or 3
reflections; (s2) a rotation-multiset classification from the all-plus pattern and CT at |X| = 3p-5 (kappa = p-2); (s3)
single-run / arc omission counts (Cauchy-Davenport via RS(b)) and +-c windows, plus empty-run constraints. None of this is
verified; it is a plan, not a result.

## Exact target (word level)
Theorem KP2-EXCL. Let p >= 7 be prime. There is NO avoider w of length 4p-2 over D_(2p) (no 2p letters in increasing original
index order with identity product) such that SOME admissible normal form w^ of w (accepted PM*/fusion process, existential
reading of ZX overlay 2) has terminal k = p+1 and kappa^ = p-2; equivalently H^ = 1: exactly one terminal block has length 3,
the other p blocks are single reflections, F = p+3, R = 3p-5. No hypothesis on o_F(w), on reflection runs, or on nonempty runs.
The length-3 block changes delta and C_max for every pattern; (SEL) is recomputed per pattern and never copied from k = p+1,
kappa^ = p-1.

## Allowed outcomes
(O1) A written proof. (O2) A genuine written avoider at a named p: an actual word (letters and order) with avoidance verified in
writing through GRX, not a count model or a rotation sequence. (O3) A precisely proved obstruction: the exact new necessary
constraint(s), the exact failing step, the smallest missing claim, with every failed route and its arithmetic preserved. A
failure is never relabelled as a solution; no partial statement is silently substituted.

## Inputs (accepted scopes only)
NF (proof-ROT-few-E-v4.md Sec. 0 with fewodd addendum line 12, ZX overlays 1-3, lowodd item 2, M1, M4), including the rule that
every empty run separates blocks of different values; GRX ("if" direction) for every cyclic constant-block representation and
every sign pattern (lowodd verdict item 1, M2); Lemma CT (STAB-delta verdict item 6: p >= 5 prime, 0 <= kappa <= p-1); Lemma
RS(b) (CFXT verdict item 4) resting on the classical Cauchy-Davenport theorem. Each cited by path, whole-file sha256 and range.
NOT premises (context only): pending ROT-PP1 / ROT-PP1-TOP (Codex ACCEPT-WITH-FIXES 7fda7f0b, parent errata v1 and v2
49c3e491, Claude pending), my pending PP1-EXCL (6fea2fd2; review frozen a20e5309), ROT-SING+, ROT-SING, ONE-SHORT-LS,
ASSEMBLY-P, (S1), Lev, S(p), REFL at any o_F, LS+2 (unless re-checked as an accepted sequence statement at its exact scope and
cited as such). Anything reused from a pending text is re-proved here and labelled [RE-DERIVED], or stated as an explicit
conditional.

## Not claimed
Reflection rigidity, INV*, any statement for other (k, kappa^) or for o_F, any assembly or word-class promotion, ordered Olson for
D_(2p) or for all groups, p = 5, existence or non-existence of avoiders outside this exact cell, novelty, priority, "first", Lean
or human review. Every new claim is CANDIDATE_UNVERIFIED; the parent owns model reviews and verdicts.

## Deliverables
Proof file or obstruction note (with interface/scope/import table), review package, excerpt manifest {path, sha256, start,
end} (<= 100 KB embedded), checkpoints (<= 1800 s apart, target 1200 s), IRC report to Main with paths and SHAs; then park.
