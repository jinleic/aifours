# Checkpoint 021 (rqls10 continuation, successor worker)

Recorded 2026-10-19T05:49:34-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate. No
process of this worker running; lane tmp/ empty. Nothing executed since 05:07 (only static syntax checks of drafts).

## Events since 020
- Parent HOLD on rqls_fixedb_lm_v3 (lm() ignored SIGTERM / stage end / BUDGET). Fixed in code/rqls_fixedb_lm_v4.py
  816884478ae6eb163c328db9c6f3984d7a447260ddbda0e4887d4f5a7310470e (diff review/rqls_fixedb_lm_v3_to_v4.diff
  504f5e85...dd32): deadline/TERM checks inside LM (outer iteration, after assembly, each retry, after each solve),
  statuses TERMINATED / DEADLINE, TermStop at run boundaries and gates, stage end passed through every caller.
- Request v2 review/rqls10-fixedb-GO-request-v2.md cbc89a55...d6cd (Q1 bounded qualification + Phase 1); configs
  evidence/rqls_fixedb_lm_v4.q1.supervisor-config-v2.json 7cb4a51c...d382 (q1 config-v1 3af8de20... superseded, never
  launched) and evidence/rqls_fixedb_lm_v4.p1.supervisor-config-v1.json 0198d797...ff46. Mandatory erratum
  review/rqls10-fixedb-GO-request-v2-erratum-1.md d47a099f...da30 (supervisor status label EXITED, stage windows,
  KP perturbation-size risk, throughput). Parent: keep amp <= 1e-2 KP gating (no v5); a KP failure is an honest
  INCONCLUSIVE Q1. Checkers code/fixedb_q1_check_v1.py 4e695ebb...081c (superseded) and code/fixedb_q1_check_v2.py
  4fd97db4...193e (intended DEADLINE trip vs any other guard trip; never admits Phase 1). Parent preparing a Codex
  review; no launch yet.
- New restricted family (written): evidence/fourier-co-ansatz-v1.md b3a79dd2...44bf - FCO(n) = generalised Huang-Li
  q_ij(t) = omega^(tj + pi(t) rho(i))/sqrt n; 1-RQLS iff (Gamma_pi, Gamma_rho) spectral pair of permutation graphs;
  exact n = 10 necessary conditions (F5); finite exact problem.
- Parent: prepare the FCO source + exact admission request, do NOT launch before an item-specific GO. Done:
  code/fourier_co_enum_v1.py 2b72ec879f44239ba441160b2174baad0b107021be2e2475e7de42dde96e83a6 (0444) and
  review/rqls10-fco-GO-request-v1.md 71b022f459237647f159bfaca6b3b8d8686b2c4ab9a34a77d4f37c62fbc2ac38 (exhaustive
  coverage over all normalised pi without prefilter, exact Phi_n arithmetic, 240 s cooperative budget, controls with
  stated normalisations, M1-M5 mutation controls incl. zero-divisor ray coincidences, immediate stop on a 100-ray hit).
- Parent notes a separate scout (QuantumGroupTableNoGo3) screening the broader Cay(Z_10)/D_5 family.

## Waiting on
Parent: Codex review + item GO for Q1 (v4); pin + item GO for fourier_co_enum_v1. No launches until then.
