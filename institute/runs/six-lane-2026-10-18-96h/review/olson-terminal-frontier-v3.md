# Olson terminal frontier v3 — corrected literal unions

Recorded 2026-10-21T04:07:49-0700 (`/bin/date`). This is union bookkeeping from separately accepted verdicts, not new mathematics. It supersedes the parameter attributions and open-cell lists in frontier v2 and both errata, outcomes-v6, the composed paragraph of FC1023 verdict v1/confirmation, and their checkpoint summaries. Those immutable records remain historical. This new table awaits a focused independent binding audit; component theorem acceptances are unchanged.

## Literal scope dictionary

All entries have the full existential antecedent: a length4p−2 word over D_(2p) avoiding an identity2p-subword in increasing original index order has SOME admissible NF with terminal k=p+1 and the stated kappa_hat. Arbitrary extra-pair placement and genuine empty-run rule remain; no o_F/nonempty-run/rigidity hypothesis is added. Every imported component retains its own premises and errata.

- K0T: kappa_hat0 for odd p, relative to Theorem P. LOWER-K1 and K2: kappa_hat1/2 for prime p≥11. P7L: kappa_hat1/2 at p7.
- USK: 3≤kappa_hat≤floor((p−1)/4).
- FCW: p=4kappa−1 prime, kappa≥3. SCW: p=4kappa−3 prime, kappa≥4. TCW: p=4kappa−5 prime, kappa≥4. FQW: p=4kappa−7 prime, kappa≥5. These require kappa_hat=kappa; none applies merely because its name is listed next to a different prime.
- BOTTOM composite: [(p−1)/2,p−2], prime p≥7. PP1-EXCL: kappa_hat=p−1, prime p≥7.
- FC717: (kappa_hat,p)=(7,17). FC19: (7,19),(8,19). FC1023: (10,23), accepted only upon the second-family confirmation.
- UFC U0: prime p≥17, floor((p+7)/4)<kappa=kappa_hat≤(p−3)/2, further kappa≤(3p+5)/8 when p≡1 mod4 or≤(3p+7)/8 when p≡3 mod4. Conclusion: no target NF in this subrange T0.

## Disjoint integer-range partitions

The universal NF/GRX range is0≤kappa_hat≤p−1 (range clarification linked below). Here BOTTOM and PP1 mean the literal intervals above, not a narrower substitute.

| p; terminal k | kappa_hat partition and provider | Remaining open cells at this terminal k |
|---|---|---|
| 7;8 | 0 K0T; 1–2 P7L; 3–5 BOTTOM; 6 PP1 | none |
| 11;12 | 0 K0T; 1 LOWER-K1; 2 K2; 3 FCW; 4 TCW; 5–9 BOTTOM; 10 PP1 | none |
| 13;14 | 0 K0T; 1 LOWER-K1; 2 K2; 3 USK; 4 SCW; 5 FQW; 6–11 BOTTOM; 12 PP1 | none |
| 17;18 | 0 K0T; 1 LOWER-K1; 2 K2; 3–4 USK; 5 SCW; 6 FQW; 7 FC717; 8–15 BOTTOM; 16 PP1 | none |
| 19;20 | 0 K0T; 1 LOWER-K1; 2 K2; 3–4 USK; 5 FCW; 6 TCW; 7–8 FC19; 9–17 BOTTOM; 18 PP1 | none |
| 23;24 | 0 K0T; 1 LOWER-K1; 2 K2; 3–5 USK; 6 FCW; 7 TCW; 8–9 UFC; 10 FC1023; 11–21 BOTTOM; 22 PP1 | none |
| 29;30 | 0 K0T; 1 LOWER-K1; 2 K2; 3–7 USK; 8 SCW; 9 FQW; 10–11 UFC; 12–13 OPEN; 14–27 BOTTOM; 28 PP1 | **12,13** |

Checkable substitutions: at p23,4·6−1=23 and4·7−5=23; USK reaches floor(22/4)=5; UFC bound is(69+7)/8=9.5. At p29,4·8−3=29 and4·9−7=29; UFC bound is(87+5)/8=11.5; BOTTOM begins(29−1)/2=14. In both cases kappa_hat is an integer, so a half-integer UFC bound rounds DOWN.

For primes p≥29 the currently unexcluded terminal middle strip is:
- p≡1 mod4: floor((3p+5)/8)<kappa_hat≤(p−3)/2;
- p≡3 mod4: floor((3p+7)/8)<kappa_hat≤(p−3)/2.
This is the complement of T0 within T; no separately accepted cell at p≥29 is being subtracted. HIGH-COVER/R_U is an unproved equivalent exclusion target, not a proved nonempty obstruction. Other k and full ordered Olson remain open.

## Error history

The report review found p29's false open14 and its inconsistent provider formulas. A further parent check found p23's incorrect attributions at5/6/7, which survived the first frontier erratum: they must be USK/FCW/TCW, NOT FCW/TCW/SCW. The closed-prime conclusion is unchanged after correct bindings, but none of the old erroneous rows is evidence. FC1023 verdict v1's ACCEPTED headline predated Claude and conflicted with its pending/provisional paragraph; no acceptance should be attributed to that headline before its subsequent second-family confirmation.

| Literal authority | SHA256 |
|---|---|
| [olson-K0T-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K0T-parent-verdict-v1.md) | `4a2a2ffd8d8624c33c0f7cc1265cf679c18ac3a9c63565bc093b2e8afc8bf8ba` |
| [olson-LOWER-K1-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LOWER-K1-parent-verdict-v1.md) | `93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83` |
| [olson-K2-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K2-parent-verdict-v1.md) | `5ca98c9a81b2e1607cf5f562bc276ad29ed81feb774857f1428e657293db04c7` |
| [olson-USK-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-USK-parent-verdict-v1.md) | `6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18` |
| [olson-FCW-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FCW-parent-verdict-v1.md) | `b28837c9c8a9549b99a6c2205e8bbe40d65ab1aad265595c511395d4c1738f71` |
| [olson-SCW-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SCW-parent-verdict-v1.md) | `d51b5d8e6c6a7c38047434b3740d477bccd2ab7e0e53ce68ea34aa83486bdfe0` |
| [olson-TCW-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-parent-verdict-v1.md) | `17f6d80d664c4e3b60bb7be5aba560502f5597350b025b3d058d7d989fef0c29` |
| [olson-FQW-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FQW-parent-verdict-v1.md) | `a9388a49e227b3bf418e2250b515860a33f880dba816b5318a834faa5da9e566` |
| [olson-P7L-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-P7L-parent-verdict-v1.md) | `57664b53b35aa0de0729d7ec7b2c2ff4d9b7e738155612c5ffcb43ec169a8569` |
| [olson-BOTTOM-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BOTTOM-parent-verdict-v1.md) | `c5e98b7f84f9b3eb3047d64e05475981c61aa4ef37adbf8e481ec2773f70c481` |
| [olson-PP1-EXCL-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-PP1-EXCL-parent-verdict-v1.md) | `5e501291f084061303224027001b6058554ec2475991343572cbd651b7d80308` |
| [olson-FC717-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC717-parent-verdict-v1.md) | `0f201041f0885e5c88ec7c05739bd67781e8a1619be31202317cc9cd2adb4789` |
| [olson-FC717-parent-verdict-erratum-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC717-parent-verdict-erratum-v1.md) | `30b4ff67f884740029d645a1262594c7dc58a5fa1c113192ac2647e8844a01ea` |
| [olson-FC717-parent-verdict-erratum-v2.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC717-parent-verdict-erratum-v2.md) | `5d9abfc6a5de5939ea08db67bd50b4d1c85cdeacf66150f8a583e5bfd25b5b70` |
| [olson-FC19-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC19-parent-verdict-v1.md) | `7be12861b233714bb4bdd583a91e0c699ddb3302bebbdbb179f443aeb0b54e77` |
| [olson-UFC-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-verdict-v1.md) | `10596e3df9eab24f0451910eb84ae3029721c60a211f9b4b22d5fff943d0c060` |
| [olson-FC1023-parent-verdict-v2-confirmation.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC1023-parent-verdict-v2-confirmation.md) | `33b2d30fca6a723884765b5393fe9e95e2a9f58e0aa1ba2b52103c9f7405a5fa` |
| [olson-terminal-union-range-clarification-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-terminal-union-range-clarification-v1.md) | `c7789ee917f80e558c114a635a4c7b4efda55d3386bd968891a900ddc2bac39a` |
