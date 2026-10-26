# Primary-source and corpus refresh v1

Observed audit clock: **2026-10-23T14:17:13-0700**. This is a bounded source screen, not a certification of current openness or novelty. All source/metadata operations stayed within the no-scientific-execution gate.

## Primary sources actually read

| Source | Actual read scope | Matched conclusion and limit |
|---|---|---|
| Song–Wang–Tomamichel–Fang, [arXiv:2609.37240v1](https://arxiv.org/abs/2609.37240v1) | Local complete text available; definitions (1), (2), (7)–(9), introduction, Theorem 1/Corollary 8, Remark 5 and discussion read; live abstract, API and title search refreshed | Exact majorization is a conjecture for arbitrary d,n and physical replacement p; therefore its n=4,d=2 case is a matched open-source target. Approximate majorization, Schatten ordering and shifted-logdet ordering do not settle all exact finite-n partial sums. The live API still linked v1. No later exact four-qubit resolution was located in this bounded screen. |
| Song–Chen, [arXiv:2603.25410v1](https://arxiv.org/html/2603.25410v1) | Primary introduction, independent-marginal counterexample, compatible-marginal Conjecture 2 and Proposition 3 entry read; current internal n3 proof also read | The counterexample chooses incompatible reduced states and is not a state counterexample to the assigned channel problem. The compatible n3 result does not settle the unrestricted n4 target. |
| Amosov, [arXiv:2401.05104v1](https://arxiv.org/html/2401.05104v1) | Definitions 1–2, Proposition 1 and its proof, condition (8), Proposition 2, Theorems 1–2 and the tensor-product proof read; live API linked v1 | Not a safe completed import: Proposition 1 as printed has the exact counterexample below. Its use in the tensor-product proof therefore cannot by itself certify the assigned target. This is a trust/applicability objection, not a complete priority audit of every theorem or intended correction in the paper. |
| Wyderka–Gühne, [arXiv:1905.06928v3](https://arxiv.org/pdf/1905.06928) | Primary definitions (1),(3),(4), sector bounds, spin inversion and shadow identities read | Pauli sector lengths, pure-state marginal-purity identities and spin-inversion methods are established prior art. The candidate derives its needed identities explicitly; these ingredients must not be marketed as new. The primary contains no matched depolarizing-majorization theorem in the read sections. |

Local SWTF PDF SHA-256: `456ba1cd2c82b37db9ac5e59986f1d54c9e90995daacc678922a4ab43ebfd6df`.

Search-engine synthesized mathematical prose was treated only as a lead. In particular, one response incorrectly assigned three rather than six weight-two Z correlations to four-qubit GHZ; that synthesis is not used as evidence. The candidate's identities come from the displayed derivation and match the primary sector-length normalization.

## Exact obstruction to importing Amosov Proposition 1 as printed

This is an **import check**, not a counterexample to four-qubit depolarizing majorization.

The proposition states that channels Phi and Psi on H, each majorized in Definition 1 by probability vectors P of length m and Q of length n, satisfy `Phi composed_with Psi prec P star Q` when `dim H>=mn`.

Take `H=C^2 tensor C^2` and the completely positive, trace-preserving mixed-unitary channel

`E(X)=(I_2/2) tensor Tr_A(X)`.

Equivalently, E is the equal mixture of conjugation by the four Pauli operators on A, tensored with identity on B. For every pure input, its output is `(I_2/2) tensor rho_B`; all eigenvalues are at most 1/2 and the trace is one. Consequently, in the source's own definition,

`E prec P`, `P=(1/2,1/2)`.

Set Phi=Psi=E, P=Q, m=n=2. The dimension hypothesis holds with equality: 4=mn. But E is idempotent. On the exact positive input `|00><00|`,

`E composed_with E (|00><00|)=(I_2/2) tensor |0><0|`,

whose spectrum is `(1/2,1/2,0,0)`. The claimed product probability vector is `(1/4,1/4,1/4,1/4)`. Their first partial sums violate the proposition: `1/2>1/4`.

The printed proof attempts to combine separate output-majorization estimates for channel composition; those estimates do not imply a tensor-product spectrum bound. Theorem 2 explicitly invokes that proposition. A corrected theorem with additional hypotheses might still be true; this check neither refutes all intended variants nor resolves the assigned channel conjecture. It does establish why an abstract-level majorization claim is not enough to mark the target solved by prior work.

## openai/math screen

Local paths actually searched:

- `/Users/jinleic/jinleic-workspace/math/CONTENTS.md`
- `/Users/jinleic/jinleic-workspace/math/overview.tex`
- `/Users/jinleic/jinleic-workspace/math/README.md`

Patterns: `depolariz|majorization|log-determinant|spin.alignment` (case-insensitive). No matches.

The live remote [CONTENTS.md](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md) was fetched and searched with the same pattern, also without a match. The remote header advertised 719 manuscripts/372 families at fetch time. A bounded `site:github.com/openai/math` search for depolarizing, majorization or spin alignment found only the repository landing page. This checks the advertised index, not every PDF, trace, theorem or unpublished change. No corpus theorem is imported.

## Actual internal receipts, not just the dated index

Read the baseline at `physics/evidence/six-lane-20261016/depolarizing-majorization-n4/`:

- `README.md` (current detailed log);
- `frozen-partial-v1/PROOF.md`, SHA-256 `6789e392dbc70dbed479ba8f307e0eb6c786d735de691d425583ec0d8b2fce8a`;
- `frozen-partial-v1/ADDENDUM_v1_1.md`, SHA-256 `73b6abb4e0a10b4fb9fe54ae5be853130c45a466b65a258c17385bc9911267d4`;
- actual `review/codex-frozen-partial-output.md` and frozen manifest;
- `zlemma-route/FROZEN_STATEMENTS.md`, SHA-256 `b3db2407c950fc56bdbbe041dce7aa329ed403685886deef6951cec38166b71b`, together with its mandatory `ERRATUM_scope.md`.

The stored reviewer accepted the partial reductions/certificates with fixes; its old arithmetic executions were not rerun here. The exact LP obstruction concerns the specific relaxation and does not prohibit all other low-degree encodings. The earlier Gram route supplies neither the current conditional theorem nor a full majorization proof.

The source book router `books/README.md`, root README and physics index were read. The book relation is a modern scoped quantum-channel instance, not a literal four-qubit statement printed in the 2009 volume and not a solution of its capacity question.

## Current verdict

**Eligible explicit conjectural source; present-day openness and priority UNCERTIFIED.** No matched settling proof was accepted from the refreshed sources. The current written contribution consists of conditional/state-region certificates and a near-product central-index exclusion, not an unrestricted solution, exact counterexample, new all-input index closure, kernel proof or priority-certified discovery. No scientific executable, numerical optimizer, eigensolver, enumeration, solver, compilation or certificate replay was launched.
