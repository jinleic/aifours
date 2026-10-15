# HMZ + Lean attempt: regular-semigroup embedding

Date: 2026-10-14 (PT).

**Full book Problem 1: not solved or refuted.** The actual HMZ reviewer returned `done:false`; the bounded loop ended `stopped`, not `done`. The artifacts below are substantive partial mathematics and formalization, not a replacement acceptance target.

## Results

| Result | Scope and evidence |
|---|---|
| **Theorem X:** every regular locally orthodox semigroup with a nonempty completely simple ideal has a completely simple quotient; weak E-unitarity makes the quotient idempotent pure. Consequently ξ is idempotent pure for every finite member of the book class. | Complete written coordinate proof in [xi-purity.md](xi-purity.md), audited step by step by the parent; [audit](written-claim-audit.json). **Not Lean-checked**, no novelty claim. This closes the finite ξ-non-purity counterexample route, not embeddability. |
| `P1.SD.embedding_necessary` | For an injective multiplicative map from a regular semigroup into an actual `B⋊G`, with `B` a locally regular band and `G` acting multiplicatively, the source is weakly E-unitary, E-unitary and locally r-orthodox. |
| `P1.Pastijn.embedding_necessary` and `P1.Restricted.embedding_necessary` | Necessary direction for both fixed book readings, using actual Rees multiplication and the genuine restricted carrier. These do not prove the sufficient direction. |
| `P1.SD.locallyROrthodox_iff`, `P1.Pastijn.locallyROrthodox_iff` | Local r-orthodoxy of the product is equivalent to local regularity of the band; the Pastijn iff supplies a row and column. No analogous iff for an arbitrary restricted action's entire base is asserted. |
| `P1.derived_embedding` and `P1.derived_from_embedding` | Constructive wreath criterion and its converse. The criterion explicitly assumes a faithful derived functor into a locally regular band; it does **not** construct such a functor from P1's source hypotheses. Surjectivity of the grading homomorphism is unnecessary. |
| Bounded condition searches | Distinct-witness pattern with 7 even/4 odd elements: UNSAT, without proof-logged certificate. 9 even/8 odd: UNKNOWN/timeout. No candidate, general exclusion or new embedding result. [Exact condition, source and constraint mapping](obstruction-condition.md). The 357/48 existing suites were not rerun. |

The complete list of **32 reported Lean roots**, source filenames, English statements, assumptions, scope and actual axiom sets is [claims.json](claims.json). The self-contained [Formal.lean](Formal.lean) prints every root's statement and transitive axioms. [progress.md](progress.md) gives the written construction proofs and exact unproved steps.

## Executed formal verification

The actor ran the frozen checker once. The HMZ reviewer independently recompiled the positive source and confirmed the 32 roots and axiom sets. After preserving the actor snapshot and correcting the review's documentation/source-evidence objections, the integration owner ran the unchanged checker once on the integrated files:

```sh
cd /Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/hmz-lean-20261014
python3 verify.py
```

Observed result: **exit 0; artifact checks pass**. Positive Lean exit **0**; semantic negative-control Lean exit **1**. Receipt: [verification/receipt.json](verification/receipt.json); [positive log](verification/formal.log); [rejection log](verification/negative.log).

- Runtime: cached Lean **4.34.1**, at `scratch/rh-quasi-lean-2026-10-07/lean`, reused read-only.
- Positive direct imports: `Mathlib.Algebra.Group.Hom.Basic`, `Mathlib.Algebra.Group.Pi.Basic`.
- Observed axiom union: **`propext`, `Quot.sound`** only. No reported root uses `Classical.choice`.
- Positive source SHA-256: `205e803eb251b10b0b17045e8c17b2081d44bf721e833c676fd4b421796cb613`.
- Negative source SHA-256: `7b05edaa6ca5cbdea33e4a3ac90beaa72769659f0a9a1ab5a0b262d9080dbfc5`.
- The negative control drops the necessary band hypothesis from the idempotent characterization. Its concrete witness `(2,1)` over multiplicative natural numbers has square `(4,1)`; the valid countermodel is checked before Lean rejects the false generalization.
- No full-corpus build/update, Comparator replay, external nanoda check, or adversarial sandbox certification is claimed.

## Actual frozen HMZ attempt

- Scratch repo: `scratch/ai4s-math-hmz-20261014/semigroup/repo`.
- Baseline: `19e7a6670a637565c73e46a920aca746bf44f275`; no subsequent commit.
- Frozen `TASK.md` and `verify.py` remained unchanged.
- Entry: shared `run_hmz.py` → `scripts/hmz-run.sh`, `--timeout 3600`.
- Worker: `codex/gpt-6.1-sol:max`; reviewer: `claude/claude-opus-5-5:max`, from the unchanged pairing authority.
- HMZ revision: `3d3e21b0da89ef5f6247cd7b3f88ad178fbac94a`; official flowverse: `2c37d06df3e356807adb93b5a9fdca170a5d0be8`.
- UTC interval: **19:21:29.713–20:21:30.124**, elapsed **3600.387 s**.
- Process exit **143**, wrapper signal 15 at timeout; actual reviewer **`done:false`**; epic terminal **`ended how:"stopped"`**; resume terminal **`ok:false`**. One completed review round; the resumed actor was interrupted.
- The permission-only local flow is **not an OS sandbox**. No pairing/runtime/credential changes were made.
- The post-run scoped process inspection found no remaining matching processes: [process-check.json](process-check.json).

Evidence: [process receipt](hmz/process.json), [actual reviewer verdict](hmz/reviewer-verdict.json), [wrapper output](hmz/wrapper.log), [epic journal](hmz/20261014T192129.920Z-ba5c3a-epic.jsonl), [resume journal](hmz/20261014T192129.920Z-ba5c3a-resume.jsonl). The original actor files and its verification receipt are preserved under [hmz/actor-snapshot/](hmz/actor-snapshot/). Documentation corrections after the run are recorded in [review-resolution.json](review-resolution.json); they do not change the failed full-goal verdict.

## References and inaccessible-source limits

[references.md](references.md) and [math-applicability.md](math-applicability.md) identify the exact local `math/` proof paths and transferable coordinate-action/congruence techniques, and explicitly reject the ordered-commutative-semigroup and field-representation conclusions as solutions of P1. No OAI theorem was imported into `Formal.lean`.

[The source-access ledger](source-access.md) records lawful author-site, institutional-repository, publisher and archival routes. Accessible additions include Szendrei 1993 and 2011, Hartmann–Szendrei 2012, Hartmann's 2007 thesis and Dékány's 2019 thesis. **Billhardt1998's actual construction, Szendrei2002's original problem wording and BS2003's full proof remain unavailable.** The later sources corroborate precise earlier statements but do not make those proofs inspected. Billhardt's specific band has not been shown locally regular. The book's undefined product wording and co-author discrepancy remain explicit.

## Exact remaining goal

1. For Q_orth with at least three D-classes, build a faithful locally-regular-band derived functor, or prove a genuine counterexample to existence. The formal criterion alone is not that construction.
2. For finite non-orthodox members, Theorem X supplies a pure completely simple quotient but not an embedding into the required products.
3. For infinite members lacking a completely simple ideal, ξ-purity also remains unresolved here.

No unsuccessful finite search is promoted to a general existence theorem. The status is **unresolved in this attempt; literature openness uncertified**, not a claim of solving the book problem.
