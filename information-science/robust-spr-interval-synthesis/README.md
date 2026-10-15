# Robust SPR synthesis for interval polynomial families of degree > 4

区间系统的鲁棒严格正实综合 — 郁文生 (Yu Wensheng), 王龙 (Wang Long).
《10000个科学难题·信息科学卷》, Science Press 2011, book pp. 680–682 (PDF pp. 701–703);
page images in [`sources/book/`](sources/book/). Dates are Pacific time; work done 2026-10-14.

## 1. Problem as posed (book p. 682)

Let P^n be the real polynomials of order n and H^n ⊂ P^n the Hurwitz ones. For b ∈ P^n and
a ∈ H^n, b/a is strictly positive real (SPR) iff Re[b(jω)/a(jω)] > 0 for all real ω
(Definition 1). A polynomial set F is robustly stable iff every member is Hurwitz (Definition 2).

**Question.** For a robustly stable interval polynomial family of order n > 4, does there always
exist one fixed polynomial b(s) such that b(s)/a(s) is SPR for every a(s) in the family? Equivalently:
is robust stability of an order-n (n > 4) interval family necessary and sufficient for robust SPR
synthesizability? The authors conjecture yes (no counterexample in their numerical examples).
Necessity is immediate; the open part is sufficiency.

**Formalization used here.** Following the authors' own papers (Wang & Yu, ACC 2001,
arXiv:math/0202242: K = {s^n + Σ a_i s^{n−i}, a_i ∈ [a_i^−, a_i^+]}) and the 2026 announcements for
n = 5, 6, an interval family is a **monic** box of closed coefficient intervals (degenerate
intervals allowed); the numerator has **exact degree n** (b ∈ P^n); SPR means **strict** positivity
of Re(b/a) at **every real ω** for **every** member. The book text itself does not say "monic";
boxes with an uncertain leading coefficient are treated as a separately labelled variant
(Prop. E in [`work/theory.md`](work/theory.md), outcome O6).

**Fully solved means:** for every n ≥ 5, either a proof that every robustly Hurwitz monic box of
degree n has such a numerator, or an explicit robustly Hurwitz box of some degree n ≥ 5 with none,
certified exactly (Lemma B below gives a finite exact certificate format).

## 2. Status verdict: PARTIALLY-SOLVED (open for every n ≥ 7)

| Order n | Status (monic boxes, exact-degree numerator, strict SPR) | Decisive source | Verified here? |
|---|---|---|---|
| ≤ 3 | Solved (classical) | Hollot–Huang–Xu 1989; Anderson et al. 1990; as cited in Wang–Yu ACC 2001 | citation chain read; originals not read |
| 4 | Solved | Wang & Yu, ACC 2001 (arXiv:math/0202242, Thm. 4); Yu & Wang, IEEE TCAS-I 48 (2001) 506–509 | arXiv proof read; journal: metadata only |
| 5 | Affirmative theorem **announced** (2026, unrefereed; manuscript only on GitHub, no arXiv version found) | Yu, Xu, Dou, Ji, Wang manuscript (GitHub release 2026-10-06) + Lean 4 sources `dgjszy/quintic-spr-proof` @ 866e2b5, `SPR.N5.Direct.robustSPR` | statement audited; build not reproduced; exact spot-checks (Section 5) |
| 6 | Affirmative theorem **announced** (2026, unrefereed) | Xu, Dou, Ji, Wang, Yu, arXiv:2609.26541v2 + Lean 4 sources `dgjszy/sextic-spr-proof` @ 2b94aa7, `SPR.N6.Direct.robustSPR` | statement audited; build not reproduced; construction spot-checked exactly (Section 5) |
| ≥ 7 | **Open** — no interval-family theorem or counterexample in the reviewed material or found here | — | searches 2026-10-14 (not proof of absence) |

Lean status: both developments pin Lean 4.30.0 + Mathlib v4.30.0 (c5ea0035). A local replay needs
about 11 GB (toolchain 2.7 GB + Mathlib oleans 6.6 GB + outputs); the disk had 13 GB free, so the
parent decided to skip it. Static source scan at the pinned commits
([`evidence/lean-static-audit.txt`](evidence/lean-static-audit.txt), command in
[`work/lean_static_audit.sh`](work/lean_static_audit.sh)) found no proof-placeholder or proof-bypass
declarations: 0 occurrences of `sorry`, `admit`, `axiom` declarations, `unsafe`, `implemented_by`,
`@[extern]`, `opaque`, `ofReduceBool`, custom notation or attribute removal; the single
`native_decide` hit (quintic) is inside a doc comment; exactly one definition of each
`RobustSPRStatement`; the build-time audit (`Lean/Audit.lean`) would allow only `propext`,
`Classical.choice`, `Quot.sound` and fail below 426 (n = 5) / 63 355 (n = 6) audited theorems. This
is not a kernel check: elaboration and the transitive axiom audit were not reproduced.
The formal statements quantify over all closed monic coefficient boxes (lower ≤ upper), require every
member to have all complex roots with negative real part, and assert one `b : ℝ[X]` with
`b.natDegree = n` and `0 < Re(b(iω)/a(iω))` for all members and all real ω — a faithful
formalization of the monic question. Neither repository has CI runs (GitHub API: 0 workflow runs,
0 check runs), so no third-party build evidence exists. The authors' own records state a successful
build for n = 5 (8540 jobs, fresh project outputs) and for n = 6 (project outputs reused from the
source project; 63 355 theorems audited). Label for n = 5, 6: *reported with public Lean proof, not
replayed locally (disk limit); statements audited; constructions spot-checked.*

Remaining open set: **every n ≥ 7** for the monic formalization; hence the book's question
("for all n > 4") is open. The non-monic variant is not covered by the n = 5, 6 theorems (Prop. E).

## 3. State of the art (all checked items link to primary sources; see [`sources/references.md`](sources/references.md))

| Result | Hypotheses | Source | Verified? |
|---|---|---|---|
| Four-corner (Kharitonov) reduction for a fixed numerator | any box, leading interval ∌ 0 | Dasgupta–Bhagwat 1987; 2609.26541 Lemma 2.2 | proof re-derived (theory.md, Lemma A) |
| Same even (or odd) parts ⇒ synthesizable | any n | Hollot et al. 1989; Patel–Datta 1997 | UNVERIFIED (book) |
| Segments (convex hull of two polynomials) ⇒ synthesizable | any n | Yu–Wang–Ackermann, Sci. China F 47 (2004); Wang arXiv:math/0210452 | abstract read |
| Interval boxes, n ≤ 4 | monic | Wang–Yu ACC 2001 / TCAS-I 2001 | arXiv proof read |
| Interval boxes, n = 5 | monic, degenerate intervals allowed | quintic manuscript + Lean (2026) | statement audit + spot-check |
| Interval boxes, n = 6 | monic, degenerate intervals allowed | arXiv:2609.26541 + Lean (2026) | statement audit + spot-check |
| Polytopes: no common numerator of degree n−1 for a stable 3rd-order triangle | polytope | Wang–Yu ACC 2001, Example 4 | read (equal-degree numerator does exist there) |
| LP sufficient condition of Anderson et al. is not necessary | n = 4 | Betser–Zeheb 1993 (reproduced as Example 1 of Wang–Yu 2001) | metadata + reproduction in Wang–Yu |

## 4. Attack log (2026-10-14)

1. Read the book pages, both 2026 papers and both Lean statement files; static Lean audit.
2. Implemented the exact problem numerically: four-corner pairing polynomials, scale-free angular
   synthesis margin δ* via LP bisection ([`work/margin.py`](work/margin.py)), semi-infinite LP
   exchange method ([`work/sprlib.py`](work/sprlib.py)).
3. Cheap falsification at the smallest open orders: random near-boundary stable boxes n = 5–8;
   δ*(ε) scans toward the stability boundary; non-monic boxes n = 3–5.
4. Derived general-n structure ([`work/theory.md`](work/theory.md)): alternation certificate
   (Lemma B), closed-limit criterion (Lemma C), fully-closed marginal boxes (Prop. D), interior
   reduction and boundary sandwich (Lemma F, Cor. G), conditional converse (Lemma H), non-monic
   reduction (Prop. E).
5. Stress test in the most constrained regime (all n−2 gaps closed): random-walk and CMA-ES search
   over realizable fully-closed boxes n = 5–11, high-precision (60-digit) re-tests of every suspicious
   case after reducing to the 3-dimensional numerator space left by the forced double contacts.
6. Census of alternation configurations surviving the combinatorial filters of the quintic proof,
   generalized to n = 4–9.
7. Independent exact spot-checks of the n = 5 and n = 6 claims (sub-agent; Section 5).
8. Codex hostile referee on the central claims (Section 7).
9. Continuation: proved the all-order critical construction and weak-numerator rigidity, including
   coprimality and all degree/endpoint cases (I–J); proved exact contact rank (K); derived an
   unwrapped-phase exclusion (L) and removed the boundary sandwich's zero-free premise (M).
   No additional random-box search or Lean build was run.
10. Challenged the remaining bridge with one exact degree-seven marginal box: a Hurwitz,
    positive-coefficient numerator satisfying every double-contact equation still fails a corner
    pairing. A different numerator works on that same box, so this is a shortcut counterexample,
    **not** a counterexample to the book.

## 5. Outcomes (evidence labels)

| # | Outcome | Label | Evidence |
|---|---|---|---|
| O1 | Status by order (Section 2): monic n ≤ 4 classical, n = 5, 6 announced in 2026 with public Lean sources whose statements match the question (builds not reproduced here), every n ≥ 7 open | Novelty status (literature); Lean: statements audited, not replayed | [`sources/references.md`](sources/references.md), [`evidence/lean-static-audit.txt`](evidence/lean-static-audit.txt) |
| O2 | n = 6: the explicit numerator of arXiv:2609.26541 ((3.6), (4.1)–(4.14); Lemma 2.3 when the even part is fixed) was implemented and **certified exactly** (rational Routh test of the 4 Kharitonov corners; rational Sturm counts on [0, ∞) for all 4 pairings) on 236/236 boxes: 200 random near-boundary (ε ∈ [1e-4, 0.3]), 12 adversarial lightly damped, 24 with degenerate intervals; Prop. 4.1 contact/root-location diagnostics pass at 50 digits; no formula discrepancy. n = 5 (non-constructive theorem): an LP-found numerator was certified exactly on 212/212 boxes. 40 sampled certificates re-verified by a separate code path (sympy root isolation + Hurwitz determinants), 40/40 | Reproduction (instances of the claimed theorems; not a proof) | [`evidence/spotcheck/log.md`](evidence/spotcheck/log.md), [`evidence/spotcheck/independent-recheck.txt`](evidence/spotcheck/independent-recheck.txt) |
| O3 | **Lemma B (all n):** n+1 frequencies at which members of the box are exactly orthogonal to a test polynomial b with alternating orientation ⇒ no common numerator of degree ≤ n. Finite, exactly checkable counterexample format | Certification (proof; Codex: correct, wording fixes applied). Novelty status: unclear — the n = 5 necessary-direction identities are in the quintic manuscript; the converse is an elementary divided-difference/Gordan argument | [`work/theory.md`](work/theory.md) |
| O4 | **Lemma C, Lemma F, Cor. G:** closed-infeasible boxes in the stable closure give counterexamples; a zero-free closed numerator for a strictly larger box gives a strict numerator. The original necessary/sufficient sandwich is now closed by M for n≥3: a nonzero closed numerator suffices, without zero-freeness. | Written proofs; earlier Codex corrections applied; continuation below | [`work/theory.md`](work/theory.md) |
| O5 | **Lemma H, now subsumed by I–J:** the formerly conditional critical-family construction and coprimality are proved for all n ≥ 3. Every failure yields either n+1 finite alternating contacts, or n finite contacts plus positive mass at infinity. The numerator has degree n or n−1 and is Hurwitz apart from a possible simple zero at zero; zero-frequency and infinity cases are retained explicitly. The argument also covers positive-leading nonmonic boxes. | Written proof; no kernel replay; novelty unclear | [`work/theory.md`](work/theory.md), [`evidence/continuation/`](evidence/continuation/) |
| O6 | **Prop. E:** a non-monic box is synthesizable iff its two normalized leading-coefficient faces have a common numerator; the monic n = 5, 6 theorems applied face by face do not give this | Certification; Novelty status unclear | [`work/theory.md`](work/theory.md) |
| O7 | No certified counterexample found: 400 random near-boundary monic boxes per n = 5–8 (0 grid-infeasible); 150 non-monic per n = 3–5 (0); fully-closed marginal boxes n = 5–11 (2000 correlated walk states per n = 7–11): all 632 float-LP negatives and 150 controls re-tested with a 40-digit contact null space and an exhaustive six-chart LP, 782/782 grid-feasible with validated positive-coefficient witnesses; CMA-ES minimization of the closed margin (n = 6–9, 4000 evaluations each) found every evaluated configuration strictly grid-feasible (smallest margin 5.3e-4) | Empirical evidence (grid relaxations; no universal claim) | [`evidence/search/summary.md`](evidence/search/summary.md) |
| O8 | Census of alternation configurations surviving the quintic proof's combinatorial filters (region order + contact multiplicity), reproducing the quintic Table 2 at n = 5: 8 (n=5), 48 (n=6), 207 (n=7), 1128 (n=8), 4176 (n=9) | Empirical (bookkeeping) | [`evidence/search/alternation_census.txt`](evidence/search/alternation_census.txt) |
| O9 | **Theorem K (all orders):** the n−2 nondegenerate fully-closed contact equations have rank exactly n−2, not just numerically observed rank. More generally m distinct nondegenerate closed gaps give m independent equations. The proof is a sign-definite Vandermonde expansion. | Written proof; exact finite identity controls; novelty unclear | [`work/theory.md`](work/theory.md), [`work/continuation_verify.py`](work/continuation_verify.py) |
| O10 | **Lemma L (all orders):** a critical contact's actual denominator quadrant is q−σ, not merely q−σ modulo four. This reduces the regular degree-seven sign/multiplicity census from 207 to **43**; it does not exclude all 43, nor the separately retained endpoint cases. | Written proof + finite exact bookkeeping; not a realizability test | [`evidence/continuation/verification.json`](evidence/continuation/verification.json) |
| O11 | **Exact degree-seven negative control:** a fully-closed coefficient box has a Hurwitz, all-positive degree-seven contact vector with P(--)(2)<0, despite correct minimizing corners, orientations and strictly positive second derivatives at every contact. A different vector is certified closed-SPR on the same box and strict on its half-width stable contraction. | Exact rational Routh/Sturm certification; refutes the universal contact-vector shortcut, not existence of a good vector | [`evidence/continuation/verification.json`](evidence/continuation/verification.json) |
| O12 | **Lemma M (all n≥3):** any nonzero closed numerator for a larger box yields an exact-degree-n strict numerator on every strictly interior robustly Hurwitz box. Possible origin zero and degree loss are repaired simultaneously by β+ε(1+sⁿ). Thus universal nonzero closed feasibility on G's radial stability-boundary boxes is **equivalent** to the monic conjecture; no extra zero-free premise remains. | Written proof; exact degree-seven perturbation controls; novelty unclear; boundary numerator existence remains open | [`work/theory.md`](work/theory.md), [`evidence/continuation/`](evidence/continuation/) |

Audit of strong words: nothing here is claimed as *new*, *first* or *optimal*. The all-order
claims are complete written proofs in `work/theory.md`, with independent-model review recorded
in the evidence directories; they are **not kernel-checked proofs**. *Exact* computational
claims refer to rational arithmetic on the explicitly recorded finite inputs, not to a general
proof obtained by sampling.

## 6. Exact remaining blocker

For every n ≥ 7, exclude **both** support alternatives of Theorem J, or realize one in a
robustly Hurwitz box with an exact positive dependence certificate. The critical construction,
coprimality and numerator-degree classification are no longer missing prerequisites. What remains
is the substantive uniform exclusion: n+1 finite contacts (possibly including zero, with numerator
degree n or n−1), and n finite contacts plus infinity (degree n−1). Theorem J's parity restriction
does not eliminate every endpoint case.

Lemma L forbids false phase wraps and leaves 43 regular degree-seven configurations rather than
207; an explicit degree-seven pattern with **both zero and infinity** still passes the stronger
ordering and multiplicity filters. None of these combinatorial survivors is a constructed box.
The quintic shared-component comparisons and the sextic cubic/quadratic construction do not yet
supply the missing all-order inequality.

The alternative boundary route now has both an exact rank theorem and an exact closed-to-strict
transfer. M removes the zero-free gap: the original monic problem is equivalent to nonzero closed
feasibility for **every radial first-stability-boundary box**. Fully-closed nondegenerate boxes
leave a three-dimensional contact kernel, but this class alone does not exhaust that quantifier.
The remaining obligation is a uniform nonnegative-pairing vector, including partial-gap,
zero-constant and collapsed boundary strata. O11 disproves “choose any Hurwitz positive-coefficient
contact vector,” even after local contact orientation/curvature checks. A genuine global positivity
mechanism, not more random samples or a numerical rank test, is required. **No original-question
proof or counterexample has been obtained.**

## 7. Codex referee (gpt-6.1-sol, effort max, read-only)

Round 1 ([prompt](evidence/codex/referee1.prompt.md), [reply](evidence/codex/referee1.reply.json)),
overall "flawed"; resolution of each point:
- C1 status: correct-with-fixes — wording changed to "announced … builds not reproduced"; static
  scan described as finding no proof-bypass declarations, not as a kernel audit.
- C2 Lemma B: proof correct; the ±90° reading is now restricted to positive nodes and Remark (3)
  replaced by the correct counting remark; necessity explicitly not claimed.
- C3 Lemma C: correct; the consequence now requires the box to lie in the closure of stable boxes and
  certified (not floating-point) infeasibility.
- C4 Prop. D: **wrong as first stated** (band alternation without the sign conditions does not imply
  stability: (s − 1)^6); fixed by adding the Hermite–Biehler sign conditions, restricting to the
  nondegenerate fully-closed class, marking the contact rank as numerically checked only, and
  correcting the n = 6 identification (odd endpoints are positive multiples of U, V).
- C5 Prop. E: correct-with-fixes — faces defined explicitly; the stability argument on intermediate
  faces added.
- C6 numerics: overclaims removed. In response, all 632 negative float-LP cases (not only 40) were
  re-tested, with the exhaustive six-chart LP the referee proposed and witness validation; the text
  now says the multiprecision part is the reconstruction and null space, the LP is double precision.
- Extra finding (solver status/zero-margin semantics): addressed by the six-chart decision procedure
  and outcome labels in `work/closed_recheck.py`; zero LP margins are no longer read as certificates.

Round 2 on the new Lemma F, Cor. G, Lemma H and revised Prop. D
([prompt](evidence/codex/referee2.prompt.md), [reply](evidence/codex/referee2.reply.json)), overall
"correct-with-fixes": F's origin step used an unstated sign assumption (counterexample supplied by
the referee) — replaced by the nonzero-gradient argument at t = 0, degree raising made explicit; G's
radius bounds and nesting justified; H's proportionality constant κ is arbitrary (fixed: c = sgn κ,
λ_i = |κ||η_i|/μ_i) and its final reduction now qualified to the cases it covers; D: correct.

### 7.1 Continuation: independent Claude hostile review

Three scoped, context-only CLI reviews used the other vendor's registry-selected
`claude-opus-5-5`, effort `max`; actual model identity and successful exit receipts are retained.
Tools and further delegation were disabled. The reviewed source snapshots, commands, complete
outputs and per-finding dispositions are in
[`evidence/continuation/`](evidence/continuation/), especially
[`review-resolution.json`](evidence/continuation/review-resolution.json).

- **I–K:** “ACCEPT WITH MINOR REVISIONS.” Added the leading-moment identity, explicit component
  simplicity calculation, precise partial-gap hypotheses and first-failure scope.
- **L and degree-seven control:** “ACCEPT_WITH_CORRECTIONS.” Corrected the endpoint survivor's
  corner tally to **1,2,2,1**; the filter's maximum-count logic was already correct. Added an explicit
  false-wrap witness and exact local-contact diagnostics. The control refutes a proposed universal
  implication, not existence of a good numerator.
- **M and monic boundary equivalence:** “ACCEPT_WITH_MINOR_REVISIONS,” using the separately proved
  I(1), C and G. Made containment and nonmonic hypotheses explicit and defined the monic radial
  boundary class. The reviewer confirmed the uniform ε(1+sⁿ) perturbation and exact-degree claim;
  no existence or novelty conclusion follows.

After these repairs, the decisive exact verifier ran **once** and passed: **85** moment identities,
**37** sign-definite determinant controls, **3** dropped-hypothesis controls, the degree-seven
Routh/Sturm/contact certificates, the 207→43 phase census, and **2** origin/degree-loss transfer
controls. The command is retained in
[`verification-command.json`](evidence/continuation/verification-command.json).
These are exact finite checks plus independently model-reviewed written proofs—not a Lean replay.

## 8. Ranked next actions

1. Find an all-order inequality excluding the projective alternatives in J, using L's actual
   phase indices. At degree seven the regular cases number 43, and endpoint cases must be treated
   separately rather than discarded. The missing obligation is realizability/exclusion, not another
   first-failure or coprimality argument.
2. Construct a nonnegative-pairing vector in K's three-dimensional fully-closed contact kernel.
   The exact degree-seven positive and negative controls distinguish the desired property from
   Hurwitzness, coefficient positivity and contact interpolation.
3. Extend a successful construction to every radial boundary stratum, including partial-gap and
   collapsed limits. M already supplies strict interior synthesis from any nonzero closed numerator;
   K handles rank only for distinct nondegenerate contacts, not coincident-contact limits.
4. When disk permits, independently replay the public n=5,6 Lean builds to strengthen their prior
   work status. This is separate from the unsolved n≥7 problem and was not performed here.

## 9. Reproduction

Python 3.14.3 with pinned packages in [`work/requirements.txt`](work/requirements.txt); venv at
`/Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/venv`
(`uv venv … && uv pip install -r work/requirements.txt`). Run from `work/` with `PYTHONPATH=.` and
`python` = that venv's interpreter; `$R` = `/Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/runs`
holds the bulky run outputs (rebuildable from the commands below; seeds fixed).
All computations here are exploratory falsification and spot-checks; no frozen pre-registered
campaign (scripts/campaign.py) was run, so no campaign-level claim is made. Scratch also holds the
two Lean clones (re-create with `work/lean_static_audit.sh`, which clones at the pinned commits) and
the downloaded PDFs (URLs and SHA-256 in `sources/references.md`).

| What | Command (from `work/`) | Output |
|---|---|---|
| Lean static audit | `bash lean_static_audit.sh > ../evidence/lean-static-audit.txt` | evidence/lean-static-audit.txt |
| Exact verifier self-test (31 tests incl. negative controls) | `python exact_verify.py` | evidence/spotcheck/self-test.json |
| n = 5, 6 spot-checks | invocation (from the repository root, single-thread env) in [`evidence/spotcheck/log.md`](evidence/spotcheck/log.md): `python information-science/robust-spr-interval-synthesis/work/spotcheck.py --random-count 200 --degenerate-count 24 --adversarial-count 12 --seed 20261014 --prefix spotcheck` | evidence/spotcheck/ |
| Independent re-verification | `python independent_recheck.py ../evidence/spotcheck/spotcheck-n6-cases.jsonl 20 99` (and n5) | evidence/spotcheck/independent-recheck.txt |
| Random near-boundary search | `python search_random.py N 400 20000 $R/rand400v2_nN.jsonl 4` | evidence/search/summary.md (S1) |
| Boundary ε-scans | `python eps_scan.py N SEED` | S2 |
| Non-monic search | `python search_nonmonic.py N 150 500 $R/nonmonic_nN.jsonl 1` | S3 |
| Fully-closed walks | `python closed_mcmc.py N 20000 101 $R/closed_mcmc_big_nN.jsonl 10` | S4 |
| Multiprecision six-chart re-test | `python closed_recheck.py $R/recheck_list.txt $R/recheck_out.jsonl 4 40`; the list = every record with s < 0 in `closed_mcmc_big_n{10,11}.jsonl` plus 30 records with s ≥ 0 per n = 7..11 drawn with `random.Random(7).sample` | S4 |
| Closed-margin CMA-ES | `python closed_opt.py N 1 4000 $R/closed_opt_nN_s1.json` | S4 |
| Alternation census | `python enumerate_configs.py 9` | evidence/search/alternation_census.txt |
| Continuation exact controls (I–M, degree seven) | `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python continuation_verify.py --output ../evidence/continuation/verification.json` | exact moments/minors, Routh/Sturm and local-contact certificates, phase census, origin/degree-loss perturbations; not a universal proof replay |

Codex referee runs: `codex exec -m gpt-6.1-sol -c model_reasoning_effort=max --sandbox read-only
--ephemeral --skip-git-repo-check -C <this folder> --output-schema evidence/codex/referee1.schema.json
-o evidence/codex/refereeK.reply.json "$(cat evidence/codex/refereeK.prompt.md)" </dev/null`.
