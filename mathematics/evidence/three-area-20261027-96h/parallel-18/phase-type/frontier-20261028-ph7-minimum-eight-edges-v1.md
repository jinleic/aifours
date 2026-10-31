# Every PH7 representation for z>1/2 has at least eight positive transitions

**WRITTEN CANDIDATE; review, parent adoption and novelty clearance pending.** MathResearch96h-2; this is an additive application of `frontier-20261028-ph7-global-irreducibility-v1.md` SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`. Its full Perron/trace/SCC proof is a named dependency, not an already independently accepted theorem.

## Claim

For z=b^2/(a-c)^2>1/2, any actual PH representation of H using at most seven states has exactly seven reachable states and **at least eight positive off-diagonal matrix entries**. This applies in particular at z=8/9. The statement is a graph restriction, NOT a proof that seven states are impossible or possible at 8/9.

The edge bound is sharp somewhere in the family: at the exact algebraic endpoint of the separate v4 construction `frontier-20261028-ph7-two-cycle-endpoint-v4.md` SHA256 `4f63347198b12ce6dfefb5c7c94adf95fcc262234d29ce055e6f789bff27e191`, read together with mandatory correction `frontier-20261028-ph7-two-cycle-endpoint-v4-erratum-v1.md` SHA256 `b5526a1556a61786c5cc382e924087a318b31b6640b35d30a41fe9d3fe22cc30`, the seven-state SAME matrix has exactly six positive superdiagonal edges and two positive return edges; its other two optional feedbacks vanish. That upper example is an unadopted separate candidate, and its existence is not needed for the lower edge bound.

## Proof of the lower bound

The named irreducibility theorem implies the graph is strongly connected on all seven states. Every vertex must have at least one outgoing off-diagonal edge, so there are at least seven edges. If exactly seven, every vertex has outdegree exactly one. Strong connectivity then forces a single directed cycle containing all seven vertices.

Consider a real n-by-n matrix M whose off-diagonal graph is a single directed n-cycle, with n>=2 and all cycle entries positive. After merely relabeling vertices, its characteristic polynomial has the literal form

    P(y)=product_{j=1}^n (y+u_j) - K,

where every u_j is real and K>0 is the product of the n cycle weights. This follows directly from the determinant permutation expansion: the diagonal permutation and the full-cycle permutation are the only nonzero terms. The diagonal signs and the sizes of the u_j are immaterial for the next step.

Every nonreal root lambda of P is SIMPLE. Since each `lambda+u_j` is nonzero, differentiation gives

    P'(lambda) = [product_j(lambda+u_j)] sum_j 1/(lambda+u_j).

For `Im(lambda)>0`, every summand in the last sum has strictly negative imaginary part, namely `-Im(lambda)/|lambda+u_j|^2`; for `Im(lambda)<0` every summand has strictly positive imaginary part. Their sum cannot vanish, and the prefactor is nonzero. Hence P'(lambda)!=0.

But the target transfer has poles `-a +/- ib`, each of order2. Each is necessarily an eigenvalue of T with algebraic multiplicity at least2. A single directed cycle cannot have such an eigenvalue, contradiction. Therefore the strongly connected seven-state graph needs at least eight off-diagonal positive entries. □

No eigenvector diagonalizability or cancellation assumption was used: pole order2 always forces characteristic algebraic multiplicity at least2. Positive diagonal similarity preserves which off-diagonal entries are positive, so the v4 endpoint's reported exact eight-edge graph stays eight-edge after PH normalization. Earlier whole-interval v4 matrices can have additional positive edges; the sharp example is the endpoint only.

## Nonclaims

The z>1/2 structural lower conclusion depends on the separately frozen WRITTEN irreducibility candidate. Its proof of the single-cycle lemma is elementary and works for all n, but the present application has not been independently reviewed. No classification/exclusion of all eight-edge digraphs, 8/9 witness, min8 proof, novelty, executable checking, Lean, or human/cross-vendor review is claimed. Earlier held results remain nonpremises and historic process qualifications remain.

END — at least eight positive transition edges for PH7 in the post-PH6 regime; eight achieved by the separately conditional v4 endpoint.
