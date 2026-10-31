# f177 review v1: finite-arithmetic and case-completeness audit of the all-tail Shor n = 165·2^t candidate

- Wave: `f177-shor-165-all-tail-finite-audit`. Reviewer: **ReviewF177ShorArithmetic**, a same-harness task agent.
- Native `/bin/date` immediately before writing this file: **2026-10-29T08:04:28-0700** (Thu Oct 29 08:04:28 PDT 2026).
- Kind: an independent same-harness scientific review of ONE slice. It is not a human review, not an independent-model-family review, not a formal or kernel check, and not a novelty or priority assessment.

## 0. Bottom line (this slice only)

Every bounded residue table and every finite lemma or checker conclusion that the candidate states was reproduced by independently authored code. The code ran once under receipt and passed **71/71 registered checks** (exit 0). Each claimed UNSAT table is UNSAT under exhaustive enumeration over all types mod 330. The stated Q-side and P-side positive controls are SAT. The pre-registered mutations flip or hold for the intended reasons. The reduction from all t to residues mod 330 is exact, as the candidate claims. One correction to that picture: it is a one-line written argument (Lemma 1). The finite runs (t ≤ 8 actual-n screens, t ≤ 10 Lemma 1 test) are diagnostics, not the all-t proof.

- **FATAL: none. MAJOR: none** (within this slice).
- **MINOR:** three presentation or fidelity items, m1–m3 in §7.
- **INCONCLUSIVE, out of slice:** the three named imports (actual-word border theorem, Sands' Theorem 2.5, Łaba–Londner Corollary 6.2/T2). The class-uniformity of Lemma 2(b) depends on T2. Also inconclusive: the author's statement that their checker ran with PASS. I did not execute it, by rule.

The theorem as a whole is therefore NOT accepted by this review. Only its finite part is.

## 1. Inputs, verification, actual read order

| Item | Path (abridged) | SHA-256 verified | Bytes | LF | Clock |
|---|---|---|---|---|---|
| manifest | `review-waves/f177-…/manifest-v1.json` | `580d3e83109722a8e5c05598500378d82246363992189157834fd7cfd2de5a6e` ✓ | 3160 | 30 | 07:28:56-0700 |
| candidate | `…/shor-completion/frontier-20261029-165-family-all-q-anchored-border-no-go-v1.md` | `20169ac9e398d9d1ef37d263f9b51d0f9168c095c3e3eb21ade47572822d39c6` ✓ | 23071 | 312 | 07:30:16-0700 |
| author checker (static only) | `…/shor-completion/frontier-20261029-165-family-all-q-check.py` | `4c550a5750a822235f20a9862d582082f3427c307f6196575099149638a4538e` ✓ | 9099 | 234 | 07:30:16-0700 |

Read order:

1. Manifest, lines 1–30.
2. The complete candidate, as raw lines 1–110, 111–220 and 221–312.
3. The complete author checker, as raw lines 1–120 and 121–234. It was read only, never executed or imported.

Mathematical interpretation began only after step 3.

**Not opened:** Q55/f128, f157, any fibre packet, the 2310-family packets, the 165-family odd-tail packets, and any other non-premise packet. Main sent two status-only notices during the run, one on the f162 Olson hold and one on the f161 hold. I never accessed f161 or f162 materials, so no response was owed.

Skills consulted:
- `independent-snapshot-review`: not applicable, because no external model is allowed and none was used.
- `finite-witness-triple-verification`: its cross-vendor delegate steps were NOT performed, because external models are prohibited.

## 2. Slice, dependencies, assumptions

**Slice.** The audit covers:
- all finite residue tables of §§5–8;
- the finite algebra of Lemmas 2(b), 5 and 6 where independently computable;
- the §9 controls;
- the all-t type reduction;
- case completeness (d ∈ {1,3,5,11}, class lifts, the t=1 endpoint).

**Out of slice:** §2 (border reconstruction and the Corollary), the truth and statement fidelity of the imports, and the cyclotomic/T2 reasoning beyond its finite identities.

**Dependencies of the candidate's finite steps:**
- **Lemma 3** uses only (SP), which comes from Sands plus Lemma 1. It does not use T2.
- **Cases d=1, 3, 5** use (SQ) and Lemma 2(b) class-nonemptiness mod e, which needs T2.
- **Case d=11** uses (SQ), Lemma 2(b) mod 15 (T2), Lemmas 4–6 and (SP).
- **d ∈ {1,3,5,11}** follows from Lemma 3 plus Lemma 2(b) for P, which needs T2.

**My assumptions:**
- Python 3.14.3 standard-library integers are exact. `math.gcd` is used only as a cross-reference against my own valuation gcd.
- No other source.

## 3. Method

**Script.** `reviewer-f177-arith-check-v1.py`, SHA-256 `ea58f1bcbf2bc61c156e384655fefe4bb7f51b34aa4ca7f071cb2fa53dd1816d` (56,439 B, 1108 LF). I wrote it from the candidate's prose. It is standard-library only and never opens the author checker.

**Representation and algorithms.** These deliberately differ from the author checker:

| Area | Approach |
|---|---|
| Types | A residue mod 330 is the CRT tuple (x mod 2, 3, 5, 11). (SQ)/(SP) are evaluated from shared coordinates, not from `gcd(·,165)`. Equivalence with gcd was proved separately on all 330² ordered pairs. |
| gcd | Own 2-adic valuation gcd with n = 165·2^t, cross-checked against `math.gcd`. |
| Arc consistency | Own AC-3 worklist, with a removal log replayed against the then-current domains as a certificate. |
| Lemma 4 | Exhaustive backtracking over the initial domains for all transversals, plus a literal, prose-order mirror of Steps 1–6 over all 22 types of each named class. |
| §6 bullets | Each of the 35 bullets was transcribed (subject class and parity, comparator, bracket, k, relation) and checked arithmetically and by brute-force (SQ) semantics. |
| Cyclotomics | Built from the Möbius product of (X^d−1), with exact division. Nonvanishing is checked twice: by exact remainder, and by evaluation at every primitive m-th root of unity in F_p for p ∈ {331, 661, 881, 991} (all ≡ 1 mod 110). A nonzero value certifies Φ_m ∤ W. |

**Independence caveat.** The code was written after I had read the author checker, as the manifest order requires. It is independently authored but not blind. Generic polynomial multiply/divide helpers are necessarily similar in form.

**Receipted execution.** `reviewer-f177-arith-receipt-v1.json`, SHA-256 `ccd903b5229b95917f9001ae86703a18ffa02707979e5e22f543de3c6d934038`.
- Command: `python3 -B reviewer-f177-arith-check-v1.py --out reviewer-f177-arith-check-v1.out.json`.
- Native clock before: **2026-10-29T08:01:12-0700**. After: **2026-10-29T08:01:13-0700**.
- Exit code **0**.
- Script SHA identical before and after the run.
- Output `reviewer-f177-arith-check-v1.out.json`, SHA-256 `54b39cad46429abbd20144af52e00160b739a757cb644caad183fecc56764b8e` (77,896 B), created exclusively. Result `ALL_REGISTERED_CHECKS_HOLD`, 71/71.
- Compute: about one second. No solver was used, so no solver UNKNOWN was ever treated as an exclusion.

## 4. Per-table coverage and verdict

In this table, "types" means residues mod 330. Every enumeration in it is exhaustive.

| # | Candidate claim | Coverage | Method(s) | Result | Verdict |
|---|---|---|---|---|---|
| 1 | Lemma 1 / all-t reduction (§3, §8) | All odd u ∈ Z_n for t=1..10 (168,795 values) | Valuation gcd vs `math.gcd(u,n)`, `gcd(u,165)` and the product of the dividing primes; shared-coordinate rule vs gcd on all 108,900 type pairs | 0 mismatches | Verified (bounded test; the all-t statement is the one-line proof, which I checked by reading) |
| 2 | Old gcd sets (§3, §8.6) | t=1..12 | Own gcd plus `math.gcd` | G_A(330)={2,3,5,11}, G_Y(330)={1,2,6}; G_A(660)={3,4,5,11}; t≥3: G_A={3,5,8,11}; t≥2: G_Y={1,2,6,12}. Odd parts are {3,5,11} and {1} for every t | Verified. See m2 for the t=1 note. |
| 3 | (SQ), (SP), rule (R) | All opposite-parity, distinct-class type pairs: 53,460 (e=55), 52,800 (e=33), 50,820 (e=15) | Rule (R) and the e=15 shared-coordinate form vs (SQ) | 0 mismatches; k ≤ 1 always | Verified |
| 4 | Lemma 3 table and exclusion | 4 mod 15: 22 types (11+11); 1 mod 33: 10; 2 mod 55: 6 | Row arithmetic (differences, determined primes, third prime ∤ 8) plus exhaustive (SP) vs A | Every type killed: **UNSAT** | Verified |
| 5 | d ∈ {1,3,5,11} | The 8 odd divisors of 165 | Each d divisible by two of 3, 5, 11 contains 15, 33 or 55 | Allowed {1,3,5,11}; e ∈ {165,55,33,15} | Verified (conditional on Lemma 2(b)/T2) |
| 6 | d=1: class 2 mod 165 | Types 2 (even) and 167 (odd), both lifts; plus all 2^t actual lifts in Z_n for t=1..8 (510 elements) | Exhaustive (SQ); actual gcd reasons | 2 is killed by anchors 13 (gcd 11) and 7 (gcd 5); 167 only by anchor 14 (gcd 3); every actual lift has exactly these gcds. **UNSAT** | Verified |
| 7 | §6 bullets (k values, relations) | 35 bullets: 15 for e=55, 20 for e=33 | Arithmetic plus brute-force semantics | All k, relations, opposite-parity and distinct-class conditions hold. One bracket has the wrong sign only (m1). | Verified (+ m1) |
| 8 | e=55: states {(1,2)}, {(1,2)}, {(0,0),(0,2)}; no triple | Classes 3, 24, 25; 6 types each | Exhaustive product (size 2); AC-3 wipeout; abstract-state product | States equal the claim; 0 compatible triples: **UNSAT** | Verified (conditional on Lemma 2(b)) |
| 9 | e=33: four state sets; no 4-tuple | Classes 22, 3, 4, 15; 10 types each | Exhaustive product (size 18); AC wipeout; abstract states | States equal the claim; 0 compatible tuples: **UNSAT** | Verified (conditional on Lemma 2(b)) |
| 10 | e=15: initial sizes [18,9,2,2,1,8,2,9,2,8,1,2,2,9,18]; AC gives the Lemma 4 singleton types {0,1,7,13,14,55,56,62,68,110,234,276,282,288,289} | All 15 classes × 22 types | AC-3 (78 removals, replay valid); exhaustive backtracking (119 nodes, uncapped); prose-literal Steps 1–6; anchor table and g | Sizes equal the claim; fixpoint equals the claim; **exactly one** pairwise-compatible transversal, namely those types; Steps 1–6 each hold; the types contain Y, are pairwise (SQ)-consistent and give {0,1,7,13,14} mod 55, three each | Verified (conditional on Lemma 2(b)) |
| 11 | Lemma 5: weights, CRT, factorization, nonvanishing | 110 residues; m ∈ {1,2,5,10,11,22,55,110} | Exact coefficient identity Σ W(z)X^z ≡ (2+X^55)Y(X^56) mod X^110−1; exact remainders; F_p evaluation at all primitive roots, 4 primes | W(z) is 2/1/0 as stated; Φ_m ∤ W for m ∈ {1,2,11,22,55,110}; Φ_5, Φ_10 divide W; Y ≢ 0 mod Φ_55 and mod Φ_11; ord(ξ^56) ∈ {11,55} as stated | Verified |
| 12 | Lemma 6: Φ_11Φ_22Φ_55Φ_110 = 1+X^10+…+X^100; 10-periodicity | Exact polynomials | Product; (X^10−1)Ψ = X^110−1; basis X^j·Ψ for j<10 | All hold; 110 divides n exactly when t ≥ 1 | Verified (finite algebra; the transfer P(ξ)=0 uses Lemma 5 and the tiling identity) |
| 13 | Lemma 2(b) identity Π_{1<m\|e} Φ_m = 1+…+X^(e−1) | e ∈ {3,5,11,15,33,55,165} | Exact | Holds | Verified (identity only; divisibility of Q needs T2) |
| 14 | Final certificate | x ≡ 1 mod 110: types 1, 111, 221 | (SP) against all of A | vs 0: only r3=0 (111); vs 8: only r3=2 (221); vs 3 and 11: no constraint (same parity); together: **UNSAT** | Verified |
| 15 | §9 Q-side control at n=2640 | The 15 stated elements | Own CRT rebuild; all pairwise actual gcds with n | G_A(2640)={3,5,8,11}; contains Y; one element per class mod 15; parity and mod-11 residues as in Lemma 4; 16-adic residues as stated; no pairwise gcd in G_A. **SAT** (a Q-only witness, not a factorization) | Verified |
| 16 | §9 P-side control | x ≡ 1 mod 110 | Per-constraint | Each single constraint is SAT (111 resp. 221) | Verified |
| 17 | §8.6 bounded screens | Z_n exhaustively, t=1..8 (claims cover t ≤ 6) | Own gcd; full actual Sands screens | P/Q screen sizes 6/47, 42/118, 112/286, 224/658, 448/1316, 896/2632 (equal to the claims); t=7: 1792/5264; t=8: 3584/10528. No Lemma 3 class or 2 mod 165 element survives. Every Q-screen type lies in every used domain. | Verified |
| 18 | t=1 endpoint | n=330, so types equal Z_n | — | The tables are literally exhaustive at t=1, where n=330 so types are Z_n. The anchors already collide there: gcd 2 appears on both sides (m2). | Verified; note m2 |

**Coverage of class lifts.** Every class r mod e, for e | 165, lifts to 330/e types covering both parities and all free-prime residues: 2 for e=165, 6 for e=55, 10 for e=33, 22 for e=15. The class x ≡ 1 mod 110 lifts to 3 types. All of these lifts were enumerated.

**Negative controls on the Q-control set:**
- Making the class-(1,0) element 385 even (replacement 880) is rejected by gcd 3 against 1, 7, 13 and 289. This is the Step 1 reason.
- Moving the class-(0,3) element 288 to 1 mod 11 (replacement 1728) is rejected by gcd 5 against anchor 13 and gcd 11 against anchor 1. This is the Step 3 reason.

**Extra reviewer P-side control.** Drop Lemma 6 and keep only (SP), the anchors A and the d=11 class-nonemptiness mod 11. The type constraints are then SAT: the even types 276, 156, 246, 126, 6, 216, 306, 186 complete A to all 11 classes. So the contradiction genuinely needs the Lemma 6 transfer, as §9 says.

## 5. The all-t reduction: what is and is not established

**What holds.** Every comparison in §§5–7 pairs elements of opposite parity. For such pairs, the relevant gcd with n equals gcd(·,165) (Lemma 1). It therefore depends only on the difference mod 330. Class membership mod e | 165 and mod 110 also factor through mod 330.

**Why the finite tables are exact for every t ≥ 1.** Each finite table over Z_330 is exactly the image of the corresponding Z_n statement, and the argument contains no t-dependent finite object. The only t-dependence is 110 | n, which holds for every t ≥ 1. The step from finite t to all t is a reduction, not an induction. The t ≤ 8 and t ≤ 10 runs are diagnostics.

**What the finite tests do NOT establish:**
- (SQ)/(SP) themselves. They are Sands consequences; the import was not reviewed.
- Any existence statement drawn from Lemma 2(b) (T2): that every class mod e (or mod d) is nonempty or uniform.
- The step P(ξ)=0 in Lemma 6. It is algebraically sound by reading, but it rests on the tiling identity.
- §2 and the Corollary.
- t = 0. There parity is not a function on Z_165 (1 ≡ 166), so the reduction does not apply. This was verified in the script.
- Any order not of the form 165·2^t.
- Same-parity (even-gcd) Sands constraints. The candidate deliberately does not use them, and that relaxation is sound.

## 6. Mutations (pre-registered expectations vs observed)

The expectations below were written in the script before any run reached this section. The first development run crashed earlier, in my own periodicity check (see §8). All of these mutations matched their expectations.

| ID | Mutation | Expected and observed | Intended reason |
|---|---|---|---|
| M01 | Drop head 0 (odd gcd set from A becomes {3,5}) | Lemma 3 SAT in all 3 classes, odd survivors only; final SAT {221}; d=1 UNSAT | An odd x keeps only one opposite-parity head (8); d=1's even lift is still killed by anchor 7 (gcd 5) |
| M02 | Drop head 3 ({3,11}) | Lemma 3 SAT, even survivors only; final UNSAT; d=1 UNSAT | An even x keeps only head 11; the final step needs only 0 and 8 |
| M03 | Drop head 8 ({3,11}) | Lemma 3 SAT, odd survivors only; final SAT {111} | The third-prime argument needs both 0 and 8 |
| M04 | Drop head 11 ({3,5}) | Lemma 3 SAT, even survivors only; the final table stays UNSAT | The final step's premise 11 ∈ P is gone, so the route breaks at the premise, not at the table |
| M08 | Drop tail 13 | d=1 still UNSAT | Backup: 2−7 ≡ −5 mod 165 gives gcd 5 |
| M09 | Drop tail 14 | d=1 SAT with survivor exactly 167; a representative-only check of 2 alone wrongly says UNSAT | The odd lift's only killer is 14, so coverage of the lift is load-bearing |
| M10–M12 | Remove gcd class 3 / 5 / 11 from (SQ) | Without 3: d=1 SAT {167}. Without 5 or without 11: UNSAT. The P-side tables are unchanged (UNSAT). | Killers of 167: gcd 3. Killers of 2: gcds 5 and 11. |
| M13 | Remove gcd class 1 from (SP) | Every Lemma 3 and final type survives (SAT); the Q-side is unchanged | (SP) is the only P-side constraint |
| M14 | Drop the parity restriction (apply the gcd(·,165) rule to all pairs) | Rejected: the literal anchors are flagged, (0,8) and (3,11) in P and (1,7), (1,13), (7,13) in Q. Every domain is wiped out. | Unsound: for t ≥ 2 the actual gcds are 8 or 4, and 6, which are not Sands collisions. Lemma 1 requires odd u. |

**Exploratory results** (not pre-registered; no exclusion is drawn from them):
- **Lemma 4 is robust to some gcd losses.** The e=15 Lemma 4 structure survives losing gcd class 11 from (SQ) (M01, M04 and M12 all leave {3,5}). AC then derives Step 5's eliminations from k=1 constraints alone. The prose's k=0 arguments are valid, but they are not the only route.
- **Dropping one of tails 1, 7, 13** leaves exactly the three classes with that r5 undetermined mod 11 (7 types each), giving 7 transversals. Each of these anchors pins g at one r5.
- **e=55 and e=33** become SAT under most anchor or gcd drops. They stay UNSAT for e=55 under M06 and M07, and under M13.
- **Capped counts.** The e=15 transversal counts for M02, M03, M05, M09, M10 and M11 hit the 1000-solution cap. These counts are UNKNOWN, and nothing is inferred from them.

## 7. Findings by claim

**FATAL:** none. **MAJOR:** none.

**MINOR:**
- **m1 (presentation, §6, d=5 chain step 4).** "x_4 is odd. Against x_15 [11, k=1]" violates the stated bracket convention r−y. The correct value is 4−15 = −11 (≡ 22 mod 33). It is the only one of 35 transcribed bullets with a bracket mismatch, and the mismatch is sign-only. k=1 and the conclusion x_4 ≡ 4 (mod 5) are unaffected; the semantics were verified by brute force.
- **m2 (scope note, t=1 endpoint).** At n=330 the anchors already violate Sands directly: gcd(8−0, 330) = gcd(14−0, 330) = 2, which lies in G_A(330) ∩ G_Y(330). At t=1 the actual P-screen contains no head, and the Q-screen contains only the tails 1, 7 and 13. For t ≥ 2, G_A ∩ G_Y = ∅. The order 330 is therefore excluded trivially, independent of the case analysis. The written analysis remains valid there; it is merely redundant. §1 and §8.6 do not mention this. A one-line remark is suggested.
- **m3 (checker/prose fidelity, static reading only).**
  - §8 item 4 says the checker "confirms" nonzero remainders for m=1 and m=2. The checker stores these in its output but asserts only m ∈ {11,22,55,110} (nonzero) and {5,10} (zero). The facts themselves hold: W(1)=15 and W(−1)=5; my run confirms them exactly and over F_p.
  - The checker's section comments label the e=165, e=55 and e=33 blocks "Section 4/5/6". The candidate puts all three in §6.
  - The checker's Step-5 mirror refutes the classes (0,0) and (2,4) with the (2,0)/(0,4) types rather than with anchors 14/0, as the prose does. This is logically valid, but not literal.

  None of these affects correctness.

**INCONCLUSIVE (not reviewed in this slice):**
- **i1.** Sands' theorem (LL Theorem 2.5): its statement and applicability. I verified only the arithmetic consequences (SQ)/(SP) given that theorem.
- **i2.** LL Corollary 6.2 (T2): statement fidelity, including the labeling of the exempt primes, and its application. I verified only the hypothesis arithmetic: for every factorization |P||Q| = 165·2^t (t ≤ 6), each of 3, 5, 11 divides exactly one cardinality. Lemma 2(b)'s nonemptiness, used in d=1/3/5/11 and in d ∈ {1,3,5,11}, rests on this import.
- **i3.** §2, the actual-word border reconstruction (RSS), and the Corollary.
- **i4.** The author's report that the checker was exec'd with PASS. It was not re-executed, by rule. My independent outputs agree with every value the candidate states.
- **i5.** Novelty and priority: not assessed.

**Review gate 8 (non-premises).** In the two frozen inputs, the §0 non-premise packets appear only in the §0 list and the §9 relation paragraph. No step of §§2–8 and no line of the checker cites them. This was established by reading the inputs only; the packets themselves were not opened.

## 8. Omitted-case accounting and status vocabulary

**UNSAT** (exhaustive):
- the three Lemma 3 classes;
- d=1 class 2 mod 165, at type level and over all actual lifts for t ≤ 8;
- the e=55 triple;
- the e=33 quadruple;
- the final certificate.

e=15 has exactly one transversal.

**SAT:**
- the Q-side control at n=2640;
- each single P-side constraint;
- the P-side relaxation without Lemma 6;
- the mutation witnesses.

**UNKNOWN:**
- No baseline table.
- Exploratory capped transversal counts only (M02, M03, M05, M09, M10, M11).

**Omitted or not run:**
- t = 0 and other orders, which the candidate itself leaves out of scope;
- actual-n enumeration for t ≥ 9, covered only by the written reduction;
- any search for full tilings or factorizations;
- the imports, Lemma 2(b) uniformity and §2.

## 9. Process deviations and disclosures

- **D1 (development runs).** Before the single receipted run there were:
  - three development runs of my script, with output captured to my eval kernel only and no files written. The first crashed with an IndexError in my own Lemma 6 basis check, before reaching the mutations.
  - one in-kernel import of my module to time `sec_lemma1`. Code edits between runs: the padding fix, two added checks (actual class-2 lift reasons; the Lemma 2(b) cyclotomic product), a check-derived summary, and a guard on the summary's check IDs. Three expectation or text defects were fixed before the first run.
- **D2 (stray non-prefixed directory).** The in-kernel import (D1) wrote `__pycache__/reviewer-f177-arith-check-v1.cpython-314.pyc` into this wave directory (123,916 B, SHA-256 `8dadde7aae11cc5634c74c1245f9197e60a1707e77ddbb1921b7afa403452e37`, mtime 08:00:48-0700). The directory name is not reviewer-prefixed, which deviates from "reviewer-prefixed artifacts only". It contains only bytecode of my own script. I did not delete it, because deletion is prohibited. The parent may dispose of it.
- **D3 (exposure).** My code was written after statically reading the author checker, as the manifest read order requires (§3).
- **D4 (harness backgrounding).** A harness-backgrounded `/bin/date`/python-version command completed at 07:46:56-0700. It had no effect.
- **D5.** No author code was run or imported. I used no web search, no external model or API, no Git, no deletion, no publication and no infrastructure change, and I did not contact the author.

## 10. Artifacts (all in this wave directory)

| File | SHA-256 | Bytes |
|---|---|---|
| `reviewer-f177-arith-check-v1.py` | `ea58f1bcbf2bc61c156e384655fefe4bb7f51b34aa4ca7f071cb2fa53dd1816d` | 56,439 |
| `reviewer-f177-arith-check-v1.out.json` | `54b39cad46429abbd20144af52e00160b739a757cb644caad183fecc56764b8e` | 77,896 |
| `reviewer-f177-arith-receipt-v1.json` | `ccd903b5229b95917f9001ae86703a18ffa02707979e5e22f543de3c6d934038` | 1,271 |
| `__pycache__/…cpython-314.pyc` (D2) | `8dadde7aae11cc5634c74c1245f9197e60a1707e77ddbb1921b7afa403452e37` | 123,916 |
| `review-v1.md` (this file) | reported in the reviewer's return message, since a file cannot contain its own hash | — |

## 11. Non-claims

- This review does not accept the theorem or the Corollary.
- It certifies nothing about the imports, Lemma 2(b) uniformity, §2, novelty or priority.
- It makes no formal or kernel claim.
- It is a same-harness review, not human or independent-model-family review.
- The original unrestricted finite UD factor-completion problem remains OPEN, as the candidate itself states.
