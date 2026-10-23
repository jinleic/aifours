All four SHA-256 values in `manifest.json` match. I found **no fatal or major defect in the standalone rank theorem**. The normal-form case split is exhaustive. The following fixes are needed.

1. **Minor — incorrect marginal matrix identity.**  
   [REDUCTION.md:13](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/REDUCTION.md:13) incorrectly identifies the left Gram matrix with the marginal by a fixed index permutation.

   With the stated ordering,
   \[
   M=(U^\Gamma)^T S,\qquad
   9\rho_{14}=MM^\dagger=(U^{\Gamma\dagger}U^\Gamma)^T.
   \]
   Replace the displayed identity accordingly. Its spectrum agrees with that of \(U^\Gamma U^{\Gamma\dagger}\), so all rank, purity and entangling-power conclusions survive.

2. **Minor — specify which rank bound transfers to T-dual gates.**  
   “The same holds” at [LEMMA_R_PROOF.md:12](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/LEMMA_R_PROOF.md:12) needs qualification.

   For \(V=US\),
   \[
   V^R=U^\Gamma S,\qquad V^\Gamma=U^R S.
   \]
   Consequently, the transferred conclusion is
   \[
   \operatorname{rank}V^R\le6,\qquad e_p(V)\le15/16.
   \]
   A T-dual gate has unitary \(V^\Gamma\), hence \(\operatorname{rank}V^\Gamma=9\). [REDUCTION.md:56](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/REDUCTION.md:56) already states the correct operator-Schmidt-rank counterpart.

3. **Minor — make the pivot argument explicit.**  
   [LEMMA_R_NORMAL_FORM.md:88](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/LEMMA_R_NORMAL_FORM.md:88) should define the projections and explain preservation of the subspaces.

   After eliminating the scalar pivot,
   \[
   \operatorname{rank}M
   =1+\operatorname{rank}
   \begin{pmatrix}0&P\\ \mathbf B&\Omega'\end{pmatrix},
   \qquad \Omega'=\Omega-xn_0.
   \]
   Define
   \[
   E_{\mathbf B}=I-\mathbf B\mathbf B^+,\qquad
   F_P=I-P^+P.
   \]
   Elementary row and column elimination gives the stated rank formula. Crucially, \(n_0\in A\) and \(x=\operatorname{vec}R_0\in C\). Thus subtraction preserves both the row-space constraint \(A\) and the column-space constraint \(C\). Therefore
   \[
   \operatorname{rank}(E_{\mathbf B}\Omega'F_P)
   \le\min(3-r_P,3-r_B),
   \]
   proving \(\operatorname{rank}M\le4+\min(r_P,r_B)\). This is an exposition fix; the argument is sound.

4. **Minor — distinguish the closed proof from unavailable certificates and imports.**  
   The named attaining matrix at [REDUCTION.md:29](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/REDUCTION.md:29), the local certificates at [LOCAL_THEOREM.md:46](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/LOCAL_THEOREM.md:46), and the text of [44] are absent from this bundle. `parent-exact-relations.json` is also outside the manifest’s hash list.

   Include the explicit matrix and certificates for a reproducible standalone package. I checked the analytic inverse-function-theorem argument in `LOCAL_THEOREM.md`; its numerical rank and determinant premises remain unverified here. The global rank proof does not depend on them. Identification with \(O_9\) remains conditional on the imported uniqueness theorem.

My independent reconstruction supports the proof as follows.

- **Normal form, relations, symmetries and gauges.**  
  At [LEMMA_R_PROOF.md:20](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/LEMMA_R_PROOF.md:20), the four biunitarity relations follow directly from unitarity of the block array and its block transpose. Over \(\mathbb C\), the two four-dimensional projective varieties in \(\mathbb P^8\) must intersect. Normalizing the resulting product-to-product pair gives the claimed entry \(1\); unit row and column norms then force exactly the stated zero pattern.

  Expanding the zero-index blocks gives the four unital Kraus triples, \((\alpha)\)–\((\delta)\), their mirrored counterparts and \((O1)\)–\((O4)\). The actions of \((14),(23),(12)(34)\) on sectors and corners are correct. They preserve the two maximally mixed bipartitions and the spectrum of the third flattening. The two gauges are independent: each changes its matrix indices while merely mixing the other sector’s labelled generators.

- **Fact K.**  
  The revised proof at [LEMMA_R_PROOF.md:55](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/LEMMA_R_PROOF.md:55) is valid, including singular Bloch matrices. Hermiticity preservation makes the Bloch matrix real; signed real SVD permits both orthogonal factors to lie in \(SO(3)\), and both lift to \(SU(2)\). For diagonal Bloch parameters \(\lambda_i\),
  \[
  p_0=(1+\lambda_1+\lambda_2+\lambda_3)/4
  \]
  with the usual three other sign patterns. Orthogonality of the vectorized Paulis proves CP exactly when all \(p_j\ge0\).

  The Kraus span is the unvectorized range of the Choi matrix, hence is representation-independent. Pauli multiplication and Clifford conjugation give the claimed three-dimensional symmetric space and the diagonal containment for dimensions one or two.

- **Lemma N1 and Lemma T.**  
  [LEMMA_R_NORMAL_FORM.md:49](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/LEMMA_R_NORMAL_FORM.md:49) correctly removes the antisymmetric components using independence of the three symmetric Kraus matrices. Applying it requires taking the adjoint of \((\alpha)\), together with \((\gamma)\); this gives precisely the asserted \(Q_a,\Omega_{ad}\) containment.

  The proof of Lemma T at [LEMMA_R_NORMAL_FORM.md:66](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/LEMMA_R_NORMAL_FORM.md:66) covers every pencil. For a non-diagonalizable \(u=\lambda I+N\), the remaining factor is \(N\otimes I+I\otimes N\), whose image has dimension two. For an entirely singular two-dimensional pencil, vanishing of the determinant forces a common image or common kernel. Zero- and one-dimensional pencils also satisfy the bound. The tensor reformulation has the correct index pairing.

- **Proposition G and Lemma S.**  
  At [LEMMA_R_PROOF.md:92](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/LEMMA_R_PROOF.md:92), strict contraction of \(N_0\) makes \(\mathbf N\) rank two. Symmetry of \(N_d\) makes both \((O1)\) and \((O3)\) constrain the required tensor flattening to the same two-dimensional kernel. Lemma T consequently gives \(r_B\le2\). Together with the corrected pivot explanation, this proves rank at most six.

  Lemma S correctly handles every norm-one corner, including \(\sigma=1\): positivity forces all remaining \(N_d,Q_a\) into one matrix-unit line, leaving at most six slice directions.

- **Residual propositions and assembly.**  
  [LEMMA_R_PROOF.md:99](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/LEMMA_R_PROOF.md:99) is valid over complex coefficients. In A*, the two independent kernel directions force nonzero \(R_b,T_b\); \((O4),(O2)\) then eliminate the off-diagonal entries of every \(Q_a\). If \(\dim A=1\), the two kernel directions would be proportional, contradicting \(\dim C=3\).

  In B*, at [LEMMA_R_PROOF.md:113](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/LEMMA_R_PROOF.md:113), the four nonempty supports force exactly the two stated patterns. The permitted simultaneous basis swap interchanges them. The reduced \((O2)\) equations give the exhaustive alternatives \(\beta=\gamma=0\) and \(\beta\gamma\ne0\). The first forces both orientations of \(\Omega\) diagonal and rank at most five. The second forces \(N_0=R_0=0\), then \(\Omega=0\), and finally a unitary flattening.

  Thus [LEMMA_R_PROOF.md:136](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/LEMMA_R_PROOF.md:136) covers every normal form: norm-one corners; a three-dimensional sector routed to \(C\); or all sectors of dimension at most two. No one-dimensional-sector or zero-corner case is omitted.

The counterexample search produced no valid counterexample.

- Exact enumeration reproduced the partial-transpose **term-rank** histogram for all dual permutations:
  \[
  \{3:2556,\;4:5508,\;5:648,\;9:72\}.
  \]
  The 72 rank-nine cases are 2-unitary. Arbitrary enphasing preserves the support bound; local unitaries preserve the actual partial-transpose rank.
- Controlled-unitary-times-SWAP gates have rank at most three directly from their slice formula. I also tested diagonal twists and local-unitary transforms of these gates.
- Across **248 projected complex starts, twists and perturbations**, 236 converged: 199 had rank six, three had rank four, and 34 were 2-unitary. Among converged non-2-unitary points, the largest seventh singular value was below \(4\times10^{-14}\).
- In **288 targeted attempts** that explicitly imposed a seventh singular value before duality retraction, 96 converged to rank-six gates, 96 to 2-unitaries, and 96 did not converge. The failed runs establish nothing.
- At 80-digit precision, a perturbation of an independently constructed attaining gate reached duality residual below \(2\times10^{-68}\), with its last three singular values below \(2\times10^{-81}\). A small perturbation of \(P_9\) retracted to a 2-unitary.

For an independent exact sharpness check, I constructed \(H\) using the supplied normal-form conventions. Set \(t=\sqrt6/4\), with Pauli matrices \(X,Z\), and take
\[
\begin{aligned}
&N_0=R_0=\tfrac12I_2,\\
&N_1=Q_1=R_1=T_1=tZ,\\
&N_2=Q_2=tX,\qquad R_2=T_2=-tX,\\
&\Omega_{ad}=-\tfrac12\delta_{ad}I_2.
\end{aligned}
\]
Exact arithmetic over \(\mathbb Q(\sqrt6)\) verifies
\[
HH^\dagger=I,\qquad H^R=H,\qquad
H^\Gamma H^{\Gamma\dagger}=\tfrac34(I+S).
\]
This proves rank six, non-2-unitarity and \(e_p(H)=15/16\), independently of the unavailable named \(U_s\) matrix.

Finally, the objective identity and Cauchy–Schwarz step at [REDUCTION.md:17](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-rank-bound-parent-inputs-v2/REDUCTION.md:17) are correct:
\[
\operatorname{tr}W=9,\qquad
1-e_p=\frac{\operatorname{tr}W^2-9}{72},\qquad
\operatorname{tr}W^2\ge\frac{81}{r}\ge\frac{27}{2}.
\]
Equality requires exactly six eigenvalues \(3/2\). The T-dual transfer preserves entangling power and 2-unitarity.

The established sharp maximum is on the non-2-unitary part of \(D\cup T\). An unrestricted assertion over \(U(9)\) would be false by continuity near a 2-unitary. The survey’s precise scope cannot be checked from this bundle. Novelty and priority were not assessed.

VERDICT: ACCEPT-WITH-FIXES