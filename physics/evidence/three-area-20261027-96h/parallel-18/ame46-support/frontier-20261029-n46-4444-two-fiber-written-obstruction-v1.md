# An elementary two-fiber obstruction for the N=46, t=26, (4,4,4,4) branch

Owner **PhysicsAME46-2**. Native clock observed before writing: `Thu Oct 29 13:41:08 PDT 2026`; not an asserted completion time. **WRITTEN author candidate**, not independently reviewed, adopted, formally verified, or novelty-cleared. This gives a proposed non-enumerative proof of a branch already dispositioned by a separate finite method; it is not an exclusion of every N=46 state and is not a global support bound.

## 1. Exact statement and input

Suppose a normalized complex AME(4,6) state in one product basis has N=46 nonzero coefficients, exactly t=26 of modulus 1/6, and four residual E symbols at each of the four parties, where E is the set of the other 20 support positions. Then no such state exists, **conditional on the no-Hamming-one lemma** below.

The sole scientific import is the written no-Hamming-one part of `institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-n46-no-hamming-one-parent-v1.md`, SHA-256 `262a5a09276a2d7ef3ce350425236b29af327c99f8ea3ba03cf50878978baac0`: at exactly N=46, t=26, no two E words differ in one coordinate. It carries that disposition's classical no-OLS(6) import. We do **not** use its separately dispositioned 4444 finite-enumeration conclusion. We do not import the pending f182 review, any SAT/solver output, LRAT certificate, held material, or any other candidate. The author has prior exposure to the separately dispositioned branch and is not blind.

Every argument below refers to the **same tensor** and its actual six pair systems. The computation is written elementary counting and unitary row orthogonality; no computer enumeration or selected tensor is a proof premise.

## 2. Pair partition, local degrees, and at most one exceptional party

In each 2|2 cut U=6ψ is a 36×36 unitary. A modulus-one U entry exhausts its row and column norms; its P word is the unique nonzero entry in each line through it. Removing these 26 singleton rows and columns gives a 10×10 unitary with exactly 20 nonzeros and no singleton line. Every residual row and column therefore has exactly two nonzeros. Equivalently, in each of the six pair-coordinate systems E occupies exactly ten values, each with exactly two E extensions, while P occupies each of the other 26 values once.

For a residual symbol a at party i, let p_i(a) count P words using a. For every other party j, the 6 values (a,b) split into p_i(a) P-carried values and `d_i(a)=6-p_i(a)` E-carried values. Thus d_i(a) is independent of j. It is at least 2: if it were 1 then E_a would be constant in each of the other three coordinates, hence consist of a single word, contradicting two E extensions per occupied pair value. Its sum over the four residual symbols is 10. The only degree multisets are

`X=(2,2,2,4)` and `Y=(2,2,3,3)`.

Call a coordinate of a P word active when it belongs to the corresponding residual E alphabet, and let n_k count P words with k active coordinates. At each party there are `6·4−10=14` active P words; at each party pair there are `4·4−10=6` jointly active P words. Hence

`Σ n_k=26,  Σ k n_k=56,  Σ C(k,2)n_k=36`,

which imply `n_0+n_3+3n_4=6` and `n_1=2−3n_0−n_4≤2`.

If a party is X, its degree-4 symbol occurs in exactly 6−4=2 P words. At each other party all four residual values already pair with that symbol in E, so those two P words are active **only** at the X party. Two X parties would require four distinct k=1 words, impossible. Thus there is at most one X party, and at least three Y parties. Choose any Y party A. Its two degree-2 symbols give low fibers L_0,L_1 of four E words each; its two degree-3 symbols give high fibers H_0,H_1 of six E words each.

## 3. Two facts about low fibers and partners

For any E symbol a at A of degree d, its fiber has exactly 2d words: sum the two extensions of each (A,B) pair value. A low fiber L has two values at each of the other three parties, each occurring twice. No two of its words can agree at any two other parties, since then they would differ only at the remaining party. Thus each two-coordinate projection of L is a bijection onto its 2×2 rectangle. For a fixed value at one of those parties, the two words use both values at each of the other two. In particular the two low rows with that fixed A value have **disjoint** column supports in the corresponding cut.

Also, in any cut, each residual row has a **unique partner row with the identical two-column support**. Indeed each of its two columns has exactly one other residual row. The other row through either column must also meet the first row at its second column, since two unitary rows cannot share exactly one nonzero column. Its degree is two, so the supports are identical. The partner is unique because the columns have degree two.

## 4. The two low fibers must be disjoint at two partner parties

For j in {B,C,D}, write S_{j,0}, S_{j,1} for the two j-value sets of L_0,L_1, and put `h_j=|S_{j,0}∩S_{j,1}|∈{0,1,2}`.

**Intersection claim.** For any distinct j,k, if h_j and h_k are both nonzero then both equal 2. Otherwise, the two jk rectangles have intersection of size 1 or 2. In the cut whose columns are jk, each low fiber projects bijectively onto its rectangle. Choose a common column: it lies in exactly one row of each low fiber. If one of h_j,h_k is 1, each such row contains at most one column whose value at that coordinate lies in the intersection, because the row uses both distinct values in its own two-element set. Thus these two distinct rows share exactly one column, impossible by unitary orthogonality.

**Two identical projections are impossible.** Suppose h_j=h_k=2. The low jk rectangles coincide, and each of their four pair values occurs once in each low fiber, hence is saturated at multiplicity 2; no high word can use it. Within either high fiber the jk projection is pair-injective: two words agreeing at A,j,k would differ only at the fourth party. Every other jk value has total E multiplicity 0 or 2, and only H_0,H_1 can carry it, at most once each. Their jk projection sets must therefore be identical. It follows that for every j symbol b,

`d_j(b)=2·1_{b∈S_{j,0}}+2·1_{b∈π_j(H_0)}`,

so every j degree is even. The only even degree multiset of four entries ≥2 summing to 10 is X. Likewise k is X. This contradicts §2's at-most-one-X fact.

Consequently at most one h_j is nonzero: if two were nonzero the intersection claim would make both 2, which the preceding paragraph rules out. Thus two of B,C,D have disjoint low-fiber value sets. Relabel the parties so these are B,C:

`S_{B,0}∩S_{B,1}=∅`,  `S_{C,0}∩S_{C,1}=∅`.

Each disjoint pair partitions its four-symbol alphabet.

## 5. The omissions of the two high fibers split across each partition

Each high fiber has degree 3, so at B it uses three of the four residual symbols and omits exactly one. Call the B omissions of H_0,H_1 respectively b_0,b_1. They are distinct: if both omitted the same b, exactly one low fiber would use b and d_B(b)=1, contrary to §2. The same holds at C, with omissions c_0,c_1.

The two B omissions lie in **different** low sets. If both lay in S_{B,0}, the two high fibers would each use only one symbol of S_{B,0}. Consider a row (A=a_0,C=c) of the AC|BD cut, with c a C value of L_0. Its two BD columns use both B values of S_{B,0}. Its other L_0 row has disjoint BD support; every L_1 row uses only B values of the disjoint set S_{B,1}; and each high row has at most one B value in S_{B,0}. None can be its identical two-column partner, contradiction. The same argument applies if both omissions lay in S_{B,1}. Interchanging B and C proves the split there as well.

Swap H_0,H_1 if necessary, so `b_0∈S_{B,0}` and `b_1∈S_{B,1}`. Then necessarily `c_0∈S_{C,0}` and `c_1∈S_{C,1}`. Indeed, if c_1 lay in S_{C,0}, the pair (b_0,c_1) would occur once in L_0, never in L_1, never in H_0 (which omits b_0), and never in H_1 (which omits c_1): exactly one E extension, forbidden.

## 6. The two low rows have only one possible partner

Write

`S_{B,0}={b_0,b_*}`, `S_{B,1}={b_1,b_†}`, `S_{C,0}={c_0,c_*}`, `S_{C,1}={c_1,c_†}`.

H_0 omits b_0,c_0; H_1 omits b_1,c_1. Within each high fiber, the BC projection is a simple bipartite graph on its three B and three C values, with every vertex of degree 2: each (A,B) and (A,C) value has exactly two E extensions, and no-Hamming-one makes the two opposite values distinct.

Each pair (b_0,c) with c∈S_{C,0} occurs once in L_0, not in L_1 or H_0. Hence H_1 must contain both (b_0,c_0) and (b_0,c_*).

H_0 must contain (b_*,c_*). If it did not, every pair in S_{B,0}×S_{C,0} would have to occur in H_1: each already occurs once in L_0 and must have exactly two extensions. Those four pairs would exhaust the two H_1 incidences at each of its two S_{C,0} vertices. The sole remaining H_1 B vertex b_† would then have only c_† available, not the two distinct C neighbours it requires. Contradiction. Thus (b_*,c_*) is in H_0 and, because L_0 also contains it, cannot be in H_1.

Finally H_1 cannot contain (b_†,c_0): that pair is in neither low rectangle, while H_0 omits c_0, so its E multiplicity would be one. Therefore among **all high AB rows**, only `(H_1,b_0)` has both C values in S_{C,0}. H_0 has only c_* from that set; the H_1 rows at b_* and b_† each miss one of its two values.

In the AB|CD cut, each of the two L_0 AB rows contains both C values of S_{C,0}, so its identical two-column partner must also contain both. The other L_0 row is disjoint from it, and all L_1 rows use only C values of the disjoint set S_{C,1}. Hence both L_0 rows require distinct high partners. There is only one possible high row, `(H_1,b_0)`. A degree-two row cannot be the unique partner of two distinct rows. Contradiction.

This completes the exact-scope branch exclusion. ∎

## 7. Scope and review points

The argument uses no equal-modulus assumption for E, no choice of separate supports for different cuts, and no computational certificate. The no-Hamming-one premise and classical no-OLS(6) boundary are essential to the stated proof. Independent review should check §4's unique-overlap and saturated-rectangle implications, the omission-splitting argument in §5, and the unique high-row count in §6. Other residual-alphabet profiles, N=45, and all sizes ≥48 are outside this result; no global bound or new exact tensor is asserted.
