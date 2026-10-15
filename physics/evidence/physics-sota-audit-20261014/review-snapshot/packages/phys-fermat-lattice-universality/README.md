# Fermat spirals realize every planar lattice of covolume pi

Snapshot: 2026-10-14 (America/Los_Angeles).

Cao Zexian's chapter “Are the Fibonacci Parastichous Spirals a Least-Energy Configuration on Conical Surface?” in *10000 Selected Problems in Sciences: Physics* (Science Press, 2009), pp. 541–543, asks whether Fibonacci patterns have an energetic/packing explanation and whether chirality alternates as disk size changes. This folder studies a precise asymptotic lattice-realization question in the same phyllotaxis geometry, explicitly left open by Tevet in 2025. It does **not** replace the chapter's unspecified elastic functional or settle its cone-energy or chirality conjectures. The earlier, already-known tail-density law remains separately preserved and is not counted as a discovery.

## Exact target and current verdict

For **every** full-rank lattice `Lambda subset R^2` of covolume **exactly pi**, find **one fixed badly approximable** `alpha` such that the Fermat spiral

`X_alpha={sqrt(n)*exp(2*pi*i*n*alpha): n=1,2,...}`

has `Lambda` as a Chabauty–Fell limit under translations escaping to infinity. No dilation, no post-hoc rotation, no changing `alpha` along the limit, and no unbounded continued-fraction digits are permitted.

**Mathematical verdict: SOLVED for the exact universal statement by the complete classical proof in RESULTS.md.** The proof also gives every rotation and affine translate of a chosen lattice using the same angle. **Evidence: Certification**, not a priority-certified Discovery. **FRONTIER_METHOD: DELIVERY-READY for external mathematical scrutiny; NOVELTY-UNCLEAR for worldwide priority.** The completed Claude referee returned **CORRECT**; Codex returned **CORRECT-WITH-FIXES**, finding no theorem gap and two minor finite-evidence scope issues now clarified. All findings are dispositioned; the finite smoke is not the universal proof.

The primary open statement is Tevet, *Chabauty Limits of Fermat Spirals*, [arXiv:2506.22863v2](https://arxiv.org/pdf/2506.22863v2), Further Questions p. 12:

> whether every lattice with co-volume π is achieved as a Chabauty limit of some Fermat spiral with badly-approximable angle difference remains.

The quote was verified in the latest public preprint. The paper also appeared in *Combinatorics and Number Theory* **14**(3–4), 239–249 (2025), DOI [10.2140/cnt.2025.14.239](https://doi.org/10.2140/cnt.2025.14.239); its subscription-blocked journal body was not compared. STATUS.md separates primary openness evidence, the bounded follow-up screen, indexed-zero results and inaccessible sources. No settling follow-up was located; worldwide priority is not thereby certified.

## Proof and scope

The proof has three substantive bridges:

1. **All target shapes:** a local Möbius relation connects two projection ratios of an arbitrary lattice basis. McMullen's absolute-winning theorem supplies a choice with both ratios badly approximable.
2. **One bounded angle:** an explicit parity-controlled concatenation of reversed/forward continued-fraction prefixes realizes both ratios in a single bounded-digit angle. Exact unimodular convergent bases recover the entire target lattice, not a sublattice.
3. **Translation-only physical limits:** uniform local Taylor bounds transfer model-lattice convergence to the spiral. Sublinear integer windows select arbitrary physical orientation while preserving the local lattice limit; the actual maps remain translations.

The local lattice linearization and area-pi normalization are prior art, notably Bacher (2014); the explicit bounds here are rederived for a self-contained proof. No dense-but-unbounded geodesic, generic ergodicity claim or solver extrapolation is used. The choice of badly approximable ratios is nonconstructive for arbitrary real target data; no effective universal algorithm or target-independent digit bound is asserted.

## One-command finite replay

From this folder:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/universality_smoke.py --write
```

Omit `--write` for the same checks without rewriting the result. No installation is required. Observed runtime: Python 3.13.9, SymPy 1.14.0, mpmath 1.3.0; one core, 2.032 seconds of script time.

Observed output:

```text
PASS: 4 quadratic fixtures; 12 bounded-word convergent bases; fixed infinite alpha cylinders
PASS: 300 forward and 300 reverse spiral-patch checks; 36 phase-window checks
PASS: 3 negative-control families (pi normalization, digit history, index-two basis)
```

The four fixtures are square, rectangular, hexagonal and skew. Their fixed digit bounds are `1,19,10,569`; the bound is allowed to depend on shape. Each uses one exact rational enclosure of its infinite constructed angle at all three pivots. High-precision midpoint evaluations and exact integer/cylinder checks are **finite empirical controls**, not a formal interval certificate or proof-kernel verification. The history mutation is detected on the two nonconstant-period fixtures; constant digit histories are not claimed to distinguish reversal.

The 300 reverse checks are paired recovery checks on the forward samples, not an independent enumeration excluding other points. The receipt field `phase_uncertainty_turns_upper` bounds phases at observation-window centers only, not every patch index or all outputs uniformly across the angle cylinder. The four quadratic fixtures directly supply admissible ratios and bypass the arbitrary-target winning-set selection. The numerical comparisons share SymPy/mpmath arithmetic; the written proof supplies the exhaustive and universal statements.

## Files

- `RESULTS.md`: complete all-target proof, imported hypotheses, frozen finite protocol, execution and review ledger.
- `STATUS.md`: primary open quote, follow-up screen, SOTA and eligibility limits.
- `source/problem.zh.txt`: unchanged excerpt from the physics book intake.
- `source/primary-pins.json`: source URLs, versions, hashes and the short open quote.
- `source/publication-and-index.json`: independently checked journal metadata/access boundary, arXiv version and index counters.
- `source/tevet-2506.22863v2.pdf`, `source/mcmullen-winning.pdf`: public primary manuscripts used by the reviewers.
- `code/universality_smoke.py`: deterministic finite controls, without another project's code.
- `results/smoke.json`: exercised counts, exact angle-enclosing cylinders, digit words, parameter bounds, high-precision observations and runtime versions.
- `review/`: immutable proof snapshot, self-contained prompts, input hashes, untouched completed Claude/Codex reports and streams, and completion receipts.

No bounded-orbit realization lemma remains open in this proof. The next scientific step is independent human mathematical review and lawful comparison with the journal body, not more numerical optimization. Broader physical energy minimization and chirality remain outside the theorem. No formal-kernel verification, submission, external contact or first-result claim is made.
