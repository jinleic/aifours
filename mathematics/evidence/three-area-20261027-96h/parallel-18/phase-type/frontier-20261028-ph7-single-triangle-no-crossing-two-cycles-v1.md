# A critical single triangle needs a bidirectional edge crossing its boundary when there is no 4-cycle

**NEW ALL-TOPOLOGY WRITTEN APPLICATION, conditional on the named exact one-triangle certificate; independent peer review pending.** MathResearch96h-2. This strictly strengthens `frontier-20261028-ph7-single-triangle-disjoint-two-cycles-v1.md` SHA256 `2719cfb37d7cf77b44a8a707e8f181ccdd86932fd67bfdf35ca25bb57a894f70`: 2-cycles INTERNAL to the triangle are now allowed, as are arbitrary 2-cycles entirely outside. The only forbidden 2-cycles in the hypothesis are those CROSSING the triangle boundary.

## Claim

At z=8/9, an irreducible seven-state Metzler matrix of spectral bound0, whose actual characteristic polynomial contains `D(y)=y[(y+1)^2+8/9]^2`, cannot have all three properties:

1. exactly one directed 3-cycle C;
2. no directed 4-cycle; and
3. no directed 2-cycle with one endpoint in C and the other outside C.

Thus any critical PH7 candidate with exactly one triangle and no 4-cycle must have a **bidirectional crossing edge between that triangle and an outside state**. Arbitrary 2-cycles entirely within C or entirely outside it and arbitrary longer cycles are permitted. This is an exact necessary graph condition, not a full seven-state exclusion.

## 1. Symmetrize and split into two strictly stable blocks

Use positive Perron similarity to make G a row generator. Let S be the symmetric geometric-mean matrix `S_ii=G_ii`, `S_ij=sqrt(G_ij G_ji)`. The no-crossing-2-cycle hypothesis gives the block split

    S = S3 direct-sum S4,

where S3 is indexed by the triangle and S4 by the other four vertices. Both blocks are strictly negative definite: for `A=kI+G>=0` irreducible, every proper principal block has Perron radius strictly below k, and geometric-mean symmetrization does not increase that radius by Cauchy–Schwarz (a reducible principal block can be approximated by strictly positive matrices). Thus `-S3,-S4` have positive real eigenrates.

S has no directed triangle: a triangle of bidirectional S edges would give both orientations as directed 3-cycles of G, contradicting uniqueness. It has no 4-cycle by the hypothesis on G. The characteristic coefficients of G and S through y3 therefore differ ONLY in the unique triangle contribution: the 2-cycle and disjoint 2+2 products coincide exactly.

Write the three positive eigenrates of `-S3` as `lambda1,lambda2,lambda3`, and the four positive eigenrates of `-S4` as `mu1,...,mu4`. Their product and sums are actual block invariants. The unique triangle edge product is w>0, and the sum of diagonal escape rates outside it is exactly `tr(-S4)=mu1+...+mu4`. Consequently the high characteristic coefficients of G are those of the seven-positive-rate product `product(y+lambda_i) product(y+mu_j)` minus the unique triangle corrections `w` at y4 and `w sum(mu_j)` at y3.

## 2. The actual triangle product fits the effective three-rate bound

Label the unique oriented triangle 1->2->3->1. Let its original diagonal escape rates be u1,u2,u3 and define the forward/backward row fractions

    p_i=G_(i,i+1)/u_i,     q_i=G_(i,i-1)/u_i,      p_i+q_i<=1,

with cyclic indices. At least one q_i=0, otherwise the reverse triangle would be a second directed 3-cycle. The actual triangle product is `w=(u1u2u3)p1p2p3`.

Because the symmetric 3-block has no triangular off-diagonal cycle, its determinant is

    det(-S3)/(u1u2u3)=1-[p1 q2+p2 q3+p3 q1].

Use `q_(i+1)<=1-p_(i+1)` and the exact identity

    1-sum_i p_i(1-p_(i+1))-p1p2p3
        =(1-p1)(1-p2)(1-p3)>=0.

It follows that

    0 < w <= det(-S3)=lambda1 lambda2 lambda3.

Hence `theta_eff=w/(lambda1 lambda2 lambda3)` belongs to(0,1]. This is a rate-independent actual row-tie inequality, not an assumed equality of the original diagonal and symmetric eigenrates.

## 3. Apply the exact full-theta spectral certificate

The preceding high coefficient identities are exactly the algebraic input of `frontier-20261028-ph7-one-triangle-full-critical-exclusion-v1.md`, SHA256 `2e30b352597880b78bfc59baa3adead91e4d4f0f1717a8cf7f684cee0a92decc`: seven positive rates partitioned into three whose product bounds w and four whose sum is the triangle's outside coefficient, with `theta_eff in[0,1]`. That source's exact five-dimensional Bernstein certificate excludes the required real outer sum/product for EVERY such choice. The coefficient-interface application needs no claim that the symmetric eigenvectors are actual PH states. Contradiction. □

## Review boundary

A disjoint review must check the proper-principal Perron comparison, triangle-block determinant signs, the cyclic product inequality, and the graph-independent high-coefficient interface of the cited full-theta certificate. No new machine computation, full critical PH7 exclusion, minimum8, global bound, novelty, or historical process repair is claimed.

END — a unique critical triangle without a 4-cycle must participate in at least one 2-cycle crossing to an outside state.
