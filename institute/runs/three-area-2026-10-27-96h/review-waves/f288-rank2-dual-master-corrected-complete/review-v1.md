# F288 review-v1 — corrected universal rank-two dual master reduction (written-only)

Wave: `f288-rank2-dual-master-corrected-complete`
Reviewer: ReviewF288Master (same-harness written review; NOT human, NOT independent-family, NOT formal/kernel, NOT novelty verification).
Manifest SHA256 d7cf69c890164ff7c53fa5cd68b769e7513e35b9bbdf443ba669ff562f8162dd; freeze receipt SHA256 709e2885ac95cf21e19a675d03b0af94d6d2465a1d53588b224040f9e81bf52a; packet SHA256 37d5f35655ccd1e8287a89a5922d69fe87479e797760cdba27e6671d0b86bbd8 (18612 B, 193 LF).

Read order honored: manifest + freeze receipt + 4 status-only controls (STATUS ONLY, no mathematical use), pre-body ACK written (reviewer-prebody-ack-v1.json, clock 2026-10-30T03:36:03-0700 PDT), then S1 (erratum-2, lines 1–19) → S2 (erratum-1, lines 1–41) → S3 (candidate v1, lines 1–71) → S4 (traceless-dual v2, lines 31–63) → S5 (local-2x3 v1, lines 79–105); all 193 packet lines read raw in ≤20-LF windows including endings; no elision remains. WRITTEN_ONLY: no selected instance, no probe, no code/CAS/solver/enumeration/replay was run; only file reads/writes and /bin/date. No prior reviewer body, sibling, author code, quarantined episode or held payload (including f198, the L1 quarantine episode, and the now-HELD f285 return per parent status notice received during review) was opened or used. Machine-verification sentences in S2|3 and S2|27 are NONINPUT per manifest role and parent deviations record 12e118d8…; they are not relied on.

Interim status notice honored: parent message (received during review) holds the f285 block-pair reviewer return and its provisional adoption; not opened, not used; all unreviewed local-support / 2+2 imports stay conditional here.

---

## A. Reconstructed mathematics (written derivations; standard imports named)

### A.1 Ky Fan step and pairing identities (S3|15, S2|17–19, S1|9–11)

Standard imports: Ky Fan max principle in squared form `max{|Tr(R†X)| : ||R||_F=1, rank R≤2} = √(σ1(X)²+σ2(X)²)`; partial-trace adjointness `Tr(R†(A⊗I))=⟨Tr_B R,A⟩_F`, `Tr(R†(I⊗B))=⟨Tr_A R,B⟩_F`; joint Cauchy–Schwarz on (A,B) ⊕-summed.

Key exact identity (d=4): for any G on C⁴, `(G)_0 := G−(Tr G/4)I₄` satisfies `||(G)_0||² = ||G||² − |Tr G|²/4` (orthogonal decomposition), and `Tr(Tr_B R)=Tr(Tr_A R)=Tr R`; hence
`q(R) = ||(Tr_B R)_0||² + ||(Tr_A R)_0||²` — S1|11's parenthetical is exact, and for fixed R the max of the pairing over traceless A,B with `||A||²+||B||²=1` equals `√q(R)` (so q(R) is itself a supremum over all unit-L traceless source pairs; this is the fact behind the withdrawn fixed-pair sentence).

### A.2 Rank-one swap identity (S4|31–43; reused as S5|81–85 (4.1))

Written reconstruction. Write slots A₁B₁A₂B₂ and let F_A (resp. F_B) swap the two A (resp. B) slots; both are self-adjoint involutions and commute. Index computation with U,V the 4×4 matrices of u,v (A rows, B columns) gives the swap-trick identities
`||Tr_A |u⟩⟨v|||_F² = Tr(ρ_A(u)ρ_A(v))`, `||Tr_B |u⟩⟨v|||_F² = Tr(ρ_B(u)ρ_B(v))`, `⟨u⊗v,(F_A⊗I)(u⊗v)⟩ = ||Tr_A|u⟩⟨v|||²`, likewise F_B, and `⟨u⊗v,(F_AF_B)(u⊗v)⟩ = |⟨v,u⟩|²`, `⟨u⊗v, u⊗v⟩ = ||u||²||v||²`. Therefore
`||u||²||v||² + |⟨v,u⟩|² − ||Tr_A r||² − ||Tr_B r||² = ⟨u⊗v,(I−F_A)(I−F_B)(u⊗v)⟩ = 4⟨u⊗v,(P_-^A⊗P_-^B)(u⊗v)⟩`, with `P_-^A=(I−F_A)/2` etc. — exactly S4 (2.1). `P_-^A⊗P_-^B` is an orthogonal projector (tensor product of commuting projectors), so the right side is `4||(P_-^A⊗P_-^B)(u⊗v)||² ≥ 0`. Symbolic cross-check on product vectors u=x⊗y, v=x′⊗y′ gives both sides `(1−|⟨x,x′⟩|²)(1−|⟨y,y′⟩|²)`; identity holds. No product-vector assumption used. If `Tr r=⟨v,u⟩=0`, both partial traces are traceless and (2.1) yields `||Φ(r)||_F² := ||Tr_A r||²+||Tr_B r||² ≤ ||u||²||v||² = ||r||_F²` — S4 (2.2), arbitrary local dimensions. All SUPPORTED.

### A.3 Residual identity for rank-two R (S3|21–41; correction S2|7–11)

Thin SVD `R=s1|u1⟩⟨v1|+s2|u2⟩⟨v2|`, s1≥s2>0, unit frames. Expanding `||Tr_B R||² = s1²||a1||²+s2²||a2||²+2s1s2 Re⟨a1,a2⟩` and similarly A, inserting A.2 for each `||a_i||²+||b_i||² = 1+|c_i|²−4p_i`, and `|Tr R|²/2` with γ=s1c1+s2c2, gives exactly
`q(R) = ||R||_F² + B − 4P + 2 s1 s2 Re C12`, `B := s1²|c1|²+s2²|c2|² − |γ|²/2`, `P := s1²p1+s2²p2` (S3|31,33) — SUPPORTED, exact rearrangement; `p_i ≥ 0` from the projector; `|c_i| ≤ 1` (inner product of unit vectors).

Trace bracket (S3|35): `|γ| ≤ s1|c1|+s2|c2|` (triangle) and `(s1|c1|+s2|c2|²)² ≤ 2(s1²|c1|²+s2²|c2|²)` (Cauchy–Schwarz) give `|γ|²/2 ≤ s1²|c1|²+s2²|c2|²`, i.e. B ≥ 0 — SUPPORTED. Also (not stated but used below): `B ≤ s1²|c1|²+s2²|c2|² ≤ ||R||²`.

Sign correction (S2|7–11): `q ≤ 2||R||²` via (2.1) is equivalent to `2 s1 s2 Re C12 ≤ ||R||² − B + 4P` (2.2′). The published (2.2) `≤ s1²+s2² + B − 4P` has the signs of both B and P flipped. (2.2′) SUPPORTED as the exact rearrangement; original (2.2) REFUTED. The ceteris-paribus remark (2.2′) more restrictive for B>0, less for P>0: SUPPORTED.

### A.4 C12=0 paid region (S3|41)

If C12=0: `q = ||R||²+B−4P ≤ ||R||²+B ≤ 2||R||²`, since P≥0 and `B ≤ s1²|c1|²+s2²|c2|² ≤ s1²+s2² = ||R||²`. SUPPORTED. Minor wording note: the operative fact is `B ≤ ||R||²` from |c_i|≤1; the Lemma B≥0 is not needed. Independent of p_i, γ, EP, supports — as claimed.

Rank-one recovery (S3|37): s2=0 gives `q = s1²(1+|c1|²/2−4p1) ≤ (3/2)||R||²`. SUPPORTED. (Same 3/2 bound independently from A.2: q ≤ 1+|c|²−|c|²/2 = 1+|c|²/2 ≤ 3/2, matching S5|85.)

### A.5 Traceless rank≤2 paid (S4|45–63)

Rank one: A.2. Rank two, Tr R=0: `Tr M = Tr(ΣV†U) = Tr R = 0` for `M=Σ^{1/2}V†UΣ^{1/2}` — SUPPORTED. 2×2 unitary hollowing: Schur-triangularize M to `[[λ,z],[0,−λ]]`; on ψ=(cosθ, e^{iφ}sinθ) the expectation is `λcos2θ+(ze^{iφ}/2)sin2θ`; choose φ so `ze^{iφ}` is antiparallel to λ (both terms then share phase e^{iα}), then match magnitudes via `tan2θ=2|λ|/|z|`, solvable with θ∈[0,π/4]; λ=0 (θ=0) and z=0 (θ=π/4) immediate; the second basis vector has zero diagonal by trace zero — SUPPORTED (my reconstruction confirms the text's instruction is solvable exactly as stated). With `a_i=UΣ^{1/2}w_i`, `b_i=VΣ^{1/2}w_i`: `R=R1+R2` (Σw_iw_i†=I₂); `Tr R_i = w_i†Mw_i = 0`; `||R_i||_F = ||a_i||·||b_i|| = w_i†Σw_i` (both norms equal √(w†Σw)); `Σ_i||R_i||_F = TrΣ = ||R||_1`. Each R_i is traceless rank one, so by (2.2) and Minkowski on the pair norm, `||Φ(R)||_F ≤ ||R1||_F+||R2||_F = ||R||_1 ≤ √2||R||_F`; for traceless R the left side of (1.1) is exactly ||Φ(R)||², giving `q(R) ≤ 2||R||²`. Complete in-packet proof — SUPPORTED, arbitrary local dimensions.

### A.6 EP (range R = range R†) paid (S5|93–105)

If range R = range R† =: S, dim S ≤ 2, then H=(R+R†)/2 and K=(R−R†)/(2i) are Hermitian with ranges ⊆ S, hence Hermitian operators on S — SUPPORTED (this is precisely where EP enters; nonnormal EP included). Spectral form H=λ|u⟩⟨u|+μ|v⟩⟨v|, u⊥v unit (μ=0 or dim S<2 covered). Using A.2's identity ||Tr_X|u⟩⟨v|||² = Tr(ρ_X(u)ρ_X(v)):
`||Tr_B H||²+||Tr_A H||² = λ²p_u+μ²p_v+2λμr` with `p_u=Tr(ρ_A(u)²)+Tr(ρ_B(u)²) ≤ (Trρ_A(u))²+(Trρ_B(u))² = 2` (Tr M² ≤ (Tr M)² for PSD) and `r = Tr(ρ_A(u)ρ_A(v))+Tr(ρ_B(u)ρ_B(v))`; `|Tr H|²/2=(λ+μ)²/2`; so the left side of (1.1) is `λ²(p_u−1/2)+μ²(p_v−1/2)+2λμ(r−1/2)` — matches S5|101.
Bounds on r: upper `r ≤ ||u||²||v||²+|⟨v,u⟩|² = 1` by (4.1) and u⊥v — paid in-packet (S5|99). Lower: r ≥ 0 because `Tr(ρ_A(u)ρ_A(v)) = ||ρ_A(u)^{1/2}ρ_A(v)^{1/2}||_F² ≥ 0` for PSD marginals (and likewise B) — TRUE and elementary, but this half is NOT argued in the packet text; supplied here by the reviewer (see C9 for severity).
Then `2λμ(r−1/2) ≤ |λμ|` (needs both r≤1 for λμ>0 and r≥0 for λμ<0), `λ²(p_u−1/2) ≤ (3/2)λ²`, so `q(H) ≤ (3/2)(λ²+μ²)+|λμ| ≤ 2(λ²+μ²) = 2||H||_F²` since `(λ²+μ²)/2−|λμ|=(|λ|−|μ|)²/2 ≥ 0` — S5|103 SUPPORTED. Splitting for R=H+iK: Tr_A H, Tr_A K Hermitian and `⟨Tr_A H,Tr_A K⟩_F = Tr(G₁G₂) ∈ R`, so cross terms vanish: `||Tr_A R||² = ||Tr_A H||²+||Tr_A K||²` (likewise B and R itself), and `|Tr R|² = (TrH)²+(TrK)²`; hence `q(R) = q(H)+q(K) ≤ 2(||H||²+||K||²) = 2||R||²` — S5|105 SUPPORTED. Remaining-dual-premise sentence (nonnormal/non-EP, rank two, nonzero trace) consistent with S3|59.

### A.7 Double-universal equivalence and constants (S2|13–19 corrected by S1|5–11)

(T2)⇒(∗): for traceless A,B and any rank≤2 R, `|Tr(R†X)| ≤ √(σ1²+σ2²)·||R|| ≤ √(2L)||R||` by (T2) and Ky Fan; `Tr(R†X)=⟨Tr_B R,A⟩+⟨Tr_A R,B⟩` — gives (∗) with constant 2. SUPPORTED.
(∗)⇒(Q): fix R; `A=(Tr_B R)_0/√N`, `B=(Tr_A R)_0/√N`, `N=q(R)` (both projections traceless); (∗) gives N ≤ 2||R||², i.e. q(R) ≤ 2||R||². SUPPORTED (boundary N=0 trivial).
(Q)⇒(T2): erratum-1's display `√(2L)·√(q(R))` follows only from splitting the two pairings (‖a‖+‖b‖ CS), and its best conclusion is `S2(X) ≤ 4L` — insufficient; erratum-1's chain REFUTED as a proof of the implication. Erratum-2's corrected joint chain `|⟨(Tr_B R)_0,A⟩+⟨(Tr_A R)_0,B⟩| ≤ √L·√(q(R)) ≤ √(2L)||R||` (joint Cauchy–Schwarz on the (A,B) pair, then (Q)) gives `|Tr(R†X)|² ≤ 2L||R||²` for all rank≤2 R, and Ky Fan over Frobenius-unit rank≤2 R gives `S2(X) ≤ 2L` — SUPPORTED, exact constants √L, √2, 2.
The original fixed-pair "iff" sentence (S3|15, "T2 holds for a pair iff … for its maximizing R") is REFUTED: q(R) is a supremum over all unit-L traceless source pairs (A.1) and a single pair's T2 bounds nothing about unrelated R; the two universal suprema must be exchanged through the joint universal (∗), exactly as S2|15–17 states. SUPPORTED after correction.

### A.8 §5 route-impossibility (S3|65–67) and its withdrawal (S1|13–15)

Define on operator space (Frobenius inner product) the Hermitian operator `𝒢 = Id − (Tr_A)†(Tr_A) − (Tr_B)†(Tr_B) + |Ĩ⟩⟨Ĩ|` (Ĩ the normalized identity functional): `G(R,R) = ⟨R,𝒢R⟩ = ||R||²+|TrR|²−||Tr_B R||²−||Tr_A R||²` is the diagonal of a Hermitian sesquilinear form — S1|15's statement is correct, and for rank-one r, `G(r,r) = 1+|c|²−||b||²−||a||² = 4p(r) ≥ 0` by A.2. Hence the original §5 "structurally unavailable / non-sesquilinear / closes the single-pair-polarization route" claim is REFUTED (its conjugate-linearity objection concerns vector-pair polarization, not the operator-space form); erratum-2's withdrawal is mathematically correct. Retained scoping claim — rank-one diagonal positivity alone does not establish the rank-two bound in (2.2′); PSD (or the needed Cauchy–Schwarz) of 𝒢 on rank-two spans is unpaid; no impossibility of any strength — SUPPORTED as a scoping statement. Erratum-1's "§5 unaffected" remark (S2|11, last item) is superseded by this withdrawal (bookkeeping, read order S1 first).

---

## B. Per-claim verdicts (LF citations = packet labels S#|line)

| # | Claim (source) | Verdict | Severity | Imports / boundaries |
|---|---|---|---|---|
| C1 | Original S3|15 fixed-pair "iff" (maximizing R) | REFUTED (correctly identified by S2|15) | MAJOR (original error) | none |
| C2 | Joint universal (∗) and (T2)⟺(∗)⟺(Q) (S2|17,19) | SUPPORTED (A.7) | — | Ky Fan max principle, joint CS; standard |
| C3 | Erratum-1 (Q)⇒(T2) chain √(2L)·√q (S2|19) | REFUTED as proof (best gives S2≤4L; S1|7 diagnosis accurate) | MAJOR | none |
| C4 | Erratum-2 corrected chain √L·√q ≤ √(2L)‖R‖, S2(X)≤2L; "hence |Tr(R†X)|²≤2L‖R‖²" (S1|9–11) | SUPPORTED (A.7) | — | joint CS; q(R)=‖(Tr_B R)_0‖²+‖(Tr_A R)_0‖² (d=4) exact |
| C5 | Rank-one swap identity (2.1)/(2.2) (S4|35–43; S5|83 (4.1)) | SUPPORTED (A.2, full reconstruction) | — | none (self-contained; standard swap algebra) |
| C6 | Trace bracket B≥0 (S3|35) | SUPPORTED (A.3) | — | triangle + CS |
| C7 | Residual identity (2.1) (S3|31,33) | SUPPORTED (A.3) | — | imports C5 (in-packet) |
| C8 | Original (2.2) signs (S3|39) | REFUTED; corrected (2.2′) 2s1s2ReC12 ≤ ‖R‖²−B+4P (S2|9) SUPPORTED; monotonicity remark (S2|11) SUPPORTED | MAJOR (original error) | none |
| C9 | EP cross-purity r∈[0,1] (S5|97,99) | SUPPORTED as mathematics, with gap: r≤1 paid in-packet ((4.1)+u⊥v); r≥0 true (PSD: Tr(ρσ)=‖ρ^{1/2}σ^{1/2}‖²≥0) but not argued in packet | MINOR (source-text gap; closed by reviewer's elementary argument — does NOT retroactively correct S5 text) | none beyond A.2 |
| C10 | EP paid region, H/K split, conclusion (S5|93–105) | SUPPORTED (A.6) | — | C5, C9, spectral theorem, Tr(G₁G₂)∈R |
| C11 | Traceless rank≤2 paid, hollow nuclear decomposition (S4|47–63) | SUPPORTED, complete in-packet proof (A.5) | — | C5; Schur 2×2; CS on (s1,s2) |
| C12 | Rank-one recovery q≤(3/2)‖R‖² (S3|37; S5|85) | SUPPORTED (A.4) | — | C5 |
| C13 | C12=0 paid region (S3|41) | SUPPORTED (A.4) | MINOR wording ("by the Lemma": operative fact is B≤‖R‖² from |c_i|≤1, not B≥0) | none |
| C14 | Original §5 structural impossibility (S3|65–67) | REFUTED (G is a Hermitian sesquilinear form's diagonal); withdrawal (S1|15) correct; retained scoping claim SUPPORTED | MAJOR (original false claim, withdrawn) | none |
| C15 | Uniformity identities: per-factor 2/w_d−1/d=−1/4, Σ_factors = −1/2 (S2|23–25); consistency 2/w_m+2/w_n=2/w_t with S3|17 w_t | SUPPORTED as written algebra (identically true, incl. d=4 zero-scalar convention) | — | none |
| C16 | Uniform support-size equivalence ("same q-shape governs every support", S3|17; "exact statement behind the uniform q", S2|25–27) | INCONCLUSIVE as paid — CONDITIONAL import: the underlying support-equivalence proofs (2x3 file outside lines 79–105; "general-support checkpoint 2310") are outside the packet | import boundary (not an error; S2|31–37 styles antecedents unreviewed) | OUT-OF-PACKET |
| C17 | Local support dim ≤2 paid region (S3|50; S2|35) | INCONCLUSIVE as paid — CONDITIONAL import ce6a §2 (SHA ce6a6288…), "FIRST QUEUED REVIEW", outside packet | import boundary | OUT-OF-PACKET |
| C18 | §4 core requirements (S3|56–63): (1) TrR≠0, s2>0; (2) non-EP; (3) C12≠0; (4) both local supports ≥3 | (1)(2)(3) SUPPORTED as paid exclusions (C11, C12, C13, C10); (4) CONDITIONAL on C17. "No member asserted to exist" honored; test-projector sentence explicitly at unreviewed ce6a scope (S3|63) | — | (4) OUT-OF-PACKET |
| C19 | Corrected core statement: violation ⟹ 2s1s2·ReC12 > ‖R‖²−B+4P (S2|37) | SUPPORTED (exact rearrangement of q>2‖R‖² via (2.1)) | — | C7, C8 |
| C20 | Machine-verification claims (S2|3 fractions.Fraction; S2|27 "verified by exact rational arithmetic") | NONINPUT (excluded per manifest role note and parent deviations record 12e118d8…); no mathematical weight rests on them here since C15 is formal algebra and C4/C8 are reconstructed | process (already parent-classified) | excluded |
| C21 | Nonclaims / scope honesty (S1|19; S2|41; S3|71): no unrestricted T2/T3/Z2/q3, no f274 η, no counterexample, no novelty; header "reduces the entire original T2 to one dimension-uniform inequality, proves that reduction exactly" (S3|3) | SUPPORTED for the (4,4) reduction T2⟺Q after corrections (C2, C4); the "dimension-uniform" part is CONDITIONAL (C16). No full T2/q3/η assertion found anywhere in the corrected reading | — | — |

## C. Conditional inputs and NONINPUT (exact boundaries)

Conditional (unpaid from this packet): (i) uniform support-size equivalence / per-support q-shape (S3|17; S2|23–27) — proofs outside packet; (ii) local support dim ≤2 paid region, hence core requirement (4) (ce6a §2); (iii) all §3 table pins cited by hash only (test-projector side: 12a2a6f4…, 2961f2d5…, ef80f84a…, bb09c6bf…, b96fcf9f…/a6a3effd…) — not reviewed here, no adoption. NONINPUT: f198 false lemma; quarantined cross-term episode; L1/quarantine controls; machine-verification sentences; prior reviewer bodies; f285 return/disposition/outcome (held by parent notice during review); author code.

## D. Overall disposition

1. The corrected core of the master reduction reconstructs completely from the literal packet: the double-universal equivalence (T2) ⟺ (∗) ⟺ (Q) with exact constants (C2, C4), the exact rank-two residual identity with corrected signs (C7, C8), and the four in-packet paid regions rank≤1 (C12), TrR=0 (C11), EP including nonnormal EP (C10, with C9's noted gap), C12=0 (C13).
2. The original v1 errors remain errors and are not retroactively corrected by the errata: fixed-pair iff (C1, MAJOR), (2.2) sign reversal (C8, MAJOR), §5 false route-impossibility (C14, MAJOR); erratum-1's own (Q)⇒(T2) constant defect (C3, MAJOR) was real and is cured only by erratum-2.
3. Unpaid/conditional: uniform support-size equivalence (C16), local-support≤2 and hence core requirement (4) (C17, C18). The core inequality itself (existence or nonexistence of a violating rank-two operator) remains open; no core member is asserted.
4. No FATAL finding in the corrected corpus; no full T2/T3/Z2/q3, f274 η, physical counterexample, or novelty is asserted or granted. This is a same-harness written reconstruction only.
