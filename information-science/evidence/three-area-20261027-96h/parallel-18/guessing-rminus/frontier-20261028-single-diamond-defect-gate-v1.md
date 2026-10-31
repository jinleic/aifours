# A single-diamond Ingleton gate for R-minus

**Status: WRITTEN with separately checked exact rational certificate and an exact FD counterexample.** This strengthens the structural conclusion of `frontier-20261028-two-ingleton-defect-gate-v1.md` (SHA-256 `3f9f543bb5893e26a5abecb21a5c81b6408214446dc495ea8c66747ea84f5f2b`). It does not establish an unrestricted `20/3` upper bound or a strict-gain law.

## Exact identity and necessary condition

Let `G` be the eight-element original-graph automorphism group in the preceding packets and use the same conditional Ingleton convention

\[
J(A,B;C,D\mid Z)=I(A;B\mid C,Z)+I(A;B\mid D,Z)
+I(C;D\mid Z)-I(A;B\mid Z).
\]

Set `J_1=J(2,4;1,3 | 5,6,7,8,9,10)`. For **every** finite entropy law satisfying all original R-minus graph FDs, the pinned certificate verifies the exact identity

\[
\frac23\sum_v H(X_v)-H(X_V)
=\sum_{i=1}^{62}a_i\,\overline{I_i}
+\frac13\,\overline{J_1},\qquad a_i>0.
\]

Bars are averages under `G`; the 62 named conditional mutual informations and rational positive coefficients are in the certificate. Three graph-FD rows also occur algebraically and vanish under the hypothesis. Therefore

\[
\overline{J_1}\le -3\left(H(X_V)-\frac23\sum_vH(X_v)\right).
\]

In particular, if `epsilon=H(X_V)-(20/3)max_v H(X_v)>0`, then `average_G J_1 <= -3 epsilon`; at least one of the following **eight specific** conditional diamond instances is `<= -3 epsilon`. Each row's conditioning set is the other six vertices.

| A,B | C,D | Conditioning vertices |
|---|---|---|
| 2,4 | 1,3 | 5,6,7,8,9,10 |
| 2,6 | 1,7 | 3,4,5,8,9,10 |
| 3,5 | 1,4 | 2,6,7,8,9,10 |
| 3,10 | 4,8 | 1,2,5,6,7,9 |
| 4,9 | 3,8 | 1,2,5,6,7,10 |
| 5,7 | 1,6 | 2,3,4,8,9,10 |
| 6,10 | 7,8 | 1,2,3,4,5,9 |
| 7,9 | 6,8 | 1,2,3,4,5,10 |

The previous **two-shape** gate remains independently valid and gives a stronger magnitude `-4 epsilon` on one of its two shapes; this single-shape gate instead forces a negative **diamond** instance. The four unconditioned vertices in each row induce a `K4` minus its `A,B` edge. Conditional on the other six vertices, the graph FDs make both `A` and `B` functions of `C,D`, and each of `C,D` a function of the other three. These dependencies alone do not force Ingleton nonnegative, as shown by the explicit witness in the preceding packet.

For representable ranks, Ingleton is nonnegative, so this 66-row certificate independently gives `h(V)<=(2/3)sum_v h(v)` and the exact finite-field vector-linear/affine optimum `20/3`. General entropic Ingleton can be negative, so no unrestricted rank upper bound follows.

## Even the averaged diamond defect can be negative

A different law on the same four original-graph FD words `0,6,3,15` has weights `(21,4,16,9)/50`. Its vertex 1 is fair, all variables are binary, and therefore `M=1` bit. It satisfies all 60 vertex/word-pair FD conditions. Exact integer entropy products give

\[
\overline{J_1}<-\frac3{400},\qquad
\overline{J_2}=0,\qquad
2\overline{J_1}+\overline{J_2}<-\frac3{200}\ \text{bits}.
\]

This rules out proving the unrestricted `20/3` bound merely by asserting either `average_G J_1>=0` or `2 average_G J_1+average_G J_2>=0`. It does **not** contradict the exact balance identities: the positive CMI terms compensate. Nor is it a strict-gain example: its four-point support has joint entropy at most two bits while `M=1`.

For the exact sign, sum the eight permuted `J_1` entropy expressions, giving integer coefficients `c_S`. With `P_S=product_k n_{S,k}^{n_{S,k}}` for the projection counts of the four weighted words, the checker forms `L=product_{c_S>0} P_S^{c_S}` and `R=product_{c_S<0} P_S^{-c_S}`. It checks `L>8R`; since the denominator is 50 and eight automorphisms were summed, this gives `average_G J_1<-3/(8*50)`. For `J_2`, aggregating entropy coefficients by identical support-projection partitions gives an empty remainder, so its average is exactly zero for every distribution on these four words.

## Evidence and scope

* Single-shape LP proposal `frontier-20261028-one-ingleton-defect-search.py` SHA-256 `c808f816704a4f83f80e632f3ac65033ea660b758b4a805705a07f6fefb2eb81`; float result SHA-256 `76473f469e3690b02add60d24a5f9aefae08074e8c34ad07b5b718157d55cd00`. Its first candidate has the exact rational identity below; the second shape alone received a floating infeasibility status, which is not used as proof.
* Exactifier `frontier-20261028-diamond-ingleton-exactify.py` SHA-256 `36ed5ad72c13a002b8dc4c24c0f35d42833ada72dc217271ee393fbf7d48766f`; certificate `frontier-20261028-diamond-ingleton-exact-dual-v1.json` SHA-256 `3704cb337dba009deffece5ab4e66932bf4a315e01d2e8e6d5e35567dbc6f90f`.
* Independent checker `frontier-20261028-diamond-ingleton-independent-check.py` SHA-256 `eede3dab5cfe1135fee27d526d3e890ac031be8ce1de5725481e1bf3ef1b74b7`; receipt SHA-256 `0ae781de13843b5b64145b7e466ce5324ed022ed2d24111f472f51a4d0c075a1`. It reconstructs graph, group, 185 entropy orbits and all 66 named rows, checks signs and exact coefficients, proves the q8 baseline by its ten parity checks, and rejects five mutation controls.
* Averaged-defect witness checker `frontier-20261028-negative-averaged-diamond.py` SHA-256 `97c11ec6a28413692aebef1693ae56faaeb82d4f607f27a8da9e6ca1166a3ff9`; receipt SHA-256 `8c6d55a95e81e4068b520075ae421537aabf4aecfdeab5952e6ecfad8a35e743`. It rebuilds the graph group, checks 60 FD conditions, computes both orbit-averaged entropy combinations and checks the integer inequality.

No formal proof, cross-model review or novelty clearance was performed. This is an exact conditional obstruction and a counterexample to simple defect-sign shortcuts, not a solution of the original guessing-number gap.
