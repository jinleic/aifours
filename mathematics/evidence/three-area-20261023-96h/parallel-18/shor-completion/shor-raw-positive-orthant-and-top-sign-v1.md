# Shor raw signed factors — positive-orthant rigidity fixes the top sign at ALL b-degrees

Owner MathShor-2. Actual `/bin/date` before composing: **Mon Oct 26 05:28:30 PDT 2026** (earlier observation bound). WRITTEN/unreviewed, symbolic-variable argument only. No numeric parameter substitution, scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent or new GO.

This strengthens the sign conclusion of `shor-raw-signed-factor-top-layer-and-gap-balance-v1.md` (9dadb66e…ee14b) at its FULL finite two-sided degrees, not only the deg_bP=deg_bS=1 control in `shor-raw-forced-negative-layer-and-one-sided-obstruction-v1.md`. Earlier bytes remain unchanged. It does not prove the factorization conjecture or settle Shor completion.

## 1. Literal algebraic hypotheses

Let finite integer P,S satisfy P(0,b)=S(0,b)=1, and let

    F=1+P(a+b−1)S

be a nonnegative0/1 polynomial containing b, with F(a,0)=a^n for some n>=1. These are the literal raw signed-factor conditions. Applying them to every hypothetical finite completion still uses named Reutenauer interface I5 (statement read, original proof NOT_RECONSTRUCTED). The theorem below needs no I5 proof or code conjecture once these algebraic hypotheses hold.

For positive real x,y, use P(x,y),S(x,y),F(x,y) for the ordinary COMMUTATIVE evaluations. No claim identifies raw word coefficients from these evaluations alone.

## 2. Neither signed factor has a positive-quadrant zero

**Theorem.** P(x,y)>0 and S(x,y)>0 for EVERY x>0,y>=0. In particular the highest-b raw layers of BOTH normalized factors are characteristic polynomials with POSITIVE unit coefficients, for arbitrary finite b-degrees p,q.

*Proof.* F has nonnegative coefficients and contains b, so for every fixed x>0 it is STRICTLY increasing as a polynomial in y>=0; indeed its y derivative is at least1 there.

If0<x<1, the signed identity gives F(x,1−x)=1. Strict increase makes this the ONLY nonnegative y at which F(x,y)=1. Were P or S zero at some positive y, the same identity would give F=1, hence y=1−x. But differentiating the commutative identity in y at that point gives

    F_y(x,1−x)=P(x,1−x)S(x,1−x)>0,

because the multiplier x+y−1 vanishes and F_y>=1. Neither factor can be zero there. Thus neither has any positive y-zero for0<x<1.

If x>=1 and y>0, F(x,y)>F(x,0)=x^n>=1. The signed identity then excludes a zero of either factor immediately. At y=0, U(x)=P(x,0),V(x)=S(x,0) satisfy U(x)V(x)=G_n(x)>0 for ALL x>0. Since U(0)=V(0)=1, continuity on the connected positive axis and the nonvanishing product give U(x),V(x)>0 everywhere. For each fixed x, absence of positive y-zeros and this positive y=0 value therefore give P,S>0 for all y>=0. This proves the first assertion.

Let p=deg_bP,q=deg_bS. The UNIQUE fixed-b separator in the raw top layer F_(p+q+1)=P_p b S_q already proves that all nonzero coefficients in P_p,S_q have one common sign epsilon and unit magnitude. Fix ANY positive symbolic x. The coefficient of y^p in P(x,y) is then epsilon times a nonzero polynomial in x with nonnegative integer coefficients, and likewise for S. If p>0 and epsilon were negative, P(x,y) would tend to negative infinity as y tends to positive infinity, contradicting its positivity. If p=0, the positive U(x) already rules out a negative common sign. Thus epsilon=+1 in every case. Both raw top layers are positive characteristic polynomials. ∎

The use of commutative evaluation fixes the ONE common raw sign only AFTER the raw fixed-separator purity proof. It does not infer arbitrary lower raw coefficients from a positive commutative polynomial.

## 3. Exact consequence for the Shor sign defect

The forced coefficient NEG14 of the preceding packet remains

    [z^14](P_1(z,z)V(z)+U(z)S_1(z,z))<=−1.

The present theorem fixes a positive boundary at the highest b-layer of EACH factor for every finite p,q. Thus the needed negative first-layer contribution cannot be justified by choosing an overall negative top sign. The earlier one-sided obstruction holds at all degrees, and in the p=q=1 subcase the negative contribution must occur in signed U or V. For larger p,q it may occur in genuinely lower b-layers as well.

Positivity at ALL positive scalar evaluations does NOT imply coefficientwise positivity; nor does it prove finite layers cannot repair NEG14. The unsolved Shor-specific task is to connect that forced low-layer negative coefficient to the exact raw higher-layer gap-balance identities with a contradiction for EVERY finite signed pair, or construct an actual finite pair satisfying every coefficient constraint.

No degree, arity, delay, n, raw a-gap or word-length bound was introduced. No residue closure, Perron potential or finite-dimensional border span is renamed raw STAB. H* stays FALSE/WITHDRAWN; I3/I4 retain their boundaries and I5 is named separately. Own permanent v109-A exactness MAJOR/all older findings remain, not cured. No source/shared/frozen edit, git/deletion/publication or formal/kernel/human/configured-family/executable/novelty acceptance. Same original cutoff/deadline; research continues without early final park.
