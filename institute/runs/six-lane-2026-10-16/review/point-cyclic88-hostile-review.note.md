VERDICT: ACCEPT

**Bottom line.** I re-derived every step of PROOF.md using only Defs. 1–5 and two elementary facts about Z_88: it has a unique subgroup of each order, and the orbit–stabilizer theorem holds. The proof is **complete, self-contained and correct**.

- It derives T1 (Cor. 4) rather than assuming it.
- It does not use the source's 149,494,720 count or any classification.
- It prescribes no group beyond ⟨σ⟩.

I found no fatal or major problems. The minor items below are edits to the write-up; none changes a logical step.

---

## Findings

**Fatal:** none. **Major:** none.

**Minor (non-blocking)**

- **m1 (§0, semantic binding).** The pinned excerpt does not quote the source's definition of "automorphism of a resolution" (presumably Def. 4). §0 infers it from the isomorphism paragraph.
  - *Repair:* quote that definition verbatim.
  - *Why it is not a gap:* the Theorem states its hypotheses explicitly (σ(B)=B and σ(P)∈R for all P). Any reading of "automorphism of R" as a self-isomorphism of R implies them. A stronger reading, such as fixing each class, only strengthens the hypothesis, so the nonexistence result still follows. Details under Task 2.

- **m2 (§6 bullets).** Several statements are not backed by any pinned text or receipt:
  - the GMJ prime condition "as quoted by the source";
  - the Lam–Miao family "as quoted by the source";
  - "known 2-(52,4,1) point-cyclic resolutions have class orbits of lengths 4 and 13";
  - "258 resolutions found by the source";
  - "excluded: exactly v=4p … and v=8p … for all v≤10000". `general_table.py` has no pinned receipt, and check88 covers only v ∈ {52, 64, 76, 88, 148}.

  *Repair:* pin the quotes and the receipt, or label these as unverified. None of them is used by the Theorem or the Corollary.

- **m3 (§6 Corollary, "Changes to the proof").** The substitution list omits 44→4p (the diameter pairs in Lemma 2) and 28→r−1 (Lemma 5). Lemma 5 is in fact redone explicitly, so nothing is missing logically. *Repair:* add both substitutions to the list.

- **m4 (Cor. 4 title).** "Type T1" is not defined in the pinned excerpt. The proof uses only the fact that S is a class of R. *Repair:* define T1 that way, or drop the label.

---

## Task 1: step-by-step audit

**Lemma 1.** Correct. x+d ≠ y+d because x ≠ y, and (H1)+(H3) suffice.

**Lemma 2.** Correct.
- X is a union of Stab(X)-cosets, so |Stab X| divides 4.
- The subgroups of order 1, 2 and 4 are unique.
- The H_2 case is excluded by Lemma 1 with d = c−a.
- Conversely, a block containing the diameter pair {a, a+44} has 44 in its stabilizer (Lemma 1, d = 44). So its stabilizer is H_4 and the block is a+H_4.
- Hence all 22 cosets are blocks, and every other block has trivial stabilizer.
- Hand check of E1:
  - order-2 stabilizer: C(44,2) − 22 = 924;
  - order-4 stabilizer: 22;
  - total C(88,4) = 2,331,890, leaving 2,330,944 with trivial stabilizer.
  
  These match the receipt.

**Lemma 3.** Correct.
- (a) (H2) makes translation a genuine action of Z_88 on the 29-element set R, so orbit–stabilizer applies. Since 88/2 = 44 > 29, h ∈ {4, 8, 11, 22, 44, 88}.
- (b) For a full block X, H_h ∩ Stab(X) = 0, so H_h acts freely on the full blocks of P. When m = 22 the condition is vacuous.
- (c) Translation preserves fullness (S+d = S), and distinct classes are disjoint.

**Cor. 4.** I re-derived all six cases. (c) gives m ≤ h/4, and then (b) fails in each case:

| h | bound on m | 22−m ranges over | h divides it? |
|---|---|---|---|
| 4 | m = 1 | 21 | no |
| 8 | m ≤ 2 | 21, 20 | no |
| 11 | m ≤ 2 | 21, 20 | no |
| 22 | m ≤ 5 | 17..21 | no |
| 44 | m ≤ 11 | 11..21 | no |
| 88 | m ≤ 21 | 1..21 | no |

- Existence of P₀ = S: some class contains a short block, so its m is 22. Uniqueness follows from disjointness of classes. Both are argued correctly.
- The sharpened remark (h = 4m, so m | 22) is also correct, though not needed.
- The finite case split is legitimate. The universal content sits in Lemmas 1–3, which reduce every triple (D, R, σ) to a pair (h, m) from a finite set. The E2 table only re-checks that split.

**Lemma 5.** Correct. h | 22 and h ≥ 4 give h ∈ {11, 22}, and 8 ∈ H_11 = ⟨8⟩ ⊂ H_22 = ⟨4⟩. The bound 88/h ≤ 28 is redundant given 3(a), but harmless.

**Lemma 6 and §5.** Correct.
- X and X+8 both lie in P and share the point 8. For a full X, X+8 ≠ X, contradicting disjointness within P.
- 8 ∉ H_4, since gcd(8,88) = 8 does not divide 22. So the block on {0,8} is full and is not in P₀.
- The count of 440 uncovered pairs = 5 difference classes (±8, ±16, ±24, ±32, ±40) × 88. All are ≠ 44, so none degenerates.

**Hostile cross-checks**
1. *Escape routes.* A non-short class whose stabilizer avoids 8 would need h ∈ {1, 2, 4, 8, 44, 88}. h ≤ 2 violates the orbit bound; the others violate h | 22. No other route exists.
2. *Concrete picture.*
   - A class with stabilizer ⟨4⟩ is {X+4j}, where X is a transversal of Z_88/⟨4⟩.
   - A class with stabilizer ⟨8⟩ is two ⟨8⟩-orbits whose base blocks together form a transversal of Z_88/⟨8⟩.
   - Neither can contain difference 8. This is consistent with Lemmas 5–6.
3. *Agreement with the source.* The source's own statement that any point-cyclic resolution at v = 88 would be T1 agrees with Cor. 4. The closing step is Lemmas 5–6. The proof is short compared with the source calling v = 88 open, but that is not a defect: no step relies on an unstated hypothesis.

---

## Task 2: semantic binding

**Hypotheses of the Theorem:** σ is a single 88-cycle with no fixed points, σ(B) = B, and σ(P) ∈ R for every P ∈ R.

**Matching the source**
- Def. 5 makes point-cyclicity a property of the *resolution* ("it has an automorphism").
- The isomorphism paragraph defines maps between resolutions as design automorphisms sending each class of one resolution to a class of the other. An automorphism of R is such a map with both resolutions equal to R.
- "Maps to a class" is unambiguous. The image of a class is 22 disjoint blocks, so being contained in a class is the same as being equal to it.
- "Permuting the points in one cycle" means a single 88-cycle. 1-rotational automorphisms are a different notion.

**Why the class partition must be preserved, not just the design**
- **(a) Definitional.** A design-only reading would make "point-cyclic" a property of the cyclic design. That contradicts Def. 5's grammatical subject and the isomorphism notion. The p.2 convention also distinguishes designs *with point-cyclic resolutions* from cyclic designs.
- **(b) The source's own usage.** It classifies possible point-cyclic resolutions by type T1, and its 64-point example has class-orbit lengths 1, 4, 16. Both presuppose that ⟨σ⟩ permutes the classes.
- **(c) The proof needs it.** (H2) is used in Lemmas 3, 5 and 6. Lemmas 1–2 hold for *every* cyclic 2-(88,4,1) design.

**Consequences**
- The proof does **not** show that no cyclic 2-(88,4,1) design is resolvable by a resolution that σ fails to preserve. That question is not targeted.
- The class-transitive convention is not covered.
- The only remaining ambiguity is that the text of Def. 4 is not pinned (m1).

---

## Task 3: Corollary for v = 8p

Verified for every prime p ≡ 11 (mod 12).

**Setup**
- Divisors of 8p: {1, 2, 4, 8, p, 2p, 4p, 8p}. This uses that p is an odd prime with p > 8.
- r = (8p−1)/3 is an integer iff p ≡ 2 (mod 3). Then 8p ≡ 4 (mod 12).
- (a): 3 < 24p/(8p−1) < 4 for all p ≥ 1, so h ≥ 4.

**Cor. 4 analogue** (1 ≤ m ≤ 2p−1, and m ≤ h/4 from (c)):

| h | bound on m | why (b) fails |
|---|---|---|
| 4 | m = 1 | 2p−1 is odd |
| 8 | m ≤ 2 | 2p−1 is odd; 8 \| 2(p−1) iff p ≡ 1 (mod 4), excluded |
| p | m ≤ p/4 | would need p \| m, but m < p |
| 2p | m ≤ p/2 | would need 2p \| m, but m < 2p |
| 4p | m ≤ p | 2p−m ∈ [p, 2p−1] |
| 8p | m ≤ 2p−1 | 2p−m ∈ [1, 2p−1] |

**Lemma 5 analogue.** 3 < 6p/(2p−1) < 4 for p ≥ 3. Then h | 2p and h ≥ 4 give h ∈ {p, 2p}. Both H_p = ⟨8⟩ and H_{2p} = ⟨4⟩ contain 8.

**§5 analogue.** The short-block differences are {2p, 4p, 6p}, and 0 < 8 < 2p, so 8 is not among them.

**Spot checks**
- *Boundary p = 11:* every bound reduces exactly to §§2–5.
- *p = 23:* h ∈ {4, 8, 23, 46, 92, 184}; the non-short stabilizers are of order 23 or 46; 8 ∉ {46, 92, 138}.

**Where each hypothesis is used**
- p ≡ 3 (mod 4): only at (h, m) = (8, 2).
- p ≡ 2 (mod 3): integrality of r.
- Primality: the divisor list.
- p ≥ 5: 8 ∉ H_4, and the bounds lie in (3, 4).

**Limits**
- For primes p ≡ 5 (mod 12), (h, m) = (8, 2) satisfies (a)–(c), e.g. v = 40 or 136. The method says nothing there.
- Composite cofactors are not covered.
- The "exactly these families up to 10000" observation is computational only. The document correctly does not extrapolate it.

---

## Task 4: the v = 64 control

**What it checks**
1. The transcribed source example satisfies (H1)–(H4). This shows the proof's formalization is not stricter than, or vacuous relative to, the source notion.
2. The v = 64 analogues of Lemmas 2, 4, 5 and 6 hold on that example: short blocks are the cosets of ⟨16⟩, the resolution is T1, the non-short stabilizer orders are 4 and 16, and their common subgroup is H_4. The orbit lengths 1 + 4 + 16 = 21 are consistent.
3. The checker rejects three corrupted copies and accepts a reordering.

**What it does not prove**
- Anything about v = 88.
- Any universally quantified lemma; it is a single instance.
- The contradiction step: at v = 64 the common subgroup lies inside H_4, so §5 has no force there.
- That the transcription matches the PDF; only receipts are pinned.

The receipts were produced by the worker. With no tools, I did not re-run them; I hand-checked the E1, E2 and E3 values for 52, 64 and 88 instead, and they agree.

**Decision.** The written proof alone is **complete**. It is not conditional on any source theorem, and it is not wrong.

---

## Minimal defensible theorem

For every 2-(88,4,1) design D = (V, B) and every resolution R of D, no single 88-cycle σ on V satisfies both σ(B) = B and σ(P) ∈ R for all P ∈ R.

Equivalently, under the Topalova–Zhelezova convention (p.2 and Def. 5), no 2-(88,4,1) design has a point-cyclic resolution, i.e. none is cyclically resolvable.

The same holds for v = 8p, for every prime p ≡ 11 (mod 12).

**What it does not cover**
- Resolvable 2-(88,4,1) designs in general.
- Cyclic designs whose resolutions are not invariant under the cycle.
- The class-transitive convention.
- Automorphisms that are not a single 88-cycle, such as 1-rotational or two 44-cycles.
- v = 8p with p ≡ 5 (mod 12), or with a composite cofactor.
- The excluded-set table beyond the families proved.
- Priority or novelty.
