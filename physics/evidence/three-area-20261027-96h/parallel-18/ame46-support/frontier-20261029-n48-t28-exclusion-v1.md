# Candidate: no support-48 AME(4,6) state has exactly 28 maximal coefficients

Owner **PhysicsAME46-2**. Native clock before writing: `Thu Oct 29 12:04:58 PDT 2026` (last observation; not an exact completion time). **WRITTEN reduction plus exact-CNF certificates**, not independently reviewed, adopted, formally verified or novelty-cleared. No classical import (no no-OLS(6), no f113, no no-Hamming-one), no phase argument and no held material is used.

## 1. Claim

A normalized complex AME(4,6) state in any product basis cannot have support `N=48` together with exactly `t=28` coefficients of modulus1/6.

This is one exact (N,t) case. It does not by itself decide N=48; see the separate composition packet, if any.

## 2. Elementary facts

Write U=6psi for the36x36 unitary of each2|2 cut, P for the t maximal coefficients and E for the rest of the support; |E|=N-t=20.

**(R1) Maximal words.** An entry of U of modulus1 exhausts the norm of its row and its column, so it is the only nonzero entry there, in every cut. Every one of the six pair systems is the row index of one cut or the column index of one cut. Hence two P words never share a pair value, and no E word shares a pair value with a P word.

**(R2) Pair partition.** In each pair system the28 P words carry28 distinct values. Every other value is carried by E, since no row or column of a unitary vanishes, and by at least two E words: a value carried once would be a row or column with one nonzero entry, which would have modulus1 and belong to P. So each system has exactly `n=8` E-carried values with multiplicities m>=2, summing to20. Hence `Σ(m-2)=4` and every m<=6.

**(R3) Partner degrees.** Let A_i be the set of E symbols at party i, r_i=|A_i|. For a in A_i let m_i(a) be the number of P words with value a at i. In system (i,j), the six values (a,y) are P-carried exactly m_i(a) times (distinct y by (R1)) and otherwise E-carried. Thus `d_i(a):=|π_j(E_a)|=6-m_i(a)` for **every** j≠i. If d_i(a)=1, every other coordinate is constant on E_a, so E_a is one word and its pair values have multiplicity1, contradicting (R2). Hence d_i(a)>=2, `Σ_a d_i(a)=8` (the eight E-carried values of system (i,j) split by their i value) and d_i(a)<=r_j. So 2<=r_i<=4 and, since the eight values of system (i,j) lie in A_i x A_j, r_i r_j>=8.

**(R4) Activity identity and the five cases.** For a P word p let k(p) be the number of coordinates whose value lies in the corresponding A_i. By (R3), `Σ_p k(p)=Σ_i(6r_i-8)`; by (R1),(R2), `Σ_p C(k(p),2)=Σ_{i<j}(r_i r_j-8)`. As (k-1)(k-2)/2 is nonnegative on integers,

`0 <= Σ_p (k-1)(k-2)/2 = Σ_{i<j} r_i r_j - 6Σ_i r_i + 12`.

Among sorted size vectors with entries2..4 and pairwise products>=8 (a2 forces all others4), the values are 3333:-6, 3334:-3, 3344:1, 3444:6, 4444:12, 2444:0. So the profile is one of 2444, 3344, 3444, 4444. Relabel parties so sizes ascend and relabel E symbols inside each party so degrees ascend. With d in [2,min_{j≠i} r_j] summing to8, the degree vectors are: size4: 2222; size3 inside 3444: 224 or233; size3 inside 3344: 233; size2: 44. These are exactly five cases.

**(R5) Unique-overlap rule.** In every cut, two distinct rows (or two distinct columns) of U that share exactly one nonzero position have a single nonzero product as inner product, so they cannot be orthogonal. E rows contain no P entries by (R1), so this is a condition on E alone.

**(R6) P code.** By (R1),(R2), the28 P words carry every non-E value of all six pair systems exactly once and no E value.

## 3. Encoding

The frozen encoder `frontier-20261029-n48-t28-support-cnf-v1.py` (SHA-256 `0755a5b4d2e296898c04cc06ff818a911781beab5b8aff9e1bcb92bee043bc43`, base cardinality encoder SHA-256 `844ea38848e6678e806113f91ed1a6ca2f9541eae5d009b0b7e833c516a4ecf9`) has one E variable per word of the residual box and, with --joint-P, one P variable per word of {0..5}^4. Its constraints are exactly: |E|=20; per system exactly8 E-carried values, each carried by2..cap E words (no value exactly once); per symbol degree d_i(a) in each system containing i; (R5) for rows and columns of all three cuts; and (R6). Its cap is4. A parametric re-implementation in `frontier-20261029-t28-encoder-controls-v2.py` produces identical clause lists at cap4 for all ten formulas, and the robustness batch reruns all five cases at **cap6, which needs only (R2)**. Thus no multiplicity-four lemma is required.

## 4. Certificates (CaDiCaL 3.0.1 --plain textual LRAT, independent RUP checker through EOF)

Cap6, joint P (sufficient for the claim; batch `frontier-20261029-n48-t28-mult6-batch-v1.py`, receipt list `sat-20261029/t28-cert/batch-t28m6-P-v1.json`, SHA-256 `1626bb9c04d641d1896dbcd4ee7df5b90ed7e0e7fa571685eb1b693c1a41f058`):

| case | degrees | CNF SHA-256 | LRAT SHA-256 | RUP receipt SHA-256 |
|---|---|---|---|---|
| 4444 | 2222/2222/2222/2222 | `c5e043b16fcc80559fbbcfc286fbe4b9b0a38a8186da3bbb09c0d1b4b83376d2` | `7496fdde089e4d6e041973129a5cbed651af8033ec7ecf91fcef80648e4069f1` | `15458777673dd480afc96c589333f81caae875603a3299895f4f4286966c7b3a` |
| 3444a | 224/2222/2222/2222 | `48f70ff8a3818edada875cb1ea56169e10caba9a9efa73f892d04563c9982a3a` | `948940af571ee62ee4871b77114da819fb528bc60ef0483c2d6b8f46659ca34e` | `dfbfcffbca975df32cc342c30c085e0f158b9448c3145c0cd234b9ce10155124` |
| 3444b | 233/2222/2222/2222 | `c23f502426eb42317c9a8adb46b421124393d3d02afdf28047b96a17e5db95dc` | `371c0599c124c9cee3812597b80a2d94858ae9c0ea24328031e258457e50ee84` | `4cc017545efcea56ffdec193ca1b18fa5f66b35a352fcadfbf99c5a2043b53e0` |
| 3344 | 233/233/2222/2222 | `08538df1eb8f86295e820e89076b6dc51d6e4622a565ef869b55cba24852210a` | `86891faec723066e1c042363e04621ddf5476328d4f85558ba37d67b1fcbdb31` | `f7a4b745038d93c8d70e32c9239180db2c7743ac8868842fa4e56ed0a3fc986f` |
| 2444 | 44/2222/2222/2222 | `fde3f01910943875961b76a15eb8bc55253052fa5b5bc54152074c6608f6f84d` | `d8b4aaca23d4c227d1d8c4057614fccad768fd755382642f822976658fe6a9fe` | `c04119dc9c27e1126a4a26f672755668530b53cab5428f44ba47ba9c15d28e31` |

Cap4 frozen encoder, joint P (batch `frontier-20261029-n48-t28-batch-v1.py`, list `sat-20261029/t28-cert/batch-t28-P-v1.json`, SHA-256 `e3b12f5f2f685ca3c86cfbab9d050996837a3d25d4e6e7e5a3f6b071c233c777`):

| case | CNF SHA-256 | LRAT SHA-256 | RUP receipt SHA-256 |
|---|---|---|---|
| 4444 | `4361ada37d4bde809e3abaab41cd1d502eca86573c0388024761a666f4b0fc56` | `3adb8e4aa135a2d960073f94e6c8214ee7db31c311c82aecd03c3b259f4553c0` | `94005530ec966a1284415089dff6f87f4d4c755307b6aab69a0c8568f3f0656c` |
| 3444a | `455eb6c792b210055ef242ce721588133ca35fbfeefd21d4f92991062cd3bb47` | `fbfd3a29a97ffa625ee8790cf3cc7d43359a0bddfe204a2d547b066ca59979ee` | `5b16df37381b320c6eda8727bb799207c91f2305989d3308975f7efbd93b6afe` |
| 3444b | `4805f28e6690940ae0ae8c5738c00d03749de92ffce23d1a9919eb1e7b2c9187` | `7372fd962cbe9bf2b2d8a42b7911f050d0519aacaca80f136843de9255fe90e4` | `e72416c0fdb50459b5d2f08cf9e095c2cc0f4dc44dde6a72ee2875159a4aeb37` |
| 3344 | `285a4780b3c68abad2b55b842250cf8823f825e44990a2876b0023d5134dd7db` | `96bb115bc169c1608dd11b639d218098556824b64d82a69a0aa8e36a5f4e3843` | `38b8b3bff0f47db22c9e417d55373bc5a4c4b7546495c7fe33216a183f7fe9b6` |
| 2444 | `ddc46aa73c5a2e366fdc503ee2d225f8f3cb36a48811dee06c2cee14d67a19ea` | `a014c197e3b534c59912625688a0ded5a3c4569c06ac61ac84225054822ce8ef` | `1205bb4fdbb4a643952976b93b5e115b43b2029a3d4716b3674f48c5f477c8c7` |

RUP checker `frontier-20261029-lrat-rup-check-v2.py`, SHA-256 `d04eb821104b12bfddfb3d6e9a6f7a03b4f97ae65247959de6eddaa39ab99366`. Every receipt reports VERIFIED_TEXT_LRAT_RUP. E-only versions (no P code) are SAT for 4444,3444(224),2444; their models contain, for instance, a4x4 component with two identical two-entry rows, which unitarity forbids. So the P code is load-bearing; no E-only claim is made for those cases.

## 5. Controls (not the proof)

`frontier-20261029-t28-encoder-controls-v2.json` (SHA-256 `50696fd25ab37ada728b611410fdf7708effe4284e485de5f0432e442d5d6497`): clause identity of the parametric and frozen encoders for all ten t28 formulas; with n24,|E|48,cap2 and the partner degrees of the exactly verified60-term AME support, unit clauses fixing that support's E and P words give SAT, while replacing one P word by a word that repeats another P word's pair value gives UNSAT. Version v1 of that control crashed while reading the witness record and wrote no receipt.

## 6. Scope and review points

The mathematical content is §2 and the claim that the CNF encodes exactly those conditions for the five cases. An UNSAT certificate proves only that its exact CNF has no model. Independent review should re-derive (R1)–(R6), the five-case list including the relabeling conventions, and audit the encoder clauses (cardinality encoder, the exactly-once/none P constraints, the unique-overlap gadget). No support-48 witness, global lower bound, formal proof or novelty is claimed here.
