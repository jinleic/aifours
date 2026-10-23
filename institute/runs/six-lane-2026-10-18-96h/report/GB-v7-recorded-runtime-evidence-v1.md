# GBv7 historical runtime evidence — recorded facts, not a fresh qualification

Recorded 2026-10-21T05:57:36-0700 (`/bin/date`). This appendix supplements the full-window report and the native authority index. It gives actual recorded control/outcome facts rather than claiming that a filename or hash proves qualification. The focused review packet supplies the full historical admission, control audit/release, all six GOs, three PASS releases and three UNKNOWN audits. No native job, guard test or checker replay was run for this closeout.

## Admission and control qualification

[moqls8-GBv7-admission-parent-decision-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-GBv7-admission-parent-decision-v1.json) — SHA256`a6e641ef55361c65def955f16e2b421830450b3350c843a21a6683047ab88fda` admitted CONTROLS after the package erratum, NOT automatic science. It scoped the exception to the GB driver/launcher lineage, which did not use the held generic supervisor. Its recorded residual risk is the launcher's final wait for its own driver (the driver has internal stage backstops); no universal boundedness certificate is inferred.

[moqls8-gb-gbs7-controls-parent-audit-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-gb-gbs7-controls-parent-audit-v1.json) — SHA256`5ac0f1d283cf62c480874e7d54e779525b8e3a0a31d462e4a53f6c74e5550a5a` records seven controls and clean settlement. The final conclusion is controls-only; subsequent science required a separate GO per item. Negative controls are successful detections, not scientific UNSAT claims.

| Control | Recorded preregistered outcome | Recorded reasons |
|---|---|---|
| gbs7-ctl-unsat | PASS | none |
| gbs7-ctl-sat-checker | AS_PREREGISTERED_NOT_VERIFIED | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified |
| gbs7-ctl-short-cnf | AS_PREREGISTERED_FAIL_CLOSED | checker_feed_measured_complete |
| gbs7-ctl-truncate | AS_PREREGISTERED_FAIL_CLOSED | feeder_plain_complete, proof_fed_equals_collected |
| gbs7-ctl-suffix | AS_PREREGISTERED_FAIL_CLOSED | feeder_plain_complete, proof_fed_equals_collected |
| gbs7-ctl-digest-alter | AS_PREREGISTERED_FAIL_CLOSED | feeder_plain_complete, proof_fed_equals_collected |
| gbs7-ctl-early-close | AS_PREREGISTERED_FAIL_CLOSED | feeder_plain_complete, proof_fed_equals_collected, checker_status_exact_verified, checker_no_fatal_diagnostic, checker_header_counts_match, checker_consumed_proof_bytes_equal_fed |

## Six distinct strengthened attempts

These are literal parent-audit measurements, not fresh replay. A solver UNSAT line alone is insufficient; UNKNOWN is preserved when independent checker completion fails. All three UNKNOWNs have driverexit3 and no qualifying science release. No retry/F2/cap/budget increase is authorized.

### P1-B1.M2 — recorded exact-input PASS

[moqls8-gb-gbs7-P1-B1.M2-parent-audit-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-gb-gbs7-P1-B1.M2-parent-audit-v1.json) — SHA256`5bdbd27dec87f5dc92a8bee85cf3eb35e2f9ab3bc0c05ec80aacfe4cd856d014`.

```json
{
  "item": "gb:P1-B1.M2:a1",
  "formula": {
    "id": "P1-B1.M2",
    "kind": "strengthened",
    "bytes": 350552783,
    "sha256": "1873f550493e6f74c65fa6b185b0f499551dece56822258dbfbaac3338813687"
  },
  "measured_formula_feeds": {
    "solver_feed": {
      "written": 350552783,
      "expected_len": 350552783,
      "limit": 350552783,
      "sha256": "1873f550493e6f74c65fa6b185b0f499551dece56822258dbfbaac3338813687"
    },
    "checker_feed": {
      "written": 350552783,
      "expected_len": 350552783,
      "limit": 350552783,
      "sha256": "1873f550493e6f74c65fa6b185b0f499551dece56822258dbfbaac3338813687"
    }
  },
  "proof": {
    "collected_bytes": 1104607693,
    "collected_sha256": "08cd39b0680f778643eb96ab605467ca52d2925f4d615f055868447b7c696d90",
    "fed_bytes": 1104607693,
    "fed_sha256": "08cd39b0680f778643eb96ab605467ca52d2925f4d615f055868447b7c696d90",
    "checker_parsed_bytes": [
      1104607693
    ],
    "undelivered_bytes": 0
  },
  "native": {
    "solver": {
      "rc": 20,
      "exited": true,
      "exit_code": 20,
      "signaled": false,
      "term_signal": null,
      "sigterm_sent": false,
      "maxrss_bytes": 3772694528,
      "wall_seconds": 2152.483,
      "user_seconds": 2146.795,
      "sys_seconds": 3.984,
      "reaped_at": "2026-10-19T06:55:08-07:00",
      "reaped_mono": 1260758.314551833,
      "wall_seconds_raw": 2152.4831173748244,
      "reaped_epoch": 1792418108.798132
    },
    "checker": {
      "rc": 0,
      "exited": true,
      "exit_code": 0,
      "signaled": false,
      "term_signal": null,
      "sigterm_sent": false,
      "maxrss_bytes": 4064444416,
      "wall_seconds": 830.417,
      "user_seconds": 827.336,
      "sys_seconds": 1.02,
      "reaped_at": "2026-10-19T07:08:59-07:00",
      "reaped_mono": 1261589.436494375,
      "wall_seconds_raw": 830.4169467501342,
      "reaped_epoch": 1792418939.9239612
    }
  },
  "status_lines": {
    "solver": [
      "s UNSATISFIABLE"
    ],
    "checker": [
      "s VERIFIED"
    ]
  },
  "resources": {
    "peak_pipeline_aggregate_rss_bytes": 5950128128,
    "peak_driver_rss_bytes": 1900871680,
    "peak_lane_total_rss_bytes": 5970116608,
    "min_free_bytes_in_flight": 185852313600,
    "pipeline_seconds": 2983.735
  },
  "scope": "Exact bound strengthened input only. Shared representative-set imports remain shared imports, not independently verified by these proof bytes."
}
```

### P1-B5.M3 — recorded exact-input PASS

[moqls8-gb-gbs7-P1-B5.M3-parent-audit-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-gb-gbs7-P1-B5.M3-parent-audit-v1.json) — SHA256`a9a7cd354074031402c701a78f5f35765fa16041e9565cbb1148378581f65e4e`.

```json
{
  "item": "gb:P1-B5.M3:a1",
  "formula": {
    "id": "P1-B5.M3",
    "kind": "strengthened",
    "bytes": 350552778,
    "sha256": "0ae019350469470e5a232e8b70a263dedbc2598ff628fc06ecd2c26c17ef7c51"
  },
  "measured_formula_feeds": {
    "solver_feed": {
      "written": 350552778,
      "expected_len": 350552778,
      "limit": 350552778,
      "sha256": "0ae019350469470e5a232e8b70a263dedbc2598ff628fc06ecd2c26c17ef7c51"
    },
    "checker_feed": {
      "written": 350552778,
      "expected_len": 350552778,
      "limit": 350552778,
      "sha256": "0ae019350469470e5a232e8b70a263dedbc2598ff628fc06ecd2c26c17ef7c51"
    }
  },
  "proof": {
    "collected_bytes": 941005003,
    "collected_sha256": "d4e380267a2ac4191b54e6d45ff846a92ae7bbed3f1598a95e4032137e9ab87f",
    "fed_bytes": 941005003,
    "fed_sha256": "d4e380267a2ac4191b54e6d45ff846a92ae7bbed3f1598a95e4032137e9ab87f",
    "checker_parsed_bytes": [
      941005003
    ],
    "undelivered_bytes": 0
  },
  "native": {
    "solver": {
      "rc": 20,
      "exited": true,
      "exit_code": 20,
      "signaled": false,
      "term_signal": null,
      "sigterm_sent": false,
      "maxrss_bytes": 3639164928,
      "wall_seconds": 906.295,
      "user_seconds": 902.983,
      "sys_seconds": 2.249,
      "reaped_at": "2026-10-19T07:29:28-07:00",
      "reaped_mono": 1262817.987044333,
      "wall_seconds_raw": 906.2947404577862,
      "reaped_epoch": 1792420168.480051
    },
    "checker": {
      "rc": 0,
      "exited": true,
      "exit_code": 0,
      "signaled": false,
      "term_signal": null,
      "sigterm_sent": false,
      "maxrss_bytes": 3886252032,
      "wall_seconds": 926.376,
      "user_seconds": 924.014,
      "sys_seconds": 1.026,
      "reaped_at": "2026-10-19T07:44:55-07:00",
      "reaped_mono": 1263744.853523166,
      "wall_seconds_raw": 926.3762317090295,
      "reaped_epoch": 1792421095.350796
    }
  },
  "status_lines": {
    "solver": [
      "s UNSATISFIABLE"
    ],
    "checker": [
      "s VERIFIED"
    ]
  },
  "resources": {
    "peak_pipeline_aggregate_rss_bytes": 5551161344,
    "peak_driver_rss_bytes": 1680048128,
    "peak_lane_total_rss_bytes": 5571100672,
    "min_free_bytes_in_flight": 185279942656,
    "pipeline_seconds": 1833.288
  },
  "scope": "Exact bound strengthened input P1-B5.M3 only. P1-B5 template coverage also requires P1-B5.M2. Shared representative-set imports remain shared imports, not independently verified by these proof bytes."
}
```

### P1-B2.M2 — scientific UNKNOWN

[moqls8-gb-gbs7-P1-B2.M2-UNKNOWN-parent-audit-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-gb-gbs7-P1-B2.M2-UNKNOWN-parent-audit-v1.json) — SHA256`574886812b545bc45980968b424f5f18d5591e714ae07ae502ff0e3ecdaa99dc`.

```json
{
  "item": "gb:P1-B2.M2:a1",
  "formula": {
    "id": "P1-B2.M2",
    "kind": "strengthened",
    "bytes": 350552781,
    "sha256": "1aa38ae7c04cd5d8b5f8bd224aa825cee149313d25a3886bb2e76eadf078a3f8"
  },
  "native": {
    "rc": 0,
    "exited": true,
    "exit_code": 0,
    "signaled": false,
    "term_signal": null,
    "sigterm_sent": false,
    "maxrss_bytes": 3640983552,
    "wall_seconds": 3600.343,
    "user_seconds": 3590.541,
    "sys_seconds": 6.73,
    "reaped_at": "2026-10-19T08:47:37-07:00",
    "reaped_mono": 1267507.004936583,
    "wall_seconds_raw": 3600.3425383339636,
    "reaped_epoch": 1792424857.5175319
  },
  "solver_status": [
    "s UNKNOWN"
  ],
  "resource_observation": {
    "peak_pipeline_aggregate_rss_bytes": 4478271488,
    "peak_driver_rss_bytes": 2192818176,
    "min_free_bytes_in_flight": 184266235904,
    "pipeline_seconds": 3600.471
  },
  "explanation": "Native kissat --time=3600 returned rc0/s UNKNOWN after3600.343s, no safety stop or signal. Expected full-pipeline PASS predicates require both children and all checker-stage threads, so false all_threads_finished/children_reaped/no_safety_stop conjuncts do not by themselves show an actual survivor; started-child/thread raw data and parent census establish this attempt ended.",
  "not_a_release": "No moqls8-gb-staged-parent-release/5 attestation may be issued: it requires actual driver exit0 and qualified complete publication. UNKNOWN receipt/commit remain unqualified; no completion file.",
  "coverage": "14/18 unchanged; P1-B2 requires both M2/M4, M2 remains open. No retry, no F2, no cap increase.",
  "actual_settlement_selected": {
    "live_children": [],
    "threads_unfinished": [],
    "helper_survivors": [],
    "fds_left": []
  }
}
```

### P1-B2.M4 — scientific UNKNOWN

[moqls8-gb-gbs7-P1-B2.M4-UNKNOWN-parent-audit-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-gb-gbs7-P1-B2.M4-UNKNOWN-parent-audit-v1.json) — SHA256`74762565fbe7d42ed3a69f78c32ebb8ea03431b764d7c747e2ae17146ade19f0`.

```json
{
  "item": "gb:P1-B2.M4:a1",
  "formula": {
    "id": "P1-B2.M4",
    "kind": "strengthened",
    "bytes": 350552781,
    "sha256": "2544240d14e105b1ec7ff25f9d7366ed9aad6faa2db8b36d4c3af42001698293"
  },
  "native": {
    "solver": {
      "rc": 20,
      "exited": true,
      "exit_code": 20,
      "signaled": false,
      "term_signal": null,
      "sigterm_sent": false,
      "maxrss_bytes": 3638050816,
      "wall_seconds": 3592.626,
      "user_seconds": 3584.384,
      "sys_seconds": 5.518,
      "reaped_at": "2026-10-19T09:54:49-07:00",
      "reaped_mono": 1271538.967585458,
      "wall_seconds_raw": 3592.6256032921374,
      "reaped_epoch": 1792428889.499657
    },
    "checker": {
      "rc": -15,
      "exited": false,
      "exit_code": null,
      "signaled": true,
      "term_signal": 15,
      "sigterm_sent": true,
      "maxrss_bytes": 4187422720,
      "wall_seconds": 339.265,
      "user_seconds": 335.603,
      "sys_seconds": 0.76,
      "reaped_at": "2026-10-19T10:00:29-07:00",
      "reaped_mono": 1271879.098410208,
      "wall_seconds_raw": 339.2652122499421,
      "reaped_epoch": 1792429229.6320908
    }
  },
  "solver_status": [
    "s UNSATISFIABLE"
  ],
  "resource_observation": {
    "peak_pipeline_aggregate_rss_bytes": 6442532864,
    "peak_driver_rss_bytes": 2270035968,
    "min_free_bytes_in_flight": 183131418624,
    "pipeline_seconds": 3932.884
  },
  "explanation": "Actual checker-phase RSS cap stop. Solver rc20/s UNSATISFIABLE is not an independently checked refutation. Full proof collection/feed equality does not establish checker consumption; no VERIFIED or consumed-proof count. One SIGTERM and bounded reap; no science completion or release.",
  "sampled_rss_cap_overshoot_bytes": 81920,
  "not_a_release": "No moqls8-gb-staged-parent-release/5: actual driverexit3 and UNKNOWN unqualified publication.",
  "coverage": "14/18 unchanged; P1-B2.M2 and P1-B2.M4 both UNKNOWN. No retry, F2 or cap increase.",
  "actual_settlement_selected": {
    "checker_TERM_once": {
      "at": "2026-10-19T10:00:29-07:00",
      "event": "SIGTERM",
      "target": "checker",
      "pid": 69014,
      "reason": "pipeline aggregate RSS 6442532864 > cap 6442450944 (driver 2255110144 incl. CNF parts and RAM proof + checker)"
    },
    "checker_reaped_within_grace_upper_seconds": 0.6320908069610596,
    "children_alive": [],
    "threads_unfinished": [],
    "helper_survivors": [],
    "fds_left": []
  }
}
```

### P1-B5.M2 — recorded exact-input PASS

[moqls8-gb-gbs7-P1-B5.M2-parent-audit-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-gb-gbs7-P1-B5.M2-parent-audit-v1.json) — SHA256`6ba224b88fb8af8015a75f304cb8e1f114db4da166e1dce8c892809ec4222c36`.

```json
{
  "formula": {
    "id": "P1-B5.M2",
    "kind": "strengthened",
    "bytes": 350552778,
    "sha256": "6a423719e4f00aa27a2e14acba89c09a02c4b368d7d012adc0224e93830d7065"
  },
  "measured_formula_feeds": {
    "solver_feed": {
      "written": 350552778,
      "expected_len": 350552778,
      "limit": 350552778,
      "sha256": "6a423719e4f00aa27a2e14acba89c09a02c4b368d7d012adc0224e93830d7065"
    },
    "checker_feed": {
      "written": 350552778,
      "expected_len": 350552778,
      "limit": 350552778,
      "sha256": "6a423719e4f00aa27a2e14acba89c09a02c4b368d7d012adc0224e93830d7065"
    }
  },
  "proof": {
    "collected_bytes": 940750621,
    "collected_sha256": "3a505fd10af6dd5a48a906e8ef30e02b10ca21868ef6d35a7147b02f2d21ba2f",
    "fed_bytes": 940750621,
    "fed_sha256": "3a505fd10af6dd5a48a906e8ef30e02b10ca21868ef6d35a7147b02f2d21ba2f",
    "checker_parsed_bytes": [
      940750621
    ],
    "undelivered_bytes": 0
  },
  "native": {
    "solver": {
      "rc": 20,
      "exited": true,
      "exit_code": 20,
      "signaled": false,
      "term_signal": null,
      "sigterm_sent": false,
      "maxrss_bytes": 3629940736,
      "wall_seconds": 1043.706,
      "user_seconds": 1040.152,
      "sys_seconds": 2.345,
      "reaped_at": "2026-10-19T10:25:07-07:00",
      "reaped_mono": 1273356.76454175,
      "wall_seconds_raw": 1043.7055544580799,
      "reaped_epoch": 1792430707.304318
    },
    "checker": {
      "rc": 0,
      "exited": true,
      "exit_code": 0,
      "signaled": false,
      "term_signal": null,
      "sigterm_sent": false,
      "maxrss_bytes": 3895246848,
      "wall_seconds": 945.788,
      "user_seconds": 943.256,
      "sys_seconds": 1.078,
      "reaped_at": "2026-10-19T10:40:53-07:00",
      "reaped_mono": 1274303.070793,
      "wall_seconds_raw": 945.7884873331059,
      "reaped_epoch": 1792431653.6148171
    }
  },
  "status_lines": {
    "solver": [
      "s UNSATISFIABLE"
    ],
    "checker": [
      "s VERIFIED"
    ]
  },
  "resources": {
    "peak_pipeline_aggregate_rss_bytes": 5560696832,
    "peak_driver_rss_bytes": 1680556032,
    "peak_lane_total_rss_bytes": 5580963840,
    "min_free_bytes_in_flight": 182164746240,
    "pipeline_seconds": 1990.294
  }
}
```

### P1-B3.M2 — scientific UNKNOWN

[moqls8-gb-gbs7-P1-B3.M2-UNKNOWN-parent-audit-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-gb-gbs7-P1-B3.M2-UNKNOWN-parent-audit-v1.json) — SHA256`6144c70300a01e02460310df4d79b631370da6fdbe68f3c467a8a40b5ee2061d`.

```json
{
  "item": "gb:P1-B3.M2:a1",
  "native": {
    "solver": {
      "rc": 0,
      "exited": true,
      "exit_code": 0,
      "signaled": false,
      "term_signal": null,
      "sigterm_sent": false,
      "maxrss_bytes": 3641409536,
      "wall_seconds": 3600.14,
      "user_seconds": 3592.174,
      "sys_seconds": 5.758,
      "reaped_at": "2026-10-19T11:44:10-07:00",
      "reaped_mono": 1278099.761931375,
      "wall_seconds_raw": 3600.1401460419875,
      "reaped_epoch": 1792435450.321089
    }
  },
  "solver_status": [
    "s UNKNOWN"
  ],
  "resource_observation": {
    "peak_pipeline_aggregate_rss_bytes": 4475240448,
    "peak_driver_rss_bytes": 2174746624,
    "min_free_bytes_in_flight": 181835943936,
    "pipeline_seconds": 3600.349
  },
  "explanation": "Solver self-budget returned rc0 / s UNKNOWN after3600.140146s; no checker was spawned. Started collector and solver-feed threads ended; solver reaped and parent snapshot is clear. False all_threads_finished/children_reaped science criteria include stages that were deliberately never started; they remain false, not backfilled. No checked refutation, no completion record or science release. Collected RAM proof was not checked/retained as a certificate.",
  "not_a_release": "No moqls8-gb-staged-parent-release/5; observed driverexit3 and unqualified UNKNOWN publication.",
  "coverage": "GB15/18 unchanged; B2.M2, B2.M4, B3.M2 UNKNOWN. No retry/F2/budget/cap widening.",
  "actual_settlement_selected": {
    "children_alive": [],
    "threads_unfinished": [],
    "helper_survivors": [],
    "fds_left": []
  }
}
```

## Consequences and limits

- Three exact-input PASS items: B1.M2, B5.M3, B5.M2. Their formula feeds and collected/fed/parsed proof-byte equalities are recorded; one implementation lineage is not a new independent mathematical encoding/normalization proof.
- B2.M2 and B3.M2: solver self-budget UNKNOWN, no checker spawned. Their deliberately unstarted checker stages leave scientific predicates false; actual ended-process settlement is a different question.
- B2.M4: solver UNSAT in3592.626s, checker terminated for the6GiB pipeline RSS cap after339.265s; sampled overshoot81920B. One SIGTERM and bounded reap were recorded. No VERIFIED/consumed-proof count; still UNKNOWN.
- Final recorded coverage is GB15/18, not full physical n8. Global runtime HOLD remains. Three native attempt settlements do not imply whole-window/current-process settlement.
- These records support an attributed historical report. Raw proof payloads, every source/binary behavior, global safety and original scientific normalization bridges are not freshly verified here. Stage/receipt strings such as `commit` are local publication records, not Git operations.
