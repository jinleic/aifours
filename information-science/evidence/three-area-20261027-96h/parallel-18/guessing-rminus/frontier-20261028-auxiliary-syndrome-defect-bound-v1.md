# An all-variable graph-FD inequality for arbitrary auxiliary syndrome

**Status: WRITTEN with an exact rational coefficient check; scientific review pending.** For any original-neighbour R-minus FD law `X` and **any** finite-valued auxiliary random variable `S` (not necessarily determined by `X`, binary, a triangle syndrome, or even correlated with `X`), define

\[
G_S=3H(X_V)+17H(S)-2\sum_{v=1}^{10}H(X_v,S)
\]

and let `T_v` be the closed triangle neighbourhood of vertex `v`: the union of the other vertices sharing one of the ten pinned triangle factors with `v`. Let `bar` denote averaging over the four checked factor-preserving graph automorphisms, and let `a_i,b_i,c_i` be the positive rational per-representative weights of the respectively named `syndrome-neighborhood`, `syndrome-triangle`, and `local-triangle-fd` rows in certificate `frontier-20261028-two-syndrome-all-factor-dual-v1.json` SHA-256 `a8f6822f2c3e3a8e0b0fd639a9b0095a8ea6f38c7833f0ef2fb6551fa9bba087`. Then the exact coefficient identity and nonnegativity of Shannon rows give the genuine graph-FD bound

\[
\begin{aligned}
\Delta(X)\le{}&\frac{37}{492}G_S
+\sum_i a_i\,\overline{H(S\mid X_{N(i)})}
+\sum_i b_i\,\overline{H(S\mid X_{T_i})}\\
&+\sum_i c_i\,\overline{H(X_i\mid X_{T_i},S)}.
\end{aligned}\tag{34}
\]

Here each `T_i` in the middle sum is the triangle named by that certificate row, not the vertex-neighbourhood `T_v` used in the last sum. All three defect families have strictly positive weights. This is an exact, unconditional **auxiliary-dependent** inequality, not a numerical improvement of the general guessing upper bound; taking an arbitrary `S` may give positive right side.

## Certificate and specializations

The certificate identity holds on all 2,047 nonempty entropy coordinates, with negative coefficients on 319 elemental CMIs and one elemental monotonicity term, arbitrary coefficients on graph FDs, and the indicated positive coefficients on (34)'s defect terms and on `G_S`. `frontier-20261028-three-syndrome-linear-defect-check.py` SHA-256 `e97f193a0c61917a2d5f74e646cedefcbe8245836e3d71fbfd4f500a13bb9df3`, receipt SHA-256 `1588f967e6ce4027c814ac4f9d1f89063fa6e2db21e3ac629201971a0d36081e`, checks the signs of all 12 defect coefficients, while the independent checker `frontier-20261028-two-syndrome-all-factor-dual-check.py` SHA-256 `64fa545134f913993ee9dd4857a7904010200b1bd546b66cccbfbc8842d0b65a` and its receipt SHA-256 `8bd6527e81cd17c9a950d24a7e6f67e8ce29cb0d1f4af4ac7e34c570425f221d` check row semantics, automorphisms and exact cancellation. No floating optimization is part of the proof.
 
For a common two-valued triangle syndrome, each of the three defect families vanishes and the conditional triangle factor argument proves `G_S<=0`; (34) recovers the common-selector case of the two-syndrome theorem. For more syndrome values, (34) remains true but its explicit defects and the potentially positive `G_S` must be bounded; the two-syndrome conditional gate may not be imported for an arbitrary state variable. Thus (34) supplies a rigorous all-variable continuation target rather than a claim of a three-state no-go.
