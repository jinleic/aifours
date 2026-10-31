# Review f187-tuscan-odd-order-t2-exists — review-v1

- Reviewer: ReviewF187TuscanOdd21 (same-harness subagent). Author of the candidate: InfoRecursiveMDS18-2 (info-4).
- Manifest: `manifest-v1.json`, SHA-256 `10b7739be62eee9ec59c183a077eef80b7217cfd33607e7a4b77df0d9d5983d5`. I recomputed it before reading anything else, at 2026-10-29T15:32:23Z, and it matched.
- Native clock observed just before this file was first written: 2026-10-29T09:01:32-0700 PDT.
- Pre-delivery revision history:
  - First written version: SHA-256 `eb8b5c40075b22f71e293511bbd693e70cdc3c4d949b28ccf4c256be8e5a8c62`. It was never delivered.
  - Before delivery I made precision edits in W1, D2, the §4.5 note on row 5, and m3. No verdict or count changed.
  - This header line was added after the clock read 2026-10-29T09:08:51-0700 PDT.
- Limits: this is an independent review inside the same harness. It is not a human review, not an independent-model-family review, not a formal or kernel proof check, and not a novelty assessment. Every computational statement below comes from reviewer-authored code that was actually run. No author code was imported or executed.

## Bottom line

Counts: **FATAL 0 / MAJOR 0 / MINOR 3**. One item is INCONCLUSIVE (table row "B = M"). Several imported statements are marked as not reviewed.

| # | Candidate claim | Verdict |
|---|---|---|
| C1 | The printed 21×21 array is a linear Tuscan-2 square. It is Latin, so an odd-order T2 exists. | **VERIFIED.** No finding. |
| C2 | The lemma "E is always a fixed-point-free involution" is false. At order 21, E has cycle type 7³. | **VERIFIED.** No finding. |
| C3 | In the even-order arrays (n = 4, 6, 8), E is a fixed-point-free involution with cycle types 2², 2³, 2⁴. | **VERIFIED for every T2(4), T2(6) and T2(8)**, using a complete reviewer enumeration. The author's own pinned arrays were not listed, so they were not inspected. |
| C4 | Four other boundary coincidences fail in some arrays (table rows 2–5). | Rows 2–4: **VERIFIED** as "not general laws" by explicit T2(8) squares, and every table cell matches. Row 5 (B = M): **INCONCLUSIVE**, because B is undefined (MINOR m2). |
| C5 | On T2(11): the candidate makes no existence or exclusion claim. The group route is impossible (only Z₁₁). No mod-4 theorem is asserted. | **VERIFIED.** No T2(11) claim is made. The group-route impossibility is proved below. Orders 3 and 7 having no T2 is independently confirmed. Two parts are imported and not reviewed: the CPro1 statement and the routing identity. |
| C6 | Status correction: "none known for odd n > 1" (1990) is outdated. | **VERIFIED** against Ollis 2016. What the 1990 sentence actually says is an import that I did not check. |

## 1. Actual source order and integrity

I read all five listed inputs completely, in the declared order, after verifying the manifest. Hashes, sizes and LF counts were checked with `shasum -a 256`, `wc -c` and an LF count, and checked again inside the receipted control run.

| # | Input (dir `information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/`) | SHA-256 | bytes | LF | match |
|---|---|---|---|---|---|
| 1 | `frontier-20261029-odd-order-t2-exists-and-refuted-boundary-shortcuts-v1.md` (target) | `4f0f07c0…ed29b` | 5393 | 71 | yes |
| 2 | `frontier-20261029-ollis-g21-t2-square-v1.json` (rows) | `4f20ab9a…fb7c3c` | 4055 | 516 | yes |
| 3 | `frontier-20261028-general-t2-check-v1.py` (author checker; read/hash only, **not executed**) | `a534f304…b760e0` | 2166 | 47 | yes |
| 4 | `frontier-20261029-ollis-g21-t2-check-v1.json` (author receipt; data only) | `419cfbab…1ee218` | 831 | 67 | yes |
| 5 | `frontier-20261029-small-and-odd-t2-profiles-v1.json` (profiles; data only) | `2d78d16d…011316` | 3028 | 200 | yes |

Full hashes are in the manifest and in `reviewer-f187-verify-v1-receipt.json` under `integrity:*`. There are no errata, overlays or scope-disposition inputs.

After the five inputs, I read one named public source, which the scope allows to be read directly:

- M. A. Ollis, *Terraces for small groups*, arXiv:1603.01496.
  - Abstract page read via the arXiv API reader.
  - PDF fetched from `https://arxiv.org/pdf/1603.01496` at 2026-10-29T15:36:41Z. The header reads `arXiv:1603.01496v1 [math.CO] 4 Mar 2016`, so v1 is the version served as latest. It has 12 pages and SHA-256 `1164d9d5ab9b601da45ec74500d5045c43c4b31f4b9d71c515c40cc376a62d58`.
  - Read in full, using the `pdftotext -layout` extraction plus a visual check of rendered page 8.

**Not opened:**

- the manifest's `authority` file (it is not an input);
- `frontier-20261028-channel-n4-run-01.json`, `…-n6-run-01.json` and `…-n8-enumeration.json`, which are cited by the candidate and the profiles JSON but not listed;
- any f161/f162 or HELD material;
- any sibling review;
- the CPro1 source and the earlier source-status note.

**Reasoning before computation:** informal reading notes started while I was reading inputs 1–5. No code was written or run, and no verdict was formed, until all five inputs had been read.

## 2. Deviations

**Wave level**

- **W1.** The manifest scope says to verify "the profile table claims for the orders 4, 6, 8 arrays contained in the profiles JSON". The profiles JSON does **not** contain those arrays. It contains only derived per-array profile fields and file-name references to three unlisted files.
  - The candidate's own wording, "per-array data", is accurate; the mismatch is in the manifest.
  - I did not open the unlisted arrays. Instead I recomputed the claims for *every* T2(4), T2(6) and T2(8) by complete independent enumeration (§4.5).
    - This settles rows 1–3 in every column, and row 4 for n = 4, 6 and 21, whichever arrays the author used.
    - Row 4 at n = 8 ("2 of 6") counts over the author's particular six arrays, which I did not inspect. It equals the count over my complete list of six normalized T2(8) squares and the JSON's per-array values.
    - Row 5 is INCONCLUSIVE.

**Reviewer level**

- **D1.** Scratch copies of the public paper were written **outside** the wave directory, in `/tmp/f187-reviewer/`. They are not deleted (no-deletion rule).
  - PDF: SHA as above.
  - `ollis-1603.01496.txt`: `aeb35d4c55c5191cab77c4e0056eb80bf35a1bfc36b04ae9cae33d7c879f323d`.
  - `ollis-p-08.png` (page-8 render): `aa26790c98e46e0b0f8c8cb2271f5512620c0fc4b2f24f5bb24af6ac83ab1da3`.
- **D2.** I ran unreceipted probe runs of my own enumerator binary at the shell before the receipted driver run:
  - n = 3, 4, 5, 6: not clocked. They ran after the binary's 08:49 PDT mtime and before 08:50:56.
  - n = 7: clocked at 08:50:56.
  - n = 8: clocked 08:51:55–08:51:57.
  - The receipted driver re-ran all of them and got the same counts.
  - I also ran one unreceipted exploratory in-kernel computation. It was not clocked; it ran after 08:56:18 and before 09:00:56. It re-ran my binary for stdout only, wrote nothing, and tested 12 boundary-pair guesses for the undefined matrix B. None reproduced the JSON `B_eq_M` pattern.
- **D3.** Beyond the orders the scope names, I also enumerated n = 3, 5, 7. n = 3 is the negative control. n = 3 and 7 also check an imported statement in the candidate (§3.3). I did not attempt any order ≥ 9 (n = 9 and n = 11 are out of scope). No SAT or DRAT was used.
- **D4.** A compiled reviewer binary (`reviewer-f187-t2enum-v1`, Apple clang 17.0.0, `-O2`) is stored in the wave directory as a reviewer-prefixed artifact.

## 3. Controls and receipts (all reviewer-authored, all actually run)

| Run | Clock (PDT) | Exit | Script SHA-256 | Receipt SHA-256 | Elapsed |
|---|---|---|---|---|---|
| `reviewer-f187-verify-v1.py` | START 2026-10-29T08:47:07 / END 08:47:09 | 0 | `97f9447b94dcd59b97be0e41042d68d577d7ee5c0ab12c9881c797eab894bb03` | `reviewer-f187-verify-v1-receipt.json` `c6495278228c047291057ecfd002977e05cccad5184ecf08cdc73bf15207c219` | 1.06 s. 64 checks, 0 mismatches. |
| `reviewer-f187-enum-driver-v1.py` (calls `reviewer-f187-t2enum-v1`) | START 2026-10-29T08:55:41 / END 08:56:18 | 0 | driver `36a28490b51936f315e4a6ce49a34a83ef819ff3db56725790747a59f8b90884`; C source `7f8e6a1e197776896e3bab9bff73a9a3460ab64ce369ebbb26555d8f65b1b1b8`; binary `5ede3da07278852e7a970d8f29d78c0eeeb440afb0bfacee211a65f6ed56bf90` | `reviewer-f187-enum-driver-v1-receipt.json` `348d06667d7c6c33328c7f71803d77d84553e6321395d93f764dc224ed157fa3` | 36.8 s. 54 checks, 0 mismatches. No cap was hit. |

Receipts were written with exclusive create.

**Positive controls (must pass)**

- The 21×21 array: Latin, linear T2, and distance-1 complete.
- Multiplicative Vatican squares (rows `(i·1,…,i·(p−1)) mod p`) of orders 4, 6, 10 and 12 pass as Tuscan-(n−1).
- The Vatican squares of orders 4 and 6, once normalized, are found by the enumerator.

**Intended-reason negative controls (must fail, for the stated reason)**

1. **All 4410 within-row transpositions** of the 21×21 array: every one is rejected. In every case the rows are still permutations and the reason is a repeated distance-1 pair. All 4410 also create a distance-2 repeat.
   - The designated single swap (row 0, columns 4↔5, i.e. 12↔7) gives 3 repeated D1 pairs and 4 repeated D2 pairs.
   - This outcome is forced by theory: in a distance-1-complete array, any transposition creates a new adjacent pair that already occurs elsewhere. For non-adjacent positions p<q this is (x_{p−1},x_q), or (x_q,x_{p+1}) when p=0; for adjacent positions it is (x_q,x_p). So the control demonstrates that the checker is sensitive, not anything specific to this array.
2. Overwriting one entry is rejected with the reason "row not a permutation".
3. Building the same 21 words under the **other** law v u v⁻¹ = u² gives an array that is still Latin but has **105** repeated D1 pairs and **105** repeated D2 pairs. At group level, b⁽¹⁾ has 15 distinct elements out of 20 and b⁽²⁾ has 14 out of 19. The sequence is not even an undirected (Bailey) terrace.
4. Cyclic Latin squares of orders 5 and 21 are rejected with a distance-1 repeat.
5. n = 3 gives 0 solutions in both enumerators. A hand proof: say the row starting with 0 is 012. Then the row starting with 1 must be 102. The row starting with 2 then needs (2,0) and (2,1) and cannot be completed. The case 021 is symmetric.

## 4. Mathematical reconstruction

### 4.1 Definitions used

A linear Tuscan-k square of order n is an n×n array with these properties:

- every row is a permutation of {0,…,n−1};
- for each m ≤ k, every ordered pair (a,b) occurs at most once with b exactly m places to the right of a (no wrap-around).

Ollis (§3, p.7) defines a Roman-k square as a *Latin* square with this property. So Roman-2 implies Tuscan-2.

Every T1 array has the D1-exactness property: there are n(n−1) adjacent slots and n(n−1) ordered pairs, so each pair occurs exactly once at distance 1.

### 4.2 The 21×21 array (C1)

My own checker parsed the rows JSON fully, with duplicate-key detection, and found:

- the label map is 3i+j for u^i v^j;
- every row and every column is a permutation of 0..20, so the array is **Latin**;
- D1: 420 events, 420 distinct, 0 repeats, and **complete** (all 420 ordered pairs occur);
- D2: 399 events, 399 distinct, 0 repeats.

So the array is a linear Tuscan-2 square (Roman-2) of odd order 21. Two further facts, for information only:

- the transpose is also T2, consistent with Ollis's "k-complete";
- distance 3 has 84 repeated pairs, so the array is not T3, and no T3 claim is made.

The author receipt, read as data only, agrees field by field with my computation: input SHA, n, k, counts, empty repeat lists, `first_column` and `last_column`.

### 4.3 Group construction against the public source

- **Presentation.** Ollis §1, p.3 gives `G21,1 = ⟨u, v : u^7 = e = v^3, vu = u^4 v⟩`, i.e. v u v⁻¹ = u⁴. This is exactly the law the candidate uses.
  - My multiplication is (i₁,j₁)(i₂,j₂) = (i₁ + i₂·4^{j₁} mod 7, j₁+j₂ mod 3).
  - Brute force confirms it is associative and non-abelian, and that the relations hold.
- **Terrace.** Ollis §3, p.8 prints `(e, v, u, v², u⁴, u²v, u⁴v², u⁶v², uv, u³, u³v², u², u⁶, u⁵v, u²v², uv², u⁵v², u⁴v, u³v, u⁶v, u⁵)`, followed by "Hence there is a Roman-2 square of order 21."
  - My visual transcription of the rendered page, the `pdftotext` token sequence, and the JSON `terrace_text_as_transcribed` all agree word for word (21 words).
  - The candidate's quotation is exact.
- **Construction.** Ollis states the "(i,j)-entry a_i⁻¹a_j" rule (§1, p.2, Gordon; §3, p.8 for directed T_k-terraces giving k-complete squares).
  - Rebuilding the square from the paper's terrace under the u⁴ law reproduces the JSON `rows` **exactly**, all 441 entries.
  - At group level, under the u⁴ law, b⁽¹⁾ consists of 20 distinct non-identity elements and b⁽²⁾ of 19 distinct non-identity elements. So the sequence is a directed T₂-terrace.
- **Abstract.** The abstract says "a Roman-2 square of order 21 (the first known such square of odd order)". This supports C6.

Why the construction works (my own reconstruction):

- The rows are left translates x·(a₁,…,a_n).
- A distance-m pair (g,h) has g⁻¹h = a_j⁻¹a_{j+m}. When the b⁽ᵐ⁾ are distinct, this fixes j, and then x = g·a_j⁻¹ fixes the row. So no pair repeats.
- The columns {x·a_j} are permutations, so the square is Latin.

### 4.4 The endpoint-permutation lemma (C2)

For any T1 array, D1-exactness means each symbol has a successor in exactly n−1 rows. So each symbol is last in exactly one row, and likewise first in exactly one row.

Therefore E (first symbol of a row ↦ last symbol of that row) is a permutation. It has no fixed points because each row is a permutation and n ≥ 2. A fixed-point-free involution consists only of 2-cycles, so it forces n to be even. Hence "E² = id for every T2(n)" would exclude every odd order.

At n = 21:

- E = [15,19,11,18,1,14,0,4,17,3,7,20,6,10,2,9,13,5,12,16,8].
- Its cycles are (0 15 9 3 18 12 6)(1 19 16 13 10 7 4)(2 11 20 8 17 5 14), so the cycle type is **7³** and E² ≠ id.
- Structurally, E(x) = x·a_n with a_n = u⁵, which has order 7. The orbits are the cosets x⟨u⟩. Both facts were checked in code.

So the lemma is refuted, exactly as claimed.

### 4.5 Boundary coincidences (C3, C4)

**Definitions I used.** Write F, S, P, L for the first, second, penultimate and last columns.

- M = the set of ordered pairs a≠b that do *not* occur at distance 2 (|M| = n in a T2 array).
- C = {(L_r, F_r)}, the closing pairs.
- R = {(P_r, S_r)}.

**n = 21** (verify run):

- S and P are permutations.
- C = M and M = R. In group terms, the unique missing 2-quotient is q* = u² = a_n⁻¹ = a_{n−1}⁻¹a₂.
- All 21 rows have the same sign, giving `row_sign_classes` [21].

These match the JSON `n21_G21` entry on every field that can be recomputed.

**n = 3…8: complete enumeration with two structurally different reviewer implementations.**

- Implementation 1 (C): cell-level depth-first search.
- Implementation 2 (Python): row-level search with bitset forward checking and choice of the most constrained row first.
- Normalization: row 0 = identity and row r starts with r. This loses no squares: in any T2(n) the first column is a permutation (§4.4), so relabelling symbols and reordering rows normalizes any square. Every profile field is invariant under these operations (E is conjugated, the pair sets are relabelled, and all row signs flip together).
- The two implementations return **identical solution sets**:

| n | Normalized T2(n) found |
|---|---|
| 3 | 0 |
| 4 | 1 |
| 5 | 0 |
| 6 | 1 |
| 7 | 0 |
| 8 | 6 |

- The C run took 1.96 s and 133,914,519 nodes for n = 8. The Python run took 34.7 s and 1,533,278 row nodes. Neither hit its cap.
- Every printed solution was re-verified as T2 by a separate checker. The profile key computed in Python equals the one computed in C.
- The solution sets are closed under renormalizing from any row and under reversing all rows.

**Profiles found:**

- Every T2(4): E = 2², Latin, S and P are permutations, C = M, M = R, sign classes [2,2].
- Every T2(6): E = 2³, with the same properties, sign classes [3,3].
- Every T2(8) has E = 2⁴ (a fixed-point-free involution), is **not** Latin, has S and P **not** permutations, and has C ≠ M. Of the 6 normalized squares:
  - 4 have M ≠ R and sign classes [4,4];
  - 2 have M = R and sign classes [8].

**Comparison with the candidate's table:**

- **Rows 1–4 for n = 4 and n = 6:** they hold for *every* T2 of those orders, so they hold for whatever pinned arrays the author used.
- **Rows 1–3 for n = 8:** they hold for every T2(8).
- **Row 4, n = 8 ("2 of 6"):** this equals my 2-of-6 split.
- **Profiles JSON, n = 8:** the multiset of the six recomputable fields equals my multiset exactly. The author's M = R arrays are at indices 3 and 5; mine are at 2 and 5. The orderings differ, but the multisets agree.
- **n = 4 and n = 6 entries:** they equal my unique profiles.

**What this establishes:**

- "S and P are permutations", "C = M" and "M = R" are each violated by explicit T2(8) squares. They are therefore **not general laws**, independently of the author's arrays.
- Row 5, `B = M` "(canonical Latin completion)", is not reproducible. B is not defined in the candidate or in any listed input.
  - The row-5 cells do equal the profiles JSON's `B_eq_M` values (receipted check `md_table_cells_eq_profiles_json_summary`), but that only shows internal consistency.
  - 12 natural boundary-pair guesses (exploratory, D2) failed to reproduce the pattern.
  - The JSON field `e_dist` is also undefined. 14 reviewer guesses (receipted) did not reproduce all of its values.
  - `e_dist` appears in no candidate claim.

**Not a verification of the author's enumeration.** Neither my normalized count 6 nor the matching multiset verifies the author's n = 8 enumeration or its final UNSAT. The candidate correctly leaves that as unverified, and it is out of scope here.

### 4.6 Section 3 statements (C5)

1. **Parity.** Because T2(21) exists, no argument that rules out *all* odd orders can be valid. Any T2(11) no-go must use more than oddness. Correct.
2. **Group route.** A group of prime order 11 is cyclic. The Gordon/Ollis route needs a directed T₂-terrace, which is in particular a sequencing.
   - Suppose Z₁₁ had a sequencing (a₁,…,a₁₁). The differences would be the 10 non-zero residues. They sum to 55 ≡ 0, but they also telescope to a₁₁ − a₁ ≠ 0. Contradiction.
   - This agrees with Gordon's theorem quoted by Ollis (§1, p.2: abelian ⇒ sequenceable iff the group has a unique involution) and with Ollis Table 1, p.10 (d(Z₁₁) = 0).
   - Correct, as restricted to that route. Wording nit: "prime n" should be "odd prime n" (m3).
3. **mod 4.**
   - 21 ≡ 1 (mod 4).
   - "Orders 3 and 7 have none" is independently confirmed by my complete enumerations (0 and 0).
   - "Order 11 is listed as open by CPro1" is an **import that I did not check**.
   - The routing identity ∏_b sign(σ_b) = (−1)^{n(n+1)/2} sign(E) is **not reviewed**: σ_b is undefined in the listed inputs, and the candidate itself says it is not an obstruction. The parity of n(n+1)/2 does depend on n mod 4.
   - No mod-4 theorem is asserted. Correct.
4. **Negative calibration.** The bounded randomized search is labelled UNKNOWN and is not used. No artifact was provided, and I did not review it.
5. **§4.** The statement that T2(11) remains OPEN, with no witness and no contradiction, is consistent. The packet makes no existence or exclusion claim about order 11.

## 5. Per-claim dependencies and conditional imports

- **C1**
  - Depends on: rows JSON `4f20ab9a…`; reviewer checker `97f9447b…`; receipt `c6495278…`.
  - Provenance: Ollis v1 PDF `1164d9d5…`, p.3 (presentation) and p.8 (terrace).
  - Conditional imports: none.
- **C2**
  - Depends on: C1 plus the proof in §4.4.
  - Conditional imports: none.
- **C3 and C4, rows 1–4**
  - Depend on: the enumeration driver `36a28490…`, the C enumerator `7f8e6a1e…`/`5ede3da0…`, and receipt `348d0666…`.
  - Conditional on: the two agreeing reviewer enumerators being correct (same-harness code).
  - The author's pinned arrays were not inspected.
- **C4, row 5:** INCONCLUSIVE (B undefined).
- **C5**
  - Depends on: an elementary proof, Ollis p.2 and p.10, and the enumerations.
  - Not reviewed (imports): the CPro1 status of order 11; the routing identity; the bounded G₂₁ search.
- **C6**
  - Depends on: the Ollis abstract and §3.
  - Import, not checked: the wording of the 1990 Golomb–Etzion–Taylor sentence.

## 6. Findings

- **m1 (MINOR, provenance).** The candidate says "the two possible laws gave different results" and picks v u v⁻¹ = u⁴ because it works. It cites only §3, but the paper fixes this law explicitly in §1, p.3 (`vu = u^4 v`). I checked that the law used is the printed one, so the results stand. Recommendation: cite the §1 presentation.
- **m2 (MINOR, undefined objects).**
  - Undefined terms: the "boundary matrix B (canonical Latin completion)" in table row 5, σ_b in the routing identity, and the "forced circular extension" in §3.1. The profiles-JSON fields `B_eq_M` and `e_dist` are also undefined.
  - Consequence: row 5 and the identity cannot be checked from the packet.
  - Neither affects any other claim.
- **m3 (MINOR, wording).**
  - The count in §4 ("removes four false shortcuts") is ambiguous.
    - It fits the E² lemma plus table rows 2–4, the coincidences that held at both n = 4 and n = 6.
    - The manifest scope instead speaks of the E² lemma plus four other coincidences (rows 2–5).
  - §3.2 says "stops at prime n" where "odd prime n" is meant: Z₂ is sequenceable.
  - Neither affects validity.

## 7. Files created by the reviewer

All files are in `review-waves/f187-tuscan-odd-order-t2-exists/`:

- `reviewer-f187-verify-v1.py`
- `reviewer-f187-verify-v1-receipt.json`
- `reviewer-f187-t2enum-v1.c`
- `reviewer-f187-t2enum-v1` (compiled binary)
- `reviewer-f187-enum-driver-v1.py`
- `reviewer-f187-enum-driver-v1-receipt.json`
- `review-v1.md` (this file)

Scratch files outside the run tree (D1): `/tmp/f187-reviewer/ollis-1603.01496.pdf`, `ollis-1603.01496.txt`, `ollis-p-08.png`.

No Git, no deletion, no publication, no external model, no author contact and no infrastructure change.
