# f233: hostile review of the head-100 high-modulus final branch

## Verdict and findings

**Scoped conclusion: CONDITIONAL WRITTEN SUPPORT** for the nonexistence of an anchored cyclic tiling with `|P|=100`, assuming the explicitly named Łaba–Londner/T2 and classical cyclotomic inputs below. I reconstructed the arbitrary-tail argument and the `K≥4, s=4` branch in this review; I did not use f220, f232, any other review as a mathematical premise, the author's controls, or an author verdict. **Mathematical findings: 0 FATAL / 0 MAJOR / 0 MINOR.** The separate process MINOR below does not affect the frozen-input ordering. The external imports and the original-code caller are **INCONCLUSIVE as independent source-verification questions**. This is not unconditional acceptance, an independent-model-family or human review, a formal/kernel check, a novelty assessment, or a claim about unrestricted Shor completion or heads of size at least 200.

| Claim | Disposition |
|---|---|
| Dilation, gcd exclusion, anchor forcing, and all mod-33 occupancies | SUPPORTED; 0F/0M/0m, reconstruction in §2 |
| Odd/even class graph, all five anchors, and six free `f` labels | SUPPORTED; 0F/0M/0m, §3 |
| Fourier nonvanishing and all 25-residue head rows | SUPPORTED **conditional on the named cyclotomic inputs**; 0F/0M/0m, §4 |
| Four-row saturation and the `2w` versus `w` count | SUPPORTED under those inputs; 0F/0M/0m, §4 |
| Prime-power ownership, T2, and transport to **every actual** `Q_r` | SUPPORTED **conditional on LL/T2 and cyclotomic irreducibility**; 0F/0M/0m, §5 |
| Elimination of `K=2`, `K=3`, and `K≥4, s≠4` | SUPPORTED conditional on the transported factors; 0F/0M/0m, §6 |
| Common global mod-16 bits, transversals, and equal weights | SUPPORTED conditional on the transported factors; 0F/0M/0m, §7 |
| `Φ16(X^25)` factorization, actual P-row pairing, and constant rows | SUPPORTED conditional on P's T2 and cyclotomic inputs; 0F/0M/0m, §8 |
| Two final complement equations and the period-6 contradiction | SUPPORTED under the established branch hypotheses; 0F/0M/0m, §9 |
| Head sizes 25 and 50 | SUPPORTED by the separately stated cardinality generalization in §10, conditional on the cyclotomic degree/irreducibility input but not LL/T2; 0F/0M/0m |
| Wording/truth of the external LL result, full cyclotomic source foundations, and the actual-code border caller | INCONCLUSIVE: not independently source-checked; exact assumptions and boundaries in §11 |

## 1. Frozen-input and process receipt

The **first research artifact** was the assigned manifest. Its full measured SHA-256 was `cfbbe3555cc1ce9a3c8b457fe2ffb98a5b686794746fff8b715b57162f3aaaa0`, exactly the assignment. The manifest was displayed, including its untruncated scope and requirements. Before opening either input body, I measured and compared **both** declared files:

1. `dispositions/math-5-shor-single-small-shared-prime-head-exclusion-conditional-parent-v1.md`: SHA-256 `c1c4c95dc4f399fbcb9cc3356b0d415778f8a496e9417c9e8828c3ecf27ea8aa`, 3,637 bytes, 13 LF; all match. Its role is adopted LL/T2 import context only, **not** its theorem.
2. `mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-arbitrary-tail-head100-high-modulus-obstruction-v1.md`: SHA-256 `9ed4749c165a2aef8ab463f54248ed25533d6c8523c09ac085227076665f9eaa`, 20,968 bytes, 218 LF; all match.

Actual complete raw displays, in manifest order, were: input 1, `1–13`; input 2, `1–15`, `16–30`, `31–45`, `46–60`, `61–75`, `76–90`, `91–105`, `106–120`, `121–135`, `136–150`, `151–165`, `166–180`, `181–195`, `196–210`, `211–218`. The last display included the target's `END OF ARBITRARY-TAIL HEAD-100 HIGH-MODULUS OBSTRUCTION` ending. No mathematics or controls were undertaken until all these displays completed. Source §8 was displayed because the entire input was required; its same-author control results were not used as evidence.

**PROCESS MINOR:** the general memory-summary-first routing instruction was consulted after the manifest and frozen input displays, rather than first. This did not change the specified source identities, all-inputs-before-reasoning sequence, or allowed mathematical premises. One attempted control-launch wrapper was rejected because its working directory was reported nonexistent; no control program ran in that attempt. The actual run below used an absolute path and completed. No author code was run, imported, or compiled; no linked paper, sibling review, held body, solver result, external model/search/API, author contact, Git operation, deletion, or publication was used.

## 2. Elementary reduction, with all quantifiers

Write `P(X),Q(X)` for masks of representative residues. In the group algebra over `F_l`, for `l∤|P|` the tiling identity gives `P^l Q = |P|^(l−1)G = G`, where `G` is the sum of all group elements. The corresponding nonnegative integer coefficients are `1 mod l` and total `n`, so all equal one. This proves both `lP⊕Q=Z_n` and injectivity on `P`. Iteration gives the same for any multiplier coprime to `|P|`; it also applies with the factors interchanged. If two nonzero differences have the same gcd `g<n` with `n`, a unit modulo `n` lifting the quotient of their unit parts sends one difference to the other, and dilation contradicts uniqueness.

The head differences `8,3,5,11` and tail difference `1` force `2·3·5·11 | n`: if a listed prime were absent from `n`, the corresponding head difference and `1` would have equal gcd 1. If `3`, `5`, or `11` failed to divide `|Q|`, dilating `Q` by that prime would make its `0,1` difference collide with the corresponding actual head difference. Hence `3·5·11 | |Q|`. Under `|P|=100`, necessarily

`n=2^K 5^v R`, `|Q|=2^(K−2)5^(v−2)R`, `K≥2`, `v≥3`, `R` odd, `5∤R`, `33|R`.

Since `gcd(R,100)=1`, `RP⊕Q` tiles. Restriction to each coset of `R Z_n` gives `|Q_r|=|Q|/R`, so every class modulo 33 has exactly `w=|Q|/33=2^(K−2)5^(v−2)R/33>0` elements, even when `R` has repeated primes.

For an odd tail difference `d`, if `5|d` but `25∤d`, set `g=gcd(d,n)` and dilate `P` by the odd 5-free multiplier `g/5`; the actual head difference 5 then has gcd `g`, impossible. If `5∤d` but `3|d` or `11|d`, the same argument uses `g/3` or `g/11` and the head difference 3 or 11. Thus **opposite-parity Q elements agreeing modulo 3, 5, or 11 agree modulo 25**. This conclusion uses actual differences and does not presume a special tail.

## 3. Class parity, all literal anchors, and `f`

No even tail is `1 mod 3`: comparing it with odd anchors 1 and 7 would require two different residues modulo 25 (anchor 13 gives a third). All class statements below have witnesses because every mod-33 class has `w>0` elements.

* Class `3 mod 33` cannot be odd: its comparisons to even anchors 0 modulo 3 and 14 modulo 11 would give residues 0 and 14 modulo 25. Class `25 mod 33` is odd and has residue 14 modulo 25 by anchor 14; comparing it to class 3 makes class 3 have residue 14 modulo 25.
* Class `11 mod 33` cannot be odd: comparisons to anchors 14 modulo 3 and 0 modulo 11 give 14 and 0 modulo 25. Class `22 mod 33` is odd and has residue 0 modulo 25 by anchor 0; comparison makes class 11 residue 0 modulo 25.
* An odd class-0-mod-3 tail would compare to 0 and to class 3, forcing 0 and 14; an odd class-2-mod-3 tail would compare to 14 and class 11, forcing 14 and 0. Therefore `q odd ⇔ q≡1 (mod 3)`.

For each `j mod 11`, every tail of label `j` has one residue `f(j) mod 25`: choose occupied classes of both parities with that label and compare across parity. If two `f` values agree mod 5, opposite-parity representatives show they agree mod 25. The following checks **all five** literal tail anchors, including zero and both even anchors; `E/O` denote the eventual even/odd mod-16 supports, not an additional premise.

| actual q | parity and mod 3 | mod 11 | mod 25 | mod 16 | later support |
|---:|---|---:|---:|---:|---|
| 0 | even, 0 | 0 | 0 | 0 | E |
| 1 | odd, 1 | 1 | 1 | 1 | O |
| 7 | odd, 1 | 7 | 7 | 7 | O |
| 13 | odd, 1 | 2 | 13 | 13 | O |
| 14 | even, 2 | 3 | 14 | 14 | E |

Thus `f(0)=0`, `f(1)=1`, `f(7)=7`, `f(2)=13`, `f(3)=14`. These five values represent all five mod-5 classes. Consequently every other `f(j)` is one of `{0,1,7,13,14}`; the remaining six labels are **not** assumed to follow a selected pattern.

## 4. Nonvanishing and actual head saturation

For `ω=±1`, `τ∈μ3`, `η∈μ11`, `ξ∈μ25`, the actual tail counts give

`Qhat(ω,τ,η,ξ) = w(1+τω+τ²) Σ_(j=0)^10 η^j ξ^f(j)`.

The second factor is nonzero for every `ξ≠1` and every allowed six-label completion. If `η≠1`, its degree-10 minimal polynomial over `Q(ξ)` is `Φ11`; vanishing of the degree-at-most-10 polynomial in `η` would make all 11 coefficients equal, but the `j=0,1` coefficients are `1,ξ`. The degree follows from the named irreducibility/degree input: for order `5^a`, `a=1,2`, the joint field is `Q(ζ_(11·5^a))`, whose degree divided by `φ(5^a)` is 10. If `η=1` and `ξ` has order 25, the nonzero sum has degree at most 14 while `deg Φ25=20`. If `η=1` and `ξ` has order 5, the five integer coefficients sum to 11 and cannot all be equal; a vanishing degree-at-most-4 polynomial would be a multiple of `Φ5`.

For `τ=1, ω=±1`, the prefactor is `2+ω≠0`; for primitive `τ` and `ω=−1`, it is `−2τ≠0`. Since the tiling product vanishes at every nontrivial character, Fourier inversion gives, for every parity and `j mod 11`, counts of P uniform over the 25 residue classes, and for each mod-3/mod-11 cell the even-minus-odd P count independent of the mod-25 residue.

The head anchors `0,11,3,8` occupy four distinct `(parity,j)` buckets. Each bucket has at least one element in **every** mod-25 class, so the 100-element budget gives exactly these four buckets, one element per class in each. The two single-parity buckets have fixed mod-3 labels: row 3 has label 0 and row 8 has label 2. In the two `j=0` rows the signed-vector invariance says either their mod-3 labels coincide for each `z`, or they are a fixed distinct ordered pair. In the coincident alternative, project the **actual** tiling to `Z_2×Z_3×Z_11×Z_25`: each target has `n/(2·3·11·25)=2w` actual representations. At parity 0 and mod-3 target 0, rows 3 and 8 are incompatible with the tail-parity rule; exactly one of the two `j=0` rows contributes `w`, for every target `j,z`. This is a contradiction. The distinct alternative is anchored by 0 and 11, hence the row labels are 0 and 2. Therefore

`P mod 66 = 25·{0,3,8,11}`,

with exactly one actual P element in **each** of the four rows for **each** mod-25 residue. The projected twofold object is only a necessary representation-count relaxation, **not** asserted to be a tiling.

## 5. Cyclotomic ownership and transport to actual fibres

The named LL/T2 statement is invoked for both factors: only primes 2 and 5 can divide `|P|`, so at most two distinct primes are shared. Conditional on that statement, both masks satisfy T2. The nonvanishing above forces P to own `Φ5` and `Φ25`. The parity rule gives `Q(−1)=22w−11w=11w≠0`, so P owns `Φ2`.

For each `1≤i≤K`, `Φ_(2^i)` divides at least one mask by the tiling identity. Distinct irreducible factors multiply inside each integral mask; evaluation at 1 bounds their number in P by 2 and in Q by `K−2`. The sum of these upper bounds equals K, so every such factor is owned exactly once. Thus P owns `Φ2` and precisely one further `Φ_(2^s)`, `2≤s≤K`, and Q owns all remaining 2-power factors. Likewise, for every `l^j|R`, `Φ_(l^j)` must belong to Q because `l∤100`.

Fix any 2-power factor `Φ_(2^i)` owned by Q. T2 combines it with the Q-owned prime powers of the distinct primes dividing any `d|R`, including repeated-prime exponents separately, to give `Φ_(2^i d)|Q`. For odd `R`, the root orders in `1+X^(2^(i−1)R)` have exact 2-part `2^i`, and hence

`Φ_(2^i)(X^R) = ∏_(d|R) Φ_(2^i d)(X)`.

Write `Q(X)=Σ_(r=0)^(R−1) X^r F_r(X^R)`. Because the product on the left divides Q and `1,X,…,X^(R−1)` are a free residue basis over `Z[X^R]`, monic division implies `Φ_(2^i)(T)|F_r(T)` for **every** `r`; no aggregate-fibre substitute is used. Since R is odd, raising a primitive `2^i`-th root to R preserves its order, so the original-exponent mask of every actual `Q_r` also owns `Φ_(2^i)`. After folding modulo `2^i`, this is exactly equality of counts at residues `x` and `x+2^(i−1)`.

The further even-difference rule is also actual: if `5∤(q−q')` and `gcd(q−q',n)` has exact 2-part 8, then `t=gcd(q−q',n)/8` is odd and 5-free, hence coprime to 100, and the dilated head difference `8t` has the forbidden same gcd. For `K≥4` the exact condition is a difference `8 mod 16`; for `K=3`, divisibility by 8 suffices.

## 6. All allocation cases before the final branch

* `K=2`: `gcd(3·8,n)=gcd(13−1,n)=12`; dilation of P by 3 is allowed, contradicting equal-gcd exclusion.
* `K=3, s=2`: Q owns `Φ8`. In the actual fibre of anchor 13, its mod-8 residue 5 is paired with residue 1. That tail is 13 mod 25, whereas anchor 1 is 1; their difference is divisible by 8 and not by 5.
* `K=3, s=3`: Q owns `Φ4`. In the fibre of anchor 7, residue 3 mod 4 forces a tail residue 1 mod 4. It is 1 or 5 mod 8, so compare to anchor 1 or 13 respectively. Its mod-5 residue is 2, versus 1 or 3.
* `K≥4, s∉{3,4}`: Q owns `Φ8,Φ16`. In the fibre of anchor 13, `Φ8` supplies residue 1 mod 8, and `Φ16` supplies actual residue 9 mod 16. Compare with anchor 1, which is 1 mod 16; their mod-5 residues differ.
* `K≥4, s=3`: Q owns `Φ4,Φ16`. In the fibre of anchor 7, `Φ4` supplies residue 1 mod 4. If it is 1 mod 8, `Φ16` supplies residue 9 mod 16 to compare with anchor 1; if it is 5 mod 8, `Φ16` supplies residue 5 mod 16 to compare with anchor 13. The fibre's mod-5 value 2 differs from both anchors' values.

Each cited fibre has fixed `f(j)` because R is divisible by 11; each claimed pairing is a positive-count consequence, not a presumed elementwise involution. The surviving case is exactly `K≥4`, P owns `Φ2,Φ16`, and Q owns `Φ4,Φ8`.

## 7. Actual mod-16 support and all transversals

Each `Q_r` has fixed parity because R is divisible by 3. Its `Φ4` condition equalizes its two classes of that parity mod 4; `Φ8` equalizes each mod-8 class with its translate by 4. Together all four mod-8 classes of that parity have the same positive count. Every permitted parity and every `j mod 11` occurs by the class counts. In particular, at each such parity/mod-8 coordinate, actual tails occur with each of the five anchored `f`-values, which are pairwise distinct mod 5.

If two different values used opposite mod-16 lifts of this coordinate, their difference would be 8 mod 16 and nonzero mod 5, violating the even-difference rule. A single value cannot use both lifts either, since another value occurs and would conflict with one of those lifts. Consequently **all** actual tails at that parity/mod-8 coordinate use one common lift, regardless of their mod-3, mod-11, or mod-R labels.

Let E and O be the resulting four even and four odd mod-16 residues. They are transversals of the two lifts of every mod-8 residue of their parity:

`E ⊔ (E+8) = {0,2,4,6,8,10,12,14}`,

and analogously for O among odd residues. Summing equal mod-8 counts over the constituent `Q_r` gives exactly `w/4` tails at each element of the appropriate support in every actual mod-33 class. In particular `4|w`. No special tail has been assumed. Every nonzero even translation of `Z_16` generates a subgroup containing 8, so `E` has trivial stabilizer under even translations: otherwise `E=E+8`, impossible by the displayed disjointness.

## 8. T2 factorization, all actual P-row pairs, and constants

P owns `Φ16,Φ5,Φ25`. T2 gives `Φ80` and `Φ400`. Distinct irreducible factors multiply; using exact polynomial identities,

`Φ16(X)=1+X^8`,
`Φ80(X)=(1+X^40)/(1+X^8)=1−X^8+X^16−X^24+X^32`,
`Φ400(X)=(1+X^200)/(1+X^40)=1−X^40+X^80−X^120+X^160`.

Thus their product is `Φ16(X^25)=1+X^200`. Decompose `P(X)=Σ_(z=0)^24 X^z H_z(X^25)`. The same monic residue-basis argument yields `Φ16(T)|H_z(T)` for **every** z. Since `gcd(25,16)=1`, the original-exponent mask at fixed z has equal counts at `r` and `r+8 mod 16`. It has exactly two even and two odd actual elements, one in each anchored row, so for all 25 classes

`p_8(z)=p_0(z)+8` and `p_11(z)=p_3(z)+8 (mod 16)`.

The projection to `Z_16×Z_3×Z_11×Z_25` is legitimate because its order divides n; every target has exactly `n/(16·3·11·25)=w/4` actual representations. Fix target mod-25 value z and mod-11 value J. At parity 0, mod-3 target 2, the only head/tail-mod-3 pairs are `(row 0,2)` and `(row 8,0)`. Each relevant Q class has weight `w/4` on each of its E residues. Hence the E translates by

`p_0(z−f(J))` and `p_8(z−f(J−8))`

must be disjoint and cover the even residues. The unique complementary translate of E is E+8, and E has no nonzero even stabilizer. With the P-row pairing, this forces `p_0(z−f(J))=p_0(z−f(J−8))`. Taking J=0 uses `f(0)=0, f(3)=14`; translation by 14 generates `Z_25`, so `p_0` is constant. Anchor 0 gives `p_0≡0`, and `p_8≡8`.

At parity 1, mod-3 target 2, the only pairs are `(row 3,2)` and `(row 11,0)`. The same argument gives `p_3(z−f(J−3))=p_3(z−f(J))`; J=3 again gives the unit shift 14. Anchor 3 gives `p_3≡3`, and `p_11≡11`. Thus **every actual P element**, not merely an aggregate count, has mod-16 residue equal to its row anchor.

## 9. Final two target classes and contradiction

For parity 0, mod-3 target 0, the only pairs are `(row 0,0)` and `(row 11,1)`. Their supports E and `11+O` each have weight `w/4` and partition the even residues. The E complement is E+8, so

`11+O=E+8`, hence `O=E−3`.

For parity 1, mod-3 target 0, the only pairs are `(row 3,0)` and `(row 8,1)`. Their supports `3+E` and `8+O` partition the odd residues, giving

`8+O=3+E+8`, hence `O=E+3`.

Therefore `E=E+6`. But the subgroup generated by 6 modulo 16 contains 8 (`4·6≡8`), forcing `E=E+8`, contrary to its transversal disjointness. This is the promised contradiction for the final high-modulus branch. The calculations use the exact multiplicity `w/4` of the **actual** tiling, not a presumed quotient tiling.

## 10. Head sizes 25 and 50

The candidate's smaller-head corollary is not merely a consequence of assuming `|P|=100`; it requires reapplying the earlier derivation. For `|P|=25` or 50, the same anchor argument forces 330 to divide n and 3,5,11 to divide `|Q|`; write `n=2^K5^vR` with `R` odd, 5-free and divisible by 33. Dilation by R remains legal, and every mod-33 class has `w=|Q|/33>0` tails. The odd-tail rule, the parity graph, all five values of `f`, and the Fourier nonvanishing proof remain valid because the relevant multipliers are odd and 5-free. The four distinct head parity/mod-11 buckets therefore each contain at least one element for each of 25 residues, forcing `|P|≥100`, a contradiction. This argument does not use LL/T2. It still uses the named cyclotomic field-degree and irreducibility inputs.

## 11. Exact conditional imports and residuals

1. **Łaba–Londner, arXiv:2106.14042v3, Corollary 6.2**: the externally stated assertion that, for a cyclic tiling with at most two distinct primes common to both factor cardinalities, **both** factors have T2. **Coven–Meyerowitz T2**, as stated in the candidate and its cited Theorem 1.1, means that products of any owned prime powers of distinct primes divide that factor's mask. The external text, hypotheses, scope, and ancestry were not opened or independently verified. Conditional on exactly that quoted formulation, the application and fibre transport are reconstructed in §5; a weaker or differently scoped result would leave that step open.
2. **Classical cyclotomic irreducibility and `deg Φ_m=φ(m)`**, including coprime-conductor compositum/degree, are named conditional imports. The particular `Φ16/Φ80/Φ400` factorization and the odd-R root-order identity are reconstructed above; finite arithmetic checks do not independently establish all the classical input.
3. **Actual-word border caller**: the Restivo–Salemi–Sportelli border theorem as stated by Cordero, arXiv:2301.13566v1, p. 3, Theorem 1.1, is an unverified separate conditional caller for the literal Shor code and finite UD factor-complete extension with a pure-`a` atom. The cyclic-tiling argument does not depend on the caller, and an arbitrary cyclic tiling is not asserted to produce a code.
4. Neither the adopted context's smaller-head theorem nor any f220/f232/sibling mathematical conclusion was imported. The declared context supplies only the authorized LL/T2 formulation. Conditional support here is confined to the stated head-cardinality slice; heads of size at least 200, other head families, original unrestricted completion, and novelty remain outside this review.

## 12. Reviewer-owned exact controls and negative controls

I wrote `reviewer-control-highmod.py` in this wave only; it imports only Python standard-library arithmetic/iteration, not author code or scientific source files. Its measured full SHA-256 is `14480a66ef711660a210bfcb5cbeb29e97cbe8edbda3d9a402a4977a67352495`. The actual bounded invocation was `python3 -I -B` on that absolute path, with the tool's 120-second cap. `/bin/date` recorded start `2026-10-29T14:02:29-0700 PDT` and end `2026-10-29T14:02:29-0700 PDT`; observed exit was **0**, not a timeout.

The control independently used integer monic division to obtain `Φ16,Φ80,Φ400` and multiply them exactly; it checked 15 sample odd-R transport identities, including R=9, 15, 33. Across 13,122 fixed-parity vectors with entries 0–2, 114 nonempty vectors of each parity satisfied both fibre constraints, all with uniform positive mod-8 counts. Of 243 five-value bit-support patterns, precisely 2 survived. Of 4,096 labelled head residue tuples, 64 satisfied the `Φ16` pairing. Binary mod-16 anchor-fibre checks admitted 2 `Φ8+Φ16` and 3 `Φ4+Φ16` support patterns, each satisfying its stated required anchor comparison. The four target pairings were explicitly enumerated. All 16 E and 16 O transversals and 256 allowed same-E partition offsets were checked; imposing all five Q anchors left 8 pairs, one satisfying each individual final equation, and none satisfying both. The `14 mod 25` orbit had size 25.

Intended-reason negatives: changing the sign at `X^8` in `Φ80` produced a nonzero `X^8` coefficient; taking even R=2 broke the odd-R factorization by an extra `Φ16`; dropping `Φ4` or `Φ8` respectively allowed a fibre without the asserted uniformity; opposite bits for two distinct f-values were rejected, while a single f-value alone did not force a single bit; duplicating the even head residue violated the `Φ16` counts; dropping the relevant factor in each anchor-fibre route removed its necessary conclusion; the full even universe is period-6 invariant but fails `E∩(E+8)=∅`; and a nonconstant row violated the 14-shift equality. These finite, bounded controls are diagnostics of the written deductions, not proof of arbitrary-n tilings or verification of the external imports. The full-file SHA-256 of this review is supplied in the detached handoff/receipt after its bytes are fixed.
