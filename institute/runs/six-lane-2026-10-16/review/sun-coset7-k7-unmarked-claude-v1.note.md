# Hostile audit: K7-unmarked-lemmas-v1 (SOURCE00)

**Scope.** This is a written-mathematics audit only; no computation was run. I could not recompute the hashes, so all cites are to the inlined LF lines.

The accepted base is SOURCE05 (TRI, U, TWIN, Q in the X1 convention, Q5, COV) and SOURCE07 (the T, K, P, VFC and RPLP rules). L5 and L6 are frozen (SOURCE06:32–35) but appear on neither accepted list (SOURCE07:23, :49; SOURCE05:5). I therefore re-verified every clause of L5 and L6 that is used.

Every use draws on Sun(2), Sun(3) and Sun(4) only, inside explicit subgroups whose index m is derived in writing. There is no least-order frame, no Sun(7) and no FH or §A4 apparatus (SOURCE03:238). **K7 remains OPEN.**

## Verdicts

| Item | Verdict | Exact scope |
|---|---|---|
| Narrow P2 | **ACCEPT** (verified here) | M=∅ and X1-Q23 with r≥2 classes ⇒ all twin blocks are singletons. This does not accept SOURCE01/02 as files. |
| K7-HIGH | **ACCEPT** | v∈U with six unmarked neighbours (so M=∅) and every α_vj≥3 |
| K7-CLASS | **ACCEPT** | M=∅, X1-Q23, r≥2; excludes class sizes 2, 3 and 4 only |
| K7-Q23U | **ACCEPT** | M=∅, X1-Q23, r≥2 |
| Status section (:85–100) | **AWF** | 1 MAJOR (scope), 4 MINOR |

There is no FATAL finding and no mathematical error in the four items.

## Narrow P2

- **L6** (SOURCE06:35): correct.
  - X=U_vU_a is right-invariant under W, so X=U_vW.
  - μX<1 gives W≠G.
  - U_a, U_b ≤ W gives m | g_ab and μ(U_aU_b) ≤ 1/m.
  - μ(U_vW) = [U_v:U_v∩W]/m.
- **L5, used clauses** (SOURCE06:32): correct using left cosets only, with |T|≤4 throughout.
  - g_lU_l meets t_l≤m left H-cosets.
  - Each piece translates to a left coset of U_l∩H, of index n_l·t_l/m.
  - The pieces are disjoint, and Sun(|T|) holds in H.
- **s≥3 with M=∅** (SOURCE01:41–67, :75–108): correct.
  - A third twin gives α=1, so m/6∈ℤ and m=6. Then U_jU_k=W_B (both have measure 1/6), and this does not depend on the pair.
  - λ_j=w_j is coprime to every λ_v, so Sun(2) keeps outsiders off the block cosets. Hence α_vB≤6−s, while unmarked non-twins need α≥2. So s≥5 is impossible.
  - s=4: 6 incidences exceed the capacity of 4 (at most 2 per coset, by Sun(3)).
  - s=3: no mixed {2,3} pair, at most two 2's and at most three 3's per coset (Sun(4)). A vertex with t=3 fills every coset.
- **s=2** (SOURCE02:29–49, :56–58, :65–69): correct.
  - m=2 forces α_vB=3 (TWIN(c) caps α at 4). Then seven t=1 pieces sit in two cosets with pairwise gcd 3, so Sun(4) fails.
  - r≥2 supplies an outsider at α=3, which kills m=3.
  - At m=6: k_2≤c_2 and k_3≤c_3, so 5≤4, a contradiction.
- **Notes for the separate BLOCK/PAIR review:**
  - SOURCE02:62 says "type Q23" without qualification, but under X1 it is proved only for r≥2 (SOURCE04:70). SOURCE00:42 correctly uses the narrow form.
  - SOURCE01:33 ("|T|≤6") disagrees with SOURCE01:10 ("≤4"). This is harmless.

## K7-HIGH (SOURCE00:19–38)

- **Values of q.** q_j∈{1,2,3} exactly, by V1 and α≥3. Since d_j=q_j·w_j, gcd(d_j,d_j′)=gcd(q_j,q_j′).
- **Allowed sets.** These are hereditary (SOURCE06:48). So every allowed set of size ≥2 lies inside the q=2 group (size ≤2) or the q=3 group (size ≤3).
- **Weights.** All weights are ≥0 and feasible on every allowed set. Absent groups receive no weight and contribute 0=k/6. "1/k_3" is only ever evaluated with k_3∈{1,2}.
- **Total.** Each group contributes at least k/6, so the total is at least 1, against VFC-count's strict <1. Every q-vector is covered.
- **Editorial (non-blocking):**
  - :19 should state M=∅ explicitly.
  - :29 "otherwise" should read "if k_3∈{1,2}".
  - :22 the symbol d_j collides with d_v(r) (overlay at SOURCE05:43).

## K7-CLASS (SOURCE00:42–73)

- **Step 1.** Take the (2,3,3) triangle with apex v∉C. T1 gives 6|τ. T3 gives μ(U_v(U_j∩U_k)) = τ/12 ≥ 1/2 = μX_j = μX_k, so U_vU_j=U_vU_k. L6 then gives m|6, m≤3 and m/2∈ℤ, so m=2 and U_v≤W for every v∉C.
- **Step 2.** t_i≤[G:W]=2 by the L5 count; :55 should say so. λ=3tw, so pairwise gcds are 3, or 6 when both vertices have t=2. Sun(4) allows at most three t=1 vertices per coset.
- **Step 3.**
  - c=2: 7 vertices with t=1 against a capacity of 6.
  - c=3: t_i=2 is forced, the split is 3+3, and four gcd-3 pieces share a coset.
  - c=4: (1,1) gives 7>6; (1,2) goes as in c=3; in (2,2) every 4-set needs both t=2 vertices, so at most 2 t=1 vertices fit per coset, and 4<5.
- Only left-coset counts are used; normality is never invoked. Class sizes ≥5 are correctly left open. Editorial: :46 should say "distinct j, k".

## K7-Q23U (SOURCE00:80–83)

Class sizes lie in {1,5,6}: r≥2 excludes 7, and at most one class has size ≥5. All remaining classes are therefore singletons. A singleton has α=3 to six unmarked vertices, so HIGH applies. Correct.

## Status findings

1. **MAJOR (scope), SOURCE00:5, :97, :100.**
   - :5 omits single-class Q23 with M=∅, which X1 assigns to Q23 (SOURCE04:26; SOURCE05:21).
   - :97 narrows that case using "P3's argument". But P3 is not among the imports (:6–14) and is under separate review. Its {2,4} extension is the S1 note (SOURCE04:71), which is outside SOURCE05's accepted scope (SOURCE05:5, :56).
   - :100 then drops single-class twin-pair patterns unconditionally, contrary to SOURCE02:122.
   - **Fix:** add single-class Q23 to :5. Rewrite :97 and :100 as: "single-class Q23 (M=∅) is OPEN; *conditional on P3 in its S1 form*, only the seven-singleton all-2 pattern remains." The block-size ≤2 part (BLOCK(d) at M=∅) is verified here.
   - I spot-checked the k_4=0 arithmetic and found no error: m=2 needs α=3; m=3 gives 7 light incidences against 6; m=6 gives 10 against 8. This check is not an acceptance.
2. **MINOR, SOURCE00:87, :91, :95.** The Q5 row with M=∅ is already accepted (SOURCE05:25), and HIGH reproves only the |U|=7 case. **Fix:** do not label that row "unreviewed".
3. **MINOR, SOURCE00:97 (the q-example).** This is illustrative, not a proved residual list.
   - My check: for q=(4,4,4,4,4,2), the allowed sets are exactly the subsets of size ≤4. Averaging gives a maximum of Σyq/6 = 11/12 < 1, attained at y≡1/4. So VFC-count is not violated at that vertex.
   - The example says nothing about the other vertices, RPLP or realizability.
   - **Fix:** write "VFC-count at one vertex".
4. **MINOR, SOURCE00:98.** **Fix:** label each Q24 constraint with its status: BLOCK verified here at M=∅, P3 conditional, HIGH proved.
5. **MINOR, SOURCE00:10–14.** "Frozen" does not mean "accepted" for L5 and L6. **Fix:** record that this audit verified the clauses used.

## Proved vs claimed

- **Proved here:** narrow P2, HIGH, CLASS (sizes 2–4), Q23U, and the Q24 neighbour corollary (:89).
- **Unreviewed claims:** the single-class narrowing, the P3 constraint and the q-example. No enumeration or list of failing q-vectors is established.
- **Still open:** single-class Q23 and Q24 with M=∅, and every case with M≠∅.
