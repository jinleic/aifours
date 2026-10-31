# Shor completion: T2-free exclusion of head cardinalities p·2^a for p=3,5,11

Owner **MathShor-2**, math-5. Native `/bin/date` immediately before writing: **Thu Oct 29 13:31:10 PDT 2026**.

**WRITTEN UNREVIEWED CANDIDATE; elementary finite checks as specified below.** This is the parent-requested T2-free successor to the separately dispositioned f201 result. It reconstructs both coprime dilation and equal-gcd exclusion from elementary finite-group arithmetic, so neither Sands, Tijdeman nor Łaba–Londner Corollary 6.2/T2 is a proof import for the cyclic-tiling theorem. The actual-word code caller is the one explicitly named classical border import in §1. This new packet has not inherited the f201 review or parent adoption.

## 0. Provenance and non-premises

Main's new direction reports f201 adopted at its conditional LL/T2 scope and explicitly asks for a separate T2-free proof, noting its reviewer identified a nonintegral-coset route. The observation that **every** constant mod-p² fibre, not just a mixed-parity fibre, is impossible comes from that parent-reported f201 review observation. This is reviewer-guided same-author work, not an independently discovered or blind argument. Section 4 gives the complete proof from the literal assumptions; it does not use the f201 result, its written proof, or its disposition as a mathematical premise.

The owner had earlier read and considered unreviewed fibre/cofactor sources before the old all-Q route. This actual exposure, the floating-sqrt-checker disclosure `9f17a24f…`, both owner cadence disclosures, the parent-recorded service gap, and all historical HELD/ZERO/NONINPUT records remain in force. There is no clean-cognition, disjoint-exposure, independent-author, or retrospective source-read claim.

No theorem or computational outcome from f189, f194, f201, f212, f217, any Q55/fibre/cofactor packet, the higher-5-power countermodel, or any HELD/ZERO material is assumed in the proof. In particular **no T2, cyclotomic-factor allocation, subgroup-reduction theorem, or SAT result is used**. The owner has considered the parent-reported f201 reviewer observation described above; it is a provenance/route fact, not a substitute for §4.

## 1. Exact theorem and the actual-code caller

Put A={0,3,8,11} and Y={0,1,7,13,14}. An anchored tiling means P,Q⊆Z_n, A⊆P, Y⊆Q, and every residue of Z_n has a unique expression p+q, p∈P,q∈Q.

> **Theorem (T2-free candidate).** Let n>14, a≥0 and p∈{3,5,11}. No anchored tiling P⊕Q=Z_n has |P|=p·2^a.

The quantifiers include arbitrary n, arbitrarily large powers of p in |Q|, all 2-adic allocations, and every other prime divisor of n.

The literal Shor code is

    S = b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8} b {1,a^2,a^4,a^6} ∪ a^11 b {1,a,a^2},

where `1` is the empty word. The Restivo–Salemi–Sportelli actual-word border theorem, stated in Cordero, [arXiv:2301.13566v1, p. 3, Thm 1.1](https://arxiv.org/pdf/2301.13566v1), supplies the following named import: for any finite uniquely decipherable, factor-complete D containing S with actual pure-a atom a^n, the borders

    P={i mod n:a^i b^k∈D,k≥1},   Q={j mod n:b^l a^j∈D,l≥1}

form P⊕Q=Z_n and contain A and Y respectively. This caller is conditional on the named theorem, and an arbitrary cyclic tiling is not asserted to construct a code. The new theorem itself is a statement about anchored cyclic tilings.

## 2. Elementary dilation and equal-gcd exclusion

The following two lemmas prove the exact tools needed from ordinary finite group algebra, integer arithmetic, the Chinese remainder theorem and Fermat's little theorem. No general tiling-structure theorem is assumed.

**Dilation lemma.** If P⊕Q=Z_n and t≥1 with gcd(t,|P|)=1, then tP⊕Q=Z_n; multiplication by t is injective on P.

*Proof.* It is enough to treat t=ℓ prime, ℓ∤|P|; then iterate over the prime factors of t. Work in the commutative group algebra F_ℓ[Z_n]. Let p and q be the characteristic sums of P and Q, and let G=Σ_(z∈Z_n)[z]. The original tiling is pq=G. In characteristic ℓ, the freshman's dream gives

    p^ℓ = Σ_(x∈P)[ℓx]                         (with multiplicities).

Also pG=|P|G, so

    p^ℓq = p^(ℓ−1)G = |P|^(ℓ−1)G = G             in F_ℓ[Z_n],

using Fermat's little theorem in the last step. In the corresponding nonnegative **integer** group algebra, every coefficient of (Σ_(x∈P)[ℓx])q is congruent to 1 mod ℓ, hence at least 1. Their total is |P||Q|=n, so all n coefficients are exactly 1. This is a direct tiling by the scaled multiset and Q; it also forbids repeated values ℓx from different x, since Q is nonempty. Thus ℓP has |P| elements. Repeating this for each prime factor of t is valid because the scaled set retains the same cardinality. ∎

**Equal-gcd exclusion.** For any actual tiling P⊕Q=Z_n and nonzero differences d_P∈P−P, d_Q∈Q−Q, the gcds gcd(d_P,n),gcd(d_Q,n) cannot be equal.

*Proof.* Suppose they equal g<n. Put m=n/g and write d_P=gu,d_Q=gv, where gcd(u,m)=gcd(v,m)=1. Choose w≡v u^(−1) (mod m). For each prime ℓ dividing n but not m, additionally impose w≡1 (mod ℓ). CRT permits all these congruences because those primes are coprime to m. The resulting w is a unit mod n and wd_P≡d_Q (mod n). Since |P| divides n, gcd(w,|P|)=1. By the dilation lemma, wP⊕Q tiles. Writing d_P=p−p′ and d_Q=q−q′ gives wp+q′≡wp′+q. Unit multiplication keeps p,p′ distinct, so these are distinct representations, contradiction. ∎

**Coset fact.** If X⊕Z=G and X lies in a subgroup H, then X⊕(Z∩(u+H))=u+H for every coset: any y=x+z in u+H has z=y−x in that coset. Hence every such coset contains exactly |H|/|X| points of Z; the quotient must be an integer. This is an elementary counting fact, not a subgroup-reduction theorem import.

## 3. All-order reductions and the tail rule

Suppose for contradiction that the theorem's anchored tiling exists.

**330 divides n.** If n were odd, the P-difference 8 and Q-difference 1 would both have gcd 1 with n. If one of 3,5,11 did not divide n, the P-difference equal to that prime and the Q-difference 1 would again both have gcd 1. Both cases violate equal-gcd exclusion. The witnesses are 3=3−0, 5=8−3, 11=11−0 and 1=1−0.

**Each of 3,5,11 divides |Q|.** Otherwise, for such a prime ℓ, the dilation lemma gives P⊕ℓQ. The A-difference ℓ and the scaled Y-difference ℓ(1−0) both have gcd ℓ with n, which is smaller than n>14. Equal-gcd exclusion contradicts this.

Thus, writing q₁,q₂ for the two members of {3,5,11} other than p, we have

    n=2^K p^v R,        |P|=p·2^a,        |Q|=p^(v−1)·R·2^b,
    K≥1, v≥2, a+b=K,   R odd, gcd(R,p)=1, q₁q₂|R.         (3.1)

There is no restriction on other prime powers dividing R.

**Tail rule.** If x=q−q′ is an odd difference of actual Q-elements and q₁|x or q₂|x, then p²|x.

*Proof.* Let g=gcd(x,n), so g is odd and g<n. If p∤x, choose ℓ∈{q₁,q₂} dividing x, and set t=g/ℓ. Then t is odd and p∤t, hence coprime to p2^a. In tP⊕Q, the actual A-difference tℓ has gcd g with n, the same as x, contradicting equal-gcd exclusion. Thus p|x. If p²∤x, then v≥2 makes p exactly divide g. Set t=g/p, again odd and coprime to p2^a, and use the actual A-difference p to get the same contradiction. Therefore p²|x. ∎

## 4. Every fibre is nonconstant modulo p² — no T2

For each r∈Z_R let Q_r={q∈Q:q≡r (mod R)}. Since gcd(R,|P|)=1, the dilation lemma gives RP⊕Q=Z_n. The coset fact gives

    |Q_r| = (n/R)/|P| = p^(v−1)2^b > 0.                    (4.1)

Fix r. Restrict RP⊕Q to the coset r+RZ_n, translate by −r, and identify RZ_n with Z_N by Rz↦z, where N=p^v2^K. This yields

    V_r⊕P̄=Z_N,   V_r=(Q_r−r)/R,   P̄={x mod N:x∈P}.

The scaled P is injective, so |P̄|=p2^a and |V_r|=p^(v−1)2^b.

Suppose **all** elements of Q_r are congruent mod p². Since R is a unit mod p², all elements of V_r lie in a single coset of p²Z_N. Translate V_r into that subgroup; translation preserves the tiling. The coset fact, with X=V_r and H=p²Z_N, would make every P̄-coset count equal to

    |p²Z_N|/|V_r| = p^(v−2)2^K / (p^(v−1)2^b) = 2^a/p.

The last number is not an integer because p is odd. This contradiction proves:

> **Every** nonempty Q_r contains at least two residues modulo p².       (4.2)

This conclusion does not assume mixed parity, cyclotomic divisibility, or T2. It is the parent-reported reviewer observation, proved here with all quotient and cardinality steps explicit.

## 5. Parity and connectivity contradiction

**Every Q_r has one parity.** Otherwise choose an even and an odd element in Q_r. Any even–odd difference of elements of this same fibre is an odd multiple of R, hence divisible by q₁. By the tail rule it is divisible by p². Fix one even and one odd element; comparison with the element of opposite parity shows that every element of Q_r has the same residue mod p². This contradicts (4.2).

Let E,O⊆Z_R be the even- and odd-fibre indices. Both are nonempty: 0∈E and 1∈O, since 0,1∈Q and q₁q₂|R makes their classes distinct.

The undirected graph on Z_R with steps ±q₁ and ±q₂ is connected: q₁,q₂ are distinct primes, so integers u,v exist with uq₁+vq₂=1. A path from 0∈E to 1∈O must contain an edge between some r∈E and s∈O. Its index difference is ±q₁ or ±q₂ mod R, so **every** difference q−q′ with q∈Q_r,q′∈Q_s is odd and divisible by the corresponding small prime. The tail rule gives q≡q′ (mod p²) for every such cross pair. As both fibres are nonempty, each is constant mod p². This contradicts (4.2).

Thus no tiling in the theorem exists. No assumption that the graph of all crossing edges is itself connected is made. ∎

## 6. Corollary and literal residual

For p∈{3,5,11}, K,s≥1, at n=165·p^s·2^K, the two small primes different from p occur to the first power and therefore lie in |Q|. Consequently |P|=p^j2^a with 0≤j≤s. The theorem excludes j=1. The j=0 case is also impossible by an elementary argument: if |P|=2^a, dilating P by the odd part of n shows Q meets the class 6 mod 165. Every odd Q-difference divisible by one of 3,5,11 gives an equal-gcd collision after multiplying the corresponding A-difference by an odd scalar; but q−0 has that property when q is odd and q−1 when q is even. Hence only 2≤j≤s remains, and s=1 is excluded.

This corollary is not a claim about all orders, no numerical order floor is asserted, and higher powers p^j with j≥2 are not excluded by this proof. The original unrestricted finite-completion question remains OPEN. The separate f212 scope on all powers of 3 has its own parent disposition; it is not used to strengthen this packet.

## 7. Exact finite checks and independent-review boundary

The owner executed a new bounded control **in the eval kernel**, using Python integers, `math.gcd`, integer group-ring convolution and finite loops only:

- At (n,|P|,ℓ)=(12,4,3),(18,3,2),(30,5,3), three explicit tilings satisfy the displayed group-algebra congruence, and the ℓ-scaled factor remains injective and tiles. A noncoprime multiplier at n=12 fails as expected. These are synthetic controls, not Shor completions.
- For every n=2,…,48, every a,b∈Z_n with gcd(a,n)=gcd(b,n) was checked to admit a unit u with ua≡b mod n: 19,431 ordered equal-gcd cases. This does not replace the written all-n CRT proof.

These checks do not prove the universal theorem, verify the border import, or confer formal/kernel/human/independent-model/novelty acceptance. The proof of the cyclic-tiling theorem is §§2–5, with no T2 or solver result. The discarded floating-sqrt checker was neither loaded nor used.

A fresh review must check: the finite-characteristic group-algebra congruence and coefficient-sum argument, CRT unit lifting for all prime-power cases, the exact fibre quotient and nonintegral coset count, both cases of the tail rule, and the existence of a crossing edge. It must also retain the original-code border import and the reviewer-guided provenance in §0. This packet is a separate immutable candidate; it changes no previous review or disposition.

**END OF T2-FREE SINGLE-SMALL-SHARED-PRIME CANDIDATE.**
