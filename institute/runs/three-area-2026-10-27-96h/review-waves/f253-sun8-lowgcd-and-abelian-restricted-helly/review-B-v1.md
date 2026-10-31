# f253 slice B: independent same-harness written review

Observed native clock immediately before preparing this report: `2026-10-29T15:23:21-0700 PDT`. This is the reviewer's observation, not a creation-time claim. The parent owns disposition and integration.

## Verdict and scope

**The stated normal-extension theorem and its numerical corollary are supported by the independent reconstruction below: 0 FATAL, 0 MAJOR, 1 MINOR wording finding.** The comparison with the exact historical f242, f243 and f151 interfaces is **INCONCLUSIVE** in this frozen review, because those definitions/bodies are not inputs; the independently checkable mathematical facts behind the comparison are recorded below. An inconclusive cross-reference is not a finding that those historical sources are wrong and is not a premise of this theorem.

The supported claim is conditional: for arbitrary G, N normal, abelian Q=G/N with no index-3 or index-4 subgroup, and positive r,s, the two assumptions B_7(N)<=r and B_7(Q)<=s give B_7(G)<=R(r+1,s+1)-1. In particular, abelian Q and the **stronger** two assumptions B_7(N), B_7(Q)<=2 give B_7(G)<=5 and hence Sun8(G). This is not unrestricted Sun8, not factor-Sun8 composition for arbitrary r=s=7, not a statement for nonabelian quotients, and not a global coset-Helly theorem.

`F`, `M`, `m` below mean fatal, major, and minor finding, respectively. `NO FINDING` means the claim was reconstructed at the stated scope; it is not formal certification. `INCONCLUSIVE` is used for an assertion whose exact source definition was not available in the permitted packet.

| Claim (target B lines) | Verdict | Review basis / limit |
|---|---|---|
| Original B_7 definition and theorem quantifiers (8–32) | NO FINDING | Actual left cosets; repeated subgroups allowed; all groups may be infinite; no covering or normality of U_i is needed. |
| Finite index product and product-of-gcd divisibility (34–47) | NO FINDING | [G:U_i]=[Q:pi(U_i)] [N:N cap U_i]; each gcd factor divides the respective factor on both sides. |
| Overlap fibre conjugation and two-coset coprime lemma (48–60) | NO FINDING | Actual fibres are left cosets of t(N cap U_i)t^{-1}; the coprime-index lemma is proved below without assuming normal subgroups. |
| Overlapping quotient images imply gcd(a_i,a_j)<=3 (55–62) | NO FINDING | Disjoint actual fibre cosets force gcd(b_i,b_j)>=2, and the product divisor is at most gcd(n_i,n_j)<=7. It is only an overlap-edge condition. |
| Finite quotient and exclusion of 3-primary and order-at-least-4 2-primary parts (66–84) | NO FINDING | Pull back any subgroup of F=Q/H; finite abelian p-groups have index-p subgroups, and two successive index-2 subgroups give index 4. |
| Primary product splitting and pairwise-coprime odd component indices (85–98) | NO FINDING | Integer powers split every subgroup/coset over coprime factors. Odd common divisors cannot be 2 or 3. |
| Two-point Helly and pairwise-coprime coset common point (91–107) | NO FINDING | The two-point components are full or singletons; the index-product injection is a bijection for arbitrary groups. |
| Actual-family restricted clique-Helly and Ramsey bound (106–120) | NO FINDING | All members of a clique have one common lifted fibre; an independent set gives disjoint quotient cosets. R(r+1,s+1) excludes that many labels. |
| B_7(Q)<=2 forbids indices 3–7; R(3,3)=6 (122–125) | NO FINDING | Three distinct cosets of any subgroup of index d in 3–7 are bad. The 6-vertex Ramsey argument and 5-cycle lower bound are given below. |
| Sun8 conclusion wording at line 124 | **m** | It says a family has “a pair of indices >=8”; the needed property is that the **gcd** of the pair is >=8. The preceding proved B_7(G)<=5 gives the stronger property, so this is wording only, not a proof defect. |
| Symbolic example: B_7(N)=B_7(Q)=2, three non-Helly quotient cosets, and 4<=B_7(G)<=5 (135–150) | NO FINDING | Verified for every prime p>7 by the argument below; reviewer additionally derives B_7(G)=4. The program independently enumerated the finite p=11 instance only. |
| Repeated index-2 subgroup and finite-J comparison (153–157) | INCONCLUSIVE for the named f242 implication | For every m there are m **labels** of the same proper index-2 subgroup with all pairwise index gcds 2. This makes a supremum of such labelled families infinite **if** its definition allows repeats and imposes no conflicting condition. The actual f242 J_7 definition is not in the six inputs. |
| Other historical-interface comparisons (153–157) | INCONCLUSIVE for exact f243/f151 attribution | The displayed triple really is pairwise intersecting with empty triple intersection, and G really has index-2 subgroups. Whether those facts violate the precise earlier hypotheses depends on the absent definitions. Neither historical interface is assumed. |
| Claims of novelty, author provenance, other prior dispositions or parent adoption | OUT OF SCOPE / NOT ESTABLISHED | This review does not adjudicate historical exposure, prior findings, priority, or adoption. |

### Minor finding and suggested additive wording

At target B line 124, replace the informal “has a pair of indices >=8” with “has two subgroup indices whose **gcd is at least 8**.” Merely having two indices >=8 is insufficient: 8 and 9 have gcd 1. The actual proof has already established B_7(G)<=5, which yields the required gcd assertion for any six, hence any eight, labels. No frozen source was edited.

## Frozen input and exposure record

The full `manifest-v2.json` SHA-256 was checked as `bd0f0a90d64e6b6899f2b5f5c89c927ba065b02389716a6e7d699200834a0f32` before reading the manifest. Before opening **any** input body, all six files were checked against the manifest for the full SHA-256, byte count and LF count; all matched. Each ended in LF and had no CR bytes. Then all bodies, including their endings, were read fully in manifest order, in raw contiguous windows of at most 15 lines, before mathematical reasoning:

| Order | File role / basename | Full SHA-256 | Bytes | LF |
|---:|---|---|---:|---:|
| 1 | `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 | 56 |
| 2 | `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 | 11 |
| 3 | `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 | 10 |
| 4 | `frontier-20261029-f243-cyclic-crt-additive-erratum-v1.json` | `775e251a582ffd01de3d1bd3a6e5af770d6be7cf3252cc10c64c201aaf64c26e` | 2329 | 12 |
| 5 | Target A: `frontier-20261029-lowgcd-affine-nonhelly-obstruction-v1.txt` | `d62eff5412e520a5b18e7bd85e6575424dd039643622fdd131c57e5f2fb556d4` | 8499 | 156 |
| 6 | Target B: `frontier-20261029-abelian-quotient-restricted-helly-v1.txt` | `e7314d8fdc0db90ecb2a9339aff42d4529194fb683dddb41ce63a9ece791ad97` | 10513 | 190 |

These are 435 LF in total. Target A was read for coverage only, not used as a premise. The three alternating overlays and cyclic-CRT erratum were read in their required order; the present proof does not depend on the corrected cyclic step. No v1 manifest, held/f161/f162/selected prime-2/3 payload, linked historical body, sibling finding, author code or author PASS, external model/API, or publication was used. The finite counterexamples and controls below are reviewer-owned constructions. Prior findings and holds are neither reopened nor cleared.

## Independent reconstruction

### 1. Product indices and genuine fibres

For a finite-index subgroup U_i<=G put V_i=pi(U_i), K_i=N cap U_i, a_i=[Q:V_i], b_i=[N:K_i] and n_i=[G:U_i]. N normal makes NU_i a subgroup and pi^{-1}(V_i)=NU_i. The left-coset map N/K_i -> NU_i/U_i is a bijection, so all these indices are finite and

    n_i = [G:NU_i] [NU_i:U_i] = a_i b_i.
    gcd(a_i,a_j) gcd(b_i,b_j) | gcd(n_i,n_j).

The final divisibility follows because the product divides each n separately; the gcd product need not equal the latter gcd.

Suppose disjoint C_i=g_iU_i and C_j=g_jU_j have images meeting at q. Choose t with pi(t)=q and x_l in C_l cap Nt, for l=i,j. Since C_l=x_lU_l and x_l in Nt,

    (C_l cap Nt)t^{-1} = x_l K_l t^{-1}
                         = (x_l t^{-1})(t K_l t^{-1}) subset N.

These are disjoint actual left cosets in N. Normality of N makes tK_lt^{-1} a subgroup of N, of index b_l. The conjugation is essential; it cannot generally be replaced by K_l.

For arbitrary H and finite-index P,R<=H, the map from left cosets H/(P cap R) into H/P x H/R is injective. Its domain size is at most the product of the two indices and divisible by each of them. If those indices are coprime, it is therefore exactly the product and the map is onto: any prescribed left cosets meet. Thus disjoint fibre cosets have gcd(b_i,b_j)>=2. If the original family has every gcd(n_i,n_j)<=7, the displayed divisor forces gcd(a_i,a_j)<=3 on every quotient-overlap edge. No such edge condition is asserted for nonoverlapping projected cosets.

### 2. Finite abelian reduction and restricted Helly

Fix a finite clique I of actual image cosets A_i=pi(g_i)V_i. Let H=intersection_i V_i. H has finite index and is normal in abelian Q. The A_i are unions of H-cosets, so their pairwise and total intersections are nonempty in Q exactly when their images have the corresponding nonempty intersections in F=Q/H. The indices a_i are unchanged. Every index-d subgroup of F pulls back to an index-d subgroup of Q.

A finite abelian p-group with nontrivial p-primary part has an index-p subgroup: for example, take a maximal proper subgroup and observe that its nontrivial simple abelian p-group quotient has order p. Thus a 3-primary part would give index 3. If the 2-primary part has order at least 4, choose an index-2 subgroup and then an index-2 subgroup within it; since F is abelian this gives an index-4 subgroup of F after adjoining the other primary factors. Both possibilities contradict the hypotheses. Hence

    F = F_2 x F_odd,    |F_2| in {1,2},    3 does not divide |F_odd|.

Every subgroup W of F splits as (W cap F_2) x (W cap F_odd): integer exponents congruent to 1 and 0 modulo the coprime component orders extract each component of every element of W. Actual cosets split as products, and their component indices multiply to a_i. Pairwise overlap of the A_i gives pairwise overlap on F_2. Its only nonempty cosets are the whole component and, if its order is 2, its two singletons; pairwise-intersecting singleton constraints must all select the same point. Thus the 2-components have a common point.

For each pair i,j, the two odd-component indices have gcd dividing gcd(a_i,a_j)<=3. As they are odd and 3 does not divide |F_odd|, that gcd is 1. For finitely many arbitrary finite-index subgroups P_i of any group with pairwise-coprime indices c_i, the index of their intersection is divisible by each c_i, hence by product_i c_i, and is at most that product via the canonical coset injection. Equality makes the injection onto the product of individual left-coset sets, so any prescribed cosets have a common point. Applying this to the odd components and combining with the common 2-point yields one point of every image in F; lifting it to Q gives a common point of all original A_i.

This establishes clique-Helly only for projected cosets arising from the actual disjoint low-gcd family under review. The constraints are not a general Helly property for every collection of Q cosets.

### 3. Ramsey step and automatic exclusion

Color an edge when two projected A_i overlap. A clique of r+1 labels has a common quotient point by the preceding argument. One lift t gives r+1 pairwise-disjoint actual left cosets in N, with indices b_i. Since gcd(b_i,b_j) divides gcd(n_i,n_j), all their pairwise gcds are <=7, contradicting B_7(N)<=r. An independent set of s+1 labels gives pairwise-disjoint actual quotient cosets, and gcd(a_i,a_j) divides gcd(n_i,n_j), contradicting B_7(Q)<=s. The definition of R(r+1,s+1) rules out an original bad family of that size, giving B_7(G)<=R(r+1,s+1)-1. The proof uses finite families and finite subgroup indices only and is valid for infinite G, N, or Q.

If B_7(Q)<=2 and Q has a subgroup of index d in {3,4,5,6,7}, choose three different left cosets of that same subgroup. They are disjoint and all pairwise index gcds equal d<=7, contradiction. For R(3,3), in a two-coloring on six vertices one vertex has three neighbors of one color; an edge of that color among the three gives a monochromatic triangle, and otherwise those three form one in the other color. A two-colored 5-cycle and its 5-cycle complement show six is minimal. Hence B_7(G)<=5, and any eight-label family contains six labels whose index gcd has to be >=8.

## Named example and historical-interface limits

Let p>7 be prime, N=C2, Q=C2 x (F_p)^2 and G=N x Q. N has precisely two disjoint index-2 cosets, so B_7(N)=2. The index of a subgroup of Q divides 2p^2. In any disjoint bad family with at least two labels, the two-coset lemma makes every pairwise gcd at least 2. Since each such gcd divides 2p^2 and is <=7<p, it must equal 2. In particular every index is even and at most one is divisible by p; all other indices are 2. The unique index-2 subgroup is {0} x (F_p)^2 and its two cosets partition Q. Three bad labels would include both of those two cosets and a third, impossible. The two cosets exist, giving B_7(Q)=2. Lagrange also rules out index 3 and 4 in Q.

In Q the three displayed actual cosets C2 x {y=0}, C2 x {x=0}, C2 x {x+y=1} have index p. Each pair meets (at respectively (0,0), (1,0), or (0,1), with either C2 coordinate), while all three do not meet. They therefore disprove the literal assertion that every pairwise-intersecting triple of Q cosets has a common point. They do not violate the restricted clique result: their pairwise quotient-index gcd is p>7, in particular greater than the necessary overlap bound 3 for an original bad family.

The subgroup {0} x {0} x (F_p)^2 of G has index 4; its four disjoint cosets all have pairwise index gcd 4, so B_7(G)>=4. The theorem gives <=5. In fact a separate reviewer observation sharpens this particular example to **B_7(G)=4 for every p>7**: G=C2^2 x (F_p)^2, and at most one member of a bad family can have index divisible by p. A p-free-index subgroup contains the entire p-primary factor and hence its coset is the inverse image of a nonempty coset in C2^2. If five bad cosets existed, at least four would be such inverse images; their four nonempty pairwise-disjoint subsets of the four-point C2^2 partition it, leaving no room for a fifth coset. The four index-4 cosets supply equality. This is an observation about this example, not a general sharpening of the theorem.

For every positive integer m, take m labels all referring to the same proper index-2 subgroup of Q. Every pair of labels has index gcd 2, including repeated labels. Consequently any J-style bound on labelled subgroup families that **permits these repetitions** and requires only that gcd condition is unbounded. This does not claim that m repeated *cosets* are pairwise disjoint; only two cosets of this subgroup exist. The target packet does not define the historical J_7 functional, so the reviewer cannot establish the exact f242 comparison without assuming its definition. Likewise, G has proper index-2 subgroups, but the exact historical definition of mu and the f151/f243 interfaces were not read. The previously displayed elementary facts are proved; those named attributions remain INCONCLUSIVE and unnecessary for the theorem.

## Reviewer-owned final exact controls

After completing all input reads and the written reconstruction, one reviewer-written control program was run once, with no author imports. The command, full output, actual exit code and native-clock observations are retained in `reviewer-B-exact-controls-v1.receipt.json` (SHA-256 `3c8e275bc90e0e59365b8a99c6d5793ec10f11d527aadcc7b11741319c9a0d88`). The checker is `reviewer-B-exact-controls-v1.py`, SHA-256 `384584b8072fbf32e37b60cece071aed67c97c00df9395b36e8dc178096b2c4a`. Native UTC start and end were both `2026-10-29T22:22:38Z`; monotonic elapsed 0.06793079199269414 s; timeout 120 s; actual process exit **0**; stderr empty.

* Exact gcd checks covered all 104,976 quadruples with each factor 1..18 and all 20,137 satisfying the overlap premises. A deliberately stronger equality was rejected specifically as `PRODUCT_NEED_NOT_EQUAL_GCD`.
* In the nonabelian group S3 x C2 the checker constructed two disjoint index-6 actual left cosets with common quotient point, a=2, b=3, and explicitly computed the conjugated fibres. The unconjugated fibre was rejected as `WRONG_FIBRE_SUBGROUP`. In S3 it also checked all six prescribed pairs of left cosets of index-2 and index-3 subgroups; all meet in one point. A false unconditional common-point claim was rejected as `NO_COMMON_POINT`.
* The at-most-two-point Helly cases were enumerated. Pairwise-intersecting line triples in F_2^2 and F_3^2 were rejected as `EMPTY_TRIPLE` when the respective index-4/index-3 exclusions were removed from the abstract quotient argument. These negatives show why that proof's hypotheses matter; they are **not** claimed counterexamples to the full extension theorem. The cyclic-CRT unique-lift misstatement was rejected as `MULTIPLE_LIFTS`.
* For p=11, the checker enumerated all 28 subgroups and 762 cosets of Q and all 70 subgroups and 2794 cosets of G. Completeness uses the coprime binary/odd splitting and the complete list of subspaces of F_11^2 (zero, 12 lines, whole space). It exhaustively searched allowable bad packings using at most one p-divisible index, obtaining B_7(Q)=2 and B_7(G)=4. It directly checked the three index-11 cosets, pairwise intersections of two points and empty triple; their attempted low-gcd-overlap use was rejected as `QUOTIENT_GCD_EXCEEDS_THREE`.
* One hundred labels of the index-2 subgroup were checked to have pairwise gcd 2; the artificial bound 99 was rejected as `REPEATED_LABELS_EXCEED_BOUND`. This is only a repeated-label arithmetic control, not a check of an unprovided J_7 definition.

These bounded calculations support the written arguments and intended-reason negatives; they do not prove the general theorem by enumeration, establish novelty, or replace independent-model-family, human, Lean/kernel or parent review. No build, linter, formatter, solver, or other test run was performed.

## Residual and disposition boundary

The written theorem remains conditional on its abelian quotient, no-index-3/no-index-4 hypothesis (automatic only in the stated B_7(Q)<=2 corollary), and the two factor B_7 bounds. It does not prove original Sun8 for arbitrary groups, for all groups with abelian quotient under factor Sun8 alone, or for arbitrary normal extensions. For general r,s even the stated Ramsey upper bound need not reach 7. The illustrative finite-J, mu and older-interface labels need their exact definitions in an independently authorized later comparison; no additional source has been opened here. Scientific priority, formal verification, distinct-model-family or human review, historical process adjudication and parent acceptance remain separate.
