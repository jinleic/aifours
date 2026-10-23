# A0 — bounded prior-art audit for mcDSQS(2p), p ≡ 7 (mod 12) (lane record; not proof of openness)

Host clock 2026-10-17 ≈03:46–03:55 PDT. A literature miss is not novelty; paywalled journal
versions were not read.

## 1. Tan–Zhou arXiv:2503.11934v1 (local text, sha256 df52a8f1…c8164), constructions read

| Statement (text lines) | What it produces | Covers 2p (p ≡ 7 mod 12)? |
|---|---|---|
| Lemma 3.4 (903–907, App. B) | mcDSQS(20) (via [16], cyclic SQS(20) of Phelps), cyclic mcDSQS(26), mcDSQS(32) | no (20 = 2·10, 26 = 2·13, 32: none is 2p with p ≡ 7 mod 12) |
| Thm 3.9 (1072–1078) via Constr. 2.7 + 2.8 + Lemmas 3.5–3.8 | mcDSQS(2·9ⁿ+2): 20, 164, 1460, … | no (2·9ⁿ+2 = 2(9ⁿ+1), 9ⁿ+1 even for n ≥ 1) |
| Constr. 2.1 (292–293) | mcDSQS(gn+s) from gcDCQS(gⁿ:s), mcDSQS(g+s), gcDSQS(g+s,s) | conditional; the paper supplies the ingredients only for the families above. For 2p one would need e.g. a gcDCQS(2^{p−1}:2) — not provided |
| Constr. 2.3/2.4, Cor. 2.6 (444–447, 568–569, 684–693) | gcDCQS((mg)ⁿ:s), mcDSQS(m·4ⁿ) **conditional** on gcDCQS(m⁴:0) (open per §4(2)) | no (m·4ⁿ is not 2p) |
| Constr. 2.7 (732–733) | mcDSQS(gn+2) from a 1cDCQS(gⁿ:2) and RDSQS(g+2), n ≡ 0 mod 3 | 2p = gn+2 needs 3 ∣ n, g ∣ 2p−2; ingredients supplied only for g = 2, n = 9^m |
| Thm 3.2 / Cor 3.3 | RDSQS(2^{2n+1}+2) (orders ≡ 4 mod 6) | not mcDSQS(6n+2) |
| §4(1) (1108–1110) | "smallest unknown mcDSQS(6n+2)" = 38 | names 38 only |

Conclusion for Tan–Zhou: no stated construction yields mcDSQS(62), mcDSQS(86) or the family.

## 2. Other sources checked (web, read-only)

| Query / source | Result |
|---|---|
| web `"mcDSQS" Steiner quadruple system minimum colorable derived designs` | only Tan–Zhou 2503.11934 (v1 15 Mar 2025) and mirrors |
| web Shi–Xia–Krotov arXiv:2212.00048v2 (JCTA 2023) listing | the source of mcDSQS(20); Tan–Zhou state it was the only known mcDSQS(6n+2), n ≥ 2 |
| web `Steiner quadruple system SQS(2p) invariant under AGL(1,p) …` | generic SQS literature (point-regular abelian groups arXiv:0910.2759, Potapov counting, SageMath); no AGL(1,p)-on-two-copies SQS with colourings located |
| web `cyclic Steiner quadruple systems SQS(2p) Siemon S-cyclic …` | generic; the lane's T1 designs are **not** cyclic (not invariant under y ↦ y+1; only even translations) |
| web `Schreiber … Netto triple systems q ≡ 7 mod 12` | nothing relevant returned |

## 3. Equivalence remarks (lane reasoning)

* Netto systems N(q) (q ≡ 7 mod 12) are STS(q) invariant under A = {x ↦ ax+b : a square}; they
  are used by Wilson/Schreiber for large sets LSTS(q+2). In T1 the two A-orbits of
  "equilateral" triples {0,1,−ω²} of each copy are exactly two Netto systems on that copy;
  the block through such a triple is fixed by its order-3 stabilizer, so its fourth point is
  the triangle's centroid in the same copy or in the other copy. T1 objects are SQS(2p), not
  Netto systems or large sets; no published equivalence located.
* Affine SQS (AG(n,2), orders 2ⁿ) and the doubling SQS(2v) from SQS(v) (v even) do not
  produce orders 2p with p odd prime.
* Status statement: **in the located literature, mcDSQS(2p) for p ≡ 7 (mod 12) is neither
  stated nor implied beyond the lane/parent-verified p = 19 example.** This is a bounded
  search result only.
