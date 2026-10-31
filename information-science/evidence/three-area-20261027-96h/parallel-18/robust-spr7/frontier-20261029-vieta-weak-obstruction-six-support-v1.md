# Weak original-box obstructions need two odd circuits and six locations

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 15:57:30 PDT 2026**. **WRITTEN theorem candidate**, with only the stated finite phase-class enumeration WRITTEN-checked-in-kernel; not independently reviewed, parent-adopted, formally verified or novelty-cleared. This is a necessary condition on an exact original-box no-go certificate, not a universal synthesis verdict.

## 1. Import and statement

Use the original eligible monic septic box, compactified rows, ordered odd bands and eight Vieta vertices of `frontier-20261029-eight-atom-vieta-alternative-v1.md`, SHA-256 `f107da4124a5a1b4516d1e9aeb7bde2ddbcc341367d869fe0916a1407da09e10`. In particular its equation (3) is a necessary-and-sufficient **weak** no-synthesis certificate with at most eight actual corner atoms. We import that theorem candidate as written, not as an independently accepted fact. The arguments below also apply directly to any finite actual-member measure satisfying (3), irrespective of that alternative's validity.

Merge same-positive-frequency atoms by averaging the actual denominator coefficients using their nonnegative weights. This preserves every row, because it is linear in the denominator, and the average remains in the same stable box. Delete zero-weight atoms. Call a finite positive-frequency merged row **odd-zero** if its odd coordinate vector is zero. Zero-frequency rows are also odd-zero; infinity is not.

**Theorem.** For every finite positive-weight measure satisfying the weak obstruction inequalities (3), after merging and removing odd-zero rows:

1. A nonzero odd-canceling measure remains and still satisfies all eight nonpositive even-vertex inequalities.
2. There is a **backward crossing in an actual even-root band**: two distinct positive nodes \(t_i<t_j\) in one even-root band and actual members whose corresponding even roots obey \(e_i<t_i<t_j<e_j\).
3. There is a backward crossing in a separate odd-root band.
4. At least **six distinct locations** are required among the positive finite nodes and infinity: if infinity is absent, at least six positive finite nodes are necessary; if infinity is present, at least five positive finite nodes are necessary. Zero-frequency and odd-zero rows cannot lower these bounds.
5. The nonzero odd-canceling measure is not a single extreme positive odd-moment circuit. It requires at least two such circuits, even though each circuit separately has an even-root-gap test numerator with positive even pairing.

All root equalities are handled below; the two reversed crossings in items 2–3 have strict signs on their respective parity components. They are necessary, not claimed sufficient. The six-location bound is for this weak projected certificate **on the original box**, including possible infinity atoms. It is not a lower bound on an unrelated certificate format.

## 2. Why zero-odd rows can be removed

Every actual member's even roots lie respectively in the open root gaps
\[
I_1=(0,\underline o_1),\quad I_2=(\overline o_1,\underline o_2),\quad I_3=(\overline o_2,\underline o_3). \tag{4}
\]
For every vertex polynomial \(F_\nu\) from the import, all its roots lie in the corresponding *closed* gaps. Hence, at an actual zero of \(O_a\), \(E_aF_\nu\ge0\): the signs agree on each odd band and a vertex factor may only vanish at its endpoint. At \(t=0\), the corresponding vertex pairing is \(a_0F_\nu(0)\ge0\). Thus deleting any odd-zero row preserves odd cancellation and can only decrease each of the eight vertex sums.

The residual cannot be empty: choose any roots strictly inside all three gaps, obtaining \(e\in\mathcal P_K\). Every odd-zero finite/zero row has a **strictly positive** even pairing with that \(F_e\), since the actual denominator is stable. Its Vieta vector is a convex combination of the eight vertices, so an all-odd-zero measure cannot satisfy all eight nonpositive inequalities. An infinity-only remainder is impossible because its odd \(v_3\) coordinate is positive. Renormalize the remaining weights if desired.

## 3. Root alignment forces an even-band reversal

Fix any finite odd-canceling measure with no odd-zero rows. Suppose it has **no** strict backward even-root crossing. In gap \(I_j\), call a node *before* if \(t_i<e_j(a_i)\), and *after* if \(t_i>e_j(a_i)\); equality is unconstrained. No backward crossing means no after-node precedes a before-node. Consequently one can choose \(x_j\in I_j\) with \(x_j\ge t_i\) for all before-nodes and \(x_j\le t_i\) for all after-nodes. This remains possible when nodes share a frequency: a forced equality \(x_j=t_i\) is allowed. Because every actual root is strictly inside its gap, such an \(x_j\) is strictly inside the gap even when one side of the node set is empty.

Put \(F(t)=\prod_{j=1}^3(x_j-t)\), with even coefficient vector \(e=V(x)\). At each finite atom, \(E_{a_i}(t_i)F(t_i)\ge0\): inside a gap this is precisely the aligned before/after condition; outside the gaps all even parts and \(F\) have the same fixed sign. At zero the product is strictly positive; an infinity row has zero even part.

At least one finite product is **strictly** positive. Otherwise every finite atom lies in the three gaps: an atom at zero, in an odd band, or at/after the third odd band's lower endpoint would already have a strict product. Choose \(r_1,r_2\) in the first and second odd bands. Throughout \(I_1,I_2,I_3\), the sign of
\[
q(t)=(r_1-t)(r_2-t)
\]
coincides strictly with that of every actual \(O_a(t)\), respectively \(+,-,+\). Thus
\[
\sum_{0<t_i<\infty}\lambda_i\frac{t_iO_{a_i}(t_i)q(t_i)}{(1+t_i)^7}>0.
\]
But the left side is a fixed linear combination of the first three zero odd moments. The infinity atom contributes zero to these three moments, so the sum must be zero. There must be a positive finite atom because infinity alone cannot cancel itself. Contradiction.

Thus \(L_e(\sum\lambda_i u_i)>0\). As \(e\) is a convex combination of the eight Vieta vertices, at least one vertex pairing is strictly positive, contradicting (3). Hence every weak no-go measure has a strict backward even crossing. Both crossing nodes lie in the actual \(j\)-th even-root band, since their members' roots bracket them.

## 4. Odd circuits and the six-location floor

Let positive finite nodes be distinct after merging, and let
\[
d_i=\frac{t_iO_{a_i}(t_i)}{(1+t_i)^7}\ne0.
\]
The four odd equations say the finite signed weights \(w_i=\lambda_i d_i\) have
\[
\sum_iw_i t_i^r=0\quad(r=0,1,2),\qquad
\sum_iw_i t_i^3=\lambda_\infty. \tag{5}
\]
The normalized positive odd-canceling weights form a finite polytope. Each extreme point has support at most five because there are four homogeneous odd equalities plus normalization. For distinct nodes, Vandermonde rank rules out a nonzero circuit with fewer than five finite nodes if infinity is absent, or fewer than four finite nodes with infinity present.

With exactly five finite nodes and no infinity, Lagrange interpolation gives \(w_i=c/H_5'(t_i)\), \(H_5(t)=\prod_{j=1}^5(t-t_j)\). Thus the nonzero signs strictly alternate, in either orientation. With exactly four finite nodes and infinity, the first three moments give \(w_i=c/H_4'(t_i)\), while the fourth equation gives \(c=\lambda_\infty>0\); the four signs are specifically \((- ,+,-,+)\). These are the only nonzero extreme-circuit forms. Their strict alternating odd signs imply that no circuit can contain two nodes in a single even gap: \(O_a\) has one fixed nonzero sign throughout each gap, including for different actual members, and every intermediate ordered node between two points in that gap also lies in it. Therefore each circuit has no even reversal and, by §3, has some \(e\in\mathcal P_K\) with strictly positive even pairing.

A no-go measure cannot be just one such circuit. In particular, without infinity, at most five finite nodes leave at most one Vandermonde-null ray; with infinity, at most four finite nodes leave at most one. The no-go measure therefore needs at least six finite nodes without infinity, or at least five finite nodes plus infinity. It must combine at least two distinct extreme odd circuits. This completes items 4–5.

For item 3, at least one constituent extreme circuit exists. Its alternating odd signs include either five alternating signs for five finite nodes, or the oriented four signs \((- ,+,-,+)\) when infinity is present. Without a backward odd-root crossing, the number of passed odd-root bands is nondecreasing. Five alternating signs would require at least four odd sign changes, more than the three odd roots. The oriented four signs start negative, hence already require at least one passed odd root before three further sign changes, again at least four. Consequently that circuit has a backward odd-root crossing. It occurs in an odd band, disjoint from the even band in item 2, and survives in the original measure's support.

## 5. The minimal five-finite-plus-infinity case: twelve phase words

This section is a **finite necessary classification**, not an exclusion or existence result. Suppose the reduced certificate has exactly five positive finite nodes and a positive infinity atom. At a finite node define its phase class as the number \(q_i\in\{0,\ldots,6\}\) of ordered even/odd roots already passed. The possible nonzero sign pairs \((E,O)\) in classes 0 through 6 are
\[
(++),(-+),(--),(+-),(++),(-+),(--). \tag{6}
\]
If the even part vanishes, either adjacent class may be assigned; the odd part cannot vanish after the deletion in §2. Global disjoint root-band order gives \(q_i\le q_j+1\) for every \(i<j\). The infinity-containing extreme circuit gives an odd-sign subsequence \((- ,+,-,+)\). The two strict backward-band crossings force, respectively, a pair \(i<j\) with \(q_i=q_j+1\) and odd \(q_i\), and a pair with the same equality and even \(q_i\). These conditions leave exactly the following 12 class words:
\[
\begin{array}{llll}
(2,1,2,5,4)&(2,1,3,2,4)&(2,1,3,2,5)&(2,1,3,5,4)\\
(2,4,3,5,4)&(2,5,4,6,5)&(3,2,4,3,4)&(3,2,4,3,5)\\
(3,2,4,6,5)&(3,2,5,6,5)&(3,4,3,5,4)&(3,5,4,6,5).
\end{array} \tag{7}
\]
The **only machine-checked part** of this packet is this finite classification: on one Python Eval host, integer-only `itertools.product(range(7),repeat=5)` and `itertools.combinations` enumerated all \(7^5\) words and retained exactly those satisfying the pairwise order, odd subsequence, and both parity-specific reversed-pair predicates just stated. The printed result was 12, exactly the displayed list. This is a conservative overclassification when an even value is zero; it does not establish any word's algebraic realizability or rule out a certificate.

## 6. Exact one-parameter test at the six-location frontier

For fixed five distinct positive finite nodes, fixed actual members with nonzero \(d_i\), and an optional infinity atom, the odd-row matrix has rank four; with infinity included it has six columns and a two-dimensional kernel. Its intersection with the nonnegative orthant is pointed, so it has at most two extreme rays. The rays are explicit:

* A five-finite ray, when its signs permit it, has weights \(\lambda_i=c/[d_iH_5'(t_i)]>0\) and \(\lambda_\infty=0\).
* For each four-node subsequence with odd signs \((- ,+,-,+)\), an infinity ray has \(\lambda_i=1/[d_iH_4'(t_i)]>0\), zero on the omitted finite node, and \(\lambda_\infty=1\).

The interpolation identities in §4 show these are all the extreme rays. If only one exists, §4 already excludes a weak no-go. If two exist, write their eight Vieta even-pairing vectors \(g^A,g^B\). A no-go on exactly these nodes is possible **if and only if** there is an \(h>0\) such that
\[
g^A_\nu+h g^B_\nu\le0\quad(\nu=1,\ldots,8), \tag{8}
\]
with both extreme rays present. Equation (8) is just an explicit one-dimensional interval intersection: \(g^B_\nu>0\) imposes \(h\le-g^A_\nu/g^B_\nu\), \(g^B_\nu<0\) imposes \(h\ge-g^A_\nu/g^B_\nu\), and \(g^B_\nu=0\) requires \(g^A_\nu\le0\). If all five nodes and infinity must have strictly positive total weight, additionally require that the union of the two ray supports covers those six locations. These formulas remain exact at equality; they do not rely on floating point.

This is the next concrete representation: analyze the 12 class words against the actual independent coefficient-box geometry and the eight scalar interval constraints, or exhibit one eligible box and \(h\) satisfying them. Excluding this frontier would still leave certificates with six or more positive finite nodes, so it would **not** by itself prove universal synthesis.

## 7. Assurance boundary

The phase-class enumeration alone was checked with exact integer arithmetic in one Python Eval host. Root alignment, Vandermonde identities, positive-circuit decomposition and the one-parameter criterion are written deductions, not a formal proof or independent reconstruction. The proof imports compact root-band ordering and the eight-vertex formula from the named candidate, plus elementary interpolation and finite-dimensional polyhedral geometry. It does not import or classify held historical mathematics. Parent-classified incidental source-display exposure is disclosed in `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made. No original negative box, universal synthesis theorem, parent adoption, cross-vendor review or novelty clearance is claimed.
