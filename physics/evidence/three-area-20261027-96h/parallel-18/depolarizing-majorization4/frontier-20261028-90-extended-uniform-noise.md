# Extending the normalized-tube k3 candidate to `|1-p|<=1/200`

**HIGH-CONSEQUENCE CONDITIONAL AUTHOR CANDIDATE — NOT ADOPTED.** Under the entire unreviewed normalized-tube derivation `frontier-20261028-88-normalized-tube-uniform-noise.md`, SHA256 `2d7aea2d8e95b3db0e547502f7828cab496129a31b569263d0cb6a48ab8fc98c`, including its named 59/77/81 Hessian, closest-product, common-projector, and mirror predecessors, the new bounds here propose the ORIGINAL k3 comparison for every physical four-qubit density, every actual complex rank-three projector, and

\[
|1-p|\le1/200.\tag{1}
\]

The noise radius is five times the 88 candidate. All imported candidates remain unreviewed; this is neither global all-parameter k3, proof of novelty, independent-family/human/formal verification, nor an executable universal proof. Historical holds, process and quarantine findings remain unchanged.

## 1. Extending the exact Hessian margin

Use the normalized notation of 88, with `t=1-p` and `0<t<=1/200`, `a=(1+t)/2`, `b=(1-t)/2`, and `D3=1-ab`. The explicit PSD weight-two identity of 81 holds throughout `t<=1/2`, not merely the smaller window used in that packet. It implies

\[
 A_2+K_2(M_2)\le-a^2t(1-t^2)
 \le-\frac{15}{64}t,
\]

since `(1-t^2)/4 >= 39999/160000 > 15/64`. The exact weight-three factorization in predecessor 59 gives

\[
 A_3+K_2(M_3)\le-
 \frac{t(1-t)(15+24t+38t^2+32t^3+3t^4)}{32D_3}
 \le-\frac{15}{32}(1-t)t
 \le-\frac{15}{64}t,
\]

where `0<D3<=1` and `1-t>1/2`. For weight four, the same source gives

\[
 A_4+K_2(M_4)=-t+\frac{t^7}{a^2+b^2}
 \le-t(1-2t^6)\le-\frac{15}{64}t,
\]

because `a^2+b^2 >= 1/2`. The cited exact mixed-weight additivity, nonnegative squared component weights summing to one, and Ky Fan subadditivity therefore extend the actual same-direction margin to this whole window:

\[
 A+K_2(M)\le-\frac{15}{64}t,
 \qquad Q_0+K_2(Q_1)\le-\frac{15}{4}.\tag{2}
\]

This extends the numerical parameter range of the written factor inequalities; it does not independently prove the predecessor coefficient identities.

## 2. Uniform norm, gap, and remainder budgets

Let `eta0=9/40`, `v0=23/200`, `s0=23/400`; use exactly the blocks, `D,V,W,S,C,Q` and `H_*` of 88. Pauli Parseval gives, for every normal direction `v`,

\[
\|V\|_F<23t\le v_0,\quad \|W-W_0\|_F<23t\le v_0,
\quad \|S\|_F\le v_0/2=s_0.
\]

Indeed `16 sqrt(2)<23`, and all reference cross-block divided gaps are at least two. They are at least two here because

\[
d_0-d_1=2(1+t)^3,\qquad
 d_1-d_2=2(1+t)^2(1-t)\ge2
\]

and `t(1-t-t^2)>=0`. In the reference weight basis the ordered rescaled diagonal eigenvalues are `[(1+t)^(4-h)(1-t)^h-1]/t`; thus `||D|| <= 4+6t+4t^2+t^3 < 5`. Also

\[
\|W_0\|\le\sum_i|\vec r_i(v)-\hat z|\le8,
\quad \|W\|<8+v_0<163/20.
\]

The commutator estimates of 88 now give

\[
\|C\|_F\le2v_0s_0+2(5)s_0^2
 =3703/80000<47/1000,\quad
 \|Q\|<163/20+47/1000<41/5.\tag{3}
\]

The same transverse-field compression in 88 is exact for all `t`; consequently

\[
\|\operatorname{off}Q\|
 <4+v_0+47/1000<21/5.\tag{4}
\]

For `eta<=eta0`, the perturbation of the block-diagonal reference satisfies

\[
\|H_*-D\|<\eta_0v_0+\eta_0^2(41/5)
=441/1000.
\]

The two relevant block gaps are therefore at least `2-2(441/1000)=559/500>11/10`, without requiring eigenvalue separation inside the weight-one block.

The first unitary conjugation and exact normalized identity from 88 give `e^{-hS}He^{hS}=H_*-eta^4 C+R`. Since `exp(2 eta0 s0)<=1/(1-2 eta0 s0)<103/100`, the full cubic remainder is bounded by

\[
\|R\|\le\eta^3\frac{103}{100}
\left[\frac{5(2s_0)^3}{6}
+\frac{v_0(2s_0)^2}{2}
+\frac{163}{20}(2s_0)\right]
=\frac{580473701}{600000000}\eta^3<\eta^3.\tag{5}
\]

Applying 88's exact two block-majorization inequalities and compression interlacing, with the new `Q_off` and gap bounds, gives

\[
K_3(H)\le K_3(D)-\frac{15}{4}\eta^2
 +3\eta^3+3\frac{47}{1000}\eta^4
 +\frac{3(21/5)^2}{11/10}\eta^4.\tag{6}
\]

Dividing the positive error terms by `eta^2` and using `eta<=9/40`, the explicit bound is

\[
3\frac9{40}+3\frac{47}{1000}(\frac9{40})^2+
 \frac{3(21/5)^2}{11/10}(\frac9{40})^2
=\frac{54870831}{17600000}<\frac{13}{4}.
\]

Thus `K3(H)<=K3(D)-eta^2/2`, or in the actual original channel

\[
 R_3(p)-K_3(\Lambda_p\rho)\ge t\eta^2/32
 \quad(0<t\le1/200,\ 0<\eta\le9/40).\tag{7}
\]

Pure product `eta=0` is exactly the reference spectrum.

## 3. Far inputs and all physical densities

For `eta>=9/40`, the same actual-marginal union bound from 88 gives

\[
8-L\ge2\eta^2\ge81/800>1/10\ge20t.
\]

Applying its common-projector inequality (17) yields a strictly positive original gap for **each** actual rank-three `P`; in fact the displayed conservative gap is at least `t/12800`. The small-tube case is (7), and at `t=0` all outputs are `I/16`. Affine averaging with one fixed `P` covers all mixed inputs; the named exact global transpose/spin-flip mirror covers `p>1`. These are conditional written derivations of (1), not a universal computational check.

## 4. Exact finite evidence and review boundary

`frontier-20261028-89-extended-noise-exact.py`, SHA256 `29e416955676d36b99b6b2bf74811973fa02c317a0125a4d7e0b692e175afbe5`, ran from repo root with single-threaded BLAS and `python3 -B`, exit0. Exact Python `Fraction` arithmetic checked all displayed numerical budgets, the three weight-margin scalar inequalities, `81/800>1/10`, and the gap at least `11/10`. For the single actual physical pure input `(1500|0000>+|0011>+2i|0111>+2|1111>)/sqrt(2250009)`, it exactly equated the full Pauli and sequential local channels at `p=199/200` and `201/200`; exact Gaussian-rational LDL certified all 16 output pivots positive and `lambda1<0.0637593981`, while exact inertia `(15,1,0)` of `0.0631249811 I-output` certified `lambda2<0.0631249811`. Hence the actual top-three sum is below `1900093603/10000000000`, the product reference is `4864239999/25600000000`, and their exact gap is at least `9383/640000000000`. The named actual rank-three projector and reflected partner were checked too. Numerical eigenvalue printouts are approximate; these two-endpoint checks are not all-input verification. Native checker-pin clock `Wed Oct 28 19:38:24 PDT 2026`.

A disjoint complete review must read this packet AND the entire 88/59/77/81/mirror proof dependency DAG, including all physical-state, complex-amplitude, Hessian, block, remaindering and same-projector steps. No individual excited-eigenvalue domination, nonphysical spectrum, independent optimizer, or unverified former conjecture is used. No source claims beyond this conditional k3 window are made.
