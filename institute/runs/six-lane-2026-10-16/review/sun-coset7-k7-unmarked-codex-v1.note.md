All eight SHA256 hashes match. Only snapshot reads and hashing were used. The four requested implications have no substantive mathematical defect; two merit minor wording fixes. **K7 remains OPEN.** The accepted premises retain SOURCE05/SOURCE07’s exact scopes.

**Narrow P2 — ACCEPT.** This means precisely \(M=\varnothing\), Q23, and **at least two 2-classes**, without accepting BLOCK or PAIR wholesale.

Here is an independent verification of the needed dependency. Choose distinct twins \(j,k\) in a block \(B\), of size \(s\ge2\). TWIN and L6 give a fixed proper subgroup \(W=\langle U_j,U_k\rangle\), with \(m\mid6\) and \(t_v=m\alpha_{vB}/6\). Another 2-class supplies an \(\alpha=3\) vertex, forcing \(m\) even. If \(m=2\), integrality forces every other vertex’s \(\alpha\) to equal 3. All seven vertices then have \(t=1\), local indices \(n_i/2\), and pairwise gcd 3. Two \(W\)-cosets force four pieces together, contradicting Sun(4). Thus \(m=6\).

Block vertices now have local indices \(w_i\). Sun(2) makes their \(s\) occupied cosets distinct and exclusive. Outsiders have \(t=2\) or 3 and index \(tw_i\). Mixed types cannot share a coset; Sun(3)/Sun(4) bound their respective capacities by 2/3. If \(k_a\) vertices use \(c_a\) cosets, incidence counting gives \(ak_a\le ac_a\). Consequently
\[
7-s=k_2+k_3\le c_2+c_3\le6-s,
\]
a contradiction. This verifies the narrow implication without importing an unreviewed theorem.

**MINOR scope fix:** [SOURCE02:62](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-unmarked-review-v1/snapshot/02-K7-pair-lemma-v1.md:62) literally states unrestricted Q23, contrary to SOURCE04:70’s description. Insert “with at least two 2-classes”; P1’s proof does not cover single-class Q23.

**HIGH — AWF, MINOR presentation only.** For every admissible \(q\), positivity and \(\alpha\ge3\) give \(q_j\in\{1,2,3\}\). Unmarkedness gives \(d_j=q_jw_j\), hence exactly \(\gcd(d_j,d_k)=\gcd(q_j,q_k)\).

The hereditary allowed sets are exactly singletons, pure \(q=2\) subsets of size at most 2, and pure \(q=3\) subsets of size at most 3. Mixed pairs and pairs containing \(q=1\) fail Sun(2); oversized pure groups contain a forbidden triple or quadruple. This checks **every subset**, not merely the full six-neighbour set.

For each nonempty group use \(y_j=1/\min(q_j,k_{q_j})\). These weights are nonnegative and satisfy every allowed-set inequality. Its contribution is
\[
\frac{k_q q}{6\min(q,k_q)}\ge\frac{k_q}{6}.
\]
Thus the total is at least 1 for **every** admissible \(q\), contradicting VFC-count’s strictly \(<1\).

At [SOURCE00:29](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-unmarked-review-v1/snapshot/00-K7-unmarked-lemmas-v1.md:29), explicitly restrict reciprocal formulas to nonempty groups and add contribution 0 for absent groups. The current per-vertex assignment is vacuous when a group is absent, so this is no counterexample, but the table should state that convention.

**CLASS — AWF, MINOR quantifier clarification.** At [SOURCE00:46](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-unmarked-review-v1/snapshot/00-K7-unmarked-lemmas-v1.md:46), write “choose **distinct** \(j,k\in C\).”

For every \(v\notin C\), triangle \((v,j,k)\) has labels \((2,3,3)\). Its unmarked \(\tau_{\min}=6\), and L4 forces intersection measure \(1/2\), equal to both product measures. Therefore \(U_vU_j=U_vU_k\).

L6 yields \(m\mid6\), \(2/6\le1/m\), hence \(m\le3\), and \(m/2\in\mathbb Z\); therefore \(m=2\). Crucially, the generated \(W\) depends only on the fixed pair \(j,k\). Applying this to **every** outside apex gives \(U_v\subseteq W\) for every \(v\notin C\).

L5 then gives \(t\in\{1,2\}\), \(\lambda=3tw\), and pair gcd 3, except gcd 6 when both vertices have \(t=2\). The capacity arguments hold:

- \(c=2\): seven \(t=1\) vertices exceed capacity six.
- \(c=3\): six fixed \(t=1\) vertices fill the cosets \(3+3\); the remaining vertex either exceeds that capacity or meets both cosets and creates a forbidden four-set.
- \(c=4\): zero or one \(t=2\) vertices give the preceding contradictions. With two, both meet both cosets. Three \(t=1\) vertices together with either one form a forbidden four-subset, so only four such vertices fit, whereas five are required.

These are incidence arguments in left cosets; no normality assumption is needed.

**Q23U — ACCEPT at its stated scope.** [SOURCE00:80](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-unmarked-review-v1/snapshot/00-K7-unmarked-lemmas-v1.md:80) correctly combines narrow P2 and CLASS. With at least two classes summing to 7, exclusion of sizes 2, 3 and 4 forces a singleton: otherwise two classes already contribute at least 10. Its six incident labels are 3, so HIGH applies. No single-class conclusion follows.

The cumulative table needs explicit dependency labels. At [SOURCE00:97](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-unmarked-review-v1/snapshot/00-K7-unmarked-lemmas-v1.md:97), “only seven-singleton all-2 remains” is conditional on BLOCK’s larger-block exclusion and the **separate P3 argument extended to all-2**, not on narrow P2. Likewise, SOURCE00:98’s BLOCK/P3 constraints remain conditional; its HIGH neighbour constraint is proved here. Add all-2 to SOURCE00:5’s abbreviated remaining-case list.

No residual enumeration, complete failing-\(q\) list, or realizability conclusion is accepted. The displayed \(q\)-vector is not a global survival certificate. The verified arguments use only Sun(2)–Sun(4), within the accepted \(t\le6\) imports; no least-order frame, subgroup Sun(7), or FH certificate enters.