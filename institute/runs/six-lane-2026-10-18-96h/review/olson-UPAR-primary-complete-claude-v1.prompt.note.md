# UPAR v1: independent tool-less review (full packet, including the six appended UMR ranges)

**Basis.** I read the literal text pasted here and nothing else. Premises are literal UMR at its accepted scope and accepted UFC U0/E0/ENV. I did not re-audit UMR's own proofs of Lemmas 7, 8, 10 and 13. No earlier model verdict on UPAR was used. Hashes, byte counts and filenames were treated as metadata and not checked.

## Verdict

| Layer | FATAL | MAJOR | MINOR |
|---|---|---|---|
| Proof (mathematics + primary import binding) | 0 | 0 | 4 |
| Scope / checkpoints / process | 0 | 0 | 2 |

- **UPAR-P is correct as stated** on T_PAR.
- **UPAR-R is correct as stated**: it gives a complete two-type R_PAR.
- **Full T is not excluded.** PAR-COVER remains unproved.
- **Named cells:** (12,29) and (13,31) are proved. (13,29), (14,31) and (17,37) remain open.
- Status stays candidate, pending the second model family and the parent hand check.

## 1. Primary import binding (checked line by line)

- **(W)** `proof-UPAR-v1.md:50` comes from `proof-UMR-v1.md:163-165` plus UMR-F (`:24-28`).
  - Lower end: low = Π₀+2−y−2p. Using Π₀ = B*−ν₀, B* = R+e* and 2p−R = 2d, this equals e−2d+2−ν−y. ✓
  - Upper end: up = −2−ν+x. ✓
  - x and y come from UMR `:138`; ℓ and M come from UMR `:64-66` with g = 2d. ✓
- **All-run parity (D2):** UMR `:202` gives θ_i ≡ σ_i. UMR `:109` gives σ_i = Σc_l with every c_l odd. Together, θ_i ≡ |L_i| (mod 2). Empty runs have nonzero even θ (UMR `:203`). ✓
- **Letter counts:**
  - q = |L△A| and the α/β splits come from UMR `:117-118`. ✓
  - ν₀ ≥ a and a′ ≥ (3κ+g)/2 come from UMR `:118`.
  - e ≥ ν−a is immediate.
- **Set structure:**
  - Independence, m(Q) = |Q| and central ≤ h−1 come from UMR `:252-253`; this needs d ≥ 2. ✓
  - Ξ and (ID) come from UMR `:254-258`.
- **Bounds:** |θ| < 2p comes from UMR `:203`. max|c| ≤ p−6 and the reservoir come from UMR `:90-91`. ✓
- **UB:** G±, Z± and lo/hi (with g = 2d) match UMR `:266-274,300-302` literally.
- **Lemma 20:** matches UMR `:315-324` literally, except MINOR-2.
  - The `:322` cap is correctly confined to the 2nd and 3rd alternatives of (i).
- **Lemma 13 restriction** (erratum v1): no level above κ+1 is used. Lemma 2 may use r = κ+1, which UMR-F covers. ✓
- **UFC imports:** E0, ρ and C/D/H are restated faithfully from UFC `:200-226`.
- **U1 is not load-bearing.** The citation at `:279-281` is redundant. Every R_PAR test is re-derivable from the lines above, and the ENV test is implied because B ≤ H.

## 2. New derivations, re-derived

**Parameters (Bal).**
- h = 2j−ε, κ = 2j−ε−d, j ≥ 5, j ≥ d+2+ε, κ ≥ j+2. ✓
- ℓ_j and M_j as stated; a′ ≥ 3j−(d+3ε)/2. ✓
- T0 ⟺ j ≤ 2d+1 ⟺ κ ≤ 3d+2−ε, in both residue classes. ✓
- T1 ⟺ j ≤ 2d+2. ✓

**Lemma 1 and the upper types** (`:66-81`).
- R−(δ+2) = 2κ+4d−4 = p+2d−3. ✓
- Q and P cannot hold together. x = ℓ−q on Q and x = M−q′ on P. ✓
- Near-A: Θ+l ≤ 2κ−2r−(ν−a)−2α. ✓
- Majority: q′−l = a′−2β, which gives 2β ≥ a′+ν+2d+2. ✓

**(Scalar) and (Mass-bound)** (`:93-98`): all four constants check, using h−d = κ.

**Lemma 2** (`:102-107`) ✓.
- c ≤ (δ+2)/2 = κ−d+1, so r = d+c lies in [d+1, κ+1].
- At that level ℓ−q′ ≤ δ+1−R < 0, and 2c−a ∈ {1,2} dominates ε, so y = 2c−a.
- The lower window is then (e−(ν−a))−2r+2 ≥ −2r+2, which exceeds the empty-run sum ≤ −2r.
- Only the label excess is used, not the total identity.

**Lemma 3** (`:109-122`) ✓.
- The top upper sum is ≤ 2j−2d−2 < 2j, so t_j ≤ 1.
- With t_j = 1: ν+z ≤ L, and outside letters ≤ α+α′ ≤ a+z.
- The opposite top exceeds M_j−2 by at least (7d+8−3ε)/2, so it is not P_j.
- δ+1−L = 3j−2d−2ε+3 > 0.
- Counting runs of S′: h ≤ (d+c−1)+(j−1)+λ, and κ−j+2 = L+d+4−ε.
- ⌈(L+1)/2⌉ ≥ m ⟺ L ≥ 2m−2, so L ≥ 2d+6−2ε and κ = 2L+3d+4−ε ≥ 7d+16−5ε.

**Lemma 4** (`:126-142`) ✓.
- Constants: g₀ = j−κ−1, p₀ = j+ε−d−2, c₀ = 2ε−d−2.
- The case table is complete:

| Pair | Bound | Note |
|---|---|---|
| G/G | 2g₀ < 0 | |
| G/Q | −1 | |
| G/P⁻ | 2ε−3 | |
| G/P⁰ | 4ε−2d−5−z | E(B′) ≥ b−l(B′); l(B)+l(B′) ≤ a+z ≤ M−2; c₀+g₀−b+M−2 = 4ε−2d−5 |
| Q/P, either sign | c₀−d | (Mass) correctly oriented (P-top q′, Q-top q) |
| P/P | 2p₀−a′ < 0, or 2c₀+M−2−a′ < 0 if one threshold is 0 | z₁+z₂ ≥ a′; density values as stated |
| P⁺/P | impossible | Lemma 3 |

- Only Q/Q and P⁺ remain.

**Lemma 5** ✓.
- l(J_i) ≤ α_{3−i}+β_i.
- The deficit sum gives z₁+z₂ ≥ 4r−2κ+ν.
- The mixed ⌈·/3⌉ bound follows from the t = −1 top inequality.

**Lemma 6** (`:157-175`) ✓. Thresholds t_s are nonincreasing in s.
- **(a)** At r* the bound is 6d−2κ−ν < 0, using κ > 3d.
  - Both strong: ≤ −2d.
  - Mixed: the coefficient is 0, so a nonnegative sum forces z₁ = z₂ = 0.
  - Then L(J₁) = L(J₂) = A and the two sets are disjoint, so A = ∅.
  - The run with θ = −1 would then be empty, contradicting parity.
- **(b)** A generic-only exit gives −1 or 2(r−κ).
- **Use of the PREVIOUS opposite Q is legitimate.** Both tops were Q_r with t_r ≤ −1. So S′'s bound κ−r−z_Q−E(B_r(S′)) holds whatever S′'s type is at r+1.
- **Bottom count:** (h−r−1)+(h−r) = 2h−2r−1 runs. (Mass) on (J_{r+1}(S), J_r(S′)) gives empties ≥ 2h−2r−1−z_P−z_Q.
  - The sum is 4r−2κ−4d+2. ✓
- **(Jump):** q(J_{r+1}) = q(J_r)+β(u)−β′(u). The caps 2κ−2r and 2r−2d sum to δ, so β(u) ≥ R−δ = 2κ+4d−2.

**UPAR-P for κ ≤ 4d** (`:177-182`) ✓.
- Outside T0: j ≥ 2d+2, so κ ≥ 3d+4−ε > 3d and r*−j ≥ 1.
- P⁺ would need κ ≥ 7d+11, so it is excluded.
- Any P exit gives (Exit) ≤ 2κ−8d−2 ≤ −2.

**Theorem 8** (`:186-194`) ✓ for every d ≥ 2.
- Membership in T: 2d+3 < 3d+4 ≤ 4d+2. Also h = 4d+4, j = 2d+2, r* = 2d+4.
- A P exit at r = j gives 2−2d.
- A generic exit gives −1.
- If both tops stay Q at j+1, Lemma 5 gives:
  - both t = −1: −2−ν;
  - both strong: −2d;
  - mixed: 1−⌈(2d+4)/3⌉ ≤ −2.
- The extra level is genuinely needed: Lemma 6's (Exit) at r = j+1 is 6−2d, which is ≥ 0 for d = 2, 3.

**T1 boundary with ε = 1** (`:196-198`) ✓. Here p = 8d+5 and κ = 3d+3, which is ≤ 4d iff d ≥ 3. For d = 2, p = 21 = 3·7 is not prime.

## 3. Coverage of T∖T_PAR ✓

- **Where the residual sits.** Outside T_PAR, κ > 4d and j ≥ 2d+3, so r* ≥ j+2.
- **(P⁺) branch.** After Lemma 4 the only survivors are (P⁺) and Q/Q. Every (P⁺) test is a proved consequence (Lemma 3 and the Sec. 1 majority bound).
- **(LJ) branch.** On Q/Q, Lemma 6 leaves exactly a P exit at r+1 with r ∈ [max(j, ⌈(κ+2d−1)/2⌉), κ−d−1].
- **Extra (LJ) exclusions:**
  - A second P exit is impossible: 2(2κ+4d−2)−R = 6d−2 > 0.
  - A both-strong predecessor is excluded.
- **Tests retained.** R0–R2 retain the literal UMR data and windows, the bounds, E0, ENV (via B ≤ H), the UB predicates, and both Lemma 20 clauses.
- **Nothing dropped.** Both residue classes and all large parameters are kept.
- **No overclaim.** There is no existence, converse, inverse or no-go claim. "Equivalent exclusion target" is correct: UPAR-R gives one direction, and the converse holds vacuously.

## 4. Named cells (every constant recomputed)

| Cell | d, ε, j, r* | N, h, R, δ | Result |
|---|---|---|---|
| (12,29) | 3, 1, 8, 9 | 30, 15, 52, 18 | **PROVED.** Not T0 (11.5 < 12). P⁺ needs 32. Exit at r=8: −2. At r*=9: −6−ν / −6 / mixed coefficient 0. |
| (13,31) | 3, 0, 8, 10 | 32, 16, 56, 20 | **PROVED.** Theorem 8 at d=3: −4 / −2−ν / −6 / 1−4. |
| (13,29) | 2, 1, 8, 11 | 30, 15, 54, 22 | OPEN (LJ). Caps 26−2s and 2r−4; β ≥ 32. |
| (14,31) | 2, 0, 8, 12 | 32, 16, 58, 24 | OPEN (LJ). Caps 28−2s and 2r−4; β ≥ 34. |
| (17,37) | 2, 1, 10, 15 | 38, 19, 70, 30 | OPEN (LJ). Caps 34−2s and 2r−4; β ≥ 40. |

- **P⁺ thresholds:** 25, 30 and 25. ✓
- **Sec. 7 second table** (`:310-317`) ✓:
  - a′: 22 / 23 / 28;
  - max|c|: 23 / 25 / 31;
  - reservoir: +25 / +27 / +33;
  - θ bound: 58 / 62 / 74;
  - hi_s: 72 / 77 / 92 − 3s;
  - giant-pair threshold: 32 / 34 / 40;
  - δ−2: 20 / 22 / 28, and δ: 22 / 24 / 30;
  - Θ(all) = e−2ν−4.

## 5. Proof findings

**MINOR-1 (statement precision)** — `proof-UPAR-v1.md:19-23,196-199`; package `:9-11,18`.
- T_PAR ∖ {κ ≤ 4d} is exactly {(10,23), (13,31)}.
- For d ≥ 4 the half-boundary family already lies in κ ≤ 4d, since 3d+4 ≤ 4d.
- At d = 2 the family is (10,23). That cell's exclusion by Theorem 8 is never stated in the outcomes.

**MINOR-2 (literal import)** — `:257,318`.
- "no empty tail" is an undefined paraphrase.
- It should read "no run of S′∖P_(S′) is empty", as in UMR `:320-321` and UFC `:256`.

**MINOR-3 (residual not reduced by the packet's own Lemma 5)** — `:271,300-305`; package `:19-21`.
- At the predecessor r, both tops are Q_r with negative thresholds.
- So (QQ-1) and (QQ-mixed) apply there, not only the both-strong case used at `:271`.
- For the named cells, survival then requires:
  - (13,29): r = 8 only;
  - (14,31): r = 9 only;
  - (17,37): r ∈ {10, 11}.
- The displayed ranges are still valid supersets, so completeness is unaffected. But "allowed predecessor r" overstates what is actually left open.

**MINOR-4 (interface table)** — `:331` (also `:55`).
- The UMR range list omits `:266-274,300-302,315-324`, which (R2) imports at `:252-253`.
- An interface erratum is needed.

## 6. Process findings (reviewed separately)

**Checked and consistent:**
- **Freeze and cadence:** the authority is timestamped 04:12:06 and the freeze 04:13:04. I recomputed the checkpoint gaps as 971 / 780 / 148 / 920 / 108 / 252 s; all are ≤ 1200. The pre-freeze operations (scope `:65-67`) are self-attested and not verifiable here.
- **Prior exposure:** the unwritten observation "r ≤ κ/2" disclosed at scope `:59-61` is exactly `:77-78`. It is re-derived in the proof and correct.
- **Unused routes:** those at cp-01 `:13-15` and cp-02 `:19-20` are disclosed and are not premises. I did not review them.

**MINOR-P1 (manifest completeness)** — package `:53-56`.
- The package claims "exact UMR ranges … Hashes match pins".
- In fact the manifest omitted six cited primary ranges, as recorded in the completeness note.
- These are cured for this review. A verdict based only on the Codex v1 prompt does not cover the binding of (D2), (W), UB or Lemma 20.

**MINOR-P2 (overlap with the author's own FC1023 cell)**
- Theorem 8 at d = 2 re-excludes FC1023's cell using FC1023's own structure. Scope `:56-58` lists levels 6/7 and a positive-P6 pair, which are levels j, j+1 and P_j at d = 2.
- No FC1023 lemma is used as a premise. ✓
- However, the overlap is only alluded to ("p23 cell", `:194`).
- It should be stated in the outcomes and checkpoints. It must not be booked as independent corroboration of FC1023.

**Uncounted observations:**
- The `:3` timestamp is the drafting date; the file was created after cp-04 (05:00:03). "After" is accurate.
- cp-03 read UFC `:192-277`, while the proof cites `:200-263`. This is harmless.

## 7. Exact theorem (no correction needed; precise form)

**UPAR-P.** For every (κ,p) ∈ T with 5κ ≤ 2(p+1), and for (κ,p) ∈ {(10,23), (13,31)}, every frame of every target NF has Ξ(S_ev)+Ξ(S_od) ≤ −1. By UMR (ID), no target NF exists there. This set is exactly the paper's T_PAR.

**UPAR-R** holds as written at `:236-275`. It may optionally be sharpened by MINOR-3. PAR-COVER remains unproved.

**Reviewer remark (not part of this verdict; uncertified, needs its own written check).** Adding Lemma 5 at the predecessor r appears to empty (LJ) whenever κ ≤ 6d−4, i.e. 7κ ≤ 3p−1. Using 2r ≥ κ+2d−1:
- both t_r = −1: the bound is ≤ κ−6d+3 ≤ −1;
- mixed: the bound is ≤ (3κ−20d+7)/6 < 0;
- P⁺ needs κ ≥ 7d+11, so it is excluded.

Under that remark, the first new cells would appear at d = 4: (17,41), (18,43) and (20,47). Rounding would also close (16,37). None of the five named outcomes changes, because they have d = 2, where 6d−4 = 4d.
