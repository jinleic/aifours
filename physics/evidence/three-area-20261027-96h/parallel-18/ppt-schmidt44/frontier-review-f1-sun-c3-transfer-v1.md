# f1 — index-three normal Sun8 transfer: independent scientific review

Reviewer **PhysicsPPT44-2**. Actual native clock observed immediately before creation: **Wed Oct 28 17:09:12 PDT 2026**.

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT CONDITIONAL SCOPE — 0 FATAL / 0 MAJOR / 0 MINOR.** For every group G and N normal of index 3, the supplied argument proves `Sun8(N) ∧ Sun7(G) ⇒ Sun8(G)`. Its finite 3-group quotient corollary additionally requires Sun7 for every intermediate group, which follows from the separately stated arbitrary-group Sun7 import **if that import holds**. Sun7 is not proved or independently authenticated in this review. This is a written proof reconstruction plus a separately implemented finite overapproximation check; it is not formal/kernel, human, configured-family, novelty, publication or unrestricted-Sun8 acceptance.

## 1. Bound inputs and exposure

The assignment `review-waves/f1-sun-c3-transfer/assignment-v1.json` has SHA256 `1dfb9f87c82a566fca9909f3a42175ca12522b293caf64f704bd71de51a34526`. The complete 100-LF candidate `frontier-20261028-c3-normal-transfer-v1.md` has SHA256 `5c9099385c75e451a60f8bebe1c133dc1da07285e504aa822799e91027e70668`; all lines, including the ending, were read. The literal eight-coset target in `math-6-sun-eight-definitions-v1.md` was also read.

I reviewed a different Sun-related proof duty earlier in this run and have prior general Sun-coset familiarity; this is not blind, independent-family or clean-cognition review. No prior quarantined outcome or author's checker result is used as a proof premise. All algebra and actual-coset statements below are reconstructed from the present candidate and elementary group/index facts. No author contact or nested agent was used.

## 2. Exact definitions and actual fibre lemma

For k=7,8, `Sun_k(X)` means that **every** collection of k pairwise-disjoint actual left cosets of finite-index subgroups of X has two subgroup indices with gcd at least k. Groups may be infinite; subgroups may coincide when their chosen cosets are disjoint; no covering or normality of the individual subgroups is assumed.

Assume N is normal in G with `[G:N]=3`, and suppose eight actual disjoint left cosets `g_i U_i` have original indices `n_i=[G:U_i]` satisfying `gcd(n_i,n_j)≤7` for every distinct pair. Put

`b_i=[N:N∩U_i]`, `a_i=[G/N:π(U_i)]`, so `n_i=a_i b_i`.

Indeed NU_i is a subgroup because N is normal, `[G:NU_i]=a_i`, and the coset bijection `N/(N∩U_i) → NU_i/U_i` gives `[NU_i:U_i]=b_i`. Finite-index hypotheses make every quantity finite. Since G/N has order three, each a_i is 1 or 3: the image of a full-image label is the entire quotient, while a proper-image label occupies one actual quotient point.

For a point q in the actual image of `g_i U_i`, fix one representative t of q and choose `tx∈g_i U_i∩tN`, with x∈N. Then

`t^(-1)(g_i U_i∩tN)=x(N∩U_i)`.

This is an actual left coset in N of index b_i. Original disjointness makes any two fibres at the **same** quotient point disjoint.

Two finite-index left cosets of H,K in any group cannot be disjoint when their indices are coprime. To prove this, the map `G/(H∩K) → G/H × G/K`, `g(H∩K)↦(gH,gK)`, is injective. The finite integer `[G:H∩K]` is divisible by both `[G:H]` and `[G:K]` and is at most their product; for coprime indices it equals the product, so the injection is surjective, including the desired pair of cosets. Therefore, whenever two quotient-image cosets meet, their actual kernel fibre indices satisfy `gcd(b_i,b_j)≥2`.

For any two proper-image labels, `n_i=3b_i`, so `3 gcd(b_i,b_j)=gcd(n_i,n_j)≤7`, hence `gcd(b_i,b_j)≤2`. For any full-image label its actual quotient image meets every other image, making the noncoprime-fibre condition available. If there are at most one proper label, all eight images share an actual point; `Sun8(N)` applied to the eight disjoint fibres yields a kernel gcd≥8 and hence an original gcd≥8. Thus a counterconfiguration must have at least two proper labels. This argument uses neither splitting nor independent artificial fibre choices.

## 3. Sun7 forcing, with the import kept explicit

Apply the assumed property `Sun7(G)` to each seven-member subfamily of the eight actual disjoint cosets. Each has a pair with gcd≥7; under the counterconfiguration assumption that gcd is exactly 7. Thus at least two members of every seven-subfamily have indices divisible by 7. If at most two of all eight indices were 7-divisible, deleting one such label when present—or any label if there are none—would leave a seven-subfamily with at most one, contradiction. Hence at least three original indices are 7-divisible.

At most one proper label is 7-divisible: two such original indices both contain 3·7, violating the gcd≤7 assumption. There are consequently at least two 7-divisible full labels, say V,W. Their pairwise gcd is exactly 7, so they cannot both be even; choose V odd. These are deductions from the **hypothesized** Sun7 property, not an independent proof of that property.

## 4. No 7-divisible proper label

Let A,B be any two proper labels. Here neither b_A nor b_B contains 7. The odd 7-divisible full label V has an actual common fibre with each, so each `gcd(b_A,n_V)` and `gcd(b_B,n_V)` is between 2 and 7. Any prime dividing such a gcd is odd and not 7, hence is 3 or 5. But `gcd(b_A,b_B)≤2`, so A and B cannot use the same odd prime. After interchanging them, `3|b_A`, `5|b_B`, and both 3 and 5 divide n_V. Since `n_B=3b_B`, both n_B and n_V are divisible by 15, contradicting their original gcd≤7. No additional quotient-position, selected index or coset-realizability assumption is used.

## 5. Exactly one 7-divisible proper label

Let A be that label, and let V,W be 7-divisible full labels with V odd. Since 21 divides n_A, no 7-divisible full index is divisible by 3; otherwise its gcd with n_A would be at least 21.

There is another proper label B, necessarily with 7∤b_B. Its fibre meets V's. Their common divisor is between 2 and 7; V is odd and not divisible by 3, while b_B is not divisible by 7. Thus `5|b_B` and `5|n_V`. There cannot be a second other proper label: its b-index would also contain 5, contradicting the proper/proper bound `gcd(b_i,b_j)≤2`. Therefore A and B are the only proper labels; the remaining six are full.

Because `gcd(n_V,n_W)=7`, the index n_W is not divisible by 5. It is not divisible by 3 as just shown. Its fibre meets B's, with no 7 available from b_B; hence the only possible common prime is 2. So `2|n_W`, `2|b_B`, and `5|b_B`. Since 7 divides b_A and both original indices would otherwise share 14, b_A is odd. The bound `gcd(b_A,b_B)≤2` then gives `gcd(b_A,b_B)=1`; in particular `5∤b_A`.

Choose a full label F different from V,W; it exists among the six full labels. If 7 divided n_F, then the common 7 with the even n_W would force F odd, the common 7 with n_V would force `5∤n_F`, and the common 7 with n_A would force `3∤n_F`. Since 7∤b_B, its actual fibre could then share no prime ≤7 with B's, while a larger shared prime would violate the original gcd≤7. This contradicts disjoint fibres. Thus `7∤n_F`.

F meets A's fibre. A's b-index is odd and not divisible by 5; n_F is not divisible by 7. Their nontrivial gcd, bounded by 7, must have common prime 3. Therefore `3|b_A` and `3|n_F`. Coprimality of b_A,b_B gives `3∤b_B`.

F also meets B's fibre. Since 3∤b_B and 7∤n_F, their common prime ≤7 must be 2 or 5. If 5 divided n_F, both n_F and `n_B=3b_B` would contain 3·5, contradicting gcd≤7. Thus `5∤n_F` and their common prime is 2.

Finally F,V are both full and have disjoint fibres, requiring `gcd(n_F,n_V)≥2`. But n_V is odd and not divisible by 3, while n_F is divisible by neither 5 nor 7. They have no common prime ≤7; a common prime >7 would violate the original bound. Hence their gcd is 1, contradiction. This pays the previously delicate single-proper-seven case using the same actual A,B,V,W,F and both kernel and G indices.

The zero/one-proper and the two possible 7-divisible-proper cases exhaust the hypotheses. Thus the conditional index-three theorem follows exactly as stated.

## 6. Finite 3-group quotient corollary

For a nontrivial finite 3-group Q, the class equation shows its centre has size divisible by 3 and is therefore nontrivial. An appropriate power of a nonidentity central element has order 3. Quotient by the resulting central subgroup and induct on |Q|; pulling the smaller series back gives a chain from 1 to Q in which each subgroup is normal in the next and each quotient has order 3. The trivial group gives the empty chain.

When Q=G/N, take inverse images of that chain in G. At each step the subgroup just reached is normal of index 3 in the next one. Induction transfers Sun8 from N to G **provided Sun7 holds for each intermediate larger group**. The stated arbitrary-group Sun7 import would pay these hypotheses simultaneously. Without it, the explicit intermediate Sun7 hypotheses are needed; neither a single unqualified source assertion nor the support calculation supplies them. No assumption that the extension splits or that G itself is finite is used.

## 7. Independent bounded check — supplementary only

I wrote and ran a separate checker, `frontier-20261028-review-f1-sun-c3-check.py`, SHA256 `6aaa582e572bfe0fe740689ad385b85eb682652b2a72b53ae7bfb6f09af6c88f`, using

`PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 frontier-20261028-review-f1-sun-c3-check.py`.

It uses only the 16 squarefree prime supports of 2,3,5,7, original-index gcd≤7 and the necessary noncoprime-fibre conditions whenever at least one image is full. It permits extra abstract support patterns and does not construct a group. For the no-proper-seven contradiction it keeps A,B,V,W, with V odd; for the one-proper-seven contradiction it keeps A,B,V,W,F, with F non-seven as proved in §5. The output was:

```text
no_proper_7: domain_sizes=[8,8,4,8], partial_counts=[1,8,36,0,0], terminal_models=0
one_proper_7: domain_sizes=[8,8,4,8,8], partial_counts=[1,8,36,12,3,0], terminal_models=0
```

This is independent code, not the author's recorded checker. The reduction is an overapproximation: each retained squarefree support divides the actual b-index; `3b` for a proper label likewise divides its actual original index. A nontrivial common fibre gcd under the original gcd≤7 bound must have a shared prime in {2,3,5,7}, so truncation does not remove the required noncoprimality. Higher valuations, other primes and actual group/coset compatibility are intentionally discarded. Zero support models are consistent with the written contradiction, but are **not** a proof of Sun7, actual coset construction, the group-fibre lemma or unrestricted Sun8. I do not use the author's truncated-signature output as independent evidence.

## 8. Disposition and unresolved scope

| Claim | Exact disposition |
| --- | --- |
| Candidate LF16–38, actual fibres and two-proper reduction | NO_SUBSTANTIVE_DEFECT; valid for arbitrary G with N normal of index 3 |
| LF40–44, seven-label forcing | NO_SUBSTANTIVE_DEFECT conditional on Sun7(G); no proof of the imported property claimed |
| LF46–76, both proper-seven cases | NO_SUBSTANTIVE_DEFECT; all gcd, parity and same-fibre steps reconstructed above |
| LF78–82, finite 3-group quotient | NO_SUBSTANTIVE_DEFECT with Sun7 at every intermediate group, e.g. from the universal statement import |
| LF84–94, supplementary author enumeration | Not treated as independent evidence; a different bounded necessary-condition checker was run as stated |

No gap requiring a counterexample was found in the conditional proof. No actual index/group counterexample, unrestricted Sun8 proof, 2-quotient/mixed-factor closure, proof of Sun7, source/book equivalence or novelty determination is supplied. Zhu's 2008 primary abstract [arXiv:0807.2207](https://arxiv.org/abs/0807.2207) states k=3,4, not the Sun7 statement; it is context, not a substitute for the explicit import. Parent must read this complete return and the candidate before any adoption. Earlier immutable quarantine/process findings remain historical and are not retrospectively certified by this proof.
