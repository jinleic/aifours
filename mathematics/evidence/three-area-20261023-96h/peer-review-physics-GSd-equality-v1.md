# Independent written review: equality cases conditional on GSd

Before-creation clock observed: **2026-10-23T13:18:10-07:00**. Reviewer: `MathResearch96h`, at the parent's explicit request. Complete addendum lines1–128 read; no execution, assay replay, model CLI or nested agent was used.

Reviewed file: `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261023-96h/proof-GS4-maximally-entangled-reference-ADDENDUM-2-equality.md`.

Exact SHA256: **`e6d88e639507904fc1d87fb2a515f5f02d9bbba6ff9e1e696583c74dd74e5202`**.

Operative dependency: GSd addendum SHA256 **`c51a4c9d0665d37d91bd325b6e9771c4591207ffb44eac92beeeadbe7664ff4b`**, independently reconstructed in `peer-review-physics-GSd-addendum-v1.md`. The present verdict is explicitly **conditional on the GSd matrices/inequalities at that candidate boundary**; an in-harness correctness review does not promote GSd to formal/human/priority acceptance.

**Verdict: 0 FATAL /0 MAJOR /0 MINOR. No substantive defect found in the kernel, strictness or two-way equality classification.** The unrestricted W4 and arbitrary-reference problems remain outside the reviewed claim.

## 1. The complete two-site defect kernel

The GSd decomposition has strictly positive minus scalars on K-perp, a single identity-block minus kernel p, and on each traceless block the three positive squares impose exactly

    z_minus=0,
    z0=sqrt((d+2)/(d-2))z1,
    z_plus=-sqrt(2d/(d-2))z1.

An independent normalization check identifies this line with J2(X): since e2=(h0+h1-h2-h3)/4,

    J2(X)=(sqrt(d+2)/2) f0+(sqrt(d-2)/2) f1
           -(sqrt(2d)/2) f_plus.

Thus the entire kernel is p plus one J2(X) for each of the d^2-1 independent traceless X, namely ran P12=span{Omega_d}_input tensor B_output, of dimension d^2. There is no zero in the remaining components. The plus inequality is strictly positive on every component because all scalar values, identity determinant/pivot and traceless pivots in GSd are strict for integer d>=3.

For the first site, the plus blocks are1 on |00>, [[2,-1],[-1,1]] on each mixed pair, and I on Q tensor Q; hence C0+S0 is strictly positive. The minus form is PSD. No unproved description of its kernel is needed.

## 2. Tensor-kernel congruence and absence of a missing conjugation

Let C be either positive co-Choi matrix and S its reference matrix. From

    I-T=C^(-1/2)(C-S)C^(-1/2)

one has ker(I-T)=C^(1/2)ker(C-S). The strict plus inequality excludes the eigenvalue-1 of T; the remaining spectrum is in(-1,1]. Thus the product T0 tensor Td has eigenvalue1 exactly on the tensor product of its two +1 eigenspaces. Undoing the two positive congruences gives

    ker(C0 tensor Cd-S0 tensor Sd)
      =ker(C0-S0) tensor ker(Cd-Sd),

as claimed. This is the correct congruence-kernel transformation, not an ordinary similarity argument.

With the co-Choi convention, direct scalar contraction yields

    <x tensor z,Jhat(E)(x tensor z)>
      =sum_ab bar(x_b)x_a <z,E(|a><b|)z>
      =<z,E(|x><x|)z>.

The coefficient bar(x_b)x_a is indeed x_a bar(x_b), so no conjugation of the vector x is missing. This identity holds for any linear map; positivity is supplied here by the PSD co-Choi matrix.

After regrouping, the defect kernel requires the B part of the full input vector to lie in span{eta}. If x has a nonzero component in H1 tensor eta-perp and z is nonzero, projecting x tensor z onto that component remains nonzero. Thus x tensor z is outside the PSD kernel, and its quadratic value is strictly positive. Since this is true for every nonzero z, Delta(|x><x|) is positive definite for each such x. It is not a uniform gap as x approaches H1 tensor eta.

## 3. Strict positivity away from the common-reference range

If the rank2 range contains u=a tensor eta but is not contained in H1 tensor eta, an orthonormal extension u,x has x outside that subspace. In a decomposition C=|u><v|+|x><y|, rank2 forces y nonzero. The exact square completion

    q3(C)=||A_u^(1/2)(v+A_u^-1 L-dagger y)||^2
           +<y,(D-L A_u^-1 L-dagger)y>

has the correct switched order and expands to the already-reviewed polarization. Its second term is strictly positive by §2. The rank1 alternative is also strict: R1 tensor R2 tensor R3 has minimum eigenvalue at least1/8, so the rank1 form is at least||C||_HS^2/8. No zero exception is omitted.

## 4. Common-reference range: both equality directions

For C with range in H1 tensor eta, choose an orthonormal basis a0,a1 of its rank2 first-site range and write C as in §5 of the addendum. In first-site matrix blocks,

    C_{alpha,i}=|eta><v_(alpha,i)| for alpha0,1,

with all other output rows zero. The spectator-block identity for q2 gives the sum over alpha,i of the positive A_eta norms. Its first-site trace is the rank1 operator |eta><v_(0,0)+v_(1,1)|, so the subtracted term is precisely one half of that A_eta norm squared. Therefore

    q3(C)=1/2||v_(0,0)-v_(1,1)||_A^2
           +sum_off-diagonal ||v_(alpha,i)||_A^2.

This identity uses no general assertion that partial trace preserves rank2: the trace's rank1 form is explicit. A_eta is positive definite, so equality is equivalent to all off-diagonal vectors vanishing and the two diagonal vectors being one common w. Substitution gives exactly P_E tensor |eta><w| with E two-dimensional. Nonzero C implies w nonzero.

Conversely, that operator has rank2 for w nonzero and factorized form

    q1(P_E) q2(|eta><w|)
      =[2-(1/2)4] q2(|eta><w|)=0.

Thus the classification is sufficient as well as necessary. General nonzero complex scalar multiples are included by adjusting the bra vector w (with its conjugate scalar convention). Adjoint invariance gives the stated co-range version. If dim H1<2 there is no such projection, and rank1 strictness excludes nonzero zeros.

## 5. Coverage, dependency and novelty limits

The strict-coverage example has range outside the common-reference padding plane, so strict positivity is consistent with its independently reconstructed value59/36. This theorem does not show generic two-planes contain the required biseparable maximally entangled ray, nor give a uniform quantitative neighborhood or arbitrary Schmidt-spectrum extension.

The known P_E padding equality family is correctly not advertised as new. The possible new content is exclusion of other zeros within the structured ray family, conditional on GSd. This review does not establish worldwide novelty, validate the assay's historical process receipts, or provide a kernel/human/cross-vendor proof gate.
