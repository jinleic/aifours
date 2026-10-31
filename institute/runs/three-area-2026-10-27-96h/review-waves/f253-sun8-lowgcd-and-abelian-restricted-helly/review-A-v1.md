# f253 slice A: four-coset low-gcd affine obstruction

Observed native clock before creation: 2026-10-29T15:17:15-0700 PDT.

## Disposition and boundaries

**Self-contained target-A mathematics: 0 FATAL / 0 MAJOR / 0 MINOR.** The four-coset construction and the stated exact packing values are supported by the written reconstruction below, for the quantified domains stated. This is a same-harness review, not a parent adoption, human review, independent-model-family review, formal/kernel proof, or novelty/priority assessment. It is not an assessment of target B. Historical/process assertions and the imported characterization of the earlier f243 result are **INCONCLUSIVE/outside this review**, not silently adopted.

Most importantly, **four cosets do not provide a six-coset obstruction under both B_7 <= 2 factor hypotheses, nor a six- or eight-coset Sun8 counterexample**. In the exhibited infinite example the quotient has B_7 = 4, not <= 2. The four displayed cosets already partition G, so another nonempty coset cannot be appended while retaining those four; this does not exclude a different six- or eight-coset family in an arbitrary group surjecting onto F_2^3. Nothing here settles the unrestricted normal-extension implication or Sun8 in arbitrary groups.

For clarity, B_7(X) below denotes the supremal cardinality of a family of pairwise-disjoint actual finite-index left cosets whose subgroup indices have pairwise gcd at most 7. Equivalently, B_7(X) <= r means every r+1 such disjoint cosets contain a pair with index gcd at least 8. Repeated subgroups are allowed. The results below prove the needed finite bounds directly.

## Inputs, ordering, and independence

Manifest `manifest-v2.json` full SHA-256: **bd0f0a90d64e6b6899f2b5f5c89c927ba065b02389716a6e7d699200834a0f32**. Its hash was matched first. All six input SHA-256, byte counts, and LF counts were then matched before any source-body reading; all decoded as UTF-8, ended in LF, and had zero CR bytes. All six bodies were subsequently read **completely and in the manifest order**, using raw windows of at most 15 lines including the endings, before any mathematical reasoning. These are 435 LF in total. The pre-body acknowledgement is `reviewer-A-ack-v1.json`; the prior exposure was only the assignment and manifest metadata/scope, with byte access solely for metadata verification.

All inputs are under `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`:

| Order | Complete input | SHA-256 | Bytes | LF |
|---:|---|---|---:|---:|
| 1 | `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 | 56 |
| 2 | `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 | 11 |
| 3 | `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 | 10 |
| 4 | `frontier-20261029-f243-cyclic-crt-additive-erratum-v1.json` | `775e251a582ffd01de3d1bd3a6e5af770d6be7cf3252cc10c64c201aaf64c26e` | 2329 | 12 |
| 5 | `frontier-20261029-lowgcd-affine-nonhelly-obstruction-v1.txt` (target A) | **`d62eff5412e520a5b18e7bd85e6575424dd039643622fdd131c57e5f2fb556d4`** | 8499 | 156 |
| 6 | `frontier-20261029-abelian-quotient-restricted-helly-v1.txt` (target B) | `e7314d8fdc0db90ecb2a9339aff42d4529194fb683dddb41ce63a9ece791ad97` | 10513 | 190 |

The overlays and erratum were honored in order, but their other mathematical contents, target B, and linked documents are **not mathematical premises** here. Target B was read for coverage only. No held/f161/f162/selected prime-2/3 payloads, linked-source expansion, author PASS or code, other reviews, external model, or publication were used. The author reports historical exposure and other provenance facts; this review cannot certify the author's cognition or independently validate that history.

## Claim-by-claim verdicts

`F/M/m` are fatal/major/minor findings for the specified claim, not a claim of external acceptance.

| Target-A claim | Verdict | Reconstruction / limit |
|---|---|---|
| A:9-19, 38-58: arbitrary surjection, normal preimages, four distinct actual index-4 left cosets with pairwise gcd 4 and union G | **0 F / 0 M / 0 m** | Explicit vectors and left-preimage/index proof below; no finiteness, commutativity, or splitting of G is required. |
| A:20-22, 60-74: three pairwise-intersecting non-Helly quotient images; fourth disjoint; projected and kernel-fiber indices and product | **0 F / 0 M / 0 m** | All images, their three pair intersections, all four quotient fibers, and the actual-fiber left-coset formula are reconstructed below. |
| A:77-87: arbitrary D with no proper finite-index subgroup, including D=(Q,+), forces every finite-index subgroup and coset to be a full V-preimage (and likewise in N) | **0 F / 0 M / 0 m** | Injection of left-coset sets, subgroup factorization, and divisibility of the rationals are proved below. |
| A:88-107: B_7(N)=2, B_7(G/N)=4, B_7(G)=4 for the stated D class; hence the infinite rational example and both factors satisfy Sun8 | **0 F / 0 M / 0 m** | Explicit lower bounds and complete index/volume upper bounds below; the finite control is supplemental, not an infinite-group test. |
| A:109-124: stated pairwise-overlap-to-common-fiber implication is false, but neither the stronger B_7<=2 factor setting nor a six/eight-coset Sun8 counterexample is supplied | **0 F / 0 M / 0 m** for these self-contained conclusions | The infinite rational example gives the counterexample to the claimed Helly shortcut, with only four cosets and B_7(G/N)=4. |
| A:120-124 and 126-150: characterization of f243's obstruction, past geometry, and historical/process/provenance statements | **INCONCLUSIVE / excluded** | Referenced source bodies and history were not opened. The present result does not require them. The failure to assess these contextual claims is not a finding that they are false. |

## Reconstruction of the four actual cosets

Write the identity of V = F_2^3 as 000 and coordinates as `(n,x,y)`. Let L = {000,100}, N = phi^{-1}(L), Z = ker(phi), and identify G/N with V/L = F_2^2 by `(n,x,y) -> (x,y)`. L is normal in the abelian V, so N is normal in arbitrary G. The induced map G/N -> V/L is an isomorphism: it is onto, and its kernel is exactly N.

The following table recomputes every displayed set. An entry `010` denotes `(0,1,0)`; addition is componentwise modulo 2.

| i | H_i = {000, generator} | v_i | v_i + H_i | pi(U_i) in F_2^2 | A_i = pi(C_i) | a_i | b_i |
|---:|---|---|---|---|---|---:|---:|
| 1 | {000,010} | 000 | {000,010} | {00,10} | {00,10} | 2 | 2 |
| 2 | {000,101} | 100 | {100,001} | {00,01} | {00,01} | 2 | 2 |
| 3 | {000,011} | 110 | {110,101} | {00,11} | {10,01} | 2 | 2 |
| 4 | {000,100} = L | 011 | {011,111} | {00} | {11} | 4 | 1 |

The eight entries in the fourth column are all different and exhaust V. For each i define U_i = phi^{-1}(H_i), and choose any g_i with phi(g_i) = v_i, possible by surjectivity. Each H_i is normal in V, so each U_i is normal in G. Directly,

`x in g_i U_i  <=>  g_i^{-1}x in U_i  <=>  phi(x) in v_i + H_i`.

Thus C_i = g_i U_i is exactly the **left** preimage phi^{-1}(v_i + H_i), nonempty, and the four C_i are pairwise disjoint and cover G. Surjectivity identifies the left-coset set G/U_i with V/H_i; hence `[G:U_i] = 8/2 = 4` and every pair of original indices has gcd 4 <= 7. This proves an actual-coset statement, not merely an index pattern.

The first three quotient images have

- A_1 intersect A_2 = {00};
- A_1 intersect A_3 = {10};
- A_2 intersect A_3 = {01};
- A_1 intersect A_2 intersect A_3 = empty.

A_4 = {11} is disjoint from each. Therefore the overlap graph is exactly a triangle plus an isolated vertex. In particular, pairwise-overlapping images need not have one common quotient point, even though the original cosets are disjoint and the original index gcds are 4.

## Kernel indices and all actual fibers

Because `N intersect U_i = phi^{-1}(L intersect H_i)`, the first three intersections are Z and the fourth is N. The restriction phi|_N maps onto L with kernel Z, giving `[N:Z] = 2`. The quotient-image subgroup pi(U_i) is the projection of H_i; its sizes are 2, 2, 2, 1. Thus `(a_i,b_i) = (2,2),(2,2),(2,2),(4,1)` and `a_i b_i = 4 = [G:U_i]` for each i.

The complete image-level fiber table, with each entry listing the possible n-coordinate(s) in that C_i, is:

| q = (x,y) | C_1 | C_2 | C_3 | C_4 |
|---|---|---|---|---|
| 00 | {0} | {1} | empty | empty |
| 01 | empty | {0} | {1} | empty |
| 10 | {0} | empty | {1} | empty |
| 11 | empty | empty | empty | {0,1} |

This table also holds for the full G-preimages, not only for V: for fixed q and a lift t in G, choose x_i in `C_i intersect pi^{-1}(q)` when nonempty and put K_i = N intersect U_i. Since `C_i = x_i U_i` and `pi^{-1}(q) = tN = x_i N`,

`C_i intersect pi^{-1}(q) = x_i K_i`, and

`t^{-1}(C_i intersect pi^{-1}(q)) = (t^{-1}x_i) K_i`, an actual **left** K_i-coset in N.

The first three K_i equal Z and have index 2; at each of 00, 01, 10 the two present pieces are the two disjoint Z-cosets in that fiber. At 11, K_4 = N and C_4 fills the entire quotient fiber. No quotient point carries all first three original fibers, so a common-fiber argument cannot be inferred from their pairwise overlaps.

## Infinite example and exact packing values

Let D be any group with no proper finite-index subgroups, G = V x D, and N = L x D. If W <= G has finite index, the map of left-coset sets

`D/(W intersect D) -> G/W`, `d(W intersect D) -> dW`

is injective: equality of the images is exactly `d_2^{-1}d_1 in W intersect D`. Thus W intersect D has finite index in D and must equal D. Let S be the image of W under G -> V. Since D <= W, for every `(v,d) in W`, multiplication by `(0,d^{-1}) in W` gives `(v,e) in W`; consequently W = S x D. Conversely every S <= V gives such a subgroup. Every finite-index left coset in G is therefore the full preimage of an affine S-coset in V, with the same index; disjointness and family size correspond exactly. The same proof applies to N = L x D. No normality of W or commutativity of D was used.

For D = (Q,+), if H has finite index d, the finite abelian quotient Q/H is annihilated by d. Every rational x equals d(x/d), hence x + H = 0, so H = Q. D is infinite and has no proper finite-index subgroup, as required.

The finite packing counts now give exact infinite-group values:

1. **N:** finite-index subgroup indices are only 1 and 2. An index-1 coset is all N; otherwise at most two disjoint index-2 cosets fit. The two cosets of `{0} x D` partition N and have gcd 2, so B_7(N) = 2.
2. **Q_0 = G/N = F_2^2:** at most four nonempty disjoint cosets fit in four points. The four singleton cosets have index 4 and pairwise gcd 4, so B_7(Q_0) = 4.
3. **G:** finite-index subgroup indices are 1, 2, 4, 8, corresponding respectively to affine sets of 8, 4, 2, 1 points in V. In a family of at least two, index 1 is impossible, and there is at most one index-8 member because gcd(8,8) = 8. Two index-2 cosets fill V. With exactly one index-2 coset, at most two index-4 cosets fit; if two fit no index-8 member fits, so there are at most three members. With no index-2 coset, at most four index-4 cosets fit; if an index-8 member is present, at most three index-4 cosets fit. Hence any bad family has at most four members. The four constructed index-4 cosets attain four, so B_7(G) = 4.

Thus in the infinite rational example both factors, and G itself, satisfy Sun8 in the B_7 <= 7 sense. Nevertheless A_1, A_2, A_3 refute the asserted general 3-Helly shortcut. These arguments apply to exactly the stated D class, not arbitrary extensions.

## Reviewer-owned bounded exact controls and intended negatives

One reviewer-written finite control was run once, after all source-body reads and written reconstruction; no author code was used. Path `reviewer-A-finite-control-v1.py`, SHA-256 **eb2c54891683c9def174f1de108d9dde00bd1c589c4a8bc0c20fa55d32a41737**. Actual command: `/usr/bin/python3 -B reviewer-A-finite-control-v1.py`. Native `/bin/date` start and end: `2026-10-29T15:16:55-0700 PDT`, `2026-10-29T15:16:55-0700 PDT`; monotonic elapsed 0.029753 seconds, subprocess timeout 120 seconds, **actual exit 0**, stderr empty. The script enumerates every F_2^d subspace and its distinct cosets for d=1,2,3 and recursively enumerates all pairwise-disjoint families with pairwise index gcd <=7:

| d | subgroups | distinct cosets | counts by family size beginning at 0 | maximum |
|---:|---:|---:|---|---:|
| 1 | 2 | 3 | 1, 3, 1 | 2 |
| 2 | 5 | 11 | 1, 11, 21, 10, 1 | 4 |
| 3 | 16 | 51 | 1, 51, 525, 1470, 945, 0, 0, 0, 0 | 4 |

It separately checks every displayed V-coset, quotient image, pair intersection, projected/kernel index, product, and fiber table. Two intended-reason negatives were observed: replacing the second generator by 001 produced the expected `OVERLAP_C2_C3` rejection; moving the third quotient-image representative to 000 preserved pairwise intersections but produced the expected `TRIPLE_NONEMPTY` rejection. These are deliberately altered finite fixtures, not counterexamples to the original construction. Output ended `ALL_CONTROL_CHECKS_PASSED`. The control does not establish arbitrary-group preimages, rational divisibility, provenance, novelty, or formal correctness; those group-theoretic claims are addressed by the written argument above.
