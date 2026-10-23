# K7-LFC-INV-erratum-v1: wording/scope overlay on K7-LFC-INV-v1 (no theorem change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-18T23:40:24-0700.
- **Overlays:** `K7-LFC-INV-v1.md`, sha256 45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c, which stays
  frozen and byte-identical. Read the two files together.
- **Responds to:** Claude review `RUN/review/sun7-lfc-inv-claude-v1.prompt.note.md` (sha256 7f61522920eff703e152a0dd7cfbbfb4dbf8f2edbae2e94a55ee3971d887744d;
  ACCEPT-WITH-FIXES, 0 FATAL/MAJOR, 9 MINOR) and Codex review `RUN/review/sun7-lfc-inv-codex-v1.prompt.stdout.txt`
  (sha256 0d849d2dda0dab58e3e033de85bb4e8dec4694a63e090469ca6d2b8b44928905; ACCEPT, one editorial MINOR = Claude m1).
  RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- **Status:** written overlay; it changes no statement of LFC, INV, ROW-U, K7-M0 or K63-U0 and adds no new claim.

## E1 (Claude m1, m2; Codex minor): L0.3 and the preliminary bounds, now listed and re-derived

Add to the import list of section 0: **L0.3** and the following preliminaries, re-derived here from L0.1/L0.2.
For subgroups U_i, U_j of the finite group G with g_iU_i cap g_jU_j = empty:
- n_i and n_j divide I_ij = [G : U_i cap U_j], so lcm(n_i,n_j) | I_ij and alpha_ij = I_ij / lcm(n_i,n_j) is a positive integer;
- by L0.1, mu(U_iU_j) = |U_i||U_j| / (|U_i cap U_j| |G|) = I_ij / (n_i n_j) = alpha_ij / g_ij (this is L0.3's identity);
- by L0.2, g_i^-1 g_j is not in U_iU_j, so U_iU_j != G and alpha_ij <= g_ij - 1.
Consequences used in the file: in K7 every alpha lies in {1,...,5}; in K63-U0, g_vd = 3 and alpha_vd in {1,2}.

## E2 (Claude m3): Sun(2)

Sun(2) (L0.6: coprime indices give U_iU_j = G, so the two cosets meet) is used and is hereby listed among the imports.
It is what forbids two pieces with gcd(lambda, lambda') = 1 in one fibre (cross-class pairs in ROW-U, R1 singletons,
and d being singleton-only in K63-U0 Step 1). It is an instance of the granted "Sun(t), t <= 6" import.

## E3 (Claude m4): LFC (c), why at most six pieces share a fibre

Replace "By (b), v is not in S_C, so |S_C| <= k - 1 <= 6" by: "v is not in S_C by definition (S_C is a set of
vertices j != v), so |S_C| <= k - 1 <= 6. The fibre g_vU_v itself is excluded from the count because it is a whole left
U_v-coset holding v's coset, and distinct left U_v-cosets are disjoint; (b) shows that no other coset meets it.
(b) is needed in (d), where it guarantees that all t_j fibres met by g_jU_j are among the n_v - 1 counted ones."

## E4 (Claude m5): notation

- V := {1, ..., k} (k = 7 in all applications).
- In the proof of LFC (c), the chosen point of g_jU_j cap C is renamed **p_j** (the file wrote y_j); the letter y denotes
  only LP weights.
- g_v (coset representative) and g_vj (= gcd(n_v, n_j)) are distinguished by the number of subscripts only; no
  statement depends on the coincidence.

## E5 (Claude m6): R0 lift for K63-U0

Add to the statement of Theorem K63-U0: "By R0 (README section 1), which preserves every index and pairwise
disjointness in the finite quotient G/N, the same holds for arbitrary G with finite-index U_i."

## E6 (Claude m7): "same class" in INV (a)

Replace the clause "so it lies in the same class (K7, K6.2*, K6.3, K5.2*, K5.3, KII) with the same marking" by: "so it
has the same labelled index tuple (n_1, ..., n_7). Every class of README section 5 (and the marking, i.e. which vertex
carries e >= 2, f >= 2 or h >= 1) is defined from the labelled index tuple alone, so the inverted configuration lies in
the same class with the same marking." The parent has read the class definitions (README section 5, sha256
2a6d6d6e...) directly. The only load-bearing use in K7-LFC-INV-v1 is Theorem K7-M0, where the hypothesis itself
(n_i = 6 w_i for all i) is visibly a property of the index tuple.

## E7 (Claude m8): external cross-references

- **(V1) and q.** rules-k7-v1 section 2 (V1), sha256 77b9afec..., defines q_j, after left multiplication making
  g_v = 1, by |D_j| = q_j |G| / g_vj with D_j = U_v g_j U_j (parent read this directly). INV (b)'s identification
  q_j = alpha*_vj is with that definition.
- **The inequality alpha + alpha* <= g does not need VFC:** with h = g_v^-1 g_j, disjointness gives h not in U_vU_j (L0.2),
  so U_v h U_j and U_vU_j are distinct, hence disjoint, (U_v, U_j)-double cosets, of measures alpha*_vj / g_vj
  (INV (b) computation) and alpha_vj / g_vj (E1). Theorem K7-M0 uses only this inequality.
- **Navigation only, not premises:** LFC Remarks (1)-(3); the "Relation to the accepted frontier" paragraph of section 4
  (Q24, Q5, Q23U); in section 5 "These are exactly the K6.3 configurations with no vertex of e >= 2, f >= 2 or h >= 1"
  (it is the definition used) and "subsumes the accepted partial D3 only on its unmarked part". These were
  cross-checked by the parent against the old frozen texts.

## E8 (Claude m9): one stated value bound for R1 cup R24

Add to the proof of ROW-U, after the list of standard partial weights:
"**Value bound.** For any N neighbours lying in R1 cup R24, the standard weights give value >= min(N, 4): R1 elements
contribute 1 each; R24 contributes a + b (its own size) when b <= 2 and at least 4 when b >= 3. Hence the value is
k1 + (a + b) = N when b <= 2, and >= k1 + 4 >= 4 when b >= 3."
With this bound:
- ROW-U (i), branch k3 <= 3: value >= 3 + min(6 - k3, 4) >= 6;
- ROW-U (i), branch k3 in {4,5}: value >= k3 + min(6 - k3, 4) = 6 (the file's clause "with b >= 3 at least 4" is
  vacuous there, since at most two elements remain);
- K63-U0 Step 1, five C-neighbours: k5 >= 1 gives >= 5; k3 >= 4 gives >= 4; k3 in {1,2,3} gives 3 + min(5 - k3, 4) >= 4;
  otherwise min(5, 4) = 4.

## Unchanged

All statements, proofs (up to the wording above) and scope limits of K7-LFC-INV-v1. Marked K7, marked K6.3 and K6.2*
remain OPEN. Correctness is separate from novelty; no novelty claim.
