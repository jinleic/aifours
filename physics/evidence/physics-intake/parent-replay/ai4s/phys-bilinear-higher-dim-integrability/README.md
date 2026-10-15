# phys-bilinear-higher-dim-integrability

Book problem: 关于得到高维可积模型的一个新猜想 / "On a new conjecture to find higher-dimensional integrable
models", Lou Senyue and Li Jinhua (Ningbo University), 《10000个科学难题·物理学卷》 (Science Press, 2009),
book pp. 350–351 (PDF pp. 383–384).

## Summary of the book problem

Lou and Li conjecture a "holographic" route from (1+1)-dimensional to higher-dimensional integrable models in
Hirota's bilinear formalism: if the bilinear system `P(D_x, D_t)F·G = 0, Q(D_x)P(D_x, D_t)F·G = 0` is
integrable, then `P(D_x, D_t)F·G = 0, R(S)P(D_x, D_t)F·G = 0` may be integrable, where S is the Hirota
operator of an extra (continuous, discrete, supersymmetric or q-deformed) variable and R is a polynomial,
often of the same form as Q. The printed `D_c` in the second system is a typo for `D_t` (STATUS.md §1). The
book asks how to prove the conjecture, how to determine R(S), and which extra conditions make it true if it is
false. The cited source (Li & Lou, Chin. Phys. B 17, 747 (2008)) proves three examples by symmetry methods
and leaves open whether `(D_t + D_x^n)F·G = 0, D_y(D_t + D_x^n)F·G = 0` is integrable for other n. Its n = 3
model coincides with a bilinear pair found by Hietarinta (1987); Peng et al. (2008) report Wronskian
N-solitons and a Lax pair for a case of Hietarinta's pair, presumably this one (STATUS.md).

## Formulations attacked

"Integrable" is made checkable as Hirota's multi-soliton property (RESULTS.md §0):

- **(R-sys)**, literal: with Q = D_x, R = D_y (any linear Q, R reduces to this), if the two-function system (1)
  passes the generic N-soliton test (all one-soliton seeds, independent amplitudes in F and G), so does (2).
  Studied in the class 𝒫: `P = D_t + p(D_x)`, `p(0) = 0`, `deg p ≥ 2`, which contains Li & Lou's family.
- **(R-eq)**, single-function: the F = G reduction, `Q(D_x)P f·f = 0` integrable ⇒ `Q(D_y)P f·f = 0`
  integrable (P, Q odd).

Not covered: models whose integrability is invisible to exponential solitons (e.g. `P = D_x D_t`),
supersymmetric and q-deformed S.

## Verdict

**SOLVED** for the approved all-N odd-cubic Pfaffian subproblem (Theorem 9.1).
The unrestricted book conjecture remains **PARTIAL**; its single-function generic-Hirota-property
reading has a **COUNTEREXAMPLE**. FRONTIER: DELIVERY-READY for the scoped Certification,
NOVELTY-UNCLEAR for prior-art positioning.

- In 𝒫 the literal conjecture holds at the three-soliton level: (1) passes the generic three-soliton test ⇔
  (2) passes it ⇔ `deg p ≤ 3` (Theorem 4.4). In particular Li & Lou's system passes only for n = 2, 3; for
  n ≥ 4 it fails the generic test (the F F G soliton pattern has no solution of Hirota form), although some
  restricted families, e.g. linear superpositions with G = 1, always exist. The same classification holds
  with the discrete operator `R(S) = sinh(D_n)` (Proposition 7.1).
- The single-function reading is false: `D_x(D_t + D_x^5) f·f = 0` (Sawada–Kotera) is integrable, but
  `D_y(D_t + D_x^5) f·f = 0` fails Hirota's three-soliton condition; the obstruction (proportional to `c5`) is
  computed exactly and reproduces the constraint found by Wang et al. (2024).
- The odd-cubic all-N gap is now closed: Theorem 9.1 proves C6's Pfaffian formula for
  every finite N, arbitrary independent `a_i,b_i` including zero amplitudes, and
  `P=Dt+c1Dx+c3Dx³`, `c3≠0`. Only the pair-sum denominators `k_i+k_j` and `l_i+l_j`
  must be nonzero. The proof is a finite-dimensional Pfaffian/Pluecker argument,
  not extrapolation from the old N≤7 checks.
- The diagonal specialization `l_i=k_i` gives the (1+1)-dimensional system; thus
  the all-N implication holds in this approved odd-cubic class. It is not a
  full proof for arbitrary P,Q,S or a claim that failure of a soliton test excludes Lax integrability.
- Peng et al.'s full text could not be reached through journal, API or archive routes.
  The source-access log and exact Hietarinta equation dictionary are in STATUS.md §6.
  No novelty or certified-scientific-openness claim is made.

## File map

| Path | Content |
|---|---|
| `source/problem.zh.txt` | Book excerpt (pdftotext, unedited) |
| `source/loulipage-383.png`, `source/loulipage-384.png` | Rendered book pages (formulas, `D_c` typo) |
| `STATUS.md` | Literature status, primary sources, what is open, baseline |
| `RESULTS.md` | Precise definitions, claims C1–C8 with proofs, labels, review dispositions |
| `code/hirota_ns.py` | Exact engine: exponential coefficients, two-function recursion, Hirota product ansatz |
| `code/two_function_3ss.py` | C3, C4: cubic class passes; F F G lemma; monomials `d ≥ 4`; lower-order terms |
| `code/single_function_3ss.py` | C5: Sawada–Kotera vs `D_y(D_t + c1D_x + c3D_x^3 + c5D_x^5)` (symbolic, ~9 min) |
| `code/direct_substitution_check.py` | C5 independent check by sympy differentiation (no engine) |
| `code/n_soliton_checks.py` | C6: N = 4, 5 exact sample points; Pfaffian closed form vs recursion (N ≤ 7); `--symbolic N` closed-form identity |
| `code/discrete_variant.py` | C7: `R(S) = sinh(D_n)` |
| `code/exploratory_scan.py` | C8: floating-point scan outside 𝒫 (Empirical) |
| `results/*.json` | Outputs of the scripts above |
| `review/` | Codex review prompts and outputs (round 1: `codex-prompt.md`/`codex-review.md`; round 2: `*-2.md`) |

## Reproduction

Python: `/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python` (3.13, sympy 1.14, mpmath). From
`code/`:

    PY=/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python
    $PY two_function_3ss.py            # C3, C4  (~12 s)
    $PY single_function_3ss.py         # C5      (~9 min)
    $PY direct_substitution_check.py   # C5 independent check (~1 s)
    $PY discrete_variant.py            # C7      (~7 s)
    $PY n_soliton_checks.py            # C6 exact sample points + Pfaffian closed form (~3 s)
    $PY n_soliton_checks.py --symbolic 3   # C6 symbolic closed-form identity, N = 3 (<1 s); N = 4 did not finish in 40 min
    $PY exploratory_scan.py            # C8      (~5 s)

All scripts are deterministic (fixed seeds, exact arithmetic except C8).

## Approved scoped target: all-N odd-cubic Pfaffians

The user approved choosing precise open subproblems. This continuation fixes the
statement to the C6 formula alone; `RESULTS.md` C9 supplies the complete proof,
zero-amplitude polynomial continuation, every denominator condition, the block-Pfaffian
coefficient dictionary, and the reductions. Old finite checks and stopped expansions
are preserved in C6 as historical evidence. Mixed parity and shared workspace indexes
are outside this worker's scope.

**One-command replay from this folder:**

    /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python -B code/all_n_pfaffian.py

Observed: dimension-independent reduction to the four-border Pluecker identity;
10 exact matrix controls (including singular matrices); 28 exact controls for N=0..6
with zero amplitudes, zero individual wave numbers and the diagonal reduction; both
Hirota residuals vanish coefficientwise and block F,G,G_y agree.
The universal quantifier comes from the written proof, not these finite controls.
No Lean/kernel verification is claimed.

New artifacts:

- `code/all_n_pfaffian.py`, `results/all_n_pfaffian.json`: new independent replay,
  without modifying or importing the shared Hirota engine.
- `results/all_n_prior_art_access.json`, `source/hietarinta-9708006.txt`: primary
  comparison and explicit limitation on Peng et al.'s unavailable full text.
- `review/codex-all-n-prompt.md`, `review/all-n-snapshot/`: pinned all-N review
  input; final outcome/dispositions are recorded in RESULTS.md §9.6.

Independent hostile Codex review (`review/codex-all-n-review.md`) found no mathematical
error or remaining proof gap in the approved all-N statement. The review verifies
the signs, minor-summation dictionary, zero-amplitude continuation, and both coupled
equations. It does not certify novelty or supply the missing Peng full-text comparison.
