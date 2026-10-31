# Lifted types — an outside-coset second-moment theorem: P spans F_2^6 at rank 6, OddSums(P) = F_2^4 at (2,160), and (3,144) at L = 8 reduced to two configurations

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:40:57 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal or novelty claim. No program was run; all arithmetic was done by hand.

No whole residue type and no whole L-value is excluded. This packet **supersedes** the direct (6,1)/(7,0) case analyses at (3,144) in `rank6-pure-coset-lemma-112-L12-and-144-L8-reduction-v1.md` (SHA `5da16610…81ab`). That earlier file stays immutable; its conclusions are consistent with this one.

## 0. Inputs

- The admitted S0017 cut: (3), (9)–(11).
- Own WRITTEN premises (unreviewed): Lemma O, and Theorems A and E, with the notation of the earlier rank-6 packets.
- Ordinary Fourier analysis: Σ_ξ σ(ξ)(−1)^{b·ξ} = 2^r c_b on U ≅ F_2^{2r}.

## 1. The defect function e and outside cosets

Let Z := {ξ ∈ U : h_0(ξ) ≡ 0} with N_0 := |Z|, and let supp := U ∖ Z. From (3):

- **Rank 6** (q = −σ): u_0 = −σ + e, where e := (3σ·1_supp + h_0)/2. Indeed, where h_0 = −σ we get u_0 = 0 and e = σ; where h_0 = σ we get u_0 = σ and e = 2σ.
- **Rank 4** (q = σ): u_0 = σ − e, where e := (3σ·1_supp − h)/2.

Let O := {ā : ā ∉ OddSums(P)}.

- By Lemma O, each ā ∈ O is monochromatic, so c_ā s_ā ∈ {−14, 10}.
- Σ ⊆ P and h_0 is an odd function of the Σ-characters, so ĥ_0 vanishes on O.
- Put G(ā) := c_ā·Walsh(σ·1_Z)(ā). Using 1_supp = 1 − 1_Z, we get, for every ā ∈ O:
  - rank 6: c_ā s_ā = −8 + (3/2)(8 − G), so **G(ā) ∈ {12, −4}**;
  - rank 4: c_ā s_ā = 4 − (3/2)(4 − G), so **G(ā) ∈ {8, −8}**.

## 2. Theorem M (outside-coset second moment)

Over ALL cosets:

- Σ_ā G(ā) = 2^r N_0, since Σ_ξ σ²·1_Z = N_0;
- Σ_ā G(ā)² = 2^{2r} N_0 (Parseval);
- hence Σ_ā (G − N_0/2^r)² = 2^{2r} N_0 − N_0².

Every ā ∈ O contributes at least min over the allowed values of (value − N_0/2^r)². Hence:

**(a) Rank 6 (2^r = 8, 64 cosets).**

```
|O|·min{(12 − N_0/8)², (4 + N_0/8)²} ≤ 64N_0 − N_0².
```

The resulting bound |O| ≤ 64(64N_0 − N_0²)/(32 + N_0)² for N_0 ≤ 32, or 64(64N_0 − N_0²)/(96 − N_0)² for N_0 ≥ 32, is maximised near N_0 = 16 or 48, where it equals 21.3.

So **|O| ≤ 21** and |OddSums(P)| ≥ 43. Since OddSums(P) ⊆ aff(P), we get **aff(P) = F_2^6, i.e. P affinely spans and |P| ≥ 7**.

As a check, a 5-flat would leave |O| ≥ 32. The two quadratic differences 512 − 32N_0 + 1.5N_0² and 4608 − 160N_0 + 1.5N_0² both have negative discriminant. This strengthens Theorem O(b), which gave dim ≥ 5.

**(b) (2,160) (2^r = 4, 16 cosets).** The budget gives N_+ = N_0 ≤ 3. Then Σ(G − N_0/4)² ≤ 16N_0 − N_0² ≤ 39, while each outside coset contributes at least (8 − 3/4)² > 52.

So **O = ∅**, i.e. OddSums(P) = F_2^4. This strengthens Theorem O(a), which allowed up to 2 outside cosets.

## 3. Consequence at (3,144), L = 8

Recall wt(h_0) ≤ 40, |P| ≥ 7 and dim aff(P) = 6 (Theorem M(a)), and the case list of Theorem R.

- **(4,2), (5,1), (6,0):** |P| = 6. Impossible.
- **(6,1):**
  - dim aff(Σ) = 5 means no relations, so N_0 = 22 and wt = 42 > 40.
  - dim aff(Σ) ≤ 4 means dim aff(P) ≤ 5. Impossible.
- **(7,0):** dim aff(Σ) = 6 means no relations, so N_0 = 21 and wt = 43 > 40. Impossible.
- **(8,0):** dim aff(Σ) = 6 leaves exactly one relation, and integrality of N_0 = (43 + 3A_4 − 9A_6 + 27A_8)/2 requires it. N_0 ≥ 24 leaves:
  - **(C1)** a single zero-sum 6-subset with g = −1: N_0 = 26, wt = 38. Then (★) gives Ξ = −34, u = 4, α = 36, ν = 2.
  - **(C2)** Σ itself zero-sum with G = +1: N_0 = 35, wt = 29. Then Ξ = (13Σ_1 − 3Σ_3)/8 ∈ {−7, −15, −23} and u ∈ {4, 12, 20}. Here complementary odd subsets pair up, the 56 triple sums are distinct, and OddSums(Σ) = F_2^6.

**Hence (3,144) at L = 8 is reduced to (C1) and (C2): eight cosets, each carrying exactly one small value, affinely spanning F_2^6.** Neither configuration is excluded here, and the (3,144) floor is NOT raised.

## 4. Status

**WRITTEN:** Theorem M (a) and (b), and the (3,144) L = 8 reduction to (C1)/(C2).

**Unchanged:**

- (3,112): L ≥ 12, and L = 12 forces |Σ| ∈ {10, 11, 12}.
- (2,160): the admitted window, with |Σ| ≥ 4 and the four-coset strata.
- The (24,24,2) gap and the original problem remain OPEN.

Novelty is UNCLEARED. All earlier findings are retained, including the permanent v167 reviewer read-order PROCESS MAJOR, the cadence MAJORs, the checkpoint-054 attribution MINOR and the s = 6 erratum MINOR. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT; no early park.
