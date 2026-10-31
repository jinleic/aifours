# Actual d=4 CORE-GRAM counterexample and rank-two sufficient regions

**Disposition: scoped same-harness written support plus an independently authored exact physical-matrix check, parent-run once.** The previously conditional universal CORE-GRAM sufficient premise is **FALSE** on genuine doubly orthonormal d=4 singular frames, even with both diagonal gaps strictly positive. This is a failure of a sufficient proof route, **NOT** a counterexample to the original rank-two dual inequality Q or the physical two-copy T2 inequality. The actual rank-two witness below satisfies Q with a strict margin. The earlier implication CORE-GRAM⇒Q⇒T2 remains a valid conditional implication; its premise is now disproved. The original Q/T2 problem remains OPEN.

## Actual frame and exact counterexample

In H=C4⊗C4, set

a=(4|00>+2|11>+2|22>+|33>)/5,
u1=|01>, v1=−(6|01>+8|02>+|10>)/sqrt(101), u2=v2=a,
x_i=|u_i><v_i|.

Both u-pair and v-pair are orthonormal. With c_i=Tr(x_i), C12=<Tr_B x1,Tr_B x2>+<Tr_A x1,Tr_A x2> using the conjugate-linear-first Hilbert–Schmidt inner product, and 4p_i=1+|c_i|²−||Tr_B x_i||²−||Tr_A x_i||², direct physical partial traces give

p1=1/404>0, p2=168/625>0, C12=−24/(5sqrt(101)),
conjugate(c1)c2−C12=−6/(5sqrt(101)) < −4sqrt(p1p2).

The strict comparison is 900>672 after taking positive squares. For this real frame the earlier displayed c1 conjugate(c2) has the same real part, so the literal old CORE-GRAM inequality is also violated. More generally the Hermitian cross coefficient multiplying conjugate(z1)z2 is **conjugate(c1)c2−C12**; do not transpose the conjugation in a complex-phase calculation. The old real-part identity for real singular weights remains correct because the two trace products have the same real part.

The ACTUAL rank-two operator is

R=x1+x2/sqrt(101)
 = (|a><a|−6|01><01|−8|01><02|−|01><10|)/sqrt(101).

It has singular values 1 and1/sqrt(101), norm²=102/101, TrR=−5/sqrt(101), and

Tr_B R=diag(−134,4,4,1)/(25sqrt(101)),
Tr_A R=(diag(16,−146,4,1)−200E12)/(25sqrt(101)).

Thus for G(R)=||R||²+|TrR|²−||Tr_B R||²−||Tr_A R||²,

G(R)=−203/63125 < 0,  q(R)=143531/126250 < 255000/126250=2||R||².

This witness is nontraceless, non-EP, has C12≠0, and both common local supports have dimension4. The strict CORE failure persists on a nonempty open set of full-Schmidt-rank doubly orthonormal frames by the explicit perturbation and determinant/continuity argument in the [complete author proof](../review-waves/f643-werner-two-copy-actual-rank2-nontrivial-frontier/author-candidate-v1.md). None of those facts asserts a violation of Q.

## Sufficient actual-frame regions and exact residual

For any actual doubly orthonormal frame, set q_i=q(x_i), h=C12−conjugate(c1)c2/2 and alpha_i=2−q_i>=1/2. For every complex z1,z2,

q(z1x1+z2x2) <= (|z1|sqrt(q1)+|z2|sqrt(q2))²
                   <= (q1+q2)(|z1|²+|z2|²).

Consequently q1+q2<=2 suffices for Q on the ENTIRE actual complex two-dyad span. The counterexample frame lies strictly inside that paid region: q1=118/101, q2=531/1250, q1+q2=201131/126250<2. This region's UNION with the previously named rank-one/traceless/EP/C12=0/common-local-qubit classes strictly enlarges those classes; no claim is made that this one region contains all of them.

For actual SVD weights s1>=s2>=0, the general rank-one bound q_i<=3/2 also pays s2/s1<=3−2sqrt(2), including its boundary. It is sufficient, not necessary.

For a given actual frame, Q on its whole complex span is EXACTLY equivalent to

|C12−conjugate(c1)c2/2|² <= (1−|c1|²/2+4p1)(1−|c2|²/2+4p2).

This is positivity of the actual 2×2 residual Gram matrix. Quantifying it over all actual frames is exactly Q and, by the separately adopted DOUBLE-UNIVERSAL duality, T2 for all traceless physical A,B. The remaining unpaid problem is this determinant inequality on all frames not already covered, in particular q1+q2>2. A future genuine strict failure can be converted, with z1=h,z2=alpha1, to an actual rank-two Q violation and corresponding physical traceless A,B; no such failure is supplied here.

## Separate physical-pair region

For X=A⊗I+I⊗B with traceless complex4×4 A,B and L=||A||²+||B||², rank-one duality gives sigma1(X)²<=3L/2. Thus sigma2(X)/sigma1(X)<=1/sqrt(3) suffices for S2(X)<=2L, with zero case and equality boundary included. This is a condition on actual physical PAIRS, not the preceding condition on dual frames.

An explicit open non-2+2-reducing example is A=B=M=D+N/10, D=diag(3,−1,−1,−1), N=E01+E12+E23. Actual X0=D⊗I+I⊗D has singular values6 once and2 fifteen times, and ||X−X0||<=1/5. Hence sigma2/sigma1<=11/29<1/sqrt3, L=1203/50 and S2<=1443L/841<2L. M is unitarily irreducible by its adjoint cyclic chain, and M² is nonnormal; both properties and the strict gap persist on an open neighborhood. The union with the separately2+2-reducing class is strictly larger, but this pair is not claimed outside every other known physical class or novel.

## Exact gate evidence and correction boundary

The complete [f643 author](../review-waves/f643-werner-two-copy-actual-rank2-nontrivial-frontier/author-candidate-v1.md), SHA256 `ccaf062c7547afd3d3c618b95673d1fb9fb6cc2a0fbd2632f1ee7276e7e53121`, 162LF; [f647 CORE/dual written review](../review-waves/f647-werner-actual-coregram-counterexample-and-dual-regions-written-review/review-v1.md), SHA256 `d6162172fad20bc9efc61a09e15b69bec1e9be228681d4edcb510a8e69cab77f`, 409 logical lines; and [f648 physical-pair written review](../review-waves/f648-werner-physical-spectral-gap-and-irreducibility-written-review/review-v1.md), SHA256 `fef74ea871a0fce0f260c2e82c9fb4f0dcc9514e8533ecb02643004fb55a07b6`, 517 logical lines, were fully parent-read. Each reviewer found0 FATAL / 0 MAJOR / 0 MINOR in this new candidate at exact scope. They used the clean original dual disposition and named source inputs, never the held CORE diagnostic or f285/f289 episodes.

Parent fully read the [f649 exact finite narrative](../review-waves/f649-werner-coregram-actual-frame-and-physical-pair-independent-exact-finite-author/author-candidate-v1.md), 163LF, and all435 lines of the [independent source](../review-waves/f649-werner-coregram-actual-frame-and-physical-pair-independent-exact-finite-author/finite-checker-v1.py), SHA256 `1811521d363170e0bafa2b692287ef5f7e02211610854a64a37f53d4eab8f1a3`, before GO. [Parent one-shot receipt](../review-waves/f649-werner-coregram-actual-frame-and-physical-pair-independent-exact-finite-author/parent-independent-finite-run-v1-receipt.json), SHA256 `e06fcaab0af8e023890431e7dc8c7a99a030746d997486d35ba02808ed94c3ad`, records exactly one isolated Python run, exit0, empty stderr,0.060969s, cooperative54-second/external55-second deadlines.

The exact Gaussian-rational checker constructs all entries of the actual16×16 frame operator with sqrt(101) factored, independently constructs its projector, verifies rank/SVD actions, partial traces, frame gap and negative G, and shows the same R satisfies Q. It checks the positive full-span residual determinant 80673/63125, constructs the actual physical Kronecker-sum pair, checks its rational bounds, rank15 commutant system and squared-matrix nonnormality. Seven named-reason mutations discriminate core sign, complex conjugation, trace order, frame orthogonality, a falsely asserted Q violation, physical normalization and a reducible diagonal comparison. These are finite exact checks, not universal proof, floating numerical evidence, a T2 counterexample, or a formal-kernel certificate.

[Additive prior-status erratum](physics-1-rank2-dual-equivalence-and-core-gram-conditional-parent-v1-erratum-1.md) makes the new falsification operative alongside the earlier conditional disposition; the old historical 'open' wording is not silently treated as current. All held episodes AND all consumers remain NONINPUT. No original-target, q3/T3, global distillability, source equivalence, novelty, independent-family/human or kernel acceptance is claimed.
