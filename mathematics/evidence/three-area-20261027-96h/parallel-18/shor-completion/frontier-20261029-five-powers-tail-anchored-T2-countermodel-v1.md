# Higher head powers of 5: a tail-anchored T2 tiling where all old-head scalar tests pass

Owner **MathShor-2**, math-5. Native `/bin/date` immediately before writing: **Thu Oct 29 13:22:56 PDT 2026**.

**WRITTEN countermodel to a proposed proof route; bounded cases checked by exact integers in the owner's eval kernel.** This gives a genuine cyclic tiling and a stronger, all-exponent explanation of why the previous single-shared-prime fibre argument cannot automatically be extended to higher powers of 5. It is **not** an anchored-border tiling, a finite-code completion, an original-problem solution, a formal proof, an independent-model-family verification, or a novelty claim. Full independent finite-witness checking has not been performed.

## 1. The exact statement

Let A={0,3,8,11} and Y={0,1,7,13,14}. For every pair of integers

    e ≥ 2,    K ≥ 4,    n = 33·2^K·5^(e+1),

there exist explicit P,Q⊆Z_n such that:

1. P⊕Q=Z_n, |P|=2^K·5^e and |Q|=165;
2. Y⊆Q, but P∩A={0}: the remaining three actual head anchors are **absent**;
3. for every integer t coprime to |P| and every nonzero difference δ∈A−A, no gcd(tδ,n) appears among gcd(q−q′,n) for distinct q,q′∈Q;
4. the actual Q-mask satisfies Coven–Meyerowitz (T2); its prime-power cyclotomic divisors are exactly Φ_3, Φ_11 and Φ_(5^(e+1));
5. for every residue r mod 33, Q_r={q∈Q:q≡r (mod 33)} has exactly five elements, all congruent mod 5^e, and their mod-5^(e+1) residues are exactly the five distinct lifts of that common class. Each Q_r is single-parity.

The fourth item is proved directly below, not adopted from a parent result. The third item checks the entire infinite family of scalar Tijdeman/Sands exclusions that would follow from the old head anchors, including same-parity comparisons and the A-difference 8. Since this P lacks 3,8,11, it is not a counterexample to any valid theorem requiring A⊆P.

In particular, no argument using only the following facts can exclude every higher-5-power anchored tiling: actual tiling, these cardinalities, Y⊆Q, all old-head **scalar** gcd exclusions, single-parity/equidistributed mod-33 fibres, and Q-side T2. This family realizes all of them without the full head anchor. A correct original-target proof must exploit a stronger fact that fails here.

## 2. Explicit construction

Put D=2^K, m=5^(e+1), h=n/5=33·D·5^e. All congruences below use integer representatives, and CRT applies to the pairwise coprime moduli D,m,33.

Define f on Z_11 by

    f(0)=0, f(1)=1, f(2)=13, f(3)=14, f(7)=7,
    f(j)=0 for j∈{4,5,6,8,9,10}.

Thus every f(j) lies in Y, and each value in Y has a different residue mod 5. For r∈{0,…,32} define

    g(r) = r                      if r∈Y,
           1                      if r∉Y and r≡1 (mod 3),
           0                      otherwise.

For each r, let q_r be the unique residue mod n with

    q_r ≡ g(r) (mod D),   q_r ≡ f(r mod 11) (mod m),   q_r ≡ r (mod 33).

Define the sets

    Q = {q_r+jh (mod n) : 0≤r<33, 0≤j<5},
    P = {33·(m t+D u) (mod n) : 0≤t<D, 0≤u<5^e}.            (6)

Every y∈Y occurs literally in Q: choose r=y. Then g(y)=y, f(y mod 11)=y, and y has the prescribed residue mod 33; CRT gives q_y=y. For different r the Q-elements have different residues mod 33. Within each r the step h has order 5 mod n. Therefore |Q|=33·5=165.

All P-elements are multiples of 33. They are distinct: dividing by 33 maps them to Z_(D m); reduction mod D uniquely determines t because gcd(m,D)=1, and reduction mod 5^e then uniquely determines u because gcd(D,5)=1. Hence |P|=D5^e. Also 0∈P and 3,8,11∉P.

## 3. P⊕Q is an actual tiling

Fix any x∈Z_n. Its residue r mod 33 uniquely chooses q_r. The difference x−q_r is divisible by 33. In Z_(D m), write

    z = (x−q_r)/33,     z = m t + D u + D5^e j.             (7)

There is a unique 0≤t<D satisfying (7) mod D, since m is a unit mod D. There is then a unique 0≤u<5^e satisfying (7) mod 5^e, since D is a unit mod 5^e. The remaining difference is divisible by D and 5^e, hence by D5^e, and uniquely determines 0≤j<5 modulo mD/(D5^e)=5. Since h/33=D5^e, equation (7) is precisely x=p+(q_r+jh) mod n with p∈P and q_r+jh∈Q.

Every step was unique, so this is a genuine direct tiling of the finite cyclic group, not a relaxation of the direct-sum equation. The missing head anchors remain the exact reason it is not an anchored tiling.

## 4. All scalar old-head gcd exclusions hold

The distinct absolute A-differences are {3,5,8,11}. If gcd(t,|P|)=1, then t is odd and 5∤t. As n has only the other primes 3 and 11 to the first power, gcd(t,n)∈{1,3,11,33}, and each choice is realized by an admissible t. Therefore the **complete** set of forbidden scalar-anchor gcds is

    F={gcd(tδ,n):gcd(t,|P|)=1, δ∈A−A, δ≠0}
     ={3,5,8,11,15,24,33,55,88,165,264}.                    (8)

This list is independent of e≥2,K≥4: δ=5 contributes exactly one factor of 5, and δ=8 contributes exactly three factors of 2.

For q∈Q, its parity is odd iff r=q mod 33 is 1 mod 3. This follows from g, because h is divisible by D. Its residue mod 25 is f(r mod 11), because h is divisible by 5^e and e≥2.

Take distinct q,q′∈Q.

- If q−q′ is odd, their mod-3 residues differ, so 3 does not divide the difference. If 5 divides the difference, the two f-values, drawn from Y with pairwise different residues mod 5, are equal; hence 25 divides it. If 11 divides the difference, the two mod-11 indices agree, so their f-values are equal and again 25 divides it. Thus an odd difference has none of the odd gcds in (8).
- If q−q′ is even, the possible even mod-D representatives g are {0,14}, and the possible odd representatives are {1,7,13}. Same-parity differences of these values are 0, ±6, ±12, or ±14. None has 2-adic valuation 3; when the difference is 0 mod D its valuation is at least K≥4. Every even gcd in (8) has 2-adic valuation exactly 3. Hence none occurs.

Consequently **every** distinct Q-pair avoids F. This is a written all-e,K argument; the finite check in §7 is only a control.

## 5. The Q-mask satisfies T2 but its fibres are constant mod 25

Every Q_r contains precisely the five elements q_r+jh. They have the same residue mod 5^e, since 5^e|h, and different residues mod 5^(e+1), since v_5(h)=e. They are single-parity because D|h. Since e≥2 they are constant mod 25.

Let Q(X)=Σ_(q∈Q)X^q with representatives in [0,n). It is uniform mod 33 with weight 5 in each residue, hence vanishes at every nontrivial 33rd root and owns Φ_3, Φ_11 and Φ_33.

For any d|33 and any primitive root ζ of order 5^(e+1)d, the element ζ^h has exact order 5: gcd(5^(e+1)d,h)=5^e d. At ζ, replacing q_r+jh by its representative mod n has no effect, and

    Q(ζ) = (Σ_r ζ^(q_r)) · (Σ_(j=0)^4 (ζ^h)^j) = 0.

Thus Φ_(5^(e+1)d) divides Q(X) for all d|33. In particular Φ_(5^(e+1)) divides Q. Since Q(1)=165=3·5·11 and Φ_(p^j)(1)=p, Q cannot have a second distinct prime-power divisor with the same prime, or a prime-power divisor for any other prime: a product of the distinct monic cyclotomics would force an extra prime factor in 165. Thus its complete prime-power divisor set is

    S_Q={3,11,5^(e+1)}.

The factors established above are exactly every product required by (T2): Φ_3, Φ_11, Φ_33, Φ_(5^(e+1)d) for d|33. Hence Q itself satisfies (T2), proved from the displayed construction and ordinary cyclotomic divisibility.

The contrast with the p^1 shared-prime obstruction is concrete. At higher exponent, Q can own its single 5-power cyclotomic factor at level e+1, while every Q_r remains constant mod 25. In the quotient Z_(D·5^(e+1)), its fibre size is 5 and the mod-25 subgroup has D·5^(e−1) elements, so the corresponding coset quotient D·5^(e−1)/5 = D·5^(e−2) is an integer. Neither the nonintegral-coset argument nor low-level fibre nonconstancy is automatic.

## 6. Exact next gap for the original target

This family contains P and Q as a genuine direct tiling with the correct |P| form and the full Y anchors, and it already passes every scalar consequence generated from A. It also has a T2-satisfying Q. Nonetheless P is contained in 33Z_n, so 3,8,11 are absent.

Therefore a higher-5-power exclusion must use the **simultaneous actual presence** of those three head elements, not merely their separate scalar gcd exclusions, or else introduce another fully justified stronger property. The most direct remaining question is whether any other complement of this Q, or of a more general tail set obeying the same necessary conditions, can contain A. This packet does not solve that complement question and does not assert that these Q admit such a complement. More generally, higher 5-powers and the original unrestricted Shor problem remain OPEN.

This is a new structural representation, not a repeated scalar/arc-consistency scan. It also separates a genuine cyclic tiling witness from the original-code completion claim: only the former is asserted here, and only at this explicit family.

## 7. Exact finite controls, provenance and review scope

The owner computed integer CRT representatives with moduli (D,m,33), constructed P and Q from (6), and enumerated the sums and Q-pair gcds in a retained eval kernel. The actual observed controls were:

| (e,K) | n | head size | tail size | distinct P+Q residues | Q-pairs checked | old-head scalar conflicts |
|---|---:|---:|---:|---:|---:|---:|
| (2,4) | 66000 | 400 | 165 | 66000 | 13530 | 0 |
| (3,4) | 330000 | 2000 | 165 | 330000 | 13530 | 0 |
| (2,5) | 132000 | 800 | 165 | 132000 | 13530 | 0 |

In each case all five q_y equalled y, Y⊆Q, P∩A={0}, and every one of the 33 Q-fibres had five residues with one mod-5^e value and five mod-5^(e+1) values. The all-e,K tiling, gcd exclusions and T2 facts are proved in §§2–5; they are not extrapolated from this table. Only integer arithmetic and `math.gcd` were used; no float, CAS, solver, network, prior checker output or held scientific source was used. These are same-owner finite controls; triple verification, a parent read, human review and independent-model-family verification were not performed.

Same-author earlier fibre/cofactor exposure, the floating-sqrt-checker disclosure, checkpoint-cadence findings, and all HELD/ZERO/NONINPUT records remain in force. No earlier unreviewed or dispositioned theorem is used as a mathematical premise; the finite-group, cyclotomic, CRT and divisor facts used above are explicitly reconstructed. A reviewer must in particular check (7), the completeness of F, the nonzero differences in (8), the exact order of ζ^h and the prime-power count from Q(1)=165.

**END OF HIGHER-FIVE-POWER TAIL-ANCHORED T2 COUNTERMODEL.**
