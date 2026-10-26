# Addendum 3 — H* is false as formalized: an exact written countercontrol

Actual preceding `/bin/date`: `Sun Oct 25 13:43:44 PDT 2026`. Originals remain immutable. This is an additive mathematical correction to R7/H* and to the claimed 'new type' consequence, not a solution of Shor's question. No scientific interpreter, enumeration or program was used.

## 1. Withdraw H* as an open route premise

R7 in the route note and checkpoint04 formalized H*: every normalized full-rank factorization of a cyclic group has, up to automorphism, factor translation and exchange, one product factor and one universal complement for some coprime CRT data. This is TOO STRONG and is FALSE. Oppositely oriented products of elementary Szabo-style factorizations give counterexamples, including at orders divisible by1320 with 330 dividing the start-side cardinality and an even end-side cardinality with at least three prime divisors.

Thus WITHDRAW the description of H* itself as a currently open classification hypothesis and WITHDRAW the inference that being outside product-plus-universal form necessarily means a genuinely new type of Sands counterexample. The exact R8/R9 construction-class obstruction is not contradicted; it is simply insufficient. This does not refute Dai's informal 'essentially different' remark: that language may quotient out products/inflations, which H* did not do.

## 2. Elementary building block, fully specified

For three distinct primes p,q,r, define

    G(p,q,r) = Z_(p^2) x Z_(q^2) x Z_(r^2),
    P = [p] x [q] x [r],
    H = p Z_(p^2) x q Z_(q^2) x r Z_(r^2),

where [p]={0,...,p-1}. Clearly P+H=G directly, |P|=|H|=pqr.

In H take the three coordinate lines

    C_p = p Z_(p^2) x {q} x {0},
    C_q = {0} x q Z_(q^2) x {r},
    C_r = {p} x {0} x r Z_(r^2).

They are pairwise disjoint: C_p/C_q have different fixed third coordinate, C_q/C_r have different first coordinate, and C_r/C_p have different second coordinate. They all exclude0. Let e_p=(1,0,0), e_q=(0,1,0), e_r=(0,0,1), and define

    Q = (H minus (C_p union C_q union C_r))
        union (C_p+e_p) union (C_q+e_q) union (C_r+e_r).

### Direct tiling verification

For example,

    P + C_p = Z_(p^2) x ([q]+q) x [r].

This set is invariant under e_p, with unique P/C_p representations because [p]+pZ_(p^2) is direct. The corresponding two other sets are invariant under e_q and e_r. The three old blocks were disjoint in the partition P+H=G, so replacing each block by an identical covered block with its translated Q-component preserves a DIRECT partition. Thus P+Q=G and |Q|=pqr. This verifies both existence and uniqueness without enumeration.

### Normalization and full rank

0 remains in Q. P generates all three coordinate cyclic groups: it contains each unit coordinate vector. Q has a point with p-coordinate1 in C_p+e_p, a point with q-coordinate1 in C_q+e_q, and a point with r-coordinate1 in C_r+e_r. As the three group orders are pairwise coprime, no prime dividing |G| divides every integer CRT representative of Q. Therefore Q generates the cyclic group G as well.

### Non-transversality

Modulo the subgroup indices p,q,r, every unmoved H point maps to(0,0,0). There are pqr-p-q-r such points. For (p,q,r)=(2,3,5) this is20; for (7,11,13) it is970. So in both blocks Q has distinct elements congruent modulo pqr. Q is NOT a complete residue system modulo its own cardinality. No list of all points is needed for this count.

## 3. A countercontrol at an admissible Shor-sized order

Apply §2 at triples (2,3,5) and (7,11,13). Use their integer CRT representatives in

    G_1 = Z_900,  |P_1|=|Q_1|=30,
    G_2 = Z_((7*11*13)^2),  |P_2|=|Q_2|=1001.

Inflate the first block to Z_1800. Take canonical representatives P_1,Q_1 in[900] and set

    P_1^+ = P_1 union (P_1+900),   Q_1^+ = Q_1.

This is a direct factorization of Z_1800: the old representation modulo900 is unique, and its two possible lifts to modulo1800 are supplied exactly by adding0 or900 to the P_1 component. Cardinalities are60 and30. Both factors generate Z_1800. For P_1^+, use the old generating set and the element900; for Q_1^+, the prime divisors of1800 are unchanged from900, so the old full-rank condition suffices.

Now take the OPPOSITELY ORIENTED product

    G = Z_1800 x Z_(1001^2),
    A = P_1^+ x Q_2,
    B = Q_1^+ x P_2.

Since gcd(1800,1001)=1, G is cyclic of order

    n = 1800*1001^2 = 2*(2*3*5*7*11*13)^2.

The product factorization is direct. Its exact sizes are

    |A| = 60*1001 = 60060,
    |B| = 30*1001 = 30030,
    |A||B| = n.

Both contain0 and generate G. Further,

    1320 | n,
    330 | |B|,
    2 | |A|,

and |A| has six distinct prime divisors. These are compatible with the inherited size/order restrictions, but DO NOT give the required Shor containments.

## 4. Why neither side can be any 'product factor' in H*

### General necessary condition

For ANY coprime CRT data Z_n=product Z_(m_i) and product P=product P_i with P_i complete modulo d_i, the cardinality is D=product d_i. Reduction of P modulo D is bijective: CRT on the coprime d_i identifies it with the product of the residue bijections P_i -> Z_(d_i). Thus every product factor, for any such data (including r=1), is a complete residue system modulo its OWN cardinality.

Failure of this property is invariant under translations and automorphisms x->ux with gcd(u,n)=1: these act bijectively on Z_D because D|n.

### The constructed A fails

Reduction modulo |A|=60*1001 is the product of reduction modulo60 in G_1 and modulo1001 in G_2. Fix one P_1^+ point and choose two distinct Q_2 points in the unmoved970-point block. Their Q_2 coordinates are both0 modulo1001. These give two distinct A points congruent modulo |A|. Therefore A cannot be a product factor for ANY coprime CRT data.

### The constructed B fails

Reduction modulo |B|=30*1001 is the product of reduction modulo30 in G_1 and modulo1001 in G_2. Fix one P_2 point and take two distinct unmoved Q_1 points (there are20). They are congruent modulo30, giving two distinct B points congruent modulo |B|. Therefore B cannot be a product factor for ANY such data either.

It follows that no exchange, translation or automorphism can put this pair in product-plus-universal form. This disproves H* exactly as formalized, even at the displayed admissible order/cardinality restrictions.

## 5. What this does and does not establish

- The construction is an explicit finite written CONTROL: it excludes H* as an available classification route and refutes my 'outside the class implies a new type' wording.
- It is built by elementary known-style operations, so no novelty claim is made.
- It is CRT-separable (between1800 and1001^2). The route note's R3 rules out the FULL Shor containments in such a product. Therefore it is NOT a FACT witness and certainly NOT a raw completion.
- Neither product factor contains the required A0/B0 in a way asserted here. No claimed witness is hidden in coordinate notation.
- A more careful irreducible/classification conjecture might survive products and inflations, but none is stated as a theorem, imported premise or sufficient proof here. A descent preserving ALL forced Shor points would itself be a new unproved step.
- The original all-order FACT/PR/STAB gap remains. No global noncompletion or finite completion follows.

All checks above are written set/block/cardinality arguments. No native solver, interpreter arithmetic, code enumeration, replay, formal verifier or new GO was used. The route's prior results remain unreviewed except where separately adopted; this addendum also requires its own actual review.
