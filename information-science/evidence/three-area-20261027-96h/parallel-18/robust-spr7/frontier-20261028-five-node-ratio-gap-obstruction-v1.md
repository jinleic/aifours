# An analytic ratio-gap obstruction to five-frequency certificates

**Status: WRITTEN candidate, with one WRITTEN-checked-in-kernel example; author result, not parent adoption.** For any robustly Hurwitz-stable monic septic interval box satisfying three explicit endpoint root-ratio inequalities, **no strict negative-coordinate atom certificate can use fewer than six distinct positive finite frequencies**, even if zero or infinity atoms are also allowed. This is a genuine conditional obstruction to the original certificate route, not a universal no-go theorem and not a positive synthesis proof.

The proof imports the unreviewed necessary three-word classification in `frontier-20261028-strict-cone-five-node-phase-barrier-v1.md`, SHA-256 `e747866fd95da2b1dfcae66eecfebb157a23a4c2bd602db9fb5b7707d89cfd68`, the endpoint-root order in `frontier-20261028-universal-endpoint-root-order-v1.md`, SHA-256 `d34963e7e341aa5e9839d76f44f6cb3c3b08ce0ad9d0891ec7608e000c671bc3`, and classical Hermite–Biehler interlacing. If either parity group is fixed, the separate fixed-parity theorem already excludes all such certificates; below assume both endpoint pairs are distinct.

## The three tests

Write the four actual parity endpoints as \(E_\pm,O_\pm\), and their ordered positive roots as \(e_i^\pm,o_i^\pm\). The imported universal order gives the strict chain
\[
0<e_1^-<e_1^+<o_1^-<o_1^+
<e_2^+<e_2^-<o_2^+<o_2^-<e_3^-<e_3^+<o_3^-<o_3^+.
\]
Define \(R_{\sigma\tau}(t)=-tO_\tau(t)/E_\sigma(t)\) wherever the denominator is nonzero, and the four positive endpoint values
\[
U_1=R_{++}(o_1^-),\qquad L_2=R_{++}(e_2^-),\qquad
U_2=R_{--}(o_2^+),\qquad L_3=R_{--}(e_3^+).
\]
If
\[
\boxed{\quad U_1\le L_2,\qquad U_1\le L_3,\qquad U_2\le L_3,\quad}
\]
then every strict negative-coordinate certificate needs at least six distinct positive finite squared frequencies. No conclusion is asserted for six or more frequencies, non-strict coordinate certificates, or boxes that fail these tests.

For a fixed stable corner, \(h(t)=tO(t)/E(t)\) is strictly increasing between consecutive \(E\)-roots. Indeed, writing \(E(t)=-a_6\prod_i(t-e_i)\), interlacing gives
\[
\frac{O(t)}{E(t)}=\frac1{a_6}-\sum_i\frac{c_i}{t-e_i},\qquad c_i>0,
\quad\text{so}\quad
h'(t)=\frac1{a_6}+\sum_i\frac{c_ie_i}{(t-e_i)^2}>0.
\]
Thus each \(R=-h\) is decreasing on every relevant root band. The endpoint tests can be certified by rational exterior brackets and rational evaluations; the example below does so without assuming algebraic roots are rational.

## Why the tests exclude the three five-node words

Merge equal positive frequencies by averaging their actual denominator coefficients, preserving membership in the same independent box. For strict negative coefficient sums, the even moments \(M_j=\sum_i\lambda_iE_i t_i^j\) and odd moments \(N_j=\sum_i\lambda_i t_iO_i t_i^j\), \(j=0,\ldots,3\), have signs \((-,+,-,+)\). Any zero or infinity atom only strengthens the endpoint inequalities, as in the imported phase proof. Therefore, for every cubic \(Q(t)=\prod_{r=1}^3(s_r-t)\) with positive roots,
\[
\sum_i\lambda_iE_iQ(t_i)<0,\qquad
\sum_i\lambda_i t_iO_iQ(t_i)<0.
\]
Suppose exactly five positive nodes occur. Strictness permits an arbitrarily small actual-member perturbation at a fixed node to remove a zero \(E_i\) or \(O_i\): both parity endpoint gaps are positive at positive \(t\). The imported classification then leaves only the following strict sign patterns, in node order:
\[
\begin{array}{c|ccccc}
A&--&-+&+-&--&++\\
B&--&-+&+-&-+&++\\
C&--&++&+-&-+&++
\end{array}
\]
In \(A\), nodes 1–2 lie in \(J_1=[o_1^-,o_1^+]\) and nodes 3–4 in \(I_2=[e_2^+,e_2^-]\). In \(B\), nodes 1–2 lie in \(J_1\) and nodes 4–5 in \(I_3=[e_3^-,e_3^+]\). In \(C\), nodes 2–3 lie in \(J_2=[o_2^+,o_2^-]\) and nodes 4–5 in \(I_3\). These are necessary placements, not existence assertions.

At any node with opposite signs put \(r_i=t_i|O_i|/|E_i|>0\). In \(A\) and \(B\), choose \(Q=(t_1-t)(t_4-t)(t_5-t)\). At nodes 2 and 3 both values of \(Q\) are negative; the two strict moment inequalities, with signs \(-+\) and \(+-\), imply \(r_2>r_3\). In \(B\) and \(C\), choose \(Q=(t_1-t)(t_2-t)(t_5-t)\). At nodes 3 and 4 both values are positive; their signs \(+-\) and \(-+\) imply \(r_3>r_4\).

Pointwise endpoint ordering and the monotonicity above give the necessary bounds
\[
\begin{array}{ll}
A:&r_2\le U_1,\quad r_3\ge L_2;\\
B:&r_2\le U_1,\quad r_4\ge L_3;\\
C:&r_3\le U_2,\quad r_4\ge L_3.
\end{array}
\]
For instance, in \(J_1\), \(E_+<0\) and \(O_+>0\); maximizing \(tO/(-E)\) uses \((E_+,O_+)\), and decreasing \(R_{++}\) bounds it by \(U_1\). In \(I_2\), the positive \(E\), negative \(O\) ratio is bounded below by \(R_{++}\) and then \(L_2\). The \(J_2,I_3\) bounds use \((E_-,O_-)\) analogously. The three displayed tests contradict, respectively, \(r_2>r_3\), \(r_2>r_3>r_4\), and \(r_3>r_4\). The imported phase theorem already excludes four or fewer nodes, completing the conditional result.

## A broad exact example

Let each of the seven coefficients of \((s+1)^7\) independently vary by \(9/10\), retaining the monic leading coefficient. The independent replay verified all 28 strict corner Hurwitz determinants and rational root brackets for the four endpoint values. The exterior rational evaluation points
\[
(p_1,p_2,p_3,p_4)=\left(\tfrac9{50},\tfrac{39}{50},\tfrac{69}{50},\tfrac{132}{25}\right)
\]
give conservative bounds \(U_1<\widehat U_1,\ L_2>\widehat L_2,\ U_2<\widehat U_2,\ L_3>\widehat L_3\), where
\[
(\widehat U_1,\widehat L_2,\widehat U_2,\widehat L_3)=
\left(\frac{2773944}{3690095},\frac{28511886}{32304955},
\frac{67202826}{87851695},\frac{947536788}{256048735}\right).
\]
All three required comparisons are strict. This establishes a nonvacuous, full-width example of the conditional obstruction; it does not use a putative certificate as an input.

Frozen endpoints, brackets and values: `frontier-20261028-five-node-ratio-gap-example-frozen-v1.json`, SHA-256 `b1e9c982ce2d535ab1e4293dec6c3b59eb0edf261dcba0e5dfaa9c1b047b01ad`. Independent sign/minor checker `frontier-20261028-five-node-ratio-gap-example-independent-kernel-v1.py`, SHA-256 `ad1b8bdb7963198819f758735dc00a9c8904fdb7ff65ea0dd42601ecfb25126e`; receipt `frontier-20261028-five-node-ratio-gap-example-independent-result-v1.json`, SHA-256 `843a874058832d22a1e8ad281ff9387aff07b87becce69ee87301d7241330c20`.

The ratio proof and its named prerequisites are written mathematics, not formally checked or parent-adopted. The finite example used exact integers and `fractions.Fraction` on one Python Eval host; no cross-vendor review, novelty clearance, all-support no-go result, or arbitrary-box verdict is claimed.
