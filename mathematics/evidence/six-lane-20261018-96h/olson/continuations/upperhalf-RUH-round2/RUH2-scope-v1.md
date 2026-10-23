# Frozen scope: R-UH round 2 -- uniform attack for p>=11, (p-1)/2<=kappa<=p-5, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T17:07:02-0700, BEFORE any derivation for this target.
Authority: Main's IRC and RUN/control/written-slot-transitions-olson-beta-prt-20261019-1708-v1.json, whole-file SHA256
32d161b0408bc297f0e95516980142d741eb219dc882e40bd93df9c79cd59f12 (recorded 2026-10-19T17:06:06-0700), key math2,
RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h. Existing ordered-Olson problem (math2 slot); not an
extra target, not runtime authority (global HOLD unchanged). Writes ONLY this new directory, exclusive create x, then chmod
a-w; corrections are new versions or errata. All older packets stay untouched. Written mathematics only; hash/byte/range
metadata only; NO scripts, assertions, enumeration, probes, CLI, nested agents, tests or computation over scientific data.

## Exact target
R-UH (named in obstruction-UH-EXCL-v1.md, SHA256 f2f1a232c98b3ef6eb45fa0486912bd54170521e5adc00e09c436b1fb8c7849d, line 44,
read with the accepted parent errata v1-v3 of the UH verdict, in particular lambda=c-1): for every prime p>=11 and every kappa
with (p-1)/2<=kappa<=p-5 (e:=p-kappa in [5,(p+1)/2]), under the FULL antecedent (an avoider w of length 4p-2 over D_(2p) has
SOME admissible NF with terminal k=p+1 and kappa^=kappa; H^=e-1 distributed arbitrarily among the odd blocks; every empty run
separates different reflection values; no o_F, nonempty-run, reflection-rigidity or rotation-pair hypothesis), and in the
residual multiplicity range A=2kappa+c with 3<=c<=2e-1 (A the larger multiplicity of the common nonzero dominant class, as in
UH-A): show that some sign pattern and some admissible length attain the target, i.e. exclude every such avoider.
Deliverable: a complete written proof on the whole range, OR the exact smallest remaining residual in (p, kappa, c, run-profile)
form with every failed branch and its arithmetic retained. A result for a sub-range (e.g. one kappa, or 3e<=p+2 only) is
reported ONLY as a clearly labelled partial with its exact parameter range; nothing is silently substituted.

## Inputs (accepted scopes only)
NF (proof-ROT-few-E-v4.md 28-43; empty-run rule at 38; fewodd addendum 1 line 12, ZX overlays 1-3, lowodd item 2, M1, M4);
GRX if direction (notes-GRX-v1.md 7-20; lowodd item 1, M2); RS(b) (proof-ROW-v1.md 16-27 with erratum-2 R5) with classical
Cauchy-Davenport; accepted UH-A, UH-L, UH-E at literal scope (RUN/review/olson-UH-CONSTRAINTS-parent-verdict-v1.md SHA256
7c7b90f2745ba0cb7a8300c3f914a72c4b457259e4fcd45385266db15e4a71e3, errata v1 8f1ea491..., v2 ac2a7f26..., v3 0dc67886...);
accepted PP1/KP2 verdicts at their own cells (context; not usable outside those cells). UH-MW/SH/PH are accepted too and may be
cited at literal scope if needed (recorded as input). NOT premises: KP3-EXCL, KP4 (proof-KP4-v1.md and its p=7 obstruction),
R7 (proof-R7-v1.md) -- CANDIDATES; any of their steps used here is re-proved inline and labelled [RE-DERIVED]. Not used:
ASSEMBLY-P, RPdelta, REFL, RUNS/RGR-LONG, S(p), Lev, (S1), LS-family, CT (unless re-scoped by a new version of this file).

## Pre-freeze exposure (prior knowledge and sketches; NONE is a premise or verified for this target)
My own candidate packets (KP3 e=3, KP4 e=4 with p>=11, R7 p=7) used: SR with C in [Phi,Phi+2(e-1)]; pairing (Lemma P) giving a
dominant signed multiplicity >=2kappa+1; the common class (Lemma U); the ordinary window lambda=A-2kappa-1, Lambda=2kappa+1-A';
multi-length omission windows MW at m=2,...,e (strong bounds for sets avoiding a heavy run); the single-toggle m=e path from
{0,2,...,2e-2} to its complement giving a super-heavy run when the m=e window is strong; light sets; >=2 empty runs; the
subset-sum missing set M with |M|<=c and the free/non-free length rule r=n-A; band subset-sum arguments (W as "no subset of runs
has d in the band"), zero-weight run counts and complete partition lists; pair-case epsilon intervals. From UH: the m=e window is
strong only when 3e<=p+2 (SH); for 3e>p+2 (e.g. every allowed kappa at p=11, e in {5,6}) no strong m=e window is known.
Planned route (unverified): (s1) generalise MW to every m<=e and find, for each (p,e), the smallest m giving phi>=p+kappa-something;
(s2) super-heavy run and light sets where available; (s3) band/subset-sum and empty-run analysis in terms of c and e;
(s4) where the route stops, record the exact (p,kappa,c,profile) residual.

## Not claimed
UH-EXCL itself (it would also need the pending KP3/KP4/R7 and other cells), reflection rigidity, INV*, REFL, o_F assembly,
ordered Olson, the lower half, p<11, multiset-only non-existence outside the full NF antecedent, novelty, priority, "first",
Lean or human review. Every new claim is CANDIDATE_UNVERIFIED; the parent owns both-family reviews and verdicts.

## Deliverables
Proof or residual note with interface/import table, review package and {path,sha256,start,end} manifest (<=100 KB embedded),
checkpoints at most 1800 s apart (target 1200 s) including waits, IRC to Main with full paths/SHAs; then park.
