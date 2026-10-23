# sun-coset7: Sun's disjoint-coset conjecture at k = 7 in every group — written reduction v1

- **Slot / transition:** math-1, transition 44.
- **Contract (binding):** `institute/runs/six-lane-2026-10-16/screening/math-1-sun-coset7-contract.json`, sha256 59d39ea153ae8f2f416931202b378ae602d822f8943ace878680b132920b6c97 (frozen 13:01:42 PDT).
- **Priority pre-check:** `screening/math-1-sun-coset7-priority-precheck-v1.md`, sha256 9931c83a…70ee. No prior general-group k ≥ 7 claim located (bounded search; not a novelty finding). A prior k = 7 claim stops science immediately.
- **Freeze record:** host-clock time and sha256 in `evidence/freeze-v1.sha256`. Times written inside files are not authoritative.
- **Status of this file:** written mathematics only; no computation was run for it. "[NEW]" means only "written in this lane"; it is not a novelty claim. Nothing here is reviewed yet.

## 0. Target and imports

**Target Sun(7).** Let G be any group, U_1, …, U_7 subgroups of finite index (possibly equal), and g_1U_1, …, g_7U_7 pairwise disjoint left cosets. Then gcd([G:U_i], [G:U_j]) ≥ 7 for some i < j. Sharpness: seven cosets of one subgroup of index 7.

**Imports, used only at these scopes** (contract `accepted_imports`):
- elementary facts on finite-index cores, products and intersections;
- Sun(2) (L0.6 below, re-proved), Sun(3) and Sun(4) (Zhu, Thm 1.1);
- Sun(5) for every group: accepted record `R/sun-coset5-parent-verdict-v1.md`, sha256 2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301;
- Sun(6) for every group: accepted record `R/sun-coset6-parent-gate-verdict-v1.md`, sha256 efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29.

**One lemma imported from inside an accepted record (flagged for the parent).** M-S Prop 4.5 — "(2r_1, 4r_2, 4r_3, 4r_4), r_i pairwise coprime, r_1 odd, is not G-harmonic for any G" — as proved self-contained in sun-coset5 `proof-v4.md` §2. That proof is part of the text of record bound by the k5 verdict 2cf02436… and was accepted by both CLI-family delta reviews of that section. It is used once, in Lemma R1c below. The same statement was also reproduced by the k5 engine control C1 (T/K/P only), which is a sanity check, not evidence.

**Elementary facts used throughout** (G finite; proofs in sun-coset5 rules-v1 L0, which hold for arbitrary indices):
- **L0.1** |XY| = |X||Y|/|X∩Y| for subgroups X, Y.
- **L0.2** gU ∩ hV = ∅ iff g⁻¹h ∉ UV.
- **L0.6 (Sun(2))** If gcd([G:U],[G:V]) = 1 then UV = G, so every left coset of U meets every left coset of V. *Proof:* [G:U∩V] is a multiple of lcm = [G:U][G:V], so |UV| = |G|·[G:U∩V]/([G:U][G:V]) ≥ |G|.
- **Deletion.** Any subfamily of a family of pairwise disjoint cosets is again pairwise disjoint (trivial). So Sun(k) for k ≤ 6 applies to every k-subfamily.

## 1. R0: reduction to finite groups

Let N = ∩_i core_G(U_i). Each core_G(U_i) is the kernel of the action of G on G/U_i, so it has index at most [G:U_i]!; hence N is normal of finite index and N ≤ U_i for all i. Each coset g_iU_i is the full preimage of its image in G/N. Therefore [G:U_i], every [G:U_i∩U_j], and pairwise disjointness are preserved in G/N. From now on G is finite.

## 2. The prime-incidence structure of a counterexample

**Definition (CE).** A *counterexample configuration* is a finite group G with subgroups U_1, …, U_7, elements g_1, …, g_7 such that the g_iU_i are pairwise disjoint and gcd(n_i, n_j) ≤ 6 for all i ≠ j, where n_i = [G:U_i]. Write
  n_i = 2^{e_i} 3^{f_i} 5^{g_i} w_i, with gcd(w_i, 30) = 1,
and put A_p = {i : p | n_i} for p ∈ {2,3,5}, C = A_2 ∩ A_3, E = {i : e_i ≥ 2}, a = |A_5|, D = V ∖ C, where V = {1, …, 7}.

**Lemma P0.** In a CE, for all i ≠ j:
- (a) gcd(n_i, n_j) ≥ 2;
- (b) gcd(w_i, w_j) = 1;
- (c) (min(e_i,e_j), min(f_i,f_j), min(g_i,g_j)) is one of (1,0,0), (2,0,0), (0,1,0), (0,0,1), (1,1,0), and then gcd(n_i,n_j) = 2, 4, 3, 5, 6 respectively.

*Proof.* (a) is L0.6 with L0.2. gcd(n_i,n_j) = 2^{min e}3^{min f}5^{min g}·gcd(w_i,w_j). A prime p ≥ 7 dividing gcd(w_i,w_j) would give gcd ≥ 7, so (b). The remaining factor is an integer in [2, 6] of the form 2^α3^β5^γ, i.e. one of 2, 3, 4, 5, 6, which gives (c). ∎

For i ≠ j put P_ij = {p ∈ {2,3,5} : i, j ∈ A_p}.

**Lemma P1.** In a CE:
- (i) For i ≠ j, P_ij ∈ {{2}, {3}, {5}, {2,3}}. If P_ij = {2}: gcd = 4 when i, j ∈ E, else 2. If P_ij = {3}: gcd = 3. If P_ij = {5}: gcd = 5. If P_ij = {2,3}: gcd = 6.
- (ii) |A_5 ∩ A_2| ≤ 1 and |A_5 ∩ A_3| ≤ 1.
- (iii) For i ≠ j: gcd(n_i,n_j) = 6 iff i, j ∈ C. For i ≠ j in C: min(e_i,e_j) = min(f_i,f_j) = 1. Hence |C ∩ E| ≤ 1 and at most one vertex of C has f ≥ 2.
- (iv) At most one vertex has e ≥ 3, at most one has f ≥ 2, at most one has g ≥ 2.

*Proof.* p ∈ P_ij iff min(v_p(n_i), v_p(n_j)) ≥ 1, so (i) restates P0(c); for P = {2} the gcd is 2^{min(e_i,e_j)} with min ∈ {1,2}, and min = 2 iff both e ≥ 2. (ii): two vertices in A_5 ∩ A_2 would have P ⊇ {2,5}, excluded by (i); same for A_3. (iii): i, j ∈ C gives P_ij ⊇ {2,3}, hence = {2,3} and the triple in P0(c) is (1,1,0). Conversely gcd 6 forces P = {2,3}. Two C-vertices in E would have min e ≥ 2, contradiction; same for f. (iv): P0(c) gives min e ≤ 2, min f ≤ 1, min g ≤ 1 for every pair. ∎

## 3. Theorem R1(7): the class decomposition [NEW]

**Theorem R1(7).** In a CE, a ∈ {0, 1, 2}, and exactly one of the following holds.
- **(I)** a ≤ 1, |C| ≥ 4, and either D ⊆ A_2 ∖ A_3 ("type 2") or D ⊆ A_3 ∖ A_2 ("type 3"). (D = ∅ is allowed.)
- **(II)** a = 2: A_5 = {x, y} with x ∈ A_2 ∖ A_3 and y ∈ A_3 ∖ A_2, and C = V ∖ {x, y}.

*Proof.*
1. **a ≥ 3 forces a = 7, which is impossible.** By P1(ii), at most two vertices of A_5 lie in A_2 ∪ A_3. If a ≥ 3, some x ∈ A_5 lies in neither. For every j ≠ x, P_xj ⊆ {5} and P_xj ≠ ∅ (P1(i)), so j ∈ A_5. Thus a = 7 and every pair has P = {5}, gcd 5. Any six of the seven cosets then contradict Sun(6) (k6 verdict efe1d849…). So a ≤ 2.
2. **a = 2.** Let A_5 = {x, y}. There is j ∉ A_5, and P_xj ≠ ∅ with 5 ∉ P_xj, so x ∈ A_2 ∪ A_3; likewise y. By P1(ii) they cannot both lie in A_2, nor both in A_3. So after naming, x ∈ A_2 ∖ A_3 and y ∈ A_3 ∖ A_2. For every j ∉ {x,y}: P_xj ≠ ∅ and P_xj ⊆ {2} give j ∈ A_2; P_yj ⊆ {3} gives j ∈ A_3. So V ∖ {x,y} ⊆ C, and x, y ∉ C. This is (II).
3. **a ≤ 1.** No pair has P = {5}. By Sun(5) (k5 verdict 2cf02436…), every 5-subset contains a pair with gcd ≥ 5, i.e. (P1) with gcd 6, i.e. (P1(iii)) a pair inside C. Hence every 5-subset of V meets C in at least two vertices, so |V ∖ C| ≤ 3, i.e. |C| ≥ 4.
   - A vertex d ∈ D lies in A_2 ∪ A_3: otherwise P_dj ⊆ {5} would be empty for every j ≠ d (as a ≤ 1), contradicting P1(i). Since d ∉ C, d lies in exactly one of A_2 ∖ A_3, A_3 ∖ A_2.
   - If d ∈ A_2 ∖ A_3 and d′ ∈ A_3 ∖ A_2, then P_dd′ = ∅, contradicting P1(i). So D lies entirely in one of them. This is (I). ∎

**Gcd matrices.** In (I) type 2: C–C pairs gcd 6; D–anything pairs have P = {2}, gcd 2 or 4 (4 iff both endpoints in E). In (I) type 3: C–C 6; every pair meeting D has gcd 3. In (II): C–C 6; x–j gcd 2 or 4 (4 iff x, j ∈ E); y–j gcd 3 (j ∈ C); x–y gcd 5.

## 4. Written eliminations inside (I) [NEW]

**Lemma R1a (type 3, |D| = 3 is impossible).** Take D = {d_1, d_2, d_3} and any i ∈ C. The four cosets of d_1, d_2, d_3, i have all pairwise gcds equal to 3 (§3), contradicting Sun(4) (Zhu). ∎

**Lemma R1b (type 2, |D| ≥ 2 forces D ⊆ E).** Let d ≠ d′ in D and suppose e_d = 1. For every i ∈ C the triple {d, d′, i} has gcd(n_d,n_d′) = 2 and gcd(n_d,n_i) = 2 (P = {2}, min e = 1), so by Sun(3) (Zhu) gcd(n_d′, n_i) ≥ 3, i.e. = 4, i.e. i ∈ E. Then C ⊆ E with |C| ≥ 4, contradicting |C ∩ E| ≤ 1 (P1(iii)). Hence e_d ≥ 2 for every d ∈ D, and then gcd(n_d,n_d′) = 4 for d ≠ d′ in D. ∎

**Lemma R1c (type 2, |D| = 3 is impossible).** By R1b, D = {d_1,d_2,d_3} ⊆ E with pairwise gcd 4, so min(e_{d_s}, e_{d_t}) = 2 for s ≠ t. Since |C ∩ E| ≤ 1 and |C| = 4, pick i ∈ C with e_i = 1. Put r_1 = n_i/2 (odd) and r_{t+1} = n_{d_t}/4.
- gcd(r_1, r_{t+1}) = 1: r_1 is odd, and gcd(n_i, n_{d_t}) = 2 has no odd part (P = {2}), so the odd parts of n_i and n_{d_t} are coprime.
- gcd(r_{s+1}, r_{t+1}) = 2^{min(e_{d_s}, e_{d_t}) − 2}·gcd(odd parts) = 2^0·1 = 1.

So the four disjoint cosets of i, d_1, d_2, d_3 realise (2r_1, 4r_2, 4r_3, 4r_4) with pairwise coprime r's and r_1 odd, contradicting M-S Prop 4.5 (sun-coset5 proof-v4 §2; see §0 flag). ∎

**Lemmas D2 and D2′** (proved in `rules-k7-v1.md` §R, using the vertex fibre count VFC there):
- **D2:** in (I) type 2 with |C| = 6, D = {d}: if gcd(n_d, n_i) = 2 for all six i ∈ C, contradiction.
- **D2′:** in (I) type 2 with |C| = 5, D = {d_1, d_2}: if C ∩ E = ∅, contradiction.

## 5. Exact remaining classes after the written reduction

Every CE belongs to one of the following classes (V = C ⊔ D or C ⊔ {x,y}; "i*" is the unique vertex of C ∩ E when it exists):

| class | definition | gcd matrix |
|---|---|---|
| **K7** | a ≤ 1, C = V | all 21 pairs gcd 6 |
| **K6.2\*** | a ≤ 1, \|C\| = 6, D = {d} ⊆ A_2 ∖ A_3, d ∈ E and C ∩ E = {i*} | C–C 6; d–i* 4; d–(C∖i*) 2 |
| **K6.3** | a ≤ 1, \|C\| = 6, D = {d} ⊆ A_3 ∖ A_2 | C–C 6; d–C 3 |
| **K5.2\*** | a ≤ 1, \|C\| = 5, D = {d_1,d_2} ⊆ (A_2∖A_3) ∩ E, C ∩ E = {i*} | C–C 6; d_1–d_2 4; d_t–i* 4; d_t–(C∖i*) 2 |
| **K5.3** | a ≤ 1, \|C\| = 5, D = {d_1,d_2} ⊆ A_3 ∖ A_2 | C–C 6; d_1–d_2 3; d_t–C 3 |
| **KII** | a = 2 (Theorem R1(7)(II)) | C–C 6; x–y 5; x–j 2, or 4 for j ∈ C ∩ E when x ∈ E; y–C 3 |

Removed so far, with the lemma responsible:
- a ≥ 3 (Sun(6));
- (I) type 3 with |D| = 3, i.e. |C| = 4 (R1a, Sun(4));
- (I) type 2 with |D| = 3 (R1b + R1c: Sun(3) + Prop 4.5);
- (I) type 2 with |C| = 6 and gcd(n_d,n_i) = 2 for all i ∈ C (D2);
- (I) type 2 with |C| = 5 and C ∩ E = ∅ (D2′).

**Known partial overlap.** Menon arXiv:2608.15873 Thm 4.2 states that (3r_1, 3r_2, 6r_3, 6r_4, 6r_5) with r_1, r_2 odd and the r's pairwise coprime is not G-harmonic. Every K5.3 configuration contains such a 5-subfamily (both D-vertices and any three C-vertices; the cofactor coprimality follows from P0–P1). That theorem rests on M-S Lemma 4.6, which is **not** an accepted import. K5.3 therefore stays in the list unless that 5-tuple is certified in this lane (see `FINITE-COVERAGE-k7-v1.md`, stage A) or the parent accepts an audit.

**Not used, and not assumed anywhere:** a common index factor of all seven indices, pairwise-coprime cofactors for all seven, or a "Core6(7)" template. K7 is the only class in which all seven indices are divisible by 6, and it is derived above, not assumed.

## 6. Minimal-counterexample frame (for the fibre rules later)

If Sun(7) fails, choose a CE in a finite group G of minimal order (R0 makes this possible). Then every proper subgroup of G satisfies Sun(7), and every group satisfies Sun(k) for k ≤ 6 (imports). The class decomposition holds in that G, because Theorem R1(7) is proved for each group separately.
