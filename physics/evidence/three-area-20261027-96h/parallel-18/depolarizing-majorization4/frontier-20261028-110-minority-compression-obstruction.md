# Physical rank-three obstruction to a fixed-minority dual certificate

**Exact physical counterexample to a proposed stronger operator certificate, NOT to original k3 or its open dual target.** Here `Q` is an actual complex-allowed rank-three projector and `rho` an actual genuinely four-partite-entangled pure input with nondegenerate one-qubit marginals. A natural pointwise PSD shortcut for the second rank-three operator target in packet 106 fails on their actual common subspace. The original dual channel is separately certified safe for this Q at two physical noises. The result needs written review and carries no novelty, formal/human/stronger-family acceptance or process-history cure.

## 1. The target and the tempting stronger shortcut

For a rank-three Q, put

\[
H_1(Q)=\sum_i I_{\bar i}\otimes\operatorname{Tr}_{\bar i}Q,
\quad \widetilde Q=Y^{\otimes4}Q^T Y^{\otimes4}.
\]

The still-open second target in `frontier-20261028-106-physical-rank3-dual-obstruction.md` is `H1(Q)+tilde Q<=10I`. Since spin flip is an involution and

\[
\widetilde{H_1(Q)}=4\operatorname{Tr}(Q)I-H_1(Q)=12I-H_1(Q),
\]

this is equivalently

\[
H_1(Q)-Q\ge2I.\tag{1}
\]

By trace-pairing self-adjointness, (1) for all rank-three Q is equivalent to

\[
\operatorname{Tr}[Q(H_1(\rho)-\rho)]\ge2
\quad\text{for all actual pure }\rho,Q.\tag{2}
\]

One particularly tempting route is stronger than (2): diagonalize all four actual one-qubit marginals of rho, take `E_min` to be the product projector onto their respective minority eigenvectors, and try to prove

\[
H_1(\rho)-\rho\stackrel{?}{\ge} I-E_{\min}.\tag{3}
\]

Indeed, tracing (3) against any actual rank-three Q would give `Tr Q(H1(rho)-rho)>=3-Tr(Q E_min)>=2`. This is an actual physical input constraint, not a scalar-spectrum relaxation. It holds on pure product inputs but, as shown next, is **false**. The even stronger rank-three compression `Q[H1(rho)-rho-I+E_min]Q>=0` is also false for a displayed actual Q. These failures do not imply that (1) or (2) fails.

## 2. Exact nondegenerate GME state and common rank-three Q

Let

\[
|\psi\rangle=\frac{9|0001\rangle+9|0010\rangle+9|0100\rangle
+9|0111\rangle+17|1000\rangle}{\sqrt{613}},
\qquad\rho=|\psi\rangle\langle\psi|.
\]

All support strings have odd parity, so each one-qubit marginal is diagonal in the displayed physical basis. Their exact minority probabilities are `(289,162,162,162)/613`, all strictly below one half; hence the four local majority/minority axes are unique up to phases and `E_min=|1111><1111|`. The exact Schmidt ranks over the seven nontrivial cut representatives are `2,2,2,2,3,3,3`; the state is genuinely four-partite entangled.

Put `A=H1(rho)-I+E_min`. It is diagonal. On the five support strings of psi, in the order `0001,0010,0100,0111,1000`, its entries are

\[
(775,775,775,197,1029)/613.
\]

Define the nonzero real vector

\[
|u\rangle=\frac9{775}(|0001\rangle+|0010\rangle+|0100\rangle)
 +\frac9{197}|0111\rangle+\frac{17}{1029}|1000\rangle,
\quad \nu=\langle u|u\rangle,
\]

and let `W=|u><u|/nu`. The exact number

\[
R=\frac{243}{775}+\frac{81}{197}+\frac{289}{1029}
=\frac{157977809}{157102575}>1
\]

satisfies `R-1=875234/157102575`. As `A|u>=sqrt(613)|psi>/613`, direct rank-one algebra gives

\[
\operatorname{Tr}[W(A-\rho)]
=\frac{R(1-R)}{613\nu}
=-\frac{138267549682306}{41828213810472121}<0.\tag{4}
\]

Finally choose the **actual rank-three Q**

\[
Q=W+|1011\rangle\langle1011|+|1111\rangle\langle1111|.
\]

Its three summands are orthogonal projections, and the negative test vector lies in its range. Therefore `Q(A-rho)Q` is not positive semidefinite, explicitly violating the compressed shortcut. Nevertheless its exact actual trace is

\[
\operatorname{Tr}[Q(H_1(\rho)-\rho)]
=\frac{167174587692206178}{41828213810472121}>2,
\]

so this SAME physical pair does not violate the open target (2). The failure is that a negative direction is a coherent superposition in the code subspace; fixing the entire rank-one allowance to the local-minority product vector is unjustified.

## 3. Executed exact original-channel checks

`frontier-20261028-109-minority-compression-check.py`, SHA256 `575476f8f0dfd24a479a801afbb50dde6b4292c77d2ee5c2b5b2cf9b2d8739ac`, ran with `python3 -B` and single-threaded BLAS, exit0. Fraction/Gaussian-rational arithmetic checked rho purity/trace, all local marginals and seven cut ranks, the actual projector `Q=Q^2=Q^dagger` with trace three, the diagonal A values, the exact negative normalized Rayleigh quotient (4), and that the negative witness is inside Q. It checked the displayed **positive** trace in (2) rather than silently treating the stronger PSD failure as a target failure.

At actual `p=2/3` and `4/3`, the exact Pauli and sequential channel matrices on Q agree, and all 16 exact LDL pivots of `(39/100)I-Phi_p^tensor4(Q)` are positive. Thus for **every** input at those two noises the actual Q has output trace below `39/100<32/81=R3`, with certified gap `41/8100`. For the specifically named rho, the exact traces are `526717342859002681/3388085318648241801` and `884853672384137971/3388085318648241801`, respectively. These checks establish no all-noise or all-projector result. Native checker-pin clock `Wed Oct 28 21:05:08 PDT 2026`.

The k3 problem and the global validity of both sufficient rank-three inequalities in 106 remain open. Any proof of (1) must tolerate this real, nondegenerate GME state’s rotated negative direction rather than forcing it into the unique local-minority product direction.
