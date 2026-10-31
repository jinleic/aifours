# Spare-sector selector and the complete o_π<=p projection band (conditional on named inputs)

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 20:53:41 PDT 2026**. NEW **WRITTEN candidate** with bounded same-model checks (§5). It is not a reviewer verdict, formal proof, novelty claim, full L_RES result or ordered-Olson proof. Mandatory before-source: `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`. All run terms below are cyclic **reflection-only PROJECTION** terms; no historical actual `o_F/e_F` value, f111 finding, or floor is used or rehabilitated.

Conventions. Letters of D_(2p) are `ρ_y=(y,0)` and `σ_y=(y,1)` with `(x,e)(y,b)=(x+(−1)^e y, e+b)`. Hence `σ_aσ_b=ρ_(a−b)`, `σ_aσ_a=1`, rotations commute. A word W is cyclic for selection purposes: a cyclic rotation of an identity product is identity, so it suffices to exhibit an identity selection in some cyclic cut order. A rotation sits in the **gap** after the reflection immediately preceding it; the gap is **assigned** to that reflection's projected run (a run's gaps are those after each of its reflections, including the boundary gap after its last one). **Singleton gaps**: no two rotation letters are cyclically adjacent.

## 1. Lemma S (spare-sector selector)

Let p be an odd prime. Let W have exactly F=3p−2 reflections and R>=p+1 rotations, with singleton gaps. Suppose the cyclic projection has exactly p odd runs with pairwise distinct labels (so their labels are all of F_p), any number of even runs, and **every projected run is assigned at most one occupied gap**. Then W has an original-order identity subsequence of exactly 2p letters.

**Canonical spares and pairs.** For an odd run O with no occupied gap, pair its reflections consecutively from its start and call its last reflection its spare. If O has its (unique) occupied gap after its k-th reflection, cut O there into `O[1..k]` and `O[k+1..L]`; exactly one piece is odd. Pair each piece consecutively from its start; the spare is the last reflection of the odd piece. Every odd run yields `(L−1)/2` pairs and one spare, and no pair crosses its own occupied gap. For an even run, pair consecutively from its start; only a gap after an ODD-indexed reflection is crossed by one of these pairs.

**Sector choice.** The p spares cut the cycle into p open sectors; each of the R>=p+1 rotations lies in one, so some sector contains two rotations `r1` then `r2` (any two, in sector order). Let `u,v` be their exponents, `s=u+v`, and cut the word immediately before r1. Then no spare lies strictly between r1 and r2. By singleton gaps and the one-gap hypothesis, r1, r2 are assigned to DIFFERENT runs `G1≠G2`.

**Geometry.** G1 is contiguous and contains the reflection before r1; it cannot contain the reflection before r2. So `G1 = G1⁻ r1 G1⁺` where `G1⁺` lies between r1 and r2 and `G1⁻` is at the END of the cut. Likewise `G2 = G2⁻ r2 G2⁺` with `G2⁻` between r1 and r2 and `G2⁺` immediately after r2. Any odd run lying wholly strictly between r1 and r2 would have its spare there (its own gap, if any, is also there), which is excluded. If G1 is odd its spare is not in `G1⁺`, hence in `G1⁻`; if G2 is odd its spare is in `G2⁺`. So the cut order is

`r1 · [G1⁺] · [even runs only] · [G2⁻] · r2 · [G2⁺] · [all other runs, containing every odd spare] · [G1⁻]`,

and all p spares lie after r2. Unselected rotations are skipped; consecutive pairs never contain another selected letter between their two members, so each selected pair multiplies to 1 wherever it lies, PROVIDED it does not cross r1 or r2.

**Loss.** Let λ be the number of i in {1,2} for which `G_i` is EVEN and r_i follows an odd-indexed reflection of `G_i`. Cut each such `G_i` at r_i into two odd pieces, pair each from its start, and record their two extra spares. The remaining usable pairs number exactly `p−1−λ` (the projected capacity is `(F−p)/2=p−1`).

**Directed differences.** For t!=0 and any linear order of all of F_p there are positions i<j with `x_i−x_j=t`: otherwise every `x−t` precedes x, and following the additive cycle of t returns a strict inequality `pos(x)<pos(x)`. Apply this to the p odd spares, all after r2, in cut order. Write `D(t)` for such an ordered pair `(o_i,o_j)`, giving `σ_(o_i)σ_(o_j)=ρ_t`.

**λ=0.** If s=0 select r1,r2 and all p−1 pairs. If s!=0 select r1,r2, `D(−s)` and p−2 pairs. Product `ρ_s ρ_(−s)=1`; size `2+2+2(p−2)=2p` (resp. `2+2(p−1)`).

**λ=1.** Let the split even run have label c; one extra spare `x_out` (label c) lies after r2. If s!=0 select r1,r2, `D(−s)` and all p−2 pairs. If s=0 select r1,r2, `x_out`, the odd spare of label c, and all p−2 pairs; `σ_c…σ_c=1` in either order. Size `2p`.

**λ=2.** Then G1, G2 are even with labels α, β, extra spares `a⁺∈G1⁺`, `b⁻∈G2⁻` between r1 and r2 (in this order) and `b⁺∈G2⁺`, `a⁻∈G1⁻` after r2, with `b⁺` before every odd spare and `a⁻` after every odd spare. There are p−3 pairs; four more reflections are needed.
* If `β−α+s!=0`: select `b⁺`, `D(β−α+s)=(o_i,o_j)`, `a⁻`. After r2 the product is `ρ_(β−o_i+o_j−α)=ρ_(−s)`, so the total is `ρ_uρ_vρ_(−s)=1`.
* If `β−α+s=0` and s!=0: select `a⁺,b⁻` (product `ρ_(α−β)=ρ_s` between the rotations) and `D(−2s)`; `−2s!=0` since p is odd. Total `ρ_(u+s+v)ρ_(−2s)=1`.
* If `β−α+s=0` and s=0 (so α=β): select `a⁺,b⁻,b⁺,a⁻`; total `ρ_u ρ_(α−β) ρ_v ρ_(β−α)=ρ_s=1`.

Each case has size `2+4+2(p−3)=2p`. Returning the selected positions to increasing original order cyclically rotates an identity product. QED.

## 2. The o_π<=p band

**Band statement (conditional).** Let p be an odd prime and W have F=3p−2 reflections, R>=p+1 rotations and singleton gaps. If its cyclic projection has `o_π<=p` odd runs, then W has an original-order identity subsequence of exactly 2p letters — conditional on the named unreviewed inputs in case (c).

Since F is odd, o_π is odd, so either `o_π<=p−2` or `o_π=p`.

(a) `o_π<=p−2`: `(F−o_π)/2>=p` disjoint consecutive equal pairs give a reflection-only selector.

(b) `o_π=p` with two odd runs of equal label: their spares plus all p−1 pairs, reflection-only.

(c) `o_π=p`, distinct odd labels, and some projected run assigned two occupied gaps: its first two give an actual segment `σ_cρ_uσ_c(σ_c)^hρ_v` inside that run. For an ODD run use the joint candidate `frontier-20261028-olson-stretched-fourblock-exception-resolution-v1.md` (SHA256 `4c13a273997c6a02c97ab9b4b45bd36a80c5ebe0751c59450770ba33b76a58ac`) read BEFORE the complete `frontier-20261028-olson-stretched-fourblock-selector-v1.md` (SHA256 `ef44c034b01a924d0930f26e6c95b70972af31f9666340a06457ff40bc261e7f`); for an EVEN run use `frontier-20261028-olson-evenrun-stretched-selector-v1.md` (SHA256 `11160fe8f83af0d7b25932732c07c330ebbc2fd4550fe4051773a215e2b7cd03`) §1–2. These are unreviewed candidates, not adoptions.

(d) Otherwise every run has at most one occupied gap: Lemma S.

This subsumes, for its scope, the earlier `frontier-20261028-olson-all-odd-projection-band-v1.md` (SHA256 `a6cf2ea0b0bb63b54d3417f22b075294eaaf04e7608a3fb21ded266484d62d4b`, e_π=0), which is not edited. **Remaining open projection stratum of this band: `o_π>=p+2`.** Nothing here shows that stratum is empty, nonempty, or selector-free; no OLD/SEL/IPGEN/GS/DS3 failure is used; no full L_RES or ordered-Olson conclusion is claimed.

## 3. Review request

A NEW disjoint review should reconstruct Lemma S entirely (geometry, loss accounting, the six terminal cases) and the case split in §2, then separately review the cited inputs in their stated source order. No previous review, verdict or f111 assessment transfers.

## 4. What is not claimed

No claim about historical actual-block counters, about callers, about R=p+1 words with `o_π>=p+2`, about non-singleton gaps, or about novelty. The finite checks below are bounded, same-model and random; they are not exhaustive and not an independent mathematical review.

## 5. Exact bounded checks (fractions-free integer arithmetic mod p)

* `frontier-20261028-olson-spare-sector-full-experiment.py`, SHA256 `9479b5e610ed9b0cf68119df68ea0f85cd7045253ddf427a2a18adb4e1193c2c`, data `frontier-20261028-olson-spare-sector-full-results.json`, SHA256 `436e7d8e8589d7e5e5a682df43fb4c1ff90a9d6af29f1082896e89415cc97489`: 1500 Lemma S words, p=3,5,7,11,13, 1–4 even runs, arbitrary rotation values including 0, random linear cuts (270 malformed generation draws discarded before use).
* `frontier-20261028-olson-spare-sector-loss2-experiment.py`, SHA256 `9d6fb1f0ec6171fb2528e6b1b70fa1e383daf875243fffdedcd5e3211f6a5da9`, data `frontier-20261028-olson-spare-sector-loss2-results.json`, SHA256 `ab625b999caea57d0a930f2d582a20d8b0567ff0c4e28cdf85ad67824acd7136`: 840 targeted λ=2 words covering all three λ=2 sub-branches (the α=β sub-branch needs three even runs, impossible at p=3, hence absent there).
* Separately written checker `frontier-20261028-olson-spare-sector-checker.py`, SHA256 `abb6b82cee6bbadaa31b53c9bbf2cb6de430dedb1a65078a100116dc7fc51fd1`, imports no producer code. It recomputed counts, singleton gaps, the cyclic projection, distinct odd labels, one-gap-per-run, canonical spares, the sector condition, λ and the branch, required the selector to contain exactly the two named rotations, and multiplied every original-order selector. Result `frontier-20261028-olson-spare-sector-check-results.json`, SHA256 `5b5472dc5e8606d6c01bac4577f07d95eb8d6ddcbccb6f2844b00c785e0fbb01`: `PASS_INDEPENDENT_SPARE_SECTOR`, 2340 words; branches L0/s!=0 472, L0/s=0 64, L1/s!=0 784, L1/s=0 153, L2/I 323, L2/II/s!=0 304, L2/II/s=0 240; duplicate-index, altered-v and altered-branch controls failed as intended.
* Earlier partial exploratory runs in this root: one-even-run subcase producer `frontier-20261028-olson-one-even-one-gap-experiment.py` (SHA256 `df05140d669dfe53d015a77c256c031930a4dde000eeeae34eda93f873bc87bc`, data `1ea1e8df79abd40b81a1a25a07638e15ae3148443dfc2980fee4b18f1ad55e86`) with independent checker `frontier-20261028-olson-one-even-one-gap-checker.py` (SHA256 `ce54002909a567829847523cb1822ad8943970702bfc61a112bcf466129725d2`, result `277ee2934214df3a0ea4dfcbe0ea20491edcd4aeb9112d555d7df527fc99325b`, PASS 1000); and `frontier-20261028-olson-low-loss-spare-gap-experiment.py` (SHA256 `89291aa8b9634ab39ee6acf79453db2f765f67758c7e25570f7a5dd848c45fde`, data `6d791a190b296397a4d71cd44959683ad70c399819a1e161c28f3e6d0d62628e`), a producer-only λ<=1 run with NO separate checker, superseded by the two datasets above and not relied upon.

**END — Lemma S and the conditional o_π<=p band; o_π>=p+2 remains open.**
