# Two mandatory path vertices on length-six connector graphs

Status: **WRITTEN**, pending independent mathematical review. This strengthens `frontier-20261028-ph7-nine-edge-length-six-connector-separation-v1.md` (SHA256 `ca03dc12f5eb30d2c247b8b37d6cd77ed9568dd96bd25703e728b4a14f977a23`). It imports the just-written three-state Metzler sector lemma in `frontier-20261028-ph7-three-state-log-derivative-sector-lemma-v1.md` (SHA256 `c2c30e487654f1d09f3e4d3df2eab19ceb80d21185912564fd8d345551c3944e`), at its current unreviewed cut. It is not an unrestricted PH7 exclusion.

## 1. Spectral theorem

On the length-six connector graph with two disjoint directed triangles and a singleton, let `x` be the singleton's diagonal rate and `t` the diagonal rate of the unique triangle vertex omitted by the connector cycle. If the row generator has an algebraically repeated pair `-d +/- ib` with `d>0` and `b^2/d^2>1/2`, then **neither `-x` nor `-t` is an eigenvalue** of that generator.

Write the triangle polynomials as `A(y),B(y)`, with `B` the triangle containing the omitted vertex, and `w>0` for the connector-cycle product. Then

`P(y)=(y+x)*A(y)*B(y)-w*(y+t)`.

First, if `x=t`, factor `P=(y+x)*(A*B-w)`. The repeated nonreal root is a repeated root of `A*B-w`; at that root both triangle factors are nonzero and the logarithmic derivative gives `A'/A+B'/B=0`. Both imaginary parts are strictly negative by the imported lemma, a contradiction. Thus `x!=t`, and `P(-x)=-w*(t-x)!=0`.

Next, if `P(-t)=0`, then `(x-t)*A(-t)*B(-t)=0`. Since the diagonal rate `t` belongs to triangle `B`, `B(-t)=-w_B` is strictly negative; thus `A(-t)=0`. Put `A_2(y)=A(y)/(y+t)`. The same determinant identity factors as

`P(y)=(y+t)*[(y+x)*A_2(y)*B(y)-w]`.

At the repeated nonreal root, the bracket has a repeated root and its nonzero factors satisfy

`1/(y+x)+A_2'(y)/A_2(y)+B'(y)/B(y)=0`.

The first term has negative imaginary part. The other two do as well: the imported lemma applies both to a full 3-state Metzler determinant and to that determinant with any real-root factor removed. This is impossible. Hence `P(-t)!=0`, completing the theorem.

## 2. Actual PH support consequence

Suppose the target transfer of relative degree five is realized on this graph with nonnegative input/exit vectors. Then:

* At least one supported simple input-to-exit path visits the singleton vertex.
* At least one supported simple input-to-exit path visits the omitted triangle vertex.

These may be different supported paths; no common-path conclusion is asserted.

For either indicated vertex `v`, if every supported simple path avoided `v`, no supported path could have length below four (relative degree and positivity), and none could have length above five (there are only six other vertices). In the adjugate path expansion the principal complement has one or two vertices, includes `v`, and has no two-cycle; each term therefore has factor `y+u_v`. The target transfer forces its adjugate numerator to be a nonzero scalar multiple of the hidden quadratic `Q`, so `P(-u_v)=0`. This contradicts §1 for each of the two vertices. The graph condition, not an assumption of a particular path, supplies the no-two-cycle property.

The graph-specific theorem and its input-output caller do not require the pending universal nine-edge template. Applying them to every nine-transition PH7 with a length-six connector additionally requires that template, its capacity/overlap-budget inputs, and the separately supported irreducibility/Perron-normalization caller. No claim is made for length 3/4/5/7, for graphs with ten or more transitions, for complete 8/9 existence/exclusion, formal proof, novelty, or parent adoption.
