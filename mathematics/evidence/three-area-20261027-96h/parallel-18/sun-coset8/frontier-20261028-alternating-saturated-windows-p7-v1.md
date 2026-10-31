# Alternating P7 exclusion through eleven positions by saturation

**Status: WRITTEN candidate, conditional on the exact public A_r source theorem and the earlier written orbit/window arguments; not independently reviewed or accepted.** Let r≥419 be a prime which is not a prime-power repunit (q^d−1)/(q−1), d≥2. For t=10 or 11, if r+1>7t!, then A_(r+t) has no seven proper subgroup indices whose pairwise gcds are all exactly 7. Combined with the previous t≤9 interval-packing candidate, this excludes direct P7 for every fixed t≤11 once r satisfies the same sufficient size condition. The earlier elementary prime count implies infinitely many such eligible r for each fixed t. No historical novelty, published priority, unrestricted Sun8, or global all-simple-groups claim is made.

## 1. Inputs and nonblind scope

The source classification import is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2, giving the unique maximal Sylow-r overgroup in A_r for eligible r. The base A_(r+1) index divisibility, actual orbit descent and numerator-window no-overlap argument are in `frontier-20261028-alternating-interval-packing-p7-v1.md`, SHA `cc6aa191d75c2658a6f93e92468d6ac9aab178c1cfc54effa3c0e50e1cc11e4f`, with the base and source dependencies named there. Those written arguments and the public classification remain independently unreviewed here; no Sun7 or old-hold rehabilitation is assumed.

The writer was nonblind; the incidental cross-topic display was recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No such snippet is used below.

## 2. Why the previous bound must be saturated

Suppose seven proper-subgroup indices have pairwise gcd exactly 7. At most one is divisible by r>7. For t=10 or 11, the earlier interval argument bounds the number of r-free indices by floor(t/2)+1=6. Therefore there are **exactly six r-free indices** and one r-divisible index.

For each r-free index choose one valid typed window from the actual orbit descent. The windows are pairwise disjoint, because a common numerator factor r+h would yield common divisor (r+h)/gcd(r+h,t!)>7. Let e and o be the numbers with even and odd endpoint. Let c count odd endpoints whose binomial is even, including the type-1 base. The common factor 7 implies at most one even index, so c≤1. Every other odd endpoint has even window length and therefore uses its distinct even predecessor. These predecessor positions and the even endpoints are mutually distinct among the five even positions 2,4,6,8,10. Thus
\[e+o=6,\qquad e+(o-c)\le5,\qquad c\le1.\]
Equality forces c=1 and **all five even positions** to be represented, each either by an even endpoint or by the predecessor of a nonexceptional odd endpoint. Distinct represented positions belong to distinct r-free indices.

## 3. Each saturated even position supplies its full factor

Fix one represented even position k.

- If k is the endpoint of an even type, its window has length u≤2. Otherwise u≥3 also covers the even position k−2, which is represented by a different window, violating disjointness. Since r+k is odd, both C(r+k,1) and C(r+k,2) are divisible by r+k.
- If k is the predecessor of a nonexceptional odd endpoint k+1, that window has even length u=2. If u≥4 it also covers the represented even position k−2, again violating disjointness. Since r+k+1 is even, C(r+k+1,2)=((r+k+1)/2)(r+k) is divisible by r+k.

At k=2 the forbidden longer lengths are automatically unavailable. Thus five **distinct** r-free indices are divisible respectively by r+2, r+4, r+6, r+8 and r+10.

Because r is a prime greater than 3, r≡1 or 2 mod 3. In the first case r+2 and r+8 are divisible by 3; in the second r+4 and r+10 are divisible by 3. The corresponding distinct indices are both divisible by 3 and by 7, so their gcd is at least 21, contradiction. This pays the equality case left open by the earlier floor(t/2)+2 bound, for **both** t=10 and t=11.

## 4. Actual exact control and scope

`frontier-20261028-alternating-saturation-check.py`, SHA-256 `a8aae12d6bff39aaca24bc8080afe81b82473d681b0a722ab02680fc6f729366`, 59 LF / 1698 bytes, ran at 18:53:05 PDT on 2026-10-28. It found one eligible prime r=279,417,613 above 7·11!, and used exact dynamic programming to check that at t=10 and t=11 at most five selected pairwise-disjoint typed windows can have at most one even and at most one 3-divisible binomial. This is one finite control, not an actual subgroup enumeration, a proof of the all-r saturation lemma, or verification of the imported source.

**Review-critical:** verify the equality/saturation argument, distinctness of represented even positions and indices, absence of unrepresented even positions in longer windows, the full-factor divisibility in both cases, and the two residue classes mod 3. Reconstruct the source theorem and earlier prime-density argument separately. No old hold, published-priority claim, or unrestricted target verdict is changed.
