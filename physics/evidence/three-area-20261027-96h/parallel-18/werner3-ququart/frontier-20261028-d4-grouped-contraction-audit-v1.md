# Actual d4 grouped Gram aggregation versus direct per-type contractions

**PhysicsResearch96h-2 / physics-1.** Native clock before this writing: Wed Oct 28 19:07:16 PDT 2026. The finite diagnostic below was actually authored/executed **before** the late-cadence gap was noticed. The complete disclosure and self-stop are preserved in `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`; Main explicitly reported reading that entire record and prospectively released primary work. The actual gaps remain a disclosed process deviation. The check is **unreviewed, one-prime and two weighted projections**, not full coefficient or certificate closure.

## 1. The source-to-aggregation index step

For one actual source row-pattern group g, write the four local compressed maps as `A_l[p,(i_l,j_l)]`, with l=1,2,3,Q and p∈S4. For type t and physical Gram row pair (r,s), the actual joint integer compression W_t is split into `W_(t,r)` and `W_(t,s)`; Z_t is the corresponding real symmetric corrected rational multiplier. The literal contribution to a source word p is

`Σ_t Σ_(i,j) [W_(t,r) Z_t W_(t,s)^T]_(i,j)
                product_l A_l[p_l,(i_l,j_l)]`.                           (1)

The source real W and symmetric Z are important to the trace convention: with the **whole** Gram block B=WZWᵀ, Bᵀ=B and, for an arbitrary compatible M,

`Tr[Z Wᵀ M W] = Tr[B M] = Σ_(u,v) B_(u,v) M_(u,v)`.

The last equality follows by interchanging u,v and using B symmetric; it does not require each isolated row-pair block or an arbitrary source word M itself to be symmetric. The owner checker enumerates both row orders. The actual 1570 physical row-pair mappings are separately proved and symbolically checked in `frontier-20261028-d4-all-gram-physical-bridge-audit-v1.md`, SHA256 `719c7a029954fadfc73b6496bb7f2e07659ca5acf4b82faa00a370c3a13dd815`.

Grouping types by their source family, exact row index rule and cut inserts each pair's `W_r Z W_sᵀ` into its module's coordinate offsets. If local dimensions are `(d1,d2,d3,dQ)`, the ordinary row-major bijection

`(i1,i2,i3,iQ ; j1,j2,j3,jQ)`
`<-> ((i1,j1),(i2,j2),(i3,j3),(iQ,jQ))`

is the owner's exact reshape/transpose. Applying the four local maps then yields (1) by repeated distributivity. Modules need not be orthogonal, complete, independent, invertible or square: the group tensor simply sums their actual congruence contributions.

## 2. Two independently arranged finite projections

For arbitrary weights `w_l[p]` on each local permutation axis, put

`L_l^(module)[i,j] = Σ_p w_l[p] A_l[p,(i,j)]`.

Then contracting (1) against the tensor-product weight `product_l w_l[p_l]` is, by exchanging finite sums,

`Σ_t < W_(t,r) Z_t W_(t,s)^T,
       L_1^(m1) ⊗ L_2^(m2) ⊗ L_3^(m3) ⊗ L_Q^(mQ) >_entrywise`.     (2)

Equation (2) gives a **per-type Kronecker contraction** that does not use grouped module offsets or the owner's 8-index interleaving. The alternative is to first assemble the group-offset tensor and project its four axes with the same weights. Their equality for arbitrary weights is an elementary finite-sum identity; comparing two specific weight tensors below is a targeted implementation diagnostic, not a check of all its coefficients.

The fixed-d4 script `frontier-20261028-d4-grouped-versus-per-type-contraction-check.py`, SHA256 `68e226dd6888b26d33364b0f6ce56e38a4a04b34da3f828c830ffec4a8efb6bc`, reads the actual pinned public source/corrected data and owner row/local-map helpers. It uses trial-division-verified prime 65521, checks every used corrected Z denominator is invertible, and reduces every intermediate exact integer operation modulo p. It checks signed-int64 bounds for each rank/dimension/axis contraction; no floating tolerance is used. The two fixed weight tensors are deterministic source-**word** functionals over all 24⁴ words; they are not chosen original physical C, states or parameter controls.

Actual one-process execution with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` produced `frontier-20261028-d4-grouped-versus-per-type-contraction-check-results.json`, SHA256 `0c93b7316404981a4395bdc43f8925052d23d616e8b2d26624a3480b103a877a`: **PASS in 1.043 s**. All **17** actual row-pattern groups matched on **both** weighted projections, covering their **1570 type/row-pair occurrences**. A deliberately altered group-tensor entry was detected by the weighted comparator. Source and corrected-data hashes in the receipt match the independently pinned bytes. Its earlier file mtimes and actual timing appear in the cadence record above; no date or process success is backfilled.

## 3. Exact limits and relationship to the full identity

This diagnostic supplies an independent per-type versus grouped **implementation arrangement** for the pinned physical Gram coefficients, subject to the shared owner row rules/local maps, source data, Python/NumPy runtime and checked modular arithmetic. It neither recomputes every source-word coefficient nor checks the equality/objective terms or multiplier PSD. A one-prime/two-projection match cannot imply the corrected rational orbit identity.

The separately executed full exact 4675-orbit FLINT-integer check and the independent modular-CRT height-bound proof are described in `frontier-20261028-d4-source-dependency-closure-v2.md`, SHA256 `124bd68bf23b52fe5b5b6db4173851b50f075c293d537dbb8fea7ed83680392b`. The separately written owner-local literal map closure is `frontier-20261028-d4-owner-local-map-closure-v1.md`, SHA256 `24e9a465d057d92960f1211a9ddcd833ee67ca2aae120ef1b80cecee3bba79c7`.

No parent adoption, f62 retrospective scope extension, formal/kernel or independent-human/model-family review, physical distillability implication, all-d proof, novelty or q3 counterexample is claimed. Historical held outcomes are not premises.
