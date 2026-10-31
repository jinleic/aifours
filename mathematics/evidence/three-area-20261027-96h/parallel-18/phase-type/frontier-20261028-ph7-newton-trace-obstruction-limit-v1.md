# At 8/9 the combined universal Newton and trace tests still permit real hidden roots

**EXACT COUNTERPOINT TO A PROPOSED EXCLUSION METHOD, not a PH or Metzler existence witness.** MathResearch96h-2. This result prospectively imports the literal public theorem of Olga Holtz, *M-matrices satisfy Newton's inequalities*, Theorem4 ([arXiv:math/0512610](https://arxiv.org/abs/math/0512610), full PDF https://arxiv.org/pdf/math/0512610). The theorem states that the elementary symmetric functions of the spectrum of any singular or nonsingular M-matrix, normalized by the corresponding binomial coefficients, satisfy all Newton inequalities. Its hypotheses and result were read in the cited full source; no claim is made to have independently proved the paper's theorem or audited its full proof. The prior v121 source's optional Holtz non-import is not changed retroactively.

## Claim and source application

Suppose an actual PH7 generator has spectral bound0 after the normalization of `frontier-20261028-ph7-global-irreducibility-v1.md`. Its `-G` is a singular M-matrix: for t large enough `B=tI+G` is nonnegative, and Perron root0 of G gives `rho(B)=t`. Thus Holtz's theorem applies to `-G`.

For the polynomial

    P(y)=y[(y+1)^2+z]^2 (y^2+p y+q)
        = sum_{j=0}^7 e_j y^(7-j),

set `c_j=e_j/binom(7,j)`. The six necessary inequalities are

    N_j=c_j^2-c_{j-1}c_{j+1} >=0,  j=1,...,6.

At `z=8/9`, the choices `p=8,q=15` give hidden roots exactly -3,-5. With these choices EVERY N_j is STRICTLY positive, and the independent seven-dimensional centered trace-two/three necessary test in `frontier-20261028-ph7-trace23-obstruction-limit-v1.md` is also STRICTLY satisfied. Hence the combined simple spectral restrictions cannot by themselves exclude the original 8/9 PH7 case, even if one additionally assumes the two hidden roots are real and negative.

This does not assert that the displayed spectrum is realizable by any Metzler matrix. It merely gives a common point in the explicitly stated necessary inequalities. It says nothing about the stronger principal-minor inequalities also appearing in Holtz's paper, arbitrary other spectral constraints, the PH input/output numerator, positivity/normalization, or a true graph realization.

## Exact reproducible arithmetic

For general z,p,q, the coefficient list used by the independent checker is

    e0=1,                    e1=4+p,
    e2=6+2z+4p+q,
    e3=4+4z+(6+2z)p+4q,
    e4=(1+z)^2+(4+4z)p+(6+2z)q,
    e5=(1+z)^2 p+(4+4z)q,
    e6=(1+z)^2 q,            e7=0.

At `(z,p,q)=(8/9,8,15)`, exact Fraction arithmetic produces

    N1 =   437/1323,
    N2 = 79949/178605,
    N3 = 758773/2679075,
    N4 = 2568677/1607445,
    N5 = 2552737/413343,
    N6 = 2088025/35721.

All are positive. For the centered symmetric-comparison test the same point has

    tau2=874/63,  tau3=-5692/147,
    (25/42)tau2^3-tau3^2=9641252/107163 >0.

In particular the negative tau3 satisfies the required lower bound strictly. The point also has the required real conjugation and negative real parts and permits a formal real Jordan normal form with length-two visible blocks, but such a normal form is generally NOT Metzler and does not establish the Jordan structures of an actual generator.

`frontier-20261028-ph7-newton-trace-limit-check.py`, SHA256 `a47415c40b7f3f90bbd68f7445b276b78bc939352d2e1802b255672f7db7fdb2`, actually printed:

    Fraction exact: all 6 normalized Newton inequalities and centered trace2/3 strictly pass
    N1..N6: 437/1323 79949/178605 758773/2679075 2568677/1607445 2552737/413343 2088025/35721
    tau2,tau3,trace slack: 874/63 -5692/147 9641252/107163
    This is a spectral necessary-condition point, not a Metzler or PH witness.

No floating arithmetic is used in the verification. The checker verifies the arithmetic, not Holtz's theorem, a seven-state existence, or an all-variable matrix search.

## Implication for work toward the target

A successful obstruction must use an additional matrix/nonnegative-realization constraint, stronger principal-minor or higher-moment structure, the repeated-pole Jordan coupling, or the actual SAME-matrix input/exit and four-edge-delay requirements. None is ruled in or out by this strict counterpoint. The existing unrestricted PH6 result is not recounted as new, and 8/9 and the true minimum remain open. No held output was accepted as premise and earlier process findings remain.

END — explicit 8/9 spectral tuple survives both the full normalized Newton list and the centered trace-two/three test.
