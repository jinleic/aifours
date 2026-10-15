# Five mathematics targets: HMZ + Lean + openai/math

## User objective

Use HMZ, Lean, and `/Users/jinleic/jinleic-workspace/math` as references to push toward complete solutions of all five selected mathematics-volume problems. Build on the existing dossiers; do not duplicate the previous intake, long searches, or known-case replays. The full goals remain the goals: a partial theorem, conditional reduction, bounded computation, or easier replacement is not a solution of the original problem.

## Shared paths and ownership

Workspace: `/Users/jinleic/jinleic-workspace`.
New scratch root: `scratch/ai4s-math-hmz-20261014/`.
Each owner has one unique scratch Git repository under this root and its existing ai4s target directory. The parent owns this root's shared files and `ai4s/README.md` mathematics integration. Do not edit shared scripts, policies, registry, global configs, credentials, model settings, math/, archived research-institute/, or other target directories. Concurrent sessions own ai4s/.claims/, physics, information science, phys-*, robust-spr-*, stochastic-*, ddp-*, visual-cryptography-* and p-type-*; do not touch these.

Read relevant workspace rules and the humanize-workflow, openai-math-lean-verification and llm-coding-discipline skills. No deletion, force kill, reset, clean, push, external message, or live infrastructure mutation. No campaigns/ or scripts/campaign.py. Only the frozen scratch TASK baseline commit is required; do not commit workspace changes.

## Shared prerequisites already exercised

- Installed Lean 4.34.1 works, and `import Mathlib` successfully compiled with an axiom print.
- Reuse the existing cached project READ-ONLY at `scratch/rh-quasi-lean-2026-10-07/lean`. Do not copy/download/rebuild the full corpus or run lake update.
- For each new single-module Lean file, execute `/Users/jinleic/.elan/bin/lake env lean /ABS/PATH/TO/FILE.lean` with cwd `/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean`. Its 23 patched-dependency warnings are known expected; preserve actual Lean errors. Prefer narrow Mathlib imports to an unnecessarily heavy umbrella.
- Keep all new Lean modules inside your isolated scratch repo; write a self-contained `Formal.lean` (or a small explicit import closure). No shared OAI/ or ComparatorChallenges/ mutations. Importing already built OAI results is allowed only after auditing their hypotheses and showing why relevant.
- Established local identity is `jinleic <jinleic@users.noreply.github.com>`; use it only for the required fresh scratch baseline commit, not global git config.
- No other HMZ run was active at start.
- Pairing is ONLY `scripts/hmz-tiers.json`, currently worker codex/gpt-6.1-sol:max and reviewer claude/claude-opus-5-5:max. Do not override it. Installed HMZ revision is 3d3e21b0da89ef5f6247cd7b3f88ad178fbac94a; official flowverse revision 2c37d06df3e356807adb93b5a9fdca170a5d0be8. This request does not authorize updating them.

## Required HMZ execution

1. Read the target's existing README.md, proof.md and exact next-gap material. Inspect local math references for transferable mathematics and formalization patterns, not only topic-name matches. Record exact reference paths/theorems and applicability/non-applicability. Use no private/personal context.
2. Create your unique fresh scratch Git repo. Freeze `TASK.md` with the original target statement, current evidence, strategy, scope, baseline, and exact verification command. Commit TASK.md plus any independently written acceptance contract/checker once as the baseline. Use no bypass/model overrides.
3. Launch the actual HMZ RLAR actor/reviewer loop via the shared evidence runner:

   `python3 scratch/ai4s-math-hmz-20261014/run_hmz.py --repo /ABS/SCRATCH/REPO --output /ABS/SCRATCH/EVIDENCE --timeout 3600`

   Run from workspace root, using bash timeout 0 and async/background delivery as supported. The runner calls ONLY scripts/hmz-run.sh and retains provenance, output, process result, frozen hashes and journals. Do not run a separate competing reviewer CLI or construct an HMZ command yourself. Do not launch nested HMZ or subagent trees. Keep computational solvers bounded and at most 2 threads each; no repeated huge known portfolios.
4. Do useful proof/reference work while HMZ executes, but never concurrently edit files owned by its actor. The actor writes only the fresh repo; you integrate only afterward. Wait only when genuinely blocked. Do not poll the live run.
5. At termination inspect the actual reviewer verdict, epic.jsonl `ended` event, resume.jsonl, unchanged task/checker hashes, process result and any remaining processes. Exit zero, actor success, budget stop or timeout is NOT acceptance. Require reviewer done:true and ended how:done for RLAR acceptance. If the full original goal is not proved, the reviewer must return done:false, even if partial artifacts compile. Do not weaken frozen acceptance to make the run pass. Preserve partial results and failed attempts honestly.

## Lean and mathematical acceptance

- Aim for a proof/counterexample of the exact selected original statement, with its actual mathematical definitions and quantifiers. Record full goal versus achieved theorem separately.
- New proofs must use Mathlib definitions where present, or mathematically faithful explicit definitions that the parent can audit. Never assume the desired conclusion as a hypothesis, encode the result into a structure field, define a target as True, or use a trivial implication as a substitute.
- No sorry, admit, new axiom, unsafe proof escape, native_decide, Lean.ofReduceBool, implemented_by, skipKernelTC, unreviewed metaprogram/initialize/run_cmd/import replacement, or narrowed finite proxy disguised as the general theorem. Standard permitted axioms: propext, Classical.choice, Quot.sound only.
- Every claimed theorem needs an actual successful Lean run and #print axioms. Include #print for the theorem statement. Record exact imports, toolchain, source hashes and commands. A printed assumption list/statement must be compared against the mathematical target, not just the theorem name.
- If the full theorem is unreachable in this run, formalize a substantive existing/new bottleneck lemma, certificate-soundness theorem, or verified genuine case with explicit scope, and state the exact missing full-theorem step. Partial formalization is progress, NOT goal acceptance. Do not spend the run on rfl wrappers or generic textbook facts disconnected from the target.
- Supply a meaningful negative control for the formal statement or computational certificate (wrong conclusion, broken certificate, or violated necessary hypothesis must be rejected). Run final builds/tests once after edits, except necessary Lean proof iteration.
- Parent will independently re-run Lean, audit transitive axioms and theorem scope, and may run Comparator fresh-kernel replay where technically suitable. Do not claim Comparator or nanoda acceptance unless actually run.

## Deliverables to integrate after HMZ

Inside your ai4s target, add `hmz-lean-20261014/` with real Lean source, a reproduction command/script using the shared cached runtime, references/applicability notes, mathematical progress, exact full-goal status and missing lemma, axiom/build receipts, source hashes, HMZ process/journal evidence and rejection control results. Update only relevant sections of your target README/proof if a permanent result or correction warrants it. No misleading scaffold/placeholder proof. Preserve all earlier evidence.

Return a compressed report: exact files; HMZ baseline/timeout/runtime/pairing/terminal verdict and journal paths; theorem names/statements/hypotheses/axioms; actual commands/results; new mathematical result versus mere formalization; full goal solved yes/no; exact remaining obstruction. Notify the parent when the HMZ process has started and its repo/evidence paths. Parent independently owns final integration and acceptance.
