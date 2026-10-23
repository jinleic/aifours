# math-p0039 continuation, 2026-10-15/16 — exact certificate and forced-subgroup obstruction

**Outcome: partial.** The all-orders conjecture (every finite flag-transitive projective plane is
Desarguesian) is neither proved nor refuted. No novelty is asserted. FRONTIER: `PROOF-OBLIGATION`.

## Imported premises (not proved here)

1. **Kantor (1987), uses CFSG.** A non-Desarguesian flag-transitive plane of order n has n even,
   p = n²+n+1 prime, and a sharply flag-transitive Frobenius group.
2. **Thas–Zagier (2008), Prop. 2.1 / Thm. 2.4 / §2.** Such a plane is the development of
   D = (F_p^*)^n = μ_(n+1) in F_p (D planar). The only orders where this special plane is also
   Desarguesian are n = 2 (PG(2,2)) and n = 8 (PG(2,8)).
3. **Feit (1990), valid parts.** 8 | n (Lemma 2.2; the parent also cites Jungnickel–Vedder for
   8 | n, not read here) and d^(n+1) ≡ 1 (mod p) for every divisor d of n. With d = n and
   ord_p(n) = 3 this gives n ≡ 2 (mod 3), hence n ≡ 8 (mod 24).

Planarity forces 2 ∈ D (elementary argument, attack-e2 PREMISES.md item 5), i.e.
2^(n+1) ≡ 1 (mod p). **Not used:** the Thas–Zagier n < 2×10^11 computation, Feit's power-of-two
exclusion, and Ott's prime-power argument.

## Results

### A. Exact conditional exclusion, n < 2,582,236,504,064

| Segment | Interval in n ≡ 8 (mod 24) | Blocks | Members | Source |
|---|---|---:|---:|---|
| **Replayed from scratch** | [8, 2×10^11) | 994 | 8,333,333,333 | this lane, `task=low` |
| Prior exact prefix | [2×10^11, 251,539,607,552) | 256 | 2,147,483,648 | attack-e2 Python replay, records checked, not recomputed |
| **Extension** | [251,539,607,552, 2×10^12) | 8,685 | 72,852,516,352 | this lane, `task=main` |
| **Extension** | [2×10^12, 2,582,236,504,064) | 2,892 | 24,259,854,336 | this lane, `task=extension` |

Every member of this lane's 12,571 blocks (105,445,704,021 members) has an exactly recomputed decision.

* **Factor.** 91,040,739,086 members have a stored q with 1 < q ≤ 10^6 and q | p, re-verified
  member by member.
* **Residue.** For 14,404,964,935 members the complete residue 2^(n+1) mod p was computed with CPython
  integers and is ≠ 1.
* **libmpdec cross-check.** 1,552,266,804 of those residues were recomputed with libmpdec: all of
  the low range, and every 32nd unsieved member elsewhere.

The only residue-1 members without such a factor are **n = 8**, the classical PG(2,8), and
**n = 512**. Its collision 89785−1 = 89788−4 inside μ_513 mod 262657 is re-derived and re-verified
from scratch. n = 2^27 = 134217728 lies in low block 0 and is eliminated by 2593 | p. For
main and extension, every block digest of the 32-byte decision records equals **both** preserved C
digests from attack-e2.

The four segments join without gaps or overlaps (`evidence/coverage.json`). Under premises 1–3,
**no non-Desarguesian flag-transitive projective plane has order n < 2,582,236,504,064**, and the
statement no longer depends on Thas–Zagier's unreplayed search. The previous referee-accepted
exact bound was n < 251,539,607,552 and needed that search. This finite range is a sub-question,
not a solution. The order n = 2,582,236,504,064 itself is the first uncovered member.

### B. Forced-subgroup obstruction (`proofs/FORCED-SUBGROUP.md`)

* **Theorem 3.** For a ≥ 3 and P = 4^a+2^a+1, prime or not, the 3a residues 2^i mod P form a
  Sidon set. The proof is elementary and uses Eisenstein integers; it fails exactly at a = 2.
* **Corollary 4.** For n = 2^a with p prime, the subgroup ⟨2⟩ contains every element the premises
  force into D: 2, all divisors of n, and μ_3. So no certificate made of repeated nonzero
  differences inside it (the closure lemma and its S-unit generalizations) can exclude n. Together
  with the attack-e2 fixed-filter lemma, the family n = 2^(3^t) passes every congruence, fixed sieve,
  base-two test, divisor condition and forced-subgroup collision test for large t. Further
  exclusions need additional information; the theorem does not prescribe its form. 2 is a Fermat
  liar for every p_t, since ord(2) = 3a divides p−1.
* **Remark 5, the Desarguesian shadow.** Singer's planar set of PG(2,2^a) contains ⟨2⟩. Checked
  for a = 3 and 9; for a = 9 it meets μ_513 exactly in ⟨2⟩. The general case cites Cohen's trace
  theorem, read in an abstract and an introduction only.
* **Lemma 6** (minor). u−1 ∉ ±D for u ∈ D \ {1, 2, 1/2}, so −3 ∉ D. It does not exclude n = 512.
* **Review.** Codex gpt-6.1-sol: ACCEPT-WITH-FIXES on snapshot SHA-256
  102a6ea9b9f8d2445f5cc488daa35d388298a9b2be335dcbe740513a94dacf60
  (`institute/review/continuation-20261015/math-structure-codex-review.md`). Its required scope fix
  is applied. An Opus review timed out without a verdict. Neither is human peer review.

### C. The power-of-two member a = 3^10 is excluded (`evidence/fermat-t10.json`)

For n = 2^59049, p_10 = 2^118098 + 2^59049 + 1 (118,099 bits). A base-3 Fermat test gives
3^(p−1) mod p ≠ 1 (low 64 bits 4674363860819735172, residue SHA-256 `c1921cf0…af39`), so p_10 is
**composite**. Under premise 1, p must be prime, so n = 2^59049 is excluded. Base 2 cannot detect
this: 2 is a Fermat liar for every p_t (Corollary 4).

Two implementations computed the full residue and agree on it: `code/fermat_power_two.py`, with
CPython integers modulo 2^(3a)−1 in four checkpointed stages of 121–132 s each, and
`code/fermat_gmp_check.py`, with GNU MP `mpz_powm` through ctypes (36.6 s; nothing installed).
Both match CPython `pow` for t ≤ 7, giving residue 1 for the primes at t = 1, 2.

With attack-e2 (p prime forces a = 3^t; t = 2 by collision; t = 3,…,9 by factors), every
power-of-two order 2^a with 3 < a < 3^11 = 177147 is now excluded. Before, the bound was a < 59049.
This sparse family is an exact result, not a general bound. The next open member is a = 177147
(p of 354,295 bits).

### D. Validation-only verifier fix, 2026-10-16

An independent algorithm audit returned ACCEPT-WITH-FIXES
(`institute/review/continuation-20261015/math-certificate-code-codex-review.md`). It found no
false-exclusion path in the producer arithmetic for the fixed task scopes. It did find three ways a
**malformed** receipt could pass verification:

1. `check_coverage` accepted collision pairs that alias the same field pair modulo p, such as
   [[1,2],[262658,262659]] at n = 512, and zero-difference aliases.
2. It accepted a fractional "proper factor" (131328.5 for the prime 262657).
3. `certify.py replay` used a receipt's libmpdec stride unchecked, so stride −1 skipped every
   libmpdec comparison.

The fixes:

* **Collision witnesses** must be integers in canonical representatives 1..p−1 with a nonzero
  difference, and factor witnesses must be integer proper divisors.
* **Stride.** The shared block path requires a positive integer stride. Replay entry enforces the
  documented sampling policy (stride 1 for low, 32 otherwise), the task, the block list,
  agreement of duplicates, and a recognized checker stamp.
* **Written receipts** must follow the sampling policy.
* **Coverage hardening** adds strict integer and SHA-256 field checks. It also fails closed with
  an explicit message on malformed shapes.
* **Arithmetic paths are untouched.** `diff code/archive/certify-f6eaa1a8.py code/certify.py`
  shows only validation and provenance lines.

**Re-review fix (P2).** The focused re-review
(`institute/review/continuation-20261015/math-certificate-code-rereview.md`) returned
ACCEPT-WITH-FIXES. It confirmed that the three defects are closed. It also found that replay of the
first guarded verifier (`f3da25a6…`, now `code/archive/certify-f3da25a6.py`) did not type-check
stored rows and compared them with Python equality, so `id: false`, `start: 8.0` and a collision
coordinate `true` passed. Now:

* Replay and coverage validate rows and witnesses with one shared module, `code/receipt_checks.py`:
  int means a Python int (never bool or float), digests are 64-character hex, block fields are
  exactly the documented ones, and witnesses use canonical representatives.
* Replay compares rows in canonical JSON, which keeps `1`, `true` and `1.0` distinct.
* The survivor resolver re-verifies its output with the same shared rules. Its outputs for
  n = 8, 24, 90, 512 are unchanged.

**Hashes.** The **producer** `f6eaa1a80c4112d7af3caa54901f5451a88f9527bb9f23c4be54e89b897941a6`
computed and stamped all 446 production receipts. Its exact bytes are archived as
`code/archive/certify-f6eaa1a8.py` (`code/archive/MANIFEST.json`) and are verified on every
coverage run and every replay of producer-stamped receipts. The current **guarded verifier** is
`code/certify.py` `07cc2bf937c88889b742f1addd0f2ea1148547b5b602f80b237fcfcf480bf566`, together with
the **shared helper** `code/receipt_checks.py`
`85e43af3931bf1215b29d3278f7217d87b72708a338fce226d09f60e3b11b419`. New runs are stamped with both.
`code/check_coverage.py` (`7ea6ac90dfc2d07e42829b3f7f07a391cede9615a361255eeb78e8ad9cf8528e`) pins
the producer, verifier and helper, verifies all three files, and rejects any other stamp.

The archive also holds the superseded first verifier `f3da25a6…` with its coverage checker
`8dee2782…`, and the intermediate P2 verifier `d66fdcf0…` with its checker `fe4d6e49…`. The two
intermediates differ from the current files only by a `sys.dont_write_bytecode` guard. A handoff
self-check had left a `__pycache__` file in the bundle; it was moved to
`controls/fixtures/stray-bytecode-from-handoff-20261016/`, not deleted. The intermediates were
reconstructed by removing exactly that guard, and their SHA-256 values match the recorded hashes.

Receipts were not re-pinned or rewritten: all 446 hashes in `evidence/receipts-sha256.json` are
unchanged.

**Why the numbers stand.** The receipts are outputs of the archived producer, whose arithmetic
both audits accepted. Both fixes change only how stored input is validated; no sieve, residue,
libmpdec or digest path changed. The guarded checks accept every authentic receipt
(`evidence/coverage-v4.json`: gap-free bound 2,582,236,504,064; 446/446 producer stamps; producer,
verifier and helper bytes verified). The guarded verifier reproduces stored rows exactly, in
type-exact comparison, on replay of low 0 and 993, main 256 and 8940, and extension 0 and 2891. The
multi-hour range was not recomputed, as instructed.

**Fail-before/pass-after regressions.** With the current verifier, `code/regressions.py` passes
14/14 in 55.5 s (`evidence/regressions-validation-fix-v3.json`, fixtures in
`controls/fixtures/20261016T112559Z-85526/`). The intermediate `d66fdcf0` run also passed 14/14
(`-v2`). The first run, before the P2 fix, passed 11/11 (`evidence/regressions-validation-fix.json`).

* Six fixtures (alias collision, zero-difference alias, fractional factor, float geometry, stride −1
  replay, foreign stamp on replay) are accepted by the pre-fix producer or coverage code.
* Three P2 fixtures (replay with `id: false`, with `start: 8.0`, and with collision coordinate
  `true`) are accepted by the archived first verifier, run from exact-byte copies in its original
  layout.
* The current code rejects all nine with explicit reasons. A copy of the producer with one bit
  flipped is rejected, and the four authentic positives pass.

The 27 controls passed under the first guarded verifier (`evidence/controls-v3-all.json`). For the
P2 change only the regressions, replay positives and coverage were rerun, as requested.

## Method and arithmetic independence

`code/certify.py` was written fresh, imports no attack-e2 code and runs no binary. The producer
version `f6eaa1a8…` (archived) computed the receipts. The current file adds only the validation
above.

* **Primes.** A numpy Eratosthenes sieve gives all 78,498 primes below 10^6.
* **Roots of x²+x+1 mod q.** Primitive cube roots of unity g^((q−1)/3) for q ≡ 1 (mod 3), the
  root 1 for q = 3, none otherwise. Root sets are brute-forced for q < 3000 on every run. The
  attack-e2 checker used Cipolla roots.
* **Factor certificate.** Each marked member is re-checked as (n mod q)²+(n mod q)+1 ≡ 0 (mod q)
  in int64 (bounds n < 2^42, q ≤ 10^6), together with q < p. Members n ≤ 999 get exact Python
  checks and the q = p guard.
* **Residue certificate.** `pow(2, n+1, p)` with CPython integers for every unsieved member, plus
  the libmpdec subset above via `decimal.Context.power`. The decimal context traps Inexact and
  Rounded, and the run refuses a non-libmpdec `decimal`.
* **Independence.** CPython's integer code and libmpdec are separate arbitrary-precision libraries
  in one process. They are independent arithmetic, not merely two control flows. The two attack-e2
  C scanners use Montgomery arithmetic with radices 2^128 and 2^96 and are a third and fourth
  implementation; same-author caveats are in attack-e2. The attack-e2 Python replay and this lane
  share CPython's `pow`, but nothing else.
* **Records.** Records are hashed exactly as in the C logs: n:u64, q:u32, tag:u32, residue:u128
  LE, with residue 0 meaning not computed. Digest equality is a consistency check; the certificate
  is the recomputed arithmetic. The low range has no C logs, so its residues are all computed twice.
* **Survivors.** Every survivor must be resolved: classical n ≤ 8, an exhaustively found and
  re-verified collision for p < 10^7, or a factor. Otherwise the block fails.

## Commands (run from this directory; CPython 3.14.3, numpy 2.4.3, libmpdec 4.0.1, macOS arm64)

| Purpose | Command | Observed |
|---|---|---|
| Production, resumable, ≤ 4 workers, each chunk a separate < 295 s command | `python3 code/run_batch.py --plan low:0:993:12 --plan main:256:8940:32 --plan extension:0:2891:32` | 446 chunks, 0 failures, 18,198 s wall; longest chunk 172.1 s; ≤ 315.5 MB RSS |
| Coverage, contiguity, pins, C digests, witnesses | `python3 code/check_coverage.py --require-through 2582236504064 --output evidence/coverage.json` | pass, < 1 s |
| Spot replay low (16 blocks) | `python3 code/certify.py replay --task low --blocks 0,66,132,198,264,330,396,462,528,594,660,726,792,858,924,993` | pass, 188.3 s |
| Spot replay main (30 blocks incl. 256, 371 ∋ 2^38, 1737 ∋ 2^39, 4467 ∋ 2^40, 8940) | see `evidence/replay-spot.json` | pass, 151.1 s |
| Spot replay extension (18 blocks incl. 0, 988 ∋ 2^41, 2891) | see `evidence/replay-spot.json` | pass, 95.1 s |
| Controls | `python3 code/controls.py --output evidence/controls-v3-all.json`, run under the first guarded verifier `f3da25a6…` and not re-run for the P2 change; earlier `evidence/controls.json` (26/26, first plumbing) and `evidence/controls-v2-*.json` | 27/27, 29.0 s |
| Validation-fix regressions | `python3 code/regressions.py --output evidence/regressions-validation-fix-v3.json` | 14/14, 55.5 s (first run 11/11, 38.4 s) |
| Coverage with guarded verifier | `python3 code/check_coverage.py --require-through 2582236504064 --output evidence/coverage-v4.json` | pass; 446 producer stamps; producer, verifier and helper bytes verified |
| Structure checks | `python3 code/structure.py --output evidence/structure.json`; broken control `--max-a 12 --char0 4 --broken` | pass, 4.4 s; broken exits 1 |
| Fermat t = 10, CPython, 4 stages | `python3 code/fermat_power_two.py stage --t 10 --stage K` (K = 0..3), then `final --t 10 --output evidence/fermat-t10.json`; re-running a stage recomputes and must reproduce its checkpoint | 131.6, 126.0, 121.9, 120.7 s; composite |
| Fermat t = 10, GMP | `python3 code/fermat_gmp_check.py --output evidence/fermat-t10-gmp.json` | equal residue, 36.6 s |
| Fermat controls | `python3 code/fermat_power_two.py controls --max-t 7` | t = 1, 2 give 1; t = 3..7 give ≠ 1; base 2 is a liar for t ≤ 7 |

Any single block can be re-executed with `python3 code/certify.py replay --task T --blocks B` in
about 5 s (main/extension) or 6–13 s (low). The benchmark receipts are in
`evidence/benchmark-main-256.json` (5.09 s, 274 MB) and `evidence/benchmark-low-993.json`.

## Controls

* **Positive.** Tiny task [2, 20000) equals both C digests. Its survivors are exactly
  2, 8, 24, 90, 512: 2 and 8 classical, the other three with collisions. Replays of low block 0 and
  main block 256 equal their receipts.
* **Injected arithmetic errors**, each rejected with its own explicit reason: q = p at n = 2; a
  wrong factor; a false factor on an unsieved member; a wrong libmpdec-sampled residue (caught by
  libmpdec); a wrong unsampled residue (caught by the C digest on tiny/main, by libmpdec on low); a
  residue forced to 1 (survivor guard); a corrupted expected C digest; a corrupted stored receipt
  digest.
* **Receipt mutations:** gap, conflicting duplicate, shifted geometry, foreign checker hash,
  inserted survivor, removed resolution, broken collision witness, bookkeeping error, C-digest
  mismatch, libmpdec count. Each is applied to a copy of a reduced receipt set (all low receipts
  plus the first main receipt), and that unmutated set passes as a baseline.

**Fixture plumbing, changed after the first run (parent request).** `evidence/controls.json`
(26/26) came from the first version of `controls.py`. That version wrote the tiny receipt and the
receipt-mutation copies to system temporary directories outside aifours, deleted them afterwards, and
simulated a gap by deleting one copied receipt. The same version also ran once inside `handoff/`
during `evidence/handoff-selfcheck/selfcheck.json`. The real receipts were only ever read.

The current `controls.py` writes every fixture into a fresh run directory
`controls/fixtures/<UTC>-<pid>/` and keeps it. It never deletes anything and simulates the gap by
omitting the receipt from the copy, recorded in `OMITTED.json`. Only the affected groups were
re-run: tiny 2/2 (`evidence/controls-v2-tiny.json`) and coverage 12/12
(`evidence/controls-v2-coverage.json`, with the reduced-set baseline). The injection and replay
rows write nothing, so they are unchanged from `evidence/controls.json`. That plumbing change left
the checker source and its pin unchanged. The later validation fix is section D, and all 27 controls
were re-run after it.

## Input pins

* **C block logs** (attack-e2 `logs/`, read only): e2-main-scan32 `74e8a84b…b036`,
  e2-main-scan128_digest `ffae5842…2b0d`, e2-extension-scan32 `3b54ff6b…58fd`,
  e2-extension-scan128_digest `0e61292c…6acf`, e2-tiny-scan32 `30c5afe1…0eb6`,
  e2-tiny-scan128_digest `2097d9db…7982`. The full hashes are pinned in `code/certify.py`.
* **Prior replay records** (attack-e2 `evidence/epoch2/prefix-groups/0?-run.json`): pinned in
  `code/check_coverage.py`.
* **Checker provenance.** The producer `f6eaa1a8…941a6` is archived with verified bytes. The
  guarded verifier is `07cc2bf9…f566` with shared helper `85e43af3…b419`. All three are pinned in
  `code/check_coverage.py`; the producer pin is also in `code/certify.py`.
* **Superseded.** `superseded-v1/` holds 20 receipts for main blocks 256–895 from checker v1
  (`9076f4e4…`), the v1 source, and its batch log. Four of those receipts were stamped with a
  mid-edit hash. None is used by any claim; all those blocks were recomputed by v2.

## Limitations

* The exclusion is conditional on premises 1–3. The prior segment [2×10^11, 251,539,607,552) is
  accepted from attack-e2 and not recomputed here, as instructed.
* The full range was computed once, by this lane; samples were replayed. A referee can re-run any
  block in under 300 s, but an end-to-end replay needs about 72,600 CPU-seconds.
* The same author wrote the checker, the driver and the coverage checker. Receipts are self-reported
  provenance. The independent cross-checks are the libmpdec recomputation and the C digests.
* Results B are a method limitation, not progress on the conjecture. The model-referee review is not
  human peer review.

## FRONTIER decision

`PROOF-OBLIGATION`. Further scanning only lengthens a finite range: each 10^12 costs about 6
CPU-hours in Python, and a heuristic survivor count grows without bound (proof note, last section).
The high-value next obligations:

1. a uniform argument that uses information beyond the forced subgroup, for example the Gaussian
   period |ω_n|² = n (no form is prescribed by Theorem 3);
2. exact elimination of p_11 = Φ_(3^12)(2) (a = 177147). With GMP, a base-3 Fermat test is
   estimated to take minutes [INFERENCE: scaling from 36.6 s at 118k bits]. A second, independent
   CPython pass would take hours. It would extend only the sparse power-of-two family.

## Files

* `code/`: certify.py (guarded verifier), receipt_checks.py (shared strict rules), run_batch.py,
  check_coverage.py, controls.py, regressions.py, structure.py, fermat_power_two.py,
  fermat_gmp_check.py, build_handoff.py
* `code/archive/`: the exact producer `certify-f6eaa1a8.py`, the pre-fix
  `check_coverage-d4949917.py`, the first guarded verifier `certify-f3da25a6.py` and its checker
  `check_coverage-8dee2782.py`, the intermediate `certify-d66fdcf0.py` and
  `check_coverage-fe4d6e49.py`, and `MANIFEST.json`
* `receipts/{low,main,extension}/*.json`: 446 chunk receipts
* `evidence/`: coverage (first, v2, v3, v4), controls (first, v2, v3), validation-fix regressions (11/11, then 14/14 twice),
  receipt hashes, structure, replay-spot, benchmarks, batch-log, handoff self-check, and Fermat.
  `fermat-t10-stages.log` is a failed first launch (macOS has no `timeout` binary); the real run is
  `fermat-t10-stages-run2.log`.
* `controls/fixtures/`: retained control and regression fixtures, not in the handoff
* `proofs/FORCED-SUBGROUP.md`
* `handoff/`: the compact bundle for a later engine epoch: 62 files, 8,104,075 bytes,
  `MANIFEST.json` SHA-256 `44916e8c863cd25db3da725e736b90c17118a6c13afe767ca2212f1a72b3d4f3`.
  Its receipts are byte-identical concatenations of the original receipt files. Final standalone
  self-check (`evidence/handoff-selfcheck-v4/`): coverage passes; +1 and a wrong producer source are
  rejected; regressions 14/14; authentic replays pass; nothing is written into the bundle. Earlier
  self-checks are `evidence/handoff-selfcheck/` (pre-fix, superseded control plumbing), `-v2` and
  `-v3`. The `-v3` run left a `__pycache__` file in the bundle, which was moved out.
* `result.json`
