**ACCEPT-WITH-FIXES.** I found no false-exclusion path in the producer’s arithmetic for the fixed task scopes. Three validation defects affect malformed receipts:

1. **Collision verification can accept the same field pair twice.** At [check_coverage.py:122](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/math-certificate-code-snapshot/code/check_coverage.py:122), membership uses modular arithmetic, but pair distinctness compares unreduced integers. For \(n=512,\ p=262657\), pairs `[[1,2],[262658,262659]]` with difference `262656` pass, although both represent \((1,2)\) modulo \(p\). Zero-difference aliases also pass. Require canonical integer representatives, or normalize before checking distinct pairs and a nonzero difference. The producer generates canonical entries; this defect concerns stored-witness verification.

2. **The stored proper-factor check accepts fractional factors.** At [check_coverage.py:117](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/math-certificate-code-snapshot/code/check_coverage.py:117), `factor=131328.5` passes for the prime `p=262657`: the inequalities hold and Python evaluates the remainder as zero. Require an integer factor before checking proper divisibility. The producer’s `uint32` factor marks do not have this defect.

3. **Replay can bypass every libmpdec comparison.** [certify.py:435](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/math-certificate-code-snapshot/code/certify.py:435) imports the receipt’s stride, and [certify.py:453](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/math-certificate-code-snapshot/code/certify.py:453) passes it directly to the block checker. Unlike `run`, replay never checks positivity. Changing a stored stride to `-1` and each block’s `mpdec_residues` to `0` makes the sampling loop empty; otherwise matching blocks can replay successfully. Validate the stride in the shared block-checking path and enforce the required sampling policy when validating receipts. Coverage rejects this negative stride, so this does not bypass its range check.

The remaining arithmetic checks are sound on inspection:

- The small-\(n\) guard clears `q=p`; subsequent checks require proper factors. Every member enters exactly one factor or residue branch.
- Progression-root construction and block offsets are correct. Factor-polynomial intermediates are below \(10^{12}\), all generated \(n<2^{42}\), and NumPy integer operations stay within their widths. Full moduli and residues use Python integers.
- Unsieved members reach complete modular `pow`; accepted sampling parameters require every low-range residue and every 32nd unsieved high-range residue to receive the libmpdec check.
- Records have the intended 32-byte layout and explicit little-endian fields. Residues need at most 84 bits, fitting the 128-bit encoding.
- Survivors cannot silently pass. Independently calculating the \(n=512\) case gave \(p=262657\), \(|D|=513\), and the valid collision \((1,89785)\), \((4,89788)\), both with nonzero difference \(172873\).

The configured geometry joins exactly:

| Segment | Blocks | Half-open interval |
|---|---|---|
| low | 0–993 | `[8,200000000000)` |
| prior | main 0–255 | `[200000000000,251539607552)` |
| main | 256–8940 | `[251539607552,2000000000000)` |
| extension | 0–2891 | `[2000000000000,2582236504064)` |

Missing blocks stop the prefix; conflicting duplicates fail; identical duplicates do not increase coverage. `--require-through 2582236504064` enforces the stated **exclusive** endpoint. Without that option, successful execution can report a shorter prefix. Explicit error gates remain active under `python -O`. The runner limits concurrency to four commands and each command’s timeout to below 300 seconds; RSS is recorded, without an enforced memory cap.

For portable handoffs, coverage recognizes `BASE/inputs`, while [certify.py:54](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/math-certificate-code-snapshot/code/certify.py:54) defaults to an ancestor-derived production log path. Replay and batch commands need explicit `--logs` pointing to bundled `inputs/logs`. Missing paths fail closed; this is an operational limitation.

All three source hashes match `manifest.json`, and the shipped producer matches its coverage pin. **Receipt checks still trust execution provenance:** hashes, counts and matching C digests cannot establish that the claimed arithmetic actually ran. The prior segment is accepted through pinned archived replay records, without rerunning its arithmetic. Those records, production receipts and C logs are absent from this snapshot, so this audit does not certify the final production endpoint.