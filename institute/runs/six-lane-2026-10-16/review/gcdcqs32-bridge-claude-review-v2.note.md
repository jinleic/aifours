DISPOSITION: ACCEPT-WITH-FIXES

**Basis.** I audited only the v2 (LF) Tan–Zhou excerpts, the stated raw predicate, `check_ingredients.py` and `build_c23.py`. All verdicts are **reported by parent**, and I reran none of them. That covers the three raw checkers, the 23, 52 and 7 control runs, the ingredient PASSes and the byte-identical rebuild. The code for the 128-point checker and the I2 checker is not in the packet. For those two I audit the stated predicate, not an implementation.

**Defects.** FATAL: none. MAJOR: none. MINOR: M1–M9 (listed at the end). None of them changes any conclusion.

## (a) Raw predicate versus the source definition

With S = ∅, the definition (281–288) reduces to two conditions:
- **(i)** The blocks form a CQS(32⁴:0). Blocks are 4-subsets, every 3-subset not inside a group lies in exactly one block, and no group triple lies in any block (258–262).
- **(ii)** For every one of the 128 points x, (X∖{x}, G(x)∖{x}, A_x) is a gcSTS(127,31). Condition (2) is vacuous.

Since 127 ≡ 1 (mod 6) and 127 ∉ {7,13}, lines 219–220 give (r,s) = (64,16).

**Pair conditions follow from the triple conditions.** The map A ↦ A∖{x} is a bijection from the blocks through x to the derived triples. Moreover, A∖{x} ⊇ {y,z} exactly when A ⊇ {x,y,z}.
- If {y,z} ⊄ G(x)∖{x}, then {x,y,z} lies in no group, so exactly one derived triple contains {y,z}.
- If {y,z} ⊆ G(x)∖{x}, then {x,y,z} is a group triple, so no derived triple contains {y,z}.

This is exactly a GDD(2,3,127) of type 1⁹⁶31¹ with long group G(x)∖{x} (line 213). No separate pair check is needed.

**r.** The predicate requires exactly 64 classes. Requiring them to be nonempty is a harmless strengthening.

**s.** A hole point lies in 96/2 = 48 derived triples, so it appears in 48 distinct classes. Hence at most 16 classes avoid the hole. "At least 16", "exactly 16" and the definition's "there are s" therefore coincide.

**All points.** The predicate is checked at all 128 points, which is the definition's quantifier when S = ∅.

**Verdict on the predicate.** The predicate implies the definition. The converse also holds, up to the nonempty requirement and the profile if the checker enforces it. The identification r = χ′(127) rests on (1.1) [19]; the lower bound χ′(127) ≥ ⌈2667/42⌉ = 64 is elementary.

**Profile consistency.** The reported profile 42⁴⁸32¹²28⁴ fits the forced structure:
- Every hole point lies in all 48 non-hole-free classes.
- Each of the 96 non-hole points has degree 63, so it misses exactly one class.
- Total misses are 48·1 + 12·0 + 4·12 = 96, as required.

The profile is an invariant of this construction, not part of the definition.

Conditional on the reported verdicts, the pinned file is a gcDCQS(32⁴:0) in the unrestricted sense, independently of how it was built.

## (b) Construction 2.3

**Hypotheses.** With (m,g,n,s) = (8,4,4,0), mgn+s = 128 ≡ 2 and mk₁+s = 32 ≡ 2 (mod 6). This is the branch proved in the quoted lines 450–541, not the branch deferred to [3].

**Relabelling is faithful.** `lab` is a bijection that maps Gᵤ×I₈ onto {32u,…,32u+31}.
- A_B: ingredient group t maps to {B_t}×I₈. Steiner-2 forces every B to meet each group once.
- D_T: ingredient group s maps to {T[s]}×I₈.
- Any group bijection is allowed, because the ingredient definitions are symmetric under relabelling groups.
- The derived-class lookup uses the same correspondence: `c = 8u[x]+i` for A_B, and `8·T.index(x)+i` for D_T.

**CQS check (the "routine" step at line 482).** Classify a triple by its first coordinates:
- Pattern {x,x,x}, or {x,x,y} with x and y in one group: uncovered. These lie in ingredient holes, and I3 is transverse.
- Pattern {x,x,y} with x and y in different groups: covered once, in A_{B₁}.
- Three distinct first coordinates inside one group: uncovered, because that triple is covered by G and so lies in no B and no T.
- Any other three distinct first coordinates: covered once, by the unique member of B ∪ T containing them.

**Disjointness rests on one fact about I1.** For each pair {x,y}, Steiner-3 partitions X∖{x,y} into two kinds of pieces:
- L∖{x,y}, where L is the member of G ∪ B through x and y (2 points);
- T∖{x,y}, for each of the four T ∈ T through x and y (3 points each).

Consequences for each class type:
- **y ∉ G.** A^{y,j}_{B₁}(x,i) lies in (B₁×I₈)∖{(x,i)}. Each D^{y,j}_T(x,i) lies in (T∖{x,y})×I₈, which is inside (X∖B₁)×I₈, and these pieces are pairwise disjoint. So the class is a PPC; reported size 10 + 4·8 = 42.
- **y ∈ G∖{x}.** Here L = G, so the four sets T∖{x,y} partition X∖G. The class is a full, hole-free parallel class of (X∖G)×I₈ (size 32).
- **Fʲ.** The four B-lines through x meet only at x and partition X∖G. So the class is a hole-free PPC (reported size 4·7 = 28).

Every class of every A_B(x,i) and D_T(x,i) is used exactly once. The triple sets of distinct ingredients are disjoint, and 4·148 + 15·128 = 2512.

**Assigning I2's hole-meeting classes to y arbitrarily is permissible.** The argument uses only that the class's support lies in (B₁×I₈)∖{(x,i)}; the label y only selects B₁. The I3 labels, by contrast, are forced: the class must be the frame class missing {y}×I₈. This is implemented by `smiss` and `y = T[smiss]` (`build_c23.py:88-90`). The hole-free I2 classes are found by actual hole-avoidance, and the (a)-style degree count forces there to be exactly 4.

**Ingredient checkers.** I found no missing hypothesis.
- `check_fg` is exactly lines 248–253. B-transversality and |T∩G| ≤ 2 are consequences of the definition, not omissions.
- `check_fdh` is exactly lines 237–247.
- In `check_fdh`, the count of m/2 classes missing each group is forced by degree, so the unused `miss` list is not a gap.
- The transverse (H-design) reading of GDD(3,4,·) is forced by line 242, where the derived design is taken on X∖G.

The implementation is faithful, and the source argument is complete for these parameters. This gives a second, paper-level route to (1) conditional on the ingredients being valid. It does not replace the raw check.

## (c) Infinite family and order 128

**Corollary 2.6 with m = 32.** Each input checks out:
- m = 32 ≡ 8 (mod 12).
- 4m + s = 128 ≡ 2 (mod 6).
- 4ᵗ ≡ 4 (mod 12).
- A 2-RSQS*(4ᵗ) exists for t ≥ 2 (Theorem 2.5(1)).
- An RDTD(3,4,32) exists, since gcd(32,4) = 4 ≠ 2 and gcd(32,18) = 2 ≠ 3 (Theorem 2.5(2)).
- Construction 2.4 then gives a gcDCQS(32^{4ᵗ}:0).
- Apply Construction 2.1 with (g,n,s) = (32, 4ᵗ, 0). Since 32·4ᵗ ≡ 2 (mod 6), this is the quoted branch, and I re-traced it for s = 0.
- Its third hypothesis, gcDSQS(32,0), is an SQS(32) with no hole points, i.e. an mcDSQS(32). The printed proof omits this step.
- χ′(31) = 16 = (g+s)/2, so the merge of classes works.
- The output order is 2^{2t+5} = 2^{2n+1} with n = t+2 ≥ 4, matching line 1113.

There is no exceptional t.

**Order 128.** t = 1 lies outside Corollary 2.6. Instead apply Construction 2.1 directly with (32,4,0), using Lemma 3.4's mcDSQS(32) on all four groups. This is valid, gives existence only, and is conditional on Lemma 3.4.

**Imports, not re-proved here:**
- Lemma 3.4 (Appendix B is not in the packet).
- Theorem 2.5(1), from [21, Cor. 3.2].
- Theorem 2.5(2), from [9,21].
- Construction 2.4 (its proof beyond line 572 is unaudited).
- (1.1) from [19], used only to name χ′. For the outputs, the elementary bound plus the constructed v/2-colouring already gives equality.

**Exceptional order (a source defect, relevant to this packet).** The ≡2 branch of Construction 2.1 needs a (g+s)/2-colouring of the filler's derived STS(g+s−1).
- This is impossible for g+s ∈ {8,14}, since χ′(7) = 7 and χ′(13) = 8.
- Every non-hole-free class of A_x already contains every hole point, so the extra filler classes cannot be absorbed.
- Corollary 2.6 admits m = 8, so it is unproved at m = 8.
- Combining I2 with the trivial mcDSQS(8) would therefore not validly give mcDSQS(8·4ᵗ), which are the same orders.
- m = 32 is unaffected.

Separately, line 314 contains a typo: "2g+1 ≤ i" should read "g/2+1 ≤ j". It is irrelevant when s = 0.

## (d) Significance (no novelty or priority claim)

- **What it settles.** It supplies one of the two objects that item (2) of the source's own problem list asks for. The resulting family is the consequence the authors pre-computed, obtained with their own machinery.
- **Where the content lies.** The non-routine input is the ingredient triple, chiefly I2 and I3, together with the fact that the AG(2,4) 1-FG with K = {5} fits at m = 8. Item (3) shows the authors had this route in mind for m = 18.
- **The certificate is not redundant.** By the m = 8 defect in (c), I2 alone does not yield the family.
- **Not checked.** I have not checked whether the ingredients already exist in the literature, or whether item (2) has been settled since v1 (March 2025).
- **Not addressed.** The v = 20 half, mcDSQS(38), RDSQS(52), and general existence.
- **Assessment.** This is a modest, short-note-scale contribution whose value is that it is explicit and mechanically checkable. I give no weight to the number of orders covered.

**Scope of the reported evidence.** The reported runs support only these claims:
- the pinned bytes satisfy the predicate in (a);
- I1 and I3 pass the checkers audited here;
- I2 passes a checker that was not supplied;
- the assembler reproduces the pinned bytes.

The reported runs are not evidence for Lemma 3.4, Theorem 2.5, Construction 2.4, an explicit mcDSQS(128), the v = 20 half, or priority.

## Required corrections (all MINOR, none changes the conclusion)

**M1 (claim 3).** Replace the first sentence with: "Conditional on Tan–Zhou (arXiv:2503.11934v1) Lemma 3.4, Theorem 2.5(1) [=21, Cor. 3.2], Theorem 2.5(2) [=9,21], Construction 2.4 (proof not reproduced here) and Construction 2.1 (≡2 mod 6 branch, lines 295–335), Corollary 2.6 with m = 32 yields an mcDSQS(32·4ᵗ) for all t ≥ 2, i.e. an mcDSQS(2^{2n+1}) for all n ≥ 4."

**M2.** Add: "With s = 0, an SQS(v,0) is an SQS(v), so gcDSQS(32,0) = mcDSQS(32). Lemma 3.4 therefore supplies all four fillers. Corollary 2.6's printed proof omits this hypothesis."

**M3.** Add the m = 8 exception from (c): "Corollary 2.6 is unproved at m = 8, and gcDCQS(8⁴:0) does not by itself yield mcDSQS(8·4ᵗ)."

**M4.** Rewrite the order-128 sentence as: "Construction 2.1 with (32,4,0) gives an mcDSQS(128), conditional on Lemma 3.4. It is existence only and not explicit, and priority is not assessed." Recommended: build it and raw-check it, which removes the dependence on Lemma 3.4 for this order.

**M5 (claim 1).** Make these wording changes:
- Change "accept" to "reported by parent to accept".
- Change "independent" to "separately implemented".
- State the accept/reject split for the "52 third-checker runs".
- Mark the profile as observed rather than required.
- Define "partition" as multiset equality with {A∖{x}}.
- Define "quadruple" as four distinct points.
- State that HOLEFREE 16 is a count, not a position. The 12 hole-free classes F^{y,j} with y ∈ G∖{x} are interleaved among the first 60 classes.

**M6 (`check_ingredients.py`).** Make three changes:
- Delete `miss` (lines 98, 109) or assert that it gives 4 per group.
- Replace the coined "FDH(5,8,4,3)" with FDGDD(3,4,5{8}).
- Quote the source's definition of GDD(3,4,·).

**M7 (I2 provenance).** Name the checker and parameters used to validate I2: 4 groups of 8, 1184 blocks, and at each of the 32 points 148 triples in 16 nonempty PPCs, 4 of them hole-free. Mark the result as reported by parent.

**M8 (`build_c23.py`).** Make three changes:
- In docstring line 15, change "increasing label order" to "increasing 1-FG point id". The code at lines 75 and 95 sorts by point id, which coincides with label order only if u is monotone in the id.
- Rename the local `s` at line 84, which shadows the stem parameter.
- Note that `python -O` strips the asserts. This is harmless because the output is raw-checked.

**M9 (claim 2).** Add: "conditional on the reported verdicts; priority not searched; the v = 20 half is outside this packet and not covered by this review."
