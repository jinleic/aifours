# reviewer-f118-review-v1-erratum-1

Observed clock before this file was written: `2026-10-29T03:07:43Z` (`/bin/date -u`).

Applies to: `review-v1.md` (SHA-256 `616a08e72e0066e8dd7b8630d9cb52c99c119eb3ce40b90a9d719ea638265a32`, 15763 B, 87 LF), §4 first line.

Correction: the size of `reviewer-f118-controls-v2.py` is **36422 bytes** on disk (UTF-8), not "36253 B". The figure 36253 was the Python *character* count printed when the file was generated; the file contains multi-byte UTF-8 characters (κ, Φ, ∫, …). The SHA-256 quoted in `review-v1.md` for that file, `084f821299bef8684ed6d7d017f43242979688decbdc09f270e0f5fe55387209`, is correct and was verified against the on-disk file before and after the run (`self_sha256` line of the output). No check, verdict or other figure in `review-v1.md` is affected.

For completeness, on-disk sizes of all reviewer artifacts at this clock: `reviewer-f118-controls-v1.py` 35797 B; `reviewer-f118-controls-output-v1.txt` 2287 B; `reviewer-f118-controls-v2.py` 36422 B; `reviewer-f118-controls-output-v2.txt` 11738 B; `reviewer-f118-receipt-v2.json` 14838 B; `review-v1.md` 15763 B.
