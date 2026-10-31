# S1 continuation: exact common-basis resolution and the rank-one commuting endpoint

Owner **PhysicsAME46-2**. Native prewrite observation **`Tue Oct 27 15:23:22 PDT 2026`**, not exact write/completion/runtime. **WRITTEN candidate only, UNREVIEWED/UNADOPTED**, not novelty or clean-cognition certification. Inputs: the exact original-model packet and the elementary spectral/rank facts proved below. No old source/proof/guide, scientific execution, selected tensor/spectrum or source search.

## 1. Original quantifiers and exact remaining basis problem

Fix ANY normalized arbitrary-complex AME(4,6) tensor and ANY physical AB product basis. Let `d=6`, `M_ab=(d psi_abkl)_(k,l)`, `P_i=M_i M_i^*`, `Q_i=M_i^*M_i`, `r_i=rank(M_i)` and `R=sum_i r_i`, where i runs over ALL (a,b). Define G by actual noncommutation of either Gram family, as in the preceding packets.

Let `s_CD` be the minimum ACTUAL coefficient support over the remaining common physical C and D bases, holding this tensor/AB basis fixed. This partial optimization is an intermediate quantity, NOT a replacement for the original minimum over all states/all four bases. Every original state/AB basis is included in the theorems below; positive-spectrum simplicity is an explicit conditional branch, never a generic WLOG.

## 2. Exact common-basis criterion when positive spectra are simple

Assume every M_i has DISTINCT positive singular-value squares; its zero singular value may have arbitrary multiplicity. Then

`G empty <=> s_CD=R`.

If G is nonempty, the preceding all-marginal theorem gives `s_CD>=R+4`, without any simplicity assumption. Thus the commuting simple-spectrum branch is resolved exactly for the remaining common local bases; all degenerate-positive-spectrum cases remain included but require the residual compatibility described below.

### Necessity, without simplicity

If some common C/D basis gives support R, every block attains its rank support. As proved directly before, every block then has partial-permutation support, so both Gram families are diagonal in that SAME basis. They pairwise commute, hence G is empty. Since support is integer and there is at least one basis, a least achieved support value exists among its finite possible values; no unproved analytic minimizer is needed.

### Sufficiency, with the stated positive-spectrum hypothesis

If G is empty, all P_i commute pairwise, and all Q_i commute pairwise. Each family consists of Hermitian matrices. It therefore has a simultaneous orthonormal eigenbasis: diagonalize one matrix, note that all commuting matrices preserve its eigenspaces, and recurse on those finite-dimensional spaces and the remaining family. This proof includes arbitrary common degeneracies.

Use these ONE common C basis and ONE common D basis for EVERY conditional matrix. The basic intertwining identity is

`P_i M_i = M_i Q_i`.

Writing the diagonal entries as p_i(k), q_i(l), it gives

`(p_i(k)-q_i(l)) M_i[k,l]=0`.                                                          (E1)

A zero p row is identically zero because its squared row norm is p_i(k); a zero q column is identically zero by its column norm. Therefore nonzero entries can occur only between POSITIVE equal eigenvalues. The two Gram matrices have the same positive spectrum. By the assumed simplicity, each positive eigenvalue occupies exactly one row and one column, forcing exactly one nonzero matrix entry for that eigenvalue. There are r_i such eigenvalues, so every M_i has EXACTLY r_i entries in these SAME bases. Total support is R, proving sufficiency.

No matrix is independently diagonalized with its own incompatible left/right bases, and no support-changing normal form is imposed at the start. A common physical basis is the proved conclusion of a fully stated sufficient condition. The actual tensor stays AME under those local basis changes.

## 3. Positive degeneracies: exact missing compatibility, not omission

Without simplicity, the same common Gram eigenbases still give (E1). For each positive eigenvalue lambda of a particular block, its allowed row and column eigenspaces have equal dimension. On them the actual block is `sqrt(lambda)` times a UNITARY map, since both Grams are lambda times identity. Those internal unitary maps are NOT determined by the Gram eigenvalues or their commutativity.

The remaining freedom in the COMMON Gram eigenbases is only within their JOINT spectral subspaces (and overall coordinate permutations), not independent freedom for each block's repeated eigenvalue. Simultaneous rank-support attainability would require compatible choices of these common bases making every internal map partial-permutation. No such compatibility theorem or converse from Gram commutation alone is asserted. The full degenerate case remains a real branch of the original arbitrary-complex problem; it cannot be discarded as nongeneric at a support minimum.

## 4. The full rank-one commuting endpoint is exactly classical pair-array data

Each M_i is nonzero of norm one. Therefore `R=d^2` iff every conditional rank is one. Positive-spectrum simplicity then holds automatically, with sole positive eigenvalue one. Consequently

`R=d^2 and G empty <=> a common C/D basis gives actual support d^2`.                     (E2)

There is a complete actual-object description of this endpoint. In the common bases, each block is

`M_ab = z_ab E_(c(a,b), e(a,b))`, with `|z_ab|=1`.

The original AC/BC row/column sums of P imply that c(a,b) is a permutation in b for each a and a permutation in a for each b. The AD/BD sums give the same two permutation conditions for e(a,b). Full AB orthogonality says no two indices have the same ordered output pair `(c(a,b),e(a,b))`, so the map from (a,b) to (c,e) is bijective. Thus c and e are two orthogonal Latin arrays, with arbitrary entry phases z. This statement is derived here, not imported from a classical existence/nonexistence source.

### Full converse and all six actual marginals

Suppose TWO actual arrays c,e are supplied, each row and column a permutation, and their ordered pairs are bijective. With ANY unit phases z define ONE tensor

`T_abkl=z_ab delta_(k,c(a,b)) delta_(l,e(a,b))`, `psi=T/d`.

- AB|CD flattening has exactly one unit-modulus entry in each row and column by the ordered-pair bijection.
- AC|BD: row (a,k) determines a unique b by the c-row permutation, then l=e(a,b). Conversely column (b,l) determines a unique a by the e-column permutation, then k=c(a,b).
- AD|BC: row (a,l) determines a unique b by the e-row permutation, then k=c(a,b). Conversely column (b,k) determines a unique a by the c-column permutation, then l=e(a,b).

All THREE physical flattenings are therefore monomial UNITARIES for this SAME T. Normalizing by d gives a normalized AME tensor; each flattening and its complementary cut prove all SIX marginals. It has exactly d^2 coefficients, all conditional ranks one and G empty. No pair of arrays is selected, enumerated or claimed to exist at the original dimension.

Conversely, ANY original AME tensor attaining support d^2 has one nonzero entry in every AB block, so the same argument recovers these arrays and phases. Thus existence of a minimal-support d^2 AME tensor is equivalent to existence of such pair-array data, at the supplied model definition.

## 5. Exact import boundary and original target

No existence OR nonexistence theorem for orthogonal Latin arrays of order6 is supplied in the allowed packet. I do NOT invoke a remembered theorem, numerical catalogue, public-status source or historical lower-bound proof to decide this endpoint. Its absence is a specific unprovided combinatorial premise, not proof the endpoint exists or that it is the only remaining case. The full commuting positive-degenerate branch and noncommuting all-rank branch remain part of the ORIGINAL problem.

The new proved content is exact common-basis attainability in the explicit simple-positive-spectrum branch, the precise degenerate-unitary compatibility gap, and a necessary/sufficient actual-object endpoint description with every flattening paid. It does not improve the actual lower bound or upper witness, establish original-minimum attainment, or replace the target by this endpoint classification.

To exploit the four-unit bound globally one still needs a uniform rank/noncommutation statement at every original tensor/AB basis. To exploit purity one needs a uniform upper bound on total conditional purity. Neither follows merely from the spectral interface or the existence of local phase directions. No numerical48..60, actual48, noexact50 or lower51 claim is made; I48/J49/J50 are not inputs.

All source/proof/method/public-status STOP outside S1, every HOLD/ZERO/exposure/process finding, N4 UNKNOWN/incomplete with historical exit UNESTABLISHED and auxiliary214 STOP persist. No scientific execution, external source or new GO. Parent full source reads/frozen review and all formal/kernel/human/executable/configured-family/novelty gates remain outstanding.
