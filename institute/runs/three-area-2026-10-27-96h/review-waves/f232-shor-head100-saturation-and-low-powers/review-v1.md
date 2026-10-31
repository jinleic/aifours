# f232 — hostile review of arbitrary-Q saturation and the low-power branches

## Verdict and claim-by-claim disposition

**Scoped result: CONDITIONAL SUPPORT for the written derivation through (6.1), not an all-n head-100 acceptance.** Given the explicitly stated cyclotomic field-degree/irreducibility facts and the stated Łaba–Londner Corollary 6.2/T2 import for Q, every hypothetical anchored tiling with |P|=100 has K≥4, P owning Φ₂ and Φ₁₆, and Q owning Φ₄ and Φ₈. In particular the independent derivation below excludes K=2, K=3, and K≥4 with s≠4. It quantifies over all eligible v and R and arbitrary Q; it does not invoke f220 or any other unlisted mathematical body. The last branch **s=4** is a distinct obligation, assigned to a separate reviewer; it is not resolved by this review. Consequently the candidate's all-n |P|=100 theorem and its full corollary cannot be accepted on this review alone.

| Claim attacked (target line references) | Disposition |
|---|---|
| Dilation, equal-gcd exclusion, forced prime divisibilities and coset counts (§2, lines 34–49) | No FATAL/MAJOR/MINOR found; reconstructed below for arbitrary multiplicities in R. |
| All-Q parity/label graph and all six free labels (§3, lines 51–69) | No FATAL/MAJOR/MINOR found; reconstructed from anchors and occupancy, not assumed from f220. |
| Fourier nonvanishing, field-degree application, uniformity and four-row saturation (§4, lines 71–97) | No FATAL/MAJOR/MINOR found, **conditional on the named ordinary cyclotomic irreducibility/degree facts**. The equal-row alternative is independently ruled out by the 2w-versus-w folded count below. |
| T2 ownership, extraction into every Q fibre, even-difference rule (§5, lines 99–116) | No FATAL/MAJOR/MINOR found, **conditional on the stated LL Cor. 6.2/T2 theorem** and cyclotomic irreducibility. Its actual external wording and applicability have not been sourced here. |
| K=2, K=3, and K≥4 with s≠4 (§6, lines 118–133) | No FATAL/MAJOR/MINOR found, conditional as above. Every possible second 2-power s is allocated; explicit residue and mod-5 comparisons are given below. |
| |P|=25 or 50 exclusion, hence the a=0,1 parts of the corollary | No FATAL/MAJOR/MINOR found. It follows from the same four-bucket lower bound with a separately adjusted w; it does **not** require T2, but remains conditional on the ordinary cyclotomic input. |
| K≥4, s=4 and the all-n |P|=100 theorem (§7) | **INCONCLUSIVE / outside this assigned mathematical slice.** The separate review must establish the final lift and contradiction; this document neither adopts nor refutes it. The a=2 part of the corollary is equally unresolved here. |
| LL source text, cyclotomic source text, actual-word code caller, author controls, unrestricted completion and novelty | **INCONCLUSIVE / not verified.** The caller is a separate import, not needed for the anchored-tiling reduction. Author controls and status are not premises. No claim of original-code completion, formal proof, human review, independent-model-family review, or novelty follows. |

No FATAL, MAJOR or MINOR mathematical finding was identified within the reviewed slice. INCONCLUSIVE categories are substantive limitations, not passes. The conditional reduction is a prospective reviewer assessment; adoption remains the parent's decision.

## Frozen evidence and actual read order

First research artifact: manifest `review-waves/f232-shor-head100-saturation-and-low-powers/manifest-v1.json`, whose measured SHA-256 was **3f60ba09509381c5eec283c81b598661cabd09254005b763924e552de7532d68**, matching the assigned full hash. I displayed its raw lines 1–15, 16–30. Before opening either declared input body, a single measurement obtained both full hashes, byte counts and LF counts and all matched their manifest declarations:

1. `institute/runs/three-area-2026-10-27-96h/dispositions/math-5-shor-single-small-shared-prime-head-exclusion-conditional-parent-v1.md`: **c1c4c95dc4f399fbcb9cc3356b0d415778f8a496e9417c9e8828c3ecf27ea8aa**, 3,637 bytes, 13 LF. Raw displayed window: 1–13, including ending. This provides only the authorized LL/T2 import context; its p·2^a theorem and its other named source bodies are not premises.
2. `mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-arbitrary-tail-head100-high-modulus-obstruction-v1.md`: **9ed4749c165a2aef8ab463f54248ed25533d6c8523c09ac085227076665f9eaa**, 20,968 bytes, 218 LF. Raw displayed windows, in order: 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, 181–195, 196–210, 211–218, including `END`. No input window exceeded 15 lines.

Both complete input displays preceded all mathematical analysis and controls. One attempt to read target lines 76–90 had a mistyped duplicated directory component and returned `Path ... not found`; it displayed no extra input and was immediately corrected to the pinned path, with the successful 76–90 window in the sequence above. This was a navigation deviation, not an input substitution. No f220, f161/f162, held source, sibling review, linked source, author receipt or author code was opened or used; no author code was run or imported. Review and control files are confined to the assigned wave directory.

## Reconstruction and attack

### 1. Elementary tiling facts, parameters and occupied classes

For X⊕Z=ℤₙ, let x,z be their integral group-algebra masks and G the sum of all n elements. If a prime ℓ does not divide |X|, then over 𝔽_ℓ, `(Σ[x])^ℓ z = x^(ℓ−1)G = |X|^(ℓ−1)G = G`. The corresponding **integral** nonnegative representation coefficients are all 1 modulo ℓ and sum to |X||Z|=n, so each is exactly 1. This proves ℓX⊕Z and injectivity of ℓ on X; iteration proves tX⊕Z when gcd(t,|X|)=1.

For differences d_X,d_Z with the same gcd g<n against n, write d_X=gu, d_Z=gv with u,v units modulo n/g. A unit t modulo n can be chosen lifting v/u: impose t≡v/u modulo n/g and avoid the remaining prime divisors of n by CRT. Since |X| divides n, t is coprime to |X|. In tX⊕Z the two differences coincide, contradicting uniqueness. This proves equal-gcd exclusion without adopting the disposition's theorem.

The head has differences 3, 5=8−3, 8, 11, and the tail has difference 1. If any of 2,3,5,11 failed to divide n, the corresponding head difference and 1 would have gcd 1 with n. Thus 330|n. If 3,5 or 11 failed to divide |Q|, dilation of Q by that prime would collide its tail difference 1 with the same head difference. Hence all three divide |Q|. For |P|=100, write

`n=2^K 5^v R`, `|Q|=2^(K−2) 5^(v−2) R`, `K≥2`, `v≥3`, `R` odd, `5∤R`, `33|R`.

Since gcd(R,100)=1, RP⊕Q tiles, and RP lies in Rℤₙ. Each class modulo R therefore contains exactly `2^(K−2) 5^(v−2)` tails. Every class modulo 33 is occupied and has the common positive count

`w = |Q|/33 = 2^(K−2) 5^(v−2) R/33`.

This uses no squarefreeness or bound on R.

For an odd Q-difference x, let g=gcd(x,n). If 5|x but 25∤x, then t=g/5 is odd and 5-free; tP⊕Q has the actual head difference 5t with gcd g. If 5∤x and 3|x or 11|x, use t=g/3 or g/11 and head difference 3 or 11. Equal-gcd exclusion therefore gives the **odd-tail rule**: opposite-parity tails agreeing modulo any of 3, 5, 11 must agree modulo 25.

### 2. Arbitrary-tail graph and mod-25 labels

An even tail congruent to 1 mod 3 would, by comparison with the odd anchors 1,7,13, be congruent modulo 25 to all three different values. Thus each tail in residue 1 mod 3 is odd. Every indicated mod-33 class is nonempty by the previous paragraph:

* A tail in class 3 mod 33 cannot be odd: comparison with even anchor 0 modulo 3 and even anchor 14 modulo 11 would force residues 0 and 14 mod 25. So the class is even. Class 25 is odd, agrees mod 11 with anchor 14, and is 14 mod 25; comparison across class 3 makes that even class 14 mod 25 too.
* A tail in class 11 cannot be odd: comparison with even anchor 14 modulo 3 and anchor 0 modulo 11 would force 14 and 0. Class 22 is odd, agrees modulo 11 with anchor 0, and is 0 mod 25; hence class 11 is 0 mod 25.
* An odd tail 0 mod 3 would compare to anchor 0 and an even class-3 tail, forcing 0 and 14 mod 25. An odd tail 2 mod 3 would compare to anchor 14 and an even class-11 tail, forcing 14 and 0. Thus `q odd ⇔ q≡1 (mod 3)` for every q.

For each j mod 11, occupied r=1 and r=0 classes have opposite parity. The odd-tail rule across equal j forces all tails with that j, for every r and either permitted parity, to share a residue f(j) mod 25. The literal anchors fix `f(0)=0, f(1)=1, f(2)=13, f(3)=14, f(7)=7`. If f(j)≡f(k) mod 5, comparing an odd class with label j to an even class with label k shows f(j)=f(k) mod 25. The five anchored values contain each residue mod 5 once; therefore every other f(j) is one of `{0,1,7,13,14}`. This argument does not restrict how the other six labels choose those values and does not assert that a resulting graph is itself a cyclic tiling.

### 3. Nonvanishing, inverse Fourier and exact four-row saturation

For ω∈{±1}, τ∈μ₃, η∈μ₁₁, ξ∈μ₂₅, all of which define characters because 1650|n, the previous class counts give

`Q̂(ω,τ,η,ξ) = w(1+τω+τ²) Σ_{j=0}^{10} η^j ξ^{f(j)}`.

When ξ≠1, the j-sum is nonzero:

* If η is primitive 11th, set d=ord(ξ)∈{5,25}. The **imported** cyclotomic degree formula gives `[ℚ(η,ξ):ℚ(ξ)]=φ(11d)/φ(d)=10`, because coprimality makes the compositum ℚ(ζ_{11d}). Hence η has minimal polynomial Φ₁₁ over ℚ(ξ). A degree-at-most-10 vanishing polynomial has all 11 coefficients equal, but here its coefficients at j=0,1 are 1 and ξ≠1.
* If η=1 and d=25, `Σ X^{f(j)}` is a nonzero integer polynomial of degree at most 14, smaller than deg Φ₂₅=20. If d=5, its coefficients aggregated mod 5 sum to 11, so cannot all be equal; the degree-at-most-4 polynomial cannot be a multiple of Φ₅.

The prefactor is nonzero for τ=1 and either ω (3 or 1), and for ω=−1 and primitive τ (−2τ). The tiling identity at these nontrivial characters, followed by inverse Fourier transform in the remaining coordinates, gives (i) for each parity and j, a P-count independent of z mod 25; and (ii) for each r mod 3 and j, the even-minus-odd P-count independent of z. Both assertions include every z, not merely a sampled subset.

The four anchors 0,11,3,8 lie in different `(parity,j)` buckets `(even,0),(odd,0),(odd,3),(even,8)`. Uniformity makes each bucket contain at least 25 elements. As |P|=100, these are exactly the four buckets, one actual element for each z in each bucket. In the odd j=3 row the signed-vector condition fixes its r label to 0 using anchor 3; in the even j=8 row it fixes r=2 using anchor 8. Let E(z),O(z) be the r labels of the even/odd j=0 elements. The signed-vector condition makes `e_{E(z)}−e_{O(z)}` independent of z: either E=O for every z, with their common value potentially varying, or E,O are one constant ordered pair of distinct labels.

To attack the variable equal case, fold the actual tiling onto `ℤ₂×ℤ₃×ℤ₁₁×ℤ₂₅`. Each target has exactly `n/1650=2w` representations counted with multiplicity. Fix target parity 0, r=0 and arbitrary j,z. For the two j=0 head rows, the required head z is the same `z−f(j)` and their r labels coincide. Exactly one of the even/odd rows can use a tail of the required parity and mod-3 class, contributing w. Neither the odd j=3 row nor the even j=8 row can contribute: their required Q parities and mod-3 classes violate `q odd ⇔ q≡1 (mod 3)`. The target would have w, not 2w, representations. Therefore E,O are distinct constants. Anchor 0 gives E=0 and anchor 11 gives O=2. The exact conclusion is `P mod 66 = 25·{0,3,8,11}`, with one P-element in every z mod 25 of each row.

The same first four-bucket lower bound separately excludes |P|=25 and 50. For either cardinality, 330|n and 5|Q| by the same anchor arguments, and 25 divides |P|; write n=2^K5^vR with K≥1, v≥3, 33|R, and use `w=|Q|/33`. Since gcd(R,|P|)=1, the equal occupied classes, graph, Fourier argument and the four ≥25 buckets all still apply. This extension does not assume the |P|=100 formula for w or its K≥2 bound.

### 4. Cyclotomic ownership and extraction in every Q fibre

Only primes 2 and 5 divide |P|, so at most two distinct primes divide both cardinalities. **Conditionally assuming** the named LL statement in the frozen input really applies to this arbitrary cyclic tiling and gives T2 for both masks, Q has T2; P's T2 is not needed for the low-power elimination reviewed here. No external LL text is represented as independently checked.

The nonvanishing at primitive 5th and 25th roots gives Φ₅,Φ₂₅|P. Also Q(−1)=11w≠0, so Φ₂|P. For the K factors Φ_{2^i}, each divides at least one mask because every primitive 2^i-th root is an n-th root and the tiling product vanishes there. Pairwise irreducibility and evaluation at 1 give ownership counts `m_P≤v₂(|P|)=2`, `m_Q≤v₂(|Q|)=K−2`, while `m_P+m_Q≥K`. Thus equality holds, no 2-power factor is shared, and P owns exactly Φ₂ and Φ_{2^s} for one 2≤s≤K; Q owns all the others. For every ℓ^j|R, ℓ is odd and not 5, so Φ_{ℓ^j}(1)=ℓ prevents P from owning it; Q owns it.

If Q owns Φ_{2^i}, T2 supplies Φ_{2^i d}|Q for every d|R, including all prime powers occurring in a nonsquarefree R. These distinct cyclotomic factors multiply to

`Φ_{2^i}(X^R) = ∏_{d|R} Φ_{2^i d}(X)`.

Indeed their roots are exactly the roots of `1+X^{R·2^(i−1)}`: their exact 2-primary order is 2^i and their odd order divides R. They are simple and both sides are monic. Write `Q(X)=Σ_{r=0}^{R−1} X^r F_r(X^R)` and decompose the quotient by Φ_{2^i}(X^R) in the same residue basis. Uniqueness gives Φ_{2^i}|F_r for **every** actual r fibre, not merely a total count. Since R is odd, each original-exponent fibre mask also vanishes at primitive 2^i-th roots. Reducing its coefficient polynomial modulo `X^{2^i}−1` and dividing by `Φ_{2^i}=1+X^{2^(i−1)}` yields equal folded counts at residues x and x+2^(i−1). In particular Φ₄, Φ₈, Φ₁₆ pair mod-4, mod-8, mod-16 counts across their lower-bit halves, respectively.

For the even-difference rule, let a Q-difference x satisfy 5∤x and have exact 2-part 8 in `g=gcd(x,n)`. Then t=g/8 is odd and 5-free, so tP⊕Q tiles, while its actual difference 8t has gcd g, contradicting equal-gcd exclusion. For K=3 the condition is simply x≡0 mod 8; for K≥4 it is x≡8 mod 16. The exclusion requires **both** the 2-adic condition and 5∤x.

### 5. All reviewed 2-adic branches

* **K=2:** n has exact 2-part 4 and is divisible by 3. `gcd(3·8,n)=gcd(13−1,n)=12`; multiplying P by 3 is allowed, or directly apply equal-gcd exclusion. Thus K=2 is impossible.
* **K=3, s=2:** Q owns Φ₈. In the mod-R fibre of anchor 13, a tail at 5 mod 8 has a mate at 1 mod 8. That mate has j=2, hence mod-5 value 13≡3, whereas anchor 1 has value 1. Their difference is divisible by 8 but not by 5, impossible.
* **K=3, s=3:** Q owns Φ₄. In anchor 7's fibre a mate is 1 mod 4, so is 1 or 5 mod 8, and has mod-5 value 7≡2. Compare it respectively to anchor 1 or 13, whose mod-5 values are 1 and 3. The difference is divisible by 8 but not 5, impossible.
* **K≥4, s∉{3,4}:** Q owns Φ₈ and Φ₁₆. In anchor 13's fibre Φ₈ supplies some residue 1 mod 8, i.e. 1 or 9 mod 16; Φ₁₆ pairing ensures residue 9 occurs. Such a tail has mod-5 value 3. Against anchor 1 it differs by 8 mod 16 and not by 0 mod 5, impossible.
* **K≥4, s=3:** Q owns Φ₄ and Φ₁₆. In anchor 7's fibre Φ₄ supplies a residue 1 mod 4. If it is 1 mod 8, Φ₁₆ ensures 9 mod 16 and comparison with anchor 1 gives difference 8 mod 16. If it is 5 mod 8, Φ₁₆ ensures 5 mod 16 and comparison with anchor 13≡13 mod 16 again gives difference 8 mod 16. The fibre's mod-5 value is 2, different from both 1 and 3. Both cases contradict the even-difference rule.

The only remaining allocation is K≥4 and s=4: P owns Φ₂ and Φ₁₆, while Q owns Φ₄ and Φ₈. The independent final obligation is to justify the source's s=4 common-bit/equal-weight fibre support, use of P's T2 in its mod-25 extraction, folded counts and shift equations, and its final contradiction, all for arbitrary Q and n. Those §7 claims are not premises of, and were not certified by, this slice.

## Reviewer-owned exact controls and limitations

One reviewer-created standard-library script, `reviewer-control-v1.py`, SHA-256 **fcf6c09cbae377943a9108a3972ceceffd5560a7f81bf42055ae7a9b8ce0f390**, was executed once with a 120-second cap. Actual `/bin/date` readings: start **2026-10-29T14:02:19-0700 PDT**, end **2026-10-29T14:02:19-0700 PDT**; monotonic elapsed 0.188 seconds, exit **0**, stderr empty. It did not import, compile or run author code.

* Exact finite arc consistency from the five anchors and the odd-tail rule reached a fixed point in 3 rounds on all 33 occupied classes. Every resulting candidate domain had the claimed parity and exactly the anchored/free label values. Intended-reason negative: an odd `(r,j,z)=(0,0,0)` candidate survives anchor-only checks but is eliminated by the occupied `(r,j)=(0,3)` class, forced even at z=14. This is a finite consequence check, not a substitute for the graph proof above.
* All **15,625=5⁶** free-label assignments passed exact integer Φ₅/Φ₂₅ remainder nonvanishing for η=1 and the mod-5-label consistency check. The η≠1 coefficient separation was checked exactly as 1−X modulo Φ₅ and Φ₂₅; the relative field degree remains an external conditional import. Intended negatives: a balanced 10-term sum reduces to zero mod Φ₅, `2Φ₂₅` reduces to zero mod Φ₂₅, and an all-equal coefficient vector is Φ₁₁, showing why the stated hypotheses matter.
* The projected head-count arithmetic gave one, not two, representations for all three E=O cases at the selected target; the anchored E=0,O=2 rows give two at all six parity/mod-3 targets. The control also exercised 129 exact K=2 gcd/low-bit cases. Its intended negative records that a mod-16 difference of 8 with equal mod-5 values cannot invoke the even-difference rule. These finite cases do not establish the arbitrary-parameter theorem by enumeration; the written argument does.

No control proves LL/T2, cyclotomic field-degree, the separate s=4 branch, the external code caller, or scientific novelty. There was no timeout. A cryptographic SHA-256 for this review is measured **after the completed write** and reported in the return to the parent; it is not a self-referential claim inside the file.
