# f189 — independent same-harness mathematical review v1

Observed native clock before writing: `2026-10-29T09:27:48-0700 PDT`.

## Disposition and scope

**CONDITIONAL PASS, full assigned scope.** Subject to the classical Sands divisor-exclusion theorem and Tijdeman positive-multiplier theorem stated below, I reconstructed a contradiction for **every** integer `k >= 0` and **every** factor-cardinality split in a direct tiling `P ⊕ Q = Z_(2310·2^k)` containing the specified anchors. I independently reconstructed the actual-same-code border bridge from finite unique decipherability and factor-completeness, rather than assuming finite maximality. Thus the stated finite-code corollary also follows under those imports. The finite controls are diagnostics, not the proof of this quantified conclusion.

No fatal (F) or major (M) mathematical finding. One minor (m) source-to-wording clarification, m1 below, is supplied with its proof and does not affect any application. No mathematical INCONCLUSIVE residual remains **conditional on the two classical imports**; their original proofs were not reproved here. In particular this is not an unconditional proof of Tijdeman or Sands, not a parent adoption, not a human review, not an independent-model-family review, not a formal/kernel verification, and not a novelty or priority determination. Same-harness review does not establish clean cognition; the candidate expressly discloses its author's same-author exposure.

### Claim-level verdicts

| Claim and candidate location | Verdict / qualifications |
|---|---|
| Actual-word border and anchors, §2, LF 49–76 | **PASS**, reconstructed below for finite, UD, factor-complete `D` with actual atoms `b,a^n`; not an assumed abstract border. |
| Sands I1, §3, LF 80–82 | **PASS conditional import**; source statement and hypotheses checked. |
| Tijdeman I2 and sequential dilation D, LF 84–90 | **PASS conditional import**, with **m1**: the directly cited positive-integer statement needs the elementary sign/zero extension if its integer wording is read literally. Every multiplier in this proof is positive. |
| Coset restriction C, LF 92 | **PASS**, by uniqueness of the original tiling, including equal fibre sizes. |
| L1, forbidden-odd-difference L2, and L3 for every `330 | n`, LF 99–113 | **PASS**, all exponents and extra odd primes allowed as stated. |
| All cardinalities and residual `d = 7,21,35,77`, LF 117–127 | **PASS**; `21,35,77` are eliminated by L1, `d=1` by L3, and every `d=7` split is treated. |
| Fibres and exact power-of-two parity dichotomy S2–S5, LF 129–156 | **PASS**, including no projection collapse, endpoints `a=0` or `b=0`, and arbitrary `K>=1`. |
| Cross-separation S6, LF 158–167 | **PASS**, both multipliers and both gcd identities checked under their exact hypotheses. |
| Lemma H and S7–S8, LF 169–181 | **PASS**, the stated bipartite graph is connected for every proper period; no partition enumeration is used in the proof. |
| Final gcd collision S9 and all-k theorem/corollary, LF 183–185 | **PASS conditional on I1–I2**; the contradiction is uniform. |
| Author's numerical checker/report, LF 194–208 and 202-LF script | **NOT REPLAYED**: author code was read in full but never executed/imported. Independent controls and their precise limits are below; no inference that its own reported run was observed here. |

**m1, minor clarity.** The cited published formulation specifies `r ∈ N`. Candidate §3 initially introduces integer dilations and then states I2 for `r` coprime to the moved factor's cardinality without explicitly restricting its sign. The source directly justifies positive `r`; all proof multipliers (`p`, odd part `T`, `165`, `7`, `g/p`, `h`) are indeed positive. If the broader signed statement is intended, it is also true: for `r<0`, apply the positive theorem to `-r`, then use Sands with `Div(-X)=Div(X)` and unchanged cardinality to replace `X` by `-X`; for `r=0`, coprimality forces the moved factor to be a singleton, so its complement is the entire cyclic group. This resolves the wording without an additional import.

## Provenance, exact input reads, and source pins

The manifest was the first wave input read; its SHA-256 was checked before reading its contents:

* `manifest-v1.json`: `a43e9738a703e6b3ce1165122d67d0771b33e20e8055822ed8f750465818cef4`, 3,406 bytes, 30 LF.
* Both declared inputs were hashed and byte/LF counted **before** mathematical consideration. Then I read the entire candidate in LF order 1–218, followed by the entire author script in LF order 1–202. The ranged reads overlapped at boundaries; no line is omitted. No mandatory overlay or erratum is declared in this manifest.
  * `mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-2310-family-complete-no-go-v1.md`: `2d6b48f85737a316bb1d2a4ec5997ee43e81ff18ef9e9a5f0eb8b0c36d41f61e`, 20,144 bytes, 218 LF.
  * `mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-2310-family-complete-no-go-check.py`: `63e36a43da435a4d699c4cee9ee7fe55d938bb446ac4e73ed0d242f6511c67a9`, 6,842 bytes, 202 LF. Read/hash only; never run or imported.
* Thereafter the two named public sources were initially fetched in parallel, so I assert no order between those initial fetches. I then fetched and pinned the exact PDFs in the order LL then Cordero and consulted the following locations on those exact pinned bytes. The LL and Cordero articles **state/attribute** the classical results; I did not read the original Sands, Tijdeman or RSS papers and do not present these source checks as reproofs of those imports.
  * Łaba–Londner, *Combinatorial and harmonic-analytic methods for integer tilings*, [arXiv:2106.14042v3](https://arxiv.org/pdf/2106.14042v3), PDF p. 3, Tijdeman sentence, and p. 10, Definition 2.4 and Theorem 2.5. Local `reviewer-source-laba-londner-2106.14042v3.pdf`, 1,006,826 bytes, SHA-256 `4a7707e7dd3ca38379a536c7ae928e7915d1be0725e1e065389c9f4bb4234cf8`.
  * Cordero, *Factorizations of Cyclic Groups and Bayonet Codes*, [arXiv:2301.13566v1](https://arxiv.org/pdf/2301.13566v1), PDF p. 3, Theorem 1.1 and definition immediately after it. Local `reviewer-source-cordero-2301.13566v1.pdf`, 331,796 bytes, SHA-256 `5ac712593068198e1bb13628df418c1802658a7c03fb9708124da05f3d82bd00`.
* Disclosure of tool display: the initial un-ranged article/PDF renders displayed surrounding material, including text about T2, in addition to the named statements. Neither T2 nor LL Corollary 6.2 is used as a premise here. The exact PDF statements were also checked with page-limited `pdftotext`, including intact mathematical symbols. I did not open sibling reviews, the cited prior packets, held/zero/f161/f162 payloads, or contact the author. No external model/API, web search, Git, deletion, publication, or infrastructure modification was used.

## Exact import hypotheses and elementary consequences

For nonempty sets `X,Y ⊂ Z_M`, put `Div_M(X) = {gcd(x-x',M): x,x'∈X}`. The pinned LL p. 10 states **Sands** as the equivalence

`X ⊕ Y = Z_M` iff `|X||Y|=M` and `Div_M(X) ∩ Div_M(Y)={M}`.

In this review, the needed direction is tiling implies divisor-set disjointness apart from `M`, plus the equivalence only for the optional signed-multiplier clarification. The equal-pair difference contributes `M`, not zero. No assertion about an arbitrary partial direct sum follows without the cardinality hypothesis.

The LL p. 3 formulation of **Tijdeman** says: if a finite integer set `A` tiles `Z` with a specified complement and positive integer `r` is relatively prime to **`|A|`**, then `rA` tiles with that same complement. It does **not** require `gcd(r,M)=1`, nor is coprimality to the complement's cardinality the required hypothesis. To obtain the cyclic form, choose representatives of `X,Y`; `X ⊕ Y=Z_M` is equivalent to the integer tiling `X ⊕ (Y+MZ)=Z`. Applying the cited result, then reducing mod `M`, preserves unique representations. If two distinct `r x` collapsed mod `M`, a fixed `y` and two different `MZ` shifts would give two integer representations, contradiction. Hence `|rX|=|X|` and `rX ⊕ Y=Z_M`. Apply this in sequence to get `tX ⊕ sY=Z_M` whenever `t,s>0`, `gcd(t,|X|)=1`, and `gcd(s,|Y|)=1`; the first dilation does not alter its cardinality.

For coset restriction, if `X ⊂ H ≤ G` and `X ⊕ Y=G`, each sum in `g+H` necessarily uses a `Y` element in that coset, and uniqueness is inherited. Thus `X ⊕ (Y∩(g+H))=g+H` and each such fibre has `|H|/|X|` elements. This elementary argument needs no separate tiling theorem.

## Actual-word border bridge

Let `D` be the **same finite code** containing the literal atoms in the candidate, and suppose it is UD, factor-complete, and contains the actual pure atom `a^n`. Let `L` be its maximum atom length. UD makes `a^n` the only pure-`a` atom: two distinct such atoms would commute and give different atom lists for the same word. Also, as `b` is an actual atom, no `b^j`, `j>1`, can be an atom. Define actual border sets, reduced mod `n`, by

`P={i: a^i b^k ∈ D for some k>=1}` and `Q={j: b^l a^j ∈ D for some l>=1}`.

These are not arbitrary witness sets chosen from different codes. To prove directness, suppose `i_t+j_t` are congruent mod `n` for two actual border pairs. Choose a common `G` in that residue class larger than both sums, and `H,K` larger than the relevant `l_t,k_t`. Both lists

`b^(H-l_t), (b^l_t a^j_t), (a^n)^((G-i_t-j_t)/n), (a^i_t b^k_t), b^(K-k_t)`

spell the same `b^H a^G b^K`; outer powers mean repeated copies of the atom `b`. A nonempty block of pure-`a^n` atoms lies between the border atoms. The atoms touching the two ends of the central `a`-run identify the actual border words; if an exponent is zero, its border atom is necessarily `b`. Consequently equal atom lists force the same actual exponents, hence the same residue pair. UD rules out two distinct pairs.

For coverage take any prescribed residue class and choose `g>L` in it. Factor-completeness puts `b^L a^g b^L` inside some `D*` word. The atom containing the last left-guard `b` starts within that guard and cannot reach the right guard, hence is `b^l a^j`; symmetrically the atom containing the first right-guard `b` is `a^i b^k`. They are distinct because `g>L`, and all atoms strictly between them are pure `a`, hence equal to `a^n`. Therefore `g ≡ j+i (mod n)`. This proves `P ⊕ Q=Z_n` without silently replacing factor-completeness by maximality. Cordero's Theorem 1.1 separately states the actual-border factorization for a **finite maximal** code containing `b,a^n`; the preceding direct argument handles the hypothesis in the candidate.

The literal code supplies `b,a^3b,a^8b,a^11b` and `b,ba,ba^7,ba^13,ba^14` as actual atoms. Thus `A={0,3,8,11}⊂P` and `Y={0,1,7,13,14}⊂Q`, with no modular collision for the target `n>=2310`.

## Uniform reconstruction of L1–L3 and the full family

Let `330|n`, and assume `P ⊕ Q=Z_n` with the anchors. In `P` there are differences exactly `3`, `5=8-3`, and `11`; in `Q` there is a difference `1`.

* **L1.** If `p∈{3,5,11}` did not divide `|Q|`, positive Tijdeman gives `P ⊕ pQ=Z_n`. The differences `p` in `P` and `p(1-0)` in `pQ` have common gcd `p<n` with `n`, contrary to Sands. Thus `165 | |Q|`.
* **L2.** If an odd `x=q-q'` is divisible by such a `p`, let `g=gcd(x,n)`. If `g/p` is coprime to `|P|`, dilate `P` by `g/p`. The anchored difference `p` then has gcd `g` with `n`, as does `x` in `Q`; `g<n` because `n` is even and `x` odd. Sands gives a contradiction. No squarefreeness assumption is needed for this lemma.
* **L3.** If `|P|=2^a`, let `T` be the odd part of `n`. Since `gcd(T,|P|)=1`, the tiling `TP ⊕ Q` and subgroup restriction show `Q` meets every class mod `T`, hence has some `q ≡ 6 (mod 165)`. For every odd `Q` difference divisible by 3, 5, or 11, the multiplier `g/p` in L2 is odd and thus coprime to `2^a`. If `q` is odd, use `q-0`, divisible by 3; if `q` is even, use `q-1`, divisible by 5. Both are prohibited. Thus `|P|` cannot be a power of two.

Now write `n=1155·2^K`, `K=k+1>=1`. By L1 and `|P||Q|=n`, the only possible odd parts of `|P|` are 1 or 7. In particular `d=21,35,77` each contain respectively a 3,5,11 already forced into `|Q|`, so are impossible; `d=1` is excluded by L3. The only remaining split, for **every** `K` and **every** `0<=a<=K`, is

`|P|=7·2^a`, `|Q|=165·2^b`, `a+b=K`.

For `q,q'∈Q` with odd difference `x`, if `gcd(x,165)>1` and `7∤x`, then `g=gcd(x,n)` is an odd divisor of 165. For any `p∈{3,5,11}` dividing `x`, `g/p` is coprime to `7·2^a`, contradicting L2. Therefore

`x odd and gcd(x,165)>1  =>  q ≡ q' (mod 7)`.  (tail rule)

Since `gcd(165,|P|)=1`, `165P ⊕ Q=Z_n` without collapse. For `r∈Z_165`, the subgroup/coset argument gives exactly `2^b` elements in `Q_r={q∈Q:q≡r mod 165}`. All fibres are nonempty.

### The parity dichotomy, without hidden projection assumptions

Fix `r` and put `N=n/165=7·2^K`. Restriction of `165P ⊕ Q` to the coset `r+165Z_n`, followed by the isomorphism `165z↦z mod N`, gives `V ⊕ Pbar=Z_N`, where `V` is the image of `Q_r-r` and `Pbar={p mod N:p∈P}`. `P→Pbar` is injective because multiplication by 165 did not collapse; `|V|=2^b`. Since `gcd(7,|V|)=1`, `7V ⊕ Pbar=Z_N` and `7V` has the same size. Restrict to the mod-7 coset `γ`: `Pbar_γ ⊕ 7V` covers that coset directly and `Pbar_γ` is nonempty. Reduction mod `2^K` is bijective on the `γ`-coset and on `7Z_N`; as reduction is an ambient group homomorphism, the two image sets directly tile `Z_(2^K)`. It is not necessary to pretend that a nonzero coset itself is a subgroup.

In any direct tiling of `Z_(2^K)`, `K>=1`, both factors cannot contain odd differences: then each divisor set contains 1, contrary to Sands. They also cannot both have one parity, since all sums would have the same parity. Thus exactly one factor has both parities. As 165 and 7 are odd, this exactly transfers to the pair `P_γ,Q_r`. Because this holds for **every** `γ,r`, either all `Q_r` are mixed-parity and no `P_γ` is, or all `Q_r` are single-parity and every `P_γ` is mixed. The argument includes `a=0` and `b=0`; no fibre is assumed to have both parities without justification.

If all `Q_r` were mixed, the tail rule makes every element of each one fibre have the same residue mod 7 (compare each element to an opposite-parity element). Comparing opposite parities in `Q_r,Q_(r+3)` and in `Q_r,Q_(r+5)` propagates that residue, since the relevant gcds with 165 are 3 and 5. The steps 3 and 5 generate all of `Z_165`; consequently all of `Q` would have one residue mod 7, contradicting its actual elements 0 and 1. Thus the second branch holds. Write `E,O` for the classes whose `Q_r` are even/odd respectively; they partition `Z_165`, both are nonempty, and the anchors put `0,14∈E` and `1,7,13∈O`.

### Cross-separation, Lemma H, and the collision

Take any opposite-parity pair `p,p'∈P_γ`, put `y=p-p'` and `h0=gcd(y,165)`. If some `r∈E,r'∈O` agree mod `h0`, take `q∈Q_r,q'∈Q_r'`, put `x=q-q'` and `h=gcd(x,165)`. Then `x,y` are odd, `7|y`, and `h0|h`. The numbers `h` and `7` are respectively coprime to `|P|=7·2^a` and `|Q|=165·2^b`; sequential positive Tijdeman yields `hP ⊕ 7Q=Z_n` without collapse. Since the odd part `1155=3·5·7·11` is squarefree, prime-by-prime

`gcd(7x,n)=7h` and `gcd(hy,n)=7h`.

For the second identity, at each `ℓ∈{3,5,11}`, `ℓ|hy` iff `ℓ|h` or `ℓ|h0`, which reduces to `ℓ|h` because `h0|h`; 7 divides `y` and no factor 2 occurs. Thus `7h<n` belongs to both divisor sets of `hP,7Q`, violating Sands. Hence no E/O pair agrees modulo `h0`: each full `h0`-class is entirely E or entirely O. This is the required periodicity, and `h0>1` since both E and O are nonempty.

If `h0<165`, choose a prime `ℓ∈{3,5,11}` absent from `h0`. By CRT, E is independent of the `ℓ` coordinate: `E=Z_ℓ×E'`, with nonempty proper `E'⊂Z_m`, `m=165/ℓ=q1 q2`. Consider the graph on all 165 classes, joining E to O when they share at least one of the three prime coordinates. Every `ℓ`-layer is a connected complete bipartite graph. Some `e'∈E',o'∈O'` must agree modulo `q1` or `q2`: otherwise, writing `e'=(e1,e2)` and `o'=(o1,o2)`, the mixed point `(e1,o2)` could belong to neither O' nor E'. Such a cross-pair connects every pair of ℓ-layers, so the whole graph is connected. On each edge the tail rule forces **all** elements in its two nonempty `Q` fibres to share a mod-7 residue; connectivity forces all of Q to do so, contradicting `0,1∈Q`. Thus `h0=165` for every opposite-parity pair in each `P_γ`.

Each `P_γ` contains both parities, so fixing one element of the opposite parity shows that **all** elements of that fibre are congruent mod 165. In `P_0`, the anchor 0 and mixed parity give an odd `p0` with `p0≡0 mod 7` and `p0≡0 mod 165`, hence `p0≡0 mod 1155`. The anchor `8∈P` yields odd difference `8-p0≡8 mod 1155`, so `gcd(8-p0,n)=1`; meanwhile `1-0` gives 1 in `Div_n(Q)`. Sands gives the final collision. This proves the entire residual branch, and therefore all `n=2310·2^k` and all factor sizes, conditional only on the named imports. It makes no assertion for other orders beyond the separately proved 330-divisibility lemmas.

## Independent finite controls and receipt

One fresh standard-library checker, written from definitions and never importing author code, was run as `python3 -B reviewer-controls-v1.py reviewer-controls-input-v1.json`. Native `/bin/date` clocks before/after the single bounded run were both `2026-10-29T09:23:10-0700 PDT`; monotonic elapsed `0.164021 s`, cap `105 s` (<120), exit `0`, empty stderr. The receipt binds script and input hashes both before and after, exact stdout/stderr hashes, clocks, cap, status and exit. A cap, had it occurred, would have meant UNKNOWN, never exclusion.

* Actual-word positive example: for `n=6`, `D={a^6,b,ab,ba^2,ba^4,aba^2,aba^4}`, the independent Sardinas–Patterson procedure finds UD; a finite subset-automaton exploration from all accessible/coaccessible codeword-prefix states finds factor-completeness (19 reachable subset states); actual border atoms give `P={0,1}`, `Q={0,2,4}`, a direct tiling. Adding `a^2` is rejected specifically as non-UD; deleting the completion atoms leaves a UD but factor-incomplete code, with explicit missing factor `baab`.
* Definition-based enumeration with 0 in both factors: in `Z_6,Z_8,Z_12`, respectively 102, 492, 28,316 size-compatible ordered set pairs were checked; 14, 34, 194 are tilings, and 50, 140, 1,168 positive admissible dilations were checked. The 194 count includes the two singleton/full-set splits, unlike the author's nontrivial-factor-only check. The `Z_6` positive dilation `r=3` is coprime to `|P|=2` but not to modulus 6. Mutations detect duplicate representation at residue 2, missing cardinality despite disjoint divisor sets, and multiplier 2 being coprime only to the wrong factor; the latter actually produces the intended tiling collision.
* For all `K=1,2,3,4` and every `a`, 28 unanchored interval tilings cover both possible odd-factor splits. For the 14 `7·2^a` examples, all 16,170 `(r,γ)` projected tilings and parity comparisons pass, exercising both branches (4 Q-mixed and 10 P-mixed cases). These are **not** anchored Shor solutions.
* Arithmetic control: 3,465 odd residue representatives for `K=1,3,5`, 2,835 second-gcd cases, and 255 final-gcd instances. Mutations introducing a second factor of 7 into `n`, dropping `h0|h`, or replacing the final anchor 8 by 6 fail for the named respective gcd reason; the last has gcd 3.
* Graph control: 32,766 nontrivial cuts of the `Z_15` two-prime CRT graph were exhaustively checked for a cross-edge; 105 additional periodic partitions were checked by constructing the full 165-vertex graph. The intentionally invalid extension to period 165 with `E={0}` and the mutated requirement of two common prime coordinates are rejected as disconnected. This is not exhaustive over all partitions for periods 33 or 55; the uniform written Lemma H above covers them.

All 11 negative checks reported their **intended** rejection, not just an arbitrary exception. Exact artifact identities (SHA-256):

* `reviewer-controls-input-v1.json`: `9bb1e2f538472dabf571cb858b2ffc77d5a3a98340fe0dbf1e612573354b48eb`.
* `reviewer-controls-v1.py`: `15bfb4d07d7f75cc3ba32bdeaf6e8fdf785b538808e82923b80b78bba2773a3a`.
* `reviewer-controls-stdout-v1.txt`: `28bb9068686dd6ec6697da08fd6a30f9432c0e34c55d4f351984a2f2790987a2`.
* `reviewer-controls-stderr-v1.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
* `reviewer-controls-receipt-v1.json`: `6a8910ebe4f03b1a6d2cad64ecc4979e0376315110eebdeac6f40a5edbcab373`.

The SHA-256 of this completed review is recorded separately in `reviewer-review-sha256-v1.txt`, avoiding a self-referential hash.
