# F839: actual mixed-edge half-gap budgets and a stronger physical support restriction

**Status.** Prospective, nonblind, same-harness GENERAL AUTHOR written candidate; parent disposition and independent checking are separate. The statements below are necessary consequences for one actual eligible box and one actual six-node, no-endpoint zero relation. They do not assert that any of the 12 rows is realizable or that any whole row, eligible zero dual, SPR problem, or ROOT problem is closed. The main new written consequences beyond the two named F817 examples are: (i) adjacent physical corner quintics have no common positive root; (ii) an all-node extremal-sign filter and its explicit 12-row root floors; (iii) three saturated positive-root cases; and (iv) two larger, unconditional actual support exclusions on row `(2,4;3,4)`. These are not claimed logically independent of the full F817 inequalities together with all of their actual coupling hypotheses.

## 1. Exact object and the conditional physical interface

Fix **one** nonempty compact independent real coefficient box `K` of monic septics, every actual member of which is strictly Hurwitz. For an actual member `a` and `t>0`, set

\[
 E_a(t)=a_0-a_2t+a_4t^2-a_6t^3,\qquad
 O_a(t)=a_1-a_3t+a_5t^2-t^3,
\]
\[
 r_a(t)=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a).
\]

Take a nontrivial zero relation of actual rows with exactly six distinct positive finite frequencies `0<u_1<...<u_6` and **no** endpoint atoms. Group each frequency, using one common positive total weight `W_i` and the same actual averaged parity pair `(E_i,O_i)` for both coordinates. Its eight equations are

\[
 \sum_{i=1}^6 u_i^qX_i=\sum_{i=1}^6 u_i^qY_i=0\quad(0\le q\le3),\qquad X_i=W_iE_i,\quad Y_i=W_i u_iO_i. \tag{1}
\]

At every `t`, independence makes the same-member attainable pair set exactly
`R(t)=[E_-(t),E_+(t)]×[O_-(t),O_+(t)]`. These four vertices are values of four **fixed actual parity-corner polynomials** `C_{στ}`, with the first sign selecting `E_σ` and the second selecting `O_τ`. The pointwise rectangle is not a claim that the entire coefficient box is the convex hull of four polynomials. The rectangle excludes `(0,0)`: otherwise independence constructs an actual member with an imaginary-axis root. Let `E_b,O_b` be the parity-center polynomials and `H_E,H_O` the half-width functions, so `E_±=E_b±H_E`, `O_±=O_b±H_O`.

Both parity widths are strictly positive at every positive `t`. Indeed, pairing (1) with the two center polynomials gives `Σ W_i E_i E_b(u_i)=0` and `Σ W_i u_i O_i O_b(u_i)=0`. If one parity is coefficientwise fixed, its identity is a sum of squares and forces it to vanish at every node; origin exclusion makes the other parity's product with its center strictly positive at each node, a contradiction. Thus each parity has a positive-width coefficient, and the nonnegative-coefficient width polynomial is strictly positive on `(0,∞)`. The same center-pairing argument shows neither sequence `X` nor `Y` is identically zero.

**Named conditional import.** We use strict Hermite–Biehler interlacing for each actual Hurwitz septic and the physical rectangle consequences recorded in packet S3–S5: the nondegenerate closed envelope-root bands are strictly separated,

\[
 B_1=I^E_1<B_2=I^O_1<B_3=I^E_2<B_4=I^O_2<B_5=I^E_3<B_6=I^O_3. \tag{2}
\]

In `I^E_l` the complementary O sign is `+,-,+` for `l=1,2,3`; in `I^O_j` the complementary E sign is `-,+,-`. The varying parity's envelope strictly straddles zero in the band's interior, with one-sided signs at its endpoints. We use only this actual local band geometry and the ordinary physical quadrant progression, not an all-frequencies fixed-envelope-sign assertion. The full underlying bodies linked by S3–S5 were not opened and are not silently treated as reconstructed here.

Deleting zero entries only for counting, each sequence in (1) has at least four sign changes: otherwise a polynomial of degree at most three, with a simple root in each sign-change gap and oriented appropriately, pairs strictly positively with it. In the absence of a strict reverse-sign pair in one of its own physical bands, a parity's sign word follows the ordinary `+,-,+,-` progression and has at most three changes. Thus both parities have strict reverse pairs, strictly in the interiors of different actual bands. The odd pair forces a repeat in the even sign word, and conversely. Four changes plus a repeat among at most six terms forces **all twelve grouped parity values nonzero**, exactly four changes and one repeat per word, and each pair to occupy a consecutive node gap. No third sample lies in either reverse band.

With `H(t)=∏_{i=1}^6(t-u_i)`, the Vandermonde identities give nonzero `c_E,c_O` and distinct positive markers `α,β` such that

\[
 X_i=\frac{c_E(u_i-\alpha)}{H'(u_i)},\qquad
 Y_i=\frac{c_O(u_i-\beta)}{H'(u_i)},\qquad
 k=\frac{c_O}{c_E}\ne0. \tag{3}
\]

`α` is in the odd reverse gap and `β` in the even reverse gap; neither is a sample. At the later node of the even reverse pair, the actual E and O have the same strict sign and `u_i>β`. Since the two bands are disjoint, (3) gives

\[
 u_iO_i(u_i-\alpha)=k E_i(u_i-\beta),\qquad
 \operatorname{sgn}k=\operatorname{sgn}(\beta-\alpha). \tag{4}
\]

## 2. All 12 physical rows, boundaries and signs

For a strict quadrant use levels 0 through 6 in the actual order
`(++),(-+),(--),(+-),(++),(-+),(--)`. A reverse gap decrements the level by 1; every other gap flips both signs and increments it by at least 2, congruent to 2 modulo 4. With two disjoint reverse gaps and only levels 0–6, all three double flips must be exactly `+2`. Let `p<q` be the reverse gap indices, `r<s` their physical band indices, `a=p-1`, `b=q-p-1≥1`, `c=5-q`. Then

\[
 s=r+2b-1,\quad r\ge2a,\quad s-1+2c\le6,\quad \ell_1=r-2a. \tag{5}
\]

The gap pairs `(1,3),(1,4),(1,5),(2,4),(2,5),(3,5)` give respective possible `r` sets `{1,2},{1,2},{1},{2,3,4},{2,3},{4,5}`; `s` is determined by (5). This produces exactly the following necessary rows. The complete six-level word in any row starts at `ℓ_1` and adds `−1` in gaps `p,q`, `+2` in the other gaps. In addition to those strict quadrant conditions, the indicated pair nodes really lie in the interiors of **those actual bands**. A quadrant word alone is not a physical realization.

Put `d_1=min(α,β)`, `d_2=max(α,β)`, and let `n=(p,q-p,6-q)` be the number of all samples in `(0,d_1),(d_1,d_2),(d_2,∞)`. The sign string is that of **each** actual corner quintic at `0,d_1,d_2,∞`; `ε` records the three adjacent sign changes. The last column is an additional all-node floor proved in Section 5: `h:C` means that the indicated actual corner must have at least two positive-root multiplicities in interval `h`, even when no singleton is assigned to it.

| `(p,q;r,s)` | `ℓ_1` | `sgn k` | `n` | boundary signs | `ε` | same-sign floor `h:C` |
|---|---:|:---:|---|:---:|:---:|---|
| `(1,3;1,2)` | 1 | − | `(1,2,3)` | `++++` | `000` | `1:--, 2:+-, 3:++` |
| `(1,3;2,3)` | 2 | + | `(1,2,3)` | `-+++` | `100` | `2:++, 3:-+` |
| `(1,4;1,4)` | 1 | − | `(1,3,2)` | `++-+` | `011` | `1:--` |
| `(1,4;2,5)` | 2 | + | `(1,3,2)` | `-+-+` | `111` | none |
| `(1,5;1,6)` | 1 | − | `(1,4,1)` | `++++` | `000` | `1:--, 2:+-, 3:++` |
| `(2,4;2,3)` | 0 | + | `(2,2,2)` | `-+++` | `100` | `2:++, 3:-+` |
| `(2,4;3,4)` | 1 | − | `(2,2,2)` | `+--+` | `101` | `2:-+` |
| `(2,4;4,5)` | 2 | + | `(2,2,2)` | `---+` | `001` | `1:-+, 2:--` |
| `(2,5;2,5)` | 0 | + | `(2,3,1)` | `-+-+` | `111` | none |
| `(2,5;3,6)` | 1 | − | `(2,3,1)` | `+-++` | `110` | `3:++` |
| `(3,5;4,5)` | 0 | + | `(3,2,1)` | `---+` | `001` | `1:-+, 2:--` |
| `(3,5;5,6)` | 1 | − | `(3,2,1)` | `++++` | `000` | `1:--, 2:+-, 3:++` |

## 3. Actual quintics and common positive weights

For every fixed actual physical corner `C`, define

\[
 P_C(t)=k(t-\beta)E_C(t)-t(t-\alpha)O_C(t). \tag{6}
\]

It is monic of degree five: `O_C` has leading coefficient `−1`, while the E term has degree at most four. The actual grouped pair satisfies the *same* affine functional equal to zero at every node. A singleton on `C` has `P_C(u_i)=0`. A two-corner group with actual weights `W_iθ,W_i(1−θ)` has exactly one common `θ`, with

\[
 \theta P_C(u_i)+(1-\theta)P_D(u_i)=0,\quad 0<\theta<1. \tag{7}
\]

It is not permissible to choose separate E and O mixture weights. A singleton/edge assignment plus (7) is also not enough without the **same** positive global scale: with `E_i,O_i` from the selected actual pair,

\[
 W_i=\frac{c_E(u_i-\alpha)}{E_iH'(u_i)}>0\quad(1\le i\le6),
 \qquad c_O=kc_E. \tag{8}
\]

All denominators are nonzero by Section 1. Conversely, for an eligible actual box, six ordered nodes, actual same-pair selections, physical marker placements, one nonzero `k,c_E`, (6)–(8), and all six positive weights, (3) follows; the Lagrange identities `Σu_i^m/H'(u_i)=0` for `m≤4` then give all of (1). Actual corner-atom or endpoint budgets must be separately imposed. If a chosen no-endpoint representation has at most eight total corner atoms, radial compression of each grouped rectangle ray to its boundary preserves both weighted parity coordinates and yields at most two adjacent-corner groups and at least four singleton groups. This is a statement about a chosen compressed representation, not every presentation and not the existence of such a representation.

If `α∈I^O_j`, `β∈I^E_l`, every corner has the same nonzero boundary signs

\[
 \operatorname{sgn}P_C(0)=-\operatorname{sgn}k,\quad
 \operatorname{sgn}P_C(\alpha)=(-1)^{j+1},\quad
 \operatorname{sgn}P_C(\beta)=(-1)^l\operatorname{sgn}k,\quad
 \operatorname{sgn}P_C(+\infty)=+. \tag{9}
\]

Indeed `E_C(0)>0`, `k(α−β)<0`, and the complementary parity signs are strict in the actual marker bands. In particular none of `0,α,β` is a root. For `k<0` the total positive-root multiplicity of any `P_C` is even and at most four; for `k>0` it is odd and at most five.

## 4. Independent reconstruction of the F817 half-gap budget

Fix any actual corner `C`. Let `n_{C,h}` count **all** distinct sampled nodes in interval `h` at which `P_C` vanishes, whether or not that corner is selected there. For each node of either consecutive reverse pair, let `m` be its own band's marker: `β` for the even pair and `α` for the odd pair. If `P_C(u_i)P_C(m)<0`, count the open half-gap between `u_i` and `m` once, in `g_{C,h}` for the interval containing that half-gap. Since the marker lies strictly between consecutive pair nodes, these open half-gaps contain no sample. The two half-gaps of one pair are disjoint; the two physical reverse bands are disjoint. Each counted gap contains a root, and all these roots are distinct from each other and from all counted sample roots.

Therefore, with `q_{C,h}=n_{C,h}+g_{C,h}` and `[x]_2` the representative modulo two in `{0,1}`, the exact per-corner necessary inequality is

\[
 \boxed{\displaystyle
 \sum_{h=1}^3\Bigl(q_{C,h}+[\epsilon_h-q_{C,h}]_2\Bigr)\le5.} \tag{10}
\]

On each open marker interval the total root multiplicity has the parity of its two nonzero boundary signs and is at least `q_{C,h}`. A double root, or an unsampled root needed to restore parity, is charged correctly. Any certified subset of sampled roots or forced gaps may be used: `q+[ε−q]_2` is nondecreasing in `q`. In particular, if two corner quintics vanish at the same mixed node, it must be entered as a sampled root for **both** corners, not discarded or counted as a fictitious singleton. Section 4.2 determines exactly which such cases are physically possible.

### 4.1 Actual wrong-orientation and strict-edge cases

In even band `I^E_l`, let `s=sgn O=(-1)^{l-1}`. The varying E parity goes from pre-sign `s` to post-sign `−s`. At the **earlier** reverse node the required sign is post; at the **later** it is pre. A physical corner with the other sign is the wrong endpoint. Since throughout this even band `sgn(t−α)=sgn k`, direct substitution into (6) shows that at either node both terms of the wrong corner have sign `−sgn(k)s=sgn P_C(β)`. In odd band `I^O_j`, write `s=sgn E=(-1)^j`; O goes from pre-sign `−s` to post-sign `s`. Throughout the band `k(t−β)<0`, and at either reverse node both terms of the wrong O-orientation corner have sign `−s=sgn P_C(α)`. These signs are strict because the reverse nodes are in the **interior** of genuine physical bands. Thus a singleton at a reverse node necessarily uses the correct physical orientation.

For a strictly mixed adjacent edge varying the band's own parity, its wrong endpoint has the marker's strict nonzero sign; (7) with its one common `θ` forces the other endpoint to have the strictly opposite sign and hence a root in that half-gap. For an edge varying the complementary parity, the band parity is common to both endpoints and has the required strict sign; if their values strictly straddle zero, exactly one is opposite the marker sign and forces a half-gap root. In the purely algebraic strict-mixture equation, if one endpoint value is zero then the other must also be zero; in that exceptional case both are included in `n_{C,h}` and no sign-forced gap is invented. Under the actual hypotheses here, the latter case is impossible for **every adjacent edge**, as follows.

### 4.2 Both-zero adjacent edges are actually impossible; diagonal cases complete

Put `a(t)=k(t−β)` and `b(t)=−t(t−α)`. For `t>0`,

\[
 P_{+\tau}(t)-P_{-\tau}(t)=2a(t)H_E(t),\qquad
 P_{\sigma+}(t)-P_{\sigma-}(t)=2b(t)H_O(t). \tag{11}
\]

Both widths are strictly positive. For an E-edge, (11) is nonzero except at `β`, where (9) says both values are nevertheless nonzero. For an O-edge it is nonzero except at `α`, where both are nevertheless nonzero. Hence **no two adjacent physical corner quintics have a common positive root**, including at either marker. At any strict adjacent-edge sample, (7) therefore has two nonzero, strictly opposite endpoint values and a unique common mixture coefficient. If the weight on C is `θ`, it is `θ=P_D/(P_D−P_C)`; both actual atom weights are `W_iθ,W_i(1−θ)>0`. No case is silently removed by assuming this before proving the width and marker facts.

Two opposite corners can still both vanish; no realizability is asserted. Write `P_b=aE_b+bO_b`. The exact, exhaustive diagonal conditions at `t>0` are

\[
 \begin{array}{ll}
 P_{++}=P_{--}=0 &\Longleftrightarrow\quad P_b=0,\quad aH_E+bH_O=0,\\
 P_{+-}=P_{-+}=0 &\Longleftrightarrow\quad P_b=0,\quad aH_E-bH_O=0.
 \end{array} \tag{12}
\]

If `a,b` have the same sign only the `(+-, -+)` diagonal can satisfy its width equation; if they have opposite signs only the `(++, --)` diagonal can. At a marker no corner vanishes. Thus, for `k<0`, the only possible common-root diagonals in intervals 1,2,3 are respectively `(+-, -+)`, `(++, --)`, `(+-, -+)`; for `k>0` they are `(++, --)`, `(+-, -+)`, `(++, --)`. Every other corner is then nonzero, by (11); in particular no three corners share a positive root. These assertions concern the actual common `K`, not independent polynomials or an invented marker configuration.

## 5. All-node physical extremal filter and explicit root floors

At any node, (4) says `aE_i+bO_i=0`. In each marker interval `a,b` have fixed nonzero signs. Since the actual rectangle has positive widths, the functional has a **unique** maximum corner `M_h` and a **unique** minimum corner `m_h` there. Consequently, for **every** actual group at every sample in interval `h`,

\[
 P_{M_h}(u_i)\ge0,\qquad P_{m_h}(u_i)\le0. \tag{13}
\]

The complete physical corner table is

| sign of `k` | interval | `M_h` | `m_h` |
|:---:|:---:|:---:|:---:|
| − | 1 | `++` | `--` |
| − | 2 | `-+` | `+-` |
| − | 3 | `--` | `++` |
| + | 1 | `-+` | `+-` |
| + | 2 | `--` | `++` |
| + | 3 | `+-` | `-+` |

Equality in either inequality means the grouped actual pair is exactly that extremal rectangle vertex: otherwise a strict inequality would remain after taking the common positive weighted average. In particular, if a genuine group contains two distinct actual pair values, both inequalities in (13) are strict. This handles zero values and arbitrary actual-member mixtures, not merely adjacent edges or a sparse representation.

Each of the three intervals contains at least one sample in every row of Section 2. If both boundary signs of an interval are `−`, apply (13) to `M_h`; if both are `+`, apply it to `m_h`. A nonnegative value between two negative endpoint signs, or a nonpositive value between two positive endpoint signs, forces at least two root multiplicities. The equality case may be an even-multiplicity zero at the sample, or may involve a second root elsewhere; it is not omitted. This proves every entry of the last table column in Section 2.

Define `F_{C,h}=2` for that row's listed `h:C` and `F_{C,h}=0` otherwise. The following safe combined budget holds for every actual corner:

\[
 \boxed{\displaystyle
 \sum_{h=1}^3\max\left\{q_{C,h}+[\epsilon_h-q_{C,h}]_2,\ F_{C,h}\right\}\le5.} \tag{14}
\]

The maximum, rather than a sum of the two lower bounds within an interval, avoids double-counting roots. This is an explicit all-12-row physical consequence; it does not close a row.

A stronger all-node sign sieve is also available without assigning imaginary roots: for one actual `P_C`, order any selected probes among `0,α,β,∞,u_1,...,u_6`, keeping `0,α,β,∞`, and record their actual signs. Between successive nonzero probes let `z` be the number of included zero probes, and `e` the bit indicating a sign change of the two nonzero endpoint values. At least `z+[e−z]_2` root multiplicities lie in that open interval. Sum over successive nonzero probes and require the result `≤5`. Unknown node signs may simply be omitted; (13), actual edge signs, and observed zeros supply legitimate probes. This includes the equality and both-zero-diagonal cases and can use signs outside the four reverse nodes. It is a necessary actual-quintic test, not a stand-alone feasibility certificate.

### 5.1 Three saturated rows

The all-node floor has the following complete consequences, still conditional on an actual relation.

* `(1,4;1,4)`: `k<0`, boundaries `++-+`; in interval 1 the minimum is `C_{--}` and `P_{--}(u_1)≤0`. Thus this corner has exactly two positive-root multiplicities in interval 1 and one each in intervals 2 and 3. If the value at `u_1` is negative, the two roots in interval 1 lie strictly on opposite sides of `u_1`; if it is zero, that sample counts and the two multiplicities may coincide there or include a second root. Equality forces the grouped pair at `u_1` to be the `--` vertex.
* `(2,5;3,6)`: `k<0`, boundaries `+-++`; in interval 3 the minimum is `C_{++}` and `P_{++}(u_6)≤0`. This corner has exactly one positive-root multiplicity in each of intervals 1 and 2 and exactly two in interval 3, with the analogous strict-negative/zero alternatives at `u_6`; equality forces the `++` vertex there.
* `(2,4;3,4)`: `k<0`, boundaries `+--+`; in interval 2 the maximum is `C_{-+}`. Since `β<u_3<u_4<α`, both `P_{-+}(u_3)` and `P_{-+}(u_4)` are nonnegative. One root lies in `(β,u_3]`, another in `[u_4,α)`, so they are distinct. The opposite boundary signs in each outer interval require one root there too. The quintic therefore has exactly four positive roots, all simple, and exactly one negative simple root; in particular `P_{-+}(t)>0` for all `u_3<t<u_4`. If either displayed node value is zero, that group's pair is exactly the `-+` vertex; a genuine distinct-pair mixture at that node is impossible.

For the first two bullets the total positive multiplicity is exactly four, not necessarily four distinct roots; the two one-root intervals are simple. In each of the three bullets the fifth root is negative and simple: the monic quintic tends to `−∞` at negative infinity while `P_C(0)>0`. These facts use the actual node and band order, not an abstract choice of markers.

## 6. Both F817 exclusions, and a larger whole-support result

Specialize only in this section to the actual row `(2,4;3,4)`. The first reverse band is `I^E_2`, the second `I^O_2`; hence

\[
 0<u_1<u_2<\beta<u_3<u_4<\alpha<u_5<u_6,\quad
 k<0,\quad (\operatorname{sgn}P_C(0),\operatorname{sgn}P_C(\beta),
 \operatorname{sgn}P_C(\alpha),\operatorname{sgn}P_C(\infty))=(+,-,-,+). \tag{15}
\]

**Whole-support exclusion A.** For every eligible box and every actual six-node relation in this row, it is impossible that

\[
 P_{--}(u_1)=P_{--}(u_3)=P_{--}(u_6)=0. \tag{16}
\]

There is no condition on which corners are used at `u_5`, nor on how many atoms any group has. Indeed `C_{--}` is the unique maximum in interval 3, so the actual group equation gives `P_{--}(u_5)≥0`. If it is positive, continuity and `P_{--}(α)<0` give another root in `(α,u_5)`; if it is zero, `u_5` itself is another root. In either case this root is distinct from `u_6`. The first marker interval has the root `u_1` and opposite endpoint signs, costing at least 1; the middle has `u_3` and equal negative endpoint signs, costing at least 2; the last has two distinct roots and opposite endpoint signs, costing at least 3. Total multiplicity is at least 6, contradicting degree 5. Equality in (13) is explicitly included.

**Whole-support exclusion B.** Likewise it is impossible that

\[
 P_{++}(u_1)=P_{++}(u_4)=P_{++}(u_6)=0. \tag{17}
\]

Here `C_{++}` is the unique maximum in interval 1, so `P_{++}(u_2)≥0`. A positive value forces a root in `(u_2,β)`; equality gives a root at `u_2`. This root is distinct from `u_1`. The interval multiplicity costs are at least `3,2,1`, respectively, again totaling 6. The proof permits **any** actual group at `u_2`, including a singleton, a strict edge, a diagonal mixture with both values zero, or a larger positive mixture. It does not assume the remaining groups are singletons or invoke an eight-atom reduction.

Consequently (16) excludes, in particular, singleton groups `u_1,u_3,u_6` on `C_{--}` **regardless** of the group at `u_5`; (17) excludes singleton groups `u_1,u_4,u_6` on `C_{++}` **regardless** of the group at `u_2`. The conditions are even stronger than singleton language because they forbid the displayed corner-zero patterns whether or not the corner is selected at those nodes.

The two F817 examples are included and can also be checked directly with their stated edges. At `u_5` the `O_+` endpoint `C_{-+}` of the edge `C_{--}–C_{-+}` is wrong-oriented in actual `I^O_2`, so `P_{-+}(u_5)<0=P_{\rm group}(u_5)`. A strict common mixture forces `P_{--}(u_5)>0`, hence the root `(α,u_5)` used above. At `u_2` the `E_-` endpoint `C_{-+}` of `C_{++}–C_{-+}` is wrong-oriented in actual `I^E_2`, so `P_{-+}(u_2)<0=P_{\rm group}(u_2)`; strict common mixing forces `P_{++}(u_2)>0` and the root `(u_2,β)`. All individual atom weights are positive multiples of the same group weight, and the rest of the six common weights remain subject to (8). With only the three indicated singleton roots and the original singleton-only parity calculation, the per-corner lower bound is `1+2+1=4`; it is the actual fourth root/half-gap and its parity charge that forces 6. Neither exclusion asserts a feasible box or rules out other support patterns in this row.

## 7. Exact residual and limits

For each of the 12 rows the residual still quantifies over one compact independent all-member-Hurwitz actual box; ordered positive nodes and actual bands; one α and β in the appropriate consecutive reverse gaps; actual same-node pairs or genuine physical corner/edge mixtures; one common `k,c_E`; the six strictly positive weights (8); and, if a chosen sparse representation is being considered, its real atom and endpoint budget. Sections 4–6 give necessary constraints on those **same** objects. No sign table, center determinant, arbitrary root placement, separate parity weighting, or algebraic mixture alone proves existence. No global row closure, complete classification of all support assignments, eligible zero dual, all-box common numerator, SPR/ROOT theorem, human/family/kernel acceptance, publication priority, novelty, or source-identity result is claimed.

The ≤5-frequency strict-negative theorem, its eligible buffered enlargement, the connected-corner compactification/eight-total-atom reduction, and the compact zero-hull/strict-SPR or ROOT alternatives are separate named conditional imports if used for a wider conclusion; they are not proved or needed for the fixed six-node/no-endpoint results here. Other endpoint patterns and seven- or eight-node cases remain outside this candidate. S3 explicitly says the F817 mixed-edge additions were not yet adopted at its recorded disposition; this document does not represent its own reconstruction as parent adoption.

## 8. Read declarations and method boundary

Let `R=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/` and let this wave be `R/review-waves/f839-septic-mixed-edge-half-gap-root-proof-author/`. Before opening a mathematical source body or reasoning on it, I read this wave's complete manifest, freeze receipt, final pre-dispatch binding, parent live metadata, **actual dispatch receipt**, and all 22 manifest-listed controls, as status/permissions only. Initial structured administrative displays elided JSON blocks; I reread each administrative file in complete raw form before the prebody acknowledgement. I created `prebody-ack-v1.md` and sent a **direct PREBODY ACK to Main**, both before reading the literal part. The owned directory was listed first and the new acknowledgement and candidate names were absent; the file-writing tool does not expose an atomic `O_EXCL` switch, so no independent atomic-exclusivity claim is made. The supplied conversation and general memory summary were visible; I do not claim a private-cognition or independent-provenance certificate.

The 22 status controls were the two `prospective-author-method-scope-restoration-20261030-v1.json` and `contract-addendum-2-frontier-first-owner-direction-v1.json`; the five parent L1/privacy/core-gram/AME-compression/PH-registration quarantine files; the `parent-selected-diagnostic-process-major-quarantine-v1.json` files in wave directories `f439-depolarizing-ancillary-all-dimensional-repair-written-review`, `f444-spr-full-seven-coefficient-enlargement-and-all-ray-review`, `f448-kac-actual-second-arm-exterior-module-and-character-review`, `f508-coherent-vacuum-w4-h2-channel-and-strictness-written-review`, `f513-boolean-five-span-physical-four-fibre-xor-obstruction-review`, `f586-semigroup-finite-pure-source-free-band-regularity-written-review`, `f602-olson-deficit-six-protected-triples-independent-actual-word-check`, `f653-sun8-psl2-small-exception-actual-cosets-written-review`, `f654-sun8-primepower-source-and-actual-normalcut-consumer-review`, `f659-fresh-original-input-sun8-source-and-normalcut-consumer-review`, `f660-fresh-original-input-sun8-exceptional-actual-coset-review`, and `f662-report-v23-werner-core-falsification-documentary-audit`; `review-waves/f596-actual-ame48-t24-entire-4555-same-tensor-frontier/parent-selected-instance-process-major-quarantine-v1.json`; and the two parent remaining-d0-occupancy and prerun-f746/f749 design-correction status files, all exactly as listed in the manifest. No control was used as a mathematical premise.

After the direct ACK and before reasoning, I read the **entire sole literal packet part**, serially in raw consecutive windows `1–20,21–40,...,501–520,521–532`, through its ending. Each display was below 30,000 bytes and at most 20 lines; no packet clipping was observed requiring recovery. The packet's parent-supplied SHA-256 is `202d2e3f0c2638fb412e07fb71f99ef58491e7f1aa4612c9e1e0ebf8034079f9` (73,704 bytes, 532 LF). It renders the complete bodies and parent-supplied original pins:

| ID | R-relative original body | complete LF | parent-supplied SHA-256 |
|---|---|---:|---|
| S1 | `review-waves/f817-septic-twelve-reverse-pattern-quintic-proof-author/author-candidate-v1.md` | 189 | `8d88c41020e504a278cf2c39c20c1455548e5155e7f5b0dad77f2132e5a01ad6` |
| S2 | `review-waves/f816-septic-determinant-minimal-atom-root-budget-proof-author/author-candidate-v1.md` | 227 | `4915f3cbc2994c8275c2fc5000d6ff443e719405fc09827220a26b6dbb567f6f` |
| S3 | `dispositions/info-2-septic-positive-determinant-minimal-atoms-root-budgets-and-twelve-patterns-parent-v1.md` | 31 | `be3e21d36784dd18d5a035557846bf300f886fb8c39d5fe3f283fb51b2f6ee22` |
| S4 | `dispositions/info-2-actual-septic-sparse-coupled-barycentric-and-six-node-frontier-parent-v1.md` | 33 | `32db73ad861d2fcafb8fda19efec027f3b957ed5878dc0ae78b8244bc5789549` |
| S5 | `dispositions/info-2-actual-septic-strict-band-quadrants-and-low-frequency-subcases-parent-v1.md` | 30 | `90ce201156b0ee89e5f09e2e6cf3c4fa9d7eb2c6178a02795c84d84dbd7fa9af` |

The parent receipt reports source roundtrip and binding checks; I did not independently open or hash the originals. All held episodes and every proof/method/selection/planning/verification/reporting/confidence/downstream consumer remained NONINPUT; no scientific link was followed. No sibling source, network, external model, code execution, scientific subprocess, test, compiler, solver, CAS, build, lint, formatter, Git operation, deletion, or scientific evaluation was used. No verifier code was requested or prepared, so there is no prepared-code hash. Parent whole-source read, independent checking, and any disposition remain separate.
