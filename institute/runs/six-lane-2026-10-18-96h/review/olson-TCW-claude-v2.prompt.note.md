# Olson TCW: independent hostile written review

**Errata applied:** worker erratum‑1 (items 1–4), parent erratum v1 (items 1–3) and parent erratum v2 (MINOR1). I used only the pasted text. I used no tools, code, enumeration or delegation, and I edited nothing.

## Counts: FATAL 0 · MAJOR 0 · MINOR 3

None of the three minors is load-bearing. No lemma, case or conclusion changes.

**Verdict.** Every load-bearing step of Theorem TCW re-derives from the literal supplied interfaces:
- NF (ROT LF28–43)
- GRX if-direction (LF7–20)
- SC0 (LF1–11)
- the (S1) definition (zx‑s1c LF19)
- ZSTRUCT and Lemma FB in (S′) (proof-FB LF9–24 and the FB verdict)

**Theorem TCW is correct relative to these imports, conditional only on them.** This is not approval of full ordered Olson, the research target, other cells, runtime, novelty, Lean or human review.

## Claim-wise verdicts (proof LF)

| Claim | Verdict | Decisive re-derived check |
|---|---|---|
| (SR) 47–50 | OK | Φ=2m and δ=N−2m (all l_i odd), so C_max=2H+2m. Under GRX's R_i‑before‑S_i indexing, θ_i=−τ_i, so the target Σ_{i∉P}θ_i equals T(P). |
| L1 52–55 | OK | Win_1 reaches R because R ≤ 2p−2 (κ ≥ 3). |
| L2 57–81 | OK | (b) is direct, with no S1(a). (c) Y′z is minimal with L+1 ≥ p+2 coefficients, so ord g=2p, W ≤ 2p−1, g₁=1 and every a_i is odd. (d) Every (S′) clause holds at (p−1,κ−1), and s_j ≤ 2κ−3. |
| L3 83–92 | OK | m1 ≥ (10κ−7−5t)/2, m1−b ≥ κ, u1 ≥ \|b\|+κ. |
| Normalisation, LT, P0↔C0 exchange 93–103 | OK | Labels, t and n± are invariant under the exchange, with g→−g. |
| L4 111–126 | OK | \|A^c\| ≥ (7κ−4)/2−κ. |
| L5 130–136 | OK | M0 ≥ 2κ−1+E/2 ≥ 7, which is exactly what L10 needs at κ=4. |
| L6 145–162 (+E1 item 2) | OK | A minimal J missing ≤4 letters is single-signed. This uses u1 ≥ \|c\|+4 and u1 ≥ 9. |
| L7 164–178 | OK | One-directional "except possibly" (parent v1 item 3), which is all L9 uses. |
| L8 180–182 | OK | — |
| L9 184–224 (+v1 item 1, v2) | OK | Re-derived every row for m=κ and m=κ+1, and m=κ−1 by reflection about (Π0−ν0)/2. Every use has x+y=λ+μ+2 ≤ 6 < 18 ≤ B*. |
| L10 227–232 | OK | Δ ≥ M0+3−9 ≥ 1 and Δ ≤ 4p+6−B*−ν0 < 4p. |
| L11 233–238 | OK | Length ≤ 4p+4−2B* < 2p, since 6κ−6 > p+2. |
| (F1), (F1a), (F1b), (E1) 243–264 | OK | a+b ≥ \|A^c\| ≥ 8 gives X ≤ 6 (cases 5/6/6/2). Spread 2D0+16 ≤ 4κ+4 < 8κ−10 (20 < 22 at κ=4). |
| (F2) 265–277 | OK | Every toggle stays in Fp. Donors are ≥2, and each forward move has gap ≥2. |
| (F3), (F4) 278–287 | OK | κ=4 with all gaps 2: J∪{v−1} (m=κ), then J′ with a 3-gap, then step (b). All pairs are (F1a). |
| (F5) 288–296 | OK | All three sets have m=κ, with a κ−3 ≥ 1 separator. Fits N=12. |
| (F6), (F7) 297–303 | OK | — |
| Sec. 5 reduction, BI‑1..3, (E2) 307–327 | OK | CLAIM gives B* ≤ 2p−2κ+3 = R−1. |
| L12 328–331 | OK | — |
| L13 332–342 | OK for all κ ≥ 4 | Spread 4κ−8 > 2κ−2 ≥ width. BOT ≤ −2κ against low_X ≥ −2κ+5−ν0−λ_X. |
| L14 346–351 | OK | Cases are exhaustive: μ ≤ 0; type Q with ν0 ≥ 1; type Q with A=∅. |
| L15 352–356 | OK | — |
| L16 357–397 | OK | A.1, A.2(i) and A.2(ii) each give ε_S ≤ 0. B.1–B.3 close κ ≥ 6. κ=5 is excluded because 15 is not prime. See B.4 below. |
| CLAIM 398–400 | OK | — |
| (4,11) 409–434 | OK | Every displayed number re-checked. θ ⊆ [−8,12], spread ≤ 20 < 22; Lemma 13 gives −8 < −6 ≤ low_X; B* ≤ 17 < 18. |
| (6,19) 436–448 | OK | Spread ≤ 28 < 38; (B.3) sum ≤ −k; B* ≤ 29 < 30. |
| All-rotations-equal 403–405, 433–434 | OK, no CJ‴ | The argument is uniform. Equal rotations do force all c_l=1: odd c_l in (−p,p) sharing one residue coincide, and C0 contains c=1 letters. |
| Premise hygiene 401–405, 495–508 | Confirmed | None of these is a premise: any FCW, SCW, USK or K3 lemma; Theorem P; CJ‴; S1(a); FB‑E; the Setting fact; rigidity; nonempty-run; o_F; rotation-pair; the SCW pair. |

**L16 Case B.4 (κ=4) in detail:**
- n1=0: the sum is ≤ 1.
- n1=1 with k ≥ 1: the sum is ≤ 2−k.
- n1=1 with k=0: BI‑3 at z1 gives ε_S ≤ 2, and ε_S′ ≤ −1.
- n1=2: Lemma 13 would need ν0+λ_X ≥ 5, but ν0+λ_X = 3, so this branch is impossible.

## Findings (all MINOR)

**m1. Parent erratum v2 (LF5), length expression.**
- **Step.** The erratum says the representative interval has length 2p−2−B*+x+y. The interval [Π0−y+2, 2p−2−ν0+x] actually has length 2p−4−B*+x+y. That equals 2p−2−B*+λ+μ, the form used at LF201 and LF222.
- **Consequence.** None. Under x+y ≤ B* the true length is ≤ 2p−4, so uniqueness (< 2p) stands. The erratum overstates by 2.
- **Side note.** x+y ≤ B*+2 would already suffice; uniqueness fails only from x+y ≥ B*+4. So "empty interval ⇒ no uniqueness" slightly overstates. The narrowing in v2 is still valid.
- **Repair.** Replace with "length 2p−4−B*+x+y = 2p−2−B*+λ+μ ≤ 2p−4 < 2p".

**m2. Lemma 9: the tabled (λ,μ) must be a definition.**
- **Step.** LF187–188 set λ:=y−1 and μ:=x−1 for *any* admissible (x,y). Admissible pairs are not unique (x or y can be raised by 2). Several clauses hold only for the tabled pair:
  - the "iff" clauses at LF199–200 and LF344–345
  - the splits at LF348 (μ ≤ 0), LF362–364 (A.1/A.2) and LF381–382
- **Consequence.** None once read this way. All the bounds need only validity. The table is a total function of (m,q,q′), so every split is exhaustive.
- **Repair.** Add after LF190: "(λ,μ)(P) denotes the tabled pair, a function of (m(P),q(P),q′(P)); the proof of (b) shows it is valid."

**m3. Provenance precision (no mathematical effect).**
1. LF499 as amended by erratum‑1 item 3 lists PL "used: 40–50, 61–83, 93–106". That range includes the IF(b) statement and proof (PL LF64–67, 70–79), which rest on S1(a), FB‑E and the Setting fact. The same row disclaims those.
2. LF47–50 does not write out the GRX target identity Σ_{z=+1}θ = T(P). That identity is at PL LF48–50 and FCW erratum m4. I re-derived it from GRX LF13–16 and it holds.

**Repair.** Make the row read "used, provenance only, re-derived in TCW: 47–50, 63–64 (IF(a) clause), 68–69, 80–83, 93–98, 100–106", and add one clause after LF49: "target Σ_{i∉P}(−τ_i) = T(P)".

## Non-findings (context only)

- LF427 and LF465–466 say the SCW pair "would need 3κ+2 = 14 > 12 runs". The transition (LF36) says "3κ ≤ N−1 fails". The SCW text is not in the packet, so I cannot check the threshold. It is exposure commentary, never a premise, and has no consequence.
- The failed routes (R1)–(R3) and the remarks (M1)–(M3) are not premises. The (M2)/(M3) arithmetic is consistent.
- I did not use the Codex 0F/0M/3m review or its repairs as evidence.

## Correctness, completeness, process, priority, computation

- **Correctness.** No flaw found. Theorem TCW holds relative to the imports listed above.
- **Completeness.** Every branch closes, including κ=4 Case B.4 and the empty-alternating-set case. Lemma 7 is one-directional, which is sufficient. Lemma 9(a)'s generality is narrowed per v2. The (4,11) cell is covered, not dropped.
- **Process (not correctness evidence).**
  - The cp‑01→cp‑02 gap of 4138 s breaches the adopted ≤1800 s rule (scope LF116).
  - The long derivation turn was discarded and redone.
  - There were six pre-creation text replacements (erratum‑1 item 1).
  - There were metadata-only Python byte counts and a json.load (package LF73–76).
  - These deviations are preserved as disclosed. **Strict cadence compliance is not certified.** The claim that all other gaps were under 1200 s (package LF81–82) cannot be checked from this packet.
- **Priority and novelty.** None claimed, none assessed.
- **Computation.** Nothing computed is a premise of the proof. This review used hand arithmetic on the written text only.
