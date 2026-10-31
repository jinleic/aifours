# f260: independent same-harness review of the corrected abelian-quotient bridge

**Verdict: written support for the corrected theorem and its stated example, at the exact hypotheses below.** I independently reconstructed the proof; no prior f253 verdict is a premise. The unchanged candidate has one **m** (minor) wording deficiency at LF 124, paid by the separately pinned mandatory gcd erratum. Counts for the frozen original: **0 F / 0 M / 1 m**. Counts remaining in the corrected composite: **0 F / 0 M / 0 m**. The provenance/history assertions are **INCONCLUSIVE**, not independently determined from the nine authorized inputs. The two claims are deliberately separate from mathematical support. F = fatal, M = major, m = minor.

Observed native `/bin/date` before composing: **2026-10-29T22:32:44Z**; not a creation-time claim.

## Per-claim dispositions

| Claim | Disposition | Finding |
|---|---|---|
| Index product for arbitrary normal extensions and finite-index original subgroups, including infinite groups | SUPPORTED; 0 F / 0 M / 0 m | `[G:U_i]=[Q:V_i][N:N∩U_i]`; no split or normality of `U_i` is needed. |
| Fibre translation and actual disjoint kernel cosets | SUPPORTED; 0 F / 0 M / 0 m | The conjugated subgroup `tK_it^{-1}` is essential. |
| Original-index gcd divisibility; projected overlap implies quotient gcd at most 3 | SUPPORTED; 0 F / 0 M / 0 m | The product of the two factor gcds divides the original gcd; equality need not hold. |
| Finite abelian quotient structure from no index 3 or 4 | SUPPORTED; 0 F / 0 M / 0 m | Every finite quotient has 3-part trivial and 2-part of order 1 or 2. |
| Simultaneous odd/2-primary quotient intersections | SUPPORTED; 0 F / 0 M / 0 m | Under the actual-family overlap constraint, odd component indices are pairwise coprime and the 2-components are singletons or the whole 2-group. This is not global Helly. |
| All-variable Ramsey bridge and `B_7(G)≤5` when both factor bounds are 2 | SUPPORTED; 0 F / 0 M / 0 m | `R(3,3)=6`; the no-index-3/4 hypotheses follow from `B_7(Q)≤2`. |
| LF 124 uncorrected expression, and corrected Sun8 conclusion | **m**, resolved by the mandatory gcd erratum; no residual finding | Two indices individually at least 8 are not the required pair with gcd at least 8. The preceding bound actually proves the corrected statement. |
| `N=C2`, `Q=C2×F_p²`, `G=N×Q`, every prime `p>7` | SUPPORTED; 0 F / 0 M / 0 m | Both factor bounds are exactly 2; `Q` is not globally 3-Helly; the candidate's `4≤B_7(G)≤5` is correct. I separately derive the stronger exact value 4 below, not attributed to the candidate. |
| Exact conditional comparisons to the pinned f151/f242/f243 dispositions | SUPPORTED; 0 F / 0 M / 0 m | The displayed example fails their respective displayed sufficient interfaces, not every possible proof or theorem application. |
| Author's historical/provenance assertions and novelty/priority | INCONCLUSIVE / not assessed | The author discloses prior exposure; these nine inputs do not establish the historical claims. No clean-cognition finding, priority, novelty, independent-family, human or formal/kernel verification follows. |

## Independent reconstruction

### 1. Index and common-fibre identities

Let `π:G→Q=G/N`, `C_i=g_iU_i`, `V_i=π(U_i)`, `K_i=N∩U_i`, `a_i=[Q:V_i]`, `b_i=[N:K_i]`, and `n_i=[G:U_i]`. Since `N` is normal, `NU_i` is a subgroup. The bijection `N/K_i→NU_i/U_i`, together with the index tower, gives `n_i=a_ib_i`; all these indices are finite even if the groups are infinite. For any pair, `gcd(a_i,a_j) gcd(b_i,b_j)` divides both `a_ib_i` and `a_jb_j`, and hence divides `gcd(n_i,n_j)`. This is divisibility, not generally equality: `a=(2,3)`, `b=(3,2)` give product of factor gcds 1 but original gcd 6.

If `π(C_i)` and `π(C_j)` intersect at `q`, choose a lift `t` of `q` and points `x_l∈C_l∩Nt`. Because `N` is normal, `C_l∩Nt=x_lK_l` and

`(C_l∩Nt)t^{-1}=(x_lt^{-1})(tK_lt^{-1})`.

These are actual left cosets in `N`, of index `b_l`; if the original cosets were disjoint, so are these two. For finite-index subgroups `P,R` of any group, `[H:P∩R]` is at most `[H:P][H:R]` and is divisible by both individual indices. If those indices are coprime, equality holds, and the natural injection of the coset set of `P∩R` into the product of the coset sets is surjective. Thus **any** prescribed two left cosets meet. The disjoint fibre cosets therefore have `gcd(b_i,b_j)≥2`. If the original family has all `gcd(n_i,n_j)≤7`, divisibility gives `gcd(a_i,a_j)≤3` on every overlap edge. It is not asserted for non-edges.

### 2. Restricted, not global, quotient Helly

For a finite overlap clique, `H=∩V_i` is finite-index and normal in abelian `Q`. Its quotient `F=Q/H` is finite abelian, and each `A_i=π(C_i)` is `H`-saturated, so intersections in `Q` correspond exactly to intersections of the image cosets in `F`. Any index-3 or index-4 subgroup of `F` would pull back to one in `Q`.

A nontrivial finite abelian 3-group has an index-3 subgroup. If its 2-primary component has order at least 4, it has two successive index-2 subgroups, giving an index-4 subgroup. Consequently `F=F_2×F_odd`, with `|F_2|≤2` and `3∤|F_odd|`. Bézout powers split every subgroup, and therefore each coset, across the coprime-order factors. In the 2-component, each coset is the entire group or a singleton; pairwise intersection forces all singleton constraints to agree. In the odd component, the indices divide the corresponding `a_i`. Their pairwise gcd divides `gcd(a_i,a_j)≤3`, but is odd and not divisible by 3, so it equals 1.

For any finite family of finite-index subgroups of any group with pairwise-coprime indices `c_i`, the intersection index is at most `∏c_i` and divisible by every `c_i`; therefore it equals `∏c_i`. The natural injection of its left-coset set into the product of the individual left-coset sets is then a bijection. In particular any prescribed odd-component cosets share a point. Combining it with the 2-component point and lifting from `F` proves a common point for this clique of actual projected cosets. It does **not** prove global Helly for arbitrary quotient cosets.

### 3. Ramsey conclusion and corrected wording

For an original bad family (pairwise-disjoint actual cosets with all index gcds at most 7), colour two labels as an overlap edge iff their quotient cosets meet. A clique of `r+1` labels has a common quotient fibre by the preceding restricted lemma and yields `r+1` pairwise-disjoint kernel cosets with index gcds at most 7, contradicting `B_7(N)≤r`. An independent set of `s+1` labels yields disjoint quotient cosets with index gcds at most 7, contradicting `B_7(Q)≤s`. Ramsey therefore gives `B_7(G)≤R(r+1,s+1)-1`, with all stated hypotheses retained.

If `B_7(Q)≤2`, a subgroup of index 3 or 4 would supply three disjoint cosets of the same subgroup whose pairwise index gcd is that index. Thus such a subgroup cannot exist. With `B_7(N),B_7(Q)≤2`, `R(3,3)=6` gives `B_7(G)≤5`. Hence every **six**, and therefore every eight, pairwise-disjoint original cosets contain **two subgroup indices whose gcd is at least 8**. This is stronger than, and is what is needed instead of, the frozen LF 124 wording. As a numerical warning `8,9` both exceed 7 but have gcd 1; even in an actual disjoint-coset setting the issue persists: in `C60`, the cosets `10Z/60Z` and `1+12Z/60Z` are disjoint, have indices 10 and 12, and gcd 2.

### 4. Example and exact comparisons

For `p>7`, let `N=C2`, `Q=C2×F_p²` and `G=C2×Q`. In `N`, two index-2 cosets are disjoint and there cannot be three; thus its exact bad-family maximum is 2. In `Q` every subgroup index divides `2p²`. For a bad family of size at least two, coprime indices would force an intersection; each pair's gcd is therefore exactly 2, and at most one index is divisible by `p`. In a putative three-family the other two must be index 2. There is a unique index-2 subgroup, and its two disjoint cosets cover `Q`, leaving no place for a third. Two exist, so `B_7(Q)=2`.

The quotient cosets `C2×{y=0}`, `C2×{x=0}`, `C2×{x+y=1}` have pairwise intersections and empty triple intersection, and each has index `p`. Thus global 3-Helly fails; these cannot be an overlap clique of an original bad family because their quotient-index gcd is `p>7`. Also no subgroup can have index 3 or 4 since each index divides `2p²`. Four cosets of `{0}×{0}×F_p²` in `G` are disjoint with index 4, giving the candidate's lower bound 4; the theorem gives upper bound 5.

**Reviewer-derived strengthening, not an author claim:** in fact `B_7(G)=4` for every such `p`. Write `G=E×P` with `E=C2²`, `P=F_p²`. Every subgroup and coset splits across the coprime factors. In any bad family, at most one subgroup index is divisible by `p`. Every other coset has full `P` component; hence the `E`-components of all family members, including the possible exceptional one, must be pairwise disjoint nonempty subsets of the four-element `E`. Thus there are at most four, and the four exhibited cosets attain this. This independent written deduction is not a change to the frozen candidate and is not parent adoption.

For these exact `N,Q,G`: the pinned **f243** interface requires global quotient 3-Helly in its `r=s=2` corollary (and finite-clique Helly in its general bridge), which fails for the displayed `Q`; **f242** requires the indicated finite `J_7(Q)` bound, whereas repetitions of the proper index-2 subgroup violate every finite such bound; and all the directly displayed **f151** sufficient criteria require `μ(G)≥8` or `≥13`, whereas `G` has index-2 subgroups. These statements use the three supplied dispositions only. They do not establish that no other argument applies, or that this example is novel.

## Independent bounded synthetic controls

One reviewer-authored standard-library script, with no producer code, was run once. Script SHA-256 `97d2a9bf6e7014ef04c4810fc6049b7f72beababc1570f189164921b0d76970a`; [receipt](reviewer-controls-v1-receipt.json) SHA-256 `861cda709c7b6ec22fb8e8f68aa8111a9cf19d615c3f9ec8c49ba56c386c8c5d`. Native `/bin/date` UTC start/end both `2026-10-29T22:32:23Z`, monotonic duration `0.204436 s`, limit 110 s (below 120 s), actual exit **0**, stderr empty; input hashes, byte counts and LF counts matched before and after. The script checks finite examples, not universal theorem validity.

- `S4`/`A4`: all 30 subgroups, 234 actual left cosets, 720 nonempty fibre-identity checks, 27,261 index-divisibility pairs, and 9,438 actual overlapping low-gcd disjoint pairs. Intended negative `MISSING_CONJUGATION` produced a genuine different set, not an arbitrary exception.
- `C2×F5²`: 168 actual cosets, 387 qualifying pairwise-overlap/low-gcd edges, and 220 clique triples, each with a common point. This bounded triple control does not replace the written finite-family argument.
- Index-4 intended negative: actual disjoint affine-line cosets in `C2³` project to three pairwise-intersecting quotient cosets with empty total intersection; original indices are 4, quotient indices 2, and original gcds are 4. It shows the restricted-Helly proof can fail without the index-4 hypothesis, **not** that the global bridge conclusion is false without it. Index-3 intended negative: three affine lines in `C3²` have quotient indices 3, pairwise meet and have empty triple intersection; no original-family lift is claimed for that control.
- `K5` has 12 and `K6` has 0 two-colourings without a monochromatic triangle, establishing the bounded `R(3,3)` check. Intended negatives explicitly distinguish indices `8,9` from gcd ≥8, and factor-gcd divisibility from equality.
- At `p=11`, 506 even-index `p`-divisible quotient cosets were checked against the index-2 partition; the three line intersections have sizes 1,1,1 with empty triple. All 11 affine cosets in the 2-primary `C2²` component were considered, with maximum disjoint packing 4. The all-prime result is the written argument above, not an extrapolation from this instance.

No archive assay or one-record diagnostic was authorized by this manifest, so none was run.

## Frozen input and coverage receipt

Manifest SHA-256 `4f224e0a23ce3acf5548af1e7d55028a55190151a0e8ea6deed0188e2df537e0` was checked **before** its complete 79-LF raw display (`1–15`, `16–30`, `31–45`, `46–60`, `61–75`, `76–79`). All nine declared inputs' full SHA-256, bytes and LF counts were checked before displaying any input body; all end in LF. They were then displayed completely, in manifest input order, using raw windows of at most 15 lines, including each ending. The overlays and both errata preceded the candidate. Exact paths and before/after metadata are in the control receipt; abbreviations below are directories, not truncated SHA values:

- `E=/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`
- `D=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`

| Order | Input (append basename to directory) | Full SHA-256 | Bytes / LF | Complete raw windows |
|---:|---|---|---:|---|
| 1 | `E/frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 / 56 | 1–15, 16–30, 31–45, 46–56 |
| 2 | `E/frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 / 11 | 1–11 |
| 3 | `E/frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 / 10 | 1–10 |
| 4 | `E/frontier-20261029-f243-cyclic-crt-additive-erratum-v1.json` | `775e251a582ffd01de3d1bd3a6e5af770d6be7cf3252cc10c64c201aaf64c26e` | 2329 / 12 | 1–12 |
| 5 | `E/frontier-20261029-f253-review-b-gcd-additive-erratum-v1.json` | `c0e21498f56ebe292ef8745a2d8457f6dcf508ecb567cd0de6f0b7a9bf5540f3` | 2825 / 25 | 1–15, 16–25 |
| 6 | `D/math-6-sun8-source-free-support-criteria-parent-v1.md` | `2ad5691a705089a6d724b2c9f21c075d76d31ddc471448abaa11240bc8d6637f` | 6429 / 30 | 1–15, 16–30 |
| 7 | `D/math-6-sun8-sparse-quotient-fibre-bridge-and-psl2-quotients-parent-v1.md` | `58992864735e124aabf00654f27b83ac59fc9f279f2848f9d81c1fcd8ae451f3` | 4426 / 24 | 1–15, 16–24 |
| 8 | `D/math-6-sun8-helly-ramsey-normal-extension-bridge-parent-v1.md` | `0a77a4311d9e6059e4c08542e7553d5f8b2c60a25476dec9995bd87aaa30fc08` | 4192 / 24 | 1–15, 16–24 |
| 9 | `E/frontier-20261029-abelian-quotient-restricted-helly-v1.txt` | `e7314d8fdc0db90ecb2a9339aff42d4529194fb683dddb41ce63a9ece791ad97` | 10513 / 190 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, 181–190 |

Coverage deviation: **none**. No held/withdrawn bodies, f161/f162, selected prime-2/3 material, sibling results, author checker/PASS, linked sources, external model/API, Git, publication, or deletion was used. The overlays' own descriptions were read as mandated, not as permission to open affected held sources. The historical f236 UNKNOWN and all holds remain unchanged. This is same-harness written review with bounded synthetics, not unrestricted Sun8, novel priority, human, independent-family or formal/kernel verification, and not parent acceptance.
