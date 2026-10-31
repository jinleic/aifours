# f105 review — level-six strip, obstructions, and partial determinant

Native `/bin/date` observation immediately before exclusive creation: **2026-10-28T19:12:30-0700 PDT**. This is a same-harness scientific review, not an external-family, human, formal/kernel, novelty, priority, or parent-acceptance verdict. I read the manifest first, verified the hash, byte count, and LF count of each input, then read all eight completely in manifest order in raw windows. No input mismatch was observed.

## Per-candidate disposition

| Item | Verdict at the reconstructed scope | Exact limit |
|---|---|---|
| (2,2,6) gap-41 strip, S2:7–44 | **0 FATAL / 0 MAJOR / 0 MINOR**, conditional on the named presentation, PBW, ideal-descent and realization imports | The computational/free-Levi statement and the conditional argument were reconstructed. An unconditional original `G_C/J` theorem is **INCONCLUSIVE** here because those upstream imports were not independently proved/authenticated. |
| Root-bracket addendum, S4:5–21 | **0 / 0 / 0** | Two real zeros of this selected polynomial, not a full-map kernel or integer witness. |
| Wide-gap addendum, S5:7–23 | **0 / 0 / 0** | Every real `g >= 42` has a real zero of this one selected minor; no other minor or full-map conclusion. |
| Euclidean accretivity obstruction, S6:7–34 | **0 / 0 / 0** for the reconstructed full tensor-word pencil, conditional on its identification with the original map | Only the two stated unweighted slope forms are indefinite in the stated coordinates; not an obstruction to other metrics or injectivity. |
| (4,4,6) partial replay, S7:1–7,42–67 and S8 | **0 / 0 / 0** for the **listed 162×162 determinant only** | Source dimension, source/kernel basis, correctness of the listed entries as an actual map, ideal descent and cone theorem are **NOT RECONSTRUCTED**. This verdict must not be expanded into a cone or map verdict. |

These are scoped review findings, not adoption of the imported results. S1:9–11 already records the inherited PBW **transcription MINOR**: the named statement is normalized/paraphrased, not a verbatim quotation or a newly verified primary proof. I preserve that existing qualification rather than count it as a new defect in these candidates. No held/withdrawn/quarantined body was used as a premise; earlier stated methodological exposure and holds are not erased by this review.

## Frozen input audit

`S1`–`S8` follow `manifest-v1.json` exactly. The full hashes below were recomputed, not merely copied as attestations; all byte and LF counts also match the manifest. `S1` is the PBW qualification, S2 the strip, S3 its replay receipt, S4–S5 its two addenda, S6 the slope obstruction, S7 the partial modular replay, and S8 its receipt.

| Input | SHA-256 observed | Bytes / LF |
|---|---|---:|
| S1 | `21b5b074fdf6b20784ec640037aaffa8d0964f6c2aa3d7855ff955bf2873f247` | 1404 / 12 |
| S2 | `a9d70a2b7da3b93056999cff6771997593e78d2d4cc12a3ac46a33d094f75f40` | 7786 / 74 |
| S3 | `ca69a9d938e1353287e72c89c1fce31601a171ea67f404d928d352605a02e48f` | 544 / 18 |
| S4 | `4dbabe1136235d403d21ec1d7ce613e6beba31f37fcdb9607c5f91b774ee970e` | 2700 / 23 |
| S5 | `2d37aa59690db768c6f79acea21e4b18c151eacb5bd1fc5d9bbf1220cce8c32d` | 3147 / 31 |
| S6 | `27376ed275b3814b62b8963831270499388940dae63e3d424aefa96f05da79af` | 3998 / 42 |
| S7 | `6d8396d936929992f9ec35341133e50c6db461e82b3abca9413995c1e980747e` | 3518 / 73 |
| S8 | `a47159906c4b624e2ce39a29fec41159b97c11024240a9e38df758d11f68d8af` | 4206 / 271 |

## Own reconstruction of the strip (S2:20–44)

1. **Source and local action.** In an independently written standard-library rational calculation, I used the eight explicitly named adjoint `sl_3` matrix-unit basis elements and computed their `e_1,e_2,e_{12},f_1,f_2` actions directly by 3×3 matrix commutators. Among the 456 length-six associative words of horizontal degree `(2,2)`, the 74 stated Lyndon-bracket words have distinct leading terms. Separately, all 456 right-normed brackets span rank **74** (336 are nonzero); Jacobi reduces arbitrary bracket trees to these brackets. Thus the 74 span the whole corresponding free-Lie component, rather than merely a selected subspace. The full joint horizontal action has rank **40**; the 34 recorded independent vectors all lie in its kernel, hence form the whole kernel.
2. **Full target and pencil.** There are **235** length-five target tensor words of degree `(2,2)`. I derived `f_3` by commuting the local `[f_3,m_i]` terms rightward through every associative tensor word, applying each resulting Levi/Cartan derivation to the suffix and checking that all rightmost degree-zero terms cancel. The resulting full 235-row pencil reproduces all **34×34×3 = 3,468** entries of the selected affine pencil `A+xB+yC`. This calculation is independent of the author's Jacobi replay and imports no author code. Affinity follows from the local table, so checking `(r,s)=(6,6),(7,6),(6,7)` determines all its entries.
3. **Whole determinant identity.** I cleared rational denominators once per row, and independently computed fraction-free integer Bareiss determinants at **all 630** points `(x,y)` with nonnegative integers `x+y<=34`. All equal the scaled asserted polynomial. A 34×34 affine determinant and the listed polynomial have total degree at most 34. This triangular grid is unisolvent: on `y=0`, 35 roots force the restriction to vanish; divide by `y` and repeat inductively on the shifted triangular grid. Thus the equality is a polynomial identity, not a sample-based inference. I independently counted its **592** nonzero coefficients: **133 positive, 459 negative**.
4. **All 620 signs.** Expanding `x=v`, `y=v+g` gives 35 polynomials `f_j(g)`. For each `m_j=deg(f_j)` I independently computed every coefficient of `Q_j(z)=(1+z)^{m_j}f_j(41z/(1+z))`, using exact binomial sums. They equal the pinned certificate entry by entry and **all 620/620 are strictly negative**. The degrees are `30` for `j=0,...,4` and `34-j` for `j=5,...,34`, giving `5·31 + 30·31/2 = 620` coefficients. For `0<=g<41`, put `z=g/(41-g)`; at `g=41` the leading `z` coefficient equals `f_j(41)`. Hence every `f_j(g)<0` throughout the closed interval, and `f_0(g)<0` makes `P(v,v+g)<0` even at `v=0`.
5. **Boundary and exchange.** In the named free-source/ideal model the repeated-node-3 seeds have level `r+1` and `s+1`, at least seven, so their positive descendants do not meet the degree-six source or degree-five target; using this in the actual quotient requires the imported full ideal splitting/transport. Swapping nodes 1 and 2, their parameters and the corresponding full realization data sends the `(2,2,6)` source and `(2,2,5)` target to the swapped problem. It is an isomorphism of the actual maps under those imports; no symmetry of this *particular* selected `P` is used. The indicated original-map strip therefore follows **conditionally** on those imports, including at `|r-s|=41`.

The constant and axis-leading terms in S2:48–54 were also recovered exactly:
`P(0,0)=-603138104964912067285615430860800000000000000`,
`[x^27]P(x,0)=4217288785920000000`, and
`[y^30]P(0,y)=2071650631680000`.

## Root and wide-gap addenda (S4:5–17; S5:9–23)

The independently evaluated rational endpoint values are:

| Evaluation | Exact value |
|---|---|
| `P(11,0)` | `-6305348604835147737157900288648995932209152000000000` |
| `P(23/2,0)` | `105031806970458227918252885972054501252791681096171875` |
| `P(0,41)` | `-89543794320180311867803237695910955547865881540644811099340800000` |
| `P(0,83/2)` | `212768324811743927958694871520235309378530289337570948038908526875/8` |

Continuity therefore gives at least one selected-minor root in each **open** interval `(11,23/2)` and `(41,83/2)`; neither interval contains an integer. In particular the first root makes the node-exchange distinction essential. These statements do not prove uniqueness or constrain other roots/minors.

For the second addendum I separately expanded `P(0,42+h)` and checked all **31** coefficients strictly positive, matching the pinned list. I also obtained the constant-in-`g` leading coefficient `[v^34]P(v,v+g)=-1454389021504438272000`. Consequently each fixed real `g>=42` starts positive at `v=0` and tends to `-infinity` as `v→infinity`, so IVT gives a positive real `v` at which **this minor** is zero. This does not show `v` is an integer, that a full map has a kernel, or that the open interval `(41,42)` is uniformly resolved.

## Accretivity (S6:13–30)

Using my reconstructed **235-row** `A,B,C`, for each symmetric form `H_x=A^TB+B^TA` and `H_y=A^TC+C^TA`, the first source-coordinate direction has value `+32578`. Direct exact dot products with the two separately pinned 34-coordinate witness vectors give, respectively,

- `v_x^T H_x v_x = -348002061658205738495568873096495816418227091760133404797613539714182002831/7422757863554950116395051224950968117487269402309263239264604492618999`;
- `v_y^T H_y v_y = -331785005763535449582655134433463570674669615511783796409643421384022467860/29330795633882012696693297881048881657822942097901423365777768331436799`.

Each form has both signs, hence is indefinite. Since the selected baseline minor has nonzero constant term, `A` has full column rank; if both slope forms had been PSD, `Re((Av)^*Dv)` would indeed be positive for nonzero complex `v` and `x,y>=0`. Their indefiniteness refutes that *sufficient route*, not the conclusion of injectivity by another route. The 235-coordinate inner product is the stated auxiliary unweighted tensor-word inner product, not a claim about a physical norm.

## (4,4,6) partial listed determinant (S7:42–67; S8)

I hash-verified the named leading-data JSON as `606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed`, extracted only the first entry of each listed triple as the 162×162 matrix `L`, cleared denominators row by row, and performed my **own pure-integer fraction-free Bareiss elimination**, asserting exact divisibility at every step. The calculation required 111 row swaps and gave

`det(L) = 527253154492450281362499347901675627491900331462363707491032596767530614784 × 10^54`,

which is nonzero and exactly equals the stated rational determinant. The row-scaled integer determinant also equals S8's integer. Separately checking the CRT arithmetic, all **256** listed moduli are distinct primes, their product has **3825 bits**, twice the product of row-L1 norms has **3814 bits**, and the product is strictly larger. Equality of my direct integer determinant to S8's integer implies equality modulo all those primes. I did not execute the author's program and do not infer historical execution beyond its receipt. **This is strictly a check of the listed determinant and receipt; I did not validate the (4,4,6) source, kernel, entries, actual map, full-Cartan transport, or any cone.**

## Named imports and limits

- The two explicitly named source constructions were read and hash-matched: `frontier-20261028-fixed-levi-level1-independent-v1.md` = `a001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a` and `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md` = `e5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f`. I independently checked the finite matrix-unit actions, complete free-Lie dimensions and local lowering consequences used above; I did **not** independently establish every premise of these source theorems.
- In particular the transitive full-Cartan/Serre/triangular structural import cited there as SHA `08217c89602bbed5bb05447144addfb1978037ad3e4c2e57271d88b794d98be9`, the positive-free-source/ideal-transport import `f08daf3e2259a563a426e8982be78a36094bb58e4d56f587b2b51f14fa8df46d`, and the qualified named PBW release `b80c97dbe4b2c112164f0880ea6cbc5eda5c46421dbb2786f5ca5ede64dac8f8` are **unverified premises** here, not newly established primary theorems. S1's normalized-transcription qualification governs the last one.
- The old cofactor cone and any claimed union with it were not reviewed; the bounded 400 one-row alternate search, other level-six types, the whole quadrant, `F6/B6`, arbitrary GCM/all-level Serre, any full-map kernel witness, novelty and priority are not established. Real selected-minor zeros are neither integer counterexamples nor full-map singular vectors. No external model, paid API, author contact, Git, publication, deletion, or infrastructure mutation was used.

## Independent code and receipts

All below are in this manifest directory, were exclusive-created, and use only Python standard library; the author's scripts were not imported. Each receipt has a native clock observed before its creation. Receipt creation intentionally refuses overwrite on a later rerun.

| Artifact | SHA-256 |
|---|---|
| `independent-226-check-v1.py` | `067833e1b61c306671b8f5858aee089b9d672b4b93dd09e2d16abdde00e63bfd` |
| `independent-226-receipt-v1.json` | `119d5a1981573c94047c2059097774ced42206482475d4763348584fa15da88c` |
| `independent-226-span-v1.py` | `929fda90cbfc2a425399446078749c0464023bc20d7d4b07ecdd848c8acf7100` |
| `independent-226-span-receipt-v1.json` | `107b5b05adbf8fcd8ae1bc9ab2229cd4a1be3d32f2d3e2ac212fee2d01c4c50c` |
| `independent-446-check-v1.py` | `c328be7489066042d553bb4a5ec58ae5bd9ae397f5f957b2cea8759cccfb2ff3` |
| `independent-446-receipt-v1.json` | `f9a0ada080fccce53a9c98b46ae793a4eb0a1b6f6e0e958680ce0b40e6da4abe` |
| `independent-446-crt-v1.py` | `3cec19ae93302d8d5ce13139d7830393f46c3075003c19ff1848bde94ebd912f` |
| `independent-446-crt-receipt-v1.json` | `73a535986dd78558fd3edbb075604e801eef364d975e3be93b95a502c0c6b8d1` |
