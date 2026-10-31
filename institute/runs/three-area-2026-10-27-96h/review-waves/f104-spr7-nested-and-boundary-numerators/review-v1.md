# Independent same-harness review — f104 SPR7 nested box, affine obstruction, and boundary numerator

Observed native clock immediately before this review was written: **2026-10-28T19:11:46-0700 PDT**.
Manifest: `manifest-v1.json`, SHA256 `b7d2fba8c9c51395148aef19b8d32268f8159eabf4dabb01ffd6906b07890349`. This is the only manifest in the wave directory. The six inputs were hash-checked **before** the complete, ordered raw-window read. All six full SHA256s, byte counts, and LF counts match the manifest; no process mismatch was found. The two named imports actually used below were also completely read and hash-checked.

Unless otherwise specified, the source filenames below are in `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/`; `Lx–Ly` refers to their original line numbers. The registered definitions are `written-releases/info-2-septic-box-definitions-v1.md` in the run root.

## Verdicts and precise scope

1. **Larger nested box / b_H** — **FATAL 0, MAJOR 0, MINOR 0** within the scoped mathematical claims. The base and stated `10^-8` endpoint neighborhood are supported, including strict stability, full-frequency SPR and failure of the two specified earlier numerators. Main claims: `frontier-20261028-larger-nested-box-new-numerator-v1.md:L7–33,L35–89`; frozen numerical proof: `frontier-20261028-harder-box-common-numerator-frozen-v1.json:L5–717`.
2. **Affine-line obstruction** — **FATAL 0, MAJOR 0, MINOR 0** within the scoped mathematical claims. The actual boundary box is Hurwitz and the two atoms exclude the **entire specified real affine line**, with positive rescalings, not all numerators. Main claims: `frontier-20261028-boundary-affine-line-obstruction-v1.md:L7–36,L38–76`; frozen import `frontier-20261028-boundary-affine-obstruction-frozen-v1.json`, SHA256 `bca55dad8e27f93371bc163093d5d49404eb2bdfd538827b11d7c4076cc131b0`.
3. **Boundary box / b_B** — **FATAL 0, MAJOR 0, MINOR 0** within the scoped mathematical claims. The base and stated `10^-9` endpoint neighborhood are supported, including strict stability, full-frequency SPR and failure of b_H. Main claims: `frontier-20261028-boundary-box-new-numerator-open-family-v1.md:L7–34,L36–88`; frozen proof: `frontier-20261028-boundary-common-numerator-frozen-v1.json:L6–707`.

The conclusion of item 2 at `L76` that constructing a numerator outside the line is the next open step is a **historical statement at the time of that earlier document**. The later pinned boundary result does construct one; it must not be repeated as the current frontier. This chronology is not a mathematical defect in the earlier line theorem.

## Independent exact reconstruction

`independent-spr-exact-check-v1.py`, SHA256 `c1d6fc35ec509242fa4447dac43c7ea4b53208bf405626439702a3a32ae26daf`, was written independently of the author's replay. Its exact bytes were compiled and executed in the Python Eval kernel before exclusive creation of the code and `independent-spr-exact-receipt-v1.json` (SHA256 `b75bfcc02cf4572925c53b1459e5f28eebc4acfceaf71c721004a0046a8081d3`). It uses standard-library `Fraction`/integers. No author replay or finite-grid optimizer was used as proof. The receipt includes all member labels, selected-frequency checks, leaf counts, exact minima, and perturbation margins.

For both boxes I independently formed the actual parity corners by alternating coefficient endpoints, expanded the pairing directly from monomials, and checked the given polynomials. I converted `Q(x)=(1-x)^7 P(x/(1-x))` into the power basis, substituted each leaf interval affinely, and used `u^j = sum_{i=j}^7 [C(i,j)/C(7,j)] B_i^7(u)` to obtain the degree-seven Bernstein coefficients. I checked exact contiguous coverage of `[0,1]` and every positive coefficient: **35 leaves / 280 coefficients for H**, and **35 leaves / 280 coefficients for B**, with claimed leaf counts `(6,11,11,7)` and `(8,9,11,7)`, respectively. Thus every corner has the asserted all-frequency normalized pairing bound, including x=0 and the compactified x=1 endpoint. For each fixed `t>=0`, the even and odd coefficient choices are independent, and the pairing is affine on their value rectangle; the four corner lower bounds therefore apply to **every** member, not merely the sampled ones.

For each box I reconstructed all four parity cubic extrema, checked all **12 exact strict root brackets**, their six disjoint interleaving bands and the reference positive Routh column. I additionally computed the **28 positive leading Hurwitz determinants** of the four corners. Three distinct sign-change roots exhaust each cubic; away from the merged E bands the E extrema have the same nonzero sign, and similarly for O. Because the E and O bands are disjoint, no member has an imaginary-axis root (also `a_0>0` at zero). The coefficient box is convex and monic, so homotopy from the checked Routh-stable reference proves **all-member** Hurwitz stability. The 28 corner determinants alone are not used as a stability theorem.

### Explicit corner and interior SPR checks

For each box, the checker evaluated four base corners, three genuinely interior coefficientwise choices, four corners and one interior point of each of the boxes formed by expanding and contracting **every** endpoint by the stated rho. Each of these 17 members was checked at the nine exact squared frequencies `0, 53/203, 1/4, 7/25, 1, 197/59, 10, 100, 1000000`, including exact positive denominator, positive pairing, literal ratio and the relevant uniform lower bound: **153 checks per box**. All 17 also have positive independently computed Routh columns. In addition to the full-frequency frozen certificates for the four base corners, the checker independently constructed full-frequency positive Bernstein proofs for all **three base interiors, eight perturbed corners and two perturbed interiors** per box. These are extra controls; the rectangle and perturbation arguments establish the universal claims.

Concrete independently evaluated ratios, where the interior is the coefficientwise midpoint:

| Box | Member | t | Exact `Re(b(i sqrt(t))/a(i sqrt(t)))` |
|---|---|---:|---:|
| H | `(E+,O+)` corner | `7/25` | `78330700917423760/27504218862682843` |
| H | midpoint interior | `7/25` | `1228012948148232180/1907703182412479` |
| B | `(E+,O+)` corner | `197/59` | `469217561706909825383319957888/2318541618647525338763642765` |
| B | midpoint interior | `197/59` | `5872604986870985773330539/166764662784678485214325` |

All four numbers are strictly positive. The check also independently reconstructed all 14 endpoint inclusions of the named earlier box in H, and all 14 of H in B. For indices `0..5`, the actual H/earlier width ratio is `105/101`, and B/earlier is `(679/640)/(101/100)`; the s^6 interval is identical. The earlier source actually read was `frontier-20261028-anisotropic-new-numerator-open-family-v1.md`, SHA256 `25db31d50117b74462a3fc25f22d46f48d2e44e79d28455c0b875eef93063d2f`.

### Perturbation and exact failure margins

The exact least recorded Bernstein coefficient is `d_H=1131593723113/6710886400000` for H and `d_B=19401458553061552497/153931627888640000000000` for B. The coefficient-sum upper bounds are `S_H=178293/1600` and `S_B=5706951/51200`. Direct rational arithmetic reproduces both stated base ratio bounds and, with `B_H=32124813/100`, `B_B=7595109/5000`, the positive endpoint gaps

- `d_H - 7(10^-8) B_H = 3064636073900093/20971520000000000`;
- `d_B - 7(10^-9) B_B = 2220585007969403446317/19241453486080000000000000`.

For any perturbed box and member, matching coefficient interpolation parameters gives a base member with each of seven nonleading coefficients within rho. On every connecting segment, `|delta a(iw)|/(1+w^2)^(7/2) <= 7 rho`; the positive gaps and `|b(iw)|/(1+w^2)^(7/2) <= B` rule out an imaginary-axis zero and keep the normalized pairing positive. Homotopy therefore preserves strict Hurwitz stability. The corresponding literal ratio lower bound is `(d-7 rho B)/(S+7 rho)^2`, exactly the claimed `47884938654688953125/4068914417784016897605632` for H and `6939328149904385769740625/747061339892751392238794027565056` for B. Both minimum widths remain strictly positive after the `2 rho` possible loss.

At H's `(E+,O+)` corner and `t=7/25`, direct expansion gives the claimed negative pairings `-19650719733069/195312500000000` and `-157843475513483/195312500000000` for the old and new previous numerators. The respective exact residual negative magnitudes after the uniform endpoint perturbation estimate are `7658466357099997613/76293945312500000000` and `12273612385949610863/15258789062500000000`, both positive. At B's `(E-,O+)` corner and `t=197/59`, the b_H pairing is `-3111053405919714332717419/318547390056832000000`; its positive residual negative magnitude after the B perturbation estimate is `9657226464955553493900607271/995460593927600000000000`. Hence the failure statements apply to the corresponding actual corner of **each** perturbed box, not just to the original box.

### Entire real affine line

For the two corners and frequencies in `frontier-20261028-boundary-affine-line-obstruction-v1.md:L56–74`, independently reconstructed pairings are affine in eta with slopes

- `D_1=3295819818853828922267/337444269128000000 > 0`;
- `D_2=-134089442642294550529/3499018444616450000 < 0`.

At `eta_0=7999/8000`, the respective pairings are exactly `-94201830162290955099253/159273695028416000000000` and `-81906391888185735590779/45459247632456918400000000`. For `eta<=eta_0` the first is no greater than its negative threshold value; for `eta>=eta_0` the second is no greater than its negative threshold value. Both corresponding denominators are actual Hurwitz corner members, so the negative pairing means a negative literal real part. Multiplying by a positive scalar cannot change the sign. This exhausts all real eta.

Independently, b_B is not on that line: equality of constant coefficients would force `eta=9999/10000`, but at that eta the b_B coefficient of s minus the corresponding line coefficient is exactly `106270839/1000000 != 0`. The successful b_B does not contradict the restricted line obstruction.

## Unverified named imports and non-claims

- The source-bound definitions transcript was read in full, but its named canonical dossier `information-science/robust-spr-interval-synthesis/README.md` (SHA256 `b9afd01e3f30274c95fa8a0a7369cc2348ab20ec60c9cdc344224f633d0f28fc`), book page images, and equivalence to those images were not independently checked. The registration explicitly disclaims book-image and current-openness certification.
- The earlier source's transitive `frontier-20261028-anisotropic-common-numerator-frozen-v1.json` (SHA256 `41411d5d0f25108a14e1dad8f8ac770ee580867d573206ce4ea22b6cf71005a4`), its earlier full positivity proof and the still-earlier unhalved-box provenance were not reviewed. This review uses the earlier source's displayed endpoint and numerator bytes only, and independently checks the actual containments and failures.
- The following author artifacts were **not** read or used as premises: `frontier-20261028-harder-box-independent-replay-kernel-v1.py` and `frontier-20261028-harder-box-independent-replay-result-v1.json`; `frontier-20261028-harder-open-family-replay-kernel-v1.py` and `frontier-20261028-harder-open-family-replay-result-v1.json`; `frontier-20261028-harder-box-exchange-result-v1.json`; `frontier-20261028-boundary-affine-independent-kernel-v1.py` and `frontier-20261028-boundary-affine-independent-result-v1.json`; `frontier-20261028-boundary-common-independent-replay-kernel-v1.py` and `frontier-20261028-boundary-common-independent-replay-result-v1.json`; `frontier-20261028-boundary-open-family-replay-kernel-v1.py` and `frontier-20261028-boundary-open-family-replay-result-v1.json`. Thus the author's historical replay, mutation-control, optimizer and resource-use reports are not independently certified here.
- This is a same-harness scientific review, **not** an external-family, human or formal/kernel proof, novelty/SOTA audit, proof that the universal degree-seven problem is currently open, a counterexample to unrestricted synthesis, or a theorem for every stable septic box. No claim of maximality of either box or of the endpoint radii is made. The source documents' general literature-status assertions at their respective `L100` were not independently checked and are not part of these verdicts.
