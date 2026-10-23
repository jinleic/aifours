# Hostile mathematics audit: k6 rule delta (L9–L12, erratum v1, CERT-FORMAT v1)

**Scope.** I re-derived everything by hand from the inlined texts. No code, run, count or survivor list was supplied, and none was audited (that includes the 263 orbits at SOURCE01:5). Nothing here says any pattern dies. No k6 theorem, survivor claim or novelty is asserted. This is one Claude-family review.

**Bottom line.** I found no FATAL defect. Each rule in the delta is a valid necessary condition for every genuine Core5(6) configuration in the minimal frame. That covers all admissible τ, all pairwise-coprime r (including r_i = 1, arbitrary prime powers and primes ≥ 7), every coincident or absent marker, every q and all seven E5 placements. Two qualifications:
- L11 has one MAJOR proof gap. The claim is true, and the repair is given below.
- CERT-FORMAT is sound predicate by predicate, but it needs explicit validation clauses.

| Component | Verdict |
|---|---|
| L9 hereditary Sun | ACCEPT-WITH-FIXES (MINOR) |
| L10 XE | ACCEPT |
| L11 N2-6 | ACCEPT-WITH-FIXES (1 MAJOR proof gap, repaired here; 1 MINOR) |
| L12 RPLP | ACCEPT |
| Erratum v1 | ACCEPT-WITH-FIXES (MINOR) |
| CERT-FORMAT v1 | ACCEPT-WITH-FIXES (required checker clauses) |

## 1. L9 (SOURCE00:8–34; SOURCE02:28–66)

**Verified.**
- **(a) Left cosets of H.**
  - The piece is g_lU_l ∩ C = y_l(U_l∩H).
  - Translating by z⁻¹ gives left cosets in H of index λ_l = 5r_lt_l/5 = r_lt_l.
  - Disjointness passes to every subset T.
- **(b) Right cosets of U_v.**
  - The piece is A_jw_j, with A_j = U_v ∩ w_jU_jw_j⁻¹.
  - [U_v:A_j] = |U_vw_jU_j|/|U_j| = d_j = q_jr_j, independent of w.
  - c_j = w_jw_0⁻¹ lies in U_v, and inversion gives disjoint left cosets c_j⁻¹A_j.
- **Which Sun is used.**
  - In U_v: L0.6, Zhu, and the accepted Sun(5), since |T| ≤ |N| = 5.
  - Sun(6) appears only in (a), and only when all six vertices meet one coset.
- **Exactness of maxgcd and fgcd.**
  - Common primes of q_jr_j and q_kr_k lie in {2,3}, since q ≤ 4.
  - Common primes of r_lt_l lie in {2,3,5}, since t ≤ 5.
  - A prime ≥ 7, or a second marked cofactor, never contributes.
  - For class-2 E2, E3 and E5, the minimum saturates at the partner's t- or q-part: v₂ ≤ 2 ≤ v₂(r), and v₃, v₅ ≤ 1 ≤ v_p(r). Class 1 is exact.
  - So maxgcd and fgcd equal the true gcd for every instance. The test is upward-closed in each gcd anyway.
- **Family relation.**
  - The hereditary family lies inside the v1 family (take T = the pairs, then T = S), and it is downward closed.
  - Every removed column and every extra rejection is justified pointwise.
  - "Maximal sets suffice" still holds.

**Findings.**
- **MINOR SOURCE00:10, 23.** The statement imports the L5 setting (H ≤ G), but step 3 relies on "H is proper".
  - With H = G, the case |T| = 6 is Sun(6) for G itself, which is circular.
  - Fix: put "H < G whenever |T| = 6" into the statement. E4 (SOURCE03:30–32) amends only v1 L5.
  - Also SOURCE02:31: "|S| = 6 is used" should read "|T| = 6".
- **MINOR SOURCE02:62–66.** Exactness is proved only for setting (b). Add the FH5 case explicitly, citing SOURCE03:36–38, including p = 5: v₅(t) ≤ 1 ≤ v₅(r_E5).

## 2. L10 XE (SOURCE01:7–19; SOURCE02:68–83)

Every step checks:
- X·U_j = X·U_k = X, so XW = X.
- U_v ⊆ X, so X = U_vW.
- α_vj ≤ 4, so W ≠ G.
- U_j, U_k ≤ W, so [G:W] divides gcd(5r_j, 5r_k) = 5.
- μ(U_jU_k) ≤ μ(W), so α_jk = 1 and U_jU_k = W.
- The product formula gives [U_v:U_v∩W] = α_vj, and hence also α_vj = α_vk.

Equal subgroups (r = 1) are a consistent special case. **No findings.**

Optional, sound strengthening: in P and RPLP, when x_j = x_k and α_jk ≥ 2, XE bars equality. So hi may drop by u even when both K2 inequalities hold.

## 3. L11 N2-6 (SOURCE01:21–46; SOURCE02:85–119)

**Verified.**
- **Step 1.**
  - (T1) on edge jk, which is opposite v, gives α_jk | r_vτ_vjk.
  - gcd(r_v, α_jk) = 1, so τ_vjk ≥ α_jk and μ(Z_jk) ≥ 1/5.
  - Granularity (L0.4/L0.5): gcd(5r_v, 5r_jr_kα_jk) = 5·gcd(r_v, α_jk) = 5.
  - XE is genuinely needed: K2 permits X_j ⊆ X_k when α_jk = 2, since 2 + 2 ≤ 4.
  - Hence μ(X_j∩X_k) = 1/5 = μ(Z_jk).
- **Step 2.**
  - Q is a multiple of 5r_jr_k·lcm(r_lτ_jkl, r_vτ_vjk).
  - Given gcd(r_v, τ_jkl) = 1, this gives Q ≥ r_v[G:W] and μ(U_vW) ≥ 1/5.
- **Step 3.**
  - Pairs sharing a vertex share a triple, and disjoint pairs chain through a third pair.
  - The count is 1/5 + 5·(1/5) = 6/5 > 1.

**MAJOR (proof gap; the claim is true): SOURCE01:42; SOURCE02:93, 109, 119.**
- "τ involves only the primes 2 and 3" is asserted, not proved.
- (T1) and (T2) alone give only τ_min | τ ≤ τ_max ≤ 16. A priori that admits 5, 7, 10 and 14.
- The claim is load-bearing exactly where the certificate carries no data: v = E5, and primes ≥ 7 in r_v.

Repair, which I verified:
- For j, k, l ≠ v, all three α lie in {2,4}, and at most one edge is opposite E2. So τ_min ∈ {2,4}.
- τ_max is 4, 8 or 16 when at most one, exactly two, or all three edges equal 4.
- With two or more 4-edges, at least one is not opposite E2, so τ_min = 4.
- Hence the admissible τ_jkl form one of the sets {2,4}, {4}, {4,8} or {4,8,12,16}.

Consequences:
- gcd(r_v, τ_jkl) = 1 for every odd r_v with 3 ∤ r_v. That includes r_v = 1, E5, and arbitrary primes or prime powers.
- 3 | τ_jkl happens only as τ = 12 in a triangle whose three edges all equal 4.
- Insert this table at SOURCE02:93.
- Remark: a longer check shows that every admissible τ in all of Core5(6) lies in {1,2,3,4,6,8,9,12,16}. This is not needed here.

**MINOR (wrong direction, but unreachable): SOURCE01:27; SOURCE02:93; SOURCE04:162.**
- If 3 | τ_min, then 3 divides every admissible τ, so (iv) fails for v = E3. The first alternative, "3 | τ_min", points the wrong way.
- SOURCE01:27's "whenever 3 ∤ τ_min" exempts exactly that bad case.
- Example outside (iii): a (3,3,3) triangle has τ_min = 3 and τ ∈ {3,6,9}.
- Under (iii), τ_min | 4, so the disjunct never fires and no invalid N26 is accepted.
- Fix: replace it with "τ_max < 3τ_min for every triple". Under (iii) this is equivalent to "no all-4 triangle in N".
- Sufficiency holds: if 3 | mτ_min and 3 ∤ τ_min, then m ≥ 3.

## 4. L12 RPLP (SOURCE01:48–80; SOURCE02:121–174)

**Decomposition.**
- X_j, Y_j and D_j are left U_v-invariant, so every right coset lies in X_j or in Y_j.
- S_C ⊆ A_C by (R1).
- S_C is hereditary-allowed by L9(b), with maxgcd exact.

**Forced containments.**
- On a T-consistent leaf, τ_min ≥ α_vwα_wj ≥ τ by (T2) at apex w, and τ ≥ τ_min, so τ is pinned.
- (T3) at apex v gives μ(U_v(U_w∩U_j)) = α_vw/5 = μ(X_w). So X_w ⊆ X_j, that is, Y_j ⊆ Y_w.
- The column bar has the correct orientation and holds for every admissible τ.

**Constraints.**
- E1 and E2 are exact.
- In B, u = 1/(5·gcd(r_v, α_jk)) is the exact P2 unit.
- lo ≤ μ(X_j∩X_k), because τ_min ≤ τ.
- hi ≥ μ(X_j∩X_k). I checked the K2-bar orientation in all three cases.
- B depends on r only through the markers. E5 never enters.
- TOT ≤ 1 − 1/(5r_v).

**Column completeness.** The only columns omitted are those with:
- A = ∅ (these appear in none of E1, E2, B or Σ);
- a violated forced containment;
- S not allowed;
- S ⊄ A.

Each has true mass 0. No realisable type is omitted.

**Duality.**
- Weak duality applied directly to the true x gives Σx ≥ Obj ≥ 1 > TOT.
- Farkas is needed only for existence. Scaling keeps the right-hand side at 0 ≤ 1.
- A pair with lo > hi also gets a valid certificate: put a large equal weight on u_p and l_p.
- All arithmetic is rational.

**q.** q_j ranges over [1, 5 − α_vj] by (R2) and (R1). Every q is covered once the per-q clause in §6 is enforced.

**No findings.**

## 5. Erratum v1 (SOURCE03)

The folding is complete:
- Codex MINORs → E1–E5;
- Codex MAJOR (controls) → E8;
- Claude MINORs → E1, E3, E5–E8.

No engine predicate is silently altered:
- E4 adds a hypothesis that FH5 satisfies.
- E6 spells out the minimum search space that soundness already requires.
- E5 replaces a false justification without changing any gcd vector.

**Findings.**
- **MINOR SOURCE03:15.** The frozen contract binds proof-v3 (SOURCE07:33, 46, 47).
  - Rebinding to the v4 verdict is licensed by SOURCE11:33.
  - The gate wording must say that the contract's v3 dependence is discharged through that verdict; an erratum cannot amend a frozen contract.
- **MINOR SOURCE03:27.** State which allowed family a dual must respect: the v1 family for engine-v1 duals, the hereditary family (SOURCE00:32) for engines v2/v3. Both are sound.
- **MINOR (optional) SOURCE03:17.** The "any five cosets" remark also closes the p = 3 branch.
- **Cosmetic.** The erratum item "E5" collides with the marker name E5.

## 6. CERT-FORMAT v1 (SOURCE04)

**Each check, if it passes, implies its rule's conclusion.**
- **K.** A link at τ_min pins τ, and Σ ≥ 5 contradicts the bound Σ ≤ 4.
- **Ppair/PB.** u, lo, hi and the bars are as in §4. The extra precondition lo ≤ hi is harmless.
- **RLP.** Weak duality over all hereditary-allowed S.
- **FH5.**
  - (i) is F3 from every vertex with t = 1. (ii) is L9(a) with exact fgcd.
  - Only a's coset is fixed. b, the inside vertices and the forced vertices range fully.
  - All seven E5 placements, including coincident ones, are refuted.
- **N26.** L11 plus the §3 repair.
- **RPLP.** (★) plus the objective, with the columns rebuilt by the checker.

**Universe.**
- The 8 types are complete. Their stabilisers are S6 (once), S5 (five times) and S4 (twice).
- T-consistency comes from the exact table.
- A certificate for an orbit representative transfers to the whole orbit: every rule is label-equivariant, and the stabilisers fix the markers.

**Clauses a checker must add.** Without these, a literal implementation could accept a bad witness.

1. **SAT for prime 5 (SOURCE04:149–152).** SAT is defined only for 2 and 3 (SOURCE04:98).
   - Require SAT₂ ≥ 2, SAT₃ ≥ 1 and SAT₅ ≥ 1.
   - Example: e5 = l with t_l = 1 and t_l′ = 5 has a true 5-part of 5. With SAT₅ = 0, fgcd is underestimated and the checker over-rejects, which is unsound.
2. **Recompute V (SOURCE04:136).**
   - Reject a witness V that contains any v with α_va ≠ α_vb. Forcing t_v = α_va for such a v can exclude the true assignment.
   - A subset of the true V is safe.
   - Also check α_ab = 1 and a ≠ b.
3. **Well-formedness.**
   - v ∈ 0..5.
   - In K and PB, S must be a duplicate-free subset of the vertices other than v. Duplicates inflate Σα_iv or Σ(1 − x_j) and produce degenerate pairs.
   - In Ppair, j ≠ k and both lie in N.
   - y has length 5 and vec has length 30.
   - Rationals are parsed exactly; floats are rejected.
4. **Ordered forced pairs (SOURCE04:174).** (w,j) is ordered, with the product taken at w. Test both orders separately: an unordered implementation over-prunes columns and is unsound.
5. **Per-q coverage (SOURCE04:168–169).**
   - Reject unless len(certs) = ∏(5 − α_vj).
   - For ["R", key], recompute the key from (q, st) and require equality. Otherwise a dual for an easier q could be cited.
   - Reject duplicate keys in rlp_duals.json.
6. **"Should" → "must" (SOURCE04:80).**
   - Enumerate the T-consistent leaves of each type independently, pruning only at completed triangles.
   - Compute orbits under the stabiliser.
   - Require exactly one valid line per orbit, with the type field among the 8 and the representative of that type.
   - leafcodes_sha256 is only a cross-check.
   - Align SOURCE01:84 (pruned-node count published) with SOURCE04:66 (count informational).
7. **SOURCE04:162.** Delete the "3 | τ_min" disjunct.
8. **SOURCE04:199.** Because FH5 uses Sun(6) inside H < G, what the certificate set actually shows is:
   - *no minimal-order Sun(6) counterexample carries a Core5(6) configuration;*
   - *with R1(6) (SOURCE06:47), Sun(6) follows, and Core5(6) follows from Sun(6).*
9. **Obligation outside the checker.** E5 is not part of the type. So E5-independence of K, P, RLP, RPLP and N26 is a written obligation. For N26 it rests on the §3 MAJOR repair.

## 7. Audited versus imported

**Audited by hand:**
- L9(a) and (b), and maxgcd/fgcd exactness;
- L10;
- L11, including the τ table;
- L12, including column completeness and duality;
- erratum folding against SOURCE12/13;
- every CERT-FORMAT predicate;
- the k6-v1 facts these lean on: L0.4–L0.6, (T1)–(T3), K2, P2, R1–R3 and R5′.

**Imported:**
- Zhu Theorem 1.1;
- Sun(5) via SOURCE11 (its engine and bridge were not re-audited);
- R1(6) and the minimal frame (SOURCE06:47–50, accepted in SOURCE12/13);
- elementary group facts.

**Not audited:** code, diffs, runs, counts, freeze hashes and survivor lists.

No Sun(6) theorem, survivor claim or novelty follows from this audit.
