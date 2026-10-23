# N8 F_one refinement r2 — approved two-level protocol; NOT YET LAUNCHED

Supersedes static r1 (unchanged). Parent reviewed r1 and approved this production design with changes at host
2026-10-18T02:21:31-07:00. The current16-case queue must finish unchanged FIRST. This protocol is frozen before
any refinement child is generated/solved. A minimal pinned child-byte/controller delta must be sent before launch.
No measured-feed wrapper is required from the worker: ONLY parent measured-feed replay counts final refutations.

## 1. Source cases and schedule

Use WMAN355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74 and F_one
374d6fb46ab2a1f7a77bdf6699aa67792c126b2e2dcdf65ad37074be9fc5eeb9 (509915vars,5740226baseclauses).
Each source template has42units and5740268clauses. Keep all source results/ledgers immutable.

After all16 current case attempts finish, run P1-B1 as the ONE-family pilot. Its source is UNKNOWN (confirmed native
900s outcome), not an old-F transfer. If its whole tree closes with every terminal child LEGACY-worker-strict,
no UNKNOWN/SAT_PATTERN/UNSTARTED, proceed without another GO to each other template that ended UNKNOWN in the
current F_one pass, in WMAN order, one family at a time. Missing historical measured feeds on a producer candidate
alone is NOT an UNKNOWN trigger. Source solver-SAT patterns are reported, not silently scheduled for refutation.
If the pilot has any UNKNOWN after L2, or remains open by a resource/time gate, STOP and report; no later family
starts. A later family's unclosed tree likewise stops the automatic finite queue for parent review.

This is a bounded finite list inside the authorised session, not a permanent autonomous scheduler. No family may
start unless its cap fits before the run deadline2026-10-18T18:31:43-07:00; no continuation after authorisation.

## 2. Lists fixed for ALL16 templates now

L1 list Z1 (first3entries of existing V7):

    [1625,1674,1723] = [g_2((0,c),(2,0)) : c=1,2,3].

L2 list Z2 (first3entries of existing V8):

    [1632,1681,1730] = [g_2((0,c),(3,0)) : c=1,2,3].

Sources: README§8.1 and code/k5_cover.py CHAIN[7],[8], GMAP SHA7b4dd597…b197. Static lookup checked both lists,
all16template42unit sets, and mutual disjointness. Neither list includes the coordinate4 bit forced zero by Q2's
(1,0) singleton{4}/G5. Q1's row2 AND row3 supports are pure-B in every template, so no selected A bit is directly
zeroed by a positive Q1 bit via G2. Some L2 branches may be logically inconsistent with their L1 assignment; all
8patterns are still emitted. No claim is made that every branch is feasible or that a globally UNSAT formula has
logically free variables. The required disjointness is of explicit variable IDs in the path-unit lists.

Why this list: all42Q1 V1–V6bits are already fixed. The Q2 A-support profiles at consecutive column0 cells couple
to the distinguished Q1 A-component and to Q2 column orthogonality/G4/G5; the P1 one-zero block is where the original
900s cases remain hard. Reusing the next two published chain lists, but only their3distinguished A coordinates,
keeps branching8 rather than128 and avoids immediate coordinate0/4 zeros. This is a heuristic, not a speed claim.

## 3. Exact cover and formula identity

For L1, append EVERY2^3=8complete sign pattern of Z1 in list order to the source42units. Index b=0,...,7 sets Z1[j]
positive iff bit j of b is1. IDs `<T>.L1.000` through`.007` (decimal index),45units,5740271clauses.

Each L1 child that ends UNKNOWN is replaced AUTOMATICALLY by ALL8 Z2sign patterns, in the same convention, appended
AFTER its45units. IDs `<T>.L1.bbb.L2.000` through`.007`,48units,5740274clauses. A LEGACY-worker-strict L1 child stays
terminal; no extra children are required there. A child ending SAT_PATTERN stops the family immediately, preserving
its model and all other statuses; it is a Boolean support pattern, not a physical counterexample.

There is NO L3 and NO retry. L2 UNKNOWN stays UNKNOWN and is reported. The tree explicitly lists every created
child, including inconsistent000/111 assignments. There are8L1attempts and up to64L2attempts (72total), with8 to64
terminal leaves. Unstarted nodes remain explicit; no branch is dropped/pruned by symmetry or heuristic.
Traversal is deterministic: complete L1 indices0..7 first, then L2 for UNKNOWN L1 parents in ascending
parent index and child index. UNKNOWN L2 does not trigger L3; finish the remaining predeclared work if budgets
permit, then report the open pilot and do not start another family. SAT_PATTERN stops immediately.

For any total assignment, exactly one full3-bit sign pattern is true. Thus replacing a parent cube by all8 children
preserves its disjunction. Apply this twice to prove the L1/L2 frontier covers the exact source-template formula.
This is a Boolean product-cover argument independent of feasibility and of property-form T16. Only after parent-F4
refutations close every terminal leaf does the parent formula refute; final n8closure also needs every other weak
case, the accepted reduction/bindings and parent disposition. No old-F/c112 proof transfers.

## 4. Legacy pipeline and counting authority

Reuse the reviewed legacy R.certify unchanged (k5_resplit_r2.py SHA90b6f592…8484) and its predicate; the minimal
DATA delta is source42units +3Z1units, or source42+3Z1+3Z2units. The header count grows by3 at each level, with the
SAME F_one body, variable IDs and no new encoder clauses/auxiliaries/H3. Pin each child's exact expected CNF SHA and
ordered path units before solving, and bind the source case/manifest/hash and controller version.

Worker outcomes are producer candidates/LEGACY-worker-strict only. Retain precomputed input hashes, proof relay
hash/bytes, raw stored native logs, returncodes, self-exit/guard/feed/relay status and resource samples. Historical
separately delivered solver/checker feed hashes remain UNMEASURED; do not fill any measured field with a planned
hash. A worker strict boolean is sufficient only for production-tree scheduling as approved, NOT final F4.
ONLY parent's independent regeneration/re-solve/replay receipt, with both measured input-feed hashes and exact
CR-only raw-status predicate, counts a final child refutation. Parent replay remains under shared8GiB/4busy and
defers to the worker queue. A future measured worker wrapper is optional, a new version+controls, not a launch prerequisite.

## 5. Limits and finite family budget

Per child: CaDiCaL3.0.1 binary601c9fa8…d1fa, defaultseed, native300s; legacy checker111b0405…d5e4, native900s;
no switch/retry. Conservative wall guard1200s, then SIGTERM owned processes only and bounded wait30s, never SIGKILL.
Any timeout, resource/wall trip, input/proof/relay failure is UNKNOWN. SAT_PATTERN is distinguished from timeout;
pin the model and notify parent immediately. Native checker VERIFIED never overrides a guard/feed/error condition.

ONE10400s cumulative ACTIVE family cap covers the entire L1+L2 tree, including preparation, case execution and
bounded stops. It does NOT reset for each L1 subdivision or on a resume. Before another child, its1230s conservative
allowance must fit; otherwise leave it UNSTARTED/deferred and STOP/report. Outer chunk cap stays<10800s. External
parent-release waiting is not active execution, but no automatic resumption occurs after a failed resource gate.

Worst native allowance for all72children is far larger than this family cap; completion is not guaranteed. The cap
intentionally makes the pilot a bounded decision experiment. Any UNKNOWN/SAT/unstarted terminal keeps the template
open. Closed pilot permits the finite subsequent UNKNOWN-family queue; otherwise parent decides a new protocol.

## 6. Resources, retained bytes and deadline

One solver+checker pipeline(2busy) plus lightweight feeder; ownaggregate<=6GiB sampled<=2s. Shared lane<=8GiB and
4busy including parent's replay; no other heavy own job. No cap increase. Last observed hard pipelines were~4–4.5GiB;
this is a proxy only, not a new child measurement. A trip is UNKNOWN and never accepted by the scheduling predicate.

Keep the parent's SAME80MB family data allowance, NOT80MB per L1 subdivision. Up to72 attempts can occur only if
actual logs/receipts stay within that shared80MB budget. Budget10MB for the next child; if remaining family allowance
cannot reserve it, STOP before that child. No raw proof or CNF is retained; regenerate137.7MBbody in RAM/FIFO and
retain only native rawlogs/models/receipts. Use log-size guards/cooperative stop rather than truncating or deleting.

Pre-family gate: fresh sharedfree-80MB>=12.2e9, and measured lane data+80MB<=9.5GiB(10200547328B).
Pre-child gate: freshfree-10MB>=12.2e9, family actualretention+10MB<=80MB and lane actualdata+10MB<=9.5GiB.
Hard floor12e9 remains. Failed gate: record explicitfrontier, report ONCE, passive wait, no polling or fallback.
In-flight RAM/FIFO may finish with small receipts per owner. No snapshots/copies>10MB, deletion/thinning or proof
compression-unlink. All new files/caches inside the lane; existing environments read-only.

If4weak templates eventually need families, hard caps alone are4*10400s=11h33m20 BEFORE parent replay;16families
would be46h13m20 and cannot be promised in the remaining authorization. All16 worst-case family retention1.28GB
might exceed lane headroom; each launch uses measured gates. The current source UNKNOWN set is not assumed from
old-F outcomes. Report each family's counts/times/RSS/bytes/ledger pin; no all-frontier or deadline success claim.

## 7. Reporting and implementation prerequisite

Freeze the minimal data-plane diff and controller/source SHAs and send them before launch. Every completed child
must append its id, ancestor/depth, ordered45/48units, exact expected CNF hash/header, native solver/checker statuses,
seconds, peakRSS, legacy-candidate qualification, proof hash/bytes and rawlog paths/hashes. Emit this per child so
parent can replay immediately; no direct messages to the replay desk. New refinement ledgers stay separate from
the source16ledger and the historical Boolean cover; bind resume to full identity and never repeat a completed UNKNOWN.
The controller performs ONE child per finite invocation so its receipt can be sent to Main immediately,
before the next invocation; all family versions share the cumulative active-time/data budgets.
The source16pass must be complete before the first P1-B1 child. This design is frozen; no child has yet been generated
or solved at this version's creation. Parent-owned measured F4, not worker metadata, is the final counting authority.
