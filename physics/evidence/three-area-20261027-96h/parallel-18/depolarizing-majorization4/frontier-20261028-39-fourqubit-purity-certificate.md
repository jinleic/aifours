# Four-qubit exact purity invariants and a state-dependent k3 certificate

**Author-written all-pure-input identities and bounds; not a global majorization proof.** The stated sufficient condition may fail on actual inputs. It is derived below from Pauli orthogonality and Schmidt spectra, not from a previously held result; historical provenance/process records are not cured. No novelty, independent-family, human or formal acceptance is claimed.

## Exact identities and output purity

Let \(\rho=|\psi\rangle\langle\psi|\) be any pure four-qubit density. Let \(r_i\) be the Bloch length of its \(i\)-th single-qubit marginal, and put
\[
 S=\sum_{i=1}^4r_i^2,\qquad
 C=\left|\langle\psi|\sigma_y^{\otimes4}\overline\psi\rangle\right|^2.
\]
For \(k=0,\ldots,4\), define the actual Pauli-weight enumerator
\[
 A_k=\sum_{\operatorname{wt}(w)=k}\left(\operatorname{Tr}\rho\sigma_w\right)^2,
\quad\sigma_w\in\{I,X,Y,Z\}^{\otimes4}.
\]
All coefficients are real because \(\rho,\sigma_w\) are Hermitian. The exact identities are
\[
(A_0,A_1,A_2,A_3,A_4)
=(1,S,\ 2+S+4C,\ 8-8C-S,\ 5-S+4C).\tag{1}
\]
In particular these impose the actual-input restrictions \(S\le8(1-C)\) and \(A_4\ge0\); they are not arbitrary assignments of Pauli coefficients.

For the physical local depolarizing channel, set \(t=|1-p|\in[0,1]\). Its Pauli eigenvalue on weight \(k\) is \((1-p)^k\), so its actual output \(\sigma=\Lambda_p(\rho)\) obeys
\[
\operatorname{Tr}\sigma^2=\frac{1+Q(t,S,C)}{16},
\quad Q=\sum_{k=1}^4t^{2k}A_k.\tag{2}
\]
This is an equality for the same pure input, including complex phases and the negative-shrink physical interval.

Moreover \(4C\le4-S\), and with \(z=t^2\) one obtains the explicit quantitative comparison to a pure-product reference:
\[
\begin{aligned}
16\bigl(\operatorname{Tr}\sigma_*^2-\operatorname{Tr}\sigma^2\bigr)
&=z(1-z)\left[(4-S)(1+z)^2-4Cz(1-z)\right]\\
&\ge z(1-z)(4-S)(1+z+2z^2)\ge0.\tag{3}
\end{aligned}
\]
The inequality is tight for every generalized GHZ input \(\sqrt a|0000\rangle+e^{i\theta}\sqrt{1-a}|1111\rangle\): all \(r_i=|2a-1|\) and \(C=1-r_i^2\). It gives a purity statement, not an assertion of original spectral majorization.

## Same-projector k3 upper bound

For any actual rank-three orthogonal projector \(P\), Hilbert–Schmidt Cauchy–Schwarz gives
\[
\begin{aligned}
\operatorname{Tr}(P\sigma)
&=\frac3{16}+\operatorname{Tr}\!\left[\left(P-\frac3{16}I\right)\left(\sigma-\frac1{16}I\right)\right]\\
&\le \frac{3+\sqrt{39Q(t,S,C)}}{16},
\end{aligned}\tag{4}
\]
because \(\operatorname{Tr}(P-3I/16)^2=39/16\) and \(\operatorname{Tr}(\sigma-I/16)^2=Q/16\). The projector is one original actual complex projector, not an independent marginal optimizer. Taking the maximum over such \(P\) yields the same Ky-Fan-3 bound.

The product-reference top3 is \(R_3(p)=[3+8t+6t^2-t^4]/16\). For \(t>0\), a sufficient condition for the original k3 inequality is therefore
\[
39\Bigl[S+t^2(2+S+4C)+t^4(8-8C-S)+t^6(5-S+4C)\Bigr]
\le(8+6t-t^3)^2.\tag{5}
\]
A strict inequality gives a strict original gap. At \(t=0\) the channel output is exactly \(I/16\), so the bound holds by equality without dividing by \(t\). For a fixed \(p\), the same non-strict conclusion extends by the **same-P affine argument** to convex combinations of pure states satisfying (5); a uniform strict gap on a closed convex hull requires a common positive margin. This is not a condition on arbitrary mixed-state marginals or a proof for pure states failing (5).

## Derivation of the invariants

Pauli orthogonality gives \(\sum_{k=0}^4A_k=16\operatorname{Tr}\rho^2=16\) and \(A_0=1,A_1=S\). The local spin-flip \(X\mapsto YX^TY\) changes the sign of each nonidentity Pauli; hence
\[
16C=A_0-A_1+A_2-A_3+A_4,\quad A_1+A_3=8(1-C).\tag{6}
\]
For each pure 1|3 bipartition, the reduced purities of the one site and complementary triple agree. Summing over all four sites and expanding in their Pauli bases gives
\[
\frac{4+A_1}{2}=\frac{4+3A_1+2A_2+A_3}{8},
\qquad 12+A_1=2A_2+A_3.\tag{7}
\]
Equations (6), (7), \(A_1=S\) and total sum16 give all entries of (1).

For \(4C\le4-S\), use any one-versus-three Schmidt decomposition \(|\psi\rangle=\sqrt a|0u\rangle+\sqrt{1-a}|1v\rangle\), after a local basis change. Spin-flip overlap magnitude is unchanged by local unitaries up to a phase, since \(Y\overline UY\) is a unit-modulus scalar times \(U\) for each qubit. The two terms contributing to \(\langle\psi|\widetilde\psi\rangle\) each have modulus at most \(\sqrt{a(1-a)}\), because the complementary three-qubit spin-flip is antiunitary. Thus \(C\le4a(1-a)=1-r_i^2\) for every \(i\); summing the four inequalities yields \(4C\le4-S\). Expanding the product purity \((1+t^2)^4/16\) minus (2), and factoring, gives (3).

## A concrete stronger-region check target

For the four-qubit W state, \(S=1,C=0\). At \(p=1/2\), \(t=1/2\), equation (2) gives \(Q=9/16\). Bound (4) is \((12+3\sqrt{39})/64\), strictly below the product reference \(135/256\), with certified gap
\[
 (87-12\sqrt{39})/256>0.
\]
The preceding anisotropic/spin-flip bound was negative at this same input and parameter; the comparison is a certificate-strength observation, not a novelty claim or a global solution. Exact original-channel and same-projector consistency checks are reported separately if run. The general all-variable residual remains open.
