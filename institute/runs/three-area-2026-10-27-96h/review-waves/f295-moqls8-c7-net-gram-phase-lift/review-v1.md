# Review v1 — wave f295-moqls8-c7-net-gram-phase-lift (reviewer ReviewF295MOQLS)

- Manifest SHA256 f6f8fd9f9634fc55ed852a426caa1ef801e413aa885217c7e39e21257ab04a8a (3546 B, 52 LF) — verified live, matches assignment.
- Freeze receipt SHA256 6228504d3406d1eeac48992974efcb17bcf7cb63ff2aaf1393c4c5c117b7e880 — verified live, matches assignment; packet SHA256 3f6a4203016f44aa7ca90d0e8c5cf368fce3136b71108ee6ca8afcefc470825f (15632 B, 181 LF) verified live.
- Source S1 hash verified live: bfd6e90d21f93efebb40ec3f0fb13e9ce12f889a35cb42a0a15e4ffd89b6e71d, 14455 B (hash/byte metadata only; the S1 content was read exclusively through the frozen packet).
- Status-only controls read and hash-verified, no excluded links followed: contract-addendum-2-frontier-first-owner-direction-v1.json (5e18c2d4…), parent-L1-selected-diagnostic-release-quarantine-v1.json (ba6b4bb9…), parent-written-duty-execution-and-reporting-deviations-20261030-v1.json (12e118d8…).
- Mode: WRITTEN_ONLY. No selected concrete net/array/vector/matrix/permutation, no chosen or symbolic special-case instantiation, no sanity probe (private or public), no code/CAS/interpreter/solver/enumeration/replay, no network, no sibling/author code, no prior review body, no held payload. All derivations below are universal written arguments over the stated quantifiers. Only hash/byte/date/ls metadata tools were used.
- Read receipt: entire literal-packet-v1.md read raw in ten windows ≤20 LF (1-20, 21-40, 41-60, 61-80, 81-100, 101-120, 121-140, 141-160, 161-181), all line endings observed; packet = 2 wrapper lines + complete S1|1..S1|179 (181 LF total), byte tail inspected ("…acceptance is claimed.\n"); no elision found, nothing to recover. Pre-body administrative ACK sent to Main 2026-10-30T03:58:22 PDT, before any packet-line read.
- Clocks (fresh /bin/date): 03:58:03 (wave dir), 03:58:22 (ACK), 03:58:36 (packet read complete), 04:08:49 (pre-write checkpoint). No gap exceeds 30 min; no unbounded wait.
- Scope boundary honored: no phase-pentagon packet and no f228/f229 artifact opened; no C7-exclusion, q1-closure or novelty question adjudicated (out of scope per assignment).

## Per-claim verdicts

### C1 — Five-net setting, line ONBs, W-ONBs, identity (1) [S1|9–S1|15] — SUPPORTED
- Five-partition incidence claims of the MOQLS(8) row/column/symbol classes (distinct classes meet exactly once; two cells share at most one line) follow from the Latin property per row/column and from orthogonality of each classical mate pair: two cells agreeing in two classes would force equal coordinates in the grid given by any other two classes. Written, universal.
- Q entries form an ONB on every net line: rows/columns are ONBs by hypothesis; for a symbol class of L_i, the same-cell tensor family {Q_x ⊗ L_i(x)} being an ONB of C^64 forces <Q_x,Q_y> = 0 for distinct cells x,y carrying the same L_i-symbol (identical second factor), i.e. mutual orthogonality of the 8 unit vectors on each symbol line, hence an ONB. Universal.
- Given the witness hypothesis (see F1): 7 component rays per line are orthonormal vectors inside W = span(component), dim W = 7, hence a W-ONB; the 8th line vector is orthogonal to that ONB, hence lies in the 1-dimensional W⊥ as a ray f, the same ray for all 40 lines; T = complement of the component meets every line exactly once and is independent. Summing one class's 8 line-resolutions of I_W gives (1) Σ_{x∈X} P_x = 8·I_W. All verified.

### C2 — Collinearity graph polynomial (2) [S1|19–S1|21] — SUPPORTED
- Degree 35 = 5 lines × 7 co-line cells, no double count since two cells share ≤ 1 line.
- Collinear pair: 6 remaining cells of the common line + 4·3 intersections of same/different-class other lines through x and y (same-class pairs are parallel, disjoint; each different-class pair meets once off {x,y} since x∈ℓ_y would give a second common line). 6+12 = 18.
- Noncollinear pair: 5·4 = 20 cross-class line intersections, each producing a common neighbor distinct from x,y; same-class pairs disjoint. Universal; (N²)_xx = 35, and 15I − 2N + 20J reproduces 35/18/20 on diagonal/collinear/noncollinear. (2) verified.

### C3 — Block relations, rank, spectrum (3)–(4) [S1|23–S1|33] — SUPPORTED
- T independent ⇒ T-T block of N is 0; X-T and T-T blocks of (2) give exactly (3). M^TM = 15I₈+20J₈ is positive definite (eigenvalues 175, 15) ⇒ rank M = 8; M·1₈ = 5·1_X ⇒ 1_X ∈ col M; A·1_X = 30·1_X.
- From AM = −2M + 20J_(56,8) and J_(56,8) = M·J₈/5: A(Mv) = −2Mv for v⊥1₈, a 7-dimensional eigenspace (M injective). col M is A-invariant and A symmetric ⇒ W₀ = (col M)⊥ (dim 48) is A-invariant; the X-X block of (2) with u ∈ W₀ (Mu = 0 via 1^TM u-type cross terms vanishing, J u = 0) yields (A²+2A−15I)u = 0, eigenvalues 3, −5.
- Multiplicities: a+b = 48 and 30 − 2·7 + 3a − 5b = tr A = 0 give a = 28, b = 20. (4) verified (1+7+28+20 = 56).

### C4 — Line incidence B, kernel V, projector polynomial (5), Pi_xx = 5/14 [S1|35–S1|43] — SUPPORTED
- (BB^T)_xy = 5,1,0 on diagonal/collinear/noncollinear ⇒ BB^T = 5I + A. ker B^T = ker BB^T (‖B^Tv‖² = v^T BB^T v) = 0-eigenspace of 5I+A = −5-eigenspace of A, dim 20.
- (5) verified eigenspace-by-eigenspace on the four spectral subspaces: on 1_X, (A²−A−6I)1 = 864·1 and (108/7)·56 = 864 ⇒ 0; on the −2 space, 4+2−6 = 0 (J vanishes, contrast space ⊂ 1⊥); on the 3 space, 9−3−6 = 0; on V, 25+5−6 = 24 ⇒ identity/24. Coefficient 108/7 is forced (= 864/56). Cross-checks: Pi·1 = 0, tr Pi = (56·30 − 336 − 864)/24 = 20 = dim V.
- Pi_xx = (30 − 0 − 6 − 108/7)/24 = (60/7)/24 = 5/14. Verified.

### C5 — m_xy range and Pi off-diagonals (6) [S1|45–S1|52] — SUPPORTED
- 2 ≤ m_xy ≤ 5 by inclusion–exclusion on two 5-subsets of the 8-point T.
- X-X block of (2): A² + MM^T = 15I − 2A + 20J, and (MM^T)_xy = m_xy off-diagonal, so A²_xy = −2A_xy + 20 − m_xy. Substituting in (5)/24 with J_xy = 1: collinear (11−7m)/168, noncollinear (32−7m)/168. Both agree with the universal bound |Pi_xy| ≤ Pi_xx = 5/14 for m ∈ [2,5]. (6) verified.

### C6 — Gram slice, deviation identity (10), variance split (11) [S1|58–S1|84] — SUPPORTED
- H is a real PSD Gram (Hilbert–Schmidt inner product of the rank-one W-projectors), H_xx = 1; H1 = 8·1 by (1) (tr P_x = 1); each line's 7 X-cells resolve I_W regardless of x, hence HB = J_(56,40).
- K = H − (1/7)J: H1 = 8·1 ⇒ K1 = 0; (1/7)JB = J_(56,40) since each line has 7 X-cells ⇒ KB = 0 ⇒ (symmetry) im K ⊆ ker B^T = V ⇒ K = Pi K Pi; K ≥ 0 because K|_{1⊥} = H|_{1⊥} ≥ 0 and K·1 = 0. diag K = 6/7, tr K = 48. All verified.
- D = K − (12/5)Pi: Pi-supported; tr D = 48 − (12/5)·20 = 0; diag D = 6/7 − (12/5)(5/14) = 0 exactly.
- On a net edge, H_xy = |<Q_x,Q_y>|² = 0 by line orthogonality, so D_xy = −1/7 − (12/5)(11−7m)/168 = −1/7 − (11−7m)/70 = (m−3)/10. (10) verified, correctly scoped to net edges only (S1|84).
- Orthogonal decomposition K = (12/5)Pi + D with PiD = D = PiDPi and tr(Pi D) = tr D = 0 gives tr(K²) = 20·(12/5)² + ‖D‖²_F = 576/5 + ‖D‖²_F, and D symmetric with prescribed edge entries gives ‖D‖²_F ≥ (1/100)·Σ_{ordered collinear x≠y}(m_xy−3)². (11) verified.

### C7 — Isotropic point, scalar-relaxation iff (12)–(13) [S1|88–S1|97] — SUPPORTED
- Isotropic point of the slice means K = c·Pi; diag c·(5/14) = 6/7 forces c = 12/5: unique.
- H_iso = (1/7)J + (12/5)Pi: PSD (sum of PSD), diagonal 1/7+6/7 = 1, H_iso·1 = 8·1 (Pi·1 = 0 since V ⊂ 1⊥), H_iso·B = (1/7)·7J = J (Pi·B = 0), real rank 1+20 = 21 (span 1 ⊕ V, orthogonal sum). Verified.
- Off-diagonals from (6): edges (3−m)/10, non-edges (6−m)/10; edge-zero on every net edge iff m ≡ 3 on all collinear pairs; then non-edge values lie in [1/10, 4/10] (m ∈ [2,5]), so entrywise nonnegativity holds. The iff is explicitly confined to the PSD/diagonal/line-sum/edge-zero SCALAR relaxation and does not assert a projector Gram — exactly as the audit requires (no scalar-PSD-as-phase-lift). SUPPORTED as scoped.

### C8 — Local Fano consequence [S1|99] — SUPPORTED
- For x,y on the fixed line ℓ: U_x = T∖S_x has size 3, excludes t₀ (t₀ ∈ S_x), and |U_x∩U_y| = m_xy − 2 via inclusion–exclusion on the 8-point T; hence m = 3 ⟺ |U_x∩U_y| = 1.
- Under m ≡ 3 on ℓ's collinear pairs: the 7 triples are distinct (equal triples would intersect in 3), any two meet in exactly one point (so no pair of T-points lies in two triples), and the 7·3 = 21 pair-incidences are distinct pairs of a 21-pair ground set, hence a bijection: Steiner triple system STS(7) = Fano plane on T∖{t₀}. Necessary-condition-only framing is honest (no classification, no constructed witness). Verified.

### C9 — Phase-sensitive physical lift iff, connectivity, (16) [S1|103–S1|115] — SUPPORTED (findings F2, F3)
- Necessity of 1–2: C = Gram of the 56 W-vectors is Hermitian PSD, rank = dim span = 7 (each line's X-cells give a W-ONB), unit diagonal, and collinear distinct cells are orthogonal so C_xy = 0 on net edges.
- Necessity of 3 is definitional, not derivable from the Gram identity: a reducible (disconnected nonorthogonality graph) C can satisfy 1–2; connectedness is the precise formalization of the "intrinsic" (non-substitutable) requirement, and the packet itself says so (S1|109). See F2. Within the intrinsic witness class the iff is closed.
- Sufficiency: factor C (PSD, rank 7) as Gram of 56 unit vectors in C^7; condition 2 makes each line's 7 vectors an ONB of C^7; adjoining one unit f ⊥ C^7 on all T cells makes all 40 lines C^8-ONBs; taking any two classes as rows/columns yields a quantum Latin square (rows/columns are line ONBs), the remaining three classes are classical Latin mates (distinct-class lines meet once), the three classical pairs are orthogonal Latin squares, and all six same-cell tensor families are ONBs (for (Q,L_i): same symbol-line cells have orthogonal Q-parts; different symbol-lines give orthogonal symbol parts). The five-net incidences carry the whole construction. Connectivity makes the component intrinsically C^7.
- (16): partitioning X by any class, Σ_z |v_z><v_z| = 8·I₇, so (C²)_xy = 8·<v_x,v_y> ⇒ C² = 8C; H = C ∘ conj(C) is exactly |C_xy|². Verified. The packet correctly states these are obligations a scalar H_iso does not pay (phases/rank not encoded in H) and constructs no C.

### C10 — Affine parametrization and T-neighbor formula (17)–(18) [S1|119–S1|132] — SUPPORTED
- Five distinct directions (c_i,1) of AG(2,8), c_i ∈ F_8 distinct, all non-parallel to T (direction (1,0)); T = {(t,0)} meets every class line x+c_i y = t once at (t,0); X = {y ≠ 0}; any two distinct-direction lines meet once, same-direction lines are disjoint: a five-net with affine-line transversal. (c_i = 0, the vertical class, is admissible; see F5.)
- For x = (t+c_i b, b) on the class-i line of parameter t: the T-points of its five lines have x-coordinates t + b·({0} ∪ D_i), D_i = {c_i+c_j : j≠i} ⊂ F_8* (distinctness, char 2). For y with y-parameter b' = qb, q ≠ 1: m_xy = |bE ∩ qbE| with E = {0}∪D_i, |E| = 5, i.e. m_xy = 1 + |D_i ∩ qD_i|. (18) verified universally, including c_i = 0.

### C11 — Difference-set lemma (19), both directions [S1|136–S1|150] — SUPPORTED
- Complement identity |D∩qD| = 1 + |C∩qC| for C = U∖D, U = F_8* (|D|=4, |C|=3, |U|=7): follows from |qD∩C| = 4 − |D∩qD| and |C∩qC| = 3 − |qD∩C|. Verified.
- |C∩qC| = 1 for all six q ≠ 1 ⟺ the 6 ordered distinct pairs of C realize each nonidentity ratio exactly once (3·2 = 6). Normalizing C ∋ 1 (multiplicative translate; both e-conditions are scaling-covariant), C = {1,x,x^k}, x of order 7, k ∈ {2..6}; ratio exponents {±1, ±k, ±(k−1)} mod 7 are 6 distinct residues exactly for k ∈ {3,5} (k=2: ±(k−1)=±1 clash; k=4: k−1 ≡ −k; k=6: k ≡ −1). Verified.
- Each x ∈ F_8∖{0,1} satisfies exactly one of x³+x+1, x³+x²+1 (product = x⁶+…+x+1 vanishing on U∖{1} in char 2). All four cases verified symbolically and universally: (k=3, f₁) y = x+1 ⇒ e₁(C) = 0; (k=3, f₂) y = x²+1 ⇒ e₂(C) = x³+x²+1 = 0; (k=5, f₁) y = x²+x+1 ⇒ e₂(C) = x³+x+1 = 0; (k=5, f₂) y = x+1 ⇒ e₁(C) = 0. e₁(C) = 0 ⟺ C = nonzero vectors of the F_2-line span{1,x}; e₂(C) = 0 ⟺ 1/C is such a line (e₁(1/C) = e₂(C)/e₃(C)). Forward direction complete.
- Converse: multiplication by q ≠ 1 is F_2-linear, so q·(line) is a line; a nonidentity multiplier has order 7 and cannot stabilize a 3-set (orbits have size 7), so translates are distinct lines; two distinct 2-dimensional F_2-subspaces of F_2³ meet in exactly one nonzero vector, giving |C∩qC| = 1 for line-type C and, by inversion (bijection c ↦ 1/c mapping ratios to inverse ratios), for inverse-line-type C. Complete.
- Translation D ↔ C: e₁(U) = e₂(U) = 0 (U = roots of x⁷+1 ∖ {1}; coefficients of x⁶, x⁵ in x⁶+…+x+1 vanish); disjoint-union identities give e₁(C) = e₁(D) and e₂(C) = e₂(D) + e₁(D)² (char 2, e₁(C) = e₁(D)). Hence the two alternatives for C are exactly (19). Fully verified.

### C12 — Symmetric-function formulas (20), at-most-two-classes [S1|152–S1|158] — SUPPORTED
- e₁(D_i) = Σ_{j≠i}(c_i+c_j) = 4c_i + (S+c_i) = S+c_i (4 = 0 in char 2; S − c_i = S + c_i). e₂(D_i) = Σ_{j<k≠i}[c_i² + c_i(c_j+c_k) + c_jc_k] = 6c_i² + c_i·3Σ_{m≠i}c_m + (E₂ + c_iΣ_{m≠i}c_m) = 0 + c_iΣ_{m≠i}c_m + E₂ + c_iΣ_{m≠i}c_m = E₂ (6 = 0, 3 = 1 in char 2). (20) verified.
- Class i passes (all six counts 2) iff S+c_i = 0 or (S+c_i)² = E₂; the five S+c_i are distinct (char 2), the Frobenius square map is injective, so at most one class satisfies each alternative and at most two classes pass; at least three classes have some collinear pair with m ≠ 3. Verified.

### C13 — Failing-class variance, ordered-pair count, bounds (21)–(23) [S1|160–S1|173] — SUPPORTED
- n_q ∈ {1,2,3}: n_q ≥ 1 by |D|+|qD| − |U| = 8−7 = 1; n_q = 4 would make D a union of <q>-orbits, but q ≠ 1 generates the order-7 U, forcing D = U ≠ 4-set. n_q = n_{q⁻¹}; Σ_{q≠1} n_q = 4·3 ordered distinct pairs = 12. Three inverse pairs with equal values in {1,2,3} summing to 6: either (2,2,2) or (1,2,3); not-all-2 forces (1,2,3), hence Σ(n_q−2)² = 2·1+2·0+2·1 = 4 ≥ 4. (21) verified.
- Per class and ratio q: on each of the 8 lines the 7 X-points have parameters b ∈ F_8*, giving 7 ordered pairs (b, qb); 8·7 = 56 ordered collinear pairs per ratio per class; a collinear pair lies on a unique line of a unique class, so classes count disjoint pair sets. With (m−3)² = (n_q−2)² per pair, each failing class contributes ≥ 56·4 = 224, and ≥ 3 failing classes give Σ_{ordered collinear}(m−3)² ≥ 672. (22) verified.
- (11) then gives ‖D‖²_F ≥ 672/100 = 168/25 and tr(K²) ≥ 576/5 + 168/25 = (2880+168)/25 = 3048/25. (23) verified; in particular D ≠ 0, so K = (12/5)Pi (equivalently the isotropic ansatz) is impossible on the whole affine-line-transversal subclass — consistent with the Section 4 characterization, since ≥ 3 classes violate m ≡ 3.

### C14 — Scope honesty (isotropic-only; no C7 exclusion, no q1 closure, no novelty) [S1|5, S1|97, S1|115, S1|173, S1|177–S1|179] — SUPPORTED
- The packet repeatedly and correctly restricts itself: the iff in Section 4 is scalar-relaxation-only; Section 5 constructs no C and keeps the phase-lift question open; Section 6 is an obstruction to the specific isotropic ansatz plus a quantitative anisotropy lower bound, explicitly not an exclusion of anisotropic C7 witnesses, arbitrary transversals, nonaffine nets, or C8; no parent/independent-family/human/formal/novelty acceptance is claimed. No overclaim found. This matches the assignment's acceptance boundary exactly.

## Findings (severity)

- F1 (MINOR, self-containedness): "intrinsic component C" (S1|11) is not independently defined in the packet. The load-bearing structural premise — every net line contains exactly seven component cells — is asserted, not derived; given it plus dim span = 7, the conclusions "each line's 8th vector is a pure ray in W⊥" and "one common ray f across all 40 lines" do follow (orthonormal 7 in 7 dimensions is a W-ONB; the 8th is orthogonal to W; W⊥ is a complex line). The class so described coincides with the class defined constructively in Section 5, so the mathematics is consistent; but a reader without the external witness-class definition must take the 7-per-line property as an axiom. No mathematical error.
- F2 (MINOR, necessity attribution): S1|109's "Necessity follows by C_xy = <Q_x,Q_y>" is exact for conditions 1–2 but not for condition 3. Connectivity of the nonorthogonality graph is not implied by the Gram identity; it is the definitional content of "intrinsic" (excluding reducible substitutes), as the packet's own subsequent sentence states. The iff, read with the intrinsic class so defined, is correct; sufficiency is fully verified.
- F3 (COSMETIC): displayed equation numbers skip (14) and (15) ((13) is followed by (16)). No mathematical effect.
- F4 (NOTE, correct scoping): (10) prescribes D only on net edges; off-edge entries of D remain free, and (11)'s inequality accounts for exactly this. S1|84 states the scoping correctly.
- F5 (NOTE, completeness): c_i = 0 (the vertical class) is admitted by "c_i distinct in F_8" and is non-T-parallel; all derivations (D_i = {c_j} ⊂ F_8*, (18)–(22)) cover it without change. No gap.
- No REFUTED and no INCONCLUSIVE claims. All fourteen claim groups SUPPORTED by complete written universal derivation. In particular every dimension count (64/56/8/40, 35/30/5, 18/20, spectrum 1+7+28+20 = 56, dim V = 20, rank 21, 56 ordered pairs per ratio per class, 21 pairs in STS(7)), every normalization (unit diagonal, 5/14, 6/7, 12/5, 576/5, 168/25, 3048/25), every quantifier ("every", "at most two / at least three", "any four-subset", "all five distinct c_i"), and the reconstruction path (phase lift ↔ conditions 1–3) were checked line-by-line against the packet.

## Explicit imports and scope
- Mathematical input: literal-packet-v1.md lines S1|1–S1|179 only (complete).
- Metadata-only imports: manifest-v1.json, freeze-receipt-v1.json, SHA256/byte counts of the three status controls and of source S1, /bin/date clocks, directory listing.
- Not accessed: any phase-pentagon packet, f228/f229 artifacts and their frozen source, prior reviewer bodies, sibling outputs, author code, held payloads, quarantined L1 content, network.
- Verdict standing: this is a written verification of the packet's claims as scoped; it grants no novelty/priority, no C7 exclusion, no q1 closure, and no acceptance of any unreviewed companion result.

Reviewer: ReviewF295MOQLS. Clocks: 03:58:03 → 04:08:49 PDT 2026-10-30 (checkpoints within cadence).
