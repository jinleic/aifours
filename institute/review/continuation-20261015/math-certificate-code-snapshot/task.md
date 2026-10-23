# Independent certificate algorithm audit

Read ONLY files inside this snapshot. Do not modify files, delegate, read outside it, or use the network. Focus on code/certify.py and code/check_coverage.py; code/run_batch.py is the bounded runner. The full production run is still finishing, so this is an algorithm audit, not confirmation of its final endpoint.

Mathematical contract (imported premises, not the subject of this review): a non-Desarguesian flag-transitive plane of order n>8 forces n=8(mod24), p=n^2+n+1 prime and D=mu_(n+1) planar. Necessity:2^(n+1)=1 mod p. The algorithm excludes each progression member only by a checked proper factor1<q<p dividing p, a fully computed non-one modular residue, or an exact repeated-difference witness inside D. n=8 is classical and n=512 is resolved by a collision.

Audit for false rejection or false range certification:
- Proper-factor guard including q=p small n, complete mark partition, integer overflow (numpy int64/uint64), progression roots, memoryview record packing and endianness.
- Every unsieved residue really recomputed with CPython arbitrary-precision pow, with a separate libmpdec check for all low-range residues and a1/32 subset above2e11. A digest comparison is consistency only, not the arithmetic proof.
- Survivor handling: no base-two survivor can silently pass. n512 witness membership, pairs distinct and nonzero equal difference. No probabilistic primality assumed for a rejection.
- Coverage: exact block geometry, all contiguous segments from8 to target2582236504064, no lost boundary class or off-by-one, duplicates/gaps, malformed or omitted receipts, source pins and C-log matching. The imported prior interval[2e11,251539607552) has its own pinned exact Python replay records and is not recomputed in this lane. Distinguish checking those records from rerunning arithmetic.
- Default paths vs portable handoff paths, --require-through, resource bounds and error gates active under python -O.

The parent separately requested fixture-safety fixes in controls.py (retain all fixtures under the repository, no cleanup deletion); that file is not in this snapshot and is not your task. Do not ask to re-run the multi-hour production scan. You may perform small in-memory calculations but no source/text tests or incidental style review.

Report ACCEPT, ACCEPT-WITH-FIXES or REJECT, then real consumer-visible correctness findings with code locations and failure examples; distinguish proof defects from scope/wording. Explicitly state the trust limits of a coverage/receipt check. No novelty assessment, no global all-orders claim, and no final production-endpoint certification.
