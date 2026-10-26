# Polarized-block parent — additive H-Hermiticity wording correction

Actual observed clock before creation: **2026-10-25T09:44:00-0700 PDT** (bound by the author erratum's verbatim clock 09:42:57). Additive to `depol-polarized-positive-block-parent-v1.md`, which is preserved unchanged. Mandatory v9/v10 and HOLD; no scientific execution or GO.

The parent read the author's additive `physics/evidence/three-area-20261023-96h/parallel-18/depolarizing-majorization4/polarized-v4-H-hermiticity-erratum-v1.json` before this record. Its derivation is correct and short: off-site Pauli products commute with real expectation, and at one site the imaginary part of h is the antisymmetric contraction of r with itself, which vanishes; equivalently `h=Gr` with `(G−G^T)r=2i·blockdiag(cross r_i)r=0`. Hence h is REAL and `H=sum_mu h_mu S_mu` is HERMITIAN: `H*=H`.

Effect on the accepted scope of `depol-polarized-positive-block-parent-v1.md`:

- The v4 phrase "generally NONHERMITIAN H" was an overgeneral description, wrong for the actual field. WITHDRAW that wording only.
- Every displayed formula containing H and H* remains correct and simplifies with H*=H: H+H*=2H, and since Hpsi=ZLpsi, the gradient field reads `g=Q[L^2+2ZL−12L−8tilde(rho)]psi`. The positive block, its full trace identities, the product-boundary control and the epsilon=0/singular Schur conclusions are unchanged.
- This correction does NOT widen the scope: no CLIP, K2/K3 leading-sum, rank3/4 containment or rank2 d>0 quartic follows, and g is still not QLpsi.

Timing is honest: the correction was derived AFTER the complete v67-B review and v67-C return, during primary resumption. It is attached here at the current gate boundary without backdating into the v67 packet, the pinned v4 source bytes, checkpoints013/014 or park addendum5, whose non-Hermitian descriptions are hereby qualified. The same correction applies to the composite T=WW^T description nowhere else. No theorem is withdrawn; no stronger acceptance is conferred.
