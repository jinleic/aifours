# FACT at all orders: unknown endpoints must break the forced-data separator

Owner MathShor / MathShor-2. Actual preceding `/bin/date`: `Sun Oct 25 14:03:47 PDT 2026`. WRITTEN CANDIDATE, unreviewed. No computation. Original finite-completion target NOT_PROVED.

## 1. Scope

Let A+B=Z_n be a FACT pair with ALL unknown additional elements retained:

    A0={0,3,8,11} subset A,
    B0={0,1,7,13,14} subset B.

The written multiplier lemma M in the original dossier proves 330||B| and2||A|, so660|n. This is inherited, not a new bound. Unlike the saturated multiplier route on just A0/B0/C, the theorem below forces a specific interaction involving UNKNOWN pure endpoints in EVERY such pair. It does not prove that the interaction is impossible.

## 2. The quotient660 cannot tile directly

There is no FACT solution at modulus660: it would have |B|>=330 and |A|>=4, contradicting |A||B|=660.

Since660|n, let pi:Z_n->Z_660. Projection of A+B covers Z_660. The projected supports retain all literal seeds, because660>14. If pi(A)+pi(B) were direct, it would be a FACT solution at660, impossible. Hence there exist DISTINCT quotient SUPPORT pairs with the same sum. They necessarily differ on BOTH coordinates; otherwise equality of one coordinate and the sums would make the other equal too.

Consequently there are a,a' in A and b,b' in B such that

    a-a' = b'-b (mod660),
    a-a' != 0 (mod660), b'-b != 0 (mod660).          (L1)

No fixed size or cutoff on the unknown factors was assumed.

## 3. An unknown-endpoint difference is forced outside its seed class

Define the symmetric residue set

    T_660={r in Z_660 : gcd(r,660) in {1,2,6,12}}.

Zero is not in T_660. Hand comparison of the fixed seeds gives:

- Positive A0 differences are3,5,8,11, with gcds modulo660 equal to3,5,4,11. Every nonzero seed end-difference is OUTSIDE T_660.
- Positive B0 differences are1,6,7,12,13,14, with gcds1,6,1,12,1,2. Every nonzero seed start-difference is INSIDE T_660.

Let r be the nonzero common residue in L1. Exactly one of the following necessary events holds (or both endpoint classes have other violations):

    r in T_660  => a-a' is a new END-difference class;
    r notin T_660 => b'-b is a new START-difference class.

In the first case a,a' cannot both belong to A0. In the second b,b' cannot both belong to B0. Thus at least one actual pure endpoint beyond the literal Shor endpoints is involved in this forced cross-interaction. It is not enough to preserve the separator on the known endpoints forever.

This statement is about DIFFERENCES of the entire unknown factors. It is not a claim that every individual added endpoint lies in a particular residue class.

## 4. The common quotient difference must be resolved in higher arithmetic

Write

    delta_A=a-a', delta_B=b'-b,
    d_A=gcd(delta_A,n), d_B=gcd(delta_B,n).

Then

    d_A != d_B,
    gcd(d_A,660)=gcd(d_B,660)=gcd(r,660)<660.          (L2)

The second line follows from660|n and L1.

For the first line, suppose d_A=d_B. In a cyclic group the unit group is transitive on residues of each fixed gcd with n: divide by the common gcd, solve the unit congruence modulo the remaining factor, and choose the unused prime-power components to be units. Thus some u coprime to n has u*delta_A=delta_B modulo n. As |A| divides n, gcd(u,|A|)=1, so M says uA+B is direct. But

    u*a+b = u*a'+b' (modn)

with distinct A-preimages (delta_A is nonzero modulo660 and hence modulo n), a contradiction. This proves L2 using only the already-written multiplier lemma; no additional Sands theorem is silently imported.

Equivalently, the unique A/B decompositions must distinguish the two endpoint differences by at least one prime-power component of n BEYOND what reduction modulo660 sees. This is an arithmetic lifting requirement on the unknown additions, not a zero-run ambiguity at modulus n.

Indeed

    a+b-a'-b' = 660*k

has a nonzero residue modulo n. If it were0 modulo n it would already contradict the original factorization. Therefore one cannot cancel660, call k=0, or treat L1 as an actual raw-code ambiguity.

## 5. Relation to all-order noncompletion

The old multiplier-saturation theorem says the forced16 words and known border pieces preserve their separator at every product length. It does NOT permit extending that separator to the unknown full factors. L1/L2 now prove that such a blanket extension is impossible in every FACT pair: unknown additions have to pay the lifting requirement.

What remains unproved is that ALL these requirements cannot be met in ONE finite endpoint configuration and then in ONE finite actual code. In particular:
- New prime factors and higher prime powers can distinguish d_A and d_B; none is bounded away here.
- No iteration is shown that forces infinitely many new primes, endpoints or bridge arities.
- L1/L2 do not imply a negative coefficient, uncancelled internal pole or nonzero high-arity STAB deficit in the raw v2 criterion.
- They do not establish FACT, a cbc, or a raw completion.

A successful next step would show that the actual full16-word/GP constraints make this mandatory endpoint lifting nonterminating or contradictory. That uniform step is OPEN in this packet. It must retain every unknown endpoint/delay/bridge and every admissible order, rather than extrapolate from the seed or a finite-depth failure.

No scientific interpreter, enumeration, solver, replay, nested agent, external model or new GO occurred. These are written congruence/counting arguments only.
