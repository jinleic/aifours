DISPOSITION: ACCEPT-WITH-FIXES

- **`c5/proof-SEED-r2.md`: ACCEPT-WITH-FIXES.** I checked Secs. 0–4 step by step and found no mathematical gap and no counterexample. All findings are MINOR, NIT or INFO.
- **`c5/proof-Cplus-r1.md`: ACCEPT-WITH-FIXES.** Theorem C+ is correct, conditional on (H). Corollary HYP is correct but computer-assisted, and one passage presents it as written (MAJOR, status only).
- There are no BLOCKERs. I did not check the SHA-256 values (no tools).
- All "hand" checks below are arithmetic on the packet's own data. They are controls, not substitutes for written steps.

Abbreviations: SEED, CP = the two targets; WALL = `c3/proof-WALL.md`; C = `c3/proof-C-r1.md`.

## 1. SEED: verification

**Sec. 0 (l.28–47)**
- lam/lamc are Lemma H with B = 1, κ = kB+1, β = 0, D = p+kB−1. ✓
- Singleton values ✓. Λ1 ≤ p−2 needs kB ≤ p−4.
- Lift intervals have kB+⌊δ/2⌋−1 and kB+⌊δ/2⌋ ≤ (p+kB)/2 ≤ p−2 integers. Existence follows from λ+λᶜ ≤ p, and uniqueness from the size. ✓

**Lemma PS**
- 2m ∈ {kB+1, kB+2} and 2m ≤ p−3 by parity (p odd). ✓
- Endpoints t ∈ {1, 2, n−3, n−2, n−1, n}:
  - The excluded runs, or run 0, separate all pairs. For t = n−2, P₁ = {n−1, n} and {1, 2} are separated by run 0.
  - Q has exactly the blocks P₁…P_m, and Q+t still has m blocks. ✓
- Count: Σ⌊(Lᵢ+1)/3⌋ ≥ (n−7)/3 ≥ kB/2, which follows from kB ≤ 2p−14. ✓
- All four closed forms in (b) ✓, and (c) ✓, with z = x_t by uniqueness.
- Containment in the canonical range needs only ⌈δ/2⌉ ≤ kB+1.
- Structural check:
  - λ(Q)+λ(Qᶜ) = p+2−⌈δ/2⌉ and λ(Q+t)+λ((Q+t)ᶜ) = p+2−⌊δ/2⌋.
  - Both equal p at δ = 4, so the arcs are single points and x_t = 1, as Remark (1) says.

**Lemma SL** ✓. With the canonical ranges, (Aˢ) and (Bˢ) are literally Lemma L's (A) and (B). It is proved from the Claim alone.

**Lemma SCW**
- The step choice is valid: m′ ≥ 1, t aligned, 0 ≤ y ≤ p+kB.
- s = 2:
  - (i) needs 3⌈δ/2⌉ ≤ p+5, which holds because ⌈δ/2⌉ ≤ (p−1)/3.
  - (ii) needs ⌈δ/2⌉ ≥ m and δ+3 ≥ 2⌈δ/2⌉.
- s ≥ 3:
  - The equivalences and all 18 term-sums are correct.
  - The integer minima are ≥ ⌊δ/2⌋+1 for (A), against a target of ⌈δ/2⌉−2, and ≥ ⌊δ/2⌋+2 for (B), against ⌊δ/2⌋. So the slack is ≥ 2 (using δ ≥ 4), matching the receipt.
  - No lower bound on kB is used here.
- Pin ✓. The lower end is ≥ 1 iff (p+kB+1)/2 ≥ kB; the upper end is ≤ 2p−1 iff kB+⌊δ/2⌋ ≤ p.

**Theorem SEED**
- (2.1) re-derived, including the case D_Q = −1.
- Step 1 ✓ (2kB−p−1 ≤ kB−5).
- Step 2 for 2kB > p ✓:
  - First term ≤ 2kB−p−2 ≤ kB−6 < c(Z).
  - Third term < |Z_al| ≤ c(Z), also when |Z_al| = 0.
- Step 3 ✓.
- Every pattern used is proper.
- Corollary ✓: the SEED range is empty at p = 5 and 7, and the hypotheses of W-ALL match exactly.

**Tiny primes (hand)**

| p, kB | [a, b] | Pair-seed arcs (PS (b)–(c)) | Pin window |
|---|---|---|---|
| 11, 6 | [0, 1] ⊂ [−4, 2] | z ∈ [0, 1] | [4, 18] |
| 11, 7 | [1, 1] | T2 = T3 in λ(Qᶜ), harmless | [3, 19] |
| 13, 6 | [−1, 2] | z ∈ [−1, 2] | [5, 21] |

The pair steps hold at each of these values.

**Circularity:** none. SEED uses Lemma H (necessary direction only), the Claim, WALL (0.1), (0.2), (2.1), and W-ALL only in the Corollary. It does not use (H), Lemma L or any c4 theorem.

## 2. SEED: findings

- **S1 MINOR, `SEED:160`.** "(c(empty) = 0 < kB − e_Z unless kB = 1)" is a garbled copy of WALL:125; there is no exception.
  - Edit: "(if Z = ∅ then e_Z = 0 and c(Z) = 0 < kB = kB − e_Z)".
- **S2 MINOR, label collision.** "(0.1)/(0.2)" denotes three different things: WALL's λ formulas (l.31), this file's arc statement and Claim (l.37, 41), and C's (0.2) (l.188). Line 154's "pure algebra from (0.1)" points to the wrong one.
  - Edit: rename l.37/41 to (S1)/(S2) and update l.45, 74, 93.
  - Edit l.154 to "pure algebra from the λ formula, l.33".
- **S3 MINOR, `SEED:19`.** "Theorems KB0, IND, IND* (… they become special cases)" is unsupported for IND*. The Consequences paragraph treats only KB0 and IND, and CP:99–102 applies IND* to 443 sample words not shown to lie in W(p, kB).
  - Edit: "their W(p, kB) cases (KB0, IND/IND-I) become special cases (Consequences); no claim about IND*".
- **S4 MINOR, `SEED:181–184` (Remark (1)).** The hypothesis ledger is imprecise and incomplete.
  - 3kB ≥ p+5 is used only through ⌈δ/2⌉ ≤ kB+1 (PS (c)) and 3⌈δ/2⌉ ≤ p+5 (aligned pair). Both hold with slack; δ ≤ 2kB−5 and δ ≤ (2p−5)/3 are sufficient conditions, not the actual uses.
  - The ledger omits k

…the remaining uses of kB ≤ p−4 (δ ≥ 4):
  - Step 1 (l.158: 2kB−p−1 ≤ kB−5);
  - Step 2 (l.163: 2kB−p−2 ≤ kB−6);
  - lift uniqueness (l.46–47) and the Λ1 closed form (kB ≤ p−3);
  - [a, b] ≠ ∅.
  
  It also omits that p is odd in 2m ≤ p−3.
  - Edit: replace Remark (1) with the exact list above. Add that p ≥ 11 enters only through kB ≤ 2p−14 in PS (a).
- **S5 NIT, `SEED:17`.** "one changed justification" is wrong: Step 1's "(2kB − p − 1 ≤ kB − 5)" at l.158 is also new relative to WALL:122.
  - Edit: "two changed justifications (Step 1, l.158; Step 2, l.163–165)".
- **S6 NIT, `SEED:78–80`.** "exists for every kB ≤ p − 4" is true only for the congruence u_t ≡ z ∈ [a, b] (with p ≥ 11). It identifies the canonical lift only when ⌈δ/2⌉ ≤ kB+1, i.e. 3kB ≥ p−2.
  - Edit: say so explicitly.
- **S7 NIT, `SEED:149`.** The restatement adds an undefined "inherited" and drops "x normalised to 1".
  - Edit: quote WALL:15–18. The reflection-run sum condition is automatic: (3p−3−kB−k)/2 = p−2−kB.
- **S8 NIT, `SEED:39–40`.** If λ+λᶜ ≤ 0, the "complement" is all of Z_p and the arc has ≥ p+1 integers. Also, "contains u_Q" should read "contains a representative of u_Q, contradicting Lemma H". This is wording only.
- **S9 INFO, `SEED:175–179`.** The DOB(p) containment, the KB0/IND scopes, and the closure of c4 README §9(i) rest on files not in the packet. They are unverified here but not load-bearing for Theorem SEED or its Corollary.
  - "c4/…-r1.md = c5/…-r2.md" asserts identity of files that differ by the minor-doc deltas.
  - Edit: "c4/proof-KB0-r1.md, superseded by the minor-doc revision c5/proof-KB0-r2.md (sha256 …, scope at l.…)". Do the same for IND, and cite the line that defines DOB(p).
- **S10 INFO, `SEED:200–201`.** "lowering the seed's lower end by w = 3 or 4 makes a pair step fail" is ambiguous. By hand, with a replaced by a−w:
  - The aligned pair step needs 3⌈δ/2⌉ ≤ p+5−2w, so it survives w = 3.
  - The anti pair step needs δ+3−w ≥ 2⌈δ/2⌉, so it fails at w = 3 iff δ is odd, and always fails at w = 4.
  - Edit: "the least failing w is 3 (δ odd) or 4 (δ even)". So a has slack 2; this does not conflict with Part C, which concerns seed width.
- **S11 INFO, receipt arithmetic (hand, from the packet's numbers).** All consistent:
  - the replay list has 95 (p, kB) pairs;
  - the stage counts sum to 11,400 = 95·60·2;
  - wordcheck has 204 cases with Σn = 16,242 runs;
  - Part D has 252 cases for 11 ≤ p ≤ 61.
- **S12 INFO, `SEED:16, :173`; `CP:10`.** These cite "Codex ACCEPT", but the frozen WALL:3 and C:3 still read "NOT yet independently reviewed".
  - Edit: cite the review-note paths.

## 3. Cplus: verification

**Case A**
- (A-ii) (C:69–76) uses only 2kB ≤ p, X_{t} ≥ λ({t}) and d_t ≤ p−3. ✓
- The deletion argument tolerates c_t < 0, because only the per-step drop bound matters.

**(B1+), CP:39–53**, every line ✓:
- the aligned-defect bound and the sur bound;
- the ≤ 2m(Z) neighbour bound;
- ⌈(b+1)/2⌉+⌊b/2⌋ = b+[b even];
- n_an+n_ev,an ≤ B−n_pr (dropping n_ev,an/2 ≥ 0 is legitimate);
- under (i), s0 ≥ kB+1 ≥ 2.

**(B2+)**
- Path independent set: in a path of L runs the odd positions give ⌈L/2⌉ pairwise non-adjacent runs.
- Runs in different maximal blocks of X_o are non-adjacent.
- Σ⌈Lᵢ/2⌉ ≥ |X_o|/2 ≥ Δ+½, so at least Δ+1 runs are available. X_o ≠ ∅ because |X_o| ≥ 1.
- S avoids Z and its neighbours, so m(Q) = m(Z)+Δ+1.
- Properness: a neighbour v ∉ Z of Z has a neighbour in Z, so v ∉ X ⊇ S, so v ∉ Q. ✓

**(M), (Fl), (P)** (C:98–109) re-derived with no use of n_ev,al. (P) gives X_Q+m(Q) ≤ p−2−B/2 < p. ✓

**Also:** Theorem C ⊆ C+ ✓. No circularity: C+ uses (H) only through (0.2) (Lemma L plus the CORE pin) and does not use SEED.

**Corollary HYP data (hand, from CP:72–85).** Every displayed parameter is consistent.

| Word | p | k | kB | A | B | R | E | F = Σl | H | κ | n_pr | n_ev,al | s0 | anti/pair blocks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H1 | 11 | 13 | 1 | 15 | 4 | 19 | 6 | 23 | 5 | 5 | 0 | 5 | 1.5 | {0},{5},{9} |
| H2 | 11 | 13 | 1 | 15 | 4 | 19 | 6 | 23 | 5 | 5 | 0 | 6 | 1 | {1,2},{4},{7} |
| H3 | 11 | 13 | 1 | 15 | 4 | 19 | 6 | 23 | 5 | 5 | 0 | 5 | 1.5 | {2},{4},{8} |
| H4 | 13 | 15 | 1 | 18 | 5 | 23 | 8 | 27 | 6 | 6 | 1 | 5 | 2 | {0},{4},{6} |
| H5 | 13 | 15 | 1 | 18 | 5 | 23 | 8 | 27 | 6 | 6 | 0 | 5 | 1.5 | {2},{5} |
| H6 | 13 | 14 | 2 | 19 | 3 | 22 | 8 | 28 | 7 | 5 | 1 | 7 | 3 | — |
| H7 | 13 | 15 | 1 | 18 | 5 | 23 | 8 | 27 | 6 | 6 | 0 | 5 | 1.5 | {1},{10,11,12} |

- Each word satisfies κ = p−1−H, kB = κ−B, R+F = 4p−2, (0.1) (with equality for the kB = 1 words) and 2kB ≤ p.
- So (ii+) holds while Theorem C's (i) and (ii) fail, as claimed.
- Remark (1)'s forcing of x = d is correct: λ({t}) = d_t iff d_t ≤ B+2, and max d = 4.

**Control (H1, hand).** Z = {0, 5, 9} is certified by Lemma L:
- λ({0}) = λ({9}) = −1 and λ({5}) = −2; the singleton complements have λ = 9.
- λ({0,5}) = −2 and λ({0,5}ᶜ) = 10; λ(Z) = −2 and λ(Zᶜ) = 9.
- (A) gives 7 and 6, both ≥ 1; (B) gives 16 and 17, both ≥ 12.
- With x = d, X_Z = −4 < −2 = λ(Z), so the kill is genuine.

## 4. Cplus: findings

- **C1 MAJOR (status overclaim), `CP:7, :86–90, :101–103`.** Corollary HYP's hypotheses are established only by [F]:
  - (H) for each word;
  - the NMH/item-(iii) conditions beyond the arithmetic above (RGR, not ZSI-B).

  This contradicts l.7 ("[F] … never a hypothesis"). Remark (3)'s "excluded by a written argument" is false as stated: it grants only IND*'s receipt, not the (H) receipts. The mathematics is fine; the label is not.
  - Edit l.86: "**Corollary HYP** [W+F, computer-assisted]".
  - Edit l.7: add "except Corollary HYP, whose hypotheses are certified by the [F] receipts cited in its proof".
  - Edit l.101–103: "…excluded by a written reduction (Theorem IND* or C+) whose per-word hypotheses are certified only by exact computation (c4/out/ind_star_ex.txt; map3/map5 DP and c3/hcheck.py)".
- **C2 MINOR (relaxation wording), `CP:96–98, :110, :112`.** "Avoiders appear" at shrink 2–3 refers to solutions of a shrunk window system. These are not words of D_(2p), and no ordered-product replay exists.
  - Edit: "no residue vector satisfies all Lemma-H window conditions (hence, by the necessary direction of Lemma H, no avoider)".
  - Edit: "solutions of the shrunk (relaxed) window system appear; they are not group counterexamples".
- **C3 MINOR, `CP:33–35`.** This conflicts on its face with C:114–115, which says the n_ev,al hypothesis "enters … (A-i)/(A-ii)".
  - Edit: add "C Remark (1) refers to branch selection; C:69–76 use only 2kB ≤ p, the singleton bound and d_t ≤ p−3."
- **C4 INFO (optional sharpening; corrected bound).** Since |X_o| ≥ 2Δ+s0 and both |X_o| and Δ are integers, s0 ≥ ½ already suffices.
  - (ii+) can be weakened to "2kB ≤ p and n_ev,al ≤ 2(k−kB−2B)+n_pr−1". At l.53, replace the s0 ≥ 1 step with "s0 ≥ ½ ⇒ |X_o| ≥ 2Δ+1 by integrality".
  - At l.54, "needed … ≥ 2" should read "> 1".
- **C5 INFO, `CP:87–88`.** "Not ZSI-B" is [F]-only, its definition is not in the packet, and it is not needed: C+ covers all NMH words with R ≤ 2p−3, ZSI-B included (C:8). Note that H6 has k = p+1 = 14.
  - Edit: drop it from the load-bearing list, or cite the definition.
- **C6 INFO, `CP:120–123`.** The Case B counts disagree: 4,208 in mut0 versus 4,334 in mut1. Part 1 cannot explain the difference of 126, because H1–H5 and H7 are forced into Case A and H6 contributes at most 30.
  - Edit: state whether the mutation runs regenerate their vectors.
- **C7 INFO, `CP:114`.** The MUT = 5 result is not reported.
- **C8 INFO (optional upgrade).** For H1–H5 and H7 the proof uses (0.2) only at singletons, for the pin, and at Q = Z.
  - Writing out the certification of Z (as done above for H1), plus one complementary pin pair (Q0, Q0ᶜ) such as Q0 = Z with a Zᶜ chain, would make these six exclusions [W].
  - H6 still needs the general argument.

## 5. Unresolved dependencies and gaps

- **SEED theorem and corollary:** no gap. They rely only on the reviewed imports: corrected Lemma H, the Claim, WALL (0.1)/(0.2)/(2.1), and W-ALL.
  - The hypotheses match: avoider, proper Q, β = 0, p ≥ 5 prime, and 3kB ≤ p+4 for W-ALL.
- **SEED Consequences and Remarks:** these rest on c4/proof-NOBCplus-r3 (DOB, NOLIFT), c5/proof-KB0-r2, c5/proof-IND-r2 and c4 README §9.
  - None of these is in the packet, so the KB0/IND deltas and hashes are unverified. They are not load-bearing.
- **CP theorem:** (H) is a per-word hypothesis; there is no uniform (H) theorem. The NMH definition (../README §1) is not in the packet.
- **CP corollary:** three things rest on [F]:
  - (H) for H1–H7;
  - RGR and not-ZSI-B membership;
  - the identification with the c3 "hyp" class (map5 = map3).
- **CP Remark (3):** IND* coverage rests on the cycle-4 [F] receipt.

## 6. Scope and significance

- **SEED with W-ALL:** together they settle exactly the B = 1 all-singleton family W(p, kB), 1 ≤ kB ≤ p−4.
  - The pair seed is a genuine structural lemma: it yields C's (0.2) on this family without (H), even though (H) fails there.
  - It says nothing about item-(iii) words with B ≥ 2 or with excess, or about (H) in general, NMH, RUNS, PAR, INV or ordered Olson.
- **C+:** a one-run sharpening of Theorem C's count, still conditional on (H).
- **Corollary HYP:** a finite, computer-assisted exclusion of seven sampled words.
- **Overall:** these are partial structural results, not a contract breakthrough. No group counterexample is claimed, and none is warranted.
