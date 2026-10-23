# Erratum 1 to ext-search-n1-fault-mapping-v1.md (2026-10-19T11:32:10-0700)

Additive correction by ContinueCFR21c; the mapping (3b7ca447ab029659dd674b2d1206f4a1bed7ab97386f9e8398045d2bbad9a201) stays byte-identical. Written only, NOEXEC.

Section 3 says the instrumented stream uses "CPython's text-layer settings for a piped stdout; only the raw layer and the
explicit 8192 buffer differ from production". That is imprecise in one more respect. Under the driver's LC_ALL=C child
environment, CPython's own sys.stdout uses UTF-8 mode with errors="surrogateescape". The child (n1_fault_child_v1.py lines
212-213) sets errors="strict". Both encode the ASCII-only B-BAD_PIN line to identical bytes, so no case expectation, relation
or audit mapping changes. Exact differences from production stdout: the raw layer (instrumented FaultRaw instead of FileIO),
the explicit 8192-byte buffer, and the errors handler.

