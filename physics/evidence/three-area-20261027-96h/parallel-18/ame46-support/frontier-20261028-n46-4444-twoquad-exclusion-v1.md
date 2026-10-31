# Candidate exclusion of the two-quad (4,4,4,4) support-46 subcase

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 19:44:05 PDT 2026`; not an exact completion time. **WRITTEN normal-form argument plus exact finite-enumeration candidate**, not independently accepted or formally verified. This excludes only one active-pattern subcase, not the entire `(4,4,4,4)` residual-alphabet profile or N=46.

The reduction to `N=46,t=26,n=10,|E|=20`, P/E terminology, maximal-entry isolation, and all-pair E multiplicity exactly two are conditional on the pinned unreviewed dependencies listed in `frontier-20261028-n46-residual-alphabet-exclusions-v1.md`, SHA-256 `966f125ed180bb48b2848b0900ca37a5f4ee53fab44d5c937050a529cba6e2fc`. No SMT result is used as the proof below.

## 1. Two all-active P words force the zero-fiber normal form

Assume every residual alphabet has size 4. Call a P coordinate active when its symbol belongs to the corresponding E alphabet, and let n_k count P words with k active coordinates. Pair-projection counting gives

`Σ k n_k=4(6·4−10)=56`, `Σ C(k,2)n_k=6(4·4−10)=36`, `Σn_k=26`.

Consequently `n_0+n_3+3n_4=6`. If `n_4=2`, then necessarily

`(n_0,n_1,n_2,n_3,n_4)=(0,0,24,0,2)`.                           (1)

For any active symbol a at party i, let d_i(a) be its number of E-partner values at another party. The number is independent of the partner: the same `6−d_i(a)` maximal P words use a, and their partner symbols are pairwise distinct. The E fiber varies in at least two other coordinates, so `d_i(a)≥2`. Since its partner coordinate has residual alphabet size four, `d_i(a)≤4`.

Let h_i(a) count the two quad-active P words using a. By (1), P words using a are either two-active or quad-active. Their number is `6−d_i(a)`, while their total number of other active-coordinate incidences is `3(4−d_i(a))`. Thus

`−2 h_i(a) = (6−d_i(a))−3(4−d_i(a)) = 2d_i(a)−6`.              (2)

The only possibilities are d=2,h=1 or d=3,h=0. In particular every symbol used by a quad has degree two, neither quad can share a local symbol with the other (h=2 would force d=1), and each party has precisely two degree-two symbols and two degree-three symbols. Relabel them so the two all-active P words are `0000` and `1111`; labels 0,1 have degree two and 2,3 degree three.

The E fiber of a local symbol a has `2d_i(a)` entries, because every E pair value has exactly two extensions. Thus at every party its four local symbol counts are `[4,4,6,6]`. Since P contains 0000 and its maximal coefficient exhausts every pair row, **no E word contains 0 in two coordinates**. We do not need the additional analogous 1111 exclusion.

The 20 E words therefore split into four disjoint zero-fibers F_i of four words, according to the unique coordinate i containing 0, and a four-word zero-free set G. In F_i, every other coordinate has two nonzero values, each appearing twice: the two residual pairs `(0_i,a_j)` have exactly two E extensions apiece. Hence each F_i is a balanced four-point subset of a 2×2×2 cube. In G, the number of occurrences of each nonzero symbol at each coordinate must be even, since the target local counts are even and every zero-fiber contributes that symbol either zero or two times. Also every two-coordinate pair in G has multiplicity at most two.

## 2. Exact finite obstruction

The 4-word G universe uses symbols `{1,2,3}`. Generate all four-element subsets with even local multiplicities and pair multiplicity at most two. There are **6,804**. Party permutations and independent swaps of high symbols 2↔3 preserve all constraints and the local count vector `[4,4,6,6]`. Their action gives **62** orbits; it is safe to examine one representative of each. Each zero-fiber has exactly 216 balanced options: choose a 2-subset of `{1,2,3}` at each of three coordinates, and one of the eight balanced four-point subsets of the resulting cube.

For a representative G, let the target count for symbol s at coordinate j be 4 if s=1, 6 if s=2 or 3, and write `g_{j,s}` for its count in G. Every zero-fiber other than F_j contributes either 0 or 2 occurrences of s at j. Therefore exactly

`m_{j,s}=(target_{j,s}−g_{j,s})/2`                                (3)

of those three fibers must use symbol s at coordinate j.

Pair conditions also factor. For distinct zero positions i,j, let k,l be the other two coordinates. In the pair projection k,l, zero-fibers F_k and F_l contribute only pairs having a zero coordinate, while the nonzero/nonzero pairs receive contributions exactly from G,F_i,F_j. Thus for each nonzero pair (a,b),

`count_G(a,b)+count_Fi(a,b)+count_Fj(a,b) ∈ {0,2}`.                (4)

Conversely, balanced fibers, all six constraints (4), and the symbol targets (3) imply the required pair multiplicity 0 or 2 everywhere: pairs with a zero coordinate are supplied twice by the corresponding balanced zero-fiber, and (4) handles the nonzero/nonzero pairs.

Two separately structured exact programs exhaust this finite normal form:

- A direct compatibility/backtracking implementation explores all 62 G orbits and their balanced F_i catalogs. With the symbol-target pruning and (4), its total search nodes by depth are `62, 1724, 5216, 198` at depths 0,1,2,3; **zero** complete assignments survive.
- An independent meet-in-the-middle implementation constructs the G universe differently, from 21 possible even-multiplicity columns rather than four-subsets; it independently verifies that the 62 supplied orbit representatives cover all 6,804 G candidates with disjoint group images. It generates the 216 balanced F_i options using parity/cylinder formulas rather than four-subset filtering. Pair-compatibility bitset joins produce **1,280** four-fiber cliques before imposing the local symbol targets; **zero** satisfy those targets. These 1,280 intermediate cliques make the unpruned pairwise search nonvacuous.

This excludes the two-quad active pattern if the normal-form deduction and exhaustive programs withstand independent review. The programs use integer operations only; no complex-unitary or SAT solver is required for the exclusion.

## 3. Checks, positive control, and scope

Direct source `frontier-20261028-n46-twoquad-zerofiber-exhaustive-v1.py`, SHA-256 `8068b2c9f61430062b8279e5b575f093ddc56f7ba7cc425549a8de7a7f2b8c9f`; receipt `frontier-20261028-n46-twoquad-zerofiber-exhaustive-v1.json`, SHA-256 `4612fd696383c1093e7222e3fdb14007859f930bf1104bb05d619781a0c1c59`. It records every orbit representative, orbit size, per-fiber candidate count and node count.

Independent meet-in-the-middle source `frontier-20261028-n46-twoquad-zerofiber-mitm-v1.py`, SHA-256 `67392e732f4149928c2be24dc6d184abfbb80d4c4301b687a21ceaccee888521`; receipt SHA-256 `f3e08a632783285201447b786777e2f14dc8f1da45b88397d94fca9489e5a567`. It reads the first receipt's orbit representatives, but independently regenerates the entire G universe and verifies disjoint group-image coverage, uses a separate fiber generator, and performs the separate join. The shared orbit-representative input should be disclosed; the two codes are not different model families or independent human reviews.

The direct source also checks an explicit 20-word positive control from `frontier-20261028-n46-4444-parity-relaxations-v1.json`, SHA-256 `47c3b3d2393027c0b06d7eaf1bc224bb07be40dda7b8debb33b315a08d2bb77a`: it has all local `[4,4,6,6]` counts, no repeated-zero pair, and even pair multiplicities, but deliberately violates the exact multiplicity cap by four overfull pairs of multiplicity four. The source checks those properties directly. This shows that dropping the cap can admit a configuration; the SMT origin of that control is not used to certify the exclusion.

A separate Z3-only diagnostic previously reported the subcase UNSAT without using unitary-overlap constraints; it is neither an AME witness nor a proof certificate and is not an independent review. The global N=46 problem still has the `(4,4,4,4)` cases with fewer than two quad-active P words, as well as the other unresolved alphabet profiles. No global lower bound 47 is claimed.
