# Addendum 2 — prime11 spectral rigidity excludes EVERY trade of size at most6

Owner MathShor / MathShor-2. Actual preceding `/bin/date`: `Sun Oct 25 14:29:47 PDT 2026`. WRITTEN CANDIDATE, unreviewed. No scientific interpreter/program. The original all-order completion question remains NOT_PROVED.

This strengthens the B/D2 trade bound to

    |D2 minus B|=|B minus D2| >= 7.

It is uniform in n and in EVERY unknown trade location, not a finite-order or finite-length check. The other bounds (B/D3>=3 and D2/D3>=3) are unchanged. Larger trades remain completely live.

## 1. The fixed and unknown terms

Use the SAME hypotheses from the common-complement gate and the first trade packet. Section2 there proves

    {1,7,13,14} subset B minus D2,
    {2,4,6} subset D2 minus B.

Let k=|B minus D2|=|D2 minus B|. Already k>=4. If k<=6, write the signed annihilator relation as

    1_A * E=0,
    E(z)=sum_(positive trade) z^j - sum_(negative trade) z^j.

After moving the seven fixed terms to one side, any root zeta of E obeys a relation with

    Q(z)=z+z^7+z^13+z^14-z^2-z^4-z^6

and at most2k-7<=5 additional signed powers of zeta. The five additional terms can have ANY exponents. Their exact signs or locations will not be assumed.

**Spectral claim.** If zeta is a root of E whose order d is divisible by11, then d=11 exactly.

## 2. Prove the spectral claim by exponent classes modulo11

The seven fixed terms of Q occupy the following classes:

| Class modulo11 | Fixed terms |
|---|---|
|1|zeta|
|2|zeta^13-zeta^2|
|3|zeta^14|
|4|-zeta^4|
|6|-zeta^6|
|7|zeta^7|

Thus there are FIVE fixed singleton classes (1,3,4,6,7), ONE paired class2, and FIVE empty classes (0,5,8,9,10). At most five unknown terms can be inserted.

### If11^2 divides d

The degree of Q(zeta) over Q(zeta^11) is11, so the powers1,zeta,...,zeta^10 are linearly independent over that field. Every grouped coefficient must vanish.

Each fixed singleton class needs at least one unknown term, consuming all five if that many are available. With fewer than five this is already impossible. With exactly five, none remains for the paired class2, which then forces

    zeta^13-zeta^2=0, so zeta^11=1,

contrary to11^2|d. Hence no such root exists.

### If11 divides d once

Write d=11m with gcd(11,m)=1, and zeta=alpha*beta with alpha a primitive11th root and beta a primitive mth root. Group by powers of alpha. Cyclotomic irreducibility over Q(beta) says the eleven grouped coefficients must all be equal. This is the standard coprime cyclotomic-field fact; coefficients include the nonzero factors beta^j.

**If a residue class remains empty**, that common coefficient is0. Then the five singleton classes again consume all five unknown terms, leaving the paired class2 unchanged. It requires beta^13-beta^2=0, hence beta^11=1. Since beta has order prime to11, beta=1 and d=11.

**If no class is empty**, all five unknown terms must lie one each in the five initially empty classes. None alters any fixed class. Comparing the three positive singleton coefficients at exponents1,7,14 gives

    beta=beta^7=beta^14,
    beta^6=beta^13=1,
    beta=1.

But the paired class2 coefficient is then0 while a positive singleton coefficient is1. They cannot all be equal. This case is impossible.

This proves the spectral claim, including arbitrary unknown signs/exponents. No conductor list or numerical root was evaluated.

## 3. Consequence for the ENTIRE unknown endpoint tile A

The annihilator equation gives A(zeta)E(zeta)=0 at every nth root. Therefore a nonzero Fourier coefficient of1_A can have either

- order prime to11; or
- order exactly11.

Let n=11^e m with gcd(11,m)=1. The written multiplier seed argument gives11||B|, so e>=1. All allowed Fourier orders divide m or11. Thus1_A is periodic modulo11m and, under the coprime identification Z_(11m)=Z_m x Z_11, has the form

    1_A(u,v)=f(u)+g(v),

with real functions f,g. Indeed its finite Fourier expansion has only characters supported on the first coordinate, only characters supported on the second, and the constant; there are no mixed modes. This is an exact finite Fourier decomposition.

### Binary separability

A function f(u)+g(v) taking only0 and1 on a full Cartesian product has one of f,g constant. If f(u)-f(u') is nonzero, it is the same nonzero difference of two binary values for EVERY v, hence it is1 or-1. Those two binary values are then fixed for all v, forcing g constant. If no such u,u' exists, f is constant.

Apply this to1_A.

**If g is constant**, A depends only on the residue modulo m. Each occupied m-residue is repeated across a full kernel of size11^e, so11^e divides |A|. Since11 divides |B|, the identity n=|A||B| would make11^(e+1) divide n, impossible.

**If f is constant**, A depends only on its residue modulo11. If it occupies s of those residues (1<=s<=11), then

    |A|=(n/11)*s,
    |B|=n/|A|=11/s <=11.

But330 divides |B|. This is impossible as well.

Both alternatives fail. Therefore k<=6 cannot occur, proving the claimed lower bound>=7.

## 4. Exact limits

This proof consumes ALL unknown factors A,B and ALL unknown trade locations when the trade size is at most6. The prime11 was not an arbitrary numerical cutoff: it comes from the literal Shor endpoints and from their forced five singleton exponent classes.

At trade size7 there can be SEVEN additional signed powers. They can populate more classes and alter the paired class2; the argument above no longer forces d=11. It must NOT be repeated with those extra terms silently absent. A larger trade can have Fourier support at orders involving11 together with other primes or higher11 powers, avoiding the binary-separability conclusion.

Thus no common-complement witness exists with the stated small trades, but no uniform obstruction for ALL trade sizes or all raw finite prefixes is yet proved. Actual D2,D3 still have not been constructed, and PR/STAB/raw finite-completion obligations remain after that gate.

Mathematical imports are explicit classical finite Fourier inversion and cyclotomic degree/irreducibility, together with the previously WRITTEN multiplier/count identities. No formal, executable, independent-family or novelty acceptance is claimed; no scientific computation, solver, replay, external model or new GO occurred.
