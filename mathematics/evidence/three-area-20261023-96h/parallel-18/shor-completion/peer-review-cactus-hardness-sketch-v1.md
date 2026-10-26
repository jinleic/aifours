# v47-A — written review of cactus portal composition and the conditional hardness sketch

Reviewer MathShor-2, math-5. Observed clock before creation: **Sun Oct 25 07:09:12 PDT 2026** (`/bin/date`). Output solely in the assigned reviewer root.

## 1. Frozen source, exposure and actual coverage

Source **A**:

`information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/replacement-information-primary-screen-v5-cactus-hardness-sketch-v1.md`

SHA-256 `5c961bb5115861285dec23a6519ad04e348e725657fd287e5d00f4a58d2459b8`, full LF1–300 read.

Literal packet: `institute/runs/three-area-2026-10-23-96h/peer-review-wave-v47-cactus-hardness-sketch-sources-v1.md`, SHA-256 `42b482ea41f46c2350560ec1b1dd45b5af5f89bf25acd0638d2811a7dfb29abf`. Packet LF1–153 and154–307 were read consecutively, covering every declared source line. Load-bearing packet LF68,77,79,89,94,95,98,104,122,129,137,139,147,155,161,163,169,176,183,189,191,205,207,223,225,226,232,235,237,239,249,256,258,260,271,305 were reread raw. Manifest LF40 was explicitly recovered raw after its displayed truncation. No unresolved load-bearing truncation remains.

Manifest v47-A, SHA-256 `5cbe412586afd74a65ee3073962fc9cee65855825916c875a49610a0810fcb2c`; complete packet receipt read. Manifest, packet and actual source hashes were freshly observed and match. The receipt's literal-equality claim was not substituted for body reading.

ACK before proof body: `peer-review-cactus-hardness-sketch-ack-v1.json`, SHA-256 `46dce639a917a6b2a2243cf4b09fc24db9f496555135f8355c1dfe97bd3e2548`. Prior exposure is disclosed there. Parent v8 was read FIRST and in full; v7/HOLD remain binding. This is a math-to-information-science cross-domain, same-harness supplied-proof review, not blind/cross-vendor/human/formal/novelty acceptance.

No scientific interpreter, program, eval, enumeration, symbolic calculation, replay, solver, external CLI or nested agent was used. All mathematics below is written reconstruction; tools were source reads, metadata clocks/hashes and file creation.

## 2. Per-piece disposition

| Requested piece | Written disposition | Exact boundary |
|---|---|---|
| (a) Portal/articulation/full cycle-block state, all ties, arbitrary k | **0 FATAL / 0 MAJOR / 0 MINOR** | Exact sufficient state and possibly exponential composition; NOT a polynomial table/frontier/cycle-pattern bound. |
| (b) The2^m mass family AND its dominance argument | **0 FATAL / 0 MAJOR / 0 MINOR** | Both reconstructed, including the subtle invariance of active-leaf/base interactions. Dominance is within the displayed subfamily, not a one-state theorem for the full legal envelope. |
| (c) Fixed-guard dyadic payload | **0 FATAL / 0 MAJOR / 0 MINOR** | Exact compact graph encoding of a mass under fixed guards; not a two-state item, cost calibration or guard-forcing gadget. |
| (d) Many-tie two-selection crossover | **0 FATAL / 0 MAJOR / 0 MINOR** | Exact comparison of two legal equal-size sets and reversal in actual completions; neither is proved globally optimal or exposed on the complete envelope. |
| (e) SUBSET-SUM square-gap template | **0 FATAL / 0 MAJOR / 0 MINOR for the CONDITIONAL algebra**, with the stated constant-fixture qualification | The required actual calibration/equal-budget realization, lossless unrestricted-site normalization, guard forcing and portal/bypass exclusion are **NOT_RECONSTRUCTED / NOT_PROVED** because no such construction is supplied. This is not an error in a hardness theorem: no hardness theorem is claimed. |

The per-piece derivations follow. The missing graph realization is not silently included in the no-defect arithmetic verdict.

## 3. Exact objective and the portal state — piece(a)

### 3.1 Endpoint convention and ordered/unordered normalization

A:11–36 freezes a finite simple connected unweighted cactus, arbitrary0<=k<=n and ALL shortest paths, including selected endpoints. Its q is the fraction avoiding C, so each ordered pair contributes1-q to GBC. Undirected path reversal gives q(x,y)=q(y,x), hence exactly

```text
GBC=n(n-1)-2*Beta,
Beta=sum_unordered q.
```

The zero-length portal convention1 if unselected and0 if selected is necessary for treating an attached root vertex on the same footing as its descendants. It is used correctly in w_i below. This is not a unique-path surrogate or a weighted-site variant.

### 3.2 Articulation theorem and dominance state

For H,K meeting ONLY at v, a shortest cross-side path must pass through v. A detour into another side and back has positive length, so it cannot shorten an internal geodesic. Every cross-side geodesic is uniquely a shortest H path to v followed by a shortest K path from v, and every such combination occurs. Both the total and avoiding counts multiply, giving product avoidance fractions.

Pairs internal to H/K, including their distinct portal pairs, are disjoint; the remaining cross-interior sum is alpha_H*alpha_K. Thus

```text
alpha_union=alpha_H+alpha_K,
beta_union=beta_H+beta_K+alpha_H*alpha_K.
```

If v is selected all alpha terms are0, and the same formula remains valid. With a excluding the portal, a-values add and the shared flag epsilon is counted once in the eventual exact k. Vertex counts are fixed graph data, not adjustable state parameters.

For fixed outside selection the H-dependent objective is beta_H+z*alpha_H, with z=alpha_out>=0. Therefore componentwise dominance at the SAME(a,epsilon) is lossless, and a lower envelope for all z>=0 is sufficient. Attainability matters for a necessity/lower-bound claim. The text does not prove that the state is a minimal statistic or that its complete envelope has many pieces; only exact sufficiency is reconstructed.

### 3.3 Cycle blocks retain every shortest-path tie

For a cycle with attached H_i, summing q(x,v_i) over all x in H_i gives exactly

```text
w_i=(1-epsilon_i)+alpha_i.
```

The first term is its root vertex's zero-length path; descendants give alpha_i. For i!=j, all geodesics between attachments combine the two child geodesics with a shortest cycle arc. No descendant provides a shortcut between two cycle vertices because it has only its own articulation attachment. A cycle has one shortest arc except at even-cycle antipodes, where BOTH equal arcs must be counted. The fraction h_ij is therefore exactly0,1/2 or1 and includes all selected cycle vertices/endpoints.

The Cartesian-product count proves

```text
beta_total=sum beta_i+sum_(i<j) h_ij*w_i*w_j,
alpha_total=alpha_0+sum_(i>=1) h_i0*w_i.
```

If a cycle vertex is selected both its child mass and relevant arc fractions vanish; there is no erroneous nonzero endpoint factor. Budgets are `sum a_i+sum_(i>=1)epsilon_i`, with root flag epsilon0 separate. This handles arbitrary cycle lengths and arbitrary selected positions, not odd cycles only.

For completeness, edge blocks need no hidden unique-cycle assumption. A parent vertex v joined by one edge to a rooted child K at w has `w_mass=(1-epsilon_w)+alpha_K`, and state

```text
alpha_new=(1-epsilon_v)*w_mass,
beta_new=beta_K+(1-epsilon_v)*w_mass,
a_new=a_K+epsilon_w.
```

Other components at v then merge by the articulation formula. A singleton root has alpha=beta=0. These elementary bases plus edge/cycle/block-cut composition cover every finite cactus and all exact cardinalities, including k0 and k=n.

This is an EXACT potentially exponential DP description. Enumerating selected cycle patterns or achievable pairs need not be polynomial. Neither this review nor A:93 proves polynomial state count or efficient cycle-pattern processing.

### 3.4 Bit size is correctly separated from number of states

Along a cactus block route, every avoided shortest-arc fraction is0,1/2 or1; the route combines independent tied block choices. With c cycles the denominator divides2^c. Summing at most n vertex terms or n(n-1)/2 pair terms gives numerators bounded by those counts times2^c. Hence each rational state has O(c+log n) bits (up to a constant-factor pair-count term), polynomial in graph size. This does not bound how many distinct numerators or lower-envelope states can occur.

## 4. The2^m family and its ACTUAL dominance proof — piece(b)

The m squares share only consecutive portals. They contribute3m+1 vertices; the m pendant leaves make4m+1. Choosing one of a_i,b_i for each i uses exactly m sites and leaves root v0 unselected.

For v_i the m-independent block product is2^-i. The unselected arm at stage i reaches its upper portal by the unique one-edge segment, followed by i-1 half factors; its fraction is2^(-(i-1)). The selected arm contributes0. The sum of those bare contributions is3(1-2^-m). A leaf at a_i contributes0 when a_i is selected and2^(-(i-1)) otherwise. This gives R1 exactly.

Multiplication of the variable part by2^(m-1) gives the ordinary binary weights2^(m-i). Every one of2^m bit strings has a distinct mass at the SAME budget/flag. This proves a raw-table lower bound for a method storing every feasible mass, not for every algorithm or the relevant envelope.

### The delicate invariance in R2 is valid

A:130 could be misread as invoking an automorphism of the entire leaf-decorated graph, which generally is NOT an arm-swap automorphism. The needed argument is narrower and valid: shortest paths between base vertices never enter pendant leaves, so their metric/path counts equal those of the bare chain. Arm swaps of that bare chain preserve its missed mass under the corresponding chosen arms.

For a fixed active leaf i, epsilon_i=1 fixes its parent a_i unselected and b_i selected. Paths from that leaf to base vertices again ignore every OTHER pendant leaf. Swapping other squares' arms is an automorphism of this restricted metric problem that fixes a_i and preserves the summed base endpoints. Thus its summed interaction L_i is independent of other bits. Positivity is immediate from its pair with its own unselected parent, whose avoidance fraction is1.

One can make the dependence completely explicit in writing. Split the base at a_i into its parent, the upstream bare chain including v_(i-1), and the downstream chain including v_i. The two rooted bare-chain masses have lengths i-1 and m-i, so

```text
L_i=1+[1+3(1-2^(-(i-1)))]+[1+3(1-2^(-(m-i)))]
   =9-3*2^(-(i-1))-3*2^(-(m-i))>0.
```

For two active leaves i<j, their own-square segments to the appropriate portals are unique and unblocked. Exactly j-i-1 intervening squares contribute one half each. Thus their avoidance fraction is exactly2^(-(j-i-1)), including adjacent i,j where it is1.

This reconstructs R2 with the SAME beta_base and positive L_i, not merely a heuristic monotonicity claim. Inactive leaves are separated from every other vertex by a selected parent, so they contribute0. Every nonzero bit vector has both a strictly larger alpha and a strictly larger beta than the all-zero choice. Therefore all its nonzero states are dominated WITHIN THIS SUBFAMILY. The all-zero state itself may be beaten by a different legal selection outside the subfamily; no statement about the complete envelope size follows. The author's negative control is sound.

## 5. Fixed-guard dyadic encoding — piece(c)

Selecting all a_i and placing a digit leaf at the unselected b_i gives exactly the same bare mass plus the digit contributions2^(-(i-1)). For the m-bit integer

```text
w=sum_i d_i*2^(m-i),
```

its contribution is2^(-(m-1))*w. Taking m=M+1 yields delta*w for delta=2^-M; leading zeros are harmless. The graph needs O(m) squares/leaf sites, not w sites, so the mass encoding is genuinely compact in binary input length.

This proves only the conditional encoding FACT. Digits are part of graph geometry here, and the guards are fixed selections. No single equal-cost vertex choice is proved to turn a whole payload on/off. No associated beta difference has been calibrated. Leaf/base and leaf/leaf interactions are real positive pair terms and cannot be assigned away. A:156 states these restrictions correctly.

## 6. Exact many-tie preference reversal — piece(d)

The comparison graph has3m+3 vertices; both X and Y select m guards plus one extra vertex. The root remains unselected. Let e=2^-m, m>=2. Bare mass is3(1-e), with terminal x contribution e, so its prefix has mass3-4e.

In X, selecting x blocks x and its leaf l from the portal, while the unselected dummy d adds1. Thus alpha_X=4-4e. In Y, d is selected while x and l each contribute e, giving alpha_Y=3-2e. Their difference is1-2e>0.

For internal beta, the bare-chain endpoint sum from x to its other bare vertices is3(1-e), by chain reversal preserving the fixed guards. Selecting x removes two copies of that sum for x-prefix and l-prefix pairs, plus x-d and l-d with fractions e each, plus x-l with fraction1. Total removed mass is7-4e.

There is no omitted positive avoiding prefix-prefix pair through x: a simple path through x internally must use both a_m and b_m (a pendant l cannot be an interior detour), and a_m is already selected. Any such shortest path was already nonavoiding. This is the necessary justification of A:182.

Selecting the leaf d affects only pairs with d. Their total is1 for root plus bare mass3(1-e) plus l's e, namely4-2e. Hence beta_Y-beta_X=3-2e and exactly

```text
F_X(z)-F_Y(z)=-(3-2e)+z*(1-2e).
```

The crossover exceeds3 by `4e/(1-2e)` and is at most5 because `5-crossover=(2-8e)/(1-2e)>=0` for e<=1/4. At z0 X wins; at z6 Y wins since the difference is3-10e>=1/2>0. Both z values are ACTUAL compatible completions: no outside vertices, or six unselected pendant vertices at the root. Their outside beta is constant between X and Y, so the comparisons are legitimate.

A third internal selection or selecting an outside/root vertex could beat both. The proof establishes neither line's membership in the COMPLETE lower envelope. The author explicitly does not claim it, and no exponential frontier conclusion follows.

## 7. Conditional square-gap reduction algebra — piece(e)

Let W=sum w_i and choose M with2^M>W. Then delta=2^-M and tau=delta*T have polynomial bit description, and `sum a_i=delta*W<1` for a_i=delta*w_i.

Assume, CONDITIONALLY, an actual graph realizes all the stated local states with both bit choices using the required per-item budget, fixed root flag0, and a proved lossless normalization of every threshold-relevant unrestricted selection. Ignore only a fixture contribution that has truly been proved CONSTANT, as A:249 requires; the caveat below is essential.

Expanding the articulation cross terms gives the b_i linear coefficient

```text
c_i+a_i*sum_(j!=i) A_j.
```

Under H1 this is a_i²/2-tau*a_i. The remaining cross terms are `sum_(i<j) a_i a_j b_i b_j`. With b_i²=b_i and s=sum a_i b_i, these combine EXACTLY to s²/2-tau*s. Therefore

```text
beta_total=K+(s-tau)²/2,
K=sum B_i+sum_(i<j)A_i A_j-tau²/2,
```

plus the declared constant fixture term. There is no missing factor2 from ordered pairs: beta is unordered and conversion to GBC happens only afterward.

If the SUBSET-SUM equality holds, s=tau and beta=K. Otherwise the integer difference of sums has absolute value at least1, so |s-tau|>=delta and beta>=K+delta²/2. Thus the exact ordered GBC threshold is

```text
N(N-1)-2K,
```

and NO canonical selection reaches it, with ordered gap at least delta². Conditional on a polynomial-size actual output and normalization proof, all state constants are dyadic shortest-path sums with polynomial bit lengths, and K/threshold arithmetic also has polynomial bit length. This is an exact binary threshold argument, not floating arithmetic or an implicit unary-weight construction.

### Fixtures are NOT automatically constants

The literal phrase “exactly declared constant fixture contribution” must remain part of the conditional claim. If a fixed fixture attached to the common root has avoidance mass z_F, articulation adds

```text
beta_F+z_F*sum_i A_i+z_F*s,
```

not just a constant. One would need z_F=0 or calibrated coefficients with an ADDITIONAL `-z_F*a_i` term in H1 (equivalently include the fixture as a fixed branch in the baseline sum). This elementary accounting amendment does not construct such a fixture or preserve a forcing argument for free. It is why I do not interpret “all fixture contributions accounted for” as an automatic license to drop their selection-dependent effects. With its stated constant-fixture qualification, the conditional algebra is correct; arbitrary nonconstant fixtures are outside that proven identity.

Likewise, both local bit choices must fit the same agreed global exact-cardinality scheme and every subset bit string must give a legal k-set. A lossless normalization must not increase beta (equivalently must not decrease GBC). Otherwise even the conditional square identity would not be a reduction from ordinary SUBSET-SUM. These are part of the requested realization/forcing obligation, not conclusions established by Claims B or T.

## 8. Why the unresolved graph gap is substantive

The missing actual graph pieces are NOT_RECONSTRUCTED/NOT_PROVED, as the source acknowledges:

1. **Mass is not a selectable item.** Claim B compactly describes one fixed-guard payload graph, not two equal-budget states in one graph with a common bit coherently toggling all binary digits.
2. **Tradeoff is not calibrated cost.** Taking Y as baseline and X as bit1 in Claim T gives `a=1-2e`, `c=-(3-2e)`, so c/a is the specific ratio `-(3-2e)/(1-2e)`, between-5 and-3. H1 instead requires c_i/a_i=a_i/2-tau-sum_(j!=i)A_j, depending on the entire instance and all baselines. There is no proved freely tunable family realizing those values. In fact the unmodified T increments are at least1/2, while the required sum_i a_i is below1; they cannot simply serve as arbitrary many item increments without another attenuation/calibration construction.
3. **Original vertices remain selectable.** The common portal, guards, other cycle vertices and payload/fixture vertices are all legal sites. A chosen common portal kills cross-branch missed mass and can invalidate the square-gap threshold. Fixed guard promises or a marked candidate set would change the input model.
4. **Exact cardinality does not enforce item consistency.** A total k alone does not prove one local choice per item, compulsory guards, or that no alternative allocation/bypass meets the threshold.
5. **Padding affects BOTH state coordinates.** Adding private leaves to force sites can alter alpha, beta, cross-item terms and the threshold; adding nonconstant fixtures causes the extra linear term just derived. Binary weight replication by w vertices may also become pseudopolynomial. A generic appeal to “large weights/leaves” supplies none of the required exact original-model inequalities.

These are missing constructive proofs, not a discovered contradiction in the conditional algebra. No impossibility of closing them is established either.

### One-paragraph hardness-gap verdict

**The hardness gap is real in the present argument, and I find no obvious standard trick that closes it from the supplied ingredients.** There is a routine bookkeeping fix for a known fixture mass—incorporate its linear term into the required calibration—but that merely changes the unproved gadget specification. Compact dyadic mass, a negative-beta/positive-alpha two-state comparison, and an abstract square objective do not jointly provide exact H1, same-budget coherent switches or a lossless unrestricted-site normalization that excludes the root and other bypasses. Standard candidate restrictions would change the target; naive padding/weight simulation must be re-proved with its altered pair interactions and binary size. This is therefore a soundly bounded conditional SKETCH with useful actual local constructions, not an NP-hardness theorem, not an argument that hardness is impossible, and not evidence for a polynomial compressed frontier.

## 9. Explicit findings and NOT_RECONSTRUCTED boundaries

At the literal conditional scopes stated in Section2, there are **no FATAL, MAJOR or MINOR mathematical findings requiring source correction**. The dominance argument's apparent symmetry issue is resolved by restricting to the base/one-leaf metric before applying swaps, as reconstructed above. The conditional fixture qualification must not be omitted in any later promotion.

NOT_RECONSTRUCTED / not accepted:

- any actual simultaneous realization of H1, fixed-guard enforcement, per-item equal-budget normalization or unrestricted portal/other-site bypass exclusion;
- a complete polynomial-time optimizer, polynomial bound on relevant state/profile count, efficient unrestricted cycle-pattern processing or exponential COMPLETE lower-envelope lower bound;
- NP-hardness/NP-completeness, any approximation classification for cactus or a full book-problem resolution;
- the historical freeze/v4 bookkeeping, book-image coverage, public-query execution and external-paper correctness beyond the explicit objective/import descriptions in this packet. Those source-screening claims are not load-bearing for pieces(a)–(e), were not independently re-audited here, and do not establish openness/novelty;
- executable, formal/kernel, human/cross-vendor or novelty acceptance.

The exact graph target remains the self-contained arbitrary-k/all-ties unweighted cactus problem in A:11–19. No weaker unique-geodesic, odd-cycle, fixed-k, restricted-site or weighted problem was substituted. Source/parent/shared files remain unchanged. HOLD/v7/v8 and the frozen deadline remain binding; no scientific computation, replay, new GO or extra agent occurred.
