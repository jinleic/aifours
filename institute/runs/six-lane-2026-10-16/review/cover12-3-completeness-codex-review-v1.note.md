VERDICT: ACCEPT

I accept \(L(12,3)=36\) as a conventional computer-assisted exact determination, trusting the recorded executions, compiler, runtime and hardware. I found no completeness or correctness defect in the three search implementations. I independently checked the accounting and a length-36 witness; I did not rerun the large searches.

Findings:

- **Fatal: none.**
- **Major affecting minimality: none.**
- **Minor — incomplete supporting archive.** The packet contains hashes and extracted job records, but omits the worker binaries, original receipts, found-string files and comparison scripts. See [worker-run-manifest.json, lines 63–101 and 132–158](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/worker-run-manifest.json:63). Likewise, the parent’s assertions that all 38 hits were independently verified and their classes equal the worker’s classes lack the underlying lists and verification receipts here: [parent-result.json, lines 18–24](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/parent-result.json:18). Those supplementary assertions remain unverified by this review. Minimality requires only one valid length-36 witness, which I checked directly.
- **Minor — incomplete failure diagnostics.** The parent leaves allocation, thread creation/join and hit-output return values unchecked: [parent-light-window.c, lines 81–87 and 133–157](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/parent-light-window.c:133). The workers similarly omit some stream-error checks. These should be hardened for future runs. No resulting failure is evident in the supplied records.

All nine copied files match the byte counts and SHA-256 hashes in [manifest.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/manifest.json:3).

The source defines a covering sequence through its consecutive cyclic windows covering every word in the ambient space: [source-cetv.txt, lines 28–49](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/source-cetv.txt:28). Thus the property under review is exactly
\[
\forall y\in\{0,1\}^{12}\quad
\exists j<L:\quad
\sum_{t=0}^{11}[y_t\ne x_{(j+t)\bmod L}]\le3.
\]
Both constant targets are included.

A radius-3 ball contains
\[
V(12,3)=1+12+66+220=299
\]
words. There are at most \(L\) distinct windows, so \(L\le13\) covers at most \(13\cdot299=3887<4096\) targets. Consequently, excluding **each individual length 14 through 35**, then exhibiting a length-36 witness, proves minimality. No monotonicity in sequence length is involved. The published lower bound 34 is unnecessary.

The C audits support complete enumeration:

- **All strings.** [worker-brute.c, lines 35–40](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/worker-brute.c:35) generates every flip subset of size at most \(R\), exactly once. Chunk indexing includes target 4095. Lines 89–108 increment through every integer in the assigned half-open range. The periodic extension at lines 92–99 supplies every required bit, including repeated wrapping when \(L<n\). Moving a failed chunk to the front preserves a permutation; acceptance requires all chunks to pass. A timeout produces `TIMEOUT`, not a complete exclusion.
- **Necklaces.** [worker-necklace.c, lines 59–116](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/worker-necklace.c:59) implements the stated FKM recurrence correctly. The lexicographic integer and sequence integer use different, consistently handled bit orientations. Strict ordering, rotation minimality, independently calculated period, necklace count and weighted-period total jointly establish complete coverage of rotation classes. Windows use actual-\(L\) modular indexing. Killer targets permit rejection only after an uncovered target is demonstrated; acceptance subsequently scans every target. Lines 149–169 distinguish timeout and failed self-checks from successful completion.
- **Parent reduction.** A covering string must cover \(0^n\), so rotating a light window to position zero is complete. [parent-light-window.c, lines 94–109 and 132–143](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/parent-light-window.c:94) enumerates precisely the required candidates: low \(n\) bits from the prefix ball, disjoint high suffix bits, or every short string followed by the wrapping-window filter. Lines 48–58 implement both wrapping cases correctly. Lines 62–78 preserve the complete target permutation and return success only after all targets pass.
- **Parent threading.** Atomic fetch-add assigns each prefix once; every assigned prefix exhausts its suffix range. Orders and counters are private to each thread, and hit output is mutex-protected. The joined counters are compared with the expected total at lines 145–166. With the audited enumeration, this is a valid completeness invariant.

At the actual main and calibration parameters, all arrays, shifts and counters fit. The largest required window-extension bit position is 46; signed target shifts remain small, and large candidate counts use 64-bit arithmetic. I found no applicable overflow, undefined shift, unsafe early acceptance, complement/reversal pruning, or omitted all-one case.

I reconstructed the worker accounting from the **269 individual job records**, rather than accepting the aggregate flags:

- 138 all-string jobs and 131 necklace jobs map exactly to 131 accounting groups.
- Every range partition starts at zero, has adjacent endpoints without gaps or overlaps, and ends at \(2^L\).
- Every all-string job reports `examined == hi-lo`; its arguments agree with its recorded parameters.
- Every necklace job reports the correct count, weighted total \(2^L\), and zero self-check flags.
- Found-line counts agree with reported covering counts. Zero-result found-file hashes equal the SHA-256 of the empty file.
- The extra length-28 benchmark is a separate repetition; it was not double-counted as another required length.

I recomputed necklace counts using
\[
N(L)=\frac1L\sum_{d\mid L}\phi(d)2^{L/d},
\]
cross-checked them with Burnside’s gcd formula, and independently reconstructed exact-period populations. All expected totals agree with the recorded generated counts.

The principal results are:

| Length | All strings checked | Necklaces checked | Parent candidates | Reported hits: strings / classes / light-first |
|---:|---:|---:|---:|---:|
| 34 | 17,179,869,184 | 505,294,128 | 1,254,096,896 | 0 / 0 / 0 |
| 35 | 34,359,738,368 | 981,706,832 | 2,508,193,792 | 0 / 0 / 0 |
| 36 | 68,719,476,736 | 1,908,881,900 | 5,016,387,584 | 432 / 12 / 38 |

The worker’s length-36 string count reconstructs as \(146+140+146=432\). Every length 1–33 also has complete records and zero reported hits. See the [lower-length accounting](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/worker-run-manifest.json:10206) and [length-34–36 accounting](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/worker-run-manifest.json:11124).

These are independently verified **accounting relationships in execution records**. They are not fresh executions of the negative searches, and matching cardinalities alone do not verify equality of the omitted found sets.

For the parent, I checked all **144 result rows**, their parameter identities, stdout counters, modes, exit statuses and agreement with `parent-result.json`. For \(L\ge n\), I independently used
\[
\left(\sum_{i=0}^{R}\binom ni\right)2^{L-n}.
\]
For \(L<n\), I explicitly counted wrapping-window weights. At \((12,3)\), the counts for lengths 1–11 are
\[
1,1,1,5,6,7,19,35,63,111,187.
\]
Every row has `checked == independently expected`.

The calibration first-existence values reconstructed from the sweep are:

| Parameters | First length | Light-first hits there |
|---|---:|---:|
| (9,3) | 12 | 46 |
| (10,3) | 16 | 46 |
| (11,3) | 20 | 2 |
| (9,2) | 20 | 2 |
| (10,2) | 38 | 8 |

They agree with [source-cetv.txt, lines 541–557](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/source-cetv.txt:541). The parent records zero at \((11,3)\), lengths 21 and 22, despite existence at 20: [parent-sweep.jsonl, lines 85–87](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/parent-sweep.jsonl:85).

I reconstructed the witness identified in [worker-README.md, lines 173–175](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cover12-3-exhaustive-review-inputs-v1/worker-README.md:173), using bit \(i\) of `0x9d7d8d8a` as \(x_i\):
```text
010100011011000110111110101110010000
```
My own definition-first Python checker evaluated all 4,096 targets against all 36 modular windows. The nearest-distance histogram is
\[
\{0:36,\;1:432,\;2:2076,\;3:1552\}.
\]
Both constant targets have nearest distance 3. The reconstructed strict certificate also matches the README’s full SHA-256 pin. This independently establishes the upper bound 36.

Additional in-memory checks matched the window expressions against direct modular construction on 50,232 cases, matched the FKM recurrence against independently enumerated rotation classes through length 12, and checked flip-ball/chunk construction. Tiny exhaustive controls gave zero covering strings for \((1,0,1)\), two for \((1,0,2)\), and sixteen for \((3,0,8)\). These checks used Python translations and direct definitions; they did not execute the supplied C programs.

The implementations provide useful independent checks: unrestricted enumeration with ball unions, FKM enumeration with target distances, and a light-window reduction with an atomic scheduler. The parent shares some concrete techniques with each worker, so they are not wholly independent experiments, but their enumeration reductions and principal failure risks differ substantially.

The evidence supports **one exact finite table entry**, \(L(12,3)=36\), at the usual exhaustive-computation standard. It supplies no DRAT/LRAT or Lean proof, and establishes no priority, asymptotic result or broader breakthrough claim.