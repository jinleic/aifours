# Parent outcome ledger — difficult-problem run, 2026-10-15 PT

The generated records under `runs/hard-2026-10-15/problems/*/record.json` are the authority. This file
summarizes them and records parent-only checks; it does not edit or replace any record.

## Status

Batch 03 (engine epoch 2) ran from 14:23:47 to 17:36:09 PT. All three visits closed **`unverified`**
with frontier `PROOF-OBLIGATION`. Every referee returned `accept-with-fixes`: no claim was judged wrong,
no negative control passed, and the requested fixes are wording or control changes. Under the engine's
rules, anything short of a clean `accept` closes before the novelty stage, so no visit has a novelty
verdict. The batch was not requeued: 26 minutes remained before the approved 18:02:24 PT cutoff, while
the shortest lane had needed 25.8 minutes for attack, replay and review before its novelty stage.
Receipts: [`batches/03/receipt.json`](../runs/hard-2026-10-15/batches/03/receipt.json).

## Results within their stated scope

| Problem | Referee verdicts | Established | Not established |
|---|---|---|---|
| Mathematics `math-p0039` | 18 correct, 3 minor fixes | Conditional on Kantor (1987, uses CFSG), Thas–Zagier's reduction and `n < 2×10^11` computation, and Feit's conditions (`n ≡ 8 mod 24`): a sandbox-replayed exact Python recomputation leaves no survivor for `n < 251,539,607,552`. Power-of-two orders `2^a`, `3 < a < 59049`, are excluded by exact factors and one difference collision. | The all-orders conjecture. Two same-author C runs agreeing through `n < 2,582,236,504,064`, and one unreplicated run to `10,341,223,092,224`, are empirical reports, not certified bounds. |
| Information science `info-p0403` | 7 correct, 2 minor fixes | Elementary degree/Parseval proof, independent of the unrefereed 2026 RM(1,9) preprint: the balanced nine-variable maximum is 240 or 242; degree ≤7 forces nonlinearity ≤240; a balanced 242 function needs degree exactly eight and nonzero support XOR. Exhaustive restricted exclusions around five Kavut–Yücel 242 tables and in listed flat and fixed-half classes. | Existence of a balanced 242 function. 252 half-classes passed the necessary-condition screen and were not searched. |
| Physics `phys-p0422` | 3 correct, 3 minor fixes | Written proof plus rigorous outward-rounded rational enclosures: random 4-SAT is unsatisfiable with high probability at density 9.96 and 5-SAT at 21.14, for independent clauses with distinct variables and fair signs. These are below the classical 10.23 and 21.33. Two referee passes found no proof gap. | Formal verification, human peer review, or novelty of the explicit constants. Exact thresholds and the chapter's other challenges. |

Remaining referee fixes are listed in each record's `next_action`. Mathematics wants stored-output
wording, a `q=p` corruption control, and a renamed bookkeeping field. Information science wants the
two certificate-backed classes and the 16-point flats stated explicitly, plus an accurate description of
one control. Physics wants a discriminating ledger control and "rigorous enclosure" instead of "exact".

## Parent checks

1. **Replay.** After the supervisor exited, the wrapper checked all 36 delivered claim contracts (21 math,
   9 information science, 6 physics). It replayed commands for 32 claims in sandboxed temporary snapshots;
   four proof-only entries had no executable commands. Every executed verify/check command exited 0,
   and every negative control failed. Receipt: [`parent-check.json`](../runs/hard-2026-10-15/parent-check.json),
   finished 18:03:59 PT. Replay demonstrates repeatability, not mathematical correctness.
2. **Physics same-law density control.** This addresses the referee's control request outside the record.
   The certified warning laws stay unchanged, and only density varies. Both checkers accept 9.96 and
   21.14, with `Psi_128` upper bounds −0.00146 and −0.00046. Both reject 9.90 and 21.10, with
   upper bounds +0.00181 and +0.000681. The two pairs straddle the cavity predictions 9.931 and 21.117
   from Mertens–Mézard–Zecchina (2006). The snapshot hash was unchanged. Evidence:
   [`physics-subcavity-control/result.json`](physics-subcavity-control/result.json).
   [INFERENCE] Linear interpolation puts these laws' zero crossings near 9.933 and 21.124, just above the
   predictions. That is consistent with the referee's remark that this method can at best reach the
   cavity threshold. The control checks the arithmetic certificate, not the written proof.
3. **Information-science theorem.** Parent audit of the {240, 242} and degree-eight argument found no
   gap: [`information-degree-theorem-audit.md`](information-degree-theorem-audit.md).
4. **Physics batch-02 proof.** [`physics-epoch1-proof-audit.md`](physics-epoch1-proof-audit.md).
5. **Independent review of this ledger.** Codex `gpt-6.1-sol` ran read-only and returned
   ACCEPT-WITH-FIXES with one major finding (replay coverage) and three minor ones. All four were applied:
   [`hard-2026-10-15-outcomes-codex-review.md`](hard-2026-10-15-outcomes-codex-review.md).

## Attribution and novelty

- **Physics.** The literature stage recorded 19 sources on 2026-10-15: 17 full-text, one abstract-only and
  one inaccessible. It located no certified k=4/5 constant below 10.23/21.33 in the accessible material.
  The parent checked that Vorobyev's paper and Lean repository
  ([arXiv:2610.10599](https://arxiv.org/abs/2610.10599), [code](https://github.com/yamelton/sat-upper-4268))
  cover k=3 only. One web search limited to the past month found no later k=4/5 claim. The principle is prior art.
  [Mertens–Mézard–Zecchina](https://arxiv.org/abs/cs/0309020) state that Franz–Leone proved, for even k,
  that the 1RSB cavity threshold is an upper bound. [Lelarge–Oulamara](https://arxiv.org/abs/1708.02457)
  condition (4) admits odd arity with nonnegative factors. At most the explicit certified constants could
  be new. Achlioptas–Menchaca-Méndez could not be reopened because its host failed DNS; the literature
  stage read its full text and still located no certified k=4/5 improvement. Search misses do not establish novelty.
- **Information science and mathematics.** No novelty is asserted. The Walsh-divisibility method may be
  classical, and the range extension is computational and conditional.

## Budget

Minutes of model and engine attempts. Batch 02 started the owner-approved fresh allocation at
12:02:24 PT. Parent replay, which ran from 17:36 to 18:04 PT, is not research time.

| Problem | Batch 01 | Batch 02 | Batch 03 | Batches 02+03 | Unused of 360 |
|---|---:|---:|---:|---:|---:|
| Mathematics | 218.7 | 55.4 | 191.4 | 246.9 | 113.1 |
| Information science | 10.0 | 93.5 | 73.3 | 166.8 | 193.2 |
| Physics | 10.0 | 54.1 | 25.8 | 79.9 | 280.1 |

The one-off cutoff watcher saw the supervisor exit before 18:00:24 PT and sent no signal:
[`approved-deadline-watchdog.log`](approved-deadline-watchdog.log).

## Next actions, not scheduled

- Physics: independent human review or Lean formalization of `attack-e2/notes/PROOF.md`, then a dated
  novelty check. Only after that would an approved requeue have a reason to reach the novelty stage.
- Mathematics: a replayable certificate or external re-execution for the paired C range.
- Information science: search the 252 half-classes that passed the necessary-condition screen, or find
  an argument for arbitrary degree-eight tables.
