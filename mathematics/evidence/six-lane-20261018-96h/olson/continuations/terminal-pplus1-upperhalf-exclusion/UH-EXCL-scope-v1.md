# Frozen scope: EXCLUSION of terminal k = p+1 for (p-1)/2 <= kappa^ <= p-3 (upper half), v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T13:08:38-0700, BEFORE any written or worked derivation for this target.
Authority: Main's IRC (received after 13:04:59) and the slot transition /Users/jinleic/repos/aifours/institute/runs/
six-lane-2026-10-18-96h/control/mathematics-slot-transition-olson-20261019-1308-v1.json (sha256
c99edba4f6324ee07fd29eec26c7abfd8409921f966472a2b69ad7a6db7f99c7), slot math2 (existing ordered-Olson problem; not an extra
target, not runtime authority). Status of everything below: target statement only, NOT a proof or verdict. Written mathematics
only: no computation, enumeration, script, solver, test, build, Lean or model CLI; hash/byte/line-range metadata only. Writes only
in this directory, exclusive create, versioned names. PP1-EXCL, KP2-EXCL and every older packet stay untouched.

## Pre-freeze disclosure
Between Main's IRC and this freeze I read only the transition record. Nothing was written and no case was worked for this range.
Known from my own earlier (pending) KP2-EXCL work and stated here as a PLAN only: (s1) recompute the GRX selection rule with
C in [Phi, Phi + 2H^] (all blocks odd); (s2) re-derive pairing (Lemma M/P) and the dominant pair (Lemma U) in the range
kappa^ >= (p-1)/2, tracking the exact admissible lengths; (s3) re-derive the window, the heavy-run first passage, the light-set
bound and the empty-run analysis with EXPLICIT inequalities in e := p - kappa^, since Main notes that they need not survive the
smaller gaps. None of this is verified for e >= 3.

## Exact target (word level)
Theorem UH-EXCL. Let p >= 7 be prime and (p-1)/2 <= kappa^ <= p-3. There is NO avoider w of length 4p-2 over D_(2p) (no 2p letters
in increasing original index order with identity product) such that SOME admissible normal form w^ of w (accepted PM*/fusion
process, existential reading of ZX overlay 2) has terminal k = p+1 and this kappa^. Here H^ = p-1-kappa^ >= 2 is distributed
arbitrarily among the p+1 odd blocks, F = p+1+2H^, R = p-1+2kappa^. No hypothesis on o_F(w), on reflection runs, on the block-length
distribution, or on nonempty runs.

## Allowed outcomes
(O1) A written proof for the whole interval. (O2) A genuine written avoider at a named p and kappa^: an actual word (letters and
order) with avoidance verified in writing through GRX; never a count or block model treated as a group word. (O3) A precisely
proved partial result plus obstruction: the exact sub-range (in p, kappa^ or e) that is excluded, the exact new necessary
constraints proved for the rest, the exact failing inequality and the smallest missing claim, with every failed route and its
arithmetic preserved. The restriction is named explicitly; no partial statement is silently substituted for the target. The lower
range 1 <= kappa^ < (p-1)/2 stays OPEN and is not addressed.

## Inputs (accepted scopes only)
NF (proof-ROT-few-E-v4.md Sec. 0 with fewodd addendum line 12, ZX overlays 1-3, lowodd item 2, M1, M4), including the rule that
every empty run separates blocks of different values; GRX ("if" direction) for every cyclic constant-block representation and
every sign pattern (lowodd verdict item 1, M2); Lemma CT (STAB-delta verdict item 6: p >= 5 prime, 0 <= kappa <= p-1); Lemma
RS(b) (CFXT verdict item 4) resting on the classical Cauchy-Davenport theorem. Each cited by path, whole-file sha256 and range.
NOT premises (context only): pending KP2-EXCL, PP1-EXCL, ROT-PP1 / ROT-PP1-TOP and its obstruction note, ROT-SING+, ROT-SING,
ONE-SHORT-LS, ASSEMBLY-P, RPdelta (not needed unless explicitly re-scoped), (S1), Lev, S(p), LS+ / LS-lin, REFL at any o_F.
Anything reused from a pending text is re-proved here and labelled [RE-DERIVED], or stated as an explicit conditional.

## Not claimed
Reflection rigidity, INV*, any statement for other (k, kappa^) or for o_F, any assembly or word-class promotion, ordered Olson for
D_(2p) or for all groups, p = 5, existence or non-existence of avoiders outside the proved cells, novelty, priority, "first", Lean
or human review. Every new claim is CANDIDATE_UNVERIFIED; the parent owns model reviews and verdicts.

## Deliverables
Proof file and/or obstruction note (with interface/scope/import table), review package, excerpt manifest {path, sha256, start,
end} (<= 100 KB embedded), checkpoints (<= 1800 s apart, target 1200 s), IRC report to Main with paths and SHAs; then park.
