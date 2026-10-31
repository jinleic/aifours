# Actual septic interval boxes: common three-root test must avoid five boundary roots

**Disposition: scoped same-harness written support plus separately authored exact finite verification.** Native observation before composition: 2026-10-30T10:51:32-0700 PDT. f389 reports **0 FATAL / 0 MAJOR / 0 MINOR**. This excludes a family of candidate common tests, not the existence of every possible interior test or the original common-SPR theorem.

## Uniform actual-box theorem and quantifiers

At the earlier adopted actual-box interface, let K be a compact independent coefficient box of monic strictly Hurwitz real septics, with at least one nonzero odd coefficient width AND at least one nonzero even coefficient width. Write the odd endpoint cubics

O_-=(a−t)(d−t)(e−t), O_+=(b−t)(c−t)(f−t), 0<a<b<c<d<e<f.

For a single F(t)=(x−t)(y−t)(z−t), (x,y,z) in [0,a]×[b,c]×[d,e], choose the actual minimizing even endpoint E_F(t)=E_-(t) when F>=0 and E_+(t) when F<0. If x=a, y=b or c, or z=d or e, there is an actual-endpoint positive R5 ray with negative pairing sum_i mu_i E_F(u_i)F(u_i)<0. The quantifiers are

**for every such K, for every such boundary-root F, there exists an actual negative R5 ray.**

Consequently any F nonnegative on EVERY actual R5 ray must satisfy x in[0,a), y in(b,c), z in(d,e). The endpoint x=0 is explicitly still permitted. Both R5 orientations remain in the full dual cone; zero-odd singleton and same-frequency cancellation rays are not discarded. Interior-root existence/sufficiency and strict SPR synthesis are not proved.

For the proof, positive even width gives DeltaE(t)=E_+(t)−E_-(t)>0 for t>0. Pair two adjacent nodes r±h around a simple root r common to F and an actual odd endpoint O_*, and hold the other three feasible ordered nodes fixed. The actual minimizing envelope switches across r. Positivity of the R5 weights fixes the orientation sign, giving

lim_(h→0+) 2h P_h = −|F'(r)| DeltaE(r) / [r |O_*'(r)| |product_(other nodes)(r−v)|] <0.

All five boundary placements have explicitly verified actual endpoint sign choices and nonzero denominators; both positive-first and negative-first R5 orientations occur. The other three contributions remain finite, so the full pairing is negative for small h. It is not one fixed ray defeating all F, and it fails to give a strict cusp when even width is zero.

## One exact actual-box fixed-test counterexample

For the independent box

s7+s6+a5 s5+(13/2)s4+a3 s3+11s2+a1 s+a0,
a0 in[15/4,17/4], a1 in[1197/80,15], a3 in[23,467/20], a5 in[179/20,9],

all members are strictly Hurwitz: every actual odd cubic has exactly one simple root in each of [19/20,1],[3,7/2],[9/2,5]; every actual even cubic has one simple root in each of (0,19/20),(1,3),(7/2,9/2). Strict interlacing plus the positive orientation at s=1 pays the named classical [Hermite–Biehler theorem](https://arxiv.org/html/math/0512591v1). This is a written ALL-COEFFICIENT proof, not a finite-corner sampling inference.

For the FIXED F=−t(1−t)(9/2−t), five positive-weight actual-corner atoms at t=(1/2,39/40,1−1/10000,1+1/10000,7/2) yield the exact pairing

−32476663889228279938856844274881800000000 / 969312078282210903256702765048923681 < −7874.

The full eight-coordinate aggregate has signs **(−,0,+,0,−,0,+,0)**. It is NOT an eight-strict-negative counterexample to common-SPR feasibility. Independently, the two actual members (E_+,O_+) and (E_-,O_+) require incompatible derivatives G(1)=−35/64 and −49/64, so no polynomial G makes even weak inequalities hold for this fixed F. Neither argument excludes a different interior F.

## Verification and remaining target

[Author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f380-spr-actual-box-common-test-or-original-certificate-frontier/review-v1.md) · [Disjoint written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f389-spr-actual-boundary-root-obstruction-written-review/review-v1.md) · [Independent finite report](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f390-spr-boundary-r5-independent-exact-finite-check/review-v1.md). Parent displayed all829 author lines,537 review lines and772 finite-report/source lines, reconstructed cusp sign/strictness/all placements, HB orientation and exact fixed-F quantifiers, and checked frozen pins. The author checker was parent-run once, exit0; it is not independent evidence. A separately authored [Fraction verifier](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f390-spr-boundary-r5-independent-exact-finite-check/independent-r5-fraction-check-v1.py) was parent-run once: exit0, all16 actual corners, five actual atoms/positive weights, exact four zero odd moments and all eight signs, identical direct and factorized pairing, four intended-reason mutations rejected. [Independent actual-run receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f390-spr-boundary-r5-independent-exact-finite-check/parent-independent-finite-run-v1-receipt.json). The finite checker is not a proof for continuum K or all F. No child scientific execution was reported.

The public degree-six work and classical HB are prior sources; no claim of novelty, full-paper coverage or independently replayed external formalization. No eligible box is shown to lack EVERY common F, no eight-strict-negative aggregate and no strict common-SPR numerator are supplied. Source authenticity, human/independent-family/formal-kernel and original-target acceptance remain unpaid.
