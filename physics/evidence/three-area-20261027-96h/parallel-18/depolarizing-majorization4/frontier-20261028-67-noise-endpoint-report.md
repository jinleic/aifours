# Exact original-channel test at both proposed uniform-noise endpoints

This is one selected **physical** consistency test of the conditional all-density interval in `frontier-20261028-65-parseval-uniform-noise.md`; it is not a proof for all inputs or an original-channel counterexample.

The actual pure input is
\[
 |\psi\rangle=\frac{1500|0000\rangle+|0011\rangle+2i|0111\rangle+2|1111\rangle}{\sqrt{2250009}}.
\]
Its displayed `|0000>` coordinate has \(\epsilon=1/500\) in a normal direction supported on weights2–4. The **optimal** product-overlap gauge epsilon is at most this displayed value; the check does not claim that `|0000>` is a global product maximizer. The exact checker verifies the density is Hermitian, idempotent and trace1.

For both physical endpoint parameters
\[
p_-=9999999/10000000,\qquad p_+=10000001/10000000,
\]
the checker constructs the complete original Pauli Kraus mixture and the sequential local channel and proves entrywise equality over exact Gaussian rationals. For each output, 16 exact positive LDL pivots certify positivity. It also certifies
\[
\lambda_1<\frac{390625156249}{6250000000000},\qquad
\lambda_2,\lambda_3<\frac{3125000624997}{50000000000000}.
\]
The first follows from 16 exact positive LDL pivots; the second from exact inertia `(15 positive,1 negative,0 zero)` for \((3125000624997/50000000000000)I-\sigma\). Thus the actual original top3 is **strictly below**
\[
 \frac{4687501249993}{25000000000000},
\]
whereas the exact product-reference top3 is
\[
 \frac{30000008000000599999999999999}{160000000000000000000000000000}.
\]
Their difference is exactly
\[
 \frac{45399999999999999}{160000000000000000000000000000}>0.
\]
This is a rigorous lower bound on the original k3 gap for this one state at each endpoint; no decimal cancellation is used.

The actual rank-three projector onto \(|0000\rangle,|0001\rangle,|0010\rangle\) is checked for \(p_-\); its deterministic spin-flipped transpose is checked for \(p_+\). Both are exactly Hermitian idempotents of trace3, and their actual original-output trace is
`7500031999996150000066666670861111/40000160000000000000000000000000000`, below the certified universal spectral upper bound for this output. NumPy additionally observed top eigenvalues approximately `(0.06250002499983709,0.06250001249993344,0.06250001249993332)` at \(p_-\); these decimals are observations only, not the certificate.

`frontier-20261028-66-noise-endpoint-check.py` SHA256 `0a9468089b7677c9846db198bc3b8e18abdd744aa68235b998d5302fbcb6efcc` ran under single-threaded BLAS and `python3 -B` from repo root, exit0. Its exact matrix/LDL/inertia helper chain is the previously pinned one; NumPy was used only for the labelled eigenvalue observations. Native hash clock **Wed Oct 28 18:39:43 PDT 2026**.

The universal \(|1-p|\le10^{-7}\) statement remains an author candidate requiring independent written review of the full predecessor and constants. One exact input at two endpoints neither proves that statement nor settles original k3 outside the interval.
