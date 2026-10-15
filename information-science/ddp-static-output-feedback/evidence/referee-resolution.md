# Independent referee disposition

Date: 2026-10-14 (America/Los_Angeles).

## Run and scope

- Command and requested model/effort: [codex-referee-command.json](codex-referee-command.json).
- Invocation: `codex exec`, read-only sandbox, ephemeral session, no live-web option, stdin closed by `printf '' | ...`.
- Observed header: Codex CLI 0.162.1; model `gpt-6.1-sol`; provider `openai`; reasoning effort `max`; sandbox `read-only`.
- Run completed successfully in 665.06 seconds. The tool returned the final reply and wrote [codex-referee-reply.md](codex-referee-reply.md).
- Reviewed immutable content is preserved in [characterization-reviewed.md](characterization-reviewed.md); its original SHA-256 is recorded in the command JSON. The corrected current manuscript is [../work/characterization.md](../work/characterization.md).
- The task was hostile review of seven mathematical claims, not a delegated implementation, benchmark run, or exhaustive literature survey. The reply is advice, not automatic proof or novelty clearance.

## Verdict and independently checked disposition

**Verdict: correct-with-fixes.** No counterexample was found to the central equivalences, count/degree bounds, lattice counterexample or hardness embedding. Both requested corrections were applied.

| Finding | Referee conclusion | Disposition |
|---|---|---|
| 1. Finite Markov criterion | Correct; last parameter is essential | Retained. Independently exercised by the exact adjugate-numerator XOR checks and `last-markov-essential` negative control. |
| 2. Internal stability | Correct, including hidden modes | Retained. Hidden-unstable-mode and strict-boundary controls reject transfer-zero but non-Hurwitz plants. |
| 3. Lifted encoding and complexity | Encoding/counts correct; arithmetic/bit wording insufficiently separated | **Fixed manuscript Section 4.** Define total dense rational bit length `ell`; state the arithmetic CAD bound separately; state only a coarse bit upper bound and no precise uniform bit prefactor. Basu 2014 Definition 1.1 / Theorem 2.4 were fetched independently. |
| 4. Fixed-V common-gain ranks | Correct; joint kernel/image tests sufficient | Retained. Expand the block equation to NMT=0, NG=0, FT=0, J=0; lift the induced map through H. Exact rank-versus-original-linear-equation checks cover 256 fixed subspaces plus all scalar plants. |
| 5. Controlled/conditioned lemma | Correct only when invariance is the sole obligation | Retained with explicit DDP/stability scope restriction. The separate direct-feedthrough negative control demonstrates why invariance alone is inadequate. |
| 6. Greatest-subspace obstruction | Correct for candidates contained in the prescribed S | Retained with its exact domain. The two lines and their sum give [true,true,false] in both exact formulations. It is not a theorem against all geometric algorithms. |
| 7. Strong-hardness inheritance | Reduction correct assuming the supplied recent theorem | Retained as **source-relative**. The 2026 primary statement was fetched; the full underlying 3SAT proof is not independently reconstructed. No hardness claim for the no-stability variant. |
| 8. Evidence/numbering | Only Theorems 1-4 are numbered; reduction versus external theorem must be separated | **Fixed manuscript Section 9.** Name Theorems 1-4, the invariance lemma and lattice example; separate our embedding from the imported lower bound; state explicitly the referee did not audit numerical/exact computation logs. |

## Additional source correction obtained during the review

The original review was launched after a primary institutional conference abstract and before retrieval of the full Automatica 2000 paper. The latter was subsequently fetched and read. Printed p.1722 explicitly describes finite-step QEPCAD for the residual general case and both DDPCM/DDPCMS; equation (A.7) already uses the finite Markov criterion. This strengthens the non-novelty limitation. The corrected manuscript and README cite that precise primary location, not merely the conference abstract. No theorem was changed as a result.

The parent clarified that decidability, hardness and equivalent existential conditions cannot count as resolution of the book's original scientific synthesis question. The final status is accordingly **PARTIALLY-SOLVED, evidence-limited**, with no claim of general structural resolution and no invented polynomial-time requirement.

## Residual trust boundaries

- Neither this project nor the referee kernel-checked the general proofs.
- The reviewer accepted the 2026 theorem as a supplied source premise; it did not independently verify its proof or publication status beyond that supplied premise.
- The reviewer did not run the test suite. The suite's exact outputs were checked by this worker; the two general algebraic encodings share the Z3 backend, while scalar decisions also have an independent analytic oracle.
- One unrestricted alternate Lyapunov check timed out. The exact redundant-cut fallback is recorded and is not represented as independent stability-oracle evidence.
- A second model run was not needed for the two wording/numbering fixes. The saved original reply remains unchanged.
