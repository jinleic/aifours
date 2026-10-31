# A finite one-dimensional envelope for the direct selector problem

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:37:05 PDT 2026**. **WRITTEN exact fixed-data reduction**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It turns a stronger version of the 16-ray selector LP into an explicit finite interval intersection; it does not decide the universal parameter question.

## 1. Fixed odd data and stable-even cone

Use the admissible odd box, bands \([a,b],[c,d],[e,f]\), nodes \(a<t_1<t_2<b<t_3<t_4<c<t_5<d\), selector \(F_\theta\), and 16 direct odd-ray/endpoint mixed-envelope linear forms \(g_j(\theta)\) of `frontier-20261029-direct-mixed-band-uniform-selector-lp-v1.md`, SHA-256 `b5380caec863a2c4e807db1aab912ee3aed2bc37fe72d2d0382d7b1262c4f36e`. The \(g_j\) are linear forms in the eight even interval endpoints and affine in \(\theta\in[0,1]\).

Let \(C\subset\mathbb R^8\) be the closed cone defined by the 14 homogeneous forms
\[
-E_+(a),-E_+(b),E_-(c),E_-(d),-E_+(e),-E_+(f),\quad
u_k-\ell_k,\quad\ell_k\quad(k=0,1,2,3)\quad\ge0. \tag{1}
\]
It is full-dimensional: select an even cubic with roots strictly inside the three gaps and sufficiently small independent positive widths. It is pointed: \(\ell_k\ge0\) and \(u_k-\ell_k\ge0\) make every coordinate nonnegative.

## 2. The exact interval test

Enumerate all \(\binom{14}{7}=3432\) seven-row subsets of the matrix of (1). For a rank-seven subset, form its cofactor null vector. Retain each orientation for which all 14 forms are nonnegative, and discard zero vectors and duplicates. The resulting set \(\mathcal R\) is exactly the extreme-ray set of \(C\): every extreme ray of a full-dimensional pointed cone has seven independent active inequalities, and any retained rank-seven one-dimensional feasible face is extreme.

For every \(v\in\mathcal R\) and \(1\le j\le16\), define
\[
A_{jv}=g_j(0)\cdot v,\qquad B_{jv}=g_j(1)\cdot v. \tag{2}
\]
There is a selector **strictly positive on every nonzero point of the closed cone** exactly when the finite interval system
\[
(1-\theta)A_{jv}+\theta B_{jv}>0\quad(j=1,\ldots,16,\ v\in\mathcal R),\qquad0\le\theta\le1 \tag{3}
\]
has a solution. There are at most \(16\cdot3432=54912\) scalar affine inequalities. For \(B>A\), the inequality is \(\theta>-A/(B-A)\); for \(B<A\), it is \(\theta<-A/(B-A)\); if \(B=A\), it requires \(A>0\). Their intersection with \([0,1]\) is the exact selector set at this stronger closed-cone assurance level.

A solution proves the uniform direct strict-certificate exclusion for those fixed data: every actual strictly stable even box is a nonzero point of \(C\), and every one of its 16 mixed-envelope pairings is strictly positive. Conversely, failure of the **strict** test at a boundary ray alone does not disprove the original open-cone selector LP: a zero boundary value may coexist with strict positivity on all actual stable boxes. The named 16-ray Motzkin LP gives the exact open-cone criterion.

If an increasing affine inequality requires \(\theta>L\), a decreasing one requires \(\theta<U\), and \(U<L\) with \((U,L)\cap(0,1)\ne\varnothing\), these two extreme rays prove the stronger fact that the original uniform selector property itself fails: their values are both strictly negative at any \(\theta_0\in(U,L)\cap(0,1)\). Add a sufficiently small multiple of a single full-width strictly stable even-box vector to each boundary ray. By continuity, one obtains two actual full-width stable boxes with the same strict failures at \(0,\theta_0\) and \(\theta_0,1\), respectively, so no parameter works for both boxes. For rational fixed data this perturbation and both box witnesses can be chosen rational. Such a failure is still **not** an original no-go: a selector depending on the even box, a different test numerator, or positive cancellation between rays could remain possible.

## 3. What this resolves and what remains

For rational band endpoints and rational nodes all cofactor entries and \(A,B\) are rational. For rational odd coefficients with algebraic band endpoints, the same finite computations are over real algebraic numbers; every denominator and sign is exact. The 32-ray worked example `frontier-20261029-selector-interior-cone-rays-frozen-v1.json`, SHA-256 `f655faab905fdc2505a024f724727c6bb9d369b2134e63ad1007f65a27cc39b0`, illustrates the construction for the four-ray weak version. It is not a proof that all possible band geometries have the same ray set: a different fixed example produced 38 rays.

The universal direct-pattern question can now be attacked by proving that the relevant parameter-dependent lower envelope lies below the upper envelope for all admissible odd bands/nodes, or by finding strict crossing \(L>U\) and extracting the two actual boxes described above. Both routes retain the exact independent-box stability geometry. No crossing or universal inequality is established here, and a negative selector result would still not settle unrestricted SPR7.

The cone and interval arguments are written deductions with standard finite-dimensional polyhedral geometry as a named import. The numerical ray count is an explicitly named author-written example, not an independent scientific review. No formal proof, parent adoption, cross-vendor review or novelty clearance is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
