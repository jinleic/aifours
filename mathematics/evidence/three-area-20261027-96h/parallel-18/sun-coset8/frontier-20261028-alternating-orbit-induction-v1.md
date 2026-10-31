# An orbit induction for seven consecutive alternating degrees

**Status: WRITTEN candidate, conditional on the one public source statement below; not independently reviewed or accepted.** Let r≥419 be a prime which is not of the form (q^d−1)/(q−1) for any prime power q and d≥2. For t=1,…,5, the actual simple group A_(r+t) has no seven proper subgroup indices with all pairwise gcd at most 7; in particular it excludes the direct P7 configuration. For t=6, A_(r+6) has no eight such indices and therefore satisfies the Sun8 conclusion. More precisely, in A_(r+t) any collection of proper subgroup indices with pairwise gcd≤7 has size at most t+1 for every t=1,…,6.

There are infinitely many eligible primes r: the elementary counting argument in Section 5 shows that eligible primes have relative density one among all primes. In particular this gives genuinely unbounded actual-group families, rather than a finite enumeration. No claim of publication priority or historical novelty is made. This packet does not claim all alternating degrees or an unconditional all-simple-groups theorem.

## 1. Named source input and provenance

The only non-elementary group-theoretic input is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2: for an eligible odd prime r≠11,23, a fixed Sylow r-subgroup of A_r has the **unique** maximal overgroup AGL1(r)∩A_r. The source theorem and its proof dependencies are not independently reconstructed. We also use standard Sylow, Lagrange, orbit-stabilizer, and alternating-group order/simplicity facts. All primes considered here exceed the source's small-n≤24 Magma-handling range, but the global source classification still remains an unreviewed import.

The base case below independently restates the argument in `frontier-20261028-alternating-successor-degree-v1.md`, SHA `f6b9d6ce920f234bc89f2be0aaae709442cc16bfccf8716366df64b322fc228c`. The general orbit induction and prime-density calculation are additional written derivations, not source-stated unique-overgroup cases. Writer exposure was nonblind; the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`, and no Olson/Kac-Moody excerpt is used here. No clean-cognition or historical-hold rehabilitation claim follows.

## 2. Common divisor in the base degree

Let G1=A_(r+1), and let R be an r-cycle fixing x. If H<G1 has r-free index, it contains a conjugate of R; conjugate H so R≤H. If H is intransitive, its orbit containing the r moved points must be exactly those r points, so H fixes x and [G1:H] is divisible by r+1.

If H is transitive, H_x is a proper subgroup of A_r containing R; otherwise orbit-stabilizer would give |H|=|G1|. By the source H_x≤AGL1(r)∩A_r, of order r(r−1)/2. Thus |H|=(r+1)|H_x| divides (r+1)r(r−1)/2. This divides |A_r|=r!/2 because r+1 divides (r−2)!: the distinct factors 2 and (r+1)/2 both occur in the factorial. Hence [G1:H]=(r+1)|A_r|/|H| is divisible by r+1 in this case too.

## 3. Uniform binomial divisors

For j≥1 let
\[L_j=\operatorname{lcm}(1,2,\ldots,j),\qquad
  d_j=\frac{r+j}{\gcd(r+j,L_j)}.\]
For any 1≤u≤j, put n=r+j and g_u=gcd(n,u). From u·binom(n,u)=n·binom(n−1,u−1), coprimality of n/g_u and u/g_u shows that n/g_u divides binom(n,u). As u|L_j, we have g_u|gcd(n,L_j), so **d_j divides every binom(n,u), 1≤u≤j**.

For r≥419 and 1≤j≤6, L_j≤60 and r+j>420≥7L_j. Therefore d_j≥(r+j)/L_j>7. In the base case d1=r+1.

## 4. Orbit induction on actual subgroups

For fixed t≤6 put G_j=A_(r+j) for j=1,…,t, and regard R as an r-cycle fixing j points. Since r+j<2r, a Sylow r-subgroup of each G_j has order r and is conjugate to R.

**Claim:** for every proper H<G_j with r-free index, [G_j:H] is divisible by at least one of d1,…,dj.

For j=1 this is Section 2. Assume j≥2 and the claim at j−1. Conjugate H so R≤H. The H-orbit O containing the r moved points of R has size r+s for some 0≤s≤j.

- If s<j, H stabilizes O. The setwise stabilizer of O in A_(r+j) has index binom(r+j,j−s): the large block has at least two elements, so its symmetric stabilizer contains an odd permutation. Consequently the original subgroup index is divisible by that binomial and hence by d_j.
- If s=j, H is transitive. Choose any point x fixed by R. Then H_x≤A_(r+j−1) contains R, and H_x is proper because otherwise |H|=|G_j|. Orbit-stabilizer gives [G_j:H]=[G_(j−1):H_x]. This index is r-free and the induction hypothesis supplies one of d1,…,d_(j−1).

This completes the all-subgroup induction. In a pairwise-gcd≤7 collection, at most one index is divisible by r. Every other index is divisible by at least one of the j numbers d1,…,dj, each >7, so each such divisor can occur for at most one index. There are therefore at most j+1 indices. For j≤5 this is at most 6 and excludes seven (hence direct P7); for j=6 it is at most 7 and excludes eight (Sun8). No assumption of coprimeness, a coset-cover relaxation, or Sun7 is made.

## 5. Infinitely many admissible primes, by an elementary count

Call a prime bad if it has the excluded repunit form. For bad odd primes from d=2, q+1 is odd and q is an even prime power, so q=2^a. There are at most O(log x) such primes up to x. For d≥3, q^(d−1)≤x gives q≤√x, and d≤log₂(x+1); counting all integer q overcounts the number of such primes by at most O(√x log x).

For completeness, an elementary lower bound π(x)≫x/log x follows from central binomial coefficients. For every prime p,
\[v_p\binom{2m}{m}=\sum_{a\ge1}\left(\lfloor2m/p^a\rfloor-2\lfloor m/p^a\rfloor\right)\le\lfloor\log_p(2m)\rfloor,\]
so binom(2m,m)≤(2m)^π(2m). The central binomial coefficient is at least 2^(2m)/(2m+1), yielding π(2m)≥(2m log 2−log(2m+1))/log(2m). Thus O(√x log x)/π(x)→0. Excluding 11,23 and finitely many primes below 419 changes neither infinitude nor this relative-density conclusion.

## 6. Actual finite controls and limits

`frontier-20261028-alternating-orbit-check.py`, SHA-256 `a0a0d50ab6cae51a21c060926000c95cec5b254ad7653ba23b4ce08960bc73a1`, 52 LF / 1310 bytes, ran at 18:39:52 PDT on 2026-10-28. It checked that 419 is prime and satisfies the repunit exclusion by exact finite search, and checked the binomial-divisor identities for j=1,…,6. Here the resulting d_j are 420,421,211,141,106,85. These sample checks do not prove the universal orbit induction, source classification, or asymptotic counting argument.

**Review-critical:** verify the source A_r hypothesis, base transitive-case Lagrange divisibility, precise setwise-stabilizer index and induction through all proper subgroups, the r-free hypothesis at every level, and the elementary prime count. No unrestricted target closure, source-proof replay, independent review, or historical holds modification is claimed.
