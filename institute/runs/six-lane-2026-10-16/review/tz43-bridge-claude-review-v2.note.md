DISPOSITION: ACCEPT

**FATAL**: none

**MAJOR**: none

**MINOR**

1. `lane/sources/tz43-feasibility-and-bridge-v1.md:20-24` (also 47, 65–66, 82, 84–86). LANE.
   - The note is stale. It is stamped 19:16, before B was pinned at 21:13 (README LF 43), yet still says "the remaining bottleneck for the frozen gate is the FDGDD/RDGDD ingredient … all small-seed symmetry models tried for B have failed or remain UNKNOWN".
   - LF 20 calls `eaff77fc…16c3` "directly verified", although receipt-v2 LF 33 records that the parent strict-ASCII checker rejected those raw bytes.
   - LF 65 "Filling by mcDSQS(20)" omits gcDSQS(20,2).
   - Fix: add a superseding v2 or erratum pointer (no in-place overwrite, contract LF 24); say "worker-checked"; cite the separate parent dispositions; add gcDSQS(20,2).
2. `lane/evidence/mcdsqs74-c21/construction-2.1-hypotheses.md:56-57`. LANE. Stale: "The frozen §4(3) target still requires FDGDD(3,4,5{18}) or RDGDD(3,4,5{18})". Fix: add a superseded pointer.
3. `lane/sources/tz43-family-consequence-v1.md:26,49-52`. LANE. The heading and the display "mcDSQS(18·4ᵗ+2), for every integer t≥2" are unconditional; the conditions appear only at LF 67–68. Fix: prefix "conditionally (LF 67–70)".
4. `lane/evidence/fdgdd18-d15-inflated/construction-note.md:64-65`. LANE.
   - "uses the certified size18 FDGDD itself … via source Construction2.3": "certified" is worker-only, the sentence has no conditionality, and it omits the fan, Construction 2.1 and mcDSQS(20).
   - Fix: "worker-checked candidate; conditional family per tz43-family-consequence-v1.md LF 67–70".
5. `lane/evidence/fdgdd18-d15-inflated/construction-note.md:6-7` (also `run/screening/math-1-tz43-contract.json:13` and `lane/evidence/fdgdd18-d15-inflated/receipt-v1.json:3`). LANE.
   - "the same definition as FDH(5,18,4,3)": FDH is defined in [2] (LF 1125–1126), which is not supplied, so the alias is unverified. No bridge step uses it.
   - Fix: drop it, or label it "alias per [2], unchecked, unused". The contract is frozen, so fix the lane texts only.
6. `lane/README.md:10`. LANE. "This README was written before any search" is false for LF 43–64, the 21:13 status block. Fix: "§1 frozen before any search; status block appended 21:13".
7. `lane/sources/tz/tan-zhou-2503.11934.txt:314`. SOURCE.
   - "each Q_x^j(G) with 2g + 1 ≤ i ≤ (g+s)/2": "2g" is a flattened g/2, and the index i for j looks like a typo (LaTeX not supplied).
   - The intended range is g/2+1 ≤ j ≤ (g+s)/2, i.e. only j = 10, matching s = 1 for gcSTS(19,1). Hypotheses LF 45 reads it this way. No change needed.

**Severity counts:** FATAL 0 · MAJOR 0 · MINOR 7.

---

**(a) Format S and Format D state exactly the source definitions; the FDH alias is not needed anywhere.**

- **gcDCQS(18⁴:2)** (LF 256–266, 281–288):
  - X = S ∪ G₀…G₃ with |S| = 2 and |Gᵢ| = 18, so v = 74.
  - Each 3-set not inside any S∪G lies in exactly one 4-block, and none inside does (60 264 triples, 15 066 blocks).
  - At x ∈ G, A_x is an STS(73,19) with hole H = (G∪S)∖{x}, and it must be a gcSTS(73,19). Since 73 ≡ 1 (mod 6) and 73 ≠ 7, 13, LF 219–220 give (r,s) = ((v+1)/2, (h+1)/2) = (37,10); r = χ′(73) = 37, and 10 = 37 − (73−19)/2.
  - At α ∈ S, (X∖S, G, A_α) is a GDD(2,3,72) of type 18⁴ and must be a KF(18⁴): PCs of X∖(S∪G). Degree 27 forces 36 classes, 9 per missed group.
- **FDGDD(3,4,5{18})** (LF 241–247): a GDD(3,4,90) of type 18⁵ (transverse 4-blocks, each transverse triple once, 14 580 blocks). Its derived GDD(2,3,72) of type 18⁴ on X∖G_x is a KF(18⁴) at every one of the 90 points.

Point-by-point comparison:
- **Hole convention:** identical, (G_x∪S)∖{x} (Format S LF 123).
- **"Exactly t" vs "there are s":** each hole point has degree 27, so it lies in 27 of the 37 classes and misses exactly 10. Any hole-avoiding class is among those 10, so at most 10 classes avoid H; "at least 10" and "exactly 10" coincide.
- **"Nonempty":** this adds nothing. The 27 non-avoiding classes contain hole points. If an avoiding class were empty, the capacity would be 27·24 + 9·18 = 810 < 819.
- **Stem frames:** "covering exactly X∖(S∪G_k) once" is a PC of X∖(S∪G_k) inside X∖S. The CQS triple check already forces derived stem triples into X∖S across three groups.
- **Format D:** "transverse + every transverse triple once" is the GDD(3,4) of type m^k (standard reading; LF 49–72 not supplied). FRAME classes are the KF classes; PC classes give the RGDD.
- **Parameters:** the values 74/4/18/2 and 5/18 come from headers and receipts, not from the generic checks.
- **FDH alias:** never used by any bridge step (see MINOR 5).

**(b) Yes: LF 1114–1116 asks for exactly these objects, with no quantifier change, and the status texts stay within "supplied, worker-checked, pending", except MINOR 1, 2 and 4.**

- LF 1114 asks for gcDCQS(18⁴:2) (stem 2, four groups of 18) and ONE of FDGDD/RDGDD(3,4,5{18}) (five groups of 18). Contract LF 4 and 11–14 and README LF 14–41 match.
- The source pairs RDGDD→2.2 (LF 339) and FDGDD→2.3 (LF 446). The lane uses FDGDD→2.3 only (family LF 54–55).
- The source does not state the range of n. The lane's t ≥ 1 matches Lemma 3.8's "positive integer", and renaming n→t avoids a clash with 2.3's n = 4ᵗ.
- README LF 43 and 62–64, family LF 3–5 and 67–70, and receipt B LF 4 and 405 claim only "supplied, worker-checked, pending".

**(c) The identification gcDSQS(20,2) = mcDSQS(20) is correct and the merges match the source; the bridge is moot for order 74 (not for t ≥ 2).**

- **Identification:**
  - With h = 2 no triple lies inside H, so SQS(20,2) = SQS(20) (LF 227–231).
  - At x ∉ H the derived design is an mcSTS(19), given by the mcDSQS(20).
  - At α the derived design is an STS(19,1) with hole {β}, which needs r = 10 and s = (1+1)/2 = 1 (LF 219–220).
  - β has degree 9 and meets each PPC at most once, so it misses exactly one class. That class is the unique avoiding class. This holds for any designated pair.
- **Merges:**
  - At a group point, P^j ∪ Q^j for j ≤ 10 and P^j for 11–37 is exactly LF 322–325.
  - At a stem point, P^j(G) ∪ Q^j(G) for j ≤ 9 per group, plus ⋃_G Q^{10}(G), is exactly LF 328–333.
  - Disjointness follows from the supports, and "listed order" is an admissible arbitrary bijection.
  - Using one SQS(20) for all four groups is legitimate: with s = 2, the source's G₀ role (mcDSQS) and the others' role (gcDSQS) coincide.
  - Counts: 15 066 + 4·285 = 16 206 = C(74,3)/4, and 819 + 57 = 648 + 4·57 = 876.
- **Moot for 74:** each derived STS(73) has 876 triples and a PPC has at most 24, so 36·24 = 864 < 876 forces at least 37 = χ′(73) classes. The order-74 claim therefore rests on the direct check alone. This is subject to the unsupplied mcDSQS definition and checker spec, and to parent verification.

**(d) Every hypothesis checks for t ≥ 2; an S(3,5,4ᵗ+1) suffices and no extra ingredient property is needed; the family is a conditional written consequence only.**

- **Fan:** for any S(3,5,n+1), B∞ is an S(2,4,n), and B∞ ∪ T covers each triple of Iₙ once, because its unique 5-block either contains ∞ or does not. With singleton groups this is a 1-FG(3,({4},{5}),n) of type 1ⁿ (LF 251–255). Resolvability is used only in 2.2's colouring (LF 390–395). The stronger Lemma 3.8 is imported and stated.
- **g = 1:** LF 444–447 impose no restriction, and type 1ᵛ is explicitly provided for (LF 253–255).
- **Congruences:** 18·4ᵗ+2 ≡ 74 ≡ 2 (mod 6).
- **Ingredients:** gcDCQS(18⁴:2) for k₁ = 4 and FDGDD(3,4,5{18}) for k = 5. The output is gcDCQS((18·1)^{4ᵗ}:2) = gcDCQS(18^{4ᵗ}:2).
- **Then 2.1** with (18, 4ᵗ, 2): the order is ≡ 2 (mod 6), and the group-point designs are gcSTS(18·4ᵗ+1, 19) with (r,s) = (9·4ᵗ+1, 10). mcDSQS(20) and gcDSQS(20,2) are as in (c).
- **Shared stem: nothing beyond the definitions is needed.** This is a reconstruction, since LF 448–541 is not supplied.
  - At (x,i), let B be the B₁-block containing x and y. The 27 non-avoiding classes of B's ingredient may be bijected arbitrarily to the labels (y,j), y ∈ B∖{x}, j ≤ 9.
  - The FDGDD frames missing y, from the T-blocks B′ ⊇ {x,y}, lie in (B′∖{x,y})×I₁₈. Since B′∩B = {x,y}, these sets partition (Iₙ∖B)×I₁₈.
  - The class count is 9(n−1) + 10 = (18n+2)/2, as required.
  - At α, the merges use the 9 frame classes per missed group that every KF(18⁴) has, and the B₁-blocks through y partition Iₙ∖{y}.
  - The same structure is visible for 2.2 in LF 351–362 and 432–441.
- **Routes:** FDGDD→2.3 is used correctly; RDGDD→2.2 is not invoked, and no RDGDD is supplied.
- **t = 1:** S(3,5,5) gives B∞ = {I₄} and T = ∅, so 2.3 just returns the ingredient. The lane bypasses this with the direct check, which is harmless.
- **No overclaim:** nothing claims certificates or formal proofs for t ≥ 2 (family LF 69–70, README LF 60).
- **Side remark (18,4,4,2):**
  - Here 290 ≡ 74 ≡ 2 (mod 6), and the output is gcDCQS(72⁴:2), not gcDCQS(18⁴:2).
  - Filling it via 2.1 needs mcDSQS(74) and gcDSQS(74,2) and gives order 290, which is just the t = 2 member again.
  - The type-4⁴ fan from RDS(3,5,17) is a valid 1-FG: G ∪ B₁ is the whole derived S(2,4,16), and G ∪ B₁ ∪ T is the whole fan, so both identities of LF 251–252 hold. The needed parallel class exists by LF 391. It is not needed for the family.

**(e) The recorded consequence (family LF 67–70; README LF 59–64) is properly conditional; the remaining defects are stale or unqualified wording (MINOR 1–6).** It disclaims formal proofs and certificates for t ≥ 2. The contract makes no result claims beyond the alias (MINOR 5).

---

**IMPORTS** (whether the lane states each)

1. Construction 2.3, statement plus the unsupplied proof: stated (family LF 37, 67–68).
2. Construction 2.1: stated. Its 2 (mod 6) proof is supplied and was checked above.
3. Lemma 3.8 [20,25]: stated (LF 28–30). Only an S(3,5,4ᵗ+1) is needed (standard; LF 34–35).
4. The fan from a Steiner 3-design: stated and proved (LF 32–35).
5. mcDSQS(20): the explicit Shi–Xia–Krotov object, worker-checked (the contract says parent-reconstructed): stated. Its existence is also given by source Theorem 3.9 with n = 1 (LF 1072), which the lane does not cite.
6. gcDSQS(20,2) = mcDSQS(20): proved by the lane, and correct.
7. χ′ values via (1.1) and LF 215–220: stated.
8. GDD, mcSTS and mcDSQS definitions: cited, not supplied.
9. The KF count of 9 classes per missed group: stated (README LF 27).

**UNKNOWN**

- The proof of 2.3 (LF 448–541): whether its 2 (mod 6) branch exists, how it handles g = 1, and whether it imposes any labelling condition.
- The (1.1) and mcDSQS definitions (LF 1–204). Order 74 meets either reading of "minimum colourable".
- The content of Lemma 3.4, and references [2], [20], [25].
- The FDH definition.
- The GDD definition text (LF 49–72).
- The raw certificate headers, the mcDSQS checker format, and parent verification.
- The LaTeX behind LF 314.
- The source's intended range of n in §4(3).
