# Robust SPR synthesis at degree seven and beyond (six-lane info-2)

Lane owner: worker `InfoRobustSpr`. Started 2026-10-16 18:35 PDT (first source-file mtime). Contract:
`institute/runs/six-lane-2026-10-16/contract.json` (lane `info-2`). Prior dossier (read-only):
`information-science/robust-spr-interval-synthesis/` (README, `work/theory.md`, evidence).
All times Pacific. This file is the frozen pre-statement; later sections are append-only checkpoints.

## 1. Frozen target (2026-10-16 PDT, written before any new computation; clock time not recorded)

Monic box of degree n: K = {s^n + a_1 s^(n-1) + ... + a_n : l_i <= a_i <= u_i}, l_i <= u_i real
(degenerate intervals allowed). Robustly Hurwitz: every member has all roots in Re s < 0.

* **T7 (specialist theorem, affirmative):** every robustly Hurwitz monic box of degree 7 admits a real
  b with deg b = 7 exactly and Re(b(iw)/a(iw)) > 0 for every real w and every a in K.
* **R (refutation of the book conjecture):** an explicit monic box of some degree n >= 7 with
  rational endpoints, robustly Hurwitz by an exact certificate (rational Routh/Hurwitz test of the four
  Kharitonov corners), together with an exact finite positive-dependence certificate that no real
  numerator of exact degree n exists (prior Lemma B data, or Theorem J alternative (B) data).

Not the target: numerical/random-box evidence, two-parameter or other special subfamilies proved
affirmatively, fully-closed-only statements, the nonmonic variant. Degree 7 alone would be a scoped
specialist theorem, not resolution of the all-n book question.

## 2. Primary-status recheck (2026-10-16 PDT; sources fetched 18:35 PDT per file mtime)

| Item | Finding | Evidence |
|---|---|---|
| Quintic (n=5) | `dgjszy/quintic-spr-proof` gained commits today (5d9f2c2, ebc7750: paper PDFs added/Chinese removed). The repo PDF `quintic-spr-paper/QuinticSPR-English.pdf` is a recompile (xdvipdfmx 20260317, created 2026-10-16 03:47 PDT) whose `pdftotext -layout` text is byte-identical to the 2026-10-06 release asset. No new mathematical content. Open issue #1 (2026-10-15) asks where the paper is published; no answer. | `sources/QuinticSPR-English.{release-2026-10-06,repo-ebc77505c7}.pdf`, `evidence/quintic-{release,repo}.txt` |
| Sextic (n=6) | arXiv:2609.26541 still v2 (23 Sep 2026); sha256 unchanged (1e448014...). | `sources/arxiv-2609.26541v2.pdf` |
| n >= 7 | arXiv API searches (author names Yu/Xu/Dou; "positive real" AND interval AND polynomial) and two web searches: no interval-family theorem or counterexample for n >= 7. The authors' `nth-order-spr-proof` project remains non-public. A search miss is not evidence of absence. | this table |
| Segments, all n | Yu-Wang arXiv:math/0210452 (2002) read: segment theorem, sketchy "lengthy calculation" induction; does not address boxes. | `sources/arxiv-math-0210452.pdf`, `evidence/segment-0210452.txt` |

Status (2026-10-16 PDT): **no general n >= 7 theorem or counterexample located in the checked primary
sources; uncertified-open** (monic, exact-degree numerator, strict SPR). This is a statement about the
sources searched, not certainty about priority.

## 3. Baseline (matched, read-only)

Prior dossier written proofs: A (four-corner), B (alternation certificate), C (closed limit),
I (weak-numerator rigidity), J (critical certificate: n+1 alternating finite contacts, or n finite +
infinity), K (contact rank), L (unwrapped phase; 207 -> 43 regular n=7 configurations), M (closed to
strict transfer; conjecture_n <=> every radial first-boundary box has a nonzero closed numerator).
Exact control O11: a Hurwitz positive-coefficient contact-kernel vector can fail globally.
Exhausted (do not repeat without new representation): random near-boundary boxes n=5..8, fully-closed
walks n=5..11, CMA-ES on the fully-closed 3-dim closed margin n=6..9, alternation census.

## 4. Frozen attack protocol

A1 (new representation, counterexample side). Dual/certificate-space search: by Lemma B and
Theorem J, conjecture_n fails iff some alternating-orthogonal configuration (test polynomial b,
nodes, members a_i with a_i(iw_i) a positive multiple of -/+ i b(iw_i), alternating) has a robustly
Hurwitz bounding box. Objective: radial stability factor of the bounding box (computed by exact
zero-exclusion formula, float for search). Calibrate on n=5,6 (claimed theorems: no factor > 1 may
appear; any > 1 is a bug or a counterexample to a 2026 claim), then n=7,8. Any candidate > 1 must be
re-derived in exact rational arithmetic (Routh of 4 corners; exact (B1) proportionality; alternation
signs), with mutation controls (flip one orientation, move one node, perturb one endpoint).
Budget: <= 4 worker processes, chunks <= 30 min between checkpoints, fixed seeds recorded.

A2 (new mechanism, proof side). Exploit fully-closed chain structure: on each interior band the
SPR corridor is bounded exactly by the phases of the two touching corners' stable cofactors, so the
closed problem is a chain of fixed-component two-corner problems linked by pinned phases. Seek a
uniform construction or induction; any claimed lemma gets an exact finite control and, if central,
an independent cross-vendor review.

A3 (exclusion side, degree seven). Generalize the quintic shared-component value-ratio exclusions
(quintic Lemmas 5.3, 6.1, Props 6.2-6.4) to the 43 regular degree-seven configurations and the
endpoint cases, tracking exactly which configurations each lemma removes.

Evidence labels kept separate: written proof / exact finite certificate / numerical / literature.
UNKNOWN or timeouts are never infeasibility; samples are never universal claims.

## 5. Checkpoints (append-only)

### C1 (README mtime 2026-10-16 19:13:59 PDT; an earlier "~20:30" label was a guess, corrected)

* Lane env: `code/venv` (uv, Python 3.14.3; numpy 2.5.4, scipy 1.18.1, sympy 1.14.0,
  mpmath 1.3.0, python-flint 0.9.0, cma 4.5.0); uv cache inside `code/env-cache`.
* Census regenerated (`code/census7.py`, `evidence/census7_regular.json`): 43 regular n=7
  configurations. Structural observation: in 41/43 the 8 nodes form (-,+) pairs inside
  consecutive denominator bands (regions 2k+1), i.e. "partial chains" of the fully-closed
  binding structure; the corners in a pair share one component.
* Fully-closed binding structure (written derivation, float-checked): on every interior band the
  extreme-angle corners are exactly the two touching corners at its ends, and the SPR corridor on
  that band is (phase of left cofactor + pi/2, phase of right cofactor + pi/2); for n=7 the binding
  sets are (+-): [0,x2] u [x4,inf), (-+): [0,x0] u [x2,x4] u [x6,inf), (++): [x1,x3] u [x5,x6],
  (--): [x0,x1] u [x3,x5].
* Gauge symmetry used for searches: scaling all EVEN coefficients of the box by l>0 (numerator
  even part by 1/l) preserves stability, box structure and the SPR problem; with frequency
  scaling this removes two parameters.
* **G1 exact structural control (not a book counterexample):** generalized fully-closed rectangle
  families at n=6 whose widths are >= 0 on [0,inf) but have negative t-coefficients have NO
  nonzero closed numerator. Two rational instances certified exactly (`code/closed_exact.py`:
  exact 3-dim contact kernel, exact residual division, 4 support points with exact positive
  weights summing the residual functionals to zero, rank 3): `evidence/genrect/cert_n6_gen_s21.json`,
  `cert_n6_gen_s22.json` (W_E, W_O nonneg on the half-line by exact factor/Sturm check). In both,
  W_E and W_O nearly have a double root inside a cluster of band points. Since monic sextic interval
  boxes are claimed synthesizable (arXiv:2609.26541), pointwise width nonnegativity plus
  Kharitonov-corner stability is NOT sufficient: any proof must use the nonnegative-coefficient
  (monotone) width structure. Pending: explicit stable shrunken family + strict certificate.
* Float artifact caught: a sphere-sampling max-min margin gave false negative values; replaced by
  the homogeneous LP margin (`fclosed.lp_margin`, >= 0 by construction) plus an LP Farkas residual.
  Earlier negative "margins" (files g1_*) are void; positive ones remain valid lower bounds.

### C2 (written 2026-10-16 ~19:35 PDT, host clock checked 19:33:15)

* **G1 strict (exact):** shrinking the s21 generalized family toward its centre by 999/1000 gives a
  family whose four corners pass the exact Routh test, widths still >= 0 on [0,inf) with negative
  t-coefficients, and an exact 8-point positive dependence sum mu_k F(c_k,t_k) = 0 (rational t_k,
  nullspace dimension 1, all weights > 0): no real numerator of ANY degree <= 6 is SPR for the
  family (`code/strict_exact.py`, `evidence/genrect/strict_n6_gen_s21_lam999_1000.json`). At
  factors 99/100 and 9/10 the float dual residual is positive (no certificate), as expected from
  Lemma C. Mechanism for the n=6 sextic proof: the G1 family violates exactly its inequalities
  sigma = w2 + 2 a w1 >= 0 (= W_E'(x_0) >= 0) and m <= M (disc O+ <= disc O-), which boxes satisfy.
* Prior-art name/full-text check requested by parent (2026-10-16 19:29 PDT): EulerSolve
  `papers/` index (419063 bytes, `sources/eulersolve-papers.html`): 0 hits for SPR, Kharitonov,
  "interval polynomial", "positive real" (only "Positive Reals" in an unrelated Erdős title).
  Zenodo API: "strictly positive real" 9 records, none on interval synthesis (2016 survey only);
  "interval polynomial" AND "positive real" 0. openai/math GitHub code search: Kharitonov 0,
  "positive realness" 0, "strictly positive real" 9 generic hits, "interval polynomial" 5
  unrelated certificate files; further queries hit the API rate limit (not run). A miss is not
  evidence of absence.

### C3 (clock time not recorded; written before the 21:23 PDT host check — earlier "~21:35" label was a guess)

* G1 strict family now also certified robustly stable by exact zero exclusion (arb root enclosures,
  Sturm root counts: E- and O-bands strictly disjoint and alternating EOEOE) in addition to exact
  corner Routh tests (`strict_exact.bands_disjoint_exact`; file sha256 7af79af8...).
* Candidate mechanisms tried and REJECTED (fully-closed n=7):
  (i) pin b's phase at all n band points (E_b(x0)=0, O_b(x6)=0 plus contacts): fails on 36/37
  realizable float samples (`code/canon.py`).
  (ii) Codex delegate proposal E_b in span(E-,E+) (receipt `review/codex-fc7.receipt.json`; model
  gpt-6.1-sol, effort max, read-only, empty workdir; exit code not captured, reply present):
  coincides with my independent construction on the O11 box where it works, but fails on 32/37
  float samples and EXACTLY for both signs on a closed-feasible box (`evidence/canon/case1_box.json`:
  P_{++}(1040/723) < 0 for +b, P_{--}(10^6) < 0 for -b; box closed LP margin 0.138).
  (iii) b = c0' + eps c0 (derivative of the box centre; locally correct at centre resonances):
  fails on 58/60 random n=7 boxes at radial stability factor 1.01 (`code/derivcand.py`).
* Adversarial general-box search (`code/advbox.py`, exact-root stability scaling, bounded
  well-conditioned parameters, signed angular margin delta*, eta = radial slack 0.005; 2 restarts
  x 700 evaluations): min delta* n=5 0.0086, n=6 0.069, n=7 0.029; n=8 one restart flagged
  "grid-infeasible" but this was an LP artefact: on the same box an LP on a slightly different
  adaptive grid gives margin 0.0033 and that numerator is positive on a 2,000,001-point grid
  (min cosine 0.0023). Lesson: HiGHS returned margin 0 / 1e-10 for a feasible problem; every
  infeasibility flag needs an exact dual certificate (none obtained). Earlier advbox runs a1/a2
  were void (grid stability scaling let CMA pick unstable boxes).

### C4 (clock time not recorded; written before the 21:23 PDT host check — earlier "~22:40" label was a guess)

* Fully-closed searches with gauge fixing (the free-lead scale is a symmetry: one lead set to 1)
  and QR-preconditioned LP margins (`code/boxsearch.py`, `fclosed.lp_margin_precond`), CMA-ES,
  12-16 restarts x 1500 evaluations, conditioning penalties:
  box n=6 (random starts, control) min 2.9e-4; box n=7 (67 realizable starts) min 1.9e-3;
  box n=8 min 9.5e-4; "genmono" (W_E, W_O >= 0 AND nondecreasing on [0,inf) — a strict superset of
  boxes for n >= 7) n=7 min 1.5e-3 and 1.7e-3, n=8 min 2.1e-3. No closed-infeasible configuration.
  Earlier near-zero box values were artefacts of an unfixed gauge (free lead pushed to e^20).
* Generalized-mode searches were found to exploit a too-coarse grid test of W >= 0: all 12 n=5
  "gen zeros" (b5) are INVALID (W_E dips below zero between grid points; e.g. exact rationalised
  instance has W_E roots ~1.0148 and ~1.0276). Fixed with critical-point minimisation; re-running.
  G1 at n=6 is unaffected (its W >= 0 was certified exactly by factorisation + Sturm counts).
* Targeted "tight cluster then wide bands" fully-closed n=7 geometries (`code/clusterstarts.py`):
  0 box-realizable configurations in 400000 structured tries. Consistent with the mechanism of G1
  (both widths dipping inside a cluster) being unavailable to boxes: narrow cluster bands force
  W/|E'| small exactly where monotone widths cannot be small after wide low bands.
* Working hypothesis (NOT proved, numerical only): monotone (nondecreasing) widths may be the
  property that makes synthesis hold; pointwise width nonnegativity is not enough (G1).

## 6. Preservation package (host clock 2026-10-16 21:25 PDT)

Replay (exact, ~0.3 s, exit 0): `cd code && OPENBLAS_NUM_THREADS=1 ./venv/bin/python -W ignore
verify_all.py ../evidence/verify_all.json` (output sha256 8aa8b92b41e3...4942; stdout copy
`evidence/verify_all.stdout.txt` sha256 3734908e...6de8; python-flint 0.9.0). Script sha256
6a36629e...4443; `closed_exact.py` 123f5b90...9893; `strict_exact.py` ce213c7f...b885.

**R1 G1-closed (Certification; novelty unclear).** For the rational fully-closed degree-6 rectangle
families `evidence/genrect/spec_n6_gen_s21.json` (sha 167a22c6...) and `spec_n6_gen_s22.json`
(c4e4ddb3...): W_E, W_O >= 0 on [0,inf) (exact factor + Sturm) but each has a negative t-coefficient
(not interval boxes), and every real b, deg b <= 6, with all four corner pairings >= 0 on [0,inf)
is b = 0. Certificates `cert_n6_gen_s21.json` (a5964ee4...), `cert_n6_gen_s22.json` (6da9a42d...):
exact 3-dim contact kernel, exact residual division, 4 support points, exact positive weights,
rank 3. Controls: identity exact; perturbing one weight breaks it; dropping any one point leaves no
positive dependence.

**R2 G1-strict (Certification; structural control, NOT a book counterexample).** Shrinking s21 toward
its centre by 999/1000 gives a robustly Hurwitz family (exact Routh of the four corners; certified
strict E,O,E,O,E band separation) whose widths are >= 0 pointwise but not coefficientwise, and which
admits NO real numerator of any degree <= 6 with Re(b/a) > 0 on iR for all members: exact 8-point
positive dependence, all weights > 0 (`strict_n6_gen_s21_lam999_1000.json`, 7af79af8...).
Controls: weight mutation breaks the identity; positive control: at shrink 9/10 an exact strict
numerator exists (four pairings > 0 on [0,inf) by Sturm, leading coefficient > 0). The near-critical
contact pattern (float, theta* ~ 0.99716, `evidence/genrect/g1_critical.json`) is exactly the n=6
census row kappa=-1, q=0112344, corners -- +- +- ++ -+ -- --: excluding that row for boxes
necessarily uses coefficientwise (monotone) width structure. Monic sextic boxes themselves are
claimed synthesizable (arXiv:2609.26541); R2 shows that claim cannot extend to this generalization.

**R3 refuted numerator mechanisms (exact on one box).** `evidence/canon/case1_box.json`
(7b352485...): rationalised fully-closed n=7 interval box (widths coefficientwise >= 0, exact),
exactly closed-feasible (rational kernel combination, exact residual nonnegativity). On it, both
(i) the Codex-delegate candidate E_b in span(E-,E+) and (ii) the pin-all-band-points candidate give
negative pairings for BOTH signs at rational frequencies (span: (++) at 1394/975, (--) at 10^6;
pin-all: (++) at 505/287, (--) at 10^6). Positive control: the span candidate is an exact closed
numerator on the O11 box. (iii) b = c0' + eps c0: float refutation only (58/60 boxes, factor 1.01).

**Voided float artefacts (retained, not evidence):** V1 sphere-sampling max-min margins (false
negatives; one-sided LP chart). V2 n=5 "gen zeros" incl. `cert_n5_gen_b5.json`,
`cert_n5_gen_s7.json`: W_E dips below zero between grid points (their WE_halfline_nonneg is false).
V3 advbox a1/a2: grid stability scaling admitted unstable boxes. V4 advbox a3 n=8 flag: HiGHS margin
~1e-10 on one grid vs 0.0033 on another; numerator verified on a 2,000,001-point grid. V5 b3
fully-closed near-zero margins: unfixed gauge (free lead driven to e^20). V6 g1/g2 negative or
zero margins at near-singular contact matrices (degenerate configurations).

**Empirical (no universal claim):** no closed-infeasible box or monotone-width (W, W' >= 0)
generalized family found at n = 7, 8 (gauge-fixed, preconditioned CMA, C4); pointwise generalized
families fail at n = 6, 7 in every restart; none found at n = 5 after the V2 fix. Mixed modes
(only one width monotone, `evidence/boxsearch/b7_*`) were launched at ~21:20 PDT; results not yet
read at handoff.

**FRONTIER status.** Full degree-7 target: OPEN — NEEDS-NEW-REPRESENTATION. The missing obligation
is unchanged in kind: a uniform exclusion of the 43 regular + endpoint Theorem-J configurations, or
a uniform closed-numerator construction, that USES coefficientwise/monotone width structure (R2
proves pointwise widths are insufficient). Precise next lemma family (not proved): Monotone-width
hypothesis H_mono — every robustly Hurwitz rectangle family with W_E, W_O nonnegative and
nondecreasing on [0,inf) has a common exact-degree numerator. Route: at Theorem-J contacts,
W_E = (P_{+O} - P_{-O})/E_b and W_O = (P_{E+} - P_{E-})/(t O_b) are expressed through positive
pairing values; for the chain configurations (41/43 regular rows; 37/43 contain a rigid
3-contact corner) derive a forced decrease of W_E or W_O between consecutive contacts. No row has
yet been excluded by this route.

## 7. Continuation after parent replay (host clock 2026-10-16 21:27 PDT onward)

**(1) One-width-monotone searches.** The ~21:20 launch produced no output: the background shell
ended with the tool call, and boxsearch writes only at the end. Relaunched at 21:28 PDT as a
supervised job; finished in 232 s (`evidence/boxsearch/b7_*.json`, 10 restarts x 1500 evaluations).
Float results only: n=6 "genO" (W_O >= 0 pointwise only, W_E nondecreasing) gave margin 0 in 3
restarts; n=6 genE min 2.9e-4; n=7 genE min 1.2e-3; n=7 genO min 1.8e-3. The n=6 genO zeros are
UNVERIFIED: both are valid families (exact: W_E coefficientwise >= 0, W_O >= 0 on [0,inf) with a
negative coefficient), but the exact certifier found no positive dependence on the float support
at denominator limits 1e6 and 1e8 (`evidence/genrect/genO_n6_exact_attempt.json`). They sit at
the conditioning threshold (contact-matrix singular-value ratio ~1e-4; lead ratio ~1.6e5).

**(2) Hypothesis H_mono(n), stated exactly (not proved).** Data: real polynomials E-, E+ of
degree <= floor(n/2) and O-, O+ of degree <= floor((n-1)/2) whose corners
c_xy(s) = E_x(-s^2) + s O_y(-s^2) all have degree n with s^n-coefficient 1. Conditions:
(a) W_E = E+ - E- and W_O = O+ - O- are >= 0 and nondecreasing on the closed half-line [0,inf)
(so W(0) >= 0 and W'(0) >= 0; constant and identically-zero widths are allowed); (b) the polytope
F = conv{c_xy} is robustly Hurwitz. By the band argument of R2, (a) plus four Hurwitz corners
suffices for (b). Claim: there is a real b with deg b = n and Re(b(iw)/a(iw)) > 0 for every real w
and every a in F. A monic interval box satisfies (a), because its widths have nonnegative
coefficients. So H_mono(n) implies the book conjecture at n.

For n <= 6 every width has degree <= 2. A nonnegative, nondecreasing polynomial of degree <= 2 on
[0,inf) has nonnegative coefficients, so for n <= 6 H_mono(n) is exactly the box statement. For
n >= 7 H_mono(n) is strictly stronger: for example, a monotone cubic W_E may have a negative t^2
coefficient. Evidence for H_mono is float only (C4 and (1)); R2 shows that dropping monotonicity of
both widths breaks it at n=6.

**(3) Exclusion attempt: Lemma DL (proved; removes 0 of 43 rows).** Setting: n=7, regular case of
Theorem J. Here b is a weak numerator of exact degree 7; it is Hurwitz, so b_0..b_7 > 0. Each
P_c has degree 7 with leading coefficient b_7 and P_c(0) = b_0 E_c(0).
Call (X,Y) a step pair if Y raises one component of X: (--,+-), (-+,++), (--,-+), (+-,++).

*Statement.* Suppose X and Y both have exactly three positive contacts, with ordered nodes
r_1<r_2<r_3 (for X) and s_1<s_2<s_3 (for Y). Then it is impossible that s_k <= r_k for all k with
at least one strict inequality.

*Proof.* Each corner with three double roots on [0,inf) has the form
P = (b_7 t + d) Q^2 with Q = prod (t - root_k). Here d = P(0)/rho^2 > 0, where rho is the product
of the roots; and [t^6]P = d - 2 b_7 sigma, where sigma is their sum.

For an E-step, D = P_Y - P_X = E_b W_E, so [t^0]D = b_0 W_E(0) >= 0 and
[t^6]D = -b_6 [t^3]W_E <= 0. For an O-step, D = t O_b W_O, so [t^0]D = 0 and
[t^6]D = -b_7 [t^2]W_O <= 0.

Under the forbidden order, rho_Y < rho_X and sigma_Y < sigma_X. Hence
d_Y = P_Y(0)/rho_Y^2 >= P_X(0)/rho_Y^2 > d_X, and
[t^6]D = (d_Y - d_X) - 2 b_7 (sigma_Y - sigma_X) > 0. This contradicts [t^6]D <= 0. QED

*Hypotheses used.* Only the top width coefficients ([t^3]W_E, [t^2]W_O) and W_E(0) must be >= 0.
So DL holds for every pointwise-nonnegative family, and cannot see the G1 mechanism.

*Controls* (`code/lemma_dl.py`, `evidence/lemma_dl.json`):
- the exact coefficient identities hold on 40 random rational instances;
- mutation: with [t^3]W_E < 0 the forbidden order is consistent (rationals given: required
  w3 = -3305/256).

*Bite.* 13 of the 43 rows have two corners with three contacts. In none of them is a step pair
ordered the forbidden way: the census's quadrant-cycle order always places the raised corner's
nodes later. **Removes 0 of 43 rows.**

**(4) Lower-envelope identity (proved; elementary) and the remaining gap.**

*Identity.* For either O-component y, W_E = (P_{+y} - P_{-y})/E_b. Hence
- on {E_b > 0}: W_E <= P_{+y}/E_b, with equality at the (-,y) contacts;
- on {E_b < 0}: W_E <= P_{-y}/|E_b|, with equality at the (+,y) contacts.
The same holds for W_O, with t O_b in place of E_b. So a monotone width must sit below these
positive envelopes and touch them at every contact.

*Gap.* An exclusion needs W at an early contact to be forced above W at a later contact, as
happens in G1. That requires upper bounds on |E_b| or |O_b| and lower bounds on partner pairings
at distant contacts. The rigid factorisations give the pairings up to one constant but not the
values of E_b or O_b, and I found no inequality that closes. No chain-type row is excluded.

**(5) Review.** No lemma excluded any configuration. Per the parent's condition no Codex review was
run; DL's proof and controls are in the files above.

**FRONTIER status unchanged:** degree-7 target OPEN, NEEDS-NEW-REPRESENTATION.

## 8. Review-vendor note (host clock 2026-10-16 21:32 PDT)

Parent notice: the parent orchestrator is now OpenAI gpt-6.1-sol. Historical receipts are kept
unchanged. `review/codex-fc7.receipt.json` records a Codex (OpenAI gpt-6.1-sol) delegate run that was
cross-vendor relative to this Claude-family worker and the then-Claude parent. That delegate's
candidate was refuted exactly (R3). It is not an accepted review.

For any NEW candidate whose hostile review is commissioned from now on, the configured Claude Opus
5.5 (max) delegate is the cross-vendor reviewer relative to the current parent. Codex is then
same-vendor relative to the parent. As of this note there is no new candidate needing review:
Lemma DL removes no configuration, and the degree-7 target remains OPEN.
