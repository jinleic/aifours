# f132 review — alternating degrees n ≥ 500,000 via Dusart close prime and Jordan prime-cycle theorem

- Review id: `f132-alternating-large-degrees-jordan-dusart`
- Kind: INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW (not human, not independent-model-family, not formal/kernel, not novelty clearance)
- Observed native clock before composing this file: `2026-10-28T20:35:17-0700 PDT` (`/bin/date` receipt in the shell log; the post-copy clock and file hashes are in `reviewer-receipt-v1.json`)
- Authority: `contract-addendum-2-frontier-first-owner-direction-v1.json` (as named by the manifest; not re-read here)
- Manifest: `manifest-v1.json`, SHA-256 `3422e973a70497843d9810aa5bac4a44225ae83cde4251e951d0823688efbc35`, 2671 bytes (verified)

## 1. Inputs read, in declared order, with verification

| # | Role | File | SHA-256 | bytes | LF | Verified |
|---|------|------|---------|-------|----|----------|
| 1 | Mandatory pre-source overlay | `sun-coset8/frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 | 56 | yes, read first and completely (raw) |
| 2 | Large-degree candidate | `sun-coset8/frontier-20261028-alternating-large-degrees-v1.md` | `be1dd7df8b322eac2bd06439be560b1d8b31967f8b3e6c220067a45bd12232f0` | 5522 | 42 | yes, read completely (raw) after the overlay |

Overlay content applied: it corrects two intermediate inequalities in ancestor files (`thirty-five-p7` line 19: `>` → `≥` with the final `>7` preserved by the strict `r+1>7t!`; `orbit-induction` line 26: the `j=1` / `2≤j≤6` split). The large-degree candidate is **not** in the overlay's inventory and does not cite either corrected intermediate; no ancestor body was opened. The overlay's non-claims are honored: nothing held is rehabilitated here.

Primary statements read directly (manifest-named entries only; no web search):
- Dusart, arXiv:1002.0442 — the abs page carries no proposition text, so the PDF of the same named entry was read. Proposition 6.8 (p. 8): **"For all x ≥ 396 738, there exists a prime p such that x < p ≤ x(1 + 1/(25 ln² x))."** The introduction restates it as the interval `[x, x + x/(25 ln² x)]` containing a prime for x ≥ 396 738. Dusart's proof sketch relies on η₂ = 0.0195 for ln x ≥ 28 (Theorem 5.2 / tables) plus Schoenfeld's maximal-gap bound p_{n+1}−p_n ≤ 652 for p_n ≤ 2.686·10¹² for the lower range; the PDF text extraction is lossy at the final threshold sentence. **Not replayed.**
- Jones, arXiv:1209.5169v1 (HTML): **Theorem 1.1 "Let G be a primitive permutation group of finite degree n, containing a cycle of prime length fixing at least three points. Then G ≥ A_n."** Jones attributes it to Jordan with references Dixon–Mortimer Thm 3.3E and Wielandt Thm 13.9, and in §3 derives it from Jordan's 1871 Théorème I and 1873 Théorème I. Jones's Comment 7 places the CFSG reliance on **Theorem 1.2** (the non-prime extension), not on Theorem 1.1. **Not replayed.**

Documentary hash checks (metadata only; the author script was neither read nor executed): `frontier-20261028-alternating-close-prime-check.py` → `762c23d8…882e79`, 1036 bytes, 37 LF (matches the candidate); `frontier-20261028-incidental-cross-topic-search-frontier-v1.json` → `d939059c…d93dec`, 1798 bytes (matches). The candidate's quoted overlay SHA `6c8f85cf…` matches input 1.

## 2. Load-bearing premises used in this review (all stated)

1. **[IMPORT, unreplayed]** Dusart Prop 6.8 as quoted above, statement level, arXiv v1 preprint.
2. **[IMPORT, unreplayed]** Jordan's prime-cycle theorem as Jones Thm 1.1, statement level. As attributed by Jones its proof is classical (pre-CFSG); I have not replayed Wielandt/Dixon–Mortimer. If a reader substitutes Jones Thm 1.2 / Cor 1.3 instead, CFSG enters; the candidate uses only Thm 1.1.
3. Elementary facts I verified by hand: Sylow/Cauchy in A_n; an element of prime order r with 2r > n in S_n is a single r-cycle; r-cycles (r odd) are even; the block/orbit arguments below; A_n (n ≥ 3) is transitive on u-subsets, 1 ≤ u ≤ n−1, with set-stabilizer index C(n,u); Lagrange tower divisibility.
4. Exact binomial arithmetic, independently controlled (§4).
5. The names "direct P7" and "Sun8" are **run-level labels not defined in my inputs**; I check them only under the readings the candidate itself states (seven proper subgroups with pairwise index gcd ≤ 7; eight pairwise disjoint cosets, whose subgroups are necessarily proper).

## 3. Independent reconstruction of the argument

### 3.1 Close prime (Section 2 of the candidate) — VERIFIED
- n ≥ 500 000 ⇒ x = 6n/7 ≥ 428 571.43 ≥ 396 738 (exact; smallest n with 6n/7 ≥ 396 738 is 462 861, so the threshold has slack). ln x > 12.8 > 1 (also log₁₀ x > 5.6 > 1, so the candidate's "log" is harmless; moreover a base-10 reading would only widen the interval relative to Dusart's ln-interval, so the import still implies it).
- Dusart gives prime r with x < r ≤ x(1 + 1/(25 ln² x)) < x·26/25 = 156n/175. Then 156n/175 < n − 3 ⇔ 19n > 525 ⇔ n ≥ 28. Hence r < n − 3, t = n − r ≥ 4 ≥ 3 (Jordan needs ≥ 3), and r > x = 6n/7 gives t < n/7, i.e., n > 7t; also t < r and r > 7. All exact (control P3).
- Left-endpoint robustness: whether Dusart's interval is read as `(x, …]` or `[x, …]` is immaterial, since x = 6n/7 is either a non-integer or (when 7 | n) a multiple of 6, never prime.
- Numerically at n = 500 000 the Dusart window forces t ∈ [71 327, 71 428] (informational, float).

### 3.2 r-free proper subgroups are intransitive — VERIFIED (conditional on import 2)
- r ≤ n and r odd ⇒ r | n!/2; 2r > n ⇒ r² ∤ n!, so Sylow r-subgroups of A_n have order r. If r ∤ [A_n:H] then r | |H|, H contains an element of order r, which (2r > n) is a single r-cycle σ fixing t ≥ 4 points. (The candidate leaves "r² ∤ |A_n|" implicit; it follows from r > 6n/7 > n/2 already established — MINOR presentation point, not a gap.)
- Transitive ⇒ primitive: a nontrivial block system has b blocks with 2 ≤ b ≤ n/2 < r; σ of prime order r > b fixes every block setwise; the single ⟨σ⟩-orbit of size r lies in one block, so block size ≥ r and n ≥ 2r — contradicting r > n/2. Correct.
- Primitive ⇒ (Jones Thm 1.1, prime cycle fixing ≥ 3 points) H ≥ A_n ⇒ H = A_n, not proper. Hence every r-free proper H is intransitive. Correct.
- The H-orbit Ω ⊇ supp(σ) has |Ω| ≥ r and Ω ≠ [n], so u = n − |Ω| satisfies 1 ≤ u ≤ t; H ≤ Stab_{A_n}(Ω) of index C(n,u); C(n,u) | [A_n:H]. Correct.

### 3.3 Binomial collision lemma (Section 3) — VERIFIED
For 1 ≤ i < j ≤ t with n > 7t, A = C(n,i), B = C(n,j), g = gcd(A,B):
- Identity C(n,i)·C(n−i,j−i) = C(n,j)·C(j,i): both sides count pairs I ⊆ J ⊆ [n], |I| = i, |J| = j. Correct.
- Dividing by g: (A/g)·C(n−i,j−i) = (B/g)·C(j,i) with gcd(A/g, B/g) = 1 ⇒ A/g | C(j,i). Direction correct.
- A/C(j,i) = ∏_{h=0}^{i−1} (n−h)/(j−h); each factor ≥ n/j because n ≥ j; product of i ≥ 1 factors each > 1 is ≥ n/j ≥ n/t > 7. Correct, including i = 1 (A/C(j,1) = n/j).
- If g ≤ 7 then A/g ≥ A/7 > C(j,i) ≥ A/g (positive divisor) — contradiction. So g ≥ 8 > 7. Correct.
- Equal case: 1 ≤ u ≤ t < n/2 ⇒ C(n,u) ≥ C(n,1) = n > 7. Correct.
- Tightness (my control): gcd(C(24,1), C(24,3)) = 8 and gcd(C(64,1), C(64,8)) = 8 with 7j < n, so the bound ">7" is attained; at the boundary n = 7t (n = 14, j = 2) the gcd is exactly 7 — the strict hypothesis n > 7t is genuinely needed.

### 3.4 Three-index conclusion — VERIFIED
Given three proper subgroups (repeats allowed): if two indices are divisible by r their gcd ≥ r > 7; otherwise two indices are r-free, hence divisible by C(n,u), C(n,v) with 1 ≤ u, v ≤ t, whose gcd (> 7 by §3.3, also when u = v) divides the gcd of the two indices. So among any three proper subgroup indices of A_n, n ≥ 500 000, some pair has gcd ≥ 8. Under the candidate's stated readings this excludes seven pairwise-gcd-≤7 indices ("direct P7") and, since eight pairwise disjoint cosets cannot involve the whole group, gives the k = 8 disjoint-coset statement ("Sun8") for these A_n. No Sun7/R8, A_r classification or factorial-terminal input is used — confirmed by reconstruction.

### 3.5 Small-n falsity note — CONFIRMED, hypothesis genuinely used
My own closure enumeration of A₅ (control N2): 59 subgroups, orders {1,2,3,4,5,6,10,12,60}, proper indices {5,6,10,12,15,20,30,60}; indices 5, 6, 15, 20 have pairwise gcds {1,5,5,3,2,5} ≤ 7, and already (5, 6, 15) are three proper subgroups violating the three-index statement. The argument cannot start at n = 5: t ≥ 3 together with 7t < n forces n ≥ 22. The n ≥ 500 000 hypothesis enters at (i) the Dusart threshold x = 6n/7 ≥ 396 738, (ii) r < n − 3 (needs n ≥ 28), and (iii) n > 7t, which drives both the block argument (r > n/2) and the gcd lemma. So the hypothesis is load-bearing, not decorative.

## 4. Independent exact control (actually run)

- Script: `reviewer-binomial-gcd-control-v1.py`, SHA-256 `70e71fe4ea8f97120aa8da8c8f0c1ce1efe1c3a1205708c1147d736319c91912`, 11 206 bytes, Python 3.14.3 stdlib only, written by the reviewer; **no author code read, imported or executed**.
- Receipt: `reviewer-binomial-gcd-control-v1.receipt.json`, SHA-256 `a3add4cf74ca51ad97ff24c72f5ba5357ce7cd94c91a17305c950ed633f69b52`, 4 086 bytes. Shell clock before run `2026-10-28T20:34:54-0700 PDT`, script-internal `20:34:55 → 20:34:58`, shell clock after `20:34:58`.
- Positive cases (all pass, 0 failures): P1(a) every n ∈ [22,300], t = ⌊(n−1)/7⌋, all 1 ≤ i < j ≤ t: 85 519 pairs (identity, divisibility direction, exact rational ratio bound, gcd > 7); P1(b) n = 510 510, t = 29: 406 pairs; P1(c) n = 500 000, all pairs with j ≤ 80 plus boundary pairs (1, 71428), (2, 71428), (71427, 71428), (1, 71427): 3 164 pairs. P2 equal-index C(n,u) ≥ n > 7: 6 339 cases. P3 Dusart threshold arithmetic in exact rationals.
- Negative cases (hypothesis violated, 7j ≥ n): 231 pairs over 125 distinct n ∈ [8,200] with gcd ≤ 7, e.g. (14,1,2) → 7, (10,1,2) → 5, (64,1,16) → 4, (8,1,4) → 2. A₅ enumeration as in §3.5.
- Side check S1: 510 481 is prime (trial division), t = 29, 7t < n, r > n/2; it is **not** the Dusart-window prime for x = 6n/7 (that window is (437 580, 437 684]) but satisfies the candidate's Section-4 condition 3 ≤ t < n/7; gcd of C(510510,u), u = 1..29, equals 1 (consistent with the candidate's "factorial residual is 1" remark, whose exact definition is not in my inputs), minimum pairwise gcd 24 310.

## 5. Findings

- **FATAL: 0.**
- **MAJOR: 0.**
- **MINOR (2, presentation only; conclusion unchanged):**
  1. Section 2 asserts the Sylow r-subgroup is "generated by an r-cycle" without stating r² ∤ |A_n|; this follows from r > n/2 (itself from r > 6n/7), which the candidate establishes. Suggested one-clause fix: "since 2r > n, r² ∤ n! and every element of order r is a single r-cycle."
  2. "log" is used where Dusart writes "ln"; only log x > 1 is used, true in every standard base, and a smaller-base reading widens the quoted interval, so nothing breaks. Also the candidate cites `https://arxiv.org/html/1002.0442v1`; the manifest names the abs entry and I verified the proposition from the PDF of that entry; the HTML URL was not tested.
- **Observations (not findings):** the constant 7 is tight in the gcd lemma (gcd = 8 attained at n = 24, (1,3) and n = 64, (1,8)); the candidate's example r for n = 510 510 is a different prime from the Dusart one, which Section 4 explicitly permits; the definitions of "direct P7" and "Sun8" are not in my inputs and were checked only under the candidate's stated readings.

## 6. Verdict (exact conditional scope)

**PASS at the conditional scope: FATAL 0 / MAJOR 0 / MINOR 2.** Conditional on (1) Dusart Prop 6.8 (arXiv:1002.0442v1, statement level, analytic/numerical proof unreplayed) and (2) Jordan's prime-cycle theorem as Jones Thm 1.1 (arXiv:1209.5169v1, statement level, classical proof unreplayed; no CFSG reliance is introduced by this import as attributed by Jones, whereas Jones Thm 1.2/Cor 1.3 would rely on CFSG and are not used), the written argument correctly proves: **for every integer n ≥ 500 000, among any three proper subgroups of A_n (repeats allowed) two have indices with gcd ≥ 8.** Under the candidate's stated readings this yields the direct-P7 exclusion and the eight-disjoint-coset (Sun8) statement for these A_n only.

**Explicit non-consequences.** Nothing follows from this review for any n < 500 000 (the statement is false at n = 5, and the candidate's own per-n extension "any n with a prime r, 3 ≤ n − r < n/7" was not surveyed or adopted here); nothing follows for any other finite simple group, for symmetric groups, for the global target, for Sun7/R8, for the A_r classification, for held or quarantined material, or for formal verification, human review, independent-model-family review, or novelty. The two imports remain unreplayed statement-level dependencies; any erratum to Dusart Prop 6.8 or to the attribution of Jones Thm 1.1 would propagate to this verdict.

## 7. Reviewer artifacts written (this directory only)

- `review-v1.md` (this file)
- `reviewer-binomial-gcd-control-v1.py`, `reviewer-binomial-gcd-control-v1.receipt.json`
- `reviewer-receipt-v1.json` (post-copy clock and SHA-256 of all four files)

No file outside this directory was created or modified; no Git, deletion, web search, external model, author contact or author-code execution occurred.
