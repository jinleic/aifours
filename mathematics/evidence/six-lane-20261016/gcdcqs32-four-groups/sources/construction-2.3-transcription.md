# Tan–Zhou Construction 2.3 — transcription and branch analysis (README E10)

Source: `../../../kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt` (pdftotext of
arXiv:2503.11934v1, sha256 `df52a8f1…c8164`). Written 2026-10-17 between the 15:11:12 and 15:3x
PDT host-clock readings, before any E10 computation. Line numbers refer to that text file.

## Definitions used (lines 237–255)

* **KF(m^v)** (237–240): a GDD(2, 3, mv) of type m^v whose blocks are partitioned into classes,
  each a parallel class (PC) of X ∖ G for some group G ("holey PCs"); exists iff m ≡ 0 (mod 2),
  v ≥ 4, m(v − 1) ≡ 0 (mod 3). Each group then has exactly m/2 holey PCs (point count).
* **FDGDD(3, 4, v{m})** (246–247): a GDD(3, 4, mv) of type m^v whose derived design at every
  point is a KF(m^{v−1}). (A GDD(3, 4, mv) of type m^v: blocks are 4-sets meeting every group in
  ≤ 1 point, every 3-set meeting three groups lies in exactly one block — the H(v, m, 4, 3)
  of Chang–Zheng–Zhou, who call this object FDH(v, m, 4, 3), Des. Codes Cryptogr. 87 (2019)
  1415–1431; abstract read 2026-10-17, body not accessed.)
* **s-FG(3, (K₁, …, K_s, K_T), v)** (248–255): (X, G, B₁, …, B_s, T), G a partition of X, each
  (X, G ∪ Bᵢ) a Steiner 2-system, (X, G ∪ (∪Bᵢ) ∪ T) a Steiner 3-system; block sizes Kᵢ for Bᵢ,
  K_T for T; type = multiset of group sizes.

## Construction 2.3 (statement lines 444–447, proof 449–541, remark 542–543)

*Hypotheses.* A 1-FG(3, (K₁, K), gn) of type gⁿ, (X, G, B, T); integers m, s with
mgn + s ≡ mk₁ + s ≡ 2, 4 (mod 6) for every k₁ ∈ K₁; a gcDCQS(m^{k₁} : s) for every k₁ ∈ K₁;
an FDGDD(3, 4, k{m}) for every k ∈ K. *Conclusion.* A gcDCQS((mg)ⁿ : s).
*Proof (case 2 mod 6, lines 449–541).* Y = (X × I_m) ∪ S, groups H = {G × I_m}, H_B =
{{x} × I_m : x ∈ B}. On B × I_m for B ∈ B put a gcDCQS(m^{|B|} : s) A_B (453–465); its derived
design at (x, i) has the resolution {A_B^{y,j}(x, i) : y ∈ B∖{x}, 1 ≤ j ≤ m/2} ∪
{A_B^j(x, i) : 1 ≤ j ≤ (m+s)/2}, the A_B^j being PPCs of (B∖{x}) × I_m (456–461). On B × I_m for
B ∈ T put an FDGDD(3, 4, |B|{m}) D_B whose derived design at (x, i) is a KF(m^{|B|−1}) with
holey PCs D_B^{y,j}(x, i), y ∈ B∖{x}, 1 ≤ j ≤ m/2, a PC of (B∖{x, y}) × I_m (467–476).
F = ∪_{B∈B} A_B ∪ ∪_{B∈T} D_B (477–480) is a CQS((mg)ⁿ : s) (482). Colouring at (x, i), x ∈ G
(495–531): for y ∈ X∖G, F^{y,j}(x, i) = A_{B₁}^{y,j}(x, i) ∪ ∪_{{x,y}⊂B∈T} D_B^{y,j}(x, i) with B₁
the block of B through {x, y} (498–508); for y ∈ G∖{x}, F^{y,j}(x, i) = ∪_{{x,y}⊂B∈T} D_B^{y,j}(x, i)
(508–514); F^j(x, i) = ∪_{x∈B∈B} A_B^j(x, i), 1 ≤ j ≤ (m+s)/2 (516–521). These form a resolution
of F(x, i) in which the F^{y,j} with y ∈ G∖{x} and all F^j avoid the hole (523–531). Stem points
(532–539) do not occur for s = 0. **So the output comes with explicit good colourings at every
point; the only freedom is the bijections between class labels.**

*Lane checks of the proof for (mg, n, s) = (32, 4, 0):* r = (gn − 1)m/2 + m/2 = mgn/2 = 64 = χ′(127),
hole-avoiding (g − 1)m/2 + m/2 = mg/2 = 16 = s. The T-blocks through a pair {x, y} partition
X∖B₁ (y ∉ G) or X∖G (y ∈ G) because G ∪ B ∪ T is a Steiner 3-system, so every F^{y,j} is a PPC;
the B-blocks through x partition X∖G (Steiner 2-system), so every F^j is a PPC; nonemptiness
holds when every B ∈ B has |B| ≥ 3 and every pair {x, y} ⊂ G lies in a T-block. The gcDCQS
ingredient needs mk₁ + s ≢ 8, 14 (χ′(7) = 7, χ′(13) = 8 are the (1.1) exceptions).

## Branches for gcDCQS(32⁴ : 0) (n = 4, s = 0, mgn = 128 ≡ 2 mod 6)

| (m, g) | 1-FG on gn points | gcDCQS(m^{k₁}:0), mk₁ ≡ 2 (6), mk₁ ≠ 8, 14 | FDGDD(3,4,k{m}): KF(m^{k−1}) ⇒ k ≥ 5, m(k−2) ≡ 0 (3) | verdict |
|---|---|---|---|---|
| (32, 1) | type 1⁴ on 4 points | k₁ = 4: the target itself | — | circular |
| (16, 2) | type 2⁴ on 8 points | k₁ ≡ 2 (3): k₁ = 2 gives no hole-free triples (empty avoiding classes), k₁ ≥ 5 impossible (a 5-set meets some group of size 2 twice, contradicting the Steiner 2-system) | — | impossible |
| **(8, 4)** | type 4⁴ on 16 points: G ∪ B an S(2, 4, 16) containing G (unique: AG(2,4), G a parallel class, B its other 16 lines; K₁ = {4}); T-blocks meet every line in ≤ 2 points (arcs, ≤ 6 points), with k ≡ 2 (3) ⇒ K = {5}: 48 affine 5-arcs covering each of the 480 non-collinear triples once | k₁ = 4: gcDCQS(8⁴ : 0) — **available** (lane certificates, parent-verified g = 8 calibration objects) | k = 5: FDGDD(3,4,5{8}) = FDH(5, 8, 4, 3) on 40 points | **cheapest**; block count 16·1184 + 48·1280 = 80384 ✓ |
| (4, 8) | type 8⁴ on 32 points; B-block sizes in {5, 8, 11, …}; point replication 4a + 7b + 10c = 24 forces mixed sizes | gcDCQS(4⁵:0), (4⁸:0), (4¹¹:0) (20, 32, 44 points) | FDH(k, 4, 4, 3), k ∈ {5, 8, …} | more ingredients |
| (2, 16) | type 16⁴ on 64 points; k₁ ∈ {10, 13, …} | gcDCQS(2^{10}:0), … | FDH(k, 2, 4, 3), k ≥ 8 (H(5,2,4,3) does not exist) | larger |
| (1, 32) | — | — | m must be even (KF) | impossible |

## Branch (8, 4): the AG(2, 4) 5-arc system (lane analysis, to be confirmed by computation)

In PG(2, 4) every 5-arc is an oval and lies in a unique hyperoval; hyperovals meet every line in
0 or 2 points, so the affine 5-arcs are exactly the 5-subsets of the 48 hyperovals disjoint from
the line at infinity (168 hyperovals, 120 of them meet ℓ∞; 168 − 120 = 48). Two 5-subsets of one
hyperoval share 4 triples, so T takes exactly one 5-subset O ∖ {f(O)} of each of the 48 affine
hyperovals. AGL(2, 4) is transitive on non-collinear triples, so each lies in exactly two affine
hyperovals (48·20 = 2·480); T exists iff there is a choice f(O) ∈ O with, for every non-collinear
triple t ⊂ O₁ ∩ O₂, exactly one of f(O₁), f(O₂) in t.
