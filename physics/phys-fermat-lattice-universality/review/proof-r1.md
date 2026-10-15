# Every covolume-pi lattice occurs: a classical existence proof

Snapshot: 2026-10-14 (America/Los_Angeles).

## Claim and evidence boundary

**Theorem U.** For every full-rank lattice `Lambda` in the oriented Euclidean plane with covolume `pi`, there is an irrational badly approximable `alpha in (0,1)` such that, for every rotation `S in SO(2)` and every `b in R^2`, `S Lambda+b` is a Chabauty–Fell limit of translates of

`X_alpha = {sqrt(n) exp(2*pi*i*n*alpha) : n=1,2,...}`

by translation vectors whose norms tend to infinity. The same `alpha` works for all these rotations and translates of the chosen lattice. It may depend on the lattice's shape. The translations contain **no rotations or dilations**.

This is the exact universal-existence question in Tevet's September 2025 preprint, Further Questions p. 12, strengthened only by spelling out rotation/translation freedom. It is not the full elastic-energy or chirality conjecture in Cao's book chapter. The older Fermat-tail density law is not claimed as a discovery.

**Evidence label: Certification (written classical proof).** Historical eligibility comes from an explicit primary open statement, not a search miss. Worldwide priority and publication acceptance remain separate from correctness. The initial proof below is awaiting the separately recorded independent review and finite smoke; those are not yet being claimed as completed.

## 1. Definitions and exact imported result

Write `Bad` for the set of real irrational numbers `x` for which there is `c>0` such that `|x-p/q| >= c/q^2` for all integers `p` and `q>=1`. Equivalently, the positive digits of the infinite simple continued fraction of `x` are bounded. This bounded-digit criterion is stated in Tevet §4, p. 6; the elementary continued-fraction identities used below are also derived where needed. Integer translation and negation preserve `Bad` directly from its definition.

The non-elementary imported input is **McMullen's absolute-winning theorem**, with its exact accompanying invariances:

1. For a hyperbolic lattice `Gamma` with a cusp at infinity, the set `D(Gamma)` of endpoints of bounded projected geodesic rays is absolutely winning. For `Gamma=SL_2(Z)`, this set is exactly `Bad`. This is Theorem 1.3 and the preceding identification, author manuscript p. 3.
2. An absolute-winning subset of `R^n` remains absolute winning under any global quasisymmetric homeomorphism of `R^n`. This is Theorem 2.2, manuscript p. 5.
3. Countable intersections of absolute-winning sets are absolute winning: §1, “Absolute winning,” property (2), p. 3. Such a set meets every nonempty open interval: start the defining game with Bob's closed interval inside that open interval and use a legal play with radii tending to zero.

Primary source: Curtis T. McMullen, *Winning sets, quasiconformal maps and Diophantine approximation*, author manuscript dated 11 August 2009; published in *Geometric and Functional Analysis* (2010), DOI [10.1007/s00039-010-0078-3](https://doi.org/10.1007/s00039-010-0078-3). [Author PDF](https://abel.math.harvard.edu/~ctm/papers/home/text/papers/winning/winning.pdf), pinned locally as `source/mcmullen-winning.pdf`.

The proof does **not** import a claim that a generic dense geodesic is bounded, a symbolic-dynamics specification theorem, or Tevet's shortest-neighbor Proposition 8. It does not infer local density from global Hausdorff dimension alone.

## 2. Put an arbitrary lattice into two badly approximable ratios

Identify the plane with `C`. Choose any negatively oriented basis `V,W0` of `Lambda`, so `det(V,W0)=-pi`. Adding an integer multiple of `V` to `W0` changes neither the lattice nor the determinant. Choose that integer large enough that the resulting basis `V,W` satisfies

`W/V = x-i*h`, with `x>1`, `h>0`.

Indeed `h=pi/|V|^2`. For a real parameter

`h/(x+1) < t < h/x`,

put `A=|V|/sqrt(1+t^2)`, `C=t*A`, and choose the rotation `R` of angle `arg(V)-arctan(t)`. Then

`R^(-1)V = A+i*C`,

`R^(-1)W = (x-i*h)(A+i*C) = A*(x+h*t) + i*A*(x*t-h)`.

Consequently

`R^(-1)V = (A,C)`,  `R^(-1)W = (A*beta,-C*u)`,

where

`beta=x+h*t > 1`,  `u=h/t-x in (0,1)`.

The admissible beta interval is the nonempty open interval

`J = (x+h^2/(x+1), x+h^2/x)`.

On it,

`u=g(beta)=h^2/(beta-x)-x`,  `g'(beta)=-h^2/(beta-x)^2`.

Choose a nondegenerate closed interval `[a0,b0]` strictly inside `J`. Extend `g` from this interval to the whole real line using its tangent line at `a0` to the left and its tangent line at `b0` to the right. The extension `G` is a decreasing `C^1` bijection, and everywhere

`0 < h^2/(b0-x)^2 <= |G'| <= h^2/(a0-x)^2 < infinity`.

Thus `G` and its inverse are globally bi-Lipschitz, hence quasisymmetric. McMullen's results imply that

`Bad intersect G^(-1)(Bad)`

is absolute winning and therefore meets `(a0,b0)`. Choose `beta` in that intersection and set `u=g(beta)`. Both numbers are badly approximable, while every strict geometric inequality remains valid. Orientation reversal is allowed by McMullen's metric definition of quasisymmetry; alternatively apply the theorem to `-G`, since `-Bad=Bad`.

Finally the determinant gives the exact identity

`pi = A*C*(beta+u)`.                                                   (1)

This proves the required geometric lemma for **every** target lattice, including highly elongated and nonalgebraic ones. No computability assumption on the entries of its basis was used. The winning-set selection is an existence argument, not an advertised finite algorithm for arbitrary real input.

## 3. One bounded continued fraction realizes the two ratios

Set `a=floor(beta)` and `r=beta-a`. Because `beta` is irrational, `a>=1` and `0<r<1`; both `r` and `u` are badly approximable. Write

`r=[0;r1,r2,...]`,  `u=[0;u1,u2,...]`.

There is a finite integer `M` bounding `a`, `1`, every `ri` and every `ui`.

Construct one infinite digit word as follows. Starting with an empty prefix, at stage `k>=1`, let `ell` be the length already written. Choose `epsilon_k in {0,1}` so that `ell+epsilon_k+k` is even. Append `epsilon_k` copies of the digit **1**, then the block

`r_k,r_(k-1),...,r_1, a, u_1,u_2,...,u_k`.                             (2)

Let `j_k=ell+epsilon_k+k`, the position immediately before the central digit `a`. Thus `j_k` is even and the central digit has position `j_k+1`. The padding is **before** the prescribed block, so it does not damage either local digit window.

Let `alpha=[0;d1,d2,...]` be the number represented by the resulting infinite word. Every digit lies in `{1,...,M}`, so `alpha` is irrational and badly approximable. This is one fixed number, not a new number at each stage, and the bound `M` does not increase with `k`.

Use convergents `p_j/q_j=[0;d1,...,dj]`, with `p_-1=1,p_0=0,q_-1=0,q_0=1`. Define

`r_j=q_(j-1)/q_j=[0;d_j,d_(j-1),...,d_1]`,

`u_j=[0;d_(j+2),d_(j+3),...]`.

At `j=j_k`, these have initial digit strings `r1,...,rk` and `u1,...,uk`, respectively. To check convergence without invoking a coding theorem, recall the elementary cylinder formula. If `P_l/Q_l` are the convergents of `[0;e1,...,el]`, all continuations are

`(P_l+eta*P_(l-1))/(Q_l+eta*Q_(l-1))`,  `0<=eta<=1`.

The endpoint difference is

`1/(Q_l*(Q_l+Q_(l-1))) <= 1/Q_l^2`,

because `|P_l*Q_(l-1)-P_(l-1)*Q_l|=1`, obtained immediately from the convergent recurrence. Positive digits make `Q_l` grow at least as Fibonacci denominators. Therefore, along the specified even indices,

`r_j -> r`,  `u_j -> u`,  `q_(j+1)/q_j=a+r_j -> beta`.                 (3)

For completeness, the complete quotient at position `j+1` is `a+u_j`, so

`alpha=(p_j*(a+u_j)+p_(j-1))/(q_j*(a+u_j)+q_(j-1))`.

Subtract `p_j/q_j`, use the determinant recurrence, and use even `j` to get

`c_j=q_j*(q_j*alpha-p_j)=1/(a+u_j+r_j) -> c=1/(beta+u)`,                (4)

`q_(j+1)*alpha-p_(j+1)=-u_j*(q_j*alpha-p_j)`.                          (5)

The signs and parity in (4)–(5) are essential; they are not recovered from squared quantities.

## 4. The exact local lattices approach the chosen basis

For a positive integer `n`, let `rho=sqrt(n)` and define the full lattice

`L_n(alpha) = {(q/(2*rho), 2*pi*rho*(q*alpha-p)) : (q,p) in Z^2}`.     (6)

Its covolume is exactly `pi`. For the even index `j=j_k`, the integer pairs `(q_j,p_j)` and `(q_(j+1),p_(j+1))` have determinant `+1`. Hence they form an **entire basis**, not merely two independent vectors in a possible sublattice, of the integer input lattice in (6).

Choose `n_k` to be a nearest positive integer to `(q_j/(2*A))^2`, discarding finitely many early terms if necessary. Then `n_k -> infinity` and

`q_j/(2*sqrt(n_k)) -> A`.

In the basis above, `L_(n_k)` has matrix

`B_k = [[q_j/(2*sqrt(n_k)), q_(j+1)/(2*sqrt(n_k))],`
`       [2*pi*sqrt(n_k)*(q_j*alpha-p_j),`
`        2*pi*sqrt(n_k)*(q_(j+1)*alpha-p_(j+1))]]`.

Equations (3)–(5) and (1) yield

`B_k -> B = [[A,A*beta],[C,-C*u]]`,  `det(B)=-pi`.                     (7)

Indeed the first lower entry tends to `pi*c/A=C`, and the second tends to `-C*u`. This proves an actual limit to the chosen lattice coordinates, not just a dense approximation among different angles.

Convergence of nonsingular basis matrices implies local convergence of their lattices: every `B*z`, `z in Z^2`, is approximated by `B_k*z`; conversely, bounded `B_k*z_k` have bounded integer `z_k` since the inverses `B_k^(-1)` are uniformly bounded, so every convergent subsequence has a further subsequence with constant `z_k`. Thus `L_(n_k) -> B Z^2` in the Chabauty–Fell topology.

## 5. Uniform local comparison with the actual spiral

This elementary lemma was developed jointly with the independent companion classification worker; it is written out here so that the proof and reviews are self-contained. No companion implementation is imported or copied.

Let `P_n=sqrt(n)*exp(2*pi*i*n*alpha)`, `rho=sqrt(n)` and

`Y_n=exp(-2*pi*i*n*alpha)*(X_alpha-P_n)`.

The rotation in this definition is an **analysis coordinate frame**, not an allowed transformation of the spiral in the theorem.

**Forward bound.** Let `v=(q/(2*rho),2*pi*rho*(q*alpha-p)) in L_n` have norm at most `R`, and suppose `rho>=4*R`. Then `n+q>=n/2>0`, so the corresponding index is allowed. With `theta=2*pi*(q*alpha-p)` and `s=sqrt(n+q)`,

`Ypoint=s*exp(i*theta)-rho`,  `v=q/(2*rho)+i*rho*theta`.

Here `|q|<=2*R*rho`, `|theta|<=R/rho`, `s<=3*rho/2`, and

`|s-rho|<=2*R`,

`|s-rho-q/(2*rho)|=q^2/(2*rho*(s+rho)^2)<=2*R^2/rho`.

Using `|exp(i*theta)-1-i*theta|<=theta^2/2`,

`|Ypoint-v| <= 2*R^2/rho + 2*R^2/rho + 3*R^2/(4*rho)`
`             <= 5*R^2/rho`.                                         (8)

Also `|q*alpha-p|<=1/(8*pi)<1/2`, so `p` is the unique nearest integer to `q*alpha` in this local range.

**Reverse bound.** If `Ypoint=s*exp(i*theta)-rho` has norm at most `R` and `rho>=12*R`, choose the principal argument `theta=arg(rho+Ypoint)` and the integer `p` with `theta=2*pi*(q*alpha-p)`. Since `|s-rho|<=R`,

`|q/(2*rho)|<=R+R^2/(2*rho)<=25*R/24`.

The real part of `rho+Ypoint` is positive, and

`|theta|<=R/(rho-R)`, hence `|rho*theta|<=12*R/11`.

Thus the corresponding `v` has norm less than `3*R`. Apply (8) at radius `3*R` to obtain

`|Ypoint-v|<=45*R^2/rho`.                                             (9)

These are neighborhood inclusions into the **full** opposing sets. They are not an incorrect same-radius truncated Hausdorff claim, which would be sensitive to points on the ball boundary. For each fixed `R`, the errors tend to zero. Equations (8)–(9) and the basis convergence in (7) therefore imply `Y_(n_k) -> B Z^2`.

## 6. Physical orientation without rotating any translate

For any positive integers `m,n`, the model lattices obey the exact relation

`L_m = diag(sqrt(n/m),sqrt(m/n))*L_n`.                                 (10)

Thus changing `n_k` by an integer `b_k` with `b_k=o(n_k)` does not alter the limit in (7).

We need the following elementary uniform form of irrational-rotation density. For an irrational `alpha` and any `epsilon>0`, some finite set `{exp(2*pi*i*b*alpha):0<=b<=H}` is an epsilon-net of the unit circle. One proof uses pigeonhole to find `0<||q*alpha||<delta`, then uses the points at indices `0,q,2q,...,floor(1/||q*alpha||)*q`; they traverse a circle grid in one of the two directions with gaps at most `||q*alpha||`. Take `delta` arbitrarily small. Rotating this finite net by any starting phase preserves the net property.

Let `H_k=floor(sqrt(n_k))`. Then `H_k -> infinity` and `H_k/n_k -> 0`. For any desired rotation `R_theta`, choose `0<=b_k<=H_k` so that

`exp(2*pi*i*(n_k+b_k)*alpha) -> exp(i*theta)`.

The finite-net argument gives this for the whole sequence, not only a subsequence; for example choose a distance-minimizing index in each finite window. Set `m_k=n_k+b_k`. Equation (10) preserves the model-lattice limit, and the local comparison applies equally at `m_k`. Therefore

`X_alpha-P_(m_k) -> R_theta*B Z^2`.                                   (11)

Take `R_theta=R` from §2 to obtain `Lambda`. Every other physical rotation is obtained by choosing another target angle, with the **same** `alpha`. Adding a fixed vector `b` to the translating maps gives `R_theta*B Z^2+b`, and

`|-P_(m_k)+b| >= sqrt(m_k)-|b| -> infinity`.

All transformations in (11) are translations. The coordinate rotation in §5 disappears through the selected phases; there is no post-hoc rotation or dilation. This completes the proof of Theorem U.

## 7. What was and was not settled

- **Settled by the written proof:** the full all-lattice existence statement with covolume exactly `pi`, a single fixed badly approximable angle for each shape, translation-only escape to infinity, and arbitrary orientation/affine offset.
- **Not asserted:** one badly approximable angle works for every lattice shape; an effective uniform bound on partial quotients independent of the target; a finite algorithm selecting the winning-set point for arbitrary noncomputable real input; optimal packing or elastic-energy selection; the book's cone chirality conjecture.
- **Why the core obligation is bounded:** two simultaneous badly-approximable real ratios are selected by a published winning-set theorem; an explicit bounded-alphabet block construction realizes them. No bounded-orbit realization or generic-geodesic assumption remains.
- **Novelty boundary:** the exact question is explicitly open in the cited 2025 preprint. A bounded follow-up screen cannot establish worldwide priority, and a classical proof assembled here is labeled Certification rather than automatically Discovery.

## 8. Frozen finite verification protocol

Finite computations exercise the construction and distinguish modeling errors; they do not prove the all-target theorem. The fixed protocol is recorded before its first run:

- Four exact quadratic examples: square (`x=0,h^2=1,beta=(1+sqrt(5))/2`); rectangular (`x=0,h^2=9,beta=9+(1+sqrt(5))/2`); hexagonal (`x=1/2,h^2=3/4,beta=sqrt(3)`); skew (`x=1/3,h^2=5/4,beta=(1+sqrt(15))/2`). For each, set `u=h^2/(beta-x)-x`, `t=(beta-x)/h`, `|V|=sqrt(pi/h)`, `A=|V|/sqrt(1+t^2)`, `C=t*A`. Verify `beta>1` and `0<u<1` before evaluating.
- Exact periodic continued fractions for `r={beta}` and `u`; construct the infinite word's finite prefixes with parity padding. Inspect pivots `k=6,10,14`; determine an enclosing cylinder from the common prefix through stage 24. It is the same infinite constructed `alpha` at every pivot, not stage-dependent rational or quadratic replacements. Record the cylinder width and its propagated phase uncertainty.
- Use high-precision arithmetic chosen from the actual convergent sizes, exact integer recurrences and an independently evaluated complex spiral displacement. Inspect integer basis combinations in `[-2,2]^2` and phase windows of lengths `128,512,2048`. All numerical observations remain Empirical evidence even when accompanied by conservative cylinder bounds.
- Check unimodularity, covolume normalization, signed convergent-error formulas, the local Taylor bound, phase-window mesh bounds, and final relative basis error below `1e-4`. No finite sample is promoted to a proof of boundedness for an unspecified angle.
- Negative controls deliberately break the factor of `pi`, reverse the wrong digit history, and replace a unimodular basis by an index-two sublattice. These must be detected. No optimization, random seeds, parameter adaptation or large point-cloud search.

## 9. Verification and review ledger

The mathematical proof above is complete as a proposed classical argument. The reproducible script, its observed outputs and independent-referee dispositions are recorded here only after execution; this initial manuscript makes no claim that those steps have already succeeded.
