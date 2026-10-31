# Four ordinary MOQLS(8) with real-flat members: at most two are nonclassical

**PhysicsMOQLS8-2 / physics-4. WRITTEN AUTHOR CANDIDATE, with a complete exact finite ray/basis census as corroboration; pending disjoint review, parent reading, novelty and formal checks.** This is an all-mixture theorem for a clearly restricted original-object subclass, not an unrestricted four-family resolution.

## 1. Exact statement and original physical scope

Call a QLS(8) *real-flat* if there exists ONE global output ONB for that member in which, after independent cell phases, every entry has all eight coordinates in `{+1/sqrt(8),−1/sqrt(8)}`. Different members may have different flat frames, unrelated entry phases, and arbitrary complex memberwise output unitaries. The SAME 8×8 cell grid, actual row/column ONBs, and ALL six original pair-product ONBs are retained.

**Theorem.** In ANY actual ordinary four-MOQLS(8) family in which ALL FOUR members are real-flat, at most TWO members are nonclassical. More precisely, in the first-row frame of ANY nonclassical member at least **24** of its 64 cells have support size4; every other cell has support size1. This holds for ANY choice of the actual row used as first row. The support-4 cells of the four members are disjoint cell sets, and the first row contains none.

Consequently no four-member all-real-flat family has three or four nonclassical members. A real-flat family with one or two nonclassical members is NOT excluded by this theorem. An arbitrary complex QLS need not be real-flat, so no unrestricted four-family classicality or numerical M(8) claim follows.

The substantive new step beyond the usual support budget is the **16-heavy-cell exclusion**: if a hypothetical member had only16, its exact 4×4 heavy board and all three mates would force TWO companions' 32 actual pair-product vectors into a 16-dimensional space. Together with a separate no-5-heavy-per-line lemma, this upgrades the usual minimum16 to24.

## 2. Every real-flat first-row ONB is a binary character basis

Fix one member and one actual row. In its flat frame its eight rays are mutually orthogonal real sign vectors. By a global diagonal sign unitary make one of them the all-plus vector,then independently rephase each vector so its first coordinate is plus. Represent each ray by the subset of the other seven coordinates where its sign is minus.

The all-plus ray gives the empty set;the other seven supports each have size4. Orthogonality of any two gives symmetric-difference size4,so any two supports meet in exactly2 points. Let A be their 7×7 incidence matrix. Then `A A^T=2I+2J`. Its column sums total28 and their squared sum is `1^T(2I+2J)1=112`;Cauchy has equality,so EVERY column sum is4.

Take any two distinct supports S,T. Their intersection contains two points. Each of those points lies in two further supports among the remaining five,so the total triple-intersection multiplicity over those five supports is4. A remaining support U cannot contain BOTH points:then `(S△T)∩U` would be empty even though both sets have size4 inside a seven-set. Thus each remaining U contains at most one intersection point,and exactly ONE contains neither. For that U,

    |(S△T)∩U|=|S∩U|+|T∩U|−2|S∩T∩U|=4,

so U=S△T. Hence the eight normalized first-row sign vectors form a 3-dimensional binary linear code under entrywise multiplication/XOR.

Choose a basis of that code and regard its seven coordinate columns as labels in F2^3. Every nonzero codeword has weight4. If m_v counts columns of label v,character inversion gives

    m_v = (1/8)[7−Σ_(u≠0)(−1)^(u·v)].

Thus m_0=0 and m_v=1 for every v≠0. Together with the fixed first coordinate0,this identifies the eight coordinates with ALL of F2^3 and the eight first-row rays with its Walsh characters,after a coordinate permutation and row-ray relabelling. This is a self-contained order8 Hadamard-basis argument,not a WLOG assumption about arbitrary complex QLS.

## 3. Every actual entry has support1 or4 in its first-row frame

Normalize any other real-flat entry so its coordinate at the source label0 is plus. It shares a column with one first-row ray and is orthogonal to it. Their sign vectors differ at exactly4 of the eight source coordinates. All first-row Walsh rays have even sign parity,so this entry also has even sign parity.

Write its sign function as `(-1)^q(x)`,x∈F2^3,with q(0)=0 and even total weight. The coefficient of the cubic monomial in the unique multilinear Boolean polynomial q is the parity of its eight values,so q has degree at most2. Its polar is alternating on a three-space and has rank0 or2.

- If rank0,q is linear and its Walsh transform has ONE nonzero coefficient of magnitude8.
- If rank2,its radical is `{0,t}` for nonzero t. Directly squaring the Walsh sum and summing characters over source differences gives

      W_q(v)^2=8[1+(-1)^(q(t)+v·t)].

  Thus exactly FOUR coefficients are nonzero,each of magnitude4;their support is the affine plane `v·t=q(t)`.

After dividing by8 for the actual basis change,every cell is either a **light** coordinate ray,or a **heavy** ray with exactly four nonzero coordinates,each of modulus1/2. No support-size2,3,5,6,7,8 case exists in this subclass. This statement applies independently to each member's own first-row frame and allows arbitrary cell phases.

## 4. Same-cell support disjointness and the heavy-line bound

Independently map each member's first row to the labelled standard basis e_j. For a cell (i,j) in any other row,its coordinate j is zero by its own column ONB. If two members had nonzero kth coordinates at that cell,their product vectors there and at first-row cell (0,k) would have nonzero overlap,contrary to their actual pair-product ONB. Thus all FOUR support sets at every nonfirst-row cell are pairwise disjoint subsets of the other seven coordinates.

One heavy entry uses four coordinates;each of the other three nonzero vectors uses at least one. Hence two heavy entries from different members CANNOT occupy the same cell. The four heavy-cell sets are disjoint.

In any actual row or column of one member containing a heavy vector with support S,|S|=4,no light singleton on S can occur:it would overlap that heavy vector. The ONB resolution of each coordinate k∈S requires total squared weight1. Every heavy contribution on k is exactly1/4,so at least FOUR heavy vectors are required in that line. In particular a nonempty heavy-cell bipartite graph has minimum degree at least4 on every incident row and column. The first row is entirely light.

For any such line with h heavy entries,let U be the union of their affine-plane supports. Every coordinate in U must receive exactly four heavy contributions by the preceding argument;every heavy contributes on four coordinates. Thus `4h=4|U|`,i.e. `h=|U|`. A union of affine planes in F2^3 cannot have size5:two distinct planes are either disjoint or intersect in2 points,so a second distinct plane enlarges a 4-plane union to at least6. Therefore **no row or column has exactly5 heavy entries**. If h=4,all four heavy supports are the SAME plane.

## 5. Exact heavy-cardinality alternatives before the 16 exclusion

If the member is nonclassical,there is at least one heavy entry,otherwise its entire array is contained in its first-row ONB. Let H be its number of heavy cells,and let R,C be the nonempty heavy rows/columns. The minimum-degree4 property gives |R|,|C|≥4 and H≥16. If H<20,then `4 max(|R|,|C|)≤H<20`,so |R|=|C|=4 and the graph is the complete 4×4 board,H=16.

If 20≤H<24,then |R|,|C|≤5. If one side has size4,the other must have size5 and all its vertices have degree4,forcing the other-side vertices to have degree5,which is impossible by §4. If both sides have size5,each nonzero degree is4 or5;degree5 is impossible,so H=20 and the graph is `K_(5,5)` minus a perfect matching.

In this last H=20 case,every heavy row has4 heavy entries and every heavy column has4. By §4 the supports in each heavy row are all the same affine plane;the same holds for each column. The `K_(5,5)` minus a matching is connected,so these planes coincide throughout the heavy board. Every heavy column j excludes coordinate j because of its first-row partner. Thus its five DISTINCT column labels all lie outside one 4-element support plane,impossible in an 8-set. Hence H∈[20,23] is impossible.

All that remains below24 is the exact H=16 4×4 board. No enumeration of boards or selected matrices is used.

## 6. The 16-heavy board is impossible in an actual four-family

Assume H=16 for the selected nonclassical member Q. Its heavy set is a 4×4 board R×C with |R|=|C|=4. Each heavy row and each heavy column contains exactly4 heavy entries,so by §4 all16 share ONE support plane S,|S|=4:row and column planes coincide at their common heavy cells.

For every j∈C the heavy Q vector in column j is orthogonal to first-row e_j,so j∉S. Thus C=S^c as subsets of the selected member's first-row coordinate LABELS. Every heavy Q row has four orthogonal unit vectors supported in S,therefore an ONB of S;its other four entries lie in S^perp. The same holds columnwise. In each nonheavy row,the four entries in columns C lie in S^perp and form an ONB there,so its other four entries lie in S. Hence Q's whole actual grid has the 4+4 block pattern determined by R/R^c and C/S.

At each cell of R×C,Q occupies all four coordinates S. Every one of its THREE mates must exclude those coordinates and the column coordinate j∈S^c;the available set has exactly3 coordinates. Pairwise disjointness and nonzero unit norm force each mate to be a singleton in S^c. This uses all three mates,not a chosen one.

For ANY mate B,its four singleton vectors on an R row over columns C form an ONB of that mate's coordinate 4-space S^c. Its other four entries in that row therefore lie in S. Similarly its four R×C entries in a fixed C column fill S^c,so its remaining entries in that column lie in S. For a row in R^c,the four entries in C are a complete ONB of S,so the other four entries lie in S^c. Thus every mate has the SAME cell-block tag:

    B_(i,j) lies in its own S^c  for (i,j)∈(R×C)∪(R^c×S),
    B_(i,j) lies in its own S    for the other two rectangles.   (5)

Here the coordinate LABELS S/S^c agree because first rows were individually standardized;the physical output spaces of different mates remain independent.

Take ANY TWO of the three mates B,D. There are32 cells in the two rectangles in (5). At all of them,`B_(i,j)⊗D_(i,j)` lies in the 16-dimensional product of their two S^c spaces. But B,D are actual orthogonal QLS,so their 64 same-cell product vectors,including those32,are mutually orthogonal nonzero units. Thirty-two such vectors cannot fit in dimension16. Contradiction. No independently projected/fabricated local bases or common physical unitary is used.

Therefore H=16 is impossible. Combined with §5,every nonclassical member has **H≥24**.

## 7. All-mixture count and exact unresolved scope

For four members,all heavy sets lie in the 56 cells outside the common first row and are pairwise disjoint (§4). Three nonclassical members would contribute at least `3·24=72` distinct heavy cells,impossible. Thus at most TWO members can be nonclassical.

This excludes the q=3 and q=4 mixtures for this entire real-flat subclass,not just affine-character arrays. It does NOT exclude q=1 or q=2 and does not construct a nonclassical q=1/2 family. It does not assume that a general ordinary MOQLS can be made real-flat by unitary isotopy;that is precisely a missing global premise. No M(8),general four-family classicality,finite witness or novelty claim follows.

## 8. Complete exact ray/basis census — finite corroboration only

`frontier-20261028-flat-sign-bases-census-v1.py`,SHA256 **30be00c2dcaed2ba6c552089c063d0c1f98c59c6ab5cf3c4169da9a3cb74ac51**;receipt `frontier-20261028-flat-sign-bases-census-receipt-v1.json`,SHA256 **3bf9d6c23afd719fd4dc60ac3b933c6b679a14d2842223738c515fd3bd24fd81**. Executed once with `python3 -B` and standard-library integers;reported elapsed0.0096s.

For the fixed Walsh first-row frame,the code exhaustively checks all64 even-parity sign rays:8 have support1,56 have support4 of magnitude1/2. It enumerates every orthonormal eight-ray basis via the ENTIRE orthogonality graph and finds **240 bases**,all affine cosets of **30** underlying binary3-spaces. Its heavy-count histogram is `0:1, 4:14, 6:56, 7:64, 8:105`; in particular no line has5 heavy rays. Every coordinate completeness identity is checked;a duplicate-ray negative control is rejected. This confirms the finite support/line claims on one canonical flat frame,not every four-family or the no-go itself.

Separately,a bounded real-flat four-family SAT attempt with a fixed first row and chosen intermediate overlap was inconclusive: the bitvector formula exceeded the768MiB Z3 cap;its compact DIMACS successor later reached the15s Z3 time cap. Neither returned SAT,UNSAT or a proof. Their frozen inputs/receipts remain in this root;they are NOT evidence for the theorem. Three full-Gram floating optimization approaches also did not find an acceptable nonclassical family. No numerical failure is promoted into a mathematical exclusion.

## 9. Trust and continuation boundary

The proof above independently derives its flat-frame/Boolean support/board/dimension steps from the original physical QLS definitions. It does not assume a prior half-split/held outcome or transfer any old numerical solver verdict. Historical process/quarantine records remain historical. The exact ray census is a finite control,not a full mathematical formalization,independent-model/human review or source-priority audit.

Remaining original work: remove the real-flat premise or find a genuine nonclassical ordinary four-family. Even inside this subclass,the q1/q2 cases remain open. For a physical candidate,verify ALL actual row/column ONBs and ALL six pair-product ONBs directly,then perform independent witness/mutation verification;an optimizer's small residual is not a witness.
