# Addendum 1 to the N=2 coupled-system packet: slack-case correction of (P1)/(P2)

Owner: InfoResearch96h-2 / info-1. Native clock observed immediately before writing: `Thu Oct 29 19:54:34 PDT 2026`.

**OWNER-WRITTEN SELF-FOUND ERRATUM (errata-only, as permitted while f273 runs).** The 105-LF source is preserved unchanged:

    frontier-20261029-n2-coupled-complementarity-system-v1.md
    SHA-256 d099eb4c4f0d69828e47c75ad9694b112e02ad843b13b30fd79d564ea79a50a2

This addendum must be read BEFORE the source. It corrects §4 (P1)/(P2); §2, §3 (the pooled-root identity and active-coupling analysis) are unaffected.

## The defect

(P1) asserted F_0 is always the clip of R_1 onto [t_0,2t_0−y], and (P2) that F_1 is the clip of R_1+1 with coupling floors. This is INCOMPLETE/WRONG in SLACK configurations where the coupling constraint is not active at the pointwise optimum. Counterexample (exact rationals): t_0=1/10, t_1=7/10, y=0, with R_0=2, R_1=13/10 (realizable by suitable λ,v). Boxes: F_0∈[1/10,1/5], F_1∈[7/10,7/5], coupling F_1≥F_0+1. The unconstrained-box projections are F_0=1/5, F_1=13/10, and 13/10≥1/5+1=6/5: the coupling is SLACK. The true pointwise minimizer is (1/5,13/10) — F_1 at its own root R_1=13/10, NOT at R_1+1=23/10. Formula (P2) gives min(7/5, max(7/10, 6/5, 23/10)) = 7/5 ≠ 13/10. Conversely, slack with F_0 INTERIOR forces F_0 = R_0 (its OWN root, not R_1) and F_1 = t_1 at its lower box with t_1 ≥ R_0+1 — also outside (P1).

## The correct two-line pointwise rule

For y∈[0,t_0] (both profiles present), with boxes B_0=[t_0,2t_0−y], B_1=[t_1,2t_1−y], let Π_0=proj(R_0,B_0), Π_1=proj(R_1,B_1) (componentwise, R_i the block's own root). The pointwise joint minimizer of the separable convex weighted objective over {F_0∈B_0, F_1∈B_1, F_1≥F_0+1} is:

* SLACK CASE, if Π_1 ≥ Π_0+1: (F_0,F_1)=(Π_0,Π_1). (Automatic when t_1>2t_0+1−y.)
* ACTIVE CASE, otherwise: F_0=S*, F_1=S*+1, where S*=proj(R_1, [max(t_0,t_1−1), min(2t_0−y,2t_1−y−1)]).

The interval in the active case is nonempty exactly when the slack test fails; feasibility of some pair always holds because t_1≥t_0+1/2 and y≤t_0 give 2t_1−y≥t_0+1. On the corner interval (t_0,t_0+1/2] only F_1 is present and its rule is unchanged: proj(R_1,[max(t_1,2t_0+1−y),2t_1−y]). At a slack/active transition the two rules give the same pair (the diagonal endpoint is the common limit), so the VALUE function is continuous; profile uniqueness can genuinely fail only at isolated pooled-stationarity coincidences, and any two minimizer pairs then give the same H_λ value by joint convexity.

## What survives unchanged

The rigid-translate statement (RIGID) is correct as stated ON THE ACTIVE REGION (where the coupling binds and both profiles are free of their boxes, F_1=F_0+1 and F_0=R_1 by §3). The exact two-scalar REDUCTION survives with the corrected pointwise rule, because the corrected rule is still an explicit function of (t_0,t_1,λ,y) only. The identity S(y)=R_1(y) of §3 and the infeasibility R_1<R_0 of §2 are untouched. The first unproved steps of §5 are unchanged except that (P3)'s envelope equations must now be derived from the corrected piecewise rule, and slack-case stationary branches (F_0 at its own root R_0 with F_1 at its lower box) are additional candidate branches.

This erratum does not edit the frozen source, does not retract the pooled-root identity, and does not claim any reviewed status.
