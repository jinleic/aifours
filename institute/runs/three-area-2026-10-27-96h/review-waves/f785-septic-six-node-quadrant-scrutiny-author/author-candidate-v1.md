# Six-node no-endpoint physical sign and quintic system: written author candidate

**Status.** GENERAL AUTHOR, nonblind and same-harness; written arguments below are unreviewed and not adopted. In addition to reconstructing the requested claims, §5 proves a 12-pattern necessary classification of the two reverse gaps and their *actual physical bands*, and §7 gives a per-corner quintic root-parity budget. Both are necessary conditions only. The exact eligible-box feasibility problem in §8 is still **open**: no six-node zero dual, counterexample, nonexistence theorem, global SPR/ROOT theorem, or novelty claim is asserted. Parent whole-read, independent checking and explicit disposition are separate. The native clock observed before composing this file was `2026-10-30T18:22:07-0700 PDT`; it is not asserted to be the creation or research-start time.

## 1. Object, tests, and imports

Fix any one nonempty compact **independent** real coefficient box K of monic septics, each of whose actual members is strictly Hurwitz. At t>0 write

\[
 E_a=a_0-a_2t+a_4t^2-a_6t^3,\qquad
 O_a=a_1-a_3t+a_5t^2-t^3,
\]
\[
 r_a(t)=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a).
\]

Let b and h be the coefficient center and halfwidths, and put `E_±=E_b±H_E`, `O_±=O_b±H_O`, with `H_E=h0+h2 t+h4 t²+h6 t³` and `H_O=h1+h3 t+h5 t²`. For each fixed t, independence makes the actual pairs exactly the rectangle `[E_-,E_+]×[O_-,O_+]`; its four vertices are values of four fixed actual parity corners. This does **not** say the whole coefficient box is the convex hull of four polynomials. Eligibility excludes `(0,0)` from every such rectangle.

Consider a nontrivial relation

\[
 \sum_j w_j r_{C_j}(t_j)+\lambda e_0+\mu e_7=0,
 \qquad t_j,w_j>0,\quad\lambda,\mu\ge0.\tag{1}
\]

The finite atoms are actual corners. Group equal finite frequencies as `0<u1<...<un`; `W_i>0` is their total weight and `(E_i,O_i)` is the pair of their **same** weighted-average actual member. Put `X_i=W_i E_i` and `Y_i=W_i u_i O_i`. A raw actual-member relation can also be expressed with physical corners at each frequency. At least one finite group occurs. Reading the eight coordinates gives

\[
 \sum X_i=-\lambda,\quad \sum X_i u_i^q=0\ (q=1,2,3),\qquad
 \sum Y_i u_i^q=0\ (q=0,1,2),\quad \sum Y_i u_i^3=\mu.\tag{2}
\]

**Exact imports and boundaries.** The band construction uses classical strict Hermite–Biehler interlacing for each actual Hurwitz septic; all remaining calculations below are written elementary interpolation, sign, continuity and degree arguments. The statement that *all* relations have at least six frequencies, including five-node relations with a nonzero endpoint, additionally imports the named at-most-five-distinct-positive-frequency **strict-negative** no-go on an eligible box: it is not proved here. The parent packet's at-most-eight-total-atom reduction is used only to discuss the sparse representation and its mixture budget. The same-box compact-zero-hull/strict-SPR equivalence and the actual-band/all-R4/both-R5/zero-odd/cancellation ROOT interface are **not** established by this return; no conclusion about a common monic Q, common margin, or ROOT is taken from them. The n=4 and endpoint-free n=5 exclusions below do not use the five-frequency import.

## 2. Both parity bands, moments, and the endpoint correction

Pair (1) separately against coefficient tests with even part `E_b`, odd part zero, and with even part zero, odd part `O_b`. Their endpoint coordinates are respectively `b0>0` and 1, so

\[
 \sum_i W_iE_iE_b(u_i)=-\lambda b_0,\qquad
 \sum_i W_i u_iO_iO_b(u_i)=-\mu.\tag{3}
\]

If the odd parity is fixed, the second left side is a sum of squares, forcing every `O_i=0` and `mu=0`; rectangle exclusion then makes every `E_i E_b(u_i)>0`, contradicting the first identity. The even-fixed case is symmetric. Thus any relation requires a positive-width coefficient interval in **each** parity. Also neither X nor Y is identically zero: if X vanished, (3)'s odd test is strictly positive because the odd interval avoids zero at each node; the other case is symmetric. Consequently `H_E,H_O>0` at every t>0.

For the actual center, strict Hermite–Biehler gives simple positive interlacing roots `e1<o1<e2<o2<e3<o3`. Varying only the even coefficients to their actual envelopes, while holding the odd center, gives one simple root of each even envelope in each `(0,o1)`, `(o1,o2)`, `(o2,o3)`; the envelope roots strictly straddle the corresponding `e_j`. The odd envelopes similarly have one root in each `(e1,e2)`, `(e2,e3)`, `(e3,∞)`, straddling `o_j`. Thus the zero-available sets are six nondegenerate closed intervals. If an even and odd interval met, even at an endpoint, the actual rectangle would contain `(0,0)`, contrary to Hurwitz eligibility. Their genuine strict order is

\[
 I^E_1<I^O_1<I^E_2<I^O_2<I^E_3<I^O_3.\tag{4}
\]

The parity's ordinary crossing directions in bands 1,2,3 are respectively down, up, down. Throughout E bands 1,2,3 the odd signs are `+,-,+`; throughout O bands 1,2,3 the even signs are `-,+,-`. These signs hold for every actual member, not just the center.

For either X or Y, delete zeros **only** for counting sign changes. Its first three appropriate moments in (2) give at least three changes: otherwise a degree-at-most-two polynomial with roots in its sign-change gaps makes all nonzero summands positive. If there are exactly three, a monic cubic with roots in the three gaps has pairing `mu` for Y, and `lambda` times the product of the three positive roots for X. In either case the final nonzero sign must be positive and the corresponding endpoint strictly positive. Hence endpoint weight zero forces at least four changes.

If one parity had no strict reverse pair in any of its actual bands, its sign word could only run through the ordered blocks `+,-,+,-`; it has at most three changes, ending negative if it has three. This contradicts the preceding paragraph. Therefore, in the **same** relation each parity has a strict reverse pair in one actual band: negative then positive in band 1 or 3, or positive then negative in band 2. The even and odd pairs are in disjoint bands.

At a downward band's left endpoint every actual value is nonnegative, and at its right endpoint every actual value is nonpositive, with signs reversed in an upward band. Because both strict reverse-pair nodes lie in the *same closed band* and are ordered, both are in its strict interior. A negative group necessarily has positive weight on a parity-lower physical corner, a positive group on a parity-upper corner; reverse this orientation as appropriate for an upward band. Opposite-parity signs are the strictly fixed signs above. This holds for mixed groups and does not imply a whole-box four-corner hull.

**Literal correction.** The endpoint assertion is local to the band and its immediately adjacent no-band components. The blanket wording in S3 §5 that all frequencies before the left endpoint, or all frequencies after the right endpoint, have the specified sign is false. For instance, `(R^E_2,L^E_3)` is a nonempty interval after the first even band where every even value is positive. The local endpoint fact suffices for strict interior; no global continuation of that sign is used.

## 3. Strict physical windows and the four- and five-node exclusions

Writing `L^E_j,R^E_j,L^O_j,R^O_j` for band endpoints, strict simultaneous quadrant availability, obtained by intersecting the two actual interval signs, is exactly

\[
\begin{array}{c|l}
(E,O)&\text{positive-frequency windows}\\\hline
(+,+)&(0,R^E_1)\ \cup\ (L^O_2,R^E_3)\\
(-,-)&(L^O_1,R^E_2)\ \cup\ (L^O_3,\infty)\\
(-,+)&(L^E_1,R^O_1)\ \cup\ (L^E_3,R^O_3)\\
(+,-)&(L^E_2,R^O_2).
\end{array}\tag{5}
\]

For example `(+,+)` requires and, by the actual rectangle, is equivalent to `E_+>0` and `O_+>0`. Thus the same-sign windows run `P1<N1<P2<N2`, and the opposite-sign windows run `A1<B<A2`. Each is an availability set, not a claim that every actual group occupies it; zero entries receive no strict sign.

For n=4, let `H_4(t)=∏(t-u_i)` and `P=∏u_i`. Vandermonde interpolation applied to (2) gives

\[
 X_i={\lambda P\over u_i H'_4(u_i)},\qquad Y_i={\mu\over H'_4(u_i)},
 \qquad\lambda,\mu>0.
\]

Indeed `Σ1/(u_iH'_4(u_i))=-1/P` and `Σu_i³/H'_4(u_i)=1`; nonzero X,Y force both endpoints positive. `H'_4(u_i)` has signs `-,+,-,+`, so the required quadrants are `(--),(++),(--),(++)`, which cannot occur in the physical window order. Thus n=4 is excluded even with both endpoint atoms.

For n=5 with `lambda=mu=0`, each sequence annihilates degrees 0–3; the one-dimensional Vandermonde nullspace yields `X_i=c/H'_5(u_i)`, `Y_i=d/H'_5(u_i)` with `cd!=0`. Both sequences alternate without zero. If `cd>0` this requires five alternating same-sign quadrants, but only four ordered same-sign windows exist. If `cd<0` it requires five alternating opposite-sign quadrants, but only three such ordered windows exist. Therefore endpoint-free n=5 is impossible. The remaining n=5 endpoint patterns are **not** excluded by this argument.

## 4. Six nodes, no endpoints: zeros, consecutive gaps, and sign(k)

Assume now `n=6` and `lambda=mu=0`, with no sparsity restriction yet. Each parity sequence has at least four sign changes. The two nodes of the odd reverse pair have the same strict even sign, and every intervening node is in the same odd band with that same even sign. Hence X has a repeated adjacent nonzero sign; similarly Y has one from the even pair. A length-at-most-six nonzero word with a repeat has at most four changes. Therefore X and Y have no zeros, exactly four changes each, and precisely one repeated adjacent sign each. Each reverse pair must consist of **consecutive nodes**, and no third node can lie in either reverse band; any other band of the same parity contains at most one node. The reverse pairs cannot share a node because their bands are disjoint, so their two gap indices differ by at least two. In each of the other three gaps both signs flip.

Put `H(t)=∏_{i=1}^6(t-u_i)`. Since each sequence has zero moments for degrees 0–3, the two-dimensional Vandermonde nullspace yields

\[
 X_i={c_E(u_i-\alpha)\over H'(u_i)},\qquad
 Y_i={c_O(u_i-\beta)\over H'(u_i)},\qquad c_Ec_O\ne0.\tag{6}
\]

To see this without dividing by any parity value, every sequence `D(u_i)/H'(u_i)` with `deg D<=1` annihilates those moments, and the nullity is two. The coefficient of t in each D is nonzero: otherwise its sign word alternates at every gap. Since the signs of `H'(u_i)` alternate, the unique repeated X sign puts `alpha` strictly inside the odd reverse-pair gap, and the unique repeated Y sign puts `beta` strictly inside the even reverse-pair gap. Thus `alpha,beta>0` are distinct, belong to different actual band interiors, and are not sample nodes.

With `k=c_O/c_E`, common weights give the **same-member** equation

\[
 u_iO_i(u_i-\alpha)=kE_i(u_i-\beta)\quad (1\le i\le6).\tag{7}
\]

At the later node of the even reverse pair, E and O have the same nonzero sign: `(+,+)` in even band 1 or 3, and `(-,-)` in band 2. Its `u_i-beta` is positive. Since the odd band lies wholly on one side of that even band, the sign of `u_i-alpha` is the sign of `beta-alpha`. Equation (7) therefore proves

\[
 \operatorname{sign}(k)=\operatorname{sign}(\beta-\alpha).\tag{8}
\]

This is a physical same-box conclusion, not a free-marker assumption.

## 5. A sharper physical-band classification of the two reverse gaps

The following is an additional written necessary condition; it does not assert that any row is physically or algebraically realizable.

Number the six physical bands in order

\[
 B_1=I^E_1,\ B_2=I^O_1,\ B_3=I^E_2,\ B_4=I^O_2,\ B_5=I^E_3,\ B_6=I^O_3.
\]

For a sample with both signs nonzero, assign an integer level `ell` as follows. Outside the bands it is the number of completed bands. Inside band `B_j`, it is `j-1` if the varying parity has its pre-crossing sign and `j` if it has its post-crossing sign. The associated strict quadrants at levels 0,…,6 are

\[
 (++),\ (-+),\ (--),\ (+-),\ (++),\ (-+),\ (--).\tag{9}
\]

Because the bands are disjoint, levels are nondecreasing between samples in different bands. A gap in which both signs flip cannot have both nodes in one band; its level increment is positive and congruent to 2 modulo 4, so it is at least 2. A strict reverse pair inside `B_j` has level decrement exactly 1. There are three double-flip gaps and two reverse gaps. Since all levels are in `[0,6]`, a double-flip increment of 6 or more would force the total increment to be at least `6+2+2-1-1=8`, impossible. Hence **each of the three double-flip gaps increments the level by exactly 2**, and `ell_6=ell_1+4` with `ell_1∈{0,1,2}`. In particular the first and last groups have the same strict quadrant, necessarily `++`, `-+`, or `--`; `+-` is impossible at either end.

Let the two reverse gaps be `p<q` among gaps 1,…,5. Let `r<s` be the corresponding physical band numbers, and set `a=p-1`, `b=q-p-1`, `c=5-q`. The pairs are disjoint, so `b>=1`, and `a+b+c=3`. The exact level increments imply

\[
 s=r+2b-1,\qquad r\ge 2a,\qquad s-1+2c\le6,\tag{10}
\]

where r and s have opposite parity. Conversely, solving just these **necessary integer constraints** gives precisely the 12 entries below. Each entry is `(r,s; ell_1; sign(k))`; an odd first band is even-parity and gives negative k, while an even first band is odd-parity and gives positive k.

| reverse gaps `(p,q)` | only allowed `(r,s; ell_1; sign(k))` |
|---|---|
| (1,3) | (1,2; 1; −), (2,3; 2; +) |
| (1,4) | (1,4; 1; −), (2,5; 2; +) |
| (1,5) | (1,6; 1; −) |
| (2,4) | (2,3; 0; +), (3,4; 1; −), (4,5; 2; +) |
| (2,5) | (2,5; 0; +), (3,6; 1; −) |
| (3,5) | (4,5; 0; +), (5,6; 1; −) |

For the table, `ell_1=r-2a`, and (8) supplies the sign of k. The short enumeration follows directly from (10), `1<=r<s<=6`, and opposite band parity; for instance `(p,q)=(1,5)` gives `b=3` and so `s-r=5`, forcing `(r,s)=(1,6)`. Conversely here means only that the displayed *integer* constraints are met; no realization of any table row by actual septics, actual weights or quintics follows.

## 6. Exact quintics, edge mixtures, and one positive weight scale

For each actual physical corner C set

\[
 P_C(t)=k(t-\beta)E_C(t)-t(t-\alpha)O_C(t).\tag{11}
\]

It is **monic of degree five**, since `O_C` has leading term `-t³` and the E contribution has degree at most four. A singleton group assigned to C has `P_C(u_i)=0`. For a genuine adjacent-edge group with the same coefficient `0<theta<1` in both parity coordinates, the condition is

\[
 \theta P_C(u_i)+(1-\theta)P_D(u_i)=0.\tag{12}
\]

For a strict edge mixture, the two P values must have opposite signs, or both must vanish. If exactly one is zero and the other is not, only an endpoint weight works and the group is a singleton, not a strict edge mixture.

The edge restriction entails no loss of aggregate or atom budget. The actual rectangle is full-dimensional because both parities vary. Given a nonzero grouped vector `v=(E_i,O_i)` and W, maximize `rho>=1` for which `rho v` remains in the rectangle. At the resulting boundary point take its at-most-two adjacent physical corner decomposition; scaling the total weight to `W/rho` preserves both `W E_i` and `W O_i`, hence all eight row coordinates. Leave existing singleton groups alone. A mixed original group used at least two atoms, so this never increases the finite count. For a chosen n=6, no-endpoint relation with at most eight finite atoms, at most two of the six compressed groups are genuine edge mixtures and at least four are singletons.

Crucially the two P equations alone are not a certificate. The **one common scalar** `c_E!=0` must yield

\[
 W_i={c_E(u_i-\alpha)\over E_i H'(u_i)}>0\quad(1\le i\le6),\tag{13}
\]

with the same chosen group `(E_i,O_i)` in (12), and `c_O=k c_E`. All divisions here are legitimate by §4. Conversely, if an eligible actual box, six ordered positive nodes, physical corner/edge selections, `alpha,beta,k,c_E`, (11)–(13), positive weights, and the mixture budget exist, then (6) holds for both sequences and Lagrange/Vandermonde annihilates all four moments. Splitting the group weights along their actual corner/edge choices gives the original eight-coordinate relation. Thus these are an **iff feasibility formulation** for the chosen sparse six-node/no-endpoint stratum, not a feasibility result.

## 7. New per-corner positive-root and parity budget

Let the odd reverse band be `I^O_j` and the even reverse band `I^E_l`. Because every physical corner has the same strictly nonzero complementary-parity signs at alpha and beta, (8) and (11) give, **for every corner C**,

\[
\begin{aligned}
 \operatorname{sgn}P_C(0)&=-\operatorname{sgn}k,\\
 \operatorname{sgn}P_C(\alpha)&=-\operatorname{sgn}E_C(\alpha)=(-1)^{j+1},\\
 \operatorname{sgn}P_C(\beta)&=-\operatorname{sgn}k\,\operatorname{sgn}O_C(\beta)=(-1)^l\operatorname{sgn}k,\\
 \operatorname{sgn}P_C(+\infty)&=+.
\end{aligned}\tag{14}
\]

In particular none of the four corner quintics vanishes at 0, alpha, or beta. Order these boundaries as `0<d1=min(alpha,beta)<d2=max(alpha,beta)<∞`. For a fixed C let `N_h` be the number of its **assigned singleton nodes** in the h-th open interval `(0,d1)`, `(d1,d2)`, `(d2,∞)`, respectively. Let `epsilon_h=0` if P_C has the same sign at the two boundary endpoints of that interval and `1` otherwise, using (14), and define `delta_h` as the element of `{0,1}` congruent to `epsilon_h-N_h (mod 2)`. Then necessarily

\[
 \sum_{h=1}^3(N_h+\delta_h)\le5.\tag{15}
\]

Proof: the total multiplicity of positive roots in each interval has parity `epsilon_h` by its two nonzero endpoint signs and is at least `N_h`. Therefore it is at least `N_h+delta_h`; their sum is bounded by the degree five. This remains valid if unassigned roots exist, roots have even multiplicity, or a different group is a mixed edge; (15) never counts an unproved root as a sampled singleton.

For example, if the odd reverse band is O1 and the later even reverse band is E3, then `alpha<beta`, `k>0`, and the four boundary signs in order are `-,+,-,+`. Thus **each** corner quintic must have at least one positive root in each of the three intervals. This is a root-existence consequence under the hypothetical relation, not a constructed dual. When `k<0`, `P_C(0)>0` and P_C is monic of odd degree; five distinct positive roots would force a negative constant term. Hence each corner has at most **four** distinct positive roots. In particular a sparse solution in that ordering cannot assign five singleton frequencies to the same corner. These checks can prune the 12 structural rows, but neither they nor the table resolve the coupled feasibility problem.

## 8. Exact unresolved gap and claims not made

The unpaid question is whether **any** eligible independent K and any of the 12 physical-band/gap patterns admit six ordered positive nodes, four or more singleton physical-corner groups and at most two positive adjacent-edge groups, distinct in-band alpha and beta, and common nonzero `k,c_E` satisfying (8), (11)–(13), all six positive weights, and the same-box strict eligibility for every member. The new root-parity budget (15) must also hold. Conversely, an explicit actual K and parameters satisfying these requirements would furnish an actual relation as shown in §6; an abstract sign word, separate E/O choices, individually stable corners, or cross-product zeros without positive common weights would not.

The wider n=6 nonzero-endpoint, n=7, and n=8 sparse cases are not solved here. General n>=6 still depends on the named strict-negative five-frequency import; no same-box weak-to-strict argument is used. Nothing here claims an actual witness, universal obstruction, universal common monic septic numerator, ROOT solution, novelty, or independent family/human/formal/kernel approval. No scientific program, numerical computation, solver, interpreter, test, build, lint, formatter, external-model CLI, network access, installation, Git operation or deletion was run. No source for later execution is proposed. SHA-256 and native-clock observations are administrative, not scientific computations.

## 9. Complete input, control and process coverage

Let `R=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`. After Main's direct confirmation of the actual dispatch receipt, I read that receipt, all 237 LF of the manifest, all 221 LF of the freeze receipt, all 193 LF of the final binding, all 234 LF of the prepared metadata, and every one of the 22 listed controls through its ending as status/permission controls only. I sent Main the required direct **PREBODY ACK** naming 22 controls and ordered part LF counts `[668]`, explicitly stating no packet body, math or comparison yet. I then read the only packet part serially in consecutive raw windows of at most 20 LF, from LF1 through LF668 and its ending, before mathematical work. No packet sequence or presentation failure occurred. All genuinely held episodes and every proof/method/selection/planning/verification/reporting/confidence/downstream consumer remained NONINPUT; no outgoing scientific link, old code, held history, or unspecified scientific source was opened. No private-cognition certificate is claimed.

The six complete source bodies, read only in that rendered packet, are listed below with parent-frozen source SHA-256 pins. Source original files were not separately opened or independently re-rendered. Parent freeze metadata reports complete source roundtrip and persisted-packet equality; the hashes are provenance, not independent source identity or correctness certification.

| ID and R-relative source path | original complete LF | SHA-256 |
|---|---:|---|
| S1 `review-waves/f759-septic-strict-interior-quadrant-refinement-proof-author/independent-reconstruction-v1.txt` | 157 | `2d253d660505dcdd30d29f94c95eb98da33012477f6d042f48ea792213928ca7` |
| S2 `review-waves/f760-septic-six-eight-frequency-coupled-frontier-author/author-coupled-frontier-v1.md` | 165 | `b5a248e86c2cda695851752fd8f364c5644d028c1b9daa343729ef91a67d505a` |
| S3 `review-waves/f742-septic-two-parity-physical-backtracking-proof-author/author-reconstruction-v1.md` | 247 | `9cb4340f358000e00cdbb0b83a287e171e140143de9ed7aacd78d1f5a34f3b87` |
| S4 `dispositions/info-2-actual-septic-eight-atom-zero-dual-six-frequency-and-parity-backtracking-parent-v1.md` | 39 | `866dd92b58bb2422281abe815bc1e6cae8e5f8f94c96f2d7eaed00bad372a183` |
| S5 `dispositions/info-2-actual-both-parity-septic-four-corner-sdp-and-zero-dual-parent-v1.md` | 29 | `949af8c879058b8be166086ab06dbba03d896a26adc64e1621dfbdf7a72e4d0b` |
| S6 `dispositions/info-2-actual-both-parity-septic-four-corner-sdp-and-zero-dual-parent-v1-erratum-1.md` | 5 | `513b44b2591954b535e138df611fab0698af2b8363b89768a5e45f320d50f5d4` |

After the complete packet read, administrative `shasum -a 256` observations for the live wave files were: manifest `59c3401f4626eb096237f59cf66acb4f975a04cccb820e67c0265972a5f5bc78`; freeze `2cd31598a7193548ccfac22a17fe25696b4051d8c556c3af493175086cb4f036`; final binding `6e874e04445a7073c33fca7b8478694f05ac1b5d2f776939c1cdae1e56f170c1`; prepared metadata `8f309cfcf43dcfb86be9df29175e31cf7ec95232f115957d75494063c934eec1`; actual dispatch `0ca5c3c75211cbb12cc73e5f00b58e60a155ad9687887c642af00588f99c04f5`; packet `6fb09e68d723dfa0996a6611289aef07469852eb59ea5adf6b8c514f4d35e059`. The manifest/receipt/binding declared packet and source pins agree with the corresponding metadata; the packet digest was separately observed, not its original source reconstruction.

All 22 controls below were read through their endings and, **after** the packet pass, their live administrative SHA-256 values were observed and matched the frozen manifest. Paths are relative to R. Entries abbreviated as `review-waves/<directory>/<filename>` are exact, not links followed beyond the listed control.

| Control path | SHA-256 |
|---|---|
| `prospective-author-method-scope-restoration-20261030-v1.json` | `6ab69778c11dbfc4ac895f97b381cc70d0059a5723d6b02f62b9957c7e8dcd95` |
| `contract-addendum-2-frontier-first-owner-direction-v1.json` | `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce` |
| `parent-L1-selected-diagnostic-release-quarantine-v1.json` | `ba6b4bb953e9ee20c57c4ae84b85dadbc66e26f8e800089f5176b2582a13555f` |
| `parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json` | `e4d6f1e49cb18aced7735cf025dee54830400554c9adc08138250ae9f0523efc` |
| `parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json` | `23fa29449cef8e02d981efc021934e4cec16960ca6bfe8f6f2178bbd048c85b4` |
| `parent-ame-held-compression-claim-consumer-quarantine-v1.json` | `c307e902eee5f3736aab0e2437738898382b3d3083f6c307118219b9a4c875b0` |
| `parent-held-ph-registration-report-consumer-quarantine-v1.json` | `97fbd5967b472783c5ed860f0745b88d7917eb93e1c340f043c974a531ac1453` |
| `review-waves/f439-depolarizing-ancillary-all-dimensional-repair-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `74f9f9d57eb5866f68dec331b9bf4facca2bc8d4116186cd241b3bff1539dfee` |
| `review-waves/f444-spr-full-seven-coefficient-enlargement-and-all-ray-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `d00f41bf0205680ef8256f38c97d2023058da935c260ba5cc7f17cb77bd8e184` |
| `review-waves/f448-kac-actual-second-arm-exterior-module-and-character-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `f6ccc5fa10f0e30536921ea86828c437359869413919eae258cbbd82d4989805` |
| `review-waves/f508-coherent-vacuum-w4-h2-channel-and-strictness-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `649349cfe636c88e60bee96400512ae6db8d8e12b875d3d100fcce3312785fd8` |
| `review-waves/f513-boolean-five-span-physical-four-fibre-xor-obstruction-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `cb9a81b76acaf740e2d691664e57e46a274c208f44fb071f5f0724973ae1a1a8` |
| `review-waves/f586-semigroup-finite-pure-source-free-band-regularity-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `e4d3dca7c41456e4e48dc154719b1df9e653b656b2cbf9324c82b195e3539681` |
| `review-waves/f602-olson-deficit-six-protected-triples-independent-actual-word-check/parent-selected-diagnostic-process-major-quarantine-v1.json` | `df412094a47e89be2507d7a7809d68449f08476aabfaca44fd9ecb4dce2a40b8` |
| `review-waves/f596-actual-ame48-t24-entire-4555-same-tensor-frontier/parent-selected-instance-process-major-quarantine-v1.json` | `3f4b2c6d31a420ecff35a6478ce7a302637765b1203c046619715eda634b6927` |
| `review-waves/f653-sun8-psl2-small-exception-actual-cosets-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `a85930a9b268d472d5ded2f31b4b9916394e99f97e854c3a3869a9c8fd7ec8de` |
| `review-waves/f654-sun8-primepower-source-and-actual-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `9aaf84aabb3ea428e3622c5e6b7961d21bd3f1a8b3a16a727be203077e784462` |
| `review-waves/f659-fresh-original-input-sun8-source-and-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `abf867950e1425ed74e1a766f6838957b255694cf0f64e936a23321c1324913b` |
| `review-waves/f660-fresh-original-input-sun8-exceptional-actual-coset-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `f5007a354d6acb8335ad2b9cc170f457c542640e1bbd15c5439d69d0c76039ab` |
| `review-waves/f662-report-v23-werner-core-falsification-documentary-audit/parent-selected-diagnostic-process-major-quarantine-v1.json` | `7dc07513bb05a7b08ba9795b566f38c39750a8f71fc68d576ea4367d4b0e4c38` |
| `parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json` | `8a98f416ed19f9d838eb286d1de32cd9508e33324fe44b2593dd3663c9b2c70c` |
| `parent-prerun-f746-matching-and-f749-occupancy-design-corrections-v1.json` | `27390c73fd6741217ce1d86c5f41e388ef87e3f51b306565053943e0333afbce` |
