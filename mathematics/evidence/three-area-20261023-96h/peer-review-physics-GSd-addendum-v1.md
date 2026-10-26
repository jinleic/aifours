# Independent written review: dimension-universal GSd addendum

Before-creation clock observed: **2026-10-23T13:16:03-07:00**. Reviewer: `MathResearch96h`, at the parent's explicit request. Entire addendum lines1–207 read. No scientific execution, symbolic algebra program, enumeration, CLI or nested agent was used; the expansions below were derived by hand.

Reviewed file: `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261023-96h/proof-GS4-maximally-entangled-reference-ADDENDUM-1-GSd.md`.

Exact SHA256: **`c51a4c9d0665d37d91bd325b6e9771c4591207ffb44eac92beeeadbe7664ff4b`**.

The frozen d4 proof was independently reconstructed in my preceding `peer-review-physics-ME4-v1.md`; this review reconstructs the dimension-dependent changes rather than extrapolating the one admitted d4 assay.

**Verdict: 0 FATAL /0 MAJOR /0 MINOR. No substantive defect found in GSd for d>=3, its switched-complement consequence or the d2 obstruction at the stated rank boundary.** Ordinary in-harness written checking only; not all-d finite verification, kernel/human/cross-vendor acceptance or a priority verdict.

## 1. Raw identity and dimension dependence

For ||Omega_d||^2=d,

    A_d=(d-1)I+|Omega_d><Omega_d|/4,
    A_d^-1=I/(d-1)-|Omega_d><Omega_d|/[(d-1)(5d-4)].

The rank-one inverse is valid because A_d has eigenvalue(d-1)+d/4=(5d-4)/4 on Omega and d-1 on its orthogonal complement. Directly L_ab Omega=delta_ab Omega+(d-4)|ab>/4, so tau=(d-4)/4 is correct.

In the independent delta-contraction table of the d4 review, the only dimension-sensitive inner product in the I/(d-1) term is <Omega,Omega>=d. The four negative/Omega products total-F/2; the Omega/Omega product is+dF/16. All identity/negative, negative/negative and identity/Omega contributions retain their displayed swap/Bell form. Hence

    H_d=CP+PC-P+(A+B)/4+(Q+Qprime)F/4+(d-8)F/16.

For the inverse rank-one term, multiplying

    (delta_ef delta_cd+tau delta_ce delta_df)
    (delta_ab delta_gh+tau delta_ag delta_bh)

gives P12 P34+tau(FP+PF)+tau^2F, with the same co-Choi input reversal as before. Therefore S_d=H_d/(d-1)-T_d/kappa follows exactly. At d4 it reduces to the pinned earlier ID, not merely to matching numerical spectra.

## 2. Full-space Gram and complement checks

The general Gram matrix follows from the same contractions: diagonal d, opposite-pair entries Tr(X-dagger)Tr(Y), and the four mixed-pair entries Tr(X-dagger Y). On traceless matrices this is exactly G_d. The h vectors have Euclidean norm squared4 and Gram eigenvalues d+2,d-2,d,d. These are all positive for d>=3. The identity block has Gram [[d^2,d],[d,d^2]], positive definite for d>1, and is orthogonal to the traceless blocks.

Thus K has dimension2+4(d^2-1)=4d^2-2 and its orthogonal complement has dimension d^4-4d^2+2. The swapped Bell ranges cover K exactly. There is no use of this four-dimensional traceless decomposition at d2, where the h1 direction becomes dependent.

On K-perp I derive

    S_d=(A+B)/(4(d-1))+(d^2-9d+4)F/(4kappa).

Indeed the F numerator before simplification is

    (d-8)(5d-4)-(d-4)^2=4(d^2-9d+4).

Substitution in the four swap sectors gives every entry in §4's table. With d=x+3 the six distinct numerator polynomials, in table order, are

    2x^2+7x+7;
    3x^2+14x+15;
    4x^2+15x+13;
    7x^2+33x+40;
    22x^2+101x+117;
    23x^2+88x+81.

All are strictly positive for x>=0, and kappa=(x+2)(5x+11)>0.

## 3. Identity block and the first determinant certificate

The swap/Bell actions in p,q coordinates become

    C=(5/4)I-exchange,
    P=[[d,1],[0,0]], Q+Qprime=[[0,0],[2,2d]],
    F=I, A+B=2 exchange, P12 P34=[[d^2,d],[0,0]].

I obtain the useful intermediate matrices

    H_d=[[ (25d-24)/16, 2-d ],
         [ 1-d, (9d-24)/16 ]],
    T_d=[[ (d+tau)^2, d+2tau ],[0,tau^2]].

They give S_d p=C_d p and S_d's lower-right action coefficient(11d^2-37d+20)/(4kappa), exactly as stated. Multiplying the differences by the nonorthogonal Gram metric yields

    Form(C-S)=diag(0, d(d+1)(7d-4)/(2(5d-4))).

The plus form is the stated two-by-two matrix. Its determinant expands as

    (d^2/4)[18d^2-43d+20-(5-4d)^2]
      =d^2(d+1)(2d-5)/4.

Completing the square with first pivot d(5d-4)/2 gives exactly the residual coefficient d(d+1)(2d-5)/(2(5d-4)). This is positive at every integer d>=3 and negative at d2. No Euclidean-Hermitian eigenvalue calculation is incorrectly applied to an action matrix.

## 4. Independently recovered traceless matrix entries

Let g0=d+2,g1=d-2,g2=g3=d. In the normalized h basis the P12 matrix has diagonals g0/4,g1/4,d/4,d/4, off-diagonal01=sqrt(d^2-4)/4, entries02/03=-sqrt(d(d+2))/4, entries12/13=-sqrt(d(d-2))/4 and entry23=d/4.

The matrix Q+Qprime has top block

    [[(d+2)/2,-sqrt(d^2-4)/2],
     [-sqrt(d^2-4)/2,(d-2)/2]],

and bottom block [[d/2,-d/2],[-d/2,d/2]], with no other entries. Also F=diag(1,1,-1,-1), A+B=diag(2,-2,0,0), and P12 P34 vanishes.

Inserting these in H_d,T_d gives

    S00=d(d+4)/(8kappa),
    S11=(41d^2-144d+80)/(8kappa),
    S01=sqrt(d^2-4)(9d-4)/(8kappa),
    S02=S03=0,
    S12=S13=-sqrt(d(d-2))/(2(d-1)),
    S22=S33=(-d^2+14d-8)/(8kappa),
    S23=d(11d-12)/(8kappa).

Consequently, in the f_plus/f_minus basis, the two f_minus scalars and the plus three-by-three block agree with the addendum.

For the minus SOS, the z1 diagonal contributed by the first two squares is

    (d+2)(9d-4)/(8kappa)+d/(d-1)
      =(49d^2-18d-8)/(8kappa),

the actual C-S entry. The01 off-diagonal is minus sqrt(d^2-4)(9d-4)/(8kappa); the1/plus entry is positive sqrt(2d(d-2))/(2(d-1)); the plus diagonal is(d-2)/(2(d-1)). The minus scalar is(21d^2-40d+16)/(4kappa). Hence the displayed SOS is exact, not just a sign estimate. The scalar numerator shifts to21x^2+86x+85, proving strict positivity for d>=3. The kernel direction is the P12/J2 reference contraction.

## 5. Second determinant certificate: both expansions checked by hand

For the plus three-by-three block, write A0,B0,E0 as in the manuscript. Its leading two-by-two determinant numerator is

    A0 B0-(d^2-4)(9d-4)^2
      =1360d^4-5128d^3+7312d^2-4864d+1280
      =8p(d).

Thus Delta2=p(d)/(8kappa^2) is correctly normalized. The third determinant subtracts the square of the1/plus entry multiplied by Delta1, giving exactly

    Delta3=[p(d)E0-A0 d(d-2)(5d-4)^2]/(16kappa^3).

An independent unshifted expansion of its numerator is

    r(d)=1425d^6-7280d^5+15637d^4-18110d^3
         +11944d^2-4256d+640.

Expanding at d=x+3 gives, coefficient by coefficient,

    p(x+3)=170x^4+1399x^3+4325x^2+5929x+3025,
    r(x+3)=1425x^6+18370x^5+98812x^4+283834x^3
           +459127x^2+396484x+142780.

These exactly match the manuscript; all coefficients are positive. Also A0(x+3)=11x^2+52x+65, and the f_minus plus-scalar numerator becomes9x^2+40x+47. The pivots Delta1,Delta2/Delta1,Delta3/Delta2 are therefore positive. This proves positive definiteness on the three-dimensional plus block by exact square completion/Sylvester criterion, with no finite-dimension assay used for the universal claim.

## 6. d2 obstruction and rank qualification

The identity-block formulas are still valid on the independent vectors p2,q2. At d2 they give [[6,-3],[-3,1]]. Evaluating the coefficient vector(1,2) yields6-12+4=-2. Expanding p2+2q2 gives exactly the six stated nonzero coefficients3,1,2,2,1,3.

Across input pair12 versus output pair34, p2 has coefficient matrix |Omega2><Omega2| and q2 has coefficient matrix F2. The matrix |Omega2><Omega2|+2F2 has eigenvalues4 on Omega,2 on the two-dimensional symmetric-orthogonal subspace, and-2 on the antisymmetric line. Its rank is4, so it is not a Schmidt-rank-at-most-two coefficient operator. The stronger co-Choi domination failure cannot be promoted to a Werner counterexample.

In the rank2-support/two-ququart assay, all displayed vector indices remain inside the reference support, and the restricted inverse is the same I-|Omega2><Omega2|/6. The compressed raw maps therefore agree with the d2 ones; the claimed embedding is an identity, not an assumed invariance under enlarging dimension. I did not replay either this new vector or the assay's different vector of value-6/17.

## 7. Consequence and boundaries

The same completely-copositive contraction bridge already independently checked for d4 applies verbatim once GSd is proved. All relevant C_d are strictly positive swap products and all reference inverses exist for d>=3; the dimensions and PSD proofs above establish their required domination. Local-unitary transport covers every maximally entangled two-d-dimensional ray, not arbitrary Schmidt spectra.

This review establishes no all-d computational receipt and imports no assay as a proof premise. It does not check worldwide novelty, human acceptance or Lean coverage. The unrestricted W4 and arbitrary nonmaximally-entangled reference obligations remain exactly as stated in the addendum.
