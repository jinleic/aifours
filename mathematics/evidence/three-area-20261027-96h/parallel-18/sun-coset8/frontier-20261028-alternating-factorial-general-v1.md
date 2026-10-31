# Factorial-terminal incompatibility for arbitrary bounded alternating offset

**Status: WRITTEN structural candidate, conditional on the named public A_r theorem and the earlier exact projection/quotient argument; not independently reviewed or accepted.** Let r≥419 be an eligible prime, meaning r is not (q^d−1)/(q−1) for any prime power q and d≥2. Let t≥1 and r+1>7t!. Then no two actual proper-subgroup indices N0,N1 in A_(r+t) can satisfy
\[(r-2)!\mid N_0,\qquad r\nmid N_1,\qquad \gcd(N_0,N_1)=7.\]
In particular, no P7 pattern in A_(r+t) has a factorial-terminal index, for **any** t meeting the size condition: at most one of seven pairwise-gcd-7 indices is r-divisible, so a factorial-terminal label always has another r-free label. This is a factorial-branch exclusion only, not a claim that P7 is solved for arbitrary t.

The result replaces the t≤33 prime-support sieve in `frontier-20261028-alternating-factorial-terminal-33-v1.md`, SHA `363205fefd1b34bde523523e87f9c981a0a45409f006c53391a46c4e29384186`; that predecessor remains unchanged and is not independently validated by this new route. No historical novelty or priority is claimed.

## 1. Source and exact chain input

Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2 says a Sylow r-subgroup of A_r has unique maximal overgroup AGL1(r)∩A_r, of index F=(r−2)!. The actual projection step, including its exact quotient, is in `frontier-20261028-alternating-seven-cell-p7-v1.md`, SHA `5b359f8e23db44d4064646db971ab33e643f03b103eb927b9e74c9f90f46d80f`: at an intransitive orbit with complement u,
\[[A_{r+j}:H]=\binom{r+j}{u}[A_m:P]c,\qquad c\mid u!,\]
where P is an actual transitive subgroup containing the same r-cycle in A_m. Transitive fixed-point descents preserve the index. The source and prior quotient proof remain independently unreviewed. The size condition implies t<r, so these Sylow subgroups have order r and all large-block arguments apply. No Sun7 is used.

The writer's source exposure was nonblind; the incidental cross-topic display was recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No such content is used and no historical hold is modified.

## 2. Small divisors of the second index

Assume F|N0 and gcd(N0,N1)=7. Since F contains 7² and every prime at most r−2, N1 has exactly one factor 7 and has no other prime factor below r: r−1 is even and greater than 2. Thus **no divisor of N1 lies strictly between 7 and r**. In particular N1 is divisible by 7.

Conjugate the subgroup underlying the r-free index N1 to contain an r-cycle and follow the exact actual projection chain from Section 1. It cannot reach a proper subgroup of A_r: the source theorem would put F into N1, yielding gcd(F,N1)>7. Thus it terminates with a full alternating-block projection and gives an exact product of binomial windows and quotient factors c_i|u_i!.

## 3. Eliminate long and singleton windows

If a window has length u≥2, its consecutive positions contain an odd h, and r+h is even. Since u! is even,
\[d=\frac{r+h}{\gcd(r+h,u!)}\]
divides that binomial, and hence N1. But
\[7<\frac{r+1}{t!}\le d\le\frac{r+t}{2}<r,\]
contradicting Section 2. Therefore every window has length 1, with quotient c_i=1.

The exact product for N1 is then a product of singleton factors r+h. Because 7|N1, some factor r+h is divisible by 7. Its quotient (r+h)/7 is also a divisor of N1 and lies strictly between 7 and r: r≥419 gives (r+h)/7>7 and t<r gives (r+h)/7<2r/7<r. This again contradicts Section 2. Hence the asserted pair of indices cannot exist.

## 4. Actual finite control and review boundary

`frontier-20261028-alternating-factorial-general-check.py`, SHA-256 `e288721f57b6b9f20bed93e5deaf1840b2179cd1f8ca4dabd39f4318be239f8c`, 23 LF / 881 bytes, ran at 19:32:33 PDT on 2026-10-28. It checked exact inequalities and binomial divisibility for four selected (r,t) pairs with t=3,9,11,13. These are finite integer controls only; they do not prove the arbitrary subgroup chain, public classification or universal implication.

**Review-critical:** verify the deduction gcd(F,N1)=7 and the complete small-divisor classification, exact projection product including every c_i, existence of an even numerator in each length≥2 window, and the singleton 7-factor contradiction. No source proof replay, independent/formal review, historical novelty, or old-hold modification is asserted.
