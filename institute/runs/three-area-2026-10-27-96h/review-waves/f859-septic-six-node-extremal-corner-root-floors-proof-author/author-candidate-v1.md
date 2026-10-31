# F859: independent actual-corner root floors and saturated exclusions

**Status.** Nonblind prospective GENERAL AUTHOR written reconstruction of the additional claims in packet S1/F839, conditional on the actual physical-band interface explicitly named below. It is not a review-family, human, formal/kernel or parent acceptance. The conclusions are necessary conditions for one actual six-node/no-endpoint relation; they neither construct a relation nor close any of the twelve rows. In particular, no at-most-five-frequency import or global SPR/ROOT statement is used.

## 1. Quantifiers, actual box, and the conditional interface

Fix an arbitrary **one** nonempty compact independent coefficient box `K` of monic real septics, every actual member strictly Hurwitz. For an actual member `f`, put

\[
 E_f(t)=a_0-a_2t+a_4t^2-a_6t^3,\quad
 O_f(t)=a_1-a_3t+a_5t^2-t^3,\quad
 f(i\sqrt t)=E_f(t)+i\sqrt t\,O_f(t).
\]

At each positive `t`, coefficient independence gives the **actual same-member pair set**
`R(t)=[E_-(t),E_+(t)]×[O_-(t),O_+(t)]`. Write `E_±=E_b±H_E` and `O_±=O_b±H_O`. The endpoint values at all positive `t` are furnished by four fixed actual parity-corner polynomials `C_{στ}`, `σ,τ∈{+,-}`; this pointwise rectangle is not a claim that the entire coefficient box is the convex hull of four polynomials. Since a member with `(E,O)=(0,0)` would have an imaginary-axis root, `(0,0)∉R(t)`.

Consider an arbitrary nontrivial actual positive-weight zero relation, with exactly six **distinct finite positive** frequencies `0<u_1<⋯<u_6` and no endpoint atoms. Group all terms at each frequency; `W_i>0` is their total weight and `(E_i,O_i)` is their one common weighted-average pair. It lies in the actual rectangle, and the same group weights are used for both parities. Set `X_i=W_iE_i`, `Y_i=W_i u_iO_i`. The actual eight-coordinate zero relation is exactly

\[
 \sum_i u_i^q X_i=\sum_i u_i^q Y_i=0\qquad(q=0,1,2,3). \tag{1}
\]

**Load-bearing conditional import, not an unopened proof.** We use strict Hermite–Biehler interlacing for each actual strictly Hurwitz septic and the actual physical rectangle/band interface stated in packet S4–S6. With both parity widths nondegenerate, the six closed envelope-root bands are strictly separated and ordered

\[
 B_1=I^E_1<B_2=I^O_1<B_3=I^E_2<B_4=I^O_2<B_5=I^E_3<B_6=I^O_3. \tag{2}
\]

In `I^E_l` the complementary O sign is `(-1)^{l-1}`; in `I^O_j` the complementary E sign is `(-1)^j`. In the interior of the relevant band the varying envelope strictly straddles zero, while its endpoints have their actual one-sided signs. A strict sign word with no reverse-sign pair in a parity's own band follows the ordinary `+,-,+,-` progression. Across *other* bands we do not assert a fixed envelope sign. The underlying full proof bodies linked by the dispositions were not supplied as bodies to this wave and remain named conditional imports, not silently reconstructed here.

Both parity widths are in fact strictly positive at every `t>0`. If E is coefficientwise fixed, pairing the four E moment equations in (1) with its coefficients gives `Σ_i W_i E_i²=0`, hence every `E_i=0`. Origin exclusion then makes each entire O interval avoid zero, so `O_i O_b(u_i)>0` for every i, contrary to the O moment equations paired with `O_b`: `Σ_i W_i u_i O_i O_b(u_i)=0`. If O is fixed, the analogous pairing gives `Σ_i W_i u_iO_i²=0`, then `E_i E_b(u_i)>0` at every node, contrary to the E-center pairing. Consequently each parity has at least one nondegenerate coefficient interval. Each half-width is a sum of nonnegative coefficient half-widths times strictly positive powers of `t`, so `H_E(t),H_O(t)>0` for all `t>0`, even when individual coefficient intervals are degenerate. The same rectangle-exclusion and center-pairing argument shows neither `X` nor `Y` is identically zero.

## 2. Deriving the two actual markers and the twelve rows

For each nonzero sequence in (1), deleting zeros only while counting, there are at least four sign changes. Otherwise multiply its entries by an oriented polynomial of degree at most three with one simple root in each sign-change gap; the sum is strictly one-signed, contradicting (1). The imported local physical geometry then forces one strict reverse pair in an E band and one in an O band. The two actual bands are disjoint; a reverse pair is strictly interior, because at a band endpoint its varying coordinate has only the one-sided sign.

The E values are strictly the same sign throughout the odd reverse band, so its pair forces a repeat in the nonzero `X` word. Four changes and a repeat among at most six entries require exactly six nonzero entries, exactly four changes and one repeat. Thus the odd pair occupies consecutive nodes and has no third node in its band. Applying the same argument to `Y` using the E reverse band proves the symmetric conclusion. Every one of the twelve grouped parity values is therefore nonzero; the two consecutive reverse gaps `p<q` are disjoint, `q≥p+2`, and the other three gaps flip both parity signs.

Let `H(t)=∏_{i=1}^6(t-u_i)`. The four-moment Vandermonde nullspace has dimension two, with basis `1/H'(u_i), u_i/H'(u_i)`, since `Σ_i u_i^m/H'(u_i)=0` for `m≤4`. A constant numerator would alternate at all six nodes and give five changes. Thus there are nonzero `c_E,c_O` and real markers `α,β` with

\[
 X_i=\frac{c_E(u_i-\alpha)}{H'(u_i)},\qquad
 Y_i=\frac{c_O(u_i-\beta)}{H'(u_i)},\qquad k=\frac{c_O}{c_E}\ne0. \tag{3}
\]

The alternating signs of `H'(u_i)` place `α` strictly in the O reverse gap and `β` strictly in the E reverse gap. In particular both markers are positive, distinct and not samples. Because one shared `W_i` couples the two coordinates,

\[
 u_iO_i(u_i-\alpha)=kE_i(u_i-\beta). \tag{4}
\]

At the **later** node of the E reverse pair, the actual E and O signs agree and `u_i>β`. The entire O band is on one side of the E band; thus `sgn(u_i-α)=sgn(β-α)`. Equation (4) gives the essential physical orientation

\[
 \operatorname{sgn}k=\operatorname{sgn}(\beta-\alpha). \tag{5}
\]

For completeness, the twelve rows can be recovered without assigning arbitrary marker patterns. Give the ordered physical strict quadrants levels 0 through 6:

\[
 (++),(-+),(--),(+-),(++),(-+),(--).
\]

Each reverse gap lowers the level by 1, while every double-flip gap raises it by `2 mod 4` and at least 2. There are three double flips; a jump of 6 or more would make the total increase exceed the range 0–6, so all are `+2`. If the reverse bands have indices `r<s`, set `a=p-1`, `b=q-p-1≥1`, `c=5-q`. Then

\[
 s=r+2b-1,\qquad r\ge2a,\qquad s-1+2c\le6,\qquad \ell_1=r-2a. \tag{6}
\]

The possible `r` lists for `(p,q)=(1,3),(1,4),(1,5),(2,4),(2,5),(3,5)` are respectively `{1,2},{1,2},{1},{2,3,4},{2,3},{4,5}`. Here `s` is fixed by (6), lies in 1–6 and has parity opposite to `r`. These are necessary integer solutions, not physical realizability assertions. The six-level word for a row starts at `ℓ_1` and adds `−1` in gaps p,q and `+2` in the others.

## 3. Actual quintics, shared mixture, and boundary signs

For every one of the four fixed actual corners `C=C_{στ}`, define

\[
 P_C(t)=k(t-\beta)E_C(t)-t(t-\alpha)O_C(t)
       =a(t)E_C(t)+b(t)O_C(t),\quad
 a=k(t-\beta),\quad b=-t(t-\alpha). \tag{7}
\]

The polynomial is monic of exact degree five, because `O_C` has leading term `−t³` and `E_C` has degree at most three. At each actual node, (4) is `a(u_i)E_i+b(u_i)O_i=0`. A group that is a strict edge mixture of corners C,D uses the **same** `θ∈(0,1)` in both parity coordinates and satisfies

\[
 \theta P_C(u_i)+(1-\theta)P_D(u_i)=0. \tag{8}
\]

For an actual arbitrary positive mixture the same statement holds with its actual common weights; no mixed group is replaced by a fictitious singleton. For any selected actual pairs the same nonzero global scale must also satisfy

\[
 W_i=\frac{c_E(u_i-\alpha)}{E_iH'(u_i)}>0\quad(1\le i\le6),\qquad c_O=kc_E. \tag{9}
\]

Conversely, an eligible actual box, ordered nodes, actual pairs, marker placements, common k and `c_E`, equations (7)–(9), and all six positive weights give (3), hence (1) by the stated Vandermonde identities. Any separate atom or endpoint budget must be imposed separately.

If `α∈I^O_j` and `β∈I^E_l`, the signs at the four boundary probes are the same for **each** actual corner:

\[
 \operatorname{sgn}P_C(0)=-\operatorname{sgn}k,\quad
 \operatorname{sgn}P_C(\alpha)=(-1)^{j+1},\quad
 \operatorname{sgn}P_C(\beta)=(-1)^l\operatorname{sgn}k,\quad
 \operatorname{sgn}P_C(+\infty)=+. \tag{10}
\]

Indeed `E_C(0)>0`, `k(α−β)<0`, and the complementary parity signs in the marker bands are strict. Thus 0, α and β are never roots. For `k<0`, positive-root multiplicity is even and at most four; for `k>0` it is odd and at most five.

## 4. Adjacent-corner no-common-root and exact diagonal alternatives

For every `t>0`, using the actual widths of **the same box**,

\[
 P_{+\tau}-P_{-\tau}=2aH_E,\qquad
 P_{\sigma+}-P_{\sigma-}=2bH_O. \tag{11}
\]

An E-adjacent pair can agree only at `t=β`; an O-adjacent pair can agree only at `t=α`. Formula (10) makes all corner values nonzero at both markers. Thus no adjacent physical corner quintics have a common positive root, **including** α and β. At a strictly mixed adjacent edge, (8) then forces the two endpoint values to be nonzero with opposite signs, and its unique shared mixing coefficient is `θ=P_D/(P_D−P_C)`; the actual atom weights are `W_iθ` and `W_i(1−θ)`, both positive.

For diagonals put `P_b=aE_b+bO_b`. Directly adding and subtracting gives the exact exhaustive alternatives

\[
 \begin{aligned}
 P_{++}=P_{--}=0&\iff P_b=0,\quad aH_E+bH_O=0,\\
 P_{+-}=P_{-+}=0&\iff P_b=0,\quad aH_E-bH_O=0.
 \end{aligned} \tag{12}
\]

At α or β neither alternative occurs. Away from the markers, positive widths imply that if a,b have equal signs only the `(+-, -+)` diagonal can satisfy its width equation, and if their signs differ only `(++, --)` can. The complete interval restrictions are

| sign k | interval 1 | interval 2 | interval 3 |
|---|---|---|---|
| − | `(+-, -+)` | `(++, --)` | `(+-, -+)` |
| + | `(++, --)` | `(+-, -+)` | `(++, --)` |

This table gives only a **possible** diagonal, subject to both equations (12), not its realization. The other two corners are nonzero by (11), so no three actual corner quintics have a common positive root. A diagonal both-zero event is not a pair of selected singleton groups.

## 5. All-node extremal filter and all twelve explicit floors

Let `d_1=min(α,β)`, `d_2=max(α,β)`, and number the open intervals `(0,d_1),(d_1,d_2),(d_2,∞)` by h=1,2,3. In each interval a and b are nonzero with fixed signs. Since both widths are positive, the functional `aE+bO` on the actual rectangle has a unique maximizing vertex `M_h` and a unique minimizing vertex `m_h`:

| sign k | h | `M_h` | `m_h` |
|---|---:|---|---|
| − | 1 | `++` | `--` |
| − | 2 | `-+` | `+-` |
| − | 3 | `--` | `++` |
| + | 1 | `-+` | `+-` |
| + | 2 | `--` | `++` |
| + | 3 | `+-` | `-+` |

For **every actual grouped pair** at **every** node `u_i` in interval h, the same-pair zero equation and extremality give

\[
 P_{M_h}(u_i)\ge0,\qquad P_{m_h}(u_i)\le0. \tag{13}
\]

Equality in either inequality forces the averaged pair to be exactly that unique extremal rectangle vertex. Indeed equality in a convex combination of values bounded by a unique extremal value forces every positive-weight pair to equal that vertex. Thus a genuine group containing two distinct pair values gives strict inequalities. This conclusion does not require that any corner was selected.

Every one of the three intervals contains at least one node: the counts are `n=(p,q-p,6-q)`. If the two nonzero boundary signs in an interval are both positive, `P_{m_h}` is nonpositive at a node and has at least two root multiplicities in that interval. If they are both negative, the analogous statement holds for `P_{M_h}`. A zero sample is included: even parity then costs at least two, whether via a double root or another root. If the node value has the opposite strict sign, continuity gives distinct roots on its two sides.

The following table independently applies (10), (13), and the extremum table to **every** integer row. `ε` records boundary sign changes in the three intervals, and `h:C` means that actual corner C has at least two positive-root multiplicities in interval h. An entry `none` means only that this same-sign-boundary argument supplies no 2-floor there.

| `(p,q;r,s)` | `ℓ_1` | `sgn k` | node counts n | signs at `0,d_1,d_2,∞` | `ε` | all-node 2-floors |
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

For explicit compatibility with the packet's mixed-edge budget, let `n_{C,h}` count all distinct actual sampled zeros of `P_C` in interval h, regardless of selection, and let `g_{C,h}` count any certified open node-to-own-marker half-gaps whose endpoint signs force a zero. The two half-gaps per reverse pair are disjoint, the pair gaps themselves are disjoint, and no half-gap contains a sample, so all these witnesses are distinct. Put `q_{C,h}=n_{C,h}+g_{C,h}`, and let `F_{C,h}=2` for an entry in the last table column and 0 otherwise. Then the safe combined necessary inequality, for **each** actual corner, is

\[
 \sum_{h=1}^3\max\{q_{C,h}+[\epsilon_h-q_{C,h}]_2,\;F_{C,h}\}\le5. \tag{14}
\]

Here `[\cdot]_2` is 0 or 1. Each term is a lower bound on the same interval's total root multiplicity; taking the maximum, not their sum, avoids double counting. Actual mixed-edge signs and any both-zero **diagonal** give legitimate witnesses, but no separate E/O mixtures or fictitious singletons are permitted.

## 6. Three saturation cases, including multiple and negative roots

All assertions here are conditional on the same actual six-node relation. For k<0 each corner has at most four positive-root multiplicities, by its positive signs at 0 and +∞. Moreover its monic quintic tends to `−∞` at `−∞` and has `P_C(0)>0`, so at least one negative real root exists. If four positive multiplicities have already been accounted for, that negative root is the sole remaining root and is simple.

1. **`(1,4;1,4)`.** Here the common boundary signs are `++-+` and `P_{--}(u_1)≤0`. The first interval costs at least two positive-root multiplicities; the second and third cost at least one each. Hence `P_{--}` has exactly `(2,1,1)` positive multiplicities in the three intervals and one negative simple root. If `P_{--}(u_1)<0`, the two first-interval roots lie strictly on opposite sides of `u_1` and are simple. If it is zero, the exact two multiplicities are either a double root there or a simple root there plus one further simple root in the interval. Equality forces the grouped pair at `u_1` to be exactly the `--` vertex; it does not turn an arbitrary group into a singleton by assumption.

2. **`(2,5;3,6)`.** The boundary signs are `+-++` and `P_{++}(u_6)≤0`. The first and second intervals cost one each and the third costs two, so `P_{++}` has exactly `(1,1,2)` positive multiplicities and one negative simple root. If `P_{++}(u_6)<0`, the third-interval roots are simple and lie on opposite sides of `u_6`; if it is zero, they form a double root at that node or a simple node root plus another simple root. Equality forces the actual grouped pair there to be the `++` vertex.

3. **`(2,4;3,4)`.** Here `0<u_1<u_2<β<u_3<u_4<α<u_5<u_6`, `k<0`, and every corner has signs `+--+` at `0,β,α,∞`. In the middle interval the maximum corner is `-+`, so `P_{-+}(u_3),P_{-+}(u_4)≥0`. As `P_{-+}(β),P_{-+}(α)<0`, there is a root in `(β,u_3]` and a distinct root in `[u_4,α)`. Each outer interval also has an odd, hence at least one, positive-root multiplicity. These give four **distinct** positive roots; the four-root upper bound makes all simple and precludes all other positive roots. The remaining root is negative and simple. It also follows that `P_{-+}(t)>0` for all `u_3<t<u_4`: the only middle roots lie in the two just-displayed disjoint half intervals, and the sign after the first is positive. If either displayed node value is zero, that actual grouped pair equals the `-+` vertex; a genuine distinct-pair mixture there is impossible.

## 7. Both broader `(2,4;3,4)` corner-zero support exclusions

Keep precisely the actual row and order in case 3 above. No atom limit, edge assignment or singleton condition is assumed in either assertion.

**A.** It is impossible that
\[
 P_{--}(u_1)=P_{--}(u_3)=P_{--}(u_6)=0. \tag{15}
\]
At `u_5` the interval-3 maximum is `--`, so (13) gives `P_{--}(u_5)≥0` for the actual group, whatever its support. If this is positive, `P_{--}(α)<0` forces a root in `(α,u_5)`; if zero, `u_5` is itself a root. In both cases it is distinct from the root at `u_6`. The first interval has odd boundary parity and at least the root `u_1`, costing ≥1; the middle has equal negative boundary signs and `u_3` as a root, costing ≥2; the last has odd boundary parity and at least two distinct roots, costing ≥3. Total ≥6 contradicts degree five.

**B.** It is impossible that
\[
 P_{++}(u_1)=P_{++}(u_4)=P_{++}(u_6)=0. \tag{16}
\]
At `u_2` the interval-1 maximum is `++`, so `P_{++}(u_2)≥0`. A strict positive value and `P_{++}(β)<0` force a root in `(u_2,β)`; equality gives a root at `u_2`. Either root is distinct from `u_1`. The positive multiplicity costs are now at least 3,2,1 in the three intervals, again impossible for a quintic.

These are corner-**zero** exclusions even when the displayed corner is not used at a displayed node. In particular A excludes singleton `--` groups at `u_1,u_3,u_6` regardless of what is used at `u_5`, and B excludes singleton `++` groups at `u_1,u_4,u_6` regardless of what is used at `u_2`. They include the narrower S2/S3 strict-edge examples, but do not eliminate other support patterns or the whole row. Equality in the extremal inequalities is explicitly retained, and all actual group pairs and positive global weights remain shared as in (4), (8), (9).

## 8. Precise residual and read/method declaration

The unsolved residual for every row still quantifies jointly over one compact independent all-member-Hurwitz actual K; six ordered nodes and the actual physical bands; two marker locations in the two reverse gaps; actual common-pair groups, their weights, one k and one `c_E`; the simultaneous positivity constraints (9); and whatever actual endpoint/atom budget is prescribed for the chosen representation. Neither the tables, root floors, nor these two exclusions assert a feasible box or give a global row no-go. Other endpoint patterns, seven/eight-node cases, an eligible zero dual, the all-box common numerator, global SPR/ROOT, source identity, publication priority and novelty are not settled. The earlier ≤5-frequency theorem, eligible enlargement, sparse-eight compactification and zero-hull/SPR duality are **not** imported into this fixed six-node/no-endpoint result.

Let `R=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`, and let the owned wave be `R/review-waves/f859-septic-six-node-extremal-corner-root-floors-proof-author/`. Before any mathematical body read or mathematical reasoning, I read through the complete manifest, freeze receipt, final pre-dispatch binding, parent live metadata and actual dispatch receipt, and all 22 listed controls as **status/permissions only**. Initial nonraw JSON displays collapsed blocks; I recovered them by reading all five administrative JSON files completely in raw form before the ACK. The 22 controls were the two prospective-author-method and owner-addendum-2 files; the five parent L1/privacy/core-gram/AME-compression/PH-registration controls; the `parent-selected-diagnostic-process-major-quarantine-v1.json` files in wave directories f439, f444, f448, f508, f513, f586, f602, f653, f654, f659, f660 and f662 as fully named in the manifest; the f596 `parent-selected-instance-process-major-quarantine-v1.json`; and the parent remaining-d0-occupancy and prerun-f746/f749 design-correction status controls. None is a mathematical input. I wrote `prebody-ack-v1.md` and sent Main a direct prebody acknowledgement before any packet body read. The owned directory was listed before the ACK; neither acknowledgement nor candidate existed in that listing. The write tool provides no atomic `O_EXCL` option, so I do not claim independently verified atomic exclusivity.

After that direct ACK and before reasoning, I read the entire sole literal packet serially in consecutive raw windows `1–20,21–40,…,561–580,581–585`, including the ending. Every display was under 30,000 bytes and at most 20 LF. No clipping was observed in these packet windows; no clipping recovery was needed. The packet's **parent-supplied**, not independently rehashed, pin is `3ed5c1793bbf85d33b3450f400bc21ba218b3a362dac322160d2811dfb8f92ec` (83,737 bytes, 585 LF). It renders these complete bodies, also with parent-supplied pins:

| ID | R-relative original body | complete LF | parent-supplied SHA-256 |
|---|---|---:|---|
| S1 | `review-waves/f839-septic-mixed-edge-half-gap-root-proof-author/author-candidate-v1.md` | 252 | `9cae58609a5af7aecdaefe4cf416c186a07cbb693545b233fd8ca07009c4a879` |
| S2 | `dispositions/info-2-actual-septic-five-node-endpoints-and-six-node-mixed-edge-gap-parent-v1.md` | 24 | `66aa98e3a42b337e781a5f95521efc7e4eff51afe850d6939d80913edc11d741` |
| S3 | `review-waves/f817-septic-twelve-reverse-pattern-quintic-proof-author/author-candidate-v1.md` | 189 | `8d88c41020e504a278cf2c39c20c1455548e5155e7f5b0dad77f2132e5a01ad6` |
| S4 | `dispositions/info-2-septic-positive-determinant-minimal-atoms-root-budgets-and-twelve-patterns-parent-v1.md` | 31 | `be3e21d36784dd18d5a035557846bf300f886fb8c39d5fe3f283fb51b2f6ee22` |
| S5 | `dispositions/info-2-actual-septic-sparse-coupled-barycentric-and-six-node-frontier-parent-v1.md` | 33 | `32db73ad861d2fcafb8fda19efec027f3b957ed5878dc0ae78b8244bc5789549` |
| S6 | `dispositions/info-2-actual-septic-strict-band-quadrants-and-low-frequency-subcases-parent-v1.md` | 30 | `90ce201156b0ee89e5f09e2e6cf3c4fa9d7eb2c6178a02795c84d84dbd7fa9af` |

The receipt reports roundtrip and parent binding checks; I did not independently open, re-render, hash or authenticate the originals. All genuine held episodes and all their proof/method/selection/planning/verification/reporting/confidence/downstream consumers were NONINPUT; no unlisted scientific link or sibling body was opened. No network, external model, scientific code execution, subprocess, test, compilation, solver, CAS, scientific evaluation, build, lint, formatter, Git operation or deletion was used. No verifier code was assigned or prepared, so there is no prepared-code hash. Supplied conversation and general memory summary were visible; no private-cognition or prior-provenance certificate is claimed. Parent full-source reading, independent checking and any disposition are separate.
