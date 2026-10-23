# rules-k7-addendum-v1: Lemma RPLP-k7, the CAP extension, per-universe CAP hypotheses, FH status and errata

- **Freeze record:** host-clock time and sha256 in `evidence/rules-addendum-v1.sha256`.
- **Responds to:** the parent HOLD relaying the SunK7ReductionAudit findings G1–G5. It was received between 13:49:17 and 13:53:48 PDT; these bounds come from adjacent host-clock tool outputs.
- **Supplements, without modifying,** the following frozen files:

  | file | sha256 |
  |---|---|
  | `rules-k7-v1.md` | 77b9afec… |
  | `README.md` | 2a6d6d6e… |
  | `FINITE-COVERAGE-k7-v1.md` | cbad6fdd… |
  | `CERT-FORMAT-k7-v1.md` | 2c0e4830… |

- **Labels.** [NEW] means written in this lane; it is not a novelty claim. Nothing here is reviewed. Rule references (L0.3, L1, L2/L3, K1, K2, L4, VFC, CAP) are to `rules-k7-v1.md`.
- **Stage C status:** not launched. No Stage C process has run. Stage C stays on HOLD until the parent issues a new GO.

## A1. Lemma RPLP-k7 [NEW; general-index form of sun-coset6 rules-k6-v3 L12]

This is the rule applied as "RPLP" to the 27 X1 leaf orbits (Stage A) and the 528 KII leaf orbits (Stage B). It is implemented in `core7_engine_v1.py` and `core7_engine_v2.py` (`p_bounds`, `forced`, `rplp_vertex`) and is formatted in CERT-FORMAT-k7-v1 §3. The correspondence between this text and the code is for the independent replay to check; it is not established here.

### Setting

As in rules-k7-v1 §0:
- G is finite, with U_i ≤ G and n_i = [G:U_i] for i ∈ V;
- the cosets g_iU_i are pairwise disjoint.

Fix v ∈ V and left-multiply every coset by g_v⁻¹. This keeps the cosets disjoint and changes no index or intersection index, so we may take g_v = 1. Put N = V ∖ {v}, and for j ∈ N:

  X_j := U_vU_j,  Y_j := G ∖ X_j,  D_j := U_v g_j U_j.

### Facts

**(F1)** μ(X_j) = α_vj/g_vj by L0.3. Hence μ(Y_j) = 1 − α_vj/g_vj; this value is what (E2) uses.

**(F2)** D_j ∩ X_j = ∅ and μ(D_j) = q_j/g_vj, for an integer q_j with 1 ≤ q_j ≤ g_vj − α_vj. This is VFC (V1); (E1) uses this value.

**(F3)** X_j, Y_j and D_j are left U_v-invariant. U_vX_j = X_j and U_vD_j = D_j, and complements of left-invariant sets are left-invariant. So each of them is a union of right cosets R = U_vy, and every right coset R is either contained in X_j or contained in Y_j, and either contained in D_j or disjoint from it.

**(F4) Types.** For a right coset R put A_R = {j ∈ N : R ⊆ Y_j} and S_R = {j ∈ N : R ⊆ D_j}.
- S_R ⊆ A_R, by (F2).
- S_R is *allowed* in the sense of Corollary VFC-count, with local indices d_j = q_j·n_j/g_vj. This is VFC (V3). The sets T in it have |T| ≤ |N| ≤ 6, so only Sun(t) for t ≤ 6 inside U_v is used, and these are imports.

**(F5)** A_R = ∅ exactly when R ⊆ ∩_j X_j. U_v is such a coset, since U_v ⊆ U_vU_j for every j. Hence μ(∪_j Y_j) ≤ 1 − μ(U_v) < 1.

**(F6) Pair bounds (L4, restated).** For j ≠ k in N, lo_jk ≤ μ(X_j∩X_k) ≤ hi_jk, where:
- u = 1/gcd(n_v, I_jk) and γ_v = lcm(g_vj, g_vk);
- Lb = max(τ_min(v,j,k)/(γ_v·α_jk), μX_j + μX_k − 1, 0);
- lo = u⌈Lb/u⌉;
- hi = u⌊min(μX_j, μX_k)/u⌋, reduced by u when hi = min(μX_j, μX_k) and the containment that equality needs is barred by K2. That containment is X_j ⊆ X_k if μX_j < μX_k, X_k ⊆ X_j if μX_k < μX_j, and both if the two are equal. K2: X_j ⊆ X_k ⇒ α_vj/g_vj + α_kj/g_kj < 1.

*Proof.*
1. **Grid.** X_j∩X_k is left U_v-invariant and right (U_j∩U_k)-invariant. So it is a union of (U_v, U_j∩U_k)-double cosets U_vz(U_j∩U_k), each of measure [G : U_v ∩ z(U_j∩U_k)z⁻¹]/(n_v·I_jk). That index is a common multiple of n_v and I_jk, so every double coset has measure in (1/gcd(n_v, I_jk))·ℤ = uℤ, and so does μ(X_j∩X_k).
2. **Lower bounds.** U_v(U_j∩U_k) ⊆ X_j∩X_k has measure τ_vjk/(γ_v·α_jk) by (T3) at apex v. This is ≥ τ_min/(γ_v·α_jk) because τ_vjk is a multiple of τ_min (L1). Inclusion–exclusion gives μ(X_j∩X_k) ≥ μX_j + μX_k − 1. Then round up to the grid uℤ.
3. **Upper bound.** μ(X_j∩X_k) ≤ min(μX_j, μX_k), with equality iff the needed containment holds (for finite sets, equal measure plus inclusion gives equality). If K2 bars that containment, the inequality is strict, so on the grid it is at most hi − u whenever hi equals the minimum. ∎

**(F7) Forced containments [NEW in this form].** Let a ≠ b in N and γ_v = lcm(g_va, g_vb). If

  τ_min(v,a,b)·g_va ≥ γ_v·α_ab·α_va,

then X_a ⊆ X_b, equivalently Y_b ⊆ Y_a.

*Proof.* Let τ = τ_vab be the true value, so that [G : U_v∩U_a∩U_b] = lcm(n_v,n_a,n_b)·τ.
1. (T3) at apex v (L1 with y = v and {x,z} = {a,b}) gives μ(U_v(U_a∩U_b)) = τ/(γ_v·α_ab).
2. (T2) at apex v: U_v(U_a∩U_b) ⊆ U_vU_a = X_a, so μ(U_v(U_a∩U_b)) ≤ α_va/g_va.
3. τ is a positive multiple of τ_min (L1), so by the hypothesis μ(U_v(U_a∩U_b)) ≥ τ_min/(γ_v·α_ab) ≥ α_va/g_va.
4. Steps 2 and 3 give equality of measures. The sets are finite with U_v(U_a∩U_b) ⊆ X_a, so U_v(U_a∩U_b) = X_a. (This also pins τ = γ_v·α_ab·α_va/g_va.)
5. Also U_v(U_a∩U_b) ⊆ U_vU_b = X_b. Hence X_a ⊆ X_b. ∎

*Consequence.* If (a, b) is forced and R ⊆ Y_b, then R ⊆ Y_a. So b ∈ A_R implies a ∈ A_R.

*Remark on attribution.* The k6 text (rules-k6-v3 L12; proof-k6-lemmas-v1 §4) attributes the pinning bound to "(T2) at apex w". The bound actually used is the apex-v bound of step 2. This note is for the record only; the accepted k6 files are not modified.

### The vertex LP for one q

For each q ∈ Q_v := Π_{j∈N} {1, …, g_vj − α_vj}, let 𝒞(q) be the set of pairs (A, S) such that:
- ∅ ≠ A ⊆ N;
- S ⊆ A, with S = ∅ or S allowed for the local indices d_j = q_j·n_j/g_vj;
- for every forced pair (a, b) of (F7), b ∈ A implies a ∈ A.

Let q* be the true vector of (F2). Put x(A,S) := μ(∪{R : A_R = A, S_R = S}) ≥ 0. By (F3), (F4) and (F7), x vanishes outside 𝒞(q*), and it satisfies:
- **(E1_j)** Σ_{(A,S): j∈S} x(A,S) = μ(D_j) = q*_j/g_vj;
- **(E2_j)** Σ_{(A,S): j∈A} x(A,S) = μ(Y_j) = 1 − α_vj/g_vj;
- **(B_jk)** ylo_jk ≤ Σ_{(A,S): j,k∈A} x(A,S) = μ(Y_j∩Y_k) ≤ yhi_jk. Here μ(Y_j∩Y_k) = 1 − μX_j − μX_k + μ(X_j∩X_k), and yhi_jk, ylo_jk = 1 − α_vj/g_vj − α_vk/g_vk + hi_jk, lo_jk respectively, by (F6);
- **(TOT)** Σ_{(A,S)} x(A,S) = μ(∪_j Y_j) < 1, by (F5).

### Certificates for one q

A q ∈ Q_v is **refuted** by either of the following.

**(R)** A vector y ≥ 0 on N with Σ_{j∈T} y_j ≤ 1 for every allowed T and Σ_j y_j·q_j/g_vj ≥ 1. If q = q*, this contradicts Corollary VFC-count (rules-k7-v1 §2).

**(P)** Rationals a_j, b_j (free) and u_jk, l_jk ≥ 0 (pairs j < k in N) such that, for every (A,S) ∈ 𝒞(q),

  Σ_{j∈S} a_j + Σ_{j∈A} b_j − Σ_{{j,k}⊆A} u_jk + Σ_{{j,k}⊆A} l_jk ≤ 1   (★)

and

  Obj := Σ_j a_j·q_j/g_vj + Σ_j b_j·(1 − α_vj/g_vj) − Σ u_jk·yhi_jk + Σ l_jk·ylo_jk ≥ 1.

*Why (P) refutes q = q\*.* x ≥ 0 is supported on 𝒞(q*), where (★) holds. So

  Σ x ≥ Σ_{(A,S)} x(A,S)·[LHS of (★)] = Σ_j a_j·E1_j + Σ_j b_j·E2_j − Σ u_jk μ(Y_j∩Y_k) + Σ l_jk μ(Y_j∩Y_k).

Since u, l ≥ 0, (B) bounds the right-hand side below by Obj ≥ 1. This contradicts (TOT).

If the primal system for q is infeasible, Farkas' lemma gives a direction with (★) holding with right-hand side 0 and Obj > 0. Scaled to Obj = 1, it is a (P) certificate, since 0 ≤ 1.

### RPLP-k7 kill

If every q ∈ Q_v is refuted by (R) or (P), then no CE has this pattern. The true q* is one of them; which one is not known, so all must be refuted.

All quantities are rational and are checked exactly, as described in CERT-FORMAT-k7-v1 §3. That section lists the columns, orders, keys and the certificate vector layout.

### Scope and imports

Only the following are used:
- L0.3;
- L1 ((T1)–(T3), τ_min);
- L4 (including K2);
- VFC (V1)–(V4) and Corollary VFC-count, with Sun(t) for t ≤ 6 inside U_v. The imports are Zhu's Sun(3) and Sun(4), Sun(5) via verdict 2cf02436…5301, and Sun(6) via verdict efe1d849…1e29.

Not used: the minimal frame, Sun(7), FH, Prop 4.5, M-S Lemma 4.6 and Menon's results.

The only dependence on τ is through τ ≥ τ_min, in (F6) step 2 and (F7) step 3. So the kill holds for every admissible τ; it is upward closed as in rules-k7-v1 §4.

## A2. Lemma CAP extended to RPLP-k7 (G1) [NEW]

Lemma CAP (rules-k7-v1 §4) also covers every quantity that RPLP-k7 uses. With CAP's bullets numbered 1 to 5 in order (g/γ; ℓ; u; VFC; L5):

| RPLP-k7 quantity | determined by (profiles, α, q) via |
|---|---|
| g_vj, so q_j/g_vj (E1), α_vj/g_vj (F1) and 1 − α_vj/g_vj (E2) | bullet 1 (pairwise minima, unaffected by the caps) |
| the allowed test: gcd(d_j, d_j′) with d_j = q_j·n_j/g_vj | bullet 4 (the VFC gcds, q ≤ 5) |
| the forced test (F7): τ_min(v,a,b), g_va, γ_v = lcm(g_va,g_vb), α_ab, α_va | bullet 1 (g, γ) and bullet 2 (min(v_p(ℓ_z), v_p(α)) in τ_min) |
| lo_jk, hi_jk (F6): u = 1/gcd(n_v, I_jk), τ_min(v,j,k)/(γ_v·α_jk), μX_j, μX_k, and the K2 test | bullet 3 (u), bullets 1–2, and L0.3 (K2 uses only α/g) |
| yhi_jk, ylo_jk | arithmetic in the rows above |
| the column set 𝒞(q) and the vectors in (R)/(P) | the allowed test and the forced test above |

No new arithmetic case arises: each RPLP-k7 quantity is either listed in CAP or a rational combination of listed ones. So RPLP-k7 is a predicate on patterns (profiles, α), quantified over all q ∈ Q_v. ∎

## A3. CAP hypotheses stated per universe (G3) [NEW]

The proof of CAP (rules-k7-v1 §4) uses only three hypotheses on the configuration, for any number of vertices:
- **(H1)** For i ≠ j: min(e_i,e_j) ≤ 2, min(f_i,f_j) ≤ 1 and min(g_i,g_j) ≤ 1; equivalently v_2(g_ij) ≤ 2, v_3(g_ij) ≤ 1 and v_5(g_ij) ≤ 1. Consequently at most one vertex has e ≥ 3, at most one has f ≥ 2, and at most one has g ≥ 2.
- **(H2)** The prime-to-30 parts w_i of the n_i are pairwise coprime.
- **(H3)** Every α and q is at most 5. This is automatic when every g_ij ≤ 6, since α ≤ g − 1 and q ≤ g − α. (t ≤ m ≤ 6 matters only for L5, which no engine uses.)

Under (H1) the capped gcds equal the true gcds, so the profiles reproduce the gcd matrix.

| universe | vertices | hypotheses on the indices | g_ij | (H1) | (H2) | (H3) |
|---|---|---|---|---|---|---|
| X1 | 5 | (3r_1, 3r_2, 6r_3, 6r_4, 6r_5), r_1 and r_2 odd, r's pairwise coprime | 3 if the pair meets {1,2}: gcd(3r_1,3r_2) = 3 and gcd(3r_1,6r_j) = 3·gcd(r_1,2r_j) = 3; 6 for C–C | min e ≤ 1, min f = 1, min g = 0 | w_i divides r_i | g ≤ 6 |
| MSP45 (control) | 4 | (2r_1, 4r_2, 4r_3, 4r_4), r_1 odd, r's pairwise coprime | 2 for P1–P4 (= 2·gcd(r_1,2r_j)); 4 for P4–P4 | min e ≤ 2, min f = min g = 0 | w_i divides r_i | g ≤ 4 |
| CORE5 (control) | 5 | (4r_1, …, 4r_5), r's pairwise coprime | 4 | min e = 2, min f = min g = 0 | w_i divides r_i | g = 4 |
| K52, KII, K62, K63 (and the unrun K53, K7) | 7 | README P0–P1 for the class | in {2,…,6} | README P0(c) and P1(iv) | README P0(b) | g ≤ 6 |

The role domains of CERT-FORMAT-k7-v1 §1 contain every capped profile admitted by these hypotheses, and the enumeration imposes the gcd matrix exactly. The audit's independent count (660 labelled / 115 orbits for X1; 567 / 135 for MSP45; 1331 / 71 for CORE5) agrees with the engine's profiles_total. That agreement checks counts only.

**X1 ⇒ K5.3 (restated).** In a K5.3 CE, take both D-vertices with r = n/3, which is odd since e = 0, and any three C-vertices with r = n/6. The r's are pairwise coprime: gcd 3 between D's gives gcd(r,r′) = 1, gcd 3 between a D and a C gives 3·gcd(r_d, 2r_c) = 3, and gcd 6 between C's gives gcd(r,r′) = 1. By deletion, these five cosets form an X1 configuration in the same group. No minimal frame is needed.

## A4. FH status (G2): UNUSED

- FH (rules-k7-v1 L5 with L6 as the subgroup source; FINITE-COVERAGE §2 item 6) is implemented in neither engine version (v1 e7b4f039…, v2 7ebb0bab…).
- No FH claim or removal is made, and the Stage A and B counts contain no FH kill.
- Before any future use, a new frozen text must fix all of the following:
  - **(a) The hypothesis of L6.** Which pattern data establish U_vU_a = U_vU_b. A sound sufficient condition is α_va/g_va = α_vb/g_vb together with (F7) holding for (a, b): then X_a ⊆ X_b, and the two sets have equal measure.
  - **(b) The admissible m.** m | g_ab, α_ab ≤ g_ab/m, and m·α_va/g_va ∈ ℤ.
  - **(c) The fibre domains.**
  - **(d) The least-order-CE scope.** Any kill that uses Sun(7) in a subgroup (|T| = 7) holds only in a least-order CE. The rules-k7-v1 wording "kills every CE" must be restricted accordingly.

## A5. Errata, deviations and clarifications

- **E1 (G4, cosmetic).** README line 81 reads "proved in `rules-k7-v1.md` §R". It should read **§3**, where D2, D2′ and D3 are proved.
- **E2 (G1).** FINITE-COVERAGE-k7-v1 §2 item 5 says RPLP is "transcribed … by rules-k7-v1 §1". That was false at freeze: rules-k7-v1 contains no RPLP. The written rule is §A1 of this file. Every Stage A and B RPLP kill was computed before §A1 existed, so those kills remain EXPLORATORY.
- **E3 (late certificate format; parent-recorded deviation).** CERT-FORMAT-k7-v1 was frozen at 13:38:43 PDT. That is after Stage A ran (13:35:02–13:35:05) and after Stage B started (13:37:15). The coverage contract required the certificate format to be frozen before counted execution. Consequences:
  - the Stage A and B outputs stay EXPLORATORY;
  - there is no retroactive preregistration;
  - any eventual acceptance needs an independent coverage replay and review.
- **E4 (certificate content versus FINITE-COVERAGE §3).** Engines v1 and v2 deviate from the coverage contract in two ways:
  - they store no per-node certificates (prefix, rule, witness) and no VFC duals keyed by q. They store the killed VFC signatures, duals keyed by LP key, and one line per leaf orbit;
  - a checker must re-walk the tree as CERT-FORMAT-k7-v1 §2 and §5 describe.
- **E5 (G5, clarification of CERT-FORMAT-k7-v1 §5).** The checker must recompute three things itself and treat the stored strings only as values to match:
  - the profile tuples (its own enumeration);
  - every leaf's canonical code (its own stabiliser, built from its own profiles);
  - every LP key (from the entries and q).
- **E6 (status).**
  - **Open:** all six residual classes (K7, K6.2\*, K6.3, K5.2\*, K5.3, KII).
  - **Exploratory:** the Stage A and B results. They are not accepted exclusions.
  - **Not a k = 7 result:** nothing in this lane.
