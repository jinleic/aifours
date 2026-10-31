# Independent same-harness Sun8 unitary source review

Observed native clock immediately before creation: **Wed Oct 28 18:34:05 PDT 2026**. This is a prewrite observation, not a claimed exact file-creation time. Review is of the frozen sources at the named theorem statements; it is not an independent proof of their imported classification, order/simplicity, or Zsigmondy theorem.

## Verdict and findings

**F=0, M=1, m=1** for this source review. The major is the **source-interface discrepancy S1**, not an exhibited counterexample to, or an uncovered step within, any of the stated candidate ranges. The minor is S2, a source-row transcription/qualification issue. The conditional reconstructions below avoid both affected small generic applications and the unused square branch. They are not a theorem-proof import audit, human review, formal proof, publication/priority finding, or parent acceptance.

| Frozen range | Review conclusion, conditioned on the exact qualified imports | Findings affecting the range |
|---|---|---|
| PSU3, every prime power q>=3 | Reconstructed, with separate q=3,5 support proofs; q=4 uses the imported statement whose source says the small case can be handled with Magma. | 0 F / 0 M / 0 m; q=4 method qualification remains. |
| Odd n=t^a>=5, t odd prime, f>=2 | Reconstructed for every p and f in this range. | 0 F / 0 M / 1 m (S2: source-row wording; no lost hypothesis in this application). |
| Same odd n, f=1 with composite 2n+1 | Reconstructed. | 0 F / 0 M / 1 m (S2). |
| Same odd n, f=1 with some primitive r>2n+1 or r^2 dividing p^n+1 | Reconstructed exactly under that existential condition; it does not assert the complementary prime-field cases. | 0 F / 0 M / 1 m (S2). |
| PSU5(2) | Reconstructed by order/support, not by the generic unique-overgroup row or the source's small-case Magma calculation. | 0 F / 0 M / 0 m. |
| Even n>=4, f>=2 | Reconstructed for every p and f in this range. | 0 F / 0 M / 0 m. |
| Even n>=4, f=1, composite 2n-1 | Reconstructed. | 0 F / 0 M / 0 m. |
| Even n>=4, f=1, excluding (6,2), with some primitive r>7 and r!=2n-1 or r^2 dividing p^(n-1)+1 | Reconstructed under the displayed existential condition; parentheses mean r>7 AND (r!=2n-1 OR the square divisibility). This does not assert its complement. | 0 F / 0 M / 0 m. |
| PSU4(2), PSU4(3) | Reconstructed by order/support, not by the generic unique-overgroup row or the source's small-case Magma calculation. | 0 F / 0 M / 0 m. |

**S1 — M, source interface, confined to excluded/unused branches.** In the literal [2024 source Table B](https://arxiv.org/html/2307.13976v2#S9.T5), the generic even row permits f=1 and `-r` a square modulo p; [Remark 9.2](https://arxiv.org/html/2307.13976v2#S9.Thmthm2) describes square modulo p without a displayed odd-p restriction. For T=U6(2), r=11, `ord_11(2)=10=2n-2`, beta is vacuous, and `-11=1 mod 2` is a square; the generic row as literally printed appears to give uniqueness. Yet [Proposition 6.4](https://arxiv.org/html/2307.13976v2#S6.Thmthm4), after naming U4(2), U4(3), U5(2), U6(2), reports that among those socles uniqueness occurs only for G=U5(2), r=11. U5(2), r=11 also satisfies the literal generic odd-row square condition while the proposition names its unique maximal overgroup as L2(11), not the generic extension-field type. This is an apparent inconsistency or missing implicit small-case qualification in the printed source interface; I do not resolve its editorial interpretation or assert that its full classification proof is false. The candidates explicitly use neither generic row for these affected groups nor the square-residue alternative. Do not extrapolate the literal generic rows to the source's four separately treated groups. This finding should accompany any parent disposition relying on the source.

**S2 — m, odd candidate Section 2.** The Table B odd-dimensional row is stated as beta AND `(f>1 OR (f=1 AND (|R|>r OR r!=2n+1 OR -r square mod p)))`. The candidate presents a sufficient subset with `|R|>r` or `r>2n+1` or the square condition, omitting the f>1 branch and replacing `!=` by `>`. This is not a verbatim transcription, although in the candidate's primitive-prime setting r>=2n+1, so `r!=2n+1` is equivalent to `r>2n+1`. Its selected f>=2 r has `r>2n+1`, and its prime-field arguments use only the displayed sufficient alternatives. This wording discrepancy does not invalidate those applications. The quadratic-residue branch is not an input to any reviewed proof.

## Frozen inputs and provenance

I read the manifest, then every line of its four complete inputs in its prescribed order, beginning with the additive q=4 qualification. Live SHA-256 values matched all manifest pins:

| Role | Filename | SHA-256 |
|---|---|---|
| Manifest | `manifest-v1.json` | `972b4cb761a5352a28db76e303a9ef450be2b71d5e28239e6886ea71d7c37f43` |
| Correction, read first | `frontier-20261028-psu3-q4-source-qualification-v1.json` | `cd1de7418b5c790d122eaed5360bda5aa3fff034c4f7b0f3a229131dd07d5d35` |
| PSU3 candidate | `frontier-20261028-psu3-all-fields-v1.md` | `c32a27c4e2c71cf76e3b129d37513dba9680da34cf4186a35d1d70126b7b8e7b` |
| Odd candidate | `frontier-20261028-unitary-odd-primepower-dimension-v1.md` | `252cdb33e748fc6d2cceec477df9fac8b4b3a15855bb91d25bfe6f17fa0b6424` |
| Even candidate | `frontier-20261028-unitary-even-dimension-v1.md` | `b397a601924663a029619737146087d985ff23d47851618d53e9f3dcac038f85` |

The first correction's q=4 source-method qualification is valid: [Proposition 6.3](https://arxiv.org/html/2307.13976v2#S6.Thmthm3) says q in {3,4,5} can be handled using Magma before assuming q>=7. No Magma computation was reproduced here. The candidate's separate q=3 and q=5 arguments do not use that branch.

I inspected the primary [Baumeister–Burness–Guralnick–Tong-Viet v2, arXiv:2307.13976](https://arxiv.org/html/2307.13976v2), including Theorem 2, Table B, Propositions 6.3–6.4, Remark 9.2 and Section 2.1. Its watermark identifies v2 dated 13 March 2024; the HTML reader reports its 2026 rendering date separately. Theorem 2 concerns an almost simple G with socle T, odd r and G/T an r-group. Here G=T=PSU is nonabelian simple, so G/T is trivial and R=R intersect T. Table `U_n(q)` names the projective simple group, and descriptions such as `GU_1(q^3)`, `GU_(n/t)(q^t)` and `GU_(n-1)(q) x GU_1(q)` are **types of maximal overgroups**, not claims that those unprojectivized matrix groups are literally subgroups of PSU or that their raw orders are indices. Only existence and uniqueness of an actual maximal subgroup M are needed below.

The exact cited [Korchmaros–Lia–Timpanella Section 3](https://arxiv.org/html/1902.10201v1#S3) states PSU3(q) has order `q^3(q^3+1)(q^2-1)/gcd(3,q+1)` and is simple for q>=3. The cited secondary [MathWorld order/simplicity reference](https://mathworld.wolfram.com/ProjectiveSpecialUnitaryGroup.html) states the general projective quotient, its center size `gcd(n,q+1)`, the product formula, and the exceptions PSU2(2), PSU2(3), PSU3(2). I checked those statements, not their proof ancestry.

## Source hypotheses and exception mapping

The relevant Table B rows, read with S1 and S2, are:

* U3(q), r=p odd: a Sylow p-subgroup has the unique maximal overgroup P1. U3(q), r=r6: beta(3,-1) and `f>1 OR (f=1 AND (|R|>r OR r>7))` give the extension-field-type overgroup. For (q,r)=(3,7), the source has a separate L2(7) row. The candidate never uses that row for its small q=3 proof.
* Odd U_n(q), n=t^a with t odd prime, r=r_(2n): the generic row and its exact f-dependent alternatives are as in S2. The explicitly listed (5,2,11) source row has L2(11) type; it is not treated here as an extension-field-type literal subgroup.
* Even U_n(q), n>=4, r=r_(2n-2): the generic row requires beta(n-1,-1) and `f>1 OR (f=1 AND (|R|>r OR r!=2n-1 OR -r square mod p))`. The reviewed use is restricted away from the four small socles and does not use the last alternative.

The source's **beta(m,-1)** quantifies over every odd prime k dividing f except k=r: `p^(mf/k) != -1 (mod r)`. It is not the alpha condition, which also tests k=2. In all f>=2 constructions below I check the stronger statement for every odd prime k|f, even one equal to r, although the source excludes it.

Proposition 6.4 expressly separates **U4(2), U4(3), U5(2), U6(2)** and reports Magma handling. The odd proof pays U5(2) independently; the even proof pays U4(2), U4(3) independently and does not settle U6(2). Their nonprime-field ranges have q>=4 and avoid all four. For prime-field generic ranges, U5(2) has only r=11 at exponent 10 and 11^2 does not divide 2^5+1; U6(2) is explicitly excluded. At U4(2), exponent 6 has no primitive divisor; at U4(3), the only primitive divisor is 7 and fails r>7. Thus none is silently passed through a generic branch. These statements concern the candidate scopes, not an independent replay of the source's Magma list.

## Reconstruction: primitive primes, beta, centers and field ranges

Use the source's stated Zsigmondy theorem as an import: a primitive divisor of p^d-1 exists for d>=2 except (p,d)=(2,6), or d=2 with p Mersenne. For such r, `ord_r(p)=d` and r=1 mod d. In every use below d is even and at least 6, so r is odd.

Let m=n for the PSU3 and odd n cases, and m=n-1 for even n. For f>=2 take d=2mf and choose r with `ord_r(p)=2mf`. The exception (2,6) is impossible: m>=3 and f>=2; d=2 is also impossible. Then

`ord_r(q) = ord_r(p^f) = 2m`, `q^m = -1 (mod r)`, and `r>=2mf+1>7`.

For odd n>=5, f>=2 even gives r>=4n+1>2n+1; for n=3 r>=13; for even n>=4 r>=4(n-1)+1>7. If k is an odd prime divisor of f and `p^(mf/k)=-1 mod r`, squaring gives `p^(2mf/k)=1` at a strictly smaller positive exponent than 2mf, impossible. Hence all beta tests, including every prime in the source quantifier, pass.

In `|PSU_n(q)| = q^(n(n-1)/2) product_{j=2}^n (q^j-(-1)^j)/gcd(n,q+1)`, m is odd and j=m is an actual factor `q^m+1`. In the relevant ranges r>n, so r cannot be removed by the full projective denominator. For the squared alternative the denominator is also r-free: `r^2 | q^m+1` forces `r^2 | |PSU_n(q)|` and hence `|R|>r`. In fact for these primitive orders, no other j<=n factor can contain r: an even j would need 2m|j, and an odd j would need j=m. Thus the r-adic contribution is exactly that of the one factor; this stronger observation is not needed to infer sufficiency.

For PSU3 at f=1, p>=11 uses the defining-characteristic p-row and p>7. For p=7 choose r=43, since 7^3+1=344=8*43 and ord_43(7)=6; beta is vacuous and 43>7. The q=3,5 endpoints are handled below; q=2 is excluded from the PSU3 claim.

For odd n=t^a>=5 at f=1, d=2n>=10, so no Zsigmondy exception occurs. Every primitive r satisfies r>=2n+1>7 and beta is vacuous. If 2n+1 is composite, r cannot equal it; otherwise the claimed range requires an actual primitive r with r>2n+1 or the above r-squared divisibility. At (n,p)=(5,2), `2^10-1=3*11*31`, ord_11(2)=10, ord_31(2)=5, and 11^2 does not divide 33. It is not an accidental application of either generic sufficient condition.

For even n>=4 at f=1, d=2(n-1); the only Zsigmondy exception is (n,p)=(4,2). A primitive r has r>=2n-1 and beta is vacuous. If 2n-1 is composite, n>=6, the exception is absent and the prime r is strictly larger than 2n-1 and 7; (6,2) is not in this composite range. Otherwise the displayed conditional range requires r>7 and either inequality with the threshold or the explicit square divisibility, with (6,2) excluded. At (4,3), `3^6-1=2^3*7*13`, ord_7(3)=6 and ord_13(3)=3, so its only primitive r is 7 and cannot satisfy r>7. Nothing proves the excluded residual prime fields here.

## Reconstruction: actual cosets, indices and small support

A family of at least two disjoint cosets cannot contain G itself; all its subgroups are proper. If `[G:H]=a` and `[G:K]=b` are coprime, the diagonal map `G/(H intersect K) -> G/H x G/K`, `g(H intersect K) -> (gH,gK)`, is injective. Its domain size is divisible by both a and b and is at most ab; coprimality therefore makes it exactly ab, so the map is onto and every actual left H-coset meets every actual left K-coset. This remains true for nonnormal H,K.

For the unique-Sylow caller, suppose r>7 and M is the unique maximal proper overgroup of a fixed Sylow r-subgroup R. In a hypothetical eight-coset counterexample, at most one index is divisible by r, since two would have gcd>=r. Each of at least seven other subgroups has r-free index, hence contains a Sylow r-subgroup of G. Sylow conjugacy sends that subgroup to R, and a maximal overgroup of the conjugate must be M. Therefore the original subgroup lies in some conjugate of M, and its original index is divisible by d=[G:M]. The conjugates need not coincide. For nonabelian simple G, a proper subgroup has trivial core. If d<=7 its faithful action embeds G in S_d, impossible when r>7 divides |G|. Thus d>=8 and two original indices share d, contradiction. For PSU3(q), q>=3, the independent alternate bound |G|>7! follows from 6048 at q=3 and at least 20800 for q>=4, so every proper index is >=8 even at the support endpoints.

The complete small-support argument is as follows. Suppose the indices are >=8, pairwise noncoprime and have pairwise gcd<=7. Among those supported on {2,3,5}, there are at most four:

1. If a pure 2-power occurs, all others are even; there is at most one pure 2-power, at most two with exact support {2,3}, and at most one divisible by 10. An exact {2,3} number >=8 is divisible by 12 or 18; two in the same category would have gcd at least 12 or 18. Total <=4.
2. If a pure 3-power occurs, all others are divisible by 3; at most one is pure 3-power, at most two have exact support {2,3}, and at most one is divisible by 15. Total <=4.
3. If a pure 5-power occurs, all others contain 5; at most one is pure, at most one is even, and at most one is divisible by 3. Total <=3.
4. With no singleton support, {2,3} contributes at most two by the 12/18 argument; {2,5} and {3,5} contribute at most one each; a triple-support number contributes at most one and cannot coexist with either of those last two types because their gcd is at least 10 or 15. Total <=4.

If a further prime 7 occurs only to exponent one in |G| and no index is 7, there are at most three 7-divisible indices: after writing them 7a_i, each a_i>1 has support inside {2,3,5}, and pairwise gcd<=7 implies the a_i are pairwise coprime, so each needs a different one of those three primes. Thus there are at most 3+4=7 indices. If the further prime is 11, at most one index is divisible by 11 and the total is at most 1+4=5; no exponent bound on 11 is needed.

The imported order formula gives the following exact factorizations. The simplicity import and the core argument give index>=8 in each case: PSU3(3) and PSU3(5) have order greater than 7!, as do PSU4(2), PSU4(3); for PSU5(2), the prime 11 already excludes an index <=7.

* `|PSU3(3)|=6048=2^5*3^3*7` and `|PSU3(5)|=126000=2^4*3^2*5^3*7`: the 7-adic support bound applies.
* `|PSU4(2)|=25920=2^6*3^4*5`: the {2,3,5} bound applies; `|PSU4(3)|=3265920=2^7*3^6*5*7` uses the 7-adic bound.
* `|PSU5(2)|=13685760=2^10*3^5*5*11`: the 11-adic bound applies.

These are arguments about actual subgroup indices of the named simple groups, with an arithmetic overapproximation only in the support step; the support bound is not inferred from a numerical search.

## New independent bounded controls

Executed `python3 -B controls-v1.py` from this review directory, with standard-library exact integers and no author-code replay. The retained machine output is `controls-result-v1.json`, SHA-256 `173fda777183a960f03d6ef32990ea227ddf66515d461682bc36df615e0f5f0a`; the script is `controls-v1.py`, SHA-256 `68a95dba84f715afb9dd4b5af77104a72648a55d7d2a712de48fe9ad6ec85407`. The recorded execution began `2026-10-28T18:33:20-07:00`, ended `2026-10-28T18:33:21-07:00`, and exited successfully. A prior execution of the same control code also completed at 18:32:39–18:32:40 PDT; the retained JSON is the later run's actual stdout.

* The five displayed endpoint formula orders were reproduced. An independent exhaustive maximum-clique search on all distinct order divisors >=8, with edges exactly when gcd is 2..7, gave `(divisors,max clique)` of `(42,4)`, `(113,5)`, `(64,4)`, `(217,5)`, `(258,5)` in the order listed above. These are numerical overapproximations, not assertions that witnesses are actual subgroup indices or disjoint cosets.
* For n in {3,4,5,6,7,8,9,10}, p in {2,3,5}, f in {2,3}, a prime search through 300000 returned 44 checked witnesses and 4 `UNKNOWN_AT_CAP` cases: (n,p,f)=(7,5,2),(8,5,2),(9,3,2),(10,3,2). Each found witness was checked by exact primality, base and q orders, beta, group-order divisibility, and the squared-factor equivalence. A cap miss is not a counterexample to Zsigmondy.
* At f=1, n in the same set and p in {2,3,5,7,11,233}, the controls returned 40 checked witnesses, six `UNKNOWN_AT_CAP`, and two `(p,d)=(2,6)` Zsigmondy exceptions (n=3 and n=4). n=3,p=2 is outside the simple PSU3 claim. All 48 individual records are in the retained stdout; the test does not claim that its least found primitive prime is the only primitive prime.
* Fault controls detected omitting the center at (4,3): 13063680 instead of 3265920; assuming ord_r(q)=6 alone implies beta fails at (p,f,m,r,k)=(7,5,3,43,5), where p^(mf/k)=42=-1 mod 43; and assuming r|p^m+1 implies r^2 divides it fails at (2,5,11), since 2^5+1=33. A positive squared example is p=233,m=5,r=11, with 233^5+1=686719856394 divisible by 121. The S1 small-source arithmetic is also explicitly checked. A separate S3 control enumerated all six pairs of left cosets of subgroups of coprime indices 2 and 3, one subgroup nonnormal, and found all pairs intersect.

These controls check the arithmetic and the control code's bounded numerical claims; they do not establish infinite primitive-prime existence, group simplicity, the source classification, or actual-coset configurations in the unitary groups.

## Remaining dependencies and exclusions

The original proof DAGs of the unique-Sylow classification, Zsigmondy's theorem, and unitary order/simplicity remain unverified. The q=4 source-Magma ancestry remains unreproduced. In particular, this review does not resolve S1 or authorize unqualified use of the generic source rows on any small exceptional socle. It does not prove all unitary groups, the unlisted prime-field cases, arbitrary Sun8, priority or novelty, and it is not an independent-model, human, formal/kernel or publication certification.
