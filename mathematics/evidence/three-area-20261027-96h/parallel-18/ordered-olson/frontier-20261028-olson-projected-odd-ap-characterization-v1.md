# A projection-only odd-run arithmetic-progression characterization

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 20:15:51 PDT 2026**. This is a NEW **WRITTEN candidate** about a reflection-only projection, with bounded exact checks below. It is NOT a repaired actual-block theorem, a full L_RES result, a formal proof or an independently reviewed/novelty-cleared claim.

Before reviewing any later proposed use of this source, read the FATAL source-correspondence record `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`. NO old f111 assessment or actual-block identification is transferred.

## 1. Definitions and statement: projection ONLY

Let p be ANY odd prime and let an actual `D_(2p)` word contain exactly F=3p−2 reflections, among arbitrary rotations. DELETE ALL ROTATIONS solely to form its cyclic REFLECTION-ONLY projection; decompose that projected cyclic sequence into maximal constant-exponent runs. Write `o_π,e_π,H_π` for the odd-run count, even-run count and sum of floor-half-lengths in THIS projection. These symbols deliberately differ from the historical actual occupied-gap block counts `o_F,e_F,H`.

Assume `o_π=p`. Then `H_π=(F−p)/2=p−1`.

**Necessary condition.** If there is no original-order reflection-only identity selection of length2p, the p odd projected-run exponents, in their cyclic order, are the p distinct values

`c, c+d, c+2d, ..., c+(p−1)d`,  `d!=0`,

for some c,d∈F_p. Even projected runs may exist; no converse is asserted for them.

**Exact special case.** If `e_π=0` as well, this arithmetic-progression condition is also sufficient for reflection-only failure. In that case the exact reflection-only `2p` product support is `F_p\{0}`.

These statements concern projection data ONLY. They do not say when an actual word has `o_π=p`, nor equate it with any actual-block or L_RES hypothesis.

## 2. Necessity: duplicate and four-term selectors

Each projected constant run supplies floor-half-length equal-reflection pairs, and each odd projected run supplies one further representative. Select reflections only; rotations are all skipped, so those pairs are actual adjacent equal factors in the selected reflection word.

If two odd projected-run exponents agree, select their two representatives and all `H_π=p−1` equal-reflection pairs. This is exactly2p actual reflections, and after cancelling each equal pair the two equal representatives multiply to1. Thus REF failure forces the p odd-run exponents to be distinct; since there are p field values, they exhaust F_p.

Suppose four of those p odd-run exponents, in projected cyclic order, have alternating sum0. Select their four actual representatives and ANY p−2 of the p−1 equal-reflection pairs. Each odd run can supply its representative disjointly from all of its pair choices. The resulting `4+2(p−2)=2p` reflections multiply to1 after cancelling the equal pairs. Hence under REF failure there is NO such four-term zero among the odd-run exponent list.

Cut the p odd-run exponents at an arbitrary run boundary. They form a permutation of F_p, so every value occurs and adjacent values differ. If there is no ordered alternating-zero quadruple, for each consecutive triple define `t=z_i−z_(i+1)+z_(i+2)`. The value t occurs in the list. An occurrence before or after the triple would give a zero quadruple. It cannot equal the first or last triple value, because adjacent values differ; therefore it equals the middle value. This forces every consecutive difference to be the same nonzero d. Hence the p labels are an affine arithmetic progression, including its cyclic wrap. This is an elementary full-support argument; it does NOT require the held f111 disposition or the unreviewed standalone p+2 lemma.

Every selector constructed after a cyclic cut uses actual reflection occurrences. Sorting them back into the original full-word order cyclically rotates an identity product; if UV=1, then VU=1. Therefore the contradiction is in the original order.

## 3. Sufficiency when all projected runs are odd

Now suppose `e_π=0` and the p projected-run labels are `c+j d` for j=0,...,p−1 in cyclic order, d!=0. A selection of exactly2p reflections cannot select an even number from every run: those even selections use at most `2H_π=2p−2` occurrences. Hence it activates at least two odd runs. Their number is even because2p is even.

Cut at the arithmetic start and write the active labels by `0<=j_1<...<j_(2t)<=p−1`. After cancelling equal pairs inside the selected runs, the reflection exponent is

`−d * sum_(r=1)^t (j_(2r)−j_(2r−1))`.

The integer sum of these positive disjoint gaps lies between1 and p−1, so the exponent is nonzero. This remains nonzero after returning to the original cyclic start because a cyclic rotation of a nonidentity group product is conjugate to it.

Conversely, select all p−1 equal pairs and activate just the runs labeled c and c+j d, for j=1,...,p−1. These are actual `2p`-reflection selections and realize every nonzero exponent `−j d`. Thus the exact support is `F_p\{0}`. If even projected runs exist, they can contribute odd selected counts, and this sufficiency argument DOES NOT apply.

## 4. Actual data and limits

The AP/e0 actual family `frontier-20261028-olson-ap-e0-actual-residual-family-v1.md`, SHA256 `c69379a1321041dbd66b88b3dd16609dbb33effe66aef5e0b5ebf6f151ee8d26`, illustrates the exact projection premise, but its actual occupied-gap/block and caller analysis is a SEPARATE unreviewed candidate. This paper neither imports that analysis nor infers actual `o_F,e_F` from `o_π,e_π`.

`frontier-20261028-olson-projected-ap-experiment.py`, SHA256 `9b795bc18a725f7dea897d3439c9bd4628a4e9d87c44ef6cb2b1565932368398`, generated 250 projection-only odd-AP fixtures at p=3,5,7,11,13. Data `frontier-20261028-olson-projected-ap-results.json` has SHA256 `6a6d52b2492c6724a0f250aa1c3df0ad2e870ab2f6d69ca0490794bf5f594838`. Separately written `frontier-20261028-olson-projected-ap-checker.py`, SHA256 `38152bd196c0267738005283da2e6bb4fde442a3fca9e09f7cb7fd65f1169112`, returned `PASS_INDEPENDENT_PROJECTED_AP_PARITY_AUDIT` in result SHA256 `5099ef9b0f0fbd9d2366e7ec4f59aae160f8bca0013163b63721760aba5c31c3`: it checked 259,950 even active-run subsets and found zero alternating sums absent, and independently found ordered zero-four witnesses for 200 non-AP swaps; duplicate-label and pair-count mutations were rejected. These checks are finite, same-harness and projection-only.

No independent full-source scientific review, formal/kernel proof, cross-family validation or novelty determination has occurred. In particular, this source does not prove L_RES and does not rehabilitate any withdrawn actual-block application.

**END — projection-only characterization and explicit nontransfers.**
