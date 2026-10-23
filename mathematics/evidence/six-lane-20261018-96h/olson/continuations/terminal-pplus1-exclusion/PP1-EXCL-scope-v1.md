# Frozen scope: EXCLUSION of terminal k = p+1, kappa^ = p-1 (all-singleton terminal blocks), v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T12:37:11-0700, BEFORE any written derivation for this target.
Authority: parent slot transition /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/
mathematics-slot-transitions-20261019-1230-v1.json (sha256 7317001625115b2be565642a3130e3072c5771ca4a585b700512ebfa5ffbb89f),
slot math2 (existing ordered-Olson problem; not an extra target, not runtime authority). Status of everything below: target
statement only, NOT a proof or verdict. Written mathematics only: no computation, enumeration, script, solver, test, build, Lean
or model CLI; hash/byte/line-range metadata only. Writes only in this directory, exclusive create, versioned names; every older
packet is read-only and untouched.

## Pre-freeze disclosure (nothing written before this file)
While reading the inputs (first /bin/date 2026-10-19T12:29:48-0700, until this freeze) I sketched mentally, without writing:
(s1) if every rotation letter lies in {rho_c, rho_-c}, c != 0, a GRX pattern with Phi = 2 selects 2p-2 rotations and its signed
sums form an arithmetic progression of difference 2c whose length is p as soon as both signed counts E+, E- are >= p-1;
(s2) applied to the all-plus pattern and to the p+1 single-run patterns (and the NF empty-run rule) this appears to exclude every
multiset inside one pair {c, -c};
(s3) in the types H2a / H2c of the pending ROT-SING+ classification, the single-run omission count (OM'-type) appears to exclude
them directly, without first deriving b = -a.
These are the planned route, UNVERIFIED at freeze; their written derivation and checking follow only after this freeze.

## Exact target (word level)
Theorem PP1-EXCL. Let p >= 7 be prime. There is NO avoider w of length 4p-2 over D_(2p) (no 2p letters in increasing original
index order with identity product) such that SOME admissible normal form w^ of w (accepted PM*/fusion process, existential
reading of ZX overlay 2) has terminal k = p+1 and kappa^ = p-1 (equivalently H^ = 0: the p+1 terminal blocks are single
reflections, F = p+1, R = 3p-3). No hypothesis on o_F(w), on reflection runs, or on nonempty runs.
Components:
(E1) Conditional Theorem EXCL-PM: the same conclusion under the EXPLICIT extra premise "every rotation letter of w lies in one set
     {rho_c, rho_-c}, c != 0" (this is the conclusion of the PENDING ROT-SING+; E1 states it as a hypothesis, never as accepted).
     Intended inputs: NF and GRX only.
(E2) Unconditional Theorem PP1-EXCL: the premise of E1 is NOT assumed. The parts of the ROT-SING+ route that are needed (Lemma CL
     via CT, Lemma OM/OM' via RS(b), Lemma ER and the elimination of type H1) are RE-DERIVED and re-checked in full in the new
     proof file, not imported; they are recorded as re-derivations, NOT as new progress. The new step is the elimination of the
     surviving multisets (types H2a, H2c, and every multiset inside one pair {c, -c}).

## Allowed outcomes
(O1) A written proof of E1 and E2. (O2) A fully specified WORD-level counterexample at a named p (letters and order) with
avoidance verified in writing through GRX. (O3) A precisely proved obstruction: exact failing step, smallest missing claim, every
failed branch preserved. A failure is never relabelled as a solution; no partial statement is silently substituted.

## Inputs (accepted scopes only)
NF (proof-ROT-few-E-v4.md Sec. 0 with fewodd addendum line 12, ZX overlays 1-3, lowodd item 2, M1, M4), including the rule that
every empty run separates blocks of different values; GRX for every cyclic constant-block representation and every sign pattern
(lowodd verdict item 1); Lemma CT (STAB-delta verdict item 6: p >= 5 prime, 0 <= kappa <= p-1); Lemma RS(b) (CFXT verdict
item 4) resting on the classical Cauchy-Davenport theorem. Each is cited by path, whole-file sha256 and line range.
NOT premises (context only): ROT-SING+ (pending), ROT-SING (accepted, k = p; not used), ONE-SHORT-LS (exact length p+2kappa),
ASSEMBLY-P, ROT-PP1 / ROT-PP1-TOP (candidates), (S1), Lev, S(p), REFL at any o_F (no REFL beyond o_F <= p exists; none is used).

## Not claimed
Reflection rigidity, INV*, any statement for other (k, kappa^) or for o_F, any assembly or word-class promotion, ordered Olson for
D_(2p) or for all groups, p = 5, existence or non-existence of avoiders outside this exact cell, novelty, priority, "first",
Lean or human review. Every new claim is CANDIDATE_UNVERIFIED; the parent owns model reviews and verdicts.

## Deliverables
Proof file (with interface/scope/import table), review package, excerpt manifest {path, sha256, start, end} (<= 100 KB
embedded), checkpoints (<= 1800 s apart, target 1200 s), IRC report to Main with paths and SHAs; then park.
