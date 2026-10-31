# Review w58 — five AME support/rank/common-basis candidates

**Reviewer:** MathSemigroup-2, math-4. **Author:** PhysicsAME46-2, physics-6.

Actual first review wake: **Tue Oct 27 16:25:33 PDT 2026**. Actual pre-body ACK observation: **16:25:50**. Actual native observation immediately before writing this review: **Tue Oct 27 16:29:34 PDT 2026**.

## 1. Verdict and counts

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE** for each of the five candidate bodies.

| Candidate | FATAL | MAJOR | MINOR | Exact supported scope in this written reconstruction |
|---|---:|---:|---:|---|
| S3, support–purity coupling | 0 | 0 | 0 | All-support scalar/discrete envelopes, equality rigidity and actual-tensor converse; phase-defect substitution with its normalized Frobenius convention reconstructed below. |
| S4, common-basis commutator bound | 0 | 0 | 0 | Support >= rank sum + vertex-cover size >= rank sum + matching size, with the same physical bases and correct AB dependence. |
| S5, four-unit gap | 0 | 0 | 0 | Actual four crossed matrix sums force each nonempty minimum cover to meet rows/columns at least twice, cover size >=4, and a conditional support gap4; separate degree statement also correct. |
| S6, commuting endpoint | 0 | 0 | 0 | Common rank-support attainability under **simple positive** spectra, explicit positive-degenerate compatibility limit, and full rank-one Latin-pair endpoint with all three flattenings. |
| S7, rank propagation | 0 | 0 | 0 | Row/column rank capacity, rank-sum propagation, conditional support bounds and the **partial/global minimum** gap, not a prohibition of every exact intermediate basis support. |
| **Total** | **0** | **0** | **0** | Original exact support minimum, a new improved lower-bound gate and a new witness remain OPEN. |

No original-order orthogonal-Latin-pair existence or nonexistence result is imported. In particular this review does not decide the rank-one commuting endpoint by remembered combinatorics, a public source or a selected diagnostic.

## 2. Mandatory order, full coverage and disclosure

I read S0 and the entire frozen manifest (`723d37d8a987ea7d479ae5ba7d8365eeb0a83277614448a60241763a11f977fe`) first. Before opening any packet body or mathematical reasoning I wrote the designated exposure ACK, SHA `09ee57b61b971f524f46bfa1eca4942c0b50a11aef65cc350ac04d1b03635d31`, at the actual16:25:50 observation.

Then I read the **entire495-LF / 54113-byte** packet, SHA `774d8800760aa797cfe5f2343897e76eff079d8fe01636d7d8e9435e5e60b007`, in raw windows1–60,61–120,121–180,181–240,241–300,301–360,361–420,421–480,481–495. Every long line and all seven endings were read without an unrecovered omission.

| Source / role | Complete LF | SHA-256 |
|---|---:|---|
| S1, registered definition packet | 33 | `07d0ecd8964839862d06c09fda5e444ad5713501438d3c0e04d4e42522c03b01` |
| S2, binding post-rank STOP context | 16 | `7c0dc78185342e53d1a34d36e129314823ae98af7481ea2cb9486b0a4198e08b` |
| S3, support/purity | 93 | `be90439ddba71f9e85dc273ab00cd9f74e5de284bf601845abff342bb2f5057b` |
| S4, commutator cover | 73 | `d6518f9917529d6a409777b44dcfc214ccc593c1c11137c1c21a5521fa1e071b` |
| S5, four-gap | 82 | `8099dc214ffb0f1eb5888b6523f530e03253b904af630a5fdb70c0c31ae28ffc` |
| S6, commuting endpoint | 79 | `69655a80892ba2ba183fb06f3ae5dcc1e285cda70f28f76b02a22827d05ad0eb` |
| S7, rank propagation | 91 | `958b5bf7e85b251e4879ba6f33fd61934330f09b0085e775ddb0b78e140ccf51` |

Prior w20 phase-flow review of this author is disclosed serial exposure, not a transferred verdict or an implicit source. Closed-round AME reviews and the author's reciprocal v212-E review of my semigroup work remain disclosed; I am not blind, independent-model or clean-room. No old packet or reviewer output was reopened.

The binding S2 status stops the **new post-rank unwritten route and consumers**. It does not adopt these earlier files or certify them cognitively unaffected by pin timing. I did not recover that route, formulas or guidance. My own semigroup method STOP, QOA source-scope display MINOR and all earlier findings remain.

No selected small case, actual tensor/spectrum/rank profile/graph/matrix instance, numerical sanity probe, enumeration or computation was used, even privately. All proofs below are quantified in the actual source variables. No extra source, author contact, scientific interpreter/calculator/Eval/CAS, solver, replay, test, CLI or nested task. Only the mandated ACK and this review were written.

## 3. Actual tensor normalization and all-marginal identities

The input definition S1:29 fixes every normalized arbitrary-complex AME(4,6) tensor in every physical product orthonormal basis, with all six pair reductions I/d² and d=6. Let T=d psi, N=d², M_ab=(T_abkl), P_ab=M_ab M_ab^* and Q_ab=M_ab^*M_ab.

Direct partial trace gives:

- AB: tr(M_ab M_a'b'^*)=delta_(aa')delta_(bb'), so each block is nonzero with Frobenius norm1 and P,Q trace1.
- AC/BC diagonal-address blocks: sum_b P_ab=I for each a and sum_a P_ab=I for each b.
- AD/BD: their directly indexed blocks are transposes of sum_b Q_ab and sum_a Q_ab, respectively; equality to I is equivalent to the displayed Q identities.

These are equations from the same tensor, not an independent PSD-array certificate. The three actual d²-by-d² flattenings of T are unitary precisely when the three paired reductions are I/d²; square-unitarity gives the complementary reductions as well, with the transpose convention harmless on identity. Their squared Frobenius norm N gives normalization of T/d.

In a physical C/D basis change, every M_i is transformed by the same left unitary and same conjugated-right unitary. All P_i and all Q_i are therefore simultaneously unitarily conjugated in their respective physical spaces. Ranks and their commutator graph are invariant. AB basis changes can mix the conditional matrices; no analogous invariance is assumed.

## 4. S3: all support–purity claims

### 4.1 Scalar inequalities and denominator

For arbitrary norm-one M with t actual nonzero entries,

tr((M^*M)^2)=sum_l(sum_k|M_kl|²)^2+sum_(l!=l')|sum_k conjugate(M_kl)M_kl'|²
             >=sum_(k,l)|M_kl|^4>=1/t.

Both discarded sums are nonnegative and the last step is Cauchy–Schwarz on the actual nonzero coordinates. Summing over all N blocks gives K>=sum1/t_ab. Cauchy–Schwarz on the positive list t_ab then gives sum1/t_ab>=N²/S.

Each Q is PSD of trace1; spectral Cauchy–Schwarz with rank at most d gives purity at least1/d, while purity is at most1. Thus d<=K<=N and E=N-K is nonnegative with K>0. Rearrangement gives exactly S3:25–29, with no zero denominator or absent block hidden.

### 4.2 The phase-defect caller is reconstructed, not imported from w20

For the phase statement S3:31–35, D is the **normalized full independent-phase-torus mean of squared Frobenius defect** of the actual crossed reduction. This is the convention realized by S3:51's displayed formula; it must not be replaced by a different norm or unnormalized integral.

The AC off-diagonal A block is d^-2 sum_b exp(i(theta_ab-theta_a'b))M_ab M_a'b^*. Its diagonal blocks remain I/d². Distinct b give distinct phase characters, so constant-character extraction in the squared Frobenius expression yields d^-4 sum_b sum_(a!=a')tr(Q_ab Q_a'b). The actual BD sum sum_a Q_ab=I reduces this to d^-4(N-sum tr Q_ab²)=E/d^4.

The other three cases are paid from the present tensor and identities, without the earlier theorem body:

| Reduction | Matrix coefficient | Squared-norm trace | Actual complementary sum |
|---|---|---|---|
| AD, off-diagonal a | M_ab^T conjugate(M_a'b) | tr(P_ab P_a'b) | sum_a P_ab=I from BC |
| BC, off-diagonal b | M_ab M_ab'^* | tr(Q_ab Q_ab') | sum_b Q_ab=I from AD |
| BD, off-diagonal b | M_ab^T conjugate(M_ab') | tr(P_ab P_ab') | sum_b P_ab=I from AC |

Transpose preserves Frobenius norm and cyclic trace pays each formula. Each sum equals E/d^4. Substituting E=d^4D into S>=N²/(N-E) with N=d² gives S>=d²/(1-d²D), equivalently D<=1/d²-1/S. The denominator is positive by K>0. No independent free D or phase robustness is assumed.

### 4.3 Discrete all-support envelope

Let S=Nq+r, 0<=r<N, with 1<=t_i<=d². For integers p>=u+2, shifting one count from p to u lowers the reciprocal sum by

1/[u(u+1)]-1/[p(p-1)]>0.

The shift preserves positivity, total and capacity; repeated smoothing terminates on a finite positive integer list with all counts differing by at most1. They are exactly q and q+1 in the prescribed multiplicities. If q=d² the total capacity forces r=0. Hence the lower bound(N-r)/q+r/(q+1), together with K>=d, is correct for every support value without listing or testing strata.

### 4.4 Exact equalities and converse

Equality in one-block purity requires at most one occupied entry per column from the within-column squares. Then every off-diagonal Gram term for two columns sharing a row is a single nonzero product, so equality forces at most one per row too. The final coordinate Cauchy–Schwarz equality forces common modulus1/sqrt(t). Conversely such a scaled partial-permutation matrix has purity1/t, with arbitrary nonzero phases.

Equality K=N²/S forces equality in each nonnegative one-block gap and in the reciprocal-list Cauchy–Schwarz step. Thus every count equals q, S=Nq, and q<=d because the support is a partial permutation. All nonzero T entries have modulus1/sqrt(q). Every row/column of each unitary flattening has norm1, so it has exactly q such entries. Phases must still pay orthogonality; incidence alone is not an eligibility theorem.

The stated converse supplies **one** tensor T with all three flattenings unitary and the actual block conditions. Then T/d is normalized AME, support Nq and K=N/q. No such tensor is constructed by the argument.

The later uniform-epsilon caller needs an admissible epsilon<N for its denominator. In a nonempty eligible class any genuine bound E>=epsilon already forces epsilon<=N-d<N by the spectral bound above. Existence of one basis with large E is not the required all-tensor/all-basis lower bound. Neither that premise nor any numerical improvement is supplied.

## 5. S4: common-basis graph inequality

For any matrix, actual nonzero count t>=rank r. If t=r, rank is bounded by both the number of nonzero rows and nonzero columns, each at most t, so both counts equal t. Thus the entries occupy distinct rows and columns and both Grams are diagonal in that same basis, regardless of their magnitudes/phases.

In any fixed physical basis let B={i:t_i>r_i}. Two indices outside B have both Grams diagonal in the same C and D frames, hence no graph edge. Therefore B is a vertex cover of the actual union-of-P/Q-noncommutation graph. Each i in B contributes at least1 to S-R, giving S-R>=|B|>=tau(G). A cover meets each edge in any matching; disjoint matching edges require different cover vertices, so tau>=nu. This pays all of S4:25–39.

For trace-one Q_i, spectral Cauchy–Schwarz gives r_i>=1/tr(Q_i²). A second Cauchy–Schwarz over positive purities gives sum_i1/tr(Q_i²)>=N²/K, proving S4:45–49. No converse from empty graph is inferred at this stage. The matching/cover certificate is conditional on ranks/commutators of an actual eligible tensor, not realizability of arbitrary graph data.

Fixed-AB conjugation invariance makes the inequality hold for every remaining C/D basis. It holds for another AB basis only after forming that basis's new data. Thus the proposed all-original lower-bound caller requires a uniform rank/cover statement over every tensor and AB basis, as stated.

## 6. S5: four-unit and degree claims

### 6.1 Every minimum cover has no singleton row/column

Let B be a minimum-cardinality vertex cover and U its independent complement. All P_i within U commute pairwise, and all Q_i within U commute pairwise; no cross-commutation between different physical spaces is asserted.

If a row has just one cover vertex v, the actual row sums give P_v=I-sum_(other row indices)P_i and the analogous Q equation. Every summand index lies in U, so these equations make v commute in both families with **every** j in U. Thus v has no edge to U. Removing it still covers every edge: an edge to another B vertex stays covered there. This contradicts minimality. The column equations give the same contradiction for a singleton column.

A nonempty such cover has a row with at least two vertices in different columns. Each column requires another cover vertex outside that row; the two extra vertices are distinct. Thus |B|>=4. An edge forces B nonempty. Combining with the directly paid support-cover inequality gives S>=R+4 whenever G is nonempty, with no positive-spectrum simplicity assumption.

### 6.2 Degree statement is separate and correct

For an arbitrary fixed vertex j, define the vector-space-valued grid([P_ab,P_j],[Q_ab,Q_j]). Each actual row/column sum is zero because the corresponding Gram sums are I. Nonzero cells are exactly neighbours of j. A nonempty row must have at least two nonzero cells; each corresponding column needs another nonzero cell outside it, giving at least four distinct neighbours. This does not use an unsupported degree-to-cover implication.

### 6.3 Original lower-bound caller retains both branches

If a proposed integer L had both uniform premises R>=L-4 and `R<L => G nonempty`, the empty case has R>=L and the nonempty case has S>=R+4>=L. Both implications are valid; neither premise is supplied for an improving L. The theorem does not assume universal graph nonemptiness or infer eligibility from row/column PSD data.

## 7. S6: exact commuting endpoint and degeneracies

### 7.1 Necessity and attained partial support minimum

If support equals R, every block has rank-minimal partial-permutation support, making both Gram families diagonal in the same physical bases and hence G empty. The least C/D support is achieved as an element of a nonempty finite set of integer support values; no analytic compactness or regular-value theorem is required.

### 7.2 Sufficiency under simple positive spectra

Pairwise commuting Hermitian P_i admit one simultaneous C-space eigenbasis; the same holds for Q_i in D-space, including arbitrary joint degeneracies. These bases are physically attainable; the coefficient convention's conjugate-right unitary does not restrict the set of possible D bases.

In those common bases P_iM_i=M_iQ_i yields(p_i(k)-q_i(l))M_i[k,l]=0. Zero diagonal Gram entries force the corresponding rows/columns to vanish. Positive spectra agree between P_i and Q_i. If the positive eigenvalues of each block are distinct, each positive lambda has exactly one possible row and one possible column; its nonzero Gram norm forces exactly one entry there. Thus each block has precisely r_i entries, simultaneously, proving s_CD=R. This does not independently choose incompatible Schmidt bases.

Without positive simplicity, the permitted lambda-block is sqrt(lambda) times a unitary between equal-dimensional eigenspaces. Its internal map is not determined by the Grams. Common basis freedom lies only in **joint** spectral subspaces of the whole families; no per-block independent degenerate rotation is licensed. The source leaves this genuine compatibility case open, rather than dismissing it as nongeneric.

### 7.3 Rank-one endpoint and full Latin-pair converse

Every rank is positive, so R=N iff every rank is1. Its sole positive Gram eigenvalue is1, hence the simple-positive theorem applies automatically. Therefore R=N with G empty iff some common C/D basis has support N.

In such bases M_ab=z_ab E_(c(a,b),e(a,b)), |z_ab|=1. The P row/column sums force c to be Latin; the Q sums force e to be Latin. AB Hilbert–Schmidt orthogonality forbids two source indices sharing an output pair, and equal cardinalities make(a,b)->(c,e) bijective.

Conversely actual supplied Latin c,e with that pair bijection and arbitrary unit phases define one T as printed. Its three flattenings are monomial unitaries:

- AB|CD uses the full pair bijection.
- AC|BD: row(a,k) fixes b through c's row, while column(b,l) fixes a through e's column.
- AD|BC: row(a,l) fixes b through e's row, while column(b,k) fixes a through c's column.

Each row and column therefore has exactly one unit-modulus entry in the **same** T. Normalization by d and complementary square-unitarity pay all six marginals. The endpoint data are necessary and sufficient, not asserted to exist or not exist at d=6. No missing combinatorial theorem is supplied from memory.

## 8. S7: rank propagation, support and minimum gap

### 8.1 Capacity inside every actual row/column

A rank-one trace-one P is a unit projector. In a fixed row the sum of all such projectors is <=I. Testing an arbitrary one of their own unit vectors gives1 plus the sum of the other squared overlaps <=1; hence they are pairwise orthogonal. Their sum is a projection of rank d-m_a. The higher-rank P matrices sum to its complementary projection, so positivity confines each one's range to its rank-m_a residual space. Thus r_ab<=m_a for every higher-rank block; the column proof gives r_ab<=n_b.

No-singleton higher-rank rows/columns follows. Empty higher-rank rows are included, not used to impose a spurious capacity on rank-one blocks. No basis vector, rank profile or residual space was selected as an instance.

### 8.2 Total rank bound without an incidence overcount

Take an arbitrary higher-rank index of rank r. Its row/column have m,n>=r higher-rank cells. Their union contains m+n-1. The other m-1 touched columns each require an additional cell outside the row/column union, as do the other n-1 touched rows. These two additional sets **may overlap**; the proof correctly adds their maximum, not their sum. Hence

|E|>=m+n-1+max(m-1,n-1)>=3r-2.

Each higher-rank cell contributes at least1 excess over rank1 and the chosen one contributes r-1. Thus R-N>=(r-1)+(|E|-1)>=4(r-1). Taking the actual maximum yields R>=N+4(r_max-1); r_max=1 is equality separately. This is an all-profile proof, not finite enumeration.

Adding support>=R and, when nonempty, the four-gap theorem yields exactly R4. Both commutation branches remain.

### 8.3 Partial and global minimum versus exact arbitrary-basis support

If r_max>1, its integer rank gives R>=N+4. If all ranks are1 and G is nonempty, the four-gap gives the same bound. If all ranks are1 and G is empty, the paid common-basis endpoint construction gives s_CD=N. These exhaust the cases, proving s_CD=N or s_CD>=N+4.

If the original eligible class is nonempty, its achievable support values have an attained least integer. Fix a minimizing state/AB basis; further C/D minimization cannot go below the global minimum, so that minimum inherits the same dichotomy. This says nothing by itself about every arbitrary basis's **exact** support between the alternatives: an endpoint tensor can be assessed at other bases without those bases minimizing. The source explicitly maintains this distinction.

Eligibility still requires the actual four-index tensor and all three unitary flattenings. Abstract rank capacities, commutator graphs, or a pair-array statement alone do not manufacture it.

## 9. Exact boundaries and assurance

No load-bearing non-elementary theorem remained unreconstructed under these five mathematical statements. The phase-defect formula was rebuilt from the present definitions and four actual marginal sums, not imported by confidence from the earlier w20 review. The precise normalized Frobenius/torus convention is stated in §4.2.

Unproved original prerequisites remain:

- an appropriately uniform conditional-entropy/purity bound over all original states/bases;
- a sufficiently strong all-tensor/all-AB rank/noncommutation statement;
- degenerate-positive-spectrum common-unitary compatibility;
- the supplied-data or unprovided combinatorial premise needed to decide the rank-one commuting endpoint at the original dimension;
- an actual improved witness or actual lower-bound improvement relative to an independently established baseline.

No order6 Latin-pair existence/nonexistence result, numerical48..60 reconciliation, actual48/noexact50/lower51, historical/native catalogue or I48/J49/J50 assertion is admitted. The parent-defined model is not a new book/public-source equivalence audit. All source/proof/method/public-status STOPs, S2's post-rank quarantine, own reviewer STOP/MINOR and permanent findings persist. Earlier pin times do not certify cognitive independence.

This is same-harness WRITTEN review of the frozen scope only—not parent adoption, formal/kernel/human/configured-family/executable/independent-model or novelty acceptance. Main must itself read complete operative sources and this actual return before any adoption. No scientific execution or selected probe occurred.
