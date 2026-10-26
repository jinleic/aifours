# Independent written review: reference-angle obstructions

Before-creation clock observed: **2026-10-23T13:34:56-07:00**. Reviewer: `MathResearch96h`, at the parent's request. Entire proof lines1–151 read; no scientific execution, symbolic algebra program, root approximation, assay replay or nested agent was used.

Reviewed file: `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261023-96h/proof-reference-angle-obstructions-v1.md`.

Exact SHA256: **`ccb579da080fcfba43c44dafbb7aa8511f989d33696c36193736ec5105abde84`**.

**Verdict: 0 FATAL /0 MAJOR /0 MINOR.** The two explicit negative co-Choi values, general two-parameter evaluation and Schmidt-rank-only obstruction reconstruct by hand. They do not constitute negative rank2 Werner coefficient operators, a full angular classification or a novelty result.

## 1. Inverse with the unused levels retained

For c=(1,1,t,u), N=2+t^2+u^2 and D_ab=N-(c_a^2+c_b^2)/2, the diagonal D is strictly positive: N-max c_a^2 is positive, including when t or u is the largest coefficient. Expansion of Lambda tensor Lambda gives A=D+|eta><eta|/4. Its inverse is therefore D^-1-|h><h|/(4+z), with h=D^-1 eta and z=<eta,D^-1 eta>.

On the two inside levels, D_ab=a=1+t^2+u^2; the other diagonal entries of eta use2+u^2 and2+t^2. Hence z=2/a+t^2/(2+u^2)+u^2/(2+t^2), exactly as claimed. The L_ab and L_ab-dagger matrix-unit contractions for inside input/output indices are also correct. The unused components are retained through z and h; replacing them by a two-level inverse would be an error, which the manuscript does not make.

## 2. Independent reconstruction of all three p2/q2 entries

Let A=1/a for this paragraph only. The I/D part of the inverse gives the following quadratic-form entries on p2,q2, obtained by the same raw delta products as in the earlier ID review:

    pp: 4A+z/4,
    pq: -A+z/8,
    qq: -2A+z/4.

The pp entry can be checked directly from sum_b L_bb-dagger Omega2=Omega2+eta/2. Its D^-1 norm is4/a+z/4. For the other entries, the dimension-free negative/identity contractions are weighted by1/a, while the eta/eta contraction has weight z rather than a truncated norm2/a.

For a separate rank-one-inverse check, contracting h with the displayed L expression gives the scalar kernel

    <h,L_ab-dagger|cd>>
      =A delta_ab delta_cd+(z/4-A)delta_ac delta_bd.

Write B=z/4-A. Its co-Choi quadratic operator on the inside indices is

    A^2 P12 P34+AB(FP+PF)+B^2F.

Using ||p2||^2=||q2||^2=4 and <p2,q2>=2, its three form entries are respectively

    pp: 4A^2+2Az+z^2/4,
    pq: 2A^2+Az+z^2/8,
    qq: 4A^2-Az+z^2/4.

Subtracting these divided by4+z from the D^-1 entries gives precisely the manuscript's three rational S entries. This reconstructs the raw contractions, not merely the final witness sign.

C_B on p2,q2 has form [[3,-3/2],[-3/2,3]], so w=p2+2q2 gives9. Combining pp+4pq+4qq yields

    <w,S w>=[7z-(32+10z)/a-28/a^2]/(4+z).

Adding9 proves the exact two-parameter formula(E).

## 3. Rank3 and rank4 specializations and exact rational values

For u0,s=t^2, substitution of a=1+s and z=2/(1+s)+s/2 gives

    2(8s^3+47s^2+75s-12)/[(s+1)(s^2+9s+12)].

The cubic is strictly increasing for s>=0, negative at0 and positive eventually, so its one positive root is a threshold for this fixed witness only. At s1/16, the cubic is-3649/512 and the denominator is54689/4096, hence the value is-58384/54689. As a direct alternative fraction check, a17/16 and z1041/544 give numerator-3649/578 and denominator4+z=3217/544; division gives the same exact result.

For t=u,s=t^2, the expression reduces to

    (2/3)(34s^3+65s^2+36s-3)/[(1+2s)(1+s)^2].

Its derivative polynomial102s^2+130s+36 is strictly positive. At s1/16 the cubic is-999/2048 and the denominator2601/2048; the full value is-74/289. Directly, a9/8,z182/99 give numerator-148/99 and denominator578/99, confirming the same rational value. At s1 the value is22/3, consistent with the positive uniform Omega4 theorem.

The references have genuinely three and four nonzero Schmidt coefficients respectively. Together with the written positive uniform full-rank theorem, the rank4 example decisively rules out a rank-only GS criterion; the rank3 example also rules out odd-rank and rank-at-least3 sufficiency.

## 4. Rank and theorem boundary

The coefficient matrix of w across input pair:output pair is |Omega2><Omega2|+2F2. Its eigenvalues are4 on Omega,2 on the two-dimensional symmetric orthogonal complement and-2 on the antisymmetric line. Thus its rank is4, not2. The negative co-Choi form falsifies symmetric domination at the stated reference rays and cannot be relabeled as a Werner/distillation witness.

The fixed-vector cubic thresholds are necessary tests for GS, not sufficient GS characterizations. Nothing in this review removes the need for a complete separate proof of the embedded uniform Omega3 reference or of arbitrary Schmidt spectra. The unrestricted W4 and asymptotic NPT questions remain unproved, and no primary-priority or formal proof gate is established.

Parent verification must be read with the operative parent-verification and timestamp errata; this review's hand derivation does not depend on the parent's Fraction spot checks or estimated labels.
