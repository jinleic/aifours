# Scale-invariant distance from the parity-endpoint span

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** For the explicit strictly stable box in `frontier-20261028-actual-endpoint-span-open-obstruction-v1.md`, every common SPR numerator \(b\) satisfies the quantitative, scale-invariant bound
\[
\boxed{\quad\operatorname{dist}_\infty(b,\mathcal L_K)>10^{-7}\,\|b\|_\infty,\quad}
\]
where coefficients are taken in the monomial basis, \(\mathcal L_K\) is the real span of the four actual parity endpoint polynomials, and the norm is the coefficient \(\ell_\infty\) norm. An unrestricted common numerator exists. This strengthens the particular-box real-span obstruction; it does not rule out unrestricted numerators or claim the same numerical bound for other boxes.

## Exact finite-atom proof

Use the five positive atoms and their exact span annihilator from the referenced packet. Let \(r_i\in\mathbb R^8\) be the monomial pairing row of atom \(i\), \(\lambda_i>0\) its weight, \(B_i=\|r_i\|_1\), and \(W=\sum_i\lambda_iB_i\). Let \(G\) be the \(8\times4\) coefficient matrix of the endpoint generators, and let \(A\) be the \(4\times4\) matrix formed by the first four atom rows times \(G\). Its determinant is nonzero. Define
\[
H=GA^{-1},\qquad
L=\max_{0\le j\le7}\sum_{i=1}^4|H_{ji}|\,W/\lambda_i.
\]
The independent rational replay checked the inverse and the exact strict inequality \(1/(1+L)>10^{-7}\); its full rational values are in the frozen record.

Take any common \(b\), any \(v\in\mathcal L_K\), and \(d=\|b-v\|_\infty\). Each actual atom pairing \(r_i\cdot b\) is strictly positive, so
\[
r_i\cdot v>-dB_i.
\]
Because \(\sum_i\lambda_i r_i\) annihilates the entire endpoint span, the weighted sum of \(r_i\cdot v\) is zero. The lower bounds on the other four terms therefore give \(|r_i\cdot v|<dW/\lambda_i\). Inverting the selected four rows yields \(\|v\|_\infty<Ld\), and hence
\[
\|b\|_\infty\le\|v\|_\infty+d<(L+1)d.
\]
The nearest point in the finite-dimensional closed subspace exists, so taking it as \(v\) proves the displayed strict bound. This uses the actual five atoms and exact rank, not a coefficientwise artificial hull.

Frozen rational constants and source pins: `frontier-20261028-endpoint-span-relative-separation-frozen-v1.json`, SHA-256 `cb9315ee6c4e20c2cfbfe29425e0deaca916be35701326d3f36d71792d4ac800`. Independent checker `frontier-20261028-endpoint-span-relative-separation-independent-kernel-v1.py`, SHA-256 `e53f9489bbe6f934dd351394527cb955da53dd0036f0c0298de4057807703d0a`; receipt `frontier-20261028-endpoint-span-relative-separation-independent-result-v1.json`, SHA-256 `0eacc55b6b50a69d867cbfc63ef7fec2cf37c21b0369f96b8c741f206770d4dd`. The referenced span theorem is SHA-256 `3585b869050db122937d3e441923e8adfc19fb61ff1bf31e279e3afdc62e530d`.

All finite identities use exact integers and `fractions.Fraction` on one Python Eval host; the norm estimate is written mathematics. No formal proof, cross-vendor review, novelty clearance, arbitrary-box conclusion, or unrestricted negative certificate is claimed.
