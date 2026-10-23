**Counts: FATAL 0 · MAJOR 0 · MINOR 4.** All four MINORs concern provenance, wording or precision. None changes a formula, a case or the conclusion.

**Disposition (this corollary only).** The corollary is mathematically correct relative to two inputs:
- Theorem P at its literal statement (P LF10, LF17, LF27).
- The NF bookkeeping (NF LF37, LF42).

The frontier change still depends on ERR LF9's review process. This review does not approve full ordered Olson, the research target, or any novelty, Lean, human-referee or runtime claim.

Aliases: COR = corollary v1, ERR = erratum v1, P = proof-theoremP, K0R = K0*/RED verdict, K1V/K2V/K3V/USKV = the four verdicts, ROTKP = ROT-KP verdict.

### Independent re-derivation

Setup: w is a length-(4p−2) avoider over D_2p, with p an odd prime. ŵ is an admissible NF of w with terminal k=p+1 odd blocks and κ̂=0.

1. **(i) Arithmetic.**
   - NF LF42 gives H=(F−k)/2 and κ=p−1−H, so F=k+2(p−1−κ̂)=(p+1)+2(p−1)=3p−1.
   - NF LF42 also gives R=2p+2κ̂−k=p−1, and F+R=4p−2 as required.
   - LOWER LF44 gives the same values (F=3p−1−2κ, R=p−1+2κ).
2. **(ii) The normalized word.** By NF LF37 (and LOWER LF42), ŵ is an avoider of length 4p−2 with w's rotation multiset. F=3p−1≥1.
3. **(ii) Theorem P's literal hypotheses all hold.**
   - p is an odd prime (P LF10) and F≥1 (P LF17).
   - N=4p−2≤4p−1 (P LF27).
   - F+Σ⌊n_t/2⌋≥F=3p−1, because every n_t≥0 (P LF21–23).
   - So ŵ has an identity 2p-subword, which contradicts step 2.
   - Two presentation details are harmless. The cyclic presentation is fine by P LF14–15. The σ_y/ρ_x vs (v,e) coordinates are fine because P's hypothesis depends only on the R/F pattern (P LF100), and identity-subword existence survives any isomorphism (the rotations are the unique order-p subgroup).
4. **(iii) Route via LOWER (S1).**
   - By LOWER LF54, ŵ's gaps are F−N empty gaps inside blocks plus the N=p+1 run gaps, so Σ⌊n_t/2⌋=Σ⌊r_i/2⌋.
   - (S1) at LF56 then gives Σ⌊r_i/2⌋≤2κ−1=−1, which is impossible.
   - LF57 gives the same contradiction another way: it requires ≥p+1 odd runs, but there are only R=p−1 letters.
   - This route is correct, but it is the contrapositive of the same Theorem P instance as step 3.

### Claim-wise verdicts

| # | Claim | Source | Verdict |
|---|---|---|---|
| C1 | Corollary statement | COR LF5 | CORRECT relative to P + NF. "NF is available" is unresolved (m4). |
| C2 | H=p−1, F=3p−1, R=p−1 | COR LF7; ERR LF5 ← NF LF42, LOWER LF44 | CORRECT |
| C3 | NF word is a length-(4p−2) avoider with F≥1 | COR LF7; ERR LF6 ← NF LF32, LF37–39 | CORRECT. LF32 is about w and transfers via LF37; F≥1 is automatic here. |
| C4 | Theorem P paraphrase and application | COR LF7 ← P LF10, LF17–27 | CORRECT. The paraphrase is faithful and there is no misapplication. |
| C5 | No run-shape, rotation-pair or placement hypothesis needed | COR LF7 | CORRECT. It also needs no empty-run rule, no p≥11, and no letter values. |
| C6 | P is accepted and used at the same threshold in LOWER | COR LF9 ← K0R LF7, LOWER LF55/LF193, K1V LF5 | CORRECT as a record. The pointer is secondary (m1). |
| C7 | "Second, already-accepted route" | ERR LF6 ← LOWER LF52–56, K1V LF5 | The mathematics is CORRECT. "Second" and "accepted at κ̂=0" are unsupported (m2). |
| C8 | Scope is terminal k=p+1 only; ROT-KP is a structure result | ERR LF7 ← ROTKP LF17 | CORRECT. The route provably cannot reach k≤p (note 4). |
| C9 | Frontier correction | COR LF11; ERR LF7, LF9 ← K1V LF9, K2V LF11, K3V LF13, USKV LF13 | Scope is CORRECT and not overstated once the erratum is applied. Quotation and p-coverage need fixes (m3, m4). |
| C10 | Does not supersede nonterminal κ=0 or the K0*/REFL residual | COR LF11 ← K0R LF7–8, LF43 | CORRECT. REFL-RES concerns κ≥2; K0* is a structure theorem. |
| C11 | No new execution, aid or novelty | COR LF3, LF9; ERR LF9 | CONSISTENT. Nothing computational is relied on. |

### Findings

**m1. The Theorem P acceptance pointer is secondary and silent on scope** (provenance/process; not correctness)
- **Step:** COR LF9 cites K0R LF7. That line accepts K0* (a p≥5 result) and lists "Theorem P (accepted)" as one of K0*'s imports. It is not P's acceptance act and gives no scope for P. The pinned P text still says "NOT yet independently reviewed" (P LF3–5).
- **Consequence:** A consumer cannot read P's accepted scope from the cited line. Correctness is unaffected: the corollary uses only P's literal LF27 statement, and LOWER LF55 (accepted under K1V LF5) already relies on P at the identical threshold. If P's primary acceptance carried a p-restriction (none is visible), the corollary would inherit it.
- **Repair:** Cite P's primary acceptance record, or reword to "recorded as accepted (K0R LF7) and relied on at this threshold in LOWER LF55 under K1V LF5".

**m2. "Second, already-accepted route" is overstated** (provenance/wording; not correctness)
- **Step (a), not independent:** (S1) is the contrapositive of the same Theorem P instance, on the same word with the same F and the same gap sum (LOWER LF54–56).
- **Step (b), acceptance at κ̂=0 is not shown:**
  - K1V LF5 accepts "Theorem S *structure*". ERR drops the word "structure".
  - Theorem S's statement and its κ- and p-range are not pasted; LOWER LF183 only names it.
  - The K1 theorem is for p≥11.
  - K1V LF9 lists κ_hat=0 as open in the same verdict.
  - The LOWER parent erratum v1 is not pasted.
- **Consequence:** None for correctness, because (S1) at κ=0 re-derives directly from LF44 and LF54–56. However, counting "two accepted routes" overstates robustness. Route 1 is the only load-bearing argument.
- **Repair:** Reword to "Equivalent restatement: (S1) at κ=0 reads Σ⌊r_i/2⌋≤−1. This is the same P instance; no claim that Theorem S's acceptance covers κ̂=0."

**m3. Frontier-correction quotation and tense** (process/wording; not correctness)
- **Step (a):** K1V LF9, K3V LF13 and USKV LF13 do say "Open". K2V LF11 says only "not settled here". That statement is true of K2 and stays true, so it was neither "called open" nor "superseded".
- **Step (b):** COR LF11's "already excluded" asserts a frontier change for a claim that had not been reviewed. ERR LF7 ("once independently reviewed") and ERR LF9 repair this; with the erratum applied, it is not overstated.
- **Step (c):** "Overly conservative" is fair as mathematics, since all inputs are recorded accepted before K1V. Still, those lines were accurate statements of the recorded frontier, not errors.
- **Consequence:** A reader of COR alone could think the frontier had already changed, or that K2V was being contradicted.
- **Repair:** Quote each line verbatim. Mark K2V LF11 as unaffected. Make supersession of K1V LF9, K3V LF13 and USKV LF13 conditional on parent acceptance.

**m4. The p-range is unresolved and the p=7 sub-cell is not recorded** (completeness/precision; not correctness)
- **Step:** COR LF5 says "for which the stated NF is available", but NF LF28–43 states no p-range. ROTKP LF15–17 does invoke admissible NFs for every p≥5. So the exclusion likely also covers the κ̂=0 terminal sub-cell at p=7. Yet the four verdicts list an undivided "p=7 lower half", and COR LF11 says all other statements "remain unchanged".
- **Consequence:** Nothing stated is false; the p=7 lower half stays open for κ̂≥1. But the corollary's real p-coverage is invisible to consumers.
- **Repair:** State the NF's accepted p-range intersected with the odd primes. Add: "At p=7 and any other p<11 in that range, the terminal κ̂=0 sub-cell is excluded; κ̂≥1 there is unchanged."

### Notes (not findings)

1. **κ̂ is used but never defined in COR or ERR.** The identification with NF LF42's κ is still forced by the pasted text:
   - ROTKP LF25: m≥2p−(2H+2)=2κ̂.
   - LOWER LF43–44.
   - K1V LF5's range 0≤κ̂≤p−1.
   - K0*'s block-κ (K0R LF7) gives the same value on ŵ, because NF blocks are maximal (LOWER LF36–37) and odd.
2. **Optional hardening.** The proof does not need NF's preservation of avoidance.
   - F(ŵ)=F(w) by NF LF37, since length and rotation multiset are unchanged.
   - Applying P to w itself gives F(w)≤3p−2 for every length-(4p−2) avoider.
   - At k=p+1 this forces 3p−1−2κ̂≤3p−2, so κ̂≥1.
3. **Cross-check independent of Theorem P** (conditional, not load-bearing).
   - Apply (SR) (LOWER LF47) at κ=0 with P={a+1..b}, a≠b, and m(P)=1. The range allows n=0, so T(P)=y_b−y_a≠0.
   - Then y_0..y_p are p+1 distinct elements of Z_p, which is impossible.
   - This is the ROTKP LF25/LF28 ARC mechanism (zero rotation letters). It rests on (SR), whose acceptance at κ̂=0 is not shown in the paste.
4. **The scope boundaries are genuine.**
   - At k≤p with κ̂=0, F=k+2p−2≤3p−2. P would then need Σ⌊r_i/2⌋≥p+1−k, which is not automatic, and the pigeonhole argument has room. So the route cannot reach k≤p.
   - The same argument would exclude κ̂=0 at any terminal k≥p+1, so restricting the claim to k=p+1 is conservative.
   - Nothing pasted equates κ̂ with K0*'s κ(w), so leaving "nonterminal κ=0" open is correct.
5. **Errata applied.** ERR is applied throughout; it repairs COR LF11 and is the source of m2. The LOWER, K2 and K3/USK parent errata are referenced but not pasted, and none of them bears on route 1.

### Category separation
- **Correctness:** no defect.
- **Completeness:** m4.
- **Process/provenance:** m1, m2, m3.
- **Priority/novelty:** none claimed; none assessed.
- **Computation:** none relied on. P LF3–4 brute force and K0R LF23–28 aids are not premises here.
