# Actual septic box: a six-node counterexample to one W1-only moment bridge

**Disposition: scoped exact finite counterexample, with a written all-parameter Hurwitz proof and two separate exact Fraction implementations.** Native observation before composition: 2026-10-30T09:18:54-0700 PDT. This example is NOT a strict-negative certificate and does NOT settle the original common-SPR problem.

## Actual coefficient box and all-member Hurwitz property

Consider the independent box with only delta varying in [−1,1]:

a_delta(s)=s⁷+s⁶+9s⁵+(13/2)s⁴+23s³+11s²+(15+delta)s+4.

Its parities at t=omega² are E(t)=(1/2−t)(2−t)(4−t) and O_delta(t)=(1−t)(3−t)(5−t)+delta. Across the ENTIRE delta interval, O(1/2) lies in [37/8,53/8], O(2) in [−4,−2], O(4) in [2,4], and the leading odd term is −t³. Each odd polynomial thus has three simple roots, one respectively in (1/2,2), (2,4) and (4,infinity), strictly interlaced with the actual even roots 1/2,2,4. The named classical Hermite–Biehler criterion gives strict Hurwitz stability for EVERY member, not just sampled deltas.

## Six actual nodes and exact moment counterexample

Take nodes (9/10,14/15,29/30,1,31/30,16/15) and respective actual deltas (−961/1000,−3107/6750,−10081/27000,1/10,4321/27000,4097/6750). Their odd values are exactly (−,+,−,+,−,+)/10. Define H6(t)=product_i(t−u_i) and positive weights mu_i=1/[u_i O_i H6′(u_i)]. Lagrange interpolation makes all four odd moment coordinates exactly zero.

The directly computed eight-coordinate raw aggregate is

(−612905105250/6293, 0, 95737200, 0, −94242480, 0, 278709746/3, 0).

Its signs are (−,0,+,0,−,0,+,0), explicitly NOT eight strict negatives.

The five-node negative-first ray on nodes1–5 and positive-first ray on nodes2–6 are both positive and zero-odd-moment; their sum, multiplied by6, is exactly the six-node weight vector. Exhausting the six same-data five-node subsets leaves exactly ONE positive-first ray, supported on nodes2–6; it has first coordinate zero while the six-node weight at node1 is positive. Thus it is impossible to express this vector as a nonnegative combination of only positive-first five-node zero-odd-moment vectors on the SAME nodes and actual odd values. This refutes that specific moment-only W1 bridge. It does NOT refute a proposed reduction that also uses all four strict even inequalities, which this example fails.

## Evidence and controls

Parent displayed the complete 923-logical-line f347 candidate and complete 729-logical-line independent f356 finite review/verifier, including all source lines; [author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f347-spr-actual-member-bridge-general-author/review-v1.md) · [written exact review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f356-spr-actual-six-node-moment-counterexample-independent-check/review-v1.md). Its first packet preview preceded all controls; the full controls and packet were read before its derivation as reported, with no retroactive clean-order claim. Fresh selected examples were allowed under the general-author/finite-check duties.

The [parent independent Fraction checker](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f356-spr-actual-six-node-moment-counterexample-independent-check/parent-fraction-check-v1.py) exited0 and directly computed all eight exact coordinates, the two-ray decomposition and all positive-first supports, rejecting four named box/value/weight/orientation mutations. [Parent run receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f356-spr-actual-six-node-moment-counterexample-independent-check/parent-independent-fraction-run-v1-receipt.json) · [Exact output](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f356-spr-actual-six-node-moment-counterexample-independent-check/parent-independent-fraction-run-v1.stdout.json). A separately authored [second Fraction verifier](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f356-spr-actual-six-node-moment-counterexample-independent-check/fraction-verifier-v1.py) was inspected in full and executed ONCE by the parent: exit0, RESULT=PASS, with all nine intended-reason mutations rejected, including expanded box/HB boundary, both orientations, wrong decomposition and first-coordinate failure. [Second run receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f356-spr-actual-six-node-moment-counterexample-independent-check/fraction-verifier-v1-parent-run-receipt.json) · [Full output](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f356-spr-actual-six-node-moment-counterexample-independent-check/fraction-verifier-v1.stdout.txt). The second reviewer's originally reported execution status was NOTRUN; these are later actual parent executions, not retroactive reviewer runs. Neither script requires external packages or author code; no data were deleted.

The numerical example and named classical HB import have not been human, independent-model-family or formal/kernel certified; neither the wider f347 actual-box reduction nor a strict SPR numerator follows from this finite check. Novelty/priority remain unassessed.
