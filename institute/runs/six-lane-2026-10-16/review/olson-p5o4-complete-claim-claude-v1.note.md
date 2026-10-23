# Hostile audit of ROT‑o4 at p = 5 (claim C5)

**Verdict: ACCEPT‑WITH‑FIXES** for the p = 5 slice C5 only.
- C5 stands as a finite, computer‑assisted result, conditional on the imported run receipts.
- Findings: 0 FATAL, 1 MAJOR, 7 MINOR. The MAJOR concerns only the consequences.
- The INV\*‑FEW(a) / OLSON‑FEW(a) lift is **INCONCLUSIVE on this packet** (M1).
- From the inlined text alone, Corollary ROT‑o≤4 follows for every prime p ≥ 5.

Notation: `Sxx:Lnn` means SOURCExx line nn. Nothing was executed. Every ✓ below was recomputed by hand from the inlined text.

## A. Independently audited

**A1. Reduction C5 ⇒ C5′ (S01:L16–28).** The parent states it did not audit this step (S02:L13, S04:L3), so I did.

- **Cyclic shift and conjugation.** Selections in UV and VU correspond one to one. Their products are uv and vu = u⁻¹(uv)u, which are conjugate, so a selection is the identity in one word exactly when it is in the other.
- **PM\* in the exact form used (S01:L20).** I re‑derived it, so nothing rests on the wording of the lowodd text, which is not in the packet.
  - Let w = …R_i σ_a^l R_{i+1} σ_b^m… with l even, and w′ = …R_i R_{i+1} σ_b^{l+m}….
  - Take a selection in w′ that uses j letters of the merged block. Reproduce it in w with the same other letters, plus j′ letters of σ_b^m (j′ ≡ j mod 2) and j−j′ letters of σ_a^l (an even number).
  - Choose j′ = j if j ≤ m. Otherwise choose j′ = m or m−1 to match parity.
  - This is always feasible: j−m ≤ l; if j−m is odd then j−m+1 ≤ l because l is even; and m ≥ 1.
  - The even σ_a part multiplies to e, so the two products agree. Hence w′ solvable ⇒ w solvable.
- **Iteration.** The argument uses neither maximality nor word length, so it can be iterated on non‑maximal representations (S05:L29).
  - Each step keeps the odd‑block count and removes one even block. The process therefore stops at exactly four blocks, all odd.
  - At that point F = 4+2H, R = 14−2H and H ≤ 7. The rotation multiset is unchanged, and reading the word from R₁ places it in D.
- **Robustness.** The same argument works for *any* cyclic constant‑block representation with exactly four odd blocks. So it does not matter whether "maximal" is read linearly or cyclically (S00:L20 vs S06:L9).
- **Runs and blocks.** Runs act as multisets (S02:L36–41), and a selection from a block depends only on the parity of its count. No symmetry pruning is used (S01:L60; none in S03).

**A2. Filter (d): sound, used only to skip, keeps the zero value.**
- **Proof (S02:L48–54).** Take 2k_i letters from each block (Σk_i = j ≤ H) together with positions carrying T. Each block contributes e, and rotations commute.
- **Code.** `filter_d` (S03:L145–163) is an exact existence test: is there T ⊆ M with |T| = 10−2j, j ≤ min(H,5), and ΣT ≡ 0? The value 0 (t₀) is included.
- **Skip‑only.** A "true" from the filter only skips work (S03:L360–364). Avoiders come only from the DP.
- **Zero value kept.** x = 0 is enumerated (S03:L106, L266–279). `rigid` rejects m₀ > 0 and rejects mixed supports {±1}∪{±2} (S03:L166–170).

**A3. The DP is exact.**
- **Group law.** Multiplication is (v+e·v′, e·e′) (S03:L51–52), and TAB is right multiplication (S03:L55–59).
- **Invariant.** After reading a prefix, r[c] is the set of products of c‑letter subsequences. The update runs c downward (S03:L76), so it reads the old r[c−1] and no letter is used twice.
- **Decision.** A word is solved iff e ∈ r[10]; TARGET is 10 in the clean run (S03:L61).
- **Cross‑checks in the code.** The prefix‑shared order (S03:L230–262) matches `build_word` (S03:L102–110). Every DP‑decided representation is re‑decided from scratch (S03:L372). The naive check (S03:L87–100) tries all 43,758 subsets, multiplying left to right.
- **Self‑test.** The relations at S03:L589–597 match the law. "60 non‑commuting ordered pairs" = 100 − 10·4 ✓, since D₁₀ has 4 conjugacy classes.

**A4. Completeness and multiplicities.**
- **Coverage.** The code enumerates:
  - H = 0..7 (S03:L317);
  - C(H+3,3) l‑tuples;
  - all 625 y‑tuples;
  - all C(R+19,19) run‑count compositions over 20 types;
  - all C(R+4,4) multisets in the filter table.
  
  The equalities asserted at S03:L412–415 are the right ones.
- **Binomials ✓.** C(33,14) = 818,809,200; C(31,12) = 141,120,525; C(29,10) = 20,030,010; C(27,8) = 2,220,075; C(25,6) = 177,100; C(23,4) = 8,855.
- **Totals ✓.**
  - Labelled representations: 1,021,369,625,000 for H 0–4 and 1,021,690,650,000 for H 0–7.
  - Classes: 613,973,068,750.
  - DP‑decided: 255,650,000 = 17,600·2,500 + 13,640·6,250 + 7,956·12,500 + 1,232·21,875.
  - Avoiding: 11,120 = 80·4 + 160·10 + 320·20 + 80·35.
  - Sequence‑run, H 0–4: 2,889,994,531,250,000.
- **Survivor families, derived by hand.** They match the 4‑tuple counts at S02:L96–100.

  | H | Surviving multisets | 4‑tuples |
  |---|---|---|
  | 0 | none: 14 elements give a zero 5‑sum twice by EGZ | 0 |
  | 1 | {c⁹,(−c)³} | 4·C(12,3)·C(6,3) = 17,600 |
  | 2 | {c⁹,−c}, {c⁸,(−c)²}, {c⁹,2c} | 4·(880+1,650+880) = 13,640 |
  | 3 | {c⁸}, {c⁷,−c}, {c⁶,−2c,−c} | 4·(165+480+1,344) = 7,956 |
  | 4 | {c⁶}, {c⁵,−2c} | 4·(84+224) = 1,232 |
  | 5–7 | none, all solved by (c) | 0 |

- **No mixed classes.** This is what the accepted GRX predicts: with all l odd, C_max = 2H+Φ (S01:L67).

**A5. Controls checked by hand.**
- **PC‑k2.** It avoids: I exhausted every combination of how many letters are taken from r1⁹, s0⁷, r4 and the final s0. Its o_F is 2, and 6 of its 10 l‑tuples spell it literally.
- **A1 with l = (3,1,1,1).** It avoids: all 8 even reflection‑parity patterns fail. All its runs are non‑empty, so it is a *maximal* o_F = 4 avoider and the slice is not vacuous.
- **N1 (untwisted law).** r1·s0⁷·r4·s0 has v‑sum 5 and 8 reflections, so it equals e.
- **N2 (target 8).** r1·s0⁶·r4 = ρ₅ = e.
- **N3 (parity bug).** Pairs become H+4 ≥ 5, so s = 0 and everything is filtered. N3 therefore only shows the pipeline is sensitive; the filter's soundness rests on A2.

**A6. Count terminology.** The parent's labelled‑representation and raw‑word definitions are correct (S02:L29–32). The worker v2 note relabels its counts correctly (S00:L30–35).

## B. Imported (not verifiable here)

- **Parent runtime.**
  - That `bin/replay_v2` was built from S03 (89abe678…6b68).
  - All runtime values in `summary.json`, including nonrigid = 0, mixed = 0 and no prefix/scratch mismatches.
  - `controls.json`, and the DP plus naive re‑check of all 11,120 avoiding representations. The `check` parser at S03:L782–827 was inspected; its run was not.
  - The Python cross‑checks.
  - That the mapped avoider list equals the worker's `dp_avoiders.txt` (78a91ba2…5967).
  - The full RESULT receipt (7dfe21eb…).
- **Plausibility.** The resource figures look reasonable for about 9.8·10⁸ leaves and 2.6·10⁸ DP representations.
- **Worker side.** Stages G and D, comparator v2, fixtures, mutants and the Codex review (S00:L5–15, L43–55).
- **Route 2.** All of it.
- **Other theorems.** The texts of ROT‑o2/o3/o4, REFL‑few‑odd, INV\*‑FEW(a) and OLSON‑FEW(a).

## C. Findings

**FATAL: none.** On the parent's route I found no incompleteness, false filter, excluded zero value, DP ordering error, multiplicity error or raw‑word miscount.

**M1 (MAJOR, consequences): S00:L61–63; S01:L120–121.**
- **Problem.** The INV\*‑FEW(a) and OLSON‑FEW(a) lifts to p = 5 rest on texts that are not in the packet: REFL‑few‑odd, INV\*, and proof‑OLSON‑few‑v3.md. They also rest on the unverified claim that "Cases 2–3 need INV\* only up to o_F(w)".
- **What the inlined text does support.** Only ROT‑o≤4 for all primes p ≥ 5, assembled from:
  - S05:L9 for o ≤ 2;
  - S05:L32 for o = 0 being impossible;
  - S06:L7 for o = 3 at p ≥ 5;
  - S06:L8–10 for o = 4 at p ≥ 7;
  - C5 for o = 4 at p = 5.
- **Fix.** Before recording the lift:
  1. Pin the accepted INV\*‑FEW(a), REFL‑few‑odd and OLSON‑FEW(a) statements by hash.
  2. Show that ROT‑o4 at p = 5 (S06:L11) was the *only* reason p = 5, o_F = 4 was excluded. In particular, show that "o_F ≤ 4 ≤ p" admits p = 5 without needing any p ≥ 7 lemma.
  3. Check that every INV\* call in Cases 2–3 at p = 5 is applied to a word with o_F ≤ 4. If a case deletes or inserts letters, block parities can change; for example, deleting one letter from an even block raises o by one.
  
  Otherwise record the lift as "conditional, unaudited".

**m1: S02:L158.** "A full no‑filter check is §7" contradicts S02:L195–202, where H = 2 and 3 (152,938,500,000 representations) are UNKNOWN.
- Replace it with: "A partial, optional no‑filter check (H = 0, 1, 4–7 complete; H = 2, 3 UNKNOWN) is in §7. It is not a premise; (d) is proved in §2."
- The verdict must cite route 2 for nothing.

**m2: S02:L13; S04:L3.** The parent replay establishes only C5′. The verdict must state C5 as: PLAN‑v1 §2 (S01:L16–28) + PM\* (S05:L8, L29) + the parent's C5′. It must also name who audited the reduction; A1 above re‑derives PM\* in the S01:L20 form.

**m3: S00:L38–39; S01:L86.** PC‑k2 is presented as a positive control without saying that it has o_F = 2 and lies in D only through non‑maximal splittings (S02:L143–148).
- The same holds for A2, where S₄, S₁ and S₂ merge.
- State this, and cite A1 or A3 (all runs non‑empty) as the maximal o_F = 4 witness.
- Optional extra check: classify the 640 avoider classes by maximal o_F. The o_F = 0 group must be empty (S05:L32).

**m4: S03:L12, L432–438, L447–449; S01:L54; S02:L113–114.**
- The fields `words_*`, `avoider_words`, `nonrigid_avoider_words` and `literal_words` count labelled representations.
- `literal_words` in particular counts sequence‑run representations, which still repeat literal words (PC‑k2 appears 6 times). "Words up to (R3)" at S01:L54 has the same problem.
- Fix: add a legend to RESULT using the S04 names, and quote only representation counts in the verdict. At S02:L113–114, say that C(R+3,3)·5^R is per H, before multiplying by C(H+3,3)·625.

**m5: S03:L360, L412–415 (fail‑closed hygiene).**
- `fv != 0` treats an unset entry (−1) as "(d)‑solved". This cannot actually happen: every multiset with |M| = R is filled, and ms_total = C(R+4,4) is asserted. Still, use `fv == 1` and abort on −1.
- The `ok` check does not assert nonrigid = 0 or mixed = 0, so C5′ is read off output fields rather than enforced.
- Fix: pin the SHA‑256 of `nonrigid_avoider_classes.txt` and `mixed_classes.txt`, which should be the empty‑file hash e3b0c442…b855. Also pin `avoider_classes.txt` and `summary.json` from enum‑clean‑v2.

**m6: S03:L9; S02:L62–63, L79–81, L196–200 (provenance).**
- The v2 source's build comment names `replay_v1` and `_v1.cpp`. Record the actual v2 build command, compiler version and binary hash 4bb26b02…1cf8, and say which binary produced enum‑clean‑v2.
- An unexplained external SIGTERM hit during route 2. Record the route‑1 run times relative to it and re‑hash the route‑1 outputs against the RESULT pins.
- A fresh route‑1 rerun (about 26 s) into a new O_EXCL directory, compared byte for byte excluding timing fields, is cheap and recommended.

**m7: S02:L60–75, L84–85 (independence wording).**
- The replay is an *unblinded*, independent *implementation* of the same method as worker Stage D (the P1′/(d) filter plus ordered DP). It is not an independent method.
- The shared‑method risk is limited to (d) and the DP idea, both proved or inspected here in A2–A3.
- Fix: describe it as "independent implementation; plan‑time counts seen".

## D. Scope decision

**Established, after fixes m1–m7.** The basis is the written reduction (audited in A1) plus the parent's complete H = 0..7 verification (code audited in A2–A4; runs imported).
- Every length‑18 word over D₁₀ with no identity ordered 10‑subsequence and exactly four odd maximal constant reflection blocks has all its rotation letters in one set {ρ_c, ρ_−c}, c ≠ 0.
- By A1, the same holds for any cyclic constant‑block representation with exactly four odd blocks.
- Combined with S05 and S06, Corollary ROT‑o≤4 now holds for every prime p ≥ 5.

This is a fresh computation. It does **not** validate the historical D10 census, which stays unaudited and unused (S06:L11; S00:L59–60; S01:L130–133).

**Not established:**
- the INV\*‑FEW(a) and OLSON‑FEW(a) lifts (pending M1);
- INV\*(5) for o_F ≥ 5;
- ROT with five or more odd blocks (S06:L36);
- any claim about reflection structure;
- ordered Olson for D₁₀ or D₂ₚ;
- novelty.

Route 2 is optional, partly UNKNOWN, and supports nothing.
