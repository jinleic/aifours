# Independent written reconstruction: degree8 primitive-Hermitian jet obstruction

Before-creation clock observed: **2026-10-23T13:43:52-07:00**. Reviewer: `MathResearch96h`, at the parent's explicit request. Complete author proof lines1–143 read. No program, symbolic-algebra execution, external model, nested agent or proof assistant was used.

Reviewed file: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/proof-SOF24-Hermitian-jet-obstruction-v1.md`.

Exact SHA256: **`d3c41cb464dc898fe03a3d38d8bd03c628e5fd27f3c2e38f75817ae5dba95470`**.

**Verdict: 0 FATAL /0 MAJOR /0 MINOR. No substantive defect found in the all-degree8-curve obstruction within the stated primitive-Hermitian certificate class.** This is not P24, generic stabilizability, an exclusion of arbitrary real-avoidance kernels, formal proof or priority acceptance.

## 1. Real polynomial row descent and its invariants

Rank2 at zero implies the row wedge is not identically zero and the rows are independent over R(z). If their real leading vectors are dependent and one row has degree a>=b, subtracting the appropriate real multiple of z^(a-b) times the lower-degree row is determinant1 and lowers the higher degree. A zero row cannot result: it would make the wedge identically zero, contradicting rank2 at zero. The nonnegative integer degree sum strictly decreases until the leading vectors are independent.

At termination the leading wedge coefficient is their nonzero real wedge, so the degree of the wedge/minor vector equals the sum of row degrees. Since the maximum minor degree is8, a+b8 exactly. A determinant1 polynomial row matrix has determinant1 at zero, so zero-point rank persists. Grouping coordinates into complex pairs does not lower row degree: a complex coefficient is zero precisely when both its real coordinates vanish.

For real scalar polynomial row coefficients, coefficient-conjugation leaves those coefficients unchanged. In the expansion of v'w'^*-w'v'^*, the v v* and w w* terms cancel and the remaining cross term is det(row operation) times the old alternating expression. Thus H and its jets are invariant under the determinant1 descent, with no conjugation of z. Under a constant nonzero-determinant real change H merely scales by that determinant. The existence of a constant real4plane L with determinant identically zero is likewise invariant under all these operations.

If a row has degree0, it is a fixed nonzero vector. A real4plane containing it makes the stacked6-by-6 determinant zero because that row is redundant with L. Otherwise both row degrees lie in[1,7]. This covers the unbalanced degree splits as well as4+4 without appealing to a polynomial-minimal-basis theorem.

## 2. The seven-dimensional annihilator constraint

For the coefficientwise Hermitian convention H0=(i/2)(v0w0*-w0v0*) is nonzero. Equality to zero would identify the two rank1 outer products, forcing w0=lambda v0 with lambda real and contradicting real row independence. Its complex rank is at most2, so it cannot be a nonzero multiple of I3. Consequently its traceless projection is nonzero.

The real trace inner product is positive definite on Hermitian matrices and on its traceless8-dimensional subspace. Therefore the H0-annihilator inside that traceless space has dimension7. The assumed S of dimension7 equals it. In the full9-dimensional Hermitian space, S-perp is exactly the real span of the independent matrices I3,H0.

Every coefficient of H at orders0,...,7 must lie in that span. Thus the necessary jet identity H=alpha I+beta H0 modulo z8 is correct, with real alpha/beta coefficients. It does not presume that arbitrary such jets arise from a decomposable curve.

## 3. Complex-independent initial rows

A constant unitary sends the complex span of v0,w0 to the first two coordinates. The31 and32 entries of both I and H0 are zero, so their jet equations are

    v3 bar(w_j)-w3 bar(v_j)=0 modulo z8, j1,2.

The2-by-2 matrix of coefficients at zero has independent columns bar(w0),-bar(v0), hence a nonzero determinant constant term. It is invertible over C[[z]], using only the elementary fact that a power series with nonzero constant term has a formal inverse. Multiplication by that inverse forces v3 and w3 into z8 C[[z]]. Their polynomial degrees are at most7, so both vanish identically.

Both rows consequently lie in a fixed complex2plane, whose underlying real dimension is4. Choosing L to contain that real space gives a real rank4 L and an identically zero stacked determinant. No convergence or pointwise analytic inversion assumption is needed for the formal argument.

## 4. Complex-dependent but real-independent initial rows

After arranging deg v<=deg w, write w0=(A+iB)v0 with B nonzero. Subtracting A v from w, dividing the latter by B, then rescaling both nonzero rows by the common norm and using an ambient unitary gives v0=e1,w0=i e1 and H0=E11. The real triangular row change preserves degrees: when degrees differ the lower row cannot cancel the higher leading term; when equal, the already-reduced independent leading vectors cannot cancel. Constant row/ambient changes preserve the total degree8, rank at zero and the span-type jet constraint.

Suppose a perpendicular component is nonzero and k is its least positive vanishing order. With u and v the order-k coefficients of the two perpendicular vectors, the cross-block jet at k gives

    -i u-v=0.

If u were zero, v would be zero, contrary to minimality of k. Therefore both vectors start at the same k with nonzero coefficients u,-i u. The lower2-by-2 block of H at degree2k is exactly

    (i/2)[u(iu*)-(-iu)u*]=-u u*.

If2k<8, the jet identity requires this nonzero rank1 matrix to be a scalar multiple of I2. Such a scalar matrix has rank0 or2, a contradiction. Thus k>=4. Both row degrees are at least k and sum8, forcing a=b=k4. Their perpendicular parts are therefore exactly z4u and-i z4u; no higher terms remain. The first coordinates can be arbitrary polynomials of degree<=4, but every row still lies in the fixed complex span of e1 and u, of real dimension at most4. This proves the same real4plane degeneracy. If both perpendicular parts vanish initially as polynomials, the smaller fixed complex line already supplies the conclusion.

These two initial-plane cases exhaust real rank2 at zero. Neither a complex-dependent real2plane nor an unbalanced degree split supplies an omitted escape.

## 5. Real L, Plucker binding and scope over complex structures

When all row values lie in a real U of dimension<=4, extend U to a real4plane and choose four independent row vectors spanning it as L. Then [V;L] has rank at most4 for all z and determinant identically zero. In the constant-row alternative it has rank at most5. Multiplying V by any invertible polynomial row matrix scales the determinant by a nonzero constant; ambient constant coordinate changes transport L and preserve its vanishing. Thus the conclusion is not chart-specific.

For Hermitian B, in a unitary eigenbasis with eigenvalues lambda_j,

    tr(BH(v,w))=sum_j lambda_j(dx_j wedge dy_j)(v,w).

For v_j=x_j+iy_j,w_j=u_j+it_j, the scalar calculation is(i/2)(v_j bar(w_j)-w_j bar(v_j))=x_j t_j-y_j u_j, confirming both reality and alternating bilinearity. A nonzero trace-free Hermitian B has at least two nonzero eigenvalues, so the associated real2form has rank at least4 and cannot be a nonzero real simple2form.

The coefficients of this bilinear evaluation on V's row wedge are exactly the first coefficient functionals in the Plucker route; vanishing through degrees0–7 is precisely divisibility by z8, not merely an analogy between matrix and form spaces. If rank at zero failed, every2-by-2 minor would have zero constant term and share the factor z, contradicting the intended basepoint-free P24 input. Hence the row-rank assumption is not a hidden extra condition on a valid intended candidate.

The proof starts with an arbitrary fixed orthogonal complex structure on R6 and uses only coordinate changes permitted within that choice plus real row operations. Its conclusion therefore holds for every such fixed structure; rotating the structure or changing the degree split cannot evade it. It does not address z-dependent complex structures, arbitrary non-Hermitian avoidance subspaces or every degree8 curve. The manuscript correctly retains those boundaries and leaves P24 unresolved.

## Verification and novelty limits

The only facts used above are the explicitly invoked elementary linear algebra, Hermitian diagonalization, determinant invariance and formal-unit inversion. No outside P24 theorem or source-control example was adopted as a premise. This is an independent in-harness written reconstruction, not a blind/cross-vendor/human/formal gate. The primitive-Hermitian obstruction may have classical precursors; priority remains unestablished. Parent records must be read with their operative timestamp and verification errata.
