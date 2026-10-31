# Balanced NL242 (3,112) — L = 12 is impossible, so L ≥ 14

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:47:36 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** The residue type (polar rank 6, weight 112) only. The type, the (24,24,2) gap and the original problem remain OPEN.

## 0. Inputs

Admitted:

- S0017 (3) and (9)–(11), giving α + 2ν = 30 − L − u/2.
- Gate III.

Own WRITTEN premises (unreviewed):

- Theorem A (u ≡ 4 mod 8), Lemma B and Corollary C (L even).
- Lemma O; Theorem M(a) (aff(P) = F_2^6, |P| ≥ 7), from `lifted-outside-coset-second-moment-and-144-L8-reduction-v1.md` (SHA `5c204162…bbb1`).
- The N_0 formulas and (★) 3wt(h_0) + Ξ = 60 − 2L − u, from `rank6-112-erratum-and-L10-exclusion-addendum-v1.md` (SHA `520f1484…41d4`).
- Theorem R′ (L ≥ 12).

Ordinary fact used: in a binary linear code of dimension k, each coordinate that is not identically zero equals 1 in exactly 2^{k−1} codewords. Hence Σ_{c} wt(c) ≤ 2^{k−1}·n.

## 1. Theorem R″ (L = 12 is impossible at (3,112))

*Proof.* At L = 12 we have wt(h_0) ≤ 18 − u/2 ≤ 16, so N_0 ≥ 48, and (★) reads 3wt + Ξ = 36 − u ≤ 32. Also |Σ| + 2|P∖Σ| ≤ 12, |P| ≥ 7 and dim aff(P) = 6. Write s := |Σ|.

- **s = 0, 1:** |P| ≤ 6. Impossible.
- **s = 2, 3, 5, 6, 7:** N_0 = 32, 16, ≤ 32, ≤ 40, ≤ 42 respectively, all < 48.
- **s = 4:** N_0 ≥ 48 forces a flat with G = +1. Then (★) gives Ξ ≤ −16, but |Ξ| ≤ 8.
- **s = 8,** with |P∖Σ| ≤ 2, so dim aff(Σ) ≥ 4:
  - dim aff(Σ) = 3 gives dim aff(P) ≤ 5. Impossible.
  - Otherwise 3A_4 − 9A_6 + 27A_8 ≥ 53 is needed. The maximum is 45 when dim aff = 4 and ΣΣ = 0, 39 when dim aff = 4 and ΣΣ ≠ 0, and 33 when dim aff ≥ 5.
- **s = 9:** this needs −A_4 + 3A_6 − 9A_8 ≥ 36. With dim aff(Σ) ≥ 5 the dependency code R has dimension ≤ 3 and the value is ≤ 19. (Even at dimension 4 the maximum is 31; see the pure-coset packet.)
- **s = 10,** with dim aff(Σ) ≥ 5, so dim R ≤ 4, Σwt(R) ≤ 80 and n_4 + n_6 + n_8 + n_10 ≤ 15. This needs A_4 − 3A_6 + 9A_8 − 27A_10 ≥ 71.
  - If ΣΣ = 0: Σ is a relation and the other relations pair as complements of sizes (4, 6). With g(T_6) = G·g(T_4), each pair contributes at most 4 when G = −1 (and −27A_10 = 27), or at most 2 when G = +1 (and −27A_10 = −27). So the value is ≤ 55.
  - If ΣΣ ≠ 0: 4n_4 + 6n_6 + 8n_8 ≤ 80 gives 2n_6 + 4n_8 ≤ 20, so the value is ≤ 15 + 2n_6 + 8n_8 ≤ 55.
  - In both cases 55 < 71.
- **s = 11:** P = Σ, dim R = 4 and Σwt ≤ 88. This needs −9A_4 + 27A_6 − 81A_8 + 243A_10 ≥ 1281.
  - Here n_10 ≤ 1, since the complement of a 10-subset is the single point ΣΣ.
  - Maximising 9n_4 + 27n_6 + 81n_8 + 243n_10 subject to these constraints gives at most 126 + 378 + 243 = 747. That is < 1281.
- **s = 12:** P = Σ, dim R = 5 and Σwt ≤ 192. This needs X = 1 + 9A_4 − 27A_6 + 81A_8 − 243A_10 + 729A_12 ≥ 2560.
  - If ΣΣ = 0: relations pair as (4, 8) or (6, 6), with 15 pairs in all. Then X ≤ 1 + 729 + 90·15 = 2080.
  - If ΣΣ ≠ 0: n_10 ≤ 6 (disjoint pairs summing to ΣΣ), and 2n_6 + 4n_8 + 6n_10 ≤ 68. Then X ≤ 1 + 279 + 9·220 = 2260.
  - Both are < 2560.

Every case fails. ∎

**Corollary.** At (3,112), every balanced peak-28 target has **L ≥ 14**, with L even. This is up from the admitted Gate III floor of 8 and from the own L ≥ 12 of Theorem R′. The result depends on the own unreviewed chain (Theorems A, M, O, R′ and Lemma B); adoption requires reviewing the whole chain.

## 2. What remains at L = 14 (not excluded)

- Σ = ∅ with seven balanced cosets is excluded at L = 14. In that case wt = Ξ = 0, and (★) forces u = 32, which contradicts u ≡ 4 (mod 8).
- The configuration "affine 3-flat Σ with g = ±character (A_4 = 14, G = +1, N_0 = 56, wt = 8) plus three balanced cosets spanning F_2^6" passes every test used here:
  - OddSums(P) = F_2^6;
  - (★) gives Ξ = 8 − u with Σ c g ∈ {±4} and u ∈ {4, 12}.
- The other values of s at L = 14 were not analysed.

## Status

**WRITTEN:** Theorem R″, giving L ≥ 14 at (3,112).

**Own WRITTEN rank-6 floors:**

- (3,112): L ≥ 14.
- (3,144): L ≥ 10.
- (3,128): untreated, admitted L ≥ 8.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All earlier findings are retained, including the permanent v167 reviewer read-order PROCESS MAJOR, the cadence MAJORs, the checkpoint-054 attribution MINOR and the s = 6 erratum MINOR. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT; no early park.
