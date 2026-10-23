# GO request: rqls_assay_v9 MODE r9 (forced Z_9+1 with its own in-run positive anchor), ONE bounded run - NOT run

Recorded 2026-10-19T02:28:30-0700 (from /bin/date 02:27:18 + writing). Requester ContinueRQLS10b (successor of ContinueRQLS10).
Nothing has been executed with numpy for v9 (no smoke). Launch owner: to be stated by the parent (per
review/rqls10-w8-launch-coordination-deviation-v1.json); this worker will NOT launch unless the GO names it as owner.

## Pins (sha256)
- source code/rqls_assay_v9.py: e907968609f9e90c1c25891068227f3117a7ec44691338494b5d99cd772164db (0444)
- diff review/rqls_assay_v8_to_v9.diff (unified, v8 0988a73b...0bfc0 -> v9): 291edc71228bafc598a368d345b3ff785f5c2bc67ede294c7169cfc7c48bf157
- config evidence/rqls_assay_v9.r9.supervisor-config-v2.json: a0f04bc00be375f6c9023808131024b7d5b0c7c0a14f2b8ab33e3c405c9fc3e7
- supervisor code/owned_supervisor_v2.py: 1fece595258d7ba448875c407e8b221bdbd01966824dc267147c316ef54115aa
- gate code/stability_gate_v2.py: 1f62874aff9b22657a90f180b81c678117fd703afe2345f7576454e0faae008a
- inputs: evidence/parker_z7p3_classical_v1.result.json 00e991d6...1c30; six-lane-20261016/rqls10-maximal/controls/C1_ex24_positive.json
  da95d092...b18c; evidence/z9p1_classical_search_v1.result.json 4199ee99...7c6b (hash-checked in-run, gate A9)
- tightening 8ac556699352a42f3d97f83861039e21f57db0646da2f38391ee1f11e330aa20

## AST diff v8 -> v9 (stdlib ast.dump of every top-level def/class)
Identical (37): _on_term, CapStop, GateFail, Capped, elapsed, over, latin, lines_from_B, Problem, polish, rank_tol,
excess_basis, newton_correct, unsym, sym, cayley_cyclic, xor8, cayley_d5, valid_betas, latin3_all, mate_labels, enc7,
parker_problem, rrr, run, summary, stage_A, stage_L, gate, T1_config, Reduced, lm, run_reduced, summary_red,
parker_reduced, run_perturbed, stop_receipt. Changed: main. Added (8): enc9, z9_array, z9p1_reduced, z9_mutant,
z9_all_betas, z9_canon, z9_config, mismatches. Module level: docstring (v9 paragraph, usage), argv (+Z9_JSON, Z9_SHA,
MODE r9 only), constants OMEGA9, R9_MAX_CLASSES = 256, R9_TARGET_RUNS = 2048. Representation, Reduced, LM, verifier and
run_reduced are therefore unchanged; the Reduced(9, 1, ...) path is executed for the FIRST time (v5 "red1" never ran).

## Stages (all gating before the target, in this order)
1. A, C1, C1p, C2, A5, C3r, C4r, KPc, KRc exactly as v8 (deterministic replays; v8 R7 audit is the reference).
2. A9: the 20 exact Z_9+1 orthogonal pairs x 2 roles (40 instances, eigen-label m* = 0): exact orthogonality re-check,
   reduced residual < 1e-12, full 10x10 verification maxdev < 1e-12 and 10 rays, input sha256 equal to the pin.
   A9m: one-vector mutation of instance (0, A) must give reduced residual >= 0.5 and full maxdev >= 0.5.
3. K9P (near-anchor, as v7 KP): anchor + amp*N(0,1) on all 189 parameters, amps 1e-3, 1e-2, 0.1, 0.5, instances
   (0,A), (1,B), (2,A), (3,B), 4 seeds each (60000 + 1000 ii + 100 ai + j), LM <= 200 iterations. GATE: all 32 runs at
   amp <= 1e-2 verify with 10 rays (local rigidity: classical_tangent_count_z9_v1 found excess 0 at all 40 points), and
   ZERO LM-converged endpoints (reduced residual < 1e-13) fail full verification (model-defect check, all amps).
4. K9R (random recovery of known classical points, as v7 KR): 128 random LM starts (seeds 95000 + k) on random
   classical instances (rng 424242). GATE: >= 64 runs, >= 1 verified, zero converged-but-unverified. Ray counts recorded;
   a verified non-classical endpoint is recorded (not a failure); any maximal endpoint is frozen with theta/Z/B.
5. R9 target (only if every gate passed): ALL Z_9+1 resolution squares with D_inf = {0} up to symbol translation,
   multipliers u in Z_9^* and transposition, m* = 0. Exact count (receipt evidence/z9p1_resolution_classes_v1.receipt.md):
   2,025 squares, 24 classes (12 contain a known classical resolution). Starts per class = max(8, min(64, 2048 // 24)) = 64
   (seeds 90000 + 64 cfg + j), 200 LM iterations: 1,536 runs. Every endpoint verified on the full configuration; ray
   counts; maximal candidate = maxdev < 1e-8, 100 rays, minsep > 1e-6 (theta, Z, B frozen in the JSONL).
   W.l.o.g. claims used for the class reduction (written, in the v9 docstring): D_inf = {0} by column translation;
   m* = 0 because U -> omega^-c U plus a permutation of the eigen-coordinates maps label m* to m* - c; multipliers and
   transposition preserve the Z_9+1 ansatz (generator g -> g^u, rows <-> columns).

## Budgets / resources
Child self-budget 1800 s (stage ends: A..KRc as v8 = 305 s, A9 +30, K9P +90, K9R +150, R9 to 1785 s); supervisor
max_wall 1900 s, settle 120 s; expected wall ~ 60 s (v8 gates) + ~100 s (A9..K9R) + ~700 s (R9; v8 R7 took 0.35 s per
161-parameter LM run, here 189 parameters). RSS expected below the v8 maximum 178.6 MB (trip 2 GiB). Projected
reservation 20 MiB as v8 (JSONL cap 8 MiB in-code, output trip 9 MiB). Launch: fresh code/stability_gate_v2.py
(observer RUN/control/resource_observer_v3.py fe311f28...4196, projected 20,971,520 B) && code/owned_supervisor_v2.py
evidence/rqls_assay_v9.r9.supervisor-config-v2.json, tool timeout 0.

## Consumer rules / claim limits
Normal exit 0 / SETTLED / no trip, cancel or stop receipt; report actual stage counts, verified ray counts, skips. Any
gate failure stops before R9 (GATE_FAIL receipt) and is itself the result (Z_9+1 path not calibrated). R9 misses are a
scoped UNKNOWN for these 24 classes x 64 starts, never nonexistence; recovery rates of known classical points do not
transfer to maximal basins. Any numeric 100-ray lead: freeze immediately, notify parent, no exact claim before
independent exact recognition and checking under a new GO.
