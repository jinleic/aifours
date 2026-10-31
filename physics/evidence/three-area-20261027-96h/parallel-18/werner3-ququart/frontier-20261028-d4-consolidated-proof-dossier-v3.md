# Three-copy d=4 original q3: consolidated written/computer-assisted dossier v3

**PhysicsResearch96h-2 / physics-1.** Native clock before writing: Wed Oct 28 20:06:41 PDT 2026. This is a consolidated **fixed-d4 proof candidate** for an already publicly claimed result. Its exact finite identity and positivity calculations have been executed as described below; mathematical source validity, Python/NumPy/FLINT/hash/OS and the stated inputs remain in the trust base. It is not a formal/Lean proof, independent human/other-model-family review, parent/f62 adoption, physical operational/distillability result, general-dimensional theorem or new-discovery claim.

## 1. Exact theorem and actual-object lift

Let H=(C⁴)^tensor3. For **every complex** C:H→H with rank<=2, including0/1, singular, nonnormal and non-Hermitian C, define the original unnormalized-trace functional

`q3(C)=||C||HS²−(1/2)Σ_i||Tr_i C||HS²
       +(1/4)Σ_(i<j)||Tr_ij C||HS²−(1/8)|Tr C|²`.

The source/certificate proof below supports `q3(C)>=0` for this complete d4 domain. Public Tomar v3/v4 already claims the broader three-copy target; the actual d4 certificate archives in those two records are byte-identical, SHA256 `2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3`. We do not independently assert its all-d route, other-copy claims or physical operational conclusion.

For nonzero C, scale to `||C||HS²=1/2`; choose an isometry A:C²→H containing ran C and set B=2C†A. Then `C=AB†/2`, `||B||HS²=2`. With `a=vec(A)/sqrt2`, `b=vec(B)/sqrt2` in V=H⊗Q, Q=C²,

`||a||=||b||=1`, `Tr_H |a><a|=I_Q/2`,
`C_xy=Σ_r a_(x,r) conjugate(b_(y,r))`.

Conversely every such physical pair gives a normalized original rank<=2 C; orthonormal completion includes rank1, and C=0 is immediate. For any subset S of the physical sites,

`||Tr_S C||HS² = <a⊗b,F_Q F_S(a⊗b)>`.                                  (1)

F_Q swaps the Q replicas and F_S swaps exactly the sites in S. This is a literal index identity for the **same** complex a,b. An independent formal-coefficient check covered all eight S and131072 exact term occurrences, script/result SHAs `fc70405ca23ebb76ca08d4539ff0251db4760a4614b0a3367995cb7c0086b5f6` / `ea9eff59833ccdd487a1ca4ace3b56f05c54a2b7711e1d09b7e8b5bfa130bf99`; it checked identity, not positivity.

## 2. Three same-pair source moments, objective and true PSD blocks

Form `Y31=|aaab><aaab|`, `Y22=|aabb><aabb|`, `Y13=|bbba><bbba|` on four complete V replicas. Apply the **same** local `U(4)^3×U(2)` unitary twirl, physical site permutations and simultaneous complex conjugation; multiply the average by `L=(2·4³)^4`. Call the three real symmetric moments X31,X22,X13. Local Q unitaries cancel in C, physical local conjugations, site permutations and complex conjugation preserve the sums of partial-trace norms. Thus (1) gives

`q3(C)=L^(-1)Tr[(F_Q product_i(I−F_i/2))_(replicas 0,3) · X31] = c(X)`.

For a four-component permutation word w=(p1,p2,p3,pQ) and tau=(0 3), the exact source objective is

`c(V_w) = [product_i(2·4^cycles(p_i)−4^cycles(tau p_i))]
           ·2^cycles(tau pQ) / 2^31`.                                    (2)

The independent cycle-versus-fixed-basis audit checked all331776 word numerators and denominator2^31, result SHA256 `080a2c8cfd6794ec74d3c435fc1daf3b1c52d94ae574a0c83e884acde07f717e`.

The actual d4 source data have **1126 single-row and111 coupled-row** Gram types; no `gram2` type is used. A single row is the outer product of its four complete replica factors, with starred replicas complex-conjugated, hence PSD. For each coupled type,

`u=a⊗a⊗b⊗conjugate(a)`, `v=b⊗b⊗a⊗conjugate(b)`,
`G=|u⊕v><u⊕v| = [[|u><u|,|u><v|],[|v><u|,|v><v|]] >=0`.

The two rows have the same cut, so under the common U they carry the same `U⊗U⊗U⊗conjugate(U)` representation; their **whole joint block**, not merely its diagonals, stays PSD under the twirl. Any actual integer module/joint compression preserves PSD by congruence.

The four original-family index rearrangements for u/u, u/v, v/u, v/v are written in `frontier-20261028-d4-consolidated-operator-certificate-proof-v1.md`, SHA256 `a6fb579592ffacd71cb0d8c115e5aea20209fc07395304be9b79651dbf1f646e`. The stronger `frontier-20261028-d4-all-gram-physical-bridge-audit-v1.md`, SHA256 `719c7a029954fadfc73b6496bb7f2e07659ca5acf4b82faa00a370c3a13dd815`, checked the actual owner's source-family/index rule against formal arbitrary-complex physical factors for **all1570 row-pair occurrences /17 distinct pairs**, zero mismatches and17 detected cross-letter faults. No physical instance is sampled.

## 3. All actual same-pair equalities

For an a-replica r, the Stiefel marginal gives

`2 Tr_(H_r)Y − I_(Q_r)⊗Tr_(V_r)Y = 0`.

Actual family31/22 use r=0 and family13 uses r=3; each is an a-replica. For aab, delete replica2 from `aaab` and `aabb`, retaining `(0,1,3)` in each. For abb, delete replica1 from `aabb` retaining `(0,2,3)`, and from `bbba` retaining **`(3,0,2)`**. In each case the deleted unit a/b gives the same ordered surviving physical pure moment, and the same common twirl preserves it.

The actual source's two signed parts use the **same compression module keys at all four factors**, not just equal shapes. All329 corrected lambda coordinates are valid against every corresponding part; actual counts are104/106/15 Stiefel31/22/13 and51/53 aab/abb. The independent exact audit and source-data fault controls are `frontier-20261028-d4-physical-equality-binding-audit-v1.md`, SHA256 `da583826005bc1874f7a8168ec1368f2654c05a71d8737ac85bc73c5d0e42563`. Arbitrary real lambda coefficients multiply exact physical zeros.

## 4. Complete actual source span and independently reindexed orbits

For each n∈{2,4}, invariance of `(C^n)^tensor4` under all local U(n) implies equal diagonal weights and the integer commutator constraints for `rho(E_ij)`. All24 replica permutations lie in their kernel. For n2 the 70-variable constraint system has a rank≥56 modular minor and the permutation columns have rank≥14; for n4 the 2716-variable system has ranks≥2692 and≥24. The rank sandwich forces the local commutants to equal those permutation spans. The standard-library witness checks all112 /20640 literal constraints against all24 permutations, and the exact permutation minors both have determinant−1; full proof is `frontier-20261028-d4-four-replica-commutant-finite-rank-proof-v1.md`, SHA256 `49df4f874bf8c4a4da60d61f1b76d9b8028e2acfca5fe6d8c2b378a324501a23`.

The actual 14 n2 permutation-minor row labels were separately checked as **valid same-weight 0/1 four-tuples**, and the literal determinant recomputed −1. This pays a semantic input check missing from the earlier standalone checker's inner guards; its full old SHA guard still rejected altered files, and the actual witness was valid. Audit SHA256 `30d6fa839420bca24962cfcefbdacaeed7c8907663d1b9e05a62da431a1158e4`.

The tensor product of these four local commutants spans every physical twirled X_f by 24⁴ permutation words. Independent left/right stabilizers of repeated source letters, physical site permutations and simultaneous inversion then give real source orbit sums; no word/orbit linear independence is needed. Direct canonical minimization classified **all331776 words in every family**, yielding 1142/2391/1142 orbits and agreeing word-for-word with the separate union-find partition; proof/result SHAs `91e4ec3fc4a135da325d4918162c63a4aa460f9a75b0d2aee8f9f4ab07923fe3` / `cc528c41e387371dd64b5e9e92263df6f977519fa1aef114e3a3ad21dc55e94b`.

## 5. Exact corrected identity and saved-matrix positivity

The final rational data, not the initial approximate base, are `frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz`, SHA256 `c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94`. The checked source functional is

`c(X)=Σ_t Tr[Z_t K_t† M_t(X)K_t]+Σ_e lambda_e E_e(X)`.                  (3)

Every actual local Gram/equality/objective map consumed by the owner checker was independently reconstructed by finite basis/trace indices and compared entrywise: **2016 site Gram maps/9672 entries**, **1224 auxiliary Gram maps/5712 entries**, **648 equality maps/1752 entries**, and all objective words; zero mismatches. The qualified complete owner-map audit is `frontier-20261028-d4-owner-local-map-closure-v1.md`, SHA256 `24e9a465d057d92960f1211a9ddcd833ee67ca2aae120ef1b80cecee3bba79c7`.

An independently arranged full rational identity verifier uses direct-canonical source orbits, opposite equal-letter matching, explicit literal local maps, cycle objective and reverse-axis integer modular contraction. It computed **zero on all4675 orbits for all424 distinct verified denominator-safe primes**. The actual common D has6645 bits; the freshly recomputed integer B has6745 bits; the exact tested-prime product P has6761 bits and `P>2B`. Thus each integer-scaled residual is zero by divisibility and `|R|<=B<P/2`. The 17 reverse physical row rules were additionally checked against the owner's rules via actual source stabilizers over all24 permutations.

The strongest **actual entrypoint/helper/data byte-bound run** is `frontier-20261028-d4-reverse-entrypoint-snapshot-v3-proof-v1.md`, SHA256 `55cb4fe7ed7a950a8c78e6209d5ead4cfa7bbf3bf41efd02afb55da516753926`, full result SHA256 `50f53a57e59eda9f40bb28ba2df1feb9ace8ce43e3a2d60530b1db8a34c95687`. It is the SAME reverse algorithm as the prior v2, freshly run from verified byte snapshots, not an additional independent algorithm. A separately written standard-library source/data bound/prime audit rederived D, all source factors, B and P using verified byte snapshots; an independent stdlib exhaustive local scan supplied its `Amax=256`, `Emax=24`. The newest stdlib audit SHA256 `efb700266ff411bc2888441ecb3e85a2cb819ae2e2a54a2aeddd6a4a2278c854` and local-maxima audit SHA256 `0389e4628a5dbb87a72ddb44ddff49da9d888818ed0279838fb81da5179245ed` do **not** themselves rerun the 424 residuals.

All **1237 corrected Z_t** were separately read from saved bytes and proved positive definite by exact rational Schur and integer Bareiss/Sylvester elimination, 4149 positive pivots, result SHA256 `5e6a3c0c7be0cf34c1b12cc2d8bf49ae958368a2254dac7fc6e169f3bacf04f6`; Main also reported an independently written standard-library Fraction Schur pass but its artifact is not asserted here. Source-data, row/index, partition, identity and PSD fault controls are cited in the detailed audits and are not physical counterexamples.

## 6. Conditional original theorem and exact boundaries

On an actual physical tuple X, every M_t(X) is PSD by §2 and every E_e(X)=0 by §3. Each saved Z_t is PSD, so

`Tr[Z_t K_t† M_t(X) K_t] = || M_t(X)^(1/2) K_t Z_t^(1/2) ||HS² >=0`.

The source span in §4 and exact source identity in §5 give `c(X)>=0`. Section1 identifies c(X)=q3(C); positive homogeneity and C=0 cover the complete original complex-rank<=2 domain. This is a **computer-assisted written proof candidate**, conditional on the actual pinned code/data/arithmetic and physical/source arguments, not a claim that every dependency has already received independent family/human/kernel acceptance.

The old reverse-v1 input-loader helper was not session-pinned; that historical run remains qualified in `frontier-20261028-1938-reverse-crt-base-loader-binding-gap-v1.json`, SHA256 `2f5706462331f27d720803f0af008483292abaf3eb29265ae026b97da99d4e45`. The prospective v2/v3 source snapshots do not retroactively cure it. The earlier 20/30-minute cadence gaps and unknown cause remain in `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`; Main actually read that record and explicitly released prospective work. No uninterrupted-supervision or source-falsity inference is made.

The prior paper claims the full target, so this is not novelty clearance. No all-d>=9 verification, other-copy result, physical distillability theorem, strict/equality classification, external human/model-family, formal/Lean, f62 or parent adoption is asserted. f62's frozen review is not silently enlarged by later material; any new review must be prospectively assigned. Old held/quarantined outcomes are not premises.
