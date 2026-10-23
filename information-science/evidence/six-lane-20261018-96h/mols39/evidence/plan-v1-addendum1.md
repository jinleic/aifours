# Plan v1 addendum 1 — W1 GO request revised after parent HOLD (2026-10-19T01:23:05-0700)

Parent HOLD on run_native_v2.py (stability parser refuses observer_start line; unprotected post-spawn path; RSS
unreadable not fail-closed; no RSS/free checks after stream close) is accepted; run_native_v1/v2 are withdrawn and will
never be executed. Replacement (no new framework):
* code/owned_supervisor_v2.py — byte-identical copy of the parent-reviewed RQLS supervisor (sha 1fece595…).
* code/stability_gate_v2.py — byte-identical copy of the RQLS gate (sha 1f62874a…), observer source
  control/resource_observer_v3.py (fe311f28…), monitor control/resource-observer-live-v3.jsonl.
* code/go_exec_shim_v1.py (fae816bba0ade4572ae2b5e10c0b1c9fbb7a014aa465d5e0e5457fdc25f6e8f7) — reads one line; only b"GO\n" -> os.execv(solver) (same PID/PGID);
  EOF/other -> exit 3 without running.
* code/make_sup_configs_v1.py (884268f470865987a3d22c02daa744f230c36632fce3a24903851c0df80f9562) — deterministic supervisor configs from the pinned wave spec
  evidence/wave-w1-spec-v1.json (c55db584cd9bc05784da39b6c9774b2e94f0fa045ac23fc6245d70c935e62f5c) and the GO record: max_wall = solver self-limit + 60 s, RSS trip 1.8 GiB,
  free trip 12e9, output trip 17 MiB, launch free >= 12.2e9 + 20 MB, sample 10 s, settle 120 s, chunk-fit 10800 s,
  owned_compute_settled_by 2026-10-22T21:56:33-07:00; pins = CNF, solver binary, shim, Python binary, model.
Exact W1 sequence (after a parent GO record exists):
 A. CNF generation (stdlib, outputs > 16 MiB): for each model in spec.cnf_generation run
    code/run_probe_v1.py <new rec dir> python code/sym_dm_cnf_v1.py write <model> evidence/cnf-v1/<name>.cnf
 B. code/make_sup_configs_v1.py <spec> <spec_sha> <GO record> <GO sha> evidence/runs-w1/
 C. J1..J7: python -I -B code/owned_supervisor_v2.py evidence/runs-w1/<item>/config.json, one at a time.
    J8, J9 (long): python -I -B code/stability_gate_v2.py <monitor> <lane> 20000000 evidence/runs-w1/<item>/gate.json
    <observer source> fe311f28… must exit 0 immediately before each launch; then both supervisors concurrently.
 D. each SAT stdout -> code/verify_solution_v1.py (decode + full clause evaluation + checker A).
Everything else in plan-v1 section 4 (purpose, expected outcomes, stop rules, no Z39 seven-row target run) unchanged.
