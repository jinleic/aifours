# f206 — independent same-harness scientific review

**Disposition: 0 F / 1 M / 0 m; 8 INCONCLUSIVE items (I1–I8 below).** The mathematical reductions, component decoders, full-state entropy gate, fiber lift, and substantial parts of the finite census are independently reconstructed below. The all-plane entropy theorem is **not independently verified**. M1 concerns the frozen review packet's inability to expose the claimed exact identities and coverage data, not a demonstrated counterexample or a finding that the inaccessible identities are false.

## Frozen inputs, sequence, and boundaries

The first research artifact accessed was `manifest-v1.json`; its SHA-256 was measured before its body was read and was `46d86e19d7379c07969d020952fb50b33aac5c7583c148bebe000f713a1146e9`, matching the assigned prefix. The two declared inputs were then both measured, **before either input body was read**, with these matching results:

| Input, in read order | SHA-256 | bytes | LF |
|---|---|---:|---:|
| E: `information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261029-all-affine-syndrome-plane-entropy-evidence-v1.json` | `3064c76b7ae540e990f9dec22158a6bf609ed115209e39b265cda697cd49a62d` | 14247 | 483 |
| M: `information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261029-all-affine-syndrome-plane-entropy-v1.md` | `9c6b11ca444122cf427a8e46f0a3cef0139f33b0615283322631c9c597c06cbd` | 13348 | 149 |

Both paths are under `/Users/jinleic/repos/aifours/`. After measuring both, I displayed E completely before M, in raw, contiguous windows no longer than 15 lines. Actual complete windows were E 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, 181–195, 196–210, 211–225, 226–240, 241–255, 256–270, 271–285, 286–300, 301–315, 316–330, 331–345, 346–360, 361–375, 376–390, 391–405, 406–420, 421–435, 436–450, 451–465, 466–480, 481–483; then M 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–149. An initial display of E 1–45 included a truncated tool-object rendering; those three windows were re-displayed as complete raw text before proceeding. Mathematical reconstruction and controls began only after the final lines of both inputs had been displayed.

E was read first as required. E 411–435 pins four erratum filenames and hashes; M 7–10 summarizes their effects. The actual erratum bodies are **not** declared inputs and were not opened. In particular, I have not used the withdrawn local-neighborhood theorem, the invalid exploratory mixed-plane permutation, the withdrawn primal receipt, or a publisher copy-LP bound. Hashes of linked bodies in E are author-supplied pins, not hashes measured by this review. The only measured source hashes are the manifest, E, and M above. No author checker, certificate, receipt, linked paper, disposition body, held material, sibling review, external search/model, or author communication was used.

## Per-claim verdicts

Counts below refer to the single packet-level M1, not a separate major for each affected row. `0/0/0` means no fatal, major, or minor mathematical defect found for the indicated independently reviewed portion; it is not an acceptance of an inaccessible import.

| Claim | Verdict | Basis and limitation |
|---|---|---|
| Literal ten-vertex graph, ten listed triangles, 26 edges, three occurrences per vertex | 0F/0M/0m for internal structure; **I1 INCONCLUSIVE** for published graph identification | Independently checked graph symmetry, factor cliques, 30 incidences, 3–4 present, 9–10 absent. The publisher PDF is not a declared input. |
| Rank-two parametrization, arbitrary probabilities and extension of points/lines | 0F/0M/0m | Reconstructed below without distributional independence. |
| Conditioning on fixed factor tuples preserves graph FDs and makes selected parities recover S | 0F/0M/0m | Written reconstruction below. |
| Actual full-state and singleton-color local XOR decoders | 0F/0M/0m | Component-by-component proof and original-FD-law negative controls below. |
| Full-state gate and tensorization from fixed fibers | 0F/0M/0m | Exact entropy algebra and conditioning proof below. |
| 174251 planes, 20993 noncover, 247 covering four-factor, 145248 full-visibility category | 0F/0M/0m for these **counts/predicates only** | Independent enumeration with displayed graph/factors and transported stated visibility sets. No imported entropy certificate is thereby verified. |
| Proper-subgraph entropy claim | 0F/0M/0m for 5299 noncover planes independently proved; **I2 INCONCLUSIVE** for the remaining 15694 not covered by this particular proof | The broader proper-subgraph certificate bodies are unreviewed. Other elementary arguments may cover some of the remaining planes. |
| All 247 covering four-factor cases, including 206+13+28 claimed proof split | **I3 INCONCLUSIVE** | Count 247 independently checked; the entropy proofs and their claimed internal partition have not been reconstructed. |
| Full-visibility entropy theorem on its counted 145248 planes | **I4 INCONCLUSIVE** | Its applicability predicate/count is checked, but the prior entropy identities are not. |
| 219 mixed identities and their exact 5858-plane coverage | 0F/1M/0m, **I5 INCONCLUSIVE** | Neither the 219 identity rows nor their per-plane coverage data occur in E or M; 5858+1905=7763 is only arithmetic. |
| Exact 1905-plane residual set, 515 coloring orbits, and 495 older identities | 0F/1M/0m, **I6 INCONCLUSIVE** | No residual set, canonical ID map, older identity coefficients, or authoritative set-equality witness is present in the declared inputs. The stated orbit counts add correctly. |
| The twenty new exact coefficient identities, IDs 65,72,150,157,225,247,335,336,353,354,355,359,363,493,494,495,496,497,498,499; abstract-profile violations | 0F/1M/0m, **I7 INCONCLUSIVE** | No one of the twenty coefficient identities, its class-to-coloring map, or the alleged abstract profiles was available for inspection. Their hashes and reported checker outcomes do not establish their truth. |
| The all-plane theorem and its entropy/count consequences | 0F/1M/0m, **I8 INCONCLUSIVE** unconditionally | The final inference is correct **conditional** on the explicitly listed unreviewed coverage and entropy propositions. It is not a proof from the displayed packet alone. |

### M1 — frozen proof-data gap

M 119–133 names twenty class IDs and says exact identities and a set-equality comparison exist; E 331–369 and 391–401 supplies filenames and hashes. The declared inputs do not contain the twenty raw identity coefficient vectors, definitions mapping their IDs to colorings, the 219 mixed profiles, the 515 residual profiles, or the exact sets being compared. The review contract forbids opening those linked bodies or relying on the author's PASS/receipts. Consequently none of the twenty identities or the actual 5858/1905 set partition can be checked here. This is a major **reviewability/verification** gap, not a mathematical disproof. A prospective new freeze would need to declare the relevant literal certificate and class/coverage data, with any permitted disposition premises and necessary errata; independent coefficient and set verification would then still be required.

## Independent mathematical reconstruction

### Representation and fiber facts

In the literal graph each triangle's three vertex pairs are edges. Each vertex occurs in exactly three factors, so the ten local variables are three-bit tuples and the word has 30 bits. Every factor has an affine parity equation. A syndrome space of dimension 0 or 1 extends to a dimension-2 affine plane in the ten-dimensional binary syndrome space. Choose independent **direction vectors** A,B and write `sigma=s0+a A+b B`, with `S=(a,b)`. This does not assume the random bits a,b are independent or even nonconstant. For a factor t, `(A_t,B_t)` is either zero or one of the three distinct nonzero linear forms on S. Its actual parity is the form plus the fixed offset `s0_t`.

Let J be the nonzero rows and F the complete tuples of all factors outside J. In a positive-probability fiber F=f, all omitted bits are constants. Consequently the original `H(X_v|X_N(v))=0` gives `H(Y_v|Y_N(v))=0` in that fiber: feed the fixed bits and neighbor selected bits to the original decoder, then project its output. The nonzero rows span the two-dimensional dual since A,B are independent. Every selected parity is recoverable from its three Y-components and its known offset. Therefore these rows recover S from `Y_V`, i.e. `H(S|Y_V)=0`, even when the actual distribution has a smaller support.

For an incident selected triangle, the other two vertices belong to N(v); the original FD in the fiber recovers Y_v from Y_N(v). Thus that triangle's parity form is also determined by Y_N(v). If two distinct nonzero incident forms occur, they are linearly independent over F2 and determine S. Each form is a deterministic function of S and of each selected triangle carrying it; any two distinct forms determine S. These are the functional and pair-determination facts needed for the claimed auxiliary rows. None uses a smaller-neighborhood FD assumption.

### Component inversion and the finer decoder

For each selected factor t through v, let u,w be the other vertices and let `x_{t,v}` denote its bit at v. With parity `p_t=s0_t+ell_t(S)` (all additions XOR), the literal equation is

`x_{t,v}=x_{t,u} + x_{t,w} + s0_t + ell_t(S)`.

All the other bits on the right lie in `Y_{L_J(v)}`. Solving this equation independently for every incident selected factor and concatenating gives `H(Y_v | Y_{L_J(v)},S)=0`. If the nonempty set of incident nonzero forms is precisely `{ell_c}`, each right-hand side needs only `ell_c`, giving the finer `H(Y_v | Y_{L_J(v)},ell_c)=0`. If v has no selected components, Y_v is constant and this singleton premise is not needed. The singleton condition is a universally sufficient guard; particular correlated laws may happen to admit further decoders, but the guard cannot universally be weakened to “contains c.”

The independent control supplies an actual original-neighbor FD counterexample to using the **wrong** form or applying the singleton rule at a mixed-color vertex. Put independent direction rows `A=e_239`, `B=e_145+e_569`; use two equiprobable words indexed by b, with only `x_{145,1}=b` and `x_{569,6}=b` nonzero, all other components zero. Here a=0 and the two words have syndromes `(a,b)=(0,0),(0,1)`. Only X_1 and X_6 vary, identically, and 1–6 is an edge, so every original graph FD holds. At vertex 1 the only selected incident color is b, `L_J(1)={4,5}` is constant, and Y_1=b: conditioning on the wrong form a=0 does not decode, whereas conditioning on b does. Replacing `A=e_239` by `A=e_123` makes the incident colors at 1 `{a,b}` and `L_J(1)={2,3,4,5}`; the same law shows that a alone still does not decode. These examples are within the stipulated affine-plane support class, not merely artificial entropy profiles.

### Full-state gate and lifting

If a triple Z has parity fixed conditional on W, any two components determine the third. Subadditivity yields, for each of its three pairs, `H(Z|W) <= H(Z_i|W)+H(Z_j|W)`; summing gives

`3 H(Z|W) <= 2 sum_i H(Z_i|W)`.

Apply this with W consisting of S and all previously processed selected factor tuples. On the right, discard from the conditioning all prior components except those at the same vertex; entropy can only increase. Summing the inequalities and applying the chain rule yields

`3 H(Y_V|S) <= 2 sum_v H(Y_v|S)`.

Because S is determined by Y_V and there are ten vertices,

`3H(Y_V)+17H(S)-2 sum_v H(Y_v,S) = 3H(Y_V|S)-2 sum_v H(Y_v|S) <= 0`.

This confirms the exact coefficient 17 and the full-state gate independently. It does not establish any unavailable coefficient identity that invokes the gate. A valid such identity would have to be checked in every entropy-coordinate coefficient, with nonnegative Shannon terms and gate multipliers and deterministic rows that really vanish; an identity's reported PASS is not a substitute.

Fixed factors have constant parity even before conditioning. Processing them in any order by the same triple inequality gives `3H(F) <= 2 sum_v H(F_v)`. Suppose each positive F=f fiber has `3H(Y_V|F=f) <= 2 sum_v H(Y_v|F=f)`. Averaging the fibers and using `H(Y_v|F) <= H(Y_v|F_v)` gives

`3H(X_V) = 3H(F)+3H(Y_V|F) <= 2 sum_v [H(F_v)+H(Y_v|F_v)] = 2 sum_v H(X_v)`.

This is valid for arbitrary probabilities and correlations. The missing issue is establishing the selected-fiber inequality in **every** required case, not this lift. If the main theorem were established, `H(X_V) <= (20/3) max_v H(X_v)` follows immediately; each local entropy is at most 3 bits, so a uniform support would have at most `2^20` words. A positive balance-gap law would require syndrome affine span at least 3 and hence at least four syndrome values. These are conditional consequences here, not independent proofs of the theorem or an unrestricted guessing-number bound.

### Finite counts reconstructed and the proper-graph subcase proved

A binary 2-plane has exactly three nonzero vectors. The control chooses its unique pair `a<b` with `a XOR b>b`; equivalently the number is `(1023*1022)/6=174251`. For selected-factor support size k there are `C(10,k)(3^k-3)/6` such planes, k=2,...,10: the three nonzero row colors must include at least two colors and GL(2,2) permutes them in all six ways. The exact control obtains the ordered disjoint categories noncover 20993, covering four-factor 247, full-visibility 145248, and other cover 7763. It independently enumerates all graph automorphisms (8) and the factor-preserving subgroup (4), and forms the eight distinct transports of the eight visibility representatives stated in M. A vertex's projection is injective exactly when at least two distinct nonzero incident colors occur. Thus the three stated category counts are substantiated, but `7763=5858+1905` does **not** identify either proposed subset or prove equality of sets. The covering four-factor count is also consistent with 19 covering four-factor supports, each admitting `(3^4-3)/6=13` direction planes.

One portion of the claimed noncover inequality can be proved without importing its certificate. If selected factors miss vertex 1, the other nine vertices have independent color classes `(2,5,8)`, `(3,6,10)`, `(4,7,9)`; if they miss vertex 8, use `(1,9,10)`, `(2,4,6)`, `(3,5,7)`. With each class C independent, the original graph FDs and the constant missing vertex give `H(Y_C|Y_{V\C})=0`. Hence `H(Y_V) <= sum_{v notin C} H(Y_v)`; adding the three inequalities gives the desired `3H(Y_V)<=2 sum_v H(Y_v)`. The control exhaustively finds proper three-colorings only for the single-vertex deletions 1 and 8; failure of this **particular proof method** is not failure of the entropy inequality.

There are `[7 choose 2]_2=127*126/6=2667` planes missing either given vertex. The three factors incident to 1 and the three incident to 8 are disjoint, so their intersection has `[4 choose 2]_2=15*14/6=35` planes. Thus this proof independently covers `2667+2667-35=5299` of the 20993 noncover planes. The remaining 15694 are not established by this argument and remain dependent on other proof or the explicitly unreviewed proper-subgraph proposition.

## Explicit unreviewed imports and remaining gap

The following are **conditional hypotheses**, not verified or adopted facts in this review; no linked body was read. They describe only what M expressly says is needed, at that scope:

1. **Proper-subgraph FD inequality.** For the noncover selected laws not independently settled above, the nine-active graph-FD entropy inequality and its graph transports. E's written pin is `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md`, SHA `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49`; the nine-active certificate and other hashes are listed in E 161–186. Only the 1/8 three-color subcase was independently reconstructed.
2. **Four-factor theorem.** Every covering plane with four selected factors has nonpositive selected-law gap; M claims a 206+13+28 division. E pins `frontier-20261028-fourfactor-plane-complete-theorem-v1.md` at `7148eb8fa7ef068743d927454c779290b0f3b4238940c7f4226b50bcb707cde5`, the color theorem at `09cb78a5bcd1d811f45d087dad567a49ce4f9f9ca898a0fcde3ef96efa0bb4ca`, and the visibility-family theorem at `ad7ee5d82f7a2ca20a21bc35f950bf1038fe660258dcbe41619bb67834cc410c`; other claimed certificates are in E 188–272. The invalid exploratory permutation is not an import.
3. **Full visibility.** The nonpositive-gap implications for the stated visible sets, subject to the actual FDs and full-state gate, plus their allowed factor-preserving transports. The stated representative predicate and count were independently checked, not the implications. E pins `frontier-20261028-visibility-lattice-theorem-v1.md` at `4180f4e072d3e3e7108c66d90aeadebd169fee6b46dcf64e72b37ab10a357b50`; associated pins are E 273–305.
4. **Mixed visibility.** The validity of all applicable identities and the exact mapping of 219 part-3 identities to their claimed 5858 direction planes, under original graph FDs, the actual full-state component decoder, `H(S|Y_V)=0`, and the gate. E pins `frontier-20261028-mixed-visibility-theorem-v1.md` at `5c6f885b3c9ca20b6216304fe6449e8011e9c7de27eaf086becd887e3e0bdc74` and `frontier-20261028-mixed-visibility-certs-part3.json` at `1b6194041f3a98b3b79313901cd2c2d3494790a8dc830fafda109a92970066fb`. Neither identity validity nor coverage has been checked here.
5. **Residual finite cover and prior identities.** That the exact planes left after the preceding categories are precisely 1905 and are covered by the stated 515 canonical coloring classes, transported legitimately; and that the prior `197+295+3=495` exact functional identities have the claimed valid coefficients and predicates. E 329–390 pins the older bundles and checkers, including part 2 `89132067417217f5ae4240f4fbce20da7d4befbdbf69ef25c03118e45e4dc0fb`, part 3 `0f7cbace8039d12959791781acdede47ec4430c7eebacd927667d63ec295241d`, and recovered bundle `65e6308cc3e32fa5e62fb022a3ff57796d9643c3b434db5e3a2b2e1c3cbb7378`. The orbit-size arithmetic `5*1+70*2+440*4=1905` and `5+70+440=515` is correct but proves neither the orbit decomposition nor identity applicability.
6. **New twenty identities.** Conditional on the twenty named identities being actual exact entropy-coordinate identities, on their class IDs mapping to the intended colorings, and on every decoder row having the independently proved guard, their nonpositive Shannon terms, nonnegative full-state gate multiples and vanishing FD rows would imply the required residual gaps. The claimed bundle pin is `c129b79abcf916afb8a91d4145e6bb9316d0a3968d919f92beb516bdadf5450d`; none of its identities was available or verified. The allegation that twenty abstract profiles violate the finer decoder is likewise unverified.

E also pins two representation writings and a new coverage checker/receipt. Their linked bodies and claimed results are not mathematical premises used in this review: the representation, key decoders and the above partial census were reconstructed independently. No pinned disposition body was among the two declared inputs; no prior result has been silently elevated to an adopted premise. The remaining exact step is to establish the listed unreviewed entropy identities and their literal, exhaustive applicability to the 7763 unclassified covering planes, together with the remaining imported noncover/four-factor/full-visibility implications. Only then does the fiber lift prove the universal statement.

## Reviewer-owned controls and receipts

All controls are independent of author code, use only E/M's literal graph, factors and stated visibility representatives, and were run with a 120-second tool deadline. Native clocks below are literal `/bin/date` observations; they are not asserted creation times.

* `reviewer-affine-control-v1.py`, first version SHA-256 `c6e0f71f901d50093568fed7d67d3d224c4ad4dfee725b111eaf22a91745f86d`: start `2026-10-29T13:15:51-0700 PDT`, end `2026-10-29T13:15:52-0700 PDT`, exit 1. It printed graph=26 edges, graph automorphisms=8 and factor-preserving=4, then the system Python rejected `int.bit_count`; no census or negative-control result from that run is claimed. The reviewer changed only this compatibility expression to `sum(bool(x) for x in colors)`.
* Corrected `reviewer-affine-control-v1.py`, SHA-256 `43530040ff251122bed7ade23f4bea46e8d7f72cf537304f5a7413eec7108ac3`: start `2026-10-29T13:16:05-0700 PDT`, end `2026-10-29T13:16:07-0700 PDT`, exit 0. It reported 174251 planes; noncover 20993, covering four-factor 247, full-visibility 145248, other cover 7763. Factor-support-size counts for k=2,...,10 were 45,480,2730,10080,25410,43680,49185,32800,9841. It verified the two original-FD-law wrong-functional/mixed-color negatives described above, rejected a rank-one fake plane, detected an equal-cardinality unequal toy set, and rejected a deliberately non-clique factor. The toy set check illustrates why equal counts are insufficient; it is **not** a replay of the author's residual set equality.
* `reviewer-proper-fd-color-v1.py`, SHA-256 `e2327b27d7a13b47995bff5efac13724cf13211fc6b208d1f275e6bef765e9ba`: start `2026-10-29T13:17:00-0700 PDT`, end `2026-10-29T13:17:00-0700 PDT`, exit 0. It exhaustively checked three-color assignments for each single-vertex deletion and found certificates only for deletions 1 and 8, listed above. As an intended-reason negative it added edge 2–4, creating a K4 that survives deletion of 10, and rejected three-colorability.

## Deviations, limits, and review identity

No contract deviation is claimed. The initial truncated display was explicitly re-read in full; the first own-control run failed for interpreter compatibility and is reported rather than counted as a pass. All other uninspected items above are limitations of the frozen packet and scope, not inferred failures. The native clock observed immediately before writing this review was `/bin/date` `2026-10-29T13:18:36-0700 PDT`.

This is a **same-harness** scientific review. It is not a human review, an independent-model-family review, a formal/kernel proof, a literature/novelty verification, a scientific adoption, or an unrestricted guessing-number result.
