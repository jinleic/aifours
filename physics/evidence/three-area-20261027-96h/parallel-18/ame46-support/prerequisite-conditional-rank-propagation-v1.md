# S1 continuation: conditional rank propagates through the actual AME array

Owner **PhysicsAME46-2**. Native prewrite observation **`Tue Oct 27 15:27:10 PDT 2026`**, not exact file-write/completion/runtime. **WRITTEN author candidate, UNREVIEWED/UNADOPTED**, not novelty or unaffected-cognition certification. No old rank/support family, source/guide, numerical catalogue, scientific execution, selected tensor/rank profile or graph enumeration. The proof is all-variable from the supplied original definitions and elementary positivity/counting shown below.

## 1. Full physical scope

Fix ANY normalized arbitrary-complex AME(4,6) tensor and ANY physical product basis. Put `d=6`, `N=d^2`, `M_ab=(d psi_abkl)_(k,l)`, `P_ab=M_ab M_ab^*`, `r_ab=rank(M_ab)`, and `R=sum r_ab`. Let `r_max=max r_ab`. Every block has Frobenius norm one, hence positive rank. The actual AC/BC marginals give

`sum_b P_ab=I` for every a; `sum_a P_ab=I` for every b.                                   (R1)

The other original marginals remain part of eligibility; no independent matrix-array relaxation is declared sufficient. Conditional Schmidt ranks are invariant under remaining physical C/D basis changes, but not generally under A/B changes. Every AB basis is still quantified.

Let E be the set of indices whose ACTUAL conditional rank exceeds one. In this packet E is an index set, NOT the total linear entropy used in earlier packets. Write `m_a=#{b:(a,b) in E}`, `n_b=#{a:(a,b) in E}`.

## 2. Rank-capacity theorem

For EVERY (a,b) in E,

`r_ab <= min(m_a,n_b)`.                                                               (R2)

In particular no row or column contains exactly one higher-rank conditional block. More strongly,

`R >= N + 4(r_max-1)`.                                                               (R3)

This holds for ALL rank profiles at once, not a chosen rank stratum. The rank-one case gives R=N and is included.

### Complete positivity proof of (R2)

Fix one row. Each of its rank-one blocks has P equal to a unit-vector projector because tr P=1. Their sum is at most I by positivity of the remaining blocks and (R1). For any one such unit vector u, its expectation of that sum is

`1 + sum_(other rank-one vectors v) |<u,v>|^2 <=1`.

Thus all rank-one vectors in the row are pairwise orthogonal. If there are d-m_a of them, their sum is an orthogonal projection, and the remaining m_a positive matrices sum to its complementary projection of rank m_a. Every one of those positive matrices has range inside this residual subspace: on the projection's kernel, their nonnegative expectations sum to zero, so each vanishes there. Hence its rank is at most m_a. This proves the row bound. The column identity gives the identical bound by n_b.

No coordinate/rank is discarded, no individual Schmidt basis is chosen and no arbitrary residual subspace is substituted for the actual matrices. If m_a=0 there is no higher-rank row block to bound; if m_a=1, (R2) contradicts its rank being above one. All degeneracies and phases are allowed.

### Complete incidence proof of (R3)

If r_max=1, every rank is one and (R3) is equality. Otherwise choose an ARBITRARY index realizing some rank r>1; the following statement holds for EVERY such choice, not a selected input test. Let its row contain m indices of E and its column contain n. Equation (R2) gives m,n>=r.

Their row/column union already contains m+n-1 indices of E. Each of the other m-1 columns met by that row must have a further E index outside the row, since no column can contain just one E index. These further indices lie outside the chosen column too and are distinct. Likewise each of the other n-1 rows met by the chosen column requires a further E index outside both. Therefore

`|E| >= m+n-1+max(m-1,n-1) >= 3r-2`.

Every E index contributes at least one to R-N, and the chosen rank-r index contributes r-1. Consequently

`R-N=sum_(i in E)(r_i-1) >= (r-1)+(|E|-1) >= 4(r-1)`.

Taking r=r_max proves (R3). This is a uniform finite incidence inequality, not an executed enumeration or an assumption of a special support pattern.

## 3. Coupling with common-basis incompatibility

Let G be the ACTUAL two-Gram noncommutation graph from the preceding packets: edge i,j iff `[M_i M_i^*,M_j M_j^*]` or `[M_i^*M_i,M_j^*M_j]` is nonzero. The same-tensor four crossed marginal identities prove

`G nonempty => S>=R+4`

in EVERY common C/D basis, by the complete minimum-cover argument in `prerequisite-commutator-four-gap-v1.md`. Combining with R3 gives

`S >= N+4(r_max-1)` always,

`S >= N+4(r_max-1)+4` if G is nonempty.                                                (R4)

No graph nonemptiness is assumed globally. This gives an actual coherent rank-to-support requirement and an extra common-basis requirement, while retaining the commuting branch. It does not replace eligibility by the ranks or the graph.

## 4. A genuine basis-minimum gap, carefully distinguished from exact-support no-go

For the fixed tensor and AB basis, let s_CD be the minimum support over the remaining physical C/D bases. Then

` s_CD=d^2  OR  s_CD>=d^2+4 `.                                                         (R5)

Proof covers ALL cases:

- If r_max>1, R3 gives R>=N+4, so s_CD>=N+4 independently of commutation.
- If r_max=1 and G is nonempty, the four-unit theorem gives s_CD>=N+4.
- If r_max=1 and G is empty, every conditional positive spectrum is simple. The complete commuting-endpoint proof supplies ONE common physical C/D basis with each M_ab supported on one entry, so s_CD=N.

That endpoint is equivalent to actual orthogonal Latin pair-array data, with all three flattenings and six marginals proved in the prior endpoint packet. No order6 existence/nonexistence theorem is imported here.

Therefore, IF the original eligible class is nonempty, its global minimum over ALL states and physical product bases is either d^2 or at least d^2+4. Nonemptiness is not supplied by an abstract rank profile. This is a statement about the MINIMUM: I do NOT claim that an arbitrary basis's exact support in the intervening range is excluded merely by R5. A support-changing basis is used only as a proved endpoint construction, not WLOG in a fixed-support no-go.

## 5. Exact remaining gap and caller boundaries

Forward caller: ANY original AME tensor in ANY AB basis yields the actual ranks, positivity sums and possible commutators. Equations R2–R4 constrain the support in every C/D basis. R5 describes the partial minimum with every degenerate/commuting alternative retained.

Converse boundary: abstract rank capacities, graph data or the dichotomy do not construct one physical tensor. An attaining witness still needs a literal coefficient array with all three actual flattenings unitary. Even an admissible pair-array endpoint must be SUPPLIED; none is asserted to exist or not exist at order6. For larger support, all complex amplitudes and global phase cancellations remain unpaid by these necessary bounds alone.

An actual improvement over an independently established baseline would require a uniformly strong original-object rank/noncommutation statement, or an exact witness. The generic rank/sparsity and four-unit bounds do not themselves identify such a baseline or clear historical numerical/assurance unions. No numerical48..60 update, actual48, noexact50 or lower51 is inferred. The original minimum and actual lower/upper witness remain OPEN.

The next admitted question is whether the original conditions force stronger rank/noncommutation in the commuting positive-degenerate branch or constrain its compatibility across the other two choices of conditioning pair. Such a result must be all-variable; no independent rank profile or preferred conditioning basis can be promoted into the original target.

All source/proof/method/public-status STOP outside S1 and all HOLD/ZERO/exposure/process findings persist. N4 UNKNOWN/incomplete, historical child exit UNESTABLISHED; auxiliary214 STOP. Named imports are positivity, unit-projector orthogonality, rank dimension and the explicit incidence argument; the common-basis/four-gap inputs are prior WRITTEN author candidates, not parent-adopted statements. Parent complete reads and frozen reviews, source equivalence, formal/kernel/human/executable/configured-family and novelty gates remain outstanding. No scientific execution or new GO.
