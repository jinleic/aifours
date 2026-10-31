# S1 continuation: conditional-rank bounds plus common-basis incompatibility

Owner **PhysicsAME46-2**. Actual native prewrite observation **`Tue Oct 27 15:14:33 PDT 2026`**, not exact write/completion/runtime. **WRITTEN candidate, UNREVIEWED/UNADOPTED**, not novelty-cleared or independently reconstructed. Only the supplied original definitions and elementary matrix/graph facts proved here are used. No old proof/guide, external source, scientific execution, selected tensor, commutator test or graph enumeration.

## 1. Full original scope and invariant data

Fix ANY normalized arbitrary-complex AME(4,6) tensor and ANY physical local orthonormal bases. Put `d=6` and `M_ab=(d psi_abkl)_(k,l)`. The SAME tensor and all SIX physical marginals remain required; no isolated conditional family is substituted for eligibility. AB maximal mixing gives each M_ab Frobenius norm one and nonzero.

Use index i=(a,b), and define

`r_i=rank(M_i)`, `P_i=M_i M_i^*`, `Q_i=M_i^* M_i`, `R=sum_i r_i`.

Build a simple graph G on the full d^2 conditional indices: distinct i,j are adjacent precisely when AT LEAST ONE actual commutator is nonzero,

`[P_i,P_j] !=0` OR `[Q_i,Q_j] !=0`.                                                     (C1)

No entries or phases are discarded. For a graph let tau(G) be its minimum vertex-cover size and nu(G) its maximum matching size. These are abstract finite parameters, not computed instances.

For a FIXED AB basis, changing the physical C and D bases conjugates all P_i simultaneously by the same C-space unitary and all Q_i simultaneously by the same D-space unitary (or its conjugate under the explicit tensor coefficient convention). R, adjacency, tau and nu are therefore invariant under those remaining physical basis changes. An A/B basis change can mix the conditional matrices and changes the data: no invariance or WLOG on A/B is claimed.

## 2. Universal support-to-common-basis theorem

For EVERY such original tensor/basis, its actual support S satisfies

`S >= R + tau(G) >= R + nu(G)`.                                                        (C2)

More directly, EVERY supplied matching of m pairwise vertex-disjoint noncommuting pairs certifies `S>=R+m` in EVERY physical C/D basis for that same tensor and AB basis. This is a strict extra support requirement when a nonempty matching is proved. No actual graph, rank profile or numerical improvement is asserted here.

### Complete proof

For a matrix M with t nonzero entries and rank r, t>=r. If t=r, all nonzero entries must occupy DISTINCT rows and DISTINCT columns: the number of nonzero rows and the number of nonzero columns each bounds the rank and is at most t. Equality r=t forces both counts to equal t. Thus M is a partial-permutation support matrix (with arbitrary nonzero complex magnitudes/phases).

In that SAME physical basis, both `MM^*` and `M^*M` are diagonal. This conclusion requires no chosen singular basis for M and no equality of its singular values. It is a consequence of its actual minimal support, not an independent diagonalization choice.

Call a conditional index good when its ACTUAL nonzero count t_i equals r_i, and bad otherwise. If two indices are both good, both corresponding P matrices and both corresponding Q matrices are diagonal in the common C and D bases. They commute, so the two indices are not adjacent in G. Consequently the bad set B meets every edge: it is a vertex cover. Since each bad matrix has integer `t_i-r_i>=1`,

`S-R=sum_i(t_i-r_i)>=|B|>=tau(G)`.

Every vertex cover meets each edge of any matching, and disjoint matching edges require distinct cover vertices. Hence tau(G)>=nu(G), proving (C2) and the supplied-matching certificate. No matrix is actually transformed, no support-preserving WLOG is assumed and no graph algorithm/enumeration is executed.

## 3. Relation to the conditional-purity mechanism

For each trace-one Q_i, the spectral Cauchy-Schwarz inequality gives

`r_i >= 1/tr(Q_i^2)`.

Thus the earlier purity lower bound is the scalar relaxation

`S>=R>=sum_i 1/tr(Q_i^2)>=(d^2)^2/sum_i tr(Q_i^2)`.

Equation (C2) adds a DIFFERENT genuinely joint obstruction: conditional matrices cannot all attain their individual rank supports in one physical C/D basis when their Gram data conflict. Independent Schmidt decompositions choose incompatible local bases and cannot pay that extra common-basis requirement. The graph bound remains meaningful with all ranks, phases and degenerate eigenvalues; it does not select a low-support family.

No converse from G having no edges is established. Pairwise commuting Gram matrices alone do not supply an actual common partial-permutation representation, and degenerate singular subspaces retain matrix information absent from the Gram spectra. To claim attainability one must supply the SAME actual C/D basis and verify all M_i there, not merely list independent Schmidt bases or graph parameters.

## 4. Forward, sufficient-certificate and eligibility callers

**Forward:** input is an arbitrary original eligible tensor in an arbitrary AB basis. Its actual ranks and nonzero commutators define the graph. Bound (C2) holds for every remaining physical C/D basis. It also holds, with newly formed data, for every other AB basis. The original global quantifiers are not narrowed.

**Lower-bound certificate caller:** an exact supplied physical tensor together with proved conditional ranks and a supplied matching whose full matrix commutators are nonzero gives the stated conditional support bound. Nonzero trace of a proposed expression is not silently substituted for a nonzero commutator. A full vertex-cover lower-bound proof can strengthen the matching estimate without choosing a state or running a solver.

**Eligibility converse:** arbitrary ranks, purities, Gram matrices or a graph are NOT a Boolean-like inverse/physical-tensor certificate. To register an actual AME witness, one must supply ONE four-index T, normalized psi=T/d and all THREE physical flattenings of T unitary. Those square-unitary identities prove the paired marginals and their complements all equal I/d^2. The graph and ranks must then be formed from T's actual M_ab. Without this input, (C2) is an all-variable necessary theorem, not an existence assertion. No such new tensor is supplied here.

If exact actual matrices happen to attain `S=R`, the proof forces G empty; if G contains any edge, S=R is impossible in EVERY C/D basis. I do not assert the reverse or any physical example realizing equality. Zero entries, repeated singular values, rank deficiency and all phases are included. No coordinate division, genericity assumption or omitted zero block is present; zero blocks are excluded only by the actual AB normalization.

## 5. Original minimum: exact uniform premise still required

A proved uniform bound `R+tau(G)>=L` for EVERY eligible tensor and EVERY AB basis would, by (C2), give the original all-product-basis lower bound S>=L. One may instead supply a universal matching/rank argument with the same quantifiers. A useful rank/matching in one preferred AB basis does NOT establish the original minimum, even though C/D basis optimization has been handled exactly.

Thus this is a necessary support-to-coupling mechanism with a possible strict delta beyond separate rank bounds, not a numerical-ledger improvement. The remaining unpaid step is a uniformly strong all-AME/all-AB rank-and-common-Gram incompatibility theorem, or a corresponding actual witness. No old numerical catalogue, I48/J49/J50 union, fixed rank stratum or protected support representation is used to assert it.

The most useful next definition-first question is whether full AME constraints force any such noncommuting pair/rank total at the relevant original quantifiers, rather than assuming the graph is nonempty. The completely commuting/product-conditional endpoint must be kept as a real unexcluded mathematical case unless its impossibility or attainment is proved from admissible inputs.

Named imports: rank bounded by nonzero row/column count; partial-permutation Gram diagonality; invariance of commutators under common unitary conjugation; elementary vertex cover/matching definitions and the explicit cover proof; positive-matrix spectral Cauchy-Schwarz. No external theorem or computation. All original STOP/HOLD/ZERO, author/reviewer/parent exposure/process history, N4 UNKNOWN with historical exit UNESTABLISHED and auxiliary214 STOP persist. No model/book-equivalence, configured-family/human/formal/kernel/executable or novelty acceptance follows.
