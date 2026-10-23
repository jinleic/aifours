# controls-v2-run1 was stopped; its outcome is UNKNOWN

- **Run.** `code/controls_v2.py` (52372b73…5505) was started at 09:47:34 PDT (host clock) as background job bg_2192.
- **Stop.** At 09:57 PDT the lane worker stopped it cooperatively through the job-control cancel. SIGKILL was not used.
- **Output.** None was written, and this directory was otherwise empty.

**Cause.** Inferred, not established: rule FH1 was applied to random realisable families containing subgroups of large index m. Its fibre enumeration grows exponentially in m.

**Replacement.** The same controls were re-run with a cost cap (FH1 only when m ≤ 6) as `code/controls_v3.py` (2ea9fba1…784). Results are in `evidence/controls-v3-run1/controls_v3.json` (c0a6b375…74c).

**Status.** None of these controls gates the run.
