# Frozen scope: terminal k=p+1 lower-half cells 1<=kappa_hat<=(p-3)/2, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T21:17:19-0700 BEFORE derivation for this target. Authority: Main's IRC and
RUN/control/written-olson-lowerhalf-transition-v1.json, whole-file SHA256
3ff7a017912c3c89c8022c7d667ef417927b8eafae9eaedb8f8141bd59717b03 (recorded 2026-10-19T21:07:27-0700),
RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h. Same math2 ordered-Olson slot; not a new target or runtime
authority; global HOLD unchanged; contract-v1.json and control/worker-contract-v1.md apply. All prior artifacts read-only. Writes
ONLY this new directory, exclusive create x then chmod a-w; corrections are new versions/errata. Written mathematics only; hash,
byte and line-range metadata only. NO scripts/assertions/enumeration/numerics/probes, model CLI, nested agents, tests/build,
/tmp, overwrite/move/delete, commits/push, publication/contact or paid API.

## Exact target
Prime p>=11, integral 1<=kappa_hat<=(p-3)/2 (e=p-kappa_hat>=(p+3)/2). Exclude, uniformly, every length-(4p-2) avoider over D_(2p)
(no increasing-original-index identity 2p-subword) that has SOME admissible NF with terminal k=p+1 and that kappa_hat; full
word/existential-NF antecedent: H=e-1 extra reflection pairs anywhere in the odd blocks, empty NF runs separating different
reflection values; no o_F, nonempty-run, rotation-pair or reflection-rigidity hypothesis. Deliverable: a full uniform written
exclusion OR an exact new obstruction (precise surviving parameter/run/rotation regime) with every failed branch kept. A
single cell or a sub-case (for example a rotation-pair sub-case) is reported only as a labelled partial at its exact scope.
No full ordered-Olson, unrestricted INV*/REFL, multiset-only, novelty/priority/first, human-review or Lean claim.

## First obligation: NF-admissible range and accepted coverage (to be recorded in the proof file, from pins only)
- Range: accepted NF (ROT/proof-ROT-few-E-v4.md lines 28-43): all blocks odd, H=(F-k)/2, kappa_hat=p-1-H, R=2p+2kappa_hat-k,
  DAV kappa_hat<=k-1; GRX all-plus gives kappa_hat>=0 (as recorded in R18/olson-ASSEMBLY-LS-parent-verdict-v1.md line 38).
  At k=p+1: H>=0 gives kappa_hat<=p-1; so the admissible k=p+1 values are 0<=kappa_hat<=p-1, and the target is 1..(p-3)/2.
- Accepted coverage to cite, not duplicate: PP1 (kappa_hat=p-1), KP2 (p-2) and UH partials concern other cells; no accepted
  result found that excludes a whole lower-half k=p+1 cell. Accepted strengthened B0S-CJ triple-prime
  (R16/olson-cj-cjx-parent-verdict-v1.md lines 8-15) applies to the EQUAL-ROTATION sub-case: there Delta=k-p-kappa-1=-kappa<=0,
  R=p-1+2kappa>=4kappa-4 and 2kappa<=p-1, so its Delta<=0 branch gives an identity subword. This is a sub-case citation only.
  RP-LIFT (R=p) and RPdelta TRANSFER clauses concern other settings (rotation-pair reflection program) and are not this cell.
- Accepted inputs (literal scopes): NF; GRX if direction (ROT/notes-GRX-v1.md 7-20); RS(a)/RS(b) (SR2/proof-ROW-v1.md 16-27 with
  erratum-2 R5); classical Cauchy-Davenport; S1(a)/S1+ ((ZP)=>(S1) for 0<=kappa<=(p+1)/2, R16 ZX verdict line 19) if used;
  B0S-CJ''' at its exact B=0 setting; classical imports already accepted in this program (EGZ, Savchev-Chen) only at their
  classical statements and only if explicitly cited. UH-A/L/E are upper-half results and are NOT used. Unreviewed BOTTOM, RUH3,
  RUH2, KP3, KP4, R7 are NOT premises; any idea reused from them is re-proved inline.

## Pre-freeze exposure (none is a premise; no derivation before this freeze beyond these disclosed sketches)
My upper-half/bottom candidates (pairing Lemma P, common class Lemma U, windows W/MW, missing sets, lifts, position lemmas,
odd-gap rigidity) - their key counts FAIL in the lower half (2(p-1)>R, 2(2kappa+1)<=R). Mental sketches made while reading the
transition, unverified: (i) SR window at k=p+1: pattern with 2m sign changes forbids its target among n signed rotations for
every even n in [max(0,2kappa+2-2m),min(R,2p-2m)], R=p-1+2kappa; so m>=kappa+1 admits n=0 (T!=0); (ii) RS(a) at n=2kappa
suggests every nonconstant pattern has a signed value of multiplicity >=2kappa+1; (iii) an arc between two equal block values
has T=0, which with S1(a) at kappa-1 and Savchev-Chen suggests a dominant generator of multiplicity >=(p+4)/2 in that signed
multiset; (iv) in the rotation-pair case the targets T/2 must avoid integer intervals (B0-style lifts); a two-arc partition sum
gives only X(P1)+X(P2)=-p, no contradiction by itself; (v) block values alone can avoid zero alternating sums (y_i=i), so
rotations are essential.
Planned route: (1) rotation structure/rigidity at k=p+1 via SR patterns (arcs, many-interval patterns with n=0) plus S1/RS/CD;
(2) rotation-pair case with B>=1 via integer lifts (B=0 by cited CJ'''); (3) otherwise exact obstruction with failed branches.

## Deliverables
Proof/obstruction with import table, review package, JSON manifest {path,sha256,start,end} (<=100 KB embedded), checkpoints
<=1800 s apart (target 1200 s, including waits, /bin/date immediately before each timestamp), exact pins to Main, park.
