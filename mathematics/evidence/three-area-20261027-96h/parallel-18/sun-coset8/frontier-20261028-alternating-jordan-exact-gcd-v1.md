# Jordan subgroup family with the exact binomial common divisor

**Status: WRITTEN successor candidate, conditional on the named classical Jordan theorem; not independently reviewed, formally verified or accepted.** Let r>7 be prime, 3≤t<r, n=r+t, and L=lcm(1,…,t). Put D*=n/gcd(n,L). If D*>7, A_n has no three proper subgroup indices with pairwise gcd at most 7. In particular direct P7 is excluded and Sun8 holds for actual disjoint cosets in this restricted family. This strictly enlarges the factorial-denominator family in `frontier-20261028-alternating-jordan-index-p7-v1.md`, SHA `ef546a7331a3938c5b550998d470ed12e4855af1e5e6014e19377b4e1e872482`; it is a prospective successor, not a retroactive change to that frozen primary. No all-degree, global, published-priority or novelty claim is made.

## 1. Named input and actual subgroup reduction

The sole non-elementary group input is Jordan's theorem as stated in Gareth A. Jones, Theorem 1.1, https://arxiv.org/html/1209.5169v1: a finite primitive group containing a prime cycle fixing at least three points contains the alternating group. Its proof is not independently reconstructed. The earlier Jordan candidate proves directly that, because r>n/2 and t≥3, every **proper** subgroup H<A_n whose index is r-free is intransitive: transitivity would be primitive (the r-cycle acts trivially on fewer than r blocks), and Jordan would force H=A_n. Its orbit U containing the r-cycle support has complement size 1≤u≤t, so the actual index is divisible by C(n,u).

**Pre-source order:** read `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json`, SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, before the prior Jordan candidate or any listed prior alternating source. This packet does not retroactively import Jordan into f116, old held history, the integer-relaxation packet or any prior verdict. Writer exposure was nonblind; the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`, and is not used here.

## 2. Exact gcd identity for the full binomial family

For integers 1≤t<n let
\[g(n,t)=\gcd\{\binom n1,\ldots,\binom nt\}.\]
We prove in writing the exact identity
\[g(n,t)=\frac n{\gcd(n,\operatorname{lcm}(1,\ldots,t))}.\tag{1}\]

For each u≤t, the identity u C(n,u)=n C(n−1,u−1) shows n/gcd(n,u) divides C(n,u). Since u|L, the right-hand side of (1) divides every C(n,u), giving one divisibility.

For the reverse divisibility fix a prime p dividing n. Write s=v_p(n), h=v_p(L), and j=min(s,h). Then u=p^j≤t (with p^0=1). Since p^j|n,
\[\binom n{p^j}=\frac n{p^j}\binom{n-1}{p^j-1}.\]
The last binomial is not divisible by p: write n=p^j m. In F_p[X], (1+X)^(p^j)=1+X^(p^j), so the coefficient of X^(p^j−1) in
\[(1+X)^{n-1}=(1+X)^{p^j-1}\bigl((1+X)^{p^j}\bigr)^{m-1}\]
is 1 mod p. Therefore v_p(C(n,p^j))=s−j=max(s−h,0), matching the p-adic valuation of the right-hand side of (1). Every common divisor also divides C(n,1)=n, so primes outside n introduce nothing. This proves (1), including j=0.

## 3. Actual-group consequence and strict extension

Every r-free proper-subgroup index is divisible by some C(n,u), u≤t, and hence by D*=g(n,t). If D*>7, two such indices have gcd>7. Among any three indices with pairwise gcd≤7 at most one is divisible by r>7, giving the contradiction. Eight disjoint cosets cannot include the whole group, so their subgroups are proper and Sun8 follows within this same D*>7 source-conditional family.

Since L divides t!, D* is a multiple of the earlier D=n/gcd(n,t!). The extension is strict: for A64 take r=53,t=11. Then 53 is prime, 3≤11<53,
\[\frac{64}{\gcd(64,11!)}=1,\qquad
 \frac{64}{\gcd(64,\operatorname{lcm}(1,\ldots,11))}=8.\]
Thus the earlier factorial condition says nothing while this theorem excludes direct P7 and gives Sun8 for A64, conditional on Jordan. Identity (1) says D* is the **largest common divisor of this full binomial list**; it does not establish that every u or divisor is realized as a subgroup index, nor that the D*≤7 cases are counterexamples.

## 4. Actual finite controls and review obligations

`frontier-20261028-alternating-binomial-gcd-check.py`, SHA-256 `8abf9d9251910186caf7136a1bc4ab38be7ea3ffcaacd4b6c8c43764163bc4a1`, 23 LF / 792 bytes, ran at 19:57:29 PDT on 2026-10-28. It verified identity (1) using exact integer gcd/lcm/binomial arithmetic for all 4,950 pairs 2≤n≤100 and 1≤t<n, and checked the A64 strict-extension numbers. These finite checks do not prove the universal identity, Jordan's theorem, actual subgroup classification or a novelty claim.

**Review-critical:** verify the Jordan-source/proper-intransitivity argument, the p-adic upper bound via the Frobenius coefficient for every prime including j=0, and the actual subgroup/binomial and coset scope. No all-degree or global verdict, earlier source modification or old-hold rehabilitation is implied.
