# A first-node-free selector route covering all of pattern C

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:49:02 PDT 2026**. **WRITTEN fixed-data LP characterization with a WRITTEN-checked-in-kernel literal phase-C example**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It extends the representation of `frontier-20261029-pattern-c-first-band-selector-lp-v1.md`, SHA-256 `fadcec7d4d9ac43a11b0bd83b572263bfe70b27fa49b6479a49db880dfa82775`, beyond its first-band restriction; it does not establish universal LP feasibility.

## 1. Fixed-data direct-certificate route

Fix an admissible independent odd coefficient box with bands \([a,b],[c,d],[e,f]\), and nodes
\[
a<t_1<c<t_2<t_3<d<t_4<t_5<e. \tag{1}
\]
At \(t_1\), retain the actual phase-C condition \(E_1(t_1)\le0\) and \(O_1(t_1)<0\). The odd values at \(t_2,t_3\) have the required signs \(+,-\), and those at \(t_4,t_5\) are positive for every actual odd component. This includes the previously uncovered case \(b\le t_1<c\).

For \(0\le\theta\le1\), let
\[
\xi=(1-\theta)t_4+\theta t_5,\qquad F_\theta(t)=(-t)(c-t)(\xi-t). \tag{2}
\]
Its even numerator coefficients are nonnegative and its roots are in the closed common root gaps. The first ray contribution is **always nonnegative**, because \(F_\theta(t_1)<0\) and the actual \(E_1(t_1)\le0\). Drop this contribution rather than incorrectly replacing it by an upper envelope of uncontrolled sign. The remaining three ray terms have their exact mixed lower bounds: both \(t_2,t_3\) use \(E_-\); the last node uses \(E_-\) on support \(X=(1,2,3,4)\) and \(E_+\) on \(Y=(1,2,3,5)\).

For each support, omitted odd moment \(k=0,1,2,3\), and last-node odd endpoint \(\sigma\in\{-,+\}\), form the normalized ray weights (4) of `frontier-20261029-three-strict-pattern-eight-ray-reduction-v1.md`, SHA-256 `8591da67f304472da00e7afb7bf1ddfc1c2a7970802f7c844cf8cd495ee93686`, but omit the first term of the even pairing. The first odd value affects only the omitted term's weight; all remaining ray weights are independent of it. Their worst odd endpoints at \(t_2,t_3\) are \(O_+,O_-\), respectively; both last endpoints are checked. Denote these 16 dropped-first mixed-envelope forms by \(g_{r,k,\sigma}(\theta)\).

Let \(S_j\) be the six stable-box sign forms, \(W_i=u_i-\ell_i\ge0\), and \(\ell_i\ge0\). Consider the finite linear program
\[
0\le\theta\le1,\quad
 g_{r,k,\sigma}(\theta)=\sum_{j=1}^6\alpha_jS_j+\sum_{i=0}^3\beta_iW_i+\sum_{i=0}^3\gamma_i\ell_i,
\quad \alpha,\beta,\gamma\ge0 \tag{3}
\]
for all 16 cases, with separate multipliers. Equality is coefficientwise in the eight even interval endpoints.

**Theorem.** For fixed odd data and nodes (1), (3) is feasible exactly when one selector (2) makes every dropped-first mixed-envelope ray pairing nonnegative for every all-Hurwitz even box and all allowed actual odd values. In particular, feasibility excludes a direct strictly-negative eight-coordinate certificate of phase C at these fixed data: the omitted first term is nonnegative and the remaining odd-ray contributions are nonnegative, whereas a strict certificate would pair negatively with the nonnegative-coefficient \(F_\theta\).

The equivalence uses the ordinary finite-dimensional Farkas alternative on the **closed** stable-even-box cone. Its strict-stability subset is dense in that cone by adding an arbitrarily small full-width stable even box. A negative value on the closed cone would persist at an actual strictly stable box; conversely a dual representation in (3) makes the dropped sum nonnegative. This is intentionally a stronger *dropped-first* criterion than necessary: its infeasibility neither exhibits a strict certificate nor disproves another selector.

## 2. A literal first-gap phase-C instance

Take odd intervals \([260,672],[292,293],[34,35]\), so the bands are \([1,4],[7,13],[20,24]\), and choose nodes
\[
(t_1,t_2,t_3,t_4,t_5)=(5,8,10,15,18). \tag{4}
\]
Here \(t_1=5\) lies **outside** the first odd band. At \(\theta=1/2\), \(\xi=33/2\). Sixteen exact dropped-first dual identities and the full odd-moment vectors are frozen in `frontier-20261029-pattern-c-first-gap-dropped-duals-v1.json`, SHA-256 `16e1b058cd63b1deea9c6d38e805b602730ec5ad69d534b6e71c3acc9cecba52`. All 16 duals actually have a positive strict-form coefficient; each was checked coefficientwise by exact integers/`fractions.Fraction` on one Eval host. Thus this fixed-data selector excludes direct strict certificates for every admissible even box.

The actual full-width stable box with even endpoints
\[
\ell=(87/1000,36479/500,1089/50,911/1000),\quad
u=(87/500,99099/1000,21867/1000,1089/1000)
\]
has the six positive band margins listed in `frontier-20261029-pattern-b-mixed-band-selector-lp-v1.md`, SHA-256 `5b5cb29a32ea08c074375bf35c5d2a88d7cd743302099607ffa18fc84e4e49df`. Choose actual odd endpoints \((O_-,O_+,O_-,O_-,O_+)\), even endpoints \((E_-,E_-,E_-,E_-,E_+)\), at (4). The odd values are \((-480,64,-270,140,924)\); the even values are
\[
(-87033/1000,\ 43647/1000,\ 98097/1000,\ -261273/1000,\ 229443/500).
\]
These signs realize the literal phase word \((2,4,3,5,4)\), including the strict odd and even reversed-band pairs, with its first node in the even-gap region \((b,c)\). This is an actual phase-placement example, not a negative certificate.

## 3. Limits

The LP is exact for the specified **dropped-first uniform nonnegativity property**, which is sufficient but not necessary for no strict certificate. No proof that it is feasible for every admissible odd box and node tuple is supplied. The complete five-frequency strict-certificate conjecture, other support sizes and original unrestricted SPR7 synthesis-or-obstruction remain **OPEN**. Moment identities and finite duals are same-host exact checks; Farkas, interlacing, root-band signs and phase reconstruction are written deductions. There was no formal proof, independent scientific review, parent adoption or novelty clearance. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
