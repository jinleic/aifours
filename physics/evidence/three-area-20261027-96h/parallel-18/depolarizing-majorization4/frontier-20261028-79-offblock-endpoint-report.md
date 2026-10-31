# Exact physical endpoint checks for the off-block noise candidate

Conditional author candidate `frontier-20261028-77-offblock-uniform-noise.md` SHA256 `04de53eea1187e9a890f263c954c3e05abe7c1e621817bfea24c811ca23eafb2` proposes original k3 for every density and rank-three projector when \(|1-p|\le9\cdot10^{-6}\), conditional on the full pending Hessian/block predecessor. This file records **one physical state at two exact endpoints**, not a verification of that universal theorem.

`frontier-20261028-78-offblock-endpoint-check.py`, SHA256 `74767e92a91a2f7dcd8b766a2698665177fffe235122b8dc56de2fb2712864ed`, ran from repo root under single-threaded BLAS and `python3 -B`, exit0. Native post-run hash clock **Wed Oct 28 18:55:33 PDT 2026**. Exact Gaussian-rational arithmetic constructs
\[
 |\psi\rangle=(1500|0000\rangle+|0011\rangle+2i|0111\rangle+2|1111\rangle)/\sqrt{2250009}.
\]
Its displayed product-coordinate epsilon is \(1/500\); the true maximizing-product gauge epsilon is at most that value. The input is directly checked Hermitian, idempotent and trace1.

At both actual physical parameters \(p=999991/1000000\) and \(p=1000009/1000000\), complete original Pauli Kraus and sequential-channel matrices agree exactly. Each output has 16 positive exact LDL pivots. Exact 16-pivot LDL and inertia `(15 positive,1 negative,0 zero)` respectively certify
\[
 \lambda_1<\frac{312511250077}{5000000000000},\qquad
 \lambda_2,\lambda_3<\frac{3125056249701}{50000000000000}.
\]
Thus its actual original k3 sum is strictly below \(2343806250043/12500000000000\), while the product-reference k3 sum is exactly
\(3000072000485999999993439/16000000000000000000000000\). Their exact positive difference is
\[
 \frac{430959999993439}{16000000000000000000000000}.
\]
For one actual rank-three reference-space projector and its deterministic spin-flipped transpose at the second endpoint, exact Hermiticity/idempotence/trace3 were checked; both same-P original output traces are `750021000085500053998683749271/4000016000000000000000000000000`.

NumPy separately observed top eigenvalues approximately `(0.06250225001537517,0.06250112499400003,0.06250112499399993)` at the first endpoint. The certified inequality above uses exact rational LDL/inertia rather than these decimal observations. The candidate's all-variable Hessian, off-block norm budget, projector ordering, product-gauge and mixed-state steps still require full disjoint written review; neither this example nor the old held outcomes establish them.
