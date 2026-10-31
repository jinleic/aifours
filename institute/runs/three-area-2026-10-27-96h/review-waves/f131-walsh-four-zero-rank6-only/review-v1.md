# Review f131 — four Walsh zeros force polar rank six with zero plane = radical (rank-6-only reduction)

Review wave `f131-walsh-four-zero-rank6-only`, manifest `manifest-v1.json`, SHA-256 `22a65c89524f43b7eb65f3838270b3ab4fcdb1384d0835f1da1519a63049f851` (2252 bytes, verified). Kind: INDEPENDENT SAME-HARNESS SCIENTIFIC REVIEW. Native `/bin/date` observed before writing: **2026-10-29T03:51:13Z (2026-10-28T20:51:13-0700 PDT)**.

Scope limits (binding): this is not a human review, not an independent-model-family review, not formal/kernel verification and not a novelty assessment. No author contact, no web search, no external model or paid API, no Git, no deletion, no publication, no infrastructure change, no repository build/lint/test suites. No held mathematical payload was opened. Authority read for framework only: `contract-addendum-2-frontier-first-owner-direction-v1.json` (SHA-256 `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce`, 3210 bytes, 14 LF). No historical held outcome is used as a premise; every load-bearing premise is listed in §6.

## 0. Inputs (declared order), verified before reading

| # | role | file | SHA-256 | bytes | LF | status |
|---|---|---|---|---:|---:|---|
| 1 | Radical reduction proof | `information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/frontier-20261028-four-zero-radical-reduction-v1.md` | `89ca5480f9c4375cc0a82b313fd66c554941bfc7856bdea3e326935a94eeb229` | 6714 | 63 | match; read completely (`:raw`) |
| 2 | Rank6-only completion | `information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/frontier-20261028-four-zero-rank6-only-v1.md` | `3e6e7572808e287da2ac3d2fb175efd1878ae52e83fa0a5864290aa3a5fc1f37` | 4088 | 43 | match; read completely (`:raw`) |

No primary URLs are declared. Packet 1 cites a non-input file (`frontier-20261028-even-half-four-zero-obstruction-v1.md`, "proves q is quadratic") and author checker scripts; none of these was read or executed. The only claim imported from the non-input file (q quadratic on K) is rederived independently in §2.1, so it is not a dependency of this review.

## 1. Exact setting fixed from the packets

- f : F₂⁹ → {0,1} balanced (|supp f| = 256). The target is "balanced NL242, peak ≤ 28": 2⁸ − 28/2 = 242, so the ambient space is **nine** variables; the manifest scope line and the assignment text say "8-variable", which can only refer to the 8-dimensional even half K below (finding M1).
- W_f(a) = Σ_x (−1)^{f(x)+a·x}. For a ≠ 0, with N_a := |{x ∈ supp f : a·x = 1}|, one has W_f(a) = 4N_a − 512; W_f(0) = 0. Hence k := W_f/4 ∈ ℤ with k(a) = N_a − 128 (a ≠ 0), k(0) = 0.
- T := XOR of supp f, assumed **nonzero**. N_a ≡ a·T (mod 2), so k(a) is even exactly on K := T^⊥ (8-dim, "even half") and odd on the complementary coset.
- q(a) := k(a)/2 mod 2 on K; B(a,b) := q(a+b)+q(a)+q(b) (q(0)=0) its alternating polar; R := rad B; rank B ∈ {0,2,4,6,8}.
- Z₈ := {a ∈ K : k(a) ≡ 0 mod 8}. Always 0 ∈ Z₈ and Z₈ ⊆ {q = 0}.
- Peak ≤ 28 ⇔ |k| ≤ 7, so k ≡ 0 mod 8 ⇔ k = 0: Z₈ is then exactly the Walsh-zero set (zeros cannot lie in the odd half, where k is odd).

## 2. Independent reconstruction (reviewer's own derivations)

### 2.1 q is quadratic on K; bonus: 1_{Z₈} = (1+q)(1+e₄) with e₄ quartic
Write b_x := a·x ∈ {0,1} for x ∈ supp f, so N_a = Σ b_x. By Lucas' theorem, bit j of N_a equals C(N_a, 2^j) mod 2 = e_{2^j}(b) mod 2, the elementary symmetric polynomial of the 256 bits. Hence, as functions of a on all of F₂⁹:
bit₀(N_a) = e₁ = a·T (linear), bit₁(N_a) = e₂ = Σ_{x<y} (a·x)(a·y) (degree ≤ 2), bit₂(N_a) = e₄ = Σ_{x<y<z<w} (a·x)(a·y)(a·z)(a·w) (degree ≤ 4).
On K (a ≠ 0): k = N_a − 128, so q = bit₁(N_a) is quadratic, and Z₈ = {bit₁ = bit₂ = 0}, i.e. 1_{Z₈} = (1+e₂)(1+e₄)|_K has degree ≤ 6 **directly**. This is an independent second route to packet 1's statement 1 (the packets' route via (1)–(3) is verified separately below). The packet's "q quadratic" dependency is therefore discharged inside this review. Also B(a,b) = aᵀGb on K with G = Σ_{x∈supp f} xxᵀ mod 2, which is how the controls realise every rank 0..8 with genuine Boolean functions.

### 2.2 Affine 6-flat energy identity
For any affine 6-flat F = c+M ⊂ F₂⁹ (M 6-dim, M^⊥ 3-dim): Σ_{a∈F} W_f(a)² = 64 Σ_C v_C², where C runs over the 64 cosets of M^⊥ and v_C = Σ_{x∈C} (−1)^{f(x)+c·x} is an 8-term signed sum (even). Σ_C v_C = W_f(c) ≡ 0 mod 4 (balanced; in fact even weight suffices), so an even number of v_C/2 are odd, Σ v_C² ≡ 0 mod 8, and Σ_F k² = Σ_F W²/16 = 4Σ v_C² ≡ 0 mod 32. Packet 1's (1) is the special case F = A ∪ B₀ (A = a+L even, B₀ = a₀+L odd, a₀+a ∉ K ⊇ L, so the union is a 6-flat). Consequently E(A) ≡ −E(B₀) is constant over the 8 cosets of L in K. Remark (not a defect): 6-flats inside K already give the same constancy (and E(A) ∈ {0,16} mod 32), so the odd coset is convenient, not necessary.

### 2.3 Residues (2)
k even ⇒ k² mod 32 ∈ {0 (k≡0 mod 8), 16 (k≡4 mod 8), 4 (k≡2,6 mod 8)}; q=1 ⇔ k ≡ 2 mod 4. With n_q(A)=wt(q|_A), n_z(A)=|A∩Z₈|: E(A) ≡ 4n_q + 16(32−n_q−n_z) ≡ −12n_q − 16n_z ≡ 16(n_q/4 + n_z) (mod 32) once 4 | n_q. For a 5-flat A, q|_A is a quadratic function in 5 variables whose polar is B|_L of rank 0, 2 or 4 with weights in {0,16,32}, {8,16,24}, {12,16,20} respectively (2⁴ ± 2^{4−h} or 16 when the affine part is non-constant on the radical); all are ≡ 0 mod 4. Hence (n_z(A) + n_q(A)/4) mod 2 is constant on K/L for every 5-dim L ≤ K. Call this **H2**.

### 2.4 Coset lemma (3)
On A = a+L, q(a+ℓ) = q(ℓ) + B(a,ℓ) + q(a). If rank(B|_L) ≤ 2 the weight is divisible by 8, so φ_L(a) := n_q(a+L)/4 mod 2 ≡ 0. If rank(B|_L) = 4 with radical ⟨r⟩, choose L = ⟨r⟩ ⊕ L′ (B|_{L′} nondegenerate, bent restriction h_a); then q(a+ℓ′+εr) = h_a(ℓ′) + ε(q(r)+B(a,r)), so the weight is 16 iff c := q(r)+B(a,r) = 1 and 12 or 20 iff c = 0, giving φ_L(a) = 1 + q(r) + B(a,r): affine in a and constant on cosets since B(L,r)=0. Verified identically.

### 2.5 Degree bounds and size bounds
D_L 1_{Z₈}(a) := Σ_{x∈a+L} 1_{Z₈}(x) = n_z(a+L) mod 2 (5th derivative along a basis of L) equals φ_L(a) + const by H2, hence is affine; two further derivatives kill it, so every 7th derivative vanishes and deg 1_{Z₈} ≤ 6. If rank B ≤ 4: for rank(B|_L)=4, dim(L∩R) ≥ 5+4−8 = 1 and L∩R ⊆ rad(B|_L) = ⟨r⟩ forces r ∈ R, so φ_L ≡ 1+q(r) is constant, every 6th derivative vanishes, deg ≤ 5. RM(d,8) minimum weight 2^{8−d} and 0 ∈ Z₈ give |Z₈| ≥ 4, resp. ≥ 8. Verified.

### 2.6 |Z₈| = 4 ⇒ linear 2-plane
For v = x+y with x ≠ y ∈ Z₈: wt(D_v 1_{Z₈}) = 2(4 − |Z₈ ∩ (Z₈+v)|) ≤ 4 < 8 = min weight of a nonzero degree-≤5 function, so D_v 1_{Z₈} = 0 and v is a period. Z₈ = x₀ + (period space) and 0 ∈ Z₈ make Z₈ a linear 2-plane. Verified.

### 2.7 R ⊆ Z₈, rank B ≥ 6, rank 6 ⇒ Z₈ = R
If r ∈ R \ Z₈ (r ≠ 0), pick a 5-dim L ∋ r with L ∩ Z₈ = {0} (extend {r} inside a 6-dim complement of Z₈). Either rank(B|_L) ≤ 2 (φ_L ≡ 0) or rank 4 with radical ⟨r⟩, r ∈ R (φ_L ≡ 1+q(r)); so H2 forces n_z(A) mod 2 constant over K/L. But the four points of the subspace Z₈ lie in four distinct cosets (z+z′ ∈ Z₈ ∩ L = 0), pattern (1,1,1,1,0,0,0,0). Contradiction. So R ⊆ Z₈, dim R ≤ 2, rank B ≥ 6, and rank 6 gives R = Z₈ (both 2-dim). Verified.

### 2.8 Rank 8 excluded (packet 2)
Z₈ = ⟨e₁,e₂⟩ with q = 0 on Z₈ gives B(e₁,e₂) = q(e₁+e₂)+q(e₁)+q(e₂) = 0, a totally singular plane. In a nondegenerate 8-space it extends to a symplectic basis (the packet's "for completeness" sketch is correct: f₁,f₂ with the dual pairings exist because B(e₁,·), B(e₂,·) are independent functionals; f₂ ← f₂ + B(f₁,f₂)e₁ fixes the mutual pairing; the complement is a nondegenerate 4-space). D = ⟨f₁,f₂,e₃⟩ is totally isotropic, L = D^{⊥_B} has dim 5, rad(B|_L) = L ∩ L^⊥ = D, rank(B|_L) = 2, and L ∩ Z₈ = 0 since αe₁+βe₂ ∈ L forces α = B(·,f₁) = 0, β = 0. All 5-flat weights of q are in {8,16,24}, φ_L ≡ 0, and H2 again demands constant n_z-parity against the pattern (1,1,1,1,0,0,0,0). Contradiction. Verified. (Reviewer's reformulation, §2.10, shows why: rank(B|_{L+⟨m⟩}) ≤ 4 for every 6-space over this L.)

### 2.9 Peak bound and counts
With |k| ≤ 7, Z₈ is the Walsh-zero set, so exactly four Walsh zeros ⇔ |Z₈| = 4 ⇒ rank B = 6 and zero set = R. Since q|_R = 0 (Z₈ ⊆ {q=0}) and B(K,R)=0, q(x′+r) = q(x′) with q|_{K′} bent on a 6-dim complement (weight 28 or 36), so |{q=0}| = 4·(36 or 28) = 144 or 112. Points of K with q = 0, k ≠ 0 have k = ±4 (|W| = 16); points with q = 1 have k ∈ {±2, ±6}; the odd half has |W| ∈ {4,12,20,28}. Magnitude-16 count = |{q=0}| − 4 = **140 or 108**. Verified (the packet's "respectively" pairs 112↔108, 144↔140 correctly).

### 2.10 Reviewer reformulation of H2 (used to make the 4-point control exhaustive)
For a 6-dim M ≤ K with hyperplane L and m ∈ M \ L, the difference of H2 over the two L-cosets inside a+M gives Σ_{x∈a+M} 1_{Z₈}(x) = lin(φ_L)(m) = [rank(B|_L)=4]·B(m,r_L). A direct case check (rank(B|_M) = 6 ⇒ every hyperplane has rank 4 with radical v, L = v^⊥∩M, B(m,v)=1; rank(B|_M) ≤ 4 ⇒ the radical generator lies in rad(B|_M)) shows this equals **[rank(B|_M) = 6]** independently of L and m. So H2 ⇔ every sixth derivative of 1_{Z₈} over a 6-space M (on every coset) equals the nondegeneracy indicator of B|_M. Two consequences: (i) two H2-solutions differ by a function with constant 5th derivatives, i.e. by an element of RM(5,8); (ii) the configuration Z = R in rank 6 satisfies every one of these parity constraints (checked by hand for M ⊇ R, M ∩ R = 0, dim(M∩R) = 1, and confirmed exhaustively in Control B), so the packets' method cannot, by itself, decide the rank-6 branch — consistent with the packets' own disclaimers. No existence of a Boolean f realising it is implied.

## 3. Independently written controls (actually run)

Artifacts (all written only in this review directory; no author code imported or executed):

| file | SHA-256 | bytes | LF |
|---|---|---:|---:|
| `reviewer-f131-controls-v1.py` | `03e56190c4eabdf1736584ab6bdb7075d18792d605fe064754a64f5e8c845071` | 27025 | 578 |
| `reviewer-f131-controls-v1-result.json` | `8f351d010f101f35a754bafcc7a8010d8d9cf1bc6768fc7216db1da8af124509` | 20059 | 933 |
| `reviewer-f131-controls-v1-stdout.log` | `6cf9a70f1153a89c83a7efeb9748657f6868bd8caee95a37192a8543e3407783` | 9518 | 32 |

Clock receipts: `/bin/date` before run 2026-10-29T03:49:07Z; in-script start 2026-10-29T03:49:08Z, end 2026-10-29T03:49:30Z (elapsed 22.0 s, Python 3.14.3, numpy 2.4.3, seed 20261028); `/bin/date` after run 2026-10-29T03:49:30Z. The JSON embeds the script's own SHA-256, equal to the file hash above. Enumerations are exact: 97155 five-dim subspaces of F₂⁸ (all 5-dim L ≤ K, via RREF annihilators), 10795 six-dim subspaces of F₂⁸, 788035 six-dim subspaces of F₂⁹ (6304280 affine 6-flats).

### Control A — genuine balanced Boolean functions on F₂⁹, all ranks 0,2,4,6,8 (positive cases)
Ten functions: three uniformly random balanced (rank 8), and hyperplane-plus-swaps constructions realising ranks 0, 2, 4, 6, 8 (G = Σ xxᵀ argument of §2.1), including two "large-D inside a subspace" variants. For every function, all of the following held: T ≠ 0; k parity = a·T on all 512 points; deg q ≤ 2 and all-pairs polar consistency; deg e₄ ≤ 4 and 1_{Z₈} = (1+q)(1+e₄); 0 ∈ Z₈ ⊆ {q=0}; identity (1) with a fixed odd coset: 0 violations over all 97155 L × 8 even cosets; E(A) mod 32 constant per L; all 5-flat weights n_q ≡ 0 mod 4; lemma (3) exact for all rank-4 L (85680 / 80640 / 61440 such L for rank 8/6/4) and φ_L ≡ 0 for all rank-≤2 L; H2: 0 violating L out of 97155; φ_L constant for every L when rank B ≤ 4; deg 1_{Z₈} = 6,6,6,0,2,2,6,6,6,4 (≤ 6 always, ≤ 5 at rank ≤ 4); |Z₈| ≥ 4 (≥ 8 at rank ≤ 4). Affine-6-flat energy ≡ 0 mod 32: exhaustive over all 6304280 flats for two functions (rank 8 random, rank 6 structured), 160000 sampled flats for each of the other eight, 0 violations.

### Control B — abstract model = exactly the packets' hypotheses, exhaustive 4-point search (positive and negative)
For 13 GL(8)-classes of quadratic q with q(0)=0 (rank 0: 0, x₀; rank 2/4/6: Arf 0, Arf 1, and "+ x_{2h}" with nonzero linear part on the radical; rank 8: Arf 0, Arf 1): build the linear system of §2.10 over all 10795 six-spaces and 4 cosets each (43180 equations); solve over F₂. Results for every class: consistent, rank 37 = dim RM(2,8) (so the solution set is exactly g₀ + RM(5,8), and by §2.10(i) it contains every H2-solution); the particular solution g₀ passes the original 5-dim-L form of H2 exhaustively (0 violating L of 97155) and has deg ≤ 6; lemma (3) exact. Then **all** 4-sets {0,z₁,z₂,z₃} (2 731 135 of them) were tested for membership by syndrome against the 37 degree-≤2 monomials, and every hit was re-verified against H2 exhaustively:
- rank 0, 2, 4 (8 classes): **0** four-sets in the solution space (consistent with |Z₈| ≥ 8);
- rank 8 (2 classes): **0** four-sets, even without requiring Z ⊆ {q=0};
- rank 6 with q|_R = 0 (Arf 0, Arf 1): exactly **one** four-set, Z = {0,64,128,192} = R, a linear plane inside {q=0}, 0 H2 violations;
- rank 6 with q|_R ≠ 0: the unique four-set is again R, but R ⊄ {q=0}, so none is admissible (Z₈ ⊆ {q=0} is forced in the real setting).
Random "cubic/quartic/quintic parts": g₀ + (random element of RM(5,8)) kept H2 (0 violations) with deg ≤ 6 in all 13 classes (positive); planting a degree-7 monomial produced 85344 violating L and deg 7 in every class (negative).
Counts: |{q=0}| = 144 (Arf 0) and 112 (Arf 1) for rank 6 with q|_R = 0, giving magnitude-16 counts 140 / 108.

### Packet-specific constructions
- N2 (rank 8, packet 2's L): for **every** totally singular plane (1575 for Arf 0, 1071 for Arf 1) the explicit symplectic extension, D = ⟨f₁,f₂,e₃⟩, L = D^⊥ gave dim L = 5, D ⊆ L, rad(B|_L) = D, rank(B|_L) = 2, L ∩ Z = {0}, Z in four distinct cosets, all eight coset weights ≡ 0 mod 8: 0 failures.
- N1 (rank 6, packet 1's radical-containment witness): among totally singular planes Z′ ≠ R (1890 / 882), 400 sampled per class; for each a 5-dim L ∋ r ∈ R \ Z′ with L ∩ Z′ = 0 was built, r ∈ rad(B|_L), φ_L constant, and the Z′-parity pattern was (1,1,1,1,0,0,0,0): 400/400 witnesses; all 400 also fail the syndrome test, while 1_R lies in the solution space.

### Planted counter-controls violating a hypothesis
- N3 (q not quadratic): adding x₀x₁x₂ to the rank-8 form made 40960 of 97155 five-dim L have a coset weight ≢ 0 mod 4, so n_q/4 and (2) collapse — the quadratic hypothesis is load-bearing.
- N4 (H2 violated): adding one extra point to Z₈ of a real rank-8 function produced 97155 violating L (every L) and degree 8 — the H2 check is sensitive.
- N5 (balancedness violated): an odd-weight f has W ≢ 0 mod 4 at all 512 frequencies, so k is not even an integer.

## 4. Findings

- **FATAL: none.** **MAJOR: none.**
- **MINOR M1 (statement hygiene).** Manifest scope and the review assignment say "8-variable Boolean target"; the packets (correctly, given NL 242 / peak 28) work on F₂⁹ and K is the 8-dimensional even half. Any adopted statement should say "balanced f on nine variables, K = T^⊥ eight-dimensional".
- **MINOR M2 (hypothesis to carry explicitly).** T ≠ 0 is assumed in both packets and is load-bearing (it makes K a hyperplane and k even exactly on K). The reduction as stated does not cover T = 0 (all W_f ≡ 0 mod 8); neither packet claims it does, but the headline sentence "four Walsh zeros force rank six" should carry "with T ≠ 0" (as the Statement section of packet 2 does).
- **MINOR M3 (out-of-manifest reference).** Packet 1's sentence that "the previously displayed rank-four four-zero formal histogram is therefore impossible at every placement" refers to an artifact outside this manifest; it was not read and is not evaluated here. The underlying lemma it invokes (rank ≤ 4 ⇒ |Z₈| ≥ 8) is verified.
- **MINOR M4 (remarks, no action needed).** (a) The odd coset in (1) is not needed: 6-flats inside K already force E(A) ≡ const (indeed ∈ {0,16}) mod 32. (b) Balancedness enters only through W ≡ 0 mod 4 (even weight would do for (1)) and through k(0) = 0 (0 ∈ Z₈, used for nonvanishing). (c) H2 has the cleaner equivalent form D_M 1_{Z₈} ≡ [rank(B|_M) = 6] (§2.10).

## 5. Verdict (scoped)

**VERIFIED (same-harness, written-math + exact finite controls), no FATAL/MAJOR, MINOR M1–M4**, for exactly this statement:

> Let f : F₂⁹ → {0,1} be balanced with T ≠ 0, and suppose max_a |W_f(a)| ≤ 28. If f has exactly four Walsh zeros, then the even-half polar form B has rank 6 and the four zeros are exactly rad(B) (a linear 2-plane in K = T^⊥); ranks 0, 2, 4 and 8 are impossible; |{q = 0}| ∈ {112, 144} and the number of Walsh coefficients of magnitude 16 is 108 or 140 respectively. Without the peak bound the same holds for Z₈ = {k ≡ 0 mod 8} with |Z₈| = 4, and in general deg 1_{Z₈} ≤ 6 (≤ 5 at rank ≤ 4), |Z₈| ≥ 4 (≥ 8).

**Not claimed / not reviewed:** existence or non-existence of a balanced peak-≤28 function with four Walsh zeros; anything about the rank-6 branch beyond the forced structure (the controls show the packets' constraints are satisfiable by Z = R in the abstract model, so the method alone cannot close it); any global statement on NL 242; any novelty; the author checker scripts; the out-of-manifest even-half obstruction file.

## 6. Exact dependencies of the verdict

- D1 f balanced on F₂⁹ (used: W_f ≡ 0 mod 4 everywhere; W_f(0) = 0).
- D2 T := XOR of supp f is nonzero (K = T^⊥ is 8-dimensional; k even exactly on K).
- D3 Peak ≤ 28 (|k| ≤ 7) — only for identifying Z₈ with the Walsh-zero set and for the magnitude-16 count.
- D4 Standard facts used without proof: Lucas' theorem (bits of a popcount are elementary symmetric polynomials mod 2); minimum weight 2^{m−d} of nonzero degree-≤d functions on F₂^m; weights of quadratic functions in 5 and 6 variables (2^{n−1} ± 2^{n−1−h} or balanced); symplectic-basis extension of a totally isotropic subspace in a nondegenerate alternating space; RM(2,8)^⊥ = RM(5,8) (used only for the completeness of Control B's search).
- D5 q quadratic on K — rederived in §2.1 (C(N,2) ≡ bit₁(N)), not imported.

Counterexamples: none found at any rank; all planted hypothesis violations (N3–N5, degree-7 perturbation, extra Z₈ point) were detected by the controls as expected. **END.**
