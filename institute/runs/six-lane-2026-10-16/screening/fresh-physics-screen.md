# Fresh physics replacement screen — 2026-10-16 PT

Source: read-only scout `FreshPhysicsScreen` (completed after 29m45s). Its report is preserved below as screening evidence, not as an established result. No SDP, solver or numerical computation was run by the scout. "No resolution found" is a dated search result, not proof of openness.

## Ranked targets

| Rank | Target | Best outcome if positive | Tractability | Main risk |
|---|---|---|---|---|
| 1 | [[24,0,10]]₂ integral matrix weights (Anglès Munné–Huber, Open Problem 1) | Answers a stated open problem. Moment feasibility only: it says nothing about whether the code exists | High: small exact computation, decisive tests | Low value if positive; a "nonexistent" result is much likelier a bug than a theorem |
| 2 | Song–Chen Conjecture 2 (spin alignment with marginals of one global state), three qubits | Proof, or one exactly certified counterexample | Medium | Crowded field; modest value; does not give platypus additivity |
| 3 | Original spin-alignment conjecture (von Neumann entropy) at three letters | 3-letter additivity of platypus coherent information | Low | Hard and crowded; stretch only |

### 1. [[24,0,10]]₂ integral matrix weights

- **Exact target.** Integers λ^{t,p}_{i,j} satisfying Eq. (31), plus the pure (32), self-dual (33), additive (34: x ≥ 0, λ ∈ ℤ) and Type II (35) constraints of [arXiv:2603.19901v1](https://arxiv.org/pdf/2603.19901v1), with n = 24, K = 1, δ = 10 and the A_j of Eq. (38); or a certificate that no such integers exist.
- **Primary attestation.** §3.3, p. 8: "We have the following open problem regarding a putative additive code for which a possible integral weight enumerator satisfying all LP constraints is known, but for which we do not know whether also integral matrix weights exist." Open Problem 1 asks for "a putative integer matrix weight enumerator λ^{t,p}_{i,j} for this code."
- **Underlying code status, as reported by the scout.** [Rains–Sloane](https://arxiv.org/pdf/math/0208001): "the possibility of an additive trace-self-dual code of length 24 over F₄ with minimal distance 10 remains open … if such a code exists then it must be even." [Grassl table](http://codetables.de/QECC.php?q=4&n=24&k=0) lists 8 ≤ d ≤ 10 (page changed 2024-06-10). [OEIS A030331](https://oeis.org/A030331) gives the extremal weight distribution.
- **Parent arithmetic check.** The Eq. (38) distribution plus A0=1 sums to 2^24. A naive t-design multiplicity calculation on the 18216 weight-10 supports is integral for t ≤ 5 and nonintegral at t = 6; this is a sanity check, not a design theorem.
- **Freshness, as reported.** arXiv v2 returned 404; five INSPIRE citing records by title do not address this code. [2607.14920](https://arxiv.org/abs/2607.14920) is a caution signal for SDP-level exclusions in another setting. The public certificate repository covers n ≤ 19. openai/math local and remote CONTENTS screens found no coverage.
- **Proposed representation [INFERENCE].** Matrix weights as S₃-symmetrized genus-two/pair enumerator coefficients; possible additional valid constraints include pair-enumerator MacWilliams self-duality and Rains–Sloane design equations. These need source-checked derivations before use.
- **Decision tree.** Real SDP feasibility; feasible-set dimension; integer points by lattice/mixed-integer methods. A sound infeasibility certificate would exclude the hypothetical code and is unusually high-risk for bugs; a positive table resolves only the stated feasibility problem.
- **Verifier.** Exact integer table, independent γ/α factors, exact algebraic-field positivity, [[5,1,3]] Eq. (37) control, brute-force hexacode/dodecacode pair weights, existing certificate replay and ±1 / wrong-normalization mutations.
- **Book link.** Related, not verbatim: Feng Keqin's quantum error-correcting codes chapter, book pp. 601–604, asks for better finite quantum codes.

### 2. Song–Chen Conjecture 2, three qubits

- **Primary attestation.** [arXiv:2603.25410v1](https://arxiv.org/pdf/2603.25410), §III Eq. (14) majorization conjecture and §IV next-step request for general three-qubit settings and arbitrary positive semidefinite Q.
- **Baseline.** Proven for Q = I/2 with μ supported on pairs (Prop. 3); one citing record [2607.07913](https://arxiv.org/abs/2607.07913) does not address it.
- **Missing lemma.** Ky Fan control for mixed singleton/pair/full-set distributions.
- **Risk.** Active field; modest consequence; does not by itself give platypus additivity.

### 3. Spin alignment with von Neumann entropy at three letters

- [2603.23417](https://arxiv.org/abs/2603.23417) states the arbitrary-tensor-power entropy version as open; [2410.18254](https://arxiv.org/abs/2410.18254) resolves two letters.
- Majorization and separable Ky Fan routes fail at three letters by cited examples; a proposed resolvent-trace route is untested.

## Dropped by the scout

- Wigner entropy conjecture: disproved by [2609.24670](https://arxiv.org/abs/2609.24670).
- Holevo–Utkin ℓ_p conjecture: proved for all d by [2606.14698](https://arxiv.org/abs/2606.14698).
- Two-factor separable Ky Fan majorization: proved by [2607.27116](https://arxiv.org/abs/2607.27116).
- Liu–Cheng reverse Araki conjectures: counterexamples in [2607.01263](https://arxiv.org/abs/2607.01263).
- Two-copy Werner undistillability and all-p minimum-output Rényi additivity: claimed resolved by [2607.23416](https://arxiv.org/abs/2607.23416) and [2607.15210](https://arxiv.org/abs/2607.15210).
- PPT², entropy photon-number inequality, six MUBs in d=6: claimed by openai/math families 272, 273 and 266.
- SUSY bilinear KdV classification and fading pure-loss channels: no precise open statement found.

## Parent disposition

Open Problem 1 is the first frozen physics replacement candidate. It is assigned first to the existing quantum-code lane if `((7,3,3))_2` lacks a credible mechanism, because the scout's representation and verification overlap that lane's source and Knill–Laflamme/enumerator tooling. A positive integer table must not be described as code existence.
