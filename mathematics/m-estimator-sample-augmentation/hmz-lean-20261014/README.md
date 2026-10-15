# HMZ, Lean and local mathematics reference attempt

Date: 2026-10-14 PT.

## Outcome and certification boundary

**Broad formalization (c) refuted: written proof, parent-audited, independent Opus referee correct (minor fixes applied); not Lean-certified; not HMZ-accepted.** The [construction](counterexample.md) uses a fixed p=2 nested design, fixed smooth loss with curvature [3/4,5/4], unique minimizers and independent exact same-law replication. Original weak consistency holds at every prefix, but pooled error has a positive-probability lower bound along completed stages. It requires **E|epsilon|=infinity**, hence infinite variance; Cui's unspecified regular-error question and the finite-moment general-convex regime remain open beyond Theorems 9/10. The separate parent-owned Claude Opus 5.5/max no-tools referee checked 44 written claims and returned **correct**, independently of Lean. Its five minor presentation fixes are applied without changing the construction. [Resolution, review receipt and both hashes](independent-referee-resolution.json); [owner audit](counterexample-owner-audit.json); [parent audit](counterexample-parent-audit.json).

This refutes the dossier's explicit **no-moment** formulation (c), not every intended interpretation of the book's unspecified error-law conditions. It shows Theorem 9's finite-variance hypothesis cannot simply be dropped; it does not prove finite variance necessary or decide finite-mean/infinite-variance cases. Cui's intended regular-error question beyond Theorems 9/10 remains unresolved here. The infinite construction and asymptotics remain written mathematics. **There is no compiled full asymptotic counterexample theorem.** Thirty substantive Lean components compile, including the exact loss/profile mechanism and stochastic second moments.

The actual HMZ actor/reviewer loop ran for its full frozen 3600-second limit. It stopped before the reviewer returned a structured verdict. **No reviewer `done:true`, no terminal `ended how:done`, and no RLAR acceptance.** A process timeout is not acceptance. Accordingly the integrated [claims.json](claims.json) sets `full_goal_solved=false` for the frozen certification gate and separately records the full written mathematical claim. [actor-claims.json](actor-claims.json) preserves the actor's original `full_goal_solved=true` and its explicit pending-review disclaimer unchanged.

Additional positive progress: [regular-bounded-score-derivation.md](regular-bounded-score-derivation.md) supplies a written, parent-audited Gaussian LAD/Huber/even-Lipschitz-loss regime without a leverage-rate assumption, subject to the original estimator's translation equivariance (uniqueness is sufficient). It is not a complete Lean proof. The actor also established the useful incompatibility that **pure LAD/Huber with unbounded two-sided error tails have positive-probability nonunique pooled minimizers for every finite repeated design**; this does not refute consistency for every selection, which the positive sufficiency argument treats.

## Actual HMZ evidence

- Frozen scratch baseline: `6961a086e7f6ed15d87d90c6c605ac8cce0a027b`.
- Runner command: `python3 scratch/ai4s-math-hmz-20261014/run_hmz.py --repo /Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/m-estimator --output /Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/m-estimator-hmz-evidence --timeout 3600`.
- Runtime revision: `3d3e21b0da89ef5f6247cd7b3f88ad178fbac94a`; official flowverse: `2c37d06df3e356807adb93b5a9fdca170a5d0be8`.
- Pairing from the unchanged registry: worker `codex/gpt-6.1-sol:max`; reviewer `claude/claude-opus-5-5:max`.
- Elapsed: **3600.369620249956 s**; process return code **143**. Frozen TASK.md and verify.py hashes remained unchanged.
- Actor and reviewer sessions both opened. Reviewer was interrupted after inspecting the proof, source, claims and receipts; no final verdict was returned. Journal terminal event: **`ended how:"stopped"`**. Resumable call ended **`ok:false`**.
- Final exact-repository `pgrep -fl` returned code **1**, no output: no remaining command matching the owned HMZ repository at that check. No process was manually killed.
- [Process receipt](hmz-run/process.json), [wrapper transcript](hmz-run/wrapper.log), [epic journal](hmz-run/20261014T192137.163Z-680165-epic.jsonl), [resume journal](hmz-run/20261014T192137.163Z-680165-resume.jsonl).

The source target README/proof and the independent Gaussian derivation were edited by the assigned owner while the actor owned only its scratch repo. The interrupted reviewer noticed those target edits; they were **not actor scope violations**. The frozen TASK.md/checker were never changed. No runtime/configuration/model update, nested HMZ, separate reviewer CLI, push, or corpus/cache mutation was performed by the owner.

## Lean results actually exercised

Source: [Formal.lean](Formal.lean), using nine direct Mathlib imports and no OAI imports. All **30** claimed declarations are listed with full assumptions, statements, novelty/formalization status and actual printed axioms in [claims.json](claims.json). Every printed axiom set is exactly `propext`, `Classical.choice`, `Quot.sound`.

Representative nontrivial roots:

- `Replication.ripple_even_error_contrast`: for every real eta,t and integer k, the ripple loss at the even-integer error 2k has contrast `rho(2k-t)-rho(2k)=rho(t)-2k*t`.
- `Replication.ripple_loss_derivative`, `ripple_score_derivative`, `ripple_curvature_bounds`, `ripple_profile_derivative`: genuine real calculus and global [3/4,5/4] curvature.
- `Replication.ripple_profile_integer_stationary` and `ripple_profile_half_score`: exact integer cancellation versus nonzero score `4 eta` after half-integer pooling.
- `Replication.centered_weighted_sum_second_moment`: arbitrary finite deterministic weights and genuine probability-space pairwise independent centered L2 variables; used only for **truncated errors**, never to assume the full counterexample error has a second moment.
- `Replication.bernoulli_frobenius_expectation`, `bernoulli_frobenius_expectation_le`, `bernoulli_frobenius_tail`: independent binary core indicators, normalized deterministic row trace and leverage; exact matrix second moment and Markov bound. These support the actor's separate bounded-score partial regime.
- `Replication.huber_core_remainder`, `huber_pair_flat_minimizing`, `convex_minimizer_inside_ball`, `integrable_loss_contrast`: faithful Huber remainder/tail geometry, convex radial confinement, and contrast integrability without requiring an error moment.

The actor's final command `python3 verify.py` ran once and passed artifact checks. [Receipt](verification/20261014T201609.802322Z/receipt.json) and [full theorem/axiom output](verification/20261014T201609.802322Z/Formal.lean.log) bind the source hash `92b3f2ac5ddb8d174ed236cc05be36006d7fdacf25e09e62bb2f26698d6acad3`. The source was copied unchanged for integration; the owner did not rerun the same acceptance check. Parent independent replay is separate.

### Meaningful rejection controls

[NegativeControl.lean](NegativeControl.lean) exits **1**, with semantic Lean failures in [the actual log](verification/20261014T201609.802322Z/NegativeControl.lean.log):

1. A singleton normalized Bernoulli row at q=1/2 has squared fluctuation exactly 1/4. A falsely halved upper bound 1/8 reduces to an unsolved `False` goal.
2. Extending integer ripple-score cancellation to the pooled half-integer would force `4 eta=0` with eta>0. The false theorem is rejected.

Neither is an import/syntax failure. These controls check the formal mechanisms, not asymptotic consistency by simulation.

## Reproduction

From this directory:

```sh
python3 verify.py
```

The unchanged checker compiles the positive and negative modules with `/Users/jinleic/.elan/bin/lake env lean`, using the existing read-only cwd `/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean` and its Lean **4.34.1** toolchain. It retains a fresh timestamped receipt. The 23 local patched-dependency warnings are expected; genuine Lean errors remain visible. No dependency update/full corpus build is needed. A checker pass still does not supply HMZ full-goal acceptance or formalize the infinite construction.

## Reference audit and exact remaining gap

- [Actor references and actual Mathlib dependencies](references.md).
- [Owner corpus applicability audit](math-reference-audit.json), including the convex-function compact-uniform pattern; no unreviewed OAI theorem was imported.
- [Primary-source access audit](source-access-audit.json): complete Zhao--Rao--Chen and Bai--Wu statements were not obtainable. Knight/Chen--Zhao--Wu are related prior work, not an unsupported novelty claim or unseen theorem premise.
- [Actor mathematical progress](mathematical-progress.md) retains the bounded-score, local-core-curvature, vanishing-leverage theorem, its noncentered bounded-drift variant, and positive-curvature Gram necessity beyond a global lower bound.

**Remaining certification work:** fully encode the fixed infinite law/design, every-prefix convergence and positive limiting pooled-error probability in Lean; the written proof has passed parent and independent Opus review, but only components are kernel-checked. The actual HMZ run ended stopped and cannot be retroactively accepted using the separate referee's verdict. **Remaining mathematical scope:** Cui's unspecified regular-error question, finite-moment general-convex formulations beyond Theorems 9/10, and LAD/Huber under singular/atomic/non-centered laws. The counterexample requires E|epsilon|=infinity; do not silently broaden it to finite-moment regimes or call the whole book problem kernel solved.
