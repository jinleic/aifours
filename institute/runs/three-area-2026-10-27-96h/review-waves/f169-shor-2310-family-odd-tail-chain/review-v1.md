# Review v1 — wave `f169-shor-2310-family-odd-tail-chain`

Reviewer **ReviewF169ShorOddTail** (in-harness same-harness subagent). Native `/bin/date` observed immediately before writing this file: **2026-10-29T07:46:22-0700 PDT**.

**Nature of this review.** Same-harness written review with independently authored exact integer controls. It is **not** a human review, an independent-model-family review, a formal/kernel verification, or a novelty/SOTA assessment. Author "PASS"/kernel statements were not used as evidence; every finite claim relied on below was recomputed by the reviewer's own code. No solver was used; nothing below rests on a solver UNKNOWN or budget hit. No adoption or novelty claim is made. **Q55, every even-|Q| branch, other order families and the original unrestricted finite-completion problem remain OPEN.**

## 0. Binding and read order

Manifest `RUN/review-waves/f169-shor-2310-family-odd-tail-chain/manifest-v1.json`: SHA-256 `c93b4a887950735b1a5ea215da629f3a26191fbb6a29fc84f88800377fd3ff00` — verified (shell, 2026-10-29T13:54:13Z, and again inside the control run). The manifest names no errata, overlays or withdrawals. The four inputs were verified (SHA-256 / bytes / LF) **before** being read, then read completely in the declared order with exact `:raw` reads; all four match again inside the control run (check `S00`).

| # | input (shor-completion/) | role | SHA-256 | bytes | LF |
|---|---|---|---|---:|---:|
| P1 | `frontier-20261028-2310-family-odd-tail-joint-prime-obstruction-v1.md` | joint prime obstruction | `b61890594ce5233fd0050d5524a4318a29020aa0ed0d30bded1d37d976d0db80` | 11601 | 119 |
| P2 | `frontier-20261028-2310-family-odd-tail-three-residuals-v1.md` | three residuals | `fce25631427ffa6e6d128383ebe3afcd4c69abbd46e73a31bc372dbfe166c23b` | 11764 | 136 |
| P3 | `frontier-20261028-2310-family-q165-coupled-gcd-obstruction-v1.md` | Q165 obstruction | `33c641153358510430cd78e5568d7e565129eba71a07c7d88d5be9b8fa5e49b2` | 12257 | 138 |
| P4 | `frontier-20261028-165-family-odd-tail-only-55-v1.md` | 165-family only-55 | `fe70ca41666dc5d6e0675787a519fefd92f37dcda93bf1f52dab82edfe65c62b` | 6328 | 65 |

P2 cites P1's SHA and P3 cites P1's and P2's SHAs; the citations equal the manifest values (checked in `S00`). The inputs contain no certificate JSON; the finite certificates are inline pair lists in P1 §5 and a head list in P2 §6. They were parsed completely by the reviewer's code from the SHA-verified bytes and compared with an independent hand transcription (equal, `S4`/`S9`). Packet pseudocode (P2 §6, P3 §7) was read only; it was never executed.

## 1. Import transcription (primary sources read directly)

**Łaba–Londner, *Combinatorial and harmonic-analytic methods for integer tilings*, arXiv:2106.14042v3** (PDF fetched 2026-10-29T13:58:33Z: HTTP 200, 1,006,826 bytes, SHA-256 `4a7707e7dd3ca38379a536c7ae928e7915d1be0725e1e065389c9f4bb4234cf8`; the text was read through the harness PDF-to-text reader, using its page markers).

* **Theorem 1.1 (Coven–Meyerowitz), p. 3.** Let `S_A` be the set of prime powers `s` such that `Φ_s(X)` divides `A(X)`. (T1) `A(1) = ∏_{s∈S_A} Φ_s(1)`. (T2) If `s_1,…,s_k ∈ S_A` are powers of different primes, then `Φ_{s_1⋯s_k}(X)` divides `A(X)`. Tiles satisfy T1, and T2 holds if `|A|` has at most two distinct prime factors.
* **(1.3), p. 3.** `A ⊕ B = Z_M` is equivalent to `|A||B| = M` together with `Φ_s | A(X)B(X)` for every `s | M`, `s ≠ 1`.
* **§2.4, pp. 9–10.** For every prime power `s = p^α | M`, `Φ_s` divides exactly one of `A(X)`, `B(X)`. `Φ_{p_i} | A` means that A is uniformly distributed mod `p_i`. Also: "Let N | M. Then the condition Φ_s | A for all s | N, s ≠ 1, means that 1 + X + ⋯ + X^{N−1} divides A(X), or, equivalently, that the elements of A are uniformly distributed mod N."
* **Definition 2.4 / Theorem 2.5 (divisor exclusion; Sands), p. 10.** `Div_M(A) = {(a − a', M) : a, a' ∈ A}`. If `A, B ⊂ Z_M` are sets, then `A ⊕ B = Z_M` if and only if `|A||B| = M` and `Div(A) ∩ Div(B) = {M}`.
* **Corollary 6.2, p. 26** (page marker confirmed). "Let A ⊕ B = Z_M, where M = p_1^{n_1} p_2^{n_2} p_3^{n_3} ⋯ p_K^{n_K}. Assume that for each i ≥ 3, the prime factor p_i divides at most one of |A| and |B|. (This happens e.g., if n_i = 1 for i ∉ {1, 2}.) Then both A and B satisfy (T2)." The proof proceeds by induction on the number of prime factors. It uses Tijdeman's theorem and Theorem 6.1 (subgroup reduction, from [CM, Lemma 2.5]), with Theorem 1.1 as the two-prime base case. The introduction (p. 4) describes the same case as "at most two of p_1,…,p_K divide both |A| and |B|". The prime labelling is arbitrary, so the hypothesis is exactly "at most two primes divide both cardinalities". The published proof was **not** re-derived here; the corollary is an import.

**Cordero, *Factorizations of Cyclic Groups and Bayonet Codes*, arXiv:2301.13566v1** (HTTP 200, 331,796 bytes, SHA-256 `5ac712593068198e1bb13628df418c1802658a7c03fb9708124da05f3d82bd00`). **Theorem 1.1 (Restivo–Salemi–Sportelli), p. 3:** "If M is a finite maximal code such that b, aⁿ ∈ M then the ordered pair ({k : a^k b⁺ ∈ M}, {k : b⁺ a^k ∈ M}) is a factorization of size n." This theorem is the packets' bridge from code to tiling. That bridge lies **outside** the frozen anchored-tiling scope and was only transcribed. As a consistency observation, the literal Shor code contains `b, a³b, a⁸b, a¹¹b` and `b, ba, ba⁷, ba¹³, ba¹⁴`. Any finite maximal code containing it would therefore give `A = {0,3,8,11} ⊂ P` and `Y = {0,1,7,13,14} ⊂ Q`, as the packets state.

## 2. Invocation audit (Corollary 6.2 and its use)

**Reconstruction of the consequence actually used.** Let `P ⊕ Q = Z_n` with `gcd(|P|,|Q|) = 1`.

1. **Ownership.** For a prime power `s = p^α | n`, `Φ_s` divides `P(X)` or `Q(X)` by (1.3) and irreducibility. If `Φ_s | Q(X)`, then because `Φ_s` is monic, Gauss's lemma gives `Q(X) = Φ_s(X)R(X)` with `R ∈ Z[X]`, so `p | Q(1) = |Q|`. Hence every prime power dividing `|P|` lies in `S_P`.
2. **T2 step.** For every `d | |P|`, `d > 1`, T2 gives `Φ_d | P(X)`. The product of these distinct irreducibles is `(X^{|P|}−1)/(X−1)`. After folding modulo `X^{|P|}−1`, the result has degree `< |P|` and nonnegative coefficients summing to `|P|`, so it is the all-ones polynomial. Therefore **P is a transversal mod |P|**; this is the p. 10 statement with `N = |P|`. The same argument applies to Q, and to uniformity modulo any `pq` with both primes dividing `|P|`.
3. **Small exhaustive check.** Control `S11` enumerated every normalized tiling of `Z_12`, `Z_20` and `Z_30` with coprime factor sizes (48, 48, 440, 440, 16440, 20070 and 5100 tilings). In every one, both factors are transversals. In the negative control, `{0,1,4,5} ⊕ {0,2} = Z_8` has non-coprime sizes and its 4-set is not a transversal mod 4.

| packet / branch | n | \|P\| | \|Q\| | primes dividing both | Cor. 6.2 hypothesis | consequence used |
|---|---|---|---|---|---|---|
| P1 §3 (all odd q) | 2310·2^k, k≥0 | n/q (contains 2^{k+1}) | odd q \| 1155 | none | holds | P uniform mod 15/33/55 (needs `Φ_{pq}` from T2) |
| P1 §4 q=1155 | 2310·2^k | 2^{k+1} | 1155 | none | holds | Q transversal mod 1155 (T2 for Q) |
| P1 §5 q=33 / 15 | 2310·2^k | 70·2^k / 154·2^k | 33 / 15 | none | holds | P uniform mod 5 / mod 11 — needs **only** `Φ_5`/`Φ_11` from ownership, not T2 |
| P2 §3 q=385 | 2310·2^k | 6·2^k | 385 | none | holds | Q transversal mod 385 |
| P2 §4 q=231 | 2310·2^k | 10·2^k | 231 | none | holds | Q transversal mod 231 |
| P2 §5 q=105 | 2310·2^k | 22·2^k = 11·2^t | 105 | none | holds | P transversal mod 11·2^t; Q transversal mod 105 |
| P3 q=165 | 2310·2^k | 14·2^k = 7·2^t | 165 | none | holds | P transversal mod 7·2^t; Q transversal mod 165 |
| P4 (all odd q) | 165·2^t, t≥1 | 165·2^t/q | odd q \| 165 | none | holds | P uniform mod 33, 15, 11·2^t, 5·2^t; Q transversal mod 165 |

In both families `|Q|` is odd and the odd part of `n` is squarefree, so every prime divides exactly one cardinality. Hence `gcd(|P|,|Q|) = 1`, and Corollary 6.2 applies under any labelling. **Every invocation is within the hypotheses.** The tiling class in every case is a cyclic tiling `P ⊕ Q = Z_n` of sets, the class the corollary addresses. The packets' paraphrases agree with the transcribed statement; P1's "after ordering the prime divisors" refers to the corollary's arbitrary labelling and does no harm here, since no prime divides both sizes. Sands (Theorem 2.5) is used only in its tiling ⇒ divisor-exclusion direction. Anchor gcds (`S01`): `Div(A) = {3,5,11,gcd(8,n)}` and `Div(Y) = G_0 = {1,6,7,14}` (k=0) or `G_k = {1,6,7,12,14}` (k≥1), disjoint for k = 0..5.

## 3. Packet reconstructions and per-claim verdicts

Abstract checks use representatives `x ∈ [0, 2·oddpart)`, which fix parity and every odd-prime residue. Any constraint that bans only **odd** differences is then exact for all k at once: for odd `d`, `gcd(d, 2^t·oddpart) = gcd(d mod oddpart, oddpart)`. Concrete checks at several k corroborate. Even-difference reasoning is checked concretely, together with the written 2-adic arguments.

### P1 — joint-prime and matching obstructions → `|Q| ∈ {55,105,165,231,385}`

* **P1-1 (§2) coprimality, in-hypothesis Corollary 6.2, transversality: WRITTEN_SUPPORTED** (conditional on the import; §2 above).
* **P1-2 (§3) missing joint classes ⇒ at least two of 3,5,11 divide q ⇒ list (2): WRITTEN_SUPPORTED.**
  * I re-derived the three residue cases by hand, including the cited residue pairs `(0,8)/(3,0)` mod 11, `(0,3)/(3,1)` mod 5 and `(0,2)` mod 3.
  * `S1`: no head state in classes 4 mod 15, 1 mod 33 or 2 mod 55 survives the odd bans `{1,7}`. This holds abstractly for all k and concretely for k = 0..3.
  * NEG: dropping ban 7 leaves 4 surviving states in class 4 mod 15.
  * `S2`: the odd divisors ≥5 of 1155 reduce to `{15,33,55,105,165,231,385,1155}`.
* **P1-3 (§4) q = 1155 impossible for all k: WRITTEN_SUPPORTED.**
  * `S3`: the even state of class 2 mod 1155 hits `y=7` (gcd 5), and also `y=13` (gcd 11). The odd state hits `y=14` (gcd 3).
  * Concrete checks for k = 0..4 agree.
  * NEG: dropping ban 3 lets the odd state 1157 survive.
* **P1-4 (§5) q = 15 and q = 33 impossible for all k: WRITTEN_SUPPORTED.** All results below are from `S4`.
  * The `C_k` counts in classes 2,4 mod 5 and 1,6 mod 11 are 14, 30, 72, 144, 288 for k = 0..4.
  * No old head lies in a screened class.
  * All six certificates (2/6/34 pairs per q) match the parsed text exactly. Every pair is valid: correct classes, endpoints in `C_k` and distinct, and pair gcd in `G_k`.
  * The counting contradictions hold: 28−2<28, 60−6<56, 144−34<112.
  * My **maximum** cross matchings are 2, 6, 36, 72 (k = 0..3, both q). They give bounds 26<28, 54<56, 108<112, 216<224.
  * Lift: for k = 3, 4 the screened classes of `C_k` equal the 9240-periodic lift of those of `C_2`. All 68 and 136 lifted pairs are valid, and `110M < 112M`.
  * I re-derived the written lift argument: membership in `G_k` depends only on the residues mod 1155 and on `v_2 ≤ 2`. It holds for every k ≥ 2.
  * This branch needs only the prime cyclotomics `Φ_5`/`Φ_11`, not T2.
  * NEG: a corrupted pair `(2192,209)` is rejected because its gcd is not in `G_0`, and keeping only 32 of the 34 pairs gives no contradiction.
* **P1-5 conclusion (1): WRITTEN_SUPPORTED** at the anchored tiling scope.
* **P1-6 (§6) reported finite numbers: WRITTEN_SUPPORTED.** The counts 14…288 are reproduced. The reported matchings 2, 6, 36 equal my maxima (`S10`).
* **P1-7 (§1) code-level bridge via RSS/Cordero: INCONCLUSIVE — outside the frozen scope, not reviewed.** This is not a defect.

### P2 — three residuals: q = 385, 231, 105

* **P2-1 (§3) q=385: WRITTEN_SUPPORTED.**
  * `S5`: the domain table `{3:(odd,2), 24:(odd,2), 25:(even,0),(even,2)}` is reproduced exactly. No consistent `(x3,x24,x25)` exists, abstractly for all k and concretely for k = 0,1,2.
  * The cited gcds 11 and 3 are confirmed.
  * NEG: without ban 11 a consistent triple exists.
* **P2-2 (§4) q=231: WRITTEN_SUPPORTED.**
  * `S5`: the domain table is reproduced exactly, and no consistent quadruple exists (all k abstractly; k = 0,1,2 concretely).
  * The cited gcds 5, 5, 11, 11, 5 are confirmed.
  * NEG: without ban 5 a consistent quadruple exists.
* **P2-3 (§5.1) P uses gcd 2: WRITTEN_SUPPORTED.**
  * `S6.1`, t = 1..6: every screen survivor in class 1 mod 11·2^t has `(x mod 3, x mod 5) ∈ {(0,3),(2,0)}`.
  * The designated difference has gcd in `{2,14}`.
  * The 12 heads per t that avoid 1, 7 and 14 all use gcd 2.
  * The written 2-adic step (`x ≡ 1 mod 4` against `3 ≡ 11 ≡ 3 mod 4`) is correct.
  * At k = 0, P already uses gcd 2 through `8−0`.
* **P2-4 (§5.2) Q uses gcd 2: WRITTEN_SUPPORTED.**
  * `S6.2`: complete backtracking over the 11 residues, with conflicts computed by actual gcds rather than by the author's rule, finds **exactly one** consistent assignment, equal to the displayed singleton table.
  * The chain pairs `(0,71),(71,72),(72,14)` differ mod 3, 5, 7 and in their forced mod-11 values.
  * For t = 1..6, every admissible `(x71,x72)` gives three pure 2-power gcds, one of them equal to 2. The mod-4 argument is correct.
  * NEG: without ban 3 there are 773,828 assignments.
* **P2-5 statement (1) and conditional combination (2) `{55,165}`: WRITTEN_SUPPORTED** as conditional statements.
* **P2-6 (§6) non-load-bearing relaxations: WRITTEN_SUPPORTED** (see Note N2). Results from `S9`/`S6.2`:
  * The 56-head set contains A, hits 56 classes mod 56 and avoids gcds `{1,2,6,7,12,14}`.
  * The 165-tail CRT relaxation is distinct, contains Y and avoids `{3,5,8,11}`.
  * Full 105-residue arc consistency yields singletons everywhere and the same 11 singletons.

### P3 — Q165 coupled-gcd obstruction

* **P3-1 (§2) coprime sizes and transversals (2): WRITTEN_SUPPORTED.** Every mod-7 head class contains every 2-adic residue, by CRT.
* **P3-2 (§3) four domain tables: WRITTEN_SUPPORTED.** `S7` reproduces all four tables exactly.
* **P3-3 (§4) forced gcds 21/35/77 and "at least two of {105,231,385}": WRITTEN_SUPPORTED.**
  * `S7`: exhaustive search over `x2,x3,x10,x11,x12` forces `x3=x10=x11=O0`, with gcds `(21,35,77)` against old 0.
  * Each pair-avoidance case admits no assignment on the cited residues, abstractly and concretely at k = 0,1.
  * NEG: with only `{3,5,11}` banned, the same residues are satisfiable.
* **P3-4 (§5) exactly one h; h = 105 and h = 231 impossible: WRITTEN_SUPPORTED.**
  * `S7`: if P avoids all three, no odd head exists in class 0 mod 7.
  * The forced triples are `(0,0,8)/(2,1,3)` for h=105 and `(2,0,8)/(0,1,3)` for h=231.
  * No compatible `(u,v)` pair exists in either case.
* **P3-5 (§6) h = 385: WRITTEN_SUPPORTED.**
  * `S7`: the forced triples are `(2,0,0)/(0,3,8)` and cross differences have odd part 1.
  * For t = 1..5, the forced odd heads realize each odd residue mod `2^t` once, and the cross gcds are exactly `{2,…,2^t}`.
  * All 14 states of `x2` conflict (all t). Concretely, for t = 1..5 every `x ≡ 2 mod 165` conflicts.
  * NEG: at t = 3 with `2^t = 8` removed from P's bans, `x = 497` survives.
* **P3-6 (§7) positive Q-only control at n = 18480: WRITTEN_SUPPORTED** (non-load-bearing). It has 165 distinct elements, contains Y, avoids `{2,3,5,8,11,385}` and uses 105, 231, 4 and 16.
* **P3 claim (1): WRITTEN_SUPPORTED.**

### P4 — 165 family, odd |Q| ⇒ |Q| = 55

* **P4-1 (§2) imports and the list `{5,11,15,33,55,165}`: WRITTEN_SUPPORTED.** The Q gcds 1, 2, 6 and P gcds 3, 11 are confirmed (`S01`, `S8`).
* **P4-2 (§3) Q5, Q11: WRITTEN_SUPPORTED.** The abstract all-t check uses the odd ban `{1}`. The concrete check covers t = 1..6 with the full `Div(Y)`.
* **P4-3 (§4) Q15, Q33: WRITTEN_SUPPORTED.** Concrete t = 1..6 with the written bans `{1,2}` and `{1,2,6}`; the written `v_2 = 1` step is correct, including t = 1.
* **P4-4 (§5) Q165: WRITTEN_SUPPORTED** (concrete t = 1..6, written bans `{3,11}`).
* **P4 overall (only 55 can remain): WRITTEN_SUPPORTED** (see Note N1).
  * NEG: for t = 2..6 the same single-class head screen leaves one survivor for Q55. The method therefore does not silently exclude 55, which is consistent with Q55 remaining OPEN.

### Chain-level

* **CHAIN-2310: WRITTEN_SUPPORTED** as a conditional tiling statement. For n = 2310·2^k and anchored tilings, P1 + P2 + P3 give: odd |Q| ⇒ |Q| = 55.
* **CHAIN-165: WRITTEN_SUPPORTED** as a conditional tiling statement. For n = 165·2^t, P4 gives: odd |Q| ⇒ |Q| = 55.

Nothing here excludes Q55. Q55, even Q and the original problem remain OPEN.

## 4. Controls and receipts (independently authored, actually run)

* **Script:** `f169r1-controls-v1.py`, SHA-256 `94a92bde3bce4fb6ac918dd34029fa7a8e37c2c65f303f924205c3f54e1d0c32` (34,696 bytes).
  * Pure Python integer arithmetic (`math.gcd`, sets, loops, CRT by search).
  * It never imports or executes author code.
* **Recorded run:** `python3 -B` (Python 3.14.3, macOS-27.0.1-arm64).
  * Shell clock: Thu Oct 29 07:40:55 → 07:40:59 PDT 2026.
  * In-script `/bin/date`: 2026-10-29T07:40:56-0700 → 07:40:59-0700 PDT.
* **Output:** `f169r1-controls-v1.out.txt`, SHA-256 `08f18b0cd3af79ba48bd04731e9450e40634cc01c58cbe6d4be3f5634141acb3` (32,811 bytes).
* **Receipt:** `f169r1-controls-v1.receipt.json`, SHA-256 `1b7eecce44345a934056c322a6b814e51f691446779bf90def60c46e0557fb67` (1,004 bytes).
* **Result:** **245/245 checks passed: POS 221/221, NEG 17/17, CLAIM 7/7.**
* **Sections:**
  * `S00` binding
  * `S01` anchor divisor sets
  * `S1`–`S4` P1
  * `S5`–`S6` P2
  * `S7` P3
  * `S8` P4
  * `S9` P2 §6 relaxations
  * `S10` P1 §6 numbers
  * `S11` lemma sanity
* **Negative controls:** each one fails for its intended reason; the mutation is named in §3.

## 5. Exact dependency list

* **Imports.**
  * Łaba–Londner arXiv:2106.14042v3: Corollary 6.2 (T2 for both factors; the only deep import, used everywhere except P1 §5), Theorem 2.5 (Sands divisor exclusion), and (1.3), the cyclotomic form of tiling.
  * Coven–Meyerowitz T1/T2 definitions (their Theorem 1.1).
  * Elementary facts: `Φ_{p^α}(1) = p`, Gauss's lemma, `∏_{d|N,d>1} Φ_d = (X^N−1)/(X−1)`, CRT.
* **Conditional premises (tiling scope).**
  * `P ⊕ Q = Z_n` with `A = {0,3,8,11} ⊂ P` and `Y = {0,1,7,13,14} ⊂ Q`.
  * `n = 2310·2^k` (k ≥ 0) for P1–P3, `n = 165·2^t` (t ≥ 1) for P4.
  * `|Q|` odd.
* **Code-level application (outside scope, unreviewed).** Restivo–Salemi–Sportelli as Cordero Thm 1.1, plus the equivalence of the packets' "finite UD factor-complete extension" with a finite maximal code containing `b` and `aⁿ`.
* **Pinned data.** P1 §5 pair lists and the P2 §6 head list, parsed from SHA-verified bytes. The P3 §7 and P2 §6 CRT recipes were transcribed by hand.
* **Not used anywhere.** Any Q55 result, the odd-55 cofactor classification, the n2640 even-tail packet.

## 6. Findings

**FATAL 0 · MAJOR 0 · MINOR 0.** The notes below are not defects:

* **N1 (P4).** At t = 1 (n = 330) the anchors already violate Sands: `gcd(8,330) = 2 ∈ Div(A)` and `gcd(14,330) = 2 ∈ Div(Y)` (`S01`). The t = 1 case is therefore vacuous for every |Q|. The packet's arguments remain valid there.
* **N2 (P2 §6, non-load-bearing).** "54 individually compatible tail candidates" reproduces only when the five old tails are counted: 49 new + 5 old. "At least 116 absent mod-165 classes" holds exactly (116) under both readings.
* **N3 (dependency minimality).** The q = 15/33 exclusions (P1 §5) use only prime cyclotomics, so they do not depend on Corollary 6.2. Every other branch does.

## 7. Deviations and process disclosures

* **PDF access.** Both PDFs were hashed by streaming `curl` into `shasum`, with no file written. Their text was read through the harness reader. No `web_search`, external model, paid API, author contact, Git operation, deletion, publication or infrastructure change.
* **Dry runs before the recorded run** (no files written by any of them):
  * Dry run 1: one CLAIM check failed under the old-tails-excluded reading (49 ≠ 54). The check was then extended to log both readings and to test the old-tails-included reading (N2).
  * Dry run 2: killed by the 900 s harness timeout. `S11` had included moduli 42, 60 and 210, whose coset-factor tilings are exponentially numerous. A check confirmed no lingering process. `S11` was rewritten with most-constrained-point search and restricted to `Z_12`, `Z_20`, `Z_30`.
  * Dry run 3: all checks passed. The single recorded run followed, writing its output files with exclusive-create mode.
* **Writes.** All writes were made inside this review directory: the three `f169r1-*` files and this file. The write tool set the executable bit on the script. `-B` prevented `__pycache__`, and no temp directory was used.
* **Parent safety controls.** Two status-only controls arrived during the review (f162 Olson; f161). Neither concerns this wave, and none of their affected materials were opened.

## 8. Summary

All four frozen packets survive this same-harness review at the anchored direct-tiling scope, with no FATAL, MAJOR or MINOR findings.

* **The import is used within its hypotheses.** Łaba–Londner Corollary 6.2 (p. 26, read directly) requires that at most two primes divide both factor sizes. In every branch, |Q| is odd and the odd part of n is squarefree, so no prime divides both and the hypothesis holds. The resulting T2 gives the transversal property used throughout, and I reconstructed that step myself.
* **The 2310-family chain is supported.** The joint-prime screen forces at least two of 3, 5, 11 into |Q|. The cases q = 1155, 15 and 33 are excluded: the certificates are valid, the maximum matchings are 2/6/36/72, and the 9240-periodic lift is verified at k = 3, 4 and holds by the written argument for all k. The cases q = 385, 231 and 105 are excluded by exhaustive domain and backtracking checks plus the gcd-2 coupling. q = 165 is excluded by the coupled-gcd argument (forced 21/35/77, the three-way pigeonhole, exclusion of h = 105/231, and for h = 385 all 2-powers against tail x2). For odd |Q| this leaves only |Q| = 55 in the 2310 family.
* **The 165-family reduction to Q55 is supported.** It is vacuous at t = 1.
* **Conditions.** All of this is conditional on the imported Łaba–Londner results (Corollary 6.2 and Sands' Theorem 2.5) and on the anchors. The code-level bridge through Restivo–Salemi–Sportelli was transcribed but not reviewed.
* **What this is not.** This is a same-harness written review with my own exact controls (245/245 passed, receipts in §4). It is not human, independent-model-family, formal/kernel or novelty verification.
* **Still open.** Q55, even |Q|, other orders and the original problem.
