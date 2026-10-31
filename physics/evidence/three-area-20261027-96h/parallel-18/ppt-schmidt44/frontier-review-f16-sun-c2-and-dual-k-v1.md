# f16 — index-two and dual normal-fibre Sun transfers

Reviewer **PhysicsPPT44-2**. Actual native clock immediately before creation: **Wed Oct 28 17:17:21 PDT 2026**.

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT STATED CONDITIONAL SCOPES — 0 FATAL / 0 MAJOR / 0 MINOR.** The index-two theorem uses `Sun8(N)` and `Sun7(G)`; the all-k dual theorem uses the distinct kernel pair-gap hypothesis and `Sun_k(G/N)`. The solvable-quotient and perfect-minimum-counterexample consequences additionally use the stated arbitrary-group Sun7 import and the prime-transfer results reconstructed below. **Sun7 is not proved or independently authenticated here.** This is same-harness written reasoning plus bounded independent checks, not unrestricted Sun8, formal/kernel, human, configured-family, novelty or publication acceptance.

## 1. Exact inputs, verification boundary and exposure

The complete frozen assignment `f16-sun-c2-and-dual-k/assignment-v1.json` has SHA256 `855a0903dd3eedfac635c88b61111ab76d7340de550dbfdeb7bc320df23efa09`.

- **C2:** `frontier-20261028-c2-normal-transfer-v1.md`, 93 LF, SHA256 `3bda86f96f33089da3f0c7ab5d6550e21d018cfc78ece70240a5c4fc54dbb063`, read completely.
- **Dual:** `frontier-20261028-dual-k-fibre-transfer-v1.md`, 91 LF, SHA256 `1c4631d57fb6c118d1d1859f9cfb33fae521433a65cfea74e4a2f41de14d1b67`, read completely.
- Used prime-transfer dependencies: `prerequisite-derivation-v2.md`, SHA256 `8d2411c012234bc34ded76f5904beb8994c01ddde22bd76c177734fdc06b3c53`, operative LF1–95; `prerequisite-derivation-v3.md`, SHA256 `0bfbb17a4d19941d7de4e856dcf7a5de58b36de6f81d63a41b2f181e5b01329b`, read completely. The index-three candidate SHA256 `5c9099385c75e451a60f8bebe1c133dc1da07285e504aa822799e91027e70668` was completely reconstructed in my immediately preceding f1 review, `frontier-review-f1-sun-c3-transfer-v1.md`, SHA256 `b6906074a12a7c4c6bd9cf011ea5ade1dda529c68f47880676f703762a343fa0`. The registered actual-left-coset definitions were read.

I have earlier Sun-coset familiarity and authored the cited f1 review; this is not blind, independent-model-family or clean-cognition review. No quarantined outcome or author's program result is used as an accepted premise. The shared actual-fibre facts are independently rederived in §2. Two separately implemented checks and their actual outputs are recorded in §8. No author contact or nested agent was used.

## 2. Actual quotient and fibre facts

For any group X, `Sun_k(X)` means every k **actual pairwise-disjoint left cosets** of finite-index subgroups has a pair of subgroup indices whose gcd is at least k. It is vacuous if no k such cosets exist. Groups may be infinite; individual subgroups need not be normal or distinct, and no cover or split extension is assumed.

For N normal in G, write `Q=G/N`, `C_i=π(g_i)π(U_i)`, `a_i=[Q:π(U_i)]`, `b_i=[N:N∩U_i]` and `n_i=[G:U_i]`. `NU_i` is a subgroup, and the natural coset bijection `N/(N∩U_i)→NU_i/U_i` yields `n_i=a_i b_i`. Both a_i,b_i are finite.

When actual quotient cosets C_i,C_j meet in q, fix t with π(t)=q. For each nonempty intersection choose `t x_i∈g_iU_i∩tN`, with x_i∈N. Then `t^(-1)(g_iU_i∩tN)=x_i(N∩U_i)`. The fibres are actual left N-cosets of indices b_i and remain disjoint.

Two disjoint finite-index left cosets in any group have noncoprime subgroup indices. If indices r,s were coprime, the injection `X/(H∩K)→X/H×X/K` would have domain size both divisible by r,s and at most rs; its size must be rs, making it onto. In particular the two specified cosets would have a common representative. This uses no subgroup normality. Thus every pair of original cosets whose quotient images meet has `gcd(b_i,b_j)≥2`.

If all eight quotient images share a point and `Sun8(N)` holds, the eight disjoint actual fibres give a pair with kernel gcd≥8, which divides the corresponding original gcd. For a prime quotient p, every image is either full or a singleton. With zero or one singleton all eight share a point, so an eight-counterconfiguration has at least two singleton/proper-image labels. Under original gcd≤7, any two such labels satisfy `p gcd(b_i,b_j)≤7`.

## 3. C2: every actual eight-coset counterconfiguration is impossible

Assume `Sun8(N)` and `Sun7(G)`, `[G:N]=2`, and eight actual disjoint original cosets have pairwise original gcd≤7. The fibre facts above imply at least two proper labels and `gcd(b_i,b_j)≤3` for any two of them.

Apply `Sun7(G)` to every seven-subfamily. Each has a gcd exactly 7 pair, so at least three of the eight original indices are divisible by 7; otherwise delete a seven-divisible label if any and leave at most one such index in seven. At most one proper index is seven-divisible because two would share 14. Hence at least two full indices are seven-divisible, and every pair of these has gcd exactly 7.

### 3.1 No proper seven-label

All at least three seven-divisible labels are full; at most one of them is even, so choose two odd ones V,W. For **every** proper A, b_A is not divisible by 7, and both full image cosets meet A's actual image. The nontrivial gcds `gcd(b_A,n_V)`, `gcd(b_A,n_W)` are each ≤7. Their possible common prime factors are 3 or 5, since V,W are odd and b_A lacks 7. Their primes must differ because `gcd(n_V,n_W)=7`. Therefore 15 divides **every** proper b_A. Two proper labels then have gcd at least 15, contradicting their bound ≤3.

### 3.2 Exactly one proper seven-label

Let it be A. Since `14|n_A`, all full seven-indices are odd. Choose two V,W. For any other proper B, its b_B is not divisible by 7; its fibres meet V and W, which have gcd 7. The two nontrivial gcds are ≤7 and must use distinct primes 3 and 5. Relabel so `3|n_V`, `5|n_W` and `15|b_B`.

A second other proper B' would likewise have `15|b_B'`, violating the proper/proper gcd≤3. Thus A,B are the only two proper labels and the other six are full. Choose a third full F different from V,W.

If `7|n_F`, then F is odd (its index would otherwise share 14 with n_A), not divisible by 3 (it would share 21 with V), and not divisible by 5 (it would share 35 with W). As b_B is not divisible by 7, no shared prime ≤7 is available for their actual meeting fibres, while a shared prime >7 violates the original gcd bound. Therefore `7∤n_F`.

F and V are full, so their b-indices coincide with their original indices and meet in every quotient fibre. Since V is odd, F is not divisible by 7, and 5∤n_V because 5|n_W and `gcd(n_V,n_W)=7`, the nontrivial common prime ≤7 must be 3; hence `3|n_F`. Likewise F and W can share only 5, giving `5|n_F`. Thus `15|n_F` and also `15|n_B=2b_B`, contradicting gcd≤7.

The common-fibre, no-proper-seven and one-proper-seven cases exhaust all configurations. This establishes `Sun8(N) ∧ Sun7(G) ⇒ Sun8(G)` at index two, with actual fibres and no stronger hidden premise.

## 4. Dual pair-gap theorem for every k≥2

Define pair-gap k for N to mean every **two** disjoint actual finite-index left N-cosets have indices with gcd≥k. Suppose pair-gap k and `Sun_k(Q)` hold, while k original G-cosets form a counterconfiguration with every original gcd<k.

If any two actual quotient cosets C_i,C_j meet, the same-fibre construction gives two actual disjoint N-cosets; pair-gap k forces `gcd(b_i,b_j)≥k`, hence `gcd(n_i,n_j)≥k`, contradiction. The k quotient cosets are therefore pairwise disjoint. Apply `Sun_k(Q)` to these very cosets: their actual indices a_i,a_j have gcd≥k, and each a divides its original index, again a contradiction. This works for arbitrary k≥2 and arbitrary normal N, including infinite quotient/kernel and trivial/vacuous cases.

For the index-spectrum condition, two disjoint N-cosets have a nontrivial index gcd by §2. If every pair of finite-index subgroup indices has gcd either 1 or ≥k, their gcd is ≥k, so pair-gap follows. If all prime divisors of all finite subgroup indices are ≥k, every nontrivial gcd has such a divisor, giving the stated stronger sufficient condition. For k=8 and finite p-group N with p≥11, all subgroup indices are p-powers; the trivial kernel is vacuous.

For a **single actual counterconfiguration**, it suffices that none of its actual b_i,b_j gcds belongs to `[2,k−1]`: meeting quotient images would produce nontrivial gcd≥k, contrary to the original bound. This is not a free-fibre construction or an implication from `Sun_k(N)` alone.

The candidate's no-seven-index observation is also conditional and correct: under Sun7(X), any hypothetical eight-counterconfiguration has a seven-subfamily whose pair gcd is exactly 7, forcing two indices divisible by 7. Thus the absence of any finite subgroup index divisible by 7 excludes such a configuration. For a finite group of order not divisible by 7, Lagrange gives the index premise. It does not prove the imported Sun7 property.

## 5. The previously named prime-transfer dependencies

The solvable-quotient caller genuinely needs each prime in a composition series. I checked the actual dependencies rather than treating their parent labels as proof.

### p>7

Under `Sun8(N)`, suppose a counterconfiguration has quotient indices a_i. For a prime-order quotient p>7 each a_i is 1 or p; two p-indices would make the original gcd≥p>7. Hence at most one is p and all eight actual images share a point, contradicting Sun8(N). More generally the v2 `(R7)` statement follows because original gcd≤7 makes the quotient indices pairwise coprime; the diagonal coset map into their Cartesian product is injective, its index is divisible by their pairwise-coprime sizes and at most their product, hence is onto. The actual eight quotient cosets have a common point. This argument does not need Sun7.

### p=5 or 7

At least two proper labels exist. Their b-indices are pairwise coprime because `p gcd(b_i,b_j)≤7`. If two had the same quotient point, their disjoint N-fibres would have coprime indices, impossible. Thus their quotient points are distinct, m≤p<8 and at least one full label exists. A full original index cannot be divisible by p: if `n_j=pc`, choose one of the at least two pairwise-coprime proper b_i with p∤b_i; the original bound forces `gcd(b_i,c)=1`, so the actual meeting-fibre gcd would be one.

For p=7, all at least three seven-divisible labels are proper. Each proper b_i shares a nontrivial gcd≤7 with any full index n_j; those gcds are pairwise coprime as i varies and have prime factors only among 2,3,5. Thus m=3 and every full n_j is divisible by 2·3·5. There are five full labels, so two share a divisor >7, contradiction.

For p=5, at most one proper index is seven-divisible, so there are at least two full seven-indices. Full indices are prime to 5. Their pairwise-coprime nontrivial common divisors with proper b-indices can use only 2,3,7, hence m≤3. If m=3, each full seven-index contains 2·3·7, and two share a divisor >7. Thus m=2. If neither proper b is divisible by 7, both coprime meeting divisors for each of the two full seven-indices use distinct primes 2 and 3, so those two full indices share 2·3·7, impossible. Exactly one proper b is seven-divisible. Its other proper b, call it b₂, must meet each full seven-index in 2 or 3. Two full seven-indices cannot share either prime, so there are exactly two, one uses 2 and the other 3, and 6|b₂. The seven-divisible proper b₁ is therefore coprime to 2,3. Among the six full labels select another, not seven-divisible; it is also prime to 5, so no prime ≤7 can witness its required nontrivial fibre gcd with b₁. Contradiction.

Both p=5/7 proofs use Sun7 only through the three-seven-label deduction; they retain Sun8(N) and actual quotient fibres.

### p=3

My cited f1 review gives the full actual-fibre proof, including all prime and unique-proper-seven cases. In brief, two proper labels have kernel gcd≤2. If neither is seven-divisible, one odd full seven-label must meet them using distinct primes 3 and 5, forcing an original gcd divisible by 15. If one proper label A is seven-divisible, every full seven-label avoids 3; an odd one forces every other proper b to contain 5, so there is exactly one B. A second full seven-label forces b_B even; b_A is odd and then coprime to b_B. A third full F cannot be seven-divisible; its fibres against A and B force 3|n_F, then force n_F even and not divisible by 5, while its fibre against the odd, 3-free full seven-label would have no common prime ≤7. Every step is reconstructed in the full pinned f1 return; no numerical-signature result is substituted.

## 6. Conditional solvable quotients and perfect minimum counterexamples

Assume the arbitrary-group Sun7 statement and the just-reconstructed prime transfers. For a finite solvable Q=G/N, refine each finite abelian factor of a derived series by a chain of cyclic prime-order factors: choose a nonidentity element, take an appropriate power of prime order, quotient by its cyclic subgroup and induct. Every step is normal in the next inside the abelian factor. Pull these chains back through successive derived quotients, then from Q to G. Starting with `Sun8(N)`, apply the applicable p=2,3,5,7 or p>7 transfer to each actual index-p normal step. Universal Sun7 supplies precisely the intermediate-group hypotheses where used. Thus Sun8 passes from N to G for finite solvable G/N under these explicit imports.

For N=1, Sun8(N) is vacuous, so every finite solvable group satisfies Sun8 under the same imports. For an arbitrary infinite solvable G with a hypothetical eight-coset counterconfiguration, intersect the eight cores `core_G(U_i)`. Each has finite index as the kernel of the action on finite G/U_i. Their intersection K is finite-index normal and lies in every U_i. The images of the eight **same** cosets in G/K are pairwise disjoint and preserve their indices: each original coset is exactly the inverse image of its image. The finite quotient is solvable, contradicting the conditional finite result.

The same finite-core reduction gives a finite counterexample whenever any original counterexample exists. If a finite counterexample of minimum positive order had nontrivial abelianization, its commutator subgroup would be a proper smaller group and hence satisfy Sun8 by minimality. Its quotient is nontrivial finite abelian, hence solvable, so the conditional transfer would force Sun8 of the original group, contradiction. Therefore such a minimum counterexample is perfect. This does not prove it simple or rule it out; all stated Sun7 and prime-transfer qualifications persist.

## 7. Independent C2 support check

I separately wrote `frontier-20261028-review-f16-sun-c2-check.py`, SHA256 `489d097cdce12cdc8ca5cb60e87dd1c6d8df8a8c5ba30072f8fdb1d5b274bb44`, and ran

`PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 frontier-20261028-review-f16-sun-c2-check.py`.

It retains the squarefree supports of 2,3,5,7 and checks original gcd≤7 plus actual-meeting-fibre noncoprimality whenever one label is full. For no proper seven-label it tests two non-seven proper labels and two odd full seven-labels; for the one-proper-seven case it tests A,B,V,W,F as derived in §3.2. This deliberately omits larger primes/valuations and actual-group compatibility, so it is a necessary-condition overapproximation, not a coset existence search. Actual output:

```text
no_proper_7: domain_sizes=[8,8,4,4], partial_counts=[1,8,45,20,0], terminal_models=0
one_proper_7: domain_sizes=[8,8,4,4,8], partial_counts=[1,8,45,35,8,0], terminal_models=0
```

Any actual bounded original gcd is divisible by every shared retained prime; every nontrivial shared fibre gcd must have a shared prime ≤7, or else already violate the original bound. Therefore no actual necessary support is removed. The zero counts agree with, but do not replace, the all-variable fibre proof and do not prove Sun7.

## 8. Independent actual D22 and A5 checks

I separately wrote `frontier-20261028-review-f16-actual-groups.py`, SHA256 `dcfd20812c9a29aada0335ada2e29b3f3b3706c3795ca938afe84e6317d14bf3`, and ran

`PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 frontier-20261028-review-f16-actual-groups.py`.

D22 is represented as C11⋊C2 with inversion action; A5 is the even permutations of five points. The program independently closes generated subgroups, checks subgroup multiplication closure, generates and checks partitions into actual **left** cosets, and builds the graph whose edges mean both disjointness and original-index gcd≤7. An eight-counterconfiguration is exactly an 8-clique. Its branch search uses integer bitsets, cardinality pruning and a proper greedy-coloring upper bound; incomplete coloring is never used to prune. Output:

```text
D22: order=22; subgroups=14; subgroup orders {1:1,2:11,11:1,22:1};
     left cosets=146; coset indices {1:1,2:2,11:121,22:22};
     search_nodes=1; counterexample_found=false
A5:  order=60; subgroups=59; subgroup orders {1:1,2:15,3:10,4:5,5:6,6:10,10:6,12:5,60:1};
     left cosets=1019; coset indices {1:1,5:25,6:36,10:100,12:72,15:75,20:200,30:450,60:60};
     search_nodes=61738; counterexample_found=false
```

The enumerated object/count and no-counterconfiguration results agree with the candidate's stated examples, while node counts differ because this is a different search. This independently checks only these finite groups; it neither establishes Sun7 nor supplies the arbitrary-group theorem. The candidate's own source programs and its coloring implementation were not used as independent evidence.

## 9. Exact final disposition

| Claim | Disposition |
| --- | --- |
| C2 LF1–68, normal index-two transfer | NO_SUBSTANTIVE_DEFECT with Sun8(N) and Sun7(G) explicit |
| Dual LF1–53, pair-gap and quotient-to-group theorem | NO_SUBSTANTIVE_DEFECT for every k≥2, with actual quotient Sun_k and actual kernel pair-gap |
| Spectrum and single-configuration sufficient conditions | NO_SUBSTANTIVE_DEFECT; sufficient only, no arbitrary free-fibre or necessity assertion |
| C2 solvable-quotient, infinite solvable reduction and perfect minimum counterexample | NO_SUBSTANTIVE_DEFECT conditional on universal Sun7 and the exact p=3,5,7,p>7 transfers reconstructed/cited above |
| Dual concrete D22/A5 claims | Independently reproduced for these finite groups only, as in §8 |

No counterexample to a claimed conditional implication was found. The source/candidate may be used only at those quantifiers and imports; no arbitrary-kernel extension theorem, arbitrary quotient closure, unconditional Sun7, unrestricted Sun8, simple-counterexample theorem or novelty conclusion follows. Parent must read the full candidate and review before adoption. Historical quarantines remain historical and are not retrospectively certified.
