# Audit of SOURCE00 (p = 5 lift, v3): L-INV and L-OLS at o_F ≤ 4

**Verdict: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 5 MINOR.**

- §§3–4 are a correct combination, conditional on the parent-accepted statements below.
- One of those statements is C5, which is computer-assisted and finite exact.
- The five fixes are citations and wording only. No statement, call or bound changes.
- I executed nothing. Every check in A was done by hand from the inlined text.

## A. Audited

**A1. Accepted p-scopes, taken from verdict statements only.**
- Accepted for every prime p ≥ 5:
  - INV*-FEW(a) and OLSON-FEW(a) at o_F ≤ 3 (SOURCE07:6-7).
  - ROT-o2, with o = 0 impossible (SOURCE10:9, 32).
  - ROT-o3 (SOURCE11:7).
  - REFL-few-odd at o_F ≤ p (SOURCE09:6).
  - RGR-LONG (SOURCE12:7).
  - K0* and small-k (SOURCE13:7; SOURCE14:3).
- C5 is accepted at p = 5 (SOURCE06:3, 6).
- The only input restricted to p ≥ 7 is ROT-o4 (SOURCE11:8-11). The fewodd verdict names it as the sole reason for the exclusion (SOURCE07:9).
- C5 is ROT-o4's accepted statement (SOURCE11:9) specialised to p = 5: length 18, D_10, exactly four odd maximal constant blocks, and no run-constancy hypothesis.
- So the scope argument follows from the verdicts alone. SOURCE00's §2.1 searches corroborate it but are not a premise.

**A2. L-INV (SOURCE00:163-173).**
- Rotations: ROT-o2 covers o ∈ {1,2}, ROT-o3 covers o = 3, and C5 covers o = 4. Equivalently, use ROT-o≤4 (SOURCE06:8).
- o = 0 is impossible:
  - If F = 0, EGZ in Z_5 gives two disjoint zero-sum 5-sets among the 18 rotations. Rotations commute, so their product is the identity.
  - If F > 0, SOURCE10:32 applies.
- Reflections: the REFL interface (SOURCE03:110-114; SOURCE04:117-121) holds.
  - (0) p = 5 is prime.
  - (a) |w| = 18.
  - (b) The rotations lie in the pair just found, with c ≠ 0.
  - (d) o_F ≤ 4 ≤ 5.
- This is exactly SOURCE01:30-36 with ROT-o4 replaced by C5. Its only other p-dependent step is "o_F ≤ 4 ≤ p" (SOURCE01:35).
- The three texts define o_F the same way (SOURCE01:14-15; SOURCE03:15-19; SOURCE06:6; cf. SOURCE05:25).

**A3. Case 1, R ≤ 2 (SOURCE02:31-36; SOURCE00:154, 214).**
- Pair count:
  - F ∈ {17,18,19} and F ≡ o (mod 2).
  - F = 17 forces o ≤ 3, and F = 18 allows o ≤ 4. Either way F − o ≥ 14.
  - So Σ⌊l_i/2⌋ = (F − o)/2 ≥ 7 ≥ 5.
- If R = 0 and all reflections are equal, σ_y² = 1 gives the identity directly.
- Otherwise:
  - Frame the word at a rotation letter, or at a value change if R = 0.
  - No block contains the cut, so the pairs are linearly adjacent and 5 of them multiply to 1.
- Moving from the frame VU back to UV changes the product vu to uv = u(vu)u⁻¹, a conjugate. The identity is therefore preserved (SOURCE12:49).
- No INV* call is made.

**A4. D1 (SOURCE00:181-183).**
- Deleting one letter from an odd block S with |S| ≥ 3 leaves |S| − 1 ≥ 2 letters, an even count.
- No rotation run changes, and S still separates its neighbours, which are unchanged. So S stays maximal.
- Hence o_F(w′) = o − 1 exactly, including when S wraps around the end of the word.

**A5. D2 (SOURCE00:184-194).**
- If x_i's run stays nonempty, nothing changes.
- If x_i was alone in its run, another rotation run exists (R ≥ 3). So its neighbours X and Y lie in different reflection runs.
  - X and Y with different values: they stay separate blocks across a legal empty run (SOURCE03:19-20).
  - X and Y with equal values: they fuse. Odd+odd gives even (Δ = −2); odd+even and even+even give Δ = 0.
- There is no cascade. Each outer neighbour of the fused block was already separated from X (or Y) by a nonempty rotation run or a value change, and the deletion does not touch those boundaries.
- So o_F(w_i) ∈ {o, o−2} ≤ 4.
- A deletion from an even block (+1) is never made (SOURCE00:195-202).
- Wrap-around at positions 19→1 behaves the same, because o_F and adjacency are cyclic.

**A6. Reconstruction (SOURCE02:38-39, 43-46; SOURCE00:204-208).**
- Case 2:
  - w has the same rotations as w′.
  - The reinserted σ_y sits inside S′, which lies in a constant run of w′.
  - So w is RGR.
- Case 3, rotations: some x_3 ∉ {x_1, x_2} lies in both w_1 and w_2.
  - This forces ±t ∈ {±c_1} ∩ {±c_2} with t ≠ 0, so the two pairs coincide.
  - x_1 lies in w_2 and x_2 lies in w_1, so every rotation of w is in that common pair.
- Case 3, reflections:
  - With R ≥ 3, a non-constant run of w is not the whole cycle, so it contains two cyclically adjacent unequal reflections.
  - Deleting a rotation keeps them adjacent in w_1, which contradicts w_1 being RGR.
- Every insertion happens after the calls on its word. No INV*, ROT or REFL statement is applied to an inserted word.

**A7. Call inventory (SOURCE00:212-225).** Every row is correct.
- Case 2 calls INV*-FEW(a) at o − 1 ≤ 3 (SOURCE07:6).
- Case 3 calls INV*-FEW(a) at o_F ≤ 3, or L-INV at o_F = 4.
  - The o_F = 4 call only happens when o = 4.
  - It is the only use of C5.
- Every REFL call is at o_F ≤ 4 ≤ 5.
- RGR-LONG(5) is applied only to w, and only after w is shown RGR.
  - Its statement carries no o_F or inherited hypothesis (SOURCE12:7). DR-Res derives the inherited conditions itself (SOURCE12:49).
  - The caveat at SOURCE10:41 is respected.
- Branches with o_F = 0 close at once by ROT-o2.
- Case 1 covers R ≤ 2 and Case 3 covers R ≥ 3, so Case 2 is optional (SOURCE02:40).
- There is no circularity:
  - C5's basis imports no INV* or OLSON statement (SOURCE06:11-17, 29).
  - REFL uses no rotation-rigidity result (SOURCE03:70).

**A8. k ≤ p and exclusions (SOURCE00:227-237).**
- REFL's caller obligations are exactly (0), (a), (b), (d) (SOURCE04:116-124).
- Inside REFL, the terminal RES_< word has k ≤ o_F(w0) ≤ 4 ≤ 5 by MON (SOURCE04:82-87). Small-k excludes it at every prime p ≥ 5 (SOURCE14:3).
- The SHgen-E obligation to carry k ≤ p binds only SHgen-E callers (SOURCE09:16; SOURCE03:125-129). Part (a) never calls SHgen-E (SOURCE01:30-36; SOURCE02:28-47).
- The RUNS split at o_F ≤ p is internal to RUNS (SOURCE12:47).
- No part (b) or SHgen input enters.
- The historical D10 census is not used:
  - C5 rests on a fresh computation (SOURCE06:27; SOURCE05:150).
  - REFL uses no finite computation (SOURCE03:71).
  - Finite aids are not premises of RED or K0* (SOURCE13:44-45).

**A9. Pins and metadata.**
- Every hash SOURCE00 gives for an inlined file matches that file's header.
- The cross-pins match SOURCE06/07: PLAN, RESULT/NOTE, the comparator, code-result, the worker note and the reviews.
- I hand-checked the §2.1/2.1a entries that fall in inlined files against both regexes. They are consistent, apart from MINOR-2.

## B. Imported, not verified here
- C5's correctness. This covers the computation, runtime outputs, byte identity and the replay (SOURCE06:11-17). The PM* reduction was audited in SOURCE05 A1, not here.
- The internal proofs of the accepted inputs: ROT-o2/o3, REFL-few-odd (MON, RED, K0*, B0S, MXG), RGR-LONG, and INV*-FEW/OLSON-FEW(a) at o_F ≤ 3.
- Search results over files not in the packet, the script check (SOURCE00:408-410), and the hashes of absent files.
- Quotes from reviews not in the packet (SOURCE00:129-131, 193).

## C. Findings

**FATAL: none. MAJOR: none.**

**MINOR-1 (SOURCE00:54, 57, 84).**
- The ROT-o3-v4 and ROT-o4-v4 rows say "accepted by … same verdict".
- SOURCE11:7-8 pins only o3-v3 and o4-v2/v3. No v4 hash appears there.
- SOURCE00:84 checks C5 against v4 L121-122, a file not in the packet.
- This is not load-bearing.
- *Repair:* label the v4 files as unpinned errata successors, as SOURCE00:49 already does for r5. Cite SOURCE11:9 for the ROT-o4 statement.

**MINOR-2 (SOURCE00:117).**
- Row 3 files INV*-FEW L146 as a quote of L54-55.
- SOURCE01:146 is actually the diff copy of the statement at SOURCE01:22, which is row 1.
- The set of hits is unaffected.
- *Repair:* move L146 to row 1.

**MINOR-3 (SOURCE00:157-161, 166, 193, 236).**
- Four claims that look load-bearing cite material not in the packet:
  - "By 2.1 none of these texts…";
  - ROT-lowodd-v1 L86, for F = 0;
  - the chain-review L22 quote;
  - PLAN-v1 L22-25.
- Each one is redundant:
  - SOURCE09:6, SOURCE13:7 and SOURCE14:3 give the scopes.
  - EGZ, or SOURCE10:9 and 32, give o = 0.
  - D2 is re-derived in A5.
  - SOURCE05:23 gives the end of the reduction.
- *Repair:* cite the verdict lines instead, and label §2.1/2.1a and the review quotes as supporting.

**MINOR-4 (SOURCE00:206-207).**
- "Hence in their common pair" assumes the third-rotation step at SOURCE02:43-44 without stating it.
- *Repair:* state it: x_3 lies in both w_1 and w_2, and since t ≠ 0, {±c_1} = {±c_2}.

**MINOR-5 (SOURCE00:20, 247 vs SOURCE06:25).**
- The note waits for "the narrow Codex review requested by the parent".
- The parent verdict says only "until the requested lift note is reviewed (Claude M1)".
- *Repair:* align the wording. This audit is one Claude review, and the parent decides.

## D. Previous M1 (SOURCE05:97-110): resolved
1. **Statements pinned by hash.** SOURCE00:46-50 match SOURCE07:12 and SOURCE09:6, and the texts are now inlined as SOURCE01-04.
2. **ROT-o4 was the only reason for the exclusion.** Shown in A1 from verdict statements (SOURCE07:9; SOURCE11:8-11). "o_F ≤ 4 ≤ p" needs no lemma restricted to p ≥ 7 (SOURCE01:35; SOURCE09:6).
3. **Every INV* call is at o_F ≤ 4.** Case 2 calls at o − 1 and Case 3 at o or o − 2. There is no even-block deletion and no insertion before a call (A4-A7).
   - The open premise at SOURCE05:98, "Cases 2–3 need INV* only up to o_F(w)", is now verified.
   - The earlier INCONCLUSIVE was a limitation of that packet, not a defect in the argument.

## E. Scope

**Established**, conditional on the accepted inputs, including the computer-assisted C5:
- At p = 5, every length-18 avoider over D_10 with o_F ≤ 4 satisfies INV*.
- Every length-19 word over D_10 with o_F ≤ 4 has an identity 10-subword in increasing index order.
- Together with SOURCE07:6-7, part (a) of both corollaries then holds with o_F ≤ 4 for every prime p ≥ 5.

**Not established:**
- INV*(5) or ordered Olson for D_10 with o_F ≥ 5;
- ROT with five or more odd blocks;
- complete D_10 or general ordered Olson;
- novelty.

The historical census stays unaudited and unused.
