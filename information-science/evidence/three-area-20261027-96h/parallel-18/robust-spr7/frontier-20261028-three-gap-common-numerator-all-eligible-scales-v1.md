# One exact numerator for every eligible box in the three-contact family

**Status: WRITTEN-checked-in-kernel; author candidate, not a parent adoption.** This successor resolves the previously open numerator question for the particular anisotropic family in `frontier-20261028-three-gap-exact-stability-family-v1.md`. It is an all-frequency obstruction to negative atom certificates **for this family**, not a universal answer for arbitrary septic boxes.

## Theorem for the explicit family

Use the center \(a_0\), halfwidth vector \(h\), and boxes \(K_\rho\) from the preceding packet. That packet proves exactly that \(K_\rho\) is all-member strictly Hurwitz if and only if \(0\le\rho<1\), and that three actual imaginary-axis contacts occur at \(\rho=1\).

For **every** \(\rho\in[0,1)\), the same monic degree-seven numerator, with ascending coefficients

\[
\begin{aligned}
(b_0,\ldots,b_7)=\Big(&
\frac{235808526135635518311909}{1110164937620186658944000000},
\frac{924105209}{156250},
\frac{4810359389487773710367835421083}{2775412344050466647360000000},
\frac{3402160821}{2000000},\\
&\frac{195395555396483510563546185669}{1110164937620186658944000000},
\frac{233389579}{2500000},
\frac{26721033}{10000000},1\Big)
\end{aligned}
\]

satisfies \(\operatorname{Re}[b(i\omega)/a(i\omega)]>0\) for every \(a\in K_\rho\) and every real \(\omega\). In fact,

\[
\operatorname{Re}\frac{b(i\omega)}{a(i\omega)}\ge (1-\rho)
\frac{5721890736288781293044570759226854974970367}
 {3324213602412068148271294311052562729845016362378854400}>0.
\]

The lower bound need not be sharp and tends to zero at the excluded boundary.

## Exact boundary-to-interior proof

Let \(t=\omega^2\), \(P_{a,b}(t)=\operatorname{Re}[b(i\sqrt t)a(-i\sqrt t)]\), and order the four actual parity corners \((E_-,O_-),(E_-,O_+),(E_+,O_-),(E_+,O_+)\). At the singular boundary \(\rho=1\), the exact pairing polynomials have the form

\[
P_0=q_0,\quad P_1=(t-15)^2q_1,\quad
P_2=(t-3)^2(t-65)^2q_2,\quad P_3=q_3,
\]

where the four residual polynomials \(q_0,q_1,q_2,q_3\), of degrees 7, 5, 3, 7 respectively, are all strictly positive on \([0,\infty)\). The frozen certificate gives their coefficients and rational Bernstein leaves on the compactified half-line. An independently written replay reconstructs each full pairing from the square factors and residual, checks exact leaf coverage, and checks every residual Bernstein coefficient strictly positive. Thus all four boundary pairings are nonnegative; they are **not** asserted strictly positive at the three contacts.

For the center denominator \(a_0\), independent exact Bernstein replay yields

\[
\frac{P_{a_0,b}(t)}{(1+t)^7}\ge
\delta:=\frac{1562889663865007609374785180469783}
 {1043026709428502262095621914624000000}>0.
\]

Each actual corner at scale \(\rho\) is \((1-\rho)a_0+\rho a_{c,1}\); its pairing is the same affine combination of the center and boundary pairings. For any fixed \(t\), linearity in the independently varying coefficients makes the minimum over the entire box the minimum of the four actual corner pairings. Therefore

\[
\frac{P_{a,b}(t)}{(1+t)^7}\ge(1-\rho)\delta>0
\qquad (a\in K_\rho,\ t\ge0).
\]

Finally \(|a(i\sqrt t)|\le S_1(1+t)^{7/2}\), where \(S_1=1+\sum_{j=0}^{6}(a_{0,j}+h_j)=44631014096/1512675\). Combining the inequalities gives the displayed ratio bound. Strict Hurwitz stability of every member was established separately by the exact marker/root-band argument in the preceding packet, not inferred from the numerator search.

In particular, for any fixed \(0\le\rho<1\), no finite nonzero nonnegative combination of actual-corner finite-frequency pairing functionals and the infinity functional can have all eight coefficient sums nonpositive: dotting such a combination with the displayed positive coefficient vector \(b\) would be simultaneously positive and nonpositive. This includes and is stronger than the earlier *finite-grid-only* obstruction for \(K_{999/1000}\). It does not exclude a certificate for a different eligible box.

## Frozen evidence and checks

- Original family and exact marker/three-contact data: `frontier-20261028-three-gap-family-and-grid-frozen-v1.json`, SHA-256 `6984f81b8bd94ad5379195b393b2662cfc43ca48a0cf1287e2acf3135ff633a9`. Its scientific packet has SHA-256 `a2ccf835c53ee88e99d24e8bdc83ba6ab26e2dfde62a6e40bf7c2f38597f4fd3`.
- New exact numerator, boundary polynomials and square factors, all Bernstein leaves, center proof and ratio constant: `frontier-20261028-three-gap-universal-numerator-frozen-v1.json`, SHA-256 `6c89ae0515bfb0a8305e0fb8da487b61a629b9a3328a5a7529290d8315299f54`.
- Standalone checker `frontier-20261028-three-gap-universal-independent-replay-kernel-v1.py`, SHA-256 `753aa66b8eb39bd4cc6c3222f2ebb34d9c30debd22559a92c0107488700db4fd`. It independently reconstructs the center, marker signs, all three boundary contacts, all four pairing factorizations, every Bernstein coefficient by affine power substitution, center bound, and ratio constant. Boundary leaf counts are 11, 8, 6, 21; the center has 7. Corrupting a leaf coefficient or square-factor residual was rejected. Receipt `frontier-20261028-three-gap-universal-independent-replay-result-v1.json`, SHA-256 `d08e72069124631f93032f6764caf51ce2e7152804c71839185d8733813f5f2a`.
- Search used exact boundary tangent equalities, physically realizable rational nodes, an interior-seeking exact LP, then exact rounding with all three tangencies solved as equalities. The final rounding producer `frontier-20261028-three-gap-universal-numerator-rounding-kernel-v1.py` has SHA-256 `0181639de78e7fb6122a768d08e227ab31729bffe73a8a7c7be68d24cb3c495d`. Its first invocation encountered a keyword-name `TypeError`; the call was corrected and resumed at the failed step. The accepted candidate was replayed from frozen bytes by the standalone checker above.

Imports are elementary polynomial factorization, interval linearity, Bernstein positivity, and the sign-band/homotopy stability proof. All machine arithmetic was integer/`fractions.Fraction` in one Python Eval host. This is not formal verification, cross-vendor review, novelty clearance, or a resolution of the original arbitrary-box decision.
