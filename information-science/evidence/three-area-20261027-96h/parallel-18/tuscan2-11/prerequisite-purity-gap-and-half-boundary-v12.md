# Definition-first common selection XII: purity greater than n−1 already forces an original array; the critical nonrounded boundary has four half-rows

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 15:42:06 PDT 2026**.

**NEW author-WRITTEN, unreviewed global actual-row rounding theorem.** This improves v7's sufficient purity threshold without a maximal-overlap, support or chosen-instance assumption. At original order11, ANY feasible whole-row mixture with squared-weight sum GREATER THAN10 yields an actual original T2(11). No such mixture is supplied or claimed to exist. The equality case is classified rather than silently rounded.

## 0. Disjoint inputs and permanent process boundary

This continues ONLY the already admitted Tuscan S1/S2 literal packet SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c` (complete LF1-37), elementary nonnegative-weight/event counting and uniqueness of an actual linear Hamilton row from its adjacent pairs. The pre-existing Tuscan v6/v7 models are restated completely below; their prior verdicts are not a premise.

The w38 Olson review is STOPPED with a permanent distinct PROCESS MAJOR, disclosed at native15:39:25 and pinned/reported15:39:51. Its ENTIRE selected episode, partial mathematical assessment and consuming verdict/confidence/method/source guidance remain HELD/ZERO/NONINPUT. Main read the complete32-LF process report and permitted only genuinely disjoint already admitted Tuscan inputs. No group, field, polynomial, carry, digit, zero-count or selected-control material from w38 (or w29/w10) is used here. The whole-row purity branch and its mathematical inputs predate w38; this is not a claim of clean cognition or retrospective cure.

The proof below uses only real nonnegative weights, actual row event caps and elementary finite sets. No interpreter/calculator/Eval/CAS/program, enumeration/generation of row states, selected numerical/control/boundary probe, solver, modelCLI or new GO. The half-weight boundary is forced by the ALL-variable equality proof, not a selected test.

## 1. Exact whole-row setting and elementary facts

Let n≥3, X an n-symbol set, and Ω the set of ALL actual linear permutation rows π of X. Let A_d(π;x,y) indicate the directed distance-d event, d=1,2 and x≠y, with NO wraparound.

Assume real weights z_π satisfy

`z_π≥0`, `Σ_π z_π=n`,

`Σ_π z_π A_1(π;x,y)=1` for EVERY x≠y,

`Σ_π z_π A_2(π;x,y)≤1` for EVERY x≠y.                            (F)

Define `P=Σ_π z_π²` and `H={π:z_π>1/2}`, h=|H|.

Every z_π≤1 because π contains an adjacent event and its exact event sum is1. Any two rows of H are compatible at both respective event distances: a shared event would have total weight greater than1. Thus h≤n by disjoint adjacency counting. If h=n, those n actual rows are the original array: their n(n−1) adjacency events cover all ordered pairs and their distance2 events are noncolliding.

For any h, using z²≤z on H and z²≤z/2 outside H gives

`P≤n/2+(1/2)Σ_H z≤(n+h)/2`.                                     (B)

In particular if P>n−1, either h=n (done) or h=n−1. It remains to round this latter case without presuming the fractional weights are integral.

## 2. The n−1-heavy-row residual controls every remaining weight

Suppose h=n−1. Write each heavy weight as

`z_i=1−ε_i`, with `0≤ε_i<1/2`, and let `δ=Σ_(i∈H) ε_i`.

The total weight outside H is1+δ. The heavy rows have disjoint adjacency sets, so the complement E0 in all n(n−1) directed pairs contains exactly n−1 arcs.

A whole actual Hamilton row is uniquely determined by its directed adjacency set: identify its unique first symbol and follow its unique successors. Hence there is at most ONE row type τ with adjacency set exactly E0; such a row need not exist.

If τ exists and is distance2-compatible with all H, the actual rows H∪{τ} already give the original array. Assume for the moment this completion does NOT exist, either because E0 is not a Hamilton row or because its unique τ fails a distance2 cap with H.

### Lemma 1 — small residual-weight cap

Under that no-completion assumption, EVERY nonheavy row σ satisfies `z_σ≤δ`.

**Proof.** If σ's adjacency set is not exactly E0, at least one of its n−1 adjacent events lies in a heavy row i: otherwise its n−1 events would equal E0. Its exact event equation gives

`z_σ+z_i≤1`, so `z_σ≤ε_i≤δ`.

The only possible exception is τ itself, if it exists. By the no-completion assumption it shares a distance2 event with a heavy row i, whose cap again gives `z_τ≤1−z_i=ε_i≤δ`. Zero-weight atoms cause no exception. ∎

If δ=0, the lemma contradicts the remaining positive total mass1; equivalently n−1 unit rows force their unique feasible completion. Thus the no-completion assumption implies δ>0.

## 3. Strong purity gap and explicit actual-row rounding

### Theorem 2

For EVERY n≥3 and EVERY feasible mixture (F), if

`P>n−1`,

an original Tuscan-2 array exists and is obtained as follows:
- if h=n, take the n heavy rows;
- if h=n−1, E0 is the adjacency set of a unique row τ compatible with every heavy row, and take H∪{τ}.

**Proof.** By (B), h≥n−1; h=n was already verified. Suppose h=n−1 and the stated completion failed. Then Lemma1 applies.

If `0<δ<1/2`, nonnegativity gives `Σ ε_i²≤δ²`. Using the improved residual cap from Lemma1,

`P_H=(n−1)−2δ+Σ ε_i²≤(n−1)−2δ+δ²`,

`P_(Ω\H)≤δ Σ_(Ω\H) z=δ(1+δ)`.

Thus

`P≤n−1−δ+2δ²<n−1`,

because δ(2δ−1)<0.

If `δ≥1/2`, every ε_i<1/2 and at least one is positive, so

`Σ ε_i² < δ/2`.

The ordinary outside-H cap z≤1/2 gives

`P<(n−1)−2δ+δ/2+(1+δ)/2 = n−1/2−δ≤n−1`.

Both cases contradict P>n−1. Therefore the no-completion assumption is false. The actual τ, not a formal margin, must exist and be distance2-compatible with H. The n actual rows H∪{τ} have disjoint adjacency sets exhausting all ordered pairs, and disjoint distance2 events. This verifies the full original caller. ∎

The same argument proves P<n−1 whenever h=n−1 and no completion exists. It does not claim that every feasible mixture is integral or that an arbitrary majority choice rounds correctly.

**Original-size forward/converse:** an original T2(11) gives indicator weights and P=11>10. Conversely any feasible whole-row mixture with P>10 gives an actual T2(11) by the theorem. Thus this high-purity existence criterion is equivalent to the original problem; the substantive addition is the rounding proof2→1 without assuming integrality, not merely an integer re-encoding.

No high-purity point or upper bound preventing one is obtained here. The uniform feasible barycentre from v6 does not pay the purity hypothesis.

## 4. Exact nonrounded equality structure

### Theorem 3

Suppose a feasible (F) has P=n−1, and neither the heavy set itself nor the heavy-set-plus-unique-completion caller of Theorem2 yields an original array (in particular, this premise holds if no original array exists at this n). Then its support consists EXACTLY of

- n−2 actual rows of weight1;
- FOUR distinct actual rows of weight1/2;
- no other positive weights.

**Proof.** h=n or h=n−1 would already give an original array by §1 or the strict no-completion gap proved above. Hence h≤n−2. Equality P=n−1 in (B) forces h=n−2 and equality at every step: all heavy weights are1, and every other positive weight satisfies z²=z/2, so is1/2. Their remaining mass is2, giving exactly four such row types. Ω contains one atom per actual row, so they are distinct. ∎

This is a conditional classification of the critical fractional boundary, not a claim that such a nonrounded point exists for order11.

## 5. The boundary is an actual four-cycle two-cover, not free formal data

For any feasible mixture, the total weighted number of starts at each symbol is1, as is the total weighted number of ends. Indeed its weighted occurrences total n and its outgoing/incoming adjacent events total n−1. Consequently the n−2 unit rows of Theorem3 have separately distinct starts and ends.

Their augmentation by ∞ and deletion from the complete directed graph gives the genuine degree-two residual of v8. The four half-weight rows are ACTUAL Hamilton rows avoiding every unit row's adjacency and distance2 events (a positive additional weight on an already unit-used event would violate its cap).

Each residual augmented arc occurs in EXACTLY TWO of their four augmented Hamilton cycles:
- an original adjacency arc has residual weighted usage1, so its half-row occurrence count is2;
- a residual sentinel-start/end arc also has weighted usage1 by the start/end count, so has occurrence count2.

Each unused original distance2 outer pair occurs in at most TWO of the half-rows, by its weighted cap. No used outer pair occurs in them at all.

Thus the equality issue is a concrete, common-vertex FOUR-Hamilton-cycle two-cover with actual D2 incidence, not independently manufactured residual degrees or a formal U set. Whether such a boundary configuration necessarily admits a compatible two-row completion is NOT proved here. One may not choose two favourable cycles independently or assume that a balanced four-cycle cover includes a complementary pair with no D2 collision.

## 6. Exact remaining original step and limits

The global original problem is now equivalently the question whether a feasible whole-row mixture can exceed purity n−1. Theorem2 gives a complete actual-row realization in that event. No existence argument reaches that region, and no upper bound for all feasible mixtures excludes it.

At the critical equality, the unproved four-cycle two-cover rounding problem of §5 is an exact additional common-selection obligation. It is analytically forced by the equality conditions, not a selected small-state probe or a restricted original target asserted WLOG.

All arguments apply to arbitrary actual row types and real feasible weights at original n=11, with every support value free. No old stopped theorem, group/polynomial proof, chosen numeric test, solver or external source is used.

The w38 PROCESS MAJOR and complete HELD/ZERO consumer boundary remain permanent, as do all earlier exposure/STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP. Author-WRITTEN, unreviewed; no Main adoption, formal/kernel, executable, human, configured-family, source-openness, priority or novelty claim. Original target OPEN; standing full-window direction and deadline unchanged.
