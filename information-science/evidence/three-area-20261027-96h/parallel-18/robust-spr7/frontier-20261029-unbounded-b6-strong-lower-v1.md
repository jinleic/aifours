# A stronger quadratic lower bound and asymptotic bracket

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel exact symbolic replay; not parent adoption.** For the already-solvable, full-width stable boxes \(K_R\) in `frontier-20261029-unbounded-common-numerator-b6-obstruction-v1.md` (SHA-256 `71896c927bafabc2098ab283bc6108a7b259bda028dc58c948cffb637106f8c7`), every common numerator satisfies the stronger bound
\[
\boxed{\quad b_6>\frac7{80}R^2b_7\quad(R\ge5000).\quad}
\]
The explicit common monic numerator from the predecessor obeys \((b_R)_6<R^2/5\), independently checked in `frontier-20261029-unbounded-b6-matching-order-v1.md` (SHA-256 `5823954bedc1630266fd89267f46f05c08fbb0b331b57ff444037c6d5faa5966`). Hence the attained coefficient is within a factor \(16/7\) of the universal lower bound for all such \(R\).

Let \(m_6(R)\) be the infimum of \(b_6\) over all common monic numerators. Nonemptiness is given by the predecessor's explicit construction. The stronger five-atom functional below has \(-C_7/(R^2C_6)\to8/91\), so
\[
\frac8{91}\le\liminf_{R\to\infty}\frac{m_6(R)}{R^2}
\le\limsup_{R\to\infty}\frac{m_6(R)}{R^2}\le\frac{1317}{8425}.
\]
No existence of a limiting optimum or equality of the two constants is claimed.

## Certificate

Use the same first four actual corner/frequency atoms and cofactor construction as in the predecessor, but replace the fifth squared frequency by \(\tfrac{14}{25}L=\tfrac{14}{125}R^2\). The five signed cofactors are strictly positive for all real \(R\ge5000\). Their aggregate has
\[
C_1=C_2=C_3=C_5=0,\quad C_0,C_4<0,\quad C_6>0,\quad
C_7+\frac7{80}R^2C_6<0.
\]
Every common numerator is Hurwitz with strictly positive coefficients, and its positive weighted atom sum gives the bound exactly as in the predecessor. The independently checked symbolic data have positive leading coefficients \(C_6\sim cR^{26}\) and \(-(C_7+\tfrac7{80}R^2C_6)\sim sR^{28}\), with
\[
\frac7{80}+\frac{s}{c}=\frac8{91},
\]
which yields the infimum's lower asymptotic bound. The numerator upper asymptote \(1317/8425\) is separately checked in the matching-order packet. The open-neighborhood argument of `frontier-20261029-unbounded-b6-open-neighborhood-addendum-v1.md` also applies shape by shape to this strictly signed alternative atom functional, without changing the claimed anchor constants.

The exact shifted sign table `frontier-20261029-unbounded-b6-strong-lower-frozen-v1.json`, SHA-256 `4f439af0c7f7645ce5241731636fba1d4892280559274d09eddeecd1e2962d48`, records nine Laurent polynomials after factoring a positive power of \(R\) and setting \(R=5000+u\). The checker `frontier-20261029-unbounded-b6-strong-lower-independent-kernel-v1.py`, SHA-256 `0f20b7ff3f869bd61c7ad8d1b90a6ccf6d261edda3eb57a4e00e4074be207efe`, reconstructs the changed atoms from pinned independent geometry and verifies all 424 shifted coefficients strictly positive; receipt `frontier-20261029-unbounded-b6-strong-lower-independent-result-v1.json`, SHA-256 `22daca24901ca45e769517e3d51d47e9553a932eb8978a7ef6f34a828bf41097`. The exact leading-term ratio has a separate checker `frontier-20261029-unbounded-b6-strong-asymptote-independent-kernel-v1.py`, SHA-256 `6a66fa361ce182b1788a2f3fd548026018d4c965d115410e0b29cedd5e26c847`.

All finite arithmetic uses exact `fractions.Fraction` in one Python Eval host. The infimum and limit deductions are written mathematics. The exact optimal constant, formal proof, cross-vendor review, novelty clearance and the original arbitrary-box verdict remain open.
