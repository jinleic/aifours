# A joint Perron/singleton gap for length-six connectors

Status: **WRITTEN**, pending independent mathematical review. This is a new exact spectral restriction on both length-six connector shapes. It imports the full-block and real-root-quotient conclusions of `frontier-20261028-ph7-three-state-log-derivative-sector-lemma-v1.md` (SHA256 `c2c30e487654f1d09f3e4d3df2eab19ceb80d21185912564fd8d345551c3944e`) and the elementary Perron squeeze reconstructed below. It does not by itself exclude the whole graph family or decide PH7 at `8/9`.

## Theorem

Consider a row generator with two vertex-disjoint directed triangles, a singleton, and a directed connector cycle of length six. Let `x>0` be the singleton diagonal rate; let `t>0` be the sole omitted triangle-vertex diagonal rate; let `-r_B` be the Perron eigenvalue of the triangle block **containing** that vertex, and `-r_A` the Perron eigenvalue of the other triangle block. If the seven-state generator has an algebraically repeated eigenvalue `-d+ib` with `d>0` and `z=b^2/d^2>1/2`, then

`1/[b^2+(x-d)^2] + 1/[b^2+(r_A-d)^2] < d^2/[b^2*(d^2+b^2)]`.

Consequently both `x` and `r_A` satisfy the individual algebraic consequences

`|x-d| > z*d`, and `|r_A-d| > z*d`.

At the requested `z=8/9`, this forces

`x<d/9 or x>17d/9`, and independently `r_A<d/9 or r_A>17d/9`.

These disjunctions are only necessary; no branch is claimed feasible. The joint reciprocal inequality is strictly stronger than merely taking the two separate disjunctions.

## Proof

The two triangle blocks are irreducible Metzler subgenerators with a strict leak row, so their Perron decay rates `r_A,r_B` are positive. The block containing the omitted vertex has a positive off-diagonal internal transition in that vertex's row; the positive Perron eigenvector therefore implies `r_B<t`.

Let `A(y),B(y)` be the two triangle characteristic polynomials, and let `w>0` be the connector cycle's transition product. The exact directed-cycle determinant is

`P(y)=(y+x)*A(y)*B(y)-w*(y+t)`.

At the repeated nonreal eigenvalue `lambda=-d+ib`, every factor is nonzero and

`1/(lambda+x)+A'/A+B'/B-1/(lambda+t)=0`,

with the derivatives evaluated at `lambda`. Factor the real Perron roots: `A=(y+r_A)A_2`, `B=(y+r_B)B_2`. The imported lemma gives strictly negative imaginary parts for both `A_2'/A_2` and `B_2'/B_2`, and the singleton term is also strictly negative. For `b>0`, writing `v_s=b^2+(s-d)^2`, the imaginary equation therefore implies the strict inequality

`1/v_t > 1/v_x + 1/v_{r_A} + 1/v_{r_B}`.

In particular `1/v_t>1/v_{r_B}`, i.e. `(r_B-d)^2>(t-d)^2`. Since `r_B<t`, this yields `r_B+t<2d`. Combining the two inequalities shows `0<r_B<d`, so `v_{r_B}<d^2+b^2`. Also `v_t>=b^2`. Subtracting the positive Perron term gives

`1/v_x+1/v_{r_A} < 1/b^2-1/(d^2+b^2) = d^2/[b^2*(d^2+b^2)]`,

which is the joint inequality. Each reciprocal on the left is positive, so either one individually is strictly below the right-hand side. Inverting and subtracting `b^2=z*d^2` gives the displayed bounds `|x-d|^2, |r_A-d|^2 > z^2*d^2`. Conjugation treats `b<0`. □

The graph-specific theorem is independent of the pending global nine-edge template. Applying it to every critical PH7 with nine transitions and length-six connector additionally requires that template, its triangle-capacity/overlap-budget dependencies, and the separately supported Perron normalization. The new sector lemma and this theorem have not yet received independent review. There is no proposed numerical state, existence/exclusion verdict, ten-edge result, formal proof, novelty clearance, or parent adoption.
