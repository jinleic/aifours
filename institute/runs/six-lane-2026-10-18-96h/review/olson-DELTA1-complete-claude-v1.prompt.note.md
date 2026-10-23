# DELTA1-PAIR-COVER: hostile written review

**Verdict: FATAL 0, MAJOR 0, MINOR 6. Source gate: PASS.**

Every new mathematical claim (GW, D1-UE, D1-MP, D1-MM and the full union) holds at full target scope. All six MINORs are documentary or credit-attribution issues. None changes a formula, case, range or conclusion. This is a review recommendation, not acceptance; the parent hand check is still pending.

**Method.** I reasoned by hand from the pasted text only. I used no tools, code, enumeration or delegation. SHA256 values, byte counts and LF counts are supplied labels; I did not verify them. Citations use the original LF numbers.

**Abbreviations:**
- **UEMP**: proof-DELTA1-UE-MP-v1
- **MM**: proof-DELTA1-MM-and-full-cover-v1
- **E1D**: erratum-1-DELTA1
- **HO**: handoff; **COV**: coverage JSON
- **FND**: REFLHI v5; **E2 / E5**: its errata 2 and 5
- **K0S**: K0star-r2; **P, Pe2**: Theorem P proof and its erratum v2
- **V5V**: REFLHI v5 verdict; **SECC**: foundation review §C
- **D1EV / D1E1**: D1-END verdict / erratum v1; **CPnn**: checkpoints

## 1. Foundation chain, re-derived from the supplied bodies

I did not rely on prior reviews or approvals for any of these.

- **GRX (GRX:18-42).**
  - Inside a block, the zone sign contributes z_i·y_i when c_i is odd and 0 when even.
  - Summation by parts gives V = σ − T(z).
  - The realisable C are the even values in [Φ, C_max]. Verified.
- **GR0 → H0 (K0S:40-65).**
  - GR0 defers its Ach-window algebra to proof-GR.md §2, which is not supplied (K0S:52-53). I re-derived it.
  - Take even n = 2p − C. Then Σ_n is the set of even t in [max(−n, n−2E−), min(n, 2E+−n)].
  - Consecutive n give even intervals that overlap or touch. Their union is 2Z ∩ [max(−s1, s0−2E−, −E−), min(s1, 2E+−s0, E+)].
  - With β = 0: δ = o_F − 2m, so C_max/2 = H + m.
  - Therefore ⌊hi/2⌋ = min(p−m, E+−κ+m−1, ⌊E+/2⌋) = γ_m(E+(P)). This gives Lemma W (FND:42-44).
- **L2.1 (FND:56-59).**
  - D_P is the sum of d_t over IN-gap runs, because runs internal to arcs are empty.
  - So E+(P) = E+ for every endpoint choice (a_i, b_i), and u_P telescopes.
- **L3.1 (FND:97-98).** E+ = B + (D ± T)/2 = (R ± T)/2.
- **BAL with I.6 (FND:103-106, E5:69-72).** Verified.
- **Realisation rule e5 with I.7 (E2:6-11, E5:74-78).** Any applicable move changes c_j by ±1 and keeps the choice made of singletons and pairs.
- **Theorem P (P:27-93, both errata).**
  - M ≥ 3p−2 > 3(p−1) ≥ deg Q, and the box cancellation holds.
  - |S| is even, at most 4p−1 and divisible by p, so |S| = 2p.
  - Original index order follows from Pe2:5.
  - This gives P0 (K0S:73-75): F + Σ⌊r_i/2⌋ ≤ 3p−2, equivalently R + o_R ≥ 2p.
- **Normalisation and order.** (v,ε) ↦ (c⁻¹v, ε) is an automorphism. Cyclic selection gives increasing original order by conjugation (GRX:41-42, Pe2:5).
- **Cauchy–Davenport (FND:27).** Classical. It is the only trusted item at the foundation layer.

## 2. Per-claim verdicts

| # | Claim | Verdict |
|---|---|---|
| C1 | Step-0 baseline audit (CP01:13-29, HO:25-35) | PASS |
| C2 | A1–A4 (UEMP:36-55) | PASS |
| C3 | Lemma GW and its s-form (UEMP:57-74) | PASS |
| C4 | D1-UE (UEMP:30-31, 76-106) | PASS |
| C5 | D1-MP (UEMP:32, 108-132) | PASS |
| C6 | UEMP §5 failure remark (UEMP:134-141) | FIX (M1) |
| C7 | UEMP §6 residual (UEMP:143-160) | PASS as a historical statement; superseded by MM |
| C8 | MM §1 windows (MM:40-55) | PASS |
| C9 | MM §2 BAL reserve and all-odd tight cases (MM:57-84) | PASS |
| C10 | MM §3: framework, DP1, DP2, tight Q0/Q+ (MM:86-123) | PASS |
| C11 | MM §4 all-flexible case (MM:125-140) | PASS |
| C12 | MM §5 exhaustion; D1-MM for every p≥7 (MM:142-156) | PASS |
| C13 | Full union (MM:15-17, 158-166; HO:46-55) | Mathematics PASS; attribution FIX (M2) |
| C14 | E1D status overlay | FIX (M3) |
| C15 | Handoff, manifest and coverage metadata | FIX (M4–M6) |

## 3. Checks of the named risks

**A1–A4.**
- P0 with e_F = 0 gives o_R ≥ p−1.
- Parity of p+1 together with an excess of 0 or 2 gives exactly three types: Q+, Q0, Q−.
- o_M ≡ k (mod 2). T ≡ Σr ≡ 0 (mod 2).
- BAL then gives |T| ≤ d ≤ 3, so |T| ≤ 2 since T is even. In Q+, d = 1 so T = 0.

**GW: window orientation and the sign of T.**
- By L2.1 the window I(P) is a single interval, independent of the endpoints chosen.
- By L3.1, {E+(P), E−(P)} = {(R±T)/2}. So |I| = Γ+1 regardless of orientation or the sign of T.
- 0 ∈ I by the hypotheses γ ≥ 0.
- The u-set is a sumset of 2m nonempty sets. Pair values are distinct because the inner empty run is genuine (K0S:25). CD gives at least min(p, G+1) residues.
- (Γ+1) + (G+1) ≥ p+1, so the window and the u-set meet.
- The run right after an arc lies in the gap, never inside the next arc. An OUT gap contains a run, so P is proper with exactly m intervals.
- The substitution E−κ+m−1 = E+H−s is correct.

**D1-UE.**
- Step 1 values:
  - p = 4a+1, s0 = a: Γ = a+a at T = 0 and at |T| = 2.
  - p = 4a+3, s0 = a+1: Γ = 2a+2 at T = 0 and (a+1)+a at |T| = 2.
  - So Γ ≥ (p−1)/2 for every H ≥ 0, and GW needs G ≥ G0−1.
- Type A needs c ≥ G0+1 and G0+2m0 ≤ k−1.
  - For p ≥ 11 this follows from c ≥ p−4 and 2p+1 ≤ 3p−8.
  - For p = 7 it holds when H ≤ 1, since k−1 = 17−2H ≥ 14.
  - The case p = 7, H = 1, c ≥ 5 also falls under type A (14 ≤ 15).
- Type B, (p, H, c) = (7, 1, 4):
  - o_M = 8 = q, so the word is Q+ with every run odd, and some M_l has at least 3 blocks.
  - Pair count: 1 + (|M_l|−3)/2 + Σ_{i≠l}⌊|M_i|/2⌋ = 4. The 5 extra singletons fit on 7 free blocks.
  - In Q+, T = 0 and Γ = 4, so there is slack.
- Loss accounting at fixed arc count:
  - If the move at i′ is +1 (an add or a split), the move at l deletes the designated singleton.
  - If the move at i′ is −1 (a deletion), the move at l adds on the reserved block (type A) or splits the designated pair (type B).
  - So at most ONE pair is lost in every combination. Since i′ ≠ l, the two moves never interfere.
- The excluded cell (7, H=2) is (7, κ=4), which D1-MP covers.

**D1-MP.**
- Window ranges:
  - p = 4a+1: Γ ≥ 2a on [a, 3a] for T ∈ {0, ±2}. At s = 3a with |T| = 2 the values are (a+1, a−1).
  - p = 4a+3: Γ = 2a+2 (T = 0) or 2a+1 (|T| = 2) on [a+1, 3a+1].
- Capacity:
  - In Q0 and Q−, o_M is even and at most p, so o_M ≤ p−1 and c ≥ (p+1)/2.
  - In the tight Q+ case c = (p−1)/2, every run is odd, so every M_i keeps one free block.
  - Block budget: G0 ≤ 2s0.
- Moves:
  - The move at i is never a split.
  - The move at i′ splits only if M_{i′} has no free block, which never happens in tight Q+.
  - So Δ ∈ {−2, 0, 2} and s′ ∈ {s0−1, s0, s0+1}, which lies in the range for a ≥ 1.
- The p = 7 line (s′ ∈ {2,3,4}, 12 ≤ 14 blocks) checks out.

**MM §1.** I checked every displayed minimum on the full intervals:
- p = 4a+1, H = 2a, |T| = 2: (a+1, a) on [a+1, 3a]; (a, a) at s = a; (a+1, a−1) at s = 3a+1.
- p = 4a+3, H = 2a+1, |T| = 2: (a+1, a) on [a+1, 3a+2].
- In both classes T = 0 gives a or a+1 respectively. All γ ≥ 0.

**MM §2.**
- Capacity: Q+ gives c ≥ (p−3)/2; Q0 and Q− give c ≥ (p−1)/2.
- Block budget: 2m0+G0 ≤ k holds iff G0 ≤ 2a+2.
- Edge case: p = 4a+3 in Q0 or Q− with G0 = 2a+2 uses all 8a+4 blocks, leaving no unused block. The move at i is then a deletion. The move at i′ is a deletion or a split, so Δ ∈ {−2, 0} and at most one pair is lost. The text covers this.
- All-odd tight cases: o_M = q is forced (4a+4, 4a+2, 4a). Singleton demand fits the free blocks (4a+2 ≤ 4a+4; 4a+1 ≤ 4a+2; 4a−2 ≤ 4a). No pair is lost.

**DP1.**
- In tight Q0, q = p and o_M = p−1, so there is exactly ONE rigid edge.
- If the two-letter run is an endpoint of that edge: f is odd with |f| ≤ 3, and the p−2 free signs reach every odd target.
- Otherwise: |f+g| ≤ 4 and even, and the p−3 free signs (an even count) reach every even target. At p = 7 this is tight (4 free signs, |f+g| = 4 reachable). d_r = 0 is also handled.
- Windows:
  - (4a+1, c = 2a): s ∈ [a+1, 3a+1], Γ = 2a, G = 2a.
  - (4a+3, c = 2a+1): x is odd and ≤ 4a+1, s ∈ [a+2, 3a+2], Γ = 2a+2, G = 2a+1 (one unit of slack).

**DP2.**
- q ≥ 14, so two rigid edges cannot close a 2-cycle. The endpoint set K is a 3-vertex path or two disjoint edges, so the constraints are consistent.
- f ≡ |K| ≡ q−|K| (mod 2), with |f| ≤ 4 ≤ 10 ≤ q−|K|.
- For p ≡ 3 (mod 4), c = 2a forces all runs odd, and c ≥ 2a+1 is handled by BAL. So DP2 is not needed there.

**MM §4.**
- c = 2a−1 forces o_M = 4a+2 = q, so every edge is flexible. Choose 2a+2 plus signs and 2a minus signs, giving T = 2.
- x must avoid 1. With x = 1 we get s = 3a+1, where Γ(±2) = (a+1)+(a−1), and the total would be 4a−1.
- Fix: flip one +1 vertex and a non-adjacent −1 vertex (there are 2a ≥ 6 candidates and at most 2 neighbours). T is unchanged.
- The two vertices have 4 distinct incident edges, so D changes by a 4-set and |D| becomes 3 or 5.
- Then s ∈ [a+1, 3a], Γ = 2a+1 and G = 2a−1, so Γ+G = 4a = p−1.

**Exhaustion (MM §5): complete.**

| Class | Q | Lowest c | c value → handler |
|---|---|---|---|
| 4a+1 | Q+ | 2a−1 | 2a−1 → §4; 2a → DP2; ≥2a+1 → BAL with G0 = 2a+1 |
| 4a+1 | Q0 | 2a | 2a → DP1; ≥2a+1 → BAL |
| 4a+1 | Q− | 2a | 2a → all-odd; ≥2a+1 → BAL |
| 4a+3 | Q+ | 2a | 2a → all-odd; ≥2a+1 → BAL |
| 4a+3 | Q0 | 2a+1 | 2a+1 → DP1; ≥2a+2 → BAL with G0 = 2a+2 |
| 4a+3 | Q− | 2a+1 | 2a+1 → all-odd; ≥2a+2 → BAL |

**Union.**
- For p ≥ 11 the pieces [2,(p−5)/2], (p−3)/2, (p−1)/2, (p+1)/2, [(p+3)/2, p−4], {p−3, p−2, p−1} are consecutive and partition [2, p−1].
- Small primes:
  - p = 11: {2,3} | 4 | 5 | 6 | 7 | 8–10
  - p = 13: 2–4 | 5 | 6 | 7 | 8–9 | 10–12
  - p = 17: 2–6 | 7 | 8 | 9 | 10–13 | 14–16
  - p = 7: κ = 2 → D1-END; 3 → MM; 4 → MP; 5, 6 → UE.
- The K2P+ band at δ = 1 is exact: k ≥ 2p+1 iff κ ≥ (p+3)/2, and k ≥ 3κ+3 iff κ ≤ p−4.
- B-prime is not load-bearing for the cover, because D1-MM covers (p−1)/2 at every p ≥ 7. The SEG-num band is contained in RP-2NE's band.
- Erratum-5 Part II is unused: R = p+1 gives Π_need = (p−1)/2 > 0, GW never calls Theorem SEG, and K2P+ does not use it either (E5:27-28).

## 4. Findings and minimal errata

- **M1 (UEMP:136-138; E1D:26-28).**
  - The text says "Gamma(s,0)<=2floor(e/2)=2a … the pair-only route of Lemma GW is one short."
  - That is true only at T = 0. At |T| = 2, Γ = 2a+1 on [a+1, 3a] (MM:45), and MM:127-139 closes exactly this capacity case with pairs and singletons.
  - E1D:27 calls this section "a correct historical statement" without qualification. It is not load-bearing.
  - Erratum: read UEMP:137-138 as "…so at T=0, the only value this BAL construction reaches in (Q+), Gamma+G<=4a-1; |T|=2 is not excluded (MM Sec.4)". Read E1D:27 as "correct when so qualified".
- **M2 (MM:158-161, HO:47-48 vs MM:155-156, HO:44).**
  - The provider list names "new D1-MM" for {(p−1)/2} at every p ≥ 11.
  - Erratum: "B-prime (ε=0) for p≥19, where D1-MM is an uncredited duplicate; new D1-MM for p∈{7,11,13,17}". This affects credit only.
- **M3 (E1D:14; CP02:8).**
  - The citation "V5V LF9-20,28-29,51-52" is off. V5V:28 and V5V:51 are blank, and V5V:29 is the Foundations bullet, not Part II.
  - The Part II evidence is at V5V:10-13, 22, 30, 49 and 52.
  - CP02:8 repeats "Part II is single-family and NOT used". E1D item 1 is scoped to UEMP Sec.7 only (E1D:11).
  - Erratum: correct the citation, and extend item 1 to cover CP02:8.
- **M4 (HO:89-90; COV:664).**
  - These assert a "literal x=0 ambient typo" in SECC:104-127.
  - As supplied, SECC:109 reads "x ≠ 0", and no line in that range has x = 0.
  - Either the metadata is wrong or the bytes differ from the rendering. The parent's byte reconstruction must decide.
  - No premise is affected (V5V:27 and FND:39 govern). Erratum: delete the claim, or cite the actual bytes.
- **M5 (D1EV:3; SCOPE:53-57).**
  - D1EV:3 names `olson-D1END-parent-disposition-v1.json` (c774c0bc…) as D1-END's "bindings".
  - That file is neither supplied nor listed in COV:617-653.
  - It is not load-bearing. D1EV:5 and D1E1:10 ("Scope confirmed: … kappa=(p-3)/2, ANY B") fix the statement, and D1E1:3 says all four MINORs were wording only.
  - Erratum: add the file to COV's not-pasted list with that reason.
- **M6 (K0S:44, 52-53; HO:91).**
  - GR0 defers its window computation to proof-GR.md §2. That file is neither supplied nor listed.
  - It is not load-bearing: the supplied, accepted GRX plus the derivation in §1 close the step.
  - Erratum: add a note in COV.

## 5. Source gate: PASS

- **Completeness.** Every direct input to the new proofs is supplied literally and was re-derived in §1.
- **Four-piece completeness.** All four pieces are present: the scope (192 LF), the acknowledgement with cp01–06, UEMP (171 LF) and MM (176 LF).
- **Status erratum.** The E1D text is identical in both physical parts.
- **Omitted bodies.** These fall into two groups, and neither is load-bearing:
  - Bodies declared accepted-statement only: the internals of RP-2NE and D1-END, and K2P+ in FND §5. Their own verdicts and overlays are supplied.
  - Bodies not needed by this result: the B/B′/SEG-k/TRANSFER internals, erratum-5 Part II, and the two references in M5–M6.

No both-family re-review is triggered.

## 6. Accepted-import trust (exact)

The union depends on exactly three accepted statements whose proofs I did not replay, plus Cauchy–Davenport:

- **T1. RP-2NE** (RP2V:8-10) at δ = 1: κ ∈ [2, (p−5)/2].
- **T2. D1-END** (D1EV:5; D1E1:10): κ = (p−3)/2, p ≥ 7, any B.
- **T3. I.14 K2P+ band** (V5V:40; SECC:124; E5:155-156) at δ = 1: κ ∈ [(p+3)/2, p−4], nonempty only for p ≥ 11.

Not relied on for this result: B-prime/N(p,1), SEG-num, E, SEG-k, TRANSFER, B.4, CJ/EDGE, Facts 2.1 and 2.2 (A1 uses P0 directly), Part II, CONNECT/LIGHT, and FP/FP-1.

## 7. Nonclaims

- No acceptance and no Lean or kernel check.
- No hash, byte or LF verification.
- No replay of the internals of T1–T3.
- No claim about existence of avoiders or realizability.
- Nothing claimed for p = 5, for R ≠ p+1, or for even blocks.
- Nothing claimed for arbitrary words or NFs, REFL, INV*, full ordered Olson, novelty or priority.
- No independent-corroboration claim for D1-MM duplicating B-prime at p ≥ 19.
- I did not audit process or timestamp compliance.
