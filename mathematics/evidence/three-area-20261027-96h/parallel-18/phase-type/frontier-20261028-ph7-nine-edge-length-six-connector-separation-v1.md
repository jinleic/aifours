# A strict separation and input-output constraint for length-six connectors

Status: **WRITTEN**, pending independent review. This is a new exact restriction on both remaining six-edge-connector shapes; it does not exclude either shape in full, all nine-edge graphs, or PH7 at `8/9`. It imports the full-three-cycle logarithmic-derivative lemma from `frontier-20261028-ph7-nine-edge-hamiltonian-cycle-exclusion-v1.md` (SHA256 `84b3075f370cd13b04ae66d120878eeba5b0f41b6bd5ac79570d96f9f36c1b54`) at its current unreviewed written status.

## 1. Spectral separation

Consider a row generator with the two disjoint directed triangles and singleton connector graph specified in the Hamiltonian manuscript, and suppose the connector cycle has length six. Let `x>0` be the singleton diagonal rate and `t>0` the diagonal rate of the **one triangle vertex omitted** from that connector cycle. If `-d+ib` is an algebraically repeated eigenvalue with `d>0` and `b^2/d^2>=3/4`, then

`(x-d)^2 > (t-d)^2`, equivalently `(x-t)*(x+t-2d)>0`.

In particular `x!=t` and `x+t!=2d`. Moreover, the separately written one-omission result of `frontier-20261028-ph7-nine-edge-omitted-rate-obstruction-v1.md` (SHA256 `0660efa2450da347f5f74a45d55ff4af6127254c899ae6c6ecc3ce867db745cf`) gives `t<2d`. Combining the two conditions places `x` strictly outside the closed interval with endpoints `t` and `2d-t`.

Proof. Scale by `d` and write `y=-1+ib/d`. If `A(y),B(y)` are the two triangle polynomials from the imported lemma and `w>0` is the length-six connector cycle product, the directed-cycle determinant is

`P(y)=(y+x)*A(y)*B(y)-w*(y+t)`.

Here and below `x,t` have been divided by `d`. At a nonreal root, neither `y+x` nor `y+t` is zero, and the root equation implies `A(y),B(y)!=0`. At a repeated root, differentiating gives

`A'(y)/A(y)+B'(y)/B(y) = 1/(y+t)-1/(y+x)`.

The left side has strictly negative imaginary part by the full-three-cycle lemma. Writing `h=Im(y)>0` and `v_r=(r-1)^2+h^2`, the right side has imaginary part `h*(1/v_x-1/v_t)`. Thus `v_x>v_t`, exactly the asserted strict separation. Conjugation gives the same conclusion when the imaginary part is negative.

## 2. Every PH realization must use the singleton in a supported path

At `z=8/9`, assume in addition that nonnegative input and exit vectors produce the target transfer of relative degree five, so its monic hidden quadratic `Q` satisfies `P(y)=D_z(y)*Q(y)` and the adjugate numerator is a positive scalar times `Q(y)`. Then **at least one supported simple input-to-exit path must visit the singleton vertex**.

If none visited it, each supported simple path would have length at most five, and no supported path could have length less than four because off-diagonal rates and input/exit weights are nonnegative. For a path of length four, the adjugate expansion multiplies its positive path weight by the determinant on the two unvisited vertices; that determinant has a factor `(y+x)` because there is no two-cycle. For a path of length five, the only unvisited vertex is the singleton, again giving the factor `(y+x)`. Therefore the complete adjugate numerator, and hence `Q`, is divisible by `y+x`. Since `P=D_z Q`, `P(-x)=0`. But the exact determinant formula gives

`P(-x)=-w*(t-x)`,

so `t=x`, contradicting §1. Thus a supported path visiting the singleton is necessary.

As a concrete support corollary, orient the contracted component cycle as triangle `A -> B -> singleton -> A`. All simple paths from `A` to `B` avoid the singleton. Therefore no critical representation on a length-six connector graph can have its entire input support in `A` and its entire exit support in `B`. The singleton-path result allows other support patterns and is not their classification or exclusion.

The graph-specific conclusions hold without the pending global template. Applying them to every candidate nine-transition PH7 additionally requires the separate, unadopted template and its capacity/overlap-budget inputs plus the separately supported irreducibility normalization. No numerical state, formal proof, independent audit, novelty, parent adoption, or unrestricted PH7 conclusion is claimed.
