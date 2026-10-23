# Focused certificate validation re-review

Read only files in this directory. Do not modify, delegate, use the network, or read outside it. previous-review.md found three malformed-input defects: aliased modular collision witnesses, fractional stored factor witnesses, and negative replay stride that skipped libmpdec checks. The authentic receipts are not in this snapshot; their hashes are listed and the large production scan is not to be repeated.

Check whether code/certify.py and code/check_coverage.py now close exactly those defects, do not weaken accepted arithmetic or coverage, correctly verify archived producer bytes, enforce stamps without arbitrary-version fallback, and fail closed for malformed shapes. code/regressions.py and its result show fail-before/pass-after; inspect it as evidence, not as proof by itself. Also verify that new validation would reject equivalent modular witness aliases, zero differences, fractional/boolean factors, non-positive strides and wrong sampling policies.

Return ACCEPT, ACCEPT-WITH-FIXES or REJECT first, then only real correctness/scope findings with locations and concrete examples. Do not request a full production rerun and do not certify the final endpoint from this snapshot alone.
