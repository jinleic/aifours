# Shor completion: the odd head cardinality cannot be exactly 3, 5 or 11

Owner **MathShor-2**, math-5. Native `/bin/date` immediately before writing: **Thu Oct 29 09:48:53 PDT 2026**.

**WRITTEN UNREVIEWED CANDIDATE, conditional on the named tiling imports.** This handles a genuine shared-prime residual, not only coprime head/tail odd parts. It uses Łaba–Londner Corollary 6.2/T2 explicitly. No acceptance, formal proof, human or independent-model-family verification, novelty clearance, or unrestricted original-problem solution is claimed.

## 0. Provenance and non-premises

This is same-author work developed after the separate global single-split-prime submission `frontier-20261029-global-single-split-odd-prime-power-v1.md` (`e7ea40e4…`). That submission does not exclude a shared odd prime. The present proof changes representation: a nonintegral coset cardinality rules out mixed-parity fibres, and T2 forces each fibre to remain nonconstant modulo p². A cross-parity edge would contradict that nonconstancy.

The owner's earlier fibre/cofactor exposure remains disclosed: the owner had read and considered earlier unreviewed fibre-related sources before developing the preceding all-Q route. This is not a disjoint-exposure or clean-cognition claim. No mathematical assertion from those sources is used below.

Non-premises are: `e7ea40e4…`; the separately frozen f189/2310 packet `2d6b48f8…`; `564956bf…`; the 165-family candidate `20169ac9…` and erratum `54329f3e…`, and its parent disposition; f128/Q55, f157, f174, f169 and all their author packets or parent dispositions; every earlier fixed-order branch or fibre packet; all HELD/ZERO/NONINPUT material. The elementary tools used here are restated. Parent disposition notices supply status only, not proof.

The floating-sqrt checker `2e4101b6…` and its output are not used. The separate arithmetic disclosure `owner-20261029-092233-prime-checker-arithmetic-disclosure-v1.json` (`9f17a24f…`) remains in force. Section 7 uses a new integer/Fraction-only checker. Historical process findings, checkpoint-cadence breaches and quarantines are not cleared by this proof.

## 1. Exact statement and original-code caller

Let A={0,3,8,11} and Y={0,1,7,13,14}. An anchored tiling means P,Q ⊆ Z_n, A⊆P, Y⊆Q, and P⊕Q=Z_n (every residue has one expression p+q).

> **Theorem (candidate).** Let n>14 and p∈{3,5,11}. No anchored tiling has |P|=p·2^a for any a≥0.

This includes **every** exponent of p in n, every allocation of powers of 2 between the factors, and arbitrary additional odd primes and prime powers in n. It does not assume p∤|Q|. In fact, the proof first forces p to divide |Q|, then excludes the shared-p situation.

> **Order-family corollary (candidate).** For K≥1 and p∈{3,5,11}, no anchored tiling exists at n=165·p·2^K. At n=165·p^s·2^K with s≥1, any anchored tiling would have |P|=p^j·2^a with 2≤j≤s. Thus s=1 gives no possibility.

No numerical order floor, all-order no-go or feasibility of the remaining cardinalities is asserted.

The literal Shor code is

    S = b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8} b {1,a^2,a^4,a^6} ∪ a^11 b {1,a,a^2},

where `1` denotes the empty word. For a finite UD, factor-complete extension D with its unique actual pure-a atom a^n, the border theorem gives the same-code anchored tiling with

    P = {i mod n:a^i b^k∈D, k≥1},    Q = {j mod n:b^l a^j∈D, l≥1}.

The border theorem is imported here as Restivo–Salemi–Sportelli, stated in Cordero, [arXiv:2301.13566v1, p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1). The code-completion corollary is conditional on that actual-word caller; no cyclic tiling is claimed sufficient to construct a code. The new mathematical proof below concerns the anchored tiling itself, and does not rely on an earlier author reconstruction of the caller.

## 2. Named imports and elementary conventions

For X⊆Z_M put Div_M(X)={gcd(x−x′,M):x,x′∈X}, including M from zero differences. Mask polynomials use representatives 0≤x<M: X(z)=Σ_(x∈X) z^x.

**Sands (import):** a tiling P⊕Q=Z_M implies |P||Q|=M and Div_M(P)∩Div_M(Q)={M}. Source: Łaba–Londner, [arXiv:2106.14042v3, p. 10, Theorem 2.5](https://arxiv.org/pdf/2106.14042v3).

**Tijdeman (import):** if gcd(t,|P|)=1, then tP⊕Q=Z_M, with multiplication by t injective on P. Source: [the same paper, p. 3 and the Corollary 6.2 proof on p. 26](https://arxiv.org/pdf/2106.14042v3), citing Tijdeman [47, Theorem 1] and Coven–Meyerowitz [2, Lemma 2.2].

**Łaba–Londner Corollary 6.2 (deep import):** if P⊕Q=Z_M, and at most two prime factors of M divide both cardinalities, then both P and Q satisfy Coven–Meyerowitz (T2). Label the possibly shared primes p₁,p₂; for every i≥3 the prime p_i divides at most one cardinality. Source: [arXiv:2106.14042v3, p. 26, Corollary 6.2](https://arxiv.org/pdf/2106.14042v3). Its proof uses the Coven–Meyerowitz two-prime result (their Theorem 1.1 as reproduced on p. 3), Tijdeman dilation and Theorem 6.1 subgroup reduction. Those are explicit ancestry of this import, not separately claimed new proofs.

For a mask Q and its prime-power cyclotomic divisors S_Q, (T2) says that whenever s₁,…,s_j∈S_Q are powers of distinct primes, Φ_(s₁⋯s_j) divides Q. See the same paper, p. 3, Theorem 1.1. We do **not** import T2 for arbitrary tilings outside the two-shared-prime hypothesis.

**Coset fact (elementary):** if X⊕Z=G with X⊆H a subgroup, then X⊕(Z∩(u+H))=u+H. Each point y in that coset has z=y−x in the same coset. Thus the other factor has |H|/|X| elements in each coset; in particular that ratio must be an integer.

Ordinary cyclotomic irreducibility over Q, Φ_(ℓ^j)(1)=ℓ for a prime ℓ, finite cyclic Fourier inversion, and elementary polynomial division are used with the proofs specified below. No numerical approximation is used.

## 3. Reductions and a stronger odd-difference rule

Suppose an anchored tiling with |P|=p·2^a exists.

**R1.** The integer n is divisible by 330. If n is odd, the A-difference 8 and Y-difference 1 both have gcd 1 with n. If one of 3,5,11 is missing from n, the A-difference equal to that prime also has gcd 1. Sands forbids each case. The differences used are 3=3−0, 5=8−3, 11=11−0, 8=8−0 and 1=1−0.

**R2.** Every ℓ∈{3,5,11} divides |Q|. Otherwise P⊕ℓQ tiles by Tijdeman, and ℓ lies in both divisor sets, from the A-difference ℓ and from ℓ(1−0). Since ℓ<n this violates Sands.

Consequently we may write

    n = 2^K p^v R,    |P|=p·2^a,    |Q|=p^(v−1) R·2^b,
    K≥1, v≥2, a+b=K, R odd, gcd(p,R)=1.

Let q₁,q₂ be the other two primes of {3,5,11}; both divide R. R may have arbitrary higher powers and arbitrary further odd primes.

**R3 (odd-difference rule).** If x∈Q−Q is odd and q₁|x or q₂|x, then p²|x.

Proof. Let g=gcd(x,n).

- If p∤x, choose ℓ∈{q₁,q₂} dividing x. Then t=g/ℓ is an odd integer not divisible by p, so gcd(t,|P|)=1. In the tiling tP⊕Q, the scaled A-difference tℓ=g has gcd g with n, matching x. Since g is odd and n is even, g<n: contradiction.
- Hence p|x. If p²∤x, then v≥2 implies p exactly divides g. Take t=g/p, again coprime to |P|, and use the A-difference p. The same Sands collision occurs.

Thus p² divides x. ∎

## 4. Every R-fibre of Q has a single parity

For u∈Z_R set Q_u={q∈Q:q≡u (mod R)}. Since gcd(R,|P|)=1, RP⊕Q=Z_n. The coset fact gives

    |Q_u| = (n/R)/|P| = p^(v−1)·2^b > 0.                  (4.1)

Suppose Q_u contains both parities. Every even–odd difference in that fibre is an odd multiple of R, hence divisible by q₁. R3 forces every such pair congruent mod p². Using one element of each parity shows that **all** elements of Q_u lie in a single residue class mod p².

Restriction of RP⊕Q to the coset u+RZ_n, followed by Rz↦z, gives

    V_u ⊕ P̄ = Z_N,    N=p^v·2^K,
    V_u=(Q_u−u)/R,    P̄={z mod N:z∈P}.

Multiplication by R was injective on P, so |P̄|=p·2^a. Since R is invertible modulo p², the supposed constancy of Q_u makes V_u lie in a single coset mod p². Translate it into the subgroup p²Z_N. The coset fact would then require the other factor to have

    |p²Z_N| / |V_u| = (p^(v−2)2^K)/(p^(v−1)2^b) = 2^a/p

points in every coset of that subgroup. This is not an integer because p is odd. Contradiction.

Thus every Q_u is single-parity. Write E⊔O=Z_R for the even and odd fibre indices. Both sets are nonempty: 0∈E and 1∈O, since 0,1∈Q and R>1.

## 5. T2 forces every R-fibre to be nonconstant modulo p²

The only primes that can divide both |P| and |Q| are 2 and p. Every other prime of n divides R and not |P|. Thus the exact hypotheses of Łaba–Londner Corollary 6.2 hold, with the exempt primes labelled **2,p**. In particular Q satisfies (T2).

**C1.** Q(X) is divisible by Φ_s(X) for at least one s∈{p,p²}.

Indeed the tiling mask identity forces each of Φ_p,Φ_(p²) to divide P(X) or Q(X). If Q had neither, both would divide P. Their product is

    Φ_p(X) Φ_(p²)(X) = 1+X+⋯+X^(p²−1).

Equivalently, P vanishes at every nontrivial p²-th root. Folding P modulo p² and applying finite Fourier inversion gives equal counts in all p² residue classes, so p² would divide |P|=p2^a. That is impossible. Choose one such s; the same s is used in all fibres below.

**C2.** For each prime ℓ|R and 1≤j≤v_ℓ(R), Φ_(ℓ^j)(X) divides Q(X). The tiling identity assigns that factor to at least one of P,Q. If it divided P, evaluating the integer polynomial divisibility at 1 would imply that ℓ divides |P|, impossible because |P| has primes only 2,p. Thus it divides Q.

**C3.** By (T2), Φ_(sm)(X) divides Q(X) for **every divisor m of R**, including m=1. Write m as a product of one prime power for each of its distinct primes, all different from p; C1 and C2 give precisely the prime-power factors required by (T2).

Since gcd(s,R)=1, we have the polynomial identity

    ∏_(m|R) Φ_(sm)(X) = Φ_s(X^R).                           (5.1)

To see it, the roots on either side are exactly the roots ζ for which ζ^R has order s, equivalently those whose order is sm for some m|R. They are simple and both polynomials are monic. Thus C3 implies Φ_s(X^R)|Q(X) in Z[X].

Decompose by exponent residue mod R:

    Q(X) = Σ_(u=0)^(R−1) X^u F_u(X^R),
    F_u(Z) = Σ_(q∈Q_u) Z^((q−u)/R).

Every F_u has nonnegative integer coefficients and weight |Q_u|>0. Decompose the integer quotient Q(X)/Φ_s(X^R) in the same residue basis. Uniqueness of this decomposition yields Φ_s(Z)|F_u(Z) for **each** u.

If all q∈Q_u were congruent to c mod p², every exponent (q−u)/R would be congruent to one value d mod p², since gcd(R,p)=1. At a primitive s-th root ζ, this would give

    F_u(ζ) = |Q_u| ζ^d ≠ 0,

contradicting Φ_s|F_u. We have therefore proved:

> Every Q_u is **nonconstant modulo p²**, despite being single-parity.

This is not an assertion of full equidistribution modulo p². The conclusion is only nonconstancy, and it is exactly what the final step needs.

## 6. Connectivity gives the contradiction

Consider the undirected graph on Z_R with edges u↔u+q₁ and u↔u+q₂. It is connected because q₁ and q₂ are coprime, so their generated subgroup is all of Z_R. The parity partition E⊔O is nontrivial; along a path from 0∈E to 1∈O there must be an edge crossing between the two parts.

Let u∈E and u′∈O be its endpoints. Their difference is divisible by q₁ or q₂, including when representatives wrap modulo R, because both primes divide R. For **any** q∈Q_u and q′∈Q_(u′), x=q−q′ is odd and divisible by that prime. R3 gives p²|x. Since both fibres are nonempty, fixing an element in one fibre shows every element of the other is congruent mod p². In particular Q_u is constant mod p². This contradicts §5 and proves the Theorem.

The connected graph in this step is the unrestricted q₁/q₂-step graph; we need only the existence of one edge crossing the parity partition. We do not assume that the bipartite graph of all crossing edges is connected.

## 7. Order-family caller and finite controls

For n=165p^s2^K with p∈{3,5,11}, each other small prime occurs to the first power, so R2 places both in |Q|. Hence |P|=p^j2^a for 0≤j≤s. The case j=0 is also impossible: if |P| were a power of 2, dilating P by the odd part T of n forces Q to meet every class mod T; a tail q≡6 (mod 165) has an odd difference from 0 divisible by 3 or an odd difference from 1 divisible by 5. Scaling the corresponding A-difference as in R3 gives a Sands collision. The theorem excludes j=1. Thus exactly the unresolved interval 2≤j≤s remains; s=1 is excluded entirely.

New checker: `frontier-20261029-single-small-shared-prime-check-v1.py`, SHA256 `c3c2f1302760e463c8db0b1e31b3589c6900040ab1c63b8fc7aaef93fb76c495`, 163 LF / 5,465 bytes. The owner executed exactly those bytes in a fresh namespace of the retained eval kernel before writing this packet. It returned `"result": "PASS"`. Scientific arithmetic uses integers and `fractions.Fraction`; polynomial division is monic integer long division. It loads no old checker output.

**WRITTEN-checked-in-kernel, exact finite scope only:**

- 152,064 bounded odd-difference cases have the claimed admissible dilation witness whenever p² fails to divide a difference divisible by q₁ or q₂.
- 576 bounded coset-cardinality cases give exactly 2^a/p, with denominator p, for p∈{3,5,11} and v=2,…,5.
- Φ_pΦ_(p²)=1+⋯+X^(p²−1) and (5.1) are checked by exact polynomial multiplication/division for (p,R)=(3,55),(5,33),(11,15), with s=p and s=p². The six degrees of (5.1) are 110,330,132,660,150,1650.
- 310 positive single-residue polynomials have nonzero remainder modulo the relevant Φ_s.
- Six explicit **unanchored** cyclic tilings exercise both choices s=p and s=p² and have nonconstant R-fibres modulo p². They are controls, not original-code completions or anchored tilings.
- The q₁/q₂-step graphs are checked connected for R=55,275,715 (p=3); R=33,99,429 (p=5); and R=15,45,195 (p=11).

The universal exponents, arbitrary R, classical imports, original-code caller, and theorem as a whole are not certified by these finite checks. They require the written proof. Independent-model CLI, human, formal/kernel and novelty reviews remain not performed by this owner.

## 8. Literal remaining gap and review request

This result does **not** exclude an odd head part 3^j,5^j or11^j with j≥2; a shared odd prime outside {3,5,11}; or at least two distinct odd head primes. No residual order is claimed feasible. The unrestricted original Shor question remains OPEN.

A reviewer must check the all-n quantifiers, the two successive admissible dilations in R3, the translated coset count in §4 for arbitrary v, Corollary 6.2 with exempt primes exactly 2,p, the low-cyclotomic dichotomy C1, all-m T2 in C3, identity (5.1), the residue-basis quotient giving every F_u divisible by Φ_s, and the existence of a crossing edge without an unjustified bipartite-connectivity claim. All named non-premises and arithmetic/process disclosures remain mandatory.

This is a separate candidate, not an expansion or correction of any earlier gate. No parent ledger or frozen author/reviewer file has been changed.

**END OF SINGLE-SMALL-SHARED-PRIME CANDIDATE.**
