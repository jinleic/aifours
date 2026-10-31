# F760: coupled six-to-eight-frequency actual-box zero relations

**Status: NONBLIND same-harness GENERAL AUTHOR, written candidate; not independently checked or adopted.** The global universal-SPR/ROOT question and existence of an eligible zero dual remain **OPEN**. I give (i) a simultaneous edge-corner compression for every grouped node, without changing the original eight-coordinate aggregate, endpoint weights, frequencies, or box; (ii) a necessary-and-sufficient coupled barycentric formulation of every sparse six-, seven-, and eight-frequency case, including zero parity values and every endpoint pattern; and (iii) a stricter uniform obstruction and an exact polynomial feasibility reformulation of the six-frequency/no-endpoint stratum. The latter excludes parity-zero samples and forces a very particular pair of adjacent reverse events; it does **not** exclude the entire stratum. These are author-written claims, pending a separate full parent read, independent reconstruction, and disposition. No numerical or symbolic scientific program was run.

Native clock observed before composition: `2026-10-30T17:45:55-0700 PDT`. It is not a claimed file-creation or research-start time.

## 1. Scope, physical object, and imports

Fix **any one** nonempty compact independent real coefficient box K of monic degree-seven polynomials for which **every actual member is strictly Hurwitz**, including any degenerate coefficient intervals. Put `t=ω²>0` and

`E_a(t)=a0−a2 t+a4 t²−a6 t³`,  `O_a(t)=a1−a3 t+a5 t²−t³`,

`r_a(t)=(E,tO,−tE,−t²O,t²E,t³O,−t³E,−t⁴O)`.

At a fixed t the *same member's* pair `(E,O)` fills its actual rectangle `R(t)=[E−,E+]×[O−,O+]`. Its four vertices are values of the four physical parity corners `C_{σ,τ}`; all subsequent corner choices are among these four actual polynomials, never independent fictional E/O choices. The rectangle excludes `(0,0)`, since independence would otherwise realize an actual polynomial with an imaginary-axis root. The center has positive constant coefficient `b0`. I retain the packet's strict Hermite–Biehler/interlacing and actual six-band ordering, and the scoped actual zero-hull/common-monic-Q alternative. In particular, a zero dual requires **both parities to have a positive-width coefficient interval**; then both pointwise parity widths are strictly positive at every t>0, and the six disjoint actual closed bands occur as

`IE1 < IO1 < IE2 < IO2 < IE3 < IO3`.

I also retain the **named at-most-five-distinct-positive-frequency strict-negative no-go** exactly as an import for the general `n≥6` conclusion. No proof below discharges that import. The eight-total-atom reduction and two physical reverse pairs are the adopted scoped input S2. Neither this input nor my subsequent reductions asserts existence of a zero dual, arbitrary marker realizability, a same-box weak-to-strict shortcut, a universal Q, or a ROOT theorem.

Consider an actual finite-corner zero relation

`Σ_{j=1}^m w_j r_{C_j}(t_j) + λ e0 + μ e7 = 0`,

with `w_j,t_j>0`, `λ,μ≥0`, not all terms zero. Let `z=1_{λ>0}+1_{μ>0}`, and for a chosen sparse representation suppose `m+z≤8`. Group equal finite frequencies into `0<u1<⋯<un`, with total weight `W_i>0` and a single actual weighted-average pair `(E_i,O_i)∈R(u_i)` at each i. Set `X_i=W_i E_i`, `Y_i=W_i u_i O_i`. Then, including the endpoints,

`Σ X_i=−λ`, `Σ X_i u_i^k=0` for `k=1,2,3`;
`Σ Y_i u_i^k=0` for `k=0,1,2`, `Σ Y_i u_i³=μ`.  (1)

The actual-pair exclusion means `(E_i,O_i)≠(0,0)`. For every possible zero dual, S2 supplies some chosen sparse representation with `6≤n≤8`; the conclusions about a representation below concern that representation, not every possible presentation of the dual.

## 2. Physical edge compression, preserving the whole relation

**Claim A.** Given any grouped finite-corner zero relation on such a K, there is another relation on exactly the same finite frequencies, with the same eight-coordinate aggregate, λ and μ, and no more finite atoms, in which every group is either a single physical corner or a positive mixture of **two adjacent** physical corners sharing one parity endpoint.

**Proof.** Leave a group already consisting of one corner unchanged. In any other group fix its actual pair `v=(E_i,O_i)≠0` and its positive total weight `W_i`. Since `R(u_i)` is compact and full-dimensional, the maximum `s=max{ρ≥1: ρv∈R(u_i)}` exists and is finite; `sv` lies on an edge. Its two edge vertices are adjacent physical corners, so write `sv=θ v_C+(1−θ)v_D`, `0≤θ≤1`. Replace the group by corner weights `(W_i/s)θ` and `(W_i/s)(1−θ)`, omitting zero weights. The replacement weighted pair equals `W_i v` exactly. Since all eight row coordinates are linear in the same E/O pair at the fixed u_i, all eight coordinates and both endpoint terms are unchanged. A formerly mixed group used at least two atoms and now uses at most two; a single-corner group was not enlarged. The frequency remains present and its weights stay positive. This proves the claim. □

Thus after this exact compression `m=n+M`, where M is the number of genuinely two-corner groups, and `M≤8−n−z`. The even and odd reverse pairs of S2 lie in different actual bands, hence involve **four different groups**. At least `4−min(4,8−n−z)` of those four groups are single physical corners. The complete sparse cases are:

| n | z | maximum M | minimum singleton groups | minimum singleton groups among the four reverse-pair nodes |
|---:|---:|---:|---:|---:|
| 6 | 0 | 2 | 4 | 2 |
| 6 | 1 | 1 | 5 | 3 |
| 6 | 2 | 0 | 6 | 4 |
| 7 | 0 | 1 | 6 | 3 |
| 7 | 1 | 0 | 7 | 4 |
| 8 | 0 | 0 | 8 | 4 |

No other z is compatible with `n≥6` and `m+z≤8`. If all four pair groups are singletons and only two distinct corners occur in the whole relation, those corners must differ in **both** parity orientations: the opposite signs in each reverse pair require both endpoints of that parity. They are therefore diagonal or antidiagonal vertices of the physical rectangle. This is only a necessary condition, not a two-corner construction.

## 3. Exact coupled barycentric reduction for all 6/7/8 cases

Let `H(t)=∏_{i=1}^n (t−u_i)`, `P=∏_{i=1}^n u_i`, and `d=n−4` (so d is 2, 3, or 4). There are unique real polynomials `A,B` of degree at most d such that

`X_i=A(u_i)/(u_i H′(u_i))`,  `Y_i=B(u_i)/H′(u_i)`.  (2)

Their endpoint constraints are exactly

`A(0)=(−1)^n λ P`,  `[t^d]B=μ`.  (3)

Here `[t^d]B` means the coefficient of exactly `t^d`; when μ=0, the degree of B is smaller. In particular, for n=6 the constant term of A is `λP` and the quadratic coefficient of B is μ; for n=7 the constant is `−λP` and the cubic coefficient is μ; for n=8 they are `λP` and the quartic coefficient μ.

**Derivation and converse.** Interpolate the values `u_i X_i H′(u_i)` by a polynomial of degree at most `n−1`. For any interpolation polynomial D, `Σ D(u_i)u_i^k/H′(u_i)` is the coefficient of `t^{n−1}` in the degree-`<n` interpolation of `t^k D(t)`. Successive vanishing for k=0,1,2 forces the coefficients of degrees `n−1,n−2,n−3` to vanish, giving A of degree at most `n−4`; the same argument gives B from Y. Conversely these degree bounds make those moments vanish. Evaluating the Lagrange formula for A at zero gives `A(0)=−H(0)Σ X_i=H(0)λ`, and the degree bound makes `Σ u_i³Y_i=[t^{n−4}]B`. This proves (2)–(3), both ways. No parity value or endpoint is divided away.

The necessary **and sufficient** actual-coupling equations, after Claim A, are, for every i,

`(A(u_i), B(u_i)) = u_i H′(u_i) W_i (E_i,O_i)`,  `W_i>0`,  (4)

where `(E_i,O_i)` is either one physical corner pair or one positive convex combination of two **adjacent** physical corner pairs at the same u_i. The same two mixture weights are used for both entries. At most `8−n−z` groups may be mixed. Equations (3)–(4), actual eligibility, the stated endpoint signs and `0<u1<⋯<un`, are an exact existential formulation of the sparse original zero relation: a solution gives the original eight moment equations and hence the relation, and any original relation can be converted to one by Claim A. In particular `(A(u_i),B(u_i))≠(0,0)`; either entry separately may vanish. Cross-multiplication `A(u_i) O_i−B(u_i) E_i=0` alone is **not** sufficient: (4)'s common positive W and the actual rectangle remain indispensable.

For a single physical corner C, `A(t)O_C(t)−B(t)E_C(t)` has degree at most `n−1` and vanishes at each singleton frequency assigned to C. It can be identically zero in the general 6/7/8 formulation; no root-count conclusion is taken from its degree without ruling this out. Mixed-node equations use the **same** adjacent-corner convex combination, not a separately selected even and odd endpoint.

## 4. Uniform zero/repetition obstruction, including endpoint patterns

For a parity sequence, delete zeros **only for sign counting**. From (1), the packet's polynomial sign argument gives at least three sign changes; if λ=0 the X sequence has at least four, and if μ=0 the Y sequence has at least four. The odd reverse pair lies in one actual odd band, throughout which the even sign is strict and constant. Thus X's nonzero sign word contains a repeated adjacent sign. The even reverse pair similarly forces a repeated adjacent sign in Y's nonzero word. Consequently, if `q_E=# {i:E_i=0}` and `q_O=# {i:O_i=0}`, then

`q_E ≤ n−5−1_{λ=0}`,  `q_O ≤ n−5−1_{μ=0}`.  (5)

Moreover no node contributes to both zero counts. These bounds hold for any grouped actual zero relation with both reverse pairs, not merely a particular corner allocation. In the complete sparse range they become:

| n | endpoint pattern | q_E bound | q_O bound |
|---:|---|---:|---:|
| 6 | λ=μ=0 | 0 | 0 |
| 6 | λ>0, μ=0 | 1 | 0 |
| 6 | λ=0, μ>0 | 0 | 1 |
| 6 | λ>0, μ>0 | 1 | 1 |
| 7 | λ=μ=0 | 1 | 1 |
| 7 | λ>0, μ=0 | 2 | 1 |
| 7 | λ=0, μ>0 | 1 | 2 |
| 8 | λ=μ=0 | 2 | 2 |

For example, the first row is a new uniform exclusion of **every** six-frequency/no-endpoint relation having any zero grouped parity value; it does not exclude nonzero parity values or a mixed corner group. When n=6 and λ=0, the unique X repeat occurs at the two consecutive nodes of the odd reverse pair, and no other odd band can contain two nodes. Symmetrically, n=6 and μ=0 force the even reverse pair to be consecutive and to be the unique even band with two nodes. These single-endpoint statements do not require the other endpoint to vanish.

## 5. Six frequencies and no endpoints: exact four-change structure

Assume now `n=6` and `λ=μ=0`. By (5) all 12 values E_i,O_i are nonzero. Both X and Y have at least four sign changes, and each has a mandatory repeat; hence each has **exactly four changes and exactly one repeated adjacent sign**. The X repeat is the pair in the odd reverse band; the Y repeat is the pair in the even reverse band. The bands are disjoint, so these are two different consecutive-node gaps; in the other three gaps **both** parity signs change. Exactly two nodes occur in each of the two reverse bands, and every other actual band contains at most one node. This excludes all six-node/no-endpoint sign configurations outside those conditions on **every** eligible K, not merely configurations in an invented band diagram.

The moment equations give still more. With H as above there are nonzero `c_E,c_O` and distinct positive `α,β` such that

`X_i=c_E (u_i−α)/H′(u_i)`,  `Y_i=c_O (u_i−β)/H′(u_i)`.  (6)

Indeed, A has zero constant and B has zero quadratic coefficient, so both displayed numerators are affine; the unique repeated sign in each word forces a genuine sign-changing root between the corresponding adjacent nodes. Precisely, **α lies in the open gap of the odd reverse pair and β lies in the open gap of the even reverse pair**, both strictly inside their actual bands. Thus α,β are not arbitrary free markers, are not sampled frequencies, and cannot coincide. With `k=c_O/c_E≠0`, the same physical values and same positive W obey

`u_i O_i (u_i−α) = k E_i (u_i−β)` for all six i.  (7)

The later node of an even reverse pair has E and O of the same strict sign: it is `(+,+)` in even bands 1/3 and `(−,−)` in band 2. Its β-gap denominator is positive, while α lies entirely to one side of that band. Applying (7) there yields the additional physical ordering restriction

`sign(k)=sign(β−α)`.  (8)

This uses the actual opposite-parity signs in the specific same box; it is not a consequence of independent sign words alone.

### 5.1. One quintic per physical corner and positive common weights

For each of the four actual corners define

`P_C(t)=k(t−β) E_C(t)−t(t−α) O_C(t)`.  (9)

It is a **monic degree-five** real polynomial: `O_C` has leading term `−t³`, while the other term has degree at most four. Every single-corner group at u_i must satisfy `P_C(u_i)=0`. At a two-corner edge group with weights θ and 1−θ the condition is

`θ P_C(u_i)+(1−θ)P_D(u_i)=0`,  `0<θ<1`.  (10)

Thus its two physical edge values must straddle zero, or both vanish. At least four of the six groups are singleton roots; the other at most two are actual adjacent-edge mixtures. The same θ determines E_i and O_i. Critically, (9)–(10) alone are not a certificate: the reconstructed weights must also share one nonzero scalar c_E and obey

`W_i = c_E (u_i−α)/(E_i H′(u_i)) > 0` for every i.  (11)

These six positivity inequalities, actual eligibility of the entire coefficient box, and the shared-corner/edge constraints are not optional.

**Exact iff for this stratum.** For any eligible K, the existence of a zero relation with exactly six distinct positive finite frequencies, no endpoint atoms, and at most eight finite corner atoms is equivalent to existence of ordered `u_i`, nonzero `c_E,k`, and α,β satisfying all the actual-band, consecutive-reverse, nonzero-value, corner/adjacent-edge, mixture-budget and sign requirements above, together with (9)–(11). For necessity, use Claim A, (5)–(8). For sufficiency, set each actual group weight by (11), split it by its displayed actual corner/edge weights, and use (9)–(10) to obtain (7). Then the resulting X and Y have exactly the forms (6) with `c_O=k c_E`; the degree-one-over-H′ Vandermonde identity annihilates all moments k=0,1,2,3. All six frequencies and weights are positive, the finite atom count is at most eight, and λ=μ=0, so the original eight-coordinate zero relation follows. This is an exact feasibility reformulation, not a proof that its real solutions do or do not exist.

An equivalent common-phase observation is useful but makes no SPR claim. Define the degree-four real polynomial

`Q_*(s)=s⁴−k s³+α s²−kβ s = s(s³−k s²+α s−kβ)`.

At each sampled frequency its actual complex value and that of the grouped polynomial are collinear, with scalar `c_E/(W_i u_i H′(u_i))`, whose sign alternates across the six nodes. If α>β, then k<0 and the cubic factor is strictly Hurwitz by the cubic Routh inequalities; Q_* still has a root at zero. If α<β, then k>0 and its cubic Routh first column has signs `+,-,-,-`, so it has exactly one right-half-plane root. Q_* is neither the demanded monic septic synthesis numerator nor evidence of a common positive-real margin.

## 6. Independent scrutiny of the packet's unadopted F742 refinements

I checked the following claims independently in writing before using them; this is not an independent reviewer or parent adoption.

* **Strict interior and corner orientation.** At an even or odd band endpoint the actual interval lies on one side of zero; hence both nodes of a strict reverse pair lie in its interior. In a downward band, the earlier negative group must have positive weight on a lower-parity corner and the later positive group on an upper-parity corner; for an upward band the orientations reverse. This stays true for mixtures because the opposite endpoint has the wrong strict sign. The opposite parity has fixed nonzero sign throughout that band. These facts justify the strict-band and sign assertions above.
* **Center deficit.** Pairing the original relation separately with the even and odd center parts gives `Σ W_i E_i E_b(u_i)=−λ b0` and `Σ W_i u_i O_i O_b(u_i)=−μ`. Each physical reverse pair forces at least one strict mismatch with that parity's center sign: otherwise the earlier and later nodes would be on the wrong sides of the center root. Thus both negative parts are nonempty and the exact positive/negative balances in F742 follow. They are necessary balances, not contradictions.
* **Physical quadrant windows.** Intersecting the signs of actual envelope intervals gives the ordered possible windows: `(+,+)` in `(0,R^E1) ∪ (L^O2,R^E3)`, `(−,−)` in `(L^O1,R^E2) ∪ (L^O3,∞)`, `(−,+)` in `(L^E1,R^O1) ∪ (L^E3,R^O3)`, and `(+ ,−)` in `(L^E2,R^O2)`. These are strict-sign windows and follow from actual envelopes and physical independence, not arbitrary markers. Consequently same-sign quadrant windows occur `(++ )_1,(−−)_1,(++ )_2,(−−)_2` in that order, and opposite-sign windows occur `(−+)_1,(+−),(−+)_2` in that order.
* **F742's two extra low-node subcases.** For four nodes, the moment and sign arguments force λ,μ>0, and Vandermonde gives `X_i=λP/(u_i H′_4(u_i))`, `Y_i=μ/H′_4(u_i)`. Both signs are `−,+,−,+`, which would require `(−−),(++),(−−),(++)`, impossible in the actual windows just stated. For five nodes with λ=μ=0, the two full four-moment null vectors are `X_i=c/H′_5(u_i)` and `Y_i=d/H′_5(u_i)` with c,d nonzero. Their five alternating same-sign or opposite-sign quadrants would require respectively five occurrences in the four-window or three-window order, impossible. This does **not** establish the other five-node endpoint patterns: the general five-frequency import remains unpaid here.

No mathematical correction to these specifically examined F742 claims is asserted. Their source remains an unadopted author reconstruction; this return does not certify the entirety of F742 or any outgoing linked scientific source.

## 7. Remaining frontier and verification boundaries

The exact first unpaid step for n=6,z=0 is deciding whether the coupled, same-box system in §5.1 can be realized with actual all-member eligibility and the common positive weights. For `n=6,z=1,2`, `n=7,z=0,1`, and `n=8,z=0`, §3 gives the complete surviving coupled systems with endpoint coefficients, zero entries, actual corner/edge multiplicities and weights retained; their nonexistence or a genuine eligible solution remains unproved. A synthetic sign word, separately realized E/O distributions, a positive eligible box with no zero relation, or a single-corner-stability check would not answer any of these cases. No rational witness, universal obstruction, common septic Q, strict-negative certificate, all-ray ROOT solution, or universal SPR theorem is claimed.

**NOT TESTED:** no scientific child execution, finite enumeration, solver, CAS, code compilation, tests, build, formatter, lint, scientific external CLI, public-source search, or independent family/human/kernel review. No finite source is proposed or run, and no parent GO is claimed. Parent full read, a disjoint check and explicit disposition are separate future actions. Original-source identity, literature priority and novelty are unverified; do not promote this as a global or family-verified result.

## 8. Complete input and process coverage

All five science inputs were read **only** as the sole rendered packet part, serially in consecutive raw ranges of at most 20 LF from LF1 through LF388 and its ending before comparison or mathematical research. Parent-reported source rendering and binding are not a separate source-identity authentication. With R=`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`:

* S1 `review-waves/f742-septic-two-parity-physical-backtracking-proof-author/author-reconstruction-v1.md`, complete LF1–247, SHA256 `9cb4340f358000e00cdbb0b83a287e171e140143de9ed7aacd78d1f5a34f3b87` (unadopted refinement).
* S2 `dispositions/info-2-actual-septic-eight-atom-zero-dual-six-frequency-and-parity-backtracking-parent-v1.md`, complete LF1–39, SHA256 `866dd92b58bb2422281abe815bc1e6cae8e5f8f94c96f2d7eaed00bad372a183` (adopted scope and named import).
* S3 `dispositions/info-2-actual-both-parity-septic-four-corner-sdp-and-zero-dual-parent-v1.md`, complete LF1–29, SHA256 `949af8c879058b8be166086ab06dbba03d896a26adc64e1621dfbdf7a72e4d0b`.
* S4 `dispositions/info-2-actual-both-parity-septic-four-corner-sdp-and-zero-dual-parent-v1-erratum-1.md`, complete LF1–5, SHA256 `513b44b2591954b535e138df611fab0698af2b8363b89768a5e45f320d50f5d4`.
* S5 `dispositions/info-2-actual-box-three-root-dual-odd-cone-and-six-node-sparsification-parent-v1.md`, complete LF1–46, SHA256 `5f35c9a1b1db95a89f928e7e7566492d29e05555d0b08822cfaf2f2a78ab58ae`.

The packet `review-waves/f760-septic-six-eight-frequency-coupled-frontier-author/literal-packet-part-01-v1.md` has 388 LF, SHA256 `1071135916d901c7f8b24ad975635d75522b5a918d345c9fec30faea1bb43c86`. Before body access I read actual dispatch, the complete manifest, freeze receipt, final binding, prepared metadata, and all 22/22 listed permission/status controls through their endings; then sent Main the direct PREBODY ACK. Administrative live SHA/byte/LF comparisons matched the five inputs, 22 controls and wave bindings. Wave metadata pins: manifest `0c495ffb8ebfe009e39b1935cfdd91127c2a311ad3f55ac76af31a8fb2ccd593`; freeze `39676c3d5b1fec69fa28f2113c788601ef8d9f23f4f8a897a97bd719c2ccf573`; final binding `635dc0f6aef2b1f45bea584cdc29ea6420929f93c15e874c0a0c0b345b12713a`; prepared metadata `4e46559e108a7e47eb39b46e1a82652b5b7797dc8a9c8806da289842d3923ad9`; actual dispatch `3f1056c8dc3fbd8ed84c4b03cee749f7e434e251ca181eac6757a21ead960c9f`.

A packet-read path typo omitted `-author` at LF181–200 and returned path-not-found with **no content**; I immediately disclosed it to Main, then resumed at LF181 using the frozen path before any science. No outgoing scientific link, unspecified sibling proof, old code, held episode, or held proof/method/selection/planning/verification/reporting/confidence/downstream consumer was used. Hashing/admin file I/O are not scientific execution. This record does not certify private cognition or imply family/human/kernel/source-identity review.
