# f154 — Independent same-harness written review of Theorem P2

## Verdict and exact scope

**NO SUBSTANTIVE DEFECT FOUND: 0 FATAL / 0 MAJOR / 0 MINOR.** No missing proof case identified. The exact-scope conclusion is supported by an independent written reconstruction and reviewer-authored bounded exact controls, not by the author's reported PASS/checker results.

Reviewed statement: for every odd prime p, a word with F=3p−2 reflection occurrences, R≥p+1 rotation occurrences, singleton cyclic reflection gaps, and exactly o_π=p+2 odd cyclic reflection-projection runs has an original-linear-order identity subsequence of exactly 2p letters, consisting either entirely of reflections or of exactly two rotations and 2p−2 reflections. Rotation exponent 0 is permitted throughout.

This is a same-harness scientific review only: not independent-model-family, human, formal/kernel, or novelty verification. It is not an ordered-Olson result, a full L_RES result, a floor result, or an adoption of any held historical output. The separate conditional lower band mentioned in candidate §5 is **not reviewed or adopted** here. No conclusion for o_π≥p+4 follows.

## 1. Frozen inputs and read boundary

Manifest: `manifest-v1.json`, SHA-256 `6204853698b308eefb05025d008a21fa6ad229a2e2e14f4a879b22d118d8f374`, 2,741 bytes, 30 LF. The supplied manifest pin matched before interpretation.

The two scientific inputs were hash/byte/LF verified before interpretation, then read completely in the declared order:

| Order | Input basename | SHA-256 | Bytes | LF/full read |
|---|---|---|---:|---:|
| 1 | `frontier-20261028-olson-actual-block-fatal-correction-v1.json` | `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e` | 9,278 | 1–92 |
| 2 | `frontier-20261028-olson-p2-band-v1.md` | `2b02c24161f4cc2127ee180a0eebd6a03326a3428c6defbe176c80f9619046f1` | 13,059 | 1–83 |

All scientific source files are under `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/`. Both input hashes were checked again by the exact-control runner in the same declared order. The input full reads used raw ranges, including the full long lines.

**No floor, L_RES, historical actual-block counter, or actual-block lift is a mathematical premise.** The sole actual-block-related input opened was the mandatory correction above, used as a nontransfer/scope constraint, not as mathematical support. No file named within that correction was opened. The spare-sector manuscript named in the candidate was not opened or used. No author experiment/checker code or result file was opened, imported, or executed. Memory/policy skills were operational guidance only, not scientific premises. No Git, network, author contact, external model/API, publication, deletion, secrets, or infrastructure mutation was used.

## 2. Projection conventions reconstructed from the candidate alone

Write ρ_u=(u,0), σ_a=(a,1), with `(x,e)(y,b)=(x+(−1)^e y,e+b mod 2)`. Thus σ_aσ_b=ρ_(a−b), σ_aρ_v=σ_(a−v), and a product of k reflections is ρ_alt for even k or σ_alt for odd k, where alt is the alternating sum of labels in selection order.

The cyclic projection is obtained by deleting **all** rotations, then taking maximal constant-label cyclic runs of the reflection sequence. An occupied gap after a reflection is assigned to that reflection's projected run, including a run's trailing boundary gap. An occupied gap between equal reflection labels does not split a projected run. Singleton gaps mean at most one rotation occurrence after each reflection, equivalently no cyclically adjacent rotations. All run parity counts below are projection counts.

For two chosen rotation occurrences r1,r2, cut immediately before r1. Delete all unchosen rotations. X is the linear reflection sequence between r1 and r2; Y is the remaining linear reflection sequence after r2 back to r1. Pieces are maximal constant stretches **separately within X and Y**; endpoint pieces are not merged across a selected rotation. Distinct occurrences of the same group-valued rotation may be r1,r2: u=v is allowed.

If a cyclic cut of a selected word has product BA=1, its original-linear-order product AB is also 1 (a conjugate of BA). Thus cuts used in the proof do not reorder the final subsequence. Selecting reflection prefixes within pieces gives distinct occurrences; sorting them with r1,r2 by the original word's indices gives a genuine original-order subsequence.

## 3. Lemma C reconstructed (candidate LF 15–21)

For each nonempty piece π impose `k_π mod 2 = [π∈T]`. The least attainable total is |T|. The greatest is

`M = F − e_T − (o_pc−o_T)`.

Each piece independently supplies a nonempty arithmetic progression of step 2, so their sum supplies **every** total of the correct parity from |T| to M. Since |T| is even, `|T|≤2p−2`, and

`M≥2p−2  ⇔  o_T−e_T≥o_pc−p`,

the required 2p−2 reflections can be chosen. This also verifies that even pieces selected oddly have enough length: a nonempty even piece has length at least 2.

Let a=alt(T_X), b=alt(T_Y). With |T_X| even, |T_Y| is even and the product is `ρ_(u+a+v+b)`. With |T_X| odd, |T_Y| is odd and the product is `ρ_(u+a−v−b)`. These are exactly the two equations stated. Thus both the capacity and the sign change on v and Y are necessary for this argument; neither can be omitted. The selected word has two distinct rotation occurrences and exactly 2p−2 reflection occurrences.

## 4. REF step, directed differences, and Lemma Q

**REF step (LF 23).** Each even run provides all its reflections as equal pairs; each odd run provides (L−1)/2 pairs and optionally one singleton. The total pair count is `(F−o_π)/2=p−2`. Four odd-run singletons with cyclic alternating label sum 0, plus all these pairs, give exactly `4+2(p−2)=2p` reflections. Every pair cancels in selection order after rotations are skipped. Cyclic-cut invariance transfers this identity to original order.

**D(t) (LF 25).** For t≠0, if no ordered pair has difference t, first occurrences would require every x−t to precede x. Since nonzero t generates F_p additively, this gives a strict ordering cycle. Thus D(t) exists. The t=0 branch is handled separately by two repeated c-labelled occurrences, not by this argument.

**Three-c tool (LF 27).** With τ≠c, two of three c occurrences lie on one side of τ, yielding `(c,c,τ)` or `(τ,c,c)`. With τ=c use three distinct c occurrences. Their alternating sum is τ.

**Lemma Q (LF 31–33): independently checked all four multiplicity steps.** Four equal labels give a zero quadruple. Three a's and two b's give a cyclic a,a,b,b order by dividing at the b's. Two doubled distinct labels therefore must interleave a1,b1,a2,b2. If no value is tripled and s values are doubled, support is p+2−s and s≥2. Fix a doubled a. For every other doubled b, x=2a−b is distinct from a,b because p is odd. In each of the four open arcs between a1,b1,a2,b2, an occurrence of x gives one of the displayed zero quadruples (the arc (a1,a2) is covered on both sides of b1). Thus s−1 distinct x values are absent. Only s−2 values can be absent, contradiction. A tripled c therefore exists; no other value can repeat, and the remaining p−1 entries are exactly F_p\{c}.

Consequently the proof's dichotomy is exhaustive: the odd-run label sequence has a zero quadruple and REF finishes, or its multiset is c×3 plus every other field value once. The sharper AP-shape observation in candidate §5 is not needed or adopted as a general theorem.

## 5. Every H case, including γ (candidate LF 42–50)

Let G=P⁻ r1 X r2 P⁺, lengths a≥1, x≥1, b≥0. Singleton gaps ensure x≥1. Other projected runs remain whole pieces of Y; P⁺, when nonempty, is first and P⁻ is last. Put S equal to the other odd-run pieces, e=label(G), s=u+v. Direct piece counting gives

`o_pc−p = 2−[G odd]+#odd{a,x,b}`.

If G is even, S contains c three times and every other value once. If G is odd, deleting its singleton label leaves either c twice and all other values (e=c), or c three times and every value except e (e≠c).

| Case | Capacity target | Independent equation/count check |
|---|---:|---|
| H-i: G even; a,x,b even | 2 | T_X empty; two odd S pieces with alt −s. D(−s) works for s≠0; two c's for s=0. | 
| H-ii: G even; x odd | 4 | Exactly one of a,b is odd. T_X={X}; three S pieces have alt τ=u−v+e. Four odd T pieces, `u−v+e−τ=0`. |
| H-iii: G even; x even, a,b odd | 4 | T_Y=(P⁺,y,y′,P⁻), y−y′=s. Its alt is e−y+y′−e=−s. All four are odd pieces. |
| H-iv-a, ordinary: G odd; only x odd; β=e+u−v in S | 2 | T_X={X}, T_Y={β}; two odd pieces and `u−v+e−β=0`. |
| H-iv-a, γ: β absent from S | 2 | Necessarily e≠c, β=e, u=v. T_Y=(P⁺,c,c) if b>0, otherwise (c,c,P⁻). The P piece is nonempty **even**, so `o_T−e_T=3−1=2`, not 4. Its alternating sum is e. When b=0, a even and a≥1 imply a≥2, so P⁻ is available. |
| H-iv-b/c: G odd; x even; exactly one of a,b odd | 2 | S plus the odd P-piece contains all field values and a duplicate. D(−s) or equal labels supplies two odd Y pieces. This covers both a odd/b even (including b=0), and a even/b odd. |
| H-v: G odd; a,x,b odd | 4 | T_X={X}. If τ=e, use (P⁺,c,c), using two c's of S. Otherwise τ∈S, and Y has ≥3 c-labelled odd pieces (3 in S when e≠c; 2 in S plus both P pieces when e=c). The three-c tool supplies alt τ. |

The even-G parity patterns are exactly eee, ooe/eoo, and oeo; the odd-G patterns are eoe, oee/eeo, and ooo. Thus none is omitted. Every construction has |T|=2 or 4, including γ, so `|T|≤2p−2` for every odd prime p≥3. The capacity inequality is an equality in each listed case.

## 6. Sectors: both A and B, λ=0,1,2 (candidate LF 54–67)

With at most one occupied gap per projected run, the stated canonical spare is in that odd run's odd piece after cutting at its unique gap; with no gap it is the last reflection. There is one spare per odd run. For the two selected rotations in distinct runs G1,G2, an odd run contributes exactly one odd piece. An even run cut after an odd-indexed reflection contributes two odd pieces; otherwise it contributes none. Hence

`o_pc=p+2+2λ`, so the capacity target is `2+2λ`.

Every spare corresponds to one odd piece and different spares correspond to different pieces. This is why selecting labels among spares is legitimate for Lemma C, not merely a count of points in a circle.

**A: two rotations in one sector.** Choosing the first two leaves no spare between them. An odd G1 has its spare in G1⁻ and an odd G2 in G2⁺; all spares are in Y. X's only odd pieces are the λ even-run split pieces.

* λ=0: D(−s) or two c-spares in Y; |T|=o_T=2 and even equation `s−s=0`.
* λ=1: X has one odd split piece of label e. Its contribution is e; the three-spare tool in Y gives τ=u−v+e. Four odd T pieces, giving the odd equation and capacity 4.
* λ=2: X's odd pieces are e1,e2; Y begins with e2 and ends with e1. Select T_X both and T_Y=(e2,y,y′,e1), with spare difference y−y′=s. Then `alt T_X+alt T_Y=(e1−e2)+(e2−y+y′−e1)=−s`. Six distinct odd pieces meet target 6.

**B: at most one rotation per sector.** There are p+2 sectors and p+1≤R≤p+2, so at most one is empty. At most two of the three c-spares border it; some c-spare z borders two nonempty sectors. Their rotations surround exactly the spare z. Y's remaining spare labels are c twice and every other value once, hence contain all of F_p.

* λ=0: T_X is z's odd piece, with label c; choose a Y spare of label c+u−v. Two odd pieces give the odd equation.
* λ=1: T_X is z plus the odd split piece, in their actual X order; its alt is ±(c−e). Choose T_Y with directed difference `−(s+alt T_X)`, or c,c when this is 0. Four odd pieces give the even equation.
* λ=2: X's odd pieces are e1,c,e2. Y starts with odd e2, followed by all its spare pieces. Put τ=u−v+e1−c+e2 and choose spare difference y−y′=e2−τ. T_Y=(e2,y,y′) has alt τ, giving the odd equation with six odd T pieces.

In both λ=2 cases, G1,G2 are distinct even runs. At p=3, F=7 and o_π=5 leave at most one even run, so λ=2 is impossible. At p≥5, `6≤2p−2`. All λ=0,1 cases have |T|=2 or 4, valid already at p=3. Nonempty split pieces and the required ordering of all Y spares follow from the cut construction. This closes both A and B with no missing λ branch.

## 7. Reviewer-authored exact controls: scope and observed results

All scripts and receipts below are in this review directory and are independent of author checkers. Scientific checks used integer residue arithmetic, exhaustive reflection-index subsets and direct group multiplication, not an imported constructor or solver.

### 7.1 Lemma Q exhaustive normalized sequences

The C++ control fixes the first label to 0 by translation. Every pruned prefix has an explicitly detected zero quadruple; its p^remaining completions are counted. All surviving full sequences have the exact Q multiset. Translation invariance makes this a complete quotient enumeration, not a random sample.

| p | All normalized sequences | With zero quadruple | Without | Q multiset violations |
|---:|---:|---:|---:|---:|
| 3 | 81 | 71 | 10 | 0 |
| 5 | 15,625 | 15,597 | 28 | 0 |
| 7 | 5,764,801 | 5,764,747 | 54 | 0 |

### 7.2 p=5: exhaustive projection/gap enumeration, all rotation values certified exactly

A projection with an odd zero quadruple is already REF-covered by §4. For the remainder the control enumerates **all** zero-quadruple-free odd-label sequences (not a lemma-derived multiplicity filter), all possible even-run insertions, all proper cyclic adjacent run labels, and all run-length compositions summing to 13 with seven odd runs. There are at most p−2=3 even runs and the remaining length is distributed in pairs. Choosing an odd starting run and translating its label to 0 loses no projection.

Canonicalization uses only cyclic cuts and the group automorphisms `σ_x→σ_(a x+b), ρ_u→ρ_(a u)` for a≠0. Gaps and rotation values are transported bijectively. No reversal reduction is used.

Observed: 13,440 proper run presentations; 480 cyclic/affine projection classes without an odd zero quadruple. Direct enumeration of all ten-reflection subsets shows 471 classes already have a reflection-only identity and 9 do not. Each of those 9 was checked over all 5,812 occupied-gap masks with R≥6: **52,308 masks total**.

For each gap pair, the control independently enumerates all `C(13,8)=1,287` actual eight-reflection index subsets. Starting at the first selected rotation, literal group multiplication has form `u+v+A` or `u−v+A`, according to the number of selected X reflections. Thus exact attainable sets for u+v and u−v are computed from reflection subsets. A pair is universal if either set is the whole field; because p is odd the coordinates u+v,u−v are independent. This tests every p² rotation-value pair without looping over every full R-tuple; unselected rotations are simply skipped.

All 702 gap pairs (9×78) were universal. Every candidate-prescribed pair selected independently from each mask passed as well. **1,925** individual original-order two-rotation products, spanning all 25 value pairs for each sampled projection/branch, were multiplied directly. These are an exhaustive quotient/symbolic word control at p=5, not a claim to have explicitly listed all 5^R full exponent assignments.

### 7.3 p=7: bounded projection family, exhaustive masks within it

The exact bounded family is specified in `reviewer-exact-control-v1.cpp::bounded7`: odd labels 0,0,0,1,…,6, two or three inserted separating even runs, declared pair-length allocations, cyclic/affine deduplication, direct REF filtering, and deterministic per-(maximum-run-length,even-run-count) selection. It yielded **26** REF-failing projection classes; all are listed in `reviewer-stdout-p7-v1.json`. This is not all p=7 projections.

For each class, all `C(19,8)=75,582` masks with R=8 were checked: **1,965,132 masks**. Any larger occupied-gap mask contains such an eight-gap mask, so existence extends by skipping the extra rotations within these 26 projection classes. All 4,446 gap pairs (26×171) were universal, computed from all `C(19,12)=50,388` twelve-reflection subsets per projection. There were **12,103** literal original-order products over all 49 selected-rotation value pairs for sampled projection/branches.

The p=5/p=7 main controls exercised H-i/ii/iii/iv-a/iv-bc/v (including γ-available pairs), A/λ0, A/λ1, and all B/λ0,1,2. **A/λ2 was not represented in those REF-failing-only families**; it was not silently marked covered. The supplementary control explicitly constructed admissible A/λ2 full words at p=5 and p=7, used the stated six-piece recipe, and multiplied all 25/49 value-pair selectors in full original order. All 74 passed. This branch can arise even when some other REF selection also exists.

### 7.4 Lemma C, γ, complete-word embeddings, and the p=3 boundary

`reviewer-piece-control-v1.py` enumerates actual reflection subsets, records their piece-parity patterns, and compares that exact set with the capacity criterion. It then checks the stated signed equation against literal multiplication in **original**, not cut, order for every feasible parity pattern and every u,v. Results:

| p | Gap pairs | Actual reflection subsets | Feasible parity patterns | Literal equation/product comparisons |
|---:|---:|---:|---:|---:|
| 3 | 21 | 735 | 585 | 5,265 |
| 5 | 6 | 7,722 | 2,124 | 53,100 |
| 7 | 6 | 302,328 | 13,868 | 679,532 |

Both γ forms were constructed separately at p=7: b>0 uses P⁺ as the even T piece; b=0 uses P⁻. Each is a full F=19,R=8 singleton-gap word with o_π=9. The result records full letters, piece lengths, T, selected counts, strictly increasing original indices, and product (0,0). The γ-selected even piece is used oddly, as the proof requires.

`reviewer-sector-control-v1.py` also embeds 24 saved pair-control witnesses into full admissible R=p+1 words, inserts arbitrary additional rotations, maps every selected occurrence to its full original index, and multiplies again. All have exactly 2p selected letters and exactly two selected rotations. This explicitly checks that two-rotation subword witnesses survive their consuming full-word embedding.

For p=3 the supplementary control examines all 3^7=2,187 reflection vectors. Exactly **672** have o_π=5; every one has a six-reflection identity subsequence by direct subset multiplication. Thus this finite boundary requires no mixed selector, and no author p=3 check was assumed.

### 7.5 Intended-reason negative controls actually observed

* **Remove capacity:** at p=3, a recorded gap cut has o_pc=7 and T empty. The mutated rule retaining only even |T|≤4 would admit T, but its maximum reflection budget is 0, not 4; exhaustive actual subsets show that parity pattern unattainable. The missing cap requires 0≥4 and correctly rejects it. This is a parity-pattern mutation, not a counterexample to the unmutated theorem.
* **Use +v in the odd equation:** recorded p=3 witness u=0,v=2,T=15 satisfies the deliberately incorrect equation but literal original-order product is (2,0), not identity. The correct equation rejects it.
* **Change one selected rotation by +1:** every literal sample in the main controls and both full γ and supplementary full-word/λ2 controls becomes nonidentity for the same selector. This checks sign/value sensitivity; it does not assert the modified full word has no alternative selector.
* **Demand reflection-only in a REF-failing class:** all 9 p=5 and 26 p=7 retained classes fail the exhaustive 2p-reflection subset check, while their two-rotation selectors pass. This distinguishes the theorem's actual disjunction from the intentionally overstrong reflection-only mutation.

## 8. Receipts and reproduction boundary

Primary controls:

* Source `reviewer-exact-control-v1.cpp`, SHA-256 `aaf8580a299b4af46606dd2331870e59d5824e6ac46047d33cbb8f3113ec2c16`.
* `reviewer-receipt-q5-v1.json`: C++ compile exit 0; q5 process exit 0, 0.157 s; output SHA-256 `7dceed3e53445824117c225dc5ecebb4475b2c6dc41d0a180a5557c2f0b57313`.
* `reviewer-receipt-p7-v1.json`: p7 process exit 0, 2.011 s; output SHA-256 `1c2965886d492eee6487dc8e32bdbe9cc578c084bdf30bf26f9ff386fcd88755`.
* `reviewer-piece-control-v1.py`, SHA-256 `cf601f32468a6a9d92294494d251f45ad48b1e16cc8be4dfb636a128b156a86a`; process exit 0, 3.064 s; receipt/result `reviewer-piece-control-results-v1.json`.
* `reviewer-sector-control-v1.py`, SHA-256 `fa1ba4370f1c648dcd7b63218ebc5c9e96c7737bdd36516ad58b14e4e7bec976`; process exit 0, 0.012 s; receipt/result `reviewer-sector-control-results-v1.json`.

The runner/source/stdout/stderr/binary hashes, exact argv, clock readings, exits and native child RSS observations are in the receipts; measured RSS is not a claimed OS-enforced ceiling. The p5/p7 C++ stages had cooperative 240-second limits; no deadline/kill fired. Outputs are exclusive-create and no failed run was overwritten or hidden. The final artifact receipt binds the completed report and reviewer artifacts. No unrelated build, lint, repository test, or formatter was run; compiling the reviewer control was part of the explicitly assigned exact assay.

## 9. Final dependency and case census

Load-bearing dependencies: the candidate's group operation; projection/gap conventions; the elementary capacity progression and signed product calculation of Lemma C; REF pairing; directed differences over the prime field; three-c pigeonhole; the complete M1–M4 proof of Lemma Q; the H parity partition including both γ endpoint forms; and the canonical-spare/sector count with A/B and λ=0,1,2. All were reconstructed above. No omitted mathematical dependency or missing case was found.

The written general proof, not finite enumeration, supports the all-prime scope. The finite controls are separately qualified by their explicit domains. **Overall correctness at this exact scope: correct. Confidence: 0.97.** No transfer to the conditional lower-band assembly, historical held programs, actual-block applications, novelty, or full original-target closure is authorized by this review.
