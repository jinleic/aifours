# Expanded information-science search — 2026-10-14

**Outcome:** 51 candidate articles checked; seven proof dossiers completed. No newly established full resolution of a previously open broad book problem. Two principal exact-data readings are answered by classical prior work; precise negative claims about POMDP optimizer existence and joint time–frequency feasibility are completely settled within their stated scope. Novelty is unestablished.

The [shared index](../../README.md#information-science-expanded-search-2026-10-14) routes all seven dossiers. Each owns its book statement, mathematical assumptions, proofs, SOTA and referee dispositions. The earlier five information-science targets and their frozen evidence remain unchanged.

## Strongest scoped result

[Positive time–frequency distributions, Theorem 10](../../positive-tfd-marginals/proof.md#10-a-genuine-fourier-pair-two-convex-orders-and-covariance-are-not-sufficient) gives an explicit zero-free Schwartz signal

\[
s(t)=\pi^{-1/4}e^{-t^2/2}\left(1+\frac{i}{14}(4t^4-12t^2+3)\right).
\]

It is its own unitary Fourier transform. A nonnegative, marginal-correct density realizing its instantaneous frequency exists; separately, one realizing its group delay exists. Nevertheless **no nonnegative joint measure realizes both**. The two separate convex-order tests and covariance identity are therefore insufficient even for actual Fourier data, not merely abstract probability inputs.

The decisive proof combines exact identities, an all-strike convex-order certificate and a rational full-plane dual contradiction. This is a **computer-assisted classical proof**, not Lean/kernel or human-journal certification. It does not classify every Fourier pair or resolve the book's unspecified “physical meaning.”

## Parent-exercised verification

- [Final ledger](parent-verification.json): all seven targets, source/proof/output hashes, limits and completed-job status.
- [Source checks](parent-primary-checks.json): passages actually read by the parent, distinct from worker-only literature checks.
- Fourier result: [256-bit Arb checker replay](positive-tfd-fourier-worker-checker-replay.json), [independent implementation](parent_verify_fourier_obstruction.py), [independent result](positive-tfd-fourier-parent-independent.json), [receipt](positive-tfd-fourier-parent-receipt.json).
- [Geomagnetic reconstruction and recurrence replay](geomagnetic-parent-sanity.json); empirical recovery is not the uniqueness proof.
- [Exact array decision replay](array-parent-check.json) and [independent original-sensor arithmetic](array-shortcut-independent-arithmetic.json).
- POMDP: [exact state-transition smoke](../../average-reward-pomdp-nonattainment/evidence/exact-checks.json), [independent finite-controller enumeration](../../average-reward-pomdp-nonattainment/evidence/finite-controller-parent-check.json), [accepted second referee](../../average-reward-pomdp-nonattainment/review/claude-referee-2.result.md).
- [Exact finite segmentation replay](piecewise-lti-parent-replay.json); not a universal theorem check.
- [Wireless Markov identities and event-driven replay](wireless-parent-check.json); the strong-stability theorem requires an impractical unbounded control clock and is labelled partial.
- Adaptive game: [empirical replay](adaptive-game-parent-replay/smoke.json), [independent exact matrix moments](adaptive-game-parent-exact-moments.json). Safe robustly stable full actuation and common/private pilots are substantive restrictions.

Independent Fourier reproduction, using Python with `mpmath==1.4.1` and no worker imports or FLINT/Arb:

```sh
python3 -B information-science/evidence/information-science-more-20261014/parent_verify_fourier_obstruction.py \
  --certificate information-science/positive-tfd-marginals/evidence/fourier-certificate.json \
  --output /tmp/positive-tfd-parent-independent.json
```

Its Fraction corner/Sturm/identity checks are exact. Its 60-digit mpmath integrals reproduce the certified totals but **are not interval enclosures**; the separately replayed worker checker supplies rigorous Arb bounds.

## Screening provenance

- [Selection and all 51 article titles](selection.json).
- Network/signal screen: [report](ScreenNetworksSignals.md), [structured findings](ScreenNetworksSignals.json).
- Computation/statistics screen: [report](ScreenComputationStatistics.md), [structured findings](ScreenComputationStatistics.json).
- Control screen: [report](ScreenControlProblems.md), [structured findings](ScreenControlProblems.json).
- [PDF identity and rendered candidate ranges](book-provenance.json).

Raw scout reports are preserved, not silently corrected. The parent selection record qualifies their coarse status labels: rate stability is not strong stability; CSP dichotomy is not every constraint-optimization problem; unknown local dynamics are not known local dynamics. The repeated-title extraction for learning control was corrected to PDF747–751. The resonator equation is Mathieu, not Duffing, despite the historical text-extraction staging filename.

## Remaining scientific gaps

Useful next obligations are mathematical, not more infrastructure work: full joint-IF/GD classification or a one-sided-spectrum counterpart; identified physical/noise assumptions for blind seismic inversion; bounded-overhead simple scheduling under changing channels; and safe decentralized joint identification/control outside a known robustly stable uncertainty family.

All research agents and reviewer processes in this round completed. No workspace/infrastructure audits, Git mutations, external contact or publication were performed.
