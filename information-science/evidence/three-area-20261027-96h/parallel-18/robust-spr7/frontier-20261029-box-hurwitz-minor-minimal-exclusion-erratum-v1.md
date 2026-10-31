# Erratum: the fixed shape in the box-minor exclusion is ineligible for every scale

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:12:48 PDT 2026**. This is an additive correction to `frontier-20261029-box-hurwitz-minor-minimal-exclusion-v1.md`, SHA-256 `0d1b72785b14ddfccec131091e73a3c4a74b463575e674bebce058ee80f7d325`. Its conditional implication and rational margin remain as written, but its hypothesis is **never satisfiable**: no all-Hurwitz independent coefficient box contains the five members at those exact root shapes, for any positive scales. Consequently that packet is a **vacuous exclusion**, not nonvacuous progress toward the eligible-box minimal obstruction. Do not use it as evidence that the second Hurwitz minor alone resolves any realizable configuration.

## Direct exact proof

Use only members 3 and 4, which have the same odd part
\[
O(t)=-(t-9/10)(t-9/2)(t-7).
\]
Let their positive even scales be \(L=\lambda_3\), \(H=\lambda_4\). Their respective middle even roots are 2 and \(16/5\), and their outer roots are \(1/2,5\). In ascending even coefficient order \((a_0,a_2,a_4,a_6)\), these members are
\[
L(5,27/2,15/2,1),\qquad H(8,201/10,87/10,1). \tag{1}
\]
An independent coefficient box containing both contains members obtained by mixing any four even coefficients from (1) while holding the shared odd part fixed. At the actual odd root \(t=9/2\), a Hurwitz septic necessarily has **positive** even part, by Hermite–Biehler interlacing. Two allowed mixes are
\[
A=(5L,(201/10)H,(15/2)L,L),\qquad
B=(5L,(27/2)L,(87/10)H,L). \tag{2}
\]
Their even evaluations at \(t=9/2\) are exactly
\[
E_A=\frac{263}{4}L-\frac{1809}{20}H,\qquad
E_B=-\frac{1175}{8}L+\frac{7047}{40}H. \tag{3}
\]
Stability of \(A\) requires \(H/L<1315/1809\); stability of \(B\) requires \(H/L>5875/7047\). But
\[
\frac{5875}{7047}-\frac{1315}{1809}=\frac{50410}{472149}>0. \tag{4}
\]
The requirements are incompatible. Each mix is an actual member of **any** independent coefficient box containing the two originals, so no choice of the other coefficients or scales repairs this obstruction. This argument is stronger than merely observing that the particular explicit example's hull is unstable: it covers every positive pair \((L,H)\) at the frozen root shapes.

The signs and identities in (3)–(4) were evaluated using integers and `fractions.Fraction` on one Python Eval host. Hermite–Biehler orientation and coefficient-box mixing are written deductions. This correction does not affect the separately stated stable parity-product countermechanism, which was explicitly ineligible, nor the general odd-circuit/Vieta alternatives. No independent review, formal proof, novelty clearance or original septic verdict is claimed. Process exposure remains disclosed in `owner-incidental-held-source-search-display-v1.json` (SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`).
