# v205 source-separated results: index, dependency DAG and remaining gaps

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:49:20 PDT 2026**.

**Authority.** `NL-post-v167-whole-read-qualified-original-direction-v205.json` was read ENTIRE. All work below is prospective and source-separated:

- Admitted inputs are used only at their exact cuts: S0017, the canonical bridge, and the floors of Gates I–III.
- These remain ZERO/NONINPUT and were not read in this session: the HELD u8/L14 lead, the v147-F1 and v112 scouts, and the unreviewed own candidates v2–v12.
- The d128/u8 branch is untouched.

**Assurance.** Every item below is a **WRITTEN author candidate**: unreviewed and unadopted, with no machine, formal or kernel check and novelty UNCLEARED. Hand arithmetic only, under HOLD v2.

## A. Files (own root, all immutable once pinned)

| # | File | SHA-256 | Content |
|---|---|---|---|
| 1 | global-exact-occupancy-identity-and-lifted-coset-structure-v1.md | 4ddecaa0…929f | §§1–3 restate the ADMITTED S0017 (see #2). New in it: lifted coset census, ℓ28 rewrite, zero-set degree bound |
| 2 | global-exact-occupancy-identity-attribution-erratum-v1.md | b0372223…7024 | OWN MINOR attribution erratum to #1 |
| 3 | u-class-L-parity-and-rank4-160-coset-projection-v1.md | 7cecd509…0c9b | Theorem A (u ≡ c_d mod 8, every type); Lemma B; Corollary C (L even at polar ranks 2/4/6); Proposition D; Theorem E (\|Σ\| ≥ 4 at (2,160)); Proposition F (Z_3 identity) |
| 4 | rank4-160-four-coset-strata-Q-shape-and-R-side-reduction-v1.md | 5517814f…7962 | Q-shape lemma and R-side reduction of the \|Σ\| = 4 strata |
| 5 | rank4-160-four-coset-slice-count-mod4-addendum-v1.md | b45484ec…a5e4 | Lemma S (mod-4 slice count); Lemma U (row-uniform parity) |
| 6 | lifted-odd-sum-support-and-affine-spanning-small-cosets-v1.md | 66981733…c7ce | Lemma O (odd-sum support); Theorem O (affine spanning); Corollary O2 |
| 7 | rank6-112-coset-projection-L8-exclusion-v1.md | 7b533fa5…3ed7 | Theorem R: (3,112) has no L ≤ 8 (the s = 6 row is corrected in #8) |
| 8 | rank6-112-erratum-and-L10-exclusion-addendum-v1.md | 520f1484…41d4 | OWN MINOR s = 6 erratum; general N_0, φ and Ξ formulas; (★); Theorem R′: (3,112) L ≥ 12 |
| 9 | rank6-pure-coset-lemma-112-L12-and-144-L8-reduction-v1.md | 5da16610…81ab | Lemma PC; L = 12 survivors (I)/(II) excluded; (3,144) partial reduction, superseded by #10 |
| 10 | lifted-outside-coset-second-moment-and-144-L8-reduction-v1.md | 5c204162…bbb1 | Theorem M: rank 6 aff(P) = F_2^6; (2,160) OddSums(P) = F_2^4; (3,144) L = 8 reduced to (C1)/(C2) |
| 11 | rank6-144-slice-value-lemma-L8-exclusion-v1.md | 3f9e20f6…2de2 | Lemma SV; Theorem S: (3,144) L ≥ 10 |
| 12 | rank6-112-L12-exclusion-L14-v1.md | 18613ab3…b6fd | Theorem R″: (3,112) L ≥ 14 |

Checkpoints 053–063 (own root) record the clocks.

## B. Dependency DAG (for any future review)

- **Admitted base.** The canonical bridge, and S0017 (3), (5)–(13) at the Gate I parent cut. Gate II: L ≥ 10 at (2,160). Gate III: L ≥ 8 at rank 6.
- **Theorem A** ← R(0) = 0 and S0017 (9).
- **Lemma B** ← S0017 (6) and R ≡ 8D (mod 16).
- **Corollary C** ← A, B and S0017 (10)/(11).
- **Lemma O** ← S0017 (3), plus q = 0 off U.
- **Theorem M(a)/(b)** ← Lemma O, S0017 (3) and Parseval.
- **(3,112) floor:**
  - **Theorem R** (L ≤ 8 impossible) ← A, B, C, O(b) [superseded by M(a)], the N_0 table (corrected in #8) and S0017 (11).
  - **Theorem R′** (L ≠ 10) ← R's inputs, plus (★) and the flat Ξ bound.
  - **Theorem R″** (L ≠ 12) ← M(a), N_0 and binary-code weight sums.
  - **Result: L ≥ 14.**
- **(3,144) floor:** **Theorem S** (L ≠ 8) ← M(a), (★) with the d = 144 budget, and Lemma SV (pure-coset slice values {0, ±6, ±12}, plus Parseval on F_2^2). **Result: L ≥ 10.**
- **(2,160):**
  - **Theorem E** ← Proposition D (projection of S0017 (3)), A, Corollary C and Gate II.
  - **Corollary O2 / Lemma S** ← O and Proposition F.
  - **Window:** L ∈ {10, …, 24}, even, with L ≡ 2α (mod 4); |Σ| ≥ 4; OddSums(P) = F_2^4.

## C. What is now proved (WRITTEN, own) versus the admitted floors

| Type | Admitted | Own WRITTEN after v205 work | Status |
|---|---|---|---|
| (1,192) | conditional at FULL J_U2 | L ≡ 0 (mod 4) (Corollary C); u ≡ 0 (mod 8) | not re-examined |
| (2,128) | historically excluded | reproved reduction to L = 4, u = 8 (S0017 §6 closes it) | old |
| (2,160) | L ≥ 10 | L even, L ≤ 24, \|Σ\| ≥ 4, \|Σ\| = 4 strata structured | OPEN |
| (3,112) | L ≥ 8 | **L ≥ 14** | OPEN |
| (3,128) | L ≥ 8 | untouched (avoided branch) | OPEN |
| (3,144) | L ≥ 8 | **L ≥ 10** | OPEN |
| (4,120) and (4,136) | sparse L ≥ 4 | u ≡ 6 or 2 (mod 8); L + N_+ = 46 − 3t or 55 − 3t | OPEN |

**No residue type is excluded. The (24,24,2) gap and the original balanced nine-variable NL242 problem remain OPEN.**

## D. First unproved steps

- **(3,112) at L = 14.** Exclude the affine 3-flat Σ with g = ±character plus three balanced cosets, and the other values of s.
- **(3,144) at L = 10.** The configurations (6,2)-b, (7,1), (8,0)-C1′/C2′, (8,1), (9,0) and (10,0) pass N_0 and dim-aff. Lemma SV slice analysis is needed.
- **(2,160).** The extremal stratum (u_0 = −σ, α = N_+ = 0, L ∈ {16, 20, 24}) survives every projection test. A genuinely 2-dimensional slice-level obstruction is needed.
- **Rank 8.** There is no slice structure. Z_3 = N_+ ≤ 46 − L (or 55 − L) forces affine dependencies in supp δ, but a configuration on a 2-flat survives at L = 4. New tools are needed.

## E. Findings retained

- The permanent v167 reviewer serial-read-order PROCESS MAJOR.
- The earlier cadence MAJORs: 049 FULL 11h47m06, post-147 FULL 3h43m59, v147-F2 FULL 1h50m49 and 021 FULL 52m32.
- The checkpoint-054 OWN attribution MINOR.
- The checkpoint-059 OWN s = 6 erratum MINOR.

Same 18 owners, OWN root and HOLD. Science cutoff 2026-10-27T11:05:38-07:00; deadline 12:35:38. This is an index, not the final park.
