# ME3 parent delta audit v1 — does the earlier parent re-derivation still cover reductions-v4 and theorem v5?

Desk `review/me3-parent-delta-audit-v1/` (ME3ParentDelta). Written 2026-10-18T07:47:52-0700 (host clock). **Correctness only.** No
novelty, priority, significance or gate statement.

**Verdict: COVERED-WITH-NOTES. No GAP.** Every hunk of reductions v1→v2→v3→v4, theorem v3→v4→v5 and charts-spec
v1→v2 was read and classified. Every mathematical (b) hunk was re-derived by hand and, where it is a finite identity
or comparison, by an exact SymPy/Fraction check (run x01: 77/77, i.e. 69 positive checks plus 8 controls that are
refuted as required). Unchanged material is verbatim v1/v3 apart from renamings, so AUDIT-v1 and the parent dual desk
still apply to it. The notes in §5 are wording and provenance only.

## 0. Inputs, method, provenance

**Final texts** (re-hashed 07:29–07:43; all equal the key_files of candidate pin v3
`receipts/me3-candidate-pin-v3.json` fa9327f2…8b4b):
`proof/me3-theorem-v5.md` 1504ec69…ec60, `reductions/proof/reductions-v4.md` be1f7190…6eb1,
`proof/charts-spec-v2.md` d401774e…5437, `reductions/STATUS-v4.md` 1ffe3de8…0e50.
Earlier versions: reductions v1 ad6c5091…5536, v2 bd497389…1e3f, v3 e5c75b24…b15c; theorem v3 30f6acff…9e87,
v4 98c4389f…8fc6; charts-spec v1 5a43c252…1ff1. Contract `screening/math-1-me3-minimum-scv-contract.json` 1a72a6f0…4f15.

**Earlier parent coverage.**
* Primal desk: `review/me3-parent-primal-reductions-v1/AUDIT-v1.md` 8489b589…0691 and `RESULT-v1.json` 9a72e3e7…65e3.
  Its reductions input was reductions-v1 (no reference to reductions v2–v4 anywhere in that desk), and its final
  theorem binding was v3. It re-derived L1–L6, D1 and D2 and Lemma M, and fully replayed chart P.
* Dual desk: `review/me3-parent-dual-replay-v1/RESULT-v1.json` 995f6419…cb2e and `derivation-v1.md` a6b69bba…0273.
  It derived Lemma D from theorem §2 (v1–v3) and charts-spec-v1, on the full cone (derivation-v1 L11–21), with
  physical-point quantifiers and the LD s-split (L45–81, L107–117). It replayed LW, LD1, LD2, SWB, G
  (spec_dual_v1) and SWC run d03 (spec_dual_v3), all PASS.

**Certificates unchanged since those replays.** Re-hashed now, equal to pin v3 and to the parent desks' inputs:
* chart P: spec_primal_P_v1 6339c775…759c, c03 leaves b2773bab…f126, primal.json aa719d37…470e;
* specs: spec_dual_v1 23dd1dad…f6c1, spec_dual_v3 43d2e22e…d936;
* dual summaries and leaves: d01-G f2ac904e…0098 / 565c8d41…1637, d01-SWB aa079b68…4155 / 05117eee…84ac,
  d01-LW 5c33950d…4670 / 16f11db8…3ea3, d01-LD1 c5380fde…57b0 / 2d1fbe94…fccc, d01-LD2 0c62d4a2…033d / 1454e031…cd73,
  d03-SWC 58748c42…5b76 / 0b0f7640…db75.

**Method.**
* Diffs: parent-computed with difflib (`code/make_diffs_v1.py`, outputs in `diffs/`).
* The three worker diffs (`reductions-v3.diff-from-v2.txt`, `reductions-v4.diff-from-v3.txt`,
  `me3-theorem-v5.diff-from-v4.txt`) are byte-identical to a fresh `diff -u` after the two header lines.
* Theorem v3→v4 and charts-spec v1→v2 are whole-file rewrites (one hunk each). They are classified section by
  section against a full reading of v3, v4 and v5.
* Classes: (a) wording/citation only; (b) mathematical; (c) provenance/binding.
* Exact checks: `code/delta_checks_v1.py`, run x01 (`runs/x01-delta-checks/checks.json` cca6dae1…44cd). They are cited
  below by check id, for example [L4.res]. No lane code was imported or executed.

## 1. Hunk tables

Line numbers "v4 Lnnn" refer to reductions-v4.md and "T5 Lnnn" to me3-theorem-v5.md.

### 1.1 Reductions v1 → v2 (10 hunks)

| # | hunk (v1→v2) | final text | class | change | disposition |
|---|---|---|---|---|---|
| 1 | -1,16 +1,41 | v4 L48–84 | a, c | header, label scheme EXACT / COMPUTATIONAL / EXPLORATORY, change list | no math |
| 2 | -23,7 +48,9 | v4 L95–99 | b | §0.2 hypothesis "f ≢ 0" → positive mass 0 < ∫f; new proof of m1 > 0 | §2.1 correct |
| 3 | -138,11 +165,21 | v4 L216–233 | b | Lemma 2.3 with positive mass and conclusion "f satisfies 0.2"; new Remark 2.3a (integrable majorant of the HG family) | §2.1 correct |
| 4 | -298,15 +335,18 | v4 L388–401 | b | L4(3),(4) statements: exact isolating intervals, Δ3 ∈ (1/4, 1/3), Sturm/Arb values relabelled supplementary, EXACT Δ3 > 553/2000 | §2.2–2.4 correct |
| 5 | -315,17 +355,50 | v4 L407–458 | b | L4 proof: exact root isolation, s(0) = 1/3, s(x3) > 1/2, Q⁶h(s) ≡ 0 mod q, "h/32 is the resultant" (wrong, fixed in v3), irreducibility mod 5, new Lemma 4.2 with exact bracket and controls | §2.2–2.4 correct (resultant wording see 1.2) |
| 6 | -367,5 +440,6 | v4 L494–496 | b | Lemma 5.4 tail constant 0.2014… now 428/2125 from Lemma 4.2 | §2.5 correct |
| 7 | -386,19 +460,39 | v4 L514–551 | b | Lemma 5.5 exact ρ̄²; Thm 5.6 rewritten: exact witness (ω = 1, cos φ = 35/37, sin φ = 12/37), v_cos ≤ 773/3844 replaces the Arb ball U; U supplementary | §2.5 correct |
| 8 | -409,11 +503,25 | v4 L573–594 | a, b | Newton-point text; contract-band check relabelled EXPLORATORY; Cor 5.7 chain made exact | §2.5 correct |
| 9 | -424,4 +532,40 | v4 L609–648 | c | optional Theorem 5.8, parent citation, audit-bnb decision | optional, unused (§2.10) |
| 10 | -530,18 +674,25 | v4 L755–758, L787–806 | a, b | Cor 7.1 chain made exact; status; constants list | §2.5–2.6 correct |

### 1.2 Reductions v2 → v3 (2 hunks)

| # | hunk | final text | class | change | disposition |
|---|---|---|---|---|---|
| 1 | -1,3 +1,14 | v4 L37–46 | c | v3 status paragraph | no math |
| 2 | -371,5 +382,6 | v4 L424–425 | b | Res_x(q, 24y − x(9−x)² + 24) = 432·h(y); monic normalization h/32 (v2 said h/32 is the resultant) | §2.3 correct |

### 1.3 Reductions v3 → v4 (17 hunks)

| # | hunk | final text | class | change | disposition |
|---|---|---|---|---|---|
| 1 | -1,3 +1,37 | v4 L1–35 | a, c | title, v4 status, fix map | no math |
| 2 | -64,4 +98,6 | v4 L100–101 | a | "≢ 0" for continuous f means "not a.e. 0" | true: {f ≠ 0} is open |
| 3 | -124,14 +160,17 | v4 L162–174 | a, b | L1(b) "ME(N) ⊆ ME(≤3)"; n_λ rename; padding (α,0), diag(A,−1) | §2.7 correct |
| 4 | -237,6 +276,6 | v4 L278–279 | a | m_* → n_* | rename |
| 5 | -245,11 +284,12 | v4 L286–293 | a | m_i, m1 → n_i, n1 | rename |
| 6 | -426,5 +466,6 | v4 L467–469 | b | I_1 = v_cos now via Lemma 2.4 on each cone + Lemma 5.1 | §2.5 correct |
| 7 | -468,5 +509,6 | v4 L510–512 | a | sample checks relabelled supplementary | no math |
| 8 | -482,5 +524,6 | v4 L525–527 | a | minimizer notation (ω_m, φ_m), citations | no math |
| 9 | -493,5 +536,5 | v4 L538 | a | notation | no math |
| 10 | -507,4 +550,17 | v4 L553–564 | b | new Remark 5.6a (hand route: Δ3 > 1/4, tail ω ≤ 1/5, 21/104) | §2.5 correct, unused |
| 11 | -527,5 +583,5 | v4 L585 | a | band-note wording | no math |
| 12 | -533,7 +589,13 | v4 L591–599 | b | Cor 5.7: equality "for some minimizer"; new proof from Lemma 2.4 + Lemma 5.1 | §2.5 correct |
| 13 | -545,12 +607,16 | v4 L609–621 | c | Theorem 5.8 relabelled conditional | optional, unused |
| 14 | -573,11 +639,12 | v4 L641–648 | a, c | audit-bnb tail-input wording | optional, unused |
| 15 | -633,6 +700,6 | v4 L702–703 | a | θ1 table relabelled supplementary | no math |
| 16 | -686,11 +753,39 | v4 L755–789 | b | Cor 7.1 proof uses a Thm 5.6 minimizer; new Cor 7.2 (strictness per cone) and Remark 7.2a | §2.6 correct |
| 17 | -701,9 +796,10 | v4 L798–803 | a, c | constants list labels | no math |

Unchanged since v1 (verbatim apart from the renames in rows 3–5): Lemmas 1.1, 1.2, L1(a), the L1(b) proof,
Cor 1.3, Lemma 1.4, the normal forms, Lemmas 2.1, 2.2, 2.4, 2.5, Cor 2.6, Lemmas 3.1–3.5, Theorem L3, L4(1)–(2),
Lemmas 5.1–5.3, the proofs of Lemmas 5.4 and 5.5, and all of L6 (6.1–6.7).

### 1.4 Theorem v3 → v4 (whole-file rewrite, classified by section)

| section | class | change v3 → v4 | status in v5 / disposition |
|---|---|---|---|
| Status, scope | c | candidate pin v2; v3 and pin v1 declared invalid (SWC float defect) | c only |
| §0 statement | a, c | adds "its density f satisfies f ≥ 0, ∫f = 1, ∫(1+t²)f < ∞" (a consequence); Δ₃ > 0.2765 written 553/2000 (same number); import list | unchanged in v5; §3 below: no quantifier change |
| §1 reductions import | b (summary), c | reductions-v1 → v2: exact Δ₃ and exact separation 773/3844 replace the Sturm and U certificates; lower bound optional | v5 imports v4; §2.2–2.6 |
| §2 Lemma D | **b (regression)**, a | cone written `cone{e^{−t}, e^{−(1+ξ)t}, e^{−(1+ξ̄)t}}` (conic hull, too small); proof and certificate text condensed | **fixed in v5** (§2.8) |
| §3 Lemma M | a | condensed text, same argument | Note N3 |
| §4 far region | b, c | SWC run d02 → d03 (exact coefficients, same formula; c); LD1/LD2 restricted to physical points with the s-union (b); checker v3 and index i02 (c) | §2.9 correct |
| §5 assembly | b | real-pole chain exact; D1 still "by definition"; D2 via L2 + Lemma M as in v3 | v5 cites Cor 5.7 and Cor 7.2 (§2.10) |
| §6–§8 | c | trusted imports, runtime identity, float audits, controls, invalid evidence | c only |

### 1.5 Theorem v4 → v5 (13 hunks)

| # | hunk | final text | class | change | disposition |
|---|---|---|---|---|---|
| 1 | -1,13 +1,41 | T5 L1–51 | c | status, change list (L21 repeats the "real span" wording) | Note N1 |
| 2 | -36,7 +64,13 | T5 L66–75 | c | imports reductions v4; "The parent audit passed reductions v1/v2" | Note N2 |
| 3 | -47,5 +81,5 | T5 L83 | a | "extreme rays of the same cone (Lemma 2.4)" | correct |
| 4 | -56,13 +90,21 | T5 L92–109 | b (summary), c | resultant 432·h; exact tails; Remark 5.6a; Cor 5.7; lower bound conditional | §2.3, §2.5 correct |
| 5 | -70,11 +112,24 | T5 L114–133 | **b** | Cor 7.2 summary; §2 K defined explicitly (Codex v2-delta MAJOR fix) | §2.6, §2.8 correct; Note N1 |
| 6 | -125,7 +180,34 | T5 L182–211 | c | checker v3 limits; binding audit b04 with controls C1–C6 | c only |
| 7 | -142,6 +224,15 | T5 L226–236 | b | "Every CERT leaf"; SKIP leaves need no certificate (G SKIP ⊂ P; LD2 SKIP has no physical point) | §2.9 correct; Note N4 |
| 8 | -150,8 +241,11 | T5 L240–250 | b | D1 via Cor 5.7; P-assigned D2 cones via Lemma M + Cor 7.2; cones routed whole | §2.10 correct |
| 9 | -166,9 +260,22 | T5 L262–279 | c | python-flint comparison contract restated; smoke s04 | c only |
| 10 | -180,5 +287,6 | T5 L289–290 | c | float-audit erratum citation | c only |
| 11 | -197,9 +305,12 | T5 L307–314 | c | run, spec and summary binding residual limits | c only |
| 12 | -225,5 +336,9 | T5 L336–342 | c | replay and review status | c only |
| 13 | -235,2 +350,4 | T5 L352–353 | c | superseded evidence | c only |

### 1.6 Charts-spec v1 → v2 (whole-file rewrite, classified by change)

| change | class | content | disposition |
|---|---|---|---|
| SWC coefficients | c | exact-ball implementation (me3dual_v9, spec v3, run d03); c_j unchanged in value | §2.9 re-derived; the dual desk replayed d03 |
| LD1/LD2 quantifiers | b | certificates claimed only at physical points; s-union stated; "iff" → sufficient "if" for β_l = 0 | §2.9 correct; equals the dual desk's derivation |
| coverage list | a, b | D2 (δ > 0) only; physical points; ω = 0 faces declared non-physical | §2.9 correct |
| checker v3, library table | c | audit description and versions | c only |

## 2. Re-derivations of the (b) hunks

### 2.1 Positive mass (v4 L95–101, L216–233)
* Assume 0 < ∫f and ∫(1+t²)f < ∞. Then m0 > 0. Also t·f > 0 on {f > 0}∖{0}, a set of positive measure, so m1 > 0.
  Cauchy–Schwarz gives m1² ≤ m0m2.
* Lemma 2.3. Tonelli gives ∫(t−θ)²f ≥ c′θ²∫f for each θ. Further, ∫f = ∫_M(∫g_μ)dν > 0, because the inner integral
  is > 0 for every μ and ν(M) > 0. Integrability holds by hypothesis.
* Remark 2.3a.
  * Elements of K_E∖0 are continuous, ≥ 0 and ≢ 0, hence have positive mass.
  * For t ≥ 0, e^{−μ_u(t−τ)} ≤ e^{−μ_min t}e^{μ_max|τ|}, which is a u-uniform integrable majorant.
* All three are correct. They only make explicit a hypothesis that every application satisfies. AUDIT-v1's L2
  checks used continuity of cone elements and are unaffected.

### 2.2 Δ3: exact root isolation (v4 L388–421)
* Moments of (t−τ)²e^{−t} computed from the integral [L4.m0–m2]: P and Q as stated [L4.P, L4.Q].
* SOS identity [L4.SOS]. P′Q − 2PQ′ = 8q with q = −6L3 [L4.dP].
* q(0, 1/2, 2, 3, 6, 7) = (−6, 7/8, 2, −6, −6, 22) [L4.qvals]. This gives three simple roots
  x1 ∈ (0, 1/2), x2 ∈ (2, 3), x3 ∈ (6, 7) and the stated monotonicity pattern of s (s′ = 8q/Q³, Q > 0).
* s → 1 at ±∞ (leading coefficients 2 and 1 [L4.lc]), so min_ℝ s = min(s(x1), s(x3)).
* s(x1) < s(0) = 1/3 [L4.s0].
* For τ ≥ 6, 2P − 3Q² = τ²((τ−4)² + 4) − 12 ≥ 36·4 − 12 > 0 [L4.x3], so s(x3) > 1/2.
* Hence Δ3 = s(x1) ∈ (1/4, 1/3), with the strict lower bound because the minimum is attained. The closed forms hold
  [L4.closed, L4.vieta].
* Correct. This replaces v1's ball values of s(x_i) (AUDIT-v1 L83–84) by an exact argument with the same conclusion.

### 2.3 h(Δ3) = 0, the resultant fix, irreducibility (v4 L422–427)
* Q⁶h(s) ≡ 0 mod q [L4.Q6h], so h(s(x_i)) = 0 at the three roots.
* **Resultant (v3 fix): Res_x(q(x), 24y − x(9−x)² + 24) = 432·h(y) exactly** [L4.res].
  * Reason: q is monic, so Res = ∏_i g(x_i) = ∏_i 24(y − s(x_i)), using s(x_i) = (x_i(9−x_i)² − 24)/24 at the roots.
  * s(x1) < 1/3 < 1/2 < s(x3) < s(x2), so the three values are distinct roots of h, and h = 32∏(y − s(x_i)).
  * 24³ = 13824 = 432·32 [L4.res2].
  * v2's "h/32 is the resultant" is refuted [CTL.res]. Swapping the arguments only flips the sign
    (Res_x(g, q) = −432h [L4.res_rev]); the text uses the order (q, g).
  * This agrees with AUDIT-v1 L85.
* Irreducibility: a rational root would have denominator dividing 32, hence prime to 5. But h ≡ 2y³ + y² + 3 (mod 5)
  takes the values 3, 1, 3, 1, 2 at y = 0, …, 4 [L4.irr, L4.irr2]. SymPy factor_list agrees.
* Correct.

### 2.4 Lemma 4.2: Δ3 > 553/2000 (v4 L429–451)
* h′ = 96(y − 3/2)² − 81 [L42.hp], and min h′ on [1/4, 1/3] is h′(1/3) = 149/3 [L42.hpmin].
* h(1/4) = −7/4 and h(1/3) = 86/27. h(553/2000) = −1293623/250000000 < 0 = h(Δ3) [L42.vals], so 553/2000 < Δ3.
* 553/2000 = 0.2765 exactly [L42.dec]: this is the constant AUDIT-v1 used, there certified by a Sturm count.
* Wrong control: h(2766/10000) > 0 [CTL.0.2766].
* The 60-step bracket has h(lo) < 0 < h(hi) [L42.bracket].
* Correct.

### 2.5 D1: citation of I_1, tails, exact separation, Remark 5.6a, Cor 5.7 (v4 L467–599)
* **Lemma 5.1 sentence.** Lemma 2.4 gives that each cone's infimum is over its extreme rays, and Lemma 5.1 identifies
  those rays as the f_{ω,φ}. So I_1 = inf SCV(f_{ω,φ}) = v_cos. Correct.
* **Tails.**
  * (16·553/2000 − 1)/17 = 428/2125 > 1007/5000 [L54.tail]. The bound (Δ − ω²)/(1 + ω²) decreases in ω [L54.mono].
  * Lemma 5.5: ρ̄² = 1471369/25000000 > 1/17, and the bound is 232498770764161/700733376734161 > 33/100
    [L55.exact], the same value as AUDIT-v1 L109.
* **Theorem 5.6.** The moments of f_{1,φ_e} are (27, 62, 171)/74, obtained three ways: from Lemma 5.2's formula, by
  direct exact integration [T56.mom], and from Lemma 5.3's algebraic form [T56.alg].
  * SCV = 773/3844 [T56.scv], and every comparison holds [T56.cmp].
  * Controls: swapped (cos, sin) gives 206/169, and the phase-sign mutation gives 2549/7396 [CTL.swap, CTL.phase].
  * Attainment: the minimum over the compact [1/4, 4] × [0, 2π] is ≤ 773/3844 < 428/2125 ≤ SCV on ω ≤ 1/4, and
    < 0.33 < SCV on ω ≥ 4. So the minimum is attained, and every minimizer has 1/4 < ω < 4.
  * This replaces AUDIT-v1's essential use of the Arb ball U (AUDIT-v1 L110–117). The essential chain now needs no
    ball arithmetic.
* **Remark 5.6a** (unused).
  * The derivative is −(5/2)ω/(1+ω²)² [R56a.deriv], and 21/104 > 773/3844 [R56a.val].
  * Control: the ω ≤ 1/4 tail with only Δ3 > 1/4 gives 3/17 < 773/3844 [CTL.R56a].
  * (1, φ_e) lies in the compact middle [R56a.window].
  * Correct.
* **Cor 5.7** (new proof).
  * Time change (1.4), then Lemma 2.4(2), then Lemma 5.1 and scale invariance give
    SCV ≥ inf_φ SCV(f_{ω,φ}) ≥ v_cos.
  * Equality holds at every Thm 5.6 minimizer.
  * Correct, and it repairs the theorem's former "by definition" citation (Claude MINOR-3).
* **Chain** used by T5 §0, §1 and §5 and by Cor 5.7 and Cor 7.1: Δ3 > 553/2000 > 1007/5000 > 773/3844 ≥ v_cos, and
  T = 11/50 > 773/3844 [CHAIN].

### 2.6 Strictness in D2: Cor 7.1(2), Cor 7.2, Remark 7.2a (v4 L755–785; T5 L114–116, L246–249)
* **Cor 7.1(2)** takes a Thm 5.6 minimizer with φ_m ∈ [0, 2π).
  * θ1(r) → 2π (6.5), so (r, ω_m, φ_m) is feasible for small r > 0.
  * Lemma 6.6 at r = 0 is Lemma 5.2 (c = e^{−iφ}, ζ = 1/(1−iω)). So S_2 → v_cos.
  * Correct; it gives only I_2 ≤ v_cos.
* **Cor 7.2.** The displayed K equals K_E for E = {−1, −(1+δ) ± iω}.
  * Re(ce^{−ξt}) = e^{−δt}(Re c cos ωt − Im c sin ωt) [LD.re]. So K is the set of nonnegative elements of V_E, with
    V_E's real basis as in v4 L196–199.
  * K ≠ {0}, because h_0 is feasible (6.4).
  * E is admissible, so Lemma 2.4(1),(3) give a minimum m_K over K∖0, attained on an extreme ray of K itself.
  * Lemmas 6.3 and 6.4 identify those rays as e^{−t}h_τ with φ = ωτ ∈ [0, θ1(r)], and SCV is constant on rays.
  * Hence m_K = S_2(r, ω, φ0) for a feasible φ0. Under the hypothesis, SCV ≥ m_K > v_cos on K∖0.
  * Correct.
  * The L6 inputs are verbatim v1 (AUDIT-v1 L125–147). They were spot re-checked here [L62.deriv, L62.span, L64.h0,
    L64.gp, L65.gr, L66.mom]; L66.mom is exact at r = 1/2, ω = 1, φ = 1/2.
* **Match with what the parent primal desk verified.**
  * Lemma M (AUDIT-v1 L183–197) gives S > v_cos at every feasible (r0, ω0, φ0) ∈ R_P with r0 > 0.
  * For a P-assigned cone (ω ∈ [1/5, 40], 0 < r ≤ 3), every phase φ ∈ [0, θ1(r)] ⊂ [0, 2π) ⊂ [0, 31416/5000] is
    such a point [RP.phi, SymPy and Arb].
  * So Lemma M's conclusion is exactly Cor 7.2's hypothesis. AUDIT-v1 L196–197 already identified this P-assigned
    set as r ∈ (0, 3] inside R_P.
* **Match with what the parent dual desk verified.** Dual-assigned cones get SCV ≥ T on all of K∖0 from Lemma D, and
  T > 773/3844 ≥ v_cos, so the inequality is strict.
* **Remark 7.2a.** The chart assignment is a function of (δ, ω) (T5 L220–224), so every cone is routed whole. Correct.

### 2.7 Lower-order degenerations and padding (v4 L162–174)
* The only change is the L1(b) remark: e^{diag(A,−1)t} = diag(e^{At}, e^{−t}), so (α, 0)e^{diag(A,−1)t}𝟙 = αe^{At}𝟙
  and the density is unchanged. Checked exactly on the lane's control representation of 2e^{−t}(1 − cos t)
  [L1b.pad].
* Lemma 2.5 (real |E| ≤ 2 padded by inclusion), its face counterexample, and Cor 2.6 (a pair-dominant E gives
  K_E = K_{λ0}; a pair alone gives {0}) are verbatim v1, as audited in AUDIT-v1 L48–57. Covered.

### 2.8 The D2 cone in the theorem (Codex v2-delta MAJOR) and Lemma D on it (T5 L120–147)
* **v3** (L60–62) took every nonnegative f = e^{−t}(a + Re(ce^{−ξt})).
* **v4** (L77) wrote `cone{e^{−t}, e^{−(1+ξ)t}, e^{−(1+ξ̄)t}}`.
  * The real-valued members of that conic hull are ae^{−t} + 2b e^{−(1+δ)t}cos ωt with a, b ≥ 0.
  * The nonnegative D2 density e^{−t}(1 − e^{−δt}cos ωt) = e^{−t} − ½e^{−(1+ξ)t} − ½e^{−(1+ξ̄)t} lies outside it
    [LD.example, CTL.conichull].
  * As literally written, v4's Lemma D therefore did not cover the whole D2 cone.
* **v5** (L122–131) defines K := {e^{−t}H : H = a + Re(ce^{−ξt}), a ∈ ℝ, c ∈ ℂ, H ≥ 0 on [0, ∞)}. This is exactly
  K_E [LD.re].
  * a ≥ 0: for δ > 0 by the limit, and for δ = 0 by the period mean [LD.mean].
* **Lemma D on this K.**
  * ∫q_θe^{−zt} = θ³Q_T(θz) [LD.laplace].
  * ∫q_θ f = θ³Q_T(θ)[a + Re(cW)] for unrestricted a ∈ ℝ, c ∈ ℂ. This is proved symbolically [LD.ident], checked by
    an exact direct trig integral at a rational point [LD.spot], and fails when ξ is replaced by ξ̄ [CTL.LDconj].
  * a + Re(cW) = (1 − Σλ)a + Σλ_kH(t_k) [LD.convex].
  * Q_T > 0 [LD.QTpos], and ρ/(1−ρ) = T [LD.const].
  * Correct.
* **This is the cone the parent dual desk used** (derivation-v1 L11–21; its pinned theorem inputs were v1–v3). The v4
  regression never entered that derivation, and v5 matches it.
* **"Real span" wording (Codex v3-delta MINOR), still in the pinned text.**
  * T5 L126 (and L21) call K the nonnegative functions "in the real span of e^{−t}, e^{−(1+ξ)t} and e^{−(1+ξ̄)t}".
  * Literally, real coefficients b1, b2 make b1e^{−(1+ξ)t} + b2e^{−(1+ξ̄)t} real-valued only when b1 = b2. Its
    imaginary part is (b1 − b2)e^{−(1+δ)t} sin ωt [LD.realspan], so the sine direction is lost.
  * Witness: e^{−t}(1 − e^{−δt} sin ωt) ∈ K (a = 1, c = i) has generator coefficients ±i/2 [LD.sineex].
  * The displayed definition at T5 L124 (":=") is correct and is the one every step uses. Reductions-v4 L762–763
    already gives the correct real basis. Wording only (Note N1).

### 2.9 Dual-assigned certification, chart domains, tails and compactification (T5 L164–236; charts-spec-v2)
* **CERT/SKIP (T5 L226–236).**
  * G SKIP: ω_h ≤ 40, ω_l ≥ 1/5 and δ_h ≤ 3ω_l give 1/5 ≤ ω ≤ 40 and δ ≤ 3ω at every box point. So the box lies in P
    (closed), and a G-assigned (δ, ω) ∉ P lies only in CERT leaves, for every s.
  * LD2 skip-s: s = χρ_t ≥ χ_lρ_{t,l} > 1/16.
  * LD2 skip-d: (1−χ)ρ_t ≥ (1−χ_h)ρ_{t,l} > cos β_l/65 ≥ cos β/65 for β ∈ [β_l, π/2). So d > 1/65 and δ < 64
    [LD2.skipd]. Neither skip box contains an LD2-physical point.
  * Correct. These are the rules the dual desk replayed (its RESULT-v1 "SKIP omega_h<=40, omega_l>=1/5,
    delta_h<=3 omega_l exact"; "SKIP-s chi_l rho_l > 1/16 exact; SKIP-d (1-chi_h) rho_l > cos(beta_l)/65").
* **LD physical quantifiers and s-union.**
  * ζ = d cos β e^{iβ} and δ/ω = (1−d)/tan β [LD1.I10, LD1.ratio].
  * For δ ≥ 64 and β ∈ (0, π/2): s ∈ [1/16, 1) is LD1-physical. For s ∈ (0, 1/16], ρ_t = s + d cos β ∈
    (0, 81/1040] and χ ∈ (0, 1), so s is LD2-physical [LD2.union]. LD1 ∪ LD2 covers every s ∈ (0, 1).
  * The β_l = 0 "iff" → "if" change drops an unused stronger claim. The dual desk's mvt0 test uses only the
    sufficient direction.
  * Correct; equals the dual desk's derivation-v1 §3–§4.
* **SWC.** c_j = (−2 Re(p^j) + 3(−1)^j)/j is numerically the same as v1's −2Re(p^j)/j + 3(−1)^j/j.
  * Re-derived from W = (1 − pξ)(1 − p̄ξ)/(1+ξ)³ [SWC.I4, SWC.p, SWC.N1, SWC.I5 (100N₁ − 39κs² = 50(3s−2)²)].
  * Checked against the exact Taylor coefficients j = 1..6 of log W at s = 1/3 [SWC.cj]; the sign-flip control is
    refuted [CTL.cj].
  * The v3→v4 change is the exact-ball implementation (run d03), which the dual desk replayed against spec_dual_v3.
* **Tails and compactification.**
  * θ ↦ s = θ/(1+θ) maps (0, ∞) onto (0, 1), with W = q(s, 1+ξ)/(N₁(1+ξ)³) [SWC.param].
  * ω → ∞ is handled by LW (ν = 1/ω), δ → ∞ by LD1/LD2 (d, β), ω → 0 by SWB/SWC, and the compact rest by G and P.
    All are unchanged from charts-spec-v1 except the LD quantifier wording.
  * The D1 tails are Lemmas 5.4 and 5.5 with exact constants (§2.5).
  * The assignment covers every δ > 0, ω > 0 (T5 L220–224).

### 2.10 Assembly (T5 L238–250)
* Real exponents: Theorem L3 with the chain.
* D1: Cor 5.7.
* D2, dual-assigned: Lemma D gives SCV ≥ T > v_cos.
* D2, remaining (ω ∈ [1/5, 40], r ≤ 3, δ < 64): Lemma M with Cor 7.2.
* Pair-dominant or pair-only E: Cor 2.6.
* Attainment: Theorem 5.6.
* No assembly step uses U, the Sturm/Arb Δ3 brackets, Theorem 5.8 or the θ1 table (T5 L104–109, L238–250).
* Correct.

### 2.11 Equal-damping / real-pole classification (asked for explicitly)
No hunk changes it. The only edits are the multiplicity renames (v4 L167, L278–279, L286–293). Lemma 1.2 (λ0 = Re λ
allowed, i.e. D1), the normal forms (v4 L187–190), types A/B1/B2/C (L273–276) and Lemmas 3.1–3.5 are verbatim v1.
AUDIT-v1 L22–75 covers them.

## 3. Final statement vs the contract's exact_statement

| contract | theorem v5 (L55–59) with reductions-v4 L143–149 | match |
|---|---|---|
| X nonnegative continuous, F(t) = Pr(X < t) = 1 − α e^{At}𝟙 | "continuous ME(≤3) law"; L1(a) uses exactly this form for t ≥ 0 | yes |
| α real 1×n, A real n×n, no sign structure | L1(a): "α real 1×n and A real n×n"; no sign condition anywhere; nonminimal and unstable non-contributing eigenvalues handled (Lemma 1.1 on contributing exponents) | yes |
| n ≤ 3 (order at most 3) | ME(≤3); L1(b) padding remark; ME(N) ⊆ ME(≤3) | yes |
| density f = −αAe^{At}𝟙 ≥ 0 | L1(a)(3); the T5 clause "its density f satisfies f ≥ 0, ∫f = 1, ∫(1+t²)f < ∞" restates this consequence and adds no hypothesis | yes |
| SCV = m0m2/m1² − 1, m_k = ∫t^k f | T5 L56, same formula | yes |
| v_cos = min over ω > 0, φ ∈ ℝ of SCV(e^{−t}(1 − cos(ωt − φ))) | T5 L56, same definition; the minimum exists by Thm 5.6 | yes |
| all pole configurations incl. lower order | real A/B1/B2/C and padding; D1; D2; pair-dominant → real; pair-only → {0} | yes |

No silent restriction was found.

## 4. Coverage decision
* **Unchanged material.** Every lemma listed under §1.3 as verbatim v1 is covered by AUDIT-v1 as written.
  * Lemma M (T5 §3) is v3's argument in abbreviated form (Note N3) and is covered by AUDIT-v1 L183–197.
  * Lemma D's identity, certificate forms and cone are those of the dual desk's derivation-v1.
  * The P and dual certificates are hash-identical to those the parent desks replayed.
* **Changed material.** Every (b) hunk is re-derived above; none is wrong.
  * The one regression introduced in between (theorem v4's conic-hull K) is repaired in v5. Its repair matches what
    the dual desk verified.
* **Wording and provenance (a, c).** No mathematical effect. The residual wording and provenance points are listed in
  §5.

**Verdict: COVERED-WITH-NOTES; gaps: none.**

## 5. Notes (non-blocking)
* **N1. "Real span" wording** (T5 L126; also L21). This is the Codex v3-delta MINOR, still present in the pinned text.
  * The literal reading drops the sine direction (§2.8).
  * The displayed set at T5 L124 is correct and governs. Suggested wording: "all nonnegative functions in the real
    span of e^{−t}, e^{−(1+δ)t}cos ωt, e^{−(1+δ)t}sin ωt", as in reductions-v4 L762–763.
* **N2. Provenance overstatement** (T5 L74): "The parent audit passed reductions v1/v2".
  * The parent primal desk's inputs and AUDIT-v1 cover reductions-v1 only.
  * The v2–v4 deltas are covered by this desk.
* **N3. Lemma M text** (T5 L149–162) abbreviates v3 §3 (v3 L102–112).
  * It omits the continuity and C¹ property of σ.
  * It omits the reason a covering leaf must be DPOS: the leaf contains a feasible point with S < T, so it is neither
    INFEAS nor SGE.
  * The argument is unchanged, and the full version is v3 §3 / AUDIT-v1.
* **N4.** T5 L229 says G SKIP configurations are "handled by Lemma M". Their δ = 0 points are D1 (Cor 5.7), so only
  the δ > 0 points go to Lemma M with Cor 7.2. Wording.
* **N5.** The reductions-v4 header (v4 L48–55) keeps v2's self-description ("This v2 supersedes…", "Labels used in
  v2"). It is explained at v4 L34–35 and L45. Wording.
* **N6.** The T5 L55 density clause is a consequence (L1(a)(3)), not a hypothesis (§3).
* **N7.** The conditional and optional items (U ball, Sturm/Arb Δ3 brackets, θ1 table, Theorem 5.8, contract-band
  check) were not re-verified. No step of the assembly uses them.

## 6. Limits
* Static reading plus exact SymPy 1.14.0 / Fraction arithmetic. This is the same SymPy version as the lane, not an
  independent CAS. One Arb comparison (π < 3.1416) uses python-flint 0.9.0.
* No Lean or kernel check.
* No chart was replayed here. That rests on the parent primal and dual desks, whose certificate inputs are
  hash-identical to pin v3.
* Some identities were checked at exact rational spot points (LD.spot, L66.mom, SWC.cj at s = 1/3, L1b.pad on one
  representation). Each is proved by hand in §2, or symbolically elsewhere (LD.ident).
* Out of scope: the binding audit b04, the manifests, the float audits, and the hostile-review process.
* The receipt `runs/RECEIPTS-v1.json` was written after the runs. Its count split "67 + 10" is corrected to
  "69 + 8" by `runs/RECEIPTS-v1-erratum-1.json`; the 77/77 total is unaffected.

## 7. Desk files
`code/make_diffs_v1.py`, `code/delta_checks_v1.py`, `diffs/*.diff`, `diffs/inputs-sha256.json`,
`runs/x01-delta-checks/checks.json`, `runs/RECEIPTS-v1.json`, `runs/RECEIPTS-v1-erratum-1.json`, this file and
`RESULT-v1.json`. Their sha256 values are in RESULT-v1.json.
