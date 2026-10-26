# Addendum 5 — an integer spectral-density obstruction for positive-filter trades

Owner MathShor / MathShor-2. Actual preceding `/bin/date`: `Sun Oct 25 14:55:10 PDT 2026`. WRITTEN CANDIDATE, unreviewed. No scientific computation. This is an additional infinite-family obstruction, not the full Shor answer.

## 1. General lemma

Let A+B=Z_n be a finite direct factorization, |B|=b. Suppose integer cyclic polynomials E,U,F satisfy

    A*E=0,
    E=U*F,

with U NONNEGATIVE and nonzero, of total coefficient mass w=U(1). Assume every nth root zeta with F(zeta)=0 has order dividing L. Put g=gcd(n,L).

Then

    b <= g*w.                                      (PF)

Proof. C=1_A*U is a nonnegative integer function and is nonzero. The equation C*F=0 makes its Fourier support lie on characters of order dividing g. Thus C(x+g)=C(x) exactly. Its sum on one period of length g is a positive INTEGER, at least1. Therefore its total mass is at least n/g. But that mass is |A|w=nw/b. Hence nw/b>=n/g, giving PF. No sign cancellation is allowed in U; without nonnegativity/nonzero mass this argument would be false.

## 2. Application to the forced Shor trade mask

Use

    Q=z+z^7+z^13+z^14-z^2-z^4-z^6,
    F_u=z^u-Q.

The exact root lemma RL in addendum1 proves: every root of unity of F_u has order in{1,4,5}, for EVERY integer u. Thus any ACTUAL common-complement trade of the form

    1_D2-1_B = U*(z^u-Q),
    U>=0, U!=0,

must satisfy

    U(1) >= |B|/gcd(n,20) >= |B|/20.

Since330 divides |B|, the mass of U must be at least17. This excludes all such positive-filter representations with mass<=16 at ALL orders, even if filter shifts, word lengths and unknown endpoints are unbounded.

The RL proof is an explicit named LOCAL dependency, not a newly assumed general theorem. It uses classical cyclotomic degree/irreducibility and the displayed coefficient-square identities, and remains WRITTEN/unreviewed.

## 3. Why the obvious eight-point primitive-root control still does not tile

For even n let h=n/2 and consider the formal mask

    E=(1+z^h)(z^u-Q).

For suitably distinct positions it has eight positive and eight negative terms, and E vanishes at EVERY primitive nth root because zeta^h=-1. Thus the seven-point primitive-spectrum argument cannot be extrapolated to this eight-point annihilator merely by omitting extra terms.

Nevertheless it cannot be an ACTUAL Shor common-complement trade: its positive filter U=1+z^h has mass2, while PF would require |B|<=40, contradicting330||B|. This exclusion uses the actual factorization cardinality and integer positivity in addition to the annihilator zeros.

## 4. Exact limitation

No theorem says an arbitrary actual larger trade admits the displayed positive-filter factorization. A signed filter, a nonfactorable trade, a different base mask, or a positive filter of larger mass is not excluded by PF. In particular neither the general nonuniform seven-point case nor all k>=8 cases are settled here.

The common-complement gate and every actual raw PR/STAB/GP realization obligation remain. No new bound on n, completion witness, all-order noncompletion, formal/executable/family or novelty acceptance is claimed. The proof is finite Fourier algebra and integer counting in writing only; no program, interpreter arithmetic, solver, replay or new GO occurred.
