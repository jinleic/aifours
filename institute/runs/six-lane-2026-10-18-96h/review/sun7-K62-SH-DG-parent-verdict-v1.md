# K6.2* residue: SH row constraints and DG depth/counting constraints

Recorded at 2026-10-19T06:39:54-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** These are written, model-reviewed results with parent checks of the double-coset divisibility, subset-incidence counting, triangle identities, and repaired P_ob argument. No native computation or Lean verification supports this verdict. K6.2* with e_d >= 4, e* = 2, and full Sun(7) remain **OPEN**.

## Governing texts and scope

- [K62-SH-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-SH-v1.md) `4f17451c60c6018e7fadbca8c36eb92fb23d3e6daef076506aed14f4c5446b5a`.
- [K62-DG-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-DG-v1.md) `a4bfc41e832ebc4e77770cab7a8092a3341827cec93a01bfb437c978c1e84f52`.
- Mandatory [DG erratum 1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-DG-erratum-v1.md) `e435430c6d4ff855871dfa7a9004757561435821dae8f53e7304b10e64626801` and [combined SH/DG erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-SH-DG-erratum-v1.md) `755edc21abdf7484f9187078d7e8cb6b4111f076906e7880085428d54f1b9d75`. Read the base texts only through these corrections.
- Definitions/setting are those of K6.2* in [SETTING-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/SETTING-v1.md) and the accepted [K62-E3 verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62E3-parent-verdict-v1.md). Use R0's finite quotient; no normality is assumed.

## Accepted claims

1. **SH-1, SH-2 and SH(i)-(iii).** Normalize alpha_(d i*) = 1. If alpha*_(d i*) = 1, at most two c in O have alpha*_(i* c) in {1,3}, or equal to 5 with h_d = 0. If alpha*_(d i*) = 3, for c != the 3-marked t, entry 1 is forbidden and entry 5 is forbidden when h_d = 0. When both distinguished entries are 1, the same count applies to alpha. These exclude violating row patterns, not entire exponent/marker regimes.
2. **DG-1.** For nonempty Q contained in O, N(Q) is a positive multiple of n_d / 2^min(e_d,v2(T*_Q)). The proof counts left U_d fibres in a union of (W*_Q,U_d) double cosets; each conjugate of U_d has index n_d. Positivity follows from U_d contained in the intersection. DG-1 itself does not require alpha_(d i*) = 1.
3. **DG-2, DG-3, DG-4.** The subset-incidence bounds and triangle/quadruple depth bounds hold as corrected. In particular a deep triple has edge values (2,4,4) or (4,4,4), with tau* in {8,16}; the latter value requires (4,4,4).
4. **Theorem DG.** In the alpha*-family when alpha_(d i*) = 1, if every four-subset Q has capped depth r_Q = min(e_d,v2(T*_Q)) <= 4, then N(O) <= n_d/16 and

   sum_(|R|=3) 2^(-r_R) <= 19/16 - 2/n_d.

   Consequently there are at least two deep triples, or exactly one deep triple of capped depth **5**, with values (4,4,4), tau* = 16 and e_d >= 5. For e_d = 4 the four-subset hypothesis is automatic and at least two deep triples are required. For e_d >= 5 a four-subset of capped depth >= 5 remains an alternative; this is not excluded. Swap alpha/alpha* only when the corresponding distinguished entry is 1.
5. **P_ob exclusion.** The defined unmarked P_ob of STATUS-v2 is excluded, and the same proof excludes its displayed (alpha,alpha*) matrix pattern under every class-admissible marker placement. It does not exclude arbitrary patterns that passed earlier local tests. The proof forces all ten triangle depths to 3, applies the four-subset bound, and contradicts 10/8 > 19/16 - 2/n_d.

## Reviews and correction disposition

- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-SH-DG-codex-v1.prompt.stdout.txt) `b79975a4babf80a56945714d42626f15c02c2903040cd92bea76307ffefa578e`: observed gpt-6.1-sol, max, read-only; ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 3 MINOR.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-SH-DG-claude-v1.prompt.note.md) `a7af8f2db638b2d795d3c0da5bc9174c97d8e98e62daee18eb4e2389ad904009`: observed claude-opus-5-5, max, no tools; ACCEPT-WITH-FIXES, SH 0/0/3 and DG 0/0/5.
- The combined erratum disposes every listed finding. Parent inspected all 13 corrected items. DG(a)'s exact arithmetic is N(O) >= n_d/8 + 1/3; the consequent contradiction is unchanged.
- The prior DG erratum is a **real gap repair**, not merely wording: both endpoints of a four-path may carry the two markers. The corrected argument selects an unmarked vertex anywhere in the path, each of which has a cycle neighbour, rather than assuming an unmarked endpoint.
- Unembedded L1/VFC citations are withdrawn from DG. Its triangle bounds are derived directly from L0.1/Lagrange; the P_ob common-fibre contradiction uses original-configuration LFC(c) at size 3. No new premise was silently accepted.

## Verification boundary

Direct Sun instances are classical Sun(2), Sun(3), Sun(4) at the exact local sizes used. The accepted LFC/global-reduction provenance still includes the **computer-assisted Sun(5) and Sun(6)**. This verdict does not remove those imports. CAP-62 and DT-A/B/C remain separate unreviewed candidates; accepting DG discharges only their DG dependency. No novelty, priority, unrestricted K6.2* or Sun(7) claim.
