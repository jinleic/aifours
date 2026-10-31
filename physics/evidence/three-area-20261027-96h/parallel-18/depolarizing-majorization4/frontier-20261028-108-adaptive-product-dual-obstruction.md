# A product-measurement bound and an adaptive-product operator obstruction

**WRITTEN physical subcase plus exact counterexample to an auxiliary strengthening, NOT an original k3 counterexample.** For arbitrary actual input, the original output comparison is elementary at every index if the test projector is diagonal in one tensor-product local basis. However, the convenient strengthening `F(Q)<=4(I+Q)` from packet 106 already fails for a rank-three Q made entirely of mutually orthogonal **product** vectors that are three leaves of an adaptive local measurement. A genuinely four-partite-entangled physical input witnesses the failure. The original dual-channel bound remains strictly valid for this Q at the two checked noise values. No global k3, novelty, independent-family/human/formal certification, or process-history cure is asserted.

## 1. Every fixed product-basis test, every input, every index

Let `Phi_p(X)=(1-p)X+(p/2)Tr(X)I_2`, and let Q project onto any k distinct vectors of one fixed local product orthonormal basis on n qubits. Local covariance lets us take those vectors to be `|x>` with `x` in a subset C of `{0,1}^n`, `|C|=k`. For any physical `0<=p<=4/3`, `Phi_p^tensor n(Q)` is diagonal in this same basis; at `|z>` its diagonal is

\[
\sum_{x\in C}\prod_{i=1}^n
\begin{cases}1-p/2,&x_i=z_i,\\p/2,&x_i\ne z_i.\end{cases}\tag{1}
\]

All terms are nonnegative. As x ranges over **all** bit strings, these `2^n` summands are exactly the pure-product output spectrum, in some order: for `p>1` the largest one corresponds to bitwise complement rather than equality. Therefore the sum over any k of them is bounded by the product-reference top-k sum, for each z. Consequently

\[
\Phi_p^{\otimes n}(Q)\le
K_k(\Phi_p^{\otimes n}(|0^n\rangle\langle0^n|))I,
\]

and by channel self-adjointness the same bound holds for `Tr[Q Phi_p^tensor n(rho)]` for every actual density rho. This is a restriction on the **test projector**, not on the input; it does not control arbitrary entangled/nonclassical projectors or prove global majorization. Ties and both physical endpoints are included.

## 2. Exact product-vector Q defeating the stronger frame inequality

Define `|+>=(|0>+|1>)/sqrt2`, `|->=(|0>-|1>)/sqrt2` and let Q project onto

\[
|0000\rangle,\qquad |1{+}00\rangle,\qquad |1{-}{+}0\rangle.\tag{2}
\]

These vectors are mutually orthogonal products; Q is an actual rank-three orthogonal projector. They are also three leaves of one adaptive local product measurement: measure qubit 1 in the Z basis; on its 0 branch use the Z bases and select `0000`; on its 1 branch measure qubit 2 in X, then use Z on qubit 3 after `+` and X after `-`, selecting the displayed branches and `0` on qubit 4. Other branches complete the measurement. Thus failure below is **not** caused by entangled spanning vectors.

Nevertheless Q is NOT diagonal in any single tensor-product local basis. If it were, it would commute with a nonzero single-qubit Pauli direction on qubit 2. Restricting Q to qubit 1=`0`, qubits 3 and 4=`00` gives `|0><0|` on qubit 2, forcing that direction to be proportional to Z. But exact matrix entry `Q_{1000,1100}=1/4` couples opposite Z eigenvalues on qubit 2, so `[Q,Z_2]!=0`. Hence the fixed-basis theorem of §1 cannot be applied to this Q.

Let

\[
|\psi\rangle=(|0001\rangle+4|1000\rangle-2|1100\rangle+2|1110\rangle)/5.
\]

This is normalized and has exact bipartition Schmidt ranks `2,2,2,2,3,3,2`, so it is genuinely four-partite entangled. With `F(Q)=sum_{i,a}sigma_i^a Q sigma_i^a`, exact arithmetic gives

\[
\langle\psi|Q|\psi\rangle=6/25,\quad
\langle\psi|F(Q)|\psi\rangle=138/25,\quad
\langle\psi|[F(Q)-4(I+Q)]|\psi\rangle=14/25>0.\tag{3}
\]

Thus the natural product-reference-saturating inequality `F(Q)<=4(I+Q)` is false even for a projector spanned by orthogonal product states and a physical GME input. It would imply the still-open `F(Q)<=8I` since `Q<=I`, but its failure does **not** refute that weaker target, the separate spin-flip target, the direct original-channel comparison, or all-index product-basis §1.

## 3. Actual original-channel checks

`frontier-20261028-107-adaptive-product-dual-check.py`, SHA256 `7ec0fa3ca8b2dbde71fd14675b23bf9fb99809740fc270080372a48801f1527b`, ran with `python3 -B`, single-threaded BLAS, exit0. Fraction/Gaussian-rational calculations verify Q Hermiticity/idempotence/trace three, exact `Q_{1000,1100}=1/4`, psi purity and trace, all seven stated cut ranks, and every equality in (3). Independently assembled Pauli and sequential original channel matrices agree exactly at `p=2/3` and `4/3`. At **each** p, all 16 exact LDL pivots of `(3/8)I-Phi_p^tensor4(Q)` are positive, so for every physical input at that p,

\[
\operatorname{Tr}[Q\Phi_p^{\otimes4}(\rho)]<3/8<32/81=R_3(p).
\]

The universal-for-this-Q certified gap is at least `13/648`; the specifically named GME psi gives exact traces `2357/8100` and `191/2025` at the two noise values, respectively. Neither number is an original-channel counterexample. Native checker-pin clock `Wed Oct 28 20:52:47 PDT 2026`.

This is an exact counterexample to one **additional** operator inequality, not to the two open sufficient inequalities or original global k3. The adaptive-vs-fixed distinction and both full-operator/actual-input boundaries should be retained in any review.
