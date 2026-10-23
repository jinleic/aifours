# Current computation and replay

`REPORT.md` and `claims.json` supersede the inherited delivery. Historical
reports, later prefix chunks, and separated windows are retained as archives;
they are not automatically current claims.

Production only (never invoked by claim replay):

* `build_epoch2.py` derives `scan128_digest.c` from the inherited `scan.c`
  and builds it alongside the separately implemented `scan32.c`.
* `run_epoch2.py` performs vectors, small controls, a benchmark, the full
  published unsieved control interval, then main/extension runs. No more
  than four scanner threads are used. Each new header records its binary hash.
* `factor_progression.c` is an unrelated bounded exact-factor search for the
  exceptional power-of-two exponent; an empty result eliminates nothing.

Replay uses Python only:

* `check_epoch2.py compare` checks fixed task scopes, provenance, consecutive
  blocks and EVERY preserved block digest, not all arithmetic.
* `check_epoch2.py samples` independently rechecks the actual smallest factor
  and COMPLETE ordinary power residue for every selected arithmetic record.
* `check_epoch2.py blocks --blocks ...` completely recomputes exactly those
  numbered blocks, with Cipolla roots and Python arbitrary-precision powers.
  It imports no scanner code and executes no local binary. NumPy stores the
  fixed-width digest records; it does not compute the modular powers.
* A factor record hashes `n:u64, q:u32, tag=1:u32, residue=0:u128` in little
  endian; zero explicitly means no power was computed. An unsieved record
  hashes its full ordinary residue and tag 2 (failure) or 3 (hit).
* `--backend manual` is a different exponentiation control flow over the SAME
  CPython integer arithmetic, not an independent arithmetic implementation.
* `--broken` deliberately corrupts a comparison and must exit nonzero.
* `recheck.py main-metadata` restores inherited oversized logs from all staged
  manifest-checked gzip parts, then checks their metadata. It does not import
  or execute their producer. Internal timeout allowances total below 300 s.

`deliver_epoch2.py` publishes completed scoped evidence and atomically replaces
`claims.json`. It preserves completed new arithmetic logs as gzip (mtime=0),
checks the decompression byte-for-byte, then removes only their redundant raw
copies. The checker reads those gzip versions directly.
`snapshot_epoch2.py` applies the actual delivery limits and runs every declared
command from the copy, requiring Python, <=300 s per command and <=1800 s total.
Its negative controls must fail with an explicit checker rejection, rather than
an import error or a timeout. `--package-only` tests packaging without arithmetic.

Live block inspection can observe a completed consecutive prefix while workers
run, without inventing a footer. Final main/controls comparisons require their
real completion footers; capped extensions claim only the common complete prefix.
The full target is not silently declared Python-replayed from samples or hashes.
