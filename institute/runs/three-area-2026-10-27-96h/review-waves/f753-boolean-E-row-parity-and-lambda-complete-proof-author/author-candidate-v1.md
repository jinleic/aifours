# F753 — E-row parity and the missing singleton-lambda branches

**Disposition of this author's written work, not a parent disposition:** the even-`d_E` conclusion is reconstructed below. The stated inference in f748 §3 that graph-lambda zero forces a four-entry E-side lambda plane is **false as a U0-profile implication**. An E-side singleton ±2 is also allowed. I give six explicit same-X arrays with the actual spatial D0/E/F/Z census, the specified-frequency zero and **all seven simultaneous U0 profiles**, not merely an arbitrary lambda fixture. They realize the omitted branch for `d_E=0` with graph occupancies `4` and `2+2`, `d_E=2` with graph occupancy `2` and either E occupancy, and `d_E=4` with either E occupancy. These are X-side countermodels, not completed common physical u/y/U3 witnesses: they do **not** refute the full theorem under its additional physical inverse, J=1 and all-U3-caps hypotheses. Whether those extra hypotheses exclude the singleton branch remains an open obligation. In particular, f748 §4's claimed unconditional `d_E=4` starting configuration cannot be imported until its singleton case is independently excluded or separately handled; I do not assess its further identities here.

## 1. Precise object, quantifiers, and local equations

Work at the actual normalized rank-two imports of packet S6–S8 and the complete f748 statement S2. One fixed physical object supplies f, R, a, g, u, x=U0 and y=U3; its original balance transports to one **specified** character t. Put `X(c)=(-1)^t(c) x(c)` only for analysis. Never replace the specified t by a convenient zero, and do not separately modulate a, g, u or invent an independent y. The two full sites are `(ell,i,b)=(0,00,00)`, one at each h, and have x=0. The six E sites are `(ell,i,b)=(0,i,00)`, i nonzero, both h. The 24 Z sites have ell=0 and b nonzero. Each D0 or Z2 site has |X|=2; the remaining E/graph-mate D3 sites and Z0/Z4 sites have X=0. At the named H_loc=0/count imports there are four D0 in the 16 physical graph mates plus those six E sites, six Z2, one Z4, seventeen Z0 and eighteen D3; graph X is ±1. These statements use the imported local types, not an asserted construction of the original caller.

Rows are `(ell,i)` with i,b in F2², h in F2. The graph is ell=1, h=F_i and `sum_i F_i=1`. Set `m_i` to the number of graph-mate D0 in row i and d to the E D0 count. Thus `sum_i m_i=4-d`, each `m_i` is 0,...,4, d is 0,...,4, and each of the three E rows has capacity two. Define

`Z_(ell,i)(s,alpha) = 1/4 sum_(h,b) X(ell,h,i,b)(-1)^(s h+alpha(b))`, and `lambda_(ell,i)=Z_(ell,i)(1,0)`.

The carried zero-flat import is `Z_(ell,i)(0,0)=0` for all eight rows. Simultaneously, for each of the seven nonzero `(s,alpha)`, S8's actual-U0 profile is **either** one ±2 entry **or** four ±1 entries on an affine two-flat of the quotient `(ell,i)` with sign product −1. Each such column is formed from this same X. A singleton may lie on either ell side. The independent graph/phase/physical imports, all U0 divisibilities and caps, and the all-U3/J1 conditions are retained where the original conditional theorem requires them; none is synthesized from the occupancy count alone.

Let p_i be the number of negative values among the four weighted graph signs in row i and let `epsilon_(i,b)=X/2` at its D0 mates. The row sum and its lambda entry are

`0=4−2p_i+2 sum epsilon`,  `lambda_(1,i)=(-1)^F_i (4−2p_i)/2 = −(-1)^F_i sum epsilon`.  (1)

Consequently, m=0 has lambda 0 and balanced graph; m=1 or 3 has lambda ±1; m=2 or 4 has lambda 0 or ±2. In particular, for m=2 the zero case has opposite mate signs and balanced graph, while the ±2 case has equal mate signs and constant graph. For m=4, lambda zero has a 2:2 mate split and balanced graph, while ±2 has a 3:1 mate split and constant graph. For m=3 the mates split 2:1 and the graph splits 3:1. These follow from (1), the four graph units and the whole-column energy 4; no arbitrary row phase is introduced.

For an E-side cell `(h,i)` write n_hi for the count of nonzero X there and let S_hi be the sum of their signs X/2. The same zero-eta equation gives `S_0i+S_1i=0` and `lambda_(0,i)=S_0i`. Thus lambda zero means **each** h-cell has even occupancy and zero signed sum; lambda ±1 means each h-cell has odd occupancy and respective sums ±1,∓1; lambda ±2 requires each h-cell to have even occupancy at least two and respective sums ±2,∓2. Each physical cell has at most four sites; a four-site cell necessarily uses its b=00 E site and i≠00. An i=00 full-site cell has at most three candidate Z sites and cannot have four supports. Since zero eta fixes even X/2 parity in each whole ell0 row, all its other partial transforms are integral. On a graph row the difference between a nonzero-eta signed sum and its zero-eta sum is divisible by four: a nontrivial b-character flips two of the four graph units, and every mate contribution changes by a multiple of four. Hence the local integrality needed in the discussion follows from the same rows, rather than from choosing each column independently; global profile/cap constraints still couple the rows.

## 2. Even E-row parity and all occupancy shapes

There are exactly `6+d` nonzero ell0 X sites, all ±2. Summing zero-eta over its four rows makes their signed X/2 sum zero, so this number is even. Thus **d is even**. This direct proof uses the given modulation only through its signs, works with the two full sites present and needs neither U3 caps nor a location theorem. Independently, (1) gives `p_i=m_i mod 2`. The XOR of all sixteen graph points is zero (each b and i occurs four times, ell occurs sixteen times, and every F_i occurs four times); therefore any fixed character t changes an even number of graph signs. The imported even original graph-negative parity implies `sum_i p_i` even, hence `sum_i m_i` even and the same conclusion d even. Neither argument sets t=0.

This is the **entire** unordered shape list before the parity exclusion; E labels are actual non-full rows and have capacity two:

| d | graph-mate multiplicities, with zero rows omitted | E-site multiplicities |
|---|---|---|
| 0 | 4; 3+1; 2+2; 2+1+1; 1+1+1+1 | none |
| 1 | 3; 2+1; 1+1+1 | 1 |
| 2 | 2; 1+1 | 2 or 1+1 |
| 3 | 1 | 2+1 or 1+1+1 |
| 4 | none | 2+2 or 2+1+1 |

The d=1 and d=3 rows are impossible by parity. The `d=0, 1+1+1+1` case is excluded only under the additional named actual physical/common-y/J1/all-U3-caps scope of S6, not by occupancy or by a lambda-only calculation. The remaining entries below are necessary profile alternatives, not asserted physical common-u/y witnesses.

## 3. Complete lambda alternatives and cell constraints

The table explicitly includes **both** singleton locations. The single graph entry, if present, is in an occupied graph row. `E plane` means four E-side ±1 entries with sign product −1. When a mixed plane has two graph and two E entries, both pairs have the same nonzero i-difference and all four signs have product −1, since they are one affine two-flat, not two independently picked pairs.

| d; graph occupancy | all lambda alternatives under the U0 profile | further necessary consequences |
|---|---|---|
| 0; 4 | graph singleton ±2 **or E singleton ±2** | the E plane is impossible: it needs ≥8 supports, but only six exist |
| 0; 2+2 | graph singleton ±2 **or E singleton ±2** | in the graph-singleton case exactly one m=2 row has equal mate signs; in the E-singleton case both have opposite signs |
| 0; 3+1 | mixed 2-graph/2-E plane | odd rows each contribute ±1 |
| 0; 2+1+1 | mixed 2-graph/2-E plane | the m=2 row has lambda zero and opposite mate signs |
| 0; 1+1+1+1 | plane on all four graph rows | E lambda zero; S6 additionally excludes this whole subfamily only at its full J1/U3/physical imports |
| 2; 2 | graph singleton ±2, **E singleton ±2**, or E plane | in the two E-supported alternatives the two graph-mate signs are opposite; graph singleton has equal signs |
| 2; 1+1 | mixed 2-graph/2-E plane | pair-difference and sign-product constraint as above |
| 4; none | **E singleton ±2 or E plane** | graph lambda identically zero; neither form follows from that fact alone |

Proof of exhaustiveness: use the row values from (1). For an even-occupancy graph configuration lambda is all zero or has a single ±2 on a graph row; two such entries exceed total energy 4. If graph lambda is all zero the common profile can be either a singleton on E or an E plane. For d=0 the E plane needs one nonzero site in each h-cell of all four E rows, i.e. at least eight, and is impossible; this counting does **not** rule out the E singleton. For 3+1, 2+1+1 and 1+1, the two odd graph rows have entries ±1, so a singleton is impossible and the plane has precisely two additional E entries. For 1+1+1+1 the plane's four entries are on the graph. This covers every shape without using a local example as a global proof.

The physical cell counts refine the alternatives as follows. They are **necessary** consequences of the actual support and lambda, not an assertion that every such pattern extends to the other six profiles, y or u.

* For d=0, a graph singleton (and likewise the 1+1+1+1 graph plane) has E lambda zero. There are exactly three occupied `(h,i)` cells, two Z2 sites per cell with opposite weighted signs. For an **E singleton**, there are also exactly three cells because no E site is nonzero and a cell has only three b≠0 sites: its two cells in the singleton row each have two equal signs, opposite between h=0 and h=1, and the third cell has two opposite signs. This is the missing sign alternative to f748's three-cell statement.
* For d=0 and a mixed plane, the two E lambda rows each occupy both h-cells with an odd number of sites. The six Z2 sites occupy either four cells (one active row has a 1:3 split) or five cells (the extra opposite-sign pair is in one zero-lambda cell). The specified graph/E pair difference and product −1 still apply.
* For d=2, graph singleton implies E lambda zero and eight E-side supports. If q of its occupied cells have four sites, then there are `4−q` occupied cells, q=0,1,2; every four-site cell contains an actual E D0 at b=00 and three Z2, never an i=00 full site. An E singleton likewise gives even cell occupancies, but two occupied four-site cells are impossible under **all seven** profiles: each would be a 3:1 sign pattern in the singleton row, so for every nonzero b-character one s-column has an E entry ±2, while any of the three m=0 graph rows has a nonzero ±1 on both s-columns for its own nonzero character. Thus its number of occupied cells is necessarily three or four; existence at either count is not inferred from this bound. The four-cell alternative is explicitly realized at the full X-profile level below.
* For d=2, graph occupancy 2 and the E plane has exactly two sites in each E-side row, one in each h-cell, with opposite weighted signs. Either E occupancy `2` or `1+1` can be placed physically at this **lambda-only** level: start with those E sites, fill every other h-cell with one Z2 and choose four row signs with product −1. This does not prove the other profiles or caps.
* For d=2 and graph occupancy 1+1, the two active E rows give four occupied cells before placing the four remaining supports. The total is four, five or six occupied cells. Four means two active cells have three sites; five means one such cell plus one opposite-sign pair in a zero-lambda cell, or one four-site zero-lambda cell; six means two extra two-site zero-lambda cells. A four-site cell uses an E D0, so the i=00 full site is never used. Pair geometry and sign product are mandatory in every alternative.
* For d=4 and the E plane, all eight E-side h-cells are occupied. Ten supports force exactly one three-site cell and seven one-site cells: one row has a 1:3 split and the other three have 1:1. Both `2+2` and `2+1+1` E patterns can be placed at lambda-only level: place the four E sites, put one Z2 into each still-empty h-cell, and put the remaining two Z2 into one occupied cell, respecting its b≠0 sites; choose the three signs there to sum to the required ±1 and choose the four lambda signs with product −1. This does not claim a simultaneous seven-profile/U3 completion.
* For d=4 and an **E singleton**, all cells have even occupancy. A four-site cell consumes one E D0 and three Z2. Two such cells would consume all six Z2 and only two of the four E D0; the other two E sites would lie in different cells and could not be paired, contradicting even occupancy. Hence there are either five two-site cells, or one four-site cell and three two-site cells. The singleton row has signed sums ±2 and ∓2; every other cell has signed sum zero. Both physical E patterns are realized with five cells by the explicit same-X examples below.

## 4. Explicit all-seven-profile X-side countermodels to the omitted-branch inference

These constructions are exact written arrays; **they were not executed**. They do not supply y, u, J, all U3 caps or an original caller. They do establish much more than a lambda-only fake: one common X in each row table has the stated actual E/F/Z/graph-mate site census, zero eta and every one of its seven simultaneously transformed U0 profile columns. Thus merely appealing to all the remaining U0 columns cannot repair the omitted implication.

For all six examples write row labels `A=00,B=01,C=10,D=11`, set `F=(0,0,0,1)`, let `u(b)=b0`, `v(b)=b1`, `w=u+v`, and put `chi_a(b)=(-1)^a(b)`. In a graph row the graph values at h=F_i are the listed character, and the only nonzero mates at h=1+F_i are those stated. On ell0 use `i:h b±` for `X=±2`; unlisted points are zero. The signs listed for a graph mate also mean ±2. All b are written as two bits. Choose one of the eighteen unused b≠00 Z sites as Z4; the other seventeen are Z0. The two `i=A,b=00` full sites are always zero.

| example | `(d; graph m; E occupancy)` | graph X in rows A,B,C,D | nonzero graph mates | ell0 nonzero X |
|---|---|---|---|---|
| I | `(0;4;none)` | `chi_u, chi_u, chi_w, chi_w` | A: `2 chi_v` at all b | C:`0 10+,0 11+,1 01−,1 10−`; D:`0 01+,0 11−` |
| II | `(0;2+2;none)` | `chi_u, chi_u, chi_v, −chi_v` | A:`00+,10−`; B:`00−,10+` | C:`0 01+,0 10+,1 01−,1 11−`; D:`0 10+,0 11−` |
| III | `(2;2;2)` | `chi_u, −chi_u, −chi_w, chi_v` | A:`00+,01−` | C:`0 00+,0 01+,1 00−,1 11−`; D:`0 01+,0 10−`; A:`0 10+,0 11−` |
| III′ | `(2;2;1+1)` | `chi_u, chi_u, −chi_w, −chi_v` | A:`00+,01−` | C:`0 10+,0 11+,1 00−,1 11−`; D:`0 00+,0 11−`; A:`0 10+,0 11−` |
| IV | `(4;none;2+2)` | `chi_u, −chi_u, chi_v, chi_v` | none | B:`0 00+,0 11+,1 00−,1 11−`; C:`0 00+,0 10−,1 00+,1 01−`; D:`0 01+,0 10−` |
| IV′ | `(4;none;2+1+1)` | `chi_u, −chi_u, chi_v, chi_v` | none | B:`0 01+,0 10+,1 00−,1 11−`; C:`0 00+,0 10−,1 00−,1 01+`; D:`0 00+,0 11−` |

Every listed ell0 row has zero total signed sum. Each example has four D0 among graph mates plus non-full b=00 E sites and exactly six b≠00 Z2 sites; its other 18 E/graph-mate D sites have X=0. All X graph values are ±1 and the full sites have X=0. Since no |x|=4 occurs anywhere, any physical inverse that realizes one of these x arrays would have H_loc=0; this observation is not itself an inverse construction. Energies and site counts are the U0-side ones of the imported local types.

For exact checking of the simultaneous transforms, `G_i` below denotes an entry at `(ell,i)=(1,i)` and `E_i` one at `(0,i)`; a coefficient in front is its signed Z value. Set `r=(-1)^s`. These are the *only* nonzero entries in each listed nonzero-eta column:

| example | lambda `(1,0)` | `(s,u)` | `(s,v)` | `(s,w)` |
|---|---|---|---|---|
| I | `2 E_C` | `G_A+G_B−E_C+E_D` | `2r G_A` | `G_C+rG_D+rE_C−E_D` |
| II | `2 E_C` | `2G_A` if s=0, `2G_B` if s=1 | `G_C−rG_D+rE_C+E_D` | `rG_A−rG_B−E_C−E_D` |
| III | `2 E_C` | `G_A−G_B+E_C+E_D` | `rG_A+rG_D+E_A−E_D` | `rG_A−G_C−rE_C−E_A` |
| III′ | `2 E_C` | `G_A+G_B−E_C+E_D` | `rG_A−rG_D+E_A+E_D` | `rG_A−G_C−rE_C−E_A` |
| IV | `2 E_B` | `G_A−G_B+E_C+E_D` | `G_C+rG_D+rE_C−E_D` | `2E_C` if s=0, `2E_B` if s=1 |
| IV′ | `2 E_B` | `G_A−G_B+E_C+E_D` | `G_C+rG_D−rE_C+E_D` | `−2E_B` if s=0, `2E_C` if s=1 |

Every four-entry support in the table has graph and E pairs with equal nonzero difference; every product is −1. Every other entry is a singleton ±2, so this is the exact allowed seven-profile list, including the omitted E lambda singleton. At eta=0 all eight entries are zero. Quotient Fourier transformation sends every four-entry odd-sign plane to four values ±2 and every singleton ±2 to eight values ±2; multiplying by the defining factor 4 gives **all 64 U0 coefficients 0 or ±8**. Thus the entire X spectrum satisfies both divisibility and the U0 cap, and its zero-eta frequencies include zero.

This construction does not assume the actual transport t is zero. For any specified linear character t in these coordinates, define `x=(-1)^t X`. Then x's spectrum is the translated spectrum of the **same** displayed X, and `xhat(t)=Xhat(0)=0`; the cap and divisibility are unchanged. This is an X-array demonstration at an arbitrary given t, not a claim that every displayed x extends to the same original caller. The profile-derived divisibility is stronger than merely checking the parity part of `(C)`; any additional physical inverse/phase/y restrictions remain separate.

## 5. Comparison with f749 and remaining frontier

The f749 narrative S4 and its additive S3 correction concern a necessary **local plus one-lambda** enumeration, not all seven simultaneous global columns and not a proof of a common capped caller. S3 correctly narrows the `0000` graph-lambda energy to exactly zero; it does not eliminate the E singleton. The parent receipt S5 records one later parent run at its stated local-and-lambda scope. In particular it reports nonzero graph-energy-zero populations for both d=0/graph-4 and d=0/graph-2+2; with six E supports those necessarily require an E singleton, not an E plane. That receipt's representative fixtures explicitly fail U0 and/or U3 caps, and no f749 checker code was read or used here. The six displayed X constructions above are independent written derivations of the stronger all-U0-profile countermodels, not claims that the receipt checked them or that a physical U3 witness exists.

**Unresolved:** impose the actual common inverse/ternarity, phase/bent conditions and `(C)` at their stated scope, the same y and J=1, all 64 U3 caps/residue, all eight occupied/zero physical site restrictions, and the specified t **on each retained branch including every E singleton**. Either a uniform contradiction or one complete common u/x/y is needed; no such U3 result is furnished here. The separately adopted S6 exclusion is not generalized to other allocations. There is no V complement, all-odd caps, full original selected-T/rank/eight-zero caller, global rank-two/five-span/six-span or NL242 conclusion. F748 §4 and its U3 partial-Parseval table are outside this assignment's proved scope, and the former's use in all d=4 cases first requires a genuine singleton treatment.

## 6. Coverage, process, pins and assurance

Fresh nonblind same-harness GENERAL AUTHOR reconstruction, not an independent-family/human/kernel review. Before any packet body I read the actual dispatch, complete manifest, freeze receipt, final binding, prepared metadata, all 22 manifest controls and the multipart policy through their endings, and directly sent PREBODY ACK to Main naming the exact 1 part / 761 LF. Thereafter I read the sole part serially as raw windows of at most 20 LF through LF 761 and its ending before mathematical comparison or research. S1–S8 were complete source bodies in that part. All genuinely held episodes and all their proof/method/selection/planning/verification/reporting/confidence/downstream consumers remained NONINPUT. No external link, held history, old code or unspecified sibling proof was followed. A separate early direct decision notice to Main identified the missing E-singleton implication with the explicit U3/non-witness qualification.

Administrative SHA-256 metadata observed: manifest `bbab9b53337af1049d8dc34ef1832644664ac89ec3453779604cc70e6d357f21`; freeze receipt `f1589cbdeff5ebc85b368bda9b48749237e2960977d4ffb8945844e41d96c82a`; final binding `d83fe8f53a882168c1a0e45d2fde6f3d77f14db339a883aa232c23016472c9eb`; prepared metadata `23b49a430e14ba741d0f9465841377797fbbd33bcc265af7ade102dbde5c7533`; actual dispatch `fcb290222c7f1fdaa13c2bbb6abbc9012f7e5999a0b44cfdc59e2d87dcce7cac`; sole packet `b20d2dcb228e52740495f5353adaf911155363b940e861bd86c3c055e2dbda64`. These hashes are administrative, not scientific checks.

The parent-supplied complete-source pins, relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`, are:

* S1 `parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json`, LF 1–11, `8a98f416ed19f9d838eb286d1de32cd9508e33324fe44b2593dd3663c9b2c70c`.
* S2 `review-waves/f748-boolean-remaining-d0-same-object-u3-frontier-author/author-candidate-v1.md`, LF 1–139, `09b37a6329453627d4d6c633c7363d8e54b7c84bb13f43fe54372b745036be55`.
* S3 `review-waves/f749-boolean-d0-occupancy-local-profile-exact-finite-author/author-lambda-energy-erratum-v1.md`, LF 1–5, `4e02d9a0a277fb830db497552d2e52e61f02e6c2a029e7b6fb71d47dc06cd17a`.
* S4 `review-waves/f749-boolean-d0-occupancy-local-profile-exact-finite-author/author-candidate-v1.md`, LF 1–35, `3a1899e8000395700de08015f06ae397288164c3c092fc2e799751594ed7bcb5`.
* S5 `review-waves/f749-boolean-d0-occupancy-local-profile-exact-finite-author/parent-d0-occupancy-local-profile-v2-run-v1-receipt.json`, LF 1–456, `44fc6d7c1f177a22eba29d295889220761f540a427bb84a7b7f9d9912cc52bf9`.
* S6 `dispositions/info-6-entire-four-distinct-d0-rank2-same-object-obstruction-parent-v1.md`, LF 1–31, `ae6fccd2b7206a1813ac3d3762774b3296fc70df6a83e24c6026391bac68c928`.
* S7 `parent-recovered-local-H-definition-and-general-g-foundation-v1.md`, LF 1–13, `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef`.
* S8 `dispositions/info-6-actual-rank2-seven-profile-and-four-distinct-d0-cross-fibre-parent-v1.md`, LF 1–37, `44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a`.

Native clock observed before writing: `2026-10-30T17:46:41-0700 PDT`; it is not represented as the creation time. This candidate is intended as one complete exclusive final-bytes write; no source program is supplied. **NOTTESTED:** no child scientific program, numerical enumeration, solver, CAS, compile, test, build, lint, formatter or external model CLI was run. All tables and deductions are written claims requiring the parent's complete independent read, scrutiny and separate disposition. No automatic parent adoption, full actual physical witness, source-identity, global-family, independent-model-family, human, kernel or novelty assurance is claimed.
