# N=46, t=26: the nine residual-alphabet profiles other than (4,4,4,4)

Owner **PhysicsAME46-2**. Native clock observed immediately before writing: `Thu Oct 29 07:56:52 PDT 2026`; not an exact completion time. **WRITTEN author candidate** with exact bounded controls; not independently reviewed, not adopted, not formally verified, and not novelty-cleared. No held, quarantined, f161, f162 or v203 material was opened or used.

## 1. Claim, admissible inputs, boundary

**Hypothesis H.** ψ is a normalized complex AME(4,6) state, written in some product basis, with exactly `N=46` nonzero coefficients, exactly `t=26` of which have modulus `1/6`. Let P be those 26 positions and E the other 20.

**Inputs.**

- **(I1)** The recorded no-Hamming-one lemma, [f127 disposition](../../../../institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-n46-no-hamming-one-parent-v1.md), SHA-256 `262a5a09276a2d7ef3ce350425236b29af327c99f8ea3ba03cf50878978baac0`: under H, no two E positions differ in exactly one coordinate. It is conditional on the classical no-OLS(6) theorem. It is used **only** in §§5–7.
- **(I2)** The (4,4,4,4) branch exclusion recorded in the same disposition. It is cited only in the combined statement below. It is not used in any proof here and inherits that disposition's enumeration trust boundary.

**Claim C.** Under H, the residual-alphabet profile `(|π_i(E)|)_i` is, up to party order, `(4,4,4,4)`. Equivalently, each of the other nine possible profiles is impossible.

- Profile `(3,4,4,4)` is excluded by counting maximal words, with no import.
- The eight profiles containing a 5 are excluded by F₂ incidence algebra, using (I1).

**Combined consequence, conditional and not adopted.** C together with (I2) excludes H. The [f141 disposition](../../../../institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-n46-unitary-bridge-t27-t29-parent-v1.md), SHA-256 `b1d3face7eb8a06faec59031e62971c3054dbd99b9426087d73d882af3f30e40`, excludes t=27,28,29 at N=46. The [f113 disposition](../../../../institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-maximal-coefficients29-parent-v1.md), SHA-256 `86968ac972bf26f1f6cac6936bbccd23b27696487c96a9779be5ef0553723d9b`, gives t≤29. With those two records, **no AME(4,6) state would have support exactly 46**. That conclusion carries three boundaries: the no-OLS(6) import of f113 and f127, f113's prior t≤30 boundary, and (I2)'s finite-enumeration trust boundary.

This packet does not promote t=26 to an exclusion. That requires review. N=45 is treated separately and remains unadopted, so **no global ≥47 claim** is made.

## 2. Residual structure from the six two-party marginals

The six two-party marginals of ψ are `I_36/36`. Equivalently, each of the three 2|2 flattenings `U=6ψ` is a 36×36 unitary, and each pair of parties indexes the rows or the columns of exactly one flattening.

A coefficient of modulus 1/6 exhausts the squared norm `1/36` of its row and column, so it is the only nonzero entry there in every cut. The 26 P positions therefore occupy 26 singleton rows and 26 singleton columns of each U. Deleting them leaves a 10×10 unitary V supported on E. A unitary singleton row has modulus 1, and the corresponding coefficient would be in P; so every row and column of V has at least two nonzeros. Since `|E|=20`, each has exactly two.

**(R1)** For every pair of parties {i,j}, the 36 values `(x_i,x_j)` split as follows:

- 26 values are carried by exactly one P word and by no E word;
- 10 values are carried by exactly two E words and by no P word.

## 3. Local degrees and the ten profiles

Write `R_i=π_i(E)`, `r_i=|R_i|`, and `E_a={x∈E : x_i=a}` for `a∈R_i`. For any `j≠i`, every value `(a,y)` carried by E has exactly two extensions, and all of them lie in E_a. Hence `|E_a|=2|π_j(E_a)|`. The number

`d(a)=|E_a|/2=|π_j(E_a)|`

is therefore the same for every `j≠i`. It has four properties:

- **(D1)** `d(a)≥2`: if `d(a)=1`, the two words of E_a would agree in every coordinate.
- **(D2)** `Σ_{a∈R_i} d(a)=|E|/2=10`.
- **(D3)** `d(a)≤r_j` for every `j≠i`.
- **(D4)** `2≤r_i≤5` and `r_i r_j≥10`, because `|π_ij(E)|=10`.

The only profiles allowed by (D4) are:

`(2,5,5,5), (3,4,4,4), (3,4,4,5), (3,4,5,5), (3,5,5,5), (4,4,4,4), (4,4,4,5), (4,4,5,5), (4,5,5,5), (5,5,5,5)`.

By (D1) and (D2), the degree multisets are:

- size 5: all `d=2`;
- size 4: `X=(2,2,2,4)` or `Y=(2,2,3,3)`;
- size 3: `(2,3,5)`, `(2,4,4)` or `(3,3,4)`, each subject to the cap (D3);
- size 2: `(5,5)`.

## 4. Profile (3,4,4,4): counting maximal words (no import)

Call a coordinate i of a P word active if its value lies in R_i, and let `k(x)` be the number of active coordinates of x. By (R1), for each `j≠i`:

- exactly `6r_i−10` P words are active at i: pairs `(a,y)` with `a∈R_i` number `6r_i`, and all 10 E-carried pairs are among them;
- exactly `r_i r_j−10` P words are active at both i and j.

For `(3,4,4,4)` this gives `Σ_x k(x)=8+3·14=50` and `Σ_x C(k(x),2)=3·2+3·6=24`. Then

`Σ_{x∈P}[k(x)−C(k(x),2)]=26=|P|`.

The summand equals `0,1,1,0,−2` for `k=0,…,4`, so it is at most 1. Therefore every P word has `k∈{1,2}`.

Fix a party i with `r_i=4`; its three partners have sizes 3, 4, 4. It has 14 active P words. The words active at i and at one other party number `(12−10)+(16−10)+(16−10)=14`, and each such word is active at exactly one other party. So **no** P word is active only at i.

For `a∈R_i`, exactly `6−d(a)` P words have `x_i=a`, by (R1) on the pair (i,j). Among them, exactly `r_j−d(a)` are also active at j. Each of these words is active at i alone or at i and exactly one other party. The number of P words with `x_i=a` that are active only at i is therefore

`(6−d(a))−[(3−d(a))+(4−d(a))+(4−d(a))]=2d(a)−5`.

It must be 0, which is impossible for integer `d(a)`. Profile `(3,4,4,4)` cannot occur.

## 5. Parity fibers (uses I1)

Let `a∈R_i` with `d(a)=2`. Then E_a has four words. In each other coordinate j it takes two values, each exactly twice: each value `(a,b)` has exactly two extensions. After relabeling those values as 0 and 1, E_a is a four-point subset of the binary cube `{0,1}^3` that is balanced in each coordinate.

There are exactly eight such subsets: the even- and odd-weight parity classes, and six cylinders `{x_j=x_k}` or `{x_j≠x_k}`. Each cylinder contains two words differing only in the free cube coordinate. Since both words have `x_i=a`, they differ in exactly one of the four coordinates, which (I1) forbids.

So E_a is a parity class. For any two other coordinates j,k, it contains **exactly one** word with each of the four value pairs in `π_j(E_a)×π_k(E_a)`.

## 6. Incidence matrices of a five-symbol party

Let A be a party with `r_A=5`. By (D1) and (D2), every `g∈R_A` has `d(g)=2`, so by §5 every A-fiber E_g is a parity class. Because `E=⊔_g E_g`, the remaining structure is described by incidence matrices.

For every other party j, let U_j be the 5×r_j matrix over F₂ whose row g has ones exactly at the two values of `π_j(E_g)`. Its column at `b∈R_j` has weight `d(b)`.

**(M)** For two other parties j≠k and `(b,c)∈R_j×R_k`, the number of E words with `(x_j,x_k)=(b,c)` is, by §5,

`|{g : b∈π_j(E_g), c∈π_k(E_g)}| = (U_j^T U_k)_{bc}` (integer product).

**(O)** By (R1) every entry of `U_j^T U_k` is 0 or 2. In particular `U_j^T U_k=0` over F₂: every column of U_j is F₂-orthogonal to every column of U_k.

Read U_j as the edge-vertex incidence matrix of a loopless multigraph G_j. Its vertices are R_j, and each fiber g is an edge joining the two values of `π_j(E_g)`; vertex degrees are the d's. Over F₂, `rank U_j=r_j−c(G_j)`, where c is the number of connected components, and `ker U_j^T` is the cycle space of G_j.

**Lemma G.**

- **(G5)** If `r_j=5`, G_j is 2-regular. It is either a 5-cycle, of rank 4, or a 2-cycle (two parallel edges) plus a disjoint triangle, of rank 3. In the second case, write p and q for the indicator vectors of the 2-cycle's and the triangle's fibers. Then `ker U_j^T={0,p,q,p+q}` and `p+q=1`, the all-ones vector.
- **(G4)** If `r_j=4` and the degrees are X, G_j is connected. Otherwise some component avoids the degree-4 vertex v; it is a 2-cycle or a triangle on degree-2 vertices, leaving v with at most one neighbor, of degree 2, which is impossible for degree 4. So it has rank 3. If the degrees are Y, G_j is either connected (rank 3) or a triple edge on the two degree-3 vertices plus a double edge on the two degree-2 vertices (rank 2). Components have even degree sums and at least two vertices, so these are the only splittings. In the rank-2 case its columns are `q′,q′,p′,p′`, with `p′+q′=1`; hence `1∈col(U_j)`.

**Lemma S.** Let j,k be distinct parties other than A.

- **(S1)** `rank U_j+rank U_k≤5`. This follows from (O) and Sylvester's inequality over F₂.
- **(S2)** j and k cannot both have size 5, since each rank is at least 3.
- **(S3)** j and k cannot both have type X, since each rank is 3.
- **(S4)** j and k cannot both have type Y. If both have rank 3, this contradicts (S1). Otherwise one, say U_j, has rank 2 and `1∈col(U_j)`; by (O), every column of U_k then has even weight. But a Y matrix has two columns of weight 3.
- **(S5)** Suppose `r_j=5` and `r_k=4`. Then (S1) forces rank `U_j=3` and rank `U_k=2`: U_k is a rank-2 Y, and by (O) every column of U_k lies in `ker U_j^T={0,p,q,1}`. The same holds for the columns of any other partner's incidence matrix.

## 7. The eight profiles containing a 5

- **At least three 5's:** `(2,5,5,5)`, `(3,5,5,5)`, `(4,5,5,5)` and `(5,5,5,5)`. Take A of size 5. Two other partners have size 5, contradicting (S2).
- **`(4,4,4,5)`:** take A the size-5 party. Each of the three size-4 partners is of type X or Y; two share a type, contradicting (S3) or (S4).
- **`(3,4,4,5)`:** take A the size-5 party. By (D3), the degrees of both size-4 partners are at most the size-3 partner's size, 3. Both are therefore Y, contradicting (S4).
- **`(4,4,5,5)`:** take A one size-5 party and B the other. By (S3) and (S4), the two size-4 partners have different types, so one of them is X, of rank 3. Together with `rank U_B≥3`, this contradicts (S1).
- **`(3,4,5,5)`:** take A and B of size 5, C of size 4 and D of size 3.
  - By (S5), applied to B and C, G_B is a 2-cycle plus a triangle, and every column of U_D lies in `{p,q,1}`, of weights 2, 3 and 5.
  - By (D3), each D degree is at most `r_C=4`, so weight 5 is excluded.
  - D's degree multiset is `(2,4,4)` or `(3,3,4)`, since it sums to 10 with entries in `[2,4]`. Either way it contains a 4.
  - A weight-4 column is not among p, q, 1, which is a contradiction.

All nine profiles other than `(4,4,4,4)` are excluded, which proves Claim C.

## 8. Exact bounded controls (not the proof)

The primary control is `frontier-20261029-n46-t26-remaining-profiles-check-v2.py`, SHA-256 `83afb6b2f37e16e651d0999a7e7bd23904e8c1dc033d57a252001756e6a83911`. Its receipt, `frontier-20261029-n46-t26-remaining-profiles-check-v2.json`, has SHA-256 `856b1a876e04505575a8c87dffc799c8055655fa0258c9431c99a6fc2f093a23`, 197 LF. The run took 29.3 s; reproduce it with `python3 -B <script> <new.json>`.

The control reconstructs the following from the normal form:

- the ten profiles;
- the 8 balanced cube four-subsets, of which exactly 2 are distance-one-free, both parity classes with full pair projections;
- **all** labeled 5×r incidence matrices with rows of weight 2 and columns of weight at least 2: 1, 210, 2580 and 2040 for r=2,3,4,5. F₂ ranks: all r=5 matrices have rank 3 (600) or 4 (1440). For r=4, X always has rank 3, and the 60 rank-2 matrices are Y with `1` in their column span.

For each size-5 profile, it counts compatible pairs with all `U_j^T U_k` entries in {0,2}. Two independent methods, a compatible-column bitmask test and numpy integer products, must agree pair by pair. The pairwise counts show that each condition is satisfiable on its own, but every profile has **zero** triples satisfying all three conditions:

| profile | BC | BD | CD | triples |
|---|---:|---:|---:|---:|
| 2,5,5,5 | 2040 | 2040 | 0 | 0 |
| 3,4,4,5 | 9720 | 9720 | 8640 | 0 |
| 3,4,5,5 | 9720 | 3600 | 3600 | 0 |
| 3,5,5,5 | 3600 | 3600 | 0 | 0 |
| 4,4,4,5 | 8640 | 8640 | 8640 | 0 |
| 4,4,5,5 | 8640 | 3600 | 3600 | 0 |
| 4,5,5,5 | 3600 | 3600 | 0 | 0 |
| 5,5,5,5 | 0 | 0 | 0 | 0 |

In `(3,4,5,5)`, the 3600 BD pairs include degree-5 size-3 columns equal to `1`. These are removed only by the C-compatibility, matching the use of the cap (D3) in §7.

An earlier run of the same normal form, `…-check-v1.py` (SHA-256 `69838b8d736b3e3739e3982e8ea9e586a328c52b2371741d53afd76bed736440`, receipt `03604b9fe459ad717202b6d48725e0cdb6d90c72cf46ebe25cdce919922275db`), reports the same zero triples and family/rank statistics. It additionally:

- checks the multiplicity formula (M) against 3000 directly built 20-word supports;
- re-derives the `(3,4,4,4)` activity vector `(n_0,…,n_4)=(0,2,24,0,0)`, the zero size-4 singleton count and the per-symbol value `2d−5`.

Its "control without CD" column requires BC and BD for the same B simultaneously; v2 replaces it by separate per-pair counts.

Both are same-harness exact computations, not independent review or a proof certificate.

## 9. Relation to earlier unreviewed author packets

None of the following is relied on here:

- the five-symbol packet `frontier-20261028-n46-five-symbol-noh1-exclusion-v1.md` (SHA-256 `846de587…`), which handled `(4,4,5,5)` through a grouped AME(4,2) step that §7 makes unnecessary;
- the partial packet `…-n46-residual-alphabet-exclusions-v1.md` (`966f125e…`), whose `(3,4,4,4)` argument is re-derived in §4;
- the `(3,4,4,5)` enumeration packet (`96131f55…`).

The present §§4–7 are self-contained apart from (I1).

## 10. Load-bearing steps for review

1. (R1) and the j-independence of d(a).
2. The eight balanced cube subsets and the exclusion of cylinders by (I1).
3. The multiplicity formula (M), and why it needs every A-fiber to be a parity class (true exactly because `r_A=5`).
4. The multigraph rank and cycle-space facts (G5) and (G4), including the rank-2 Y column span.
5. Sylvester's inequality over F₂ and the odd-column argument in (S4).
6. The cap (D3) in `(3,4,4,5)` and `(3,4,5,5)`.
7. The `(3,4,4,4)` count, including that every P word with `x_i=a` is active at i alone or at exactly one further party.
