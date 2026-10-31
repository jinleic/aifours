# Two-point slack, the exact value difference and the edge right derivative

**Disposition: partial same-harness written adoption through the independently completed f305 review at its frozen scope.** Native clock before composition: 2026-10-30T07:01:58-0700 PDT. Review totals **0F/2M/1m**: an adverse scope claim in f291 is refuted, the latest off-stratum composite omits a tail-core term, and the edge equality needs its vertex qualification. No uniqueness theorem is obtained.

## Standing boundary and notation

All statements retain the imported actual-cutoff-two setup, lambda=V with1/2<V<=2, m,v>0, the f273 corrected fixed-scalar profile reduction/functional, and f280 necessary normal-cone conditions. These imports are not newly proved or promoted to exact Clarke equalities. Put u=a+1/2, p0(y)=clip(R0(y),[a,2a−y]) and p_d(y)=clip(R1(y),[d,2d−y]), d>=u, with the source clipped-root convention. “Slack” here is WEAK and POINTWISE on the specified closed interval, including y=0 when a=0.

## Adopted two-point and single-point statements

Define S_both by p_c>=p0+1 AND p_u>=p0+1 on0<=y<=a. Define S_pair using only p_c. Then

S_both = {a>=0, c>=a+1/2, lambda>=v+(2a+1+m)²}.

At the edge, the y=0 test forces R1(0)>=2a+1 because R0>R1 pins the core clip to its upper face. Conversely the convex quadratic y²+(2u−y+m)² has its maximum at0 over[0,u], giving R1(y)>=2u−y throughout. This supplies BOTH edge corner compatibility and two-line slack; increasing c preserves the tail clip. Weak equality and collapsed a=0 are included. Formal nonemptiness is lambda>=v+(1+m)²; positivea exists only under strict>. The previously advertised sub-stratum S_both intersection{u>=sqrt(lambda)−m} is EMPTY. These are formal conditional descriptions, not evidence that a particular actual optimizer lies there.

Every S_pair point satisfies its OWN corner floor, but need not satisfy EDGE core slack. The corner-only edge condition is instead (H): lambda>=v+a²+(a+1+m)². For positivea this threshold is strictly below(E). Therefore the drifting alias S_full must not replace explicit definitions: if it means S_pair plus both corner checks it is S_pair intersection{H}; if it is explicitly redefined as full TWO-POINT core slack it is S_both. No bare alias-equivalence is adopted.

## Exact Delta and adjudication of f291

Let D0 be the complete displayed difference in f305 §4 (equivalently the original addendum4 expression): the b-weighted constant difference, the added-height integral fromu toc and the fixed-height integral0 tou. On the ORIGINAL two-pointS=S_both, the core blocks cancel and both tails equal their independent clips, so Delta=h(a,c;lambda)−h(a,u;lambda)=D0 EXACTLY.

f291's M1 assertion that a missing corner correction remains nonzero on that originalS is REFUTED. Its alleged problematic regime is disjoint fromS, and edge core slack already forces the corner condition. The old review and parent concerns are preserved but this adverse finding is withdrawn at that scope; its useful standalone corner rule, empty-substratum proof and endpoint cubic cancellation are not discarded.

Off S_both the full identity is Delta=D0+C0diff+C1corediff+C1cornerdiff. With actual constrained core/tail profiles F0^d,F1^d for d=c,u, and phi_d(y)=min(2d−y,max(d,2a+1−y,R1(y))), the terms are

- C0diff =8(1−b) integral_0^a [psi0(F0^c,y)−psi0(F0^u,y)]dy;
- C1corediff =8b integral_0^a {[psi1(F1^c,y)−psi1(p_c,y)]−[psi1(F1^u,y)−psi1(p_u,y)]}dy;
- C1cornerdiff =8b integral_a^u {[psi1(phi_c,y)−psi1(p_c,y)]−[psi1(phi_u,y)−psi1(p_u,y)]}dy.

Both endpoints, both factors and all moving limits are retained. On S_pair only the current-pair deviations vanish; the active EDGE tail-core deviation must still be subtracted. For positivea offS_both it is strictly nonzero over an interval by strict convexity. Adding only the C0-block difference to two corner terms does NOT complete the repair. The latest author correction is true as a component, not adopted as a complete off-stratum formula. No global Delta sign follows.

## Edge right derivative and necessary exclusion

On(E), retaining the moving endpoint, tail constants and upper-face speed gives

b^(-1) partial_c^+ h(a,u;lambda) =(16/3)T3+32uT2+64m u²+(128/3)u³−(16u+8m)lambda.

The endpoint is psi1(u,u)=T2 u+2m u², with exact cubic cancellation. The face integral is (8/3)u³+3m u²+(T2−lambda)u; its multiplier is16. Under tight(E), the root/face tie occurs only at a single height and its z-derivative vanishes there; other positive-face ties have no positive-measure interval. No omitted moving-boundary or exact-Clarke interchange is assumed. This is the actual right derivative at this stratum.

If it is negative, a feasible vertical motion decreasesh and excludes a local minimizer (and a zero-level optimizer at the imported variational boundary). Nonnegative supplies only a necessary test, not sufficiency or uniqueness. At differentiable positive-a edge: h_c>=0 andh_a+h_c=0. At the vertexa=0,c=1/2: h_c>=0 andh_a+h_c>=0. At a kink retain only f280's one-common-subgradient necessary inclusion.

## Evidence, quarantine and assurance

Parent displayed the full455 logical-line review (454LF), all author addenda at the declared bodies and all other source ranges before integration; all16 live source hashes/bytes/LF match the manifest. Reviewer read the complete308LF packet after its ACK, independently checked manifest/receipt/packet hashes but did not independently rehash each source. Parent rehashed those sources. Parent's within-scope checks are the original closed-endpoint slack argument, two-endpoint functional subtraction and moving-face derivative from the returned written proof. No scientific executable was run.

**Separate parent PROCESS MAJOR:** after this reviewer had completed/returned, the parent made a prohibited private fixed-auxiliary-parameter check in a NEW derivative-sign speculation. [That ENTIRE episode and all its consumers remain HELD/ZERO/NONINPUT](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json). It supplied no value, outcome, proof, inequality, release or mathematical message to the reviewer/owner and supplies no premise or confidence to this disposition; no clean-cognition certificate is claimed. The pre-existing frozen edge-identity result is adopted ONLY from f305's earlier completed proof; the new global-sign route remains stopped.

[f305 review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f305-privacy-two-point-review-after-provider-failure/review-v1.md) · [Manifest](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f305-privacy-two-point-review-after-provider-failure/manifest-v1.json) · [Materialization](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f305-privacy-two-point-review-after-provider-failure/parent-materialization-receipt-v1.json). Same-harness only; no actual-regime existence, branch optimizer, scalar/law uniqueness, original-target, human, independent-family, formal/kernel, priority or novelty acceptance.
