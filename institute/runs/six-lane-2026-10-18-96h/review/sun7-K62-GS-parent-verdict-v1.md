# Sun K6.2*: generic sub-case G is empty; every K6.2* configuration has an O-marker

Recorded at 2026-10-19T11:23:24-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, written mathematics relative to the exact parent-accepted imports listed in [K62-GS-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/K62-GS-v1.md) section 1 at their original scopes, read with the [parent erratum](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-GS-parent-erratum-v1.md). The computer-assisted Sun(5) (verdict 2cf02436…5301) and Sun(6) (verdict efe1d849…1e29) remain in the transitive dependency closure through the LFC/VFC package and the K6.2* class reduction. This is not full K6.2*, K7 or Sun(7).

## Accepted statements

Class: the CAP-DT K6.2* setting with e_d >= 4, e* = 2, |O| = 5, n_c = 2*3^(f_c)5^(h_c)w_c. **G**: no vertex of O carries a marker (n_c = 6w_c for all c in O); the 3-marker is on i* (any f* >= 2) or absent; the 5-marker is on d, on i* (any exponent) or absent.

1. **Theorem FB.** In G, for every e_d >= 4, every admissible f*, h_d, h* and w-parts, both families x in {alpha, alpha*} and every 4-subset Q of O: v2 T_x(Q) <= 4.
2. **Theorem GE.** G is empty: no K6.2* configuration in a finite group lies in G, with all exponents unbounded; by R0 the same holds for arbitrary groups with finite-index subgroups.
3. **Corollary OM.** Every K6.2* configuration, in any group with finite-index subgroups, has a marker on a vertex of O: some c in O has f_c >= 2 or h_c >= 1.

## Text of record

| Item | SHA256 |
|---|---|
| [Frozen scope](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/K62-GS-SCOPE-v1.md) | `cdd5f84a27f22661e479c5d8fc9b8713a62273afd758b2f192530eae9a6fc0d7` |
| [K62-GS-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/K62-GS-v1.md), 213 lines | `020fdc7aacf105c224842990dbd434ecd49a86e39e2e70ca0f6ced41b57b4627` |
| [Review freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-GS-review-freeze-v1.json) | `0ef99649cbb61df85174fb61f2cd0f4e3875d28e651d3a45a41176ca48454638` |
| [Queue replacement](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-GS-review-queue-replacement-v1.json) (this standalone review replaced the unlaunched HD/GX second-family reviews) | `ec00e3a37cdb069885813229d70d60e9ca8ae7b5ecec1004bb2c6824cb06a540` |
| [Parent erratum v1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-GS-parent-erratum-v1.md), m1/m2/m4/m5/m6 | `9c60e4187748eddaf7997201a3e208dce7a86ba86a349db1359648c4c797616b` |

## Reviews

- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-GS-codex-v1.prompt.stdout.txt) `fecc0372b94a9bacebeae22387a3fd3d50852f495584d588e462a969ac9d882c`: gpt-6.1-sol/max/read-only. FB, GE, OM **ACCEPT**, 0 FATAL/0 MAJOR/0 MINOR; dependency order acyclic; every import at its original domain.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-GS-claude-v1.prompt.note.md) `1a5527de67ea298ab153864b5b98db9aee69774eac46dfc459395a931845ddd9`: claude-opus-5-5/max/no tools. FB, GE, OM **ACCEPT**; file ACCEPT-WITH-FIXES, 0 FATAL/0 MAJOR/6 MINOR citation or wording. No new-proof gap and no domain violation.

Required dispositions: m2 (TRI was literally false as worded; the proof establishes "any two distinct triangles share an edge", which is all GE uses) and m1 (P1's value set is E3's C2 proof sub-claim (a), not an accepted standalone statement; its orientation hypotheses hold in G for both families) are corrected in the erratum. m4, m5 and m6 are setting, citation and bookkeeping fixes; m3 needs no change.

## Parent independent checks

- P4 apex identity: mu(Phi_c(Phi_a cap Phi_b)) = T(R)/(n_c lcm(n_a,n_b) x_ab) = tau/(6x_ab), using n = 6w in G.
- FB: delta(Q) >= 5 with T16 forces v2 k_e >= 1, so no 1-pair; no K4 gives a nonempty set N of 2-pairs; ONE leaves at most one endpoint with an avoiding N-edge, forcing N = {ab}; then k_b = 2 = x_ba and both apex inclusions give tau = 8 for {a,b,c} and {a,b,q}, contradicting ONE.
- GE step 2: the complement in K5 of a diamond on {a,b,c,q} missing ab is {ab, ae, be, ce, qe}, whose only triangle is {a,b,e}, so the second family cannot carry a diamond.
- OM: absent O-markers, E3 places the configuration in G because d carries no 3-part; GE excludes it.

## Relation to HD and GX

FB has the statement of candidate Theorem HD (K62-HD-v2) and GE is candidate Theorem GX (K62-GX-v1) without its HD condition. Those texts and their pending reviews are not accepted. Their statements are now covered by this verdict through a different, dual-reviewed proof; the HD Codex review 5c885c6a and HD erratum 3c670e5f remain records only.

## Discharged and open

Inside G this discharges the remaining CAP-DT G-patterns (f* >= 2, the 5-marker on d or i*, all exponents) and DG's e_d >= 5 four-subset alternative. Still open: every O-marked K6.2* configuration (3-marker t in O in orientations (1,1), (1,3), (3,1), the last two being the pending M13 candidates; 5-marker in O), full K6.2*, K7, marked K6.3 and Sun(7). Pending candidate K62-MK-v2 (ab7cfcb6) addresses the 5-marker-in-O and (1,1) cases and is not an input here. No Lean, human-referee, novelty or priority claim.
