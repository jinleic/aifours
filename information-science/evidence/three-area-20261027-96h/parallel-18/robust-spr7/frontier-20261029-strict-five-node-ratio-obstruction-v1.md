# A quantitative ratio barrier for five-node strict certificates

**Status: WRITTEN theorem candidate with WRITTEN-checked-in-kernel finite sign classification; not parent adoption.** This strengthens the direct strict-negative-coordinate certificate obstruction in `frontier-20261029-strict-negative-certificate-two-band-obstruction-v1.md` (SHA-256 `33cce85c5451984a670de2ae05c921ea3a61d0c88c867c3c81a1bb94cd026783`). It adds inequalities on the **actual averaged parity evaluations**, not merely a frequency count or a zero-certificate reformulation.

Under the same hypotheses, suppose a positive-weight atom sum has all eight numerator-monomial coefficients strictly negative and has exactly five distinct positive squared frequencies \(t_1<\cdots<t_5\) after averaging repeated-node actual denominators. The cited theorem gives exactly three possible phase-class sequences. At every mixed-sign node define the extended nonnegative ratio
\[
r_i=\frac{t_i|O_{a_i}(t_i)|}{|E_{a_i}(t_i)|},
\]
using \(+\infty\) if the even part is zero and 0 if the odd part is zero. They cannot both be zero because \(a_i\) is Hurwitz. Then the following **strict** chains are necessary:

| Phase classes | Necessary quantitative condition |
|---|---|
| \((2,1,3,2,4)\) | \(r_2>r_3\) |
| \((2,1,3,5,4)\) | \(r_2>r_3>r_4\) |
| \((2,4,3,5,4)\) | \(r_3>r_4\) |

The comparison uses the usual order on \([0,+\infty]\). For these particular classes, the lower-bound ratio in each comparison is always strictly positive or \(+\infty\), and the upper-bound ratio is always finite or 0; the nonzero alternating subsequences established by the cited theorem give this even at a parity-root sample. Hence equality of two infinities or of two zeros cannot occur in the displayed comparisons.

## Positive-polynomial test

Choose three of the five positive nodes as zeros and let
\[
b_\gamma(s)=(s+\gamma)\prod_{j\in J}(s^2+t_j),\qquad \gamma>0,\quad |J|=3.
\]
It has degree seven and **all eight coefficients strictly positive**, even though it has imaginary-axis roots and is used only as a linear test polynomial, not as a common numerator. At a selected node,
\[
P_{a_i,b_\gamma}(t_i)=
\prod_{j\in J}(t_j-t_i)\,[\gamma E_{a_i}(t_i)+t_iO_{a_i}(t_i)].
\]
The three nodes in \(J\) contribute 0. A zero-frequency atom, if present, contributes \(a_0b_0>0\); an infinity atom contributes \(b_7=1>0\). But an all-strictly-negative aggregate coefficient vector dotted with this positive-coefficient \(b_\gamma\) is strictly negative. Therefore no choice of \(J,\gamma\) can make the other two node contributions both nonnegative.

For \((2,1,3,2,4)\), choose \(J=\{1,4,5\}\). The two remaining mixed-sign terms are both nonnegative whenever \(r_2\le\gamma\le r_3\), so necessarily \(r_2>r_3\). For \((2,1,3,5,4)\), the same choice gives \(r_2>r_3\), and \(J=\{1,2,5\}\) gives \(r_3>r_4\). For \((2,4,3,5,4)\), \(J=\{1,2,5\}\) gives \(r_3>r_4\). When a relevant parity value vanishes, the extended-ratio convention makes the asserted inequality automatic unless a finite admissible interval of \(\gamma\) exists; that interval leads to the same contradiction. Equality also contradicts the strict-negative dot product, since all five finite-node contributions can then vanish.

The finite sign-choice checker examines all ten three-node zero sets in each of the three phase cases, including the above choices. It is `frontier-20261029-five-node-ratio-obstruction-independent-kernel-v1.py`, SHA-256 `ee194d2854ba8efa281571073ca40edcbeb2928fca63a52e18abd6a676a541a1`; receipt `frontier-20261029-five-node-ratio-obstruction-independent-result-v1.json`, SHA-256 `572f53b621eca3d9ae5a8c1de52a933cbd991cfc57f1d8ec2df06902eb1e4139`. The test-polynomial and root-side deductions are written mathematics; finite sign enumeration used integer arithmetic on one Python Eval host. These inequalities are necessary only. No five-node certificate, formal proof, cross-vendor review, novelty clearance, or arbitrary-box verdict is claimed.
