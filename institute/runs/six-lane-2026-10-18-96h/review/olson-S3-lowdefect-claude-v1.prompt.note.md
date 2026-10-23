# Hostile review: S3 low-defect P1/P2/P3 (not general S3)

**Bottom line.** All three exclusions are correct as written. There are no FATAL or MAJOR findings. The required fixes cover scope wording, status wording and explicitness. None of them repairs a mathematical gap.

**What was read**
- The package and the full candidate, l.1–85. I cite the candidate as **C:n**; its path is `.../stab-round2/proof-S3-lowdefect-core-v1.md`.
- The frozen scope, l.1–23.
- All 21 embedded excerpts from 17 files, which matches the package's §5 count.

**Trust boundary**
- I did not recompute any SHA256 (no tools were allowed). These verdicts bind to the embedded text.
- The candidate's P1–P3 match frozen scope l.14–21 with no drift.
- I checked the status of L1 and B2-1 directly against verdict 9df92bda l.10–11 (cited **V:n**), not against the package's paraphrase.
- The package's comparison claims about I-small (§2 table) cannot be checked from the excerpts. They are not load-bearing.

**No outside input.** Every check below is a written derivation from C and the accepted interfaces listed later. I used none of the following:
- index-one, AP', greedy, I-small, Zeng–Yuan or Savchev–Chen;
- the Lev few-sums theorem;
- LS(17,12) or LS(23,16), except where flagged under remaining targets.

## Verdicts

| Claim | Verdict | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| P1: standalone packing, n ≥ 2m+3 | ACCEPT-WITH-FIXES | 0 | 0 | P1-1, P1-2 |
| P2: δ0 ≠ 2 | ACCEPT-WITH-FIXES | 0 | 0 | P2-1 |
| P3: δ' ≠ 1 | ACCEPT-WITH-FIXES | 0 | 0 | P3-1, P3-2 (optional) |
| Shared / residual | — | 0 | 0 | S-1, S-2, R-1, R-2 |

Shared findings are listed once. Do not add them into per-claim counts.

## Setting (C:10–19): checks out

- **Sizes.** |Y| = 14m and |U| = 14m − (2p − d) = 2m+2+d.
- **(F\*).** |U| + 2h = 6m−2+d ≤ 8m−5 ≤ 2p. So CF(a)(F) yields (F\*) for every occurrence W ≤ U, with no size restriction.
- **Z0 and U'.** (F\*) at ρ = 0 gives |Z0| ≤ d−1. Maximality makes U' zero-sum-free.
- **(F').** This is (F\*) applied to the occurrence-disjoint union W' ∪ Z0.

## P1 (C:25–49): ACCEPT-WITH-FIXES

I re-derived P1 independently, and every step holds.

**1. Prefix sums and symmetry (C:28–32)**
- S is zero-sum-free. Prefix sums give |A| ≥ n+1 ≥ 2m+4, and σ ∈ [h+1, p−1].
- Occurrence complements, including the empty and full sub-multisets, give A = σ − A.
- So A misses both [1,h] and [σ−h, σ−1]. Both arcs lie inside [1, p−2].
- The two arcs are disjoint exactly when σ ≥ 2h+1 = 4m−3. In that case |A| ≤ p − 2h = 2m+3, a contradiction.
- Hence σ ≤ 4m−4, so σ−h ≤ h. The union is [1, σ−1], and Q = −S has every nonempty sum in [1,B], with B = p−σ ∈ [2m+3, 4m].

**2. The interval J (C:33–35)**
- Take a proper nonempty V1 of V with residue x ∈ [1,B]. Its complement has residue 1−x.
- If x = 1, the complement has residue 0 ∉ [1,B].
- If x ≥ 2, the complement's residue p+1−x lies in [1,B] exactly when x ≥ 6m−B.
- So J = [6m−B, B], and 6m−B ≥ 2m. When B ≤ 3m−1, J is empty, which is a contradiction because t ≥ 3 gives singleton subsets.

**3. Case 3m ≤ B ≤ 4m−1 (C:36–39)**
- Pair sums lie in [12m−2B, 2B]. Here 12m−2B > B and 2B < 2p.
- A pair sum below p has residue above B; a pair sum equal to p has residue 0. So the pair sum is p+y with y ∈ J, hence at least 12m−1−B.
- t ≥ 4: a proper triple is a lifted pair plus a third term, so its sum lies in [18m−1−2B, 3B] ⊆ [10m+1, 12m−3] ⊆ (p, 2p). Its residue is in [4m+2, 6m−2], above B.
- t = 3: the sum lies in [18m−3B, 3B] ⊆ [6m+3, 12m−3]. This misses both 6m and 12m−1.
- At B = 3m the t ≥ 4 window is empty, which is harmless.

**4. Case B = 4m (C:40–44)**
- Here J = [2m, 4m]. For integer sums 4m ≤ S ≤ 12m = 2p+2, the residue is:
  - S, when S < p;
  - 0, when S = p or S = 2p;
  - S−p, when p < S < 2p;
  - 1 or 2, when S = 2p+1 or 2p+2.
- Since m ≥ 3, the residues 0, 1, 2 are all outside J.
- Pairs: the sum is 4m (both terms 2m), 8m−1 or 8m.
- Proper triples: the sum lies in [8m−1, 10m−1].
  - A high pair forces the third term to be 2m.
  - Pairing that 2m with each other term z gives 2m+z ≤ 6m, so the sum must be 4m and z = 2m. This contradicts the high pair.
  - With no high pair, the triple is (2m)³ with residue 1 ∉ J.
- So t = 3, and the total is 6m or 12m−1.
  - A total of 6m forces (2m)³.
  - A total of 12m−1 makes each pair sum 12m−1−z_k ∈ [8m−1, 10m−1], which must be 8m−1 or 8m. Hence z_k ∈ {4m−1, 4m}, giving (4m−1, 4m, 4m).

**5. Extension to a term y outside V (C:45–48)**
- y has a representative in [1, 4m]. Each set {y} ∪ V1 is an occurrence sub-multiset of Q.
- Case (2m)³:
  - y+1 ≤ 4m.
  - y+4m must be ≥ 6m, so y ≥ 2m.
  - y+2m must be ≤ 4m, since 6m−1 ≡ 0. So y = 2m.
  - Hence Q = (2m)^n. With n ≥ 5, five copies give 10m ≡ 4m+1 > B, a contradiction.
- Case (4m−1, 4m, 4m):
  - y ≤ 4m−1 and y ≥ 2m.
  - y ≠ 2m, because y+4m−1 would equal p.
  - Then y+8m−1 ∈ [10m, 12m−2] has residue y+2m ∈ [4m+1, 6m−1], where 6m−1 ≡ 0. This is outside [1, 4m].

No rectification is assumed anywhere. Every residue is computed from an integer sum of at most five representatives, compared against p and 2p.

**Audit of every use of the length n**

| Use | Location | Needs | Supplied by n ≥ 2m+3 |
|---|---|---|---|
| Rule out σ ≥ 4m−3 | C:29–30 | \|A\| ≥ 2m+4 | ✓ |
| B ≥ n ≥ 2m+3 | C:32 | Unused afterwards | (true, idle) |
| B ≤ 4m | C:31 | σ ≥ h+1 only | Independent of n |
| J, pair and triple analysis | C:33–44 | Depends only on B and t | Independent of n |
| A term y outside V | C:45 | n ≥ 4 | n ≥ 9 ✓ |
| Five copies of 2m | C:46, 49 | n ≥ 5 | ✓ |

- No step uses n = 2m+3 or any upper bound on n.
- The hypothesis is consistent exactly when 2m+3 ≤ n ≤ 4m.
  - S = (−1)^n satisfies it in that range.
  - For n > 4m it contradicts n ≤ B ≤ 4m.
  - So P1 is not vacuous at n = 2m+4, the length P2 needs.
- P1 is proved in-file. It does not lean on B2-1, or on Sublemma(a), which keeps |V| = 2m+3 exactly (V:11).

**P1-1 MINOR (C:32).**
- **Problem.** The sentence "This is the only place the old proof used |S|=2m+3" is false as an inventory of the source. B2-1(f) also used the exact length: "2m + 3 ≥ 4 terms" and "(2m)^(2m+3)… five of its terms" (source l.56, l.58).
- **Effect.** The candidate's own proof is unaffected, because C:45–46 and C:49 use n ≥ 9 instead. But this sentence is precisely the equality-use inventory under review.
- **Minimal fix.** Replace it with: "The exact length entered the source at (a) (|A| ≥ 2m+4), (b) (B ≥ 2m+3, unused in the case split) and (f) (a fourth term; five copies of 2m). Here n+1 ≥ 2m+4 and n ≥ 9 supply all of these."

**P1-2 MINOR (C:31, 34, 37, 40, 44, 45).** P1 is a standalone re-proof, not an import. It should therefore write out the steps that the accepted erratum added to the source, not just state their conclusions. I verified each of these conclusions above; none is a gap.
- **C:34.** Add the x = 1 exclusion (source l.44).
- **C:37.** Add the lifted-pair derivation of 18m−1−2B (erratum E-B2).
- **C:40.** Add the B = 4m residue table for 4m ≤ S ≤ 2p+2 (erratum E-B1).
- **C:44.** Spell out "pair constraints" as derived above.
- **C:31 and C:45.** State that every term of Q, including y, is identified with its representative in [1,B].

## P2 (C:51–54): ACCEPT-WITH-FIXES

- **(F\*) gives P1's hypothesis.** At d = 2, (F\*) reads: ρ ≤ h implies |W| + 2ρ ≤ 1.
  - A nonempty W with ρ ∈ [1,h] has weight at least 3.
  - A nonempty W with ρ = 0 has |W| ≥ 2, because every μ ∈ [1, p−1].
  - So U satisfies P1's hypothesis with n = |U| = 2m+4.
- **d = 2 is a real case.** For m ≥ 3 we have 2 ≤ 2m−3. Also Z0 = ∅ automatically, since |Z0| ≤ 1.
- **Contradiction.** Accepted L1 (V:10, the same threshold CF setting with respect to g0) gives W\* ≤ U with σ ≡ −1 and |W\*| ≥ 4. P1 forbids this.
- **The n ≥ 2m+3 form is genuinely needed.** B2-1 and Sublemma(a) at exactly 2m+3 would not apply to |U| = 2m+4. The in-file P1 carries this step.

**P2-1 MINOR (C:51, 53–54).**
- **Problem.** "impossible at EVERY BASE2 cell, conditional on candidate L1" is too broad and has stale status.
- **Minimal fix.** Restrict it the way erratum E-B3 restricted B2-1: "For a threshold LS counterexample at a BASE2 cell (p = 6m−1 prime, m ≥ 3, κ = 4m, |Y| = 14m, (ZP_4m), a zero-sum of length ≥ 2p+2), with CF data w.r.t. g0: δ0 ≠ 2." Cite V:10 in place of "candidate L1".
- **Scope note.** This is not LS(p,4m).

## P3 (C:56–75): ACCEPT-WITH-FIXES

**Empty Z0.** Then δ' = d = 1. Accepted B2-1 (V:10) excludes this at exactly this scope. P1 plus L1 at n = 2m+3 also works.

**Nonempty Z0**
- **Range.** k = d−1 ≥ 2, since no single term is zero mod p. Hence 3 ≤ d ≤ 2m−3, and m = 3 forces d = 3.
- **U'.** |U'| = 2m+3, and (F') at δ' = 1 forbids every nonempty residue in [0,h]. So |A'| ≥ 2m+4 and A' ⊆ {0} ∪ T, where |T| = 4m.
- **Complement step.**
  - For each occurrence z, Z0 − {z} has size d−2 ≥ 1 and residue −ζ.
  - It is occurrence-disjoint from every W' ≤ U' = U − Z0.
  - If the union had ρ ∈ [1,h], its weight would be at least (d−2) + 2 = d > d−1, contradicting (F\*).
  - Every a ∈ A' is realised by some W' (with W' = ∅ for a = 0). Hence A' ∩ (ζ + [1,h]) = ∅.
- **The three regions partition [1, p−1]** (since h < p−h).
  - **(a) ζ ∈ [4m+1, 6m−2].** Then ζ+1 ≤ p ≤ ζ+h, so 0 ∈ ζ+[1,h], but 0 ∈ A'. Endpoints: ζ = p−h gives ζ+h = p, and ζ = p−1 gives ζ+1 = p. ✓
  - **(b) ζ ∈ [2m−1, 4m].** Then [ζ+1, ζ+h] ⊆ [h+2, p−1] ⊆ T, so |A'| ≤ 1 + 4m − (2m−2) = 2m+3, a contradiction. Endpoints: ζ = h+1 gives [h+2, 2h+1], and ζ = 4m gives [p−h, p−1]. ✓
  - **(c) ζ ≤ h.** The singleton case of (F\*) gives ζ ≤ ⌊(d−2)/2⌋.
- **(c) at d = 3.** The bound allows no ζ at all, while k = 2 occurrences must exist. Contradiction.
- **(c) at d ≥ 4: first crossing.**
  - w₁ = 1 + 2ζ₁ ≤ d−1, and w_k ≥ 3(d−1) ≥ d. So the first crossing index j satisfies j ≥ 2.
  - 2S_{j−1} ≤ d−j and 2ζ_j ≤ d−2, so 2S_j ≤ 2d−j−2 ≤ 2d−4.
  - Hence 1 ≤ S_j ≤ d−2 ≤ 2m−5 < h < p. The ρ of that prefix is exactly S_j, with no wrap, yet w_j ≥ d. This contradicts (F\*).
  - If j = k, then S_k ∈ [1, d−2] also contradicts S_k ≡ 0. The argument is consistent either way.
- **Spot checks.**
  - d = 4: ζ = 1 is forced, j = 2, S₂ = 2, w₂ = 6.
  - d = 2m−3: ζ ≤ m−3 and S_j ≤ h−3.
- **Dependencies.** This branch uses only (F\*), (F'), cardinality and occurrence complements. It does not use L1, the p23 table, or any bound d ≤ 5.
- **Choice of Z0.** Maximality of Z0 is never used, because (F') at δ' = 1 already makes U' zero-sum-free. So the conclusion holds for every inclusion-maximal choice of Z0.

**P3-1 MINOR (C:56–57, 74–75).**
- **Problem.** "impossible at every BASE2 threshold" is too broad. The choice of Z0 is not quantified. "(candidate B2-1)" is stale.
- **Minimal fix.** Use the same restriction as P2-1. State "for every inclusion-maximal Z0". Cite accepted B2-1 (V:10) for the empty branch.

**P3-2 MINOR, optional.**
- **C:59.** Only two facts from P1's first paragraph are needed: |A'| ≥ 2m+4, and A' ∩ [1,h] = ∅, which follows directly from (F'). The σ'-localisation and the symmetry A' = σ' − A' are unused. The package's §4 phrase "complement symmetry" should read "occurrence complement Z0 − {z}".
- **C:69.** Name the empty-range case explicitly: it is exactly d = 3.

## Shared findings

**S-1 MINOR (C:3–6, 18, 51, 54, 57, 75, 78).**
- **Problem.** The status labels predate verdict 9df92bda.
- **Fix.** Record the following in the candidate's own overlay, not only in the package:
  - L1 and B2-1 are accepted only for threshold counterexamples with CF data w.r.t. g0. That is exactly where P2 and the empty-Z0 branch of P3 use them.
  - P1 is proved in-file.
  - "Conditional on L1/P1" at C:78 should become "relative to accepted L1/B2-1 at threshold scope and in-file P1".
- **Effect.** No logical change.

**S-2 MINOR (C:11).**
- **Problem.** The bound d ≥ 1 is attributed to RED, DGM-p, the dichotomy and LS-II'. It actually comes from CF(a), via M ≤ 2p−1, as erratum E-G1 records.
- **Effect.** Not load-bearing: P2 fixes d = 2, and P3 either derives d ≥ 3 or uses B2-1.

## Imports at literal scope

| Import | Authority | Scope check | Used in |
|---|---|---|---|
| CF(a) | ca6e4ca7 item 1, read with E1 | Integer 0 ≤ κ = 4m ≤ p−1 ✓ | (F\*), (F'), d ≥ 1 |
| DGM-p | ca6e4ca7 item 5 | 3m−2 ≤ 4m ≤ p−1 ✓ | g0 is a generator |
| Threshold dichotomy | ca6e4ca7 item 6, read with R13 | κ0+1 = 4m ≤ p−2; length 14m; g = g0 ✓ | Cases (I)/(II) |
| LS-II' | ac8ead13 item 1, D-1 wording | p ≥ 7, same κ range ✓ | Case (I): d ≤ 2m−3 |
| RED | 23d1a488 item 4, read with E-2 | 0 ≤ κ ≤ p−2 ✓ | Framing only |
| L1 | V:10 | Threshold counterexample, CF w.r.t. g0 ✓ | P2; P3 empty branch |
| B2-1 | V:10 | Same ✓ | P3 empty branch |
| SLZ3 | 2b7b08a3 | Only inside accepted L1 | — |

**Not used in P1–P3:**
- Sublemma(a), which is superseded in-file.
- CF(b) and R4.
- index-one, AP', greedy and I-small.
- LS+, STAB and the three-occurrence transversal.
- Lev few-sums.

## Residual check (C:77–85; package §2)

The residual follows from five facts:
- B2-1: d ≠ 1.
- P2: d ≠ 2.
- Case (I): d ≤ 2m−3.
- P3: δ' ≠ 1 for every inclusion-maximal Z0.
- |Z0| ≠ 1, since every term is nonzero.

So every threshold counterexample at a BASE2 cell, with CF data w.r.t. g0, satisfies 3 ≤ d ≤ 2m−3. In addition, for every inclusion-maximal Z0, one of these holds:
- **(i)** Z0 = ∅ and δ' = d ∈ [3, 2m−3]; or
- **(ii)** 2 ≤ |Z0| ≤ d−2 and δ' ∈ [2, d−2], which forces d ≥ 4.

This is confirmed as a **necessary condition only**. It is neither an existence result nor an emptiness result. It is not LS(p,4m), S3, LS+, STAB, INV\* or ordered Olson. C:82–85 asserts no theorem, and P1–P3 do not depend on it.

**R-1 MINOR (C:78–80; package §2).**
- **Problem.** The stated residual "2 ≤ δ' ≤ d, |Z0| ∈ {0} ∪ [2,∞)" is correct but looser than what P1–P3 give.
- **Fix.** Tighten it to (i)/(ii) above and state the quantifier over Z0.

**R-2 MINOR (C:80–81; package §2, "In particular at p=29").**
- **What is correct.** The arithmetic holds: 2m+3+δ' ≥ 3m+1 exactly when δ' ≥ m−2.
- **Problem.** No accepted interface turns δ' ≥ m−2 into an exclusion at general m. V:22 records index-one only at p = 17 and p = 23, with explicit lengths. So the open region is the whole residual, not just δ' < m−2.
- **Fix.** Label the remark as orientation only.

## Supported scope

- **P1** (unconditional, elementary). Let p = 6m−1, m ≥ 3, h = 2m−2. Take any sequence of nonzero residues mod p of length at least 2m+3 whose nonempty occurrence sums all avoid [0,h]. Then it has no occurrence sub-multiset of size at least 3 summing to −1.
- **P2.** Take a threshold LS counterexample at a BASE2 cell, with CF data w.r.t. g0. Then δ0 ≠ 2. This holds relative to CF(a), DGM-p, the dichotomy, LS-II', accepted L1 at that scope, and in-file P1.
- **P3.** In the same setting, δ' ≠ 1 for every inclusion-maximal Z0. The nonempty branch is independent of L1. The empty branch is accepted B2-1.

## Remaining targets

- **The open residual.** Configurations (i)/(ii) for m ≥ 5, i.e. p ∈ {29, 41, 47, 53, 59, 71, …}. The smallest case is p = 29 with d ∈ [3, 7].
- **m = 3 and m = 4 are already closed**, but not by P1–P3. The separately accepted LS(17,12) and LS(23,16) (V:8–9) exclude every threshold counterexample there.
- **δ' = 2 occurs only in branch (ii).** It requires |Z0| = d−2 ≥ 2 and d ≥ 4. So the C:82–85 lever only needs to handle the nonempty-Z0 setting. It remains a planning sketch, as does any general-m index-one step.
- **Still open:** full S3, LS+, STAB, INV\* and ordered Olson.
