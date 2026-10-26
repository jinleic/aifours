# Addendum 4 — a surviving seven-point trade forces the primitive spectrum of A to vanish

Owner MathShor / MathShor-2. Actual preceding `/bin/date`: `Sun Oct 25 14:53:03 PDT 2026`. WRITTEN CANDIDATE, unreviewed. No scientific computation.

Under the common-complement gate, let k=|D2 minus B|=|B minus D2|. The earlier proof gives k>=7. This addendum proves the uniform DISJUNCTION

    k>=8 OR Phi_n(z) divides A(z).

The second alternative remains live. In particular the statement is NOT a noncompletion theorem: an aperiodic0/1 cyclic tile may have a zero primitive Fourier coefficient without having any period.

## 1. Assume k=7

There are exactly seven fixed signed terms and seven additional signed terms in E=1_D2-1_B. All fourteen support locations are distinct modulo n. Write

    Q=z+z^7+z^13+z^14-z^2-z^4-z^6,
    E=S-Q,

where S contains FOUR unknown positive terms and THREE unknown negative terms. At any root of E the signed relation F=Q-S=0 therefore has FOUR known positive, THREE known negative, THREE unknown positive and FOUR unknown negative terms.

The endpoint multiplier facts give11|n and n>=1320. We show E cannot vanish at a primitive nth root zeta.

## 2. Exponent classes modulo11

The known classes are five singletons at exponents1,4,6,7,14, and the paired class2 containing zeta^13-zeta^2. There are five initially empty classes0,5,8,9,10.

If11^2|n, all eleven class coefficients must vanish independently over Q(zeta^11). If11 divides n once and a class remains empty, cyclotomic irreducibility likewise forces every class coefficient to vanish. First consider either of these zero-coefficient cases.

Each singleton consumes at least one unknown term. The paired class cannot have no unknown term, since that would give zeta^11=1. It cannot have just one unknown term: an equation zeta^13-zeta^2+/-zeta^u=0 would imply |zeta^11-1|=1, so zeta^11 has order6 and n=66. This contradicts n>=1320.

Hence the paired class consumes at least two unknowns. Exactly seven are available. Thus EVERY singleton has exactly one unknown term, the paired class has exactly two, and no other class is used.

The singleton terms must cancel in pairs. The paired class has four signed unit complex terms with sum0; the unit-circle quadrilateral lemma makes it a union of two opposite pairs. Its two known terms cannot cancel each other (that again would require zeta^11=1), so each must cancel one unknown term. Therefore ALL seven known terms cancel one-to-one against the seven unknown terms.

At a primitive nth root, opposite-sign terms can cancel only when their exponents agree modulo n, which is forbidden by the fourteen distinct support locations. Thus each cancellation would have to be between SAME-sign terms whose exponents differ by n/2. But the FOUR known positive terms of F would need FOUR unknown positive terms, and F has only THREE. Contradiction.

## 3. The nonempty-coefficient case is also impossible at primitive order n

It remains to consider11 exactly dividing n and NO exponent class empty after inserting the seven unknown terms. At least five unknowns must occupy the initially empty classes. At most two unknown terms can then alter the five known singleton classes. At least THREE known singleton classes stay untouched.

Write n=11m with gcd(11,m)=1 and zeta=alpha*beta, with alpha of order11 and beta of order m. All eleven class coefficients are equal over Q(beta). Each untouched singleton coefficient is plus/minus beta^a with a in{1,4,6,7,14}. Equality of any three gives

    beta^(2(a-b))=beta^(2(a-c))=1.

The gcd of pair differences for a triple of distinct elements of{1,4,6,7,14} is1,2 or3: explicitly the only larger-than1 cases are{1,4,7} with gcd3 and{4,6,14} with gcd2. Therefore m divides2,4 or6, in particular m<=6. This would give n<=66, again contrary to n>=1320.

All cases are excluded, so E(zeta)!=0 at every primitive nth root.

## 4. Conclude the spectral restriction, not periodicity

Since A*E=0 on Z_n, A(zeta)E(zeta)=0 at all nth roots. The preceding proof forces A(zeta)=0 at every primitive nth root, equivalently Phi_n|A in Z[z]. This proves the displayed disjunction.

Do NOT replace Phi_n|A by a proper period: the other Fourier modes may have several incomparable orders whose least common multiple is n. No such period or direct quotient is proved here. The entire k7/Phi_n-divisible case and all k>=8 cases remain unexcluded. The simultaneous D3 tiling, positivity, unknown endpoints and raw PR/STAB realization still have to be used for any full answer.

All arguments are WRITTEN class counts, classical cyclotomic irreducibility, elementary unit-circle geometry and finite Fourier algebra. No numerical root, interpreter, symbolic program, enumeration, replay, solver, formal gate or new GO was used. No novelty or stronger assurance is claimed.
