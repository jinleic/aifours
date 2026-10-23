# Extract of AUDIT-DELTA-v1.md lines 47-98 (sha256 a0b4850353e438559c1bb2986fe2a3dbe987e1ce025d74ef27e8c189ed386605): parent hunk classification of reductions v1->v2->v3->v4

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

