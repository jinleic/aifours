# f151 — independent same-harness review of the consolidated source-free support criteria

## Verdict and exact scope

**CORRECT at the stated mathematical scope. FATAL 0 / MAJOR 0 / MINOR 0.** All four index-family bounds, the four stated sufficient conditions, the elementary simple-group applicability argument, and the distinction between integer witnesses and actual cosets withstand independent reconstruction. This is a review recommendation, not a parent adoption or an independent-model-family, human, formal/kernel, classification, or novelty certificate.

Let G be finite; let μ be its least proper-subgroup index (∞ for the trivial group), Y the primes in {2,3,5,7} dividing |G|, and k the number of distinct primes >7 dividing |G|. In this review, **Sun8(G)** means precisely: every eight pairwise disjoint left cosets of subgroups of G have two subgroup indices with gcd at least 8. No seven-index assertion or source-specific “P7” equivalence is inferred from that name.

For a family of N≥2 pairwise disjoint left cosets with all pairwise index gcds ≤7, the per-bound verdicts are:

| Bound | Exact hypotheses in addition to the preceding family assumptions | Independently reconstructed conclusion | Verdict |
|---|---|---|---|
| 1 | μ≥8 | N≤k+5 | VALID |
| 2 | μ≥8 and (2∉Y or 3∉Y) | N≤k+|Y|≤k+3 | VALID |
| 3 | μ≥13 and |Y|≤2 | N≤k+2 | VALID |
| 4 | μ≥13 and |Y|≤3 | N≤k+4; bounds 2–3 remain available on their own hypotheses | VALID |

The word “or” in bound 2 is inclusive, and μ≥8 is required in either alternative. No hypothesis is dropped in these verdicts.

## 1. Frozen inputs, verification, and source order

Manifest: `manifest-v1.json`, SHA-256 `c92cf3011beb60b23c51fb00eded8383564c9654ef7c05df8d682573e10da1fe`, 3432 bytes, 44 LF. The manifest was read first, including its initially truncated requirements line through an exact raw reread. Every input below had its complete SHA-256, byte length, and LF count checked against the manifest **before interpretation**, then was read completely in the declared order:

| Order | Input basename | SHA-256 | Bytes | LF |
|---|---|---|---:|---:|
| 1 | `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 | 56 |
| 2 | `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 | 11 |
| 3 | `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 | 10 |
| 4 | `frontier-20261028-source-free-support-consolidated-v1.md` | `eefaac6481bd7d5d40945f44863ce474fcfb2aaf5c8c6031a3494aa84ecd7f37` | 11092 | 72 |

All four inputs are under `mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`. The initial metadata verification's observed native clock was `2026-10-28T21:45:11-0700 PDT`; the supplemental execution receipt independently binds the same metadata. The overlays remain binding: their false seven-index exclusion and withdrawn P7 wording are not revived. Their referenced historical scientific files were not opened or used as premises.

Mathematical source exposure for this assignment was the four manifested inputs. Administrative skill/memory guidance was also read. No author checker or other author executable was imported or executed. No Git, web search, external model/API, author contact, source edit, deletion, publication, or infrastructure mutation was performed. Mathematical output files are confined to this review directory; local scratch copies were used to transfer reviewer-authored text. No unrelated build, lint, test, or formatter was run.

## 2. Reduction from disjoint cosets to a constrained integer family

Every subgroup H_i is proper: the sole left coset of G is G, which meets every other nonempty coset. Thus m_i=[G:H_i]≥μ and m_i divides |G| by Lagrange.

For finite H,K≤G, the map from G/(H∩K) to G/H × G/K taking a left coset to its two left cosets is injective. Consequently [G:H∩K]≤[G:H][G:K]. It is divisible by each subgroup index. If the two indices are coprime, their product divides [G:H∩K], so equality holds. Then |HK|=|H||K|/|H∩K|=|G|, hence HK=G. For any a,b∈G, writing a⁻¹b=hk with h∈H,k∈K gives ah=bk⁻¹ in aH∩bK. Thus coprime-index cosets always intersect.

The disjoint family therefore has **2≤gcd(m_i,m_j)≤7** for every distinct pair. Since N≥2, each index shares a prime with another index. That prime must be one of {2,3,5,7}. With T_i={p∈Y:p divides m_i}, each T_i is nonempty and every two supports meet. The product of distinct primes in their intersection divides the pairwise gcd. The only possible two-prime intersection is {2,3}; three-prime intersections are impossible. Every prime >7 can appear in at most one index.

For μ≥8, repeated index values themselves are impossible: equal indices would have gcd equal to that value, ≥8. This is not the erroneous assertion that pairwise-coprime cofactors cannot repeat the value 1. The μ hypotheses, not any restriction on unit cofactors, do the necessary work.

## 3. Bound 1: μ≥8 gives k+5

### A common small prime

When p divides every index, any resource r in the following table is one-use because lcm(p,r)>7. Each of the k large primes is separately one-use. Avoiding every listed resource and every large prime leaves exactly the values in the third column.

| Common p | Small resources | Resource-free indices | Those still ≥8 |
|---|---|---|---|
| 2 | 8, 9, 5, 7 | 2,4,6,12 | 12 only |
| 3 | 4, 9, 5, 7 | 3,6 | none |
| 5 | 2, 3, 7, 25 | 5 | none |
| 7 | 2, 3, 5, 49 | 7 | none |

In the first row, the exceptional value 12 can occur only once, since two such indices have gcd 12. All other indices can be assigned a resource, with no resource assigned twice. This gives k+5 in the first row and k+4 in the others. Arbitrary higher powers of 7 are covered by the resource 49; there is no hidden restriction on v_7(|G|).

### Empty common-prime intersection: exhaustive four-type argument

A singleton support would force its prime into every support, so every distinct support has size at least two. Work on U={2,3,5,7}, allowing unused primes in the ambient universe.

* A four-element support can coexist only with the pair {2,3}: its intersection with any other nonsingleton support is that whole support, whose prime product must be ≤7. This cannot give empty total intersection, so no four-element support occurs here.
* With no triples, the supports are pairwise-intersecting edges of K4. Such an edge family is a star or a triangle, with at most three edges.
* Two different triples can coexist only when their intersection is {2,3}; they must then be {2,3,5} and {2,3,7}. The only pairs compatible with both are {2,3} and {5,7}, which are disjoint and cannot both occur. Thus this case has at most three types, and a third triple is impossible.
* With exactly one triple T and missing point d, each compatible pair is {x,d} for x∈T, except that {2,3} is also allowed if it is contained in T. If T omits 2 or 3 there are at most three such pairs. If T={2,3,c}, the extra pair {2,3} is disjoint from {c,d}, so again at most three of the pairs can coexist. Including T gives at most four types.

This is exhaustive, independent of any author finite-coloring certificate. The separate exact enumeration found 23 valid empty-common-intersection families and exactly six of maximum size four.

Every nonsingleton type other than {2,3} has prime product ≥10, so it occurs at most once. An index of type {2,3} must use 4, 9, or a large prime: otherwise it is 6<8. Those are one-use within that type, since sharing 4 forces gcd at least 12 and sharing 9 forces gcd at least 9. Thus that type contributes at most k+2 labels, and at most three other types contribute one each. If {2,3} is absent, there are at most four indices. In every case N≤k+5.

## 4. Bound 2: one of 2,3 absent

Here every product of two distinct primes in Y exceeds 7, and |Y|≤3.

If p is common, take every other prime in Y and the least p-power >7 as small resources, together with the k large primes. Two indices using any of these small resources have gcd at least lcm(p,r)>7. Resource avoidance leaves a pure p-power ≤7, excluded by μ≥8. There are |Y| small resources, proving N≤k+|Y|.

If no prime is common, supports are nonsingletons and none can repeat. A three-element support cannot coexist with any other nonsingleton type, since the intersection would contain two primes with product >7. The empty-common case is therefore possible only for |Y|=3 and all three pair supports. It has N=3≤k+|Y|. For |Y|≤2 this case is empty, not a use of the false inequality 3≤k+|Y| at smaller |Y|. Bound 2 follows.

## 5. Bound 3: μ≥13 and at most two small primes

Pairwise-intersecting nonempty subsets of a universe of at most two elements have a common element: any singleton forces it, and otherwise every support is the full pair. An empty Y permits no family with N≥2 at all.

For Y={2,3} and common 2, resources 8 and 9 leave only 2,4,6,12, all below 13. For common 3, resources 4 and 9 leave only 3,6. For every other one- or two-prime Y, use the other small prime if present and the least p-power >7. The product of distinct primes is then >7, and resource avoidance leaves only a p-power ≤7. Thus at most two small resources, together with k large-prime resources, cover all indices: N≤k+2.

The threshold 13 really excludes the exceptional index 12 in the {2,3}, common-2 argument. The independent mutation (12,16,18), with pairwise gcds 4,6,2, violates k+2 at k=0 if the threshold is weakened to 12.

## 6. Bound 4: three-small-prime aggregation

Cases with |Y|≤2 use bound 3; cases missing 2 or 3 use bound 2. Otherwise Y={2,3,d}, d=5 or 7.

If a prime is common, the small resources are (8,9,d) for common 2; (4,9,d) for common 3; or (2,3,d²) for common d. Resource-free indices are respectively {2,4,6,12}, {3,6}, or {d}. All are below 13. Therefore this part actually gives N≤k+3.

If no prime is common, the triple {2,3,d} could coexist only with {2,3}; that would have nonempty common intersection, so the triple is absent. All three pair types {2,3}, {2,d}, {3,d} must occur: any two alone share a prime. The first type contributes at most k+2 indices using 4,9 and the globally available large primes. Each of the other two types contributes at most one because its prime product exceeds 7. Thus the aggregate is (k+2)+1+1=k+4, not three separate large-prime budgets. Sharing resources between these types could only reduce the number, not increase it. This proves the stated bound with its stated μ≥13 hypothesis.

No assertion that every listed μ hypothesis is optimal is required or made. The stronger-than-needed nature of a sufficient hypothesis is not a mathematical defect.

## 7. Sufficient conditions (i)–(iv)

A Sun8 counterexample would supply N=8 with every index gcd ≤7. The bounds exclude it as follows:

| Condition | Exact hypotheses | Upper bound on N |
|---|---|---|
| (i) | μ≥8, k≤2 | k+5≤7 |
| (ii) | μ≥8, (2∉Y or 3∉Y), k≤4 | k+|Y|≤k+3≤7 |
| (iii) | μ≥13, |Y|≤2, k≤5 | k+2≤7 |
| (iv) | μ≥13, |Y|≤3, k≤3 | k+4≤7 |

These are alternative sufficient conditions, not necessary conditions or a classification. The same reasoning also rules out any larger family with all pairwise index gcds ≤7, since an eight-member subfamily would already contradict the relevant bound.

## 8. Simple-group applicability; alternating examples

For finite nonabelian simple S and proper H<S, the kernel of the action on S/H is the core of H, a normal subgroup contained in H. Simplicity and properness force the kernel to be 1. Hence S embeds in the symmetric group of degree m=[S:H]; Lagrange gives |S| dividing m!. If r is the largest prime dividing |S|, then r divides m! and therefore r≤m. This proves μ(S)≥r without a small-index subgroup classification.

If k≥1, r≥11, so μ≥11≥8. If k≥2, r≥13, so μ≥13. It follows exactly as claimed that Sun8 holds for such S in each of these ranges: 1≤k≤2; 1≤k≤4 with 2 or 3 absent; 2≤k≤5 with |Y|≤2; and 2≤k≤3 with |Y|≤3. The proof does not assert that these classes are populated or infinite, nor identify all groups in them.

For the stated A_n examples, the additional elementary group-theory dependency is the standard simplicity of A_n for n≥5. This is **not** CFSG. With that fact, if a proper index m<n existed, the faithful action would force n!/2≤m!≤(n−1)!, impossible for n≥5. Thus μ(A_n)≥n. This order argument, not merely the largest-prime bound, is needed for n=8,9,10. In 8≤n≤13, k is respectively 0 for n=8,9,10; 1 for n=11,12; and 2 for n=13. Bound 1 applies in each case. The supplemental control checked these factorial/order inequalities and prime counts exactly, but arithmetic computation is not presented as a proof of simplicity.

Nothing in this review adopts the separately cited small-degree A5–A7 packets, n≥14 Nagura/Jordan result, their historical dispositions, or the withdrawn seven-index statement. Those referenced bodies and source statements were not reviewed. Bounds 1–4, conditions (i)–(iv), and the simple-group remark do not depend on them.

## 9. Integer sharpness is not coset sharpness

For arbitrary distinct primes q_i>7, the candidate's four integer lists have the stated cardinalities, lower bounds, small-prime supports, and pairwise gcds in 2,…,7:

* 8,12,18,20,28 and 6q_i: k+5, lower bound 8, Y={2,3,5,7}.
* 8,10,14 and 2q_i: k+3, lower bound 8, Y={2,5,7}.
* 16,18 and 6q_i: k+2, lower bound 13, Y={2,3}.
* 24,18,20,15 and 6q_i: k+4, lower bound 13, Y={2,3,5}.

Their entries all divide a common integer, for example their least common multiple. Since every q_i is >7 and absent from the fixed base entries, gcd(6q_i,b)=gcd(6,b), gcd(2q_i,b)=gcd(2,b), and distinct variable entries have gcd 6 or 2. This checks the arbitrary-k pattern; the executable additionally checked all four lists for k=0,…,5 using q_i=11,13,17,19,23.

These witnesses establish sharpness of the **integer-divisor relaxation only**. A lower bound on these integers is not the claim μ(G)≥that number for any realizing group. No group with the required minimum index is constructed, no subgroups realizing the lists are constructed, and no disjoint cosets are constructed for the positive witnesses. The candidate expressly makes the same distinction. There is no group-sharpness or Sun8-counterexample conclusion.

## 10. Independently authored controls and actual execution evidence

### First control: capped-divisor graph and support enumeration

`reviewer-control-v1.py` was authored in this review without importing author code. Its observed execution was Python 3.14.3, from native pre-command clock `2026-10-28T21:54:53-0700 PDT` through `2026-10-28T21:55:25-0700 PDT`; it exited successfully. It enumerated all 15 nonempty Y⊆{2,3,5,7}, k=0,…,3 and lower thresholds 8 and 13: **120 distinct-vertex divisor-graph maximum-clique computations, with zero violations of any applicable stated bound**. It also enumerated support families and deliberate mutations.

For these positive cases, the graph reduction is complete: cap exponents at 2^4,3^3,5^2,7^2 and large primes at exponent 1, relabelling the distinct large primes to 11,13,17. Pairwise gcds in 2,…,7 are unchanged. A changed small-prime exponent leaves the resulting number at least 16,27,25, or 49. Any index using a relabelled large prime and a nonempty small support is at least 22. Thus lower thresholds up to 13 are preserved. Distinctness follows because two equal truncated numbers ≥8 would have gcd ≥8. Every capped divisor is itself an integer-relaxation candidate. An empty small support cannot belong to a family of size ≥2, so omitting it is harmless for the bounds. These calculations are bounded controls; the arbitrary-k written proof is supplied above.

**Reviewer-control correction, preserved rather than silently edited:** the first script's introductory wording “exact relaxation maximum” was too broad for its μ=6/7 mutation probes or gcd-cap-8 mutation, because its graph has distinct vertices, whereas indices ≤the gcd cap can repeat in a multiset family. Its positive μ≥8, cap-7 computations are unaffected. The negative probes' explicit distinct-integer witnesses remain valid, but their finite set maxima are not upper bounds on multiset families. Its μ=7 set probe and minimum-support-size-1 probe did not produce intended failures and are not counted as successful negative controls. This is a limitation of the reviewer's first control, not a defect in the candidate. The original script and output are retained unchanged; the supplemental control's header and output record this correction.

### Supplemental control: resource exhaustiveness and asserted intended-reason mutations

`reviewer-resource-control-v2.py` is a separate stdlib-only implementation, importing neither the author code nor the first reviewer script. It actually ran with start and end native clock both `2026-10-28T21:59:21-0700 PDT`; all assertions passed and an execution receipt was created. It verified:

* 46 exact resource-free divisor cases, covering every common-prime resource allocation needed in bounds 1–4, including all one- and two-prime universes and both d=5,7.
* All support families on the four-small-prime universe: maximum four, 23 valid families, six maximum-size families. On {2,3,d}, the unique empty-common-prime family is exactly the three pair types.
* 24 positive sharpness-list instances (four patterns for each k=0,…,5).
* Five asserted negative mutations, each satisfying the mutated assumptions and exceeding the corresponding mutated bound for the intended reason:
  * μ≥7 in place of μ≥8: seven repeated indices 7 exceed k+5=5; index repetition is now permitted. As an actual finite-group check, the seven singleton cosets of the trivial subgroup in the cyclic group C7 were explicitly constructed and checked pairwise disjoint. This is a seven-coset counterexample to the weakened bound, **not** an eight-coset Sun8 counterexample.
  * μ≥12 in place of μ≥13 in bound 3: (12,16,18) has size 3>2, since the exceptional base value 12 is no longer excluded.
  * Removing the missing-2-or-3 hypothesis from bound 2: (8,12,18), Y={2,3}, has size 3>k+|Y|=2; sharing the pair {2,3} is now possible.
  * Allowing |Y|=4 in bound 4: (24,18,20,15,42) has size 5>4; the fourth small prime permits an additional support type.
  * Raising the gcd cap from 7 to 8: (8,10,12,14,16,18) has size 6>5; resource 8 is no longer one-use.
* Eight deliberately reused resources rejected by explicit gcd>7: common-2 resources 8,9,5,7; common-3 resource 4; resources 25,49; and a large prime 11.
* Exact order/factorial arithmetic for A_n, 8≤n≤13.
* The manifest and all four input metadata again, before those supplemental computations.

Relaxing the support-intersection product cap from 7 to 15 was a further sensitive negative control: maximum distinct support-family size rose from four to six. No failed or insensitive mutation is passed off as a successful sensitivity check.

### Hash binding

All names below are relative to this review directory. The supplemental receipt includes live SHA-256/bytes/LF metadata for its script, output, the earlier script/output, and Python/argv/clock fields.

| Artifact | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `reviewer-control-v1.py` | `9bbd2220b7bf14afd5d224df2295eb2b8c98a726200f6a2494b03ffa2f80a04c` | 8381 | 186 |
| `reviewer-control-v1-output.json` | `0b059fda0eb6b0b24cb6f8190c80226015334d34c21fea4d560691dd561bc65a` | 43866 | 3656 |
| `reviewer-resource-control-v2.py` | `6b965ae19c562929a1cb040a0d8dd6f928bcf1607112ca1a3d3cc9f23806275c` | 12706 | 279 |
| `reviewer-resource-control-v2-output.json` | `6ee7535d007dd9c055cfc987c7bf067a4bfed2ddbb6cc24852a1025ff4f31889` | 40193 | 2360 |
| `reviewer-resource-control-v2-receipt.json` | `afaa4ca80b359cdc872d05935ce8f258f5535baaa0f411deb83adfc362d0639d` | 1784 | 38 |

## 11. Dependency ledger and limits on conclusions about finite groups

Load-bearing mathematical dependencies are integer prime factorization, gcd/lcm arithmetic, finite coset cardinalities and Lagrange's theorem, the proved coprime-index intersection lemma, the explicitly reconstructed finite support-family argument, and one-use-resource counting. The simple-group corollary additionally uses only the defining simplicity property and the permutation action on cosets. The alternating examples additionally use the standard elementary theorem that A_n is simple for n≥5, with their index lower bound independently derived here from its order. No classification of maximal subgroups or finite simple groups is used.

**What is established about actual finite groups:** every finite G satisfying any one of conditions (i)–(iv) has the exact eight-disjoint-coset property defined above. More generally its disjoint-coset families with pairwise index gcds ≤7 obey each bound whose hypotheses it satisfies. The listed simple-group consequences follow from the proved faithful-action lower bounds. These are genuine conditional-on-the-displayed-group-invariants group statements, not merely facts about the integer examples.

**What is not established:** unrestricted Sun8 for arbitrary finite groups; all-simple Sun8; seven-index exclusion; results for groups failing every displayed hypothesis; realization or optimality of the integer maxima by actual subgroup/coset families; any classification or infinitude of the sufficient classes; the cited small-degree or n≥14 historical results; novelty, priority, publication readiness, human review, independent-family review, or formal/kernel verification. No Sun7, R8, Sun3, Jones, Jordan, Nagura, CFSG, held historical result, or author “PASS” claim supplies a premise to this review's conclusions.

There is no unresolved mathematical blocker in the assigned consolidated source-free scope. Parent disposition remains a separate action.
