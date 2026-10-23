# Information-science volume

Source volume: 《10000个科学难题·信息科学卷》 (10000 Selected Problems in Sciences: Information
Science, Science Press, 2011, ISBN 978-7-03-031911-1). Local copy: [`books/`](../books/README.md),
not tracked by Git; 1139 PDF pages; the table of contents is on PDF pages 11–21; PDF page = book
page + 21.

Each target directory owns its own status, sources, evidence and claims. This index only routes.
Round-level selection reviews, screening reports and parent replays live in
[`evidence/`](evidence/). [Repository overview](../README.md).

## Information-science selection (2026-10-14)

Screened the full table of contents, then read about 40 candidate sections to identify precise questions. A problem was kept only if it

1. has a precise mathematical statement in the book,
2. showed no full solution in a quick literature pre-screen on 2026-10-14, and
3. has a bounded attack path (exact computation, counterexample search or proof) on this machine.

"Not too hard" is a provisional [INFERENCE], not a guarantee. A failed literature search does not
prove that a problem is open. An independent selection review flagged disturbance decoupling as a weak
choice because exact per-instance decision is older than the book; it is retained as a scoped
partial result, not counted as a confirmed easy open problem. Intake provenance, the review and parent
replays are under [`evidence/information-science-intake/`](evidence/information-science-intake/).

| # | Target | Book problem (authors) | Book pages (PDF pages) | Outcome after the 2026-10-14 continuation | Directory |
|---|---|---|---|---|---|
| 1 | Robust SPR synthesis for stable interval polynomial families of degree > 4 | 区间系统的鲁棒严格正实综合 (郁文生, 王龙) | 680–682 (701–703) | Partially solved. Degrees 5 and 6 have recent public claims with Lean sources; neither build was replayed. New all-order proofs reduce every failure to two explicit critical contact certificates and make the conjecture equivalent to nonzero closed feasibility on radial stability-boundary boxes. There is still no proof or counterexample for degree 7 or higher. | [`robust-spr-interval-synthesis/`](robust-spr-interval-synthesis/) |
| 2 | Stochastic H∞ preview control | 随机系统 H∞ 预演控制 (张焕水, 王宏霞) | 674–676 (695–697) | Partially solved. A candidate continuous-time theory covers the mean-square substitute. A new exact constant-matrix finite-horizon example is feasible at γ = 6 under the printed criterion for all adapted disturbances, while every controller has mean-square gain above 14, so the substitute is not equivalent. General synthesis under the printed criterion remains unsolved. The 2020 SIAM N&S result is confirmed from its author manuscript to be discrete-time and finite-horizon; priority remains unclear. | [`stochastic-hinf-preview-control/`](stochastic-hinf-preview-control/) |
| 3 | Disturbance decoupling by static output feedback | 静态输出反馈下的干扰解耦 (陈本美) | 631–632 (652–653) | Partially solved. Exact per-instance algebraic decision is prior work. All unstabilized gains are now synthesized explicitly when min(m, p) = 1 (an affine family) and when m = p = 2 (one real quadric), at every order and with all feedthrough terms. General real gain selection and stable selection remain open; the Grassmannian framework is classical. | [`ddp-static-output-feedback/`](ddp-static-output-feedback/) |
| 4 | Optimal pixel expansion and contrast of visual cryptography schemes | 视觉密码方案的最优化问题 (刘峰) | 409–410 (430–431) | Partially solved. All four basis and collection optima are now certified for every strong access structure on at most five participants. The five remaining collection cases were closed by full-distribution impossibility proofs and independently re-derived without the original code. The general access-structure problem remains open. | [`visual-cryptography-optimality/`](visual-cryptography-optimality/) |
| 5 | P-type iterative learning control under bounded initial errors, relative degree ≥ 1 | 相对阶不小于 1 的 P 型迭代学习控制系统 (孙明轩) | 712–715 (733–736) | Open. No stationary finite-memory linear pointwise P-type learner combines exact nominal tracking with robustness to arbitrary bounded starts, at any relative degree. An initial-error-rectified P-type law achieves both for the degree-one integrator with initial errors only. It fails under arbitrary measurement noise at every degree and under process noise at degree one. | [`p-type-ilc-initial-error/`](p-type-ilc-initial-error/) |

None of the original five information-science targets was fully solved. The initial 2026-10-14 continuation produced the scoped
theorems and certificates above; parent replays and the independent re-derivation are under
[`evidence/information-science-push-20261014/`](evidence/information-science-push-20261014/). Four of
the five are control-theory problems: in this volume the control chapter holds most of the
precisely stated, tractable problems.

## Information-science screened out

Solved after the book was published:

- 基因组间的转位距离 (complexity of sorting by transpositions): NP-hard. Bulteau, Fertin, Rusu,
  "Sorting by Transpositions Is Difficult", ICALP 2011 / SIAM J. Discrete Math. 2012
  (doi:10.1137/110851390).
- 三维凸多面体相交检测 (O(log n) intersection test with linear-space preprocessing): Barba,
  Langerman, "Optimal detection of intersections between convex polyhedra", SODA 2015
  (doi:10.1137/1.9781611973730.109).

Too hard for a bounded attempt: existence of APN permutations for even n ≥ 8; tight nonlinearity
bounds for resilient Boolean functions (e.g. whether 8-variable balanced functions reach 118); the
P vs NP family; polynomial-time μ-calculus model checking; the Unique Games Conjecture; Tarski's
exponential-function problem; non-abelian hidden subgroups; lattice reduction; general decoding;
general characterizations for differential flatness and linear time-varying stability.

Not precisely posed (research directions or laboratory work rather than a checkable claim): most
engineering, optics, metrology and network items, and the popular-science section.

## Information-science expanded search (2026-10-14)

Checked **51 distinct candidate articles**, including targeted rereads, with three topic scouts;
then pursued seven proof dossiers. Exact book wording and current primary literature—not the
book's historical “open” label—determine each verdict. This round establishes **no new full
resolution of a previously open broad book problem**. It does completely answer the specific
mathematical readings and insufficiency claims below. Novelty is separate and remains
unestablished. Selection, direct source checks and parent replays:
[`evidence/information-science-more-20261014/`](evidence/information-science-more-20261014/).

| Target; book authors | Book pages (PDF pages) | Defensible outcome | Dossier |
|---|---|---|---|
| Geomagnetic Gauss uniqueness; 李玉和、杨建中 | 880–882 (901–903) | **Answered by classical prior work** for exact tangential+vertical continuum data on one source-free closed surface. Complete Green/Gauss separation proofs supplied; noisy, scalar-only and discrete data remain distinct. | [`geomagnetic-gauss-uniqueness/`](geomagnetic-gauss-uniqueness/) |
| Nonuniform spatial sampling / array aliases; 穆鹏程、殷勤业 | 446–448 (467–469) | **Answered by prior work** in the isotropic, noiseless, single-source model. Exact rational/algebraic decision and two counterexamples to published arbitrary-basis vertex shortcuts are certified. Arbitrary directional element gains are not silently included. | [`array-nonaliasing/`](array-nonaliasing/) |
| POMDP performance optimization; 汪德新、曹希仁 | 653–655 (674–676) | **Complete negative answer to universal expected-average optimizer existence:** a four-state blind model has supremum 1 but no maximizing policy, even with randomization/unbounded memory. The book omits an expectation symbol; other objectives and general optimization are not thereby solved. | [`average-reward-pomdp-nonattainment/`](average-reward-pomdp-nonattainment/) |
| Nonnegative, marginal-correct time–frequency distributions; 张建国、殷勤业 | 452–454 (473–475) | **Scoped sufficiency question fully refuted:** a genuine Schwartz Fourier pair passes both separate IF/GD density-feasibility tests and the covariance identity, but admits no joint nonnegative measure satisfying both. Rational dual + Arb interval certificate, independently reproduced. Broad “physical meaning” remains unspecified, not solved. | [`positive-tfd-marginals/`](positive-tfd-marginals/) |
| Piecewise-LTI approximation; 高静怀 | 467–469 (488–490) | **Partial:** complete known-kernel L¹ criterion, declared stochastic-metric characterizations, optimal segmentation and error bounds. Blind wavelet/reflectivity/Q identification needs extra assumptions; classical results are not called new discoveries. | [`piecewise-lti-approximation/`](piecewise-lti-approximation/) |
| Distributed scheduling under time-varying channels; 关新平、杨博 | 731–734 (752–755) | **Partial:** strong-stability theorem for arbitrary conflict graphs and finite-state Markov channels, but requires synchronized unbounded-rate control clocks. This does not satisfy the book's simple-policy intent. Prior rate stability is not confused with strong stability. | [`wireless-timevarying-strong-stability/`](wireless-timevarying-strong-stability/) |
| Adaptive large-population stochastic games; 李韬 | 635–637 (656–658) | **Partial:** all unknown A/B/Λ matrices identified, N-independent stability, mean-MSE and Nash-gap rates proved for a robustly stable, fully actuated homogeneous subclass with common/private pilots. General unknown stabilizable dynamics remain outside the theorem. | [`adaptive-mean-field-game/`](adaptive-mean-field-game/) |

**Strongest additional certificate:** the time–frequency example has both one-sided constraints
separately feasible with densities, yet its full-plane nonnegative dual has forced expectation
`−0.0057637133335289…`. This settles the proposed joint-sufficiency claim negatively, not the
complete classification of physically meaningful distributions. Parent replayed the 256-bit Arb
checker and independently reconstructed the Fourier identities, exact corner/Sturm checks and
60-digit Gaussian integrals with different code. No Lean/kernel or human-journal certification
is claimed.

Additional status findings, not new solutions by this project:

- The finite-domain **CSP dichotomy** mentioned in 约束求解与优化 was proved independently in
  2017; [Zhuk's primary theorem](https://arxiv.org/abs/1704.01914) was checked. This does not settle
  every constraint-optimization or random-phase-transition question in the article.
- The **binary surrogate-paradox** question within 因果推断 has sharp observed-data criteria
  ([Yin–Liu–Geng–Luo](https://arxiv.org/abs/1607.05454)); general causal inference is not solved.
- Network-coding **exact solvability** is undecidable
  ([Li, arXiv:2205.11461](https://arxiv.org/abs/2205.11461)); this is not a theorem computing the
  general asymptotic capacity region.
- The sensor article's displayed **Mathieu equation**, not Duffing, has classical analytic
  fundamental solutions ([DLMF §28.2](https://dlmf.nist.gov/28.2)); the wider physical sensor-design
  programme has no single specified mathematical acceptance condition.

No workspace/infrastructure audit, Git mutation, external contact or publication was performed.

## Difficult-problem visit (2026-10-15)

The owner requested one difficult information-science problem with a six-hour total ceiling, alongside
mathematics and physics. The [hard-problem catalog](evidence/information-science-hard-20261015/catalog.md)
records candidates, status sources, budget classes, probes and parent-review restrictions.

Selected `info-p0403`, **弹性布尔函数的非线性度的紧上界** (张卫国, 肖国镇, book pp. 403–405; PDF
pp. 424–426): existence of a balanced nine-variable Boolean function with nonlinearity at least 242.
An explicit truth table can settle this instance without assuming the unrefereed 2026 upper-bound
claim. Local-neighborhood or symmetry-class exclusions remain partial; timeout and heuristic failure
establish no nonexistence.

The [institute run](../institute/runs/hard-2026-10-15/README.md) first timed out during 10-minute
identification. With owner approval it restarted at 12:02 PT with a fresh six-hour allocation and a
30-minute selected-question identification stage. Authority for those engine visits:
[`record.json`](../institute/runs/hard-2026-10-15/problems/info-p0403/record.json).
Its batch 03 continuation closed **unverified** (accept-with-fixes) at 15:37 PT with partial results.
An elementary proof shows that the balanced nine-variable maximum is 240 or 242. Any balanced 242 function
must have degree exactly eight and nonzero support XOR. Restricted exhaustive exclusions were also replayed.
Existence remains open. See the [outcome ledger](../institute/review/hard-2026-10-15-outcomes.md).
The screening worker's one read-only Git-command deviation is recorded in the
[parent source checks](../institute/review/parent-source-checks.md).

### Authorized continuation (2026-10-16)

All **252** remaining fixed-half classes in the pinned restricted corpus are now excluded;
this is not global nonexistence. A universal odd-half residue argument gives distance at least
112. Its [zero-geometry continuation](evidence/hard-continuation-20261015/quadratic-distance/zero-geometry/README.md)
then excludes the entire balanced quadratic residue type **(polar rank4,weight128)** by an
explicit zero-flat/next-bit/character-projection proof. Fresh Codex review returned **ACCEPT**,
with a separate Opus review of its imported lemmas and independently replayed finite certificates.
Seven large residue-type families remain.

A separate corollary proves that a nine-variable function with exactly one, two or three Walsh zeros
has nonlinearity at most 240; attainment and priority are not claimed. The methods build on
Wang–Lou–Wang and Lou–Xu–Wang. Neither result is Lean-verified or human peer reviewed.
Balanced NL242 existence remains open. See the
[continuation ledger](../institute/review/continuation-20261015/outcomes.md). Three later attempts
on the remaining seven types produced only unreviewed sub-case conditions; none excluded another type.

## Six concurrent research lanes (2026-10-16–18)

The replacement info-2 slot constructed cyclic `(v,5,1)` difference families for
**v = 321, 501, 621, 681, 801 and 901** (16, 25, 31, 34, 40 and 45 base blocks). The pinned certificates
passed three independently written checkers, including a cross-vendor checker executed by the parent.
These are exactly the six possible exceptions of Abel–Costa–Finizio 2004 Theorem 14, restated as open in
two 2025–2026 primary sources; with that published theorem, the cyclic spectrum for v ≡ 1 (mod 20),
v ≤ 1001 is complete. The bounded priority audit found no earlier construction; it does not establish priority.
See the [parent verdict](../institute/runs/six-lane-2026-10-16/review/cdf-k5-parent-verdict.md)
for certificate hashes, checker controls, source/access limits and ongoing review.
All six finite existence theorems passed parent fresh Lean-kernel replay, and the complete claim
passed hostile review with minor fixes. The slot then proved that **no 2-(88,4,1) design has a
point-cyclic resolution**, the smallest undetermined case named by Topalova–Zhelezova (13 Oct 2026),
and the same for v = 8p, p ≡ 11 (mod 12). The written proof passed parent derivation, finite and
semantic controls, hostile review and a Codex cross-vendor review (ACCEPT). The full v = 88 theorem
also passed a parent fresh Lean-kernel replay. A bounded audit found no earlier equivalent
(NOVELTY-UNCLEAR; [verdict](../institute/runs/six-lane-2026-10-16/review/point-cyclic88-parent-verdict.md)).

**Optimal CPCW codes now exist for all eight frozen cases from the screened Baicheva–Topalova
(Axioms 2026) list**: (v,6,1) for v=122,123,124 and (v,5,1) for v=143,144,146,162,167. The source
also lists (126,6,1), which was already known and was excluded. The explicit codes
passed four independent verifier routes and parent byte-exact rebuilds. Existence together with the
matching upper bound is Lean-kernel checked by a parent fresh replay. **Priority correction:** Vos's Zenodo note
(registered 2026-08-24) already gives explicit optimal codes for all nine listed cases; PRIOR-CLAIM, not a gate
([verdict](../institute/runs/six-lane-2026-10-16/review/cpcw-optimal-parent-verdict.md),
[addendum](../institute/runs/six-lane-2026-10-16/review/cpcw-priority-addendum-v1.md)).

An explicit **point-cyclic resolution of a 2-(100,4,1) design** now passes three independent verifier
routes, byte-exact seed and producer replays and a parent-replayed Lean existence proof
([verdict](../institute/runs/six-lane-2026-10-16/review/point-cyclic100-parent-verdict.md)).
The bounded priority audit found no earlier equivalent, not proof of priority. Its source-status
label remains DERIVED-OPEN: the source names 88, not 100. The slot now works on the existence table
for all v ≡ 4 (mod 12) up to 200 ([contract](../institute/runs/six-lane-2026-10-16/screening/info-2-point-cyclic-table200-contract.json)).
**The table is now complete:** explicit point-cyclic resolutions exist for v = 112, 136, 160 and 196
(three checkers, parent seed expansion, mutations, rebuilt-producer byte replays and a parent fresh Lean
replay); 148 exists by the cited Lam–Miao family; 124 and 172 are excluded by Genma–Mishima–Jimbo 1997;
184 is excluded by this round's written 8p corollary. DERIVED-OPEN and NOVELTY-UNCLEAR
([verdict](../institute/runs/six-lane-2026-10-16/review/point-cyclic-table200-parent-verdict.md)).

**The covering-sequence minimum is exact: L(12,3) = 36.** No cyclic binary sequence shorter than 36 has length-12 windows within distance 3 of every 12-bit word. Counting excludes lengths through 13; three independently written exhaustive implementations exclude 14–35; the published CPro1 length-36 sequence is checked against all targets. A completeness review accepts it. This settles one table entry, modestly and computer-assisted, not by DRAT or Lean ([verdict](../institute/runs/six-lane-2026-10-16/review/cover12-3-parent-verdict.md)). **Priority correction:** Raval's Zenodo report (registered 2026-09-07) already claims L(12,3) = 36; PRIOR-CLAIM, not a gate ([addendum](../institute/runs/six-lane-2026-10-16/review/cover12-3-priority-addendum-v1.md)).

**The balanced ternary design BTD(12,15;6,2,10;8,6) does not exist**, even with repeated blocks; Rosin's 2025 table lists it among the Handbook's open instances. With H = 40I − 5MᵀM + 24J, the design identities give H² = 40H, and Connor's determinant method makes every 3 × 3 principal minor of H a perfect square; row relations then force two classes of columns and a mixed minor in {−150, 50, 150, 200}, a contradiction. The written proof passed Codex and Claude reviews, and a Lean 4 kernel proof of the explicit unrestricted statement passed the parent's fresh replay against its own restatement, with standard axioms only. The method is classical and the significance modest; NOVELTY-UNCLEAR ([verdict](../institute/runs/six-lane-2026-10-16/review/btd12-15-parent-verdict.md)).

**The companion instance BTD(14,18;7,1,9;7,4) does not exist either**, again with repeated blocks allowed. Here H = 63I − 9MᵀM + 28J satisfies H² = 63H; there are 14 columns with one entry 2 and 4 with none, the identity 729·det(N)² = 7¹⁰·det H[S] excludes the two possible mixed 4 × 4 minors (3645 by a mod-3 argument, −2187 by sign), and the remaining column-pair sums would total 36 instead of 0. Codex and Claude reviews accepted it, the parent's exact arithmetic and checker replay pass, and the Lean kernel proof passed the parent's fresh replay against its own restatement. Same classical mechanism and one modest contribution with (12,15); NOVELTY-UNCLEAR ([verdict](../institute/runs/six-lane-2026-10-16/review/btd14-18-parent-verdict.md)).

**BTD(12,20;4,3,10;6,4) does not exist**, also with repeated blocks allowed. Since B − V = 8, determinant conditions are weak; instead the 1-entries are tetrads meeting in 0 or 2 points, a self-contained lemma classifies connected families into pair multigraphs or e7/e8 structures, and the resulting 3073 covering cases are each excluded by a DRAT-certified SAT proof of their ternary completion. Structural reviews and a complete-claim audit found no fatal or major issue, and the parent replayed every generator byte-identically and re-checked all 3073 proofs. Computer-assisted, not Lean; NOVELTY-UNCLEAR ([verdict](../institute/runs/six-lane-2026-10-16/review/btd12-20-parent-verdict.md)). **BTD(14,28;8,3,14;7,6) exists**: an explicit 14 × 28 witness, invariant under an order-3 permutation of rows and columns and found by a restricted SAT model, passes the parent's definition-first checker, a Codex-written verifier and a Claude-written prompt-only checker, with intended-reason controls and a byte-identical producer replay ([verdict](../institute/runs/six-lane-2026-10-16/review/btd14-28-parent-verdict.md)). The 1996 Handbook table listed no design for it; priority is not established. All four Handbook BTDs still listed open in Rosin's 2025 tables are therefore decided. The slot then targeted BRD(26,130,25,5,4); an explicit witness was found and verified, but existence had already been claimed by Abel–Chan–Combe–Palmer (2011), so the CPro1 open label was stale and no gate is claimed ([verdict](../institute/runs/six-lane-2026-10-16/review/brd26-parent-verdict.md)). After a post-2006 literature [kill check](../institute/runs/six-lane-2026-10-16/review/info2-killcheck-screen-v1.md), the slot targeted SW(25,16). An explicit witness was found and verified (including a Lean kernel proof), but a public preprint registered on 2026-10-15 already claims SW(25,16), SW(27,16) and SW(29,16), so no gate is claimed ([verdict](../institute/runs/six-lane-2026-10-16/review/sw25-parent-verdict.md)). CFR(4,33) then proved stale too: Sage has a cyclic difference matrix that gives CFR(5,33), independently reconstructed by the parent ([record](../institute/runs/six-lane-2026-10-16/review/cfr33-prior-art-parent-verdict.md)). The active info-2 target is the authorized alternate **CFR(5,27)**, with an exact cyclic-group prior-art screen before search ([contract](../institute/runs/six-lane-2026-10-16/screening/info-2-cfr33-contract.json)).

**Update, 2026-10-17 PDT: CFR(5,27) exists.** Two explicit 5 × 27 circular Florentine rectangles (equivalently 6-row difference matrices over cyclic Z_27, from symmetric orbit models with groups C6 and S3) resolve an instance CPro1 lists in `OPEN_INSTANCES`, so F_c(27) ≥ 5. Six routes verified them: the parent definition-first checker with 43 intended-reason controls, Codex's own verifier, a Claude-written checker run by the parent (58/58), a byte-identical producer rebuild/replay with an independent group-action audit, and CPro1's own acceptance predicate. The bounded priority screen found nothing in scope; the Handbook table, Song 2000 and the 2005 baseline bodies were unread. Modest significance: one row beyond the 2005 cyclic Z_27 baseline; no MOLS-table consequence ([verdict](../institute/runs/six-lane-2026-10-16/review/cfr27-parent-verdict.md)). Next: an exact-group screen of the alternate CFR(6,21).

**Count clarification and next target, 2026-10-17 19:01 PDT.** The CFR(5,27) “six routes” are six evidence categories, not six independent checker implementations: the parent checker, Codex verifier and Claude-authored checker are the three separately authored definition-level checkers; parent controls reuse the parent checker; producer replay and the action/conversion audit are reproduction evidence; CPro1's predicate is an additional upstream check. The active info-2 target is now **CFR(6,21)**, a 7-row difference matrix over cyclic Z_21 ([contract](../institute/runs/six-lane-2026-10-16/screening/info-2-cfr21-contract.json), [screen](../institute/runs/six-lane-2026-10-16/screening/info-2-cfr21-priority-screen-v1.md)). A positive witness would also give six MOLS(21), compared with the located published lower bound five; symmetry-model exhaustion would not prove nonexistence.


The info-1 guessing-number target remains open: `20/3 ≤ gn(R⁻) ≤ 1847/276`.
Its reviewed triangle-balancing lemma gives an exact entropy/code reformulation, not a new bound.
The following cyclic (211,7,1) difference-family target found no witness. Worker-level complete
searches exclude every nontrivial multiplier model, and unrestricted searches remain UNKNOWN.
The slot now targets the packing array PA(19,8,6)
([contract](../institute/runs/six-lane-2026-10-16/screening/info-1-packing-array19-contract.json)).
Earlier Boolean and robust-SPR evidence is preserved without promoting the unsolved targets.


