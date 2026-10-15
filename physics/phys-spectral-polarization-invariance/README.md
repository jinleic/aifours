# Spectrum and polarization invariance in light propagation

**Openness gate (final, 2026-10-14): NO-SETTLING-SOURCE-AMONG-CHECKED.** C8 was **previously unproved in this project**; historical openness remains uncertified. Substantial antecedents were found, and relevant full texts—including Li (2015)—remain inaccessible. The scoped SOLVED label below certifies the project's written proof, **not** admission as a verified historically unsolved problem. See the final per-source table and access record in `STATUS.md`.


Zhao Daomu's problem in *10000 Selected Problems in Sciences: Physics* (Science Press, 2009), pp. 333–334, asks for general conditions under which propagation preserves the normalized optical spectrum, the local spectral degree of polarization, or both, and how those conditions depend on the source and environment. These are different observables: the spectrum depends on the trace of a local coherency matrix; polarization also depends on its eigenvalue ratio. The book's description of Wolf (2007) as a necessary condition is stronger than the paper's own abstract, which explicitly states **sufficiency** and **far-zone** hypotheses.

**Verdict: PARTIAL.** **FRONTIER state: NOVELTY-UNCLEAR** for the optical synthesis of established mathematical ingredients; the original unrestricted book goal remains **OPEN-BLOCKED / PROOF-OBLIGATION in this project**. No current primary source was verified declaring the entire chapter an unsolved theorem, and its selection as “not too hard” is not justified. Several broad subclasses are already solved in the literature. No claim to a complete book solution or scientific priority is made.

## Approved scoped target (2026-10-14)

**Scoped verdict: SOLVED. Correctness state: DELIVERY-READY. Scientific novelty: NOVELTY-UNCLEAR.** The user-approved target fixes one frequency, a common waist, and four Laguerre–Gaussian spatial modes with radial indices `n=0,1` and azimuthal orders `+m,-m`, for any integer `m>=1`. With no cross-azimuthal-sector covariance, **all** PSD within-sector covariances having one local degree at every illuminated point for **every forward full-plane scalar Fresnel distance** are classified in `RESULTS.md` C8. The sum of the two sector blocks must be trace-whitened replacement, depolarizing, or transpose-depolarizing; any PSD split of such a sum is allowed. Forward radial responses are not projectively dense, but their attained open set forces the required quartic identity. This is genuine Fresnel necessity for the approved class, not global all-probe necessity. The same class is characterized for every centered lossless isotropic real ABCD system. Exact identities and 42 physical propagation cases passed; the independent referee found the theorem correct with no remaining scoped proof obligation. The original unrestricted book problem remains PARTIAL.

## Precisely addressed

1. An inverse-Fourier necessary-and-sufficient condition for normalized-spectrum invariance over the **entire ideal paraxial far-zone angular plane**, expressed in the source's midpoint-integrated trace correlation. This does not impose a Schell-model assumption.
2. A **stronger-invariance-requirement partial lemma**: classification of every finite-spatial-mode positive source whose local degree is the same under **every deterministic polarization-independent scalar linear probe**. Besides factorized sources, there are two-spatial-mode depolarizing/transpose-depolarizing families. This is **not a necessary condition for Fresnel-only invariance**.
3. A necessary-and-sufficient factorization condition when the invariance must survive **every incoherent mixture of scalar probes**. This includes a precise explanation of why a deterministic invariant family need not remain invariant after averaging a random medium.
4. Explicit finite-energy counterexamples to either invariance implying the other, and a joint-invariance criterion for matched achromatic probes. Fresnel/ABCD and random-kernel numerical controls are included; full Maxwell vector propagation is not silently identified with scalar propagation.
5. A physical **counterexample to that quantifier transfer**: a positive trace-support-rank-four source has degree exactly `1/2` at every illuminated point at every Fresnel distance, but an allowed scalar mode projector produces degree `1`. Its proof uses the established degeneracy of opposite azimuthal orders; it is not claimed novel.

## Files

- [source/problem.zh.txt](source/problem.zh.txt): supplied, unedited book excerpt.
- [STATUS.md](STATUS.md): dated primary-source survey, scope distinctions, baseline, remaining gap.
- [RESULTS.md](RESULTS.md): complete arguments, evidence labels, numerical results and review dispositions.
- `code/verify.py`: deterministic exact identities and independent numerical propagation checks.
- `results/verification.json`: replay output, fixed parameters and dependency versions.
- `code/fresnel_only.py`, `results/fresnel-only.json`: exact rank/orthogonality and independent 2D FFT/Hankel checks for the physical bridge counterexample.
- `code/lg_fresnel_classification.py`, `results/lg-fresnel-classification.json`: approved scoped theorem's exact arbitrary-`m` identities, seven PSD families/dark and negative controls, and physical 2D propagation checks.
- `results/literature-evidence.json`: checked primary excerpts and explicit access limits.
- `review/codex-prompt.md`, `review/codex-review.md`: independent hostile-referee request and response.
- `review/fresnel-bridge-prompt.md`, `review/fresnel-bridge-review.md`: separate hostile review of the physical counterexample.
- `review/receipt.json`: historical first-phase reviewer identities, exit codes and artifact hashes; subsequent scoped-target documentation revisions are not covered by that earlier receipt.
- `review/lg-fresnel-prompt.md`, `review/lg-fresnel-review.md`, `review/lg-fresnel-receipt.json`: independent review and evidence for the approved scoped theorem.
- `results/openness-gate-access.json`, `review/openness-literature-audits.json`: legitimate retrieval attempts and two read-only primary-literature audits for the final openness gate. The earlier review receipts are proof-delivery snapshots and predate this gate.

## Reproduce

From this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify.py && \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/fresnel_only.py && \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/lg_fresnel_classification.py
```

The written mathematical proofs, not numerical agreement, carry the universal quantifiers. The script certifies symbolic/rational sub-identities and exercises independent propagation controls. Its finite-grid floating-point results are explicitly **Empirical evidence**.
