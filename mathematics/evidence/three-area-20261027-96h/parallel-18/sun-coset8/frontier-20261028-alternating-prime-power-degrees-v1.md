# Alternating groups of odd prime-power degree

**Status: WRITTEN candidate conditional on the three named classical/external statements; not independently reviewed, formally verified or accepted.** Let n=p^a≥17 for a prime p>7 and integer a≥1. Then A_n has no three proper subgroups whose indices have all pairwise gcds at most 7. In particular A_n excludes direct P7 and satisfies Sun8 for actual pairwise disjoint cosets, at this exact source-conditional scope. This includes every prime degree n≥17, but not prime-power degrees of characteristic 2,3,5,7, or arbitrary alternating degrees. No published-priority or novelty claim is made.

## 1. Exact named imports and pre-source condition

- **Bertrand:** for integer m>1 there is a prime r with m<r<2m; see the elementary theorem/proof statement at https://academicweb.nd.edu/~dgalvin1/pdf/bertrand.pdf.
- **Jordan:** Gareth A. Jones, Theorem 1.1, https://arxiv.org/html/1209.5169v1: a primitive permutation group containing a prime cycle fixing at least three points contains A_n.
- **Two fixed points:** Jones Theorem 1.2, case k=2, same source: a primitive degree-n group not containing A_n but containing a cycle with exactly two fixed points satisfies PGL2(q)≤H≤PΓL2(q) with n=q+1 for a prime power q. The source explicitly notes its classification proof uses CFSG. We import the stated conclusion, not its proof or a formal verification.

The source proofs and their dependencies are not independently reconstructed here. Standard Sylow, elementary block actions, orbit-stabilizer and alternating-group facts are also used. No A_r unique-overgroup theorem, Sun7 or R8 is required.

Before any earlier alternating source body cited for context, read `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json`, SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`. This prospective packet does not inject Jordan/Jones retroactively into f116, held history, earlier integer models or prior verdicts. Writer exposure was nonblind; the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json` SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no such content is used.

## 2. Select an actual large prime cycle

n is odd. Put m=(n−1)/2. Bertrand gives a prime r with m<r<2m=n−1. Thus r>n/2, r≤n−2 and r>7; t=n−r is even and at least 2. Since n<2r, the Sylow r-subgroups of A_n have order r and consist of an r-cycle with t fixed points.

Let H<A_n have r-free index. Then H contains a Sylow r-subgroup. If H is transitive, it is primitive: a nontrivial block system has fewer than r blocks, so the r-cycle fixes every block; its r moved points must lie in one block, forcing the degree at least 2r, contradiction.

If t≥3, Jordan forces H to contain A_n, contrary to H<A_n. If t=2, the Jones k=2 statement forces q=n−1=r+1 to be a prime power. q is even, hence q=2^e. But q−1=r is a prime >7 and q+1=n=p^a has p>7. Modulo 3, one of 2^e−1 and 2^e+1 is divisible by 3. Neither number is divisible by 3 under these hypotheses, a contradiction. Therefore **every r-free proper H is intransitive**, including the two-fixed-point case.

## 3. Every r-free index shares p

The H-orbit containing the r moved points has complement u with 1≤u≤t. Its setwise stabilizer in A_n has index C(n,u), hence C(n,u) divides [A_n:H]. Since n=p^a, in characteristic p
\[(1+X)^n=(1+X^{p^a}),\]
so p divides every C(n,u) for 1≤u<n. In particular p divides every r-free proper-subgroup index.

Among three indices whose pairwise gcd is at most 7, at most one is divisible by r>7. The other two are r-free and hence both divisible by p>7, a contradiction. Seven indices of pairwise gcd 7 are therefore impossible. For Sun8, eight pairwise disjoint cosets cannot include a coset of the whole group, so their subgroups are proper and any three already force a pair gcd>7.

This proof pays the t=2 case using the additional Jones classification statement; it does not silently apply the three-fixed-point Jordan theorem to a cycle fixing only two points.

## 4. Actual arithmetic control and review scope

`frontier-20261028-alternating-prime-power-check.py`, SHA-256 `1e367ecd5385e724c1b4c173ce09d2bef26594292f4f6e5b36ad790e9a2ae80b`, 31 LF / 958 bytes, ran at 19:59:49 PDT on 2026-10-28. It checked the prime-cycle selection and all binomial p-divisibilities for 59 prime-power degrees n≤300, including 17 where the selected r gives t=2. This is bounded exact arithmetic only; it does not prove Bertrand, Jordan, Jones, CFSG or any actual subgroup statement.

**Review-critical:** verify the exact Jones Theorem 1.2 k=2 scope, the even-prime-power/mod-3 elimination, Bertrand endpoint, primitive-block reasoning and common-p binomial divisor. This is an unreviewed source-conditional family, not a human/formal proof or global Sun8 verdict.
