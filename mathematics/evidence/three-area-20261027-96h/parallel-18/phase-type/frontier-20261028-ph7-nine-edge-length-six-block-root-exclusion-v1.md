# A real-root exclusion interval for both triangle blocks

Status: **WRITTEN**, pending independent mathematical review. This strengthens the length-six rate-separation theorem using the real-root quotient part of `frontier-20261028-ph7-three-state-log-derivative-sector-lemma-v1.md` (SHA256 `c2c30e487654f1d09f3e4d3df2eab19ceb80d21185912564fd8d345551c3944e`). It is a graph-specific necessary condition, not an exclusion of the full length-six family or of PH7 at `8/9`.

## Theorem

For a row generator on the length-six connector graph with two disjoint directed triangles and singleton, let `x` be the singleton diagonal rate and `t` the diagonal rate of the one triangle vertex omitted by the connector cycle. Let `-r` be **any real eigenvalue of either actual 3-by-3 triangle block** (the block retains the full diagonal and only its internal edges). If the seven-state generator has an algebraically repeated eigenvalue `-d+ib` with `d>0` and `b^2/d^2>1/2`, then

`(x-d)^2>(t-d)^2` and `(r-d)^2>(t-d)^2`.

Equivalently, neither `x` nor any real decay rate of either triangle block belongs to the **closed interval** with endpoints `t` and `2d-t`.

Let `-r_B` be the Perron eigenvalue of the triangle `B` containing the omitted vertex. It additionally satisfies

`0<r_B<t` and `r_B+t<2d`.

In particular the omitted rate must satisfy `t<2d`.

## Proof

The triangle blocks are irreducible Metzler subgenerators with nonpositive row sums and a strict leak row. Consequently their spectral bounds are strictly negative and are real Perron roots. A positive Perron eigenvector in the block containing the omitted vertex gives `-r_B> -t`, since the omitted vertex has a positive internal outgoing edge; hence `0<r_B<t`.

Let `A(y),B(y)` be the triangle characteristic polynomials, with `B` the block containing the omitted vertex, and `w>0` the connector-cycle product. The full determinant is

`P(y)=(y+x)*A(y)*B(y)-w*(y+t)`.

At a repeated nonreal eigenvalue `lambda` the factors are nonzero and

`1/(lambda+x)+A'(lambda)/A(lambda)+B'(lambda)/B(lambda)-1/(lambda+t)=0`.

The imported three-state lemma states that the imaginary parts of `A'/A` and `B'/B` are strictly negative for `b>0`. Therefore `Im[1/(lambda+x)-1/(lambda+t)]>0`, or `(x-d)^2>(t-d)^2`.

Now select any real root `-r` of `A` or `B`, and factor that polynomial as `(y+r)C_2(y)`. The logarithmic derivative of `C_2` has strictly negative imaginary part by the same lemma; the other full triangle block and `1/(lambda+x)` also have negative imaginary parts. Hence the equation above forces

`Im[1/(lambda+r)-1/(lambda+t)]>0`,

which is exactly `(r-d)^2>(t-d)^2`. It applies with multiplicity even if a real root is repeated; only one factor is removed.

For the Perron root of `B`, `r_B<t`. Thus `(r_B-t)*(r_B+t-2d)>0` forces `r_B+t<2d`. Conjugation handles negative `b`. □

The condition on `x` recovers the earlier result at the larger domain `z>1/2`; the exclusion for **every** real block root and the Perron squeeze are additional. Neither a root-free block interval nor the path-cover restrictions in the preceding manuscript show that all remaining rates are impossible. The nine-edge-universal PH caller depends on the separately pending template/capacity/overlap chain and the supported Perron normalization. No input-output witness, complete 8/9 decision, executable proof, independent audit, or novelty claim is made.
