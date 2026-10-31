# Review v1 — wave f302-rank2-dual-master-and-core-gram (WRITTEN-ONLY)

Reviewer: ReviewF302Master (fresh disjoint reviewer; no f288 review body/held payload read; only the manifest-named status-only controls were read, as status).
Clocks: pre-body ACK delivered to Main 2026-10-30 04:06 PDT; substantive checkpoints 04:05:32, 04:06:14, 04:17:02 PDT; delivery below.
Hashes verified on disk: manifest 7bdd598f…842380 (6375 B, 123 LF), freeze receipt 4b70bcbf…e16b4 (3757 B, 99 LF), packet 29a2bf12…de8bb3 (23619 B, 234 LF); all six source files hash-stable against the manifest.
Read receipt: entire literal packet read raw in 12 windows of ≤20 LF (1-20,21-40,…,221-234), endings included, no elisions left; read order S1 (erratum-2, L1-19) → S2 (erratum-1, L1-41) → S3 (original master, L1-71) → S4 (selected L31-63 only) → S5 (selected L79-105 only) → S6 (CORE-GRAM, L1-41). S2 machine-verification sentences treated NONINPUT. No code/CAS/interpreter/solver/enumeration/replay; no selected instance privately or publicly (every derivation below is over universally quantified variables); no f288 wave file opened beyond the manifest-listed classification control.

## A. Joint universal duality and constants (S3 §1 + erratum-1 §2 + erratum-2 §1) — SUPPORTED (as corrected)

Reconstructed chain, all written:
- Ky Fan/von Neumann: √S2(X) = max{|Tr(R†X)| : ||R||_F=1, rank R≤2} (trace inequality + extremizer; standard, dimension-free).
- Partial-trace adjointness: Tr(R†X) = ⟨Tr_B R,A⟩_F + ⟨Tr_A R,B⟩_F; traceless A,B pair only with the 4×4 traceless projections x=(Tr_B R)_0, y=(Tr_A R)_0.
- (T2)⇒(∗): scale any traceless pair to L=||A||²+||B||²=1 and instantiate Ky Fan at R/||R||. Valid.
- (∗)⇒(T2): Ky Fan maximum over unit rank≤2 R, each value ≤ √(2L) by (∗). Valid.
- (∗)⇒(Q): for arbitrary R take traceless A=x/√q₀, B=y/√q₀ (q₀=||x||²+||y||²; q₀=0 trivial); (∗) gives q₀ ≤ 2||R||², and q(R)=q₀ identically (below). Valid.
- (Q)⇒(T2): |Tr(R†X)| ≤ √L·√(||x||²+||y||²) [Cauchy–Schwarz in the (A,B) direct sum] = √L·√q(R) ≤ √(2L)||R||_F by (Q); Ky Fan ⇒ S2(X) ≤ 2L. Valid. Key 4×4 identity: ||G_0||²=||G||²−|TrG|²/4 and Tr(Tr_B R)=Tr(Tr_A R)=Tr R, so q(R):=||Tr_B R||²+||Tr_A R||²−|TrR|²/2 = ||x||²+||y||² exactly.
Verdict: (T2) ⟺ (∗) ⟺ (Q) SUPPORTED after the two errata. Erratum-2 §1's diagnosis is correct: erratum-1's displayed √(2L)·√(q(R)) caps at 2√L·||R|| (i.e. S2 ≤ 4L) and did not close the implication; erratum-2's √L·√(q(R)) ≤ √(2L)||R|| closes it.

## B. Residual identity, trace bracket, corrected condition (S3 §2, erratum-1 §1) — SUPPORTED

- (2.1) q(R)=||R||²+B−4(s1²p1+s2²p2)+2s1s2·Re C12: verified by written expansion (Frobenius Gram expansion of both partial traces in the doubly-orthonormal SVD frame, |TrR|²=s1²|c1|²+s2²|c2|²+2s1s2 Re(c1 c̄2), and the pinned rank-one identity ||a_i||²+||b_i||²=1+|c_i|²−4p_i).
- Trace bracket B=s1²|c1|²+s2²|c2|²−|s1c1+s2c2|²/2 ≥ 0: Cauchy–Schwarz (s1c1,s2c2)·(1,1). Verified; also B ≤ ||R||² via |c_i|≤1.
- (2.2′) 2s1s2 Re C12 ≤ ||R||²−B+4P is the exact rearrangement of q ≤ 2||R||²; monotonicity remark (more restrictive when B>0, less when P>0) correct.
- Original published (2.2) (signs of B and P reversed): REFUTED — load-bearing MAJOR, correctly fixed by erratum-1 §1; all readings must use (2.2′).
- Rank-one recovery q ≤ (3/2)||R||² at s2=0: verified. C12=0 paid region q ≤ ||R||²+B ≤ 2||R||²: verified (uses |c_i|≤1 and B≥0).

## C. Rank-one swap identity and traceless region (S4 selected L31-63; antecedent 1) — SUPPORTED

- S4 (2.1) = S5 (4.1): ||u||²||v||²+|⟨v,u⟩|²−||Tr_A|u⟩⟨v|||²−||Tr_B|u⟩⟨v|||² = 4⟨u⊗v,(P_-^A⊗P_-^B)(u⊗v)⟩ ≥ 0. Verified from scratch by coordinate expansion (u,v as m×n coefficient matrices U,V: ⟨u⊗v,F_A(u⊗v)⟩=||UᵀV̄||²_F, ⟨u⊗v,F_B(u⊗v)⟩=||UV†||²_F, ⟨u⊗v,F_AF_B(u⊗v)⟩=|⟨u,v⟩|²; P_-^A⊗P_-^B = (I−F_A)(I−F_B)/4 is an orthogonal projector). Dimension-general.
- S4 (2.2): ⟨v,u⟩=0 ⇒ partial traces traceless and ||Φ(r)|| ≤ ||r||_F. Verified; no product-vector assumption used.
- S4 §3 hollow nuclear decomposition (traceless rank-two, any local dims): Tr M=0 for M=Σ^{1/2}V†UΣ^{1/2}; the 2×2 zero-diagonal unitary exists (Schur [[λ,z],[0,−λ]], expectation λcos2θ+(ze^{iφ}/2)sin2θ, phase opposition + θ∈[0,π/4]; λ=0/z=0 immediate); R=ΣR_i, Tr R_i=0, Σ||R_i||_F=TrΣ=||R||_1; triangle + (2.2) + (s1,s2)·(1,1) Cauchy–Schwarz ⇒ ||Tr_B R||²+||Tr_A R||² ≤ ||R||_1² ≤ 2||R||_F². All verified. Traceless region paid unconditionally (relative to nothing unverified: identity C above is self-contained).

## D. EP region and cross-purity flag (S5 selected L79-105; antecedent 2) — SUPPORTED, flag CLOSED by this review

- EP support splitting: x⊥S ⇒ Hx=Kx=0 (H,K Hermitian parts map S→S and vanish on S⊥) — verified without normality.
- q(H)=λ²(p_u−1/2)+μ²(p_v−1/2)+2λμ(r−1/2) ≤ (3/2)(λ²+μ²)+|λμ| ≤ 2||H||²_F given p_u≤2 (purities ≤1, verified) and r∈[0,1]; H/K Frobenius-and-trace splitting for R=H+iK verified (Hermitian partial traces; ⟨X,iY⟩ purely imaginary).
- Cross-purity sublemma r∈[0,1] (flagged import): DERIVED here in writing. Index identities: Tr(ρ_A(u)ρ_A(v)) = ||Tr_A|u⟩⟨v|||²_F and Tr(ρ_B(u)ρ_B(v)) = ||Tr_B|u⟩⟨v|||²_F (pure coefficient contraction; both directions of the mixed contractions collapse to these squared Frobenius norms). Hence r = ||Tr_A|u⟩⟨v|||²+||Tr_B|u⟩⟨v|||² ≤ ||u||²||v||²+|⟨v,u⟩|² = 1 for orthonormal u,v by C's identity; r≥0 since each term is a squared norm (equivalently PSD pairings). The flag on antecedent 2 is therefore closed relative to the (verified) swap identity.

## E. Core narrowing (S3 §4 / erratum-1 §4) — SUPPORTED items 1–3; item 4 CONDITIONAL

Items 1 (rank two, s2>0, TrR≠0), 2 (non-EP), 3 (C12≠0) follow from the verified paid regions (rank≤1; traceless; EP via D; C12=0 via B). Item 4 (both local support dims ≥3) reduces to the unreviewed import ce6a6288 §2 (support-dim ≤2 block identity; explicitly first-queued); the definition of "local support dimension" is inherited from that packet and is not defined inside the provided ranges. Corrected core statement (erratum-1 §4) correctly uses (2.2′) and asserts no core member exists. Test-projector-side marginal-rank/PPT remarks are explicitly scoped to unreviewed imports and are not verified here.

## F. CORE-GRAM bridge (S6) — SUPPORTED as a conditional theorem; MINOR findings

- G(R,R') is a genuine Hermitian sesquilinear form (operator-space Gram pieces); q(R)=||R||²+|TrR|²/2−G(R,R). Verified.
- Identity (1.1) G(R,R)=4(s1²p1+s2²p2)+2s1s2·Re δ, δ=c1c̄2−C12: verified by written expansion (diagonal c-terms cancel to 4s_i²p_i; cross terms to 2s1s2 Re δ).
- Theorem: CORE-GRAM ⇒ G(R,R) ≥ 4(s1√p1−s2√p2)² ≥ 0 ⇒ q ≤ ||R||²+|TrR|²/2 ≤ 2||R||² (|TrR| ≤ s1+s2 ≤ √2||R||) ⇒ (Q) ⇒ full original T2 via A. All steps verified. Conditional on CORE-GRAM (open, not claimed proven).
- Sharpness/equivalence (S6 §3 first part): for a fixed frame, ∀t=s1/s2>0: G≥0 ⟺ Re δ ≥ −2(tp1+p2/t) ∀t ⟺ Re δ ≥ sup_t[−2(tp1+p2/t)] = −4√(p1p2); AM–GM inf_t(tp1+p2/t)=2√(p1p2) valid for all p_i≥0 (p1p2=0 cases included: threshold 0, sup approached t→∞ or t→0⁺, unattained; p1=p2=0 reads Re(c1c̄2−C12) ≥ 0). Rank-one s2=0 automatic. Hence CORE-GRAM ⟺ G ⪰ 0 on the rank-two cone, uniformly in singular values — EXACT equivalence verified.
- MINOR M1 (S6 L33): "whose right side has infimum −4√(p1p2)" — wrong descriptor; the binding quantity is the supremum of the right side (equivalently −2×inf of tp1+p2/t), attained at t=√(p2/p1) when p1p2>0. Value, attainment ratio, and the equivalence itself are correct.
- MINOR M2 (S6 L37): "that shortcut is stronger than CORE-GRAM" is a mislabel: the CS bound |G(r1,r2)|² ≤ 16s1²s2²p1p2 on rank-one pairs is EQUIVALENT to CORE-GRAM (CORE-GRAM ⇒ G ⪰ 0 on all rank≤2 ⇒ CS on any 2-dimensional span of rank-one operators, since rank(ar1+br2)≤2; conversely the shortcut applied to the SVD frame of any rank-two R gives G ≥ 4(s1√p1−s2√p2)²). The operative warning — not derivable from rank-one positivity alone — is valid and important.
- §4 sufficiency-not-necessity: SUPPORTED. (Q) ⟺ G(R,R) ≥ |TrR|²/2−||R||² pointwise, with right side in [−||R||²,0]; a CORE-GRAM failure at some frame would not by itself refute T2. Necessity of CORE-GRAM holds exactly relative to G⪰0 on rank≤2, not relative to (Q)/T2 — correctly stated.
- Scope note M5: CORE-GRAM is quantified over frames in any C^m⊗C^n although only (4,4) is consumed by the T2 chain; the broader scope serves the (unreviewed) support hierarchy and only strengthens the premise. Harmless.

## G. Withdrawal of original §5 (erratum-2 §2) — SUPPORTED

G is genuinely sesquilinear (F above), so operator-space polarization exists; the original pair-space conjugate-linearity objection attacked the wrong polarization and closed no route. Withdrawal correct. Retained residual — rank-one positivity G(r,r)=4p(r)≥0 alone does not give the rank-two bound in (2.2′); PSD/CS on rank-two spans is the genuine unpaid extension — SUPPORTED (and per M2 the two named options coincide). Sequencing note M4: erratum-1 §1's "§5 unaffected" item is superseded by this withdrawal; the first three "unaffected" items (2.1, B≥0, C12=0 region) remain correct.

## H. Uniformity identities (erratum-1 §3; S3 L17 remark) — identities SUPPORTED; equivalence content UNREVIEWED IMPORT

2/w_d−1/d ≡ −1/4 for d<4 (w_d=8d/(4−d)), d=4 contributing 0−1/4=−1/4 under the zero-scalar-sector convention; hence Σ_factors(2/w_d−1/d) ≡ −1/2 for every (m,n)≤(4,4), mn≥2; likewise 2/w_t−1/m−1/n ≡ −1/2 for w_t=4mn/(2(m+n)−mn). All verified as written algebra (universal in m,n; the five listed dimension tuples are covered by the identity and are not needed). The claim that this makes the (m,n)-statement equivalent to the same inequality (1.1) rests on the pinned general-support packet and the 2x3 pin semantics — UNREVIEWED IMPORT (with ce6a6288), not verified here. MINOR M3: erratum-1's "exact-rational verification … fractions.Fraction" sentences are NONINPUT (manifest) and process-tainted (parent 20261030 control); no mathematical content here depends on them.

## I. Scope and nonclaims — SUPPORTED

All four documents honor: no global/unrestricted T2/T3/Z2/q3, no f274 η>2L, no physical counterexample, no selected parameter, no novelty, quarantined cross-term episode HELD/ZERO/NONINPUT and unused (confirmed unused in the reviewed text), original bytes preserved. The only T2-content offered is the conditional CORE-GRAM theorem.

## Verdict summary

| # | Claim | Verdict |
|---|---|---|
| 1 | (T2)⟺(∗)⟺(Q) with constants √L·√q ≤ √(2L)‖R‖ (post-errata) | SUPPORTED |
| 2 | Original §1 fixed-pair "iff" phrasing | REFUTED (corrected, erratum-1 §2 — SUPPORTED) |
| 3 | Original (2.2) | REFUTED, MAJOR (corrected to (2.2′) — SUPPORTED) |
| 4 | Identity (2.1); B≥0; B≤‖R‖²; rank-one 3/2; C12=0 region | SUPPORTED |
| 5 | Swap identity S4(2.1)/S5(4.1) and S4(2.2) | SUPPORTED (from scratch) |
| 6 | Traceless rank-two paid (hollow nuclear, any dims) | SUPPORTED |
| 7 | EP paid region | SUPPORTED (cross-purity flag closed by written derivation in D) |
| 8 | Core narrowing items 1–3 | SUPPORTED |
| 9 | Core narrowing item 4 (supports ≥3) | CONDITIONAL on unreviewed ce6a6288 §2 |
| 10 | Original §5 route-closure | REFUTED; withdrawal (erratum-2 §2) SUPPORTED |
| 11 | Uniformity weight identities | SUPPORTED (as identities) |
| 12 | Uniform-q support-hierarchy equivalence | UNREVIEWED IMPORT (not verified) |
| 13 | S6 identity (1.1); CORE-GRAM ⟹ G⪰0 ⟹ (Q) ⟹ T2 | SUPPORTED (conditional on CORE-GRAM) |
| 14 | Per-frame t-equivalence, threshold −4√(p1p2), p_i=0 limits, rank-two-cone equivalence | SUPPORTED (M1 wording) |
| 15 | "CS shortcut stronger than CORE-GRAM" | REFUTED as stated (equivalent; M2); warning substance SUPPORTED |
| 16 | Sufficiency-not-necessity of CORE-GRAM for (Q)/T2 | SUPPORTED |
| 17 | Nonclaims/scope discipline | SUPPORTED |

Findings: FATAL none. MAJOR (all in superseded text, dispositioned): original (2.2) signs; original §1 phrasing; original §5 closure; erratum-1 (Q)⇒(T2) constant. MINOR: M1 infimum/supremum wording; M2 "stronger" mislabel; M3 machine-verification sentences noninput/tainted; M4 superseded "§5 unaffected" note; M5 CORE-GRAM over-broad quantification (scope note); M6 item-4 dependence incl. undefined-here "local support dimension".
Conditional claims (final state): full T2 only via CORE-GRAM (open); core item 4 via ce6a6288 §2; support hierarchy via general-support/2x3 imports. Unconditional after this review: equivalence chain, (2.1)/(2.2′)/B/C12=0/rank-one regions, traceless region, EP region (flag closed), CORE-GRAM⟹T2 implication, per-frame equivalence, non-necessity.
Original errors remaining uncorrected: none load-bearing in the operative chain; the byte-frozen original still contains its three errors and must be read only together with erratum-1 and erratum-2 (standing boundary, erratum-2 §3).
