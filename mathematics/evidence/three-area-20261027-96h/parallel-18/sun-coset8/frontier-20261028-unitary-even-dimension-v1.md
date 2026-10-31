# Sun8 for every even-dimensional unitary group over a nonprime field

**NEW FAMILY CANDIDATE at NAMED EXTERNAL INPUTS — WRITTEN plus bounded exact arithmetic; not reviewed/adopted/formally verified/novelty-cleared.** Actual native prewrite clock **Wed Oct 28 18:03:24 PDT 2026**. This concerns actual cosets and subgroup indices in finite simple groups, not merely compatible tuples or a group-order cutoff. It is separate from the odd-prime-power-dimensional result and needs its own complete source/exception review.

## 1. Exact scope

For a group X, `Sun_8(X)` means every eight pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups have a pair of subgroup indices with gcd>=8.

**Theorem.** Let n>=4 be ANY EVEN integer and let q=p^f for a prime p. At the EXACT named unitary/Sylow and primitive-prime statements in Section2, `Sun_8(PSU_n(q))` holds in each of these ranges:

1. Every nonprime field: f>=2, all even n>=4 and all p.
2. Prime fields when `2n−1` is composite: f=1, all even n>=4 and all p.
3. Other prime fields, excluding `(n,q)=(6,2)`, when there exists a primitive prime r of `p^(2n−2)−1` with `r>7` and either `r != 2n−1` or `r² | (p^(n−1)+1)`.
4. The separate small groups `(n,q)=(4,2),(4,3)`, proved by an elementary support argument in Section6, without invoking a small-case maximal-subgroup computation.

The ranges overlap. For f=1 not meeting these conditions we do NOT claim closure; in particular `(6,2)` is not automatically settled. No result is asserted for odd dimensions by this packet. No Sun7, NC7, P7, normal-extension or covering hypothesis is imported.

## 2. Exact named external statements

- **Finite unitary order and simplicity.** [MathWorld, Projective Special Unitary Group](https://mathworld.wolfram.com/ProjectiveSpecialUnitaryGroup.html) states

      |PSU_n(q)| = q^(n(n−1)/2) product_(j=2)^n(q^j−(−1)^j) / gcd(n,q+1),

  and that PSU_n(q) is nonabelian simple for n>=2 except PSU2(2), PSU2(3), PSU3(2). This is the precise standard statement used, not an independently audited proof source.
- **Unique maximal Sylow overgroup.** [Baumeister–Burness–Guralnick–Tong-Viet, arXiv:2307.13976v2](https://arxiv.org/html/2307.13976v2), Theorem2/Table B, U_n(q) with even n>=4 and r a primitive prime divisor of `q^(2n−2)−1`, states that `beta(n−1,−1)` and either f>1, or f=1 with one of `|R|>r`, `r != 2n−1`, or the displayed quadratic-residue alternative, give a unique maximal overgroup of a Sylow r-subgroup R of type `GU_(n−1)(q)×GU_1(q)`. We use only f>1, r!=2n−1, or |R|>r, not the quadratic alternative. Source Proposition6.4 separately handles `U4(2),U4(3),U5(2),U6(2)` using Magma. We do NOT silently apply the generic row to these exceptions; the nonprime-field range avoids them, and Section6 treats the two U4 endpoints without their Magma result.
- **Exact beta condition.** The source's Remark9.2 defines beta(m,−1) by `(q^(1/k))^m != −1 (mod r)` for every ODD prime k|f with k!=r. Every such k is explicitly handled below.
- **Zsigmondy.** The source §2.1 states the primitive-prime theorem with exceptions `(base,exponent)=(2,6)` and exponent2 with Mersenne base. It is applied only where those exceptions are absent.

These are statement-level imports: **NR-UNITARY-ORDER/SIMPLICITY-PROOFS, NR-UNIQUE-SYLOW-CLASSIFICATION-PROOF, NR-ZSIGMONDY-PROOF** remain. No unexamined full group catalogue or source proof is represented as newly reconstructed.

## 3. Actual Sylow-overgroup-to-coset caller

If G is a finite nonabelian simple group, r>7 divides |G| and a Sylow r-subgroup has a UNIQUE maximal proper overgroup M, then G satisfies Sun8.

If eight actual disjoint cosets had pairwise index gcd<=7, at most one subgroup index could be divisible by r; at least seven actual subgroups have r-free index and hence contain a Sylow r-subgroup of G. By Sylow conjugacy and uniqueness, each lies in a conjugate of M. Their original indices are all divisible by d=[G:M]. Since G is simple, its action on G/M is faithful. If d<=7 then |G| divides d!, impossible because r>7 divides |G|. Hence d>=8 and two original indices share a divisor>=8, contradiction. □

The maximal conjugates need NOT coincide; the common divisor d is what is used. The argument applies to the ACTUAL subgroup indices and does not assume a covering or arbitrary projection of disjoint cosets.

## 4. Every nonprime field, all even dimensions

Let n>=4 be even, q=p^f, f>=2. Zsigmondy gives a prime r with

    ord_r(p)=2(n−1)f.

The only possible `(p,exponent)=(2,6)` exception would require `(n−1)f=3`, impossible for n>=4 and f>=2; the exponent2 exception is also impossible. Therefore

    r ≡ 1 (mod 2(n−1)f),
    r >= 2(n−1)f+1 >= 4(n−1)+1 > 7.

Also `ord_r(q)=2(n−1)`, so `q^(n−1)≡−1 (mod r)`. Because n−1 is odd, `q^(n−1)+1` is the j=n−1 factor of the named unitary-order product. The center denominator gcd(n,q+1)<=n is strictly smaller than r, so r divides |PSU_n(q)|.

For ANY odd prime k dividing f,

    (q^(1/k))^(n−1)=p^((n−1)f/k) != −1 (mod r),

since a −1 congruence would imply `p^(2(n−1)f/k)=1` at an exponent smaller than ord_r(p). Thus beta(n−1,−1) holds at all required k. The source's f>1 branch applies. Since q>=4, none of its separately handled small exceptions U4(2),U4(3),U5(2),U6(2) occurs. The chosen Sylow r-subgroup has a unique maximal overgroup, and the group is nonabelian simple. Section3 proves Sun8.

This covers every even n>=4, not just n−1 prime or a prime power, and every f>=2; no finite-parameter trial is used in the proof.

## 5. Explicit prime-field ranges

Let f=1. When `(p,2n−2) != (2,6)`, Zsigmondy supplies a primitive r with `ord_r(p)=2(n−1)`, so `r≡1 (mod 2n−2)` and r>=2n−1. The beta condition is vacuous.

- If `2n−1` is composite, n>=6 and the exception `(2,6)` cannot arise. A prime r cannot equal composite 2n−1, so r>2n−1>7. The source's `r != 2n−1` alternative gives uniqueness. The source-exception `(6,2)` is absent because 2*6−1=11 is prime.
- If a primitive r>7 is explicitly available and `r != 2n−1`, use the same source alternative, provided `(n,q)` is not one of the source's separate small exceptions.
- If such a primitive r satisfies `r² | p^(n−1)+1`, then the named unitary order product contains r² in its j=n−1 factor, while its center denominator is <=n<r. Thus the actual Sylow r-subgroup has order >r, satisfying the source's other alternative. Again the source's separate small exceptions must not be silently replaced by the generic row.

The statement in Section1 excludes `(6,2)` from range3; `(4,2),(4,3)` are instead paid below. `(5,2)` is odd-dimensional and never enters this even-n theorem. For any other prime field not satisfying the displayed sufficient conditions, including a case where the only primitive prime is r=2n−1 with Sylow order r, NO result is inferred here.

## 6. PSU4(2) and PSU4(3), without the small-group maximal list

The named order formula gives

    |PSU4(2)| = 25920 = 2^6 3^4 5,
    |PSU4(3)| = 3265920 = 2^7 3^6 5 7.

Both are nonabelian simple and have order >7!=5040. A subgroup of index2,...,7 would give a faithful embedding into S7, contradicting their orders; thus all proper indices are at least8.

We now use the following fully written arithmetic lemma, also reconstructed in `frontier-20261028-psu3-all-fields-v1.md` (SHA256 `c32a27c4e2c71cf76e3b129d37513dba9680da34cf4186a35d1d70126b7b8e7b`): among pairwise-disjoint cosets with pairwise index gcd<=7, at most FOUR indices >=8 whose prime supports lie inside {2,3,5} can occur. Briefly, actual disjointness forces each pair to have gcd>=2; if a singleton prime support occurs, all others must contain that prime, and the possible prime-power/mixed categories have capacities at most4. With no singleton support, {2,3} contributes at most2 because each such index>=8 is divisible by12 or18; {2,5},{3,5} contribute at most1 each and cannot both coexist with a {2,3,5} index. Thus the maximum remains4. The cited earlier packet gives every singleton and mixed subcase, not a numerical-divisor guess.

For PSU4(2) all subgroup indices have supports inside {2,3,5}; eight would violate the at-most-four lemma. For PSU4(3), at most THREE indices can be divisible by7: its 7-adic valuation is1, there is no index7, and after dividing each seven-index by7 the pairwise-coprime factors must each own a distinct prime among2,3,5. The remaining seven-free indices have supports inside {2,3,5} and number at most4. Thus there are at most7 cosets in a hypothetical eight-counterconfiguration. This proves both endpoints with no Sun7 or external maximal-list application.

## 7. Independent bounded arithmetic controls

- `frontier-20261028-unitary-even-dimension-check.py`, SHA256 `57040c337148826bc0eb9768962b0a3715514cf9920ddd9ffa15b67ecd57eb1d`, used exact primality/order, unitary-product divisibility and beta checks for n=4,6,8,10, p=2,3, f=2,3. The bounded run found and checked primitive primes for **16/16** inputs, ending at actual **Wed Oct28 18:02:41 PDT2026**. No sample proves Zsigmondy or the classification row for arbitrary n/q.
- `frontier-20261028-u4-small-order-check.py`, SHA256 `406d8cdf6bef87da5580f8f1227844328f4299c97518dd765c86de5b628ccbac`, returned exact source-formula orders `25920` and `3265920`, matching the two displayed prime-factor products, and PASS at **Wed Oct28 18:03:12 PDT2026**. It did not prove group simplicity or the general at-most-four support lemma.

Both checks used standard-library integers only. No actual subgroup/coset graph was enumerated for arbitrary unitary groups; the universal proof rests on the stated classification and arithmetic, not these controls.

## 8. Prior scope and open obligations

The old adopted math-6 summary covered all-field SL/PSL and symplectic families; later unitary leads have separate historic unreviewed/held states. This is a fresh source-dependent EVEN-dimensional unitary proof candidate, not a claim that those old leads were accepted or clean. Targeted prior-parent searching did not establish an adopted all-even-unitary gate, but it is not an exhaustive priority/novelty review. The earlier rediscovery correction remains mandatory.

No original arbitrary-group Sun8 or all-simple-family classification is claimed. Remaining even prime-field cases (including any unlisted small exception), odd dimensions not covered by the separate odd-prime-power theorem, original proofs of all named imports, human/kernel/independent-family review and publication/priority remain open. Main and a disjoint reviewer must verify the source row, beta, small exceptions, exact coset caller and entire support lemma before adoption.
