# Independent in-harness review: ordered-four odd-run boundary

Native clock observed immediately before this report: **2026-10-28T19:29:52-0700 PDT**.

## Verdict and scope

- **Universal odd-prime scope: FATAL 0 / MAJOR 0 / MINOR 0.** I found no error in the written proof that every adjacent-distinct length-`p+2` sequence over `F_p`, for every odd prime `p`, has four increasing indices with alternating sum zero; in its lift to actual original-order reflection selectors for `F=3p−2`, `o_F=p+2`, `e_F≤1`; or in the stated raw-graph inequality under its actual hypotheses. The argument below is a written mathematical review, not a computer proof inferred from finite tests.
- **Separately conditional p=7 lower residual: FATAL 0 / MAJOR 0 / MINOR 0 for the conditional implication only.** Assuming both that the lower residual class has the cited actual-word, reflection-failure and raw-matching hypotheses and that the separately inherited floor `o_F≥p+2` applies to that class, the class is empty for `p=7`. I did **not** reconstruct, verify or prove that historical floor, its S(p)/Lev ancestry, or the earlier identification of the lower `L_RES` interface. These are imports, not conclusions of this review. Without the floor, the new inequality alone leaves the necessary profiles `κ=0`, `e_F∈{0,1}` at `p=7`; this is not a claim that any such failing word exists.
- This is one same-harness review, **not** an independent-family, human, formal/kernel, novelty, priority, full `L_RES`, full count-band, or original ordered-Olson closure certification. No author contact, external model, public search or additional source was used. The author checker was read but neither imported nor executed; its 600-case data and producer are not among the frozen inputs and were not independently reproduced here.

## Frozen input coverage

I read the assigned manifest first, then every complete listed input in its declared order, including the checker and its JSON receipt. Full SHA-256, byte count and LF count matched for all four; the manifest itself matched the assigned SHA.

| Input in declared order | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `written-releases/math-2-ordered-word-definitions-v1.md` | `010ef028f750f718df327102ec92e1803289169b512d361bf66ed2e28145c9fc` | 1,275 | 16 |
| `frontier-20261028-olson-ordered-four-odd-boundary-v1.md` | `7d4d356430303b1538cd1e621d0943ba9096be98fe3f53cce3184c7783a33fb5` | 10,262 | 98 |
| `frontier-20261028-olson-odd-run-boundary-checker.py` | `72325542919d2e5bd59ff3686717e221a42163354e2a318754c0142659f5d13b` | 5,241 | 136 |
| `frontier-20261028-olson-odd-run-boundary-check-results.json` | `34242dc9c388e44e24ee90d76abefa34cffe3bf6b2dcb5661c2e7f63a9fe1fbb` | 709 | 24 |

Manifest SHA-256: `8579d24dc6e6a5ed1b7601aa6b28e92eb1dae5998af5a79fa5797f744513227d`; 2,741 bytes, 41 LF. Line references below are to the frozen candidate.

## Re-derived ordered-four argument

1. **Full support, candidate LF17–19.** For a consecutive triple `(u,v,w)`, put `t=u−v+w`. A copy of `t` before it gives `(t,u,v,w)` and a copy after it gives `(u,v,w,t)`, either with zero alternating sum. Under a no-zero assumption, full support forces a copy inside the triple. Adjacent inequality excludes `t=u,w`, so `t=v`; consecutive differences are all the same nonzero `d`. Positions `1,2,3,p+2` then have alternating sum `−pd=0`. They are distinct even for `p=3`.
2. **High multiplicities, LF25–29.** Four copies give zero. For three `a` and two distinct `b`, partition the three `a` positions by the two `b` positions. Two `a` in one region give either a disjoint or nested equal pair; otherwise the five positions are `a,b,a,b,a`, and the outer `a` and both `b` give zero. If exactly one value is tripled and all others are singletons, the length is `p+2` and support is exactly `p`, so step 1 applies.
3. **Every repeated-value interval, LF31–41.** With multiplicities at most two, let `s` be the number of doubled values. The support is `p+2−s`, so `s≥2` and exactly `s−2` field values are absent. Disjoint intervals produce `a,a,b,b` or its reverse; nested intervals produce `a,b,b,a` or its reverse. Both give zero. Thus a zero-free word forces every pair to cross. For a crossing pair, `x=2a−b` is distinct from both repeated values because `p` is odd. Let `X` denote an occurrence of `x`; all indices in this table are distinct and increasing:

   | Repeated positions | `X` before `a₁` | `a₁ < X < a₂` | `X` after `a₂` |
   |---|---|---|---|
   | `a₁<b₁<a₂<b₂` | `X,a₁,b₁,a₂` | `a₁,X,a₂,b₂` | `a₁,b₁,a₂,X` |
   | `b₁<a₁<b₂<a₂` | `X,a₁,b₂,a₂` | `b₁,a₁,X,a₂` | `a₁,b₂,a₂,X` |

   Their alternating sums are zero, including when `X` lies on either side of the intervening `b` position. Hence every `2a−b` must be absent. For fixed doubled `a`, the other `s−1` doubled values give `s−1` distinct such absent values, contradicting the `s−2` missing values. This checks both crossing orientations, all insertion intervals and the missing-value injection at universal `p` scope.

## Actual-word lift and cyclic-cut restoration

For `F=3p−2`, `o_F=p+2`, the number of disjoint same-reflection pairs in the cyclic constant runs is `H=(F−o_F)/2=p−2`. Equal consecutive labels in the cyclic list of odd runs must have at least one even run between them; the intervening regions are disjoint. Since `e_F≤1`, at most one odd-label adjacency is equal. Cutting that edge, or cutting anywhere when there is none, yields the adjacent-distinct linear `p+2` list required by the lemma.

Choose one actual occurrence from each of the four certified odd runs and choose all `H` run-internal pairs, arranging each odd run so that its pair slots and possible representative are disjoint. There are `2H+4=2p` selected reflections. Rotations in the original word are unselected; in the cut cyclic reflection order each selected equal pair cancels, leaving the four certified reflections. For `s_x=r^x s`, their product is `r^(x₁−x₂+x₃−x₄)=1`.

Sorting the selected full-word indices does not permute them arbitrarily: it cyclically rotates the cut-order list. If its cut-order product is `UV=1`, then the original-order product is `VU=1`, including when the original start splits a selected pair. This proves the actual selector claim without assuming the selected reflections are adjacent in the full word (candidate LF43–57).

## Raw-graph bound and conditional profiles

For the graph described at candidate LF61, the full `F`-cycle has matching number `(3p−3)/2>p−3`, so a graph with `ν_M≤p−3` is a proper cycle subgraph. Its components are paths, including isolated vertices. If `q` is the number of absent edges and `o_M` the number of odd components, then `q` is the number of components and

`ν_M=(F−o_M)/2`, hence `q≥o_M≥F−2(p−3)=p+4`.

Every absent edge joins equal neighboring reflection exponents across an empty actual gap. A REF-failing word cannot have all reflections equal: select any `2p` of them. For every other cyclic exponent list, there are exactly `F−r` equal-neighbor edges, where `r=o_F+e_F` is the number of maximal cyclic runs. Thus `p+4≤q≤F−r`, giving `r≤2p−6`. Also, if `H≥p`, choosing `p` same-reflection pairs in cyclic order and restoring the cut gives an original-order identity selector; therefore failure implies `H≤p−1`. Put `κ=p−1−H≥0`. Then `o_F=F−2H=p+2κ`, and substitution gives

`2κ+e_F≤p−6`.

When `κ=1`, the proved lift eliminates `e_F=0,1`; thus any still-failing lower word has `e_F≥2` and necessarily `p≥11`. At `p=7`, the inequality is `2κ+e_F≤1`; the **assumed**, not proved, floor gives `κ≥1` and a contradiction. At `p=11`, with that same floor, the profiles not eliminated by this argument are exactly the necessary count profiles `(κ,e_F)=(1,2),(1,3),(2,0),(2,1)`; this does not establish realizability or discharge other caller conditions.

## Independently structured finite controls

The retained controls use Python's standard library only and no author code or data. They are bounded checks, not the justification for the all-prime conclusions.

- Enumerated **all**, not just normalized, adjacent-distinct length-`p+2` sequences: `48=3·2^4` at `p=3` and `20,480=5·4^6` at `p=5`; every one had a zero alternating quadruple in its original index order. The program also explicitly checked the applicable multiplicity, nested/disjoint, crossing-target and missing-injection branches. For example, all-cross injection witnesses occurred in 30 and 5,040 words respectively.
- Independently enumerated every local triple/double order and every insertion of `x=2a−b` into both crossing patterns at `p=3,5,7,11`: respectively 60, 200, 420 and 1,100 insertion cases, with the explicit case-table witnesses above. Also checked disjoint/nested patterns and constant-step examples.
- Compared a cycle-matching dynamic program with separately reconstructed path components on **every** edge mask for `F=7,13,19`: 128, 8,192 and 524,288 graphs. The lower-matching mask counts were 1, 287 and 33,631. A separate brute subset-matching implementation examined all 2,187 reflection-label sequences and 128 binary empty/nonempty gap assignments at `p=3` (279,936 combinations): there were 126 REF-failing label sequences, but no combination both REF-failing and `ν_M≤0`. These gap bits describe arbitrary rotation-gap incidence, not exclusively words with a fixed rotation count.
- Constructed and directly checked 12 exact full words at `p=3,5,7,11`, with `p+1` rotations and `3p−2` reflections, covering `e_F=0`, `e_F=1` with an equal odd-label edge, and `e_F=1` without one. Every selected original-order product was computed as an actual permutation of `F_p`; all 12 cut orders were nontrivial cyclic rotations of the original selector. Wrong-count and rotation-in-selector controls were rejected; changing one selected reflection exponent by one preserved the selector size but made all 12 products nonidentity.

**Concrete original-order example, `p=5`, `e_F=1` with one equal odd-label edge.** With zero-based indices and `rj=r^j`, `sj=r^j s`, the full word is

`[r1,s0,s0,r2,s0,s0,r3,s1,s0,r4,s0,s1,r1,s2,s3,r2,s4,s1,s0]`.

The cut-order odd labels are `[1,2,3,4,1,0,1]`; quadruple positions `[0,1,4,5]` yield `[1,2,1,0]`. The selected original full-word indices are `[1,2,4,5,8,10,11,13,17,18]`, with reflection exponents `[0,0,0,0,0,0,1,2,1,0]` and direct permutation product `[0,1,2,3,4]`. The cut-order selected indices are `[11,13,17,18,1,2,4,5,8,10]`, whose rotation by four positions gives the original order. Mutating only selected index 1 from `s0` to `s1` changes the direct action to `[1,2,3,4,0]`, a nonidentity product.

## Retained control artifacts

| File | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `reviewer-controls.py` | `d964cf9f7dbaa5fce28825f1b359a20da71438b2c69d526be3f9073aa3cc75aa` | 17,517 | 419 |
| `reviewer-controls-results.json` | `064fd7bf3e577be84f52d8875c24f2f4be448f1cb9074ccefd7e9b7fc68d29da` | 23,218 | 1,434 |
| `reviewer-gap-mutation-controls.py` | `d59c9293b994c0024fd9dfa7b1d05c3caa7e5c0df686b0ce33853bae15f332ff` | 4,313 | 109 |
| `reviewer-gap-mutation-results.json` | `a3b606c95c8c745030983c8e548ff5a5650a81159743621912fc122f54a2353d` | 3,745 | 187 |
