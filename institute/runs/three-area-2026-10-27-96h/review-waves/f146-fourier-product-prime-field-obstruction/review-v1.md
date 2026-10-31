# Review v1 — f146-fourier-product-prime-field-obstruction

**Kind:** INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW (slot physics-5, author PhysicsRQLS10-2).
**Authority:** `contract-addendum-2-frontier-first-owner-direction-v1.json` (frontier-first owner direction).
**Reviewer:** same-harness Claude reviewer. This is NOT human review, NOT independent-family review, NOT formal/kernel verification, and NOT a novelty or priority assessment.

## 0. Receipts

Native clocks are `/bin/date` (PDT) or `date -u` as noted; all hashes SHA-256.

| item | path (abs. prefix `/Users/jinleic/repos/aifours/`) | expected | observed | clock |
|---|---|---|---|---|
| manifest | `institute/runs/three-area-2026-10-27-96h/review-waves/f146-fourier-product-prime-field-obstruction/manifest-v1.json` | `e6c5bfe1991bcdbd1e3abeb28ab530ad9db538349bebb6994299b5439ee9d9a8`, 2505 B | match, 2505 B | 2026-10-29T04:09:14Z |
| input 1 (main general-p proof) | `physics/evidence/three-area-20261027-96h/parallel-18/rqls10/frontier-20261028-two-prime-field-product-obstruction-v1.md` | `e92814b44e774d35bc7dfc5377ccb713ae0bb900ba778207d53f124534ad3ca4`, 2253 B, 23 LF | match (sha, 2253 B, 23 LF) | 2026-10-29T04:09:22Z |
| input 2 (order-10 predecessor) | `physics/evidence/three-area-20261027-96h/parallel-18/rqls10/frontier-20261028-no5-field-product-no-transversal-v1.md` | `69849d0dad81748b50771dea667176fb3818aa54fb728268340d2fbff064fc36`, 3832 B, 39 LF | match (sha, 3832 B, 39 LF) | 2026-10-29T04:09:22Z |

Read order: manifest → input 1 (full, `:raw`) → input 2 (full, `:raw`). No other author file was opened. The author's Z3 script/JSON named in input 2 §3 were **not** read, imported, or executed. No web search, no external model, no paid API, no author contact, no Git operation, no deletion.

Reviewer artifacts (all in this directory, written only by me; hashes taken 2026-10-28 21:23:16 PDT):

| file | sha256 | bytes |
|---|---|---|
| `reviewer-f146-controls-v1.py` | `0c6fd94b1fb76214b81eb349fabfd4e696d426d1dcb8e7cc2b34728764c73f02` | 33057 |
| `reviewer-f146-controls-v1.json` | `e605c7a1a2e83a936696ffc28d031f3e4032b0af98916975efc56e29ca2fe090` | 18768 |
| `reviewer-f146-controls-v1.log` | `d7672fc5e0f37a9f90561d6fd92beb6189d71546aa7e0848e78798a0d8e84d6f` | 7239 |
| `reviewer-f146-controls-supp-v1.py` | `858b2442f85832685038d48a490eb1a970f53768a4a446b2b808d28a858286b8` | 3337 |
| `reviewer-f146-controls-supp-v1.json` | `90975debc162ed82b702c34594f11f9875674d8a56504c24f8ec863c25c80bf1` | 2545 |
| `reviewer-f146-controls-supp-v1.log` | `201d59b9271323100e74fab19a414d27159689393201cf264c62d210c4002823` | 684 |

Run clocks: main controls `/bin/date` 21:21:08 PDT → 21:21:10 PDT (script-internal 21:21:08.225 → 21:21:10.055, elapsed 1.83 s; the script hashes itself at start and printed `0c6fd94b…`, matching the file). Supplementary hunt 21:22:42 → 21:22:54 PDT (elapsed 11.06 s). Python 3.14.3, macOS arm64. Exit status 0 both runs.

## 1. Scope under review (exact)

Claim A (input 1, Theorem, first paragraph). For every prime p ≥ 3 and every conjugation-stable subfield F ⊆ C over which Φ_p is irreducible, and every 2p×2p complex Hadamard K with entries in F, the Fourier-product array ψ_{(r,c)}(t) = ζ_{2p}^{rt} K_{t,c}/√(2p) has no three pairwise-orthogonal cells in three distinct same-parity physical rows and three distinct columns; hence no orthogonal transversal.

Claim B (input 1, Theorem, second paragraph; input 2 §1 for p = 5). For p ∤ q, Φ_p is irreducible over Q(ζ_q), so no BH(2p,q) Fourier-product QLS has a transversal.

Not under review and not granted here: anything about p | q, composite orders, non-Fourier products, arbitrary/non-product QLS, the "formerly open q18 family" status language, the Z3 corroboration of input 2 §3, the "remaining root order divisible by 30" synthesis (depends on other imports), novelty, priority, and the predecessor's Section 3 claims in general.

## 2. Independent reconstruction and proof

Throughout, F is a **field** with Q ⊆ F ⊂ C (so characteristic 0), closed under complex conjugation; p ≥ 3 prime; N = 2p; ζ_m = e^{2πi/m}; a complex Hadamard matrix has entries of modulus 1 and K*K = KK* = N·I. Cells are (r,c) with r,c ∈ Z_N; ψ_{(r,c)}(t) = ζ_N^{rt} K_{t,c}/√N.

**Step 0 (it is a QLS).** Row r: ψ_{(r,c)} = D_r K_{·,c}/√N with D_r = diag(ζ_N^{rt}) unitary and the columns of K/√N orthonormal ⇒ orthonormal basis. Column c: ⟨ψ_{(r,c)},ψ_{(s,c)}⟩ = N⁻¹Σ_t ζ_N^{(s−r)t}|K_{t,c}|² = δ_{rs}. (Exact control: `qls_axioms_exact = true` on every instance.)

**Step 1 (inner product, same-parity reduction).** For cells (r,c),(s,d):
⟨ψ_{(r,c)},ψ_{(s,d)}⟩ = N⁻¹ Σ_{t=0}^{N−1} ζ_N^{(s−r)t} z_t, with z_t := conj(K_{t,c})K_{t,d}.
Conjugation-stability gives z_t ∈ F (this is the only place conjugation-stability is used). If r ≠ s have the same parity, Δ := s−r ∈ {2,4,…,2p−2} mod 2p, write Δ = 2k with k ∈ {1,…,p−1} well defined mod p, so k ≢ 0 (mod p) and ζ_N^{Δt} = ζ_p^{kt}. Since ζ_p^{k(u+p)} = ζ_p^{ku}, pairing t = u and t = u+p (u = 0,…,p−1) and setting w_u := z_u + z_{u+p} ∈ F,
 (O) orthogonality of the two cells ⇔ Σ_{u=0}^{p−1} ζ_p^{ku} w_u = 0.
If moreover c ≠ d, column orthogonality of K gives Σ_t z_t = 0, i.e.
 (C) Σ_{u=0}^{p−1} w_u = 0.
(For different parity, Δ odd, the pairing picks up a sign: ζ_N^{Δ(u+p)} = −ζ_N^{Δu}, so one gets Σ_u ζ_N^{Δu}(z_u − z_{u+p}) = 0 and (C) gives no information about z_u − z_{u+p}; the parity restriction is therefore genuinely load-bearing.)

**Step 2 (Lemma: F-linear relations among p-th roots).** Let a_0,…,a_{p−1} ∈ F with Σ_j a_j ζ_p^j = 0. If Φ_p is irreducible over F then a_0 = a_1 = … = a_{p−1}.
Proof. g(x) := Σ_j a_j x^j ∈ F[x] has deg g ≤ p−1 and g(ζ_p) = 0. Φ_p ∈ Q[x] ⊆ F[x] is monic, has ζ_p as a root and is irreducible over F, so it is the minimal polynomial of ζ_p over F and divides g. Since deg Φ_p = p−1 ≥ deg g, either g = 0 or g = a·Φ_p with a = lc(g) ∈ F; in both cases all a_j equal (to 0 or a). ∎
Conversely (1,…,1) is a relation, so the relation space is exactly F·(1,…,1): dimension 1. If Φ_p is reducible over F the relation space has dimension p − [F(ζ_p):F] ≥ 2 (exact control B: dim 2 for p = 3 over Q(ζ_3), dim 4 for p = 5 over Q(ζ_5); dim 1 over Q, Q(i), and over Q(ζ_3) for p = 5).

**Step 3 (pair lemma).** Let r ≠ s have the same parity, c ≠ d, and suppose Φ_p is irreducible over F. Then the cells (r,c),(s,d) are orthogonal ⇔ z_{u+p} = −z_u for all u ⇔ h_d(u) = −h_c(u) for all u, where h_c(u) := K_{u+p,c}/K_{u,c} (well defined, |h_c(u)| = 1).
Proof. (⇒) In (O) the coefficient of ζ_p^{j} is a_j := w_{k^{-1}j} (k invertible mod p because p is prime — this is where primality is used, together with Step 2). By Step 2 all w_u equal a common a ∈ F; by (C) p·a = 0, and char F = 0 gives a = 0. So w_u = 0, i.e. z_{u+p} = −z_u. Using |K_{t,c}| = 1 (conj = inverse): K_{u+p,d}/K_{u+p,c} = −K_{u,d}/K_{u,c}, i.e. h_d(u) = −h_c(u). (⇐) If h_d = −h_c then z_{u+p} = −z_u, all w_u = 0, and (O) holds for every even nonzero Δ — no irreducibility needed. ∎
Remarks. (i) The ⇒ direction uses unit moduli only to pass from z_{u+p} = −z_u to h_d = −h_c; for nonzero entries of arbitrary modulus one would get h_d(u) = −1/conj(h_c(u)), and the three-cell contradiction below still follows (it would force |h|² = −1). The author's statement is correct as written since complex Hadamard entries are unimodular. (ii) Consequence for odd q: if K ∈ BH(2p,q) with q odd (and Φ_p irreducible over Q(ζ_q), e.g. p ∤ q) then h_c(u), h_d(u) ∈ μ_q while −h_c(u) ∉ μ_q, so there are **no** orthogonal same-parity distinct-column pairs at all — stronger than Claim A; not claimed by the author, recorded as a by-product only.

**Step 4 (Claim A).** Let (r_1,c_1),(r_2,c_2),(r_3,c_3) be pairwise orthogonal with r_i distinct of equal parity and c_i distinct. Step 3 on the three pairs (all hypotheses — distinct rows of equal parity, distinct columns — hold for each pair) gives, for any fixed u, h_{c_2} = −h_{c_1}, h_{c_3} = −h_{c_1}, h_{c_3} = −h_{c_2}. Hence h_{c_2} = h_{c_3} = −h_{c_2}, so h_{c_2}(u) = 0, contradicting |h_{c_2}(u)| = 1. An orthogonal transversal is a set of 2p pairwise-orthogonal cells, one per row and per column; the rows 0,…,2p−1 contain exactly p even-indexed rows, and p ≥ 3, so any transversal contains three pairwise-orthogonal cells in distinct even rows and distinct columns — impossible. (Only pairwise orthogonality is used, so whether rays repeat is irrelevant; p = 2 is correctly excluded, since then each parity class has only two rows.) ∎

Every premise and step of the author's proof is thereby reconstructed and found correct: Δ = 2k with k ≢ 0; w_u ∈ F; (C) from K-column orthogonality; (O) from physical orthogonality; permutation of the p-th roots (k invertible); Φ_p-irreducibility ⇒ all w_u equal ⇒ w_u = 0 (char 0); sign relation h_d = −h_c from unit moduli; three-cell contradiction; p ≥ 3 same-parity rows per transversal.

## 3. Gauges, permutations and the "actual stated physical formula"

Let H(F) := {K ∈ M_{2p}(F) : |K_{tc}| = 1, K*K = 2p·I}. The theorem quantifies over all K ∈ H(F) and the proof uses no normalization (no dephasing, no K_{0,c} = 1, no symmetry). H(F) is closed under left and right multiplication by permutation matrices and by diagonal matrices with entries in F ∩ U(1). Therefore:

* **Row permutations of K** (K ↦ P_σK) stay in H(F) and the theorem applies verbatim to the new matrix. This matters because the induced QLS is in general *not* equivalent to the old one: the Fourier factor D_r = diag(ζ_{2p}^{rt}) does not commute with P_σ, and the pairing t ↔ t+p used in h_c is tied to the coordinate index that carries ζ_{2p}^{rt}. The theorem survives precisely because it is proved for every member of H(F), not for a normal form. Exact controls confirm this on all 720 row permutations of a BH(6,4) (p = 3) and on 25 row permutations of a BH(10,4) (p = 5): zero same-parity triples and zero transversals in every case (§5).
* **Column permutations of K** relabel the QLS columns; **column gauges** diag(μ_c) multiply each cell by a phase; **row gauges** diag(λ_t) (|λ_t| = 1, λ_t arbitrary in C) act as one global diagonal unitary on all cells. None changes any inner product, so the orthogonality structure, triple counts and transversals are invariant even when λ_t ∉ F.
* **Physical-row shifts** r ↦ r + a equal a row gauge by ζ_{2p}^{at} up to a per-cell phase, hence preserve the structure; the condition "r ≡ s (mod 2)" is a relation between two rows and is shift-invariant. Multiplying the coordinate by a unit u mod 2p (t ↦ ut) relabels r ↦ u⁻¹r, which preserves parity (u odd).
* Transposing the physical array does not change what a transversal is; the three-cell statement itself is about physical rows as given by the formula.

Conclusion: no hidden gauge or normalization assumption; row permutations of K over F preserve the theorem (because they preserve membership in H(F)), while they do change the QLS — exactly as the proof requires.

## 4. The coprime-conductor corollary (Claim B), proved with explicit imports

**Import I (classical, stated, not re-proved):** for every n ≥ 1, Φ_n is irreducible over Q; equivalently [Q(ζ_n):Q] = φ(n) (Gauss for prime n; Kronecker/Dedekind in general — textbook material, e.g. Lang *Algebra* VI §3 or Washington *Cyclotomic Fields* ch. 2; no primary-source read was needed or performed). Elementary facts used: φ is multiplicative on coprime arguments (CRT), and the tower law.

**Lemma.** Let p be an odd prime and q ≥ 1 with p ∤ q. Then Φ_p is irreducible over Q(ζ_q), and Q(ζ_q) is conjugation-stable.
Proof. gcd(p,q) = 1, so there are integers a, b with ap + bq = 1. Put m = pq. Then ζ_m = ζ_m^{ap+bq} = ζ_q^{a}·ζ_p^{b} ∈ Q(ζ_p,ζ_q), while ζ_p = ζ_m^{q}, ζ_q = ζ_m^{p}; hence Q(ζ_p,ζ_q) = Q(ζ_m). By Import I, [Q(ζ_m):Q] = φ(pq) = φ(p)φ(q) = (p−1)φ(q) and [Q(ζ_q):Q] = φ(q); the tower law gives [Q(ζ_q)(ζ_p):Q(ζ_q)] = p−1. The minimal polynomial of ζ_p over Q(ζ_q) divides Φ_p (monic, degree p−1, ζ_p a root, coefficients in Q ⊆ Q(ζ_q)) and has degree p−1, so it equals Φ_p; i.e. Φ_p is irreducible over Q(ζ_q). Conjugation is the automorphism ζ_q ↦ ζ_q^{−1} of Q(ζ_q), so the field is conjugation-stable. ∎
(This is the same statement as the author's "linear disjointness of Q(ζ_q) and Q(ζ_p) for coprime conductors", i.e. Q(ζ_q) ∩ Q(ζ_p) = Q; I have reduced it to Import I rather than importing the disjointness theorem itself.)

**Corollary (Claim B).** If K ∈ BH(2p,q) with p ∤ q, its entries lie in Q(ζ_q), which satisfies the hypotheses of Claim A by the Lemma; hence the Fourier-product QLS of K has no three pairwise-orthogonal cells in distinct same-parity rows and distinct columns, and no orthogonal transversal. For p = 5 this is input 2 §1 (q = 6, 12, 18, 24, 36, 42, … all have 5 ∤ q). ∎

When p | q, Φ_p splits completely over Q(ζ_q) and nothing here applies; the author states this exclusion explicitly and I make no claim either way.

## 5. Exact controls (independently authored; receipts in §0)

Method: all arithmetic exact in Z[ζ_L] (integer polynomials reduced modulo Φ_L, Φ_L computed from scratch by exact division of x^L−1 by the lower Φ_d). QLS built from my own transcription of the author's formula as exponent vectors; orthogonality via the Δ-table cross-checked cell-by-cell against direct inner products on every primary instance (`delta_table_matches_direct_cellwise = true`). Transversal search = exhaustive backtracking (node-capped; no search hit its cap). Author code was not used in any way.

**A. Machinery (positive and negative):** Φ_n table for n ∈ {1,2,3,4,5,6,10,12,15,20,30} and degrees φ(n) for n ≤ 60 correct; zero tests: 1+ζ_3+ζ_3² = 0, 1+ζ_4² = 0, 1+ζ_6³ = 0, Σζ_5^j = 0, Σζ_10^{2j} = 0, ζ_12⁴+ζ_12⁸+1 = 0 (true) and 1+ζ_3, 1+ζ_6, 1+ζ_5+ζ_5²+ζ_5³, Σ_{t<5}ζ_10^t (nonzero) — all as expected; Hadamard checker accepts Tao BH(6,3), F_6, F_2⊗F_3, F_3⊗F_2, F_10, F_2⊗F_5, F_5⊗F_2 and rejects the all-ones 6×6 and single-entry mutations of Tao and F_6; transversal counter on cyclic Latin squares returns Z_3: 3, Z_4: 0, Z_5: 15, Z_6: 0, Z_7: 133 (all complete). `A_machinery.all_ok = true`.

**B. Algebraic core:** dim_F of {a ∈ F^p : Σ a_jζ_p^j = 0} computed by exact Q-rank: p = 3: Q → 1, Q(i) → 1, Q(ζ_3) → 2; p = 5: Q → 1, Q(i) → 1, Q(ζ_3) → 1, Q(ζ_5) → 4 — dimension 1 exactly when gcd(conductor, p) = 1, consistent with Step 2. Over Q the two conditions (O)+(C) have rank p (force w = 0) for p = 3, 5. Explicit reducible-case relation w_u = ζ_p^u: Σ_u ζ_p^u w_u = 0 and Σ_u w_u = 0 hold exactly while w_0 ≠ w_1 — the author's "all w_u equal" step fails without irreducibility. `B_algebraic_core.all_ok = true`.

**C. Positive controls (Φ_p irreducible; F = Q(i), q = 4, p ∤ 4):** Paley/Turyn matrices C = I + iS from the symmetric conference matrices of orders 6 (q = 5) and 10 (GF(9)); conference properties and Butson-Hadamard property verified exactly (L = 12 and 20).

| instance | same-parity triples | any-parity distinct-row/col triples | ordered (Δ,c,d) same-parity orth. pairs | pair-lemma mismatches | transversals (complete) |
|---|---|---|---|---|---|
| BH(6,4), p = 3 | 0 | 0 | 12 (= 6 ordered (c,d) with h_d = −h_c × 2 values of Δ) | 0 | 0 (36 nodes) |
| BH(6,4)ᵀ | 0 | 0 | — | 0 | 0 |
| BH(10,4), p = 5 | 0 | 0 | 8 (= 2 × 4) | 0 | 0 (100 nodes) |
| BH(10,4)ᵀ | 0 | 0 | — | 0 | 0 |
| BH(6,4), all 720 row perms | 0 in all 720 | — | — | — | 0 in all 720 |
| BH(10,4), identity + 24 seeded row perms | 0 in all 25 | — | — | — | 0 in all 25 |

The pair lemma is non-vacuous (orthogonal same-parity pairs exist) and holds as an exact equivalence (0 mismatches over all even Δ ≠ 0 and all c ≠ d). `C_positive_controls_all_ok = true`.

**D. Negative-hypothesis controls (Φ_p reducible):** F = Q(ζ_3) = Q(ζ_6) with p = 3 (Tao BH(6,3), F_6, F_2⊗F_3, F_3⊗F_2) and F = Q(ζ_5) = Q(ζ_10) with p = 5 (F_10, F_2⊗F_5, F_5⊗F_2).

| instance | same-parity triples | orth. same-parity pairs violating h_d = −h_c | transversals (identity rows; complete) | row-perm sweep: perms with triples / with transversal |
|---|---|---|---|---|
| Tao BH(6,3) | 24, e.g. (0,0),(2,3),(4,1) | 18 of 18 | 0 | 720/720 triples; 0/720 transversal |
| F_6 | 120 | 12 | 0 | 432/720; 0/720 |
| F_2⊗F_3 | 120 | 12 | 0 | 432/720; 0/720 |
| F_3⊗F_2 | 48 | 24 | 0 | 432/720; 0/720 |
| F_10 | 10000, incl. hand triple (0,0),(2,1),(4,2) | 120 | 0 (282 800 nodes) | 5/25; 0/25 — supp.: 206/1501; 0/1501 |
| F_2⊗F_5 | 10000 | 120 | 0 (2240 nodes) | 5/25; 0/25 — supp.: 206/1501; 0/1501 |
| F_5⊗F_2 | 6400 | 240 | 0 (12 340 nodes) | 3/25; 0/25 — supp.: 210/1501; 0/1501 |

Every triple example was re-verified by direct exact inner products. Hand check of the Tao triple: with ω = ζ_3 the three cells are (1,1,1,1,1,1), (1,ω²,ω,1,ω²,ω), (1,ω²,ω²,ω,ω,1); each pairwise inner product equals 2(1+ω+ω²) = 0; and for columns 0 and 3 one has h_3 = h_0 = (1,1,1) ≠ −h_0 with w = (2,2ω,2ω²) — the explicit relation of control B realized by an actual Hadamard matrix. So the three-cell lemma genuinely needs the irreducibility hypothesis ("intended-reason" negative control passes: `D_every_reducible_case_has_same_parity_triples = true`).

**No full transversal in a reducible case was found:** none exists for any row permutation of the four order-6 matrices (exhaustive over all 720, which covers their whole Hadamard-equivalence classes, since column permutations and row/column gauges do not change the orthogonality structure), and none for identity + 1500 seeded random row permutations of the three order-10 matrices (all searches complete, none capped). For F_{2p} itself and for the lexicographic F_2⊗F_5 / F_5⊗F_2 I also checked by hand that no transversal can exist (complete-mapping obstruction of Z_{2p}; forced equal-c₁/c₂ fiber arguments). This is a bounded negative result on specific instances, not a theorem; the manifest's "if available" option is therefore discharged by the exact failing relation and the exact three-cell counterexamples, as permitted.

Limits of the controls: no odd-q or q ∉ {3,4,6,10} instance was available to me (e.g. no BH(10,6) or BH(6,10) at hand), so Remark (ii) of Step 3 is proved but not exercised; p = 7 and higher were not exercised (the proof is uniform in p and the controls are illustrations, not the evidence for the theorem).

## 6. Findings

No FATAL and no MAJOR issue at the reviewed scope.

MINOR (expository; none affects correctness):
1. Input 1 proof, "their only F-linear relation is the all-ones relation": should read "every F-linear relation is an F-multiple of the all-ones relation", and the reason (Φ_p monic with root ζ_p and irreducible ⇒ minimal polynomial ⇒ divides any relation polynomial of degree ≤ p−1) is left implicit. Same in input 2 §2. Supplied in §2 Step 2.
2. The hypothesis that F is a *field* (needed for the division argument) is only implicit in "irreducible over F"; and characteristic 0 is used in "p·a = 0 ⇒ a = 0" without mention (automatic for F ⊂ C).
3. "including when rays repeat" is undefined; harmless, since only pairwise orthogonality of the 2p cells is used.
4. The coprime-conductor import is named but not stated precisely; §4 states and proves it from the irreducibility of cyclotomic polynomials over Q.
5. Input 2's "formerly open", Section 3 (Z3 corroboration) and the "divisible by 30" synthesis depend on other artifacts and are outside this manifest; they are neither confirmed nor contradicted here. The general-p file (input 1) does not repeat them.

## 7. Verdict (exact scope)

* **Claim A (general-p three-cell obstruction and no-transversal corollary for Fourier-product QLS of order 2p over conjugation-stable fields F ⊂ C with Φ_p irreducible):** CORRECT as a written proof. Independently reconstructed in full (§2); no gap found; gauge/permutation robustness confirmed (§3); exact positive controls at p = 3, 5 pass and exact negative-hypothesis controls show every load-bearing hypothesis (irreducibility, same parity, distinct columns, p prime, p ≥ 3) is used.
* **Claim B (BH(2p,q) with p ∤ q has no Fourier-product transversal):** CORRECT, with the field fact proved in §4 from the classical irreducibility of Φ_n over Q (explicit import).
* Severity: no FATAL, no MAJOR; MINOR expository items only (§6).
* Not asserted: anything for p | q; anything for arbitrary (non-Fourier-product) QLS; source priority, novelty, or publication status; the predecessor's status/synthesis statements; human, independent-family, kernel or formal verification. Same-harness review only.

— reviewer, written 2026-10-28 PDT (artifact clocks in §0).
