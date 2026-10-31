# Sun8 for the finite simple groups E8(q), every finite field

**NEW FAMILY PROOF CANDIDATE at NAMED EXTERNAL INPUTS — WRITTEN plus bounded exact polynomial/arithmetic checks; not reviewed/adopted/formally verified or novelty-cleared.** Actual native prewrite clock **Wed Oct 28 18:08:36 PDT 2026**. This is an ALL-q actual-coset theorem conditional on a precise published E8 Sylow-overgroup classification; it is NOT a proof of unrestricted Sun8 or of that classification.

## 1. Exact theorem and source cuts

For a group X, `Sun_8(X)` means every eight pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups have a pair of original indices with gcd>=8.

**Theorem.** For EVERY prime p and integer f>=1, put q=p^f. At the named E8 order/simplicity, unique-Sylow-overgroup and primitive-prime inputs below, the finite simple group `E8(q)` satisfies Sun8.

This theorem uses NO Sun7, NC7, P7, group-covering or arbitrary normal-extension assumption. The full input cut is:

1. **E8 order and simplicity.** The relevant source treats T=E8(q) as a finite nonabelian simple group and explicitly states

       |T|=q^120 (q²−1)(q⁸−1)(q¹²−1)(q¹⁴−1)
                     (q¹⁸−1)(q²⁰−1)(q²⁴−1)(q³⁰−1).

2. **Exact unique-maximal-Sylow statement.** In [Baumeister–Burness–Guralnick–Tong-Viet, *On the maximal overgroups of Sylow subgroups of finite groups*, arXiv:2307.13976v2](https://arxiv.org/html/2307.13976v2), Theorem2/Table C and the proof of Proposition7.8, take G=T=E8(q), r an odd primitive prime divisor of `q³⁰−1`, and assume `alpha(30,1)`. The cited row gives a UNIQUE maximal proper overgroup of the Sylow r-subgroup when either `r>61` OR `|R|>r`. Other exceptional alternatives in the table are not needed here. Remark9.2 defines alpha(30,1) as

       (q^(1/k))³⁰ != 1 (mod r)

   for EVERY prime k dividing f with k!=r. I read the displayed E8 order, E8 proof/row and alpha definition, but did not reprove the external maximal-subgroup classification, the external paper's dependencies or the simplicity theorem: **NR-E8-MAXIMAL-CLASSIFICATION / NR-E8-SIMPLICITY-ORDER-PROOFS** remain. This is a statement-level input, not a newly certified classification or a prior held E8 proof.
3. **Zsigmondy.** For any prime p and d>=2, a prime divisor of `p^d−1` not dividing `p^j−1` for 1<=j<d exists except `(p,d)=(2,6)` and d=2 with p a Mersenne prime. The same 2024 source states the theorem in §2.1. It is used only with d=30f>=90, so no exception applies. **NR-ZSIGMONDY-PROOF** remains.

The written elementary polynomial arguments in Sections4–6 handle f=1,2 rather than assuming a primitive prime >61 exists automatically. The source's other r=61 exception is not silently used.

## 2. Actual unique-Sylow-overgroup caller

Let G be any finite nonabelian simple group, let r>7 divide |G|, and suppose a Sylow r-subgroup has a UNIQUE maximal proper overgroup M. Then G has Sun8.

If eight actual pairwise-disjoint cosets had pairwise original-index gcd<=7, at most one index could be divisible by r. Each of the other at least seven actual subgroups H has r-free index and hence contains a Sylow r-subgroup of G. Sylow conjugacy takes it to the fixed Sylow r-subgroup; a maximal proper overgroup of the conjugate H must be M by uniqueness. Thus each actual H lies in some conjugate of M and `[G:M]` divides its original index.

The actual simple-group coset action on G/M is faithful. If `[G:M]<=7`, it embeds G in S7, but r>7 divides |G| and not 7!, impossible. Hence `[G:M]>=8`. Any two of the seven r-free original indices share that divisor, contradiction. This pays the original left-coset caller; different original H may lie in DIFFERENT conjugates of M. No Sun7 or group-order threshold is assumed. □

## 3. Two elementary integer polynomials

Put

    F(x)=x⁸+x⁷−x⁵−x⁴−x³+x+1.

Elementary polynomial multiplication gives

    x^15+1=(x+1)(x²−x+1)(x⁴−x³+x²−x+1) F(x).              (3.1)

The explicit factor is the 30th cyclotomic polynomial, but only the displayed factorization is needed below. For every INTEGER x, direct reduction modulo2,3,5 gives

    gcd(F(x),30)=1.                                             (3.2)

For example, x≡0,±1 mod3 gives F≡1; if 5∤x use x⁴≡1 to cancel the x³ and x terms and get F≡1 mod5, and x≡0 gives1. The parity check is immediate from x=0 or1 modulo2. Hence the same holds for F(x²), so `gcd(F(x²),60)=1`.

**Primitive-factor lemma.** If a prime r divides F(x), then `ord_r(x)=30`. Indeed r∤30 by (3.2), x is nonzero mod r because F(0)=1, and (3.1) gives x^15≡−1. Its order divides30 but not15, so it is one of2,6,10,30. The derivative of X^15+1 is `15 X^14`, nonzero at x modulo r; hence the reduction of X^15+1 is square-free at this root. The four polynomial factors in (3.1) cannot share that root. Orders2,6,10 respectively make x a root of the first, second, or third factor, so none can occur. Thus the order is30.

If r divides F(x²), applying the same lemma to x² gives `ord_r(x²)=30`. The order of x must then be60: an odd order cannot have square order30, while an even order d has square order d/2. This argument uses only elementary multiplicative orders and the explicit separable factorization, not an unproved claim that every cyclotomic factor is primitive.

Finally,

    F(2)=331 >61, and 331 is prime;
    F(x)>31*61=1891 for every integer x>=3.                     (3.3)

For the bound, `F(x)>x⁸−3x⁵=x⁵(x³−3)>=3⁵(27−3)=5832>1891`. Primality of331 is verified by trial divisors 2,3,5,7,11,13,17. These are universal written inequalities plus one exact endpoint, not a guessed numerical threshold.

## 4. Every prime field f=1

Let q=p be prime. By (3.2) every prime divisor of F(p) is prime to30; by Section3 it has order30 for p and is therefore congruent to1 modulo30. The only possibilities at most61 are31 and61.

If p=2, F(2)=331 supplies a primitive r=331>61. If p>=3, F(p)>31*61. If F(p) has a prime divisor r>61, use it. Otherwise all its prime factors are31 and/or61; the strict product bound forces at least one to occur with exponent at least2. Choose that r, so `r² | F(p) | p³⁰−1`. Therefore either r>61 or the actual Sylow r-subgroup has order>r. In every case `ord_r(q)=30`; alpha(30,1) is vacuous when f=1. The exact E8 source row supplies a unique maximal Sylow r-overgroup. The E8 order has p³⁰−1 as a factor, so this r divides |E8(p)|. Section2 proves Sun8(E8(p)).

No statement that every primitive divisor is >61 is made. The square-Sylow alternative is used EXACTLY when needed and is not replaced by a guessed prime search.

## 5. Every degree-two field f=2

Let q=p² and consider F(p²). Its prime divisors r satisfy `ord_r(p)=60` by Section3, hence `ord_r(q)=30` and `r≡1 (mod60)`. Thus r>=61. Since p²>=4, (3.3) gives `F(p²)>1891>61`. If it has a prime factor r>61, choose it. Otherwise all its prime factors equal61; the strict inequality then forces `61² | F(p²)`, so the actual Sylow61 subgroup has order>61 because `F(p²)|p^30+1|p^60−1=q^30−1`, a factor of the E8 group order.

The source alpha(30,1) condition needs only k=2, and

    (q^(1/2))³⁰ = p³⁰ != 1 (mod r),

because ord_r(p)=60. Thus the exact source row yields a unique maximal r-overgroup and Section2 gives Sun8(E8(p²)) for EVERY prime p. The potentially troublesome r=61, f=2, order-r exception is NOT assumed away; when r=61 is the only prime, the proved square gives the separate `|R|>r` alternative.

## 6. Every higher field degree f>=3

Zsigmondy gives a prime r with `ord_r(p)=30f`. Hence `r≡1 (mod30f)`, so `r>=30f+1>=91>61`. For q=p^f, `ord_r(q)=30`, so r divides q³⁰−1 and the named E8 order.

For EVERY prime k dividing f,

    (q^(1/k))³⁰ = p^(30f/k) != 1 (mod r),

since the exponent is strictly smaller than ord_r(p). Thus alpha(30,1) holds, including all k omitted by the source's k!=r convention. The source row's r>61 condition supplies unique maximal overgroup, and Section2 proves Sun8(E8(q)). No finite sample is used for the universal f argument.

Sections4–6 exhaust ALL prime powers q; this proves the theorem at precisely the named inputs. □

## 7. Bounded exact controls

Executed `/opt/homebrew/bin/python3 frontier-20261028-e8-cyclotomic-check.py` with a20-second deadline. Source SHA256 `27bacf35f10570654c54631895acdf1f8c52022a2d25bff3582d0c9bcdfd4c54`. It verifies the polynomial identity (3.1) by exact integer-coefficient multiplication; independently constructs F(x²) and checks its corresponding x³⁰+1 factorization; checks gcd(F(x),30)=gcd(F(x²),60)=1 for integers x=2,...,100; and factors seven bounded prime-field/degree-two values with exact trial division. Actual output:

```text
Phi30_Phi60_factorizations: PASS
gcd_controls_x2_to_100: PASS
f=1, p=2, Phi=331, factors=[(331, 1)], source_candidate=(331, 1)
f=1, p=3, Phi=8401, factors=[(31, 1), (271, 1)], source_candidate=(271, 1)
f=1, p=5, Phi=464881, factors=[(61, 1), (7621, 1)], source_candidate=(7621, 1)
f=1, p=7, Phi=6568801, factors=[(6568801, 1)], source_candidate=(6568801, 1)
f=2, p=2, Phi=80581, factors=[(61, 1), (1321, 1)], source_candidate=(1321, 1)
f=2, p=3, Phi=47763361, factors=[(47763361, 1)], source_candidate=(47763361, 1)
f=2, p=5, Phi=158681234401, factors=[(2281, 1), (69566521, 1)], source_candidate=(2281, 1)
PASS: exact bounded E8 primitive-order and source-threshold controls
Wed Oct 28 18:07:51 PDT 2026
```

The finite modular controls do NOT prove the all-integer congruences, which were derived symbolically in Section3; nor do they check any actual E8 subgroup, Sun7, the classification or novelty. The family proof's f>=3 primitive-prime existence is the explicit Zsigmondy import, not a bound from these tests.

## 8. Prior scope and remaining obligations

The previous round final math-6 summary states its later E8 leads were not generally adopted and retained individual unreviewed/held statuses. This independently written source-based candidate does NOT consume or retrospectively validate a held E8 result. Earlier exposure is not erased; the previously recorded R8/normal-section rediscovery correction remains mandatory. Targeted prior-parent searching did not find an adopted all-q E8 gate, but the repository/literature priority screen is not exhaustive; no novelty or firstness is claimed.

If reviewed, the result excludes the finite simple E8 family only. It does not exclude all finite simple direct-P7 factors or settle unrestricted Sun8, E6/E7/large-Ree or other families. A reviewer must check the ENTIRE E8 source row/alpha scope, prime-field and f=2 cyclotomic primitive-factor arguments, all exceptional alternatives, actual Sylow/coset caller and the exact external imports before any adoption. Human/kernel/independent-family verification, full source theorem proofs and publication/priority remain unpaid.
