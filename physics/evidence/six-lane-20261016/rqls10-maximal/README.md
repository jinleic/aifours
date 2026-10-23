# rqls10-maximal — maximal-cardinality 1-resolvable QLS of order 10 (physics slot 2, transition 45)

**Status: UNKNOWN.** There is no candidate witness and no unrestricted nonexistence proof. The lane holds:
- a frozen representation;
- an exact definition-level checker with controls;
- restricted-ansatz derivations R1-R8 plus one sub-case, all unreviewed, ansatz-only, and with external imports
  marked;
- one parent-authorised float probe, which stopped at DISK_FLOOR, so its outcome is UNKNOWN.

Nothing here claims novelty, priority or significance.

- Lane created: 2026-10-18T14:02:07-0700 (`/bin/mkdir`, exclusive).
- Owner: PhysRqls10 (subagent of Main).
- Root: /Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/rqls10-maximal.

## Inputs (read-only)

- Contract: institute/runs/six-lane-2026-10-16/screening/phys-2-rqls10-contract.json, sha256
  0adc1f92552936f8dbbaa5dcdc82a92c9a8aac32bd40481d835ab0c180750f16. Verified 13:47:26 PDT.
- Priority pre-check: screening/phys-2-rqls10-priority-precheck-v1.md, sha256
  4c62b2435ae08d8ce26b8554afceedf47b60891d41f561f69a6a18df4354aec5. Verified 13:47:26 PDT.
- Primary source: Zhang-Cao arXiv:2608.29201v2 (7 Sep 2026). The arXiv HTML was read, and the e-print was fetched
  into memory only:
  - e-print tar.gz sha256 127bef1882685dcaa03927f9e64ac27a71c14a468d26fcb22368f138eb7d21b6 (19956 bytes);
  - RQLS.tex raw sha256 39d0e4b67a8de5e8f30c8065bdf0999fe728c27b10672c4007176468757c417f.
  - Order 10 is explicitly listed as open (Thm 1.3, Section 5).
- Parent priority scout (IRC, about 14:05 PDT): NONE_FOUND_IN_SCOPE.
  - 2609.24653 (symmetric, at most 55 rays, one diagonal transversal) and 2609.29070 (full-rank) do not resolve
    order 10.
  - Han 2507.20154's order-10 pair has at most 13 rays.
  - A search miss is not novelty.

## Files (all frozen read-only after writing; sha256)

| file | sha256 | role |
|---|---|---|
| representation-v1.md | de4b30b3edde35504cde60bfebffe90ec4299102b5e9ac25a1b4918c4d3b40a9 | frozen representation, predicate MAX10, initial obstacles (14:11 PDT) |
| restricted-results-v1.md | 4ccf86cd600f7aba525e828f6a363a120c5076c945cda98388bb38bdbbdb111e | detailed derivations R1, R2, R3 (full proof), R4, R5, R6 |
| restricted-results-addendum-1.md | 7ee05dd21d8c90e6fcbe6bfe331827ae19b1558e68d0fcc1be1bc8d064c15a28 | R7: qubit (x) pairwise-non-orthogonal-bases product ansatz |
| restricted-results-addendum-2.md | 5bebfb32aacd671a6391cd782a5c474d41e715d7170477b250cdf7621d90a07a | R8: controlled tensor products; list of open split families (4+6 corner split is parity-feasible) |
| restricted-results-addendum-3.md | 61bee974951ca6580835afc9f6493d253c8d13ba65c25df75ec2d80235fa5101 | flat 5th-root half-splits: exact combinatorial family; uniform-direction sub-case closed; mixed open |
| exact_rqls_checker_v1.py | 90aaf3beefd049087b7b3d5f00644884a7a99bebcdfdbf90d26c2985cbe89a5d | exact Q(zeta_N) checker: P1 Latin, P2 norms, P3 30 line ONBs, P4 nonparallel by 2x2 minors |
| controls/zhang_cao_ex24_cells.json | ec2bd177b32f17b61d98193fa2b54146aef4ffe50b02b5c78c3b3b43e935fdf5 | extracted source Example 2.4 (v=8) cell strings, with provenance |
| controls/build_controls_v1.py | 5ad382d173d248dbeeb993413b346dfc036cfdcec55e7dfa7d03840cc8916a9d | builds C1-C5 |
| controls/C1_ex24_positive.json | da95d0921259bae04a679adf47fd6b09620bf3d5e06dd5decc92b1220bb5b18c | positive control |
| controls/C2_classical_nonparallel_negative.json | 3c91eabd80f1212ecac6a0d586a0b7e643b36b2f5c1a6833b6ec05f49642b4bc | P4-only negative |
| controls/C3_phase_mutation_negative.json | bbf612577e3a1f62d8cd5192c9ac20a254f60af9e7ad8f9a04a7953d89a8385c | P3 negative |
| controls/C4_latin_mutation_negative.json | 6e7f9e63a7ff9c22b2895060b8a71828182a63f9b24d9fb38f803d918cf4effe | P1 negative |
| controls/C5_norm_mutation_negative.json | c1ad2a56c25d2fa782957d4f15df8f4fb3334c9501ad117dce2749de5eec7f82 | P2 negative |
| controls/controls-receipt-v1.md | 276c72de8cd69011d324bf3961876001b3139d6960f3b6eb029fefcc504cb2d2 | control commands and results |
| probes/numeric_structure_probe_v1.prereg.json | da184627296edbb6f2cb803109eb78c143d82ee8db08b0cf7e8e4b608f3ff07e | pre-registration (frozen 14:15:29 PDT) |
| probes/numeric_structure_probe_v1.py | 268edffc29703fe9ccdd73de5a3c0f7bacf3e89299073a78162f21db2a454910 | the single parent-GO float probe |
| probes/numeric_structure_probe_v1.result.json | b854adf9a9fa8adc80bbb3f07a120f1495f9ffdf14fc00e00390b86e748d6346 | probe output (9141 bytes) |
| probes/numeric_structure_probe_v1.receipt.md | be1949c68619525844ad08697501b9e73cd7d13f57ef38a53b3665d2bd3dcfac | probe receipt |
| probes/numeric_structure_probe_v1.receipt-addendum-1.md | 87bdd775dd0b9080ddd54576a07e140b5e39f3c711abf0f73c31e72ed7dcbbbb | withdraws the "not the writer" clause; causal writer unidentified |
| probes/__pycache__/numeric_structure_probe_v1.cpython-314.pyc | 4bb2e8bacb2b73e315996ef2b785ec94b9d2a571df5c3f64b849537594cfd009 | py_compile side effect, lane-local, retained |

The tmp/ directory is a lane-local TMPDIR and is empty.

## Commands actually run (host times PDT, 2026-10-18)

- 14:02:07 `/bin/mkdir rqls10-maximal`, then `/bin/mkdir rqls10-maximal/tmp`.
- 14:13:32 `/bin/mkdir probes`.
- 14:15:01 `python3.14 -m py_compile probes/numeric_structure_probe_v1.py`. This created __pycache__.
- 14:15:29 Freeze (`chmod a-w`) of the probe and prereg. Admission `df -k`: free 13,481,033,728 bytes.
- 14:15:38-14:19:49 `cd probes && /usr/bin/env TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 numeric_structure_probe_v1.py numeric_structure_probe_v1.result.json`.
  - EXIT=0.
  - stop_reason DISK_FLOOR free=11999363072, at elapsed 251.2 s.
  - Fresh df at 14:20:05 PDT: 11,771,092,992 bytes.
- 14:17:06 Freeze of the checker, builder and Example-2.4 strings. Then
  `TMPDIR=<lane>/tmp PYTHONDONTWRITEBYTECODE=1 python3.14 build_controls_v1.py`.
- 14:17:06-14:17:13 `python3.14 ../exact_rqls_checker_v1.py C{1..5}*.json`, with summary fields printed by
  /usr/bin/python3. Results are in controls/controls-receipt-v1.md.
- Every other action was file writes or reads, `shasum` or `chmod`.
- Process discipline: no other computation was launched. No deletion, overwrite, /tmp use, Git, paid API, external
  contact, global config change or native solver.

## Results

1. **Checker controls (exact, Q(zeta_8)).**
   - C1, source Example 2.4: ALL_PASS. 64 pairwise non-parallel rays; all 24 lines are ONBs.
   - C2 (classical): fails P4 only, with 8 rays and 224 parallel pairs.
   - C3, C4 and C5 fail exactly P3, P1 and P2 respectively.
2. **Numeric probe** (float; NOT a certificate; one run only; stopped at DISK_FLOOR, hence UNKNOWN).
   - W5 control converged to 6.7e-32.
   - WH10 best residual: 0.0523 for lambda in {3,7}; 0.2020 for lambda in {1,9}. No candidate.
   - G8 control is weak: maxdev 8.5e-6, above the 1e-9 threshold. It is not a successful sensitivity control.
   - G6 calibration stalled at 4.82.
   - G10 (Cay(Z10)) was truncated: 7 starts, all stalled at f = 11.4-13.2.
   - No reconstruction lead.
3. **Restricted-ansatz statements.** Unreviewed, ansatz-only, not no-go theorems for the target.
   - R1: laminar coordinate trade rotations from a classical MOLS(10) pair always repeat rays.
   - R2: superposing two classical mates always repeats rays.
   - R3: in the flat Fourier-permutation family q_ij(t) = omega^{i mu(t)+jt}/sqrt10, every transversal fails when
     mu(t) - t is non-constant mod 2. So at most 50 rays, for every B. The proof uses de Bruijn vanishing sums, CRT
     forcing and Rédei [IMPORT].
   - R4: Z_10^2 regular translation-orbit ansatz. Three of the four cocycle cases are impossible. The WH10 case is
     UNKNOWN (numerically infeasible, not proven).
   - R5:
     - rectangular 5+5 half-splits fail by Mann parity;
     - a dim-2 part always repeats rays;
     - a closed 3x3 dim-3 block repeats rays.
   - R6: common orthogonal subsquares have order at most 5, hence are classical [IMPORT].
   - R7: sigma (x) e with e from pairwise non-orthogonal bases of C^5 (e.g. MUBs) repeats rays. The classes are
     essential to this.
   - R8: controlled tensor products, 2x5 and 5x2, give at most 50 rays or are not resolvable.
   - Flat 5th-root half-splits: the uniform-direction sub-case is rectangular, hence fails by Mann parity. The
     mixed-direction case is open.

## Remaining obstruction (exact)

- **Positive direction.** No construction is known in any family not covered above. Open families include:
  - non-rectangular 5+5 and 4+6 / 3+7 / 3+3+4 splits;
  - general product sigma (x) e with arbitrary e in C^5;
  - mixed-direction flat 5th-root half-splits;
  - Parker-type Z_7 + 3 quantum prolongations;
  - non-abelian or non-regular group-orbit ansätze;
  - unstructured vectors with a non-group B.

  Every structured family whose Z_2 part is labelled (classical bits, Fourier signs, rectangular halves) hits a
  parity obstruction of the Hall-Paige, Mann or Rédei-plus-parity kind. A 1-RQLS has 3 ONB lines per cell, so
  naive real counting is overdetermined by a factor 1.5. Solutions must therefore be special algebraic objects.
- **Negative direction.** An unrestricted proof must handle every Latin square B and every complex vector. Even
  v = 4, 5 required the Ball-Simoens case analysis. No route exists within the lane's permissions.
- **Next step, if the parent authorises it.**
  - Run a pre-registered exact combinatorial search (SAT/CSP) in the mixed-direction flat 5th-root half-split
    family, or in non-rectangular 4+6 splits.
  - Alternatively, run a numeric alternating-projection search on non-group B with a classical mate, adding a
    ray-separation penalty. Any lead must then be reconstructed exactly and checked by the exact checker, an
    independent second checker, and both hostile reviews.

UNKNOWNs preserved:
- the WH10 sub-case;
- quantum orthogonal mates of Cay(Z10);
- every open family above;
- the target itself.
