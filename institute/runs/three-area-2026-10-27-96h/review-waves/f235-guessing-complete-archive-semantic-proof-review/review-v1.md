# f235 — semantic review of the all-affine-syndrome-plane candidate

## Disposition

**Global theorem, exact certificate identities and global coverage: UNKNOWN / NOT ADOPTED.** The elementary fiber, component-decoder, visibility, full-state gate and conditional-lift implications below are justified under their stated guards. They do **not** establish any of the uninspected finite identities or coverage records. In particular, the proper-subgraph D2/D3 identities, every four-factor/visibility/mixed/residual certificate, and the union of all direction-plane classes remain unverified until a separately admitted exact replay. No bulk scientific replay was authorized or performed.

There is a concrete process sequencing deviation in the metadata inspection, disclosed below and to Main; it requires parent disposition. Separately, identifying the literal graph with the named publisher figure is unverified because that PDF body is not among this wave's permitted metadata. These are not claims that the candidate theorem is false. This review is same-harness work, not human, independent-model-family, formal/kernel, novelty or publication review.

The companion `reviewer-semantic-contract-v1.json` states the machine-readable row, action, coverage and dependency obligations. Statuses there distinguish proved semantic implications from unverified machine data.

## Input, sequence and limitations

1. The first research artifact was the wave manifest; its full SHA-256 matched `068131acf76e05320784d5a1ce9228858aeb112bba2e1448fc3b2a4935568f92`. Before displaying any written body, all 15 manifest-listed staged files matched their individual SHA-256, byte counts and LF counts: 64,830 bytes and 708 LF in total. I then displayed the four errata first, followed by all other staged bodies in declared order through their endings, using raw windows of at most 15 lines. Thus all 15 are candidate inputs actually read, not imported referee conclusions.
2. The complete archive was subsequently hashed read-only: SHA-256 `3bde5418e776a88b6a8f9c3e7a147a016b2b09272908eac226e1f3b33ced3040`, 67,393,983 bytes. The archive central directory reported 71 distinct names and 457,373,801 uncompressed bytes. I inspected only the two wave-whitelisted metadata members, not certificate, coverage, author/reviewer code or PDF bodies. Python `zipfile` was used only for read-only central-directory and bounded metadata inspection. Index sizes and counts in those metadata are claims, not scientific evidence.
3. **Late member-pin comparison, not a clean sequence.** Before displaying `data/graph-factor-actions-and-proper-color.json`, the whole-archive SHA had matched, the two allowed names had been whitelisted, and its own digest and size had been computed. I displayed its metadata before comparing that digest to the member entry in `packet-manifest.json`. The later comparison matched both 1,554 bytes and SHA-256 `449203f43ac9f3fce6c39b7df16228bf87af93c9e26119422a2e6bb92e031b90`. No comparison timestamp was captured, and none is backdated. No semantic conclusion was drawn from this metadata before that comparison or adopted from it afterwards: the findings below follow from the staged written definitions and independently checked small controls. The earlier whole-archive match does not erase the member-pin sequencing deviation.
4. No prior PASS/receipt counts, author or previous-reviewer code, f161/f162 or held material, unlisted sibling result, web/model/API or author contact was used as evidence. Neither the withdrawn two-syndrome inference, the exploratory invalid mixed-plane permutation, publisher copy-LP bound, nor a conditional functional-fiber Delta theorem is a premise here. Archive SHA and the source pins identify bytes; they do not prove mathematics.

Source references below use the manifest's numbered staged files: `05` is the prospective entry; `06` proper subgraph; `07` four-factor complete; `08` four-factor color; `09` visibility families; `10` visibility lattice; `11` mixed visibility; `12` single-functional decoder; `13` triangle-code tensorization; `14` noncover gate; `15` the candidate manuscript. The four preceding errata are `01`–`04`.

## Independently justified semantics, with exact guards

### 1. Literal graph, actual components and original-neighbor FDs

Work conditionally on the literal graph and ordered triangles in `05:25–149` and `15:16–44`. In particular, 3–4 is an edge and 9–10 is not. The ten listed triangles really are triangles of this graph and each vertex occurs in three; the small control checks the 26-edge undirected graph, all incidences and the listed action subgroups. This is an **internal** correspondence. Agreement with the external publisher figure remains blocked by the source-access restriction.

For finite variables, `H(X_v|X_N(v))=0` means that the full vertex tuple is a function of the **full original neighbor tuple on the support**. It does not, on its own, allow deletion of neighbor 4 from the decoder at vertex 3, or neighbor 3 at vertex 4; `03:3–9` correctly warns against that implication. In a positive-probability fiber of the full tuples of fixed factors, their component values can be supplied as constants to each original decoder. Therefore `H(Y_v|Y_N(v))=0` holds for the selected components. No independent-factor or uniformity assumption is needed (`14:16–23`, `15:61–71`).

A concrete actual-encoding counterexample confirms that the missing-edge distinction is substantive. Let independent fair bits be `a,b,c`. All occurrence bits are zero except

- factor 1 = `123`: `x_1^1=x_2^1=c`, `x_3^1=a`;
- factor 2 = `145`: `x_4^2=a`;
- factor 4 = `239`: `x_2^4=x_3^4=x_9^4=b`.

Then `sigma=(a,a,0,b,0,0,0,0,0,0)`, an actual rank-two syndrome plane. The original FDs hold: for example, vertex 3 obtains `a` from neighbor 4 and `b` from neighbor 2, while vertex 4 obtains `a` from neighbor 3. Yet `L_all(3)={1,2,8,9}` and the actual partial syndrome `sigma_3=0` reveal only `b,c`, so

`H(X_3 | X_1,X_2,X_8,X_9,sigma_3)=1` bit.

This does not contradict the legitimate full-syndrome component decoder below: the full syndrome reveals `a`. It does refute the bare claim that original-neighbor FDs plus an arbitrary partial auxiliary force the smaller local FD.

### 2. Affine coordinates, local inversion and visibility

Choose an ambient plane `sigma=s0+A*a+B*b`, where **the direction vectors** `a,b` are independent, not necessarily the random bits `A,B`. Put `S=(A,B)`. Its law can be nonuniform, correlated or supported on a point or line. `J` contains the coordinates nonconstant on the chosen ambient plane, even if some happen to be constant under the actual law. Each selected parity is `c_t+l_t(S)` with known offset and `l_t` one of `A,B,A+B`. The direction map has rank two, so all selected parities together determine `S`; consequently `H(S|Y_V)=0` on each fiber.

For `L_J(v)`, the other vertices in selected triangles incident to `v`, every selected component satisfies

`x_v^t = c_t + l_t(S) + x_u^t + x_w^t` over `F_2`.

Those other components are coordinate projections of `Y_L_J(v)`. Concatenating the recovered bits gives `H(Y_v|Y_L_J(v),S)=0`. This is a component identity, not a smaller-neighborhood consequence of the original graph FD. If the **nonempty** incident-color set is exactly `{c}`, the same inversion requires only `l_c`: `H(Y_v|Y_L_J(v),l_c)=0` (`12:10–30`, `15:72–81`). An empty selected tuple is constant. If there are two or three colors, a single arbitrary functional has no universal authorization.

The eight-state law above makes both guard failures concrete. Its selected set is `J={1,2,4}` with colors `A,A,B`. At vertex 3 the two incident colors are `A,B`, and `H(Y_3|Y_L_J(3),B)=1`. At vertex 4 the unique incident color is `A`, but substituting the wrong functional gives `H(Y_4|Y_L_J(4),B)=1`. This law still obeys every original-neighbor FD. Thus the checker must reconstruct the singleton and the specific functional, not just see a local-row name.

For visibility, the original graph FD recovers `Y_v` from `Y_N(v)`; its neighbors already contain the other two components of every incident triangle. Therefore the incident parities, and their incident functionals, are determined by `Y_N(v)`. The incident projection is injective on the entire two-dimensional ambient plane exactly when it has rank two, equivalently at least two distinct nonzero incident colors. This condition is **sufficient**, not necessary, for `H(S|Y_N(v))=0` in an actual law: other neighbor information or a restricted sub-support might provide additional visibility. One color cannot be promoted to full-state visibility without another valid premise. Restricting to a sub-support does not invalidate a rank-two ambient projection. A single triangle's parity determines its own functional, not generally all of `S`.

For the full-visibility import `10`, the selected local set is contained in the full triangle-local set, so conditioning on the latter cannot destroy the valid selected-component decoder. The complete full syndrome, with omitted coordinates fixed, is in bijective correspondence with `S` on the chosen plane. This explains the semantic applicability of such rows; it does **not** verify any full-visibility coefficient identity or plane binding.

### 3. Full-state entropy gate and sign

With `S` fixed, each selected triangle has fixed affine parity, and any two bits determine the third. For any conditional distribution of its three bits,

`3 H(Z_t | S,past) <= 2 sum_{v in t} H(x_v^t | S,past)`.

Sum in a factor order and replace all-past conditioning on the right by the corresponding vertex's own past. This yields `3H(Y_V|S)<=2 sum_v H(Y_v|S)`. Because `H(S|Y_V)=0`, expansion over **all ten** vertex variables gives exactly

`G_S = 3H(Y_V) + 17H(S) - 2 sum_v H(Y_v,S) <= 0`.

The coefficient is `2*10-3=17`; it is not a syndrome-size estimate, and `S` is not treated as a single binary random bit. For the eight-state law above the independent control computes `H(Y_V)=3`, `H(S)=2`, `sum H(Y_v,S)=22`, hence `G_S=-1`. Replacing 17 by 18 makes the proposed inequality `+1<=0`, false for that actual law. For a target written `Delta<=0` or `3Delta<=0`, a valid `G_S<=0` row needs a **nonnegative** multiplier; an elemental `ge` Shannon row needs a **nonpositive** multiplier; a proven zero equality can have either sign. For the positive proper-subgraph target the `ge` sign is reversed. All weights and cancellation must be exact rationals.

### 4. Auxiliary branches and exact row reconstruction

The functional coordinate is `5*m+b`, with `m` the ten-vertex subset mask and `b=0,1,2,3,4` meaning respectively no auxiliary, full `S=(A,B)`, `A`, `B`, `A+B` (`05:158–164`). Only coordinate 0, `H(empty)`, is omitted: there are 5,119 coordinates. These five branches describe **one common law**, not unrelated copies. The full-state 11-variable representation has 2,047 nonempty masks; the proper nine-variable representation has 511.

Let `L_c` be one nonzero functional and `K` a vertex set. Because `L_c=f_c(S)`, ordinary entropy gives

- `H(Y_K,S)-H(Y_K,L_c)=H(S|Y_K,L_c)>=0`;
- `I(Y_i;S|Y_K)-I(Y_i;L_c|Y_K)=I(Y_i;S|Y_K,L_c)>=0`.

For distinct nonzero `c,d`, `(L_c,L_d)` is a bijective recoding of `S`, so

`H(Y_K,L_c)+H(Y_K,L_d)-H(Y_K,S)-H(Y_K) = I(L_c;L_d|Y_K) >= 0`.

These statements require no independence or full-support assumption. A checker must expand **each actual row** and each action image in these coordinates, validate every FD/visibility/color guard, and compare the exact vector; a descriptive row name is not a proof. Any row outside the authorized elementary/FD/gate templates requires its own explicit valid derivation or must be rejected. In particular, no unproved functional-fiber Delta gate, syndrome entropy cap, DFZ row or withdrawn two-syndrome theorem may be silently introduced.

### 5. Proper-subgraph proof shape and full conditional lift

For deletion of vertex 1, the staged coloring classes are `{2,5,8}`, `{3,6,10}`, `{4,7,9}`. The tiny control checks that they are a proper coloring of the actual induced graph. Any two support words differing only in the third class would have an active vertex with no active neighbor, contradicting its FD. Thus every pair of color-class tuples determines the whole word. Summing the three pairwise subadditivity inequalities gives `3H(Y)<=2 sum_v H(Y_v)`.

For the two other representatives, this argument depends on the uninspected **exact** identities `13(2 sum H_i-3H_joint)` and `72(2 sum H_i-3H_joint)`, respectively, with valid elemental `ge` rows and zero induced-graph FD rows on all 511 coordinates (`06:31–45`). The eight listed literal graph actions were independently checked as an adjacency-preserving subgroup; their images give the candidate orbits `{1,8}`, `{2,5,9,10}`, `{3,4,6,7}`. Exhaustion of the entire graph automorphism group was not checked and is not needed if these explicit transports and the actual identities are verified. The D2/D3 mathematical validity remains **blocked**, not inferred from their hashes or historical receipts.

Conditioning a ten-vertex FD law on a positive-probability value of `X_k` yields the induced-graph FDs: the removed neighbor is supplied as a constant. Hence the asserted nine-variable result, **if** its proper-subgraph identities are verified, applies in every such fiber. For a noncover selected block, some `Y_k` is constant, so the same conditional result proves its nonpositive gap. Process all fixed-parity factor tuples before the selected block, use the conditional triangle inequalities and that selected-block result, then chain-rule both sides. Since each vertex's past is a function of the full past, replacing full-past conditioning on the right by vertex-past conditioning only increases it. This establishes the fiber-to-original implication conditional on the selected-block proof; correlations across factors are allowed (`13:10–38`, `14:10–23`, `15:136–141`).

## Actions and exact coverage obligations

A legal proper-subgraph transport needs a vertex bijection preserving every graph adjacency. A legal **encoded-law** transport additionally needs a permutation `p` with `g(T_t)=T_{p(t)}` for every ordered-list triangle. A graph automorphism that moves a selected factor outside the triangle list is not an encoded-law action. Even a valid factor action cannot be averaged at a fixed certificate unless every image's actual selected set, visible vertices and local-color premises hold on the target law; preserving the relevant `J` and required visibility set is one sufficient way to ensure this. The tiny control rejects both a graph-only automorphism and a valid factor action that fails to stabilize its selected `J`.

A change of coordinates of the two-bit state induces one of the six `GL(2,2)` permutations of `A,B,A+B`; affine offsets only complement individual functionals and do not affect their entropy. Recompute the induced permutation, the factor-coordinate permutation of all three nonzero direction vectors, and the actual client/source coloring. Check both transport directions and their inverse equations. The control verified the four displayed factor-preserving actions and six color permutations, not every archived action/binding or the complete automorphism group.

The later checker must independently generate the actual rank-two plane set as sorted triples `{u,v,u xor v}` for distinct nonzero ten-bit vectors, or by a canonical rank-two RREF enumeration. The count formula `(1023*1022)/6=174251` is justified: an independent ordered basis has 1,023 choices for its first vector, 1,022 for its second, and each plane has six ordered bases. **The actual set and its coverage were not generated here.** Three triangles cover at most nine vertices, so a covering selected set indeed needs at least four factors.

Use the candidate's disjoint precedence: noncover; covering four-factor; remaining full visibility; remaining mixed visibility; residual. For **each** plane recompute `J`, its cover, the full incident-projection set `W`, certificate premises and direction-correct transport. Reject duplicate or invalid plane keys; prove the category sets are pairwise disjoint and their actual union equals the independently generated universe. Claimed sizes `20993/247/145248/5858/1905` are not substitutes for that equality.

For each four-factor color witness, independently enumerate the selected-component difference words whose syndrome lies in that direction plane. Any difference of actual FD words must have an active neighbor at each active vertex. Verify that no nonzero necessary active mask lies inside a proposed single color class. Then two color classes determine the selected word and the three pairwise entropy inequalities give the bound. Verify the **actual** 206 color, 13 visibility and 28 residual-orbit sets and bindings, not only the sum 247. Likewise bind each residual zero-based class ID to the literal certificate coloring, each factor/`GL(2,2)` action and every plane-to-class map; exact residual orbit-set equality is indispensable.

## Complete dependency disposition

| Node and required inputs | Semantic conclusion | Unverified load-bearing body |
|---|---|---|
| Literal graph and triangles | Internal graph/triangle consistency; original full-neighbor FDs | Publisher-figure identification is outside this scope |
| Fixed-factor fibers; actual XOR components | Original selected FDs, guarded local/functional decoders, visibility and full-state determinism | Each archived row must actually match those guards |
| Full-state factor gate and lift | `G_S<=0` and chain-rule tensorization, conditional on a selected-block inequality | Exact use/sign in every identity; selected-block results themselves |
| Proper subgraph | Deletion-1 color proof, graph-FD conditioning and written transport logic | D2/D3 coefficient vectors, FD rows and all applicable transports |
| Noncover | Constant selected vertex plus the proper-subgraph result, then lift | The proper-subgraph certificate dependencies and actual noncover roster |
| Four-factor | Difference-mask color proof, guarded visibility/local rows, legal orbit transport | 206 exact color bindings, two visibility identities/13 bindings, seven identities/28 orbit bindings and set equality |
| Full visibility | `S` visible at rank-two incident projections; selected local decoder implies the full-local row | Three representative identities, all generator transports and actual per-plane applicability |
| Mixed visibility | Guarded original/local/visibility equalities and `G_S` suffice as row types | All 219 literal identities and each claimed mixed-plane guard/transport |
| Residual functional | Five-branch semantics, pair-determination/data processing, singleton-color local decoder | All 495 older plus 20 newer color-bound identities, 515 actual class bindings and 1,905 plane orbit maps |
| All affine planes | Point/line extension, conditional selected-block cases and chain-rule lift | Exact rank-two universe, category disjointness/union, all above identities and bindings |

The machine-readable contract additionally lists the leaves and their dependencies explicitly. The table does not rely on predecessor theorem names as axioms. A valid later replay must bind **every** coefficient row, action, target and coverage record to an independently proved semantic premise; a numerical count, coefficient hash, receipt, author PASS, or assertion of completeness cannot close any blocked node.

## Bounded controls: exercised evidence only

Before writing the control source, `/bin/date` gave `2026-10-29T14:15:59-0700 PDT`; before correcting its transcription, `/bin/date` gave `2026-10-29T14:16:52-0700 PDT`. Own corrected source `semantic-controls-v1.py` SHA-256 `e923820f51b9178367352ffffcd69a84e936d22759c943e1cc38f9a90e5773a7` was run as `python3 -B semantic-controls-v1.py` with a 120-second ceiling. The native clock immediately before the successful run was `2026-10-29T14:17:02-0700 PDT`, and after it was `2026-10-29T14:17:07-0700 PDT`; actual exit was 0. It exercised the 26-edge/ten-triangle literal graph, eight listed graph actions, four factor actions, the deletion-1 coloring, six state-form permutations, and the single eight-state actual law above. It did **not** read the archive or enumerate the scientific atlas.

Seven negatives were rejected for their intended reasons: improper deletion coloring (`not_proper_coloring`); duplicate color action (`not_color_bijection`); graph-only non-factor action (`not_factor_automorphism`); non-stabilized selected set (`selected_factors_not_preserved`); wrong singleton functional and one functional at a two-color vertex (both `local_not_determined`); and the coefficient-18 gate (`gate_inequality_false`).

Transparency on an initial failed control: the first source SHA was `825a32a8633338e30bf576ec8b897e9597eb7828676d4659520fb5d35d520afc`; it exited 1 with `not_a_group` because I transcribed the last two entries of one proposed graph permutation incorrectly. I corrected that local control transcription and reran the corrected, newly hashed source. The first failure was not an intended negative, not evidence of an archive error, and not a scientific PASS.

**Next permissible scientific step:** a separately authorized independent definition-first replay of every referenced certificate, per-row/action guard, and exact coverage set under this contract, plus separately authorized verification of the named graph's publisher figure. Until those steps and parent disposition of the sequencing deviation, the global theorem and coverage remain unverified.
