**Counts (new defects in erratum v6):** FATAL 0 · MAJOR 0 · MINOR 2 (one completeness, one process/literal). I found no correctness defect in v6's mathematics.

**AFIBRE dispositions:**
- **MAJ-1:** RESOLVED.
- **MIN-1:** RESOLVED.
- **MIN-2:** RESOLVED.
- **MIN-3:** RESOLVED. New finding m-A comes from how the restriction was implemented.
- **MIN-4:** RESOLVED for all five items AFIBRE named. The same defect type remains in R16, counted as new finding m-B.

## Claim-wise verdicts

**Explicit order (v6 LF6): correct.**
- N15's only input is N02 (LEDGER LF232), and N02 comes before N15 in the new order.
- I re-checked every input cell at LEDGER LF218–276:
  - every original edge has a smaller-numbered source;
  - v6 does not change the relative order of any nodes other than N15.
- All four new edges point forward in the explicit order: N02→N10, N02→N14, N15→N13, N15→N14.
- Every consumer of N15 (N16 onward) comes after N15's new position 9.
- So the order is topological and the graph is acyclic.
- v6 LF6 withdraws the numeric-order claim at LEDGER LF214–215. The withdrawal is necessary, because the N15→N13/N14 edges make that claim false.

**INV wording (v6 LF8; L LF56–58; LE LF49–52): correct, with no backward profile dependency.**
- [G:U_i*] = n_i and inversion is a bijection, so the inverted family is again a CE with the same labelled index tuple.
- The following are all functions of that tuple: A_p, C, E, a, D, the marking (LE LF50–51), the six class predicates, and any π_i (RK7 LF68).
- So "every index-determined invariant" covers whatever profile definition a consumer brings.
- N13's inputs are complete: N02, N03 (cons.), N11 (V1 only), N15. N03 really is conservative, because INV assumes G is finite (L LF54).

**ROWU (v6 LF8, LF19; L LF79, LF85–86): correct.**
- N15 supplies:
  - the K7 predicate and matrix (g_vj = 6);
  - "unmarked" ⇒ n_j = 6w_j;
  - gcd(w, 30) = 1;
  - P0(b).
- N02 supplies α ≤ g−1 = 5 (LE LF18) and Sun(2) (LE LF23–24).
- I re-derived the gcd reduction:
  - Suppose a prime p divides gcd(w_jα_j, w_j′α_j′).
  - Then p ∤ w_j, because p ∤ w_j′ (P0(b)) and p ≥ 7 > α_j′.
  - By symmetry p ∤ w_j′.
  - So the gcd equals gcd(α_j, α_j′).

**MIN-1 (v6 LF16–19): correct.**
- N10's inputs are {N02, N09}.
- N14's inputs are {N02, N12, N15}.
- N16 is added to R05's consumers.
- N13 uses only (V1)'s definition of q. The inequality α + α* ≤ g needs no VFC (LE LF61–63).

**MIN-2 (v6 LF22; ME LF26–32; LE LF71–80): correct.**
- The hypothesis at ME LF27–30 mentions only three things: g_vj = 6, α_vj ≤ 5, and the neighbour-label gcds.
- From that hypothesis alone I re-derived:
  - the LFC(d) bound, which needs only g_vj = 6;
  - the class split (cross-class gcds are 1, so Sun(2) applies);
  - the allowed sets (Sun(3), Sun(4), Sun(5), Sun(6));
  - the standard weights;
  - the E8 bound min(N, 4);
  - conclusions (i)–(iii).
- The consumer instances are excluded: ME LF26 and LF31–32 (ROW-1/M1) and LE LF79–80 (K63-U0).
- No ROW1/M1 edge or cycle is created.

**MIN-3 (v6 LF11, LF13): correct.**

The KII derivation re-derives step by step:
1. Suppose x ∉ A_2 ∪ A_3. Then for any j ∉ A_5, P_xj = ∅, so gcd(n_x, n_j) = gcd(w_x, w_j) = 1. This contradicts P0(a)/(b).
2. P1(ii) allows at most one of x, y in A_2 and at most one in A_3. So, up to renaming, x ∈ A_2∖A_3 and y ∈ A_3∖A_2.
3. For j ∉ A_5, P_xj ⊆ {2} and P_yj ⊆ {3}, and both are nonempty by P1(i). So j ∈ C, and C = V∖{x, y}.
4. P1 then gives the four matrix entries, which match README LF96.

The derivation uses no R1(7), no exhaustiveness, and no Sun(t) for t ≥ 3.

The other five class matrices each follow in one line:
- Take a D-vertex in A_2∖A_3 (or A_3∖A_2) and pair it with a C-vertex or a D-vertex of the same type.
- Then P contains 2 (or 3).
- P1(i) then forces P = {2} (or {3}).

Two further checks:
- K7 "unmarked" (v6 LF11) agrees with the marking in LE LF50–51, since C = V forces e, f ≥ 1.
- Predicates are kept separate from COVER: LF87 is excluded, and exhaustiveness goes to N23 (LEDGER LF240).

**MIN-4 (v6 LF25) against RWE/RWV: matches.**
- The export hashes are correct.
- RK7 citations follow RWE m1 (LF5): LF70 for non-L5 quantities only, then LF71–75, then the first sentence of LF80.
- RPLP scope follows m1: ADD LF21–110 with W2 governing LF106, plus the first two sentences of LF124.
- CAP citations follow m1: ADD LF128–139, LF143–148, LF155, with LF152–154, LF157 and LF159 excluded.
- R12 uses only the WV packing proof, so there is no alternative K route (m4, LF8).
- N57 is affirmed as the capping consumer.
- The R0 clause is consumer-side (RWV LF5).
- There is no INV export (m2) and no CAP-ENV claim (m6).

## New findings

**m-A (MINOR, completeness): N15's narrowed export has no consumer check beyond N09–N16.**
- **Step.** v6 LF11 ("N15 exports only …") drops three items that LEDGER LF65 exported:
  - RM LF67, the conditional matrices for (I) type 2, (I) type 3 and (II);
  - WV LF18–21;
  - overlay A-1 LF46.
- v6 names no new provider for LF67. The only pasted range for N17 is RM LF60–65 (LEDGER LF234).
- The only consumer check on record is AFIBRE LF109, and it covers only N09–N16. Yet v6 LF3 ("no class theorem is weakened") and LF27 ("No other incoming edge changes") speak for all consumers.
- The exposed rows are N18–N22:
  - they list N15 but not N17 (LEDGER LF235–239);
  - README LF100–103 phrases their cases as "(I) type 2/3".
- I cannot point to a consumer that actually breaks from the pasted text. The obligation is unverified, not refuted.
- **Consequence.**
  - Any N15 consumer that cites LF67, or the (I)/(II) vocabulary, as N15 content now has no listed provider. This is a missing provider of the same kind as MAJ-1, but it can be repaired with forward edges.
  - What happens to overlay A-1 is not stated. If it amended README LF33–52 or LF89–96, dropping it reverts a correction.
- **Repair** (either option):
  1. Re-export LF67 from N15, with the case predicates written without R1(7). If the intended meanings are (I)-2 := a ≤ 1 ∧ D ⊆ A_2∖A_3, (I)-3 := a ≤ 1 ∧ D ⊆ A_3∖A_2, and (II) := a = 2, the matrices follow from P0/P1:
     - Take d ∈ D ⊆ A_2∖A_3 and j ∉ A_2. Then P_dj ⊆ {5}, which needs both d and j in A_5. That contradicts a ≤ 1, so P_dj = {2}.
     - Type 3 is symmetric.
     - (II) is v6's KII derivation.
  2. Record that no row from N17 to N59 cites RM LF67, WV LF18–21 or overlay A-1 as N15 content, and add forward N17 edges wherever one does.

  In either case, state what happens to overlay A-1 LF46.

**m-B (MINOR, process/literal): RW-row alignment is incomplete.**
- **Step.**
  - R16 (LEDGER LF154) is one of N16's rows (LEDGER LF233), and it is the row that carries CAP to N57.
  - It still cites "RK7 LF70-76; ADD LF126-159", with correction "RW LF18" and no RWE citation.
  - That range literally includes four pieces of text that RWE m1 excludes:
    - RK7 LF76, the L5 λ-gcd bullet;
    - ADD LF152–154, the five-vertex universes;
    - ADD LF157, the engine counts;
    - ADD LF159, the K5.3 bridge, which belongs to R11/N25.
  - Neither AFIBRE MIN-4 nor v6 touches R16.
- **Second gap.** v6 LF25 lists "Body/discharge ranges: RK7 …; ADD …" but does not say whether LEDGER LF66's other entries ("RKE W1-W2; WV LF23, LF38-42, items 4-5 LF49-50") remain. v6 itself relies on them: R12 points to WV LF38/LF48, and v6 says "W2 governs LF106".
- **Consequence.**
  - Under the intended reading there is no mathematical change.
  - Read literally, R16 attributes to N16, at the N57 edge, the L5 seven-piece bullet and the control universes, which RWV LF9 does not accept.
  - If v6 LF25 is read as replacing the whole cell, the only proof body for K (R12) is no longer located anywhere.
- **Repair.**
  - Rewrite R16 as "RK7 LF70 (non-L5 only), LF71–75, LF80 first sentence; ADD LF128–139, LF143–148, LF155; WV LF42; read with RWE m1, m6".
  - Add to v6 LF25: "replaces the RK7/ADD entries only; RKE W1–W2 and WV LF23, LF38–42, LF49–50 remain".
  - Optionally, write out the new R12 and R18 cells in full.

## Uncounted notes
- **"No Sun input" (v6 LF13).** P0(a) is L0.6 = Sun(2) (README LF42; LEDGER LF52). The sentence should say "no Sun(t≥3) or Sun7 input". The existing N02 edge already covers Sun(2).
- **Unannounced rename (v6 LF11).** v6 writes the 5-exponent as h_i, but README P0(c), P1(iv), RK7 LF68 and LF71–75, and ADD LF144 still write it as g. README also uses g_i for the coset representatives. Add "h_i := v_5(n_i)".
- **"(e.g. N16)" (v6 LF8).** N16 is not a consumer of INV (RWE m2); the intended meaning is "via the consumer's own N16 import".
  - RK7 LF68, where π_i is defined, is not among v6 LF25's ranges. Confirm that RW LF10–23 defines π_i.
  - INV is unaffected either way.
- **ADD LF124, second sentence.** It cites "rules-k7-v1 §4" for upward closure, which points at the excluded L8 M1 clause in LF80. RWE m8 and v6's "No excluded range is an import" neutralize this, and upward closure follows from LF124's first sentence alone.
- **Sentence fragments.** ME LF27–30 starts mid-sentence (its subject is on LF26) and ends mid-sentence (the provenance tail is on LF31). These are pointers, not premises.
- **KII predicate.** The "(Theorem R1(7)(II))" in README LF96 is covered by v6 LF11's exclusion. Writing "KII := a = 2" outright would be cleaner.
- **Priority.** The KII argument follows AFIBRE's outline (LF112–115), which is disclosed in scope LF3. v6 writes out the steps.
- **Process.** The scope file and v6 carry the identical stamp 05:36:54, so "recorded before the repair" is not witnessed at that resolution. The scope already disclaims preregistration.
- **Computation.** None was used or needed.

## Status and limits
- Once v6 is accepted, N13 and N14 are closed relative to N02, N03 (cons.), N11, N12 and N15.
- N14's Sun(3)–(6) uses rely on the F17/site-S4 convention through N12. L LF18–34 is not in the pasted text, so I have not re-checked that.
- I could not check: RW LF10–23, RKE W1–W2, WV, overlay A-1, rows H01/K01, CI62V, and the bodies of N18–N22.
- Because of m-A, v6 LF3 and LF27's claims about all consumers remain conditional.
- Not approved here: the global graph, the final join, full Sun7, and runtime. I make no novelty, Lean or human-review claim.
