# Sun8 for PSU(3,q) over every finite field q>=3, at named Sylow-overgroup and primitive-prime imports

**NEW FAMILY PROOF CANDIDATE, not yet reviewed/adopted/formally verified or novelty-cleared.** Actual native prewrite clock **Wed Oct 28 17:55:56 PDT 2026**. The statement covers ALL actual finite-index left cosets of ALL subgroups of each named finite simple group. It does not use Sun7, NC7 or any P7/simple-factor reduction. Two small-field endpoints are treated by a complete written index-support argument, not by assuming the executable test proves an unbounded theorem.

## 1. Claim and named external inputs

**Theorem.** For EVERY prime power q>=3, the finite simple group `G=PSU(3,q)` satisfies Sun8: for every eight pairwise-disjoint ACTUAL LEFT cosets of subgroups of G, some pair of subgroup indices has gcd at least8.

The result is conditional on the EXACT named group-theory inputs below. I read their stated source interfaces, not the complete original classification or theorem proofs:

1. **Unitary group order and simplicity.** For q>=3, `PSU(3,q)` is simple and has order

       |G| = q³(q³+1)(q²−1)/gcd(3,q+1).

   This exact statement appears in [G. Korchmáros et al., arXiv:1902.10201v1](https://arxiv.org/html/1902.10201v1), §3, reader line410. **NR-UNITARY-ORDER/SIMPLICITY-PROOFS:** the source statements, not their full proofs/ancestry, are used.
2. **Unique maximal Sylow overgroups for U3.** [Baumeister–Burness–Guralnick–Tong-Viet, *On the maximal overgroups of Sylow subgroups of finite groups*, arXiv:2307.13976v2](https://arxiv.org/html/2307.13976v2), Theorem2 and Table B, at G=T=U3(q), gives:
   - for defining characteristic r=p odd, a fixed Sylow p-subgroup has a UNIQUE maximal overgroup P1;
   - for an odd primitive prime r of q^6−1 satisfying beta(3,−1), a Sylow r-subgroup has a UNIQUE maximal overgroup of type GU1(q³), provided f>1 or r>7 (the source also lists |R|>r as another alternative, not needed here).

   Its Remark9.2 defines beta(3,−1) as `(q^(1/k))³ != −1 (mod r)` for every ODD prime k dividing f other than r. I read Theorem2, Table B, this definition and the relevant U3 discussion, but did not independently reprove the classification: **NR-UNIQUE-SYLOW-OVERGROUP-PROOF** remains. Only these two exact theorem rows are imported, not an unrestricted use of all rows or an unspecified classification database.
3. **Zsigmondy's primitive-prime statement.** For a prime power a and d>=2, a prime divisor of a^d−1 not dividing any a^j−1 for 1<=j<d exists except the standard `(a,d)=(2,6)` and d=2 Mersenne cases. This exact statement is also printed in §2.1 of [arXiv:2307.13976v2](https://arxiv.org/html/2307.13976v2). It is used only with `a=p`, `d=6f>=12` and f>=2, so neither exception applies. **NR-ZSIGMONDY-PROOF:** its original proof is not reproduced or authenticated here.

Simplicity and exact subgroup-structure claims are named imports, not inferred from numerical tests. q=2 is excluded because PSU(3,2) is not simple and is outside the stated theorem. The two q=3,5 cases are nevertheless fully included, separately, below.

## 2. Unique-Sylow-overgroup criterion, with NO Sun7 premise for r>7

**Lemma.** Let G be any finite group and r>7 a prime dividing |G|. Suppose a Sylow r-subgroup R has a UNIQUE maximal subgroup M among the proper subgroups containing R, and let d=[G:M]>=8. Then Sun8(G) holds.

**Proof.** Suppose eight actual pairwise-disjoint left cosets have subgroup indices n_i with all pair gcds<=7. At most ONE index is divisible by r: any two would have gcd at least r>7. Thus at least SEVEN actual subgroups have r-free index. If r∤[G:H], H contains a Sylow r-subgroup of G. All Sylow r-subgroups of G are conjugate; after conjugating H, its Sylow subgroup is R, and a maximal proper overgroup of the conjugate contains R, hence must be M. Therefore the original H is contained in a conjugate of M and d divides its actual original index. In particular, two of the seven r-free indices share divisor d>=8, contradiction. □

Nothing here assumes all the H share the SAME conjugate maximal subgroup. The conclusion comes from their common NUMERICAL divisor d, paid by exact subgroup-index chains. No Sun7, P7 or normal-subgroup hypothesis is used.

## 3. Universal lower bound on proper subgroup indices

The source in Section1 states PSU(3,q) is simple for q>=3. Every proper subgroup H has trivial core, so its transitive action on G/H embeds G into S_d, d=[G:H]. We show |G|>7!=5040 and hence d>=8.

At q=3 the formula gives |G|=6048>5040. For q>=4, `gcd(3,q+1)<=3`, so

    |G| >= 4³(4³+1)(4²−1)/3 = 20800 > 5040.

Thus for EVERY q>=3, EVERY proper maximal subgroup M has `[G:M]>=8`. An index-one subgroup cannot appear in a disjoint family of size>=2. The simple-action argument proves the needed lower bound; it does not import a minimum-index catalogue.

## 4. Every extension degree f>=2: a primitive Sylow prime

Write q=p^f with p prime and f>=2. By Zsigmondy at a=p, d=6f, choose a prime r with

    ord_r(p)=6f.

The exceptional `(2,6)` does not apply because f>=2. Since the multiplicative order divides r−1, `r≡1 (mod 6f)` and r>=13>7. Also `ord_r(q)=6`, so q³≡−1 (mod r); hence r divides q³+1 and divides the unitary group order (the possible denominator gcd(3,q+1) is at most3).

We verify the SOURCE'S beta condition, including ALL odd-prime subfield divisors. If k is any odd prime divisor of f, then

    (q^(1/k))³ = p^(3f/k) is NOT ≡ −1 (mod r),

because otherwise squaring would give `p^(6f/k)≡1 (mod r)`, contradicting `ord_r(p)=6f`. This proves beta(3,−1), even for any k excluded by the source condition. The source's f>1 alternative holds. Hence a Sylow r-subgroup of G has the UNIQUE maximal overgroup M in the named Table B row. Section3 gives `[G:M]>=8`. Section2 applies and proves Sun8(G), with NO Sun7 or group-specific computation.

This handles every characteristic p, including p=7, and ALL extension degrees f>=2. No selected-field search is used to infer primitive primes or beta for the full range.

## 5. Prime fields: all p>=7

If f=1 and p>=11, choose r=p. The source's defining-characteristic U3 row supplies the UNIQUE maximal overgroup P1 of a Sylow p-subgroup; p>7 and `[G:P1]>=8` by Section3. Apply Section2.

If f=1 and p=7, choose r=43. Directly `7³+1=344=8*43` and `7³≡−1 (mod 43)`, while `7` and `7²` are not1 mod43. Hence `ord_43(7)=6`. The beta subfield condition is vacuous since f=1, and the source's `r>7` alternative is satisfied. The same unique-overgroup lemma gives Sun8(PSU(3,7)).

Thus only prime fields q=3 and q=5 remain. The proof here does not need Zsigmondy at f=1.

## 6. An elementary small-prime-spectrum lemma for q=3,5

The group-order statement gives

    |PSU(3,3)|=6048=2^5 3^3 7,
    |PSU(3,5)|=126000=2^4 3^2 5^3 7.

We prove a more general finite-index statement, using no Sun7:

**Lemma.** Let a finite group G have prime divisors contained in {2,3,5,7}, with 7-adic valuation at most1, and no proper subgroup of index2 through7. Then Sun8(G).

**Proof.** Suppose eight disjoint cosets form a counterconfiguration. Their indices are divisors of |G|, all >=8, and each pair has gcd between2 and7: the lower bound is the ordinary coprime-coset fact, proved in Section7. Split the labels into seven-divisible and seven-free.

For the seven-divisible labels write `n_i=7r_i`. Since gcd(n_i,n_j)<=7, their r_i are pairwise coprime. Their r_i>1 because index7 is absent; the 7-adic valuation assumption makes every r_i seven-free. Each r_i therefore has at least one prime from {2,3,5}, different across labels. There are at most THREE seven-divisible labels.

We claim there are at most FOUR seven-free labels. Their indices use only2,3,5, are >=8, and have pairwise gcd in [2,7]. Classify by the set of prime divisors.

- If a singleton support {2} occurs, every other index is even. There is at most one pure 2-power (two >=8 would share divisor8); among indices supported exactly on {2,3}, at most two, because each >=8 is divisible by12 or18 and two bearing the same one would share that divisor; and at most one index divisible by both2 and5, since two would share10. Thus at most4.
- If singleton {3} occurs, every other index is divisible3. There is at most one pure 3-power (each is >=9), at most two supported exactly on {2,3} as above, and at most one divisible by both3 and5 (otherwise gcd>=15). Thus at most4.
- If singleton {5} occurs, every other index is divisible5. At most one is a pure 5-power (each is >=25); at most one is even and at most one is divisible by3, otherwise a pair shares10 or15. Thus at most3.
- If no singleton occurs, the only supports are {2,3}, {2,5}, {3,5}, {2,3,5}. The first contributes at most two by the 12/18 argument. Each of the next two contributes at most one, because duplicates share10 or15. A {2,3,5} index cannot coexist with either {2,5} or {3,5}, and at most one such triple support exists. Thus the 5-containing supports contribute at most two, and the total is at most4.

Therefore the entire eight-label configuration would have at most3+4=7 labels, contradiction. □

The numerical orders of PSU(3,3) and PSU(3,5), together with Section3's simplicity/index argument, satisfy this lemma. This completes BOTH prime-field endpoints and hence the entire family.

## 7. Coprime-index coset fact and logical boundaries

For completeness, disjoint actual cosets must have noncoprime subgroup indices. If indices a,b are coprime, the diagonal map `G/(H∩K)->G/H × G/K` is injective; its domain index is divisible by ab and at most ab, so the map is onto. The given actual cosets therefore meet. This holds for nonnormal subgroups and is the ONLY intersection fact needed in Section6.

The proof did not rely on a graph search, on all eight indices being seven-divisible, or on Sun7(G). In particular, q=3,5 are decided by the written all-divisor support lemma, while f>=2 and p>=7 are decided by the unique-Sylow-overgroup criterion. The cited 2024 classification, unitary order/simplicity, and Zsigmondy are genuine NAMED imports, not proved by this paper. Their scope, exceptions and beta condition are explicit. A false/nonadmitted unique-overgroup statement or missing primitive prime would leave the corresponding field cases unproved.

## 8. Actual bounded checks and one honest initial failure

All code uses standard-library exact integers; these checks are supportive and do NOT establish the all-q imports or replace the written Section6 argument.

1. `frontier-20261028-unitary-small-divisor-check.py`, SHA256 `b98a495969d41147a8dd558df241a3277d2d6abb07fe80c9c122c2810dc19a68`, enumerated ALL divisors>=8 of the two source group orders and searched the exact compatibility graph (indices adjacent iff gcd in[2,7]). Actual run, Wed Oct28 17:54:02 PDT 2026:

   ```text
   q=3, group_order=6048, candidate_divisors=42, max_compatibility_clique=4, search_nodes=5
   one_max_clique: [12, 21, 54, 224]
   q=5, group_order=126000, candidate_divisors=113, max_compatibility_clique=5, search_nodes=39
   one_max_clique: [18, 20, 42, 48, 375]
   PASS: neither divisor graph admits eight indices
   ```

   This is an overapproximation: these are numerical divisors, not claimed actual subgroup indices or coset witnesses. It does not prove the simple-group order or the general family.

2. The first bounded prime-search source `frontier-20261028-unitary-primitive-prime-check.py`, SHA256 `37a33f7f69b39396217bde04474c960f43b7b453faafcbd1b320cc5722b4a00e`, found f=1..4 but exited with `RuntimeError: no bounded witness f=5 cap=1000000`. That was a SEARCH-CAP failure, not a counterexample to Zsigmondy, beta or the theorem. Its bytes and actual failure are retained.
3. The new successor `frontier-20261028-unitary-primitive-prime-check-v2.py`, SHA256 `7785ff395566f9ef24920f0782f44ea130aa4136181f47f50f0f9a95f0b733b7`, treated missing bounded primes as UNKNOWN, searched up to10,000,000 and actually returned:

   ```text
   f=1, primitive_prime=43, ord_7=6, beta=PASS, r_divides_unitary_order=YES, order_gt_7_factorial=YES
   f=2, primitive_prime=13, ord_7=12, beta=PASS, r_divides_unitary_order=YES, order_gt_7_factorial=YES
   f=3, primitive_prime=117307, ord_7=18, beta=PASS, r_divides_unitary_order=YES, order_gt_7_factorial=YES
   f=4, primitive_prime=73, ord_7=24, beta=PASS, r_divides_unitary_order=YES, order_gt_7_factorial=YES
   f=5, primitive_prime=6568801, ord_7=30, beta=PASS, r_divides_unitary_order=YES, order_gt_7_factorial=YES
   f=6: UNKNOWN, no witness searched up to 10000000
   FINISHED: verified=5/6; cap misses are UNKNOWN
   Wed Oct 28 17:51:58 PDT 2026
   ```

4. A separate direct `Phi_36(7)` check `frontier-20261028-unitary-f6-direct-prime-check.py`, SHA256 `45bb7c81873d45de094856c8bcf11bd7ff8019e778e51d47e8128dd35922446e`, used exhaustive trial division to sqrt(n) and modular exponentiation; actual output:

   ```text
   Phi36_at_7: 13841169553
   trial_division_primality: PASS
   ord_7: 36
   f6_beta_condition: PASS
   Wed Oct 28 17:52:15 PDT 2026
   ```

   This resolves that ONE bounded f=6 search control, not Zsigmondy for arbitrary f. The reported initial failure and v2 UNKNOWN remain true historical run outcomes, not rewritten passes.

## 9. Prior scope and remaining gates

The older round summary names all SL/PSL and symplectic families as written-supported; later unitary candidates were not adopted by that broad summary and have separate individual statuses. A targeted search of prior parent dispositions did not reveal an adopted all-q PSU3 family gate; it is not an exhaustive repository/publication priority search. This is a prospective ALL-FIELDS UNITARY FAMILY candidate at the precisely named imports, not an assertion that old held unitary proofs were used or validated. No novelty/firstness claim is made.

The result, if reviewed, excludes this one infinite family and DOES NOT settle unrestricted Sun8, other unitary dimensions, all simple groups, large Ree or a complete simple-group classification. Parent and a disjoint reviewer must reconstruct the source theorem's U3 rows, beta condition, Zsigmondy exceptions, all-field arithmetic, small q argument and actual subgroup-to-coset caller. Human/kernel/independent-family verification, original classification proofs, priority and publication remain unpaid.
