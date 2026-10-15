# Norm-ranked lattice spirals: proof and evidence

Date: 2026-10-14 (PT). **Evidence label: Certification of the written theorem below; novelty/priority is not established by this label.** The classical lattice-discrepancy argument is a reproduction of established Fourier/Poisson machinery. Finite computations are Empirical evidence or exact finite identity checks, not a substitute for the infinite-set argument. Independent review and the later-source screen are recorded separately.

## 1. Exact obligation and frozen research contract

The target is the explicit density question in Adiceam–Tsokanos, *Higher Dimensional Spiral Delone Sets*, arXiv:2010.06428v3, §6, pp. 22–23. Their points have **exact radii** \(k^{1/n}\), with arbitrary spherical directions. Their asymptotic-density limit is required for **every bounded measurable set whose boundary has zero Lebesgue measure**. Merely counting origin-centered balls does not answer the question.

- **Claim:** the norm-ranked nonzero integer lattice construction below gives a Delone spiral with the required density and angular uniform distribution in every fixed dimension \(n\ge2\), hence in every dimension asked about, \(n\ge3\).
- **Baseline:** their paper constructs spiral Delone sets in every dimension but explicitly leaves the additional density/angular-equidistribution condition open. The classical smooth-ball lattice discrepancy is an ingredient, not a claimed new estimate.
- **Load-bearing bridge:** an error \(o(R^{n-1})\) in the lattice-ball count makes the radial rank correction \(o(1)\), including all points tied on a lattice sphere. A volume main term \(N(R)\sim V_nR^n\) alone does not supply that bridge.
- **Scope:** arbitrary directions are allowed by the source definition. No continuity, bounded step between consecutive indices, transitive-map orbit, distinctness of directions, or visually sunflower-like appearance is claimed. The points themselves are distinct because their radii are distinct. Every nonzero lattice vector is used, including nonprimitive vectors.
- **Book connection:** this is a higher-dimensional phyllotaxis/regular-packing subproblem, not a theorem about elastic energy, cone packing, Fibonacci optimality, or a minimum-energy configuration.
- **Frozen scientific controls:** two independent exact lattice enumerators, complete and partially cut tie shells, normalization and exponent identities, 3D ball Fourier-transform identity, and deterministic 3D geometric/density observations. Main geometric sample: all nonzero integer points in the ball of radius 24; smaller radii 4, 8, 12, 16 check prefix consistency. Directional counts and translated Jordan-box counts include negative controls. No optimizer, fitted parameter, or learned model is used. Single-thread numerical libraries; no giant search.

## 2. The theorem

Write
\[
V_n=\lambda_n(B_1)=\frac{\pi^{n/2}}{\Gamma(1+n/2)},\qquad c_n=V_n^{1/n}.
\]
Enumerate \(\mathbb Z^n\setminus\{0\}\) as \((z_k)_{k\ge1}\), in nondecreasing Euclidean norm, with lexicographic order within equal-norm shells. Put
\[
r_k=\|z_k\|_2,\qquad u_k=z_k/r_k,\qquad s_k=k^{1/n}u_k,\qquad S=\{s_k:k\ge1\}.
\tag{2.1}
\]

**Theorem.** For each fixed integer \(n\ge2\):

1. (2.1) is effectively constructible and \(\|s_k\|_2=k^{1/n}\) exactly.
2. With \(\beta_n=(n-1)/(n+1)>0\),
   \[
   \|s_k-c_nz_k\|_2=O_n(r_k^{-\beta_n})=o(1).
   \tag{2.2}
   \]
   The estimate is uniform over all ranks within any tied shell; the conclusion does not depend on the chosen order inside ties.
3. \(S\) is uniformly discrete and relatively dense in \(\mathbb R^n\), including the finite initial part.
4. For every bounded Jordan-measurable \(X\subset\mathbb R^n\),
   \[
   \lim_{R\to\infty}\frac{\#(S\cap RX)}{R^n}
   =\frac{\lambda_n(X)}{V_n}.
   \tag{2.3}
   \]
5. For every spherical cap \(C\subset\mathbb S^{n-1}\),
   \[
   \lim_{N\to\infty}\frac{\#\{1\le k\le N:u_k\in C\}}{N}
   =\frac{\sigma_{n-1}(C)}{\sigma_{n-1}(\mathbb S^{n-1})}.
   \tag{2.4}
   \]

No numerical value of the global separation or covering constant is inferred from a finite nearest-neighbor computation. Their existence is proved in §5.

## 3. Ball-count lemma, with a special-case proof

Define the full closed-ball count
\[
N_0(R)=\#\{z\in\mathbb Z^n:\|z\|_2\le R\}.
\]
For all real \(R\ge2\), we prove
\[
N_0(R)=V_nR^n+O_n(R^{\alpha_n}),\qquad
\alpha_n=\frac{n(n-1)}{n+1}=n-2+\frac{2}{n+1}.
\tag{3.1}
\]
In particular \(\alpha_n<n-1\). The constant may depend on fixed dimension; no dimension-uniform constant is asserted.

### 3.1 Fourier transform and its decay

Use the Fourier convention
\(\widehat f(\xi)=\int f(x)e^{-2\pi i x\cdot\xi}\,dx\).
For \(\xi\ne0\), rotation invariance and slicing perpendicular to \(\xi\) give
\[
\widehat{1_{B_R}}(\xi)
=V_{n-1}\int_{-R}^{R}(R^2-t^2)^{(n-1)/2}
 e^{-2\pi i\|\xi\|t}\,dt
=R^{n/2}\|\xi\|^{-n/2}J_{n/2}(2\pi R\|\xi\|).
\tag{3.2}
\]
The last equality is Poisson's Bessel integral, [NIST DLMF 10.9.4](https://dlmf.nist.gov/10.9.E4), with fixed real order \(\nu=n/2>-1/2\). The constants follow from \(V_{n-1}=\pi^{(n-1)/2}/\Gamma((n+1)/2)\); substituting \(t=Rv\) into the first integral makes (3.2) immediate from that identity.

For fixed order, [DLMF 10.17.3](https://dlmf.nist.gov/10.17.E3) gives
\(J_{n/2}(x)=O_n(x^{-1/2})\) as positive real \(x\to\infty\). Continuity on compact positive intervals extends the bound to all \(x\ge1\). Hence, when \(R\ge1\) and \(\|\xi\|\ge1\),
\[
|\widehat{1_{B_R}}(\xi)|
\le A_n R^{(n-1)/2}\|\xi\|^{-(n+1)/2}.
\tag{3.3}
\]
These are established special-function identities; neither the formula nor its decay is a new result here.

For the requested ambient dimension three, no Bessel asymptotic is necessary: direct integration of the disk cross-sections gives
\[
\widehat{1_{B_R^3}}(\xi)
=\frac{\sin(2\pi Rq)-2\pi Rq\cos(2\pi Rq)}{2\pi^2q^3},
\qquad q=\|\xi\|>0.
\tag{3.4}
\]
The triangle inequality gives \(O(Rq^{-2})\) for \(R,q\ge1\), exactly the \(n=3\) case of (3.3).

### 3.2 Smoothing and Poisson summation

Choose a fixed nonnegative \(C_c^\infty\) function \(\phi\), supported in \(B_1\), with integral one. For example normalize \(\exp[-1/(1-\|x\|^2)]\) inside the unit ball and set it to zero outside. For \(0<\varepsilon\le1\), set \(\phi_\varepsilon(x)=\varepsilon^{-n}\phi(x/\varepsilon)\) and
\[
f_\pm=1_{B_{R\pm\varepsilon}}*\phi_\varepsilon.
\]
Pointwise, including the closed-ball boundary,
\[
f_-\le1_{B_R}\le f_+.
\tag{3.5}
\]
Indeed, an outside point cannot lie within \(\varepsilon\) of \(B_{R-\varepsilon}\); at every point of \(B_R\), the translated support of \(\phi_\varepsilon\) lies in \(B_{R+\varepsilon}\). Nonnegativity and unit integral establish both inequalities.

The functions \(f_\pm\) are smooth and compactly supported, hence Schwartz. Poisson summation therefore applies with absolutely convergent Fourier sums:
\[
\sum_{z\in\mathbb Z^n}f_\pm(z)
=V_n(R\pm\varepsilon)^n
+\sum_{\ell\in\mathbb Z^n\setminus\{0\}}
\widehat{1_{B_{R\pm\varepsilon}}}(\ell)\widehat\phi(\varepsilon\ell).
\tag{3.6}
\]
For completeness, this instance of Poisson summation follows by periodizing a Schwartz function, computing its Fourier-series coefficients by integration over the unit cube, and evaluating its absolutely convergent Fourier series at zero. It is not being applied directly to a discontinuous ball indicator.

For any chosen integer \(M>n\), integration by parts gives
\(|\widehat\phi(\eta)|\le C_M(1+\|\eta\|)^{-M}\).
Also the number of integer vectors in a unit-width annulus of radius \(j\ge1\) is \(O_n(j^{n-1})\): the disjoint unit cubes centered at those vectors lie in an annulus whose thickness is bounded solely in terms of dimension, and comparison with its volume gives this bound. Thus
\[
\sum_{\ell\ne0}\|\ell\|^{-(n+1)/2}(1+\varepsilon\|\ell\|)^{-M}
\ll_n\sum_{j\ge1}j^{(n-3)/2}(1+\varepsilon j)^{-M}
\ll_n\varepsilon^{-(n-1)/2}.
\tag{3.7}
\]
To verify the last step, split at \(j=\varepsilon^{-1}\). The lower sum is \(O(\varepsilon^{-(n-1)/2})\), since \((n-3)/2>-1\) for \(n\ge2\). For the upper sum, factor out \(\varepsilon^{-M}\) and sum \(j^{(n-3)/2-M}\); it gives the same order. For \(R\ge2\), both \(R\pm\varepsilon\) are comparable to \(R\), so (3.3), (3.5)–(3.7) yield
\[
|N_0(R)-V_nR^n|
\ll_n R^{n-1}\varepsilon
+R^{(n-1)/2}\varepsilon^{-(n-1)/2}.
\tag{3.8}
\]
The first term here is a **continuous volume difference** \(V_n(R\pm\varepsilon)^n-V_nR^n\). We have not assumed that the discrete count in a thin lattice shell equals its volume; doing that would be an unjustified shortcut.

Take \(\varepsilon=R^{-(n-1)/(n+1)}\). The two terms in (3.8) both equal order \(R^{n(n-1)/(n+1)}\), proving (3.1) for every real \(R\ge2\). For \(n=3\), the choices are \(\varepsilon=R^{-1/2}\) and error \(O(R^{3/2})\). ∎

## 4. Ranking and ties imply a vanishing radial correction

Let \(N(R)=N_0(R)-1\), excluding the origin, and let
\(N_<(r)=\#\{z\ne0:\|z\|<r\}\).
For a vector on a shell of radius \(r\), every possible rank within the shell satisfies
\[
N_<(r)+1\le k\le N(r).
\tag{4.1}
\]
Equation (3.1) also gives
\[
N_<(r)=V_nr^n+O_n(r^{\alpha_n})
\tag{4.2}
\]
by letting a real radius \(R\uparrow r\). Counts are locally finite, so that left limit is the strict count. The bound in (3.1) holds for **all real radii**, which is essential here. Subtracting the two estimates also bounds the entire tie multiplicity by \(O_n(r^{\alpha_n})\).

It follows uniformly for every rank in that shell that
\[
|k-V_nr^n|\ll_n r^{\alpha_n}.
\tag{4.3}
\]
For \(A=k^{1/n}\), \(B=c_nr\), use
\[
|A-B|=
\frac{|A^n-B^n|}{A^{n-1}+A^{n-2}B+\cdots+B^{n-1}}
\le\frac{|k-V_nr^n|}{(c_nr)^{n-1}}.
\tag{4.4}
\]
As \(\alpha_n-(n-1)=-(n-1)/(n+1)\), (4.4) proves (2.2). In particular \(r_k\to\infty\) and the displacement tends to zero uniformly through ties. Lexicographic order is chosen for a reproducible algorithm, not to rescue the estimate.

This is exactly the point at which an ordinary leading count asymptotic would be insufficient. For example \((R+1)^n=R^n+O(R^{n-1})\) has the same relative volume main term as \(R^n\), but the associated n-th-root correction equals **one**, not a vanishing quantity. ∎

## 5. All-pair separation and global covering

Let \(\delta_k=\|s_k-c_nz_k\|\). By (2.2), choose \(K\) such that \(\delta_k\le c_n/4\) for every \(k\ge K\). Distinct integer vectors are at distance at least one. Hence, for distinct \(i,j\ge K\),
\[
\|s_i-s_j\|\ge c_n\|z_i-z_j\|-\delta_i-\delta_j\ge c_n/2.
\tag{5.1}
\]
This alone does not address the finite initial part. Put \(A=0\) if \(K=1\), and otherwise \(A=(K-1)^{1/n}\). Choose an integer \(L\ge\max(K,2)\) such that \(L^{1/n}>A+1\). If \(i<K\) and \(j\ge L\), the reverse triangle inequality gives
\[
\|s_j-s_i\|\ge j^{1/n}-i^{1/n}>1.
\tag{5.2}
\]
All remaining pairs have both indices less than \(L\), or are already covered by (5.1). Points with different indices have different norms, so none of these finitely many pairs coincide. More explicitly, since \(x^{1/n}\) is concave,
\[
\|s_j-s_i\|\ge j^{1/n}-i^{1/n}
\ge L^{1/n}-(L-1)^{1/n}>0
\quad(1\le i<j<L).
\tag{5.3}
\]
Thus a global separation constant is
\[
\eta_n=\min\{c_n/2,1,L^{1/n}-(L-1)^{1/n}\}>0.
\tag{5.4}
\]
This proves separation for the entire sequence, including all finite-prefix/cross-prefix pairs. It is not an extrapolation of a sampled minimum distance.

Since \(\delta_k\to0\), \(D_n=\sup_k\delta_k<\infty\). For any \(x\in\mathbb R^n\), rounding \(x/c_n\) to an integer vector gives a lattice point at distance at most \(c_n\sqrt n/2\). If that vector is zero, choose \(e_1\) instead, increasing this bound by at most \(c_n\). Every nonzero integer vector occurs in the enumeration, so some \(s_k\) satisfies
\[
\|x-s_k\|\le c_n(\sqrt n/2+1)+D_n.
\tag{5.5}
\]
Therefore \(S\) is relatively dense. Removing the lattice origin has been explicitly accounted for. ∎

## 6. Density for every bounded Jordan-measurable set

First, the scaled lattice \(\Lambda=c_n\mathbb Z^n\) has
\[
\frac{\#(\Lambda\cap RX)}{R^n}\longrightarrow
\frac{\lambda_n(X)}{c_n^n}
=\frac{\lambda_n(X)}{V_n}
\tag{6.1}
\]
for every bounded Jordan-measurable \(X\). For an axis-aligned box this follows by multiplying the one-dimensional counts \((R/c_n)(b-a)+O(1)\). Finite inner and outer unions of grid boxes, whose volume difference can be made arbitrarily small because \(\lambda_n(\partial X)=0\), prove (6.1) by sandwiching. Removing one point, the origin, changes the count by at most one.

We next prove that the bounded displacement \(c_nz_k\mapsto s_k\) preserves this density. Fix \(X\) and \(\epsilon>0\). Its boundary \(\partial X\) is compact and has measure zero, so choose finitely many open axis-aligned boxes whose union \(U\) covers \(\partial X\) and whose **sum of volumes** is less than \(\epsilon\). Compactness gives an \(h>0\) such that the h-neighborhood of \(\partial X\) is contained in \(U\).

For sufficiently large \(R\), \(D_n/R<h\). If \(c_nz_k/R\) and \(s_k/R\) differ in membership in \(X\), a segment between them meets the boundary, or one endpoint is itself on it. Consequently \(c_nz_k/R\in U\). Therefore
\[
\left|\#(S\cap RX)-\#((\Lambda\setminus\{0\})\cap RX)\right|
\le\#(\Lambda\cap RU).
\tag{6.2}
\]
Using the separate box counts, the upper limit of the right side divided by \(R^n\) is at most \(\epsilon/V_n\), even if the covering boxes overlap. Letting \(\epsilon\downarrow0\) proves that the normalized difference tends to zero. Combining with (6.1) proves (2.3).

Boundary membership conventions do not affect this argument. No convexity, smoothness, connectedness, or uniform boundary-content bound is required for \(X\). The constants and the chosen box cover may depend on that fixed set, exactly as allowed in the source definition. ∎

## 7. Angular uniform distribution and normalization

Let \(C\) be a spherical cap, and define its truncated cone
\[
X_C=\{ru:0<r\le1,\ u\in C\}.
\]
This is Jordan-measurable: its boundary consists of parts of a sphere, a cone over the boundary of a spherical cap, and the origin, all of n-dimensional measure zero. For the degenerate full/empty caps the conclusion is immediate. Polar coordinates give
\[
\lambda_n(X_C)=\frac{\sigma_{n-1}(C)}{n}
=V_n\frac{\sigma_{n-1}(C)}{\sigma_{n-1}(\mathbb S^{n-1})}.
\tag{7.1}
\]
Since the radii in (2.1) are exact, taking \(R=N^{1/n}\) makes
\[
\#(S\cap RX_C)=\#\{1\le k\le N:u_k\in C\}.
\]
Equation (2.4) now follows from (2.3) and (7.1).

**Independent count-based check of the same implication.** Apply the lattice Jordan-count argument directly to the cone \(X_C\), at radius \(r_k\). The difference between the first k norm-ordered lattice vectors and the complete ball of radius \(r_k\) is at most the tie multiplicity \(O(r_k^{\alpha_n})=o(r_k^n)\). Dividing the lattice sector count by \(k\sim V_nr_k^n\) gives the same spherical-cap limit, independently of the bounded-displacement density argument.

Finally, for the unit ball itself,
\[
\#(S\cap B_R)=\lfloor R^n\rfloor.
\tag{7.2}
\]
Thus any density \(\rho\) in the source's sense must satisfy \(1=\rho V_n\), i.e. \(\rho=V_n^{-1}\). The rendered pp. 22–23 of the primary source indeed print a **superscript inverse**, not \(V_{n-1}\). The OCR ambiguity is resolved both visually and by this forced normalization. ∎

## 8. Effective construction and limits

For each integer radius \(M\), enumerate the finite cube \([-M,M]^n\cap\mathbb Z^n\), discard the origin and points whose squared norm exceeds \(M^2\), and sort by the integer key
\[
(\|z\|_2^2,z_1,\ldots,z_n).
\]
Increase \(M\) until at least k vectors are present, then take the first k. No point outside that cube has norm at most \(M\); consequently this is exactly the desired initial segment. The process terminates because even the nonzero axis vectors alone increase without bound. Norm comparisons and tie decisions use integers, not rounded square roots. Each direction and each new point is computable to arbitrary precision from integer square roots and positive n-th roots. This is an effectively constructible sequence in the paper's sense; no polynomial-time-in-dimension claim is made.

The all-dimensional assertion is proved for each fixed \(n\ge2\). The numerical smoke primarily exercises \(n=3\), and does not certify all dimensions by sampling. There is no claimed optimal packing density, best separation constant, minimum energy, or novel Fourier-analytic method. The answer concerns the stated existence problem only. Historical novelty depends on the forward-source screen, not merely on this proof being written here.

## 9. Claim ledger and verification/review record

| Claim | Evidence category | Novelty status | Load-bearing justification |
|---|---|---|---|
| Ball discrepancy (3.1) | Reproduction of classical argument / Certification of displayed derivation | Established ingredient, not new | Bessel decay, compact smoothing, absolutely convergent Poisson sum, balanced error terms |
| Exact-radius norm-ranked construction and vanishing displacement | Certification | Later-source and priority screen separate | Integer ordering, both endpoints of tied shells, algebraic root identity |
| Global Delone property | Certification | No claim to a new technique | Tail lattice separation plus explicit finite-prefix/cross-pair bound; bounded-displacement covering |
| All-Jordan-set density and angular uniform distribution | Certification | Direct answer to the explicit source question if not already settled later | Boundary-box count comparison and two independent angular-count arguments |
| Finite generator/geometric observations | Empirical evidence and exact finite controls | No universal or novelty inference | Deterministic code, independent enumerator, boundary/negative controls |

The executed scientific command, numerical outputs, primary-source pins, and completed independent referee dispositions are integrated into this section after their respective runs. The mathematical argument above does not rely on any empirical tolerance.
