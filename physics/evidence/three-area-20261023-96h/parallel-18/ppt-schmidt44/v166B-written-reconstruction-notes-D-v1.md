# v166-B reviewer working notes D — v2, v1, parents S222–S236, author checkpoints S237–S240, request S241, preflight S242–S243

Reviewer PhysicsPPT44-2. Preceding `/bin/date`: Tue Oct 27 05:40:59 PDT 2026. Read frontier: ALL 19 literal parts read through every ending (part15 end S222|17 / S223|74 / S224|47; part16 end S235|26; part17 end S241|29; part18 end S242|1313; part19 end S243|2398). WRITTEN reasoning only.

## v2 (S220, 414 LF) — finite rational Robin certificate and constructive short-horizon separation
- Kernel (2) re-derived: K(v,w) = (1/2)e^((v+w)/2) ∫_max^1 (e^(-s) - e^(-(s+1)/2)) ds = (1/2)e^((v+w)/2)(e^(-max/2) - e^(-1/2))^2. Its origin re-derived from the zero-law cascade on the unit interval (E y(s)^2 = ∫ e^(-(s-τ)/2) f(τ)^2 dτ; ∫_τ^1 e^(-(s-τ)/2) ds = 2(1 - e^(-(1-τ)/2))). PASS.
- Robin identity ∫φ^2 = ∫(F'^2 + F^2/4) + F(1)^2/2 and θ = 1/(2Λ1). PASS. Lower bound θ >= 1/384 (f >= s/4, OU variance >= s^3/96). PASS.
- Taylor degree-40 kernel K0, error < 2^-38 < η = 2^-36; Q decreasing via pairing Q39 >= 1 - v/2; Q(1) >= e^(-1/2) (even-degree truncation overestimates). PASS.
- K0 positive via Hilbert–Schmidt factorization; trace <= 1/2. PASS.
- Trace-moment enclosure μ_n <= λ <= μ_n + Tr(H)/n re-derived (n p^(n-1)(1-p) <= 1 - p^n). l = μ - η, ν = μ + 1/(2N) + η; width 2^-31 + 2^-35 < 2^-30; ν/l < 1 + 2^-20 since l > 1/1024. PASS.
- §5 integer formula: cycle contraction, vertex E^2, edge J(higher endpoint), order-simplex integral ∏(j1+…+jk+k)^(-1), F_n = (241n)! divisibility, τ_n = A_n/(2^n D^(6n) F_n^n), μ formula. PASS (never evaluated; positivity from the operator).
- §6 Gaussian gap: E(||Y||^2/q)^2 = 1 + 2s2, ^3 = 1 + 6s2 + 8s3; 1 - E√X >= (E(X-1)^2)^2 / (4E[(X-1)^2(X+1)]) re-derived (1 - √X = (1 - X)/(1 + √X), Cauchy–Schwarz, (√X+1)^2 <= 2(X+1)); E[(X-1)^2(X+1)] = 4s2 + 8s3 <= 12 s2 ⇒ E||Y|| <= √q(1 - s2/12). Tr Γ^2 >= q^3/(8B) (terminal-interval argument); s2 >= 1/1536 when q >= m^2/2; else < m/√2. δ = 1/18432. PASS. Conditioning for L <= h (entire input F_L-measurable before forcing starts at h). PASS.
- §7 Newton brackets: q_(j+1) - g = (q_j - g)^2/(2 q_j); q0 = S >= g; relative error <= 32 S^2 2^(-S-64) <= 2^-58 (S^2 <= 2^(S+1)); m_+ >= m_L >= m_-; m_+/m_- < 1 + 2^-19 < 1 + 1/18432. PASS.
- §8 d midpoint; control-map bound M̄ = d(4L + U), U = 1 + 2L >= √(2L) (deterministic L1 mass 4L, stochastic √(2L)); r = 1 + B*/A*, r^2 A* > B*; G2(F) >= d m_L/√(1 + (M̄/r)^2) > γ for every progressive control; u = 0 literal-feasible. PASS.
- §9 canonical plant: d = (18431 q^2 + 18432 l)/(2·18431 l q), r = 1 + 49 d^2/(d^2 (l/q)^2 - 1); matrices re-checked (A = diag(-1/2,-1/4), B = B0 = (0,1)^T, C = (1/2,0)^T, A0 = [[0,0],[1,0]], D0 = [[0,d],[0,0]], D1 = (0,r)^T); storage 2f^2 + y^2 decays at rate 1/2 with the Itô term. PASS.
- §10 long/infinite direction retained from v1 with the √2 import (see v1 below).

## v1 (S221, 459 LF) — horizon-dependent separation and quantitative bridge
- §2 control-cost exclusion: (2.2) N2 bound; (2.3) N1(S_d u) <= √2 M̄ N1(u) via the continuous monotone Lenglart transfer applied to the causal linear map S_d (input-energy stopping); (2.4)/(2.5) by pointwise Cauchy in (dy, r u). At v1's own date the √2 step is a NAMED Geiss–Scheutzow import (historical NOT_RECONSTRUCTED-PROB-SQRT2 in S231). At the CURRENT union, v22 §§2–3 supplies exactly the continuous nondecreasing adapted case needed here, which I reconstructed; so the import is now paid inside the reviewed union (prospective composition; v1's historical label is not rewritten).
- §3 (3.1) re-derived. §4.1 exit moments E τ = 1, E τ^2 = 5/3, E τ^3 = 61/15 via μ1, μ2, μ3 (μ_j''/2 = -j μ_(j-1), zero boundary) re-derived; v = 2/3, w = 12/5, E√τ <= 103/108. PASS.
- §4.2 OU endpoint |Z_τa| >= a e^(-ε τa); tail energy; N1(Z) >= (a/√(2ε))(1 - ε a^2); finite version with Markov 5/(3R^2) and tail factor 1 - 2^-m; filter error N2(f/c - w) <= p + q ((1 - e^(-κθ))/κ <= p^2, delay set length <= 2h); N1(d y0) >= H a Q. PASS.
- §4.3 strict storage quadratic form re-derived coefficient by coefficient (f^2: (-3η^2 + H^2)/(2c^2); y^2: -εα/(c^2 σ^2) using d^2 = 2εH^2/(c^2 σ^2); cross 2η^2 f v/c). PASS.
- §4.4 constructive rationals re-derived by hand exact arithmetic: H = 64γ/65; κp^2 = 4; 2εU^2 = 578/512; slack 129/16384; η^2 - H^2 = 257γ^2/16900, γ^2 - η^2 = 259γ^2/16900; Q∞ = 507/512; (γ/H) q0 (1 + ρ) = 287885/294912; difference 4147/294912; ratio 22464/22145; 2ε(T - 32a^2) = 8; Q_T = 258137/262144; difference 20153/2359296; ratio 2323233/2303080. PASS (hand exact rational arithmetic, not a program).
- §5 short-horizon conditioning and compact strictness ℓ < m (attainment + non-constant Gaussian norm). PASS. §6 nonconstructive opposite separation. PASS. Short-regime consistency Q_T < 0 when T <= 2h. PASS.
- §7 quantitative bridge (same as v2 §6) PASS; §8 Robin representation (8.2) PASS. The "one next attack" is discharged by v2.

## Parents and process records (S222–S236) — read; consistency with my reconstruction
- S222 model boundary (17 LF): expectation outside path norm; current-state/window F; h >= 0; finite F_t and strict-uniform conventions declared. Used as the frozen model.
- S223 (v21/v25/v26 eight gates + Q1). My notes A remark on v25 §6.1 coincides with Q1. DISCLOSURE: before reading v25 I had already read the S107 summary label "one terminal F_T conditioning MINOR" (part4), so my remark is consistent with but NOT independent of Q1.
- S224 (v16 three gates) consistent with my v16 reconstruction.
- S225–S229 (v15, v14, v13 + addendum, v12, v11) consistent.
- S230 (v9/v10) carries a mandatory MINOR: v9 LF107 "hidden state need NOT have a mean" and v5's "nonexistent full-state expectation" must be read as "the projected proof does not require/take a hidden mean"; under R > 0 and finite N1, v10 Part I proves the finite-prefix mean exists. I did not independently flag this while reading v9; after reading S230 I re-checked v9 LF107 and v10 §3 and concur (wording-level, non-load-bearing).
- S231 (v6/v7/v8 three cores; NOT_RECONSTRUCTED-PROB-SQRT2 at that date). S232 (v4/v5 union), S233 (v3), S234 (v2), S235 (v1), S236 (older proof-v1/reverse-separation/tangent packets; R1 coefficient correction 3/16 → 11/32 in an OLDER packet not in this scope).
- S237 checkpoint 66: Shaikin 2009 at414 pages 1–4 (printed 3–6) pixels: E2/RMS Hilbert norm, not N1; logical point N1(z) <= N2(z) <= γ N2(w) does not give N1(z) <= γ N1(w) (correct). Finite curl/pdftoppm source-acquisition commands disclosed (source-only, not scientific).
- S238 (whole75), S239 (whole84, the v163-A 624 LF return — per S193/v182 HELD, not adopted; ZERO input here), S240 (cp101: thirty findings incl. 16 missed blocked-wait intervals cp85–cp100).
- S241 request v2: gates A1–A4, B1–B3 exactly as reconstructed.
- S242–S243 preflight (2398 LF): metadata header inventory of all 27 inputs (26 bodies + v13 addendum), the 26 whole-version branch scopes, model, request copy, source-import boundaries (Shaikin p5 E2/RMS; Perkowski §2.2 SKETCH; Pardoux failed access; Geiss–Scheutzow bounded reader), quarantines (post56/post60/postS126 ZERO; 163 cp83 self-release assessment ZERO; old 624 RETURN HELD), "v1 v2 old source defects remain historical".

## Named items carried into the review
- NAMED ordinary (not re-proved): scalar Brownian MRT (canonical ONE-Brownian), Hahn–Banach, L1(Ω;H)* = L∞(Ω;H) (coordinate RN), BDG/H1 (author proofs re-derived), linear-SDE moment bounds, Gaussian smoothing regularity (v25 §6.2), inverse-BES(3)/Newtonian potential, Wiener functional representation and strong-solution transition kernels, Cayley–Hamilton/PBH, matrix-ODE continuation, Hilbert–Schmidt compactness, Rayleigh principle, exit-time Dynkin.
- NAMED_NOT_RECONSTRUCTED sources (non-load-bearing after the union): Pardoux–Peng 1990 (failed access), Perkowski notes (prefix sketch), Geiss–Scheutzow full general theorem (only the continuous case is used and is reconstructed in v22), Shaikin 2009 beyond printed pp3–6, Tadmor–Mirkin 2005 (HTTP 418).
- No specialized edge of v1–v26 left unreconstructed at my depth.
