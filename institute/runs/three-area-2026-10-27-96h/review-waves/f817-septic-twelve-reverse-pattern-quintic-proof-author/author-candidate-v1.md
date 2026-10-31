# Six-node physical reverse patterns and strengthened quintic parity budget

**Status: nonblind same-harness GENERAL AUTHOR, written candidate; no automatic parent disposition.** For an actual zero relation with exactly six distinct positive finite nodes and no endpoint atoms, I reconstruct the 12 **necessary** physical-band/gap rows, the physical sign of the common ratio, and the corner-quintic boundary and multiplicity formulas. I also give a strictly stronger necessary budget that charges roots forced in the two reverse gaps by actual mixed-edge signs, and two explicit uniform support-pattern exclusions. No row is claimed realizable; no eligible zero dual, global no-go, universal SPR/ROOT result, or source/priority/novelty conclusion is asserted. All results are conditional on the exact actual-box hypotheses below. This is not a parent, human, independent-family, or kernel acceptance.

## 1. Exact object, imports, and scope

Fix ONE nonempty compact independent real coefficient box of monic septics all of whose actual members are strictly Hurwitz. At t>0, for one actual member a write

\[
 E_a(t)=a_0-a_2t+a_4t^2-a_6t^3,\qquad
 O_a(t)=a_1-a_3t+a_5t^2-t^3,
\]
\[
 r_a(t)=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a).
\]

At fixed t, independence makes the actual pair set exactly the rectangle `[E_-(t),E_+(t)] × [O_-(t),O_+(t)]`, with vertices supplied by four **fixed actual parity corners** `C_{στ}`, σ,τ∈{−,+}. This pointwise fact is not a four-polynomial convex-hull representation of the coefficient box. The actual rectangle excludes (0,0). Consider an actual nontrivial zero relation grouped into six distinct `0<u_1<...<u_6`, with NO endpoint atoms. Let W_i>0 and `(E_i,O_i)` be the SAME actual averaged pair at u_i. Define `X_i=W_i E_i`, `Y_i=W_i u_i O_i`. Then

\[
 \sum_{i=1}^6 u_i^qX_i=\sum_{i=1}^6 u_i^qY_i=0\quad(0\le q\le3). \tag{1}
\]

I use classical strict Hermite–Biehler interlacing and the physical rectangle exclusion to obtain the disjoint closed uncertainty bands

\[
 B_1=I^E_1<B_2=I^O_1<B_3=I^E_2<B_4=I^O_2<B_5=I^E_3<B_6=I^O_3. \tag{2}
\]

A relation forces both parities to vary: otherwise pairing with the fixed parity and then the other center parity gives a sum of squares and a strictly positive contradiction. Thus the widths are strictly positive at positive t. Inside each actual band the varying interval strictly straddles zero; the other parity is strictly signed. In the even bands `I^E_1,I^E_2,I^E_3`, O signs are `+,-,+`; in odd bands `I^O_1,I^O_2,I^O_3`, E signs are `-,+,-`. Outside those bands ordinary parity signs pass through `+,-,+,-`. The parent packet's adopted band/reverse-pair statements S5–S7 and the fuller S4 reconstruction give this same physical interface; I do not treat outgoing linked sources as newly read or independently authenticated.

The named **at-most-five-frequency strict-negative no-go**, the eligible enlargement that imports it, and the connected-corner eight-total-atom reduction are NOT needed for the conditional six-node/no-endpoint statements below. They are retained only if one uses the wider S7 conclusion that every zero relation has at least six frequencies or that a chosen relation can be made eight-total-atom sparse. The compact zero-hull/strict-SPR alternative and the ROOT interface are not proved or consumed here. No source stability assertion is substituted for all-member eligibility.

## 2. Exact six-node structure and common ratio

Neither X nor Y can vanish identically: if all E_i=0, actual rectangle exclusion forces O_i to have its center's nonzero sign, contradicting the odd-center pairing, and conversely. On deletion of zeros only for counting signs, each sequence in (1) has at least four sign changes. Otherwise a polynomial of degree at most three, with one simple zero in each sign-change gap and suitably oriented, gives a strictly one-signed pairing with that sequence, contradicting (1). Without a strict reverse pair within a physical band, a parity's signs form a subsequence of `+,-,+,-`, with at most three changes. Hence both parities have strict reverse pairs in their own disjoint bands. Their two nodes are strictly inside their bands: at a band's two endpoints the corresponding actual interval has the ordinary one-sided signs.

In an odd band, the even sign is strict and constant across all its sampled nodes. The two nodes of the odd reverse pair therefore impose at least one repeated adjacent nonzero X sign, including any intervening nodes. Four changes and this repeat in a word of length at most six force no X zeros, exactly four changes, exactly one repeat, and the pair to be consecutive; no third node lies in that band. A second odd band cannot contain two sampled nodes, as that would force another X repeat. Interchanging E and O yields the symmetric conclusions. Thus the two reverse pairs use disjoint consecutive gaps `p<q` with `q≥p+2`, every other gap flips both signs, and every other physical band contains at most one sampled node.

Put `H(t)=∏_{i=1}^6(t-u_i)`. The degree-one-over-H′ Vandermonde nullspace for (1) gives nonzero c_E,c_O and real α,β with

\[
 X_i=\frac{c_E(u_i-\alpha)}{H'(u_i)},\qquad
 Y_i=\frac{c_O(u_i-\beta)}{H'(u_i)}. \tag{3}
\]

The affine coefficients cannot be constant, since that would give five rather than four changes. `H′(u_i)` alternates sign, so the unique X repeat places α strictly in the odd reverse gap and the unique Y repeat places β strictly in the even reverse gap. Both are strictly inside the respective actual bands, are distinct and positive, and are not sampled nodes. With `k=c_O/c_E`, the SAME pair and SAME positive W_i give

\[
 u_i O_i(u_i-\alpha)=k E_i(u_i-\beta),\qquad
 \operatorname{sgn}k=\operatorname{sgn}(\beta-\alpha). \tag{4}
\]

For the sign, use the later node of the even reverse pair: its E and O have equal nonzero signs in all three even bands, `u_i−β>0`, and the odd band containing α is entirely to one side of β's band. These statements use physical bands, not freely chosen marker positions.

## 3. All 12 necessary physical gap/band rows

Assign each strict quadrant a level as follows: outside the bands, the number of completed bands; inside B_j, `j−1` for its varying parity's pre-crossing sign and j for its post-crossing sign. The strict quadrant sequence at levels 0,…,6 is

\[
 (++),(-+),(--),(+-),(++),(-+),(--). \tag{5}
\]

At a band endpoint the permitted strict sign has the corresponding adjacent level, so this convention does not exclude sampled endpoints of *other* bands. Levels are nondecreasing between samples in distinct bands. A gap flipping both signs joins different bands and has a positive level increment congruent to 2 mod 4, hence at least 2. Each reverse gap has level increment exactly −1. There are three double flips and two reverse gaps. If any double flip were at least 6, the total increment would be at least `6+2+2−1−1=8`, inconsistent with levels in [0,6]. Therefore all three increments are exactly +2, `ℓ_6=ℓ_1+4`, and `ℓ_1∈{0,1,2}`.

Let the first and second reverse gaps be p and q, with physical bands r<s, and put `a=p−1`, `b=q−p−1≥1`, `c=5−q`. The first node of the first reverse pair has level r, the first of the second level s. Hence

\[
 s=r+2b-1,\quad r\ge 2a,\quad s-1+2c\le6,\quad
 \ell_1=r-2a. \tag{6}
\]

The two bands have opposite parity: odd band numbers are even-parity bands and even numbers odd-parity bands. The exhaustive solutions of these **necessary integer constraints** are the following 12 rows. To make every row's root budget explicit, `n_h` is the number of all six sample nodes between consecutive ordered boundaries `(0,d_1,d_2,∞)`, `d_1=min(α,β)`, `d_2=max(α,β)`; the four-sign string is the sign of EACH physical corner quintic at these boundaries, and ε is the three-bit sign-change vector.

| (p,q) | (r,s) | ℓ₁ | sign k | (n₁,n₂,n₃) | boundary signs | ε |
|---|---|---:|:---:|---|:---:|:---:|
| (1,3) | (1,2) | 1 | − | (1,2,3) | ++++ | 000 |
| (1,3) | (2,3) | 2 | + | (1,2,3) | −+++ | 100 |
| (1,4) | (1,4) | 1 | − | (1,3,2) | ++−+ | 011 |
| (1,4) | (2,5) | 2 | + | (1,3,2) | −+−+ | 111 |
| (1,5) | (1,6) | 1 | − | (1,4,1) | ++++ | 000 |
| (2,4) | (2,3) | 0 | + | (2,2,2) | −+++ | 100 |
| (2,4) | (3,4) | 1 | − | (2,2,2) | +−−+ | 101 |
| (2,4) | (4,5) | 2 | + | (2,2,2) | −−−+ | 001 |
| (2,5) | (2,5) | 0 | + | (2,3,1) | −+−+ | 111 |
| (2,5) | (3,6) | 1 | − | (2,3,1) | +−++ | 110 |
| (3,5) | (4,5) | 0 | + | (3,2,1) | −−−+ | 001 |
| (3,5) | (5,6) | 1 | − | (3,2,1) | ++++ | 000 |

Here `n=(p,q−p,6−q)` because the two markers lie strictly in gaps p and q. The exact six levels in any row are recovered by starting at ℓ₁ and adding −1 in gaps p,q and +2 in the other gaps; (5) then gives all six strict quadrants. For verification of exhaustiveness, the six possible gap pairs give respectively `r∈{1,2}`, `{1,2}`, `{1}`, `{2,3,4}`, `{2,3}`, `{4,5}` from (6); s is then fixed. Conversely, these entries solve only the displayed integer restrictions. Neither this enumeration nor the abstract level word asserts that any row is realized by actual coefficients, markers, mixed edges, or weights.

## 4. Actual corner quintics, common weights, and the original parity budget

For each fixed actual corner C define

\[
 P_C(t)=k(t-\beta)E_C(t)-t(t-\alpha)O_C(t). \tag{7}
\]

This is monic of degree five: the odd polynomial has leading term `−t³` and the E contribution has degree at most four. A singleton group on C must satisfy `P_C(u_i)=0`. A genuine adjacent-edge group between physical corners C,D uses ONE coefficient θ for both parities and satisfies `θP_C(u_i)+(1−θ)P_D(u_i)=0`, `0<θ<1`; the two values either have strictly opposite signs or both vanish. One zero and one nonzero value is not a strict mixture.

Compression to adjacent edges preserves the same box and all eight aggregate coordinates: move the nonzero grouped rectangle vector along its ray to its farthest boundary point, decompose that point into adjacent physical vertices, and rescale its group weight. The total W_i need not stay fixed, but both weighted parity values do. A formerly singleton group is left alone, and a mixed group uses at most two corners after compression. Thus a chosen relation with at most eight finite atoms and no endpoints has at most two genuinely mixed groups and at least four singleton groups. This is a sparse-representation consequence, not a restriction on every presentation of an arbitrary relation.

The quintic and edge equations alone do not certify positive weights. In (3), the same nonzero c_E must give

\[
 W_i=\frac{c_E(u_i-\alpha)}{E_i H'(u_i)}>0\quad(1\le i\le6),\qquad c_O=kc_E, \tag{8}
\]

using the SAME selected actual corner or SAME convex edge mixture in E and O. All denominators are nonzero by Section 2. Conversely, with an eligible box, distinct ordered nodes, actual corner/edge selections, common k,c_E, the marker placement and equations (7)–(8), the weights and interpolation identity (3) produce all eight moment equations. Add the actual atom budget to obtain the stated sparse six-node/no-endpoint iff formulation. No independently chosen parity weights, negative scalars, fictitious box, or cross-product-only certificate is admitted.

If α is in odd band `I^O_j` and β in even band `I^E_l`, then for EVERY C,

\[
\begin{aligned}
 \operatorname{sgn}P_C(0)&=-\operatorname{sgn}k,\\
 \operatorname{sgn}P_C(\alpha)&=(-1)^{j+1},\\
 \operatorname{sgn}P_C(\beta)&=(-1)^l\operatorname{sgn}k,\\
 \operatorname{sgn}P_C(+\infty)&=+.
\end{aligned} \tag{9}
\]

Indeed `P_C(0)=−kβE_C(0)` with `E_C(0)>0`; `k(α−β)<0`; at β the remaining term is `−β(β−α)O_C(β)`; and the fixed complementary signs are as in Section 1. Thus 0,α,β are nonroots. Formula (9) yields the sign and ε columns of every table row.

For a corner C, let `N_h` be the number of distinct assigned singleton nodes on C in the h-th interval between `0,d_1,d_2,∞`. If `δ_h∈{0,1}` has `δ_h≡ε_h−N_h (mod 2)`, then

\[
 \sum_{h=1}^3(N_h+\delta_h)\le5. \tag{10}
\]

The multiplicity of real roots in an interval has the parity determined by its nonzero endpoint signs and is at least N_h; the sums over the disjoint positive intervals cannot exceed five. Thus (10) counts a sampled root once initially but correctly charges any even multiplicity or additional unsampled roots required by parity. In particular the total positive-root multiplicity of each P_C is even and at most four if k<0, or odd and at most five if k>0. Both-vanishing mixed corners may be counted as roots, but a mixed node is never automatically a singleton.

## 5. Strengthening: forced roots in the actual reverse gaps

For each physical corner C, instead let `n_{C,h}` count **all** sample nodes in interval h where the actual `P_C(u_i)=0`: this includes assigned singleton roots, and also both edge corners when an actual mixed node has two zero quintic values. Let `g_{C,h}` count the following distinct forced gaps contained in interval h. For each of the four nodes belonging to the two reverse pairs, use its band's marker m (β for an even band, α for an odd band). If `P_C(u_i)` is nonzero and has the opposite sign to `P_C(m)`, count the open interval with endpoints u_i and m once.

Each counted interval contains a root by continuity. These open intervals contain no sample nodes because m lies between consecutive pair nodes; the two half-gaps for one marker are disjoint, and the two physical reverse bands are disjoint. Their roots are therefore distinct from each other and from all sampled roots. Consequently the following refined necessary condition holds for EACH C and EACH of the 12 table rows:

\[
 \sum_{h=1}^3\left(m_{C,h}+((\epsilon_h-m_{C,h})\bmod 2)\right)\le5,
 \qquad m_{C,h}=n_{C,h}+g_{C,h}, \tag{11}
\]

where the mod-2 term means its representative in `{0,1}`. It is valid to use any certified subset of the roots and forced gaps in place of all of them, because the displayed lower bound is nondecreasing in each m. This is a necessary constraint on the **actual four corner polynomials**, not an assertion of independent realizability of their signs. It strengthens (10) whenever signs at a reverse node force a new root in a half-gap that the original singleton-only parity accounting did not charge.

The new gap flags have an explicitly physical edge interpretation. For a particular band B_j, let its varying parity's pre/post signs be `(+ ,−)` for j=1,2,5,6 and `(−,+)` for j=3,4. At its *earlier* reverse node a corner with the pre sign is the wrong orientation; at its *later* reverse node a corner with the post sign is the wrong orientation. At either node EVERY such wrong-orientation physical corner has the strict sign of `P_C(m)`, independent of its other parity orientation:

* In an even band, `sgn(t−α)=sgn k` throughout that band. Before β the wrong E sign equals the fixed O sign; after β the wrong E sign is its opposite. In either case both terms of (7) have sign `−sgn(k)sgn(O)=sgn P_C(β)`.
* In an odd band, `k(t−β)<0` throughout that band. Before α the wrong O sign is opposite the fixed E sign; after α it equals that E sign. In either case both terms have sign `−sgn(E)=sgn P_C(α)`.

The strictness uses the interior of the genuine actual band. Thus a singleton at a reverse node must have the correct physical orientation. If a strict edge mixture there varies the **band's parity**, its wrong-orientation endpoint has the marker's nonzero sign; the same-mixture equation forces the other endpoint to have the opposite nonzero sign and hence forces a root of that other corner quintic in the corresponding half-gap. If instead the edge varies the complementary parity, its endpoint values either strictly straddle zero, forcing at least one such gap root for one endpoint, or both vanish, making the mixed node an actual sampled root of both endpoint quintics. These conclusions retain the actual shared θ and positive weights; they do not replace a mixed group by fictitious singletons.

### Two uniform support-pattern exclusions beyond singleton-only (10)

Consider the table row `(p,q;r,s)=(2,4;3,4)`: the even reverse band is E2 and the later odd reverse band is O2. Thus `β∈(u_2,u_3)`, `α∈(u_4,u_5)`, k<0, and every corner has boundary signs `(+,-,-,+)`. The following two actual configurations are impossible on **every** eligible K under the six-node/no-endpoint assumptions:

1. `u_1,u_3,u_6` are singleton groups on `C_{--}` and `u_5` is a strict edge mixture of `C_{--}` with `C_{-+}`.
2. `u_1,u_4,u_6` are singleton groups on `C_{++}` and `u_2` is a strict edge mixture of `C_{++}` with `C_{-+}`.

For (1), in O2 the common E value of these edge corners is positive and at u_5>α the `O_+` corner `C_{-+}` is wrong-oriented; both terms in its quintic are strictly negative. The actual mixture equation and `0<θ<1` force `P_{C_{--}}(u_5)>0`, whereas `P_{C_{--}}(α)<0`; there is a root in `(α,u_5)`. The singleton roots `u_1,u_3,u_6` lie respectively in `(0,β)`, `(β,α)`, `(α,∞)`. Endpoint signs force at least 1, 2, and 3 root multiplicities in those intervals: the middle interval has equal negative signs, while the last has opposite signs and already contains two distinct roots. This totals at least 6, impossible for a quintic.

For (2), at u_2<β in E2, the `E_-` endpoint `C_{-+}` is wrong-oriented and has strictly negative quintic value; the strict mixture forces `P_{C_{++}}(u_2)>0`, while `P_{C_{++}}(β)<0`. Hence there is a root in `(u_2,β)`. The three singleton roots occupy the three marker intervals, and the first interval now has two distinct roots with opposite endpoint signs, requiring at least three multiplicities; the middle needs at least two and the last at least one. Again the total is at least 6. Neither argument assumes that the remaining two groups are singletons or discards a mixed edge or common positive W.

For either exclusion, the original singleton-only (10) on the indicated corner sees `N=(1,1,1)` and ε=101, giving only `1+2+1=4≤5`. The new sign-forced gap root increases the applicable parity lower bound to six. These are conditional support exclusions, **not** constructions of marker rows or a conclusion that the other assignments or the row are feasible or infeasible.

## 6. Remaining frontier and precise limits

For each of all 12 rows, the full residual is: an eligible independent actual K; six ordered nodes in the indicated physical bands with the exact quadrant levels and both strict reverse pairs; markers α,β in their actual consecutive gaps; one common nonzero k and c_E satisfying (4), the physical corner/adjacent-edge equations (7), and all six strict positive-weight inequalities (8). For a chosen at-most-eight-atom representation, retain at most two mixed groups and at least four singletons. Apply (9)–(11) to every actual corner, including both-zero mixed nodes and forced half-gap roots. Apart from the two just-proved support subcases, no complete characterization or elimination of these coupled systems is asserted. If such a system is solved with all the physical hypotheses and weights, the reverse interpolation constructs the zero relation; a consistent sign word or root allocation alone does not.

Six-node relations with one or both endpoint atoms, seven-node and eight-node sparse cases, the general ≤5-frequency import, the eight-atom compactification import, universal SPR/ROOT and existence or nonexistence of an eligible zero dual remain outside this proof. No same-box weak-to-strict inference, corner-only stability criterion, arbitrary marker construction, or global obstruction is made. The refined per-corner budget and these two exclusions are written author results, not independently checked acceptance. No finite source was assigned or prepared, and no scientific child execution, numerical calculation, solver/CAS, test, compiler, build, lint, formatter, external-model CLI, network, old code, or outgoing scientific source was used.

## 7. Actual input and administrative coverage

Let `R=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`. Before any packet body, I read through endings this wave's complete `manifest-v1.json`, `freeze-receipt-v1.json`, `final-pre-dispatch-binding-v1.json`, `parent-live-metadata-supply-v1.json`, actual `dispatch-receipt-v1.json`, and every one of the 22 manifest-listed controls, as status/permission only. I sent Main a direct PREBODY ACK naming those controls, both ordered part LF counts, and expressly stating no body, math, or source comparison. Then I read part 01 consecutively RAW LF 1–657, and part 02 consecutively RAW LF 1–277, each window at most 20 LF, through both endings and before research. All long lines in those windows were displayed in full; there was no packet sequence, read, or presentation fault to disclose. The direct ACK is not a private-cognition or source-identity certificate.

The complete rendered science inputs, with **parent-supplied** whole-source pins, are:

| ID | R-relative complete source | original LF | parent-supplied SHA-256 |
|---|---|---:|---|
| S1 | `review-waves/f785-septic-six-node-quadrant-scrutiny-author/author-candidate-v1.md` | 250 | `458749db8e544f6373ddeb14f05428f385c5b77b059e3484ab20092ce4e5b293` |
| S2 | `review-waves/f784-septic-coupled-corner-barycentric-author/author-candidate-v1.md` | 228 | `87dc831218af8309b041b50b39cfe686f51f20c5b4743a085ac6d59b200273e5` |
| S3 | `review-waves/f760-septic-six-eight-frequency-coupled-frontier-author/author-coupled-frontier-v1.md` | 165 | `b5a248e86c2cda695851752fd8f364c5644d028c1b9daa343729ef91a67d505a` |
| S4 | `review-waves/f759-septic-strict-interior-quadrant-refinement-proof-author/independent-reconstruction-v1.txt` | 157 | `2d253d660505dcdd30d29f94c95eb98da33012477f6d042f48ea792213928ca7` |
| S5 | `dispositions/info-2-actual-septic-sparse-coupled-barycentric-and-six-node-frontier-parent-v1.md` | 33 | `32db73ad861d2fcafb8fda19efec027f3b957ed5878dc0ae78b8244bc5789549` |
| S6 | `dispositions/info-2-actual-septic-strict-band-quadrants-and-low-frequency-subcases-parent-v1.md` | 30 | `90ce201156b0ee89e5f09e2e6cf3c4fa9d7eb2c6178a02795c84d84dbd7fa9af` |
| S7 | `dispositions/info-2-actual-septic-eight-atom-zero-dual-six-frequency-and-parity-backtracking-parent-v1.md` | 39 | `866dd92b58bb2422281abe815bc1e6cae8e5f8f94c96f2d7eaed00bad372a183` |

The wave receipt reports complete-source rendering/roundtrip and persisted packet equality; I did not independently reopen, rerender, hash, or authenticate the original source files. The parent-provided part SHA-256 values are `5566efb1827178ee14792bdad831b1dce33a2bfdb1d2b409c1acca982122aa0e` and `3fe0dfc587b9b840f617c7ea965e94a4a4c907724d6bc5aac38cc8338940564f`. Hashes are administrative provenance, not scientific validation.

The 22 controls, paths R-relative, were exactly: `prospective-author-method-scope-restoration-20261030-v1.json`; `contract-addendum-2-frontier-first-owner-direction-v1.json`; `parent-L1-selected-diagnostic-release-quarantine-v1.json`; `parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json`; `parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json`; `parent-ame-held-compression-claim-consumer-quarantine-v1.json`; `parent-held-ph-registration-report-consumer-quarantine-v1.json`; the `parent-selected-diagnostic-process-major-quarantine-v1.json` files in `review-waves/` directories `f439-depolarizing-ancillary-all-dimensional-repair-written-review`, `f444-spr-full-seven-coefficient-enlargement-and-all-ray-review`, `f448-kac-actual-second-arm-exterior-module-and-character-review`, `f508-coherent-vacuum-w4-h2-channel-and-strictness-written-review`, `f513-boolean-five-span-physical-four-fibre-xor-obstruction-review`, `f586-semigroup-finite-pure-source-free-band-regularity-written-review`, `f602-olson-deficit-six-protected-triples-independent-actual-word-check`, `f653-sun8-psl2-small-exception-actual-cosets-written-review`, `f654-sun8-primepower-source-and-actual-normalcut-consumer-review`, `f659-fresh-original-input-sun8-source-and-normalcut-consumer-review`, `f660-fresh-original-input-sun8-exceptional-actual-coset-review`, and `f662-report-v23-werner-core-falsification-documentary-audit`; `review-waves/f596-actual-ame48-t24-entire-4555-same-tensor-frontier/parent-selected-instance-process-major-quarantine-v1.json`; `parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json`; and `parent-prerun-f746-matching-and-f749-occupancy-design-corrections-v1.json`. All genuinely held episodes and EVERY proof/method/selection/planning/verification/reporting/confidence/downstream consumer remained NONINPUT. The exclusive file-creation I/O is not a scientific experiment.
