# Shor code: no finite completion with pure-a order 1320

**Disposition: ACCEPT as a written, computer-assisted exclusion of one actual order.** Native clock observed before composing: **2026-10-28T20:02:03-0700 PDT**. This is same-harness verification, not a human, independent-model-family, formal/kernel or novelty certification. The original all-order finite-completion problem remains open.

## Exact adopted statement

No finite uniquely decipherable factor-complete code D containing the literal 16-word Shor code

`b{1,a,a⁷,a¹³,a¹⁴} ∪ {a³,a⁸}b{1,a²,a⁴,a⁶} ∪ a¹¹b{1,a,a²}`

can have `a¹³²⁰` as its actual pure-a atom. More strongly, there is no direct cyclic tiling `P⊕Q=Z₁₃₂₀` with `{0,3,8,11}⊆P` and `{0,1,7,13,14}⊆Q`.

This does **not** exclude every finite completion, establish the separate candidate order floor 1980, accept any order-660 or order-1980 result, or construct a completion. An incomplete six-head search and earlier uncertified Z3 UNSAT statuses are not premises.

## General code-to-border and arithmetic proof

Finiteness and factor-completeness force a pure-a atom: embed an a-run longer than twice the maximum atom length and inspect an interior atom. UD makes it unique, since two different pure-a words would give distinct factorizations of a common power. The actual b atom also rules out a longer pure-b atom.

For actual D atoms set `P={i mod n:aⁱbᵏ∈D,k≥1}` and `Q={j mod n:bˡaʲ∈D,l≥1}`. These include genuine multi-b atoms, not merely the one-b layer. The literal code supplies the stated anchors. Two representations of a residue produce two D factorizations of the same guarded word `bᴸaᴳbᴷ`; comparing the initial and terminal b-atom runs forces the same border atoms. Conversely, embed `bᴸaᵍbᴸ` for a sufficiently long a-gap in any chosen residue class. The atoms meeting its two guard boundaries are actual tail/head border atoms and all intervening atoms are powers of the unique a atom. Hence `P⊕Q=Z_n`, with `|P||Q|=n`. This reconstructs the necessary classical Restivo–Salemi–Sportelli border theorem in the present finite/complete/b-contained case.

For a direct cyclic tiling, primitive-root evaluation implies prime balance: if a prime divides n but not one cardinality, the other factor is uniform modulo that prime. Also nonzero P- and Q-differences cannot have the same gcd with n. Indeed a unit u can map either difference to the other. Cyclotomic irreducibility preserves all root-vanishing conditions under P→uP, so `uP⊕Q` remains a direct tiling, but that mapped difference creates a collision. This is the necessary direction of the classical Sands divisor-class theorem, reconstructed in writing rather than inferred from finite solver output.

## Exhaustive cardinality reduction at n=1320

The old head/tail difference gcd classes are `{3,5,8,11}` and `{1,2,6,12}`. Direct integer screens give 112 possible P residues and 286 possible Q residues. The retained 16 disjoint head conflict triangles and 130-clique tail partition prove `|P|≤80, |Q|≤130`. Product1320 leaves 13 possible P sizes; mod11 balance and heads0,11 exclude size11. The remaining twelve are

`12,15,20,22,24,30,33,40,44,55,60,66`.

Mod3 and mod5 capacities exclude `30,33,40,55,60,66`. Explicit forced-head blocking excludes15. For22, Q would be uniform modulo3 and5; parity and gcd5 conflicts force at least24 Q elements in a class whose quota is20. Thus only `12,20,24,44` remain.

For12, Q needs nine non-anchor entries in each of two 25-element mod11 classes. Independently exhaustive Hall counts give minimum neighborhoods18 for every nine-set on one side and17 for every eight-set on the other. Either leaves fewer than the required nine on the opposite side.

For20, mod5 balance forces P to use gcd264 by a six-pair matching. If Q avoided264, mod3/mod11 balance gives 91,125 possible six-element non-1-mod3 seeds. Exactly1,143 survive compatibility;1,089 cannot open22 required slots, and the remaining54 fail a required mod11 quota even under a permissive upper bound. No seed survives. Thus Q also uses264, contradicting Sands. The independently checked reduction leaves only `(24,55)` or `(44,30)`.

## The final two cases, independently checked by the parent

### |P|=24, |Q|=55

Because Q is odd, `Φ₂Φ₄Φ₈` divides P and P has exactly three elements in each mod8 class. Four classes each have exactly three screened candidates, forcing twelve heads in addition to the old four. All differences of these sixteen forced heads yield fifteen gcd classes. Screening Q against the actual old tails using **all** those known forbidden classes gives mod11 candidate counts

`(4,5,5,4,14,14,14,3,14,14,14)`.

Q must have five entries per mod11 class; classes0,3,7 already have too few. This parent/reviewer strengthening is a pure counting contradiction. The author's weaker 144-candidate relaxation was also independently rejected by two complete reviewer searches; the stronger proof does not need those searches.

### |P|=44, |Q|=30

P has four heads in each mod11 class. In two six-element classes, avoiding gcd55 forces heads155 and816, whose difference has gcd1, forbidden by the old tails. An independent exhaustive form finds61 admissible four-plus-four head choices and none avoiding55. Hence Q must avoid55.

Q needs six elements in each mod5 class and ten in each mod3 class. Its mod5 classes0,4 contain no 1-mod3 candidates under the five forbidden gcd classes. The other eight non-1-mod3 Q elements must be chosen from exactly twelve residues. There are495 seeds, of which21 are internally compatible. For every such seed, enumerate **all** internally compatible anchored six-subsets in classes0,4 and every pair of those subsets. There are104,112 pairs,156 meeting the mod3 quotas, and **zero** satisfying the cross-gcd test; in fact zero are cross-compatible even without balance. This necessary relaxation is impossible. Removing the cross test admits156 pairs, a positive sensitivity control; independent reviewer controls also provide a genuine gcd55-relaxed partial witness.

## Evidence, findings and limitations

The parent read the complete literal code definition, border/divisor/cardinality manuscripts, 116-LF final candidate and all four review reports. It reconstructed the same-code border, prime balance, Sands necessary direction, final cyclotomic/counting steps and the completeness of the final seed enumeration. The author final [candidate](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261028-1320-border-no-go-candidate-v1.md) is pinned at `52aeaff132fb0e59f9c735054b017df9471e543035ba0bfea1d3dcd04385869e`.

| Evidence | SHA-256 / exact scope |
|---|---|
| [f114 manifest](../review-waves/f114-shor-1320-two-border-sizes/manifest-v1.json) | `ad3f0ad3e4a7d80afa037fe238e791f267d993ba0c0cbf8945abe72224c30eaf` |
| [Written reduction review](../review-waves/f114-shor-1320-two-border-sizes/written-review-v1.md) | `938a03393a2b549eb906017826f189537544df906f9af5c3094014909151145e`;0F/0M/3m, complete general reconstruction and independent finite replay |
| [Finite reduction review](../review-waves/f114-shor-1320-two-border-sizes/finite-review-v1.md) | `01af31a82386d84803b8c5feae4f2a1d1ea74ff4f3d9d6d07403eb726df85208`;0F/0M/0m, all packing/Hall/seed facts |
| [f117 manifest](../review-waves/f117-shor-1320-final-cardinality-cases/manifest-v1.json) | `5ba7dfc08c681e28bb9e9d1f2ae6134bbf62f634061eb17c0e131b6d71258346` |
| [Size24 review](../review-waves/f117-shor-1320-final-cardinality-cases/size24-review-v1.md) | `4f42bebd6b4ae50a7b8907c6d313e638866192cbd3c579c0afea0cb04ebb6d9e`;0F/0M/3m |
| [Size44 review](../review-waves/f117-shor-1320-final-cardinality-cases/size44-review-v1.md) | `7bda5904ff6ac392cfea3c738294e62b6a296a49e58557efd1e002e56c9e192c`;0F/0M/4m |
| [Independent parent final-case checker](../review-waves/f117-shor-1320-final-cardinality-cases/parent-two-cases-exact-v1.py) | `9e69085ce373afc23a04f0d3458d5252455cac664b6e102d9a77942801b865de` |
| [Actual parent result](../review-waves/f117-shor-1320-final-cardinality-cases/parent-two-cases-result-v1.json) | `6d7346bcaea7a0eaaac382010026ba5abb25ba46010a934fdf99f2df08b87488`;executed20:00-era native observation19:59:39 PDT on2026-10-28, PASS |

The parent checker imports neither author nor reviewer code. It freshly derives both screens, forced gcd classes, every seed and every final pair. The earlier 112/286 packing/Hall/264 reduction has two independently written same-harness replay implementations; the parent final-case code is not asserted to replay that entire earlier reduction. All scripts use trusted exact integer arithmetic, gcd/combinatorics and their respective runtime/parsers; no proof assistant or independent hardware/model family verifies them.

The MINORs are explicitly qualified rather than silently edited: the earlier 'preceding17 possibilities' count is not supported by the frozen inputs and is unused; pure-a existence/uniqueness and the harmless n≥26 statement are supplied above or by the written review; omitted size24 constraints only weakened its search; author search-node figures are implementation-specific; the size44 relaxed witness changes the candidate universe and is not a solution of the original relaxation. Unreviewed graded multi-b tradeoffs, all-order divisibility/floors and later order1980 claims are not adopted. Classical border/Sands source statements were directly matched by the reviewer, but this is not an exhaustive priority or latest-status search.
