# Hostile model review: (A) pc100 reduction and (B) mcDSQS(38) construction note

This is a model review from the supplied snapshot only, not peer review. I did not rerun any certificate, seed, symmetry or mutation check. Certificate facts are quoted from the supplied JSON as reported. Every step of (A), and every group and arithmetic statement in (B), I re-derived by hand. For (B) I use the definition as you supplied it: χ′(37) is the minimum chromatic index over all STS(37).

| | Verdict | Mathematical errors | Bridge from checked data to the source definition |
|---|---|---|---|
| (A) | **ACCEPT-WITH-FIXES** | none found | sound, and does not depend on Theorems A–D |
| (B) | **ACCEPT-WITH-FIXES** | none found | sound, and self-contained once B1 is applied |

No finding blocks either verdict. They concern how hypotheses are stated, how claims are scoped, and provenance.

---

## (A) Point-cyclic 2-(100,4,1): reduction to eight base blocks

### Re-derivation of the load-bearing chain

**Block stabilizers (Lemma 2).**
- Stab(X) acts freely on X, so its order is 1, 2 or 4.
- The ⟨50⟩ case fails by Lemma 1 with d = c−a.
- The block through {a, a+50} is fixed by +50 (Lemma 1 with d = 50). Its stabilizer is therefore H and the block is a+H.
- So all 25 H-cosets are blocks, they are the only short blocks, and no full block contains two points differing by 25, 50 or 75. ✓

**h ≥ 4 (Lemma 3a).**
- The proof uses only H2, orbit–stabilizer and the count of 33 classes: 100/h ≤ 33 rules out h = 1 and h = 2.
- The bound is load-bearing in exactly two places:
  - Lemma 5: without it, h = 1 survives for classes with m = 0. Such a class need not contain 20 in its stabilizer, and Theorem A fails.
  - Theorem B(3): it rules out stabilizer H₅.
- No other constraint is used. ✓

**Trichotomy (Lemma 3b,c and Corollary 4).**
- Classes in one translation orbit are disjoint block sets with equal m, and S is a single orbit. So (100/h)m = 25, i.e. h = 4m with m | 25.
- This leaves (4,1), (20,5) and (100,25). The condition h | 25−m holds in all three, and O_S is unique.
- This is derived in the note, not imported from the source's type list. ✓

**Lemma 5:** h | 25 and h ≥ 4 give H₅ or K. ✓ **Lemma 6:** ✓

**Theorem A (excluding T3 and T1).**
- The core fact is that every admissible stabilizer of a class carrying a full block, other than H, contains H₅ = ⟨20⟩. These are H₅, H₂₀ and H₂₅. H₁₀₀ occurs only for the all-short class S. Meanwhile H₅ ∩ H = {0}.
- Under T1 or T3, every class with a full block therefore has 20 in its stabilizer.
- The block through {0, 20} is full because 20 ∉ H. Lemma 6 then gives 20 ∈ Stab(X) = {0}, a contradiction.
- T3 and T1 fall together, and Corollary 4 leaves only T2. ✓

**Theorem B.**
- (1) ✓
- (2) X_i + H is exactly the preimage of X_i mod 25, which gives (S2). ✓
- (3) A class with stabilizer H₅ would bring 20 > 8 classes outside O_S. So all 8 have stabilizer K and form two orbits of 4. Y and Y+(y′−y) would collide unless Y mod 4 = Z₄. ✓
- (4) 25 + 600 + 200 = 825 forces the eight full orbits to be distinct. The bijection between triples (Z, z, z′) and full blocks through {0, d} then gives (S1). ✓

**Theorem C.**
- (S1) gives trivial stabilizers.
- The 825 indexed blocks cover 825·6 = 4950 pairs, each exactly once. So the blocks are distinct and form a design.
- P₀ and Q_j are partitions, and each block lies in exactly one of the 33 listed classes.
- P₀+25 = P₀ and Q_j+4 = Q_j, so +1 permutes the classes. ✓

**Corollary D:** both directions hold. ✓

**Cross-checks (not used in any proof).**
- The reported orbit data of the certified object (class orbits {25×1, 4×2}, block orbits {25×1, 100×8}) is exactly the structure Theorem B forces.
- The §7 arithmetic for v = 52 and v = 64 is correct.

### Findings

1. **Minor. Location: Thm B items 2–4 (where the tags (S2), (S3), (S1) are attached); first sentence of Thm C; Cor. D.**
   - **Problem:** (S1)–(S3) are never stated as standalone conditions. (S3) is attached to item 3, which is mostly a conclusion about class orbits and includes "Y_j is a full block". So the hypotheses of Theorem C and Corollary D are not formally defined.
   - **Fix:** before Theorem B, define the conditions for 4-subsets X₁,…,X₆, Y₁, Y₂ of Z₁₀₀:
     - **(S1)** The 96 ordered differences z′−z (z ≠ z′ in one set) are exactly the elements of Z₁₀₀∖H, each once.
     - **(S2)** X₁,…,X₆ mod 25 are pairwise disjoint 4-sets with union Z₂₅∖{0}.
     - **(S3)** Y_j mod 4 = Z₄ for j = 1, 2.

     Then restate Theorem B as "there exist base blocks satisfying (S1)–(S3) with P₀ = …, Q_j = …". The property "full" then follows from (S1), as the first lines of Theorem C's proof already show.

2. **Minor. Location: proof of Thm C, "…correspond bijectively to translates containing {x, y} (as in the proof of Theorem B(4))".**
   - **Problem:** B(4)'s injectivity uses distinctness of the eight orbits. In B that came from the block count of a given design, which is not available in C. The step is correct only for indexed translates, and the next sentence ("Counting with multiplicity") presupposes exactly that. So the conclusion stands.
   - **Fix:** "Index the translates by (Z, s) ∈ {X₁,…,Y₂} × Z₁₀₀. For d = y−x, the map (Z, s) ↦ (Z, x−s, y−s) is a bijection from {(Z, s) : x, y ∈ Z+s} onto {(Z, z, z′) : z, z′ ∈ Z, z′−z = d}. Hence {x, y} is covered exactly N(d) times." The trivial-stabilizer sentence then becomes a corollary rather than a prerequisite.

3. **Minor. Location: proof of Thm C, "P₀ is a partition … (it has 1 + 24 = 25 blocks)".**
   - **Problem:** The residue fact gives covering, but disjointness needs the count, which the parenthetical only gestures at.
   - **Fix:** "Each p lies in H, or in X_i + (p−x) for the unique i and x ∈ X_i with p ≡ x (mod 25). So the 25 blocks cover Z₁₀₀, and since 25·4 = 100 they are pairwise disjoint."

4. **Minor. Location: §3 "Types (matching the source's list)" and Thm A.**
   - **Problem:** Read literally, the source's T3 wording ("there are parallel classes with more than one block from the short block orbit") also holds in T1. Calling (20,5) "T3" therefore assumes the source's types are exclusive. Validity is unaffected, because Theorem A proves m = 1, which is the source's T2 verbatim.
   - **Fix:** "Cor. 4 gives m ∈ {1, 5, 25}, labelled T2/T3/T1. Thm A proves m = 1, so every short block lies in a different class: T2 under any reading of T1/T3."

5. **Editorial. Location: Thm C, "maps onto itself class by class"; §0, "Any stronger reading only adds hypotheses to Theorems A and B".**
   - **Problem:** "Class by class" reads as "fixes every class", which is false: +1 cycles P₀+t ↦ P₀+t+1. Also, a stronger automorphism notion would break only the "if" half of Corollary D, and §0 does not say so.
   - **Fix:** "+1 maps B onto B and each class onto a class (P₀+t ↦ P₀+t+1, Q_j+t ↦ Q_j+t+1)". Add: "Cor. D is for the class-permuting definition of §0."

6. **Info. Location: §7.**
   - **Problem:** The arithmetic is correct. Lam–Miao–Mishima (Thm 2.3, §3, App. A), the source's Thm 1 and `control52.py` cannot be checked from this snapshot.
   - **Fix:** add "citations not re-checked in review".

7. **Minor (provenance, not mathematics). Location: `pc100-class-action-control.json`; `pc100-parent-result.json` field `candidate.receipt.input`.**
   - **Problem:** At v = 100 no subpartition-exchange control was available, so the class-mapping test has only the v = 64 control. That control records no checker hash, so it is not bound to checker `12a591…`. The receipt identifies the certificate by path only; its hash is recoverable only indirectly through `own_expansion_sha256` plus `bytes_equal`.
   - **Fix:** add `checker_sha256` to the control and `input_sha256` to the receipt.

### Validity, novelty, significance

- **Validity:** Theorems A–D are correct, subject to the wording fixes 1–5.
  - The exclusion of T3 and T1, the forcing of T2, and both directions of Corollary D all check.
  - h ≥ 4 follows from the class count alone.
- **Novelty:** none is claimed. The method is the standard stabilizer and orbit analysis. The source names 88, not 100, as open. Whether point-cyclic resolutions for v = 100 are already known is a separate audit, and nothing here establishes priority.
- **Significance:** modest and specific to this case.
  - Corollary D makes the 8-block ansatz exact. That is what would give a future certified exhaustive search meaning, given separately proved normalizations.
  - The existence result does not answer a problem the source names as open.

### Bridge (A): sound

- **Direct route:** the parent checker reports the defining conditions, and the point map is a single 100-cycle:
  - 825 blocks, with all 4950 pairs covered once;
  - 33 classes of 25 blocks, each partitioning Z₁₀₀, together partitioning B;
  - x ↦ x+1 maps B onto B and every class onto a listed class.

  The v = 64 class-exchange control shows the checker distinguishes class-permuting invariance from mere block-set invariance, subject to finding 7.
- **Seed route:** the (S1)–(S3) checks plus Theorem C give a second, proof-based route.
- **Role of Theorems A–B:** they lie on neither route. They are needed only to claim the ansatz is complete.

---

## (B) mcDSQS(38) construction note

### Re-derivation

**The group G.**
- 3 has order 18 in U(38) ≅ C₁₈, since 3⁹ ≡ 37 = −1. So k is defined mod 18 and its parity is well defined.
- Composition is (m₁, b₁)∘(m₂, b₂) = (m₁m₂, m₁b₂ + b₁). Since m₁ is odd, the parities add. So G is closed under composition and inverses, and |G| = 18·19 = 342. ✓
- y+2 and 3y+1 generate all even translations and every k. ✓
- G is transitive: y+2 reaches the even points, and 3·0+1 = 1. ✓
- Stab(0) = {y ↦ 9ʲy} = {1,5,7,9,11,17,23,25,35}, which I recomputed. It has odd order, so it contains no involution. ✓
- Every involution of G has the form y ↦ −y+b with b odd, and is fixed-point-free. y ↦ −y+19 ∈ G. ✓

**The AGL(1,19) remark.** (m, b) ↦ (m mod 19, b mod 19) is an injective homomorphism onto AGL(1,19). The condition b ≡ k ≡ χ(μ) holds because 3 is a primitive root mod 19. ✓

**Orbit data.**
- 2·114 + 3·171 + 4·342 = 2109 = C(38,3)/4. ✓
- Orbit lengths 342/3 and 342/2 are realizable:
  - an order-3 element fixes exactly 2 points, so a block can be a fixed point plus a 3-cycle;
  - a block can be a pair of 2-cycles of a fixed-point-free involution.
- "26 triple orbits" is consistent: 19 subgroups of order 3, each with 12 three-cycles, give 228 = 2·114 triples, and the remaining 8208/342 = 24 orbits are regular.

**The colouring at 0.**
- The six listed triples are x·⟨7⟩ with ⟨7⟩ = {1,7,11}.
- They are pairwise disjoint and cover ⟨9⟩·2 ∪ ⟨9⟩·3.
- They form two ⟨9⟩-orbits of size 3.
- They miss {19} ∪ ⟨9⟩·1 ∪ ⟨9⟩·4, which is 19 points.
- The class-size profile 12¹⁸6 forces every point to miss exactly one class.
- Triples through 19 have trivial ⟨9⟩-stabilizer, consistent with "two ⟨9⟩-orbits of 9 classes". ✓

**Transport.** If g ∈ Aut(SQS) and g(0) = x, then g maps D₀ isomorphically onto D_x and maps partial parallel classes to partial parallel classes. ✓

### Findings

1. **Minor. Location: §0 "i.e. an mcDSQS(38)"; §1 "χ′(37) = 19 (Tan–Zhou (1.1))…"; §5 "COLOURS = χ′(37) = 19".**
   - **Problem:** The bridge to the definition is under-specified and relies on a citation for the upper bound.
   - **Fix:** "Every STS(37) S has χ′(S) ≥ ⌈222/⌊37/3⌋⌉ = 19, so χ′(37) := min_S χ′(S) ≥ 19. The certificate gives χ′(D_x) ≤ 19 at all 38 points. Hence χ′(D_x) = 19 = χ′(37) for every x. This agrees with, but does not depend on, Tan–Zhou (1.1)."

2. **Editorial. Location: §2, definition of G.**
   - **Fix:** add "3 generates U(38) ≅ C₁₈; k is defined mod 18, so its parity is well defined (equivalently, b is even iff m mod 19 is a square)."

3. **Editorial. Location: §2 "neither Z38⋊⟨9⟩ nor a subgroup of the cyclic translation group".**
   - **Problem:** the second clause is vacuous, since 342 > 38.
   - **Fix:** "G does not contain y ↦ y+1, so G ≠ Z38⋊⟨9⟩ despite equal order. The two are not even abstractly isomorphic: y ↦ y+19 is central in Z38⋊⟨9⟩, while AGL(1,19) is centerless. G contains no element of order 38."

4. **Minor. Location: §3 "so this labelling is not cyclic".**
   - **Problem:** Failure of +1 says nothing about other 38-cycles in Aut(SQS), and G is silent too because it has no 38-cycle. The note already disclaims an isomorphism test, but this sentence should be hardened so it cannot be paraphrased as "noncyclic".
   - **Fix:** "The block set is not invariant under y ↦ y+1. Whether Aut(SQS) contains a 38-cycle was not tested; no noncyclicity claim is made."

5. **Minor. Location: §4 "⟨9⟩-invariant" and "two ⟨9⟩-orbits of 9 classes"; parent audit key `colouring_at_0_invariant_under_stabilizer`; §7 "transported by G".**
   - **Problem:** The invariance can only be invariance of the unordered set of classes, because ⟨9⟩ moves 18 of the labelled classes. It follows that the 38 colourings are G-equivariant, and independent of the choice of g_x, only as unordered partitions: g∘g_x and g_{g(x)} differ by an element of ⟨9⟩. The note's own wording is correct, and validity does not depend on this.
   - **Fix:** write "invariant as a set of classes" in §4 and in the audit key's documentation. Never describe the labelled certificate as G-invariant.

6. **Minor. Location: §6 "no SQS(38) is invariant under Z38⋊⟨3⟩, ⟨9⟩, ⟨31⟩ (exhaustive exact cover, two implementations)"; README Lemmas A, B, D.**
   - **Problem:** These are unreviewed computational nonexistence claims, with no certificates in the snapshot, and the README lemmas are not supplied. The ⟨3⟩ case is redundant: ⟨9⟩ ≤ ⟨3⟩ = U(38), so it follows from the ⟨9⟩ case.
   - **Lemma A is true.** Proof:
     - Let τ be an involutory automorphism of an STS(37) fixing only p.
     - The third point of the triple through {a, τa} is fixed by τ, so it is p. Hence all 18 triples through p are τ-invariant, and so are the colour classes containing them.
     - The deficiencies sum to 19·12 − 222 = 6, so at least 12 of those 18 classes have size 12.
     - Each such class misses one point q ≠ p. τ-invariance forces τq = q, a contradiction.
   - **Fix:** prefix the §6 claims with "lane computation, not independently verified", and either inline the proof of Lemma A or cite it precisely.

7. **Minor. Location: §0 "checked by two independent lane programs; parent verification … pending".**
   - **Problem:** This is stale, since the parent checker `ca7418…` reports VALID_MCDSQS. It is also slightly overstated: two checkers from the same lane are independent in code but not in specification.
   - **Fix:** "two separately written lane checkers (Python, C) and the parent checker `ca7418…`."

8. **Info. Location: §0, novelty sentence.**
   - The sentence is correctly hedged. Before any "first" or "new" wording, audit the literature after arXiv:2503.11934v1, including later versions and citing works.

### Validity, novelty, significance

- **Validity:** sound. It rests on the certificate checks, reported as passing by three checkers and not rerun by me. All §2 group statements and the transport argument are correct, and validity needs neither.
- **Novelty:** none is claimed. Tan–Zhou v1 names mcDSQS(38) as the smallest unknown mcDSQS(6n+2). Later literature has not been audited, and a literature miss would not establish novelty.
- **Significance:** if the audit confirms it, this settles the smallest case the source explicitly names. It is a single object with no family, and Tan–Zhou's downstream consequences are not re-proved here.

### Bridge (B): sound

- The SQS check makes every derived design D_x an STS(37).
- An explicit 19-colouring of each D_x, together with the universal lower bound of 19, gives χ′(D_x) = 19 = χ′(37) at all 38 points.
- χ′(37) = 19 is itself witnessed by the certificate.
- G, the orbit structure and the transport only explain how the certificate was found; none of them is needed for the bridge.
