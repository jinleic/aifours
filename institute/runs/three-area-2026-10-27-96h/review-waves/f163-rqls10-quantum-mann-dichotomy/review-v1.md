# Review v1: wave f163-rqls10-quantum-mann-dichotomy

- **Kind.** This is an independent same-harness scientific review. It is not a human review, an independent-model-family review, a formal or kernel verification, or a novelty assessment.
- **Reviewer.** ReviewF163QuantumMann.
- **Author of the candidate.** PhysicsRQLS10-2, slot physics-5.
- **Manifest.** `manifest-v1.json`, SHA-256 `faec1ab8c8a378d1f7d4f7b50fed336a53e5fc078c4ac286e545fb5683ddb63e`. I verified this hash before reading the file. It matches the value in my task.
- **Clock.** Native `/bin/date` immediately before the first write of this file: 2026-10-29T07:53:39-0700 PDT. Proofreading edits followed. The final bytes are pinned, with a later native clock, by `rv163-receipts-v1.json`.

## 0. Bottom line

**Counts: FATAL 0, MAJOR 0, MINOR 3.**

| Claim | Verdict |
|---|---|
| Theorem A: L(K3,3,3) has no orthonormal representation in C^6 (written proof) | **WRITTEN_SUPPORTED.** I reconstructed every step (§3). |
| Corollary A: a Z2-quotient Latin square of order 6 has no quantum orthogonal mate; the 9 core contexts alone are impossible | **WRITTEN_SUPPORTED**, via the parity-core embedding lemma. I proved that lemma in §3.5, because the bundle states it without proof (MINOR m2). |
| Theorem B existence: exact Z[ζ20] representation of L(K5,5,5) in C^10 with 75 flat rays and 675 orthogonalities | **WRITTEN_SUPPORTED.** Two exact zero tests of my own, plus my own structural proof (§4). |
| Theorem B: rays pairwise non-parallel; entries ζ20^e/√10; 825 orthogonal pairs in total | **WRITTEN_SUPPORTED** (exact). |
| Theorem B: trivial commutant | **WRITTEN_SUPPORTED, upgraded.** The candidate computed this numerically. I verified it exactly (§4.5). |
| Consequence: the parity core of a Z2-quotient-labelled 1-RQLS(10) is realizable, and irreducibly; a no-go for such squares cannot come from the 75-ray core alone | **WRITTEN_SUPPORTED** in the precise sense of §4.6. The comparison with "reducible 4+6 cores analysed earlier" is **not evaluated**, because that material is outside the bundle. |
| Maximal QLS(10): 100 pairwise non-parallel rays, rows and columns orthonormal, five T1 classes that are orthonormal transversals, 1225 orthogonal pairs, **exactly 5** orthogonal transversals, hence not 1-resolvable | **WRITTEN_SUPPORTED.** Exact; the census was run with two independent algorithms (§5). The phase data come only from the author-replay literals (MINOR m1). |
| Exact L(K7,7,7) representation in C^14: 147 non-parallel rays, 1911 orthogonalities | **WRITTEN_SUPPORTED** (exact, §6). Same provenance caveat (m1). |
| K666 control JSON (input 2) | **INCONCLUSIVE / not evaluable.** It is a PASS receipt with no vectors. No claim in scope relies on it. |
| Theorem C; m7-packet §3–§4; the "25 solvable offsets / only T0 inconsistent" remark in QLS-packet §1 | **NOT REVIEWED.** These are outside the frozen scope. |

The manifest scope also says "no 1-RQLS10 or novelty claim". I found no such claim in the bundle. Both packets state that the 100-ray 1-RQLS(10) target remains open.

## 1. Inputs verified before interpretation

All files were read completely with exact `:raw` selectors, in the declared order. Every file is LF-only (0 CR bytes) and ends in LF.

| # | File (`physics/evidence/three-area-20261027-96h/parallel-18/rqls10/`) | SHA-256 | Bytes | LF | Match |
|---|---|---|---|---|---|
| 1 | `frontier-20261029-quantum-mann-dichotomy-k333-k555-v1.md` | `9fba4852…dde3c` | 12099 | 135 | yes |
| 2 | `frontier-20261029-k666-zhangcao-control-v1.json` | `455ad0b7…73731` | 353 | 9 | yes |
| 3 | `frontier-20261029-half-resolved-maximal-qls10-and-m7-v1.md` | `e72f7c7d…791d1` | 6594 | 79 | yes |
| 4 | `frontier-20261029-norm-test-independent-replay-v1.py` (read/hash only) | `3a5627da…7f7a6` | 4953 | 80 | yes |
| 5 | `frontier-20261029-norm-test-independent-replay-v1.json` (read/hash only) | `82b4d05a…f8b4e` | 700 | 26 | yes |

All full 64-hex SHA-256 values equal the manifest values. The bundle has no errata, overlays or withdrawals.

I did not open any file the packets cite but the manifest does not list. These include:
- the producer scripts and JSONs for K555, K777, the half-resolved QLS10 and the flat-diagonal searches;
- the earlier reformulation packet `6f6a2dd8…`.

Their pinned hashes are therefore unverified by me.

## 2. Conventions used in this review

- **Orthonormal representation.** The candidate's §0 defines an *orthonormal representation of L(K_{m,m,m}) in C^{2m}*: each of the 3m² edges gets a unit vector, and every vertex star of 2m edges is an orthonormal basis (ONB). Because each star has exactly 2m = dim members, this is the same as "unit vectors, and line-graph-adjacent edges are orthogonal".
  - Extra orthogonalities between non-adjacent edges are allowed. The representation is therefore not required to be *faithful*, and it is not: see the counts of 150 and 441 below.
- **QLS(n), orthogonal transversal, 1-RQLS.**
  - A QLS(n) is an n×n array of unit vectors in C^n whose rows and columns are ONBs.
  - An *orthogonal transversal* is a set of n cells, one per row and one per column, whose vectors are pairwise orthogonal (hence an ONB).
  - A *1-RQLS(n)* is a QLS(n) whose n² cells partition into n orthogonal transversals. Its *resolution square* L(r,c) = index of the transversal containing (r,c) is a classical Latin square.
- **Z2 quotient.** L has a Z2 quotient if rows = R0⊔R1, columns = C0⊔C1 and symbols = T0⊔T1, each part of size m, with L(R_i × C_j) ⊆ T_{i+j mod 2}.

## 3. Theorem A: complete reconstruction

### 3.1 Frame identity (stated in §0 of the candidate, derivation omitted)

Let X_AB = Σ_{a,b} |ψ_ab⟩⟨ψ_ab|, and define X_AC and X_BC in the same way.
- Summing the star completeness relations over a ∈ A gives X_AB + X_AC = mI.
- Over B: X_AB + X_BC = mI.
- Over C: X_AC + X_BC = mI.
- Hence X_AB = X_AC = X_BC = (m/2)I, i.e. Σ_a P_a = (m/2)I with P_a = Σ_b |ψ_ab⟩⟨ψ_ab|. ✔

Each P_a is a rank-m projector, because the ψ_ab (b ∈ B) are orthonormal.

As an exact sanity check, I verified the identity Σ_{cells in a quadrant} v v* = m² I on the actual K555 and K777 objects (unnormalised flat v, every quadrant) in Z[ζ_N].

### 3.2 Lemma 1

Assume P1 + P2 + P3 = (3/2)I.
- **The anticommutator.** Put S = P1 + P2 = 3/2 − P3. Then S² = 9/4 − 3P3 + P3 = 9/4 − 2P3 = 2S − 3/4. Also S² = S + {P1,P2}. So {P1,P2} = S − 3/4.
- **The sandwich.** Compress by P1 on both sides:
  - the left side gives 2 P1P2P1;
  - the right side gives P1 + P1P2P1 − (3/4)P1.
  - Hence P1P2P1 = P1/4. ✔ The same holds for every pair.
- **Ranks.** Taking traces gives tr(P1P2) = rk P1/4 = rk P2/4. So all ranks equal some k. The trace of the sum gives 3k = (3/2)·dim H, so dim H = 2k. ✔
- **The basis f_j, g_j.** Let f_j be an ONB of ran P1. Then P2 f_j = P1P2P1 f_j + (1−P1)P2 f_j = f_j/4 + g_j.
  - Using P2P1P2 = P2/4: ⟨g_i, g_j⟩ = ⟨f_i, P2 f_j⟩ − ⟨f_i, P2P1P2 f_j⟩ = (3/4)⟨f_i, P1P2P1 f_j⟩ = 3δ_ij/16. ✔
  - With w_j = 4g_j/√3, {f_j, w_j} is an ONB of H.
- **The 2×2 blocks.**
  - P2 w_j = (4/√3)(P2 f_j − P2 f_j/4) = √3 P2 f_j = (√3/4) f_j + (3/4) w_j. ✔
  - So P2 = [[1/4, √3/4], [√3/4, 3/4]] ⊗ I = |u2⟩⟨u2| ⊗ I, with u2 = (1/2, √3/2), i.e. t = π/3.
  - Then 3/2·I2 − |e1⟩⟨e1| − |u2⟩⟨u2| = [[1/4, −√3/4], [−√3/4, 3/4]] = |u3⟩⟨u3| with u3 = (−1/2, √3/2), i.e. t = 2π/3. ✔

### 3.3 Lemma 2

Take the first row as the basis. Row 2 is then a unitary M with zero diagonal: M_cc = ⟨η_1c, η_2c⟩ = 0 by column orthonormality. Write M = [[0,a,b],[c,0,d],[e,f,0]].
- Column orthogonality gives ē·f = c̄·d = ā·b = 0.
- With unit columns:
  - a = 0 forces |f| = 1, then e = 0, then |c| = 1, then d = 0, then |b| = 1;
  - a ≠ 0 forces b = 0, then |d| = 1, then c = 0, then |e| = 1, then f = 0.
- Both cases give a phased 3-cycle.
- Row 3 is orthogonal to e_c and e_{σ(c)}, so it is a phase times e_{σ²(c)}. The array is therefore a phased Latin square of basis vectors. ✔

### 3.4 Steps 1–6

- **Step 1.**
  - Lemma 1 with k = 3 gives H = C²⊗K and P_a = |u_a⟩⟨u_a| ⊗ I.
  - ψ_ab ∈ ran P_a gives ψ_ab = u_a⊗x_ab.
  - ψ_ac ⊥ ran P_a gives ψ_ac = u_a^⊥⊗y_ac.
  - For fixed a, {x_ab}_b and {y_ac}_c are ONBs of K. This is immediate, since ⟨u_a⊗x, u_a⊗x'⟩ = ⟨x,x'⟩.
  - For fixed b, ⟨ψ_ab, ψ_a'b⟩ = ⟨u_a,u_a'⟩⟨x_ab,x_a'b⟩ with ⟨u_a,u_a'⟩ ∈ {±1/2} ≠ 0, so {x_ab}_a is orthonormal. The same holds for y because ⟨u_a^⊥, u_a'^⊥⟩ = ⟨u_a,u_a'⟩. ✔
- **Step 2.** I recomputed the circular-basis coordinates.
  - u = (cos t, sin t) = (e^{−it} f₊ + e^{it} f₋)/√2, so ψ_ab = e^{it_a}(ξ_a x_ab, x_ab)/√2 with ξ_a = e^{−2it_a}.
  - u^⊥ = (−sin t, cos t) = i e^{it}(−e^{−2it} f₊ + f₋)/√2, so ψ_ac ∝ (−ξ_a y_ac, y_ac)/√2.
  - The set is {ξ_a} = {1, ω², ω} = {1, ω, ω²}. ✔
- **Step 3.**
  - The projector onto G(U) is ½[[I,U],[U*,I]], and G(U)^⊥ = G(−U), by a direct check for unitary U. ✔
  - (K_b x_ab, x_ab) ∈ G(K_b), so the A-edges at b span G(K_b). Similarly the A-edges at c span G(−L_c).
  - The stars at b and at c are ONBs, so ψ_bc ∈ G(−K_b) ∩ G(L_c).
  - η-rows are orthonormal via the G(K_b) form, and η-columns via the G(L_c) form (L_c unitary). The same holds for κ = K_bη = −L_cη.
  - Hence K_b = Σ_c |κ_bc⟩⟨η_bc| and L_c = −Σ_b |κ_bc⟩⟨η_bc|.
  - det K_b = det L_c = ω³ = 1, because x and y are column-orthonormal. ✔
- **Step 4.** Lemma 2 applied to η and κ gives K_b = W Σ_c θ_bc E_{μ(b,c),λ(b,c)}. ✔
- **Step 5.** Σ_b K_b = Σ_a ξ_a Σ_b |x_ab⟩⟨x_ab| = (1+ω+ω²)I = 0, so S = 0.
  - Column j of S collects the three cells with λ = j.
  - A μ-value hit by exactly one of them leaves a unimodular entry. With three cells, the only multiset of μ-values without a singleton is {3}. So μ = π∘λ. π is a bijection because μ and λ are Latin.
  - Hence K_b = WP_πΘ_b and L_c = −WP_πΘ^c. ✔
- **Step 6.**
  - Π_b det K_b = (det U)³ Π θ = 1.
  - Π_c det L_c = (−1)⁹ (det U)³ Π θ = 1.
  - Together these give −1 = 1. ✔

I found no gap, no hidden case and no unjustified "WLOG". All phase ambiguities are absorbed into η, κ and θ before any statement depends on them.

### 3.5 Parity-core embedding lemma and Corollary A

This lemma is load-bearing for Corollary A and for the Consequence of Theorem B. The bundle asserts it in §0, citing an out-of-bundle packet, but does not prove it.

**Lemma.** Let L be a Latin square of order 2m with a Z2 quotient. Define φ_L on the 3m² cells R0×C0 ∪ R0×C1 ∪ R1×C0:
- (r,c) ∈ R0×C0 ↦ A_r B_c;
- (r,c) ∈ R0×C1 ↦ A_r C_{L(r,c)};
- (r,c) ∈ R1×C0 ↦ B_c C_{L(r,c)}.

φ_L is a bijection onto E(K_{m,m,m}), and it maps:
- each row r ∈ R0 onto star(A_r);
- each column c ∈ C0 onto star(B_c);
- each label class t ∈ T1 onto star(C_t).

**Proof.**
- For r ∈ R0, c ↦ L(r,c) is a bijection C1 → T1. For c ∈ C0, r ↦ L(r,c) is a bijection R1 → T1.
- Hence each of the three blocks is mapped injectively onto the m² AB-, AC- or BC-edges respectively, and φ_L is a bijection.
- T1-labels occur only in R0×C1 ∪ R1×C0. So rows r ∈ R0, columns c ∈ C0 and label classes t ∈ T1 lie entirely in the core, and their images are exactly the stated stars. ∎

**Consequence for Corollary A.** Any 1-RQLS(2m) with resolution square L restricts, on these 3m contexts, to an orthonormal representation of L(K_{m,m,m}). For m = 3, Theorem A therefore gives Corollary A, including the "nine contexts alone" strengthening. ✔

*Abstract-level comparison.* The cited arXiv:2603.02334 (Ball–Simoens, "Thirty-six quantum officers are entangled") has the abstract "mutually orthogonal quantum Latin squares of order six do not exist if entanglement is not allowed". The candidate's paraphrase is accurate at that level.
- [INFERENCE, definitions not read] A classical L together with a quantum mate Q gives the product family {Q_rc ⊗ e_{L(r,c)}}. That family is an ONB of C⁶⊗C⁶ exactly when Q is a quantum mate of L.
- So the full-array form of Corollary A for *every* order-6 Latin square is plausibly already covered by that theorem.
- The incremental content is Theorem A's 9-context statement. The candidate itself flags the broader result. This is not counted as a finding; novelty remains unassessed.

### 3.6 Sanity controls for Theorem A (not evidence of non-existence)

**(a) Numerical random attempts.** Script `rv163-thmA-numeric-v1.py`; L-BFGS-B on F = Σ_v ‖Ψ_v*Ψ_v − I‖²_F with an analytic gradient (finite-difference check: relative error 9.0e-11).

| m | Dimension | Starts | Result | Role |
|---|---|---|---|---|
| 2 | C⁴ | 40 | 40/40 reach F < 1e-12 | positive control |
| 4 | C⁸ | 30 | 29/30 reach F < 1e-12; all reach F < 1e-6 | positive control |
| **3** | **C⁶** | **300** | **0/300 below 1e-6; min F = 0.92987** | **target** |

- The m = 3 quantiles (0/10/50/90/100 %) are 0.92987, 0.92987, 1.00679, 1.02646 and 1.02646, which suggests a few recurring plateau values. Only the quantiles were recorded.
- At the best m = 3 point (gradient norm 1.8e-8), the finite-difference Hessian has exactly 63 eigenvalues with |λ| < 1e-6 (the largest is 3.7e-9) and no eigenvalue below −1e-6. The next eigenvalue is 0.4703.
  - 63 equals the predicted gauge dimension: 36 from global U(6) plus 27 per-vector phases.
  - So this point is a strict local minimum modulo gauge with F > 0. This rank count is numerical.
- **Limit of this control.** For m = 5, 6 random starts also stall, at F between 0.126 and 0.157, although an exact solution exists. A start at the exact certificate plus 1e-2 noise returns to F = 3e-26. Random-start failure is therefore weak evidence, and I give it no weight beyond "no numerical counterexample appeared".

**(b) Exact-rank control (restricted flat family).** Script `rv163-flat-torus-parity-v1.py`.

My own reduction, for flat Z_m²-diagonal vectors ζ_m^{⟨c_j,x⟩}e^{iφ_{q,j}}/√(2m) with the Theorem-B incidence:
- Within-quadrant orthogonality holds if and only if α, β and α−β each take every value of Z_m exactly twice.
- Fourier inversion on Z_m turns cross-quadrant orthogonality into one congruence per pair of indices sharing a value, with right-hand side π:
  - β-pairs on a = φ_AC − φ_AB;
  - α-pairs on b = φ_BC − φ_AB;
  - (α−β)-pairs on b − a.
- The system is solvable if and only if every vector of a Z-basis of the integer left kernel has even coordinate sum.

I also proved a graph form of the criterion:
- The kernel has one generator per bipartite component of the union of the three pairings.
- Each generator's coordinate sum is 3|C|/2.
- So the system is obstructed if and only if some bipartite component has |C| ≡ 2 (mod 4).
- In particular, for odd m a connected bipartite union graph always obstructs. This is a flat "quantum Mann parity".

Results:

| Case | Integer left kernel | Outcome |
|---|---|---|
| m = 3, all **6** admissible character multisets | (see the two rows below) | **0 solvable** (JSON: `m3_solvable_count` 0; `m3_criteria_agree_all` true) |
| m = 3, the 3 multisets with distinct characters (union graph K3,3; all three listed in the JSON) | dimension 1, odd generator | obstructed |
| m = 3, the 3 multisets of the form {p,p,q,q,r,r} (one listed in the JSON, [(0,0),(0,0),(1,2),(1,2),(2,1),(2,1)]; the other two were seen in the in-memory dry run of the same code) | dimension 3, all odd | obstructed |
| m = 5, candidate T | rank 15, kernel 0 | solvable; the candidate phases satisfy every congruence mod 20 exactly |
| m = 7, candidate T | rank 21, kernel 0 | solvable; phases satisfy every congruence mod 28 |
| Negative control: m = 5, T' = {(s,2s),(s,2s+1)}, admissible, connected bipartite union graph of size 10 | dimension 1, odd generator | inconsistent, for the intended parity reason |
| Negative control: one candidate phase shifted by one unit | — | violates the β- and γ-congruences |

The Z-basis was computed by unimodular integer row reduction. It agreed with the graph criterion in every case. The m = 3 outcome agrees with Theorem A, but it is restricted to this ansatz.

**Verdict, Theorem A: WRITTEN_SUPPORTED.** It depends only on elementary linear algebra. There are no imports, no pinned data and no conditional premises.

## 4. Theorem B: exact certificate, verified from scratch

### 4.1 Object

I transcribed the data from candidate §2 text:
- T = [(0,0),(0,1),(1,0),(1,3),(2,2),(2,4),(3,1),(3,4),(4,2),(4,3)];
- PHI2[AB] = (−35,−25,−25,−15,−20,−10,−15,−5,−10,0), PHI2[AC] = (−10,−10,−10,−5,0,5,−10,0,0,0), PHI2[BC] = 0;
- ψ_q(x)_j = ζ20^{4⟨c_j,x⟩ + PHI2[q][j]}/√10;
- incidence AB: A_s B_t; AC: A_s C_{s+t}; BC: B_t C_{s+t}.

The data are fully reproducible from the packet text.

### 4.2 Arithmetic, both methods mine

- **M1: polynomial reduction.**
  - Each inner product is the group-ring element Σ_j ζ^{v_j − u_j}, reduced modulo Φ20.
  - I computed Φ20 from x²⁰ − 1 by exact integer division. It equals x⁸ − x⁶ + x⁴ − x² + 1, as the candidate states. Φ28 = x¹² − x¹⁰ + … + 1 was computed the same way.
  - Irreducibility of Φ_N makes M1 exact.
- **M2: modular evaluation.**
  - P = 1000000000006421 is a deterministic Miller–Rabin prime with P ≡ 1 (mod 140). g has exact order 20 (or 28) in F_P.
  - If s ≠ 0, then N(s) is a nonzero integer with |N(s)| ≤ (Σ|c_k|)^{φ(N)}. That bound is 10⁸ for N = 20 and 14¹² ≈ 5.7e13 for N = 28, both below P, and the script asserts it on every call. N(s) also lies in (P, ζ − g), because Z[ζ] is the full ring of integers.
  - So s(g) ≡ 0 (mod P) if and only if s = 0. This test is exact.
- **Agreement.** M1 and M2 agreed on every inner product tested (all pairs of all three objects) and on the sanity cases. The frame-identity and |⟨u,v⟩|² tests use M1 only.
- **Zero-test sanity cases.** I checked eight elements with known values:

  | Element | Expected | Result |
  |---|---|---|
  | 1 + ζ20¹⁰ | 0 | ✔ |
  | 1 + ζ20⁵ | ≠ 0 | ✔ |
  | Σ ζ20^{4k} | 0 | ✔ |
  | Σ ζ20^{5k} | 0 | ✔ |
  | 1 + ζ20⁴ + ζ20⁸ | ≠ 0 | ✔ |
  | Σ ζ28^{4k} | 0 | ✔ |
  | 1 + ζ28¹⁴ | 0 | ✔ |
  | 1 + ζ28⁷ | ≠ 0 | ✔ |

### 4.3 Results (`rv163-exact-cert-check-v1.json`)

- **Incidence.** The edge map is a bijection onto the 75 edges of K5,5,5. There are 15 contexts, each of size 10. Same-part contexts are disjoint, and cross-part contexts share exactly one ray, which characterises the line-graph incidence.
- **Orthogonality.** The line graph has **675** edges (= 3m·C(2m,2)), and **675/675** of them are exactly orthogonal. Over all 2775 pairs there are **825** orthogonal pairs in total, i.e. 150 orthogonal non-adjacent pairs, as claimed.
- **Non-parallelism.** **0** parallel pairs among 2775 pairs, by two tests: the combinatorial test (exponent-difference vector constant mod 20) and the exact test |⟨u,v⟩|² = 100 in Z[ζ20]. The two tests agree.
- **Nonzero and flat.** Every ray has exact ⟨v,v⟩ = 10 and integer exponents, i.e. entries ζ20^e/√10.
- **Frame identity.** It holds exactly on AB, AC and BC.
- **Float cross-check.** The maximum basis error is 2.0e-15, matching the candidate's figure.
- **Structural cross-proof.** This is independent of the cyclotomic computation. T is uniform in α, β and α−β, and the three congruence families of §3.6(b) hold exactly for the candidate phases. By the Fourier-inversion argument this alone implies all 675 orthogonalities.

### 4.4 Negative controls (each fails for its intended reason)

- Shifting one exponent of ray 0 by +1 gives exactly 18 non-orthogonal adjacent pairs: ray 0 against its 18 star-mates.
- Replacing ray 40 by a phase multiple of ray 0 is detected as exactly 1 parallel pair by both parallelism tests.

### 4.5 Commutant: exact, not numerical

- I intersected, over F_P, the kernels of X ↦ X v vᴴ − v vᴴ X for all 75 rays. The result has dimension **1**, and the identity lies in it.
- Why this is exact:
  - rank over F_P ≤ rank over Q(ζ20), so dim_{Q(ζ)} ker ≤ 1;
  - the identity is always in the kernel;
  - so the commutant is exactly the scalars over Q(ζ20), and hence over C.
- Code controls: a single ray gives 82 = 1 + 81, and a single context ONB gives 10.
- Float SVD also gives dimension 1: smallest singular values 3.24, 3.24 and 5.4e-14.
- So "irreducible" (trivial commutant) is now exact.

### 4.6 What "parity core realizable" means, and whether the Consequence follows

**Precise meaning.** For a Z2-quotient Latin square L of order 10, the parity core P(L) consists of:
- the 75 cells R0×C0 ∪ R0×C1 ∪ R1×C0;
- 15 contexts: the 5 rows R0, the 5 columns C0 and the 5 label classes T1.

"Realizable" means there are unit vectors in C^10 on those 75 cells that make all 15 contexts ONBs. It says nothing about:
- the R1 rows, the C1 columns or the T0 classes;
- whether the realization can be completed to a QLS(10) or a 1-RQLS(10).

**It follows.** By the lemma of §3.5, P(L) is realizable if and only if L(K5,5,5) has an orthonormal representation in C^10, whatever L is. Theorem B therefore realizes P(L) for every such L, cyclic Z10 included. The same 75 rays relabelled through φ_L do it, with pairwise non-parallel rays and a trivial commutant.

So both of the following follow from Theorem B plus the lemma:
- "the parity core … is realizable, and realizable irreducibly";
- "a no-go for cyclic-label 1-RQLS(10) cannot come from the 75-ray core alone". Any obstruction must use at least one R1, C1 or T0 context.

The candidate does not overclaim. It states that 1-RQLS(10) remains open. "Dichotomy" is descriptive: m = 3 impossible, m = 5 possible.

**Verdict, Theorem B and its Consequence: WRITTEN_SUPPORTED.**

## 5. Maximal QLS(10) with exactly five orthogonal transversals

**Object.**
- From the packet text: T as above, v_q(x)_j = ζ20^{4⟨c_j,x⟩ + PHI2[q][j]}/√10, and the grid placement Q00 (x1,x2), Q01 (x1,5+x2), Q10 (5+x1,x2), Q11 (5+y1,5+y2).
- From the replay literal PHH: PHI2 = PHH. The packet says only "given in the script" (see m1).

**Exact results** (every inner product by both M1 and M2):
- **Rows, columns, T1 classes.**
  - All 10 rows and all 10 columns are ONBs.
  - The five T1(u) classes are transversals: one cell per row and per column. They are disjoint, cover exactly Q01 ∪ Q10, and are ONBs.
- **Pairs.**
  - 0 of 4950 pairs are parallel (both tests), so the cardinality is 100, the maximum.
  - There are **1225** orthogonal pairs: 450 from rows, 450 from columns, 225 from T1, and 100 others.
- **Census.**
  - **Method 1.** A row-by-row depth-first search with bitmask pruning finds exactly **5** orthogonal transversals. They are exactly the T1 classes.
  - **Method 2.** An independent Bron–Kerbosch enumeration finds all maximal cliques of the orthogonality graph. The maximum clique size is 10, and there are exactly 25 ten-cliques (ONBs): 10 rows, 10 columns and 5 transversals, with no other ONB among the 100 rays. This again gives 5 transversals.
  - **Census-code controls on classical cyclic Latin squares.** The counts match the known values:

    | Square | Transversals |
    |---|---|
    | Z5 | 15 |
    | Z6 | 0 |
    | Z7 | 133 |
    | Z10 | 0 |
- **Not 1-resolvable.** A 1-resolution needs 10 disjoint orthogonal transversals. Only 5 exist, and they cover 50 cells. ✔ The half-resolution cannot be extended. ✔
- **"Forced Q11" explanation.** For all 25 cells (r,c) ∈ R1×C1, the 5 Q10 vectors of row r together with the 5 Q01 vectors of column c have rank exactly 9: F_P rank 9 gives ≥ 9, and the exact orthogonality of the Q11 vector to all ten gives ≤ 9. So the intersection of the two complements is exactly 1-dimensional, and the Q11 vector spans it. ✔
- **Structure.** The given phases satisfy the five congruence systems exactly: R0, C0, R1 and C1 via β/α pairs on the appropriate quadrant differences, and T1 via (α−β) pairs.
- **Negative control.** Shifting one Q10 phase by +5 breaks the rows, the columns and T1; only 850 orthogonal pairs remain.

**Verdict: WRITTEN_SUPPORTED**, for the object defined by the bundle data.

## 6. Exact L(K7,7,7) representation in C^14

**Object.** T7 comes from the packet text; PHI2 = PH7 comes from the replay literal. Arithmetic is in Z[ζ28], with Φ28 computed and checked.

**Exact results:**
- the edge map is a bijection onto the 147 edges; 21 contexts of size 14 with the line-graph incidence pattern;
- **1911/1911** adjacent pairs are orthogonal;
- **0** parallel pairs among 10731 (both tests);
- entries are flat ζ28^e/√14;
- T7 is uniform in α, β and α−β; the congruences hold mod 28; the frame identity holds exactly.

Informational, not claimed by the author:
- there are 2352 orthogonal pairs in total, i.e. 441 orthogonal non-adjacent pairs;
- the commutant is exactly trivial (F_P dimension 1).

**Verdict: WRITTEN_SUPPORTED.**

**Status list in the packet's §2.**
- m = 1: impossible. This is trivial: three mutually orthogonal vectors cannot fit in C².
- m = 3: impossible, by Theorem A.
- m = 5 and m = 7: exist, as verified here.
- Even m: classical edge-colourings exist. This is standard: K_{m,m,m} has even order and is class 1. I corroborated it only numerically, for m = 2 and m = 4.
- "All odd m ≥ 5" is correctly labelled as a conjecture.

## 7. Remaining inputs

- **Input 2 (K666 control JSON).** It records a construction label, the vertex and edge counts 18/108, a source hash and "PASS". It contains no vectors, and its producer is outside the bundle. It is not evaluable. An author PASS is not evidence. No in-scope claim depends on it.
- **Inputs 4 and 5 (author replay), read and hashed only, never executed.**
  - Its zero test is a 60-digit floating Galois-norm product with threshold 1/2. That is sound in principle, because a nonzero algebraic integer has |N| ≥ 1, but it is not exact arithmetic.
  - Its reported booleans and counts (15/21 contexts, 1225 pairs, 5 transversals) agree with my exact results. I used it only as the in-bundle source of the PH7 and PHH integer literals.

## 8. Findings

- **m1 (MINOR, provenance and reproducibility).** The QLS(10) and K777 phase data (PHI2) are not printed in the packet (§1 says "given in the script"). The only in-bundle source is the literals in the author-replay script (input 4). The producer scripts and JSONs whose SHA-256 values the packet pins are outside the frozen bundle, so I have not verified that they define the same objects. This does not affect the existential claims, because the verified objects witness them. It does mean the packet pins are unverified. *Fix:* print PHI2 in the packet, or include the producer data in the bundle.
- **m2 (MINOR, write-up completeness).** Two short load-bearing facts are stated without proof in the bundle:
  - the frame identity (§0);
  - the parity-core embedding φ_L (§0, citing an out-of-bundle packet).
  Corollary A and the Consequence depend on the embedding. Both facts are correct and reconstructed in §3.1 and §3.5. *Fix:* include the two short arguments.
- **m3 (MINOR, notation).**
  - Step 2 uses "w" both for ω = e^{2πi/3} and for a generic vector.
  - "E_b, E_c" denote stars, which clashes with the matrix units E_{μ,λ}.
  - {ξ_a} = {1, w, w²} holds as a set: t = π/3 gives ω² and t = 2π/3 gives ω.
  None of this affects correctness.

There are no FATAL or MAJOR findings.

## 9. Exact dependency list

- **Theorem A.** Elementary finite-dimensional linear algebra only. No imports, pinned data or conditional premises.
- **Corollary A and the Consequence.** Theorem A or Theorem B, plus the embedding lemma (§3.5, elementary).
- **Theorem B and the irreducibility claim.** The pinned data printed in candidate §2. Standard facts: Φ_N is irreducible over Q; the ring of integers of Q(ζ_N) is Z[ζ_N]; a nonzero algebraic integer has a nonzero integer norm; and rank over a residue field is at most rank over the number field.
- **QLS(10) and K777.** Same arithmetic facts, plus the bundle data: packet text for T, T7 and the placement; replay-script literals for PHH and PH7 (m1).
- **Not relied on.** No author PASS claim, no author code execution, no out-of-bundle file.

## 10. Controls and receipts (all reviewer-authored; directory `review-waves/f163-rqls10-quantum-mann-dichotomy/`)

| Artifact | SHA-256 | Bytes |
|---|---|---|
| `rv163-exact-cert-check-v1.py` | `11b1c7f86f080f45c8dd31ada27bedc8acabe9e43cf4efdb762ca7f40008d8a7` | 23555 |
| `rv163-exact-cert-check-v1.json` (output) | `3dc49f3868874945a6e36f7ce78ded41b13807c1f3e44eeee04fba68ef093922` | 5684 |
| `rv163-flat-torus-parity-v1.py` | `153f9a3fb71101c2d6ba1fce4ef8965d9e5a22408321ea4f256023f86f09e25f` | 9962 |
| `rv163-flat-torus-parity-v1.json` (output) | `dd9370eebf46ac293e8c376c34b78ae816d57d6eef16c23713a0c2352cea70f1` | 5159 |
| `rv163-thmA-numeric-v1.py` | `cf73a4dc8ca1a3e25a9091fa6fc635fdc8b1988f9cdc1248da05420c137d1c89` | 7556 |
| `rv163-thmA-numeric-v1.json` (output) | `74334f379cd18d73e7bd3c119b8477bcbfd6863b894f9d0de8c21a69256604bb` | 4279 |

**Run records (native `/bin/date`):**
- **Exact and torus scripts.** Run in one shell command with `/opt/homebrew/bin/python3 -B` (Python 3.14.3, pure-integer code, no third-party imports).
  - Shell clock before: 07:37:49 PDT.
  - Exact script internal clocks: 07:37:49 → 07:37:53.
  - Torus script internal clocks: 07:37:53 → 07:37:53.
  - Shell clock after: 07:37:53 PDT.
  - Both reported `ALL_CHECKS_AS_EXPECTED` with an empty FAILS list.
- **Numeric script.** Run with `/usr/bin/python3 -B` (3.9.6, numpy 2.0.2, scipy 1.13.1).
  - Shell clock before: 07:42:41.
  - Internal clocks: 07:42:41 → 07:43:37.
  - Shell clock after: 07:43:38.

All dates are 2026-10-29, −0700. Each JSON embeds its script's SHA-256, and those values match the pre-run `shasum`. A machine-generated receipt, `rv163-receipts-v1.json` (written by `rv163-receipt-v1.py` after this file), re-hashes all artifacts and this review.

**Controls:**

| Control | Positive cases | Negative cases (intended failure) |
|---|---|---|
| Exact zero tests | 8 known values, M1 = M2 | — |
| Census code | cyclic Z5 = 15, Z7 = 133 | Z6 = 0, Z10 = 0 |
| Commutant code | trivial for K555 and K777 | 82 for one ray, 10 for one ONB |
| Certificates | K555, K777, QLS10 | shifted exponent (18 failures), cloned ray (1 parallel pair), QLS shift (850 pairs) |
| Flat torus | m = 5 and m = 7 solvable | m = 3 all obstructed; m = 5 bipartite T' obstructed; shifted phase rejected |
| Numerics | m = 2, m = 4, m = 5 from certificate | m = 3 floor 0.93 |

## 11. Deviations and disclosures

- **Dry runs before the recorded runs.**
  - I first exercised the function definitions in memory. Neither route wrote files.
    - The exact and torus scripts were tested in the session Python kernel.
    - The numeric script was tested via `/usr/bin/python3 -B -c` `exec` of its definitions-only portion. The first such attempt failed with NameError (`__file__`). The second ran timing trials of `run()` with seed 99 (m = 2: 3 starts; m = 3: 5 starts; m = 4: 2 starts). These gave m = 3 minima of 0.9299 and above, and m = 2 and m = 4 near 0, consistent with the recorded run.
  - After the dry test I added the commutant controls to the exact script, before its single recorded run.
  - Numeric script:
    - I changed its success threshold from 1e-20 to 1e-12 before its first invocation.
    - That first invocation, at 07:40:29 with script SHA `6d27a54d…`, crashed at the gradient-check line (wrong parameter dimension) and wrote no output.
    - I fixed `return fg, 2*E*n` and re-ran it once. That is the recorded run.
- **Executable bit.** The write tool set the executable bit on all four of my scripts, including `rv163-receipt-v1.py`.
- **Interpreters.** Two system interpreters were used (above). Nothing was installed. `-B` was used, and no `__pycache__` was created.
- **Author data.** The PH7 and PHH integer literals were transcribed from the author-replay script, which was read and hashed only. No author code was imported or executed.
- **External source.** I read one named public primary source, the arXiv abstract page of 2603.02334, abstract only.
- **Prohibited actions.** None of the following was used or done: web_search, an external model or paid API, contact with the author, Git, deletion, publication, infrastructure changes, or writing outside this directory.
- **Held material.** No HELD or quarantined material was accessed, including the f161 and f162 materials named in the parent's status-only notices.

## 12. Limits

- The verdicts on Theorem A and Corollary A are a careful same-harness reading of a short written proof. They are not a formal or kernel proof.
- The m = 3 numerics are explicitly weak (see the m = 5 random-start failure). The flat-torus check is ansatz-restricted.
- The exact verdicts certify the objects defined by the bundle's integer data. They do not certify the out-of-bundle producer files.
- No novelty assessment was made.

## 13. Summary

All five inputs matched the manifest byte-for-byte. I found no FATAL and no MAJOR issue, and three MINOR ones: phase data for the QLS(10) and K777 objects exist in the bundle only as replay-script literals; two short load-bearing lemmas are asserted rather than proved; and some notation clashes.

- **Theorem A.** The written proof that L(K3,3,3) has no orthonormal representation in C^6 is correct: frame identity, then Lemma 1's 60° rigidity, then Lemma 2's classicality of 3×3 orthonormal arrays, then the determinant parity (−1)⁹. I reconstructed every step. With the parity-core embedding lemma, which I proved, Corollary A follows.
- **Exact certificates.** My own exact cyclotomic arithmetic (polynomial reduction mod Φ_N and a norm-bounded modular test, cross-checked) confirms:
  - the Z[ζ20] L(K5,5,5) representation: 675/675 orthogonalities, 825 orthogonal pairs, 75 pairwise non-parallel flat rays, and an exactly trivial commutant (the candidate's numerical irreducibility, made exact);
  - the maximal QLS(10): 100 non-parallel rays and exactly five orthogonal transversals, counted by two independent algorithms, so it is not 1-resolvable;
  - the Z[ζ28] L(K7,7,7) representation in C^14.
- **The Consequence.** "Parity core realizable" means precisely that the 15 contexts R0 ∪ C0 ∪ T1 of any Z2-quotient order-10 resolution square admit an orthonormal realization, here an irreducible one. It says nothing about completion. In that sense the consequence follows from Theorem B.
- **Sanity controls.** These are consistent with Theorem A but not evidence for it: numerical searches at m = 3 stall at F ≈ 0.93, while the m = 2 and m = 4 controls succeed; and an exact integer-left-kernel parity argument obstructs all 6 admissible character multisets of the flat Z3²-diagonal ansatz with the Theorem-B incidence.
- **Not reviewed.** Theorem C and the completion-search claims are outside scope.
- **What this review is not.** It is not human, independent-model-family, formal or kernel, or novelty verification.
