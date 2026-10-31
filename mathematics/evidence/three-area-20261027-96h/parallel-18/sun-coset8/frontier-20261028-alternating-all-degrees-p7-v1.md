# Direct P7 for every finite simple alternating group: conditional written candidate

**Status: WRITTEN candidate conditional on the explicitly named public theorems below, with finite exact controls; not independently reviewed, formally verified, accepted, published, or priority-cleared.** For every n≥5, the finite simple group A_n has no seven proper subgroup indices whose pairwise gcds are all exactly 7; in particular it excludes the eight-index direct-P7 configuration. More strongly, for every n≥14 there are no **four** proper subgroup indices with all pairwise gcds at most 7. Hence Sun8 follows for A_n, n≥14, directly at this same source-conditional scope. For n≤13 the direct-P7 exclusion is an elementary prime-support bound; the optional Sun8 conclusion there requires the separately named Sun7/R8 interfaces in Section 7.

The requested still-stronger all-degree statement 'no three proper-subgroup indices have pairwise gcd≤7' is **false**: Section 8 gives actual A5 subgroups of indices 5,6,15,20 whose pairwise gcds are all ≤7. These are not claimed to be disjoint cosets or a Sun counterexample. No global all-finite-simple-group, published-priority or historical-novelty claim is made.

## 1. Exact named imports and mandatory pre-source order

1. **Bertrand:** for integer m>1, a prime r satisfies m<r<2m; see https://academicweb.nd.edu/~dgalvin1/pdf/bertrand.pdf.
2. **Jordan:** Theorem 1.1 of https://arxiv.org/html/1209.5169v1: a primitive finite permutation group containing a prime cycle fixing at least three points contains A_n.
3. **Two-fixed-point classification:** Jones Theorem 1.2, case k=2, same versioned source: a primitive degree-n group not containing A_n but containing a cycle fixing exactly two points satisfies PGL2(q)≤H≤PΓL2(q), n=q+1 for a prime power q. The source states its proof uses CFSG. We import the statement, not a source proof replay or formal verification.
4. **Even half-prime case:** Theorem 2(i)(b) of https://arxiv.org/html/2307.13976v2: for odd prime r, a Sylow r-subgroup of A_(2r) has exactly one maximal overgroup (S_r wr S_2)∩A_(2r). We use it only for r>7. The classification source is not independently reconstructed.
5. Standard Sylow, orbit-stabilizer, alternating-group order/simplicity, projective semilinear group order and elementary binomial arithmetic. No numerical prime-gap theorem is needed.

Read `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json`, SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, **before** any earlier alternating source body cited for context. This prospective argument does not retroactively import Jordan/Jones/Bertrand into f116, held history, the earlier integer-relaxation packet or any prior verdict. The writer was nonblind; the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no such excerpt is used and no historical hold changes.

## 2. A reusable binomial pair lemma

For 3≤i<j<n/2, let A=C(n,i), B=C(n,j), g=gcd(A,B). The identity
\[\binom ni\binom{n-i}{j-i}=\binom nj\binom ji\]
gives A/g|C(j,i), because A/g and B/g are coprime. But
\[\frac{\binom ni}{\binom ji}=\prod_{h=0}^{i-1}\frac{n-h}{j-h}
 \ge\left(\frac nj\right)^i>2^i\ge8.\]
Thus g≤7 would imply A/g≥A/7>C(j,i), impossible. For repeated i≥3 the common binomial C(n,i) is itself >7. Therefore any pairwise-gcd≤7 collection contains at most one index divisible by a factor C(n,u) with u≥3, u<n/2.

## 3. A large prime cycle and intransitivity

For a prime r with n/2<r≤n−2, an r-free-index H<A_n contains an actual r-cycle R fixing t=n−r≥2 points. If H is transitive, it is primitive: a nontrivial block system has fewer than r blocks, so R fixes each block and its r moved points lie in one, forcing n≥2r. When t≥3, Jordan then forces H=A_n, contradiction. Hence every r-free proper H is intransitive.

For an intransitive H, its orbit U containing the r moved points has complement size 1≤u≤t<n/2, and C(n,u) divides [A_n:H] because the alternating set stabilizer has that index. Among indices with pairwise gcd≤7, there is at most one r-divisible index. Among r-free indices, at most one has u≥3 by Section 2; at most one can use either u=1 or u=2 when n≥15 because gcd(n,C(n,2)) is n if n is odd and n/2 if n is even, both >7. Thus there are at most **three** such subgroup indices in total for n≥15 in the t≥3 case. At n=14 the three possible binomials are 14,91,364; the last has gcd >7 with each of the first two, so at most two r-free labels and the same total bound 3 holds.

## 4. Obtaining r for every n≥14

For n=14,15,16, use the explicit prime r=11, with t=3,4,5 respectively; Section 3 applies.

For odd n≥17 write n=2m+1 with m≥8. Bertrand supplies m<r<2m=n−1, so r>n/2, r>7 and t is even at least 2. If t≥3, Section 3 applies. The t=2 case is treated in Section 5.

For even n≥18 write n=2m. If m is composite, Bertrand applied to m−1 gives m−1<r<2m−2=n−2. Since m is composite, r>m=n/2; hence t≥3 and Section 3 applies. If m is prime, m≥11, use r=m and the source Theorem 2(i)(b): every r-free H lies in a conjugate of the same maximal Sylow-r overgroup M. Two r-free indices are divisible by [A_n:M]≥n>7, and at most one index can be r-divisible. So in this even half-prime case there are at most two subgroup indices with pairwise gcd≤7.

## 5. The odd t=2 exception

Suppose n odd, r=n−2>7 is prime, and the r-cycle has exactly two fixed points. Intransitive r-free subgroup indices are divisible by C(n,1)=n or C(n,2)=n(n−1)/2, both multiples of n>7; at most one such index can occur in a pairwise-gcd≤7 collection.

A transitive r-free H is primitive by Section 3. If it is proper, the named Jones k=2 theorem gives q=n−1=r+1 a prime power and PGL2(q)≤H≤PΓL2(q). q is even, so q=2^e. Since r=2^e−1 is prime, e is prime; r>7 forces e odd and e≥5. The quotient PΓL2(q)/PGL2(q) is cyclic of order e, so H has one of only two possible orders q(q²−1)d, d∈{1,e}. If either order is not realized inside A_n, treating it as possible only overcounts.

For either order the subgroup index is I=(q−2)!/(2d). We show n=q+1 divides I. Since e is odd, q+1 is divisible by 3. Put a=(q+1)/3. For e≥5, a>e (e.g. 2^e+1>3e by induction) and a≤q−2. Thus the distinct integers 2,3,e,a occur among the factors of (q−2)!, and their product is 2e(q+1). As d divides e, n divides (q−2)!/(2d). Hence **all** transitive r-free indices also share n>7 with all intransitive r-free indices. There is at most one r-free index and at most one r-divisible index in this t=2 case.

Combining Sections 3–5, for every n≥14 any four proper subgroup indices contain a pair with gcd>7. A family of eight disjoint cosets necessarily uses proper subgroups, so it satisfies Sun8 at this source-conditional scope.

## 6. The small direct-P7 table

An index divides |A_n|. If seven indices have every pairwise gcd 7, they are 7a_i with pairwise-coprime a_i; at most one a_i is 1. For n≤13, 7 occurs in n!/2 at most once, so no a_i contains 7. Each remaining a_i needs a distinct prime from the indicated set:

| Degree n | Non-7 prime divisors of A_n | Maximum possible number of gcd-7 indices |
|---|---|---:|
| 5,6 | 2,3,5; in fact 7 does not divide the group order | 0 |
| 7,8,9,10 | 2,3,5 | 4 |
| 11,12 | 2,3,5,11 | 5 |
| 13 | 2,3,5,11,13 | 6 |

These are arithmetic upper bounds, not claims that the maxima are achieved. They exclude seven gcd-7 indices for n=5,…,13, completing the direct-P7 alternating family in combination with n≥14. They do not, by themselves, rule out every possible Sun8 counterconfiguration with gcds other than 7.

## 7. Exact Sun8 versus direct-P7 boundary

For n≥14, Sun8 follows directly from the stronger subgroup-index result. For n=5,…,13, Sun8 follows **if** the separately named old written Sun7 parent verdict SHA `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2` and prior R8 source SHA `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6`, with their mandatory overlays, are admitted. R8 makes every hypothetical Sun8 counterconfiguration have pairwise index gcd exactly 7, contrary to the small table. This is conditional on prior same-harness written interfaces, not a new Sun7 proof or human/formal certification.

## 8. The stronger three-index preference is false

In A5, H1=A4 (the point stabilizer), H2=⟨(1 2 3 4 5),(2 5)(3 4)⟩≅D10, H3=⟨(1 2)(3 4),(1 3)(2 4)⟩≅V4, and H4=⟨(1 2 3)⟩≅C3 have orders 12,10,4,3 and indices 5,6,15,20. Their six pairwise gcds are 1,5,5,3,2,5. This explicitly disproves an all-n no-three/no-four **subgroup-index** claim with threshold 7. In particular the coprime pair cannot be disjoint cosets; no Sun counterexample is asserted.

## 9. Actual finite checks and review obligations

`frontier-20261028-alternating-family-check.py`, SHA `ca2212f54af6088dcd0be7a0860a2381efddee04b89001a32ff173a6691f477c`, 40 LF / 1185 bytes, ran at 20:20:14 PDT on 2026-10-28. It checked 304,178 finite binomial pairs, the n=14,15,16 cycle choices, the small prime-support bounds and two source-allowed semilinear-order examples. `frontier-20261028-a5-subgroup-check.py`, SHA `ee55652225ff44de4b970b1828e84920088fee2645d1535799be3a4b172cd936`, 54 LF / 1693 bytes, ran at 20:23:38 PDT: it generated the four listed groups as even permutations, checked their orders and index gcds, and confirmed an identity-generator mutation reduces the D10 order to 5. These are the author's finite checks, not independent replays, source classification proofs, external-model/human review or formal verification.

**Priority review:** independently attack the binomial identity/divisibility direction, all Bertrand endpoints, the actual r-cycle block argument, Theorem 2(i)(b) scope, the Jones k=2 order alternatives and the factorial proof that n divides every transitive index; check the n14 and small-prime tables and A5 construction separately. The public source proof DAG and any old S7/R8 overlays remain independent inputs. No all-simple-groups/global Sun8 verdict, priority or historical-hold modification is claimed.
