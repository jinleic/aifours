# Recommendation after Theorem A screen — v1 (2026-10-19T00:27:30-0700, ContinueCFR21)

## Cost calibration results (frozen stdlib probes; ownership records = each probe's launch.json)
* p10b (n = 13 control, probe_involution_mrv_cost_v2.py c1d3da2d…): 14 canonical H; H1-13 have empty G_h, H14 has
  36 elements and 112 compatible ordered pairs, all re-checked as DMs — matches the old lane's per-H SAT verdicts
  (13 UNSAT claims, 1 SAT) on the same pinned list (2b279b1e…).
* p10c (n = 21, mu = 1, first canonical H of the pinned 15,715-list fa724ba0…): orbit-MRV + coverage pruning explored
  37,934,080 nodes in 240 s and did NOT finish (INCOMPLETE_BUDGET; launch record evidence/probes/
  p10c-involution-mrv-n21-mu1-v1/launch.json, stdout b4beb9b0…). Together with the old lane's C measurements
  (>= 9 s/H for g10, >= 43 s/H for g00) the order-2 closure stays >= ~300 core-hours.

## Recommendation
1. CFR(6,21): mark NATIVE-BLOCKED with reason "no bounded experiment with decision value fits the lane caps":
   order-2 symmetric closure >= ~300 core-hours; any unrestricted route (row-triple classes ~1.8e8 x ~74 s)
   ~ 4e2 core-years; generic stratum has no generating mechanism (generic-analysis-v1). Deliverables stand:
   Theorem A (parent CORRECTNESS-ACCEPTED scoped partial) + errata, Lemma B, Proposition C (both unreviewed),
   calibrations. Target stays OPEN.
2. A frozen replacement info-2 target is justified. Candidate from this lane's analysis (needs the parent's own
   primary open-status contract): construct 6 MOLS of order 39 or 51 through a 7-row cyclic difference matrix
   (equivalently CFR(6,39) / CFR(6,51)). Primary status evidence read now: Miller-Abel-Valkov-Fraser 2024 (Symmetry
   16:1678) Table 1 gives N(33) >= 5, N(39) >= 5, N(51) >= 5 (unchanged from the Handbook), and Sage's database
   (develop, sources/sage-database-develop.py sha 761494dd…) has only 6-row cyclic DMs for 21, 33, 35, 39, 51.
   The same calibrated random model that matches omega(Z15) = 3 and the rarity of Z21 DM6 predicts ~20 classes of
   7-row Z39 DMs and astronomically many for Z51, versus ~1e-18.6 for Z21 [HEURISTIC; existence in that model does
   not imply findability: a random 6-row Z51 DM extends with probability ~e^-75, so a structured search is needed].
   Not yet screened: Janiszczak-Staszewski 2019/Abel et al. 2024 search scopes at n = 39, 51; 2025-2026 arXiv/
   DataCite; CPro1 does not list these n. Priority/open status must be frozen by the parent before any work.
