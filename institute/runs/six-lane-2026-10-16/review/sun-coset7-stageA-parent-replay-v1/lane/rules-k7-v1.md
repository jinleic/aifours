# rules-k7-v1: rules for the k = 7 class analysis (general index profiles)

- **Freeze record:** host-clock time and sha256 in `evidence/freeze-v1.sha256`. Corrections go only into new versions.
- **Labels.** [GEN] = proved for arbitrary indices in an accepted predecessor record (sun-coset5 `rules-v1.md` with `rules-v1-erratum-v3.md`; sun-coset5 `proof-v4.md` §5; sun-coset6 `proof-k6-lemmas-v1.md` with `rules-k6-erratum-v3.md`); restated here with explicit hypotheses because the k7 classes mix indices. [NEW] = written in this lane (not a novelty claim), with a full proof here. Nothing in this file is reviewed yet.
- **Units.** μ(X) := |X|/|G| for X ⊆ G.

## §0 Setting

G is finite; U_1, …, U_k ≤ G with n_i = [G:U_i]; the cosets g_1U_1, …, g_kU_k are **pairwise disjoint**. For i ≠ j put
- g_ij = gcd(n_i, n_j), I_ij = [G:U_i∩U_j], α_ij = I_ij / lcm(n_i,n_j) (an integer);
- for a triangle {x,y,z}: γ_y := gcd(n_y, lcm(n_x,n_z)) = lcm(g_xy, g_yz), and ℓ_z := n_z / γ_z.

(γ_y = lcm(g_xy, g_yz) because gcd distributes over lcm.) Imports available inside any subgroup: Sun(t) for t ≤ 6 (README §0). Sun(7) inside a subgroup only for a proper subgroup of a minimal counterexample (README §6).

## §1 Pairwise, triangle, star and count rules

**L0.3 [GEN].** μ(U_iU_j) = α_ij / g_ij and 1 ≤ α_ij ≤ g_ij − 1. Per gcd: g = 2 ⇒ α = 1; g = 3 ⇒ α ∈ {1,2}; g = 4 ⇒ α ∈ {1,2,3}; g = 5 ⇒ α ∈ {1,…,4}; g = 6 ⇒ α ∈ {1,…,5}.

**L1 (T) [GEN, general form].** For a triangle {a,b,c} let L = lcm(n_a,n_b,n_c) and T = [G:U_a∩U_b∩U_c]. Then L | T; put τ = T/L. For every labelling {x,y,z} = {a,b,c}:
- **(T1)** I_xy | Lτ, equivalently α_xy | ℓ_z·τ. *Proof:* I_xy = lcm(n_x,n_y)α_xy, and L = lcm(n_x,n_y)·ℓ_z because lcm(lcm(n_x,n_y), n_z) = lcm(n_x,n_y)·n_z/gcd(n_z, lcm(n_x,n_y)).
- **(T3)** μ(U_y(U_x∩U_z)) = τ / (γ_y·α_xz). *Proof:* by L0.1 it equals Lτ/(n_y I_xz) = Lτ/(n_y lcm(n_x,n_z) α_xz), and L/lcm(n_x,n_z) = ℓ_y = n_y/γ_y.
- **(T2)** μ(U_y(U_x∩U_z)) ≤ min(μ(U_yU_x), μ(U_yU_z)), since U_y(U_x∩U_z) ⊆ U_yU_x ∩ U_yU_z.

Hence τ is a multiple of τ_min := lcm over the three edges of α_xy / gcd(α_xy, ℓ_z), and τ ≤ τ_max := min over apexes y of ⌊γ_y·α_xz·min(α_xy/g_xy, α_yz/g_yz)⌋. **T-kill:** τ_min > τ_max. (Core specialisation: when all indices are d·r_i with r_i pairwise coprime, γ = d and ℓ_z = r_z, recovering the k5/k6 forms.)

**L2/L3 (K) [GEN].** If, for every pair {i,j} ⊆ S (S ⊆ V ∖ {v}), U_vU_i ⊆ U_jU_i or U_vU_j ⊆ U_iU_j, then Σ_{i∈S} α_iv/g_iv ≤ 1 − μ(U_v) < 1. (Proof: sun-coset5 rules-v1 L3; it uses only disjointness.)
- **K1 (links, general).** The pair condition at v for {i,j} holds when μ(U_i(U_v∩U_j)) = μ(U_iU_v), i.e. (T3) at apex i equals (T2)'s bound. Since τ ≥ τ_min, this is forced whenever τ_min·g_iv ≥ γ_i·α_vj·α_iv; then τ is pinned to that value.
- **K2.** U_vU_j ⊆ U_vU_k implies α_vj/g_vj + α_kj/g_kj < 1.

**L4 (P) [GEN].** At v put X_j = U_vU_j. Then μ(X_j) = α_vj/g_vj; μ(X_j∩X_k) is a multiple of u_vjk := 1/gcd(n_v, I_jk) (double cosets of (U_v, U_j∩U_k), L0.4/L0.5); μ(X_j∩X_k) ≥ max(τ_vjk/(γ_v α_jk), μ(X_j) + μ(X_k) − 1, 0); and the Bonferroni inequality Σ_S μ(Y_j) − Σ_{pairs ⊆ S} μ(Y_j∩Y_k) < 1 holds for Y_j = G ∖ X_j. Rounding exactly as in sun-coset6 `CERT-FORMAT-k6-v3.md` (lo = u⌈Lb/u⌉, hi = u⌊min/u⌋, minus u when K2 forbids the forced containment).

**L5 (F) [GEN].** For H ≤ G with [G:H] = m put t_l = [U_l : U_l∩H] and λ_l = n_l t_l / m. Each g_lU_l meets exactly t_l left H-cosets; in each H-coset the pieces are disjoint left cosets in H of subgroups of index λ_l; every subfamily T of the vertices meeting one H-coset has a pair with gcd(λ,λ′) ≥ |T| (Sun(|T|) in H; |T| = 7 only if H < G in the minimal frame). (F3): U_i ⊆ H ⇒ μ(U_iU_l) ≤ t_l/m.

**L6 (XE, general) [NEW].** If U_vU_a = U_vU_b (v, a, b distinct), then W := ⟨U_a, U_b⟩ satisfies U_vW = U_vU_a; W ≠ G; m := [G:W] divides g_ab; α_ab/g_ab ≤ 1/m; and [U_v : U_v∩W] = m·α_va/g_va.
*Proof.* X := U_vU_a = U_vU_b is right-invariant under U_a and U_b, hence under W; 1 ∈ X gives U_vW ⊆ X ⊆ U_vW. μ(X) = α_va/g_va < 1, so W ≠ G. U_a, U_b ≤ W, so m divides n_a and n_b, hence g_ab. U_aU_b ⊆ W gives α_ab/g_ab ≤ 1/m. Finally μ(U_vW) = [U_v:U_v∩W]·μ(W) = [U_v:U_v∩W]/m. ∎
(When g_ab is prime this forces m = g_ab and α_ab = 1, the k6 XE. For g_ab ∈ {4, 6} several m remain; an FH certificate must refute every admissible m.)

## §2 VFC: the vertex fibre count (Lemma R in general form)

**Lemma VFC [GEN for (V1)–(V4); NEW for the count].** Fix v and left-translate so that g_v = 1. For j ≠ v put D_j := U_v g_j U_j. Then:
- **(V1)** D_j ∩ U_vU_j = ∅, and |D_j| = q_j·|G|/g_vj for an integer q_j with 1 ≤ q_j ≤ g_vj − α_vj.
- **(V2)** d_j := |D_j|/|U_j| = q_j·n_j/g_vj is an integer, and every right coset R = U_vy ⊆ D_j meets g_jU_j in a right coset of a subgroup of U_v of index d_j.
- **(V3)** For a right coset R put S_R := {j : R ⊆ D_j}. Every T ⊆ S_R with |T| ≥ 2 contains a pair j ≠ j′ with gcd(d_j, d_j′) ≥ |T|. (|T| ≤ k − 1 = 6, so only imports are used.)
- **(V4)** Each D_j is left U_v-invariant, and ∪_j D_j ⊆ G ∖ U_v.

*Proofs.* (V1): U_v = g_vU_v is disjoint from g_jU_j, so g_j ∉ U_vU_j (L0.2); D_j and U_vU_j are distinct (U_v,U_j)-double cosets. |D_j| = |U_v||U_j|/|U_v ∩ g_jU_jg_j⁻¹| = |G|·[G : U_v ∩ g_jU_jg_j⁻¹]/(n_v n_j), and that index is a multiple of lcm(n_v, n_j), so |D_j| is a positive multiple of |G|/g_vj; D_j ⊆ G ∖ U_vU_j gives q_j ≤ g_vj − α_vj. (V2) and (V4): sun-coset5 proof-v4 §5 (R2, R3). (V3): sun-coset6 proof-k6-lemmas-v1 §1(b): the pieces in R are pairwise disjoint; right-translating by w⁻¹ (w ∈ R) and inverting turns them into pairwise disjoint left cosets in U_v of indices d_j; apply Sun(|T|) in U_v. ∎

**Corollary VFC-count [NEW].** Call T ⊆ V ∖ {v} *allowed* if |T| ≤ 1 or every T′ ⊆ T with |T′| ≥ 2 has a pair with gcd(d,d′) ≥ |T′|. If every allowed set has size ≤ s, then Σ_j q_j/g_vj < s. More generally, for any y ≥ 0 with Σ_{j∈T} y_j ≤ 1 on every allowed T, Σ_j y_j q_j/g_vj < 1.
*Proof.* Each S_R is allowed (V3). Σ_j |D_j| = Σ_R |S_R|·|R| and Σ_j y_j|D_j| = Σ_R |R|·Σ_{j∈S_R} y_j ≤ Σ_R |R| = |∪_j D_j| ≤ |G| − |U_v| (V4). ∎

**Valuations of local indices.** v_p(d_j) = v_p(q_j) + v_p(n_j) − v_p(g_vj). Common prime factors of d_j and d_j′ (j ≠ j′) lie in {2,3,5}: q ≤ 5, and the w-parts are pairwise coprime (README P0(b)).

## §3 Written eliminations used by the README [NEW]

**Lemma D2.** In class (I) type 2 with |C| = 6 and D = {d}: if gcd(n_d, n_i) = 2 for all i ∈ C, there is no CE.
*Proof.* Apply VFC at v = d. For i ∈ C: g_di = 2, so α_di = 1 and q_i = 1, and d_i = n_i/2. For i ≠ j in C, gcd(n_i/2, n_j/2) = gcd(n_i,n_j)/2 = 3. A set of four of these indices has all pairwise gcds 3 < 4, so it is not allowed; allowed sets have size ≤ 3. But Σ_{i∈C} q_i/g_di = 6·(1/2) = 3, contradicting Σ < 3. ∎ (Uses Sun(4) in U_d.)

**Lemma D2′.** In class (I) type 2 with |C| = 5 and D = {d_1, d_2} (so D ⊆ E by README R1b): if C ∩ E = ∅, there is no CE.
*Proof.* VFC at v = d_1. For i ∈ C: g_{d_1 i} = 2 (min e = 1 as e_i = 1), q_i = 1, d_i = n_i/2 = 3^{f_i}5^{g_i}w_i, odd. For i ≠ j in C: gcd(d_i,d_j) = 3 (min f = 1; min g = 0 since a ≤ 1). For d_2: g_{d_1d_2} = 4, |D_{d_2}| = q|G|/4 with 1 ≤ q ≤ 3, and d′ := q·n_{d_2}/4 = q·2^{e_{d_2}−2}5^{g_{d_2}}w_{d_2} (d_2 ∉ A_3).
- If q ∈ {1,2}: gcd(d′, d_i) = 1 for all i ∈ C (d_i is odd; no common 3, since d_2 ∉ A_3 and 3 ∤ q; no common 5, since a ≤ 1). So every right coset inside D_{d_2} has S_R = {d_2}, i.e. D_{d_2} is disjoint from ∪_{i∈C} D_i, and the C-pieces have allowed sets of size ≤ 3. Then μ(∪) ≥ q/4 + (5·½)/3 ≥ 1/4 + 5/6 > 1, contradicting (V4).
- If q = 3: gcd(d′, d_i) = 3 for all i ∈ C, so all six local indices have pairwise gcd 3, allowed sets have size ≤ 3, and Σ q/g = 5/2 + 3/4 = 13/4 > 3, contradicting VFC-count. ∎

**Lemma D3 (partial, K6.3).** In class K6.3 (D = {d} ⊆ A_3 ∖ A_2): if C ∩ E = ∅ and α_di = 2 for at least four i ∈ C, there is no CE.
*Proof.* VFC at v = d. For i ∈ C: g_di = 3, q_i ≤ 3 − α_di, so q_i = 1 when α_di = 2 and q_i ∈ {1,2} when α_di = 1; d_i = q_i·n_i/3 = q_i·2^{e_i}3^{f_i−1}5^{g_i}w_i. With e_i = 1 (C ∩ E = ∅): gcd(d_i,d_j) = 2^{min(1+v_2(q_i), 1+v_2(q_j))} (min f = 1 kills the 3-part; a ≤ 1 kills the 5-part); this is 4 if q_i = q_j = 2 and 2 otherwise. Let Q = {i : q_i = 2}; by hypothesis |Q| ≤ 2. A set with two elements outside Q and any third element has all pairwise gcds 2 < 3, so it is not allowed. Put y_i = 1/4 for i ∈ Q and y_i = 1/2 otherwise. Allowed sets are: subsets of Q (|Q| ≤ 2: sum ≤ 1/2); one element outside Q plus at most two of Q (sum ≤ 1/2 + 1/2); two elements outside Q (sum 1). So y is feasible, and Σ_i y_i q_i/3 = |Q|·(2/3)(1/4) + (6 − |Q|)·(1/3)(1/2) = |Q|/6 + (6 − |Q|)/6 = 1, contradicting VFC-count (which requires < 1). ∎

## §4 Exact certificate representation: capped valuation profiles [NEW]

For each vertex i let its **profile** be π_i = (min(e_i,4), min(f_i,2), min(g_i,2)).

**Lemma CAP.** In a CE, every quantity used by L0.3, L1 (γ, gcd(α,ℓ)), K1, K2, L4 (u = 1/gcd(n_v,I_jk)), VFC (gcd(d_j,d_j′) for q ≤ 5) and L5 (gcd(λ_l,λ_l′) for t ≤ m ≤ 6) is determined by the α's, the q's or t's, and the profiles.
*Proof.* Each quantity is a product over p ∈ {2,3,5} of p raised to a min/max expression in the valuations of the n's and of numbers ≤ 6; the w-parts never contribute (pairwise coprime, coprime to 30, and α, q, t ≤ 6). Recall (README P1(iv)): at most one vertex has e ≥ 3, at most one has f ≥ 2, at most one has g ≥ 2, and every pairwise min is ≤ 2 (for e) and ≤ 1 (for f, g).
- g_ij and γ_y = lcm(g_xy, g_yz) involve only pairwise mins: unaffected by the caps.
- min(v_p(ℓ_z), c_p) with c_2 = 2, c_3 = c_5 = 1 (the largest valuations of α ≤ 5): v_p(ℓ_z) = v_p(n_z) − v_p(γ_z) with v_2(γ_z) ≤ 2 and v_3(γ_z), v_5(γ_z) ≤ 1; if v_2(n_z) ≥ 4 then both the true and the capped value give v_2(ℓ_z) ≥ 2; similarly for p = 3, 5 with cap 2.
- v_p(gcd(n_v, I_jk)) = min(v_p(n_v), max(v_p(n_j), v_p(n_k)) + v_p(α_jk)): if v_p(n_v) is the unique large valuation, the other argument is ≤ 2 + 2 (p = 2) or ≤ 1 + 1 (p = 3, 5), within the cap; if v_p(n_j) is the large one, v_p(n_v) is small and is the min either way.
- VFC: v_p(gcd(d_j,d_j′)) = min(v_p(q_j) + v_p(n_j) − v_p(g_vj), v_p(q_j′) + v_p(n_j′) − v_p(g_vj′)). If n_j carries the unique large 2-valuation, the capped first term is ≥ 4 − min(e_v, 2), and the second term is ≤ 2 + max(0, e_j′ − e_v) ≤ 4 − min(e_v,2) (e_v, e_j′ ≤ 2 here), so the min is unchanged; if n_v carries it, v_2(d_j) = v_2(q_j) does not involve e_v. The same argument with caps 2 works for p = 3, 5 (v_3(q), v_5(q) ≤ 1).
- L5: v_p(gcd(λ_l,λ_l′)) = min(v_p(n_l)+v_p(t_l), v_p(n_l′)+v_p(t_l′)) − v_p(m) with t ≤ 6: if l carries the large valuation, the capped first term (≥ 4 for p = 2, ≥ 2 for p = 3, 5) dominates the second (≤ 2 + 2, ≤ 1 + 1). ∎

**Admissible profiles by class** (from README P0–P1 and §5): C-vertices have e, f ≥ 1, with at most one C-vertex of e ≥ 2 and at most one of f ≥ 2; type-2 D-vertices have f = 0, e ≥ 1 (≥ 2 in K6.2\*, K5.2\*); type-3 D-vertices have e = 0, f ≥ 1; in class (I) at most one vertex has g ≥ 1; in KII, g_x, g_y ≥ 1 with min(g_x, g_y) = 1, f_x = 0, e_y = 0, and C-vertices have g = 0; globally at most one vertex with e ≥ 3, one with f ≥ 2, one with g ≥ 2; and the pairwise gcds computed from the profiles must equal the class's gcd matrix.

A **pattern** of a class is a pair (profiles, α) with α_ij ∈ [1, g_ij − 1]. By Lemma CAP, every rule above is a predicate on patterns, and a rule that kills a pattern kills every CE with that pattern (every admissible τ: rules are upward closed in τ as in sun-coset6 rules-k6-v1 L8 M1; every instance: Lemma CAP).
