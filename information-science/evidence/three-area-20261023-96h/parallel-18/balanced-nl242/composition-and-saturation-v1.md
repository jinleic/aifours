# Final composition check: histogram redistribution, but no further residual-union shrink

Observed before creation: **2026-10-23T14:53:08-07:00**. Author: InfoBalancedNL242, info-6. Written-only response to the parent's requested composition question. The mod3 family remains **CANDIDATE**, with actual reconstruction pending.

## Decision

The two boundary statements can be put into one histogram-only necessary condition, and Parseval propagates them to a lower bound on the number of magnitude28 coefficients. **This is algebraic consolidation of the existing family plus baseline identities, not a strictly stronger restriction than their combined residual frontier.** It does not transfer a lower-rank function to full rank, eliminate a type, or establish a global ceiling240.

The automatic composition route is therefore saturated at the stated boundary. This does **not** prove that no new spatial S/R theorem, stronger scalar optimization, construction, or expert prior-art input could improve the problem. It says precisely that the two stated boundary theorems and the ordinary magnitude accounting do not by themselves do so.

## 1. All magnitude classes in the same coordinates

For a hypothetical balanced nine-variable peak<=28 target, write

`N_j=#{a:|W_f(a)|=j}`, `j in {0,4,8,12,16,20,24,28}`,

`L=N_4+N_12`, `d=N_8+N_24`, `u=N_0+2N_8`.

The nonzero support XOR s partitions the spectrum into256 coefficients divisible by8 and256 congruent to4 modulo8. Thus

`N_0+N_8+N_16+N_24=256`,

`N_4+N_12+N_20+N_28=256`.

Here d is the weight of the intrinsic quadratic on s-perp; u is the zero/eight-magnitude combination already used in the baseline (`u=z+2c`). No half of the truth table is fixed.

On the seven-type roster, exactly the full-rank cases have d=8 modulo16:

- lower ranks: d in `{112,128,144,160,192}`, all0 modulo16;
- full rank: d in `{120,136}`, both8 modulo16.

Consequently set `epsilon=(d/8 mod2)`. The complete current family is equivalently the single histogram condition

`L >=4+4epsilon`.                                         (1)

This is stronger than either theorem considered in isolation, but **exactly equivalent to their conjunction** on the existing roster. For every allowed d, (1) asserts only the already stated lower threshold on L. There is no extra numerical constraint in (1) that could remove another part of that frontier.

## 2. The actual forced magnitude redistribution

Eliminate N_16 and N_20 from Parseval `sum_j j^2 N_j=262144`. The even sector has energy

`65536+320d-256N_0-512N_8`.

The odd sector has energy

`102400-384L+128N_12+384N_28`.

Equating their sum to262144 yields the exact identity

`3N_28+N_12 =736-(5/2)d+2u+3L`.                           (2)

It also gives the exact residue constraint

`N_12 =736-(5/2)d+2u (mod3)`.

Since N_12<=L, (2) implies

`3N_28 >=736-(5/2)d+2u+2L`.

Combining this with (1) gives one all-type mixed necessary inequality

`6N_28+5d-4u >=1488+16epsilon`.                            (3)

Thus extra low odd-sector magnitudes do require extra magnitude28 mass at fixed d and u. This is real redistribution, but it is already forced by Parseval. The direction is not a contradiction: the magnitude28 class has room, and no premise in the family forces d to change its polar-rank branch when this mass changes.

Equations (1)–(3) are useful consolidated reporting/pruning conditions. They are **not a new scientific mechanism or an additional shrink of the residual union** once Parseval and the original boundary thresholds are retained.

## 3. A governing old scalar profile already reaches the new rank-eight boundary

To avoid treating a lack of contradiction as evidence, read the actual preserved source

`hard-continuation-20261015/quadratic-distance/remaining-types/results/explore.json.gz`,

SHA256 `1e1470a7d5380bb61ac5ebb95221f531c44fdd67f53a3463fe7e4fc3c98d5136`, member `explore.json`.

The accompanying `remaining-types/result.json`, SHA256

`5548853b6be9c2af0d251afe2ca4101c4b70437fdda19e1d5c21977e4aa16d2c`,

records its finite audit and scalar statistics. No audit or old solver was rerun. The source's Proposition1.3 says its scalar witnesses satisfy the canonical local pairs, both Parseval equations, canonical sums, type zero/count restrictions, and the shared quadratic-correlation budgets for D,J_g,J_h. Their genuine Boolean realizability is expressly not claimed.

The archived `(8,136)` profile has L=8, exactly the new full-rank lower threshold. Its explicit canonical-pair count table is:

| K_g | K_h | count |
|---:|---:|---:|
|2|18|2|
|2|-22|22|
|2|26|44|
|-6|18|1|
|-6|-22|22|
|10|10|18|
|10|18|1|
|-14|2|6|
|-14|10|1|
|-14|-14|52|
|18|10|1|
|-22|2|19|
|-22|-6|20|
|26|2|47|

Every entry is a permitted canonical pair with `|K_g|+|K_h|<=28`. For S=K_g+K_h, R=K_g-K_h, its magnitude histogram is

| magnitude j |0|4|8|12|16|20|24|28|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| N_j |70|1|2|7|50|61|134|187|

Direct written summation gives

`L=8`, `d=136`, `u=74`,

`sum K_g=sum K_h=-256`,

`sum K_g^2=sum K_h^2=65536`,

`sum S=-512`, `sum R=0`, `sum SR=0`,

`sum S^2=172032`, `sum R^2=90112`,

`Gamma_D=sum(-1)^D S=-4096`.

For example, the pair counts give the first individual square sum as

`4*68+36*23+100*19+196*59+324+484*39+676*47=65536`.

The histogram gives total energy

`64*2+256*50+576*134 +16+144*7+400*61+784*187=262144`.

Equation (2) is exact: `3*187+7=568=736-340+148+24`. Inequality (3) has left side `6*187+5*136-4*74=1506`, versus required1504. The scalar profile therefore survives even near the composed redistribution boundary.

**It is not a Boolean function, not a balanced242 witness, not an S-side realization, and not evidence that type(8,136) is feasible.** It proves only that composing the stated multiplicity boundaries with those retained scalar identities is not an unrestricted impossibility proof. Exact common coordinates, sign realization and the full S/R Fourier partition remain indispensable.

## 4. Lower-rank status was not silently promoted

The same archived audit records these L values:

| type | archived L | effect of current family |
|---|---:|---|
|(2,192)|8|survives L>=4|
|(4,160)|2|this particular profile is removed|
|(6,112)|17|survives L>=4|
|(6,128)|17|survives L>=4|
|(6,144)|2|this particular profile is removed|
|(8,120)|10|survives L>=8|
|(8,136)|8|survives L>=8|

The two L=2 scalar vectors must **not** be cited as witnesses for the newly strengthened feasible region. No replacement scalar vectors or Boolean objects are manufactured here. Whether the complete old scalar model plus the new cut is still feasible in those two types has not been established by this composition check. An unchecked claim of scalar UNSAT would not exclude a type either.

This limitation does not alter the logical conclusion about (1)–(3): no statement among the two boundary theorems maps either lower-rank type to full rank or forces a new value of d. Resolving those two updated scalar regions would be an additional mathematical/encoding obligation, not automatic composition. The original source also warns that counts are not the full spatial problem.

## 5. Final measurable frontier and next input

The candidate family still leaves exactly

- five lower-rank types with L>=4;
- two full-rank types with L>=8.

The sharp all-type ceiling remains NL<=240 under L<=3, with the exact classical q8+t attainment. No stronger unconditional ceiling or general construction follows from the redistribution identity.

**Mechanism decision:** stop adding per-defect manuscripts as though they independently solve the target. The next consequential full-target input is an actual joint Boolean S/R realization (yielding all512 bits through the frozen modular-saturation criterion), a genuinely new spatial obstruction for the residual union, or a parent-discussed distinct redirect. There is no new execution authorization, no queued solver command, and no substitute review-only problem.

All current claims remain at the author-written candidate level until the actual queued reconstruction and parent checks return. Scalar consistency, full Boolean correctness, finite replay, formal proof, novelty and significance are separate gates.
