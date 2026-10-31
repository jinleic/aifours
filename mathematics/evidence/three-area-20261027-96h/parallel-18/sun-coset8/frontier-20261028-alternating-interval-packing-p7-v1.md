# Alternating P7 exclusion by packing typed orbit windows

**Status: WRITTEN candidate, conditional on the named public A_r theorem and the earlier written base/orbit descent; not independently reviewed or accepted.** Let r≥419 be a prime which is not a prime-power repunit (q^d−1)/(q−1), d≥2. Let t≥1 satisfy
\[r+1>7t!.\]
In G=A_(r+t), any collection of proper subgroup indices whose pairwise gcds are all **exactly 7** has size at most floor(t/2)+2. Consequently, for every t≤9 satisfying the inequality, direct P7 is excluded. For t≤11, no eight indices can have all pairwise gcd exactly 7; this last statement is **not** by itself an unrestricted Sun8 claim, because general Sun8 configurations need not have a common factor 7 without an additional Sun7/R8 import.

For any fixed t, the size condition excludes only finitely many r. The elementary count in the earlier orbit packet shows the eligible primes have relative density one among primes, so these are unbounded actual-simple-group families. We do not claim published priority, historical novelty, or the unproved unrestricted alternating/global target.

## 1. Source boundary and typed branches

The non-elementary group input is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2: for eligible r≥419, a Sylow r-subgroup of A_r has unique maximal overgroup AGL1(r)∩A_r. The previously written base argument shows that every r-free proper-subgroup index in A_(r+1) is divisible by r+1; see `frontier-20261028-alternating-successor-degree-v1.md`, SHA `f6b9d6ce920f234bc89f2be0aaae709442cc16bfccf8716366df64b322fc228c`. The actual orbit/stabilizer descent and its full binomial types appear in `frontier-20261028-alternating-six-step-typed-p7-v1.md`, SHA `b58cde595c44155c158d0d2226b721ace070322233774611d79b7c4772c57aa4`. We re-state the needed extension to arbitrary t below. Neither the source classification nor the earlier written proofs have been independently reviewed here.

The writer was nonblind. The incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no such snippet is used in this proof. No clean-cognition, prior-art clearance, or historical-hold rehabilitation claim follows.

## 2. Descent produces a numerator window

Since r+1>7t!, we have t<r, and a Sylow r-subgroup R of A_(r+t) is an r-cycle with t fixed points. If a proper subgroup H has r-free index, conjugate it to contain R. Descend through point stabilizers fixed by R while the subgroup is transitive; each descent preserves its index and produces a proper subgroup containing R. If the descent reaches A_(r+1), the original index is divisible by r+1; call this **type 1** with window W={1}. Otherwise, at the first intransitive stage A_(r+j), 2≤j≤t, the orbit of H containing the r moved points has a complement of size u∈{1,…,j}. Its setwise stabilizer has index
\[B_{j,u}=\binom{r+j}{u},\]
so the original index is divisible by B_(j,u). Associate the **window**
\[W_{j,u}=\{j-u+1,j-u+2,\ldots,j\},\]
corresponding to the consecutive factors r+h, h∈W, in the numerator of the binomial. Choose one valid actual descent/type for each subgroup; no uniqueness of this choice is assumed.

## 3. Overlap is impossible

Suppose two selected windows share h. Let a=r+h and put F=a/gcd(a,t!). If the first type is a binomial with denominator u!, then u! divides t! and a divides u!·B; Euclid's lemma implies F|B. The same is true for the second binomial, and type 1 is covered because its associated divisor is exactly r+1. Thus F divides both original indices. Since F≥(r+1)/t!>7, their gcd cannot be exactly 7. Therefore the windows of any P7-pattern r-free indices are **pairwise disjoint**, including windows with the same endpoint type.

## 4. Packing bound using the actual common 7

Consider a collection of at least two indices with pairwise gcd 7; each is divisible by 7, and at most one is even. Let e be the number of selected r-free windows with even endpoint j and o the number with odd endpoint j.

If j is odd, r+j is even. For odd u, the integer (r+j)/gcd(r+j,u) is even and divides binom(r+j,u); so the original index is even. Type 1 is also even. Hence at most one selected odd endpoint can have odd u (or be type 1). Every other selected odd endpoint has even u≥2, so its window contains the **even** position j−1. These positions are distinct for distinct odd endpoints. Pairwise window disjointness means none of them is an endpoint of a selected even type, and all are among the floor(t/2) even positions from 1 to t. Consequently
\[e+(o-1)\le\lfloor t/2\rfloor,\qquad e+o\le\lfloor t/2\rfloor+1.\]
At most one original index can be divisible by r>7, so the entire collection has at most floor(t/2)+2 members. For t≤9 this is at most 6 and excludes seven P7 indices. For t≤11 it is at most 7 and excludes eight indices **when their pairwise gcd is 7**. A singleton collection is trivial and does not affect the bound.

## 5. Actual exact control and scope

`frontier-20261028-alternating-interval-check.py`, SHA-256 `d2f9790348db6ac5eff588c7663f798275e9d6b4b5abd26f9bcb985b4528e6d3`, 65 LF / 1729 bytes, ran at 18:51:07 PDT on 2026-10-28. It found the eligible prime r=2,540,173 above 7·9!, checked its primitive geometric-sum exclusions, and used exact dynamic programming over type windows to confirm a maximum of 5 disjoint windows with at most one even binomial for t=9. This is one finite integer control, not a proof of the packing argument, source subgroup classification, or subgroup realization.

**Review-critical:** verify the A_r source condition and base, the all-t descent including n<2r, the denominator overlap divisor, the odd-endpoint predecessor injection, and the exact common-7 scope. The earlier elementary prime-density argument is separately reviewable. No source-proof replay, novelty clearance, or modification of old holds is claimed.
