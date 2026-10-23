# Hostile review: ASSEMBLY-P v2 `059033b0`, with parent erratum v1 `d6fe328f` applied last

I worked only from the supplied text and did not verify any hashes. I treated [ONE-SHORT-LS] and [ROT-SING] as conditions only, not as imports. I did not use any prior review as a premise.

## 1. Per-claim verdicts

| Claim | Verdict |
|---|---|
| Theorem ASSEMBLY-P (A), conditional on [ONE-SHORT-LS] and [ROT-SING] | **ACCEPT-WITH-FIXES**: MINOR-1 trust label only; no mathematical change |
| Theorem ASSEMBLY-P (B), same conditions | **ACCEPT-WITH-FIXES**: MINOR-1 |
| Proposition ROT-P, conditional by cell | **ACCEPT-WITH-FIXES**: MINOR-1 |
| Proposition DEP, including U(7) = ∅ and U(p) ≠ ∅ for p ≥ 11 | **ACCEPT** (see MINOR-2a for its trust row) |
| Corollary ASSEMBLY-P0 (A0), no pending premise | **ACCEPT-WITH-FIXES**: MINOR-1 |
| Corollary ASSEMBLY-P0 (B0), no pending premise | **ACCEPT-WITH-FIXES**: MINOR-1; MINOR-3 is optional |
| Parent erratum v1 | **ACCEPT**, with MINOR-5 (a stale reference list it leaves behind) |

**FATAL: none. MAJOR: none.**

## 2. Findings

### MINOR-1 (required for verdict text): trust labels missing from the statements

- **Where:** lines 29-31, 33-36 and 45-50.
- **What is missing:** the statements carry only the pending premises. The proof also uses:
  - Lev 2022 Thm 2 for p ≥ 11, through ROT-LS and ASSEMBLY-LS (verdict lines 11 and 15).
  - Lev again inside [ONE-SHORT-LS] at κ̂ ∈ U(p) (its lines 249-250).
  - S(p) at secondary-statement trust (KPS-SLZ line 8 with M-1), through ROT-KP+ in every cell with k = p and 2 ≤ κ̂ ≤ p−2. This includes p = 7, at κ̂ ∈ [2, 5].
- **Witness of the omission:**
  - Lines 49-50 say "(A), (B) at p = 7 use [ROT-SING] only … and no Lev input" and omit S(7).
  - The frozen addendum (lines 14-15) put a trust sentence inside the P0 statement. Proof lines 45-50 dropped it.
  - The ASSEMBLY-LS erratum N1 treated exactly this kind of omission as a required MINOR.
- **Minimal fix:** add one trust sentence to each statement: "for p ≥ 11, Lev (statement level) exactly in the ROT-LS cells ⌊2p/3⌋+1 ≤ κ̂ ≤ p−3 [for ASSEMBLY-P/ROT-P: and inside [ONE-SHORT-LS] at κ̂ ∈ U(p)]; S(p) at KPS-SLZ item-1/M-1 trust through ROT-KP+; classical imports as Sec. 8." On line 50, add "S(7) through ROT-KP+". Lines 57-60 and Sec. 8 already contain this content, so no proof step changes.

### MINOR-2: transitive trust disclosure cannot be checked from the supplied excerpts

- **(a)** Sec. 8 gives "Lev: no" for the DEP cells and lists index-one "inside LS+2 / LS+ band / BASE1+". Both rest on the import lists of the STAB-delta and LS+-chain verdicts, which are not in the excerpts; only their status and statement lines are. The absence of Lev in those status lines is consistent with the label, but it is not a quotation.
- **(b)** Line 281 cites STAB-delta line 5 as a "no computation premise" boundary. That line actually says no computation "was performed for this verdict", which is a different claim.
- **(c)** Lines 161, 193 and 282 say [ROT-SING] uses no Lev, REFL or (S1) and records no computation, citing "Sec. 4". The supplied ROT-SING excerpt (lines 12-21 and 41-44) supports only "no o_F hypothesis" and the use of CT.
- **Effect:** none on the logic. The internals of a pending premise do not affect a conditional composition, and line 284 already disclaims a transitive audit.
- **Minimal fix:** quote the exact import and trust lines, or relabel these entries "as recorded in status lines; import lists not in this manifest".

### MINOR-3 (optional): line 232, "exactly as the accepted multi-condition uses"

- The cited precedents (K01 line 38, ROT-KP line 43, FB line 29) all use monotone classes of the form o_F ≤ B with F − o_F ≥ c. Those classes are preserved by inequality closure.
- P0 is not monotone in κ. A Case-3 deletion of type (o−2, F) lowers κ by 1, which could land in U(p) ∪ {p−1} if o_F stayed at p. P0 survives only because o_F then drops to p−2.
- (B0) is actually carried by the explicit membership check at lines 229-231, and that check is correct.
- **Minimal fix:** replace "exactly as" with "analogous to; preservation here is by explicit check".

### MINOR-4 (optional): residual wording

- **(a) Lines 289-290:** label the ONE-SHORT-LS residual an "outer bound", matching the erratum's ROT-SING sentence. It is a correct outer bound: every admissible normal form has k = p, κ(w) ∈ U(p), and under (ZP) the failure of (S1) is exactly the presence of a long zero-sum.
- **(b) Line 54:** "not covered" should read "not fully covered". At p = 5, the sub-cell k = 5, κ̂ ≤ 1 is covered by ROT-KP plus REFL.
- **(c) Line 312:** the existential ROT-LS coverage is only the rotation half. INV* there is the composition ROT-LS + REFL.
- **(d) Lines 305-306:** the stall condition is true as a necessary condition. R ≥ 3 is implicit, since R ≤ 2 falls into Case 1.

### MINOR-5: reference list made stale by the erratum

- **Where:** lines 115-118, "Residual-only references (Sec. 9): RED/K0*, small-k, ROT-SING+".
- **Problem:** erratum m3 removed every Sec. 9 use of these references, so the list now points at nothing.
- **Minimal fix:** delete the list, or relabel it "formerly cited; not used or certified".

### INFO (no fix, no scope change): [ROT-SING] is not actually needed for (B)

- In (B), [ROT-SING] can enter only through (A) applied to a Case-3 word w_i with o_F(w_i) = p, k = p and κ̂ = p−1.
- That forces F(w) = F(w_i) = p, hence R(w) = 3p−1.
- EGZ applied twice then gives an identity 2p-subword made of rotations, before Case 3 is ever reached.
- So the stated dependency of (B) on [ROT-SING] is conservative, and therefore sound. Removing it would need a new frozen scope, which I am not proposing.

## 3. Domain violations

None found. Each interface is used inside its quoted original domain:

| Interface | Domain check |
|---|---|
| NF | avoiders of length 4p−2 |
| GRX | every representation, including empty runs |
| DAV | N = 4p−2, F ≥ p ≥ 2, frame at a run gap |
| ROT-LS | k ≤ p−1, any o_F |
| ALS | o_F ≤ p−1 |
| ROT-KP | k = p, κ̂ ∈ {0,1}, p ≥ 5, no o_F hypothesis (lines 15-17) |
| S1-sharp | 2 ≤ κ ≤ ⌊2p/3⌋ |
| ROT-KP+ | k = p, κ̂ ≥ 1 with no upper bound and no o_F hypothesis (line 10) |
| LS+2 | κ = p−2 |
| LS+ band | e ≥ 3 and p ≥ 10e−13 |
| BASE1+ | p ≡ 1 (mod 3), κ = (2p+1)/3 |
| REFL | original w, o_F ≤ p |
| Ledger | B = p ≤ 2p−3 (precedent: ROT-KP line 43); in (B0) the case analysis is re-run with explicit membership checks |
| RGR-LONG | p ≥ 5 |
| [ONE-SHORT-LS] (pending) | used only at \|Y\| = p+2κ̂ exactly, with ⌊2p/3⌋+1 ≤ κ̂ ≤ p−2 |
| [ROT-SING] (pending) | used only at k = p, κ̂ = p−1 |

No pending candidate is treated as accepted anywhere: Steps 4-5, Sec. 5, Sec. 8 and the residual sections all label them as conditions.

## 4. Audit record (independently verified)

**Quantifiers.**
- Every admissible normal form has k ≤ o_F. Under o_F ≤ p, each one falls into either ROT-LS (k ≤ p−1) or ROT-P (k = p).
- The criteria are existential and are applied to whichever form the process produces. The residual sections quantify over all forms.
- κ̂ = (R + k − 2p)/2 is determined by k and F. So all normal forms with k = p share one κ̂, and ROT-P's per-cell premise label is well defined for each w.
- When o_F ≤ p, k = p forces o_F = p and κ̂ = κ(w).

**GRX, all-plus pattern.**
- f_i = 0, so Φ = 0. δ = #{l_i odd} = p, so C_max = F − p = 2Ĥ. T = Σθ_i = 0.
- If Ĥ ≥ p, take C = 2p with the empty rotation selection, so κ̂ ≥ 0.
- An even m = 2p − C lies in [2κ̂+2, 2p] exactly when C ∈ [0, 2Ĥ]. Lengths m > R are vacuous. This gives (ZP_κ̂).

**DAV.**
- R + Ĥ = 2p − 1 + κ̂ ≤ 3p − 2, so κ̂ ≤ p−1.
- The four κ̂ cells partition [0, p−1] because ⌊2p/3⌋ ≤ p−3 for p ≥ 7 (at p = 7 both sides are 4).

**Endpoint κ = p−1.**
- Y = g^(2p−1)(3g)^(p−1) has |Y| = 3p−2 and satisfies (ZP_{p−1}): a zero-sum of length 2p would need b ≡ 0, hence a = 2p > 2p−1.
- It contains a long zero-sum with a = p+3, b = p−1 (length 2p+2, sum 4p ≡ 0).
- So (S1_{p−1}) fails. This confirms ONE-SHORT-LS is false at κ = p−1 and that ROT-KP+ is not available uniformly there.
- In Step 5, Ĥ = 0 gives p singleton blocks, F = p and R = 3p−2.

**DEP.**
- Inside [⌊2p/3⌋+1, p−2], the complement of U(p) is exactly: κ = p−2, or p ≥ 10(p−κ) − 13, or (p ≡ 1 mod 3 and κ = (2p+1)/3).
- Each case contradicts a long zero-sum:
  - (i) 3p−4 > 3p−5;
  - (ii) 3κ + e ≥ 3κ + 3;
  - (iii) (7p+2)/3 > 2p+2, which holds exactly when p > 4.
- U(7) = ∅, since 5 > 4. At p = 7 the only Step-4 value is κ̂ = 5, which is covered by both (i) and (iii).

| p | U(p) |
|---|---|
| 11 | {8} |
| 13 | {10} (9 is the BASE1+ cell) |
| 17 | {12, 13} |
| 19 | {14, 15} |
| 23 | {16, …, 19} |

- U(p) equals the LS+ verdict's undecided set (line 24) exactly.
- The nonemptiness arithmetic holds: 10p − 59 > 3p for p ≥ 9, and 10p − 79 > 3p for p ≥ 12.

**(A).**
- REFL hypotheses (i)-(iii) are met on the original w.
- REFL's caller obligations (its line 16) bind only callers that rebase SHgen-E on it. They are discharged inside ROT-KP (overlay m5) and ROT-KP+ (KPS erratum M-6), where base words have o_F(u°) ≤ k = p.

**(B).**
- *Case 1:* (F − o_F)/2 ≥ (3p−3)/2 ≥ p.
  - The frame starts at a rotation (R ≥ 1) or at a change of reflection value (R = 0), so no block wraps.
  - A cyclic shift only conjugates the product, so the same letter set is an identity 2p-subword in the original index order.
- *Case 2:* the shortened block stays nonempty, even and maximal, so o_F drops by exactly 1.
- *Case 3, odd count:* since R(w_i) ≥ 2, the only possible change is a junction fusion at an emptied run: odd+odd gives −2, odd+even and even+even give 0. Single-run and single-block words cannot empty a run.
- *Case 3, rotations and runs:*
  - A third rotation t ≠ 0 forces the two pairs to coincide.
  - Every rotation of w lies in w_1 or w_2.
  - Adjacent reflections of different values stay adjacent after deleting a rotation, including across the cyclic wrap.
- *Exhaustiveness:* Cases 1 and 3 already cover every R, so Case 2 is optional.

**(A0) and (B0).**
- **(A0) routing:**
  - o_F ≤ p−1 goes to ASSEMBLY-LS.
  - o_F = p with k ≤ p−1 goes to ROT-LS.
  - o_F = p with k = p goes to ROT-KP, S1-sharp + ROT-KP+, or DEP + ROT-KP+.
  - P0 restricted to p = 7 is exactly ¬(o_F = F = 7).
- **(B0) membership after each deletion:**
  - Case 2 gives o_F ≤ p−1.
  - Case 3 gives either o_F(w_i) ≤ p−1, or o_F(w_i) = p. In the second case o_F(w) = p and F is unchanged, so κ(w_i) = κ(w).

**Residual sections 9 and 10.**
- *9.1 singleton remark:* o_F = F means all blocks are odd singletons and there are no even blocks, so PM* never acts. Blocks separated by an empty run differ in value by maximality, so nothing fuses. The terminal word is unique, with k = p and κ̂ = p−1. Correct.
- *Erratum EGZ remark:* 3p−1 = (2p−1) + p, so two disjoint p-term zero-sums exist. Correct.
- *9.2 at o_F = p+1:* the Case-2 consequence holds, Case-3 deletions give o_F ∈ {p−1, p+1}, and the stall condition holds as a necessary condition.
- *Sec. 10 examples* (with F = p + 2(p−1−κ)) are all correct and are stated as sufficient classes only:

| p | P0 cells (o_F, F) | [ONE-SHORT-LS] cells (o_F, F) |
|---|---|---|
| 7 | (7, 9) | none |
| 11 | (11, 13) | (11, 15) |
| 13 | (13, 19), (13, 15) | (13, 17) |

## 5. Erratum assessment

- m1, the three m2 edits and both m3 edits are mathematically correct.
- The new endpoint row's claim that ROT-KP+ remains applicable when (S1_{p−1}) actually holds matches the quoted ROT-KP+ scope (KPS line 10: κ̂ ≥ 1, no upper bound).
- The erratum's only side effect is the stale list in MINOR-5.

## 6. Boundary preserved

- (A), (B) and ROT-P remain conditional on the pending [ONE-SHORT-LS] and [ROT-SING].
- DEP and P0 rest on accepted interfaces only, with their Lev (p ≥ 11), S(p) and classical trust carried as recorded.
- ROT-SING+ is not a premise, and p = 5 is not claimed.
- This review makes no claim at o_F ≥ p+1, about unrestricted INV*(p), or about ordered Olson for all D_(2p) or all groups.
- It involves no Lean, human review, novelty assessment or acceptance of the full problem.
