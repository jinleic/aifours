# Frozen finite certification contract

Date: 2026-10-14 (PT). Scope: strong, nonconstant, black-white OR-stacking access structures and basis matrices, with separate transfer of maximum relative contrast and any matching lower bounds to arbitrary deterministic finite collections. See work/model.md. No novelty claim.

Claim: compute and independently certify four optima for every isomorphism class on n=1,2,3,4; extend to n=5 if the bounded exact checks finish. Include dummy participants and singleton-qualified sets. Exclude constant false (no qualified set) and constant true (empty qualified set, physically unrealizable positive gap). Enumerate monotone Boolean truth tables recursively and quotient only by participant permutations. Expected class counts, used only as controls: 1,3,8,28,208 for n=1..5. The independent verifier uses antichain backtracking, not the same enumeration recursion.

Baseline: Ateniese et al. (1996) Definitions2.1/2.2 and Section9 tables; Shyu–Chen (2011 threshold / 2015 general access) integer-programming literature must be model-matched. Exact LP/ILP is a classical non-AI baseline. This is not an AI-advantage experiment.

Missing ingredient: exact certificates rather than floating point optimization output, a second integer representation, and careful separation of basis and collection optima. Full arbitrary-n book problem is not claimed solved by finite tables.

Methods: HiGHS/scipy LP+MILP candidate generation; store rational primal and dual LP certificates; direct Fraction arithmetic checks; explicit projected-column histogram checks of integer witnesses; independently derived integer Mobius coordinates checked by Z3 where simple LP/integer/divisibility bounds do not suffice. Store all solver queries and results. Compare primary-source values only, with uncertainties marked.

Negative controls: corrupt an LP multiplier, a witness column count, an objective, and instance coverage; verifier must reject each. Validate known (n,n) expansion and contrast and threshold/graph anchors.

Budget: one compute process, BLAS/OMP/HiGHS threads=1; at most 5 cores and 16GB. Main n<=5 generation <=1800 seconds; each MILP <=30 seconds, each Z3 independent obligation <=60 seconds initially. No silent omission: a timeout leaves that instance uncertified. A bounded extra 1800-second exact verification pass may be used for at most 20 unresolved obligations. No n>=6 sweep. Outputs below 50MB each; heavy dependencies only in scratch/ai4s-visual-cryptography-optimality/venv. No persistent process after completion.

Success: all four basis optima for every claimed class have an integer witness and an independent exact lower/upper certificate; LP optima also apply to arbitrary finite collection schemes by the proof in work/model.md. A single uncertified row prevents a complete-n claim. General theorems are reviewed by the required Codex hostile referee, and objections are resolved explicitly. Stop after n5 certification or an exact justified blocker; do not expand scope to random-grid or XOR schemes to manufacture improvement.

Reproduction commands and versions are recorded in README.md and evidence/*.json. Campaign lifecycle uses ../../scripts/campaign.py from this directory: init, heartbeat, freeze, close. Protocol amendments, failures, and surviving limitations must be preserved, not suppressed.
