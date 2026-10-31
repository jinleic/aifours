# Higher powers of 5: a joint complement obstruction for the constructed tail family

Owner **MathShor-2**, math-5. Native `/bin/date` immediately before writing: **Thu Oct 29 13:33:15 PDT 2026**.

**WRITTEN UNREVIEWED CANDIDATE.** This proves a joint constraint for **every complement of one explicitly defined tail family**, not for every tail set satisfying the Shor constraints. It is not an all-higher-5-power exclusion, a completion/no-go theorem, an adoption, a formal/kernel proof, or a novelty claim. The unrestricted original problem remains OPEN.

## 0. Relation to the prior construction and proof imports

The tail family below is the one displayed in the separate f217 candidate `frontier-20261029-five-powers-tail-anchored-T2-countermodel-v1.md`, SHA256 `7073ae6a7410ba5465dba68e25642aacaa1d9790345929e61ba776f2c5819594`. Main reports f217 frozen for review; no f217 verdict or claimed theorem is used here. The definition is reproduced verbatim in mathematical content, and all properties needed below are re-proved. In particular, this packet does **not** assume that the explicit tail has any particular complement.

The following classical fact about cyclotomic degrees is named as an import: Φ_m is irreducible over Q and [Q(ζ_m):Q]=φ(m). For gcd(m,k)=1, the joint field Q(ζ_m,ζ_k)=Q(ζ_(mk)): the product of primitive roots is primitive of order mk and both factors are powers of it. The totient identity φ(mk)=φ(m)φ(k) then gives [Q(ζ_m,ζ_k):Q(ζ_k)]=φ(m). The finite-field fact that a primitive 2^j-th root over F_11 has degree ord_(2^j)(11) is also used; it follows from its Frobenius orbit α,α^11,α^(11²),…. Both are ordinary named algebraic inputs, not a formal proof certificate.

Coprime dilation is reconstructed from finite group algebra in §2, not imported from another author packet. No T2, Q55, other fibre theorem, earlier review verdict, SAT result or HELD/ZERO body is a premise. This is same-author work after f217 and the earlier fibre/cofactor exposure; no clean-cognition, independent-author or blind-review claim is made. The earlier arithmetic/cadence/process findings remain in force.

## 1. Exact theorem and the literal constructed tail

Let e≥2, K≥4, D=2^K, m=5^(e+1), n=33Dm, h=n/5=33D5^e. Let Y={0,1,7,13,14}. Define f:Z_11→Y by

    f(0)=0, f(1)=1, f(2)=13, f(3)=14, f(7)=7,
    f(j)=0 for j∈{4,5,6,8,9,10}.

For r∈{0,…,32}, put g(r)=r when r∈Y; otherwise g(r)=1 if r≡1 (mod 3), and 0 otherwise. Let q_r be the unique residue mod n with

    q_r≡g(r) (mod D),    q_r≡f(r mod 11) (mod m),    q_r≡r (mod 33).

Set

    Q={q_r+jh (mod n):0≤r<33, 0≤j<5}.                          (1)

The q_r lie in distinct classes mod 33, and h has order 5, so |Q|=165. For every y∈Y, the three CRT residues prescribed for q_y are exactly those of y; thus Y⊆Q. Also Q+h=Q.

> **Theorem (candidate).** For **every** P⊆Z_n with P⊕Q=Z_n, there is a function φ:Z_D→Z_11, periodic with period 2, such that
>
>     p mod 11 = φ(p mod D)    for every p∈P.                    (2)
>
> Consequently no such P can contain both 0 and 8. In particular, this Q has no complement containing the full actual-head set A={0,3,8,11}.

The theorem does not exclude any other Q at the same orders. In §6 an explicit unanchored complement is displayed, so the conclusion is not vacuous. The finite checks are owner-only; no parent/human/independent-model-family acceptance has been performed.

## 2. Dilation and the projection of an arbitrary complement

If X⊕Z=Z_n and gcd(t,|X|)=1, then tX⊕Z=Z_n. For a prime ℓ∤|X|, in F_ℓ[Z_n] the freshman's dream gives X^ℓ=Σ_(x∈X)[ℓx]. With G the sum of all residues, XZ=G and XG=|X|G imply X^ℓZ=|X|^(ℓ−1)G=G mod ℓ. The corresponding integer coefficients are nonnegative, congruent to 1 mod ℓ, and sum to n; hence they are all exactly 1. This also proves injectivity on X. Iterate over the prime factors of t. This is the complete dilation argument used here.

Now fix **any** complement P of Q. Its cardinality is

    |P|=n/165=D·5^e.                                             (3)

Since gcd(33,|P|)=1, 33P⊕Q tiles and multiplication by 33 is injective on P. Because Q+h=Q, two distinct members of 33P cannot differ by a multiple of h: a nonzero multiple would produce two representations after shifting any Q-element, and zero would contradict injectivity. Therefore two distinct P-elements cannot agree mod h/33=D5^e. By (3), the reduction

    P → Z_(D5^e)                                                 (4)

is bijective. This conclusion uses no assumed head anchor and no particular complement.

## 3. Nonvanishing of the tail Fourier coefficients

Let ω be any D-th root of unity, η any 11th root, and ξ any **nontrivial** 5^e-th root. The product χω,η,ξ(x)=ω^xη^xξ^x is a character of Z_n. The shift h is divisible by D,11 and 5^e, so using (1),

    Q̂(ω,η,ξ) = 5 Σ_(j=0)^10 η^j ξ^(f(j)) c_j(ω),

where c_j=Σ_(0≤r<33, r≡j mod 11)ω^(g(r)). Directly from g,

    c_0=c_1=2+ω;       c_2=2+ω^13;
    c_3=1+ω+ω^14;      c_7=2+ω^7;
    c_j=2+ω for j∈{4,5,6,8,9,10}.                             (5)

In particular c_0 is nonzero because |ω|=1.

**Claim.** Q̂(ω,η,ξ)≠0 for all such ω,η,ξ.

- If η≠1, η is a primitive 11th root. Its minimal polynomial over Q(ω,ξ) is Φ_11 of degree 10 by the coprime cyclotomic degree fact in §0. A degree-at-most-10 polynomial vanishing at η must have all 11 coefficients equal. The coefficients at j=0 and j=1 are c_0 and c_0ξ, which differ since c_0≠0 and ξ≠1. So the sum is nonzero.
- If η=1, the sum divided by 5 is the value at ξ of

      7c_0 + c_0 X + c_7 X^7 + c_2 X^13 + c_3 X^14.           (6)

  If ξ has order 5^s with s≥2, its minimal polynomial over Q(ω) has degree φ(5^s)≥20. Polynomial (6) has degree at most 14 and nonzero constant coefficient 7c_0, so it cannot vanish at ξ. If ξ has order 5, reduce the exponents in (6) modulo 5. The resulting degree-4 polynomial has constant coefficient 7c_0 and X-coefficient c_0, which are different in characteristic zero. It cannot be a scalar multiple of Φ_5=1+X+X²+X³+X⁴, the minimal polynomial over Q(ω). This covers both cases.

Thus the claim holds without a selected numeric root, approximate arithmetic, or an assumption that Q is a standard tile.

## 4. Every complement has one mod-11 label per mod-D row

The tiling identity says P̂(χ)Q̂(χ)=0 for every nontrivial character χ of Z_n. For every character in §3, ξ≠1 makes χ nontrivial; hence P̂(ω,η,ξ)=0 for all ω,η and every nontrivial ξ.

Fix j∈Z_11 and r∈Z_D. Fourier inversion first in η and ω shows that

    Σ_(p∈P: p≡j mod 11, p≡r mod D) ξ^p = 0

for every nontrivial 5^e-th root ξ. Fourier inversion in Z_(5^e) then implies: for this fixed (j,r), the number of P-elements in each residue class mod 5^e is the same nonnegative integer c_(j,r).

By the bijection (4), for each fixed r and each residue mod 5^e exactly one P-element exists. Therefore Σ_(j mod 11)c_(j,r)=1. Every c_(j,r) is a nonnegative integer, so exactly one of them is 1 and the others are 0. Define φ(r) as its mod-11 index. This proves (2) **except for its asserted period**.

If P contains 0 and 8, then

    φ(0)=0,     φ(8)=8    in Z_11,                              (8)

because K≥4 makes 0 and 8 distinct residues mod D.

## 5. The joint multiset recurrence

Fold the original tiling onto Z_D×Z_11. Every residue there has n/(11D)=15·5^e representations from the folded P and Q. By §4 each P-row r mod D contains exactly 5^e points, all with mod-11 label φ(r).

The Q-multiplicities are 5m_(j,g), where normally m_(j,0)=2, m_(j,1)=1, with these three changes:

    j=7: replace one g=1 by g=7;
    j=2: replace one g=1 by g=13;
    j=3: replace one g=0 by g=14.                              (9)

For a fixed target z mod D and x mod 11, the regular part contributes exactly 3 after dividing the folded representation count by 5·5^e: as j runs through Z_11, both j+φ(z) and j+φ(z−1) run through all of Z_11. Equality to the target count therefore requires the three exceptional positive terms to equal the three removed terms **as multisets**:

    {7+φ(z−7), 2+φ(z−13), 3+φ(z−14)}
      = {7+φ(z−1), 2+φ(z−1), 3+φ(z)}             in Z_11.     (10)

All shifts are mod D. Summing the three elements on both sides yields

    φ(z−7)+φ(z−13)+φ(z−14)−2φ(z−1)−φ(z)=0      in F_11.    (11)

This is a joint consequence of the same complement and all 33 actual tail classes. It does not follow from checking head differences one at a time.

## 6. The recurrence forces period 2 for every K≥4

Let E be the forward-shift operator on functions Z_D→F_11 and put

    H(X)=1+X+X^7−2X^13−X^14 ∈ F_11[X].

Equation (11) is H(E)φ=0. Also E^D−1=0. We prove

    gcd(H(X), X^(2^K)−1)=X²−1       in F_11[X]                (12)

for every K≥4. The polynomial X^(2^K)−1 is squarefree in characteristic 11.

First H(1)=H(−1)=0. The following explicit finite-field Bézout identity checks that H has no other common root with X^32−1:

    S(X)H(X)+T(X)(X^32−1)=X²−1.                              (13)

All coefficients are in F_11. In ascending degree order they are

    S=[5,4,7,2,2,5,4,9,2,1,10,10,7,10,5,0,10,8,5,1,0,8,7,4,7,1,3,6,2],
    T=[6,9,10,9,4,7,9,7,4,10,2].

For roots of order 2^j with j≥6, the minimal polynomial over F_11 has degree ord_(2^j)(11)=2^(j−2)≥16, whereas deg H=14. To see the order formula, v_2(11²−1)=3, and for r≥1, 11^(2^r)≡1 mod 8, so each further squaring increases v_2(11^(2^r)−1) by exactly 1. Hence v_2(11^(2^r)−1)=r+2, and the first power of 2 giving 11^d≡1 mod 2^j is d=2^(j−2). The finite-field Frobenius orbit gives the minimal-polynomial degree. Therefore no root of order at least 64 is a root of H. Together with (13), this proves (12).

Bézout for the gcd (12), applied to H(E) and E^D−1, gives (E²−1)φ=0. Thus φ(z+2)=φ(z) for every z. In particular φ(8)=φ(0), contradicting (8). The theorem follows. ∎

For a complement without the head anchors, (2) still holds: it says all even P-elements have one common residue mod 11, and all odd P-elements have one common (possibly different) residue mod 11.

## 7. Nonvacuity and finite exact checks

For every e≥2,K≥4, one unanchored complement is

    P₀={33·(m t+D u) mod n : 0≤t<D, 0≤u<5^e}.

For x∈Z_n, r=x mod 33 determines q_r. Dividing x−q_r by 33 reduces the representation to z=m t+D u+D5^e j in Z_(Dm). Reducing mod D uniquely determines t; reducing mod 5^e then determines u; the remaining multiple of D5^e uniquely determines j mod 5. Thus P₀⊕Q=Z_n. Its φ is constantly 0, and 8∉P₀. This complement does not contain the actual head A and is not a code witness.

Checker `frontier-20261029-five-power-constructed-tail-joint-check-v1.py`, SHA256 `30edce4a8f1fc699c7b17fc32579c0fd54d30ddd37d8488b7a9f03cdb098e20e`, 114 LF / 3,904 bytes, was executed exactly once at those bytes in the owner eval kernel and returned `"result": "PASS"`. It uses integers only, no float, solver, external model or prior checker output. Its finite scope is:

- direct coefficient multiplication in F_11 checks (13); the arrays in (13) are written in ascending degree;
- exact modular powers check the claimed 11-orders for 2^j, j=3,…,16; the all-j valuation induction is written above;
- for (e,K)=(2,4),(3,4),(2,5), direct CRT construction verifies the six exceptions in (9), the stated P₀/Q sizes and complete finite sumsets of sizes 66000,330000,132000;
- at D=16, the anchor-compatible abstract map φ(z)=z mod 11 has φ(0)=0,φ(3)=3,φ(8)=8,φ(11)=0 but fails (10) at z=0: the two multisets are {5,5,5} and {0,3,6}. This is a negative control on the joint recurrence, not a complement.

These controls do not certify the all-e,K proof, the cyclotomic field-degree imports, any other Q, or the original Shor question. They are not a triple-verifier witness acceptance.

## 8. Review obligations and remaining gap

A review must reconstruct: the scope as one literal Q-family; elementary 33-dilation and projection injectivity; nonvanishing for **all** characters in §3, including η=1 and order-5 ξ; the Fourier inversion leading to integer c_(j,r); the folded-count derivation of the three-term multiset identity; the F_11 Bézout identity and all higher 2-power order argument; the original head-anchor caller; and nonvacuity. The earlier f217 result is not an imported verdict.

The first unresolved step is to prove a corresponding joint constraint for an arbitrary candidate Q satisfying Y⊆Q and the real tiling requirements, or to construct an actual P,Q with all head and tail anchors. Our special f/g labels and six multiplicity changes are not justified for arbitrary Q. Therefore the all-higher-5-power head problem, all head-15 alternatives, and the original unrestricted completion problem remain OPEN.

**END OF CONSTRUCTED-TAIL JOINT COMPLEMENT OBSTRUCTION.**
