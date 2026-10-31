# Four-qubit depolarizing: exact physical-parameter mirror

**Scope:** Independently derived written proposition for the original four-qubit channel and all complex densities/projectors. It reduces the parameter domain; it does **not** prove the outstanding global \(k=3\) inequality or assert novelty. Earlier process/quarantine records remain historical and are not imported as mathematical premises. No held result is treated as established. Prior work already identified the actual common-projector gap; it is not filled here.

## Proposition

Let
\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I_2,
\quad \Lambda_p=\Phi_p^{\otimes4},\quad 0\le p\le 4/3.
\]
For every \(p\in[1,4/3]\), put \(p'=2-p\in[2/3,1]\) and \(U=\sigma_y^{\otimes4}\), where \(\sigma_y=\left(\begin{smallmatrix}0&-i\\ i&0\end{smallmatrix}\right)\). For every four-qubit operator \(X\),
\[
\Lambda_p(X)=U\,\Lambda_{p'}(X)^T U.
\]
The transpose is in the fixed tensor-product computational basis. Consequently, for every density \(\rho\), the ordered output spectra at \(p\) and \(p'\) are **identical**, not merely bounded; this holds for mixed, pure and genuinely entangled inputs. For every actual complex rank-three projector \(P\),
\[
\operatorname{Tr}\!\left[P\Lambda_p(\rho)\right]
 =\operatorname{Tr}\!\left[\widetilde P\Lambda_{p'}(\rho)\right],
\qquad \widetilde P=UP^T U.
\]
Here \(\widetilde P\) is an actual complex rank-three orthogonal projector and the map \(P\mapsto\widetilde P\) is a bijection. The same input \(\rho\) is used on both sides, and \(\widetilde P\) is deterministically generated from the single original \(P\), not a separately optimized or independently selected copy.

Therefore the original \(k=3\) claim for **all** physical \(p\in[0,4/3]\) and all four-qubit densities is equivalent to that claim for \(p\in[0,1]\), with the ordinary product reference on each side. The same equivalence holds for every Ky-Fan index simultaneously. Strict original-channel violations also correspond under this map.

## Direct proof

For an arbitrary \(2\times2\) matrix \(X\), direct entrywise multiplication gives
\[
S(X):=\sigma_y X^T\sigma_y=\operatorname{Tr}(X)I_2-X.
\]
This is an identity of complex-linear maps, not an assumption that \(X\) is real or a density. Since \(\operatorname{Tr}(\Phi_{2-p}(X))=\operatorname{Tr}(X)\), substitution yields
\[
S(\Phi_{2-p}(X))
=\operatorname{Tr}(X)I_2-(p-1)X-\frac{2-p}{2}\operatorname{Tr}(X)I_2
=\Phi_p(X).
\]
Tensor the equality four times. On the tensor-product matrix-unit basis,
\(S^{\otimes4}(X)=UX^T U\); linearity extends this to every operator. Thus the displayed channel identity is exact. For Hermitian \(\Lambda_{p'}(\rho)\), transposition and unitary conjugation preserve the entire multiset of real eigenvalues, establishing spectral equality including degeneracies.

For the projector claim, \(U^T=U\) for four copies and \(U^2=I\). Cyclicity and \(\operatorname{Tr}(AB^T)=\operatorname{Tr}(A^TB)\) give
\[
\operatorname{Tr}[P U\Lambda_{p'}(\rho)^T U]
=\operatorname{Tr}[UP^T U\,\Lambda_{p'}(\rho)].
\]
Transposition preserves orthogonal-projector rank and positivity, and conjugation by \(U\) preserves both. The transformation is its own inverse: transpose twice and use \(U^T=U\), \(U^2=I\).

For a pure single-qubit input, the two local output eigenvalues are \(a=(1+|1-p|)/2\), \(b=(1-|1-p|)/2\), with \(a\ge b\ge0\). A pure four-qubit product reference consequently has top-three sum
\[
R_3(p)=a^4+2a^3b=a^3(2-a)
=\frac{(1+|1-p|)^3(3-|1-p|)}{16}.
\]
This includes the degeneracies at \(a=b\) and \(b=0\). Since \(|1-p|=|1-(2-p)|\), \(R_3(p)=R_3(p')\). Thus the product-reference margin and the actual projector trace are preserved by the physical mirror. Equality of all output eigenvalues yields the same conclusion for every \(k\), not just \(3\).

## Exact remaining gap

The reduced global problem is still
\[
\operatorname{Tr}[P\Lambda_p(\rho)]\le R_3(p)
\quad\text{for every }0\le p\le1,\;\rho\ge0,\;\operatorname{Tr}\rho=1,\;
P=P^*=P^2,\;\operatorname{rank}P=3.
\]
No independent optimization of reduced marginals or nonphysical projector is permitted in this statement. A full proof or a physical strict violation remains open. The derivation is ordinary written mathematics, not a formal/kernel verification, independent-family review or novelty clearance. Subsequent bounded numerical checks, if performed, are separate evidence and cannot establish the universal claim.
