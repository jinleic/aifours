# Checker I/O-boundary v3 (certificate package v5) — 2026-10-19T08:41:58-0700

Final checker: /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker_v3.py, SHA256 ed93f236c342925eded12b299b52cfb5f6fb5b7835d30833cb8ff0b22b759dcb.
Prior capped-read boundary: cert_checker_v2.py9056dccb...; original independent algorithm: cert_checker.py e7e84962....
All scientific code FORMAT_TAG through compute_facts remains EXACTLY17,671 bytes,
SHA256 b2b8719207d7375189b982feacf0b8409220db14dab39d2da575f036009d9e56, source-byte comparison only.
No execution, compilation, syntax parsing or control replay performed.

Actual input reader remains O_RDONLY|O_NONBLOCK|O_NOFOLLOW, regular-file descriptor fstat, cap+1 byte read loop,
64KiB maximum block, budget before/after reads, same bytes hashed/parsed, no snapshot. Input/overflow/FIFO errors
return ERROR2, never intended INVALID1. Output schema and math/rejection strings unchanged.

The ONLY new checker change from v2 is after final print(line,flush=True) returns: compare shared monotonic deadline,
and if late return ERROR2 regardless of the emitted scientific verdict (including INVALID1). The already-emitted
single line and exclusive retained file are immutable and are NOT rewritten or reprinted. Their wall_s may describe
the pre-flush duration; parent accepts only exact expected exit plus supervisor/parent completion telemetry, NEVER
status text alone. Late exit2 invalidates even an intended INVALID1 control.
Parent audit must inspect exact final exit and stdout/file binding, and reject any non-success completion.
No program helper launches, new outputs or changes to the scientific certificate argument.
