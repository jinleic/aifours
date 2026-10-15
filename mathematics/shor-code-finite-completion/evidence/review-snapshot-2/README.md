# Shor's code: finite completion (book Question 1)

Date: 2026-10-14 PT. Verdict: **PARTIAL / OPEN-BLOCKED**. Question 1 is not resolved, and no novelty is claimed.

## Exact book question

Source: *10000个科学难题·数学卷* (Science Press, 2009; ISBN 978-7-03-024267-9), chapter "关于有限码具有有限完备化的判定问题" by Guo Yuqi and Liu Yun. Book pp.64–65, PDF pp.80–81. Verbatim excerpt: `source/problem.zh.txt`; page images: `source/page-080.png` and `source/page-081.png`.

Translation of the decisive passage:

> A code C over X is complete if X\*wX\* ∩ C\* ≠ ∅ for every w ∈ X\*. A finite code has a finite completion if it can be embedded in a finite complete code. Fact: a regular (in particular finite) code is complete if and only if it is maximal. The non-maximal finite code over {a,b} that refuted the conjecture "every code is commutatively equivalent to a prefix code" is
> C = b{1,a,a⁷,a¹³,a¹⁴} ∪ {a³,a⁸}b{1,a²,a⁴,a⁶} ∪ a¹¹b{1,a,a²}.
> **Question 1.** Does C have a finite completion (equivalently, by Fact 1, a finite maximal extension)? A positive answer would refute the conjecture that finite maximal codes are commutatively equivalent to finite maximal prefix codes.
> **Question 2.** Is it decidable whether a finite code has a finite completion?

This dossier addresses Question 1 only. The exact quantified proposition is `work/Question.lean`, which also served as the frozen HMZ statement.

## Status and baseline

- Restivo–Salemi–Sportelli (1989) prove a necessary condition: any completion yields a cyclic factorization containing Shor's pair `({0,3,8,11},{0,1,7,13,14})`. They conjecture noncompletion, but the general form of their factorization conjecture was refuted by Sands (2007).
- Cordero (2019) states that inclusion in a finite maximal code is unknown. He gives `n=330k`, `k≥4`, for the order `n` of `a`, so `n≥1320`. The 2022 De Felice and 2023 Cordero results cover only special orders that every admissible order here avoids.
- Szabó (2006), Theorem 7, as transcribed by the HMZ actor, would give `330p_1p_2p_3 | n` and so `n≥9900`. **This source was unverified by this worker.**
- No published construction or all-order impossibility proof was found or validated. A search miss is not evidence of openness or novelty.

## Results (see `proof.md`)

| Claim | Status | Evidence |
|---|---|---|
| `C` is UD and incomplete (`bbaab`, `a^26` are missing factors) | finite certification; reproduction | `work/check_evidence.py`, `evidence/verification.json` |
| Bridge: any completion gives tilings `R×Y^t×L≅Z_n^{t+1}` for all `t≥0`, with `R⊇{0,1,7,13,14}`, `L⊇{0,3,8,11}`, `Y⊇C`; no converse | written proof, `proof.md` §3 | independent review; replay on 5 explicit maximal codes in `evidence/bridge-multiplier-sanity.json` |
| Multiplier Lemma M and unit Lemma U | written proofs, §§4–5 | review; sanity replay |
| `660 | n` | written proof, §6; the 330 part is prior art | collision certificates in `evidence/raw-instance.json` |
| `8 | n`, hence `1320 | n` | written proof plus Lean arithmetic root `exists_unit_eight_mul_eq_four`; novelty unestablished | `work/ShorArithmetic.lean` |
| If Szabó Theorem 7 holds, then `n≥19800` | conditional; Lean roots `quotient_ge_sixty` and `combined_order_lower_bound` | primes may overlap 2, 3, 5, 11; only distinctness is used |
| Known words under all unit multipliers give no contradiction for any `1320 | n` | written proof of a method limit, §8 | |

Lean: three roots with only `propext`, `Classical.choice` and `Quot.sound`, plus four false-proposition controls. They formalize arithmetic only, not the bridge, the multiplier lemmas, or the book question. Byte hashes and logs are in `evidence/final-verification.json`.

## HMZ attempt (one run, exact Question 1)

Repo `scratch/ai4s-math-more-20261014/shor`, baseline `af6baa9`, frozen `TASK.md`, `ACCEPTANCE.md`, `Statement.lean` and `verify.py`, run through the shared `run_hmz.py` and `scripts/hmz-run.sh`.

- Pairing: worker codex `gpt-6.1-sol:max`, reviewer claude `claude-opus-5-5:max`; HMZ `3d3e21b`, flowverse `2c37d06`.
- The run was stopped by the watchdog at 3600 s: return code 143, epic `ended how:"stopped"`, resume `end ok:false`.
- Two completed reviews both returned "not done"; a third reviewer session was interrupted.
- Frozen files were unchanged. `verify.py` reports UNRESOLVED (exit 2).
- **Not accepted.** Summary and copies: `evidence/hmz-summary.json` and `evidence/hmz/`.

## Independent review

Codex `gpt-6.1-sol` (max effort, read-only) reviewed snapshots of the dossier. Prompts, snapshot manifests, verdicts and dispositions are in `evidence/review-*.json`. The partial results are not novelty-cleared, and no reviewer has approved a full resolution.

## Exact next actions

1. Authenticate Szabó (2006), Theorem 7 and its proof through library access; obtain Sands (2007) and check whether its construction can embed the RSS sub-pair `({0,3,8},{0,1})`.
2. Settle the embedding problem for Shor's pair over all `n` divisible by 1320. Impossibility would answer Question 1 negatively, through §3. An embedding would only be a first step: a positive answer still needs an explicit finite UD code with Kraft sum 1.
3. Only after 2: formalize the bridge and Lemma U in Lean against `work/Question.lean`.

Verification commands (from the workspace root):

```sh
python3 -B ai4s/shor-code-finite-completion/work/check_evidence.py
python3 -B ai4s/shor-code-finite-completion/work/check_bridge_multiplier.py
cd scratch/ai4s-math-hmz-20261014/verification/lean-verify && PATH=$HOME/.elan/bin:$PATH \
  lake env lean /Users/jinleic/jinleic-workspace/ai4s/shor-code-finite-completion/work/ShorArithmetic.lean
```
