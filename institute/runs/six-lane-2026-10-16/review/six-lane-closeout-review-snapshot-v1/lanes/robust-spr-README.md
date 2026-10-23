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

### C3 (written 2026-10-16 ~21:35 PDT)

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
