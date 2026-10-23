# Construction 2.3 hypotheses used for gcDCQS(32⁴ : 0) and how each ingredient meets them

Frozen note for the bridge audit, written 2026-10-17 after 15:27:49 PDT (host clock). Source:
Tan–Zhou arXiv:2503.11934v1, pinned text `mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt`
(sha256 `df52a8f11a46974eef129fa115bb3305831f7c8edc3e2102e4fd22c64c3c8164`). Line numbers refer to that file.
Certificate: `gcdcqs32_c23.txt`, sha256 `e38945b1204e78937527f17db3d87f147e47885dc160c04b6a4de49377da0f46`.
Acceptance of the certificate does not rely on this note: both lane checkers verify the 128-point
object directly, without using the construction or any symmetry. The note says which instance of
the construction produced it.

**Statement (lines 444–447).** If there is a 1-FG(3, (K₁, K), gn) of type gⁿ, integers m, s with
mgn + s ≡ mk₁ + s ≡ 2, 4 (mod 6) for every k₁ ∈ K₁, a gcDCQS(m^{k₁} : s) for every k₁ ∈ K₁, and an
FDGDD(3, 4, k{m}) for every k ∈ K, then there is a gcDCQS((mg)ⁿ : s). The proof used is the
2 (mod 6) case, lines 449–541.

**Instance.** g = 4, n = 4, m = 8, s = 0, K₁ = {4}, K = {5}.

| Hypothesis | Source definition | Instance | Ingredient and check |
|---|---|---|---|
| H1: 1-FG(3, (K₁, K), gn) of type gⁿ | s-FG, lines 248–255: G partitions X; (X, G ∪ B) is a Steiner 2-system; (X, G ∪ B ∪ T) is a Steiner 3-system; B has block sizes K₁ and T has block sizes K; the type is the multiset of group sizes | gn = 16, type 4⁴. X = AG(2, 4) on F₄², G = the 4 lines u = const, B = the other 16 lines, T = 48 affine 5-arcs | `ingredient_I1_fg_ag24.json` (sha256 `f748c9c5…519e`). Checked by `code/check_ingredients.py fg`: every pair of the 16 points lies in exactly one member of G ∪ B; every 3-subset lies in exactly one member of G ∪ B ∪ T; |B| = 16 blocks of size 4; |T| = 48 blocks of size 5; 4 groups of 4. Result: PASS. Controls: 5/5 mutants rejected for the intended reason |
| H2: mgn + s ≡ mk₁ + s ≡ 2, 4 (mod 6) for all k₁ ∈ K₁ | lines 445; the proof case is "≡ 2 (mod 6)", lines 449–450 | mgn + s = 128 ≡ 2; mk₁ + s = 32 ≡ 2 (k₁ = 4). Also mk₁ + s − 1 = 31 ∉ {7, 13}, so (1.1) gives (r, s) = (16, 4) for the ingredient | arithmetic |
| H3: gcDCQS(m^{k₁} : s) for all k₁ ∈ K₁ | gcDCQS, lines 281–288. For x in a group, the derived design is a gcSTS(gn + s − 1, g + s − 1), defined at lines 205–220 | gcDCQS(8⁴ : 0): CQS(8⁴ : 0) on 32 points. Each derived design is a gcSTS(31, 7) with r = 16 and s = 4 | `ingredient_I2_gcdcqs8.txt` (sha256 `125a4d24…65c4`): lane certificate `runs/e1/col_g8_s0_str/gcdcqs8_s0.txt`, byte-identical to the gcdcqs20 lane's E8(iii) certificate. Both gcDCQS checkers PASS (stdlib and C: v = 32, 1184 blocks, 16 colours, 4 hole-free) |
| H4: FDGDD(3, 4, k{m}) for all k ∈ K | FDGDD, lines 241–247: a GDD(3, 4, mv) of type m^v whose derived design at every point is a KF(m^{v−1}). KF, lines 237–240: a GDD(2, 3, mv) of type m^v whose blocks split into classes, each a parallel class of X ∖ G for one group G | FDGDD(3, 4, 5{8}): 40 points, 5 groups of 8. Blocks are 4-sets meeting each group at most once, and each 3-set meeting 3 groups lies in exactly one block. At every point x the derived design on X ∖ G_x is split into parallel classes of X ∖ (G_x ∪ G′) | `ingredient_I3_fdh_5_8.txt` (sha256 `b860b493…d4d7`). Checked by `code/check_ingredients.py fdh`, which tests exactly these conditions at all 40 points: 1280 blocks, 16 classes per point. Result: PASS. Controls: 5/5 mutants rejected for the intended reason |

**How the proof is applied (`code/build_c23.py`).**
- **Labels.** The big point (x, i), with x ∈ X and i ∈ I₈, gets label 32·u(x) + 8·w(x) + i. Here u(x) is the index of the group of x and w(x) is the position of x in that group. The big groups G × I₈ are therefore {32u, …, 32u + 31}.
- **Blocks (lines 453 and 467–480).**
  - Each B-line meets every group once (in an affine plane, non-parallel lines meet in one point). So the gcDCQS(8⁴ : 0) is placed on B × I₈ by sending its point 8t + i to (B_t, i), where B_t is the point of B in group t.
  - The FDH(5, 8, 4, 3) is placed on T × I₈ by sending its point 8s + i to (a_s, i), where T = {a₀ < … < a₄}.
  - In total F has 16·1184 + 48·1280 = 80384 blocks.
- **Colouring at (x, i) (lines 495–531).**
  - For y ∉ G(x): F^{y,j} = A_{B₁}^{y,j}(x, i) ∪ ⋃_{T∋x,y} D_T^{y,j}(x, i).
  - For y ∈ G(x) ∖ {x}: F^{y,j} = ⋃_{T∋x,y} D_T^{y,j}(x, i).
  - F^j = ⋃_{B∋x} A_B^j(x, i), for j = 1, …, 4.
  - The class-label bijections the proof leaves free are fixed as follows. The non-avoiding classes of A_B at (x, i), in index order, are dealt to the points y ∈ B ∖ {x} in increasing order, 4 each. The avoiding classes keep index order. The frame classes missing the group of y keep index order.
- **Checks on the output.** Both lane checkers PASS: every non-group triple lies in exactly one block, and at all 128 points there are 64 nonempty partial parallel classes, 16 of them hole-free. The class sizes at every point are 42⁴⁸ 32¹² 28⁴. Controls: 21/21 retained mutants rejected for the intended reason. Producer replay is byte-identical: I1 and I3 re-solved by kissat with the same seeds, I2 re-produced, then assembled.

**Not claimed.** No statement about novelty or priority, and nothing about the mcDSQS(2^{2n+1}) family. Corollary 2.6 and Construction 2.1 also need an mcDSQS(32), Theorem 2.5 inputs and a separate check. FDH(v, g, 4, 3) designs are studied by Chang–Zheng–Zhou (Des. Codes Cryptogr. 87 (2019) 1415–1431); only the abstract was read. The ingredients here were constructed and checked independently of that paper.
