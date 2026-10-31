# Same-harness scientific review: f246 SPR7 universal robustification

## Disposition and scope

**Scientific disposition:** the stated conditional robustification, interior, certificate, rationalization and one-sided search claims are supported by the reconstruction below, subject to the explicitly identified standard imports. No mathematical fatal (F), major (M), or minor (m) finding was found; no mathematical claim is marked INCONCLUSIVE. There is one **procedural m**: the manifest-prefix comparison and input measurements were collected by a single command, rather than completing the comparison before beginning the input measurements. Both input bodies remained unopened until the command returned and all hashes and counts had been compared. The exact sequence and a failed pathname attempt are disclosed below. Parent disposition is separate.

This is **same-harness** review, not a human review, independent-model-family review, formal/kernel verification, or novelty verification. It proves neither that a counterexample exists nor that every box has a numerator. **This is not a termination proof for the synthesis case; the original septic question remains OPEN within the assigned scope.** No external literature/status or novelty search was performed.

## Frozen inputs and actual sequence

1. Opened the assigned `manifest-v1.json` first. The ordinary display shortened its two long lines, so I opened manifest lines 9 and 29 again raw. Full manifest SHA-256 measured as `5c1eca0929dbb11713c358f14466417d64ee5741d19dcb46b7b4762b90e920a7`, matching the assigned prefix `5c1eca0929db`.
2. One `shasum -a 256` invocation measured the manifest followed by both inputs, and `wc -cl` then measured both inputs. The returned values were compared with the assignment and manifest **before opening either input body**. However, because all three digests were produced in that one command, the prefix comparison was not completed before the input digest measurements began, contrary to the literal two-stage order. This is the procedural m reported above; it is not silently treated as compliant sequencing.
3. Input 1, `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/written-releases/info-2-septic-box-definitions-v1.md`: SHA-256 `d86737954bee95836e2d2cffade9cba15a99f2bb486b660ada2562c25fc764ad`, 3005 bytes, 37 LF, all matching the manifest. Read completely, in raw windows 1–15, 16–30, 31–45, through its actual final line 37. It supplies the assigned definition and scope only, not an adopted theorem or an independently checked book transcription.
4. Input 2, `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261029-universal-counterexample-robustification-v1.md`: SHA-256 `6c60f44465c55e786d0871bb6c1e3675557a927087259c618ced8e567353295f`, 12849 bytes, 110 LF, all matching the manifest. Read completely in raw windows 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, and 106–120, through its actual final line 110. The first attempt at 76–90 accidentally used a path omitting `information-science/evidence` and returned not found; the correct declared path was immediately read before the next window. No input body was obtained from the bad path.
5. Only after the complete declared-input display did I undertake mathematical reconstruction. The mandatory general memory summary and operational review skills were consulted after those declared inputs; they supplied no mathematical premise. There were no other source bodies, adopted scientific dispositions, linked-body expansions, sibling reviews, author contacts, author code executions, solver results, external searches or model/API calls. The manifest and two declared bodies are the complete scientific input.

The native `/bin/date` reading before writing the reviewer control script was `2026-10-29T14:43:19-0700 PDT`; the reading before writing this review was `2026-10-29T14:44:40-0700 PDT`. These are observed prewrite clocks, not assertions of file creation times.

## Per-claim verdicts

In this table **SUPPORTED** means F = none, M = none, m = none, and INCONCLUSIVE = no for that scientific claim; this is a reasoned same-harness assessment, not a formal proof certificate. The procedural m above is separate from these mathematical verdicts.

| Claim | Verdict | Reason, reconstructed below |
|---|---|---|
| Pairing identity and four actual parity corners | SUPPORTED | Direct real/imaginary multiplication and affine minimization over two independent intervals. |
| Compactification, exact-degree strictness, and synthesis iff zero is outside the hull | SUPPORTED | Endpoints are `a_0 e_0` and `e_7`; exact degree forces positive limiting leading ratio; compact strict separation is bidirectional. |
| Every zero annihilator has at least four distinct positive finite nodes | SUPPORTED | Endpoint-vanishing two-parity isolators contradict Hurwitz stability if there are at most three. |
| Strict enlargement in all seven coordinates forces full eight-dimensional interior | SUPPORTED | A weak supporting vector must vanish at four conjugate pairs, so a nonzero degree-at-most-seven polynomial is impossible. No stability of the enlargement is needed. |
| Strict-negative certificate with at most eight actual finite positive-frequency atoms | SUPPORTED | Full interior supplies a strict negative vector; conic elimination gives at most eight, and continuity replaces endpoint atoms. |
| Rational frequencies and weights for rational boxes | SUPPORTED | Strict coordinate inequalities survive simultaneous rational perturbations of finitely many positive variables. |
| Negative certificate excludes an exact-degree common SPR numerator for a Hurwitz box | SUPPORTED | A common numerator is Hurwitz with strictly positive coefficients, contradicting the negative aggregate. |
| Arbitrarily small rational full-width robustly Hurwitz enlargement and open nonsynthesis neighborhood | SUPPORTED | Compactness gives a uniform stability margin, and the finite strict certificate persists under endpoint perturbations. |
| Effective one-sided counterexample enumeration | SUPPORTED, conditional on the named Kharitonov and Routh–Hurwitz imports | Every rational witness is eventually visited and checked exactly; these imports are not used to prove the interior theorem. |
| No synthesis-case termination or actual septic answer | SUPPORTED as a limitation | A conditional existence-to-witness implication and a semidecision procedure do not decide the universal question. |

## Independent reconstruction

### 1. Rows, corners, compactification, and strict duality

Let `a(s) = s^7 + sum_{j=0}^6 a_j s^j`, `b(s) = sum_{j=0}^7 b_j s^j`, and `t = w^2`. Write `a(iw) = E_a(t) + iw O_a(t)` and similarly for `b`. Multiplying by the conjugate gives

`P_{a,b}(t) = Re(b(iw) conjugate(a(iw))) = E_a E_b + t O_a O_b`.

A Hurwitz denominator has no imaginary-axis zero, so its positive squared modulus makes `P > 0` exactly the assigned SPR inequality at finite frequencies. For a fixed nonnegative `t`, the even and odd coefficients vary independently and give a rectangle of possible `(E_a,O_a)`. The alternating signs of powers of `-t` give its two even and two odd endpoints; each of the four combinations is one actual box member. The displayed `P` is linear in `(E_a,O_a)`, so its minimum over the rectangle is at an actual corner. Thus four strict inequalities are equivalent to strict inequalities for every member at each finite `t`, including `t=0`.

For the row `g_a(t)` of the target, dotting with `b` gives `P/(1+t)^7`. Degree counting gives the limits `g_a(0) = a_0 e_0` and `g_a(infinity) = e_7`: every even-coordinate numerator has degree at most six in `t`, every odd-coordinate numerator at most seven, and the top-degree `b_7` pairing has coefficient one. The four curves therefore extend continuously to `[0,infinity]`; their union is compact, and its convex hull is compact.

A common exact-degree numerator satisfies `b_7 != 0`. Its real ratio is strictly positive at every finite frequency and tends to `b_7`; hence `b_7 >= 0`, and exact degree makes `b_7 > 0`. All finite corner pairings and the infinity pairing are strictly positive. Compactness yields a single positive lower bound on the four compactified curves, hence zero is not in their convex hull. Conversely, if zero is outside that compact convex hull, strict separation gives a vector pairing positively with every row. Since `e_7` is one of the rows, this vector has `b_7 > 0`; the four-corner reduction supplies strict positivity for all original members and finite frequencies. Thus, for a robustly Hurwitz `K`, **no common exact-degree numerator iff `0 in C_K`**. The exact-degree requirement is essential for the infinity step.

### 2. Why a zero representation needs four positive nodes

Caratheodory gives a finite zero representation using at most nine rows. Delete zero weights, and group rows at each common positive finite `t_i`. Since a row is affine in the monic denominator coefficients, the group equals its total positive weight times `g_{a_i}(t_i)`, where `a_i` is the weighted average of the original denominators. The box is convex, so `a_i in K` and is Hurwitz. The zero-frequency contribution is a nonnegative multiple of `e_0`: stable monic real polynomials have `a_0 > 0`. The infinity contribution is a nonnegative multiple of `e_7`. Endpoint contributions alone cannot sum to zero with positive total mass.

Assume there are `m <= 3` distinct positive finite nodes. For each node define

`H_i(s) = product_{j != i}(s^2 + t_j)`, `q_i^o(s) = s H_i(s)`, and `q_i^e(s) = s^2 H_i(s)`.

Their degrees are at most five and six, respectively, and their constant and seventh coefficients vanish. Thus both pairings with endpoint rows vanish. They also vanish at each other positive node. At the selected node, with `h_i = product_{j != i}(t_j - t_i) != 0`, the respective pairings are

`q_i^o . g_{a_i}(t_i) = t_i h_i O_{a_i}(t_i)/(1+t_i)^7`,

`q_i^e . g_{a_i}(t_i) = -t_i h_i E_{a_i}(t_i)/(1+t_i)^7`.

Dotting the zero representation with both coefficient vectors and using the positive group weight forces both `E_{a_i}(t_i)` and `O_{a_i}(t_i)` to vanish. Then `a_i(i sqrt(t_i)) = 0`, contradicting Hurwitz stability. Hence at least four distinct positive finite nodes occur in every such representation.

### 3. Full interior after any strict coordinate enlargement

At every fixed finite `t`, each row of `K` lies in the convex hull of the four rows of `K'`: its even and odd values lie in the enlarged rectangle, and the row is affine in those values. The endpoint inclusion also holds. Consequently `C_K subset C_{K'}` and zero belongs to `C_{K'}`.

If zero were not in the full `R^8` interior, a supporting hyperplane would supply nonzero `b` with `b . g >= 0` on `C_{K'}`; this applies even if the hull were lower-dimensional. Pair it with the positive zero representation from `K`. Every original term is nonnegative, so every positive-node group pairs to zero. Each grouped denominator `a_i` is strictly interior to all seven intervals of `K'`, even if its original interval was degenerate. The affine function `a -> P_{a,b}(t_i)` is nonnegative throughout `K'` and zero at `a_i`. Varying only `a_0` both ways forces `E_b(t_i) = 0`; varying only `a_1` forces `t_i O_b(t_i) = 0`. Thus `b` vanishes at both `+i sqrt(t_i)` and `-i sqrt(t_i)` for at least four distinct positive `t_i`. Those are eight distinct roots, impossible for nonzero real `b` of degree at most seven. Hence `0` is in the **full** eight-dimensional interior of `C_{K'}`. This reasoning uses stability of `K`, not stability of `K'`.

### 4. At most eight atoms, endpoint replacement, and rationalization

Full interior gives `-eta * (1,...,1) in C_{K'}` for some `eta > 0`. Rescale a finite convex representation to represent `-(1,...,1)` as a nonnegative conic combination. If more than eight row vectors occur, they are linearly dependent in `R^8`. Choose the sign of a nonzero dependence so at least one coefficient is positive, subtract the largest feasible multiple preserving all nonnegative weights, and delete a zero weight. Repetition proves the conic Caratheodory bound of eight; all retained weights are positive. This argument counts rows, not distinct denominators or frequencies.

If an atom is at zero or infinity, retain its actual corner and positive weight, and replace its compactified parameter by a sufficiently close strictly positive finite value. There are finitely many atoms, the row curves are continuous, and all eight aggregate coordinates started strictly negative, so all signs survive. This remains valid for an unstable `K'` and for any sign of its endpoint row. For rational interval endpoints, rows at positive rational `t` have rational entries. Simultaneously approximate each finite positive `t` and weight by positive rationals closely enough to preserve the eight strict signs. Alternatively absorb each positive rational `(1+t)^{-7}` into its weight and use uncompactified polynomial-pairing rows. No assumption that an original zero annihilator is rational or strictly negative is required.

### 5. Why the certificate is a genuine obstruction for a stable box

Suppose, for contradiction, a robustly Hurwitz box with the strict-negative aggregate has a common exact-degree numerator `b`. As above `b_7 > 0`. Fix any box member `a` and set `p_theta = (1-theta)a + theta b` for `0 <= theta <= 1`. Its leading coefficient is `(1-theta)+theta b_7 > 0`, uniformly bounded away from zero on the compact parameter interval. On the imaginary axis,

`Re(p_theta(iw)/a(iw)) = (1-theta) + theta Re(b(iw)/a(iw)) > 0`.

Thus no `p_theta` has an imaginary-axis zero. Continuity of roots and the uniformly nonzero leading coefficient prevent crossings of the imaginary axis or escape to infinity, so all `p_theta`, including `b`, are Hurwitz. A real Hurwitz polynomial with positive leading coefficient factors into positive-coefficient linear factors for real negative roots and positive-coefficient quadratics for nonreal conjugate pairs. Hence every coefficient `b_j` is strictly positive. Each finite certificate atom has positive pairing with `b`, so its positive weighted sum has positive pairing; but the aggregate has eight strictly negative coordinates, whose dot product with `b > 0` is negative. Contradiction.

### 6. Uniform stability, open neighborhood, and exact search

The Hurwitz region in the seven nonleading coefficient coordinates is open. The compact set `K` lies inside it, so some uniform coefficient neighborhood of `K` also lies inside it. Choose each lower endpoint rational and strictly below its original lower endpoint, and each upper endpoint rational and strictly above its original upper endpoint, all sufficiently close. Coordinatewise clamping maps the resulting enlarged box into `K` with uniformly small displacement, so the entire enlargement is Hurwitz. Rational density makes the choices possible at arbitrarily small prescribed distances; all seven widths are positive.

At this enlarged rational box fix its finite rational positive-frequency, positive-weight certificate. Row sums depend continuously on the fourteen endpoints, so all strict negative signs persist under small endpoint perturbations. The box remains full-width and uniformly Hurwitz by the same compactness argument. Every sufficiently nearby box therefore has the same obstruction. This proves an open nonsynthesizable neighborhood **conditional on the initial nonsynthesizable `K`**.

Fair enumeration of rational ordered endpoint vectors, the four parity corners, up to eight positive rational squared frequencies, and positive rational weights eventually visits any such rational witness. The eight signs are exact rational comparisons. For robust stability, the target explicitly imports the classical Kharitonov theorem: for a fixed-degree, independent real closed interval polynomial, robust Hurwitz stability is equivalent to Hurwitz stability of the four alternating endpoint polynomials; here monicity fixes the degree, and degenerate intervals are permitted. The target also imports the Routh–Hurwitz criterion, which decides each rational monic septic by strict positivity of its seven leading Hurwitz determinants. These imports apply to the enumerator and are not inferred from an author PASS or solver output. Consequently the search is sound and, **if any original real or degenerate counterexample exists**, eventually finds one. It does not terminate with a positive synthesis theorem in the opposite case.

## Reviewer-owned exact controls and limits

The independently written standard-library `Fraction` script `reviewer-exact-controls-v1.py` has SHA-256 `d7a5400fe09f891ebbf9917f58a824a318ad7737f44b6478d170c33c90295789`. It was run once, with a 120-second deadline: native `/bin/date` before execution `2026-10-29T14:43:42-0700 PDT`, native `/bin/date` after execution `2026-10-29T14:43:46-0700 PDT`, exit code `0`. It did not read, import, compile, or run author code. It performed the following finite illustrations; they are controls, not substitutes for the universal argument:

- Checked the row identity against direct complex arithmetic at five rational frequencies over all 128 vertices of one box: 640 exact comparisons. At those frequencies it checked both extrema against the four actual parity corners. An intentional wrong odd-coordinate sign changed the pairing, as intended.
- For `(s+1)^7` and nodes `1,2,3`, checked both endpoint-vanishing isolators at each node and their off-node vanishing exactly. An intentionally missing locator factor produced a nonzero off-node pairing, as intended.
- Checked finite samples of `(s+1)^6/(s+1)^7`; independently, its real part is exactly `1/(1+w^2) > 0` at every finite frequency while its leading ratio tends to zero. This is a negative control for omitting the exact-degree requirement, not a valid degree-seven numerator.
- Constructed a four-atom rational strictly negative aggregate for a deliberately **non-Hurwitz** box with `a_0=...=a_4=0` and `a_5,a_6 in [-3000,3000]`. For squared frequencies `(1,2,3,4)`, signs of `(-10,20,-15,4)`, the corresponding actual parity corners, and weights `|x_i|(1+t_i)^7/(3000 t_i^3)`, the exact eight coordinates were `(-1,-1037/1000,-1,-2711/3000,-1,-1277/1000,-1,-431/3000)`. Flipping the first atom's even corner made coordinate zero equal `19`, rejecting the strict-negative condition for the intended reason. This example is not a septic counterexample because its denominators have a zero root.

## Explicit imports and remaining gap

The reconstruction imports elementary real/complex polynomial arithmetic and root-counting, compactness, finite-dimensional strict and supporting separation, ordinary and conic Caratheodory, continuity of roots and openness of the Hurwitz region, and density of the rationals. It imports Kharitonov and Routh–Hurwitz only for the optional exact enumeration implementation under the hypotheses stated above; these classical results are not re-proved or formally checked here. No adopted scientific disposition, prior result, historical held payload, author verification line, search output, or sibling conclusion is used as a premise.

The remaining gap is substantive and explicit: no actual robustly Hurwitz septic counterexample was produced, and no proof of universal septic synthesis was produced. The conditional rational-witness theorem and counterexample semidecision do not resolve that gap or establish novelty. The original septic question remains **OPEN** in this review's scope.
