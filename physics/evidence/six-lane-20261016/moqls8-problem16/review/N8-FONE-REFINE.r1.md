# N8 F_one UNKNOWN-template refinement — static design r1 (NOT LAUNCHED)

Prepared at the parent's request. This document and its JSON are a preregistration only: no child CNF has been
generated, no child solved, and no running16-case input changed. Parent review and a NEW launch decision are required.
The current16-case queue remains900s/case, one pipeline, no retry. This plan proposes smaller limits for FUTURE
children only.

## 1. Frozen parent problem and eligibility

Use exactly WMAN355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74 and F_one base
374d6fb46ab2a1f7a77bdf6699aa67792c126b2e2dcdf65ad37074be9fc5eeb9 (509915variables,5740226baseclauses), as
independently parent-bound by65311ab0…28b0. A template T contributes its42 existing units, with5740268totalclauses.
The16-template genuine-object coverage is the conditionally accepted property-form T16, parent disposition29d17f38…eaeb.

Apply ONLY to template formulas still UNKNOWN after the current pass and explicitly selected by the parent, with no
parent full-F4 refutation already available. Missing historical worker feed measurements alone do not trigger a
refinement: those producer candidates first belong to the parent replay desk. A solver-SAT Boolean support model
is NOT an UNKNOWN to refute by subdivision; record SAT_PATTERN and seek a separate parent decision. It is not a
physical QLS counterexample.

The variable list below is fixed for ALL16 template IDs NOW, before any child is solved. Thus final parent selection
of an UNKNOWN case does not change its split rule. P1-B1 is the confirmed weakened-F UNKNOWN at the01:55 checkpoint;
the four old-F UNKNOWNs are resource-planning scenarios only, not transferred weakened-F outcomes.

## 2. Selection rule and exact variables (parent requirement a)

Split the A-support profile of Q2 at cell(2,0) in the row0 frame, A={1,2,3}:

    Z=[g_2((0,1),(2,0)),g_2((0,2),(2,0)),g_2((0,3),(2,0))]
     =[1625,1674,1723].

This is the FIRST THREE entries of the already-declared V7 in README§8.1 / code/k5_cover.py CHAIN[7]:
V7=g_2((0,c),(2,0)),c=1,...,7, with IDs[1625,1674,1723,1772,1821,1870,1919]. V1–V6 are unavailable because every
full-column template has already fixed those42 Q1 variables. No selected ID is among any template's42 fixed units.
Static map lookup against GMAP7b4dd597…b197 verified the three meanings and disjointness for all16 WMAN cases.
All16 Q1 row2 supports lie in B={4,5,6,7}, so their A bits are false; G2 therefore does not directly force any of
these Q2 A bits to zero. They are also not the base's Q2 row1 SB2 bits.

Why these three rather than the full7: the base gives Q2(1,0) support{4}, so coordinate4 at(2,0) is zero by column
orthogonality/same-ray G5; Q1's row2 support also excludes corresponding Q2 coordinates by G2. Avoid those immediate
zeros, while using a common3-bit list for every case. A is the distinguished3-coordinate component of Q1's witness
and the troublesome P1 one-zero block, so its Q2 overlap profile couples into frame/G4/G5 propagation. This is a
justified heuristic, not a promised speedup or an assertion that every branch is satisfiable.

Useful expectations (NEVER used to prune): profile000 forces Q2's nonempty support into B excluding4 and Q1's
row2 support. For root64 this is{5,6}; for root96 it is{5}; for root112 it is empty. Profile111, with Q1 row2
weight>=2, exceeds the seven-position disjoint-support budget after allowing three other nonempty squares.
Those inconsistent branches must still be emitted and checked like all others.

## 3. Full8-child cover and formula identity (requirement b)

For every selected template T with ordered42unit list U_T, emit ALL8 children indexed b=0,...,7. For j=0,1,2 append
+Z[j] if bit j of b is1 and -Z[j] otherwise. The order is Z[0],Z[1],Z[2]; existing42units remain unchanged and first.
Child id: `<template>.Q2A3.L1.<b>` (decimal b). Exactly45units,509915variables,5740271clauses per child; no new variable,
encoder clause, H3 family or square-type assumption.

For any total Boolean assignment there is exactly one sign pattern equal to its three Z values. Hence the
8-child disjunction is logically identical to the parent cube; F_one∧U_T is UNSAT iff all8 children are UNSAT.
This is a Boolean product cover, independent of the heuristic or of whether branches are already inconsistent.
No symmetry pruning, sample, omitted000/111 branch or old-F/c112 certificate is allowed. Every child CNF/hash must
be frozen before its launch from the SAME base and ordered45units.

## 4. Limits and stopping/refinement rule (requirement c)

Proposed FUTURE per-child limits: CaDiCaL3.0.1 (binary601c9fa8…d1fa, default seed, no switch) native300s;
parent drat-trim a46c0c71…8e37 native900s; no retry. The checker runs
concurrently on the binary stream. Conservative per-child wall guard1200s (not relying on overlap/native timer
implementation), then SIGTERM only owned processes and bounded wait30s, never SIGKILL. Any solver/checker timeout,
resource trip, incomplete stream, failure or unrecognised status is UNKNOWN, never UNSAT.

One family has8 explicit children. Attempt all8 once unless a resource gate defers or SAT_PATTERN makes refutation
of that formula impossible (then stop and preserve the remaining UNSTARTED children). Global family/chunk wall cap
10400s; stop between children rather than begin a child whose conservative1230s allowance does not fit. Preserve
complete receipts after each child in a NEW refinement ledger, separate from the original Boolean cover and from
the16-template ledger. Bind source case,42units,3extension units,ancestor/depth,hashes and attempt1 exactly on resume.

There is NO pre-authorised second split level. Any L1 child still UNKNOWN remains UNKNOWN after this pass; no
second attempt, seed switch, changed-limit run or recursive split starts automatically. Parent reviews the observed
frontier/timing and must freeze/authorise a new version before a level2. A completed UNKNOWN is not silently skipped
on resume; only never-started/interrupted-without-a-complete-receipt children can be considered under an explicit
resume decision.

## 5. Resource and deadline projections (requirement d)

One native solver+checker pipeline only (2busy, plus lightweight feeder). The existing engine+solver+checker aggregate
cap remains6GiB, sampled<=2s; parent/worker joint lane cap stays8GiB and4busy. Parent replay defers when two hard
pipelines would exceed those caps. No other heavy own lane job during a family.

One family:8*300=2400solver-seconds worst,8*900=7200checker-seconds worst, concurrent but conservatively<=9600s
plus8bounded-wait overheads<=240s and small preparation; a10400s chunk stays below the10800s contract. Lower-bound
parsing overhead proxy is a few seconds/child from earlier passes, but the new variable profile has NOT been piloted;
no measured mean/median or guaranteed shrink is claimed. The four-old-F-UNKNOWN planning scenario would mean
32children: native-budget sum10h40 plus overhead, conservative four-family hard caps11h33m20s BEFORE parent replay.
Worst16UNKNOWN templates mean128children: native-budget sum42h40, hard caps46h13m20s; that cannot be promised
inside the remaining authorization. Start only with a parent-approved ONE-family pilot; its performance must be
reported before a wider batch. The full scientific target is not narrowed by this staged resource decision.

Before a family: fresh sharedfree minus80MB projected family retention must remain>=12.2e9, and actual lane data
plus80MB must stay<=9.5GiB(10200547328bytes). Before EACH child: freshfree minus10MB must remain>=12.2e9. The hard
sharedfloor remains12e9. If a gate fails, record deferred/UNKNOWN or UNSTARTED as appropriate, report ONCE and wait
for the parent, without polling. In-flight RAM/FIFO proof streams may finish with small receipts under the owner's
rule. No proof/CNF copies or snapshots>10MB, no deletion/thinning/cap increase. CNF137.7MB is regenerated in RAM/FIFO;
only<=1MiB buffers, hashes, rawlogs/models and receipts persist. Conservative10MBretention/child,80MB/family; raw
solver/checker log guards keep individual files below10MB, cooperatively stopping/UNKNOWN rather than truncating or
deleting bytes. Four families~320MB fit the last observed~8.56GiB lane only conditionally on a NEW measured lane-size
gate; all16families~1.28GB might not fit, so no all-frontier disk promise.

## 6. Measured-feed/full-F4 prerequisite (requirement e)

The inherited LEGACY R.certify is NOT sufficient for this design's counted child refutations. A NEW versioned measured
wrapper plus parent review/controls is required before launch; none is implemented or run by this static plan.
It must use unbuffered writes/write-all loops and hash/count every byte ACTUALLY accepted by each write, separately
for solver-CNF and checker-CNF. Both measured complete hashes and counts must equal the independently regenerated
child CNF hash/byte length; record successful EOF/close and every error. Also hash/count proof bytes read from the
solver and actually written to the checker; require complete EOF/delivery and equal counts/hashes. Planned hashes
must never be copied into measured fields.

Capture native stdout/stderr as BYTES, retaining CRs; status parsing removes CR ONLY, no strip() or other whitespace
normalisation. Require solver self-exit20 + exact `s UNSATISFIABLE`; checker self-exit0 + exact `s VERIFIED`, no
`s NOT VERIFIED`/`s TIMEOUT`, no unrecognised fatal/warning, guard, relay or feed error. A checker VERIFIED with a
failed/incomplete byte delivery is UNKNOWN. Controls before use must separately cover: positive valid proof;
SAT+bogus empty clause; a mutated/truncated proof; wrong-child/unit hash; partial-feed/bad-tail while native checker
says VERIFIED; native timeout/RSS guard; exact-line whitespace rejection. Controls and their intended failures are
recorded without claiming they already ran for this future wrapper.

Every final counted child requires independent PARENT regeneration/re-solve/replay with its own measured feeds,
parentchecker a46c0c71…8e37 (not a copied expected hash or worker binary111b0405…d5e4), accepted negative controls
and disposition. Only8qualifying child refutations close one parent template; all16 parent templates still need
qualifying direct refutations or validated closed child covers for the original conditional theorem. No old-F or old
c112 result transfers; no SAT support model becomes a physical counterexample without vectors/exact verification.

## 7. Status

STATIC/NOT LAUNCHED. Only map/unit disjointness data were read to bind the list. No child generated/solved, no
runtime limit or existing input changed. Parent review and a new explicit go are required before any implementation
or execution of this design.
