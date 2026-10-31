# Every four-qubit density has a state-dependent k3 noise neighborhood

**Author-written consequence of the common-projector bound; not a uniform all-state interval and not the full original problem.** No independent-family/human/formal review or novelty clearance has occurred, and historical held outputs are not accepted as premises.

## Exact quantifiers and explicit threshold

For every actual four-qubit density \(\rho\), choose **one finite spectral decomposition**
\[
 \rho=\sum_{j=1}^m w_j|\psi_j\rangle\langle\psi_j|,
 \qquad w_j>0,\quad \sum_jw_j=1,\quad m\le16.
\]
For each non-product pure \(\psi_j\), let \(r_{j,1}\le\cdots\le r_{j,4}\) be its local Bloch radii and define
\[
 S_j=\sum_i r_{j,i}^2,\quad L_j=r_{j,1}+r_{j,2}+3r_{j,3}+3r_{j,4},
 \quad \delta_j=8-L_j>0,\quad K_j=\sqrt{39(15-S_j)}-5>0.
\]
Let \(J\) be the non-product indices. If \(J\ne\varnothing\), put
\[
 \epsilon(\rho;\{\psi_j\})=
 \min\!\left\{1,\min_{j\in J}\frac{\delta_j}{2K_j}\right\}>0,
 \qquad D=\sum_{j\in J}w_j\delta_j>0.
\]
For every physical \(p\in[0,4/3]\), every actual complex rank-three projector \(P\), and \(0<t:=|1-p|\le\epsilon\),
\[
 R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]\ge\frac{tD}{32}>0.\tag{A}
\]
Consequently the original output Ky-Fan-3 sum is strictly less than the product-reference sum on that state-dependent punctured noise neighborhood. At \(t=0\) all inputs yield the identical maximally mixed output.

If \(J=\varnothing\), the selected spectral decomposition is a mixture of product pure states; the non-strict original k3 inequality holds at **every** physical p, so one may take \(\epsilon=1\). This case does not assert strictness of a mixture. The threshold may depend on the chosen eigenbasis in a degenerate eigenspace and is not claimed canonical.

The exact logical statement is **\(\forall\rho\;\exists\epsilon(\rho)>0\)**. It is not \(\exists\epsilon>0\;\forall\rho\): as a non-product component approaches a product state, the displayed lower bound for epsilon can approach zero. No uniform all-input interval or unrestricted-p original k3 result is inferred.

## Proof

The predecessor `frontier-20261028-42-firstorder-common-projector.md` proves, by Pauli expansion and a single actual \(P\), that for each pure input
\[
 16\bigl(R_3(p)-\operatorname{Tr}[P\Lambda_p(|\psi_j\rangle\langle\psi_j|)]\bigr)
 \ge t\bigl[(8-L_j)-tK_j\bigr].\tag{B}
\]
Here the proof handles \(1-p<0\) by the explicit four-site transpose/spin-flip mirror and does not optimize separate projectors for different terms. For a non-product pure input, not all local radii are1, so \(L_j<8\). If \(t\le\delta_j/(2K_j)\), the bracket in (B) is at least \(\delta_j/2\), giving a common-P gap \(t\delta_j/32\). The denominator is positive because \(S_j\le4\).

For a product pure input, all such inputs give the same output spectrum as the reference by local unitary covariance. Therefore \(\operatorname{Tr}(P\Lambda_p(\rho_j))\le R_3(p)\) for **the same arbitrarily fixed P**. Combining the finitely many estimates with weights \(w_j\), and using linearity of \(\Lambda_p\) and trace, gives (A). Because the inequality holds for every actual rank-three P with the same D, the finite-dimensional Ky-Fan variational principle gives the spectrum statement. The case with no non-product eigenvectors follows by the same affine argument at all p. Continuity or direct evaluation covers \(t=0\).

Only the pure-state bound in the named predecessor and elementary finite-dimensional spectral/convex facts are used. This is an all-density **statewise local** statement, not a substitute for proving the original k3 inequality at arbitrary input/parameter.
