# Final hostile audit: Sun(6) complete composition

## Verdict

**COMPLETE-COMPOSITION ACCEPT-WITH-FIXES.**

- No FATAL and no MAJOR finding.
- Six MINOR findings: one latent checker fail-open that the observed run provably did not reach, and five binding or documentation items.
- No fix changes a mathematical conclusion, and none requires a re-run for correctness.

I worked from the inlined text only and executed nothing. SOURCE10–12 are imported as the parent's observed execution record.

## Does the package establish Sun(6) for every group?

**Yes.** The accepted imports, the supplied observed finite verification and the bridge audited below together establish the exact target. For any group, six pairwise disjoint left cosets of finite-index subgroups, possibly equal, force some pairwise index-gcd ≥ 6.

The only remaining load-bearing prerequisites are imports:
1. Zhu Theorem 1.1: Sun(3) and Sun(4) in every group.
2. Sun(5) in every group, accepted at SOURCE13:5–8. That result is itself computer-assisted, with its trust boundary at SOURCE13:35.
3. Authenticity of the observed replay: checker 5c25199b… run on the inputs at SOURCE11:7–22 gave PASS (SOURCE11:1073–1082). This also assumes correct CPython 3.9.6 integer and Fraction arithmetic.
4. Elementary group theory: the product formula, Lagrange's theorem, and finite-index cores.

The open contract items (§7) gate the *claim*, not its truth. Trust boundary: model-written code (SOURCE10:38), no Lean, no human referee, no novelty or priority claim.

---

## 1. Bridge, re-derived by hand

**R0 (SOURCE07:23).**
- N = ⋂ core_G(G_i) is normal of finite index and lies inside every G_i.
- So each a_iG_i is a union of N-cosets, and indices, intersection indices and disjointness all pass to G/N.
- A counterexample in G therefore gives one in G/N. ✓

**R1(6) (SOURCE07:31–43, with C1 at SOURCE01:24).**
- k = 2 (L0.2 + L0.6) excludes gcd 1. So each gcd lies in {2,3,4,5} and is a power of exactly one p ∈ {2,3,5}.
- The cliques A_p cover the 15 pairs exactly once, and two different cliques share at most one point.
- If every |A_p| ≤ 5, then ΣC(|A_p|,2) = 15 with values in {0,1,3,6,10} forces 6+6+3. That needs two 4-sets sharing at most one point, i.e. 7 points, but there are only 6. So one prime p divides all six indices.
- **p ∈ {2,3}:** every gcd is ≤ 4 < 5, so any five of the cosets contradict the accepted Sun(5). The original Zhu k3/k4 + Prop 4.5 + Core(5) branches (SOURCE14:53–101) are also valid.
- **p = 5:** gcd(5r_i,5r_j) = 5·gcd(r_i,r_j) = 5, so the r_i are pairwise coprime. This is a Core5(6) configuration on the same cosets of the same G. ✓

**Minimal-counterexample frame (SOURCE07:47–50).**
- R1(6) works group by group, so a minimal-order finite counterexample G carries a Core5(6) configuration.
- In that frame, proper subgroups satisfy Sun(6), and every group satisfies Sun(≤5).
- The **only** use of Sun(6) is L9(a) with |T| = 6, inside H = U_aU_b of index 5 (C4, C15: SOURCE01:30, 63–66).
- L9(b) and R4′ never see more than 5 pieces in U_v (SOURCE03:51). T, K, P, XE and N26 use no Sun at all.
- So Sun(6) is never applied to G itself. ✓

**Patterns, types and markers.**
- α_ij ∈ {1,…,4} by L0.3.
- The 91 (E2, class, E3) placements map onto the 8 types, with stabiliser sizes 720, 120 (five times) and 24 (twice). I checked this by hand; the observed run agrees (SOURCE11:52–75).
- Every special case is covered: r_i = 1 (no marker), arbitrary prime powers, primes ≥ 7, equal subgroups (which force r = 1 and α = 1), and any coincidence of E2, E3 and E5.
- The E2 class split is exactly what the rules need: α = 4 reads v₂ ∈ {1, ≥2}, and maxgcd/fgcd saturate at v₂ ≥ 2.
- **Transfer.** A genuine configuration, relabelled to type t, has α = π(rep) for exactly one line and some π in the stabiliser.
  - Its certificate transfers, because every rule is label-equivariant and π fixes E2 and E3.
  - E5 can land anywhere; that is handled by C19 and by FH5's seven placements.

**Rules.** Each is a necessary condition for every τ, every q and every finite r.

- **T.** (T1) is equivalent to α_xy/gcd(α_xy, r_z) dividing τ, and (T2)/(T3) give τ ≤ the smallest vertex product. The gcd table (SOURCE02:60–64) is exact: 5 never divides α, and primes ≥ 7 never enter.
- **K.** On a T-consistent leaf, τ_min = α_ivα_vj ≥ τ_max pins τ, so L2 gives L3's pair condition. Then Σα_iv/5 ≤ 1 − 1/(5r_v), so Σ ≤ 4.
- **P.**
  - The unit u = 1/(5·gcd(r_v, α_jk)) is exact, by L0.4/L0.5 and gcd(r_v, r_jr_k) = 1.
  - Grid rounding of lo and hi (C13) is correct.
  - The K2 bars are oriented correctly in all three cases; for example, X_j ⊆ X_k needs α_vj + α_kj ≤ 4.
  - The Bonferroni sum is ≤ μ(⋃Y) ≤ 1 − μ(U_v).
- **H5, F and FH5.**
  - In the triangle vab, (T2) gives τ ≤ c and (T1) gives c | τ; for c = 4 this uses whichever of r_a, r_b is odd.
  - Hence U_vU_a = U_vU_b. W = U_aU_b then has index 5, using both U_a ≤ W and U_b ≤ W (C2), and t_v = c.
  - Then λ_l = r_lt_l, and F3 and L9(a) apply.
  - fgcd equals the true gcd: common primes lie in {2,3,5}, and since v₂(t) ≤ 2 and v₃(t), v₅(t) ≤ 1, each exponent saturates (C16).
- **RLP with L9(b).**
  - R1–R3 and R5′ (SOURCE14:181–197) use only pairwise disjointness.
  - q_j ∈ [1, 5 − α_vj] and d_j = q_jr_j.
  - maxgcd equals the true gcd: v₂(q) ≤ 2, v₃(q) ≤ 1, and 5 is never a common prime.
  - Weak duality gives Σμ ≥ Σ y_jq_j/5 ≥ 1 > 1 − μ(U_v).
  - The hereditary family is contained in the v1 family, and both are sound (C10/C17).
- **XE.** [G:W] divides gcd(5r_j, 5r_k) and W ≠ G, so α_jk = 1. Neither distinct subgroups nor normality is assumed.
- **N26 with C14.**
  - Step 1 (granularity 1/5 plus XE), Step 2 (gcd(r_v, r_lτ) = gcd(r_v, τ)) and Step 3 (the 6/5 count) are correct.
  - **The C14 table, re-derived.** Since v ≠ E2, at most one edge of a neighbour triangle is opposite E2. So τ_min ∈ {2,4}, with τ_min = 4 as soon as there are two 4-edges, and τ_max is 4, 8 or 16. The admissible sets are {2,4}, {4}, {4,8} and {4,8,12,16}.
  - So gcd(r_v, τ) ≠ 1 only when 3 | r_v and τ = 12 in a 4,4,4 triangle. The C11 test τ_max < 3τ_min fails on exactly those triangles.
  - This closes the Claude MAJOR (SOURCE18:80–94).
  - Independently, the checker enumerates every admissible τ of every neighbour triple (SOURCE08:645–659). The 108 N26 lines therefore do not rest on the written table at all.
- **RPLP.**
  - Every omitted column has true mass 0: A = ∅, a violated forced containment, S not allowed, or S ⊄ A.
  - **Orientation.** τ_min(v,w,j) ≥ α_vwα_wj ≥ τ_max pins τ, so X_w = U_v(U_w∩U_j) ⊆ X_j, i.e. Y_j ⊆ Y_w.
  - **Weak duality.** a and b are free (E1 and E2 are identities) and u, l ≥ 0, so regrouping gives Σx ≥ Obj ≥ 1 > TOT.
  - Feasibility is never assumed, so "Farkas" vectors are validated by the identical inequalities.

**M1 (every τ).**
- T is a necessary condition.
- K links and forced containments are pinned at τ_min.
- lo only increases with τ, and hi, K2, RLP and F do not read τ.
- H5 derives τ = c itself, and N26 enumerates every admissible τ.

**M2 (every r).** Every quantity depends on r only through the markers, and does so exactly.

**E5 (C19).** 5 divides no α and no q, and no two cofactors share the prime 5. Only FH5 reads E5, and it covers all seven placements.

**Strictness.** Every contradiction is either "≥ 1" against "≤ 1 − 1/(5r_v)", or 6/5 > 1. Both hold for every finite r_v.

## 2. Erratum v3 (SOURCE01)

Repairs verified:
- **C14:** the MAJOR.
- **Minor items:** C2; C4/C15 (properness); C5/C16 (saturation, including SAT₅); C11; C13 (grid rounding); C10/C17 (allowed family); C12 (dependency); C18 (closure); C19 (E5); C20.
- **Unused:** C21.

Every Codex finding (SOURCE17:62–66, 92, 98–115) and every Claude finding or clause (SOURCE18:44–48, 97–103, 156–161, 183–211) is folded in.

**The k5 dependency is discharged, not amended.**
- The frozen contract names proof-v3 (SOURCE20:33, 46, 47, 55).
- SOURCE13:5, 11 accepts proof-v4 with its erratum v3.
- SOURCE14:22 states that no mathematical step changed from v3 to v4.
- SOURCE13:33 explicitly licenses the k = 6 lane to cite that verdict.
- SOURCE00:12 and SOURCE01:35 record the discharge without amending the contract. ✓

## 3. Checker against CERT-FORMAT-k6-v3 §6

The checker uses the standard library only and imports no engine code (SOURCE08:21–35).

1. **Universe.**
   - Two structurally different enumerations must agree exactly: the star-bitmask one (219–257) and the edge-DFS one (260–295, compared at 1078). Each triangle is tested exactly when its last edge is assigned.
   - Orbits are recomputed from `rep` under the typed stabiliser (335–337, 389–413).
   - "Σ|orbit| = |union|" together with "union = leafset" is exactly "each orbit is met once". This is set equality, not a comparison of counts or hashes.
   - Each `rep` must lie in the leaf set and pass the scalar T test (1097–1102).
   - The type must be one of the 8 (154–162), and all 91 placements are brute-forced (345–369). ✓
2. **Well-formedness.**
   - bool is rejected where an integer is required (87–88).
   - Each S must be duplicate-free and must not contain v (550–552).
   - Vector lengths 5 and 30 are enforced (510, 698).
   - Rationals must match a strict regex and are parsed with Fraction; a zero denominator is caught (428–433).
   - Duplicate JSON keys are rejected at every nesting level (436–446), and each line's key set must be exact (886–887). ✓
3. **FH5.**
   - V is recomputed and must equal the witness; α_ab = 1 and a ≠ b are checked (756–762).
   - The domains match C6, with only a's coset fixed (768–778). SAT = 30 is used for 2, 3 and 5 (781–785).
   - **Pruning is monotone.** A placement is dropped only when F3 fails, or when some subset T containing the newest member fails. Every T ⊆ M_c is tested when its last member arrives, and a failed T stays failed under extension (816–869).
   - An ACCEPTED or INCOMPLETE search never counts as verified (914–916, 1162–1164). ✓
4. **RLP.**
   - Every q is enumerated in product order (462–464).
   - Each key is recomputed, and a missing key fails (531–542).
   - All 31 supports get every hereditary sub-test (470–504).
   - An "R" entry's key must equal the recomputed key (733–734). ✓
5. **RPLP.**
   - The certificate count must be exact (725–726).
   - Forced pairs are ordered, with closure j ∈ A ⇒ w ∈ A (663–667, 678).
   - Empty S is included (681).
   - Bounds, signs, every column and the objective are rebuilt from scratch (686–715). ✓
6. **N26.** The corrected test, plus the prime-support check on every admissible τ (633–660). ✓
7. **K and P.** Everything is recomputed, with grid rounding followed by the K2 decrement (555–631). ✓

**Global.**
- A SURVIVE line, a non-empty survivors.json, or a nonzero total_survivors makes the run fail (938–948).
- Any CertError makes the run fail.
- **Exception:** the deadline path described in MINOR-1.

## 4. The engine `code` boundary

**Where `code` is used.** Only shape checks (SOURCE08:166–168, 890) and informational counters (401–403, 416–424). Coverage and every rule decision use (type, rep) (1089–1092, 1144). This matches the receipt's warning (SOURCE10:39).

**What `code` actually is.**
- It lies outside the typed stabiliser orbit of `rep` for most lines: 402 of 2,268, 315 of 16,414, and 315 of 23,715 (SOURCE11:224, 566, 916).
- Yet all 1,600 sampled codes lie in the full S6 orbit of their `rep`.
- This is consistent with an S6 canonical form that moves the markers.

**Consequences.**
1. The engine's own deduplication is not evidence.
2. Reconstructing patterns from (type, code) would produce wrong labelled patterns, and the witnesses would not apply to them.
3. The witness indices are relative to `rep`, as confirmed by 61,124 of 61,124 lines passing on `rep`.

**The boundary holds.** Mathematical validity does not depend on the engine.

## 5. Observed execution record (imported, not re-run)

SOURCE11 (Python 3.9.6, 57.4 s, one process):
- For all 8 types, edge-DFS matched the primary enumeration, the leaf hash matched, and coverage passed with no missing, extra or duplicate patterns.
- 1,575,031 leaves and 61,124 lines, every line verified (1073–1078).
- Per rule: K 55,159; RLP 5,513; FH5 134; N26 108; PB 55; RPLP 155 (1035–1072).
- RLP keys: 1,275 checked, 1,275 passed (1030–1032).
- No SURVIVE line. Verdict PASS (1082).

My arithmetic cross-checks of SOURCE11 are consistent:
- the per-type sums;
- the spot-check total, 33,500 = 20,000 + 300·15·3;
- union hash equal to leaf hash for every type;
- 1,275 + 71 = 1,346 dual entries.

SOURCE12 records 68/68 tests passing, including 43/43 mutations rejected. These are observations, not soundness proofs.

## 6. Findings

**FATAL:** none. **MAJOR:** none.

**MINOR-1 (code; latent fail-open).**
- **Where:** SOURCE08:1141–1143. After the deadline, a skipped line increments `rs["incomplete"]` but is never appended to `rep["incomplete"]`.
- **Why it matters:** the verdict logic (1208–1213) and the bookkeeping check (1203) both still pass, so a budget overrun could print **PASS with unchecked lines**.
- **Effect on the observed run:** none. Incomplete = 0 and verified = 61,124 (SOURCE11:1073–1078), at 57.4 s against a 3,300 s budget.
- **Fix:** append to `rep["incomplete"]` in that branch; require `tot["verified"] == len(lines)` for PASS; add a test that forces the deadline inside the rule loop (SOURCE09 has none).

**MINOR-2 (spec).**
- **Where:** SOURCE02:83, 87 call `code` "the engine's canonical form".
- **Fix:** declare it untrusted and non-representative, state that it MUST NOT be used, and cite the statistics in §4.

**MINOR-3 (binding).**
- **Where:** SOURCE00:27 binds the certificates in `engine-v3-core56/` through `engine-v3-run.sha256`, but the replay read the parent's copies (SOURCE11:7–22). The checker looks for the manifest only beside the engine directory (SOURCE08:1004–1010), so `manifest_lists_input_hashes` is absent (SOURCE11:1006–1079). The link, MANIFEST-v1 (SOURCE10:20–24), was not supplied.
- **Effect:** mathematically immaterial, because any complete valid certificate set suffices.
- **Fix:** the verdict must cite the checked hashes: run.json 6d8dc91d…, orbits.jsonl.gz a580c580… (uncompressed f4f69363…), rlp_duals.json bbf91e05…, survivors.json 4f53cda1… (the bytes `[]`).

**MINOR-4 (spec provenance).**
- **Where:** the checker was written from CERT-FORMAT v1/v2, errata v1/v2 and the review notes (SOURCE08:6–11, 57–71). It does not cite the v3 texts that SOURCE00:5 and SOURCE00:51 make normative.
- **Effect:** none found; §3 shows conformance to v3 clause by clause.
- **Fix:** record that v3 conformance was established by audit, not by construction.

**MINOR-5 (stale status).**
- **Where:** SOURCE00:56–68 lists the NumPy auxiliary replay as "Done", although it does not meet the standard-library rule (SOURCE21:16). It still lists the standard-library checker as "Pending". SOURCE07:25 and SOURCE07:45 are likewise stale frozen text.
- **Fix:** supersede the status: the primary evidence is SOURCE10/11, and the auxiliary route is a disclosed deviation. The README lines are already superseded by C1/C12 and SOURCE13.

**MINOR-6 (editorial).**
- SOURCE02:171 is garbled; the operative conditions are the rows of C14.
- CERT-FORMAT-k6-v3 has no §5 (it jumps from §4 to §6).
- SOURCE02:105 states SAT thresholds stronger than needed (2 and 1 suffice). This is harmless.

## 7. Process, priority and significance

**Disclosed deviations (none load-bearing):**
- the NumPy auxiliary route (SOURCE21:16–20);
- model-assisted authorship of the checker (SOURCE10:38);
- the lane self-check, stopped with outcome UNKNOWN (SOURCE00:70).

**Open contract prerequisites for the gate (SOURCE20:46):**
1. The Codex-family final composition review. This note is the Claude-family one.
2. The parent's final verdict must record its own re-derivation of *every rule used*. The supplied record shows parent re-derivation only of R0 and R1 (SOURCE00:11; SOURCE20:30). The rules otherwise rest on reviews (SOURCE00:18–24). The verdict may adopt §1 of this note.
3. The post-result priority refresh, still pending (SOURCE19:26). Any "announcement" must stay internal (SOURCE20:69–70).
4. Gate wording that states the v3→v4 dependency discharge.

**Priority.**
- The screen's result is PARTIAL_OVERLAP_FOUND: Margolis–Schnabel Cor 3.9 covers some Core5(6) patterns.
- No k ≥ 6 general-group claim was located within the bounded scope.
- Several sources were unreachable (SOURCE19:5, 24). Not finding a claim is a search miss, not evidence of novelty.

**Significance.** If the gate closes, this is the k = 6 general-group case of Sun 2006, Conjecture 1.2. k = 5 is a previously claimed case (SOURCE13:33), and for G = ℤ the result is known up to k = 20. I make no novelty, "first" or publication claim.

## 8. Audited versus imported

**Audited (statically, in this review):**
- R0, R1(6) and the minimal-counterexample frame;
- L0.4–L0.6, T, K/K1/K2, P1–P5, H5, F1–F3, R1–R3, R5′, R4′, L9(a)(b), L10, L11 with C14, and L12;
- M1, M2, C19 and strictness;
- erratum v3 (C1–C22) and CERT-FORMAT-k6-v3;
- checker_v1 line by line, and the design of its tests;
- the internal arithmetic of SOURCE11.

**Imported:**
- Zhu Theorem 1.1 and the accepted Sun(5) verdict (SOURCE13);
- every execution fact in SOURCE10–12;
- hashes that were not inlined (MANIFEST-v1, engine-v3-run.sha256, the freeze records);
- the rules-v1 review notes;
- CPython arithmetic and elementary group theory.

**Not relied upon:** the engine's code and its `code` field; run.json counts and hashes (cross-checks only); the NumPy route; the controls.
