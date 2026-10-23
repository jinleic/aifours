# Sun K6.2*, orientation (1,3)/(3,1): M13 local structure (A-D) accepted at stated scope

Recorded at 2026-10-19T12:42:57-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, written mathematics relative to the parent-accepted imports named in A-D at their original scopes (R0; L0.1 with Lagrange; E1; LFC (a)-(d) and INV (a)-(b) with E6, verdict 8621e744; rules-k7-v1 VFC (V1)-(V4) with L1 (T3), 73a25ba6; K62-E3 Lemma 1, Lemma 2 and Z11 (a), 576969dd; DG-3 G3 form, cae455c3; CAP C1 and RC-i* at the interfaces of CAP-DT verdict 84061c6f), read with the worker overlay and the parent erratum below. The computer-assisted Sun(5) and Sun(6) remain in the transitive dependency closure through LFC/VFC and the K6.2* class reduction. This is **not** an exclusion of (1,3) or (3,1), and not full K6.2*, K7 or Sun(7).

## Setting

K6.2* with e_d >= 4, e* = 2, orientation (alpha_(d i*), alpha*_(d i*)) = (1,3); hence t in O, f* = 1, f_t >= 2; the 5-marker in any admissible placement; all exponents and w-parts unbounded. Orientation (3,1) is covered by INV (a) with E6, exchanging the two families.

## Accepted statements

1. **A1 (a)-(e)** as stated (inverted d-row: |S*_F cap O| <= 3, |S*_F| <= 4, every four-piece fibre contains t and i*, at least n_d/4 + 3 four-piece fibres); **DG-1\*** and **DG-2\***; **DG\*** only under each family's own hypothesis that every 4-subset Q has r_Q <= 4 (automatic when e_d = 4).
2. **C1\***: v2 T_alpha(Q) >= 3 for every 4-subset Q and v2 T_alpha(O) >= 4. **C2\***: n_4(alpha) >= 2 n_1(alpha) + 2 (no four-subset hypothesis).
3. **Joint budget** 2N41 + 2N14 + 5N11 + 3N12 + 3N21 + N22 <= 6, hence N11 <= 1; if N11 = 1 then N41 = N14 = N12 = N21 = 0 and N22 <= 1; N12 + N21 <= 2.
4. **i\*-rows (B1-B3, B section 4)**: |K_alpha| <= 3 and |K_alpha*| <= 3; at least two c in O have alpha_(i* c) >= 3 and therefore alpha*_(i* c) <= 3.
5. **Granularity (C1w, C2)**: gcd(n_v, T_alpha*(V minus v)) = 6 at every unmarked v in O.
6. **Row bounds**: at every unmarked v in O both rows satisfy the nonstrict 5/6 bound (alpha-row by the fresh light-fibre count of the worker overlay using the new alpha*-granularity; alpha*-row by CAP C1, the RC-O opposite-entry-1 instance); both i*-rows satisfy 11/12 by RC-i* at f* = 1. No subset or atom grid and no strict slack.
7. **Cherry isolation**: CI13 and CI13' in both families at every unmarked apex (a, b may be marked); the two section-4 forcing statements of C, each with its unmarked-apex hypothesis.
8. **Unmarked centres (D)**: D4, D3 and L1-L4 at every unmarked centre in O, for every placement of marked neighbours.

## Text of record

| Item | SHA256 |
|---|---|
| [Frozen scope](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-SCOPE-v1.md) | `e5795694e99c0d0ae535bd0b8edf6d8d58d2fd17683f1abbaf3498ac5ce5d625` |
| [K62-M13-A-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-A-v1.md) | `77ce4077584582c699ce1bec870f2b19c55242bfc05aac99febcfbd69c466a8d` |
| [K62-M13-B-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-B-v1.md) | `455c58f9d35cc165f666eeaec9462e6b6ab6286196450532e619d6c0b9810058` |
| [K62-M13-C-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-C-v1.md) | `13f2c8dc42a95be24b819ec3cf68dbb178140bb2cd876b2c491d941d1e552e12` |
| [K62-M13-D-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-D-v1.md) | `d5fabd614afd1ef626d206df01f165db25883e54668c5ceab1e8ca69b7462194` |
| [Worker overlay K62-M13-erratum-v1 (Codex M1)](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-erratum-v1.md) | `a4c476c10aede99ed77420413eec21549988c93926ce5d5fc081f4feefc346d9` |
| [Review package v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/review-package-M13-v2.md) | `d6a07082aeec148d368b9b9f5334533efb8e1160e185e154a637d729450e7eb3` |
| [Excerpt manifest v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/review-excerpts-M13-v2.json) | `cd1059ca8910e0f97b95c8059eeb3af8e6b71f00a7672a59c03bf8d37642d8f5` |
| [Review freeze v1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13-review-freeze-v1.json) | `2709854a1e208c0d861ee0f20f86f2abda91e3228b9be11ccf8eda395bb9bd08` |
| [Claude v2 freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13-claude-v2-deferred-freeze-v1.json) | `f0704372ebe4d4e54e34269ca7b701349bd90e8b04bf037eaed3678983ae49c9` |
| [Parent erratum v1 (Claude m1-m3, status tags)](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13-parent-erratum-v1.md) | `99276f6d66c15c15d55cfa0346440d9db3b244a8a4b5eb40e5bae5a92d549e29` |

## Reviews

- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13-codex-v1.prompt.stdout.txt) `c8c4184bb4c71df3a34f04dcf1f03424b76df60ea9b229216eea6e89c14ef17d`: gpt-6.1-sol/max/read-only, v1 snapshot. ACCEPT-WITH-FIXES 0 FATAL/0 MAJOR/1 MINOR: every claim group ACCEPT except the C:58-63 row-consequence citation, for which Codex supplied the explicit light-fibre derivation; the worker overlay implements it.
- [Claude v1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13-claude-v1.prompt.receipt.json): NO_VERDICT (capacity), never counted as approval.
- [Claude v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13-claude-v2.prompt.note.md) `53c3a6de375b2c69e8b5d1ea2572f8c0908b5f89f871f2cde44666324f72333a`: claude-opus-5-5/max/no tools, corrected snapshot with the overlay applied last. ACCEPT-WITH-FIXES 0 FATAL/0 MAJOR/3 MINOR (premise narrowing, definitions and the tau = 4 reason, D premise pointer), all disposed in the parent erratum. It re-derived A1, DG, C1w, the overlay row proof, CI13/CI13' and every B/D certificate.

## Parent independent checks

- DG-2*: b_3 + 2b_4 + 3b_5 = n_d/2 and b_3 + b_4 + b_5 >= n_d/4 + 1 give b_4 + 2b_5 <= n_d/4 - 1; the triple and four-subset counts use C(3,3), C(4,3), C(5,3) = 1, 4, 10 and C(4,4), C(5,4) = 1, 5.
- Four-piece fibres are forced: the inverted incidence total is 5(n_d/2) + 3n_d/4 = 13n_d/4 > 3(n_d - 1).
- C2*: with n_1 + n_2 + n_4 = 10, 4n_1 + 2n_2 + n_4 <= 18 is equivalent to n_4 >= 2n_1 + 2.
- Budget consequences follow from 5*2 > 6, 3*3 > 6 and the residual budget 1 when N11 = 1.
- The two reviews' claim tables coincide claim by claim; their D3/D4 certificate values agree (11/2, 11/2, 6, 15/2, 13/2 or 11/2, all > 5).

## Open

Rows centred at t (always marked here) and at p in O with p != t; every global graph conclusion (no-K4, bowtie, diamond, free family, joint-pattern division) and the G-only DT-C counts; (4,4,4) triples with tau = 8; a deep triple at a marked apex; for e_d >= 5 the capped-depth->=5 four-subset alternative in each family; exclusion of (1,3)/(3,1); full K6.2*, K7 and Sun(7). Exploratory derivation preceded the scope freeze, so no preregistration claim. No Lean, human-referee, novelty or priority claim.
