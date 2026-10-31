# Exact polarization/interpolation audit of product Hessian identities

This is an algebraic consistency audit of the weight2/3/4 and mixed-weight coefficient formulas used by `frontier-20261028-59-uniform-high-noise-k3.md`; it is **not** an independent review of the perturbation lemma, the projector inequalities, the far-input argument or the claimed uniform theorem. The reviewed author candidate remains unadopted.

`frontier-20261028-73-hessian-polynomial-audit.py` SHA256 `57626c72a11882440c26886b387c718eeb50dccce27a006c7a39ad36701c830e` ran `python3 -B ...` from repo root, exit0, wall time 39.22 seconds. It imports the already pinned exact checker `frontier-20261028-57-product-hessian-exact.py` SHA256 `647ca9ef45936094b0414d143a475fed4089dd263a3b32885221ff338d87c0ec`, not an external model or third-party CAS. Native pin clock **Wed Oct 28 18:49:35 PDT 2026**.

At each of the **32 distinct exact shrinkages** \(t=k/33\), \(k=1,\ldots,32\), it evaluates the original channel and second-order coefficient definitions on all 11 computational normal-direction basis vectors, every same-weight pair with relative phase1 or i, and every cross-weight pair with relative phase1 or i. Totals: **352 basis directions, 1344 same-weight superpositions, 2176 cross-weight superpositions**, 3872 exact directions. The Gaussian-rational checks verify each displayed A/M coefficient formula and each mixed-weight additivity equality at these directions. The checker also samples the stated inequalities at those directions/t values; sampling alone does **not** establish their universal inequality.

## Why the coefficient-identity data admit a bounded algebraic interpolation

For fixed direction, the unnormalized local depolarizing channel is affine in t at each of four sites. Thus the displayed \(W,V\) entries are polynomials of degree at most4 in t, and any numerator \(V_{ik}V_{kj}\) has degree at most8. The six possible nonzero denominators in the exact second-order definitions are
\[
\lambda_0-\lambda_h,\quad\lambda_1-\lambda_h\quad(h=2,3,4),
\qquad \lambda_h=a^{4-h}b^h,
\]
each a polynomial of degree at most4. Their product has degree at most24 and is nonzero for every \(0<t<1\). Thus, after multiplication by that product, each actual A/M coefficient has numerator degree at most28.

The written weight2 right sides are polynomial of degree at most5; the weight3 right sides have denominator \(D=1-ab\) of degree2 and numerator degree at most6; the weight4 scalar has denominator \(D_4=a^2+b^2\) of degree2 and numerator degree at most7. Clearing the applicable additional denominator, the difference polynomial has degree **at most31** in every case. The mixed-weight difference has degree at most28. Therefore 32 distinct exact roots force each checked coefficient-difference polynomial to vanish identically over \(\mathbb Q(i)\) as a function of t; the endpoint t=0 is taken by the continuous rescaled limit, not by dividing by a vanishing gap.

For fixed t, multiply the normalized A/M equations by \(\|v\|^2\). Both sides are quadratic in the 11 complex normal-direction coordinates and conjugates. Values on each \(e_i\), \(e_i+e_j\), \(e_i+i e_j\) determine all quadratic coefficients by polarization; the cross-weight pair equations separately enforce the claimed additivity. Thus, **subject to the stated degree and quadratic-homogeneity argument**, this exact data supports the coefficient identities for all complex normal directions and \(0<t<1\), not merely 3872 chosen directions. It is not a numerical extrapolation. This inference should itself be checked in the disjoint review.

The weight2 Frobenius bound, weight3/4 sign factorizations, strict uniform Hessian margin, two-conjugation operator remainder, product gauge and same-P all-density bridge remain written mathematical obligations; this program does not prove them by counting or by interpolation. No global all-p k3, formal proof, configured-family/human review or novelty is claimed.
