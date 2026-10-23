# ROT-PP1: independent second-family mathematical review (historical packet, errata v1 → v2 → v3)

**Basis**

- **Texts reviewed.** `proof-ROT-PP1-v2.md` (`99143ea5…`, L1–211) and `obstruction-ROT-PP1-v2.md` (`4839cbd3…`, L1–106). I read them together with the scope and its addendum, then overlaid parent errata v1 (`7f192a89…`), v2 (`49c3e491…`) and v3 (`6a666fcc…`) in that order.
- **No tools were used**, as instructed. Pins and line numbers are taken as supplied and were not recomputed.
- **"Erratum v2 LF94"** is identified by its content: the *Supplementary CT estimate* paragraph.
- **Earlier reviews are not evidence here.** The Codex disposition quoted in erratum v2 and the first reviewer's suggestion were not relied on.
- **Overlay mechanics check out.**
  - Every Old span in v1 and v2 occurs exactly once:
    - proof L109;
    - obstruction L80, L83, L86–87, L88, L95–98 and L99–101.
  - The v1 and v2 spans do not overlap.
  - v3 changes how the text is read, not the text itself.
  - Proof L34 and L209 point to the never-sent obstruction v1; erratum v1 redirects them to the delivered v2.

## 1. Verdicts

| Item | Verdict | Findings |
|---|---|---|
| (SR) selection rule, proof L57–66 | ACCEPT | none |
| Proposition VAC | ACCEPT | none |
| Lemma M | ACCEPT | none |
| Lemma P (with v2 m1) | ACCEPT | none |
| Lemma U | ACCEPT | none |
| Theorem ROT-PP1-TOP | ACCEPT | n1–n3, editorial and optional |
| Supplementary CT estimate (erratum v2, LF94) | ACCEPT | n7, presentation only |
| Obstruction §2 (NS facts) | ACCEPT | none |
| Obstruction §§3–4 with v1/v2/v3 applied | ACCEPT-WITH-FIXES | n4–n6 and n8, wording and navigation only |
| Errata v1, v2, v3 as overlays | ACCEPT | none |

There are no FATAL and no MAJOR findings. No finding changes any statement, step or inequality.

## 2. Mathematical audit

**Sign convention, re-derived from the group law.**
- With entering sign z_i, block S_i contributes z_i·y_i·f_i.
- Summing over blocks gives Σ y_i(z_i−z_{i+1})/2 = −½Σz_iθ_i = −T(z).
- So the selection is the identity exactly when the signed rotation sum equals T(z). This matches GRX.

**(SR).**
- All blocks are odd, so l_i ≢ f_i (mod 2) exactly when f_i = 0. Hence the GRX-δ equals k−2m and C_max = 2Ĥ+2m.
- Using 2p−2Ĥ = 2κ̂+2, the admissible n are the even n with max(0, 2κ̂+2−2m) ≤ n ≤ min(2p−2m, R).
- T(z_P) = Σ_{i∈P} τ_i follows from Σθ_i = 0.
- τ_i ≠ 0 for empty runs is exactly the NF rule (few-E L38).
- Φ(z_P) = 2m(P) for every non-constant P.

**VAC.**
- Pigeonhole on k ≥ p+1 > p block values gives y_j = y_{j'}.
- The arc R_{j+1..j'} is nonempty, proper and a single interval, so m = 1 and T = y_{j'} − y_j = 0.
- At κ̂ = 0, n = 0 is admissible, with C = 2p = C_max.
- The adjacent case j' = j+1 also works: no rotation letter is selected, so NF emptiness is irrelevant.

**Lemma M.**
- The capped total is at least 2q in both cases:
  - if μ ≤ q, it is N;
  - if μ > q, it is q from the top value plus min(q, N−μ) = q from the rest.
- In the consecutive listing, pairing i ↔ i+q with equal values would fill q+1 slots, exceeding the cap.

**Lemma P.** n = max(p−1, 2κ+2−2m) is even and satisfies:
- n ≤ 2κ, because p−1 ≤ 2κ and m ≥ 1;
- n ≤ 2p−2m, because Φ ≤ p+1 gives m ≤ (p+1)/2, and κ ≤ p−1;
- n ≤ R.

The rest of the argument:
- R ≥ 2p−2 holds exactly when κ ≥ (p−1)/2.
- The negation gives R−μ ≥ p−1 = q and 2q ≤ R, so Lemma M applies.
- |F0| = 2κ−p+1 ≥ n−(p−1) ≥ 0.
- Each Q_I consists of actual distinct letters and has |Q_I| = n.
- Iterating Cauchy–Davenport with t = p−1 nonzero d_i covers all of Z_p.
- C = 2p−n is even and lies in [Φ, C_max].
- Check at p = 7, κ = 5: R = 16, n = 10/8/6/6 for m = 1/2/3/4, |F0| = 4.

**Lemma U.**
- Uniqueness: 2(2κ+1) > R holds exactly when 2κ > p−3.
- Classes {x, −x} are disjoint and each dominant class holds at least 2κ+1 letters, so all non-constant z share one class.
- a ≠ 0: take the pigeonhole arc (m = 1, T = 0) with n = 2κ, which satisfies 2κ ≤ 2p−2 and 2κ ≤ R. Then 2κ zero-valued letters sum to 0 under any signs.

**Theorem ROT-PP1-TOP.**
- **Setup.** Ĥ = 1, F = p+3, R = 3p−5. The admissible n are {2p−2, 2p} for m = 0, {2p−4, 2p−2} for m = 1 and {2p−6, 2p−4} for m = 2.
- **Steps 1–2.** Lengths 2p−2 and 2p both lie in the ZP window, which gives A' ≤ p−2 and A ≤ 2p−1.
- **Step 3.** CT with κ = p−2 and n = p−3 (so |Y|−n = 2p−2) gives a capped sum ≤ 2p−5.
  - A ≥ p−1, so a contributes p−3.
  - Every other value has multiplicity ≤ p−2.
  - Two values at p−2 would contribute 2(p−3) > p−2.
  - Hence b ≤ p−1, and b ∈ {p−4, …, p−1}.
- **Step 4.** φ_a(z_P) = A−e(P) and φ_{−a}(z_P) = A'+e(P); deviant letters have signed values outside {±a}.
  - λ = p−2−b ∈ {−1, 0, 1, 2}, and Λ−λ = p−1+δ.
  - (W) is invoked only for non-constant P: singletons, prefixes P_t with 1 ≤ t ≤ k−1, and nonempty sets avoiding h.
- **Step 5.** A−A'−λ = Λ holds as an identity, so e(P_{k−1}) ≥ Λ.
  - The first passage gives e({t}) ≥ p−1+δ > 2 ≥ λ, a contradiction.
  - This step does not use δ.
  - α({h}) ≥ Λ ≥ p−1, so h is nonempty.
- **Step 6.** A ≥ 2Λ is equivalent to b ≥ p−1+2δ. This contradicts Step 3 only when δ ≥ 1, and the proof invokes it only under δ ≥ 1.
- **Step 7.** λ = −1, so every singleton {i} with i ≠ h (empty or not) needs e({i}) ≤ −1. Then A' ≥ p > p−2, a contradiction.
- **Step 8.** |P+| ≤ e(P+) ≤ λ, so there are at most b+λ = p−2 nonempty runs other than h. This leaves at least 2 empty runs among p+1.
- **Step 9 (setup).**
  - Every n-selection has the form na + Σ_J ω, where J is its part in B.
  - |J| ≤ n holds automatically, since b ≤ p−1 ≤ 2p−6 ≤ n.
  - The filler constraint is n−|J| ≤ A.
  - Cauchy–Davenport gives |M| ≤ p−1−b and 0 ∉ M.
  - The all-plus pattern, z_{i} and z_{i,i'} for empty runs have an empty negative side.
- **Step 9, b = p−2 (A = 2p−3).**
  - n = 2p−4 gives M = {τ_i+4a}.
  - n = 2p−2 needs |J| ≥ 1, so τ_i+2a ∈ Σ(B)∖Σ_{≥1}(B) ⊆ {0}. Hence τ_i = −2a for every empty run.
  - For a pair of empty runs, T = −4a. n = 2p−4 is admissible for m = 1 and m = 2, and 2p−4 ≤ A copies of a reach T, a contradiction.
- **Step 9, b = p−3.**
  - 2a, τ_i+2a and τ_i+4a are pairwise distinct unless τ_i = −2a, and that case puts 0 in M.
  - This case needs only one empty run.
- **Step 9, b = p−4.**
  - M = {2a, τ_i+2a, τ_i+4a}.
  - The crossed matching would give 4a = 0, so τ_i = τ_{i'}.
  - Adjacent pair: x = 1, and 4 ∉ {1, 2, 3}.
  - Non-adjacent pair: x = −½, and 2 ∉ {1, ½, 3/2}.
  - Every n used is at most A.
- **Conclusion.** δ = 0 and A ∈ [2p−3, 2p−1]. This transfers to w through NF's invariant rotation multiset, under the existential normal-form reading.
- **Endpoints checked.**
  - p = 7: b ∈ {3, …, 6}; for a non-adjacent pair, x = 3 and M/(2a) = {1, 4, 5} ∌ 2.
  - b = p−1 is Step 7; A = 2p−1 is the b = p−4 case; δ = 1 gives b ≥ p+1 in Step 6.
  - τ_i = −2a is handled in each case, and both adjacent and non-adjacent pairs are handled.
- **§6 remark.**
  - E2's largest class has 2p−4 < 2p−3 letters, because 3c ∉ {±c}.
  - E3 has a = 3c, A = 2p−1, A' = 0 and b = δ = p−4, so Steps 6–9 exclude it.

**Supplementary CT estimate (erratum v2, LF94), checked independently.** Range: k = p+1, (p−1)/2 ≤ κ̂ ≤ p−2.
1. CT applies: n = p−3 lies in [1, R], and R−n = 2κ̂+2 is even and in [2κ̂+2, 2p]. So the capped sum is ≤ 2p−5.
2. Lemma U gives δ ≤ R−(2κ̂+1) = p−2.
3. Suppose A ≤ p−3, with A ≥ A'.
   - The values a and −a are uncapped.
   - The deviant capped sum is ≥ min(p−3, δ) ≥ δ−1, because Σmin ≥ min Σ and δ ≤ p−2.
   - The total is then ≥ R−1 ≥ 2p−3 > 2p−5, a contradiction. So a contributes p−3.
4. Two sub-multisets are forbidden zero-sums:
   - a^{2p} has length 2p;
   - a^{p−1}(−a)^{p−1} has length 2p−2 ≥ 2κ̂+2, using κ̂ ≤ p−2.
   - So A ≤ 2p−1 and A' ≤ p−2, and every deviant multiplicity is ≤ δ ≤ p−2.
5. The tail is verbatim proof L135–137: two values at p−2 would exceed p−2, so b ≤ p−1.

The paragraph is a complete proof apart from one back-reference that applies unchanged. Its conclusion, b ≤ p−1 throughout the P/U range (so b ∈ [p−2e, p−1]), is correct. As stated, it proves no rigidity for lower κ̂.

**Obstruction §2.**
- **Reduction (L27–28).** Under ZP, (S1) fails exactly when there is a long zero-sum.
- **§2.1 — S1-sharp.** It carries no length hypothesis.
- **§2.1 — LS+ band.** |Y| = 3κ+e−1 > 3κ+1 exactly when e ≥ 3.
- **§2.1 — BASE1+.** Restricted to p ≥ 13:
  - e = (p−1)/3 ≥ 4;
  - (7p−1)/3 > 2p+2 exactly when p > 7;
  - these cells lie outside the LS+ band.
- **§2.2, hand-checked occurrence counts.**
  - A length-2p zero-sum h^i(3h)^j needs p | j.
  - A length-(2p−2) zero-sum needs j ≡ 1 (mod p).
  - Every resulting case exceeds an available multiplicity for E2 and E3.
  - The long sums have coefficient sums 4p and 6p.
  - At κ = p−1 only length 2p is forbidden, and j ∈ {0, p} is excluded.
  - g^{p+6}(3g)^{p−2} has coefficient sum 4p and length 2p+4.
- **§2.2 at p = 7.** Included and valid. All three displayed long zero-sums are the whole sequence, since p+3 = 2p−4, 3 = p−4 and p+6 = 2p−1. E2 and E3 coincide with BASE1+'s two forms, with g = 3h because 5·3h = h.
- **§2.3.**
  - U(p) is exactly the complement of the §2.1 cells within [⌊2p/3⌋+1, p−3]. It matches LSplus-chain L24, since p − ⌊(p−1)/3⌋ = ⌊2p/3⌋+1 for p ≢ 0 (mod 3).
  - The examples (11,8), (13,10), (17,12) and (17,13) are correct; (13,9) is a BASE1+ cell and (17,14) is in the LS+ band.
  - The ONE-SHORT-LS observation is literally correct: its theorem is stated at the exact length p+2κ.
  - The implication runs LS+ ⇒ NS only, as stated.
  - "Undecided" means undecided by the cited interfaces; it is neither a counterexample nor a claim of global openness.

**Obstruction §§3–4, with the errata applied.**
- **(O1)–(O3).**
  - L = p−1+2(κ̂−t), and the complement of a longest zero-sum is zero-sum-free.
  - The quoted hypotheses of FB (S′), SHgen (nonempty runs), SHgen-E (REFL for o_F ≤ k) and REFL-fewodd (o_F ≤ p) match the excerpts.
- **(P1) arithmetic.**
  - λ = p−2−b does not depend on κ̂; Λ = 2κ̂+1−A'; Λ−λ = p−2e+3+δ.
  - The Step 5 condition is b+δ > 2e−5.
  - The Step 6 condition is b < p−2e+3+2δ.
  - v2 m3 is correct: δ ≥ e−1 suffices uniformly and is exactly the requirement at b = p−1.
  - v2 m4's selectability qualifier b ≤ n ≤ A and the forced elements 2a{1..e−1} and τ_i+2a{1..e} are correct.
- **Steps 7–8 need no listing.**
  - They depend only on Steps 5–6, b ≤ p−1 and A' ≤ p−2.
  - b+λ = p−2 holds for every κ̂, and the supplement now supplies b ≤ p−1 and A' ≤ p−2.
  - So the list is not missing a failure point. This is an accuracy check, not a new result.
- **v1 (F1) overlay is correct.**
  - At most p−2 off-dominant letters give a Cauchy–Davenport lower bound of at most p−1, so full coverage is not guaranteed.
  - The old text's "at most p−1 residues" was an unjustified upper bound.
- **v2 m5 (F2) is correct.**
  - The move (R+2, F−2) preserves length and raises κ̂ by one.
  - FLEXa is not used.
- **(F3) is correct.**
  - τ₁ = 0 and every other τ_i = 1.
  - A zero τ-sum requires |P ∩ {2..p+1}| ∈ {0, p}, which forces P = {1} or P = {2..p+1}; both are single intervals.
  - At κ̂ = 1, patterns with m ≥ 2 admit n = 0.
- **Nothing in §§3–4 is overclaimed.** After the overlays, no statement asserts that a cell is false, that an avoider exists, that an input is necessary or minimal, or that a method is impossible.

## 3. Findings

FATAL: none. MAJOR: none.

| # | Location | Issue | Minimal fix |
|---|---|---|---|
| n1 | proof L45/L57 vs L129 | The symbol δ denotes both the GRX parity defect and the deviant count. | At L129, add "(not the GRX δ of Sec. 1)". |
| n2 | proof L205 | The residue facts invoked in Step 9 need only p ∤ 6, so the remark overstates where p ≥ 7 enters. This is not a p = 5 claim. | "p ≥ 7 is assumed throughout (lane range)." |
| n3 | proof L203 | "Lemma U fails" reads as if the lemma were false. | "The conclusion of Lemma U fails for E2." |
| n4 | obstruction L79–80 after v2 m2 | The CT bullet sits under the heading "steps that do not carry over", although it now says the estimate does carry over. "Below" points outside the note. | Re-head the list, and cite "erratum v2, Supplementary CT estimate". |
| n5 | obstruction L84 | "b can be as small as p−2e" reads as a claim of attainability. | "The available bounds (A ≤ 2p−1) give only b ≥ p−2e." |
| n6 | obstruction L76 | "(P0) … gives nothing" | "Lemma P as written does not apply." |
| n7 | erratum v2 supplement | The phrases "capping the deviant total" and "remaining argument" are compressed. | State Σmin(p−3, v_x) ≥ min(p−3, δ) ≥ δ−1, and cite proof L135–137. |
| n8 | obstruction L61–62, L66–67 | How ROT-KP+ consumes S(p), and the domain of FB-E, cannot be checked from the supplied excerpts. | None needed (navigation only, not premises); optionally pin the FB-E line range. |

## 4. Import-domain audit (separate from logic)

| Interface | Accepted domain | Use | Hypotheses met |
|---|---|---|---|
| NF | Every avoider of length 4p−2, p ≥ 5; existential reading (ZX overlay 2); PM* in the original-to-reduced direction only. | ŵ with p ≥ 7, odd blocks, empty-run rule. | Yes |
| GRX | Every word over D_{2p}; any cyclic constant-block representation, empty runs allowed; every z. | The all-plus pattern (ZP, κ̂ ≥ 0) and z_P for arbitrary non-constant P. | Yes |
| CT | p ≥ 5, 0 ≤ κ ≤ p−1, odd ZP sequence, R−n even in [2κ+2, 2p]. | TOP Step 3 (κ = p−2) and the supplement (κ̂ ∈ [(p−1)/2, p−2]), both with n = p−3. | Yes |
| Cauchy–Davenport | Z_p, classical. | Swap sums in Lemma P; subset sums Σ(B) in Step 9. | Yes |

- **Context-only citations in the obstruction note.** These are S1-sharp, LS+ chain, BASE1+, LS+2 (E2/E3), FB (S′), SHgen, SHgen-E, REFL-fewodd and KPS-SLZ. Their quoted hypotheses match the excerpts, and E2/E3 were also hand-checked independently.
- **ONE-SHORT-LS is cited only to note that it does not apply.** Its dependence on Lev therefore never enters.
- **Excluded inputs are not premises.**
  - None of Lev, (S1), index-one, S(p), REFL, SHgen/SHgen-E, ROT-SING(+), ROT-KP(+) or any pending candidate is a premise of VAC, M, P, U, TOP or the supplement.
  - The κ̂ = p−1 endpoint is never used, so there is no circularity.
- **Direction of avoidance.**
  - The proofs exhibit identity 2p-subwords only of ŵ, using GRX on ŵ's own representation.
  - They contradict ŵ's avoidance, which NF supplies through PM*'s original-to-reduced direction.
  - Nothing is transported back from ŵ to w except the invariant rotation multiset.

## 5. Dated route gaps vs the current terminal exclusion frontier

- **Accepted here as mathematics, independent of date:**
  - VAC (k ≥ p+1 forces κ̂ ≥ 1);
  - the P/U structure on (p−1)/2 ≤ κ̂ ≤ p−2;
  - TOP at κ̂ = p−2;
  - the NS facts in §2.1–2.2.
- **Dated route statements (2026-10-19, relative to this packet's cited interfaces).** These are accurate descriptions of where these routes stop, not statements of the current frontier:
  - the coverage rows "nothing new", "structure only" and "not treated";
  - §2.3 "undecided on U(p)";
  - (O1)–(O3), (P0)–(P1) and (F1)–(F3).
  - Per v3, every "smallest missing" input means a possible further input for this route, with no minimality or necessity asserted.
- **Not assessed.** I did not assess whether later accepted results (v3 names KP2 and BOTTOM; their texts are not in this packet) close any of these cells. I treat v3's sentence as parent-recorded context only.
- **No credit is booked.** This review books no new case count, no count credit, and no corroboration of any other result.

## 6. Trust boundary

- This is a written-proof-level review, relative to accepted NF, GRX and CT at their recorded scopes plus classical Cauchy–Davenport.
- The accepted imports were not replayed. In particular, CT's internal RS(a) step was taken at statement level.
- No computation, enumeration, code or tools were used. Hashes and line ranges are as supplied.
- **Not reviewed or approved:**
  - rigidity for 1 ≤ κ̂ ≤ p−3 or κ̂ = p−1 at k = p+1;
  - reflection rigidity;
  - INV*;
  - any o_F assembly;
  - ordered Olson for D_{2p} or for other groups;
  - p = 5;
  - Lean or human review;
  - novelty or priority.
