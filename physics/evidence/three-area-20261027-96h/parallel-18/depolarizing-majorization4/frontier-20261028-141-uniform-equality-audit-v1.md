# Conditional equality audit for the 121 uniform-noise candidate

**AUTHOR-WRITTEN CONSEQUENCE, NOT ADOPTED.** Assume the complete unreviewed uniform-interval proof in `frontier-20261028-121-consolidated-physical-k3.md`, SHA256 `91643ea8965e0e423f2b5010a18e967ddfaeb4c0f78a175ba6509dd9f2e5c36b`, with mandatory corrections 125/127/128/130/133 applied prospectively. For `0<t=|1-p|<=1/200`, that proof's strict pure-nonproduct gap plus the elementary same-projector argument below implies

\[
K_3(\Lambda_p(\rho))=R_3(p)
\quad\Longleftrightarrow\quad
\rho\text{ is a pure product density}.\tag{1}
\]

For a **fixed** actual rank-three Q, equality also requires Q to be a Ky-Fan-maximizing projector of that product output; it is not automatic for arbitrary Q. At `p=1` all densities and Qs have equality; `p=0` lies outside this small-t interval and is separately covered by erratum 127. No new input class, unconditional original k3 theorem, independent-family/human/formal review, novelty, or process-history cure is claimed.

## 1. The product-output maximizing subspace

First take positive shrinkage `p'=1-t` with `0<t<1`, and write `a=(1+t)/2>b=(1-t)/2>0`. A pure product input has one top output eigenvector equal to the input product vector, with eigenvalue `a^4`; the next eigenvalue `a^3b` has multiplicity four, spanned by the four one-site orthogonal flips; all remaining eigenvalues are strictly smaller. Thus any rank-three maximizing Q contains the input vector and has its entire range inside the five-dimensional space

\[
S_\psi=\operatorname{span}\{|\psi\rangle,|e_1^\psi\rangle,\ldots,|e_4^\psi\rangle\}.
\tag{2}
\]

This includes all choices within the degenerate second eigenspace, not just a single reference Q.

## 2. Two distinct product rays cannot share a maximizing rank-three Q

Suppose product vectors psi and phi have a common maximizing Q. Then `phi` belongs to `S_psi`. Rotate the local bases so `psi=|0000>`, and write `phi=tensor_i(alpha_i|0>+beta_i|1>)`. If no `alpha_i` is zero, membership in `S_psi` forces at most one `beta_i` to be nonzero: otherwise a nonzero coefficient at a word of weight at least two appears. If one `alpha_i=0`, there can be no second zero alpha and no nonzero beta at any other site, for the same support reason. Thus a distinct phi differs from psi at exactly one local site.

After relabeling, write `phi=(alpha|0>+beta|1>) tensor |000>` with `beta!=0`. The two five-dimensional maximizing-support spaces are

\[
\begin{aligned}
S_\psi&=(\mathbb C^2\otimes|000\rangle)
 \oplus\operatorname{span}\{|0\rangle\otimes|e_j\rangle:j=2,3,4\},\\
S_\phi&=(\mathbb C^2\otimes|000\rangle)
 \oplus\operatorname{span}\{(\alpha|0\rangle+\beta|1\rangle)\otimes|e_j\rangle:j=2,3,4\}.
\end{aligned}
\]

Their intersection has dimension exactly two: a linear combination of the latter three vectors lies in `S_psi` only if its `|1> tensor sum_j c_j|e_j>` component vanishes, forcing all `c_j=0`. This remains true for `alpha=0`. A rank-three Q cannot lie in a two-dimensional intersection. Therefore common maximizing Qs require psi and phi to be the same product ray.

## 3. Mixed-state equality and exact boundaries

For positive shrinkage with `0<t<=1/200`, 121's written tube/far estimates give a strictly positive original gap for every pure nonproduct input. Take any finite pure-state decomposition of rho and fix an actual maximizing Q for the mixed output. If equality held, every component's fixed-Q trace would have to equal R3. Thus every component would be a pure product and, by §2, all components would be the same product ray; rho is that pure product density. Conversely, every pure product output has the reference spectrum and admits a maximizing Q. The full-transpose spin-flip bijection transfers the same characterization to `p>1` without changing the input. This proves (1) **only conditional on** the entire still-unreviewed 121 uniform-interval proof.

The `t=0` case is `p=1`, where every output is `I/16` and every Q is maximizing. At `p=0` (outside `t<=1/200`) the channel is identity and equality for a fixed Q is instead equivalent to `supp(rho) subset ran(Q)`; this includes nonproduct and mixed densities of rank at most three. No broader all-p equality classification follows.

This is a substantive equality/degeneracy self-audit, not a separate family candidate or independent review. No program or external model was used. Native observation before this note: `Wed Oct 28 23:29:44 PDT 2026`. The 132 cadence lapse and all five separate source corrections remain; parent controls their ordering and the status of the pending review.
