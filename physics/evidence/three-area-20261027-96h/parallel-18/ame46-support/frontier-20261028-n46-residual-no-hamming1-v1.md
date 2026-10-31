# Candidate: no Hamming-distance-one pair in the 46-support residual

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 19:56:20 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently reviewed, accepted, formally verified, or novelty-cleared. It assumes the conditional reduction for a 46-support AME state to `t=26,n=10,|E|=20`, as in `frontier-20261028-n46-residual-alphabet-exclusions-v1.md`, SHA-256 `966f125ed180bb48b2848b0900ca37a5f4ee53fab44d5c937050a529cba6e2fc`, and the n=2/n=4 exclusions in `frontier-20261028-global-ame46-lower42-review-packet-v2.md`, SHA-256 `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf`. The named no-OLS(6) theorem is inherited. All dependencies remain under review.

## Claim

In the conditional N=46, t=26 case, no two nonmaximal E support words can differ in exactly one coordinate. Consequently every four-point residual fiber on two values in each of the other three coordinates is one of the two binary parity sets; its three pair projections are all full.

The claim is a necessary support property, not a construction or exclusion of N=46.

## 1. A distance-one pair propagates a free two-value fiber

Every pair projection of E has ten values, each with exactly two E extensions. Suppose E contains `(a,b,c,d_0)` and `(a,b,c,d_1)` with `d_0≠d_1`. Write the base triple as `s=(a,b,c)` and `D_0={d_0,d_1}`. Its three base coordinate pairs already have their full two E extensions, so no other base triple in E can share two coordinates with s.

For each base coordinate, there is exactly one other base triple using the same value and both D values. For example, in the AD|BC cut the column `(A=a,D=d_0)` has exactly two nonzeros: one at `(b,c)` and another at some `(b′,c′)`. The column `(a,d_1)` also contains `(b,c)` and has degree two. Two unitary columns with one shared nonzero position must share a second, so it also contains `(b′,c′)`. Thus `s′=(a,b′,c′)` occurs with both d_0,d_1; it differs from s in both other base coordinates because the AB and AC pairs of s are already saturated. The same argument applies when B or C is the shared coordinate.

Close the initial s under these three partner operations. The resulting finite set S has these properties:

- every s∈S occurs in E with exactly the same D-value set D_0;
- no two distinct S triples share two coordinates;
- every base-coordinate value used in S occurs in exactly two S triples;
- the graph joining triples with a common A, B, or C value is simple and 3-regular.

The last assertion follows because each triple has one distinct partner for each of its three coordinate values, and pair-injectivity prevents one neighbor from serving two coordinate types.

## 2. The free component is isolated in every cut

Let `m=|S|`. For any cut, one side is a pair of the base coordinates and the other is the remaining base coordinate paired with D. A base/base pair used by S has its two E extensions already supplied by the two values in D_0. A base/D pair used by S likewise has its two extensions already supplied by the two S triples sharing that base value. No E entry outside `S×D_0` can therefore use either pair. The maximal P entries cannot use any E pair at all. Hence the source residual unitary decomposes in every cut into an isolated m×m block supported on `S×D_0` and a complementary `(10−m)×(10−m)` unitary block.

The S graph is bipartite. For an edge s—s′ sharing a base coordinate, the two residual-unitary columns for the other base pair have the same two D supports. With `r_s=u_{s,d_0}/u_{s,d_1}`, column orthogonality gives `r_{s′}=−1/conjugate(r_s)`. This involution has no fixed nonzero complex point, so there is no odd cycle. A simple 3-regular bipartite graph has at least three vertices on each side, and the degree count gives m even. Since m≤10,

`m∈{6,8,10}`.                                                        (1)

## 3. Every possible component size is impossible

- If m=10, color the bipartite S graph and select d_0 for one color and d_1 for the other. No two selected words share two coordinates: S is pair-injective on the base, and an edge sharing one base coordinate receives opposite D choices. No selected word shares a pair with an existing maximal P word. Thus these ten words complete the 26 P words to OA(36,4,6,2), forbidden by the named no-OLS(6) theorem.
- If m=8, the complementary residual has size 2. In every cut it is a 2×2 unitary with both rows and columns of degree two. Its support therefore satisfies the incidence lemma of the 42-review packet with n=2, which is impossible.
- If m=6, the complementary residual has size 4, again degree two in every pair projection. The n=4 argument of the 42-review packet makes the normalized complementary component an AME(4,2), which the packet rules out by the Pauli spin-flip contradiction.

All possibilities in (1) fail, proving the candidate no-distance-one claim.

## 4. Consequence for four-point fibers

A residual symbol of partner degree two has four E occurrences: each of its two pair rows has exactly two extensions. Each of the other coordinates takes exactly two values twice in this fiber. There are eight balanced four-point subsets of the binary 3-cube: two parity subsets and six cylinders. Every cylinder contains a pair at Hamming distance one, so only the even and odd parity subsets remain. Their projections onto every pair of the three varying coordinates are full 2×2 squares.

## 5. Exact nonvacuity control and limitations

`frontier-20261028-freefiber-component-control-v1.py`, SHA-256 `e302ae4688c473e53412e03cc938cd7d785f874257ef0c5b4a85a197c73b5d29`; receipt SHA-256 `0ff419e62ac26185b580decb82d6e02efcac370a760660b12d036bdb485bef5e`, constructs an exact 12-entry free-fiber component from the six permutations of three symbols and a binary fourth coordinate. All three 6×6 Gram checks are `F F^T=2I`; a single sign flip is rejected, and bipartition selects six pair-injective words. This is a **valid residual component**, not a full AME state. It shows the proof does not falsely assert that every free component is impossible in isolation: the complement and the full P code are essential.

The general no-distance-one statement is the written argument, not a finite search or formal proof. It requires disjoint-block and graph-phase reconstruction in independent review. It does not imply the global N=46 case is closed.
