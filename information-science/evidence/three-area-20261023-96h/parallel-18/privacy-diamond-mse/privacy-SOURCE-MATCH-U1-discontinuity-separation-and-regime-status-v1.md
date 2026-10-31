# SOURCE-MATCH-U1: a discontinuity separation at every ε, and the exact regime-split status

Owner InfoResearch96h-2, original info-1. Actual `/bin/date` observed before this file was first written: **Tue Oct 27 06:49:37 PDT 2026**; the file was written after checkpoint 191. Status: **AUTHOR-WRITTEN, UNREVIEWED**, under v207 (SHA256 12542cf8…e8f8). Written reasoning only. This does not edit the ledger `privacy-current-source-equivalence-priority-ledger-v1.md` (SHA256 7720dad7…827f) or the packets v1 (050e469f…d450) and v2 (89db15ba…c936). It is a prospective status successor for the SOURCE-MATCH-U1 row of the ledger's §5 only.

## 1. Lemma (the optimal law has no continuous density version)

Fix any finite ε > 0. Let μ_* be the unique optimal law of LAW642 §1, with density p_* = Z_*^(−1)·b^(n_*), core S_* and n_*(z) = min{k ≥ 0 : z ∈ S_* + kD}.

S_* is compact and convex with nonempty interior: LAW642 §8.3 shows it is convex and contains [−t_*, t_*]² with t_* > 0. Hence every boundary point x0 of S_* is:
- a limit of interior points of S_*, where p_* = Z_*^(−1);
- a limit of interior points of the open set int(S_* + D) minus S_*, where p_* = Z_*^(−1)·b.

The second claim holds because x0 + δ·u lies outside S_* for a suitable direction u and small δ > 0, and it lies in the interior of S_* + D since D contains a neighbourhood of 0.

Suppose a continuous f equalled p_* almost everywhere. Then f would equal Z_*^(−1) on the closure of int S_* and Z_*^(−1)·b on the closure of the open shell. Both closures contain x0. This contradicts b < 1. ∎

**Consequence (all ε, no allocation needed).** LAW642 makes μ_* the unique minimizer as a LAW. So every feasible law with a continuous density version has cost STRICTLY above V at every finite ε. Therefore no source CONCLUSION whose optimal, attaining or equality law has a continuous density can instantiate T-MATCH at any ε. The first failed implication is that its optimizer is not μ_*. At the statement level this separates:
- the product-Laplace optimum of KHP (log-Lipschitz class);
- K-norm mechanisms (AS21, JY24);
- elliptic/Gaussian programs (JY24, DA26; Gaussian is moreover infeasible for pure DP at finite ε, as DA26 itself states);
- spherical generalized-gamma laws (Wei).

This is a fact about those families' optimizers. It is NOT a reading of the unread ranges of those sources. Any other statement in their unread ranges remains uncovered.

## 2. Exact regime-split status of the remaining staircase-type sources

The threshold is that of v2: ε_t = 2·arcsinh(√s_t), where s_t is the unique positive root of 2s³ − 9s² − 108s − 81.

| Source chain (recorded coverage per ledger §4.1) | ε > ε_t (rounded core) | ε ≤ ε_t (diamond core) |
|---|---|---|
| G13 v1 (ALL 1073 lines), G15 (ALL 372 lines + image) | Separated: the homothetic l1 staircases are norm-radial, and NORM148 + v2 give a strict gap. | Their family CONTAINS μ_*. Their formal theorems are l1-cost; the missing implication is the mixed-cost all-law bound E_μ‖Z‖₂² ≥ (2/3)·V1 with equality only at μ_*. G13's posed squared-Euclidean question is answered AFFIRMATIVELY here, by LAW642 + v2, not by any source. |
| K25 (ALL 995 lines), MDA (ALL 1999 lines; adopted alternative proofs) | Separated (norm-radial matching-norm staircases). | At the MDA per-cost interface (cost r ↦ r²), μ_* is the all-law optimizer of E‖Z‖₁², with V = (2/3)·V1. This ENLARGES positive prior overlap. The missing implication is the same mixed-cost bound: the cost ‖z‖₂² is not a function of ‖z‖₁. |
| SCDF 2011/2013 (all slides; accepted manuscript complete) | Its arbitrary-core shell family contains μ_* (ledger cut LAW642 + BRANCH-OLD). | Same. In both regimes the first failed implication is that concentration-order minimality supplies no squared-Euclidean selector or exhaustive equality. Never separated by v2. |
| EG16/EG18 (entire 521/499 lines) | The framework embeds the registered model and supplies generic attainment. | Same. In both regimes no selector/value/unique-law statement exists; the circularization hypotheses differ. The printed regulated-density infimum edge is still not cleared, which is a correctness, not a matching, issue. |
| Gilani 2025 (ALL 786 lines) | Scalar programs; no planar angular/core selector. | Same. |
| Q26 (ALL 943 lines), LCR original/extended | Different privacy class/objective (metric privacy; KL). | Same. |
| R2DP/UDP-FL (1–110 of 2276 / 1–110 of 1453), GVapprox (1–100 of 1547), scalar GV (selected), LCR scalar (1–550 of 1284) | Templates contain staircase laws; discrete/approximate/scalar statements. | Same. Unread ranges are UNCOVERED; no exclusion is claimed. |
| AS21, JY24, Wei, DA26, AG26 (selected ranges only) | Continuous-optimizer statements separated by §1 at every ε. | Same. Unread ranges are UNCOVERED. AG26 is still an all-pair-LDP Fisher objective. |

## 3. The exact missing statements (what v207 asks to be reported)

1. **Diamond regime, ε ≤ ε_t.** T-MATCH is equivalent, at LAW642 + v2, to the following. For EVERY feasible Borel law μ under the full closed diamond D at this ε,

       E_μ‖Z‖₂² ≥ (2/3)·inf_ν E_ν‖Z‖₁²,

   with equality ONLY for μ = μ_*, the homothetic l1 staircase with core q*·D. No source in the recorded inventory has been located that states or implies this. The fully read G13, G15, K25 and MDA formal theorems concern costs that are functions of ‖z‖₁. SCDF, EG and Gilani provide no squared-Euclidean selector.
2. **Rounded regime, ε > ε_t.** T-MATCH additionally needs the rounded-core selector of LAW642's R-system together with all-law equality. Every norm-radial or continuous-density source conclusion is strictly separated (§1, v2 §7(ii)). The remaining non-separated families are SCDF shells, EG and the templates, and none of them supplies an MSE selector.
3. **Coverage limits that remain.**
   - the unread ranges of AS21, JY24, Wei, DA26, AG26, R2DP, UDP-FL, GVapprox, scalar GV and LCR scalar (exact line ranges in ledger §4.1);
   - sources outside the recorded inventory;
   - publisher-final versions where only preprints or accepted manuscripts were read.

   No worldwide absence, firstness, novelty or priority clearance is claimed. An independent full-result/priority audit has still NOT been performed.

## 4. Process

The inputs are v207, the own ledger, LAW642 §§1/6/8 and packets v1/v2. The ledger's coverage rows are used as recorded; no source body was re-read for this file. Written reasoning only. ENTIRE116, cp102/AD33, cp108, the guides and the v156 bodies are unused and unopened. Same 18/OWN/HOLD/immutable. Science cutoff 2026-10-27T11:05:38-07:00.
