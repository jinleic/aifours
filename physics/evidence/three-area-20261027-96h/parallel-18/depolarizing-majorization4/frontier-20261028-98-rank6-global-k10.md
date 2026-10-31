# A rank-six spin-flip certificate for original global k10

**HIGH-CONSEQUENCE WRITTEN AUTHOR CANDIDATE, NOT ADOPTED.** The written argument below proposes that for **every** four-qubit physical density `rho`, every actual complex rank-ten orthogonal projector `P`, and every physical `0<=p<=4/3`,

\[
\operatorname{Tr}[P\Phi_p^{\otimes4}(\rho)]
\le K_{10}(\Phi_p^{\otimes4}(|0000\rangle\langle0000|)).\tag{1}
\]

It is a new original-channel **index10** comparison, not the outstanding index3 or a full-majorization solution. All identities and inequalities are derived here at ordinary finite-dimensional spectral/Pauli interfaces; no historical held result, old coefficient claim, external theorem, formal proof, stronger-family/human review, executable universal verification or novelty assessment is assumed. Full disjoint review is requested. Earlier process and quarantine findings remain unchanged.

## 1. A rank-six projector operator inequality

For any four-qubit operator `X`, put

\[
H_1(X)=\sum_i I_{\bar i}\otimes\operatorname{Tr}_{\bar i}X,\qquad
\widetilde X=Y^{\otimes4}X^T Y^{\otimes4}.
\]

**Lemma.** For every complex rank-six orthogonal projector `Q`,

\[
H_1(Q)+\widetilde Q\ge7I_{16}.\tag{2}
\]

*Proof.* Independently rotate each physical qubit so the Pauli expansion of its actual marginal `Tr_bar_i Q` is `3I+(m_i/2)Z_i` with `m_i>=0`. The left side is covariant under these local unitary changes, including the full spin flip. Write `S=sum_i m_i`; then

\[
H_1(Q)=12I+\tfrac12\sum_i m_i Z_i.\tag{3}
\]

By the rank-six variational principle, `S=Tr Q sum_i Z_i<=12`: the six largest eigenvalues of `sum_i Z_i` are `4,2,2,2,2,0`. Similarly, for **each** omitted site i, the six largest eigenvalues of the remaining three-site sum (with the fourth factor carried along) are `3,3,1,1,1,1`, giving

\[
\sum_{j\ne i}m_j\le10,\qquad m_i\ge S-10.\tag{4}
\]

If `S<=10`, (3) gives `H1(Q)>=7I`, and (2) follows from `tilde Q>=0`. Otherwise set `c=(S-10)/2`, so `0<c<=1`. Let `e=|1111>` in the rotated basis and `E=|e><e|`. The eigenvalue of `H1(Q)-7I` at e is `-c`; every other computational basis eigenvalue is at least `-c+min_i m_i>=c` by (4). Therefore

\[
H_1(Q)-7I\ge c(I-2E).\tag{5}
\]

It remains to show `tilde Q+c(I-2E)>=0`. Since full spin flip sends `|1111>` to `|0000>` up to phase,

\[
q:=\langle e|\widetilde Q|e\rangle=\langle0000|Q|0000\rangle.
\]

Let `N=sum_i (I-Z_i)/2`, and `Pi_1` be the weight-one computational projector, of rank four. The exact diagonal inequality `N>=2I-2|0000><0000|-Pi_1`, the rank of Q, and `Tr(Q Pi_1)<=4` imply

\[
\operatorname{Tr}(QN)\ge 12-2q-4=8-2q.
\]

But `S=Tr Q(4I-2N)`, hence `S<=8+4q` and

\[
q\ge(S-8)/4=(1+c)/2.\tag{6}
\]

For any orthogonal projection R, unit vector e, and `0<=c<=1`, the elementary implication

\[
\langle e|R|e\rangle\ge(1+c)/2
\quad\Longrightarrow\quad R+c(I-2|e\rangle\langle e|)\ge0\tag{7}
\]

holds. To see it, let `q=<e|R|e>`. For `0<q<1`, in the orthonormal basis `Re/sqrt(q),(I-R)e/sqrt(1-q)`, the relevant 2-by-2 block has diagonal entries `1+c-2cq` and `c(2q-1)`, and determinant `c(2q-1-c)`. The hypothesis makes both diagonals and determinant nonnegative. On its orthogonal complement the operator is `R+cI>=0`; `q=1` is immediate and `q=0` is excluded when `c>0`. Equations (5)–(7) give (2). ∎

## 2. From the same rank-six Q to the two-body marginal tail

Define

\[
H_2(\rho)=\sum_{i<j}I_{\overline{ij}}\otimes\rho_{ij},\qquad
F(\rho)=\sum_{i,a}\sigma_i^a\rho\sigma_i^a.
\]

The one-site spin-flip identity and the Pauli twirl give the exact operator identity, for every four-qubit density,

\[
H_2(\rho)-H_1(\rho)+I
=\rho+\widetilde\rho+\tfrac12 F(\rho)\ge\widetilde\rho.\tag{8}
\]

For instance, if `T_m=sum_|S|=m E_S(rho)`, full spin flip gives `tilde(rho)=rho-2T1+4T2-8T3+16T4`, while `H2=4T2`, `H1=8T3`, `16T4=I` and `F=4T1-4rho`. This proves (8) without any partial-transpose positivity assumption.

Both `H1` and full spin flip are self-adjoint in the trace pairing. Thus, with the SAME actual rank-six Q, (2) yields

\[
\operatorname{Tr}Q(H_1(\rho)+\widetilde\rho)
=\operatorname{Tr}\rho(H_1(Q)+\widetilde Q)\ge7.
\]

Combining with (8) and `Tr Q=6` gives

\[
\operatorname{Tr}(QH_2(\rho))\ge1.\tag{9}
\]

The actual rank-six `H1` trace is at least six as well: as in `frontier-20261028-94-global-tail-biseparable.md`, the sum of one-qubit marginals is a convex average of local-unitary conjugates of `sum_i |0><0|_i`; the latter's six smallest eigenvalues are `0,1,1,1,1,2`, summing to six. No independent optimization of Q is used in either coefficient.

## 3. Original k10, every physical noise

For `0<=p<=1`, set `t=1-p`, `b=p/2`, `a=t+b`. Expanding the commuting erasures and retaining the terms with four, three, and two erased sites gives the actual Loewner bound

\[
\Phi_p^{\otimes4}(\rho)\ge b^4 I+tb^3H_1(\rho)+t^2b^2H_2(\rho).\tag{10}
\]

Apply one actual rank-six Q and both preceding inequalities:

\[
\operatorname{Tr}[Q\Phi_p^{\otimes4}(\rho)]
\ge6b^4+6tb^3+t^2b^2
=b^4+4ab^3+a^2b^2.\tag{11}
\]

The last expression is exactly the sum of the six smallest eigenvalues of the pure product reference, with ties permitted. Minimize the left side over actual rank-six Q and use unit trace: the complementary ten-prefix is at most the reference k10, proving (1) in this range. At `p=1` the output is uniform. For `1<=p<=4/3`, the exact four-site full-transpose spin flip maps the channel at `2-p` to the channel at p and bijects the actual projectors, with unchanged reference spectrum. Thus (1) extends over the whole physical interval.

Together with the separately written tail comparison `94`, this candidate gives original global `k=10,11,12,13,14,15` plus trace; it does **not** establish `k=3` or the intervening global indices. The written proof, not the finite tests below, is the source of the universal claim and still requires disjoint review.

## 4. Actual exact and numerical evidence

`frontier-20261028-97-rank6-tail-check.py`, SHA256 `16e3f2b3ec6572d2d1ff3c8caea863affec342db7e0bf3753b0f44e43555175f`, ran with `python3 -B` and single-threaded BLAS, exit0. For the explicit non-diagonal rank-six projector spanning `(24|0000>+7|1111>)/25`, `|0001>`, `|0010>`, `|0011>`, `|0100>`, `|1000>`, exact Gaussian-rational arithmetic verifies `Q=Q^2=Q^dagger`, trace six, `S=7108/625`, `c=429/625`, `q=576/625`, and all 16 positive LDL pivots of the actual dual operator `H1(Q)+tilde Q-7I`. Thus the check exercises the nontrivial `S>10` branch, not just the direct PSD branch.

For the actual state `(2|0000>+|0101>+|0110>+|1001>+|1010>+|1111>)/3`, exact matrix arithmetic verifies (8), the same-Q `Tr Q(H1+tilde rho)=79606/5625>=7`, and `Tr QH2=67243/5625>=1`. At `p=2/3` and `4/3`, the exact sequential and Pauli channel matrices agree and the same actual Q/reflected Q has trace `68864/151875>13/81`, the latter being product bottom-six. At `p=2/3` the omitted-erasure remainder is checked exactly as `(3rho+F(rho)/2)/81`, a positive sum. Numerical top10/bottom6 printouts are explicitly approximate; one state and one Q do not establish (1).

Two prior 500-start floating scouts, `frontier-20261028-95-pair-tail-scout.py` SHA256 `ac7a235ecc9698c2d30d7ff39895a16b25c7e98e5039848fe3da7fbb0054c6e4` and `frontier-20261028-96-spinflip-tail-scout.py` SHA256 `7a2cc2ff2b00154172c3564dec4560f98a9f24a39ae7558f5758c46caa554a37`, respectively found minima `0.9999999999999937` and `6.9999999999999725`, with no robust auxiliary violation. They are not proof and their roundoff does not contradict (2) or (9). Native evidence-pin clock `Wed Oct 28 20:08:02 PDT 2026`.
