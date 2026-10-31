# Exact mixed-density check for the statewise noise theorem

Author candidate `frontier-20261028-45-every-density-statewise.md` SHA256 `37d0fa872876ebd7ed03a9860522e63e2f2b86b0e268074affa9815a68838e2f`; checker `frontier-20261028-46-statewise-mixed-check.py` SHA256 `101c91bf716abb555e207380a2e77c441317b89b4a13af1ac4e44525079e2ca2`. Native post-run hash clock **Wed Oct 28 18:07:53 PDT 2026**. Ran `python3 -B physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-20261028-46-statewise-mixed-check.py` from repo root; exit0. The checker imports the previously pinned exact Gaussian-rational matrix, spectral-rank and independent Pauli-mixture helpers.

The actual mixed density is
\[
 \rho=\tfrac12|W_4\rangle\langle W_4|+\tfrac12|0000\rangle\langle0000|.
\]
The two displayed components are exactly orthogonal pure densities; the checker verifies \(\rho^2=\rho/2\), \(\operatorname{Tr}\rho=1\), hence rank2 and spectral weights \(1/2,1/2\). For W, exact local radii are all1/2, \(S=1,L=4,\delta=4\); the theorem's decomposition gives \(D=2\) and \(\epsilon=2/(\sqrt{546}-5)>1/10\), since \(546<25^2\). The product component needs no smaller threshold. For \(t=1/20\), the theorem's common-projector lower gap is \(tD/32=1/320\).

At `p=19/20` and `p=21/20`, the checker independently builds the complete original Pauli Kraus mixture and the sequential original channel and checks all matrix entries agree. It verifies every eigenvalue multiplicity by exact rational rank. At each p the actual output spectrum is
\[
\begin{array}{c|rrrrrrrrr}
\text{eigenvalue}&9261/128000&345303/5120000&343539/5120000&80199/1280000&399/6400&159201/2560000&297103/5120000&295659/5120000&6859/128000\\
\text{multiplicity}&1&1&3&1&3&2&1&3&1
\end{array}
\]
in descending order. An actual rank-three top projector is constructed for the first p and mapped deterministically by the spin-flip mirror for the second; exact Hermiticity, idempotence and trace3 are checked. At both p its trace and the actual top3 are **529641/2560000**, the product reference top3 is **546399/2560000**, and the exact gap is **8379/1280000 > 1/320**.

This is one exact mixed state and two parameters, not a proof of the all-density theorem or a counterexample. The written predecessor chain and universal statewise quantifier require disjoint review. In particular, no **uniform in all states** positive epsilon follows from these calculations or from the stated proof.
