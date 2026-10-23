# HIGH-K-CORE v1 — second-family hostile written review

This review covers the core proof through worker errata 1–2 and the parent precision erratum v1.

**Method and inputs**
- Hand reasoning only, from the pasted text. No tools, code, computation, enumeration, solver, Lean, network or delegation were used.
- Inputs read: the governing parent erratum (LF1–9), package v2, manifest v2, coverage v2, cp06, and all 16+16 blocks of Parts 1 and 2.
- I did not verify any hash or byte pin. The only metadata I checked was internal LF arithmetic, which is consistent with the manifest:
  - Part 1: 882 source LF + 16×4 header LF = 946.
  - Part 2: 631 + 64 = 695.
- This review is not blind. I saw the parent erratum's summary of the first-family counts. I did not rely on that summary, or on cp05's report of a parent hand check, which is not pasted.

## Verdict

- **FATAL 0 / MAJOR 0 / MINOR 7.** Three are required documentary fixes and four are optional. No lemma, inequality, case, outcome or residual test changes. All seven can be disposed by numbered errata.
- **Source gate: PASS for this family.** No omitted body is load-bearing, so nothing here triggers RE_REVIEW_REQUIRED.
- **Outcome (c) is confirmed.**
  - HIGH-K-CORE-COVER is NOT_PROVED.
  - LOW-CORE, TOP-CORE and P-CRITICAL-DIAGONAL are NOT excluded.
  - HK1 HIGH-K-RES (R0)–(R3) is unchanged.
- **First-family findings:** the parent erratum targets and disposes all three correctly, with one documentary caveat on the second sentence of its item 1 (R-3 below).

## Per-item result

| # | Item (LF) | Result |
|---|---|---|
| 1 | (G) in P-form + erratum 1 full-domain convention (proof 36–44; E1 8–12) | PASS |
| 2 | (D) δ-identities (46–49) | PASS |
| 3 | Z1 (55–59) | PASS |
| 4 | Z2 (61–68) | PASS |
| 5 | Corollaries (i)–(iv) (70–73) | PASS |
| 6 | TOP specialisation, λ-normalisation, (H) (79–92) | PASS, relative to HK1 item 3 (re-derived from HK1 LF153–169) |
| 7 | Lemma W (96–102) | PASS |
| 8 | BIG-RUN (106–114) | PASS |
| 9 | (AP) (118–120) | PASS |
| 10 | SIDE (122–126) | PASS |
| 11 | BALANCE (130–138) | PASS |
| 12 | TOP failed step (142–147) | PASS as a method record; FIX R-2 |
| 13 | LOW-CORE facts and failed step (151–157; E1 item 3; E2) | PASS |
| 14 | Diagonal facts and failed step (159–165; E1 item 2; E2; parent item 1) | PASS as a method record; FIX R-3 |
| 15 | Residual, table, first unproved lemma (169–185) | PASS |
| 16 | cp03 draft W statement (cp03 LF14) | FIX R-1 |

No REJECT.

## Verification record

**1. (G) in P-form.**
- All blocks are odd, so GRX's δ = #{f_i = 0} = k−Φ and C_max = 2H+Φ.
- Hence n = 2p−C is even and lies in [max(0, 2κ̂+2−Φ), min(R, 2p−Φ)], which is HK1 (G).
- T(P) = Σ_{i∈P} τ_i = Σ_{i∉P} θ_i, using Σθ = 0. An interval {j+1..j′} telescopes to y_{j′}−y_j.
- Erratum 1 sets m = Φ = 0 for both P = ∅ and P = all. This makes the complement identities hold for every P. No proof reads P = all with Φ ≠ 0.

**2. (D).**
- F = 3p−2−δ, R = p+δ, Pgap ≤ δ, and 0 ≤ δ ≤ 2κ̂−2.
- At δ = 0 every r_i ≤ 1 and Σr_i = p. So there are p singleton runs and 2κ̂ genuinely empty runs.

**3. Z1.**
- Since k > p, pigeonhole gives y_j = y_{j′} with j ≠ j′.
- P = {j+1..j′} has size in [1, k−1], so it is proper and nonempty. Φ = 2 and T = 0.
- The window is [2κ̂, min(R, 2p−2)].
- n = 2κ̂ needs 2κ̂ ≤ z0 ≤ R and 2κ̂ ≤ 2p−2; both hold. Signed zeros are zero in either zone.

**4. Z2.**
- If z0 ∈ [1, δ+1], there are at least p−1 nonzero letters.
- 2κ̂+2 ≤ p+1 < k change blocks are available. An even number of changes gives a consistent cyclic z.
- The window [0, min(p+δ, 2p−2κ̂−2)] contains every even n ≤ p−1.
- p−1 two-element sets {0, s_i} give all of Z_p by iterated Cauchy–Davenport.
- If |I| is odd then |I| ≤ p−2, and an unused zero letter exists to fix parity.
- I = ∅ gives n = 0 with C = 2p = C_max, which is admissible.
- Corollaries:
  - k = p+2 gives δ = 2κ̂−2, so [δ+2, 2κ̂−1] is empty.
  - Every LOW-CORE NF has κ̂ = 2 ≤ (p−1)/2.
  - On the diagonal with κ̂ ≥ (p+1)/2, Z1 is vacuous because 2κ̂−1 ≥ p = R. The table understates nothing.

**5. TOP setup and (H).**
- C_max = Φ, so n = 2p−Φ. k is odd, so m ≤ (p+1)/2 and n ∈ [p−1, 2p] ⊆ [0, R].
- (v,e) ↦ (λv, e) is an automorphism. It preserves letter order, blocks, the empty-gap rule and zero letters, and sends T ↦ λT and X^P ↦ λX^P. It is applied to u only.
- The HK1 item-3 import is re-checked:
  - The pair lemma at q = p−1 needs μ ≤ 2p−3.
  - The p−2 spare letters cover the at most p−3 fillers.
  - The heavy value is unique since 2(2p−2) > 3p−4, and its class is common across patterns.
  - The class is nonzero by the Φ2, T0 pattern at n = 2p−2.
- Signed ±1 multiplicities are exactly S_±, because a signed deviant (including value 0) is never ±1.
- With S_+ + S_− = 3p−4−D, (H) is equivalent to max(S_±) ≥ 2p−2.

**6. Lemma W.**
- For 2 ≤ Φ ≤ p+1: p−1 ≤ n ≤ 2p−2 ≤ S_+, and there are at most p−2 non-unit letters, so fewer than n.
- Every set V of non-unit letters completes with signed ones, and every n-selection splits this way. So Σ_n = n + Σ(W_P), and −n ≡ Φ.

**7. BIG-RUN.** Checked vertex by vertex.
- Growth phase: every X with {1,5} ⊆ X ⊆ all∖{2,6} has distinct complement pieces through 2 (inside [2,4]) and through 6 (inside [6,N]). So m ≥ 2.
- The complements of Xb..Xe are {1,2}∪{6}, {1}∪{6}, {1}∪{5,6} and {1}∪{5}. These pieces are separated whenever N ≥ 7, and here N = p+2 ≥ 9.
- The path is N−4 growth flips followed by four flips (−1, +2, −5, +6).
- Δ(X^c) = −Δ(X), and |Δ| ≥ p+D > 0 in the integers.
- Flipping run q changes Δ by ∓2g_q, so |g_q| ≥ p+D.

**8. (AP) and SIDE.**
- The all-plus pattern has n = 2p and T = 0.
  - A ≥ 2p would give 2p ones summing to zero.
  - A′ ≥ p, together with A ≥ p, would give p ones plus p minus-ones.
- If q ∉ P, then S_− ≤ A′+O ≤ 2p−4−2D < 2p−2. (H) then gives S_+ ≥ 2p−2 and S_− ≤ p−2−D.
- The q ∈ P case follows by complement. |W_P| = S_− + D ≤ p−2.

**9. BALANCE.**
- For every e ≤ D, S_± ≤ 2p−2−D ≤ n−e. So i ranges over [n−e−S_−, S_+], a run of N_e = p−1−D+e values, with N_e in [1, p−1].
- The signed sums form a step-2 progression of N_e < p distinct residues.
- With e = D, the only residue missed is μ.
- Dropping one deviant d (e = D−1), the residues missed are μ−d±1.
- Avoidance would need d ≡ ±1, which is impossible for a deviant, including d = 0.
- When D = 0, μ ≡ 2S_+ + 4 ≡ −2S_− − 4, which agrees with cp02 LF19.

**10. LOW-CORE.**
- For 6 ≤ Φ ≤ p−1 the window is every even n ≤ p+1, since R = p+2 is odd. So the window is exactly E(X^P).
- The Φ2 window is [4, p+1], so HK1's n = 2 step is unavailable.
- The pure skeleton window is [6, 2p]. ABCABC (length 6) stays forbidden; length-4 selections are only not forbidden.
- Both stated failure points are accurate.

**11. Diagonal.**
- Every Theorem P gap has floor(n_t/2) = 0, so M = 3p−3 = 3(p−1). That only matches the degree bound, and the box lemma needs strict inequality.
- The four listed single-letter rules are confirmed:
  - "select iff u_t" contributes −x·u_t.
  - "select iff 1−u_t" contributes (1−u_t)·x.
  - "never" contributes nothing.
  - "select iff e⊕u_t" contributes (e−u_t)·x and adds e+u_t to the size parity.
- Even with all p singletons, M = 4p−3 exceeds the degree bound. The obstruction is parity, as stated.

**12. Residual.**
- Every auxiliary statement is the contrapositive of an explicit (R2) violation on (R0) data. Adjoining them leaves the (R0)–(R3) set unchanged.
- No exclusion, feasibility claim or converse is made.

## Findings and minimal new errata

**R-1 — MINOR, required documentary (cp03 LF14).**
- Problem:
  - cp03 says "W-formulation valid with UNRESTRICTED subset sums whenever S_+≥2p−2 and Φ≤p+1". It omits Φ ≥ 2.
  - At Φ = 0 (n = 2p) with S_+ ∈ {2p−2, 2p−1}, every 2p-selection needs at least 2p−S_+ ≥ 1 non-unit letters. V = ∅ is unavailable, so Σ_{2p} = 2p + Σ(W_P) fails in general.
  - The parenthetical checks only the non-unit side.
  - The manuscript's Lemma W (proof LF96) already carries Φ ≥ 2.
- Erratum: *At cp03 LF14 read "whenever 2≤Φ≤p+1 and S_+≥2p−2 (so n=2p−Φ≤2p−2≤S_+ and the non-unit part is ≤p−2<n)". No lemma or use changes.*

**R-2 — MINOR, required documentary (proof LF143).**
- Problem:
  - "|Σ(W_P)|≥|W_P|+1≤p−1, so no single pattern forces an identity" chains inequalities in mixed directions.
  - It also reads as an absolute claim. For given data, a single pattern does give an identity whenever T(P)+2m(P) ∈ Σ(W_P).
- Erratum: *Read "Cauchy–Davenport guarantees only |Σ(W_P)| ≥ |W_P|+1, and |W_P|+1 ≤ p−1. So this size bound alone does not force T(P)+2m(P) ∈ Σ(W_P) for any single pattern. Nothing is asserted about whether an actual configuration avoids a pattern."*

**R-3 — MINOR, required documentary.**
- Locations: proof LF164–165, E1 LF17–18, parent erratum LF5 (item 1, second sentence), cp01 LF23–24, package v2 LF25.
- Problem: the "attempted cross-gap encoding" is never written down, yet parent item 1 asserts a guaranteed degree-≤2 bound for it.
- That bound holds for the plain-mark rule: for x in gap t and x′ in gap t′≠t, select both iff m_π.
  - V gains m_π((1−2u_t)x + (1−2u_{t′})x′).
  - Z gains 2m_π, so parity, injectivity and the zero point are kept.
  - deg Q ≤ 4(p−1), and M = (7p−7)/2 ≤ 4(p−1).
- The bound fails for a Theorem-P-style rule "select iff m_π⊕u_t": the multilinear form of V then contains 4x′u_{t′}m_πu_t, which is degree 3 when x′ ≠ 0.
- The method fails under either rule, so nothing load-bearing is affected.
- Erratum: *The attempted encoding is the plain-mark rule (worker to confirm). For it, deg V ≤ 2, deg Q ≤ 4(p−1) and M = (7p−7)/2 < 4p−3. If an XOR-with-u_t rule was used instead, read "degree ≤ 3", which also fails. No classification and no no-go theorem.*

**O-1 — MINOR, optional (proof LF6–8, package v2 LF20, cp03 LF16–17).**
- Problem:
  - "Because GRX is exact … unchanged", "GRX is exact, so the residual set is unchanged" and "GRX is an IFF, so …" give the wrong reason.
  - The real reason is that each auxiliary statement is a formal consequence of (R0)+(R2). Exactness and the converse direction are unused and promote nothing.
  - "Data subclasses of HIGH-K-RES" should read "data subclasses of the (R0)–(R1) data space, which meet HIGH-K-RES trivially".

**O-2 — MINOR, optional (proof LF29–30, coverage LF45).**
- Theorem P also enters through (R0)'s displayed bound k ≤ p+2κ̂ (δ ≥ 0, R ≥ p), used at LF46–47 and in Z2 at LF62/65.
- This is the scalar consequence of the same accepted P-fail inequality, not a new use. Suggested reading: "through HK1's (R0) k-range and (R1) gap floor".

**O-3 — MINOR, optional (notation).** Suggested renames: δ_P, A_±, N_runs.
- δ := p+2κ̂−k (LF46) collides with GRX's δ (notes-GRX LF14).
- A, A′ are counts at LF88, but A, B, C are reflection values at LF155.
- N is the run count at LF107, but word length in Theorem P; N_e at LF134 is a progression length.

**O-4 — MINOR, optional (cp01 LF22–24, cp03 LF20–21).**
- These lines repeat the unqualified phrases: "keeps V linear only with…", "makes V quadratic", "make Z cubic", "pure length-4 identities are permitted".
- Read them under E1 items 2–3 and parent item 1. E1 item 3 formally targets LF155 and the package, not cp03.

## Errata re-check

**Worker errata**
- **E1 item 1:** correct. T(all) = 0 = −T(∅), and all-minus is the global flip with the same window.
- **E1 item 2:** correct for the listed family of rules.
- **E1 item 3:** correct; the skeleton window is [6, 2p].
- **E2:** correct. The LOW sentence is at LF155, inside LF154–157, and the diagonal sentence starts at LF162.

**Parent erratum**
- **Item 1, first sentence:** correct. It targets LF164 and E1 LF17; the diagonal has 2κ̂ empty runs plus all internal zero gaps.
- **Item 1, second sentence:** see R-3.
- **Item 2:** correct. The path is N−4 growth flips plus four flips, and cp04 LF13's "five-step path" is also covered.
- **Item 3:** correct. The "16" is at ack LF54 (LF65 is the RS-based Φ2 exposure line), and scope LF34–125 holds 15 entries (counted).

None of these errata adds a lemma, premise or residual change.

## Source gate and missing-body list

- **Pasted whole:**
  - the new proof, both errata (in both parts), scope, acknowledgement, cp01–05, and all 15 governing inputs;
  - notes-GRX and lowodd v2 (M1–M7 inline), the fewodd addendum and the zx-s1c verdict;
  - separately: package, manifest, coverage, cp06 and the parent erratum.
- **Pasted partially:** few-E v4, LF28–43 only.

Referenced but unpasted bodies. I checked each and found none load-bearing for any new lemma:

1. **NF and GRX sources.**
   - Bodies: few-E v4 LF1–27 and LF44–331; olson-fewodd-parent-verdict-v1 (the base that the addendum extends); proof-ROT-lowodd-v1 (PM*, K1/K2); proof-dihedral-partial Sec.0; GR/GR0.
   - Why not load-bearing: the new lemmas are implications inside (R0)+(R2), and NF enters only through accepted HK1 item 4. The group law is restated in lowodd v2 item 1/M2 and in Theorem P LF10–11, and the GRX proof is self-contained.
2. **CT and S(p).**
   - Bodies: lane CT/STAB-δ item 6/RS(a); the S(p) sources.
   - Why not load-bearing: no new lemma uses them. (R3) and the κ̂ ≥ 2 boundary are inherited unchanged.
3. **Process and verification artifacts.**
   - Bodies: HK1 parent check, review notes and receipts; HK1 cp03–08; the 330026-byte locator input; the HK1 base scope, addendum 1 and acknowledgements; ASSEMBLY-LS/P; UPAR5 verdict/erratum v1; ZX/S1(c); the Theorem P parent check and notes; GRX controls; v1 package Sec.3 (incorporated by reference at package v2 LF46–47).
   - Why not load-bearing: these are process or verification artifacts, or statements the new lemmas do not use.

**Process observation (not a finding):**
- The manuscript has no embedded clock. Its creation is bounded only by the cp03 (17:07:22) and cp04 (17:13:43) records.
- Checkpoint gaps were 740, 753, 889, 381, 272 and 100 s, all within target.
- "All by hand" is a self-report.

## Boundaries retained

- Z1, Z2, W, BIG-RUN, AP, SIDE and BALANCE remain CANDIDATE. This return is one family's input, not acceptance.
- HIGH-K-CORE-COVER is NOT_PROVED, all three uniform diagnostics are NOT excluded, and full (R0)–(R3) is unchanged.
- No claims are made of:
  - a parameter-family exclusion, feasibility, a converse or an exact classification;
  - full terminal k ≥ p+2 exclusion, or lower-terminal/original-o_F > p assembly;
  - full ordered Olson or p = 5.
- S(p) and CT are not premises of any new lemma; their trust is inherited only. There is no Lev, p+1 lift or rigidity transfer.
- No novelty, priority, independent-discovery or preregistration claim. No human, Lean/formal or runtime certification. Permanent process history remains uncured.
