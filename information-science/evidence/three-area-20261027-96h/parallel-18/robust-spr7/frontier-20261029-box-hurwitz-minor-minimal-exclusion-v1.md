# A box-specific Hurwitz-minor exclusion for the minimal two-circuit mechanism

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:10:55 PDT 2026**. **WRITTEN theorem candidate with WRITTEN-checked-in-kernel finite rational margin**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. This is a quantified exclusion of one structural mechanism, not a general septic verdict.

## 1. Statement

Let \(K\) be any all-member-Hurwitz closed independent monic septic coefficient box containing five actual members \(a_i\) with
\[
E_i(t)=-\lambda_i(t-1/2)(t-v_i)(t-5),\quad
O_i(t)=-(t-o_i)(t-9/2)(t-7),\quad \lambda_i>0,
\]
where
\[
(v_i)=(16/5,16/5,2,16/5,2),\qquad
(o_i)=(9/10,13/10,9/10,9/10,9/10). \tag{1}
\]
Let
\[
(t_i)=(1,121/100,9/4,49/16,121/25). \tag{2}
\]
The positive scales \(\lambda_i\) are **arbitrary** subject only to existence of this eligible box; the box may be much larger than the five members and need not contain their entire independent-parity product.

Then no nonzero positive odd-canceling measure supported on these five prescribed member/frequency pairs plus compactified infinity can satisfy the eight nonpositive Vieta-vertex conditions for \(K\). This excludes **every real mixture weight** of the two possible odd circuits, not just selected sample weights. Removing any additional zero-odd atoms is permitted as in the named predecessor, but adding further nonzero odd-frequency locations is not covered.

This isolates a concrete coefficient-box constraint absent from the stable parity-product countermechanism in `frontier-20261029-parity-product-minimal-weak-countermechanism-v1.md`, SHA-256 `23a54abc392fe8b3c1bc3d64803a2b3d0bad18c09835af80b39d6e64e3ef3895`. It does **not** exclude other five-node shapes or all interval-box obstructions.

## 2. The robust second Hurwitz minor couples all five scales

For a monic septic \(s^7+a_6s^6+a_5s^5+a_4s^4+\cdots\), Hurwitz stability implies
\[
a_6a_5-a_4>0. \tag{3}
\]
Because coefficients in \(K\) vary independently, an actual box member has \(a_6=\ell_6\), \(a_5=\ell_5\), \(a_4=u_4\). Therefore \(\ell_6\ell_5>u_4\). Put \(m=\min_i\lambda_i\), \(M=\max_i\lambda_i\). The five actual members give
\[
\ell_6\le m,\qquad \ell_5\le 62/5,\qquad
u_4\ge\max_i\lambda_i(1/2+v_i+5)\ge(15/2)M.
\]
Consequently
\[
1\le\frac{\lambda_i}{m}\le\frac{M}{m}<\frac{124}{75}. \tag{4}
\]
This argument uses a genuinely independent coefficient-box member; mere convexity or independent *parity sets* does not provide it.

## 3. The only two odd circuits

At (2), the odd signs are \((- ,+,-,-,+)\). In the compact row convention of `frontier-20261029-minimal-weak-circuit-pair-v1.md`, SHA-256 `9993e2e0bf89bf36a3dfc4efc42b98f466c138e6fd6f952a55c854400d4a1282`, the nonnegative odd-cancellation cone on the five rows and infinity has exactly two extreme rays. Their finite uncompactified weights are
\[
w_i^X=\frac{\mathbf1_{i\in X}}{t_iO_i(t_i)H_X'(t_i)},\quad
w_i^Y=\frac{\mathbf1_{i\in Y}}{t_iO_i(t_i)H_Y'(t_i)},\quad
X=\{1,2,3,5\},\quad Y=\{1,2,4,5\}, \tag{5}
\]
where \(H_X(t)=\prod_{i\in X}(t-t_i)\), etc. Each has infinity weight 1. All listed finite weights are positive, odd moments through degree two vanish, and the degree-three finite moment is exactly one, so the compactified \(v_3\) moment cancels. Every nonzero measure on these locations is \(pX+qY\) with \(p,q\ge0\) not both zero.

## 4. All outer Vieta vertices have a uniform positive margin

Because \(K\) contains members with first odd roots \(9/10\) and \(13/10\), second odd root \(9/2\), and third odd root \(7\), every allowed Vieta root triple of \(K\) belongs to the larger product
\[
[0,9/10]\times[13/10,9/2]\times[9/2,7]. \tag{6}
\]
This remains true even if \(K\)'s actual odd bands are wider. Let \(F_x(t)=\prod_{j=1}^3(x_j-t)\). Its image is coefficientwise multi-affine in \(x\), so it is enough to examine the eight vertices of (6).

For ray \(Z\in\{X,Y\}\) and a vertex \(x\), put
\[
c_i^{Z,x}=w_i^Z\,[-(t_i-1/2)(t_i-v_i)(t_i-5)]\,F_x(t_i),\qquad
B^{Z,x}=\sum_{c_i\ge0}c_i+\frac{124}{75}\sum_{c_i<0}c_i. \tag{7}
\]
Exact `fractions.Fraction` arithmetic gives **all 16** bounds \(B^{Z,x}>1/5\); the minimum, over both rays and all eight vertices, is
\[
\frac{9563320046098277}{41361377804175429}>\frac15. \tag{8}
\]
The strictly positive exact numbers in (7) use only (1)–(2), the ray formula (5), and the eight endpoints in (6); the minimum and each comparison were computed with rational/integer arithmetic in one Python Eval kernel.

By (4), at every outer vertex and for either ray,
\[
\sum_iw_i^Z E_i(t_i)F_x(t_i)=\sum_i c_i^{Z,x}\lambda_i\ge mB^{Z,x}>m/5. \tag{9}
\]
The same positive bound holds at every triple in the closed product (6), since the cubic itself is a convex combination of the vertex cubics. In particular it holds throughout the actual box's Vieta polytope. Any nonzero combination \(pX+qY\) has even pairing at least \((p+q)m/5>0\); it cannot obey eight nonpositive box-vertex inequalities. This proves the stated exclusion for **all** eligible boxes and **all** scale vectors and odd-circuit mixtures at the fixed five samples.

## 5. Remaining gap and assurance

The general six-location theorem and extreme-ray identities are imported as author-written candidates. The robust second-minor argument is a written deduction, and the 16 exact margins in (8) were checked in one Eval host with `fractions.Fraction`; they are not an independent replay or formal proof. This result addresses only the fixed sample shape (1)–(2). Other geometries, more atoms, all-box synthesis and an eligible-box negative witness remain unresolved. Parent-classified incidental source-display exposure is recorded in `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim, parent adoption, external review or novelty clearance is made.
