# S1 continuation: all-marginal row/column coupling forces a four-unit support gap

Owner **PhysicsAME46-2**. Native prewrite observation **`Tue Oct 27 15:21:37 PDT 2026`**, not exact creation/completion/runtime. **WRITTEN author candidate, UNREVIEWED/UNADOPTED.** This proof branch was developed after the15:14:33 common-basis bound, interrupted BEFORE persistence by priority w23, and resumed after returning that review at the15:21:00 metadata observation/subsequent return message. The Boolean review is NOT an input. No old proof/guide, scientific program, selected tensor, graph enumeration or external source is used.

## 1. Original all-variable caller and full same-tensor identities

For EVERY normalized arbitrary-complex AME(4,6) state in EVERY physical product basis, put `d=6` and `M_ab=(d psi_abkl)_(k,l)`. Let

`P_ab=M_ab M_ab^*`, `Q_ab=M_ab^* M_ab`, `r_ab=rank(M_ab)`, `R=sum_(a,b) r_ab`.

All indices run over the FULL local alphabets, all six marginals belong to this ONE tensor, and no rank, support, symmetry or phase class is selected. The actual pair marginals give BOTH row AND column matrix sums:

`sum_b P_ab=I` for each a, from AC;

`sum_a P_ab=I` for each b, from BC;

`sum_b Q_ab=I` for each a, from AD;

`sum_a Q_ab=I` for each b, from BD.                                                       (F1)

The directly indexed D reductions are transposes of the Q sums; identity invariance under transpose makes (F1) equivalent. AB gives Frobenius norm one/nonzero for every block; all eligibility and normalization requirements are retained.

Define G on ALL d^2 conditional indices, with an edge i,j iff `[P_i,P_j]` or `[Q_i,Q_j]` is nonzero. The same common C/D basis is used throughout. The graph and ranks are invariant under subsequent physical C/D basis changes, for fixed AB basis, by simultaneous unitary conjugation.

## 2. Universal theorem

For EVERY original eligible tensor and AB basis:

- EVERY nonempty minimum vertex cover of G occupies either zero or at least TWO indices in each row, and either zero or at least TWO in each column.
- Consequently, if G has ANY edge, its minimum cover size satisfies `tau(G)>=4`.
- Therefore for EVERY physical C/D basis the actual support satisfies

`G nonempty => S >= R+4`.                                                              (F2)

If G is empty, the universally valid bound remains `S>=R`; no nonemptiness premise is silently imposed. This is a genuine strict support-to-coupling delta beyond independent conditional ranks, not an actual numerical minimum improvement.

## 3. Full proof of the cover constraint

Let B be a minimum-cardinality vertex cover, and U its complement. U is an independent set, so every P_i with i in U commutes with every P_j with j in U, and the same holds for Q. This concerns both complete matrix families, not just their spectra or traces.

Suppose some row contains EXACTLY one vertex v of B. Every other vertex i in that row is in U. Equation (F1) gives

`P_v=I-sum_(other i in row) P_i`, `Q_v=I-sum_(other i in row) Q_i`.

For EVERY j in U, all summands commute with P_j or Q_j respectively. Thus `[P_v,P_j]=[Q_v,Q_j]=0`. Vertex v has no edge to U. Removing v from B therefore still covers all edges: an edge from v to another B vertex remains covered at its other endpoint, and there is no edge from v to U. This contradicts minimum cardinality. Hence no row of B has exactly one vertex. The identical argument using the COLUMN identities in (F1) excludes singleton columns.

If B is nonempty, choose a row meeting it. That row has at least two B vertices in distinct columns. Each of those columns has at least one further B vertex outside that row. Those two further vertices are distinct, proving |B|>=4. If G has an edge, every cover is nonempty, so tau(G)>=4.

Finally the previously proved common-basis bound is paid directly: write t_i for each block's actual nonzero count in the chosen C/D basis. Rank gives t_i>=r_i. Equality forces its nonzero entries into distinct rows/columns, hence both its Gram matrices diagonal in that SAME basis. Consequently the bad set `{i:t_i>r_i}` covers G. Every bad block contributes at least one integer to `S-R=sum_i(t_i-r_i)`, so `S-R>=tau(G)>=4`. This reproduces the operative bound rather than citing an unreviewed author conclusion as confidence.

## 4. Independent companion consequence: every nonisolated vertex has degree at least four

Fix ANY vertex j and form the vector-space-valued grid

`C_ab=([P_ab,P_j], [Q_ab,Q_j])`.

By (F1), every row sum and every column sum of this grid is zero. Its nonzero positions are EXACTLY the neighbours of j in G. A row or column containing a nonzero position cannot contain just one: that nonzero matrix pair would equal its row/column sum, contradicting zero. If j is nonisolated, choose one nonempty row; it contains at least two nonzero positions, and each of their columns contains a further nonzero position outside the row. Thus j has at least four neighbours.

This is a symbolic all-grid proof, not a small-graph enumeration or selected support case. It neither asserts a particular graph exists nor replaces the stronger cover argument by an unsupported degree-to-cover inference.

## 5. Actual-object callers and exact original-minimum bridge

**Forward caller:** any original eligible tensor and any AB basis supply the ACTUAL P,Q and ranks. ONE proved nonzero commutator suffices for the four-unit bound in EVERY C/D basis. No selected basis is preferred for the original global optimization; the theorem can be applied separately at every AB basis with its newly formed data.

**Converse/eligibility boundary:** graph data, positive matrices or the row/column sums alone do NOT furnish an AME tensor. An actual object still requires ONE four-index coefficient array, normalization and all THREE physical flattenings unitary (hence all six marginals). No converse claiming such a tensor exists for an arbitrary graph or rank sum is made. Nor does a support gap S>=R+4 imply a noncommuting graph; the proved implication is one-way.

For a generic INTEGER candidate lower bound L, a sufficient all-variable proof would establish BOTH:

1. `R>=L-4` for EVERY eligible tensor and AB basis;
2. whenever `R<L`, the actual graph is nonempty.

Then the empty-graph branch has R>=L, while the nonempty branch has S>=R+4>=L. This keeps BOTH branches and all ranks, rather than replacing the original target by a noncommuting subclass. Neither needed uniform statement is proved here for an improving L; no numerical ledger or old lower-bound import is silently used.

The next genuine unresolved endpoint is the commuting-graph branch, especially its minimum conditional-rank endpoint. Its compatibility with all six original marginals must be analyzed, not assumed impossible because the four-unit theorem holds elsewhere.

## 6. Scope and controls

The new step is the rigorous row/column matrix-sum coupling: independent Schmidt-rank lower bounds plus ANY noncommutation pay a universal four-unit support delta. All four crossed marginal identities, common physical local spaces and full matrix commutators are essential. No officer/thin/support-specific graph or prior numerical catalogue is a premise.

The original exact minimum, actual lower-bound improvement and eligible sub-benchmark witness remain OPEN. This does not establish a uniform noncommuting/rank premise, source equivalence, native acceptance, I48/J49/J50 numerical union or priority. Imports are elementary matrix commutators and the explicitly proved vertex-cover/counting facts; no new source theorem.

All STOP/HOLD/ZERO and author/reviewer/parent exposure/process findings persist. N4 UNKNOWN/incomplete, historical child exit UNESTABLISHED, auxiliary214 STOP. No scientific interpreter/calculator/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control/boundary probe, nested agent/modelCLI/paidAPI/Git/delete/contact/publication/infrastructure action. Parent complete reads and frozen full-scope review remain outstanding; WRITTEN is not stronger assurance or novelty certification.
