# Independent same-harness review: anisotropic septic numerator family

Native `/bin/date` observed immediately before this file was created: **2026-10-28T19:01:26-0700 PDT**.

## Verdict and scope

**ONE CANDIDATE: NO DEFECT FOUND within the reconstructed scope. FATAL 0; MAJOR 0; MINOR 0.** The frozen base box is a genuine seven-positive-width monic Hurwitz septic box. The displayed exact-degree-seven `b_new` is common SPR for every member at every finite real frequency, including zero. The same assertion, with the stated uniform bound, holds for every fourteen-endpoint perturbation of radius at most `1/100000000`. The designated `b_old` fails at the actual `(E+,O+)` corner of every one of those boxes. This is a same-harness mathematical review, **not** a parent acceptance, an external-family or human review, a formal proof, or a novelty verdict.

In particular, this does **not** prove that every Hurwitz septic box has an SPR numerator; it does **not** exhibit a box with no common numerator; and it does **not** imply failure of any numerator other than the displayed `b_old`. The closed radius-`rho` set of endpoint vectors contains a genuine open fourteen-dimensional neighborhood, and the width margin below ensures those vectors still describe actual boxes.

## Inputs, identity and completeness

The binding `manifest-v1.json` SHA-256 is `b381c13db497862f912c2a7e84ed54e3d631851c405814e7108df56d824cff75`. I read the following three complete bodies, in manifest order, in exact raw windows; each current SHA-256, byte count and LF count matches the manifest. No pin mismatch was observed. `S`, `C`, `F` below abbreviate the named paths in the manifest, not a different copy.

| Label | Frozen input | SHA-256 | Bytes / LF |
|---|---|---|---|
| S | `written-releases/info-2-septic-box-definitions-v1.md` | `d86737954bee95836e2d2cffade9cba15a99f2bb486b660ada2562c25fc764ad` | 3005 / 37 |
| C | `frontier-20261028-anisotropic-new-numerator-open-family-v1.md` | `25db31d50117b74462a3fc25f22d46f48d2e44e79d28455c0b875eef93063d2f` | 10370 / 119 |
| F | `frontier-20261028-anisotropic-common-numerator-frozen-v1.json` | `41411d5d0f25108a14e1dad8f8ac770ee580867d573206ce4ea22b6cf71005a4` | 17493 / 610 |

The precise registered target is S:13–15, 23–27, 33: monic closed coefficient boxes, degree exactly seven for the numerator, strict positivity for **every** real frequency and every denominator member. The reviewed candidate's endpoints and numerators are C:7–27 and F:5–33, 595–607; its quantified neighborhood assertion is C:29–38. The leading numerator coefficient is exactly one; its rational coefficient denominators are at most 100.

## Independent exact work

My standard-library `Fraction`/integer implementation is `independent-exact-check-v1.py`, SHA-256 `6b711eca5bc2f4f4fe841fce25298cf6e37c15f6093176b394f76fd97dd0be85`. I ran `python3 -B independent-exact-check-v1.py` once; it completed successfully and exclusively created `independent-exact-receipt-v1.json`, SHA-256 `1f9b0a0364d18d2028d43ef2c4c372bc9c8c1727d32cc12447aeaf85a9b7de80`. The code did not import author code; it rechecks the input identities. The receipt contains all 28 corner Hurwitz minors, all six members, margins and control outcomes. It is executable evidence, not a substitute for the following mathematical reconstruction.

### Base stability, all members

1. For `t=w²≥0`, I reconstructed the four parity-extremum cubics from the seven actual intervals (C:42–47; F:498–581). Each has positive constant and negative leading coefficient. All **12** pinned intervals have strictly opposite-sign endpoint evaluations; within each cubic the three intervals are disjoint and positive. Thus each cubic has exactly three distinct positive simple roots and no others. For each of the four cubics, the three sign transitions are `+→−`, `−→+`, `+→−`.
2. Taking the two extrema's enclosing ranges for each root gives six strictly separated bands in the order `E1 < O1 < E2 < O2 < E3 < O3`, with the exact endpoints stated at C:49–56. Outside an E band the two E-extrema have the same nonzero sign, and outside an O band the two O-extrema do too. Since an E band and an O band cannot overlap, at every `t>0` one of the two entire parity intervals excludes zero. At `t=0`, every `a_0>0`. Consequently no box member has an imaginary-axis zero.
3. The actual `(E−,O−)` corner's independently computed Routh first column is exactly the positive eight-entry column at F:582–591. As a separate calculation, rational Gaussian elimination independently gave seven strictly positive leading Hurwitz determinants for **each** of the four actual parity corners; all 28 values also agree with the named author receipt. For the all-member argument, the positive reference Routh column, connected monic coefficient box, and absence of imaginary-axis zeros are sufficient: continuous roots cannot change the Hurwitz count along the segment from the reference corner to any member. Checking the corners alone is **not** being used as a stability theorem.

### Base pairing, all frequencies and members

I formed `P_a(t)=Re[a(i√t)b_new(−i√t)]` directly from complex monomial products, with no author pairing implementation, and matched all four coefficient arrays at F:34–75. If `P(t)=Σ_{k=0}^7 p_k t^k`, then

`Q(x)=(1−x)^7 P(x/(1−x)) = Σ p_k x^k(1−x)^(7−k)`.

The degree-seven Bernstein coefficients of `Q` on `[0,1]` are therefore exactly `p_k / binom(7,k)`. My checker restricts these coefficients to each reported interval by rational de Casteljau splitting. It verified the interval partitions, **every one of the 224** recorded coefficients, strict positivity, the four per-corner minima, and the leaf counts `6, 6, 7, 9` (C:64–70; F:76–497). Their global minimum is exactly

`d = 1050465553521003/96207267430400000 > 0`.

Thus `P_a(t) ≥ d(1+t)^7` at every corner and every `t≥0`. For fixed `t`, the pairing is affine in the independently variable even/odd real-value rectangle, so the same bound holds for **every** member, not merely the corners. With `S=178113/1600` bounding the denominator coefficient L1 norm, `|a(iw)|²≤S²(1+w²)^7`. Therefore the claimed base ratio lower bound is exactly `d/S² = 116718394835667/132469727243471421440 > 0` (C:70–72; F:592–594).

### Explicit six-member SPR checks

Here `λ_j` means `a_j=lower_j+λ_j(upper_j−lower_j)` for `j=0,…,6`. The two interior members use, respectively,

* midpoint: `λ=(1/2,1/2,1/2,1/2,1/2,1/2,1/2)`;
* mixed: `λ=(1/4,3/4,1/3,2/3,1/5,4/5,2/5)`.

All fourteen listed interior inequalities are strict. For each of these two members **and** each of the four actual parity corners I independently obtained seven positive Hurwitz minors and constructed the pairing polynomial directly. On the common refinement of the four frozen partitions, each polynomial has strictly positive degree-seven Bernstein coefficients on all ten subintervals. The table's exact `m` is the smallest of those 80 coefficients for that member, so it certifies `P_a(t)/(1+t)^7≥m>0` for **all** `t≥0`, not just the additional displayed finite-frequency check. Consequently `Re(b_new/a)≥m/S²>0` at every real `w` for each listed member. The precise coefficient vectors and each actual ratio at `t=7/25` are in the receipt.

| Member | Exact all-frequency `m` | Exact `P_a(7/25)` |
|---|---:|---:|
| `E−,O−` | `390273469338209/28185722880000000` | `2908881655355019/39062500000000` |
| `E−,O+` | `1115489199327/36700160000000` | `123749585562361/7812500000000` |
| `E+,O−` | `191014987257/2867200000000` | `11578213125018807/195312500000000` |
| `E+,O+` | `1050465553521003/96207267430400000` | `127544487302737/195312500000000` |
| midpoint | `9021/50000` | `1833994095509729/48828125000000` |
| mixed | `1788949/10000000` | `197700742439131541/5859375000000000` |

### Old failure and exact endpoint neighborhood

At the actual base `(E+,O+)` corner and `t=7/25`, my direct pairing calculation gives `−553009337053/39062500000000`; the denominator squared modulus is `687499186865723227/390625000000000000 > 0`. Hence the exact real part is `−5530093370530000/687499186865723227 < 0`, at real frequencies `w=±√7/5` (C:74–79; F:595–607).

For every perturbed endpoint box, preserve each coefficient's interval-interpolation parameter to map any `a'` back to an `a` in the base box. Each of the seven nonleading coefficient differences is at most `rho`. For all real `w`, `|w|^j≤(1+w²)^(7/2)` for `j=0,…,7`; hence the normalized denominator perturbation is at most `7rho`. The independently recomputed values are `B_new=963073/100`, `B_old=585271/1000`, `S=178113/1600`, and minimum base width `29/1000`. Using the base pairing bound and Cauchy–Schwarz, every monic interpolation segment from `a` to `a'` has normalized modulus at least `d/B_new−7rho>0`. Thus no segment crosses the imaginary axis and every `a'` is Hurwitz. The exact inequalities and reduced values in C:83–104 are:

* width lower bound `29/1000−2rho = 1449999/50000000 > 0`;
* new normalized-pairing lower bound `d−7rho B_new = 3080022869858764583/300647710720000000000 > 0`;
* new **uniform ratio** lower bound `(d−7rho B_new)/(S+7rho)² = 48125357341543196609375/58214235678253038721514340352 > 0`;
* at the corresponding perturbed `(E+,O+)` corner, old pairing remains negative by absolute margin `1062500322801560113/76293945312500000000 > 0`, after the error bound `7rho B_old(32/25)^7`.

The argument covers arbitrary simultaneous endpoint perturbations, every member of every such box and every finite real frequency. It does not assume the perturbed box's vertices alone determine stability.

### Controls, prior box, and disclosed tooling issue

I independently exercised the two claimed base-certificate mutations and both radius controls, checking the **intended** rejection reason: modified leaf → `LEAF_MISMATCH`; reversed root bracket → `ROOT_BRACKET`; radius `1` → `WIDTH`; radius `1/1000` → `NEW_MARGIN`. These are my separate checks, not author replay execution. The named author result receipts report the same four outcomes; those receipt hashes and both author source hashes match the pins at C:111–112.

The separately named search receipt at C:113 has SHA-256 `af830d936a56ca8b446d09b4082ff2bcfa0b4c036e969c0cb98dfc5a9fa60d66`; its `base_lower`/`base_upper` metadata give the prior box. I checked all seven midpoints match the new box and the new widths are exactly `101/100` times the prior widths for `j=0,…,5`, and `1/2` for `j=6`. Independently applying adaptive exact Bernstein subdivision to the **old** numerator and the four prior-box parity corners gave leaf counts `7,8,9,7`, each with strictly positive coefficients; a positive reference Routh column plus the no-imaginary-zero argument then proves that numerator is common SPR on the box described by that metadata. This supports the mathematical comparison at C:38; it does not by itself independently establish the historical identity or chronology of a separately pinned earlier artifact.

C:115 discloses an Eval `os` shadowing incident. The hash-matched author's base-replay source actually has the top-level `for os in (0,1)` at its LF19–23, which can shadow a persistent-kernel `os` module binding. I did **not** reproduce the incident or independently inspect a live event log establishing the reported bridge failure, restoration, and retry; those details remain author-reported provenance, not an input to my proof. The fresh checker above neither imports the author's source nor relies on that kernel binding. The disclosure is not hidden or treated as a mathematical counterexample.

## Explicit unverified imports and limits

* S is a registered transcription of a canonical dossier. I did **not** verify its transcription against the book page images, read the underlying dossier README, or check the cited Wang–Yu papers/announcements; S:35–37 already discloses that limitation. My result is relative to S's stated definitions.
* The author's search history, claims about its floating-point/non-floating-point execution and the exact past replay/bridge chronology were not independently reconstructed. The hash-matched author result receipts and selected source excerpts were inspected; the full bodies of the optional replay scripts and the 3,924-LF search receipt were not reviewed as proof. My arithmetic does not depend on those algorithmic or historical claims, except that the prior box's coordinates are taken from the named search receipt and then directly checked.
* No external-model/paid API, literature or novelty screening, book-image comparison, human review, proof assistant, or external-family review was performed. This review does not establish the present literature status of the universal septic question. It certifies neither a universal synthesis result nor an unrestricted obstruction/counterexample.
