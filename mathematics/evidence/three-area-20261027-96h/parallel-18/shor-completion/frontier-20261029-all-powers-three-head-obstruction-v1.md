# Shor completion: no power of 3 can be the odd part of the head cardinality

Owner **MathShor-2**, math-5. Native `/bin/date` immediately before writing: **Thu Oct 29 09:57:22 PDT 2026**.

**WRITTEN UNREVIEWED CANDIDATE.** The proof is universal in the order and in the exponents. Its three named imports are the actual-word border theorem, Sands' divisor exclusion, and Tijdeman's dilation theorem. **No T2, no Corollary 6.2 and no prior scientific packet is a premise.** A finite residue checker supports only the exact scope listed in §6. The original unrestricted finite-completion question remains OPEN.

## 0. Provenance and non-premises

This is same-author work developed after the separate global split-prime packet `e7ea40e4…` and the single-small-shared-prime packet `da734f2a…`. The latter addressed odd head part 3 only to the first power and used T2. This proof addresses **every positive power of 3**, with a different elementary three-class certificate. Neither earlier packet supplies a lemma here; all required arguments are restated.

The owner has already disclosed reading and considering earlier unreviewed fibre/cofactor sources before the preceding all-Q route. There is no disjoint-exposure, clean-cognition or independent-author claim. No theorem, proof guide or output from those earlier sources is used as a premise.

Other non-premises are: f189/`2d6b48f8…`; `564956bf…`; `20169ac9…` and its erratum `54329f3e…` and parent disposition; f128/Q55, f157, f174, f169 and their source packets or dispositions; every fixed-order or fibre packet; all HELD/ZERO/NONINPUT material. Current disposition notices are status only. The discarded floating-sqrt checker `2e4101b6…` and its output are not used. The arithmetic disclosure `9f17a24f…`, all historical findings and the recorded cadence breaches remain binding records; none is cleared by the new proof.

The three-class proof arose from a fresh exact projection onto parity, residue mod 55, and residue mod 9. An exploratory arc-consistency calculation found an empty domain at class 25. The written proof below replaces that propagation output by an explicit short certificate involving classes 3,25,45. No arc-consistency algorithm, search verdict or particular model is needed by the universal proof.

## 1. Exact theorem and original-code caller

Put A={0,3,8,11}, Y={0,1,7,13,14}. An anchored tiling is P,Q⊆Z_n with A⊆P, Y⊆Q and P⊕Q=Z_n.

> **Theorem (candidate).** For n>14, no anchored tiling has |P|=3^e·2^a with e≥1 and a≥0.

This does not assume any upper bound on n, e, a, the exponent of 3 in |Q|, or the number or exponents of the other primes in n.

> **Corollary (candidate).** For K,v≥1, there is no anchored tiling at n=55·3^v·2^K. Equivalently, this excludes every order 165·3^s·2^K with s≥0,K≥1, for all tail cardinalities.

These are not an unrestricted no-go or a numerical lower bound on completion order.

For the literal Shor code

    S = b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8} b {1,a^2,a^4,a^6} ∪ a^11 b {1,a,a^2},

where `1` denotes the empty word, a finite UD, factor-complete extension D with its unique actual pure-a atom a^n has actual borders

    P={i mod n:a^i b^k∈D,k≥1},    Q={j mod n:b^l a^j∈D,l≥1}.

The Restivo–Salemi–Sportelli theorem, as stated in Cordero, [arXiv:2301.13566v1, p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1), gives P⊕Q=Z_n and A⊆P,Y⊆Q. This actual-word caller is an explicit classical import. The theorem and corollary consequently exclude the same actual border cardinalities and pure-a orders of the same hypothetical D, when n>14. An arbitrary cyclic tiling is not asserted to construct a completion. Smaller-order issues are not imported or proved here.

## 2. Tools and reductions, stated independently

**Sands (import).** In a tiling P⊕Q=Z_n, no nonzero P-difference and Q-difference have the same gcd with n. Source: Łaba–Londner, [arXiv:2106.14042v3, p. 10, Theorem 2.5](https://arxiv.org/pdf/2106.14042v3).

**Tijdeman (import).** If gcd(t,|P|)=1, then tP⊕Q=Z_n and multiplication by t is injective on P. It also holds with P and Q interchanged. Source: [the same paper, p. 3](https://arxiv.org/pdf/2106.14042v3), and its application in the Corollary 6.2 proof on p. 26, citing Tijdeman [47, Theorem 1] and Coven–Meyerowitz [2, Lemma 2.2]. We use the dilation statement only, not Corollary 6.2 or T2.

**Coset fact (elementary).** If X⊕Z=G and X lies in a subgroup H, then X⊕(Z∩(u+H))=u+H for every coset, because y=x+z in that coset implies z=y−x lies there. In particular every such coset meets Z.

Suppose |P|=3^e2^a with e≥1.

1. **330|n.** If n is odd, the A-difference 8 and Y-difference 1 have common gcd 1. If one of 3,5,11 does not divide n, the A-difference equal to that prime also has gcd 1. Each violates Sands. The witnesses are 3=3−0, 5=8−3, 11=11−0 and 1=1−0.
2. **3,5,11 divide |Q|.** If ℓ∈{3,5,11} did not divide |Q|, Tijdeman would give P⊕ℓQ, whose two divisor sets contain ℓ, from the A-difference ℓ and the scaled Y-difference ℓ(1−0). This is forbidden by Sands.
3. In particular **9|n**: 3 divides both cardinalities. Write n=2^K3^vT with K≥1, v≥e+1 and gcd(T,6)=1. Then 55|T.
4. Since gcd(T,|P|)=1, TP⊕Q tiles. TP lies in TZ_n. The coset fact shows that Q meets every residue class mod T, hence every class mod 55.

The last property concerns every hypothetical anchored tiling. It is not an assumed transversal or sampled tail set.

## 3. Two universal opposite-parity rules

Let x=q−q′ be an **odd** difference of actual elements of Q, and put g=gcd(x,n). As n is even, g is odd and g<n.

**Rule U.** If 3|x, then 9|x.

If not, 9|n implies that 3 exactly divides g. Put t=g/3. Then gcd(t,3^e2^a)=1, so tP⊕Q tiles. Its scaled A-difference t(3−0)=g has gcd g with n, matching x. This contradicts Sands.

**Rule V.** If 5|x or 11|x, then 9|x.

If 3|x, apply U. Otherwise choose ℓ∈{5,11} dividing x and set t=g/ℓ. Then t is odd and not divisible by 3, so gcd(t,|P|)=1. Use the A-difference ℓ in tP⊕Q to obtain the same forbidden gcd g. Thus 3∤x is impossible, and U finishes the rule.

In particular opposite-parity Q-elements that agree mod 3 must agree mod 9; and opposite-parity elements that agree mod 5 or mod 11 must agree mod 9. These statements hold for all e and every n in the hypotheses. Extra prime powers in n only enter the admissible odd multiplier t and do not change its coprimality with |P|.

## 4. The three-class contradiction, written without computation

**First observation.** No even element q∈Q has q≡1 (mod 3). Otherwise compare it with the three odd anchors 1,7,13. Rule U would require simultaneously

    q≡1,  q≡7,  q≡4  (mod 9),

since 13≡4 (mod 9). These residues are different.

By §2, Q contains elements x₃,x₂₅,x₄₅ in the classes 3,25,45 (mod 55). Their integer representatives and all unspecified residues are arbitrary.

1. **x₃ is odd and x₃≡5 (mod 9).** If x₃ were even, comparison with anchor 13 (same class mod 5: 3) would give x₃≡13≡4 (mod 9) by V. It would then be an even tail congruent to 1 mod 3, against the first observation. Therefore x₃ is odd. It agrees with even anchor 14 mod 11 (both are 3), so V gives x₃≡14≡5 (mod 9).
2. **x₄₅ is odd and x₄₅≡0 (mod 9).** If even, its agreement mod 11 with odd anchor 1 would give x₄₅≡1 (mod 9), again forbidden by the first observation. Thus it is odd. It agrees mod 5 with even anchor 0, so V gives x₄₅≡0 (mod 9).
3. **x₂₅ is even.** If odd, compare with even anchors 0 and 14. It agrees with 0 mod 5 and with 14 mod 11, so V would give x₂₅≡0 and x₂₅≡5 (mod 9), impossible.
4. **Final contradiction.** The even x₂₅ agrees mod 11 with the odd x₃, since 25−3=22. Rule V gives x₂₅≡5 (mod 9). It agrees mod 5 with the odd x₄₅, since 25−45=−20. Rule V instead gives x₂₅≡0 (mod 9).

This proves the Theorem. Every comparison is between opposite-parity actual elements in distinct named classes or against the actual anchors; no finite representative has been substituted for an arbitrary Q-element.

## 5. The all-orders 55·3^v·2^K caller

Suppose an anchored tiling exists at n=55·3^v·2^K, K,v≥1. As 5 and 11 occur to the first power, §2 places both in |Q|. Hence |P|=3^e2^a for some 0≤e≤v−1.

If e≥1, the Theorem excludes it. For e=0, let |P|=2^a and let T be the odd part of n. Tijdeman and the coset fact force Q to meet every class mod T. Choose q≡6 (mod 165). Every odd Q-difference x divisible by ℓ∈{3,5,11} is impossible: with g=gcd(x,n), t=g/ℓ is odd, hence coprime to |P|, and the A-difference ℓ in tP⊕Q gives a Sands collision. But if q is odd, q−0 is odd and divisible by 3; if q is even, q−1 is odd and divisible by 5. This excludes e=0 and proves the Corollary without an imported earlier power-of-two-head lemma.

## 6. Integer-only finite check and exact boundary

Checker: `frontier-20261029-all-powers-three-head-obstruction-check-v1.py`, SHA256 `fb3b83446fd36051351ba6285af40a6a2c78afbe35026ba3ec0fda9d56fcbbdd`, 75 LF / 2,717 bytes. The owner executed exactly these bytes in a fresh namespace of the retained eval kernel before writing this packet. The actual output was `"result": "PASS"`. Only Python integers, `math.gcd` and finite loops are used; no prior checker output is read.

**WRITTEN-checked-in-kernel, listed finite scope only:**

- 980,100 ordered pairs of residue types mod 990 are checked. The coordinate form of U,V agrees with the odd-gcd exclusion {3,5,11,15,33,55,165} at modulus 990; same-parity pairs are left unrestricted by this relaxation.
- All 990 types are filtered against Y. No even type congruent to 1 mod 3 survives.
- The exact (parity, mod 9) domains of the three named classes are:
  - class 3 mod 55: {(1,5)};
  - class 25 mod 55: {(0,0),(0,2),(0,3),(0,5),(0,6),(0,8)};
  - class 45 mod 55: {(1,0)}.
- Exhaustive comparison of those literal domains gives zero compatible triples. The final differences 22 and −20 and the contradictory mod-9 residues are asserted separately.
- 25,600 bounded generic controls verify the actual admissible multiplier and gcd collision for e=1,…,4, K=1,…,4, v=e+1 or e+2, T∈{55,275,605,715}, and the relevant odd differences below 990.

Why a fixed projection suffices: n is divisible by 990 under the contradictory hypothesis. The two rules use only parity, congruences mod 3 and 9, and mod 5 and 11. Each therefore factors through residues mod 990 for every e and every remaining factor of n. The all-n step is proved in §§2–4, not inferred from a finite exponent scan. The exact finite check is a control on that projection and the literal certificate, not a formal or independent-model proof of the theorem.

## 7. Limits and review obligations

Still unexcluded by this packet: odd head part 5^e or11^e with e≥2; a shared odd head prime outside {3,5,11}; or at least two distinct odd head primes. The original unrestricted Shor completion/noncompletion problem remains OPEN. No residual is declared feasible, no previous result is adopted, and no scientific ledger or frozen source has been edited.

Review must check the all-n scalar dilations and their coprimality, the universal coverage of classes mod 55, Rules U,V without an illicit same-parity use, the four steps of the three-class proof, the power-of-two-head caller in §5, the actual-code border import, and every provenance/process/non-premise qualification. This is a separate candidate with its own scope; no earlier review verdict is inherited.

**END OF ALL-POWERS-OF-THREE HEAD OBSTRUCTION.**
