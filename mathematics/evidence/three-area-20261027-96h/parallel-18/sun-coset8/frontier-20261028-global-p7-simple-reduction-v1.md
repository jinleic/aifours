# From Sun7 to global seven-saturation and a finite-simple Sun8 reduction

**NEW WRITTEN CANDIDATE, not reviewed/adopted/formally verified/novelty-cleared.** Actual native prewrite clock **Wed Oct 28 17:33:21 PDT 2026**. The new all-eight seven-saturation proof below uses ONLY the explicit `Sun_7(G)` hypothesis and elementary actual-coset/index reasoning. The independently reconstructed P7 normal-section descent was already supported as a DIRECT P7 result in the prior parent source; it is included here so the new global bridge does not merely rely on its headline. No arbitrary-group Sun8 solution is claimed.

## 1. Exact theorem and scope

For a group X, `Sun_k(X)` means every k pairwise-disjoint actual LEFT cosets of finite-index subgroups have a pair of indices with gcd>=k. A **direct P7 configuration** is eight such cosets whose indices are `7r_i` with positive pairwise-coprime r_i, including any single private factor divisible by7.

**Theorem A (localized).** For ANY group G, if `Sun_7(G)` holds and `Sun_8(G)` fails, then EVERY actual counterconfiguration to Sun8 in G is a direct P7 configuration. If ANY group has a direct P7 configuration, then there is such a configuration in a FINITE NONABELIAN SIMPLE group.

**Corollary (conditional global equivalence).** If the arbitrary-group Sun7 statement holds, then the following are equivalent:

- Sun8 holds for every group;
- Sun8 holds for every finite nonabelian simple group.

The reverse direction is the new bridge plus the direct-P7 finite-simple descent; the forward direction is inclusion of a subclass. The statement does NOT assert Sun8 for the finite simple groups. It identifies the exact remaining universal target, with no simple-group classification or finite cutoff.

**Sun7 import boundary.** The later 2026-10-20 parent record `sun7-complete-written-composition-parent-verdict-v1.md`, SHA256 `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`, states the exact all-group Sun7 assertion as `CORRECTNESS_ACCEPTED_WRITTEN_COMPOSITION` at its named source/errata/imports. Its full proof/dependency closure has NOT been independently reverified here; it is not a Lean/human/publication/priority certificate. The older 2026-10-18 partial Stage B verdict explicitly said no Sun7 theorem; this predates the later composition and is not represented as its proof. Without the Sun7 import, Theorem A's FIRST hypothesis remains explicit. The direct-P7 finite-simple statement in the theorem's SECOND sentence uses NO Sun7 hypothesis.

## 2. The elementary two-coset fact

Two actual left cosets of finite-index subgroups H,K in any group X must intersect if `[X:H]` and `[X:K]` are coprime. Indeed the diagonal map

    X/(H∩K) -> X/H × X/K

is injective. Its finite domain index is a common multiple of `[X:H]` and `[X:K]`, and is at most their product, so coprimality forces equality and the map is onto. In particular, pairwise disjoint actual finite-index cosets have original-index gcd at least2. No normality, finiteness of X, or intersection of abstract numerical indices is assumed.

## 3. ALL eight original indices must contain7

Let G satisfy `Sun_7(G)` and let `g_i U_i`, i=1,...,8, be an ACTUAL Sun8 counterconfiguration. Write n_i=[G:U_i]. Thus `gcd(n_i,n_j)<=7` for every distinct pair, while Section2 gives `gcd(n_i,n_j)>=2`.

Apply `Sun_7(G)` to each of the eight seven-label subfamilies. The pair it supplies has gcd exactly7. Hence at least THREE of the n_i are divisible by7: if at most two were, delete one of those at most two to obtain a seven-subfamily containing at most one.

For any two distinct seven-divisible labels i,l, `gcd(n_i,n_l)=7`. Suppose some label j has `7∤n_j`. For each seven-label i, Section2 and the counterconfiguration bound give

    2 <= gcd(n_i,n_j) <= 7,

and this gcd is prime to7. Choose ANY prime factor p_i of that gcd; necessarily `p_i∈{2,3,5}`. The p_i for different seven-labels are distinct, because any prime common to n_i and n_l must divide their gcd7, while p_i is not7. Therefore there are at most THREE seven-labels. There are already at least three, so exactly three, and every non-seven original index n_j is divisible by each of2,3,5, hence by30.

But with exactly three seven-labels there are FIVE non-seven labels. Two of their original indices share30, contradicting `gcd<=7`. Hence NO label j can be seven-free. All eight n_i are divisible by7, and every pair has gcd exactly7. Consequently

    n_i=7r_i,      gcd(r_i,r_j)=1 for every i≠j.                (3.1)

This proves Theorem A's first sentence for the SAME actual G-cosets. It does not require normal subgroups, finite G, any source enlargement, a small-index table or an independent numerical realization of the r_i. At most one r_i can contain the prime7, but that possible private-seven owner is retained below.

## 4. Finite-core preservation of an actual direct P7 family

Let ANY group G carry a direct P7 family. For each finite-index U_i, its core `core_G(U_i)` is the kernel of the finite left-coset action on G/U_i, hence is finite-index normal and contained in U_i. Their finite intersection K is finite-index normal and contained in EVERY U_i. Project into F=G/K. Because K⊂U_i, each original coset is the full inverse image of its projected coset. Thus the eight projected actual left cosets remain pairwise disjoint and their subgroup indices remain EXACTLY `7r_i`.

At least one finite direct P7 group exists, and the positive integer group orders have a least value. Choose a globally least-order finite direct P7 group F. This is minimum GROUP ORDER across all finite examples, not a minimum private-index sum in a fixed group.

## 5. Normal-section descent, including the private-seven owner

Suppose F has a proper nontrivial normal subgroup N. For each ORIGINAL U_i and its original coset, set

    c_i=[N:N∩U_i],  d_i=[F/N:NU_i/N],
    c_i d_i=7r_i,  C_i=pi(g_i)pi(U_i).

At any point of C_i, the corresponding actual fibre is a left N-coset of N∩U_i, with index c_i. Fibres of disjoint original cosets are disjoint. Hence if `gcd(d_i,d_j)=1`, the ACTUAL quotient cosets meet by Section2; if in addition `gcd(c_i,c_j)=1`, their actual N-fibre cosets meet by Section2 and the original cosets intersect, a contradiction.

Because the r_i are pairwise coprime, at most ONE of them is divisible by7. Designate its label e if it exists; otherwise designate any one label e. The remaining SEVEN regular r_i are all prime to7. For each regular i the single 7 in 7r_i lies wholly in exactly one of c_i,d_i.

Two regular labels cannot put that factor7 on opposite sides. If c_i has7 and d_i does not, while d_j has7 and c_j does not, pairwise coprimality of r_i,r_j gives both `gcd(c_i,c_j)=1` and `gcd(d_i,d_j)=1`, which the preceding actual two-stage intersection argument forbids. Therefore ALL seven regular labels place7 on the SAME side.

### 5.1. Quotient side for the seven regular labels

Suppose every regular d_i is divisible by7 and every regular c_i is seven-free. For any two c_i,c_j, at least one label is regular and their private r's are coprime; a common divisor cannot contain7 or any shared private prime. Thus ALL EIGHT c_i are pairwise coprime, INCLUDING c_e even if r_e contains a higher power of7.

If any two quotient cosets C_i,C_j met, their actual N-fibre cosets would have coprime indices and would intersect, contradiction. Therefore the EIGHT actual C_i are pairwise disjoint. If d_e were seven-free, then its gcd with any regular d_i would be1, since r_e is coprime to r_i. Section2 would force C_e to meet C_i, contradiction. Thus every d_i is divisible by7, and

    d_i=7s_i with s_i|r_i; the s_i are pairwise coprime.

The smaller actual quotient F/N therefore has a direct P7 family. This contradicts least order because N is nontrivial.

### 5.2. Kernel side for the seven regular labels

Suppose every regular c_i is divisible by7 and every regular d_i is seven-free. As in the prior paragraph, ALL EIGHT quotient indices d_i are pairwise coprime, including d_e. The multi-coset diagonal map

    (F/N)/(intersection_i pi(U_i)) -> product_i (F/N)/pi(U_i)

is injective; its domain index is divisible by every d_i and at most their product. Pairwise coprimality forces equality, so the map is surjective. Therefore the SAME eight projected cosets have ONE common point, not merely pairwise intersections.

Translate that common actual fibre into N. It contains EIGHT pairwise-disjoint actual N-cosets with subgroup indices c_i. If c_e were seven-free, its index would be coprime to every regular c_i (their private r's are coprime), forcing an intersection, contradiction. Hence

    c_i=7s_i with s_i|r_i; the s_i are pairwise coprime.

Thus the smaller proper normal subgroup N itself has a direct P7 family, contradicting least order.

The two placements exhaust every possibility. Thus a least-order finite P7 group has NO proper nontrivial normal subgroup and is simple. It cannot be cyclic of prime order: if its order p is not7, no index is divisible by7; if p=7, all eight cosets would be distinct singleton cosets in a seven-element group. Hence it is finite NONABELIAN simple. This proves Theorem A's second sentence independently of Sun7. □

## 6. Verification, prior support and precise nonclaims

The finite support checker `frontier-20261028-global-seven-support-check.py`, SHA256 `882e6cb61e7baccd76216301a14a0428dc15ffe805672738e6398768db39d5b3`, was run with a20-second deadline. Actual output:

```text
partial_multiset_counts: [1, 15, 61, 102, 119, 139, 161, 183, 205]
eight_label_patterns_with_at_least_three_sevens: 15
patterns_with_at_least_one_nonseven: 0
PASS: every eligible eight-label support multiset is seven-divisible
Wed Oct 28 17:32:48 PDT 2026
```

Its squarefree supports on2,3,5,7 overapproximate all actual index tuples with every pair gcd between2 and7; primes>7 cannot be shared under that upper bound, and truncating higher powers cannot remove a shared small prime. The condition of at least three seven labels is the exact consequence of the stated Sun7 premise. The program checks the finite arithmetic shadow of Section3 only; it does not construct cosets, prove Sun7, verify the finite-core/normal-section descent, or establish a formal proof.

The earlier parent disposition `sun-unrestricted-private-and-least-order-source-union-parent-v1.md` already supports direct-P7 least-order simple descent and explicitly says the global Sun7/Sun8-to-P7 ancestry was NOT reauthenticated at that gate. The present Section3 supplies a short NEW written bridge at the EXPLICIT Sun7(G) hypothesis; Section5 independently restates/pays the actual subgroup/fibre descent. No assertion of first discovery or retrospective correction of the earlier disposition is made. The present equivalence is conditional on the prior all-group Sun7 statement and on review of THIS proof, not on a new public-source verification.

No current simple group is shown to be a counterexample, and no completeness of the previously screened simple families is inferred. Arbitrary finite nonabelian simple groups, the original unrestricted target, formal/human/independent-family review, source priority and novelty remain open. Earlier held outputs are not used as valid premises or retroactively validated; previous exposure is not claimed erased.
