# math-p0039 handoff bundle (continuation 2026-10-15/16)

A compact, hash-frozen bundle of new load-bearing sources, proofs, checkers and data, for staging
as a later engine selection input. `MANIFEST.json` lists every file with size and SHA-256 (all
files < 4 MB, total < 25 MB). The full evidence, including the 446 per-chunk receipts, is in the
parent directory `mathematics/evidence/hard-continuation-20261015/`. No old snapshot was modified.

## Claims (details and commands in `claims-candidates.json`)

Premises, imported: Kantor 1987 (CFSG); the Thas–Zagier reduction to D = μ_(n+1) in F_p with
p = n²+n+1 prime, with PG(2,2) and PG(2,8) the only special Desarguesian planes; Feit's valid
conditions 8 | n and d^(n+1) ≡ 1 (mod p), hence n ≡ 8 (mod 24). The Thas–Zagier n < 2×10^11
computation is **not** used. The all-orders conjecture remains open; no novelty is asserted.

1. **Replayed from scratch:** every n ≡ 8 (mod 24) in [8, 2×10^11) has an exact recomputed
   elimination. Survivors are only n = 8 (classical) and n = 512 (collision).
2. **Extension:** every n ≡ 8 (mod 24) in [251,539,607,552, 2,582,236,504,064) has an exact
   recomputed elimination, and all 11,577 block digests equal both preserved C digests.
3. **Combined conditional bound:** no non-Desarguesian flag-transitive plane has order
   n < 2,582,236,504,064. The middle segment [2×10^11, 251,539,607,552) is attack-e2's exact
   replay, checked here as pinned records only.
4. **Forced-subgroup Sidon theorem** (`proofs/FORCED-SUBGROUP.md`): a method limitation for n = 2^a.
   Codex review ACCEPT-WITH-FIXES on snapshot `102a6ea9…dacf60`; fix applied.
5. **p_10 = Φ_(3^11)(2) composite** (base-3 Fermat witness, CPython and GMP agree), so power-of-two
   orders 2^a with 3 < a < 177147 are excluded.
6. **Controls:** 27 positive and negative controls (the 26 of the first run plus a baseline for the
   reduced mutation fixture), all with the expected explicit reasons.
7. **Validation-only verifier fixes (2026-10-16):** 14 fail-before/pass-after regressions in
   `code/regressions.py`. They cover the three audited malformed-receipt defects, the re-review's
   replay field-typing gap (`id: false`, `start: 8.0`, a witness coordinate `true`), and hardening.
   Replay and coverage share one strict rule set, `code/receipt_checks.py`.

## Input pins (bundled under `inputs/`, identical bytes to attack-e2)

| File | SHA-256 |
|---|---|
| `inputs/logs/e2-main-scan32.blocks.jsonl` | 74e8a84b5bb34f26f00600ceb9570c942e922f92382a99d9de9981e4d1b0b036 |
| `inputs/logs/e2-main-scan128_digest.blocks.jsonl` | ffae5842bae87f84eb35006c1a86e659b2e2888f8ac952980bf92c1217b12b0d |
| `inputs/logs/e2-extension-scan32.blocks.jsonl` | 3b54ff6b9a2e3d4bf2e7ca9f285cbac81f8b91160bd6c628a75e4f8cb2a858fd |
| `inputs/logs/e2-extension-scan128_digest.blocks.jsonl` | 0e61292cc48886e1ea35a5f47d528d583b006e552561600a2f98415b84156acf |
| `inputs/logs/e2-tiny-scan32.blocks.jsonl` | 30c5afe1fb21741c9ca8111bb610176846f8c3dda2a82405d0f1a35b7e200eb6 |
| `inputs/logs/e2-tiny-scan128_digest.blocks.jsonl` | 2097d9db3f3e69e74aee0bf34398cc7280523b5038839f6a6d3ef93daf007982 |
| `inputs/evidence/epoch2/prefix-groups/0?-run.json` | pinned in `code/check_coverage.py` |
| `code/archive/certify-f6eaa1a8.py`: the **producer** that computed and stamped all 446 receipts (exact bytes, verified on use) | f6eaa1a80c4112d7af3caa54901f5451a88f9527bb9f23c4be54e89b897941a6 |
| `code/certify.py`: the current **guarded verifier**, validation only, arithmetic unchanged | 07cc2bf937c88889b742f1addd0f2ea1148547b5b602f80b237fcfcf480bf566 |
| `code/receipt_checks.py`: the **shared helper** imported by replay and coverage | 85e43af3931bf1215b29d3278f7217d87b72708a338fce226d09f60e3b11b419 |
| `code/check_coverage.py`: pins producer, verifier and helper, and rejects any other receipt stamp | 7ea6ac90dfc2d07e42829b3f7f07a391cede9615a361255eeb78e8ad9cf8528e |
| `code/archive/certify-f3da25a6.py`, `check_coverage-8dee2782.py`: the superseded first guarded verifier and its checker (the "before" side of the P2 regressions) | f3da25a6…ebff, 8dee2782…cb9a |
| `code/archive/certify-d66fdcf0.py`, `check_coverage-fe4d6e49.py`: the intermediate P2 versions, identical except for the bytecode guard | d66fdcf0…aef6, fe4d6e49…afe1 |

The checkers verify these pins themselves. Receipts are `receipts/{low,main,extension}.jsonl.gz`.
Each is a byte-identical concatenation of the original per-chunk receipt files, one per line, in
block order; raw SHA-256 values are in `MANIFEST.json` and per-file hashes in
`evidence/receipts-sha256.json`. The receipts keep their original producer stamp. They were not
re-pinned or rewritten.

## Commands (from this directory; Python 3 with numpy; GMP check needs libgmp)

```sh
python3 code/check_coverage.py --require-through 2582236504064          # coverage, pins, digests, witnesses (<1 s)
python3 code/certify.py replay --task low --blocks 0,66,132,198,264,330,396,462,528,594,660,726,792,858,924,993 --logs inputs/logs   # ~190 s
python3 code/certify.py replay --task main --blocks 256,371,1737,4467,8940 --logs inputs/logs    # ~30 s; any block id works
python3 code/certify.py replay --task extension --blocks 0,988,2891 --logs inputs/logs           # ~20 s
python3 code/controls.py                                                # 27 controls (~30 s); keeps fixtures in controls/fixtures/<run-id>/
python3 code/regressions.py                                             # 14 regressions: 9 fail-before/pass-after, 1 provenance, 4 positives (~55 s)
python3 code/structure.py                                               # Sidon/shadow finite checks (~5 s)
python3 code/fermat_gmp_check.py                                        # independent GMP Fermat residue (~40 s)
python3 code/fermat_power_two.py stage --t 10 --stage 3 --stages 4      # CPython stage replay vs checkpoint (~125 s)
```

Negative controls that must exit 1: `python3 code/check_coverage.py --require-through 2582236504065`,
`python3 code/certify.py replay --task low --blocks 0 --inject stored-digest --logs inputs/logs`,
`python3 code/structure.py --max-a 12 --char0 4 --broken`, and `python3 code/fermat_gmp_check.py --base 2`.

`code/controls.py` and `code/regressions.py` write every fixture into a new
`controls/fixtures/<UTC>-<pid>/` directory here (or under `--fixtures`) and keep it; they delete
nothing. The lane's own fixture runs are kept in the parent tree and are not copied into this bundle.
`evidence/controls.json` is the first, superseded run, which used system temporary directories.
`code/archive/check_coverage-d4949917.py` is the pre-fix coverage checker, kept only as the
"before" side of the regressions.

Production is reproducible with
`python3 code/run_batch.py --logs inputs/logs --plan low:0:993:12 --plan main:256:8940:32 --plan extension:0:2891:32`
(at most 4 workers, each chunk a separate command under 295 s). It writes per-chunk receipts under
`receipts/<task>/` and uses about 72,600 CPU-seconds.

## Limits

Conditional on the premises. The range was computed once and samples were replayed. The same
author wrote the checker, the driver and the coverage checker. The independent arithmetic
cross-checks are libmpdec (all low-range residues, 1/32 elsewhere), the two preserved C scanners
(main/extension digests), and GMP (Fermat). Structural results are method limitations; model
review is not human peer review.
