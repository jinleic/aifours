# Full original output majorization for the convex 2+2 class

Write \(\Phi_p(X)=(1-p)X+(p/2)\operatorname{Tr}(X)I_2\) and \(\Lambda_p=\Phi_p^{\otimes4}\).

**WRITTEN AUTHOR RESULT, UNREVIEWED.** For every four-qubit density in the convex hull of states product across **some two-versus-two partition**, every physical noise `0<=p<=4/3`, every index `1<=k<=16`, and every actual complex rank-k projector `P`, the original channel satisfies

\[
\operatorname{Tr}[P\Lambda_p(\rho)]\le
K_k(\Lambda_p(|0000\rangle\langle0000|)).\tag{1}
\]

Thus the whole output spectrum is majorized by the product-reference spectrum on this specific mixed-state class; it includes the original k3 problem there. The class permits different 2+2 partitions in one mixture, but it is **not** all biseparable states and does not cover arbitrary genuinely four-partite-entangled states. No novelty, priority, external-model/human/formal/kernel/independent-family acceptance or global k3 claim is made. The only outside mathematical inputs are the elementary finite-dimensional Schmidt decomposition, Ky Fan variational principle and ordinary doubly stochastic characterization of vector majorization. The reflection is proved below.

## 1. Exact two-qubit output and a single bistochastic swap

First let `0<=p<=1`, `t=1-p`, `a=(1+t)/2`, `b=(1-t)/2`. By local-unitary covariance and Schmidt decomposition, a pure two-qubit input is locally equivalent to

\[
|\chi\rangle=\sqrt{u}|00\rangle+\sqrt{1-u}|11\rangle,\quad 0\le u\le1.
\]

Set `c=4u(1-u)` and `r=sqrt(1-c(1-t^2))`; then `t<=r<=1`. Directly applying the two local channels gives two odd-basis eigenvalues `(1-t^2)/4=ab` and two even-block eigenvalues

\[
\lambda_\pm=\frac{1+t^2}{4}\pm\frac{t}{2}r.\tag{2}
\]

They are ordered `lambda_+>=ab>=lambda_-`, including ties. The pure-product reference has eigenvalues `(a^2,ab,ab,b^2)`. Set `alpha=(1-r)/2` and let `J` exchange the first and fourth coordinates. Since

\[
\lambda_+=a^2-\alpha t,\qquad
\lambda_-=b^2+\alpha t,\qquad a^2-b^2=t,
\]

the **whole actual eigenvalue vector** is obtained from the reference vector by the single doubly stochastic matrix `(1-alpha) I+alpha J`. At `t=0` both vectors are uniform and the same conclusion holds. This is stronger than checking only a few eigenvalues: it supplies all three nontrivial two-qubit prefix inequalities at once.

## 2. Tensorization and the actual mixed-state bridge

If a pure four-qubit input is `chi_A tensor chi_B` across a 2+2 partition, its channel output is the tensor product of the two **actual** two-qubit outputs. Their individually established bistochastic relations give

\[
\lambda(\Lambda_p(\rho))
=(D_A\otimes D_B)\lambda(\Lambda_p(|0000\rangle\langle0000|))
\]

up to the harmless choice of tensor-product eigenvalue order. `D_A tensor D_B` is doubly stochastic, so every k-prefix satisfies (1). The reference spectrum does not depend on the chosen partition or local product bases. For a convex mixture of such pure states, even with different balanced partitions, fix **the same actual** rank-k `P`, apply each pure-input bound to its trace, and average; taking the maximum over `P` gives full majorization. No independent optimizing projectors are combined.

For `1<=p<=4/3`, `p'=2-p` lies in `[2/3,1]`. The one-qubit identity `Y X^T Y=Tr(X)I-X` gives

\[
\Lambda_p(X)=Y^{\otimes4}\Lambda_{p'}(X)^T Y^{\otimes4}.
\]

This preserves the whole output spectrum and maps every actual `P` to `Y^{\otimes4}P^T Y^{\otimes4}`. The product-reference spectra agree. Hence the established `[0,1]` result covers all physical noise.

## 3. Exact auxiliary Pauli-frame spectrum for pure 2+2 inputs

This second result concerns the auxiliary frame, not an additional premise for (1). For a pure two-qubit density `tau`, write `tilde(tau)=(Y tensor Y) tau^T (Y tensor Y)` and

\[
F_2(\tau)=\sum_{i=1}^2\sum_{a=x,y,z}\sigma_i^a\tau\sigma_i^a.
\]

Using the one-qubit Pauli twirl and the two-qubit spin-flip expansion gives the operator identity

\[
F_2(\tau)=2(I_4-\widetilde\tau).\tag{3}
\]

For an actual pure product `rho=tau_A tensor tau_B` across the balanced partition,

\[
F_4(\rho)=2(P_A+P_B),\quad
P_A=(I-\widetilde\tau_A)\otimes\tau_B,\quad
P_B=\tau_A\otimes(I-\widetilde\tau_B).
\]

Both `P_A,P_B` have rank three. Put `c_A=Tr(tau_A tilde(tau_A))`, `c_B=Tr(tau_B tilde(tau_B))`, and `kappa=sqrt((1-c_A)(1-c_B))`. The overlap map between their ranges has rank at most one and sole possibly nonzero singular value `kappa`: projecting the normalized `tau_A` vector onto `I-tilde(tau_A)` has squared norm `1-c_A`, and likewise for B. Choosing the two overlap directions and their orthogonal complements gives

\[
\operatorname{spec} F_4(\rho)=
\{2(1+\kappa),\;2^{\times4},\;2(1-\kappa),\;0^{\times10}\}.\tag{4}
\]

The multiset remains valid at `kappa=0` or `1` after combining coincident values. Consequently

\[
\operatorname{Tr}(F_4(\rho)-2I)_+=2\kappa\le2,\quad
K_3(F_4)=6+2\kappa\le8,\quad
\operatorname{Tr}(PT_1(\rho))\le\frac{5+\kappa}{2}\le3.\tag{5}
\]

The last step uses `T1=rho+F4/4` and the same actual rank-three `P`; it is strict in this bound if at least one pure two-qubit factor is entangled, since then its `c` is positive. For mixed states in the full convex 2+2 class, linearity of `F4` and convexity of `Tr(X-2I)_+ = max_{0<=E<=I}Tr[E(X-2I)]` extend the first inequality of (5), and hence the `t1<=3` auxiliary consequence. This establishes that named part of the separate conjecture in packet 86 **only on the balanced-biseparable convex class**, not globally.

## 4. Exact finite check, limitations, and parent boundary

`frontier-20261028-91-two-pair-spectrum-check.py`, SHA256 `d1ab7806e9a62f63c4821b37349ac588fc3097b56bab377213307b126fcb0fbc`, ran with `python3 -B` and single-threaded BLAS, exit0. On the actual normalized factorized state

\[
\frac{3|00\rangle+4|11\rangle}{5}\otimes
\frac{5|00\rangle+12|11\rangle}{13},
\]

exact Fraction/Gaussian-rational matrix arithmetic verified pure-state physicality and, by exact ranks of every shifted 16-by-16 frame matrix, the full spectrum `(10116/4225)^1, 2^4, (6784/4225)^1, 0^10`, corresponding to `kappa=833/4225`. The exact positive excess is `1666/4225`, `K3(F4)=27016/4225`, and the common-P bound in (5) is `10979/4225<3`. At original `p=2/3` and `4/3`, independently assembled Pauli and sequential channel matrices agreed exactly; 16 positive LDL pivots certified each output positive; another LDL certified `lambda1<141/1000`; exact inertia `(15,1,0)` of `(9/100)I-output` certified `lambda2<9/100`. Thus `K3(output)<321/1000<32/81`, with certified gap `5999/81000`; an actual rank-three projector and its reflected partner were explicitly checked. The printed numerical eigenvalues are approximate. This is a finite example, not a universal test or an independence review of the written argument. Native checker-pin clock: `Wed Oct 28 19:52:01 PDT 2026`.

The old parent-supported all-BISEP **k3** cut remains separately documented in `institute/runs/three-area-2026-10-23-96h/depol-v27-v29-biseparable-Slater-active-exterior-entire-parent-v1.md`; it is not an input to this direct all-index proof. No previous acceptance is transferred to (1) or (4), and prior process findings and quarantine dispositions remain unchanged.
