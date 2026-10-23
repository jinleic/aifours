DISPOSITION: ACCEPT-WITH-FIXES

This is a static audit of the inline packet only. Nothing was executed, no receipt was replayed, and hashes are taken from the packet. Line numbers are original LF lines, and paths are packet paths (relative to `olson/`). **T** means `inverse-run-count/mixdef-high/c6/proof-C0WB.md`.

## FATAL

none

## MAJOR

none

## MINOR — new target defects

**m1. `inverse-run-count/mixdef-high/c6/proof-C0WB.md:82-84` — SA\*\*/PA\*\* misquotes its base.**
- Corollaries SA and PA (`inverse-run-count/mixdef-high/c6/proof-SEEDG-r2.md:202-203, :221-222`) conclude per word: "if w satisfies (i) or (ii+)".
- The quoted condition "E ≤ 4, or 2kB ≤ p and E ≤ 2(k−kB−2B)−1" is Remark (3) at `proof-SEEDG-r2.md:179-180`. It is a sufficient condition for (i)/(ii+), not SA/PA's hypothesis, so the "replacement" has no literal target.
- The parenthetical at T:84, "The seeds there are quality seeds", drops SA/PA's alternative "or seeds from actual configurations with empty intersection".
- The mathematics that results is true. Corrected statement:

> **Corollary SA\*\*/PA\*\*.** Let w be an NMH word with R ≤ 2p−3 whose parameters satisfy the hypotheses of Corollary SA (resp. PA) of proof-SEEDG-r2.md, with region inequalities, b\* and m unchanged. Then every run of w has a quality seed, or seeds from actual configurations with empty intersection. Moreover, w has an identity 2p-subword if any of the following holds:
> - (i) or (ii+) of Lemma C0+;
> - B ≥ kB+1 and 3kB+1 ≤ p;
> - k ≥ kB+3B.
>
> In particular, this holds for every word of a class satisfying the region inequalities and one of: E ≤ 4; 2kB ≤ p and E ≤ 2(k−kB−2B)−1; B ≥ kB+1 and 3kB+1 ≤ p; k ≥ kB+3B.

**m2. `inverse-run-count/mixdef-high/c6/proof-C0WB.md:75-80` — SEED-G\*\* wording.**
- (a) F3 is unbracketed. Lemma C0B needs k ≥ kB+3B ∧ [2kB ≤ p ∨ seed inequality]. The other reading, (k ≥ kB+3B ∧ 2kB ≤ p) ∨ seed inequality, is not proved. The code (`seedXX.py:58-60`) implements the correct reading.
- (b) F3 quantifies a_t "for every run t" before the actual-empty-intersection alternative is discharged. "Seeds as in SEED-G\*" should also name (QS\*), (P2) and (PIN).
- (c) T:80 cites "Theorem SEED-G\*, resp. SEED-G" for (0.2). Those statements carry the count hypothesis; what is used is their proof, minus the final appeal to Lemma C0+.
- Corrected statement:

> Let w be an NMH word, R ≤ 2p−3, p ≥ 5 prime. For every run t, assume either that seeds of t from actual configurations (Lemma GS(a)) have empty intersection, or that t has a seed [a_t, b_t]. Assume these seeds satisfy (QS\*), (P2) and (PIN); quality seeds suffice by Lemma QQ. Assume (F1), or (F2), or (F3): k ≥ kB+3B **and** [2kB ≤ p, or min(kB−1, d_t−a_t) ≤ p−kB−1 for every run t]. Then w has an identity 2p-subword.
>
> *Proof.* An actual empty intersection excludes w. Otherwise, if w avoids, the proof of Theorem SEED-G\* (resp. SEED-G), stopped before Lemma C0+, gives (0.2) for the canonical lifts, and the seed property gives x_t ≥ a_t. Lemma C0+, C0W or C0B then gives a contradiction.

**m3. `inverse-run-count/mixdef-high/c6/proof-C0WB.md:86-88` vs `inverse-run-count/mixdef-high/c6/seedXX.py:39-42,52,60` — X\*\* hypothesis differs from what the code verifies.**
- As written, X\*\* requires the F3 seed inequality "for every allowed profile and every live weight d".
- The code checks only profiles that are not excluded by an empty guaranteed weight (`if gempty: continue` comes before `lives.append`). If every profile is excluded, the check passes vacuously.
- The code-checked condition is weaker and logically sufficient, because excluded profiles have no avoider. As stated, though, the [W+F] instantiations (the 15 F3\* classes) certify a different hypothesis.
- The notation "[a_d, b_d]" should also be σ_π(d).
- Corrected text: "… or k ≥ kB+3B together with [2kB ≤ p, or: for every allowed profile π none of whose guaranteed weights a\*, −b\* (if b\* ≥ 1), 0 (if n_pr ≥ 1) has empty σ_π, and every live weight d of π, min(kB−1, d−a_π(d)) ≤ p−kB−1, where σ_π(d) = [a_π(d), b_π(d)]]."
- The transfer argument itself is correct: an actual seed lies inside σ_π(d), so a_t ≥ a_π(d), and min(kB−1, d−a) is non-increasing in a.

**m4. `inverse-run-count/mixdef-high/c6/proof-C0WB.md:70-71` and `:119-121` — the Case-B remarks overclaim.**
The proof gives only a one-way obstruction.

- **(a) "exactly" at T:120-121 is false.** Take (p,k,κ,B) = (11,13,4,2).
  - Derived values: kB = 2, R = 17, E = 4, A = 15. The setting holds: k ≥ 2κ+3 = 11, R ≤ 19, A ≤ 21, and k ≠ p+1, so this is not the ZSI-B case.
  - Run counts: one anti run of length 2, three aligned runs of length 2, nine aligned singles. So n_an = 1, n_pr = 0, n_ev,al = 3, with A = 6+9 and E = 1+3.
  - k = 13 ≥ kB+3B = 8, and C+'s count holds via (i), since 3 ≤ 4.
  - Yet n_ev,al = 3 > B+n_an−2 = 1, so the inequality that "Case B forces" fails. Words for which that inequality excludes Case B therefore strictly contain the C+-violators.
  - Separately, Lemma C0B itself makes Case B impossible for every word once k ≥ kB+3B.
  - This is a relaxed run-count datum, not an RGR or group counterexample.
- **(b) The premise "for these words n_ev,al > 2(k−kB−2B)+n_pr−1" at T:120** holds only for violators of the second clause of (ii+).
  - Take (23,33,13,1): kB = 12, E = 6, with one pair and five aligned runs of length 2. This violates (i) and (ii+) because 2kB = 24 > 23.
  - But n_ev,al = 5 ≤ 38. Case B is still excluded here, since it needs 5 ≤ B+n_an−2 = −1.
- **(c) "n_ev,al = E cannot occur there" at T:70-71** does not follow from the bound. The bound n_ev,al ≤ B+n_an−2 excludes n_ev,al = E only when E ≥ B+n_an−1.
  - Take (11,13,4,3) with three anti singles and four aligned runs of length 2. Then n_ev,al = E = 4 = B+n_an−2.
- **Fix:** "Case B forces n_ev,al ≤ B+n_an−2, hence s0 ≥ 1 when k ≥ kB+3B. Every word violating (ii+) through its n_ev,al clause has n_ev,al ≥ 2B+n_pr > B+n_an−2. No converse is claimed."

**m5. `inverse-run-count/mixdef-high/c6/proof-C0WB.md:92-96, :106, :110, :112-121` — Sec. 4 status and range.**
- "Uniform (written) effect … SA\*\*/PA\*\* exclude EVERY word of every region class for p ≤ 61" is a census-instantiated claim and should be labelled [W+F].
- The code ranges start at 11 (`seedXX.py:68`, `seedX2.py:114`). So "p ≤ 61", "p ≤ 31" and "p ≤ 23" should read "11 ≤ p ≤ …".
- For p = 5, 7, E ≤ p−4 forces E ≤ 2, so C+'s class condition holds. This settles T:92-95 by hand. Nothing is computed for X\*\* at p = 5, 7, where r2's gaps (kB,B) = (2,2), (1,3) remain.
- Replay bookkeeping: MUT1 and MUT3 have 1,440 C0W constructions and 420 C0B vectors, against MUT0's 1,320 and 360. Say that mutation runs draw their own words.
- Both C0B replays (`replayW_mut0.txt:6`, `replayW2_mut0.txt:7`, `replayW2_mut1.txt:7`) have **zero Case-B instances**. Case B rests solely on the written proof, so T:119 must not read as validation.

**m6. `inverse-run-count/mixdef-high/c6/proof-C0WB.md:7-12` — provenance, path and imports.**
- (a) "wording fixes only in Sec. 2" (T:11) is inaccurate. The six Claude MINORs are at Rstar L13, L52, L109, L128, L163-165 and L172-191 (`review-notes/olson-rstar-claude-review-v1.note.md:7-35`); none falls in Sec. 2 (L56-72). Write instead: "Sec. 2 received no fix; Lemma KL/K, where MINOR-3 sits, is not used here."
- (b) `../../../inverse-parity/…` (T:10) resolves only from c6/, while T:12 says "Paths relative to mixdef-high/". Use `../../inverse-parity/mixdef-low/c2/proof-Rstar-partial-v2.md`, or restrict the convention to `c3/` and `c6/` paths as r2:28 does.
- (c) The import list at T:7-9 omits `c6/proof-SEEDG-cls.md` (Corollary X, Lemmas PR, CF′), which X\*\* uses at T:86. It also does not record that SEEDGstar and cls are frozen with Codex ACCEPT-WITH-FIXES and pending repairs.

## Imported pre-existing repairs (conditions, not new defects)

- **i1. `inverse-run-count/mixdef-high/c6/proof-SEEDGstar.md:42-43`.** "At least each" should be the minimum over the term sums. SEED-G\*\*'s (QS\*) branch and X\*\* inherit this. The conclusion survives, but the repair is a condition for those two.
- **i2. `inverse-run-count/mixdef-high/c6/proof-SEEDG-cls.md:35`.** "(k ≥ 12)" should be "cyclic distance min(4, k−4) ≥ 2, since k ≥ 7". X\*\* inherits this through CF′, so it is a condition for X\*\*.
- **i3. `inverse-run-count/mixdef-high/c6/seedXstar2.py:23-27`.** The floating-point `bounds()` is used at `seedXX.py:44`. It is exact within 11 ≤ p ≤ 31, and the X\*\* instantiations stay inside that range. Any extension needs doubled-integer bounds.
- **i4. `inverse-run-count/mixdef-high/c6/proof-SEEDGstar.md:82` (scope MAJOR).** Not inherited: T:106-107 correctly reports the seed-failing class.

None of i1–i4 touches SA\*\*/PA\*\*. Its route is r2 SA/PA → proof of SEED-G (SCW-G, SL, lifts) → DF/C0W/C0B, and it never passes through star or cls.

**Severity counts:**
- New target defects: FATAL 0, MAJOR 0, MINOR 6.
- Imported conditions: 3 MINOR-level (i1–i3), plus 1 import MAJOR that is not inherited (i4).

## Required checks

### 1. DF (T:27-29) — correct

- bh_t ≤ 1 gives x_t ≤ (d_t+1)/2 ≤ (d_t+B)/2 < ⌊(d_t+B)/2⌋+1. The last step is strict for every integer d and every B ≥ 1, including B = 1.
- x_t ≤ (E+2)/2 ≤ (p−2)/2 < p, using E ≤ p−4, which follows from (0.1) and k ≥ p+1.
- Since λ({t}) = min(p, d+1−kB, ⌊(d+B)/2⌋+1) ≤ x_t, the binding term must be the second one, so c_t ≤ kB−1.
- No sign of d is used. With kB = 1 this gives c_t ≤ 0.
- DF covers defects too: every defect has c_t ≤ kB−1. This is stronger than c3 (A-ii)'s max-bound, and it is exactly why (A\*) is automatic when 2kB ≤ p.

### 2. C0W (T:33-49) — correct

- **Step (1):** cheap runs have 1 ≤ w ≤ kB.
- **Step (2):** Σw = D−p+k = p+2kB. A non-cheap run with c ≥ 0 has bh ≥ 2, so d = bh+2c ≥ 2: it is aligned, and w ≤ d/2. Pairs and anti runs with c ≥ 0 have bh ≤ 0 and are cheap. The aligned d-sum is A−n_pr ≤ 2p−1, so W(cheap) ≥ 2kB+½, hence ≥ 2kB+1.
- **Step (3), some run non-cheap:** cheap runs form paths. The heavier parity class of each path has weight ≥ half. Distinct paths are separated, and path endpoints are adjacent only when k ≤ 3.
- **Step (3), all runs cheap:** deleting t₀ (w ≤ kB) leaves path weight ≥ p+kB. The path ends t₀±1 are non-adjacent since k ≥ 6, and the heavier class weighs ≥ (p+kB)/2 ≥ kB+1, using p ≥ kB+2, which follows from 3kB+1 ≤ p.
- **Step (4):** |S| ≤ kB+1; m(P) = |P|; Φ(P) = W(P) ∈ [kB+1, 2kB]; bh(P) ≤ #{bh=1} ≤ kB+1 ≤ B; X_P+m(P) = bh(P)+Φ(P) ≤ 3kB+1 ≤ p. Equality is allowed because (P) is non-strict.
- The reorder from S to P is redundant, since S already has these properties, but harmless.
- **Hypotheses used:** (0.2) enters only through singletons (via DF), Σx = p, and the final violated pattern. The c3 Kill lemma is an exact iff for λ with β = 0. Nothing from k ≤ p, interval-chain lifts, Fact F, or Lemma K (i)/(iv)–(vi) is used or needed: a single violated lower bound already contradicts (0.2). P is proper and nonempty.

### 3. C0B (T:53-69) — correct

**Case A.**
- Z is nonempty because Σ(1−bh) = 2kB. Z ≠ [k] by (0.1).
- At each step an end run with ≤ 1 neighbour exists. The change in Φ is −c or −c−1, which can be non-monotone.
- The predecessor has Φ > p, and each step drops Φ by at most p−kB by (A\*), so Φ(Q) ≥ kB+1. Hence Q is nonempty, and Q ⊆ Z makes it proper.
- (Fl) holds since bh ≤ 0. (P) holds since x_t ≤ c_t on defects.

**(A\*) sources.**
- If 2kB ≤ p, DF gives c ≤ kB−1 ≤ p−kB−1.
- Otherwise c ≤ min(kB−1, d−a_t).
- Under (QS): d−a ≤ (d+Δ₀)/2−1 ≤ (2p−k−1)/2 ≤ p−kB−1, using k ≥ 2kB+1 and real-valued steps against an integer bound.

**Case B.**
- (2.2) with m(Z) ≥ 1 and sur ≥ 0 gives n_ev/2 ≤ −f(Z)−1.
- f values: aligned f ≥ 0, pair f = −1, anti f = −⌈(b+1)/2⌉ = −(b+1+[b even])/2.
- Extending the sums to all runs is safe because every added term is positive.
- This yields n_ev,al ≤ B+n_an−2. With n_an ≤ B−n_pr it gives s0 ≥ k−kB−3B+1+n_pr ≥ 1. This bound is an integer, so (B1+)'s integrality step is not needed.
- (B1+)'s count (`proof-Cplus-r2.md:62-76`) uses no n_ev,al hypothesis before its final line.
- (B2+) (`proof-Cplus-r2.md:80-88`) uses (1.2), (2.1)–(2.3), (0.1), E/2 = p−k+κ, n_an(Z) ≤ B and n_ev,an(Z) ≤ B/2. It uses no count hypothesis.
- No hidden sign, parity or empty-set assumption appears. Case B needs neither (A\*) nor 2kB ≤ p.

### 4. SEED-G\*\* (T:75-81)

- F1/F2/F3 replace only C0+'s count. Seeds, certification, (QS\*)/(P2)/(PIN), lifts and the NMH hypotheses are untouched.
- Repairs needed: F3 bracketing and empty-case ordering (m2).
- No formal empty window is treated as an exclusion.

### 5. SA\*\*/PA\*\* (T:82-85)

- Region inequalities are unchanged.
- Quality seeds make the seed form of (A\*) automatic (T:56), so F3 reduces to the class condition k ≥ kB+3B.
- The six Claim E′ classes re-check by hand, each with lower bound = m (and m ≤ upper bound) in the required region:

  | Class (p; kB, B) | Region | m |
  |---|---|---|
  | (11; 4, 2) | SA | 4 |
  | (11; 5, 2) | PA | 4 |
  | (13; 6, 2) | PA | 4 (upper 5) |
  | (13; 7, 2) | PA | 5 |
  | (13; 5, 3) | SA | 5 |
  | (17; 7, 4) | SA | 7 |

- (11; 5, 3) lies outside both regions (SA bounds 5 > 3; PA has Δ₀ = 3 < 4).
- The p = 7 classes (2,2) and (1,3) remain gaps, and the target does not claim them. F2/F3 supply no seeds.
- F2/F3 matter only when E ≥ 6, which forces p ≥ 11.

### 6. X\*\* and [F]

- The implication and the seed transfer are correct, subject to the m3 quantifier fix. X\*\* is labelled [W+F] (T:5, T:86).
- **X table:** OPENE totals 24+47+137+210+438+1001+1257 = 3114. By column:
  - C+: 2736 = 1793+756+187.
  - F2: 343.
  - F3: 19.
  - F3\*: 15.
  - seed-fail: 1.
  - The columns sum to 3114. F2+F3+F3\* = 377, matching star.
- **README tally:** 344 = 343+1, and 76−57 = 19.
- **R part:** OPENE totals are 26,225 / 22 / 602, and IE totals are 21,308 / 0 / 5,062. There are no "none" keys. Region F2+F3 at p ≤ 43 is 103, and at p = 61 it is 7+183 = 190; these match T:95, although r2 Sec. 6 itself is not in the packet.
- **Ablations:** 56 = 1+7+13+35; 3 = 1+2; 1.
- **Remaining scope:** (31; 51, 24, 23), with R = 59 and E = 8, plus the OPEN0 seed failures (10 at p ≤ 31). There is no census extrapolation and no ordered-Olson claim.

## Correctness, novelty, significance

**Correctness.** DF, C0W, C0B, SEED-G\*\* and SA\*\*/PA\*\* are mathematically correct as written, and I found no proof gap. Every finding concerns statement precision, labelling, provenance, or remarks outside the proofs. X\*\*'s written implication is correct once m3 is applied, and its class instantiations remain computer-assisted.

**Novelty.** Within this ledger, the new content is threefold. First, DF. Second, the transfer of the Lemma W weight construction (attributed at T:9-12) to the high-run system (0.2), with Fact F replaced by DF and Lemma K by c3's Kill lemma. Third, the Case-B observation that (2.2) forces n_ev,al ≤ B+n_an−2, together with the seed form of (A\*). External novelty and priority were not checked.

**Significance.** C+'s n_ev,al count is no longer the obstruction for seeded words satisfying F2 or F3. Every SA/PA region class with 11 ≤ p ≤ 61 is finished ([W+F] enumeration over a written corollary). With exact seeds, 3,113 of 3,114 OPENE classes at 11 ≤ p ≤ 31 are finished ([W+F]). What remains: (31; 51, 24, 23); OPEN0 seed failures; the p = 7 gaps and (11; 5, 3) for written coverage; everything beyond the census ranges; and NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV\* and ordered Olson, none of which is claimed.

## PARENT-DELTA-FIT: YES-AFTER-FIXES

This applies to the whole written SA\*\*/PA\*\* claim. Necessary changes:
1. Replace T:82-85 with the m1 statement: per-word, keeping (i)/(ii+), with SA/PA's actual-empty alternative.
2. Repair T:75-80 as in m2: bracket F3, discharge actual-empty seeds first, name (QS\*)/(P2)/(PIN), and cite "proof of" SEED-G.
3. Record any "p ≤ 61" consequence as [W+F] over 11 ≤ p ≤ 61, with the E ≤ 2 remark if p = 5, 7 are included.
4. Record that the regions are unchanged and that p = 7 (2,2), (1,3) and (11; 5, 3) remain outside.

m3–m6 and i1–i3 are needed for X\*\* and file hygiene, not for SA\*\*/PA\*\*. This is advisory review only, not authorization to accept the parent claim.
