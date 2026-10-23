DISPOSITION: ACCEPT-WITH-FIXES

## Basis and summary

I audited only the quoted Tan–Zhou lines, `check_ingredients.py` and `build_c23.py`. The following are *reported by parent* and were not rerun:
- the certificate bytes and their SHA;
- the verdicts of all three checkers;
- the corruption and control runs;
- the byte-identical rebuild;
- the I2 file.

Neither the generic checker's code nor any I2 checker is in the packet, so (a) audits the predicate as stated, not an implementation. At most, the reports establish that predicate on the pinned bytes. They establish nothing about I2, Lemma 3.4, Corollary 2.6 or §4(2).

**By claim:**
- **(1)** Accepted on the reported runs. The stated predicate is equivalent to the source's definition.
- **(2)** Cannot be checked from the excerpt (M1).
- **(3)** The arithmetic and logic are correct for m = 32. It depends on unquoted source results (M2) and lacks an exceptional-order caveat (M3).
- **(4)** The assembler is a faithful instance of Construction 2.3.

There are no FATAL findings.

## (a) Predicate vs. definition

1. **CQS layer.** s = 0 gives S = ∅. Lines 262–266 (t = 3, K = {4}) then say exactly:
   - four groups of 32 partition the 128 points;
   - every block is a 4-subset;
   - every triple not inside a group lies in exactly one block;
   - no triple inside a group lies in any block.

   Check: C(128,3) − 4·C(32,3) = 341376 − 19840 = 321536 = 4·80384.

   This is the candelabra convention: triples with two points in one group must be covered. The object depends on it. I2's blocks covering {(a,i),(a,j),(b,k)} become blocks that meet a big group twice. A transverse-only (H-design) checker would therefore wrongly reject this object.

2. **The incomplete-STS pair conditions follow from the triple conditions.** Fix x ∈ G and let H := G∖{x}.
   - A ↦ A∖{x} is injective on blocks through x.
   - {y,z} lies in a derived triple iff {x,y,z} lies in a block.
   - {x,y,z} ⊆ G iff {y,z} ⊆ H.

   So the triple predicate gives exactly a GDD(2,3,127) of type 1^96 31^1 with H as the long group, i.e. an STS(127,31) (line 215). Nothing extra needs checking. Count: (C(127,2) − C(31,2))/3 = 2512.

3. **r and s.** 127 ≡ 1 (mod 6) and 127 ∉ {7,13}. Hence r = χ′(127) = 64, and s = r − (v−h)/2 = 64 − 48 = 16 = (h+1)/2 (lines 216–223).
   - The only import is the value of χ′(127) from (1.1)/[19].
   - That import can be weakened. 2667/42 > 63 gives χ′(127) ≥ 64. Filling H with any 16-colourable STS(31) inside the 16 hole-free classes gives χ′(127) ≤ 64.

4. **"Nonempty" and "exactly 16" are forced, not extra conditions.**
   - A hole point has degree 96/2 = 48 and cannot lie in a hole-free class. So at least 48 classes are non-hole-free, and at most 16 are hole-free.
   - Hence "≥ 16 hole-free" and "= 16 hole-free" are the same condition, and every hole point lies in every non-hole-free class.
   - Class sizes are at most 42 (127 = 3·42 + 1) for non-hole-free classes and at most 32 (96 points) for hole-free ones. If a hole-free class were empty, the total would be at most 48·42 + 15·32 = 2496 < 2512. So all 16 hole-free classes are nonempty.

   **Conclusion: predicate ⇔ definition.**

5. **All points.** There is no stem, so condition (2) (line 293) is vacuous. Condition (1) applies at all 128 points, which is what was checked.

**Caveat (cannot be verified here).** The equivalence needs the checker to fix 64 and 16 from (v, g, s), not from the `COLOURS`/`HOLEFREE` header. It must already identify hole-free classes by content: `build_c23.py:95-96` puts 12 of the 16 hole-free classes (those with y ∈ G(x)∖{x}) at positions that depend on x.

**Consistency with reported data.** The reported class-size profile 42^48 32^12 28^4 is exactly what the construction predicts:
- 42 = 10 + 4·8;
- 32 = 4·8;
- 28 = 4·7.

This forces I2's class sizes to be 10^12 7^4 at every point.

## (b) Construction 2.3

**Inputs.**
- (m,g,n,s) = (8,4,4,0).
- mgn+s = 128 and mk₁+s = 32 are both ≡ 2 (mod 6). This is the case the source proves itself (line 456).
- m is even.
- Part (2), for α ∈ S, is vacuous at s = 0.
- The excerpt's "gcDCQS(mk1 : s)" means gcDCQS(m^{k₁}:s) (compare line 460).

**The union is a CQS(32^4:0).** This is line 490's "routine" step. Take a triple of Y and look at its X-coordinates:
- **Three distinct a, b, c.** {a,b,c} lies in exactly one member of G, B or T.
  - In G: a big-group triple, correctly uncovered.
  - In B: covered once by A_B.
  - In T: covered once by D_T.
- **{a, a, c}.** The pair {a,c} lies in exactly one member of G or B.
  - In G: the triple is inside a big group.
  - In B: A_B covers it once, and D_T cannot (D_T blocks are transverse).
- **{a, a, a}.** Inside a big group.

Also |B∩G| ≤ 1 and |T∩G| ≤ 2, since otherwise a G-triple would be covered again. So no block contains a big-group triple. Count: 16·1184 + 48·1280 = 80384.

**The relabelling and colouring match the source** (lines 459–539):
- `build_c23.py:49,55` send I2 group t to {B_t}×I₈ and FDH group s to {a_s}×I₈, which is H_B.
- `:69` and `:85` take the preimage of (x,i).
- Hole-free A-classes are identified by content (`:72`). The counts are asserted as 4 = (m+s)/2 and 12 = (|B|−1)m/2 (`:74`).
- The 12 non-hole-free classes go bijectively onto (B∖{x})×{0..3} (`:76-78`).
- Each FDH class goes to y = T[missed group], with j indexed per T (`:86-94`).
- F^j is built from the hole-free A-classes (`:79-80`).
- Totals: 15·4 + 4 = 64 classes, of which 3·4 + 4 = 16 are hole-free.

**Why the unions are disjoint.** Only containment is used.
- **y ∉ G.** A_{B₁}^{y,j} ⊆ (B₁×I₈)∖{(x,i)} and D_T^{y,j} ⊆ (T∖{x,y})×I₈. B₁∩T = {x,y}, and T∩T′ = {x,y} for distinct T, T′ ⊇ {x,y}. (A third common point would put a triple twice into G∪B∪T.) So these pieces are pairwise disjoint.
- **y ∈ G∖{x}.** T∩G = {x,y}, so each D_T^{y,j} avoids G×I₈. Disjointness follows as above.
- **F^j.** A_B^j ⊆ (B∖{x})×I₈, and distinct B ∋ x meet only in x.

Every ingredient class is used exactly once, and each derived triple determines its block. So the 64 classes partition F(x,i).

**Arbitrary assignment of non-hole-free classes is permissible.** The proof uses only A_{B₁}^{y,j} ⊆ B₁×I₈, so any bijection onto (B₁∖{x})×[4] works. Bijectivity itself is forced:
- By (a)4 applied to I2, each non-hole-free class contains all 7 points of {x}×(I₈∖{i}).
- So two such classes cannot share a slot.
- A slot with y′ ∉ B₁ would collide with A_{B₁′} on those points.

Likewise, two D_T classes that miss the same group have the same support, so the per-T indexing must be a bijection. It is (`:94`).

**Ingredient checkers.**
- **`fg` (`check_ingredients.py`)** implements lines 252–259 exactly:
  - four groups of size 4;
  - Steiner-2 on G∪B;
  - Steiner-3 on G∪B∪T;
  - block sizes {4} and {5}.

  Transversality of B and |T∩G| ≤ 2 follow from these, so they are rightly not checked. The description "AG(2,4) lines + 5-arcs" is forced (given uniqueness of AG(2,4)) and is descriptive only.
- **`fdh`** implements lines 241–251 exactly, under the transverse reading forced by line 246 (the derived design has groups G∖{G}):
  - blocks are transverse;
  - transverse triples are covered once;
  - at all 40 points the classes partition the derived design;
  - each class is a parallel class of X∖(G_x∪G′).

  The "4 classes missing each group" counts are forced, since 12 = 16 − 4. `miss` (`:98,:109`) is dead code.
- **No I2 checker is supplied.** `build_c23.py:74` only checks counts. This does not affect (1), but it does affect any claim that the pinned ingredients are valid.

## (c) Bridge

**Order 128: Construction 2.1 with (g,n,s) = (32,4,0).**
- 128 ≡ 2 (mod 6), the case the source proves itself (line 300). The stem-point part (lines 318–335, partly garbled in the excerpt) is vacuous at s = 0.
- Inputs: the certificate, mcDSQS(32) and gcDSQS(32,0).
- With h = 0, SQS(v,0) = SQS(v) and the hole-point condition is vacuous. So gcDSQS(32,0) = mcDSQS(32). Cor 2.6 drops this third hypothesis at s = 0, which supports the convention.
- Proof at x ∈ G (lines 326–330): 16 merged classes P∪Q plus 48 classes P give 64 = χ′(127). This needs χ′(31) = (g+s)/2 = 16, which holds because 31 ∉ {7,13}.
- Imports: **Lemma 3.4 (unquoted)** and (1.1)/[19] only. Neither 2-RSQS* nor RDTD is needed.

**n ≥ 4: Cor 2.6 with m = 32.**
- 32 ≡ 8 (mod 12).
- 32·4^t ≡ 2·4 ≡ 2 (mod 6). The derived orders 2^{2t+5} − 1 ≥ 511 are ≡ 1 (mod 6) and not exceptional.
- Reindexing: 32·4^t = 2^{2(t+2)+1}, so n = t + 2, and t ≥ 2 ⇔ n ≥ 4.
- Imports. The proof is not quoted, so these are inferred from its hypotheses:
  - Thm 2.5(1) [21, Cor 3.2]: a 2-RSQS*(4^t) for t ≥ 2;
  - Thm 2.5(2) [9,21]: an RDTD(3,4,32), since gcd(32,4) = 4 ≠ 2 and gcd(32,18) = 2 ≠ 3;
  - the source's Construction 2.4 (unquoted);
  - Construction 2.1 with (32, 4^t, 0);
  - Lemma 3.4;
  - [19].
- The source is arXiv v1. The packet shows no refereed version.

**Exceptional order.** On this path the only exception is derived order 7, i.e. m = 8. Cor 2.6 as stated admits it, since 8 ≡ 8 (mod 12).
- Construction 2.1 (line 311) needs the derived STS(g+s−1) resolved into (g+s)/2 classes. This fails when g+s ∈ {8,14}.
- In a gcSTS(8·4^t − 1, 7), each hole point has degree r − 4, so it lies in every non-hole-free class.
- The 7 pairwise-intersecting STS(7) blocks therefore have only 4 hole-free classes available.
- So Construction 2.1 and Cor 2.6, as quoted, are missing the hypothesis "g+s ∉ {8,14}" (equivalently m ≠ 8).

This matters directly for the packet:
- I2 *is* a gcDCQS(8^4:0), and mcDSQS(8) exists trivially because χ′(7) = 7.
- So a literal reading of Cor 2.6 would give mcDSQS(2^{2n+1}) for every n ≥ 3 without the 32^4 certificate.
- The m = 32 route is unaffected.

As bookkeeping only: with n = 1 trivial and n = 2 from Lemma 3.4, the chain covers every n ≥ 1, conditionally on the imports.

## (d) Significance

- **What it is.** An explicit, pinned, independently checkable gcDCQS(32^4:0). If M1 confirms the wording, it settles the m = 32 instance that §4(2) asks for.
- **Structural reading.** m = 8 cannot seed the source's recursion because of the STS(7) exception. Construction 2.3 with g = 4 turns the unusable m = 8 ingredient into m = 32. 20 and 32 are the first two non-exceptional m ≡ 8 (mod 12), which plausibly explains why §4(2) names them; this is unverified.
- **Limits.**
  - The object is a direct instance of the source's own construction, so it contributes no new method.
  - The consequences are mechanical and conditional on Lemma 3.4 and Cor 2.6.
  - The family has density zero in v ≡ 2 (mod 6) and leaves the general spectrum untouched.
- **What decides whether it is more than bookkeeping.** The provenance of I2 and I3, which the packet does not disclose.
- **Pitch.** Specialist interest (colourings of SQS derived designs), at the level of a short note or computational addendum. "Infinitely many orders" is not significance on its own.

## Findings

**FATAL:** none.

**MAJOR**

- **M1. §4(2) is not in the excerpt.** §4 is quoted only up to line 1117.
  - Fix: quote §4(2) verbatim with line numbers.
  - Fix: restate (2) as "settles the m = 32 (order-128) case" only if the wording supports that. If §4(2) asks for mcDSQS orders, say the answer goes through Cor 2.6 and Lemma 3.4.
  - Fix: write "m = 32 (v = 128)" instead of "v=32".
  - Fix: mark m = 20 as reported elsewhere and not audited.
  - Fix: state what priority check was done.
  - Effect: (1) is unchanged; (2) is unsupported until this is fixed.

- **M2. Load-bearing source results are not quoted.** Lemma 3.4 is the only source of mcDSQS(32), which both consequences need. Cor 2.6's proof chain is inferred, not quoted.
  - Fix: quote Lemma 3.4 and the proof of Cor 2.6.
  - Fix: list the imports as in (c).
  - Fix: note that the source is arXiv v1.
  - Effect: (3) is conditional on these imports until they are supplied.

- **M3. The m = 8 exception is not addressed.**
  - Fix: cite Construction 2.1 and Cor 2.6 with the tacit hypothesis g+s ∉ {8,14} (m ≠ 8).
  - Fix: include the four-hole-free-classes argument showing why I2 + mcDSQS(8) does not already give the family.
  - If the source handles m = 8 some other way, then (3) adds nothing and (d) must say so.
  - Effect: (1) is unchanged; this can change what (3) contributes and the assessment in (d).

**MINOR** (none of these changes a conclusion)

- **m1. Checker documentation.**
  - State that 64 and 16 come from (1.1), not from the header, and that hole-free classes are found by content.
  - List the 23 corruption reasons. Include header tampering and hole-free-class tampering among them.
  - Replace "52 third-checker runs expected" with an explicit tally of passes and rejections.
  - Pin the checker SHAs and include the generic checker's source.
- **m2. Symbol clash.** s means both the stem size (0) and the hole-free class count (16, or 4 in I2). Write s_H for the latter.
- **m3. Wording.**
  - "PPCs avoiding x" → "PPCs of X∖{x}".
  - "16 classes avoiding G(x) minus x" → "16 of them PPCs of X∖G(x)".
  - "triples … occur once" → "lie in exactly one block, including triples with two points in one group".
  - "point profile" → "class-size multiset at each point".
  - Report I2's profile, 10^12 7^4.
- **m4. Line citations.**
  - `check_ingredients.py:4`: 248–255 → 252–259.
  - `check_ingredients.py:7`: 241–247 → 241–251.
  - `build_c23.py:2`: 444–541 → 451–541. Lines 444–449 belong to the previous proof.
  - `build_c23.py:13`: 495–531 → 503–539.
  - Restore the superscripts in the transcription.
- **m5. Code details.** `build_c23.py:15` says "label order", but `:75` sorts by 1-FG point id; say which is meant. Delete `miss` or assert its counts.
- **m6. Ingredients.** Supply the I2 checker and the provenance of I1–I3.
- **m7. Convention.** State the h = 0 convention gcDSQS(32,0) = mcDSQS(32) explicitly in (3).
- **m8. Independence.** The checkers are independent in code but not in specification. State the predicate explicitly, as in (a), so it can be audited separately from the code.
